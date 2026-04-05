---
title: Lists in Jetpack Compose Glimmer  |  Android XR for Jetpack XR SDK  |  Android Developers
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/lists
source: html-scrape
---

The Android XR SDK has  [reached Developer Preview 3](https://android-developers.googleblog.com/2025/12/build-for-ai-glasses-with-android-xr.html), and we want your feedback! Try things out, and visit our [support page](/develop/xr/support) to reach out.

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android XR](https://developer.android.com/develop/xr)
* [Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk)
* [Guides](https://developer.android.com/develop/xr/get-started)

# Lists in Jetpack Compose Glimmer Stay organized with collections Save and categorize content based on your preferences.




Applicable XR devices

This guidance helps you build experiences for these types of XR devices.

[Learn about XR device types →](/develop/xr/devices)

![](/static/images/develop/xr/ai-glasses-icon.svg)


AI Glasses

[Learn about XR device types →](/develop/xr/devices)

In Jetpack Compose Glimmer, lists are vertically scrollable UI components that
efficiently render only visible items, designed to provide specific behaviors
and input compatibility for AI glasses apps. Jetpack Compose Glimmer
accomplishes this using the [`VerticalList`](/reference/kotlin/androidx/xr/glimmer/list/VerticalList.composable#VerticalList(androidx.compose.ui.Modifier,androidx.xr.glimmer.list.ListState,androidx.compose.foundation.layout.PaddingValues,kotlin.Boolean,androidx.compose.foundation.OverscrollEffect,androidx.compose.foundation.gestures.FlingBehavior,kotlin.Boolean,androidx.compose.ui.Alignment.Horizontal,androidx.compose.foundation.layout.Arrangement.Vertical,kotlin.Function1)) and [`ListItem`](/reference/kotlin/androidx/xr/glimmer/ListItem.composable#ListItem(androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Function0,kotlin.Function0,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function0)) components.

![](/static/images/design/ui/glasses/guides/glasses_components_lists.png)


**Figure 1.** An example of some different styles of lists in Jetpack Compose Glimmer.

The [`VerticalList`](/reference/kotlin/androidx/xr/glimmer/list/VerticalList.composable#VerticalList(androidx.compose.ui.Modifier,androidx.xr.glimmer.list.ListState,androidx.compose.foundation.layout.PaddingValues,kotlin.Boolean,androidx.compose.foundation.OverscrollEffect,androidx.compose.foundation.gestures.FlingBehavior,kotlin.Boolean,androidx.compose.ui.Alignment.Horizontal,androidx.compose.foundation.layout.Arrangement.Vertical,kotlin.Function1)) is Jetpack Compose Glimmer's component for displaying
scrollable vertical content. It offers the same API functionality as
[`LazyColumn`](/reference/kotlin/androidx/compose/foundation/lazy/LazyColumn.composable#LazyColumn(androidx.compose.ui.Modifier,androidx.compose.foundation.lazy.LazyListState,androidx.compose.foundation.layout.PaddingValues,kotlin.Boolean,androidx.compose.foundation.layout.Arrangement.Vertical,androidx.compose.ui.Alignment.Horizontal,androidx.compose.foundation.gestures.FlingBehavior,kotlin.Boolean,androidx.compose.foundation.OverscrollEffect,kotlin.Function1)) but with behaviors specifically optimized for Jetpack Compose
Glimmer and AI glasses with a display.

**Warning:** Don't use `LazyColumn` in your AI glasses activities.

Jetpack Compose Glimmer lists have a few unique constraints:

* Lists should only show three items or less within a view.
* When a list contains more items than can fit within a view, a black scrim is
  used near the list's bounds.

## Example: Display a vertical list with three items

The following code shows how to use a [`VerticalList`](/reference/kotlin/androidx/xr/glimmer/list/VerticalList.composable#VerticalList(androidx.compose.ui.Modifier,androidx.xr.glimmer.list.ListState,androidx.compose.foundation.layout.PaddingValues,kotlin.Boolean,androidx.compose.foundation.OverscrollEffect,androidx.compose.foundation.gestures.FlingBehavior,kotlin.Boolean,androidx.compose.ui.Alignment.Horizontal,androidx.compose.foundation.layout.Arrangement.Vertical,kotlin.Function1)) and [`ListItem`](/reference/kotlin/androidx/xr/glimmer/ListItem.composable#ListItem(androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Function0,kotlin.Function0,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function0))
components to create a list of three items:

```
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
```

### Key points about the code

* The list displays three items that are generated dynamically, with each
  being a [`ListItem`](/reference/kotlin/androidx/xr/glimmer/ListItem.composable#ListItem(androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Function0,kotlin.Function0,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function0)).
* Each `ListItem` can be customized, and an icon can be added to it.