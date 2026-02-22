---
title: https://developer.android.com/develop/ui/compose/quick-guides/content/video/five-animations-compose
url: https://developer.android.com/develop/ui/compose/quick-guides/content/video/five-animations-compose
source: md.txt
---

# Five quick animations in Compose

<br />

These 5 quick and easy animations can help make your app come to life in just a few minutes. Make your Compose app stand out even if you don't have the time to learn everything there is to know about animations.  

## Key points

- Wrap changing visible states in an[`AnimatedVisibility`](https://developer.android.com/reference/kotlin/androidx/compose/animation/package-summary#(androidx.compose.animation.core.Transition).AnimatedVisibility(kotlin.Function1,androidx.compose.ui.Modifier,androidx.compose.animation.EnterTransition,androidx.compose.animation.ExitTransition,kotlin.Function1))composable to transform how state changes show on screen.
- To smoothly transition between two states, use the built-in modifier[`animateContentSize`](https://developer.android.com/reference/kotlin/androidx/compose/animation/package-summary#(androidx.compose.ui.Modifier).animateContentSize(androidx.compose.animation.core.FiniteAnimationSpec,kotlin.Function2)).
- Wrap a`when`conditional in an[`AnimatedContent`](https://developer.android.com/reference/kotlin/androidx/compose/animation/package-summary#AnimatedContent(kotlin.Any,androidx.compose.ui.Modifier,kotlin.Function1,androidx.compose.ui.Alignment,kotlin.String,kotlin.Function1,kotlin.Function2))composable to switch content based on the provided target states.
- Use[`animate*AsState`](https://developer.android.com/reference/kotlin/androidx/compose/animation/core/package-summary#animateDpAsState(androidx.compose.ui.unit.Dp,androidx.compose.animation.core.AnimationSpec,kotlin.String,kotlin.Function1))functions to perform the animation when the state of your input variable changes.
- Compose triggers a redraw as variables change over time, creating an animation on screen.

## Resources

- [Blog: Customizing AnimatedContent in Jetpack Compose](https://medium.com/androiddevelopers/customizing-animatedcontent-in-jetpack-compose-629c67b45894)

## Collections that contain this guide

This guide is part of these curated Quick Guide collections that cover broader Android development goals:  
![](https://developer.android.com/static/images/quick-guides/collection-illustration.png)  
![](https://developer.android.com/static/images/picto-icons/collection.svg)  

### Display images

Discover techniques for using bright, engaging visuals to give your Android app a beautiful look and feel.  
[Quick guide collection](https://developer.android.com/develop/ui/compose/quick-guides/collections/display-images)
![](https://developer.android.com/static/images/picto-icons/help.svg)  

## Have questions or feedback

Go to our frequently asked questions page and learn about quick guides or reach out and let us know your thoughts.  
[Go to FAQ](https://developer.android.com/quick-guides/faq)[Leave feedback](https://issuetracker.google.com/issues/new?component=1573691&template=1993320)