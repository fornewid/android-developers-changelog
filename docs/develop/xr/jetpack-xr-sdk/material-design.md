---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/material-design
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/material-design
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

Material Design provides components and layouts that adapt for XR. Using the
existing [Material 3 library](https://developer.android.com/jetpack/androidx/releases/compose-material3), components and [adaptive layouts](https://developer.android.com/jetpack/androidx/releases/compose-material3-adaptive) are
enhanced with spatial UI behaviors.
Alas, your browser doesn't support HTML5 video. That's OK! You can still [download the
video](https://developer.android.com/static/videos/design/ui/xr/visual-design-ls-adapted-opt.mp4) and watch it with a video player.

## Navigation rail

Navigation rail in any Compose layout, including [`NavigationSuiteScaffold`](https://developer.android.com/develop/ui/compose/layouts/adaptive/build-adaptive-navigation)
will automatically adapt to XR Orbiter. For more information, read [Material
Design guidelines](https://m3.material.io/components/navigation-rail/xr).


![Non-spatialized navigation
rail](https://developer.android.com/static/images/design/ui/xr/guides/spatial-ui-nav-rail-1.jpg)

Non-spatialized navigation rail
![Spatialized (XR-adapted) navigation
rail](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/material-design/navigation-rail-spatial.jpg)

Spatialized (XR-adapted) navigation rail

<br />

## Navigation bar

Navigation bar in any Compose layout, including [`NavigationSuiteScaffold`](https://developer.android.com/develop/ui/compose/layouts/adaptive/build-adaptive-navigation)
will automatically adapt to XR orbiter. For more information, read [Material
Design guidelines](https://m3.material.io/components/navigation-bar/xr).


![Non-spatialized navigation
bar](https://developer.android.com/static/images/design/ui/xr/guides/spatial-ui-nav-bar-1.jpg)

Non-spatialized navigation bar
![Spatialized (XR-adapted) navigation
bar](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/material-design/navigation-bar-spatial.jpg)

Spatialized (XR-adapted) navigation bar

<br />

## Dialogs

A `BasicAlertDialog` will adapt to XR, adding elevation to the component.

Learn more about [Dialogs](https://m3.material.io/components/dialogs/xr) and [adaptive design guidelines](https://m3.material.io/foundations/adaptive-design).


![Non-spatialized
dialog](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/material-design/alert-dialog-non-spatial.png)

Non-spatialized dialog
![Spatialized (XR-adapted)
dialog](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/material-design/alert-dialog-spatial.png)

Spatialized (XR-adapted) dialog

<br />

## Top app bars

A `TopAppBar` will automatically adapt to XR orbiter.

Learn more about [Top app bars](https://m3.material.io/components/app-bars/xr) and [adaptive design
guidelines](https://m3.material.io/foundations/adaptive-design).


![Non-spatialized top app
bar](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/material-design/top-app-bar-non-spatial.png)

Non-spatialized top app bar
![Spatialized (XR-adapted) top app
bar](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/material-design/top-app-bar-spatial.jpg)

Spatialized (XR-adapted) top app bar

<br />

## List-detail layout for XR

[Compose Material 3 Adaptive Layouts](https://developer.android.com/jetpack/androidx/releases/compose-material3-adaptive) in XR have a 1:1 mapping where each
pane is placed inside its own XR spatial panel. Learn more about
[`ListDetailPaneScaffold`](https://developer.android.com/develop/ui/compose/layouts/adaptive/list-detail) and [adaptive design guidelines](https://m3.material.io/foundations/adaptive-design).


![Non-spatialized
ListDetailPaneScaffold](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/material-design/list-non-spatial-panel.jpg)

Non-spatialized ListDetailPaneScaffold
![Spatialized (XR-adapted)
ListDetailPaneScaffold](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/material-design/list-spatial-panel.jpg)

Spatialized (XR-adapted) ListDetailPaneScaffold

<br />

## Support pane layout for XR

[Compose Material 3 Adaptive Layouts](https://developer.android.com/jetpack/androidx/releases/compose-material3-adaptive) in XR have a 1:1 mapping where each
pane is placed inside its own XR spatial panel. Learn more about
[`SupportingPaneScaffold`](https://developer.android.com/develop/ui/compose/layouts/adaptive/build-a-supporting-pane-layout) and [adaptive design guidelines](https://m3.material.io/foundations/adaptive-design).


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

- [Develop UI with Jetpack Compose for XR](https://developer.android.com/develop/xr/jetpack-xr-sdk/develop-ui)
- [Spatial UI design guidelines](https://developer.android.com/design/ui/xr/guides/spatial-ui)