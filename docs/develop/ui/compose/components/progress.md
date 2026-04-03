---
title: Progress indicators  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/components/progress
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Progress indicators Stay organized with collections Save and categorize content based on your preferences.




Progress indicators visually surface the status of an operation. They use motion
to bring to the user's attention how near completion the process is, such as
loading or processing data. They can also signify that processing is taking
place, without reference to how close to completion it might be.

Consider these three use cases where you might use a progress indicator:

* **Loading content**: While fetching content from a network, such as loading
  an image or data for a user profile.
* **File upload**: Give the user feedback on how long the upload might take.
* **Long processing**: While an app is processing a large amount of data,
  convey to the user how much of the total is complete.

In Material Design, there are two types of progress indicator:

* **Determinate**: Displays exactly how much progress has been made.
* **Indeterminate**: Animates continually without regard to progress.

Likewise, a progress indicator can take one of the two following forms:

* **Linear**: A horizontal bar that fills from left to right.
* **Circular**: A circle whose stroke grows in length until it encompasses the
  full circumference of the circle.

![A linear progress indicator alongside a circular progress indicator.](/static/develop/ui/compose/images/components/progress-indicators.svg)


**Figure 1.** The two types of progress indicators.

## API Surface

Although there are several composables you can use to create progress indicators
consistent with Material Design, their parameters don't differ greatly. Among
the key parameters you should keep in mind are the following:

* `progress`: The current progress that the indicator displays. Pass a `Float`
  between `0.0` and `1.0`.
* `color`: The color of the actual indicator. That is, the part of the
  component that reflects progress and which fully encompasses the component
  when progress is complete.
* `trackColor`: The color of the track over which the indicator is drawn.

**Note:** The APIs for `LinearProgressIndicator` and `CircularProgressIndicator` are
essentially the same and the way you use either one is identical. You can use
the following snippets for either.

## Determinate indicators

A determinate indicator reflects exactly how complete an action is. Use either
the [`LinearProgressIndicator`](/reference/kotlin/androidx/compose/material3/LinearProgressIndicator.composable#LinearProgressIndicator(kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.StrokeCap,androidx.compose.ui.unit.Dp,kotlin.Function1)) or [`CircularProgressIndicator`](/reference/kotlin/androidx/compose/material3/CircularProgressIndicator.composable#CircularProgressIndicator(kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.Dp,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.StrokeCap,androidx.compose.ui.unit.Dp))
composables and pass a value for the `progress` parameter.

The following snippet provides a relatively detailed example. When the user
presses the button, the app both displays the progress indicator, and launches a
coroutine that gradually increases the value of `progress`. This causes the
progress indicator to iterate up in turn.

**Note:** The following example uses a coroutine to do the work of iterating the
`progress` value because it would otherwise block the UI thread.

```
@Composable
fun LinearDeterminateIndicator() {
    var currentProgress by remember { mutableFloatStateOf(0f) }
    var loading by remember { mutableStateOf(false) }
    val scope = rememberCoroutineScope() // Create a coroutine scope

    Column(
        verticalArrangement = Arrangement.spacedBy(12.dp),
        horizontalAlignment = Alignment.CenterHorizontally,
        modifier = Modifier.fillMaxWidth()
    ) {
        Button(onClick = {
            loading = true
            scope.launch {
                loadProgress { progress ->
                    currentProgress = progress
                }
                loading = false // Reset loading when the coroutine finishes
            }
        }, enabled = !loading) {
            Text("Start loading")
        }

        if (loading) {
            LinearProgressIndicator(
                progress = { currentProgress },
                modifier = Modifier.fillMaxWidth(),
            )
        }
    }
}

/** Iterate the progress value */
suspend fun loadProgress(updateProgress: (Float) -> Unit) {
    for (i in 1..100) {
        updateProgress(i.toFloat() / 100)
        delay(100)
    }
}

ProgressIndicator.kt
```

When loading is partially complete, the linear indicator in the preceding
example appears as follows:

[

](/static/develop/ui/compose/images/components/linear-indicator-determinate.mp4)

Likewise, the circular indicator appears as follows:

[

](/static/develop/ui/compose/images/components/circular-indicator-determinate.mp4)

## Indeterminate indicators

An indeterminate indicator does not reflect how close to completion an operation
is. Rather, it uses motion to indicate to the user that processing is ongoing,
though without specifying any degree of completion.

To create an indeterminate progress indicator, use the `LinearProgressIndicator`
or `CircularProgressIndicator` composable, but don't pass in a value for
`progress`. The following example demonstrates how you can toggle an
indeterminate indicator with a button press.

**Note:** This example also demonstrates how you can pass values for the `color` and
`trackColor` parameters to customize the appearance of the indicator.

```
@Composable
fun IndeterminateCircularIndicator() {
    var loading by remember { mutableStateOf(false) }

    Button(onClick = { loading = true }, enabled = !loading) {
        Text("Start loading")
    }

    if (!loading) return

    CircularProgressIndicator(
        modifier = Modifier.width(64.dp),
        color = MaterialTheme.colorScheme.secondary,
        trackColor = MaterialTheme.colorScheme.surfaceVariant,
    )
}

ProgressIndicator.kt
```

The following is an example of this implementation when the indicator is active:

[

](/static/develop/ui/compose/images/components/circular-indicator.mp4)

The following is an example of the same implementation but with
`LinearProgressIndicator` instead of `CircularProgressIndicator`.

[

](/static/develop/ui/compose/images/components/linear-indicator.mp4)

## Additional resources

* [Material UI docs](https://m3.material.io/components/progress-indicators/overview)