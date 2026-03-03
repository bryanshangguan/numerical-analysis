from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, List, Optional

Function = Callable[[float], float]


@dataclass
class IterationPoint:
    iteration: int
    x: float
    fx: float


@dataclass
class MethodResult:
    method: str
    converged: bool
    root: float
    iterations: int
    residual: float
    history: List[IterationPoint]
    message: str = ""


def _failure_result(method: str, x_value: float, history: List[IterationPoint], message: str) -> MethodResult:
    residual = float("inf")
    if history:
        residual = abs(history[-1].fx)
    return MethodResult(
        method=method,
        converged=False,
        root=x_value,
        iterations=len(history),
        residual=residual,
        history=history,
        message=message,
    )


def _safe_eval(f: Function, x: float) -> tuple[bool, float, str]:
    try:
        return True, f(x), ""
    except Exception as exc:  # pragma: no cover - defensive catch
        return False, float("nan"), str(exc)


def bisection_method(
    f: Function,
    a: float,
    b: float,
    tol: float = 1e-6,
    max_iter: int = 500,
) -> MethodResult:
    method = "Bisection"
    history: List[IterationPoint] = []
    ok_a, fa, err_a = _safe_eval(f, a)
    if not ok_a:
        return _failure_result(method, a, history, f"Function evaluation failed at interval start: {err_a}")
    ok_b, fb, err_b = _safe_eval(f, b)
    if not ok_b:
        return _failure_result(method, b, history, f"Function evaluation failed at interval end: {err_b}")
    if fa == 0.0:
        history.append(IterationPoint(iteration=1, x=a, fx=fa))
        return MethodResult(
            method = method,
            converged = True,
            root = a,
            iterations = 0,
            residual = 0.0,
            history = history,
        )
    if fb == 0.0:
        history.append(IterationPoint(iteration=1, x=b, fx=fb))
        return MethodResult(
            method = method,
            converged = True,
            root = b,
            iterations = 0,
            residual = 0.0,
            history = history,
        )
    if fa * fb > 0.0:
        return _failure_result(method, a, history, "Interval does not bracket a root.")

    prev_mid: Optional[float] = None
    left, right = a, b
    for n in range(1, max_iter + 1):
        mid = (left + right) / 2.0
        ok_mid, fmid, err_mid = _safe_eval(f, mid)
        if not ok_mid:
            return _failure_result(method, mid, history, f"Function evaluation failed: {err_mid}")
        history.append(IterationPoint(iteration=n, x=mid, fx=fmid))
        if prev_mid is not None and abs(mid - prev_mid) < tol:
            return MethodResult(
                method = method,
                converged = True,
                root = mid,
                iterations = n,
                residual = abs(fmid),
                history = history,
            )
        if fmid == 0.0:
            return MethodResult(
                method = method,
                converged = True,
                root = mid,
                iterations = n,
                residual = 0.0,
                history = history,
            )
        if fa * fmid < 0.0:
            right = mid
            fb = fmid
        else:
            left = mid
            fa = fmid
        prev_mid = mid

    return _failure_result(method, (left + right) / 2.0, history, "Maximum iterations reached.")


def _poly_add(p: List[float], q: List[float]) -> List[float]:
    size = max(len(p), len(q))
    out = [0.0] * size
    for i in range(size):
        if i < len(p):
            out[i] += p[i]
        if i < len(q):
            out[i] += q[i]
    return out


def _poly_mul(p: List[float], q: List[float]) -> List[float]:
    out = [0.0] * (len(p) + len(q) - 1)
    for i, pi in enumerate(p):
        for j, qj in enumerate(q):
            out[i + j] += pi * qj
    return out


def lagrange_interpolation(points: list[tuple[float, float]]) -> list[float]:
    if len(points) == 0:
        raise ValueError("At least one point is required.")
    xs = [x for x, _ in points]
    if len(set(xs)) != len(xs):
        raise ValueError("Interpolation points must have distinct x-values.")

    n = len(points)
    poly = [0.0]
    for k in range(n):
        xk, yk = points[k]
        basis = [1.0]
        denom = 1.0
        for j in range(n):
            if j == k:
                continue
            xj, _ = points[j]
            basis = _poly_mul(basis, [-xj, 1.0])  # multiply by (x - xj)
            denom *= (xk - xj)
        scale = yk / denom
        scaled_basis = [scale * coeff for coeff in basis]
        poly = _poly_add(poly, scaled_basis)
    return poly


def eval_polynomial(coeffs: list[float], x: float) -> float:
    value = 0.0
    for coeff in reversed(coeffs):
        value = value * x + coeff
    return value
