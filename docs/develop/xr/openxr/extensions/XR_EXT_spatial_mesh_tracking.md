---
title: https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking
url: https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking
source: md.txt
---

### XR_EXT_spatial_mesh_tracking

**Name String**

`XR_EXT_spatial_mesh_tracking`

**Extension Type**

Instance extension

**Registered Extension Number**

784

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

Ron Bessems, Meta  

Yin Li, Microsoft  

Jimmy Alamparambil, ByteDance  

Zhipeng Liu, ByteDance  

Jun Yan, ByteDance

## Overview

This extension builds on `XR_EXT_spatial_entity` and defines spatial capabilities for tracking the triangle mesh of the environment. The triangle mesh provided by the capability defined in this extension is intended to be used by applications for determining collisions of the virtual content with the environment.

## Spatial Mesh Tracking Capability

This extension defines `XR_SPATIAL_CAPABILITY_MESH_TRACKING_EXT` as a spatial capability for tracking the triangle mesh of the environment. Tracking the mesh of entities like planes and objects is not covered by this capability and **must** instead be indicated by the enumeration of the `XR_SPATIAL_COMPONENT_TYPE_MESH_3D_EXT` component for the respective capabilities of that track those entities.

`XR_SPATIAL_CAPABILITY_MESH_TRACKING_EXT` is used to provide both a watertight and a non-watertight mesh to the application, depending on the runtime's abilities and the configuration selected by the application.

A watertight mesh is one where gaps and unscanned regions of all sizes have been filled and it forms a tight mesh within a certain volumetric block. As the name suggests, if an application fills up water inside a watertight mesh, there **should** be no water that leaks out of the watertight volume. Making a scanned mesh watertight often requires very high compute, though some runtimes offset that cost by processing the mesh beforehand.

### Runtime Support

If the runtime supports tracking for the triangle mesh of the environment, it **must** indicate this by enumerating `XR_SPATIAL_CAPABILITY_MESH_TRACKING_EXT` in [xrEnumerateSpatialCapabilitiesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrEnumerateSpatialCapabilitiesEXT) .

There are 3 possible abilities of a runtime that supports `XR_SPATIAL_CAPABILITY_MESH_TRACKING_EXT` -

