---
title: https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast
url: https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast
source: md.txt
---

### XR_ANDROID_spatial_discovery_raycast

**Name String**

`XR_ANDROID_spatial_discovery_raycast`

**Extension Type**

Instance extension

**Registered Extension Number**

787

**Revision**

1

**Ratification Status**

Not ratified

**Extension and Version Dependencies**

`XR_EXT_spatial_entity`

**Last Modified Date**

2025-08-12

**IP Status**

No known IP claims.

**Contributors**

Brian Chen, Google  

Levana Chen, Google  

Kyle Chen, Google  

Nihav Jain, Google  

Spencer Quin, Google  

Natalie Fleury, Meta  

Yuichi Taguchi, Meta  

Jimmy Alamparambil, ByteDance  

Zhipeng Liu, ByteDance

## Overview

This extension builds on `XR_EXT_spatial_entity` and provides raycast functionality for existing spatial capabilities, such as `XR_SPATIAL_CAPABILITY_PLANE_TRACKING_EXT` , to discover spatial entities.

This extension also introduces a new spatial capability for raycasting against depth buffer.

### Permissions

Required permissions depending on the capabilities the Android application uses. If `XR_SPATIAL_CAPABILITY_DEPTH_RAYCAST_ANDROID` is used, the application **must** have android.permission.SCENE_UNDERSTANDING_FINE permission. If `XR_SPATIAL_CAPABILITY_PLANE_TRACKING_EXT` is used, the application **must** have android.permission.SCENE_UNDERSTANDING_COARSE permission. The android.permission.SCENE_UNDERSTANDING_FINE also implies the android.permission.SCENE_UNDERSTANDING_COARSE permission, if the application uses both capabilities, the application does not need to request both permissions separately.

Both android.permission.SCENE_UNDERSTANDING_COARSE and android.permission.SCENE_UNDERSTANDING_FINE are considered dangerous permissions.

(protection level: dangerous)

## Runtime Support

If the runtime supports discovery of spatial entities via raycasting, it **must** indicate this by enumerating `XR_SPATIAL_COMPONENT_TYPE_RAYCAST_RESULT_ANDROID` in [xrEnumerateSpatialCapabilityComponentTypesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrEnumerateSpatialCapabilityComponentTypesEXT) for the capabilities that support discovery by raycast.

If the runtime supports raycasting against the depth buffer, it **must** enumerate `XR_SPATIAL_CAPABILITY_DEPTH_RAYCAST_ANDROID` in [xrEnumerateSpatialCapabilitiesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrEnumerateSpatialCapabilitiesEXT) .

## Discover spatial entities by raycasting

