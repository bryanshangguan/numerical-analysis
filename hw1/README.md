# CS323 HW1 (Numerical Analysis)

This directory contains a full Python implementation for HW1:

- Problem 1: Newton, Secant, and Bisection methods on functions (a) through (j).
- Problem 2: Proof writeup in `theory.md`.
- Problem 3: Fixed-point iteration experiment and theory-vs-observed iteration counts.

## Run

From repository root:

```bash
python main.py
```

This prints the numerical tables to the console and writes:

- `results.md` (auto-generated numeric results for Problems 1 and 3)
- `hw1/theory.md` (derivations for Problems 2 and 3)

## File Overview

- `root_methods.py`: reusable method implementations and result dataclasses
- `problems.py`: function definitions, derivatives, and method setups
- `main.py`: single runner and markdown report generation
- `theory.md`: written solutions for Problems 2 and 3
