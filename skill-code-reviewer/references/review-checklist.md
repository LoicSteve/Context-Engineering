# Review Checklist

Use this checklist to find substantive issues. Do not report items unless they create real risk in the reviewed change.

## Correctness

- Check whether the implementation matches the intended behavior.
- Look for off-by-one errors, wrong conditions, stale state, bad defaults, and incorrect assumptions about null or empty values.
- Check error paths, retries, cleanup, rollback behavior, and partial failure handling.
- Verify that data transformations preserve required fields and types.

## Integration

- Check call sites, public interfaces, imports, dependency injection, configuration, and feature flags.
- Look for mismatches between frontend and backend contracts, API schemas, database columns, or event payloads.
- Check whether the change breaks backward compatibility or existing saved data.

## Security And Privacy

- Check authentication, authorization, input validation, secret handling, logging, file access, and network boundaries.
- Flag exposure of tokens, credentials, personal data, or internal implementation details.
- Check injection risks in SQL, shell commands, templates, paths, URLs, and serialized data.

## Reliability

- Check concurrency, timeouts, resource leaks, idempotency, caching, and race conditions.
- Verify that long-running operations have clear failure behavior.
- Check whether the change handles unavailable services or missing optional dependencies.

## Tests

- Look for tests that exercise the changed behavior, important edge cases, and failure paths.
- Do not ask for tests only for coverage. Ask for tests when they would catch a realistic regression.
- Mention when tests were not run or cannot be verified from the available context.

## Maintainability

- Check whether the implementation follows existing local patterns.
- Flag duplication only when it is likely to cause bugs or inconsistent behavior.
- Avoid style-only feedback unless it obscures behavior or creates future risk.