- The runtime supports only non-watertight mesh tracking. In this case the runtime enumerates `XR_SPATIAL_CAPABILITY_MESH_TRACKING_EXT` in [xrEnumerateSpatialCapabilitiesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrEnumerateSpatialCapabilitiesEXT) but **must** not enumerate `XR_SPATIAL_CAPABILITY_FEATURE_TRACK_WATERTIGHT_MESH_EXT` in [xrEnumerateSpatialCapabilityFeaturesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrEnumerateSpatialCapabilityFeaturesEXT) (see [Tracking a Watertight Mesh](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#ext_spatial_mesh_tracking_watertight_feature) ).
- The runtime supports both watertight and non-watertight mesh tracking. In this case the runtime enumerates `XR_SPATIAL_CAPABILITY_MESH_TRACKING_EXT` in [xrEnumerateSpatialCapabilitiesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrEnumerateSpatialCapabilitiesEXT) and **must** also enumerate `XR_SPATIAL_CAPABILITY_FEATURE_TRACK_WATERTIGHT_MESH_EXT` in [xrEnumerateSpatialCapabilityFeaturesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrEnumerateSpatialCapabilityFeaturesEXT) (see [Tracking a Watertight Mesh](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#ext_spatial_mesh_tracking_watertight_feature) ) in order to enable watertight mesh tracking requests from the application.
- The runtime supports only watertight mesh tracking. In this case the runtime enumerates `XR_SPATIAL_CAPABILITY_MESH_TRACKING_EXT` in [xrEnumerateSpatialCapabilitiesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrEnumerateSpatialCapabilitiesEXT) and **must** also enumerate `XR_SPATIAL_CAPABILITY_FEATURE_TRACK_WATERTIGHT_MESH_EXT` in [xrEnumerateSpatialCapabilityFeaturesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrEnumerateSpatialCapabilityFeaturesEXT) (see [Tracking a Watertight Mesh](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#ext_spatial_mesh_tracking_watertight_feature) ) to indicate to the application that it supports watertight mesh tracking. In this particular case, the runtime always returns a watertight mesh to the application regardless of the configuration for `XR_SPATIAL_CAPABILITY_FEATURE_TRACK_WATERTIGHT_MESH_EXT` .

### Configuration

The [XrSpatialCapabilityConfigurationMeshTrackingEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#XrSpatialCapabilityConfigurationMeshTrackingEXT) structure is defined as:

    typedef struct XrSpatialCapabilityConfigurationMeshTrackingEXT {
        XrStructureType                     type;
        const void*                         next;
        XrSpatialCapabilityEXT              capability;
        uint32_t                            enabledComponentCount;
        const XrSpatialComponentTypeEXT*    enabledComponents;
    } XrSpatialCapabilityConfigurationMeshTrackingEXT;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `capability` is an [XrSpatialCapabilityEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityEXT) and **must** be `XR_SPATIAL_CAPABILITY_MESH_TRACKING_EXT` .
- `enabledComponentCount` is a `uint32_t` describing the count of elements in the `enabledComponents` array.
- `enabledComponents` is a pointer to an array of [XrSpatialComponentTypeEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentTypeEXT) .

Applications **can** enable the `XR_SPATIAL_CAPABILITY_MESH_TRACKING_EXT` spatial capability by including a pointer to an [XrSpatialCapabilityConfigurationMeshTrackingEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#XrSpatialCapabilityConfigurationMeshTrackingEXT) structure in [XrSpatialContextCreateInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextCreateInfoEXT) :: `capabilityConfigs` .

The runtime **must** return `XR_ERROR_VALIDATION_FAILURE` if `capability` is not `XR_SPATIAL_CAPABILITY_MESH_TRACKING_EXT` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#VUID-XrSpatialCapabilityConfigurationMeshTrackingEXT-extension-notenabled) The `XR_EXT_spatial_mesh_tracking` extension **must** be enabled prior to using [XrSpatialCapabilityConfigurationMeshTrackingEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#XrSpatialCapabilityConfigurationMeshTrackingEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#VUID-XrSpatialCapabilityConfigurationMeshTrackingEXT-type-type) `type` **must** be `XR_TYPE_SPATIAL_CAPABILITY_CONFIGURATION_MESH_TRACKING_EXT`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#VUID-XrSpatialCapabilityConfigurationMeshTrackingEXT-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains) . See also: [XrSpatialFeatureTrackWatertightMeshEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#XrSpatialFeatureTrackWatertightMeshEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#VUID-XrSpatialCapabilityConfigurationMeshTrackingEXT-capability-parameter) `capability` **must** be a valid [XrSpatialCapabilityEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityEXT) value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#VUID-XrSpatialCapabilityConfigurationMeshTrackingEXT-enabledComponents-parameter) `enabledComponents` **must** be a pointer to an array of `enabledComponentCount` valid [XrSpatialComponentTypeEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentTypeEXT) values
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#VUID-XrSpatialCapabilityConfigurationMeshTrackingEXT-enabledComponentCount-arraylength) The `enabledComponentCount` parameter **must** be greater than `0`

### Tracking a Watertight Mesh

The [XrSpatialFeatureTrackWatertightMeshEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#XrSpatialFeatureTrackWatertightMeshEXT) structure is defined as:

    typedef struct XrSpatialFeatureTrackWatertightMeshEXT {
        XrStructureType    type;
        const void*        next;
        XrBool32           enableWatertightMeshTracking;
    } XrSpatialFeatureTrackWatertightMeshEXT;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `enableWatertightMeshTracking` indicates if the runtime **must** compute a watertight mesh for the scanned environment.

Runtimes that support watertight mesh tracking **must** enumerate `XR_SPATIAL_CAPABILITY_FEATURE_TRACK_WATERTIGHT_MESH_EXT` in [xrEnumerateSpatialCapabilityFeaturesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrEnumerateSpatialCapabilityFeaturesEXT) . The `XR_SPATIAL_CAPABILITY_FEATURE_TRACK_WATERTIGHT_MESH_EXT` feature allows the applications to optionally enable watertight mesh tracking and explicitly opt-into any additional compute that the watertight mesh generation **may** incur.

If `XR_SPATIAL_CAPABILITY_FEATURE_TRACK_WATERTIGHT_MESH_EXT` is enumerated by [xrEnumerateSpatialCapabilityFeaturesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrEnumerateSpatialCapabilityFeaturesEXT) for a certain capability, the application **can** chain [XrSpatialFeatureTrackWatertightMeshEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#XrSpatialFeatureTrackWatertightMeshEXT) to the corresponding configuration structure of that capability to indicate whether it wants the tracked mesh to be watertight or not. If the application sets `enableWatertightMeshTracking` to `XR_TRUE` , the runtime **must** compute and provide the application with a watertight mesh of the environment. If the application sets `enableWatertightMeshTracking` to `XR_FALSE` , the tracked mesh **may** still be watertight if the runtime only supports watertight mesh tracking, e.g. in cases where the runtime is providing a processed mesh from a prescanned environment.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#VUID-XrSpatialFeatureTrackWatertightMeshEXT-extension-notenabled) The `XR_EXT_spatial_mesh_tracking` extension **must** be enabled prior to using [XrSpatialFeatureTrackWatertightMeshEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#XrSpatialFeatureTrackWatertightMeshEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#VUID-XrSpatialFeatureTrackWatertightMeshEXT-type-type) `type` **must** be `XR_TYPE_SPATIAL_FEATURE_TRACK_WATERTIGHT_MESH_EXT`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#VUID-XrSpatialFeatureTrackWatertightMeshEXT-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)

### Application Flow

The diagram below shows how an application can go about configuring the spatial context if it wants to track a watertight mesh of the environment.

Yes

Yes

App needs  

watertight mesh

App needs...

Yes

Yes

No

No

Runtime  

supports "mesh tracking"  

capability

Runtime...

Yes

Yes

No

No

Runtime  

supports "track watertight mesh"  

feature

Runtime...

App creates spatial context with "mesh tracking capability" AND "track watertight mesh" feature

App creates spatial...

App handles lack of feature support on current runtime

App handles lack of...

App processes the tracked mesh to create a watertight mesh itself, perhaps with the aid of the user in patching the holes in the mesh

App processes the tr... [Text is not SVG - cannot display](https://www.diagrams.net/doc/faq/svg-export-text-problems)

### Figure 29. App flow for requesting watertight mesh

### Guaranteed Components

A runtime that supports `XR_SPATIAL_CAPABILITY_MESH_TRACKING_EXT` **must** provide the following spatial components as guaranteed components of all entities discovered by this capability and **must** enumerate them in [xrEnumerateSpatialCapabilityComponentTypesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrEnumerateSpatialCapabilityComponentTypesEXT) :

- `XR_SPATIAL_COMPONENT_TYPE_BOUNDED_3D_EXT`
- `XR_SPATIAL_COMPONENT_TYPE_MESH_3D_EXT`

###### Bounded 3D Component

The bounded 3D component provides the center and extents of the entity it is on. The data provided by this component makes it easier for applications to cull the entities that are outside its view frustum.

See [Bounded 3D](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#ext_spatial_entity_bounded3D_component) for more details.

###### Mesh 3D Component

The mesh 3D component provides the 3D mesh of the entity it is on. See [Mesh 3D](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#ext_spatial_entity_mesh3d_component) for more details.

### Volumetric Segmentation (Chunking)

The runtime **may** segment the mesh into volumetric blocks (chunks) to make it easier for applications to cull the mesh blocks outside of its view frustum. In such a case the runtime **must** treat each such volumetric block as a separate entity and have the set of [Guaranteed Components](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#ext_spatial_mesh_tracking_guaranteed_components) on each such entity (volumetric block). If the runtime is providing a watertight mesh in this manner, each volumetric block individually is not watertight, but a group of blocks together form a watertight mesh. In such a scenario, the runtime **must** add the `XR_SPATIAL_COMPONENT_TYPE_PARENT_EXT` component on each entity (volumetric block), and the value of the parent entity across the blocks that together form a watertight mesh **must** be the same. This enables the application to identify which chunks together form a watertight mesh.

Meshes of adjacent volumetric blocks **may** share vertices, but the triangles of one volumetric block **must** not overlap with the triangles of its adjacent volume.

## Optional Components

### Mesh Normals

###### Component data

`XR_SPATIAL_COMPONENT_TYPE_MESH_3D_NORMALS_EXT` uses [XrSpatialBufferEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialBufferEXT) for its data. [XrSpatialBufferEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialBufferEXT) :: `bufferId` represents the buffer containing the vertex normals of the mesh of the entity this component is on. The [XrSpatialBufferEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialBufferEXT) :: `bufferType` **must** be `XR_SPATIAL_BUFFER_TYPE_VECTOR3F_EXT` . An entity that has `XR_SPATIAL_COMPONENT_TYPE_MESH_3D_NORMALS_EXT` **must** also have the `XR_SPATIAL_COMPONENT_TYPE_MESH_3D_EXT` on it. The normals provided by this component **must** correspond to the vertices provided in the [XrSpatialMeshDataEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialMeshDataEXT) :: `vertexBuffer` of the `XR_SPATIAL_COMPONENT_TYPE_MESH_3D_EXT` component.

###### Component list structure to query data

The [XrSpatialComponentMesh3DNormalsListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#XrSpatialComponentMesh3DNormalsListEXT) structure is defined as:

    typedef struct XrSpatialComponentMesh3DNormalsListEXT {
        XrStructureType        type;
        void*                  next;
        uint32_t               meshNormalsCount;
        XrSpatialBufferEXT*    meshNormals;
    } XrSpatialComponentMesh3DNormalsListEXT;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.
- `meshNormalsCount` is a `uint32_t` describing the count of elements in the `meshNormals` array.
- `meshNormals` is an array of [XrVector3f](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrVector3f) .

The runtime **must** return `XR_ERROR_VALIDATION_FAILURE` from [xrQuerySpatialComponentDataEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrQuerySpatialComponentDataEXT) if [XrSpatialComponentMesh3DNormalsListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#XrSpatialComponentMesh3DNormalsListEXT) is in the next chain of [XrSpatialComponentDataQueryResultEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryResultEXT) :: `next` but [XrSpatialComponentDataQueryConditionEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryConditionEXT) :: `componentTypeCount` is not zero and `XR_SPATIAL_COMPONENT_TYPE_MESH_3D_NORMALS_EXT` is not included in [XrSpatialComponentDataQueryConditionEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryConditionEXT) :: `componentTypes` .

The runtime **must** return `XR_ERROR_SIZE_INSUFFICIENT` from [xrQuerySpatialComponentDataEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrQuerySpatialComponentDataEXT) if `meshNormalsCount` is less than [XrSpatialComponentDataQueryResultEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryResultEXT) :: `entityIdCountOutput` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#VUID-XrSpatialComponentMesh3DNormalsListEXT-extension-notenabled) The `XR_EXT_spatial_mesh_tracking` extension **must** be enabled prior to using [XrSpatialComponentMesh3DNormalsListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#XrSpatialComponentMesh3DNormalsListEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#VUID-XrSpatialComponentMesh3DNormalsListEXT-type-type) `type` **must** be `XR_TYPE_SPATIAL_COMPONENT_MESH_3D_NORMALS_LIST_EXT`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#VUID-XrSpatialComponentMesh3DNormalsListEXT-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#VUID-XrSpatialComponentMesh3DNormalsListEXT-meshNormals-parameter) `meshNormals` **must** be a pointer to an array of `meshNormalsCount` [XrSpatialBufferEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialBufferEXT) structures
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#VUID-XrSpatialComponentMesh3DNormalsListEXT-meshNormalsCount-arraylength) The `meshNormalsCount` parameter **must** be greater than `0`

### Configuration

If `XR_SPATIAL_COMPONENT_TYPE_MESH_3D_NORMALS_EXT` is enumerated in [XrSpatialCapabilityComponentTypesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityComponentTypesEXT) :: `componentTypes` for some capability, the application **can** enable it by including the enum in the [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityConfigurationBaseHeaderEXT) :: `enabledComponents` list. This component does not require any special configuration to be included in the next chain of [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityConfigurationBaseHeaderEXT) . However, applications are encouraged to use this component and its data in conjunction with the `XR_SPATIAL_COMPONENT_TYPE_MESH_3D_EXT` component.

### Mesh Semantic Labels

    typedef enum XrSpatialMeshSemanticLabelEXT {
        XR_SPATIAL_MESH_SEMANTIC_LABEL_UNCATEGORIZED_EXT = 1,
        XR_SPATIAL_MESH_SEMANTIC_LABEL_FLOOR_EXT = 2,
        XR_SPATIAL_MESH_SEMANTIC_LABEL_WALL_EXT = 3,
        XR_SPATIAL_MESH_SEMANTIC_LABEL_CEILING_EXT = 4,
        XR_SPATIAL_MESH_SEMANTIC_LABEL_TABLE_EXT = 5,
        XR_SPATIAL_MESH_SEMANTIC_LABEL_CHAIR_EXT = 6,
        XR_SPATIAL_MESH_SEMANTIC_LABEL_SOFA_EXT = 7,
        XR_SPATIAL_MESH_SEMANTIC_LABEL_BED_EXT = 8,
        XR_SPATIAL_MESH_SEMANTIC_LABEL_MAX_ENUM_EXT = 0x7FFFFFFF
    } XrSpatialMeshSemanticLabelEXT;

The [XrSpatialMeshSemanticLabelEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#XrSpatialMeshSemanticLabelEXT) enumeration describes a set of semantic labels for a mesh. This is used by different spatial components to give meaning to the `uint8_t` values from an [XrSpatialBufferEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialBufferEXT) for per-vertex or per-triangle semantic labels. See [Mesh Vertex Semantic Labels](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#ext_spatial_entity_mesh_vertex_semantic_labels_component) and [Mesh Triangle Semantic Labels](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#ext_spatial_entity_mesh_triangle_semantic_labels_component)

Extensions that want to extend either this semantic label set or add their own new set for meshes, **should** follow the guidelines given in [Semantic Label Design \& Extension Guidelines](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#ext_spatial_entity_semantic_labels_guidelines) .

Enum Description

`XR_SPATIAL_MESH_SEMANTIC_LABEL_UNCATEGORIZED_EXT`

The runtime was unable to classify the vertex or triangle.

`XR_SPATIAL_MESH_SEMANTIC_LABEL_FLOOR_EXT`

The vertex or triangle maps to a floor.

`XR_SPATIAL_MESH_SEMANTIC_LABEL_WALL_EXT`

The vertex or triangle maps to a wall.

`XR_SPATIAL_MESH_SEMANTIC_LABEL_CEILING_EXT`

The vertex or triangle maps to a ceiling.

`XR_SPATIAL_MESH_SEMANTIC_LABEL_TABLE_EXT`

The vertex or triangle maps to a table.

`XR_SPATIAL_MESH_SEMANTIC_LABEL_CHAIR_EXT`

The vertex or triangle maps to a chair.

`XR_SPATIAL_MESH_SEMANTIC_LABEL_SOFA_EXT`

The vertex or triangle maps to a sofa.

`XR_SPATIAL_MESH_SEMANTIC_LABEL_BED_EXT`

The vertex or triangle maps to a bed.

### Mesh Vertex Semantic Labels

###### Component Overview

`XR_SPATIAL_COMPONENT_TYPE_MESH_3D_VERTEX_SEMANTIC_LABELS_EXT` provides a single semantic label for each vertex of the mesh of a spatial entity.

###### Component data

`XR_SPATIAL_COMPONENT_TYPE_MESH_3D_VERTEX_SEMANTIC_LABELS_EXT` uses [XrSpatialBufferEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialBufferEXT) for its data. [XrSpatialBufferEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialBufferEXT) :: `bufferId` represents the buffer containing the vertex semantic labels of the mesh of the entity this component is on. The [XrSpatialBufferEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialBufferEXT) :: `bufferType` **must** be `XR_SPATIAL_BUFFER_TYPE_UINT8_EXT` . The values in the buffer correspond to the values of the [XrSpatialMeshSemanticLabelEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#XrSpatialMeshSemanticLabelEXT) enumeration. An entity that has `XR_SPATIAL_COMPONENT_TYPE_MESH_3D_VERTEX_SEMANTIC_LABELS_EXT` **must** also have the `XR_SPATIAL_COMPONENT_TYPE_MESH_3D_EXT` component on it. The semantic labels provided by this component **must** correspond to the vertices provided in the [XrSpatialMeshDataEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialMeshDataEXT) :: `vertexBuffer` of the `XR_SPATIAL_COMPONENT_TYPE_MESH_3D_EXT` component. This implies that the semantic label at a given index of the spatial buffer data provided by this component corresponds to the vertex at the same index provided by [XrSpatialMeshDataEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialMeshDataEXT) :: `vertexBuffer` . This also implies that [xrGetSpatialBufferUint8EXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrGetSpatialBufferUint8EXT) :: `bufferCountOutput` **must** be the same value for the vertex semantic label buffer and [XrSpatialMeshDataEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialMeshDataEXT) :: `vertexBuffer` .

###### Component list structure to query data

The [XrSpatialComponentMesh3DVertexSemanticLabelsListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#XrSpatialComponentMesh3DVertexSemanticLabelsListEXT) structure is defined as:

    typedef struct XrSpatialComponentMesh3DVertexSemanticLabelsListEXT {
        XrStructureType        type;
        void*                  next;
        uint32_t               meshSemanticLabelsCount;
        XrSpatialBufferEXT*    meshSemanticLabels;
    } XrSpatialComponentMesh3DVertexSemanticLabelsListEXT;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.
- `meshSemanticLabelsCount` is a `uint32_t` describing the count of elements in the `meshSemanticLabels` array.
- `meshSemanticLabels` is an array of [XrSpatialBufferEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialBufferEXT) .

The runtime **must** return `XR_ERROR_VALIDATION_FAILURE` from [xrQuerySpatialComponentDataEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrQuerySpatialComponentDataEXT) if [XrSpatialComponentMesh3DVertexSemanticLabelsListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#XrSpatialComponentMesh3DVertexSemanticLabelsListEXT) is in the next chain of [XrSpatialComponentDataQueryResultEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryResultEXT) :: `next` but [XrSpatialComponentDataQueryConditionEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryConditionEXT) :: `componentTypeCount` is not zero and `XR_SPATIAL_COMPONENT_TYPE_MESH_3D_VERTEX_SEMANTIC_LABELS_EXT` is not included in [XrSpatialComponentDataQueryConditionEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryConditionEXT) :: `componentTypes` .

The runtime **must** return `XR_ERROR_SIZE_INSUFFICIENT` from [xrQuerySpatialComponentDataEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrQuerySpatialComponentDataEXT) if `meshSemanticLabelsCount` is less than [XrSpatialComponentDataQueryResultEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryResultEXT) :: `entityIdCountOutput` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#VUID-XrSpatialComponentMesh3DVertexSemanticLabelsListEXT-extension-notenabled) The `XR_EXT_spatial_mesh_tracking` extension **must** be enabled prior to using [XrSpatialComponentMesh3DVertexSemanticLabelsListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#XrSpatialComponentMesh3DVertexSemanticLabelsListEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#VUID-XrSpatialComponentMesh3DVertexSemanticLabelsListEXT-type-type) `type` **must** be `XR_TYPE_SPATIAL_COMPONENT_MESH_3D_VERTEX_SEMANTIC_LABELS_LIST_EXT`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#VUID-XrSpatialComponentMesh3DVertexSemanticLabelsListEXT-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#VUID-XrSpatialComponentMesh3DVertexSemanticLabelsListEXT-meshSemanticLabels-parameter) `meshSemanticLabels` **must** be a pointer to an array of `meshSemanticLabelsCount` [XrSpatialBufferEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialBufferEXT) structures
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#VUID-XrSpatialComponentMesh3DVertexSemanticLabelsListEXT-meshSemanticLabelsCount-arraylength) The `meshSemanticLabelsCount` parameter **must** be greater than `0`

### Configuration

If `XR_SPATIAL_COMPONENT_TYPE_MESH_3D_VERTEX_SEMANTIC_LABELS_EXT` is enumerated in [XrSpatialCapabilityComponentTypesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityComponentTypesEXT) :: `componentTypes` for some capability, the application **can** enable it by including the enum in the [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityConfigurationBaseHeaderEXT) :: `enabledComponents` list. This component does not require any special configuration to be included in the next chain of [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityConfigurationBaseHeaderEXT) . However, applications are encouraged to use this component and its data in conjunction with the `XR_SPATIAL_COMPONENT_TYPE_MESH_3D_EXT` component. This component **cannot** be enabled together with `XR_SPATIAL_COMPONENT_TYPE_MESH_3D_TRIANGLE_SEMANTIC_LABELS_EXT` . If an application adds both `XR_SPATIAL_COMPONENT_TYPE_MESH_3D_VERTEX_SEMANTIC_LABELS_EXT` and `XR_SPATIAL_COMPONENT_TYPE_MESH_3D_TRIANGLE_SEMANTIC_LABELS_EXT` to [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityConfigurationBaseHeaderEXT) :: `enabledComponents` , the runtime **must** return `XR_ERROR_SPATIAL_CAPABILITY_CONFIGURATION_INVALID_EXT` . The runtime **must** also return `XR_ERROR_SPATIAL_CAPABILITY_CONFIGURATION_INVALID_EXT` if the application attempts to enable both components in separate [XrSpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextEXT) .

### Mesh Triangle Semantic Labels

###### Component Overview

`XR_SPATIAL_COMPONENT_TYPE_MESH_3D_TRIANGLE_SEMANTIC_LABELS_EXT` provides a single semantic label for each triangle of the mesh of a spatial entity.

###### Component data

`XR_SPATIAL_COMPONENT_TYPE_MESH_3D_TRIANGLE_SEMANTIC_LABELS_EXT` uses [XrSpatialBufferEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialBufferEXT) for its data. [XrSpatialBufferEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialBufferEXT) :: `bufferId` represents the buffer containing the triangle semantic labels of the mesh of the entity this component is on. The [XrSpatialBufferEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialBufferEXT) :: `bufferType` **must** be `XR_SPATIAL_BUFFER_TYPE_UINT8_EXT` . The values in the buffer correspond to the values of the [XrSpatialMeshSemanticLabelEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#XrSpatialMeshSemanticLabelEXT) enumeration. An entity that has `XR_SPATIAL_COMPONENT_TYPE_MESH_3D_TRIANGLE_SEMANTIC_LABELS_EXT` **must** also have the `XR_SPATIAL_COMPONENT_TYPE_MESH_3D_EXT` component on it. The semantic labels provided by this component **must** correspond to the triangles provided in the [XrSpatialMeshDataEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialMeshDataEXT) of the `XR_SPATIAL_COMPONENT_TYPE_MESH_3D_EXT` component. The element count of the spatial buffer containing the triangle semantic labels is the element count of the [XrSpatialMeshDataEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialMeshDataEXT) :: `indexBuffer` divided by 3. This implies that the semantic label at a given index of the spatial buffer data provided by this component corresponds to the triangle represented by \[index \* 3\], \[index \* 3 + 1\], \[index \* 3 + 2\] in the [XrSpatialMeshDataEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialMeshDataEXT) :: `indexBuffer` .

###### Component list structure to query data

The [XrSpatialComponentMesh3DTriangleSemanticLabelsListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#XrSpatialComponentMesh3DTriangleSemanticLabelsListEXT) structure is defined as:

    typedef struct XrSpatialComponentMesh3DTriangleSemanticLabelsListEXT {
        XrStructureType        type;
        void*                  next;
        uint32_t               meshSemanticLabelsCount;
        XrSpatialBufferEXT*    meshSemanticLabels;
    } XrSpatialComponentMesh3DTriangleSemanticLabelsListEXT;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.
- `meshSemanticLabelsCount` is a `uint32_t` describing the count of elements in the `meshSemanticLabels` array.
- `meshSemanticLabels` is an array of [XrSpatialBufferEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialBufferEXT) .

The runtime **must** return `XR_ERROR_VALIDATION_FAILURE` from [xrQuerySpatialComponentDataEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrQuerySpatialComponentDataEXT) if [XrSpatialComponentMesh3DTriangleSemanticLabelsListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#XrSpatialComponentMesh3DTriangleSemanticLabelsListEXT) is in the next chain of [XrSpatialComponentDataQueryResultEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryResultEXT) :: `next` but [XrSpatialComponentDataQueryConditionEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryConditionEXT) :: `componentTypeCount` is not zero and `XR_SPATIAL_COMPONENT_TYPE_MESH_3D_TRIANGLE_SEMANTIC_LABELS_EXT` is not included in [XrSpatialComponentDataQueryConditionEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryConditionEXT) :: `componentTypes` .

The runtime **must** return `XR_ERROR_SIZE_INSUFFICIENT` from [xrQuerySpatialComponentDataEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrQuerySpatialComponentDataEXT) if `meshSemanticLabelsCount` is less than [XrSpatialComponentDataQueryResultEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryResultEXT) :: `entityIdCountOutput` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#VUID-XrSpatialComponentMesh3DTriangleSemanticLabelsListEXT-extension-notenabled) The `XR_EXT_spatial_mesh_tracking` extension **must** be enabled prior to using [XrSpatialComponentMesh3DTriangleSemanticLabelsListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#XrSpatialComponentMesh3DTriangleSemanticLabelsListEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#VUID-XrSpatialComponentMesh3DTriangleSemanticLabelsListEXT-type-type) `type` **must** be `XR_TYPE_SPATIAL_COMPONENT_MESH_3D_TRIANGLE_SEMANTIC_LABELS_LIST_EXT`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#VUID-XrSpatialComponentMesh3DTriangleSemanticLabelsListEXT-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#VUID-XrSpatialComponentMesh3DTriangleSemanticLabelsListEXT-meshSemanticLabels-parameter) `meshSemanticLabels` **must** be a pointer to an array of `meshSemanticLabelsCount` [XrSpatialBufferEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialBufferEXT) structures
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#VUID-XrSpatialComponentMesh3DTriangleSemanticLabelsListEXT-meshSemanticLabelsCount-arraylength) The `meshSemanticLabelsCount` parameter **must** be greater than `0`

### Configuration

If `XR_SPATIAL_COMPONENT_TYPE_MESH_3D_TRIANGLE_SEMANTIC_LABELS_EXT` is enumerated in [XrSpatialCapabilityComponentTypesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityComponentTypesEXT) :: `componentTypes` for some capability, the application **can** enable it by including the enum in the [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityConfigurationBaseHeaderEXT) :: `enabledComponents` list. This component does not require any special configuration to be included in the next chain of [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityConfigurationBaseHeaderEXT) . However, applications are encouraged to use this component and its data in conjunction with the `XR_SPATIAL_COMPONENT_TYPE_MESH_3D_EXT` component. This component **cannot** be enabled together with `XR_SPATIAL_COMPONENT_TYPE_MESH_3D_VERTEX_SEMANTIC_LABELS_EXT` . If an application adds both `XR_SPATIAL_COMPONENT_TYPE_MESH_3D_VERTEX_SEMANTIC_LABELS_EXT` and `XR_SPATIAL_COMPONENT_TYPE_MESH_3D_TRIANGLE_SEMANTIC_LABELS_EXT` to [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityConfigurationBaseHeaderEXT) :: `enabledComponents` , the runtime **must** return `XR_ERROR_SPATIAL_CAPABILITY_CONFIGURATION_INVALID_EXT` . The runtime **must** also return `XR_ERROR_SPATIAL_CAPABILITY_CONFIGURATION_INVALID_EXT` if the application attempts to enable both components in separate [XrSpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextEXT) .

## New Structures

- [XrSpatialCapabilityConfigurationMeshTrackingEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#XrSpatialCapabilityConfigurationMeshTrackingEXT)
- Extending [XrSpatialCapabilityConfigurationMeshTrackingEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#XrSpatialCapabilityConfigurationMeshTrackingEXT) :

  - [XrSpatialFeatureTrackWatertightMeshEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#XrSpatialFeatureTrackWatertightMeshEXT)
- Extending [XrSpatialComponentDataQueryResultEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryResultEXT) :

  - [XrSpatialComponentMesh3DNormalsListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#XrSpatialComponentMesh3DNormalsListEXT)
  - [XrSpatialComponentMesh3DTriangleSemanticLabelsListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#XrSpatialComponentMesh3DTriangleSemanticLabelsListEXT)
  - [XrSpatialComponentMesh3DVertexSemanticLabelsListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#XrSpatialComponentMesh3DVertexSemanticLabelsListEXT)

## New Enums

- [XrSpatialMeshSemanticLabelEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking#XrSpatialMeshSemanticLabelEXT)

## New Enum Constants

- `XR_EXT_SPATIAL_MESH_TRACKING_EXTENSION_NAME`
- `XR_EXT_spatial_mesh_tracking_SPEC_VERSION`
- Extending [XrSpatialCapabilityEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityEXT) :

  - `XR_SPATIAL_CAPABILITY_MESH_TRACKING_EXT`
- Extending [XrSpatialCapabilityFeatureEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityFeatureEXT) :

  - `XR_SPATIAL_CAPABILITY_FEATURE_TRACK_WATERTIGHT_MESH_EXT`
- Extending [XrSpatialComponentTypeEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentTypeEXT) :

  - `XR_SPATIAL_COMPONENT_TYPE_MESH_3D_NORMALS_EXT`
  - `XR_SPATIAL_COMPONENT_TYPE_MESH_3D_TRIANGLE_SEMANTIC_LABELS_EXT`
  - `XR_SPATIAL_COMPONENT_TYPE_MESH_3D_VERTEX_SEMANTIC_LABELS_EXT`
- Extending [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) :

  - `XR_TYPE_SPATIAL_CAPABILITY_CONFIGURATION_MESH_TRACKING_EXT`
  - `XR_TYPE_SPATIAL_COMPONENT_MESH_3D_NORMALS_LIST_EXT`
  - `XR_TYPE_SPATIAL_COMPONENT_MESH_3D_TRIANGLE_SEMANTIC_LABELS_LIST_EXT`
  - `XR_TYPE_SPATIAL_COMPONENT_MESH_3D_VERTEX_SEMANTIC_LABELS_LIST_EXT`
  - `XR_TYPE_SPATIAL_FEATURE_TRACK_WATERTIGHT_MESH_EXT`

## Issues

## Version History

- Revision 1, 2025-11-02 (Nihav Jain, Google)

  - Initial extension description