---
title: https://developer.android.com/agents/skills/performance/r8-analyzer/skill
url: https://developer.android.com/agents/skills/performance/r8-analyzer/skill
source: md.txt
---

## Step 1. Setup and configuration check

- Inspect `build.gradle`, `build.gradle.kts`, and `gradle.properties`.
- Use [references/CONFIGURATION.md](https://developer.android.com/agents/skills/performance/r8-analyzer/references/CONFIGURATION) to identify missing optimizations.
- **AGP** : If the version is lower than 9.3, suggest migration to 9.3 for the simplified [`optimization {}` DSL](https://developer.android.com/topic/performance/app-optimization/enable-app-optimization) and the Configuration Analyzer task.
- **Full mode** : Verify `android.enableR8.fullMode=false` is removed from the `gradle.properties` file.

## Step 2. Analysis path selection

- Inspect `build.gradle`, `build.gradle.kts`, `settings.gradle`, `settings.gradle.kts`, `gradle.properties`, and `libs.versions.toml` to get the AGP and R8 versions. An R8 version pinned in `settings.gradle(.kts)` replaces the R8 bundled with AGP.
- Find the app module (usually `app`) and a build variant with R8 enabled (usually `release`). The following commands use them as `<module>` and `<Variant>`, for example `:app:minifyReleaseWithR8`.
- The helper scripts are in this skill's `scripts/` directory. In the following
  commands, `<skill_dir>` is this skill's directory. Run every command from the
  project root.

- **If AGP \>= 9.3.0** : Proceed to **Path A (Standalone Task)**.

- **If AGP \< 9.3.0** : Proceed to **Path B (Quantitative)**.

### Path A: Standalone Gradle task (AGP \>= 9.3.0)

- **Step 1: Check requirements** : Python and the `protobuf` package 6.33.4 or later are mandatory (used by [`scripts/keep_radius_pb2.py`](https://developer.android.com/agents/skills/performance/r8-analyzer/scripts/keep_radius_pb2.py.rawcontent)). Install it with `pip install "protobuf>=6.33.4"`; versions lower than 6.33.4 fail on import with a `VersionError` or `ImportError`.
- **Step 2: Run standalone task on R8-enabled build** : For the module and variant you found during path selection, run `./gradlew :<module>:analyze<Variant>R8Config` (for example, `./gradlew :app:analyzeReleaseR8Config`). It generates the report in `<module>/build/reports/r8/` (for example, `app/build/reports/r8/r8-config-analyzer-release.pb`). You must wait for this command to finish before proceeding.
- **Step 3: Convert to JSON** : You must explicitly run the conversion script [`scripts/convert_pb_to_json.py`](https://developer.android.com/agents/skills/performance/r8-analyzer/scripts/convert_pb_to_json.py.rawcontent) as `python3 <skill_dir>/scripts/convert_pb_to_json.py` with arguments `<module>/build/reports/r8` and `tmp/keepradius/keepruleradius.json`. Wait for this command to finish.
- **Step 4: Analyze** : You must explicitly run the analysis script [`scripts/analyze.py`](https://developer.android.com/agents/skills/performance/r8-analyzer/scripts/analyze.py.rawcontent) by executing `python3 <skill_dir>/scripts/analyze.py tmp/keepradius/keepruleradius.json`. This outputs `tmp/keepradius/analysis_result.txt`. Wait for this command to finish.

### Path B: Invoke R8 release build (AGP \< 9.3.0)

- **Step 1: Check requirements** : Python and the `protobuf` package 6.33.4 or later are mandatory: `pip install "protobuf>=6.33.4"`.
- **Step 2: Generate and analyze** : You must run the shell commands described in [references/FULL_BUILD_CONFIG_ANALYZER.md](https://developer.android.com/agents/skills/performance/r8-analyzer/references/FULL_BUILD_CONFIG_ANALYZER) to temporarily update the R8 version in `settings.gradle(.kts)` to 9.4.34 or later (so R8 generates the report), generate the proto report in `tmp/r8analysis/`, convert it to `tmp/r8analysis/keepruleradius.json`, analyze the result, and revert the temporary `settings.gradle(.kts)` change.
- **Step 3: Analyze** : Verify that the analysis outputs `tmp/r8analysis/analysis_result.txt` for scores and rule impact metrics.

## Step 3. Report generation

- **Format** : Follow [references/REPORT_FORMAT.md](https://developer.android.com/agents/skills/performance/r8-analyzer/references/REPORT_FORMAT) strictly.
- **Redundant rules** : Check keep rules against [references/INSPECT-RULES.md](https://developer.android.com/agents/skills/performance/r8-analyzer/references/INSPECT-RULES). If a keep rule matches a pattern in [references/INSPECT-RULES.md](https://developer.android.com/agents/skills/performance/r8-analyzer/references/INSPECT-RULES), include the guidance and remediation from that reference alongside the impact metrics.
- **Input** : Extract metrics (Scores, Impacts, Example Classes, rule origins) directly from the generated file `tmp/keepradius/analysis_result.txt` if using Path A, or `tmp/r8analysis/analysis_result.txt` if using Path B.
- **Output** : Short progress updates are fine while Gradle runs; the final message is the report only. Output only the raw Markdown report in the chat. Do not output conversational filler (for example, "Here is your report..."). Do not provide recommendations, next steps, or any other text outside of the sections defined in [references/REPORT_FORMAT.md](https://developer.android.com/agents/skills/performance/r8-analyzer/references/REPORT_FORMAT). Do not mention the path used for analysis of the configuration.

## Constraints

- **Strict output limit**: The final output must strictly be the Markdown report and nothing else.
- **No code changes** : Research and suggest only; do not modify project files. Create files only under `tmp/` (analysis output, the settings backup, and any scratch scripts), and never write the report to a file. The one exception is the temporary R8 `classpath` in `settings.gradle(.kts)` that Path B needs when the project doesn't already pin R8 9.4.34 or later: ask the user first when running interactively, and revert it after the analysis (see [references/FULL_BUILD_CONFIG_ANALYZER.md](https://developer.android.com/agents/skills/performance/r8-analyzer/references/FULL_BUILD_CONFIG_ANALYZER)). If that change is needed but the user says no, or asks you not to edit build files, report rule-level and build file findings without scores and say why.
- **No placeholder scores** : Never print `N/A%` as a score.
- **No redundancy**: Do not explain R8 benefits or reference skill internal files in the report.
- **Focus**: Omit sections (for example, Subsumed Rules, Configuration) if no issues or items are found.