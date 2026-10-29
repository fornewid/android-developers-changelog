---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/compose/scene-core-entity
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/compose/scene-core-entity
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

A [`SceneCoreEntity`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/SceneCoreEntity.composable) is a [subspace composable](https://developer.android.com/develop/xr/jetpack-xr-sdk/compose/components#subspace-composables) that bridges the
[Jetpack SceneCore](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/package-summary) and [Compose for XR](https://developer.android.com/reference/kotlin/androidx/xr/compose/spatial/package-summary) libraries so that you can use
entities built with SceneCore in Compose layouts. This lets you build
lower-level entities and custom components while allowing Compose to size,
position, reparent, add children, and apply modifiers to those entities.

## Use a SceneCore entity to place entities in your layout

The following example shows how to use a SceneCore entity to place entities in
your layout:


```kotlin
val virtualPixelDensity = session.scene.virtualPixelDensity

Subspace {
    SceneCoreEntity(
        modifier = SubspaceModifier.offset(x = 50.dp),
        factory = {
            SurfaceEntity.create(
                session = session,
                pose = Pose.Identity,
                stereoMode = SurfaceEntity.StereoMode.MONO
            )
        },
        update = { entity ->
            // Compose state changes may be applied to the SceneCore entity here.
            entity.stereoMode = SurfaceEntity.StereoMode.SIDE_BY_SIDE
        },
        sizeAdapter =
            object : SceneCoreEntitySizeAdapter<SurfaceEntity> {
                override fun onLayoutSizeChanged(
                    entity: SurfaceEntity,
                    size: IntVolumeSize
                ) {
                    val extents = FloatSize2d(
                        size.width.toFloat(),
                        size.height.toFloat()
                    )
                    entity.shape = SurfaceEntity.Shape.Quad(extents)
                }
            },
    ) {
        // Content here will be children of the SceneCoreEntity
        // in the scene graph.
    }
}
```

<br />

### Key points about the code

- Factory block: The factory block is where you initialize the underlying [`SurfaceEntity`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/SurfaceEntity) entity from SceneCore.
- Update block: Use the update block to modify the entity's properties in response to changes in your Compose state.
- Size Adaptation: The `sizeAdapter` communicates the entity's dimensions back to the Compose layout system.

### Additional information

- See [Add 3D models to your app](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-3d-models) to better understand how to load 3D content within a `SceneCoreEntity`.