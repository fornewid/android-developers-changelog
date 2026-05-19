---
title: https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_face_tracking_data_source
url: https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_face_tracking_data_source
source: md.txt
---

### XR_ANDROID_face_tracking_data_source

**Name String**

`XR_ANDROID_face_tracking_data_source`

**Extension Type**

Instance extension

**Registered Extension Number**

707

**Revision**

1

**Ratification Status**

Not ratified

**Extension and Version Dependencies**

`XR_ANDROID_face_tracking`

**Last Modified Date**

2025-12-16

**IP Status**

No known IP claims.

**Contributors**

Kenny Vercaemer, Google  

Yinglei Zhang, Google  

Nihav Jain, Google  

Spencer Quin, Google

## Overview

This extension enables applications to get face tracking data from multiple data sources.

## Query supported data sources

Applications **should** call [xrEnumerateFaceTrackingDataSourcesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_face_tracking_data_source#xrEnumerateFaceTrackingDataSourcesANDROID) to get the list of supported face tracking data sources.

The [xrEnumerateFaceTrackingDataSourcesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_face_tracking_data_source#xrEnumerateFaceTrackingDataSourcesANDROID) function is defined as:

    XrResult                                                                                 xrEnumerateFaceTrackingDataSourcesANDROID(
        XrInstance                                  instance,
        XrSystemId                                  systemId,
        uint32_t                                    supportedDataSourcesInputCapacity,
        uint32_t*                                   supportedDataSourcesOutputCount,
        XrFaceTrackingDataSourceANDROID*            supportedDataSources);

### Parameter Descriptions

- `instance` is a handle to an [XrInstance](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrInstance) .
- `systemId` is the `XrSystemId` for which the face tracking data sources will be enumerated.
- `supportedDataSourcesInputCapacity` is the capacity of the `supportedDataSources` array, or 0 to indicate a request to retrieve the required capacity.
- `supportedDataSourcesOutputCount` is the number of supported data sources, or the required capacity in the case that `supportedDataSourcesInputCapacity` is insufficient.
- `supportedDataSources` is an array of [XrFaceTrackingDataSourceANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_face_tracking_data_source#XrFaceTrackingDataSourceANDROID) . It **can** be `NULL` if `supportedDataSourcesInputCapacity` is 0.
- See the [Buffer Size Parameters](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-buffer-size-parameters) section for a detailed description of retrieving the required `supportedDataSources` size.

The application **can** enumerate the list of data sources supported by the system by calling the [xrEnumerateFaceTrackingDataSourcesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_face_tracking_data_source#xrEnumerateFaceTrackingDataSourcesANDROID) function.

If [XrSystemFaceTrackingPropertiesANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSystemFaceTrackingPropertiesANDROID) :: `supportsFaceTracking` is `XR_TRUE` then the runtime **must** also return `XR_FACE_TRACKING_DATA_SOURCE_IMAGE_ANDROID` from [xrEnumerateFaceTrackingDataSourcesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_face_tracking_data_source#xrEnumerateFaceTrackingDataSourcesANDROID) .

If the runtime returns zero data sources, then it does not support any kind of face tracking.

The runtime **must** return the data sources in order of highest quality to lowest quality.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_face_tracking_data_source#VUID-xrEnumerateFaceTrackingDataSourcesANDROID-extension-notenabled) The `XR_ANDROID_face_tracking_data_source` extension **must** be enabled prior to calling [xrEnumerateFaceTrackingDataSourcesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_face_tracking_data_source#xrEnumerateFaceTrackingDataSourcesANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_face_tracking_data_source#VUID-xrEnumerateFaceTrackingDataSourcesANDROID-instance-parameter) `instance` **must** be a valid [XrInstance](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrInstance) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_face_tracking_data_source#VUID-xrEnumerateFaceTrackingDataSourcesANDROID-supportedDataSourcesOutputCount-parameter) `supportedDataSourcesOutputCount` **must** be a pointer to a `uint32_t` value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_face_tracking_data_source#VUID-xrEnumerateFaceTrackingDataSourcesANDROID-supportedDataSources-parameter) If `supportedDataSourcesInputCapacity` is not `0` , `supportedDataSources` **must** be a pointer to an array of `supportedDataSourcesInputCapacity` [XrFaceTrackingDataSourceANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_face_tracking_data_source#XrFaceTrackingDataSourceANDROID) values

### Return Codes

[Success](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`

[Failure](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FEATURE_UNSUPPORTED`
- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_HANDLE_INVALID`
- `XR_ERROR_INSTANCE_LOST`
- `XR_ERROR_RUNTIME_FAILURE`
- `XR_ERROR_SYSTEM_INVALID`
- `XR_ERROR_VALIDATION_FAILURE`

The [XrFaceTrackingDataSourceANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_face_tracking_data_source#XrFaceTrackingDataSourceANDROID) enumeration identifies the different data sources that a runtime **may** support.

    typedef enum XrFaceTrackingDataSourceANDROID {
        XR_FACE_TRACKING_DATA_SOURCE_IMAGE_ANDROID = 1,
        XR_FACE_TRACKING_DATA_SOURCE_AUDIO_ANDROID = 2,
        XR_FACE_TRACKING_DATA_SOURCE_MULTIMODAL_ANDROID = 3,
        XR_FACE_TRACKING_DATA_SOURCE_MAX_ENUM_ANDROID = 0x7FFFFFFF
    } XrFaceTrackingDataSourceANDROID;

The enumerants have the following meanings:

Enum Description

`XR_FACE_TRACKING_DATA_SOURCE_IMAGE_ANDROID`

Indicates that this config uses image data

`XR_FACE_TRACKING_DATA_SOURCE_AUDIO_ANDROID`

Indicates that this config uses audio data

`XR_FACE_TRACKING_DATA_SOURCE_MULTIMODAL_ANDROID`

Indicates that this config uses image and audio data

## Configuring data sources

The [XrFaceTrackingDataSourceInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_face_tracking_data_source#XrFaceTrackingDataSourceInfoANDROID) structure is described as follows:

    typedef struct XrFaceTrackingDataSourceInfoANDROID {
        XrStructureType                           type;
        const void*                               next;
        uint32_t                                  requestedDataSourceCount;
        const XrFaceTrackingDataSourceANDROID*    requestedDataSources;
    } XrFaceTrackingDataSourceInfoANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.
- `requestedDataSourceCount` is the number of data sources requested by the application.
- `requestedDataSources` is an array of [XrFaceTrackingDataSourceANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_face_tracking_data_source#XrFaceTrackingDataSourceANDROID) values, specifying the data sources requested by the application.

The [XrFaceTrackingDataSourceInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_face_tracking_data_source#XrFaceTrackingDataSourceInfoANDROID) structure describes the data sources to create an [XrFaceTrackerANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrFaceTrackerANDROID) handle.

An application **may** pass a [XrFaceTrackingDataSourceInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_face_tracking_data_source#XrFaceTrackingDataSourceInfoANDROID) structure in the next chain of a [XrFaceTrackerCreateInfoANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrFaceTrackerCreateInfoANDROID) structure to request one or more data sources for face tracking when calling [xrCreateFaceTrackerANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateFaceTrackerANDROID) .

If the application passes zero data sources, or any of the data sources were not enumerated by [xrEnumerateFaceTrackingDataSourcesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_face_tracking_data_source#xrEnumerateFaceTrackingDataSourcesANDROID) , then the runtime **must** return `XR_ERROR_VALIDATION_FAILURE` .

If the user has not have granted all the required permissions for all of the requested data sources, then the runtime **must** return `XR_ERROR_PERMISSION_INSUFFICIENT` .

The required permissions for each data source are defined as follows:

- `XR_FACE_TRACKING_DATA_SOURCE_IMAGE_ANDROID` requires the android.permission.FACE_TRACKING permission.
- `XR_FACE_TRACKING_DATA_SOURCE_AUDIO_ANDROID` requires the android.permission.RECORD_AUDIO permission.
- `XR_FACE_TRACKING_DATA_SOURCE_MULTIMODAL_ANDROID` requires both android.permission.FACE_TRACKING and android.permission.RECORD_AUDIO permissions.

The runtime **must** interpret the [XrFaceTrackingDataSourceInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_face_tracking_data_source#XrFaceTrackingDataSourceInfoANDROID) : `requestedDataSources` array as highest preference to lowest preference by the application. The runtime **must** produce tracking data using the first requested data source that still complies with the required permissions. If a permission is revoked during the tracker lifetime, causing a data source to be no longer usable, the runtime **must** continue attempting to use the next highest preference data source. If none of the requested data sources are usable, the runtime **must** set [XrFaceStateANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrFaceStateANDROID) :: `isValid` to `XR_FALSE` in calls to [xrGetFaceStateANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrGetFaceStateANDROID) and other fields are considered undefined.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_face_tracking_data_source#VUID-XrFaceTrackingDataSourceInfoANDROID-extension-notenabled) The `XR_ANDROID_face_tracking_data_source` extension **must** be enabled prior to using [XrFaceTrackingDataSourceInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_face_tracking_data_source#XrFaceTrackingDataSourceInfoANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_face_tracking_data_source#VUID-XrFaceTrackingDataSourceInfoANDROID-type-type) `type` **must** be `XR_TYPE_FACE_TRACKING_DATA_SOURCE_INFO_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_face_tracking_data_source#VUID-XrFaceTrackingDataSourceInfoANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_face_tracking_data_source#VUID-XrFaceTrackingDataSourceInfoANDROID-requestedDataSources-parameter) `requestedDataSources` **must** be a pointer to an array of `requestedDataSourceCount` valid [XrFaceTrackingDataSourceANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_face_tracking_data_source#XrFaceTrackingDataSourceANDROID) values
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_face_tracking_data_source#VUID-XrFaceTrackingDataSourceInfoANDROID-requestedDataSourceCount-arraylength) The `requestedDataSourceCount` parameter **must** be greater than `0`

### Permissions

Android applications **must** have the permissions they intend to request listed in their manifest. The android.permission.FACE_TRACKING permission is considered a dangerous permission. The android.permission.RECORD_AUDIO permission is considered a dangerous permission. The application **must** request the permissions at runtime to use these functions:

- [xrCreateFaceTrackerANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateFaceTrackerANDROID)

(protection level: dangerous)

The [XrFaceTrackingDataSourceStateANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_face_tracking_data_source#XrFaceTrackingDataSourceStateANDROID) structure is described as follows:

    typedef struct XrFaceTrackingDataSourceStateANDROID {
        XrStructureType                    type;
        void*                              next;
        XrFaceTrackingDataSourceANDROID    dataSource;
    } XrFaceTrackingDataSourceStateANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.
- `dataSource` is the [XrFaceTrackingDataSourceANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_face_tracking_data_source#XrFaceTrackingDataSourceANDROID) used to produce the face tracking data.

An application **may** chain a [XrFaceTrackingDataSourceStateANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_face_tracking_data_source#XrFaceTrackingDataSourceStateANDROID) structure to a [XrFaceStateANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrFaceStateANDROID) structure passed to [xrGetFaceStateANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrGetFaceStateANDROID) to query the data source used to produce the face tracking data for that call.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_face_tracking_data_source#VUID-XrFaceTrackingDataSourceStateANDROID-extension-notenabled) The `XR_ANDROID_face_tracking_data_source` extension **must** be enabled prior to using [XrFaceTrackingDataSourceStateANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_face_tracking_data_source#XrFaceTrackingDataSourceStateANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_face_tracking_data_source#VUID-XrFaceTrackingDataSourceStateANDROID-type-type) `type` **must** be `XR_TYPE_FACE_TRACKING_DATA_SOURCE_STATE_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_face_tracking_data_source#VUID-XrFaceTrackingDataSourceStateANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_face_tracking_data_source#VUID-XrFaceTrackingDataSourceStateANDROID-dataSource-parameter) `dataSource` **must** be a valid [XrFaceTrackingDataSourceANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_face_tracking_data_source#XrFaceTrackingDataSourceANDROID) value

## Example code for face tracking with data source.

    XrInstance instance; // previously initialized
    XrSystemId systemId; // previously initialized
    XrSession session; // previously initialized, e.g. created at app startup.

    // The function pointers are previously initialized using xrGetInstanceProcAddr.
    PFN_xrCreateFaceTrackerANDROID xrCreateFaceTrackerANDROID; // previously initialized
    PFN_xrDestroyFaceTrackerANDROID xrDestroyFaceTrackerANDROID; // previously initialized
    PFN_xrGetFaceStateANDROID xrGetFaceStateANDROID; // previously initialized
    PFN_xrEnumerateFaceTrackingDataSourcesANDROID xrEnumerateFaceTrackingDataSourcesANDROID; // previously initialized
    bool (*requestPermission)(const char* permission);

    // Inspect data sources supported by the system.
    uint32_t dataSourcesCount = 0;
    CHK_XR(xrEnumerateFaceTrackingDataSourcesANDROID(instance, systemId, dataSourcesCount,
           &dataSourcesCount, nullptr));
    std::vector<XrFaceTrackingDataSourceANDROID> dataSources(dataSourcesCount);
    CHK_XR(xrEnumerateFaceTrackingDataSourcesANDROID(instance, systemId, dataSourcesCount,
           &dataSourcesCount, dataSources.data()));

    if (dataSources.size() == 0) {
      // System does not support face tracking at all ...
      return;
    }

    auto requestDataSourcePermissions = [requestPermission](XrFaceTrackingDataSourceANDROID dataSource) {
      switch (dataSource) {
        case XR_FACE_TRACKING_DATA_SOURCE_IMAGE_ANDROID:
          return requestPermission("android.permission.FACE_TRACKING");
        case XR_FACE_TRACKING_DATA_SOURCE_AUDIO_ANDROID:
          return requestPermission("android.permission.RECORD_AUDIO");
        case XR_FACE_TRACKING_DATA_SOURCE_MULTIMODAL_ANDROID:
          return requestPermission("android.permission.FACE_TRACKING") &&
                 requestPermission("android.permission.RECORD_AUDIO");
        default:
          return false;
      }
    };

    // Request permissions and remove data sources that are not granted.
    for (uint32_t i = 0; i < dataSources.size();) {
      if (requestDataSourcePermissions(dataSources[i])) {
        ++i;
        continue;
      }

      dataSources.erase(dataSources.begin() + i);
    }

    if (dataSources.size() == 0) {
      // User denied all permissions, cannot create face tracker.
      return;
    }

    // Create face tracker with requested data sources.
    XrFaceTrackerANDROID faceTracker;
    XrFaceTrackingDataSourceInfoANDROID
            faceTrackerModeInfo{.type = XR_TYPE_FACE_TRACKING_DATA_SOURCE_INFO_ANDROID,
                           .next = nullptr,
                           .requestedDataSourceCount = static_cast<uint32_t>(
                               dataSources.size()),
                           .requestedDataSources = dataSources.data()};
    XrFaceTrackerCreateInfoANDROID
            createInfo{.type = XR_TYPE_FACE_TRACKER_CREATE_INFO_ANDROID,
                        .next = &faceTrackerModeInfo};
    CHK_XR(xrCreateFaceTrackerANDROID(session, &createInfo, &faceTracker));

    XrFaceTrackingDataSourceStateANDROID dataSourceState{
      .type = XR_TYPE_FACE_TRACKING_DATA_SOURCE_STATE_ANDROID,
      .next = nullptr};
    XrFaceStateANDROID faceState;
    float faceExpressionParameters[XR_FACE_PARAMETER_COUNT_ANDROID];
    faceState.type = XR_TYPE_FACE_STATE_ANDROID;
    faceState.next = &dataSourceState;
    faceState.parametersCapacityInput = XR_FACE_PARAMETER_COUNT_ANDROID;
    faceState.parameters = faceExpressionParameters;

    while (1) {
        // ...
        // For every frame in the frame loop
        // ...
        XrFrameState frameState; // previously returned from xrWaitFrame

        XrFaceStateGetInfoANDROID faceGetInfo{
                .type = XR_TYPE_FACE_STATE_GET_INFO_ANDROID,
                .next = nullptr,
                .time = frameState.predictedDisplayTime,
        };

        CHK_XR(xrGetFaceStateANDROID(faceTracker, &faceGetInfo, &faceState));
        if (faceState.isValid) {
            for (uint32_t i = 0; i < XR_FACE_PARAMETER_COUNT_ANDROID; ++i) {
                // parameters[i] contains a weight of specific blend shape
            }

            // If the system changes data source because of permission changes,
            // handle the new data source ...
            switch (dataSourceState.dataSource) {
              default:
                break;
            }
        }
    }

    // after usage
    CHK_XR(xrDestroyFaceTrackerANDROID(faceTracker));

**Issues**

**Version History**

- Revision 1, 2024-10-07 (Kenny Vercaemer)

  - Initial extension description