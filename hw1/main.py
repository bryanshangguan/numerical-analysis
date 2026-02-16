from __future__ import annotations

import math
from pathlib import Path
from typing import List

from problems import PROBLEM_SET, fixed_point_g, fixed_point_g_prime
from root_methods import MethodResult, bisection_method, newton_method, secant_method

TOL = 1e-6
FIXED_POINT_TARGET = 1e-5
MAX_ITER = 500

def format_float(value: float) -> str:
    if math.isnan(value):
        return "nan"
    if math.isinf(value):
        return "inf"
    return f"{value:.10f}"

def run_problem_1() -> List[dict]:
    rows: List[dict] = []
    for problem in PROBLEM_SET:
        method_results: List[MethodResult] = []
        method_results.append(newton_method(problem.f, problem.df, problem.x0, tol=TOL, max_iter=MAX_ITER))
        method_results.append(secant_method(problem.f, problem.x0, problem.secant_x1, tol=TOL, max_iter=MAX_ITER))

        if problem.bisection_interval is not None:
            left, right = problem.bisection_interval
            method_results.append(bisection_method(problem.f, left, right, tol=TOL, max_iter=MAX_ITER))
        else:
            method_results.append(
                MethodResult(
                    method="Bisection",
                    converged=False,
                    root=problem.x0,
                    iterations=0,
                    residual=float("inf"),
                    history=[],
                    message="No valid bracketing interval: f(x) = 2 - ln(x)/x has no real root.",
                )
            )

        for result in method_results:
            rows.append(
                {
                    "label": problem.label,
                    "expression": problem.expression,
                    "method": result.method,
                    "converged": result.converged,
                    "root": result.root,
                    "iterations": result.iterations,
                    "residual": result.residual,
                    "message": result.message,
                }
            )
    return rows

def fixed_point_reference(x0: float = 1.5, tol: float = 1e-14, max_iter: int = 5000) -> float:
    x_n = x0
    for _ in range(max_iter):
        x_next = fixed_point_g(x_n)
        if abs(x_next - x_n) < tol:
            return x_next
        x_n = x_next
    return x_n

def fixed_point_iterations_to_error(x0: float, alpha_ref: float, target_error: float) -> int:
    x_n = x0
    for n in range(1, 5000):
        x_n = fixed_point_g(x_n)
        if abs(x_n - alpha_ref) < target_error:
            return n
    return -1

def fixed_point_theory_bound(x0: float, target_error: float) -> int:
    l_const = max(abs(fixed_point_g_prime(1.0)), abs(fixed_point_g_prime(2.0)))
    x1 = fixed_point_g(x0)
    numerator = target_error * (1.0 - l_const)
    denominator = abs(x1 - x0)
    if denominator == 0.0:
        return 0
    n_real = math.log(numerator / denominator) / math.log(l_const)
    return max(0, math.ceil(n_real))

def run_problem_3() -> dict:
    alpha_ref = fixed_point_reference()
    x0_values = [1.0, 1.5, 2.0]
    observed = {
        x0: fixed_point_iterations_to_error(x0, alpha_ref, FIXED_POINT_TARGET) for x0 in x0_values
    }
    theory = {x0: fixed_point_theory_bound(x0, FIXED_POINT_TARGET) for x0 in x0_values}
    l_const = max(abs(fixed_point_g_prime(1.0)), abs(fixed_point_g_prime(2.0)))
    return {
        "alpha_ref": alpha_ref,
        "l_const": l_const,
        "target": FIXED_POINT_TARGET,
        "x0_values": x0_values,
        "observed": observed,
        "theory": theory,
    }

def print_problem_1(rows: List[dict]) -> None:
    print("Problem 1: Root-finding comparison (tol = 1e-6 on |x_{n+1} - x_n|)")
    print(
        "label | method    | converged | root          | iterations | residual      | note"
    )
    print("-" * 88)
    for row in rows:
        note = row["message"] if row["message"] else "-"
        print(
            f"{row['label']:>5} | {row['method']:<9} | {str(row['converged']):<9} | "
            f"{format_float(row['root']):<13} | {row['iterations']:<10} | "
            f"{format_float(row['residual']):<13} | {note}"
        )

def print_problem_3(data: dict) -> None:
    print("\nProblem 3: Fixed-point iteration x_(n+1) = 1 + exp(-x_n)")
    print(f"Reference fixed point alpha ~= {format_float(data['alpha_ref'])}")
    print(f"Lipschitz constant estimate L = max|g'(x)| on [1,2] = {format_float(data['l_const'])}")
    print(f"Target accuracy: {data['target']:.0e}")
    print("x0    | predicted_n | observed_n")
    print("-" * 34)
    for x0 in data["x0_values"]:
        print(f"{x0:<5} | {data['theory'][x0]:<11} | {data['observed'][x0]}")

def write_results_markdown(rows: List[dict], p3: dict, out_path: Path) -> None:
    lines: List[str] = []
    lines.append("# HW1 Results")
    lines.append("")
    lines.append("## Problem 1")
    lines.append("")
    lines.append("| Function | Method | Converged | Root | Iterations | Residual | Note |")
    lines.append("|---|---|---:|---:|---:|---:|---|")
    for row in rows:
        lines.append(
            f"| {row['label']}: `{row['expression']}` | {row['method']} | "
            f"{row['converged']} | {format_float(row['root'])} | {row['iterations']} | "
            f"{format_float(row['residual'])} | {row['message'] or '-'} |"
        )

    lines.append("")
    lines.append("## Problem 3")
    lines.append("")
    lines.append(f"- Fixed-point map: `g(x) = 1 + exp(-x)`")
    lines.append(f"- Reference fixed point: `{format_float(p3['alpha_ref'])}`")
    lines.append(f"- Contraction constant on `[1,2]`: `L = {format_float(p3['l_const'])}`")
    lines.append(f"- Target accuracy: `{p3['target']:.0e}`")
    lines.append("")
    lines.append("| x0 | Predicted iterations (theory) | Observed iterations |")
    lines.append("|---:|---:|---:|")
    for x0 in p3["x0_values"]:
        lines.append(f"| {x0} | {p3['theory'][x0]} | {p3['observed'][x0]} |")
    lines.append("")

    out_path.write_text("\n".join(lines), encoding="utf-8")

def main() -> None:
    hw1_dir = Path(__file__).resolve().parent
    rows = run_problem_1()
    p3 = run_problem_3()
    print_problem_1(rows)
    print_problem_3(p3)
    write_results_markdown(rows, p3, hw1_dir / "results.md")
    print(f"\nWrote markdown report: {hw1_dir / 'results.md'}")

if __name__ == "__main__":
    main()
