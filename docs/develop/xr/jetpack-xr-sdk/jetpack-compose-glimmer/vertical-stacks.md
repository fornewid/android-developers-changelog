---
title: Vertical stacks in Jetpack Compose Glimmer  |  Android XR for Jetpack XR SDK  |  Android Developers
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/vertical-stacks
source: html-scrape
---

The Android XR SDK has  [reached Developer Preview 4](https://android-developers.googleblog.com/2026/05/android-xr-sdk-developer-preview-4-updates.html), and we want your feedback! Try things out, and visit our [support page](/develop/xr/support) to reach out.

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android XR](https://developer.android.com/develop/xr)
* [Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk)
* [Guides](https://developer.android.com/develop/xr/get-started)

# Vertical stacks in Jetpack Compose Glimmer Stay organized with collections Save and categorize content based on your preferences.





Applicable XR devices

This guidance helps you build experiences for these types of XR devices.

[Learn about XR device types →](/develop/xr/devices)

![](/static/images/develop/xr/ai-glasses-icon.svg)


Display Glasses

[Learn about XR device types →](/develop/xr/devices)

In Jetpack Compose Glimmer, the [`VerticalStack`](/reference/kotlin/androidx/xr/glimmer/stack/VerticalStack.composable) is a lazy, vertically
scrollable layout that arranges items in a visually overlapping,
three-dimensional sequence. The primary item is prominently displayed in the
foreground, while subsequent items are positioned behind it.

![](/static/images/design/ui/glasses/guides/glasses_components_stacks.png)


**Figure 1.** An example of some different styles of stacks in Jetpack Compose Glimmer.

## Scrolling and positioning behaviors

Because stacks keep items arranged in a compact, overlapping layout, they have
some behaviors that are different from other types of sequenced components, such
as [lists](/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/lists):

* As a user scrolls vertically, the active foreground item transitions out of
  view, allowing the item immediately beneath it to slide into the prominent
  foreground position.
* Items always snap-animate using a specialized spring animation into the
  foreground position after a user's gesture ends.
* Items are positioned along the z-axis, with items further in the list placed
  behind the primary item.

## Focus management

The `VerticalStack` uses a specialized focus system to ensure that the current
foreground item is always the primary target for user interaction:

* **Initial focus and re-entry**: Initial focus and focus re-entry goes to the
  current top item of the stack.
* **Auto-focus notification**: As items transition, the stack requests focus
  for the top item.
* **Focus tracking**: Each item uses `onFocusChanged` to notify the
  `StackState` of its individual focus status.

## Example: Create a vertical stack

The following code creates a vertical stack with a few card items:

```
@Composable
fun VerticalStackSample() {
    VerticalStack {
        item {
            Card { Text("Top Card") }
        }
        item {
            Card { Text("Second Card") }
        }
        item {
            Card { Text("Third Card") }
        }
    }
}

StackSamples.kt
```