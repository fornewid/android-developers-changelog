---
title: https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_frame_synthesis
url: https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_frame_synthesis
source: md.txt
---

### XR_EXT_frame_synthesis

**Name String**

`XR_EXT_frame_synthesis`

**Extension Type**

Instance extension

**Registered Extension Number**

212

**Revision**

1

**Ratification Status**

Not ratified

**Extension and Version Dependencies**

[OpenXR 1.0](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#versions-1.0)

**Contributors**

Jian Zhang, Meta Platforms  

Neel Bedekar, Meta Platforms  

Xiang Wei, Meta Platforms  

Guodong Rong, Meta Platforms  

Trevor Dasch, Meta Platforms  

Rémi Arnaud, Varjo  

Paulo Gomes, Samsung Electronics  

Bryce Hutchings, Microsoft  

Rylie Pavlik, Collabora  

Shuai Liu, ByteDance

## Overview

This extension provides support to enable frame synthesis on applications based on additional application provided data. Application generated motion vector images and depth images **may** be used by the runtime to do high quality frame extrapolation and reprojection to synthesize a new frame, providing a smooth experience even when the application is running below the FPS target.

This extension is designed to be independent of `XR_KHR_composition_layer_depth` , and both **may** be enabled and used at the same time, for different purposes. The [XrFrameSynthesisInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_frame_synthesis#XrFrameSynthesisInfoEXT) :: `depthSubImage` **may** use depth data dedicated for frame synthesis, and its resolution **may** be lower than [XrCompositionLayerDepthInfoKHR](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrCompositionLayerDepthInfoKHR) :: `subImage` . See [XrFrameSynthesisConfigViewEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_frame_synthesis#XrFrameSynthesisConfigViewEXT) for the suggested resolution of `depthSubImage` .

## Submit motion vector images and depth images

The [XrFrameSynthesisInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_frame_synthesis#XrFrameSynthesisInfoEXT) structure is defined as:

    typedef struct XrFrameSynthesisInfoEXT {
        XrStructureType                 type;
        const void*                     next;
        XrFrameSynthesisInfoFlagsEXT    layerFlags;
        XrSwapchainSubImage             motionVectorSubImage;
        XrVector4f                      motionVectorScale;
        XrVector4f                      motionVectorOffset;
        XrPosef                         appSpaceDeltaPose;
        XrSwapchainSubImage             depthSubImage;
        float                           minDepth;
        float                           maxDepth;
        float                           nearZ;
        float                           farZ;
    } XrFrameSynthesisInfoEXT;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `layerFlags` is a bitmask of [XrFrameSynthesisInfoFlagsEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_frame_synthesis#XrFrameSynthesisInfoFlagsEXT) .
- `motionVectorSubImage` identifies the motion vector image [XrSwapchainSubImage](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSwapchainSubImage) to be used for frame synthesis.
- `motionVectorScale` is an [XrVector4f](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrVector4f) which scales the interpretation of the motion vector in `motionVectorSubImage` .
- `motionVectorOffset` is an [XrVector4f](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrVector4f) which offsets the interpretation of the motion vector in `motionVectorSubImage` .
- `appSpaceDeltaPose` is the incremental application-applied transform, if any, that affects the view since the previous frame. Experiences of artificial locomotion (scripted movement, teleportation, etc.) involve the application transforming the whole [XrCompositionLayerProjection](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrCompositionLayerProjection) :: `space` from one application space pose to another pose between frames, affecting the view by more than the tracked movement between frames. The `appSpaceDeltaPose` **must** be identity when there is no [XrCompositionLayerProjection](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrCompositionLayerProjection) :: `space` transformation in the application. The [XrPosef](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrPosef) :: `position` in `appSpaceDeltaPose` **must** be relative to the current application [XrCompositionLayerProjection](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrCompositionLayerProjection) :: `space` .
- `depthSubImage` identifies the depth image [XrSwapchainSubImage](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSwapchainSubImage) to be used for frame synthesis.
- `minDepth` and `maxDepth` are the range of depth values in the `depthSubImage` , and **must** be in the range of \[0.0,1.0\] . This is akin to min and max values of OpenGL's `glDepthRange` , but with the requirement here that maxDepth ≥ minDepth .
- `nearZ` is the positive distance in meters of the `minDepth` value in the depth swapchain. Applications **may** use a `nearZ` that is greater than `farZ` to indicate depth values are reversed. `nearZ` **may** be infinite.
- `farZ` is the positive distance in meters of the `maxDepth` value in the depth swapchain. `farZ` **may** be infinite. The runtime **must** return error `XR_ERROR_VALIDATION_FAILURE` if `nearZ` == `farZ`

When submitting motion vector images and depth images along with projection layers, add an [XrFrameSynthesisInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_frame_synthesis#XrFrameSynthesisInfoEXT) structure to the [XrCompositionLayerProjectionView](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrCompositionLayerProjectionView) :: `next` chain, for each [XrCompositionLayerProjectionView](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrCompositionLayerProjectionView) structure in the given layer.

The runtime **must** interpret the motion vector data in the `motionVectorSubImage` 's RGB channels, modified by `motionVectorScale` and `motionVectorOffset` as follows: motionVector = motionVectorSubImage rgb \* motionVectorScale xyz + motionVectorOffset xyz . The components motionVectorSubImage a , motionVectorScale w and motionVectorOffset w are ignored.

The motion vector represents the movement of a pixel since the [XrFrameEndInfo](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrFrameEndInfo) ::displayTime of the previous frame until the [XrFrameEndInfo](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrFrameEndInfo) ::displayTime of the current frame. The runtime **may** use this information to extrapolate the rendered frame into a future frame.

The motion vector **must** derived from normalized device coordinate (NDC) space, which in this context uses Vulkan-style conventions: the NDC range is defined as \[-1, -1, 0\] to \[1, 1, 1\], different from OpenGL's NDC range. However, the motion vector itself is not constrained to this range; its values depend on the pixel's movement and may extend beyond the boundaries of the NDC space. For example, given that a pixel's NDC in the previous frame is PrevNDC, and CurrNDC in current frame, and that there is no scale or offset, then the motion vector value is " (CurrNDC - PrevNDC) xyz ".

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_frame_synthesis#VUID-XrFrameSynthesisInfoEXT-extension-notenabled) The `XR_EXT_frame_synthesis` extension **must** be enabled prior to using [XrFrameSynthesisInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_frame_synthesis#XrFrameSynthesisInfoEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_frame_synthesis#VUID-XrFrameSynthesisInfoEXT-type-type) `type` **must** be `XR_TYPE_FRAME_SYNTHESIS_INFO_EXT`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_frame_synthesis#VUID-XrFrameSynthesisInfoEXT-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_frame_synthesis#VUID-XrFrameSynthesisInfoEXT-layerFlags-parameter) `layerFlags` **must** be `0` or a valid combination of [XrFrameSynthesisInfoFlagBitsEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_frame_synthesis#XrFrameSynthesisInfoFlagBitsEXT) values
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_frame_synthesis#VUID-XrFrameSynthesisInfoEXT-motionVectorSubImage-parameter) `motionVectorSubImage` **must** be a valid [XrSwapchainSubImage](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSwapchainSubImage) structure
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_frame_synthesis#VUID-XrFrameSynthesisInfoEXT-depthSubImage-parameter) `depthSubImage` **must** be a valid [XrSwapchainSubImage](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSwapchainSubImage) structure

### Note

There are many different ways to generate `motionVectorSubImage` and `depthSubImage` . For example, the application may render them in a lower resolution dedicated motion vector pass (see [XrFrameSynthesisConfigViewEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_frame_synthesis#XrFrameSynthesisConfigViewEXT) for recommended resolution), or render them in the main view pass with MRT (Multiple Render Targets). It is up to the application to decide the specific approach. Signed 16 bit float per pixel channel formats are recommended for `motionVectorSubImage` .

## Frame synthesis flags

    typedef XrFlags64 XrFrameSynthesisInfoFlagsEXT;

    // Flag bits for XrFrameSynthesisInfoFlagsEXT
    static const XrFrameSynthesisInfoFlagsEXT XR_FRAME_SYNTHESIS_INFO_USE_2D_MOTION_VECTOR_BIT_EXT = 0x00000001;
    static const XrFrameSynthesisInfoFlagsEXT XR_FRAME_SYNTHESIS_INFO_REQUEST_RELAXED_FRAME_INTERVAL_BIT_EXT = 0x00000002;

### Flag Descriptions

- `XR_FRAME_SYNTHESIS_INFO_USE_2D_MOTION_VECTOR_BIT_EXT` indicates 2D motion vector data is used.
- `XR_FRAME_SYNTHESIS_INFO_REQUEST_RELAXED_FRAME_INTERVAL_BIT_EXT` provides a hint to the runtime that the application prefers additional time to render each frame, with the trade-off that more frames would be synthesized by the runtime. This may be useful for applications that prefer to conserve CPU and GPU utilization (e.g. for increased battery life) or to increase the compute budget of each frame. The runtime **may** request frames at any interval, regardless of the value of this flag.

By default, 3D motion vector data is expected by the runtime, so motionVectorSubImage rgb , motionVectorScale xyz and motionVectorOffset xyz are used, as described in [XrFrameSynthesisInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_frame_synthesis#XrFrameSynthesisInfoEXT) .

When `XR_FRAME_SYNTHESIS_INFO_USE_2D_MOTION_VECTOR_BIT_EXT` is enabled on [XrFrameSynthesisInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_frame_synthesis#XrFrameSynthesisInfoEXT) `layerFlags` , the runtime instead interprets the submitted motion vector image as 2D motion vector data, representing 2D pixel movement from the previous frame to the current frame. Pixels values are interpreted as follows for 2D motion vector data: motionVector = motionVectorSubImage rg \* motionVectorScale xy + motionVectorOffset xy . The components motionVectorSubImage ba , motionVectorScale zw and motionVectorOffset zw are ignored. Using 2D instead of 3D motion vector data **may** decrease the quality of the synthesized frames.

## Get recommended resolution

The [XrFrameSynthesisConfigViewEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_frame_synthesis#XrFrameSynthesisConfigViewEXT) structure is defined as:

    typedef struct XrFrameSynthesisConfigViewEXT {
        XrStructureType    type;
        void*              next;
        uint32_t           recommendedMotionVectorImageRectWidth;
        uint32_t           recommendedMotionVectorImageRectHeight;
    } XrFrameSynthesisConfigViewEXT;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `recommendedMotionVectorImageRectWidth` : recommended motion vector and depth image width.
- `recommendedMotionVectorImageRectHeight` : recommended motion vector and depth image height.

When this extension is enabled, an application **can** pass in an [XrFrameSynthesisConfigViewEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_frame_synthesis#XrFrameSynthesisConfigViewEXT) structure in the [XrViewConfigurationView](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrViewConfigurationView) :: `next` chain when calling [xrEnumerateViewConfigurationViews](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrEnumerateViewConfigurationViews) to acquire information about the recommended motion vector image resolution.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_frame_synthesis#VUID-XrFrameSynthesisConfigViewEXT-extension-notenabled) The `XR_EXT_frame_synthesis` extension **must** be enabled prior to using [XrFrameSynthesisConfigViewEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_frame_synthesis#XrFrameSynthesisConfigViewEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_frame_synthesis#VUID-XrFrameSynthesisConfigViewEXT-type-type) `type` **must** be `XR_TYPE_FRAME_SYNTHESIS_CONFIG_VIEW_EXT`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_frame_synthesis#VUID-XrFrameSynthesisConfigViewEXT-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)

## New Structures

- Extending [XrCompositionLayerProjectionView](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrCompositionLayerProjectionView) :

  - [XrFrameSynthesisInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_frame_synthesis#XrFrameSynthesisInfoEXT)
- Extending [XrViewConfigurationView](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrViewConfigurationView) :

  - [XrFrameSynthesisConfigViewEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_frame_synthesis#XrFrameSynthesisConfigViewEXT)

## New Enum Constants

- `XR_EXT_FRAME_SYNTHESIS_EXTENSION_NAME`
- `XR_EXT_frame_synthesis_SPEC_VERSION`
- Extending [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) :

  - `XR_TYPE_FRAME_SYNTHESIS_CONFIG_VIEW_EXT`
  - `XR_TYPE_FRAME_SYNTHESIS_INFO_EXT`

**Issues**

**Version History**

- Revision 1, 2022-01-31 (Jian Zhang)

  - Initial extension description, converted from fb_space_warp
  - Collaborating with contributors to refine the extension interfaces.