---
title: https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap
url: https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap
source: md.txt
---

### XR_ANDROID_light_estimation_cubemap

**Name String**

`XR_ANDROID_light_estimation_cubemap`

**Extension Type**

Instance extension

**Registered Extension Number**

722

**Revision**

1

**Ratification Status**

Not ratified

**Extension and Version Dependencies**

`XR_ANDROID_light_estimation`

**Last Modified Date**

2025-08-06

**IP Status**

No known IP claims.

**Contributors**

Salar Khan, Google  

Scott Chung, Google  

Jared Finder, Google  

Spencer Quin, Google  

Levana Chen, Google  

Nihav Jain, Google  

Jürgen Sturm, Google

## Overview

This extension builds upon the basic `XR_ANDROID_light_estimation` extension. It adds support for getting cubemap lighting estimates, which provides more detailed estimates about the lighting in the physical environment.

### Note

The mechanism for getting the light estimate data is the same as the basic extension, except that [XrCubemapLightEstimatorCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#XrCubemapLightEstimatorCreateInfoANDROID) has to be chained to the [XrLightEstimatorCreateInfoANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrLightEstimatorCreateInfoANDROID) when creating the light estimator handle.

## Inspect system capability

    typedef struct XrSystemCubemapLightEstimationPropertiesANDROID {
        XrStructureType    type;
        void*              next;
        XrBool32           supportsCubemapLightEstimation;
    } XrSystemCubemapLightEstimationPropertiesANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.
- `supportsCubemapLightEstimation` is an `XrBool32` , indicating if the current system supports cubemap light estimation.

An application **can** inspect whether the system is capable of supporting cubemap light estimation by extending [XrSystemProperties](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSystemProperties) with [XrSystemCubemapLightEstimationPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#XrSystemCubemapLightEstimationPropertiesANDROID) structure when calling [xrGetSystemProperties](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrGetSystemProperties) .

If the runtime returns `XR_FALSE` for `supportsCubemapLightEstimation` and [XrCubemapLightEstimatorCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#XrCubemapLightEstimatorCreateInfoANDROID) has been chained to [XrLightEstimatorCreateInfoANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrLightEstimatorCreateInfoANDROID) , the runtime **must** return `XR_ERROR_FEATURE_UNSUPPORTED` from [xrCreateLightEstimatorANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateLightEstimatorANDROID) .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#VUID-XrSystemCubemapLightEstimationPropertiesANDROID-extension-notenabled) The `XR_ANDROID_light_estimation_cubemap` extension **must** be enabled prior to using [XrSystemCubemapLightEstimationPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#XrSystemCubemapLightEstimationPropertiesANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#VUID-XrSystemCubemapLightEstimationPropertiesANDROID-type-type) `type` **must** be `XR_TYPE_SYSTEM_CUBEMAP_LIGHT_ESTIMATION_PROPERTIES_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#VUID-XrSystemCubemapLightEstimationPropertiesANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)

## Getting supported cubemap resolutions

    XrResult xrEnumerateCubemapLightingResolutionsANDROID(
        XrInstance                                  instance,
        XrSystemId                                  systemId,
        uint32_t                                    resolutionCapacityInput,
        uint32_t*                                   resolutionCountOutput,
        uint32_t*                                   resolutions);

### Parameter Descriptions

- `instance` is an [XrInstance](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrInstance) created previously.
- `systemId` is the `XrSystemId` retrieved previously by [xrGetSystem](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrGetSystem) for which to get the supported cubemap resolutions.
- `resolutionCapacityInput` is a `uint32_t` indicating the maximum number of elements that **can** be stored in the `resolutions` array.
- `resolutionCountOutput` is a pointer to a `uint32_t` which is set by the runtime indicating the number of elements written to the `resolutions` array by the runtime.
- `resolutions` is an array of `uint32_t` which is populated by the runtime with the supported cubemap resolutions.

A cubemap resolution indicates the width and height of each face of the cubemap in pixels. [2-call idiom](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-buffer-size-parameters) The application **can** then choose to use one of the supported resolutions in [XrCubemapLightEstimatorCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#XrCubemapLightEstimatorCreateInfoANDROID) :: `cubemapResolution` when creating the light estimator handle. The application **must** allocate the appropriate amount of memory for the image buffer members of [XrCubemapLightingDataANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#XrCubemapLightingDataANDROID) based on the resolution chosen and the color format.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#VUID-xrEnumerateCubemapLightingResolutionsANDROID-extension-notenabled) The `XR_ANDROID_light_estimation_cubemap` extension **must** be enabled prior to calling [xrEnumerateCubemapLightingResolutionsANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#xrEnumerateCubemapLightingResolutionsANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#VUID-xrEnumerateCubemapLightingResolutionsANDROID-instance-parameter) `instance` **must** be a valid [XrInstance](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrInstance) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#VUID-xrEnumerateCubemapLightingResolutionsANDROID-resolutionCountOutput-parameter) `resolutionCountOutput` **must** be a pointer to a `uint32_t` value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#VUID-xrEnumerateCubemapLightingResolutionsANDROID-resolutions-parameter) If `resolutionCapacityInput` is not `0` , `resolutions` **must** be a pointer to an array of `resolutionCapacityInput` `uint32_t` values

### Return Codes

[Success](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`

[Failure](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_HANDLE_INVALID`
- `XR_ERROR_INSTANCE_LOST`
- `XR_ERROR_RUNTIME_FAILURE`
- `XR_ERROR_SIZE_INSUFFICIENT`
- `XR_ERROR_SYSTEM_INVALID`
- `XR_ERROR_VALIDATION_FAILURE`

## Getting supported cubemap color formats

The [XrCubemapLightingColorFormatANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#XrCubemapLightingColorFormatANDROID) enumeration identifies to the runtime, the color format of cubemap lighting to use.

    typedef enum XrCubemapLightingColorFormatANDROID {
        XR_CUBEMAP_LIGHTING_COLOR_FORMAT_R32G32B32_SFLOAT_ANDROID = 1,
        XR_CUBEMAP_LIGHTING_COLOR_FORMAT_R32G32B32A32_SFLOAT_ANDROID = 2,
        XR_CUBEMAP_LIGHTING_COLOR_FORMAT_R16G16B16A16_SFLOAT_ANDROID = 3,
        XR_CUBEMAP_LIGHTING_COLOR_FORMAT_MAX_ENUM_ANDROID = 0x7FFFFFFF
    } XrCubemapLightingColorFormatANDROID;

The enums have the following meanings:

Enum Description

`XR_CUBEMAP_LIGHTING_COLOR_FORMAT_R32G32B32_SFLOAT_ANDROID`

A color format with 3 channels where each channel is a 32-bit floating point value.

`XR_CUBEMAP_LIGHTING_COLOR_FORMAT_R32G32B32A32_SFLOAT_ANDROID`

A color format with 4 channels where each channel is a 32-bit floating point value.

`XR_CUBEMAP_LIGHTING_COLOR_FORMAT_R16G16B16A16_SFLOAT_ANDROID`

A color format with 4 channels where each channel is a 16-bit floating point value.

    XrResult xrEnumerateCubemapLightingColorFormatsANDROID(
        XrInstance                                  instance,
        XrSystemId                                  systemId,
        uint32_t                                    colorFormatCapacityInput,
        uint32_t*                                   colorFormatCountOutput,
        XrCubemapLightingColorFormatANDROID*        colorFormats);

### Parameter Descriptions

- `instance` is an [XrInstance](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrInstance) created previously.
- `systemId` is the `XrSystemId` retrieved previously by [xrGetSystem](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrGetSystem) for which to get the supported cubemap resolutions.
- `colorFormatCapacityInput` is a `uint32_t` indicating the maximum number of elements that **can** be stored in the `colorFormats` array.
- `colorFormatCountOutput` is a pointer to a `uint32_t` which is set by the runtime indicating the number of elements written to the `colorFormats` array by the runtime.
- `colorFormats` is an array of [XrCubemapLightingColorFormatANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#XrCubemapLightingColorFormatANDROID) which is populated by the runtime with the supported cubemap color formats.

[2-call idiom](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-buffer-size-parameters) The application **can** then choose to use one of the supported color formats in [XrCubemapLightEstimatorCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#XrCubemapLightEstimatorCreateInfoANDROID) :: `colorFormat` when creating the light estimator handle. The application **must** allocate the appropriate amount of memory for the image buffer members of [XrCubemapLightingDataANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#XrCubemapLightingDataANDROID) based on the color format chosen.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#VUID-xrEnumerateCubemapLightingColorFormatsANDROID-extension-notenabled) The `XR_ANDROID_light_estimation_cubemap` extension **must** be enabled prior to calling [xrEnumerateCubemapLightingColorFormatsANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#xrEnumerateCubemapLightingColorFormatsANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#VUID-xrEnumerateCubemapLightingColorFormatsANDROID-instance-parameter) `instance` **must** be a valid [XrInstance](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrInstance) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#VUID-xrEnumerateCubemapLightingColorFormatsANDROID-colorFormatCountOutput-parameter) `colorFormatCountOutput` **must** be a pointer to a `uint32_t` value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#VUID-xrEnumerateCubemapLightingColorFormatsANDROID-colorFormats-parameter) If `colorFormatCapacityInput` is not `0` , `colorFormats` **must** be a pointer to an array of `colorFormatCapacityInput` [XrCubemapLightingColorFormatANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#XrCubemapLightingColorFormatANDROID) values

### Return Codes

[Success](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`

[Failure](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_HANDLE_INVALID`
- `XR_ERROR_INSTANCE_LOST`
- `XR_ERROR_RUNTIME_FAILURE`
- `XR_ERROR_SIZE_INSUFFICIENT`
- `XR_ERROR_SYSTEM_INVALID`
- `XR_ERROR_VALIDATION_FAILURE`

## Create a cubemap light estimator handle

    typedef struct XrCubemapLightEstimatorCreateInfoANDROID {
        XrStructureType                        type;
        const void*                            next;
        uint32_t                               cubemapResolution;
        XrCubemapLightingColorFormatANDROID    colorFormat;
        XrBool32                               reproject;
    } XrCubemapLightEstimatorCreateInfoANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `cubemapResolution` is a `uint32_t` indicating the resolution of the cubemap lighting to use.
- `colorFormat` is an [XrCubemapLightingColorFormatANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#XrCubemapLightingColorFormatANDROID) indicating the color format of the cubemap lighting data to use.
- `reproject` is an `XrBool32` indicating whether the cubemap lighting **should** be reprojected to the application base space.

The [XrCubemapLightEstimatorCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#XrCubemapLightEstimatorCreateInfoANDROID) structure describes the information to create an [XrLightEstimatorANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrLightEstimatorANDROID) handle to be capable of providing cubemap lighting estimates. The [XrCubemapLightEstimatorCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#XrCubemapLightEstimatorCreateInfoANDROID) :: `cubemapResolution` member **must** be set to one of the resolutions returned by [xrEnumerateCubemapLightingResolutionsANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#xrEnumerateCubemapLightingResolutionsANDROID) . The [XrCubemapLightEstimatorCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#XrCubemapLightEstimatorCreateInfoANDROID) :: `colorFormat` member **must** be set to one of the color formats returned by [xrEnumerateCubemapLightingColorFormatsANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#xrEnumerateCubemapLightingColorFormatsANDROID) . If the application does not set to the resolution to one of the supported resolutions or the color format to one of the supported color formats, the runtime **must** return `XR_ERROR_FEATURE_UNSUPPORTED` from [xrCreateLightEstimatorANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateLightEstimatorANDROID) .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#VUID-XrCubemapLightEstimatorCreateInfoANDROID-extension-notenabled) The `XR_ANDROID_light_estimation_cubemap` extension **must** be enabled prior to using [XrCubemapLightEstimatorCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#XrCubemapLightEstimatorCreateInfoANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#VUID-XrCubemapLightEstimatorCreateInfoANDROID-type-type) `type` **must** be `XR_TYPE_CUBEMAP_LIGHT_ESTIMATOR_CREATE_INFO_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#VUID-XrCubemapLightEstimatorCreateInfoANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#VUID-XrCubemapLightEstimatorCreateInfoANDROID-colorFormat-parameter) `colorFormat` **must** be a valid [XrCubemapLightingColorFormatANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#XrCubemapLightingColorFormatANDROID) value

## Cubemap light estimates

    typedef struct XrCubemapLightingDataANDROID {
        XrStructureType                type;
        void*                          next;
        XrLightEstimateStateANDROID    state;
        uint32_t                       imageBufferSize;
        uint8_t*                       imageBufferRight;
        uint8_t*                       imageBufferLeft;
        uint8_t*                       imageBufferTop;
        uint8_t*                       imageBufferBottom;
        uint8_t*                       imageBufferFront;
        uint8_t*                       imageBufferBack;
        XrQuaternionf                  rotation;
        XrTime                         centerExposureTime;
    } XrCubemapLightingDataANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. Valid structures are [XrAmbientLightANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrAmbientLightANDROID) , [XrSphericalHarmonicsANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSphericalHarmonicsANDROID) , [XrDirectionalLightANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrDirectionalLightANDROID) .
- `state` is the [XrLightEstimateStateANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrLightEstimateStateANDROID) representing the state of the light estimate.
- `imageBufferSize` is a `uint32_t` indicating the byte size of each face image buffer in the cubemap.
- `imageBufferRight` is a `uint8_t` buffer containing the right face image of the cubemap.
- `imageBufferLeft` is a `uint8_t` buffer containing the left face image of the cubemap.
- `imageBufferTop` is a `uint8_t` buffer containing the top face image of the cubemap.
- `imageBufferBottom` is a `uint8_t` buffer containing the bottom face image of the cubemap.
- `imageBufferFront` is a `uint8_t` buffer containing the front face image of the cubemap.
- `imageBufferBack` is a `uint8_t` buffer containing the back face image of the cubemap.
- `rotation` is an [XrQuaternionf](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrQuaternionf) indicating the rotation of the cubemap.
- `centerExposureTime` is an `XrTime` indicating the time the cubemap was captured.

This structure **can** be chained to the [XrLightEstimateANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrLightEstimateANDROID) . The runtime **must** only populate this structure in [xrGetLightEstimateANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrGetLightEstimateANDROID) if the [XrCubemapLightEstimatorCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#XrCubemapLightEstimatorCreateInfoANDROID) was used to create the light estimator handle. The application **must** allocate the appropriate amount of memory for the image buffers which is dependent on the values set in [XrCubemapLightEstimatorCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#XrCubemapLightEstimatorCreateInfoANDROID) :: `cubemapResolution` and [XrCubemapLightEstimatorCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#XrCubemapLightEstimatorCreateInfoANDROID) :: `colorFormat` when creating the light estimator handle. The application **must** set [XrCubemapLightingDataANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#XrCubemapLightingDataANDROID) :: `imageBufferSize` to the capacity of each face image buffer in bytes. If the application is not using cubemap light estimation or if [XrCubemapLightingDataANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#XrCubemapLightingDataANDROID) :: `imageBufferSize` is not large enough for the runtime to populate the image buffers, the runtime **must** set [XrCubemapLightingDataANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#XrCubemapLightingDataANDROID) :: `state` to `XR_LIGHT_ESTIMATE_STATE_INVALID_ANDROID` .

If the application set [XrCubemapLightEstimatorCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#XrCubemapLightEstimatorCreateInfoANDROID) :: `reproject` to `XR_TRUE` when creating the light estimator handle, the runtime **must** set [XrCubemapLightingDataANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#XrCubemapLightingDataANDROID) :: `rotation` to the identity rotation and ensure the internal rotated cubemap is reprojected onto the faces of an identity cubemap in the application base space.

The layout of the lighting cubemap is same as OpenGL cubemap layout, as shown in the [following image](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#fig-ANDROID_light_estimation-cubemap-layout)

![XR ANDROID light estimation cubemap layout](data:image/png;base64,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)

### Figure 24. Cubemap layout.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#VUID-XrCubemapLightingDataANDROID-extension-notenabled) The `XR_ANDROID_light_estimation_cubemap` extension **must** be enabled prior to using [XrCubemapLightingDataANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#XrCubemapLightingDataANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#VUID-XrCubemapLightingDataANDROID-type-type) `type` **must** be `XR_TYPE_CUBEMAP_LIGHTING_DATA_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#VUID-XrCubemapLightingDataANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#VUID-XrCubemapLightingDataANDROID-state-parameter) `state` **must** be a valid [XrLightEstimateStateANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrLightEstimateStateANDROID) value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#VUID-XrCubemapLightingDataANDROID-imageBufferRight-parameter) `imageBufferRight` **must** be a pointer to an array of `imageBufferSize` `uint8_t` values
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#VUID-XrCubemapLightingDataANDROID-imageBufferLeft-parameter) `imageBufferLeft` **must** be a pointer to an array of `imageBufferSize` `uint8_t` values
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#VUID-XrCubemapLightingDataANDROID-imageBufferTop-parameter) `imageBufferTop` **must** be a pointer to an array of `imageBufferSize` `uint8_t` values
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#VUID-XrCubemapLightingDataANDROID-imageBufferBottom-parameter) `imageBufferBottom` **must** be a pointer to an array of `imageBufferSize` `uint8_t` values
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#VUID-XrCubemapLightingDataANDROID-imageBufferFront-parameter) `imageBufferFront` **must** be a pointer to an array of `imageBufferSize` `uint8_t` values
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#VUID-XrCubemapLightingDataANDROID-imageBufferBack-parameter) `imageBufferBack` **must** be a pointer to an array of `imageBufferSize` `uint8_t` values
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#VUID-XrCubemapLightingDataANDROID-imageBufferSize-arraylength) The `imageBufferSize` parameter **must** be greater than `0`

## Example code for light estimation

The following example code demonstrates how to get all possible light estimation quantities from the runtime

    XrSession session;  // Created at app startup
    XrInstance instance; // Created at app startup
    XrSpace appSpace;   // Created previously.
    XrSystemId systemId; // Retrieved previously by xrGetSystem
    PFN_xrCreateLightEstimatorANDROID xrCreateLightEstimatorANDROID; // Created previously.
    PFN_xrDestroyLightEstimatorANDROID xrDestroyLightEstimatorANDROID; // Created previously.
    PFN_xrGetLightEstimateANDROID xrGetLightEstimateANDROID; // Created previously.
    PFN_xrEnumerateCubemapLightingResolutionsANDROID xrEnumerateCubemapLightingResolutionsANDROID; // Created previously.
    PFN_xrEnumerateCubemapLightingColorFormatsANDROID xrEnumerateCubemapLightingColorFormatsANDROID; // Created previously.

    XrSystemCubemapLightEstimationPropertiesANDROID props = {
      .type = XR_TYPE_SYSTEM_CUBEMAP_LIGHT_ESTIMATION_PROPERTIES_ANDROID};
    XrSystemProperties base = {.type = XR_TYPE_SYSTEM_PROPERTIES,
                               .next = &props};
    CHK_XR(xrGetSystemProperties(instance, systemId, &base));
    if (!props.supportsCubemapLightEstimation) {
       // Cubemap light estimation is not supported
    }

    uint32_t cubemapResolution = 0;
    std::vector<uint32_t> supportedCubemapResolutions;
    uint32_t resolutionCount;
    CHK_XR(xrEnumerateCubemapLightingResolutionsANDROID(
      instance, systemId, 0, &resolutionCount, nullptr));
    supportedCubemapResolutions.resize(resolutionCount);
    if (resolutionCount == 0) {
      // No cubemap lighting supported
    } else {
      CHK_XR(xrEnumerateCubemapLightingResolutionsANDROID(
        instance, systemId, 0, &resolutionCount, supportedCubemapResolutions.data()));
      cubemapResolution = supportedCubemapResolutions[0];
    }

    uint32_t pixelCount = cubemapResolution * cubemapResolution;

    XrCubemapLightingColorFormatANDROID colorFormat;
    std::vector<XrCubemapLightingColorFormatANDROID> supportedColorFormats;
    uint32_t colorFormatCount;
    CHK_XR(xrEnumerateCubemapLightingColorFormatsANDROID(
      instance, systemId, 0, &colorFormatCount, nullptr));
    supportedColorFormats.resize(colorFormatCount);
    if (colorFormatCount == 0) {
      // No supported color formats for cubemap lighting. Cannot use cubemap
      // light estimation.
    } else {
      CHK_XR(xrEnumerateCubemapLightingColorFormatsANDROID(
        instance, systemId, 0, &colorFormatCount, supportedColorFormats.data()));
      colorFormat = supportedColorFormats[0];
    }

    uint32_t pixelSize = 0;
    switch (colorFormat) {
      case XR_CUBEMAP_LIGHTING_COLOR_FORMAT_R32G32B32_SFLOAT_ANDROID:
        pixelSize = 3 * sizeof(float);
        break;
      case XR_CUBEMAP_LIGHTING_COLOR_FORMAT_R32G32B32A32_SFLOAT_ANDROID:
        pixelSize = 4 * sizeof(float);
        break;
      case XR_CUBEMAP_LIGHTING_COLOR_FORMAT_R16G16B16A16_SFLOAT_ANDROID:
        pixelSize = 4 * sizeof(uint16_t);
        break;
      default:
        // Should not happen since the color format was validated previously.
        break;
    }

    uint32_t perFaceImageBufferSize = pixelCount * pixelSize;

    XrLightEstimatorANDROID estimator;
    XrCubemapLightEstimatorCreateInfoANDROID cubemapCreateInfo = {
        .type = XR_TYPE_CUBEMAP_LIGHT_ESTIMATOR_CREATE_INFO_ANDROID,
        .cubemapResolution = cubemapResolution,
        .colorFormat = colorFormat,
        .reproject = XR_TRUE
    };
    XrLightEstimatorCreateInfoANDROID basicCreateInfo = {
        .type = XR_TYPE_LIGHT_ESTIMATOR_CREATE_INFO_ANDROID,
        .next = &cubemapCreateInfo};
    CHK_XR(xrCreateLightEstimatorANDROID(session, &basicCreateInfo, &estimator));

    std::vector<uint8_t> cubemapBuffer(perFaceImageBufferSize * 6); // 6 faces * perFaceImageBufferSize

    // Every frame
    XrTime updateTime;  // Time used for the current frame's simulation update.

    XrLightEstimateGetInfoANDROID info = {
        .type = XR_TYPE_LIGHT_ESTIMATE_GET_INFO_ANDROID,
        .space = appSpace,
        .time = updateTime,
    };

    XrCubemapLightingDataANDROID cubemap = {
        .type = XR_TYPE_CUBEMAP_LIGHTING_DATA_ANDROID,
        .next = nullptr,
        .imageBufferSize = perFaceImageBufferSize,
        .imageBufferRight = cubemapBuffer.data() + 0 * perFaceImageBufferSize,
        .imageBufferLeft = cubemapBuffer.data() + 1 * perFaceImageBufferSize,
        .imageBufferTop = cubemapBuffer.data() + 2 * perFaceImageBufferSize,
        .imageBufferBottom = cubemapBuffer.data() + 3 * perFaceImageBufferSize,
        .imageBufferFront = cubemapBuffer.data() + 4 * perFaceImageBufferSize,
        .imageBufferBack = cubemapBuffer.data() + 5 * perFaceImageBufferSize,
    };

    XrDirectionalLightANDROID directionalLight = {
        .type = XR_TYPE_DIRECTIONAL_LIGHT_ANDROID,
        .next = &cubemap,
    };

    XrSphericalHarmonicsANDROID totalSh = {
        .type = XR_TYPE_SPHERICAL_HARMONICS_ANDROID,
        .next = &directionalLight,
        .kind = XR_SPHERICAL_HARMONICS_KIND_TOTAL_ANDROID,
    };

    XrSphericalHarmonicsANDROID ambientSh = {
        .type = XR_TYPE_SPHERICAL_HARMONICS_ANDROID,
        .next = &totalSh,
        .kind = XR_SPHERICAL_HARMONICS_KIND_AMBIENT_ANDROID,
    };

    XrAmbientLightANDROID ambientLight = {
        .type = XR_TYPE_AMBIENT_LIGHT_ANDROID,
        .next = &ambientSh,
    };

    XrLightEstimateANDROID estimate = {
        .type = XR_TYPE_LIGHT_ESTIMATE_ANDROID,
        .next = &ambientLight,
    };

    XrResult result = xrGetLightEstimateANDROID(estimator, &info, &estimate);
    if (result == XR_SUCCESS &&
        estimate.state == XR_LIGHT_ESTIMATE_STATE_VALID_ANDROID) {
      // use cubemap, directionalLight, totalSh, ambientSh, and
      // ambientLight if each struct has a valid state field

      if (cubemap.state == XR_LIGHT_ESTIMATE_STATE_VALID_ANDROID) {
        // use cubemap
        if (cubemapCreateInfo.reproject == XR_TRUE) {
          XrQuaternionf identityQuaternion = {0.0f, 0.0f, 0.0f, 1.0f};
          assert(memcmp(&cubemap.rotation, &identityQuaternion, sizeof(XrQuaternionf)) == 0);
        }
      }
    }

    // When you want to disable light estimation
    CHK_XR(xrDestroyLightEstimatorANDROID(estimator));

## New Commands

- [xrEnumerateCubemapLightingColorFormatsANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#xrEnumerateCubemapLightingColorFormatsANDROID)
- [xrEnumerateCubemapLightingResolutionsANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#xrEnumerateCubemapLightingResolutionsANDROID)

## New Structures

- Extending [XrLightEstimateANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrLightEstimateANDROID) :

  - [XrCubemapLightingDataANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#XrCubemapLightingDataANDROID)
- Extending [XrLightEstimatorCreateInfoANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrLightEstimatorCreateInfoANDROID) :

  - [XrCubemapLightEstimatorCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#XrCubemapLightEstimatorCreateInfoANDROID)
- Extending [XrSystemProperties](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSystemProperties) :

  - [XrSystemCubemapLightEstimationPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#XrSystemCubemapLightEstimationPropertiesANDROID)

## New Enums

- [XrCubemapLightingColorFormatANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap#XrCubemapLightingColorFormatANDROID)

## New Enum Constants

- `XR_ANDROID_LIGHT_ESTIMATION_CUBEMAP_EXTENSION_NAME`
- `XR_ANDROID_light_estimation_cubemap_SPEC_VERSION`
- Extending [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) :

  - `XR_TYPE_CUBEMAP_LIGHTING_DATA_ANDROID`
  - `XR_TYPE_CUBEMAP_LIGHT_ESTIMATOR_CREATE_INFO_ANDROID`
  - `XR_TYPE_SYSTEM_CUBEMAP_LIGHT_ESTIMATION_PROPERTIES_ANDROID`

**Issues**

**Version History**

- Revision 1, 2025-12-05 (Salar Khan)

  - Initial extension description