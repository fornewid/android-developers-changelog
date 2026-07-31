---
title: https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking
url: https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking
source: md.txt
---

### XR_EXT_spatial_marker_tracking

**Name String**

`XR_EXT_spatial_marker_tracking`

**Extension Type**

Instance extension

**Registered Extension Number**

744

**Revision**

1

**Ratification Status**

Ratified

**Extension and Version Dependencies**

`XR_EXT_spatial_entity`

**Contributors**

Ron Bessems, Meta  

Nihav Jain, Google  

Natalie Fleury, Meta  

Yuichi Taguchi, Meta  

Yin Li, Microsoft  

Jimmy Alamparambil, ByteDance  

Zhipeng Liu, ByteDance  

Jun Yan, ByteDance

## Overview

This extension builds on `XR_EXT_spatial_entity` and allows applications to detect and track markers in their environment. Markers are 2D codes which **may** include QR Codes, Micro QR Codes, ArUco markers, or AprilTags.

A tracked marker is represented as a spatial entity with (or "that has") the following components:

- `XR_SPATIAL_COMPONENT_TYPE_MARKER_EXT`
- `XR_SPATIAL_COMPONENT_TYPE_BOUNDED_2D_EXT`

## Runtime support

A runtime **must** advertise its support for the various marker tracking capabilities using [xrEnumerateSpatialCapabilitiesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrEnumerateSpatialCapabilitiesEXT) by listing any of the following capabilities:

- `XR_SPATIAL_CAPABILITY_MARKER_TRACKING_QR_CODE_EXT`
- `XR_SPATIAL_CAPABILITY_MARKER_TRACKING_MICRO_QR_CODE_EXT`
- `XR_SPATIAL_CAPABILITY_MARKER_TRACKING_ARUCO_MARKER_EXT`
- `XR_SPATIAL_CAPABILITY_MARKER_TRACKING_APRIL_TAG_EXT`

## Configuration

To enable detection of a marker type the application **must** pass the corresponding configuration structure to [xrCreateSpatialContextAsyncEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateSpatialContextAsyncEXT) .

### Marker Type Configurations

###### QR codes

The [XrSpatialCapabilityConfigurationQrCodeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialCapabilityConfigurationQrCodeEXT) structure is defined as:

    typedef struct XrSpatialCapabilityConfigurationQrCodeEXT {
        XrStructureType                     type;
        const void*                         next;
        XrSpatialCapabilityEXT              capability;
        uint32_t                            enabledComponentCount;
        const XrSpatialComponentTypeEXT*    enabledComponents;
    } XrSpatialCapabilityConfigurationQrCodeEXT;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `capability` **must** be `XR_SPATIAL_CAPABILITY_MARKER_TRACKING_QR_CODE_EXT` .
- `enabledComponentCount` is a `uint32_t` with the number of elements in `enabledComponents` .
- `enabledComponents` is a pointer to an array of components to enable for this capability.

If QR codes are supported, the runtime **must** enable QR Code tracking when an [XrSpatialCapabilityConfigurationQrCodeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialCapabilityConfigurationQrCodeEXT) structure is passed in [XrSpatialContextCreateInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextCreateInfoEXT) :: `capabilityConfigs` when calling [xrCreateSpatialContextAsyncEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateSpatialContextAsyncEXT) .

The runtime **must** return `XR_ERROR_SPATIAL_CAPABILITY_UNSUPPORTED_EXT` if `XR_SPATIAL_CAPABILITY_MARKER_TRACKING_QR_CODE_EXT` is not enumerated by [xrEnumerateSpatialCapabilitiesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrEnumerateSpatialCapabilitiesEXT) .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#VUID-XrSpatialCapabilityConfigurationQrCodeEXT-extension-notenabled) The `XR_EXT_spatial_marker_tracking` extension **must** be enabled prior to using [XrSpatialCapabilityConfigurationQrCodeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialCapabilityConfigurationQrCodeEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#VUID-XrSpatialCapabilityConfigurationQrCodeEXT-type-type) `type` **must** be `XR_TYPE_SPATIAL_CAPABILITY_CONFIGURATION_QR_CODE_EXT`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#VUID-XrSpatialCapabilityConfigurationQrCodeEXT-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains) . See also: [XrSpatialMarkerSizeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialMarkerSizeEXT) , [XrSpatialMarkerStaticOptimizationEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialMarkerStaticOptimizationEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#VUID-XrSpatialCapabilityConfigurationQrCodeEXT-capability-parameter) `capability` **must** be a valid [XrSpatialCapabilityEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityEXT) value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#VUID-XrSpatialCapabilityConfigurationQrCodeEXT-enabledComponents-parameter) `enabledComponents` **must** be a pointer to an array of `enabledComponentCount` valid [XrSpatialComponentTypeEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentTypeEXT) values
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#VUID-XrSpatialCapabilityConfigurationQrCodeEXT-enabledComponentCount-arraylength) The `enabledComponentCount` parameter **must** be greater than `0`

###### Micro QR codes

The [XrSpatialCapabilityConfigurationMicroQrCodeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialCapabilityConfigurationMicroQrCodeEXT) structure is defined as:

    typedef struct XrSpatialCapabilityConfigurationMicroQrCodeEXT {
        XrStructureType                     type;
        const void*                         next;
        XrSpatialCapabilityEXT              capability;
        uint32_t                            enabledComponentCount;
        const XrSpatialComponentTypeEXT*    enabledComponents;
    } XrSpatialCapabilityConfigurationMicroQrCodeEXT;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `capability` **must** be `XR_SPATIAL_CAPABILITY_MARKER_TRACKING_MICRO_QR_CODE_EXT` .
- `enabledComponentCount` is a `uint32_t` with the number of elements in `enabledComponents` .
- `enabledComponents` is a pointer to an array of components to enable for this capability.

If Micro QR codes are supported, the runtime **must** enable Micro QR Code tracking when an [XrSpatialCapabilityConfigurationMicroQrCodeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialCapabilityConfigurationMicroQrCodeEXT) structure is passed in [XrSpatialContextCreateInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextCreateInfoEXT) :: `capabilityConfigs` when calling [xrCreateSpatialContextAsyncEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateSpatialContextAsyncEXT) .

The runtime **must** return `XR_ERROR_SPATIAL_CAPABILITY_UNSUPPORTED_EXT` if `XR_SPATIAL_CAPABILITY_MARKER_TRACKING_MICRO_QR_CODE_EXT` is not enumerated by [xrEnumerateSpatialCapabilitiesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrEnumerateSpatialCapabilitiesEXT) .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#VUID-XrSpatialCapabilityConfigurationMicroQrCodeEXT-extension-notenabled) The `XR_EXT_spatial_marker_tracking` extension **must** be enabled prior to using [XrSpatialCapabilityConfigurationMicroQrCodeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialCapabilityConfigurationMicroQrCodeEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#VUID-XrSpatialCapabilityConfigurationMicroQrCodeEXT-type-type) `type` **must** be `XR_TYPE_SPATIAL_CAPABILITY_CONFIGURATION_MICRO_QR_CODE_EXT`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#VUID-XrSpatialCapabilityConfigurationMicroQrCodeEXT-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains) . See also: [XrSpatialMarkerSizeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialMarkerSizeEXT) , [XrSpatialMarkerStaticOptimizationEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialMarkerStaticOptimizationEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#VUID-XrSpatialCapabilityConfigurationMicroQrCodeEXT-capability-parameter) `capability` **must** be a valid [XrSpatialCapabilityEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityEXT) value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#VUID-XrSpatialCapabilityConfigurationMicroQrCodeEXT-enabledComponents-parameter) `enabledComponents` **must** be a pointer to an array of `enabledComponentCount` valid [XrSpatialComponentTypeEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentTypeEXT) values
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#VUID-XrSpatialCapabilityConfigurationMicroQrCodeEXT-enabledComponentCount-arraylength) The `enabledComponentCount` parameter **must** be greater than `0`

###### ArUco Markers

The [XrSpatialCapabilityConfigurationArucoMarkerEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialCapabilityConfigurationArucoMarkerEXT) structure is defined as:

    typedef struct XrSpatialCapabilityConfigurationArucoMarkerEXT {
        XrStructureType                     type;
        const void*                         next;
        XrSpatialCapabilityEXT              capability;
        uint32_t                            enabledComponentCount;
        const XrSpatialComponentTypeEXT*    enabledComponents;
        XrSpatialMarkerArucoDictEXT         arUcoDict;
    } XrSpatialCapabilityConfigurationArucoMarkerEXT;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `capability` **must** be `XR_SPATIAL_CAPABILITY_MARKER_TRACKING_ARUCO_MARKER_EXT` .
- `enabledComponentCount` is a `uint32_t` with the number of elements in `enabledComponents` .
- `enabledComponents` is a pointer to an array of components to enable for this capability.
- `arUcoDict` is the marker dictionary to detect.

If ArUco markers are supported, the runtime **must** enable ArUco marker tracking when an [XrSpatialCapabilityConfigurationArucoMarkerEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialCapabilityConfigurationArucoMarkerEXT) structure is passed in [XrSpatialContextCreateInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextCreateInfoEXT) :: `capabilityConfigs` when calling [xrCreateSpatialContextAsyncEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateSpatialContextAsyncEXT) .

The runtime **must** return `XR_ERROR_SPATIAL_CAPABILITY_UNSUPPORTED_EXT` from [xrCreateSpatialContextAsyncEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateSpatialContextAsyncEXT) if an [XrSpatialCapabilityConfigurationArucoMarkerEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialCapabilityConfigurationArucoMarkerEXT) structure is in [XrSpatialContextCreateInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextCreateInfoEXT) :: `capabilityConfigs` but `XR_SPATIAL_CAPABILITY_MARKER_TRACKING_ARUCO_MARKER_EXT` is not enumerated by [xrEnumerateSpatialCapabilitiesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrEnumerateSpatialCapabilitiesEXT) .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#VUID-XrSpatialCapabilityConfigurationArucoMarkerEXT-extension-notenabled) The `XR_EXT_spatial_marker_tracking` extension **must** be enabled prior to using [XrSpatialCapabilityConfigurationArucoMarkerEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialCapabilityConfigurationArucoMarkerEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#VUID-XrSpatialCapabilityConfigurationArucoMarkerEXT-type-type) `type` **must** be `XR_TYPE_SPATIAL_CAPABILITY_CONFIGURATION_ARUCO_MARKER_EXT`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#VUID-XrSpatialCapabilityConfigurationArucoMarkerEXT-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains) . See also: [XrSpatialMarkerSizeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialMarkerSizeEXT) , [XrSpatialMarkerStaticOptimizationEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialMarkerStaticOptimizationEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#VUID-XrSpatialCapabilityConfigurationArucoMarkerEXT-capability-parameter) `capability` **must** be a valid [XrSpatialCapabilityEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityEXT) value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#VUID-XrSpatialCapabilityConfigurationArucoMarkerEXT-enabledComponents-parameter) `enabledComponents` **must** be a pointer to an array of `enabledComponentCount` valid [XrSpatialComponentTypeEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentTypeEXT) values
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#VUID-XrSpatialCapabilityConfigurationArucoMarkerEXT-arUcoDict-parameter) `arUcoDict` **must** be a valid [XrSpatialMarkerArucoDictEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialMarkerArucoDictEXT) value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#VUID-XrSpatialCapabilityConfigurationArucoMarkerEXT-enabledComponentCount-arraylength) The `enabledComponentCount` parameter **must** be greater than `0`

The [XrSpatialMarkerArucoDictEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialMarkerArucoDictEXT) enumeration is defined as:

    typedef enum XrSpatialMarkerArucoDictEXT {
        XR_SPATIAL_MARKER_ARUCO_DICT_4X4_50_EXT = 1,
        XR_SPATIAL_MARKER_ARUCO_DICT_4X4_100_EXT = 2,
        XR_SPATIAL_MARKER_ARUCO_DICT_4X4_250_EXT = 3,
        XR_SPATIAL_MARKER_ARUCO_DICT_4X4_1000_EXT = 4,
        XR_SPATIAL_MARKER_ARUCO_DICT_5X5_50_EXT = 5,
        XR_SPATIAL_MARKER_ARUCO_DICT_5X5_100_EXT = 6,
        XR_SPATIAL_MARKER_ARUCO_DICT_5X5_250_EXT = 7,
        XR_SPATIAL_MARKER_ARUCO_DICT_5X5_1000_EXT = 8,
        XR_SPATIAL_MARKER_ARUCO_DICT_6X6_50_EXT = 9,
        XR_SPATIAL_MARKER_ARUCO_DICT_6X6_100_EXT = 10,
        XR_SPATIAL_MARKER_ARUCO_DICT_6X6_250_EXT = 11,
        XR_SPATIAL_MARKER_ARUCO_DICT_6X6_1000_EXT = 12,
        XR_SPATIAL_MARKER_ARUCO_DICT_7X7_50_EXT = 13,
        XR_SPATIAL_MARKER_ARUCO_DICT_7X7_100_EXT = 14,
        XR_SPATIAL_MARKER_ARUCO_DICT_7X7_250_EXT = 15,
        XR_SPATIAL_MARKER_ARUCO_DICT_7X7_1000_EXT = 16,
        XR_SPATIAL_MARKER_ARUCO_DICT_MAX_ENUM_EXT = 0x7FFFFFFF
    } XrSpatialMarkerArucoDictEXT;

Supported predefined ArUco dictionary:

### Enumerant Descriptions

- `XR_SPATIAL_MARKER_ARUCO_DICT_4X4_50_EXT` --- 4 by 4 pixel Aruco marker dictionary with 50 IDs.
- `XR_SPATIAL_MARKER_ARUCO_DICT_4X4_100_EXT` --- 4 by 4 pixel Aruco marker dictionary with 100 IDs.
- `XR_SPATIAL_MARKER_ARUCO_DICT_4X4_250_EXT` --- 4 by 4 pixel Aruco marker dictionary with 250 IDs.
- `XR_SPATIAL_MARKER_ARUCO_DICT_4X4_1000_EXT` --- 4 by 4 pixel Aruco marker dictionary with 1000 IDs.
- `XR_SPATIAL_MARKER_ARUCO_DICT_5X5_50_EXT` --- 5 by 5 pixel Aruco marker dictionary with 50 IDs.
- `XR_SPATIAL_MARKER_ARUCO_DICT_5X5_100_EXT` --- 5 by 5 pixel Aruco marker dictionary with 100 IDs.
- `XR_SPATIAL_MARKER_ARUCO_DICT_5X5_250_EXT` --- 5 by 5 pixel Aruco marker dictionary with 250 IDs.
- `XR_SPATIAL_MARKER_ARUCO_DICT_5X5_1000_EXT` --- 5 by 5 pixel Aruco marker dictionary with 1000 IDs.
- `XR_SPATIAL_MARKER_ARUCO_DICT_6X6_50_EXT` --- 6 by 6 pixel Aruco marker dictionary with 50 IDs.
- `XR_SPATIAL_MARKER_ARUCO_DICT_6X6_100_EXT` --- 6 by 6 pixel Aruco marker dictionary with 100 IDs.
- `XR_SPATIAL_MARKER_ARUCO_DICT_6X6_250_EXT` --- 6 by 6 pixel Aruco marker dictionary with 250 IDs.
- `XR_SPATIAL_MARKER_ARUCO_DICT_6X6_1000_EXT` --- 6 by 6 pixel Aruco marker dictionary with 1000 IDs.
- `XR_SPATIAL_MARKER_ARUCO_DICT_7X7_50_EXT` --- 7 by 7 pixel Aruco marker dictionary with 50 IDs.
- `XR_SPATIAL_MARKER_ARUCO_DICT_7X7_100_EXT` --- 7 by 7 pixel Aruco marker dictionary with 100 IDs.
- `XR_SPATIAL_MARKER_ARUCO_DICT_7X7_250_EXT` --- 7 by 7 pixel Aruco marker dictionary with 250 IDs.
- `XR_SPATIAL_MARKER_ARUCO_DICT_7X7_1000_EXT` --- 7 by 7 pixel Aruco marker dictionary with 1000 IDs.

###### AprilTags

The [XrSpatialCapabilityConfigurationAprilTagEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialCapabilityConfigurationAprilTagEXT) structure is defined as:

    typedef struct XrSpatialCapabilityConfigurationAprilTagEXT {
        XrStructureType                     type;
        const void*                         next;
        XrSpatialCapabilityEXT              capability;
        uint32_t                            enabledComponentCount;
        const XrSpatialComponentTypeEXT*    enabledComponents;
        XrSpatialMarkerAprilTagDictEXT      aprilDict;
    } XrSpatialCapabilityConfigurationAprilTagEXT;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `capability` **must** be `XR_SPATIAL_CAPABILITY_MARKER_TRACKING_APRIL_TAG_EXT` .
