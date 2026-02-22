---
title: https://developer.android.com/develop/ui/compose/components/slider
url: https://developer.android.com/develop/ui/compose/components/slider
source: md.txt
---

The [`Slider`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#Slider(androidx.compose.material3.SliderState,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.material3.SliderColors,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function1,kotlin.Function1)) composable allows users to make selections from a range of
values. You might use a slider to let the user do the following:

- Adjust settings that use a range of values, such as volume, and brightness.
- Filter data in a graph, as when setting a price range.
- User input, like setting a rating in a review.

The slider contains a track, thumb, value label, and tick marks:

- **Track**: The track is the horizontal bar that represents the range of values the slider can take.
- **Thumb**: The thumb is a draggable control element on the slider that allows the user to select a specific value within the range defined by the track.
- **Tick marks**: Tick marks are optional visual markers or indicators that appear along the track of the slider.

![A slider with thumb, track and tick marks.](https://developer.android.com/static/develop/ui/compose/images/components/slider.png) **Figure 1.** An implementation of a slider.

## Basic implementation

See the [`Slider`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#Slider(androidx.compose.material3.SliderState,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.material3.SliderColors,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function1,kotlin.Function1)) reference for a full API definition. Some of the key
parameters for the `Slider` composable are the following:

- **`value`**: The current value of the slider.
- **`onValueChange`**: A lambda that gets called every time the value is changed.
- **`enabled`**: A boolean value that indicates if the user can interact with the slider.

The following example is a straightforward slider. That allows the user to
select a value from `0.0` to `1.0`. Because the user can select any value in
that range, the slider is *continuous*.


```kotlin
@Preview
@Composable
fun SliderMinimalExample() {
    var sliderPosition by remember { mutableFloatStateOf(0f) }
    Column {
        Slider(
            value = sliderPosition,
            onValueChange = { sliderPosition = it }
        )
        Text(text = sliderPosition.toString())
    }
}
```

<br />

This implementation appears as follows:
![A slider component with a value selected roughly three quarters along the track.](https://developer.android.com/static/develop/ui/compose/images/components/slider-basic.png) **Figure 2.** A basic implementation of a slider.

## Advanced implementation

When implementing a more complex slider, you can additionally make use of the
following parameters.

- **`colors`** : An instance of `SliderColors` that lets you control the colors of the slider.
- **`valueRange`**: The range of values that the slider can take.
- **`steps`**: The number of notches on the slider to which the thumb snaps.

The following snippet implements a slider that has three steps, with a range
from `0.0` to `50.0`. Because the thumb snaps to each step, this slider is
*discrete*.


```kotlin
@Preview
@Composable
fun SliderAdvancedExample() {
    var sliderPosition by remember { mutableFloatStateOf(0f) }
    Column {
        Slider(
            value = sliderPosition,
            onValueChange = { sliderPosition = it },
            colors = SliderDefaults.colors(
                thumbColor = MaterialTheme.colorScheme.secondary,
                activeTrackColor = MaterialTheme.colorScheme.secondary,
                inactiveTrackColor = MaterialTheme.colorScheme.secondaryContainer,
            ),
            steps = 3,
            valueRange = 0f..50f
        )
        Text(text = sliderPosition.toString())
    }
}
```

<br />

The implementation appears as follows:
![A discrete slider with a range from 0 to 50, showing five tick marks at equal intervals. The thumb is positioned near the second tick mark, indicating a selected just of 16.](https://developer.android.com/static/develop/ui/compose/images/components/slider-advanced.png) **Figure 3.** A slider with steps and a set value range.

> [!NOTE]
> **Note:** The very beginning and end of a slider count as "steps". In the preceding example where the range is `0f..50f` and the number of `steps` is `3`, each interval along the range is `12.5` because the beginning and end of the slider are also intervals the user can select.

> [!NOTE]
> **Note:** You can also pass `Slider` a `thumb` and `track` composable to more thoroughly customize the appearance of the component.

## Range slider

You can also use the dedicated `RangeSlider` composable. This allows the user to
select two values. This can be useful in cases such as when the user wishes to
select a minimum and maximum price.

The following example is a relatively straightforward example of a continuous
range slider.


```kotlin
@Preview
@Composable
fun RangeSliderExample() {
    var sliderPosition by remember { mutableStateOf(0f..100f) }
    Column {
        RangeSlider(
            value = sliderPosition,
            steps = 5,
            onValueChange = { range -> sliderPosition = range },
            valueRange = 0f..100f,
            onValueChangeFinished = {
                // launch some business logic update with the state you hold
                // viewModel.updateSelectedSliderValue(sliderPosition)
            },
        )
        Text(text = sliderPosition.toString())
    }
}
```

<br />

![A range slider component with two values selected. A label displays the upper and lower bounds of the selection.](https://developer.android.com/static/develop/ui/compose/images/components/slider-range.png) **Figure 4.** An implementation of a range slider.

## Additional resources

- [Material UI docs](https://m3.material.io/components/sliders/overview)