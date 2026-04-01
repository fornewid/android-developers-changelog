---
title: https://developer.android.com/develop/ui/compose/animation/shared-elements/customize
url: https://developer.android.com/develop/ui/compose/animation/shared-elements/customize
source: md.txt
---

To customize how the shared element transition animation runs, there are a few
parameters that can be used to change how the shared elements transition.

## Animation spec

To change the animation spec used for the size and position movement, you can
specify a different `boundsTransform` parameter on `Modifier.sharedElement()`.
This provides the initial `Rect` position and target `Rect` position.

For example, to make the text in the preceding example to move with an arc
motion, specify the `boundsTransform` parameter to use a [`keyframes`](https://developer.android.com/develop/ui/compose/animation/customize#animationspec) spec:


```kotlin
val textBoundsTransform = BoundsTransform { initialBounds, targetBounds ->
    keyframes {
        durationMillis = boundsAnimationDurationMillis
        initialBounds at 0 using ArcMode.ArcBelow using FastOutSlowInEasing
        targetBounds at boundsAnimationDurationMillis
    }
}
Text(
    "Cupcake", fontSize = 28.sp,
    modifier = Modifier.sharedBounds(
        rememberSharedContentState(key = "title"),
        animatedVisibilityScope = animatedVisibilityScope,
        boundsTransform = textBoundsTransform
    )
)
```

<br />

You can use any `AnimationSpec`. This example uses a `keyframes` spec.
**Figure 1.** Example showing different `boundsTransform` parameters

## Resize mode

When animating between two shared bounds, you can set the `resizeMode` parameter
to either `RemeasureToBounds` or `ScaleToBounds`. This parameter determines how
the shared element transitions between the two states. `ScaleToBounds` first
measures the child layout with the lookahead (or target) constraints. Then, the
child's stable layout is scaled to fit in the shared bounds.
`ScaleToBounds` can be thought of as a "graphical scale" between the states.

In contrast, `RemeasureToBounds` re-measures and re-layouts the child layout of
`sharedBounds` with animated fixed constraints based on the target size. The
re-measurement is triggered by the bounds size change, which could potentially
be every frame.

For `Text` composables, `ScaleToBounds` is recommended, as it avoids relayout
and reflowing of text onto different lines. `RemeasureToBounds` is recommended
for bounds that are different aspect ratios, and if you'd like fluid continuity
between the two shared elements.

The difference between the two resize modes can be seen in the examples that follow:

| `ScaleToBounds` | `RemeasureToBounds` |
|---|---|
|   |   |

## Dynamically enable and disable shared elements

By default, `sharedElement()` and `sharedBounds()` are configured to animate the
layout changes whenever a matching key is found in the target state. However,
you may want to disable this animation dynamically based on specific conditions,
such as the direction of navigation or the current UI state.

To control whether the shared element transition occurs, you can customize the
`SharedContentConfig` passed to `rememberSharedContentState()`. The `isEnabled`
property determines if the shared element is active.

The following example demonstrates how to define a configuration that only
enables the shared transition when navigating between specific screens (e.g.,
only from A to B), while disabling it for others.


```kotlin
SharedTransitionLayout {
    val transition = updateTransition(currentState)
    transition.AnimatedContent { targetState ->
        // Create the configuration that depends on state changing.
        fun animationConfig() : SharedTransitionScope.SharedContentConfig {
            return object : SharedTransitionScope.SharedContentConfig {
                override val SharedTransitionScope.SharedContentState.isEnabled: Boolean
                    // For this example, we only enable the transition in one direction
                    // from A -> B and not the other way around.
                    get() =
                        transition.currentState == "A" && transition.targetState == "B"
            }
        }
        when (targetState) {
            "A" -> Box(
                modifier = Modifier
                    .sharedElement(
                        rememberSharedContentState(
                            key = "shared_box",
                            config = animationConfig()
                        ),
                        animatedVisibilityScope = this
                    )
                    // ...
            ) {
                // Your content
            }
            "B" -> {
                Box(
                    modifier = Modifier
                        .sharedElement(
                            rememberSharedContentState(
                                key = "shared_box",
                                config = animationConfig()
                            ),
                            animatedVisibilityScope = this
                        )
                        // ...
                ) {
                    // Your content
                }
            }
        }
    }
}
```

<br />

By default, if a shared element is disabled during an ongoing animation, it
still completes the current in-progress animation to prevent accidentally
removing in-flight animations. If you need to remove the element whilst the
animation is in progress, you can override
`shouldKeepEnabledForOngoingAnimation` in the `SharedContentConfig` interface to
return false.

## Skip to final layout

By default, when transitioning between two layouts, the layout size animates
between its start and final state. This may be undesirable behavior when
animating content such as text.

The following example illustrates the description text "Lorem Ipsum" entering
the screen in two different ways. In the first example, the text reflows as it
enters as the container grows in size. In the second example the text does not
reflow as it grows. Adding `Modifier.skipToLookaheadSize()` prevents the reflow
as it grows.

| No `Modifier.skipToLookaheadSize()` - notice the "Lorem Ipsum" text reflowing | `Modifier.skipToLookaheadSize()` - notice the "Lorem Ipsum" text keeps its final state at the start of the animation |
|---|---|
|   |   |

## Clip and overlays

In order for shared elements to share between different composables,
**the rendering of the composable is elevated** into a layer overlay when the
transition is started to its match in the destination. The effect of this is that
it'll escape the parent's bounds and its layer transformations (for example, the
alpha and scale).

It will render on top of other non-shared UI elements. Once the transition is
finished, the element will be dropped from the overlay to its own `DrawScope`.

> [!IMPORTANT]
> **Important:** In order to avoid the shared element fading in or out with its parents as it transitions to the target state, the shared element is rendered into the `SharedTransitionScope` overlay when a match is found.

To clip a shared element to a shape, use the standard `Modifier.clip()`
function. Place it after the `sharedElement()`:


```kotlin
Image(
    painter = painterResource(id = R.drawable.cupcake),
    contentDescription = "Cupcake",
    modifier = Modifier
        .size(100.dp)
        .sharedElement(
            rememberSharedContentState(key = "image"),
            animatedVisibilityScope = this@AnimatedContent
        )
        .clip(RoundedCornerShape(16.dp)),
    contentScale = ContentScale.Crop
)
```

<br />

If you need to ensure that a shared element never renders outside of a parent
container, you can set `clipInOverlayDuringTransition` on `sharedElement()`. By
default, for nested shared bounds, `clipInOverlayDuringTransition` uses the clip
path from the parent `sharedBounds()`.

To support keeping specific UI elements, such as a bottom bar or floating action
button, always on top during a shared element transition, use
[`Modifier.renderInSharedTransitionScopeOverlay()`](https://developer.android.com/reference/kotlin/androidx/compose/animation/SharedTransitionScope#(androidx.compose.ui.Modifier).renderInSharedTransitionScopeOverlay(kotlin.Function0,kotlin.Float,kotlin.Function2)). By default, this
modifier keeps the content in the overlay during the time when the shared
transition is active.

For example, in Jetsnack, the `BottomAppBar` needs to be placed on top of the
shared element until such time as the screen is not visible. Adding the modifier
onto the composable keeps it elevated.

| Without `Modifier.renderInSharedTransitionScopeOverlay()` | With `Modifier.renderInSharedTransitionScopeOverlay()` |
|---|---|
|   |   |

You might want your non-shared composable to animate away as well as
remain on top of the other composables before the transition. In such cases, use
`renderInSharedTransitionScopeOverlay().animateEnterExit()` to animate the
composable out as the shared element transition runs:


```kotlin
JetsnackBottomBar(
    modifier = Modifier
        .renderInSharedTransitionScopeOverlay(
            zIndexInOverlay = 1f,
        )
        .animateEnterExit(
            enter = fadeIn() + slideInVertically {
                it
            },
            exit = fadeOut() + slideOutVertically {
                it
            }
        )
)
```

<br />

**Figure 2.** Bottom app bar sliding in and out as the animation transitions.

In the rare case that you'd like your shared element to not render in an
overlay, you can set the `renderInOverlayDuringTransition` on `sharedElement()`
to false.

## Notify sibling layouts of changes to shared element size

By default, `sharedBounds()` and `sharedElement()` don't notify the parent
container of any size changes as the layout transitions.

In order to propagate size changes to the parent container as it transitions,
change the `placeholderSize` parameter to `PlaceholderSize.AnimatedSize`. Doing
so causes the item to grow or shrink. All other items in the layout respond to
the change.

| `PlaceholderSize.ContentSize` (default) | `PlaceholderSize.AnimatedSize` (Notice how the other items in the list move down in response to the one item growing) |
|---|---|
|   |   |