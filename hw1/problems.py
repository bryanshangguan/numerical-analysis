from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Callable, Optional, Tuple

Function = Callable[[float], float]
Interval = Tuple[float, float]

@dataclass(frozen=True)
class ProblemDefinition:
    label: str
    expression: str
    f: Function
    df: Function
    x0: float
    secant_x1: float
    bisection_interval: Optional[Interval]

PROBLEM_SET = [
    ProblemDefinition(
        label="a",
        expression="1 - 2x*exp(-x/2)",
        f=lambda x: 1.0 - 2.0 * x * math.exp(-x / 2.0),
        df=lambda x: (x - 2.0) * math.exp(-x / 2.0),
        x0=0.0,
        secant_x1=0.5,
        bisection_interval=(0.0, 2.0),
    ),
    ProblemDefinition(
        label="b",
        expression="5 - x^(-1)",
        f=lambda x: 5.0 - 1.0 / x,
        df=lambda x: 1.0 / (x * x),
        x0=0.25,
        secant_x1=0.3,
        bisection_interval=(0.1, 0.5),
    ),
    ProblemDefinition(
        label="c",
        expression="x^3 - 2x - 5",
        f=lambda x: x**3 - 2.0 * x - 5.0,
        df=lambda x: 3.0 * x * x - 2.0,
        x0=2.0,
        secant_x1=2.2,
        bisection_interval=(2.0, 3.0),
    ),
    ProblemDefinition(
        label="d",
        expression="exp(x) - 2",
        f=lambda x: math.exp(x) - 2.0,
        df=lambda x: math.exp(x),
        x0=1.0,
        secant_x1=0.5,
        bisection_interval=(0.0, 2.0),
    ),
    ProblemDefinition(
        label="e",
        expression="x - exp(-x)",
        f=lambda x: x - math.exp(-x),
        df=lambda x: 1.0 + math.exp(-x),
        x0=1.0,
        secant_x1=0.5,
        bisection_interval=(0.0, 1.0),
    ),
    ProblemDefinition(
        label="f",
        expression="x^6 - x - 1",
        f=lambda x: x**6 - x - 1.0,
        df=lambda x: 6.0 * (x**5) - 1.0,
        x0=1.0,
        secant_x1=1.2,
        bisection_interval=(1.0, 2.0),
    ),
    ProblemDefinition(
        label="g",
        expression="x^2 - sin(x)",
        f=lambda x: x * x - math.sin(x),
        df=lambda x: 2.0 * x - math.cos(x),
        x0=0.5,
        secant_x1=0.8,
        bisection_interval=(0.5, 1.0),
    ),
    ProblemDefinition(
        label="h",
        expression="x^3 - 2",
        f=lambda x: x**3 - 2.0,
        df=lambda x: 3.0 * x * x,
        x0=1.0,
        secant_x1=1.2,
        bisection_interval=(1.0, 2.0),
    ),
    ProblemDefinition(
        label="i",
        expression="x + tan(x)",
        f=lambda x: x + math.tan(x),
        df=lambda x: 1.0 + 1.0 / (math.cos(x) ** 2),
        x0=3.0,
        secant_x1=2.9,
        bisection_interval=(2.0, 3.0),
    ),
    ProblemDefinition(
        label="j",
        expression="2 - ln(x)/x",
        f=lambda x: 2.0 - math.log(x) / x,
        df=lambda x: (math.log(x) - 1.0) / (x * x),
        x0=1.0 / 3.0,
        secant_x1=0.4,
        bisection_interval=None,
    ),
]

def fixed_point_g(x: float) -> float:
    return 1.0 + math.exp(-x)

def fixed_point_g_prime(x: float) -> float:
    return -math.exp(-x)
