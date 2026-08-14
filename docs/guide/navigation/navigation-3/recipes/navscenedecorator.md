---
title: https://developer.android.com/guide/navigation/navigation-3/recipes/navscenedecorator
url: https://developer.android.com/guide/navigation/navigation-3/recipes/navscenedecorator
source: md.txt
---

# Nav UI with Scene Decorators Recipe

This recipe demonstrates how to add UI elements such as top app bars and navigation bars or rails that you'd like to add at the scene, rather than nav entry level. To do this, it uses the scene decorator API.

## How it works

### The `NavigationScene` class

The `NavigationScene` class is the core of this recipe. It takes in a `Scene`, the current window size class, a `SharedTransitionScope`, and composables for a nav bar and nav rail. If the window width size class is medium or greater, it renders the nav rail on the start edge of the screen with the content on the end edge. Otherwise, it renders the nav bar on the bottom edge of the screen with the content on top.

#### Rendering shared UI elements only once

During transitions between scenes, both scenes are composed and rendered at the same time. For elements that are shared between scenes, such as a nav bar or rail, it may not be desirable for them to be composed in both scenes.

For example, the nav bar and rail composables in this recipe have some internal state that can't be hoisted (such as the state for the animations after an item is selected). As such, it's desirable to call the given composable only from one scene at any given time.

To accomplish the desired behavior, this recipe combines Compose's [movable content](https://developer.android.com/reference/kotlin/androidx/compose/runtime/package-summary#movableContentOf(kotlin.Function0)) and [shared element](https://developer.android.com/develop/ui/compose/animation/shared-elements) APIs:

- By using `movableContentOf`, it is able to retain the state of the composable as it is moved between the different branches of the composition corresponding to each scene.
- By using the shared element APIs, it is able to keep the nav bar/rail in place while animating the content of the scenes that have been decorated. This is accomplished using the `sharedElement` modifier as well as a custom modifier, `cacheSize`, that maintains a placeholder of the correct size in the scene that doesn't call the movable content composable.

### The `NavigationSceneDecoratorStrategy` class

