# HW2 Theory Notes

## Problem 2

Let `f in C^2(I)` with `f(alpha) = 0`, and define Newton's iteration

`x_(n+1) = x_n - f(x_n) / f'(x_n)`.

Apply Taylor's theorem to `f(alpha)` around `x_n`. Since `f` is twice differentiable, there exists a point `xi_n` between `alpha` and `x_n` such that

`f(alpha) = f(x_n) + f'(x_n)(alpha - x_n) + (1/2)f''(xi_n)(alpha - x_n)^2`.

Using `f(alpha)=0`, we have

`0 = f(x_n) + f'(x_n)(alpha - x_n) + (1/2)f''(xi_n)(alpha - x_n)^2`.

Divide by `f'(x_n)`:

`0 = f(x_n)/f'(x_n) + (alpha - x_n) + (1/2)(alpha - x_n)^2 * f''(xi_n)/f'(x_n)`.

From Newton's definition,

`f(x_n)/f'(x_n) = x_n - x_(n+1)`.

Substitute:

`0 = (x_n - x_(n+1)) + (alpha - x_n) + (1/2)(alpha - x_n)^2 * f''(xi_n)/f'(x_n)`

`0 = alpha - x_(n+1) + (1/2)(alpha - x_n)^2 * f''(xi_n)/f'(x_n)`.

Therefore,

`(alpha - x_(n+1)) = -(1/2)(alpha - x_n)^2 * f''(xi_n)/f'(x_n)`,

## Problem 3

From Problem 2, define the error `e_n = |alpha - x_n|`. Then

`e_(n+1) = (1/2)e_n^2 * |f''(xi_n)| / |f'(x_n)|`.

Given `|f''(x)| <= 3` and `|f'(x)| >= 1`, we get

`e_(n+1) <= (1/2)e_n^2 * 3/1 = (3/2)e_n^2`.

With initial bound `e_0 < 1/3`, a valid upper bound sequence uses `e_0 = 1/3`:

- `e_1 <= (3/2)(1/3)^2 = 1/6`
- `e_2 <= (3/2)(1/6)^2 = 1/24`
- `e_3 <= (3/2)(1/24)^2 = 1/384`

So upper bounds for the first three Newton steps are:

`e_1 <= 1/6`, `e_2 <= 1/24`, `e_3 <= 1/384`.
