---
title: App architecture  |  Android Developers
url: https://developer.android.com/guide/navigation/navigation-3/recipes/retain
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [App architecture](https://developer.android.com/topic/architecture/intro)

Stay organized with collections

Save and categorize content based on your preferences.



# Retain Recipe

This recipe demonstrates how to retain values for items on the back stack.
It also shows how to implement a custom NavEntryDecorator.

## How it works

To use retain with nav 3, you need to define and install a NavEntryDecorator.
This decorator will mange a `RetainedValuesStoreRegistry` that wraps destinations in a unique `RetainedValuesStore`.

The decorator implemented in this sample will keep retained values for as long as the item is in the backstack.
If an item is popped and then re-added, it will get new retained values.

For more information on retain, see the documentation for
[`retain`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/retain/package-summary?hl=en#retain(kotlin.Function0)),
[`RetainedValuesStore`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/retain/RetainedValuesStore?hl=en),
and [`RetainedValuesStoreRegistry`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/retain/RetainedValuesStoreRegistry?hl=en).

For information on NavEntryDecorator, see [the official documentation](https://developer.android.com/guide/navigation/navigation-3/naventrydecorators).

[![](/static/images/picto-icons/code.svg)

Explore

View the full recipe on GitHub.

arrow\_forward](https://github.com/android/nav3-recipes/tree/main/app/src/main/java/com/example/nav3recipes/retain)

```
package com.example.nav3recipes.retain

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.LocalActivity
import androidx.activity.compose.setContent
import androidx.compose.material3.Button
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.mutableStateListOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.rememberUpdatedState
import androidx.compose.runtime.retain.RetainedValuesStore
import androidx.compose.runtime.retain.RetainedValuesStoreRegistry
import androidx.compose.runtime.retain.retain
import androidx.compose.runtime.retain.retainRetainedValuesStoreRegistry
import androidx.lifecycle.compose.dropUnlessResumed
import androidx.navigation3.runtime.NavEntry
import androidx.navigation3.runtime.NavEntryDecorator
import androidx.navigation3.ui.NavDisplay
import com.example.nav3recipes.content.ContentBlue
import com.example.nav3recipes.content.ContentGreen
import com.example.nav3recipes.ui.setEdgeToEdgeConfig

private data object RouteA

private data class RouteB(val id: Int)

class RetainActivity : ComponentActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        setEdgeToEdgeConfig()
        super.onCreate(savedInstanceState)
        setContent {
            val backStack = remember { mutableStateListOf<Any>(RouteA) }

            NavDisplay(
                backStack = backStack,
                onBack = { backStack.removeLastOrNull() },
                entryDecorators = listOf(
                    rememberRetainedValuesStoreNavEntryDecorator()
                ),
                entryProvider = { key ->
                    when (key) {
                        is RouteA -> NavEntry(key) {
                            ContentGreen("Nav3 with retain support") {
                                Text("Retained value: ${retainValue()}")
                                Button(onClick = dropUnlessResumed {
                                    backStack.add(RouteB(1))
                                }) {
                                    Text("Click to navigate")
                                }
                            }
                        }

                        is RouteB -> NavEntry(key) {
                            ContentBlue("Route id: ${key.id}") {
                                Text("Retained value: ${retainValue()}")
                                Button(onClick = dropUnlessResumed {
                                    backStack.add(RouteB(key.id + 1))
                                }) {
                                    Text("Click to navigate")
                                }
                            }
                        }

                        else -> {
                            error("Unknown route: $key")
                        }
                    }
                }
            )
        }
    }

    @Composable
    private fun retainValue() = retain { "Retained Value ${retainCount++}" }

    private companion object {
        // Counter to track how many values have been retained
        // Resets on process death.
        var retainCount = 0
    }
}

/**
 * Returns a [RetainedValuesStoreNavEntryDecorator] that is remembered across recompositions backed
 * by [registry].
 *
 * The underlying storage is controlled by the provided [registry]. By default, a new
 * [RetainedValuesStoreRegistry] is retained at this point in the composition hierarchy and will be
 * destroyed when the composition is permanently discarded or when the returned decorator is removed
 * from the composition hierarchy. If you need the backing storage of this decorator to have a
 * different lifespan, you can manually manage and provide a [RetainedValuesStoreRegistry] with the
 * intended lifespan.
 *
 * @param registry The underlying [RetainedValuesStoreRegistry] used to provide
 *   [RetainedValuesStore] instances to [NavEntries][NavEntry]. This instance should be retained to
 *   properly survive destruction and recreation scenarios.
 */
@Composable
fun <T : Any> rememberRetainedValuesStoreNavEntryDecorator(
    registry: RetainedValuesStoreRegistry = retainRetainedValuesStoreRegistry()
): RetainedValuesStoreNavEntryDecorator<T> {
    return remember(registry) {
        RetainedValuesStoreNavEntryDecorator(registry)
    }
}

/**
 * Provides the content of each [NavEntry] with a dedicated [RetainedValuesStore] so that each nav
 * entry may retain its own values.
 *
 * @param registry The underlying [RetainedValuesStoreRegistry] used to provide
 *   [RetainedValuesStore] instances to [NavEntries][NavEntry]. This instance should be retained to
 *   properly survive destruction and recreation scenarios.
 */
class RetainedValuesStoreNavEntryDecorator<T : Any>(
    registry: RetainedValuesStoreRegistry,
) : NavEntryDecorator<T>(
    onPop = { key ->
        registry.clearChild(key)
    },
    decorate = { entry ->
        registry.LocalRetainedValuesStoreProvider(entry.contentKey) { entry.Content() }
    },
)

RetainActivity.kt
```