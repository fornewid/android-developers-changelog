---
title: https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_qr_code
url: https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_qr_code
source: md.txt
---

### XR_ANDROID_trackables_qr_code

**Name String**

`XR_ANDROID_trackables_qr_code`

**Extension Type**

Instance extension

**Registered Extension Number**

709

**Revision**

1

**Ratification Status**

Not ratified

**Extension and Version Dependencies**

`XR_ANDROID_trackables`

**Deprecation State**

- *Deprecated* by `XR_EXT_spatial_marker_tracking` extension

**Last Modified Date**

2025-02-05

**IP Status**

No known IP claims.

**Contributors**

Christopher Doer, Google  

Levana Chen, Google  

Jared Finder, Google  

Spencer Quin, Google  

Nihav Jain, Google  

Diego Tipaldi, Google  

Ken Mackay, Google  

Daniel Guttenberg, Qualcomm

## Overview

This extension enables physical QR code tracking and QR code data decoding.

### Permissions

Android applications **must** have the android.permission.SCENE_UNDERSTANDING_COARSE permission listed in their manifest as this extension depends on `XR_ANDROID_trackables` and exposes the geometry of the environment. The android.permission.SCENE_UNDERSTANDING_COARSE permission is considered a dangerous permission.

(protection level: dangerous)

## Inspect system capability

The [XrSystemQrCodeTrackingPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_qr_code#XrSystemQrCodeTrackingPropertiesANDROID) structure is defined as:

    typedef struct XrSystemQrCodeTrackingPropertiesANDROID {
        XrStructureType    type;
        void*              next;
        XrBool32           supportsQrCodeTracking;
        XrBool32           supportsQrCodeSizeEstimation;
        uint16_t           maxQrCodeCount;
    } XrSystemQrCodeTrackingPropertiesANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.
- `supportsQrCodeTracking` is an `XrBool32` indicating if current system provides QR code tracking capability.
- `supportsQrCodeSizeEstimation` is an `XrBool32` indicating if current system provides QR code size estimation.
- `maxQrCodeCount` is the total maximum number of QR codes that **can** be tracked at the same time.

An application **can** inspect whether the system is capable of QR code tracking by extending the [XrSystemProperties](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSystemProperties) with [XrSystemQrCodeTrackingPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_qr_code#XrSystemQrCodeTrackingPropertiesANDROID) structure when calling [xrGetSystemProperties](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrGetSystemProperties) . The runtime **must** return `XR_ERROR_FEATURE_UNSUPPORTED` for QR code tracker creation if and only if `supportsQrCodeTracking` is `XR_FALSE` .

If a runtime supports QR code tracking, `maxQrCodeCount` **must** be at least 1. If a runtime does not support QR code tracking, `maxQrCodeCount` **must** be 0.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_qr_code#VUID-XrSystemQrCodeTrackingPropertiesANDROID-extension-notenabled) The `XR_ANDROID_trackables_qr_code` extension **must** be enabled prior to using [XrSystemQrCodeTrackingPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_qr_code#XrSystemQrCodeTrackingPropertiesANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_qr_code#VUID-XrSystemQrCodeTrackingPropertiesANDROID-type-type) `type` **must** be `XR_TYPE_SYSTEM_QR_CODE_TRACKING_PROPERTIES_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_qr_code#VUID-XrSystemQrCodeTrackingPropertiesANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)

## Tracking QR codes

This extension adds `XR_TRACKABLE_TYPE_QR_CODE_ANDROID` to [XrTrackableTypeANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackableTypeANDROID) .

The application **may** create an [XrTrackableTrackerANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackableTrackerANDROID) by calling [xrCreateTrackableTrackerANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateTrackableTrackerANDROID) and specifying `XR_TRACKABLE_TYPE_QR_CODE_ANDROID` as the trackable type in [XrTrackableTrackerCreateInfoANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackableTrackerCreateInfoANDROID) :: `trackableType` to track QR codes.

The runtime **must** return `XR_ERROR_FEATURE_UNSUPPORTED` if [XrTrackableTrackerCreateInfoANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackableTrackerCreateInfoANDROID) :: `trackableType` is `XR_TRACKABLE_TYPE_QR_CODE_ANDROID` and [XrSystemQrCodeTrackingPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_qr_code#XrSystemQrCodeTrackingPropertiesANDROID) :: `supportsQrCodeTracking` returns `XR_FALSE` via [xrGetSystemProperties](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrGetSystemProperties) .

The [XrTrackableQrCodeConfigurationANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_qr_code#XrTrackableQrCodeConfigurationANDROID) structure is defined as:

    typedef struct XrTrackableQrCodeConfigurationANDROID {
        XrStructureType                type;
        void*                          next;
        XrQrCodeTrackingModeANDROID    trackingMode;
        float                          qrCodeEdgeSize;
    } XrTrackableQrCodeConfigurationANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.
- `trackingMode` is an [XrQrCodeTrackingModeANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_qr_code#XrQrCodeTrackingModeANDROID) indicating the desired mode for tracking.
- `qrCodeEdgeSize` indicates the size of the QR code edge in meters. If zero, the runtime estimates the QR code size online.

The application **must** set a valid configuration by adding a [XrTrackableQrCodeConfigurationANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_qr_code#XrTrackableQrCodeConfigurationANDROID) to the next chain of [XrTrackableTrackerCreateInfoANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackableTrackerCreateInfoANDROID) . Otherwise, the runtime **must** return `XR_ERROR_VALIDATION_FAILURE` .

If the runtime supports QR code size estimation, the application **may** set [XrTrackableQrCodeConfigurationANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_qr_code#XrTrackableQrCodeConfigurationANDROID) :: `qrCodeEdgeSize` to `0.0` to indicate the usage of size estimation.

If the runtime does not support QR code size estimation, the application **must** set [XrTrackableQrCodeConfigurationANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_qr_code#XrTrackableQrCodeConfigurationANDROID) :: `qrCodeEdgeSize` to a positive value, otherwise the runtime **must** return `XR_ERROR_VALIDATION_FAILURE` .

The runtime **must** filter the output from [xrGetAllTrackablesANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrGetAllTrackablesANDROID) to match the `trackingMode` . If [XrTrackableQrCodeConfigurationANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_qr_code#XrTrackableQrCodeConfigurationANDROID) :: `qrCodeEdgeSize` is not set to `0.0` the runtime **must** only return QR codes that match this size. If [XrTrackableQrCodeConfigurationANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_qr_code#XrTrackableQrCodeConfigurationANDROID) :: `qrCodeEdgeSize` is set to `0.0` the runtime **must** return all QR codes with estimated size.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_qr_code#VUID-XrTrackableQrCodeConfigurationANDROID-extension-notenabled) The `XR_ANDROID_trackables_qr_code` extension **must** be enabled prior to using [XrTrackableQrCodeConfigurationANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_qr_code#XrTrackableQrCodeConfigurationANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_qr_code#VUID-XrTrackableQrCodeConfigurationANDROID-type-type) `type` **must** be `XR_TYPE_TRACKABLE_QR_CODE_CONFIGURATION_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_qr_code#VUID-XrTrackableQrCodeConfigurationANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains) . See also: [XrTrackableQrCodeVersionFilterQCOM](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackableQrCodeVersionFilterQCOM)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_qr_code#VUID-XrTrackableQrCodeConfigurationANDROID-trackingMode-parameter) `trackingMode` **must** be a valid [XrQrCodeTrackingModeANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_qr_code#XrQrCodeTrackingModeANDROID) value

The [XrQrCodeTrackingModeANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_qr_code#XrQrCodeTrackingModeANDROID) enum describes the supported tracking modes of QR codes.

    typedef enum XrQrCodeTrackingModeANDROID {
        XR_QR_CODE_TRACKING_MODE_DYNAMIC_ANDROID = 0,
        XR_QR_CODE_TRACKING_MODE_STATIC_ANDROID = 1,
        XR_QR_CODE_TRACKING_MODE_ANCHORED_QCOM = 1000314000,
        XR_QR_CODE_TRACKING_MODE_MAX_ENUM_ANDROID = 0x7FFFFFFF
    } XrQrCodeTrackingModeANDROID;

### Enumerant Descriptions

- `XR_QR_CODE_TRACKING_MODE_DYNAMIC_ANDROID` --- Tracking dynamic QR codes. This mode has the highest accuracy and works on moving and static QR codes, but also has the highest power consumption.
- `XR_QR_CODE_TRACKING_MODE_STATIC_ANDROID` --- Tracking static QR codes. This mode is primarily useful for QR codes that are known to be static, which leads to less power consumption in comparison to the dynamic mode.
- `XR_QR_CODE_TRACKING_MODE_ANCHORED_QCOM` --- This mode should be used for QR codes that are static. Contrary to the static mode, this mode will track the QR code only once and then updates positions of tracked instances solely based on the device's position. As a result, tracking continues even if the QR code goes out of view of the reference frame. This leads to minimal power consumption once the QR code has been tracked. (Added by the `XR_QCOM_trackables_qr_code_operations` extension)

## Get QR codes

The [xrGetTrackableQrCodeANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_qr_code#xrGetTrackableQrCodeANDROID) function is defined as:

    XrResult xrGetTrackableQrCodeANDROID(
        XrTrackableTrackerANDROID                   tracker,
        const XrTrackableGetInfoANDROID*            getInfo,
        XrTrackableQrCodeANDROID*                   qrCodeOutput);

### Parameter Descriptions

- `tracker` is the [XrTrackableTrackerANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackableTrackerANDROID) to query.
- `getInfo` is the [XrTrackableGetInfoANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackableGetInfoANDROID) with the information used to get the trackable QR code.
- `qrCodeOutput` is a pointer to the [XrTrackableQrCodeANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_qr_code#XrTrackableQrCodeANDROID) structure in which the trackable QR code is returned.

The runtime **must** return `XR_ERROR_MISMATCHING_TRACKABLE_TYPE_ANDROID` if the trackable type of the `XrTrackableANDROID` is not `XR_TRACKABLE_TYPE_QR_CODE_ANDROID` , or if the trackable type of the [XrTrackableTrackerANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackableTrackerANDROID) is not `XR_TRACKABLE_TYPE_QR_CODE_ANDROID` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_qr_code#VUID-xrGetTrackableQrCodeANDROID-extension-notenabled) The `XR_ANDROID_trackables_qr_code` extension **must** be enabled prior to calling [xrGetTrackableQrCodeANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_qr_code#xrGetTrackableQrCodeANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_qr_code#VUID-xrGetTrackableQrCodeANDROID-tracker-parameter) `tracker` **must** be a valid [XrTrackableTrackerANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackableTrackerANDROID) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_qr_code#VUID-xrGetTrackableQrCodeANDROID-getInfo-parameter) `getInfo` **must** be a pointer to a valid [XrTrackableGetInfoANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackableGetInfoANDROID) structure
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_qr_code#VUID-xrGetTrackableQrCodeANDROID-qrCodeOutput-parameter) `qrCodeOutput` **must** be a pointer to an [XrTrackableQrCodeANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_qr_code#XrTrackableQrCodeANDROID) structure

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
- `XR_ERROR_SIZE_INSUFFICIENT`
- `XR_ERROR_TIME_INVALID`
- `XR_ERROR_VALIDATION_FAILURE`

The [XrTrackableQrCodeANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_qr_code#XrTrackableQrCodeANDROID) structure is defined as:

    typedef struct XrTrackableQrCodeANDROID {
        XrStructureType           type;
        void*                     next;
        XrTrackingStateANDROID    trackingState;
        XrTime                    lastUpdatedTime;
        XrPosef                   centerPose;
        XrExtent2Df               extents;
        uint32_t                  bufferCapacityInput;
        uint32_t                  bufferCountOutput;
        char*                     buffer;
    } XrTrackableQrCodeANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.
- `trackingState` is the [XrTrackingStateANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackingStateANDROID) of the QR code.
- `lastUpdatedTime` is the `XrTime` of the last update of the QR code. If `lastUpdatedTime` is changed from the last call, all other fields **may** have changed.
- `centerPose` is the [XrPosef](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrPosef) of the QR code located in [XrTrackableGetInfoANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackableGetInfoANDROID) :: `baseSpace` . The QR code lies in the XZ plane with X pointing to the right of the QR code, Z pointing to its bottom and Y coming out of the QR code as the normal.
- `extents` is the [XrExtent2Df](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrExtent2Df) dimensions of the QR code. The boundary of the bounding box is at points: `centerPose` +/- ( `extents` / 2).
- `bufferCapacityInput` is the capability of the `buffer` , or `0` to retrieve the required capability.
- `bufferCountOutput` If the `bufferCapacityInput` is `0` , the runtime will write the required buffer size into `bufferCountOutput` . Otherwise, it contains the total elements written in `buffer` . If the QR code data has not been decoded yet, the runtime **must** set bufferCountOutput to 0.
- `buffer` is a pointer to an array of `char` to write the decoded QR code data. If the application does not care about the decoded QR code data it **can** pass `nullptr` and omit the second two-call call. The QR code data is returned as null-terminated UTF-8 string.
- See the [Buffer Size Parameters](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-buffer-size-parameters) section for a detailed description of retrieving the required `buffer` size.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_qr_code#VUID-XrTrackableQrCodeANDROID-extension-notenabled) The `XR_ANDROID_trackables_qr_code` extension **must** be enabled prior to using [XrTrackableQrCodeANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_qr_code#XrTrackableQrCodeANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_qr_code#VUID-XrTrackableQrCodeANDROID-type-type) `type` **must** be `XR_TYPE_TRACKABLE_QR_CODE_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_qr_code#VUID-XrTrackableQrCodeANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains) . See also: [XrTrackableQrCodeVersionQCOM](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackableQrCodeVersionQCOM)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_qr_code#VUID-XrTrackableQrCodeANDROID-trackingState-parameter) `trackingState` **must** be a valid [XrTrackingStateANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackingStateANDROID) value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_qr_code#VUID-XrTrackableQrCodeANDROID-buffer-parameter) If `bufferCapacityInput` is not `0` , `buffer` **must** be a pointer to an array of `bufferCapacityInput` char values

## Example code for getting trackable QR codes

The following example code demonstrates how to get trackable QR codes.

    XrInstance instance; // previously initialized
    XrSystemId systemId; // previously initialized
    XrSession session;   // previously initialized

    // The function pointers are previously initialized using xrGetInstanceProcAddr.
    PFN_xrGetSystemProperties xrGetSystemProperties;                       // previously initialized
    PFN_xrCreateTrackableTrackerANDROID xrCreateTrackableTrackerANDROID;   // previously initialized
    PFN_xrGetAllTrackablesANDROID xrGetAllTrackablesANDROID;               // previously initialized
    PFN_xrGetTrackableQrCodeANDROID xrGetTrackableQrCodeANDROID;           // previously initialized
    PFN_xrDestroyTrackableTrackerANDROID xrDestroyTrackableTrackerANDROID; // previously initialized

    XrTime updateTime; // Time used for the current frame's simulation update.
    XrSpace appSpace;  // Space created for XR_REFERENCE_SPACE_TYPE_LOCAL.

    // Inspect system capability
    XrSystemQrCodeTrackingPropertiesANDROID qrCodeProperty {
      .type = XR_TYPE_SYSTEM_QR_CODE_TRACKING_PROPERTIES_ANDROID,
      .next = nullptr,
    };
    XrSystemProperties systemProperties {
      .type = XR_TYPE_SYSTEM_PROPERTIES,
      .next = &qrCodeProperty,
    };
    CHK_XR(xrGetSystemProperties(instance, systemId, &systemProperties));
    if (!qrCodeProperty.supportsQrCodeTracking) {
        // QR code tracking is not supported.
        return;
    }

    // Create a trackable tracker for QR code tracking.
    // If the runtime does not support size estimation, configures QR code edge size of 0.1m.
    XrTrackableQrCodeConfigurationANDROID configuration {
      .type = XR_TYPE_TRACKABLE_QR_CODE_CONFIGURATION_ANDROID,
      .next = nullptr,
      .trackingMode = XR_QR_CODE_TRACKING_MODE_DYNAMIC_ANDROID,
      .qrCodeEdgeSize = qrCodeProperty.supportsQrCodeSizeEstimation ? 0.0f : 0.1f,
    };
    XrTrackableTrackerCreateInfoANDROID createInfo {
      .type = XR_TYPE_TRACKABLE_TRACKER_CREATE_INFO_ANDROID,
      .next = &configuration,
      .trackableType = XR_TRACKABLE_TYPE_QR_CODE_ANDROID
    };
    XrTrackableTrackerANDROID qrCodeTracker;
    auto res = xrCreateTrackableTrackerANDROID(session, &createInfo, &qrCodeTracker);
    if (res == XR_ERROR_PERMISSION_INSUFFICIENT) {
        // Handle permission requests.
    }
    CHK_XR(res);

    // Get QR codes.
    std::vector<XrTrackableANDROID> trackables(qrCodeProperty.maxQrCodeCount);
    std::vector<XrTrackableQrCodeANDROID> qrCodes(qrCodeProperty.maxQrCodeCount, {
      .type = XR_TYPE_TRACKABLE_QR_CODE_ANDROID,
      .next = nullptr,
      .bufferCountOutput = 0,
    });
    uint32_t qrCodeSize = 0;
    CHK_XR(xrGetAllTrackablesANDROID(qrCodeTracker, qrCodeProperty.maxQrCodeCount, &qrCodeSize,
                                     trackables.data()));
    for (int i = 0; i < qrCodeSize; i++) {
        XrTrackableGetInfoANDROID getInfo {
          .type = XR_TYPE_TRACKABLE_GET_INFO_ANDROID,
          .next = nullptr,
          .trackable = trackables.at(i),
          .baseSpace = appSpace,
          .time = updateTime,
        };
        CHK_XR(xrGetTrackableQrCodeANDROID(qrCodeTracker, &getInfo, &qrCodes[i]));
        if (qrCodes[i].bufferCountOutput > 0) {
            // Allocate the buffer if it is not already allocated.
            if (qrCodes[i].bufferCapacityInput == 0) {
                qrCodes[i].buffer = new char[qrCodes[i].bufferCountOutput];
                qrCodes[i].bufferCapacityInput = qrCodes[i].bufferCountOutput;
                CHK_XR(xrGetTrackableQrCodeANDROID(qrCodeTracker, &getInfo, &qrCodes[i]));
            }
        }
    }

    // Release trackable tracker.
    CHK_XR(xrDestroyTrackableTrackerANDROID(qrCodeTracker));

## New Commands

- [xrGetTrackableQrCodeANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_qr_code#xrGetTrackableQrCodeANDROID)

## New Structures

- [XrTrackableQrCodeANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_qr_code#XrTrackableQrCodeANDROID)
- Extending [XrSystemProperties](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSystemProperties) :

  - [XrSystemQrCodeTrackingPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_qr_code#XrSystemQrCodeTrackingPropertiesANDROID)
- Extending [XrTrackableTrackerCreateInfoANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackableTrackerCreateInfoANDROID) :

  - [XrTrackableQrCodeConfigurationANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_qr_code#XrTrackableQrCodeConfigurationANDROID)

## New Enums

- [XrQrCodeTrackingModeANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_qr_code#XrQrCodeTrackingModeANDROID)

## New Enum Constants

- `XR_ANDROID_TRACKABLES_QR_CODE_EXTENSION_NAME`
- `XR_ANDROID_trackables_qr_code_SPEC_VERSION`
- Extending [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) :

  - `XR_TYPE_SYSTEM_QR_CODE_TRACKING_PROPERTIES_ANDROID`
  - `XR_TYPE_TRACKABLE_QR_CODE_ANDROID`
  - `XR_TYPE_TRACKABLE_QR_CODE_CONFIGURATION_ANDROID`
- Extending [XrTrackableTypeANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackableTypeANDROID) :

  - `XR_TRACKABLE_TYPE_QR_CODE_ANDROID`

## Issues

## Version History

- Revision 1, 2025-02-05 (Levana Chen)

  - Initial extension description.