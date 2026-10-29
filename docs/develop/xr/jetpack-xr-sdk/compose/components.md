---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/compose/components
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/compose/components
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

Jetpack Compose for XR includes a variety of *spatialized components* to help
you build spatial UI and layouts for your app.

## Subspace composables

*Subspace composables* are a special type of spatialized components that can
only be rendered in a [subspace](https://developer.android.com/develop/xr/jetpack-xr-sdk/compose/subspace-layouts) and must be enclosed within `Subspace`
before being placed within a 2D layout. A [`SubspaceModifier`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/layout/SubspaceModifier) lets you add
attributes like [depth, offset, and positioning](https://developer.android.com/develop/xr/jetpack-xr-sdk/subspace-modifiers) to your subspace
composables.

## Other spatialized components

Other spatialized components don't require being called inside a subspace. They
consist of conventional 2D elements wrapped within a spatial container. These
elements can be used within 2D or 3D layouts if defined for both. When
spatialization is not enabled, their spatialized features will be ignored and
they will fall back to their 2D counterparts.

Spatialized components can be placed anywhere in your app's UI hierarchy. These
elements can be reused in your 2D UI, and their spatial attributes are only
visible when spatial capabilities are enabled. This lets you add elevation to
menus, dialogs, and other components without the need to write your code twice.
Here are some examples of how different spatialized components change their
behavior when spatialization is enabled or not:

| **Spatialized component** | **When spatialization is enabled** | **In 2D environment** |
|---|---|---|
| `SpatialDialog` | Panel pushes slightly back in z-depth to display an elevated dialog | Falls back to 2D [`Dialog`](https://developer.android.com/reference/kotlin/androidx/compose/ui/window/Dialog.composable#Dialog(kotlin.Function0,androidx.compose.ui.window.DialogProperties,kotlin.Function0)). |
| `SpatialPopup` | Panel pushes slightly back in z-depth to display an elevated popup | Falls back to a 2D [`Popup`](https://developer.android.com/reference/kotlin/androidx/compose/ui/window/Popup.composable#Popup(androidx.compose.ui.window.PopupPositionProvider,kotlin.Function0,androidx.compose.ui.window.PopupProperties,kotlin.Function0)). |
| `SpatialElevation` | `SpatialElevationLevel` can be set to add elevation. | Shows without spatial elevation. |

## Guides

This section includes the following developer guides:

- [Orbiter](https://developer.android.com/develop/xr/jetpack-xr-sdk/compose/orbiter)
- [SceneCore entity](https://developer.android.com/develop/xr/jetpack-xr-sdk/compose/scene-core-entity)
- [Spatial dialog](https://developer.android.com/develop/xr/jetpack-xr-sdk/compose/spatial-dialog)
- [Spatial external surface](https://developer.android.com/develop/xr/jetpack-xr-sdk/compose/spatial-external-surface)
- [Spatial panel](https://developer.android.com/develop/xr/jetpack-xr-sdk/compose/spatial-panel)