---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/ui-compose
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/ui-compose
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

With Jetpack Compose for XR, you can use spatialized components like [rows](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/SpatialRow.composable)
and [columns](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/SpatialColumn.composable) to build spatial UI and layouts using a [familiar, declarative
Compose model](https://developer.android.com/develop/ui/compose/layouts/basics). This lets you [extend your existing Android UI into 3D
space](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-xr-to-existing) or build entirely new immersive 3D apps.

This library also provides [subspace composeables](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/SubspaceComposable), such as [spatial
panels](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/SpatialPanel.composable) and [orbiters](https://developer.android.com/reference/kotlin/androidx/xr/compose/spatial/Orbiter.composable), which let you place your existing 2D Compose or
Views-based UI in a spatial layout. Other subspace composeables handle other
types of spatial use cases, such as [`SceneCoreEntity`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/SceneCoreEntity.composable) that lets you [place
entities](https://developer.android.com/develop/xr/jetpack-xr-sdk/ui-compose#use-scenecoreentity) like 3D models relative to your UI.
![Develop UI XR components orbiter generic example](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/index/develop-ui-xr-component-orbiter-generic.jpg)

## Guides

This section includes the following developer guides:

### Layout components

- [Overview](https://developer.android.com/develop/xr/jetpack-xr-sdk/compose/components)
- [Orbiter](https://developer.android.com/develop/xr/jetpack-xr-sdk/compose/orbiter)
- [SceneCore entity](https://developer.android.com/develop/xr/jetpack-xr-sdk/compose/scene-core-entity)
- [Spatial dialog](https://developer.android.com/develop/xr/jetpack-xr-sdk/compose/spatial-dialog)
- [Spatial external surface](https://developer.android.com/develop/xr/jetpack-xr-sdk/compose/spatial-external-surface)
- [Spatial gLTF model](https://developer.android.com/develop/xr/jetpack-xr-sdk/compose/spatial-gltf-model)
- [Spatial panel](https://developer.android.com/develop/xr/jetpack-xr-sdk/compose/spatial-panel)

### Material Design for spatial UI

- [Implement Material Design for XR](https://developer.android.com/develop/xr/jetpack-xr-sdk/material-design)

### Working with existing Views-based layouts

- [Build spatial UI for existing Android Views-based apps](https://developer.android.com/develop/xr/jetpack-xr-sdk/develop-ui-views)