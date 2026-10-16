---
title: https://developer.android.com/agents/skills/performance/anr-audit-and-fix/skill
url: https://developer.android.com/agents/skills/performance/anr-audit-and-fix/skill
source: md.txt
---

Select the execution path matching the user's request:

## 1. Path A: Static codebase ANR risk audit

When auditing source files or scanning for thread-blocking operations:

- Follow [references/risk_analysis_guide.md](https://developer.android.com/agents/skills/performance/anr-audit-and-fix/references/risk_analysis_guide) step by step: list candidates, **prove the executing thread** (trace callers when the thread depends on them), **prove the call blocks**, then attribute and grade. Report only candidates that pass these checks; list the dismissed ones separately with a one-line reason.
- Evaluate off-main-thread mutations of attached Views not merely as crash risks (`CalledFromWrongThreadException`), but as **Sync Barrier Leak ANR** risks with their own proof (off-main execution plus an attached View).

## 2. Path B: Trace-driven diagnosis and remediation

When analyzing ANR traces or stack dumps:

- Diagnose systematically using [references/trace_analysis_guide.md](https://developer.android.com/agents/skills/performance/anr-audit-and-fix/references/trace_analysis_guide) and format the report with [references/anr_trace_report_template.md](https://developer.android.com/agents/skills/performance/anr-audit-and-fix/references/anr_trace_report_template).
- Base findings strictly on log evidence. Propose application fixes **only** for `APP_DEFECT` or `APP_RESOURCE_OVERLOAD` (never for `EXTERNAL_BOTTLENECK`).