---
title: https://developer.android.com/guide/navigation/navigation-3/recipes/migration
url: https://developer.android.com/guide/navigation/navigation-3/recipes/migration
source: md.txt
---

```python
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

package com.example.nav3recipes.migration.content

import androidx.compose.foundation.layout.Column
import androidx.compose.material3.Button
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.lifecycle.compose.dropUnlessResumed
import com.example.nav3recipes.content.ContentGreen
import com.example.nav3recipes.content.ContentMauve
import com.example.nav3recipes.content.ContentPink
import com.example.nav3recipes.content.ContentPurple
import com.example.nav3recipes.content.ContentRed


@Composable
fun ScreenA(onSubRouteClick: () -> Unit, onDialogClick: () -> Unit) {
    ContentRed("Route A title") {
        Column(horizontalAlignment = Alignment.CenterHorizontally) {
            Button(onClick = dropUnlessResumed(block = onSubRouteClick)) {
                Text("Go to A1")
            }
            Button(onClick = dropUnlessResumed(block = onDialogClick)) {
                Text("Open dialog D")
            }
        }
    }
}

@Composable
fun ScreenA1() {
    ContentPink("Route A1 title")
}

@Composable
fun ScreenB(
    onDetailClick: (String) -> Unit,
    onDialogClick: () -> Unit
) {
    ContentGreen("Route B title") {
        Column(horizontalAlignment = Alignment.CenterHorizontally) {
            Button(onClick = dropUnlessResumed { onDetailClick("ABC") }) {
                Text("Go to B1")
            }
            Button(onClick = dropUnlessResumed(block = onDialogClick)) {
                Text("Open dialog D")
            }
        }
    }
}

@Composable
fun ScreenB1(id: String) {
    ContentPurple("Route B1 title. ID: $id")
}

@Composable
fun ScreenC(onDialogClick: () -> Unit) {
    ContentMauve("Route C title") {
        Column(horizontalAlignment = Alignment.CenterHorizontally) {
            Button(onClick = dropUnlessResumed(block = onDialogClick)) {
                Text("Open dialog D")
            }
        }
    }
}
```

```python
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

package com.example.nav3recipes.migration.atomic.end

import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Camera
import androidx.compose.material.icons.filled.Face
import androidx.compose.material.icons.filled.Home
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.navigation3.runtime.NavKey
import kotlinx.serialization.Serializable

// Feature module A
@Serializable data object RouteA : NavKey
@Serializable data object RouteA1 : NavKey

// Feature module B
@Serializable data object RouteB : NavKey
@Serializable data class RouteB1(val id: String) : NavKey

// Feature module C
@Serializable data object RouteC : NavKey

// Common UI modules
@Serializable data object RouteD : NavKey

val TOP_LEVEL_ROUTES = mapOf(
    RouteA to NavBarItem(icon = Icons.Default.Home, description = "Route A"),
    RouteB to NavBarItem(icon = Icons.Default.Face, description = "Route B"),
    RouteC to NavBarItem(icon = Icons.Default.Camera, description = "Route C"),
)

class NavBarItem(
    val icon: ImageVector,
    val description: String
)
```

