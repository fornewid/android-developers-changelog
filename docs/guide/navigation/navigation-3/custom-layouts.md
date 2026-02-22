---
title: https://developer.android.com/guide/navigation/navigation-3/custom-layouts
url: https://developer.android.com/guide/navigation/navigation-3/custom-layouts
source: md.txt
---

Navigation 3 introduces a powerful and flexible system for managing your app's
UI flow through **Scenes**. Scenes allow you to create highly customized
layouts, adapt to different screen sizes, and manage complex multi-pane
experiences seamlessly.

## Understand Scenes

In Navigation 3, a [`Scene`](https://developer.android.com/reference/kotlin/androidx/navigation3/scene/Scene) is the fundamental unit that renders one or more
`NavEntry` instances. Think of a `Scene` as a distinct visual state or section
of your UI that can contain and manage the display of content from your back
stack.

Each `Scene` instance is uniquely identified by its [`key`](https://developer.android.com/reference/kotlin/androidx/navigation3/scene/Scene#key()) and the class of
the `Scene` itself. This unique identifier is crucial because it drives the
top-level animation when the `Scene` changes.

The `Scene` interface has the following properties:

- `key: Any`: A unique identifier for this specific `Scene` instance. This key, combined with the `Scene`'s class, ensures distinctness, primarily for animation purposes.
- `entries: List<NavEntry<T>>`: This is a list of `NavEntry` objects that the `Scene` is responsible for displaying. Importantly, if the same `NavEntry` is displayed in multiple `Scenes` during a transition (e.g., in a shared element transition), its content will only be rendered by the most recent target `Scene` that is displaying it.
- `previousEntries: List<NavEntry<T>>`: This property defines the `NavEntry`s that would result if a "back" action occurs from the current `Scene`. It's essential for calculating the proper predictive back state, allowing the `NavDisplay` to anticipate and transition to the correct previous state, which may be a Scene with a different class and/or key.
- `content: @Composable () -> Unit`: This is the composable function where you define how the `Scene` renders its `entries` and any surrounding UI elements specific to that `Scene`.

## Understand scene strategies

A [`SceneStrategy`](https://developer.android.com/reference/kotlin/androidx/navigation3/scene/SceneStrategy) is the mechanism that determines how a given list of
`NavEntry`s from the back stack should be arranged and transitioned into a
`Scene`. Essentially, when presented with the current back stack entries, a
`SceneStrategy` asks itself two key questions:

1. **Can I create a `Scene` from these entries?** If the `SceneStrategy` determines it can handle the given `NavEntry`s and form a meaningful `Scene` (e.g., a dialog or a multi-pane layout), it proceeds. Otherwise, it returns `null`, giving other strategies a chance to create a `Scene`.
2. **If so, how should I arrange those entries into the `Scene?`** Once a `SceneStrategy` commits to handling the entries, it takes on the responsibility of constructing a `Scene` and defining how the specified `NavEntry`s will be displayed within that `Scene`.

The core of a `SceneStrategy` is its [`calculateScene`](https://developer.android.com/reference/kotlin/androidx/navigation3/scene/SceneStrategy#calculateScene(kotlin.collections.List)) method:


```kotlin
@Composable
public fun calculateScene(
    entries: List<NavEntry<T>>,
    onBack: (count: Int) -> Unit,
): Scene<T>?  
https://github.com/android/snippets/blob/7a4ea7786ed5b5716f69abd3291976b01a6017d0/compose/snippets/src/main/java/com/example/compose/snippets/navigation3/scenes/ScenesSnippets.kt#L44-L48
```

<br />

This method is an extension function on a `SceneStrategyScope` that takes the
current `List<NavEntry<T>>` from the back stack. It should return a `Scene<T>`
if it can successfully form one from the provided entries, or `null` if it
cannot.

The `SceneStrategyScope` is responsible for maintaining any optional arguments
that the `SceneStrategy` might need, such as an `onBack` callback.

`SceneStrategy` also provides a convenient `then` infix function, allowing
you to chain multiple strategies together. This creates a flexible
decision-making pipeline where each strategy can attempt to calculate a `Scene`,
and if it can't, it delegates to the next one in the chain.

## How Scenes and scene strategies work together

The `NavDisplay` is the central composable that observes your back stack and
uses a `SceneStrategy` to determine and render the appropriate `Scene`.

The `NavDisplay's sceneStrategy` parameter expects a `SceneStrategy` that is
responsible for calculating the `Scene` to display. If no `Scene` is calculated
by the provided strategy (or chain of strategies), `NavDisplay` automatically
falls back to using a `SinglePaneSceneStrategy` by default.

Here's a breakdown of the interaction:

- When you add or remove keys from your back stack (e.g., using `backStack.add()` or `backStack.removeLastOrNull()`), the `NavDisplay` observes these changes.
- The `NavDisplay` passes the current list of `NavEntrys` (derived from the back stack keys) to the configured `SceneStrategy's calculateScene` method.
- If the `SceneStrategy` successfully returns a `Scene`, the `NavDisplay` then renders the `content` of that `Scene`. The `NavDisplay` also manages animations and predictive back based on the `Scene`'s properties.

## Example: Single pane layout (default behavior)

The simplest custom layout you can have is a single-pane display, which is the
default behavior if no other `SceneStrategy` takes precedence.


```kotlin
data class SinglePaneScene<T : Any>(
    override val key: Any,
    val entry: NavEntry<T>,
    override val previousEntries: List<NavEntry<T>>,
) : Scene<T> {
    override val entries: List<NavEntry<T>> = listOf(entry)
    override val content: @Composable () -> Unit = { entry.Content() }
}

/**
 * A [SceneStrategy] that always creates a 1-entry [Scene] simply displaying the last entry in the
 * list.
 */
public class SinglePaneSceneStrategy<T : Any> : SceneStrategy<T> {
    override fun SceneStrategyScope<T>.calculateScene(entries: List<NavEntry<T>>): Scene<T>? =
        SinglePaneScene(
            key = entries.last().contentKey,
            entry = entries.last(),
            previousEntries = entries.dropLast(1)
        )
}
```

<br />

## Example: Basic list-detail layout (custom Scene and strategy)

This example demonstrates how to create a simple list-detail layout that is
activated based on two conditions:

1. The **window width** is sufficiently wide to support two panes (i.e., at least `WIDTH_DP_MEDIUM_LOWER_BOUND`).
2. The back stack contains entries that have declared their support for being displayed in a list-detail layout using specific metadata.

The following snippet is the source code for `ListDetailScene.kt` and it
contains both `ListDetailScene` and `ListDetailSceneStrategy`:


```kotlin
// --- ListDetailScene ---
/**
 * A [Scene] that displays a list and a detail [NavEntry] side-by-side in a 40/60 split.
 *
 */
class ListDetailScene<T : Any>(
    override val key: Any,
    override val previousEntries: List<NavEntry<T>>,
    val listEntry: NavEntry<T>,
    val detailEntry: NavEntry<T>,
) : Scene<T> {
    override val entries: List<NavEntry<T>> = listOf(listEntry, detailEntry)
    override val content: @Composable (() -> Unit) = {
        Row(modifier = Modifier.fillMaxSize()) {
            Column(modifier = Modifier.weight(0.4f)) {
                listEntry.Content()
            }
            Column(modifier = Modifier.weight(0.6f)) {
                detailEntry.Content()
            }
        }
    }
}

@Composable
fun <T : Any> rememberListDetailSceneStrategy(): ListDetailSceneStrategy<T> {
    val windowSizeClass = currentWindowAdaptiveInfo().windowSizeClass

    return remember(windowSizeClass) {
        ListDetailSceneStrategy(windowSizeClass)
    }
}

// --- ListDetailSceneStrategy ---
/**
 * A [SceneStrategy] that returns a [ListDetailScene] if the window is wide enough, the last item
 * is the backstack is a detail, and before it, at any point in the backstack is a list.
 */
class ListDetailSceneStrategy<T : Any>(val windowSizeClass: WindowSizeClass) : SceneStrategy<T> {

    override fun SceneStrategyScope<T>.calculateScene(entries: List<NavEntry<T>>): Scene<T>? {

        if (!windowSizeClass.isWidthAtLeastBreakpoint(WIDTH_DP_MEDIUM_LOWER_BOUND)) {
            return null
        }

        val detailEntry =
            entries.lastOrNull()?.takeIf { it.metadata.containsKey(DETAIL_KEY) } ?: return null
        val listEntry = entries.findLast { it.metadata.containsKey(LIST_KEY) } ?: return null

        // We use the list's contentKey to uniquely identify the scene.
        // This allows the detail panes to be displayed instantly through recomposition, rather than
        // having NavDisplay animate the whole scene out when the selected detail item changes.
        val sceneKey = listEntry.contentKey

        return ListDetailScene(
            key = sceneKey,
            previousEntries = entries.dropLast(1),
            listEntry = listEntry,
            detailEntry = detailEntry
        )
    }

    companion object {
        internal const val LIST_KEY = "ListDetailScene-List"
        internal const val DETAIL_KEY = "ListDetailScene-Detail"

        /**
         * Helper function to add metadata to a [NavEntry] indicating it can be displayed
         * as a list in the [ListDetailScene].
         */
        fun listPane() = mapOf(LIST_KEY to true)

        /**
         * Helper function to add metadata to a [NavEntry] indicating it can be displayed
         * as a list in the [ListDetailScene].
         */
        fun detailPane() = mapOf(DETAIL_KEY to true)
    }
}
```

<br />

To use this `ListDetailSceneStrategy` in your `NavDisplay`, modify your
`entryProvider` calls to include `ListDetailScene.listPane()` metadata for the
entry you intend to show as a **list** layout, and the
`ListDetailScene.detailPane()` for the entry you want to show as **detail**
layout. Then, provide `ListDetailSceneStrategy()` as your `sceneStrategy`,
relying on the default fallback for single-pane scenarios:


```kotlin
// Define your navigation keys
@Serializable
data object ConversationList : NavKey

@Serializable
data class ConversationDetail(val id: String) : NavKey

@Composable
fun MyAppContent() {
    val backStack = rememberNavBackStack(ConversationList)
    val listDetailStrategy = rememberListDetailSceneStrategy<NavKey>()

    NavDisplay(
        backStack = backStack,
        onBack = { backStack.removeLastOrNull() },
        sceneStrategy = listDetailStrategy,
        entryProvider = entryProvider {
            entry<ConversationList>(
                metadata = ListDetailSceneStrategy.listPane()
            ) {
                Column(modifier = Modifier.fillMaxSize()) {
                    Text(text = "I'm a Conversation List")
                    Button(onClick = { backStack.addDetail(ConversationDetail("123")) }) {
                        Text(text = "Open detail")
                    }
                }
            }
            entry<ConversationDetail>(
                metadata = ListDetailSceneStrategy.detailPane()
            ) {
                Text(text = "I'm a Conversation Detail")
            }
        }
    )
}

private fun NavBackStack<NavKey>.addDetail(detailRoute: ConversationDetail) {

    // Remove any existing detail routes, then add the new detail route
    removeIf { it is ConversationDetail }
    add(detailRoute)
}
```

<br />

If you don't want to create your own list-detail scene, you can use the
Material list-detail scene, which comes with sensible details and the
support for placeholders, as showcased in the next section.

## Display list-detail content in a Material Adaptive Scene

For the **list-detail use case** , the
`androidx.compose.material3.adaptive:adaptive-navigation3` artifact provides a
`ListDetailSceneStrategy` that creates a list-detail `Scene`. This `Scene`
automatically handles complex multi-pane arrangements (list, detail, and extra
panes) and adapts them based on window size and device state.

To create a Material list-detail `Scene`, follow these steps:

1. **Add the dependency** : Include `androidx.compose.material3.adaptive:adaptive-navigation3` in your project's `build.gradle.kts` file.
2. **Define your entries with `ListDetailSceneStrategy` metadata** : Use `listPane(), detailPane()`, and `extraPane()` to mark your `NavEntrys` for appropriate pane display. The `listPane()` helper also allows you to specify a `detailPlaceholder` when no item is selected.
3. **Use `rememberListDetailSceneStrategy`** (): This composable function provides a pre-configured `ListDetailSceneStrategy` that can be used by a `NavDisplay`.

The following snippet is a sample `Activity` demonstrating the usage of
`ListDetailSceneStrategy`:


```kotlin
@Serializable
object ProductList : NavKey

@Serializable
data class ProductDetail(val id: String) : NavKey

@Serializable
data object Profile : NavKey

class MaterialListDetailActivity : ComponentActivity() {

    @OptIn(ExperimentalMaterial3AdaptiveApi::class)
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        setContent {
            Scaffold { paddingValues ->
                val backStack = rememberNavBackStack(ProductList)
                val listDetailStrategy = rememberListDetailSceneStrategy<NavKey>()

                NavDisplay(
                    backStack = backStack,
                    modifier = Modifier.padding(paddingValues),
                    onBack = { backStack.removeLastOrNull() },
                    sceneStrategy = listDetailStrategy,
                    entryProvider = entryProvider {
                        entry<ProductList>(
                            metadata = ListDetailSceneStrategy.listPane(
                                detailPlaceholder = {
                                    ContentYellow("Choose a product from the list")
                                }
                            )
                        ) {
                            ContentRed("Welcome to Nav3") {
                                Button(onClick = {
                                    backStack.add(ProductDetail("ABC"))
                                }) {
                                    Text("View product")
                                }
                            }
                        }
                        entry<ProductDetail>(
                            metadata = ListDetailSceneStrategy.detailPane()
                        ) { product ->
                            ContentBlue("Product ${product.id} ", Modifier.background(PastelBlue)) {
                                Column(horizontalAlignment = Alignment.CenterHorizontally) {
                                    Button(onClick = {
                                        backStack.add(Profile)
                                    }) {
                                        Text("View profile")
                                    }
                                }
                            }
                        }
                        entry<Profile>(
                            metadata = ListDetailSceneStrategy.extraPane()
                        ) {
                            ContentGreen("Profile")
                        }
                    }
                )
            }
        }
    }
}
```

<br />

**Figure 1**. Example content running in Material list-detail Scene.