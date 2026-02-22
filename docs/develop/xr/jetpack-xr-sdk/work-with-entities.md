---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/work-with-entities
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/work-with-entities
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

The Jetpack XR SDK lets you use Jetpack SceneCore to create, control, and manage
[`Entity`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/Entity) instances such as [3D models](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-3d-models), [stereoscopic video](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-spatial-video), and
[`PanelEntity`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/PanelEntity) using Jetpack SceneCore.

Jetpack SceneCore adopts two common architectural patterns to support 3D
development: a [scene graph](https://en.wikipedia.org/wiki/Scene_graph) and an [entity-component
system](https://en.wikipedia.org/wiki/Entity_component_system) (ECS).

## Use the scene graph to create and control entities

To create and control objects in 3D space, you can use Jetpack SceneCore's
[Session](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-session) API to gain access to the scene graph. The scene graph aligns with
the user's real world and lets you organize 3D entities such as panels and 3D
models into a hierarchical structure, and hold the state of those entities.

Once you've gained access to the scene graph, you can use the APIs in Jetpack
Compose for XR to create spatial UI (for example, [`SpatialPanel`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/package-summary#SpatialPanel(androidx.xr.compose.subspace.layout.SubspaceModifier,androidx.xr.compose.subspace.layout.SpatialShape,androidx.xr.compose.subspace.DragPolicy,androidx.xr.compose.subspace.ResizePolicy,kotlin.Function0)) and
[`Orbiter`](https://developer.android.com/reference/kotlin/androidx/xr/compose/spatial/package-summary#Orbiter(androidx.xr.compose.spatial.ContentEdge.Horizontal,androidx.compose.ui.unit.Dp,androidx.xr.compose.spatial.OrbiterOffsetType,androidx.compose.ui.Alignment.Horizontal,androidx.xr.compose.subspace.layout.SpatialShape,androidx.compose.ui.unit.Dp,kotlin.Boolean,kotlin.Function0)) instances) within the scene graph. For 3D content such as 3D
models, you can access the Session directly. To learn more, see [About the
ActivitySpace](https://developer.android.com/develop/xr/jetpack-xr-sdk/work-with-entities#activityspace) on this page.

## Entity component system

An entity component system follows the principle of composition over
inheritance. You can expand the behavior of entities by attaching
behavior-defining components, which lets you apply the same behavior to
different types of entities. For more information, check out [Add common
behavior to entities](https://developer.android.com/develop/xr/jetpack-xr-sdk/work-with-entities#add-common) on this page.

## About the ActivitySpace

Each [`Session`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/Session) has an [`ActivitySpace`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/ActivitySpace) that is automatically created
with the `Session`. The `ActivitySpace` is the top-level `Entity` in the scene
graph.

The ActivitySpace represents a 3-dimensional space with a right-handed
coordinate system (the x-axis points to the right, the y-axis points up and the
z-axis back relative to the origin) and with meters for units that match the
real world. The origin for `ActivitySpace` is somewhat arbitrary (as users can
reset the position of the `ActivitySpace` within the real world), therefore it's
recommended to position content relative to each other instead of relative to
the origin.

## Work with Entities

Entities are central to SceneCore. Most everything the user sees and interacts
with are entities representing panels, 3D models and more.

Since the `ActivitySpace` is the top-level node of the scene graph, by default,
all new entities are placed directly into the `ActivitySpace`. You can relocate
entities along the scene graph by setting its [`parent`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/Entity#parent()) or by using
[`addChild()`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/Entity#addChild(androidx.xr.scenecore.Entity)).

Entities have some default behaviors for things that are universal to all
entities, such as changing position, rotation, or visibility. Specific `Entity`
subclasses, like the [`GltfModelEntity`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/GltfModelEntity), have additional behaviors that
support the subclass.

### Manipulate Entities

When you make a change to an `Entity` property that belongs to the base `Entity`
class, the change will cascade down to all of its children. For example,
adjusting the [`Pose`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/math/Pose) of a parent `Entity` results in all of its children
having the same adjustment. Making a change in a child `Entity` does not impact
its parent.

A `Pose` represents the location and rotation of the Entity within 3D space. The
location is a [`Vector3`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/math/Vector3) consisting of x, y, z numerical positions. The
rotation is represented by a [`Quaternion`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/math/Quaternion). The position of an `Entity` is
always relative to its parent entity. In other words, an `Entity` whose position
is (0, 0, 0) will be placed at the origin of its parent entity.


```kotlin
// Place the entity forward 2 meters
val newPosition = Vector3(0f, 0f, -2f)
// Rotate the entity by 180 degrees on the up axis (upside-down)
val newOrientation = Quaternion.fromEulerAngles(0f, 0f, 180f)
// Update the position and rotation on the entity
entity.setPose(Pose(newPosition, newOrientation))
```

<br />

> [!IMPORTANT]
> **Important:** When discussing the location of an `Entity`, remember the `Entity` can be located at a specific point in the Scene Graph and it also has a position in 3D space.

To disable an `Entity`, use [`setEnabled()`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/Entity#setEnabled(kotlin.Boolean)). This makes it invisible and
stops all processing done on it.


```kotlin
// Disable the entity.
entity.setEnabled(false)
```

<br />

To resize an `Entity` while keeping its overall shape, use [`setScale()`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/Entity#setScale(kotlin.Float)).


```kotlin
// Double the size of the entity
entity.setScale(2f)
```

<br />

> [!CAUTION]
> **Caution:** The scale of an `Entity` impacts the units of its coordinate system. For example, changing the scale to 2, makes it so every unit in this entity no longer represents 1 meter in the real world, it represents 2 meters in the real world. This also cascades down to any children of the entity.

### Add common behavior to entities

You can use the following components to add common behavior to entities:

- [`MovableComponent`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/MovableComponent): Allows the user to move entities
- [`ResizableComponent`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/ResizableComponent): Allows the user to resize entities with consistent UI patterns
- [`InteractableComponent`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/InteractableComponent): Lets you capture input events for custom interactions

Instantiating components must be done through the appropriate creation method in
the `Session` class. For example, to create a `ResizableComponent`, call
[`ResizableComponent.create()`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/ResizableComponent#create).

> [!WARNING]
> **Preview:** Currently, not all components can be used in all types of entities. Refer to the documentation of the specific component to see which entities are supported.

To add the specific component behavior to an `Entity` use the
[`addComponent()`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/Entity#addComponent(androidx.xr.scenecore.Component)) method.

#### Use `MovableComponent` to make an Entity user-movable

The [`MovableComponent`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/MovableComponent) allows an `Entity` to be movable by the user.


Your browser doesn't support HTML video. Here is a
[link to the video](https://developer.android.com/static/develop/xr/jetpack-xr-sdk/videos/movablecomponent.mp4) instead.

Movement events are dispatched to the component when the decorations are
interacted with. The default system behavior, created with
[`MovableComponent.createSystemMovable()`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/MovableComponent#createSystemMovable(androidx.xr.runtime.Session,kotlin.Boolean)), moves your `Entity` when the
decorations are dragged:


```kotlin
val movableComponent = MovableComponent.createSystemMovable(session)
entity.addComponent(movableComponent)
```

<br />

The optional `scaleInZ` parameter (by default, set to `true`), makes the Entity
automatically adjust its scale as it is moved away from the user,
in a similar way to how panels are scaled by the system in [home space](https://developer.android.com/develop/xr/jetpack-xr-sdk/transition-home-space-to-full-space).
Due to the "cascading" nature of the entity component system, the parent's scale
will impact all of its children.

You can also specify whether the entity can be anchored to a surface type like
horizontal or vertical surfaces, or specific semantic surfaces like table, wall
or ceiling. To specify anchor options, specify a set of [`AnchorPlacement`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/AnchorPlacement)
when creating the `MovableComponent`. In this example, the entity that can be
moved and anchored to any floor or table horizontal surface:


```kotlin
val anchorPlacement = AnchorPlacement.createForPlanes(
    anchorablePlaneOrientations = setOf(PlaneOrientation.VERTICAL),
    anchorablePlaneSemanticTypes = setOf(PlaneSemanticType.FLOOR, PlaneSemanticType.TABLE)
)

val movableComponent = MovableComponent.createAnchorable(
    session = session,
    anchorPlacement = setOf(anchorPlacement)
)
entity.addComponent(movableComponent)
```

<br />

> [!NOTE]
> **Note:** If you are creating your spatialized UI with [Jetpack Compose for XR](https://developer.android.com/develop/xr/jetpack-xr-sdk/develop-ui), you may choose to use the [`movable`](https://developer.android.com/develop/xr/jetpack-xr-sdk/subspacemodifiers#movable) subspace modifier to enable movement of your panels.

#### Use `ResizableComponent` to make an Entity user-resizable

The [`ResizableComponent`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/ResizableComponent) allows users to resize an `Entity`. The
`ResizableComponent` includes visual interaction cues that invite the user to
resize an `Entity`. When creating the `ResizableComponent`, you can specify a
minimum or maximum size (in meters). You also have the option to specify a fixed
aspect ratio when resizing so that the width and height resize proportionally to
each other.

When creating a `ResizableComponent`, specify a `resizeEventListener` that
handles the update events. You can respond to different [`ResizeState`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/ResizeEvent.ResizeState)
events, such as `RESIZE_STATE_ONGOING` or `RESIZE_STATE_END`.

Here's an example of using the `ResizableComponent` with a fixed aspect ratio on
a `SurfaceEntity`:


```kotlin
val resizableComponent = ResizableComponent.create(session) { event ->
    if (event.resizeState == ResizeEvent.ResizeState.END) {
        // update the Entity to reflect the new size
        surfaceEntity.shape = SurfaceEntity.Shape.Quad(FloatSize2d(event.newSize.width, event.newSize.height))
    }
}
resizableComponent.minimumEntitySize = FloatSize3d(177f, 100f, 1f)
resizableComponent.isFixedAspectRatioEnabled = true // Maintain a fixed aspect ratio when resizing

surfaceEntity.addComponent(resizableComponent)
```

<br />

> [!NOTE]
> **Note:** If you are creating your spatialized UI with [Jetpack Compose for XR](https://developer.android.com/develop/xr/jetpack-xr-sdk/develop-ui), you may choose to use the [`resizable`](https://developer.android.com/develop/xr/jetpack-xr-sdk/subspacemodifiers#resizable) subspace modifier to enable resizing of your panels.

#### Use `InteractableComponent` to capture user input events

The [`InteractableComponent`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/InteractableComponent) lets you capture input events from the user,
such as when the user engages or hovers over an `Entity`. When creating an
`InteractableComponent`, specify a listener that receives the input events.
When the user performs any input action, the listener will be called with the
input information provided in the [`InputEvent`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/InputEvent) parameter.

- [`InputEvent.action`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/InputEvent#action()) specifies the type of input such as [hovering](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/InputEvent.Action#ACTION_HOVER_ENTER()) or [tapping](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/InputEvent.Action#ACTION_DOWN()) on an entity
- [`InputEvent.source`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/InputEvent#source()) specifies where the input came from such as [hand](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/InputEvent.Source#SOURCE_HANDS()) or [controller](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/InputEvent.Source#SOURCE_CONTROLLER()) input
- [`InputEvent.pointerType`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/InputEvent#pointerType()) specifies whether the input came from the right hand or left hand

For a full list of all the `InputEvent` constants, see the [reference
documentation](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/InputEvent).

The following code snippet shows an example of using an `InteractableComponent`
to increase the size of an entity with the right hand and decreases with the
left hand.


```kotlin
val executor = Executors.newSingleThreadExecutor()
val interactableComponent = InteractableComponent.create(session, executor) {
    // when the user disengages with the entity with their hands
    if (it.source == InputEvent.Source.HANDS && it.action == InputEvent.Action.UP) {
        // increase size with right hand and decrease with left
        if (it.pointerType == InputEvent.Pointer.RIGHT) {
            entity.setScale(1.5f)
        } else if (it.pointerType == InputEvent.Pointer.LEFT) {
            entity.setScale(0.5f)
        }
    }
}
entity.addComponent(interactableComponent)
```

<br />