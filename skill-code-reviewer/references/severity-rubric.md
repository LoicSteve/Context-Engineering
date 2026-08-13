# Severity Rubric

Use severity to reflect user impact and merge risk, not personal preference.

## Blocking

Use for issues that should stop the merge:

- data loss or corruption
- security vulnerability
- broken authentication or authorization
- application crash in a common path
- migration or deployment issue likely to break production

## High

Use for serious issues that should be fixed before release:

- incorrect behavior in an important workflow
- missing handling for a likely edge case
- broken integration with another module or service
- significant reliability or performance regression

## Medium

Use for issues that are real but limited:

- bug in a less common path
- confusing behavior with a workaround
- missing validation for non-critical input
- test gap around meaningful changed behavior

## Low

Use for minor issues:

- maintainability concern with low immediate risk
- unclear naming that could cause future mistakes
- small inconsistency with local patterns

Avoid reporting purely subjective style preferences as findings.