The `NavigationSceneDecoratorStrategy` class is responsible for wrapping the input scene in a `NavigationScene`. The `rememberNavigationSceneDecoratorStrategy` function simplifies the process of creating a `NavigationSceneDecoratorStrategy` by handling the creation of the `movableContentOf` composables. Generally, the `NavigationSceneDecoratorStrategy` should be one of, if not the final, items in the `sceneDecoratorStrategies` parameter so that it can contain all the other content of the app.
[![](https://developer.android.com/static/images/picto-icons/code.svg) Explore View the full recipe on GitHub.](https://github.com/android/nav3-recipes/tree/main/app/src/main/java/com/example/nav3recipes/navscenedecorator)

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

package com.example.nav3recipes.navscenedecorator

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.animation.SharedTransitionLayout
import androidx.compose.runtime.remember
import androidx.navigation3.runtime.NavKey
import androidx.navigation3.runtime.entryProvider
import androidx.navigation3.ui.NavDisplay
import com.example.nav3recipes.scenes.listdetail.rememberListDetailSceneStrategy
import com.example.nav3recipes.ui.setEdgeToEdgeConfig

class ResponsiveNavigationSceneDecoratorActivity : ComponentActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setEdgeToEdgeConfig()

        setContent {
            SharedTransitionLayout {
                val navigationState = rememberNavigationState(
                    startRoute = RouteA,
                    topLevelRoutes = setOf(RouteA, RouteB, RouteC)
                )

                val navigator = remember(navigationState) { Navigator(navigationState) }

                val listDetailStrategy = rememberListDetailSceneStrategy<NavKey>()

                val responsiveNavigationSceneDecoratorStrategy =
                    rememberResponsiveNavigationSceneDecoratorStrategy<NavKey>(
                        navBar = { NavBar(NAV_ITEMS, navigator) },
                        navRail = { NavRail(NAV_ITEMS, navigator) },
                        sharedTransitionScope = this
                    )

                val entryProvider = entryProvider {
                    featureASection { id -> navigator.navigate(RouteA1(id)) }
                    featureBSection { navigator.navigate(RouteB1) }
                    featureCSection { navigator.navigate(RouteC1) }
                }

                NavDisplay(
                    entries = navigationState.toEntries(entryProvider),
                    sceneDecoratorStrategies = listOf(responsiveNavigationSceneDecoratorStrategy),
                    sceneStrategies = listOf(listDetailStrategy),
                    sharedTransitionScope = this,
                    onBack = navigator::goBack
                )
            }
        }
    }
}
```

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

package com.example.nav3recipes.navscenedecorator

import androidx.compose.animation.EnterExitState
import androidx.compose.animation.SharedTransitionScope
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.adaptive.currentWindowAdaptiveInfoV2
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.movableContentOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.rememberUpdatedState
import androidx.compose.ui.Modifier
import androidx.navigation3.scene.Scene
import androidx.navigation3.scene.SceneDecoratorStrategy
import androidx.navigation3.scene.SceneDecoratorStrategyScope
import androidx.navigation3.ui.LocalNavAnimatedContentScope
import androidx.window.core.layout.WindowSizeClass

data class ResponsiveNavigationScene<T : Any>(
    private val scene: Scene<T>,
    private val sharedTransitionScope: SharedTransitionScope,
    private val windowSizeClass: WindowSizeClass,
    private val navBarContent: @Composable (() -> Unit),
    private val navRailContent: @Composable (() -> Unit),
) : Scene<T> by scene {
    override val key = scene::class to scene.key

    override val content = @Composable {
        val animatedContentScope = LocalNavAnimatedContentScope.current
        val isMovableContentCaller =
            animatedContentScope.transition.targetState == EnterExitState.Visible

        with(sharedTransitionScope) {
            if (windowSizeClass.isWidthAtLeastBreakpoint(WindowSizeClass.WIDTH_DP_MEDIUM_LOWER_BOUND)) {
                Row(Modifier.fillMaxSize()) {
                    Box(
                        modifier = Modifier
                            .cacheSize(!isMovableContentCaller)
                            .sharedElement(
                                rememberSharedContentState("nav-rail"),
                                animatedContentScope
                            )
                    ) {
                        if (isMovableContentCaller) {
                            navRailContent()
                        }
                    }
                    Box(modifier = Modifier.weight(1f)) {
                        scene.content()
                    }
                }
            } else {
                Column(Modifier.fillMaxSize()) {
                    Box(modifier = Modifier.weight(1f)) {
                        scene.content()
                    }
                    Box(
                        modifier = Modifier
                            .cacheSize(!isMovableContentCaller)
                            .sharedElement(
                                rememberSharedContentState("nav-bar"),
                                animatedContentScope
                            )
                    ) {
                        if (isMovableContentCaller) {
                            navBarContent()
                        }
                    }
                }
            }
        }
    }
}

@Composable
fun <T : Any> rememberResponsiveNavigationSceneDecoratorStrategy(
    navBar: @Composable () -> Unit,
    navRail: @Composable () -> Unit,
    sharedTransitionScope: SharedTransitionScope,
    windowSizeClass: WindowSizeClass = currentWindowAdaptiveInfoV2().windowSizeClass
): ResponsiveNavigationSceneDecoratorStrategy<T> {
    val currentNavBar by rememberUpdatedState(navBar)
    val currentNavRail by rememberUpdatedState(navRail)

    val movableNavBar = remember { movableContentOf { currentNavBar() } }
    val movableNavRail = remember { movableContentOf { currentNavRail() } }

    return remember(windowSizeClass, sharedTransitionScope) {
        ResponsiveNavigationSceneDecoratorStrategy(
            windowSizeClass,
            sharedTransitionScope,
            movableNavBar,
            movableNavRail
        )
    }
}

class ResponsiveNavigationSceneDecoratorStrategy<T : Any>(
    private val windowSizeClass: WindowSizeClass,
    private val sharedTransitionScope: SharedTransitionScope,
    private val navBarContent: @Composable () -> Unit,
    private val navRailContent: @Composable () -> Unit,
) : SceneDecoratorStrategy<T> {

    override fun SceneDecoratorStrategyScope<T>.decorateScene(scene: Scene<T>): Scene<T> {
        return ResponsiveNavigationScene(
            scene,
            sharedTransitionScope,
            windowSizeClass,
            navBarContent,
            navRailContent
        )
    }

}
```

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

package com.example.nav3recipes.navscenedecorator

