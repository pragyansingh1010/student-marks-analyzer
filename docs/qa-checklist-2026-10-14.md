# Student Marks Analyzer — QA Checklist

- Verify empty input produces a clear message instead of a division-by-zero error.
- Check that marks at 0 and at the maximum allowed value are accepted.
- Reject marks below 0 and above the configured maximum.
- Confirm averages use numeric values and round only for display.
- Test missing, duplicate, and non-numeric CSV values.
- Confirm the report labels each statistic and handles a file with one student.