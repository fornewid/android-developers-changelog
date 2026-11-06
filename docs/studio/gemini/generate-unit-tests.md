---
title: https://developer.android.com/studio/gemini/generate-unit-tests
url: https://developer.android.com/studio/gemini/generate-unit-tests
source: md.txt
---

The agent can generate comprehensive, compilable unit tests
for your Kotlin and Java code. Powered by the model of your choice, the
agent analyzes your source code to identify constructor dependencies, business
logic branches, and edge cases, and then automatically creates a complete test
class. This includes the generation of `setUp` methods, mock initialization,
and individual test cases tailored to your project's specific architecture and
coding style.

The agent detects your project's existing configuration and uses the
appropriate frameworks and mocking libraries. This helps you bootstrap test
classes, saving you time on repetitive setup.

## Generate unit tests from the editor

To generate unit tests from the Android Studio editor, do the following:

1. Open a Kotlin or Java source file in the Android Studio editor.
2. Right-click a class name or a specific method, or select a block of code, and then select **AI \> Generate Unit Tests**.

## Generate unit tests from the tool window

To ask the agent directly to generate unit tests, do the following:

1. Click **Agent** in the tool window bar.
2. Enter a request such as "Generate unit tests for this file" or "Write unit tests for MyClass".

**Figure 1.** Unit test generation demo

<br />


**Figure 2.** Unit test generation with code selection demo

<br />