# HW1 Results

## Problem 1

| Function | Method | Converged | Root | Iterations | Residual | Note |
|---|---|---:|---:|---:|---:|---|
| a: `1 - 2x*exp(-x/2)` | Newton | True | 0.7148059124 | 5 | 0.0000000000 | - |
| a: `1 - 2x*exp(-x/2)` | Secant | True | 0.7148059124 | 6 | 0.0000000000 | - |
| a: `1 - 2x*exp(-x/2)` | Bisection | True | 0.7148065567 | 21 | 0.0000005792 | - |
| b: `5 - x^(-1)` | Newton | True | 0.2000000000 | 5 | 0.0000000000 | - |
| b: `5 - x^(-1)` | Secant | True | 0.2000000004 | 6 | 0.0000000093 | - |
| b: `5 - x^(-1)` | Bisection | True | 0.2000000000 | 2 | 0.0000000000 | - |
| c: `x^3 - 2x - 5` | Newton | True | 2.0945514815 | 4 | 0.0000000000 | - |
| c: `x^3 - 2x - 5` | Secant | True | 2.0945514815 | 5 | 0.0000000000 | - |
| c: `x^3 - 2x - 5` | Bisection | True | 2.0945520401 | 20 | 0.0000062343 | - |
| d: `exp(x) - 2` | Newton | True | 0.6931471806 | 4 | 0.0000000000 | - |
| d: `exp(x) - 2` | Secant | True | 0.6931471806 | 5 | 0.0000000000 | - |
| d: `exp(x) - 2` | Bisection | True | 0.6931467056 | 21 | 0.0000009499 | - |
| e: `x - exp(-x)` | Newton | True | 0.5671432904 | 4 | 0.0000000000 | - |
| e: `x - exp(-x)` | Secant | True | 0.5671432904 | 4 | 0.0000000000 | - |
| e: `x - exp(-x)` | Bisection | True | 0.5671434402 | 20 | 0.0000002348 | - |
| f: `x^6 - x - 1` | Newton | True | 1.1347241384 | 5 | 0.0000000000 | - |
| f: `x^6 - x - 1` | Secant | True | 1.1347241384 | 6 | 0.0000000000 | - |
| f: `x^6 - x - 1` | Bisection | True | 1.1347246170 | 20 | 0.0000049237 | - |
| g: `x^2 - sin(x)` | Newton | True | 0.8767262154 | 8 | 0.0000000000 | - |
| g: `x^2 - sin(x)` | Secant | True | 0.8767262154 | 6 | 0.0000000000 | - |
| g: `x^2 - sin(x)` | Bisection | True | 0.8767271042 | 19 | 0.0000009899 | - |
| h: `x^3 - 2` | Newton | True | 1.2599210499 | 5 | 0.0000000000 | - |
| h: `x^3 - 2` | Secant | True | 1.2599210499 | 5 | 0.0000000000 | - |
| h: `x^3 - 2` | Bisection | True | 1.2599210739 | 20 | 0.0000001144 | - |
| i: `x + tan(x)` | Newton | True | 2.0287578381 | 11 | 0.0000000000 | - |
| i: `x + tan(x)` | Secant | True | 2.0287578381 | 14 | 0.0000000000 | - |
| i: `x + tan(x)` | Bisection | True | 2.0287580490 | 20 | 0.0000012898 | - |
| j: `2 - ln(x)/x` | Newton | False | -68.2431832697 | 4 | 1.6935244379 | Function evaluation failed: math domain error |
| j: `2 - ln(x)/x` | Secant | False | -90.9083087166 | 5 | 1.7666023552 | Function evaluation failed: math domain error |
| j: `2 - ln(x)/x` | Bisection | False | 0.3333333333 | 0 | inf | No valid bracketing interval: f(x) = 2 - ln(x)/x has no real root. |

## Problem 3

- Fixed-point map: `g(x) = 1 + exp(-x)`
- Reference fixed point: `1.2784645428`
- Contraction constant on `[1,2]`: `L = 0.3678794412`
- Target accuracy: `1e-05`

| x0 | Predicted iterations (theory) | Observed iterations |
|---:|---:|---:|
| 1.0 | 11 | 9 |
| 1.5 | 11 | 8 |
| 2.0 | 12 | 9 |