```python
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

package com.example.nav3recipes.migration.atomic.end

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Icon
import androidx.compose.material3.NavigationBar
import androidx.compose.material3.NavigationBarItem
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.navigation3.runtime.EntryProviderScope
import androidx.navigation3.runtime.NavKey
import androidx.navigation3.runtime.entryProvider
import androidx.navigation3.scene.DialogSceneStrategy
import androidx.navigation3.ui.NavDisplay
import com.example.nav3recipes.migration.content.ScreenA
import com.example.nav3recipes.migration.content.ScreenA1
import com.example.nav3recipes.migration.content.ScreenB
import com.example.nav3recipes.migration.content.ScreenB1
import com.example.nav3recipes.migration.content.ScreenC
import com.example.nav3recipes.multiplestacks.Navigator
import com.example.nav3recipes.multiplestacks.rememberNavigationState
import com.example.nav3recipes.ui.setEdgeToEdgeConfig


class EndAtomicMigrationActivity : ComponentActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        setEdgeToEdgeConfig()
        super.onCreate(savedInstanceState)

        setContent {

            val navigationState = rememberNavigationState(
                startRoute = RouteA,
                topLevelRoutes = TOP_LEVEL_ROUTES.keys
            )

            val navigator = remember { Navigator(navigationState) }

            val entryProvider = entryProvider {
                featureASection(
                    onSubRouteClick = { navigator.navigate(RouteA1) },
                    onDialogClick = { navigator.navigate(RouteD) },
                )
                featureBSection(
                    onDetailClick = { id -> navigator.navigate(RouteB1(id)) },
                    onDialogClick = { navigator.navigate(RouteD) },
                )
                featureCSection(
                    onDialogClick = { navigator.navigate(RouteD) },
                )
                entry<RouteD>(metadata = DialogSceneStrategy.dialog()) {
                    Text(
                        modifier = Modifier.background(Color.White),
                        text = "Route D title (dialog)"
                    )
                }
            }

            Scaffold(bottomBar = {
                NavigationBar {
                    TOP_LEVEL_ROUTES.forEach { (key, value) ->
                        val isSelected = key == navigationState.topLevelRoute
                        NavigationBarItem(
                            selected = isSelected,
                            onClick = {
                                navigator.navigate(key)
                            },
                            icon = {
                                Icon(
                                    imageVector = value.icon,
                                    contentDescription = value.description
                                )
                            },
                            label = { Text(value.description) }
                        )
                    }
                }
            })

            { paddingValues ->
                NavDisplay(
                    entries = navigationState.toDecoratedEntries(entryProvider),
                    onBack = { navigator.goBack() },
                    sceneStrategy = remember { DialogSceneStrategy() },
                    modifier = Modifier.padding(paddingValues)
                )
            }
        }
    }
}

// Feature module A
private fun EntryProviderScope<NavKey>.featureASection(
    onSubRouteClick: () -> Unit,
    onDialogClick: () -> Unit
) {
    entry<RouteA> { ScreenA(onSubRouteClick, onDialogClick) }
    entry<RouteA1> { ScreenA1() }
}


// Feature module B
private fun EntryProviderScope<NavKey>.featureBSection(
    onDetailClick: (id: String) -> Unit,
    onDialogClick: () -> Unit
) {
    entry<RouteB> { ScreenB(onDetailClick, onDialogClick) }
    entry<RouteB1> { key -> ScreenB1(id = key.id) }
}

// Feature module C
private fun EntryProviderScope<NavKey>.featureCSection(
    onDialogClick: () -> Unit
) {
    entry<RouteC> { ScreenC(onDialogClick) }
}
```

```python
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

package com.example.nav3recipes.migration.atomic.begin

import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Camera
import androidx.compose.material.icons.filled.Face
import androidx.compose.material.icons.filled.Home
import androidx.compose.ui.graphics.vector.ImageVector
import kotlinx.serialization.Serializable

// Feature module A
@Serializable data object BaseRouteA
@Serializable data object RouteA
@Serializable data object RouteA1

// Feature module B
@Serializable data object BaseRouteB
@Serializable data object RouteB
@Serializable data class RouteB1(val id: String)

// Feature module C
@Serializable data object BaseRouteC
@Serializable data object RouteC

// Common UI modules
@Serializable data object RouteD


val TOP_LEVEL_ROUTES = mapOf(
    BaseRouteA to NavBarItem(icon = Icons.Default.Home, description = "Route A"),
    BaseRouteB to NavBarItem(icon = Icons.Default.Face, description = "Route B"),
    BaseRouteC to NavBarItem(icon = Icons.Default.Camera, description = "Route C"),
)

class NavBarItem(
    val icon: ImageVector,
    val description: String
)
```

