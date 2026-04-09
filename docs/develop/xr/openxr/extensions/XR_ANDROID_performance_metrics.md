---
title: https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_performance_metrics
url: https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_performance_metrics
source: md.txt
---

**Name String**

`XR_ANDROID_performance_metrics`

**Extension Type**

Instance extension

**Registered Extension Number**

466

**Last Modified Date**

2024-09-06

**IP Status**

No known IP claims.

**Extension and Version Dependencies**

[OpenXR 1.0](https://registry.khronos.org/OpenXR/specs/1.0/man/html/openxr.html)

**Contributors**

Dmitry Kotov, Google

Levana Chen, Google

Jared Finder, Google

Spencer Quin, Google

## Overview

This extension provides APIs to enumerate and query various performance metrics
counters of the current XR device, compositor and XR application. Developers
**can** perform performance analysis and do targeted optimization to the XR
application using the performance metrics counters being collected. The
application **should** not change its behavior based on the counter reads.

The performance metrics counters are organized into predefined
[`XrPath`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrPath) values, under the root path
*/perfmetrics_android*. An
application **can** query the available counters through
[xrEnumeratePerformanceMetricsCounterPathsANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_performance_metrics#xrEnumeratePerformanceMetricsCounterPathsANDROID). Here is a list of the
performance metrics counter paths that **may** be provided on Android devices:

- */perfmetrics_android/app/cpu_frametime* (milliseconds, float) - wallclock time client spent to process a frame.
- */perfmetrics_android/app/gpu_frametime* (milliseconds, float) - wallclock time client spent waiting for GPU work to complete per frame. Notes:
  - A high wait time **can** mean that the GPU was busy with other tasks, not necessarily that this client is doing too much GPU work.
  - The GPU wait time **can** be zero if rendering was already complete when checked by the compositor.
- */perfmetrics_android/app/cpu_utilization* (percentage, float) - total app CPU utilization rate averaged over time.
  - It **can** be higher than 100% on multi-core processors.
- */perfmetrics_android/app/gpu_utilization* (percentage) - app total GPU utilization rate averaged over time.
- */perfmetrics_android/app/motion_to_photon_latency* (milliseconds, float) - time spent from user-initiated motion event to corresponding physical image update on the display.
- */perfmetrics_android/compositor/cpu_frametime* (milliseconds, float) - wallclock time compositor spent to process a frame.
- */perfmetrics_android/compositor/gpu_frametime* (milliseconds, float) - wallclock time compositor spent waiting for GPU work to complete per frame.
- */perfmetrics_android/compositor/dropped_frame_count* (integer) - total number of dropped frames from all apps.
- */perfmetrics_android/compositor/frames_per_second* (float) - number of compositor frames drawn on device per second.
- */perfmetrics_android/device/cpu_utilization_average* (percentage, float) - device CPU utilization rate averaged across all cores and averaged over time.
- */perfmetrics_android/device/cpu_utilization_worst* (percentage, float) - device CPU utilization rate of worst performing core averaged over time.
- */perfmetrics_android/device/cpu0_utilization* through */perfmetrics_android/device/cpuX_utilization* (percentage, float, X is the number of CPU cores minus one) - device CPU utilization rate per CPU core averaged over time.
- */perfmetrics_android/device/cpu_frequency* (MHz, float) - device CPU frequency averaged across all cores and averaged over time.
- */perfmetrics_android/device/gpu_utilization* (percentage, float) - device GPU utilization rate averaged over time.

After a session is created, an application **can** use
[xrSetPerformanceMetricsStateANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_performance_metrics#xrSetPerformanceMetricsStateANDROID) to enable the performance metrics
system for that session. An application **can** use
[xrQueryPerformanceMetricsCounterANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_performance_metrics#xrQueryPerformanceMetricsCounterANDROID) to query a performance metrics
counter on a session that has the performance metrics system enabled, or use
[xrGetPerformanceMetricsStateANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_performance_metrics#xrGetPerformanceMetricsStateANDROID) to query if the performance metrics
system is enabled.

> [!NOTE]
> **Note:** the measurement intervals of individual performance metrics counters are defined by the OpenXR runtime. The application **should** not make assumptions or change its behavior at runtime by measuring them.

In order to enable the functionality of this extension, the application
**should** pass the name of the extension into [xrCreateInstance](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateInstance)
using the [XrInstanceCreateInfo::enabledExtensionNames](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrInstanceCreateInfo) parameter
as indicated in the [Extensions](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-extensions) section.

### New Flag Types

    typedef XrFlags64 XrPerformanceMetricsCounterFlagsANDROID;

    // Flag bits for XrPerformanceMetricsCounterFlagsANDROID
    static const XrPerformanceMetricsCounterFlagsANDROID XR_PERFORMANCE_METRICS_COUNTER_ANY_VALUE_VALID_BIT_ANDROID = 0x00000001;
    static const XrPerformanceMetricsCounterFlagsANDROID XR_PERFORMANCE_METRICS_COUNTER_UINT_VALUE_VALID_BIT_ANDROID = 0x00000002;
    static const XrPerformanceMetricsCounterFlagsANDROID XR_PERFORMANCE_METRICS_COUNTER_FLOAT_VALUE_VALID_BIT_ANDROID = 0x00000004;

### New Enum Constants

[XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) enumeration is extended with:

- `XR_TYPE_PERFORMANCE_METRICS_STATE_ANDROID`
- `XR_TYPE_PERFORMANCE_METRICS_COUNTER_ANDROID`

### New Enums

    typedef enum XrPerformanceMetricsCounterUnitANDROID {
        XR_PERFORMANCE_METRICS_COUNTER_UNIT_GENERIC_ANDROID = 0,
        XR_PERFORMANCE_METRICS_COUNTER_UNIT_PERCENTAGE_ANDROID = 1,
        XR_PERFORMANCE_METRICS_COUNTER_UNIT_MILLISECONDS_ANDROID = 2,
        XR_PERFORMANCE_METRICS_COUNTER_UNIT_BYTES_ANDROID = 3,
        XR_PERFORMANCE_METRICS_COUNTER_UNIT_HERTZ_ANDROID = 4
    } XrPerformanceMetricsCounterUnitANDROID;

### New Structures

The [XrPerformanceMetricsStateANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_performance_metrics#XrPerformanceMetricsStateANDROID) structure is defined
as:

    typedef struct XrPerformanceMetricsStateANDROID {
        XrStructureType    type;
        void*              next;
        XrBool32           enabled;
    } XrPerformanceMetricsStateANDROID;

#### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.
- `enabled` is set to `XR_TRUE` to indicate the performance metrics system is enabled, `XR_FALSE` otherwise, when getting state. When setting state, set to `XR_TRUE` to enable the performance metrics system and `XR_FALSE` to disable it.

[XrPerformanceMetricsStateANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_performance_metrics#XrPerformanceMetricsStateANDROID) is provided as input when calling
[xrSetPerformanceMetricsStateANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_performance_metrics#xrSetPerformanceMetricsStateANDROID) to enable or disable the performance
metrics system. [XrPerformanceMetricsStateANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_performance_metrics#XrPerformanceMetricsStateANDROID) is populated as an output
parameter when calling [xrGetPerformanceMetricsStateANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_performance_metrics#xrGetPerformanceMetricsStateANDROID) to query if the
performance metrics system is enabled.

#### Valid Usage (Implicit)

- The `XR_ANDROID_performance_metrics` extension **must** be enabled prior to using [XrPerformanceMetricsStateANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_performance_metrics#XrPerformanceMetricsStateANDROID)
- `type` **must** be `XR_TYPE_PERFORMANCE_METRICS_STATE_ANDROID`
- `next` **must** be `NULL` or a valid pointer to the next structure in a structure chain

The [XrPerformanceMetricsCounterANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_performance_metrics#XrPerformanceMetricsCounterANDROID) structure is defined
as:

    typedef struct XrPerformanceMetricsCounterANDROID {
        XrStructureType                            type;
        void*                                      next;
        XrPerformanceMetricsCounterFlagsANDROID    counterFlags;
        XrPerformanceMetricsCounterUnitANDROID     counterUnit;
        uint32_t                                   uintValue;
        float                                      floatValue;
    } XrPerformanceMetricsCounterANDROID;

#### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.
- `counterFlags` is a bitmask of [XrPerformanceMetricsCounterFlagsANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_performance_metrics#XrPerformanceMetricsCounterFlagsANDROID) describing the validity of value members.
- `counterUnit` is an enum of [XrPerformanceMetricsCounterUnitANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_performance_metrics#XrPerformanceMetricsCounterUnitANDROID) describing the measurement unit.
- `uintValue` is the counter value in `uint32_t` format. It is valid if `counterFlags` contains `XR_PERFORMANCE_METRICS_COUNTER_UINT_VALUE_VALID_BIT_ANDROID`.
- `floatValue` is the counter value in `float` format. It is valid if `counterFlags` contains `XR_PERFORMANCE_METRICS_COUNTER_FLOAT_VALUE_VALID_BIT_ANDROID`.

[XrPerformanceMetricsCounterANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_performance_metrics#XrPerformanceMetricsCounterANDROID) is populated by calling
[xrQueryPerformanceMetricsCounterANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_performance_metrics#xrQueryPerformanceMetricsCounterANDROID) to query real-time performance
metrics counter information.

#### Valid Usage (Implicit)

- The `XR_ANDROID_performance_metrics` extension **must** be enabled prior to using [XrPerformanceMetricsCounterANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_performance_metrics#XrPerformanceMetricsCounterANDROID)
- `type` **must** be `XR_TYPE_PERFORMANCE_METRICS_COUNTER_ANDROID`
- `next` **must** be `NULL` or a valid pointer to the next structure in a structure chain
- `counterFlags` **must** be 0 or a valid combination of [XrPerformanceMetricsCounterFlagsANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_performance_metrics#XrPerformanceMetricsCounterFlagsANDROID) values
- `counterUnit` **must** be a valid [XrPerformanceMetricsCounterUnitANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_performance_metrics#XrPerformanceMetricsCounterUnitANDROID) value

### New Functions

The [xrEnumeratePerformanceMetricsCounterPathsANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_performance_metrics#xrEnumeratePerformanceMetricsCounterPathsANDROID) function enumerates
all performance metrics counter paths that are supported by the runtime, it is
defined as:

    XrResult xrEnumeratePerformanceMetricsCounterPathsANDROID(
        XrInstance                                  instance,
        uint32_t                                    counterPathCapacityInput,
        uint32_t*                                   counterPathCountOutput,
        XrPath*                                     counterPaths);

#### Parameter Descriptions

- `instance` is an [XrInstance](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrInstance) handle previously created with [xrCreateInstance](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateInstance).
- `counterPathCapacityInput` is the capacity of the `counterPaths` array, or 0 to indicate a request to retrieve the required capacity.
- `counterPathCountOutput` is filled in by the runtime with the count of `counterPaths` written or the required capacity in the case that `counterPathCapacityInput` is insufficient.
- `counterPaths` is an array of [`XrPath`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrPath) filled in by the runtime which contains all the available performance metrics counters, but **can** be `NULL` if `counterPathCapacityInput` is 0.
- See the [Buffer Size Parameters](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-buffer-size-parameters) section for a detailed description of retrieving the required `counterPaths` size.

#### Valid Usage (Implicit)

- The `XR_ANDROID_performance_metrics` extension **must** be enabled prior to calling [xrEnumeratePerformanceMetricsCounterPathsANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_performance_metrics#xrEnumeratePerformanceMetricsCounterPathsANDROID)
- `instance` **must** be a valid [XrInstance](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrInstance) handle
- `counterPathCountOutput` **must** be a pointer to a `uint32_t` value
- If `counterPathCapacityInput` is not 0, `counterPaths` **must** be a pointer to an array of `counterPathCapacityInput` [`XrPath`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrPath) values

#### Return Codes

[**Success**](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`

[**Failure**](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_VALIDATION_FAILURE`
- `XR_ERROR_RUNTIME_FAILURE`
- `XR_ERROR_HANDLE_INVALID`
- `XR_ERROR_INSTANCE_LOST`
- `XR_ERROR_SIZE_INSUFFICIENT`

The [xrSetPerformanceMetricsStateANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_performance_metrics#xrSetPerformanceMetricsStateANDROID) function is defined
as:

    XrResult xrSetPerformanceMetricsStateANDROID(
        XrSession                                   session,
        const XrPerformanceMetricsStateANDROID*     state);

#### Parameter Descriptions

- `session` is an [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) handle previously created with [xrCreateSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateSession).
- `state` is a pointer to an [XrPerformanceMetricsStateANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_performance_metrics#XrPerformanceMetricsStateANDROID) structure.

The [xrSetPerformanceMetricsStateANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_performance_metrics#xrSetPerformanceMetricsStateANDROID) function enables or disables the
performance metrics system.

#### Valid Usage (Implicit)

- The `XR_ANDROID_performance_metrics` extension **must** be enabled prior to calling [xrSetPerformanceMetricsStateANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_performance_metrics#xrSetPerformanceMetricsStateANDROID)
- `session` **must** be a valid [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) handle
- `state` **must** be a pointer to a valid [XrPerformanceMetricsStateANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_performance_metrics#XrPerformanceMetricsStateANDROID) structure

#### Return Codes

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

The [xrGetPerformanceMetricsStateANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_performance_metrics#xrGetPerformanceMetricsStateANDROID) function is defined
as:

    XrResult xrGetPerformanceMetricsStateANDROID(
        XrSession                                   session,
        XrPerformanceMetricsStateANDROID*           state);

#### Parameter Descriptions

- `session` is an [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) handle previously created with [xrCreateSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateSession).
- `state` is a pointer to an [XrPerformanceMetricsStateANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_performance_metrics#XrPerformanceMetricsStateANDROID) structure.

The [xrGetPerformanceMetricsStateANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_performance_metrics#xrGetPerformanceMetricsStateANDROID) function gets the
current state of the performance metrics system.

#### Valid Usage (Implicit)

- The `XR_ANDROID_performance_metrics` extension **must** be enabled prior to calling [xrGetPerformanceMetricsStateANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_performance_metrics#xrGetPerformanceMetricsStateANDROID)
- `session` **must** be a valid [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) handle
- `state` **must** be a pointer to an [XrPerformanceMetricsStateANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_performance_metrics#XrPerformanceMetricsStateANDROID) structure

#### Return Codes

[**Success**](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`
- `XR_SESSION_LOSS_PENDING`

[**Failure**](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_VALIDATION_FAILURE`
- `XR_ERROR_HANDLE_INVALID`
- `XR_ERROR_INSTANCE_LOST`
- `XR_ERROR_SESSION_LOST`

The [xrQueryPerformanceMetricsCounterANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_performance_metrics#xrQueryPerformanceMetricsCounterANDROID) function is
defined as:

    XrResult xrQueryPerformanceMetricsCounterANDROID(
        XrSession                                   session,
        XrPath                                      counterPath,
        XrPerformanceMetricsCounterANDROID*         counter);

#### Parameter Descriptions

- `session` is an [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) handle previously created with [xrCreateSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateSession).
- `counterPath` is a valid performance metrics counter path.
- `counter` is a pointer to an [XrPerformanceMetricsCounterANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_performance_metrics#XrPerformanceMetricsCounterANDROID) structure.

The [xrQueryPerformanceMetricsCounterANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_performance_metrics#xrQueryPerformanceMetricsCounterANDROID) function queries a
performance metrics counter.

The application **should** enable the performance metrics system by calling
[xrSetPerformanceMetricsStateANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_performance_metrics#xrSetPerformanceMetricsStateANDROID) before querying metrics using
[xrQueryPerformanceMetricsCounterANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_performance_metrics#xrQueryPerformanceMetricsCounterANDROID).

#### Valid Usage (Implicit)

- The `XR_ANDROID_performance_metrics` extension **must** be enabled prior to calling [xrQueryPerformanceMetricsCounterANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_performance_metrics#xrQueryPerformanceMetricsCounterANDROID)
- `session` **must** be a valid [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) handle
- `counter` **must** be a pointer to an [XrPerformanceMetricsCounterANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_performance_metrics#XrPerformanceMetricsCounterANDROID) structure

#### Return Codes

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
- `XR_ERROR_PATH_UNSUPPORTED`
- `XR_ERROR_PATH_INVALID`

*** ** * ** ***

OpenXR™ and the OpenXR logo are trademarks owned
by The Khronos Group Inc. and are registered as a trademark in China,
the European Union, Japan and the United Kingdom.