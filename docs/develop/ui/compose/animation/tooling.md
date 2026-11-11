---
title: https://developer.android.com/develop/ui/compose/animation/tooling
url: https://developer.android.com/develop/ui/compose/animation/tooling
source: md.txt
---

Android Studio supports inspection of [`animate*AsState`](https://developer.android.com/develop/ui/compose/animation/value-based.md.txt#animate-as-state), [`Crossfade`](https://developer.android.com/develop/ui/compose/animation/composables-modifiers.md.txt#crossfade),
[`rememberInfiniteTransition`](https://developer.android.com/develop/ui/compose/animation/value-based.md.txt#rememberinfinitetransition), [`AnimatedContent`](https://developer.android.com/develop/ui/compose/animation/composables-modifiers.md.txt#animatedcontent),
[`updateTransition`](https://developer.android.com/develop/ui/compose/animation/value-based.md.txt#updateTransition), and [`AnimatedVisibility`](https://developer.android.com/develop/ui/compose/animation/composables-modifiers.md.txt#animatedvisibility) in
[Animation Preview](https://developer.android.com/develop/ui/compose/tooling/animation-preview.md.txt). You can do the following:

- Preview a transition frame by frame.
- Inspect values for all animations in the transition.
- Preview a transition between any initial and target state.
- Inspect and coordinate multiple animations at once.

When you start Animation Preview, you see the **Animations** pane, where you can
run any transition included in the preview. The transition, as well as each of
its animation values, is labeled with a default name. You can customize the
label by specifying the `label` parameter in the `updateTransition` and the
`AnimatedVisibility` functions. For more information, see
[Animation Preview](https://developer.android.com/develop/ui/compose/tooling/animation-preview.md.txt).
![The Animation Preview panel in Android Studio, showing a timeline of animations and their properties.](https://developer.android.com/static/develop/ui/compose/images/animation-preview-overview.png) **Figure 1.** The Animation Preview panel in Android Studio.

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Value-based animations](https://developer.android.com/develop/ui/compose/animation/value-based.md.txt)
- [Animations in Compose](https://developer.android.com/develop/ui/compose/animation/introduction)
- [Animation modifiers and composables](https://developer.android.com/develop/ui/compose/animation/composables-modifiers.md.txt)