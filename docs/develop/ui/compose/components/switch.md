---
title: Switch  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/components/switch
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Switch Stay organized with collections Save and categorize content based on your preferences.




The [`Switch`](/reference/kotlin/androidx/compose/material3/Switch.composable#Switch(kotlin.Boolean,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Boolean,androidx.compose.material3.SwitchColors,androidx.compose.foundation.interaction.MutableInteractionSource)) component allows users to toggle between two states: checked
and unchecked. In your app you may use a switch to let the user to do one of the
following:

* Toggle a setting on or off.
* Enable or disable a feature.
* Select an option.

The component has two parts: the thumb and the track. The thumb is the draggable
part of the switch, and the track is the background. The user can drag the thumb
to the left or right to change the state of the switch. They can also tap the
switch to check and clear it.

![Examples of the Switch component in both light and dark mode.](/static/develop/ui/compose/images/components/switches.png)


**Figure 1.** The switch component.

## Basic implementation

See the [`Switch`](/reference/kotlin/androidx/compose/material3/Switch.composable#Switch(kotlin.Boolean,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Boolean,androidx.compose.material3.SwitchColors,androidx.compose.foundation.interaction.MutableInteractionSource)) reference for a full API definition. The following are
some of the key parameters you might need to use:

* **`checked`**: The initial state of the switch.
* **`onCheckedChange`**: A callback that is called when the state of the
  switch changes.
* **`enabled`**: Whether the switch is enabled or disabled.
* **`colors`**: The colors used for the switch.

The following example is a minimal implementation of the `Switch` composable.

```
@Composable
fun SwitchMinimalExample() {
    var checked by remember { mutableStateOf(true) }

    Switch(
        checked = checked,
        onCheckedChange = {
            checked = it
        }
    )
}

Switch.kt
```

This implementation appears as follows when unchecked:

![A basic switch that is unchecked.](/static/develop/ui/compose/images/components/switch-deactivated.png)


**Figure 2.** An unchecked switch.

This is the appearance when checked:

![A basic Switch that is checked.](/static/develop/ui/compose/images/components/switch.png)


**Figure 3.** A checked switch.

## Advanced implementation

The primary parameters you might want to use when implementing a more advanced
switch are the following:

* **`thumbContent`**: Use this to customize the appearance of the thumb when
  it is checked.
* **`colors`**: Use this to customize the color of the track and thumb.

### Custom thumb

You can pass any composable for the `thumbContent` parameter to create a custom
thumb. The following is an example of a switch that uses a custom icon for its
thumb:

```
@Composable
fun SwitchWithIconExample() {
    var checked by remember { mutableStateOf(true) }

    Switch(
        checked = checked,
        onCheckedChange = {
            checked = it
        },
        thumbContent = if (checked) {
            {
                Icon(
                    imageVector = Icons.Filled.Check,
                    contentDescription = null,
                    modifier = Modifier.size(SwitchDefaults.IconSize),
                )
            }
        } else {
            null
        }
    )
}

Switch.kt
```

In this implementation, the unchecked appearance is the same as the example in
the preceding section. However, when checked, this implementation appears as
follows:

![A switch that uses the thumbContent parameter to display a custom icon when checked.](/static/develop/ui/compose/images/components/switch-icon.png)


**Figure 4.** A switch with a custom checked icon.

### Custom colors

The following example demonstrates how you can use the colors parameter to
change the color of a switch's thumb and track, taking into account whether the
switch is checked.

```
@Composable
fun SwitchWithCustomColors() {
    var checked by remember { mutableStateOf(true) }

    Switch(
        checked = checked,
        onCheckedChange = {
            checked = it
        },
        colors = SwitchDefaults.colors(
            checkedThumbColor = MaterialTheme.colorScheme.primary,
            checkedTrackColor = MaterialTheme.colorScheme.primaryContainer,
            uncheckedThumbColor = MaterialTheme.colorScheme.secondary,
            uncheckedTrackColor = MaterialTheme.colorScheme.secondaryContainer,
        )
    )
}

Switch.kt
```

This implementation appears as follows:

![A switch that uses the colors parameter to display a switch with custom colors for both the thumb and track.](/static/develop/ui/compose/images/components/switch-colors.png)


**Figure 5.** A switch with custom colors.

## Additional resources

* [Material UI docs](https://m3.material.io/components/switch/overview)