from __future__ import annotations

from typing import List

Matrix = List[List[float]]
Vector = List[float]

PROBLEM_2_MATRIX: Matrix = [
    [14.0, 14.0, -9.0, 3.0, -5.0],
    [14.0, 52.0, -15.0, 2.0, -32.0],
    [-9.0, -15.0, 36.0, -5.0, 16.0],
    [3.0, 2.0, -5.0, 47.0, 49.0],
    [-5.0, -32.0, 16.0, 49.0, 79.0],
]

PROBLEM_2_VECTOR: Vector = [-15.0, -100.0, 106.0, 329.0, 463.0]

def problem_1_operation_counts() -> list[dict[str, str]]:
    return [
        {
            "operation": "Dot product x . y for x, y in R^(n x 1)",
            "multiplications": "n",
            "additions": "n - 1",
            "total": "2n - 1",
        },
        {
            "operation": "Matrix-vector product Ax for A in R^(m x n), x in R^(n x 1)",
            "multiplications": "mn",
            "additions": "m(n - 1)",
            "total": "m(2n - 1)",
        },
        {
            "operation": "Matrix-matrix product AB for A in R^(m x n), B in R^(n x p)",
            "multiplications": "mnp",
            "additions": "mp(n - 1)",
            "total": "mp(2n - 1)",
        },
    ]
