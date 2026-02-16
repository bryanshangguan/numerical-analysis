# HW1 Theory Notes

## Problem 2

Given a fixed-point iteration

`x_(n+1) = g(x_n)`, with `g : [a,b] -> [a,b]`,

assume there exists `L in [0,1)` such that for all `x,y in [a,b]`,

`|g(x) - g(y)| <= L |x - y|`.

Let `alpha` be the fixed point (`g(alpha) = alpha`) and define errors `e_n = |alpha - x_n|`.

From the contraction condition:

`e_n = |g(alpha) - g(x_(n-1))| <= L |alpha - x_(n-1)| = L e_(n-1)`.

By induction:

`e_n <= L^n e_0`.

Also,

`|x_1 - x_0| = |g(x_0) - x_0|`
`>= |alpha - x_0| - |alpha - x_1|`
`= e_0 - e_1`
`>= e_0 - L e_0 = (1-L)e_0`.

So,

`e_0 <= |x_1 - x_0| / (1-L)`.

Combining with `e_n <= L^n e_0`:

`|alpha - x_n| = e_n <= (L^n / (1-L)) |x_1 - x_0|`.

That is exactly the required bound.

## Problem 3

Iteration:

`x_(n+1) = g(x_n) = 1 + e^(-x_n)`, with `x_0 in [1,2]`.

1. `g([1,2]) subset [1,2]`:
   - `g(1) = 1 + e^(-1) ~= 1.3679`,
   - `g(2) = 1 + e^(-2) ~= 1.1353`,
   so all values stay in `[1,2]`.

2. Contraction on `[1,2]`:
   - `g'(x) = -e^(-x)`,
   - `|g'(x)| = e^(-x) <= e^(-1) =: L < 1`.

Therefore the iteration converges for any `x_0 in [1,2]`.

For accuracy `|alpha - x_n| <= 10^(-5)`, use Problem 2:

`|alpha - x_n| <= (L^n/(1-L)) |x_1 - x_0|`.

Take worst case over `x_0 in [1,2]`:

- `L = e^(-1) ~= 0.367879`,
- `|x_1 - x_0| = |1 + e^(-x_0) - x_0|` is maximized at `x_0 = 2`, giving `|x_1-x_0| = 1 - e^(-2) ~= 0.864665`.

Require

`(L^n/(1-L))*0.864665 <= 10^(-5)`.

So

`n >= ln(10^(-5)*(1-L)/0.864665) / ln(L) ~= 11.66`.

Hence `n = 12` iterations are sufficient by theory (uniformly for all `x_0 in [1,2]`).