- `enabledComponentCount` is a `uint32_t` with the number of elements in `enabledComponents` .
- `enabledComponents` is a pointer to an array of components to enable for this capability.
- `aprilDict` is the marker dictionary to detect.

If AprilTags are supported, the runtime **must** enable AprilTag tracking when an [XrSpatialCapabilityConfigurationAprilTagEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialCapabilityConfigurationAprilTagEXT) structure is passed in [XrSpatialContextCreateInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextCreateInfoEXT) :: `capabilityConfigs` when calling [xrCreateSpatialContextAsyncEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateSpatialContextAsyncEXT) .

The runtime **must** return `XR_ERROR_SPATIAL_CAPABILITY_UNSUPPORTED_EXT` from [xrCreateSpatialContextAsyncEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateSpatialContextAsyncEXT) if an [XrSpatialCapabilityConfigurationAprilTagEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialCapabilityConfigurationAprilTagEXT) structure is in [XrSpatialContextCreateInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextCreateInfoEXT) :: `capabilityConfigs` but `XR_SPATIAL_CAPABILITY_MARKER_TRACKING_APRIL_TAG_EXT` is not enumerated by [xrEnumerateSpatialCapabilitiesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrEnumerateSpatialCapabilitiesEXT) .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#VUID-XrSpatialCapabilityConfigurationAprilTagEXT-extension-notenabled) The `XR_EXT_spatial_marker_tracking` extension **must** be enabled prior to using [XrSpatialCapabilityConfigurationAprilTagEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialCapabilityConfigurationAprilTagEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#VUID-XrSpatialCapabilityConfigurationAprilTagEXT-type-type) `type` **must** be `XR_TYPE_SPATIAL_CAPABILITY_CONFIGURATION_APRIL_TAG_EXT`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#VUID-XrSpatialCapabilityConfigurationAprilTagEXT-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains) . See also: [XrSpatialMarkerSizeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialMarkerSizeEXT) , [XrSpatialMarkerStaticOptimizationEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialMarkerStaticOptimizationEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#VUID-XrSpatialCapabilityConfigurationAprilTagEXT-capability-parameter) `capability` **must** be a valid [XrSpatialCapabilityEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityEXT) value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#VUID-XrSpatialCapabilityConfigurationAprilTagEXT-enabledComponents-parameter) `enabledComponents` **must** be a pointer to an array of `enabledComponentCount` valid [XrSpatialComponentTypeEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentTypeEXT) values
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#VUID-XrSpatialCapabilityConfigurationAprilTagEXT-aprilDict-parameter) `aprilDict` **must** be a valid [XrSpatialMarkerAprilTagDictEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialMarkerAprilTagDictEXT) value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#VUID-XrSpatialCapabilityConfigurationAprilTagEXT-enabledComponentCount-arraylength) The `enabledComponentCount` parameter **must** be greater than `0`

The [XrSpatialMarkerAprilTagDictEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialMarkerAprilTagDictEXT) enumeration is defined as:

    typedef enum XrSpatialMarkerAprilTagDictEXT {
        XR_SPATIAL_MARKER_APRIL_TAG_DICT_16H5_EXT = 1,
        XR_SPATIAL_MARKER_APRIL_TAG_DICT_25H9_EXT = 2,
        XR_SPATIAL_MARKER_APRIL_TAG_DICT_36H10_EXT = 3,
        XR_SPATIAL_MARKER_APRIL_TAG_DICT_36H11_EXT = 4,
        XR_SPATIAL_MARKER_APRIL_TAG_DICT_MAX_ENUM_EXT = 0x7FFFFFFF
    } XrSpatialMarkerAprilTagDictEXT;

Supported predefined AprilTag dictionary:

### Enumerant Descriptions

- `XR_SPATIAL_MARKER_APRIL_TAG_DICT_16H5_EXT` --- 4 by 4 bits, minimum Hamming distance between any two codes = 5, 30 codes.
- `XR_SPATIAL_MARKER_APRIL_TAG_DICT_25H9_EXT` --- 5 by 5 bits, minimum Hamming distance between any two codes = 9, 35 codes.
- `XR_SPATIAL_MARKER_APRIL_TAG_DICT_36H10_EXT` --- 6 by 6 bits, minimum Hamming distance between any two codes = 10, 2320 codes.
- `XR_SPATIAL_MARKER_APRIL_TAG_DICT_36H11_EXT` --- 6 by 6 bits, minimum Hamming distance between any two codes = 11, 587 codes.

### Optional Marker Configurations

Applications **should** call [xrEnumerateSpatialCapabilityFeaturesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrEnumerateSpatialCapabilityFeaturesEXT) to get the list of supported optional features.

See [XrSpatialCapabilityFeatureEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityFeatureEXT) for a complete list of all spatial capability features supported by any extension.

###### Marker Size

The [XrSpatialMarkerSizeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialMarkerSizeEXT) structure is defined as:

    typedef struct XrSpatialMarkerSizeEXT {
        XrStructureType    type;
        const void*        next;
        float              markerSideLength;
    } XrSpatialMarkerSizeEXT;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `markerSideLength` is the size in meters of all markers.

If `XR_SPATIAL_CAPABILITY_FEATURE_MARKER_TRACKING_FIXED_SIZE_MARKERS_EXT` is enumerated by [xrEnumerateSpatialCapabilityFeaturesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrEnumerateSpatialCapabilityFeaturesEXT) for a certain capability, and if the application chains [XrSpatialMarkerSizeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialMarkerSizeEXT) to the corresponding configuration structure of that capability, the runtime **must** assume that all markers detected have width and height of `markerSideLength` . Providing this information to the runtime allows the runtime to return a more accurate pose and size. This structure **must** be linked into the `next` chain of [XrSpatialCapabilityConfigurationQrCodeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialCapabilityConfigurationQrCodeEXT) , [XrSpatialCapabilityConfigurationMicroQrCodeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialCapabilityConfigurationMicroQrCodeEXT) , [XrSpatialCapabilityConfigurationArucoMarkerEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialCapabilityConfigurationArucoMarkerEXT) , or [XrSpatialCapabilityConfigurationAprilTagEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialCapabilityConfigurationAprilTagEXT) .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#VUID-XrSpatialMarkerSizeEXT-extension-notenabled) The `XR_EXT_spatial_marker_tracking` extension **must** be enabled prior to using [XrSpatialMarkerSizeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialMarkerSizeEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#VUID-XrSpatialMarkerSizeEXT-type-type) `type` **must** be `XR_TYPE_SPATIAL_MARKER_SIZE_EXT`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#VUID-XrSpatialMarkerSizeEXT-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)

###### Static Marker Optimization

The [XrSpatialMarkerStaticOptimizationEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialMarkerStaticOptimizationEXT) structure is defined as:

    typedef struct XrSpatialMarkerStaticOptimizationEXT {
        XrStructureType    type;
        const void*        next;
        XrBool32           optimizeForStaticMarker;
    } XrSpatialMarkerStaticOptimizationEXT;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `optimizeForStaticMarker` indicates if all markers in the space are expected to not move.

If `XR_SPATIAL_CAPABILITY_FEATURE_MARKER_TRACKING_STATIC_MARKERS_EXT` is enumerated by [xrEnumerateSpatialCapabilityFeaturesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrEnumerateSpatialCapabilityFeaturesEXT) for a certain capability, and if the application chains [XrSpatialMarkerStaticOptimizationEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialMarkerStaticOptimizationEXT) to the corresponding configuration structure of that capability, the runtime **must** assume that all markers detected are static if `optimizeForStaticMarker` is set to `XR_TRUE` . This allows the runtime to generate a more accurate pose and size. This structure **must** be linked into the `next` chain of [XrSpatialCapabilityConfigurationQrCodeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialCapabilityConfigurationQrCodeEXT) , [XrSpatialCapabilityConfigurationMicroQrCodeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialCapabilityConfigurationMicroQrCodeEXT) , [XrSpatialCapabilityConfigurationArucoMarkerEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialCapabilityConfigurationArucoMarkerEXT) , or [XrSpatialCapabilityConfigurationAprilTagEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialCapabilityConfigurationAprilTagEXT) .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#VUID-XrSpatialMarkerStaticOptimizationEXT-extension-notenabled) The `XR_EXT_spatial_marker_tracking` extension **must** be enabled prior to using [XrSpatialMarkerStaticOptimizationEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialMarkerStaticOptimizationEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#VUID-XrSpatialMarkerStaticOptimizationEXT-type-type) `type` **must** be `XR_TYPE_SPATIAL_MARKER_STATIC_OPTIMIZATION_EXT`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#VUID-XrSpatialMarkerStaticOptimizationEXT-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)

## Guaranteed Components

A runtime that supports `XR_SPATIAL_CAPABILITY_MARKER_TRACKING_QR_CODE_EXT` , `XR_SPATIAL_CAPABILITY_MARKER_TRACKING_MICRO_QR_CODE_EXT` , `XR_SPATIAL_CAPABILITY_MARKER_TRACKING_ARUCO_MARKER_EXT` , or `XR_SPATIAL_CAPABILITY_MARKER_TRACKING_APRIL_TAG_EXT` **must** provide the following spatial components as guaranteed components of all entities discovered by those capabilities, and **must** enumerate them in [xrEnumerateSpatialCapabilityComponentTypesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrEnumerateSpatialCapabilityComponentTypesEXT) :

- `XR_SPATIAL_COMPONENT_TYPE_MARKER_EXT`
- `XR_SPATIAL_COMPONENT_TYPE_BOUNDED_2D_EXT`

### Marker Component

###### Component data

The [XrSpatialMarkerDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialMarkerDataEXT) structure is defined as:

    typedef struct XrSpatialMarkerDataEXT {
        XrSpatialCapabilityEXT    capability;
        uint32_t                  markerId;
        XrSpatialBufferEXT        data;
    } XrSpatialMarkerDataEXT;

### Member Descriptions

- `capability` is the [XrSpatialCapabilityEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityEXT) that detected the marker.
- `markerId` is the encoded identifier from the marker. For ArUco markers and AprilTag this field **must** be valid and filled with the encoded ID. For QR codes this field **must** be zero.
- `data` is the buffer ID and type of additional information contained in the marker.

`XR_SPATIAL_CAPABILITY_MARKER_TRACKING_QR_CODE_EXT` and `XR_SPATIAL_CAPABILITY_MARKER_TRACKING_MICRO_QR_CODE_EXT` support extra data. If `capability` is one of these -

- If the runtime has successfully decoded the data for the marker, it **must** set the `data` buffer type to either `XR_SPATIAL_BUFFER_TYPE_UINT8_EXT` or `XR_SPATIAL_BUFFER_TYPE_STRING_EXT` , depending on the data in the marker. The runtime **must** also set a valid buffer ID in `data` which the application **can** use with the appropriate `xrGetSpatialBuffer*` function to get the data.
- If the runtime has not yet decoded the data of the marker, it **must** set `data` buffer ID to [XR_NULL_SPATIAL_BUFFER_ID_EXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_NULL_SPATIAL_BUFFER_ID_EXT) and the buffer type to `XR_SPATIAL_BUFFER_TYPE_UNKNOWN_EXT` .

`XR_SPATIAL_CAPABILITY_MARKER_TRACKING_ARUCO_MARKER_EXT` and `XR_SPATIAL_CAPABILITY_MARKER_TRACKING_APRIL_TAG_EXT` do not support extra data and the runtime **must** set the buffer ID of `data` to [XR_NULL_SPATIAL_BUFFER_ID_EXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_NULL_SPATIAL_BUFFER_ID_EXT) .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#VUID-XrSpatialMarkerDataEXT-extension-notenabled) The `XR_EXT_spatial_marker_tracking` extension **must** be enabled prior to using [XrSpatialMarkerDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialMarkerDataEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#VUID-XrSpatialMarkerDataEXT-capability-parameter) `capability` **must** be a valid [XrSpatialCapabilityEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityEXT) value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#VUID-XrSpatialMarkerDataEXT-data-parameter) `data` **must** be a valid [XrSpatialBufferEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialBufferEXT) structure

###### Component list structure to query data

The [XrSpatialComponentMarkerListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialComponentMarkerListEXT) structure is defined as:

    typedef struct XrSpatialComponentMarkerListEXT {
        XrStructureType            type;
        void*                      next;
        uint32_t                   markerCount;
        XrSpatialMarkerDataEXT*    markers;
    } XrSpatialComponentMarkerListEXT;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.
- `markerCount` is the number of elements in the `markers` member.
- `markers` is an array of [XrSpatialMarkerDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialMarkerDataEXT) .

The application **can** query the marker component of the spatial entities in an [XrSpatialSnapshotEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialSnapshotEXT) by adding `XR_SPATIAL_COMPONENT_TYPE_MARKER_EXT` in [XrSpatialComponentDataQueryConditionEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryConditionEXT) :: `componentTypes` and adding [XrSpatialComponentMarkerListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialComponentMarkerListEXT) to the next pointer chain of [XrSpatialComponentDataQueryResultEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryResultEXT) .

The runtime **must** return `XR_ERROR_VALIDATION_FAILURE` from [xrQuerySpatialComponentDataEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrQuerySpatialComponentDataEXT) if [XrSpatialComponentMarkerListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialComponentMarkerListEXT) is in the next chain of [XrSpatialComponentDataQueryResultEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryResultEXT) :: `next` but `XR_SPATIAL_COMPONENT_TYPE_MARKER_EXT` is not included in [XrSpatialComponentDataQueryConditionEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryConditionEXT) :: `componentTypes` .

The runtime **must** return `XR_ERROR_SIZE_INSUFFICIENT` from [xrQuerySpatialComponentDataEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrQuerySpatialComponentDataEXT) if `markerCount` is less than [XrSpatialComponentDataQueryResultEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryResultEXT) :: `entityIdCountOutput` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#VUID-XrSpatialComponentMarkerListEXT-extension-notenabled) The `XR_EXT_spatial_marker_tracking` extension **must** be enabled prior to using [XrSpatialComponentMarkerListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialComponentMarkerListEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#VUID-XrSpatialComponentMarkerListEXT-type-type) `type` **must** be `XR_TYPE_SPATIAL_COMPONENT_MARKER_LIST_EXT`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#VUID-XrSpatialComponentMarkerListEXT-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#VUID-XrSpatialComponentMarkerListEXT-markers-parameter) `markers` **must** be a pointer to an array of `markerCount` [XrSpatialMarkerDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialMarkerDataEXT) structures
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#VUID-XrSpatialComponentMarkerListEXT-markerCount-arraylength) The `markerCount` parameter **must** be greater than `0`

###### Configuration

If `XR_SPATIAL_COMPONENT_TYPE_MARKER_EXT` is enumerated in [XrSpatialCapabilityComponentTypesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityComponentTypesEXT) :: `componentTypes` for some capability, an application **can** enable it by including the enumerant in the [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityConfigurationBaseHeaderEXT) :: `enabledComponents` list of the [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityConfigurationBaseHeaderEXT) derived structure of the capability that supports this component.

This component does not require any special configuration to be included in the [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityConfigurationBaseHeaderEXT) :: `next` chain.

### Bounded 2D Component

