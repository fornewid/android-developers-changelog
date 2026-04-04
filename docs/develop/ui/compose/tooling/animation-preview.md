---
title: Animation Preview  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/tooling/animation-preview
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Animation Preview Stay organized with collections Save and categorize content based on your preferences.




Android Studio allows you to inspect animations from Animation Preview. If an
animation is described in a composable preview, you can inspect the exact value
of each animated value at a given time, pause the animation, loop it,
fast-forward it, or slow it, to help you debug the animation throughout its
transitions:

![Play back, scrub through, and slow down the
AnimatedVisibility](/static/develop/ui/compose/images/animation-preview.gif)

You can also use Animation Preview to graph visualize animation curves, which is
useful for making sure that the animation values are choreographed properly:

![Visualization of an animation
curve](/static/develop/ui/compose/images/animation-preview-curve.gif)

Animation Preview automatically detects inspectable animations, which are
indicated by the **Start Animation Preview** icon
![Run icon](/static/develop/ui/compose/images/start-animation-inspection-icon.png).

![Start Animation Preview icon in Design
window](/static/develop/ui/compose/images/start-animation-inspection-highlight.png)

If you have multiple animations, you can use Animation Preview to inspect and
coordinate them all at once. You can also freeze a specific animation.

![Gif showing inspection with All Animations
UI](/static/studio/images/releases/compose-animation-coordination.gif)

Use pickers to set non-enum or boolean states to debug your Compose animation
using precise inputs. For all supported Compose Animation APIs, you can play,
pause, scrub, control speed, and coordinate.

![Pick precise values for animation previews](/static/studio/images/compose-animation-preview-picker.gif)

Animation Preview currently supports the
[`updateTransition`](/reference/kotlin/androidx/compose/animation/core/updateTransition.composable#updateTransition(kotlin.Any,kotlin.String)),
[`AnimatedVisibility`](/reference/kotlin/androidx/compose/animation/AnimatedVisibility.composable#AnimatedVisibility(androidx.compose.animation.core.MutableTransitionState,androidx.compose.ui.Modifier,androidx.compose.animation.EnterTransition,androidx.compose.animation.ExitTransition,kotlin.String,kotlin.Function1)),
[`animate*AsState`](/develop/ui/compose/animation#animate-as-state),
[`CrossFade`](/develop/ui/compose/animation#crossfade),
[`rememberInfiniteTransition`](/develop/ui/compose/animation#rememberinfinitetransition),
and [`AnimatedContent`](/develop/ui/compose/animation#animatedcontent)
APIs. To access the latest features, use Animation Preview with
Android Studio Panda 3 and `compose.animation` 1.10.5 and higher.

## Recommended for you

* Note: link text is displayed when JavaScript is off
* [Animations in Compose](/develop/ui/compose/animation/introduction)
* [Animation tooling support {:#tooling}](/develop/ui/compose/animation/tooling)
* [Value-based animations](/develop/ui/compose/animation/value-based)

[Previous

arrow\_back

Preview your UI](/develop/ui/compose/tooling/previews)

[Next

Develop code iteratively

arrow\_forward](/develop/ui/compose/tooling/iterative-development)