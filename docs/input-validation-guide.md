# Input Validation Guide

Validate that every entered mark is numeric and falls within the expected range before analysis. Invalid values should be rejected with a clear message so calculations never use malformed data.

## Recommended checks

- Accept numeric input only.
- Keep marks between 0 and 100.
- Re-prompt after invalid input.
- Preserve valid values for the final analysis.