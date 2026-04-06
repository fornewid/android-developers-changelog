---
title: Animated vector images in Compose  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/animation/vectors
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Animated vector images in Compose Stay organized with collections Save and categorize content based on your preferences.




Animating vectors in Compose is possible in a few different ways. You can use any of the following:

* `AnimatedVectorDrawable` file format
* `ImageVector` with Compose animation APIs, like in [this Medium article](https://medium.com/androiddevelopers/making-jellyfish-move-in-compose-animating-imagevectors-and-applying-agsl-rendereffects-3666596a8888)
* A third-party solution like [Lottie](https://airbnb.design/lottie/)

## Animated vector drawables (experimental)

![Hourglass animating its contents and rotating](/static/develop/ui/compose/images/animations/avd_example_compose.gif)


**Figure 1.** Animated vector drawable in Compose

To use an [`AnimatedVectorDrawable`](/reference/android/graphics/drawable/AnimatedVectorDrawable) resource, load up the drawable file using `animatedVectorResource` and pass in a `boolean` to switch between the start and end state of your drawable, performing the animation.

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

For more information about the format of your drawable file, see [Animate drawable graphics](/guide/topics/graphics/drawable-animation).

## Recommended for you

* Note: link text is displayed when JavaScript is off
* [Loading images {:#loading-images}](/develop/ui/compose/graphics/images/loading)

[Previous

arrow\_back

Value-based animations](/develop/ui/compose/animation/value-based)

[Next

Customize animations

arrow\_forward](/develop/ui/compose/animation/customize)