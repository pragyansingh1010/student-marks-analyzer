# Input Validation Notes

- Parse scores as numbers before calculating summaries.
- Enforce the configured score range at the input boundary.
- Report which row contains an invalid score when importing CSV.
- Distinguish missing values from genuine zero marks.
- Avoid dividing by zero when no valid scores remain.
- Keep display rounding separate from the underlying calculation.