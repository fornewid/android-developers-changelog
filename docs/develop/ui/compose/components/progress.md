---
title: https://developer.android.com/develop/ui/compose/components/progress
url: https://developer.android.com/develop/ui/compose/components/progress
source: md.txt
---

Progress indicators visually surface the status of an operation. They use motion
to bring to the user's attention how near completion the process is, such as
loading or processing data. They can also signify that processing is taking
place, without reference to how close to completion it might be.

Consider these three use cases where you might use a progress indicator:

- **Loading content**: While fetching content from a network, such as loading an image or data for a user profile.
- **File upload**: Give the user feedback on how long the upload might take.
- **Long processing**: While an app is processing a large amount of data, convey to the user how much of the total is complete.

In Material Design, there are two types of progress indicator:

- **Determinate**: Displays exactly how much progress has been made.
- **Indeterminate**: Animates continually without regard to progress.

Likewise, a progress indicator can take one of the two following forms:

- **Linear**: A horizontal bar that fills from left to right.
- **Circular**: A circle whose stroke grows in length until it encompasses the full circumference of the circle.

![A linear progress indicator alongside a circular progress indicator.](https://developer.android.com/static/develop/ui/compose/images/components/progress-indicators.svg) **Figure 1.** The two types of progress indicators.

## API Surface

Although there are several composables you can use to create progress indicators
consistent with Material Design, their parameters don't differ greatly. Among
the key parameters you should keep in mind are the following:

- `progress`: The current progress that the indicator displays. Pass a `Float` between `0.0` and `1.0`.
- `color`: The color of the actual indicator. That is, the part of the component that reflects progress and which fully encompasses the component when progress is complete.
- `trackColor`: The color of the track over which the indicator is drawn.

> [!NOTE]
> **Note:** The APIs for `LinearProgressIndicator` and `CircularProgressIndicator` are essentially the same and the way you use either one is identical. You can use the following snippets for either.

## Determinate indicators

A determinate indicator reflects exactly how complete an action is. Use either
the [`LinearProgressIndicator`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#LinearProgressIndicator(kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.StrokeCap,androidx.compose.ui.unit.Dp,kotlin.Function1)) or [`CircularProgressIndicator`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#CircularProgressIndicator(kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.Dp,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.StrokeCap,androidx.compose.ui.unit.Dp))
composables and pass a value for the `progress` parameter.

The following snippet provides a relatively detailed example. When the user
presses the button, the app both displays the progress indicator, and launches a
coroutine that gradually increases the value of `progress`. This causes the
progress indicator to iterate up in turn.

> [!NOTE]
> **Note:** The following example uses a coroutine to do the work of iterating the `progress` value because it would otherwise block the UI thread.


```kotlin
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
```

<br />

When loading is partially complete, the linear indicator in the preceding
example appears as follows:

Likewise, the circular indicator appears as follows:

## Indeterminate indicators

An indeterminate indicator does not reflect how close to completion an operation
is. Rather, it uses motion to indicate to the user that processing is ongoing,
though without specifying any degree of completion.

To create an indeterminate progress indicator, use the `LinearProgressIndicator`
or `CircularProgressIndicator` composable, but don't pass in a value for
`progress`. The following example demonstrates how you can toggle an
indeterminate indicator with a button press.

> [!NOTE]
> **Note:** This example also demonstrates how you can pass values for the `color` and `trackColor` parameters to customize the appearance of the indicator.


```kotlin
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
```

<br />

The following is an example of this implementation when the indicator is active:

The following is an example of the same implementation but with
`LinearProgressIndicator` instead of `CircularProgressIndicator`.

## Additional resources

- [Material UI docs](https://m3.material.io/components/progress-indicators/overview)