The bounded 2D component provides the center and extents of the marker represented by the entity it is on. See [Bounded 2D](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#ext_spatial_entity_bounded2D_component) for more details about the bounded 2D component.

The [XrSpatialBounded2DDataEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialBounded2DDataEXT) :: `center` **must** point to the center of the marker. When looking at the front face of the marker, the X-axis **must** point to the right, and the Y-axis **must** point to the top of the marker. The runtime **must** follow the right-handed coordinate system convention thus the Z-axis comes out of the front face of the marker. This means that a marker with a position of {0, 0, 0}, rotation of {0, 0, 0, 1} (no rotation), and an extent of {1, 1} refers to a 1 meter x 1 meter marker centered at {0, 0, 0} with its front face normal vector pointing towards the +Z direction in the component's space.

A representation of the orientation of the marker is shown below.

![xr ml marker understanding axis](data:image/png;base64,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)

### Figure 25. QR code marker with axis

## Test Codes

The following codes **must** have their X-Y plane inside the document and the Z-axis pointing at the viewer. The axis origin **must** appear at the center of each marker. The X-axis **must** point to the right, the Y-axis **must** point to the top of the document.

![ext marker tracking qr](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjxzdmcKICAgeG1sbnM6ZGM9Imh0dHA6Ly9wdXJsLm9yZy9kYy9lbGVtZW50cy8xLjEvIgogICB4bWxuczpjYz0iaHR0cDovL2NyZWF0aXZlY29tbW9ucy5vcmcvbnMjIgogICB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiCiAgIHhtbG5zOnN2Zz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiAgIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIKICAgeG1sbnM6c29kaXBvZGk9Imh0dHA6Ly9zb2RpcG9kaS5zb3VyY2Vmb3JnZS5uZXQvRFREL3NvZGlwb2RpLTAuZHRkIgogICB4bWxuczppbmtzY2FwZT0iaHR0cDovL3d3dy5pbmtzY2FwZS5vcmcvbmFtZXNwYWNlcy9pbmtzY2FwZSIKICAgdmVyc2lvbj0iMS4xIgogICBpZD0iTGF5ZXJfMSIKICAgeD0iMHB4IgogICB5PSIwcHgiCiAgIHdpZHRoPSIxMDBtbSIKICAgaGVpZ2h0PSIxMDRtbSIKICAgdmlld0JveD0iMCAwIDM3Ny45NTI3NiAzOTMuMDcwODgiCiAgIGVuYWJsZS1iYWNrZ3JvdW5kPSJuZXcgMCAwIDYwMCA2MDAiCiAgIHhtbDpzcGFjZT0icHJlc2VydmUiCiAgIHNvZGlwb2RpOmRvY25hbWU9ImV4dF9tYXJrZXJfdHJhY2tpbmdfcXIuc3ZnIgogICBpbmtzY2FwZTp2ZXJzaW9uPSIwLjkyLjUgKDIwNjBlYzFmOWYsIDIwMjAtMDQtMDgpIj48bWV0YWRhdGEKICAgaWQ9Im1ldGFkYXRhMzU1NSI+PHJkZjpSREY+PGNjOldvcmsKICAgICAgIHJkZjphYm91dD0iIj48ZGM6Zm9ybWF0PmltYWdlL3N2Zyt4bWw8L2RjOmZvcm1hdD48ZGM6dHlwZQogICAgICAgICByZGY6cmVzb3VyY2U9Imh0dHA6Ly9wdXJsLm9yZy9kYy9kY21pdHlwZS9TdGlsbEltYWdlIiAvPjxkYzp0aXRsZT48L2RjOnRpdGxlPjwvY2M6V29yaz48L3JkZjpSREY+PC9tZXRhZGF0YT48ZGVmcwogICBpZD0iZGVmczM1NTMiIC8+PHNvZGlwb2RpOm5hbWVkdmlldwogICBwYWdlY29sb3I9IiNmZmZmZmYiCiAgIGJvcmRlcmNvbG9yPSIjNjY2NjY2IgogICBib3JkZXJvcGFjaXR5PSIxIgogICBvYmplY3R0b2xlcmFuY2U9IjEwIgogICBncmlkdG9sZXJhbmNlPSIxMCIKICAgZ3VpZGV0b2xlcmFuY2U9IjEwIgogICBpbmtzY2FwZTpwYWdlb3BhY2l0eT0iMCIKICAgaW5rc2NhcGU6cGFnZXNoYWRvdz0iMiIKICAgaW5rc2NhcGU6d2luZG93LXdpZHRoPSIzODQwIgogICBpbmtzY2FwZTp3aW5kb3ctaGVpZ2h0PSIyMDEzIgogICBpZD0ibmFtZWR2aWV3MzU1MSIKICAgc2hvd2dyaWQ9ImZhbHNlIgogICB1bml0cz0ibW0iCiAgIGlua3NjYXBlOnpvb209IjIuODI4NDI3MSIKICAgaW5rc2NhcGU6Y3g9IjM4MS42MjQ5MSIKICAgaW5rc2NhcGU6Y3k9IjEwNi44NDIyOCIKICAgaW5rc2NhcGU6d2luZG93LXg9IjM4NDAiCiAgIGlua3NjYXBlOndpbmRvdy15PSIwIgogICBpbmtzY2FwZTp3aW5kb3ctbWF4aW1pemVkPSIxIgogICBpbmtzY2FwZTpjdXJyZW50LWxheWVyPSJMYXllcl8xIiAvPgo8ZwogICB0cmFuc2Zvcm09Im1hdHJpeCgwLjc0ODc1MjYxLDAsMCwwLjc0ODc1MjYxLDAuNjUyMTMwMTcsOS4wMzcwMTcxKSIKICAgaWQ9ImczNTQ4Ij48ZwogICAgIHRyYW5zZm9ybT0ibWF0cml4KDAuMjQsMCwwLDAuMjQsMjQwLDApIgogICAgIGlkPSJnMjc5MCI+PGcKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDAiCiAgICAgICBpZD0iZzI3ODgiPgo8cmVjdAogICB3aWR0aD0iMTAwIgogICBoZWlnaHQ9IjEwMCIKICAgaWQ9InJlY3QyNzg2IgogICB4PSIwIgogICB5PSIwIiAvPgo8L2c+PC9nPjxnCiAgICAgdHJhbnNmb3JtPSJtYXRyaXgoMC4yNCwwLDAsMC4yNCwyNjQsMCkiCiAgICAgaWQ9ImcyNzk2Ij48ZwogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMCIKICAgICAgIGlkPSJnMjc5NCI+CjxyZWN0CiAgIHdpZHRoPSIxMDAiCiAgIGhlaWdodD0iMTAwIgogICBpZD0icmVjdDI3OTIiCiAgIHg9IjAiCiAgIHk9IjAiIC8+CjwvZz48L2c+PGcKICAgICB0cmFuc2Zvcm09Im1hdHJpeCgwLjI0LDAsMCwwLjI0LDE5MiwyNCkiCiAgICAgaWQ9ImcyODAyIj48ZwogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMCIKICAgICAgIGlkPSJnMjgwMCI+CjxyZWN0CiAgIHdpZHRoPSIxMDAiCiAgIGhlaWdodD0iMTAwIgogICBpZD0icmVjdDI3OTgiCiAgIHg9IjAiCiAgIHk9IjAiIC8+CjwvZz48L2c+PGcKICAgICB0cmFuc2Zvcm09Im1hdHJpeCgwLjI0LDAsMCwwLjI0LDIxNiwyNCkiCiAgICAgaWQ9ImcyODA4Ij48ZwogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMCIKICAgICAgIGlkPSJnMjgwNiI+CjxyZWN0CiAgIHdpZHRoPSIxMDAiCiAgIGhlaWdodD0iMTAwIgogICBpZD0icmVjdDI4MDQiCiAgIHg9IjAiCiAgIHk9IjAiIC8+CjwvZz48L2c+PGcKICAgICB0cmFuc2Zvcm09Im1hdHJpeCgwLjI0LDAsMCwwLjI0LDI2NCwyNCkiCiAgICAgaWQ9ImcyODE0Ij48ZwogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMCIKICAgICAgIGlkPSJnMjgxMiI+CjxyZWN0CiAgIHdpZHRoPSIxMDAiCiAgIGhlaWdodD0iMTAwIgogICBpZD0icmVjdDI4MTAiCiAgIHg9IjAiCiAgIHk9IjAiIC8+CjwvZz48L2c+PGcKICAgICB0cmFuc2Zvcm09Im1hdHJpeCgwLjI0LDAsMCwwLjI0LDI4OCwyNCkiCiAgICAgaWQ9ImcyODIwIj48ZwogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMCIKICAgICAgIGlkPSJnMjgxOCI+CjxyZWN0CiAgIHdpZHRoPSIxMDAiCiAgIGhlaWdodD0iMTAwIgogICBpZD0icmVjdDI4MTYiCiAgIHg9IjAiCiAgIHk9IjAiIC8+CjwvZz48L2c+PGcKICAgICB0cmFuc2Zvcm09Im1hdHJpeCgwLjI0LDAsMCwwLjI0LDE5Miw0OCkiCiAgICAgaWQ9ImcyODI2Ij48ZwogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMCIKICAgICAgIGlkPSJnMjgyNCI+CjxyZWN0CiAgIHdpZHRoPSIxMDAiCiAgIGhlaWdodD0iMTAwIgogICBpZD0icmVjdDI4MjIiCiAgIHg9IjAiCiAgIHk9IjAiIC8+CjwvZz48L2c+PGcKICAgICB0cmFuc2Zvcm09Im1hdHJpeCgwLjI0LDAsMCwwLjI0LDI0MCw0OCkiCiAgICAgaWQ9ImcyODMyIj48ZwogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMCIKICAgICAgIGlkPSJnMjgzMCI+CjxyZWN0CiAgIHdpZHRoPSIxMDAiCiAgIGhlaWdodD0iMTAwIgogICBpZD0icmVjdDI4MjgiCiAgIHg9IjAiCiAgIHk9IjAiIC8+CjwvZz48L2c+PGcKICAgICB0cmFuc2Zvcm09Im1hdHJpeCgwLjI0LDAsMCwwLjI0LDE5Miw3MikiCiAgICAgaWQ9ImcyODM4Ij48ZwogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMCIKICAgICAgIGlkPSJnMjgzNiI+CjxyZWN0CiAgIHdpZHRoPSIxMDAiCiAgIGhlaWdodD0iMTAwIgogICBpZD0icmVjdDI4MzQiCiAgIHg9IjAiCiAgIHk9IjAiIC8+CjwvZz48L2c+PGcKICAgICB0cmFuc2Zvcm09Im1hdHJpeCgwLjI0LDAsMCwwLjI0LDIxNiw3MikiCiAgICAgaWQ9ImcyODQ0Ij48ZwogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMCIKICAgICAgIGlkPSJnMjg0MiI+CjxyZWN0CiAgIHdpZHRoPSIxMDAiCiAgIGhlaWdodD0iMTAwIgogICBpZD0icmVjdDI4NDAiCiAgIHg9IjAiCiAgIHk9IjAiIC8+CjwvZz48L2c+PGcKICAgICB0cmFuc2Zvcm09Im1hdHJpeCgwLjI0LDAsMCwwLjI0LDI0MCw3MikiCiAgICAgaWQ9ImcyODUwIj48ZwogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMCIKICAgICAgIGlkPSJnMjg0OCI+CjxyZWN0CiAgIHdpZHRoPSIxMDAiCiAgIGhlaWdodD0iMTAwIgogICBpZD0icmVjdDI4NDYiCiAgIHg9IjAiCiAgIHk9IjAiIC8+CjwvZz48L2c+PGcKICAgICB0cmFuc2Zvcm09Im1hdHJpeCgwLjI0LDAsMCwwLjI0LDI2NCw3MikiCiAgICAgaWQ9ImcyODU2Ij48ZwogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMCIKICAgICAgIGlkPSJnMjg1NCI+CjxyZWN0CiAgIHdpZHRoPSIxMDAiCiAgIGhlaWdodD0iMTAwIgogICBpZD0icmVjdDI4NTIiCiAgIHg9IjAiCiAgIHk9IjAiIC8+CjwvZz48L2c+PGcKICAgICB0cmFuc2Zvcm09Im1hdHJpeCgwLjI0LDAsMCwwLjI0LDI4OCw3MikiCiAgICAgaWQ9ImcyODYyIj48ZwogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMCIKICAgICAgIGlkPSJnMjg2MCI+CjxyZWN0CiAgIHdpZHRoPSIxMDAiCiAgIGhlaWdodD0iMTAwIgogICBpZD0icmVjdDI4NTgiCiAgIHg9IjAiCiAgIHk9IjAiIC8+CjwvZz48L2c+PGcKICAgICB0cmFuc2Zvcm09Im1hdHJpeCgwLjI0LDAsMCwwLjI0LDIxNiw5NikiCiAgICAgaWQ9ImcyODY4Ij48ZwogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMCIKICAgICAgIGlkPSJnMjg2NiI+CjxyZWN0CiAgIHdpZHRoPSIxMDAiCiAgIGhlaWdodD0iMTAwIgogICBpZD0icmVjdDI4NjQiCiAgIHg9IjAiCiAgIHk9IjAiIC8+CjwvZz48L2c+PGcKICAgICB0cmFuc2Zvcm09Im1hdHJpeCgwLjI0LDAsMCwwLjI0LDI2NCw5NikiCiAgICAgaWQ9ImcyODc0Ij48ZwogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMCIKICAgICAgIGlkPSJnMjg3MiI+CjxyZWN0CiAgIHdpZHRoPSIxMDAiCiAgIGhlaWdodD0iMTAwIgogICBpZD0icmVjdDI4NzAiCiAgIHg9IjAiCiAgIHk9IjAiIC8+CjwvZz48L2c+PGcKICAgICB0cmFuc2Zvcm09Im1hdHJpeCgwLjI0LDAsMCwwLjI0LDI4OCw5NikiCiAgICAgaWQ9ImcyODgwIj48ZwogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMCIKICAgICAgIGlkPSJnMjg3OCI+CjxyZWN0CiAgIHdpZHRoPSIxMDAiCiAgIGhlaWdodD0iMTAwIgogICBpZD0icmVjdDI4NzYiCiAgIHg9IjAiCiAgIHk9IjAiIC8+CjwvZz48L2c+PGcKICAgICB0cmFuc2Zvcm09Im1hdHJpeCgwLjI0LDAsMCwwLjI0LDIxNiwxMjApIgogICAgIGlkPSJnMjg4NiI+PGcKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDAiCiAgICAgICBpZD0iZzI4ODQiPgo8cmVjdAogICB3aWR0aD0iMTAwIgogICBoZWlnaHQ9IjEwMCIKICAgaWQ9InJlY3QyODgyIgogICB4PSIwIgogICB5PSIwIiAvPgo8L2c+PC9nPjxnCiAgICAgdHJhbnNmb3JtPSJtYXRyaXgoMC4yNCwwLDAsMC4yNCwyODgsMTIwKSIKICAgICBpZD0iZzI4OTIiPjxnCiAgICAgICBzdHlsZT0iZmlsbDojMDAwMDAwIgogICAgICAgaWQ9ImcyODkwIj4KPHJlY3QKICAgd2lkdGg9IjEwMCIKICAgaGVpZ2h0PSIxMDAiCiAgIGlkPSJyZWN0Mjg4OCIKICAgeD0iMCIKICAgeT0iMCIgLz4KPC9nPjwvZz48ZwogICAgIHRyYW5zZm9ybT0ibWF0cml4KDAuMjQsMCwwLDAuMjQsMTkyLDE0NCkiCiAgICAgaWQ9ImcyODk4Ij48ZwogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMCIKICAgICAgIGlkPSJnMjg5NiI+CjxyZWN0CiAgIHdpZHRoPSIxMDAiCiAgIGhlaWdodD0iMTAwIgogICBpZD0icmVjdDI4OTQiCiAgIHg9IjAiCiAgIHk9IjAiIC8+CjwvZz48L2c+PGcKICAgICB0cmFuc2Zvcm09Im1hdHJpeCgwLjI0LDAsMCwwLjI0LDI0MCwxNDQpIgogICAgIGlkPSJnMjkwNCI+PGcKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDAiCiAgICAgICBpZD0iZzI5MDIiPgo8cmVjdAogICB3aWR0aD0iMTAwIgogICBoZWlnaHQ9IjEwMCIKICAgaWQ9InJlY3QyOTAwIgogICB4PSIwIgogICB5PSIwIiAvPgo8L2c+PC9nPjxnCiAgICAgdHJhbnNmb3JtPSJtYXRyaXgoMC4yNCwwLDAsMC4yNCwyODgsMTQ0KSIKICAgICBpZD0iZzI5MTAiPjxnCiAgICAgICBzdHlsZT0iZmlsbDojMDAwMDAwIgogICAgICAgaWQ9ImcyOTA4Ij4KPHJlY3QKICAgd2lkdGg9IjEwMCIKICAgaGVpZ2h0PSIxMDAiCiAgIGlkPSJyZWN0MjkwNiIKICAgeD0iMCIKICAgeT0iMCIgLz4KPC9nPjwvZz48ZwogICAgIHRyYW5zZm9ybT0ibWF0cml4KDAuMjQsMCwwLDAuMjQsMTkyLDE2OCkiCiAgICAgaWQ9ImcyOTE2Ij48ZwogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMCIKICAgICAgIGlkPSJnMjkxNCI+CjxyZWN0CiAgIHdpZHRoPSIxMDAiCiAgIGhlaWdodD0iMTAwIgogICBpZD0icmVjdDI5MTIiCiAgIHg9IjAiCiAgIHk9IjAiIC8+CjwvZz48L2c+PGcKICAgICB0cmFuc2Zvcm09Im1hdHJpeCgwLjI0LDAsMCwwLjI0LDI2NCwxNjgpIgogICAgIGlkPSJnMjkyMiI+PGcKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDAiCiAgICAgICBpZD0iZzI5MjAiPgo8cmVjdAogICB3aWR0aD0iMTAwIgogICBoZWlnaHQ9IjEwMCIKICAgaWQ9InJlY3QyOTE4IgogICB4PSIwIgogICB5PSIwIiAvPgo8L2c+PC9nPjxnCiAgICAgdHJhbnNmb3JtPSJtYXRyaXgoMC4yNCwwLDAsMC4yNCwyODgsMTY4KSIKICAgICBpZD0iZzI5MjgiPjxnCiAgICAgICBzdHlsZT0iZmlsbDojMDAwMDAwIgogICAgICAgaWQ9ImcyOTI2Ij4KPHJlY3QKICAgd2lkdGg9IjEwMCIKICAgaGVpZ2h0PSIxMDAiCiAgIGlkPSJyZWN0MjkyNCIKICAgeD0iMCIKICAgeT0iMCIgLz4KPC9nPjwvZz48ZwogICAgIHRyYW5zZm9ybT0ibWF0cml4KDAuMjQsMCwwLDAuMjQsMCwxOTIpIgogICAgIGlkPSJnMjkzNCI+PGcKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDAiCiAgICAgICBpZD0iZzI5MzIiPgo8cmVjdAogICB3aWR0aD0iMTAwIgogICBoZWlnaHQ9IjEwMCIKICAgaWQ9InJlY3QyOTMwIgogICB4PSIwIgogICB5PSIwIiAvPgo8L2c+PC9nPjxnCiAgICAgdHJhbnNmb3JtPSJtYXRyaXgoMC4yNCwwLDAsMC4yNCwxNDQsMTkyKSIKICAgICBpZD0iZzI5NDAiPjxnCiAgICAgICBzdHlsZT0iZmlsbDojMDAwMDAwIgogICAgICAgaWQ9ImcyOTM4Ij4KPHJlY3QKICAgd2lkdGg9IjEwMCIKICAgaGVpZ2h0PSIxMDAiCiAgIGlkPSJyZWN0MjkzNiIKICAgeD0iMCIKICAgeT0iMCIgLz4KPC9nPjwvZz48ZwogICAgIHRyYW5zZm9ybT0ibWF0cml4KDAuMjQsMCwwLDAuMjQsMTkyLDE5MikiCiAgICAgaWQ9ImcyOTQ2Ij48ZwogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMCIKICAgICAgIGlkPSJnMjk0NCI+CjxyZWN0CiAgIHdpZHRoPSIxMDAiCiAgIGhlaWdodD0iMTAwIgogICBpZD0icmVjdDI5NDIiCiAgIHg9IjAiCiAgIHk9IjAiIC8+CjwvZz48L2c+PGcKICAgICB0cmFuc2Zvcm09Im1hdHJpeCgwLjI0LDAsMCwwLjI0LDI0MCwxOTIpIgogICAgIGlkPSJnMjk1MiI+PGcKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDAiCiAgICAgICBpZD0iZzI5NTAiPgo8cmVjdAogICB3aWR0aD0iMTAwIgogICBoZWlnaHQ9IjEwMCIKICAgaWQ9InJlY3QyOTQ4IgogICB4PSIwIgogICB5PSIwIiAvPgo8L2c+PC9nPjxnCiAgICAgdHJhbnNmb3JtPSJtYXRyaXgoMC4yNCwwLDAsMC4yNCwyODgsMTkyKSIKICAgICBpZD0iZzI5NTgiPjxnCiAgICAgICBzdHlsZT0iZmlsbDojMDAwMDAwIgogICAgICAgaWQ9ImcyOTU2Ij4KPHJlY3QKICAgd2lkdGg9IjEwMCIKICAgaGVpZ2h0PSIxMDAiCiAgIGlkPSJyZWN0Mjk1NCIKICAgeD0iMCIKICAgeT0iMCIgLz4KPC9nPjwvZz48ZwogICAgIHRyYW5zZm9ybT0ibWF0cml4KDAuMjQsMCwwLDAuMjQsMzEyLDE5MikiCiAgICAgaWQ9ImcyOTY0Ij48ZwogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMCIKICAgICAgIGlkPSJnMjk2MiI+CjxyZWN0CiAgIHdpZHRoPSIxMDAiCiAgIGhlaWdodD0iMTAwIgogICBpZD0icmVjdDI5NjAiCiAgIHg9IjAiCiAgIHk9IjAiIC8+CjwvZz48L2c+PGcKICAgICB0cmFuc2Zvcm09Im1hdHJpeCgwLjI0LDAsMCwwLjI0LDMzNiwxOTIpIgogICAgIGlkPSJnMjk3MCI+PGcKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDAiCiAgICAgICBpZD0iZzI5NjgiPgo8cmVjdAogICB3aWR0aD0iMTAwIgogICBoZWlnaHQ9IjEwMCIKICAgaWQ9InJlY3QyOTY2IgogICB4PSIwIgogICB5PSIwIiAvPgo8L2c+PC9nPjxnCiAgICAgdHJhbnNmb3JtPSJtYXRyaXgoMC4yNCwwLDAsMC4yNCw0MDgsMTkyKSIKICAgICBpZD0iZzI5NzYiPjxnCiAgICAgICBzdHlsZT0iZmlsbDojMDAwMDAwIgogICAgICAgaWQ9ImcyOTc0Ij4KPHJlY3QKICAgd2lkdGg9IjEwMCIKICAgaGVpZ2h0PSIxMDAiCiAgIGlkPSJyZWN0Mjk3MiIKICAgeD0iMCIKICAgeT0iMCIgLz4KPC9nPjwvZz48ZwogICAgIHRyYW5zZm9ybT0ibWF0cml4KDAuMjQsMCwwLDAuMjQsNDMyLDE5MikiCiAgICAgaWQ9ImcyOTgyIj48ZwogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMCIKICAgICAgIGlkPSJnMjk4MCI+CjxyZWN0CiAgIHdpZHRoPSIxMDAiCiAgIGhlaWdodD0iMTAwIgogICBpZD0icmVjdDI5NzgiCiAgIHg9IjAiCiAgIHk9IjAiIC8+CjwvZz48L2c+PGcKICAgICB0cmFuc2Zvcm09Im1hdHJpeCgwLjI0LDAsMCwwLjI0LDQ1NiwxOTIpIgogICAgIGlkPSJnMjk4OCI+PGcKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDAiCiAgICAgICBpZD0iZzI5ODYiPgo8cmVjdAogICB3aWR0aD0iMTAwIgogICBoZWlnaHQ9IjEwMCIKICAgaWQ9InJlY3QyOTg0IgogICB4PSIwIgogICB5PSIwIiAvPgo8L2c+PC9nPjxnCiAgICAgdHJhbnNmb3JtPSJtYXRyaXgoMC4yNCwwLDAsMC4yNCw5NiwyMTYpIgogICAgIGlkPSJnMjk5NCI+PGcKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDAiCiAgICAgICBpZD0iZzI5OTIiPgo8cmVjdAogICB3aWR0aD0iMTAwIgogICBoZWlnaHQ9IjEwMCIKICAgaWQ9InJlY3QyOTkwIgogICB4PSIwIgogICB5PSIwIiAvPgo8L2c+PC9nPjxnCiAgICAgdHJhbnNmb3JtPSJtYXRyaXgoMC4yNCwwLDAsMC4yNCwxMjAsMjE2KSIKICAgICBpZD0iZzMwMDAiPjxnCiAgICAgICBzdHlsZT0iZmlsbDojMDAwMDAwIgogICAgICAgaWQ9ImcyOTk4Ij4KPHJlY3QKICAgd2lkdGg9IjEwMCIKICAgaGVpZ2h0PSIxMDAiCiAgIGlkPSJyZWN0Mjk5NiIKICAgeD0iMCIKICAgeT0iMCIgLz4KPC9nPjwvZz48ZwogICAgIHRyYW5zZm9ybT0ibWF0cml4KDAuMjQsMCwwLDAuMjQsMTY4LDIxNikiCiAgICAgaWQ9ImczMDA2Ij48ZwogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMCIKICAgICAgIGlkPSJnMzAwNCI+CjxyZWN0CiAgIHdpZHRoPSIxMDAiCiAgIGhlaWdodD0iMTAwIgogICBpZD0icmVjdDMwMDIiCiAgIHg9IjAiCiAgIHk9IjAiIC8+CjwvZz48L2c+PGcKICAgICB0cmFuc2Zvcm09Im1hdHJpeCgwLjI0LDAsMCwwLjI0LDE5MiwyMTYpIgogICAgIGlkPSJnMzAxMiI+PGcKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDAiCiAgICAgICBpZD0iZzMwMTAiPgo8cmVjdAogICB3aWR0aD0iMTAwIgogICBoZWlnaHQ9IjEwMCIKICAgaWQ9InJlY3QzMDA4IgogICB4PSIwIgogICB5PSIwIiAvPgo8L2c+PC9nPjxnCiAgICAgdHJhbnNmb3JtPSJtYXRyaXgoMC4yNCwwLDAsMC4yNCwyMTYsMjE2KSIKICAgICBpZD0iZzMwMTgiPjxnCiAgICAgICBzdHlsZT0iZmlsbDojMDAwMDAwIgogICAgICAgaWQ9ImczMDE2Ij4KPHJlY3QKICAgd2lkdGg9IjEwMCIKICAgaGVpZ2h0PSIxMDAiCiAgIGlkPSJyZWN0MzAxNCIKICAgeD0iMCIKICAgeT0iMCIgLz4KPC9nPjwvZz48ZwogICAgIHRyYW5zZm9ybT0ibWF0cml4KDAuMjQsMCwwLDAuMjQsMjQwLDIxNikiCiAgICAgaWQ9ImczMDI0Ij48ZwogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMCIKICAgICAgIGlkPSJnMzAyMiI+CjxyZWN0CiAgIHdpZHRoPSIxMDAiCiAgIGhlaWdodD0iMTAwIgogICBpZD0icmVjdDMwMjAiCiAgIHg9IjAiCiAgIHk9IjAiIC8+CjwvZz48L2c+PGcKICAgICB0cmFuc2Zvcm09Im1hdHJpeCgwLjI0LDAsMCwwLjI0LDI4OCwyMTYpIgogICAgIGlkPSJnMzAzMCI+PGcKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDAiCiAgICAgICBpZD0iZzMwMjgiPgo8cmVjdAogICB3aWR0aD0iMTAwIgogICBoZWlnaHQ9IjEwMCIKICAgaWQ9InJlY3QzMDI2IgogICB4PSIwIgogICB5PSIwIiAvPgo8L2c+PC9nPjxnCiAgICAgdHJhbnNmb3JtPSJtYXRyaXgoMC4yNCwwLDAsMC4yNCwzMzYsMjE2KSIKICAgICBpZD0iZzMwMzYiPjxnCiAgICAgICBzdHlsZT0iZmlsbDojMDAwMDAwIgogICAgICAgaWQ9ImczMDM0Ij4KPHJlY3QKICAgd2lkdGg9IjEwMCIKICAgaGVpZ2h0PSIxMDAiCiAgIGlkPSJyZWN0MzAzMiIKICAgeD0iMCIKICAgeT0iMCIgLz4KPC9nPjwvZz48ZwogICAgIHRyYW5zZm9ybT0ibWF0cml4KDAuMjQsMCwwLDAuMjQsMzg0LDIxNikiCiAgICAgaWQ9ImczMDQyIj48ZwogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMCIKICAgICAgIGlkPSJnMzA0MCI+CjxyZWN0CiAgIHdpZHRoPSIxMDAiCiAgIGhlaWdodD0iMTAwIgogICBpZD0icmVjdDMwMzgiCiAgIHg9IjAiCiAgIHk9IjAiIC8+CjwvZz48L2c+PGcKICAgICB0cmFuc2Zvcm09Im1hdHJpeCgwLjI0LDAsMCwwLjI0LDQzMiwyMTYpIgogICAgIGlkPSJnMzA0OCI+PGcKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDAiCiAgICAgICBpZD0iZzMwNDYiPgo8cmVjdAogICB3aWR0aD0iMTAwIgogICBoZWlnaHQ9IjEwMCIKICAgaWQ9InJlY3QzMDQ0IgogICB4PSIwIgogICB5PSIwIiAvPgo8L2c+PC9nPjxnCiAgICAgdHJhbnNmb3JtPSJtYXRyaXgoMC4yNCwwLDAsMC4yNCw0NTYsMjE2KSIKICAgICBpZD0iZzMwNTQiPjxnCiAgICAgICBzdHlsZT0iZmlsbDojMDAwMDAwIgogICAgICAgaWQ9ImczMDUyIj4KPHJlY3QKICAgd2lkdGg9IjEwMCIKICAgaGVpZ2h0PSIxMDAiCiAgIGlkPSJyZWN0MzA1MCIKICAgeD0iMCIKICAgeT0iMCIgLz4KPC9nPjwvZz48ZwogICAgIHRyYW5zZm9ybT0ibWF0cml4KDAuMjQsMCwwLDAuMjQsMjQsMjQwKSIKICAgICBpZD0iZzMwNjAiPjxnCiAgICAgICBzdHlsZT0iZmlsbDojMDAwMDAwIgogICAgICAgaWQ9ImczMDU4Ij4KPHJlY3QKICAgd2lkdGg9IjEwMCIKICAgaGVpZ2h0PSIxMDAiCiAgIGlkPSJyZWN0MzA1NiIKICAgeD0iMCIKICAgeT0iMCIgLz4KPC9nPjwvZz48ZwogICAgIHRyYW5zZm9ybT0ibWF0cml4KDAuMjQsMCwwLDAuMjQsNzIsMjQwKSIKICAgICBpZD0iZzMwNjYiPjxnCiAgICAgICBzdHlsZT0iZmlsbDojMDAwMDAwIgogICAgICAgaWQ9ImczMDY0Ij4KPHJlY3QKICAgd2lkdGg9IjEwMCIKICAgaGVpZ2h0PSIxMDAiCiAgIGlkPSJyZWN0MzA2MiIKICAgeD0iMCIKICAgeT0iMCIgLz4KPC9nPjwvZz48ZwogICAgIHRyYW5zZm9ybT0ibWF0cml4KDAuMjQsMCwwLDAuMjQsMTQ0LDI0MCkiCiAgICAgaWQ9ImczMDcyIj48ZwogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMCIKICAgICAgIGlkPSJnMzA3MCI+CjxyZWN0CiAgIHdpZHRoPSIxMDAiCiAgIGhlaWdodD0iMTAwIgogICBpZD0icmVjdDMwNjgiCiAgIHg9IjAiCiAgIHk9IjAiIC8+CjwvZz48L2c+PGcKICAgICB0cmFuc2Zvcm09Im1hdHJpeCgwLjI0LDAsMCwwLjI0LDE5MiwyNDApIgogICAgIGlkPSJnMzA3OCI+PGcKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDAiCiAgICAgICBpZD0iZzMwNzYiPgo8cmVjdAogICB3aWR0aD0iMTAwIgogICBoZWlnaHQ9IjEwMCIKICAgaWQ9InJlY3QzMDc0IgogICB4PSIwIgogICB5PSIwIiAvPgo8L2c+PC9nPjxnCiAgICAgdHJhbnNmb3JtPSJtYXRyaXgoMC4yNCwwLDAsMC4yNCwyNDAsMjQwKSIKICAgICBpZD0iZzMwODQiPjxnCiAgICAgICBzdHlsZT0iZmlsbDojMDAwMDAwIgogICAgICAgaWQ9ImczMDgyIj4KPHJlY3QKICAgd2lkdGg9IjEwMCIKICAgaGVpZ2h0PSIxMDAiCiAgIGlkPSJyZWN0MzA4MCIKICAgeD0iMCIKICAgeT0iMCIgLz4KPC9nPjwvZz48ZwogICAgIHRyYW5zZm9ybT0ibWF0cml4KDAuMjQsMCwwLDAuMjQsMjY0LDI0MCkiCiAgICAgaWQ9ImczMDkwIj48ZwogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMCIKICAgICAgIGlkPSJnMzA4OCI+CjxyZWN0CiAgIHdpZHRoPSIxMDAiCiAgIGhlaWdodD0iMTAwIgogICBpZD0icmVjdDMwODYiCiAgIHg9IjAiCiAgIHk9IjAiIC8+CjwvZz48L2c+PGcKICAgICB0cmFuc2Zvcm09Im1hdHJpeCgwLjI0LDAsMCwwLjI0LDMxMiwyNDApIgogICAgIGlkPSJnMzA5NiI+PGcKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDAiCiAgICAgICBpZD0iZzMwOTQiPgo8cmVjdAogICB3aWR0aD0iMTAwIgogICBoZWlnaHQ9IjEwMCIKICAgaWQ9InJlY3QzMDkyIgogICB4PSIwIgogICB5PSIwIiAvPgo8L2c+PC9nPjxnCiAgICAgdHJhbnNmb3JtPSJtYXRyaXgoMC4yNCwwLDAsMC4yNCwzODQsMjQwKSIKICAgICBpZD0iZzMxMDIiPjxnCiAgICAgICBzdHlsZT0iZmlsbDojMDAwMDAwIgogICAgICAgaWQ9ImczMTAwIj4KPHJlY3QKICAgd2lkdGg9IjEwMCIKICAgaGVpZ2h0PSIxMDAiCiAgIGlkPSJyZWN0MzA5OCIKICAgeD0iMCIKICAgeT0iMCIgLz4KPC9nPjwvZz48ZwogICAgIHRyYW5zZm9ybT0ibWF0cml4KDAuMjQsMCwwLDAuMjQsNDMyLDI0MCkiCiAgICAgaWQ9ImczMTA4Ij48ZwogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMCIKICAgICAgIGlkPSJnMzEwNiI+CjxyZWN0CiAgIHdpZHRoPSIxMDAiCiAgIGhlaWdodD0iMTAwIgogICBpZD0icmVjdDMxMDQiCiAgIHg9IjAiCiAgIHk9IjAiIC8+CjwvZz48L2c+PGcKICAgICB0cmFuc2Zvcm09Im1hdHJpeCgwLjI0LDAsMCwwLjI0LDQ1NiwyNDApIgogICAgIGlkPSJnMzExNCI+PGcKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDAiCiAgICAgICBpZD0iZzMxMTIiPgo8cmVjdAogICB3aWR0aD0iMTAwIgogICBoZWlnaHQ9IjEwMCIKICAgaWQ9InJlY3QzMTEwIgogICB4PSIwIgogICB5PSIwIiAvPgo8L2c+PC9nPjxnCiAgICAgdHJhbnNmb3JtPSJtYXRyaXgoMC4yNCwwLDAsMC4yNCwyNCwyNjQpIgogICAgIGlkPSJnMzEyMCI+PGcKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDAiCiAgICAgICBpZD0iZzMxMTgiPgo8cmVjdAogICB3aWR0aD0iMTAwIgogICBoZWlnaHQ9IjEwMCIKICAgaWQ9InJlY3QzMTE2IgogICB4PSIwIgogICB5PSIwIiAvPgo8L2c+PC9nPjxnCiAgICAgdHJhbnNmb3JtPSJtYXRyaXgoMC4yNCwwLDAsMC4yNCw5NiwyNjQpIgogICAgIGlkPSJnMzEyNiI+PGcKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDAiCiAgICAgICBpZD0iZzMxMjQiPgo8cmVjdAogICB3aWR0aD0iMTAwIgogICBoZWlnaHQ9IjEwMCIKICAgaWQ9InJlY3QzMTIyIgogICB4PSIwIgogICB5PSIwIiAvPgo8L2c+PC9nPjxnCiAgICAgdHJhbnNmb3JtPSJtYXRyaXgoMC4yNCwwLDAsMC4yNCwxMjAsMjY0KSIKICAgICBpZD0iZzMxMzIiPjxnCiAgICAgICBzdHlsZT0iZmlsbDojMDAwMDAwIgogICAgICAgaWQ9ImczMTMwIj4KPHJlY3QKICAgd2lkdGg9IjEwMCIKICAgaGVpZ2h0PSIxMDAiCiAgIGlkPSJyZWN0MzEyOCIKICAgeD0iMCIKICAgeT0iMCIgLz4KPC9nPjwvZz48ZwogICAgIHRyYW5zZm9ybT0ibWF0cml4KDAuMjQsMCwwLDAuMjQsMTY4LDI2NCkiCiAgICAgaWQ9ImczMTM4Ij48ZwogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMCIKICAgICAgIGlkPSJnMzEzNiI+CjxyZWN0CiAgIHdpZHRoPSIxMDAiCiAgIGhlaWdodD0iMTAwIgogICBpZD0icmVjdDMxMzQiCiAgIHg9IjAiCiAgIHk9IjAiIC8+CjwvZz48L2c+PGcKICAgICB0cmFuc2Zvcm09Im1hdHJpeCgwLjI0LDAsMCwwLjI0LDE5MiwyNjQpIgogICAgIGlkPSJnMzE0NCI+PGcKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDAiCiAgICAgICBpZD0iZzMxNDIiPgo8cmVjdAogICB3aWR0aD0iMTAwIgogICBoZWlnaHQ9IjEwMCIKICAgaWQ9InJlY3QzMTQwIgogICB4PSIwIgogICB5PSIwIiAvPgo8L2c+PC9nPjxnCiAgICAgdHJhbnNmb3JtPSJtYXRyaXgoMC4yNCwwLDAsMC4yNCwyNDAsMjY0KSIKICAgICBpZD0iZzMxNTAiPjxnCiAgICAgICBzdHlsZT0iZmlsbDojMDAwMDAwIgogICAgICAgaWQ9ImczMTQ4Ij4KPHJlY3QKICAgd2lkdGg9IjEwMCIKICAgaGVpZ2h0PSIxMDAiCiAgIGlkPSJyZWN0MzE0NiIKICAgeD0iMCIKICAgeT0iMCIgLz4KPC9nPjwvZz48ZwogICAgIHRyYW5zZm9ybT0ibWF0cml4KDAuMjQsMCwwLDAuMjQsMzg0LDI2NCkiCiAgICAgaWQ9ImczMTU2Ij48ZwogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMCIKICAgICAgIGlkPSJnMzE1NCI+CjxyZWN0CiAgIHdpZHRoPSIxMDAiCiAgIGhlaWdodD0iMTAwIgogICBpZD0icmVjdDMxNTIiCiAgIHg9IjAiCiAgIHk9IjAiIC8+CjwvZz48L2c+PGcKICAgICB0cmFuc2Zvcm09Im1hdHJpeCgwLjI0LDAsMCwwLjI0LDQwOCwyNjQpIgogICAgIGlkPSJnMzE2MiI+PGcKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDAiCiAgICAgICBpZD0iZzMxNjAiPgo8cmVjdAogICB3aWR0aD0iMTAwIgogICBoZWlnaHQ9IjEwMCIKICAgaWQ9InJlY3QzMTU4IgogICB4PSIwIgogICB5PSIwIiAvPgo8L2c+PC9nPjxnCiAgICAgdHJhbnNmb3JtPSJtYXRyaXgoMC4yNCwwLDAsMC4yNCw0MzIsMjY0KSIKICAgICBpZD0iZzMxNjgiPjxnCiAgICAgICBzdHlsZT0iZmlsbDojMDAwMDAwIgogICAgICAgaWQ9ImczMTY2Ij4KPHJlY3QKICAgd2lkdGg9IjEwMCIKICAgaGVpZ2h0PSIxMDAiCiAgIGlkPSJyZWN0MzE2NCIKICAgeD0iMCIKICAgeT0iMCIgLz4KPC9nPjwvZz48ZwogICAgIHRyYW5zZm9ybT0ibWF0cml4KDAuMjQsMCwwLDAuMjQsNDU2LDI2NCkiCiAgICAgaWQ9ImczMTc0Ij48ZwogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMCIKICAgICAgIGlkPSJnMzE3MiI+CjxyZWN0CiAgIHdpZHRoPSIxMDAiCiAgIGhlaWdodD0iMTAwIgogICBpZD0icmVjdDMxNzAiCiAgIHg9IjAiCiAgIHk9IjAiIC8+CjwvZz48L2c+PGcKICAgICB0cmFuc2Zvcm09Im1hdHJpeCgwLjI0LDAsMCwwLjI0LDQ4MCwyNjQpIgogICAgIGlkPSJnMzE4MCI+PGcKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDAiCiAgICAgICBpZD0iZzMxNzgiPgo8cmVjdAogICB3aWR0aD0iMTAwIgogICBoZWlnaHQ9IjEwMCIKICAgaWQ9InJlY3QzMTc2IgogICB4PSIwIgogICB5PSIwIiAvPgo8L2c+PC9nPjxnCiAgICAgdHJhbnNmb3JtPSJtYXRyaXgoMC4yNCwwLDAsMC4yNCwyNCwyODgpIgogICAgIGlkPSJnMzE4NiI+PGcKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDAiCiAgICAgICBpZD0iZzMxODQiPgo8cmVjdAogICB3aWR0aD0iMTAwIgogICBoZWlnaHQ9IjEwMCIKICAgaWQ9InJlY3QzMTgyIgogICB4PSIwIgogICB5PSIwIiAvPgo8L2c+PC9nPjxnCiAgICAgdHJhbnNmb3JtPSJtYXRyaXgoMC4yNCwwLDAsMC4yNCwxMjAsMjg4KSIKICAgICBpZD0iZzMxOTIiPjxnCiAgICAgICBzdHlsZT0iZmlsbDojMDAwMDAwIgogICAgICAgaWQ9ImczMTkwIj4KPHJlY3QKICAgd2lkdGg9IjEwMCIKICAgaGVpZ2h0PSIxMDAiCiAgIGlkPSJyZWN0MzE4OCIKICAgeD0iMCIKICAgeT0iMCIgLz4KPC9nPjwvZz48ZwogICAgIHRyYW5zZm9ybT0ibWF0cml4KDAuMjQsMCwwLDAuMjQsMTQ0LDI4OCkiCiAgICAgaWQ9ImczMTk4Ij48ZwogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMCIKICAgICAgIGlkPSJnMzE5NiI+CjxyZWN0CiAgIHdpZHRoPSIxMDAiCiAgIGhlaWdodD0iMTAwIgogICBpZD0icmVjdDMxOTQiCiAgIHg9IjAiCiAgIHk9IjAiIC8+CjwvZz48L2c+PGcKICAgICB0cmFuc2Zvcm09Im1hdHJpeCgwLjI0LDAsMCwwLjI0LDIxNiwyODgpIgogICAgIGlkPSJnMzIwNCI+PGcKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDAiCiAgICAgICBpZD0iZzMyMDIiPgo8cmVjdAogICB3aWR0aD0iMTAwIgogICBoZWlnaHQ9IjEwMCIKICAgaWQ9InJlY3QzMjAwIgogICB4PSIwIgogICB5PSIwIiAvPgo8L2c+PC9nPjxnCiAgICAgdHJhbnNmb3JtPSJtYXRyaXgoMC4yNCwwLDAsMC4yNCwyNDAsMjg4KSIKICAgICBpZD0iZzMyMTAiPjxnCiAgICAgICBzdHlsZT0iZmlsbDojMDAwMDAwIgogICAgICAgaWQ9ImczMjA4Ij4KPHJlY3QKICAgd2lkdGg9IjEwMCIKICAgaGVpZ2h0PSIxMDAiCiAgIGlkPSJyZWN0MzIwNiIKICAgeD0iMCIKICAgeT0iMCIgLz4KPC9nPjwvZz48ZwogICAgIHRyYW5zZm9ybT0ibWF0cml4KDAuMjQsMCwwLDAuMjQsMzM2LDI4OCkiCiAgICAgaWQ9ImczMjE2Ij48ZwogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMCIKICAgICAgIGlkPSJnMzIxNCI+CjxyZWN0CiAgIHdpZHRoPSIxMDAiCiAgIGhlaWdodD0iMTAwIgogICBpZD0icmVjdDMyMTIiCiAgIHg9IjAiCiAgIHk9IjAiIC8+CjwvZz48L2c+PGcKICAgICB0cmFuc2Zvcm09Im1hdHJpeCgwLjI0LDAsMCwwLjI0LDQwOCwyODgpIgogICAgIGlkPSJnMzIyMiI+PGcKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDAiCiAgICAgICBpZD0iZzMyMjAiPgo8cmVjdAogICB3aWR0aD0iMTAwIgogICBoZWlnaHQ9IjEwMCIKICAgaWQ9InJlY3QzMjE4IgogICB4PSIwIgogICB5PSIwIiAvPgo8L2c+PC9nPjxnCiAgICAgdHJhbnNmb3JtPSJtYXRyaXgoMC4yNCwwLDAsMC4yNCwxOTIsMzEyKSIKICAgICBpZD0iZzMyMjgiPjxnCiAgICAgICBzdHlsZT0iZmlsbDojMDAwMDAwIgogICAgICAgaWQ9ImczMjI2Ij4KPHJlY3QKICAgd2lkdGg9IjEwMCIKICAgaGVpZ2h0PSIxMDAiCiAgIGlkPSJyZWN0MzIyNCIKICAgeD0iMCIKICAgeT0iMCIgLz4KPC9nPjwvZz48ZwogICAgIHRyYW5zZm9ybT0ibWF0cml4KDAuMjQsMCwwLDAuMjQsMjY0LDMxMikiCiAgICAgaWQ9ImczMjM0Ij48ZwogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMCIKICAgICAgIGlkPSJnMzIzMiI+CjxyZWN0CiAgIHdpZHRoPSIxMDAiCiAgIGhlaWdodD0iMTAwIgogICBpZD0icmVjdDMyMzAiCiAgIHg9IjAiCiAgIHk9IjAiIC8+CjwvZz48L2c+PGcKICAgICB0cmFuc2Zvcm09Im1hdHJpeCgwLjI0LDAsMCwwLjI0LDI4OCwzMTIpIgogICAgIGlkPSJnMzI0MCI+PGcKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDAiCiAgICAgICBpZD0iZzMyMzgiPgo8cmVjdAogICB3aWR0aD0iMTAwIgogICBoZWlnaHQ9IjEwMCIKICAgaWQ9InJlY3QzMjM2IgogICB4PSIwIgogICB5PSIwIiAvPgo8L2c+PC9nPjxnCiAgICAgdHJhbnNmb3JtPSJtYXRyaXgoMC4yNCwwLDAsMC4yNCwzMTIsMzEyKSIKICAgICBpZD0iZzMyNDYiPjxnCiAgICAgICBzdHlsZT0iZmlsbDojMDAwMDAwIgogICAgICAgaWQ9ImczMjQ0Ij4KPHJlY3QKICAgd2lkdGg9IjEwMCIKICAgaGVpZ2h0PSIxMDAiCiAgIGlkPSJyZWN0MzI0MiIKICAgeD0iMCIKICAgeT0iMCIgLz4KPC9nPjwvZz48ZwogICAgIHRyYW5zZm9ybT0ibWF0cml4KDAuMjQsMCwwLDAuMjQsMzM2LDMxMikiCiAgICAgaWQ9ImczMjUyIj48ZwogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMCIKICAgICAgIGlkPSJnMzI1MCI+CjxyZWN0CiAgIHdpZHRoPSIxMDAiCiAgIGhlaWdodD0iMTAwIgogICBpZD0icmVjdDMyNDgiCiAgIHg9IjAiCiAgIHk9IjAiIC8+CjwvZz48L2c+PGcKICAgICB0cmFuc2Zvcm09Im1hdHJpeCgwLjI0LDAsMCwwLjI0LDQwOCwzMTIpIgogICAgIGlkPSJnMzI1OCI+PGcKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDAiCiAgICAgICBpZD0iZzMyNTYiPgo8cmVjdAogICB3aWR0aD0iMTAwIgogICBoZWlnaHQ9IjEwMCIKICAgaWQ9InJlY3QzMjU0IgogICB4PSIwIgogICB5PSIwIiAvPgo8L2c+PC9nPjxnCiAgICAgdHJhbnNmb3JtPSJtYXRyaXgoMC4yNCwwLDAsMC4yNCw0MzIsMzEyKSIKICAgICBpZD0iZzMyNjQiPjxnCiAgICAgICBzdHlsZT0iZmlsbDojMDAwMDAwIgogICAgICAgaWQ9ImczMjYyIj4KPHJlY3QKICAgd2lkdGg9IjEwMCIKICAgaGVpZ2h0PSIxMDAiCiAgIGlkPSJyZWN0MzI2MCIKICAgeD0iMCIKICAgeT0iMCIgLz4KPC9nPjwvZz48ZwogICAgIHRyYW5zZm9ybT0ibWF0cml4KDAuMjQsMCwwLDAuMjQsMjQwLDMzNikiCiAgICAgaWQ9ImczMjcwIj48ZwogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMCIKICAgICAgIGlkPSJnMzI2OCI+CjxyZWN0CiAgIHdpZHRoPSIxMDAiCiAgIGhlaWdodD0iMTAwIgogICBpZD0icmVjdDMyNjYiCiAgIHg9IjAiCiAgIHk9IjAiIC8+CjwvZz48L2c+PGcKICAgICB0cmFuc2Zvcm09Im1hdHJpeCgwLjI0LDAsMCwwLjI0LDI4OCwzMzYpIgogICAgIGlkPSJnMzI3NiI+PGcKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDAiCiAgICAgICBpZD0iZzMyNzQiPgo8cmVjdAogICB3aWR0aD0iMTAwIgogICBoZWlnaHQ9IjEwMCIKICAgaWQ9InJlY3QzMjcyIgogICB4PSIwIgogICB5PSIwIiAvPgo8L2c+PC9nPjxnCiAgICAgdHJhbnNmb3JtPSJtYXRyaXgoMC4yNCwwLDAsMC4yNCwzMzYsMzM2KSIKICAgICBpZD0iZzMyODIiPjxnCiAgICAgICBzdHlsZT0iZmlsbDojMDAwMDAwIgogICAgICAgaWQ9ImczMjgwIj4KPHJlY3QKICAgd2lkdGg9IjEwMCIKICAgaGVpZ2h0PSIxMDAiCiAgIGlkPSJyZWN0MzI3OCIKICAgeD0iMCIKICAgeT0iMCIgLz4KPC9nPjwvZz48ZwogICAgIHRyYW5zZm9ybT0ibWF0cml4KDAuMjQsMCwwLDAuMjQsMzYwLDMzNikiCiAgICAgaWQ9ImczMjg4Ij48ZwogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMCIKICAgICAgIGlkPSJnMzI4NiI+CjxyZWN0CiAgIHdpZHRoPSIxMDAiCiAgIGhlaWdodD0iMTAwIgogICBpZD0icmVjdDMyODQiCiAgIHg9IjAiCiAgIHk9IjAiIC8+CjwvZz48L2c+PGcKICAgICB0cmFuc2Zvcm09Im1hdHJpeCgwLjI0LDAsMCwwLjI0LDQwOCwzMzYpIgogICAgIGlkPSJnMzI5NCI+PGcKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDAiCiAgICAgICBpZD0iZzMyOTIiPgo8cmVjdAogICB3aWR0aD0iMTAwIgogICBoZWlnaHQ9IjEwMCIKICAgaWQ9InJlY3QzMjkwIgogICB4PSIwIgogICB5PSIwIiAvPgo8L2c+PC9nPjxnCiAgICAgdHJhbnNmb3JtPSJtYXRyaXgoMC4yNCwwLDAsMC4yNCw0MzIsMzM2KSIKICAgICBpZD0iZzMzMDAiPjxnCiAgICAgICBzdHlsZT0iZmlsbDojMDAwMDAwIgogICAgICAgaWQ9ImczMjk4Ij4KPHJlY3QKICAgd2lkdGg9IjEwMCIKICAgaGVpZ2h0PSIxMDAiCiAgIGlkPSJyZWN0MzI5NiIKICAgeD0iMCIKICAgeT0iMCIgLz4KPC9nPjwvZz48ZwogICAgIHRyYW5zZm9ybT0ibWF0cml4KDAuMjQsMCwwLDAuMjQsNDU2LDMzNikiCiAgICAgaWQ9ImczMzA2Ij48ZwogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMCIKICAgICAgIGlkPSJnMzMwNCI+CjxyZWN0CiAgIHdpZHRoPSIxMDAiCiAgIGhlaWdodD0iMTAwIgogICBpZD0icmVjdDMzMDIiCiAgIHg9IjAiCiAgIHk9IjAiIC8+CjwvZz48L2c+PGcKICAgICB0cmFuc2Zvcm09Im1hdHJpeCgwLjI0LDAsMCwwLjI0LDIxNiwzNjApIgogICAgIGlkPSJnMzMxMiI+PGcKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDAiCiAgICAgICBpZD0iZzMzMTAiPgo8cmVjdAogICB3aWR0aD0iMTAwIgogICBoZWlnaHQ9IjEwMCIKICAgaWQ9InJlY3QzMzA4IgogICB4PSIwIgogICB5PSIwIiAvPgo8L2c+PC9nPjxnCiAgICAgdHJhbnNmb3JtPSJtYXRyaXgoMC4yNCwwLDAsMC4yNCwyNjQsMzYwKSIKICAgICBpZD0iZzMzMTgiPjxnCiAgICAgICBzdHlsZT0iZmlsbDojMDAwMDAwIgogICAgICAgaWQ9ImczMzE2Ij4KPHJlY3QKICAgd2lkdGg9IjEwMCIKICAgaGVpZ2h0PSIxMDAiCiAgIGlkPSJyZWN0MzMxNCIKICAgeD0iMCIKICAgeT0iMCIgLz4KPC9nPjwvZz48ZwogICAgIHRyYW5zZm9ybT0ibWF0cml4KDAuMjQsMCwwLDAuMjQsMjg4LDM2MCkiCiAgICAgaWQ9ImczMzI0Ij48ZwogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMCIKICAgICAgIGlkPSJnMzMyMiI+CjxyZWN0CiAgIHdpZHRoPSIxMDAiCiAgIGhlaWdodD0iMTAwIgogICBpZD0icmVjdDMzMjAiCiAgIHg9IjAiCiAgIHk9IjAiIC8+CjwvZz48L2c+PGcKICAgICB0cmFuc2Zvcm09Im1hdHJpeCgwLjI0LDAsMCwwLjI0LDMxMiwzNjApIgogICAgIGlkPSJnMzMzMCI+PGcKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDAiCiAgICAgICBpZD0iZzMzMjgiPgo8cmVjdAogICB3aWR0aD0iMTAwIgogICBoZWlnaHQ9IjEwMCIKICAgaWQ9InJlY3QzMzI2IgogICB4PSIwIgogICB5PSIwIiAvPgo8L2c+PC9nPjxnCiAgICAgdHJhbnNmb3JtPSJtYXRyaXgoMC4yNCwwLDAsMC4yNCw0MDgsMzYwKSIKICAgICBpZD0iZzMzMzYiPjxnCiAgICAgICBzdHlsZT0iZmlsbDojMDAwMDAwIgogICAgICAgaWQ9ImczMzM0Ij4KPHJlY3QKICAgd2lkdGg9IjEwMCIKICAgaGVpZ2h0PSIxMDAiCiAgIGlkPSJyZWN0MzMzMiIKICAgeD0iMCIKICAgeT0iMCIgLz4KPC9nPjwvZz48ZwogICAgIHRyYW5zZm9ybT0ibWF0cml4KDAuMjQsMCwwLDAuMjQsNDMyLDM2MCkiCiAgICAgaWQ9ImczMzQyIj48ZwogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMCIKICAgICAgIGlkPSJnMzM0MCI+CjxyZWN0CiAgIHdpZHRoPSIxMDAiCiAgIGhlaWdodD0iMTAwIgogICBpZD0icmVjdDMzMzgiCiAgIHg9IjAiCiAgIHk9IjAiIC8+CjwvZz48L2c+PGcKICAgICB0cmFuc2Zvcm09Im1hdHJpeCgwLjI0LDAsMCwwLjI0LDIxNiwzODQpIgogICAgIGlkPSJnMzM0OCI+PGcKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDAiCiAgICAgICBpZD0iZzMzNDYiPgo8cmVjdAogICB3aWR0aD0iMTAwIgogICBoZWlnaHQ9IjEwMCIKICAgaWQ9InJlY3QzMzQ0IgogICB4PSIwIgogICB5PSIwIiAvPgo8L2c+PC9nPjxnCiAgICAgdHJhbnNmb3JtPSJtYXRyaXgoMC4yNCwwLDAsMC4yNCwyODgsMzg0KSIKICAgICBpZD0iZzMzNTQiPjxnCiAgICAgICBzdHlsZT0iZmlsbDojMDAwMDAwIgogICAgICAgaWQ9ImczMzUyIj4KPHJlY3QKICAgd2lkdGg9IjEwMCIKICAgaGVpZ2h0PSIxMDAiCiAgIGlkPSJyZWN0MzM1MCIKICAgeD0iMCIKICAgeT0iMCIgLz4KPC9nPjwvZz48ZwogICAgIHRyYW5zZm9ybT0ibWF0cml4KDAuMjQsMCwwLDAuMjQsMzYwLDM4NCkiCiAgICAgaWQ9ImczMzYwIj48ZwogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMCIKICAgICAgIGlkPSJnMzM1OCI+CjxyZWN0CiAgIHdpZHRoPSIxMDAiCiAgIGhlaWdodD0iMTAwIgogICBpZD0icmVjdDMzNTYiCiAgIHg9IjAiCiAgIHk9IjAiIC8+CjwvZz48L2c+PGcKICAgICB0cmFuc2Zvcm09Im1hdHJpeCgwLjI0LDAsMCwwLjI0LDQ1NiwzODQpIgogICAgIGlkPSJnMzM2NiI+PGcKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDAiCiAgICAgICBpZD0iZzMzNjQiPgo8cmVjdAogICB3aWR0aD0iMTAwIgogICBoZWlnaHQ9IjEwMCIKICAgaWQ9InJlY3QzMzYyIgogICB4PSIwIgogICB5PSIwIiAvPgo8L2c+PC9nPjxnCiAgICAgdHJhbnNmb3JtPSJtYXRyaXgoMC4yNCwwLDAsMC4yNCwyMTYsNDA4KSIKICAgICBpZD0iZzMzNzIiPjxnCiAgICAgICBzdHlsZT0iZmlsbDojMDAwMDAwIgogICAgICAgaWQ9ImczMzcwIj4KPHJlY3QKICAgd2lkdGg9IjEwMCIKICAgaGVpZ2h0PSIxMDAiCiAgIGlkPSJyZWN0MzM2OCIKICAgeD0iMCIKICAgeT0iMCIgLz4KPC9nPjwvZz48ZwogICAgIHRyYW5zZm9ybT0ibWF0cml4KDAuMjQsMCwwLDAuMjQsMjg4LDQwOCkiCiAgICAgaWQ9ImczMzc4Ij48ZwogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMCIKICAgICAgIGlkPSJnMzM3NiI+CjxyZWN0CiAgIHdpZHRoPSIxMDAiCiAgIGhlaWdodD0iMTAwIgogICBpZD0icmVjdDMzNzQiCiAgIHg9IjAiCiAgIHk9IjAiIC8+CjwvZz48L2c+PGcKICAgICB0cmFuc2Zvcm09Im1hdHJpeCgwLjI0LDAsMCwwLjI0LDM2MCw0MDgpIgogICAgIGlkPSJnMzM4NCI+PGcKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDAiCiAgICAgICBpZD0iZzMzODIiPgo8cmVjdAogICB3aWR0aD0iMTAwIgogICBoZWlnaHQ9IjEwMCIKICAgaWQ9InJlY3QzMzgwIgogICB4PSIwIgogICB5PSIwIiAvPgo8L2c+PC9nPjxnCiAgICAgdHJhbnNmb3JtPSJtYXRyaXgoMC4yNCwwLDAsMC4yNCw0MDgsNDA4KSIKICAgICBpZD0iZzMzOTAiPjxnCiAgICAgICBzdHlsZT0iZmlsbDojMDAwMDAwIgogICAgICAgaWQ9ImczMzg4Ij4KPHJlY3QKICAgd2lkdGg9IjEwMCIKICAgaGVpZ2h0PSIxMDAiCiAgIGlkPSJyZWN0MzM4NiIKICAgeD0iMCIKICAgeT0iMCIgLz4KPC9nPjwvZz48ZwogICAgIHRyYW5zZm9ybT0ibWF0cml4KDAuMjQsMCwwLDAuMjQsMjE2LDQzMikiCiAgICAgaWQ9ImczMzk2Ij48ZwogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMCIKICAgICAgIGlkPSJnMzM5NCI+CjxyZWN0CiAgIHdpZHRoPSIxMDAiCiAgIGhlaWdodD0iMTAwIgogICBpZD0icmVjdDMzOTIiCiAgIHg9IjAiCiAgIHk9IjAiIC8+CjwvZz48L2c+PGcKICAgICB0cmFuc2Zvcm09Im1hdHJpeCgwLjI0LDAsMCwwLjI0LDMzNiw0MzIpIgogICAgIGlkPSJnMzQwMiI+PGcKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDAiCiAgICAgICBpZD0iZzM0MDAiPgo8cmVjdAogICB3aWR0aD0iMTAwIgogICBoZWlnaHQ9IjEwMCIKICAgaWQ9InJlY3QzMzk4IgogICB4PSIwIgogICB5PSIwIiAvPgo8L2c+PC9nPjxnCiAgICAgdHJhbnNmb3JtPSJtYXRyaXgoMC4yNCwwLDAsMC4yNCwzODQsNDMyKSIKICAgICBpZD0iZzM0MDgiPjxnCiAgICAgICBzdHlsZT0iZmlsbDojMDAwMDAwIgogICAgICAgaWQ9ImczNDA2Ij4KPHJlY3QKICAgd2lkdGg9IjEwMCIKICAgaGVpZ2h0PSIxMDAiCiAgIGlkPSJyZWN0MzQwNCIKICAgeD0iMCIKICAgeT0iMCIgLz4KPC9nPjwvZz48ZwogICAgIHRyYW5zZm9ybT0ibWF0cml4KDAuMjQsMCwwLDAuMjQsNDA4LDQzMikiCiAgICAgaWQ9ImczNDE0Ij48ZwogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMCIKICAgICAgIGlkPSJnMzQxMiI+CjxyZWN0CiAgIHdpZHRoPSIxMDAiCiAgIGhlaWdodD0iMTAwIgogICBpZD0icmVjdDM0MTAiCiAgIHg9IjAiCiAgIHk9IjAiIC8+CjwvZz48L2c+PGcKICAgICB0cmFuc2Zvcm09Im1hdHJpeCgwLjI0LDAsMCwwLjI0LDQ1Niw0MzIpIgogICAgIGlkPSJnMzQyMCI+PGcKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDAiCiAgICAgICBpZD0iZzM0MTgiPgo8cmVjdAogICB3aWR0aD0iMTAwIgogICBoZWlnaHQ9IjEwMCIKICAgaWQ9InJlY3QzNDE2IgogICB4PSIwIgogICB5PSIwIiAvPgo8L2c+PC9nPjxnCiAgICAgdHJhbnNmb3JtPSJtYXRyaXgoMC4yNCwwLDAsMC4yNCw0ODAsNDMyKSIKICAgICBpZD0iZzM0MjYiPjxnCiAgICAgICBzdHlsZT0iZmlsbDojMDAwMDAwIgogICAgICAgaWQ9ImczNDI0Ij4KPHJlY3QKICAgd2lkdGg9IjEwMCIKICAgaGVpZ2h0PSIxMDAiCiAgIGlkPSJyZWN0MzQyMiIKICAgeD0iMCIKICAgeT0iMCIgLz4KPC9nPjwvZz48ZwogICAgIHRyYW5zZm9ybT0ibWF0cml4KDAuMjQsMCwwLDAuMjQsMjE2LDQ1NikiCiAgICAgaWQ9ImczNDMyIj48ZwogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMCIKICAgICAgIGlkPSJnMzQzMCI+CjxyZWN0CiAgIHdpZHRoPSIxMDAiCiAgIGhlaWdodD0iMTAwIgogICBpZD0icmVjdDM0MjgiCiAgIHg9IjAiCiAgIHk9IjAiIC8+CjwvZz48L2c+PGcKICAgICB0cmFuc2Zvcm09Im1hdHJpeCgwLjI0LDAsMCwwLjI0LDQwOCw0NTYpIgogICAgIGlkPSJnMzQzOCI+PGcKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDAiCiAgICAgICBpZD0iZzM0MzYiPgo8cmVjdAogICB3aWR0aD0iMTAwIgogICBoZWlnaHQ9IjEwMCIKICAgaWQ9InJlY3QzNDM0IgogICB4PSIwIgogICB5PSIwIiAvPgo8L2c+PC9nPjxnCiAgICAgdHJhbnNmb3JtPSJtYXRyaXgoMC4yNCwwLDAsMC4yNCw0MzIsNDU2KSIKICAgICBpZD0iZzM0NDQiPjxnCiAgICAgICBzdHlsZT0iZmlsbDojMDAwMDAwIgogICAgICAgaWQ9ImczNDQyIj4KPHJlY3QKICAgd2lkdGg9IjEwMCIKICAgaGVpZ2h0PSIxMDAiCiAgIGlkPSJyZWN0MzQ0MCIKICAgeD0iMCIKICAgeT0iMCIgLz4KPC9nPjwvZz48ZwogICAgIHRyYW5zZm9ybT0ibWF0cml4KDAuMjQsMCwwLDAuMjQsMTkyLDQ4MCkiCiAgICAgaWQ9ImczNDUwIj48ZwogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMCIKICAgICAgIGlkPSJnMzQ0OCI+CjxyZWN0CiAgIHdpZHRoPSIxMDAiCiAgIGhlaWdodD0iMTAwIgogICBpZD0icmVjdDM0NDYiCiAgIHg9IjAiCiAgIHk9IjAiIC8+CjwvZz48L2c+PGcKICAgICB0cmFuc2Zvcm09Im1hdHJpeCgwLjI0LDAsMCwwLjI0LDI0MCw0ODApIgogICAgIGlkPSJnMzQ1NiI+PGcKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDAiCiAgICAgICBpZD0iZzM0NTQiPgo8cmVjdAogICB3aWR0aD0iMTAwIgogICBoZWlnaHQ9IjEwMCIKICAgaWQ9InJlY3QzNDUyIgogICB4PSIwIgogICB5PSIwIiAvPgo8L2c+PC9nPjxnCiAgICAgdHJhbnNmb3JtPSJtYXRyaXgoMC4yNCwwLDAsMC4yNCwyNjQsNDgwKSIKICAgICBpZD0iZzM0NjIiPjxnCiAgICAgICBzdHlsZT0iZmlsbDojMDAwMDAwIgogICAgICAgaWQ9ImczNDYwIj4KPHJlY3QKICAgd2lkdGg9IjEwMCIKICAgaGVpZ2h0PSIxMDAiCiAgIGlkPSJyZWN0MzQ1OCIKICAgeD0iMCIKICAgeT0iMCIgLz4KPC9nPjwvZz48ZwogICAgIHRyYW5zZm9ybT0ibWF0cml4KDAuMjQsMCwwLDAuMjQsMzEyLDQ4MCkiCiAgICAgaWQ9ImczNDY4Ij48ZwogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMCIKICAgICAgIGlkPSJnMzQ2NiI+CjxyZWN0CiAgIHdpZHRoPSIxMDAiCiAgIGhlaWdodD0iMTAwIgogICBpZD0icmVjdDM0NjQiCiAgIHg9IjAiCiAgIHk9IjAiIC8+CjwvZz48L2c+PGcKICAgICB0cmFuc2Zvcm09Im1hdHJpeCgwLjI0LDAsMCwwLjI0LDM2MCw0ODApIgogICAgIGlkPSJnMzQ3NCI+PGcKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDAiCiAgICAgICBpZD0iZzM0NzIiPgo8cmVjdAogICB3aWR0aD0iMTAwIgogICBoZWlnaHQ9IjEwMCIKICAgaWQ9InJlY3QzNDcwIgogICB4PSIwIgogICB5PSIwIiAvPgo8L2c+PC9nPjxnCiAgICAgdHJhbnNmb3JtPSJtYXRyaXgoMC4yNCwwLDAsMC4yNCwzODQsNDgwKSIKICAgICBpZD0iZzM0ODAiPjxnCiAgICAgICBzdHlsZT0iZmlsbDojMDAwMDAwIgogICAgICAgaWQ9ImczNDc4Ij4KPHJlY3QKICAgd2lkdGg9IjEwMCIKICAgaGVpZ2h0PSIxMDAiCiAgIGlkPSJyZWN0MzQ3NiIKICAgeD0iMCIKICAgeT0iMCIgLz4KPC9nPjwvZz48ZwogICAgIHRyYW5zZm9ybT0ibWF0cml4KDAuMjQsMCwwLDAuMjQsNDA4LDQ4MCkiCiAgICAgaWQ9ImczNDg2Ij48ZwogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMCIKICAgICAgIGlkPSJnMzQ4NCI+CjxyZWN0CiAgIHdpZHRoPSIxMDAiCiAgIGhlaWdodD0iMTAwIgogICBpZD0icmVjdDM0ODIiCiAgIHg9IjAiCiAgIHk9IjAiIC8+CjwvZz48L2c+PGcKICAgICB0cmFuc2Zvcm09Im1hdHJpeCgwLjI0LDAsMCwwLjI0LDQzMiw0ODApIgogICAgIGlkPSJnMzQ5MiI+PGcKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDAiCiAgICAgICBpZD0iZzM0OTAiPgo8cmVjdAogICB3aWR0aD0iMTAwIgogICBoZWlnaHQ9IjEwMCIKICAgaWQ9InJlY3QzNDg4IgogICB4PSIwIgogICB5PSIwIiAvPgo8L2c+PC9nPjxnCiAgICAgdHJhbnNmb3JtPSJtYXRyaXgoMC4yNCwwLDAsMC4yNCw0NTYsNDgwKSIKICAgICBpZD0iZzM0OTgiPjxnCiAgICAgICBzdHlsZT0iZmlsbDojMDAwMDAwIgogICAgICAgaWQ9ImczNDk2Ij4KPHJlY3QKICAgd2lkdGg9IjEwMCIKICAgaGVpZ2h0PSIxMDAiCiAgIGlkPSJyZWN0MzQ5NCIKICAgeD0iMCIKICAgeT0iMCIgLz4KPC9nPjwvZz48ZwogICAgIHRyYW5zZm9ybT0ic2NhbGUoMS42OCkiCiAgICAgaWQ9ImczNTA4Ij48ZwogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMCIKICAgICAgIGlkPSJnMzUwNiI+CjxnCiAgIGlkPSJnMzUwNCI+Cgk8cmVjdAogICB4PSIxNSIKICAgeT0iMTUiCiAgIHN0eWxlPSJmaWxsOm5vbmUiCiAgIHdpZHRoPSI3MCIKICAgaGVpZ2h0PSI3MCIKICAgaWQ9InJlY3QzNTAwIiAvPgoJPHBhdGgKICAgZD0iTSA4NSwwIEggMTUgMCB2IDE1IDcwIDE1IGggMTUgNzAgMTUgViA4NSAxNSAwIFogbSAwLDg1IEggMTUgViAxNSBoIDcwIHoiCiAgIGlkPSJwYXRoMzUwMiIKICAgaW5rc2NhcGU6Y29ubmVjdG9yLWN1cnZhdHVyZT0iMCIgLz4KPC9nPgo8L2c+PC9nPjxnCiAgICAgdHJhbnNmb3JtPSJtYXRyaXgoMS42OCwwLDAsMS42OCwzMzYsMCkiCiAgICAgaWQ9ImczNTE4Ij48ZwogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMCIKICAgICAgIGlkPSJnMzUxNiI+CjxnCiAgIGlkPSJnMzUxNCI+Cgk8cmVjdAogICB4PSIxNSIKICAgeT0iMTUiCiAgIHN0eWxlPSJmaWxsOm5vbmUiCiAgIHdpZHRoPSI3MCIKICAgaGVpZ2h0PSI3MCIKICAgaWQ9InJlY3QzNTEwIiAvPgoJPHBhdGgKICAgZD0iTSA4NSwwIEggMTUgMCB2IDE1IDcwIDE1IGggMTUgNzAgMTUgViA4NSAxNSAwIFogbSAwLDg1IEggMTUgViAxNSBoIDcwIHoiCiAgIGlkPSJwYXRoMzUxMiIKICAgaW5rc2NhcGU6Y29ubmVjdG9yLWN1cnZhdHVyZT0iMCIgLz4KPC9nPgo8L2c+PC9nPjxnCiAgICAgdHJhbnNmb3JtPSJtYXRyaXgoMS42OCwwLDAsMS42OCwwLDMzNikiCiAgICAgaWQ9ImczNTI4Ij48ZwogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMCIKICAgICAgIGlkPSJnMzUyNiI+CjxnCiAgIGlkPSJnMzUyNCI+Cgk8cmVjdAogICB4PSIxNSIKICAgeT0iMTUiCiAgIHN0eWxlPSJmaWxsOm5vbmUiCiAgIHdpZHRoPSI3MCIKICAgaGVpZ2h0PSI3MCIKICAgaWQ9InJlY3QzNTIwIiAvPgoJPHBhdGgKICAgZD0iTSA4NSwwIEggMTUgMCB2IDE1IDcwIDE1IGggMTUgNzAgMTUgViA4NSAxNSAwIFogbSAwLDg1IEggMTUgViAxNSBoIDcwIHoiCiAgIGlkPSJwYXRoMzUyMiIKICAgaW5rc2NhcGU6Y29ubmVjdG9yLWN1cnZhdHVyZT0iMCIgLz4KPC9nPgo8L2c+PC9nPjxnCiAgICAgdHJhbnNmb3JtPSJtYXRyaXgoMC43MiwwLDAsMC43Miw0OCw0OCkiCiAgICAgaWQ9ImczNTM0Ij48ZwogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMCIKICAgICAgIGlkPSJnMzUzMiI+CjxyZWN0CiAgIHdpZHRoPSIxMDAiCiAgIGhlaWdodD0iMTAwIgogICBpZD0icmVjdDM1MzAiCiAgIHg9IjAiCiAgIHk9IjAiIC8+CjwvZz48L2c+PGcKICAgICB0cmFuc2Zvcm09Im1hdHJpeCgwLjcyLDAsMCwwLjcyLDM4NCw0OCkiCiAgICAgaWQ9ImczNTQwIj48ZwogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMCIKICAgICAgIGlkPSJnMzUzOCI+CjxyZWN0CiAgIHdpZHRoPSIxMDAiCiAgIGhlaWdodD0iMTAwIgogICBpZD0icmVjdDM1MzYiCiAgIHg9IjAiCiAgIHk9IjAiIC8+CjwvZz48L2c+PGcKICAgICB0cmFuc2Zvcm09Im1hdHJpeCgwLjcyLDAsMCwwLjcyLDQ4LDM4NCkiCiAgICAgaWQ9ImczNTQ2Ij48ZwogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMCIKICAgICAgIGlkPSJnMzU0NCI+CjxyZWN0CiAgIHdpZHRoPSIxMDAiCiAgIGhlaWdodD0iMTAwIgogICBpZD0icmVjdDM1NDIiCiAgIHg9IjAiCiAgIHk9IjAiIC8+CjwvZz48L2c+PC9nPjwvc3ZnPgo=)

### Figure 26. QR code with text 'OpenXR'

![ext marker tracking apriltag](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjxzdmcKICAgeG1sbnM6ZGM9Imh0dHA6Ly9wdXJsLm9yZy9kYy9lbGVtZW50cy8xLjEvIgogICB4bWxuczpjYz0iaHR0cDovL2NyZWF0aXZlY29tbW9ucy5vcmcvbnMjIgogICB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiCiAgIHhtbG5zOnN2Zz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiAgIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIKICAgeG1sbnM6c29kaXBvZGk9Imh0dHA6Ly9zb2RpcG9kaS5zb3VyY2Vmb3JnZS5uZXQvRFREL3NvZGlwb2RpLTAuZHRkIgogICB4bWxuczppbmtzY2FwZT0iaHR0cDovL3d3dy5pbmtzY2FwZS5vcmcvbmFtZXNwYWNlcy9pbmtzY2FwZSIKICAgd2lkdGg9IjEwMG1tIgogICBoZWlnaHQ9IjEwMG1tIgogICB2aWV3Qm94PSIwIDAgMTAwIDEwMCIKICAgdmVyc2lvbj0iMS4xIgogICBpZD0ic3ZnODUyNiIKICAgc29kaXBvZGk6ZG9jbmFtZT0iZXh0X21hcmtlcl90cmFja2luZ19hcHJpbHRhZy5zdmciCiAgIGlua3NjYXBlOnZlcnNpb249IjAuOTIuNSAoMjA2MGVjMWY5ZiwgMjAyMC0wNC0wOCkiPgogIDxtZXRhZGF0YQogICAgIGlkPSJtZXRhZGF0YTg1MzIiPgogICAgPHJkZjpSREY+CiAgICAgIDxjYzpXb3JrCiAgICAgICAgIHJkZjphYm91dD0iIj4KICAgICAgICA8ZGM6Zm9ybWF0PmltYWdlL3N2Zyt4bWw8L2RjOmZvcm1hdD4KICAgICAgICA8ZGM6dHlwZQogICAgICAgICAgIHJkZjpyZXNvdXJjZT0iaHR0cDovL3B1cmwub3JnL2RjL2RjbWl0eXBlL1N0aWxsSW1hZ2UiIC8+CiAgICAgICAgPGRjOnRpdGxlPjwvZGM6dGl0bGU+CiAgICAgIDwvY2M6V29yaz4KICAgIDwvcmRmOlJERj4KICA8L21ldGFkYXRhPgogIDxkZWZzCiAgICAgaWQ9ImRlZnM4NTMwIiAvPgogIDxzb2RpcG9kaTpuYW1lZHZpZXcKICAgICBwYWdlY29sb3I9IiNmZmZmZmYiCiAgICAgYm9yZGVyY29sb3I9IiM2NjY2NjYiCiAgICAgYm9yZGVyb3BhY2l0eT0iMSIKICAgICBvYmplY3R0b2xlcmFuY2U9IjEwIgogICAgIGdyaWR0b2xlcmFuY2U9IjEwIgogICAgIGd1aWRldG9sZXJhbmNlPSIxMCIKICAgICBpbmtzY2FwZTpwYWdlb3BhY2l0eT0iMCIKICAgICBpbmtzY2FwZTpwYWdlc2hhZG93PSIyIgogICAgIGlua3NjYXBlOndpbmRvdy13aWR0aD0iMzg0MCIKICAgICBpbmtzY2FwZTp3aW5kb3ctaGVpZ2h0PSIyMDE1IgogICAgIGlkPSJuYW1lZHZpZXc4NTI4IgogICAgIHNob3dncmlkPSJmYWxzZSIKICAgICBpbmtzY2FwZTp6b29tPSIyLjQ5NzY2NjciCiAgICAgaW5rc2NhcGU6Y3g9IjI4NC44OTA1OCIKICAgICBpbmtzY2FwZTpjeT0iMTU1LjY4OTIzIgogICAgIGlua3NjYXBlOndpbmRvdy14PSIwIgogICAgIGlua3NjYXBlOndpbmRvdy15PSIwIgogICAgIGlua3NjYXBlOndpbmRvdy1tYXhpbWl6ZWQ9IjEiCiAgICAgaW5rc2NhcGU6Y3VycmVudC1sYXllcj0ic3ZnODUyNiIgLz4KICA8cGF0aAogICAgIHN0eWxlPSJmaWxsOiMwMDAwMDA7c3Ryb2tlOm5vbmU7c3Ryb2tlLXdpZHRoOjEuMjUwMjY0ODgiCiAgICAgZD0iTSAwLjI1NDIzNzM1LDAuMTQ4MzA1MTUgViAxMDAuMTY5NDkgSCAxMDAuMjc1NDIgViAwLjE0ODMwNTE1IFoiCiAgICAgaWQ9InBhdGg4NTIwIgogICAgIGlua3NjYXBlOmNvbm5lY3Rvci1jdXJ2YXR1cmU9IjAiIC8+CiAgPHBhdGgKICAgICBzdHlsZT0iZmlsbDojZmZmZmZmO3N0cm9rZTpub25lO3N0cm9rZS13aWR0aDoxLjI1MDI2NDg4IgogICAgIGQ9Ik0gMTIuNzU2ODg1LDEyLjY1MDk1MyBWIDM3LjY1NjI1IEggMjUuMjU5NTM0IFYgMjUuMTUzNjAyIEggMzcuNzYyMTgyIFYgMzcuNjU2MjUgSCA1MC4yNjQ4MyBWIDI1LjE1MzYwMiBIIDYyLjc2NzQ3OCBWIDEyLjY1MDk1MyBIIDUwLjI2NDgzIFYgMjUuMTUzNjAyIEggMzcuNzYyMTgyIFYgMTIuNjUwOTUzIEggMTIuNzU2ODg1IE0gNzUuMjcwMTI3LDI1LjE1MzYwMiBWIDM3LjY1NjI1IEggNjIuNzY3NDc4IFYgNjIuNjYxNTQ2IEggNTAuMjY0ODMgViA1MC4xNTg4OTggSCAzNy43NjIxODIgViA2Mi42NjE1NDYgSCAyNS4yNTk1MzQgViA1MC4xNTg4OTggSCAxMi43NTY4ODUgViA2Mi42NjE1NDYgSCAyNS4yNTk1MzQgViA3NS4xNjQxOTUgSCAxMi43NTY4ODUgViA4Ny42NjY4NDMgSCA1MC4yNjQ4MyBWIDc1LjE2NDE5NSBIIDYyLjc2NzQ3OCBWIDg3LjY2Njg0MyBIIDg3Ljc3Mjc3NSBWIDYyLjY2MTU0NiBIIDc1LjI3MDEyNyBWIDM3LjY1NjI1IEggODcuNzcyNzc1IFYgMjUuMTUzNjAyIFoiCiAgICAgaWQ9InBhdGg4NTIyIgogICAgIGlua3NjYXBlOmNvbm5lY3Rvci1jdXJ2YXR1cmU9IjAiIC8+CiAgPHBhdGgKICAgICBzdHlsZT0iZmlsbDojMDAwMDAwO3N0cm9rZTpub25lO3N0cm9rZS13aWR0aDoxLjI1MDI2NDg4IgogICAgIGQ9Ik0gNjIuNzY3NDc4LDYyLjY2MTU0NiBWIDc1LjE2NDE5NSBIIDc1LjI3MDEyNyBWIDYyLjY2MTU0NiBaIgogICAgIGlkPSJwYXRoODUyNCIKICAgICBpbmtzY2FwZTpjb25uZWN0b3ItY3VydmF0dXJlPSIwIiAvPgo8L3N2Zz4K)

### Figure 27. AprilTag `XR_SPATIAL_MARKER_APRIL_TAG_DICT_36H11_EXT` with ID 42

![ext marker tracking aruco](data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgNyA3IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHNoYXBlLXJlbmRlcmluZz0iY3Jpc3BFZGdlcyIgd2lkdGg9IjEwMG1tIiBoZWlnaHQ9IjEwMG1tIj48cmVjdCB4PSIwIiB5PSIwIiB3aWR0aD0iNyIgaGVpZ2h0PSI3IiBmaWxsPSJibGFjayI+PC9yZWN0PjxyZWN0IHdpZHRoPSIxLjUiIGhlaWdodD0iMSIgeD0iMiIgeT0iMSIgZmlsbD0id2hpdGUiPjwvcmVjdD48cmVjdCB3aWR0aD0iMSIgaGVpZ2h0PSIxIiB4PSIzIiB5PSIxIiBmaWxsPSJ3aGl0ZSI+PC9yZWN0PjxyZWN0IHdpZHRoPSIxIiBoZWlnaHQ9IjEuNSIgeD0iMyIgeT0iMSIgZmlsbD0id2hpdGUiPjwvcmVjdD48cmVjdCB3aWR0aD0iMS41IiBoZWlnaHQ9IjEiIHg9IjMiIHk9IjIiIGZpbGw9IndoaXRlIj48L3JlY3Q+PHJlY3Qgd2lkdGg9IjEiIGhlaWdodD0iMSIgeD0iNCIgeT0iMiIgZmlsbD0id2hpdGUiPjwvcmVjdD48cmVjdCB3aWR0aD0iMSIgaGVpZ2h0PSIxLjUiIHg9IjQiIHk9IjIiIGZpbGw9IndoaXRlIj48L3JlY3Q+PHJlY3Qgd2lkdGg9IjEiIGhlaWdodD0iMSIgeD0iNCIgeT0iMyIgZmlsbD0id2hpdGUiPjwvcmVjdD48cmVjdCB3aWR0aD0iMSIgaGVpZ2h0PSIxLjUiIHg9IjQiIHk9IjMiIGZpbGw9IndoaXRlIj48L3JlY3Q+PHJlY3Qgd2lkdGg9IjEuNSIgaGVpZ2h0PSIxIiB4PSIyIiB5PSI0IiBmaWxsPSJ3aGl0ZSI+PC9yZWN0PjxyZWN0IHdpZHRoPSIxIiBoZWlnaHQ9IjEuNSIgeD0iMiIgeT0iNCIgZmlsbD0id2hpdGUiPjwvcmVjdD48cmVjdCB3aWR0aD0iMS41IiBoZWlnaHQ9IjEiIHg9IjMiIHk9IjQiIGZpbGw9IndoaXRlIj48L3JlY3Q+PHJlY3Qgd2lkdGg9IjEiIGhlaWdodD0iMSIgeD0iNCIgeT0iNCIgZmlsbD0id2hpdGUiPjwvcmVjdD48cmVjdCB3aWR0aD0iMS41IiBoZWlnaHQ9IjEiIHg9IjEiIHk9IjUiIGZpbGw9IndoaXRlIj48L3JlY3Q+PHJlY3Qgd2lkdGg9IjEiIGhlaWdodD0iMSIgeD0iMiIgeT0iNSIgZmlsbD0id2hpdGUiPjwvcmVjdD48cmVjdCB3aWR0aD0iMSIgaGVpZ2h0PSIxIiB4PSI1IiB5PSI1IiBmaWxsPSJ3aGl0ZSI+PC9yZWN0Pjwvc3ZnPgo=)

### Figure 28. ArUco marker `XR_SPATIAL_MARKER_ARUCO_DICT_5X5_50_EXT` with ID 43

## Example Code

### Configure QR Code Tracking Capability

The following example code demonstrates how to configure the QR code tracking capability when creating a spatial context.

    // Check if marker tracking capability is supported
    uint32_t capabilityCount;
    CHK_XR(xrEnumerateSpatialCapabilitiesEXT(instance, systemId, 0, &capabilityCount, nullptr));
    std::vector<XrSpatialCapabilityEXT> capabilities(capabilityCount);
    CHK_XR(xrEnumerateSpatialCapabilitiesEXT(instance, systemId, capabilityCount, &capabilityCount, capabilities.data()));

    if (std::find(capabilities.begin(), capabilities.end(), XR_SPATIAL_CAPABILITY_MARKER_TRACKING_QR_CODE_EXT) == capabilities.end()) {
      return;
    }

    uint32_t featureCount = 0;
    CHK_XR(xrEnumerateSpatialCapabilityFeaturesEXT(instance, systemId, XR_SPATIAL_CAPABILITY_MARKER_TRACKING_QR_CODE_EXT, 0, &featureCount, nullptr));
    std::vector<XrSpatialCapabilityFeatureEXT> capabilityFeatures(featureCount);
    CHK_XR(xrEnumerateSpatialCapabilityFeaturesEXT(instance, systemId, XR_SPATIAL_CAPABILITY_MARKER_TRACKING_QR_CODE_EXT, featureCount, &featureCount, capabilityFeatures.data()));

    bool supportsFixedMarkerSize = std::find(capabilityFeatures.begin(), capabilityFeatures.end(), XR_SPATIAL_CAPABILITY_FEATURE_MARKER_TRACKING_FIXED_SIZE_MARKERS_EXT) != capabilityFeatures.end();

    // Create a spatial context
    XrSpatialContextEXT spatialContext{};

    // Enable the 2 guaranteed components of the qr code tracking capability
    std::vector<XrSpatialComponentTypeEXT> enabledComponents = {
      XR_SPATIAL_COMPONENT_TYPE_BOUNDED_2D_EXT,
      XR_SPATIAL_COMPONENT_TYPE_MARKER_EXT,
    };
    XrSpatialCapabilityConfigurationQrCodeEXT markerConfiguration{XR_TYPE_SPATIAL_CAPABILITY_CONFIGURATION_QR_CODE_EXT};
    markerConfiguration.capability = XR_SPATIAL_CAPABILITY_MARKER_TRACKING_QR_CODE_EXT;
    markerConfiguration.enabledComponentCount = static_cast<uint32_t>(enabledComponents.size());
    markerConfiguration.enabledComponents = enabledComponents.data();

    // only chained if features.markerSideLength is true.
    XrSpatialMarkerSizeEXT markerSize{XR_TYPE_SPATIAL_MARKER_SIZE_EXT};
    markerSize.markerSideLength = 0.10f;
    if (supportsFixedMarkerSize) {
      markerConfiguration.next = &markerSize;
    }


    std::array<XrSpatialCapabilityConfigurationBaseHeaderEXT*, 1> capabilityConfigs = {
      reinterpret_cast<XrSpatialCapabilityConfigurationBaseHeaderEXT*>(&markerConfiguration),
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

    // ...
    // Discovery entities with the spatial context
    // ...

    CHK_XR(xrDestroySpatialContextEXT(spatialContext));

### Discover Spatial Entities \& Query Component Data

The following example code demonstrates how to discover spatial entities for a context configured with `XR_SPATIAL_CAPABILITY_MARKER_TRACKING_QR_CODE_EXT` and query its component data.

    XrFutureEXT future = XR_NULL_FUTURE_EXT;

    // We want to look for entities that have the following components.
    std::vector<XrSpatialComponentTypeEXT> snapshotComponents = {
      XR_SPATIAL_COMPONENT_TYPE_BOUNDED_2D_EXT,
      XR_SPATIAL_COMPONENT_TYPE_MARKER_EXT,
    };

    auto discoverSpatialEntities = [&](XrSpatialContextEXT spatialContext, XrTime time) {
      XrSpatialDiscoverySnapshotCreateInfoEXT snapshotCreateInfo{XR_TYPE_SPATIAL_DISCOVERY_SNAPSHOT_CREATE_INFO_EXT};
      snapshotCreateInfo.componentTypeCount = snapshotComponents.size();
      snapshotCreateInfo.componentTypes = snapshotComponents.data();
      CHK_XR(xrCreateSpatialDiscoverySnapshotAsyncEXT(spatialContext, &snapshotCreateInfo, &future));

      waitUntilReady(future);

      XrCreateSpatialDiscoverySnapshotCompletionInfoEXT completionInfo{XR_TYPE_CREATE_SPATIAL_DISCOVERY_SNAPSHOT_COMPLETION_INFO_EXT};
      completionInfo.baseSpace = localSpace;
      completionInfo.time = time;
      completionInfo.future = future;

      XrCreateSpatialDiscoverySnapshotCompletionEXT completion{XR_TYPE_CREATE_SPATIAL_DISCOVERY_SNAPSHOT_COMPLETION_EXT};
      CHK_XR(xrCreateSpatialDiscoverySnapshotCompleteEXT(spatialContext, &completionInfo, &completion));
      if (completion.futureResult == XR_SUCCESS) {

        // Query for the bounded2D and marker component data
        XrSpatialComponentDataQueryConditionEXT queryCond{XR_TYPE_SPATIAL_COMPONENT_DATA_QUERY_CONDITION_EXT};
        queryCond.componentTypeCount = snapshotComponents.size();
        queryCond.componentTypes = snapshotComponents.data();

        XrSpatialComponentDataQueryResultEXT queryResult{XR_TYPE_SPATIAL_COMPONENT_DATA_QUERY_RESULT_EXT};
        CHK_XR(xrQuerySpatialComponentDataEXT(completion.snapshot, &queryCond, &queryResult));

        std::vector<XrSpatialEntityIdEXT> entityIds(queryResult.entityIdCountOutput);
        std::vector<XrSpatialEntityTrackingStateEXT> entityStates(queryResult.entityIdCountOutput);
        queryResult.entityIdCapacityInput = entityIds.size();
        queryResult.entityIds = entityIds.data();
        queryResult.entityStateCapacityInput = entityStates.size();
        queryResult.entityStates = entityStates.data();

        std::vector<XrSpatialBounded2DDataEXT> bounded2D(queryResult.entityIdCountOutput);
        XrSpatialComponentBounded2DListEXT bounded2DList{XR_TYPE_SPATIAL_COMPONENT_BOUNDED_2D_LIST_EXT};
        bounded2DList.boundCount = bounded2D.size();
        bounded2DList.bounds = bounded2D.data();
        queryResult.next = &bounded2DList;

        std::vector<XrSpatialMarkerDataEXT> markers;
        XrSpatialComponentMarkerListEXT markerList{XR_TYPE_SPATIAL_COMPONENT_MARKER_LIST_EXT};
        markers.resize(queryResult.entityIdCountOutput);
        markerList.markerCount = markers.size();
        markerList.markers = markers.data();
        bounded2DList.next = &markerList;

        CHK_XR(xrQuerySpatialComponentDataEXT(completion.snapshot, &queryCond, &queryResult));

        for (int32_t i = 0; i < queryResult.entityIdCountOutput; ++i) {
          if (entityStates[i] != XR_SPATIAL_ENTITY_TRACKING_STATE_TRACKING_EXT) {
            continue;
          }

          // 2D bounds for entity entityIds[i] is bounded2D[i].extents centered on bounded2D[i].center.

          if (markers[i].capability == XR_SPATIAL_CAPABILITY_MARKER_TRACKING_QR_CODE_EXT) {
            // Check if marker data has been decoded.
            if (markers[i].data.bufferId != XR_NULL_SPATIAL_BUFFER_ID_EXT) {
              if (markers[i].data.bufferType == XR_SPATIAL_BUFFER_TYPE_STRING_EXT) {
                // Qr Code data can be queried using
                // XrSpatialBufferGetInfoEXT getInfo{XR_TYPE_SPATIAL_BUFFER_GET_INFO_EXT};
                // info.bufferId = markers[i].data.bufferId;
                // xrGetSpatialBufferStringEXT(completion.snapshot, &getInfo, ...)
              } else if (markers[i].data.bufferType == XR_SPATIAL_BUFFER_TYPE_UINT8_EXT) {
                // Qr Code data can be queried using
                // XrSpatialBufferGetInfoEXT getInfo{XR_TYPE_SPATIAL_BUFFER_GET_INFO_EXT};
                // info.bufferId = markers[i].data.bufferId;
                // xrGetSpatialBufferUint8(completion.snapshot, &getInfo, ...)
              }
            }
          }
        }

        CHK_XR(xrDestroySpatialSnapshotEXT(completion.snapshot));
      }
    };

    while (1) {
      // ...
      // For every frame in frame loop
      // ...

      XrFrameState frameState;  // previously returned from xrWaitFrame
      const XrTime time = frameState.predictedDisplayTime;

      // Poll for the XR_TYPE_EVENT_DATA_SPATIAL_DISCOVERY_RECOMMENDED_EXT event
      XrEventDataBuffer event = {XR_TYPE_EVENT_DATA_BUFFER};
      XrResult result = xrPollEvent(instance, &event);
      if (result == XR_SUCCESS) {
          switch (event.type) {
              case XR_TYPE_EVENT_DATA_SPATIAL_DISCOVERY_RECOMMENDED_EXT: {
                  const XrEventDataSpatialDiscoveryRecommendedEXT& eventdata =
                      *reinterpret_cast<XrEventDataSpatialDiscoveryRecommendedEXT*>(&event);
                  // Discover spatial entities for the context that we received the "discovery
                  // recommended" event for.
                  discoverSpatialEntities(eventdata.spatialContext, time);
                  break;
              }
          }
      }

      // ...
      // Finish frame loop
      // ...
    }

## New Structures

- [XrSpatialCapabilityConfigurationAprilTagEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialCapabilityConfigurationAprilTagEXT)
- [XrSpatialCapabilityConfigurationArucoMarkerEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialCapabilityConfigurationArucoMarkerEXT)
- [XrSpatialCapabilityConfigurationMicroQrCodeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialCapabilityConfigurationMicroQrCodeEXT)
- [XrSpatialCapabilityConfigurationQrCodeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialCapabilityConfigurationQrCodeEXT)
- [XrSpatialMarkerDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialMarkerDataEXT)
- Extending [XrSpatialCapabilityConfigurationArucoMarkerEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialCapabilityConfigurationArucoMarkerEXT) , [XrSpatialCapabilityConfigurationAprilTagEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialCapabilityConfigurationAprilTagEXT) , [XrSpatialCapabilityConfigurationQrCodeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialCapabilityConfigurationQrCodeEXT) , [XrSpatialCapabilityConfigurationMicroQrCodeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialCapabilityConfigurationMicroQrCodeEXT) :

  - [XrSpatialMarkerSizeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialMarkerSizeEXT)
  - [XrSpatialMarkerStaticOptimizationEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialMarkerStaticOptimizationEXT)
- Extending [XrSpatialComponentDataQueryResultEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryResultEXT) :

  - [XrSpatialComponentMarkerListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialComponentMarkerListEXT)

## New Enums

- [XrSpatialMarkerAprilTagDictEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialMarkerAprilTagDictEXT)
- [XrSpatialMarkerArucoDictEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking#XrSpatialMarkerArucoDictEXT)

## New Enum Constants

- `XR_EXT_SPATIAL_MARKER_TRACKING_EXTENSION_NAME`
- `XR_EXT_spatial_marker_tracking_SPEC_VERSION`
- Extending [XrSpatialCapabilityEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityEXT) :

  - `XR_SPATIAL_CAPABILITY_MARKER_TRACKING_APRIL_TAG_EXT`
  - `XR_SPATIAL_CAPABILITY_MARKER_TRACKING_ARUCO_MARKER_EXT`
  - `XR_SPATIAL_CAPABILITY_MARKER_TRACKING_MICRO_QR_CODE_EXT`
  - `XR_SPATIAL_CAPABILITY_MARKER_TRACKING_QR_CODE_EXT`
- Extending [XrSpatialCapabilityFeatureEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityFeatureEXT) :

  - `XR_SPATIAL_CAPABILITY_FEATURE_MARKER_TRACKING_FIXED_SIZE_MARKERS_EXT`
  - `XR_SPATIAL_CAPABILITY_FEATURE_MARKER_TRACKING_STATIC_MARKERS_EXT`
- Extending [XrSpatialComponentTypeEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentTypeEXT) :

  - `XR_SPATIAL_COMPONENT_TYPE_MARKER_EXT`
- Extending [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) :

  - `XR_TYPE_SPATIAL_CAPABILITY_CONFIGURATION_APRIL_TAG_EXT`
  - `XR_TYPE_SPATIAL_CAPABILITY_CONFIGURATION_ARUCO_MARKER_EXT`
  - `XR_TYPE_SPATIAL_CAPABILITY_CONFIGURATION_MICRO_QR_CODE_EXT`
  - `XR_TYPE_SPATIAL_CAPABILITY_CONFIGURATION_QR_CODE_EXT`
  - `XR_TYPE_SPATIAL_COMPONENT_MARKER_LIST_EXT`
  - `XR_TYPE_SPATIAL_MARKER_SIZE_EXT`
  - `XR_TYPE_SPATIAL_MARKER_STATIC_OPTIMIZATION_EXT`

## Version History

- Revision 1, 2024-07-29 (Ron Bessems, Meta)

  - Initial extension description