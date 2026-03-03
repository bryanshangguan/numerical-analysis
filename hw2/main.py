from __future__ import annotations

from fractions import Fraction
from pathlib import Path
from typing import Dict, List

from methods import bisection_method, eval_polynomial, lagrange_interpolation
from problems import ANNUITY_BISECTION_INTERVAL, INTERPOLATION_POINTS, annuity_residual

TOL = 1e-10
MAX_ITER = 500


def format_float(value: float) -> str:
    return f"{value:.10f}"


def format_polynomial(coeffs: list[float], tol: float = 1e-12) -> str:
    terms: list[str] = []
    for power, coeff in enumerate(coeffs):
        if abs(coeff) < tol:
            continue
        abs_coeff = abs(coeff)
        if power == 0:
            body = f"{abs_coeff:.10g}"
        elif power == 1:
            body = "x" if abs(abs_coeff - 1.0) < tol else f"{abs_coeff:.10g}x"
        else:
            body = f"x^{power}" if abs(abs_coeff - 1.0) < tol else f"{abs_coeff:.10g}x^{power}"
        sign = "-" if coeff < 0 else "+"
        terms.append((sign, body))

    if not terms:
        return "0"
    first_sign, first_body = terms[0]
    pieces = [first_body if first_sign == "+" else f"-{first_body}"]
    for sign, body in terms[1:]:
        pieces.append(f" {sign} {body}")
    return "".join(pieces)


def run_problem_1() -> Dict[str, float | int | bool | str]:
    left, right = ANNUITY_BISECTION_INTERVAL
    result = bisection_method(annuity_residual, left, right, tol=TOL, max_iter=MAX_ITER)
    return {
        "converged": result.converged,
        "rate_decimal": result.root,
        "rate_percent": 100.0 * result.root,
        "iterations": result.iterations,
        "residual": result.residual,
        "message": result.message,
        "interval_left": left,
        "interval_right": right,
    }


def run_problem_3() -> List[dict]:
    bounds: List[dict] = []
    e_n = Fraction(1, 3)
    bounds.append({"step": 0, "fraction": e_n, "float": float(e_n)})
    for step in range(1, 4):
        e_n = Fraction(3, 2) * e_n * e_n
        bounds.append({"step": step, "fraction": e_n, "float": float(e_n)})
    return bounds


def lagrange_form_expression(points: list[tuple[float, float]]) -> str:
    terms: list[str] = []
    for i, (xi, yi) in enumerate(points):
        numerator_parts: list[str] = []
        denominator_parts: list[str] = []
        for j, (xj, _) in enumerate(points):
            if i == j:
                continue
            numerator_parts.append(f"(x - {xj:g})")
            denominator_parts.append(f"({xi:g} - {xj:g})")
        numerator = " * ".join(numerator_parts)
        denominator = " * ".join(denominator_parts)
        terms.append(f"{yi:g} * [{numerator}] / [{denominator}]")
    return " + ".join(terms)


def run_problem_4() -> dict:
    coeffs = lagrange_interpolation(INTERPOLATION_POINTS)
    verification = []
    for x, y in INTERPOLATION_POINTS:
        p_x = eval_polynomial(coeffs, x)
        verification.append({"x": x, "expected": y, "computed": p_x, "abs_error": abs(p_x - y)})
    return {
        "points": INTERPOLATION_POINTS,
        "coeffs": coeffs,
        "lagrange_form": lagrange_form_expression(INTERPOLATION_POINTS),
        "simplified": format_polynomial(coeffs),
        "verification": verification,
    }


def print_problem_1(data: Dict[str, float | int | bool | str]) -> None:
    print("Problem 1: Mortgage rate via bisection")
    print(f"Interval: [{data['interval_left']}, {data['interval_right']}]")
    print(f"Converged: {data['converged']}")
    print(f"Annual interest rate (decimal): {format_float(float(data['rate_decimal']))}")
    print(f"Annual interest rate (percent): {format_float(float(data['rate_percent']))}%")
    print(f"Iterations: {data['iterations']}")
    print(f"Residual: {float(data['residual']):.6e}")
    if data["message"]:
        print(f"Note: {data['message']}")