import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.WindowInsets
import androidx.compose.foundation.layout.WindowInsetsSides
import androidx.compose.foundation.layout.consumeWindowInsets
import androidx.compose.foundation.layout.fillMaxHeight
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.only
import androidx.compose.foundation.layout.safeDrawing
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Camera
import androidx.compose.material.icons.filled.Face
import androidx.compose.material.icons.filled.Home
import androidx.compose.material3.Button
import androidx.compose.material3.Icon
import androidx.compose.material3.ListItem
import androidx.compose.material3.NavigationBar
import androidx.compose.material3.NavigationBarItem
import androidx.compose.material3.NavigationRail
import androidx.compose.material3.NavigationRailItem
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.saveable.rememberSaveable
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.compose.ui.unit.dp
import androidx.lifecycle.compose.dropUnlessResumed
import androidx.navigation3.runtime.EntryProviderScope
import androidx.navigation3.runtime.NavKey
import com.example.nav3recipes.content.ContentBase
import com.example.nav3recipes.content.ContentGreen
import com.example.nav3recipes.content.ContentMauve
import com.example.nav3recipes.content.ContentOrange
import com.example.nav3recipes.content.ContentPurple
import com.example.nav3recipes.scenes.listdetail.ListDetailScene
import com.example.nav3recipes.ui.theme.colors
import kotlinx.serialization.Serializable

@Serializable
data object RouteA : NavKey

@Serializable
data class RouteA1(val id: Int) : NavKey

@Serializable
data object RouteB : NavKey

@Serializable
data object RouteB1 : NavKey

@Serializable
data object RouteC : NavKey

@Serializable
data object RouteC1 : NavKey

const val ITEM_COUNT = 20

fun EntryProviderScope<NavKey>.featureASection(
    onSubRouteClick: (Int) -> Unit,
) {
    entry<RouteA>(
        metadata = ListDetailScene.listPane()
    ) {
        Surface(modifier = Modifier.fillMaxHeight()) {
            var contentPadding by remember { mutableStateOf(PaddingValues()) }
            LazyColumn(
                modifier = Modifier
                    .fillMaxSize()
                    .onWindowInsetsOverlapChanged(WindowInsets.safeDrawing) { contentPadding = it },
                contentPadding = contentPadding
            ) {
                items(List(ITEM_COUNT) { it + 1 }) { id ->
                    ListItem(
                        headlineContent = {
                            Text("Item $id")
                        },
                        leadingContent = {
                            Box(
                                modifier = Modifier
                                    .size(24.dp)
                                    .clip(RoundedCornerShape(4.dp))
                                    .background(colors[id % colors.size])
                            )
                        },
                        modifier = Modifier
                            .fillMaxWidth()
                            .clickable(onClick = dropUnlessResumed {
                                onSubRouteClick(id)
                            }),
                    )
                }
            }
        }
    }
    entry<RouteA1>(
        metadata = ListDetailScene.detailPane()
    ) { key ->
        ContentBase(
            "Item ${key.id}",
            modifier = Modifier.background(colors[key.id % colors.size])
        ) {
            var count by rememberSaveable {
                mutableIntStateOf(0)
            }

            Button(onClick = { count++ }) {
                Text("Value: $count")
            }
        }
    }
}

fun EntryProviderScope<NavKey>.featureBSection(
    onSubRouteClick: () -> Unit,
) {
    entry<RouteB> {
        ContentGreen("Route B") {
            Column(
                horizontalAlignment = Alignment.CenterHorizontally
            ) {
                Button(onClick = dropUnlessResumed { onSubRouteClick() }) {
                    Text("Go to B1")
                }
            }
        }
    }
    entry<RouteB1> {
        ContentPurple("Route B1") {
            var count by rememberSaveable {
                mutableIntStateOf(0)
            }
            Button(onClick = { count++ }) {
                Text("Value: $count")
            }
        }
    }
}

fun EntryProviderScope<NavKey>.featureCSection(
    onSubRouteClick: () -> Unit,
) {
    entry<RouteC> {
        ContentMauve("Route C") {
            Column(horizontalAlignment = Alignment.CenterHorizontally) {
                Button(onClick = dropUnlessResumed { onSubRouteClick() }) {
                    Text("Go to C1")
                }
            }
        }
    }
    entry<RouteC1> {
        ContentOrange("Route C1") {
            var count by rememberSaveable {
                mutableIntStateOf(0)
            }

            Button(onClick = { count++ }) {
                Text("Value: $count")
            }
        }
    }
}

