from __future__ import annotations
import math
from typing import List

def f_exp(x: float) -> float:
    """The exponential function f(x) = e^x"""
    return math.exp(x)

def get_evaluation_nodes(num_points: int = 501, interval: tuple[float, float] = (-1.0, 1.0)) -> List[float]:
    """
    Generates equally spaced points for error evaluation.
    Default is 501 points on [-1, 1] as defined by t_k = -1 + 2k/500
    """
    left, right = interval
    step = (right - left) / (num_points - 1)
    return [left + step * k for k in range(num_points)]

def get_interpolation_nodes(n: int, interval: tuple[float, float] = (-1.0, 1.0)) -> List[float]:
    """
    Generates n+1 equally spaced interpolation nodes on the interval.
    """
    left, right = interval
    if n == 0:
        return [(left + right) / 2.0]
    step = (right - left) / n
    return [left + step * i for i in range(n + 1)]