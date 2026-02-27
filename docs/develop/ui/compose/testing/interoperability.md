---
title: https://developer.android.com/develop/ui/compose/testing/interoperability
url: https://developer.android.com/develop/ui/compose/testing/interoperability
source: md.txt
---

Compose integrates with common testing frameworks.

## Interoperability with Espresso

In a hybrid app, you can find Compose components inside view hierarchies and
views inside Compose composables (via the [`AndroidView`](https://developer.android.com/reference/kotlin/androidx/compose/ui/viewinterop/package-summary#AndroidView(kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Function1)) composable).

There are no special steps needed to match either type. You match views with
Espresso's [`onView`](https://developer.android.com/reference/androidx/test/espresso/Espresso#onView(org.hamcrest.Matcher%3Candroid.view.View%3E)), and Compose elements with the [`ComposeTestRule`](https://developer.android.com/reference/kotlin/androidx/compose/ui/test/junit4/ComposeTestRule).

    @Test
    fun androidViewInteropTest() {
        // Check the initial state of a TextView that depends on a Compose state.
        Espresso.onView(withText("Hello Views")).check(matches(isDisplayed()))
        // Click on the Compose button that changes the state.
        composeTestRule.onNodeWithText("Click here").performClick()
        // Check the new value.
        Espresso.onView(withText("Hello Compose")).check(matches(isDisplayed()))
    }

## Interoperability with UiAutomator

By default, composables are accessible from [UiAutomator](https://developer.android.com/training/testing/other-components/ui-automator) only by their
convenient descriptors (displayed text, content description, etc.). If you want
to access any composable that uses [`Modifier.testTag`](https://developer.android.com/reference/kotlin/androidx/compose/ui/Modifier#(androidx.compose.ui.Modifier).testTag(kotlin.String)), you need to enable
the semantic property `testTagsAsResourceId` for the particular composable's
subtree. Enabling this behavior is useful for composables that don't have any
other unique handle, such as scrollable composables (for example, `LazyColumn`).

> [!NOTE]
> **Note:** This feature is available in Jetpack Compose version 1.2.0-alpha08 and higher.

Enable the semantic property only once high in your composables hierarchy to
ensure all nested composables with `Modifier.testTag` are accessible from
UiAutomator.

    Scaffold(
        // Enables for all composables in the hierarchy.
        modifier = Modifier.semantics {
            testTagsAsResourceId = true
        }
    ){
        // Modifier.testTag is accessible from UiAutomator for composables nested here.
        LazyColumn(
            modifier = Modifier.testTag("myLazyColumn")
        ){
            // Content
        }
    }

Any composable with the `Modifier.testTag(tag)` can be accessible with the use
of [`By.res(resourceName)`](https://developer.android.com/reference/androidx/test/uiautomator/BySelector#res) using the same `tag` as the `resourceName`.

> [!CAUTION]
> **Caution:** Make sure you don't use [`By.res(resourcePackage, resourceId)`](https://developer.android.com/reference/androidx/test/uiautomator/BySelector#res_1) as this formats the argument as `$resourcePackage:id/$resourceId`, which is different from `Modifier.testTag`.

    val device = UiDevice.getInstance(getInstrumentation())

    val lazyColumn: UiObject2 = device.findObject(By.res("myLazyColumn"))
    // Some interaction with the lazyColumn.

## Additional Resources

- **[Test apps on Android](https://developer.android.com/training/testing)**: The main Android testing landing page provides a broader view of testing fundamentals and techniques.
- **[Fundamentals of testing](https://developer.android.com/training/testing/fundamentals):** Learn more about the core concepts behind testing an Android app.
- **[Local tests](https://developer.android.com/training/testing/local-tests):** You can run some tests locally, on your own workstation.
- **[Instrumented tests](https://developer.android.com/training/testing/instrumented-tests):** It is good practice to also run instrumented tests. That is, tests that run directly on-device.
- **[Continuous integration](https://developer.android.com/training/testing/continuous-integration):** Continuous integration lets you integrate your tests into your deployment pipeline.
- **[Test different screen sizes](https://developer.android.com/training/testing/different-screens):** With some many devices available to users, you should test for different screen sizes.
- **[Espresso](https://developer.android.com/training/testing/espresso)**: While intended for View-based UIs, Espresso knowledge can still be helpful for some aspects of Compose testing.