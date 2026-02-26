---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/lists
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/lists
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/ai-glasses-icon.svg) AI Glasses [](https://developer.android.com/develop/xr/devices#ai-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

In Jetpack Compose Glimmer, lists are vertically scrollable UI components that
efficiently render only visible items, designed to provide specific behaviors
and input compatibility for AI glasses apps. Jetpack Compose Glimmer
accomplishes this using the [`VerticalList`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/list/package-summary#VerticalList(androidx.compose.ui.Modifier,androidx.xr.glimmer.list.ListState,androidx.compose.foundation.layout.PaddingValues,kotlin.Boolean,androidx.compose.foundation.OverscrollEffect,androidx.compose.foundation.gestures.FlingBehavior,kotlin.Boolean,androidx.compose.ui.Alignment.Horizontal,androidx.compose.foundation.layout.Arrangement.Vertical,kotlin.Function1)) and [`ListItem`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/package-summary#ListItem(androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Function0,kotlin.Function0,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function0)) components.
![](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_components_lists.png) **Figure 1.** An example of some different styles of lists in Jetpack Compose Glimmer.

The [`VerticalList`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/list/package-summary#VerticalList(androidx.compose.ui.Modifier,androidx.xr.glimmer.list.ListState,androidx.compose.foundation.layout.PaddingValues,kotlin.Boolean,androidx.compose.foundation.OverscrollEffect,androidx.compose.foundation.gestures.FlingBehavior,kotlin.Boolean,androidx.compose.ui.Alignment.Horizontal,androidx.compose.foundation.layout.Arrangement.Vertical,kotlin.Function1)) is Jetpack Compose Glimmer's component for displaying
scrollable vertical content. It offers the same API functionality as
[`LazyColumn`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/lazy/package-summary#LazyColumn(androidx.compose.ui.Modifier,androidx.compose.foundation.lazy.LazyListState,androidx.compose.foundation.layout.PaddingValues,kotlin.Boolean,androidx.compose.foundation.layout.Arrangement.Vertical,androidx.compose.ui.Alignment.Horizontal,androidx.compose.foundation.gestures.FlingBehavior,kotlin.Boolean,androidx.compose.foundation.OverscrollEffect,kotlin.Function1)) but with behaviors specifically optimized for Jetpack Compose
Glimmer and AI glasses with a display.

> [!WARNING]
> **Warning:** Don't use `LazyColumn` in your AI glasses activities.

Jetpack Compose Glimmer lists have a few unique constraints:

- Lists should only show three items or less within a view.
- When a list contains more items than can fit within a view, a black scrim is used near the list's bounds.

## Example: Display a vertical list with three items

The following code shows how to use a [`VerticalList`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/list/package-summary#VerticalList(androidx.compose.ui.Modifier,androidx.xr.glimmer.list.ListState,androidx.compose.foundation.layout.PaddingValues,kotlin.Boolean,androidx.compose.foundation.OverscrollEffect,androidx.compose.foundation.gestures.FlingBehavior,kotlin.Boolean,androidx.compose.ui.Alignment.Horizontal,androidx.compose.foundation.layout.Arrangement.Vertical,kotlin.Function1)) and [`ListItem`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/package-summary#ListItem(androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Function0,kotlin.Function0,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function0))
components to create a list of three items:

    @Composable
    fun GlimmerListWithButtons() {
        VerticalList(
            contentPadding = PaddingValues(16.dp),
            verticalArrangement = Arrangement.spacedBy(20.dp)
        ) {
            items(count = 3) { index ->
                ListItem(
                    onClick = { /* Handle Click */ },
                    leadingIcon = if (index == 1) {
                        { Icon(Icons.Rounded.Favorite, "Favorite Icon") }
                    } else null
                ) {
                    Text("List Item + $index")
                }
            }
        }
    }

### Key points about the code

- The list displays three items that are generated dynamically, with each being a [`ListItem`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/package-summary#ListItem(androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Function0,kotlin.Function0,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function0)).
- Each `ListItem` can be customized, and an icon can be added to it.