---
title: https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_qr_code
url: https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_qr_code
source: md.txt
---

**Name String**

`XR_ANDROID_trackables_qr_code`

**Extension Type**

Instance extension

**Registered Extension Number**

460

**Revision**

1

**Extension and Version Dependencies**

[`XR_ANDROID_trackables`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables)

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

This extension enables physical QR Code tracking and QR Code data decoding.

> [!CAUTION]
> **Permissions**   
>
> Android applications **must** have the \`android.permission.SCENE_UNDERSTANDING\` permission listed in their manifest as this extension depends on \`XR_ANDROID_trackables\` and exposes the geometry of the environment. The \`android.permission.SCENE_UNDERSTANDING\` permission is considered a dangerous permission.   
> (protection level: dangerous)

## Inspect system capability

### XrSystemQrCodeTrackingPropertiesANDROID

The `XrSystemQrCodeTrackingPropertiesANDROID` structure is defined as:

    typedef struct XrSystemQrCodeTrackingPropertiesANDROID {
        XrStructureType    type;
        void*              next;
        XrBool32           supportsQrCodeTracking;
        XrBool32           supportsQrCodeSizeEstimation;
        uint32_t           maxQrCodeCount;
    } XrSystemQrCodeTrackingPropertiesANDROID;

#### Member Descriptions

- `type` is the [`XrStructureType`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.
- `supportsQrCodeTracking` is an [`XrBool32`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrBool32) indicating if current system provides QR Code tracking capability.
- `supportsQrCodeSizeEstimation` is an [`XrBool32`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrBool32) indicating if current system provides QR Code size estimation.
- `maxQrCodeCount` is the total maximum number of QR Codes that can be tracked at the same time.

An application can inspect whether the system is capable of QR Code
tracking by extending the [`XrSystemProperties`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSystemProperties) with
`XrSystemQrCodeTrackingPropertiesANDROID` structure when calling
[`xrGetSystemProperties`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrGetSystemProperties).
The runtime **must** return `XR_ERROR_FEATURE_UNSUPPORTED` for QR Code
tracker creation if and only if `supportsQrCodeTracking` is
`XR_FALSE`.

If a runtime supports QR Code tracking, it **must** support
`maxQrCodeCount` tracked QR Codes at any given time.

If a runtime supports QR Code size estimation, the application can set
`XrTrackableQrCodeConfigurationANDROID::qrCodeEdgeSize` `0` to
indicate the usage of size estimation.
Otherwise, the application **must** set
`XrTrackableQrCodeConfigurationANDROID::qrCodeEdgeSize` to a
positive value or `XR_ERROR_VALIDATION_FAILURE` will be returned.

#### Valid Usage (Implicit)

- The `XR_ANDROID_trackables_qr_code` extension **must** be enabled prior to using `XrSystemQrCodeTrackingPropertiesANDROID`
- `type` **must** be `XR_TYPE_SYSTEM_QR_CODE_TRACKING_PROPERTIES_ANDROID`
- `next` **must** be `NULL` or a valid pointer to the next structure in a structure chain

## Tracking QR Codes

This extension adds `XR_TRACKABLE_TYPE_QR_CODE_ANDROID` to
[`XrTrackableTypeANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables#XrTrackableTypeANDROID).

