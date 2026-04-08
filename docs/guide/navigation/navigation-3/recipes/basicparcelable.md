---
title: App architecture  |  Android Developers
url: https://developer.android.com/guide/navigation/navigation-3/recipes/basicparcelable
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [App architecture](https://developer.android.com/topic/architecture/intro)

Stay organized with collections

Save and categorize content based on your preferences.



# Basic Parcelable Recipe

This recipe shows a basic example of how to create a persistent back stack that survives configuration changes, without using `kotlinx.serialization`. Instead, it uses Android's `Parcelable` and the [`kotlin-parcelize`](https://developer.android.com/kotlin/parcelize) plugin to save and restore the navigation state.

## How it works

In this example, `RouteA` and `RouteB` implement a marker interface, `Route`, which itself extends `Parcelable`. They are also annotated with `@Parcelize` from the `kotlin-parcelize` plugin, which automatically generates a `Parcelable` implementation:

```
sealed interface Route : Parcelable

@Parcelize
data object RouteA : Route

@Parcelize
data class RouteB(val id: String) : Route
```

To make the back stack persistent, this recipe defines the `rememberParcelableBackStack` function. To ensure that `NavDisplay` and other composables are aware of changes to the back stack, the back stack is stored in a `SnapshotStateList`.

```
@Composable
fun <T : Parcelable> rememberParcelableBackStack(vararg elements: T): SnapshotStateList<T> {
    return rememberSaveable {
        mutableStateListOf(*elements)
    }
}
```

This acts as an alternative to the built-in `rememberNavBackStack` from `androidx.navigation3.runtime` which relies on `kotlinx.serialization`. Use this approach if your application strictly prefers `Parcelable` and avoids depending on `kotlinx.serialization`.

[![](/static/images/picto-icons/code.svg)

Explore

View the full recipe on GitHub.

arrow\_forward](https://github.com/android/nav3-recipes/tree/main/app/src/main/java/com/example/nav3recipes/basicparcelable)

```
/*
 * Copyright 2026 The Android Open Source Project
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

package com.example.nav3recipes.basicparcelable

import android.os.Bundle
import android.os.Parcelable
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.material3.Button
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.mutableStateListOf
import androidx.compose.runtime.saveable.rememberSaveable
import androidx.compose.runtime.snapshots.SnapshotStateList
import androidx.lifecycle.compose.dropUnlessResumed
import androidx.navigation3.runtime.NavEntry
import androidx.navigation3.ui.NavDisplay
import com.example.nav3recipes.content.ContentBlue
import com.example.nav3recipes.content.ContentGreen
import com.example.nav3recipes.ui.setEdgeToEdgeConfig
import kotlinx.parcelize.Parcelize

sealed interface Route : Parcelable

@Parcelize
data object RouteA : Route

@Parcelize
data class RouteB(val id: String) : Route

/**
 * Creates and remembers a [SnapshotStateList] to hold a back stack of [Parcelable] routes
 * that survives configuration changes and process death.
 *
 * @param T The route type, which must implement [Parcelable].
 * @param elements The initial routes to populate the back stack.
 * @return A reactive [SnapshotStateList] managing the navigation back stack.
 */
@Composable
fun <T : Parcelable> rememberParcelableBackStack(vararg elements: T): SnapshotStateList<T> {
    return rememberSaveable {
        mutableStateListOf(*elements)
    }
}

class BasicParcelableActivity : ComponentActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        setEdgeToEdgeConfig()
        super.onCreate(savedInstanceState)
        setContent {
            val backStack = rememberParcelableBackStack<Route>(RouteA)

            NavDisplay(
                backStack = backStack,
                onBack = { backStack.removeLastOrNull() },
                entryProvider = { key ->
                    when (key) {
                        is RouteA -> NavEntry(key) {
                            ContentGreen("Welcome to Nav3") {
                                Button(onClick = dropUnlessResumed {
                                    backStack.add(RouteB("123"))
                                }) {
                                    Text("Click to navigate")
                                }
                            }
                        }

                        is RouteB -> NavEntry(key) {
                            ContentBlue("Route id: ${key.id} ")
                        }
                    }
                }
            )
        }
    }
}

BasicParcelableActivity.kt
```