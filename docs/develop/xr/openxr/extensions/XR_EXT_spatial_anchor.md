{% raw %}
---
title: https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_anchor
url: https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_anchor
source: md.txt
---

### XR_EXT_spatial_anchor

**Name String**

`XR_EXT_spatial_anchor`

**Extension Type**

Instance extension

**Registered Extension Number**

763

**Revision**

1

**Ratification Status**

Ratified

**Extension and Version Dependencies**

`XR_EXT_spatial_entity`

**Contributors**

Nihav Jain, Google  

Natalie Fleury, Meta  

Yuichi Taguchi, Meta  

Ron Bessems, Meta  

Yin Li, Microsoft  

Jimmy Alamparambil, ByteDance  

Zhipeng Liu, ByteDance  

Jun Yan, ByteDance

## Overview

This extension builds on `XR_EXT_spatial_entity` and allows applications to create spatial anchors, which are arbitrary points in the user's physical environment that will then be tracked by the runtime. The runtime **should** then adjust the position and orientation of the anchor's origin over time as needed, independent of all other spaces \& anchors, to ensure that it maintains its original mapping to the real world.

An anchor that tracks a given position and orientation within an [XrSpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextEXT) is represented as a spatial entity with (or "that has") the `XR_SPATIAL_COMPONENT_TYPE_ANCHOR_EXT` component.

## Benefit of using anchors

As the runtime's understanding of the user's physical environment updates throughout the lifetime of an [XrSpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextEXT) , virtual objects **may** appear to drift away from where they were placed by the application, which impacts the application's realism and the quality of the user's experience. By creating an anchor close to where a virtual object is placed, and then always rendering that virtual object relative to its anchor, an application **can** ensure that each virtual object appears to stay at the same position and orientation in the physical environment. Also, unlike certain reference spaces, anchors are unaffected by system-level recentering.

## Runtime support

If the runtime supports spatial anchors, it **must** indicate this by enumerating `XR_SPATIAL_CAPABILITY_ANCHOR_EXT` in [xrEnumerateSpatialCapabilitiesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrEnumerateSpatialCapabilitiesEXT) .

## Configuration

