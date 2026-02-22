---
title: https://developer.android.com/training/testing/fundamentals/what-to-test
url: https://developer.android.com/training/testing/fundamentals/what-to-test
source: md.txt
---

# What to test in Android

What you should test depends on factors such as the type of app, the development team, the amount of legacy code, and the architecture used. The following sections outline what a beginner might want to consider when planning what to test in their app.

## Organization of test directories

A typical project in Android Studio contains two directories that hold tests depending on their execution environment. Organize your tests in the following directories as described:

- The`androidTest`directory should contain the tests that run on real or virtual devices. Such tests include integration tests, end-to-end tests, and other tests where the JVM alone cannot validate your app's functionality.
- The`test`directory should contain the tests that run on your local machine, such as unit tests. In contrast to the above, these can be tests that run on a local JVM.

## Essential unit tests

When following best practice, you should ensure you use unit tests in the following cases:

- **Unit tests** for**ViewModels**, or presenters.
- **Unit tests** for the**data** layer, especially repositories. Most of the data layer should be platform-independent. Doing so enables test doubles to replace database modules and remote data sources in tests. See the guide on[using test doubles in Android](https://developer.android.com/training/testing/fundamentals/test-doubles)
- **Unit tests** for other platform-independent layers such as the**Domain**layer, as with use cases and interactors.
- **Unit tests** for**utility classes**such as string manipulation and math.

### Testing Edge Cases

Unit tests should focus on both normal and edge cases. Edge cases are uncommon scenarios that human testers and larger tests are unlikely to catch. Examples include the following:

- Math operations using negative numbers, zero, and[boundary conditions](https://en.wikipedia.org/wiki/Off-by-one_error).
- All the possible network connection errors.
- Corrupted data, such as malformed JSON.
- Simulating full storage when saving to a file.
- Object recreated in the middle of a process (such as an activity when the device is rotated).

### Unit Tests to Avoid

Some unit tests should be avoided because of their low value:

- Tests that verify the correct operation of the framework or a library, not your code.
- Framework entry points such as*activities, fragments, or services*should not have business logic so unit testing shouldn't be a priority. Unit tests for activities have little value, because they would cover mostly framework code and they require a more involved setup. Instrumented tests such as UI tests can cover these classes.

## UI tests

There are several types of UI tests you should employ:

- **Screen UI tests**check critical user interactions in a single screen. They perform actions such as clicking on buttons, typing in forms, and checking visible states. One test class per screen is a good starting point.
- **User flow tests** or**Navigation tests**, covering most common paths. These tests simulate a user moving through a navigation flow. They are simple tests, useful for checking for run-time crashes in initialization.

| **Note:** Test coverage is a metric that some testing tools can calculate, and indicates how much of your code is visited by your tests. It can detect untested portions of the codebase, but it should not be used as the only metric to claim a good testing strategy.

## Other tests

There are more specialized tests such as screenshot tests, performance tests, and[monkey tests](https://developer.android.com/studio/test/monkey). You can also categorize tests by purpose, such as regressions, accessibility, and compatibility.

## Further reading

In order to test in isolation, you oftentimes need to replace the dependencies of the subject under test with fake or mock dependencies, called "Test doubles" in general. Continue reading about them in[Using test doubles in Android](https://developer.android.com/training/testing/fundamentals/test-doubles).

If you want to learn how to create unit and UI tests, check out the[Testing codelabs](https://developer.android.com/codelabs/advanced-android-kotlin-training-testing-basics).