The [XrSpatialRaycastInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#XrSpatialRaycastInfoANDROID) structure is defined as:

    typedef struct XrSpatialRaycastInfoANDROID {
        XrStructureType    type;
        const void*        next;
        XrSpace            space;
        XrTime             time;
        XrVector3f         origin;
        XrVector3f         direction;
        float              maxDistance;
    } XrSpatialRaycastInfoANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `space` is the [XrSpace](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpace) in which the pose of [XrSpatialRaycastResultDataANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#XrSpatialRaycastResultDataANDROID) will be located.
- `time` is an `XrTime` at which the pose of [XrSpatialRaycastResultDataANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#XrSpatialRaycastResultDataANDROID) defined.
- `origin` is an [XrVector3f](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrVector3f) which describes the origin of the ray.
- `direction` is an [XrVector3f](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrVector3f) which describes the direction of the ray.
- `maxDistance` is the distance in meters that application **can** optionally specify to limit the discovery of entities that are within the specified distance from the `origin` , along `direction` .

An application **can** include [XrSpatialRaycastInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#XrSpatialRaycastInfoANDROID) in the [XrSpatialDiscoverySnapshotCreateInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialDiscoverySnapshotCreateInfoEXT) :: `next` chain to discover spatial entities that intersect with the ray defined in this struct.

If an application uses [XrSpatialRaycastInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#XrSpatialRaycastInfoANDROID) with an [XrSpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextEXT) that was configured without enabling `XR_SPATIAL_COMPONENT_TYPE_RAYCAST_RESULT_ANDROID` for any capability, the runtime **must** return `XR_ERROR_SPATIAL_COMPONENT_NOT_ENABLED_EXT` from [xrCreateSpatialDiscoverySnapshotAsyncEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateSpatialDiscoverySnapshotAsyncEXT) or [xrCreateSpatialRaycastSnapshotANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#xrCreateSpatialRaycastSnapshotANDROID) .

The runtime **must** include the component data and ids of only those spatial entities in [XrSpatialSnapshotEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialSnapshotEXT) that come from capabilities that support the `XR_SPATIAL_COMPONENT_TYPE_RAYCAST_RESULT_ANDROID` component.

If an application sets `maxDistance` to a positive value, the runtime **must** not include any hit spatial entities in the snapshot that are more than `maxDistance` away from the panme:origin along `direction` . If `maxDistance` is set to 0 or a negative value, the runtime **must** consider the ray unbounded.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#VUID-XrSpatialRaycastInfoANDROID-extension-notenabled) The `XR_ANDROID_spatial_discovery_raycast` extension **must** be enabled prior to using [XrSpatialRaycastInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#XrSpatialRaycastInfoANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#VUID-XrSpatialRaycastInfoANDROID-type-type) `type` **must** be `XR_TYPE_SPATIAL_RAYCAST_INFO_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#VUID-XrSpatialRaycastInfoANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#VUID-XrSpatialRaycastInfoANDROID-space-parameter) `space` **must** be a valid [XrSpace](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpace) handle

## Raycast Result Component

The [XrSpatialRaycastResultDataANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#XrSpatialRaycastResultDataANDROID) structure is defined as:

    typedef struct XrSpatialRaycastResultDataANDROID {
        XrPosef    hitPose;
        float      distanceSquared;
    } XrSpatialRaycastResultDataANDROID;

### Member Descriptions

- `hitPose` is an [XrPosef](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrPosef) defining the point where the ray intersects with the spatial entity.
- `distanceSquared` is the squared of the distance from origin of the ray to the intersection point.

The `XR_SPATIAL_COMPONENT_TYPE_RAYCAST_RESULT_ANDROID` component will only be present in an [XrSpatialSnapshotEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialSnapshotEXT) created from [xrCreateSpatialDiscoverySnapshotAsyncEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateSpatialDiscoverySnapshotAsyncEXT) where [XrSpatialRaycastInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#XrSpatialRaycastInfoANDROID) is included in the [XrSpatialDiscoverySnapshotCreateInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialDiscoverySnapshotCreateInfoEXT) :: `next` chain or in an [XrSpatialSnapshotEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialSnapshotEXT) created from [xrCreateSpatialRaycastSnapshotANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#xrCreateSpatialRaycastSnapshotANDROID) .

The runtime **must** not include this component in any [XrSpatialSnapshotEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialSnapshotEXT) that is created using [xrCreateSpatialUpdateSnapshotEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateSpatialUpdateSnapshotEXT) .

The runtime **must** return `XR_ERROR_VALIDATION_FAILURE` from [xrCreateSpatialUpdateSnapshotEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateSpatialUpdateSnapshotEXT) if the application includes `XR_SPATIAL_COMPONENT_TYPE_RAYCAST_RESULT_ANDROID` in [XrSpatialUpdateSnapshotCreateInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialUpdateSnapshotCreateInfoEXT) :: `componentTypes` .

If `XR_SPATIAL_COMPONENT_TYPE_RAYCAST_RESULT_ANDROID` is enabled only for certain capabilities, the runtime **must** include only spatial entities provided by those capabilities in the snapshot. For example, if an object and a plane lines up in the same direction and `XR_SPATIAL_COMPONENT_TYPE_RAYCAST_RESULT_ANDROID` is enabled only for `XR_SPATIAL_CAPABILITY_PLANE_TRACKING_EXT` , only the plane will be discovered.

The `hitPose` of the `XR_SPATIAL_COMPONENT_TYPE_RAYCAST_RESULT_ANDROID` will be located in [XrCreateSpatialDiscoverySnapshotCompletionInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrCreateSpatialDiscoverySnapshotCompletionInfoEXT) :: `baseSpace` at [XrCreateSpatialDiscoverySnapshotCompletionInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrCreateSpatialDiscoverySnapshotCompletionInfoEXT) :: `time` . The positive Z axis is the normal of the hit surface, and the negative Y axis roughly points toward the ray origin.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#VUID-XrSpatialRaycastResultDataANDROID-extension-notenabled) The `XR_ANDROID_spatial_discovery_raycast` extension **must** be enabled prior to using [XrSpatialRaycastResultDataANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#XrSpatialRaycastResultDataANDROID)

### Component list struct to query data

The [XrSpatialComponentRaycastResultListANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#XrSpatialComponentRaycastResultListANDROID) structure is defined as:

    typedef struct XrSpatialComponentRaycastResultListANDROID {
        XrStructureType                       type;
        void*                                 next;
        uint32_t                              raycastResultCount;
        XrSpatialRaycastResultDataANDROID*    raycastResults;
    } XrSpatialComponentRaycastResultListANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `raycastResultCount` is a `uint32_t` describing the count of elements in the `raycastResults` array.
- `raycastResults` is an array of [XrSpatialRaycastResultDataANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#XrSpatialRaycastResultDataANDROID) .

To query the raycast result component of the spatial entities in an [XrSpatialSnapshotEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialSnapshotEXT) , include `XR_TYPE_SPATIAL_COMPONENT_RAYCAST_RESULT_LIST_ANDROID` in [XrSpatialComponentDataQueryConditionEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryConditionEXT) :: `componentTypes` and add [XrSpatialComponentRaycastResultListANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#XrSpatialComponentRaycastResultListANDROID) to the [XrSpatialComponentDataQueryResultEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryResultEXT) :: `next` chain.

The runtime **must** return `XR_ERROR_VALIDATION_FAILURE` from [xrQuerySpatialComponentDataEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrQuerySpatialComponentDataEXT) if [XrSpatialComponentRaycastResultListANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#XrSpatialComponentRaycastResultListANDROID) is in the [XrSpatialComponentDataQueryResultEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryResultEXT) :: `next` chain but `XR_SPATIAL_COMPONENT_TYPE_RAYCAST_RESULT_ANDROID` is not included in [XrSpatialComponentDataQueryConditionEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryConditionEXT) :: `componentTypes` .

The runtime **must** return `XR_ERROR_SIZE_INSUFFICIENT` from [xrQuerySpatialComponentDataEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrQuerySpatialComponentDataEXT) if `raycastResultCount` is less than [XrSpatialComponentDataQueryResultEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryResultEXT) :: `entityIdCountOutput` .

The returned `raycastResults` are unordered. An application **can** use [XrSpatialRaycastResultDataANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#XrSpatialRaycastResultDataANDROID) :: `distanceSquared` to sort the results by distance.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#VUID-XrSpatialComponentRaycastResultListANDROID-extension-notenabled) The `XR_ANDROID_spatial_discovery_raycast` extension **must** be enabled prior to using [XrSpatialComponentRaycastResultListANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#XrSpatialComponentRaycastResultListANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#VUID-XrSpatialComponentRaycastResultListANDROID-type-type) `type` **must** be `XR_TYPE_SPATIAL_COMPONENT_RAYCAST_RESULT_LIST_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#VUID-XrSpatialComponentRaycastResultListANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#VUID-XrSpatialComponentRaycastResultListANDROID-raycastResults-parameter) `raycastResults` **must** be a pointer to an array of `raycastResultCount` [XrSpatialRaycastResultDataANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#XrSpatialRaycastResultDataANDROID) structures
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#VUID-XrSpatialComponentRaycastResultListANDROID-raycastResultCount-arraylength) The `raycastResultCount` parameter **must** be greater than `0`

### Configuration

If `XR_SPATIAL_COMPONENT_TYPE_RAYCAST_RESULT_ANDROID` is enumerated in [XrSpatialCapabilityComponentTypesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityComponentTypesEXT) :: `componentTypes` for some capability, the application **can** enable it by including the enum value in the [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityConfigurationBaseHeaderEXT) :: `enabledComponents` list. This component does not require any special configuration to be included in the next chain of [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityConfigurationBaseHeaderEXT) .

The runtime **must** return `XR_ERROR_VALIDATION_FAILURE` from [xrCreateSpatialUpdateSnapshotEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateSpatialUpdateSnapshotEXT) if the application includes `XR_SPATIAL_COMPONENT_TYPE_RAYCAST_RESULT_ANDROID` in [XrSpatialUpdateSnapshotCreateInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialUpdateSnapshotCreateInfoEXT) :: `componentTypes` . This component is specific to discovery snapshots.

## Depth Raycast Spatial Capability

### Configuration

The [XrSpatialCapabilityConfigurationDepthRaycastANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#XrSpatialCapabilityConfigurationDepthRaycastANDROID) structure is defined as:

    typedef struct XrSpatialCapabilityConfigurationDepthRaycastANDROID {
        XrStructureType                     type;
        const void*                         next;
        XrSpatialCapabilityEXT              capability;
        uint32_t                            enabledComponentCount;
        const XrSpatialComponentTypeEXT*    enabledComponents;
    } XrSpatialCapabilityConfigurationDepthRaycastANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `capability` is an [XrSpatialCapabilityEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityEXT) and **must** be `XR_SPATIAL_CAPABILITY_DEPTH_RAYCAST_ANDROID` .
- `enabledComponentCount` is a `uint32_t` describing the count of elements in the `enabledComponents` array. It **must** be greater than 0.
- `enabledComponents` is a pointer to an array of [XrSpatialComponentTypeEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentTypeEXT) .

Anpplications **can** enable the `XR_SPATIAL_CAPABILITY_DEPTH_RAYCAST_ANDROID` spatial capability by including a pointer to an [XrSpatialCapabilityConfigurationDepthRaycastANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#XrSpatialCapabilityConfigurationDepthRaycastANDROID) structure in [XrSpatialContextCreateInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextCreateInfoEXT) :: `capabilityConfigs` .

The runtime **must** return `XR_ERROR_VALIDATION_FAILURE` if `capability` is not `XR_SPATIAL_CAPABILITY_DEPTH_RAYCAST_ANDROID` .

The ID of entities discovered via this capability is always [XR_NULL_SPATIAL_ENTITY_ID_EXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_NULL_SPATIAL_ENTITY_ID_EXT) . This also means that application **can** not create an [XrSpatialEntityEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialEntityEXT) handle for these entities, and thus they **can** not be included in [XrSpatialUpdateSnapshotCreateInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialUpdateSnapshotCreateInfoEXT) :: `entities` to create a update snapshot

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#VUID-XrSpatialCapabilityConfigurationDepthRaycastANDROID-extension-notenabled) The `XR_ANDROID_spatial_discovery_raycast` extension **must** be enabled prior to using [XrSpatialCapabilityConfigurationDepthRaycastANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#XrSpatialCapabilityConfigurationDepthRaycastANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#VUID-XrSpatialCapabilityConfigurationDepthRaycastANDROID-type-type) `type` **must** be `XR_TYPE_SPATIAL_CAPABILITY_CONFIGURATION_DEPTH_RAYCAST_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#VUID-XrSpatialCapabilityConfigurationDepthRaycastANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#VUID-XrSpatialCapabilityConfigurationDepthRaycastANDROID-capability-parameter) `capability` **must** be a valid [XrSpatialCapabilityEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityEXT) value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#VUID-XrSpatialCapabilityConfigurationDepthRaycastANDROID-enabledComponents-parameter) `enabledComponents` **must** be a pointer to an array of `enabledComponentCount` valid [XrSpatialComponentTypeEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentTypeEXT) values
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#VUID-XrSpatialCapabilityConfigurationDepthRaycastANDROID-enabledComponentCount-arraylength) The `enabledComponentCount` parameter **must** be greater than `0`

### Guaranteed Components

A runtime that supports `XR_SPATIAL_CAPABILITY_DEPTH_RAYCAST_ANDROID` , **must** support the following spatial components as guaranteed components of the entities discovered by this capability and **must** enumerate them in [xrEnumerateSpatialCapabilityComponentTypesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrEnumerateSpatialCapabilityComponentTypesEXT) -

- `XR_SPATIAL_COMPONENT_TYPE_RAYCAST_RESULT_ANDROID`

## Synchronous Raycast

The [xrCreateSpatialRaycastSnapshotANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#xrCreateSpatialRaycastSnapshotANDROID) function is defined as:

    XrResult xrCreateSpatialRaycastSnapshotANDROID(
        XrSpatialContextEXT                         spatialContext,
        const XrSpatialRaycastSnapshotCreateInfoANDROID* createInfo,
        XrSpatialSnapshotEXT*                       snapshot);

### Parameter Descriptions

- `spatialContext` is an [XrSpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextEXT) previously created by using [xrCreateSpatialContextAsyncEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateSpatialContextAsyncEXT) .
- `createInfo` is a pointer to an [XrSpatialRaycastSnapshotCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#XrSpatialRaycastSnapshotCreateInfoANDROID) .
- `snapshot` is a pointer to an [XrSpatialSnapshotEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialSnapshotEXT) .

While [xrCreateSpatialDiscoverySnapshotAsyncEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateSpatialDiscoverySnapshotAsyncEXT) is sufficient for most use cases, it is considered slow for applications that require instant raycast results. [xrCreateSpatialRaycastSnapshotANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#xrCreateSpatialRaycastSnapshotANDROID) starts a synchronous raycasting to create a snapshot, which allows applications to start querying raycast results immediately.

The runtime **must** return `XR_ERROR_SPATIAL_COMPONENT_NOT_ENABLED_EXT` if any of the [XrSpatialComponentTypeEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentTypeEXT) in [XrSpatialRaycastSnapshotCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#XrSpatialRaycastSnapshotCreateInfoANDROID) :: `componentTypes` are not enabled for the spatial capabilities passed to [XrSpatialContextCreateInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextCreateInfoEXT) :: `capabilityConfigs` when creating `spatialContext` .

If the application does not provide a list of spatial component types in [XrSpatialRaycastSnapshotCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#XrSpatialRaycastSnapshotCreateInfoANDROID) :: `componentTypes` , the runtime **must** include all the spatial entities in the snapshot that have the set of components which are enumerated in [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityConfigurationBaseHeaderEXT) ::enabledComponents for raycast supported capabilities configured for `spatialContext` . The runtime **must** include the data for all the enabled components of the raycast supported capabilities configured for `spatialContext` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#VUID-xrCreateSpatialRaycastSnapshotANDROID-extension-notenabled) The `XR_ANDROID_spatial_discovery_raycast` extension **must** be enabled prior to calling [xrCreateSpatialRaycastSnapshotANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#xrCreateSpatialRaycastSnapshotANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#VUID-xrCreateSpatialRaycastSnapshotANDROID-spatialContext-parameter) `spatialContext` **must** be a valid [XrSpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextEXT) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#VUID-xrCreateSpatialRaycastSnapshotANDROID-createInfo-parameter) `createInfo` **must** be a pointer to a valid [XrSpatialRaycastSnapshotCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#XrSpatialRaycastSnapshotCreateInfoANDROID) structure
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#VUID-xrCreateSpatialRaycastSnapshotANDROID-snapshot-parameter) `snapshot` **must** be a pointer to an [XrSpatialSnapshotEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialSnapshotEXT) handle

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
- `XR_ERROR_SPATIAL_COMPONENT_NOT_ENABLED_EXT`
- `XR_ERROR_TIME_INVALID`
- `XR_ERROR_VALIDATION_FAILURE`

The [XrSpatialRaycastSnapshotCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#XrSpatialRaycastSnapshotCreateInfoANDROID) structure is defined as:

    typedef struct XrSpatialRaycastSnapshotCreateInfoANDROID {
        XrStructureType                       type;
        const void*                           next;
        uint32_t                              componentTypeCount;
        const XrSpatialComponentTypeEXT*      componentTypes;
        const XrSpatialRaycastInfoANDROID*    raycastInfo;
    } XrSpatialRaycastSnapshotCreateInfoANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.
- `componentTypeCount` is a `uint32_t` describing the count of elements in the `componentTypes` array.
- `componentTypes` is an array of [XrSpatialComponentTypeEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentTypeEXT) .
- `raycastInfo` is the [XrSpatialRaycastInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#XrSpatialRaycastInfoANDROID) structure describing the information of a ray.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#VUID-XrSpatialRaycastSnapshotCreateInfoANDROID-extension-notenabled) The `XR_ANDROID_spatial_discovery_raycast` extension **must** be enabled prior to using [XrSpatialRaycastSnapshotCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#XrSpatialRaycastSnapshotCreateInfoANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#VUID-XrSpatialRaycastSnapshotCreateInfoANDROID-type-type) `type` **must** be `XR_TYPE_SPATIAL_RAYCAST_SNAPSHOT_CREATE_INFO_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#VUID-XrSpatialRaycastSnapshotCreateInfoANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#VUID-XrSpatialRaycastSnapshotCreateInfoANDROID-componentTypes-parameter) If `componentTypeCount` is not `0` , `componentTypes` **must** be a pointer to an array of `componentTypeCount` valid [XrSpatialComponentTypeEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentTypeEXT) values
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#VUID-XrSpatialRaycastSnapshotCreateInfoANDROID-raycastInfo-parameter) `raycastInfo` **must** be a pointer to a valid [XrSpatialRaycastInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#XrSpatialRaycastInfoANDROID) structure

## Example code

### Configure Depth Raycast and Plane Tracking Capability

The following example code demonstrates how to create a spatial context with capabilities that support raycast functionality. For this example, `XR_SPATIAL_CAPABILITY_DEPTH_RAYCAST_ANDROID` and `XR_SPATIAL_CAPABILITY_PLANE_TRACKING_EXT` are used.

    // Check runtime supported capabilities
    uint32_t capabilityCount;
    CHK_XR(xrEnumerateSpatialCapabilitiesEXT(instance, systemId, 0, &capabilityCount, nullptr));
    std::vector<XrSpatialCapabilityEXT> capabilities(capabilityCount);
    CHK_XR(xrEnumerateSpatialCapabilitiesEXT(instance, systemId, capabilityCount, &capabilityCount, capabilities.data()));

    if (std::find(capabilities.begin(), capabilities.end(), XR_SPATIAL_CAPABILITY_DEPTH_RAYCAST_ANDROID) == capabilities.end()) {
      return;
    }

    if (std::find(capabilities.begin(), capabilities.end(), XR_SPATIAL_CAPABILITY_PLANE_TRACKING_EXT) == capabilities.end()) {
      return;
    }

    // Create capability config for depth raycasting
    std::vector<XrSpatialComponentTypeEXT> depthRaycastComponents {
      XR_SPATIAL_COMPONENT_TYPE_RAYCAST_RESULT_ANDROID
    };

    // Create capability config for depth raycasting
    XrSpatialCapabilityConfigurationDepthRaycastANDROID depthRaycastConfig {
      .type = XR_TYPE_SPATIAL_CAPABILITY_CONFIGURATION_DEPTH_RAYCAST_ANDROID,
      .next = nullptr,
      .capability = XR_SPATIAL_CAPABILITY_DEPTH_RAYCAST_ANDROID,
      .enabledComponentCount = (uint32_t)depthRaycastComponents.size(),
      .enabledComponents = depthRaycastComponents.data(),
    };

    // Enumerate runtime supported components for plane tracking capability
    XrSpatialCapabilityComponentTypesEXT capabilityComponentTypes {
      XR_TYPE_SPATIAL_CAPABILITY_COMPONENT_TYPES_EXT
    };

    bool isRaycastSupportedViaPlaneTracking;
    std::vector<XrSpatialComponentTypeEXT> planeTrackingComponents {
      XR_SPATIAL_COMPONENT_TYPE_BOUNDED_2D_EXT,
      XR_SPATIAL_COMPONENT_TYPE_PLANE_ALIGNMENT_EXT,
    };

    CHK_XR(xrEnumerateSpatialCapabilityComponentTypesEXT(instance, systemId,
           XR_SPATIAL_CAPABILITY_PLANE_TRACKING_EXT, &capabilityComponentTypes));

    planeTrackingComponents.resize(capabilityComponentTypes.componentTypeCountOutput);
    capabilityComponentTypes.componentTypeCapacityInput = (uint32_t)planeTrackingComponents.size();
    capabilityComponentTypes.componentTypes = planeTrackingComponents.data();

    CHK_XR(xrEnumerateSpatialCapabilityComponentTypesEXT(instance, systemId,
           XR_SPATIAL_CAPABILITY_PLANE_TRACKING_EXT, &capabilityComponentTypes));

    // Check if raycast is supported by plane tracking
    isRaycastSupportedViaPlaneTracking = std::find(planeTrackingComponents.begin(),
    planeTrackingComponents.end(), XR_SPATIAL_COMPONENT_TYPE_RAYCAST_RESULT_ANDROID)
    != planeTrackingComponents.end();

    // Create capability config for plane tracking
    XrSpatialCapabilityConfigurationPlaneTrackingEXT planeTrackingConfig {
      .type = XR_TYPE_SPATIAL_CAPABILITY_CONFIGURATION_PLANE_TRACKING_EXT,
      .next = nullptr,
      .capability = XR_SPATIAL_CAPABILITY_PLANE_TRACKING_EXT,
      .enabledComponentCount = (uint32_t)planeTrackingComponents.size(),
      .enabledComponents = planeTrackingComponents.data(),
    };

    // Create spatial context
    // Types of raycast is determined by configs included in XrSpatialContextCreateInfoEXT
    // For this example, both plane raycast & depth raycast are performed
    std::vector<const XrSpatialCapabilityConfigurationBaseHeaderEXT*> capabilityConfigs;
    capabilityConfigs.push_back(reinterpret_cast<const XrSpatialCapabilityConfigurationBaseHeaderEXT*>(&depthRaycastConfig));
    if(isRaycastSupportedViaPlaneTracking) capabilityConfigs.push_back(reinterpret_cast<const XrSpatialCapabilityConfigurationBaseHeaderEXT*>(&planeTrackingConfig));

    XrSpatialContextCreateInfoEXT contextCreateInfo {
      .type = XR_TYPE_SPATIAL_CONTEXT_CREATE_INFO_EXT,
      .next = nullptr,
      .capabilityConfigCount = (uint32_t)capabilityConfigs.size(),
      .capabilityConfigs = capabilityConfigs.data(),
    };

    CHK_XR(xrCreateSpatialContextAsyncEXT(session, &contextCreateInfo, &future))

    // Completes creating spatial context
    XrCreateSpatialContextCompletionEXT contextCompletion{
    XR_TYPE_CREATE_SPATIAL_CONTEXT_COMPLETION_EXT};

    CHK_XR(xrCreateSpatialContextCompleteEXT(session, future, &contextCompletion))

### Discover Spatial Entities \& Query Component Data

The following example code demonstrates how to discover spatial entities for a context configured with `XR_SPATIAL_CAPABILITY_DEPTH_RAYCAST_ANDROID` \& `XR_SPATIAL_CAPABILITY_PLANE_TRACKING_EXT` and query its component data.

    // Fill in the raycast info.
    XrSpatialRaycastInfoANDROID raycastInfo {
      .type        = XR_TYPE_SPATIAL_RAYCAST_INFO_ANDROID,
      .next        = nullptr,
      .space       = viewSpace,
      .time        = updateTime,
      .origin      = {0.0f, 0.0f, 0.0f},
      .direction   = {0.0f, 0.0f,-1.0f},
      .maxDistance = 0.0f  // ray is unbounded
    };

    // Next pointing to the raycast info.
    XrSpatialDiscoverySnapshotCreateInfoEXT discoverySnapshotCreateInfo {
      .type = XR_TYPE_SPATIAL_DISCOVERY_SNAPSHOT_CREATE_INFO_EXT,
      .next = &raycastInfo
    };

    // Create snapshot
    CHK_XR(xrCreateSpatialDiscoverySnapshotAsyncEXT (
    spatialContext, &discoverySnapshotCreateInfo, &future));

    waitUntilReady(future);

    // Complete async operation.
    XrCreateSpatialDiscoverySnapshotCompletionInfoEXT
      createSnapshotCompletionInfo {
        .type      = XR_TYPE_CREATE_SPATIAL_DISCOVERY_SNAPSHOT_COMPLETION_INFO_EXT,
        .baseSpace = viewSpace,
        .time      = updateTime,
        .future    = future,
      };

    XrCreateSpatialDiscoverySnapshotCompletionEXT completion {
      XR_TYPE_CREATE_SPATIAL_DISCOVERY_SNAPSHOT_COMPLETION_EXT};

    CHK_XR(xrCreateSpatialDiscoverySnapshotCompleteEXT(
               spatialContext, &createSnapshotCompletionInfo,
               &completion));

    if(completion.futureResult != XR_SUCCESS) return;

    // Query hit result components
    std::array<XrSpatialComponentTypeEXT, 1> enabledComponents = {
      XR_SPATIAL_COMPONENT_TYPE_RAYCAST_RESULT_ANDROID
    };

    XrSpatialComponentDataQueryConditionEXT queryCond {
      .type = XR_TYPE_SPATIAL_COMPONENT_DATA_QUERY_CONDITION_EXT,
      .componentTypeCount = 1,
      .componentTypes     = enabledComponents.data(),
    };

    XrSpatialComponentDataQueryResultEXT queryResult {
      .type = XR_TYPE_SPATIAL_COMPONENT_DATA_QUERY_RESULT_EXT,
    };

    XrResult result = xrQuerySpatialComponentDataEXT(
               completion.snapshot, &queryCond, &queryResult);

    // Check query result.
    if(result != XR_SUCCESS) return;

    // Query again for the hit result list.
    std::vector<XrSpatialRaycastResultDataANDROID> raycastResults;
    raycastResults.resize(queryResult.entityIdCountOutput);
    XrSpatialComponentRaycastResultListANDROID raycastResultList {
      .type               = XR_TYPE_SPATIAL_COMPONENT_RAYCAST_RESULT_LIST_ANDROID,
      .raycastResultCount = (uint32_t)raycastResults.size(),
      .raycastResults     = raycastResults.data(),
    };

    queryResult.next = &raycastResultList;
    result = xrQuerySpatialComponentDataEXT(completion.snapshot, &queryCond, &queryResult);

    // Check query result again.
    if(result != XR_SUCCESS) return;

    std::vector<XrSpatialEntityEXT> hitEntities;
    std::vector<XrPosef> depthHitPoses;
    for(uint32_t i = 0; i < queryResult.entityIdCountOutput; ++i) {
        // access raycastResults[i] for id & pose
        XrSpatialEntityIdEXT   id   = queryResult.entityIds[i];
        XrPosef                pose = raycastResults[i].hitPose;

        if (id != XR_NULL_SPATIAL_ENTITY_ID_EXT) {
            // hit entities (e.g. planes)
        // get entity handle via entity id
        XrSpatialEntityFromIdCreateInfoEXT entityCreateInfo {
          .type = XR_TYPE_SPATIAL_ENTITY_FROM_ID_CREATE_INFO_EXT,
          .entityId = id,
        };

        XrSpatialEntityEXT entity = XR_NULL_HANDLE;
        xrCreateSpatialEntityFromIdEXT(spatialContext, &entityCreateInfo, &entity);

        hitEntities.push_back(entity);
      } else {
        // hit depth
        depthHitPoses.push_back(pose);
      }
    }

    // Cleanup
    xrDestroySpatialSnapshotEXT(completion.snapshot);

### Create Raycast Snapshot

The following example code demonstrates how to create synchronous raycast snapshot.

    // fill in create info
    XrSpatialRaycastSnapshotCreateInfoANDROID createInfo {
      .type = XR_TYPE_SPATIAL_RAYCAST_SNAPSHOT_CREATE_INFO_ANDROID,
      .componentTypeCount = 0,   // include all hit spatial entities
      .componentTypes = nullptr,
      .raycastInfo = &raycastInfo
    };

    // create raycast snapshot
    XrSpatialSnapshotEXT raycastSnapshot = XR_NULL_HANDLE;
    CHK_XR(xrCreateSpatialRaycastSnapshotANDROID(
      spatialContext, &createInfo, &raycastSnapshot));

    // ...
    // query component data as previous example
    // ...

    // Cleanup
    xrDestroySpatialSnapshotEXT(raycastSnapshot);

## New Commands

- [xrCreateSpatialRaycastSnapshotANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#xrCreateSpatialRaycastSnapshotANDROID)

## New Structures

- [XrSpatialCapabilityConfigurationDepthRaycastANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#XrSpatialCapabilityConfigurationDepthRaycastANDROID)
- [XrSpatialRaycastResultDataANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#XrSpatialRaycastResultDataANDROID)
- [XrSpatialRaycastSnapshotCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#XrSpatialRaycastSnapshotCreateInfoANDROID)
- Extending [XrSpatialComponentDataQueryResultEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryResultEXT) :

  - [XrSpatialComponentRaycastResultListANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#XrSpatialComponentRaycastResultListANDROID)
- Extending [XrSpatialDiscoverySnapshotCreateInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialDiscoverySnapshotCreateInfoEXT) :

  - [XrSpatialRaycastInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast#XrSpatialRaycastInfoANDROID)

## New Enum Constants

- `XR_ANDROID_SPATIAL_DISCOVERY_RAYCAST_EXTENSION_NAME`
- `XR_ANDROID_spatial_discovery_raycast_SPEC_VERSION`
- Extending [XrSpatialCapabilityEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityEXT) :

  - `XR_SPATIAL_CAPABILITY_DEPTH_RAYCAST_ANDROID`
- Extending [XrSpatialComponentTypeEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentTypeEXT) :

  - `XR_SPATIAL_COMPONENT_TYPE_RAYCAST_RESULT_ANDROID`
- Extending [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) :

  - `XR_TYPE_SPATIAL_CAPABILITY_CONFIGURATION_DEPTH_RAYCAST_ANDROID`
  - `XR_TYPE_SPATIAL_COMPONENT_RAYCAST_RESULT_LIST_ANDROID`
  - `XR_TYPE_SPATIAL_RAYCAST_INFO_ANDROID`
  - `XR_TYPE_SPATIAL_RAYCAST_SNAPSHOT_CREATE_INFO_ANDROID`

## Issues

## Version History

- Revision 1, 2025-07-15 (Brian Chen)

  - Initial extension description.