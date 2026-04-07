from __future__ import annotations
from typing import List

def newton_divided_differences(x_nodes: List[float], y_nodes: List[float]) -> List[float]:
    """
    Computes the coefficients for the Newton interpolating polynomial
    using divided differences in-place.
    """
    n = len(x_nodes)
    if n == 0:
        return []
    
    coef = list(y_nodes)
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) / (x_nodes[i] - x_nodes[i - j])
    return coef

def evaluate_newton_polynomial(coef: List[float], x_nodes: List[float], x: float) -> float:
    """
    Evaluates a Newton polynomial at point x using Horner's method.
    """
    n = len(coef)
    if n == 0:
        return 0.0
    
    val = coef[n - 1]
    for i in range(n - 2, -1, -1):
        val = val * (x - x_nodes[i]) + coef[i]
    return val