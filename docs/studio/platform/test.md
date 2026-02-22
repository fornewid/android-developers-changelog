---
title: https://developer.android.com/studio/platform/test
url: https://developer.android.com/studio/platform/test
source: md.txt
---

# Test platform code with atest

Android Studio for Platform (ASfP) integrates with the`atest`command-line tool, letting you run tests on your connected device or emulator directly from the IDE.

## Prerequisites

- Open an ASfP project with your AOSP source code.
- Successfully build and flash your code to a device or emulator.
- Initialize your build environment using`source build/envsetup.sh`and`lunch`.

## Run tests

You can run tests using`atest`in ASfP in several ways:

- **Gutter run icons:** Click the**Run** iconplay_circle

  next to a test class or method in the editor to run that specific test.
- **Right-click menu:** Right-click on a test file, class, or method in the Project window or editor and select**Run 'atest'**.

- **Using the terminal:** Open the integrated terminal in ASfP (**View \> Tool Windows \> Terminal** ) and run`atest`commands directly. For example:`bash
  atest MyTestModule
  atest MyTestClass#myTestMethod`

## View test results

Test results are displayed in the**Run**tool window within ASfP. This window shows the test progress, pass or fail status, and provides logs and output for each test.

## Test configurations

When you run a test from the gutter or right-click menu, ASfP automatically creates a temporary run or debug configuration. You can modify and save these configurations to quickly re-run tests with specific options or flags:

1. Go to**Run \> Edit Configurations**.
2. Find the`atest`configuration you want to modify or create a new one by clicking the**+** button and selecting**atest**.
3. Specify the test module, class, method, and add any necessary`atest`command-line options.

## Tips for testing

- **Targeted testing:** Run only the specific tests you need to save time. Use the format`Module:Class#Method`or other`atest`filters.
- **Use emulator snapshots:**For faster test runs on emulators, consider using snapshots to quickly revert to a known good state.
- **Check logs:** Use the logs in the**Run**tool window to diagnose any test failures.