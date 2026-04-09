---
title: Extend Agent Mode with skills  |  Android Studio  |  Android Developers
url: https://developer.android.com/studio/gemini/skills
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Android Studio](https://developer.android.com/studio)
* [Gemini in Android Studio](https://developer.android.com/gemini-in-android)

# Extend Agent Mode with skills Stay organized with collections Save and categorize content based on your preferences.




Skills let you enhance Agent Mode's capabilities with specialized expertise
and custom workflows. They are based on the [Agent Skills](https://agentskills.io/)
open standard.

Unlike [`AGENTS.md`](/studio/gemini/agent-files) files, skills represent on-demand expertise. This
structure allows Agent Mode to maintain a large number of specialized
capabilities—such as migrating between specific library versions or making a
composable adapt to different screen sizes—without cluttering the model's
immediate context window.

The model autonomously decides when to employ a skill based on your request and
the skill's description. When a relevant skill is identified, the model
dynamically pulls in the full instructions and resources required to complete
the task.

To activate a skill on demand, ask the agent to perform a task that is relevant
to the skill. You can also enter `@` in the input box to trigger a specific
skill.

## Key benefits

* **Shared expertise:** Package complex workflows (like a specific team's pull
  request review process) into a dedicated folder that anyone can use.
* **Repeatable workflows:** Ensure complex, multi-step tasks are performed
  consistently by providing standard instructions.
* **Resource bundling:** Include scripts, templates, or example data alongside
  your instructions so the agent has everything it needs in one place.
* **Efficient use of context window:** To save context tokens, only the skill's
  metadata (name and description) is loaded initially. The full `SKILL.md` file
  is only loaded upon activation. Supporting files within the `references/`,
  `scripts/`, or `assets/` directories only load into context when the agent
  specifically needs them.

## Create your own skills

The agent looks for skills starting from the `.skills/` or `.agent/skills/`
directories located at your project root. To build a custom skill, follow these
steps:

1. **Create a directory** for your skill (for example, `my-new-skill/`).
2. **Create a `SKILL.md` file** (case-sensitive) inside the new directory.

Skills must follow these rules:

* **One directory per skill:** Each skill must have its own unique directory
  that includes a `SKILL.md` file and any [additional resources](#directories).
* **Nesting:** All skills must be in the `.skills/` or `.agent/skills/`
  directory at the project root. However, you can use subdirectories for better
  organization (for example, `skills/ui-flows/<skill name>/SKILL.md` or
  `skills/testing/<skill name>/SKILL.md`).
* **Scope:** Currently, only skills located within the project's codebase are
  supported.

![](/static/studio/images/skill-files.png)

The `SKILL.md` file uses a YAML block for metadata and standard Markdown for the
instructions.

* `name`: A unique identifier for the skill. This should match the directory
  name.
* `description`: A clear explanation of what the skill does and when the agent
  should use it.
* **Body:** The Markdown body below the YAML block contains the instructions
  that guide the agent’s behavior when the skill is active.

```
---
name: skill-name
description: A description of what this skill does and when to use it.
metadata:
  author: example-org
  version: "1.0"
---

Skill content
```

### Format guidelines

* **Name:** Maximum of 64 characters (lowercase letters, numbers, and hyphens
  only).
* **Description:** Maximum of 1024 characters.
* **Body content:** Aim for 10k–20k characters (~2,500–5,000 tokens). If your
  instructions exceed this, consider moving detailed documentation to a resource
  file as described in [Optional skill directories](#directories).

### Optional skill directories

To keep your `SKILL.md` file concise and modular, you can include additional
resources in the following optional directories within your skill's folder:

* `scripts/`: Contains executable code (for example, Python or Bash) that the
  agent can run.
* `references/`: Contains detailed technical documentation, API references, or
  domain-specific guides.
* `assets/`: Contains static resources such as document templates, UI diagrams,
  or JSON schemas.

When referring to these files within your `SKILL.md` instructions, use relative
paths from the skill root. For example: `Run the script at scripts/cleanup.py`.