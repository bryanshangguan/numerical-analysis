# HW2 Results

## Problem 1

- Equation solved with bisection on annual rate `r`:
  `L = (12M/r) * [1 - (1 + r/12)^(-12m)]`, with `L=150000`, `M=600`, `m=30`.
- Bracketing interval: `[0.001, 0.2]`
- Converged: `True`
- Affordable annual rate (decimal): `0.0259351340`
- Affordable annual rate (percent): `2.5935134042%`
- Iterations: `31`
- Residual: `1.656007e-04`

## Problem 2

Written proof is in `hw2/theory.md`.

## Problem 3

Using `e_(n+1) <= (3/2)e_n^2` and worst-case initial bound `e_0 = 1/3`:

| Step | Exact bound | Decimal |
|---:|---:|---:|
| e_0 | 1/3 | 0.3333333333 |
| e_1 | 1/6 | 0.1666666667 |
| e_2 | 1/24 | 0.0416666667 |
| e_3 | 1/384 | 0.0026041667 |

## Problem 4

- Lagrange form: `0 * [(x - 1) * (x - 2) * (x - 3)] / [(0 - 1) * (0 - 2) * (0 - 3)] + 1 * [(x - 0) * (x - 2) * (x - 3)] / [(1 - 0) * (1 - 2) * (1 - 3)] + 8 * [(x - 0) * (x - 1) * (x - 3)] / [(2 - 0) * (2 - 1) * (2 - 3)] + 27 * [(x - 0) * (x - 1) * (x - 2)] / [(3 - 0) * (3 - 1) * (3 - 2)]`
- Simplified polynomial: `P(x) = x^3`

| x | Expected y | P(x) | Abs error |
|---:|---:|---:|---:|
| 0 | 0 | 0.0000000000 | 0.000e+00 |
| 1 | 1 | 1.0000000000 | 0.000e+00 |
| 2 | 8 | 8.0000000000 | 0.000e+00 |
| 3 | 27 | 27.0000000000 | 0.000e+00 |
