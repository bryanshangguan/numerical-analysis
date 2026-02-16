# CS323 HW1 (Numerical Analysis)

This directory contains a full Python implementation for HW1:

- Problem 1: Newton, Secant, and Bisection methods on functions (a) through (j).
- Problem 2: Concise proof writeup in `theory.md`.
- Problem 3: Fixed-point iteration experiment and theory-vs-observed iteration counts.

## Run

From repository root:

```bash
python hw1/main.py
```

This prints the numerical tables to the console and writes:

- `hw1/results.md` (auto-generated numeric results for Problems 1 and 3)
- `hw1/theory.md` (derivations for Problems 2 and 3)

## File Overview

- `hw1/root_methods.py`: reusable method implementations and result dataclasses
- `hw1/problems.py`: function definitions, derivatives, and method setups
- `hw1/main.py`: single runner and markdown report generation
- `hw1/theory.md`: written solutions for Problems 2 and 3
