---
title: https://developer.android.com/develop/xr/openxr/extensions/XR_QCOM_trackables_qr_code_operations
url: https://developer.android.com/develop/xr/openxr/extensions/XR_QCOM_trackables_qr_code_operations
source: md.txt
---

### XR_QCOM_trackables_qr_code_operations

**Name String**

`XR_QCOM_trackables_qr_code_operations`

**Extension Type**

Instance extension

**Registered Extension Number**

315

**Revision**

1

**Ratification Status**

Not ratified

**Extension and Version Dependencies**

`XR_ANDROID_trackables_qr_code`

**Last Modified Date**

2025-12-19

**IP Status**

No known IP claims.

**Contributors**

Maximilian Mayer, Qualcomm

## Overview

The [XrSystemQrCodeTrackingOperationsPropertiesQCOM](https://developer.android.com/develop/xr/openxr/extensions/XR_QCOM_trackables_qr_code_operations#XrSystemQrCodeTrackingOperationsPropertiesQCOM) structure is defined as:

    typedef struct XrSystemQrCodeTrackingOperationsPropertiesQCOM {
        XrStructureType    type;
        void*              next;
        XrBool32           supportsQrCodeTrackingOperations;
    } XrSystemQrCodeTrackingOperationsPropertiesQCOM;

### Member Descriptions

- `type`
- `next`
- `supportsQrCodeTrackingOperations`

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_QCOM_trackables_qr_code_operations#VUID-XrSystemQrCodeTrackingOperationsPropertiesQCOM-extension-notenabled) The `XR_QCOM_trackables_qr_code_operations` extension **must** be enabled prior to using [XrSystemQrCodeTrackingOperationsPropertiesQCOM](https://developer.android.com/develop/xr/openxr/extensions/XR_QCOM_trackables_qr_code_operations#XrSystemQrCodeTrackingOperationsPropertiesQCOM)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_QCOM_trackables_qr_code_operations#VUID-XrSystemQrCodeTrackingOperationsPropertiesQCOM-type-type) `type` **must** be `XR_TYPE_SYSTEM_QR_CODE_TRACKING_OPERATIONS_PROPERTIES_QCOM`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_QCOM_trackables_qr_code_operations#VUID-XrSystemQrCodeTrackingOperationsPropertiesQCOM-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)

The [XrTrackableQrCodeVersionFilterQCOM](https://developer.android.com/develop/xr/openxr/extensions/XR_QCOM_trackables_qr_code_operations#XrTrackableQrCodeVersionFilterQCOM) structure is defined as:

    typedef struct XrTrackableQrCodeVersionFilterQCOM {
        XrStructureType    type;
        const void*        next;
        uint32_t           qrCodeVersionCount;
        uint32_t*          qrCodeVersions;
    } XrTrackableQrCodeVersionFilterQCOM;

### Member Descriptions

- `type`
- `next`
- `qrCodeVersionCount`
- `qrCodeVersions`

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_QCOM_trackables_qr_code_operations#VUID-XrTrackableQrCodeVersionFilterQCOM-extension-notenabled) The `XR_QCOM_trackables_qr_code_operations` extension **must** be enabled prior to using [XrTrackableQrCodeVersionFilterQCOM](https://developer.android.com/develop/xr/openxr/extensions/XR_QCOM_trackables_qr_code_operations#XrTrackableQrCodeVersionFilterQCOM)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_QCOM_trackables_qr_code_operations#VUID-XrTrackableQrCodeVersionFilterQCOM-type-type) `type` **must** be `XR_TYPE_TRACKABLE_QR_CODE_VERSION_FILTER_QCOM`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_QCOM_trackables_qr_code_operations#VUID-XrTrackableQrCodeVersionFilterQCOM-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_QCOM_trackables_qr_code_operations#VUID-XrTrackableQrCodeVersionFilterQCOM-qrCodeVersions-parameter) `qrCodeVersions` **must** be a pointer to an array of `qrCodeVersionCount` `uint32_t` values
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_QCOM_trackables_qr_code_operations#VUID-XrTrackableQrCodeVersionFilterQCOM-qrCodeVersionCount-arraylength) The `qrCodeVersionCount` parameter **must** be greater than `0`

The [XrTrackableQrCodeVersionQCOM](https://developer.android.com/develop/xr/openxr/extensions/XR_QCOM_trackables_qr_code_operations#XrTrackableQrCodeVersionQCOM) structure is defined as:

    typedef struct XrTrackableQrCodeVersionQCOM {
        XrStructureType    type;
        void*              next;
        uint32_t           qrVersion;
    } XrTrackableQrCodeVersionQCOM;

### Member Descriptions

- `type`
- `next`
- `qrVersion`

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_QCOM_trackables_qr_code_operations#VUID-XrTrackableQrCodeVersionQCOM-extension-notenabled) The `XR_QCOM_trackables_qr_code_operations` extension **must** be enabled prior to using [XrTrackableQrCodeVersionQCOM](https://developer.android.com/develop/xr/openxr/extensions/XR_QCOM_trackables_qr_code_operations#XrTrackableQrCodeVersionQCOM)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_QCOM_trackables_qr_code_operations#VUID-XrTrackableQrCodeVersionQCOM-type-type) `type` **must** be `XR_TYPE_TRACKABLE_QR_CODE_VERSION_QCOM`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_QCOM_trackables_qr_code_operations#VUID-XrTrackableQrCodeVersionQCOM-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)

The [xrGetTrackableQrCodeRawDataQCOM](https://developer.android.com/develop/xr/openxr/extensions/XR_QCOM_trackables_qr_code_operations#xrGetTrackableQrCodeRawDataQCOM) function is defined as:

    XrResult xrGetTrackableQrCodeRawDataQCOM(
        XrTrackableTrackerANDROID                   tracker,
        XrTrackableANDROID                          qrCode,
        uint32_t                                    bufferCapacityInput,
        uint32_t*                                   bufferCountOutput,
        uint8_t*                                    buffer);

### Parameter Descriptions

- `tracker`
- `qrCode`
- `bufferCapacityInput`
- `bufferCountOutput`
- `buffer`

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_QCOM_trackables_qr_code_operations#VUID-xrGetTrackableQrCodeRawDataQCOM-extension-notenabled) The `XR_QCOM_trackables_qr_code_operations` extension **must** be enabled prior to calling [xrGetTrackableQrCodeRawDataQCOM](https://developer.android.com/develop/xr/openxr/extensions/XR_QCOM_trackables_qr_code_operations#xrGetTrackableQrCodeRawDataQCOM)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_QCOM_trackables_qr_code_operations#VUID-xrGetTrackableQrCodeRawDataQCOM-tracker-parameter) `tracker` **must** be a valid [XrTrackableTrackerANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackableTrackerANDROID) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_QCOM_trackables_qr_code_operations#VUID-xrGetTrackableQrCodeRawDataQCOM-bufferCountOutput-parameter) `bufferCountOutput` **must** be a pointer to a `uint32_t` value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_QCOM_trackables_qr_code_operations#VUID-xrGetTrackableQrCodeRawDataQCOM-buffer-parameter) If `bufferCapacityInput` is not `0` , `buffer` **must** be a pointer to an array of `bufferCapacityInput` `uint8_t` values

### Return Codes

[Success](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`
- `XR_SESSION_LOSS_PENDING`

[Failure](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_HANDLE_INVALID`
- `XR_ERROR_INSTANCE_LOST`
- `XR_ERROR_MISMATCHING_TRACKABLE_TYPE_ANDROID`
- `XR_ERROR_RUNTIME_FAILURE`
- `XR_ERROR_SESSION_LOST`
- `XR_ERROR_SIZE_INSUFFICIENT`
- `XR_ERROR_VALIDATION_FAILURE`

The [xrResetTrackableQrCodeTrackingQCOM](https://developer.android.com/develop/xr/openxr/extensions/XR_QCOM_trackables_qr_code_operations#xrResetTrackableQrCodeTrackingQCOM) function is defined as:

    XrResult xrResetTrackableQrCodeTrackingQCOM(
        XrTrackableTrackerANDROID                   tracker,
        XrTrackableANDROID                          qrCode);

### Parameter Descriptions

- `tracker`
- `qrCode`

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_QCOM_trackables_qr_code_operations#VUID-xrResetTrackableQrCodeTrackingQCOM-extension-notenabled) The `XR_QCOM_trackables_qr_code_operations` extension **must** be enabled prior to calling [xrResetTrackableQrCodeTrackingQCOM](https://developer.android.com/develop/xr/openxr/extensions/XR_QCOM_trackables_qr_code_operations#xrResetTrackableQrCodeTrackingQCOM)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_QCOM_trackables_qr_code_operations#VUID-xrResetTrackableQrCodeTrackingQCOM-tracker-parameter) `tracker` **must** be a valid [XrTrackableTrackerANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackableTrackerANDROID) handle

### Return Codes

[Success](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`
- `XR_SESSION_LOSS_PENDING`

[Failure](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_HANDLE_INVALID`
- `XR_ERROR_INSTANCE_LOST`
- `XR_ERROR_MISMATCHING_TRACKABLE_TYPE_ANDROID`
- `XR_ERROR_RUNTIME_FAILURE`
- `XR_ERROR_SESSION_LOST`
- `XR_ERROR_VALIDATION_FAILURE`

**Version History**

- Revision 1, 2025-12-19

  - Placeholder