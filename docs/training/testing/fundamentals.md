---
title: https://developer.android.com/training/testing/fundamentals
url: https://developer.android.com/training/testing/fundamentals
source: md.txt
---

This page outlines the core tenets of testing Android apps, including the central best practices and their benefits.

## Benefits of testing

Testing is an integral part of the app development process. By running tests against your app consistently, you can verify your app's correctness, functional behavior, and usability before you release it publicly.

You can*manually*test your app by navigating through it. You might use different devices and emulators, change the system language, and try to generate every user error or traverse every user flow.

However, manual testing scales poorly, and it can be easy to overlook regressions in your app's behavior.*Automated testing*involves using tools that perform tests for you, which is faster, more repeatable, and generally gives you more actionable feedback about your app earlier in the development process.

## Types of tests in Android

Mobile applications are complex and must work well in many environments. As such, there are many types of tests.

### Subject

For example, there are different types of tests depending on the*subject*:

- **Functional testing**: does my app do what it's supposed to?
- **Performance testing**: does it do it quickly and efficiently?
- **Accessibility testing**: does it work well with accessibility services?
- **Compatibility testing**: does it work well on every device and API level?

### Scope

Tests also vary depending on*size* , or*degree of isolation*:

- **Unit tests** or**small tests**only verify a very small portion of the app, such as a method or class.
- **End-to-end** tests or**big tests**verify larger parts of the app at the same time, such as a whole screen or user flow.
- **Medium tests** are in between and check the**integration**between two or more units.

![Tests can be either small, medium, or big.](https://developer.android.com/static/training/testing/fundamentals/test-scopes.png)**Figure 1**: Test scopes in a typical application.

There are many ways to classify tests. However, the most important distinction for app developers is where tests run.

## Instrumented versus local tests

You can run tests on an Android device or on another computer:

- **Instrumented tests** run on an Android device, either physical or emulated. The app is built and installed alongside a*test app*that injects commands and reads the state. Instrumented tests are usually UI tests, launching an app and then interacting with it.
- **Local tests** execute on your development machine or a server, so they're also called*host-side tests*. They're usually small and fast, isolating the subject under test from the rest of the app.

![Tests can run as instrumented tests on a device, or local tests on your development machine.](https://developer.android.com/static/training/testing/fundamentals/instru-vs-local.png)**Figure 2**: Different types of tests depending on where they run.

Not all unit tests are local, and not all end-to-end tests run on a device. For example:

- **Big local test** : You can use an Android simulator that runs locally, such as[Robolectric](https://developer.android.com/training/testing/local-tests/robolectric).
- **Small instrumented test**: You can verify that your code works well with a framework feature, such as a SQLite database. You might run this test on multiple devices to check the integration with multiple versions of SQLite.

### Examples

The following snippets demonstrate how to interact with the UI in an*instrumented UI test*that clicks on an element and verifies that another element is displayed.  

### Espresso

    // When the Continue button is clicked
    onView(withText("Continue"))
        .perform(click())

    // Then the Welcome screen is displayed
    onView(withText("Welcome"))
        .check(matches(isDisplayed()))

### Compose UI

    // When the Continue button is clicked
    composeTestRule.onNodeWithText("Continue").performClick()

    // Then the Welcome screen is displayed
    composeTestRule.onNodeWithText("Welcome").assertIsDisplayed()

This snippet shows part of a*unit test*for a ViewModel (local, host-side test):  

    // Given an instance of MyViewModel
    val viewModel = MyViewModel(myFakeDataRepository)

    // When data is loaded
    viewModel.loadData()

    // Then it should be exposing data
    assertTrue(viewModel.data != null)

## Testable architecture

With a testable app architecture, the code follows a structure that allows you to easily test different parts of it in isolation. Testable architectures have other advantages, such as better readability, maintainability, scalability, and reusability.

An architecture that is*not testable*produces the following:

- Bigger, slower, more flaky tests. Classes that can't be unit-tested might have to be covered by bigger integration tests or UI tests.
- Fewer opportunities for testing different scenarios. Bigger tests are slower, so testing all possible states of an app might be unrealistic.

To learn more about architecture guidelines, see the[guide to app architecture](https://developer.android.com/jetpack/guide).

### Approaches to decoupling

If you can extract part of a function, class, or module from the rest, testing it is easier, and more effective. This practice is known as decoupling, and it is the concept most important to testable architecture.

Common decoupling techniques include the following:

- Split an app into*layers* such as Presentation, Domain, and Data. You can also split an app into*modules*, one per feature.
- Avoid adding logic to entities that have large dependencies, such as activities and fragments. Use these classes as entry points to the framework and move*UI and business logic*elsewhere, such as to a Composable, ViewModel, or domain layer.
- Avoid direct*framework dependencies* in classes containing business logic. For example,[don't use Android Contexts in ViewModels](https://medium.com/androiddevelopers/locale-changes-and-the-androidviewmodel-antipattern-84eb677660d9).
- Make dependencies easy to*replace* . For example, use[interfaces](https://en.wikipedia.org/wiki/Interface_segregation_principle)instead of concrete implementations. Use[Dependency injection](https://developer.android.com/training/dependency-injection)even if you don't use a DI framework.

## Next steps

Now that you know why you should test and the two main types of tests, you can read[What to test](https://developer.android.com/training/testing/fundamentals/what-to-test)or learn about[Testing strategies](https://developer.android.com/training/testing/fundamentals/strategies)

Alternatively, if you want to create your first test and learn by doing, check out the[Testing codelabs](https://developer.android.com/codelabs/advanced-android-kotlin-training-testing-basics).