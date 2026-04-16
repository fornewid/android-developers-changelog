---
title: https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_recommended_resolution
url: https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_recommended_resolution
source: md.txt
---

### XR_ANDROID_recommended_resolution

**Name String**

`XR_ANDROID_recommended_resolution`

**Extension Type**

Instance extension

**Registered Extension Number**

462

**Revision**

1

**Ratification Status**

Not ratified

**Extension and Version Dependencies**

[OpenXR 1.0](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#versions-1.0)

**Last Modified Date**

**IP Status**

**Contributors**

Trevor Debrechtabel, Google  

Spencer Quin, Google  

Lachlan Ford, Google  

Vasiliy Baranov, Google

## Overview

This extension allows the runtime to notify the application when the recommended resolution changes, based on current system performance, device thermals, or other factors.

This extension modifies the specification in the following way:

- The runtime **may** return non-identical buffer contents from the [xrEnumerateViewConfigurationViews](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrEnumerateViewConfigurationViews) enumeration for the given `systemId` and `viewConfigurationType` for the lifetime of the instance.

The [XrEventDataRecommendedResolutionChangedANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_recommended_resolution#XrEventDataRecommendedResolutionChangedANDROID) structure is defined as:

    typedef struct XrEventDataRecommendedResolutionChangedANDROID {
        XrStructureType    type;
        const void*        next;
    } XrEventDataRecommendedResolutionChangedANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.

Receiving the [XrEventDataRecommendedResolutionChangedANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_recommended_resolution#XrEventDataRecommendedResolutionChangedANDROID) event structure indicates that the recommended resolution has changed. The application **should** query the runtime for the new recommended resolution using [xrEnumerateViewConfigurationViews](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrEnumerateViewConfigurationViews) .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_recommended_resolution#VUID-XrEventDataRecommendedResolutionChangedANDROID-extension-notenabled) The `XR_ANDROID_recommended_resolution` extension **must** be enabled prior to using [XrEventDataRecommendedResolutionChangedANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_recommended_resolution#XrEventDataRecommendedResolutionChangedANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_recommended_resolution#VUID-XrEventDataRecommendedResolutionChangedANDROID-type-type) `type` **must** be `XR_TYPE_EVENT_DATA_RECOMMENDED_RESOLUTION_CHANGED_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_recommended_resolution#VUID-XrEventDataRecommendedResolutionChangedANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)

## Example code

The following example code demonstrates how to listen for recommended resolution change events.

    // Created at app startup time.
    XrInstance instance;
    XrSystemId systemId; // Previously initialized.
    uint32_t viewCountOutput; // Previously initialized.

    // View configuration type the application uses.
    XrViewConfigurationType viewConfigType;

    // Poll events for recommended resolution changes.
    XrEventDataBuffer event = {XR_TYPE_EVENT_DATA_BUFFER};
    XrResult result = xrPollEvent(instance, &event);
    if (result == XR_SUCCESS) {
      switch (event.type) {
        case XR_TYPE_EVENT_DATA_RECOMMENDED_RESOLUTION_CHANGED_ANDROID: {
            uint32_t viewCapacityInput = viewCountOutput;
            std::vector<XrViewConfigurationView> views(viewCapacityInput);
            result = xrEnumerateViewConfigurationViews(instance, systemId,
              viewConfigType, viewCapacityInput, &viewCountOutput, views.data());
            if(!XR_SUCCEEDED(result)) {
              // Handle error
            }

            // New recommended resolution is found in
            // views.recommendedImageRectWidth and views.recommendedImageRectHeight
            // Change the resolution for the viewConfigType
          break;
        }
        default:
          break;
      }
    }

## Version History

- Revision 1, 2025-04-04 (Kenny Vercaemer)

  - Initial extension description