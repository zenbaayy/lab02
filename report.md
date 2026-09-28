# Lab 02 Report — CSE325-2026-L02-M4RB

## Task 1: Baseline (before any AI critique)
Verbatim ruff / radon output + commit hash containing file AND baseline:
```
<PASTE>
```
Measured against the construction baseline. CSE325-2026-L02-M4RB-T1

## Task 2: Accept / reject table (use quotes from YOUR LLM's critique)
| Suggestion (quoted) | Verdict | Reason (must name something in the file) |
|---|---|---|
| "<split run() ...>" | ACCEPT | run() does parsing, grading and printing in one 40-line body |
| "<rename d>" | ACCEPT | `d` holds student records and is used across the whole function |
| "<extract grade logic>" | ACCEPT | the A/B/C/F ladder is copy-pasted three times |
| "<remove unused params verbose, flag, mode, extra, path>" | REJECT | changes run()'s public signature and would break existing callers |
| "<rename loop vars r, p, m>" | REJECT | cosmetic; the loops are 3-6 lines each |

Measured against the construction baseline. CSE325-2026-L02-M4RB-T2

## Task 3: Before / after (paste real tool output)
| Metric | Before | After | Why it moved |
|---|---|---|---|
| Longest function (lines) | | | |
| Max cyclomatic complexity | | | |
| Duplicate grade blocks | 3 | 0 | letter_grade() |
| Params on worst function | 6 | 6 | did NOT move: kept for API compatibility (explain!) |

Measured against the construction baseline. CSE325-2026-L02-M4RB-T3

## Task 4: Behaviour preserved
`pytest -q` output on both modules: `<PASTE>`
What these tests would NOT catch: they only cover 3 inputs and do not test
non-numeric marks or empty input.

Measured against the construction baseline. CSE325-2026-L02-M4RB-T4
