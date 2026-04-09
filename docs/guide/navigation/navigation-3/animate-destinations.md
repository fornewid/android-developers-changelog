---
title: https://developer.android.com/guide/navigation/navigation-3/animate-destinations
url: https://developer.android.com/guide/navigation/navigation-3/animate-destinations
source: md.txt
---

[`NavDisplay`](https://developer.android.com/reference/kotlin/androidx/navigation3/ui/package-summary#NavDisplay(kotlin.collections.List,androidx.compose.ui.Modifier,androidx.compose.ui.Alignment,kotlin.Function0,kotlin.collections.List,androidx.navigation3.scene.SceneStrategy,androidx.compose.animation.SharedTransitionScope,androidx.compose.animation.SizeTransform,kotlin.Function1,kotlin.Function1,kotlin.Function2,kotlin.Function1)) provides built-in animation capabilities to create smooth
visual transitions as users navigate through your app. You can customize these
animations globally for the `NavDisplay` or at the [`Scene`](https://developer.android.com/reference/kotlin/androidx/navigation3/scene/Scene) level using
metadata.

## Understand built-in animation capabilities

`NavDisplay` uses the [`ContentTransform`](https://developer.android.com/reference/kotlin/androidx/compose/animation/ContentTransform) API to define how content animates
during navigation. `NavDisplay` automatically animates transitions between
scenes when a key derived from the class of the current scene and its `key`
property changes. When this key changes, `NavDisplay` uses the
`ContentTransform` for the type of transition---forward, back, or predictive
back---from the appropriate scene in the transition. If that `ContentTransform`
isn't defined, `NavDisplay` falls back to using its corresponding [default
transition](https://developer.android.com/guide/navigation/navigation-3/animate-destinations#override-default).

> [!NOTE]
> **Note:** If your app doesn't [create custom layouts using scenes](https://developer.android.com/guide/navigation/navigation-3/scenes#understand-scenes), `NavDisplay` defaults to using a `SinglePaneSceneStrategy`, which creates a `SinglePaneScene` for each entry on the back stack.

## Override default transitions

You can override the default animation behaviors by providing transition
parameters to `NavDisplay`.

- `transitionSpec`: This parameter defines the `ContentTransform` to apply when content is added to the back stack (i.e., when navigating forward).
- `popTransitionSpec`: This parameter defines the `ContentTransform` to apply when content is removed from the back stack (i.e., when navigating back).
- `predictivePopTransitionSpec`: This parameter defines the `ContentTransform` to apply when content is popped using a predictive back gesture.

## Override transitions at the `Scene` level

You can use [metadata](https://developer.android.com/guide/navigation/navigation-3/metadata#provide-scene) to define custom animations for individual scenes
using the following [metadata keys](https://developer.android.com/guide/navigation/navigation-3/metadata#define-keys) defined by `NavDisplay`:

- [`NavDisplay.TransitionKey`](https://developer.android.com/reference/kotlin/androidx/navigation3/ui/NavDisplay.TransitionKey): The forward navigation animation.
- [`NavDisplay.PopTransitionKey`](https://developer.android.com/reference/kotlin/androidx/navigation3/ui/NavDisplay.PopTransitionKey): The backward navigation animation.
- [`NavDisplay.PredictivePopTransitionKey`](https://developer.android.com/reference/kotlin/androidx/navigation3/ui/NavDisplay.PredictivePopTransitionKey): The predictive back animation.

When provided, these scene-level transitions are used instead of the
corresponding defaults set on the `NavDisplay`.

The following snippet demonstrates both global `NavDisplay` transitions and an
override at the individual `NavEntry` level:


```kotlin
@Serializable
data object ScreenA : NavKey

@Serializable
data object ScreenB : NavKey

@Serializable
data object ScreenC : NavKey

class AnimatedNavDisplayActivity : ComponentActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {

            Scaffold { paddingValues ->

                val backStack = rememberNavBackStack(ScreenA)

                NavDisplay(
                    backStack = backStack,
                    onBack = { backStack.removeLastOrNull() },
                    entryProvider = entryProvider {
                        entry<ScreenA> {
                            ContentOrange("This is Screen A") {
                                Button(onClick = { backStack.add(ScreenB) }) {
                                    Text("Go to Screen B")
                                }
                            }
                        }
                        entry<ScreenB> {
                            ContentMauve("This is Screen B") {
                                Button(onClick = { backStack.add(ScreenC) }) {
                                    Text("Go to Screen C")
                                }
                            }
                        }
                        entry<ScreenC>(
                            metadata = metadata {
                                put(NavDisplay.TransitionKey) {
                                    // Slide new content up, keeping the old content in place underneath
                                    slideInVertically(
                                        initialOffsetY = { it },
                                        animationSpec = tween(1000)
                                    ) togetherWith ExitTransition.KeepUntilTransitionsFinished
                                }
                                put(NavDisplay.PopTransitionKey) {
                                    // Slide old content down, revealing the new content in place underneath
                                    EnterTransition.None togetherWith
                                            slideOutVertically(
                                                targetOffsetY = { it },
                                                animationSpec = tween(1000)
                                            )
                                }
                                put(NavDisplay.PredictivePopTransitionKey) {
                                    // Slide old content down, revealing the new content in place underneath
                                    EnterTransition.None togetherWith
                                            slideOutVertically(
                                                targetOffsetY = { it },
                                                animationSpec = tween(1000)
                                            )
                                }
                            }
                        ) {
                            ContentGreen("This is Screen C")
                        }
                    },
                    transitionSpec = {
                        // Slide in from right when navigating forward
                        slideInHorizontally(initialOffsetX = { it }) togetherWith
                            slideOutHorizontally(targetOffsetX = { -it })
                    },
                    popTransitionSpec = {
                        // Slide in from left when navigating back
                        slideInHorizontally(initialOffsetX = { -it }) togetherWith
                            slideOutHorizontally(targetOffsetX = { it })
                    },
                    predictivePopTransitionSpec = {
                        // Slide in from left when navigating back
                        slideInHorizontally(initialOffsetX = { -it }) togetherWith
                            slideOutHorizontally(targetOffsetX = { it })
                    },
                    modifier = Modifier.padding(paddingValues)
                )
            }
        }
    }
}
```

<br />

**Figure 1**. App with custom animations.

## Transition nav entries between scenes

In apps that [create custom layouts using scenes](https://developer.android.com/guide/navigation/navigation-3/scenes#understand-scenes), it's possible for a
`NavEntry` to be included in the `entries` property of both scenes during a
transition. Internally, `NavDisplay` verifies that every entry is displayed in
at most one scene at any time, which can result in jumpy transitions when the
scene rendering a `NavEntry` changes. To smoothly animate entries between
scenes, you can wrap your `NavDisplay` in a [`SharedTransitionLayout`](https://developer.android.com/reference/kotlin/androidx/compose/animation/SharedTransitionLayout) and
provide the [`SharedTransitionScope`](https://developer.android.com/reference/kotlin/androidx/compose/animation/SharedTransitionScope) to the `NavDisplay` as shown in the
following example:


```kotlin
SharedTransitionLayout {
    NavDisplay(
        // ...
        sharedTransitionScope = this
    )
}
```

<br />