---
title: https://developer.android.com/develop/ui/compose/animation/choose-api
url: https://developer.android.com/develop/ui/compose/animation/choose-api
source: md.txt
---

The following diagram helps you decide what API to use to implement your animation.


![Flowchart describing the decision tree for choosing the appropriate animation API](https://developer.android.com/static/develop/ui/compose/images/animations/compose_animation_decision_tree_v2.jpg) **Figure 1.** Decision tree describing how to choose the appropriate animation API.

<br />

![Flowchart describing the decision tree for choosing the appropriate animation API](https://developer.android.com/static/develop/ui/compose/images/animations/compose_animation_decision_tree_v2.jpg)

Use the following decision tree to choose the most appropriate animation API for your use case:

- Is your animation art-based (that is, SVGs or images)?
  - Yes: Does it use simple SVGs (that is, an icon with micro-animations)?
    - Yes: [`AnimatedVectorDrawable`](https://developer.android.com/develop/ui/compose/animation/avd).
    - No: Third-party animation framework, for example, [`Lottie`](https://airbnb.io/lottie/).
  - No: Does the animation need to repeat infinitely?
    - Yes: [`rememberInfiniteTransition`](https://developer.android.com/develop/ui/compose/animation/value-based#rememberinfinitetransition).
    - No: Are you animating a layout?
      - Yes: Are you switching between composables with different content?
        - Yes: Are you using Navigation-Compose?
          - Yes: [`composable()`](https://developer.android.com/reference/kotlin/androidx/navigation/compose/package-summary#(androidx.navigation.NavGraphBuilder).composable(kotlin.String,kotlin.collections.List,kotlin.collections.List,kotlin.Function1,kotlin.Function1,kotlin.Function1,kotlin.Function1,kotlin.Function2)) with `enterTransition` and `exitTransition` set.
          - No: [`AnimatedContent`](https://developer.android.com/develop/ui/compose/animation/composables-modifiers#animatedcontent), [`Crossfade`](https://developer.android.com/develop/ui/compose/animation/composables-modifiers#crossfade), or [`Pager`](https://developer.android.com/develop/ui/compose/layouts/pager).
        - No: Are you animating the appearance or disappearance of content?
          - Yes: [`AnimatedVisibility`](https://developer.android.com/develop/ui/compose/animation/composables-modifiers#animatedvisibility) or [`animateFloatAsState`](https://developer.android.com/develop/ui/compose/animation/value-based#animate-as-state) with `Modifier.alpha()`.
          - No: Are you animating a size change?
            - Yes: [`Modifier.animateContentSize`](https://developer.android.com/develop/ui/compose/animation/composables-modifiers#animatedContentSize).
            - No: Are you animating another layout property (for example, offset or padding)?
              - Yes: See "Are the properties completely independent of each other?".
              - No: Are you animating list items?
                - Yes: [`animateItem()`](https://developer.android.com/develop/ui/compose/lists#item-animations).
      - No: Are you animating multiple properties?
        - Yes: Are the properties completely independent of each other?
          - Yes: [`animate*AsState`](https://developer.android.com/develop/ui/compose/animation/value-based#animate-as-state). For Text, use [`TextMotion.Animated`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/style/TextMotion#Animated()).
          - No: Do they need to start at the same time?
            - Yes: [`updateTransition`](https://developer.android.com/develop/ui/compose/animation/value-based#updatetransition) with `AnimatedVisibility`, `animateFloat`, `animateInt`, etc.
            - No: [`Animatable`](https://developer.android.com/develop/ui/compose/animation/value-based#animatable) with `animateTo`, called with different timings using suspend functions.
        - No: Does the animation have predefined target values?
          - Yes: [`animate*AsState`](https://developer.android.com/develop/ui/compose/animation/value-based#animate-as-state). For Text, use `TextMotion.Animated`.
          - No: Is the animation gesture-driven and the single source of truth?
            - Yes: `Animatable` with `animateTo` / `snapTo`.
            - No: Is it a one-shot animation without state management?
              - Yes: [`AnimationState`](https://developer.android.com/reference/kotlin/androidx/compose/animation/core/AnimationState) or [`animate`](https://developer.android.com/reference/kotlin/androidx/compose/animation/core/package-summary#animate(kotlin.Float,kotlin.Float,kotlin.Float,androidx.compose.animation.core.AnimationSpec,kotlin.Function2)).
              - No: Answer not here? [File a feature request](https://goo.gle/compose-feedback).

Download the [PDF version of the diagram](https://developer.android.com/static/develop/ui/compose/images/animations/compose_animation_decision_tree_v2.pdf).