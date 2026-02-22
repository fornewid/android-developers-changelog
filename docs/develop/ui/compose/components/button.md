---
title: https://developer.android.com/develop/ui/compose/components/button
url: https://developer.android.com/develop/ui/compose/components/button
source: md.txt
---

Buttons are fundamental components that allow the user to trigger a defined
action. There are five types of buttons. This table describes the
appearance of each of the five button types, as well as where you should use
them:

| Type | Appearance | Purpose |
|---|---|---|
| Filled | Solid background with contrasting text. | High-emphasis buttons. These are for primary actions in an application, such as "submit" and "save." The shadow effect highlights the button's importance. |
| Filled tonal | Background color varies to match the surface. | Also for primary or significant actions. Filled tonal buttons provide more visual weight and suit functions such as "add to cart" and "Sign in." |
| Elevated | Stands out by having a shadow. | Serves a similar purpose to tonal buttons. Increase elevation to make the button appear even more prominently. |
| Outlined | Features a border with no fill. | Medium-emphasis buttons, containing actions that are important but not primary. They pair well with other buttons to indicate alternative, secondary actions like "Cancel" or "Back." |
| Text | Displays text with no background or border. | Low-emphasis buttons, ideal for less critical actions such as navigational links, or secondary functions like "Learn More" or "View details." |

This image demonstrates the five types of buttons in Material Design:
![An example of each of the five button components, with their unique characteristics highlighted.](https://developer.android.com/static/develop/ui/compose/images/components/buttons.svg) Figure 1. The five button components.

## API surface

`onClick`
:   The function that the system calls when the user presses the button.

`enabled`
:   When `false`, this parameter makes the button appear unavailable and
    inactive.

`colors`
:   An instance of `ButtonColors` that determines the colors used in the
    button.

`contentPadding`
:   The padding within the button.

## Filled button

The filled button component uses the basic [`Button`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#Button(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.compose.material3.ButtonColors,androidx.compose.material3.ButtonElevation,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function1)) composable. It is
filled with a solid color by default. The snippet shows how to implement the
component:


```kotlin
@Composable
fun FilledButtonExample(onClick: () -> Unit) {
    Button(onClick = { onClick() }) {
        Text("Filled")
    }
}
```

<br />

> [!NOTE]
> **Note:** If you want to build a custom button, use the `Button` composable.

This implementation appears as shown:
![A filled button with a purple background that reads, 'Filled'.](https://developer.android.com/static/develop/ui/compose/images/components/button-filled.png) Figure 2. A filled button.

## Filled tonal button

The filled tonal button component uses the [`FilledTonalButton`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#FilledTonalButton(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.compose.material3.ButtonColors,androidx.compose.material3.ButtonElevation,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function1)) composable.
It is filled with a tonal color by default.

The snippet shows how to implement the component:


```kotlin
@Composable
fun FilledTonalButtonExample(onClick: () -> Unit) {
    FilledTonalButton(onClick = { onClick() }) {
        Text("Tonal")
    }
}
```

<br />

This implementation appears as shown:
![A tonal button with a light purple background that reads, 'Tonal'.](https://developer.android.com/static/develop/ui/compose/images/components/button-tonal.png) Figure 3. A tonal button.

## Outlined button

The outlined button component uses the [`OutlinedButton`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#OutlinedButton(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.compose.material3.ButtonColors,androidx.compose.material3.ButtonElevation,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function1)) composable. It
appears with an outline by default.

The snippet shows how to implement the component:


```kotlin
@Composable
fun OutlinedButtonExample(onClick: () -> Unit) {
    OutlinedButton(onClick = { onClick() }) {
        Text("Outlined")
    }
}
```

<br />

This implementation appears as shown:
![A transparent outlined button with a dark border that reads, 'Outlined'.](https://developer.android.com/static/develop/ui/compose/images/components/button-outlined.png) Figure 4. An outlined button.

## Elevated button

The elevated button component uses the [`ElevatedButton`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#ElevatedButton(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.compose.material3.ButtonColors,androidx.compose.material3.ButtonElevation,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function1)) composable. It has
a shadow that represents the elevation effect by default. It is a filled button
that includes a shadow.

The snippet shows how to implement the component:


```kotlin
@Composable
fun ElevatedButtonExample(onClick: () -> Unit) {
    ElevatedButton(onClick = { onClick() }) {
        Text("Elevated")
    }
}
```

<br />

This implementation appears as shown:
![An elevated button with a gray background that reads, 'Elevated'.](https://developer.android.com/static/develop/ui/compose/images/components/button-elevated.png) Figure 5. An elevated button.

## Text button

The text button component uses the [`TextButton`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#TextButton(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.compose.material3.ButtonColors,androidx.compose.material3.ButtonElevation,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function1)) composable. It appears as
only text until pressed. It does not have a solid fill or outline by default.

The snippet shows how to implement the component:


```kotlin
@Composable
fun TextButtonExample(onClick: () -> Unit) {
    TextButton(
        onClick = { onClick() }
    ) {
        Text("Text Button")
    }
}
```

<br />

This implementation appears as shown:
![A text button that reads 'Text Button'](https://developer.android.com/static/develop/ui/compose/images/components/button-text.png) Figure 6. A text button.

## Additional resources

- [Floating action button](https://developer.android.com/develop/ui/compose/components/fab)
- [Material Design 3 Buttons overview](https://m3.material.io/components/buttons/overview)