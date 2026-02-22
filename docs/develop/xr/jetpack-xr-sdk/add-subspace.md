---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/add-subspace
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/add-subspace
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

A subspace is a partition of 3D space within your app where you can place 3D
models, build 3D layouts, and add depth to otherwise 2D content. A subspace is
rendered only when spatialization is enabled. In Home Space or on non-XR
devices, any code within that subspace is ignored.

You can use subspace composables like [`SpatialPanel`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/package-summary#SpatialPanel(androidx.xr.compose.subspace.layout.SubspaceModifier,androidx.xr.compose.subspace.layout.SpatialShape,androidx.xr.compose.subspace.DragPolicy,androidx.xr.compose.subspace.ResizePolicy,androidx.xr.compose.subspace.layout.InteractionPolicy,kotlin.Function0)), [`SpatialRow`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/package-summary#SpatialRow(androidx.xr.compose.subspace.layout.SubspaceModifier,androidx.xr.compose.subspace.layout.SpatialAlignment,androidx.xr.compose.subspace.layout.SpatialArrangement.Horizontal,kotlin.Function1)),
and [`SpatialColumn`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/package-summary#SpatialColumn(androidx.xr.compose.subspace.layout.SubspaceModifier,androidx.xr.compose.subspace.layout.SpatialAlignment,androidx.xr.compose.subspace.layout.SpatialArrangement.Vertical,kotlin.Function1)) to create your layout and place 2D content in 3D
space. For placing 3D content, use the appropriate Subspace Composable like
[`SceneCoreEntity`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/package-summary#SceneCoreEntity(kotlin.Function0,androidx.xr.compose.subspace.layout.SubspaceModifier,kotlin.Function1,androidx.xr.compose.subspace.SceneCoreEntitySizeAdapter,kotlin.Function0)) for 3D models and [`SpatialExternalSurface`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/package-summary#SpatialExternalSurface(androidx.xr.compose.subspace.StereoMode,androidx.xr.compose.subspace.layout.SubspaceModifier,androidx.xr.compose.subspace.layout.SpatialFeatheringEffect,androidx.xr.compose.subspace.SurfaceProtection,androidx.xr.compose.subspace.DragPolicy,androidx.xr.compose.subspace.ResizePolicy,androidx.xr.compose.subspace.layout.InteractionPolicy,kotlin.Function1)) for
stereo images. Some XR components such as [`Orbiter`](https://developer.android.com/reference/kotlin/androidx/xr/compose/spatial/package-summary#Orbiter(androidx.xr.compose.spatial.ContentEdge.Horizontal,androidx.compose.ui.unit.Dp,androidx.xr.compose.spatial.OrbiterOffsetType,androidx.compose.ui.Alignment.Horizontal,androidx.xr.compose.subspace.layout.SpatialShape,androidx.compose.ui.unit.Dp,kotlin.Boolean,kotlin.Function0)) or [`SpatialDialog`](https://developer.android.com/reference/kotlin/androidx/xr/compose/spatial/package-summary#SpatialDialog(kotlin.Function0,androidx.xr.compose.spatial.SpatialDialogProperties,kotlin.Function0))
are standard 2D composables that can be used anywhere in your 2D UI hierarchy,
but a [`SubspaceComposable`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/SubspaceComposable) must be invoked in your app's subspace. To do
this, use the [`Subspace`](https://developer.android.com/reference/kotlin/androidx/xr/compose/spatial/package-summary#Subspace(kotlin.Function1)) subspace composable.

## About subspace hierarchies

The top-level [`Subspace`](https://developer.android.com/reference/kotlin/androidx/xr/compose/spatial/package-summary#Subspace(kotlin.Function1)) is the outermost subspace invoked by your app.
Each call to a [`Subspace`](https://developer.android.com/reference/kotlin/androidx/xr/compose/spatial/package-summary#Subspace(kotlin.Function1)) creates a new, independent Spatial UI hierarchy.
It does not inherit the spatial position, orientation, or scale of any parent
`Subspace` it is nested within.

To create an embedded or nested `Subspace` within a `SpatialPanel`, `Orbiter`,
`SpatialPopup`, or other component, use [`PlanarEmbeddedSubspace`](https://developer.android.com/reference/kotlin/androidx/xr/compose/spatial/package-summary#PlanarEmbeddedSubspace(kotlin.Function1)).

[`PlanarEmbeddedSubspace`](https://developer.android.com/reference/kotlin/androidx/xr/compose/spatial/package-summary#PlanarEmbeddedSubspace(kotlin.Function1)) has two key differences from [`Subspace`](https://developer.android.com/reference/kotlin/androidx/xr/compose/spatial/package-summary#Subspace(kotlin.Function1)):

- They participate in the 2D layout in which they are invoked. This means that the height and width of the subspace will be constrained by the height and width of its 2D parent layout.
- They behave as children of the entity they're invoked in. This means that, if you call a subspace composable nested inside of a [`SpatialPanel`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/package-summary#SpatialPanel(androidx.xr.compose.subspace.layout.SubspaceModifier,androidx.xr.compose.subspace.layout.SpatialShape,androidx.xr.compose.subspace.DragPolicy,androidx.xr.compose.subspace.ResizePolicy,androidx.xr.compose.subspace.layout.InteractionPolicy,kotlin.Function0)), that subspace is a child of the [`SpatialPanel`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/package-summary#SpatialPanel(androidx.xr.compose.subspace.layout.SubspaceModifier,androidx.xr.compose.subspace.layout.SpatialShape,androidx.xr.compose.subspace.DragPolicy,androidx.xr.compose.subspace.ResizePolicy,androidx.xr.compose.subspace.layout.InteractionPolicy,kotlin.Function0)) it's called in.

These behaviors of [`PlanarEmbeddedSubspace`](https://developer.android.com/reference/kotlin/androidx/xr/compose/spatial/package-summary#PlanarEmbeddedSubspace(kotlin.Function1)) enable capabilities such as:

- Moving the child with the parent entity
- Offsetting the location of the child using the offset [`SubspaceModifier`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/layout/SubspaceModifier)
- Presenting a 3D object that hovers above your 2D UI and matches the height and width of the appropriate space in the 2D layout

## Adapt layouts for a subspace

On Android XR, your app's layout is bound to the `VolumeConstraints` of [`Subspace`](https://developer.android.com/reference/kotlin/androidx/xr/compose/spatial/package-summary#Subspace(kotlin.Function1))
in Full Space Mode by default. Because of this, you should consider the amount of visible space
available to the user and adjust your layout accordingly. The
[`recommendedContentBoxInFullSpace`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/ActivitySpace#recommendedContentBoxInFullSpace()) provides the specific dimensions for
the bounding box inside the [`ActivitySpace`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/ActivitySpace) so that content can be placed
within the user's field of view.

Your app's primary content should fit within this box. If you have content that
must exceed the recommended bounds, consider a layout that encourages users to
explore the space by moving their head. The default constraint of the
[`recommendedContentBoxInFullSpace`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/ActivitySpace#recommendedContentBoxInFullSpace()) can be overridden by applying a
custom size-based modifier such as `SubspaceModifier.requiredSizeIn`. For unbounded behavior, set `allowUnboundedSubspace = true`.

Call [`recommendedContentBoxInFullSpace`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/ActivitySpace#recommendedContentBoxInFullSpace()) using the current [Session](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-session) to
get these specific dimensions as needed. See the following example:


```kotlin
val session = LocalSession.current
session?.scene?.activitySpace?.recommendedContentBoxInFullSpacehttps://github.com/android/snippets/blob/fbed24d5695413cfd86b4b2c6b6faf0a3a2eadb8/xr/src/main/java/com/example/xr/compose/Subspace.kt#L73-L74
```

<br />

## Add a subspace to your app

The following code example shows how to add [`Subspace`](https://developer.android.com/reference/kotlin/androidx/xr/compose/spatial/package-summary#Subspace(kotlin.Function1)) and
[`PlanarEmbeddedSubspace`](https://developer.android.com/reference/kotlin/androidx/xr/compose/spatial/package-summary#PlanarEmbeddedSubspace(kotlin.Function1)) to your app:


```kotlin
setContent {
    // This is a top-level subspace
    Subspace {
        SpatialPanel {
            MyComposable()
        }
    }
}
```

<br />


```kotlin
@Composable
private fun MyComposable() {
    Row {
        PrimaryPane()
        SecondaryPane()
    }
}

@Composable
private fun PrimaryPane() {
    // This is an embedded subspace, because PrimaryPane is in a SpatialPanel
    // and that SpatialPanel is in the top-level Subspace
    PlanarEmbeddedSubspace {
        SpatialPanel {}
    }
}
```

<br />

See the full reference documentation on [`Subspace`](https://developer.android.com/reference/kotlin/androidx/xr/compose/spatial/package-summary#Subspace(kotlin.Function1)) and
[`PlanarEmbeddedSubspace`](https://developer.android.com/reference/kotlin/androidx/xr/compose/spatial/package-summary#PlanarEmbeddedSubspace(kotlin.Function1)) for more details.