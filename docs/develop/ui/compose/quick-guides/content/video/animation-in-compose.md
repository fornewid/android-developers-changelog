---
title: Animation in Compose  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/quick-guides/content/video/animation-in-compose
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Quick Guides](https://developer.android.com/develop/ui/compose/quick-guides)

# Animation in Compose Stay organized with collections Save and categorize content based on your preferences.



See how to animate state values, using transitions, animating visibility or size
changes and crossfades by using the Compose animation APIs.

## Key points

* The [`animate*AsState`](/reference/kotlin/androidx/compose/animation/core/animateDpAsState.composable#animateDpAsState(androidx.compose.ui.unit.Dp,androidx.compose.animation.core.AnimationSpec,kotlin.String,kotlin.Function1)) API is useful for animating a single value based
  on a state change.
* To animate multiple values at the same time, create a transition with the
  [`updateTransition`](/reference/kotlin/androidx/compose/animation/core/updateTransition.composable#updateTransition(kotlin.Any,kotlin.String)) function.
  + You can declare each animation value with an extension function on the
    transition object.
* To customize the animation behavior, specify the `transitionSpec` parameter.
* [`AnimatedVisibility`](/reference/kotlin/androidx/compose/animation/AnimatedVisibility.composable#(androidx.compose.animation.core.Transition).AnimatedVisibility(kotlin.Function1,androidx.compose.ui.Modifier,androidx.compose.animation.EnterTransition,androidx.compose.animation.ExitTransition,kotlin.Function1)) is useful for animating appearance and
  disappearance.
* Customize animation behavior by specifying parameters for enter and exit.
* To animate size changes of elements, use the [`animateContentSize`](/reference/kotlin/androidx/compose/animation/animateContentSize.modifier#(androidx.compose.ui.Modifier).animateContentSize(androidx.compose.animation.core.FiniteAnimationSpec,kotlin.Function2))
  modifier.
* To animate changes when you swap out portions of your UI, use the
  [`Crossfade`](/reference/kotlin/androidx/compose/animation/Crossfade.composable#(androidx.compose.animation.core.Transition).Crossfade(androidx.compose.ui.Modifier,androidx.compose.animation.core.FiniteAnimationSpec,kotlin.Function1,kotlin.Function1)) composable.

## Collections that contain this guide

This guide is part of these curated Quick Guide collections that cover
broader Android development goals:

![](/static/images/quick-guides/collection-illustration.png)

![](/static/images/picto-icons/collection.svg)

### Compose basics

This series of videos introduces various Compose APIs,
quickly showing you what’s available and how to use them.

[Quick guide collection](/develop/ui/compose/quick-guides/collections/compose-basics)

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