---
title: https://developer.android.com/studio/gemini/generate-unit-tests
url: https://developer.android.com/studio/gemini/generate-unit-tests
source: md.txt
---

> [!NOTE]
> **Note:** **Generate unit tests** is a preview feature and only available in Android Studio Panda 4 \| 2025.3.4 Canary 3 or higher. If you are on an earlier version, you can [generate unit test scenarios](https://developer.android.com/studio/gemini/generate-unit-tests#generate-scenarios).

Gemini in Android Studio can generate comprehensive, compilable unit tests for
your Kotlin and Java code. Gemini analyzes your source code to identify
constructor dependencies, business logic branches, and edge cases, and then
automatically creates a complete test class. This includes the generation of
`setUp` methods, mock initialization, and individual test cases tailored to your
project's specific architecture and coding style.

Gemini detects your project's existing configuration and uses the appropriate
frameworks and mocking libraries. This helps you bootstrap test
classes, saving you time on repetitive setup.

## Prerequisites

This feature is available in Android Studio Panda 4 \| 2025.3.4 Canary 3 or higher.

## Generate unit tests from the editor

To generate unit tests from the Android Studio editor, do the following:

1. Open a Kotlin or Java source file in the Android Studio editor.
2. Right-click a class name or a specific method, or select a block of code, and then select **AI \> Generate Unit Tests**.

## Generate unit tests from the tool window

To ask Gemini directly to generate unit tests, do the following:

1. Click **Agent** in the tool window bar.
2. Enter a request such as "Generate unit tests for this file" or "Write unit tests for MyClass".

**Figure 1.** Unit test generation demo

<br />


**Figure 2.** Unit test generation with code selection demo

<br />

## Generate unit test scenarios

> [!NOTE]
> **Note:** The ability to generate only test scenarios is being upgraded by [Generate
> unit tests](https://developer.android.com/studio/gemini/generate-unit-tests#prerequisites), which offers more comprehensive test generation, including test implementation.

When writing unit tests for your app, Gemini can suggest test scenarios using
the context of the code you want to test. When generating unit test scenarios,
Gemini includes detailed names and descriptions for your tests, so that you
better understand the intention for each suggested test. You need to implement
the body of each test yourself.

To generate unit test scenarios, do the following:

1. Navigate to the class you want to generate unit test scenarios for.
2. Right-click on the class name and select **Gemini \> Generate Unit Test Scenarios** from the context menu.
3. In the dialog that appears, select the methods of the class that you want to generate scenarios for, and set the destination package for the tests.
4. Click **OK**.
5. Confirm the destination directory for your tests and click **OK**.
6. If the test class already exists, confirm whether you want Gemini to suggest updates to the existing file.

After Gemini processes the request, you should see either a new file with the
suggested unit tests or a diff for you to accept recommended changes to an
existing file.
![Unit test scenario generation demo](https://developer.android.com/static/studio/gemini/images/unit-test-scenario.gif) **Figure 3.** Unit test scenario generation demo

<br />