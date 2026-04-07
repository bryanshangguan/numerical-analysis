from __future__ import annotations

import math
from pathlib import Path
from typing import List, Dict

from methods import newton_divided_differences, evaluate_newton_polynomial
from problems import f_exp, get_evaluation_nodes, get_interpolation_nodes

def format_float(value: float) -> str:
    return f"{value:.6e}"

def run_problem_2() -> List[Dict[str, int | float]]:
    ns = [2, 4, 8, 16, 32]
    t_nodes = get_evaluation_nodes(501)
    results: List[Dict[str, int | float]] = []

    for n in ns:
        x_nodes = get_interpolation_nodes(n)
        y_nodes = [f_exp(x) for x in x_nodes]
        
        coefs = newton_divided_differences(x_nodes, y_nodes)

        max_err = 0.0
        for t in t_nodes:
            p_t = evaluate_newton_polynomial(coefs, x_nodes, t)
            err = abs(f_exp(t) - p_t)
            if err > max_err:
                max_err = err

        results.append({
            "n": n,
            "E_n": max_err
        })

    return results

def print_problem_2(results: List[Dict[str, int | float]]) -> None:
    print("Problem 2: Newton Interpolation Error for f(x) = e^x on [-1, 1]")
    print(f"{'n':>4} | {'E_n (Max Error)':<15}")
    print("-" * 22)
    for row in results:
        print(f"{row['n']:>4} | {format_float(float(row['E_n'])):<15}")

def plot_results(results: List[Dict[str, int | float]], out_path: Path) -> None:
    try:
        import matplotlib.pyplot as plt
        ns = [row['n'] for row in results]
        errors = [row['E_n'] for row in results]

        plt.figure(figsize=(8, 5))
        plt.plot(ns, errors, marker='o', linestyle='-', color='b')
        plt.yscale('log')
        plt.xlabel('Degree n')
        plt.ylabel('Maximum Error $E_n$ (Log Scale)')
        plt.title('Max Interpolation Error vs. Polynomial Degree n for $e^x$')
        plt.grid(True, which="both", ls="--", alpha=0.7)
        plt.xticks(ns)
        
        plt.savefig(out_path)
        print(f"\nSaved interpolation error plot to: {out_path}")
    except ImportError:
        print("\nNote: 'matplotlib' is not installed. Skipping plot generation.")

def write_results_markdown(results: List[Dict[str, int | float]], out_path: Path) -> None:
    lines: list[str] = []
    lines.append("# HW3 Results")
    lines.append("")
    lines.append("## Problem 2")
    lines.append("")
    lines.append("Maximum error $E_n = \\max_{0 \\le k \\le 500} |f(t_k) - p_n(t_k)|$ sampled at 501 points on $[-1, 1]$.")
    lines.append("")
    lines.append("| n | Maximum Error ($E_n$) |")
    lines.append("|---:|---:|")
    for row in results:
        lines.append(f"| {row['n']} | {format_float(float(row['E_n']))} |")
    lines.append("")
    
    out_path.write_text("\n".join(lines), encoding="utf-8")

def main() -> None:
    hw3_dir = Path(__file__).resolve().parent
    
    p2_results = run_problem_2()
    print_problem_2(p2_results)

    report_path = hw3_dir / "results.md"
    write_results_markdown(p2_results, report_path)
    
    print(f"\nWrote markdown report: {report_path}")
    print("\nGenerated markdown report contents:\n")
    print(report_path.read_text(encoding="utf-8"))

if __name__ == "__main__":
    main()