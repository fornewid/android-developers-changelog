---
title: https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_bounds
url: https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_bounds
source: md.txt
---

### XR_ANDROID_spatial_discovery_bounds

**Name String**

`XR_ANDROID_spatial_discovery_bounds`

**Extension Type**

Instance extension

**Registered Extension Number**

762

**Revision**

1

**Ratification Status**

Not ratified

**Extension and Version Dependencies**

`XR_EXT_spatial_entity`

**Contributors**

Nihav Jain, Google  

Natalie Fleury, Meta  

Yuichi Taguchi, Meta  

Yin Li, Microsoft  

Ron Bessems, Meta  

Karthik Kadappan, Magic Leap  

Jimmy Alamparambil, ByteDance  

Zhipeng Liu, ByteDance  

Jun Yan, ByteDance

## Overview

This extension adds definitions for spatial bounds that allows applications to filter discovered spatial entities when calling [xrCreateSpatialDiscoverySnapshotAsyncEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateSpatialDiscoverySnapshotAsyncEXT) .

## Spatial Bounds

The [XrSpatialBoundsSpherefANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_bounds#XrSpatialBoundsSpherefANDROID) structure is defined as:

    typedef struct XrSpatialBoundsSpherefANDROID {
        XrStructureType    type;
        const void*        next;
        XrSpace            space;
        XrTime             time;
        XrSpheref          sphere;
    } XrSpatialBoundsSpherefANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `space` is the [XrSpace](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpace) that any poses for the bounds are defined in.
- `time` is an `XrTime` at which the poses for the bounds are defined.
- `sphere` is an [XrSpheref](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpheref) which describes the spherical volume within which the runtime **must** constrain its discovery of spatial entities.

Spatial capabilities that support `XR_SPATIAL_CAPABILITY_FEATURE_SPHERE_BOUNDS_FILTER_ANDROID` (as enumerated by [xrEnumerateSpatialCapabilityFeaturesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrEnumerateSpatialCapabilityFeaturesEXT) ) allow the application to restrict the discovery to spatial entities whose location or bounds are within or intersecting with `sphere` by chaining [XrSpatialBoundsSpherefANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_bounds#XrSpatialBoundsSpherefANDROID) to [XrSpatialDiscoverySnapshotCreateInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialDiscoverySnapshotCreateInfoEXT) :: `next` . For a discovery snapshot in which the applicable capability supports `XR_SPATIAL_CAPABILITY_FEATURE_SPHERE_BOUNDS_FILTER_ANDROID` , if this structure is present in the `next` chain, the runtime **must** not include any spatial entities whose location or bounds are entirely outside of `sphere` .

It is important to note that the inclusion of [XrSpatialBoundsSpherefANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_bounds#XrSpatialBoundsSpherefANDROID) in the next chain of [XrSpatialDiscoverySnapshotCreateInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialDiscoverySnapshotCreateInfoEXT) acts as an 'AND' condition with the other filters provided. Entities coming from spatial capabilities that do not support `XR_SPATIAL_CAPABILITY_FEATURE_SPHERE_BOUNDS_FILTER_ANDROID` **must** not be included in the discovery snapshot. This behavior is different from the rest of the OpenXR specification where unrecognized or unsupported structures in the next pointer chain are ignored by the runtime. Also, as described in the [Next Chain Structure Uniqueness](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-next-chain-structure-uniqueness) section, the runtime will only process the first occurrence of the [XrSpatialBoundsSpherefANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_bounds#XrSpatialBoundsSpherefANDROID) structure in the next chain.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_bounds#VUID-XrSpatialBoundsSpherefANDROID-extension-notenabled) The `XR_ANDROID_spatial_discovery_bounds` extension **must** be enabled prior to using [XrSpatialBoundsSpherefANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_bounds#XrSpatialBoundsSpherefANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_bounds#VUID-XrSpatialBoundsSpherefANDROID-type-type) `type` **must** be `XR_TYPE_SPATIAL_BOUNDS_SPHEREF_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_bounds#VUID-XrSpatialBoundsSpherefANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_bounds#VUID-XrSpatialBoundsSpherefANDROID-space-parameter) `space` **must** be a valid [XrSpace](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpace) handle

The [XrSpatialBoundsBoxfANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_bounds#XrSpatialBoundsBoxfANDROID) structure is defined as:

    typedef struct XrSpatialBoundsBoxfANDROID {
        XrStructureType    type;
        const void*        next;
        XrSpace            space;
        XrTime             time;
        XrBoxf             box;
    } XrSpatialBoundsBoxfANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `space` is the [XrSpace](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpace) that any poses for the bounds are defined in.
- `time` is an `XrTime` at which the poses for the bounds are defined.
- `box` is an [XrBoxf](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrBoxf) which describes the box volume within which the runtime **must** constrain its discovery of spatial entities.

Spatial capabilities that support `XR_SPATIAL_CAPABILITY_FEATURE_BOX_BOUNDS_FILTER_ANDROID` (as enumerated by [xrEnumerateSpatialCapabilityFeaturesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrEnumerateSpatialCapabilityFeaturesEXT) ) allow the application to restrict the discovery to spatial entities whose location or bounds are within or intersecting with `box` by chaining [XrSpatialBoundsBoxfANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_bounds#XrSpatialBoundsBoxfANDROID) to [XrSpatialDiscoverySnapshotCreateInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialDiscoverySnapshotCreateInfoEXT) :: `next` . For a discovery snapshot in which the applicable capability supports `XR_SPATIAL_CAPABILITY_FEATURE_BOX_BOUNDS_FILTER_ANDROID` , if this structure is present in the `next` chain, the runtime **must** not include any spatial entities whose location or bounds are entirely outside of `box` .

It is important to note that the inclusion of [XrSpatialBoundsBoxfANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_bounds#XrSpatialBoundsBoxfANDROID) in the next chain of [XrSpatialDiscoverySnapshotCreateInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialDiscoverySnapshotCreateInfoEXT) acts as an 'AND' condition with the other filters provided. Entities coming from spatial capabilities that do not support `XR_SPATIAL_CAPABILITY_FEATURE_BOX_BOUNDS_FILTER_ANDROID` **must** not be included in the discovery snapshot. This behavior is different from the rest of the OpenXR specification where unrecognized or unsupported structures in the next pointer chain are ignored by the runtime. Also, as described in the [Next Chain Structure Uniqueness](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-next-chain-structure-uniqueness) section, the runtime will only process the first occurrence of the [XrSpatialBoundsBoxfANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_bounds#XrSpatialBoundsBoxfANDROID) structure in the next chain.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_bounds#VUID-XrSpatialBoundsBoxfANDROID-extension-notenabled) The `XR_ANDROID_spatial_discovery_bounds` extension **must** be enabled prior to using [XrSpatialBoundsBoxfANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_bounds#XrSpatialBoundsBoxfANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_bounds#VUID-XrSpatialBoundsBoxfANDROID-type-type) `type` **must** be `XR_TYPE_SPATIAL_BOUNDS_BOXF_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_bounds#VUID-XrSpatialBoundsBoxfANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_bounds#VUID-XrSpatialBoundsBoxfANDROID-space-parameter) `space` **must** be a valid [XrSpace](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpace) handle

The [XrSpatialBoundsFrustumfANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_bounds#XrSpatialBoundsFrustumfANDROID) structure is defined as:

    typedef struct XrSpatialBoundsFrustumfANDROID {
        XrStructureType    type;
        const void*        next;
        XrSpace            space;
        XrTime             time;
        XrFrustumf         frustum;
    } XrSpatialBoundsFrustumfANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `space` is the [XrSpace](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpace) that any poses for the bounds are defined in.
- `time` is an `XrTime` at which the poses for the bounds are defined.
- `frustum` is an [XrFrustumf](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrFrustumf) which describes the frustum volume within which the runtime **must** constrain its discovery of spatial entities.

Spatial capabilities that support `XR_SPATIAL_CAPABILITY_FEATURE_FRUSTUM_BOUNDS_FILTER_ANDROID` (as enumerated by [xrEnumerateSpatialCapabilityFeaturesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrEnumerateSpatialCapabilityFeaturesEXT) ) allow the application to restrict the discovery to spatial entities whose location or bounds are within or intersecting with `frustum` by chaining [XrSpatialBoundsFrustumfANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_bounds#XrSpatialBoundsFrustumfANDROID) to [XrSpatialDiscoverySnapshotCreateInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialDiscoverySnapshotCreateInfoEXT) :: `next` . For a discovery snapshot in which the applicable capability supports `XR_SPATIAL_CAPABILITY_FEATURE_FRUSTUM_BOUNDS_FILTER_ANDROID` , if this structure is present in the `next` chain, the runtime **must** not include any spatial entities whose location or bounds are entirely outside of `frustum` .

It is important to note that the inclusion of [XrSpatialBoundsFrustumfANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_bounds#XrSpatialBoundsFrustumfANDROID) in the next chain of [XrSpatialDiscoverySnapshotCreateInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialDiscoverySnapshotCreateInfoEXT) acts as an 'AND' condition with the other filters provided. Entities coming from spatial capabilities that do not support `XR_SPATIAL_CAPABILITY_FEATURE_FRUSTUM_BOUNDS_FILTER_ANDROID` **must** not be included in the discovery snapshot. This behavior is different from the rest of the OpenXR specification where unrecognized or unsupported structures in the next pointer chain are ignored by the runtime. Also, as described in the [Next Chain Structure Uniqueness](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-next-chain-structure-uniqueness) section, the runtime will only process the first occurrence of the [XrSpatialBoundsFrustumfANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_bounds#XrSpatialBoundsFrustumfANDROID) structure in the next chain.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_bounds#VUID-XrSpatialBoundsFrustumfANDROID-extension-notenabled) The `XR_ANDROID_spatial_discovery_bounds` extension **must** be enabled prior to using [XrSpatialBoundsFrustumfANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_bounds#XrSpatialBoundsFrustumfANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_bounds#VUID-XrSpatialBoundsFrustumfANDROID-type-type) `type` **must** be `XR_TYPE_SPATIAL_BOUNDS_FRUSTUMF_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_bounds#VUID-XrSpatialBoundsFrustumfANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_bounds#VUID-XrSpatialBoundsFrustumfANDROID-space-parameter) `space` **must** be a valid [XrSpace](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpace) handle

## Example

The following code demonstrates how to use spatial bounds to filter the discovery of spatial entities.

    // previously initialized & configured with the XR_SPATIAL_CAPABILITY_PLANE_TRACKING_EXT capability.
    XrSpatialContextEXT spatialContext;

    // Enumerate supported features for XR_SPATIAL_CAPABILITY_PLANE_TRACKING_EXT capability
    uint32_t featureCount = 0;
    CHK_XR(xrEnumerateSpatialCapabilityFeaturesEXT(instance, systemId, XR_SPATIAL_CAPABILITY_PLANE_TRACKING_EXT, 0, &featureCount, nullptr));
    std::vector<XrSpatialCapabilityFeatureEXT> fooFeatures(featureCount);
    CHK_XR(xrEnumerateSpatialCapabilityFeaturesEXT(instance, systemId, XR_SPATIAL_CAPABILITY_PLANE_TRACKING_EXT, featureCount, &featureCount, fooFeatures.data()));

    // Check if spatial sphere bounds filter is supported
    const auto supportsFeature = [&fooFeatures](XrSpatialCapabilityFeatureEXT feature) {
      return std::find(fooFeatures.begin(), fooFeatures.end(), feature) != fooFeatures.end();
    };

    const bool supportsSphereBoundsFilter = supportsFeature(XR_SPATIAL_CAPABILITY_FEATURE_SPHERE_BOUNDS_FILTER_ANDROID);

    // We want to look for entities in a sphere around the head with a radius of 2m.
    XrSpatialBoundsSpherefANDROID sphereBounds {
      .type = XR_TYPE_SPATIAL_BOUNDS_SPHEREF_ANDROID,
      .space = viewSpace,
      .time = predictedDisplayTime,
      .sphere = {
        .center = {
          .orientation = {
            .w = 1.0f,
          },
        },
        .radius = 2.0f,
      },
    };

    // We want to look for entities that have the following components.
    std::array<XrSpatialComponentTypeEXT, 1> snapshotComponents{XR_SPATIAL_COMPONENT_TYPE_BOUNDED_2D_EXT};

    XrSpatialDiscoverySnapshotCreateInfoEXT snapshotCreateInfo{
      .type = XR_TYPE_SPATIAL_DISCOVERY_SNAPSHOT_CREATE_INFO_EXT,
      .next = supportsSphereBoundsFilter ? &sphereBounds : nullptr,
      .componentTypeCount = snapshotComponents.size(),
      .componentTypes = snapshotComponents.data(),
    };

    XrFutureEXT future = XR_NULL_FUTURE_EXT;
    CHK_XR(xrCreateSpatialDiscoverySnapshotAsyncEXT(spatialContext, &snapshotCreateInfo, &future));

## New Structures

- Extending [XrSpatialDiscoverySnapshotCreateInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialDiscoverySnapshotCreateInfoEXT) :

  - [XrSpatialBoundsBoxfANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_bounds#XrSpatialBoundsBoxfANDROID)
  - [XrSpatialBoundsFrustumfANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_bounds#XrSpatialBoundsFrustumfANDROID)
  - [XrSpatialBoundsSpherefANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_bounds#XrSpatialBoundsSpherefANDROID)

## New Enum Constants

- `XR_ANDROID_SPATIAL_DISCOVERY_BOUNDS_EXTENSION_NAME`
- `XR_ANDROID_spatial_discovery_bounds_SPEC_VERSION`
- Extending [XrSpatialCapabilityFeatureEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityFeatureEXT) :

  - `XR_SPATIAL_CAPABILITY_FEATURE_BOX_BOUNDS_FILTER_ANDROID`
  - `XR_SPATIAL_CAPABILITY_FEATURE_FRUSTUM_BOUNDS_FILTER_ANDROID`
  - `XR_SPATIAL_CAPABILITY_FEATURE_SPHERE_BOUNDS_FILTER_ANDROID`
- Extending [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) :

  - `XR_TYPE_SPATIAL_BOUNDS_BOXF_ANDROID`
  - `XR_TYPE_SPATIAL_BOUNDS_FRUSTUMF_ANDROID`
  - `XR_TYPE_SPATIAL_BOUNDS_SPHEREF_ANDROID`

## Issues

- Why is the support for spatial bounds dependent on an [XrSpatialCapabilityFeatureEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityFeatureEXT) definition?

  - Resolved
  - Answer: Not every spatial capability is capable of supporting spatial bounds. An example of this is a hypothetical global container entity that does not have any spatial position or bounds of its own but merely helps collect and organize the other entities inside it. The [XrSpatialCapabilityFeatureEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityFeatureEXT) values enumerated by the capability helps inform the app about the support for spatial bounds filtering.

## Version History

- Revision 1, 2025-05-03 (Nihav Jain, Google)

  - Initial extension description