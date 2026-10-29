---
title: https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking
url: https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking
source: md.txt
---

### XR_EXT_spatial_image_tracking

**Name String**

`XR_EXT_spatial_image_tracking`

**Extension Type**

Instance extension

**Registered Extension Number**

783

**Revision**

1

**Ratification Status**

Not ratified

**Extension and Version Dependencies**

`XR_EXT_spatial_entity`

**Contributors**

Daniel Guttenberg, Qualcomm  

Nihav Jain, Google  

Jared Finder, Google  

Zhipeng Liu, ByteDance

## Overview

This extension provides the image tracking capability for the [XR_EXT_spatial_entity](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_spatial_entity) extension. It enables applications to detect and track specific planar images as specified by sets of input reference images.

A tracked image is represented as a spatial entity with (or "that has") the following components:

- `XR_SPATIAL_COMPONENT_TYPE_IMAGE_2D_EXT`
- `XR_SPATIAL_COMPONENT_TYPE_BOUNDED_2D_EXT`

Applications typically use the spatial image tracking extension in the following pattern:

- An application first creates one or many [XrSpatialImageTrackingDatabaseEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageTrackingDatabaseEXT) handles based on sets of preloaded reference image data.
- The application then creates an [XrSpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextEXT) handle based on the [XrSpatialImageTrackingDatabaseEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageTrackingDatabaseEXT) handles created previously.
- The application then releases the reference image data to reduce its memory consumption.
- The application discovers and queries images according to the spatial entity access patterns.
- The application **can** load additional sets of reference images and create additional [XrSpatialImageTrackingDatabaseEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageTrackingDatabaseEXT) and subsequently [XrSpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextEXT) from them to extend the set of detectable and trackable images dynamically at runtime.
- The application **can** destroy [XrSpatialImageTrackingDatabaseEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageTrackingDatabaseEXT) handles to reduce the set of detectable and trackable images dynamically at runtime.
- The application **can** destroy [XrSpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextEXT) handles to reduce the set of detectable and trackable images dynamically at runtime.

## Runtime Support

A runtime **must** advertise its support for the image tracking capability using [xrEnumerateSpatialCapabilitiesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrEnumerateSpatialCapabilitiesEXT) by listing the following capability:

- `XR_SPATIAL_CAPABILITY_IMAGE_TRACKING_EXT`

## Configuration

To enable detection and tracking of planar images, the application **can** pass [XrSpatialCapabilityConfigurationImageTrackingEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialCapabilityConfigurationImageTrackingEXT) structures in [XrSpatialContextCreateInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextCreateInfoEXT) :: `capabilityConfigs` when calling the [xrCreateSpatialContextAsyncEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateSpatialContextAsyncEXT) function, and passing arrays of\< [XrSpatialImageTrackingDatabaseEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageTrackingDatabaseEXT) structures in each [XrSpatialCapabilityConfigurationImageTrackingEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialCapabilityConfigurationImageTrackingEXT) :: `imageTrackingDatabases` .

## Input Image Set Creation

To specify the reference images to be detected and tracked, the application **must** create at least one set of input reference images. A set of input reference images is represented by an [XrSpatialImageTrackingDatabaseEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageTrackingDatabaseEXT) handle and contains at least one image.

    XR_DEFINE_HANDLE(XrSpatialImageTrackingDatabaseEXT)

The [XrSpatialImageTrackingDatabaseEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageTrackingDatabaseEXT) handle represents the resources for discovering and updating some number of spatial images in the environment of the user. Applications **can** use this handle to discover and update spatial images using other functions in this extension.

### Create the Spatial Image Tracking Database

