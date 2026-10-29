---
title: https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_viewport_feathering
url: https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_viewport_feathering
source: md.txt
---

### XR_ANDROID_viewport_feathering

**Name String**

`XR_ANDROID_viewport_feathering`

**Extension Type**

Instance extension

**Registered Extension Number**

807

**Revision**

1

**Ratification Status**

Not ratified

**Extension and Version Dependencies**

[OpenXR 1.0](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#versions-1.0)

**Last Modified Date**

2026-05-06

**IP Status**

No known IP claims.

**Contributors**

Brian Chen, Google  

Kyle Chen, Google  

Nihav Jain, Google  

Spencer Quin, Google

## Overview

While devices with large FOV **can** display the full content of an application without any issues, devices with small FOV(50 to 70) are only capable of showing part of the content and the rest of will be cut off at the edges of the display. A hard clip around the perimeter **may** seem restrictive and distracting to the user and eventually cause discomfort. Feathering is a technique to apply fading at the perimeter edge of the field of view. This extension exposes feathered area applied by the runtime, an application **can** then layout the UI elements within the safe area that is not affected by the feathering.

## Get Feathered Area

The [XrViewportFeatheringConfigViewANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_viewport_feathering#XrViewportFeatheringConfigViewANDROID) structure is defined as:

    typedef struct XrViewportFeatheringConfigViewANDROID {
        XrStructureType    type;
        void*              next;
        uint32_t           insetLeft;
        uint32_t           insetRight;
        uint32_t           insetTop;
        uint32_t           insetBottom;
    } XrViewportFeatheringConfigViewANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `insetLeft` is the number of pixels on the left side of the view that is affected by feathering.
- `insetRight` is the number of pixels on the right side of the view that is affected by feathering.
- `insetTop` is the number of pixels on the top side of the view that is affected by feathering.
- `insetBottom` is the number of pixels on the bottom side of the view that is affected by feathering.

When this extension is enabled, an application **can** pass in an [XrViewportFeatheringConfigViewANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_viewport_feathering#XrViewportFeatheringConfigViewANDROID) structure in the [XrViewConfigurationView](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrViewConfigurationView) :: `next` chain when calling [xrEnumerateViewConfigurationViews](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrEnumerateViewConfigurationViews) to acquire information about the feathered insets for each side of the view.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_viewport_feathering#VUID-XrViewportFeatheringConfigViewANDROID-extension-notenabled) The `XR_ANDROID_viewport_feathering` extension **must** be enabled prior to using [XrViewportFeatheringConfigViewANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_viewport_feathering#XrViewportFeatheringConfigViewANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_viewport_feathering#VUID-XrViewportFeatheringConfigViewANDROID-type-type) `type` **must** be `XR_TYPE_VIEWPORT_FEATHERING_CONFIG_VIEW_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_viewport_feathering#VUID-XrViewportFeatheringConfigViewANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)

## New Structures

- Extending [XrViewConfigurationView](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrViewConfigurationView) :

  - [XrViewportFeatheringConfigViewANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_viewport_feathering#XrViewportFeatheringConfigViewANDROID)

## New Enum Constants

- `XR_ANDROID_VIEWPORT_FEATHERING_EXTENSION_NAME`
- `XR_ANDROID_viewport_feathering_SPEC_VERSION`
- Extending [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) :

  - `XR_TYPE_VIEWPORT_FEATHERING_CONFIG_VIEW_ANDROID`

## Issues

## Version History

- Revision 1, 2026-05-06 (Brian Chen)

  - Initial extension description.