---
title: https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_entity_bound_anchor
url: https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_entity_bound_anchor
source: md.txt
---

### XR_ANDROID_spatial_entity_bound_anchor

**Name String**

`XR_ANDROID_spatial_entity_bound_anchor`

**Extension Type**

Instance extension

**Registered Extension Number**

791

**Revision**

2

**Ratification Status**

Not ratified

**Extension and Version Dependencies**

`XR_EXT_spatial_anchor`

**Last Modified Date**

2025-08-18

**IP Status**

No known IP claims.

**Contributors**

YuSheng Chang, Google  

Kyle Chen, Google  

Nihav Jain, Google  

Levana Chen, Google  

Spencer Quin, Google

## Overview

This extension allows applications to create and attach anchors to spatial entities, which are called "entity-bound anchors" in this extension.

An entity-bound anchor is represented as a spatial entity with (or "that has") the `XR_SPATIAL_COMPONENT_TYPE_ANCHOR_EXT` component and the `XR_SPATIAL_COMPONENT_TYPE_PARENT_EXT` component. The `XR_SPATIAL_COMPONENT_TYPE_PARENT_EXT` component stores the `XrSpatialEntityIdEXT` of the parent entity that the anchor is attached to.

The pose of an entity-bound anchor is always represented by a fixed offset from its parent entity, which is thought of as the "base" of the anchor. For example, imagine a user has a virtual picture frame attached to a wall, the user uses an entity-bound anchor to represent the virtual picture frame, and attaches it to the wall entity. With that, the relative position between the wall and the picture frame is always consistent as the tracking estimates of the physical wall improve.

## Runtime Support

