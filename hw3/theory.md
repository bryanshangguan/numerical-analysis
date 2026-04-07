# HW3 Theory Notes

## Problem 1

**Part 1: Prove $p(x) = \sum_{i=0}^{n} L_i^{(n)}(x) p(x_i)$ for any polynomial of degree $\le n$.**

Let $p(x)$ be an arbitrary polynomial of degree $\le n$. We are given a set of $n+1$ distinct nodes $x_0, x_1, \dots, x_n$.

Consider the interpolating polynomial $P(x)$ defined using the Lagrange basis:
$$P(x) = \sum_{i=0}^{n} L_i^{(n)}(x) p(x_i)$$

Recall that the Lagrange basis polynomials $L_i^{(n)}(x)$ each have degree exactly $n$, meaning any linear combination of them, including $P(x)$, is a polynomial of degree at most $n$. Furthermore, the Lagrange basis polynomials satisfy the Kronecker delta property at the nodes:
$$L_i^{(n)}(x_j) = \delta_{ij}$$

If we evaluate our interpolating polynomial $P(x)$ at any node $x_j$, we obtain:
$$P(x_j) = \sum_{i=0}^{n} L_i^{(n)}(x_j) p(x_i) = p(x_j)$$

Because $P(x)$ and $p(x)$ agree exactly at $n+1$ distinct points (the nodes $x_0, \dots, x_n$), and both are polynomials of degree $\le n$, the Fundamental Theorem of Algebra (specifically the uniqueness of polynomial interpolation) dictates that they must be the exact same polynomial. Therefore, $p(x) = \sum_{i=0}^{n} L_i^{(n)}(x) p(x_i)$.

**Part 2: Prove $\sum_{i=0}^{n} L_i^{(n)}(x) = 1$.**

Consider the constant function $p(x) = 1$. This is trivially a polynomial of degree $0$, which is $\le n$.

Applying the result from Part 1, we can substitute $p(x) = 1$ into our proven representation:
$$1 = \sum_{i=0}^{n} L_i^{(n)}(x) (1)$$
$$1 = \sum_{i=0}^{n} L_i^{(n)}(x)$$

This confirms that the Lagrange basis polynomials form a partition of unity.

---

## Problem 3

We are tasked with finding the error in the quadratic interpolation to $f(x) = \sqrt{x}$ using equally spaced nodes on the interval $[1/4, 1]$.

For quadratic interpolation, $n=2$. The interval length is $1 - 1/4 = 3/4$. Splitting this into two equal sub-intervals gives our three nodes:

- $x_0 = 1/4$
- $x_1 = 5/8$
- $x_2 = 1$

The general error formula for polynomial interpolation is:
$$E_2(x) = f(x) - p_2(x) = \frac{f'''(\xi_x)}{3!} (x - x_0)(x - x_1)(x - x_2)$$
where $\xi_x \in (1/4, 1)$.

To find the strict upper bound of the error $|E_2(x)|$, we maximize both $|f'''(\xi)|$ and the nodal polynomial $|w(x)| = |(x-1/4)(x-5/8)(x-1)|$ over the interval $[1/4, 1]$.

**Step 1: Maximize $|f'''(\xi)|$**
Given $f(x) = x^{1/2}$:

- $f'(x) = \frac{1}{2} x^{-1/2}$
- $f''(x) = -\frac{1}{4} x^{-3/2}$
- $f'''(x) = \frac{3}{8} x^{-5/2}$

The function $f'''(x)$ is strictly decreasing on $[1/4, 1]$, so its absolute maximum occurs at the leftmost point of the interval, $x = 1/4$:
$$|f'''(1/4)| = \frac{3}{8} (1/4)^{-5/2} = \frac{3}{8} (2^5) = \frac{3}{8} (32) = 12$$

Thus, $\max |f'''(\xi)| = 12$.

**Step 2: Maximize $|w(x)| = |(x-1/4)(x-5/8)(x-1)|$**
To simplify, let's shift the coordinate system to the center node by letting $u = x - 5/8$. The interval $[1/4, 1]$ becomes $u \in [-3/8, 3/8]$.
$$w(u) = (u + 3/8)(u)(u - 3/8) = u(u^2 - 9/64) = u^3 - \frac{9}{64}u$$

To find the critical points, set the derivative to $0$:
$$w'(u) = 3u^2 - \frac{9}{64} = 0 \implies u^2 = \frac{3}{64} \implies u = \pm \frac{\sqrt{3}}{8}$$

Evaluate the absolute value at these critical points:
$$\left|w\left(\pm\frac{\sqrt{3}}{8}\right)\right| = \left|\left(\pm\frac{\sqrt{3}}{8}\right)\left(\frac{3}{64} - \frac{9}{64}\right)\right| = \left|\pm\frac{\sqrt{3}}{8}\left(-\frac{6}{64}\right)\right| = \frac{6\sqrt{3}}{512} = \frac{3\sqrt{3}}{256}$$

**Step 3: Calculate the maximum error**
Substitute both maximums back into the error bound formula:
$$|E_2(x)| \le \frac{\max |f'''(\xi)|}{3!} \cdot \max |w(x)|$$
$$|E_2(x)| \le \frac{12}{6} \cdot \frac{3\sqrt{3}}{256} = 2 \cdot \frac{3\sqrt{3}}{256} = \frac{3\sqrt{3}}{128}$$

The maximum theoretical error in the quadratic interpolation over the interval is exactly **$\frac{3\sqrt{3}}{128}$** (approximately $0.04059$).
