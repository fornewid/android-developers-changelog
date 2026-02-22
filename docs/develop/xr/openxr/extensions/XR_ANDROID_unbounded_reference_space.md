---
title: https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_unbounded_reference_space
url: https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_unbounded_reference_space
source: md.txt
---

**Name String**

`XR_ANDROID_unbounded_reference_space`

**Extension Type**

Instance extension

**Registered Extension Number**

468

**Revision**

1

**Extension and Version Dependencies**

[OpenXR 1.0](https://registry.khronos.org/OpenXR/specs/1.0/html/xrspec.html#versions-1.0)

**Last Modified Date**

2024-09-12

**IP Status**

No known IP claims.

**Contributors**

Spencer Quin, Google

Jared Finder, Google

Fengtao Fan, Google

Lachlan Ford, Google

Nihav Jain, Google

Levana Chen, Google

## Overview

This extension allows applications to create an`UNBOUNDED_ANDROID`reference space. This reference space enables the viewer to move freely through a complex environment, often many meters from where they started, while always optimizing for coordinate system stability near the viewer. As the device senses more of its environment to build a better scene understanding, the origin of the reference space**can** drift with**huge adjustments**as necessary to maintain device tracking.

To create an`UNBOUNDED_ANDROID`reference space, the application**can** set[XrReferenceSpaceCreateInfo::referenceSpaceType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrReferenceSpaceCreateInfo)`XR_REFERENCE_SPACE_TYPE_UNBOUNDED_ANDROID`and pass to[xrCreateReferenceSpace](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateReferenceSpace).  

    XrInstance instance; // previously initialized
    XrSession session; // previously initialized
    XrPosef pose; // previously initialized

    // Use the new reference space type in the create info struct
    XrReferenceSpaceCreateInfo createInfo = {
        .type = XR_REFERENCE_SPACE_CREATE_INFO;
        .next = nullptr;
        .referenceSpaceType = XR_REFERENCE_SPACE_TYPE_UNBOUNDED_ANDROID;
        .poseInReferenceSpace = pose;
    }
    XrSpace referenceSpace;
    CHK_XR(xrCreateReferenceSpace(session, &createInfo, &referenceSpace));

    // After usage
    CHK_XR(xrDestroySpace(referenceSpace));

The`UNBOUNDED_ANDROID`reference space establishes a world-locked origin of the headset's position when the device tracking starts. It is gravity-aligned to exclude pitch and roll, with +X to the right, +Y up, and -Z forward.

`UNBOUNDED_ANDROID`space is useful when an application needs to render**world-scale** content that spans beyond the bounds of a single`STAGE`, for example, an entire floor or multiple floors of a building.

An`UNBOUNDED_ANDROID`space maintains stability near the viewer by adjusting its origin over time. It**can** make**slight** and**huge**adjustments as necessary to maintain device tracking.

- The runtime**should** not queue the[XrEventDataReferenceSpaceChangePending](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrEventDataReferenceSpaceChangePending)event in response to**minor adjustments**.
- The runtime**should** queue the[XrEventDataReferenceSpaceChangePending](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrEventDataReferenceSpaceChangePending)event in response to**huge adjustments** . For example, the pose in`UNBOUNDED_ANDROID`space is reset due to a tracking loss and the tracking is re-established on a disconnected estimate of the world (a "new map").
- The system is constantly updating its understanding of the world and adjusting device tracking. If an application requires a persisted location regardless of tracking resets, an anchor**can**be used in this case.

## Reference space change event

For parameters defined by[XrEventDataReferenceSpaceChangePending](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrEventDataReferenceSpaceChangePending)structure that returned on world changing or optimizing relocalization events:  

    typedef struct XrEventDataReferenceSpaceChangePending {
        XrStructureType         type;
        const void*             next;
        XrSession               session;
        XrReferenceSpaceType    referenceSpaceType;
        XrTime                  changeTime;
        XrBool32                poseValid;
        XrPosef                 poseInPreviousSpace;
    } XrEventDataReferenceSpaceChangePending;

### Member Descriptions

- `referenceSpaceType`is`XR_REFERENCE_SPACE_TYPE_UNBOUNDED_ANDROID`.
- `changeTime`will represent the[`XrTime`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTime)at which relocalization completed.
- `poseValid`will be`false`due to the disconnected estimate or`true`after reconnected.
- `poseInPreviousSpace`won't be valid when`poseValid`is`false`.

When views, controllers or other spaces experience tracking loss relative to the`UNBOUNDED_ANDROID`space, applications**can** continue to receive inferred or last-known`position`and`orientation`values. These inferred poses**can** , for example, be based on neck model updates, inertial dead reckoning, or a last-known position. An application can assume that it will continue to have the`XR_SPACE_LOCATION_POSITION_VALID_BIT`and`XR_VIEW_STATE_POSITION_VALID_BIT`set, but`XR_SPACE_LOCATION_POSITION_TRACKED_BIT`and`XR_VIEW_STATE_POSITION_TRACKED_BIT`may be cleared by the runtime to indicate that the position is inferred or last-known in this way.

When tracking is recovered, the runtime**may** recenter the origin arbitrarily, for example moving the origin to coincide with the viewer. An application**can** check the`poseValid`value returned from the[XrEventDataReferenceSpaceChangePending](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrEventDataReferenceSpaceChangePending)event to determine if it's ready to use.

**New Object Types**

**New Flag Types**

**New Enum Constants**

[XrReferenceSpaceType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrReferenceSpaceType)enumeration is extended with:

- `XR_REFERENCE_SPACE_TYPE_UNBOUNDED_ANDROID`

**New Enums**

**New Structures**

**New Functions**

**Issues**

**Version History**

- Revision 1, 2024-09-12 (Levana Chen)
  - Initial extension description

*** ** * ** ***

OpenXR™ and the OpenXR logo are trademarks owned by The Khronos Group Inc. and are registered as a trademark in China, the European Union, Japan and the United Kingdom.