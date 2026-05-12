# test-force-push-rebase

A/B test repo for sonarcloud-code-review PR #431 — "force full review when rebase shifts the merge-base".

## Scenarios

- **PR A (regression)**: renovate-style — branch is rebased onto a newer base. The merge-base shifts, so the bot must do a full review against the current base. Pre-fix bug: bot would review the upstream churn between the old and new merge-bases.
- **PR B (control)**: `git commit --amend` style — branch diverges from the previously reviewed commit, but the merge-base is unchanged. The bot should still do smart-incremental on the amend delta.

## How to read the results

For each PR, the bot posts an initial review at the first commit. Then we force-push and wait for a follow-up review. The follow-up's content is the evidence:
- PR A post-fix: should mention only the dependency change, never the unrelated security/validation files added on main.
- PR B post-fix: should mention the amend delta and use the "rebased / force-pushed" mode note.
