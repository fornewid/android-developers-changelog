---
title: https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture
url: https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture
source: md.txt
---

**Name String**

`XR_ANDROID_depth_texture`

**Extension Type**

Instance extension

**Registered Extension Number**

703

**Revision**

1

**Extension and Version Dependencies**

[OpenXR 1.0](https://registry.khronos.org/OpenXR/specs/1.0/html/xrspec.html#versions-1.0)

**Last Modified Date**

2024-09-11

**IP Status**

No known IP claims.

**Contributors**

Sushant Kulkarni, Google

Cairn Overturf, Google

Spencer Quin, Google

Levana Chen, Google

## Overview

This extension allows the application to request depth maps of the real-world
environment around the headset and query supported depth resolutions at
creation.

This extension is intended to expose raw and smooth depth for occlusion, hit
tests and other specific tasks that make use of accurate scene geometry, for
example, counterfeit face detection.

> [!CAUTION]
> **Caution:**   
>
> **Permissions**   
> This extension exposes a downsampled depth texture to mitigate PII concerns. Android applications **must** have the `android.permission.SCENE_UNDERSTANDING_FINE` permission listed in their manifest as this extension exposes the geometry of the environment.  
>
> The `android.permission.SCENE_UNDERSTANDING_FINE` permission is considered a dangerous permission. The application **must** request the [permission at runtime](https://developer.android.com/training/permissions/requesting) to use these functions:  
> [`xrCreateDepthSwapchainANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#xrCreateDepthSwapchainANDROID)  
> (protection level: dangerous)

## Inspect system capability

The [XrSystemDepthTrackingPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrSystemDepthTrackingPropertiesANDROID) structure is defined
as:

    typedef struct XrSystemDepthTrackingPropertiesANDROID {
        XrStructureType    type;
        const void*        next;
        XrBool32           supportsDepthTracking;
    } XrSystemDepthTrackingPropertiesANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.
- `supportsDepthTracking` is an [`XrBool32`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrBool32) indicating if current system supports depth tracking.

An application **can** inspect whether the system is capable of depth tracking
by extending the [XrSystemProperties](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSystemProperties) with
[XrSystemDepthTrackingPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrSystemDepthTrackingPropertiesANDROID) structure when calling
[xrGetSystemProperties](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrGetSystemProperties).

### Valid Usage (Implicit)

- The [`XR_ANDROID_depth_texture`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XR_ANDROID_depth_texture) extension **must** be enabled prior to using [XrSystemDepthTrackingPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrSystemDepthTrackingPropertiesANDROID)
- `type` **must** be `XR_TYPE_SYSTEM_DEPTH_TRACKING_PROPERTIES_ANDROID`
- `next` **must** be `NULL` or a valid pointer to the [next structure in a
  structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-valid-usage-for-structure-pointer-chains)

## Query depth resolutions

The [xrEnumerateDepthResolutionsANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#xrEnumerateDepthResolutionsANDROID) function is defined as:

    XrResult xrEnumerateDepthResolutionsANDROID(
        XrSession                                   session,
        uint32_t                                    resolutionCapacityInput,
        uint32_t*                                   resolutionCountOutput,
        XrDepthCameraResolutionANDROID*             resolutions);

### Parameter Descriptions

- `session` is the [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) that enumerates the supported depth resolutions.
- `resolutionCapacityInput` is the capacity of the `resolutions`, or 0 to retrieve the required capacity.
- `resolutionCountOutput` is a pointer to the count of `uint64_t` `resolutions` written, or a pointer to the required capacity in the case that `resolutionCapacityInput` is insufficient.
- `resolutions` is a pointer to an array of [XrDepthCameraResolutionANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthCameraResolutionANDROID), but **can** be `NULL` if `resolutionCapacityInput` is 0.
- See the [Buffer Size Parameters](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-buffer-size-parameters) section for a detailed description of retrieving the required `resolutions` size.

[xrEnumerateDepthResolutionsANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#xrEnumerateDepthResolutionsANDROID) enumerates the depth
resolutions supported by the current session. Depth resolutions **should** be in
order from highest to lowest runtime preference. The application **should** use
the highest preference that it supports for optimal performance and quality.

### Valid Usage (Implicit)

- The [`XR_ANDROID_depth_texture`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XR_ANDROID_depth_texture) extension **must** be enabled prior to calling [xrEnumerateDepthResolutionsANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#xrEnumerateDepthResolutionsANDROID)
- `session` **must** be a valid [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) handle
- `resolutionCountOutput` **must** be a pointer to a `uint32_t` value
- If `resolutionCapacityInput` is not 0, `resolutions` **must** be a pointer to an array of `resolutionCapacityInput` [XrDepthCameraResolutionANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthCameraResolutionANDROID) values

### Return Codes

[**Success**](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`
- `XR_SESSION_LOSS_PENDING`

[**Failure**](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_VALIDATION_FAILURE`
- `XR_ERROR_RUNTIME_FAILURE`
- `XR_ERROR_HANDLE_INVALID`
- `XR_ERROR_INSTANCE_LOST`
- `XR_ERROR_SESSION_LOST`
- `XR_ERROR_SIZE_INSUFFICIENT`

The [XrDepthCameraResolutionANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthCameraResolutionANDROID) enum describes the
supported depth resolutions when creating an
[XrDepthSwapchainANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthSwapchainANDROID).

    typedef enum XrDepthCameraResolutionANDROID {
        XR_DEPTH_CAMERA_RESOLUTION_80x80_ANDROID = 0,
        XR_DEPTH_CAMERA_RESOLUTION_160x160_ANDROID = 1,
        XR_DEPTH_CAMERA_RESOLUTION_320x320_ANDROID = 2
        } XrDepthCameraResolutionANDROID;

### Enumerant Descriptions

- `XR_DEPTH_CAMERA_RESOLUTION_80x80_ANDROID` --- The resolution of the depth and confidence images is 80x80.
- `XR_DEPTH_CAMERA_RESOLUTION_160x160_ANDROID` --- The resolution of the depth and confidence images is 160x160.
- `XR_DEPTH_CAMERA_RESOLUTION_320x320_ANDROID` --- The resolution of the depth and confidence images is 320x320.

## Create a depth swapchain

    XR_DEFINE_HANDLE(XrDepthSwapchainANDROID)

An [XrDepthSwapchainANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthSwapchainANDROID) is a depth swapchain handle.

The [xrCreateDepthSwapchainANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#xrCreateDepthSwapchainANDROID) function is defined as:

    XrResult xrCreateDepthSwapchainANDROID(
        XrSession                                   session,
        const XrDepthSwapchainCreateInfoANDROID*    createInfo,
        XrDepthSwapchainANDROID*                    swapchain);

### Parameter Descriptions

- `session` is the [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) that creates the depth swapchain.

- `createInfo` is a pointer to an
  [XrDepthSwapchainCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthSwapchainCreateInfoANDROID) structure containing
  parameters to be used to create the swapchain.

- `swapchain` is a pointer to a handle in which the created
  [XrDepthSwapchainANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthSwapchainANDROID) is returned.

The application **can** use [xrCreateDepthSwapchainANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#xrCreateDepthSwapchainANDROID)
function to create a depth swapchain which manages both depth and confidence
images.

The returned depth swapchain handle **may** be subsequently used in API calls.
The [XrDepthSwapchainANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthSwapchainANDROID) handle **must** be eventually freed
using the [xrDestroyDepthSwapchainANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#xrDestroyDepthSwapchainANDROID) function.

### Valid Usage (Implicit)

- The [`XR_ANDROID_depth_texture`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XR_ANDROID_depth_texture) extension **must** be enabled prior to calling [xrCreateDepthSwapchainANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#xrCreateDepthSwapchainANDROID)
- `session` **must** be a valid [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) handle
- `createInfo` **must** be a pointer to a valid [XrDepthSwapchainCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthSwapchainCreateInfoANDROID) structure
- `swapchain` **must** be a pointer to an [XrDepthSwapchainANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthSwapchainANDROID) handle

### Return Codes

[**Success**](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`
- `XR_SESSION_LOSS_PENDING`

[**Failure**](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_RUNTIME_FAILURE`
- `XR_ERROR_INSTANCE_LOST`
- `XR_ERROR_SESSION_LOST`
- `XR_ERROR_OUT_OF_MEMORY`
- `XR_ERROR_HANDLE_INVALID`
- `XR_ERROR_LIMIT_REACHED`

The [XrDepthSwapchainCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthSwapchainCreateInfoANDROID) structure is defined as:

    typedef struct XrDepthSwapchainCreateInfoANDROID {
        XrStructureType                       type;
        const void*                           next;
        XrDepthCameraResolutionANDROID        resolution;
        XrDepthSwapchainCreateFlagsANDROID    createFlags;
    } XrDepthSwapchainCreateInfoANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.
- `resolution` is the [XrDepthCameraResolutionANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthCameraResolutionANDROID) that the depth and confidence textures should be created in.
- `createFlags` is one or more [XrDepthSwapchainCreateFlagsANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthSwapchainCreateFlagsANDROID).

The [XrDepthSwapchainCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthSwapchainCreateInfoANDROID) structure provides
creation options for the [XrDepthSwapchainANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthSwapchainANDROID) when passed to
[xrCreateDepthSwapchainANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#xrCreateDepthSwapchainANDROID).

### Valid Usage (Implicit)

- The [`XR_ANDROID_depth_texture`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XR_ANDROID_depth_texture) extension **must** be enabled prior to using [XrDepthSwapchainCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthSwapchainCreateInfoANDROID)
- `type` **must** be `XR_TYPE_DEPTH_SWAPCHAIN_CREATE_INFO_ANDROID`
- `next` **must** be `NULL` or a valid pointer to the [next structure in a
  structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-valid-usage-for-structure-pointer-chains)
- `resolution` **must** be a valid [XrDepthCameraResolutionANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthCameraResolutionANDROID) value
- `createFlags` **must** be a valid combination of [XrDepthSwapchainCreateFlagBitsANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthSwapchainCreateFlagBitsANDROID) values
- `createFlags` **must** not be 0

The [XrDepthSwapchainCreateFlagsANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthSwapchainCreateFlagsANDROID) specifies creation
options for [XrDepthSwapchainANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthSwapchainANDROID).

    typedef XrFlags64 XrDepthSwapchainCreateFlagsANDROID;

Valid bits for [XrDepthSwapchainCreateFlagsANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthSwapchainCreateFlagsANDROID) are defined
by [XrDepthSwapchainCreateFlagBitsANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthSwapchainCreateFlagBitsANDROID), which is specified
as:

    // Flag bits for XrDepthSwapchainCreateFlagsANDROID
    static const XrDepthSwapchainCreateFlagsANDROID XR_DEPTH_SWAPCHAIN_CREATE_SMOOTH_DEPTH_IMAGE_BIT_ANDROID = 0x00000001;
    static const XrDepthSwapchainCreateFlagsANDROID XR_DEPTH_SWAPCHAIN_CREATE_SMOOTH_CONFIDENCE_IMAGE_BIT_ANDROID = 0x00000002;
    static const XrDepthSwapchainCreateFlagsANDROID XR_DEPTH_SWAPCHAIN_CREATE_RAW_DEPTH_IMAGE_BIT_ANDROID = 0x00000004;
    static const XrDepthSwapchainCreateFlagsANDROID XR_DEPTH_SWAPCHAIN_CREATE_RAW_CONFIDENCE_IMAGE_BIT_ANDROID = 0x00000008;

The [xrDestroyDepthSwapchainANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#xrDestroyDepthSwapchainANDROID) function is defined as:

    XrResult xrDestroyDepthSwapchainANDROID(
        XrDepthSwapchainANDROID                     swapchain);

### Parameter Descriptions

- `swapchain` is an [XrDepthSwapchainANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthSwapchainANDROID) handle previously created by `xrCreateDepthSwapchainANDROID`.

The [xrDestroyDepthSwapchainANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#xrDestroyDepthSwapchainANDROID) function destroys the depth
swapchain.

### Valid Usage (Implicit)

- The [`XR_ANDROID_depth_texture`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XR_ANDROID_depth_texture) extension **must** be enabled prior to calling [xrDestroyDepthSwapchainANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#xrDestroyDepthSwapchainANDROID)
- `swapchain` **must** be a valid [XrDepthSwapchainANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthSwapchainANDROID) handle

### Thread Safety

- Access to `swapchain`, and any child handles, **must** be externally synchronized

### Return Codes

[**Success**](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`

[**Failure**](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_HANDLE_INVALID`

## Access depth textures

The [xrEnumerateDepthSwapchainImagesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#xrEnumerateDepthSwapchainImagesANDROID) function is defined
as:

    XrResult xrEnumerateDepthSwapchainImagesANDROID(
        XrDepthSwapchainANDROID                     depthSwapchain,
        uint32_t                                    depthImageCapacityInput,
        uint32_t*                                   depthImageCountOutput,
        XrDepthSwapchainImageANDROID*               depthImages);

### Parameter Descriptions

- `depthSwapchain` is the [XrDepthSwapchainANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthSwapchainANDROID) to get images from.
- `depthImageCapacityInput` is the capacity of the `depthImages` array, or 0 to indicate a request to retrieve the required capacity.
- `depthImageCountOutput` is a pointer to the count of `depthImages` written, or a pointer to the required capacity in the case that `depthImageCapacityInput` is insufficient.
- `depthImages` is a pointer to an array of [XrDepthSwapchainImageANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthSwapchainImageANDROID) structures. It **can** be `NULL` if `depthImageCapacityInput` is 0.
- See the [Buffer Size Parameters](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-buffer-size-parameters) section for a detailed description of retrieving the required `depthImages` size.

[xrEnumerateDepthSwapchainImagesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#xrEnumerateDepthSwapchainImagesANDROID) fills an array of
[XrDepthSwapchainImageANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthSwapchainImageANDROID) structures. The resources
will be constant and valid for the lifetime of the
[XrDepthSwapchainANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthSwapchainANDROID). This function behaves analogously to
[xrEnumerateSwapchainImages](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrEnumerateSwapchainImages).

### Valid Usage (Implicit)

- The [`XR_ANDROID_depth_texture`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XR_ANDROID_depth_texture) extension **must** be enabled prior to calling [xrEnumerateDepthSwapchainImagesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#xrEnumerateDepthSwapchainImagesANDROID)
- `depthSwapchain` **must** be a valid [XrDepthSwapchainANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthSwapchainANDROID) handle
- `depthImageCountOutput` **must** be a pointer to a `uint32_t` value
- If `depthImageCapacityInput` is not 0, `depthImages` **must** be a pointer to an array of `depthImageCapacityInput` [XrDepthSwapchainImageANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthSwapchainImageANDROID) structures

### Return Codes

[**Success**](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`
- `XR_SESSION_LOSS_PENDING`

[**Failure**](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_VALIDATION_FAILURE`
- `XR_ERROR_RUNTIME_FAILURE`
- `XR_ERROR_HANDLE_INVALID`
- `XR_ERROR_INSTANCE_LOST`
- `XR_ERROR_SESSION_LOST`
- `XR_ERROR_SIZE_INSUFFICIENT`

The [XrDepthSwapchainImageANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthSwapchainImageANDROID) structure is defined as:

    typedef struct XrDepthSwapchainImageANDROID {
        XrStructureType    type;
        void*              next;
        const float*       rawDepthImage;
        const uint8_t*     rawDepthConfidenceImage;
        const float*       smoothDepthImage;
        const uint8_t*     smoothDepthConfidenceImage;
    } XrDepthSwapchainImageANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.
- `rawDepthImage` is `NULL` or the pointer to raw depth images for both left and right views. The values have units of meters. Special values: `0.0` indicates an invalid or empty depth pixel in the raw depth, `Inf` indicates known depth that is effectively infinitely far away,
- `rawDepthConfidenceImage` is `NULL` or the pointer to raw depth confidence images for both left and right views.
- `smoothDepthImage` is `NULL` or the pointer to smooth depth images for both left and right views. The values have units of meters. Special values: `0.0` indicates an invalid or empty depth pixel in the smooth depth, `Inf` indicates known depth that is effectively infinitely far away.
- `smoothDepthConfidenceImage` is `NULL` or the pointer to smooth depth confidence images for both left and right views.

[XrDepthSwapchainImageANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthSwapchainImageANDROID) represents the depth images from a
readable [XrDepthSwapchainANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthSwapchainANDROID), allocated as described in the
[XrDepthSwapchainCreateInfoANDROID::resolution](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthSwapchainCreateInfoANDROID) and
[XrDepthSwapchainCreateInfoANDROID::createFlags](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthSwapchainCreateInfoANDROID) while calling
[xrCreateDepthSwapchainANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#xrCreateDepthSwapchainANDROID). For each depth image:

- Image values are laid out in memory in row-major order, with no padding between rows.
- The first value is the top left and the last value is the bottom right.
- The size of the memory pointed to is determined by the value of [xrEnumerateDepthSwapchainImagesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#xrEnumerateDepthSwapchainImagesANDROID) and set by [XrDepthSwapchainCreateInfoANDROID::resolution](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthSwapchainCreateInfoANDROID) while calling [xrCreateDepthSwapchainANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#xrCreateDepthSwapchainANDROID). For example, if `resolution` is `XR_DEPTH_CAMERA_RESOLUTION_160x160_ANDROID`, the depth images will have size `2*160*160*sizeof(float)`.
- The value of `rawDepthImage` **must** be `NULL` if [XrDepthSwapchainCreateInfoANDROID::createFlags](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthSwapchainCreateInfoANDROID) has not set `XR_DEPTH_SWAPCHAIN_CREATE_RAW_DEPTH_IMAGE_BIT_ANDROID`.
- The value of `rawDepthConfidenceImage` **must** be `NULL` if [XrDepthSwapchainCreateInfoANDROID::createFlags](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthSwapchainCreateInfoANDROID) has not set `XR_DEPTH_SWAPCHAIN_CREATE_RAW_CONFIDENCE_IMAGE_BIT_ANDROID`.
- The value of `smoothDepthImage` **must** be `NULL` if [XrDepthSwapchainCreateInfoANDROID::createFlags](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthSwapchainCreateInfoANDROID) has not set `XR_DEPTH_SWAPCHAIN_CREATE_SMOOTH_DEPTH_IMAGE_BIT_ANDROID`.
- The value of `smoothDepthConfidenceImage` **must** be `NULL` if [XrDepthSwapchainCreateInfoANDROID::createFlags](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthSwapchainCreateInfoANDROID) has not set `XR_DEPTH_SWAPCHAIN_CREATE_SMOOTH_CONFIDENCE_IMAGE_BIT_ANDROID`.

### Valid Usage (Implicit)

- The [`XR_ANDROID_depth_texture`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XR_ANDROID_depth_texture) extension **must** be enabled prior to using [XrDepthSwapchainImageANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthSwapchainImageANDROID)
- `type` **must** be `XR_TYPE_DEPTH_SWAPCHAIN_IMAGE_ANDROID`
- `next` **must** be `NULL` or a valid pointer to the [next structure in a
  structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-valid-usage-for-structure-pointer-chains)

The [xrAcquireDepthSwapchainImagesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#xrAcquireDepthSwapchainImagesANDROID) function is defined
as:

    XrResult xrAcquireDepthSwapchainImagesANDROID(
        XrDepthSwapchainANDROID                     depthSwapchain,
        const XrDepthAcquireInfoANDROID*            acquireInfo,
        XrDepthAcquireResultANDROID*                acquireResult);

### Parameter Descriptions

- `depthSwapchain` is an [XrDepthSwapchainANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthSwapchainANDROID) handle for the depth image.
- `acquireInfo` is an [XrDepthAcquireInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthAcquireInfoANDROID) containing information about how to acquire the depth image.
- `acquireResult` is the returned [XrDepthAcquireResultANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthAcquireResultANDROID) containing information about the acquired depth image.

Applications **can** use [xrAcquireDepthSwapchainImagesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#xrAcquireDepthSwapchainImagesANDROID)
function to acquire the latest available swapchain image index, such as
[XrDepthAcquireResultANDROID::acquiredIndex](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthAcquireResultANDROID), into the
[XrDepthSwapchainImageANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthSwapchainImageANDROID) array enumerated by
[xrEnumerateDepthSwapchainImagesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#xrEnumerateDepthSwapchainImagesANDROID). The returned
[XrDepthAcquireResultANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthAcquireResultANDROID) also contains other information
such as the field of view and pose that are necessary to interpret the depth
data. It is safe to read from the acquired slot in the image array until the
next call to [xrAcquireDepthSwapchainImagesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#xrAcquireDepthSwapchainImagesANDROID).

There **must** be no more than one call to
[xrAcquireDepthSwapchainImagesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#xrAcquireDepthSwapchainImagesANDROID) between any pair of
corresponding [xrBeginFrame](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrBeginFrame) and [xrEndFrame](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrEndFrame)
calls in a session.

### Valid Usage (Implicit)

- The [`XR_ANDROID_depth_texture`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XR_ANDROID_depth_texture) extension **must** be enabled prior to calling [xrAcquireDepthSwapchainImagesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#xrAcquireDepthSwapchainImagesANDROID)
- `depthSwapchain` **must** be a valid [XrDepthSwapchainANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthSwapchainANDROID) handle
- `acquireInfo` **must** be a pointer to a valid [XrDepthAcquireInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthAcquireInfoANDROID) structure
- `acquireResult` **must** be a pointer to an [XrDepthAcquireResultANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthAcquireResultANDROID) structure

### Return Codes

[**Success**](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`
- `XR_SESSION_LOSS_PENDING`

[**Failure**](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_VALIDATION_FAILURE`
- `XR_ERROR_RUNTIME_FAILURE`
- `XR_ERROR_HANDLE_INVALID`
- `XR_ERROR_INSTANCE_LOST`
- `XR_ERROR_SESSION_LOST`
- `XR_ERROR_DEPTH_NOT_AVAILABLE_ANDROID`
- `XR_ERROR_CALL_ORDER_INVALID`
- `XR_ERROR_LIMIT_REACHED`
- `XR_ERROR_TIME_INVALID`

The [XrDepthAcquireInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthAcquireInfoANDROID) structure is defined as:

    typedef struct XrDepthAcquireInfoANDROID {
        XrStructureType    type;
        const void*        next;
        XrSpace            space;
        XrTime             displayTime;
    } XrDepthAcquireInfoANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.
- `space` is an [XrSpace](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpace) defining the reference frame of the returned pose in [XrDepthAcquireResultANDROID::views](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthAcquireResultANDROID).
- `displayTime` is an [`XrTime`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTime) specifying the time used to compute the pose for the returned pose in [XrDepthAcquireResultANDROID::views](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthAcquireResultANDROID). Applications **should** pass their predicted display time for the current frame.

### Valid Usage (Implicit)

- The [`XR_ANDROID_depth_texture`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XR_ANDROID_depth_texture) extension **must** be enabled prior to using [XrDepthAcquireInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthAcquireInfoANDROID)
- `type` **must** be `XR_TYPE_DEPTH_ACQUIRE_INFO_ANDROID`
- `next` **must** be `NULL` or a valid pointer to the [next structure in a
  structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-valid-usage-for-structure-pointer-chains)
- `space` **must** be a valid [XrSpace](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpace) handle

The [XrDepthAcquireResultANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthAcquireResultANDROID) structure is defined as:

    typedef struct XrDepthAcquireResultANDROID {
        XrStructureType       type;
        const void*           next;
        uint32_t              acquiredIndex;
        XrTime                exposureTimestamp;
        XrDepthViewANDROID    views[2];
    } XrDepthAcquireResultANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.
- `acquiredIndex` is the index of the acquired texture into the [XrDepthSwapchainImageANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthSwapchainImageANDROID) array enumerated by [xrEnumerateDepthSwapchainImagesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#xrEnumerateDepthSwapchainImagesANDROID).
- `exposureTimestamp` is the [`XrTime`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTime) specifying the time at which the depth map was captured.
- `views` is an array of two [XrDepthViewANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthViewANDROID), one for each eye, where index 0 is left eye and index 1 is the right eye.

### Valid Usage (Implicit)

- The [`XR_ANDROID_depth_texture`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XR_ANDROID_depth_texture) extension **must** be enabled prior to using [XrDepthAcquireResultANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthAcquireResultANDROID)
- `type` **must** be `XR_TYPE_DEPTH_ACQUIRE_RESULT_ANDROID`
- `next` **must** be `NULL` or a valid pointer to the [next structure in a
  structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-valid-usage-for-structure-pointer-chains)
- Any given element of `views` **must** be a valid [XrDepthViewANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthViewANDROID) structure

The [XrDepthViewANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthViewANDROID) structure is defined as:

    typedef struct XrDepthViewANDROID {
        XrStructureType    type;
        const void*        next;
        XrFovf             fov;
        XrPosef            pose;
    } XrDepthViewANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.
- `fov` is an [XrFovf](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrFovf) specifying the field of view used to generate this view. The view is never flipped horizontally nor vertically.
- `pose` is an [XrPosef](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrPosef) specifying the pose from which the depth map was rendered. The reference frame is specified in [XrDepthAcquireInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthAcquireInfoANDROID).

### Valid Usage (Implicit)

- The [`XR_ANDROID_depth_texture`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XR_ANDROID_depth_texture) extension **must** be enabled prior to using [XrDepthViewANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthViewANDROID)
- `type` **must** be `XR_TYPE_DEPTH_VIEW_ANDROID`
- `next` **must** be `NULL` or a valid pointer to the [next structure in a
  structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-valid-usage-for-structure-pointer-chains)

## Example code for depth tracking

The following example code demonstrates how to acquire depth images.

    XrInstance instance;  // previously initialized
    XrSystemId systemId;  // previously initialized
    XrSession session; // previously initialized
    XrSpace stageSpace; // space created for XR_REFERENCE_SPACE_TYPE_STAGE.

    // The function pointers are previously initialized using xrGetInstanceProcAddr.
    PFN_xrCreateDepthSwapchainANDROID xrCreateDepthSwapchainANDROID; // previously initialized
    PFN_xrDestroyDepthSwapchainANDROID xrDestroyDepthSwapchainANDROID; // previously initialized
    PFN_xrEnumerateDepthSwapchainImagesANDROID xrEnumerateDepthSwapchainImagesANDROID; // previously initialized
    PFN_xrEnumerateDepthResolutionsANDROID xrEnumerateDepthResolutionsANDROID; // previously initialized
    PFN_xrAcquireDepthSwapchainImagesANDROID xrAcquireDepthSwapchainImagesANDROID; // previously initialized

    // Inspect system capability
    XrSystemProperties properties{XR_TYPE_SYSTEM_PROPERTIES};
    XrSystemDepthTrackingPropertiesANDROID depthTrackingProperties{XR_TYPE_SYSTEM_DEPTH_TRACKING_PROPERTIES_ANDROID};
    properties.next = &depthTrackingProperties;
    CHK_XR(xrGetSystemProperties(instance, systemId, &properties));
    if (!depthTrackingProperties.supportsDepthTracking) {
      // depth tracking is not supported.
      return;
    }

    // Query the supported depth resolution.
    XrDepthCameraResolutionANDROID supportedDepthResolution;
    uint32_t supportedResolutionCount = 0;
    CHK_XR(xrEnumerateDepthResolutionsANDROID(
        session, 1, &supportedResolutionCount, &supportedDepthResolution));

    // Define metadata to access the raw and smooth depth along with confidences.
    XrDepthSwapchainCreateInfoANDROID swapchainCreateInfo = {
      .type = XR_TYPE_DEPTH_SWAPCHAIN_CREATE_INFO_ANDROID,
      .next = nullptr,
      .createFlags =
        XR_DEPTH_SWAPCHAIN_CREATE_SMOOTH_DEPTH_IMAGE_BIT_ANDROID |
        XR_DEPTH_SWAPCHAIN_CREATE_SMOOTH_CONFIDENCE_IMAGE_BIT_ANDROID |
        XR_DEPTH_SWAPCHAIN_CREATE_RAW_DEPTH_IMAGE_BIT_ANDROID |
        XR_DEPTH_SWAPCHAIN_CREATE_RAW_CONFIDENCE_IMAGE_BIT_ANDROID,

      // Use the resolution supported by the runtime.
      .resolution = supportedDepthResolution,
    };

    XrDepthSwapchainANDROID depthSwapchain;
    CHK_XR(xrCreateDepthSwapchainANDROID(
        session, &swapchainCreateInfo, &depthSwapchain));

    // Enumerate depth images.
    uint32_t imageCountOutput = 0;
    CHK_XR(xrEnumerateDepthSwapchainImagesANDROID(
        depthSwapchain, 0, &imageCountOutput, nullptr));
    std::vector<XrDepthSwapchainImageANDROID> depthImages(imageCountOutput);
    for (int i = 0; i < imageCountOutput; i++) {
      depthImages[i].type = XR_TYPE_DEPTH_SWAPCHAIN_IMAGE_ANDROID;
    }
    CHK_XR(xrEnumerateDepthSwapchainImagesANDROID(
      depthSwapchain, imageCountOutput, &imageCountOutput, depthImages.data()));

    while (1) {
        // ...
        // For every frame in frame loop
        // ...

        XrFrameState frameState;  // previously returned from xrWaitFrame
        const XrTime time = frameState.predictedDisplayTime;

        XrDepthAcquireInfoANDROID acquireInfo = {
            .type = XR_TYPE_DEPTH_ACQUIRE_INFO_ANDROID,
            .space = stageSpace,
            .displayTime = time};
        XrDepthAcquireResultANDROID acquireResult = {
            .type = XR_TYPE_DEPTH_ACQUIRE_RESULT_ANDROID,
        };
        CHK_XR(xrAcquireDepthImagesANDROID(
            depthSwapchain, &acquireInfo, &acquireResult));

        // Each value in a depth image corresponds to a point in the real world.
        // The sample code in this section shows how to find the stageSpace position
        // of the point corresponding to a particular value in the depth image.

        // For this sample code, assume we are using a right handed coordinate system
        // with +X to the right, +Y up and -Z forward.

        XrDepthSwapchainImageANDROID *image =
            &depthImages[acquireResult.acquireIndex];

        // Assume supported resolution is XR_DEPTH_CAMERA_RESOLUTION_160x160_ANDROID.
        const int imageResolution = 160;
        int imageY = // value in [0, imageResolution)
        int imageX = // value in [0, imageResolution)

        // Get depth value from left eye.
        // A right depth value would be obtained with the following expression:
        // depthR = image->rawDepthImage[imageResolution*imageResolution+i*imageResolution+j]
        float depthL = image->rawDepthImage[imageY*imageResolution + imageX];
        XrDepthViewANDROID viewL = acquireResult.views[0];

        float tanL = tanf(viewL.fov.angleLeft);
        float tanR = tanf(viewL.fov.angleRight);
        float tanU = tanf(viewL.fov.angleUp);
        float tanD = tanf(viewL.fov.angleDown);

        float s = (imageX + 0.5f) / (float)imageResolution;
        float t = (imageY + 0.5f) / (float)imageResolution;

        // Calculate the depth camera space position of the point
        // corresponding to this depth value.
        XrVector3f posInCameraSpace;
        posInCameraSpace.z = -depthL;
        posInCameraSpace.x = (tanL + (tanR - tanL)*s)*depthL;
        posInCameraSpace.y = (tanB + (tanU - tanB)*t)*depthL;

        XrPosef depthCameraPoseL = viewL.pose;
        // Transform posInCameraSpace by depthCameraPoseL

        // ...
        // Finish frame loop
        // ...
    }

### New Object Types

- [XrDepthSwapchainANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthSwapchainANDROID)

### New Enum Constants

[XrObjectType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrObjectType) enumeration is extended with:

- `XR_OBJECT_TYPE_DEPTH_SWAPCHAIN_ANDROID`

[XrResult](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrResult) enumeration is extended with:

- `XR_ERROR_DEPTH_NOT_AVAILABLE_ANDROID`

[XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) enumeration is extended with:

- `XR_TYPE_DEPTH_SWAPCHAIN_CREATE_INFO_ANDROID`
- `XR_TYPE_DEPTH_VIEW_ANDROID`
- `XR_TYPE_DEPTH_ACQUIRE_INFO_ANDROID`
- `XR_TYPE_DEPTH_ACQUIRE_RESULT_ANDROID`
- `XR_TYPE_SYSTEM_DEPTH_TRACKING_PROPERTIES_ANDROID`
- `XR_TYPE_DEPTH_SWAPCHAIN_IMAGE_ANDROID`

### New Enums

- [XrDepthSwapchainCreateFlagsANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthSwapchainCreateFlagsANDROID)
- [XrDepthCameraResolutionANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthCameraResolutionANDROID)

### New Structures

- [XrDepthSwapchainCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthSwapchainCreateInfoANDROID)
- [XrDepthSwapchainImageANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthSwapchainImageANDROID)
- [XrDepthAcquireInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthAcquireInfoANDROID)
- [XrDepthViewANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthViewANDROID)
- [XrDepthAcquireResultANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrDepthAcquireResultANDROID)
- [XrSystemDepthTrackingPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#XrSystemDepthTrackingPropertiesANDROID)

### New Functions

- [xrCreateDepthSwapchainANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#xrCreateDepthSwapchainANDROID)
- [xrDestroyDepthSwapchainANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#xrDestroyDepthSwapchainANDROID)
- [xrEnumerateDepthSwapchainImagesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#xrEnumerateDepthSwapchainImagesANDROID)
- [xrEnumerateDepthResolutionsANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#xrEnumerateDepthResolutionsANDROID)
- [xrAcquireDepthSwapchainImagesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture#xrAcquireDepthSwapchainImagesANDROID)

### Issues

### Version History

- Revision 1, 2024-09-09 (Levana Chen)
  - Initial extension description

*** ** * ** ***

OpenXR™ and the OpenXR logo are trademarks owned
by The Khronos Group Inc. and are registered as a trademark in China,
the European Union, Japan and the United Kingdom.