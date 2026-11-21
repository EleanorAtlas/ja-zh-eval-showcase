#!/usr/bin/env python3
"""Inter-rater agreement for ordinal 1-5 scores.

Reports Cohen's kappa (unweighted), linearly weighted kappa, quadratically
weighted kappa, and a small variance report. Designed for two raters and a
handful to a few thousand items. Only the standard library is required;
numpy is optional and is used only for a self-test cross-check.

Requires Python 3.8 or later.

Usage
-----
    python KAPPA-SCRIPT.py ratings.csv
    python KAPPA-SCRIPT.py ratings.csv --json
    python KAPPA-SCRIPT.py ratings.csv --categories 1,2,3,4,5
    python KAPPA-SCRIPT.py --selftest

Input
-----
A UTF-8 CSV with a header and three columns:

    item_id,rater_a,rater_b
    JA-001,4,3
    JA-002,5,5
    JA-003,,4          <- excluded listwise and reported

- `item_id` must be unique and non-empty.
- Scores must be integers in the category set (default 1-5). Categories do
  not have to be consecutive; distances are measured on the values.
- A blank score in either rater column excludes that row from the
  agreement calculation; the row is listed in the report.
- Extra columns are ignored. A UTF-8 BOM is tolerated.

Output
------
Human-readable text by default; `--json` emits the same data as JSON.
Kappa is reported as `null` / `undefined` when it is mathematically
undefined (for example, when both raters used only one category).

What the numbers mean
---------------------
- Observed agreement: the proportion of items on which the raters agree
  exactly (unweighted) or the weighted proportion (weighted variants).
- Expected agreement: agreement expected from the marginal distributions
  if the raters were independent.
- Cohen's kappa: (observed - expected) / (1 - expected). It corrects for
  chance agreement but is sensitive to prevalence and to small n.
- Weighted kappa: the same correction with partial credit for near misses.
  Linear weights penalize a gap by the gap divided by the observed range;
  quadratic weights square that ratio. Quadratic is the usual choice for
  ordinal scales, but it is a choice, not a law.

This script is a reporting aid, not a significance test. A kappa on 20
items is unstable; always report n, the score distribution, and the item-level
disagreements alongside it. Variance in this report is population variance
(divide by n), not sample variance; SD is its square root.

Self-test
---------
`--selftest` runs a 10-item fixture with known values:
unweighted 0.7500, linear 0.8649, quadratic 0.9412. If numpy is installed,
the self-test also cross-checks the matrix arithmetic against a vectorized
implementation. numpy is optional; the main path uses only the standard
library.

Exit codes
----------
0  report produced
2  bad input, bad arguments, or failed self-test
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import sys
from typing import Iterable, Optional, Sequence

DEFAULT_CATEGORIES = (1, 2, 3, 4, 5)
WEIGHT_KINDS = ("unweighted", "linear", "quadratic")


# ---------------------------------------------------------------------------
# Input
# ---------------------------------------------------------------------------

def load_wide(path: str) -> tuple[list[tuple[str, int, int]], list[dict]]:
    """Load a wide CSV with item_id,rater_a,rater_b.

    Returns (pairs, excluded). Excluded rows are kept for the report rather
    than silently dropped, because a missing score is itself a finding.
    """
    pairs: list[tuple[str, int, int]] = []
    excluded: list[dict] = []
    seen: set[str] = set()

    with open(path, encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        if reader.fieldnames is None:
            raise ValueError("CSV has no header row")

        fields = {name.strip() for name in reader.fieldnames if name is not None}
        missing = {"item_id", "rater_a", "rater_b"} - fields
        if missing:
            raise ValueError(
                "missing column(s): " + ", ".join(sorted(missing))
                + "; expected item_id,rater_a,rater_b"
            )

        for lineno, row in enumerate(reader, start=2):
            item = (row.get("item_id") or "").strip()
            a_raw = (row.get("rater_a") or "").strip()
            b_raw = (row.get("rater_b") or "").strip()

            if not item and not a_raw and not b_raw:
                continue
            if not item:
                raise ValueError(f"line {lineno}: empty item_id")
            if item in seen:
                raise ValueError(f"line {lineno}: duplicate item_id {item!r}")
            seen.add(item)

            if not a_raw or not b_raw:
                excluded.append(
                    {
                        "item_id": item,
                        "rater_a": a_raw or None,
                        "rater_b": b_raw or None,
                        "reason": "missing score",
                    }
                )
                continue

            try:
                a = int(a_raw)
                b = int(b_raw)
            except ValueError as exc:
                raise ValueError(
                    f"line {lineno}: scores must be integers, got "
                    f"{a_raw!r} and {b_raw!r}"
                ) from exc

            pairs.append((item, a, b))

    if not pairs:
        raise ValueError("no complete rating pairs found")
    return pairs, excluded


def validate_categories(
    pairs: Sequence[tuple[str, int, int]], categories: Sequence[int]
) -> None:
    allowed = set(categories)
    bad = [(item, a, b) for item, a, b in pairs if a not in allowed or b not in allowed]
    if bad:
        item, a, b = bad[0]
        raise ValueError(
            f"item {item!r} has score {a!r}/{b!r} outside categories "
            f"{list(categories)}"
        )


# ---------------------------------------------------------------------------
# Kappa
# ---------------------------------------------------------------------------

def confusion_matrix(
    pairs: Sequence[tuple[str, int, int]], categories: Sequence[int]
) -> list[list[int]]:
    """Rows = rater_a, columns = rater_b."""
    index = {value: i for i, value in enumerate(categories)}
    matrix = [[0 for _ in categories] for _ in categories]
    for _, a, b in pairs:
        matrix[index[a]][index[b]] += 1
    return matrix


def weight_matrix(categories: Sequence[int], kind: str) -> list[list[float]]:
    """Agreement weights on the diagonal (1.0) and off-diagonal (partial).

    Distances are measured on the category values, not on their positions in
    the sequence, so a non-consecutive set such as (1, 2, 5) is weighted
    correctly. Linear weights divide the distance by the observed range;
    quadratic weights square that ratio.
    """
    k = len(categories)
    if k < 2:
        raise ValueError("at least two categories are required")
    if kind == "unweighted":
        return [[1.0 if i == j else 0.0 for j in range(k)] for i in range(k)]
    span = max(categories) - min(categories)
    if span <= 0:
        raise ValueError("categories must span more than one value")
    distances = [
        [abs(categories[i] - categories[j]) / span for j in range(k)]
        for i in range(k)
    ]
    if kind == "linear":
        return [[1.0 - d for d in row] for row in distances]
    if kind == "quadratic":
        return [[1.0 - d * d for d in row] for row in distances]
    raise ValueError(f"unknown weight kind {kind!r}")


def kappa_from_matrix(
    matrix: Sequence[Sequence[int]], weights: Sequence[Sequence[float]]
) -> tuple[Optional[float], float, float]:
    """Return (kappa, observed weighted agreement, expected weighted agreement)."""
    k = len(matrix)
    n = sum(sum(row) for row in matrix)
    if n == 0:
        raise ValueError("empty confusion matrix")

    row_sums = [sum(matrix[i][j] for j in range(k)) for i in range(k)]
    col_sums = [sum(matrix[i][j] for i in range(k)) for j in range(k)]

    observed_num = sum(
        weights[i][j] * matrix[i][j] for i in range(k) for j in range(k)
    )
    expected_num = sum(
        weights[i][j] * row_sums[i] * col_sums[j]
        for i in range(k)
        for j in range(k)
    )

    observed = observed_num / n
    expected = expected_num / (n * n)

    if math.isclose(1.0, expected, rel_tol=0.0, abs_tol=1e-12):
        return None, observed, expected

    return (observed - expected) / (1.0 - expected), observed, expected


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------

def _mean(values: Sequence[float]) -> float:
    return sum(values) / len(values)


def _pvar(values: Sequence[float]) -> float:
    """Population variance (divide by n), not the sample variance."""
    if not values:
        raise ValueError("empty sequence")
    mu = _mean(values)
    return sum((x - mu) ** 2 for x in values) / len(values)


def _summary(values: Sequence[int]) -> dict:
    return {
        "n": len(values),
        "mean": _mean(values),
        "variance": _pvar(values),
        "sd": math.sqrt(_pvar(values)),
        "min": min(values),
        "max": max(values),
    }


def build_report(
    pairs: Sequence[tuple[str, int, int]],
    categories: Sequence[int] = DEFAULT_CATEGORIES,
    excluded: Iterable[dict] = (),
) -> dict:
    """Compute the full agreement report as a JSON-serializable dict."""
    validate_categories(pairs, categories)
    matrix = confusion_matrix(pairs, categories)

    kappa: dict[str, Optional[float]] = {}
    agreement: dict[str, dict[str, float]] = {}
    for kind in WEIGHT_KINDS:
        value, observed, expected = kappa_from_matrix(matrix, weight_matrix(categories, kind))
        kappa[kind] = value
        agreement[kind] = {"observed": observed, "expected": expected}

    a_scores = [a for _, a, _ in pairs]
    b_scores = [b for _, _, b in pairs]
    diffs = [a - b for _, a, b in pairs]
    disagreements = [
        {
            "item_id": item,
            "rater_a": a,
            "rater_b": b,
            "difference": a - b,
        }
        for item, a, b in pairs
        if a != b
    ]
    disagreements.sort(key=lambda row: (-abs(row["difference"]), row["item_id"]))

    return {
        "n_items": len(pairs),
        "categories": list(categories),
        "excluded": list(excluded),
        "kappa": kappa,
        "agreement": agreement,
        "confusion_matrix": matrix,
        "raters": {
            "rater_a": _summary(a_scores),
            "rater_b": _summary(b_scores),
        },
        "differences": {
            "mean": _mean(diffs),
            "mean_absolute": _mean([abs(d) for d in diffs]),
            "max_absolute": max(abs(d) for d in diffs),
            "variance": _pvar(diffs),
            "sd": math.sqrt(_pvar(diffs)),
            "nonzero": sum(1 for d in diffs if d != 0),
            "gap_ge_2": sum(1 for d in diffs if abs(d) >= 2),
        },
        "disagreements": disagreements,
    }


def _fmt(value: Optional[float]) -> str:
    return "undefined" if value is None else f"{value:.4f}"


def render_text(report: dict) -> str:
    cats = ", ".join(str(c) for c in report["categories"])
    n = report["n_items"]
    lines = [
        "Inter-rater agreement (2 raters)",
        f"  {'categories:':<22}{cats}",
        f"  {'items scored:':<22}{n}",
        f"  {'items excluded:':<22}{len(report['excluded'])}",
        "",
        "Agreement",
        f"  {'exact agreement:':<22}{_fmt(report['agreement']['unweighted']['observed'])}",
        f"  {'expected agreement:':<22}{_fmt(report['agreement']['unweighted']['expected'])}",
        "",
        "Kappa",
        f"  {'unweighted kappa:':<22}{_fmt(report['kappa']['unweighted'])}",
        f"  {'linear weighted:':<22}{_fmt(report['kappa']['linear'])}",
        f"  {'quadratic weighted:':<22}{_fmt(report['kappa']['quadratic'])}",
        "",
        "Score distribution",
    ]

    for key, label in (("rater_a", "A"), ("rater_b", "B")):
        row = report["raters"][key]
        lines.append(
            f"  rater {label}: n={row['n']} mean={row['mean']:.4f} "
            f"sd={row['sd']:.4f} min={row['min']} max={row['max']}"
        )

    diff = report["differences"]
    lines += [
        "",
        "Differences (A - B)",
        f"  mean={diff['mean']:.4f}  mean|d|={diff['mean_absolute']:.4f}  "
        f"max|d|={diff['max_absolute']}  variance={diff['variance']:.4f}  "
        f"sd={diff['sd']:.4f}",
        f"  disagreements: {diff['nonzero']} / {n}; gaps of 2+: {diff['gap_ge_2']}",
    ]

    if report["excluded"]:
        lines += ["", "Excluded rows"]
        for row in report["excluded"]:
            lines.append(
                f"  {row['item_id']}  a={row['rater_a']}  b={row['rater_b']}  "
                f"({row['reason']})"
            )

    if report["disagreements"]:
        lines += ["", "Items with disagreement"]
        for row in report["disagreements"]:
            lines.append(
                f"  {row['item_id']}  a={row['rater_a']}  b={row['rater_b']}  "
                f"d={row['difference']:+d}"
            )
    else:
        lines += ["", "No disagreements."]

    lines += [
        "",
        "Note: kappa is prevalence-sensitive and unstable on small n. Report n,",
        "the distribution, and the item-level disagreements with the coefficient.",
    ]
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Optional numpy cross-check
# ---------------------------------------------------------------------------

def _numpy_kappa(matrix: Sequence[Sequence[int]], weights: Sequence[Sequence[float]]) -> float:
    """Vectorized kappa, used only by the self-test when numpy is present."""
    import numpy as np  # imported lazily on purpose

    arr = np.asarray(matrix, dtype=float)
    w = np.asarray(weights, dtype=float)
    n = arr.sum()
    row = arr.sum(axis=1)
    col = arr.sum(axis=0)
    observed = float((w * arr).sum() / n)
    expected = float((w * np.outer(row, col)).sum() / (n * n))
    return (observed - expected) / (1.0 - expected)


# ---------------------------------------------------------------------------
# Self-test
# ---------------------------------------------------------------------------

SELFTEST_PAIRS = [
    ("S01", 1, 1),
    ("S02", 2, 2),
    ("S03", 3, 3),
    ("S04", 4, 4),
    ("S05", 5, 5),
    ("S06", 1, 2),
    ("S07", 2, 2),
    ("S08", 3, 3),
    ("S09", 4, 4),
    ("S10", 5, 4),
]


def run_selftest() -> None:
    report = build_report(SELFTEST_PAIRS, DEFAULT_CATEGORIES)
    expected = {
        "unweighted": 0.75,
        "linear": 0.8648648648648649,
        "quadratic": 0.9411764705882353,
    }
    for kind, want in expected.items():
        got = report["kappa"][kind]
        if got is None or not math.isclose(got, want, rel_tol=0.0, abs_tol=1e-12):
            raise AssertionError(f"selftest {kind}: expected {want}, got {got}")

    if abs(report["agreement"]["unweighted"]["observed"] - 0.8) > 1e-12:
        raise AssertionError("selftest: exact agreement should be 0.8")
    if abs(report["differences"]["mean_absolute"] - 0.2) > 1e-12:
        raise AssertionError("selftest: mean absolute difference should be 0.2")
    if report["differences"]["gap_ge_2"] != 0:
        raise AssertionError("selftest: no gap of 2 or more expected")

    w = weight_matrix((1, 2, 5), "linear")
    if not math.isclose(w[0][1], 0.75, rel_tol=0.0, abs_tol=1e-12):
        raise AssertionError(
            "selftest: non-consecutive categories should scale to the observed range"
        )

    undefined = build_report([("X1", 5, 5), ("X2", 5, 5)], DEFAULT_CATEGORIES)
    if undefined["kappa"]["unweighted"] is not None:
        raise AssertionError("selftest: kappa should be undefined for one category")

    try:
        import numpy as np  # noqa: F401
    except ImportError:
        np = None

    if np is not None:
        matrix = confusion_matrix(SELFTEST_PAIRS, DEFAULT_CATEGORIES)
        for kind in WEIGHT_KINDS:
            got = _numpy_kappa(matrix, weight_matrix(DEFAULT_CATEGORIES, kind))
            want = report["kappa"][kind]
            if want is None or not math.isclose(got, want, rel_tol=0.0, abs_tol=1e-12):
                raise AssertionError(
                    f"selftest numpy {kind}: stdlib={want}, numpy={got}"
                )
        print("selftest OK (numpy cross-check passed)")
    else:
        print("selftest OK (numpy not installed; stdlib path only)")

    print(
        "  unweighted=0.7500  linear=0.8649  quadratic=0.9412  "
        "observed=0.8000  mean|d|=0.2000"
    )


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Cohen's kappa, weighted kappa, and a variance report for two raters."
    )
    parser.add_argument("file", nargs="?", help="CSV with item_id,rater_a,rater_b")
    parser.add_argument(
        "--categories",
        default="1,2,3,4,5",
        help="comma-separated integer categories (default: 1,2,3,4,5)",
    )
    parser.add_argument("--json", action="store_true", help="emit JSON instead of text")
    parser.add_argument("--selftest", action="store_true", help="run the built-in test")
    return parser.parse_args(argv)


def parse_categories(raw: str) -> tuple[int, ...]:
    try:
        values = sorted({int(part.strip()) for part in raw.split(",") if part.strip()})
    except ValueError as exc:
        raise ValueError(f"--categories must be integers, got {raw!r}") from exc
    if len(values) < 2:
        raise ValueError("--categories needs at least two distinct values")
    return tuple(values)


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_args(argv)

    if args.selftest:
        try:
            run_selftest()
        except AssertionError as exc:
            print(f"selftest FAILED: {exc}", file=sys.stderr)
            return 2
        return 0

    if not args.file:
        print("error: provide a CSV file or use --selftest", file=sys.stderr)
        return 2

    try:
        categories = parse_categories(args.categories)
        pairs, excluded = load_wide(args.file)
        validate_categories(pairs, categories)
        report = build_report(pairs, categories, excluded)
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(render_text(report))
    return 0


if __name__ == "__main__":
    sys.exit(main())
