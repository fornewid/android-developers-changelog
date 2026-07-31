{% raw %}
---
title: https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_anchor_space
url: https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_anchor_space
source: md.txt
---

### XR_ANDROID_spatial_anchor_space

**Name String**

`XR_ANDROID_spatial_anchor_space`

**Extension Type**

Instance extension

**Registered Extension Number**

796

**Revision**

1

**Ratification Status**

Not ratified

**Extension and Version Dependencies**

`XR_EXT_spatial_anchor`

**Last Modified Date**

2025-09-15

**IP Status**

No known IP claims.

**Contributors**

YuSheng Chang, Google  

Kyle Chen, Google  

Levana Chen, Google  

Nihav Jain, Google  

Spencer Quin, Google

## Overview

The [xrCreateSpatialAnchorEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateSpatialAnchorEXT) function defined in the `XR_EXT_spatial_anchor` extension allows applications to create spatial anchors with an [XrSpatialEntityEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialEntityEXT) handle to represent it. In contrast, this extension creates a spatial anchor that are represented by an [XrSpace](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpace) handle instead. This is useful for cases where the application wants to:

- Use [xrLocateSpaces](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrLocateSpaces) to get the location of the anchor.
- Locate other spaces relative to the anchor.
- Export the anchor using `XR_ANDROID_anchor_sharing_export` .
- Application has placed anchors and now only cares about the location of the anchors (to attach virtual content to), and does not care about any other component of any other entities discovered via the [XrSpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextEXT) used to create the anchor, thereby allowing the application to destroy the spatial context.

