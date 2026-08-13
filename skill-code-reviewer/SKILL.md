---
name: code-reviewer
description: Review code changes, pull requests, and merge requests for bugs, regressions, security issues, missing tests, and maintainability risks. Use when Codex is asked to inspect a diff, review a PR/MR, review local changes before merging, or provide code review feedback.
---

# Code Reviewer

## Workflow

1. Inspect the change scope with `git status`, `git diff`, branch comparison commands, or PR metadata available in the environment.
2. Read the changed files and the surrounding code before judging the implementation.
3. Identify behavior changes, edge cases, error handling paths, data migrations, security boundaries, and user-facing workflows touched by the diff.
4. Prioritize confirmed risks over style preferences.
5. Report findings first, ordered by severity, with exact file and line references.
6. Include open questions only after findings.
7. Mention tests or validation gaps when they materially affect confidence.

## Review Standards

Use [the review checklist](references/review-checklist.md) when the change is non-trivial, crosses module boundaries, or touches user-facing behavior.

Use [the severity rubric](references/severity-rubric.md) when deciding whether a finding is blocking, high, medium, or low priority.

## Output Format

Lead with findings. For each finding, include:

- severity
- file and line
- the problem
- why it matters
- a concrete fix direction

If there are no findings, say that clearly and note any residual risk or missing validation.

Keep summaries brief and secondary to the findings.
