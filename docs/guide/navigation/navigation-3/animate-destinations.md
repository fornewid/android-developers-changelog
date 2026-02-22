---
title: https://developer.android.com/guide/navigation/navigation-3/animate-destinations
url: https://developer.android.com/guide/navigation/navigation-3/animate-destinations
source: md.txt
---

[`NavDisplay`](https://developer.android.com/reference/kotlin/androidx/navigation3/ui/package-summary#NavDisplay(kotlin.collections.List,androidx.compose.ui.Modifier,androidx.compose.ui.Alignment,kotlin.Function0,kotlin.collections.List,androidx.navigation3.scene.SceneStrategy,androidx.compose.animation.SharedTransitionScope,androidx.compose.animation.SizeTransform,kotlin.Function1,kotlin.Function1,kotlin.Function2,kotlin.Function1)) provides built-in animation capabilities to create smooth
visual transitions as users navigate through your app. You can customize these
animations globally for the `NavDisplay` or on a per-`NavEntry` basis using
metadata.

## Override default transitions

`NavDisplay` uses `ContentTransform`s to define how content animates during
navigation. You can override the default animation behaviors by providing
transition parameters to `NavDisplay`.

- `transitionSpec`: This parameter defines the `ContentTransform` to apply when content is added to the back stack (i.e., when navigating forward).
- `popTransitionSpec`: This parameter defines the `ContentTransform` to apply when content is removed from the back stack (i.e., when navigating back).
- `predictivePopTransitionSpec`: This parameter defines the `ContentTransform` to apply when content is popped using a predictive back gesture.

## Override transitions at the individual `NavEntry` level

You can also define custom animations for specific [`NavEntry`s](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/NavEntry) using their
metadata. `NavDisplay` recognizes special metadata keys to apply per-entry
transitions:

- `NavDisplay.transitionSpec`: Use this helper function to define the forward navigation animation.
- `NavDisplay.popTransitionSpec`: Use this helper function to define the backward navigation animation for a specific `NavEntry`.
- `NavDisplay.predictivePopTransitionSpec`: Use this helper function to define the animation for predictive back gestures for a specific `NavEntry`.

These per-entry metadata transitions override the `NavDisplay`'s global
transitions of the same name.

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
                            metadata = NavDisplay.transitionSpec {
                                // Slide new content up, keeping the old content in place underneath
                                slideInVertically(
                                    initialOffsetY = { it },
                                    animationSpec = tween(1000)
                                ) togetherWith ExitTransition.KeepUntilTransitionsFinished
                            } + NavDisplay.popTransitionSpec {
                                // Slide old content down, revealing the new content in place underneath
                                EnterTransition.None togetherWith
                                    slideOutVertically(
                                        targetOffsetY = { it },
                                        animationSpec = tween(1000)
                                    )
                            } + NavDisplay.predictivePopTransitionSpec {
                                // Slide old content down, revealing the new content in place underneath
                                EnterTransition.None togetherWith
                                    slideOutVertically(
                                        targetOffsetY = { it },
                                        animationSpec = tween(1000)
                                    )
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