Anchors created with this extension **cannot** be persisted using the `XR_ANDROID_device_anchor_persistence` extension and the application **must** instead use `XR_EXT_spatial_persistence_operations` . The runtime **must** return `XR_ERROR_VALIDATION_FAILURE` from [xrPersistAnchorANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrPersistAnchorANDROID) if [XrPersistedAnchorSpaceInfoANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrPersistedAnchorSpaceInfoANDROID) :: `anchor` is created using [xrCreateSpatialAnchorSpaceANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_anchor_space#xrCreateSpatialAnchorSpaceANDROID) or [xrCreateSpatialAnchorSpaceFromIdANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_anchor_space#xrCreateSpatialAnchorSpaceFromIdANDROID) .

## Create XrSpace for a Spatial Anchor

### Create a spatial anchor and space

The [xrCreateSpatialAnchorSpaceANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_anchor_space#xrCreateSpatialAnchorSpaceANDROID) function is defined as:

    XrResult xrCreateSpatialAnchorSpaceANDROID(
        XrSession                                   session,
        XrSpatialContextEXT                         spatialContext,
        const XrSpatialAnchorCreateInfoEXT*         createInfo,
        XrSpatialEntityIdEXT*                       anchorEntityId,
        XrSpace*                                    anchorSpace);

### Parameter Descriptions

- `session` is a handle to an [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) previously created with [xrCreateSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateSession)
- `spatialContext` is an [XrSpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextEXT) previously created using [xrCreateSpatialContextAsyncEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateSpatialContextAsyncEXT) .
- `createInfo` is a pointer to an [XrSpatialAnchorCreateInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialAnchorCreateInfoEXT) .
- `anchorEntityId` is a pointer to an `XrSpatialEntityIdEXT` .
- `anchorSpace` is a pointer to an [XrSpace](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpace) .

The [xrCreateSpatialAnchorSpaceANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_anchor_space#xrCreateSpatialAnchorSpaceANDROID) function creates an anchor that outputs an `XrSpatialEntityIdEXT` and an [XrSpace](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpace) handle. [xrCreateSpatialAnchorSpaceANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_anchor_space#xrCreateSpatialAnchorSpaceANDROID) has the same validation requirements as [xrCreateSpatialAnchorEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateSpatialAnchorEXT) .

Runtime **must** return `XR_ERROR_VALIDATION_FAILURE` if the [XrSpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextEXT) passed to [xrCreateSpatialAnchorSpaceANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_anchor_space#xrCreateSpatialAnchorSpaceANDROID) was not configured with `XR_SPATIAL_CAPABILITY_ANCHOR_EXT` .

With respect to the discoverability of the created anchor by [xrCreateSpatialAnchorSpaceANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_anchor_space#xrCreateSpatialAnchorSpaceANDROID) , the last paragraph of the [xrCreateSpatialAnchorEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateSpatialAnchorEXT) spec applies.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_anchor_space#VUID-xrCreateSpatialAnchorSpaceANDROID-extension-notenabled) The `XR_ANDROID_spatial_anchor_space` extension **must** be enabled prior to calling [xrCreateSpatialAnchorSpaceANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_anchor_space#xrCreateSpatialAnchorSpaceANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_anchor_space#VUID-xrCreateSpatialAnchorSpaceANDROID-session-parameter) `session` **must** be a valid [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_anchor_space#VUID-xrCreateSpatialAnchorSpaceANDROID-spatialContext-parameter) `spatialContext` **must** be a valid [XrSpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextEXT) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_anchor_space#VUID-xrCreateSpatialAnchorSpaceANDROID-createInfo-parameter) `createInfo` **must** be a pointer to a valid [XrSpatialAnchorCreateInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialAnchorCreateInfoEXT) structure
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_anchor_space#VUID-xrCreateSpatialAnchorSpaceANDROID-anchorEntityId-parameter) `anchorEntityId` **must** be a pointer to an `XrSpatialEntityIdEXT` value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_anchor_space#VUID-xrCreateSpatialAnchorSpaceANDROID-anchorSpace-parameter) `anchorSpace` **must** be a pointer to an [XrSpace](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpace) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_anchor_space#VUID-xrCreateSpatialAnchorSpaceANDROID-spatialContext-parent) `spatialContext` **must** have been created, allocated, or retrieved from `session`

### Return Codes

[Success](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`
- `XR_SESSION_LOSS_PENDING`

[Failure](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_HANDLE_INVALID`
- `XR_ERROR_INSTANCE_LOST`
- `XR_ERROR_LIMIT_REACHED`
- `XR_ERROR_OUT_OF_MEMORY`
- `XR_ERROR_POSE_INVALID`
- `XR_ERROR_RUNTIME_FAILURE`
- `XR_ERROR_SESSION_LOST`
- `XR_ERROR_SPATIAL_ANCHOR_ATTACHABLE_COMPONENT_NOT_FOUND_ANDROID`
- `XR_ERROR_SPATIAL_ENTITY_ID_INVALID_EXT`
- `XR_ERROR_TIME_INVALID`
- `XR_ERROR_VALIDATION_FAILURE`

### Create XrSpace from an existing spatial anchor

The [xrCreateSpatialAnchorSpaceFromIdANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_anchor_space#xrCreateSpatialAnchorSpaceFromIdANDROID) function is defined as:

    XrResult xrCreateSpatialAnchorSpaceFromIdANDROID(
        XrSession                                   session,
        XrSpatialContextEXT                         spatialContext,
        const XrSpatialAnchorSpaceFromIdCreateInfoANDROID* createInfo,
        XrSpace*                                    anchorSpace);

### Parameter Descriptions

- `session` is a handle to an [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) previously created with [xrCreateSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateSession)
- `spatialContext` is an [XrSpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextEXT) previously created using [xrCreateSpatialContextAsyncEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateSpatialContextAsyncEXT) .
- `createInfo` is a pointer to an [XrSpatialAnchorSpaceFromIdCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_anchor_space#XrSpatialAnchorSpaceFromIdCreateInfoANDROID) .
- `anchorSpace` is a pointer to an [XrSpace](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpace) .

In scenarios where spatial anchor entities are preexisting (e.g. due to persistence), applications **can** create an [XrSpace](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpace) from these spatial anchors by supplying their spatial entity IDs.

The [xrCreateSpatialAnchorSpaceFromIdANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_anchor_space#xrCreateSpatialAnchorSpaceFromIdANDROID) function creates an [XrSpace](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpace) handle by providing an `XrSpatialEntityIdEXT` in the [XrSpatialAnchorSpaceFromIdCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_anchor_space#XrSpatialAnchorSpaceFromIdCreateInfoANDROID) ::entityId field.

Runtime **must** return `XR_ERROR_VALIDATION_FAILURE` if the [XrSpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextEXT) passed to [xrCreateSpatialAnchorSpaceFromIdANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_anchor_space#xrCreateSpatialAnchorSpaceFromIdANDROID) was not configured with `XR_SPATIAL_CAPABILITY_ANCHOR_EXT` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_anchor_space#VUID-xrCreateSpatialAnchorSpaceFromIdANDROID-extension-notenabled) The `XR_ANDROID_spatial_anchor_space` extension **must** be enabled prior to calling [xrCreateSpatialAnchorSpaceFromIdANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_anchor_space#xrCreateSpatialAnchorSpaceFromIdANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_anchor_space#VUID-xrCreateSpatialAnchorSpaceFromIdANDROID-session-parameter) `session` **must** be a valid [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_anchor_space#VUID-xrCreateSpatialAnchorSpaceFromIdANDROID-spatialContext-parameter) `spatialContext` **must** be a valid [XrSpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextEXT) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_anchor_space#VUID-xrCreateSpatialAnchorSpaceFromIdANDROID-createInfo-parameter) `createInfo` **must** be a pointer to a valid [XrSpatialAnchorSpaceFromIdCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_anchor_space#XrSpatialAnchorSpaceFromIdCreateInfoANDROID) structure
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_anchor_space#VUID-xrCreateSpatialAnchorSpaceFromIdANDROID-anchorSpace-parameter) `anchorSpace` **must** be a pointer to an [XrSpace](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpace) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_anchor_space#VUID-xrCreateSpatialAnchorSpaceFromIdANDROID-spatialContext-parent) `spatialContext` **must** have been created, allocated, or retrieved from `session`

### Return Codes

[Success](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`
- `XR_SESSION_LOSS_PENDING`

[Failure](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_HANDLE_INVALID`
- `XR_ERROR_INSTANCE_LOST`
- `XR_ERROR_LIMIT_REACHED`
- `XR_ERROR_OUT_OF_MEMORY`
- `XR_ERROR_RUNTIME_FAILURE`
- `XR_ERROR_SESSION_LOST`
- `XR_ERROR_SPATIAL_ANCHOR_ENTITY_ID_INVALID_ANDROID`
- `XR_ERROR_SPATIAL_ENTITY_ID_INVALID_EXT`
- `XR_ERROR_VALIDATION_FAILURE`

The [XrSpatialAnchorSpaceFromIdCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_anchor_space#XrSpatialAnchorSpaceFromIdCreateInfoANDROID) structure is defined as:

    typedef struct XrSpatialAnchorSpaceFromIdCreateInfoANDROID {
        XrStructureType         type;
        const void*             next;
        XrSpatialEntityIdEXT    anchorEntityId;
    } XrSpatialAnchorSpaceFromIdCreateInfoANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `anchorEntityId` is the `XrSpatialEntityIdEXT` of the existing spatial anchor from which to create the [XrSpace](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpace) .

The runtime **must** return `XR_ERROR_SPATIAL_ENTITY_ID_INVALID_EXT` if [XrSpatialAnchorSpaceFromIdCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_anchor_space#XrSpatialAnchorSpaceFromIdCreateInfoANDROID) ::entityId is not a valid ID for `spatialContext` .

The runtime **must** return `XR_ERROR_SPATIAL_ANCHOR_ENTITY_ID_INVALID_ANDROID` if [XrSpatialAnchorSpaceFromIdCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_anchor_space#XrSpatialAnchorSpaceFromIdCreateInfoANDROID) ::entityId is not a valid entity ID for an anchor.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_anchor_space#VUID-XrSpatialAnchorSpaceFromIdCreateInfoANDROID-extension-notenabled) The `XR_ANDROID_spatial_anchor_space` extension **must** be enabled prior to using [XrSpatialAnchorSpaceFromIdCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_anchor_space#XrSpatialAnchorSpaceFromIdCreateInfoANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_anchor_space#VUID-XrSpatialAnchorSpaceFromIdCreateInfoANDROID-type-type) `type` **must** be `XR_TYPE_SPATIAL_ANCHOR_SPACE_FROM_ID_CREATE_INFO_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_anchor_space#VUID-XrSpatialAnchorSpaceFromIdCreateInfoANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)

## Anchor Lifecycle

The parent of an [XrSpace](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpace) handle is an [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) . This implies that an [XrSpace](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpace) handle representing the anchor remains valid even after [xrCreateSpatialAnchorSpaceFromIdANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_anchor_space#xrCreateSpatialAnchorSpaceFromIdANDROID) :: `spatialContext` or [xrCreateSpatialAnchorSpaceANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_anchor_space#xrCreateSpatialAnchorSpaceANDROID) :: `spatialContext` are destroyed. Creating an [XrSpace](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpace) to represent a spatial entity anchor allows the application to destroy the [XrSpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextEXT) that was configured with `XR_SPATIAL_CAPABILITY_ANCHOR_EXT` while still continuing to get the latest pose of the anchor using its [XrSpace](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpace) with [xrLocateSpaces](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrLocateSpaces) i.e. the runtime **must** continue to track the anchor until all [XrSpace](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpace) handles that represent it have been destroyed.

## Example code

### Create spatial anchor as an XrSpace

The following example code demonstrates how to create a spatial anchor and return it as an [XrSpace](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpace) .

    XrSpatialEntityIdEXT spatialAnchorEntityId;
    XrSpace spatialAnchorSpace {XR_NULL_HANDLE}; // XrSpace handle of anchor

    // Spatial anchor create info
    XrSpatialAnchorCreateInfoEXT createInfo{
      .type = XR_TYPE_SPATIAL_ANCHOR_CREATE_INFO_EXT,
      .baseSpace = localSpace,
      .time = predictedDisplayTime,
      .pose = {{0, 0, 0, 1}, {1, 1, 1}},
    };

    // Create spatial anchor using the new API
    CHK_XR(xrCreateSpatialAnchorSpaceANDROID(session, spatialContext, &createInfo, &spatialAnchorEntityId, &spatialAnchorSpace));

    // ...

### Create XrSpace from anchor entity ID

The following example code demonstrates how to create an [XrSpace](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpace) from a preexisting anchor entity ID.

    XrSpace anchorSpace = XR_NULL_HANDLE;

    // Spatial anchor from XrSpace create info
    XrSpatialAnchorSpaceFromIdCreateInfoANDROID createInfoFromId{
      .type = XR_TYPE_SPATIAL_ANCHOR_SPACE_FROM_ID_CREATE_INFO_ANDROID,
      .anchorEntityId = spatialAnchorEntityId,
    };

    // Create XrSpace handle from spatial anchor ID
    CHK_XR(xrCreateSpatialAnchorSpaceFromIdANDROID(session, spatialContext, &createInfoFromId, &anchorSpace));

    // ...

## New Commands

- [xrCreateSpatialAnchorSpaceANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_anchor_space#xrCreateSpatialAnchorSpaceANDROID)
- [xrCreateSpatialAnchorSpaceFromIdANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_anchor_space#xrCreateSpatialAnchorSpaceFromIdANDROID)

## New Structures

- [XrSpatialAnchorSpaceFromIdCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_anchor_space#XrSpatialAnchorSpaceFromIdCreateInfoANDROID)

## New Enum Constants

- `XR_ANDROID_SPATIAL_ANCHOR_SPACE_EXTENSION_NAME`
- `XR_ANDROID_spatial_anchor_space_SPEC_VERSION`
- Extending [XrResult](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrResult) :

  - `XR_ERROR_SPATIAL_ANCHOR_ENTITY_ID_INVALID_ANDROID`
- Extending [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) :

  - `XR_TYPE_SPATIAL_ANCHOR_SPACE_FROM_ID_CREATE_INFO_ANDROID`

## Issues

## Version History

- Revision 1, 2025-09-15 (YuSheng Chang, Kyle Chen)

  - Initial extension description.
{% endraw %}