def print_problem_3(bounds: List[dict]) -> None:
    print("\nProblem 3: Newton error upper bounds")
    print("e_{n+1} <= (3/2) * e_n^2, with e_0 < 1/3")
    print("step | exact bound | decimal")
    print("-" * 36)
    for row in bounds:
        print(f"{row['step']:>4} | {row['fraction']!s:<11} | {row['float']:.10f}")


def print_problem_4(data: dict) -> None:
    print("\nProblem 4: Degree-3 interpolation")
    print(f"Lagrange form: {data['lagrange_form']}")
    print(f"Simplified polynomial: P(x) = {data['simplified']}")
    print("Verification at points:")
    print("x | expected | computed | abs_error")
    print("-" * 38)
    for row in data["verification"]:
        print(f"{row['x']:.0f} | {row['expected']:.0f} | {row['computed']:.10f} | {row['abs_error']:.3e}")


def write_results_markdown(problem_1: dict, problem_3: List[dict], problem_4: dict, out_path: Path) -> None:
    lines: list[str] = []
    lines.append("# HW2 Results")
    lines.append("")
    lines.append("## Problem 1")
    lines.append("")
    lines.append("- Equation solved with bisection on annual rate `r`:")
    lines.append("  `L = (12M/r) * [1 - (1 + r/12)^(-12m)]`, with `L=150000`, `M=600`, `m=30`.")
    lines.append(f"- Bracketing interval: `[{problem_1['interval_left']}, {problem_1['interval_right']}]`")
    lines.append(f"- Converged: `{problem_1['converged']}`")
    lines.append(f"- Affordable annual rate (decimal): `{float(problem_1['rate_decimal']):.10f}`")
    lines.append(f"- Affordable annual rate (percent): `{float(problem_1['rate_percent']):.10f}%`")
    lines.append(f"- Iterations: `{problem_1['iterations']}`")
    lines.append(f"- Residual: `{float(problem_1['residual']):.6e}`")
    if problem_1["message"]:
        lines.append(f"- Note: `{problem_1['message']}`")
    lines.append("")
    lines.append("## Problem 2")
    lines.append("")
    lines.append("Written proof is in `hw2/theory.md`.")
    lines.append("")
    lines.append("## Problem 3")
    lines.append("")
    lines.append("Using `e_(n+1) <= (3/2)e_n^2` and worst-case initial bound `e_0 = 1/3`:")
    lines.append("")
    lines.append("| Step | Exact bound | Decimal |")
    lines.append("|---:|---:|---:|")
    for row in problem_3:
        lines.append(f"| e_{row['step']} | {row['fraction']} | {row['float']:.10f} |")
    lines.append("")
    lines.append("## Problem 4")
    lines.append("")
    lines.append(f"- Lagrange form: `{problem_4['lagrange_form']}`")
    lines.append(f"- Simplified polynomial: `P(x) = {problem_4['simplified']}`")
    lines.append("")
    lines.append("| x | Expected y | P(x) | Abs error |")
    lines.append("|---:|---:|---:|---:|")
    for row in problem_4["verification"]:
        lines.append(
            f"| {row['x']:.0f} | {row['expected']:.0f} | {row['computed']:.10f} | {row['abs_error']:.3e} |"
        )
    lines.append("")
    out_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    hw2_dir = Path(__file__).resolve().parent
    p1 = run_problem_1()
    p3 = run_problem_3()
    p4 = run_problem_4()

    print_problem_1(p1)
    print_problem_3(p3)
    print_problem_4(p4)

    report_path = hw2_dir / "results.md"
    write_results_markdown(p1, p3, p4, report_path)
    print(f"\nWrote markdown report: {report_path}")
    print("\nGenerated markdown report contents:\n")
    print(report_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
