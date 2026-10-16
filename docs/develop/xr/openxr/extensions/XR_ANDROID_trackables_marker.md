---
title: https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker
url: https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker
source: md.txt
---

### XR_ANDROID_trackables_marker

**Name String**

`XR_ANDROID_trackables_marker`

**Extension Type**

Instance extension

**Registered Extension Number**

708

**Revision**

1

**Ratification Status**

Not ratified

**Extension and Version Dependencies**

`XR_ANDROID_trackables`

**Deprecation State**

- *Deprecated* by `XR_EXT_spatial_marker_tracking` extension

**Last Modified Date**

2025-07-23

**IP Status**

No known IP claims.

**Contributors**

Christopher Doer, Google  

Diego Tipaldi, Google  

Levana Chen, Google  

Jared Finder, Google  

Spencer Quin, Google  

Nihav Jain, Google  

Ken Mackay, Google  

Daniel Guttenberg, Qualcomm

## Overview

This extension enables physical marker tracking, and enables applications to attach XR content to physical markers in an efficient way.

The extension supports well known marker types, specifically ArUco and April Tags. It enables runtimes to optionally support marker size estimation.

### Permissions

Android applications **must** have the android.permission.SCENE_UNDERSTANDING_COARSE permission listed in their manifest as this extension depends on `XR_ANDROID_trackables` and exposes the geometry of the environment. The android.permission.SCENE_UNDERSTANDING_COARSE permission is considered a dangerous permission i.e. applications **must** explicitly request the permission.

(protection level: dangerous)

## Inspect system capability

The [XrSystemMarkerTrackingPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#XrSystemMarkerTrackingPropertiesANDROID) structure is defined as:

    typedef struct XrSystemMarkerTrackingPropertiesANDROID {
        XrStructureType    type;
        void*              next;
        XrBool32           supportsMarkerTracking;
        XrBool32           supportsMarkerSizeEstimation;
        uint16_t           maxMarkerCount;
    } XrSystemMarkerTrackingPropertiesANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension. For more details about the structure chain, see the structure being extended ( [XrSystemProperties](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSystemProperties) ).
- `supportsMarkerTracking` is an `XrBool32` indicating if the current system provides marker tracking capability.
- `supportsMarkerSizeEstimation` is an `XrBool32` indicating if the current system provides marker size estimation.
- `maxMarkerCount` is the maximum number of markers that the runtime is able to track at the same time.

An application **can** inspect whether the system is capable of marker tracking by extending the [XrSystemProperties](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSystemProperties) with [XrSystemMarkerTrackingPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#XrSystemMarkerTrackingPropertiesANDROID) structure when calling [xrGetSystemProperties](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrGetSystemProperties) . The runtime **must** return `XR_ERROR_FEATURE_UNSUPPORTED` for marker tracker creation if and only if `supportsMarkerTracking` is `XR_FALSE` .

If a runtime supports marker tracking, `maxMarkerCount` **must** be at least 1.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#VUID-XrSystemMarkerTrackingPropertiesANDROID-extension-notenabled) The `XR_ANDROID_trackables_marker` extension **must** be enabled prior to using [XrSystemMarkerTrackingPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#XrSystemMarkerTrackingPropertiesANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#VUID-XrSystemMarkerTrackingPropertiesANDROID-type-type) `type` **must** be `XR_TYPE_SYSTEM_MARKER_TRACKING_PROPERTIES_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#VUID-XrSystemMarkerTrackingPropertiesANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)

## Tracking markers

This extension adds `XR_TRACKABLE_TYPE_MARKER_ANDROID` to [XrTrackableTypeANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackableTypeANDROID) .

The application creates an [XrTrackableTrackerANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackableTrackerANDROID) by calling [xrCreateTrackableTrackerANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateTrackableTrackerANDROID) and specifying `XR_TRACKABLE_TYPE_MARKER_ANDROID` as the trackable type in [XrTrackableTrackerCreateInfoANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackableTrackerCreateInfoANDROID) :: `trackableType` as well as setting a setting a valid configuration by adding a [XrTrackableMarkerConfigurationANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#XrTrackableMarkerConfigurationANDROID) to the next chain of [XrTrackableTrackerCreateInfoANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackableTrackerCreateInfoANDROID) .

The runtime **must** return `XR_ERROR_FEATURE_UNSUPPORTED` if [XrTrackableTrackerCreateInfoANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackableTrackerCreateInfoANDROID) :: `trackableType` is `XR_TRACKABLE_TYPE_MARKER_ANDROID` and [XrSystemMarkerTrackingPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#XrSystemMarkerTrackingPropertiesANDROID) :: `supportsMarkerTracking` returns `XR_FALSE` via [xrGetSystemProperties](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrGetSystemProperties) .

The [XrTrackableMarkerConfigurationANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#XrTrackableMarkerConfigurationANDROID) structure is defined as:

    typedef struct XrTrackableMarkerConfigurationANDROID {
        XrStructureType                            type;
        void*                                      next;
        XrTrackableMarkerTrackingModeANDROID       trackingMode;
        uint32_t                                   databaseCount;
        const XrTrackableMarkerDatabaseANDROID*    databases;
    } XrTrackableMarkerConfigurationANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `trackingMode` is an [XrTrackableMarkerTrackingModeANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#XrTrackableMarkerTrackingModeANDROID) indicating the desired mode for tracking.
- `databaseCount` is a `uint32_t` describing the count of elements in the `databases` array.
- `databases` is a pointer to an array of [XrTrackableMarkerDatabaseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#XrTrackableMarkerDatabaseANDROID) , each of which contains the desired markers from a given dictionary to track.

The application **must** set a valid configuration by adding a [XrTrackableMarkerConfigurationANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#XrTrackableMarkerConfigurationANDROID) to the [XrTrackableTrackerCreateInfoANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackableTrackerCreateInfoANDROID) :: `next` chain when calling [xrCreateTrackableTrackerANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateTrackableTrackerANDROID) with [XrTrackableTrackerCreateInfoANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackableTrackerCreateInfoANDROID) :: `trackableType` set to `XR_TRACKABLE_TYPE_MARKER_ANDROID` . Otherwise, if the tracker type is set as above but the configuration structure is not present or not valid, the runtime **must** return `XR_ERROR_VALIDATION_FAILURE` .

If a runtime supports marker size estimation, the application **can** set [XrTrackableMarkerDatabaseEntryANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#XrTrackableMarkerDatabaseEntryANDROID) :: `edgeSize` to `0` in [XrTrackableMarkerDatabaseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#XrTrackableMarkerDatabaseANDROID) :: `entries` to indicate the usage of size estimation. Otherwise, the application **must** set [XrTrackableMarkerDatabaseEntryANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#XrTrackableMarkerDatabaseEntryANDROID) :: `edgeSize` to a positive value or the runtime **must** return `XR_ERROR_VALIDATION_FAILURE` .

The runtime **must** filter the output from [xrGetAllTrackablesANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrGetAllTrackablesANDROID) to match the `trackingMode` and [XrTrackableMarkerDatabaseEntryANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#XrTrackableMarkerDatabaseEntryANDROID) :: `edgeSize` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#VUID-XrTrackableMarkerConfigurationANDROID-extension-notenabled) The `XR_ANDROID_trackables_marker` extension **must** be enabled prior to using [XrTrackableMarkerConfigurationANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#XrTrackableMarkerConfigurationANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#VUID-XrTrackableMarkerConfigurationANDROID-type-type) `type` **must** be `XR_TYPE_TRACKABLE_MARKER_CONFIGURATION_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#VUID-XrTrackableMarkerConfigurationANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#VUID-XrTrackableMarkerConfigurationANDROID-trackingMode-parameter) `trackingMode` **must** be a valid [XrTrackableMarkerTrackingModeANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#XrTrackableMarkerTrackingModeANDROID) value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#VUID-XrTrackableMarkerConfigurationANDROID-databases-parameter) `databases` **must** be a pointer to an array of `databaseCount` valid [XrTrackableMarkerDatabaseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#XrTrackableMarkerDatabaseANDROID) structures
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#VUID-XrTrackableMarkerConfigurationANDROID-databaseCount-arraylength) The `databaseCount` parameter **must** be greater than `0`

The [XrTrackableMarkerTrackingModeANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#XrTrackableMarkerTrackingModeANDROID) enum describes the supported tracking modes of markers.

    typedef enum XrTrackableMarkerTrackingModeANDROID {
        XR_TRACKABLE_MARKER_TRACKING_MODE_DYNAMIC_ANDROID = 0,
        XR_TRACKABLE_MARKER_TRACKING_MODE_STATIC_ANDROID = 1,
        XR_TRACKABLE_MARKER_TRACKING_MODE_MAX_ENUM_ANDROID = 0x7FFFFFFF
    } XrTrackableMarkerTrackingModeANDROID;

### Enumerant Descriptions

- `XR_TRACKABLE_MARKER_TRACKING_MODE_DYNAMIC_ANDROID` --- Tracking dynamic markers. This mode has the highest accuracy and works on moving and static markers, but also has the highest power consumption.
- `XR_TRACKABLE_MARKER_TRACKING_MODE_STATIC_ANDROID` --- Tracking static markers. This mode is primarily useful for markers that are known to be static, which leads to less power consumption in comparison to the dynamic mode.

The [XrTrackableMarkerDatabaseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#XrTrackableMarkerDatabaseANDROID) structure defines a dictionary and corresponding marker ids to be tracked.

    typedef struct XrTrackableMarkerDatabaseANDROID {
        XrTrackableMarkerDictionaryANDROID              dictionary;
        uint32_t                                        entryCount;
        const XrTrackableMarkerDatabaseEntryANDROID*    entries;
    } XrTrackableMarkerDatabaseANDROID;

### Member Descriptions

- `dictionary` is the [XrTrackableMarkerDictionaryANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#XrTrackableMarkerDictionaryANDROID) that all `entries` belong to.
- `entryCount` is a uint32_t describing the count of elements in the `entries` array. The application **can** set `entryCount` `0` to track all markers in the `dictionary` .
- `entries` is a pointer to an array of [XrTrackableMarkerDatabaseEntryANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#XrTrackableMarkerDatabaseEntryANDROID) , each of which contains the configuration of a marker to track.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#VUID-XrTrackableMarkerDatabaseANDROID-extension-notenabled) The `XR_ANDROID_trackables_marker` extension **must** be enabled prior to using [XrTrackableMarkerDatabaseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#XrTrackableMarkerDatabaseANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#VUID-XrTrackableMarkerDatabaseANDROID-dictionary-parameter) `dictionary` **must** be a valid [XrTrackableMarkerDictionaryANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#XrTrackableMarkerDictionaryANDROID) value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#VUID-XrTrackableMarkerDatabaseANDROID-entries-parameter) If `entryCount` is not `0` , `entries` **must** be a pointer to an array of `entryCount` [XrTrackableMarkerDatabaseEntryANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#XrTrackableMarkerDatabaseEntryANDROID) structures

The [XrTrackableMarkerDictionaryANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#XrTrackableMarkerDictionaryANDROID) enum describes the supported marker dictionaries.

    typedef enum XrTrackableMarkerDictionaryANDROID {
        XR_TRACKABLE_MARKER_DICTIONARY_ARUCO_4X4_50_ANDROID = 0,
        XR_TRACKABLE_MARKER_DICTIONARY_ARUCO_4X4_100_ANDROID = 1,
        XR_TRACKABLE_MARKER_DICTIONARY_ARUCO_4X4_250_ANDROID = 2,
        XR_TRACKABLE_MARKER_DICTIONARY_ARUCO_4X4_1000_ANDROID = 3,
        XR_TRACKABLE_MARKER_DICTIONARY_ARUCO_5X5_50_ANDROID = 4,
        XR_TRACKABLE_MARKER_DICTIONARY_ARUCO_5X5_100_ANDROID = 5,
        XR_TRACKABLE_MARKER_DICTIONARY_ARUCO_5X5_250_ANDROID = 6,
        XR_TRACKABLE_MARKER_DICTIONARY_ARUCO_5X5_1000_ANDROID = 7,
        XR_TRACKABLE_MARKER_DICTIONARY_ARUCO_6X6_50_ANDROID = 8,
        XR_TRACKABLE_MARKER_DICTIONARY_ARUCO_6X6_100_ANDROID = 9,
        XR_TRACKABLE_MARKER_DICTIONARY_ARUCO_6X6_250_ANDROID = 10,
        XR_TRACKABLE_MARKER_DICTIONARY_ARUCO_6X6_1000_ANDROID = 11,
        XR_TRACKABLE_MARKER_DICTIONARY_ARUCO_7X7_50_ANDROID = 12,
        XR_TRACKABLE_MARKER_DICTIONARY_ARUCO_7X7_100_ANDROID = 13,
        XR_TRACKABLE_MARKER_DICTIONARY_ARUCO_7X7_250_ANDROID = 14,
        XR_TRACKABLE_MARKER_DICTIONARY_ARUCO_7X7_1000_ANDROID = 15,
        XR_TRACKABLE_MARKER_DICTIONARY_APRILTAG_16H5_ANDROID = 16,
        XR_TRACKABLE_MARKER_DICTIONARY_APRILTAG_25H9_ANDROID = 17,
        XR_TRACKABLE_MARKER_DICTIONARY_APRILTAG_36H10_ANDROID = 18,
        XR_TRACKABLE_MARKER_DICTIONARY_APRILTAG_36H11_ANDROID = 19,
        XR_TRACKABLE_MARKER_DICTIONARY_MAX_ENUM_ANDROID = 0x7FFFFFFF
    } XrTrackableMarkerDictionaryANDROID;

The [XrTrackableMarkerDatabaseEntryANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#XrTrackableMarkerDatabaseEntryANDROID) structure configures a single marker id of a dictionary.

    typedef struct XrTrackableMarkerDatabaseEntryANDROID {
        int32_t    id;
        float      edgeSize;
    } XrTrackableMarkerDatabaseEntryANDROID;

### Member Descriptions

- `id` is the marker id as given in the dictionary.
- `edgeSize` represents the size of marker edge in meters. If the runtime supports marker size estimation, the application **can** set this to zero and the marker size will be estimated online. If this is set to zero but the runtime does not support marker size estimation, the runtime **must** return `XR_ERROR_VALIDATION_FAILURE` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#VUID-XrTrackableMarkerDatabaseEntryANDROID-extension-notenabled) The `XR_ANDROID_trackables_marker` extension **must** be enabled prior to using [XrTrackableMarkerDatabaseEntryANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#XrTrackableMarkerDatabaseEntryANDROID)

## Get markers

The [xrGetTrackableMarkerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#xrGetTrackableMarkerANDROID) function is defined as:

    XrResult xrGetTrackableMarkerANDROID(
        XrTrackableTrackerANDROID                   tracker,
        const XrTrackableGetInfoANDROID*            getInfo,
        XrTrackableMarkerANDROID*                   markerOutput);

### Parameter Descriptions

- `tracker` is the [XrTrackableTrackerANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackableTrackerANDROID) to query.
- `getInfo` is the [XrTrackableGetInfoANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackableGetInfoANDROID) with the information used to get the trackable marker.
- `markerOutput` is a pointer to the [XrTrackableMarkerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#XrTrackableMarkerANDROID) structure in which the trackable marker is returned.

The runtime **must** return `XR_ERROR_MISMATCHING_TRACKABLE_TYPE_ANDROID` if the trackable type of the `XrTrackableANDROID` is not `XR_TRACKABLE_TYPE_MARKER_ANDROID` , or if the trackable type of the [XrTrackableTrackerANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackableTrackerANDROID) is not `XR_TRACKABLE_TYPE_MARKER_ANDROID` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#VUID-xrGetTrackableMarkerANDROID-extension-notenabled) The `XR_ANDROID_trackables_marker` extension **must** be enabled prior to calling [xrGetTrackableMarkerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#xrGetTrackableMarkerANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#VUID-xrGetTrackableMarkerANDROID-tracker-parameter) `tracker` **must** be a valid [XrTrackableTrackerANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackableTrackerANDROID) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#VUID-xrGetTrackableMarkerANDROID-getInfo-parameter) `getInfo` **must** be a pointer to a valid [XrTrackableGetInfoANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackableGetInfoANDROID) structure
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#VUID-xrGetTrackableMarkerANDROID-markerOutput-parameter) `markerOutput` **must** be a pointer to an [XrTrackableMarkerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#XrTrackableMarkerANDROID) structure

### Return Codes

[Success](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`
- `XR_SESSION_LOSS_PENDING`

[Failure](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_HANDLE_INVALID`
- `XR_ERROR_INSTANCE_LOST`
- `XR_ERROR_LIMIT_REACHED`
- `XR_ERROR_MISMATCHING_TRACKABLE_TYPE_ANDROID`
- `XR_ERROR_RUNTIME_FAILURE`
- `XR_ERROR_SESSION_LOST`
- `XR_ERROR_TIME_INVALID`
- `XR_ERROR_VALIDATION_FAILURE`

The [XrTrackableMarkerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#XrTrackableMarkerANDROID) structure is defined as:

    typedef struct XrTrackableMarkerANDROID {
        XrStructureType                       type;
        void*                                 next;
        XrTrackingStateANDROID                trackingState;
        XrTime                                lastUpdatedTime;
        XrTrackableMarkerDictionaryANDROID    dictionary;
        int32_t                               markerId;
        XrPosef                               centerPose;
        XrExtent2Df                           extents;
    } XrTrackableMarkerANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.
- `trackingState` is the [XrTrackingStateANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackingStateANDROID) of the marker.
- `lastUpdatedTime` is the `XrTime` of the last update of the marker.
- `dictionary` is the [XrTrackableMarkerDictionaryANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#XrTrackableMarkerDictionaryANDROID) of the marker.
- `markerId` is the marker id as given in the dictionary.
- `centerPose` is the [XrPosef](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrPosef) of the marker located in [XrTrackableGetInfoANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackableGetInfoANDROID) :: `baseSpace` . The marker lies in the XZ plane with X pointing to the right of the marker and Z pointing to its bottom and Y coming out of the marker as the normal.
- `extents` is the [XrExtent2Df](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrExtent2Df) dimensions of the marker. The boundary of the bounding box is at points: `centerPose` +/- ( `extents` / 2).

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#VUID-XrTrackableMarkerANDROID-extension-notenabled) The `XR_ANDROID_trackables_marker` extension **must** be enabled prior to using [XrTrackableMarkerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#XrTrackableMarkerANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#VUID-XrTrackableMarkerANDROID-type-type) `type` **must** be `XR_TYPE_TRACKABLE_MARKER_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#VUID-XrTrackableMarkerANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#VUID-XrTrackableMarkerANDROID-trackingState-parameter) `trackingState` **must** be a valid [XrTrackingStateANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackingStateANDROID) value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#VUID-XrTrackableMarkerANDROID-dictionary-parameter) `dictionary` **must** be a valid [XrTrackableMarkerDictionaryANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#XrTrackableMarkerDictionaryANDROID) value

## Example code for getting trackable markers

The following example code demonstrates how to get trackable markers.

    XrInstance instance; // previously initialized
    XrSystemId systemId; // previously initialized
    XrSession session;   // previously initialized

    // The function pointers are previously initialized using xrGetInstanceProcAddr.
    PFN_xrGetSystemProperties xrGetSystemProperties;                       // previously initialized
    PFN_xrCreateTrackableTrackerANDROID xrCreateTrackableTrackerANDROID;   // previously initialized
    PFN_xrGetAllTrackablesANDROID xrGetAllTrackablesANDROID;               // previously initialized
    PFN_xrGetTrackableMarkerANDROID xrGetTrackableMarkerANDROID;           // previously initialized
    PFN_xrDestroyTrackableTrackerANDROID xrDestroyTrackableTrackerANDROID; // previously initialized

    XrTime updateTime; // Time used for the current frame's simulation update.
    XrSpace appSpace;  // Space created for XR_REFERENCE_SPACE_TYPE_LOCAL.

    // Inspect system capability
    XrSystemMarkerTrackingPropertiesANDROID markerProperty {
      .type = XR_TYPE_SYSTEM_MARKER_TRACKING_PROPERTIES_ANDROID,
      .next = nullptr,
    };
    XrSystemProperties systemProperties {
      .type = XR_TYPE_SYSTEM_PROPERTIES,
      .next = &markerProperty,
    };
    CHK_XR(xrGetSystemProperties(instance, systemId, &systemProperties));
    if (!markerProperty.supportsMarkerTracking) {
        // Marker tracking is not supported.
        return;
    }

    // Create a trackable tracker for marker tracking.
    // If the runtime does not support size estimation, configures marker edge size of 0.1m.
    XrTrackableMarkerDatabaseEntryANDROID markerEntries {
      .id = 0,
      .edgeSize = markerProperty.supportsMarkerSizeEstimation ? 0.0f : 0.1f,
    };
    XrTrackableMarkerDatabaseANDROID markerDatabases {
      .dictionary = XR_TRACKABLE_MARKER_DICTIONARY_ARUCO_4X4_50_ANDROID,
      .entryCount = 1,
      .entries = &markerEntries,
    };
    XrTrackableMarkerConfigurationANDROID configuration {
      .type = XR_TYPE_TRACKABLE_MARKER_CONFIGURATION_ANDROID,
      .next = nullptr,
      .trackingMode = XR_TRACKABLE_MARKER_TRACKING_MODE_DYNAMIC_ANDROID,
      .databaseCount = 1,
      .databases = &markerDatabases,
    };
    XrTrackableTrackerCreateInfoANDROID createInfo {
      .type = XR_TYPE_TRACKABLE_TRACKER_CREATE_INFO_ANDROID,
      .next = &configuration,
      .trackableType = XR_TRACKABLE_TYPE_MARKER_ANDROID,
    };
    XrTrackableTrackerANDROID markerTracker;
    auto res = xrCreateTrackableTrackerANDROID(session, &createInfo, &markerTracker);
    if (res == XR_ERROR_PERMISSION_INSUFFICIENT) {
        // Handle permission requests.
    }
    CHK_XR(res);

    // Get markers.
    std::vector<XrTrackableANDROID> trackables(markerProperty.maxMarkerCount);
    std::vector<XrTrackableMarkerANDROID> markers(markerProperty.maxMarkerCount, {
      .type = XR_TYPE_TRACKABLE_MARKER_ANDROID,
      .next = nullptr,
    });
    uint32_t markerSize = 0;
    CHK_XR(xrGetAllTrackablesANDROID(markerTracker, markerProperty.maxMarkerCount, &markerSize,
                                     trackables.data()));
    for (int i = 0; i < markerSize; i++) {
        XrTrackableGetInfoANDROID getInfo {
          .type = XR_TYPE_TRACKABLE_GET_INFO_ANDROID,
          .next = nullptr,
          .trackable = trackables[i],
          .baseSpace = appSpace,
          .time = updateTime,
        };
        CHK_XR(xrGetTrackableMarkerANDROID(markerTracker, &getInfo, &markers[i]));
        // Handle markers.
    }

    // Release trackable tracker.
    CHK_XR(xrDestroyTrackableTrackerANDROID(markerTracker));

## New Commands

- [xrGetTrackableMarkerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#xrGetTrackableMarkerANDROID)

## New Structures

- [XrTrackableMarkerANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#XrTrackableMarkerANDROID)
- [XrTrackableMarkerDatabaseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#XrTrackableMarkerDatabaseANDROID)
- [XrTrackableMarkerDatabaseEntryANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#XrTrackableMarkerDatabaseEntryANDROID)
- Extending [XrSystemProperties](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSystemProperties) :

  - [XrSystemMarkerTrackingPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#XrSystemMarkerTrackingPropertiesANDROID)
- Extending [XrTrackableTrackerCreateInfoANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackableTrackerCreateInfoANDROID) :

  - [XrTrackableMarkerConfigurationANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#XrTrackableMarkerConfigurationANDROID)

## New Enums

- [XrTrackableMarkerDictionaryANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#XrTrackableMarkerDictionaryANDROID)
- [XrTrackableMarkerTrackingModeANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker#XrTrackableMarkerTrackingModeANDROID)

## New Enum Constants

- `XR_ANDROID_TRACKABLES_MARKER_EXTENSION_NAME`
- `XR_ANDROID_trackables_marker_SPEC_VERSION`
- Extending [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) :

  - `XR_TYPE_SYSTEM_MARKER_TRACKING_PROPERTIES_ANDROID`
  - `XR_TYPE_TRACKABLE_MARKER_ANDROID`
  - `XR_TYPE_TRACKABLE_MARKER_CONFIGURATION_ANDROID`
- Extending [XrTrackableTypeANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackableTypeANDROID) :

  - `XR_TRACKABLE_TYPE_MARKER_ANDROID`

## Issues

## Version History

- Revision 1, 2025-07-23 (Levana Chen)

  - Initial extension description.