```python
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

package com.example.nav3recipes.migration.atomic.begin

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Icon
import androidx.compose.material3.NavigationBar
import androidx.compose.material3.NavigationBarItem
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.runtime.getValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.navigation.NavDestination
import androidx.navigation.NavDestination.Companion.hasRoute
import androidx.navigation.NavDestination.Companion.hierarchy
import androidx.navigation.NavGraphBuilder
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.currentBackStackEntryAsState
import androidx.navigation.compose.dialog
import androidx.navigation.compose.navigation
import androidx.navigation.compose.rememberNavController
import androidx.navigation.navOptions
import androidx.navigation.toRoute
import com.example.nav3recipes.migration.content.ScreenA
import com.example.nav3recipes.migration.content.ScreenA1
import com.example.nav3recipes.migration.content.ScreenB
import com.example.nav3recipes.migration.content.ScreenB1
import com.example.nav3recipes.migration.content.ScreenC
import com.example.nav3recipes.ui.setEdgeToEdgeConfig
import kotlin.reflect.KClass

/**
 * Basic Navigation2 example with the following navigation graph:
 *
 * A -> A, A1
 * B -> B, B1
 * C -> C
 * D
 *
 * - The starting destination (or home screen) is A.
 * - A, B and C are top level destinations that appear in a navigation bar.
 * - D is a dialog destination.
  * - Navigating to a top level destination pops all other top level destinations off the stack,
 * except for the start destination.
 * - Navigating back from the start destination exits the app.
 *
 * This will be the starting point for migration to Navigation 3.
 *
 * @see `AtomicMigrationTest` for instrumented tests that verify this behavior.
 */
class BeginAtomicMigrationActivity : ComponentActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        setEdgeToEdgeConfig()
        super.onCreate(savedInstanceState)
        setContent {
            val navController = rememberNavController()
            val currentBackStackEntry by navController.currentBackStackEntryAsState()

            Scaffold(bottomBar = {
                NavigationBar {
                    TOP_LEVEL_ROUTES.forEach { (key, value) ->
                        val isSelected = currentBackStackEntry?.destination.isRouteInHierarchy(key::class)
                        NavigationBarItem(
                            selected = isSelected,
                            onClick = {
                                navController.navigate(key, navOptions {
                                    popUpTo(route = RouteA)
                                })
                            },
                            icon = {
                                Icon(
                                    imageVector = value.icon,
                                    contentDescription = value.description
                                )
                            },
                            label = { Text(value.description) }
                        )
                    }
                }
            })

            { paddingValues ->
                NavHost(
                    navController = navController,
                    startDestination = BaseRouteA,
                    modifier = Modifier.padding(paddingValues)
                ) {
                    featureASection(
                        onSubRouteClick = { navController.navigate(RouteA1) },
                        onDialogClick = { navController.navigate(RouteD) },
                    )
                    featureBSection(
                        onDetailClick = { id -> navController.navigate(RouteB1(id)) },
                        onDialogClick = { navController.navigate(RouteD) },
                    )
                    featureCSection(
                        onDialogClick = { navController.navigate(RouteD) },
                    )
                    dialog<RouteD> { key ->
                        Text(modifier = Modifier.background(Color.White), text = "Route D title (dialog)")
                    }
                }
            }
        }
    }
}

// Feature module A
private fun NavGraphBuilder.featureASection(
    onSubRouteClick: () -> Unit,
    onDialogClick: () -> Unit
) {
    navigation<BaseRouteA>(startDestination = RouteA) {
        composable<RouteA> { ScreenA(onSubRouteClick, onDialogClick) }
        composable<RouteA1> { ScreenA1() }
    }
}


// Feature module B
private fun NavGraphBuilder.featureBSection(
    onDetailClick: (id: String) -> Unit,
    onDialogClick: () -> Unit
) {
    navigation<BaseRouteB>(startDestination = RouteB) {
        composable<RouteB> { ScreenB(onDetailClick, onDialogClick) }
        composable<RouteB1> { key -> ScreenB1(id = key.toRoute<RouteB1>().id) }
    }
}

// Feature module C
private fun NavGraphBuilder.featureCSection(
    onDialogClick: () -> Unit
) {
    navigation<BaseRouteC>(startDestination = RouteC) {
        composable<RouteC> { ScreenC(onDialogClick) }
    }
}


private fun NavDestination?.isRouteInHierarchy(route: KClass<*>) =
    this?.hierarchy?.any {
        it.hasRoute(route)
    } ?: falsehttps://github.com/android/nav3-recipes/blob/720136f00b4c1bfbb3d09ae4b0f4bd16e3006536/app/src/main/java/com/example/nav3recipes/migration/atomic/begin/BeginAtomicMigrationActivity.kt
```