---
title: Animation tooling support  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/animation/tooling
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Animation tooling support Stay organized with collections Save and categorize content based on your preferences.




Android Studio supports inspection of [`animate*AsState`](/develop/ui/compose/animation/value-based#animate-as-state), [`CrossFade`](/develop/ui/compose/animation/composables-modifiers#crossfade),
[`rememberInfiniteTransition`](/develop/ui/compose/animation/value-based#rememberinfinitetransition), [`AnimatedContent`](/develop/ui/compose/animation/composables-modifiers#animatedcontent),
[`updateTransition`](/develop/ui/compose/animation/value-based#updateTransition), and [`animatedVisibility`](/develop/ui/compose/animation/composables-modifiers#animatedvisibility) in
[Animation Preview](/develop/ui/compose/tooling#animations). You can do the following:

* Preview a transition frame by frame.
* Inspect values for all animations in the transition.
* Preview a transition between any initial and target state.
* Inspect and coordinate multiple animations at once.

When you start Animation Preview, you see the **Animations** pane, where you can
run any transition included in the preview. The transition, as well as each of
its animation values, is labeled with a default name. You can customize the
label by specifying the `label` parameter in the `updateTransition` and the
`AnimatedVisibility` functions. For more information, see
[Animation Preview](/develop/ui/compose/tooling/animation-preview).

![The Animation Preview panel in Android Studio, showing a timeline of animations and their properties.](/static/develop/ui/compose/images/animation-preview-overview.png)


**Figure 1.** The Animation Preview panel in Android Studio.



## Recommended for you

* Note: link text is displayed when JavaScript is off
* [Value-based animations](/develop/ui/compose/animation/value-based)
* [Animations in Compose](/develop/ui/compose/animation/introduction)
* [Animation modifiers and composables](/develop/ui/compose/animation/composables-modifiers)

[Previous

arrow\_back

Test animations](/develop/ui/compose/animation/testing)

[Next

Additional resources

arrow\_forward](/develop/ui/compose/animation/resources)