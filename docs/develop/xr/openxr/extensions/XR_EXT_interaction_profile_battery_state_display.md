---
title: https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_interaction_profile_battery_state_display
url: https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_interaction_profile_battery_state_display
source: md.txt
---

### XR_EXT_interaction_profile_battery_state_display

**Name String**

`XR_EXT_interaction_profile_battery_state_display`

**Extension Type**

Instance extension

**Registered Extension Number**

837

**Revision**

1

**Ratification Status**

Ratified

**Extension and Version Dependencies**

[OpenXR 1.0](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#versions-1.0)

**Last Modified Date**

2025-10-21

**IP Status**

No known IP claims.

**Contributors**

John Kearney, Meta  

Daniel Willmott, Valve  

Denny Rönngren, Varjo  

Jakob Bornecrantz, NVIDIA  

Nathan Nuber, Valve  

Lachlan Ford, Google  

Nihav Jain, Google

## Overview

`XR_EXT_interaction_profile_battery_state_display` provides a mechanism for applications to query the runtime for battery state information for devices used with interaction profiles. This battery state information **should** only be used for display purposes and the runtime **should** ensure that this information matches what is used in built-in system user interfaces.

In cases where multiple physical devices provide input to the actions associated with a top level path, such as runtimes performing remapping for user customization or accessibility, those runtimes **should** make a best effort to present useful battery information in a single value.

Specifically, it is not expected for this information to be calibrated between runtimes or devices and **should** not be used to generate warnings or otherwise modify the application behavior.

## Querying for battery state

The [XrBatteryStateDisplayEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_interaction_profile_battery_state_display#XrBatteryStateDisplayEXT) structure is defined as:

    typedef struct XrBatteryStateDisplayEXT {
        XrStructureType                       type;
        void*                                 next;
        XrBatteryStateDisplayStateFlagsEXT    stateFlags;
        float                                 batteryLevel;
    } XrBatteryStateDisplayEXT;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `stateFlags` describes the validity of `batteryLevel` with bit masks defined in [XrBatteryStateDisplayStateFlagBitsEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_interaction_profile_battery_state_display#XrBatteryStateDisplayStateFlagBitsEXT)
- `batteryLevel` is the level of the battery (from 0.0f to 1.0f) of the device connected by the associated entity or action.

To query the battery level, the application chains an [XrBatteryStateDisplayEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_interaction_profile_battery_state_display#XrBatteryStateDisplayEXT) structure to the [XrInteractionProfileState](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrInteractionProfileState) :: `next` chain when calling [xrGetCurrentInteractionProfile](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrGetCurrentInteractionProfile) .

If [xrGetCurrentInteractionProfile](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrGetCurrentInteractionProfile) sets the [XrInteractionProfileState](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrInteractionProfileState) :: `interactionProfile` to [XR_NULL_PATH](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_NULL_PATH) , then the runtime **must** not set the `XR_BATTERY_STATE_DISPLAY_STATE_VALID_BIT_EXT` bit in `stateFlags` .

`XR_BATTERY_STATE_DISPLAY_STATE_VALID_BIT_EXT` indicates whether the `batteryLevel` contains valid data. The application **must** not read the `batteryLevel` if the `XR_BATTERY_STATE_DISPLAY_STATE_VALID_BIT_EXT` bit is not set in `stateFlags` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_interaction_profile_battery_state_display#VUID-XrBatteryStateDisplayEXT-extension-notenabled) The `XR_EXT_interaction_profile_battery_state_display` extension **must** be enabled prior to using [XrBatteryStateDisplayEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_interaction_profile_battery_state_display#XrBatteryStateDisplayEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_interaction_profile_battery_state_display#VUID-XrBatteryStateDisplayEXT-type-type) `type` **must** be `XR_TYPE_BATTERY_STATE_DISPLAY_EXT`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_interaction_profile_battery_state_display#VUID-XrBatteryStateDisplayEXT-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_interaction_profile_battery_state_display#VUID-XrBatteryStateDisplayEXT-stateFlags-parameter) `stateFlags` **must** be a valid combination of [XrBatteryStateDisplayStateFlagBitsEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_interaction_profile_battery_state_display#XrBatteryStateDisplayStateFlagBitsEXT) values
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_interaction_profile_battery_state_display#VUID-XrBatteryStateDisplayEXT-stateFlags-requiredbitmask) `stateFlags` **must** not be `0`

The [XrBatteryStateDisplayEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_interaction_profile_battery_state_display#XrBatteryStateDisplayEXT) :: `stateFlags` member is of the following type, and contains a bitwise-OR of zero or more of the bits defined in [XrBatteryStateDisplayStateFlagBitsEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_interaction_profile_battery_state_display#XrBatteryStateDisplayStateFlagBitsEXT) .

    typedef XrFlags64 XrBatteryStateDisplayStateFlagsEXT;

    // Flag bits for XrBatteryStateDisplayStateFlagsEXT
    static const XrBatteryStateDisplayStateFlagsEXT XR_BATTERY_STATE_DISPLAY_STATE_VALID_BIT_EXT = 0x00000001;
    static const XrBatteryStateDisplayStateFlagsEXT XR_BATTERY_STATE_DISPLAY_STATE_CHARGING_BIT_EXT = 0x00000002;
    static const XrBatteryStateDisplayStateFlagsEXT XR_BATTERY_STATE_DISPLAY_STATE_PLUGGED_IN_BIT_EXT = 0x00000004;
    static const XrBatteryStateDisplayStateFlagsEXT XR_BATTERY_STATE_DISPLAY_STATE_NO_BATTERY_BIT_EXT = 0x00000008;

The flag bits have the following meanings:

### Flag Descriptions

- `XR_BATTERY_STATE_DISPLAY_STATE_VALID_BIT_EXT` --- Indicates validity of [XrBatteryStateDisplayEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_interaction_profile_battery_state_display#XrBatteryStateDisplayEXT) :: `batteryLevel`
- `XR_BATTERY_STATE_DISPLAY_STATE_CHARGING_BIT_EXT` --- Indicates that the device associated with the interaction profile is charging.
- `XR_BATTERY_STATE_DISPLAY_STATE_PLUGGED_IN_BIT_EXT` --- Indicates that the device associated with the interaction profile is plugged in to a power source.
- `XR_BATTERY_STATE_DISPLAY_STATE_NO_BATTERY_BIT_EXT` --- Indicates that the device associated with the interaction profile does not have a battery power source.

## Example

    // previously initialized
    extern XrSession session;
    extern XrPath topLevelUserPath;

    XrBatteryStateDisplayEXT batteryStateDisplay{XR_TYPE_BATTERY_STATE_DISPLAY_EXT};
    XrInteractionProfileState ipState{XR_TYPE_INTERACTION_PROFILE_STATE, &batteryStateDisplay};
    CHK_XR(xrGetCurrentInteractionProfile(session, topLevelUserPath, &ipState));
    if ((batteryStateDisplay.stateFlags & XR_BATTERY_STATE_DISPLAY_STATE_VALID_BIT_EXT) != 0) {
      // use value of batteryStateDisplay.batteryLevel
    }

## New Structures

- Extending [XrInteractionProfileState](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrInteractionProfileState) :

  - [XrBatteryStateDisplayEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_interaction_profile_battery_state_display#XrBatteryStateDisplayEXT)

## New Enums

- [XrBatteryStateDisplayStateFlagBitsEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_interaction_profile_battery_state_display#XrBatteryStateDisplayStateFlagBitsEXT)

## New Bitmasks

- [XrBatteryStateDisplayStateFlagsEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_interaction_profile_battery_state_display#XrBatteryStateDisplayStateFlagsEXT)

## New Enum Constants

- `XR_EXT_INTERACTION_PROFILE_BATTERY_STATE_DISPLAY_EXTENSION_NAME`
- `XR_EXT_interaction_profile_battery_state_display_SPEC_VERSION`
- Extending [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) :

  - `XR_TYPE_BATTERY_STATE_DISPLAY_EXT`

## Issues

- Can the application query the battery level displayed for a head-mounted device with this extension?

  - **Resolved.** **Not directly** . This extension only supports returning battery level displayed for top-level */user* paths with current interaction profiles. If the application suggests bindings for an interaction profile for the head-mounted device ( */user/head* ), and if the runtime makes that interaction profile active, then the runtime can return battery level for that top-level */user* path.

## Version History

- Revision 1, 2025-10-21 (John Kearney)

  - Initial draft.