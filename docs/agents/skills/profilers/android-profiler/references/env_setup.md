---
title: https://developer.android.com/agents/skills/profilers/android-profiler/references/env_setup
url: https://developer.android.com/agents/skills/profilers/android-profiler/references/env_setup
source: md.txt
---

**`$SKILL_ROOT`** is the absolute path of the directory containing this
skill's `SKILL.md`. Every file the skill references is written as
`$SKILL_ROOT/<path>`, never relative to the file doing the referencing,
because the skill is loaded from a plugin directory, not from the
user's workspace.

Set it before running any command from this skill:

```bash
# Replace with the absolute path of the directory containing SKILL.md.
export SKILL_ROOT="/absolute/path/to/android-profiler"
```