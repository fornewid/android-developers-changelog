---
title: https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor
url: https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor
source: md.txt
---

### XR_ANDROID_geospatial_anchor

**Name String**

`XR_ANDROID_geospatial_anchor`

**Extension Type**

Instance extension

**Registered Extension Number**

798

**Revision**

1

**Ratification Status**

Not ratified

**Extension and Version Dependencies**

`XR_ANDROID_geospatial`  

and  

`XR_EXT_future`  

and  

`XR_EXT_spatial_entity`  

and  

`XR_EXT_spatial_anchor`

**Last Modified Date**

2025-10-30

**IP Status**

No known IP claims.

**Contributors**

John Ullman, Google  

Ben King, Google  

Nihav Jain, Google  

Jared Finder, Google

## Overview

This extension provides Geospatial Anchors and Surface Anchors that build on the base Geospatial extension. Geospatial Anchors are anchors that are positioned in space relative to the Earth at a given latitude, longitude and altitude. Surface Anchors are Earth-relative anchors which are placed at a given latitude, longitude, and altitude relative to a surface as known by the Visual Positioning Service. As the runtime's accuracy of its position relative to the Earth improves, the Anchor's pose will adjust accordingly.

## System Capability for Geospatial Anchors

The [XrSystemGeospatialAnchorPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#XrSystemGeospatialAnchorPropertiesANDROID) structure is defined as:

    typedef struct XrSystemGeospatialAnchorPropertiesANDROID {
        XrStructureType    type;
        void*              next;
        uint32_t           maxSurfaceAnchorCount;
    } XrSystemGeospatialAnchorPropertiesANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.
- `maxSurfaceAnchorCount` is a `uint32_t` indicating the maximum number of surface anchors that **can** be created.

An application **can** inspect geospatial anchor capabilities of the system by chaining an [XrSystemGeospatialAnchorPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#XrSystemGeospatialAnchorPropertiesANDROID) structure to the [XrSystemProperties](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSystemProperties) when calling [xrGetSystemProperties](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrGetSystemProperties) .

If [XrSystemGeospatialPropertiesANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSystemGeospatialPropertiesANDROID) :: `supportsGeospatial` is `XR_TRUE` , then `maxSurfaceAnchorCount` indicates the maximum number of surface anchors the runtime supports. The limit **must** be greater than 0 in this case.

If [XrSystemGeospatialPropertiesANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSystemGeospatialPropertiesANDROID) :: `supportsGeospatial` is not `XR_TRUE` , then `maxSurfaceAnchorCount` **must** be 0.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#VUID-XrSystemGeospatialAnchorPropertiesANDROID-extension-notenabled) The `XR_ANDROID_geospatial_anchor` extension **must** be enabled prior to using [XrSystemGeospatialAnchorPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#XrSystemGeospatialAnchorPropertiesANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#VUID-XrSystemGeospatialAnchorPropertiesANDROID-type-type) `type` **must** be `XR_TYPE_SYSTEM_GEOSPATIAL_ANCHOR_PROPERTIES_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#VUID-XrSystemGeospatialAnchorPropertiesANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)

## Plane Tracking for Anchors

The [XrGeospatialTrackerAnchorTrackingInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#XrGeospatialTrackerAnchorTrackingInfoANDROID) structure is defined as:

    typedef struct XrGeospatialTrackerAnchorTrackingInfoANDROID {
        XrStructureType    type;
        const void*        next;
        XrBool32           shouldTrackPlanes;
    } XrGeospatialTrackerAnchorTrackingInfoANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `shouldTrackPlanes` is an `XrBool32` indicating if the geospatial tracker will track planes to improve positioning of surface-locked anchors.

Plane tracking **can** be enabled to improve positioning of surface-locked anchors.

If the application wants to enable plane tracking to improve surface anchor poses, it **can** chain an [XrGeospatialTrackerAnchorTrackingInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#XrGeospatialTrackerAnchorTrackingInfoANDROID) structure to [XrGeospatialTrackerCreateInfoANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrGeospatialTrackerCreateInfoANDROID) when calling [xrCreateGeospatialTrackerANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateGeospatialTrackerANDROID) .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#VUID-XrGeospatialTrackerAnchorTrackingInfoANDROID-extension-notenabled) The `XR_ANDROID_geospatial_anchor` extension **must** be enabled prior to using [XrGeospatialTrackerAnchorTrackingInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#XrGeospatialTrackerAnchorTrackingInfoANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#VUID-XrGeospatialTrackerAnchorTrackingInfoANDROID-type-type) `type` **must** be `XR_TYPE_GEOSPATIAL_TRACKER_ANCHOR_TRACKING_INFO_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#VUID-XrGeospatialTrackerAnchorTrackingInfoANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)

## Geospatial Anchors

The [xrCreateGeospatialAnchorANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#xrCreateGeospatialAnchorANDROID) function is defined as:

    XrResult xrCreateGeospatialAnchorANDROID(
        XrSpatialContextEXT                         spatialContext,
        const XrGeospatialAnchorCreateInfoANDROID*  createInfo,
        XrSpatialEntityIdEXT*                       anchorEntityId);

### Parameter Descriptions

- `spatialContext` is the [XrSpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextEXT) to create the anchor in. The context **must** be configured for `XR_SPATIAL_CAPABILITY_ANCHOR_EXT` otherwise the runtime **must** return `XR_ERROR_VALIDATION_FAILURE` .
- `createInfo` is a pointer to [XrGeospatialAnchorCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#XrGeospatialAnchorCreateInfoANDROID) containing anchor creation parameters.
- `anchorEntityId` is a pointer to `XrSpatialEntityIdEXT` in which the anchor entity ID is returned.

If the [XrGeospatialTrackerANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrGeospatialTrackerANDROID) specified in [XrGeospatialAnchorCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#XrGeospatialAnchorCreateInfoANDROID) :: `geospatialTracker` is not in the `XR_GEOSPATIAL_TRACKER_STATE_RUNNING_ANDROID` state, the runtime **must** return `XR_ERROR_GEOSPATIAL_TRACKER_NOT_RUNNING_ANDROID` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#VUID-xrCreateGeospatialAnchorANDROID-extension-notenabled) The `XR_ANDROID_geospatial_anchor` extension **must** be enabled prior to calling [xrCreateGeospatialAnchorANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#xrCreateGeospatialAnchorANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#VUID-xrCreateGeospatialAnchorANDROID-spatialContext-parameter) `spatialContext` **must** be a valid [XrSpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextEXT) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#VUID-xrCreateGeospatialAnchorANDROID-createInfo-parameter) `createInfo` **must** be a pointer to a valid [XrGeospatialAnchorCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#XrGeospatialAnchorCreateInfoANDROID) structure
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#VUID-xrCreateGeospatialAnchorANDROID-anchorEntityId-parameter) `anchorEntityId` **must** be a pointer to an `XrSpatialEntityIdEXT` value

### Return Codes

[Success](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`
- `XR_SESSION_LOSS_PENDING`

[Failure](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_GEOSPATIAL_COORDINATES_INVALID_ANDROID`
- `XR_ERROR_GEOSPATIAL_TRACKER_NOT_RUNNING_ANDROID`
- `XR_ERROR_HANDLE_INVALID`
- `XR_ERROR_INSTANCE_LOST`
- `XR_ERROR_LIMIT_REACHED`
- `XR_ERROR_OUT_OF_MEMORY`
- `XR_ERROR_RUNTIME_FAILURE`
- `XR_ERROR_SESSION_LOST`
- `XR_ERROR_VALIDATION_FAILURE`

The [XrGeospatialAnchorCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#XrGeospatialAnchorCreateInfoANDROID) structure is defined as:

    typedef struct XrGeospatialAnchorCreateInfoANDROID {
        XrStructureType               type;
        const void*                   next;
        XrGeospatialTrackerANDROID    geospatialTracker;
        XrGeospatialPoseANDROID       geospatialPose;
    } XrGeospatialAnchorCreateInfoANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `geospatialTracker` is the [XrGeospatialTrackerANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrGeospatialTrackerANDROID) to use for creating the anchor.
- `geospatialPose` is a pointer to [XrGeospatialPoseANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrGeospatialPoseANDROID) defining the anchor's location and orientation.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#VUID-XrGeospatialAnchorCreateInfoANDROID-extension-notenabled) The `XR_ANDROID_geospatial_anchor` extension **must** be enabled prior to using [XrGeospatialAnchorCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#XrGeospatialAnchorCreateInfoANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#VUID-XrGeospatialAnchorCreateInfoANDROID-type-type) `type` **must** be `XR_TYPE_GEOSPATIAL_ANCHOR_CREATE_INFO_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#VUID-XrGeospatialAnchorCreateInfoANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#VUID-XrGeospatialAnchorCreateInfoANDROID-geospatialTracker-parameter) `geospatialTracker` **must** be a valid [XrGeospatialTrackerANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrGeospatialTrackerANDROID) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#VUID-XrGeospatialAnchorCreateInfoANDROID-geospatialPose-parameter) `geospatialPose` **must** be a valid [XrGeospatialPoseANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrGeospatialPoseANDROID) structure

## Surface Anchors

Surface anchors are anchors placed relative to a surface, such as terrain or rooftops.

The [XrSurfaceAnchorTypeANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#XrSurfaceAnchorTypeANDROID) enumeration is defined as:

    typedef enum XrSurfaceAnchorTypeANDROID {
        XR_SURFACE_ANCHOR_TYPE_TERRAIN_ANDROID = 1,
        XR_SURFACE_ANCHOR_TYPE_ROOFTOP_ANDROID = 2,
        XR_SURFACE_ANCHOR_TYPE_MAX_ENUM_ANDROID = 0x7FFFFFFF
    } XrSurfaceAnchorTypeANDROID;

The [XrSurfaceAnchorTypeANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#XrSurfaceAnchorTypeANDROID) enumeration specifies the type of surface an anchor is relative to.

The enumerants have the following values:

Enum Description

`XR_SURFACE_ANCHOR_TYPE_TERRAIN_ANDROID`

Type of an anchor placed relative to the ground.

`XR_SURFACE_ANCHOR_TYPE_ROOFTOP_ANDROID`

Type of an anchor placed relative to the rooftop, or ground where there is no building.

The [xrCreateSurfaceAnchorAsyncANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#xrCreateSurfaceAnchorAsyncANDROID) function is defined as:

    XrResult xrCreateSurfaceAnchorAsyncANDROID(
        XrSpatialContextEXT                         spatialContext,
        const XrSurfaceAnchorCreateInfoANDROID*     createInfo,
        XrFutureEXT*                                future);

### Parameter Descriptions

- `spatialContext` is the [XrSpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextEXT) to create the anchor in.
- `createInfo` is a pointer to [XrSurfaceAnchorCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#XrSurfaceAnchorCreateInfoANDROID) containing anchor creation parameters.
- `future` is a pointer to `XrFutureEXT` that will hold the result of the asynchronous operation.

The [xrCreateSurfaceAnchorAsyncANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#xrCreateSurfaceAnchorAsyncANDROID) function begins an asynchronous operation to create a surface anchor. Unlike standard geospatial anchors, the runtime **may** fetch terrain data to determine the correct altitude. The runtime **must** return `XR_ERROR_LIMIT_REACHED` if the application attempts to create more than [XrSystemGeospatialAnchorPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#XrSystemGeospatialAnchorPropertiesANDROID) :: `maxSurfaceAnchorCount` surface anchors at a time. If the [XrGeospatialTrackerANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrGeospatialTrackerANDROID) specified in [XrSurfaceAnchorCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#XrSurfaceAnchorCreateInfoANDROID) :: `geospatialTracker` is not in the `XR_GEOSPATIAL_TRACKER_STATE_RUNNING_ANDROID` state, the runtime **must** return `XR_ERROR_GEOSPATIAL_TRACKER_NOT_RUNNING_ANDROID` . The operation **may** fail asynchronously with result `XR_ERROR_SURFACE_ANCHOR_LOCATION_UNSUPPORTED_ANDROID` if there is no surface data for the given location. The runtime **must** return `XR_ERROR_VALIDATION_FAILURE` if `XR_SPATIAL_CAPABILITY_ANCHOR_EXT` was not configured for `spatialContext` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#VUID-xrCreateSurfaceAnchorAsyncANDROID-extension-notenabled) The `XR_ANDROID_geospatial_anchor` extension **must** be enabled prior to calling [xrCreateSurfaceAnchorAsyncANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#xrCreateSurfaceAnchorAsyncANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#VUID-xrCreateSurfaceAnchorAsyncANDROID-spatialContext-parameter) `spatialContext` **must** be a valid [XrSpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextEXT) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#VUID-xrCreateSurfaceAnchorAsyncANDROID-createInfo-parameter) `createInfo` **must** be a pointer to a valid [XrSurfaceAnchorCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#XrSurfaceAnchorCreateInfoANDROID) structure
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#VUID-xrCreateSurfaceAnchorAsyncANDROID-future-parameter) `future` **must** be a pointer to an `XrFutureEXT` value

### Return Codes

[Success](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`
- `XR_SESSION_LOSS_PENDING`

[Failure](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_GEOSPATIAL_COORDINATES_INVALID_ANDROID`
- `XR_ERROR_GEOSPATIAL_TRACKER_NOT_RUNNING_ANDROID`
- `XR_ERROR_HANDLE_INVALID`
- `XR_ERROR_INSTANCE_LOST`
- `XR_ERROR_LIMIT_REACHED`
- `XR_ERROR_OUT_OF_MEMORY`
- `XR_ERROR_RUNTIME_FAILURE`
- `XR_ERROR_SESSION_LOST`
- `XR_ERROR_VALIDATION_FAILURE`

The [XrSurfaceAnchorCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#XrSurfaceAnchorCreateInfoANDROID) structure is defined as:

    typedef struct XrSurfaceAnchorCreateInfoANDROID {
        XrStructureType               type;
        const void*                   next;
        XrGeospatialTrackerANDROID    geospatialTracker;
        XrSurfaceAnchorTypeANDROID    surfaceAnchorType;
        XrQuaternionf                 eastUpSouthOrientation;
        double                        latitude;
        double                        longitude;
        double                        altitudeRelativeToSurface;
    } XrSurfaceAnchorCreateInfoANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `geospatialTracker` is the [XrGeospatialTrackerANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrGeospatialTrackerANDROID) to use.
- `surfaceAnchorType` is the [XrSurfaceAnchorTypeANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#XrSurfaceAnchorTypeANDROID) for the anchor.
- `eastUpSouthOrientation` is the orientation with respect to a coordinate system where +X=East, +Y=Up and +Z=South.
- `latitude` is the latitude in degrees, between -89.9 and +89.9.
- `longitude` is the longitude in degrees, between -180 and +180.
- `altitudeRelativeToSurface` is the altitude in meters relative to the surface specified by `surfaceAnchorType` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#VUID-XrSurfaceAnchorCreateInfoANDROID-extension-notenabled) The `XR_ANDROID_geospatial_anchor` extension **must** be enabled prior to using [XrSurfaceAnchorCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#XrSurfaceAnchorCreateInfoANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#VUID-XrSurfaceAnchorCreateInfoANDROID-type-type) `type` **must** be `XR_TYPE_SURFACE_ANCHOR_CREATE_INFO_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#VUID-XrSurfaceAnchorCreateInfoANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#VUID-XrSurfaceAnchorCreateInfoANDROID-geospatialTracker-parameter) `geospatialTracker` **must** be a valid [XrGeospatialTrackerANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrGeospatialTrackerANDROID) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#VUID-XrSurfaceAnchorCreateInfoANDROID-surfaceAnchorType-parameter) `surfaceAnchorType` **must** be a valid [XrSurfaceAnchorTypeANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#XrSurfaceAnchorTypeANDROID) value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#VUID-XrSurfaceAnchorCreateInfoANDROID-latitude-parameter) `latitude` **must** be a valid `double` value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#VUID-XrSurfaceAnchorCreateInfoANDROID-longitude-parameter) `longitude` **must** be a valid `double` value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#VUID-XrSurfaceAnchorCreateInfoANDROID-altitudeRelativeToSurface-parameter) `altitudeRelativeToSurface` **must** be a valid `double` value

The [xrCreateSurfaceAnchorCompleteANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#xrCreateSurfaceAnchorCompleteANDROID) function is defined as:

    XrResult xrCreateSurfaceAnchorCompleteANDROID(
        XrSpatialContextEXT                         spatialContext,
        XrFutureEXT                                 future,
        XrSurfaceAnchorCreateCompletionANDROID*     completion);

### Parameter Descriptions

- `spatialContext` is the [XrSpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextEXT) used for creation.
- `future` is the `XrFutureEXT` returned by [xrCreateSurfaceAnchorAsyncANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#xrCreateSurfaceAnchorAsyncANDROID) .
- `completion` is a pointer to [XrSurfaceAnchorCreateCompletionANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#XrSurfaceAnchorCreateCompletionANDROID) that receives the result.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#VUID-xrCreateSurfaceAnchorCompleteANDROID-extension-notenabled) The `XR_ANDROID_geospatial_anchor` extension **must** be enabled prior to calling [xrCreateSurfaceAnchorCompleteANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#xrCreateSurfaceAnchorCompleteANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#VUID-xrCreateSurfaceAnchorCompleteANDROID-spatialContext-parameter) `spatialContext` **must** be a valid [XrSpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextEXT) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#VUID-xrCreateSurfaceAnchorCompleteANDROID-completion-parameter) `completion` **must** be a pointer to an [XrSurfaceAnchorCreateCompletionANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#XrSurfaceAnchorCreateCompletionANDROID) structure

### Return Codes

[Success](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`
- `XR_SESSION_LOSS_PENDING`

[Failure](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_FUTURE_INVALID_EXT`
- `XR_ERROR_FUTURE_PENDING_EXT`
- `XR_ERROR_HANDLE_INVALID`
- `XR_ERROR_INSTANCE_LOST`
- `XR_ERROR_LIMIT_REACHED`
- `XR_ERROR_OUT_OF_MEMORY`
- `XR_ERROR_RUNTIME_FAILURE`
- `XR_ERROR_SESSION_LOST`
- `XR_ERROR_VALIDATION_FAILURE`

The [XrSurfaceAnchorCreateCompletionANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#XrSurfaceAnchorCreateCompletionANDROID) structure holds the result of an asynchronous surface anchor creation.

    typedef struct XrSurfaceAnchorCreateCompletionANDROID {
        XrStructureType         type;
        void*                   next;
        XrResult                futureResult;
        XrSpatialEntityIdEXT    anchorEntityId;
    } XrSurfaceAnchorCreateCompletionANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `futureResult` is the [XrResult](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrResult) of the creation operation. If `futureResult` is `XR_ERROR_GEOSPATIAL_CLOUD_AUTH_FAILED_ANDROID` , a structure in the `next` chain **may** provide more information about the failure.
- `anchorEntityId` is the `XrSpatialEntityIdEXT` of the created anchor, or [XR_NULL_SPATIAL_ENTITY_ID_EXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_NULL_SPATIAL_ENTITY_ID_EXT) if `futureResult` is not `XR_SUCCESS` .

### Future Return Codes

`futureResult` values:

[Success](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`
- `XR_SESSION_LOSS_PENDING`

[Failure](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_RUNTIME_FAILURE`
- `XR_ERROR_INSTANCE_LOST`
- `XR_ERROR_SESSION_LOST`
- `XR_ERROR_OUT_OF_MEMORY`
- `XR_ERROR_LIMIT_REACHED`
- `XR_ERROR_GEOSPATIAL_TRACKER_NOT_RUNNING_ANDROID`
- `XR_ERROR_SURFACE_ANCHOR_LOCATION_UNSUPPORTED_ANDROID`
- `XR_ERROR_GEOSPATIAL_CLOUD_AUTH_FAILED_ANDROID`

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#VUID-XrSurfaceAnchorCreateCompletionANDROID-extension-notenabled) The `XR_ANDROID_geospatial_anchor` extension **must** be enabled prior to using [XrSurfaceAnchorCreateCompletionANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#XrSurfaceAnchorCreateCompletionANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#VUID-XrSurfaceAnchorCreateCompletionANDROID-type-type) `type` **must** be `XR_TYPE_SURFACE_ANCHOR_CREATE_COMPLETION_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#VUID-XrSurfaceAnchorCreateCompletionANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#VUID-XrSurfaceAnchorCreateCompletionANDROID-futureResult-parameter) `futureResult` **must** be a valid [XrResult](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrResult) value

## Example

### Create Terrain Anchor

    PFN_xrCreateSpatialContextAsyncEXT xrCreateSpatialContextAsyncEXT;
    PFN_xrCreateSpatialContextCompleteEXT xrCreateSpatialContextCompleteEXT;
    PFN_xrCreateSurfaceAnchorAsyncANDROID xrCreateSurfaceAnchorAsyncANDROID;
    PFN_xrPollFutureEXT xrPollFutureEXT;
    PFN_xrCreateSurfaceAnchorCompleteANDROID xrCreateSurfaceAnchorCompleteANDROID;
    XrInstance instance;
    XrSession session;
    XrGeospatialTrackerANDROID geospatialTracker;

    // Create a spatial context
    XrSpatialContextEXT spatialContext{};
    {
      std::vector<XrSpatialComponentTypeEXT> enabledComponents = {
        XR_SPATIAL_COMPONENT_TYPE_ANCHOR_EXT,
      };

      XrSpatialCapabilityConfigurationAnchorEXT
           anchorConfig{XR_TYPE_SPATIAL_CAPABILITY_CONFIGURATION_ANCHOR_EXT};
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

      // ... wait until future is ready ...

      XrCreateSpatialContextCompletionEXT contextCompletion{XR_TYPE_CREATE_SPATIAL_CONTEXT_COMPLETION_EXT};
      CHK_XR(xrCreateSpatialContextCompleteEXT(session, createContextFuture, &contextCompletion));
      if (contextCompletion.futureResult != XR_SUCCESS) {
        return;
      }

      spatialContext = contextCompletion.spatialContext;
    }

    XrSurfaceAnchorCreateInfoANDROID anchorCreateInfo{
        XR_TYPE_SURFACE_ANCHOR_CREATE_INFO_ANDROID};
    anchorCreateInfo.surfaceAnchorType = XR_SURFACE_ANCHOR_TYPE_TERRAIN_ANDROID;
    anchorCreateInfo.eastUpSouthOrientation = {0, 0, 0, 1};
    anchorCreateInfo.latitude = 37.7749;
    anchorCreateInfo.longitude = -122.4194;
    anchorCreateInfo.altitudeRelativeToSurface = 0;
    anchorCreateInfo.geospatialTracker = geospatialTracker;
    XrFutureEXT anchorFuture = XR_NULL_FUTURE_EXT;
    CHK_XR(xrCreateSurfaceAnchorAsyncANDROID(spatialContext, &anchorCreateInfo, &anchorFuture));

    XrFuturePollInfoEXT anchorPollInfo{XR_TYPE_FUTURE_POLL_INFO_EXT};
    XrFuturePollResultEXT anchorPollResult{XR_TYPE_FUTURE_POLL_RESULT_EXT};
    anchorPollInfo.future = anchorFuture;
    anchorPollResult.state = XR_FUTURE_STATE_PENDING_EXT;
    while (anchorPollResult.state == XR_FUTURE_STATE_PENDING_EXT) {
      // Do in render loop/state loop.
      CHK_XR(xrPollFutureEXT(instance, &anchorPollInfo, &anchorPollResult));
    }

    XrSurfaceAnchorCreateCompletionANDROID anchorCompletion{
        XR_TYPE_SURFACE_ANCHOR_CREATE_COMPLETION_ANDROID};
    CHK_XR(xrCreateSurfaceAnchorCompleteANDROID(spatialContext, anchorFuture, &anchorCompletion));
    if (anchorCompletion.futureResult == XR_SUCCESS) {
      // Use completion.anchorEntityId.
      XrSpatialEntityIdEXT anchorId = anchorCompletion.anchorEntityId;

      // Query in UpdateSnapshot.
    }

## New Commands

- [xrCreateGeospatialAnchorANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#xrCreateGeospatialAnchorANDROID)
- [xrCreateSurfaceAnchorAsyncANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#xrCreateSurfaceAnchorAsyncANDROID)
- [xrCreateSurfaceAnchorCompleteANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#xrCreateSurfaceAnchorCompleteANDROID)

## New Structures

- [XrGeospatialAnchorCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#XrGeospatialAnchorCreateInfoANDROID)
- [XrSurfaceAnchorCreateCompletionANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#XrSurfaceAnchorCreateCompletionANDROID)
- [XrSurfaceAnchorCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#XrSurfaceAnchorCreateInfoANDROID)
- Extending [XrGeospatialTrackerCreateInfoANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrGeospatialTrackerCreateInfoANDROID) :

  - [XrGeospatialTrackerAnchorTrackingInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#XrGeospatialTrackerAnchorTrackingInfoANDROID)
- Extending [XrSystemProperties](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSystemProperties) :

  - [XrSystemGeospatialAnchorPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#XrSystemGeospatialAnchorPropertiesANDROID)

## New Enums

- [XrSurfaceAnchorTypeANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor#XrSurfaceAnchorTypeANDROID)

## New Enum Constants

- `XR_ANDROID_GEOSPATIAL_ANCHOR_EXTENSION_NAME`
- `XR_ANDROID_geospatial_anchor_SPEC_VERSION`
- Extending [XrResult](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrResult) :

  - `XR_ERROR_SURFACE_ANCHOR_LOCATION_UNSUPPORTED_ANDROID`
- Extending [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) :

  - `XR_TYPE_GEOSPATIAL_ANCHOR_CREATE_INFO_ANDROID`
  - `XR_TYPE_GEOSPATIAL_TRACKER_ANCHOR_TRACKING_INFO_ANDROID`
  - `XR_TYPE_SURFACE_ANCHOR_CREATE_COMPLETION_ANDROID`
  - `XR_TYPE_SURFACE_ANCHOR_CREATE_INFO_ANDROID`
  - `XR_TYPE_SYSTEM_GEOSPATIAL_ANCHOR_PROPERTIES_ANDROID`

**Issues**

**Version History**

- Revision 1, 2025-10-30 (Ben King)

  - Initial draft.