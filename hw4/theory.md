# HW4 Theory Notes

## Problem 3

Let the elimination matrix at step `k` be

`M_k = I - m_k e_k^T`,

where `m_k` is the vector of multipliers stored below the diagonal in column `k`, and its first `k` entries are zero. In particular, the `k`-th entry of `m_k` is zero, so

`e_k^T m_k = 0`.

### Part (a)

We claim that

`M_k^(-1) = I + m_k e_k^T`.

To verify this, multiply:

`(I - m_k e_k^T)(I + m_k e_k^T)`

`= I + m_k e_k^T - m_k e_k^T - m_k e_k^T m_k e_k^T`

`= I - m_k (e_k^T m_k) e_k^T`

`= I`,

because `e_k^T m_k = 0`. The reverse product is identical, so `I + m_k e_k^T` is indeed the inverse of `M_k`.

### Part (b)

Using part (a),

`M_k^(-1) M_(k-1)^(-1) = (I + m_k e_k^T)(I + m_(k-1) e_(k-1)^T)`.

Expanding gives

`I + m_k e_k^T + m_(k-1) e_(k-1)^T + m_k e_k^T m_(k-1) e_(k-1)^T`.

Now `m_(k-1)` has zeros in its first `k-1` entries, so its `(k)`-th entry is also zero. Hence

`e_k^T m_(k-1) = 0`.

Therefore the cross term vanishes:

`m_k e_k^T m_(k-1) e_(k-1)^T = m_k (e_k^T m_(k-1)) e_(k-1)^T = 0`.

So

`M_k^(-1) M_(k-1)^(-1) = I + m_k e_k^T + m_(k-1) e_(k-1)^T`.

### Part (c)

In elimination-matrix LU factorization,

`L = M_1^(-1) M_2^(-1) ... M_(n-1)^(-1)`.

From part (a), each factor has the form `I + m_j e_j^T`. When these factors are multiplied together, every mixed term disappears for the same reason as in part (b): whenever `i > j`, the vector `m_j` has a zero in position `i`, so `e_i^T m_j = 0`.

Thus only the linear terms remain, and we obtain

`L = I + m_1 e_1^T + m_2 e_2^T + ... + m_(n-1) e_(n-1)^T`.

This is exactly the claimed formula.

## Problem 4

Define

`||A||_* = max_(i,j) |a_(ij)|`.

To be a matrix norm, this quantity must satisfy submultiplicativity:

`||AB|| <= ||A|| ||B||`

for all compatible matrices `A` and `B`.

Consider

`A = B = [[1, 1], [1, 1]]`.

Then every entry of `A` and `B` has absolute value `1`, so

`||A||_* = 1,   ||B||_* = 1`.

But

`AB = [[2, 2], [2, 2]]`,

so

`||AB||_* = 2`.

Therefore

`||AB||_* = 2 > 1 = ||A||_* ||B||_*`.

This violates submultiplicativity, so `||A||_*` is not a matrix norm.
