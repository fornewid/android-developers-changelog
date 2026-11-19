---
title: https://developer.android.com/develop/ui/compose/components/progress
url: https://developer.android.com/develop/ui/compose/components/progress
source: md.txt
---

> Documentation index: https://developer.android.com/develop/ui/compose/components/llms.txt

[Progress indicators](https://m3.material.io/components/progress-indicators/guidelines#f4cc8d62-23b8-47e5-8ffa-5684ef4f1975) visually surface the status of an operation.
They use motion
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

## API surface

Although there are several composables you can use to create progress indicators
consistent with Material Design, their parameters don't differ greatly. Among
the key parameters you should keep in mind are the following:

- `progress`: The current progress that the indicator displays. Pass a `Float` between `0.0` and `1.0`.
- `color`: The color of the actual indicator. That is, the part of the component that reflects progress and which fully encompasses the component when progress is complete.
- `trackColor`: The color of the track over which the indicator is drawn.

> [!NOTE]
> **Note:** The APIs for `LinearProgressIndicator` and `CircularProgressIndicator` are essentially the same and the way you use either one is identical. You can use the following snippets for either.

## M3 Expressive update

Material 3 Expressive introduces `LinearWavyProgressIndicator` and
`CircularWavyProgressIndicator` as additional options alongside the standard
flat `LinearProgressIndicator` and `CircularProgressIndicator`. These indicators
feature a rounded style and configurations for track height and wave shape.
Choose the visual style that best fits your product.

For more information about the M3 Expressive updates for progress indicators,
see the [Material Design 3 progress indicator guidelines](https://m3.material.io/components/progress-indicators/guidelines#f4cc8d62-23b8-47e5-8ffa-5684ef4f1975).
**Figure 2.** Material 3 Expressive progress indicator wavy shapes and variable track heights.

Progress indicators have a rounded, colorful style and additional configurations
to choose from, including a wavy shape and variable track height. The active
indicator has two shape options: **wavy** and **flat**.

### Wavy

Wavy progress indicators offer both determinate and indeterminate variants, and
let you customize their appearance with wave parameters for more expressive
visuals.
**Figure 3.** Wavy progress indicators with expressive wave parameters.

Wavy linear indicators increase the height of the overall container.

> [!NOTE]
> **Note:** The wavy shape can make longer processes feel less static and is best used when a more expressive style is appropriate. When using the wavy shape, the overall height of the component changes. At very small sizes, the wavy shape might not be as visible.

There are two variants of wavy progress indicators: **linear** and **circular**.

#### Determinate linear wavy progress indicator

By default, when using a wavy progress indicator, a wave speed is applied to
create a constant wave motion, even in determinate mode. You can turn this wave
motion off by passing `0.dp` to `waveSpeed`.

The following snippet demonstrates how to implement a determinate
`LinearWavyProgressIndicator` controlled by a `Slider`:


```kotlin
@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun LinearWavyProgressIndicatorSample() {
    val sliderState = rememberSliderState(0.1f)
    val animatedProgress by animateFloatAsState(
            targetValue = sliderState.value,
            animationSpec = ProgressIndicatorDefaults.ProgressAnimationSpec,
        )

    Column(horizontalAlignment = Alignment.CenterHorizontally) {
        LinearWavyProgressIndicator(progress = { animatedProgress })
        Spacer(Modifier.requiredHeight(30.dp))
        Text("Set progress:")
        Slider(
            state = sliderState,
            onValueChange = { sliderState.value = it },
            modifier = Modifier.width(300.dp),
        )
    }
}
```
![A determinate linear wavy progress indicator above the label 'Set progress:' and a horizontal slider.](https://developer.android.com/static/develop/ui/compose/images/components/previews/android_compose_expressive_components_determinatelinearwavyindicator.png)

<br />

#### Indeterminate linear wavy progress indicator

Use indeterminate indicators to show that a process is happening when the wait
time is unknown. The following snippet demonstrates how to implement an
indeterminate `LinearWavyProgressIndicator`:


```kotlin
@Composable
fun IndeterminateLinearWavyProgressIndicatorSample() {
    Column(horizontalAlignment = Alignment.CenterHorizontally) { LinearWavyProgressIndicator() }
}
```
![An indeterminate linear wavy progress indicator showing a wavy active track.](https://developer.android.com/static/develop/ui/compose/images/components/previews/android_compose_expressive_components_indeterminatelinearwavyindicator.png)

<br />

#### Determinate circular wavy progress indicator

The wavy shape can make longer processes feel less static and is best used when
a more expressive style is appropriate. The following snippet demonstrates how
to implement a determinate `CircularWavyProgressIndicator` controlled by a
`Slider`:


```kotlin
@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun CircularWavyProgressIndicatorSample() {
    val sliderState = rememberSliderState(0.1f)
    val animatedProgress by animateFloatAsState(
            targetValue = sliderState.value,
            animationSpec = ProgressIndicatorDefaults.ProgressAnimationSpec,
        )

    Column(horizontalAlignment = Alignment.CenterHorizontally) {
        CircularWavyProgressIndicator(progress = { animatedProgress })
        Spacer(Modifier.requiredHeight(30.dp))
        Text("Set progress:")
        Slider(
            state = sliderState,
            onValueChange = { sliderState.value = it },
            modifier = Modifier.width(300.dp),
        )
    }
}
```
![A determinate circular wavy progress indicator above the label 'Set progress:' and a horizontal slider.](https://developer.android.com/static/develop/ui/compose/images/components/previews/android_compose_expressive_components_determinatecircularwavyindicator.png)

<br />

#### Indeterminate circular wavy progress indicator

Circular progress indicators should be centered directly on the container or
page that's loading, such as a button or card. The following snippet
demonstrates how to implement an indeterminate `CircularWavyProgressIndicator`:


```kotlin
@Composable
fun IndeterminateCircularWavyProgressIndicatorSample() {
    Column(horizontalAlignment = Alignment.CenterHorizontally) { CircularWavyProgressIndicator() }
}
```
![An indeterminate circular wavy progress indicator.](https://developer.android.com/static/develop/ui/compose/images/components/previews/android_compose_expressive_components_indeterminatecircularwavyindicator.png)

<br />

### Flat

#### Determinate indicators

A determinate indicator reflects exactly how complete an action is. Use either
the [`LinearProgressIndicator`](https://developer.android.com/reference/kotlin/androidx/compose/material3/LinearProgressIndicator.composable.md.txt#LinearProgressIndicator(kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.StrokeCap,androidx.compose.ui.unit.Dp,kotlin.Function1)) or [`CircularProgressIndicator`](https://developer.android.com/reference/kotlin/androidx/compose/material3/CircularProgressIndicator.composable.md.txt#CircularProgressIndicator(kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.Dp,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.StrokeCap,androidx.compose.ui.unit.Dp))
composables and pass a value for the `progress` parameter.

The following snippet demonstrates how to implement a determinate
`LinearProgressIndicator` controlled by a `Slider`:


```kotlin
@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun LinearProgressIndicatorSample() {
    val sliderState = rememberSliderState(0.1f)
    val animatedProgress by animateFloatAsState(
            targetValue = sliderState.value,
            animationSpec = ProgressIndicatorDefaults.ProgressAnimationSpec,
        )

    Column(horizontalAlignment = Alignment.CenterHorizontally) {
        LinearProgressIndicator(progress = { animatedProgress })
        Spacer(Modifier.requiredHeight(30.dp))
        Text("Set progress:")
        Slider(
            state = sliderState,
            onValueChange = { sliderState.value = it },
            modifier = Modifier.width(300.dp),
        )
    }
}
```
![A determinate linear progress indicator above the label 'Set progress:' and a horizontal slider.](https://developer.android.com/static/develop/ui/compose/images/components/previews/android_compose_expressive_components_determinatelinearindicator.png)

<br />

The following snippet demonstrates how to implement a determinate
`CircularProgressIndicator` controlled by a `Slider`:


```kotlin
@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun CircularProgressIndicatorSample() {
    val sliderState = rememberSliderState(0.1f)
    val animatedProgress by animateFloatAsState(
            targetValue = sliderState.value,
            animationSpec = ProgressIndicatorDefaults.ProgressAnimationSpec,
        )

    Column(horizontalAlignment = Alignment.CenterHorizontally) {
        CircularProgressIndicator(progress = { animatedProgress })
        Spacer(Modifier.requiredHeight(30.dp))
        Text("Set progress:")
        Slider(
            state = sliderState,
            onValueChange = { sliderState.value = it },
            modifier = Modifier.width(300.dp),
        )
    }
}
```
![A determinate circular progress indicator above the label 'Set progress:' and a horizontal slider.](https://developer.android.com/static/develop/ui/compose/images/components/previews/android_compose_expressive_components_determinatecircularindicator.png)

<br />

The following snippet provides a relatively detailed example. When the user
presses the button, the app replaces it with the progress indicator and launches
a coroutine that gradually increases the value of `progress`. This causes the
progress indicator to iterate up in turn.

> [!NOTE]
> **Note:** The following example uses a coroutine to do the work of iterating the `progress` value because it would otherwise block the UI thread.


```kotlin
@Composable
fun LinearDeterminateIndicator() {
    var currentProgress by remember { mutableFloatStateOf(0f) }
    var loading by remember { mutableStateOf(false) }
    val scope = rememberCoroutineScope() // Create a coroutine scope
    // Animate between progress updates so the indicator fills smoothly.
    val animatedProgress by animateFloatAsState(
        targetValue = currentProgress,
        animationSpec = ProgressIndicatorDefaults.ProgressAnimationSpec,
    )

    if (loading) {
        LinearProgressIndicator(
            progress = { animatedProgress },
            modifier = Modifier.fillMaxWidth(),
        )
    } else {
        Button(onClick = {
            loading = true
            scope.launch {
                loadProgress { progress ->
                    currentProgress = progress
                }
                loading = false // Reset loading when the coroutine finishes
            }
        }) {
            Text("Start loading")
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
![A linear progress indicator about half filled, shown in place of the 'Start loading' button after it's pressed.](https://developer.android.com/static/develop/ui/compose/images/components/previews/android_compose_components_determinateindicator.png)

<br />

When loading is partially complete, the linear indicator in the preceding
example appears as follows:
**Figure 4.** A linear determinate progress indicator.

Likewise, the circular indicator appears as follows:
**Figure 5.** A circular determinate progress indicator.

#### Indeterminate indicators

An indeterminate indicator does not reflect how close to completion an operation
is. Rather, it uses motion to indicate to the user that processing is ongoing,
though without specifying any degree of completion.

To create an indeterminate progress indicator, use the `LinearProgressIndicator`
or `CircularProgressIndicator` composable, but don't pass in a value for
`progress`. The following snippet demonstrates how to implement an indeterminate
`LinearProgressIndicator`:


```kotlin
@Composable
fun IndeterminateLinearProgressIndicatorSample() {
    Column(horizontalAlignment = Alignment.CenterHorizontally) { LinearProgressIndicator() }
}
```
![An indeterminate linear progress indicator showing animated track segments.](https://developer.android.com/static/develop/ui/compose/images/components/previews/android_compose_expressive_components_indeterminatelinearindicator.png)

<br />

The following snippet demonstrates how to implement an indeterminate
`CircularProgressIndicator`:


```kotlin
@Composable
fun IndeterminateCircularProgressIndicatorSample() {
    Column(horizontalAlignment = Alignment.CenterHorizontally) { CircularProgressIndicator() }
}
```
![An indeterminate circular progress indicator.](https://developer.android.com/static/develop/ui/compose/images/components/previews/android_compose_expressive_components_indeterminatecircularindicator.png)

<br />

The following example demonstrates how you can toggle an indeterminate indicator
with a button press. This example also demonstrates how you can pass values for
the `color` and `trackColor` parameters to customize the appearance of the
indicator:


```kotlin
@Composable
fun IndeterminateCircularIndicator() {
    var loading by remember { mutableStateOf(false) }

    if (loading) {
        CircularProgressIndicator(
            modifier = Modifier.size(64.dp),
            color = MaterialTheme.colorScheme.secondary,
            trackColor = MaterialTheme.colorScheme.surfaceVariant,
        )
    } else {
        Button(onClick = { loading = true }) {
            Text("Start loading")
        }
    }
}
```
![A circular progress indicator, shown in place of the 'Start loading' button after it's pressed.](https://developer.android.com/static/develop/ui/compose/images/components/previews/android_compose_components_indeterminateindicator.png)

<br />

The following is an example of this implementation when the indicator is active:
**Figure 6.** A circular indeterminate progress indicator.

The following is an example of the same implementation, but with
`LinearProgressIndicator` instead of `CircularProgressIndicator`:
**Figure 7.** A linear indeterminate progress indicator.

## Additional resources

- [Material UI docs](https://m3.material.io/components/progress-indicators/overview)