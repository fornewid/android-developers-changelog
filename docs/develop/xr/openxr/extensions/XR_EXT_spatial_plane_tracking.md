---
title: https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking
url: https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking
source: md.txt
---

### XR_EXT_spatial_plane_tracking

**Name String**

`XR_EXT_spatial_plane_tracking`

**Extension Type**

Instance extension

**Registered Extension Number**

742

**Revision**

1

**Ratification Status**

Ratified

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

This extension builds on `XR_EXT_spatial_entity` and defines the plane tracking spatial capability for the spatial entity framework.

## Runtime Support

If the runtime supports plane tracking, it **must** indicate this by enumerating `XR_SPATIAL_CAPABILITY_PLANE_TRACKING_EXT` in [xrEnumerateSpatialCapabilitiesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrEnumerateSpatialCapabilitiesEXT) .

## Configuration

The [XrSpatialCapabilityConfigurationPlaneTrackingEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#XrSpatialCapabilityConfigurationPlaneTrackingEXT) structure is defined as:

    typedef struct XrSpatialCapabilityConfigurationPlaneTrackingEXT {
        XrStructureType                     type;
        const void*                         next;
        XrSpatialCapabilityEXT              capability;
        uint32_t                            enabledComponentCount;
        const XrSpatialComponentTypeEXT*    enabledComponents;
    } XrSpatialCapabilityConfigurationPlaneTrackingEXT;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `capability` is an [XrSpatialCapabilityEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityEXT) and **must** be `XR_SPATIAL_CAPABILITY_PLANE_TRACKING_EXT` .
- `enabledComponentCount` is a `uint32_t` describing the count of elements in the `enabledComponents` array.
- `enabledComponents` is a pointer to an array of [XrSpatialComponentTypeEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentTypeEXT) .

Applications **can** enable the `XR_SPATIAL_CAPABILITY_PLANE_TRACKING_EXT` spatial capability by including a pointer to an [XrSpatialCapabilityConfigurationPlaneTrackingEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#XrSpatialCapabilityConfigurationPlaneTrackingEXT) structure in [XrSpatialContextCreateInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextCreateInfoEXT) :: `capabilityConfigs` .

The runtime **must** return `XR_ERROR_VALIDATION_FAILURE` if `capability` is not `XR_SPATIAL_CAPABILITY_PLANE_TRACKING_EXT` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#VUID-XrSpatialCapabilityConfigurationPlaneTrackingEXT-extension-notenabled) The `XR_EXT_spatial_plane_tracking` extension **must** be enabled prior to using [XrSpatialCapabilityConfigurationPlaneTrackingEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#XrSpatialCapabilityConfigurationPlaneTrackingEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#VUID-XrSpatialCapabilityConfigurationPlaneTrackingEXT-type-type) `type` **must** be `XR_TYPE_SPATIAL_CAPABILITY_CONFIGURATION_PLANE_TRACKING_EXT`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#VUID-XrSpatialCapabilityConfigurationPlaneTrackingEXT-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#VUID-XrSpatialCapabilityConfigurationPlaneTrackingEXT-capability-parameter) `capability` **must** be a valid [XrSpatialCapabilityEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityEXT) value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#VUID-XrSpatialCapabilityConfigurationPlaneTrackingEXT-enabledComponents-parameter) `enabledComponents` **must** be a pointer to an array of `enabledComponentCount` valid [XrSpatialComponentTypeEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentTypeEXT) values
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#VUID-XrSpatialCapabilityConfigurationPlaneTrackingEXT-enabledComponentCount-arraylength) The `enabledComponentCount` parameter **must** be greater than `0`

## Guaranteed Components

A runtime that supports `XR_SPATIAL_CAPABILITY_PLANE_TRACKING_EXT` **must** provide the following spatial components as guaranteed components of all entities discovered by this capability and **must** enumerate them in [xrEnumerateSpatialCapabilityComponentTypesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrEnumerateSpatialCapabilityComponentTypesEXT) :

- `XR_SPATIAL_COMPONENT_TYPE_BOUNDED_2D_EXT`
- `XR_SPATIAL_COMPONENT_TYPE_PLANE_ALIGNMENT_EXT`

### Bounded 2D Component

The bounded 2D component provides the center and extents of the plane represented by the entity it is on. See [Bounded 2D](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#ext_spatial_entity_bounded2D_component) for more details.

### Plane Alignment Component

###### Component data

    typedef enum XrSpatialPlaneAlignmentEXT {
        XR_SPATIAL_PLANE_ALIGNMENT_HORIZONTAL_UPWARD_EXT = 0,
        XR_SPATIAL_PLANE_ALIGNMENT_HORIZONTAL_DOWNWARD_EXT = 1,
        XR_SPATIAL_PLANE_ALIGNMENT_VERTICAL_EXT = 2,
        XR_SPATIAL_PLANE_ALIGNMENT_ARBITRARY_EXT = 3,
        XR_SPATIAL_PLANE_ALIGNMENT_MAX_ENUM_EXT = 0x7FFFFFFF
    } XrSpatialPlaneAlignmentEXT;

The [XrSpatialPlaneAlignmentEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#XrSpatialPlaneAlignmentEXT) enumeration describes the alignment of the plane associated with the spatial entity with an `XR_SPATIAL_COMPONENT_TYPE_PLANE_ALIGNMENT_EXT` component.

The enumeration values have the following meanings:

Enum Description

`XR_SPATIAL_PLANE_ALIGNMENT_HORIZONTAL_UPWARD_EXT`

The entity is horizontal and faces upward (e.g. floor).

`XR_SPATIAL_PLANE_ALIGNMENT_HORIZONTAL_DOWNWARD_EXT`

The entity is horizontal and faces downward (e.g. ceiling).

`XR_SPATIAL_PLANE_ALIGNMENT_VERTICAL_EXT`

The entity is vertical (e.g. wall).

`XR_SPATIAL_PLANE_ALIGNMENT_ARBITRARY_EXT`

The entity has an arbitrary, non-vertical and non-horizontal orientation.

###### Component list structure to query data

The [XrSpatialComponentPlaneAlignmentListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#XrSpatialComponentPlaneAlignmentListEXT) structure is defined as:

    typedef struct XrSpatialComponentPlaneAlignmentListEXT {
        XrStructureType                type;
        void*                          next;
        uint32_t                       planeAlignmentCount;
        XrSpatialPlaneAlignmentEXT*    planeAlignments;
    } XrSpatialComponentPlaneAlignmentListEXT;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `planeAlignmentCount` is a `uint32_t` describing the count of elements in the `planeAlignments` array.
- `planeAlignments` is an array of [XrSpatialPlaneAlignmentEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#XrSpatialPlaneAlignmentEXT) .

To query the plane alignment component of the spatial entities in an [XrSpatialSnapshotEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialSnapshotEXT) , include `XR_SPATIAL_COMPONENT_TYPE_PLANE_ALIGNMENT_EXT` in [XrSpatialComponentDataQueryConditionEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryConditionEXT) :: `componentTypes` and add [XrSpatialComponentPlaneAlignmentListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#XrSpatialComponentPlaneAlignmentListEXT) to the [XrSpatialComponentDataQueryResultEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryResultEXT) :: `next` chain.

The runtime **must** return `XR_ERROR_VALIDATION_FAILURE` from [xrQuerySpatialComponentDataEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrQuerySpatialComponentDataEXT) if [XrSpatialComponentPlaneAlignmentListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#XrSpatialComponentPlaneAlignmentListEXT) is in the [XrSpatialComponentDataQueryResultEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryResultEXT) :: `next` chain but `XR_SPATIAL_COMPONENT_TYPE_PLANE_ALIGNMENT_EXT` is not included in [XrSpatialComponentDataQueryConditionEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryConditionEXT) :: `componentTypes` .

The runtime **must** return `XR_ERROR_SIZE_INSUFFICIENT` from [xrQuerySpatialComponentDataEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrQuerySpatialComponentDataEXT) if `planeAlignmentCount` is less than [XrSpatialComponentDataQueryResultEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryResultEXT) :: `entityIdCountOutput` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#VUID-XrSpatialComponentPlaneAlignmentListEXT-extension-notenabled) The `XR_EXT_spatial_plane_tracking` extension **must** be enabled prior to using [XrSpatialComponentPlaneAlignmentListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#XrSpatialComponentPlaneAlignmentListEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#VUID-XrSpatialComponentPlaneAlignmentListEXT-type-type) `type` **must** be `XR_TYPE_SPATIAL_COMPONENT_PLANE_ALIGNMENT_LIST_EXT`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#VUID-XrSpatialComponentPlaneAlignmentListEXT-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#VUID-XrSpatialComponentPlaneAlignmentListEXT-planeAlignments-parameter) `planeAlignments` **must** be a pointer to an array of `planeAlignmentCount` [XrSpatialPlaneAlignmentEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#XrSpatialPlaneAlignmentEXT) values
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#VUID-XrSpatialComponentPlaneAlignmentListEXT-planeAlignmentCount-arraylength) The `planeAlignmentCount` parameter **must** be greater than `0`

###### Configuration

If `XR_SPATIAL_COMPONENT_TYPE_PLANE_ALIGNMENT_EXT` is enumerated in [XrSpatialCapabilityComponentTypesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityComponentTypesEXT) :: `componentTypes` for some capability, an application **can** enable it by including the enumerant in the [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityConfigurationBaseHeaderEXT) :: `enabledComponents` list of the [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityConfigurationBaseHeaderEXT) derived structure of the capability that supports this component.

This component does not require any special configuration to be included in the [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityConfigurationBaseHeaderEXT) :: `next` chain.

## Optional Components

A runtime that supports `XR_SPATIAL_CAPABILITY_PLANE_TRACKING_EXT` **may** support other spatial components in addition to the ones listed in the [Guaranteed Components](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#ext_spatial_plane_tracking_guaranteed_components) section. An application uses [xrEnumerateSpatialCapabilityComponentTypesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrEnumerateSpatialCapabilityComponentTypesEXT) to get the full list of components that a runtime supports, then configures the ones it is interested in when creating the spatial context.

### Mesh 2D Component

###### Component data

`XR_SPATIAL_COMPONENT_TYPE_MESH_2D_EXT` uses the [XrSpatialMeshDataEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialMeshDataEXT) structure for its data.

###### Component list structure to query data

The [XrSpatialComponentMesh2DListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#XrSpatialComponentMesh2DListEXT) structure is defined as:

    typedef struct XrSpatialComponentMesh2DListEXT {
        XrStructureType          type;
        void*                    next;
        uint32_t                 meshCount;
        XrSpatialMeshDataEXT*    meshes;
    } XrSpatialComponentMesh2DListEXT;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `meshCount` is a `uint32_t` describing the count of elements in the `meshes` array.
- `meshes` is an array of [XrSpatialMeshDataEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialMeshDataEXT) .

To query the mesh 2D component of the spatial entities in an [XrSpatialSnapshotEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialSnapshotEXT) , include `XR_SPATIAL_COMPONENT_TYPE_MESH_2D_EXT` in [XrSpatialComponentDataQueryConditionEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryConditionEXT) :: `componentTypes` and add [XrSpatialComponentMesh2DListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#XrSpatialComponentMesh2DListEXT) to the [XrSpatialComponentDataQueryResultEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryResultEXT) :: `next` chain.

The runtime **must** return `XR_ERROR_VALIDATION_FAILURE` from [xrQuerySpatialComponentDataEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrQuerySpatialComponentDataEXT) if [XrSpatialComponentMesh2DListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#XrSpatialComponentMesh2DListEXT) is in the [XrSpatialComponentDataQueryResultEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryResultEXT) :: `next` chain but `XR_SPATIAL_COMPONENT_TYPE_MESH_2D_EXT` is not included in [XrSpatialComponentDataQueryConditionEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryConditionEXT) :: `componentTypes` .

The runtime **must** return `XR_ERROR_SIZE_INSUFFICIENT` from [xrQuerySpatialComponentDataEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrQuerySpatialComponentDataEXT) if `meshCount` is less than [XrSpatialComponentDataQueryResultEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryResultEXT) :: `entityIdCountOutput` .

For the [XrSpatialMeshDataEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialMeshDataEXT) populated by the runtime in the `meshes` array, the [XrSpatialBufferEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialBufferEXT) :: `bufferType` for [XrSpatialMeshDataEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialMeshDataEXT) :: `vertexBuffer` **must** be `XR_SPATIAL_BUFFER_TYPE_VECTOR2F_EXT` and [XrSpatialBufferEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialBufferEXT) :: `bufferType` for [XrSpatialMeshDataEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialMeshDataEXT) :: `indexBuffer` **must** be `XR_SPATIAL_BUFFER_TYPE_UINT16_EXT` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#VUID-XrSpatialComponentMesh2DListEXT-extension-notenabled) The `XR_EXT_spatial_plane_tracking` extension **must** be enabled prior to using [XrSpatialComponentMesh2DListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#XrSpatialComponentMesh2DListEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#VUID-XrSpatialComponentMesh2DListEXT-type-type) `type` **must** be `XR_TYPE_SPATIAL_COMPONENT_MESH_2D_LIST_EXT`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#VUID-XrSpatialComponentMesh2DListEXT-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#VUID-XrSpatialComponentMesh2DListEXT-meshes-parameter) `meshes` **must** be a pointer to an array of `meshCount` [XrSpatialMeshDataEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialMeshDataEXT) structures
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#VUID-XrSpatialComponentMesh2DListEXT-meshCount-arraylength) The `meshCount` parameter **must** be greater than `0`

###### Configuration

If `XR_SPATIAL_COMPONENT_TYPE_MESH_2D_EXT` is enumerated in [XrSpatialCapabilityComponentTypesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityComponentTypesEXT) :: `componentTypes` for some capability, an application **can** enable it by including the enumerant in the [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityConfigurationBaseHeaderEXT) :: `enabledComponents` list of the [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityConfigurationBaseHeaderEXT) derived structure of the capability that supports this component.

This component does not require any special configuration to be included in the [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityConfigurationBaseHeaderEXT) :: `next` chain.

### Polygon 2D Component

###### Component Data

The [XrSpatialPolygon2DDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#XrSpatialPolygon2DDataEXT) structure is defined as:

    typedef struct XrSpatialPolygon2DDataEXT {
        XrPosef               origin;
        XrSpatialBufferEXT    vertexBuffer;
    } XrSpatialPolygon2DDataEXT;

### Member Descriptions

- `origin` is an [XrPosef](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrPosef) defining the origin of the polygon. All vertices of the polygon are relative to this origin in the X-Y plane.
- `vertexBuffer` is an [XrSpatialBufferEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialBufferEXT) that provides the ID for a buffer of type `XR_SPATIAL_BUFFER_TYPE_VECTOR2F_EXT` and represents the vertex buffer of the entity this component is on. The vertices **must** be returned in counter-clockwise order. The polygon represented by these vertices **must** not be self-intersecting and **may** be concave.

[XrSpatialBufferEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialBufferEXT) :: `bufferType` for `vertexBuffer` **must** be `XR_SPATIAL_BUFFER_TYPE_VECTOR2F_EXT` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#VUID-XrSpatialPolygon2DDataEXT-extension-notenabled) The `XR_EXT_spatial_plane_tracking` extension **must** be enabled prior to using [XrSpatialPolygon2DDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#XrSpatialPolygon2DDataEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#VUID-XrSpatialPolygon2DDataEXT-vertexBuffer-parameter) `vertexBuffer` **must** be a valid [XrSpatialBufferEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialBufferEXT) structure

###### Component list structure to query data

The [XrSpatialComponentPolygon2DListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#XrSpatialComponentPolygon2DListEXT) structure is defined as:

    typedef struct XrSpatialComponentPolygon2DListEXT {
        XrStructureType               type;
        void*                         next;
        uint32_t                      polygonCount;
        XrSpatialPolygon2DDataEXT*    polygons;
    } XrSpatialComponentPolygon2DListEXT;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `polygonCount` is a `uint32_t` describing the count of elements in the `polygons` array.
- `polygons` is an array of [XrSpatialPolygon2DDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#XrSpatialPolygon2DDataEXT) .

To query the polygon 2D component of the spatial entities in an [XrSpatialSnapshotEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialSnapshotEXT) , include `XR_SPATIAL_COMPONENT_TYPE_POLYGON_2D_EXT` in [XrSpatialComponentDataQueryConditionEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryConditionEXT) :: `componentTypes` and add [XrSpatialComponentPolygon2DListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#XrSpatialComponentPolygon2DListEXT) to the [XrSpatialComponentDataQueryResultEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryResultEXT) :: `next` chain.

The runtime **must** return `XR_ERROR_VALIDATION_FAILURE` from [xrQuerySpatialComponentDataEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrQuerySpatialComponentDataEXT) if [XrSpatialComponentPolygon2DListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#XrSpatialComponentPolygon2DListEXT) is in the [XrSpatialComponentDataQueryResultEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryResultEXT) :: `next` chain but `XR_SPATIAL_COMPONENT_TYPE_POLYGON_2D_EXT` is not included in [XrSpatialComponentDataQueryConditionEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryConditionEXT) :: `componentTypes` .

The runtime **must** return `XR_ERROR_SIZE_INSUFFICIENT` from [xrQuerySpatialComponentDataEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrQuerySpatialComponentDataEXT) if `polygonCount` is less than [XrSpatialComponentDataQueryResultEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryResultEXT) :: `entityIdCountOutput` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#VUID-XrSpatialComponentPolygon2DListEXT-extension-notenabled) The `XR_EXT_spatial_plane_tracking` extension **must** be enabled prior to using [XrSpatialComponentPolygon2DListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#XrSpatialComponentPolygon2DListEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#VUID-XrSpatialComponentPolygon2DListEXT-type-type) `type` **must** be `XR_TYPE_SPATIAL_COMPONENT_POLYGON_2D_LIST_EXT`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#VUID-XrSpatialComponentPolygon2DListEXT-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#VUID-XrSpatialComponentPolygon2DListEXT-polygons-parameter) `polygons` **must** be a pointer to an array of `polygonCount` [XrSpatialPolygon2DDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#XrSpatialPolygon2DDataEXT) structures
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#VUID-XrSpatialComponentPolygon2DListEXT-polygonCount-arraylength) The `polygonCount` parameter **must** be greater than `0`

###### Configuration

If `XR_SPATIAL_COMPONENT_TYPE_POLYGON_2D_EXT` is enumerated in [XrSpatialCapabilityComponentTypesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityComponentTypesEXT) :: `componentTypes` for some capability, an application **can** enable it by including the enumerant in the [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityConfigurationBaseHeaderEXT) :: `enabledComponents` list of the [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityConfigurationBaseHeaderEXT) derived structure of the capability that supports this component.

This component does not require any special configuration to be included in the [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityConfigurationBaseHeaderEXT) :: `next` chain.

### Plane Semantic Label

###### Component Data

    typedef enum XrSpatialPlaneSemanticLabelEXT {
        XR_SPATIAL_PLANE_SEMANTIC_LABEL_UNCATEGORIZED_EXT = 1,
        XR_SPATIAL_PLANE_SEMANTIC_LABEL_FLOOR_EXT = 2,
        XR_SPATIAL_PLANE_SEMANTIC_LABEL_WALL_EXT = 3,
        XR_SPATIAL_PLANE_SEMANTIC_LABEL_CEILING_EXT = 4,
        XR_SPATIAL_PLANE_SEMANTIC_LABEL_TABLE_EXT = 5,
        XR_SPATIAL_PLANE_SEMANTIC_LABEL_MAX_ENUM_EXT = 0x7FFFFFFF
    } XrSpatialPlaneSemanticLabelEXT;

The [XrSpatialPlaneSemanticLabelEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#XrSpatialPlaneSemanticLabelEXT) enumeration describes a set of semantic labels for planes.

Enum Description

`XR_SPATIAL_PLANE_SEMANTIC_LABEL_UNCATEGORIZED_EXT`

The runtime was unable to classify this entity.

`XR_SPATIAL_PLANE_SEMANTIC_LABEL_FLOOR_EXT`

The entity is a floor.

`XR_SPATIAL_PLANE_SEMANTIC_LABEL_WALL_EXT`

The entity is a wall.

`XR_SPATIAL_PLANE_SEMANTIC_LABEL_CEILING_EXT`

The entity is a ceiling.

`XR_SPATIAL_PLANE_SEMANTIC_LABEL_TABLE_EXT`

The entity is a table.

###### Component List Structure to Query Data

The [XrSpatialComponentPlaneSemanticLabelListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#XrSpatialComponentPlaneSemanticLabelListEXT) structure is defined as:

    typedef struct XrSpatialComponentPlaneSemanticLabelListEXT {
        XrStructureType                    type;
        void*                              next;
        uint32_t                           semanticLabelCount;
        XrSpatialPlaneSemanticLabelEXT*    semanticLabels;
    } XrSpatialComponentPlaneSemanticLabelListEXT;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `semanticLabelCount` is a `uint32_t` describing the count of elements in the `semanticLabels` array.
- `semanticLabels` is an array of [XrSpatialPlaneSemanticLabelEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#XrSpatialPlaneSemanticLabelEXT) .

To query the plane semantic label component of the spatial entities in an [XrSpatialSnapshotEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialSnapshotEXT) , include `XR_SPATIAL_COMPONENT_TYPE_PLANE_SEMANTIC_LABEL_EXT` in [XrSpatialComponentDataQueryConditionEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryConditionEXT) :: `componentTypes` and add [XrSpatialComponentPlaneSemanticLabelListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#XrSpatialComponentPlaneSemanticLabelListEXT) to the [XrSpatialComponentDataQueryResultEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryResultEXT) :: `next` chain.

The runtime **must** return `XR_ERROR_VALIDATION_FAILURE` from [xrQuerySpatialComponentDataEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrQuerySpatialComponentDataEXT) if [XrSpatialComponentPlaneSemanticLabelListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#XrSpatialComponentPlaneSemanticLabelListEXT) is in the next chain of [XrSpatialComponentDataQueryResultEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryResultEXT) :: `next` but `XR_SPATIAL_COMPONENT_TYPE_PLANE_SEMANTIC_LABEL_EXT` is not included in [XrSpatialComponentDataQueryConditionEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryConditionEXT) :: `componentTypes` .

The runtime **must** return `XR_ERROR_SIZE_INSUFFICIENT` from [xrQuerySpatialComponentDataEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrQuerySpatialComponentDataEXT) if `semanticLabelCount` is less than [XrSpatialComponentDataQueryResultEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryResultEXT) :: `entityIdCountOutput` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#VUID-XrSpatialComponentPlaneSemanticLabelListEXT-extension-notenabled) The `XR_EXT_spatial_plane_tracking` extension **must** be enabled prior to using [XrSpatialComponentPlaneSemanticLabelListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#XrSpatialComponentPlaneSemanticLabelListEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#VUID-XrSpatialComponentPlaneSemanticLabelListEXT-type-type) `type` **must** be `XR_TYPE_SPATIAL_COMPONENT_PLANE_SEMANTIC_LABEL_LIST_EXT`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#VUID-XrSpatialComponentPlaneSemanticLabelListEXT-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#VUID-XrSpatialComponentPlaneSemanticLabelListEXT-semanticLabels-parameter) `semanticLabels` **must** be a pointer to an array of `semanticLabelCount` [XrSpatialPlaneSemanticLabelEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#XrSpatialPlaneSemanticLabelEXT) values
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#VUID-XrSpatialComponentPlaneSemanticLabelListEXT-semanticLabelCount-arraylength) The `semanticLabelCount` parameter **must** be greater than `0`

###### Configuration

If `XR_SPATIAL_COMPONENT_TYPE_PLANE_SEMANTIC_LABEL_EXT` is enumerated in [XrSpatialCapabilityComponentTypesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityComponentTypesEXT) :: `componentTypes` for some capability, an application **can** enable it by including the enumerant in the [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityConfigurationBaseHeaderEXT) :: `enabledComponents` list of the [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityConfigurationBaseHeaderEXT) derived structure of the capability that supports this component.

This component does not require any special configuration to be included in the [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityConfigurationBaseHeaderEXT) :: `next` chain.

## Example Code

### Configure Plane Tracking Capability

The following example code demonstrates how to configure plane tracking capability when creating a spatial context.

    // Check if plane tracking capability is supported
    uint32_t capabilityCount;
    CHK_XR(xrEnumerateSpatialCapabilitiesEXT(instance, systemId, 0, &capabilityCount, nullptr));
    std::vector<XrSpatialCapabilityEXT> capabilities(capabilityCount);
    CHK_XR(xrEnumerateSpatialCapabilitiesEXT(instance, systemId, capabilityCount, &capabilityCount, capabilities.data()));

    if (std::find(capabilities.begin(), capabilities.end(), XR_SPATIAL_CAPABILITY_PLANE_TRACKING_EXT) == capabilities.end()) {
      return;
    }

    // Enumerate supported components for plane tracking capability
    XrSpatialCapabilityComponentTypesEXT planeComponents{XR_TYPE_SPATIAL_CAPABILITY_COMPONENT_TYPES_EXT};
    CHK_XR(xrEnumerateSpatialCapabilityComponentTypesEXT(instance, systemId, XR_SPATIAL_CAPABILITY_PLANE_TRACKING_EXT, &planeComponents));
    std::vector<XrSpatialComponentTypeEXT> planeCapabilityComponents(planeComponents.componentTypeCountOutput);
    planeComponents.componentTypeCapacityInput = planeCapabilityComponents.size();
    planeComponents.componentTypes = planeCapabilityComponents.data();
    CHK_XR(xrEnumerateSpatialCapabilityComponentTypesEXT(instance, systemId, XR_SPATIAL_CAPABILITY_PLANE_TRACKING_EXT, &planeComponents));

    // Check if polygon 2D and plane semantic labels optional components are supported
    const auto supportsComponent = [&planeCapabilityComponents](XrSpatialComponentTypeEXT component) {
      return std::find(planeCapabilityComponents.begin(), planeCapabilityComponents.end(), component) != planeCapabilityComponents.end();
    };

    const bool supportsPolygon2DComponent = supportsComponent(XR_SPATIAL_COMPONENT_TYPE_POLYGON_2D_EXT);
    const bool supportsSemanticLabelComponent = supportsComponent(XR_SPATIAL_COMPONENT_TYPE_PLANE_SEMANTIC_LABEL_EXT);

    // Create a spatial context
    XrSpatialContextEXT spatialContext{};

    // Enable the 2 guaranteed components of the plane tracking capability
    std::vector<XrSpatialComponentTypeEXT> enabledComponents = {
      XR_SPATIAL_COMPONENT_TYPE_BOUNDED_2D_EXT,
      XR_SPATIAL_COMPONENT_TYPE_PLANE_ALIGNMENT_EXT,
    };
    // Optionally enable polygon2D if it is supported
    if (supportsPolygon2DComponent) {
      enabledComponents.push_back(XR_SPATIAL_COMPONENT_TYPE_POLYGON_2D_EXT);
    }
    // Optionally enable semantic labels if it is supported
    if (supportsSemanticLabelComponent) {
      enabledComponents.push_back(XR_SPATIAL_COMPONENT_TYPE_PLANE_SEMANTIC_LABEL_EXT);
    }

    XrSpatialCapabilityConfigurationPlaneTrackingEXT planeConfig{XR_TYPE_SPATIAL_CAPABILITY_CONFIGURATION_PLANE_TRACKING_EXT};
    planeConfig.capability = XR_SPATIAL_CAPABILITY_PLANE_TRACKING_EXT;
    planeConfig.enabledComponentCount = enabledComponents.size();
    planeConfig.enabledComponents = enabledComponents.data();

    std::array<XrSpatialCapabilityConfigurationBaseHeaderEXT*, 1> capabilityConfigs = {
      reinterpret_cast<XrSpatialCapabilityConfigurationBaseHeaderEXT*>(&planeConfig),
    };

    XrSpatialContextCreateInfoEXT spatialContextCreateInfo{XR_TYPE_SPATIAL_CONTEXT_CREATE_INFO_EXT};
    spatialContextCreateInfo.capabilityConfigCount = capabilityConfigs.size();
    spatialContextCreateInfo.capabilityConfigs = capabilityConfigs.data();
    XrFutureEXT createContextFuture;
    CHK_XR(xrCreateSpatialContextAsyncEXT(session, &spatialContextCreateInfo, &createContextFuture));

    waitUntilReady(createContextFuture);

    XrCreateSpatialContextCompletionEXT completion{XR_TYPE_CREATE_SPATIAL_CONTEXT_COMPLETION_EXT};
    CHK_XR(xrCreateSpatialContextCompleteEXT(session, createContextFuture, &completion));
    if (completion.futureResult != XR_SUCCESS) {
      return;
    }

    spatialContext = completion.spatialContext;

    // ...
    // Discover entities with the spatial context
    // ...

    CHK_XR(xrDestroySpatialContextEXT(spatialContext));

### Discover Spatial Entities \& Query Component Data

The following example code demonstrates how to discover spatial entities for a context configured with `XR_SPATIAL_CAPABILITY_PLANE_TRACKING_EXT` and query its component data.

    XrFutureEXT future = XR_NULL_FUTURE_EXT;

    // We want to look for entities that have the following components.
    std::vector<XrSpatialComponentTypeEXT> snapshotComponents = {
      XR_SPATIAL_COMPONENT_TYPE_BOUNDED_2D_EXT,
      XR_SPATIAL_COMPONENT_TYPE_PLANE_ALIGNMENT_EXT,
    };
    if (supportsPolygon2DComponent) {
      snapshotComponents.push_back(XR_SPATIAL_COMPONENT_TYPE_POLYGON_2D_EXT);
    }
    if (supportsSemanticLabelComponent) {
      snapshotComponents.push_back(XR_SPATIAL_COMPONENT_TYPE_PLANE_SEMANTIC_LABEL_EXT);
    }

    auto discoverSpatialEntities = [&](XrSpatialContextEXT spatialContext, XrTime time) {
      XrSpatialDiscoverySnapshotCreateInfoEXT snapshotCreateInfo{XR_TYPE_SPATIAL_DISCOVERY_SNAPSHOT_CREATE_INFO_EXT};
      snapshotCreateInfo.componentTypeCount = snapshotComponents.size();
      snapshotCreateInfo.componentTypes = snapshotComponents.data();
      CHK_XR(xrCreateSpatialDiscoverySnapshotAsyncEXT(spatialContext, &snapshotCreateInfo, &future));

      waitUntilReady(future);

      XrCreateSpatialDiscoverySnapshotCompletionInfoEXT completionInfo{XR_TYPE_CREATE_SPATIAL_DISCOVERY_SNAPSHOT_COMPLETION_INFO_EXT};
      completionInfo.baseSpace = localSpace;
      completionInfo.time = time;
      completionInfo.future = future;

      XrCreateSpatialDiscoverySnapshotCompletionEXT completion{XR_TYPE_CREATE_SPATIAL_DISCOVERY_SNAPSHOT_COMPLETION_EXT};
      CHK_XR(xrCreateSpatialDiscoverySnapshotCompleteEXT(spatialContext, &completionInfo, &completion));
      if (completion.futureResult == XR_SUCCESS) {

        // Query for the semantic label component data
        XrSpatialComponentDataQueryConditionEXT queryCond{XR_TYPE_SPATIAL_COMPONENT_DATA_QUERY_CONDITION_EXT};
        queryCond.componentTypeCount = snapshotComponents.size();
        queryCond.componentTypes = snapshotComponents.data();

        XrSpatialComponentDataQueryResultEXT queryResult{XR_TYPE_SPATIAL_COMPONENT_DATA_QUERY_RESULT_EXT};
        CHK_XR(xrQuerySpatialComponentDataEXT(completion.snapshot, &queryCond, &queryResult));

        std::vector<XrSpatialEntityIdEXT> entityIds(queryResult.entityIdCountOutput);
        std::vector<XrSpatialEntityTrackingStateEXT> entityStates(queryResult.entityIdCountOutput);
        queryResult.entityIdCapacityInput = entityIds.size();
        queryResult.entityIds = entityIds.data();
        queryResult.entityStateCapacityInput = entityStates.size();
        queryResult.entityStates = entityStates.data();

        std::vector<XrSpatialBounded2DDataEXT> bounded2D(queryResult.entityIdCountOutput);
        XrSpatialComponentBounded2DListEXT bounded2DList{XR_TYPE_SPATIAL_COMPONENT_BOUNDED_2D_LIST_EXT};
        bounded2DList.boundCount = bounded2D.size();
        bounded2DList.bounds = bounded2D.data();
        queryResult.next = &bounded2DList;

        std::vector<XrSpatialPolygon2DDataEXT> polygons;
        XrSpatialComponentPolygon2DListEXT polygonList{XR_TYPE_SPATIAL_COMPONENT_POLYGON_2D_LIST_EXT};
        if (supportsPolygon2DComponent) {
          polygons.resize(queryResult.entityIdCountOutput);
          polygonList.polygonCount = polygons.size();
          polygonList.polygons = polygons.data();
          polygonList.next = queryResult.next;
          queryResult.next = &polygonList;
        }

        std::vector<XrSpatialPlaneSemanticLabelEXT> semanticLabels;
        XrSpatialComponentPlaneSemanticLabelListEXT semanticLabelsList{XR_TYPE_SPATIAL_COMPONENT_PLANE_SEMANTIC_LABEL_LIST_EXT};
        if (supportsSemanticLabelComponent) {
          semanticLabels.resize(queryResult.entityIdCountOutput);
          semanticLabelsList.semanticLabelCount = semanticLabels.size();
          semanticLabelsList.semanticLabels = semanticLabels.data();
          semanticLabelsList.next = queryResult.next;
          queryResult.next = &semanticLabelsList;
        }

        CHK_XR(xrQuerySpatialComponentDataEXT(completion.snapshot, &queryCond, &queryResult));

        for (int32_t i = 0; i < queryResult.entityIdCountOutput; ++i) {
          if (entityStates[i] != XR_SPATIAL_ENTITY_TRACKING_STATE_TRACKING_EXT) {
            continue;
          }

          // 2D bounds for entity entityIds[i] is bounded2D[i].extents centered on bounded2D[i].center.

          if (supportsPolygon2DComponent) {
            // 2D polygon for entity entityIds[i] is the buffer represented by polygons[i].bufferId.
            // Application uses flink:xrGetSpatialBufferVector2fEXT to get the buffer data.
          }

          if (supportsSemanticLabelComponent) {
            // semantic label for entity entityIds[i] is semanticLabels[i].
          }
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
      XrEventDataBuffer event = {XR_TYPE_EVENT_DATA_BUFFER};
      XrResult result = xrPollEvent(instance, &event);
      if (result == XR_SUCCESS) {
          switch (event.type) {
              case XR_TYPE_EVENT_DATA_SPATIAL_DISCOVERY_RECOMMENDED_EXT: {
                  const XrEventDataSpatialDiscoveryRecommendedEXT& eventdata =
                      *reinterpret_cast<XrEventDataSpatialDiscoveryRecommendedEXT*>(&event);
                  // Discover spatial entities for the context that we received the "discovery
                  // recommended" event for.
                  discoverSpatialEntities(eventdata.spatialContext, time);
                  break;
              }
          }
      }

      // ...
      // Finish frame loop
      // ...
    }

## New Structures

- [XrSpatialCapabilityConfigurationPlaneTrackingEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#XrSpatialCapabilityConfigurationPlaneTrackingEXT)
- [XrSpatialPolygon2DDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#XrSpatialPolygon2DDataEXT)
- Extending [XrSpatialComponentDataQueryResultEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryResultEXT) :

  - [XrSpatialComponentMesh2DListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#XrSpatialComponentMesh2DListEXT)
  - [XrSpatialComponentPlaneAlignmentListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#XrSpatialComponentPlaneAlignmentListEXT)
  - [XrSpatialComponentPlaneSemanticLabelListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#XrSpatialComponentPlaneSemanticLabelListEXT)
  - [XrSpatialComponentPolygon2DListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#XrSpatialComponentPolygon2DListEXT)

## New Enums

- [XrSpatialPlaneAlignmentEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#XrSpatialPlaneAlignmentEXT)
- [XrSpatialPlaneSemanticLabelEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking#XrSpatialPlaneSemanticLabelEXT)

## New Enum Constants

- `XR_EXT_SPATIAL_PLANE_TRACKING_EXTENSION_NAME`
- `XR_EXT_spatial_plane_tracking_SPEC_VERSION`
- Extending [XrSpatialCapabilityEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityEXT) :

  - `XR_SPATIAL_CAPABILITY_PLANE_TRACKING_EXT`
- Extending [XrSpatialComponentTypeEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentTypeEXT) :

  - `XR_SPATIAL_COMPONENT_TYPE_MESH_2D_EXT`
  - `XR_SPATIAL_COMPONENT_TYPE_PLANE_ALIGNMENT_EXT`
  - `XR_SPATIAL_COMPONENT_TYPE_PLANE_SEMANTIC_LABEL_EXT`
  - `XR_SPATIAL_COMPONENT_TYPE_POLYGON_2D_EXT`
- Extending [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) :

  - `XR_TYPE_SPATIAL_CAPABILITY_CONFIGURATION_PLANE_TRACKING_EXT`
  - `XR_TYPE_SPATIAL_COMPONENT_MESH_2D_LIST_EXT`
  - `XR_TYPE_SPATIAL_COMPONENT_PLANE_ALIGNMENT_LIST_EXT`
  - `XR_TYPE_SPATIAL_COMPONENT_PLANE_SEMANTIC_LABEL_LIST_EXT`
  - `XR_TYPE_SPATIAL_COMPONENT_POLYGON_2D_LIST_EXT`

## Issues

## Version History

- Revision 1, 2024-07-02 (Nihav Jain, Google)

  - Initial extension description