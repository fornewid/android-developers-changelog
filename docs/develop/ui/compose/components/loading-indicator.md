---
title: https://developer.android.com/develop/ui/compose/components/loading-indicator
url: https://developer.android.com/develop/ui/compose/components/loading-indicator
source: md.txt
---

> Documentation index: https://developer.android.com/develop/ui/compose/components/llms.txt

[Loading indicators](https://developer.android.com/reference/kotlin/androidx/compose/material3/LoadingIndicator.composable.md.txt) show progress for a short wait time---typically operations
that complete in under five seconds. There are two configurations of loading
indicators:

1. **Default**: Uncontained morphing shapes.
2. **Contained**: Morphing shapes within a circular container.

![Default and contained configurations of loading indicators](https://developer.android.com/static/develop/ui/compose/images/components/loading_indicator_types.png) **Figure 1.** Default and contained loading indicators.

The indicator continuously morphs between its polygon shapes, either
indefinitely or in response to a progress value.

## Using loading indicators

- Recommended as a replacement for most indeterminate circular progress indicators.
- Always reflect an ongoing process and are never purely decorative.
- Use them when progress isn't measurable, or when it isn't necessary to indicate how long an activity takes.
- Can be used for pull-to-refresh interactions.
- Capture attention through shape-morphing motion.

## Examples

> [!NOTE]
> **Note:** The following examples use experimental APIs marked as `@ExperimentalMaterial3ExpressiveApi`. These APIs are still under development and may change before becoming stable.

### Implement a loading indicator

Loading indicators use animation to grab attention, mitigate perceived latency,
and indicate that an activity is in progress. The following snippet renders a
default indeterminate [`LoadingIndicator`](https://developer.android.com/reference/kotlin/androidx/compose/material3/LoadingIndicator.composable.md.txt):


```kotlin
@Composable
fun LoadingIndicatorSample() {
    Column(horizontalAlignment = Alignment.CenterHorizontally) { LoadingIndicator() }
}
```
![A default uncontained loading indicator showing a dark polygon shape.](https://developer.android.com/static/develop/ui/compose/images/components/previews/android_compose_expressive_components_loadingindicator.png)

<br />

### Implement a contained loading indicator

Use [`ContainedLoadingIndicator`](https://developer.android.com/reference/kotlin/androidx/compose/material3/ContainedLoadingIndicator.composable.md.txt) to render morphing shapes inside a circular
container that provides extra contrast over body content. The following snippet
implements a contained loading indicator:


```kotlin
@Composable
fun ContainedLoadingIndicatorSample() {
    Column(horizontalAlignment = Alignment.CenterHorizontally) { ContainedLoadingIndicator() }
}
```
![A contained loading indicator showing a dark polygon shape inside a light gray circular container.](https://developer.android.com/static/develop/ui/compose/images/components/previews/android_compose_expressive_components_containedloadingindicator.png)

<br />

### Implement a determinate loading indicator

Pass a `progress` lambda returning a `Float` from `0.0` to `1.0` to morph
[`LoadingIndicator`](https://developer.android.com/reference/kotlin/androidx/compose/material3/LoadingIndicator.composable.md.txt) determinately as an operation progresses. The following
snippet drives the loading indicator's progress with a [`Slider`](https://developer.android.com/reference/kotlin/androidx/compose/material3/Slider.composable.md.txt) and
`rememberSliderState`:


```kotlin
@Composable
fun DeterminateLoadingIndicatorSample() {
    val sliderState = rememberSliderState()
    val animatedProgress by
        animateFloatAsState(
            targetValue = sliderState.value,
            animationSpec =
                spring(
                    dampingRatio = Spring.DampingRatioNoBouncy,
                    stiffness = Spring.StiffnessVeryLow,
                    visibilityThreshold = 1 / 1000f,
                ),
        )

    Column(horizontalAlignment = Alignment.CenterHorizontally) {
        LoadingIndicator(progress = { animatedProgress })
        Spacer(Modifier.requiredHeight(30.dp))
        Text("Set loading progress:")
        Slider(
            state = sliderState,
            onValueChange = { sliderState.value = it },
            modifier = Modifier.width(300.dp),
        )
    }
}
```
![A determinate loading indicator shape above the label 'Set loading progress:' and a horizontal slider.](https://developer.android.com/static/develop/ui/compose/images/components/previews/android_compose_expressive_components_determinateloadingindicator.png)

<br />