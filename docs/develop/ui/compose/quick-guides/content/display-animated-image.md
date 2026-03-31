---
title: Display an animated image  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/quick-guides/content/display-animated-image
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Quick Guides](https://developer.android.com/develop/ui/compose/quick-guides)

# Display an animated image Stay organized with collections Save and categorize content based on your preferences.



You can create a more interactive and engaging user experience in your app by
loading a drawable file to display animated images. Animated images are useful
for creating loading indicators, success or error indicators, facilitating game
development, and various other UI functions.

## Results

![Hourglass animating its contents and rotating](/static/develop/ui/compose/images/animations/avd_example_compose.gif)


**Figure 1.** Animated vector drawable in Compose.

## Version compatibility

This implementation requires that your project minSDK be set to API level 21 or
higher.

### Dependencies

## Display an animated image

The following code displays an animated vector that automatically toggles
between two states:

```
@Composable
fun AnimatedVectorDrawable() {
    val image = AnimatedImageVector.animatedVectorResource(R.drawable.ic_hourglass_animated)
    var atEnd by remember { mutableStateOf(false) }
    Image(
        painter = rememberAnimatedVectorPainter(image, atEnd),
        contentDescription = "Timer",
        modifier = Modifier.clickable {
            atEnd = !atEnd
        },
        contentScale = ContentScale.Crop
    )
}

AnimationSnippets.kt
```

### Key points about the code

* Loads a vector resource, animating the drawing attributes over time.
* An `Image` instance that uses a [`Painter`](/reference/kotlin/androidx/compose/ui/graphics/painter/Painter) instance to perform the
  animation, created from the `AnimatedImageVector` and `boolean` state by the
  `rememberAnimatedVectorPainter()` function.
* When `atEnd` is `true`, the `Painter` instance stops animating.

## Collections that contain this guide

This guide is part of these curated Quick Guide collections that cover
broader Android development goals:

![](/static/images/quick-guides/collection-illustration.png)

![](/static/images/picto-icons/collection.svg)

### Display images

Discover techniques for using bright, engaging visuals to
give your Android app a beautiful look and feel.

[Quick guide collection](/develop/ui/compose/quick-guides/collections/display-images)

![](/static/images/picto-icons/help.svg)

## Have questions or feedback

Go to our frequently asked questions page and learn about quick guides or reach out and let us know your thoughts.

[Go to FAQ](/quick-guides/faq)
[Leave feedback](https://issuetracker.google.com/issues/new?component=1573691&template=1993320)