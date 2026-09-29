---
title: https://developer.android.com/develop/ui/compose/touch-input/focus/focused-state
url: https://developer.android.com/develop/ui/compose/touch-input/focus/focused-state
source: md.txt
---

A focused state provides a clear visual cue to help users understand which UI
element currently holds input focus. All interactive Material 3 components
provide built-in focus indications by default.

> [!NOTE]
> **Note:** This guide covers how to draw visual focus indications. To programmatically listen to focus transitions, query focus flags (`isFocused`, `hasFocus`, `isCaptured`), or trigger state-driven UI changes, see [React to focus](https://developer.android.com/develop/ui/compose/touch-input/focus/react-to-focus).

## Material theme focus indication

Material components use the [`ripple`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#ripple(kotlin.Boolean,androidx.compose.ui.unit.Dp,androidx.compose.ui.graphics.Color)) function and [`LocalIndication`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/package-summary#LocalIndication())
to draw visual state changes.
To attach standard Material focus feedback to a custom component:

1. Create a [`MutableInteractionSource`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/interaction/MutableInteractionSource) using `remember { MutableInteractionSource() }`.
2. Pass the interaction source to the [`indication`](https://developer.android.com/reference/kotlin/androidx/compose/ui/Modifier#(androidx.compose.ui.Modifier).indication(androidx.compose.foundation.interaction.InteractionSource,androidx.compose.foundation.Indication)) modifier, alongside `ripple()`.


```kotlin
val interactionSource = remember { MutableInteractionSource() }

Box(
    modifier = Modifier
        .clickable(
            interactionSource = interactionSource,
            indication = null
        ) { /* onClick */ }
        .indication(
            interactionSource = interactionSource,
            indication = ripple()
        )
) {
    Text("Custom component with Material ripple")
}
```

<br />

## Implement custom focus indications

For custom visual cues (such as scaling, borders, or glowing effects):

1. Create an [`IndicationNodeFactory`](https://developer.android.com/develop/ui/compose/touch-input/user-interactions/migrate-indication-ripple#create-an-indicationnodefactory).
2. Observe focus interactions emitted by the element's `InteractionSource`.
3. Apply the custom indication using the `indication` modifier.


```kotlin
var interactionSource = remember { MutableInteractionSource() }

Card(
    modifier = Modifier
        .clickable(
            interactionSource = interactionSource,
            indication = MyHighlightIndication,
            enabled = true,
            onClick = { }
        )
) {
    Text("hello")
}
```

<br />

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Focus targets](https://developer.android.com/develop/ui/compose/touch-input/focus/focus-target)
- [Focus traversal order](https://developer.android.com/develop/ui/compose/touch-input/focus/focus-traversal)
- [React to focus](https://developer.android.com/develop/ui/compose/touch-input/focus/react-to-focus)