data class NavBarItem(
    val navKey: NavKey,
    val icon: ImageVector,
    val description: String
)

val NAV_ITEMS = listOf(
    NavBarItem(RouteA, Icons.Default.Home, "Route A"),
    NavBarItem(RouteB, Icons.Default.Face, "Route B"),
    NavBarItem(RouteC, Icons.Default.Camera, "Route C"),
)

@Composable
fun NavBar(navBarItems: List<NavBarItem>, navigator: Navigator) {
    NavBar(
        navBarItems = navBarItems,
        topLevelRoute = navigator.state.topLevelRoute,
        onNavItemClick = { navigator.navigate(it) }
    )
}

@Composable
fun NavBar(navBarItems: List<NavBarItem>, topLevelRoute: NavKey, onNavItemClick: (NavKey) -> Unit) {
    NavigationBar(Modifier.consumeWindowInsets(WindowInsets.safeDrawing.only(WindowInsetsSides.Horizontal + WindowInsetsSides.Bottom))) {
        navBarItems.forEach { item ->
            NavigationBarItem(
                selected = item.navKey == topLevelRoute,
                onClick = { onNavItemClick(item.navKey) },
                icon = {
                    Icon(
                        imageVector = item.icon,
                        contentDescription = item.description
                    )
                },
                label = {
                    Text(item.description)
                })
        }
    }
}

@Composable
fun NavRail(navRailItems: List<NavBarItem>, navigator: Navigator) {
    NavRail(
        navRailItems = navRailItems,
        topLevelRoute = navigator.state.topLevelRoute,
        onNavItemClick = { navigator.navigate(it) }
    )
}

