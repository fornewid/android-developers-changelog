---
title: React to focus  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/touch-input/focus/react-to-focus
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# React to focus Stay organized with collections Save and categorize content based on your preferences.




## Provide visual cues for easier focus visualization

While all the focusable elements from Material Theme already have a focus style
that matches the theme, you might need to add some visual elements to make the
focused element easier to spot. A good solution would be to change the border of
your element with a color that has a good contrast with the background:

```
var color by remember { mutableStateOf(Color.White) }
Card(
    modifier = Modifier
        .onFocusChanged {
            color = if (it.isFocused) Red else White
        }
        .border(5.dp, color)
) {}

FocusSnippets.kt
```

In this example, `remember` is used to store the color of the border across
recompositions, and the outline of the element is updated every time the element
gains or loses focus.

### Implement advanced visual cues

With Jetpack Compose, you can also create more sophisticated and advanced visual
cues that match better with your UI.

1. First, create an `IndicationInstance` that visually draws the cue you want in your UI:

   ```
   private class MyHighlightIndicationNode(private val interactionSource: InteractionSource) :
       Modifier.Node(), DrawModifierNode {
       private var isFocused = false

       override fun onAttach() {
           coroutineScope.launch {
               var focusCount = 0
               interactionSource.interactions.collect { interaction ->
                   when (interaction) {
                       is FocusInteraction.Focus -> focusCount++
                       is FocusInteraction.Unfocus -> focusCount--
                   }
                   val focused = focusCount > 0
                   if (isFocused != focused) {
                       isFocused = focused
                       invalidateDraw()
                   }
               }
           }
       }

       override fun ContentDrawScope.draw() {
           drawContent()
           if (isFocused) {
               drawRect(size = size, color = Color.White, alpha = 0.2f)
           }
       }
   }

   FocusSnippets.kt
   ```
2. Next, create an `Indication` and remember the focused state:

   ```
   object MyHighlightIndication : IndicationNodeFactory {
       override fun create(interactionSource: InteractionSource): DelegatableNode {
           return MyHighlightIndicationNode(interactionSource)
       }

       override fun hashCode(): Int = -1

       override fun equals(other: Any?) = other === this
   }

   FocusSnippets.kt
   ```
3. Add both the `Indication` and an `InteractionSource` to the UI, via the `indication()` modifier:

   ```
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

   FocusSnippets.kt
   ```

## Understand the state of the focus

Generally, every time a state of the focus changes, a `FocusEvent` is fired up
the tree, and the parents of a `focusable()` modifier can listen to it using the
`onFocusChanged()` modifier.

If you need to know the state of the focus,you can use these APIs in conjunction
with the `onFocusChanged` modifier:

* `isFocused` returns `true` if the composable to which the modifier is attached
  is focused
* `hasFocus` works similarly to `isFocused`, but with a substantial difference:
  rather than checking only the current, it checks if the element or one of its
  children is focused
* `isCaptured` returns `true` whenever the focus is held. This happens, for
  instance, when a `TextField` contains incorrect data, so that trying to focus
  other elements will not clear the focus.

These fields are shown below:

```
Modifier.onFocusChanged {
    val isFocused = it.isFocused
    val hasFocus = it.hasFocus
    val isCaptured= it.isCaptured
}
```



## Recommended for you

* Note: link text is displayed when JavaScript is off
* [Change focus behavior](/develop/ui/compose/touch-input/focus/change-focus-behavior)
* [Material Design 2 in Compose](/develop/ui/compose/designsystems/material)
* [Handle user input](/develop/ui/compose/text/user-input)

[Previous

arrow\_back

Change focus behavior](/develop/ui/compose/touch-input/focus/change-focus-behavior)