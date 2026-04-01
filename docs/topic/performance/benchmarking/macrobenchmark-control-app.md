---
title: Control your app from Macrobenchmark  |  App quality  |  Android Developers
url: https://developer.android.com/topic/performance/benchmarking/macrobenchmark-control-app
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [App quality](https://developer.android.com/quality)
* [Technical quality](https://developer.android.com/quality/technical)

# Control your app from Macrobenchmark Stay organized with collections Save and categorize content based on your preferences.



Unlike most Android UI tests, Macrobenchmark tests run in a separate process
from the app itself. This is necessary to enable things like stopping the
app process and compiling from DEX bytecode to machine code.

You can drive your app's state using the [UIAutomator library](/training/testing/ui-automator) or other
mechanisms that can control the target app from the test process.
You can't use [Espresso](/training/testing/espresso) or [`ActivityScenario`](/reference/androidx/test/core/app/ActivityScenario) for
Macrobenchmark because they expect to run in a shared process with the app.

The following example finds a [`RecyclerView`](/reference/androidx/recyclerview/widget/RecyclerView) using its resource ID and
scrolls down several times:

### Kotlin

```
@Test
fun scrollList() {
    benchmarkRule.measureRepeated(
        // ...
        setupBlock = {
            uiAutomator {
                // Before starting to measure, navigate to the UI to be measured
                startIntent(Intent("$packageName.RECYCLER_VIEW_ACTIVITY"))
            }
        }
    ) {
        uiAutomator {
            val recycler = onElement { className == "androidx.recyclerview.widget.RecyclerView" }
            // Scroll down several times
            repeat(3) { recycler.fling(Direction.DOWN) }
        }

    }
}

FrameTimingBenchmark.kt
```

### Java

```
@Test
public void scrollList() {
    benchmarkRule.measureRepeated(
        // ...
        /* setupBlock */ scope -> {
            // Before measuring, navigate to the UI to be measured.
            val intent = Intent("$packageName.RECYCLER_VIEW_ACTIVITY")
            scope.startActivityAndWait();
            return Unit.INSTANCE;
        },
        /* measureBlock */ scope -> {
            UiDevice device = scope.getDevice();
            UiObject2 recycler = device.findObject(By.res(scope.getPackageName(), "recycler"));

            // Set gesture margin to avoid triggering gesture navigation
            // with input events from automation.
            recycler.setGestureMargin(device.getDisplayWidth() / 5);

            // Fling the recycler several times.
            for (int i = 0; i < 3; i++) {
                recycler.fling(Direction.DOWN);
            }

            return Unit.INSTANCE;
        }
    );
}
```

Your benchmark doesn't have to scroll the UI. Instead, it can run an
animation, for example. It also doesn't need to use UI Automator
specifically. It collects performance metrics as long as frames are being
produced by the view system, including frames produced by [Jetpack Compose](/jetpack/compose).

**Note:** When accessing UI objects, specify the `packageName`, because the tests
run in a separate process.

## Navigate to internal parts of the app

Sometimes you want to benchmark parts of your app that aren't directly
accessible from outside. This might be, for example, accessing inner Activities
that are marked with [`exported=false`](/guide/topics/manifest/activity-element#exported), navigating to a [`Fragment`](/reference/android/app/Fragment), or swiping
some part of your UI away. The benchmarks need to manually navigate to these
parts of the app like a user.

To manually navigate, change the code inside `setupBlock{}` to contain the
effect you want, such as button tap or swipe. Your `measureBlock{}` contains
only the UI manipulation you want to actually benchmark:

### Kotlin

```
@Test
fun nonExportedActivityScrollList() {
    benchmarkRule.measureRepeated(
        // ...
        setupBlock = setupBenchmark()
    ) {
        // ...
    }
}

private fun setupBenchmark(): MacrobenchmarkScope.() -> Unit = {
    uiAutomator {
        // Before starting to measure, navigate to the UI to be measured
        startApp(TARGET_PACKAGE)
        // click a button to launch the target activity.
        onElement { textAsString() == "RecyclerView" }.click()
        // wait until the activity is shown
        waitForStableInActiveWindow()
    }
}

NonExportedActivityBenchmark.kt
```

### Java

```
@Test
public void scrollList() {
    benchmarkRule.measureRepeated(
        // ...
        /* setupBlock */ scope -> {
            // Before measuring, navigate to the default activity.
            scope.startActivityAndWait();

            // Click a button to launch the target activity.
            // While you use resourceId here to find the button, you can also
            // use accessibility info or button text content.
            UiObject2 launchRecyclerActivity = scope.getDevice().findObject(
                By.res(packageName, "launchRecyclerActivity")
            )
            launchRecyclerActivity.click();

            // Wait until activity is shown.
            scope.getDevice().wait(
                Until.hasObject(By.clazz("$packageName.NonExportedRecyclerActivity")),
                10000L
            )

            return Unit.INSTANCE;
        },
        /* measureBlock */ scope -> {
            // ...
        }
    );
}
```

## Recommended for you

* Note: link text is displayed when JavaScript is off
* [Writing a Macrobenchmark](/topic/performance/benchmarking/macrobenchmark-overview)
* [Capture Macrobenchmark metrics](/topic/performance/benchmarking/macrobenchmark-metrics)
* [Microbenchmark](/topic/performance/benchmarking/microbenchmark-overview)

[Previous

arrow\_back

Capture the metrics](/topic/performance/benchmarking/macrobenchmark-metrics)

[Next

Adding instrumentation arguments

arrow\_forward](/topic/performance/benchmarking/macrobenchmark-instrumentation-args)