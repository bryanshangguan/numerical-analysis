from __future__ import annotations

from dataclasses import dataclass
from typing import List

Matrix = List[List[float]]
Vector = List[float]

@dataclass
class LUResult:
    l_matrix: Matrix
    u_matrix: Matrix

def copy_matrix(matrix: Matrix) -> Matrix:
    return [row[:] for row in matrix]

def identity_matrix(size: int) -> Matrix:
    return [[1.0 if i == j else 0.0 for j in range(size)] for i in range(size)]

def lu_factorization(matrix: Matrix, tol: float = 1e-12) -> LUResult:
    n = len(matrix)
    if n == 0:
        raise ValueError("Matrix must be non-empty.")
    if any(len(row) != n for row in matrix):
        raise ValueError("LU factorization requires a square matrix.")

    u_matrix = copy_matrix(matrix)
    l_matrix = identity_matrix(n)

    for k in range(n - 1):
        pivot = u_matrix[k][k]
        if abs(pivot) < tol:
            raise ValueError(f"Zero pivot encountered at column {k}.")

        for i in range(k + 1, n):
            multiplier = u_matrix[i][k] / pivot
            l_matrix[i][k] = multiplier
            u_matrix[i][k] = 0.0
            for j in range(k + 1, n):
                u_matrix[i][j] -= multiplier * u_matrix[k][j]

    return LUResult(l_matrix=l_matrix, u_matrix=u_matrix)

def forward_substitution(lower: Matrix, rhs: Vector, tol: float = 1e-12) -> Vector:
    n = len(lower)
    if len(rhs) != n:
        raise ValueError("Right-hand side dimension does not match lower-triangular system.")

    solution = [0.0] * n
    for i in range(n):
        pivot = lower[i][i]
        if abs(pivot) < tol:
            raise ValueError(f"Zero diagonal encountered in forward substitution at row {i}.")
        subtotal = sum(lower[i][j] * solution[j] for j in range(i))
        solution[i] = (rhs[i] - subtotal) / pivot
    return solution

def backward_substitution(upper: Matrix, rhs: Vector, tol: float = 1e-12) -> Vector:
    n = len(upper)
    if len(rhs) != n:
        raise ValueError("Right-hand side dimension does not match upper-triangular system.")

    solution = [0.0] * n
    for i in range(n - 1, -1, -1):
        pivot = upper[i][i]
        if abs(pivot) < tol:
            raise ValueError(f"Zero diagonal encountered in backward substitution at row {i}.")
        subtotal = sum(upper[i][j] * solution[j] for j in range(i + 1, n))
        solution[i] = (rhs[i] - subtotal) / pivot
    return solution

def solve_lu(l_matrix: Matrix, u_matrix: Matrix, rhs: Vector) -> Vector:
    y_vec = forward_substitution(l_matrix, rhs)
    return backward_substitution(u_matrix, y_vec)

def matrix_vector_product(matrix: Matrix, vector: Vector) -> Vector:
    return [sum(value * vector[j] for j, value in enumerate(row)) for row in matrix]

def matrix_multiply(left: Matrix, right: Matrix) -> Matrix:
    if not left or not right:
        return []
    rows = len(left)
    inner = len(left[0])
    cols = len(right[0])
    if any(len(row) != inner for row in left):
        raise ValueError("Left matrix is not rectangular.")
    if any(len(row) != cols for row in right):
        raise ValueError("Right matrix is not rectangular.")
    if len(right) != inner:
        raise ValueError("Matrix dimensions do not align for multiplication.")

    product = [[0.0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for k in range(inner):
            for j in range(cols):
                product[i][j] += left[i][k] * right[k][j]
    return product

def vector_subtract(left: Vector, right: Vector) -> Vector:
    if len(left) != len(right):
        raise ValueError("Vectors must have the same length.")
    return [a - b for a, b in zip(left, right)]

def max_abs_vector(vector: Vector) -> float:
    return max((abs(value) for value in vector), default=0.0)

def max_abs_matrix(matrix: Matrix) -> float:
    return max((abs(value) for row in matrix for value in row), default=0.0)