The [XrSpatialCapabilityConfigurationAnchorEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_anchor#XrSpatialCapabilityConfigurationAnchorEXT) structure is defined as:

    typedef struct XrSpatialCapabilityConfigurationAnchorEXT {
        XrStructureType                     type;
        const void*                         next;
        XrSpatialCapabilityEXT              capability;
        uint32_t                            enabledComponentCount;
        const XrSpatialComponentTypeEXT*    enabledComponents;
    } XrSpatialCapabilityConfigurationAnchorEXT;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `capability` is an [XrSpatialCapabilityEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityEXT) .
- `enabledComponentCount` is a `uint32_t` describing the count of elements in the `enabledComponents` array.
- `enabledComponents` is a pointer to an array of [XrSpatialComponentTypeEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentTypeEXT) .

Applications **can** enable the `XR_SPATIAL_CAPABILITY_ANCHOR_EXT` spatial capability by including a pointer to an [XrSpatialCapabilityConfigurationAnchorEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_anchor#XrSpatialCapabilityConfigurationAnchorEXT) structure in [XrSpatialContextCreateInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextCreateInfoEXT) :: `capabilityConfigs` .

The runtime **must** return `XR_ERROR_VALIDATION_FAILURE` if `capability` is not `XR_SPATIAL_CAPABILITY_ANCHOR_EXT` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_anchor#VUID-XrSpatialCapabilityConfigurationAnchorEXT-extension-notenabled) The `XR_EXT_spatial_anchor` extension **must** be enabled prior to using [XrSpatialCapabilityConfigurationAnchorEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_anchor#XrSpatialCapabilityConfigurationAnchorEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_anchor#VUID-XrSpatialCapabilityConfigurationAnchorEXT-type-type) `type` **must** be `XR_TYPE_SPATIAL_CAPABILITY_CONFIGURATION_ANCHOR_EXT`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_anchor#VUID-XrSpatialCapabilityConfigurationAnchorEXT-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_anchor#VUID-XrSpatialCapabilityConfigurationAnchorEXT-capability-parameter) `capability` **must** be a valid [XrSpatialCapabilityEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityEXT) value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_anchor#VUID-XrSpatialCapabilityConfigurationAnchorEXT-enabledComponents-parameter) `enabledComponents` **must** be a pointer to an array of `enabledComponentCount` valid [XrSpatialComponentTypeEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentTypeEXT) values
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_anchor#VUID-XrSpatialCapabilityConfigurationAnchorEXT-enabledComponentCount-arraylength) The `enabledComponentCount` parameter **must** be greater than `0`

## Guaranteed Components

A runtime that supports `XR_SPATIAL_CAPABILITY_ANCHOR_EXT` **must** provide the following spatial components as guaranteed components of all entities created or discovered by this capability and **must** enumerate them in [xrEnumerateSpatialCapabilityComponentTypesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrEnumerateSpatialCapabilityComponentTypesEXT) :

- `XR_SPATIAL_COMPONENT_TYPE_ANCHOR_EXT`

### Anchor Component

###### Component Data

The `XR_SPATIAL_COMPONENT_TYPE_ANCHOR_EXT` uses [XrPosef](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrPosef) for its data which provides the position and orientation of the anchor.

###### Component List Structure to Query Data

The [XrSpatialComponentAnchorListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_anchor#XrSpatialComponentAnchorListEXT) structure is defined as:

    typedef struct XrSpatialComponentAnchorListEXT {
        XrStructureType    type;
        void*              next;
        uint32_t           locationCount;
        XrPosef*           locations;
    } XrSpatialComponentAnchorListEXT;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `locationCount` is a `uint32_t` describing the count of elements in the `locations` array.
- `locations` is an array of [XrPosef](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrPosef) .

The runtime **must** return `XR_ERROR_VALIDATION_FAILURE` from [xrQuerySpatialComponentDataEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrQuerySpatialComponentDataEXT) if [XrSpatialComponentAnchorListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_anchor#XrSpatialComponentAnchorListEXT) is in the [XrSpatialComponentDataQueryResultEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryResultEXT) :: `next` chain but `XR_SPATIAL_COMPONENT_TYPE_ANCHOR_EXT` is not included in [XrSpatialComponentDataQueryConditionEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryConditionEXT) :: `componentTypes` .

The runtime **must** return `XR_ERROR_SIZE_INSUFFICIENT` from [xrQuerySpatialComponentDataEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrQuerySpatialComponentDataEXT) if `locationCount` is less than [XrSpatialComponentDataQueryResultEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryResultEXT) :: `entityIdCountOutput` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_anchor#VUID-XrSpatialComponentAnchorListEXT-extension-notenabled) The `XR_EXT_spatial_anchor` extension **must** be enabled prior to using [XrSpatialComponentAnchorListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_anchor#XrSpatialComponentAnchorListEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_anchor#VUID-XrSpatialComponentAnchorListEXT-type-type) `type` **must** be `XR_TYPE_SPATIAL_COMPONENT_ANCHOR_LIST_EXT`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_anchor#VUID-XrSpatialComponentAnchorListEXT-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_anchor#VUID-XrSpatialComponentAnchorListEXT-locations-parameter) `locations` **must** be a pointer to an array of `locationCount` [XrPosef](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrPosef) structures
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_anchor#VUID-XrSpatialComponentAnchorListEXT-locationCount-arraylength) The `locationCount` parameter **must** be greater than `0`

###### Configuration

If `XR_SPATIAL_COMPONENT_TYPE_ANCHOR_EXT` is enumerated in [XrSpatialCapabilityComponentTypesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityComponentTypesEXT) :: `componentTypes` for some capability, an application **can** enable it by including the enumerant in the [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityConfigurationBaseHeaderEXT) :: `enabledComponents` list of the [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityConfigurationBaseHeaderEXT) derived structure of the capability that supports this component.

This component does not require any special configuration to be included in the [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityConfigurationBaseHeaderEXT) :: `next` chain.

## Creating a Spatial Anchor

The [xrCreateSpatialAnchorEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_anchor#xrCreateSpatialAnchorEXT) function is defined as:

    XrResult xrCreateSpatialAnchorEXT(
        XrSpatialContextEXT                         spatialContext,
        const XrSpatialAnchorCreateInfoEXT*         createInfo,
        XrSpatialEntityIdEXT*                       anchorEntityId,
        XrSpatialEntityEXT*                         anchorEntity);

### Parameter Descriptions

- `spatialContext` is an [XrSpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextEXT) previously created using [xrCreateSpatialContextAsyncEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateSpatialContextAsyncEXT) .
- `createInfo` is a pointer to an [XrSpatialAnchorCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_anchor#XrSpatialAnchorCreateInfoEXT) .
- `anchorEntityId` is a pointer to an `XrSpatialEntityIdEXT` in which the anchor entity's ID is returned.
- `anchorEntity` is a pointer to an [XrSpatialEntityEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialEntityEXT) in which the anchor entity's handle is returned.

The application **can** create a spatial anchor by using [xrCreateSpatialAnchorEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_anchor#xrCreateSpatialAnchorEXT) .

To get updated component data for an anchor, pass the value populated in `anchorEntity` into the [XrSpatialUpdateSnapshotCreateInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialUpdateSnapshotCreateInfoEXT) :: `entities` when creating a snapshot. The application **can** use `anchorEntityId` to uniquely identify this anchor in the [XrSpatialComponentDataQueryResultEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryResultEXT) :: `entityIds` array when using [xrQuerySpatialComponentDataEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrQuerySpatialComponentDataEXT) .

The runtime **must** return `XR_ERROR_VALIDATION_FAILURE` from [xrCreateSpatialAnchorEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_anchor#xrCreateSpatialAnchorEXT) if `XR_SPATIAL_CAPABILITY_ANCHOR_EXT` was not configured for `spatialContext` . See [Configuration](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_anchor#ext_spatial_anchor_config) for how to configure an [XrSpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextEXT) for the `XR_SPATIAL_CAPABILITY_ANCHOR_EXT` capability.

The anchor represented by `anchorEntity` is only valid for the lifetime of `spatialContext` , or until the application calls [xrDestroySpatialEntityEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrDestroySpatialEntityEXT) on it, whichever comes first. Other extensions **may** offer functions to persist this newly created anchor across multiple [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) or to share it across process boundaries with other applications.

A newly created anchor, until destroyed, **must** be discoverable in its parent spatial context. This means that the runtime **must** include `anchorEntityId` in the snapshot created using [xrCreateSpatialDiscoverySnapshotAsyncEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateSpatialDiscoverySnapshotAsyncEXT) for `spatialContext` if the anchor matches the discovery criteria set in [XrSpatialDiscoverySnapshotCreateInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialDiscoverySnapshotCreateInfoEXT) . The newly created anchor **may** also be discoverable in other spatial contexts configured with `XR_SPATIAL_CAPABILITY_ANCHOR_EXT` , although with a different `XrSpatialEntityIdEXT` since a particular `XrSpatialEntityIdEXT` is unique to its [XrSpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextEXT) .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_anchor#VUID-xrCreateSpatialAnchorEXT-extension-notenabled) The `XR_EXT_spatial_anchor` extension **must** be enabled prior to calling [xrCreateSpatialAnchorEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_anchor#xrCreateSpatialAnchorEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_anchor#VUID-xrCreateSpatialAnchorEXT-spatialContext-parameter) `spatialContext` **must** be a valid [XrSpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextEXT) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_anchor#VUID-xrCreateSpatialAnchorEXT-createInfo-parameter) `createInfo` **must** be a pointer to a valid [XrSpatialAnchorCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_anchor#XrSpatialAnchorCreateInfoEXT) structure
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_anchor#VUID-xrCreateSpatialAnchorEXT-anchorEntityId-parameter) `anchorEntityId` **must** be a pointer to an `XrSpatialEntityIdEXT` value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_anchor#VUID-xrCreateSpatialAnchorEXT-anchorEntity-parameter) `anchorEntity` **must** be a pointer to an [XrSpatialEntityEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialEntityEXT) handle

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
- `XR_ERROR_TIME_INVALID`
- `XR_ERROR_VALIDATION_FAILURE`
- `XR_ERROR_SPATIAL_ANCHOR_ATTACHABLE_COMPONENT_NOT_FOUND_ANDROID` (if `XR_ANDROID_spatial_entity_bound_anchor` is enabled)
- `XR_ERROR_SPATIAL_ENTITY_ID_INVALID_EXT` (if `XR_ANDROID_spatial_entity_bound_anchor` is enabled)

The [XrSpatialAnchorCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_anchor#XrSpatialAnchorCreateInfoEXT) structure is defined as:

    typedef struct XrSpatialAnchorCreateInfoEXT {
        XrStructureType    type;
        const void*        next;
        XrSpace            baseSpace;
        XrTime             time;
        XrPosef            pose;
    } XrSpatialAnchorCreateInfoEXT;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `baseSpace` is the [XrSpace](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpace) in which `pose` is applied.
- `time` is the `XrTime` at which `baseSpace` is located (and `pose` is applied).
- `pose` is the location for the anchor entity.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_anchor#VUID-XrSpatialAnchorCreateInfoEXT-extension-notenabled) The `XR_EXT_spatial_anchor` extension **must** be enabled prior to using [XrSpatialAnchorCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_anchor#XrSpatialAnchorCreateInfoEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_anchor#VUID-XrSpatialAnchorCreateInfoEXT-type-type) `type` **must** be `XR_TYPE_SPATIAL_ANCHOR_CREATE_INFO_EXT`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_anchor#VUID-XrSpatialAnchorCreateInfoEXT-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains) . See also: [XrSpatialAnchorParentANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialAnchorParentANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_anchor#VUID-XrSpatialAnchorCreateInfoEXT-baseSpace-parameter) `baseSpace` **must** be a valid [XrSpace](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpace) handle

## Query Anchor Pose

After the anchor is created, the runtime **should** then adjust its position and orientation over time relative to other spaces in order to maintain the best possible alignment to its original real-world location, even if that changes the anchor's relationship to the original [XrSpatialAnchorCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_anchor#XrSpatialAnchorCreateInfoEXT) :: `baseSpace` used to initialize it.

The application **can** use [xrCreateSpatialUpdateSnapshotEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateSpatialUpdateSnapshotEXT) with the anchor's [XrSpatialEntityEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialEntityEXT) to create a new [XrSpatialSnapshotEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialSnapshotEXT) and then query the `XR_SPATIAL_COMPONENT_TYPE_ANCHOR_EXT` component from that snapshot using [xrQuerySpatialComponentDataEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrQuerySpatialComponentDataEXT) . The application **can** add [XrSpatialComponentAnchorListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_anchor#XrSpatialComponentAnchorListEXT) to [XrSpatialComponentDataQueryResultEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryResultEXT) :: `next` to retrieve the latest location data for the anchors.

The runtime **may** set the tracking state of a newly created anchor to `XR_SPATIAL_ENTITY_TRACKING_STATE_PAUSED_EXT` . The application **must** only read the anchor entity's state provided in [XrSpatialComponentDataQueryResultEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryResultEXT) :: `entityStates` and the entity's anchor component data if the tracking state is `XR_SPATIAL_ENTITY_TRACKING_STATE_TRACKING_EXT` .

## Guidelines For Using Anchors

- Each anchor's pose adjusts independent of any other anchor or space. Separately anchored virtual objects **may** shift or rotate relative to each other, breaking the spatial hierarchy in cases where these virtual objects are expected to stay in place relative to each other. For such cases, the application **should** reuse the same anchor for all virtual objects that do not move relative to each other.
- Application **should** destroy any [XrSpatialEntityEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialEntityEXT) handles for anchors that are no longer being used in order to free up the resources the runtime **may** be using to track those anchors.

## Example Code

### Configure Anchor Capability

The following example demonstrates how to configure the anchor capability when creating a spatial context.

    // Create a spatial spatial context
    XrSpatialContextEXT spatialContext{};
    {

      std::vector<XrSpatialComponentTypeEXT> enabledComponents = {
        XR_SPATIAL_COMPONENT_TYPE_ANCHOR_EXT,
      };

      XrSpatialCapabilityConfigurationAnchorEXT anchorConfig{XR_TYPE_SPATIAL_CAPABILITY_CONFIGURATION_ANCHOR_EXT};
      anchorConfig.capability = XR_SPATIAL_CAPABILITY_ANCHOR_EXT;
      anchorConfig.enabledComponentCount = enabledComponents.size();
      anchorConfig.enabledComponents = enabledComponents.data();

      std::array<XrSpatialCapabilityConfigurationBaseHeaderEXT*, 1> capabilityConfigs = {
        reinterpret_cast<XrSpatialCapabilityConfigurationBaseHeaderEXT*>(&anchorConfig),
      };

      XrSpatialContextCreateInfoEXT spatialContextCreateInfo{XR_TYPE_SPATIAL_CONTEXT_CREATE_INFO_EXT};
      spatialContextCreateInfo.capabilityConfigCount = capabilityConfigs.size();
      spatialContextCreateInfo.capabilityConfigs = capabilityConfigs.data();
      XrFutureEXT createContextFuture;
      CHK_XR(xrCreateSpatialContextAsyncEXT(session, &spatialContextCreateInfo, &createContextFuture));

      waitUntilReady(createContextFuture);

      XrCreateSpatialContextCompletionEXT completion{XR_TYPE_CREATE_SPATIAL_CONTEXT_COMPLETION_EXT};
      CHK_XR(xrCreateSpatialContextCompleteEXT(session, createContextFuture, &completion));
      if (completion.futureResult != XR_SUCCESS) {
        return;
      }

      spatialContext = completion.spatialContext;
    }

    // ...
    // Create spatial anchors and get their latest pose in the frame loop.
    // ...

    CHK_XR(xrDestroySpatialContextEXT(spatialContext));

### Create Spatial Anchor \& Get Its Location

The following example demonstrates how to create a spatial anchor \& gets its pose every frame.

    XrSpatialAnchorCreateInfoEXT createInfo{XR_TYPE_SPATIAL_ANCHOR_CREATE_INFO_EXT};
    createInfo.baseSpace = localSpace;
    createInfo.time = predictedDisplayTime;
    createInfo.pose = {{0, 0, 0, 1}, {1, 1, 1}};

    XrSpatialEntityIdEXT spatialAnchorEntityId;
    XrSpatialEntityEXT spatialAnchorEntity;
    CHK_XR(xrCreateSpatialAnchorEXT(spatialContext, &createInfo, &spatialAnchorEntityId, &spatialAnchorEntity));

    auto updateAnchorLocation = [&](XrTime time) {
      // We want to get updated data for all components of the entities, so skip specifying componentTypes.
      XrSpatialUpdateSnapshotCreateInfoEXT snapshotCreateInfo{XR_TYPE_SPATIAL_UPDATE_SNAPSHOT_CREATE_INFO_EXT};
      snapshotCreateInfo.entityCount = 1;
      snapshotCreateInfo.entities = &spatialAnchorEntity;
      snapshotCreateInfo.baseSpace = localSpace;
      snapshotCreateInfo.time = time;

      XrSpatialSnapshotEXT snapshot;
      CHK_XR(xrCreateSpatialUpdateSnapshotEXT(spatialContext, &snapshotCreateInfo, &snapshot));

      // Query for the entities that have the anchor component on them.
      std::array<XrSpatialComponentTypeEXT, 1> componentsToQuery {XR_SPATIAL_COMPONENT_TYPE_ANCHOR_EXT};
      XrSpatialComponentDataQueryConditionEXT queryCond{XR_TYPE_SPATIAL_COMPONENT_DATA_QUERY_CONDITION_EXT};
      queryCond.componentTypeCount = componentsToQuery.size();
      queryCond.componentTypes = componentsToQuery.data();

      XrSpatialComponentDataQueryResultEXT queryResult{XR_TYPE_SPATIAL_COMPONENT_DATA_QUERY_RESULT_EXT};
      CHK_XR(xrQuerySpatialComponentDataEXT(snapshot, &queryCond, &queryResult));

      std::vector<XrSpatialEntityIdEXT> entityIds(queryResult.entityIdCountOutput);
      std::vector<XrSpatialEntityTrackingStateEXT> entityStates(queryResult.entityIdCountOutput);
      queryResult.entityIdCapacityInput = entityIds.size();
      queryResult.entityIds = entityIds.data();
      queryResult.entityStateCapacityInput = entityStates.size();
      queryResult.entityStates = entityStates.data();

      // query for the pose data
      std::vector<XrPosef> locations(queryResult.entityIdCountOutput);
      XrSpatialComponentAnchorListEXT locationList{XR_TYPE_SPATIAL_COMPONENT_ANCHOR_LIST_EXT};
      locationList.locationCount = locations.size();
      locationList.locations = locations.data();
      queryResult.next = &locationList;

      CHK_XR(xrQuerySpatialComponentDataEXT(snapshot, &queryCond, &queryResult));

      for (int32_t i = 0; i < queryResult.entityIdCountOutput; ++i) {
        if (entityStates[i] == XR_SPATIAL_ENTITY_TRACKING_STATE_TRACKING_EXT) {
          // Pose for entity entityIds[i] is locations[i].
        }
      }

      CHK_XR(xrDestroySpatialSnapshotEXT(snapshot));
    };


    while (1) {
      // ...
      // For every frame in frame loop
      // ...

      XrFrameState frameState;  // previously returned from xrWaitFrame
      const XrTime time = frameState.predictedDisplayTime;

      updateAnchorLocation(time);

      // ...
      // Finish frame loop
      // ...
    }

    CHK_XR(xrDestroySpatialEntityEXT(spatialAnchorEntity));

## New Commands

- [xrCreateSpatialAnchorEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_anchor#xrCreateSpatialAnchorEXT)

## New Structures

- [XrSpatialAnchorCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_anchor#XrSpatialAnchorCreateInfoEXT)
- [XrSpatialCapabilityConfigurationAnchorEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_anchor#XrSpatialCapabilityConfigurationAnchorEXT)
- Extending [XrSpatialComponentDataQueryResultEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryResultEXT) :

  - [XrSpatialComponentAnchorListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_anchor#XrSpatialComponentAnchorListEXT)

## New Enum Constants

- `XR_EXT_SPATIAL_ANCHOR_EXTENSION_NAME`
- `XR_EXT_spatial_anchor_SPEC_VERSION`
- Extending [XrSpatialCapabilityEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityEXT) :

  - `XR_SPATIAL_CAPABILITY_ANCHOR_EXT`
- Extending [XrSpatialComponentTypeEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentTypeEXT) :

  - `XR_SPATIAL_COMPONENT_TYPE_ANCHOR_EXT`
- Extending [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) :

  - `XR_TYPE_SPATIAL_ANCHOR_CREATE_INFO_EXT`
  - `XR_TYPE_SPATIAL_CAPABILITY_CONFIGURATION_ANCHOR_EXT`
  - `XR_TYPE_SPATIAL_COMPONENT_ANCHOR_LIST_EXT`

## Issues

- Why does [xrCreateSpatialAnchorEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_anchor#xrCreateSpatialAnchorEXT) output an entity ID as well as an entity handle?

  - Resolved
  - Answer: The [xrCreateSpatialAnchorEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_anchor#xrCreateSpatialAnchorEXT) function could very well have provided just the entity id as the output and applications could create an entity handle for that id using [xrCreateSpatialEntityFromIdEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateSpatialEntityFromIdEXT) . However, given the typical usage of an anchor where applications query the anchor pose every frame, it becomes a good candidate to be used in an "update snapshot", which requires entity handles as input. Anticipating this typical usecase, [xrCreateSpatialAnchorEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_anchor#xrCreateSpatialAnchorEXT) performs [xrCreateSpatialEntityFromIdEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateSpatialEntityFromIdEXT) on behalf of the application and provides it with the entity handle to use with [xrCreateSpatialUpdateSnapshotEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateSpatialUpdateSnapshotEXT) .

## Version History

- Revision 1, 2024-07-10 (Nihav Jain, Google)

  - Initial extension description
{% endraw %}
