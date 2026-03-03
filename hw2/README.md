# CS323 HW2 (Numerical Analysis)

This directory contains a complete solution package for HW2:

- Problem 1: bisection solution for the mortgage annuity interest rate.
- Problem 2: Taylor-theorem proof of Newton's local error formula.
- Problem 3: error bounds for the first three Newton steps.
- Problem 4: degree-3 interpolation through `(0,0), (1,1), (2,8), (3,27)`.

## Run

From repository root:

```bash
python hw2/main.py
```

This prints numerical outputs to the console and writes:

- `hw2/results.md` (auto-generated computational results for Problems 1, 3, and 4)
- `hw2/theory.md` (written derivations for Problems 2 and 3)

## File Overview

- `methods.py`: bisection implementation and polynomial interpolation utilities
- `problems.py`: constants and definitions for HW2 problem setup
- `main.py`: runner, formatted console output, and markdown report generation
- `theory.md`: written proofs and derivations
- `results.md`: generated report with final computational outputs
