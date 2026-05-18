---
title: https://developer.android.com/studio/gemini/skills
url: https://developer.android.com/studio/gemini/skills
source: md.txt
---

Skills let you enhance Agent Mode's capabilities with specialized expertise
and custom workflows. They are based on the [Agent Skills](https://agentskills.io/)
open standard.

Unlike [`AGENTS.md`](https://developer.android.com/studio/gemini/agent-files) files, skills represent on-demand expertise. This
structure allows Agent Mode to maintain a large number of specialized
capabilities---such as migrating between specific library versions or making a
composable adapt to different screen sizes---without cluttering the model's
immediate context window.

The model autonomously decides when to employ a skill based on your request and
the skill's description. When a relevant skill is identified, the model
dynamically pulls in the full instructions and resources required to complete
the task.

To activate a skill on demand, ask the agent to perform a task that is relevant
to the skill. You can also enter `@` in the input box to trigger a specific
skill.

To import an Android skill into Android Studio, download the skill from the
[GitHub repository](https://github.com/android/skills) and save it in a directory called
`.agents/skills` or `.android-studio/skills` at your project root or your home
directory.

Note that Android Studio, before Quail, used to load skills from non-standard
directories --- `.skills` and `agent/skills`. If you have skills in those
locations, move them to `.agents/skills` or `.android-studio/skills` when
upgrading Android Studio to Quail 1 or later versions.

To learn more about Android skills, see [Intro to Android skills](https://developer.android.com/tools/agents/android-skills).