---
title: https://developer.android.com/agents/skills/performance/r8-analyzer/skill
url: https://developer.android.com/agents/skills/performance/r8-analyzer/skill
source: md.txt
---

## Step 1. Setup and Configuration Check

- Inspect `build.gradle`, `build.gradle.kts`, and `gradle.properties`.
- Use [/references/CONFIGURATION.md](https://developer.android.com/agents/skills/performance/r8-analyzer/references/CONFIGURATION) to identify missing optimizations.
- **AGP** : If \< 9.0, suggest migration to 9.0 for [build time improvement
  performance](https://developer.android.com/topic/performance/app-optimization/enable-app-optimization#agp-r8-behavior-changes)
- **Full Mode** : Verify `android.enableR8.fullMode=false` is removed from gradle.properties.

## Step 2. Analysis Path Selection

- Inspect `build.gradle`, `build.gradle.kts`, and `gradle.properties`
  and `libs.versions.toml` to
  get the R8 version

- **If R8 \>= 9.3.7-dev** : Proceed to **Path A (Quantitative)**.

- **If R8 \< 9.3.7-dev** : Proceed to **Path B (Heuristic)**.

### Path A: Quantitative Data Generation (R8 \>= 9.3.7-dev)

- **Check Requirements** : Python and `protobuf` package are mandatory.
- **Generate and Analyze** : You MUST run the shell commands described in `[/references/CONFIGURATION-ANALYZER.md][7]` to generate the proto file using R8 configuration analyzer, convert it to json and analyze the result.
- **Report**: Rely entirely on the generated file analysis.txt for scores and rule impact metrics. Proceed to Step 3.

### Path B: Heuristic Evaluation and Recommendation (R8 \< 9.3.7-dev)

*(Use ONLY if quantitative data generation is not possible)*

- **Manual Evaluation** : Inspect `proguard-rules.pro`.
- **Library Check** : Compare rules against [/references/REDUNDANT-RULES.md](https://developer.android.com/agents/skills/performance/r8-analyzer/references/REDUNDANT-RULES) .Suggest **Remove** for bundled rules.
- **Custom Rule Check** : Use [/references/KEEP-RULES-IMPACT-HIERARCHY.md](https://developer.android.com/agents/skills/performance/r8-analyzer/references/KEEP-RULES-IMPACT-HIERARCHY) and [/references/REFLECTION-GUIDE.md](https://developer.android.com/agents/skills/performance/r8-analyzer/references/REFLECTION-GUIDE) to prioritize and evaluate. Suggest **Refine** for broad rules (e.g., package-wide).
- **Validation** : Suggest Macrobenchmark tests using [ui automator](https://developer.android.com/training/testing/other-components/ui-automator) for any proposed changes. Proceed to Step 3.

## Step 3. Report Generation

- **Format** : Follow `[/references/REPORT_FORMAT.md][8]` strictly.
- **Input**: Extract metrics (Scores, Impacts, Example Classes)
  directly from generated file analysis.txt if using Path A,
  or from manual findings if using Path B.

- **Output** :
  Output ONLY the raw Markdown report in the chat.
  Do NOT output conversational filler (e.g., "Here is your report...").
  Do NOT provide recommendations, next steps,
  or any other text outside of the sections defined in
  `[/references/REPORT_FORMAT.md][8]`
  Do NOT mention the path used for analysis of the configuration

## Constraints

- **Strict Output Limit**: The final output MUST strictly be the Markdown report and nothing else.
- **No Code Changes**: Research and suggest only; Do not modify files.
- **No Redundancy**: Do not explain R8 benefits or reference skill internal files in the report.
- **Focus**: Omit sections (e.g., Subsumed Rules, Configuration) if no issues or items are found.