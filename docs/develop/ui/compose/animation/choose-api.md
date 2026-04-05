---
title: Choose an animation API  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/animation/choose-api
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Choose an animation API Stay organized with collections Save and categorize content based on your preferences.




The following diagram helps you decide what API to use to implement your animation.

![Flowchart describing the decision tree for choosing the appropriate animation API](/static/develop/ui/compose/images/animations/compose_animation_decision_tree_v2.jpg)


**Figure 1.** Decision tree describing how to choose the appropriate animation API.

![Flowchart describing the decision tree for choosing the appropriate animation API](/static/develop/ui/compose/images/animations/compose_animation_decision_tree_v2.jpg)

Use the following decision tree to choose the most appropriate animation API for your use case:

* Is your animation art-based (that is, SVGs or images)?
  + Yes: Does it use simple SVGs (that is, an icon with micro-animations)?
    - Yes: [`AnimatedVectorDrawable`](/develop/ui/compose/animation/avd).
    - No: Third-party animation framework, for example, [`Lottie`](https://airbnb.io/lottie/).
  + No: Does the animation need to repeat infinitely?
    - Yes: [`rememberInfiniteTransition`](/develop/ui/compose/animation/value-based#rememberinfinitetransition).
    - No: Are you animating a layout?
      * Yes: Are you switching between composables with different content?
        + Yes: Are you using Navigation-Compose?
          - Yes: [`composable()`](/reference/kotlin/androidx/navigation/compose/package-summary#(androidx.navigation.NavGraphBuilder).composable(kotlin.String,kotlin.collections.List,kotlin.collections.List,kotlin.Function1,kotlin.Function1,kotlin.Function1,kotlin.Function1,kotlin.Function2)) with `enterTransition` and `exitTransition` set.
          - No: [`AnimatedContent`](/develop/ui/compose/animation/composables-modifiers#animatedcontent), [`Crossfade`](/develop/ui/compose/animation/composables-modifiers#crossfade), or [`Pager`](/develop/ui/compose/layouts/pager).
        + No: Are you animating the appearance or disappearance of content?
          - Yes: [`AnimatedVisibility`](/develop/ui/compose/animation/composables-modifiers#animatedvisibility) or [`animateFloatAsState`](/develop/ui/compose/animation/value-based#animate-as-state) with `Modifier.alpha()`.
          - No: Are you animating a size change?
            * Yes: [`Modifier.animateContentSize`](/develop/ui/compose/animation/composables-modifiers#animatedContentSize).
            * No: Are you animating another layout property (for example, offset or padding)?
              + Yes: See "Are the properties completely independent of each other?".
              + No: Are you animating list items?
                - Yes: [`animateItem()`](/develop/ui/compose/lists#item-animations).
      * No: Are you animating multiple properties?
        + Yes: Are the properties completely independent of each other?
          - Yes: [`animate*AsState`](/develop/ui/compose/animation/value-based#animate-as-state). For Text, use [`TextMotion.Animated`](/reference/kotlin/androidx/compose/ui/text/style/TextMotion#Animated()).
          - No: Do they need to start at the same time?
            * Yes: [`updateTransition`](/develop/ui/compose/animation/value-based#updatetransition) with `AnimatedVisibility`, `animateFloat`, `animateInt`, etc.
            * No: [`Animatable`](/develop/ui/compose/animation/value-based#animatable) with `animateTo`, called with different timings using suspend functions.
        + No: Does the animation have predefined target values?
          - Yes: [`animate*AsState`](/develop/ui/compose/animation/value-based#animate-as-state). For Text, use `TextMotion.Animated`.
          - No: Is the animation gesture-driven and the single source of truth?
            * Yes: `Animatable` with `animateTo` / `snapTo`.
            * No: Is it a one-shot animation without state management?
              + Yes: [`AnimationState`](/reference/kotlin/androidx/compose/animation/core/AnimationState) or [`animate`](/reference/kotlin/androidx/compose/animation/core/package-summary#animate(kotlin.Float,kotlin.Float,kotlin.Float,androidx.compose.animation.core.AnimationSpec,kotlin.Function2)).
              + No: Answer not here? [File a feature request](https://goo.gle/compose-feedback).

Download the [PDF version of the diagram](/static/develop/ui/compose/images/animations/compose_animation_decision_tree_v2.pdf).

[Previous

arrow\_back

Overview](/develop/ui/compose/animation/introduction)

[Next

Quick guide

arrow\_forward](/develop/ui/compose/animation/quick-guide)