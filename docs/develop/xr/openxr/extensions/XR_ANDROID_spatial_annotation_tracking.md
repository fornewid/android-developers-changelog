---
title: https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking
url: https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking
source: md.txt
---

### XR_ANDROID_spatial_annotation_tracking

**Name String**

`XR_ANDROID_spatial_annotation_tracking`

**Extension Type**

Instance extension

**Registered Extension Number**

795

**Revision**

1

**Ratification Status**

Not ratified

**Extension and Version Dependencies**

`XR_EXT_spatial_entity`  

and  

`XR_EXT_spatial_image_tracking`

**Last Modified Date**

2026-01-12

**IP Status**

No known IP claims.

**Contributors**

Levana Chen, Google  

Christopher Feil, Google  

Martin Sundermeyer, Google  

David Joseph Tan, Google  

Jared Finder, Google  

Nihav Jain, Google

## Overview

This extension provides the annotation tracking capability for the [XR_EXT_spatial_entity](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_spatial_entity) extension to tracking various annotations in the scene. It enables applications to put overlays on physical or virtual objects defined by runtime references.

This extension provides a basic annotation type "Quad", which is a polygon that has exactly 4 sides, i.e. convex quadrilateral, representing a generalized 2D bounding box within a runtime reference. A tracked quad annotation is represented as a spatial entity with (or "that has") the following components:

- `XR_SPATIAL_COMPONENT_TYPE_ANNOTATION_QUAD_ANDROID`

Applications **can** typically use the spatial annotation tracking extension in the following patterns:

- An application first creates a handle of [XrSpatialReferenceCacheANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialReferenceCacheANDROID) which starts recording runtime references from the given source.
- The application then captures a runtime reference of [XrSpatialReferenceImageEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialReferenceImageEXT) and defines a desired annotation within the reference during the timespan of the reference cache.
- The application then creates an [XrSpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextEXT) handle based on the [XrSpatialReferenceImageEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialReferenceImageEXT) given by [XrSpatialCapabilityConfigurationAnnotationTrackingANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialCapabilityConfigurationAnnotationTrackingANDROID) .
- The application **can** destroy the [XrSpatialReferenceCacheANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialReferenceCacheANDROID) handle to stop recording runtime references to reduce memory usage, or wait for `XR_TYPE_EVENT_DATA_SPATIAL_ANNOTATION_TRACKING_ANDROID` event to confirm the initialization result.
- The application then pulls for the `XR_TYPE_EVENT_DATA_SPATIAL_ANNOTATION_TRACKING_ANDROID` event to confirm the initialization result of the annotation.
- If the initialization is successful, the application **can** then pull for the `XR_TYPE_EVENT_DATA_SPATIAL_DISCOVERY_RECOMMENDED_EXT` event to track the annotation.
- If the initialization fails, the application **can** use the error code returned in the event to determine the failure reason, and destroy existing [XrSpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextEXT) handle to start a new annotation.
- Regardless of the initialization result, the application **can** release image buffer to reduce memory usage after receiving the event.
- The application discovers and queries annotations according to the spatial entity access patterns.
- The application **can** create additional [XrSpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextEXT) handle to track annotations within a new reference during the timespan of a valid [XrSpatialReferenceCacheANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialReferenceCacheANDROID) .
- The application **can** destroy [XrSpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextEXT) handles to reduce the set of detectable and trackable annotations dynamically at runtime.

## Runtime Support

A runtime **must** advertise its support for the annotation tracking capability using [xrEnumerateSpatialCapabilitiesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrEnumerateSpatialCapabilitiesEXT) by listing the following capability:

- `XR_SPATIAL_CAPABILITY_ANNOTATION_TRACKING_ANDROID`

When the runtime supports the annotation tracking capability:

