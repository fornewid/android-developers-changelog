---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/list-items
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/list-items
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/ai-glasses-icon.svg) Display Glasses [](https://developer.android.com/develop/xr/devices#audio-display) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

In Jetpack Compose Glimmer, the [`ListItem`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/ListItem.composable) is the standard component for
displaying a single row of content. List items are designed for the focus-based
interaction of display glasses, so they provide a built-in visual response upon
gaining focus.

The component has two overloads: one with an `onClick` parameter for items that
trigger actions, and a focusable-only version for informational content that
does not require a click action.
![](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_components_lists.png) **Figure 1.** An example of two lists with different styles of list items in Jetpack Compose Glimmer.

## Usage within lists

List items are the primary choice for rows within a [list](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/lists), however lists can
also host other components, such as a [`Card`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/Card.composable) or [`TitleChip`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/TitleChip.composable), to
provide different visual emphasis.

List items use `headlineContent` slot for their primary text to align with
`Card` and `TitleChip` components that are used for other items.

## Example: List item with a supporting label and icons

The following code creates a list item with a supporting label and both leading
and trailing icons:


```kotlin
@Composable
private fun ListItemWithSupportingLabelAndIcons() {
    ListItem(
        supportingLabel = { Text("Supporting Label") },
        leadingIcon = { Icon(FavoriteIcon, "Localized description") },
        trailingIcon = { Icon(FavoriteIcon, "Localized description") },
    ) {
        Text("Primary Label")
    }
}
```

<br />