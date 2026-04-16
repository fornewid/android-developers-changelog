---
title: https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial
url: https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial
source: md.txt
---

### XR_ANDROID_geospatial

**Name String**

`XR_ANDROID_geospatial`

**Extension Type**

Instance extension

**Registered Extension Number**

790

**Revision**

1

**Ratification Status**

Not ratified

**Extension and Version Dependencies**

`XR_EXT_future`

**Last Modified Date**

2025-12-18

**IP Status**

No known IP claims.

**Contributors**

John Ullman, Google  

Ben King, Google  

Nihav Jain, Google  

Jared Finder, Google

## Overview

This extension provides the Geospatial tracking for Google's Geospatial API, which provides precise geo-location and orientation, and allows the application to place content with respect to the Earth. It does this using a combination of motion tracking, GPS and other sensors, and Google's Visual Positioning System (VPS). VPS compares images from a device's camera to Street View imagery in order to determine a precise location and orientation. The Geospatial API often provides sub-meter positional accuracy (orders of magnitude better than GPS) and sub-degree orientation accuracy.

To successfully use the APIs in this extension (other than checking for extension support), the application **must** have successfully set authentication credentials via some mechanism, such as `XR_ANDROID_google_cloud_auth` . See the auth extension's documentation for more details about setup and error results.

### Permissions

Android applications **must** have the android.permission.ACCESS_FINE_LOCATION permission listed in their manifest to use this extension. The android.permission.ACCESS_FINE_LOCATION permission is considered a dangerous permission. The application **must** request the permission at runtime to use these functions:

- [xrCreateGeospatialTrackerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#xrCreateGeospatialTrackerANDROID)

(protection level: dangerous)

## Inspect system capability

The [XrSystemGeospatialPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrSystemGeospatialPropertiesANDROID) structure is defined as:

    typedef struct XrSystemGeospatialPropertiesANDROID {
        XrStructureType    type;
        void*              next;
        XrBool32           supportsGeospatial;
    } XrSystemGeospatialPropertiesANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.
- `supportsGeospatial` is an `XrBool32` , indicating if the current system supports geospatial features.

An application **can** inspect whether the system supports geospatial features by chaining an [XrSystemGeospatialPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrSystemGeospatialPropertiesANDROID) structure to the [XrSystemProperties](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSystemProperties) when calling [xrGetSystemProperties](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrGetSystemProperties) .

If a runtime returns `XR_FALSE` for `supportsGeospatial` , the system does not support geospatial features, and therefore **must** return `XR_ERROR_FEATURE_UNSUPPORTED` from [xrCreateGeospatialTrackerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#xrCreateGeospatialTrackerANDROID) . The application **should** avoid using geospatial functionality when `supportsGeospatial` is `XR_FALSE` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#VUID-XrSystemGeospatialPropertiesANDROID-extension-notenabled) The `XR_ANDROID_geospatial` extension **must** be enabled prior to using [XrSystemGeospatialPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrSystemGeospatialPropertiesANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#VUID-XrSystemGeospatialPropertiesANDROID-type-type) `type` **must** be `XR_TYPE_SYSTEM_GEOSPATIAL_PROPERTIES_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#VUID-XrSystemGeospatialPropertiesANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)

## Create a Geospatial Tracker handle

    XR_DEFINE_HANDLE(XrGeospatialTrackerANDROID)

The [xrCreateGeospatialTrackerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#xrCreateGeospatialTrackerANDROID) function is defined as:

    XrResult xrCreateGeospatialTrackerANDROID(
        XrSession                                   session,
        const XrGeospatialTrackerCreateInfoANDROID* createInfo,
        XrGeospatialTrackerANDROID*                 geospatialTrackerOutput);

### Parameter Descriptions

- `session` is an [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) in which the geospatial tracker will be active.
- `createInfo` is a pointer to an [XrGeospatialTrackerCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialTrackerCreateInfoANDROID) structure specifying initial geospatial tracker parameters.
- `geospatialTrackerOutput` is a pointer to a handle in which the created [XrGeospatialTrackerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialTrackerANDROID) is returned.

An application **can** create an [XrGeospatialTrackerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialTrackerANDROID) handle by calling [xrCreateGeospatialTrackerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#xrCreateGeospatialTrackerANDROID) . The returned [XrGeospatialTrackerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialTrackerANDROID) handle **can** be subsequently used in API calls. If the application has not obtained the required permissions, the runtime **must** return `XR_ERROR_PERMISSION_INSUFFICIENT` . Only one [XrGeospatialTrackerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialTrackerANDROID) **can** exist at a time for a particular [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) . The application **must** ensure that any previous [XrGeospatialTrackerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialTrackerANDROID) objects have been destroyed before calling this function again, otherwise the runtime **must** return `XR_ERROR_LIMIT_REACHED` . If the tracker is successfully created, it will initially enter the state `XR_GEOSPATIAL_TRACKER_STATE_STOPPED_ANDROID` , and the application **must** wait until the state changes to `XR_GEOSPATIAL_TRACKER_STATE_RUNNING_ANDROID` before using the tracker. See [XrEventDataGeospatialTrackerStateChangedANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrEventDataGeospatialTrackerStateChangedANDROID) . If the application passes an [XrGeospatialTrackerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialTrackerANDROID) which is not in the state `XR_GEOSPATIAL_TRACKER_STATE_RUNNING_ANDROID` to a function which requires it, the runtime **must** return `XR_ERROR_GEOSPATIAL_TRACKER_NOT_RUNNING_ANDROID` .

The [XrGeospatialTrackerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialTrackerANDROID) handle **must** be eventually freed via the [xrDestroyGeospatialTrackerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#xrDestroyGeospatialTrackerANDROID) function.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#VUID-xrCreateGeospatialTrackerANDROID-extension-notenabled) The `XR_ANDROID_geospatial` extension **must** be enabled prior to calling [xrCreateGeospatialTrackerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#xrCreateGeospatialTrackerANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#VUID-xrCreateGeospatialTrackerANDROID-session-parameter) `session` **must** be a valid [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#VUID-xrCreateGeospatialTrackerANDROID-createInfo-parameter) `createInfo` **must** be a pointer to a valid [XrGeospatialTrackerCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialTrackerCreateInfoANDROID) structure
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#VUID-xrCreateGeospatialTrackerANDROID-geospatialTrackerOutput-parameter) `geospatialTrackerOutput` **must** be a pointer to an [XrGeospatialTrackerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialTrackerANDROID) handle

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
- `XR_ERROR_PERMISSION_INSUFFICIENT`
- `XR_ERROR_RUNTIME_FAILURE`
- `XR_ERROR_SESSION_LOST`
- `XR_ERROR_VALIDATION_FAILURE`

The [XrGeospatialTrackerCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialTrackerCreateInfoANDROID) structure is defined as:

    typedef struct XrGeospatialTrackerCreateInfoANDROID {
        XrStructureType    type;
        const void*        next;
    } XrGeospatialTrackerCreateInfoANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#VUID-XrGeospatialTrackerCreateInfoANDROID-extension-notenabled) The `XR_ANDROID_geospatial` extension **must** be enabled prior to using [XrGeospatialTrackerCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialTrackerCreateInfoANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#VUID-XrGeospatialTrackerCreateInfoANDROID-type-type) `type` **must** be `XR_TYPE_GEOSPATIAL_TRACKER_CREATE_INFO_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#VUID-XrGeospatialTrackerCreateInfoANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains) . See also: [XrGeospatialTrackerAnchorTrackingInfoANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrGeospatialTrackerAnchorTrackingInfoANDROID)

The [xrDestroyGeospatialTrackerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#xrDestroyGeospatialTrackerANDROID) function is defined as:

    XrResult xrDestroyGeospatialTrackerANDROID(
        XrGeospatialTrackerANDROID                  geospatialTracker);

### Parameter Descriptions

- `geospatialTracker` is the [XrGeospatialTrackerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialTrackerANDROID) to be destroyed.

An application **can** use [xrDestroyGeospatialTrackerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#xrDestroyGeospatialTrackerANDROID) function to release the geospatial tracker and the underlying resources.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#VUID-xrDestroyGeospatialTrackerANDROID-extension-notenabled) The `XR_ANDROID_geospatial` extension **must** be enabled prior to calling [xrDestroyGeospatialTrackerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#xrDestroyGeospatialTrackerANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#VUID-xrDestroyGeospatialTrackerANDROID-geospatialTracker-parameter) `geospatialTracker` **must** be a valid [XrGeospatialTrackerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialTrackerANDROID) handle

### Thread Safety

- Access to `geospatialTracker` , and any child handles, **must** be externally synchronized

### Return Codes

[Success](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`

[Failure](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_CALL_ORDER_INVALID`
- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_HANDLE_INVALID`

## Geospatial Tracker State

The [XrGeospatialTrackerStateANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialTrackerStateANDROID) enumeration is defined as:

    typedef enum XrGeospatialTrackerStateANDROID {
        XR_GEOSPATIAL_TRACKER_STATE_STOPPED_ANDROID = 0,
        XR_GEOSPATIAL_TRACKER_STATE_RUNNING_ANDROID = 1,
        XR_GEOSPATIAL_TRACKER_STATE_INITIALIZATION_FAILED_ANDROID = 2,
        XR_GEOSPATIAL_TRACKER_STATE_MAX_ENUM_ANDROID = 0x7FFFFFFF
    } XrGeospatialTrackerStateANDROID;

The [XrGeospatialTrackerStateANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialTrackerStateANDROID) enumeration identifies the different states of a geospatial tracker.

The enumerants have the following values:

Enum Description

`XR_GEOSPATIAL_TRACKER_STATE_STOPPED_ANDROID`

The Geospatial Tracker is not running.

`XR_GEOSPATIAL_TRACKER_STATE_RUNNING_ANDROID`

The Geospatial tracker is running and usable.

`XR_GEOSPATIAL_TRACKER_STATE_INITIALIZATION_FAILED_ANDROID`

The Geospatial Tracker failed to initialize, and will never be usable.

The [XrEventDataGeospatialTrackerStateChangedANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrEventDataGeospatialTrackerStateChangedANDROID) structure is defined as:

    typedef struct XrEventDataGeospatialTrackerStateChangedANDROID {
        XrStructureType                    type;
        const void*                        next;
        XrGeospatialTrackerANDROID         geospatialTracker;
        XrGeospatialTrackerStateANDROID    state;
        XrResult                           initializationResult;
        XrTime                             time;
    } XrEventDataGeospatialTrackerStateChangedANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `geospatialTracker` is the [XrGeospatialTrackerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialTrackerANDROID) whose state has changed.
- `state` is the new [XrGeospatialTrackerStateANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialTrackerStateANDROID) .
- `initializationResult` is the error result if `state` is `XR_GEOSPATIAL_TRACKER_STATE_INITIALIZATION_FAILED_ANDROID` , otherwise `XR_SUCCESS` .
- `time` is the `XrTime` at which the state change occurred.

The [XrEventDataGeospatialTrackerStateChangedANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrEventDataGeospatialTrackerStateChangedANDROID) structure is sent when the geospatial tracker state changes. If the application has a valid [XrGeospatialTrackerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialTrackerANDROID) , it **should** poll for this event. The first event received for a tracker will have `state` `XR_GEOSPATIAL_TRACKER_STATE_STOPPED_ANDROID` . After a runtime-determined amount of time, the state **must** change to either `XR_GEOSPATIAL_TRACKER_STATE_RUNNING_ANDROID` or `XR_GEOSPATIAL_TRACKER_STATE_INITIALIZATION_FAILED_ANDROID` . This transition will take an arbitrary amount of time. If `state` changes to `XR_GEOSPATIAL_TRACKER_STATE_INITIALIZATION_FAILED_ANDROID` , it **must** be the last event received for this tracker, and the `initializationResult` field will hold the error code. It **may** take several seconds for an error to occur. The application **should** destroy the tracker in this case. If `state` changes to `XR_GEOSPATIAL_TRACKER_STATE_STOPPED_ANDROID` , all previously created geospatial anchors **must** permanently stop tracking and **should** be destroyed by the application. The state **may** change back and forth between `XR_GEOSPATIAL_TRACKER_STATE_RUNNING_ANDROID` and `XR_GEOSPATIAL_TRACKER_STATE_STOPPED_ANDROID` arbitrarily many times.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#VUID-XrEventDataGeospatialTrackerStateChangedANDROID-extension-notenabled) The `XR_ANDROID_geospatial` extension **must** be enabled prior to using [XrEventDataGeospatialTrackerStateChangedANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrEventDataGeospatialTrackerStateChangedANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#VUID-XrEventDataGeospatialTrackerStateChangedANDROID-type-type) `type` **must** be `XR_TYPE_EVENT_DATA_GEOSPATIAL_TRACKER_STATE_CHANGED_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#VUID-XrEventDataGeospatialTrackerStateChangedANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)

## Geospatial Pose

The [XrGeospatialPoseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialPoseANDROID) structure is defined as:

    typedef struct XrGeospatialPoseANDROID {
        XrQuaternionf    eastUpSouthOrientation;
        double           latitude;
        double           longitude;
        double           altitude;
    } XrGeospatialPoseANDROID;

### Member Descriptions

- `eastUpSouthOrientation` is an [XrQuaternionf](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrQuaternionf) defining the orientation with respect to a coordinate system where +X=East, +Y=Up and +Z=South.
- `latitude` is the latitude in degrees, between -90 and +90.
- `longitude` is the longitude in degrees, between -180 and +180.
- `altitude` is the altitude in meters above the WGS84 ellipsoid.

The [XrGeospatialPoseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialPoseANDROID) structure represents a position and orientation relative to the Earth using the WGS84 ellipsoid.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#VUID-XrGeospatialPoseANDROID-extension-notenabled) The `XR_ANDROID_geospatial` extension **must** be enabled prior to using [XrGeospatialPoseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialPoseANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#VUID-XrGeospatialPoseANDROID-latitude-parameter) `latitude` **must** be a valid `double` value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#VUID-XrGeospatialPoseANDROID-longitude-parameter) `longitude` **must** be a valid `double` value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#VUID-XrGeospatialPoseANDROID-altitude-parameter) `altitude` **must** be a valid `double` value

The [XrGeospatialPoseFlagBitsANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialPoseFlagBitsANDROID) enumeration is defined as:

    // Flag bits for XrGeospatialPoseFlagsANDROID
    static const XrGeospatialPoseFlagsANDROID XR_GEOSPATIAL_POSE_ORIENTATION_VALID_BIT_ANDROID = 0x00000001;
    static const XrGeospatialPoseFlagsANDROID XR_GEOSPATIAL_POSE_POSITION_VALID_BIT_ANDROID = 0x00000002;

The [XrGeospatialPoseFlagBitsANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialPoseFlagBitsANDROID) enumeration specifies flags for geospatial poses.

The flag bits have the following meanings:

### Flag Descriptions

- `XR_GEOSPATIAL_POSE_ORIENTATION_VALID_BIT_ANDROID` --- Indicates that the orientation member contains valid data
- `XR_GEOSPATIAL_POSE_POSITION_VALID_BIT_ANDROID` --- Indicates that the position member contains valid data

The [XrGeospatialPoseFlagsANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialPoseFlagsANDROID) type is a bitmask of [XrGeospatialPoseFlagBitsANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialPoseFlagBitsANDROID) .

    typedef XrFlags64 XrGeospatialPoseFlagsANDROID;

## Converting XrPosef to Geospatial Pose

The [xrLocateGeospatialPoseFromPoseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#xrLocateGeospatialPoseFromPoseANDROID) function is defined as:

    XrResult xrLocateGeospatialPoseFromPoseANDROID(
        XrGeospatialTrackerANDROID                  geospatialTracker,
        const XrGeospatialPoseFromPoseLocateInfoANDROID* locateInfo,
        XrGeospatialPoseResultANDROID*              geospatialPoseResult);

### Parameter Descriptions

- `geospatialTracker` is the [XrGeospatialTrackerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialTrackerANDROID) to use for conversion.
- `locateInfo` is a pointer to [XrGeospatialPoseFromPoseLocateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialPoseFromPoseLocateInfoANDROID) containing query parameters.
- `geospatialPoseResult` is a pointer to [XrGeospatialPoseResultANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialPoseResultANDROID) that receives the result.

The [xrLocateGeospatialPoseFromPoseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#xrLocateGeospatialPoseFromPoseANDROID) function converts a pose in [XrGeospatialPoseFromPoseLocateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialPoseFromPoseLocateInfoANDROID) :: `space` to a geospatial pose. If the state of `geospatialTracker` is not `XR_GEOSPATIAL_TRACKER_STATE_RUNNING_ANDROID` , the runtime **must** return `XR_ERROR_GEOSPATIAL_TRACKER_NOT_RUNNING_ANDROID` . If the function returns `XR_SUCCESS` , the [XrGeospatialPoseResultANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialPoseResultANDROID) :: `poseFlags` field of `geospatialPoseResult` determines which output fields are valid. If `XR_GEOSPATIAL_POSE_POSITION_VALID_BIT_ANDROID` is not set in [XrGeospatialPoseResultANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialPoseResultANDROID) :: `poseFlags` , the application **must** not read the fields [XrGeospatialPoseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialPoseANDROID) :: `latitude` , [XrGeospatialPoseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialPoseANDROID) :: `longitude` , [XrGeospatialPoseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialPoseANDROID) :: `altitude` , [XrGeospatialPoseResultANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialPoseResultANDROID) :: `horizontalAccuracy` or [XrGeospatialPoseResultANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialPoseResultANDROID) :: `verticalAccuracy` in [XrGeospatialPoseResultANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialPoseResultANDROID) . If `XR_GEOSPATIAL_POSE_ORIENTATION_VALID_BIT_ANDROID` is not set in [XrGeospatialPoseResultANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialPoseResultANDROID) :: `poseFlags` , the application **must** not read [XrGeospatialPoseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialPoseANDROID) :: `eastUpSouthOrientation` or [XrGeospatialPoseResultANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialPoseResultANDROID) :: `orientationYawAccuracy` . If `XR_GEOSPATIAL_POSE_POSITION_VALID_BIT_ANDROID` is not set, `XR_GEOSPATIAL_POSE_ORIENTATION_VALID_BIT_ANDROID` **must** also not be set.

If the accuracy is lower than expected, this **may** be an indication that the device is not utilizing VPS localization. The application **can** instruct the user to point their device at signs and buildings to improve localization.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#VUID-xrLocateGeospatialPoseFromPoseANDROID-extension-notenabled) The `XR_ANDROID_geospatial` extension **must** be enabled prior to calling [xrLocateGeospatialPoseFromPoseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#xrLocateGeospatialPoseFromPoseANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#VUID-xrLocateGeospatialPoseFromPoseANDROID-geospatialTracker-parameter) `geospatialTracker` **must** be a valid [XrGeospatialTrackerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialTrackerANDROID) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#VUID-xrLocateGeospatialPoseFromPoseANDROID-locateInfo-parameter) `locateInfo` **must** be a pointer to a valid [XrGeospatialPoseFromPoseLocateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialPoseFromPoseLocateInfoANDROID) structure
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#VUID-xrLocateGeospatialPoseFromPoseANDROID-geospatialPoseResult-parameter) `geospatialPoseResult` **must** be a pointer to an [XrGeospatialPoseResultANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialPoseResultANDROID) structure

### Return Codes

[Success](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`
- `XR_SESSION_LOSS_PENDING`

[Failure](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_GEOSPATIAL_TRACKER_NOT_RUNNING_ANDROID`
- `XR_ERROR_HANDLE_INVALID`
- `XR_ERROR_INSTANCE_LOST`
- `XR_ERROR_POSE_INVALID`
- `XR_ERROR_RUNTIME_FAILURE`
- `XR_ERROR_SESSION_LOST`
- `XR_ERROR_TIME_INVALID`
- `XR_ERROR_VALIDATION_FAILURE`

The [XrGeospatialPoseFromPoseLocateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialPoseFromPoseLocateInfoANDROID) structure is defined as:

    typedef struct XrGeospatialPoseFromPoseLocateInfoANDROID {
        XrStructureType    type;
        const void*        next;
        XrSpace            space;
        XrTime             time;
        XrPosef            pose;
    } XrGeospatialPoseFromPoseLocateInfoANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `space` is the [XrSpace](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpace) in which `pose` is defined.
- `time` is the `XrTime` at which to evaluate `pose` .
- `pose` is the [XrPosef](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrPosef) in `space` to convert to a geospatial pose.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#VUID-XrGeospatialPoseFromPoseLocateInfoANDROID-extension-notenabled) The `XR_ANDROID_geospatial` extension **must** be enabled prior to using [XrGeospatialPoseFromPoseLocateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialPoseFromPoseLocateInfoANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#VUID-XrGeospatialPoseFromPoseLocateInfoANDROID-type-type) `type` **must** be `XR_TYPE_GEOSPATIAL_POSE_FROM_POSE_LOCATE_INFO_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#VUID-XrGeospatialPoseFromPoseLocateInfoANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#VUID-XrGeospatialPoseFromPoseLocateInfoANDROID-space-parameter) `space` **must** be a valid [XrSpace](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpace) handle

The [XrGeospatialPoseResultANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialPoseResultANDROID) structure is defined as:

    typedef struct XrGeospatialPoseResultANDROID {
        XrStructureType                 type;
        void*                           next;
        XrGeospatialPoseFlagsANDROID    poseFlags;
        XrGeospatialPoseANDROID         geospatialPose;
        double                          horizontalAccuracy;
        double                          verticalAccuracy;
        double                          orientationYawAccuracy;
    } XrGeospatialPoseResultANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `poseFlags` is a bitmask of [XrGeospatialPoseFlagsANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialPoseFlagsANDROID) indicating validity of pose components.
- `geospatialPose` is the resulting [XrGeospatialPoseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialPoseANDROID) .
- `horizontalAccuracy` is the estimated horizontal accuracy of the Geospatial pose position, defined as the radius in meters of the circle of 68% confidence level around the given latitude and longitude.
- `verticalAccuracy` is the estimated vertical accuracy of the Geospatial pose position, defined as the distance in meters of 68% confidence level around the given altitude. In other words, there is a 68% chance that the true altitude is in the range \[ [XrGeospatialPoseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialPoseANDROID) :: `altitude` - `verticalAccuracy` , [XrGeospatialPoseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialPoseANDROID) :: `altitude` \\+ `verticalAccuracy` \].
- `orientationYawAccuracy` is the estimated yaw accuracy of the Geospatial pose orientation, defined as the radius in degrees of 68% confidence level around the given orientation.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#VUID-XrGeospatialPoseResultANDROID-extension-notenabled) The `XR_ANDROID_geospatial` extension **must** be enabled prior to using [XrGeospatialPoseResultANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialPoseResultANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#VUID-XrGeospatialPoseResultANDROID-type-type) `type` **must** be `XR_TYPE_GEOSPATIAL_POSE_RESULT_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#VUID-XrGeospatialPoseResultANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)

## Converting a Geospatial Pose to an XrPosef

The [xrLocateGeospatialPoseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#xrLocateGeospatialPoseANDROID) function is defined as:

    XrResult xrLocateGeospatialPoseANDROID(
        XrGeospatialTrackerANDROID                  geospatialTracker,
        const XrGeospatialPoseLocateInfoANDROID*    locateInfo,
        XrSpaceLocation*                            location);

### Parameter Descriptions

- `geospatialTracker` is the [XrGeospatialTrackerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialTrackerANDROID) to use for conversion.
- `locateInfo` is a pointer to [XrGeospatialPoseLocateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialPoseLocateInfoANDROID) containing query parameters.
- `location` is a pointer to [XrSpaceLocation](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpaceLocation) that receives the resulting pose.

The [xrLocateGeospatialPoseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#xrLocateGeospatialPoseANDROID) function converts a geospatial pose to an [XrSpaceLocation](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpaceLocation) . If the [XrGeospatialTrackerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialTrackerANDROID) is not running, the runtime **must** return `XR_ERROR_GEOSPATIAL_TRACKER_NOT_RUNNING_ANDROID` . If the function returns `XR_SUCCESS` , the [XrSpaceLocation](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpaceLocation) :: `locationFlags` field of `location` determines which output fields are valid.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#VUID-xrLocateGeospatialPoseANDROID-extension-notenabled) The `XR_ANDROID_geospatial` extension **must** be enabled prior to calling [xrLocateGeospatialPoseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#xrLocateGeospatialPoseANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#VUID-xrLocateGeospatialPoseANDROID-geospatialTracker-parameter) `geospatialTracker` **must** be a valid [XrGeospatialTrackerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialTrackerANDROID) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#VUID-xrLocateGeospatialPoseANDROID-locateInfo-parameter) `locateInfo` **must** be a pointer to a valid [XrGeospatialPoseLocateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialPoseLocateInfoANDROID) structure
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#VUID-xrLocateGeospatialPoseANDROID-location-parameter) `location` **must** be a pointer to an [XrSpaceLocation](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpaceLocation) structure

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
- `XR_ERROR_RUNTIME_FAILURE`
- `XR_ERROR_SESSION_LOST`
- `XR_ERROR_TIME_INVALID`
- `XR_ERROR_VALIDATION_FAILURE`

The [XrGeospatialPoseLocateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialPoseLocateInfoANDROID) structure is defined as:

    typedef struct XrGeospatialPoseLocateInfoANDROID {
        XrStructureType            type;
        const void*                next;
        XrSpace                    space;
        XrTime                     time;
        XrGeospatialPoseANDROID    geospatialPose;
    } XrGeospatialPoseLocateInfoANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `space` is the [XrSpace](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpace) in which the resulting pose will be represented.
- `time` is the `XrTime` at which to locate the pose.
- `geospatialPose` is the [XrGeospatialPoseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialPoseANDROID) to convert.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#VUID-XrGeospatialPoseLocateInfoANDROID-extension-notenabled) The `XR_ANDROID_geospatial` extension **must** be enabled prior to using [XrGeospatialPoseLocateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialPoseLocateInfoANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#VUID-XrGeospatialPoseLocateInfoANDROID-type-type) `type` **must** be `XR_TYPE_GEOSPATIAL_POSE_LOCATE_INFO_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#VUID-XrGeospatialPoseLocateInfoANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#VUID-XrGeospatialPoseLocateInfoANDROID-space-parameter) `space` **must** be a valid [XrSpace](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpace) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#VUID-XrGeospatialPoseLocateInfoANDROID-geospatialPose-parameter) `geospatialPose` **must** be a valid [XrGeospatialPoseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialPoseANDROID) structure

## VPS Availability

The [XrVPSAvailabilityANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrVPSAvailabilityANDROID) enumeration is defined as:

    typedef enum XrVPSAvailabilityANDROID {
        XR_VPS_AVAILABILITY_UNAVAILABLE_ANDROID = 1,
        XR_VPS_AVAILABILITY_AVAILABLE_ANDROID = 2,
        XR_VPSAVAILABILITY_MAX_ENUM_ANDROID = 0x7FFFFFFF
    } XrVPSAvailabilityANDROID;

The [XrVPSAvailabilityANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrVPSAvailabilityANDROID) enumeration indicates VPS availability.

The enumerants have the following values:

Enum Description

`XR_VPS_AVAILABILITY_UNAVAILABLE_ANDROID`

VPS is not available near the given location.

`XR_VPS_AVAILABILITY_AVAILABLE_ANDROID`

VPS is available near the given location.

The [xrCheckVpsAvailabilityAsyncANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#xrCheckVpsAvailabilityAsyncANDROID) function is defined as:

    XrResult xrCheckVpsAvailabilityAsyncANDROID(
        XrSession                                   session,
        double                                      latitude,
        double                                      longitude,
        XrFutureEXT*                                future);

### Parameter Descriptions

- `session` is the [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) to use for the check.
- `latitude` is the latitude in degrees.
- `longitude` is the longitude in degrees.
- `future` is a pointer to `XrFutureEXT` that will hold the result of the asynchronous operation.

Visual Positioning Service (VPS) availability indicates whether VPS **can** be used to improve geospatial accuracy at a given location.

The [xrCheckVpsAvailabilityAsyncANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#xrCheckVpsAvailabilityAsyncANDROID) function begins an asynchronous check for VPS availability at a given location. The application does not need an [XrGeospatialTrackerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialTrackerANDROID) to call this function, and **can** use the result of this operation to decide whether to create one. If the application has not obtained the required permissions, the runtime **must** return `XR_ERROR_PERMISSION_INSUFFICIENT` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#VUID-xrCheckVpsAvailabilityAsyncANDROID-extension-notenabled) The `XR_ANDROID_geospatial` extension **must** be enabled prior to calling [xrCheckVpsAvailabilityAsyncANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#xrCheckVpsAvailabilityAsyncANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#VUID-xrCheckVpsAvailabilityAsyncANDROID-session-parameter) `session` **must** be a valid [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#VUID-xrCheckVpsAvailabilityAsyncANDROID-latitude-parameter) `latitude` **must** be a valid `double` value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#VUID-xrCheckVpsAvailabilityAsyncANDROID-longitude-parameter) `longitude` **must** be a valid `double` value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#VUID-xrCheckVpsAvailabilityAsyncANDROID-future-parameter) `future` **must** be a pointer to an `XrFutureEXT` value

### Return Codes

[Success](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`
- `XR_SESSION_LOSS_PENDING`

[Failure](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_GEOSPATIAL_COORDINATES_INVALID_ANDROID`
- `XR_ERROR_HANDLE_INVALID`
- `XR_ERROR_INSTANCE_LOST`
- `XR_ERROR_RUNTIME_FAILURE`
- `XR_ERROR_SESSION_LOST`
- `XR_ERROR_VALIDATION_FAILURE`

The [xrCheckVpsAvailabilityCompleteANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#xrCheckVpsAvailabilityCompleteANDROID) function is defined as:

    XrResult xrCheckVpsAvailabilityCompleteANDROID(
        XrSession                                   session,
        XrFutureEXT                                 future,
        XrVPSAvailabilityCheckCompletionANDROID*    completion);

### Parameter Descriptions

- `session` is the [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) used for the check.
- `future` is the `XrFutureEXT` returned by [xrCheckVpsAvailabilityAsyncANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#xrCheckVpsAvailabilityAsyncANDROID) .
- `completion` is a pointer to [XrVPSAvailabilityCheckCompletionANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrVPSAvailabilityCheckCompletionANDROID) that receives the result.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#VUID-xrCheckVpsAvailabilityCompleteANDROID-extension-notenabled) The `XR_ANDROID_geospatial` extension **must** be enabled prior to calling [xrCheckVpsAvailabilityCompleteANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#xrCheckVpsAvailabilityCompleteANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#VUID-xrCheckVpsAvailabilityCompleteANDROID-session-parameter) `session` **must** be a valid [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#VUID-xrCheckVpsAvailabilityCompleteANDROID-completion-parameter) `completion` **must** be a pointer to an [XrVPSAvailabilityCheckCompletionANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrVPSAvailabilityCheckCompletionANDROID) structure

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
- `XR_ERROR_RUNTIME_FAILURE`
- `XR_ERROR_SESSION_LOST`
- `XR_ERROR_VALIDATION_FAILURE`

The [XrVPSAvailabilityCheckCompletionANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrVPSAvailabilityCheckCompletionANDROID) structure is defined as:

    typedef struct XrVPSAvailabilityCheckCompletionANDROID {
        XrStructureType             type;
        void*                       next;
        XrResult                    futureResult;
        XrVPSAvailabilityANDROID    availability;
    } XrVPSAvailabilityCheckCompletionANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `futureResult` is the [XrResult](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrResult) of the check operation. If `futureResult` is `XR_ERROR_GEOSPATIAL_CLOUD_AUTH_FAILED_ANDROID` , a structure in the `next` chain **may** provide more information about the failure.
- `availability` is the resulting [XrVPSAvailabilityANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrVPSAvailabilityANDROID) . The application **must** not read this field unless `futureResult` is `XR_SUCCESS` .

### Future Return Codes

`futureResult` values:

[Success](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`
- `XR_SESSION_LOSS_PENDING`

[Failure](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_RUNTIME_FAILURE`
- `XR_ERROR_INSTANCE_LOST`
- `XR_ERROR_SESSION_LOST`
- `XR_ERROR_GEOSPATIAL_CLOUD_AUTH_FAILED_ANDROID`

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#VUID-XrVPSAvailabilityCheckCompletionANDROID-extension-notenabled) The `XR_ANDROID_geospatial` extension **must** be enabled prior to using [XrVPSAvailabilityCheckCompletionANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrVPSAvailabilityCheckCompletionANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#VUID-XrVPSAvailabilityCheckCompletionANDROID-type-type) `type` **must** be `XR_TYPE_VPS_AVAILABILITY_CHECK_COMPLETION_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#VUID-XrVPSAvailabilityCheckCompletionANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#VUID-XrVPSAvailabilityCheckCompletionANDROID-futureResult-parameter) `futureResult` **must** be a valid [XrResult](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrResult) value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#VUID-XrVPSAvailabilityCheckCompletionANDROID-availability-parameter) `availability` **must** be a valid [XrVPSAvailabilityANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrVPSAvailabilityANDROID) value

## Example

### Setup Geospatial Tracker

    PFN_xrCheckVpsAvailabilityAsyncANDROID xrCheckVpsAvailabilityAsyncANDROID;
    PFN_xrPollFutureEXT xrPollFutureEXT;
    PFN_xrCheckVpsAvailabilityCompleteANDROID xrCheckVpsAvailabilityCompleteANDROID;
    PFN_xrCreateGeospatialTrackerANDROID xrCreateGeospatialTrackerANDROID;
    XrInstance instance = XR_NULL_HANDLE;
    XrSystemId systemId = XR_NULL_SYSTEM_ID;
    XrSession session = XR_NULL_HANDLE;
    double lat = 37.422, lng = -122.084;

    // Check for support.
    XrSystemGeospatialPropertiesANDROID geospatialSystemProperties{
        XR_TYPE_SYSTEM_GEOSPATIAL_PROPERTIES_ANDROID};
    XrSystemProperties systemProperties{XR_TYPE_SYSTEM_PROPERTIES,
                                        &geospatialSystemProperties};
    CHK_XR(xrGetSystemProperties(instance, systemId, &systemProperties));
    if (!geospatialSystemProperties.supportsGeospatial) {
      return;
    }

    // Check VPS Availability.
    XrFutureEXT future = XR_NULL_FUTURE_EXT;
    CHK_XR(xrCheckVpsAvailabilityAsyncANDROID(session, lat, lng, &future));

    XrFuturePollInfoEXT pollInfo{XR_TYPE_FUTURE_POLL_INFO_EXT};
    XrFuturePollResultEXT pollResult{XR_TYPE_FUTURE_POLL_RESULT_EXT};
    pollInfo.future = future;
    pollResult.state = XR_FUTURE_STATE_PENDING_EXT;
    while (pollResult.state == XR_FUTURE_STATE_PENDING_EXT) {
      // Do in render loop/state loop.
      CHK_XR(xrPollFutureEXT(instance, &pollInfo, &pollResult));
    }

    XrVPSAvailabilityCheckCompletionANDROID vpsCompletion{
        XR_TYPE_VPS_AVAILABILITY_CHECK_COMPLETION_ANDROID};
    CHK_XR(xrCheckVpsAvailabilityCompleteANDROID(session, future, &vpsCompletion));
    if (vpsCompletion.futureResult == XR_SUCCESS) {
      if (vpsCompletion.availability == XR_VPS_AVAILABILITY_UNAVAILABLE_ANDROID) {
        // Visual Positioning Service is not available. Accuracy of positions and
        // orientations from Geospatial APIs are expected to be lower at this location.
      } else {
        // Visual Positioning Service is available. Higher accuracy of position and
        // orientation is achievable at this location.
      }
    }

    // Create Geospatial Tracker.
    XrGeospatialTrackerCreateInfoANDROID createInfo{
        XR_TYPE_GEOSPATIAL_TRACKER_CREATE_INFO_ANDROID};
    XrGeospatialTrackerANDROID geospatialTracker = XR_NULL_HANDLE;
    CHK_XR(xrCreateGeospatialTrackerANDROID(session, &createInfo, &geospatialTracker));

    // In application main event loop:
    while (true) {
      XrEventDataBuffer event = {XR_TYPE_EVENT_DATA_BUFFER};
      if (xrPollEvent(instance, &event) != XR_SUCCESS) {
        continue;
      }
      switch (event.type) {
        case XR_TYPE_EVENT_DATA_GEOSPATIAL_TRACKER_STATE_CHANGED_ANDROID:
          const XrEventDataGeospatialTrackerStateChangedANDROID& eventData =
              *reinterpret_cast<XrEventDataGeospatialTrackerStateChangedANDROID*>(&event);
          switch (eventData.state) {
            case XR_GEOSPATIAL_TRACKER_STATE_STOPPED_ANDROID:
              // Destroy existing anchors, if any.
              break;
            case XR_GEOSPATIAL_TRACKER_STATE_RUNNING_ANDROID:
              // Start adding content.
              break;
            case XR_GEOSPATIAL_TRACKER_STATE_INITIALIZATION_FAILED_ANDROID:
              // Handle eventData.initializationResult error result.
              break;
          }
      }
    }

### Call Geospatial Pose APIs

    PFN_xrLocateGeospatialPoseFromPoseANDROID xrLocateGeospatialPoseFromPoseANDROID;
    PFN_xrLocateGeospatialPoseANDROID xrLocateGeospatialPoseANDROID;

    XrGeospatialTrackerANDROID geospatialTracker;

    // Get pose from view space.
    XrSpace viewSpace;
    XrPosef identityPose = {{0,0,0,1},{0,0,0}};
    XrGeospatialPoseFromPoseLocateInfoANDROID poseGetInfo{
        XR_TYPE_GEOSPATIAL_POSE_FROM_POSE_LOCATE_INFO_ANDROID};
    XrGeospatialPoseResultANDROID poseResult{
        XR_TYPE_GEOSPATIAL_POSE_RESULT_ANDROID};
    poseGetInfo.space = viewSpace;
    poseGetInfo.pose = identityPose;
    poseGetInfo.time = 0;  // Next frame timestamp.
    CHK_XR(xrLocateGeospatialPoseFromPoseANDROID(geospatialTracker, &poseGetInfo, &poseResult));
    if ((poseResult.poseFlags & XR_GEOSPATIAL_POSE_ORIENTATION_VALID_BIT_ANDROID) &&
        (poseResult.poseFlags & XR_GEOSPATIAL_POSE_POSITION_VALID_BIT_ANDROID)) {
      // poseResult.geospatialPose is valid.
    }

    // Convert Geospatial pose to an XrSpaceLocation.
    XrGeospatialPoseLocateInfoANDROID poseLocateInfo{
        XR_TYPE_GEOSPATIAL_POSE_LOCATE_INFO_ANDROID};
    XrSpaceLocation location{XR_TYPE_SPACE_LOCATION};
    poseLocateInfo.space = viewSpace;
    poseLocateInfo.geospatialPose = poseResult.geospatialPose;
    poseLocateInfo.time = 0; // Next frame timestamp.
    CHK_XR(xrLocateGeospatialPoseANDROID(geospatialTracker, &poseLocateInfo, &location));
    if ((location.locationFlags & XR_SPACE_LOCATION_ORIENTATION_VALID_BIT) &&
        (location.locationFlags & XR_SPACE_LOCATION_POSITION_VALID_BIT)) {
      // location.pose is valid.
    }

## New Object Types

- [XrGeospatialTrackerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialTrackerANDROID)

## New Commands

- [xrCheckVpsAvailabilityAsyncANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#xrCheckVpsAvailabilityAsyncANDROID)
- [xrCheckVpsAvailabilityCompleteANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#xrCheckVpsAvailabilityCompleteANDROID)
- [xrCreateGeospatialTrackerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#xrCreateGeospatialTrackerANDROID)
- [xrDestroyGeospatialTrackerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#xrDestroyGeospatialTrackerANDROID)
- [xrLocateGeospatialPoseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#xrLocateGeospatialPoseANDROID)
- [xrLocateGeospatialPoseFromPoseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#xrLocateGeospatialPoseFromPoseANDROID)

## New Structures

- [XrEventDataGeospatialTrackerStateChangedANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrEventDataGeospatialTrackerStateChangedANDROID)
- [XrGeospatialPoseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialPoseANDROID)
- [XrGeospatialPoseFromPoseLocateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialPoseFromPoseLocateInfoANDROID)
- [XrGeospatialPoseLocateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialPoseLocateInfoANDROID)
- [XrGeospatialPoseResultANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialPoseResultANDROID)
- [XrGeospatialTrackerCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialTrackerCreateInfoANDROID)
- [XrVPSAvailabilityCheckCompletionANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrVPSAvailabilityCheckCompletionANDROID)
- Extending [XrSystemProperties](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSystemProperties) :

  - [XrSystemGeospatialPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrSystemGeospatialPropertiesANDROID)

## New Enums

- [XrGeospatialPoseFlagBitsANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialPoseFlagBitsANDROID)
- [XrGeospatialTrackerStateANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialTrackerStateANDROID)
- [XrVPSAvailabilityANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrVPSAvailabilityANDROID)

## New Bitmasks

- [XrGeospatialPoseFlagsANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial#XrGeospatialPoseFlagsANDROID)

## New Enum Constants

- `XR_ANDROID_GEOSPATIAL_EXTENSION_NAME`
- `XR_ANDROID_geospatial_SPEC_VERSION`
- Extending [XrObjectType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrObjectType) :

  - `XR_OBJECT_TYPE_GEOSPATIAL_TRACKER_ANDROID`
- Extending [XrResult](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrResult) :

  - `XR_ERROR_GEOSPATIAL_CLOUD_AUTH_FAILED_ANDROID`
  - `XR_ERROR_GEOSPATIAL_COORDINATES_INVALID_ANDROID`
  - `XR_ERROR_GEOSPATIAL_TRACKER_NOT_RUNNING_ANDROID`
- Extending [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) :

  - `XR_TYPE_EVENT_DATA_GEOSPATIAL_TRACKER_STATE_CHANGED_ANDROID`
  - `XR_TYPE_GEOSPATIAL_POSE_FROM_POSE_LOCATE_INFO_ANDROID`
  - `XR_TYPE_GEOSPATIAL_POSE_LOCATE_INFO_ANDROID`
  - `XR_TYPE_GEOSPATIAL_POSE_RESULT_ANDROID`
  - `XR_TYPE_GEOSPATIAL_TRACKER_CREATE_INFO_ANDROID`
  - `XR_TYPE_SYSTEM_GEOSPATIAL_PROPERTIES_ANDROID`
  - `XR_TYPE_VPS_AVAILABILITY_CHECK_COMPLETION_ANDROID`

**Issues**

**Version History**

- Revision 1, 2025-12-18 (Ben King)

  - Initial extension description.