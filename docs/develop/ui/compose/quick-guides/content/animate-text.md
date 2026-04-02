---
title: Animate character-by-character the appearance of text  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/quick-guides/content/animate-text
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Quick Guides](https://developer.android.com/develop/ui/compose/quick-guides)

# Animate character-by-character the appearance of text Stay organized with collections Save and categorize content based on your preferences.




You can animate, character-by-character, the appearance of text, so it looks
like a streaming typing effect, similar to what a typewriter would produce.

## Results

[

](/static/quick-guides/content/animate_char_by_char_example.mp4)


**Figure 1.** Text and emoji animated character-by-character.

## Version compatibility

This implementation requires that your project minSDK be set to API level 21 or
higher.

### Dependencies

## Animate text character-by-character

This code animates text character-by-character. It tracks an index to control
how much of the text is revealed. The displayed text updates dynamically to show
only the characters up to the current index. Finally, the variable runs the
animation when it changes.

```
@Composable
private fun AnimatedText() {
    val text = "This text animates as though it is being typed \uD83E\uDDDE\u200D♀\uFE0F \uD83D\uDD10  \uD83D\uDC69\u200D❤\uFE0F\u200D\uD83D\uDC68 \uD83D\uDC74\uD83C\uDFFD"

    // Use BreakIterator as it correctly iterates over characters regardless of how they are
    // stored, for example, some emojis are made up of multiple characters.
    // You don't want to break up an emoji as it animates, so using BreakIterator will ensure
    // this is correctly handled!
    val breakIterator = remember(text) { BreakIterator.getCharacterInstance() }

    // Define how many milliseconds between each character should pause for. This will create the
    // illusion of an animation, as we delay the job after each character is iterated on.
    val typingDelayInMs = 50L

    var substringText by remember {
        mutableStateOf("")
    }
    LaunchedEffect(text) {
        // Initial start delay of the typing animation
        delay(1000)
        breakIterator.text = StringCharacterIterator(text)

        var nextIndex = breakIterator.next()
        // Iterate over the string, by index boundary
        while (nextIndex != BreakIterator.DONE) {
            substringText = text.subSequence(0, nextIndex).toString()
            // Go to the next logical character boundary
            nextIndex = breakIterator.next()
            delay(typingDelayInMs)
        }
    }
    Text(substringText)

AnimationSnippets.kt
```

### Key points about the code

* [`BreakIterator`](/reference/android/icu/text/BreakIterator) correctly iterates over characters regardless of how they
  are stored. For example, animated emojis are made up of multiple characters;
  `BreakIterator` ensures that they're handled as a single character, so that
  the animation isn't broken.
* [`LaunchedEffect`](/reference/kotlin/androidx/compose/runtime/LaunchedEffect.composable#LaunchedEffect(kotlin.Any,kotlin.coroutines.SuspendFunction1)) starts a coroutine to introduce the delay between
  the characters. You can replace the code block with a click
  listener–or any other event–to trigger animation.
* The [`Text`](/reference/kotlin/androidx/compose/material/Text.composable#Text(kotlin.String,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.font.FontStyle,androidx.compose.ui.text.font.FontWeight,androidx.compose.ui.text.font.FontFamily,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.style.TextDecoration,androidx.compose.ui.text.style.TextAlign,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.style.TextOverflow,kotlin.Boolean,kotlin.Int,kotlin.Int,kotlin.Function1,androidx.compose.ui.text.TextStyle)) composable re-renders every time the value
  of `substringText` is updated.

## Collections that contain this guide

This guide is part of these curated Quick Guide collections that cover
broader Android development goals:

![](/static/images/quick-guides/collection-illustration.png)

![](/static/images/picto-icons/collection.svg)

### Display text

Text is a central piece of any UI. Find out different ways
you can present text in your app to provide a delightful user experience.

[Quick guide collection](/develop/ui/compose/quick-guides/collections/display-text)

![](/static/images/quick-guides/collection-illustration.png)

![](/static/images/picto-icons/collection.svg)

### Compose basics (video collection)

This series of videos introduces various Compose APIs,
quickly showing you what’s available and how to use them.

[Quick guide collection](/develop/ui/compose/quick-guides/collections/compose-basics)

![](/static/images/picto-icons/help.svg)

## Have questions or feedback

Go to our frequently asked questions page and learn about quick guides or reach out and let us know your thoughts.

[Go to FAQ](/quick-guides/faq)
[Leave feedback](https://issuetracker.google.com/issues/new?component=1573691&template=1993320)