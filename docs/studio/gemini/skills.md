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

To import an Android skill into Android Studio, download the skills from the
[GitHub repository](https://github.com/android/skills) and save it in a directory called
`.skills/` or `.agent/skills/` at your project root.

To learn more about Android skills, see [Intro to Android skills](https://developer.android.com/tools/agents/android-skills).