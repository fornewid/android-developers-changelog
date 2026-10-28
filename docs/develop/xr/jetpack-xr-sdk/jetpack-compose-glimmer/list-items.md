---
title: List items in Jetpack Compose Glimmer  |  Android XR for Jetpack XR SDK  |  Android Developers
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/list-items
source: html-scrape
---

The Android XR SDK has  [reached Developer Preview 4](https://android-developers.googleblog.com/2026/05/android-xr-sdk-developer-preview-4-updates.html), and we want your feedback! Try things out, and visit our [support page](/develop/xr/support) to reach out.

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android XR](https://developer.android.com/develop/xr)
* [Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk)
* [Guides](https://developer.android.com/develop/xr/get-started)

# List items in Jetpack Compose Glimmer Stay organized with collections Save and categorize content based on your preferences.





Applicable XR devices

This guidance helps you build experiences for these types of XR devices.

[Learn about XR device types →](/develop/xr/devices)

![](/static/images/develop/xr/ai-glasses-icon.svg)


Display Glasses

[Learn about XR device types →](/develop/xr/devices)

In Jetpack Compose Glimmer, the [`ListItem`](/reference/kotlin/androidx/xr/glimmer/ListItem.composable) is the standard component for
displaying a single row of content. List items are designed for the focus-based
interaction of display glasses, so they provide a built-in visual response upon
gaining focus.

The component has two overloads: one with an `onClick` parameter for items that
trigger actions, and a focusable-only version for informational content that
does not require a click action.

![](/static/images/design/ui/glasses/guides/glasses_components_lists.png)


**Figure 1.** An example of two lists with different styles of list items in Jetpack Compose Glimmer.

## Usage within lists

List items are the primary choice for rows within a [list](/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/lists), however lists can
also host other components, such as a [`Card`](/reference/kotlin/androidx/xr/glimmer/Card.composable) or [`TitleChip`](/reference/kotlin/androidx/xr/glimmer/TitleChip.composable), to
provide different visual emphasis.

List items use `headlineContent` slot for their primary text to align with
`Card` and `TitleChip` components that are used for other items.

## Example: Basic list item

The following code creates a basic list item:

```
@Composable
fun ListItemSample() {
    ListItem { Text("This is a list item") }
}

ListItemSamples.kt
```

## Example: List item with a supporting label and icons

The following code creates a list item with a supporting label and both leading
and trailing icons:

```
@Composable
fun ListItemWithIconsSample() {
    ListItem(
        leadingIcon = { Icon(FavoriteIcon, contentDescription = "Favorite") },
        trailingIcon = { Icon(FavoriteIcon, contentDescription = "Favorite") }
    ) {
        Text("This is a list item with icons")
    }
}

ListItemSamples.kt
```