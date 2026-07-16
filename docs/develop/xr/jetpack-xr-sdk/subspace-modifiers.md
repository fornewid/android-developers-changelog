---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/subspace-modifiers
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/subspace-modifiers
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

A [`SubspaceModifier`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/layout/SubspaceModifier) is similar to a [Compose modifier](https://developer.android.com/develop/ui/compose/modifiers) for composables
in a [`Subspace`](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-subspace). A `SubspaceModifier` lets you manipulate composables in 3D
space, helping you position, rotate, and add behaviors to 3D layout nodes.

## Layout

By default, a `Subspace` is [bounded by the recommended space for viewing an
app](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-subspace#subspace-hierarchies). These bounds are used when measuring the layout of your subspace
components, similar to [bounds in 2D Compose layouts](https://developer.android.com/develop/ui/compose/layouts/constraints-modifiers).

### Fill bounds

The modifiers [`fillMaxSize`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/layout/SubspaceModifier#(androidx.xr.compose.subspace.layout.SubspaceModifier).fillMaxSize(kotlin.Float)), [`fillMaxWidth`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/layout/SubspaceModifier#(androidx.xr.compose.subspace.layout.SubspaceModifier).fillMaxWidth(kotlin.Float)), [`fillMaxHeight`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/layout/SubspaceModifier#(androidx.xr.compose.subspace.layout.SubspaceModifier).fillMaxHeight(kotlin.Float)), and
[`fillMaxDepth`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/layout/SubspaceModifier#(androidx.xr.compose.subspace.layout.SubspaceModifier).fillMaxDepth(kotlin.Float)) make content (partially) fill the bounds of its parent.
Using fill modifiers helps your app layout content that's independent of the XR
device's display characteristics.

### Set the size and required size

The modifiers [`size`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/layout/SubspaceModifier#(androidx.xr.compose.subspace.layout.SubspaceModifier).size(androidx.compose.ui.unit.Dp)), [`width`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/layout/SubspaceModifier#(androidx.xr.compose.subspace.layout.SubspaceModifier).width(androidx.compose.ui.unit.Dp)), [`height`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/layout/SubspaceModifier#(androidx.xr.compose.subspace.layout.SubspaceModifier).height(androidx.compose.ui.unit.Dp)), and [`depth`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/layout/SubspaceModifier#(androidx.xr.compose.subspace.layout.SubspaceModifier).depth(androidx.compose.ui.unit.Dp))
declare the preferred size of the content. To declare the exact size of the
content, use [`requiredSize`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/layout/SubspaceModifier#(androidx.xr.compose.subspace.layout.SubspaceModifier).requiredSize(androidx.compose.ui.unit.Dp)), [`requiredWidth`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/layout/SubspaceModifier#(androidx.xr.compose.subspace.layout.SubspaceModifier).requiredWidth(androidx.compose.ui.unit.Dp)),
[`requiredHeight`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/layout/SubspaceModifier#(androidx.xr.compose.subspace.layout.SubspaceModifier).requiredHeight(androidx.compose.ui.unit.Dp)), and [`requiredDepth`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/layout/SubspaceModifier#(androidx.xr.compose.subspace.layout.SubspaceModifier).requiredDepth(androidx.compose.ui.unit.Dp)). These units must be specified
in `dp`; to convert from meters to dp, use [`Meter.toDp()`](https://developer.android.com/reference/kotlin/androidx/xr/compose/unit/Meter#toDp()).

## Position composables

### `offset`

The [`offset`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/layout/SubspaceModifier#(androidx.xr.compose.subspace.layout.SubspaceModifier).offset(androidx.compose.ui.unit.Dp,androidx.compose.ui.unit.Dp,androidx.compose.ui.unit.Dp)) modifier moves the composable in 3D space along the `x`, `y`,
and `z` axes. These units must be specified in `dp`; to convert from meters to
dp, use [`Meter.toDp()`](https://developer.android.com/reference/kotlin/androidx/xr/compose/unit/Meter#toDp()).

### `rotate`

The [`rotate`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/layout/SubspaceModifier#(androidx.xr.compose.subspace.layout.SubspaceModifier).rotate(androidx.xr.runtime.math.Quaternion)) modifier rotates the given composable in space. You can
specify the direction and the amount of rotation in different ways:

- Using pitch, yaw, and roll, which specify the rotation around the `x`, `y`, and `z` axes respectively,
- Using an `axisAngle`, which is a `Vector3` representing the axis of rotation, and the amount of degrees it should be rotated around,
- Using a `Quaternion` that represents the rotation.

### `rotateToLookAtUser`

The [`rotateToLookAtUser`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/layout/SubspaceModifier#(androidx.xr.compose.subspace.layout.SubspaceModifier).rotateToLookAtUser(androidx.xr.runtime.math.Vector3)) modifier continuously rotates
content so that it faces the user at all times. You can also use this modifier
to achieve a "billboard" effect where the content rotates to face the user on
the Y-axis while still remaining upright and aligned with gravity. To do this,
combine the [`rotateToLookAtUser`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/layout/SubspaceModifier#(androidx.xr.compose.subspace.layout.SubspaceModifier).rotateToLookAtUser(androidx.xr.runtime.math.Vector3)) modifier with
the [`gravityAligned`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/layout/package-summary#(androidx.xr.compose.subspace.layout.SubspaceModifier).gravityAligned()) modifier.

> [!NOTE]
> **Note:** This modifier requires your app to [configure](https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore#configure-session) the [current session's](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-session#localsession) object with [`DeviceTrackingMode.SPATIAL_LAST_KNOWN`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/DeviceTrackingMode#SPATIAL_LAST_KNOWN()).

## Move and Resize with composables

Let users directly manipulate the position and size of objects in 3D space. You
can add these modifiers to individual components (like `SpatialPanel`),
subspaces, and spatial layout components (like `SpatialRow` or `SpatialColumn`).

### Move elements

When the [`movable()`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/layout/SubspaceModifier#(androidx.xr.compose.subspace.layout.SubspaceModifier).movable(kotlin.Boolean,androidx.xr.compose.subspace.layout.MovePolicy)) modifier is present and enabled, draggable UI controls will
be shown that allow the user to move the element in 3D space. The specific
behavior of this movement is defined by the provided `movePolicy`:

- `MovePolicy.default()`: The system handles the movement entirely and automatically calculates and applies the new pose and scale based on user input.
- `MovePolicy.custom()`: The system calculates the target Pose based on input, but does not automatically apply it to the associated element. This is useful for restricting movement or creating custom movement in your app.

### Resize elements

When the [`resizable()`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/layout/SubspaceModifier#(androidx.xr.compose.subspace.layout.SubspaceModifier).resizable(kotlin.Boolean,androidx.xr.compose.unit.DpVolumeSize,androidx.xr.compose.unit.DpVolumeSize,kotlin.Boolean,androidx.xr.compose.subspace.layout.ResizePolicy)) modifier is present and enabled, UI controls
will be shown that allow the user to resize the element in 3D space. The
specific behavior of the resize is defined by the provided `resizePolicy`:

- `ResizePolicy.default()`: The system automatically handles the resize gesture and applies the new dimensions to the content.
- `ResizePolicy.custom()`: The system provides a [`SpatialResizeEvent`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/layout/SpatialResizeEvent) and does not automatically apply the result of the resize to the associated element.

## Change the appearance of composables

### `alpha`

The [`alpha`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/layout/SubspaceModifier#(androidx.xr.compose.subspace.layout.SubspaceModifier).alpha(kotlin.Float)) modifier sets the opacity of the element and its children,
where `0f` represents fully transparent and `1.0f` represents completely opaque.

> [!WARNING]
> **Preview:** Currently, the `alpha` modifier only works on `SpatialPanel`.

### `scale`

The [`scale`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/layout/SubspaceModifier#(androidx.xr.compose.subspace.layout.SubspaceModifier).scale(kotlin.Float)) modifier scales the contents of the composible along the
horizontal, vertical, and depth axes.

## Testing and accessibility

### `semantics`

The [`semantics`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/layout/SubspaceModifier#(androidx.xr.compose.subspace.layout.SubspaceModifier).semantics(kotlin.Function1)) modifier adds semantics to the layout node, for use in
testing and accessibility. See [Semantics in Jetpack Compose](https://developer.android.com/develop/ui/compose/accessibility/semantics) and
[`SemanticsModifier`](https://developer.android.com/reference/kotlin/androidx/compose/ui/semantics/SemanticsModifier).

### `testTag`

The [`testTag`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/layout/SubspaceModifier#(androidx.xr.compose.subspace.layout.SubspaceModifier).testTag(kotlin.String)) modifier is a shorthand for
[`SemanticsPropertyReceiver.testTag`](https://developer.android.com/reference/kotlin/androidx/compose/ui/semantics/SemanticsPropertyReceiver#(androidx.compose.ui.semantics.SemanticsPropertyReceiver).testTag()), which allows test frameworks to find
the element in tests.