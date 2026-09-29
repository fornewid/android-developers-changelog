---
title: https://developer.android.com/develop/ui/compose/touch-input/focus/focus-target
url: https://developer.android.com/develop/ui/compose/touch-input/focus/focus-target
source: md.txt
---

A focus target is a UI element that keyboard focus can move to. Users can move
keyboard focus with the <kbd>Tab</kbd> key or directional (arrow) keys:

- <kbd>Tab</kbd> or <kbd>Shift+Tab</kbd> --- Move focus forward or backward in one-dimensional appearance order.
- Directional keys --- Move focus two-dimensionally (<kbd>Up</kbd>, <kbd>Down</kbd>, <kbd>Left</kbd>, and <kbd>Right</kbd>).

## Interactive UI elements are focus targets by default

An interactive component is a focus target by default. In other words, a UI
element is a focus target if users can tap or click it.

For example, consider three [Card](https://developer.android.com/develop/ui/compose/components/card) components. If the first and third cards are
interactive (they define an `onClick` callback), but the second card is purely
informational (has no click handling), pressing the <kbd>Tab</kbd> key on the first card
skips the second card and advances directly to the third card.


```kotlin
Card(onClick = { /* First card action */ }) {
    Text("Card 1 (Interactive)")
}
Card {
    Text("Card 2 (Informational - not focusable)")
}
Card(onClick = { /* Third card action */ }) {
    Text("Card 3 (Interactive)")
}
```

<br />

You can make the second card a focus target by providing an [`onClick`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#Card(androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Shape,androidx.compose.material3.CardColors,androidx.compose.material3.CardElevation,androidx.compose.foundation.BorderStroke,kotlin.Function1))
parameter:


```kotlin
Card(onClick = { /* Second card action */ }) {
    Text("Card 2 (Now interactive and focusable)")
}
```

<br />

The [`clickable`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/package-summary#(androidx.compose.ui.Modifier).clickable(kotlin.Boolean,kotlin.String,androidx.compose.ui.semantics.Role,kotlin.Function0)) modifier also turns custom or standard UI elements into
focus targets. Refer to [Tap and press](https://developer.android.com/develop/ui/compose/touch-input/pointer-input/tap-and-press) for details.

> [!WARNING]
> **Warning:** Don't use the `focusable` modifier and the `clickable` modifier at the same time. It leads to incorrect behavior because it creates two independent focus targets.


```kotlin
Box(
    modifier = Modifier
        .clickable { /* Handle click */ }
) {
    Text("Custom interactive element")
}
```

<br />

## Make a composable a non-clickable focus target

The [`focusable`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/package-summary#(androidx.compose.ui.Modifier).focusable(kotlin.Boolean,androidx.compose.foundation.interaction.MutableInteractionSource)) modifier makes a composable a focus target without requiring
click semantics. Users can move keyboard focus to the modified composable (for
example, to inspect content with accessibility tools or scroll the viewport),
but pressing <kbd>Enter</kbd> or <kbd>Space</kbd> keys
don't trigger a click action:


```kotlin
Box(
    modifier = Modifier
        .focusable()
) {
    Text("Non-clickable focus target")
}
```

<br />

## Make a composable unfocusable

In some scenarios, you may want to exclude an interactive element from keyboard
navigation without disabling pointer or click events. You can prevent a
component from receiving focus by setting `canFocus = false` inside the
[`focusProperties`](https://developer.android.com/reference/kotlin/androidx/compose/ui/focus/package-summary#(androidx.compose.ui.Modifier).focusProperties(kotlin.Function1)) modifier:


```kotlin
var checked by remember { mutableStateOf(false) }

Switch(
    checked = checked,
    onCheckedChange = { checked = it },
    // Prevent component from being focused
    modifier = Modifier
        .focusProperties { canFocus = false }
)
```

<br />

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Focus traversal order](https://developer.android.com/develop/ui/compose/touch-input/focus/focus-traversal)
- [Focus in text fields](https://developer.android.com/develop/ui/compose/touch-input/focus/focus-in-text-fields)
- [Group focus targets](https://developer.android.com/develop/ui/compose/touch-input/focus/focus-group)
- [Indicate focus state](https://developer.android.com/develop/ui/compose/touch-input/focus/focused-state)
- [Test focus navigation](https://developer.android.com/develop/ui/compose/touch-input/focus/testing-focus)