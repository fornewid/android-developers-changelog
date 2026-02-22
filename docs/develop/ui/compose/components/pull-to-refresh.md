---
title: https://developer.android.com/develop/ui/compose/components/pull-to-refresh
url: https://developer.android.com/develop/ui/compose/components/pull-to-refresh
source: md.txt
---

The pull to refresh component allows users to drag downwards at the beginning of
an app's content to refresh the data.

> [!NOTE]
> **Note:** [`PullToRefreshBox()`](https://developer.android.com/reference/kotlin/androidx/compose/material3/pulltorefresh/package-summary#PullToRefreshBox(kotlin.Boolean,kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.material3.pulltorefresh.PullToRefreshState,androidx.compose.ui.Alignment,kotlin.Function1,kotlin.Function1)) is experimental.

## API surface

Use the [`PullToRefreshBox`](https://developer.android.com/reference/kotlin/androidx/compose/material3/pulltorefresh/package-summary#PullToRefreshBox(kotlin.Boolean,kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.material3.pulltorefresh.PullToRefreshState,androidx.compose.ui.Alignment,kotlin.Function1,kotlin.Function1)) composable to implement pull-to-refresh, which
acts as a container for your scrollable content. The following key parameters
control the refresh behavior and appearance:

- `isRefreshing`: A boolean value indicating whether the refresh action is in progress.
- `onRefresh`: A lambda function that executes when the user initiates a refresh.
- `indicator`: Customizes the indicator that the system draws on pull-to-refresh.

## Basic example

This snippet demonstrates basic usage of `PullToRefreshBox`:


```kotlin
@Composable
fun PullToRefreshBasicSample(
    items: List<String>,
    isRefreshing: Boolean,
    onRefresh: () -> Unit,
    modifier: Modifier = Modifier
) {
    PullToRefreshBox(
        isRefreshing = isRefreshing,
        onRefresh = onRefresh,
        modifier = modifier
    ) {
        LazyColumn(Modifier.fillMaxSize()) {
            items(items) {
                ListItem({ Text(text = it) })
            }
        }
    }
}
```

<br />

### Key points about the code

- `PullToRefreshBox` wraps a [`LazyColumn`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/lazy/package-summary#LazyColumn(androidx.compose.ui.Modifier,androidx.compose.foundation.lazy.LazyListState,androidx.compose.foundation.layout.PaddingValues,kotlin.Boolean,androidx.compose.foundation.layout.Arrangement.Vertical,androidx.compose.ui.Alignment.Horizontal,androidx.compose.foundation.gestures.FlingBehavior,kotlin.Boolean,androidx.compose.foundation.OverscrollEffect,kotlin.Function1)), which displays a list of strings.
- `PullToRefreshBox` requires `isRefreshing` and `onRefresh` parameters.
- The content within the `PullToRefreshBox` block represents the scrollable content.

### Result

This video demonstrates the basic pull-to-refresh implementation from
the preceding code:
**Figure 1**. A basic pull-to-refresh implementation on a list of items.

## Advanced example: Customize indicator color


```kotlin
@Composable
fun PullToRefreshCustomStyleSample(
    items: List<String>,
    isRefreshing: Boolean,
    onRefresh: () -> Unit,
    modifier: Modifier = Modifier
) {
    val state = rememberPullToRefreshState()

    PullToRefreshBox(
        isRefreshing = isRefreshing,
        onRefresh = onRefresh,
        modifier = modifier,
        state = state,
        indicator = {
            Indicator(
                modifier = Modifier.align(Alignment.TopCenter),
                isRefreshing = isRefreshing,
                containerColor = MaterialTheme.colorScheme.primaryContainer,
                color = MaterialTheme.colorScheme.onPrimaryContainer,
                state = state
            )
        },
    ) {
        LazyColumn(Modifier.fillMaxSize()) {
            items(items) {
                ListItem({ Text(text = it) })
            }
        }
    }
}
```

<br />

### Key points about the code

- The indicator color is customized through the `containerColor` and `color` properties in the `indicator` parameter.
- [`rememberPullToRefreshState()`](https://developer.android.com/reference/kotlin/androidx/compose/material3/pulltorefresh/PullToRefreshState) manages the state of the refresh action. You use this state in conjunction with the `indicator` parameter.

> [!NOTE]
> **Note:** In the basic example, `state` was not passed to `PullToRefreshBox` because it was using the default parameter value. However, in this example, you need to define the state, and pass that state to both the box and indicator to coordinate their behavior.

### Result

This video shows a pull-to-refresh implementation with a colored
indicator:
**Figure 2**. A pull-to-refresh implementation with a custom style.

## Advanced example: Create a fully customized indicator

You can create complex custom indicators by leveraging existing composables and
animations.This snippet demonstrates how to create a fully custom indicator in
your pull-to-refresh implementation:


```kotlin
@Composable
fun PullToRefreshCustomIndicatorSample(
    items: List<String>,
    isRefreshing: Boolean,
    onRefresh: () -> Unit,
    modifier: Modifier = Modifier
) {
    val state = rememberPullToRefreshState()

    PullToRefreshBox(
        isRefreshing = isRefreshing,
        onRefresh = onRefresh,
        modifier = modifier,
        state = state,
        indicator = {
            MyCustomIndicator(
                state = state,
                isRefreshing = isRefreshing,
                modifier = Modifier.align(Alignment.TopCenter)
            )
        }
    ) {
        LazyColumn(Modifier.fillMaxSize()) {
            items(items) {
                ListItem({ Text(text = it) })
            }
        }
    }
}

// ...
@Composable
fun MyCustomIndicator(
    state: PullToRefreshState,
    isRefreshing: Boolean,
    modifier: Modifier = Modifier,
) {
    Box(
        modifier = modifier.pullToRefresh(
            state = state,
            isRefreshing = isRefreshing,
            threshold = PositionalThreshold,
            onRefresh = {

            }
        ),
        contentAlignment = Alignment.Center
    ) {
        Crossfade(
            targetState = isRefreshing,
            animationSpec = tween(durationMillis = CROSSFADE_DURATION_MILLIS),
            modifier = Modifier.align(Alignment.Center)
        ) { refreshing ->
            if (refreshing) {
                CircularProgressIndicator(Modifier.size(SPINNER_SIZE))
            } else {
                val distanceFraction = { state.distanceFraction.coerceIn(0f, 1f) }
                Icon(
                    imageVector = Icons.Filled.CloudDownload,
                    contentDescription = "Refresh",
                    modifier = Modifier
                        .size(18.dp)
                        .graphicsLayer {
                            val progress = distanceFraction()
                            this.alpha = progress
                            this.scaleX = progress
                            this.scaleY = progress
                        }
                )
            }
        }
    }
}
```

<br />

### Key points about the code

- The previous snippet used the `Indicator` provided by the library. This snippet creates a custom indicator composable called `MyCustomIndicator`. In this composable, the `pullToRefreshIndicator` modifier handles positioning and triggering a refresh.
- As in the previous snippet, the example extracts the `PullToRefreshState` instance, so you can pass the same instance to both the `PullToRefreshBox` and the `pullToRefreshModifier`.
- The example uses the container color and the position threshold from the `PullToRefreshDefaults` class. This way, you can reuse the default behavior and styling from the Material library, while customizing only the elements you're interested in.
- `MyCustomIndicator` uses [`Crossfade`](https://developer.android.com/reference/kotlin/androidx/compose/animation/package-summary#Crossfade(kotlin.Any,androidx.compose.ui.Modifier,androidx.compose.animation.core.FiniteAnimationSpec,kotlin.String,kotlin.Function1)) to transition between a cloud icon and a `CircularProgressIndicator`. The cloud icon scales up as the user pulls, and transitions to a `CircularProgressIndicator` when the refresh action begins.
  - `targetState` uses `isRefreshing` to determine which state to display (the cloud icon or the circular progress indicator).
  - `animationSpec` defines a `tween` animation for the transition, with a specified duration of `CROSSFADE_DURATION_MILLIS`.
  - `state.distanceFraction` represents how far the user has pulled down, ranging from `0f` (no pull) to `1f` (fully pulled).
  - The `graphicsLayer` modifier modifies scale and transparency.

### Result

This video shows the custom indicator from the preceding code:
**Figure 3**. A pull-to-refresh implementation with a custom indicator.

## Additional resources

- [`PullToRefreshState`](https://developer.android.com/reference/kotlin/androidx/compose/material3/pulltorefresh/PullToRefreshState)