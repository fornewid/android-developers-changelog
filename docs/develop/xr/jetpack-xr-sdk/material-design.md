---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/material-design
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/material-design
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

Material Design provides components and layouts for XR. Using the [Material 3
library](https://developer.android.com/jetpack/androidx/releases/compose-material3), [adaptive layouts](https://developer.android.com/jetpack/androidx/releases/compose-material3-adaptive), and the [XR Compose Material 3 library](https://developer.android.com/jetpack/androidx/releases/xr-compose-material3#declaring_dependencies),
you can build spatial UI behaviors into your Compose app.
Alas, your browser doesn't support HTML5 video. That's OK! You can still [download the
video](https://developer.android.com/static/videos/design/ui/xr/visual-design-ls-adapted-opt.mp4) and watch it with a video player.

Add the [XR Compose Material 3 library](https://developer.android.com/jetpack/androidx/releases/xr-compose-material3#declaring_dependencies) to your app's dependencies to use
Material 3 for XR components, or place standard [Material 3](https://developer.android.com/jetpack/androidx/releases/compose-material3) components
directly inside Jetpack Compose for XR containers such as [`Orbiter`](https://developer.android.com/develop/xr/jetpack-xr-sdk/compose/orbiter),
[`SpatialDialog`](https://developer.android.com/develop/xr/jetpack-xr-sdk/compose/spatial-dialog), and [`SpatialPanel`](https://developer.android.com/develop/xr/jetpack-xr-sdk/compose/spatial-panel).

## Use Material 3 for XR components

The [`androidx.xr.compose.material3`](https://developer.android.com/reference/kotlin/androidx/xr/compose/material3/package-summary) library provides Material 3 for XR
components for common spatial UI patterns---including navigation rails and bars,
top app bars, floating toolbars, dialogs, list-detail layouts, and a toggle
button to switch between Home Space and Full Space. The spatialized `Spatial*`
composables in this library are experimental and require opting in with
[`@OptIn(ExperimentalMaterial3XrApi::class)`](https://developer.android.com/reference/kotlin/androidx/xr/compose/material3/ExperimentalMaterial3XrApi).

Check [`LocalSpatialCapabilities.current.isSpatialUiEnabled`](https://developer.android.com/reference/kotlin/androidx/xr/compose/platform/package-summary#LocalSpatialCapabilities()) to render
Material 3 for XR components when spatial UI is enabled and standard Material 3
components when spatial UI isn't enabled. For more information, see [Check for
spatial capabilities](https://developer.android.com/develop/xr/jetpack-xr-sdk/check-spatial-capabilities).

## Navigation rail

Use [`SpatialNavigationRail`](https://developer.android.com/reference/kotlin/androidx/xr/compose/material3/SpatialNavigationRail.composable) or [`SpatialWideNavigationRail`](https://developer.android.com/reference/kotlin/androidx/xr/compose/material3/SpatialWideNavigationRail.composable) to display
a Material 3 navigation rail in a start-aligned [`Orbiter`](https://developer.android.com/develop/xr/jetpack-xr-sdk/compose/orbiter) when spatial UI
is enabled. For more information, see the [Material Design
guidelines](https://m3.material.io/components/navigation-rail/xr).


![Non-spatialized navigation
rail](https://developer.android.com/static/images/design/ui/xr/guides/spatial-ui-nav-rail-1.jpg)

Non-spatialized navigation rail
![Spatialized (XR-adapted) navigation
rail](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/material-design/navigation-rail-spatial.jpg)

Spatialized (XR-adapted) navigation rail

<br />

## Navigation bar

Use [`SpatialNavigationBar`](https://developer.android.com/reference/kotlin/androidx/xr/compose/material3/SpatialNavigationBar.composable) or [`SpatialShortNavigationBar`](https://developer.android.com/reference/kotlin/androidx/xr/compose/material3/SpatialShortNavigationBar.composable) to display
a Material 3 navigation bar in a bottom-aligned [`Orbiter`](https://developer.android.com/develop/xr/jetpack-xr-sdk/compose/orbiter) when spatial UI
is enabled. For more information, see the [Material Design
guidelines](https://m3.material.io/components/navigation-bar/xr).


![Non-spatialized navigation
bar](https://developer.android.com/static/images/design/ui/xr/guides/spatial-ui-nav-bar-1.jpg)

Non-spatialized navigation bar
![Spatialized (XR-adapted) navigation
bar](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/material-design/navigation-bar-spatial.jpg)

Spatialized (XR-adapted) navigation bar

<br />

## Dialogs

Use [`SpatialBasicAlertDialog`](https://developer.android.com/reference/kotlin/androidx/xr/compose/material3/SpatialBasicAlertDialog.composable) to display a basic alert dialog inside a
[`SpatialDialog`](https://developer.android.com/develop/xr/jetpack-xr-sdk/compose/spatial-dialog) with spatial elevation, or wrap standard Material 3 dialog
content directly in `SpatialDialog`.

For more information, see [Dialogs](https://m3.material.io/components/dialogs/xr) and the [adaptive design
guidelines](https://m3.material.io/foundations/adaptive-design).


![Non-spatialized
dialog](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/material-design/alert-dialog-non-spatial.png)

Non-spatialized dialog
![Spatialized (XR-adapted)
dialog](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/material-design/alert-dialog-spatial.png)

Spatialized (XR-adapted) dialog

<br />

## Top app bars

Use [`SpatialTopAppBar`](https://developer.android.com/reference/kotlin/androidx/xr/compose/material3/SpatialTopAppBar.composable) or [`SpatialTwoRowsTopAppBar`](https://developer.android.com/reference/kotlin/androidx/xr/compose/material3/SpatialTwoRowsTopAppBar.composable) to display a
Material 3 top app bar inside a top-aligned [`Orbiter`](https://developer.android.com/develop/xr/jetpack-xr-sdk/compose/orbiter) when spatial UI is
enabled.

For more information, see [Top app bars](https://m3.material.io/components/app-bars/xr) and the [adaptive
design guidelines](https://m3.material.io/foundations/adaptive-design).


![Non-spatialized top app
bar](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/material-design/top-app-bar-non-spatial.png)

Non-spatialized top app bar
![Spatialized (XR-adapted) top app
bar](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/material-design/top-app-bar-spatial.jpg)

Spatialized (XR-adapted) top app bar

<br />

## List-detail layout for XR

Use [`SpatialListDetailPaneScaffold`](https://developer.android.com/reference/kotlin/androidx/xr/compose/material3/SpatialListDetailPaneScaffold.composable) when spatial UI is enabled to display
a [Material 3 adaptive](https://developer.android.com/jetpack/androidx/releases/compose-material3-adaptive) list-detail layout where each pane is placed inside
its own [`SpatialPanel`](https://developer.android.com/develop/xr/jetpack-xr-sdk/compose/spatial-panel). When spatial UI isn't enabled, use
[`ListDetailPaneScaffold`](https://developer.android.com/develop/ui/compose/layouts/adaptive/list-detail). For more information, see [List-detail
layout](https://developer.android.com/develop/ui/compose/layouts/adaptive/list-detail) and the [adaptive design guidelines](https://m3.material.io/foundations/adaptive-design).


![Non-spatialized
ListDetailPaneScaffold](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/material-design/list-non-spatial-panel.jpg)

Non-spatialized ListDetailPaneScaffold
![Spatialized (XR-adapted)
ListDetailPaneScaffold](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/material-design/list-spatial-panel.jpg)

Spatialized (XR-adapted) ListDetailPaneScaffold

<br />

## Support pane layout for XR

When spatial UI is enabled, place your main pane and supporting pane into
separate [`SpatialPanel`](https://developer.android.com/develop/xr/jetpack-xr-sdk/compose/spatial-panel) containers inside a [`SpatialRow`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/SpatialRow.composable) within a
[`Subspace`](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-subspace). When spatial UI isn't enabled, use
[`SupportingPaneScaffold`](https://developer.android.com/develop/ui/compose/layouts/adaptive/build-a-supporting-pane-layout). For more information, see [Supporting pane](https://developer.android.com/develop/ui/compose/layouts/adaptive/build-a-supporting-pane-layout)
and the [adaptive design guidelines](https://m3.material.io/foundations/adaptive-design).


![Non-spatialized
SupportingPaneScaffold](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/material-design/supporting-non-spatial-panel.jpg)

Non-spatialized SupportingPaneScaffold
![Spatialized (XR-adapted)
SupportingPaneScaffold](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/material-design/supporting-spatial-panel.jpg)

Spatialized (XR-adapted) SupportingPaneScaffold

<br />

## Start designing with the Material 3 Design Kit for Figma

![Collage of elements from the Material 3 Design Kit](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/material-design/material-3-design-kit.jpg)

[Download the Material 3 Design Kit to get started](https://www.figma.com/community/file/1035203688168086460)

## See also

- [Develop UI with Jetpack Compose for XR](https://developer.android.com/develop/xr/jetpack-xr-sdk/ui-compose)
- [Transition from Home Space to Full Space](https://developer.android.com/develop/xr/jetpack-xr-sdk/transition-home-space-to-full-space)
- [Spatial UI design guidelines](https://developer.android.com/design/ui/xr/guides/spatial-ui)