---
title: https://developer.android.com/studio/test
url: https://developer.android.com/studio/test
source: md.txt
---

# Test your app

This page describes various tools that help you create, configure, and run your tests from Android Studio or the command line.

If you want to learn more about the fundamentals of testing and how to write tests, see[Test apps on Android](https://developer.android.com/training/testing).

There are different ways to run and configure your tests:

- **Test in Android Studio**

  For basic testing needs, Android Studio includes features that help you create, run, and view results of tests all from the IDE. Using Android Studio, you can point and click in the app source code to create and run tests for specific classes or methods, use menus to configure multiple test devices, and interact with the Test Matrix tool window to visualize test results. For more information on how to use Android Studio to create and manage your tests, see[Test in Android Studio](https://developer.android.com/studio/test/test-in-android-studio).
- **Run tests from the command line**

  For more fine-grained control, you can run tests from the command line. Command-line testing provides a straightforward way to target modules or build variants individually or in combinations. Running tests through the Android Debug Bridge (adb) shell allows for the most customization in terms of which tests you want to run.

  Running tests from the command line is also useful on a[continuous integration system](https://developer.android.com/studio/projects/continuous-integration).

  For more information, see[Test from the command line](https://developer.android.com/studio/test/command-line).
- **Advanced testing**

  For advanced testing needs, you may want to override default settings, configure Gradle options, or refactor your code so that tests are separated in their own module. For more information about how to set up your test configurations for special use cases, see[Advanced test setup](https://developer.android.com/studio/test/advanced-test-setup).

  To test how your app behaves when your user interacts with it, you can use tools such as[Espresso Test Recorder](https://developer.android.com/studio/test/other-testing-tools/espresso-test-recorder),[App Crawler](https://developer.android.com/studio/test/other-testing-tools/app-crawler),[UI Automator](https://developer.android.com/training/testing/other-components/ui-automator), or[Monkey testing](https://developer.android.com/studio/test/other-testing-tools/monkey).