---
title: https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking
url: https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking
source: md.txt
---

**Name String**

`XR_ANDROID_eye_tracking`

**Extension Type**

Instance extension

**Registered Extension Number**

457

**Revision**

1

**Extension and Version Dependencies**

[OpenXR 1.0](https://registry.khronos.org/OpenXR/specs/1.0/html/xrspec.html#versions-1.0)

**Last Modified Date**

2025-01-17

**IP Status**

No known IP claims.

**Contributors**

Spencer Quin, Google

Jared Finder, Google

Levana Chen, Google

Kenny Vercaemer, Google

Prasanthi Gurumurthy, Google

Nihav Jain, Google

## Overview

This extension enables applications to obtain position and orientation of the
user's eyes, as well as eye tracking status.

Eye tracking data is provided in two modes: coarse and fine. Coarse tracking
provides a coarse estimate of the user's eyes, while fine tracking provides a
more accurate estimate. Coarse tracking is meant for applications that want to
provide a basic avatar-like representation, while fine tracking is meant for
more precise applications.

For
interaction, [`XR_EXT_eye_gaze_interaction`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_eye_gaze_interaction) **should** be used.

> [!CAUTION]
> **Caution:**   
>
> **Permissions**   
>
> Android applications **must** have the android.permission.EYE_TRACKING_COARSE or the android.permission.EYE_TRACKING_FINE permission listed in their manifest. These permissions are considered dangerous permissions. The application **must** [request the permission at runtime](https://developer.android.com/training/permissions/requesting) to use these functions:
>
> - [`xrCreateEyeTrackerANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#xrCreateEyeTrackerANDROID)(at least one of the permissions)
> - [`xrGetCoarseTrackingEyesInfoANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#xrGetCoarseTrackingEyesInfoANDROID)(android.permission.EYE_TRACKING_COARSE)
> - [`xrGetFineTrackingEyesInfoANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#xrGetFineTrackingEyesInfoANDROID)(android.permission.EYE_TRACKING_FINE)
>
> (protection level: dangerous)

## Inspect system capability

The [`XrSystemEyeTrackingPropertiesANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrSystemEyeTrackingPropertiesANDROID) structure is defined as:

    typedef struct XrSystemEyeTrackingPropertiesANDROID {
        XrStructureType    type;
        void*              next;
        XrBool32           supportsEyeTracking;
    } XrSystemEyeTrackingPropertiesANDROID;

### Member Descriptions

- `type` is the [`XrStructureType`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.
- `supportsEyeTracking` is an [`XrBool32`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrBool32), indicating if the current system supports eye tracking.

An application **can** inspect whether the system is capable of eye tracking by
chaining an [`XrSystemEyeTrackingPropertiesANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrSystemEyeTrackingPropertiesANDROID) structure to the
[XrSystemProperties](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSystemProperties) when calling [`xrGetSystemProperties`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrGetSystemProperties). If
`supportsEyeTracking` returns `XR_FALSE`, then an application will receive
`XR_ERROR_FEATURE_UNSUPPORTED` from [`xrCreateEyeTrackerANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#xrCreateEyeTrackerANDROID).

### Valid Usage (Implicit)

- The `XR_ANDROID_eye_tracking` extension **must** be enabled prior to using [`XrSystemEyeTrackingPropertiesANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrSystemEyeTrackingPropertiesANDROID)
- `type` **must** be `XR_TYPE_SYSTEM_EYE_TRACKING_PROPERTIES_ANDROID`
- `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-valid-usage-for-structure-pointer-chains)

## Create an eye tracker handle

    XR_DEFINE_HANDLE(XrEyeTrackerANDROID)

The [`XrEyeTrackerANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrEyeTrackerANDROID) handle represents an eye tracker for tracking eyes
and accurately maps what the user is looking at.

Eye tracking data can be sensitive personal information and is closely linked to
personal privacy and integrity. It is strongly recommended that applications
that store or transfer eye tracking data always ask the user for active and
specific acceptance to do so.

This handle **can** be used to access eye tracking data using other functions in
this extension.

Eye tracking provides eye pose and status representation in the scene.

The [`xrCreateEyeTrackerANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#xrCreateEyeTrackerANDROID) function is defined
as:

    XrResult xrCreateEyeTrackerANDROID(
        XrSession                                   session,
        const XrEyeTrackerCreateInfoANDROID*        createInfo,
        XrEyeTrackerANDROID*                        eyeTracker);

### Parameter Descriptions

- `session` is an [`XrSession`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) handle in which the eye tracking will be active.
- `createInfo` is the [`XrEyeTrackerCreateInfoANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrEyeTrackerCreateInfoANDROID) used to specify the eye tracking.
- `eyeTracker` is the returned [`XrEyeTrackerANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrEyeTrackerANDROID) handle.

An application **can** create an [`XrEyeTrackerANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrEyeTrackerANDROID) handle using
[`xrCreateEyeTrackerANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#xrCreateEyeTrackerANDROID) function.

If the system does not support eye tracking, then `XR_ERROR_FEATURE_UNSUPPORTED`
will be returned from [`xrCreateEyeTrackerANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#xrCreateEyeTrackerANDROID).

### Valid Usage (Implicit)

- The `XR_ANDROID_eye_tracking` extension **must** be enabled prior to calling [`xrCreateEyeTrackerANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#xrCreateEyeTrackerANDROID)
- `session` **must** be a valid [`XrSession`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) handle
- `createInfo` **must** be a pointer to a valid [`XrEyeTrackerCreateInfoANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrEyeTrackerCreateInfoANDROID) structure
- `eyeTracker` **must** be a pointer to an [`XrEyeTrackerANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrEyeTrackerANDROID) handle

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
- `XR_ERROR_OUT_OF_MEMORY`
- `XR_ERROR_LIMIT_REACHED`
- `XR_ERROR_FEATURE_UNSUPPORTED`

The [`XrEyeTrackerCreateInfoANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrEyeTrackerCreateInfoANDROID) structure is defined as:

    typedef struct XrEyeTrackerCreateInfoANDROID {
        XrStructureType    type;
        void*              next;
    } XrEyeTrackerCreateInfoANDROID;

### Member Descriptions

- `type` is the [`XrStructureType`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.

The [`XrEyeTrackerCreateInfoANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrEyeTrackerCreateInfoANDROID) structure describes the information to
create an [`XrEyeTrackerANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrEyeTrackerANDROID) handle.

### Valid Usage (Implicit)

- The `XR_ANDROID_eye_tracking` extension **must** be enabled prior to using [`XrEyeTrackerCreateInfoANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrEyeTrackerCreateInfoANDROID)
- `type` **must** be `XR_TYPE_EYE_TRACKER_CREATE_INFO_ANDROID`
- `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-valid-usage-for-structure-pointer-chains)

The [`xrDestroyEyeTrackerANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#xrDestroyEyeTrackerANDROID) function is defined as:

    XrResult xrDestroyEyeTrackerANDROID(
        XrEyeTrackerANDROID                         eyeTracker);

### Parameter Descriptions

- `eyeTracker` is an [`XrEyeTrackerANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrEyeTrackerANDROID) previously created by [`xrCreateEyeTrackerANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#xrCreateEyeTrackerANDROID).

[`xrDestroyEyeTrackerANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#xrDestroyEyeTrackerANDROID) function releases the `eyeTracker` and the
underlying resources when finished with eye tracking experiences.

### Valid Usage (Implicit)

- The `XR_ANDROID_eye_tracking` extension **must** be enabled prior to calling [`xrDestroyEyeTrackerANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#xrDestroyEyeTrackerANDROID)
- `eyeTracker` **must** be a valid [`XrEyeTrackerANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrEyeTrackerANDROID) handle.

### Thread Safety

- Access to `eyeTracker`, and any child handles, **must** be externally synchronized

### Return Codes

[**Success**](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`

[**Failure**](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_HANDLE_INVALID`

## Getting eyes information

The [`xrGetCoarseTrackingEyesInfoANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#xrGetCoarseTrackingEyesInfoANDROID) function is defined as:

    XrResult xrGetCoarseTrackingEyesInfoANDROID(
        XrEyeTrackerANDROID                         eyeTracker,
        const XrEyesGetInfoANDROID*                 getInfo,
        XrEyesANDROID*                              eyesOutput);

### Parameter Descriptions

- `eyeTracker` is an [`XrEyeTrackerANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrEyeTrackerANDROID) previously created by [`xrCreateEyeTrackerANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#xrCreateEyeTrackerANDROID).
- `getInfo` is a pointer to [`XrEyesGetInfoANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrEyesGetInfoANDROID) used to specify what output is required.
- `infoOutput` is a pointer to [`XrEyesANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrEyesANDROID) that contains the returned eyes information including poses and states.

[`xrGetCoarseTrackingEyesInfoANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#xrGetCoarseTrackingEyesInfoANDROID) function gets the information for eye
states and
poses in a way that preserves user privacy.

The runtime must return `XR_ERROR_PERMISSION_INSUFFICIENT` if the application
does not have the `android.permission.EYE_TRACKING_COARSE` permission.

The eyes information is resolved and relative to the base space at the time of
the call to [`xrGetCoarseTrackingEyesInfoANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#xrGetCoarseTrackingEyesInfoANDROID) using
[`XrEyesGetInfoANDROID::time`, `XrEyesGetInfoANDROID::baseSpace`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrEyesGetInfoANDROID).

At any point of time both the position and direction of the eye pose is tracked
or untracked. This means that applications can expect that both
`XR_SPACE_LOCATION_POSITION_TRACKED_BIT` and
`XR_SPACE_LOCATION_ORIENTATION_TRACKED_BIT` will either be set or cleared on the
supplied [`XrEyesANDROID::eyes`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrEyesANDROID), and that [`XrEyesANDROID::mode`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrEyesANDROID) will
indicate the tracking states.

### Valid Usage (Implicit)

- The `XR_ANDROID_eye_tracking` extension **must** be enabled prior to calling [`xrGetCoarseTrackingEyesInfoANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#xrGetCoarseTrackingEyesInfoANDROID)
- `eyeTracker` **must** be a valid [`XrEyeTrackerANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrEyeTrackerANDROID) handle
- `getInfo` **must** be a pointer to a valid [`XrEyesGetInfoANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrEyesGetInfoANDROID) structure
- `eyesOutput` **must** be a pointer to an [`XrEyesANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrEyesANDROID) structure

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
- `XR_ERROR_OUT_OF_MEMORY`
- `XR_ERROR_LIMIT_REACHED`
- `XR_ERROR_TIME_INVALID`
- `XR_ERROR_PERMISSION_INSUFFICIENT`

The [`xrGetFineTrackingEyesInfoANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#xrGetFineTrackingEyesInfoANDROID)
function is defined as:

    XrResult xrGetFineTrackingEyesInfoANDROID(
        XrEyeTrackerANDROID                         eyeTracker,
        const XrEyesGetInfoANDROID*                 getInfo,
        XrEyesANDROID*                              eyesOutput);

### Parameter Descriptions

- `eyeTracker` is an [`XrEyeTrackerANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrEyeTrackerANDROID) previously created by [`xrCreateEyeTrackerANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#xrCreateEyeTrackerANDROID).
- `getInfo` is a pointer to [`XrEyesGetInfoANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrEyesGetInfoANDROID) used to specify what output is required.
- `infoOutput` is a pointer to [`XrEyesANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrEyesANDROID) that contains the returned eyes information including poses and states. [`xrGetFineTrackingEyesInfoANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#xrGetFineTrackingEyesInfoANDROID) function gets the information for eye states and poses with higher precision than [`xrGetCoarseTrackingEyesInfoANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#xrGetCoarseTrackingEyesInfoANDROID).

The runtime must return `XR_ERROR_PERMISSION_INSUFFICIENT` if the application
does not have the `android.permission.EYE_TRACKING_FINE` permission.

The eyes information is resolved and relative to the base space at the time of
the call to [`xrGetFineTrackingEyesInfoANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#xrGetFineTrackingEyesInfoANDROID) using
[`XrEyesGetInfoANDROID::time`, `XrEyesGetInfoANDROID::baseSpace`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrEyesGetInfoANDROID).

At any point of time both the position and direction of the eye pose is tracked
or untracked. This means that applications can expect that both
`XR_SPACE_LOCATION_POSITION_TRACKED_BIT` and
`XR_SPACE_LOCATION_ORIENTATION_TRACKED_BIT` will either be set or cleared on the
supplied [`XrEyesANDROID::eyes`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrEyesANDROID), and that [`XrEyesANDROID::mode`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrEyesANDROID) will
indicate the tracking states.

### Valid Usage (Implicit)

- The `XR_ANDROID_eye_tracking` extension **must** be enabled prior to calling [`xrGetFineTrackingEyesInfoANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#xrGetFineTrackingEyesInfoANDROID)
- `eyeTracker` **must** be a valid [`XrEyeTrackerANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrEyeTrackerANDROID) handle
- `getInfo` **must** be a pointer to a valid [`XrEyesGetInfoANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrEyesGetInfoANDROID) structure
- `eyesOutput` **must** be a pointer to an [`XrEyesANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrEyesANDROID) structure

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
- `XR_ERROR_OUT_OF_MEMORY`
- `XR_ERROR_LIMIT_REACHED`
- `XR_ERROR_TIME_INVALID`
- `XR_ERROR_PERMISSION_INSUFFICIENT`

[`XrEyesGetInfoANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrEyesGetInfoANDROID) structure contains the information required to
retrieve eye poses and states.

    typedef struct XrEyesGetInfoANDROID {
        XrStructureType    type;
        void*              next;
        XrTime             time;
        XrSpace            baseSpace;
    } XrEyesGetInfoANDROID;

### Member Descriptions

- `type` is the [`XrStructureType`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.
- `time` is the [`XrTime`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrTime) at which to evaluate the coordinates relative to the `baseSpace`.
- `baseSpace` the eye pose will be relative to this [`XrSpace`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpace) at `time`.

### Valid Usage (Implicit)

- The `XR_ANDROID_eye_tracking` extension **must** be enabled prior to using [`XrEyesGetInfoANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrEyesGetInfoANDROID)
- `type` **must** be `XR_TYPE_EYES_GET_INFO_ANDROID`
- `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-valid-usage-for-structure-pointer-chains)
- `baseSpace` **must** be a valid [`XrSpace`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpace) handle

[`XrEyesANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrEyesANDROID) structure contains information on the tracked eyes.

    typedef struct XrEyesANDROID {
        XrStructureType             type;
        void*                       next;
        XrEyeANDROID                eyes[XR_EYE_MAX_ANDROID];
        XrEyeTrackingModeANDROID    mode;
    } XrEyesANDROID;

### Member Descriptions

- `type` is the [`XrStructureType`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.
- `eyes` is an array of [`XrEyeANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrEyeANDROID) for the left and right eyes as indexed by `XrEyeIndexANDROID`.
- `mode` is the [`XrEyeTrackingModeANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrEyeTrackingModeANDROID) to indicate if the eyes are tracking and which ones.

### Valid Usage (Implicit)

- The `XR_ANDROID_eye_tracking` extension **must** be enabled prior to using [`XrEyesANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrEyesANDROID)
- `type` **must** be `XR_TYPE_EYES_ANDROID`
- `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-valid-usage-for-structure-pointer-chains)
- Any given element of `eyes` **must** be a valid [`XrEyeANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrEyeANDROID) structure
- `mode` **must** be a valid [`XrEyeTrackingModeANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrEyeTrackingModeANDROID) value

[`XrEyeANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrEyeANDROID) structure describes the state, position and orientation of an
eye.

    typedef struct XrEyeANDROID {
        XrEyeStateANDROID    eyeState;
        XrPosef              eyePose;
    } XrEyeANDROID;

### Member Descriptions

- `eyeState` is the [`XrEyeStateANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrEyeStateANDROID) of an eye.
- `pose` is an [`XrPosef`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrPosef) defining the position and orientation of the origin of an eye within the reference frame of the corresponding [`XrEyesGetInfoANDROID::baseSpace`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrEyesGetInfoANDROID). An identity orientation here represents a coordinate axes with +Z into the user's eyes, +X to the right and +Y up.

### Valid Usage (Implicit)

- The `XR_ANDROID_eye_tracking` extension **must** be enabled prior to using [`XrEyeANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrEyeANDROID)
- `eyeState` **must** be a valid [`XrEyeStateANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrEyeStateANDROID) value

The [`XrEyeStateANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrEyeStateANDROID) enumeration identifies the different states of
tracked eyes.

    typedef enum XrEyeStateANDROID {
        XR_EYE_STATE_INVALID_ANDROID = 0,
        XR_EYE_STATE_GAZING_ANDROID = 1,
        XR_EYE_STATE_SHUT_ANDROID = 2
    } XrEyeStateANDROID;

The enums have the following meanings:

|---|---|
| **Enum** | **Description** |
| `XR_EYE_STATE_INVALID_ANDROID` | Indicates that the eye is in an error state or not present. |
| `XR_EYE_STATE_GAZING_ANDROID` | Indicates that the eye is gazing. |
| `XR_EYE_STATE_SHUT_ANDROID` | Indicates that the eye is shut due to a wink or a blink. |

The [`XrEyeIndexANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrEyeIndexANDROID) enumeration identifies the index of the left or
right eye.

    typedef enum XrEyeIndexANDROID {
        XR_EYE_INDEX_LEFT_ANDROID = 0,
        XR_EYE_INDEX_RIGHT_ANDROID = 1
    } XrEyeIndexANDROID;

The enums have the following meanings:

|---|---|
| **Enum** | **Description** |
| `XR_EYE_INDEX_LEFT_ANDROID` | Left eye. |
| `XR_EYE_INDEX_RIGHT_ANDROID` | Right eye. |

The [`XrEyeTrackingModeANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrEyeTrackingModeANDROID) enumeration identifies the different modes of
tracked eyes.

    typedef enum XrEyeTrackingModeANDROID {
        XR_EYE_TRACKING_MODE_NOT_TRACKING_ANDROID = 0,
        XR_EYE_TRACKING_MODE_RIGHT_ANDROID = 1,
        XR_EYE_TRACKING_MODE_LEFT_ANDROID = 2,
        XR_EYE_TRACKING_MODE_BOTH_ANDROID = 3
    } XrEyeTrackingModeANDROID;

The enums have the following meanings:

|---|---|
| **Enum** | **Description** |
| `XR_EYE_TRACKING_MODE_NOT_TRACKING_ANDROID` | Indicates that eye tracking is not active. |
| `XR_EYE_TRACKING_MODE_RIGHT_ANDROID` | Indicates that only the right eye is tracking. |
| `XR_EYE_TRACKING_MODE_LEFT_ANDROID` | Indicates that only the left eye is tracking. |
| `XR_EYE_TRACKING_MODE_BOTH_ANDROID` | Indicates that both the left and right eyes are tracking. |

## Example code for eye tracking

The following example code demonstrates how to get eye information relative to a
view space.

    XrSession session; // previously initialized, e.g. created at app startup.
    XrSpace viewSpace; // space created for XR_REFERENCE_SPACE_TYPE_VIEW.

    // The function pointers are previously initialized using xrGetInstanceProcAddr.
    PFN_xrCreateEyeTrackerANDROID xrCreateEyeTrackerANDROID; // previously initialized
    PFN_xrDestroyEyeTrackerANDROID xrDestroyEyeTrackerANDROID; // previously initialized
    PFN_xrGetCoarseTrackingEyesInfoANDROID xrGetCoarseTrackingEyesInfoANDROID; // previously initialized
    PFN_xrGetFineTrackingEyesInfoANDROID xrGetFineTrackingEyesInfoANDROID; // previously initialized

    // This will use the XrSession that is bound to the eye tracker done at time of creation.
    XrEyeTrackerANDROID eyeTracker;
    XrEyeTrackerCreateInfoANDROID createInfo{
        .type = XR_TYPE_EYE_TRACKER_CREATE_INFO_ANDROID,
        .next = nullptr};
    CHK_XR(xrCreateEyeTrackerANDROID(session, &createInfo, &eyeTracker));

    while (1) {
        // ...
        // For every frame in frame loop
        // ...

        XrFrameState frameState;  // previously returned from xrWaitFrame
        const XrTime time = frameState.predictedDisplayTime;
        XrEyesANDROID fineEyesInfo{.type = XR_TYPE_EYES_ANDROID,
                                   .next = nullptr,
                                   .mode = XR_EYE_TRACKING_MODE_BOTH_ANDROID};
        XrEyesANDROID coarseEyesInfo{.type = XR_TYPE_EYES_ANDROID,
                                     .next = nullptr,
                                     .mode = XR_EYE_TRACKING_MODE_BOTH_ANDROID};
        XrEyesGetInfoANDROID eyesGetInfo{.type = XR_TYPE_EYES_GET_INFO_ANDROID,
                                         .next = nullptr,
                                         .time = time,
                                         .baseSpace = viewSpace};
        CHK_XR(xrGetCoarseTrackingEyesInfoANDROID(eyeTracker, &eyesGetInfo, &coarseEyesInfo));
        CHK_XR(xrGetFineTrackingEyesInfoANDROID(eyeTracker, &eyesGetInfo, &fineEyesInfo));

        // eyes tracking information is now available:
        // drawLeftEye(eyesInfo.eyes[XR_EYE_INDEX_LEFT_ANDROID].eyePose);
        // drawRightEye(eyesInfo.eyes[XR_EYE_INDEX_RIGHT_ANDROID].eyePose);

        // ...
        // Finish frame loop
        // ...
    }

    // after usage
    CHK_XR(xrDestroyEyeTrackerANDROID(eyeTracker));

**New Object Types**

- [`XrEyeTrackerANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrEyeTrackerANDROID)

**New Enum Constants**

- `XR_EYE_MAX_ANDROID`

[`XrObjectType`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrObjectType) enumeration is extended with:

- `XR_OBJECT_TYPE_EYE_TRACKER_ANDROID`

[`XrStructureType`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) enumeration is extended with:

- `XR_TYPE_EYES_ANDROID`
- `XR_TYPE_EYE_TRACKER_CREATE_INFO_ANDROID`
- `XR_TYPE_EYES_GET_INFO_ANDROID`
- `XR_TYPE_SYSTEM_EYE_TRACKING_PROPERTIES_ANDROID`

**New Enums**

- [`XrEyeIndexANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrEyeIndexANDROID)
- [`XrEyeStateANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrEyeStateANDROID)
- [`XrEyeTrackingModeANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrEyeTrackingModeANDROID)

**New Structures**

- [`XrEyeANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrEyeANDROID)
- [`XrEyesANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrEyesANDROID)
- [`XrEyesGetInfoANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrEyesGetInfoANDROID)
- [`XrEyeTrackerCreateInfoANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrEyeTrackerCreateInfoANDROID)
- [`XrSystemEyeTrackingPropertiesANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#XrSystemEyeTrackingPropertiesANDROID)

**New Functions**

- [`xrCreateEyeTrackerANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#xrCreateEyeTrackerANDROID)
- [`xrDestroyEyeTrackerANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#xrDestroyEyeTrackerANDROID)
- [`xrGetCoarseTrackingEyesInfoANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#xrGetCoarseTrackingEyesInfoANDROID)
- [`xrGetFineTrackingEyesInfoANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking#xrGetFineTrackingEyesInfoANDROID)

**Issues**

**Version History**

- Revision 1, 2025-01-17 (Kenny Vercaemer)
  - Initial extension description

*** ** * ** ***

OpenXR™ and the OpenXR logo are trademarks owned
by The Khronos Group Inc. and are registered as a trademark in China,
the European Union, Japan and the United Kingdom.