---
title: https://developer.android.com/studio/gemini/generate-unit-test-scenarios
url: https://developer.android.com/studio/gemini/generate-unit-test-scenarios
source: md.txt
---

# Generate unit test scenarios

When writing unit tests for your app, Gemini can suggest test scenarios using the context of the code you want to test. When generating unit test scenarios, Gemini includes detailed names and descriptions for your tests, so that you better understand the intention for each suggested test. You need to implement the body of each test yourself.

To generate unit test scenarios, do the following:

1. Navigate to the class you want to generate unit test scenarios for.
2. Right-click on the class name and select**Gemini \> Generate Unit Test Scenarios**from the context menu.
3. In the dialog that appears, select the methods of the class that you want to generate scenarios for, and set the destination package for the tests.
4. Click**OK**.
5. Confirm the destination directory for your tests and click**OK**.
6. If the test class already exists, confirm whether you want Gemini to suggest updates to the existing file.

After Gemini processes the request, you should see either a new file with the suggested unit tests or a diff for you to accept recommended changes to an existing file.

![Unit test scenario generation demo](https://developer.android.com/static/studio/gemini/images/unit-test-scenario.gif)