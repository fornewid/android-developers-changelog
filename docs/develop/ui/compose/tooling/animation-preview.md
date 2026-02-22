---
title: https://developer.android.com/develop/ui/compose/tooling/animation-preview
url: https://developer.android.com/develop/ui/compose/tooling/animation-preview
source: md.txt
---

Android Studio allows you to inspect animations from Animation Preview. If an
animation is described in a composable preview, you can inspect the exact value
of each animated value at a given time, pause the animation, loop it,
fast-forward it, or slow it, to help you debug the animation throughout its
transitions:

![Play back, scrub through, and slow down the
AnimatedVisibility](https://developer.android.com/static/develop/ui/compose/images/animation-preview.gif)

You can also use Animation Preview to graph visualize animation curves, which is
useful for making sure that the animation values are choreographed properly:

![Visualization of an animation
curve](https://developer.android.com/static/develop/ui/compose/images/animation-preview-curve.gif)

Animation Preview automatically detects inspectable animations, which are
indicated by the **Start Animation Preview** icon
![Run icon](https://developer.android.com/static/develop/ui/compose/images/start-animation-inspection-icon.png).

![Start Animation Preview icon in Design
window](https://developer.android.com/static/develop/ui/compose/images/start-animation-inspection-highlight.png)

If you have multiple animations, you can use Animation Preview to inspect and
coordinate them all at once. You can also freeze a specific animation.

![Gif showing inspection with All Animations
UI](https://developer.android.com/static/studio/images/releases/compose-animation-coordination.gif)

Use pickers to set non-enum or boolean states to debug your Compose animation
using precise inputs. For all supported Compose Animation APIs, you can play,
pause, scrub, control speed, and coordinate.

![Pick precise values for animation previews](https://developer.android.com/static/studio/images/compose-animation-preview-picker.gif)

Animation Preview currently supports the
[`updateTransition`](https://developer.android.com/reference/kotlin/androidx/compose/animation/core/package-summary#updateTransition(kotlin.Any,kotlin.String)),
[`AnimatedVisibility`](https://developer.android.com/reference/kotlin/androidx/compose/animation/package-summary#AnimatedVisibility(androidx.compose.animation.core.MutableTransitionState,androidx.compose.ui.Modifier,androidx.compose.animation.EnterTransition,androidx.compose.animation.ExitTransition,kotlin.String,kotlin.Function1)),
[`animate*AsState`](https://developer.android.com/develop/ui/compose/animation#animate-as-state),
[`CrossFade`](https://developer.android.com/develop/ui/compose/animation#crossfade),
[`rememberInfiniteTransition`](https://developer.android.com/develop/ui/compose/animation#rememberinfinitetransition),
and [`AnimatedContent`](https://developer.android.com/develop/ui/compose/animation#animatedcontent)
APIs. To access the latest features, use Animation Preview with
Android Studio Panda 1 and `compose.animation` 1.10.2 and higher.

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Animations in Compose](https://developer.android.com/develop/ui/compose/animation/introduction)
- [Animation tooling support {:#tooling}](https://developer.android.com/develop/ui/compose/animation/tooling)
- [Value-based animations](https://developer.android.com/develop/ui/compose/animation/value-based)