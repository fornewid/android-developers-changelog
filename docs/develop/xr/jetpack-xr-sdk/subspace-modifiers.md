---
title: Understand subspace modifiers  |  Android XR for Jetpack XR SDK  |  Android Developers
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/subspace-modifiers
source: html-scrape
---

The Android XR SDK has  [reached Developer Preview 3](https://android-developers.googleblog.com/2025/12/build-for-ai-glasses-with-android-xr.html), and we want your feedback! Try things out, and visit our [support page](/develop/xr/support) to reach out.

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android XR](https://developer.android.com/develop/xr)
* [Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk)
* [Guides](https://developer.android.com/develop/xr/get-started)

# Understand subspace modifiers Stay organized with collections Save and categorize content based on your preferences.




Applicable XR devices

This guidance helps you build experiences for these types of XR devices.

[Learn about XR device types →](/develop/xr/devices)

![](/static/images/develop/xr/xr-headsets-icon.svg)


XR Headsets

![](/static/images/develop/xr/xr-glasses-icon.svg)


Wired XR Glasses

[Learn about XR device types →](/develop/xr/devices)

A [`SubspaceModifier`](/reference/kotlin/androidx/xr/compose/subspace/layout/SubspaceModifier) is similar to a [Compose modifier](/develop/ui/compose/modifiers) for composables
in a [`Subspace`](/develop/xr/jetpack-xr-sdk/add-subspace). A `SubspaceModifier` lets you manipulate composables in 3D
space, helping you position, rotate, and add behaviors to 3D layout nodes.

## Layout

By default, a `Subspace` is [bounded by the recommended space for viewing an
app](/develop/xr/jetpack-xr-sdk/add-subspace#subspace-hierarchies). These bounds are used when measuring the layout of your subspace
components, similar to [bounds in 2D Compose layouts](/develop/ui/compose/layouts/constraints-modifiers).

### Fill bounds

The modifiers [`fillMaxSize`](/reference/kotlin/androidx/xr/compose/subspace/layout/SubspaceModifier#(androidx.xr.compose.subspace.layout.SubspaceModifier).fillMaxSize(kotlin.Float)), [`fillMaxWidth`](/reference/kotlin/androidx/xr/compose/subspace/layout/SubspaceModifier#(androidx.xr.compose.subspace.layout.SubspaceModifier).fillMaxWidth(kotlin.Float)), [`fillMaxHeight`](/reference/kotlin/androidx/xr/compose/subspace/layout/SubspaceModifier#(androidx.xr.compose.subspace.layout.SubspaceModifier).fillMaxHeight(kotlin.Float)), and
[`fillMaxDepth`](/reference/kotlin/androidx/xr/compose/subspace/layout/SubspaceModifier#(androidx.xr.compose.subspace.layout.SubspaceModifier).fillMaxDepth(kotlin.Float)) make content (partially) fill the bounds of its parent.
Using fill modifiers helps your app layout content that's independent of the XR
device's display characteristics.

### Set the size and required size

The modifiers [`size`](/reference/kotlin/androidx/xr/compose/subspace/layout/SubspaceModifier#(androidx.xr.compose.subspace.layout.SubspaceModifier).size(androidx.compose.ui.unit.Dp)), [`width`](/reference/kotlin/androidx/xr/compose/subspace/layout/SubspaceModifier#(androidx.xr.compose.subspace.layout.SubspaceModifier).width(androidx.compose.ui.unit.Dp)), [`height`](/reference/kotlin/androidx/xr/compose/subspace/layout/SubspaceModifier#(androidx.xr.compose.subspace.layout.SubspaceModifier).height(androidx.compose.ui.unit.Dp)), and [`depth`](/reference/kotlin/androidx/xr/compose/subspace/layout/SubspaceModifier#(androidx.xr.compose.subspace.layout.SubspaceModifier).depth(androidx.compose.ui.unit.Dp))
declare the preferred size of the content. To declare the exact size of the
content, use [`requiredSize`](/reference/kotlin/androidx/xr/compose/subspace/layout/SubspaceModifier#(androidx.xr.compose.subspace.layout.SubspaceModifier).requiredSize(androidx.compose.ui.unit.Dp)), [`requiredWidth`](/reference/kotlin/androidx/xr/compose/subspace/layout/SubspaceModifier#(androidx.xr.compose.subspace.layout.SubspaceModifier).requiredWidth(androidx.compose.ui.unit.Dp)),
[`requiredHeight`](/reference/kotlin/androidx/xr/compose/subspace/layout/SubspaceModifier#(androidx.xr.compose.subspace.layout.SubspaceModifier).requiredHeight(androidx.compose.ui.unit.Dp)), and [`requiredDepth`](/reference/kotlin/androidx/xr/compose/subspace/layout/SubspaceModifier#(androidx.xr.compose.subspace.layout.SubspaceModifier).requiredDepth(androidx.compose.ui.unit.Dp)). These units must be specified
in `dp`; to convert from meters to dp, use [`Meter.toDp()`](/reference/kotlin/androidx/xr/compose/unit/Meter#toDp()).

## Position composables

### `offset`

The [`offset`](/reference/kotlin/androidx/xr/compose/subspace/layout/SubspaceModifier#(androidx.xr.compose.subspace.layout.SubspaceModifier).offset(androidx.compose.ui.unit.Dp,androidx.compose.ui.unit.Dp,androidx.compose.ui.unit.Dp)) modifier moves the composable in 3D space along the `x`, `y`,
and `z` axes. These units must be specified in `dp`; to convert from meters to
dp, use [`Meter.toDp()`](/reference/kotlin/androidx/xr/compose/unit/Meter#toDp()).

### `rotate`

The [`rotate`](/reference/kotlin/androidx/xr/compose/subspace/layout/SubspaceModifier#(androidx.xr.compose.subspace.layout.SubspaceModifier).rotate(androidx.xr.runtime.math.Quaternion)) modifier rotates the given composable in space. You can
specify the direction and the amount of rotation in different ways:

* Using pitch, yaw, and roll, which specify the rotation around the `x`, `y`,
  and `z` axes respectively,
* Using an `axisAngle`, which is a `Vector3` representing the axis of
  rotation, and the amount of degrees it should be rotated around,
* Using a `Quaternion` that represents the rotation.

### `lookAtUser`

The [`lookAtUser`](/reference/kotlin/androidx/xr/compose/subspace/layout/SubspaceModifier#(androidx.xr.compose.subspace.layout.SubspaceModifier).lookAtUser(kotlin.Boolean,androidx.xr.runtime.math.Vector3)) modifier continually rotates the given composable
in space such that it appears to be facing the viewer. A similar modifier,
[`billboard`](/reference/kotlin/androidx/xr/compose/subspace/layout/SubspaceModifier#(androidx.xr.compose.subspace.layout.SubspaceModifier).billboard(kotlin.Boolean)), rotates to face the viewer, but the content will
remain upright.

These modifiers require the `android.permission.HEAD_TRACKING` permission [to be
granted to your app](/training/permissions/requesting). Additionally, the
[current session](/develop/xr/jetpack-xr-sdk/add-session#localsession) must [be configured](/develop/xr/jetpack-xr-sdk/arcore#configure-session) to set
[`HeadTrackingMode.LAST_KNOWN`](/reference/kotlin/androidx/xr/runtime/HeadTrackingMode#LAST_KNOWN()).

## Change the appearance of composables

### `alpha`

The [`alpha`](/reference/kotlin/androidx/xr/compose/subspace/layout/SubspaceModifier#(androidx.xr.compose.subspace.layout.SubspaceModifier).alpha(kotlin.Float)) modifier sets the opacity of the element and its children,
where `0f` represents fully transparent and `1.0f` represents completely opaque.

**Preview:** Currently, the `alpha` modifier only works on `SpatialPanel`.

### `scale`

The [`scale`](/reference/kotlin/androidx/xr/compose/subspace/layout/SubspaceModifier#(androidx.xr.compose.subspace.layout.SubspaceModifier).scale(kotlin.Float)) modifier scales the contents of the composible along the
horizontal, vertical, and depth axes.

## Testing and accessibility

### `semantics`

The [`semantics`](/reference/kotlin/androidx/xr/compose/subspace/layout/SubspaceModifier#(androidx.xr.compose.subspace.layout.SubspaceModifier).semantics(kotlin.Function1)) modifier adds semantics to the layout node, for use in
testing and accessibility. See [Semantics in Jetpack Compose](/develop/ui/compose/accessibility/semantics) and
[`SemanticsModifier`](/reference/kotlin/androidx/compose/ui/semantics/SemanticsModifier).

### `testTag`

The [`testTag`](/reference/kotlin/androidx/xr/compose/subspace/layout/SubspaceModifier#(androidx.xr.compose.subspace.layout.SubspaceModifier).testTag(kotlin.String)) modifier is a shorthand for
[`SemanticsPropertyReceiver.testTag`](/reference/kotlin/androidx/compose/ui/semantics/SemanticsPropertyReceiver#(androidx.compose.ui.semantics.SemanticsPropertyReceiver).testTag()), which allows test frameworks to find
the element in tests.