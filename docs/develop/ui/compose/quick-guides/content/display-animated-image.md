---
title: https://developer.android.com/develop/ui/compose/quick-guides/content/display-animated-image
url: https://developer.android.com/develop/ui/compose/quick-guides/content/display-animated-image
source: md.txt
---

<br />

You can create a more interactive and engaging user experience in your app by
loading a drawable file to display animated images. Animated images are useful
for creating loading indicators, success or error indicators, facilitating game
development, and various other UI functions.

## Results

![Hourglass animating its contents and rotating](https://developer.android.com/static/develop/ui/compose/images/animations/avd_example_compose.gif) **Figure 1.** Animated vector drawable in Compose.

## Version compatibility

This implementation requires that your project minSDK be set to API level 21 or
higher.

### Dependencies

<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/display-animated-image_8d8f9dd907dc7aee76397dfbc17c99c43149e016828d89b0492e85a9aeb07412.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

## Display an animated image

The following code displays an animated vector that automatically toggles
between two states:


```kotlin
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
```

<br />

### Key points about the code

- Loads a vector resource, animating the drawing attributes over time.
- An `Image` instance that uses a [`Painter`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/painter/Painter) instance to perform the animation, created from the `AnimatedImageVector` and `boolean` state by the `rememberAnimatedVectorPainter()` function.
- When `atEnd` is `true`, the `Painter` instance stops animating.

## Collections that contain this guide

This guide is part of these curated Quick Guide collections that cover
broader Android development goals:
![](https://developer.android.com/static/images/quick-guides/collection-illustration.png) ![](https://developer.android.com/static/images/picto-icons/collection.svg)

### Display images

Discover techniques for using bright, engaging visuals to give your Android app a beautiful look and feel. [Quick guide collection](https://developer.android.com/develop/ui/compose/quick-guides/collections/display-images) ![](https://developer.android.com/static/images/picto-icons/help.svg)

## Have questions or feedback

Go to our frequently asked questions page and learn about quick guides or reach out and let us know your thoughts. [Go to FAQ](https://developer.android.com/quick-guides/faq) [Leave feedback](https://issuetracker.google.com/issues/new?component=1573691&template=1993320)