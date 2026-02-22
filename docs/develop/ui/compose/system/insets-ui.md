---
title: https://developer.android.com/develop/ui/compose/system/insets-ui
url: https://developer.android.com/develop/ui/compose/system/insets-ui
source: md.txt
---

Once your Activity has taken control of handling all insets, you can use Compose
APIs to verify that content isn't obscured and interactable elements don't
overlap with the system UI. These APIs also synchronize your app's layout with
inset changes.

## Handle insets using padding or size modifiers

For example, this is the most basic method of applying the insets to the content
of your entire app:


```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)

    enableEdgeToEdge()

    setContent {
        Box(Modifier.safeDrawingPadding()) {
            // the rest of the app
        }
    }
}
```

<br />

This snippet applies the [`safeDrawing`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#(androidx.compose.foundation.layout.WindowInsets.Companion).safeDrawing()) window insets as padding around the
entire content of the app. While this ensures that interactable elements don't
overlap with the system UI, it also means that none of the app will draw behind
the system UI to achieve an edge-to-edge effect. To make full use of the entire
window, you need to fine-tune where the insets are applied on a screen-by-screen
or component-by-component basis.

All of these inset types are animated automatically with IME animations
backported to API 21. By extension, all of your layouts using these insets are
also automatically animated as the inset values change.

There are three ways to handle insets to adjust your Composable layouts:

- [rulers](https://developer.android.com/develop/ui/compose/system/evaluate-rulers)
- [padding modifiers](https://developer.android.com/develop/ui/compose/system/insets-ui#padding-modifiers)
- [inset size modifiers](https://developer.android.com/develop/ui/compose/system/insets-ui#inset-size)

### Padding modifiers

[`Modifier.windowInsetsPadding(windowInsets: WindowInsets)`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#(androidx.compose.ui.Modifier).windowInsetsPadding(androidx.compose.foundation.layout.WindowInsets)) applies the
given window insets as padding, acting just like [`Modifier.padding`](https://developer.android.com/reference/kotlin/androidx/compose/ui/Modifier#(androidx.compose.ui.Modifier).padding(androidx.compose.ui.unit.Dp,androidx.compose.ui.unit.Dp,androidx.compose.ui.unit.Dp,androidx.compose.ui.unit.Dp)) would.
For example, `Modifier.windowInsetsPadding(WindowInsets.safeDrawing)` applies
the safe drawing insets as padding on all 4 sides.

There are also several built-in utility methods for the most common inset types.
[`Modifier.safeDrawingPadding()`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#(androidx.compose.ui.Modifier).safeDrawingPadding()) is one such method, equivalent to
`Modifier.windowInsetsPadding(WindowInsets.safeDrawing)`. There are analogous
modifiers for the other inset types.

### Inset size modifiers

The following modifiers apply an amount of window insets by setting the size of
the component to be the size of the insets:

|---|---|
| [`Modifier.windowInsetsStartWidth(windowInsets: WindowInsets)`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#(androidx.compose.ui.Modifier).windowInsetsStartWidth(androidx.compose.foundation.layout.WindowInsets)) | Applies the start side of windowInsets as the width (like `Modifier.width`) |
| [`Modifier.windowInsetsEndWidth(windowInsets: WindowInsets)`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#(androidx.compose.ui.Modifier).windowInsetsEndWidth(androidx.compose.foundation.layout.WindowInsets)) | Applies the end side of windowInsets as the width (like `Modifier.width`) |
| [`Modifier.windowInsetsTopHeight(windowInsets: WindowInsets)`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#(androidx.compose.ui.Modifier).windowInsetsTopHeight(androidx.compose.foundation.layout.WindowInsets)) | Applies the top side of windowInsets as the height (like `Modifier.height`) |
| [`Modifier.windowInsetsBottomHeight(windowInsets: WindowInsets)`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#(androidx.compose.ui.Modifier).windowInsetsBottomHeight(androidx.compose.foundation.layout.WindowInsets)) | Applies the bottom side of windowInsets as the height (like `Modifier.height`) |

These modifiers are especially useful for sizing a `Spacer` that takes up the
space of insets:


```kotlin
LazyColumn(
    Modifier.imePadding()
) {
    // Other content
    item {
        Spacer(
            Modifier.windowInsetsBottomHeight(
                WindowInsets.systemBars
            )
        )
    }
}
```

<br />

## Inset consumption

The inset padding modifiers (`windowInsetsPadding` and helpers like
`safeDrawingPadding`) automatically consume the portion of the insets that are
applied as padding. While going deeper into the composition tree, nested inset
padding modifiers and the inset size modifiers know that some portion of the
insets have already been consumed by outer inset padding modifiers, and avoid
using the same portion of the insets more than once which would result in too
much extra space.

Inset size modifiers also avoid using the same portion of insets more than once
if insets have already been consumed. However, since they are changing their
size directly, they don't consume insets themselves.

As a result, nesting padding modifiers automatically change the amount of
padding applied to each composable.

Looking at the same `LazyColumn` example as before, the `LazyColumn` is being
resized by the `imePadding` modifier. Inside the `LazyColumn`, the last item is
sized to be the height of the bottom of the system bars:


```kotlin
LazyColumn(
    Modifier.imePadding()
) {
    // Other content
    item {
        Spacer(
            Modifier.windowInsetsBottomHeight(
                WindowInsets.systemBars
            )
        )
    }
}
```

<br />

When the IME is closed, the `imePadding()` modifier applies no padding, since
the IME has no height. Since the `imePadding()` modifier is applying no padding,
no insets are being consumed, and the height of the `Spacer` will be the size of
the bottom side of the system bars.

When the IME opens, the IME insets animate to match the size of the IME, and the
`imePadding()` modifier begins applying bottom padding to resize the
`LazyColumn` as the IME opens. As the `imePadding()` modifier begins applying
bottom padding, it also starts consuming that amount of insets. Therefore, the
height of the `Spacer` starts to decrease, as part of the spacing for the system
bars has already been applied by the `imePadding()` modifier. Once the
`imePadding()` modifier is applying an amount of bottom padding that is larger
than the system bars, the height of the `Spacer` is zero.

When the IME closes, the changes happen in reverse: The `Spacer` starts to
expand from a height of zero once the `imePadding()` is applying less than the
bottom side of the system bars, until finally the `Spacer` matches the height of
the bottom side of the system bars once the IME is completely animated out.
**Figure 2.** Edge-to-edge lazy column with `TextField`.

> [!CAUTION]
> **Caution:** Use `Spacer` instead of `contentPadding` to draw the last `TextField` in a `LazyColumn` above the system bars. Otherwise, the IME may hide the `TextField`.

This behavior is accomplished through communication between all
`windowInsetsPadding` modifiers, and can be influenced in a couple of other
ways.

[`Modifier.consumeWindowInsets(insets: WindowInsets)`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#(androidx.compose.ui.Modifier).consumeWindowInsets(androidx.compose.foundation.layout.WindowInsets)) also consumes insets
in the same way as [`Modifier.windowInsetsPadding`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#(androidx.compose.ui.Modifier).windowInsetsPadding(androidx.compose.foundation.layout.WindowInsets)), but it doesn't apply
the consumed insets as padding. This is useful in combination with the inset
size modifiers, to indicate to siblings that a certain amount of insets have
already been consumed:


```kotlin
Column(Modifier.verticalScroll(rememberScrollState())) {
    Spacer(Modifier.windowInsetsTopHeight(WindowInsets.systemBars))

    Column(
        Modifier.consumeWindowInsets(
            WindowInsets.systemBars.only(WindowInsetsSides.Vertical)
        )
    ) {
        // content
        Spacer(Modifier.windowInsetsBottomHeight(WindowInsets.ime))
    }

    Spacer(Modifier.windowInsetsBottomHeight(WindowInsets.systemBars))
}
```

<br />

[`Modifier.consumeWindowInsets(paddingValues: PaddingValues)`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#(androidx.compose.ui.Modifier).consumeWindowInsets(androidx.compose.foundation.layout.PaddingValues)) behaves very
similarly to the version with a [`WindowInsets`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/WindowInsets) argument, but takes an
arbitrary [`PaddingValues`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/PaddingValues) to consume. This is useful for informing
children when padding or spacing is provided by some other mechanism than the
inset padding modifiers, such as an ordinary `Modifier.padding` or fixed height
spacers:


```kotlin
Column(Modifier.padding(16.dp).consumeWindowInsets(PaddingValues(16.dp))) {
    // content
    Spacer(Modifier.windowInsetsBottomHeight(WindowInsets.ime))
}
```

<br />

In cases where the raw window insets are needed without consumption, use the
`WindowInsets` values directly, or use [`WindowInsets.asPaddingValues()`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/WindowInsets#(androidx.compose.foundation.layout.WindowInsets).asPaddingValues()) to
return a `PaddingValues` of the insets that are unaffected by consumption.
However, due to the following caveats, prefer to use the window insets padding
modifiers and window insets size modifiers wherever possible.

## Insets and Jetpack Compose phases

Compose uses the underlying AndroidX core APIs to update and animate insets,
which use the underlying platform APIs managing insets. Because of that platform
behavior, insets have a special relationship with the [phases of Jetpack
Compose](https://developer.android.com/develop/ui/compose/phases).

The value of insets are updated *after* the composition phase, but *before* the
layout phase. This means that reading the value of insets in composition
generally uses a value of the insets that is one frame late. The built-in
modifiers described on this page are built to delay using the values of the
insets until the layout phase, which ensures that the inset values are used on
the same frame as they are updated.