@Composable
fun NavRail(
    navRailItems: List<NavBarItem>,
    topLevelRoute: NavKey,
    onNavItemClick: (NavKey) -> Unit
) {
    NavigationRail {
        navRailItems.forEach { item ->
            NavigationRailItem(
                selected = item.navKey == topLevelRoute,
                onClick = { onNavItemClick(item.navKey) },
                icon = {
                    Icon(
                        imageVector = item.icon,
                        contentDescription = item.description
                    )
                },
                label = {
                    Text(item.description)
                })
        }
    }
}
```

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

package com.example.nav3recipes.navscenedecorator

import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.WindowInsets
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.layout.LayoutCoordinates
import androidx.compose.ui.layout.Measurable
import androidx.compose.ui.layout.MeasureResult
import androidx.compose.ui.layout.MeasureScope
import androidx.compose.ui.layout.boundsInWindow
import androidx.compose.ui.node.GlobalPositionAwareModifierNode
import androidx.compose.ui.node.LayoutModifierNode
import androidx.compose.ui.node.ModifierNodeElement
import androidx.compose.ui.node.invalidateMeasurement
import androidx.compose.ui.platform.InspectorInfo
import androidx.compose.ui.platform.LocalDensity
import androidx.compose.ui.platform.LocalLayoutDirection
import androidx.compose.ui.platform.LocalWindowInfo
import androidx.compose.ui.unit.Constraints
import androidx.compose.ui.unit.Density
import androidx.compose.ui.unit.IntSize
import androidx.compose.ui.unit.LayoutDirection

/**
 * A modifier that caches the measured size of the component and optionally reuses it. For example,
 * this can be used to maintain the size of an element that contains moveable content.
 *
 * @param useCachedSize If true, the modifier will use the previously measured and cached size
 * (if available) instead of the current size. If false, it measures normally and caches the new size.
 */
fun Modifier.cacheSize(useCachedSize: Boolean): Modifier =
    this.then(CacheSizeElement(useCachedSize))

private data class CacheSizeElement(
    val useCachedSize: Boolean
) : ModifierNodeElement<CacheSizeNode>() {

    override fun create() = CacheSizeNode(useCachedSize)

    override fun update(node: CacheSizeNode) {
        node.useCachedSize = useCachedSize
    }

    override fun InspectorInfo.inspectableProperties() {
        name = "cacheSize"
        properties["useCachedSize"] = useCachedSize
    }
}

private class CacheSizeNode(
    useCachedSize: Boolean
) : Modifier.Node(), LayoutModifierNode {

    var useCachedSize: Boolean = useCachedSize
        set(value) {
            if (field != value) {
                field = value
                invalidateMeasurement()
            }
        }

    private var isSizeCached = false
    private var cachedSize: IntSize = IntSize.Zero

    override fun MeasureScope.measure(
        measurable: Measurable,
        constraints: Constraints
    ): MeasureResult {
        val placeable = measurable.measure(constraints)
        val currentSize = IntSize(placeable.width, placeable.height)

        val size = if (useCachedSize && isSizeCached) {
            cachedSize
        } else {
            currentSize
        }

        cachedSize = size
        isSizeCached = true

        return layout(size.width, size.height) {
            placeable.placeRelative(0, 0)
        }
    }
}

/**
 * A modifier that calculates how much the component overlaps with the given [WindowInsets]
 * and reports the overlap as [PaddingValues].
 *
 * This can be used to dynamically adjust the layout of content that is partially obscured
 * by system bars or other window insets, such as by using it as the `contentPadding` parameter
 * for a [androidx.compose.foundation.lazy.LazyColumn] or [androidx.compose.foundation.lazy.LazyRow]
 *
 * @param insets The [WindowInsets] to calculate the overlap against.
 * @param onOverlapChanged A callback invoked whenever the overlap changes, providing the overlap as [PaddingValues].
 */
@Composable
fun Modifier.onWindowInsetsOverlapChanged(
    insets: WindowInsets,
    onOverlapChanged: (PaddingValues) -> Unit
): Modifier {
    val density = LocalDensity.current
    val windowInfo = LocalWindowInfo.current
    val layoutDirection = LocalLayoutDirection.current

    return this.then(
        WindowInsetsOverlapElement(
            insets = insets,
            density = density,
            windowHeight = windowInfo.containerSize.height.toFloat(),
            windowWidth = windowInfo.containerSize.width.toFloat(),
            layoutDirection = layoutDirection,
            onOverlapChanged = onOverlapChanged
        )
    )
}

private data class WindowInsetsOverlapElement(
    val insets: WindowInsets,
    val density: Density,
    val windowHeight: Float,
    val windowWidth: Float,
    val layoutDirection: LayoutDirection,
    val onOverlapChanged: (PaddingValues) -> Unit
) : ModifierNodeElement<WindowInsetsOverlapNode>() {
    override fun create() = WindowInsetsOverlapNode(
        insets, density, windowHeight, windowWidth, layoutDirection, onOverlapChanged
    )

    override fun update(node: WindowInsetsOverlapNode) {
        node.insets = insets
        node.density = density
        node.windowHeight = windowHeight
        node.windowWidth = windowWidth
        node.layoutDirection = layoutDirection
        node.onOverlapChanged = onOverlapChanged

        // Recalculate padding when modifier properties (like insets) change,
        // even if the component hasn't moved or changed size (no layout pass).
        node.calculatePadding()
    }

    override fun InspectorInfo.inspectableProperties() {
        name = "onWindowInsetsOverlapChanged"
        properties["insets"] = insets
    }
}

private class WindowInsetsOverlapNode(
    var insets: WindowInsets,
    var density: Density,
    var windowHeight: Float,
    var windowWidth: Float,
    var layoutDirection: LayoutDirection,
    var onOverlapChanged: (PaddingValues) -> Unit
) : Modifier.Node(), GlobalPositionAwareModifierNode {

    // Cache the layout coordinates so padding can be recalculated
    // when insets change without triggering a new global positioning pass.
    private var lastCoordinates: LayoutCoordinates? = null

    override fun onGloballyPositioned(coordinates: LayoutCoordinates) {
        lastCoordinates = coordinates
        calculatePadding()
    }

    fun calculatePadding() {
        val coordinates = lastCoordinates ?: return
        val screenRect = coordinates.boundsInWindow()

        val topOverlap = (insets.getTop(density) - screenRect.top).coerceAtLeast(0f)
        val bottomOverlap = (screenRect.bottom - (windowHeight - insets.getBottom(density))).coerceAtLeast(0f)
        val leftOverlap = (insets.getLeft(density, layoutDirection) - screenRect.left).coerceAtLeast(0f)
        val rightOverlap = (screenRect.right - (windowWidth - insets.getRight(density, layoutDirection))).coerceAtLeast(0f)

        with(density) {
            onOverlapChanged(
                PaddingValues.Absolute(
                    left = leftOverlap.toDp(),
                    top = topOverlap.toDp(),
                    right = rightOverlap.toDp(),
                    bottom = bottomOverlap.toDp()
                )
            )
        }
    }
}
```

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

