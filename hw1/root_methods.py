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
    except Exception as exc:  # pragma: no cover - defensive catch for domain/singularity issues
        return False, float("nan"), str(exc)

def newton_method(
    f: Function,
    df: Function,
    x0: float,
    tol: float = 1e-6,
    max_iter: int = 200,
) -> MethodResult:
    method = "Newton"
    history: List[IterationPoint] = []
    x_n = x0

    for n in range(1, max_iter + 1):
        ok_f, f_xn, err = _safe_eval(f, x_n)
        if not ok_f:
            return _failure_result(method, x_n, history, f"Function evaluation failed: {err}")
        history.append(IterationPoint(iteration=n, x=x_n, fx=f_xn))
        ok_df, dfx, err_df = _safe_eval(df, x_n)
        if not ok_df:
            return _failure_result(method, x_n, history, f"Derivative evaluation failed: {err_df}")
        if dfx == 0.0:
            return _failure_result(method, x_n, history, "Derivative became zero.")
        x_next = x_n - f_xn / dfx
        if abs(x_next - x_n) < tol:
            ok_next, fx_next, err_next = _safe_eval(f, x_next)
            if not ok_next:
                return _failure_result(method, x_next, history, f"Function evaluation failed: {err_next}")
            history.append(IterationPoint(iteration=n + 1, x=x_next, fx=fx_next))
            return MethodResult(
                method=method,
                converged=True,
                root=x_next,
                iterations=n,
                residual=abs(fx_next),
                history=history,
            )
        x_n = x_next

    return _failure_result(method, x_n, history, "Maximum iterations reached.")

def secant_method(
    f: Function,
    x0: float,
    x1: float,
    tol: float = 1e-6,
    max_iter: int = 200,
) -> MethodResult:
    method = "Secant"
    history: List[IterationPoint] = []
    x_prev = x0
    x_curr = x1

    for n in range(1, max_iter + 1):
        ok_prev, f_prev, err_prev = _safe_eval(f, x_prev)
        if not ok_prev:
            return _failure_result(method, x_prev, history, f"Function evaluation failed: {err_prev}")
        ok_curr, f_curr, err_curr = _safe_eval(f, x_curr)
        if not ok_curr:
            return _failure_result(method, x_curr, history, f"Function evaluation failed: {err_curr}")
        history.append(IterationPoint(iteration=n, x=x_curr, fx=f_curr))
        denominator = f_curr - f_prev
        if denominator == 0.0:
            return _failure_result(method, x_curr, history, "Secant denominator became zero.")
        x_next = x_curr - f_curr * (x_curr - x_prev) / denominator
        if abs(x_next - x_curr) < tol:
            ok_next, fx_next, err_next = _safe_eval(f, x_next)
            if not ok_next:
                return _failure_result(method, x_next, history, f"Function evaluation failed: {err_next}")
            history.append(IterationPoint(iteration=n + 1, x=x_next, fx=fx_next))
            return MethodResult(
                method=method,
                converged=True,
                root=x_next,
                iterations=n,
                residual=abs(fx_next),
                history=history,
            )
        x_prev, x_curr = x_curr, x_next

    return _failure_result(method, x_curr, history, "Maximum iterations reached.")

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
            method=method,
            converged=True,
            root=a,
            iterations=0,
            residual=0.0,
            history=history,
        )
    if fb == 0.0:
        history.append(IterationPoint(iteration=1, x=b, fx=fb))
        return MethodResult(
            method=method,
            converged=True,
            root=b,
            iterations=0,
            residual=0.0,
            history=history,
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
                method=method,
                converged=True,
                root=mid,
                iterations=n,
                residual=abs(fmid),
                history=history,
            )
        if fmid == 0.0:
            return MethodResult(
                method=method,
                converged=True,
                root=mid,
                iterations=n,
                residual=0.0,
                history=history,
            )
        if fa * fmid < 0.0:
            right = mid
            fb = fmid
        else:
            left = mid
            fa = fmid
        prev_mid = mid

    return _failure_result(method, (left + right) / 2.0, history, "Maximum iterations reached.")
