---
title: https://developer.android.com/agents/skills/performance/r8-analyzer/skill
url: https://developer.android.com/agents/skills/performance/r8-analyzer/skill
source: md.txt
---

## Step 1. Setup and configuration check

- Inspect `build.gradle`, `build.gradle.kts`, and `gradle.properties`.
- Use [references/CONFIGURATION.md](https://developer.android.com/agents/skills/performance/r8-analyzer/references/CONFIGURATION) to identify missing optimizations.
- **AGP** : If \< 9.0, suggest migration to 9.0 for [build time improvement
  performance](https://developer.android.com/topic/performance/app-optimization/enable-app-optimization#agp-r8-behavior-changes)
- **Full Mode** : Verify `android.enableR8.fullMode=false` is removed from gradle.properties.

## Step 2. Analysis path selection

- Inspect `build.gradle`, `build.gradle.kts`, and `gradle.properties` and
  `libs.versions.toml` to get the R8 version

- **If R8 \>= 9.3.7-dev** : Proceed to **Path A (Quantitative)**.

- **If R8 \< 9.3.7-dev** : Proceed to **Path B (Heuristic)**.

### Path A: Quantitative data generation (R8 \>= 9.3.7-dev)

- **Check requirements** : Python and `protobuf` package are mandatory.
- **Generate and analyze** : You MUST run the shell commands described in [references/CONFIGURATION-ANALYZER.md](https://developer.android.com/agents/skills/performance/r8-analyzer/references/CONFIGURATION-ANALYZER) to generate the proto file using R8 configuration analyzer, convert it to json and analyze the result.
- **Report** : Rely entirely on the generated file `analysis.txt` for scores and rule impact metrics. Proceed to Step 3.

### Path B: Heuristic evaluation and recommendation (R8 \< 9.3.7-dev)

*(Use ONLY if quantitative data generation is not possible)*

- **Manual evaluation** : Inspect `proguard-rules.pro`.
- **Library check** : Compare rules against [references/REDUNDANT-RULES.md](https://developer.android.com/agents/skills/performance/r8-analyzer/references/REDUNDANT-RULES). Suggest **Remove** for bundled rules.
- **Custom rule check** : Use [references/KEEP-RULES-IMPACT-HIERARCHY.md](https://developer.android.com/agents/skills/performance/r8-analyzer/references/KEEP-RULES-IMPACT-HIERARCHY) and [references/REFLECTION-GUIDE.md](https://developer.android.com/agents/skills/performance/r8-analyzer/references/REFLECTION-GUIDE) to prioritize and evaluate. Suggest **Refine** for broad rules (for example, package-wide).
- **Validation** : Suggest Macrobenchmark tests using [UI Automator](https://developer.android.com/training/testing/other-components/ui-automator) for any proposed changes. Proceed to Step 3.

## Step 3. Report generation

- **Format** : Follow [references/REPORT_FORMAT.md](https://developer.android.com/agents/skills/performance/r8-analyzer/references/REPORT_FORMAT) strictly.
- **Input**: Extract metrics (Scores, Impacts, Example Classes) directly from generated file analysis.txt if using Path A, or from manual findings if using Path B.
- **Output** : Output ONLY the raw Markdown report in the chat. Do NOT output conversational filler (for example, "Here is your report..."). Do NOT provide recommendations, next steps, or any other text outside of the sections defined in [references/REPORT_FORMAT.md](https://developer.android.com/agents/skills/performance/r8-analyzer/references/REPORT_FORMAT) Do NOT mention the path used for analysis of the configuration

## Constraints

- **Strict output limit**: The final output MUST strictly be the Markdown report and nothing else.
- **No code changes**: Research and suggest only; Do not modify files.
- **No redundancy**: Do not explain R8 benefits or reference skill internal files in the report.
- **Focus**: Omit sections (for example, Subsumed Rules, Configuration) if no issues or items are found.