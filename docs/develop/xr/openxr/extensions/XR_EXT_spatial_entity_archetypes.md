---
title: https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity_archetypes
url: https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity_archetypes
source: md.txt
---

### XR_EXT_spatial_entity_archetypes

**Name String**

`XR_EXT_spatial_entity_archetypes`

**Extension Type**

Instance extension

**Registered Extension Number**

843

**Revision**

1

**Ratification Status**

Not ratified

**Extension and Version Dependencies**

`XR_EXT_spatial_entity`

**Contributors**

Nihav Jain, Google  

Andy Biar, Unity Technologies  

Natalie Fleury, Meta  

Yuichi Taguchi, Meta  

Ron Bessems, Meta  

Jimmy Alamparambil, ByteDance  

Zhipeng Liu, ByteDance  

Bastiaan Olij, Godot Engine

## Overview

The [xrQuerySpatialComponentDataEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrQuerySpatialComponentDataEXT) function offers applications a way to query entities and component data using a simple filter of the component types that **must** be present on an entity. While a component type-based query is suitable for some use cases, it poses a challenge for applications that want to read all component data on an entity (regardless of how many optional components the entity contains).

For example, imagine an application wants to query all component data for all anchors in a spatial context that is configured with persistence enabled. Some anchors might have the optional `XR_SPATIAL_COMPONENT_TYPE_PERSISTENCE_EXT` component, while others will not have this component. To get all the component data, the application needs to query for all entities that have `XR_SPATIAL_COMPONENT_TYPE_ANCHOR_EXT` (this returns all entities that have this component, regardless of what other components this entity **may** have), then query for all entities that have the `XR_SPATIAL_COMPONENT_TYPE_ANCHOR_EXT` and `XR_SPATIAL_COMPONENT_TYPE_PERSISTENCE_EXT` , and then perform a set difference themselves to remove the persisted anchors from the set of all anchors. Only then does the application have access to all component data for all anchor entities without duplication. The complexity of application logic required to deduplicate entities from such queries scales with the number of optional components that are supported for a capability.

This extension introduces the concept of archetypes (unique component combinations) as a solution for entity-centric query use cases. Instead of querying all possible optional components individually, then calculating set intersection to deduplicate entities from multiple query results, an application can query for all entities of each archetype instead. Archetypes enable applications to read all component data for all entities without duplication.

### Spatial Archetype ID

    XR_DEFINE_ATOM(XrSpatialArchetypeIdEXT)

`XrSpatialArchetypeIdEXT` is used to represent a spatial archetype which is a unique combination of components that exist on an entity. e.g. consider the following entities -

- Entity 1 has components A, B
- Entity 2 has components A, B, C
- Entity 3 has components D, E
- Entity 4 has components A, B

In the above example, the runtime **must** enumerate 3 archetype ids, one for each unique combination of components - (A, B), (A, B, C), (D, E).

Archetypes are different from spatial capabilities and their list of guaranteed components because the unique combination of component types that make up an archetype **may** include component types that are optional components for a given capability, and **may** even span more than one capability. Consider this real world example of a physical table, where that entity **may** have `XR_SPATIAL_COMPONENT_TYPE_BOUNDED_2D_EXT` and `XR_SPATIAL_COMPONENT_TYPE_PLANE_ALIGNMENT_EXT` because of the `XR_SPATIAL_CAPABILITY_PLANE_TRACKING_EXT` and `XR_SPATIAL_COMPONENT_TYPE_BOUNDED_3D_EXT` because of a hypothetical object tracking capability. A wall, on the other hand, **may** only have `XR_SPATIAL_COMPONENT_TYPE_BOUNDED_2D_EXT` and `XR_SPATIAL_COMPONENT_TYPE_PLANE_ALIGNMENT_EXT` . So while both the table and wall are seemingly being discovered by `XR_SPATIAL_CAPABILITY_PLANE_TRACKING_EXT` , their set of components are different and will therefore be represented by different `XrSpatialArchetypeIdEXT` .

An `XrSpatialArchetypeIdEXT` is valid and unique for the [XrSpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextEXT) parent of the [XrSpatialSnapshotEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialSnapshotEXT) in which the entities of that archetype exist. This means that for the same unique combination of components, the runtime **must** use the same `XrSpatialArchetypeIdEXT` in all the spatial snapshots created under an [XrSpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextEXT) . The runtime **may** reuse the same `XrSpatialArchetypeIdEXT` across multiple [XrSpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextEXT) within the same [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) if it represents the same unique combination of component types.

### Enumerate Spatial Archetypes in a Snapshot

The [xrEnumerateSpatialArchetypesEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity_archetypes#xrEnumerateSpatialArchetypesEXT) function is defined as:

    XrResult xrEnumerateSpatialArchetypesEXT(
        XrSpatialSnapshotEXT                        snapshot,
        uint32_t                                    archetypeCapacityInput,
        uint32_t*                                   archetypeCountOutput,
        XrSpatialArchetypeIdEXT*                    archetypes);

### Parameter Descriptions

- `snapshot` is a handle to an [XrSpatialSnapshotEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialSnapshotEXT) .
- `archetypeCapacityInput` is the capacity of the `archetypes` array, or 0 to indicate a request to retrieve the required capacity.
- `archetypeCountOutput` is the number of archetype ids, or the required capacity in the case that `archetypeCapacityInput` is insufficient.
- `archetypes` is an array of `XrSpatialArchetypeIdEXT` . It **can** be `NULL` if `archetypeCapacityInput` is 0.
- See the [Buffer Size Parameters](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-buffer-size-parameters) section for a detailed description of retrieving the required `archetypes` size.

The application **can** enumerate the list of spatial archetypes in `snapshot` using [xrEnumerateSpatialArchetypesEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity_archetypes#xrEnumerateSpatialArchetypesEXT) .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity_archetypes#VUID-xrEnumerateSpatialArchetypesEXT-extension-notenabled) The `XR_EXT_spatial_entity_archetypes` extension **must** be enabled prior to calling [xrEnumerateSpatialArchetypesEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity_archetypes#xrEnumerateSpatialArchetypesEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity_archetypes#VUID-xrEnumerateSpatialArchetypesEXT-snapshot-parameter) `snapshot` **must** be a valid [XrSpatialSnapshotEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialSnapshotEXT) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity_archetypes#VUID-xrEnumerateSpatialArchetypesEXT-archetypeCountOutput-parameter) `archetypeCountOutput` **must** be a pointer to a `uint32_t` value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity_archetypes#VUID-xrEnumerateSpatialArchetypesEXT-archetypes-parameter) If `archetypeCapacityInput` is not `0` , `archetypes` **must** be a pointer to an array of `archetypeCapacityInput` `XrSpatialArchetypeIdEXT` values

### Return Codes

[Success](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`
- `XR_SESSION_LOSS_PENDING`

[Failure](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_HANDLE_INVALID`
- `XR_ERROR_INSTANCE_LOST`
- `XR_ERROR_RUNTIME_FAILURE`
- `XR_ERROR_SESSION_LOST`
- `XR_ERROR_SIZE_INSUFFICIENT`
- `XR_ERROR_VALIDATION_FAILURE`

The [xrEnumerateSpatialArchetypeComponentTypesEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity_archetypes#xrEnumerateSpatialArchetypeComponentTypesEXT) function is defined as:

    XrResult xrEnumerateSpatialArchetypeComponentTypesEXT(
        XrSpatialSnapshotEXT                        snapshot,
        XrSpatialArchetypeIdEXT                     archetype,
        uint32_t                                    componentTypeCapacityInput,
        uint32_t*                                   componentTypeCountOutput,
        XrSpatialComponentTypeEXT*                  componentTypes);

### Parameter Descriptions

- `snapshot` is a handle to an [XrSpatialSnapshotEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialSnapshotEXT) .
- `archetype` is an `XrSpatialArchetypeIdEXT` for which the component types are enumerated.
- `componentTypeCapacityInput` is the capacity of the `componentTypes` array, or 0 to indicate a request to retrieve the required capacity.
- `componentTypeCountOutput` is the number of component types, or the required capacity in the case that `componentTypeCapacityInput` is insufficient.
- `componentTypes` is an array of [XrSpatialComponentTypeEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentTypeEXT) . It **can** be `NULL` if `componentTypeCapacityInput` is 0.
- See the [Buffer Size Parameters](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-buffer-size-parameters) section for a detailed description of retrieving the required `componentTypes` size.

The application **can** enumerate the list of spatial component types that make up an `XrSpatialArchetypeIdEXT` using [xrEnumerateSpatialArchetypeComponentTypesEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity_archetypes#xrEnumerateSpatialArchetypeComponentTypesEXT) .

The runtime **must** return `XR_ERROR_VALIDATION_FAILURE` if `archetype` is not enumerated by [xrEnumerateSpatialArchetypesEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity_archetypes#xrEnumerateSpatialArchetypesEXT) .

The runtime **must** return only the component types that were supplied by the application in [XrSpatialDiscoverySnapshotCreateInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialDiscoverySnapshotCreateInfoEXT) :: `componentTypes` or [XrSpatialUpdateSnapshotCreateInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialUpdateSnapshotCreateInfoEXT) :: `componentTypes` when creating `snapshot` . If the application does not provide a list of component types in [XrSpatialDiscoverySnapshotCreateInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialDiscoverySnapshotCreateInfoEXT) or [XrSpatialUpdateSnapshotCreateInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialUpdateSnapshotCreateInfoEXT) , the runtime **must** return only the component types which are enumerated in [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityConfigurationBaseHeaderEXT) ::enabledComponents for the capabilities configured for the spatial context that `snapshot` was created from.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity_archetypes#VUID-xrEnumerateSpatialArchetypeComponentTypesEXT-extension-notenabled) The `XR_EXT_spatial_entity_archetypes` extension **must** be enabled prior to calling [xrEnumerateSpatialArchetypeComponentTypesEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity_archetypes#xrEnumerateSpatialArchetypeComponentTypesEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity_archetypes#VUID-xrEnumerateSpatialArchetypeComponentTypesEXT-snapshot-parameter) `snapshot` **must** be a valid [XrSpatialSnapshotEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialSnapshotEXT) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity_archetypes#VUID-xrEnumerateSpatialArchetypeComponentTypesEXT-componentTypeCountOutput-parameter) `componentTypeCountOutput` **must** be a pointer to a `uint32_t` value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity_archetypes#VUID-xrEnumerateSpatialArchetypeComponentTypesEXT-componentTypes-parameter) If `componentTypeCapacityInput` is not `0` , `componentTypes` **must** be a pointer to an array of `componentTypeCapacityInput` [XrSpatialComponentTypeEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentTypeEXT) values

### Return Codes

[Success](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`
- `XR_SESSION_LOSS_PENDING`

[Failure](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_HANDLE_INVALID`
- `XR_ERROR_INSTANCE_LOST`
- `XR_ERROR_RUNTIME_FAILURE`
- `XR_ERROR_SESSION_LOST`
- `XR_ERROR_SIZE_INSUFFICIENT`
- `XR_ERROR_VALIDATION_FAILURE`

### Query Entities \& Component Data of Archetypes

The [XrSpatialFilterArchetypeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity_archetypes#XrSpatialFilterArchetypeEXT) structure is defined as:

    typedef struct XrSpatialFilterArchetypeEXT {
        XrStructureType            type;
        const void*                next;
        XrSpatialArchetypeIdEXT    archetype;
    } XrSpatialFilterArchetypeEXT;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `archetype` is an `XrSpatialArchetypeIdEXT` for which to get the data from the snapshot.

The application **can** chain the [XrSpatialFilterArchetypeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity_archetypes#XrSpatialFilterArchetypeEXT) structure to [XrSpatialComponentDataQueryConditionEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryConditionEXT) if it wants to query the entities and component data belonging to `archetype` .

When using [XrSpatialFilterArchetypeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity_archetypes#XrSpatialFilterArchetypeEXT) in the next chain of [XrSpatialComponentDataQueryConditionEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryConditionEXT) , the [XrSpatialComponentDataQueryConditionEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryConditionEXT) :: `componentTypes` array is implicit and is considered to be the same as the component types enumerated by [xrEnumerateSpatialArchetypeComponentTypesEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity_archetypes#xrEnumerateSpatialArchetypeComponentTypesEXT) for `archetype` . Therefore, if an application chains a valid [XrSpatialFilterArchetypeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity_archetypes#XrSpatialFilterArchetypeEXT) structure to [XrSpatialComponentDataQueryConditionEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryConditionEXT) , but [XrSpatialComponentDataQueryConditionEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryConditionEXT) :componentTypeCount is not 0, the runtime **must** return `XR_ERROR_VALIDATION_FAILURE` . The rest of the behavior of [xrQuerySpatialComponentDataEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrQuerySpatialComponentDataEXT) still holds true.

If `archetype` is not enumerated by [xrEnumerateSpatialArchetypesEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity_archetypes#xrEnumerateSpatialArchetypesEXT) , the runtime **must** return `XR_ERROR_VALIDATION_FAILURE` from [xrQuerySpatialComponentDataEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrQuerySpatialComponentDataEXT) .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity_archetypes#VUID-XrSpatialFilterArchetypeEXT-extension-notenabled) The `XR_EXT_spatial_entity_archetypes` extension **must** be enabled prior to using [XrSpatialFilterArchetypeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity_archetypes#XrSpatialFilterArchetypeEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity_archetypes#VUID-XrSpatialFilterArchetypeEXT-type-type) `type` **must** be `XR_TYPE_SPATIAL_FILTER_ARCHETYPE_EXT`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity_archetypes#VUID-XrSpatialFilterArchetypeEXT-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)

## Example Code

    // previously initialized using xrCreateSpatialDiscoverySnapshotCompleteEXT
    // or xrCreateSpatialUpdateSnapshotEXT.
    XrSpatialSnapshotEXT snapshot;

    uint32_t archetypeCountOutput = 0;
    CHK_XR(xrEnumerateSpatialArchetypesEXT(snapshot, 0, &archetypeCountOutput, nullptr));
    std::vector<XrSpatialArchetypeIdEXT> archetypes(archetypeCountOutput);
    CHK_XR(xrEnumerateSpatialArchetypesEXT(snapshot, archetypes.size(), &archetypeCountOutput, archetypes.data()));

    for (uint32_t i = 0; i < archetypes.size(); ++i) {
      XrSpatialFilterArchetypeEXT archetypeFilter{XR_TYPE_SPATIAL_FILTER_ARCHETYPE_EXT};
      archetypeFilter.archetype = archetypes[i];
      XrSpatialComponentDataQueryConditionEXT queryCond{XR_TYPE_SPATIAL_COMPONENT_DATA_QUERY_CONDITION_EXT};
      queryCond.next = &archetypeFilter;

      XrSpatialComponentDataQueryResultEXT queryResult{XR_TYPE_SPATIAL_COMPONENT_DATA_QUERY_RESULT_EXT};

      CHK_XR(xrQuerySpatialComponentDataEXT(snapshot, &queryCond, &queryResult));

      std::vector<XrSpatialEntityIdEXT> entityIds(queryResult.entityIdCountOutput);
      std::vector<XrSpatialEntityTrackingStateEXT> entityStates(queryResult.entityStateCountOutput);
      queryResult.entityIdCapacityInput = entityIds.size();
      queryResult.entityIds = entityIds.data();
      queryResult.entityStateCapacityInput = entityStates.size();
      queryResult.entityStates = entityStates.data();

      uint32_t componentTypeCountOutput = 0;
      CHK_XR(xrEnumerateSpatialArchetypeComponentTypesEXT(snapshot, archetypes[i], 0, &componentTypeCountOutput, nullptr));
      std::vector<XrSpatialComponentTypeEXT> componentTypes(componentTypeCountOutput);
      CHK_XR(xrEnumerateSpatialArchetypeComponentTypesEXT(snapshot, archetypes[i], componentTypes.size(), &componentTypeCountOutput, componentTypes.data()));

      std::vector<XrPosef> locations;
      XrSpatialComponentAnchorListEXT locationList{XR_TYPE_SPATIAL_COMPONENT_ANCHOR_LIST_EXT};
      std::vector<XrSpatialPersistenceDataEXT> persistenceData;
      XrSpatialComponentPersistenceListEXT persistenceDataList{XR_TYPE_SPATIAL_COMPONENT_PERSISTENCE_LIST_EXT};

      const auto archetypeContainsComponent = [&](XrSpatialComponentTypeEXT componentType) {
        return std::find(componentTypes.begin(), componentTypes.end(), componentType) != componentTypes.end();
      };

      XrBaseOutStructure* queryResultNext = reinterpret_cast<XrBaseOutStructure*>(&queryResult);

      if (archetypeContainsComponent(XR_SPATIAL_COMPONENT_TYPE_ANCHOR_EXT)) {
        locations.resize(queryResult.entityIdCountOutput);
        locationList.locationCount = locations.size();
        locationList.locations = locations.data();

        queryResultNext->next = reinterpret_cast<XrBaseOutStructure*>(&locationList);
        queryResultNext = queryResultNext->next;
      }
      if (archetypeContainsComponent(XR_SPATIAL_COMPONENT_TYPE_PERSISTENCE_EXT)) {
        persistenceData.resize(queryResult.entityIdCountOutput);
        persistenceDataList.persistDataCount = persistenceData.size();
        persistenceDataList.persistData = persistenceData.data();

        queryResultNext->next = reinterpret_cast<XrBaseOutStructure*>(&persistenceDataList);
        queryResultNext = queryResultNext->next;
      }
      // ...
      // similar conditions for other component types
      // ...

      CHK_XR(xrQuerySpatialComponentDataEXT(snapshot, &queryCond, &queryResult));
      // ... read entity ids and component data ...
    }

## New Base Types

- `XrSpatialArchetypeIdEXT`

## New Commands

- [xrEnumerateSpatialArchetypeComponentTypesEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity_archetypes#xrEnumerateSpatialArchetypeComponentTypesEXT)
- [xrEnumerateSpatialArchetypesEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity_archetypes#xrEnumerateSpatialArchetypesEXT)

## New Structures

- Extending [XrSpatialComponentDataQueryConditionEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryConditionEXT) :

  - [XrSpatialFilterArchetypeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity_archetypes#XrSpatialFilterArchetypeEXT)

## New Enum Constants

- `XR_EXT_SPATIAL_ENTITY_ARCHETYPES_EXTENSION_NAME`
- `XR_EXT_spatial_entity_archetypes_SPEC_VERSION`
- Extending [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) :

  - `XR_TYPE_SPATIAL_FILTER_ARCHETYPE_EXT`

## Issues

## Version History

- Revision 1, 2025-10-21 (Nihav Jain, Google)

  - Initial extension description