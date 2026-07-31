---
title: https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_recommended_settings
url: https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_recommended_settings
source: md.txt
---

### XR_ANDROID_recommended_settings

**Name String**

`XR_ANDROID_recommended_settings`

**Extension Type**

Instance extension

**Registered Extension Number**

455

**Revision**

1

**Ratification Status**

Not ratified

**Extension and Version Dependencies**

[OpenXR 1.0](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#versions-1.0)

**Last Modified Date**

2026-03-16

**Contributors**

Spencer Quin, Google  

Jared Finder, Google  

Kevin Moule, Google  

Nihav Jain, Google  

Levana Chen, Google  

Alvin Shi, Google  

Salar Khan, Google

## Overview

The user's default environment **can** be in a variety of states using a combination of a blend mode and input modality. This extension provides the recommended settings for the user, which correspond to the state of the user's default environment before application launch, to ensure a smooth transition.

## Structs and Enums

The [XrInputModalityFlagsANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_recommended_settings#XrInputModalityFlagsANDROID) bits identifies different input modalities which the **may** be in use.

    typedef XrFlags64 XrInputModalityFlagsANDROID;

Valid bits for [XrInputModalityFlagsANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_recommended_settings#XrInputModalityFlagsANDROID) are defined by [XrInputModalityFlagBitsANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_recommended_settings#XrInputModalityFlagBitsANDROID) , which is specified as:

    // Flag bits for XrInputModalityFlagsANDROID
    static const XrInputModalityFlagsANDROID XR_INPUT_MODALITY_HEAD_BIT_ANDROID = 0x00000001;
    static const XrInputModalityFlagsANDROID XR_INPUT_MODALITY_CONTROLLER_BIT_ANDROID = 0x00000002;
    static const XrInputModalityFlagsANDROID XR_INPUT_MODALITY_HANDS_BIT_ANDROID = 0x00000004;
    static const XrInputModalityFlagsANDROID XR_INPUT_MODALITY_MOUSE_BIT_ANDROID = 0x00000008;
    static const XrInputModalityFlagsANDROID XR_INPUT_MODALITY_GAZE_AND_GESTURE_BIT_ANDROID = 0x00000010;

### Flag Descriptions

- `XR_INPUT_MODALITY_HEAD_BIT_ANDROID` --- Indicates an input modality that is using head tracking.
- `XR_INPUT_MODALITY_CONTROLLER_BIT_ANDROID` --- Indicates an input modality that is using any XR controller inputs.
- `XR_INPUT_MODALITY_HANDS_BIT_ANDROID` --- Indicates an input modality that is using hand tracking.
- `XR_INPUT_MODALITY_MOUSE_BIT_ANDROID` --- Indicates an input modality that is using mouse inputs.
- `XR_INPUT_MODALITY_GAZE_AND_GESTURE_BIT_ANDROID` --- Indicates an input modality that combines eye tracking and hand tracking.

The [XrRecommendedSettingsANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_recommended_settings#XrRecommendedSettingsANDROID) structure is defined as:

    typedef struct XrRecommendedSettingsANDROID {
        XrStructureType                type;
        void*                          next;
        XrEnvironmentBlendMode         blendMode;
        float                          passthroughOpacity;
        XrInputModalityFlagsANDROID    activeInputModalities;
    } XrRecommendedSettingsANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.
- `blendMode` is a [XrEnvironmentBlendMode](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrEnvironmentBlendMode) indicating the default environment's blend mode just before application launch.
- `passthroughOpacity` is a `float` indicating the default environment's passthrough opacity just before application launch. The runtime **must** set this value to (1.0 - dimming_value) for OST devices.
- `activeInputModalities` is a bitmask of [XrInputModalityFlagsANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_recommended_settings#XrInputModalityFlagsANDROID) indicating the input modalities in use within the default environment just before application launch.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_recommended_settings#VUID-XrRecommendedSettingsANDROID-extension-notenabled) The `XR_ANDROID_recommended_settings` extension **must** be enabled prior to using [XrRecommendedSettingsANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_recommended_settings#XrRecommendedSettingsANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_recommended_settings#VUID-XrRecommendedSettingsANDROID-type-type) `type` **must** be `XR_TYPE_RECOMMENDED_SETTINGS_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_recommended_settings#VUID-XrRecommendedSettingsANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_recommended_settings#VUID-XrRecommendedSettingsANDROID-blendMode-parameter) `blendMode` **must** be a valid [XrEnvironmentBlendMode](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrEnvironmentBlendMode) value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_recommended_settings#VUID-XrRecommendedSettingsANDROID-activeInputModalities-parameter) `activeInputModalities` **must** be a valid combination of [XrInputModalityFlagBitsANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_recommended_settings#XrInputModalityFlagBitsANDROID) values
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_recommended_settings#VUID-XrRecommendedSettingsANDROID-activeInputModalities-requiredbitmask) `activeInputModalities` **must** not be `0`

## Enumerating supported environment states

An application **can** determine which blend mode and input modality states are supported by the system with [xrEnumerateEnvironmentBlendModes](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrEnumerateEnvironmentBlendModes) and extending the [XrSystemProperties](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSystemProperties) with [XrSystemInputModalityPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_recommended_settings#XrSystemInputModalityPropertiesANDROID) structure when calling [xrGetSystemProperties](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrGetSystemProperties) .

The [XrSystemInputModalityPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_recommended_settings#XrSystemInputModalityPropertiesANDROID) structure is defined as:

    typedef struct XrSystemInputModalityPropertiesANDROID {
        XrStructureType                type;
        void*                          next;
        XrInputModalityFlagsANDROID    supportedInputModalities;
    } XrSystemInputModalityPropertiesANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.
- `supportedInputModalities` is one or more [XrInputModalityFlagsANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_recommended_settings#XrInputModalityFlagsANDROID) indicating the input modalities supported by the system.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_recommended_settings#VUID-XrSystemInputModalityPropertiesANDROID-extension-notenabled) The `XR_ANDROID_recommended_settings` extension **must** be enabled prior to using [XrSystemInputModalityPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_recommended_settings#XrSystemInputModalityPropertiesANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_recommended_settings#VUID-XrSystemInputModalityPropertiesANDROID-type-type) `type` **must** be `XR_TYPE_SYSTEM_INPUT_MODALITY_PROPERTIES_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_recommended_settings#VUID-XrSystemInputModalityPropertiesANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)

## Get the recommended settings (prelaunch default environment state)

    XrResult xrGetRecommendedSettingsANDROID(
        XrInstance                                  instance,
        XrSystemId                                  systemId,
        XrRecommendedSettingsANDROID*               output);

### Parameter Descriptions

- `instance` is an [XrInstance](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrInstance) handle previously created with [xrCreateInstance](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateInstance) .
- `systemId` is an `XrSystemId` previously fetched from [xrGetSystem](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrGetSystem) .
- `output` is a pointer to an [XrRecommendedSettingsANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_recommended_settings#XrRecommendedSettingsANDROID) struct which is outputted with the default environment state.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_recommended_settings#VUID-xrGetRecommendedSettingsANDROID-extension-notenabled) The `XR_ANDROID_recommended_settings` extension **must** be enabled prior to calling [xrGetRecommendedSettingsANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_recommended_settings#xrGetRecommendedSettingsANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_recommended_settings#VUID-xrGetRecommendedSettingsANDROID-instance-parameter) `instance` **must** be a valid [XrInstance](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrInstance) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_recommended_settings#VUID-xrGetRecommendedSettingsANDROID-output-parameter) `output` **must** be a pointer to an [XrRecommendedSettingsANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_recommended_settings#XrRecommendedSettingsANDROID) structure

### Return Codes

[Success](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`

[Failure](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_HANDLE_INVALID`
- `XR_ERROR_INSTANCE_LOST`
- `XR_ERROR_RUNTIME_FAILURE`
- `XR_ERROR_SYSTEM_INVALID`

## Example code for recommended settings

The following example code demonstrates how to get supported input modalities, get recommended settings, and asserts that the reported settings are supported by the system.

    XrInstance instance;  // Created at app startup
    XrSystemId systemId;  // previously initialized from xrGetSystem
    XrViewConfigurationType viewType;  // previously initialized to select desired view configuration

    // The function pointers are previously initialized using xrGetInstanceProcAddr.
    PFN_xrGetRecommendedSettingsANDROID xrGetRecommendedSettingsANDROID; // previously initialized

    XrSystemInputModalityPropertiesANDROID props = {
      .type = XR_TYPE_SYSTEM_INPUT_MODALITY_PROPERTIES_ANDROID
    };
    XrSystemProperties base = {
      .type = XR_TYPE_SYSTEM_PROPERTIES,
      .next = &props
    };
    CHK_XR(xrGetSystemProperties(instance, systemId, &base));

    uint32_t blendModeCount = 0;
    CHK_XR(
     xrEnumerateEnvironmentBlendModes(instance, systemId, viewType, 0, &blendModeCount, nullptr));
    std::vector<XrEnvironmentBlendMode> supportedBlendModes(blendModeCount);
    CHK_XR(
      xrEnumerateEnvironmentBlendModes(
        instance, systemId, viewType, blendModeCount, &blendModeCount, supportedBlendModes.data()));

    XrRecommendedSettingsANDROID output = {
      .type = XR_TYPE_RECOMMENDED_SETTINGS_ANDROID
    };

    XrResult result = xrGetRecommendedSettingsANDROID(instance, systemId, &output);

    if (result == XR_SUCCESS) {
      // We now know the current state of the default environment as recommended settings

      bool correctBlendMode = false;
      for(XrEnvironmentBlendMode blendMode : supportedBlendModes) {
        if (blendMode == output.blendMode) {
          correctBlendMode = true;
          break;
        }
      }
      assert(correctBlendMode);
      assert((~props.supportedInputModalities & output.activeInputModalities) == 0);
    }

## New Commands

- [xrGetRecommendedSettingsANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_recommended_settings#xrGetRecommendedSettingsANDROID)

## New Structures

- [XrRecommendedSettingsANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_recommended_settings#XrRecommendedSettingsANDROID)
- Extending [XrSystemProperties](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSystemProperties) :

  - [XrSystemInputModalityPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_recommended_settings#XrSystemInputModalityPropertiesANDROID)

## New Enums

- [XrInputModalityFlagBitsANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_recommended_settings#XrInputModalityFlagBitsANDROID)

## New Bitmasks

- [XrInputModalityFlagsANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_recommended_settings#XrInputModalityFlagsANDROID)

## New Enum Constants

- `XR_ANDROID_RECOMMENDED_SETTINGS_EXTENSION_NAME`
- `XR_ANDROID_recommended_settings_SPEC_VERSION`
- Extending [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) :

  - `XR_TYPE_RECOMMENDED_SETTINGS_ANDROID`
  - `XR_TYPE_SYSTEM_INPUT_MODALITY_PROPERTIES_ANDROID`

**Issues**

**Version History**

- Revision 3, 2026-03-16 (Salar Khan)

  - Promoted to public, made input modalities flag bits, and changed extension name to `XR_ANDROID_recommended_settings` .
- Revision 2, 2025-03-28 (Salar Khan)

  - Change to ANDROIDX and included passthroughOpacity.
- Revision 1, 2025-02-18 (Salar Khan)

  - Initial version.