---
title: Customize your experience with Rules  |  Android Studio  |  Android Developers
url: https://developer.android.com/studio/gemini/rules
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Android Studio](https://developer.android.com/studio)
* [Gemini in Android Studio](https://developer.android.com/gemini-in-android)

# Customize your experience with Rules Stay organized with collections Save and categorize content based on your preferences.



Rules in Gemini let you define preferred coding languages, styles,
or output formats that apply to all prompts. When you set these
preferences once, they are automatically applied to all subsequent
prompts sent to Gemini. Rules help Gemini understand project
standards and preferences for more accurate and tailored code
assistance. For example, you can create a rule such as
"Always give me concise responses in Kotlin."

Store and manage rules in the [Prompt Library](/studio/gemini/prompt-library) in Android Studio.
To set up a rule, follow these steps:

1. To open Gemini's settings, click the Gemini status icon
   ![Gemini active status icon](/static/studio/gemini/images/gemini-active.png)
   at the bottom of the IDE and then click **Configure AI** >
   **Prompt Library**. Alternatively go to **File** (**Android Studio** on
   macOS) **> Settings > Tools > AI > Prompt Library**.
2. Use the **Scope** drop-down to store rules at the IDE level or the
   project level:
   * IDE-level rules are private to yourself and can be used across
     multiple projects.
   * Project-level rules can be shared among teammates working on the
     same project. They're saved in the `/.idea/project.prompts.xml`
     file with [project-level prompts](/studio/gemini/prompt-library#share-project-prompts).
3. To add a rule, click **Rules** and add the rule(s) in the editor.
   Make sure that the rules are specific and actionable. The layout of
   the rules isn't critical, but for your own readability and
   maintainability, consider putting multiple rules in a bullet list.
4. Click **Apply** to save and stay in the settings dialog. Click **OK**
   to save and exit the settings dialog.

![The Android Studio Settings dialog showing the Rules editor under Gemini > Prompt Library](/static/studio/images/rules.png)


**Figure 1**: Android Studio Settings dialog with the Rules editor open.

Here are some ideas of what to add as rules:

* Company style guides, for example conventions for variable naming or
  code commenting
* Recommended libraries to use
* Coding language preferences, for example "Provide all code examples
  in Kotlin"

## De-select rules for a query

Rules are automatically applied to every query you send to Gemini.
If you don't want the rules to apply to a specific prompt, you can
de-select the rules before you send the prompt by clicking **Context**
and un-checking **Rules**.

![The Context pop-up in the Gemini chat window, showing the Rules option enabled](/static/studio/gemini/images/select-rules.png)


**Figure 2**: The Context pop-up in the Gemini chat window, showing the Rules option enabled.

## How rules work

Rules are added to the beginning of every prompt as a *preamble*.
Use rules to provide context, specify a selected output and format,
and help shape Gemini's behavior to generate more accurate and helpful
responses. If you are using both IDE-level and project-level rules,
both categories of rules are applied to every prompt.