- It **must** support at least one annotation component, by listing the supported annotation components via [xrEnumerateSpatialCapabilityComponentTypesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrEnumerateSpatialCapabilityComponentTypesEXT) .
- It **must** support at least one of [XrSpatialReferenceImageFormatEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialReferenceImageFormatEXT) , by listing the supported reference formats via [xrEnumerateSpatialReferenceImageFormatsEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrEnumerateSpatialReferenceImageFormatsEXT) with `capability` setting to `XR_SPATIAL_CAPABILITY_ANNOTATION_TRACKING_ANDROID` .
- It **must** support at least one of [XrSpatialAnnotationReferenceSourceANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialAnnotationReferenceSourceANDROID) , by listing the supported reference sources via [xrEnumerateSpatialAnnotationReferenceSourcesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#xrEnumerateSpatialAnnotationReferenceSourcesANDROID) with `capability` setting to `XR_SPATIAL_CAPABILITY_ANNOTATION_TRACKING_ANDROID` .

The [xrEnumerateSpatialAnnotationReferenceSourcesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#xrEnumerateSpatialAnnotationReferenceSourcesANDROID) function is defined as:

    XrResult xrEnumerateSpatialAnnotationReferenceSourcesANDROID(
        XrInstance                                  instance,
        XrSystemId                                  systemId,
        XrSpatialCapabilityEXT                      capability,
        uint32_t                                    sourceCapacityInput,
        uint32_t*                                   sourceCountOutput,
        XrSpatialAnnotationReferenceSourceANDROID*  sources);

### Parameter Descriptions

- `instance` is a handle to an [XrInstance](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrInstance) .
- `systemId` is the `XrSystemId` whose reference sources will be enumerated.
- `capability` is the [XrSpatialCapabilityEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityEXT) for which the reference sources will be enumerated.
- `sourceCapacityInput` is the capacity of the `sources` array, or 0 to indicate a request to retrieve the required capacity.
- `sourceCountOutput` is the number of sources, or the required capacity in the case that `sourceCapacityInput` is insufficient.
- `sources` is an array of [XrSpatialAnnotationReferenceSourceANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialAnnotationReferenceSourceANDROID) . It **can** be `NULL` if `sourceCapacityInput` is 0.
- See the [Buffer Size Parameters](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-buffer-size-parameters) section for a detailed description of retrieving the required `sources` size.

The application **can** enumerate the list of reference sources supported by a given `XrSystemId` using [xrEnumerateSpatialAnnotationReferenceSourcesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#xrEnumerateSpatialAnnotationReferenceSourcesANDROID) .

The runtime **must** not enumerate the reference sources whose extension is not enabled for `instance` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#VUID-xrEnumerateSpatialAnnotationReferenceSourcesANDROID-extension-notenabled) The `XR_ANDROID_spatial_annotation_tracking` extension **must** be enabled prior to calling [xrEnumerateSpatialAnnotationReferenceSourcesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#xrEnumerateSpatialAnnotationReferenceSourcesANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#VUID-xrEnumerateSpatialAnnotationReferenceSourcesANDROID-instance-parameter) `instance` **must** be a valid [XrInstance](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrInstance) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#VUID-xrEnumerateSpatialAnnotationReferenceSourcesANDROID-capability-parameter) `capability` **must** be a valid [XrSpatialCapabilityEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityEXT) value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#VUID-xrEnumerateSpatialAnnotationReferenceSourcesANDROID-sourceCountOutput-parameter) `sourceCountOutput` **must** be a pointer to a `uint32_t` value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#VUID-xrEnumerateSpatialAnnotationReferenceSourcesANDROID-sources-parameter) If `sourceCapacityInput` is not `0` , `sources` **must** be a pointer to an array of `sourceCapacityInput` [XrSpatialAnnotationReferenceSourceANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialAnnotationReferenceSourceANDROID) values

### Return Codes

[Success](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`

[Failure](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_HANDLE_INVALID`
- `XR_ERROR_INSTANCE_LOST`
- `XR_ERROR_RUNTIME_FAILURE`
- `XR_ERROR_SIZE_INSUFFICIENT`
- `XR_ERROR_SPATIAL_CAPABILITY_UNSUPPORTED_EXT`
- `XR_ERROR_SYSTEM_INVALID`
- `XR_ERROR_VALIDATION_FAILURE`

    typedef enum XrSpatialAnnotationReferenceSourceANDROID {
        XR_SPATIAL_ANNOTATION_REFERENCE_SOURCE_CAMERA_ANDROID = 0,
        XR_SPATIAL_ANNOTATION_REFERENCE_SOURCE_MEDIA_PROJECTION_ANDROID = 1,
        XR_SPATIAL_ANNOTATION_REFERENCE_SOURCE_MAX_ENUM_ANDROID = 0x7FFFFFFF
    } XrSpatialAnnotationReferenceSourceANDROID;

The [XrSpatialAnnotationReferenceSourceANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialAnnotationReferenceSourceANDROID) enumeration describes the source of the reference which provides the metadata for an annotation.

The enums have the following meanings:

Enum Description

`XR_SPATIAL_ANNOTATION_REFERENCE_SOURCE_CAMERA_ANDROID`

The reference image is an uncropped image output from an Android camera API, e.g. an Image from an ImageReader associated with a Camera2 CameraDevice or an ImageProxy from an ImageAnalysis associated with CameraX. This is typically one of the RGB cameras facing forward.

`XR_SPATIAL_ANNOTATION_REFERENCE_SOURCE_MEDIA_PROJECTION_ANDROID`

The reference image is an uncropped image output from the Android MediaProjection API, e.g. an Image from an ImageReader associated with a MediaProjection virtual display. It can include virtual and real content.

The [XrSystemSpatialAnnotationPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSystemSpatialAnnotationPropertiesANDROID) structure is defined as:

    typedef struct XrSystemSpatialAnnotationPropertiesANDROID {
        XrStructureType    type;
        void*              next;
        uint32_t           referenceCacheTimespan;
        uint32_t           maxReferencePixelWidth;
        uint32_t           maxReferencePixelHeight;
        uint32_t           maxReferenceCount;
        uint32_t           maxAnnotationCount;
    } XrSystemSpatialAnnotationPropertiesANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `referenceCacheTimespan` indicates the timespan in sceconds of a valid [XrSpatialReferenceCacheANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialReferenceCacheANDROID) handle.
- `maxReferencePixelWidth` indicates the maximum width of the edge of reference images in pixels.
- `maxReferencePixelHeight` indicates the maximum height of the edge of reference images in pixels.
- `maxReferenceCount` indicates the maximum count of reference images to be allocated at the same time.
- `maxAnnotationCount` indicates the maximum count of annotations to be tracked at the same time.

When the runtime supports the annotation tracking capability, an application **can** inspect relevant system properties by chaining an [XrSystemSpatialAnnotationPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSystemSpatialAnnotationPropertiesANDROID) structure to the [XrSystemProperties](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSystemProperties) when calling [xrGetSystemProperties](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrGetSystemProperties) .

If [XrSpatialReferenceImageEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialReferenceImageEXT) :: `width` from [XrSpatialCapabilityConfigurationAnnotationTrackingANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialCapabilityConfigurationAnnotationTrackingANDROID) :: `reference` exceeds `maxReferencePixelWidth` , the runtime **must** return `XR_ERROR_VALIDATION_FAILURE` when calling [xrCreateSpatialContextAsyncEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateSpatialContextAsyncEXT) .

If [XrSpatialReferenceImageEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialReferenceImageEXT) :: `height` from [XrSpatialCapabilityConfigurationAnnotationTrackingANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialCapabilityConfigurationAnnotationTrackingANDROID) :: `reference` exceeds `maxReferencePixelHeight` , the runtime **must** return `XR_ERROR_VALIDATION_FAILURE` when calling [xrCreateSpatialContextAsyncEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateSpatialContextAsyncEXT) .

If [XrSpatialCapabilityConfigurationAnnotationTrackingANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialCapabilityConfigurationAnnotationTrackingANDROID) :: `time` is out of the timespan of [XrSpatialReferenceCacheANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialReferenceCacheANDROID) :: `cache` , the runtime **must** return `XR_ERROR_TIME_INVALID` when calling [xrCreateSpatialContextAsyncEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateSpatialContextAsyncEXT) . The application **can** recreate the [XrSpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextEXT) handle with a new reference during the timespan of the [XrSpatialReferenceCacheANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialReferenceCacheANDROID) .

If the number of allocated reference images exceed `maxReferenceCount` , the runtime **must** return `XR_ERROR_LIMIT_REACHED` and indicate the initialization failure via [XrEventDataSpatialAnnotationTrackingANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrEventDataSpatialAnnotationTrackingANDROID) :: `initializationResult` . The application **can** destroy the [XrSpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextEXT) handle and try again after pending initialization completed.

If the number of active annotations exceed `maxAnnotationCount` , the runtime **must** return `XR_ERROR_VALIDATION_FAILURE` when calling [xrCreateSpatialContextAsyncEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateSpatialContextAsyncEXT) .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#VUID-XrSystemSpatialAnnotationPropertiesANDROID-extension-notenabled) The `XR_ANDROID_spatial_annotation_tracking` extension **must** be enabled prior to using [XrSystemSpatialAnnotationPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSystemSpatialAnnotationPropertiesANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#VUID-XrSystemSpatialAnnotationPropertiesANDROID-type-type) `type` **must** be `XR_TYPE_SYSTEM_SPATIAL_ANNOTATION_PROPERTIES_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#VUID-XrSystemSpatialAnnotationPropertiesANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)

## Runtime reference cache

    XR_DEFINE_HANDLE(XrSpatialReferenceCacheANDROID)

The [XrSpatialReferenceCacheANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialReferenceCacheANDROID) handle represents a cache of runtime references recorded from a given source.

The [xrCreateSpatialReferenceCacheAsyncANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#xrCreateSpatialReferenceCacheAsyncANDROID) function is defined as:

    XrResult xrCreateSpatialReferenceCacheAsyncANDROID(
        XrSession                                   session,
        const XrSpatialReferenceCacheCreateInfoANDROID* createInfo,
        XrFutureEXT*                                future);

### Parameter Descriptions

- `session` is an [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) in which the reference cache will be active.
- `createInfo` is a pointer to an [XrSpatialReferenceCacheCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialReferenceCacheCreateInfoANDROID) used to specify the reference cache parameters.
- `future` is a pointer to the output handle of an `XrFutureEXT` .

The application **can** create an [XrSpatialReferenceCacheANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialReferenceCacheANDROID) handle by calling [xrCreateSpatialReferenceCacheAsyncANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#xrCreateSpatialReferenceCacheAsyncANDROID) . The runtime **may** take some time to initialize the tracking services. The application **can** then call [xrCreateSpatialReferenceCacheCompleteANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#xrCreateSpatialReferenceCacheCompleteANDROID) repeatedly to check the completion of this asynchronous operation.

The runtime **must** return `XR_ERROR_SPATIAL_CAPABILITY_UNSUPPORTED_EXT` if [XrSpatialReferenceCacheCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialReferenceCacheCreateInfoANDROID) :: `capability` is not listed by [xrEnumerateSpatialCapabilitiesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrEnumerateSpatialCapabilitiesEXT) .

The runtime **must** return `XR_ERROR_FEATURE_UNSUPPORTED` if [XrSpatialReferenceCacheCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialReferenceCacheCreateInfoANDROID) :: `source` is not listed by [xrEnumerateSpatialAnnotationReferenceSourcesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#xrEnumerateSpatialAnnotationReferenceSourcesANDROID) for the given capability.

The application **can** only create one handle per source for a given capability. Otherwise, the runtime **must** return `XR_ERROR_LIMIT_REACHED` .

The application **can** then capture runtime references during the timespan of the [XrSpatialReferenceCacheANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialReferenceCacheANDROID) handle to configure a new [XrSpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextEXT) handle.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#VUID-xrCreateSpatialReferenceCacheAsyncANDROID-extension-notenabled) The `XR_ANDROID_spatial_annotation_tracking` extension **must** be enabled prior to calling [xrCreateSpatialReferenceCacheAsyncANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#xrCreateSpatialReferenceCacheAsyncANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#VUID-xrCreateSpatialReferenceCacheAsyncANDROID-session-parameter) `session` **must** be a valid [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#VUID-xrCreateSpatialReferenceCacheAsyncANDROID-createInfo-parameter) `createInfo` **must** be a pointer to a valid [XrSpatialReferenceCacheCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialReferenceCacheCreateInfoANDROID) structure
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#VUID-xrCreateSpatialReferenceCacheAsyncANDROID-future-parameter) `future` **must** be a pointer to an `XrFutureEXT` value

### Return Codes

[Success](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`
- `XR_SESSION_LOSS_PENDING`

[Failure](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FEATURE_UNSUPPORTED`
- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_HANDLE_INVALID`
- `XR_ERROR_INSTANCE_LOST`
- `XR_ERROR_LIMIT_REACHED`
- `XR_ERROR_OUT_OF_MEMORY`
- `XR_ERROR_RUNTIME_FAILURE`
- `XR_ERROR_SESSION_LOST`
- `XR_ERROR_SPATIAL_CAPABILITY_UNSUPPORTED_EXT`
- `XR_ERROR_VALIDATION_FAILURE`

The [XrSpatialReferenceCacheCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialReferenceCacheCreateInfoANDROID) structure is defined as:

    typedef struct XrSpatialReferenceCacheCreateInfoANDROID {
        XrStructureType                              type;
        const void*                                  next;
        XrSpatialCapabilityEXT                       capability;
        XrSpatialAnnotationReferenceSourceANDROID    source;
    } XrSpatialReferenceCacheCreateInfoANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.
- `capability` is an [XrSpatialCapabilityEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityEXT) describing for which capability the reference cache is created.
- `source` is a an [XrSpatialAnnotationReferenceSourceANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialAnnotationReferenceSourceANDROID) describing the source of the reference cache.

The [XrSpatialReferenceCacheCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialReferenceCacheCreateInfoANDROID) structure describes the information to create an [XrSpatialReferenceCacheANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialReferenceCacheANDROID) handle.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#VUID-XrSpatialReferenceCacheCreateInfoANDROID-extension-notenabled) The `XR_ANDROID_spatial_annotation_tracking` extension **must** be enabled prior to using [XrSpatialReferenceCacheCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialReferenceCacheCreateInfoANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#VUID-XrSpatialReferenceCacheCreateInfoANDROID-type-type) `type` **must** be `XR_TYPE_SPATIAL_REFERENCE_CACHE_CREATE_INFO_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#VUID-XrSpatialReferenceCacheCreateInfoANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#VUID-XrSpatialReferenceCacheCreateInfoANDROID-capability-parameter) `capability` **must** be a valid [XrSpatialCapabilityEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityEXT) value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#VUID-XrSpatialReferenceCacheCreateInfoANDROID-source-parameter) `source` **must** be a valid [XrSpatialAnnotationReferenceSourceANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialAnnotationReferenceSourceANDROID) value

The [xrCreateSpatialReferenceCacheCompleteANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#xrCreateSpatialReferenceCacheCompleteANDROID) function is defined as:

    XrResult xrCreateSpatialReferenceCacheCompleteANDROID(
        XrSession                                   session,
        XrFutureEXT                                 future,
        XrCreateSpatialReferenceCacheCompletionANDROID* completion);

### Parameter Descriptions

- `session` is the [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) previously passed to [xrCreateSpatialReferenceCacheAsyncANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#xrCreateSpatialReferenceCacheAsyncANDROID) :: `session` .
- `future` is the `XrFutureEXT` received from [xrCreateSpatialReferenceCacheAsyncANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#xrCreateSpatialReferenceCacheAsyncANDROID) :: `future` .
- `completion` is a pointer to an [XrCreateSpatialReferenceCacheCompletionANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrCreateSpatialReferenceCacheCompletionANDROID) .

The application **can** call [xrCreateSpatialReferenceCacheCompleteANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#xrCreateSpatialReferenceCacheCompleteANDROID) to wait for the completion of the asynchronous operation started by [xrCreateSpatialReferenceCacheAsyncANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#xrCreateSpatialReferenceCacheAsyncANDROID) .

The runtime **must** return `XR_ERROR_FUTURE_PENDING_EXT` if `future` is not in ready state. The runtime **must** return `XR_ERROR_FUTURE_INVALID_EXT` if `future` has already been completed or cancelled.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#VUID-xrCreateSpatialReferenceCacheCompleteANDROID-extension-notenabled) The `XR_ANDROID_spatial_annotation_tracking` extension **must** be enabled prior to calling [xrCreateSpatialReferenceCacheCompleteANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#xrCreateSpatialReferenceCacheCompleteANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#VUID-xrCreateSpatialReferenceCacheCompleteANDROID-session-parameter) `session` **must** be a valid [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#VUID-xrCreateSpatialReferenceCacheCompleteANDROID-completion-parameter) `completion` **must** be a pointer to an [XrCreateSpatialReferenceCacheCompletionANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrCreateSpatialReferenceCacheCompletionANDROID) structure

### Return Codes

[Success](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`
- `XR_SESSION_LOSS_PENDING`

[Failure](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FEATURE_UNSUPPORTED`
- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_FUTURE_INVALID_EXT`
- `XR_ERROR_FUTURE_PENDING_EXT`
- `XR_ERROR_HANDLE_INVALID`
- `XR_ERROR_INSTANCE_LOST`
- `XR_ERROR_LIMIT_REACHED`
- `XR_ERROR_OUT_OF_MEMORY`
- `XR_ERROR_RUNTIME_FAILURE`
- `XR_ERROR_SESSION_LOST`
- `XR_ERROR_VALIDATION_FAILURE`

The [XrCreateSpatialReferenceCacheCompletionANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrCreateSpatialReferenceCacheCompletionANDROID) structure is defined as:

    typedef struct XrCreateSpatialReferenceCacheCompletionANDROID {
        XrStructureType                   type;
        void*                             next;
        XrResult                          futureResult;
        XrSpatialReferenceCacheANDROID    referenceCache;
    } XrCreateSpatialReferenceCacheCompletionANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.
- `futureResult` is the [XrResult](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrResult) of the reference cache creation operation.
- `referenceCache` is the [XrSpatialReferenceCacheANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialReferenceCacheANDROID) handle if the operation succeeds.

### Future Return Codes

`futureResult` values:

[Success](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`
- `XR_SESSION_LOSS_PENDING`

[Failure](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FEATURE_UNSUPPORTED`
- `XR_ERROR_RUNTIME_FAILURE`
- `XR_ERROR_INSTANCE_LOST`
- `XR_ERROR_SESSION_LOST`
- `XR_ERROR_OUT_OF_MEMORY`
- `XR_ERROR_LIMIT_REACHED`

If `futureResult` is a success code, the runtime **must** return a valid `referenceCache` handle. If `referenceCache` is valid, it remains so only within the lifetime of [xrCreateSpatialReferenceCacheAsyncANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#xrCreateSpatialReferenceCacheAsyncANDROID) :: `session` or until the application destroys the handle with [xrDestroySpatialReferenceCacheANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#xrDestroySpatialReferenceCacheANDROID) whichever comes first.

When `referenceCache` is valid, it records caches within [XrSystemSpatialAnnotationPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSystemSpatialAnnotationPropertiesANDROID) :: `referenceCacheTimespan` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#VUID-XrCreateSpatialReferenceCacheCompletionANDROID-extension-notenabled) The `XR_ANDROID_spatial_annotation_tracking` extension **must** be enabled prior to using [XrCreateSpatialReferenceCacheCompletionANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrCreateSpatialReferenceCacheCompletionANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#VUID-XrCreateSpatialReferenceCacheCompletionANDROID-type-type) `type` **must** be `XR_TYPE_CREATE_SPATIAL_REFERENCE_CACHE_COMPLETION_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#VUID-XrCreateSpatialReferenceCacheCompletionANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#VUID-XrCreateSpatialReferenceCacheCompletionANDROID-futureResult-parameter) `futureResult` **must** be a valid [XrResult](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrResult) value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#VUID-XrCreateSpatialReferenceCacheCompletionANDROID-referenceCache-parameter) `referenceCache` **must** be a valid [XrSpatialReferenceCacheANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialReferenceCacheANDROID) handle

The [xrDestroySpatialReferenceCacheANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#xrDestroySpatialReferenceCacheANDROID) function is defined as:

    XrResult xrDestroySpatialReferenceCacheANDROID(
        XrSpatialReferenceCacheANDROID              cacheHandle);

### Parameter Descriptions

- `cacheHandle` is an [XrSpatialReferenceCacheANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialReferenceCacheANDROID) previously created by [xrCreateSpatialReferenceCacheAsyncANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#xrCreateSpatialReferenceCacheAsyncANDROID) .

The application **can** call [xrDestroySpatialReferenceCacheANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#xrDestroySpatialReferenceCacheANDROID) function to release the `cacheHandle` handle and the underlying resources when finished with spatial context creation.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#VUID-xrDestroySpatialReferenceCacheANDROID-extension-notenabled) The `XR_ANDROID_spatial_annotation_tracking` extension **must** be enabled prior to calling [xrDestroySpatialReferenceCacheANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#xrDestroySpatialReferenceCacheANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#VUID-xrDestroySpatialReferenceCacheANDROID-cacheHandle-parameter) `cacheHandle` **must** be a valid [XrSpatialReferenceCacheANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialReferenceCacheANDROID) handle

### Thread Safety

- Access to `cacheHandle` , and any child handles, **must** be externally synchronized

### Return Codes

[Success](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`

[Failure](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_HANDLE_INVALID`

## Configuration

The [XrSpatialCapabilityConfigurationAnnotationTrackingANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialCapabilityConfigurationAnnotationTrackingANDROID) structure is defined as:

    typedef struct XrSpatialCapabilityConfigurationAnnotationTrackingANDROID {
        XrStructureType                     type;
        const void*                         next;
        XrSpatialCapabilityEXT              capability;
        uint32_t                            enabledComponentCount;
        const XrSpatialComponentTypeEXT*    enabledComponents;
        XrSpatialReferenceCacheANDROID      cache;
        XrTime                              time;
        XrSpatialReferenceImageEXT          reference;
    } XrSpatialCapabilityConfigurationAnnotationTrackingANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `capability` is an [XrSpatialCapabilityEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityEXT) and **must** be `XR_SPATIAL_CAPABILITY_ANNOTATION_TRACKING_ANDROID` .
- `enabledComponentCount` is a `uint32_t` describing the count of elements in the `enabledComponents` array.
- `enabledComponents` is a pointer to an array of [XrSpatialComponentTypeEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentTypeEXT) .
- `cache` is an [XrSpatialReferenceCacheANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialReferenceCacheANDROID) previously created to record runtime references for the `reference` configuration.
- `time` is the `XrTime` at which the `reference` is captured.
- `reference` is an [XrSpatialReferenceImageEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialReferenceImageEXT) with annotations chained to its next pointer.

Applications **can** enable the `XR_SPATIAL_CAPABILITY_ANNOTATION_TRACKING_ANDROID` spatial capability by adding a pointer to the [XrSpatialCapabilityConfigurationAnnotationTrackingANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialCapabilityConfigurationAnnotationTrackingANDROID) structure in [XrSpatialContextCreateInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextCreateInfoEXT) :: `capabilityConfigs` .

The runtime **must** return `XR_ERROR_VALIDATION_FAILURE` if `capability` is not `XR_SPATIAL_CAPABILITY_ANNOTATION_TRACKING_ANDROID` .

The runtime **must** return `XR_ERROR_SPATIAL_CAPABILITY_CONFIGURATION_INVALID_EXT` if `reference` contains no annotations.

The runtime **must** return `XR_ERROR_SPATIAL_CAPABILITY_CONFIGURATION_INVALID_EXT` if the annotation component is listed in `enabledComponents` but no corresponding annotations are associated with `reference` .

The runtime **must** return `XR_ERROR_VALIDATION_FAILURE` if `cache` is not owned by the same [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) passing to [xrCreateSpatialContextAsyncEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateSpatialContextAsyncEXT) .

The runtime **must** return `XR_ERROR_TIME_INVALID` if `time` is out of the timespan of the `cache` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#VUID-XrSpatialCapabilityConfigurationAnnotationTrackingANDROID-extension-notenabled) The `XR_ANDROID_spatial_annotation_tracking` extension **must** be enabled prior to using [XrSpatialCapabilityConfigurationAnnotationTrackingANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialCapabilityConfigurationAnnotationTrackingANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#VUID-XrSpatialCapabilityConfigurationAnnotationTrackingANDROID-type-type) `type` **must** be `XR_TYPE_SPATIAL_CAPABILITY_CONFIGURATION_ANNOTATION_TRACKING_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#VUID-XrSpatialCapabilityConfigurationAnnotationTrackingANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#VUID-XrSpatialCapabilityConfigurationAnnotationTrackingANDROID-capability-parameter) `capability` **must** be a valid [XrSpatialCapabilityEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityEXT) value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#VUID-XrSpatialCapabilityConfigurationAnnotationTrackingANDROID-enabledComponents-parameter) `enabledComponents` **must** be a pointer to an array of `enabledComponentCount` valid [XrSpatialComponentTypeEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentTypeEXT) values
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#VUID-XrSpatialCapabilityConfigurationAnnotationTrackingANDROID-cache-parameter) `cache` **must** be a valid [XrSpatialReferenceCacheANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialReferenceCacheANDROID) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#VUID-XrSpatialCapabilityConfigurationAnnotationTrackingANDROID-reference-parameter) `reference` **must** be a valid [XrSpatialReferenceImageEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialReferenceImageEXT) structure
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#VUID-XrSpatialCapabilityConfigurationAnnotationTrackingANDROID-enabledComponentCount-arraylength) The `enabledComponentCount` parameter **must** be greater than `0`

## Annotation Tracking Events

The [XrEventDataSpatialAnnotationTrackingANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrEventDataSpatialAnnotationTrackingANDROID) structure is defined as:

    typedef struct XrEventDataSpatialAnnotationTrackingANDROID {
        XrStructureType        type;
        const void*            next;
        XrSpatialContextEXT    spatialContext;
        uint32_t               annotationIndex;
        XrResult               initializationResult;
    } XrEventDataSpatialAnnotationTrackingANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `spatialContext` is the [XrSpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextEXT) for which has activated annotation tracking.
- `annotationIndex` maps to the index from the annotation array associated with [XrSpatialCapabilityConfigurationAnnotationTrackingANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialCapabilityConfigurationAnnotationTrackingANDROID) :: `reference` .
- `initializationResult` indicates the initialization result of the annotation. If it is not `XR_SUCCESS` , the application **can** destroy and recreate the [XrSpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextEXT) handle to reinitialize the annotation, or continue using the `spatialContext` to track other annotations.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#VUID-XrEventDataSpatialAnnotationTrackingANDROID-extension-notenabled) The `XR_ANDROID_spatial_annotation_tracking` extension **must** be enabled prior to using [XrEventDataSpatialAnnotationTrackingANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrEventDataSpatialAnnotationTrackingANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#VUID-XrEventDataSpatialAnnotationTrackingANDROID-type-type) `type` **must** be `XR_TYPE_EVENT_DATA_SPATIAL_ANNOTATION_TRACKING_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#VUID-XrEventDataSpatialAnnotationTrackingANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)

The runtime **must** populate the [XrEventDataSpatialAnnotationTrackingANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrEventDataSpatialAnnotationTrackingANDROID) for each annotation to indicate the completion of its initialization. Regardless of the initialization result, the application **can** release the image buffer to reduce memory usage after receiving the event.

The runtime **must** populate `initializationResult` with `XR_SUCCESS` if the annotation is initialized successfully. The application **can** then pull for the `XR_TYPE_EVENT_DATA_SPATIAL_DISCOVERY_RECOMMENDED_EXT` event to track the annotation.

Otherwise, the runtime **must** populate `initializationResult` with an appropriate error code to indicate the failure reason. The application **can** destroy the [XrSpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextEXT) handle to start a new annotation or continue using the `spatialContext` to track other annotations.

## Quad Annotation

A runtime **must** advertise its support for quad annotations using [xrEnumerateSpatialCapabilityComponentTypesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrEnumerateSpatialCapabilityComponentTypesEXT) by listing the following component type:

- `XR_SPATIAL_COMPONENT_TYPE_ANNOTATION_QUAD_ANDROID`

### Quad Reference

The [XrSpatialAnnotationQuadReferenceANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialAnnotationQuadReferenceANDROID) structure is defined as:

    typedef struct XrSpatialAnnotationQuadReferenceANDROID {
        XrStructureType                          type;
        const void*                              next;
        uint32_t                                 quadCount;
        const XrSpatialAnnotationQuadANDROID*    quads;
    } XrSpatialAnnotationQuadReferenceANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `quadCount` is a `uint32_t` describing the count of elements in the `quads` array.
- `quads` is the pointer to an array of [XrSpatialAnnotationQuadANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialAnnotationQuadANDROID) .

When the runtime supports quad annotations, an application **can** configure annotations by chaining an [XrSpatialAnnotationQuadReferenceANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialAnnotationQuadReferenceANDROID) structure to the [XrSpatialReferenceImageEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialReferenceImageEXT) :: `next` , and set the reference in [XrSpatialCapabilityConfigurationAnnotationTrackingANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialCapabilityConfigurationAnnotationTrackingANDROID) :: `reference` when creating the [XrSpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextEXT) handle.

The runtime **must** return `XR_ERROR_SPATIAL_CAPABILITY_CONFIGURATION_INVALID_EXT` from [xrCreateSpatialContextAsyncEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateSpatialContextAsyncEXT) if `quadCount` is 0.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#VUID-XrSpatialAnnotationQuadReferenceANDROID-extension-notenabled) The `XR_ANDROID_spatial_annotation_tracking` extension **must** be enabled prior to using [XrSpatialAnnotationQuadReferenceANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialAnnotationQuadReferenceANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#VUID-XrSpatialAnnotationQuadReferenceANDROID-type-type) `type` **must** be `XR_TYPE_SPATIAL_ANNOTATION_QUAD_REFERENCE_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#VUID-XrSpatialAnnotationQuadReferenceANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#VUID-XrSpatialAnnotationQuadReferenceANDROID-quads-parameter) `quads` **must** be a pointer to an array of `quadCount` valid [XrSpatialAnnotationQuadANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialAnnotationQuadANDROID) structures
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#VUID-XrSpatialAnnotationQuadReferenceANDROID-quadCount-arraylength) The `quadCount` parameter **must** be greater than `0`

The [XrSpatialAnnotationQuadANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialAnnotationQuadANDROID) structure is defined as:

    typedef struct XrSpatialAnnotationQuadANDROID {
        XrSpatialAnnotationQuadAlignmentANDROID    alignment;
        XrVector2f                                 upperLeft;
        XrVector2f                                 upperRight;
        XrVector2f                                 lowerRight;
        XrVector2f                                 lowerLeft;
    } XrSpatialAnnotationQuadANDROID;

### Member Descriptions

- `alignment` is the [XrSpatialAnnotationQuadAlignmentANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialAnnotationQuadAlignmentANDROID) of the quad.
- `upperLeft` is a [XrVector2f](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrVector2f) describing the coordinate of the upper left corner of the quad related to the origin.
- `upperRight` is a [XrVector2f](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrVector2f) describing the coordinate of the upper right corner of the quad related to the origin.
- `lowerRight` is a [XrVector2f](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrVector2f) describing the coordinate of the lower right corner of the quad related to the origin.
- `lowerLeft` is a [XrVector2f](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrVector2f) describing the coordinate of the lower left corner of the quad related to the origin.

A quad in a 2D space is a convex quadrilateral with clockwise order. The value of 4 corners is related to the origin (0, 0) in which the quad is associated with.

- When it's associated with an [XrSpatialReferenceImageEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialReferenceImageEXT) , the origin is the upper left corner of the image where X maps to the pixel on width and Y maps to the pixel on height.
- When it's associated with an [XrSpatialAnnotationQuadDataANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialAnnotationQuadDataANDROID) , the origin is indicated by [XrSpaceLocationData](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpaceLocationData) :: `pose` of [XrSpatialAnnotationQuadDataANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialAnnotationQuadDataANDROID) :: `origin` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#VUID-XrSpatialAnnotationQuadANDROID-extension-notenabled) The `XR_ANDROID_spatial_annotation_tracking` extension **must** be enabled prior to using [XrSpatialAnnotationQuadANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialAnnotationQuadANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#VUID-XrSpatialAnnotationQuadANDROID-alignment-parameter) `alignment` **must** be a valid [XrSpatialAnnotationQuadAlignmentANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialAnnotationQuadAlignmentANDROID) value

    typedef enum XrSpatialAnnotationQuadAlignmentANDROID {
        XR_SPATIAL_ANNOTATION_QUAD_ALIGNMENT_SCREEN_ANDROID = 0,
        XR_SPATIAL_ANNOTATION_QUAD_ALIGNMENT_OBJECT_ANDROID = 1,
        XR_SPATIAL_ANNOTATION_QUAD_ALIGNMENT_MAX_ENUM_ANDROID = 0x7FFFFFFF
    } XrSpatialAnnotationQuadAlignmentANDROID;

The [XrSpatialAnnotationQuadAlignmentANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialAnnotationQuadAlignmentANDROID) enumeration describes the alignment of the quad annotation.

The enums have the following meanings:

Enum Description

`XR_SPATIAL_ANNOTATION_QUAD_ALIGNMENT_SCREEN_ANDROID`

The annotation quad is parallel to the screen plane, while its in-plane rotation remains locked to world gravity. The output appears as a regular, upright bounding box.

`XR_SPATIAL_ANNOTATION_QUAD_ALIGNMENT_OBJECT_ANDROID`

The annotation quad is anchored directly to the object, matching the alignment defined in the reference image. The output is a convex quadrilateral, adjusting its shape to match the perspective of the object.

### Quad Components

The [XrSpatialAnnotationQuadDataANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialAnnotationQuadDataANDROID) structure is defined as:

    typedef struct XrSpatialAnnotationQuadDataANDROID {
        uint32_t                          annotationIndex;
        XrSpaceLocationData               origin;
        XrSpatialAnnotationQuadANDROID    quad;
    } XrSpatialAnnotationQuadDataANDROID;

### Member Descriptions

- `annotationIndex` is the index mapping to the [XrSpatialAnnotationQuadReferenceANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialAnnotationQuadReferenceANDROID) :: `quads` array associated with the reference passed by [XrSpatialCapabilityConfigurationAnnotationTrackingANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialCapabilityConfigurationAnnotationTrackingANDROID) :: `reference` .
- `origin` is a [XrSpaceLocationData](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpaceLocationData) describing the origin of a 2D plane where the quad is rooted. The runtime **must** set [XrSpaceLocationData](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpaceLocationData) :: `locationFlags` to indicate the valid bits of origin pose.
- `quad` is a [XrSpatialAnnotationQuadANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialAnnotationQuadANDROID) representing the quad in the local space. Use `origin` to transform the quad to pose space.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#VUID-XrSpatialAnnotationQuadDataANDROID-extension-notenabled) The `XR_ANDROID_spatial_annotation_tracking` extension **must** be enabled prior to using [XrSpatialAnnotationQuadDataANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialAnnotationQuadDataANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#VUID-XrSpatialAnnotationQuadDataANDROID-origin-parameter) `origin` **must** be a valid [XrSpaceLocationData](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpaceLocationData) structure
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#VUID-XrSpatialAnnotationQuadDataANDROID-quad-parameter) `quad` **must** be a valid [XrSpatialAnnotationQuadANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialAnnotationQuadANDROID) structure

The [XrSpatialComponentAnnotationQuadListANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialComponentAnnotationQuadListANDROID) structure is defined as:

    typedef struct XrSpatialComponentAnnotationQuadListANDROID {
        XrStructureType                        type;
        void*                                  next;
        uint32_t                               quadCount;
        XrSpatialAnnotationQuadDataANDROID*    quads;
    } XrSpatialComponentAnnotationQuadListANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `quadCount` is a `uint32_t` describing the count of elements in the `quads` array.
- `quads` is an array of [XrSpatialAnnotationQuadDataANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialAnnotationQuadDataANDROID) .

The application **can** query the quad annotation component of the spatial entities in an [XrSpatialSnapshotEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialSnapshotEXT) by adding `XR_SPATIAL_COMPONENT_TYPE_ANNOTATION_QUAD_ANDROID` in [XrSpatialComponentDataQueryConditionEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryConditionEXT) :: `componentTypes` and adding [XrSpatialComponentAnnotationQuadListANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialComponentAnnotationQuadListANDROID) to the next pointer chain of [XrSpatialComponentDataQueryResultEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryResultEXT) .

The runtime **must** return `XR_ERROR_VALIDATION_FAILURE` from [xrQuerySpatialComponentDataEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrQuerySpatialComponentDataEXT) if [XrSpatialComponentAnnotationQuadListANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialComponentAnnotationQuadListANDROID) is in the next chain of [XrSpatialComponentDataQueryResultEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryResultEXT) :: `next` but `XR_SPATIAL_COMPONENT_TYPE_ANNOTATION_QUAD_ANDROID` is not included in [XrSpatialComponentDataQueryConditionEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryConditionEXT) :: `componentTypes` .

The runtime **must** return `XR_ERROR_SIZE_INSUFFICIENT` from [xrQuerySpatialComponentDataEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrQuerySpatialComponentDataEXT) if `quadCount` is less than [XrSpatialComponentDataQueryResultEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryResultEXT) :: `entityIdCountOutput` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#VUID-XrSpatialComponentAnnotationQuadListANDROID-extension-notenabled) The `XR_ANDROID_spatial_annotation_tracking` extension **must** be enabled prior to using [XrSpatialComponentAnnotationQuadListANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialComponentAnnotationQuadListANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#VUID-XrSpatialComponentAnnotationQuadListANDROID-type-type) `type` **must** be `XR_TYPE_SPATIAL_COMPONENT_ANNOTATION_QUAD_LIST_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#VUID-XrSpatialComponentAnnotationQuadListANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#VUID-XrSpatialComponentAnnotationQuadListANDROID-quads-parameter) `quads` **must** be a pointer to an array of `quadCount` [XrSpatialAnnotationQuadDataANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialAnnotationQuadDataANDROID) structures
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#VUID-XrSpatialComponentAnnotationQuadListANDROID-quadCount-arraylength) The `quadCount` parameter **must** be greater than `0`

## Example Code

### Check runtime support

The following example code demonstrates how to check if the runtime supports annotation tracking capability.

    XrInstance instance;  // previously initialized
    XrSystemId systemId;  // previously initialized
    XrSession session;    // previously initialized
    XrSpace localSpace;   // previously initialized, e.g. from
                          // XR_REFERENCE_SPACE_TYPE_LOCAL

    PFN_xrEnumerateSpatialCapabilitiesEXT xrEnumerateSpatialCapabilitiesEXT;
    PFN_xrEnumerateSpatialAnnotationReferenceSourcesANDROID xrEnumerateSpatialAnnotationReferenceSourcesANDROID;
    PFN_xrEnumerateSpatialReferenceImageFormatsEXT xrEnumerateSpatialReferenceImageFormatsEXT;
    PFN_xrEnumerateSpatialCapabilityComponentTypesEXT xrEnumerateSpatialCapabilityComponentTypesEXT;

    // Check spatial annotation tracking capability
    uint32_t capabilityCount;
    CHK_XR(xrEnumerateSpatialCapabilitiesEXT(instance, systemId, 0,
                                             &capabilityCount, nullptr));
    std::vector<XrSpatialCapabilityEXT> capabilities(capabilityCount);
    CHK_XR(xrEnumerateSpatialCapabilitiesEXT(instance, systemId, capabilityCount,
                                             &capabilityCount,
                                             capabilities.data()));
    if (std::find(capabilities.begin(), capabilities.end(),
                  XR_SPATIAL_CAPABILITY_ANNOTATION_TRACKING_ANDROID) ==
        capabilities.end()) {
      // System does not support spatial annotation tracking.
      return;
    }

    // Inspect system properties for annotation tracking variables
    XrSystemSpatialAnnotationPropertiesANDROID annotationSystemProperties{
        XR_TYPE_SYSTEM_SPATIAL_ANNOTATION_PROPERTIES_ANDROID};
    XrSystemProperties systemProperties{.type = XR_TYPE_SYSTEM_PROPERTIES,
                                        .next = &annotationSystemProperties,
                                        .systemId = systemId};
    CHK_XR(xrGetSystemProperties(instance, systemId, &systemProperties));
    if (annotationSystemProperties.maxAnnotationCount == 0) {
      // System does not support any active annotations.
      return;
    }

    // Enumerate supported reference sources
    uint32_t sourceCountOutput = 0;
    XrSpatialAnnotationReferenceSourceANDROID desiredSource =
        XR_SPATIAL_ANNOTATION_REFERENCE_SOURCE_CAMERA_ANDROID;
    CHK_XR(xrEnumerateSpatialAnnotationReferenceSourcesANDROID(
        instance, systemId, XR_SPATIAL_CAPABILITY_ANNOTATION_TRACKING_ANDROID,
        0, &sourceCountOutput, nullptr));
    std::vector<XrSpatialAnnotationReferenceSourceANDROID> sources(sourceCountOutput);
    CHK_XR(xrEnumerateSpatialAnnotationReferenceSourcesANDROID(
        instance, systemId, XR_SPATIAL_CAPABILITY_ANNOTATION_TRACKING_ANDROID,
        sourceCountOutput, &sourceCountOutput, sources.data()));
    if (std::find(sources.begin(), sources.end(), desiredSource) == sources.end()) {
      // The desired source is not supported.
      return;
    }

    // Enumerate supported reference image formats, provided by XR_EXT_spatial_image_tracking.
    uint32_t formatCountOutput = 0;
    XrSpatialReferenceImageFormatEXT desiredFormat =
        XR_SPATIAL_REFERENCE_IMAGE_FORMAT_YUV_420_888_EXT; // Or XR_SPATIAL_REFERENCE_IMAGE_FORMAT_RGBA_8888_EXT for screenshot.
    CHK_XR(xrEnumerateSpatialReferenceImageFormatsEXT(
        instance, systemId, XR_SPATIAL_CAPABILITY_ANNOTATION_TRACKING_ANDROID, 0,
        &formatCountOutput, nullptr));
    std::vector<XrSpatialReferenceImageFormatEXT> formats(formatCountOutput);
    CHK_XR(xrEnumerateSpatialReferenceImageFormatsEXT(
        instance, systemId, XR_SPATIAL_CAPABILITY_ANNOTATION_TRACKING_ANDROID,
        formats.size(), &formatCountOutput, formats.data()));
    if (std::find(formats.begin(), formats.end(), desiredFormat) == formats.end()) {
      // The desired format is not supported
      return;
    }

    // Enumerate supported components for annotation tracking capability.
    XrSpatialCapabilityComponentTypesEXT capabilityComponentTypes{
        XR_TYPE_SPATIAL_CAPABILITY_COMPONENT_TYPES_EXT};
    CHK_XR(xrEnumerateSpatialCapabilityComponentTypesEXT(
        instance, systemId, XR_SPATIAL_CAPABILITY_ANNOTATION_TRACKING_ANDROID,
        &capabilityComponentTypes));
    std::vector<XrSpatialComponentTypeEXT>
        annotationTypes(capabilityComponentTypes.componentTypeCountOutput);
    capabilityComponentTypes.componentTypeCapacityInput = annotationTypes.size();
    capabilityComponentTypes.componentTypes = annotationTypes.data();
    CHK_XR(xrEnumerateSpatialCapabilityComponentTypesEXT(
        instance, systemId, XR_SPATIAL_CAPABILITY_ANNOTATION_TRACKING_ANDROID,
        &capabilityComponentTypes));

    // Check supported annotation components.
    XrSpatialComponentTypeEXT desiredComponent =
        XR_SPATIAL_COMPONENT_TYPE_ANNOTATION_QUAD_ANDROID;
    const auto supportedComponent = [&annotationTypes](
                                        XrSpatialComponentTypeEXT component) {
      return std::find(annotationTypes.begin(), annotationTypes.end(), component) !=
             annotationTypes.end();
    };
    if (!supportedComponent(desiredComponent)) {
      // The desired annotation is not supported.
      return;
    }

### Configure quad annotation

The following example code demonstrates how to configure quad annotation.

    XrInstance instance;  // previously initialized
    XrSystemId systemId;  // previously initialized
    XrSession session;    // previously initialized
    XrSpace localSpace;   // previously initialized, e.g. from
                          // XR_REFERENCE_SPACE_TYPE_LOCAL

    PFN_xrCreateSpatialReferenceCacheAsyncANDROID xrCreateSpatialReferenceCacheAsyncANDROID;
    PFN_xrCreateSpatialReferenceCacheCompleteANDROID xrCreateSpatialReferenceCacheCompleteANDROID;
    PFN_xrDestroySpatialReferenceCacheANDROID xrDestroySpatialReferenceCacheANDROID;
    PFN_xrCreateSpatialContextAsyncEXT xrCreateSpatialContextAsyncEXT;
    PFN_xrCreateSpatialContextCompleteEXT xrCreateSpatialContextCompleteEXT;
    void (*waitUntilReady)(XrFutureEXT);

    XrSpatialReferenceImageFormatEXT desiredFormat;
    XrSpatialAnnotationReferenceSourceANDROID desiredSource;
    XrSpatialComponentTypeEXT desiredComponent;

    // Create and start reference cache to prepare for capturing reference images.
    XrSpatialReferenceCacheANDROID referenceCache;
    XrSpatialReferenceCacheCreateInfoANDROID cacheCreateInfo{
      .type = XR_TYPE_SPATIAL_REFERENCE_CACHE_CREATE_INFO_ANDROID,
      .next = nullptr,
      .capability = XR_SPATIAL_CAPABILITY_ANNOTATION_TRACKING_ANDROID,
      .source = desiredSource,
    };
    XrFutureEXT cacheFuture = XR_NULL_FUTURE_EXT;
    CHK_XR(xrCreateSpatialReferenceCacheAsyncANDROID(session, &cacheCreateInfo, &cacheFuture));

    waitUntilReady(cacheFuture);

    XrCreateSpatialReferenceCacheCompletionANDROID cacheCompletion{
        XR_TYPE_CREATE_SPATIAL_REFERENCE_CACHE_COMPLETION_ANDROID};
    CHK_XR(xrCreateSpatialReferenceCacheCompleteANDROID(session, cacheFuture,
                                                         &cacheCompletion));
    if (cacheCompletion.futureResult != XR_SUCCESS) {
      // Error, reference cache creation failed
      return;
    }

    referenceCache = cacheCompletion.referenceCache;

    // Create the reference image with quad annotations

    //  YUV 4:2:0 Planar:
    // ---
    // |     Y      |Cb |Cr |
    // ---
    XrSpatialReferenceImagePlaneEXT cameraImagePlanes[3];
    // for each plane (0=Y, 1=U(cb), 2=V(Cr)) return by Image#getPlanes().
    for (int i = 0; i < 3; ++i) {
      cameraImagePlanes[i].buffer; // read from Plane#getBuffer().
      cameraImagePlanes[i].bufferSize; // set each buffer size. Y = width * height (bytes); U = Y / 4 (bytes); V = Y / 4 (bytes).
      cameraImagePlanes[i].rowStride; // read from Plane#getRowStride().
      cameraImagePlanes[i].pixelStride; // read from Plane#getPixelStride().
    }
    XrSpatialReferenceImageEXT referenceImage{
          XR_TYPE_SPATIAL_REFERENCE_IMAGE_EXT};
    referenceImage.width = 640;
    referenceImage.height = 480;
    referenceImage.format = desiredFormat;
    referenceImage.planeCount = 3;
    referenceImage.planes = cameraImagePlanes;

    XrSpatialAnnotationQuadANDROID
        quad; // quad coordinates within the reference image.
    quad.alignment = XR_SPATIAL_ANNOTATION_QUAD_ALIGNMENT_OBJECT_ANDROID;
    // Set unnormalized pixel coordinates of 4 corners.
    quad.upperLeft = {0.0, 0.0};
    quad.upperRight = {0.0, 100.0};
    quad.lowerRight = {100.0, 100.0};
    quad.lowerLeft = {0.0, 100.0};

    XrSpatialAnnotationQuadReferenceANDROID quadReference{
        XR_TYPE_SPATIAL_ANNOTATION_QUAD_REFERENCE_ANDROID};
    quadReference.quads = &quad;
    quadReference.quadCount = 1;
    referenceImage.next = &quadReference;

    // Create the spatial context with annotation configuration.
    XrSpatialContextEXT spatialContext{};
    {
      const std::array<XrSpatialComponentTypeEXT, 1> enabledComponents = {
          desiredComponent,
      };

      // Configure annotation tracking
      XrSpatialCapabilityConfigurationAnnotationTrackingANDROID annotationConfig{
          XR_TYPE_SPATIAL_CAPABILITY_CONFIGURATION_ANNOTATION_TRACKING_ANDROID};
      annotationConfig.capability =
          XR_SPATIAL_CAPABILITY_ANNOTATION_TRACKING_ANDROID;
      annotationConfig.enabledComponentCount = enabledComponents.size();
      annotationConfig.enabledComponents = enabledComponents.data();
      annotationConfig.cache = referenceCache;
      annotationConfig.time; // The time when this reference image is captured.
      annotationConfig.reference = referenceImage;

      std::vector<XrSpatialCapabilityConfigurationBaseHeaderEXT *>
          capabilityConfigs;
      capabilityConfigs.push_back(
          reinterpret_cast<XrSpatialCapabilityConfigurationBaseHeaderEXT *>(
              &annotationConfig));

      XrSpatialContextCreateInfoEXT spatialContextCreateInfo{
          XR_TYPE_SPATIAL_CONTEXT_CREATE_INFO_EXT};
      spatialContextCreateInfo.capabilityConfigCount = capabilityConfigs.size();
      spatialContextCreateInfo.capabilityConfigs = capabilityConfigs.data();

      XrFutureEXT createContextFuture = XR_NULL_FUTURE_EXT;
      CHK_XR(xrCreateSpatialContextAsyncEXT(session, &spatialContextCreateInfo,
                                            &createContextFuture));

      waitUntilReady(createContextFuture);

      XrCreateSpatialContextCompletionEXT completion{
          XR_TYPE_CREATE_SPATIAL_CONTEXT_COMPLETION_EXT};
      CHK_XR(xrCreateSpatialContextCompleteEXT(session, createContextFuture,
                                               &completion));
      if (completion.futureResult != XR_SUCCESS) {
        // Error, spatial context creation failed
        return;
      }

      spatialContext = completion.spatialContext;
      CHK_XR(xrDestroySpatialReferenceCacheANDROID(referenceCache));
    }

### Discover active annotations

The following example code demonstrates how to discover and query annotations.

    XrInstance instance;  // previously initialized
    XrSession session;    // previously initialized
    XrSpace localSpace;   // previously initialized, e.g. from
                          // XR_REFERENCE_SPACE_TYPE_LOCAL
    XrSpatialContextEXT spatialContext; // previously created

    PFN_xrCreateSpatialDiscoverySnapshotAsyncEXT xrCreateSpatialDiscoverySnapshotAsyncEXT;
    PFN_xrCreateSpatialDiscoverySnapshotCompleteEXT xrCreateSpatialDiscoverySnapshotCompleteEXT;
    PFN_xrQuerySpatialComponentDataEXT xrQuerySpatialComponentDataEXT;
    PFN_xrDestroySpatialSnapshotEXT xrDestroySpatialSnapshotEXT;
    PFN_xrPollEvent xrPollEvent;
    PFN_xrDestroySpatialContextEXT xrDestroySpatialContextEXT;
    void (*waitUntilReady)(XrFutureEXT);

    XrSpatialComponentTypeEXT desiredComponent; // e.g. XR_SPATIAL_COMPONENT_TYPE_ANNOTATION_QUAD_ANDROID

    auto discoverAnnotations = [&](XrSpatialContextEXT spatialContext, XrTime time,
                                   XrSpace baseSpace) {
      std::array<XrSpatialComponentTypeEXT, 1> snapshotComponents{desiredComponent};
      XrSpatialDiscoverySnapshotCreateInfoEXT snapshotCreateInfo{
          XR_TYPE_SPATIAL_DISCOVERY_SNAPSHOT_CREATE_INFO_EXT};
      snapshotCreateInfo.componentTypeCount = snapshotComponents.size();
      snapshotCreateInfo.componentTypes = snapshotComponents.data();
      XrFutureEXT discoveryFuture = XR_NULL_FUTURE_EXT;
      CHK_XR(xrCreateSpatialDiscoverySnapshotAsyncEXT(
          spatialContext, &snapshotCreateInfo, &discoveryFuture));

      waitUntilReady(discoveryFuture);

      XrCreateSpatialDiscoverySnapshotCompletionInfoEXT completionInfo{
          XR_TYPE_CREATE_SPATIAL_DISCOVERY_SNAPSHOT_COMPLETION_INFO_EXT};
      completionInfo.baseSpace = baseSpace;
      completionInfo.time = time;
      completionInfo.future = discoveryFuture;

      XrCreateSpatialDiscoverySnapshotCompletionEXT completion{
          XR_TYPE_CREATE_SPATIAL_DISCOVERY_SNAPSHOT_COMPLETION_EXT};
      CHK_XR(xrCreateSpatialDiscoverySnapshotCompleteEXT(
          spatialContext, &completionInfo, &completion));
      if (completion.futureResult == XR_SUCCESS) {
        // Query for desired annotation data, e.g. quad.
        XrSpatialComponentTypeEXT componentsToQuery[] = {
            XR_SPATIAL_COMPONENT_TYPE_ANNOTATION_QUAD_ANDROID};
        XrSpatialComponentDataQueryConditionEXT queryCond{
            XR_TYPE_SPATIAL_COMPONENT_DATA_QUERY_CONDITION_EXT};
        queryCond.componentTypeCount = 1;
        queryCond.componentTypes = componentsToQuery;
        XrSpatialComponentDataQueryResultEXT queryResult{
            XR_TYPE_SPATIAL_COMPONENT_DATA_QUERY_RESULT_EXT};
        CHK_XR(xrQuerySpatialComponentDataEXT(completion.snapshot, &queryCond,
                                              &queryResult));

        std::vector<XrSpatialEntityIdEXT> entityIds(
            queryResult.entityIdCountOutput);
        std::vector<XrSpatialEntityTrackingStateEXT> entityStates(
            queryResult.entityStateCountOutput);
        queryResult.entityIdCapacityInput = entityIds.size();
        queryResult.entityIds = entityIds.data();
        queryResult.entityStateCapacityInput = entityStates.size();
        queryResult.entityStates = entityStates.data();

        std::vector<XrSpatialAnnotationQuadDataANDROID> quads(
            queryResult.entityIdCountOutput);
        XrSpatialComponentAnnotationQuadListANDROID quadList{
            XR_TYPE_SPATIAL_COMPONENT_ANNOTATION_QUAD_LIST_ANDROID};
        quadList.quadCount = quads.size();
        quadList.quads = quads.data();
        queryResult.next = &quadList;

        CHK_XR(xrQuerySpatialComponentDataEXT(completion.snapshot, &queryCond,
                                              &queryResult));

        for (int32_t i = 0; i < queryResult.entityIdCountOutput; ++i) {
          if (entityStates[i] == XR_SPATIAL_ENTITY_TRACKING_STATE_TRACKING_EXT) {
            const XrSpatialAnnotationQuadDataANDROID &currentQuad = quads[i];
            // Rendering quad in the view.
          }
        }

        CHK_XR(xrDestroySpatialSnapshotEXT(completion.snapshot));
      }
    };

    while (1) {
      // For every frame in frame loop

      XrSpace space;           // Application's play space.
      XrFrameState frameState; // Previously returned from xrWaitFrame
      const XrTime time = frameState.predictedDisplayTime;

      // Poll for the XR_TYPE_EVENT_DATA_SPATIAL_DISCOVERY_RECOMMENDED_EXT event
      XrEventDataBuffer event = {XR_TYPE_EVENT_DATA_BUFFER};
      XrResult result = xrPollEvent(instance, &event);
      if (result == XR_SUCCESS) {
        switch (event.type) {
        case XR_TYPE_EVENT_DATA_SPATIAL_ANNOTATION_TRACKING_ANDROID: {
          const XrEventDataSpatialAnnotationTrackingANDROID &eventdata =
              *reinterpret_cast<XrEventDataSpatialAnnotationTrackingANDROID *>(
                  &event);
          if (eventdata.initializationResult != XR_SUCCESS) {
            // handle initialization failure.
            // e.g. CHK_XR(xrDestroySpatialContextEXT(spatialContext));
          }
          break;
        }
        case XR_TYPE_EVENT_DATA_SPATIAL_DISCOVERY_RECOMMENDED_EXT: {
          const XrEventDataSpatialDiscoveryRecommendedEXT &eventdata =
              *reinterpret_cast<XrEventDataSpatialDiscoveryRecommendedEXT *>(
                  &event);
          // Discover spatial entities for the context that we received the
          // "discovery recommended" event for.
          //discoverSpatialEntities(eventdata.spatialContext, time, space);
          break;
        }
        }
      }

      // Finish frame loop
    }

    CHK_XR(xrDestroySpatialContextEXT(spatialContext));

## New Object Types

- [XrSpatialReferenceCacheANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialReferenceCacheANDROID)

## New Commands

- [xrCreateSpatialReferenceCacheAsyncANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#xrCreateSpatialReferenceCacheAsyncANDROID)
- [xrCreateSpatialReferenceCacheCompleteANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#xrCreateSpatialReferenceCacheCompleteANDROID)
- [xrDestroySpatialReferenceCacheANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#xrDestroySpatialReferenceCacheANDROID)
- [xrEnumerateSpatialAnnotationReferenceSourcesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#xrEnumerateSpatialAnnotationReferenceSourcesANDROID)

## New Structures

- [XrCreateSpatialReferenceCacheCompletionANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrCreateSpatialReferenceCacheCompletionANDROID)
- [XrEventDataSpatialAnnotationTrackingANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrEventDataSpatialAnnotationTrackingANDROID)
- [XrSpatialAnnotationQuadANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialAnnotationQuadANDROID)
- [XrSpatialAnnotationQuadDataANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialAnnotationQuadDataANDROID)
- [XrSpatialCapabilityConfigurationAnnotationTrackingANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialCapabilityConfigurationAnnotationTrackingANDROID)
- [XrSpatialReferenceCacheCreateInfoANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialReferenceCacheCreateInfoANDROID)
- Extending [XrSpatialComponentDataQueryResultEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryResultEXT) :

  - [XrSpatialComponentAnnotationQuadListANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialComponentAnnotationQuadListANDROID)
- Extending [XrSpatialReferenceImageEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialReferenceImageEXT) :

  - [XrSpatialAnnotationQuadReferenceANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialAnnotationQuadReferenceANDROID)
- Extending [XrSystemProperties](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSystemProperties) :

  - [XrSystemSpatialAnnotationPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSystemSpatialAnnotationPropertiesANDROID)

## New Enums

- [XrSpatialAnnotationQuadAlignmentANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialAnnotationQuadAlignmentANDROID)
- [XrSpatialAnnotationReferenceSourceANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking#XrSpatialAnnotationReferenceSourceANDROID)

## New Enum Constants

- `XR_ANDROID_SPATIAL_ANNOTATION_TRACKING_EXTENSION_NAME`
- `XR_ANDROID_spatial_annotation_tracking_SPEC_VERSION`
- Extending [XrObjectType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrObjectType) :

  - `XR_OBJECT_TYPE_SPATIAL_REFERENCE_CACHE_ANDROID`
- Extending [XrSpatialCapabilityEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityEXT) :

  - `XR_SPATIAL_CAPABILITY_ANNOTATION_TRACKING_ANDROID`
- Extending [XrSpatialComponentTypeEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentTypeEXT) :

  - `XR_SPATIAL_COMPONENT_TYPE_ANNOTATION_QUAD_ANDROID`
- Extending [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) :

  - `XR_TYPE_CREATE_SPATIAL_REFERENCE_CACHE_COMPLETION_ANDROID`
  - `XR_TYPE_EVENT_DATA_SPATIAL_ANNOTATION_TRACKING_ANDROID`
  - `XR_TYPE_SPATIAL_ANNOTATION_QUAD_REFERENCE_ANDROID`
  - `XR_TYPE_SPATIAL_CAPABILITY_CONFIGURATION_ANNOTATION_TRACKING_ANDROID`
  - `XR_TYPE_SPATIAL_COMPONENT_ANNOTATION_QUAD_LIST_ANDROID`
  - `XR_TYPE_SPATIAL_REFERENCE_CACHE_CREATE_INFO_ANDROID`
  - `XR_TYPE_SYSTEM_SPATIAL_ANNOTATION_PROPERTIES_ANDROID`

## Issues

## Version History

- Revision 1, 2025-09-17 (Levana Chen)

  - Initial extension description.