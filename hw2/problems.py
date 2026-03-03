from __future__ import annotations

LOAN_AMOUNT = 150_000.0
MONTHLY_PAYMENT = 600.0
YEARS = 30.0

BisectionInterval = tuple[float, float]
ANNUITY_BISECTION_INTERVAL: BisectionInterval = (0.001, 0.20)

INTERPOLATION_POINTS: list[tuple[float, float]] = [
    (0.0, 0.0),
    (1.0, 1.0),
    (2.0, 8.0),
    (3.0, 27.0),
]


def annuity_residual(r: float) -> float:
    if r <= 0.0:
        raise ValueError("Interest rate r must be positive.")
    months = 12.0 * YEARS
    return (12.0 * MONTHLY_PAYMENT / r) * (1.0 - (1.0 + r / 12.0) ** (-months)) - LOAN_AMOUNT
