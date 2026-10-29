---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/compose/subspace-layouts
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/compose/subspace-layouts
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

A *subspace* is a partition of 3D space within your app where you can place 3D
content, build 3D layouts, and add depth to otherwise 2D content. A subspace is
rendered only when spatialization is enabled. In Home Space or on non-XR
devices, any code within a subspace is ignored.

There are multiple ways to create a subspace:

- Use a [`Subspace`](https://developer.android.com/reference/kotlin/androidx/xr/compose/spatial/Subspace.composable): This composable creates a new, independent spatial UI hierarchy. It doesn't inherit the spatial position, orientation, or scale of any parent `Subspace` it is nested within. A `Subspace` is automatically bound by the system's recommended content box. Using this composable, you can choose either to [create a standard subspace](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-subspace) that stays at a fixed position, or a [subspace that follows a target](https://developer.android.com/develop/xr/jetpack-xr-sdk/subspace-follow-target).
- Use a [`PlanarEmbeddedSubspace`](https://developer.android.com/reference/kotlin/androidx/xr/compose/spatial/PlanarEmbeddedSubspace.composable#PlanarEmbeddedSubspace(kotlin.Function1)): This composable can be placed within your app's UI hierarchy, letting you maintain layouts for 2D and spatial UI. `PlanarEmbeddedSubspace` respects the constraints and positioning of its parent. The 3D content placed inside it is then positioned relative to this 2D-defined area.

## Guides

This section includes the following developer guides:

- [Add a subspace](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-subspace)
- [Add a subspace that follows a target](https://developer.android.com/develop/xr/jetpack-xr-sdk/subspace-follow-target)
- [Understand subspace modifiers](https://developer.android.com/develop/xr/jetpack-xr-sdk/subspace-modifiers)