package com.example.nav3recipes.navscenedecorator

import androidx.compose.runtime.Composable
import androidx.compose.runtime.MutableState
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.saveable.rememberSerializable
import androidx.compose.runtime.setValue
import androidx.compose.runtime.snapshots.SnapshotStateList
import androidx.compose.runtime.toMutableStateList
import androidx.navigation3.runtime.NavBackStack
import androidx.navigation3.runtime.NavEntry
import androidx.navigation3.runtime.NavKey
import androidx.navigation3.runtime.rememberDecoratedNavEntries
import androidx.navigation3.runtime.rememberSaveableStateHolderNavEntryDecorator
import androidx.navigation3.runtime.serialization.NavKeySerializer
import androidx.savedstate.compose.serialization.serializers.MutableStateSerializer
import com.example.nav3recipes.conditional.rememberNavBackStack

/**
 * Create a navigation state that persists config changes and process death.
 */
@Composable
fun rememberNavigationState(
    startRoute: NavKey, topLevelRoutes: Set<NavKey>
): NavigationState {

    val topLevelRoute = rememberSerializable(
        startRoute, topLevelRoutes, serializer = MutableStateSerializer(NavKeySerializer())
    ) {
        mutableStateOf(startRoute)
    }

    val backStacks = topLevelRoutes.associateWith { key -> rememberNavBackStack(key) }

    return remember(startRoute, topLevelRoutes) {
        NavigationState(
            startRoute = startRoute, topLevelRoute = topLevelRoute, backStacks = backStacks
        )
    }
}

/**
 * State holder for navigation state.
 *
 * @param startRoute - the start route. The user will exit the app through this route.
 * @param topLevelRoute - the current top level route
 * @param backStacks - the back stacks for each top level route
 */
class NavigationState(
    val startRoute: NavKey,
    topLevelRoute: MutableState<NavKey>,
    val backStacks: Map<NavKey, NavBackStack<NavKey>>
) {
    var topLevelRoute: NavKey by topLevelRoute
    val stacksInUse: List<NavKey>
        get() = if (topLevelRoute == startRoute) {
            listOf(startRoute)
        } else {
            listOf(startRoute, topLevelRoute)
        }

}

/**
 * Convert NavigationState into NavEntries.
 */
@Composable
fun NavigationState.toEntries(
    entryProvider: (NavKey) -> NavEntry<NavKey>
): SnapshotStateList<NavEntry<NavKey>> {

    val decoratedEntries = backStacks.mapValues { (_, stack) ->
        val decorators = listOf(
            rememberSaveableStateHolderNavEntryDecorator<NavKey>(),
        )
        rememberDecoratedNavEntries(
            backStack = stack, entryDecorators = decorators, entryProvider = entryProvider
        )
    }

    return stacksInUse.flatMap { decoratedEntries[it] ?: emptyList() }.toMutableStateList()
}
```

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

package com.example.nav3recipes.navscenedecorator

import androidx.navigation3.runtime.NavKey

class Navigator(val state: NavigationState) {
    fun navigate(route: NavKey) {
        if (route in state.backStacks.keys) {
            // This is a top level route, just switch to it
            state.topLevelRoute = route
        } else {
            if (route is RouteA1) {
                state.backStacks[state.topLevelRoute]?.removeAll { it is RouteA1 }
            }
            state.backStacks[state.topLevelRoute]?.add(route)
        }
    }

    fun goBack() {
        val currentStack = state.backStacks[state.topLevelRoute]
            ?: error("Stack for ${state.topLevelRoute} not found")
        val currentRoute = currentStack.last()

        // If we're at the base of the current route, go back to the start route stack.
        if (currentRoute == state.topLevelRoute) {
            state.topLevelRoute = state.startRoute
        } else {
            currentStack.removeLastOrNull()
        }
    }
}
```