The [xrCreateSpatialImageTrackingDatabaseAsyncEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#xrCreateSpatialImageTrackingDatabaseAsyncEXT) function is defined as:

    XrResult xrCreateSpatialImageTrackingDatabaseAsyncEXT(
        XrSession                                   session,
        const XrSpatialImageTrackingDatabaseCreateInfoEXT* createInfo,
        XrFutureEXT*                                future);

### Parameter Descriptions

- `session` is an [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) in which the spatial image tracking database will be active.
- `createInfo` is the [XrSpatialImageTrackingDatabaseCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageTrackingDatabaseCreateInfoEXT) used to specify the spatial image tracking database parameters.
- `future` is a pointer to an `XrFutureEXT` .

An application **can** create an [XrSpatialImageTrackingDatabaseEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageTrackingDatabaseEXT) handle using the [xrCreateSpatialImageTrackingDatabaseAsyncEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#xrCreateSpatialImageTrackingDatabaseAsyncEXT) function and configure the sets of input reference images of the image tracking database with `createInfo` .

The runtime **must** return `XR_ERROR_SPATIAL_IMAGE_FORMAT_UNSUPPORTED_EXT` if the [XrSpatialReferenceImageEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialReferenceImageEXT) :: `format` of any of the input reference images is not enumerated by [xrEnumerateSpatialReferenceImageFormatsEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#xrEnumerateSpatialReferenceImageFormatsEXT) .

The runtime **must** return `XR_ERROR_SPATIAL_IMAGE_INVALID_EXT` if the [XrSpatialReferenceImageEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialReferenceImageEXT) :: `planes` array of any of the input reference images cannot be evaluated according to the reference image metadata of [XrSpatialReferenceImageEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialReferenceImageEXT) .

The runtime **must** return `XR_ERROR_SPATIAL_IMAGE_INVALID_EXT` if the [XrSpatialReferenceImageEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialReferenceImageEXT) :: `planes` array of any of the input reference images does not provide exactly as many planes as the [XrSpatialReferenceImageEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialReferenceImageEXT) :: `format` has color channels.

If a runtime enforces a permission system to control application access to the image tracking capability, then the runtime **must** return `XR_ERROR_PERMISSION_INSUFFICIENT` if those permissions have not been granted to this application.

This function starts an asynchronous operation and creates a corresponding `XrFutureEXT` , usable with [xrPollFutureEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrPollFutureEXT) and related functions. The return value of this function only indicates whether the parameters were acceptable to schedule the asynchronous operation. The corresponding completion function is [xrCreateSpatialImageTrackingDatabaseCompleteEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#xrCreateSpatialImageTrackingDatabaseCompleteEXT) , usable when a future from this function is in the [READY](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrFutureStateEXT) state, with outputs populated by that function in the completion structure [XrCreateSpatialImageTrackingDatabaseCompletionEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrCreateSpatialImageTrackingDatabaseCompletionEXT) .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#VUID-xrCreateSpatialImageTrackingDatabaseAsyncEXT-extension-notenabled) The `XR_EXT_spatial_image_tracking` extension **must** be enabled prior to calling [xrCreateSpatialImageTrackingDatabaseAsyncEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#xrCreateSpatialImageTrackingDatabaseAsyncEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#VUID-xrCreateSpatialImageTrackingDatabaseAsyncEXT-session-parameter) `session` **must** be a valid [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#VUID-xrCreateSpatialImageTrackingDatabaseAsyncEXT-createInfo-parameter) `createInfo` **must** be a pointer to a valid [XrSpatialImageTrackingDatabaseCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageTrackingDatabaseCreateInfoEXT) structure
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#VUID-xrCreateSpatialImageTrackingDatabaseAsyncEXT-future-parameter) `future` **must** be a pointer to an `XrFutureEXT` value

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
- `XR_ERROR_SPATIAL_IMAGE_FORMAT_UNSUPPORTED_EXT`
- `XR_ERROR_SPATIAL_IMAGE_INVALID_EXT`
- `XR_ERROR_SPATIAL_IMAGE_SIZE_MISSING_EXT`
- `XR_ERROR_VALIDATION_FAILURE`

The [XrSpatialImageTrackingDatabaseCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageTrackingDatabaseCreateInfoEXT) structure is defined as:

    typedef struct XrSpatialImageTrackingDatabaseCreateInfoEXT {
        XrStructureType                      type;
        const void*                          next;
        uint32_t                             spatialReferenceImageCount;
        const XrSpatialReferenceImageEXT*    spatialReferenceImages;
    } XrSpatialImageTrackingDatabaseCreateInfoEXT;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `spatialReferenceImageCount` is the number of elements in the `spatialReferenceImages` array.
- `spatialReferenceImages` is an array of [XrSpatialReferenceImageEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialReferenceImageEXT) .

The [XrSpatialImageTrackingDatabaseCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageTrackingDatabaseCreateInfoEXT) structure describes the information to create an [XrSpatialImageTrackingDatabaseEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageTrackingDatabaseEXT) handle.

Each [XrSpatialImageTrackingDatabaseEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageTrackingDatabaseEXT) **must** be created with at least one [XrSpatialReferenceImageEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialReferenceImageEXT) in the [XrSpatialImageTrackingDatabaseCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageTrackingDatabaseCreateInfoEXT) :: `spatialReferenceImages` array.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#VUID-XrSpatialImageTrackingDatabaseCreateInfoEXT-extension-notenabled) The `XR_EXT_spatial_image_tracking` extension **must** be enabled prior to using [XrSpatialImageTrackingDatabaseCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageTrackingDatabaseCreateInfoEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#VUID-XrSpatialImageTrackingDatabaseCreateInfoEXT-type-type) `type` **must** be `XR_TYPE_SPATIAL_IMAGE_TRACKING_DATABASE_CREATE_INFO_EXT`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#VUID-XrSpatialImageTrackingDatabaseCreateInfoEXT-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains) . See also: [XrSpatialImageSizeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageSizeEXT) , [XrSpatialImageStaticOptimizationEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageStaticOptimizationEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#VUID-XrSpatialImageTrackingDatabaseCreateInfoEXT-spatialReferenceImages-parameter) `spatialReferenceImages` **must** be a pointer to an array of `spatialReferenceImageCount` valid [XrSpatialReferenceImageEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialReferenceImageEXT) structures
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#VUID-XrSpatialImageTrackingDatabaseCreateInfoEXT-spatialReferenceImageCount-arraylength) The `spatialReferenceImageCount` parameter **must** be greater than `0`

The [xrCreateSpatialImageTrackingDatabaseCompleteEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#xrCreateSpatialImageTrackingDatabaseCompleteEXT) function is defined as:

    XrResult xrCreateSpatialImageTrackingDatabaseCompleteEXT(
        XrSession                                   session,
        XrFutureEXT                                 future,
        XrCreateSpatialImageTrackingDatabaseCompletionEXT* completion);

### Parameter Descriptions

- `session` is the [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) previously passed to [xrCreateSpatialContextAsyncEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateSpatialContextAsyncEXT) :: `session` .
- `future` is the `XrFutureEXT` received from [xrCreateSpatialContextAsyncEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateSpatialContextAsyncEXT) .
- `completion` is a pointer to an [XrCreateSpatialImageTrackingDatabaseCompletionEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrCreateSpatialImageTrackingDatabaseCompletionEXT) .

[xrCreateSpatialImageTrackingDatabaseCompleteEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#xrCreateSpatialImageTrackingDatabaseCompleteEXT) completes the asynchronous operation started by [xrCreateSpatialImageTrackingDatabaseAsyncEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#xrCreateSpatialImageTrackingDatabaseAsyncEXT) .

The runtime **must** not access any [XrSpatialReferenceImagePlaneEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialReferenceImagePlaneEXT) :: `buffer` pointers that were provided by the [XrSpatialImageTrackingDatabaseCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageTrackingDatabaseCreateInfoEXT) :: `spatialReferenceImages` input array for this [xrCreateSpatialImageTrackingDatabaseAsyncEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#xrCreateSpatialImageTrackingDatabaseAsyncEXT) call after it has been completed. The application **may** free any [XrSpatialReferenceImagePlaneEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialReferenceImagePlaneEXT) :: `buffer` data after the [xrCreateSpatialImageTrackingDatabaseAsyncEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#xrCreateSpatialImageTrackingDatabaseAsyncEXT) has been completed to reduce it memory footprint.

The runtime **must** return `XR_ERROR_FUTURE_PENDING_EXT` if `future` is not in ready state. The runtime **must** return `XR_ERROR_FUTURE_INVALID_EXT` if `future` has already been completed or cancelled.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#VUID-xrCreateSpatialImageTrackingDatabaseCompleteEXT-extension-notenabled) The `XR_EXT_spatial_image_tracking` extension **must** be enabled prior to calling [xrCreateSpatialImageTrackingDatabaseCompleteEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#xrCreateSpatialImageTrackingDatabaseCompleteEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#VUID-xrCreateSpatialImageTrackingDatabaseCompleteEXT-session-parameter) `session` **must** be a valid [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#VUID-xrCreateSpatialImageTrackingDatabaseCompleteEXT-completion-parameter) `completion` **must** be a pointer to an [XrCreateSpatialImageTrackingDatabaseCompletionEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrCreateSpatialImageTrackingDatabaseCompletionEXT) structure

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

The [XrCreateSpatialImageTrackingDatabaseCompletionEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrCreateSpatialImageTrackingDatabaseCompletionEXT) structure is defined as:

    typedef struct XrCreateSpatialImageTrackingDatabaseCompletionEXT {
        XrStructureType                      type;
        void*                                next;
        XrResult                             futureResult;
        XrSpatialImageTrackingDatabaseEXT    database;
    } XrCreateSpatialImageTrackingDatabaseCompletionEXT;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `futureResult` is the [XrResult](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrResult) of the spatial image tracking database creation operation.
- `database` is an [XrSpatialImageTrackingDatabaseEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageTrackingDatabaseEXT) created using the data and configuration in [xrCreateSpatialImageTrackingDatabaseAsyncEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#xrCreateSpatialImageTrackingDatabaseAsyncEXT) :: `createInfo` .

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
- `XR_ERROR_SPATIAL_IMAGE_FORMAT_UNSUPPORTED_EXT`
- `XR_ERROR_SPATIAL_IMAGE_INVALID_EXT`

If `futureResult` is a success code, `database` **must** be a valid handle. If `database` is valid, it remains so only within the lifecycle of [xrCreateSpatialImageTrackingDatabaseAsyncEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#xrCreateSpatialImageTrackingDatabaseAsyncEXT) :: `session` or until the application destroys the `database` with [xrDestroySpatialImageTrackingDatabaseEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#xrDestroySpatialImageTrackingDatabaseEXT) , whichever comes first.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#VUID-XrCreateSpatialImageTrackingDatabaseCompletionEXT-extension-notenabled) The `XR_EXT_spatial_image_tracking` extension **must** be enabled prior to using [XrCreateSpatialImageTrackingDatabaseCompletionEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrCreateSpatialImageTrackingDatabaseCompletionEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#VUID-XrCreateSpatialImageTrackingDatabaseCompletionEXT-type-type) `type` **must** be `XR_TYPE_CREATE_SPATIAL_IMAGE_TRACKING_DATABASE_COMPLETION_EXT`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#VUID-XrCreateSpatialImageTrackingDatabaseCompletionEXT-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#VUID-XrCreateSpatialImageTrackingDatabaseCompletionEXT-futureResult-parameter) `futureResult` **must** be a valid [XrResult](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrResult) value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#VUID-XrCreateSpatialImageTrackingDatabaseCompletionEXT-database-parameter) `database` **must** be a valid [XrSpatialImageTrackingDatabaseEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageTrackingDatabaseEXT) handle

### Destroy the Spatial Image Tracking Database

The [xrDestroySpatialImageTrackingDatabaseEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#xrDestroySpatialImageTrackingDatabaseEXT) function is defined as:

    XrResult xrDestroySpatialImageTrackingDatabaseEXT(
        XrSpatialImageTrackingDatabaseEXT           database);

### Parameter Descriptions

- `database` is an [XrSpatialImageTrackingDatabaseEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageTrackingDatabaseEXT) previously created by [xrCreateSpatialImageTrackingDatabaseAsyncEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#xrCreateSpatialImageTrackingDatabaseAsyncEXT) .

The application **can** call the [xrDestroySpatialImageTrackingDatabaseEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#xrDestroySpatialImageTrackingDatabaseEXT) function to release the `database` handle and the underlying resources when finished with spatial image discovery and update tasks.

The application **can** call the [xrDestroySpatialImageTrackingDatabaseEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#xrDestroySpatialImageTrackingDatabaseEXT) function before calling [xrDestroySpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrDestroySpatialContextEXT) . The runtime **must** no longer report images managed by this destroyed [XrSpatialImageTrackingDatabaseEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageTrackingDatabaseEXT) . The runtime **must** continue to report images managed by other databases.

The runtime **must** ensure that discovery snapshots returned by [xrCreateSpatialDiscoverySnapshotCompleteEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateSpatialDiscoverySnapshotCompleteEXT) do not contain images pertaining to destroyed or otherwise invalid [XrSpatialImageTrackingDatabaseEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageTrackingDatabaseEXT) handles, even if the handle was destroyed after the application called [xrCreateSpatialDiscoverySnapshotAsyncEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateSpatialDiscoverySnapshotAsyncEXT) . Given that the data in a spatial snapshot is immutable, the application **should** destroy any [XrSpatialSnapshotEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialSnapshotEXT) handles that were created before it destroys `database` , otherwise the application **may** receive invalid [XrSpatialImageTrackingDatabaseEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageTrackingDatabaseEXT) handles when using [xrQuerySpatialComponentDataEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrQuerySpatialComponentDataEXT) .

The application **can** call the [xrDestroySpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrDestroySpatialContextEXT) function to release the [XrSpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextEXT) handle before destroying any of the [XrSpatialImageTrackingDatabaseEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageTrackingDatabaseEXT) handles that [XrSpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextEXT) was created with. The runtime **must** not implicitly destroy these [XrSpatialImageTrackingDatabaseEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageTrackingDatabaseEXT) handles when the [XrSpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextEXT) is destroyed.

Managing the lifetime of [XrSpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextEXT) and [XrSpatialImageTrackingDatabaseEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageTrackingDatabaseEXT) independently enables applications to reuse previously created [XrSpatialImageTrackingDatabaseEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageTrackingDatabaseEXT) handles without needing to reperform the costly creation procedure.

For example, destroying an [XrSpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextEXT) and subsequently recreating another [XrSpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextEXT) with the same [XrSpatialImageTrackingDatabaseEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageTrackingDatabaseEXT) enables pausing and resuming image tracking without needing to perform another initialization procedure.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#VUID-xrDestroySpatialImageTrackingDatabaseEXT-extension-notenabled) The `XR_EXT_spatial_image_tracking` extension **must** be enabled prior to calling [xrDestroySpatialImageTrackingDatabaseEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#xrDestroySpatialImageTrackingDatabaseEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#VUID-xrDestroySpatialImageTrackingDatabaseEXT-database-parameter) `database` **must** be a valid [XrSpatialImageTrackingDatabaseEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageTrackingDatabaseEXT) handle

### Thread Safety

- Access to `database` , and any child handles, **must** be externally synchronized

### Return Codes

[Success](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`

[Failure](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_HANDLE_INVALID`
- `XR_ERROR_RUNTIME_FAILURE`

### Input Image Format Support

Applications **should** call [xrEnumerateSpatialReferenceImageFormatsEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#xrEnumerateSpatialReferenceImageFormatsEXT) to get the list of supported input reference image formats.

The [xrEnumerateSpatialReferenceImageFormatsEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#xrEnumerateSpatialReferenceImageFormatsEXT) function is defined as:

    XrResult xrEnumerateSpatialReferenceImageFormatsEXT(
        XrInstance                                  instance,
        XrSystemId                                  systemId,
        XrSpatialCapabilityEXT                      capability,
        uint32_t                                    formatCapacityInput,
        uint32_t*                                   formatCountOutput,
        XrSpatialReferenceImageFormatEXT*           formats);

### Parameter Descriptions

- `instance` is a handle to an [XrInstance](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrInstance) .
- `systemId` is the `XrSystemId` whose input reference image formats will be enumerated.
- `capability` is the [XrSpatialCapabilityEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityEXT) for which the input reference image formats will be enumerated.
- `formatCapacityInput` is the capacity of the `formats` array, or 0 to indicate a request to retrieve the required capacity.
- `formatCountOutput` is the number of formats, or the required capacity in the case that `formatCapacityInput` is insufficient.
- `formats` is an array of [XrSpatialReferenceImageFormatEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialReferenceImageFormatEXT) . It **can** be `NULL` if `formatCapacityInput` is 0.
- See the [Buffer Size Parameters](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-buffer-size-parameters) section for a detailed description of retrieving the required `formats` size.

The application **can** enumerate the list of input reference image formats supported by a given `XrSystemId` for a given [XrSpatialCapabilityEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityEXT) using [xrEnumerateSpatialReferenceImageFormatsEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#xrEnumerateSpatialReferenceImageFormatsEXT) .

The runtime **must** not enumerate the formats of extensions that are not enabled for `instance` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#VUID-xrEnumerateSpatialReferenceImageFormatsEXT-extension-notenabled) The `XR_EXT_spatial_image_tracking` extension **must** be enabled prior to calling [xrEnumerateSpatialReferenceImageFormatsEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#xrEnumerateSpatialReferenceImageFormatsEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#VUID-xrEnumerateSpatialReferenceImageFormatsEXT-instance-parameter) `instance` **must** be a valid [XrInstance](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrInstance) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#VUID-xrEnumerateSpatialReferenceImageFormatsEXT-capability-parameter) `capability` **must** be a valid [XrSpatialCapabilityEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityEXT) value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#VUID-xrEnumerateSpatialReferenceImageFormatsEXT-formatCountOutput-parameter) `formatCountOutput` **must** be a pointer to a `uint32_t` value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#VUID-xrEnumerateSpatialReferenceImageFormatsEXT-formats-parameter) If `formatCapacityInput` is not `0` , `formats` **must** be a pointer to an array of `formatCapacityInput` [XrSpatialReferenceImageFormatEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialReferenceImageFormatEXT) values

### Return Codes

[Success](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`

[Failure](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_HANDLE_INVALID`
- `XR_ERROR_INSTANCE_LOST`
- `XR_ERROR_RUNTIME_FAILURE`
- `XR_ERROR_SIZE_INSUFFICIENT`
- `XR_ERROR_SPATIAL_CAPABILITY_UNSUPPORTED_EXT`
- `XR_ERROR_SYSTEM_INVALID`
- `XR_ERROR_VALIDATION_FAILURE`

See [XrSpatialReferenceImageFormatEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialReferenceImageFormatEXT) for a complete list of all reference image formats supported by any extension.

    typedef enum XrSpatialReferenceImageFormatEXT {
        XR_SPATIAL_REFERENCE_IMAGE_FORMAT_RGBA_8888_EXT = 1,
        XR_SPATIAL_REFERENCE_IMAGE_FORMAT_RGB_888_EXT = 2,
        XR_SPATIAL_REFERENCE_IMAGE_FORMAT_YUV_420_888_EXT = 3,
        XR_SPATIAL_REFERENCE_IMAGE_FORMAT_MAX_ENUM_EXT = 0x7FFFFFFF
    } XrSpatialReferenceImageFormatEXT;

The [XrSpatialReferenceImageFormatEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialReferenceImageFormatEXT) enumeration identifies the input reference image formats that the runtime **may** support.

At least the `XR_SPATIAL_REFERENCE_IMAGE_FORMAT_RGBA_8888_EXT` value and `XR_SPATIAL_REFERENCE_IMAGE_FORMAT_RGB_888_EXT` value **must** be supported.

The enumerants have the following meaning:

### Enumerant Descriptions

- `XR_SPATIAL_REFERENCE_IMAGE_FORMAT_RGBA_8888_EXT` --- An RGBA buffer. The format makes no guarantees regarding the layout of the pixel data in memory. The pixels **must** be accessed using the metadata provided by the corresponding [XrSpatialReferenceImagePlaneEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialReferenceImagePlaneEXT) structures. Each pixel color channel has an 8 bit size, making each pixel 32 bit in size.
- `XR_SPATIAL_REFERENCE_IMAGE_FORMAT_RGB_888_EXT` --- An RGB buffer. The format makes no guarantees regarding the layout of the pixel data in memory. The pixels **must** be accessed using the metadata provided by the corresponding [XrSpatialReferenceImagePlaneEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialReferenceImagePlaneEXT) structures. Each pixel color channel has an 8 bit size, making each pixel 24 bit in size.
- `XR_SPATIAL_REFERENCE_IMAGE_FORMAT_YUV_420_888_EXT` --- A YUV buffer that is 4:2:0 pattern chroma sub-sampled. The format makes no guarantees regarding the layout of the pixel data in memory. The pixels **must** be accessed using the metadata provided by the corresponding [XrSpatialReferenceImagePlaneEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialReferenceImagePlaneEXT) structures. Each decoded RGB pixel color channel has an 8 bit size, making each pixel 24 bit in size.

## Spatial Image Tracking Settings

This extension provides optional structures that the application **can** use to configure the image tracking capability with.

### Static Image Optimization

The [XrSpatialImageStaticOptimizationEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageStaticOptimizationEXT) structure is defined as:

    typedef struct XrSpatialImageStaticOptimizationEXT {
        XrStructureType    type;
        const void*        next;
        XrBool32           optimizeForStaticImage;
    } XrSpatialImageStaticOptimizationEXT;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `optimizeForStaticImage` is an `XrBool32` that indicates whether images move or not. A value of `XR_TRUE` indicates that images do not move.

If `XR_SPATIAL_CAPABILITY_FEATURE_IMAGE_TRACKING_STATIC_IMAGES_EXT` is enumerated by [xrEnumerateSpatialCapabilityFeaturesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrEnumerateSpatialCapabilityFeaturesEXT) for the `XR_SPATIAL_CAPABILITY_IMAGE_TRACKING_EXT` capability, the application **can** chain [XrSpatialImageStaticOptimizationEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageStaticOptimizationEXT) to the [XrSpatialImageTrackingDatabaseCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageTrackingDatabaseCreateInfoEXT) :: `next` chain, or [XrSpatialReferenceImageEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialReferenceImageEXT) :: `next` .

If the application chains [XrSpatialImageStaticOptimizationEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageStaticOptimizationEXT) to the [XrSpatialImageTrackingDatabaseCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageTrackingDatabaseCreateInfoEXT) structure, the runtime **must** assume that all images of that [XrSpatialImageTrackingDatabaseEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageTrackingDatabaseEXT) are static if `optimizeForStaticImage` is set to `XR_TRUE` . Correspondingly, the runtime **must** assume that all images of that [XrSpatialImageTrackingDatabaseEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageTrackingDatabaseEXT) are not static if `optimizeForStaticImage` is set to `XR_FALSE` .

If application chains [XrSpatialImageStaticOptimizationEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageStaticOptimizationEXT) to the [XrSpatialReferenceImageEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialReferenceImageEXT) structure, the runtime **must** assume that this reference image is static if `optimizeForStaticImage` is set to `XR_TRUE` . Correspondingly, the runtime **must** assume that this reference image is not static if `optimizeForStaticImage` is set to `XR_FALSE` . Chaining the [XrSpatialImageStaticOptimizationEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageStaticOptimizationEXT) structure to the [XrSpatialReferenceImageEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialReferenceImageEXT) structure takes precedence over chaining it to the [XrSpatialImageTrackingDatabaseCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageTrackingDatabaseCreateInfoEXT) structure.

If `XR_SPATIAL_CAPABILITY_FEATURE_IMAGE_TRACKING_STATIC_IMAGES_EXT` is not enumerated by [xrEnumerateSpatialCapabilityFeaturesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrEnumerateSpatialCapabilityFeaturesEXT) for the `XR_SPATIAL_CAPABILITY_IMAGE_TRACKING_EXT` capability and the application chains an [XrSpatialImageStaticOptimizationEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageStaticOptimizationEXT) structure to any of the applicable next chains the runtime **must** return `XR_ERROR_VALIDATION_FAILURE` from [xrCreateSpatialImageTrackingDatabaseAsyncEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#xrCreateSpatialImageTrackingDatabaseAsyncEXT) .

This **may** allow the runtime to generate a more accurate pose and size.

This **may** allow the runtime to reduce power consumption.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#VUID-XrSpatialImageStaticOptimizationEXT-extension-notenabled) The `XR_EXT_spatial_image_tracking` extension **must** be enabled prior to using [XrSpatialImageStaticOptimizationEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageStaticOptimizationEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#VUID-XrSpatialImageStaticOptimizationEXT-type-type) `type` **must** be `XR_TYPE_SPATIAL_IMAGE_STATIC_OPTIMIZATION_EXT`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#VUID-XrSpatialImageStaticOptimizationEXT-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)

### Reference Image Width

The [XrSpatialImageSizeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageSizeEXT) structure is defined as:

    typedef struct XrSpatialImageSizeEXT {
        XrStructureType    type;
        const void*        next;
        float              physicalWidth;
    } XrSpatialImageSizeEXT;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `physicalWidth` is a `float` value representing the physical width in meters to set.

If `XR_SPATIAL_CAPABILITY_FEATURE_IMAGE_TRACKING_FIXED_SIZE_IMAGES_EXT` is enumerated by [xrEnumerateSpatialCapabilityFeaturesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrEnumerateSpatialCapabilityFeaturesEXT) for the `XR_SPATIAL_CAPABILITY_IMAGE_TRACKING_EXT` capability, the application **can** chain [XrSpatialImageSizeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageSizeEXT) to [XrSpatialImageTrackingDatabaseCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageTrackingDatabaseCreateInfoEXT) :: `next` or [XrSpatialReferenceImageEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialReferenceImageEXT) :: `next` .

If the application chains [XrSpatialImageSizeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageSizeEXT) to the [XrSpatialImageTrackingDatabaseCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageTrackingDatabaseCreateInfoEXT) structure, the runtime **must** assume that all images of that [XrSpatialImageTrackingDatabaseEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageTrackingDatabaseEXT) have a width of `physicalWidth` meters and a height according to the aspect ratio as provided implicitly through [XrSpatialReferenceImageEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialReferenceImageEXT) :: `width` and [XrSpatialReferenceImageEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialReferenceImageEXT) :: `height` .

If the application chains [XrSpatialImageSizeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageSizeEXT) to the [XrSpatialReferenceImageEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialReferenceImageEXT) structure, the runtime **must** assume that this reference image has a width of `physicalWidth` meters and a height according to the aspect ratio as provided implicitly through [XrSpatialReferenceImageEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialReferenceImageEXT) :: `width` and [XrSpatialReferenceImageEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialReferenceImageEXT) :: `height` . Chaining the [XrSpatialImageSizeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageSizeEXT) structure to the [XrSpatialReferenceImageEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialReferenceImageEXT) structure takes precedence over chaining it to the [XrSpatialImageTrackingDatabaseCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageTrackingDatabaseCreateInfoEXT) structure.

This **may** allow the runtime to return a more accurate pose and size.

The runtime **must** enumerate either `XR_SPATIAL_CAPABILITY_FEATURE_IMAGE_TRACKING_FIXED_SIZE_IMAGES_EXT` or `XR_SPATIAL_CAPABILITY_FEATURE_IMAGE_TRACKING_AUTOMATIC_SIZE_IMAGES_EXT` or both.

If `XR_SPATIAL_CAPABILITY_FEATURE_IMAGE_TRACKING_AUTOMATIC_SIZE_IMAGES_EXT` is enumerated by [xrEnumerateSpatialCapabilityFeaturesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrEnumerateSpatialCapabilityFeaturesEXT) the runtime **must** provide image sizes automatically for images for which the application did not provide any [XrSpatialImageSizeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageSizeEXT) structures as part of any of the applicable next chains.

For the runtime to be able to generate images sizes automatically and accurately, certain device capabilities and pre requisites **may** be required; i.e. stereo cameras, accurately calibrated camera extrinsic and intrinsic parameters.

If `XR_SPATIAL_CAPABILITY_FEATURE_IMAGE_TRACKING_AUTOMATIC_SIZE_IMAGES_EXT` is not enumerated by [xrEnumerateSpatialCapabilityFeaturesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrEnumerateSpatialCapabilityFeaturesEXT) the application **must** link [XrSpatialImageSizeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageSizeEXT) structures into the applicable next chains such that all images have an explicit size provided for them, otherwise the runtime **must** return `XR_ERROR_SPATIAL_IMAGE_SIZE_MISSING_EXT` from [xrCreateSpatialImageTrackingDatabaseAsyncEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#xrCreateSpatialImageTrackingDatabaseAsyncEXT) .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#VUID-XrSpatialImageSizeEXT-extension-notenabled) The `XR_EXT_spatial_image_tracking` extension **must** be enabled prior to using [XrSpatialImageSizeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageSizeEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#VUID-XrSpatialImageSizeEXT-type-type) `type` **must** be `XR_TYPE_SPATIAL_IMAGE_SIZE_EXT`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#VUID-XrSpatialImageSizeEXT-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)

The [XrSpatialCapabilityConfigurationImageTrackingEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialCapabilityConfigurationImageTrackingEXT) structure is defined as:

    typedef struct XrSpatialCapabilityConfigurationImageTrackingEXT {
        XrStructureType                             type;
        const void*                                 next;
        XrSpatialCapabilityEXT                      capability;
        uint32_t                                    enabledComponentCount;
        const XrSpatialComponentTypeEXT*            enabledComponents;
        uint32_t                                    imageTrackingDatabaseCount;
        const XrSpatialImageTrackingDatabaseEXT*    imageTrackingDatabases;
    } XrSpatialCapabilityConfigurationImageTrackingEXT;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `capability` is an [XrSpatialCapabilityEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityEXT) and **must** be `XR_SPATIAL_CAPABILITY_IMAGE_TRACKING_EXT` .
- `enabledComponentCount` is an `uint32_t` that specifies the number of elements in `enabledComponents` .
- `enabledComponents` is an array of [XrSpatialComponentTypeEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentTypeEXT) that specifies the components to enable for this capability.
- `imageTrackingDatabaseCount` is an `unint32_t` that specifies the number of elements in `imageTrackingDatabases` .
- `imageTrackingDatabases` is an array of [XrSpatialImageTrackingDatabaseEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageTrackingDatabaseEXT) handles that specifies the image tracking databases to enable for the spatial context.

If image tracking is supported, the runtime **must** enable image tracking if an [XrSpatialCapabilityConfigurationImageTrackingEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialCapabilityConfigurationImageTrackingEXT) structure is passed in [XrSpatialContextCreateInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextCreateInfoEXT) :: `capabilityConfigs` when calling [xrCreateSpatialContextAsyncEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateSpatialContextAsyncEXT) .

The [XrSpatialCapabilityConfigurationImageTrackingEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialCapabilityConfigurationImageTrackingEXT) structure enables the application to discover the reference images represented by the [XrSpatialImageTrackingDatabaseEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageTrackingDatabaseEXT) handles in `imageTrackingDatabases` .

The runtime **must** return `XR_ERROR_SPATIAL_CAPABILITY_UNSUPPORTED_EXT` if `XR_SPATIAL_CAPABILITY_IMAGE_TRACKING_EXT` is not enumerated by [xrEnumerateSpatialCapabilitiesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrEnumerateSpatialCapabilitiesEXT) .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#VUID-XrSpatialCapabilityConfigurationImageTrackingEXT-extension-notenabled) The `XR_EXT_spatial_image_tracking` extension **must** be enabled prior to using [XrSpatialCapabilityConfigurationImageTrackingEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialCapabilityConfigurationImageTrackingEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#VUID-XrSpatialCapabilityConfigurationImageTrackingEXT-type-type) `type` **must** be `XR_TYPE_SPATIAL_CAPABILITY_CONFIGURATION_IMAGE_TRACKING_EXT`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#VUID-XrSpatialCapabilityConfigurationImageTrackingEXT-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#VUID-XrSpatialCapabilityConfigurationImageTrackingEXT-capability-parameter) `capability` **must** be a valid [XrSpatialCapabilityEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityEXT) value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#VUID-XrSpatialCapabilityConfigurationImageTrackingEXT-enabledComponents-parameter) `enabledComponents` **must** be a pointer to an array of `enabledComponentCount` valid [XrSpatialComponentTypeEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentTypeEXT) values
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#VUID-XrSpatialCapabilityConfigurationImageTrackingEXT-imageTrackingDatabases-parameter) `imageTrackingDatabases` **must** be a pointer to an array of `imageTrackingDatabaseCount` valid [XrSpatialImageTrackingDatabaseEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageTrackingDatabaseEXT) handles
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#VUID-XrSpatialCapabilityConfigurationImageTrackingEXT-enabledComponentCount-arraylength) The `enabledComponentCount` parameter **must** be greater than `0`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#VUID-XrSpatialCapabilityConfigurationImageTrackingEXT-imageTrackingDatabaseCount-arraylength) The `imageTrackingDatabaseCount` parameter **must** be greater than `0`

## Spatial Reference Image

The [XrSpatialReferenceImagePlaneEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialReferenceImagePlaneEXT) structure is defined as:

    typedef struct XrSpatialReferenceImagePlaneEXT {
        uint32_t    bufferSize;
        uint8_t*    buffer;
        uint32_t    rowStride;
        uint32_t    pixelStride;
    } XrSpatialReferenceImagePlaneEXT;

### Parameter Descriptions

- `bufferSize` is the size of the `buffer` array.
- `buffer` is an array of `uint8_t` data representing the plane data.
- `rowStride` is the byte distance between two starting positions of consecutive pixel data rows.
- `pixelStride` is the byte distance between two consecutive pixels.

The runtime **must** access `buffer` according to the patterns the `rowStride` and `pixelStride` parameters provide.

The application **must** set `rowStride` and `pixelStride` such that only meaningful pixels of this [XrSpatialReferenceImagePlaneEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialReferenceImagePlaneEXT) are extracted by the runtime.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#VUID-XrSpatialReferenceImagePlaneEXT-extension-notenabled) The `XR_EXT_spatial_image_tracking` extension **must** be enabled prior to using [XrSpatialReferenceImagePlaneEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialReferenceImagePlaneEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#VUID-XrSpatialReferenceImagePlaneEXT-buffer-parameter) `buffer` **must** be a pointer to an array of `bufferSize` `uint8_t` values
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#VUID-XrSpatialReferenceImagePlaneEXT-bufferSize-arraylength) The `bufferSize` parameter **must** be greater than `0`

The [XrSpatialReferenceImageEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialReferenceImageEXT) structure is defined as:

    typedef struct XrSpatialReferenceImageEXT {
        XrStructureType                           type;
        const void*                               next;
        uint32_t                                  width;
        uint32_t                                  height;
        XrSpatialReferenceImageFormatEXT          format;
        uint32_t                                  planeCount;
        const XrSpatialReferenceImagePlaneEXT*    planes;
    } XrSpatialReferenceImageEXT;

### Parameter Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `width` is the pixel width of the reference image.
- `height` is the pixel height of the reference image.
- `format` is an [XrSpatialReferenceImageFormatEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialReferenceImageFormatEXT) representing the format of the image.
- `planeCount` is the number of elements in the `planes` array.
- `planes` is an array of [XrSpatialReferenceImagePlaneEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialReferenceImagePlaneEXT) structures representing the planes of the image data.

The application **can** create one or more [XrSpatialReferenceImageEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialReferenceImageEXT) structures each representing a single input reference image to be passed into the [xrCreateSpatialImageTrackingDatabaseAsyncEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#xrCreateSpatialImageTrackingDatabaseAsyncEXT) function through [XrSpatialImageTrackingDatabaseCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageTrackingDatabaseCreateInfoEXT) :: `spatialReferenceImages` when creating an [XrSpatialImageTrackingDatabaseEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageTrackingDatabaseEXT) handle.

The [XrSpatialReferenceImagePlaneEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialReferenceImagePlaneEXT) :: `buffer` data **must** be supplied in a left-to-right and top-to-bottom pixel ordering by the application.

The application **must** provide an [XrSpatialReferenceImagePlaneEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialReferenceImagePlaneEXT) structure in the [XrSpatialReferenceImageEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialReferenceImageEXT) :: `planes` array for each color channel of the [XrSpatialReferenceImageEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialReferenceImageEXT) :: `format` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#VUID-XrSpatialReferenceImageEXT-extension-notenabled) The `XR_EXT_spatial_image_tracking` extension **must** be enabled prior to using [XrSpatialReferenceImageEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialReferenceImageEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#VUID-XrSpatialReferenceImageEXT-type-type) `type` **must** be `XR_TYPE_SPATIAL_REFERENCE_IMAGE_EXT`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#VUID-XrSpatialReferenceImageEXT-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains) . See also: [XrSpatialAnnotationQuadReferenceANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialAnnotationQuadReferenceANDROID) , [XrSpatialImageSizeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageSizeEXT) , [XrSpatialImageStaticOptimizationEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageStaticOptimizationEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#VUID-XrSpatialReferenceImageEXT-format-parameter) `format` **must** be a valid [XrSpatialReferenceImageFormatEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialReferenceImageFormatEXT) value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#VUID-XrSpatialReferenceImageEXT-planes-parameter) `planes` **must** be a pointer to an array of `planeCount` valid [XrSpatialReferenceImagePlaneEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialReferenceImagePlaneEXT) structures
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#VUID-XrSpatialReferenceImageEXT-planeCount-arraylength) The `planeCount` parameter **must** be greater than `0`

## Guaranteed Components

A runtime that supports `XR_SPATIAL_CAPABILITY_IMAGE_TRACKING_EXT` **must** provide the following spatial components as guaranteed components of all entities discovered by those capabilities, and must enumerate them in [xrEnumerateSpatialCapabilityComponentTypesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrEnumerateSpatialCapabilityComponentTypesEXT) :

- `XR_SPATIAL_COMPONENT_TYPE_IMAGE_2D_EXT`
- `XR_SPATIAL_COMPONENT_TYPE_BOUNDED_2D_EXT`

### Image 2D Component

###### Component List Struct to Query Data

The [XrSpatialComponentImage2DListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialComponentImage2DListEXT) structure is defined as:

    typedef struct XrSpatialComponentImage2DListEXT {
        XrStructureType             type;
        const void*                 next;
        uint32_t                    imageCount;
        XrSpatialImage2DDataEXT*    images;
    } XrSpatialComponentImage2DListEXT;

### Parameter Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `imageCount` is the number of elements in the `images` array.
- `images` is an array of [XrSpatialImage2DDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImage2DDataEXT) .

The runtime **must** return `XR_ERROR_VALIDATION_FAILURE` from [xrQuerySpatialComponentDataEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrQuerySpatialComponentDataEXT) if [XrSpatialComponentImage2DListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialComponentImage2DListEXT) is in the [XrSpatialComponentDataQueryResultEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryResultEXT) :: `next` chain, but `XR_SPATIAL_COMPONENT_TYPE_IMAGE_2D_EXT` is not included in [XrSpatialComponentDataQueryConditionEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryConditionEXT) :: `componentTypes` .

The runtime **must** return `XR_ERROR_SIZE_INSUFFICIENT` from [xrQuerySpatialComponentDataEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrQuerySpatialComponentDataEXT) if `imageCount` is less than [XrSpatialComponentDataQueryResultEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryResultEXT) :: `entityIdCountOutput` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#VUID-XrSpatialComponentImage2DListEXT-extension-notenabled) The `XR_EXT_spatial_image_tracking` extension **must** be enabled prior to using [XrSpatialComponentImage2DListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialComponentImage2DListEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#VUID-XrSpatialComponentImage2DListEXT-type-type) `type` **must** be `XR_TYPE_SPATIAL_COMPONENT_IMAGE_2D_LIST_EXT`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#VUID-XrSpatialComponentImage2DListEXT-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#VUID-XrSpatialComponentImage2DListEXT-images-parameter) `images` **must** be a pointer to an array of `imageCount` [XrSpatialImage2DDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImage2DDataEXT) structures
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#VUID-XrSpatialComponentImage2DListEXT-imageCount-arraylength) The `imageCount` parameter **must** be greater than `0`

###### Component Data

The [XrSpatialImage2DDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImage2DDataEXT) structure is defined as:

    typedef struct XrSpatialImage2DDataEXT {
        XrSpatialImageTrackingDatabaseEXT    imageTrackingDatabase;
        uint32_t                             referenceImageIndex;
    } XrSpatialImage2DDataEXT;

### Parameter Descriptions

- `imageTrackingDatabase` is the [XrSpatialImageTrackingDatabaseEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageTrackingDatabaseEXT) that detected or tracked the image.
- `referenceImageIndex` is the index that maps into the [XrSpatialImageTrackingDatabaseCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageTrackingDatabaseCreateInfoEXT) :: `spatialReferenceImages` array of input reference images that `imageTrackingDatabase` was created with.

The application **can** use `imageTrackingDatabase` to identify which previously created [XrSpatialImageTrackingDatabaseEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageTrackingDatabaseEXT) contains the reference image of this [XrSpatialImage2DDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImage2DDataEXT) structure. For that [XrSpatialImageTrackingDatabaseEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageTrackingDatabaseEXT) , the application **can** use `referenceImageIndex` to identify the [XrSpatialReferenceImageEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialReferenceImageEXT) of this [XrSpatialImage2DDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImage2DDataEXT) structure by matching it to the input order of [XrSpatialImageTrackingDatabaseCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageTrackingDatabaseCreateInfoEXT) :: `spatialReferenceImages` array.

The set of reference images defined by the set of all active databases **should** not include duplicate images. Including duplicate images **may** cause adverse discovery or tracking behavior; i.e. inconsistent or multiple indices being returned.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#VUID-XrSpatialImage2DDataEXT-extension-notenabled) The `XR_EXT_spatial_image_tracking` extension **must** be enabled prior to using [XrSpatialImage2DDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImage2DDataEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#VUID-XrSpatialImage2DDataEXT-imageTrackingDatabase-parameter) `imageTrackingDatabase` **must** be a valid [XrSpatialImageTrackingDatabaseEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageTrackingDatabaseEXT) handle

###### Configuration

If `XR_SPATIAL_COMPONENT_TYPE_IMAGE_2D_EXT` is enumerated in [XrSpatialCapabilityComponentTypesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityComponentTypesEXT) :: `componentTypes` for some capability, the application **can** enable it by including the enum value in the [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityConfigurationBaseHeaderEXT) :: `enabledComponents` list. This component does not require any special configuration to be included in the next chain of [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityConfigurationBaseHeaderEXT) .

### Bounded 2D Component

The bounded 2D component provides the center and extents of the spatial image represented by the entity it is on. See [Bounded 2D](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#ext_spatial_entity_bounded2D_component) for more details about the bounded 2D component.

## Example Code

### Discover Spatial Images \& Query Component Data

The following example code demonstrates how to discover spatial entities for the image tracking capability and query its component data.

    XrInstance instance; // Previously initialized
    XrSystemId systemId; // Previously initialized
    XrSession session; // Previously initialized

    uint32_t capabilityCountOutput = 0;
    CHK_XR(xrEnumerateSpatialCapabilitiesEXT(instance, systemId, 0, &capabilityCountOutput, nullptr));
    std::vector<XrSpatialCapabilityEXT> capabilities(capabilityCountOutput);
    CHK_XR(xrEnumerateSpatialCapabilitiesEXT(instance, systemId, capabilities.size(), &capabilityCountOutput, capabilities.data()));

    if (std::find(capabilities.begin(), capabilities.end(), XR_SPATIAL_CAPABILITY_IMAGE_TRACKING_EXT) == capabilities.end()) {
      // Image tracking not supported
    }

    XrSpatialCapabilityComponentTypesEXT imageTrackingComponents{XR_TYPE_SPATIAL_CAPABILITY_COMPONENT_TYPES_EXT};
    CHK_XR(xrEnumerateSpatialCapabilityComponentTypesEXT(instance, systemId, XR_SPATIAL_CAPABILITY_IMAGE_TRACKING_EXT, &imageTrackingComponents));
    std::vector<XrSpatialComponentTypeEXT> imageTrackingCapabilityComponents(imageTrackingComponents.componentTypeCountOutput);
    imageTrackingComponents.componentTypes = imageTrackingCapabilityComponents.data();
    CHK_XR(xrEnumerateSpatialCapabilityComponentTypesEXT(instance, systemId, XR_SPATIAL_CAPABILITY_IMAGE_TRACKING_EXT, &imageTrackingComponents));

    if (std::find(imageTrackingCapabilityComponents.begin(), imageTrackingCapabilityComponents.end(), XR_SPATIAL_COMPONENT_TYPE_IMAGE_2D_EXT) == imageTrackingCapabilityComponents.end()) {
      // The image2d component is not supported
    }

    uint32_t capabilityFeatureCountOutput = 0;
    CHK_XR(xrEnumerateSpatialCapabilityFeaturesEXT(instance, systemId, XR_SPATIAL_CAPABILITY_IMAGE_TRACKING_EXT, 0, &capabilityFeatureCountOutput, nullptr));
    std::vector<XrSpatialCapabilityFeatureEXT> capabilityFeatures(capabilityFeatureCountOutput);
    CHK_XR(xrEnumerateSpatialCapabilityFeaturesEXT(instance, systemId, XR_SPATIAL_CAPABILITY_IMAGE_TRACKING_EXT, capabilityFeatures.size(), &capabilityFeatureCountOutput, capabilityFeatures.data()));

    // Helper function to query optional feature support
    const auto supportsFeature = [&capabilityFeatures](XrSpatialCapabilityFeatureEXT feature) {
      return std::find(capabilityFeatures.begin(), capabilityFeatures.end(), feature) != capabilityFeatures.end();
    };

    // supported state for optional features
    const bool supportsAutomaticScaleEstimation = supportsFeature(XR_SPATIAL_CAPABILITY_FEATURE_IMAGE_TRACKING_AUTOMATIC_SIZE_IMAGES_EXT);
    const bool supportsStaticImages = supportsFeature(XR_SPATIAL_CAPABILITY_FEATURE_IMAGE_TRACKING_STATIC_IMAGES_EXT);
    const bool supportsFixedSizeImages = supportsFeature(XR_SPATIAL_CAPABILITY_FEATURE_IMAGE_TRACKING_FIXED_SIZE_IMAGES_EXT);

    uint32_t formatCountOutput = 0;
    CHK_XR(xrEnumerateSpatialReferenceImageFormatsEXT(instance, systemId, XR_SPATIAL_CAPABILITY_IMAGE_TRACKING_EXT, 0, &formatCountOutput, nullptr));
    std::vector<XrSpatialReferenceImageFormatEXT> formats(formatCountOutput);
    CHK_XR(xrEnumerateSpatialReferenceImageFormatsEXT(instance, systemId, XR_SPATIAL_CAPABILITY_IMAGE_TRACKING_EXT, formats.size(), &formatCountOutput, formats.data()));

    if (std::find(formats.begin(), formats.end(), XR_SPATIAL_REFERENCE_IMAGE_FORMAT_RGBA_8888_EXT) == formats.end()) {
      // The desired format is not supported
    }

    // Helper function to wait for XrFutureEXT completion
    auto waitUntilReady = [&](XrFutureEXT future) {
      XrFuturePollInfoEXT pollInfo{XR_TYPE_FUTURE_POLL_INFO_EXT};
      XrFuturePollResultEXT pollResult{XR_TYPE_FUTURE_POLL_RESULT_EXT};
      pollInfo.future = future;
      do {
        // sleep(1);
        CHK_XR(xrPollFutureEXT(instance, &pollInfo, &pollResult));
      } while (pollResult.state != XR_FUTURE_STATE_READY_EXT);
    };

    // Data/metadata about reference images (identifiers, 3D models, trigger functions, etc.)
    std::vector<std::string> referenceImageIdentifiers;

    XrSpatialImageTrackingDatabaseEXT imageTrackingDatabase{};
    {
      uint32_t imgSize; // preloaded interleaved RGBA buffer size
      uint8_t* img; // preloaded interleaved RGBA buffer data

      // interleaved RGBA buffer memory layout and buffer positions

      // first row of pixels
      // img[0] | img[1] | img[2] | img[3] | img[0]+pStride | img[1]+pStride | ...
      //  R0    |   G0   |   B0   |   A0   |       R1       |       G1       | ...

      // second row of pixels
      // img[0]+rStride | img[1]+rStride | img[2]+rStride | img[3]+rStride | img[0]+rStride+pStride | ...
      //      R640      |      G640      |      B640      |      A640      |          R641          | ...

      XrSpatialReferenceImagePlaneEXT spatialReferenceImagePlanes[4];

      for (int i = 0; i < 4; ++i) { // for each plane (0=R, 1=G, 2=B, 3=A)
        spatialReferenceImagePlanes[i].buffer = img + i; // set each plane buffer pointer to the first pixel of the plane
        spatialReferenceImagePlanes[i].bufferSize = imgSize - i; // adjust remeinaing buffer size according to offset applied
        spatialReferenceImagePlanes[i].rowStride = 640 * 4; // set byte offset to start of next row for this plane
        spatialReferenceImagePlanes[i].pixelStride = 4; // set byte offset to next pixel for this plane
      }

      XrSpatialReferenceImageEXT spatialReferenceImage{XR_TYPE_SPATIAL_REFERENCE_IMAGE_EXT};
      spatialReferenceImage.width = 640;
      spatialReferenceImage.height = 480;
      spatialReferenceImage.format = XR_SPATIAL_REFERENCE_IMAGE_FORMAT_RGBA_8888_EXT;
      spatialReferenceImage.planeCount = 4;
      spatialReferenceImage.planes = spatialReferenceImagePlanes;

      referenceImageIdentifiers.emplace_back("MyReferenceImage");

      // Helper function to append to the next chain
      XrBaseOutStructure* appendTo = reinterpret_cast<XrBaseOutStructure*>(&spatialReferenceImage);
      const auto appendToNextChain = [&appendTo](XrBaseOutStructure* toAppend) {
        appendTo->next = toAppend;
        appendTo = toAppend;
      };

      XrSpatialImageSizeEXT imageSize{XR_TYPE_SPATIAL_IMAGE_SIZE_EXT};
      imageSize.physicalWidth = 0.1f;

      if (!supportsAutomaticScaleEstimation) {
        if (supportsFixedSizeImages) {
          appendToNextChain(reinterpret_cast<XrBaseOutStructure*>(&imageSize));
        }
      }

      XrSpatialImageStaticOptimizationEXT imageStaticOptimization{XR_TYPE_SPATIAL_IMAGE_STATIC_OPTIMIZATION_EXT};
      imageStaticOptimization.optimizeForStaticImage = XR_TRUE;

      if (supportsStaticImages) {
        appendToNextChain(reinterpret_cast<XrBaseOutStructure*>(&imageStaticOptimization));
      }

      XrSpatialImageTrackingDatabaseCreateInfoEXT spatialImageTrackingDatabaseCreateInfo{XR_TYPE_SPATIAL_IMAGE_TRACKING_DATABASE_CREATE_INFO_EXT};
      spatialImageTrackingDatabaseCreateInfo.spatialReferenceImages = &spatialReferenceImage;
      spatialImageTrackingDatabaseCreateInfo.spatialReferenceImageCount = 1;

      XrFutureEXT createImageTrackingDatabaseFuture = XR_NULL_FUTURE_EXT;
      CHK_XR(xrCreateSpatialImageTrackingDatabaseAsyncEXT(session, &spatialImageTrackingDatabaseCreateInfo, &createImageTrackingDatabaseFuture));

      waitUntilReady(createImageTrackingDatabaseFuture);

      XrCreateSpatialImageTrackingDatabaseCompletionEXT imageTrackingCompletion{XR_TYPE_CREATE_SPATIAL_IMAGE_TRACKING_DATABASE_COMPLETION_EXT};
      CHK_XR(xrCreateSpatialImageTrackingDatabaseCompleteEXT(session, createImageTrackingDatabaseFuture, &imageTrackingCompletion));
      if (imageTrackingCompletion.futureResult != XR_SUCCESS) {
        // Error, image tracking database creation failed
      }

      imageTrackingDatabase = imageTrackingCompletion.database;
    }

    XrSpatialContextEXT spatialContext{};
    {
      const std::array<XrSpatialComponentTypeEXT, 2> enabledComponents = {
        XR_SPATIAL_COMPONENT_TYPE_BOUNDED_2D_EXT,
        XR_SPATIAL_COMPONENT_TYPE_IMAGE_2D_EXT
      };

      // Configure the image tracking capability for the spatial context
      XrSpatialCapabilityConfigurationImageTrackingEXT imageTrackingCapabilityConfig{XR_TYPE_SPATIAL_CAPABILITY_CONFIGURATION_IMAGE_TRACKING_EXT};
      imageTrackingCapabilityConfig.capability = XR_SPATIAL_CAPABILITY_IMAGE_TRACKING_EXT;
      imageTrackingCapabilityConfig.enabledComponentCount = enabledComponents.size();
      imageTrackingCapabilityConfig.enabledComponents = enabledComponents.data();
      imageTrackingCapabilityConfig.imageTrackingDatabaseCount = 1;
      imageTrackingCapabilityConfig.imageTrackingDatabases = &imageTrackingDatabase;

      std::vector<XrSpatialCapabilityConfigurationBaseHeaderEXT*> capabilityConfigs;
      capabilityConfigs.push_back(reinterpret_cast<XrSpatialCapabilityConfigurationBaseHeaderEXT*>(&imageTrackingCapabilityConfig));

      XrSpatialContextCreateInfoEXT spatialContextCreateInfo{XR_TYPE_SPATIAL_CONTEXT_CREATE_INFO_EXT};
      spatialContextCreateInfo.capabilityConfigCount = capabilityConfigs.size();
      spatialContextCreateInfo.capabilityConfigs = capabilityConfigs.data();

      XrFutureEXT createContextFuture = XR_NULL_FUTURE_EXT;
      CHK_XR(xrCreateSpatialContextAsyncEXT(session, &spatialContextCreateInfo, &createContextFuture));

      waitUntilReady(createContextFuture);

      XrCreateSpatialContextCompletionEXT completion{XR_TYPE_CREATE_SPATIAL_CONTEXT_COMPLETION_EXT};
      CHK_XR(xrCreateSpatialContextCompleteEXT(session, createContextFuture, &completion));
      if (completion.futureResult != XR_SUCCESS) {
        // Error, spatial context creation failed
      }

      spatialContext = completion.spatialContext;
    }

    auto discoverSpatialEntities = [&](XrSpatialContextEXT spatialContext, XrTime time) {
      // We want to look for entities that have the following components
      std::array<XrSpatialComponentTypeEXT, 2> snapshotComponents {XR_SPATIAL_COMPONENT_TYPE_BOUNDED_2D_EXT, XR_SPATIAL_COMPONENT_TYPE_IMAGE_2D_EXT};

      XrSpatialDiscoverySnapshotCreateInfoEXT snapshotCreateInfo{XR_TYPE_SPATIAL_DISCOVERY_SNAPSHOT_CREATE_INFO_EXT};
      snapshotCreateInfo.componentTypeCount = snapshotComponents.size();
      snapshotCreateInfo.componentTypes = snapshotComponents.data();
      XrFutureEXT discoveryFuture = XR_NULL_FUTURE_EXT;
      CHK_XR(xrCreateSpatialDiscoverySnapshotAsyncEXT(spatialContext, &snapshotCreateInfo, &discoveryFuture));

      waitUntilReady(discoveryFuture);

      XrCreateSpatialDiscoverySnapshotCompletionInfoEXT completionInfo{XR_TYPE_CREATE_SPATIAL_DISCOVERY_SNAPSHOT_COMPLETION_INFO_EXT};
      completionInfo.baseSpace = localSpace;
      completionInfo.time = time;
      completionInfo.future = discoveryFuture;

      XrCreateSpatialDiscoverySnapshotCompletionEXT completion{XR_TYPE_CREATE_SPATIAL_DISCOVERY_SNAPSHOT_COMPLETION_EXT};
      CHK_XR(xrCreateSpatialDiscoverySnapshotCompleteEXT(spatialContext, &completionInfo, &completion));
      if (completion.futureResult == XR_SUCCESS) {
        // Query for the bounded2d component data
        XrSpatialComponentTypeEXT componentsToQuery[] = {XR_SPATIAL_COMPONENT_TYPE_BOUNDED_2D_EXT, XR_SPATIAL_COMPONENT_TYPE_IMAGE_2D_EXT};
        XrSpatialComponentDataQueryConditionEXT queryCond{XR_TYPE_SPATIAL_COMPONENT_DATA_QUERY_CONDITION_EXT};
        queryCond.componentTypes = componentsToQuery;

        XrSpatialComponentDataQueryResultEXT queryResult{XR_TYPE_SPATIAL_COMPONENT_DATA_QUERY_RESULT_EXT};
        CHK_XR(xrQuerySpatialComponentDataEXT(completion.snapshot, &queryCond, &queryResult));

        std::vector<XrSpatialEntityIdEXT> entityIds(queryResult.entityIdCountOutput);
        std::vector<XrSpatialEntityTrackingStateEXT> entityStates(queryResult.entityStateCountOutput);
        queryResult.entityIdCapacityInput = entityIds.size();
        queryResult.entityIds = entityIds.data();
        queryResult.entityStateCapacityInput = entityStates.size();
        queryResult.entityStates = entityStates.data();

        std::vector<XrSpatialBounded2DDataEXT> bounded2d(queryResult.entityIdCountOutput);
        XrSpatialComponentBounded2DListEXT boundsList{XR_TYPE_SPATIAL_COMPONENT_BOUNDED_2D_LIST_EXT};
        boundsList.boundCount = bounded2d.size();
        boundsList.bounds = bounded2d.data();
        queryResult.next = &boundsList;

        std::vector<XrSpatialImage2DDataEXT> image2d(queryResult.entityIdCountOutput);
        XrSpatialComponentImage2DListEXT imagesList{XR_TYPE_SPATIAL_COMPONENT_IMAGE_2D_LIST_EXT};
        imagesList.imageCount = image2d.size();
        imagesList.images = image2d.data();
        queryResult.next = &imagesList;

        CHK_XR(xrQuerySpatialComponentDataEXT(completion.snapshot, &queryCond, &queryResult));

        for (int32_t i = 0; i < queryResult.entityIdCountOutput; ++i) {
          if (entityStates[i] == XR_SPATIAL_ENTITY_TRACKING_STATE_TRACKING_EXT) {
            const XrSpatialImage2DDataEXT& currentImage2d = image2d[i];
            const std::string& currentReferenceImageIdentifier = referenceImageIdentifiers[currentImage2d.referenceImageIndex];
            std::cout << currentReferenceImageIdentifier << std::endl; // Outputs the "MyReferenceImage" string the app defined previously; could be any other assocatied data or action.

            // Access bounded2d[i] for image bounds
          }
        }

        CHK_XR(xrDestroySpatialSnapshotEXT(completion.snapshot));
      }
    };

    while (1) {
      // For every frame in frame loop

      XrFrameState frameState;  // Previously returned from xrWaitFrame
      const XrTime time = frameState.predictedDisplayTime;

      // Poll for the XR_TYPE_EVENT_DATA_SPATIAL_DISCOVERY_RECOMMENDED_EXT event
      XrEventDataBuffer event = {XR_TYPE_EVENT_DATA_BUFFER};
      XrResult result = xrPollEvent(instance, &event);
      if (result == XR_SUCCESS) {
          switch (event.type) {
              case XR_TYPE_EVENT_DATA_SPATIAL_DISCOVERY_RECOMMENDED_EXT: {
                  const XrEventDataSpatialDiscoveryRecommendedEXT& eventdata = *reinterpret_cast<XrEventDataSpatialDiscoveryRecommendedEXT*>(&event);
                  // Discover spatial entities for the context that we received the "discovery
                  // recommended" event for
                  discoverSpatialEntities(eventdata.spatialContext, time);
                  break;
              }
          }
      }

      // Finish frame loop
    }

    CHK_XR(xrDestroySpatialContextEXT(spatialContext));

    // Unload spatial image tracking resources internally
    CHK_XR(xrDestroySpatialImageTrackingDatabaseEXT(imageTrackingDatabase));

## New Object Types

- [XrSpatialImageTrackingDatabaseEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageTrackingDatabaseEXT)

## New Commands

- [xrCreateSpatialImageTrackingDatabaseAsyncEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#xrCreateSpatialImageTrackingDatabaseAsyncEXT)
- [xrCreateSpatialImageTrackingDatabaseCompleteEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#xrCreateSpatialImageTrackingDatabaseCompleteEXT)
- [xrDestroySpatialImageTrackingDatabaseEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#xrDestroySpatialImageTrackingDatabaseEXT)
- [xrEnumerateSpatialReferenceImageFormatsEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#xrEnumerateSpatialReferenceImageFormatsEXT)

## New Structures

- [XrCreateSpatialImageTrackingDatabaseCompletionEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrCreateSpatialImageTrackingDatabaseCompletionEXT)
- [XrSpatialCapabilityConfigurationImageTrackingEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialCapabilityConfigurationImageTrackingEXT)
- [XrSpatialImage2DDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImage2DDataEXT)
- [XrSpatialImageTrackingDatabaseCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageTrackingDatabaseCreateInfoEXT)
- [XrSpatialReferenceImageEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialReferenceImageEXT)
- [XrSpatialReferenceImagePlaneEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialReferenceImagePlaneEXT)
- Extending [XrSpatialComponentDataQueryResultEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryResultEXT) :

  - [XrSpatialComponentImage2DListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialComponentImage2DListEXT)
- Extending [XrSpatialReferenceImageEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialReferenceImageEXT) , [XrSpatialImageTrackingDatabaseCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageTrackingDatabaseCreateInfoEXT) :

  - [XrSpatialImageSizeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageSizeEXT)
  - [XrSpatialImageStaticOptimizationEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialImageStaticOptimizationEXT)

## New Enums

- [XrSpatialReferenceImageFormatEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking#XrSpatialReferenceImageFormatEXT)

## New Enum Constants

- `XR_EXT_SPATIAL_IMAGE_TRACKING_EXTENSION_NAME`
- `XR_EXT_spatial_image_tracking_SPEC_VERSION`
- Extending [XrObjectType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrObjectType) :

  - `XR_OBJECT_TYPE_SPATIAL_IMAGE_TRACKING_DATABASE_EXT`
- Extending [XrResult](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrResult) :

  - `XR_ERROR_SPATIAL_IMAGE_FORMAT_UNSUPPORTED_EXT`
  - `XR_ERROR_SPATIAL_IMAGE_INVALID_EXT`
  - `XR_ERROR_SPATIAL_IMAGE_SIZE_MISSING_EXT`
- Extending [XrSpatialCapabilityEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityEXT) :

  - `XR_SPATIAL_CAPABILITY_IMAGE_TRACKING_EXT`
- Extending [XrSpatialCapabilityFeatureEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityFeatureEXT) :

  - `XR_SPATIAL_CAPABILITY_FEATURE_IMAGE_TRACKING_AUTOMATIC_SIZE_IMAGES_EXT`
  - `XR_SPATIAL_CAPABILITY_FEATURE_IMAGE_TRACKING_FIXED_SIZE_IMAGES_EXT`
  - `XR_SPATIAL_CAPABILITY_FEATURE_IMAGE_TRACKING_STATIC_IMAGES_EXT`
- Extending [XrSpatialComponentTypeEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentTypeEXT) :

  - `XR_SPATIAL_COMPONENT_TYPE_IMAGE_2D_EXT`
- Extending [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) :

  - `XR_TYPE_CREATE_SPATIAL_IMAGE_TRACKING_DATABASE_COMPLETION_EXT`
  - `XR_TYPE_SPATIAL_CAPABILITY_CONFIGURATION_IMAGE_TRACKING_EXT`
  - `XR_TYPE_SPATIAL_COMPONENT_IMAGE_2D_LIST_EXT`
  - `XR_TYPE_SPATIAL_IMAGE_SIZE_EXT`
  - `XR_TYPE_SPATIAL_IMAGE_STATIC_OPTIMIZATION_EXT`
  - `XR_TYPE_SPATIAL_IMAGE_TRACKING_DATABASE_CREATE_INFO_EXT`
  - `XR_TYPE_SPATIAL_REFERENCE_IMAGE_EXT`

## Issues

## Version History

- Revision 1, 2025-04-22 (Daniel Guttenberg, Qualcomm)

  - Initial extension description