---
title: https://developer.android.com/develop/ui/compose/components/tooltip
url: https://developer.android.com/develop/ui/compose/components/tooltip
source: md.txt
---

Use [tooltips](https://m3.material.io/components/tooltips/overview) to add context to a button or other UI element.
There are two types of tooltips:

- **Plain tooltips**: Describe elements or actions of icon buttons.
- **Rich tooltips**: Provide more detail, such as describing the value of a feature. Can also include an optional title, link, and buttons.

![Single line plain tooltip labeled (1), and a multi-line rich tooltip with a title and information block labeled (2).](https://developer.android.com/static/develop/ui/compose/images/tooltip-comparison.png) **Figure 1.** A plain tooltip (1) and a rich tooltip (2).

## API surface

You can use the [`TooltipBox`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#TooltipBox(androidx.compose.ui.window.PopupPositionProvider,kotlin.Function1,androidx.compose.material3.TooltipState,androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Boolean,kotlin.Boolean,kotlin.Function0)) composable to implement tooltips in your app.
You control [`TooltipBox`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#TooltipBox(androidx.compose.ui.window.PopupPositionProvider,kotlin.Function1,androidx.compose.material3.TooltipState,androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Boolean,kotlin.Boolean,kotlin.Function0)) appearance with these main parameters:

- `positionProvider`: Places the tooltip relative to the anchor content. You typically use a default position provider from the `TooltipDefaults`, or you can provide your own if you need custom positioning logic.
- `tooltip`: The composable that contains the tooltip's content. You typically use either the `PlainTooltip` or `RichTooltip` composables.
  - Use `PlainTooltip` to describe elements or actions of icon buttons.
  - Use `RichTooltip` to provide more details, like describing the value of a feature. Rich tooltips can include an optional title, link, and buttons.
- `state`: The state holder that contains the UI logic and element state for this tooltip.
- `content`: The composable content that the tooltip is anchored to.

## Display a plain tooltip

Use a plain tooltip to briefly describe a UI element. This code snippet displays
a plain tooltip on top of an icon button, labeled "Add to favorites":


```kotlin
@Composable
fun PlainTooltipExample(
    modifier: Modifier = Modifier,
    plainTooltipText: String = "Add to favorites"
) {
    TooltipBox(
        modifier = modifier,
        positionProvider = TooltipDefaults.rememberPlainTooltipPositionProvider(),
        tooltip = {
            PlainTooltip { Text(plainTooltipText) }
        },
        state = rememberTooltipState()
    ) {
        IconButton(onClick = { /* Do something... */ }) {
            Icon(
                imageVector = Icons.Filled.Favorite,
                contentDescription = "Add to favorites"
            )
        }
    }
}
```

<br />

### Key points about the code

- `TooltipBox` generates a tooltip with the text "Add to favorites".
  - [`TooltipDefaults.rememberPlainTooltipPositionProvider()`](https://developer.android.com/reference/kotlin/androidx/compose/material3/TooltipDefaults#rememberPlainTooltipPositionProvider(androidx.compose.ui.unit.Dp)) provides default positioning for plain tooltips.
  - `tooltip` is a lambda function that defines the tooltip's content using the [`PlainTooltip`](https://developer.android.com/reference/kotlin/androidx/compose/material3/TooltipScope#(androidx.compose.material3.TooltipScope).PlainTooltip(androidx.compose.ui.Modifier,androidx.compose.ui.unit.DpSize,androidx.compose.ui.unit.Dp,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.Dp,androidx.compose.ui.unit.Dp,kotlin.Function0)) composable.
  - `Text(plainTooltipText)` displays the text within the tooltip.
  - [`tooltipState`](https://developer.android.com/reference/kotlin/androidx/compose/material3/TooltipState) controls the state of the tooltip.
- `IconButton` creates a clickable button with an icon.
  - `Icon(...)` displays a heart icon within the button.
  - When a user interacts with the `IconButton`, `TooltipBox` shows the tooltip with the text "Add to favorites". Depending on the device, users can trigger the tooltip in the following ways:
  - Hovering over the icon with a cursor
  - Long-pressing the icon on a mobile device

### Result

This example produces a plain tooltip on top of an icon:
![Single-line tooltip containing the text](https://developer.android.com/static/develop/ui/compose/images/PlainTooltipExample.png) **Figure 2.**A plain tooltip that appears when a user hovers over or long-presses the heart icon.

## Display a rich tooltip

Use a rich tooltip to provide additional context about a UI element. This
example creates a multi-line rich tooltip with a title that is anchored to an
`Icon`:


```kotlin
@Composable
fun RichTooltipExample(
    modifier: Modifier = Modifier,
    richTooltipSubheadText: String = "Rich Tooltip",
    richTooltipText: String = "Rich tooltips support multiple lines of informational text."
) {
    TooltipBox(
        modifier = modifier,
        positionProvider = TooltipDefaults.rememberRichTooltipPositionProvider(),
        tooltip = {
            RichTooltip(
                title = { Text(richTooltipSubheadText) }
            ) {
                Text(richTooltipText)
            }
        },
        state = rememberTooltipState()
    ) {
        IconButton(onClick = { /* Icon button's click event */ }) {
            Icon(
                imageVector = Icons.Filled.Info,
                contentDescription = "Show more information"
            )
        }
    }
}
```

<br />

### Key points about the code

- `TooltipBox` handles the event listeners for user interactions and updates `TooltipState` accordingly. When `TooltipState` indicates that the tooltip should be shown, the tooltip lambda executes, and `TooltipBox` displays the `RichTooltip`. The `TooltipBox` acts as the anchor and container for both content and the tooltip.
  - In this case, the content is an `IconButton` component, which provides the tappable action behavior. When long-pressed (on touch devices) or hovered over (as with the mouse pointer) anywhere in `TooltipBox`'s content, the tooltip will display to show more information.
- The `RichTooltip` composable defines the tooltip's content, including the title and body text. [`TooltipDefaults.rememberRichTooltipPositionProvider()`](https://developer.android.com/reference/kotlin/androidx/compose/material3/TooltipDefaults#rememberRichTooltipPositionProvider(androidx.compose.ui.unit.Dp)) provides positioning information for rich tooltips.

### Result

This example produces a rich tooltip with a title attached to an information
icon:
![A multiple-line tooltip with the title](https://developer.android.com/static/develop/ui/compose/images/RichTooltipExample.png) **Figure 3.**A rich tooltip with a title and an information icon.

## Customize a rich tooltip

This code snippet displays a rich tooltip with a title, custom actions, and a
custom caret (arrow) displayed on top of a camera icon button:


```kotlin
@Composable
fun AdvancedRichTooltipExample(
    modifier: Modifier = Modifier,
    richTooltipSubheadText: String = "Custom Rich Tooltip",
    richTooltipText: String = "Rich tooltips support multiple lines of informational text.",
    richTooltipActionText: String = "Dismiss"
) {
    val tooltipState = rememberTooltipState()
    val coroutineScope = rememberCoroutineScope()

    TooltipBox(
        modifier = modifier,
        positionProvider = TooltipDefaults.rememberRichTooltipPositionProvider(),
        tooltip = {
            RichTooltip(
                title = { Text(richTooltipSubheadText) },
                action = {
                    Row {
                        TextButton(onClick = {
                            coroutineScope.launch {
                                tooltipState.dismiss()
                            }
                        }) {
                            Text(richTooltipActionText)
                        }
                    }
                },
            ) {
                Text(richTooltipText)
            }
        },
        state = tooltipState
    ) {
        IconButton(onClick = {
            coroutineScope.launch {
                tooltipState.show()
            }
        }) {
            Icon(
                imageVector = Icons.Filled.Camera,
                contentDescription = "Open camera"
            )
        }
    }
}
```

<br />

### Key points about the code

- A `RichToolTip` displays a tooltip with a title and dismiss action.
- When activated, either by a long-press or hovering over the `ToolTipBox` content with the mouse pointer, the tooltip is displayed for about one second. You can dismiss this tooltip by either tapping elsewhere on the screen or using the dismiss action button.
- When the dismiss action executes, the system launches a coroutine to call `tooltipState.dismiss`. This verifies the action execution isn't blocked while the tooltip is displayed.
- `onClick = coroutineScope.launch { tooltipState.show() } }` launches a coroutine to manually show the tooltip using `tooltipState.show`.
- The `action` parameter allows for the adding of interactive elements to a tooltip, such as a button.
- The `caretSize` parameter modifies the size of the tooltip's arrow.

### Result

This example produces the following:
![Multi-line tooltip with the title](https://developer.android.com/static/develop/ui/compose/images/AdvancedRichTooltipExample.png) **Figure 4.** A custom rich tooltip with a dismiss action anchored to a camera icon.

## Additional resources

- Material Design: [Tooltips](https://m3.material.io/components/tooltips/overview)