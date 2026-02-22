---
title: https://developer.android.com/training/wearables/tiles/animations
url: https://developer.android.com/training/wearables/tiles/animations
source: md.txt
---

Tiles support a few different animation approaches, including the following:

- [Sweep transitions](https://developer.android.com/training/wearables/tiles/animations#sweep-transition) using tween animations.
- [Smooth fade and slide](https://developer.android.com/training/wearables/tiles/animations#smooth-fade-slide) animations into and out of a tile.
- [Lottie animations](https://developer.android.com/training/wearables/tiles/animations#lottie).

## Show a sweep transition

To show a smooth sweep from one value to another, you can enable [tween
animations](https://wikipedia.org/wiki/Inbetweening) for an element, as shown in the following code
snippet:

```kotlin
private var startValue = 15f
private var endValue = 105f
private val animationDurationInMillis = 2000L // 2 seconds

override fun onTileRequest(requestParams: RequestBuilders.TileRequest): ListenableFuture<Tile> {
    val circularProgressIndicator =
        CircularProgressIndicator.Builder()
            .setProgress(
                FloatProp.Builder(/* static value */ 0.25f)
                    .setDynamicValue(
                        // Or you can use some other dynamic object, for example
                        // from the platform and then at the end of expression
                        // add animate().
                        DynamicFloat.animate(
                            startValue,
                            endValue,
                            AnimationSpec.Builder()
                                .setAnimationParameters(
                                    AnimationParameters.Builder()
                                        .setDurationMillis(animationDurationInMillis)
                                        .build()
                                )
                                .build(),
                        )
                    )
                    .build()
            )
            .build()

    return Futures.immediateFuture(
        Tile.Builder()
            .setResourcesVersion(RESOURCES_VERSION)
            .setTileTimeline(Timeline.fromLayoutElement(circularProgressIndicator))
            .build()
    )
}
```

### Set arc direction

If your tile contains an arc, you might not want the arc line or text to always
grow in the default text direction for the user's chosen language. To specify an
arc growth direction, use the `ArcDirection` APIs:

```kotlin
public override fun onTileRequest(
    requestParams: RequestBuilders.TileRequest
): ListenableFuture<Tile> {
    return Futures.immediateFuture(
        Tile.Builder()
            .setResourcesVersion(RESOURCES_VERSION)
            .setTileTimeline(
                Timeline.fromLayoutElement(
                    EdgeContentLayout.Builder(deviceParameters)
                        .setResponsiveContentInsetEnabled(true)
                        .setEdgeContent(
                            Arc.Builder()
                                // Arc should always grow clockwise.
                                .setArcDirection(LayoutElementBuilders.ARC_DIRECTION_CLOCKWISE)
                                .addContent(
                                    ArcLine.Builder()
                                        // Set color, length, thickness, and more.
                                        // Arc should always grow clockwise.
                                        .setArcDirection(
                                            LayoutElementBuilders.ARC_DIRECTION_CLOCKWISE
                                        )
                                        .build()
                                )
                                .build()
                        )
                        .build()
                )
            )
            .build()
    )
}
```

## Show a smooth fade or slide

To indicate more clearly that an element is appearing or disappearing in a tile,
or to more subtly show a step-change in a tile's value, use fade and slide
effects in your tile animations.

If a tile layout contains an element whose value changes, the tile shows the
element's exit animation, then updates the layout and shows the element's enter
animation.

### Fade transitions

The following code snippet demonstrates how to perform fade-in and fade-out
transitions using the helper methods from [`DefaultContentTransitions`](https://developer.android.com/reference/androidx/wear/protolayout/ModifiersBuilders.DefaultContentTransitions). To
define custom `FadeInTransition` and `FadeOutTransition` objects, call
[`setFadeIn()`](https://developer.android.com/reference/androidx/wear/protolayout/ModifiersBuilders.EnterTransition.Builder#setFadeIn(androidx.wear.protolayout.ModifiersBuilders.FadeInTransition)) and [`setFadeOut()`](https://developer.android.com/reference/androidx/wear/protolayout/ModifiersBuilders.ExitTransition.Builder#setFadeOut(androidx.wear.protolayout.ModifiersBuilders.FadeOutTransition)), respectively, in the transition
setter methods.

```kotlin
public override fun onTileRequest(
    requestParams: RequestBuilders.TileRequest
): ListenableFuture<Tile> {
    // Assumes that you've defined a custom helper method called
    // getTileTextToShow().
    val tileText = getTileTextToShow()
    return Futures.immediateFuture(
        Tile.Builder()
            .setResourcesVersion(RESOURCES_VERSION)
            .setTileTimeline(
                Timeline.fromLayoutElement(
                    Text.Builder(this, tileText)
                        .setModifiers(
                            Modifiers.Builder()
                                .setContentUpdateAnimation(
                                    AnimatedVisibility.Builder()
                                        .setEnterTransition(DefaultContentTransitions.fadeIn())
                                        .setExitTransition(DefaultContentTransitions.fadeOut())
                                        .build()
                                )
                                .build()
                        )
                        .build()
                )
            )
            .build()
    )
}
```

### Slide transitions

This other code snippet demonstrates how to perform slide-in and slide-out
transitions using the helper methods from [`DefaultContentTransitions`](https://developer.android.com/reference/androidx/wear/protolayout/ModifiersBuilders.DefaultContentTransitions). You
can also define custom `SlideInTransition` and `SlideOutTransition` objects by
calling [`setSlideIn()`](https://developer.android.com/reference/androidx/wear/protolayout/ModifiersBuilders.EnterTransition.Builder#setSlideIn(androidx.wear.protolayout.ModifiersBuilders.SlideInTransition)) and [`setSlideOut()`](https://developer.android.com/reference/androidx/wear/protolayout/ModifiersBuilders.ExitTransition.Builder#setSlideOut(androidx.wear.protolayout.ModifiersBuilders.SlideOutTransition)), respectively, in the
transition setter methods.

```kotlin
public override fun onTileRequest(
    requestParams: RequestBuilders.TileRequest
): ListenableFuture<Tile> {
    // Assumes that you've defined a custom helper method called
    // getTileTextToShow().
    val tileText = getTileTextToShow()
    return Futures.immediateFuture(
        Tile.Builder()
            .setResourcesVersion(RESOURCES_VERSION)
            .setTileTimeline(
                Timeline.fromLayoutElement(
                    Text.Builder(this, tileText)
                        .setModifiers(
                            Modifiers.Builder()
                                .setContentUpdateAnimation(
                                    AnimatedVisibility.Builder()
                                        .setEnterTransition(
                                            DefaultContentTransitions.slideIn(
                                                ModifiersBuilders.SLIDE_DIRECTION_LEFT_TO_RIGHT
                                            )
                                        )
                                        .setExitTransition(
                                            DefaultContentTransitions.slideOut(
                                                ModifiersBuilders.SLIDE_DIRECTION_LEFT_TO_RIGHT
                                            )
                                        )
                                        .build()
                                )
                                .build()
                        )
                        .build()
                )
            )
            .build()
    )
}
```

## Show a transformation

To call attention to a specific element or area in a tile, you can apply several
types of transformations to it, including: rotation, scaling, and translation.

Many floating-point values associated with transformations accept [dynamic
expressions](https://developer.android.com/training/wearables/tiles/dynamic#associate-with-data-sources), which let you animate these transformations.

### Rotation

To perform a clockwise rotation about a customizable pivot point, use code
similar to the following:

```kotlin
return Futures.immediateFuture(
    Tile.Builder()
        .setResourcesVersion(RESOURCES_VERSION)
        .setTileTimeline(
            Timeline.fromLayoutElement(
                Text.Builder(this, someTileText)
                    .setModifiers(
                        Modifiers.Builder()
                            .setTransformation(
                                ModifiersBuilders.Transformation.Builder()
                                    // Set the pivot point 50 dp from the left edge
                                    // and 100 dp from the top edge of the screen.
                                    .setPivotX(dp(50f))
                                    .setPivotY(dp(100f))
                                    // Rotate the element 45 degrees clockwise.
                                    .setRotation(degrees(45f))
                                    .build()
                            )
                            .build()
                    )
                    .build()
            )
        )
        .build()
)
```

### Scaling

To grow or shrink an element by horizontal and vertical scaling factors, use
code similar to the following:

```kotlin
return Futures.immediateFuture(
    Tile.Builder()
        .setResourcesVersion(RESOURCES_VERSION)
        .setTileTimeline(
            Timeline.fromLayoutElement(
                Text.Builder(this, someTileText)
                    .setModifiers(
                        Modifiers.Builder()
                            .setTransformation(
                                ModifiersBuilders.Transformation.Builder()
                                    // Set the pivot point 50 dp from the left edge
                                    // and 100 dp from the top edge of the screen.
                                    .setPivotX(dp(50f))
                                    .setPivotY(dp(100f))
                                    // Shrink the element by a scale factor
                                    // of 0.5 horizontally and 0.75 vertically.
                                    .setScaleX(FloatProp.Builder(0.5f).build())
                                    .setScaleY(FloatProp.Builder(0.75f).build())
                                    .build()
                            )
                            .build()
                    )
                    .build()
            )
        )
        .build()
)
```

### Geometric translation

To move an element by a specific number of density pixels (dp) across the screen
horizontally or vertically, use code similar to the following:

```kotlin
return Futures.immediateFuture(
    Tile.Builder()
        .setResourcesVersion(RESOURCES_VERSION)
        .setTileTimeline(
            Timeline.fromLayoutElement(
                Text.Builder(this, someTileText)
                    .setModifiers(
                        Modifiers.Builder()
                            .setTransformation(
                                ModifiersBuilders.Transformation.Builder()
                                    // Translate (move) the element 60 dp to the right
                                    // and 80 dp down.
                                    .setTranslationX(dp(60f))
                                    .setTranslationY(dp(80f))
                                    .build()
                            )
                            .build()
                    )
                    .build()
            )
        )
        .build()
)
```

## Lottie animations

Tiles supports the playback of [Lottie animations](https://lottie.github.io/), using a syntax similar
to that of images:

```kotlin
class LottieAnimation : TileService() {

    val lottieResourceId = "lottie_animation"

    override fun onTileRequest(requestParams: RequestBuilders.TileRequest): ListenableFuture<Tile> {

        val layout =
            LayoutElementBuilders.Image.Builder()
                .setWidth(dp(150f))
                .setHeight(dp(150f))
                .setResourceId(lottieResourceId)
                .build()

        return Futures.immediateFuture(
            Tile.Builder()
                .setResourcesVersion(RESOURCES_VERSION)
                .setTileTimeline(Timeline.fromLayoutElement(layout))
                .build()
        )
    }

    override fun onTileResourcesRequest(
        requestParams: ResourcesRequest
    ): ListenableFuture<Resources> {

        val lottieImage =
            ResourceBuilders.ImageResource.Builder()
                .setAndroidLottieResourceByResId(
                    ResourceBuilders.AndroidLottieResourceByResId.Builder(R.raw.lottie)
                        .setStartTrigger(createOnVisibleTrigger())
                        .build()
                )
                .build()

        return Futures.immediateFuture(
            Resources.Builder()
                .setVersion(requestParams.version)
                .addIdToImageMapping(lottieResourceId, lottieImage)
                .build()
        )
    }
}
```

A few points to note:

- Only a subset of Lottie files are supported. Check compatibility using one of the following validators:
  - An online validator: <https://skottie.skia.org/>. In the "Compatibility Report" section, the file needs to pass the "Specification Errors", "Specification Warnings" (with Common Properties ignored) and "Low Power Profile Errors" tests.
  - A Rust validation library: <https://github.com/google/lottie-tools>.
- Lottie playback is supported by tile renderers with a major version of at least `1` and a minor version of at least `500`. If a given animation isn't supported, the animation doesn't appear, but the rest of the tile renders as expected. If needed, you can [provide a fallback option](https://developer.android.com/training/wearables/tiles/versioning#fallbacks), such as a static image.

## Don't show important information in the middle of an animation

There are several situations in which animations are disabled:

- The system's tile render might disable animations for all tiles.
- A tile can animate only 4 elements at a time. If you try to animate more than 4 elements at the same time, not all of them show an animation.

In the case where an animation is disabled, the elements are static and show the
animation's end value. For this reason, don't rely on the animation's behavior,
such as its duration, to show important information.