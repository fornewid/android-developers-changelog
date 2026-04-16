---
title: https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_component_subsumed_by
url: https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_component_subsumed_by
source: md.txt
---

### XR_ANDROID_spatial_component_subsumed_by

**Name String**

`XR_ANDROID_spatial_component_subsumed_by`

**Extension Type**

Instance extension

**Registered Extension Number**

792

**Revision**

1

**Ratification Status**

Not ratified

**Extension and Version Dependencies**

`XR_EXT_spatial_entity`  

and  

`XR_EXT_spatial_plane_tracking`

**Last Modified Date**

2025-08-19

**IP Status**

No known IP claims.

**Contributors**

Brian Chen, Google  

Kyle Chen, Google  

Levana Chen, Google  

Nihav Jain, Google  

Spencer Quin, Google

## Overview

This extension builds on `XR_EXT_spatial_entity` and provides a new component for `XR_SPATIAL_CAPABILITY_PLANE_TRACKING_EXT` , to expose the subsumed_by property.

When the runtime has acquired enough environment information to detect 2 tracked planes are actually the same, the subsumed_by component with the ID of one of the planes will be attached to the other.

This extension also introduces a new filter, which the application **can** chain to [XrSpatialDiscoverySnapshotCreateInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialDiscoverySnapshotCreateInfoEXT) to filter out any entities that has subsumed_by component attached to it.

### Permissions

Android applications **must** have the android.permission.SCENE_UNDERSTANDING_COARSE permission listed in their manifest as this extension tracks planes in the environment. The android.permission.SCENE_UNDERSTANDING_COARSE permission is considered a dangerous permission.

(protection level: dangerous)

## Runtime Support

If the runtime supports subumed_by, it **must** support plane tracking capability and indicating this by enumerating `XR_SPATIAL_CAPABILITY_PLANE_TRACKING_EXT` in [xrEnumerateSpatialCapabilitiesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrEnumerateSpatialCapabilitiesEXT) .

If the runtime provides subsumed_by, it **must** indicate this by enumerating `XR_SPATIAL_COMPONENT_TYPE_SUBSUMED_BY_ANDROID` as a supported component for `XR_SPATIAL_CAPABILITY_PLANE_TRACKING_EXT` capability in [xrEnumerateSpatialCapabilityComponentTypesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrEnumerateSpatialCapabilityComponentTypesEXT) .

All the component data of the `XR_SPATIAL_COMPONENT_TYPE_SUBSUMED_BY_ANDROID` attached entity **must** be identical to the entity that subsumes it.

## Subsumed By Component

### Component data

`XR_SPATIAL_COMPONENT_TYPE_SUBSUMED_BY_ANDROID` uses the `XrSpatialEntityIdEXT` structure for its data, which represents the ID of the subsuming entity.

### Component list struct to query data

The [XrSpatialComponentSubsumedByListANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_component_subsumed_by#XrSpatialComponentSubsumedByListANDROID) structure is defined as:

    typedef struct XrSpatialComponentSubsumedByListANDROID {
        XrStructureType          type;
        void*                    next;
        uint32_t                 subsumedUniqueIdCount;
        XrSpatialEntityIdEXT*    subsumedUniqueIds;
    } XrSpatialComponentSubsumedByListANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `subsumedUniqueIdCount` is a `uint32_t` describing the count of elements in the `subsumedUniqueIds` array.
- `subsumedUniqueIds` is an array of `XrSpatialEntityIdEXT` .

The application **can** query the subsumed_by component of the spatial entities in an [XrSpatialSnapshotEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialSnapshotEXT) by adding `XR_TYPE_SPATIAL_COMPONENT_SUBSUMED_BY_LIST_ANDROID` to the next chain of the [XrSpatialComponentDataQueryResultEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryResultEXT) .

The runtime **must** return `XR_ERROR_VALIDATION_FAILURE` from [xrQuerySpatialComponentDataEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrQuerySpatialComponentDataEXT) if `XR_TYPE_SPATIAL_COMPONENT_SUBSUMED_BY_LIST_ANDROID` is in the next chain of [XrSpatialComponentDataQueryResultEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryResultEXT) :: `next` but `XR_SPATIAL_COMPONENT_TYPE_SUBSUMED_BY_ANDROID` is not included in [XrSpatialComponentDataQueryConditionEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryConditionEXT) :: `componentTypes` .

The runtime **must** return `XR_ERROR_SIZE_INSUFFICIENT` from [xrQuerySpatialComponentDataEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrQuerySpatialComponentDataEXT) if `subsumedUniqueIdCount` is less than [XrSpatialComponentDataQueryResultEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryResultEXT) :: `entityIdCountOutput` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_component_subsumed_by#VUID-XrSpatialComponentSubsumedByListANDROID-extension-notenabled) The `XR_ANDROID_spatial_component_subsumed_by` extension **must** be enabled prior to using [XrSpatialComponentSubsumedByListANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_component_subsumed_by#XrSpatialComponentSubsumedByListANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_component_subsumed_by#VUID-XrSpatialComponentSubsumedByListANDROID-type-type) `type` **must** be `XR_TYPE_SPATIAL_COMPONENT_SUBSUMED_BY_LIST_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_component_subsumed_by#VUID-XrSpatialComponentSubsumedByListANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_component_subsumed_by#VUID-XrSpatialComponentSubsumedByListANDROID-subsumedUniqueIds-parameter) `subsumedUniqueIds` **must** be a pointer to an array of `subsumedUniqueIdCount` `XrSpatialEntityIdEXT` values
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_component_subsumed_by#VUID-XrSpatialComponentSubsumedByListANDROID-subsumedUniqueIdCount-arraylength) The `subsumedUniqueIdCount` parameter **must** be greater than `0`

### Configuration

If `XR_SPATIAL_COMPONENT_TYPE_SUBSUMED_BY_ANDROID` is enumerated in [XrSpatialCapabilityComponentTypesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityComponentTypesEXT) :: `componentTypes` for `XR_SPATIAL_CAPABILITY_PLANE_TRACKING_EXT` capability, the application **can** enable it by including the enum in the [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityConfigurationBaseHeaderEXT) :: `enabledComponents` list of the [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityConfigurationBaseHeaderEXT) derived structure of the capability that supports this component.

### Filter Subsumed Entities

The [XrSpatialDiscoveryUniqueEntitiesFilterANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_component_subsumed_by#XrSpatialDiscoveryUniqueEntitiesFilterANDROID) structure is defined as:

    typedef struct XrSpatialDiscoveryUniqueEntitiesFilterANDROID {
        XrStructureType    type;
        const void*        next;
    } XrSpatialDiscoveryUniqueEntitiesFilterANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.

The application **can** include [XrSpatialDiscoveryUniqueEntitiesFilterANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_component_subsumed_by#XrSpatialDiscoveryUniqueEntitiesFilterANDROID) in the next chain of [XrSpatialDiscoverySnapshotCreateInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialDiscoverySnapshotCreateInfoEXT) to get a snapshot with entities that are not subsumed by another entity.

If applications chain [XrSpatialDiscoveryUniqueEntitiesFilterANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_component_subsumed_by#XrSpatialDiscoveryUniqueEntitiesFilterANDROID) to [XrSpatialDiscoverySnapshotCreateInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialDiscoverySnapshotCreateInfoEXT) while including `XR_SPATIAL_COMPONENT_TYPE_SUBSUMED_BY_ANDROID` component in the [XrSpatialDiscoverySnapshotCreateInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialDiscoverySnapshotCreateInfoEXT) :: `componentTypes` , the runtime **must** return `XR_ERROR_VALIDATION_FAILURE` .

If application chains [XrSpatialDiscoveryUniqueEntitiesFilterANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_component_subsumed_by#XrSpatialDiscoveryUniqueEntitiesFilterANDROID) to [XrSpatialDiscoverySnapshotCreateInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialDiscoverySnapshotCreateInfoEXT) but does not list any components in [XrSpatialDiscoverySnapshotCreateInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialDiscoverySnapshotCreateInfoEXT) :: `componentTypes` , the runtime **must** include all the spatial entities in the snapshot that have the set of components which are enumerated in [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityConfigurationBaseHeaderEXT) :: `enabledComponents` for the capabilities configured for spatialContext, except entities that have the `XR_SPATIAL_COMPONENT_TYPE_SUBSUMED_BY_ANDROID` component.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_component_subsumed_by#VUID-XrSpatialDiscoveryUniqueEntitiesFilterANDROID-extension-notenabled) The `XR_ANDROID_spatial_component_subsumed_by` extension **must** be enabled prior to using [XrSpatialDiscoveryUniqueEntitiesFilterANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_component_subsumed_by#XrSpatialDiscoveryUniqueEntitiesFilterANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_component_subsumed_by#VUID-XrSpatialDiscoveryUniqueEntitiesFilterANDROID-type-type) `type` **must** be `XR_TYPE_SPATIAL_DISCOVERY_UNIQUE_ENTITIES_FILTER_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_component_subsumed_by#VUID-XrSpatialDiscoveryUniqueEntitiesFilterANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)

## Example code

### Configure Plane Tracking Capability

The following example code demonstrates how to create a spatial context with `XR_SPATIAL_CAPABILITY_PLANE_TRACKING_EXT` capability that supports subsumed_by.

    // Check runtime supported capabilities
    uint32_t capabilityCount;
    CHK_XR(xrEnumerateSpatialCapabilitiesEXT(instance, systemId, 0, &capabilityCount, nullptr));
    std::vector<XrSpatialCapabilityEXT> capabilities(capabilityCount);
    CHK_XR(xrEnumerateSpatialCapabilitiesEXT(instance, systemId, capabilityCount, &capabilityCount, capabilities.data()));

    if (std::find(capabilities.begin(), capabilities.end(), XR_SPATIAL_CAPABILITY_PLANE_TRACKING_EXT) == capabilities.end()) {
      return;
    }

    std::vector<XrSpatialComponentTypeEXT> planeTrackingComponents {
      XR_SPATIAL_COMPONENT_TYPE_BOUNDED_2D_EXT,
      XR_SPATIAL_COMPONENT_TYPE_PLANE_ALIGNMENT_EXT,
      XR_SPATIAL_COMPONENT_TYPE_SUBSUMED_BY_ANDROID,
    };

    // Create capability config for plane tracking
    XrSpatialCapabilityConfigurationPlaneTrackingEXT planeTrackingConfig {
      .type = XR_TYPE_SPATIAL_CAPABILITY_CONFIGURATION_PLANE_TRACKING_EXT,
      .next = nullptr,
      .capability = XR_SPATIAL_CAPABILITY_PLANE_TRACKING_EXT,
      .enabledComponentCount = (uint32_t)planeTrackingComponents.size(),
      .enabledComponents = planeTrackingComponents.data(),
    };

    // Create spatial context
    std::vector<const XrSpatialCapabilityConfigurationBaseHeaderEXT*> capabilityConfigs;
    capabilityConfigs.push_back(reinterpret_cast<const XrSpatialCapabilityConfigurationBaseHeaderEXT*>(&planeTrackingConfig));

    XrSpatialContextCreateInfoEXT contextCreateInfo{
      .type = XR_TYPE_SPATIAL_CONTEXT_CREATE_INFO_EXT,
      .next = nullptr,
      .capabilityConfigCount = (uint32_t)capabilityConfigs.size(),
      .capabilityConfigs = capabilityConfigs.data(),
    };

    CHK_XR(xrCreateSpatialContextAsyncEXT(session, &contextCreateInfo, &future))

    // Completes creating spatial context
    XrCreateSpatialContextCompletionEXT contextCompletion{
    XR_TYPE_CREATE_SPATIAL_CONTEXT_COMPLETION_EXT};

    CHK_XR(xrCreateSpatialContextCompleteEXT(session, future, &contextCompletion))

### Query Component Data

The following example code demonstrates how to query subsumed_by component data from context configured with `XR_SPATIAL_CAPABILITY_PLANE_TRACKING_EXT` .

    // Create Discovery Snapshot
    XrSpatialDiscoverySnapshotCreateInfoEXT discoverySnapshotCreateInfo {
      .type = XR_TYPE_SPATIAL_DISCOVERY_SNAPSHOT_CREATE_INFO_EXT,
    };

    CHK_XR(xrCreateSpatialDiscoverySnapshotAsyncEXT (
    spatialContext, &discoverySnapshotCreateInfo, &future));

    // Poll the state till snapshot it's ready.
    waitUntilReady(future);

    // Complete async operation.
    XrCreateSpatialDiscoverySnapshotCompletionInfoEXT
      createSnapshotCompletionInfo {
        .type   = XR_TYPE_CREATE_SPATIAL_DISCOVERY_SNAPSHOT_COMPLETION_INFO_EXT,
        .baseSpace = space,
        .time      = updateTime,
        .future    = future,
      };

    XrCreateSpatialDiscoverySnapshotCompletionEXT completion {
      XR_TYPE_CREATE_SPATIAL_DISCOVERY_SNAPSHOT_COMPLETION_EXT};

    CHK_XR(xrCreateSpatialDiscoverySnapshotCompleteEXT(
               spatialContext, &createSnapshotCompletionInfo,
               &completion));

    if(completion.futureResult != XR_SUCCESS) return;

    // Query subsumed_by components
    std::array<XrSpatialComponentTypeEXT, 1> enabledComponents = {
      XR_SPATIAL_COMPONENT_TYPE_SUBSUMED_BY_ANDROID
    };

    XrSpatialComponentDataQueryConditionEXT queryCond {
      .type = XR_TYPE_SPATIAL_COMPONENT_DATA_QUERY_CONDITION_EXT,
      .componentTypeCount = 1,
      .componentTypes     = enabledComponents.data(),
    };

    XrSpatialComponentDataQueryResultEXT queryResult {
      .type = XR_TYPE_SPATIAL_COMPONENT_DATA_QUERY_RESULT_EXT,
    };

    CHK_XR(xrQuerySpatialComponentDataEXT(
               completion.snapshot, &queryCond, &queryResult));

    // Query again with allocated memory
    std::vector<XrSpatialEntityIdEXT> subsumedUniqueIds;
    subsumedUniqueIds.resize(queryResult.entityIdCountOutput);
    XrSpatialComponentSubsumedByListANDROID subsumedByList {
      .type = XR_TYPE_SPATIAL_COMPONENT_SUBSUMED_BY_LIST_ANDROID,
      .subsumedUniqueIdCount = static_cast<uint32_t>(subsumedUniqueIds.size()),
      .subsumedUniqueIds = subsumedUniqueIds.data(),
    };

    queryResult.next = &subsumedByList;
    CHK_XR(xrQuerySpatialComponentDataEXT(
               completion.snapshot, &queryCond, &queryResult));

    std::vector<XrSpatialEntityEXT> subsumedEntities;
    for(uint32_t i = 0; i < queryResult.entityIdCountOutput; ++i) {
        // access planes[i] for merged plane id
        XrSpatialEntityIdEXT entityId = queryResult.entityIds[i];
        XrSpatialEntityIdEXT subsumedUniqueId = subsumedUniqueIds[i];

        // create handle via entityId
      XrSpatialEntityFromIdCreateInfoEXT entityCreateInfo {
        .type = XR_TYPE_SPATIAL_ENTITY_FROM_ID_CREATE_INFO_EXT,
        .entityId = entityId,
      };

      XrSpatialEntityEXT entity = XR_NULL_HANDLE;
      xrCreateSpatialEntityFromIdEXT(spatialContext, &entityCreateInfo, &entity);

      subsumedEntities.push_back(entity);
    }

    // Cleanup
    xrDestroySpatialSnapshotEXT(completion.snapshot);

### Filter Out Subsumed Entities

The following example code demonstrates how to filter out entities with subsumed_by component attached from discovery snapshot using the filter, as well as queryc the entity id of the subsuming entities.

    // Init filter
    XrSpatialDiscoveryUniqueEntitiesFilterANDROID filter {
      .type = XR_TYPE_SPATIAL_DISCOVERY_UNIQUE_ENTITIES_FILTER_ANDROID,
    };

    // Chain filter to the snapshot create info
    // WARNING: Chain the filter while include subsumed_by component in the
    // componentTypes is invalid
    XrSpatialDiscoverySnapshotCreateInfoEXT discoverySnapshotCreateInfo {
      .type = XR_TYPE_SPATIAL_DISCOVERY_SNAPSHOT_CREATE_INFO_EXT,
      .next = &filter
    };

    waitUntilReady(future);

    // Complete async operation.
    XrCreateSpatialDiscoverySnapshotCompletionInfoEXT
      createSnapshotCompletionInfo {
        .type   = XR_TYPE_CREATE_SPATIAL_DISCOVERY_SNAPSHOT_COMPLETION_INFO_EXT,
        .baseSpace = space,
        .time      = updateTime,
        .future    = future,
      };

    XrCreateSpatialDiscoverySnapshotCompletionEXT completion {
      XR_TYPE_CREATE_SPATIAL_DISCOVERY_SNAPSHOT_COMPLETION_EXT};

    CHK_XR(xrCreateSpatialDiscoverySnapshotCompleteEXT(
               spatialContext, &createSnapshotCompletionInfo,
               &completion));

    if(completion.futureResult != XR_SUCCESS) return;

    // Subsumed entities has already been filtered out in this snapshot,now query
    // Bounded2D to render subsuming planes
    std::vector<XrSpatialComponentTypeEXT> queryComponents {
      XR_SPATIAL_COMPONENT_TYPE_BOUNDED_2D_EXT,
    };

    XrSpatialComponentDataQueryConditionEXT queryCond {
      .type = XR_TYPE_SPATIAL_COMPONENT_DATA_QUERY_CONDITION_EXT,
      .componentTypeCount = 1,
      .componentTypes     = queryComponents.data(),
    };

    XrSpatialComponentDataQueryResultEXT queryResult {
      .type = XR_TYPE_SPATIAL_COMPONENT_DATA_QUERY_RESULT_EXT,
    };

    CHK_XR(xrQuerySpatialComponentDataEXT(
               completion.snapshot, &queryCond, &queryResult));

    // Chain Bounded2D list
    std::vector<XrSpatialBounded2DDataEXT> bounded2dData;
    bounded2dData.resize(queryResult.entityIdCountOutput);

    XrSpatialComponentBounded2DListEXT bounded2dList {
      .type = XR_TYPE_SPATIAL_COMPONENT_BOUNDED_2D_LIST_EXT,
      .boundCount = static_cast<uint32_t>(bounded2dData.size()),
      .bounds = bounded2dData.data(),
    };

    // Query again
    queryResult.next = &bounded2dList;
    CHK_XR(xrQuerySpatialComponentDataEXT(
               completion.snapshot, &queryCond, &queryResult));

    std::vector<XrSpatialEntityEXT> subsumingPlanes;
    for(uint32_t i = 0; i < queryResult.entityIdCountOutput; ++i) {
      // access planes[i] for merged plane id
      XrSpatialEntityIdEXT entityId = queryResult.entityIds[i];

      // create handle via entityId.
      XrSpatialEntityFromIdCreateInfoEXT entityCreateInfo {
        .type = XR_TYPE_SPATIAL_ENTITY_FROM_ID_CREATE_INFO_EXT,
        .entityId = entityId,
      };

      XrSpatialEntityEXT entity = XR_NULL_HANDLE;
      xrCreateSpatialEntityFromIdEXT(spatialContext, &entityCreateInfo, &entity);

      subsumingPlanes.push_back(entity);
    }

    // Cleanup
    xrDestroySpatialSnapshotEXT(completion.snapshot);

## New Structures

- Extending [XrSpatialComponentDataQueryResultEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryResultEXT) :

  - [XrSpatialComponentSubsumedByListANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_component_subsumed_by#XrSpatialComponentSubsumedByListANDROID)
- Extending [XrSpatialDiscoverySnapshotCreateInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialDiscoverySnapshotCreateInfoEXT) :

  - [XrSpatialDiscoveryUniqueEntitiesFilterANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_component_subsumed_by#XrSpatialDiscoveryUniqueEntitiesFilterANDROID)

## New Enum Constants

- `XR_ANDROID_SPATIAL_COMPONENT_SUBSUMED_BY_EXTENSION_NAME`
- `XR_ANDROID_spatial_component_subsumed_by_SPEC_VERSION`
- Extending [XrSpatialComponentTypeEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentTypeEXT) :

  - `XR_SPATIAL_COMPONENT_TYPE_SUBSUMED_BY_ANDROID`
- Extending [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) :

  - `XR_TYPE_SPATIAL_COMPONENT_SUBSUMED_BY_LIST_ANDROID`
  - `XR_TYPE_SPATIAL_DISCOVERY_UNIQUE_ENTITIES_FILTER_ANDROID`

## Issues

## Version History

- Revision 1, 2025-11-19 (Brian Chen)

  - Initial extension description.