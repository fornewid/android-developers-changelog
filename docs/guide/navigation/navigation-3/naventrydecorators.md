---
title: https://developer.android.com/guide/navigation/navigation-3/naventrydecorators
url: https://developer.android.com/guide/navigation/navigation-3/naventrydecorators
source: md.txt
---

You can provide extra information or apply the same logic to
destinations using the [`NavEntryDecorator`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/NavEntryDecorator) class. This class wraps each
[`NavEntry`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/NavEntry) in a back stack with a composable function. Put another way,
it *decorates* the entry's content.

## Create a custom decorator

To create a decorator, extend the [`NavEntryDecorator`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/NavEntryDecorator) class and override
the following methods:

- `decorate` - A composable lambda that is called for each `NavEntry` in your back stack. It receives the `NavEntry` as a parameter. This lets you to create state objects that are keyed to the entry's `contentKey`. You can use `CompositionLocalProvider` to provide dependencies to the entry's content. You can also surround the content with a composable function, or trigger side-effects. You should always call `entry.Content()` inside this method.
- `onPop` - A callback that is invoked when a `NavEntry` has been removed from the back stack and has left the composition. It receives the `contentKey` of the removed entry. Use the `contentKey` to identify and clean up any state associated with that entry.

The following example extends the `NavEntryDecorator` class to create a custom
decorator.


```kotlin
// import androidx.navigation3.runtime.NavEntryDecorator
class CustomNavEntryDecorator<T : Any> : NavEntryDecorator<T>(
    decorate = { entry ->
        Log.d("CustomNavEntryDecorator", "entry with ${entry.contentKey} entered composition and was decorated")
        entry.Content()
    },
    onPop = { contentKey -> Log.d("CustomNavEntryDecorator", "entry with $contentKey was popped") }
)
```

<br />

If your decorator needs access to state, create a composable function that
creates that state then use it to construct the decorator. For an example
implementation, see the source code for
[`rememberSaveableStateHolderNavEntryDecorator`](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:navigation3/navigation3-runtime/src/commonMain/kotlin/androidx/navigation3/runtime/SaveableStateHolderNavEntryDecorator.kt;l=33?q=rememberSaveableStateHolderNavEntryDecorator&ss=androidx/platform/frameworks/support:navigation3/navigation3-runtime/src/). This creates
the state - a `SaveableStateHolder` - and uses it to construct the decorator.

## Decorate a back stack

Once you've created your `NavEntryDecorator`, decorate the entries in your
back stack in one of two ways:

- Use [`rememberDecoratedNavEntries`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/package-summary#rememberDecoratedNavEntries(kotlin.collections.List,kotlin.collections.List)). This function is useful when you have multiple back stacks, each with its own set of decorators (see [this code recipe](https://github.com/android/nav3-recipes/tree/main/app/src/main/java/com/example/nav3recipes/multiplestacks) for more details). The function returns a decorated list of `NavEntry`s that you can use with [`NavDisplay`](https://developer.android.com/reference/kotlin/androidx/navigation3/ui/package-summary#NavDisplay(kotlin.collections.List,androidx.compose.ui.Modifier,androidx.compose.ui.Alignment,androidx.navigation3.scene.SceneStrategy,androidx.compose.animation.SharedTransitionScope,androidx.compose.animation.SizeTransform,kotlin.Function1,kotlin.Function1,kotlin.Function2,kotlin.Function0)).
- Supply your decorator directly to `NavDisplay` using the `entryDecorators` parameter. `NavDisplay` calls `rememberDecoratedNavEntries` under the hood and displays the decorated entries.

### Include the default decorator

Navigation 3 includes a default decorator named
`SaveableStateHolderNavEntryDecorator` that enables a `NavEntry`'s state to
be retained through configuration changes and process death. It wraps
`NavEntry` content with a `SaveableStateProvider`, which enables
`rememberSaveable` calls inside the `NavEntry` content to function correctly.

Unless your decorator is providing a `SaveableStateProvider`, you should
include `SaveableStateHolderNavEntryDecorator` as the first decorator in your
list of supplied decorators. It is created using
`rememberSaveableStateHolderNavEntryDecorator`.

For example:


```kotlin
// import androidx.navigation3.runtime.rememberSaveableStateHolderNavEntryDecorator
NavDisplay(
    entryDecorators = listOf(
        rememberSaveableStateHolderNavEntryDecorator(),
        remember { CustomNavEntryDecorator() }
    ),
    // ...
)
```

<br />

## When to use a decorator

Use a decorator to:

- Create a dependency for every `NavEntry` in a back stack. For example, the [`ViewModelStoreNavEntryDecorator`](https://developer.android.com/guide/navigation/navigation-3/save-state#scoping-viewmodels) creates a `ViewModelStore` for every `NavEntry`.
- Scope an object to multiple `NavEntry`s. For example, to share a `ViewModel` between multiple entries.
- Perform the same action for multiple `NavEntry`s. For example, to perform logging, debugging or tracing operations for each entry.
- Wrap `NavEntry`s with the same composable function.
- Clean up state associated with `NavEntry`s. For example, when an entry is removed from the back stack the [`ViewModelStoreNavEntryDecorator`](https://developer.android.com/guide/navigation/navigation-3/save-state#scoping-viewmodels) clears its associated `ViewModelStore`.

Don't use a decorator to:

- Pass a dependency to a single `NavEntry`.
- Provide dependencies whose scope is broader than the back stack.

In both these cases, pass the dependency directly when creating the `NavEntry`
instead.

For more code examples, see [`NavEntryDecorator`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/NavEntryDecorator).