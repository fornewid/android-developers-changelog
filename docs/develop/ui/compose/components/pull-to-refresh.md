---
title: Pull to refresh  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/components/pull-to-refresh
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Pull to refresh Stay organized with collections Save and categorize content based on your preferences.




The pull to refresh component allows users to drag downwards at the beginning of
an app's content to refresh the data.

**Note:** [`PullToRefreshBox()`](/reference/kotlin/androidx/compose/material3/pulltorefresh/PullToRefreshBox.composable) is experimental.

## API surface

Use the [`PullToRefreshBox`](/reference/kotlin/androidx/compose/material3/pulltorefresh/PullToRefreshBox.composable) composable to implement pull-to-refresh, which
acts as a container for your scrollable content. The following key parameters
control the refresh behavior and appearance:

* `isRefreshing`: A boolean value indicating whether the refresh action is
  in progress.
* `onRefresh`: A lambda function that executes when the user initiates a
  refresh.
* `indicator`: Customizes the indicator that the system draws on pull-to-refresh.

## Basic example

This snippet demonstrates basic usage of `PullToRefreshBox`:

```
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

PullToRefreshBox.kt
```

### Key points about the code

* `PullToRefreshBox` wraps a [`LazyColumn`](/reference/kotlin/androidx/compose/foundation/lazy/LazyColumn.composable#LazyColumn(androidx.compose.ui.Modifier,androidx.compose.foundation.lazy.LazyListState,androidx.compose.foundation.layout.PaddingValues,kotlin.Boolean,androidx.compose.foundation.layout.Arrangement.Vertical,androidx.compose.ui.Alignment.Horizontal,androidx.compose.foundation.gestures.FlingBehavior,kotlin.Boolean,androidx.compose.foundation.OverscrollEffect,kotlin.Function1)), which displays a list of
  strings.
* `PullToRefreshBox` requires `isRefreshing` and `onRefresh` parameters.
* The content within the `PullToRefreshBox` block represents the scrollable
  content.

### Result

This video demonstrates the basic pull-to-refresh implementation from
the preceding code:

[

](/static/develop/ui/compose/images/components/PullToRefreshBasicSample (1).mp4)


**Figure 1**. A basic pull-to-refresh implementation on a list of items.

## Advanced example: Customize indicator color

```
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

PullToRefreshBox.kt
```

### Key points about the code

* The indicator color is customized through the `containerColor` and `color`
  properties in the `indicator` parameter.
* [`rememberPullToRefreshState()`](/reference/kotlin/androidx/compose/material3/pulltorefresh/PullToRefreshState) manages the state of the refresh action.
  You use this state in conjunction with the `indicator` parameter.

**Note:** In the basic example, `state` was not passed to `PullToRefreshBox` because
it was using the default parameter value. However, in this example, you need to
define the state, and pass that state to both the box and indicator to
coordinate their behavior.

### Result

This video shows a pull-to-refresh implementation with a colored
indicator:

[

](/static/develop/ui/compose/images/components/PullToRefreshCustomStyleSample (1).mp4)


**Figure 2**. A pull-to-refresh implementation with a custom style.

## Advanced example: Create a fully customized indicator

You can create complex custom indicators by leveraging existing composables and
animations.This snippet demonstrates how to create a fully custom indicator in
your pull-to-refresh implementation:

```
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
}PullToRef
```

reshBox.kt

### Key points about the code

* The previous snippet used the `Indicator` provided by the library. This
  snippet creates a custom indicator composable called `MyCustomIndicator`. In
  this composable, the `pullToRefreshIndicator` modifier handles positioning and
  triggering a refresh.
* As in the previous snippet, the example extracts the `PullToRefreshState`
  instance, so you can pass the same instance to both the `PullToRefreshBox`
  and the `pullToRefreshModifier`.
* The example uses the container color and the position threshold from the
  `PullToRefreshDefaults` class. This way, you can reuse the default behavior
  and styling from the Material library, while customizing only the elements
  you're interested in.
* `MyCustomIndicator` uses [`Crossfade`](/reference/kotlin/androidx/compose/animation/Crossfade.composable#Crossfade(kotlin.Any,androidx.compose.ui.Modifier,androidx.compose.animation.core.FiniteAnimationSpec,kotlin.String,kotlin.Function1)) to transition between a cloud icon
  and a `CircularProgressIndicator`. The cloud icon scales up as the user pulls,
  and transitions to a `CircularProgressIndicator` when the refresh action
  begins.
  + `targetState` uses `isRefreshing` to determine which state to display (the
    cloud icon or the circular progress indicator).
  + `animationSpec` defines a `tween` animation for the transition, with a
    specified duration of `CROSSFADE_DURATION_MILLIS`.
  + `state.distanceFraction` represents how far the user has pulled down,
    ranging from `0f` (no pull) to `1f` (fully pulled).
  + The `graphicsLayer` modifier modifies scale and transparency.

### Result

This video shows the custom indicator from the preceding code:

[

](/static/develop/ui/compose/images/components/PullToRefreshCustomStyleSample (1).mp4)


**Figure 3**. A pull-to-refresh implementation with a custom indicator.

## Additional resources

* [`PullToRefreshState`](/reference/kotlin/androidx/compose/material3/pulltorefresh/PullToRefreshState)