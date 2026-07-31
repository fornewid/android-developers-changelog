---
title: https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image
url: https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image
source: md.txt
---

### XR_ANDROID_trackables_image

**Name String**

`XR_ANDROID_trackables_image`

**Extension Type**

Instance extension

**Registered Extension Number**

710

**Revision**

1

**Ratification Status**

Not ratified

**Extension and Version Dependencies**

`XR_EXT_future`  

and  

`XR_ANDROID_trackables`

**Last Modified Date**

2025-04-08

**IP Status**

No known IP claims.

**Contributors**

Christopher Doer, Google  

Levana Chen, Google  

Jared Finder, Google  

Spencer Quin, Google  

Nihav Jain, Google  

Diego Tipaldi, Google  

Daniel Guttenberg, Qualcomm  

Mark Vadasi, Qualcomm  

Markus Birkner, Qualcomm  

Maximilian Mayer, Qualcomm

## Overview

This extension enables tracking of planar images as specified by sets of input reference images.

### Permissions

Android applications **must** have the android.permission.SCENE_UNDERSTANDING_COARSE permission listed in their manifest as this extension depends on `XR_ANDROID_trackables` and exposes the geometry of the environment. The android.permission.SCENE_UNDERSTANDING_COARSE permission is considered a dangerous permission.

(protection level: dangerous)

## Inspect system capability

The [XrSystemImageTrackingPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrSystemImageTrackingPropertiesANDROID) structure is defined as:

    typedef struct XrSystemImageTrackingPropertiesANDROID {
        XrStructureType    type;
        void*              next;
        XrBool32           supportsImageTracking;
        XrBool32           supportsPhysicalSizeEstimation;
        uint32_t           maxTrackedImageCount;
        uint32_t           maxLoadedImageCount;
    } XrSystemImageTrackingPropertiesANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension. For more details about the structure chain, see the structure being extended ( [XrSystemProperties](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSystemProperties) ).
- `supportsImageTracking` is an `XrBool32` indicating if current system provides image tracking capability.
- `supportsPhysicalSizeEstimation` is an `XrBool32` indicating if current system provides image size estimation.
- `maxTrackedImageCount` is the total maximum number of images that **can** be tracked at the same time.
- `maxLoadedImageCount` is the total maximum number of reference images that **can** be loaded across all databases.

An application **can** inspect whether the system is capable of image tracking by extending the [XrSystemProperties](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSystemProperties) with [XrSystemImageTrackingPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrSystemImageTrackingPropertiesANDROID) structure when calling [xrGetSystemProperties](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrGetSystemProperties) . The runtime **must** return `XR_ERROR_FEATURE_UNSUPPORTED` for image tracker creation if and only if `supportsImageTracking` is `XR_FALSE` .

If a runtime supports image tracking, it **must** support `maxTrackedImageCount` tracked images at any given time.

If a runtime supports image tracking, it **must** support `maxLoadedImageCount` loaded images at any given time.

If a runtime supports image size estimation, the application **can** set [XrTrackableImageDatabaseEntryANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageDatabaseEntryANDROID) :: `physicalWidth` `0` to indicate the usage of size estimation. Otherwise, the application **must** set [XrTrackableImageDatabaseEntryANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageDatabaseEntryANDROID) :: `physicalWidth` to a positive value or `XR_ERROR_VALIDATION_FAILURE` will be returned.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#VUID-XrSystemImageTrackingPropertiesANDROID-extension-notenabled) The `XR_ANDROID_trackables_image` extension **must** be enabled prior to using [XrSystemImageTrackingPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrSystemImageTrackingPropertiesANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#VUID-XrSystemImageTrackingPropertiesANDROID-type-type) `type` **must** be `XR_TYPE_SYSTEM_IMAGE_TRACKING_PROPERTIES_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#VUID-XrSystemImageTrackingPropertiesANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)

## Creating databases

The application **can** create an [XrTrackableImageDatabaseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageDatabaseANDROID) handle by creating one or more [XrTrackableImageDatabaseEntryANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageDatabaseEntryANDROID) structures and passing them to the [xrCreateTrackableImageDatabaseAsyncANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#xrCreateTrackableImageDatabaseAsyncANDROID) function through an [XrTrackableImageDatabaseCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageDatabaseCreateInfoANDROID) structure.

The application **must** provide at least one [XrTrackableImageDatabaseEntryANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageDatabaseEntryANDROID) when creating an [XrTrackableImageDatabaseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageDatabaseANDROID) handle.

An [XrTrackableImageDatabaseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageDatabaseANDROID) is a handle that represents a set processed reference images that **can** be discovered and tracked in the environment.

    XR_DEFINE_HANDLE(XrTrackableImageDatabaseANDROID)

The [XrTrackableImageDatabaseEntryANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageDatabaseEntryANDROID) structure is defined as:

    typedef struct XrTrackableImageDatabaseEntryANDROID {
        XrStructureType                        type;
        const void*                            next;
        XrTrackableImageTrackingModeANDROID    trackingMode;
        float                                  physicalWidth;
        uint32_t                               imageWidth;
        uint32_t                               imageHeight;
        XrTrackableImageFormatANDROID          format;
        uint32_t                               bufferSize;
        const uint8_t*                         buffer;
    } XrTrackableImageDatabaseEntryANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.
- `trackingMode` is an [XrTrackableImageTrackingModeANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageTrackingModeANDROID) indicating the desired mode for tracking.
- `physicalWidth` indicates the width of the image in meters. If zero, the image size will be estimated online.
- `imageWidth` indicates the width of the image in pixels.
- `imageHeight` indicates the height of the image in pixels.
- `format` is an [XrTrackableImageFormatANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageFormatANDROID) indicating the format of the image data in `buffer` .
- `bufferSize` indicates the byte length of `buffer` .
- `buffer` is the `uint8_t` buffer containing the reference image pixel data. The contents of `buffer` **must** be valid for the duration of the database creation async operation, which is started by [xrCreateTrackableImageDatabaseAsyncANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#xrCreateTrackableImageDatabaseAsyncANDROID) and completed by [xrCreateTrackableImageDatabaseCompleteANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#xrCreateTrackableImageDatabaseCompleteANDROID) .

The application **may** set `physicalWidth` to 0 to request online size estimation if [XrSystemImageTrackingPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrSystemImageTrackingPropertiesANDROID) :: `supportsPhysicalSizeEstimation` is `XR_TRUE` .

The runtime **may** return `XR_ERROR_VALIDATION_FAILURE` from [xrCreateTrackableImageDatabaseAsyncANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#xrCreateTrackableImageDatabaseAsyncANDROID) if `bufferSize` does not match the expected size based on the entry's `imageWidth` , `imageHeight` and `format` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#VUID-XrTrackableImageDatabaseEntryANDROID-extension-notenabled) The `XR_ANDROID_trackables_image` extension **must** be enabled prior to using [XrTrackableImageDatabaseEntryANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageDatabaseEntryANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#VUID-XrTrackableImageDatabaseEntryANDROID-type-type) `type` **must** be `XR_TYPE_TRACKABLE_IMAGE_DATABASE_ENTRY_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#VUID-XrTrackableImageDatabaseEntryANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#VUID-XrTrackableImageDatabaseEntryANDROID-trackingMode-parameter) `trackingMode` **must** be a valid [XrTrackableImageTrackingModeANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageTrackingModeANDROID) value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#VUID-XrTrackableImageDatabaseEntryANDROID-format-parameter) `format` **must** be a valid [XrTrackableImageFormatANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageFormatANDROID) value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#VUID-XrTrackableImageDatabaseEntryANDROID-buffer-parameter) `buffer` **must** be a pointer to an array of `bufferSize` `uint8_t` values
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#VUID-XrTrackableImageDatabaseEntryANDROID-bufferSize-arraylength) The `bufferSize` parameter **must** be greater than `0`

The [XrTrackableImageDatabaseCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageDatabaseCreateInfoANDROID) structure is defined as:

    typedef struct XrTrackableImageDatabaseCreateInfoANDROID {
        XrStructureType                                type;
        const void*                                    next;
        uint32_t                                       entryCount;
        const XrTrackableImageDatabaseEntryANDROID*    entries;
    } XrTrackableImageDatabaseCreateInfoANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.
- `entryCount` is a `uint32_t` specifying the count of elements in the `entries` array.
- `entries` is an array of [XrTrackableImageDatabaseEntryANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageDatabaseEntryANDROID) structures.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#VUID-XrTrackableImageDatabaseCreateInfoANDROID-extension-notenabled) The `XR_ANDROID_trackables_image` extension **must** be enabled prior to using [XrTrackableImageDatabaseCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageDatabaseCreateInfoANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#VUID-XrTrackableImageDatabaseCreateInfoANDROID-type-type) `type` **must** be `XR_TYPE_TRACKABLE_IMAGE_DATABASE_CREATE_INFO_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#VUID-XrTrackableImageDatabaseCreateInfoANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#VUID-XrTrackableImageDatabaseCreateInfoANDROID-entries-parameter) `entries` **must** be a pointer to an array of `entryCount` valid [XrTrackableImageDatabaseEntryANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageDatabaseEntryANDROID) structures
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#VUID-XrTrackableImageDatabaseCreateInfoANDROID-entryCount-arraylength) The `entryCount` parameter **must** be greater than `0`

The [XrCreateTrackableImageDatabaseCompletionANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrCreateTrackableImageDatabaseCompletionANDROID) structure is defined as:

    typedef struct XrCreateTrackableImageDatabaseCompletionANDROID {
        XrStructureType                    type;
        void*                              next;
        XrResult                           futureResult;
        XrTrackableImageDatabaseANDROID    database;
    } XrCreateTrackableImageDatabaseCompletionANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.
- `futureResult` is the [XrResult](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrResult) of the asynchronous operation.
- `database` is the created [XrTrackableImageDatabaseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageDatabaseANDROID) handle.

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

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#VUID-XrCreateTrackableImageDatabaseCompletionANDROID-extension-notenabled) The `XR_ANDROID_trackables_image` extension **must** be enabled prior to using [XrCreateTrackableImageDatabaseCompletionANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrCreateTrackableImageDatabaseCompletionANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#VUID-XrCreateTrackableImageDatabaseCompletionANDROID-type-type) `type` **must** be `XR_TYPE_CREATE_TRACKABLE_IMAGE_DATABASE_COMPLETION_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#VUID-XrCreateTrackableImageDatabaseCompletionANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#VUID-XrCreateTrackableImageDatabaseCompletionANDROID-futureResult-parameter) `futureResult` **must** be a valid [XrResult](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrResult) value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#VUID-XrCreateTrackableImageDatabaseCompletionANDROID-database-parameter) `database` **must** be a valid [XrTrackableImageDatabaseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageDatabaseANDROID) handle

The [xrCreateTrackableImageDatabaseAsyncANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#xrCreateTrackableImageDatabaseAsyncANDROID) function is defined as:

    XrResult xrCreateTrackableImageDatabaseAsyncANDROID(
        XrSession                                   session,
        const XrTrackableImageDatabaseCreateInfoANDROID* createInfo,
        XrFutureEXT*                                future);

### Parameter Descriptions

- `session` is a handle to an [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) previously created with [xrCreateSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateSession) .
- `createInfo` is a pointer to an [XrTrackableImageDatabaseCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageDatabaseCreateInfoANDROID) structure.
- `future` is a pointer to the created `XrFutureEXT` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#VUID-xrCreateTrackableImageDatabaseAsyncANDROID-extension-notenabled) The `XR_ANDROID_trackables_image` extension **must** be enabled prior to calling [xrCreateTrackableImageDatabaseAsyncANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#xrCreateTrackableImageDatabaseAsyncANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#VUID-xrCreateTrackableImageDatabaseAsyncANDROID-session-parameter) `session` **must** be a valid [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#VUID-xrCreateTrackableImageDatabaseAsyncANDROID-createInfo-parameter) `createInfo` **must** be a pointer to a valid [XrTrackableImageDatabaseCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageDatabaseCreateInfoANDROID) structure
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#VUID-xrCreateTrackableImageDatabaseAsyncANDROID-future-parameter) `future` **must** be a pointer to an `XrFutureEXT` value

### Return Codes

[Success](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`
- `XR_SESSION_LOSS_PENDING`

[Failure](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FEATURE_UNSUPPORTED`
- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_HANDLE_INVALID`
- `XR_ERROR_IMAGE_FORMAT_UNSUPPORTED_ANDROID`
- `XR_ERROR_INSTANCE_LOST`
- `XR_ERROR_LIMIT_REACHED`
- `XR_ERROR_OUT_OF_MEMORY`
- `XR_ERROR_RUNTIME_FAILURE`
- `XR_ERROR_SESSION_LOST`
- `XR_ERROR_VALIDATION_FAILURE`

The [xrCreateTrackableImageDatabaseCompleteANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#xrCreateTrackableImageDatabaseCompleteANDROID) function is defined as:

    XrResult xrCreateTrackableImageDatabaseCompleteANDROID(
        XrSession                                   session,
        XrFutureEXT                                 future,
        XrCreateTrackableImageDatabaseCompletionANDROID* completion);

### Parameter Descriptions

- `session` is a handle to an [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) previously created with [xrCreateSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateSession) .
- `future` is the `XrFutureEXT` of the future to complete.
- `completion` is a pointer to an [XrCreateTrackableImageDatabaseCompletionANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrCreateTrackableImageDatabaseCompletionANDROID) structure containing the result of the operation.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#VUID-xrCreateTrackableImageDatabaseCompleteANDROID-extension-notenabled) The `XR_ANDROID_trackables_image` extension **must** be enabled prior to calling [xrCreateTrackableImageDatabaseCompleteANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#xrCreateTrackableImageDatabaseCompleteANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#VUID-xrCreateTrackableImageDatabaseCompleteANDROID-session-parameter) `session` **must** be a valid [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#VUID-xrCreateTrackableImageDatabaseCompleteANDROID-completion-parameter) `completion` **must** be a pointer to an [XrCreateTrackableImageDatabaseCompletionANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrCreateTrackableImageDatabaseCompletionANDROID) structure

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

The [xrDestroyTrackableImageDatabaseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#xrDestroyTrackableImageDatabaseANDROID) function is defined as:

    XrResult xrDestroyTrackableImageDatabaseANDROID(
        XrTrackableImageDatabaseANDROID             database);

### Parameter Descriptions

- `database` is the [XrTrackableImageDatabaseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageDatabaseANDROID) handle to destroy.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#VUID-xrDestroyTrackableImageDatabaseANDROID-extension-notenabled) The `XR_ANDROID_trackables_image` extension **must** be enabled prior to calling [xrDestroyTrackableImageDatabaseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#xrDestroyTrackableImageDatabaseANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#VUID-xrDestroyTrackableImageDatabaseANDROID-database-parameter) `database` **must** be a valid [XrTrackableImageDatabaseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageDatabaseANDROID) handle

### Thread Safety

- Access to `database` , and any child handles, **must** be externally synchronized

### Return Codes

[Success](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`

[Failure](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_HANDLE_INVALID`
- `XR_ERROR_RUNTIME_FAILURE`

## Tracking images

This extension adds `XR_TRACKABLE_TYPE_IMAGE_ANDROID` to [XrTrackableTypeANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackableTypeANDROID) .

The application **can** create an [XrTrackableTrackerANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackableTrackerANDROID) by calling [xrCreateTrackableTrackerANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateTrackableTrackerANDROID) and specifying `XR_TRACKABLE_TYPE_IMAGE_ANDROID` as the trackable type in [XrTrackableTrackerCreateInfoANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackableTrackerCreateInfoANDROID) :: `trackableType` to track images.

The runtime **must** return `XR_ERROR_FEATURE_UNSUPPORTED` if [XrTrackableTrackerCreateInfoANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackableTrackerCreateInfoANDROID) :: `trackableType` is `XR_TRACKABLE_TYPE_IMAGE_ANDROID` and [XrSystemImageTrackingPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrSystemImageTrackingPropertiesANDROID) :: `supportsImageTracking` returns `XR_FALSE` via [xrGetSystemProperties](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrGetSystemProperties) .

The [XrTrackableImageConfigurationANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageConfigurationANDROID) structure is defined as:

    typedef struct XrTrackableImageConfigurationANDROID {
        XrStructureType                           type;
        const void*                               next;
        uint32_t                                  databaseCount;
        const XrTrackableImageDatabaseANDROID*    databases;
    } XrTrackableImageConfigurationANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.
- `databaseCount` is a `uint32_t` that specifies the number of elements in `databases`
- `databases` is an array of [XrTrackableImageDatabaseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageDatabaseANDROID) that specifies the databases to create the tracker with.

The application **must** set a valid configuration by adding a [XrTrackableImageConfigurationANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageConfigurationANDROID) to the `next` chain of [XrTrackableTrackerCreateInfoANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackableTrackerCreateInfoANDROID) . Otherwise, the runtime **must** return `XR_ERROR_VALIDATION_FAILURE` .

The application **must** provide at least one [XrTrackableImageDatabaseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageDatabaseANDROID) structure to create the tracker with.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#VUID-XrTrackableImageConfigurationANDROID-extension-notenabled) The `XR_ANDROID_trackables_image` extension **must** be enabled prior to using [XrTrackableImageConfigurationANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageConfigurationANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#VUID-XrTrackableImageConfigurationANDROID-type-type) `type` **must** be `XR_TYPE_TRACKABLE_IMAGE_CONFIGURATION_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#VUID-XrTrackableImageConfigurationANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#VUID-XrTrackableImageConfigurationANDROID-databases-parameter) `databases` **must** be a pointer to an array of `databaseCount` valid [XrTrackableImageDatabaseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageDatabaseANDROID) handles
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#VUID-XrTrackableImageConfigurationANDROID-databaseCount-arraylength) The `databaseCount` parameter **must** be greater than `0`

The [XrTrackableImageTrackingModeANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageTrackingModeANDROID) enum describes the supported tracking modes of images.

    typedef enum XrTrackableImageTrackingModeANDROID {
        XR_TRACKABLE_IMAGE_TRACKING_MODE_DYNAMIC_ANDROID = 1,
        XR_TRACKABLE_IMAGE_TRACKING_MODE_STATIC_ANDROID = 2,
        XR_TRACKABLE_IMAGE_TRACKING_MODE_MAX_ENUM_ANDROID = 0x7FFFFFFF
    } XrTrackableImageTrackingModeANDROID;

### Enumerant Descriptions

- `XR_TRACKABLE_IMAGE_TRACKING_MODE_DYNAMIC_ANDROID` --- This mode has the highest accuracy and allows low latency tracking of moving images. It has also has the highest power consumption.
- `XR_TRACKABLE_IMAGE_TRACKING_MODE_STATIC_ANDROID` --- This mode should be used for images that are known to be static or semi-static. This mode leads to less power consumption in comparison to the dynamic mode. If a static image is being moved, it will be updated with a much higher latency than using the dynamic mode.

The [XrTrackableImageFormatANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageFormatANDROID) enum describes the supported formats of images.

    typedef enum XrTrackableImageFormatANDROID {
        XR_TRACKABLE_IMAGE_FORMAT_R8G8B8A8_ANDROID = 1,
        XR_TRACKABLE_IMAGE_FORMAT_MAX_ENUM_ANDROID = 0x7FFFFFFF
    } XrTrackableImageFormatANDROID;

### Enumerant Descriptions

- `XR_TRACKABLE_IMAGE_FORMAT_R8G8B8A8_ANDROID` --- RGBA image format with 8 bits per channel color and transparency data.

The [xrAddTrackableImageDatabaseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#xrAddTrackableImageDatabaseANDROID) function is defined as:

    XrResult xrAddTrackableImageDatabaseANDROID(
        XrTrackableTrackerANDROID                   tracker,
        XrTrackableImageDatabaseANDROID             database);

### Parameter Descriptions

- `tracker` is the [XrTrackableTrackerANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackableTrackerANDROID) handle to add the `database` to.
- `database` is the [XrTrackableImageDatabaseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageDatabaseANDROID) handle to add to the `tracker` .

When an [XrTrackableImageDatabaseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageDatabaseANDROID) is added to a tracker, the reference images of that database **must** be considered for detection and tracking in addition to any other databases that have been added previously with either [xrAddTrackableImageDatabaseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#xrAddTrackableImageDatabaseANDROID) or through the [XrTrackableImageConfigurationANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageConfigurationANDROID) structure when initially creating the tracker.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#VUID-xrAddTrackableImageDatabaseANDROID-extension-notenabled) The `XR_ANDROID_trackables_image` extension **must** be enabled prior to calling [xrAddTrackableImageDatabaseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#xrAddTrackableImageDatabaseANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#VUID-xrAddTrackableImageDatabaseANDROID-tracker-parameter) `tracker` **must** be a valid [XrTrackableTrackerANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackableTrackerANDROID) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#VUID-xrAddTrackableImageDatabaseANDROID-database-parameter) `database` **must** be a valid [XrTrackableImageDatabaseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageDatabaseANDROID) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#VUID-xrAddTrackableImageDatabaseANDROID-commonparent) Both of `database` and `tracker` **must** have been created, allocated, or retrieved from the same [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession)

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
- `XR_ERROR_VALIDATION_FAILURE`

The [xrRemoveTrackableImageDatabaseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#xrRemoveTrackableImageDatabaseANDROID) function is defined as:

    XrResult xrRemoveTrackableImageDatabaseANDROID(
        XrTrackableTrackerANDROID                   tracker,
        XrTrackableImageDatabaseANDROID             database);

### Parameter Descriptions

- `tracker` is the [XrTrackableTrackerANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackableTrackerANDROID) handle to remove the `database` from.
- `database` is the [XrTrackableImageDatabaseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageDatabaseANDROID) handle to remove from the `tracker` .

When an [XrTrackableImageDatabaseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageDatabaseANDROID) is removed from an [XrTrackableTrackerANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackableTrackerANDROID) , the [XrTrackableImageDatabaseEntryANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageDatabaseEntryANDROID) structures of that database **must** no longer be considered for detection and tracking. Any actively tracked entries of that database **must** no longer be reported. The removed [XrTrackableImageDatabaseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageDatabaseANDROID) handle **must** not be implicitly destroyed as part of this operation.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#VUID-xrRemoveTrackableImageDatabaseANDROID-extension-notenabled) The `XR_ANDROID_trackables_image` extension **must** be enabled prior to calling [xrRemoveTrackableImageDatabaseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#xrRemoveTrackableImageDatabaseANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#VUID-xrRemoveTrackableImageDatabaseANDROID-tracker-parameter) `tracker` **must** be a valid [XrTrackableTrackerANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackableTrackerANDROID) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#VUID-xrRemoveTrackableImageDatabaseANDROID-database-parameter) `database` **must** be a valid [XrTrackableImageDatabaseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageDatabaseANDROID) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#VUID-xrRemoveTrackableImageDatabaseANDROID-commonparent) Both of `database` and `tracker` **must** have been created, allocated, or retrieved from the same [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession)

### Return Codes

[Success](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`
- `XR_SESSION_LOSS_PENDING`

[Failure](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_HANDLE_INVALID`
- `XR_ERROR_INSTANCE_LOST`
- `XR_ERROR_RUNTIME_FAILURE`
- `XR_ERROR_SESSION_LOST`
- `XR_ERROR_VALIDATION_FAILURE`

## Getting images

The [xrGetTrackableImageANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#xrGetTrackableImageANDROID) function is defined as:

    XrResult xrGetTrackableImageANDROID(
        XrTrackableTrackerANDROID                   tracker,
        const XrTrackableGetInfoANDROID*            getInfo,
        XrTrackableImageANDROID*                    trackable);

### Parameter Descriptions

- `tracker` is the [XrTrackableTrackerANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackableTrackerANDROID) to query.
- `getInfo` is the [XrTrackableGetInfoANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackableGetInfoANDROID) with the information used to get the trackable QR code.
- `trackable` is a pointer to the [XrTrackableImageANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageANDROID) structure in which the trackable image is returned.

The runtime **must** return `XR_ERROR_MISMATCHING_TRACKABLE_TYPE_ANDROID` if the trackable type of the `XrTrackableANDROID` is not `XR_TRACKABLE_TYPE_IMAGE_ANDROID` , or if the trackable type of the [XrTrackableTrackerANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackableTrackerANDROID) is not `XR_TRACKABLE_TYPE_IMAGE_ANDROID` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#VUID-xrGetTrackableImageANDROID-extension-notenabled) The `XR_ANDROID_trackables_image` extension **must** be enabled prior to calling [xrGetTrackableImageANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#xrGetTrackableImageANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#VUID-xrGetTrackableImageANDROID-tracker-parameter) `tracker` **must** be a valid [XrTrackableTrackerANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackableTrackerANDROID) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#VUID-xrGetTrackableImageANDROID-getInfo-parameter) `getInfo` **must** be a pointer to a valid [XrTrackableGetInfoANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackableGetInfoANDROID) structure
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#VUID-xrGetTrackableImageANDROID-trackable-parameter) `trackable` **must** be a pointer to an [XrTrackableImageANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageANDROID) structure

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
- `XR_ERROR_TIME_INVALID`
- `XR_ERROR_VALIDATION_FAILURE`

The [XrTrackableImageANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageANDROID) structure is defined as:

    typedef struct XrTrackableImageANDROID {
        XrStructureType                    type;
        const void*                        next;
        XrTrackingStateANDROID             trackingState;
        XrTime                             lastUpdatedTime;
        XrTrackableImageDatabaseANDROID    database;
        uint32_t                           databaseEntryIndex;
        XrPosef                            centerPose;
        XrExtent2Df                        extents;
    } XrTrackableImageANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.
- `trackingState` is the [XrTrackingStateANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackingStateANDROID) of the image.
- `lastUpdatedTime` is the `XrTime` of the last update of the image.
- `database` is the [XrTrackableImageDatabaseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageDatabaseANDROID) handle this image was tracked from.
- `databaseEntryIndex` is the index that maps into the [XrTrackableImageDatabaseCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageDatabaseCreateInfoANDROID) :: `entries` array of `database` .
- `centerPose` is the [XrPosef](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrPosef) of the image located in [XrTrackableGetInfoANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackableGetInfoANDROID) :: `baseSpace` . The image lies in the XZ plane with X pointing to the right of the image and Z pointing to its bottom.
- `extents` is the [XrExtent2Df](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrExtent2Df) dimensions of the image. The boundary of the bounding box is at points: `centerPose` +/- ( `extents` / 2).

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#VUID-XrTrackableImageANDROID-extension-notenabled) The `XR_ANDROID_trackables_image` extension **must** be enabled prior to using [XrTrackableImageANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#VUID-XrTrackableImageANDROID-type-type) `type` **must** be `XR_TYPE_TRACKABLE_IMAGE_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#VUID-XrTrackableImageANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#VUID-XrTrackableImageANDROID-trackingState-parameter) `trackingState` **must** be a valid [XrTrackingStateANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackingStateANDROID) value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#VUID-XrTrackableImageANDROID-database-parameter) `database` **must** be a valid [XrTrackableImageDatabaseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageDatabaseANDROID) handle

## Handling failures

The application **must** poll for the [XrEventDataImageTrackingLostANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrEventDataImageTrackingLostANDROID) event using [xrPollEvent](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrPollEvent) and **must** not ignore it.

The [XrEventDataImageTrackingLostANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrEventDataImageTrackingLostANDROID) structure is defined as:

    typedef struct XrEventDataImageTrackingLostANDROID {
        XrStructureType    type;
        const void*        next;
        XrTime             time;
    } XrEventDataImageTrackingLostANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.
- `time` `XrTime`

Receiving the [XrEventDataImageTrackingLostANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrEventDataImageTrackingLostANDROID) event indicates that image tracking has suffered and internal failure causing existing resources to be invalidated. The application **must** destroy all [XrTrackableImageDatabaseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageDatabaseANDROID) handles and re-create them if it wishes to continue image tracking. The application **must** also destroy all image tracking related [XrTrackableTrackerANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackableTrackerANDROID) handles and re-create them if it wishes to continue image tracking.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#VUID-XrEventDataImageTrackingLostANDROID-extension-notenabled) The `XR_ANDROID_trackables_image` extension **must** be enabled prior to using [XrEventDataImageTrackingLostANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrEventDataImageTrackingLostANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#VUID-XrEventDataImageTrackingLostANDROID-type-type) `type` **must** be `XR_TYPE_EVENT_DATA_IMAGE_TRACKING_LOST_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#VUID-XrEventDataImageTrackingLostANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)

## Example code for getting trackable images

The following example code demonstrates how to get trackable images.

    XrInstance instance;  // Previously initialized.
    XrSession session;    // Previously initialized.
    XrSystemId systemId;  // Previously initialized.

    // The function pointers are previously initialized using xrGetInstanceProcAddr.
    PFN_xrGetSystemProperties xrGetSystemProperties;                       // Previously initialized.
    PFN_xrPollFutureEXT xrPollFutureEXT;                                   // Previously initialized.
    PFN_xrCreateTrackableTrackerANDROID xrCreateTrackableTrackerANDROID;   // Previously initialized.
    PFN_xrGetAllTrackablesANDROID xrGetAllTrackablesANDROID;               // Previously initialized.
    PFN_xrDestroyTrackableTrackerANDROID xrDestroyTrackableTrackerANDROID; // Previously initialized.

    PFN_xrGetTrackableImageANDROID xrGetTrackableImageANDROID;                                        // Previously initialized.
    PFN_xrCreateTrackableImageDatabaseAsyncANDROID xrCreateTrackableImageDatabaseAsyncANDROID;        // Previously initialized.
    PFN_xrCreateTrackableImageDatabaseCompleteANDROID xrCreateTrackableImageDatabaseCompleteANDROID;  // Previously initialized.
    PFN_xrDestroyTrackableImageDatabaseANDROID xrDestroyTrackableImageDatabaseANDROID;                // Previously initialized.
    PFN_xrAddTrackableImageDatabaseANDROID xrAddTrackableImageDatabaseANDROID;                        // Previously initialized.
    PFN_xrRemoveTrackableImageDatabaseANDROID xrRemoveTrackableImageDatabaseANDROID;                  // Previously initialized.

    XrTime updateTime; // Time used for the current frame's simulation update.
    XrSpace appSpace;  // Space created for XR_REFERENCE_SPACE_TYPE_LOCAL.

    // Inspect system capability
    XrSystemImageTrackingPropertiesANDROID imageProperty {
      .type = XR_TYPE_SYSTEM_IMAGE_TRACKING_PROPERTIES_ANDROID,
      .next = nullptr,
    };
    XrSystemProperties systemProperties {
      .type = XR_TYPE_SYSTEM_PROPERTIES,
      .next = &imageProperty,
    };
    CHK_XR(xrGetSystemProperties(instance, systemId, &systemProperties));
    if (!imageProperty.supportsImageTracking) {
        // image tracking is not supported.
        return;
    }

    uint8_t* imageBuffer; // Load the image buffer.
    uint32_t imageBufferSize; // Get the image buffer size.

    XrTrackableImageDatabaseEntryANDROID imageDatabaseEntries[1] = {
      {
        .type = XR_TYPE_TRACKABLE_IMAGE_DATABASE_ENTRY_ANDROID,
        .next = nullptr,
        .trackingMode = XR_TRACKABLE_IMAGE_TRACKING_MODE_STATIC_ANDROID,
        .physicalWidth = 0.1f, // The width of the image in meters.
        .imageWidth = 640,
        .imageHeight = 480,
        .format = XR_TRACKABLE_IMAGE_FORMAT_R8G8B8A8_ANDROID,
        .bufferSize = imageBufferSize, // RGBA buffer size in bytes.
        .buffer = imageBuffer, // RGBA data.
      }
    };

    XrTrackableImageDatabaseCreateInfoANDROID imageDatabaseCreateInfo {
      .type = XR_TYPE_TRACKABLE_IMAGE_DATABASE_CREATE_INFO_ANDROID,
      .next = nullptr,
      .entryCount = 1,
      .entries = imageDatabaseEntries
    };

    XrFutureEXT imageDatabaseFuture;
    CHK_XR(xrCreateTrackableImageDatabaseAsyncANDROID(session, &imageDatabaseCreateInfo, &imageDatabaseFuture));

    bool keepLooping = true;
    bool futureReady = false;
    while (keepLooping) {
      XrFuturePollInfoEXT pollInfo{
        .type = XR_TYPE_FUTURE_POLL_INFO_EXT,
        .future = imageDatabaseFuture,
      };
      XrFuturePollResultEXT pollResult{
        .type = XR_TYPE_FUTURE_POLL_RESULT_EXT,
      };
      CHK_XR(xrPollFutureEXT(instance, &pollInfo, &pollResult));

      if (pollResult.state == XR_FUTURE_STATE_READY_EXT) {
        futureReady = true;
        keepLooping = false;
      } else {
        // Throttle the loop to not fully expend this CPU core.
        std::this_thread::yield();
      }
    }

    XrTrackableImageDatabaseANDROID imageDatabase;

    if (futureReady) {
      XrCreateTrackableImageDatabaseCompletionANDROID imageDatabaseCompletion {
        .type = XR_TYPE_CREATE_TRACKABLE_IMAGE_DATABASE_COMPLETION_ANDROID,
        .next = nullptr,
      };

      CHK_XR(xrCreateTrackableImageDatabaseCompleteANDROID(session, imageDatabaseFuture, &imageDatabaseCompletion));
      CHK_XR(imageDatabaseCompletion.futureResult);
      imageDatabase = imageDatabaseCompletion.database;
    }

    XrTrackableImageConfigurationANDROID imageConfig {
      .type = XR_TYPE_TRACKABLE_IMAGE_CONFIGURATION_ANDROID,
      .next = nullptr,
      .databaseCount = 1,
      .databases = &imageDatabase
    };

    XrTrackableTrackerCreateInfoANDROID createInfo {
      .type = XR_TYPE_TRACKABLE_TRACKER_CREATE_INFO_ANDROID,
      .next = &imageConfig,
      .trackableType = XR_TRACKABLE_TYPE_IMAGE_ANDROID
    };

    XrTrackableTrackerANDROID imageTrackableTracker;
    CHK_XR(xrCreateTrackableTrackerANDROID(session, &createInfo, &imageTrackableTracker));

    XrTrackableImageDatabaseANDROID anotherImageDatabase; // Load another database.

    // ... dynamically add it to the existing tracker
    CHK_XR(xrAddTrackableImageDatabaseANDROID(imageTrackableTracker, anotherImageDatabase));

    while (1) {
      uint32_t trackableCountOutput = 0;

      CHK_XR(xrGetAllTrackablesANDROID(imageTrackableTracker, 0, &trackableCountOutput, nullptr));

      std::vector<XrTrackableANDROID> allImageTrackables;
      allImageTrackables.resize(trackableCountOutput);

      CHK_XR(xrGetAllTrackablesANDROID(imageTrackableTracker, 0, &trackableCountOutput, allImageTrackables.data()));

      for (XrTrackableANDROID trackable : allImageTrackables) {
        XrTrackableGetInfoANDROID imageGetInfo {
          .type = XR_TYPE_TRACKABLE_GET_INFO_ANDROID,
          .next = nullptr,
          .trackable = trackable,
          .baseSpace = appSpace,
          .time = updateTime
        };

        XrTrackableImageANDROID trackableImage{
          .type = XR_TYPE_TRACKABLE_IMAGE_ANDROID,
        };
        CHK_XR(xrGetTrackableImageANDROID(imageTrackableTracker, &imageGetInfo, &trackableImage));

        // Use XrTrackableImageANDROID data.
        (void)trackableImage.trackingState;
        (void)trackableImage.lastUpdatedTime;
        (void)trackableImage.centerPose;
        (void)trackableImage.extents;

        if (trackableImage.database == imageDatabase && trackableImage.databaseEntryIndex == 0) {
          // Knowing which image the index of 0 maps to, use the specific image database
          // entry (e.g. rendering A for image A).
        }
        // indices 1+N comparisons for another specific image database entry.
      }

      // Throttle the loop to not fully expend this CPU core.
      std::this_thread::yield();
    }

    // Remove image database from an existing tracker to stop tracking the images
    // of that specific database. To resume tracking of those images re-add the
    // database at a later point.
    CHK_XR(xrRemoveTrackableImageDatabaseANDROID(imageTrackableTracker, anotherImageDatabase));

    // Destroy the image tracker to stop image tracking completely. Re-creating the
    // image tracker with existing image databases will restart image tracking.
    CHK_XR(xrDestroyTrackableTrackerANDROID(imageTrackableTracker));

    // Destroy image databases to unload the associated resources. Re-creatingd
    // databases requires going through the asynchronous creation procedure again.
    CHK_XR(xrDestroyTrackableImageDatabaseANDROID(anotherImageDatabase));
    CHK_XR(xrDestroyTrackableImageDatabaseANDROID(imageDatabase));

## Example code for managing image databases at runtime

The following example code demonstrates how to modify the set of images being tracked.

    XrSession session; // Previously initialized.

    // The function pointers are previously initialized using xrGetInstanceProcAddr.
    PFN_xrCreateTrackableTrackerANDROID xrCreateTrackableTrackerANDROID;   // Previously initialized.
    PFN_xrDestroyTrackableTrackerANDROID xrDestroyTrackableTrackerANDROID; // Previously initialized.

    PFN_xrDestroyTrackableImageDatabaseANDROID xrDestroyTrackableImageDatabaseANDROID;                // Previously initialized.
    PFN_xrAddTrackableImageDatabaseANDROID xrAddTrackableImageDatabaseANDROID;                        // Previously initialized.
    PFN_xrRemoveTrackableImageDatabaseANDROID xrRemoveTrackableImageDatabaseANDROID;                  // Previously initialized.

    // See previous C++ sample for database and tracker initialization.
    XrTrackableImageDatabaseANDROID imageDatabases[2]; // Previously initialized.
    XrTrackableImageDatabaseANDROID anotherImageDatabase; // Previously initialized.

    // Create the image tracker config with two input databases to track.
    XrTrackableImageConfigurationANDROID imageConfig {
      .type = XR_TYPE_TRACKABLE_IMAGE_CONFIGURATION_ANDROID,
      .next = nullptr,
      .databaseCount = 2,
      .databases = imageDatabases
    };

    XrTrackableTrackerCreateInfoANDROID createInfo {
      .type = XR_TYPE_TRACKABLE_TRACKER_CREATE_INFO_ANDROID,
      .next = &imageConfig,
      .trackableType = XR_TRACKABLE_TYPE_IMAGE_ANDROID
    };

    XrTrackableTrackerANDROID imageTrackableTracker;
    CHK_XR(xrCreateTrackableTrackerANDROID(session, &createInfo, &imageTrackableTracker));

    // The tracker currently tracks the images of the two databases 'imageDatabases[0]' and
    // 'imageDatabases[1]' supplied through 'imageConfig'.

    CHK_XR(xrRemoveTrackableImageDatabaseANDROID(imageTrackableTracker, imageDatabases[1]));

    // The tracker currently tracks 'imageDatabases[0]', but no longer tracks
    // 'imageDatabases[1]'.
    // The 'imageDatabases[1]' database handle is still valid.

    CHK_XR(xrAddTrackableImageDatabaseANDROID(imageTrackableTracker, imageDatabases[1]));

    // The tracker currently tracks 'imageDatabases[0]' and 'imageDatabases[1]'.

    CHK_XR(xrDestroyTrackableImageDatabaseANDROID(imageDatabases[1]));

    // The tracker currently tracks 'imageDatabases[0]', but no longer tracks
    // 'imageDatabases[1]'.
    // The 'imageDatabases[1]' database handle is no longer valid and the corresponding
    // resources have been released internally. The database needs to be re-initialized
    // and re-added to resume tracking of 'imageDatabases[0]'.

    CHK_XR(xrAddTrackableImageDatabaseANDROID(imageTrackableTracker, anotherImageDatabase));

    // The tracker currently tracks 'imageDatabases[0]' and 'anotherImageDatabase'.

    CHK_XR(xrDestroyTrackableTrackerANDROID(imageTrackableTracker));

    // The 'imageTrackableTracker' tracker handle is invalid and image tracking has been
    // stopped.
    // The 'imageDatabases[0]' and 'anotherImageDatabase' database handles are still valid.

    // Create another the image tracker config to re-create the image tracker.
    XrTrackableImageConfigurationANDROID anotherImageConfig {
      .type = XR_TYPE_TRACKABLE_IMAGE_CONFIGURATION_ANDROID,
      .next = nullptr,
      .databaseCount = 1,
      .databases = &anotherImageDatabase
    };

    XrTrackableTrackerCreateInfoANDROID anotherCreateInfo {
      .type = XR_TYPE_TRACKABLE_TRACKER_CREATE_INFO_ANDROID,
      .next = &anotherImageConfig,
      .trackableType = XR_TRACKABLE_TYPE_IMAGE_ANDROID
    };

    CHK_XR(xrCreateTrackableTrackerANDROID(session, &anotherCreateInfo, &imageTrackableTracker));

    // The tracker handle has been re-initialized and image tracking has been started again.
    // The tracker currently tracks 'anotherImageDatabase'.
    // The 'imageDatabases[0]' database handle is still valid, but not currently tracked.

## Example code for reacting to image tracking failures

The following example code demonstrates how to handle failure by polling for the [XrEventDataImageTrackingLostANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrEventDataImageTrackingLostANDROID) event.

    XrInstance instance; // Previously initialized.
    XrSession session; // Previously initialized.

    // The function pointers are previously initialized using xrGetInstanceProcAddr.
    PFN_xrPollFutureEXT xrPollFutureEXT;                                   // Previously initialized.
    PFN_xrCreateTrackableTrackerANDROID xrCreateTrackableTrackerANDROID;   // Previously initialized.
    PFN_xrDestroyTrackableTrackerANDROID xrDestroyTrackableTrackerANDROID; // Previously initialized.

    PFN_xrCreateTrackableImageDatabaseAsyncANDROID xrCreateTrackableImageDatabaseAsyncANDROID;        // Previously initialized.
    PFN_xrCreateTrackableImageDatabaseCompleteANDROID xrCreateTrackableImageDatabaseCompleteANDROID;  // Previously initialized.
    PFN_xrDestroyTrackableImageDatabaseANDROID xrDestroyTrackableImageDatabaseANDROID;                // Previously initialized.

    XrTrackableImageDatabaseEntryANDROID imageDatabaseEntries[1]; // Previously initialized.
    XrTrackableImageDatabaseANDROID imageDatabase; // Previously initialized.
    XrTrackableTrackerANDROID imageTrackableTracker; // Previously initialized.

    // Initialize an event buffer to hold the output.
    XrEventDataBuffer event = {
      .type = XR_TYPE_EVENT_DATA_BUFFER,
    };
    XrResult result = xrPollEvent(instance, &event);
    if (result == XR_SUCCESS) {
      switch (event.type) {
        case XR_TYPE_EVENT_DATA_IMAGE_TRACKING_LOST_ANDROID: {
          const XrEventDataImageTrackingLostANDROID& eventdata =
            *reinterpret_cast<XrEventDataImageTrackingLostANDROID*>(&event);

          // All existing databases and trackers need to be destroyed.
          CHK_XR(xrDestroyTrackableTrackerANDROID(imageTrackableTracker));
          CHK_XR(xrDestroyTrackableImageDatabaseANDROID(imageDatabase));

          // To resume image tracking, the database(s) and the tracker need to be re-created.

          XrTrackableImageDatabaseCreateInfoANDROID imageDatabaseCreateInfo {
            .type = XR_TYPE_TRACKABLE_IMAGE_DATABASE_CREATE_INFO_ANDROID,
            .next = nullptr,
            .entryCount = 1,
            .entries = imageDatabaseEntries
          };

          XrFutureEXT imageDatabaseFuture;
          CHK_XR(xrCreateTrackableImageDatabaseAsyncANDROID(session, &imageDatabaseCreateInfo, &imageDatabaseFuture));

          while (true) {
            XrFuturePollInfoEXT pollInfo{
              .type = XR_TYPE_FUTURE_POLL_INFO_EXT,
              .future = imageDatabaseFuture,
            };
            XrFuturePollResultEXT pollResult{
              .type = XR_TYPE_FUTURE_POLL_RESULT_EXT,
            };
            CHK_XR(xrPollFutureEXT(instance, &pollInfo, &pollResult));

            if (pollResult.state == XR_FUTURE_STATE_READY_EXT) {
              break;
            } else {
              // Throttle the loop to not fully expend this CPU core.
              std::this_thread::yield();
            }
          }

          XrCreateTrackableImageDatabaseCompletionANDROID imageDatabaseCompletion {
            .type = XR_TYPE_CREATE_TRACKABLE_IMAGE_DATABASE_COMPLETION_ANDROID,
            .next = nullptr,
          };

          CHK_XR(xrCreateTrackableImageDatabaseCompleteANDROID(session, imageDatabaseFuture, &imageDatabaseCompletion));
          CHK_XR(imageDatabaseCompletion.futureResult);
          imageDatabase = imageDatabaseCompletion.database;

          XrTrackableImageConfigurationANDROID imageConfig {
           .type = XR_TYPE_TRACKABLE_IMAGE_CONFIGURATION_ANDROID,
           .next = nullptr,
           .databaseCount = 1,
           .databases = &imageDatabase
          };

          XrTrackableTrackerCreateInfoANDROID createInfo {
            .type = XR_TYPE_TRACKABLE_TRACKER_CREATE_INFO_ANDROID,
            .next = &imageConfig,
            .trackableType = XR_TRACKABLE_TYPE_IMAGE_ANDROID
          };

          XrTrackableTrackerANDROID imageTrackableTracker;
          CHK_XR(xrCreateTrackableTrackerANDROID(session, &createInfo, &imageTrackableTracker));

          break;
        }
      }
    }

## New Object Types

- [XrTrackableImageDatabaseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageDatabaseANDROID)

## New Commands

- [xrAddTrackableImageDatabaseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#xrAddTrackableImageDatabaseANDROID)
- [xrCreateTrackableImageDatabaseAsyncANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#xrCreateTrackableImageDatabaseAsyncANDROID)
- [xrCreateTrackableImageDatabaseCompleteANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#xrCreateTrackableImageDatabaseCompleteANDROID)
- [xrDestroyTrackableImageDatabaseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#xrDestroyTrackableImageDatabaseANDROID)
- [xrGetTrackableImageANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#xrGetTrackableImageANDROID)
- [xrRemoveTrackableImageDatabaseANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#xrRemoveTrackableImageDatabaseANDROID)

## New Structures

- [XrCreateTrackableImageDatabaseCompletionANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrCreateTrackableImageDatabaseCompletionANDROID)
- [XrEventDataImageTrackingLostANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrEventDataImageTrackingLostANDROID)
- [XrTrackableImageANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageANDROID)
- [XrTrackableImageConfigurationANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageConfigurationANDROID)
- [XrTrackableImageDatabaseCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageDatabaseCreateInfoANDROID)
- [XrTrackableImageDatabaseEntryANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageDatabaseEntryANDROID)
- Extending [XrSystemProperties](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSystemProperties) :

  - [XrSystemImageTrackingPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrSystemImageTrackingPropertiesANDROID)

## New Enums

- [XrTrackableImageFormatANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageFormatANDROID)
- [XrTrackableImageTrackingModeANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image#XrTrackableImageTrackingModeANDROID)

## New Enum Constants

- `XR_ANDROID_TRACKABLES_IMAGE_EXTENSION_NAME`
- `XR_ANDROID_trackables_image_SPEC_VERSION`
- Extending [XrObjectType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrObjectType) :

  - `XR_OBJECT_TYPE_TRACKABLE_IMAGE_DATABASE_ANDROID`
- Extending [XrResult](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrResult) :

  - `XR_ERROR_IMAGE_FORMAT_UNSUPPORTED_ANDROID`
- Extending [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) :

  - `XR_TYPE_CREATE_TRACKABLE_IMAGE_DATABASE_COMPLETION_ANDROID`
  - `XR_TYPE_EVENT_DATA_IMAGE_TRACKING_LOST_ANDROID`
  - `XR_TYPE_SYSTEM_IMAGE_TRACKING_PROPERTIES_ANDROID`
  - `XR_TYPE_TRACKABLE_IMAGE_ANDROID`
  - `XR_TYPE_TRACKABLE_IMAGE_CONFIGURATION_ANDROID`
  - `XR_TYPE_TRACKABLE_IMAGE_DATABASE_CREATE_INFO_ANDROID`
  - `XR_TYPE_TRACKABLE_IMAGE_DATABASE_ENTRY_ANDROID`
- Extending [XrTrackableTypeANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTrackableTypeANDROID) :

  - `XR_TRACKABLE_TYPE_IMAGE_ANDROID`

## Issues

## Version History

- Revision 1, 2025-04-08 (Daniel Guttenberg)

  - Initial extension description.