---
title: https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_global_passthrough_dimming
url: https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_global_passthrough_dimming
source: md.txt
---

### XR_ANDROID_global_passthrough_dimming

**Name String**

`XR_ANDROID_global_passthrough_dimming`

**Extension Type**

Instance extension

**Registered Extension Number**

797

**Revision**

1

**Ratification Status**

Not ratified

**Extension and Version Dependencies**

[OpenXR 1.0](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#versions-1.0)

**Last Modified Date**

2026-03-10

**IP Status**

No known IP claims.

**Contributors**

Brian Chen, Google  

Kyle Chen, Google  

Nihav Jain, Google  

Spencer Quin, Google

## Overview

As optical see-through devices are introduced, it's important to not only allow applications to adjust the darkness of the passthrough in order to provide the best blending with the app context to the user, but also let system undim the passthrough for safety reasons.

This extension provides two functions for apps to set and get the current dimming level, as well as an event to broadcast when the dimming level changes.

## Inspect system capability

The [XrSystemGlobalDimmingPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_global_passthrough_dimming#XrSystemGlobalDimmingPropertiesANDROID) structure is defined as:

    typedef struct XrSystemGlobalDimmingPropertiesANDROID {
        XrStructureType    type;
        void*              next;
        XrBool32           supportsGlobalDimming;
    } XrSystemGlobalDimmingPropertiesANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension. No such structures are defined in core OpenXR or this extension.
- `supportsGlobalDimming` is an `XrBool32` , indicating if the current system supports global dimming.

An application **can** inspect whether the system supports global dimming by chaining an [XrSystemGlobalDimmingPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_global_passthrough_dimming#XrSystemGlobalDimmingPropertiesANDROID) structure to the [XrSystemProperties](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSystemProperties) when calling [xrGetSystemProperties](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrGetSystemProperties) .

If the runtime returns `XR_FALSE` for `supportsGlobalDimming` , the runtime **must** return `XR_ERROR_FEATURE_UNSUPPORTED` when [xrGetGlobalDimmingLevelANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_global_passthrough_dimming#xrGetGlobalDimmingLevelANDROID) is called.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_global_passthrough_dimming#VUID-XrSystemGlobalDimmingPropertiesANDROID-extension-notenabled) The `XR_ANDROID_global_passthrough_dimming` extension **must** be enabled prior to using [XrSystemGlobalDimmingPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_global_passthrough_dimming#XrSystemGlobalDimmingPropertiesANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_global_passthrough_dimming#VUID-XrSystemGlobalDimmingPropertiesANDROID-type-type) `type` **must** be `XR_TYPE_SYSTEM_GLOBAL_DIMMING_PROPERTIES_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_global_passthrough_dimming#VUID-XrSystemGlobalDimmingPropertiesANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)

## Enumerate supported global dimming levels

The [xrEnumerateSupportedGlobalDimmingLevelsANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_global_passthrough_dimming#xrEnumerateSupportedGlobalDimmingLevelsANDROID) structure is defined as:

    XrResult xrEnumerateSupportedGlobalDimmingLevelsANDROID(
        XrInstance                                  instance,
        XrSystemId                                  systemId,
        uint32_t                                    supportedGlobalDimmingLevelCapacityInput,
        uint32_t*                                   supportedGlobalDimmingLevelCountOutput,
        float*                                      supportedGlobalDimmingLevels);

### Member Descriptions

- `instance` is the instance from which `systemId` was retrieved.
- `systemId` is the `XrSystemId` whose supported levels will be enumerated.
- `supportedGlobalDimmingLevelCapacityInput` is the capacity of the `supportedGlobalDimmingLevels` array, or 0 to indicate a request to retrieve the required capacity.
- `supportedGlobalDimmingLevelCountOutput` is a pointer to the count of `supportedGlobalDimmingLevels` written, or a pointer to the required capacity in the case that `supportedGlobalDimmingLevelCapacityInput` is insufficient.
- `supportedGlobalDimmingLevels` is a pointer to an array of supported levels, but **can** be NULL if `supportedGlobalDimmingLevelCapacityInput` is 0.

If returned `supportedGlobalDimmingLevelCountOutput` is 0, all global dimming levels between 0.0 and 1.0 are supported.

[xrEnumerateSupportedGlobalDimmingLevelsANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_global_passthrough_dimming#xrEnumerateSupportedGlobalDimmingLevelsANDROID) enumerates the global dimming levels supported by the `XrSystemId` . The supported levels **must** not change during the lifetime of its [XrInstance](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrInstance) . The returned list of levels **must** be sorted in ascending order.

Runtimes **must** always return identical buffer contents from this enumeration for the given `systemId` and for the lifetime of the `instance` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_global_passthrough_dimming#VUID-xrEnumerateSupportedGlobalDimmingLevelsANDROID-extension-notenabled) The `XR_ANDROID_global_passthrough_dimming` extension **must** be enabled prior to calling [xrEnumerateSupportedGlobalDimmingLevelsANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_global_passthrough_dimming#xrEnumerateSupportedGlobalDimmingLevelsANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_global_passthrough_dimming#VUID-xrEnumerateSupportedGlobalDimmingLevelsANDROID-instance-parameter) `instance` **must** be a valid [XrInstance](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrInstance) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_global_passthrough_dimming#VUID-xrEnumerateSupportedGlobalDimmingLevelsANDROID-supportedGlobalDimmingLevelCountOutput-parameter) `supportedGlobalDimmingLevelCountOutput` **must** be a pointer to a `uint32_t` value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_global_passthrough_dimming#VUID-xrEnumerateSupportedGlobalDimmingLevelsANDROID-supportedGlobalDimmingLevels-parameter) If `supportedGlobalDimmingLevelCapacityInput` is not `0` , `supportedGlobalDimmingLevels` **must** be a pointer to an array of `supportedGlobalDimmingLevelCapacityInput` `float` values

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

## Configure Global Dimming Level

The [XrGlobalDimmingFrameEndInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_global_passthrough_dimming#XrGlobalDimmingFrameEndInfoANDROID) structure is defined as:

    typedef struct XrGlobalDimmingFrameEndInfoANDROID {
        XrStructureType    type;
        const void*        next;
        float              globalDimmingLevel;
    } XrGlobalDimmingFrameEndInfoANDROID;

### Parameter Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.
- `globalDimmingLevel` is a value between 0.0 (transparent) and 1.0 (opaque). The runtime **may** map this value to the closest supported global dimming level. The application **can** set this value to -1.0 to indicate that the current dimming level is preferred.

The `globalDimmingLevel` value specifies the percentage of light being blocked, where a value of 0.0 corresponds to 0% light blocking and 1.0 corresponds to 100% light blocking. The percentage of blocked light **can** be represented in general as:

    100% - Light Transmittance%

The percentage of light transmittance, according to [ISO 8980-3:2022](https://www.iso.org/standard/75921.html) , **can** be measured as the ratio of transmitted radiant flux to incident radiant flux at wavelengths of visible light (380nm to 780nm).

The [XrGlobalDimmingFrameEndInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_global_passthrough_dimming#XrGlobalDimmingFrameEndInfoANDROID) is a structure that an application **can** chain in [XrFrameEndInfo](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrFrameEndInfo) to request a preferred global dimming level.

The runtime **must** honor the requested dimming level if the requested dimming level is different from the current dimming level.

The runtime will have control of the global dimming level and **may** disregard the preferred global dimming level for safety reasons.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_global_passthrough_dimming#VUID-XrGlobalDimmingFrameEndInfoANDROID-extension-notenabled) The `XR_ANDROID_global_passthrough_dimming` extension **must** be enabled prior to using [XrGlobalDimmingFrameEndInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_global_passthrough_dimming#XrGlobalDimmingFrameEndInfoANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_global_passthrough_dimming#VUID-XrGlobalDimmingFrameEndInfoANDROID-type-type) `type` **must** be `XR_TYPE_GLOBAL_DIMMING_FRAME_END_INFO_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_global_passthrough_dimming#VUID-XrGlobalDimmingFrameEndInfoANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)

The [xrGetGlobalDimmingLevelANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_global_passthrough_dimming#xrGetGlobalDimmingLevelANDROID) function is defined as:

    XrResult xrGetGlobalDimmingLevelANDROID(
        XrSession                                   session,
        float*                                      dimmingLevel);

### Parameter Descriptions

- `session` is a valid [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) handle.
- `dimmingLevel` is a pointer to the current dimming level.

The returned `dimmingLevel` **must** be between 0.0 and 1.0 while 0.0 means fully transparent and 1.0 means fully dimmed.

If the dimming level has not been set, the runtime **must** set the dimming level to 0.0 when passthrough is enabled and 1.0 when passthrough is disabled.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_global_passthrough_dimming#VUID-xrGetGlobalDimmingLevelANDROID-extension-notenabled) The `XR_ANDROID_global_passthrough_dimming` extension **must** be enabled prior to calling [xrGetGlobalDimmingLevelANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_global_passthrough_dimming#xrGetGlobalDimmingLevelANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_global_passthrough_dimming#VUID-xrGetGlobalDimmingLevelANDROID-session-parameter) `session` **must** be a valid [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_global_passthrough_dimming#VUID-xrGetGlobalDimmingLevelANDROID-dimmingLevel-parameter) `dimmingLevel` **must** be a pointer to a `float` value

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

## Dimming Level Changed Event

The [XrEventDataGlobalDimmingLevelChangedANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_global_passthrough_dimming#XrEventDataGlobalDimmingLevelChangedANDROID) structure is defined as:

    typedef struct XrEventDataGlobalDimmingLevelChangedANDROID {
        XrStructureType    type;
        const void*        next;
        XrSession          session;
    } XrEventDataGlobalDimmingLevelChangedANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.
- `session` is a valid [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) handle.

The application **can** retrieve this event by using [xrPollEvent](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrPollEvent) . This event will be sent when the dimming level is changed by either apps or physical buttons on devices.

This event will not be sent when focused app switches to another.

The application **should** respond to the event by calling [xrGetGlobalDimmingLevelANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_global_passthrough_dimming#xrGetGlobalDimmingLevelANDROID) to get the new dimming level and update [XrGlobalDimmingFrameEndInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_global_passthrough_dimming#XrGlobalDimmingFrameEndInfoANDROID) :: `globalDimmingLevel` accordingly. Responding to the event guarantees the runtime will be signaled when the application changes preferred dimming level.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_global_passthrough_dimming#VUID-XrEventDataGlobalDimmingLevelChangedANDROID-extension-notenabled) The `XR_ANDROID_global_passthrough_dimming` extension **must** be enabled prior to using [XrEventDataGlobalDimmingLevelChangedANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_global_passthrough_dimming#XrEventDataGlobalDimmingLevelChangedANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_global_passthrough_dimming#VUID-XrEventDataGlobalDimmingLevelChangedANDROID-type-type) `type` **must** be `XR_TYPE_EVENT_DATA_GLOBAL_DIMMING_LEVEL_CHANGED_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_global_passthrough_dimming#VUID-XrEventDataGlobalDimmingLevelChangedANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)

## Example code

### Check system capability \& Enumerate supported global dimming levels

The following example code demonstrates how to check if the global dimming is supported.

    XrInstance instance; // previously initialized
    XrSystemId systemId; // previously initialized

    // The function pointers are previously initialized using xrGetInstanceProcAddr.
    PFN_xrEnumerateSupportedGlobalDimmingLevelsANDROID xrEnumerateSupportedGlobalDimmingLevelsANDROID;

    XrSystemGlobalDimmingPropertiesANDROID dimmingControlSystemProperties { XR_TYPE_SYSTEM_GLOBAL_DIMMING_PROPERTIES_ANDROID };

    XrSystemProperties systemProperties; // Chain dimmingControlSystemProperties

    // ...
    // Run xrGetSystemProperties()
    // ...

    if (!dimmingControlSystemProperties.supportsGlobalDimming) {
      // The system does not support global dimming
      return;
    }

    // Enumerate supported levels
    uint32_t count = 0;
    CHK_XR(xrEnumerateSupportedGlobalDimmingLevelsANDROID(instance, systemId, count, &count, nullptr));

    std::vector<float> supportedLevels(count);
    CHK_XR(xrEnumerateSupportedGlobalDimmingLevelsANDROID(instance, systemId, count, &count, supportedLevels.data()));

### Poll Dimming Level Changed Event

The following example code demonstrates how to poll the dimming level changed event.

    XrEventDataBuffer event{ XR_TYPE_EVENT_DATA_BUFFER };

    // ...
    // Run xrPollEvent()
    // ...

    switch (event.type) {
      // This event will not be sent when focused app switches
      case XR_TYPE_EVENT_DATA_GLOBAL_DIMMING_LEVEL_CHANGED_ANDROID:
      {
        const XrEventDataGlobalDimmingLevelChangedANDROID &dimmingLevelChangedEvent =
                *reinterpret_cast<XrEventDataGlobalDimmingLevelChangedANDROID *>(&event);

        // Query new dimming level using xrGetGlobalDimmingLevelANDROID()
      }
    }

## New Commands

- [xrEnumerateSupportedGlobalDimmingLevelsANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_global_passthrough_dimming#xrEnumerateSupportedGlobalDimmingLevelsANDROID)
- [xrGetGlobalDimmingLevelANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_global_passthrough_dimming#xrGetGlobalDimmingLevelANDROID)

## New Structures

- [XrEventDataGlobalDimmingLevelChangedANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_global_passthrough_dimming#XrEventDataGlobalDimmingLevelChangedANDROID)
- Extending [XrFrameEndInfo](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrFrameEndInfo) :

  - [XrGlobalDimmingFrameEndInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_global_passthrough_dimming#XrGlobalDimmingFrameEndInfoANDROID)
- Extending [XrSystemProperties](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSystemProperties) :

  - [XrSystemGlobalDimmingPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_global_passthrough_dimming#XrSystemGlobalDimmingPropertiesANDROID)

## New Enum Constants

- `XR_ANDROID_GLOBAL_PASSTHROUGH_DIMMING_EXTENSION_NAME`
- `XR_ANDROID_global_passthrough_dimming_SPEC_VERSION`
- Extending [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) :

  - `XR_TYPE_EVENT_DATA_GLOBAL_DIMMING_LEVEL_CHANGED_ANDROID`
  - `XR_TYPE_GLOBAL_DIMMING_FRAME_END_INFO_ANDROID`
  - `XR_TYPE_SYSTEM_GLOBAL_DIMMING_PROPERTIES_ANDROID`

## Issues

## Version History

- Revision 1, 2025-10-07 (Brian Chen)

  - Initial extension description.