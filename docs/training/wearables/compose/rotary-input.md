---
title: Rotary input with Compose  |  Wear OS  |  Android Developers
url: https://developer.android.com/training/wearables/compose/rotary-input
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Wear OS](https://developer.android.com/training/wearables)

# Rotary input with Compose Stay organized with collections Save and categorize content based on your preferences.




Compose for Wear OS Material version

2.5
3


---

Rotary input refers to input from pieces of your watch that spin or rotate. On
average, users spend only a few seconds interacting with their watch. You
can enhance your user experience by using Rotary input to allow your user to
quickly accomplish various tasks.

The three main sources of rotary input on most watches include the rotating side
button (RSB), and either a physical bezel or a touch bezel, which is a circular
touch zone around the screen. Though expected behavior may vary based on the
type of input, be sure to support rotary input for all essential interactions.

## Scroll indicator

Most users expect apps to support the scroll gesture. As the content scrolls on
the screen, give the users visual feedback in response to rotary interactions.
Visual feedback can include [scrolling indicators](/reference/kotlin/androidx/wear/compose/material3/ScrollIndicator.composable#ScrollIndicator(androidx.compose.foundation.lazy.LazyListState,androidx.compose.ui.Modifier,androidx.wear.compose.material3.ScrollIndicatorColors,kotlin.Boolean,androidx.compose.animation.core.AnimationSpec)) for vertical scroll or
[page indicators](/reference/kotlin/androidx/wear/compose/material3/HorizontalPageIndicator.composable#HorizontalPageIndicator(androidx.wear.compose.foundation.pager.PagerState,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color)).

`ScalingLazyColumn`, `TransformingLazyColumn` and `Picker` support the scroll
gesture by default, if you place these components inside `AppScaffold` and `ScreenScaffold` and pass the list state between
`ScreenScaffold` and the component, such as a `TransformingLazyColumn`.

`AppScaffold` and `ScreenScaffold` provides the basic layout structure for Wear
OS apps and already has a slot for a scroll indicator with a default
implementation. To customize the scrolling progress, create a scroll indicator
based on the list state object, as shown in the following code snippet:

```
val listState = rememberTransformingLazyColumnState()
ScreenScaffold(
    scrollState = listState,
    scrollIndicator = {
        ScrollIndicator(state = listState)
    }
) {
    // ...
}

Rotary.kt
```

You can configure a snap behavior for `ScalingLazyColumn` by using
`ScalingLazyColumnDefaults.snapFlingBehavior`, as shown in the following
code snippet:

```
val listState = rememberScalingLazyListState()
ScreenScaffold(
    scrollState = listState,
    scrollIndicator = {
        ScrollIndicator(state = listState)
    }
) {

    val state = rememberScalingLazyListState()
    ScalingLazyColumn(
        modifier = Modifier.fillMaxWidth(),
        state = state,
        flingBehavior = ScalingLazyColumnDefaults.snapFlingBehavior(state = state)
    ) {
        // Content goes here
        // ...
    }
}

Rotary.kt
```

## Custom actions

You can also create custom actions that respond to rotary input in your app. For
example, use rotary input to zoom in and out or to control volume in a media
app.

If your component doesn't natively support scrolling events such as volume
control, you can handle scroll events yourself.

The first step is to create a custom state managed in view model, and a custom
callback that is used to process rotary scroll events.

```
class VolumeRange(
    val max: Int = 10,
    val min: Int = 0
)

private object VolumeViewModel {
    class MyViewModel : ViewModel() {
        private val _volumeState = mutableIntStateOf(0)
        val volumeState: State<Int>
            get() = _volumeState

        // ...
        fun onVolumeChangeByScroll(pixels: Float) {
            _volumeState.value = when {
                pixels > 0 -> minOf(volumeState.value + 1, VolumeRange().max)
                pixels < 0 -> maxOf(volumeState.value - 1, VolumeRange().min)
                else -> volumeState.value
            }
        }
    }
}

Rotary.kt
```

Then, use the callback once you receive the events, as shown in the following
snippet.

```
val focusRequester: FocusRequester = remember { FocusRequester() }
val volumeViewModel: VolumeViewModel.MyViewModel =
    viewModel()
val volumeState by volumeViewModel.volumeState

TransformingLazyColumn(
    modifier = Modifier
        .fillMaxSize()
        .onRotaryScrollEvent {
            volumeViewModel.onVolumeChangeByScroll(it.verticalScrollPixels)
            true
        }
        .focusRequester(focusRequester)
        .focusable(),
) {
    // You can use volumeState here, for example:
    item {
        Text("Volume: $volumeState")
    }
}

Rotary.kt
```

Note that for the sake of simplicity, the preceding example uses pixel values
that, if actually used are likely to be overly sensitive.

## Recommended for you

* Note: link text is displayed when JavaScript is off
* [Change focus behavior](/develop/ui/compose/touch-input/focus/change-focus-behavior)
* [Add keyboard, mouse, trackpad, and stylus support with Jetpack Compose](/codelabs/large-screens/add-keyboard-and-mouse-support-with-compose/index.lab)
* [Compose for Wear OS Codelab](/codelabs/compose-for-wear-os/index.lab)