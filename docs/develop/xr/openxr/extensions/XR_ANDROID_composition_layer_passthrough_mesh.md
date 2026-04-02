---
title: https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh
url: https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh
source: md.txt
---

**Name String**

`XR_ANDROID_composition_layer_passthrough_mesh`

**Extension Type**

Instance extension

**Registered Extension Number**

463

**Revision**

1

**Extension and Version Dependencies**

[OpenXR 1.0](https://registry.khronos.org/OpenXR/specs/1.0/html/xrspec.html#versions-1.0)

**Last Modified Date**

2024-09-18

**IP Status**

No known IP claims.

**Contributors**

Grant Yoshida, Google

Kevin Moule, Google

Vasiliy Baranov, Google

Peter Chen, Google

Levana Chen, Google

## Overview

For devices that support multiple environment blend modes, the system may
provide passthrough configurations to show a user their physical environment
from an immersive view.

This extension enables applications to project passthrough textures onto
arbitrary geometry through an additional composition layer
[XrCompositionLayerPassthroughANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrCompositionLayerPassthroughANDROID).

The passthrough layer characteristics are specified by the following parameters,
in which the projection is represented by [XrPassthroughLayerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrPassthroughLayerANDROID).

      XrPosef                      pose;
        XrVector3f                   scale;
        float                        opacity;
        XrPassthroughLayerANDROID    layer;

For full screen passthrough, applications **can** use
[Environment Blend Mode](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#rendering-environment-blend-mode).

## Inspect system capability

An application **can** inspect whether the system is capable of composition
layer passthrough mesh by chaining an
[XrSystemPassthroughLayerPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrSystemPassthroughLayerPropertiesANDROID) structure to the
[XrSystemProperties](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSystemProperties) when calling [xrGetSystemProperties](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrGetSystemProperties).

    typedef struct XrSystemPassthroughLayerPropertiesANDROID {
        XrStructureType    type;
        void*              next;
        XrBool32           supportsPassthroughLayer;
        uint32_t           maxMeshIndexCount;
        uint32_t           maxMeshVertexCount;
    } XrSystemPassthroughLayerPropertiesANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.
- `supportsPassthroughLayer` is an [`XrBool32`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrBool32), indicating if the current system supports composition layer passthrough mesh.
- `maxMeshIndexCount` is a `uint32_t` returns the maximum count of indices that will be accepted for a passthrough mesh.
- `maxMeshVertexCount` is a `uint32_t` returns the maximum count of vertices that will be accepted for a passthrough mesh.

If `supportsPassthroughLayer` returns `XR_FALSE`, the system does
not support composition layer passthrough mesh, and therefore will receive
`XR_ERROR_FEATURE_UNSUPPORTED` from [xrCreatePassthroughLayerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#xrCreatePassthroughLayerANDROID). The
application **should** avoid using composition layer passthrough mesh when
`supportsPassthroughLayer` is `XR_FALSE`.

If `supportsPassthroughLayer` returns `XR_TRUE`, the system
supports composition layer passthrough mesh. In this case,
`maxMeshIndexCount` and `maxMeshVertexCount` will return a non-zero number. An
application **should** use `maxMeshIndexCount` and `maxMeshVertexCount` as the
maximum values to set passthrough meshes when calling
[xrCreatePassthroughLayerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#xrCreatePassthroughLayerANDROID) and
[xrSetPassthroughLayerMeshANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#xrSetPassthroughLayerMeshANDROID), otherwise
`XR_ERROR_MESH_DATA_LIMIT_EXCEEDED_ANDROID` may be returned
to indicate the mesh data exceeds
the supported limit.

### Valid Usage (Implicit)

- The [`XR_ANDROID_composition_layer_passthrough_mesh`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XR_ANDROID_composition_layer_passthrough_mesh) extension **must** be enabled prior to using [XrSystemPassthroughLayerPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrSystemPassthroughLayerPropertiesANDROID)
- `type` **must** be `XR_TYPE_SYSTEM_PASSTHROUGH_LAYER_PROPERTIES_ANDROID`
- `next` **must** be `NULL` or a valid pointer to the [next structure in a
  structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-valid-usage-for-structure-pointer-chains)

## Passthrough Layer Composition

The [XrCompositionLayerPassthroughANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrCompositionLayerPassthroughANDROID) contains the information needed to
render a passthrough texture onto a triangle mesh when calling [xrEndFrame](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrEndFrame).
[XrCompositionLayerPassthroughANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrCompositionLayerPassthroughANDROID) is an alias type for the base struct
[XrCompositionLayerBaseHeader](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrCompositionLayerBaseHeader) used in [XrFrameEndInfo](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrFrameEndInfo).

    typedef struct XrCompositionLayerPassthroughANDROID {
        XrStructureType              type;
        const void*                  next;
        XrCompositionLayerFlags      layerFlags;
        XrSpace                      space;
        XrPosef                      pose;
        XrVector3f                   scale;
        float                        opacity;
        XrPassthroughLayerANDROID    layer;
    } XrCompositionLayerPassthroughANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.
- `layerFlags` is a bitmask of [XrCompositionLayerFlags](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrCompositionLayerFlags) describing flags to apply to the layer.
- `space` is the [XrSpace](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpace) in which the `pose` of the layer mesh is evaluated over time.
- `pose` is an `XrPosef` defining the position and orientation of the layer mesh in the reference frame of the `space`.
- `scale` is an `XrVector3f` defining the scale of the layer mesh.
- `opacity` is a `float` defining the opacity of the passthrough texture in range \[0, 1\].
- `layer` is the [XrPassthroughLayerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrPassthroughLayerANDROID) previously created by [xrCreatePassthroughLayerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#xrCreatePassthroughLayerANDROID).

The application **can** create an [XrCompositionLayerPassthroughANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrCompositionLayerPassthroughANDROID)
structure with the created `layer` and the corresponding meshes provided by
[XrPassthroughLayerMeshANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrPassthroughLayerMeshANDROID).

A pointer to [XrCompositionLayerPassthroughANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrCompositionLayerPassthroughANDROID) **may** be submitted in
[xrEndFrame](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrEndFrame) as a pointer to the base structure
[XrCompositionLayerBaseHeader](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrCompositionLayerBaseHeader), in the chosen layer order, to request the
runtime to composite a passthrough layer into the final frame output.

### Valid Usage (Implicit)

- The [`XR_ANDROID_composition_layer_passthrough_mesh`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XR_ANDROID_composition_layer_passthrough_mesh) extension **must** be enabled prior to using [XrCompositionLayerPassthroughANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrCompositionLayerPassthroughANDROID)
- `type` **must** be `XR_TYPE_COMPOSITION_LAYER_PASSTHROUGH_ANDROID`
- `next` **must** be `NULL` or a valid pointer to the [next structure in a
  structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-valid-usage-for-structure-pointer-chains)
- `layerFlags` **must** be `0` or a valid combination of [XrCompositionLayerFlagBits](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrCompositionLayerFlagBits) values
- `space` **must** be a valid [XrSpace](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpace) handle
- `layer` **must** be a valid [XrPassthroughLayerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrPassthroughLayerANDROID) handle
- Both of `layer` and `space` **must** have been created, allocated, or retrieved from the same [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession)

## Create a passthrough layer handle

The [XrPassthroughLayerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrPassthroughLayerANDROID) handle represents a passthrough layer which
defines the behavior of [XrCompositionLayerPassthroughANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrCompositionLayerPassthroughANDROID).

    XR_DEFINE_HANDLE(XrPassthroughLayerANDROID)

An application **can** create an [XrPassthroughLayerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrPassthroughLayerANDROID) handle by
calling [xrCreatePassthroughLayerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#xrCreatePassthroughLayerANDROID). The returned
[XrPassthroughLayerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrPassthroughLayerANDROID) handle **can** be subsequently used in API calls.

    XrResult xrCreatePassthroughLayerANDROID(
        XrSession                                   session,
        const XrPassthroughLayerCreateInfoANDROID*  createInfo,
        XrPassthroughLayerANDROID*                  layer);

Parameter Descriptions

- `session` is an [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) in which the passthrough layer will be created for.
- `createInfo` is a pointer to an [XrPassthroughLayerCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrPassthroughLayerCreateInfoANDROID) structure specifying initial passthrough layer parameters. This field **can** also be chained to an [XrPassthroughLayerMeshANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrPassthroughLayerMeshANDROID) structure to set the mesh at the same time.
- `layer` is a pointer to a handle in which the created [XrPassthroughLayerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrPassthroughLayerANDROID) is returned.

The application **should** specify the number of passthrough mesh indices in the
[XrPassthroughLayerCreateInfoANDROID::vertexCapacity](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrPassthroughLayerCreateInfoANDROID) and
[XrPassthroughLayerCreateInfoANDROID::indexCapacity](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrPassthroughLayerCreateInfoANDROID) less than or equal to
the maximum values returned by
[XrSystemPassthroughLayerPropertiesANDROID::maxMeshIndexCount](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrSystemPassthroughLayerPropertiesANDROID) and
[XrSystemPassthroughLayerPropertiesANDROID::maxMeshVertexCount](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrSystemPassthroughLayerPropertiesANDROID) when calling
[xrGetSystemProperties](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrGetSystemProperties). [xrCreatePassthroughLayerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#xrCreatePassthroughLayerANDROID) will return a
`XR_ERROR_MESH_DATA_LIMIT_EXCEEDED_ANDROID` error if the count of mesh indices
defined by`createInfo` is greater than the maximum values.

The [XrPassthroughLayerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrPassthroughLayerANDROID) handle **must** be eventually freed using the
`xrDestroyPassthroughLayerANDROID` function.

### Valid Usage (Implicit)

- The [`XR_ANDROID_composition_layer_passthrough_mesh`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XR_ANDROID_composition_layer_passthrough_mesh) extension **must** be enabled prior to calling [xrCreatePassthroughLayerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#xrCreatePassthroughLayerANDROID)
- `session` **must** be a valid [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) handle
- `createInfo` **must** be a pointer to a valid [XrPassthroughLayerCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrPassthroughLayerCreateInfoANDROID) structure
- `layer` **must** be a pointer to an [XrPassthroughLayerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrPassthroughLayerANDROID) handle

### Return Codes

[**Success**](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`
- `XR_SESSION_LOSS_PENDING`

[**Failure**](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_VALIDATION_FAILURE`
- `XR_ERROR_RUNTIME_FAILURE`
- `XR_ERROR_HANDLE_INVALID`
- `XR_ERROR_INSTANCE_LOST`
- `XR_ERROR_SESSION_LOST`
- `XR_ERROR_OUT_OF_MEMORY`
- `XR_ERROR_LIMIT_REACHED`
- `XR_ERROR_SIZE_INSUFFICIENT`
- `XR_ERROR_MESH_DATA_LIMIT_EXCEEDED_ANDROID`

The [XrPassthroughLayerCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrPassthroughLayerCreateInfoANDROID) structure is defined as:

    typedef struct XrPassthroughLayerCreateInfoANDROID {
        XrStructureType    type;
        const void*        next;
        uint32_t           vertexCapacity;
        uint32_t           indexCapacity;
    } XrPassthroughLayerCreateInfoANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is NULL or a pointer to the next structure in a structure chain. [XrPassthroughLayerMeshANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrPassthroughLayerMeshANDROID) **can** be provided in the next chain to specify an initial mesh for the passthrough layer when calling [xrCreatePassthroughLayerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#xrCreatePassthroughLayerANDROID).
- `vertexCapacity` is an `uint32_t` representing the **maximum** capacity of the vertex buffer for this layer's mesh, or `0` if unspecified. If specified, the [XrPassthroughLayerMeshANDROID::vertexCount](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrPassthroughLayerMeshANDROID) of any mesh set for this layer **must** be less than or equal to the `vertexCapacity`.
- `indexCapacity` is an `uint32_t` representing the **maximum** capacity of the index buffer for this layer's mesh, or `0` if unspecified. If specified, the [XrPassthroughLayerMeshANDROID::indexCount](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrPassthroughLayerMeshANDROID) of any mesh set for this layer **must** be less than or equal to the `indexCapacity`.

### Valid Usage (Implicit)

- The [`XR_ANDROID_composition_layer_passthrough_mesh`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XR_ANDROID_composition_layer_passthrough_mesh) extension **must** be enabled prior to using [XrPassthroughLayerCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrPassthroughLayerCreateInfoANDROID)
- `type` **must** be `XR_TYPE_PASSTHROUGH_LAYER_CREATE_INFO_ANDROID`
- `next` **must** be `NULL` or a valid pointer to the [next structure in a
  structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-valid-usage-for-structure-pointer-chains). See also: [XrPassthroughLayerMeshANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrPassthroughLayerMeshANDROID)

An application **can** use `xrDestroyPassthroughLayerANDROID` function to
release the passthrough layer and the underlying resources.

    XrResult xrDestroyPassthroughLayerANDROID(
        XrPassthroughLayerANDROID                   layer);

### Parameter Descriptions

- `layer` is the [XrPassthroughLayerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrPassthroughLayerANDROID) to be destroyed.

### Valid Usage (Implicit)

- The [`XR_ANDROID_composition_layer_passthrough_mesh`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XR_ANDROID_composition_layer_passthrough_mesh) extension **must** be enabled prior to calling `xrDestroyPassthroughLayerANDROID`
- `layer` **must** be a valid [XrPassthroughLayerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrPassthroughLayerANDROID) handle

### Thread Safety

- Access to `layer`, and any child handles, **must** be externally synchronized

### Return Codes

[**Success**](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`

[**Failure**](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_RUNTIME_FAILURE`
- `XR_ERROR_HANDLE_INVALID`

## Set passthrough layer mesh

An application **can** use [xrSetPassthroughLayerMeshANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#xrSetPassthroughLayerMeshANDROID) function to
set the mesh for a passthrough layer.

    XrResult xrSetPassthroughLayerMeshANDROID(
        XrPassthroughLayerANDROID                   layer,
        const XrPassthroughLayerMeshANDROID*        mesh);

### Parameter Descriptions

- `layer` is an [XrPassthroughLayerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrPassthroughLayerANDROID) handle in which to update with the given `mesh`.
  - `mesh` is a pointer to an [XrPassthroughLayerMeshANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrPassthroughLayerMeshANDROID) structure specifying the information of the mesh.

The application **should** specify the number of passthrough mesh indices in the
[XrPassthroughLayerMeshANDROID::vertexCount](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrPassthroughLayerMeshANDROID) and
[XrPassthroughLayerMeshANDROID::indexCount](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrPassthroughLayerMeshANDROID) less than or equal to the
maximum values returned by
[XrSystemPassthroughLayerPropertiesANDROID::maxMeshIndexCount](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrSystemPassthroughLayerPropertiesANDROID) and
[XrSystemPassthroughLayerPropertiesANDROID::maxMeshVertexCount](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrSystemPassthroughLayerPropertiesANDROID) when calling
[xrGetSystemProperties](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrGetSystemProperties). If the count of mesh indices given by `mesh` from
[xrSetPassthroughLayerMeshANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#xrSetPassthroughLayerMeshANDROID) is greater than the maximum values, then
`XR_ERROR_MESH_DATA_LIMIT_EXCEEDED_ANDROID` will be returned.

If the mesh buffer capacity is specified by the
[XrPassthroughLayerCreateInfoANDROID::vertexCapacity](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrPassthroughLayerCreateInfoANDROID) and
[XrPassthroughLayerCreateInfoANDROID::indexCapacity](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrPassthroughLayerCreateInfoANDROID) when creating the
`layer` using [xrCreatePassthroughLayerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#xrCreatePassthroughLayerANDROID), then the
`XR_ERROR_SIZE_INSUFFICIENT` error will be returned on
[xrSetPassthroughLayerMeshANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#xrSetPassthroughLayerMeshANDROID) if
the count of mesh indices defined by `mesh` is greater than the capacity.

### Valid Usage (Implicit)

- The [`XR_ANDROID_composition_layer_passthrough_mesh`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XR_ANDROID_composition_layer_passthrough_mesh) extension **must** be enabled prior to calling [xrSetPassthroughLayerMeshANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#xrSetPassthroughLayerMeshANDROID)
- `layer` **must** be a valid [XrPassthroughLayerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrPassthroughLayerANDROID) handle
- `mesh` **must** be a pointer to a valid [XrPassthroughLayerMeshANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrPassthroughLayerMeshANDROID) structure

### Return Codes

[**Success**](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`
- `XR_SESSION_LOSS_PENDING`

[**Failure**](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_VALIDATION_FAILURE`
- `XR_ERROR_RUNTIME_FAILURE`
- `XR_ERROR_HANDLE_INVALID`
- `XR_ERROR_INSTANCE_LOST`
- `XR_ERROR_SESSION_LOST`
- `XR_ERROR_OUT_OF_MEMORY`
- `XR_ERROR_LIMIT_REACHED`
- `XR_ERROR_SIZE_INSUFFICIENT`
- `XR_ERROR_MESH_DATA_LIMIT_EXCEEDED_ANDROID`

The [XrPassthroughLayerMeshANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrPassthroughLayerMeshANDROID) structure is defined as:

    typedef struct XrPassthroughLayerMeshANDROID {
        XrStructureType          type;
        const void*              next;
        XrWindingOrderANDROID    windingOrder;
        uint32_t                 vertexCount;
        const XrVector3f*        vertices;
        uint32_t                 indexCount;
        const uint16_t*          indices;
    } XrPassthroughLayerMeshANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `windingOrder` is the [XrWindingOrderANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrWindingOrderANDROID) of the mesh triangles, which will be used for backface culling when rendering the mesh.
- `vertexCount` is an `uint32_t` representing the number of vertices in the mesh. When [XrPassthroughLayerCreateInfoANDROID::vertexCapacity](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrPassthroughLayerCreateInfoANDROID) is specified, the `vertexCount` **must** be less than or equal to the `vertexCapacity`.
  - `vertices` is a pointer to an array of `XrVector3f` which contains the vertex positions of the triangle mesh.
- `indexCount` is an `uint32_t` representing the number of indices in the triangle mesh. The last `indexCount % 3` indices, if any, won't be drawn. When [XrPassthroughLayerCreateInfoANDROID::indexCapacity](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrPassthroughLayerCreateInfoANDROID) is specified, the `indexCount` **must** be less than or equal to the `indexCapacity`.
- `indices` is a pointer to an array of `uint16_t` which contains the indices of the triangle mesh.

### Valid Usage (Implicit)

- The [`XR_ANDROID_composition_layer_passthrough_mesh`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XR_ANDROID_composition_layer_passthrough_mesh) extension **must** be enabled prior to using [XrPassthroughLayerMeshANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrPassthroughLayerMeshANDROID)
- `type` **must** be `XR_TYPE_PASSTHROUGH_LAYER_MESH_ANDROID`
- `next` **must** be `NULL` or a valid pointer to the [next structure in a
  structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-valid-usage-for-structure-pointer-chains)
- `windingOrder` **must** be a valid [XrWindingOrderANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrWindingOrderANDROID) value
- If `vertexCount` is not `0, vertices` **must** be a pointer to an array of `vertexCount` [XrVector3f](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrVector3f) structures
- If `indexCount` is not `0, indices` **must** be a pointer to an array of `indexCount uint16_t` values

The [XrWindingOrderANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrWindingOrderANDROID) enumeration identifies the winding order of a
mesh's triangles, used by the runtime for backface culling when rendering the
mesh of the passthrough layer.

    typedef enum XrWindingOrderANDROID {
        XR_WINDING_ORDER_UNKNOWN_ANDROID = 0,
        XR_WINDING_ORDER_CW_ANDROID = 1,
        XR_WINDING_ORDER_CCW_ANDROID = 2
    } XrWindingOrderANDROID;

### Enumerant Descriptions

- `XR_WINDING_ORDER_UNKNOWN_ANDROID`  --- Winding order of the mesh's triangles is not known.
- `XR_WINDING_ORDER_CW_ANDROID`  --- Winding order of the mesh's triangles is clockwise.
- `XR_WINDING_ORDER_CCW_ANDROID`  --- Winding order of the mesh's triangles is counter-clockwise.

## Example code for passthrough layer composition

The following example code demonstrates how to create a passthrough layer and
use it in compositing.

    XrInstance instance; // previously initialized
    XrSystemId systemId; // previously initialized
    XrSession session; // previously initialized
    XrSpace space; // previously initialized

    // The function pointers are previously initialized using xrGetInstanceProcAddr.
    PFN_xrCreatePassthroughLayerANDROID xrCreatePassthroughLayerANDROID; // previously initialized
    PFN_xrDestroyPassthroughLayerANDROID xrDestroyPassthroughLayerANDROID; // previously initialized
    PFN_xrSetPassthroughLayerMeshANDROID xrSetPassthroughLayerMeshANDROID; // previously initialized

    // Inspect passthrough mesh system properties
    XrSystemPassthroughLayerPropertiesANDROID passthroughLayerSystemProperties{
      XR_TYPE_SYSTEM_PASSTHROUGH_LAYER_PROPERTIES_ANDROID};
    XrSystemProperties systemProperties{
      XR_TYPE_SYSTEM_PROPERTIES, &passthroughLayerSystemProperties};
    CHK_XR(xrGetSystemProperties(instance, systemId, &systemProperties));
    if (!passthroughLayerSystemProperties.supportsPassthroughLayer) {
        // the system does not support composite layer passthrough mesh.
        return;
    }

    // The initial mesh for the layer.
    XrPassthroughLayerMeshANDROID mesh = {
      .type = XR_TYPE_PASSTHROUGH_LAYER_MESH_ANDROID,
      .windingOrder = XR_WINDING_ORDER_CW_ANDROID,
      .vertexCount = 4,
      .vertices = {
        { 0, 0, 0 }, { 0, 1, 0 }, { 1, 1, 0 }, { 1, 0, 0 }
      },
      .indexCount = 6,
      .indices = {
        0, 1, 2,
        0, 2, 3
      },
    };

    // Create the layer. Layers are expected to persist across frames.
    XrPassthroughLayerCreateInfoANDROID create_info = {
      .type = XR_TYPE_PASSTHROUGH_LAYER_CREATE_INFO_ANDROID,
      .next = &mesh,
      .vertexCapacity = 0,
      .indexCapacity = 0,
    };
    XrPassthroughLayerANDROID layer;
    CHK_XR(xrCreatePassthroughLayerANDROID(session, &create_info, &layer));

    // Create a composition layer. Composition layers are submitted per frame.
    XrCompositionLayerPassthroughANDROID passthrough_layer = {
      .type = XR_TYPE_COMPOSITION_LAYER_PASSTHROUGH_ANDROID,
      .next = nullptr,
      .layerFlags = 0,
      .space = space,
      .pose = {
        .orientation = { 0.0f, 0.0f, 0.0f, 1.0f }
        .position = { 0.0f, 0.0f, 0.0f }
      },
      .scale = { 1.0f, 1.0f, 1.0f },
      .opacity = 1.0f,
      .layer = layer
    };

    while (1) {
        // ...
        // For every frame in frame loop
        // ...

        // Submit composition layer in xrEndFrame.
        std::vector<XrCompositionLayerBaseHeader*> layers = {
            ...,
            &passthrough_layer,
            ...,
        };
        XrFrameEndInfo end_frame_info = { XR_TYPE_FRAME_END_INFO, nullptr };
        end_frame_info.layerCount = (uint32_t)layers.size();
        end_frame_info.layers = layers.data();
        CHK_XR(xrEndFrame(session, &end_frame_info));

        // Update the layer. Results can be seen the next time a passthrough composition
        // layer is submitted.
        mesh.indexCount = 9;
        const uint16_t new_index_buffer[] = {
            0, 1, 2,
            0, 2, 3,
            0, 1, 2
        };
        mesh.indexBuffer = &new_index_buffer[0];
        CHK_XR(xrSetPassthroughLayerMeshANDROID(&layer, &mesh));

        // ...
        // Finish frame loop
        // ...
    }

    // Clean up.
    CHK_XR(xrDestroyPassthroughLayerANDROID(layer));

**New Object Types**

- [XrPassthroughLayerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrPassthroughLayerANDROID)

**New Enum Constants**

[XrObjectType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrObjectType) enumeration is extended with:

- `XR_OBJECT_TYPE_PASSTHROUGH_LAYER_ANDROID`

[XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) enumeration is extended with:

- `XR_TYPE_PASSTHROUGH_LAYER_CREATE_INFO_ANDROID`
- `XR_TYPE_PASSTHROUGH_LAYER_MESH_ANDROID`
- `XR_TYPE_COMPOSITION_LAYER_PASSTHROUGH_ANDROID`
- `XR_TYPE_SYSTEM_PASSTHROUGH_LAYER_PROPERTIES_ANDROID`

[XrResult](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrResult) enumeration is extended with:

- `XR_ERROR_MESH_DATA_LIMIT_EXCEEDED_ANDROID`

**New Enums**

- [XrWindingOrderANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrWindingOrderANDROID)

**New Structures**

- [XrPassthroughLayerCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrPassthroughLayerCreateInfoANDROID)
- [XrPassthroughLayerMeshANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrPassthroughLayerMeshANDROID)
- [XrCompositionLayerPassthroughANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrCompositionLayerPassthroughANDROID)
- [XrSystemPassthroughLayerPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#XrSystemPassthroughLayerPropertiesANDROID)

**New Functions**

- [xrCreatePassthroughLayerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#xrCreatePassthroughLayerANDROID)
- `xrDestroyPassthroughLayerANDROID`
- [xrSetPassthroughLayerMeshANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh#xrSetPassthroughLayerMeshANDROID)

**Issues**

**Version History**

- Revision 1, 2024-09-11 (Levana Chen)
  - Initial extension description

*** ** * ** ***

OpenXR™ and the OpenXR logo are trademarks owned
by The Khronos Group Inc. and are registered as a trademark in China,
the European Union, Japan and the United Kingdom.