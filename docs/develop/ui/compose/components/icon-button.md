---
title: https://developer.android.com/develop/ui/compose/components/icon-button
url: https://developer.android.com/develop/ui/compose/components/icon-button
source: md.txt
---

> Documentation index: https://developer.android.com/develop/ui/compose/components/llms.txt

[Icon buttons](https://m3.material.io/components/icon-buttons/guidelines#1f6f6121-e403-4d82-aa6a-5ab276f4bc4c) display actions that users can take. Icon buttons must use an
icon with a clear meaning, and typically represent common or frequently used
actions.

There are two types of icon buttons:

- **Default**: These buttons can open other elements, such as a menu or search.
- **Toggle**: These buttons can represent binary actions that can be toggled on or off, such as "favorite" or "bookmark".

![Five icon buttons with different icons, such as settings and more. Some are filled, indicating selection, and some are outlined.](https://developer.android.com/static/develop/ui/compose/images/components/icon-buttons.png) **Figure 1.** Icon buttons; some are filled (indicating selection), and others are outlined.

## API surface

Use the [`IconButton`](https://developer.android.com/reference/kotlin/androidx/compose/material3/IconButton.composable.md.txt) composable to implement standard icon buttons, and
[`IconToggleButton`](https://developer.android.com/reference/kotlin/androidx/compose/material3/IconToggleButton.composable.md.txt) for a button that toggles between selected and
unselected states. To create different visual styles like filled, filled tonal,
or outlined, use [`FilledIconButton`](https://developer.android.com/reference/kotlin/androidx/compose/material3/FilledIconButton.composable.md.txt#FilledIconButton(kotlin.Function0,androidx.compose.material3.IconButtonShapes,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.material3.IconButtonColors,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function0)), [`FilledTonalIconButton`](https://developer.android.com/reference/kotlin/androidx/compose/material3/FilledTonalIconButton.composable.md.txt#FilledTonalIconButton(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.compose.material3.IconButtonColors,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function0)), and
[`OutlinedIconButton`](https://developer.android.com/reference/kotlin/androidx/compose/material3/OutlinedIconButton.composable.md.txt#OutlinedIconButton(kotlin.Function0,androidx.compose.material3.IconButtonShapes,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.material3.IconButtonColors,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function0)), or their toggleable counterparts
`FilledIconToggleButton`, `FilledTonalIconToggleButton`, and
`OutlinedIconToggleButton`.

The key parameters for `IconButton` include:

- `onClick`: A lambda function that executes when the user taps the icon button.
- `enabled`: A boolean that controls the enabled state of the button. When `false`, the button does not respond to user input.
- `content`: The composable content inside the button, typically an `Icon`.

The key parameters for [`IconToggleButton`](https://developer.android.com/reference/kotlin/androidx/compose/material3/IconToggleButton.composable.md.txt) include:

- `checked`: A boolean that controls the selected state of the button.
- `onCheckedChange`: A lambda function that executes when the user taps the button, providing the new checked state.
- `enabled`: A boolean that controls the enabled state of the button. When `false`, the button does not respond to user input.

## Basic example: Toggle icon button

Toggle icon buttons allow a single choice to be selected or deselected, such as
adding or removing something from favorites. [`IconToggleButton`](https://developer.android.com/reference/kotlin/androidx/compose/material3/IconToggleButton.composable.md.txt) and its
variants are designed for this purpose.

The following example shows you how to implement a toggle icon button that
changes its appearance based on whether it's selected or unselected, by managing
state with `IconButton`:


```kotlin
@Preview
@Composable
fun ToggleIconButtonExample() {
    // isToggled initial value should be read from a view model or persistent storage.
    var isToggled by rememberSaveable { mutableStateOf(false) }

    IconButton(
        onClick = { isToggled = !isToggled }
    ) {
        Icon(
            painter = if (isToggled) painterResource(R.drawable.favorite_filled) else painterResource(R.drawable.favorite),
            contentDescription = if (isToggled) "Selected icon button" else "Unselected icon button."
        )
    }
}
```

<br />

### Key points about the code

- The `ToggleIconButtonExample` composable defines a toggleable `IconButton`.
  - `mutableStateOf(false)` creates a `MutableState` object that holds a boolean value, initially `false`. This makes `isToggled` a state holder, meaning Compose recomposes the UI whenever its value changes.
  - `rememberSaveable` makes sure that the `isToggled` state persists across configuration changes, like screen rotation.
- The `onClick` lambda of the `IconButton` defines the button's behavior when clicked, toggling the state between `true` and `false`.
- The [`Icon`](https://developer.android.com/reference/kotlin/androidx/compose/material3/Icon.composable.md.txt#Icon(androidx.compose.ui.graphics.painter.Painter,kotlin.String,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color)) composable's `painter` parameter conditionally loads a different `painterResource` based on the `isToggled` state. This changes the visual appearance of the icon.
  - If `isToggled` is `true`, it loads the filled heart drawable.
  - If `isToggled` is `false`, it loads the outlined heart drawable.
- The `contentDescription` of the `Icon` also updates based on the `isToggled` state to provide appropriate accessibility information.

### Result

The following image shows the toggle icon button from the preceding snippet in
its selected state:
![A filled heart icon button in its selected state.](https://developer.android.com/static/develop/ui/compose/images/components/previews/android_compose_components_togglebuttonexample.png) **Figure 2.** A "favorite" toggle icon button in its selected state.

## Advanced example: Repeated actions on press

This section demonstrates how to create icon buttons that continuously trigger
an action while the user presses and holds them, rather than just triggering
once per click.


```kotlin
@Composable
fun MomentaryIconButton(
    unselectedImage: Int,
    selectedImage: Int,
    contentDescription: String,
    modifier: Modifier = Modifier,
    stepDelay: Long = 100L, // Minimum value is 1L milliseconds.
    onClick: () -> Unit
) {
    val interactionSource = remember { MutableInteractionSource() }
    val isPressed by interactionSource.collectIsPressedAsState()
    val pressedListener by rememberUpdatedState(onClick)

    LaunchedEffect(isPressed) {
        while (isPressed) {
            delay(stepDelay.coerceIn(1L, Long.MAX_VALUE))
            pressedListener()
        }
    }

    IconButton(
        modifier = modifier,
        onClick = onClick,
        interactionSource = interactionSource
    ) {
        Icon(
            painter = if (isPressed) painterResource(id = selectedImage) else painterResource(id = unselectedImage),
            contentDescription = contentDescription,
        )
    }
}
```

<br />

### Key points about the code

- `MomentaryIconButton` takes an `unselectedImage: Int`, the drawable resource ID for the icon when the button is not pressed, and `selectedImage: Int`, the drawable resource ID for the icon when the button is pressed.
- It uses an `interactionSource` to specifically track "press" interactions from the user.
- `isPressed` is true when the button is actively being pressed and false otherwise. When `isPressed` is `true`, the `LaunchedEffect` enters a loop.
  - Inside this loop, it uses a `delay` (with `stepDelay`) to create pauses between triggering actions. `coerceIn` ensures the delay is at least 1ms to prevent infinite loops.
  - The `pressedListener` is invoked after each delay within the loop. This makes the action repeat.
- The `pressedListener` uses `rememberUpdatedState` to ensure that the `onClick` lambda (the action to perform) is always the most up-to-date from the latest composition.
- The `Icon` changes its displayed image based on whether the button is currently pressed or not.
  - If `isPressed` is true, the `selectedImage` is shown.
  - Otherwise, the `unselectedImage` is shown.

Next, use this `MomentaryIconButton` in an example. The following snippet
demonstrates two icon buttons controlling a counter:


```kotlin
@Preview()
@Composable
fun MomentaryIconButtonExample() {
    var pressedCount by remember { mutableIntStateOf(0) }

    Row(
        modifier = Modifier.fillMaxWidth(),
        verticalAlignment = Alignment.CenterVertically
    ) {
        MomentaryIconButton(
            unselectedImage = R.drawable.fast_rewind,
            selectedImage = R.drawable.fast_rewind_filled,
            stepDelay = 100L,
            onClick = { pressedCount -= 1 },
            contentDescription = "Decrease count button"
        )
        Spacer(modifier = Modifier)
        Text("advanced by $pressedCount frames")
        Spacer(modifier = Modifier)
        MomentaryIconButton(
            unselectedImage = R.drawable.fast_forward,
            selectedImage = R.drawable.fast_forward_filled,
            contentDescription = "Increase count button",
            stepDelay = 100L,
            onClick = { pressedCount += 1 }
        )
    }
}
```
![Rewind and fast-forward icon buttons on either side of the text 'advanced by 5 frames'.](https://developer.android.com/static/develop/ui/compose/images/components/previews/android_compose_components_momentaryiconbuttons.png)

<br />

### Key points about the code

- The `MomentaryIconButtonExample` composable displays a `Row` containing two `MomentaryIconButton` instances and a `Text` composable to build a UI for incrementing and decrementing a counter.
- It maintains a `pressedCount` mutable state variable using `remember` and `mutableIntStateOf`, initialized to 0. When `pressedCount` changes, any composables observing it (like the `Text` composable) recompose to reflect the new value.
- The first `MomentaryIconButton` decreases `pressedCount` when clicked or held.
- The second `MomentaryIconButton` increases `pressedCount` when clicked or held.
- Both buttons use a `stepDelay` of 100 milliseconds, meaning the `onClick` action repeats every 100ms while a button is held.

### Result

The following video shows the UI with the icon buttons and the counter:
**Figure 3**. A counter UI with two icon buttons (plus and minus) that increment and decrement the counter.

## M3 Expressive update

With the M3 Expressive update, icon buttons support additional size, corner, and
width options, and can change shape when pressed or selected. When placed in
standard button groups, icon buttons also interact with neighboring buttons when
pressed.

### Animated shape

Icon buttons can animate their shape when pressed, and toggle icon buttons can
animate their shape based on their checked state. To enable shape animation,
pass `IconButtonDefaults.shapes()` or `IconButtonDefaults.toggleableShapes()` to
the `shapes` parameter of `IconButton` or `IconToggleButton`.

#### Icon buttons

![States of icon button](https://developer.android.com/static/develop/ui/compose/images/components/iconbutton_shape_morph.png) **Figure 4.** Icon button shape animation in round and square shapes.

The following snippet demonstrates how to implement an icon button that animates
its shape when pressed:


```kotlin
@Composable
fun IconButtonWithAnimatedShapeSample() {
    IconButton(
        onClick = { /* doSomething() */ },
        shapes = IconButtonDefaults.shapes(),
    ) {
        Icon(painter = rememberVectorPainter(AppIcons.LockFilled), contentDescription = "Localized description")
    }
}
```
![An icon button displaying a filled lock icon.](https://developer.android.com/static/develop/ui/compose/images/components/previews/android_compose_expressive_components_animatediconbuttons.png)

<br />

#### Toggle icon buttons

![States of toggle icon button](https://developer.android.com/static/develop/ui/compose/images/components/toggle_iconbutton.png) **Figure 5.** Toggle icon button shape animation in unselected and selected states.

The following snippet demonstrates how to implement a toggle icon button that
animates its shape based on its checked state:


```kotlin
@Composable
fun IconToggleButtonWithAnimatedShapeSample() {
    var checked by remember { mutableStateOf(false) }
    IconToggleButton(
        checked = checked,
        onCheckedChange = { checked = it },
        shapes = IconButtonDefaults.toggleableShapes(),
    ) {
        if (checked) {
            Icon(painter = rememberVectorPainter(AppIcons.LockFilled), contentDescription = "Localized description")
        } else {
            Icon(painter = rememberVectorPainter(AppIcons.Lock), contentDescription = "Localized description")
        }
    }
}
```
![A toggle icon button in its unselected state displaying an outlined lock icon.](https://developer.android.com/static/develop/ui/compose/images/components/previews/android_compose_expressive_components_animatedtoggleiconbuttons.png)

<br />

### Size, width, and shape variants

Icon buttons are available in round and square shapes, five sizes, and three
widths.
![Examples of icon button sizes, shapes, and widths.](https://developer.android.com/static/develop/ui/compose/images/components/expressive_update.png) **Figure 6.** Expressive features include five sizes, two shapes, and three widths.

For more information about the M3 Expressive updates for icon buttons, see the
[Material Design 3 Icon buttons guidelines](https://m3.material.io/components/icon-buttons/guidelines#1f6f6121-e403-4d82-aa6a-5ab276f4bc4c).

There are five icon button size variants: extra small, small, medium, large, and
extra large. Each size supports three width options: uniform (default), narrow,
and wide.
![Five rows and three columns of icon buttons displaying a heart icon. Each row increases in size, and the three columns vary by width: uniform, narrow, and wide.](https://developer.android.com/static/develop/ui/compose/images/components/icon_button_Measurements.png) **Figure 7.** Icon buttons showing five sizes and three width options: uniform, narrow, and wide.

Icon buttons are available in round or square corner variants, and toggle icon
buttons change their shape when pressed or selected.
![Two rows of five icon buttons with a heart icon, increasing in size from left to right; the top row has round corners and the bottom row has square corners.](https://developer.android.com/static/develop/ui/compose/images/components/iconButtonCornerRadius.png) **Figure 8.** Icon buttons available in round or square corner variants.

For guidance on choosing between corner variants, see the [Material Design 3
Icon buttons guidelines](https://m3.material.io/components/icon-buttons/guidelines#1f6f6121-e403-4d82-aa6a-5ab276f4bc4c).

## Additional resources

- [Material 3 - Icon buttons](https://m3.material.io/components/icon-buttons/overview)