The application **may** create an [`XrTrackableTrackerANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables#XrTrackableTrackerANDROID) by calling
[`xrCreateTrackableTrackerANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables#xrCreateTrackableTrackerANDROID) and specifying
`XR_TRACKABLE_TYPE_QR_CODE_ANDROID` as the trackable type in
`XrTrackableTrackerCreateInfoANDROID::trackableType` to track QR
codes.

The runtime **must** return `XR_ERROR_FEATURE_UNSUPPORTED` if
`XrTrackableTrackerCreateInfoANDROID::trackableType` is
`XR_TRACKABLE_TYPE_QR_CODE_ANDROID` and
`XrSystemQrCodeTrackingPropertiesANDROID::supportsQrCodeTracking`
returns `XR_FALSE` via `xrGetSystemProperties`.

### XrTrackableQrCodeConfigurationANDROID

The `XrTrackableQrCodeConfigurationANDROID` structure is defined as:

    typedef struct XrTrackableQrCodeConfigurationANDROID {
        XrStructureType               type;
        const void*                   next;
        XrQrCodeTrackingModeANDROID   trackingMode;
        float                         qrCodeEdgeSize;
    } XrTrackableQrCodeConfigurationANDROID;

#### Member Descriptions

- `type` is the [`XrStructureType`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.
- `trackingMode` is an `XrQrCodeTrackingModeANDROID` indicating the desired mode for tracking.
- `qrCodeEdgeSize` indicates the size of the QR Code edge in meters. If zero, the QR Code size will be estimated online.

The application **must** set a valid configuration by adding a
`XrTrackableQrCodeConfigurationANDROID` to the next chain of
`XrTrackableTrackerCreateInfoANDROID`.
Otherwise, the runtime **must** return `XR_ERROR_VALIDATION_FAILURE`.

If the runtime supports QR Code size estimation, the application **may** set
`XrTrackableQrCodeConfigurationANDROID::qrCodeEdgeSize` to `0` to
indicate the usage of size estimation.
Otherwise, the application **must** set
`XrTrackableQrCodeConfigurationANDROID::qrCodeEdgeSize` to a
positive value or `XR_ERROR_VALIDATION_FAILURE` will be returned.

The runtime **must** filter the output from `xrGetAllTrackablesANDROID` to
match the `trackingMode` and `qrCodeEdgeSize`.

#### Valid Usage (Implicit)

- The `XR_ANDROID_trackables_qr_code` extension **must** be enabled prior to using `XrTrackableQrCodeConfigurationANDROID`
- `type` **must** be `XR_TYPE_TRACKABLE_QR_CODE_CONFIGURATION_ANDROID`
- `next` **must** be `NULL` or a valid pointer to the next structure in a structure chain
- `trackingMode` **must** be a valid `XrQrCodeTrackingModeANDROID` value

### XrQrCodeTrackingModeANDROID

The `XrQrCodeTrackingModeANDROID` enum describes the supported tracking
modes of QR Codes.

    typedef enum XrQrCodeTrackingModeANDROID {
        XR_QR_CODE_TRACKING_MODE_STATIC_ANDROID = 0,
        XR_QR_CODE_TRACKING_MODE_DYNAMIC_ANDROID = 1,
        XR_QR_CODE_TRACKING_MODE_MAX_ENUM_ANDROID = 0x7FFFFFFF
    } XrQrCodeTrackingModeANDROID;

\| Enum \| Description -
\| `XR_QR_CODE_TRACKING_MODE_STATIC_ANDROID` \| The QR Code is static and does not move. '
\| `XR_QR_CODE_TRACKING_MODE_DYNAMIC_ANDROID` \| The QR Code is dynamic and may move. \|

## Get QR Codes

### xrGetTrackableQrCodeANDROID

The `xrGetTrackableQrCodeANDROID` function is defined as:

    XrResult xrGetTrackableQrCodeANDROID(
        XrTrackableTrackerANDROID                   tracker,
        const XrTrackableGetInfoANDROID*            getInfo,
        XrTrackableQrCodeANDROID*                   qrCodeOutput);

#### Parameter Descriptions

- `tracker` is the [`XrTrackableTrackerANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables#XrTrackableTrackerANDROID) to query.
- `getInfo` is the [`XrTrackableGetInfoANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables#XrTrackableGetInfoANDROID) with the information used to get the trackable QR Code.
- `qrCodeOutput` is a pointer to the `XrTrackableQrCodeANDROID` structure in which the trackable QR Code is returned.

The runtime **must** return `XR_ERROR_MISMATCHING_TRACKABLE_TYPE_ANDROID`
if the trackable type of the `XrTrackableANDROID` is not
`XR_TRACKABLE_TYPE_QR_CODE_ANDROID`, or if the trackable type of the
`XrTrackableTrackerANDROID` is not
`XR_TRACKABLE_TYPE_QR_CODE_ANDROID`.

#### Valid Usage (Implicit)

- The `XR_ANDROID_trackables_qr_code` extension **must** be enabled prior to calling `xrGetTrackableQrCodeANDROID`
- `tracker` **must** be a valid `XrTrackableTrackerANDROID` handle
- `getInfo` **must** be a pointer to a valid `XrTrackableGetInfoANDROID` structure
- `qrCodeOutput` **must** be a pointer to an `XrTrackableQrCodeANDROID` structure

### XrTrackableQrCodeANDROID

The `XrTrackableQrCodeANDROID` structure is defined as:

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

#### Member Descriptions

- `type` is the [`XrStructureType`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.
- `trackingState` is the [`XrTrackingStateANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables#XrTrackingStateANDROID) of the QR Code.
- `lastUpdatedTime` is the [`XrTime`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTime) of the last update of the QR code.
- `centerPose` is the [`XrPosef`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrPosef) of the QR Code located in `XrTrackableGetInfoANDROID::baseSpace`. The QR Code lies in the XZ plane with X pointing to the right of the QR code and Z pointing to its bottom.
- `extents` is the [`XrExtent2Df`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrExtent2Df) dimensions of the QR Code. The boundary of the bounding box is at points: `centerPose` +/- (`extents` / 2).
- `bufferCapacityInput` is the capability of the `buffer`, or `0` to retrieve the required capability.
- `bufferCountOutput` If the `bufferCapacityInput` is `0`, the runtime will write the required buffer size into `bufferCountOutput`. Otherwise, it contains the total elements written in `buffer`.
- `buffer` is a pointer to an array of `char` to write the decoded QR code data. The application can pass a `nullptr` to determine the required buffer size or if not requesting the decode QR Code data. The QR Code data is returned as null-terminated UTF-8 string.
- See the [Buffer Size Parameters](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-buffer-size-parameters) section for a detailed description of retrieving the required `buffer` size.

#### Valid Usage (Implicit)

- The `XR_ANDROID_trackables_qr_code` extension **must** be enabled prior to using `XrTrackableQrCodeANDROID`
- `type` **must** be `XR_TYPE_TRACKABLE_QR_CODE_ANDROID`
- `next` **must** be `NULL` or a valid pointer to the next structure in a structure chain
- `trackingState` **must** be a valid `XrTrackingStateANDROID` value
- If `bufferCapacityInput` is not `0`, `buffer` **must** be a pointer to an array of `bufferCapacityInput` char values

## Example code for getting trackable QR Codes

The following example code demonstrates how to get trackable QR Codes.

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
    XrSystemQrCodeTrackingPropertiesANDROID qrCodeProperty =
            {.type = XR_TYPE_SYSTEM_QR_CODE_TRACKING_PROPERTIES_ANDROID, .next = nullptr};
    XrSystemProperties systemProperties = {.type = XR_TYPE_SYSTEM_PROPERTIES,
                                           .next = &qrCodeProperty};
    CHK_XR(xrGetSystemProperties(instance, systemId, &systemProperties));
    if (!qrCodeProperty.supportsQrCodeTracking) {
        // QR Code tracking is not supported.
        return;
    }

    // Create a trackable tracker for QR Code tracking.
    // If the runtime does not support size estimation, configures QR Code edge size of 0.1m.
    XrTrackableQrCodeConfigurationANDROID configuration =
            {.type = XR_TYPE_TRACKABLE_QR_CODE_CONFIGURATION_ANDROID,
             .next = nullptr,
             .trackingMode = XR_QR_CODE_TRACKING_MODE_DYNAMIC_ANDROID,
             .qrCodeEdgeSize = qrCodeProperty.supportsQrCodeSizeEstimation ? 0.0f : 0.1f};
    XrTrackableTrackerCreateInfoANDROID createInfo =
            {.type = XR_TYPE_TRACKABLE_TRACKER_CREATE_INFO_ANDROID,
             .next = &configuration,
             .trackableType = XR_TRACKABLE_TYPE_QR_CODE_ANDROID};
    XrTrackableTrackerANDROID qrCodeTracker;
    auto res = xrCreateTrackableTrackerANDROID(session, &createInfo, &qrCodeTracker);
    if (res == XR_ERROR_PERMISSION_INSUFFICIENT) {
        // Handle permission requests.
    }
    CHK_XR(res);

    // Get QR Codes.
    std::vector<XrTrackableANDROID> trackables(qrCodeProperty.maxQrCodeCount);
    std::vector<XrTrackableQrCodeANDROID> qrCodes(qrCodeProperty.maxQrCodeCount);
    uint32_t qrCodeSize = 0;
    CHK_XR(xrGetAllTrackablesANDROID(qrCodeTracker, qrCodeProperty.maxQrCodeCount, &qrCodeSize,
                                     trackables.data()));
    for (int i = 0; i < qrCodeSize; i++) {
        qrCodes[i].type = XR_TYPE_TRACKABLE_QR_CODE_ANDROID;
        qrCodes[i].next = nullptr;
        qrCodes[i].bufferCountOutput = 0;
        XrTrackableGetInfoANDROID getInfo = {.type = XR_TYPE_TRACKABLE_GET_INFO_ANDROID,
                                             .next = nullptr,
                                             .trackable = trackables.at(i),
                                             .baseSpace = appSpace,
                                             .time = updateTime};
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

**New Enum Constants**

[`XrStructureType`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) enumeration is extended with:

- `XR_TYPE_SYSTEM_QR_CODE_TRACKING_PROPERTIES_ANDROID`
- `XR_TYPE_TRACKABLE_QR_CODE_CONFIGURATION_ANDROID`
- `XR_TYPE_TRACKABLE_QR_CODE_ANDROID`

[`XrTrackableTypeANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables#XrTrackableTypeANDROID) enumeration is extended with:

- `XR_TRACKABLE_TYPE_QR_CODE_ANDROID`

**New Enums**

- `XrQrCodeTrackingModeANDROID`

**New Structures**

- `XrSystemQrCodeTrackingPropertiesANDROID`
- `XrTrackableQrCodeConfigurationANDROID`
- `XrTrackableQrCodeANDROID`

**New Functions**

- `xrGetTrackableQrCodeANDROID`

**Issues**

**Version History**

- Revision 1, 2025-02-05 (Levana Chen)
  - Initial extension description.

*** ** * ** ***

OpenXR™ and the OpenXR logo are trademarks owned
by The Khronos Group Inc. and are registered as a trademark in China,
the European Union, Japan and the United Kingdom.