A runtime **must** support at least one spatial tracking extension, e.g. `XR_EXT_spatial_plane_tracking` . If the runtime supports spatial entity bound anchor, it **must** provide at least one attachable component by enumerating the [xrEnumerateSpatialAnchorAttachableComponentsANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_entity_bound_anchor#xrEnumerateSpatialAnchorAttachableComponentsANDROID) function. The application **can** enumerate the attachable components by using [xrEnumerateSpatialAnchorAttachableComponentsANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_entity_bound_anchor#xrEnumerateSpatialAnchorAttachableComponentsANDROID) .

The [xrEnumerateSpatialAnchorAttachableComponentsANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_entity_bound_anchor#xrEnumerateSpatialAnchorAttachableComponentsANDROID) function is defined as:

    XrResult xrEnumerateSpatialAnchorAttachableComponentsANDROID(
        XrInstance                                  instance,
        XrSystemId                                  systemId,
        uint32_t                                    attachableComponentCapacityInput,
        uint32_t*                                   attachableComponentCountOutput,
        XrSpatialComponentTypeEXT*                  attachableComponents);

### Parameter Descriptions

- `instance` is a handle to an [XrInstance](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrInstance) .
- `systemId` is the `XrSystemId` whose spatial persistence stores will be enumerated.
- `attachableComponentCapacityInput` is the capacity of the `attachableComponents` array, or 0 to indicate a request to retrieve the required capacity.
- `attachableComponentCountOutput` is the number of attachable components, or the required capacity in the case that `attachableComponentCapacityInput` is insufficient.
- `attachableComponents` is an array of [XrSpatialComponentTypeEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentTypeEXT) . It **can** be `NULL` if `attachableComponentCapacityInput` is 0.
- See [Buffer Size Parameters](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-buffer-size-parameters) chapter for a detailed description of retrieving the required `attachableComponents` size.

Runtimes **must** always return identical buffer contents from this enumeration for the given `systemId` for the lifetime of the instance.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_entity_bound_anchor#VUID-xrEnumerateSpatialAnchorAttachableComponentsANDROID-extension-notenabled) The `XR_ANDROID_spatial_entity_bound_anchor` extension **must** be enabled prior to calling [xrEnumerateSpatialAnchorAttachableComponentsANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_entity_bound_anchor#xrEnumerateSpatialAnchorAttachableComponentsANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_entity_bound_anchor#VUID-xrEnumerateSpatialAnchorAttachableComponentsANDROID-instance-parameter) `instance` **must** be a valid [XrInstance](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrInstance) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_entity_bound_anchor#VUID-xrEnumerateSpatialAnchorAttachableComponentsANDROID-attachableComponentCountOutput-parameter) `attachableComponentCountOutput` **must** be a pointer to a `uint32_t` value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_entity_bound_anchor#VUID-xrEnumerateSpatialAnchorAttachableComponentsANDROID-attachableComponents-parameter) If `attachableComponentCapacityInput` is not `0` , `attachableComponents` **must** be a pointer to an array of `attachableComponentCapacityInput` [XrSpatialComponentTypeEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentTypeEXT) values

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

## Creating a spatial entity-bound anchor

Applications use the [xrCreateSpatialAnchorEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateSpatialAnchorEXT) function to create an anchor. If an application wants to create an entity-bound anchor that is attached to a spatial entity, it **can** chain an [XrSpatialAnchorParentANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_entity_bound_anchor#XrSpatialAnchorParentANDROID) structure to the next pointer of the [XrSpatialAnchorCreateInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialAnchorCreateInfoEXT) structure when calling the [xrCreateSpatialAnchorEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateSpatialAnchorEXT) function.

The [XrSpatialAnchorParentANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_entity_bound_anchor#XrSpatialAnchorParentANDROID) structure is defined as:

    typedef struct XrSpatialAnchorParentANDROID {
        XrStructureType         type;
        const void*             next;
        XrSpatialEntityIdEXT    parentId;
    } XrSpatialAnchorParentANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `parentId` is the `XrSpatialEntityIdEXT` of the entity that the anchor will be attached to.

The runtime **must** guaranteed that the distance between the parent entity and the anchor is always consistent, where the distance is the anchor's pose to the nearest surface of the parent entity along the surface's normal. The pose of the anchor is updated based on the parent entity's position and the distance to the parent entity's surface regardless of how many attachable components the parent entity has.

The runtime **must** return `XR_ERROR_SPATIAL_ENTITY_ID_INVALID_EXT` from [xrCreateSpatialAnchorEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateSpatialAnchorEXT) if [XrSpatialAnchorParentANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_entity_bound_anchor#XrSpatialAnchorParentANDROID) ::parentId is not a valid ID for [xrCreateSpatialAnchorEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateSpatialAnchorEXT) :: `spatialContext` .

The runtime **must** return `XR_ERROR_SPATIAL_ANCHOR_ATTACHABLE_COMPONENT_NOT_FOUND_ANDROID` from [xrCreateSpatialAnchorEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateSpatialAnchorEXT) if none of the components enumerated by [xrEnumerateSpatialAnchorAttachableComponentsANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_entity_bound_anchor#xrEnumerateSpatialAnchorAttachableComponentsANDROID) are on the parent entity.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_entity_bound_anchor#VUID-XrSpatialAnchorParentANDROID-extension-notenabled) The `XR_ANDROID_spatial_entity_bound_anchor` extension **must** be enabled prior to using [XrSpatialAnchorParentANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_entity_bound_anchor#XrSpatialAnchorParentANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_entity_bound_anchor#VUID-XrSpatialAnchorParentANDROID-type-type) `type` **must** be `XR_TYPE_SPATIAL_ANCHOR_PARENT_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_entity_bound_anchor#VUID-XrSpatialAnchorParentANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)

## Example code

### Create spatial entity-bound anchor

The following example code demonstrates how to create an entity-bound anchor and attach it to a spatial plane tracking entity.

    XrFutureEXT future {XR_NULL_FUTURE_EXT};

    std::vector<XrSpatialEntityEXT> entityBoundAnchorEntities;

    // We want to look for entities that have the plane tracking components.
    std::vector<XrSpatialComponentTypeEXT> snapshotComponents = {
      XR_SPATIAL_COMPONENT_TYPE_BOUNDED_2D_EXT,
      XR_SPATIAL_COMPONENT_TYPE_PLANE_ALIGNMENT_EXT,
    };

    auto discoverSpatialEntities = [&](XrSpatialContextEXT spatialContext, XrTime time) {
      XrSpatialDiscoverySnapshotCreateInfoEXT snapshotCreateInfo{
        .type = XR_TYPE_SPATIAL_DISCOVERY_SNAPSHOT_CREATE_INFO_EXT,
        .componentTypeCount = static_cast<uint32_t>(snapshotComponents.size()),
        .componentTypes = snapshotComponents.data(),
      };
      CHK_XR(xrCreateSpatialDiscoverySnapshotAsyncEXT(spatialContext, &snapshotCreateInfo, &future));

      waitUntilReady(future);

      XrCreateSpatialDiscoverySnapshotCompletionInfoEXT completionInfo{
        .type = XR_TYPE_CREATE_SPATIAL_DISCOVERY_SNAPSHOT_COMPLETION_INFO_EXT,
        .baseSpace = localSpace,
        .time = time,
        .future = future,
      };

      XrCreateSpatialDiscoverySnapshotCompletionEXT completion{
        .type = XR_TYPE_CREATE_SPATIAL_DISCOVERY_SNAPSHOT_COMPLETION_EXT,
      };
      CHK_XR(xrCreateSpatialDiscoverySnapshotCompleteEXT(spatialContext, &completionInfo, &completion));
      if (completion.futureResult == XR_SUCCESS) {

        XrSpatialComponentDataQueryConditionEXT queryCond{
          .type = XR_TYPE_SPATIAL_COMPONENT_DATA_QUERY_CONDITION_EXT,
          .componentTypeCount = static_cast<uint32_t>(snapshotComponents.size()),
          .componentTypes = snapshotComponents.data(),
        };

        XrSpatialComponentDataQueryResultEXT queryResult{
          .type = XR_TYPE_SPATIAL_COMPONENT_DATA_QUERY_RESULT_EXT,
        };
        CHK_XR(xrQuerySpatialComponentDataEXT(completion.snapshot, &queryCond, &queryResult));

        std::vector<XrSpatialEntityIdEXT> entityIds(queryResult.entityIdCountOutput);
        std::vector<XrSpatialEntityTrackingStateEXT> entityStates(queryResult.entityIdCountOutput);
        queryResult.entityIdCapacityInput = entityIds.size();
        queryResult.entityIds = entityIds.data();
        queryResult.entityStateCapacityInput = entityStates.size();
        queryResult.entityStates = entityStates.data();

        std::vector<XrSpatialBounded2DDataEXT> bounded2D(queryResult.entityIdCountOutput);
        XrSpatialComponentBounded2DListEXT bounded2DList{
          .type = XR_TYPE_SPATIAL_COMPONENT_BOUNDED_2D_LIST_EXT,
          .boundCount = static_cast<uint32_t>(bounded2D.size()),
          .bounds = bounded2D.data(),
        };
        queryResult.next = &bounded2DList;

        CHK_XR(xrQuerySpatialComponentDataEXT(completion.snapshot, &queryCond, &queryResult));

        entityBoundAnchorEntities.reserve(queryResult.entityIdCountOutput);

        // Create anchors attached to the plane entities
        for (int32_t i = 0; i < queryResult.entityIdCountOutput; ++i) {
          if (entityStates[i] != XR_SPATIAL_ENTITY_TRACKING_STATE_TRACKING_EXT) {
            continue;
          }

          // Parent ID info the chained to spatial anchor create info next
          XrSpatialAnchorParentANDROID parentIdCreateInfo{
            .type = XR_TYPE_SPATIAL_ANCHOR_PARENT_ANDROID,
            .parentId = entityIds[i],
          };

          // spatial anchor create info
          XrSpatialAnchorCreateInfoEXT createInfo{
            .type = XR_TYPE_SPATIAL_ANCHOR_CREATE_INFO_EXT,
            // assign Parent ID to anchor create info next, and the pose to the bounded2D center
            .next = &parentIdCreateInfo,
            .baseSpace = localSpace,
            .time = time,
            .pose = bounded2D[i].center,
          };

          XrSpatialEntityIdEXT entityBoundAnchorEntityId {XR_NULL_SPATIAL_ENTITY_ID_EXT};
          XrSpatialEntityEXT entityBoundAnchorEntity {XR_NULL_HANDLE};
          CHK_XR(xrCreateSpatialAnchorEXT(spatialContext, &createInfo, &entityBoundAnchorEntityId, &entityBoundAnchorEntity));

          entityBoundAnchorEntities.push_back(entityBoundAnchorEntity);
        }

        CHK_XR(xrDestroySpatialSnapshotEXT(completion.snapshot));
      }
    };

    while (1) {
      // ...
      // For every frame in frame loop
      // ...

      XrFrameState frameState;  // previously returned from xrWaitFrame
      const XrTime time = frameState.predictedDisplayTime;

      // Poll for the XR_TYPE_EVENT_DATA_SPATIAL_DISCOVERY_RECOMMENDED_EXT event
      XrEventDataBuffer event = {
        .type = XR_TYPE_EVENT_DATA_BUFFER,
      };
      XrResult result = xrPollEvent(instance, &event);
      if (result == XR_SUCCESS) {
          if (event.type == XR_TYPE_EVENT_DATA_SPATIAL_DISCOVERY_RECOMMENDED_EXT) {
                  const XrEventDataSpatialDiscoveryRecommendedEXT& eventdata =
                      *reinterpret_cast<XrEventDataSpatialDiscoveryRecommendedEXT*>(&event);
                  // Discover spatial entities for the context that we received the "discovery
                  // recommended" event for.
                  discoverSpatialEntities(eventdata.spatialContext, time);
                  break;
          }
      }

      // ...
      // Finish frame loop
      // ...
    }

### Get entity-bound anchor pose and parent entity ID

The following example code demonstrates how to get the pose of an entity-bound anchor and the ID of its parent entity.

    std::vector<XrSpatialEntityEXT> entities;

    auto updateEntityBoundAnchorInfo = [&](XrSpatialContextEXT spatialContext, XrTime time) {
        // We want to get updated data for all components of the entities, so skip specifying componentTypes.
        XrSpatialUpdateSnapshotCreateInfoEXT snapshotCreateInfo{
          .type = XR_TYPE_SPATIAL_UPDATE_SNAPSHOT_CREATE_INFO_EXT,
          .entityCount = static_cast<uint32_t>(entities.size()),
          .entities = entities.data(),
          .baseSpace = localSpace,
          .time = time,
        };

        XrSpatialSnapshotEXT snapshot {XR_NULL_HANDLE};
        CHK_XR(xrCreateSpatialUpdateSnapshotEXT(spatialContext, &snapshotCreateInfo, &snapshot));

        // Query for the entities that have the anchor component and parent component on them.
        std::array<XrSpatialComponentTypeEXT, 2> componentsToQuery {XR_SPATIAL_COMPONENT_TYPE_ANCHOR_EXT, XR_SPATIAL_COMPONENT_TYPE_PARENT_EXT};
        XrSpatialComponentDataQueryConditionEXT queryCond{
          .type = XR_TYPE_SPATIAL_COMPONENT_DATA_QUERY_CONDITION_EXT,
          .componentTypeCount = componentsToQuery.size(),
          .componentTypes = componentsToQuery.data(),
        };

        XrSpatialComponentDataQueryResultEXT queryResult{
          .type = XR_TYPE_SPATIAL_COMPONENT_DATA_QUERY_RESULT_EXT,
        };
        CHK_XR(xrQuerySpatialComponentDataEXT(snapshot, &queryCond, &queryResult));

        std::vector<XrSpatialEntityIdEXT> entityIds(queryResult.entityIdCountOutput);
        std::vector<XrSpatialEntityTrackingStateEXT> entityStates(queryResult.entityIdCountOutput);
        queryResult.entityIdCapacityInput = entityIds.size();
        queryResult.entityIds = entityIds.data();
        queryResult.entityStateCapacityInput = entityStates.size();
        queryResult.entityStates = entityStates.data();

        // query for the pose data
        std::vector<XrPosef> locations(queryResult.entityIdCountOutput);
        XrSpatialComponentAnchorListEXT locationList{
          .type = XR_TYPE_SPATIAL_COMPONENT_ANCHOR_LIST_EXT,
          .locationCount = static_cast<uint32_t>(locations.size()),
          .locations = locations.data(),
        };
        queryResult.next = &locationList;

        // query for the parent entity ID data
        std::vector<XrSpatialEntityIdEXT> parentIds(queryResult.entityIdCountOutput);
        XrSpatialComponentParentListEXT parentList{
          .type = XR_TYPE_SPATIAL_COMPONENT_PARENT_LIST_EXT,
          .parentCount = static_cast<uint32_t>(parentIds.size()),
          .parents = parentIds.data(),
        };
        queryResult.next = &parentList;

        CHK_XR(xrQuerySpatialComponentDataEXT(snapshot, &queryCond, &queryResult));

        for (int32_t i = 0; i < queryResult.entityIdCountOutput; ++i) {
          if (entityStates[i] == XR_SPATIAL_ENTITY_TRACKING_STATE_TRACKING_EXT) {
            // Pose for entity entityIds[i] is locations[i].
            // Parent entity ID for entity entityIds[i] is parentIds[i].
          }
        }

        CHK_XR(xrDestroySpatialSnapshotEXT(snapshot));
    };

    while (1) {
      // ...
      // For every frame in frame loop
      // ...

      XrFrameState frameState;  // previously returned from xrWaitFrame
      const XrTime time = frameState.predictedDisplayTime;

      updateEntityBoundAnchorInfo(spatialContext, time);

      // ...
      // Finish frame loop
      // ...
    }

### Enumerate attachable Components and check entity bound anchor capability

The following example code demonstrates how to enumerate the attachable components and check if the runtime supports entity bound anchor capability.

    // Check spatial capability
    uint32_t capabilityCount = 0;
    CHK_XR(xrEnumerateSpatialCapabilitiesEXT(instance, systemId, 0, &capabilityCount, nullptr));
    std::vector<XrSpatialCapabilityEXT> capabilities(capabilityCount);
    CHK_XR(xrEnumerateSpatialCapabilitiesEXT(instance, systemId, capabilityCount, &capabilityCount, capabilities.data()));

    // Check if anchor capability is supported
    if (std::find(capabilities.begin(), capabilities.end(), XR_SPATIAL_CAPABILITY_ANCHOR_EXT) == capabilities.end()) {
      return;
    }

    // Check if plane tracking capability is supported
    if (std::find(capabilities.begin(), capabilities.end(), XR_SPATIAL_CAPABILITY_PLANE_TRACKING_EXT) == capabilities.end()) {
      return;
    }

    // The supported spatial tracking components
    std::vector<XrSpatialComponentTypeEXT> spatialTrackingCapabilityComponents;

    // Enumerate supported components for plane tracking capability
    XrSpatialCapabilityComponentTypesEXT planeComponents{
      .type = XR_TYPE_SPATIAL_CAPABILITY_COMPONENT_TYPES_EXT,
    };
    CHK_XR(xrEnumerateSpatialCapabilityComponentTypesEXT(instance, systemId, XR_SPATIAL_CAPABILITY_PLANE_TRACKING_EXT, &planeComponents));
    std::vector<XrSpatialComponentTypeEXT> planeCapabilityComponents(planeComponents.componentTypeCountOutput);
    planeComponents.componentTypes = planeCapabilityComponents.data();
    CHK_XR(xrEnumerateSpatialCapabilityComponentTypesEXT(instance, systemId, XR_SPATIAL_CAPABILITY_PLANE_TRACKING_EXT, &planeComponents));

    // Add plane supported components to spatial tracking supported components
    spatialTrackingCapabilityComponents.insert(spatialTrackingCapabilityComponents.end(), planeCapabilityComponents.begin(), planeCapabilityComponents.end());

    // Enumerate supported attachable components for anchor
    uint32_t attachableComponentCount = 0;
    CHK_XR(xrEnumerateSpatialAnchorAttachableComponentsANDROID(instance, systemId, 0, &attachableComponentCount, nullptr));
    std::vector<XrSpatialComponentTypeEXT> attachableComponents(attachableComponentCount);
    CHK_XR(xrEnumerateSpatialAnchorAttachableComponentsANDROID(instance, systemId, attachableComponentCount, &attachableComponentCount, attachableComponents.data()));

    // Check if at least one spatial tracking component is supported
    const auto supportsComponent = [&spatialTrackingCapabilityComponents](XrSpatialComponentTypeEXT component) {
      return std::find(spatialTrackingCapabilityComponents.begin(), spatialTrackingCapabilityComponents.end(), component) != spatialTrackingCapabilityComponents.end();
    };

    bool atLeastOneComponentSupported = false;
    for (int32_t i = 0; i < attachableComponentCount; ++i) {
      if(supportsComponent(attachableComponents[i])) {
        atLeastOneComponentSupported = true;
        break;
      }
    }

    // No spatial tracking component supported for anchor attachment
    if(!atLeastOneComponentSupported) return;

    // ...
    // Create spatial entity anchors and get their latest pose in the frame loop.
    // ...

## New Commands

- [xrEnumerateSpatialAnchorAttachableComponentsANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_entity_bound_anchor#xrEnumerateSpatialAnchorAttachableComponentsANDROID)

## New Structures

- Extending [XrSpatialAnchorCreateInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialAnchorCreateInfoEXT) :

  - [XrSpatialAnchorParentANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_entity_bound_anchor#XrSpatialAnchorParentANDROID)

## New Enum Constants

- `XR_ANDROID_SPATIAL_ENTITY_BOUND_ANCHOR_EXTENSION_NAME`
- `XR_ANDROID_spatial_entity_bound_anchor_SPEC_VERSION`
- Extending [XrResult](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrResult) :

  - `XR_ERROR_SPATIAL_ANCHOR_ATTACHABLE_COMPONENT_NOT_FOUND_ANDROID`
- Extending [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) :

  - `XR_TYPE_SPATIAL_ANCHOR_PARENT_ANDROID`

## Issues

## Version History

- Revision 1, 2025-08-18 (YuSheng Chang)

  - Initial extension description.
- Revision 2, 2025-12-16 (Kyle Chen)

  - Add more prescriptive language to certain behaviors of the API.
  - Add the example code of [xrEnumerateSpatialAnchorAttachableComponentsANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_entity_bound_anchor#xrEnumerateSpatialAnchorAttachableComponentsANDROID) .