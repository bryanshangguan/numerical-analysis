from __future__ import annotations

from pathlib import Path

from methods import (
    lu_factorization,
    matrix_multiply,
    matrix_vector_product,
    max_abs_matrix,
    max_abs_vector,
    solve_lu,
    vector_subtract,
)
from problems import PROBLEM_2_MATRIX, PROBLEM_2_VECTOR, problem_1_operation_counts

def format_float(value: float) -> str:
    return f"{value:.10f}"

def format_vector(values: list[float]) -> str:
    return "[" + ", ".join(format_float(value) for value in values) + "]"

def format_matrix_rows(matrix: list[list[float]]) -> list[str]:
    return ["[" + ", ".join(format_float(value) for value in row) + "]" for row in matrix]

def run_problem_1() -> list[dict[str, str]]:
    return problem_1_operation_counts()

def run_problem_2() -> dict:
    lu_result = lu_factorization(PROBLEM_2_MATRIX)
    solution = solve_lu(lu_result.l_matrix, lu_result.u_matrix, PROBLEM_2_VECTOR)
    reconstructed = matrix_multiply(lu_result.l_matrix, lu_result.u_matrix)
    reconstruction_error = [
        [reconstructed[i][j] - PROBLEM_2_MATRIX[i][j] for j in range(len(PROBLEM_2_MATRIX[0]))]
        for i in range(len(PROBLEM_2_MATRIX))
    ]
    residual = vector_subtract(matrix_vector_product(PROBLEM_2_MATRIX, solution), PROBLEM_2_VECTOR)

    return {
        "a_matrix": PROBLEM_2_MATRIX,
        "b_vector": PROBLEM_2_VECTOR,
        "l_matrix": lu_result.l_matrix,
        "u_matrix": lu_result.u_matrix,
        "solution": solution,
        "residual": residual,
        "residual_max": max_abs_vector(residual),
        "reconstruction_error": reconstruction_error,
        "reconstruction_error_max": max_abs_matrix(reconstruction_error),
    }

def print_problem_1(rows: list[dict[str, str]]) -> None:
    print("Problem 1: Operation counts")
    for row in rows:
        print(f"- {row['operation']}")
        print(
            f"  multiplications = {row['multiplications']}, "
            f"additions = {row['additions']}, total = {row['total']}"
        )

def print_problem_2(data: dict) -> None:
    print("\nProblem 2: LU factorization and solve")
    print(f"Solution x = {format_vector(data['solution'])}")
    print(f"Max |Ax - b| = {data['residual_max']:.6e}")
    print(f"Max |LU - A| = {data['reconstruction_error_max']:.6e}")

def write_results_markdown(problem_1: list[dict[str, str]], problem_2: dict, out_path: Path) -> None:
    lines: list[str] = []
    lines.append("# HW4 Results")
    lines.append("")
    lines.append("## Problem 1")
    lines.append("")
    lines.append("| Computation | Multiplications | Additions | Total operations |")
    lines.append("|---|---:|---:|---:|")
    for row in problem_1:
        lines.append(
            f"| {row['operation']} | {row['multiplications']} | {row['additions']} | {row['total']} |"
        )
    lines.append("")
    lines.append("## Problem 2")
    lines.append("")
    lines.append("- Solved the system `Ax = b` using LU factorization without pivoting.")
    lines.append(f"- Solution vector: `{format_vector(problem_2['solution'])}`")
    lines.append(f"- Maximum reconstruction error `max |LU - A|`: `{problem_2['reconstruction_error_max']:.6e}`")
    lines.append(f"- Maximum residual `max |Ax - b|`: `{problem_2['residual_max']:.6e}`")
    lines.append("")
    lines.append("### L matrix")
    lines.append("")
    for row in format_matrix_rows(problem_2["l_matrix"]):
        lines.append(f"- `{row}`")
    lines.append("")
    lines.append("### U matrix")
    lines.append("")
    for row in format_matrix_rows(problem_2["u_matrix"]):
        lines.append(f"- `{row}`")
    lines.append("")
    lines.append("### Residual vector")
    lines.append("")
    lines.append(f"- `Ax - b = {format_vector(problem_2['residual'])}`")
    lines.append("")
    lines.append("## Problem 3")
    lines.append("")
    lines.append("Written proof is in `hw4/theory.md`.")
    lines.append("")
    lines.append("## Problem 4")
    lines.append("")
    lines.append("Written proof is in `hw4/theory.md`.")
    lines.append("")
    out_path.write_text("\n".join(lines), encoding="utf-8")

def main() -> None:
    hw4_dir = Path(__file__).resolve().parent

    problem_1 = run_problem_1()
    problem_2 = run_problem_2()

    print_problem_1(problem_1)
    print_problem_2(problem_2)

    report_path = hw4_dir / "results.md"
    write_results_markdown(problem_1, problem_2, report_path)

    print(f"\nWrote markdown report: {report_path}")
    print("\nGenerated markdown report contents:\n")
    print(report_path.read_text(encoding="utf-8"))

if __name__ == "__main__":
    main()
