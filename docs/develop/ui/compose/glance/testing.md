---
title: Unit testing with Glance  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/glance/testing
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Unit testing with Glance Stay organized with collections Save and categorize content based on your preferences.



The Glance unit test API let you test your Glance code without inflating views
or needing a UI automator. For example, the unit test API lets you verify
conditions, such as whether elements are in a list or whether boxes have been
checked, using matchers such as `hasContentDescriptionEqualTo` or `isChecked`.

This API is lightweight and requires less setup, so you can perform test driven
development as you develop individual pieces of your widget and organize them to
improve code reuse.

**Note:** The test doesn't render the composables under test, so it doesn't
let you perform clicks. Instead, it uses matchers, which let you perform
assertions on actions in clickables such as starting a service or activity.

## Setup

The dependencies required to use the unit test library are shown in the
following examples:

```
// Other Glance and Compose runtime dependencies.
...
testImplementation 'androidx.glance:glance-testing:1.1.1'
testImplementation 'androidx.glance:glance-appwidget-testing:1.1.1'
...
// You may include additional dependencies, such as Robolectric, if your test
// needs to set a LocalContext.
```

## Test structure

Organize composable functions outside of the `GlanceAppWidget` class to enable
code reuse and unit testing. Reduce the complexity of your units under test as
much as possible.

You can target a test Composable with `provideComposable` and run your unit
tests on one or multiple Glance nodes with `onNode` or `onAllNodes`
respectively.

```
private const val FAKE_HEADLINE = "EXTRA! EXTRA! READ ALL ABOUT IT!"

class MyGlanceComposableTest {
    @Test
    fun myNewsItemComposable_largeSize_hasHeadline() = runGlanceAppWidgetUnitTest {
        // Set the composable to test
        provideComposable {
            MyNewsItemComposable(FAKE_HEADLINE)
        }

        // Perform assertions
        onNode(hasTestTag("headline"))
            .assertHasText(FAKE_HEADLINE)
    }


    @Composable
    fun MyNewsItemComposable(headline: String) {
        Row {
            Text(
                text = headline,
                modifier = GlanceModifier.semantics { testTag = "headline" },
            )
        }
    }
}

GlanceUnitTest.kt
```

## Set context and size for the test

If your composable function reads context using the `LocalContext.current()`
method, you must set a context using `setContext()`. Otherwise, this step is
optional.

You can use any JVM-based Android unit testing framework, such as Roboletric, to
provide the context.

If your composable function accesses `LocalSize`, set the intended size
for the test before providing a composable in the test. The default size is
349.dp x 455.dp, which is equivalent to a 5x4 widget shown on a Pixel 4 device
in portrait mode.

* If your AppWidget uses `sizeMode == Single`, you can set this to the
  `minWidth` and `minHeight` in your widget's `info.xml` file.
* If your AppWidget uses `sizeMode == Exact`, you can identify the sizes to
  test in a similar way to how you [determine a size for your widget](/develop/ui/views/appwidgets/layouts#anatomy_determining_size) and
  identify landscape and portrait sizes that your widget may appear on and test
  for them.
* If your AppWidget uses `sizeMode == Responsive`, you can set this to one of
  the sizes from the list that you provide when specifying the `sizeMode`.

The default duration for a test timeout is 1 second, but you can pass a custom
duration as an argument to the `runGlanceAppWidgetUnitTest` method if your test
infrastructure enforces a different timeout.

For more information and code samples, see the reference documentation for
[`runGlanceAppWidgetUnitTest`](/reference/kotlin/androidx/glance/appwidget/testing/unit/package-summary#runGlanceAppWidgetUnitTest(kotlin.time.Duration,kotlin.Function1)).

[Previous

arrow\_back

Handle errors with Glance](/develop/ui/compose/glance/error-handling)

[Next

Handle user interaction with Glance

arrow\_forward](/develop/ui/compose/glance/user-interaction)