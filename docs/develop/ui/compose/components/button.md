---
title: Button  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/components/button
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Button Stay organized with collections Save and categorize content based on your preferences.



Buttons are fundamental components that allow the user to trigger a defined
action. There are five types of buttons. This table describes the
appearance of each of the five button types, as well as where you should use
them:

| Type | Appearance | Purpose |
| --- | --- | --- |
| Filled | Solid background with contrasting text. | High-emphasis buttons. These are for primary actions in an application, such as "submit" and "save." The shadow effect highlights the button's importance. |
| Filled tonal | Background color varies to match the surface. | Also for primary or significant actions. Filled tonal buttons provide more visual weight and suit functions such as "add to cart" and "Sign in." |
| Elevated | Stands out by having a shadow. | Serves a similar purpose to tonal buttons. Increase elevation to make the button appear even more prominently. |
| Outlined | Features a border with no fill. | Medium-emphasis buttons, containing actions that are important but not primary. They pair well with other buttons to indicate alternative, secondary actions like "Cancel" or "Back." |
| Text | Displays text with no background or border. | Low-emphasis buttons, ideal for less critical actions such as navigational links, or secondary functions like "Learn More" or "View details." |

This image demonstrates the five types of buttons in Material Design:

![An example of each of the five button components, with their unique characteristics highlighted.](/static/develop/ui/compose/images/components/buttons.svg)


Figure 1. The five button components.

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

The filled button component uses the basic [`Button`](/reference/kotlin/androidx/compose/material3/package-summary?#Button(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.compose.material3.ButtonColors,androidx.compose.material3.ButtonElevation,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function1)) composable. It is
filled with a solid color by default. The snippet shows how to implement the
component:

```
@Composable
fun FilledButtonExample(onClick: () -> Unit) {
    Button(onClick = { onClick() }) {
        Text("Filled")
    }
}

Button.kt
```

**Note:** If you want to build a custom button, use the `Button` composable.

This implementation appears as shown:

![A filled button with a purple background that reads, 'Filled'.](/static/develop/ui/compose/images/components/button-filled.png)


Figure 2. A filled button.

## Filled tonal button

The filled tonal button component uses the [`FilledTonalButton`](/reference/kotlin/androidx/compose/material3/FilledTonalButton.composable#FilledTonalButton(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.compose.material3.ButtonColors,androidx.compose.material3.ButtonElevation,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function1)) composable.
It is filled with a tonal color by default.

The snippet shows how to implement the component:

```
@Composable
fun FilledTonalButtonExample(onClick: () -> Unit) {
    FilledTonalButton(onClick = { onClick() }) {
        Text("Tonal")
    }
}

Button.kt
```

This implementation appears as shown:

![A tonal button with a light purple background that reads, 'Tonal'.](/static/develop/ui/compose/images/components/button-tonal.png)


Figure 3. A tonal button.

## Outlined button

The outlined button component uses the [`OutlinedButton`](/reference/kotlin/androidx/compose/material3/OutlinedButton.composable#OutlinedButton(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.compose.material3.ButtonColors,androidx.compose.material3.ButtonElevation,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function1)) composable. It
appears with an outline by default.

The snippet shows how to implement the component:

```
@Composable
fun OutlinedButtonExample(onClick: () -> Unit) {
    OutlinedButton(onClick = { onClick() }) {
        Text("Outlined")
    }
}

Button.kt
```

This implementation appears as shown:

![A transparent outlined button with a dark border that reads, 'Outlined'.](/static/develop/ui/compose/images/components/button-outlined.png)


Figure 4. An outlined button.

## Elevated button

The elevated button component uses the [`ElevatedButton`](/reference/kotlin/androidx/compose/material3/ElevatedButton.composable#ElevatedButton(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.compose.material3.ButtonColors,androidx.compose.material3.ButtonElevation,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function1)) composable. It has
a shadow that represents the elevation effect by default. It is a filled button
that includes a shadow.

The snippet shows how to implement the component:

```
@Composable
fun ElevatedButtonExample(onClick: () -> Unit) {
    ElevatedButton(onClick = { onClick() }) {
        Text("Elevated")
    }
}

Button.kt
```

This implementation appears as shown:

![An elevated button with a gray background that reads, 'Elevated'.](/static/develop/ui/compose/images/components/button-elevated.png)


Figure 5. An elevated button.

## Text button

The text button component uses the [`TextButton`](/reference/kotlin/androidx/compose/material3/TextButton.composable#TextButton(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.compose.material3.ButtonColors,androidx.compose.material3.ButtonElevation,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function1)) composable. It appears as
only text until pressed. It does not have a solid fill or outline by default.

The snippet shows how to implement the component:

```
@Composable
fun TextButtonExample(onClick: () -> Unit) {
    TextButton(
        onClick = { onClick() }
    ) {
        Text("Text Button")
    }
}

Button.kt
```

This implementation appears as shown:

![A text button that reads 'Text Button'](/static/develop/ui/compose/images/components/button-text.png)


Figure 6. A text button.

## Additional resources

* [Floating action button](/develop/ui/compose/components/fab)
* [Material Design 3 Buttons overview](https://m3.material.io/components/buttons/overview)