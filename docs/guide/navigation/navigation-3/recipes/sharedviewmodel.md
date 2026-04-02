---
title: App architecture  |  Android Developers
url: https://developer.android.com/guide/navigation/navigation-3/recipes/sharedviewmodel
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [App architecture](https://developer.android.com/topic/architecture/intro)

Stay organized with collections

Save and categorize content based on your preferences.



# Shared ViewModel Recipe

This recipe demonstrates how to share a `ViewModel` between different screens (entries) in Navigation 3 using a custom `NavEntryDecorator`.

## How it works

This example defines three screens:

* `ParentScreen`: Displays a button that increments a counter, the counter state is held in a `CounterViewModel`.
* `ChildScreen`: A sub-screen that can update the `ParentScreen`'s counter state.
* `StandaloneScreen`: An independent screen with its own isolated state.

### `SharedViewModelStoreNavEntryDecorator`

The core of this recipe is the `SharedViewModelStoreNavEntryDecorator`. This decorator manages `ViewModelStore`s for navigation entries. It allows an entry to specify a "parent" entry whose `ViewModelStore` it should share.

In `SharedViewModelActivity.kt`, the `NavDisplay` is configured with this decorator:

```
entryDecorators = listOf(
    rememberSaveableStateHolderNavEntryDecorator(),
    rememberSharedViewModelStoreNavEntryDecorator(),
)
```

### Sharing the ViewModel

To enable sharing, the `ChildScreen` entry explicitly defines its parent using metadata:

```
entry<ChildScreen>(
    metadata = SharedViewModelStoreNavEntryDecorator.parent(
        ParentScreen.toContentKey()
    )
) {
    // ...
}
```

The `toContentKey()` extension function is used to standardize how the parent `NavEntry`'s `contentKey` is specified, both when defining the parent and when referenced in metadata by the child.

When `ChildScreen` requests a `CounterViewModel`:

```
val parentViewModel = viewModel(modelClass = CounterViewModel::class)
```

The decorator ensures it receives the **same instance** that `ParentScreen` is using, because it's using the `ParentScreen`'s `ViewModelStore`.

In contrast, `StandaloneScreen` does not define a parent, so it gets its own fresh `ViewModelStore` and a new instance of `CounterViewModel`.

[![](/static/images/picto-icons/code.svg)

Explore

View the full recipe on GitHub.

arrow\_forward](https://github.com/android/nav3-recipes/tree/main/app/src/main/java/com/example/nav3recipes/sharedviewmodel)

```
/*
 * Copyright 2025 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.example.nav3recipes.sharedviewmodel

import androidx.compose.runtime.Composable
import androidx.compose.runtime.CompositionLocalProvider
import androidx.compose.runtime.remember
import androidx.compose.runtime.rememberUpdatedState
import androidx.compose.runtime.staticCompositionLocalOf
import androidx.lifecycle.HasDefaultViewModelProviderFactory
import androidx.lifecycle.Lifecycle
import androidx.lifecycle.SAVED_STATE_REGISTRY_OWNER_KEY
import androidx.lifecycle.SavedStateViewModelFactory
import androidx.lifecycle.VIEW_MODEL_STORE_OWNER_KEY
import androidx.lifecycle.ViewModel
import androidx.lifecycle.ViewModelProvider
import androidx.lifecycle.ViewModelStore
import androidx.lifecycle.ViewModelStoreOwner
import androidx.lifecycle.enableSavedStateHandles
import androidx.lifecycle.viewmodel.CreationExtras
import androidx.lifecycle.viewmodel.MutableCreationExtras
import androidx.lifecycle.viewmodel.compose.LocalViewModelStoreOwner
import androidx.lifecycle.viewmodel.initializer
import androidx.lifecycle.viewmodel.viewModelFactory
import androidx.navigation3.runtime.NavEntry
import androidx.navigation3.runtime.NavEntryDecorator
import androidx.navigation3.runtime.NavMetadataKey
import androidx.navigation3.runtime.get
import androidx.navigation3.runtime.metadata
import androidx.savedstate.SavedStateRegistryOwner
import androidx.savedstate.compose.LocalSavedStateRegistryOwner

/**
 * Returns a [SharedViewModelStoreNavEntryDecorator] that is remembered across recompositions.
 *
 * @param [viewModelStoreOwner] The [ViewModelStoreOwner] that provides the [ViewModelStore] to
 *   NavEntries
 * @param [removeViewModelStoreOnPop] A lambda that returns a Boolean for whether the store for a
 *   [NavEntry] should be removed when the [NavEntry] is popped from the backStack. If true, the
 *   entry's ViewModelStore will be removed.
 */
@Composable
fun <T : Any> rememberSharedViewModelStoreNavEntryDecorator(
    viewModelStoreOwner: ViewModelStoreOwner =
        checkNotNull(LocalViewModelStoreOwner.current) {
            "No ViewModelStoreOwner was provided via LocalViewModelStoreOwner"
        },
    removeViewModelStoreOnPop: () -> Boolean = { true },
): SharedViewModelStoreNavEntryDecorator<T> {
    val currentRemoveViewModelStoreOnPop = rememberUpdatedState(removeViewModelStoreOnPop)
    return remember(viewModelStoreOwner, currentRemoveViewModelStoreOnPop) {
        SharedViewModelStoreNavEntryDecorator(
            viewModelStoreOwner.viewModelStore,
            removeViewModelStoreOnPop,
        )
    }
}

/**
 * Provides the content of a [NavEntry] with a [ViewModelStoreOwner] and provides that
 * [ViewModelStoreOwner] as a [LocalViewModelStoreOwner] so that it is available within the content.
 *
 * If the [NavEntry] specifies that it has a parent in its metadata, the parent's
 * [ViewModelStoreOwner] will be supplied instead of creating a new one. This allows the
 * entry to access its parent's [ViewModel]s.
 *
 * @see [SharedViewModelStoreNavEntryDecorator.parent]
 *
 * This requires the usage of [androidx.navigation3.runtime.SaveableStateHolderNavEntryDecorator] to
 * ensure that the [NavEntry] scoped [ViewModel]s can properly provide access to
 * [androidx.lifecycle.SavedStateHandle]s
 *
 * @param [viewModelStore] The [ViewModelStore] that provides to NavEntries
 * @param [removeViewModelStoreOnPop] A lambda that returns a Boolean for whether the store for a
 *   [NavEntry] should be cleared when the [NavEntry] is popped from the backStack. If true, the
 *   entry's ViewModelStore will be removed.
 * @see NavEntryDecorator.onPop for more details on when this callback is invoked
 */
class SharedViewModelStoreNavEntryDecorator<T : Any>(
    viewModelStore: ViewModelStore,
    removeViewModelStoreOnPop: () -> Boolean,
) :
    NavEntryDecorator<T>(
        onPop = ({ key ->
            if (removeViewModelStoreOnPop()) {
                viewModelStore.getEntryViewModel().clearViewModelStoreOwnerForKey(key)
            }
        }),
        decorate = { entry ->
            val standaloneViewModelStore =
                viewModelStore.getEntryViewModel().viewModelStoreForKey(entry.contentKey)
            val standaloneViewModelStoreOwner =
                rememberViewModelStoreOwner(standaloneViewModelStore)

            // If the entry indicates it has a parent, use its parent's ViewModelStore.
            val parentViewModelStore = entry.metadata[ParentKey]?.let {
                viewModelStore.getEntryViewModel().viewModelStoreForKey(it)
            }
            val parentViewModelStoreOwner = parentViewModelStore?.let {
                rememberViewModelStoreOwner(it)
            }

            CompositionLocalProvider(LocalViewModelStoreOwner provides standaloneViewModelStoreOwner) {
                if (parentViewModelStoreOwner != null) {
                    CompositionLocalProvider(
                        LocalSharedViewModelStoreOwner provides parentViewModelStoreOwner
                    ) {
                        entry.Content()
                    }
                } else {
                    entry.Content()
                }
            }
        },
    ) {

    companion object {
        /**
         * Use this function to specify a `NavEntry`'s parent. The parent's
         * `ViewModelStoreOwner` will be supplied using `LocalViewModelStoreOwner` rather than
         * creating a new `ViewModelStoreOwner` for this `NavEntry`.
         */
        fun parent(key: Any) = metadata {
            put(ParentKey, key)
        }

        object ParentKey : NavMetadataKey<Any>
    }

}

private class EntryViewModel : ViewModel() {
    private val owners = mutableMapOf<Any, ViewModelStore>()

    fun viewModelStoreForKey(key: Any): ViewModelStore = owners.getOrPut(key) { ViewModelStore() }

    fun clearViewModelStoreOwnerForKey(key: Any) {
        owners.remove(key)?.clear()
    }

    override fun onCleared() {
        owners.forEach { (_, store) -> store.clear() }
    }
}


private fun ViewModelStore.getEntryViewModel(): EntryViewModel {
    val provider =
        ViewModelProvider.create(
            store = this,
            factory = viewModelFactory { initializer { EntryViewModel() } },
        )
    return provider[EntryViewModel::class]
}

val LocalSharedViewModelStoreOwner =
    staticCompositionLocalOf<ViewModelStoreOwner> { error("No LocalSharedViewModelStoreOwner provided!") }

@Composable
fun rememberViewModelStoreOwner(viewModelStore: ViewModelStore): ViewModelStoreOwner {
    val savedStateRegistryOwner = LocalSavedStateRegistryOwner.current

    return remember(viewModelStore, savedStateRegistryOwner) {
        object :
            ViewModelStoreOwner,
            SavedStateRegistryOwner by savedStateRegistryOwner,
            HasDefaultViewModelProviderFactory {
            override val viewModelStore: ViewModelStore
                get() = viewModelStore

            override val defaultViewModelProviderFactory: ViewModelProvider.Factory
                get() = SavedStateViewModelFactory()

            override val defaultViewModelCreationExtras: CreationExtras
                get() =
                    MutableCreationExtras().also {
                        it[SAVED_STATE_REGISTRY_OWNER_KEY] = this
                        it[VIEW_MODEL_STORE_OWNER_KEY] = this
                    }

            init {
                require(this.lifecycle.currentState == Lifecycle.State.INITIALIZED) {
                    "The Lifecycle state is already beyond INITIALIZED. The " +
                            "SharedViewModelStoreNavEntryDecorator requires adding the " +
                            "SavedStateNavEntryDecorator to ensure support for " +
                            "SavedStateHandles."
                }
                enableSavedStateHandles()
            }
        }
    }
}

SharedViewModelStoreNavEntryDecorator.kt
```

```
/*
 * Copyright 2025 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.example.nav3recipes.sharedviewmodel

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.material3.Button
import androidx.compose.material3.Text
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.setValue
import androidx.lifecycle.ViewModel
import androidx.lifecycle.compose.dropUnlessResumed
import androidx.lifecycle.viewmodel.compose.viewModel
import androidx.navigation3.runtime.NavKey
import androidx.navigation3.runtime.entryProvider
import androidx.navigation3.runtime.rememberNavBackStack
import androidx.navigation3.runtime.rememberSaveableStateHolderNavEntryDecorator
import androidx.navigation3.ui.NavDisplay
import com.example.nav3recipes.content.ContentBlue
import com.example.nav3recipes.content.ContentGreen
import com.example.nav3recipes.content.ContentRed
import com.example.nav3recipes.ui.setEdgeToEdgeConfig
import kotlinx.serialization.Serializable


@Serializable
private data object ParentScreen : NavKey

@Serializable
private data object ChildScreen : NavKey

@Serializable
private data object StandaloneScreen : NavKey

class SharedViewModelActivity : ComponentActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        setEdgeToEdgeConfig()
        super.onCreate(savedInstanceState)

        setContent {
            val backStack = rememberNavBackStack(ParentScreen)

            NavDisplay(
                backStack = backStack,
                onBack = { backStack.removeLastOrNull() },
                entryDecorators = listOf(
                    rememberSaveableStateHolderNavEntryDecorator(),
                    rememberSharedViewModelStoreNavEntryDecorator(),
                ),
                entryProvider = entryProvider {
                    entry<ParentScreen>(
                        clazzContentKey = { key -> key.toContentKey() },
                    ) {
                        val viewModel = viewModel(modelClass = CounterViewModel::class)

                        ContentRed("Parent screen") {
                            Button(onClick = dropUnlessResumed { viewModel.count++ }) {
                                Text("Count: ${viewModel.count}")
                            }
                            Button(onClick = dropUnlessResumed { backStack.add(ChildScreen) }) {
                                Text("View child screen")
                            }
                        }
                    }
                    entry<ChildScreen>(
                        metadata = SharedViewModelStoreNavEntryDecorator.parent(
                            ParentScreen.toContentKey()
                        )
                    ) {
                        val parentViewModel = viewModel(
                            modelClass = CounterViewModel::class,
                            viewModelStoreOwner = LocalSharedViewModelStoreOwner.current
                        )
                        val standaloneViewModel = viewModel(modelClass = CounterViewModel::class)

                        ContentBlue("Child screen") {
                            Button(onClick = dropUnlessResumed { parentViewModel.count++ }) {
                                Text("Parent count: ${parentViewModel.count}")
                            }
                            Button(onClick = dropUnlessResumed {
                                backStack.add(StandaloneScreen)
                            }) {
                                Text("View standalone screen")
                            }
                            Button(onClick = dropUnlessResumed {
                                standaloneViewModel.count++
                            }) {
                                Text("Standalone Count: ${standaloneViewModel.count}")
                            }
                        }
                    }
                    entry<StandaloneScreen> {
                        val viewModel = viewModel(modelClass = CounterViewModel::class)

                        ContentGreen("Standalone screen") {
                            Button(onClick = dropUnlessResumed {
                                viewModel.count++
                            }) {
                                Text("Count: ${viewModel.count}")
                            }
                        }
                    }
                }
            )
        }
    }
}

fun NavKey.toContentKey() = this.toString()

class CounterViewModel : ViewModel() {
    var count by mutableIntStateOf(0)
}

SharedViewModelActivity.kt
```