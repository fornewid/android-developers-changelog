---
title: https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity
url: https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity
source: md.txt
---

### XR_EXT_spatial_entity

**Name String**

`XR_EXT_spatial_entity`

**Extension Type**

Instance extension

**Registered Extension Number**

741

**Revision**

1

**Ratification Status**

Ratified

**Extension and Version Dependencies**

`XR_EXT_future`

**Contributors**

Nihav Jain, Google  

Jared Finder, Google  

Natalie Fleury, Meta  

Yuichi Taguchi, Meta  

Ron Bessems, Meta  

Yin Li, Microsoft  

Karthik Kadappan, Magic Leap  

Jimmy Alamparambil, ByteDance  

Zhipeng Liu, ByteDance  

Jun Yan, ByteDance

## Overview

This extension introduces the concepts and foundations for scene understanding and spatial reasoning in OpenXR. This unifies several related but distinct areas of functionality, which are enumerated, configured, and interacted with in a broadly uniform way as defined by this extension. As this extension lacks concrete definitions of any one of these functional areas, the formal specification text tends to be somewhat abstract. Examples included in this extension specification text refers at times to functionality defined in a forthcoming or hypothetical related extension for the purpose of illustration, without inherently limiting or specifying such additional functionality.

The broad pieces of this extension are the following:

- [Spatial entities](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#ext_spatial_entity_entity) : The functionality is centered around *entities* , which provide very little functionality on their own.
- [Spatial components](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#ext_spatial_entity_common_components) : These entities have *components* associated with them that provide data and behaviors.
- [Spatial component types](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#ext_spatial_entity_component_types) : Each spatial component is of a specific *component type* , and any given *entity* has at most a single *component* of any given *component type* .
- [Spatial context](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#ext_spatial_entity_context) : All spatial entity interaction occurs in a *context* after an initialization and configuration phase.
- [Spatial capabilities](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#ext_spatial_entity_capabilities_setup) : Spatial entity manipulation is broadly provided by *capabilities* . A capability is some unit of functionality, for example (without limitation) application-defined anchors, plane detection, or image tracking. Each *capability* is typically defined in a separate extension (enabled at instance creation as usual) and is enabled for a specific *context* at the time of creation.
- Each *capability* is associated with a set of *component types* for which *components* are present on every entity exposed by that *capability* . The extension defining a *capability* specifies which *component types* are mandatory for the capability ("guaranteed"), while that same extension or others **may** specify **optional** *component types* provided by some potential implementations. Any number of *capabilities* might provide entities with components of a given *component type* , which are uniformly usable no matter the *capability* that produced it.
- [Spatial capability features](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#ext_spatial_entity_capability_features) : Further, some capabilities require configuration, and thus are parameterized by *capability features* .

This extension provides a mechanism for enumerating the *components* provided by each *capability* supported on the current system, both the mandatory and any **optional** *components* .

As some implementations **may** require different degrees of parameterization for *capabilities* , this extension provides a mechanism for enumerating the supported *capability features* associated with a given *capability* in the current system.

This extension also defines several common *components* expected to be used across a wide range of *capabilities* .

## Spatial Entity

Spatial entities are entities that exist in some space, that have various associated data organized into components. They **may** be any of the following:

- Physical (e.g. planar surfaces like walls and floors, objects like chairs and bookcases, etc.)
- Virtual (e.g. content placed and shared by another application or user),
- App-defined (e.g. application marking an area as the "living room" or "kitchen", or marking a point as the location to place the TV etc.)

Things which are exposed via the action system, like controllers or eye gaze, are not intended to be modeled as spatial entities.

Spatial entities in OpenXR are modeled as an *Entity-Component system* . Each spatial entity has a set of components, and each component provides a unique set of data and behaviors for that entity.

Spatial entities are represented by either an `XrSpatialEntityIdEXT` atom or an [XrSpatialEntityEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialEntityEXT) handle, details of which are provided in the [Spatial Entity Representations](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#ext_spatial_entity_representations) section.

## Spatial Component Types

A spatial entity has one or more components which provide data or behaviors for that entity. See [Common Components](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#ext_spatial_entity_common_components) for some common components defined by this extension.

    typedef enum XrSpatialComponentTypeEXT {
        XR_SPATIAL_COMPONENT_TYPE_BOUNDED_2D_EXT = 1,
        XR_SPATIAL_COMPONENT_TYPE_BOUNDED_3D_EXT = 2,
        XR_SPATIAL_COMPONENT_TYPE_PARENT_EXT = 3,
        XR_SPATIAL_COMPONENT_TYPE_MESH_3D_EXT = 4,
        XR_SPATIAL_COMPONENT_TYPE_PLANE_ALIGNMENT_EXT = 1000741000,
        XR_SPATIAL_COMPONENT_TYPE_MESH_2D_EXT = 1000741001,
        XR_SPATIAL_COMPONENT_TYPE_POLYGON_2D_EXT = 1000741002,
        XR_SPATIAL_COMPONENT_TYPE_PLANE_SEMANTIC_LABEL_EXT = 1000741003,
        XR_SPATIAL_COMPONENT_TYPE_MARKER_EXT = 1000743000,
        XR_SPATIAL_COMPONENT_TYPE_OBJECT_SEMANTIC_LABEL_EXT = 1000744000,
        XR_SPATIAL_COMPONENT_TYPE_KEYBOARD_SEMANTIC_LABEL_EXT = 1000744001,
        XR_SPATIAL_COMPONENT_TYPE_MOUSE_SEMANTIC_LABEL_EXT = 1000744002,
        XR_SPATIAL_COMPONENT_TYPE_ANCHOR_EXT = 1000762000,
        XR_SPATIAL_COMPONENT_TYPE_PERSISTENCE_EXT = 1000763000,
        XR_SPATIAL_COMPONENT_TYPE_IMAGE_2D_EXT = 1000782000,
        XR_SPATIAL_COMPONENT_TYPE_MESH_3D_NORMALS_EXT = 1000783000,
        XR_SPATIAL_COMPONENT_TYPE_MESH_3D_VERTEX_SEMANTIC_LABELS_EXT = 1000783001,
        XR_SPATIAL_COMPONENT_TYPE_MESH_3D_TRIANGLE_SEMANTIC_LABELS_EXT = 1000783002,
        XR_SPATIAL_COMPONENT_TYPE_OBJECT_SEMANTIC_LABEL_ANDROID = 1000785000,
        XR_SPATIAL_COMPONENT_TYPE_RAYCAST_RESULT_ANDROID = 1000786000,
        XR_SPATIAL_COMPONENT_TYPE_SUBSUMED_BY_ANDROID = 1000791000,
        XR_SPATIAL_COMPONENT_TYPE_ROOM_ANDROIDSYS = 1000792002,
        XR_SPATIAL_COMPONENT_TYPE_MATERIAL_TYPE_ANDROIDSYS = 1000792003,
        XR_SPATIAL_COMPONENT_TYPE_CONFIDENCE_ANDROIDSYS = 1000792004,
        XR_SPATIAL_COMPONENT_TYPE_ROOM_EMPTINESS_ANDROIDSYS = 1000792005,
        XR_SPATIAL_COMPONENT_TYPE_OCCUPANCY_GRID_ANDROIDX1 = 1000793000,
        XR_SPATIAL_COMPONENT_TYPE_ANNOTATION_QUAD_ANDROID = 1000794000,
        XR_SPATIAL_COMPONENT_TYPE_STREETSCAPE_GEOMETRY_METADATA_ANDROIDX2 = 1000798000,
        XR_SPATIAL_COMPONENT_TYPE_MAX_ENUM_EXT = 0x7FFFFFFF
    } XrSpatialComponentTypeEXT;

The [XrSpatialComponentTypeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentTypeEXT) enumeration identifies the different types of components that the runtime **may** support.

Not all component types listed are provided by this extension on its own: some require additional extensions to be enabled at instance creation time, as documented.

The enumerants have the following values:

Enum Description

`XR_SPATIAL_COMPONENT_TYPE_BOUNDED_2D_EXT`

Component that provides the 2D bounds for a spatial entity. Corresponding list structure is [XrSpatialComponentBounded2DListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentBounded2DListEXT) ; Corresponding data structure is [XrSpatialBounded2DDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBounded2DDataEXT)

`XR_SPATIAL_COMPONENT_TYPE_BOUNDED_3D_EXT`

Component that provides the 3D bounds for a spatial entity. Corresponding list structure is [XrSpatialComponentBounded3DListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentBounded3DListEXT) ; Corresponding data structure is [XrBoxf](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrBoxf)

`XR_SPATIAL_COMPONENT_TYPE_PARENT_EXT`

Component that provides the `XrSpatialEntityIdEXT` of the parent for a spatial entity. Corresponding list structure is [XrSpatialComponentParentListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentParentListEXT) ; Corresponding data structure is `XrSpatialEntityIdEXT`

`XR_SPATIAL_COMPONENT_TYPE_MESH_3D_EXT`

Component that provides a 3D mesh for a spatial entity. Corresponding list structure is [XrSpatialComponentMesh3DListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentMesh3DListEXT) ; Corresponding data structure is [XrSpatialMeshDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialMeshDataEXT)

`XR_SPATIAL_COMPONENT_TYPE_PLANE_ALIGNMENT_EXT`

Component that provides the plane alignment enum for a spatial entity. Corresponding list structure is [XrSpatialComponentPlaneAlignmentListEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentPlaneAlignmentListEXT) ; Corresponding data structure is [XrSpatialPlaneAlignmentEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialPlaneAlignmentEXT) (Added by the `XR_EXT_spatial_plane_tracking` extension)

`XR_SPATIAL_COMPONENT_TYPE_MESH_2D_EXT`

Component that provides a 2D mesh for a spatial entity. Corresponding list structure is [XrSpatialComponentMesh2DListEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentMesh2DListEXT) ; Corresponding data structure is [XrSpatialMeshDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialMeshDataEXT) (Added by the `XR_EXT_spatial_plane_tracking` extension)

`XR_SPATIAL_COMPONENT_TYPE_POLYGON_2D_EXT`

Component that provides a 2D boundary polygon for a spatial entity. Corresponding list structure is [XrSpatialComponentPolygon2DListEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentPolygon2DListEXT) ; Corresponding data structure is [XrSpatialPolygon2DDataEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialPolygon2DDataEXT) (Added by the `XR_EXT_spatial_plane_tracking` extension)

`XR_SPATIAL_COMPONENT_TYPE_PLANE_SEMANTIC_LABEL_EXT`

Component that provides a semantic label for a plane. Corresponding list structure is [XrSpatialComponentPlaneSemanticLabelListEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentPlaneSemanticLabelListEXT) ; Corresponding data structure is [XrSpatialPlaneSemanticLabelEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialPlaneSemanticLabelEXT) (Added by the `XR_EXT_spatial_plane_tracking` extension)

`XR_SPATIAL_COMPONENT_TYPE_MARKER_EXT`

A component describing the marker type, id and location. Corresponding list structure is [XrSpatialComponentMarkerListEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentMarkerListEXT) ; Corresponding data structure is [XrSpatialMarkerDataEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialMarkerDataEXT) (Added by the `XR_EXT_spatial_marker_tracking` extension)

`XR_SPATIAL_COMPONENT_TYPE_OBJECT_SEMANTIC_LABEL_EXT`

Component that provides a semantic label for a scene; Corresponding list structure is [XrSpatialComponentObjectSemanticLabelListEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentObjectSemanticLabelListEXT) . Corresponding data structure is [XrSpatialObjectSemanticLabelEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialObjectSemanticLabelEXT) . (Added by the `XR_EXT_spatial_object_tracking` extension)

`XR_SPATIAL_COMPONENT_TYPE_KEYBOARD_SEMANTIC_LABEL_EXT`

Component that provides a semantic label for a keyboard; Corresponding list structure is [XrSpatialComponentKeyboardSemanticLabelListEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentKeyboardSemanticLabelListEXT) . Corresponding data structure is [XrSpatialKeyboardSemanticLabelEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialKeyboardSemanticLabelEXT) (Added by the `XR_EXT_spatial_object_tracking` extension)

`XR_SPATIAL_COMPONENT_TYPE_MOUSE_SEMANTIC_LABEL_EXT`

Component that provides a semantic label for a mouse; Corresponding list structure is [XrSpatialComponentMouseSemanticLabelListEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentMouseSemanticLabelListEXT) . Corresponding data structure is [XrSpatialMouseSemanticLabelEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialMouseSemanticLabelEXT) (Added by the `XR_EXT_spatial_object_tracking` extension)

`XR_SPATIAL_COMPONENT_TYPE_ANCHOR_EXT`

Component that provides the location for an anchor. Corresponding list structure is [XrSpatialComponentAnchorListEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentAnchorListEXT) ; Corresponding data structure is [XrPosef](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrPosef) (Added by the `XR_EXT_spatial_anchor` extension)

`XR_SPATIAL_COMPONENT_TYPE_PERSISTENCE_EXT`

Component that provides the persisted UUID for a spatial entity. Corresponding list structure is [XrSpatialComponentPersistenceListEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentPersistenceListEXT) ; Corresponding data structure is [XrSpatialPersistenceDataEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialPersistenceDataEXT) (Added by the `XR_EXT_spatial_persistence` extension)

`XR_SPATIAL_COMPONENT_TYPE_IMAGE_2D_EXT`

A component describing the planar image type. Corresponding list structure is [XrSpatialComponentImage2DListEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentImage2DListEXT) ; Corresponding data structure is [XrSpatialImageSizeEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialImageSizeEXT) . (Added by the `XR_EXT_spatial_image_tracking` extension)

`XR_SPATIAL_COMPONENT_TYPE_MESH_3D_NORMALS_EXT`

Component that provides the normals for the 3D mesh of a spatial entity. Corresponding list structure is [XrSpatialComponentMesh3DNormalsListEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentMesh3DNormalsListEXT) ; Corresponding data structure is [XrSpatialBufferEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferEXT) (Added by the `XR_EXT_spatial_mesh_tracking` extension)

`XR_SPATIAL_COMPONENT_TYPE_MESH_3D_VERTEX_SEMANTIC_LABELS_EXT`

Component that provides the per-vertex semantic labels for the 3D mesh of a spatial entity. Corresponding list structure is [XrSpatialComponentMesh3DVertexSemanticLabelsListEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentMesh3DVertexSemanticLabelsListEXT) ; Corresponding data structure is [XrSpatialBufferEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferEXT) ; Data within the buffer maps to [XrSpatialMeshSemanticLabelEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialMeshSemanticLabelEXT) (Added by the `XR_EXT_spatial_mesh_tracking` extension)

`XR_SPATIAL_COMPONENT_TYPE_MESH_3D_TRIANGLE_SEMANTIC_LABELS_EXT`

Component that provides the per-triangle-face semantic labels for the 3D mesh of a spatial entity. Corresponding list structure is [XrSpatialComponentMesh3DTriangleSemanticLabelsListEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentMesh3DTriangleSemanticLabelsListEXT) ; Corresponding data structure is [XrSpatialBufferEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferEXT) ; Data within the buffer maps to [XrSpatialMeshSemanticLabelEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialMeshSemanticLabelEXT) (Added by the `XR_EXT_spatial_mesh_tracking` extension)

`XR_SPATIAL_COMPONENT_TYPE_OBJECT_SEMANTIC_LABEL_ANDROID`

Component that provides a semantic label for a object; Corresponding list structure is [XrSpatialComponentObjectSemanticLabelListANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentObjectSemanticLabelListANDROID) ; Corresponding data structure is [XrSpatialObjectSemanticLabelANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialObjectSemanticLabelANDROID) (Added by the `XR_ANDROID_spatial_object_tracking` extension)

`XR_SPATIAL_COMPONENT_TYPE_RAYCAST_RESULT_ANDROID`

Component that provides the pose of a raycast hit on an entity. Corresponding list structure is [XrSpatialComponentRaycastResultListANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentRaycastResultListANDROID) ; Corresponding data structure is [XrSpatialRaycastResultDataANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialRaycastResultDataANDROID) (Added by the `XR_ANDROID_spatial_discovery_raycast` extension)

`XR_SPATIAL_COMPONENT_TYPE_SUBSUMED_BY_ANDROID`

Component that provides entity ID of the entity subsuming the attached entity. Corresponding list structure is [XrSpatialComponentSubsumedByListANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentSubsumedByListANDROID) ; Corresponding data structure is `XrSpatialEntityIdEXT` (Added by the `XR_ANDROID_spatial_component_subsumed_by` extension)

`XR_SPATIAL_COMPONENT_TYPE_ROOM_ANDROIDSYS`

Component that provides the dimensions and the room type of a shoebox; Corresponding list structure is [XrSpatialComponentRoomListANDROIDSYS](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentRoomListANDROIDSYS) ; Corresponding data structure is [XrSpatialRoomDataANDROIDSYS](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialRoomDataANDROIDSYS) (Added by the `XR_ANDROIDSYS_spatial_room_tracking` extension)

`XR_SPATIAL_COMPONENT_TYPE_MATERIAL_TYPE_ANDROIDSYS`

Component that provides the material type of a boudary surface; Corresponding list structure is [XrSpatialComponentMaterialTypeListANDROIDSYS](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentMaterialTypeListANDROIDSYS) ; Corresponding data structure is [XrSpatialMaterialTypeANDROIDSYS](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialMaterialTypeANDROIDSYS) (Added by the `XR_ANDROIDSYS_spatial_room_tracking` extension)

`XR_SPATIAL_COMPONENT_TYPE_CONFIDENCE_ANDROIDSYS`

Component that provides the confidence of a trackable; Corresponding list structure is [XrSpatialComponentConfidenceListANDROIDSYS](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentConfidenceListANDROIDSYS) ; Corresponding data structure is `float` (Added by the `XR_ANDROIDSYS_spatial_room_tracking` extension)

`XR_SPATIAL_COMPONENT_TYPE_ROOM_EMPTINESS_ANDROIDSYS`

Component that provides the emptiness of a room; Corresponding list structure is [XrSpatialComponentRoomEmptinessListANDROIDSYS](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentRoomEmptinessListANDROIDSYS) ; Corresponding data structure is `float` (Added by the `XR_ANDROIDSYS_spatial_room_tracking` extension)

`XR_SPATIAL_COMPONENT_TYPE_OCCUPANCY_GRID_ANDROIDX1`

Component that provides information of occupancy grid on the attached entity. Corresponding list structure is [XrSpatialComponentOccupancyGridListANDROIDX1](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentOccupancyGridListANDROIDX1) ; Corresponding data structure is [XrSpatialOccupancyGridDataANDROIDX1](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialOccupancyGridDataANDROIDX1) (Added by the `XR_ANDROIDX1_spatial_occupancy_grid` extension)

`XR_SPATIAL_COMPONENT_TYPE_ANNOTATION_QUAD_ANDROID`

A component describing a quad annotation. Corresponding list structure is [XrSpatialComponentAnnotationQuadListANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentAnnotationQuadListANDROID) ; Corresponding data structure is [XrSpatialAnnotationQuadDataANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialAnnotationQuadDataANDROID) (Added by the `XR_ANDROID_spatial_annotation_tracking` extension)

`XR_SPATIAL_COMPONENT_TYPE_STREETSCAPE_GEOMETRY_METADATA_ANDROIDX2`

Component that provides the metadata for a streetscape geometry; Corresponding list structure is [XrSpatialComponentStreetscapeGeometryMetadataListANDROIDX2](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentStreetscapeGeometryMetadataListANDROIDX2) ; Corresponding data structure is [XrSpatialStreetscapeGeometryMetadataANDROIDX2](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialStreetscapeGeometryMetadataANDROIDX2) (Added by the `XR_ANDROIDX2_geospatial_streetscape` extension)

## Spatial Capabilities and Setup

Spatial capabilities define a runtime's abilities to discover entities that have a guaranteed set of components on them. Applications enable the components of a spatial capability when creating the [XrSpatialContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialContextEXT) , and the runtime in turn **must** provide only the enabled components on discovered entities. e.g. If a runtime reports that one of the components for a given capability is "semantic labels", it means the application **can** enable semantic labels via the configuration for that capability and the runtime **must** only provide the semantic label component if it is configured.

    typedef enum XrSpatialCapabilityEXT {
        XR_SPATIAL_CAPABILITY_PLANE_TRACKING_EXT = 1000741000,
        XR_SPATIAL_CAPABILITY_MARKER_TRACKING_QR_CODE_EXT = 1000743000,
        XR_SPATIAL_CAPABILITY_MARKER_TRACKING_MICRO_QR_CODE_EXT = 1000743001,
        XR_SPATIAL_CAPABILITY_MARKER_TRACKING_ARUCO_MARKER_EXT = 1000743002,
        XR_SPATIAL_CAPABILITY_MARKER_TRACKING_APRIL_TAG_EXT = 1000743003,
        XR_SPATIAL_CAPABILITY_OBJECT_TRACKING_EXT = 1000744000,
        XR_SPATIAL_CAPABILITY_ANCHOR_EXT = 1000762000,
        XR_SPATIAL_CAPABILITY_IMAGE_TRACKING_EXT = 1000782000,
        XR_SPATIAL_CAPABILITY_MESH_TRACKING_EXT = 1000783000,
        XR_SPATIAL_CAPABILITY_OBJECT_TRACKING_ANDROID = 1000785000,
        XR_SPATIAL_CAPABILITY_DEPTH_RAYCAST_ANDROID = 1000786000,
        XR_SPATIAL_CAPABILITY_ROOM_TRACKING_ANDROIDSYS = 1000792000,
        XR_SPATIAL_CAPABILITY_ROOM_BOUNDARY_TRACKING_ANDROIDSYS = 1000792001,
        XR_SPATIAL_CAPABILITY_ANNOTATION_TRACKING_ANDROID = 1000794000,
        XR_SPATIAL_CAPABILITY_STREETSCAPE_GEOMETRY_ANDROIDX2 = 1000798000,
        XR_SPATIAL_CAPABILITY_MAX_ENUM_EXT = 0x7FFFFFFF
    } XrSpatialCapabilityEXT;

The [XrSpatialCapabilityEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityEXT) enumeration identifies the different types of capabilities that the runtime **may** support.

The enumerants have the following values:

Enum Description

`XR_SPATIAL_CAPABILITY_PLANE_TRACKING_EXT`

Plane tracking (Added by the `XR_EXT_spatial_plane_tracking` extension)

`XR_SPATIAL_CAPABILITY_MARKER_TRACKING_QR_CODE_EXT`

Capability to be able to detect and track QR codes. (Added by the `XR_EXT_spatial_marker_tracking` extension)

`XR_SPATIAL_CAPABILITY_MARKER_TRACKING_MICRO_QR_CODE_EXT`

Capability to be able to detect and track Micro QR codes. (Added by the `XR_EXT_spatial_marker_tracking` extension)

`XR_SPATIAL_CAPABILITY_MARKER_TRACKING_ARUCO_MARKER_EXT`

Capability to be able to detect and track Aruco Markers. (Added by the `XR_EXT_spatial_marker_tracking` extension)

`XR_SPATIAL_CAPABILITY_MARKER_TRACKING_APRIL_TAG_EXT`

Capability to be able to detect and track AprilTags. (Added by the `XR_EXT_spatial_marker_tracking` extension)

`XR_SPATIAL_CAPABILITY_OBJECT_TRACKING_EXT`

Object tracking (Added by the `XR_EXT_spatial_object_tracking` extension)

`XR_SPATIAL_CAPABILITY_ANCHOR_EXT`

Capability to be able to create spatial anchors (Added by the `XR_EXT_spatial_anchor` extension)

`XR_SPATIAL_CAPABILITY_IMAGE_TRACKING_EXT`

Capability to be able to detect and track planar reference images. (Added by the `XR_EXT_spatial_image_tracking` extension)

`XR_SPATIAL_CAPABILITY_MESH_TRACKING_EXT`

Capability to track the mesh of an environment. (Added by the `XR_EXT_spatial_mesh_tracking` extension)

`XR_SPATIAL_CAPABILITY_OBJECT_TRACKING_ANDROID`

Object tracking (Added by the `XR_ANDROID_spatial_object_tracking` extension)

`XR_SPATIAL_CAPABILITY_DEPTH_RAYCAST_ANDROID`

Raycast against depth buffer (Added by the `XR_ANDROID_spatial_discovery_raycast` extension)

`XR_SPATIAL_CAPABILITY_ROOM_TRACKING_ANDROIDSYS`

Capability to track a room (Added by the `XR_ANDROIDSYS_spatial_room_tracking` extension)

`XR_SPATIAL_CAPABILITY_ROOM_BOUNDARY_TRACKING_ANDROIDSYS`

Capability to track a room boundary (Added by the `XR_ANDROIDSYS_spatial_room_tracking` extension)

`XR_SPATIAL_CAPABILITY_ANNOTATION_TRACKING_ANDROID`

Annotation tracking (Added by the `XR_ANDROID_spatial_annotation_tracking` extension)

`XR_SPATIAL_CAPABILITY_STREETSCAPE_GEOMETRY_ANDROIDX2`

Streetscape geometry (Added by the `XR_ANDROIDX2_geospatial_streetscape` extension)

The [xrEnumerateSpatialCapabilitiesEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrEnumerateSpatialCapabilitiesEXT) function is defined as:

    XrResult xrEnumerateSpatialCapabilitiesEXT(
        XrInstance                                  instance,
        XrSystemId                                  systemId,
        uint32_t                                    capabilityCapacityInput,
        uint32_t*                                   capabilityCountOutput,
        XrSpatialCapabilityEXT*                     capabilities);

### Parameter Descriptions

- `instance` is a handle to an [XrInstance](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrInstance) .
- `systemId` is the `XrSystemId` whose spatial capabilities will be enumerated.
- `capabilityCapacityInput` is the capacity of the `capabilities` array, or 0 to indicate a request to retrieve the required capacity.
- `capabilityCountOutput` is the number of capabilities, or the required capacity in the case that `capabilityCapacityInput` is insufficient.
- `capabilities` is an array of [XrSpatialCapabilityEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityEXT) . It **can** be `NULL` if `capabilityCapacityInput` is 0.
- See the [Buffer Size Parameters](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-buffer-size-parameters) section for a detailed description of retrieving the required `capabilities` size.

The application **can** enumerate the list of spatial capabilities supported by a given `XrSystemId` using [xrEnumerateSpatialCapabilitiesEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrEnumerateSpatialCapabilitiesEXT) .

The runtime **must** not enumerate the spatial capabilities whose extension is not enabled for `instance` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrEnumerateSpatialCapabilitiesEXT-extension-notenabled) The `XR_EXT_spatial_entity` extension **must** be enabled prior to calling [xrEnumerateSpatialCapabilitiesEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrEnumerateSpatialCapabilitiesEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrEnumerateSpatialCapabilitiesEXT-instance-parameter) `instance` **must** be a valid [XrInstance](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrInstance) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrEnumerateSpatialCapabilitiesEXT-capabilityCountOutput-parameter) `capabilityCountOutput` **must** be a pointer to a `uint32_t` value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrEnumerateSpatialCapabilitiesEXT-capabilities-parameter) If `capabilityCapacityInput` is not `0` , `capabilities` **must** be a pointer to an array of `capabilityCapacityInput` [XrSpatialCapabilityEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityEXT) values

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

The [xrEnumerateSpatialCapabilityComponentTypesEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrEnumerateSpatialCapabilityComponentTypesEXT) function is defined as:

    XrResult xrEnumerateSpatialCapabilityComponentTypesEXT(
        XrInstance                                  instance,
        XrSystemId                                  systemId,
        XrSpatialCapabilityEXT                      capability,
        XrSpatialCapabilityComponentTypesEXT*       capabilityComponents);

### Parameter Descriptions

- `instance` is a handle to an [XrInstance](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrInstance) .
- `systemId` is the `XrSystemId` whose spatial capability components will be enumerated.
- `capability` is the [XrSpatialCapabilityEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityEXT) for which the components will be enumerated.
- `capabilityComponents` is a pointer to an [XrSpatialCapabilityComponentTypesEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityComponentTypesEXT) , which is an input/output structure in which an application-allocated array is populated.

This function enumerates the component types that the given capability provides on its entities in the system as configured.

The application **can** use the component types enumerated in [XrSpatialCapabilityComponentTypesEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityComponentTypesEXT) :: `componentTypes` to understand the full set of components that the `systemId` supports for `capability` and **can** use this list to determine what a valid configuration for `capability` is when creating an [XrSpatialContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialContextEXT) for it.

The runtime **must** return `XR_ERROR_SPATIAL_CAPABILITY_UNSUPPORTED_EXT` if `capability` is not enumerated by [xrEnumerateSpatialCapabilitiesEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrEnumerateSpatialCapabilitiesEXT) .

The runtime **must** not enumerate the spatial component types whose extension is not enabled for `instance` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrEnumerateSpatialCapabilityComponentTypesEXT-extension-notenabled) The `XR_EXT_spatial_entity` extension **must** be enabled prior to calling [xrEnumerateSpatialCapabilityComponentTypesEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrEnumerateSpatialCapabilityComponentTypesEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrEnumerateSpatialCapabilityComponentTypesEXT-instance-parameter) `instance` **must** be a valid [XrInstance](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrInstance) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrEnumerateSpatialCapabilityComponentTypesEXT-capability-parameter) `capability` **must** be a valid [XrSpatialCapabilityEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityEXT) value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrEnumerateSpatialCapabilityComponentTypesEXT-capabilityComponents-parameter) `capabilityComponents` **must** be a pointer to an [XrSpatialCapabilityComponentTypesEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityComponentTypesEXT) structure

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

The [XrSpatialCapabilityComponentTypesEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityComponentTypesEXT) structure is defined as:

    typedef struct XrSpatialCapabilityComponentTypesEXT {
        XrStructureType               type;
        void*                         next;
        uint32_t                      componentTypeCapacityInput;
        uint32_t                      componentTypeCountOutput;
        XrSpatialComponentTypeEXT*    componentTypes;
    } XrSpatialCapabilityComponentTypesEXT;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.
- `componentTypeCapacityInput` is the capacity of the array, or 0 to indicate a request to retrieve the required capacity.
- `componentTypeCountOutput` is the number of component types, or the required capacity in the case that `componentTypeCapacityInput` is insufficient.
- `componentTypes` is an array of [XrSpatialComponentTypeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentTypeEXT) . It **can** be `NULL` if `componentTypeCapacityInput` is 0.
- See the [Buffer Size Parameters](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-buffer-size-parameters) section for a detailed description of retrieving the required `componentTypes` size.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialCapabilityComponentTypesEXT-extension-notenabled) The `XR_EXT_spatial_entity` extension **must** be enabled prior to using [XrSpatialCapabilityComponentTypesEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityComponentTypesEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialCapabilityComponentTypesEXT-type-type) `type` **must** be `XR_TYPE_SPATIAL_CAPABILITY_COMPONENT_TYPES_EXT`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialCapabilityComponentTypesEXT-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialCapabilityComponentTypesEXT-componentTypes-parameter) If `componentTypeCapacityInput` is not `0` , `componentTypes` **must** be a pointer to an array of `componentTypeCapacityInput` [XrSpatialComponentTypeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentTypeEXT) values

## Spatial capability features

    typedef enum XrSpatialCapabilityFeatureEXT {
        XR_SPATIAL_CAPABILITY_FEATURE_MARKER_TRACKING_FIXED_SIZE_MARKERS_EXT = 1000743000,
        XR_SPATIAL_CAPABILITY_FEATURE_MARKER_TRACKING_STATIC_MARKERS_EXT = 1000743001,
        XR_SPATIAL_CAPABILITY_FEATURE_OBJECT_SEMANTIC_LABEL_SUBSET_EXT = 1000744000,
        XR_SPATIAL_CAPABILITY_FEATURE_SPHERE_BOUNDS_FILTER_ANDROID = 1000761000,
        XR_SPATIAL_CAPABILITY_FEATURE_BOX_BOUNDS_FILTER_ANDROID = 1000761001,
        XR_SPATIAL_CAPABILITY_FEATURE_FRUSTUM_BOUNDS_FILTER_ANDROID = 1000761002,
        XR_SPATIAL_CAPABILITY_FEATURE_IMAGE_TRACKING_AUTOMATIC_SIZE_IMAGES_EXT = 1000782000,
        XR_SPATIAL_CAPABILITY_FEATURE_IMAGE_TRACKING_STATIC_IMAGES_EXT = 1000782001,
        XR_SPATIAL_CAPABILITY_FEATURE_IMAGE_TRACKING_FIXED_SIZE_IMAGES_EXT = 1000782002,
        XR_SPATIAL_CAPABILITY_FEATURE_TRACK_WATERTIGHT_MESH_EXT = 1000783000,
        XR_SPATIAL_CAPABILITY_FEATURE_MAX_ENUM_EXT = 0x7FFFFFFF
    } XrSpatialCapabilityFeatureEXT;

Some capabilities have parameters exposed to the application to configure how the component data is computed by the runtime. These dimensions of parameterization/configurability are known as capability features. E.g. for an image tracking capability, a runtime **may** support a feature for the application to specify whether the tracked images are stationary or not.

Providing this information to the runtime via a configuration structure **must** not change the set of component types present on the associated entities, e.g. on the tracked image. However, the runtime **may** be able to optimize e.g. the tracking abilities of the image tracking capability and provide a better experience to the application.

Such features are represented by [XrSpatialCapabilityFeatureEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityFeatureEXT) and the application enumerates them by using [xrEnumerateSpatialCapabilityFeaturesEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrEnumerateSpatialCapabilityFeaturesEXT) .

Each capability feature has a corresponding configuration structure to enable it. Such configuration structures **must** be chained to [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityConfigurationBaseHeaderEXT) :: `next` of the corresponding capability.

The enumerants have the following values:

Enum Description

`XR_SPATIAL_CAPABILITY_FEATURE_MARKER_TRACKING_FIXED_SIZE_MARKERS_EXT`

Capability feature to allow applications to specify the size for the markers. Corresponding config structure is [XrSpatialMarkerSizeEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialMarkerSizeEXT) (Added by the `XR_EXT_spatial_marker_tracking` extension)

`XR_SPATIAL_CAPABILITY_FEATURE_MARKER_TRACKING_STATIC_MARKERS_EXT`

Capability feature to allow applications to specify if markers are static. Corresponding config structure is [XrSpatialMarkerStaticOptimizationEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialMarkerStaticOptimizationEXT) (Added by the `XR_EXT_spatial_marker_tracking` extension)

`XR_SPATIAL_CAPABILITY_FEATURE_OBJECT_SEMANTIC_LABEL_SUBSET_EXT`

Spatial feature allowing applications to specify a subset of labels from [XrSpatialObjectSemanticLabelEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialObjectSemanticLabelEXT) for the runtime to track. Corresponding config structure is [XrSpatialFeatureObjectSemanticLabelSubsetEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialFeatureObjectSemanticLabelSubsetEXT) . (Added by the `XR_EXT_spatial_object_tracking` extension)

`XR_SPATIAL_CAPABILITY_FEATURE_SPHERE_BOUNDS_FILTER_ANDROID`

The runtime supports [XrSpatialBoundsSpherefANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialBoundsSpherefANDROID) filter for [XrSpatialDiscoverySnapshotCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialDiscoverySnapshotCreateInfoEXT) ; This does not require any configuration structure to be included during spatial context creation. (Added by the `XR_ANDROID_spatial_discovery_bounds` extension)

`XR_SPATIAL_CAPABILITY_FEATURE_BOX_BOUNDS_FILTER_ANDROID`

The runtime supports [XrSpatialBoundsBoxfANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialBoundsBoxfANDROID) filter for [XrSpatialDiscoverySnapshotCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialDiscoverySnapshotCreateInfoEXT) ; This does not require any configuration structure to be included during spatial context creation. (Added by the `XR_ANDROID_spatial_discovery_bounds` extension)

`XR_SPATIAL_CAPABILITY_FEATURE_FRUSTUM_BOUNDS_FILTER_ANDROID`

The runtime supports [XrSpatialBoundsFrustumfANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialBoundsFrustumfANDROID) filter for [XrSpatialDiscoverySnapshotCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialDiscoverySnapshotCreateInfoEXT) ; This does not require any configuration structure to be included during spatial context creation. (Added by the `XR_ANDROID_spatial_discovery_bounds` extension)

`XR_SPATIAL_CAPABILITY_FEATURE_IMAGE_TRACKING_AUTOMATIC_SIZE_IMAGES_EXT`

The runtime supports automatically deducing the physical size of detected and tracked images. Corresponding config structure is [XrSpatialImageSizeEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialImageSizeEXT) (Added by the `XR_EXT_spatial_image_tracking` extension)

`XR_SPATIAL_CAPABILITY_FEATURE_IMAGE_TRACKING_STATIC_IMAGES_EXT`

The runtime supports [XrSpatialImageStaticOptimizationEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialImageStaticOptimizationEXT) . Corresponding config structure is [XrSpatialImageStaticOptimizationEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialImageStaticOptimizationEXT) . (Added by the `XR_EXT_spatial_image_tracking` extension)

`XR_SPATIAL_CAPABILITY_FEATURE_IMAGE_TRACKING_FIXED_SIZE_IMAGES_EXT`

The runtime supports [XrSpatialImageSizeEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialImageSizeEXT) . Corresponding config structure is [XrSpatialImageSizeEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialImageSizeEXT) (Added by the `XR_EXT_spatial_image_tracking` extension)

`XR_SPATIAL_CAPABILITY_FEATURE_TRACK_WATERTIGHT_MESH_EXT`

Capability feature to track a watertight mesh of the environment. Corresponding config structure is [XrSpatialFeatureTrackWatertightMeshEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialFeatureTrackWatertightMeshEXT) . (Added by the `XR_EXT_spatial_mesh_tracking` extension)

The [xrEnumerateSpatialCapabilityFeaturesEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrEnumerateSpatialCapabilityFeaturesEXT) function is defines as:

    XrResult xrEnumerateSpatialCapabilityFeaturesEXT(
        XrInstance                                  instance,
        XrSystemId                                  systemId,
        XrSpatialCapabilityEXT                      capability,
        uint32_t                                    capabilityFeatureCapacityInput,
        uint32_t*                                   capabilityFeatureCountOutput,
        XrSpatialCapabilityFeatureEXT*              capabilityFeatures);

### Parameter Descriptions

- `instance` is a handle to an [XrInstance](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrInstance) .
- `systemId` is the `XrSystemId` whose spatial capability features will be enumerated.
- `capability` is the [XrSpatialCapabilityEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityEXT) for which the features will be enumerated.
- `capabilityFeatureCapacityInput` is the capacity of the array, or 0 to indicate a request to retrieve the required capacity.
- `capabilityFeatureCountOutput` is the number of features, or the required capacity in the case that `capabilityFeatureCapacityInput` is insufficient.
- `capabilityFeatures` is an array of [XrSpatialCapabilityFeatureEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityFeatureEXT) . It **can** be `NULL` if `capabilityFeatureCapacityInput` is 0.
- See the [Buffer Size Parameters](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-buffer-size-parameters) section for a detailed description of retrieving the required `capabilityFeatures` size.

The application discovers the features supported by a given system for a [XrSpatialCapabilityEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityEXT) by using [xrEnumerateSpatialCapabilityFeaturesEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrEnumerateSpatialCapabilityFeaturesEXT) .

For capabilities that have features exposed, the application selects the feature or features to enable and provides the corresponding configuration structure in the next chain of the capability configuration structures in [XrSpatialContextCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialContextCreateInfoEXT) :: `capabilityConfigs` .

If `capability` is not a capability enumerated by [xrEnumerateSpatialCapabilitiesEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrEnumerateSpatialCapabilitiesEXT) , the runtime **must** return `XR_ERROR_SPATIAL_CAPABILITY_UNSUPPORTED_EXT` .

The runtime **must** not enumerate the spatial capability features whose extension is not enabled for `instance` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrEnumerateSpatialCapabilityFeaturesEXT-extension-notenabled) The `XR_EXT_spatial_entity` extension **must** be enabled prior to calling [xrEnumerateSpatialCapabilityFeaturesEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrEnumerateSpatialCapabilityFeaturesEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrEnumerateSpatialCapabilityFeaturesEXT-instance-parameter) `instance` **must** be a valid [XrInstance](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrInstance) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrEnumerateSpatialCapabilityFeaturesEXT-capability-parameter) `capability` **must** be a valid [XrSpatialCapabilityEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityEXT) value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrEnumerateSpatialCapabilityFeaturesEXT-capabilityFeatureCountOutput-parameter) `capabilityFeatureCountOutput` **must** be a pointer to a `uint32_t` value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrEnumerateSpatialCapabilityFeaturesEXT-capabilityFeatures-parameter) If `capabilityFeatureCapacityInput` is not `0` , `capabilityFeatures` **must** be a pointer to an array of `capabilityFeatureCapacityInput` [XrSpatialCapabilityFeatureEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityFeatureEXT) values

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

## Spatial Context

### Create a spatial context

    XR_DEFINE_HANDLE(XrSpatialContextEXT)

The [XrSpatialContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialContextEXT) handle represents the resources for discovering and updating some number of spatial entities in the environment of the user. Application **can** use this handle to discover and update spatial entities using other functions in this extension.

The [xrCreateSpatialContextAsyncEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialContextAsyncEXT) function is defined as:

    XrResult xrCreateSpatialContextAsyncEXT(
        XrSession                                   session,
        const XrSpatialContextCreateInfoEXT*        createInfo,
        XrFutureEXT*                                future);

### Parameter Descriptions

- `session` is an [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) in which the spatial context will be active.
- `createInfo` is the [XrSpatialContextCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialContextCreateInfoEXT) used to specify the spatial context parameters.
- `future` is a pointer to an `XrFutureEXT` .

The application **can** create an [XrSpatialContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialContextEXT) handle by:

- Providing [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityConfigurationBaseHeaderEXT) derived structures in [XrSpatialContextCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialContextCreateInfoEXT) :: `capabilityConfigs` to enable capabilities and enable components for that capability.
- Configuring the capabilities themselves with the corresponding configuration structures of its [XrSpatialCapabilityFeatureEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityFeatureEXT) .

The runtime **must** return `XR_ERROR_SPATIAL_CAPABILITY_CONFIGURATION_INVALID_EXT` if [XrSpatialContextCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialContextCreateInfoEXT) ::capabilityConfigCount is 0. A spatial context handle needs at least one capability.

The runtime **must** return `XR_ERROR_SPATIAL_CAPABILITY_UNSUPPORTED_EXT` if any capability in the [XrSpatialContextCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialContextCreateInfoEXT) :: `capabilityConfigs` array is not enumerated by [xrEnumerateSpatialCapabilitiesEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrEnumerateSpatialCapabilitiesEXT) .

The runtime **must** return `XR_ERROR_SPATIAL_CAPABILITY_CONFIGURATION_INVALID_EXT` if any [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityConfigurationBaseHeaderEXT) :: `enabledComponentCount` in [XrSpatialContextCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialContextCreateInfoEXT) :: `capabilityConfigs` is 0. A capability configuration is incomplete without a list of component types to enable for that capability.

The runtime **must** return `XR_ERROR_SPATIAL_COMPONENT_UNSUPPORTED_FOR_CAPABILITY_EXT` if any component type listed in [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityConfigurationBaseHeaderEXT) :: `enabledComponents` is not enumerated for [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityConfigurationBaseHeaderEXT) :: `capability` in [xrEnumerateSpatialCapabilityComponentTypesEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrEnumerateSpatialCapabilityComponentTypesEXT) .

If any of the structures in the next chain of [XrSpatialContextCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialContextCreateInfoEXT) :: `capabilityConfigs` corresponds to an [XrSpatialCapabilityFeatureEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityFeatureEXT) that is not enumerated for that capability in [xrEnumerateSpatialCapabilityFeaturesEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrEnumerateSpatialCapabilityFeaturesEXT) , the runtime **must** ignore that [XrSpatialCapabilityFeatureEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityFeatureEXT) structure.

The runtime **must** return `XR_ERROR_SPATIAL_CAPABILITY_CONFIGURATION_INVALID_EXT` if [XrSpatialContextCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialContextCreateInfoEXT) :: `capabilityConfigs` contains multiple structures with the same [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityConfigurationBaseHeaderEXT) :: `capability` .

To ensure optimal use of system resources, the runtime **may** use the configurations provided in [XrSpatialContextCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialContextCreateInfoEXT) array to prepare itself for spatial requests to come in. For example, a runtime that supports plane tracking capability **may** only begin its plane tracking pipeline if a spatial context handle containing the plane tracking capability is created by the application. If the configured capabilities have a long warm-up time, calls to [xrCreateSpatialDiscoverySnapshotAsyncEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialDiscoverySnapshotAsyncEXT) **may** result in an empty snapshot. Application **can** wait for [XrEventDataSpatialDiscoveryRecommendedEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrEventDataSpatialDiscoveryRecommendedEXT) before using [xrCreateSpatialDiscoverySnapshotAsyncEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialDiscoverySnapshotAsyncEXT) to be sure that the underlying tracking services have warmed up.

If a runtime enforces a permission system to control application access to the spatial capabilities being configured for the [XrSpatialContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialContextEXT) , then the runtime **must** return `XR_ERROR_PERMISSION_INSUFFICIENT` if those permissions have not been granted to this application.

This function starts an asynchronous operation and creates a corresponding `XrFutureEXT` , usable with [xrPollFutureEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrPollFutureEXT) and related functions. The return value of this function only indicates whether the parameters were acceptable to schedule the asynchronous operation. The corresponding completion function is [xrCreateSpatialContextCompleteEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialContextCompleteEXT) , usable when a future from this function is in the READY state, with outputs populated by that function in the completion structure [XrCreateSpatialContextCompletionEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrCreateSpatialContextCompletionEXT) .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrCreateSpatialContextAsyncEXT-extension-notenabled) The `XR_EXT_spatial_entity` extension **must** be enabled prior to calling [xrCreateSpatialContextAsyncEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialContextAsyncEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrCreateSpatialContextAsyncEXT-session-parameter) `session` **must** be a valid [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrCreateSpatialContextAsyncEXT-createInfo-parameter) `createInfo` **must** be a pointer to a valid [XrSpatialContextCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialContextCreateInfoEXT) structure
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrCreateSpatialContextAsyncEXT-future-parameter) `future` **must** be a pointer to an `XrFutureEXT` value

### Return Codes

[Success](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`
- `XR_SESSION_LOSS_PENDING`

[Failure](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_HANDLE_INVALID`
- `XR_ERROR_INSTANCE_LOST`
- `XR_ERROR_LIMIT_REACHED`
- `XR_ERROR_OUT_OF_MEMORY`
- `XR_ERROR_PERMISSION_INSUFFICIENT`
- `XR_ERROR_RUNTIME_FAILURE`
- `XR_ERROR_SESSION_LOST`
- `XR_ERROR_SPATIAL_CAPABILITY_CONFIGURATION_INVALID_EXT`
- `XR_ERROR_SPATIAL_CAPABILITY_UNSUPPORTED_EXT`
- `XR_ERROR_SPATIAL_COMPONENT_UNSUPPORTED_FOR_CAPABILITY_EXT`
- `XR_ERROR_VALIDATION_FAILURE`

The [XrSpatialContextCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialContextCreateInfoEXT) structure is defined as:

    typedef struct XrSpatialContextCreateInfoEXT {
        XrStructureType                                                type;
        const void*                                                    next;
        uint32_t                                                       capabilityConfigCount;
        const XrSpatialCapabilityConfigurationBaseHeaderEXT* const*    capabilityConfigs;
    } XrSpatialContextCreateInfoEXT;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.
- `capabilityConfigCount` is a `uint32_t` describing the count of elements in the `capabilityConfigs` array.
- `capabilityConfigs` is a pointer to an array of [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityConfigurationBaseHeaderEXT) pointers.

The [XrSpatialContextCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialContextCreateInfoEXT) structure describes the information to create an [XrSpatialContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialContextEXT) handle.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialContextCreateInfoEXT-extension-notenabled) The `XR_EXT_spatial_entity` extension **must** be enabled prior to using [XrSpatialContextCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialContextCreateInfoEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialContextCreateInfoEXT-type-type) `type` **must** be `XR_TYPE_SPATIAL_CONTEXT_CREATE_INFO_EXT`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialContextCreateInfoEXT-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains) . See also: [XrSpatialContextPersistenceConfigEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextPersistenceConfigEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialContextCreateInfoEXT-capabilityConfigs-parameter) `capabilityConfigs` **must** be a pointer to an array of `capabilityConfigCount` valid [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityConfigurationBaseHeaderEXT) -based structures. See also: [XrSpatialCapabilityConfigurationAnchorEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityConfigurationAnchorEXT) , [XrSpatialCapabilityConfigurationAprilTagEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityConfigurationAprilTagEXT) , [XrSpatialCapabilityConfigurationArucoMarkerEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityConfigurationArucoMarkerEXT) , [XrSpatialCapabilityConfigurationDepthRaycastANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityConfigurationDepthRaycastANDROID) , [XrSpatialCapabilityConfigurationImageTrackingEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityConfigurationImageTrackingEXT) , [XrSpatialCapabilityConfigurationMeshTrackingEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityConfigurationMeshTrackingEXT) , [XrSpatialCapabilityConfigurationMicroQrCodeEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityConfigurationMicroQrCodeEXT) , [XrSpatialCapabilityConfigurationObjectTrackingANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityConfigurationObjectTrackingANDROID) , [XrSpatialCapabilityConfigurationObjectTrackingEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityConfigurationObjectTrackingEXT) , [XrSpatialCapabilityConfigurationPlaneTrackingEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityConfigurationPlaneTrackingEXT) , [XrSpatialCapabilityConfigurationQrCodeEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityConfigurationQrCodeEXT) , [XrSpatialCapabilityConfigurationRoomBoundaryTrackingANDROIDSYS](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityConfigurationRoomBoundaryTrackingANDROIDSYS) , [XrSpatialCapabilityConfigurationRoomTrackingANDROIDSYS](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityConfigurationRoomTrackingANDROIDSYS) , [XrSpatialCapabilityConfigurationStreetscapeGeometryANDROIDX2](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityConfigurationStreetscapeGeometryANDROIDX2)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialContextCreateInfoEXT-capabilityConfigCount-arraylength) The `capabilityConfigCount` parameter **must** be greater than `0`

The [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityConfigurationBaseHeaderEXT) structure is defined as:

    typedef struct XrSpatialCapabilityConfigurationBaseHeaderEXT {
        XrStructureType                     type;
        const void*                         next;
        XrSpatialCapabilityEXT              capability;
        uint32_t                            enabledComponentCount;
        const XrSpatialComponentTypeEXT*    enabledComponents;
    } XrSpatialCapabilityConfigurationBaseHeaderEXT;

This structure is not directly used in the API but instead its child structures **can** be used with [XrSpatialContextCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialContextCreateInfoEXT) to configure spatial capabilities.

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `capability` is an [XrSpatialCapabilityEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityEXT) .
- `enabledComponentCount` is a `uint32_t` describing the count of elements in the `enabledComponents` array.
- `enabledComponents` is a pointer to an array of [XrSpatialComponentTypeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentTypeEXT) .

The runtime **must** return `XR_ERROR_SPATIAL_CAPABILITY_UNSUPPORTED_EXT` if `capability` is not enumerated by [xrEnumerateSpatialCapabilitiesEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrEnumerateSpatialCapabilitiesEXT) . The runtime **must** return `XR_ERROR_SPATIAL_COMPONENT_UNSUPPORTED_FOR_CAPABILITY_EXT` if any component type listed in `enabledComponents` is not enumerated for `capability` in [xrEnumerateSpatialCapabilityComponentTypesEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrEnumerateSpatialCapabilityComponentTypesEXT) .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialCapabilityConfigurationBaseHeaderEXT-extension-notenabled) The `XR_EXT_spatial_entity` extension **must** be enabled prior to using [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityConfigurationBaseHeaderEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialCapabilityConfigurationBaseHeaderEXT-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialCapabilityConfigurationBaseHeaderEXT-capability-parameter) `capability` **must** be a valid [XrSpatialCapabilityEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityEXT) value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialCapabilityConfigurationBaseHeaderEXT-enabledComponents-parameter) `enabledComponents` **must** be a pointer to an array of `enabledComponentCount` valid [XrSpatialComponentTypeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentTypeEXT) values
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialCapabilityConfigurationBaseHeaderEXT-enabledComponentCount-arraylength) The `enabledComponentCount` parameter **must** be greater than `0`

The [xrCreateSpatialContextCompleteEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialContextCompleteEXT) function is defined as:

    XrResult xrCreateSpatialContextCompleteEXT(
        XrSession                                   session,
        XrFutureEXT                                 future,
        XrCreateSpatialContextCompletionEXT*        completion);

### Parameter Descriptions

- `session` is the [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) previously passed to [xrCreateSpatialContextAsyncEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialContextAsyncEXT) :: `session` .
- `future` is the `XrFutureEXT` received from [xrCreateSpatialContextAsyncEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialContextAsyncEXT) .
- `completion` is a pointer to an [XrCreateSpatialContextCompletionEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrCreateSpatialContextCompletionEXT) .

[xrCreateSpatialContextCompleteEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialContextCompleteEXT) completes the asynchronous operation started by [xrCreateSpatialContextAsyncEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialContextAsyncEXT) . The runtime **must** return `XR_ERROR_FUTURE_PENDING_EXT` if `future` is not in ready state. The runtime **must** return `XR_ERROR_FUTURE_INVALID_EXT` if `future` has already been completed or cancelled.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrCreateSpatialContextCompleteEXT-extension-notenabled) The `XR_EXT_spatial_entity` extension **must** be enabled prior to calling [xrCreateSpatialContextCompleteEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialContextCompleteEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrCreateSpatialContextCompleteEXT-session-parameter) `session` **must** be a valid [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrCreateSpatialContextCompleteEXT-completion-parameter) `completion` **must** be a pointer to an [XrCreateSpatialContextCompletionEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrCreateSpatialContextCompletionEXT) structure

### Return Codes

[Success](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`
- `XR_SESSION_LOSS_PENDING`

[Failure](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

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

The [XrCreateSpatialContextCompletionEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrCreateSpatialContextCompletionEXT) structure is defined as:

    typedef struct XrCreateSpatialContextCompletionEXT {
        XrStructureType        type;
        void*                  next;
        XrResult               futureResult;
        XrSpatialContextEXT    spatialContext;
    } XrCreateSpatialContextCompletionEXT;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `futureResult` is the [XrResult](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrResult) of the spatial context creation operation.
- `spatialContext` is an [XrSpatialContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialContextEXT) created using the data and configuration in [xrCreateSpatialContextAsyncEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialContextAsyncEXT) :: `createInfo` .

### Future Return Codes

`futureResult` values:

[Success](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`
- `XR_SESSION_LOSS_PENDING`

[Failure](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_RUNTIME_FAILURE`
- `XR_ERROR_INSTANCE_LOST`
- `XR_ERROR_SESSION_LOST`
- `XR_ERROR_OUT_OF_MEMORY`
- `XR_ERROR_LIMIT_REACHED`
- `XR_ERROR_SPATIAL_CAPABILITY_CONFIGURATION_INVALID_EXT`

If `futureResult` is a success code, `spatialContext` **must** be valid. If `spatialContext` is valid, it remains so only within the lifecycle of [xrCreateSpatialContextAsyncEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialContextAsyncEXT) :: `session` or until the application destroys the `spatialContext` with [xrDestroySpatialContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrDestroySpatialContextEXT) , whichever comes first.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrCreateSpatialContextCompletionEXT-extension-notenabled) The `XR_EXT_spatial_entity` extension **must** be enabled prior to using [XrCreateSpatialContextCompletionEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrCreateSpatialContextCompletionEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrCreateSpatialContextCompletionEXT-type-type) `type` **must** be `XR_TYPE_CREATE_SPATIAL_CONTEXT_COMPLETION_EXT`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrCreateSpatialContextCompletionEXT-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrCreateSpatialContextCompletionEXT-futureResult-parameter) `futureResult` **must** be a valid [XrResult](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrResult) value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrCreateSpatialContextCompletionEXT-spatialContext-parameter) If `spatialContext` is not [XR_NULL_HANDLE](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_NULL_HANDLE) , `spatialContext` **must** be a valid [XrSpatialContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialContextEXT) handle

### Destroy the spatial context

The [xrDestroySpatialContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrDestroySpatialContextEXT) function is defined as:

    XrResult xrDestroySpatialContextEXT(
        XrSpatialContextEXT                         spatialContext);

### Parameter Descriptions

- `spatialContext` is an [XrSpatialContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialContextEXT) previously created by [xrCreateSpatialContextAsyncEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialContextAsyncEXT) .

The application **can** call [xrDestroySpatialContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrDestroySpatialContextEXT) function to release the `spatialContext` handle and the underlying resources when finished with spatial entity discovery and update tasks. If there is no other valid [XrSpatialContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialContextEXT) that was created with the same spatial capabilities as `spatialContext` , this call serves as a suggestion to the runtime to disable the tracking services required for those capabilities to save system resources.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrDestroySpatialContextEXT-extension-notenabled) The `XR_EXT_spatial_entity` extension **must** be enabled prior to calling [xrDestroySpatialContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrDestroySpatialContextEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrDestroySpatialContextEXT-spatialContext-parameter) `spatialContext` **must** be a valid [XrSpatialContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialContextEXT) handle

### Thread Safety

- Access to `spatialContext` , and any child handles, **must** be externally synchronized

### Return Codes

[Success](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`

[Failure](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_HANDLE_INVALID`
- `XR_ERROR_RUNTIME_FAILURE`

## Spatial Entity Representations

### Spatial Entity ID

    XR_DEFINE_ATOM(XrSpatialEntityIdEXT)

`XrSpatialEntityIdEXT` is used to represent any kind of entity discovered by the runtime in the spatial environment of the user. An `XrSpatialEntityIdEXT` is valid for the [XrSpatialContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialContextEXT) in which it is discovered, and the runtime **must** not reuse the same `XrSpatialEntityIdEXT` for different entities within the same [XrSpatialContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialContextEXT) . Also, the runtime **must** not reuse the same `XrSpatialEntityIdEXT` across multiple [XrSpatialContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialContextEXT) within the same [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) regardless of whether it represents the same entity or different ones.

    #define XR_NULL_SPATIAL_ENTITY_ID_EXT 0

[XR_NULL_SPATIAL_ENTITY_ID_EXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XR_NULL_SPATIAL_ENTITY_ID_EXT) is a reserved value representing an invalid `XrSpatialEntityIdEXT` . It **may** be passed to and returned from API functions only when specifically allowed.

### Spatial Entity Handle

    XR_DEFINE_HANDLE(XrSpatialEntityEXT)

The [XrSpatialEntityEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialEntityEXT) handle represents a spatial entity. An application **can** create such a handle to express its interest in a specific entity to the runtime.

### Create Spatial Entity Handle from ID

The [xrCreateSpatialEntityFromIdEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialEntityFromIdEXT) function is defined as:

    XrResult xrCreateSpatialEntityFromIdEXT(
        XrSpatialContextEXT                         spatialContext,
        const XrSpatialEntityFromIdCreateInfoEXT*   createInfo,
        XrSpatialEntityEXT*                         spatialEntity);

### Parameter Descriptions

- `spatialContext` is an [XrSpatialContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialContextEXT) previously created using [xrCreateSpatialContextAsyncEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialContextAsyncEXT) .
- `createInfo` is a pointer to [XrSpatialEntityFromIdCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialEntityFromIdCreateInfoEXT) structure.
- `spatialEntity` is the returned [XrSpatialEntityEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialEntityEXT) handle.

The application **can** use [xrCreateSpatialEntityFromIdEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialEntityFromIdEXT) to create an [XrSpatialEntityEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialEntityEXT) handle which is a reference to an entity that exists in the user's environment.

The runtime **must** return `XR_ERROR_SPATIAL_ENTITY_ID_INVALID_EXT` if [XrSpatialEntityFromIdCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialEntityFromIdCreateInfoEXT) :: `entityId` is not a valid ID for `spatialContext` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrCreateSpatialEntityFromIdEXT-extension-notenabled) The `XR_EXT_spatial_entity` extension **must** be enabled prior to calling [xrCreateSpatialEntityFromIdEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialEntityFromIdEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrCreateSpatialEntityFromIdEXT-spatialContext-parameter) `spatialContext` **must** be a valid [XrSpatialContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialContextEXT) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrCreateSpatialEntityFromIdEXT-createInfo-parameter) `createInfo` **must** be a pointer to a valid [XrSpatialEntityFromIdCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialEntityFromIdCreateInfoEXT) structure
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrCreateSpatialEntityFromIdEXT-spatialEntity-parameter) `spatialEntity` **must** be a pointer to an [XrSpatialEntityEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialEntityEXT) handle

### Return Codes

[Success](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`
- `XR_SESSION_LOSS_PENDING`

[Failure](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_HANDLE_INVALID`
- `XR_ERROR_INSTANCE_LOST`
- `XR_ERROR_LIMIT_REACHED`
- `XR_ERROR_OUT_OF_MEMORY`
- `XR_ERROR_RUNTIME_FAILURE`
- `XR_ERROR_SESSION_LOST`
- `XR_ERROR_SPATIAL_ENTITY_ID_INVALID_EXT`
- `XR_ERROR_VALIDATION_FAILURE`

The [XrSpatialEntityFromIdCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialEntityFromIdCreateInfoEXT) structure is defined as:

    typedef struct XrSpatialEntityFromIdCreateInfoEXT {
        XrStructureType         type;
        const void*             next;
        XrSpatialEntityIdEXT    entityId;
    } XrSpatialEntityFromIdCreateInfoEXT;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.
- `entityId` is the `XrSpatialEntityIdEXT` of the entity that the application wants to create a handle for.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialEntityFromIdCreateInfoEXT-extension-notenabled) The `XR_EXT_spatial_entity` extension **must** be enabled prior to using [XrSpatialEntityFromIdCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialEntityFromIdCreateInfoEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialEntityFromIdCreateInfoEXT-type-type) `type` **must** be `XR_TYPE_SPATIAL_ENTITY_FROM_ID_CREATE_INFO_EXT`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialEntityFromIdCreateInfoEXT-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)

### Destroy Spatial Entity Handle

The [xrDestroySpatialEntityEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrDestroySpatialEntityEXT) function is defined as:

    XrResult xrDestroySpatialEntityEXT(
        XrSpatialEntityEXT                          spatialEntity);

### Parameter Descriptions

- `spatialEntity` is a handle to an [XrSpatialEntityEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialEntityEXT) previously created by a function such as [xrCreateSpatialEntityFromIdEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialEntityFromIdEXT) .

The application **can** use [xrDestroySpatialEntityEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrDestroySpatialEntityEXT) to release the `spatialEntity` handle when it is no longer interested in the entity referenced by this handle.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrDestroySpatialEntityEXT-extension-notenabled) The `XR_EXT_spatial_entity` extension **must** be enabled prior to calling [xrDestroySpatialEntityEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrDestroySpatialEntityEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrDestroySpatialEntityEXT-spatialEntity-parameter) `spatialEntity` **must** be a valid [XrSpatialEntityEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialEntityEXT) handle

### Thread Safety

- Access to `spatialEntity` , and any child handles, **must** be externally synchronized

### Return Codes

[Success](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`

[Failure](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_HANDLE_INVALID`
- `XR_ERROR_RUNTIME_FAILURE`

## Spatial Snapshot

    XR_DEFINE_HANDLE(XrSpatialSnapshotEXT)

The application **can** create spatial snapshots for the purpose of discovering spatial entities or for updating its information about known spatial entities. The [XrSpatialSnapshotEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialSnapshotEXT) handle represents the immutable data for the discovered or updated spatial entities and a subset of their components as selected by the application. The spatial snapshot represents a coherent view of the entities and their component data. Once a snapshot is created, the snapshot's data **must** remain constant while the snapshot is valid.

The application **can** create any number of snapshots it wants but **must** be mindful of the memory being allocated for each new snapshot and **must** destroy the snapshots once it no longer needs them.

### Create discovery snapshot

The [xrCreateSpatialDiscoverySnapshotAsyncEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialDiscoverySnapshotAsyncEXT) function is defined as:

    XrResult xrCreateSpatialDiscoverySnapshotAsyncEXT(
        XrSpatialContextEXT                         spatialContext,
        const XrSpatialDiscoverySnapshotCreateInfoEXT* createInfo,
        XrFutureEXT*                                future);

### Parameter Descriptions

- `spatialContext` is an [XrSpatialContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialContextEXT) previously created by using [xrCreateSpatialContextAsyncEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialContextAsyncEXT) .
- `createInfo` is a pointer to an [XrSpatialDiscoverySnapshotCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialDiscoverySnapshotCreateInfoEXT) .
- `future` is a pointer to an `XrFutureEXT` .

The application **can** discover spatial entities by creating a discovery snapshot by using [xrCreateSpatialDiscoverySnapshotAsyncEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialDiscoverySnapshotAsyncEXT) .

This function starts an asynchronous operation and creates a corresponding `XrFutureEXT` , usable with [xrPollFutureEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrPollFutureEXT) and related functions. The return value of this function only indicates whether the parameters were acceptable to schedule the asynchronous operation. The corresponding completion function is [xrCreateSpatialDiscoverySnapshotCompleteEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialDiscoverySnapshotCompleteEXT) , usable when a future from this function is in the READY state, with outputs populated by that function in the completion structure [XrCreateSpatialDiscoverySnapshotCompletionEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrCreateSpatialDiscoverySnapshotCompletionEXT) .

The application **can** submit multiple discovery snapshot creation requests without needing to wait for the previous one to be completed. The runtime **may** process and complete the snapshot creation in any order. The runtime **may** delay the completion of the discovery snapshot creation to throttle the application if it needs to reduce the use of system resources due to power, thermal or other policies of the device.

The application **can** use [XrSpatialDiscoverySnapshotCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialDiscoverySnapshotCreateInfoEXT) :: `componentTypes` to filter the list of entities and the components whose data the runtime **must** include in the snapshot. If the application provides a valid list of spatial component types in [XrSpatialDiscoverySnapshotCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialDiscoverySnapshotCreateInfoEXT) :: `componentTypes` , then the runtime **must** only include spatial entities in the snapshot that have at least one of the components provided in [XrSpatialDiscoverySnapshotCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialDiscoverySnapshotCreateInfoEXT) :: `componentTypes` . Also, the runtime **must** only include data for only those components in the snapshot.

The runtime **must** return `XR_ERROR_SPATIAL_COMPONENT_NOT_ENABLED_EXT` if any of the [XrSpatialComponentTypeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentTypeEXT) in [XrSpatialDiscoverySnapshotCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialDiscoverySnapshotCreateInfoEXT) :: `componentTypes` are not enabled for the spatial capabilities passed to [XrSpatialContextCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialContextCreateInfoEXT) :: `capabilityConfigs` when creating `spatialContext` .

If the application does not provide a list of spatial component types in [XrSpatialDiscoverySnapshotCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialDiscoverySnapshotCreateInfoEXT) :: `componentTypes` , the runtime **must** include all the spatial entities in the snapshot that have the set of components which are enumerated in [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityConfigurationBaseHeaderEXT) ::enabledComponents for the capabilities configured for `spatialContext` . The runtime **must** include the data for all the enabled components of the capabilities configured for `spatialContext` .

If [XrEventDataReferenceSpaceChangePending](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrEventDataReferenceSpaceChangePending) is queued before the completion of `future` , and [XrEventDataReferenceSpaceChangePending](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrEventDataReferenceSpaceChangePending) :: `poseValid` is false, then the runtime **may** either create an [XrSpatialSnapshotEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialSnapshotEXT) that has no entities in it or set the [XrSpatialEntityTrackingStateEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialEntityTrackingStateEXT) of the entities that are no longer locatable in [XrCreateSpatialDiscoverySnapshotCompletionInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrCreateSpatialDiscoverySnapshotCompletionInfoEXT) :: `baseSpace` at [XrCreateSpatialDiscoverySnapshotCompletionInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrCreateSpatialDiscoverySnapshotCompletionInfoEXT) :: `time` to `XR_SPATIAL_ENTITY_TRACKING_STATE_PAUSED_EXT` or `XR_SPATIAL_ENTITY_TRACKING_STATE_STOPPED_EXT` . The runtime **must** not set [XrCreateSpatialContextCompletionEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrCreateSpatialContextCompletionEXT) :: `futureResult` to an error code because of [XrEventDataReferenceSpaceChangePending](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrEventDataReferenceSpaceChangePending) .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrCreateSpatialDiscoverySnapshotAsyncEXT-extension-notenabled) The `XR_EXT_spatial_entity` extension **must** be enabled prior to calling [xrCreateSpatialDiscoverySnapshotAsyncEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialDiscoverySnapshotAsyncEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrCreateSpatialDiscoverySnapshotAsyncEXT-spatialContext-parameter) `spatialContext` **must** be a valid [XrSpatialContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialContextEXT) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrCreateSpatialDiscoverySnapshotAsyncEXT-createInfo-parameter) `createInfo` **must** be a pointer to a valid [XrSpatialDiscoverySnapshotCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialDiscoverySnapshotCreateInfoEXT) structure
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrCreateSpatialDiscoverySnapshotAsyncEXT-future-parameter) `future` **must** be a pointer to an `XrFutureEXT` value

### Return Codes

[Success](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`
- `XR_SESSION_LOSS_PENDING`

[Failure](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_HANDLE_INVALID`
- `XR_ERROR_INSTANCE_LOST`
- `XR_ERROR_LIMIT_REACHED`
- `XR_ERROR_OUT_OF_MEMORY`
- `XR_ERROR_RUNTIME_FAILURE`
- `XR_ERROR_SESSION_LOST`
- `XR_ERROR_SPATIAL_COMPONENT_NOT_ENABLED_EXT`
- `XR_ERROR_VALIDATION_FAILURE`

The [XrSpatialDiscoverySnapshotCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialDiscoverySnapshotCreateInfoEXT) structure is defined as:

    typedef struct XrSpatialDiscoverySnapshotCreateInfoEXT {
        XrStructureType                     type;
        const void*                         next;
        uint32_t                            componentTypeCount;
        const XrSpatialComponentTypeEXT*    componentTypes;
    } XrSpatialDiscoverySnapshotCreateInfoEXT;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.
- `componentTypeCount` is a `uint32_t` describing the count of elements in the `componentTypes` array.
- `componentTypes` is an array of [XrSpatialComponentTypeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentTypeEXT) .

The [XrSpatialDiscoverySnapshotCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialDiscoverySnapshotCreateInfoEXT) structure describes the information to create an [XrSpatialSnapshotEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialSnapshotEXT) handle when discovering spatial entities.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialDiscoverySnapshotCreateInfoEXT-extension-notenabled) The `XR_EXT_spatial_entity` extension **must** be enabled prior to using [XrSpatialDiscoverySnapshotCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialDiscoverySnapshotCreateInfoEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialDiscoverySnapshotCreateInfoEXT-type-type) `type` **must** be `XR_TYPE_SPATIAL_DISCOVERY_SNAPSHOT_CREATE_INFO_EXT`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialDiscoverySnapshotCreateInfoEXT-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains) . See also: [XrSpatialBoundsBoxfANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialBoundsBoxfANDROID) , [XrSpatialBoundsFrustumfANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialBoundsFrustumfANDROID) , [XrSpatialBoundsSpherefANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialBoundsSpherefANDROID) , [XrSpatialDiscoveryPersistenceUuidFilterEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialDiscoveryPersistenceUuidFilterEXT) , [XrSpatialDiscoveryRoomBoundaryFilterANDROIDSYS](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialDiscoveryRoomBoundaryFilterANDROIDSYS) , [XrSpatialDiscoveryUniqueEntitiesFilterANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialDiscoveryUniqueEntitiesFilterANDROID) , [XrSpatialFilterTrackingStateEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialFilterTrackingStateEXT) , [XrSpatialRaycastInfoANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialRaycastInfoANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialDiscoverySnapshotCreateInfoEXT-componentTypes-parameter) If `componentTypeCount` is not `0` , `componentTypes` **must** be a pointer to an array of `componentTypeCount` valid [XrSpatialComponentTypeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentTypeEXT) values

The [xrCreateSpatialDiscoverySnapshotCompleteEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialDiscoverySnapshotCompleteEXT) function is defined as:

    XrResult xrCreateSpatialDiscoverySnapshotCompleteEXT(
        XrSpatialContextEXT                         spatialContext,
        const XrCreateSpatialDiscoverySnapshotCompletionInfoEXT* createSnapshotCompletionInfo,
        XrCreateSpatialDiscoverySnapshotCompletionEXT* completion);

### Parameter Descriptions

- `spatialContext` is the [XrSpatialContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialContextEXT) previously passed to [xrCreateSpatialDiscoverySnapshotAsyncEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialDiscoverySnapshotAsyncEXT) :: `spatialContext` .
- `createSnapshotCompletionInfo` is a pointer to an [XrCreateSpatialDiscoverySnapshotCompletionInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrCreateSpatialDiscoverySnapshotCompletionInfoEXT) which provides info about the discovery snapshot creation request completion.
- `completion` is a pointer to an [XrCreateSpatialDiscoverySnapshotCompletionEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrCreateSpatialDiscoverySnapshotCompletionEXT) .

[xrCreateSpatialDiscoverySnapshotCompleteEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialDiscoverySnapshotCompleteEXT) completes the asynchronous operation started by [xrCreateSpatialDiscoverySnapshotAsyncEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialDiscoverySnapshotAsyncEXT) . The runtime **must** return `XR_ERROR_FUTURE_PENDING_EXT` if [XrCreateSpatialDiscoverySnapshotCompletionInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrCreateSpatialDiscoverySnapshotCompletionInfoEXT) :: `future` is not in ready state. The runtime **must** return `XR_ERROR_FUTURE_INVALID_EXT` if [XrCreateSpatialDiscoverySnapshotCompletionInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrCreateSpatialDiscoverySnapshotCompletionInfoEXT) :: `future` has already been completed or cancelled.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrCreateSpatialDiscoverySnapshotCompleteEXT-extension-notenabled) The `XR_EXT_spatial_entity` extension **must** be enabled prior to calling [xrCreateSpatialDiscoverySnapshotCompleteEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialDiscoverySnapshotCompleteEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrCreateSpatialDiscoverySnapshotCompleteEXT-spatialContext-parameter) `spatialContext` **must** be a valid [XrSpatialContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialContextEXT) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrCreateSpatialDiscoverySnapshotCompleteEXT-createSnapshotCompletionInfo-parameter) `createSnapshotCompletionInfo` **must** be a pointer to a valid [XrCreateSpatialDiscoverySnapshotCompletionInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrCreateSpatialDiscoverySnapshotCompletionInfoEXT) structure
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrCreateSpatialDiscoverySnapshotCompleteEXT-completion-parameter) `completion` **must** be a pointer to an [XrCreateSpatialDiscoverySnapshotCompletionEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrCreateSpatialDiscoverySnapshotCompletionEXT) structure

### Return Codes

[Success](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`
- `XR_SESSION_LOSS_PENDING`

[Failure](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_FUTURE_INVALID_EXT`
- `XR_ERROR_FUTURE_PENDING_EXT`
- `XR_ERROR_HANDLE_INVALID`
- `XR_ERROR_INSTANCE_LOST`
- `XR_ERROR_LIMIT_REACHED`
- `XR_ERROR_OUT_OF_MEMORY`
- `XR_ERROR_RUNTIME_FAILURE`
- `XR_ERROR_SESSION_LOST`
- `XR_ERROR_TIME_INVALID`
- `XR_ERROR_VALIDATION_FAILURE`

The [XrCreateSpatialDiscoverySnapshotCompletionInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrCreateSpatialDiscoverySnapshotCompletionInfoEXT) structure is defined as:

    typedef struct XrCreateSpatialDiscoverySnapshotCompletionInfoEXT {
        XrStructureType    type;
        const void*        next;
        XrSpace            baseSpace;
        XrTime             time;
        XrFutureEXT        future;
    } XrCreateSpatialDiscoverySnapshotCompletionInfoEXT;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `baseSpace` is the [XrSpace](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpace) in which all the locations of the discovery [XrSpatialSnapshotEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialSnapshotEXT) will be located.
- `time` is the `XrTime` at which all the locations of the discovery [XrSpatialSnapshotEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialSnapshotEXT) will be located.
- `future` is the `XrFutureEXT` received from [xrCreateSpatialDiscoverySnapshotAsyncEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialDiscoverySnapshotAsyncEXT)

The locations in the various component data included in the created snapshot will be represented in `baseSpace` , located at `time` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrCreateSpatialDiscoverySnapshotCompletionInfoEXT-extension-notenabled) The `XR_EXT_spatial_entity` extension **must** be enabled prior to using [XrCreateSpatialDiscoverySnapshotCompletionInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrCreateSpatialDiscoverySnapshotCompletionInfoEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrCreateSpatialDiscoverySnapshotCompletionInfoEXT-type-type) `type` **must** be `XR_TYPE_CREATE_SPATIAL_DISCOVERY_SNAPSHOT_COMPLETION_INFO_EXT`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrCreateSpatialDiscoverySnapshotCompletionInfoEXT-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrCreateSpatialDiscoverySnapshotCompletionInfoEXT-baseSpace-parameter) `baseSpace` **must** be a valid [XrSpace](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpace) handle

The [XrCreateSpatialDiscoverySnapshotCompletionEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrCreateSpatialDiscoverySnapshotCompletionEXT) structure is defined as:

    typedef struct XrCreateSpatialDiscoverySnapshotCompletionEXT {
        XrStructureType         type;
        void*                   next;
        XrResult                futureResult;
        XrSpatialSnapshotEXT    snapshot;
    } XrCreateSpatialDiscoverySnapshotCompletionEXT;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `futureResult` is the [XrResult](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrResult) of the spatial discovery snapshot creation operation.
- `snapshot` is an [XrSpatialSnapshotEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialSnapshotEXT) which **can** be used to query the component data of the discovered spatial entities.

### Future Return Codes

`futureResult` values:

[Success](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`
- `XR_SESSION_LOSS_PENDING`

[Failure](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_RUNTIME_FAILURE`
- `XR_ERROR_INSTANCE_LOST`
- `XR_ERROR_SESSION_LOST`
- `XR_ERROR_OUT_OF_MEMORY`
- `XR_ERROR_LIMIT_REACHED`

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrCreateSpatialDiscoverySnapshotCompletionEXT-extension-notenabled) The `XR_EXT_spatial_entity` extension **must** be enabled prior to using [XrCreateSpatialDiscoverySnapshotCompletionEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrCreateSpatialDiscoverySnapshotCompletionEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrCreateSpatialDiscoverySnapshotCompletionEXT-type-type) `type` **must** be `XR_TYPE_CREATE_SPATIAL_DISCOVERY_SNAPSHOT_COMPLETION_EXT`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrCreateSpatialDiscoverySnapshotCompletionEXT-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrCreateSpatialDiscoverySnapshotCompletionEXT-futureResult-parameter) `futureResult` **must** be a valid [XrResult](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrResult) value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrCreateSpatialDiscoverySnapshotCompletionEXT-snapshot-parameter) If `snapshot` is not [XR_NULL_HANDLE](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_NULL_HANDLE) , `snapshot` **must** be a valid [XrSpatialSnapshotEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialSnapshotEXT) handle

### Discovery Recommendation Event

The [XrEventDataSpatialDiscoveryRecommendedEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrEventDataSpatialDiscoveryRecommendedEXT) structure is defined as:

    typedef struct XrEventDataSpatialDiscoveryRecommendedEXT {
        XrStructureType        type;
        const void*            next;
        XrSpatialContextEXT    spatialContext;
    } XrEventDataSpatialDiscoveryRecommendedEXT;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `spatialContext` is the [XrSpatialContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialContextEXT) for which discovery is being recommended by the runtime.

The application **can** retrieve this event by using [xrPollEvent](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrPollEvent) . The application **can** avoid excessive calls to [xrCreateSpatialDiscoverySnapshotAsyncEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialDiscoverySnapshotAsyncEXT) to discover spatial entities by waiting for this event. If the application creates multiple discovery snapshots with the same [XrSpatialDiscoverySnapshotCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialDiscoverySnapshotCreateInfoEXT) between two [XrEventDataSpatialDiscoveryRecommendedEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrEventDataSpatialDiscoveryRecommendedEXT) events, the resultant snapshots **may** contain the same entities and therefore the snapshot creation and data queries would be wasteful.

Waiting for this event to create a new discovery snapshot ensures that the application is not overloading the system with discovery requests for which the runtime **may** not return any new data and helps avoid the risk of overusing the system resources, and getting throttled due to power or thermal policies of the device. This also helps create parity between runtimes that are discovering spatial entities on the fly with live tracking and runtimes which are providing spatial entities off of a previously recorded state (where the runtime **may** queue the discovery recommendation event only once for each [XrSpatialContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialContextEXT) ).

The runtime **must** not queue this event for notifying the application about changes or adjustments made to the component data of existing spatial entities. The application **can** use the [xrCreateSpatialUpdateSnapshotEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialUpdateSnapshotEXT) to keep track of component data updates for the spatial entities it is interested in.

A runtime **may** queue a discovery recommendation event without waiting for the application to first call [xrCreateSpatialDiscoverySnapshotAsyncEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialDiscoverySnapshotAsyncEXT) . For example, a runtime **may** base the decision of queueing the discovery recommendation event on the configuration of the [XrSpatialContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialContextEXT) , its own understanding of the environment around the user (discovery of new entities or loss of existing ones), or for hinting an appropriate discovery request cadence to the application so as not to overload the system resources. The runtime **may** choose to never queue this event for an [XrSpatialContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialContextEXT) if no entities are found in the user's environment throughout the lifetime of that [XrSpatialContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialContextEXT) .

The runtime **must** not queue this event for a given `spatialContext` until the application completes its creation by using [xrCreateSpatialContextCompleteEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialContextCompleteEXT) .

After the application calls [xrDestroySpatialContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrDestroySpatialContextEXT) , the runtime **must** not queue any more discovery recommendation events for that spatial context nor return any such events for that context from [xrPollEvent](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrPollEvent) .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrEventDataSpatialDiscoveryRecommendedEXT-extension-notenabled) The `XR_EXT_spatial_entity` extension **must** be enabled prior to using [XrEventDataSpatialDiscoveryRecommendedEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrEventDataSpatialDiscoveryRecommendedEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrEventDataSpatialDiscoveryRecommendedEXT-type-type) `type` **must** be `XR_TYPE_EVENT_DATA_SPATIAL_DISCOVERY_RECOMMENDED_EXT`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrEventDataSpatialDiscoveryRecommendedEXT-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)

### Query Component Data

The [xrQuerySpatialComponentDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrQuerySpatialComponentDataEXT) function is defined as:

    XrResult xrQuerySpatialComponentDataEXT(
        XrSpatialSnapshotEXT                        snapshot,
        const XrSpatialComponentDataQueryConditionEXT* queryCondition,
        XrSpatialComponentDataQueryResultEXT*       queryResult);

### Parameter Descriptions

- `snapshot` is an [XrSpatialSnapshotEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialSnapshotEXT) previously provided by [xrCreateSpatialDiscoverySnapshotCompleteEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialDiscoverySnapshotCompleteEXT) or [xrCreateSpatialUpdateSnapshotEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialUpdateSnapshotEXT) .
- `queryCondition` is a pointer to an [XrSpatialComponentDataQueryConditionEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentDataQueryConditionEXT) structure.
- `queryResult` is a pointer to an [XrSpatialComponentDataQueryResultEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentDataQueryResultEXT) structure.

The application **can** use [xrQuerySpatialComponentDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrQuerySpatialComponentDataEXT) to query the component data of the entities in the snapshot by attaching a list structure to [XrSpatialComponentDataQueryResultEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentDataQueryResultEXT) :: `next` corresponding to each [XrSpatialComponentTypeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentTypeEXT) in [XrSpatialComponentDataQueryConditionEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentDataQueryConditionEXT) :: `componentTypes` .

If the application attaches a list structure to [XrSpatialComponentDataQueryResultEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentDataQueryResultEXT) :: `next` that does not correspond to any of the components listed in [XrSpatialComponentDataQueryConditionEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentDataQueryConditionEXT) :: `componentTypes` , the runtime **must** return `XR_ERROR_VALIDATION_FAILURE` .

The application **can** choose to attach the list structures corresponding to only a subset of components listed in [XrSpatialComponentDataQueryConditionEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentDataQueryConditionEXT) :: `componentTypes` . The application **can** choose to omit the list structures altogether if it only wishes to know the ids and tracking state of the spatial entities that satisfy the `queryCondition` . The runtime **must** not treat the absence of list structures from the [XrSpatialComponentDataQueryResultEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentDataQueryResultEXT) :: `next` chain as a failure.

If [XrEventDataReferenceSpaceChangePending](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrEventDataReferenceSpaceChangePending) is queued and [XrEventDataReferenceSpaceChangePending](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrEventDataReferenceSpaceChangePending) :: `changeTime` elapsed while the application is querying component data from an [XrSpatialSnapshotEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialSnapshotEXT) , the application **may** use the event data to adjust the poses accordingly.

The runtime **must** populate [XrSpatialComponentDataQueryResultEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentDataQueryResultEXT) :: `entityIds` only with entities that have all the components specified in [XrSpatialComponentDataQueryConditionEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentDataQueryConditionEXT) :: `componentTypes` . If [XrSpatialComponentDataQueryConditionEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentDataQueryConditionEXT) :: `componentTypeCount` is 0, the runtime **must** populate `queryResult` with all the entities (and their tracking states) that are in the snapshot. If additional query conditions are added to [XrSpatialComponentDataQueryConditionEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentDataQueryConditionEXT) :: `next` , the runtime **must** treat those as an "AND" with the component types availability i.e. the runtime **must** populate [XrSpatialComponentDataQueryResultEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentDataQueryResultEXT) ::entityIds only with entities that satisfy all of the provided conditions. The runtime **must** populate the component data in the list structures in the same order as the entities in [XrSpatialComponentDataQueryResultEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentDataQueryResultEXT) :: `entityIds` i.e. the component data at a given index in the list structure array **must** correspond to the entity at the same index.

If the tracking state for an entity is not `XR_SPATIAL_ENTITY_TRACKING_STATE_TRACKING_EXT` , the runtime **must** not change the data at the index corresponding to that entity in the array contained in the list structures attached to [XrSpatialComponentDataQueryResultEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentDataQueryResultEXT) .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrQuerySpatialComponentDataEXT-extension-notenabled) The `XR_EXT_spatial_entity` extension **must** be enabled prior to calling [xrQuerySpatialComponentDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrQuerySpatialComponentDataEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrQuerySpatialComponentDataEXT-snapshot-parameter) `snapshot` **must** be a valid [XrSpatialSnapshotEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialSnapshotEXT) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrQuerySpatialComponentDataEXT-queryCondition-parameter) `queryCondition` **must** be a pointer to a valid [XrSpatialComponentDataQueryConditionEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentDataQueryConditionEXT) structure
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrQuerySpatialComponentDataEXT-queryResult-parameter) `queryResult` **must** be a pointer to an [XrSpatialComponentDataQueryResultEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentDataQueryResultEXT) structure

### Return Codes

[Success](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`
- `XR_SESSION_LOSS_PENDING`

[Failure](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_HANDLE_INVALID`
- `XR_ERROR_INSTANCE_LOST`
- `XR_ERROR_OUT_OF_MEMORY`
- `XR_ERROR_RUNTIME_FAILURE`
- `XR_ERROR_SESSION_LOST`
- `XR_ERROR_SIZE_INSUFFICIENT`
- `XR_ERROR_VALIDATION_FAILURE`

As an example the application creates an [XrSpatialSnapshotEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialSnapshotEXT) which contains 5 entities, where -

- Entity 1 and 2 have components `XR_SPATIAL_COMPONENT_TYPE_BOUNDED_2D_EXT` and `XR_SPATIAL_COMPONENT_TYPE_PARENT_EXT`
- Entity 3 and 4 have components `XR_SPATIAL_COMPONENT_TYPE_BOUNDED_3D_EXT` and `XR_SPATIAL_COMPONENT_TYPE_MESH_3D_EXT`
- Entity 5 has components `XR_SPATIAL_COMPONENT_TYPE_BOUNDED_2D_EXT` and `XR_SPATIAL_COMPONENT_TYPE_MESH_3D_EXT` .

XrSpatialEntityIdEXT

XrSpatialEntityIdEXT

1

1

2

2

3

3

4

4

5

5

Bounded2D

Bounded2D

Yes

Yes

Yes

Yes

No

No

No

No

Yes

Yes

Parent

Parent

Yes

Yes

Yes

Yes

No

No

No

No

No

No

Mesh3D

Mesh3D

No

No

No

No

Yes

Yes

Yes

Yes

Yes

Yes

Bounded3D

Bounded3D

No

No

No

No

Yes

Yes

Yes

Yes

No

No [Text is not SVG - cannot display](https://www.diagrams.net/doc/faq/svg-export-text-problems)

### Figure 20. Example snapshot

[xrQuerySpatialComponentDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrQuerySpatialComponentDataEXT) on the above snapshot with `XR_SPATIAL_COMPONENT_TYPE_BOUNDED_2D_EXT` listed in the query condition will result in entity #1, #2, and #5 being returned to the application and the application **can** attach an array of [XrSpatialBounded2DDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBounded2DDataEXT) as part of the [XrSpatialComponentBounded2DListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentBounded2DListEXT) structure to the next chain of [XrSpatialComponentDataQueryResultEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentDataQueryResultEXT) to get the bounded2D data.

XrSpatialEntityIdEXT

XrSpatialEntityIdEXT

1

1

2

2

5

5

Bounded2D

Bounded2D

Data for entityId #1

Data for entit...

Data for entityId #2

Data for entit...

Data for entityId #5

Data for entit...

entityIds

entityIds

next

next

XrSpatialComponent DataQueryResultEXT

XrSpatialComponent Dat...

bounds

bounds

XrSpatialComponent Bounded2DListEXT

XrSpatialComponent Bou... [Text is not SVG - cannot display](https://www.diagrams.net/doc/faq/svg-export-text-problems)

### Figure 21. Example query result

[xrQuerySpatialComponentDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrQuerySpatialComponentDataEXT) on the above snapshot with `XR_SPATIAL_COMPONENT_TYPE_BOUNDED_3D_EXT` and `XR_SPATIAL_COMPONENT_TYPE_MESH_3D_EXT` components listed in the query condition will result in entity #3 and #4 being returned to the application and the application **can** attach arrays of [XrBoxf](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrBoxf) and [XrSpatialMeshDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialMeshDataEXT) as part of the [XrSpatialComponentBounded3DListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentBounded3DListEXT) and [XrSpatialComponentMesh3DListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentMesh3DListEXT) structures respectively to the next chain of [XrSpatialComponentDataQueryResultEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentDataQueryResultEXT) to get the component data.

XrSpatialEntityIdEXT

XrSpatialEntityIdEXT

3

3

4

4

Bounded3D

Bounded3D

Data for entityId #3

Data for entit...

Data for entityId #4

Data for entit...

Mesh3D

Mesh3D

Data for entityId #3

Data for entit...

Data for entityId #4

Data for entit...

entityIds

entityIds

next

next

XrSpatialComponent DataQueryResultEXT

XrSpatialComponent Da...

bounds

bounds

next

next

XrSpatialComponent Bounded3DListEXT

XrSpatialComponent Bo...

XrSpatialComponent Mesh3DListEXT

XrSpatialComponent Me...

meshes

meshes [Text is not SVG - cannot display](https://www.diagrams.net/doc/faq/svg-export-text-problems)

### Figure 22. Example query result

The [XrSpatialComponentDataQueryConditionEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentDataQueryConditionEXT) structure is defined as:

    typedef struct XrSpatialComponentDataQueryConditionEXT {
        XrStructureType                     type;
        const void*                         next;
        uint32_t                            componentTypeCount;
        const XrSpatialComponentTypeEXT*    componentTypes;
    } XrSpatialComponentDataQueryConditionEXT;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `componentTypeCount` is a `uint32_t` describing the count of elements in the `componentTypes` array.
- `componentTypes` is an array of [XrSpatialComponentTypeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentTypeEXT) for which to get the data from the snapshot.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialComponentDataQueryConditionEXT-extension-notenabled) The `XR_EXT_spatial_entity` extension **must** be enabled prior to using [XrSpatialComponentDataQueryConditionEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentDataQueryConditionEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialComponentDataQueryConditionEXT-type-type) `type` **must** be `XR_TYPE_SPATIAL_COMPONENT_DATA_QUERY_CONDITION_EXT`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialComponentDataQueryConditionEXT-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains) . See also: [XrSpatialDiscoveryPersistenceUuidFilterEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialDiscoveryPersistenceUuidFilterEXT) , [XrSpatialFilterArchetypeEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialFilterArchetypeEXT) , [XrSpatialFilterTrackingStateEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialFilterTrackingStateEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialComponentDataQueryConditionEXT-componentTypes-parameter) If `componentTypeCount` is not `0` , `componentTypes` **must** be a pointer to an array of `componentTypeCount` valid [XrSpatialComponentTypeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentTypeEXT) values

The [XrSpatialComponentDataQueryResultEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentDataQueryResultEXT) structure is defined as:

    typedef struct XrSpatialComponentDataQueryResultEXT {
        XrStructureType                     type;
        void*                               next;
        uint32_t                            entityIdCapacityInput;
        uint32_t                            entityIdCountOutput;
        XrSpatialEntityIdEXT*               entityIds;
        uint32_t                            entityStateCapacityInput;
        uint32_t                            entityStateCountOutput;
        XrSpatialEntityTrackingStateEXT*    entityStates;
    } XrSpatialComponentDataQueryResultEXT;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `entityIdCapacityInput` is the capacity of the `entityIds` array, or 0 to indicate a request to retrieve the required capacity.
- `entityIdCountOutput` is the number of `XrSpatialEntityIdEXT` in `entityIds` , or the required capacity in the case that `entityIdCapacityInput` is insufficient.
- `entityIds` is an array of `XrSpatialEntityIdEXT` . It **can** be `NULL` if `entityIdCapacityInput` is 0.
- `entityStateCapacityInput` is the capacity of the `entityStates` array, or 0 to indicate a request to retrieve the required capacity.
- `entityStateCountOutput` is the number of [XrSpatialEntityTrackingStateEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialEntityTrackingStateEXT) in `entityStates` , or the required capacity in the case that `entityStateCapacityInput` is insufficient. This **must** always be the same as `entityIdCountOutput` .
- `entityStates` is an array of [XrSpatialEntityTrackingStateEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialEntityTrackingStateEXT) . It **can** be `NULL` if `entityStateCapacityInput` is 0.
- See the [Buffer Size Parameters](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-buffer-size-parameters) section for a detailed description of retrieving the required `entityIds` size.

An application **can** use the `entityIds` with [xrCreateSpatialEntityFromIdEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialEntityFromIdEXT) to create [XrSpatialEntityEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialEntityEXT) handles for the entities it is interested in getting regular updates for. The application **can** then use these [XrSpatialEntityEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialEntityEXT) handles with [xrCreateSpatialUpdateSnapshotEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialUpdateSnapshotEXT) to create an update snapshot that has the runtime's latest known data of the components for the provided entities.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialComponentDataQueryResultEXT-extension-notenabled) The `XR_EXT_spatial_entity` extension **must** be enabled prior to using [XrSpatialComponentDataQueryResultEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentDataQueryResultEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialComponentDataQueryResultEXT-type-type) `type` **must** be `XR_TYPE_SPATIAL_COMPONENT_DATA_QUERY_RESULT_EXT`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialComponentDataQueryResultEXT-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains) . See also: [XrSpatialComponentAnchorListEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentAnchorListEXT) , [XrSpatialComponentAnnotationQuadListANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentAnnotationQuadListANDROID) , [XrSpatialComponentBounded2DListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentBounded2DListEXT) , [XrSpatialComponentBounded3DListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentBounded3DListEXT) , [XrSpatialComponentConfidenceListANDROIDSYS](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentConfidenceListANDROIDSYS) , [XrSpatialComponentImage2DListEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentImage2DListEXT) , [XrSpatialComponentKeyboardSemanticLabelListEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentKeyboardSemanticLabelListEXT) , [XrSpatialComponentMarkerListEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentMarkerListEXT) , [XrSpatialComponentMaterialTypeListANDROIDSYS](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentMaterialTypeListANDROIDSYS) , [XrSpatialComponentMesh2DListEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentMesh2DListEXT) , [XrSpatialComponentMesh3DListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentMesh3DListEXT) , [XrSpatialComponentMesh3DNormalsListEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentMesh3DNormalsListEXT) , [XrSpatialComponentMesh3DTriangleSemanticLabelsListEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentMesh3DTriangleSemanticLabelsListEXT) , [XrSpatialComponentMesh3DVertexSemanticLabelsListEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentMesh3DVertexSemanticLabelsListEXT) , [XrSpatialComponentMouseSemanticLabelListEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentMouseSemanticLabelListEXT) , [XrSpatialComponentObjectSemanticLabelListANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentObjectSemanticLabelListANDROID) , [XrSpatialComponentObjectSemanticLabelListEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentObjectSemanticLabelListEXT) , [XrSpatialComponentOccupancyGridListANDROIDX1](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentOccupancyGridListANDROIDX1) , [XrSpatialComponentParentListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentParentListEXT) , [XrSpatialComponentPersistenceListEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentPersistenceListEXT) , [XrSpatialComponentPlaneAlignmentListEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentPlaneAlignmentListEXT) , [XrSpatialComponentPlaneSemanticLabelListEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentPlaneSemanticLabelListEXT) , [XrSpatialComponentPolygon2DListEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentPolygon2DListEXT) , [XrSpatialComponentRaycastResultListANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentRaycastResultListANDROID) , [XrSpatialComponentRoomEmptinessListANDROIDSYS](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentRoomEmptinessListANDROIDSYS) , [XrSpatialComponentRoomListANDROIDSYS](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentRoomListANDROIDSYS) , [XrSpatialComponentStreetscapeGeometryMetadataListANDROIDX2](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentStreetscapeGeometryMetadataListANDROIDX2) , [XrSpatialComponentSubsumedByListANDROID](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentSubsumedByListANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialComponentDataQueryResultEXT-entityIds-parameter) If `entityIdCapacityInput` is not `0` , `entityIds` **must** be a pointer to an array of `entityIdCapacityInput` `XrSpatialEntityIdEXT` values
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialComponentDataQueryResultEXT-entityStates-parameter) If `entityStateCapacityInput` is not `0` , `entityStates` **must** be a pointer to an array of `entityStateCapacityInput` [XrSpatialEntityTrackingStateEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialEntityTrackingStateEXT) values

    typedef enum XrSpatialEntityTrackingStateEXT {
        XR_SPATIAL_ENTITY_TRACKING_STATE_STOPPED_EXT = 1,
        XR_SPATIAL_ENTITY_TRACKING_STATE_PAUSED_EXT = 2,
        XR_SPATIAL_ENTITY_TRACKING_STATE_TRACKING_EXT = 3,
        XR_SPATIAL_ENTITY_TRACKING_STATE_MAX_ENUM_EXT = 0x7FFFFFFF
    } XrSpatialEntityTrackingStateEXT;

The [XrSpatialEntityTrackingStateEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialEntityTrackingStateEXT) enumerates the possible spatial entity tracking states:

The enums have the following meanings:

Enum Description

`XR_SPATIAL_ENTITY_TRACKING_STATE_STOPPED_EXT`

The runtime has stopped tracking this entity and will never resume tracking it.

`XR_SPATIAL_ENTITY_TRACKING_STATE_PAUSED_EXT`

The runtime has paused tracking this entity but **may** resume tracking it in the future.

`XR_SPATIAL_ENTITY_TRACKING_STATE_TRACKING_EXT`

The runtime is currently tracking this entity and its component data is valid.

TRACKING

PAUSED

STOPPED

### Figure 23. [XrSpatialEntityTrackingStateEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialEntityTrackingStateEXT)

- The runtime **may** change the state of the spatial entity from `XR_SPATIAL_ENTITY_TRACKING_STATE_TRACKING_EXT` to `XR_SPATIAL_ENTITY_TRACKING_STATE_PAUSED_EXT` if it suspends the tracking of that spatial entity but has the possibility of resuming its tracking in the future. Some examples of when the runtime **may** do this include (but not limited to) if the application loses input focus; or if the given spatial entity is too far from the user to be accurately tracked; or if there are too many entities being tracked and the runtime wants to reduce the cost of tracking. [XrSpatialEntityTrackingStateEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialEntityTrackingStateEXT) helps the application insulate itself from the different tracking policies of each runtime.
- The runtime **may** change the state of an entity from `XR_SPATIAL_ENTITY_TRACKING_STATE_PAUSED_EXT` to `XR_SPATIAL_ENTITY_TRACKING_STATE_TRACKING_EXT` or `XR_SPATIAL_ENTITY_TRACKING_STATE_STOPPED_EXT` .
- The runtime **must** change the state of the spatial entity from `XR_SPATIAL_ENTITY_TRACKING_STATE_TRACKING_EXT` or `XR_SPATIAL_ENTITY_TRACKING_STATE_PAUSED_EXT` to `XR_SPATIAL_ENTITY_TRACKING_STATE_STOPPED_EXT` if the spatial entity is lost and its tracking will never be recovered or resumed. An example of such a case would be if the device loses tracking, restarts its tracking session but is unable to relocalize in its environment, and therefore treats discovered entities of this tracking session as new entities.
- Once the tracking state of an entity is set to `XR_SPATIAL_ENTITY_TRACKING_STATE_STOPPED_EXT` , the runtime **must** never change it any other state.
- When querying the component data of a spatial entity using [xrQuerySpatialComponentDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrQuerySpatialComponentDataEXT) , the runtime **must** set valid data in the contents of the buffers provided by the application in the next chain of [XrSpatialComponentDataQueryResultEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentDataQueryResultEXT) if the entity state is `XR_SPATIAL_ENTITY_TRACKING_STATE_TRACKING_EXT` . If the entity state is `XR_SPATIAL_ENTITY_TRACKING_STATE_STOPPED_EXT` or `XR_SPATIAL_ENTITY_TRACKING_STATE_PAUSED_EXT` , the runtime **must** not change the content of the buffers.

### Two-call idiom for component data

The [XrSpatialBufferEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferEXT) structure is defined as:

    typedef struct XrSpatialBufferEXT {
        XrSpatialBufferIdEXT      bufferId;
        XrSpatialBufferTypeEXT    bufferType;
    } XrSpatialBufferEXT;

### Member Descriptions

- `bufferId` the `XrSpatialBufferIdEXT` of the buffer data.
- `bufferType` is the [XrSpatialBufferTypeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferTypeEXT) to indicate the type of data in `bufferId` . The application **can** use `bufferType` to determine which function to use to retrieve the actual data of the buffer.

Some spatial components have variable-sized data and therefore require using [the two-call idiom](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-buffer-size-parameters) to retrieve their data. In such cases, the spatial component data structure provides an [XrSpatialBufferEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferEXT) for each variable sized buffer needed in that component's data.

For the same `bufferId` , the runtime **must** provide the same data from one component data query to another, even across one snapshot to another. A different `bufferId` between component data query calls indicates to the application that the data for that component **may** have changed.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialBufferEXT-extension-notenabled) The `XR_EXT_spatial_entity` extension **must** be enabled prior to using [XrSpatialBufferEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialBufferEXT-bufferType-parameter) `bufferType` **must** be a valid [XrSpatialBufferTypeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferTypeEXT) value

    XR_DEFINE_ATOM(XrSpatialBufferIdEXT)

`XrSpatialBufferIdEXT` is used to represent any kind of variable sized data for a spatial component.

The runtime **must** keep the `XrSpatialBufferIdEXT` and its data in memory for at least the lifecycle of the [XrSpatialSnapshotEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialSnapshotEXT) that contains it. The runtime **may** keep the `XrSpatialBufferIdEXT` and its data in memory for longer than the lifecycle of the [XrSpatialSnapshotEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialSnapshotEXT) in order to return the same ID as part of snapshots created later on by the application. For the same `XrSpatialBufferIdEXT` , the runtime **must** always return the same data via the appropriate `xrGetSpatialBuffer*` function.

    typedef enum XrSpatialBufferTypeEXT {
        XR_SPATIAL_BUFFER_TYPE_UNKNOWN_EXT = 0,
        XR_SPATIAL_BUFFER_TYPE_STRING_EXT = 1,
        XR_SPATIAL_BUFFER_TYPE_UINT8_EXT = 2,
        XR_SPATIAL_BUFFER_TYPE_UINT16_EXT = 3,
        XR_SPATIAL_BUFFER_TYPE_UINT32_EXT = 4,
        XR_SPATIAL_BUFFER_TYPE_FLOAT_EXT = 5,
        XR_SPATIAL_BUFFER_TYPE_VECTOR2F_EXT = 6,
        XR_SPATIAL_BUFFER_TYPE_VECTOR3F_EXT = 7,
        XR_SPATIAL_BUFFER_TYPE_MAX_ENUM_EXT = 0x7FFFFFFF
    } XrSpatialBufferTypeEXT;

The [XrSpatialBufferTypeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferTypeEXT) enumeration identifies the different data types of the buffer represented `XrSpatialBufferIdEXT` .

### Enumerant Descriptions

- `XR_SPATIAL_BUFFER_TYPE_STRING_EXT` . The `XrSpatialBufferIdEXT` **can** be passed to [xrGetSpatialBufferStringEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrGetSpatialBufferStringEXT) to retrieve a string buffer.
- `XR_SPATIAL_BUFFER_TYPE_UINT8_EXT` . The `XrSpatialBufferIdEXT` **can** be passed to [xrGetSpatialBufferUint8EXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrGetSpatialBufferUint8EXT) to retrieve a `uint8_t` buffer.
- `XR_SPATIAL_BUFFER_TYPE_UINT16_EXT` . The `XrSpatialBufferIdEXT` **can** be passed to [xrGetSpatialBufferUint16EXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrGetSpatialBufferUint16EXT) to retrieve a `uint16_t` buffer.
- `XR_SPATIAL_BUFFER_TYPE_UINT32_EXT` . The `XrSpatialBufferIdEXT` **can** be passed to [xrGetSpatialBufferUint32EXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrGetSpatialBufferUint32EXT) to retrieve a `uint32_t` buffer.
- `XR_SPATIAL_BUFFER_TYPE_FLOAT_EXT` . The `XrSpatialBufferIdEXT` **can** be passed to [xrGetSpatialBufferFloatEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrGetSpatialBufferFloatEXT) to retrieve a `float` buffer.
- `XR_SPATIAL_BUFFER_TYPE_VECTOR2F_EXT` . The `XrSpatialBufferIdEXT` **can** be passed to [xrGetSpatialBufferVector2fEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrGetSpatialBufferVector2fEXT) to retrieve an [XrVector2f](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrVector2f) buffer.
- `XR_SPATIAL_BUFFER_TYPE_VECTOR3F_EXT` . The `XrSpatialBufferIdEXT` **can** be passed to [xrGetSpatialBufferVector3fEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrGetSpatialBufferVector3fEXT) to retrieve an [XrVector3f](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrVector3f) buffer.

The [xrGetSpatialBufferStringEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrGetSpatialBufferStringEXT) function is defined as:

    XrResult xrGetSpatialBufferStringEXT(
        XrSpatialSnapshotEXT                        snapshot,
        const XrSpatialBufferGetInfoEXT*            info,
        uint32_t                                    bufferCapacityInput,
        uint32_t*                                   bufferCountOutput,
        char*                                       buffer);

### Parameter Descriptions

- `snapshot` is a handle to an [XrSpatialSnapshotEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialSnapshotEXT) .
- `info` holds the information on the buffer to query.
- `bufferCapacityInput` is the capacity of the array, or 0 to indicate a request to retrieve the required capacity.
- `bufferCountOutput` is the number of characters, or the required capacity in the case that `bufferCapacityInput` is insufficient.
- `buffer` is an array of `char` . It **can** be `NULL` if `bufferCapacityInput` is 0.
- See the [Buffer Size Parameters](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-buffer-size-parameters) section for a detailed description of retrieving the required `buffer` size.

The application **can** get the data for an [XrSpatialBufferEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferEXT) provided by a component, where [XrSpatialBufferEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferEXT) :: `bufferType` is `XR_SPATIAL_BUFFER_TYPE_STRING_EXT` by using [xrGetSpatialBufferStringEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrGetSpatialBufferStringEXT) .

The runtime **must** return `XR_ERROR_VALIDATION_FAILURE` if the [XrSpatialBufferTypeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferTypeEXT) for [XrSpatialBufferGetInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferGetInfoEXT) :: `bufferId` is not `XR_SPATIAL_BUFFER_TYPE_STRING_EXT` .

The runtime **must** return `XR_ERROR_SPATIAL_BUFFER_ID_INVALID_EXT` if [XrSpatialBufferGetInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferGetInfoEXT) :: `bufferId` does not belong to `snapshot` .

`buffer` filled by the runtime **must** be a null-terminated UTF-8 string.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrGetSpatialBufferStringEXT-extension-notenabled) The `XR_EXT_spatial_entity` extension **must** be enabled prior to calling [xrGetSpatialBufferStringEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrGetSpatialBufferStringEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrGetSpatialBufferStringEXT-snapshot-parameter) `snapshot` **must** be a valid [XrSpatialSnapshotEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialSnapshotEXT) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrGetSpatialBufferStringEXT-info-parameter) `info` **must** be a pointer to a valid [XrSpatialBufferGetInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferGetInfoEXT) structure
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrGetSpatialBufferStringEXT-bufferCountOutput-parameter) `bufferCountOutput` **must** be a pointer to a `uint32_t` value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrGetSpatialBufferStringEXT-buffer-parameter) If `bufferCapacityInput` is not `0` , `buffer` **must** be a pointer to an array of `bufferCapacityInput` char values

### Return Codes

[Success](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`
- `XR_SESSION_LOSS_PENDING`

[Failure](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_HANDLE_INVALID`
- `XR_ERROR_INSTANCE_LOST`
- `XR_ERROR_OUT_OF_MEMORY`
- `XR_ERROR_RUNTIME_FAILURE`
- `XR_ERROR_SESSION_LOST`
- `XR_ERROR_SIZE_INSUFFICIENT`
- `XR_ERROR_SPATIAL_BUFFER_ID_INVALID_EXT`
- `XR_ERROR_VALIDATION_FAILURE`

The [xrGetSpatialBufferUint8EXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrGetSpatialBufferUint8EXT) function is defined as:

    XrResult xrGetSpatialBufferUint8EXT(
        XrSpatialSnapshotEXT                        snapshot,
        const XrSpatialBufferGetInfoEXT*            info,
        uint32_t                                    bufferCapacityInput,
        uint32_t*                                   bufferCountOutput,
        uint8_t*                                    buffer);

### Parameter Descriptions

- `snapshot` is a handle to an [XrSpatialSnapshotEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialSnapshotEXT) .
- `info` holds the information on the buffer to query.
- `bufferCapacityInput` is the capacity of the array, or 0 to indicate a request to retrieve the required capacity.
- `bufferCountOutput` is the number of elements in the `buffer` array, or the required capacity in the case that `bufferCapacityInput` is insufficient.
- `buffer` is an array of `uint8_t` . It **can** be `NULL` if `bufferCapacityInput` is 0.
- See the [Buffer Size Parameters](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-buffer-size-parameters) section for a detailed description of retrieving the required `buffer` size.

The application **can** get the data for an [XrSpatialBufferEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferEXT) provided by a component, where [XrSpatialBufferEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferEXT) :: `bufferType` is `XR_SPATIAL_BUFFER_TYPE_UINT8_EXT` by using [xrGetSpatialBufferUint8EXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrGetSpatialBufferUint8EXT) .

The runtime **must** return `XR_ERROR_VALIDATION_FAILURE` if the [XrSpatialBufferTypeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferTypeEXT) for [XrSpatialBufferGetInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferGetInfoEXT) :: `bufferId` is not `XR_SPATIAL_BUFFER_TYPE_UINT8_EXT` .

The runtime **must** return `XR_ERROR_SPATIAL_BUFFER_ID_INVALID_EXT` if [XrSpatialBufferGetInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferGetInfoEXT) :: `bufferId` does not belong to `snapshot` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrGetSpatialBufferUint8EXT-extension-notenabled) The `XR_EXT_spatial_entity` extension **must** be enabled prior to calling [xrGetSpatialBufferUint8EXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrGetSpatialBufferUint8EXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrGetSpatialBufferUint8EXT-snapshot-parameter) `snapshot` **must** be a valid [XrSpatialSnapshotEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialSnapshotEXT) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrGetSpatialBufferUint8EXT-info-parameter) `info` **must** be a pointer to a valid [XrSpatialBufferGetInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferGetInfoEXT) structure
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrGetSpatialBufferUint8EXT-bufferCountOutput-parameter) `bufferCountOutput` **must** be a pointer to a `uint32_t` value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrGetSpatialBufferUint8EXT-buffer-parameter) If `bufferCapacityInput` is not `0` , `buffer` **must** be a pointer to an array of `bufferCapacityInput` `uint8_t` values

### Return Codes

[Success](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`
- `XR_SESSION_LOSS_PENDING`

[Failure](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_HANDLE_INVALID`
- `XR_ERROR_INSTANCE_LOST`
- `XR_ERROR_OUT_OF_MEMORY`
- `XR_ERROR_RUNTIME_FAILURE`
- `XR_ERROR_SESSION_LOST`
- `XR_ERROR_SIZE_INSUFFICIENT`
- `XR_ERROR_SPATIAL_BUFFER_ID_INVALID_EXT`
- `XR_ERROR_VALIDATION_FAILURE`

The [xrGetSpatialBufferUint16EXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrGetSpatialBufferUint16EXT) function is defined as:

    XrResult xrGetSpatialBufferUint16EXT(
        XrSpatialSnapshotEXT                        snapshot,
        const XrSpatialBufferGetInfoEXT*            info,
        uint32_t                                    bufferCapacityInput,
        uint32_t*                                   bufferCountOutput,
        uint16_t*                                   buffer);

### Parameter Descriptions

- `snapshot` is a handle to an [XrSpatialSnapshotEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialSnapshotEXT) .
- `info` holds the information on the buffer to query.
- `bufferCapacityInput` is the capacity of the array, or 0 to indicate a request to retrieve the required capacity.
- `bufferCountOutput` is the number of elements in the `buffer` array, or the required capacity in the case that `bufferCapacityInput` is insufficient.
- `buffer` is an array of `uint16_t` . It **can** be `NULL` if `bufferCapacityInput` is 0.
- See the [Buffer Size Parameters](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-buffer-size-parameters) section for a detailed description of retrieving the required `buffer` size.

The application **can** get the data for an [XrSpatialBufferEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferEXT) provided by a component, where [XrSpatialBufferEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferEXT) :: `bufferType` is `XR_SPATIAL_BUFFER_TYPE_UINT16_EXT` by using [xrGetSpatialBufferUint16EXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrGetSpatialBufferUint16EXT) .

The runtime **must** return `XR_ERROR_VALIDATION_FAILURE` if the [XrSpatialBufferTypeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferTypeEXT) for [XrSpatialBufferGetInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferGetInfoEXT) :: `bufferId` is not `XR_SPATIAL_BUFFER_TYPE_UINT16_EXT` .

The runtime **must** return `XR_ERROR_SPATIAL_BUFFER_ID_INVALID_EXT` if [XrSpatialBufferGetInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferGetInfoEXT) :: `bufferId` does not belong to `snapshot` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrGetSpatialBufferUint16EXT-extension-notenabled) The `XR_EXT_spatial_entity` extension **must** be enabled prior to calling [xrGetSpatialBufferUint16EXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrGetSpatialBufferUint16EXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrGetSpatialBufferUint16EXT-snapshot-parameter) `snapshot` **must** be a valid [XrSpatialSnapshotEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialSnapshotEXT) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrGetSpatialBufferUint16EXT-info-parameter) `info` **must** be a pointer to a valid [XrSpatialBufferGetInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferGetInfoEXT) structure
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrGetSpatialBufferUint16EXT-bufferCountOutput-parameter) `bufferCountOutput` **must** be a pointer to a `uint32_t` value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrGetSpatialBufferUint16EXT-buffer-parameter) If `bufferCapacityInput` is not `0` , `buffer` **must** be a pointer to an array of `bufferCapacityInput` `uint16_t` values

### Return Codes

[Success](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`
- `XR_SESSION_LOSS_PENDING`

[Failure](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_HANDLE_INVALID`
- `XR_ERROR_INSTANCE_LOST`
- `XR_ERROR_OUT_OF_MEMORY`
- `XR_ERROR_RUNTIME_FAILURE`
- `XR_ERROR_SESSION_LOST`
- `XR_ERROR_SIZE_INSUFFICIENT`
- `XR_ERROR_SPATIAL_BUFFER_ID_INVALID_EXT`
- `XR_ERROR_VALIDATION_FAILURE`

The [xrGetSpatialBufferUint32EXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrGetSpatialBufferUint32EXT) function is defined as:

    XrResult xrGetSpatialBufferUint32EXT(
        XrSpatialSnapshotEXT                        snapshot,
        const XrSpatialBufferGetInfoEXT*            info,
        uint32_t                                    bufferCapacityInput,
        uint32_t*                                   bufferCountOutput,
        uint32_t*                                   buffer);

### Parameter Descriptions

- `snapshot` is a handle to an [XrSpatialSnapshotEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialSnapshotEXT) .
- `info` holds the information on the buffer to query.
- `bufferCapacityInput` is the capacity of the array, or 0 to indicate a request to retrieve the required capacity.
- `bufferCountOutput` is the number of elements in the `buffer` array, or the required capacity in the case that `bufferCapacityInput` is insufficient.
- `buffer` is an array of `uint32_t` . It **can** be `NULL` if `bufferCapacityInput` is 0.
- See the [Buffer Size Parameters](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-buffer-size-parameters) section for a detailed description of retrieving the required `buffer` size.

The application **can** get the data for an [XrSpatialBufferEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferEXT) provided by a component, where [XrSpatialBufferEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferEXT) :: `bufferType` is `XR_SPATIAL_BUFFER_TYPE_UINT32_EXT` by using [xrGetSpatialBufferUint32EXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrGetSpatialBufferUint32EXT) .

The runtime **must** return `XR_ERROR_VALIDATION_FAILURE` if the [XrSpatialBufferTypeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferTypeEXT) for [XrSpatialBufferGetInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferGetInfoEXT) :: `bufferId` is not `XR_SPATIAL_BUFFER_TYPE_UINT32_EXT` .

The runtime **must** return `XR_ERROR_SPATIAL_BUFFER_ID_INVALID_EXT` if [XrSpatialBufferGetInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferGetInfoEXT) :: `bufferId` does not belong to `snapshot` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrGetSpatialBufferUint32EXT-extension-notenabled) The `XR_EXT_spatial_entity` extension **must** be enabled prior to calling [xrGetSpatialBufferUint32EXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrGetSpatialBufferUint32EXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrGetSpatialBufferUint32EXT-snapshot-parameter) `snapshot` **must** be a valid [XrSpatialSnapshotEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialSnapshotEXT) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrGetSpatialBufferUint32EXT-info-parameter) `info` **must** be a pointer to a valid [XrSpatialBufferGetInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferGetInfoEXT) structure
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrGetSpatialBufferUint32EXT-bufferCountOutput-parameter) `bufferCountOutput` **must** be a pointer to a `uint32_t` value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrGetSpatialBufferUint32EXT-buffer-parameter) If `bufferCapacityInput` is not `0` , `buffer` **must** be a pointer to an array of `bufferCapacityInput` `uint32_t` values

### Return Codes

[Success](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`
- `XR_SESSION_LOSS_PENDING`

[Failure](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_HANDLE_INVALID`
- `XR_ERROR_INSTANCE_LOST`
- `XR_ERROR_OUT_OF_MEMORY`
- `XR_ERROR_RUNTIME_FAILURE`
- `XR_ERROR_SESSION_LOST`
- `XR_ERROR_SIZE_INSUFFICIENT`
- `XR_ERROR_SPATIAL_BUFFER_ID_INVALID_EXT`
- `XR_ERROR_VALIDATION_FAILURE`

The [xrGetSpatialBufferFloatEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrGetSpatialBufferFloatEXT) function is defined as:

    XrResult xrGetSpatialBufferFloatEXT(
        XrSpatialSnapshotEXT                        snapshot,
        const XrSpatialBufferGetInfoEXT*            info,
        uint32_t                                    bufferCapacityInput,
        uint32_t*                                   bufferCountOutput,
        float*                                      buffer);

### Parameter Descriptions

- `snapshot` is a handle to an [XrSpatialSnapshotEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialSnapshotEXT) .
- `info` holds the information on the buffer to query.
- `bufferCapacityInput` is the capacity of the array, or 0 to indicate a request to retrieve the required capacity.
- `bufferCountOutput` is the number of elements in the `buffer` array, or the required capacity in the case that `bufferCapacityInput` is insufficient.
- `buffer` is an array of `float` . It **can** be `NULL` if `bufferCapacityInput` is 0.
- See the [Buffer Size Parameters](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-buffer-size-parameters) section for a detailed description of retrieving the required `buffer` size.

The application **can** get the data for an [XrSpatialBufferEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferEXT) provided by a component, where [XrSpatialBufferEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferEXT) :: `bufferType` is `XR_SPATIAL_BUFFER_TYPE_FLOAT_EXT` by using [xrGetSpatialBufferFloatEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrGetSpatialBufferFloatEXT) .

The runtime **must** return `XR_ERROR_VALIDATION_FAILURE` if the [XrSpatialBufferTypeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferTypeEXT) for [XrSpatialBufferGetInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferGetInfoEXT) :: `bufferId` is not `XR_SPATIAL_BUFFER_TYPE_FLOAT_EXT` .

The runtime **must** return `XR_ERROR_SPATIAL_BUFFER_ID_INVALID_EXT` if [XrSpatialBufferGetInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferGetInfoEXT) :: `bufferId` does not belong to `snapshot` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrGetSpatialBufferFloatEXT-extension-notenabled) The `XR_EXT_spatial_entity` extension **must** be enabled prior to calling [xrGetSpatialBufferFloatEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrGetSpatialBufferFloatEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrGetSpatialBufferFloatEXT-snapshot-parameter) `snapshot` **must** be a valid [XrSpatialSnapshotEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialSnapshotEXT) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrGetSpatialBufferFloatEXT-info-parameter) `info` **must** be a pointer to a valid [XrSpatialBufferGetInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferGetInfoEXT) structure
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrGetSpatialBufferFloatEXT-bufferCountOutput-parameter) `bufferCountOutput` **must** be a pointer to a `uint32_t` value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrGetSpatialBufferFloatEXT-buffer-parameter) If `bufferCapacityInput` is not `0` , `buffer` **must** be a pointer to an array of `bufferCapacityInput` `float` values

### Return Codes

[Success](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`
- `XR_SESSION_LOSS_PENDING`

[Failure](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_HANDLE_INVALID`
- `XR_ERROR_INSTANCE_LOST`
- `XR_ERROR_OUT_OF_MEMORY`
- `XR_ERROR_RUNTIME_FAILURE`
- `XR_ERROR_SESSION_LOST`
- `XR_ERROR_SIZE_INSUFFICIENT`
- `XR_ERROR_SPATIAL_BUFFER_ID_INVALID_EXT`
- `XR_ERROR_VALIDATION_FAILURE`

The [xrGetSpatialBufferVector2fEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrGetSpatialBufferVector2fEXT) function is defined as:

    XrResult xrGetSpatialBufferVector2fEXT(
        XrSpatialSnapshotEXT                        snapshot,
        const XrSpatialBufferGetInfoEXT*            info,
        uint32_t                                    bufferCapacityInput,
        uint32_t*                                   bufferCountOutput,
        XrVector2f*                                 buffer);

### Parameter Descriptions

- `snapshot` is a handle to an [XrSpatialSnapshotEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialSnapshotEXT) .
- `info` holds the information on the buffer to query.
- `bufferCapacityInput` is the capacity of the array, or 0 to indicate a request to retrieve the required capacity.
- `bufferCountOutput` is the number of elements in the `buffer` array, or the required capacity in the case that `bufferCapacityInput` is insufficient.
- `buffer` is an array of [XrVector2f](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrVector2f) . It **can** be `NULL` if `bufferCapacityInput` is 0.
- See the [Buffer Size Parameters](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-buffer-size-parameters) section for a detailed description of retrieving the required `buffer` size.

The application **can** get the data for an [XrSpatialBufferEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferEXT) provided by a component, where [XrSpatialBufferEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferEXT) :: `bufferType` is `XR_SPATIAL_BUFFER_TYPE_VECTOR2F_EXT` by using [xrGetSpatialBufferVector2fEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrGetSpatialBufferVector2fEXT) .

The runtime **must** return `XR_ERROR_VALIDATION_FAILURE` if the [XrSpatialBufferTypeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferTypeEXT) for [XrSpatialBufferGetInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferGetInfoEXT) :: `bufferId` is not `XR_SPATIAL_BUFFER_TYPE_VECTOR2F_EXT` .

The runtime **must** return `XR_ERROR_SPATIAL_BUFFER_ID_INVALID_EXT` if [XrSpatialBufferGetInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferGetInfoEXT) :: `bufferId` does not belong to `snapshot` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrGetSpatialBufferVector2fEXT-extension-notenabled) The `XR_EXT_spatial_entity` extension **must** be enabled prior to calling [xrGetSpatialBufferVector2fEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrGetSpatialBufferVector2fEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrGetSpatialBufferVector2fEXT-snapshot-parameter) `snapshot` **must** be a valid [XrSpatialSnapshotEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialSnapshotEXT) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrGetSpatialBufferVector2fEXT-info-parameter) `info` **must** be a pointer to a valid [XrSpatialBufferGetInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferGetInfoEXT) structure
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrGetSpatialBufferVector2fEXT-bufferCountOutput-parameter) `bufferCountOutput` **must** be a pointer to a `uint32_t` value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrGetSpatialBufferVector2fEXT-buffer-parameter) If `bufferCapacityInput` is not `0` , `buffer` **must** be a pointer to an array of `bufferCapacityInput` [XrVector2f](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrVector2f) structures

### Return Codes

[Success](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`
- `XR_SESSION_LOSS_PENDING`

[Failure](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_HANDLE_INVALID`
- `XR_ERROR_INSTANCE_LOST`
- `XR_ERROR_OUT_OF_MEMORY`
- `XR_ERROR_RUNTIME_FAILURE`
- `XR_ERROR_SESSION_LOST`
- `XR_ERROR_SIZE_INSUFFICIENT`
- `XR_ERROR_SPATIAL_BUFFER_ID_INVALID_EXT`
- `XR_ERROR_VALIDATION_FAILURE`

The [xrGetSpatialBufferVector3fEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrGetSpatialBufferVector3fEXT) function is defined as:

    XrResult xrGetSpatialBufferVector3fEXT(
        XrSpatialSnapshotEXT                        snapshot,
        const XrSpatialBufferGetInfoEXT*            info,
        uint32_t                                    bufferCapacityInput,
        uint32_t*                                   bufferCountOutput,
        XrVector3f*                                 buffer);

### Parameter Descriptions

- `snapshot` is a handle to an [XrSpatialSnapshotEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialSnapshotEXT) .
- `info` holds the information on the buffer to query.
- `bufferCapacityInput` is the capacity of the array, or 0 to indicate a request to retrieve the required capacity.
- `bufferCountOutput` is the number of elements in the `buffer` array, or the required capacity in the case that `bufferCapacityInput` is insufficient.
- `buffer` is an array of [XrVector3f](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrVector3f) . It **can** be `NULL` if `bufferCapacityInput` is 0.
- See the [Buffer Size Parameters](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-buffer-size-parameters) section for a detailed description of retrieving the required `buffer` size.

The application **can** get the data for an [XrSpatialBufferEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferEXT) provided by a component, where [XrSpatialBufferEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferEXT) :: `bufferType` is `XR_SPATIAL_BUFFER_TYPE_VECTOR3F_EXT` by using [xrGetSpatialBufferVector3fEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrGetSpatialBufferVector3fEXT) .

The runtime **must** return `XR_ERROR_VALIDATION_FAILURE` if the [XrSpatialBufferTypeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferTypeEXT) for [XrSpatialBufferGetInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferGetInfoEXT) :: `bufferId` is not `XR_SPATIAL_BUFFER_TYPE_VECTOR3F_EXT` .

The runtime **must** return `XR_ERROR_SPATIAL_BUFFER_ID_INVALID_EXT` if [XrSpatialBufferGetInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferGetInfoEXT) :: `bufferId` does not belong to `snapshot` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrGetSpatialBufferVector3fEXT-extension-notenabled) The `XR_EXT_spatial_entity` extension **must** be enabled prior to calling [xrGetSpatialBufferVector3fEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrGetSpatialBufferVector3fEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrGetSpatialBufferVector3fEXT-snapshot-parameter) `snapshot` **must** be a valid [XrSpatialSnapshotEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialSnapshotEXT) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrGetSpatialBufferVector3fEXT-info-parameter) `info` **must** be a pointer to a valid [XrSpatialBufferGetInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferGetInfoEXT) structure
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrGetSpatialBufferVector3fEXT-bufferCountOutput-parameter) `bufferCountOutput` **must** be a pointer to a `uint32_t` value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrGetSpatialBufferVector3fEXT-buffer-parameter) If `bufferCapacityInput` is not `0` , `buffer` **must** be a pointer to an array of `bufferCapacityInput` [XrVector3f](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrVector3f) structures

### Return Codes

[Success](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`
- `XR_SESSION_LOSS_PENDING`

[Failure](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_HANDLE_INVALID`
- `XR_ERROR_INSTANCE_LOST`
- `XR_ERROR_OUT_OF_MEMORY`
- `XR_ERROR_RUNTIME_FAILURE`
- `XR_ERROR_SESSION_LOST`
- `XR_ERROR_SIZE_INSUFFICIENT`
- `XR_ERROR_SPATIAL_BUFFER_ID_INVALID_EXT`
- `XR_ERROR_VALIDATION_FAILURE`

The [XrSpatialBufferGetInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferGetInfoEXT) structure is defined as:

    typedef struct XrSpatialBufferGetInfoEXT {
        XrStructureType         type;
        const void*             next;
        XrSpatialBufferIdEXT    bufferId;
    } XrSpatialBufferGetInfoEXT;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `bufferId` an `XrSpatialBufferIdEXT` for the buffer whose data to retrieve.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialBufferGetInfoEXT-extension-notenabled) The `XR_EXT_spatial_entity` extension **must** be enabled prior to using [XrSpatialBufferGetInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferGetInfoEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialBufferGetInfoEXT-type-type) `type` **must** be `XR_TYPE_SPATIAL_BUFFER_GET_INFO_EXT`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialBufferGetInfoEXT-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)

    #define XR_NULL_SPATIAL_BUFFER_ID_EXT 0

[XR_NULL_SPATIAL_BUFFER_ID_EXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XR_NULL_SPATIAL_BUFFER_ID_EXT) is a reserved value representing an invalid `XrSpatialBufferIdEXT` . It **may** be passed to and returned from API functions only when specifically allowed.

### Create Update Snapshot

The [xrCreateSpatialUpdateSnapshotEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialUpdateSnapshotEXT) function is defined as:

    XrResult xrCreateSpatialUpdateSnapshotEXT(
        XrSpatialContextEXT                         spatialContext,
        const XrSpatialUpdateSnapshotCreateInfoEXT* createInfo,
        XrSpatialSnapshotEXT*                       snapshot);

### Parameter Descriptions

- `spatialContext` is an [XrSpatialContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialContextEXT) previously created using [xrCreateSpatialContextAsyncEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialContextAsyncEXT) .
- `createInfo` is a pointer to an [XrSpatialUpdateSnapshotCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialUpdateSnapshotCreateInfoEXT) .
- `snapshot` is a pointer to the result [XrSpatialSnapshotEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialSnapshotEXT) .

The application **can** use [xrCreateSpatialUpdateSnapshotEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialUpdateSnapshotEXT) to create a snapshot and get the latest component data for specific entities as known by the runtime. Applications **can** provide the [XrSpatialEntityEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialEntityEXT) handles and the component types they are interested in when creating the snapshot.

The application **can** use [XrSpatialUpdateSnapshotCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialUpdateSnapshotCreateInfoEXT) :: `componentTypes` to filter the list of components whose data **must** be included in the snapshot. If the application provides a valid list of spatial component types in [XrSpatialUpdateSnapshotCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialUpdateSnapshotCreateInfoEXT) :: `componentTypes` , then the runtime **must** only include spatial entities in the snapshot that have at least one of the components provided in [XrSpatialUpdateSnapshotCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialUpdateSnapshotCreateInfoEXT) :: `componentTypes` . Also, the runtime **must** only include data for those components in the snapshot.

The runtime **must** return `XR_ERROR_SPATIAL_COMPONENT_NOT_ENABLED_EXT` if any of the [XrSpatialComponentTypeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentTypeEXT) in [XrSpatialUpdateSnapshotCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialUpdateSnapshotCreateInfoEXT) :: `componentTypes` are not enabled for the spatial capabilities passed to [XrSpatialContextCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialContextCreateInfoEXT) :: `capabilityConfigs` when creating `spatialContext` .

If the application does not provide a list of spatial component types in [XrSpatialUpdateSnapshotCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialUpdateSnapshotCreateInfoEXT) :: `componentTypes` , the runtime **must** include all the spatial entities listed in [XrSpatialUpdateSnapshotCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialUpdateSnapshotCreateInfoEXT) :: `entities` in the snapshot and it **must** include the data for all the enabled components of the capabilities configured for `spatialContext` .

The runtime **must** not include spatial entities that are not listed in [XrSpatialUpdateSnapshotCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialUpdateSnapshotCreateInfoEXT) :: `entities` in `snapshot` .

The application **can** create any number of snapshots it wants but **must** be mindful of the memory being allocated for each new snapshot and **must** destroy the snapshots once it no longer needs them.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrCreateSpatialUpdateSnapshotEXT-extension-notenabled) The `XR_EXT_spatial_entity` extension **must** be enabled prior to calling [xrCreateSpatialUpdateSnapshotEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialUpdateSnapshotEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrCreateSpatialUpdateSnapshotEXT-spatialContext-parameter) `spatialContext` **must** be a valid [XrSpatialContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialContextEXT) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrCreateSpatialUpdateSnapshotEXT-createInfo-parameter) `createInfo` **must** be a pointer to a valid [XrSpatialUpdateSnapshotCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialUpdateSnapshotCreateInfoEXT) structure
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrCreateSpatialUpdateSnapshotEXT-snapshot-parameter) `snapshot` **must** be a pointer to an [XrSpatialSnapshotEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialSnapshotEXT) handle

### Return Codes

[Success](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`
- `XR_SESSION_LOSS_PENDING`

[Failure](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_HANDLE_INVALID`
- `XR_ERROR_INSTANCE_LOST`
- `XR_ERROR_LIMIT_REACHED`
- `XR_ERROR_OUT_OF_MEMORY`
- `XR_ERROR_RUNTIME_FAILURE`
- `XR_ERROR_SESSION_LOST`
- `XR_ERROR_SPATIAL_COMPONENT_NOT_ENABLED_EXT`
- `XR_ERROR_TIME_INVALID`
- `XR_ERROR_VALIDATION_FAILURE`

The [XrSpatialUpdateSnapshotCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialUpdateSnapshotCreateInfoEXT) structure is defined as:

    typedef struct XrSpatialUpdateSnapshotCreateInfoEXT {
        XrStructureType                     type;
        const void*                         next;
        uint32_t                            entityCount;
        const XrSpatialEntityEXT*           entities;
        uint32_t                            componentTypeCount;
        const XrSpatialComponentTypeEXT*    componentTypes;
        XrSpace                             baseSpace;
        XrTime                              time;
    } XrSpatialUpdateSnapshotCreateInfoEXT;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.
- `entityCount` is a `uint32_t` describing the count of elements in the `entities` array.
- `entities` is an array of [XrSpatialEntityEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialEntityEXT) for which the runtime **must** include the component data in the snapshot.
- `componentTypeCount` is a `uint32_t` describing the count of elements in the `componentTypes` array.
- `componentTypes` is an array of [XrSpatialComponentTypeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentTypeEXT) for which the runtime **must** include the data in the snapshot.
- `baseSpace` is the [XrSpace](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpace) relative to which all the locations of the update [XrSpatialSnapshotEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialSnapshotEXT) will be located.
- `time` is the `XrTime` at which all the locations of the update [XrSpatialSnapshotEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialSnapshotEXT) will be located.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialUpdateSnapshotCreateInfoEXT-extension-notenabled) The `XR_EXT_spatial_entity` extension **must** be enabled prior to using [XrSpatialUpdateSnapshotCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialUpdateSnapshotCreateInfoEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialUpdateSnapshotCreateInfoEXT-type-type) `type` **must** be `XR_TYPE_SPATIAL_UPDATE_SNAPSHOT_CREATE_INFO_EXT`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialUpdateSnapshotCreateInfoEXT-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialUpdateSnapshotCreateInfoEXT-entities-parameter) `entities` **must** be a pointer to an array of `entityCount` valid [XrSpatialEntityEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialEntityEXT) handles
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialUpdateSnapshotCreateInfoEXT-componentTypes-parameter) If `componentTypeCount` is not `0` , `componentTypes` **must** be a pointer to an array of `componentTypeCount` valid [XrSpatialComponentTypeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentTypeEXT) values
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialUpdateSnapshotCreateInfoEXT-baseSpace-parameter) `baseSpace` **must** be a valid [XrSpace](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpace) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialUpdateSnapshotCreateInfoEXT-entityCount-arraylength) The `entityCount` parameter **must** be greater than `0`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialUpdateSnapshotCreateInfoEXT-commonparent) Both of `baseSpace` and the elements of `entities` **must** have been created, allocated, or retrieved from the same [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession)

### Destroy snapshot

The [xrDestroySpatialSnapshotEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrDestroySpatialSnapshotEXT) function is defined as:

    XrResult xrDestroySpatialSnapshotEXT(
        XrSpatialSnapshotEXT                        snapshot);

### Parameter Descriptions

- `snapshot` is an [XrSpatialSnapshotEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialSnapshotEXT) previously provided by [xrCreateSpatialDiscoverySnapshotCompleteEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialDiscoverySnapshotCompleteEXT) or [xrCreateSpatialUpdateSnapshotEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialUpdateSnapshotEXT) .

The application **can** call [xrDestroySpatialSnapshotEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrDestroySpatialSnapshotEXT) to destroy the [XrSpatialSnapshotEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialSnapshotEXT) handle and the resources associated with it.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrDestroySpatialSnapshotEXT-extension-notenabled) The `XR_EXT_spatial_entity` extension **must** be enabled prior to calling [xrDestroySpatialSnapshotEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrDestroySpatialSnapshotEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-xrDestroySpatialSnapshotEXT-snapshot-parameter) `snapshot` **must** be a valid [XrSpatialSnapshotEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialSnapshotEXT) handle

### Thread Safety

- Access to `snapshot` , and any child handles, **must** be externally synchronized

### Return Codes

[Success](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`

[Failure](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_HANDLE_INVALID`
- `XR_ERROR_RUNTIME_FAILURE`

## Common Components

### Bounded 2D

###### Component data

The [XrSpatialBounded2DDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBounded2DDataEXT) structure is defined as:

    typedef struct XrSpatialBounded2DDataEXT {
        XrPosef        center;
        XrExtent2Df    extents;
    } XrSpatialBounded2DDataEXT;

### Member Descriptions

- `center` is an [XrPosef](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrPosef) defining the geometric center of the bounded 2D component.
- `extents` is extents of the bounded 2D component along the x-axis (extents.width), y-axis (extents.height), centered on `center` .

The `extents` of the `XR_SPATIAL_COMPONENT_TYPE_BOUNDED_2D_EXT` refer to the entity's size in the x-y plane of the plane's coordinate system. A plane with a position of {0, 0, 0}, rotation of {0, 0, 0, 1} (no rotation), and an extent of {1, 1} refers to a 1 meter x 1 meter plane centered at {0, 0, 0} with its front face normal vector pointing towards the +Z direction in the component's space.

X X Y Y Z Z Height Height Y Y Z Z X X Vertical plane Vertical plane Horizontal Plane Horizontal Plane Width Width Width Width Height Height

### Figure 24. Bounded2D Component Coordinate System

### Note

OpenXR uses an X-Y plane with +Z as the plane normal but other APIs **may** use an X-Z plane with +Y as the plane normal. The X-Y plane **can** be converted to an X-Z plane by rotating -π/2 radians around the +X axis.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialBounded2DDataEXT-extension-notenabled) The `XR_EXT_spatial_entity` extension **must** be enabled prior to using [XrSpatialBounded2DDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBounded2DDataEXT)

###### Component list structure to query data

The [XrSpatialComponentBounded2DListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentBounded2DListEXT) structure is defined as:

    typedef struct XrSpatialComponentBounded2DListEXT {
        XrStructureType               type;
        void*                         next;
        uint32_t                      boundCount;
        XrSpatialBounded2DDataEXT*    bounds;
    } XrSpatialComponentBounded2DListEXT;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.
- `boundCount` is a `uint32_t` describing the count of elements in the `bounds` array.
- `bounds` is an array of [XrSpatialBounded2DDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBounded2DDataEXT) .

The runtime **must** return `XR_ERROR_VALIDATION_FAILURE` from [xrQuerySpatialComponentDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrQuerySpatialComponentDataEXT) if [XrSpatialComponentBounded2DListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentBounded2DListEXT) is in the next chain of [XrSpatialComponentDataQueryResultEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentDataQueryResultEXT) :: `next` but [XrSpatialComponentDataQueryConditionEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentDataQueryConditionEXT) ::componentTypeCount is not zero and `XR_SPATIAL_COMPONENT_TYPE_BOUNDED_2D_EXT` is not included in [XrSpatialComponentDataQueryConditionEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentDataQueryConditionEXT) :: `componentTypes` .

The runtime **must** return `XR_ERROR_SIZE_INSUFFICIENT` from [xrQuerySpatialComponentDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrQuerySpatialComponentDataEXT) if `boundCount` is less than [XrSpatialComponentDataQueryResultEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentDataQueryResultEXT) :: `entityIdCountOutput` .

If [xrQuerySpatialComponentDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrQuerySpatialComponentDataEXT) :: `snapshot` was created from [xrCreateSpatialDiscoverySnapshotCompleteEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialDiscoverySnapshotCompleteEXT) , then the runtime **must** provide [XrSpatialBounded2DDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBounded2DDataEXT) :: `center` in [XrCreateSpatialDiscoverySnapshotCompletionInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrCreateSpatialDiscoverySnapshotCompletionInfoEXT) :: `baseSpace` and [XrCreateSpatialDiscoverySnapshotCompletionInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrCreateSpatialDiscoverySnapshotCompletionInfoEXT) :: `time` .

If [xrQuerySpatialComponentDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrQuerySpatialComponentDataEXT) :: `snapshot` was created from [xrCreateSpatialUpdateSnapshotEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialUpdateSnapshotEXT) , then the runtime **must** provide [XrSpatialBounded2DDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBounded2DDataEXT) :: `center` in [XrSpatialUpdateSnapshotCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialUpdateSnapshotCreateInfoEXT) :: `baseSpace` and [XrSpatialUpdateSnapshotCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialUpdateSnapshotCreateInfoEXT) :: `time` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialComponentBounded2DListEXT-extension-notenabled) The `XR_EXT_spatial_entity` extension **must** be enabled prior to using [XrSpatialComponentBounded2DListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentBounded2DListEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialComponentBounded2DListEXT-type-type) `type` **must** be `XR_TYPE_SPATIAL_COMPONENT_BOUNDED_2D_LIST_EXT`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialComponentBounded2DListEXT-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialComponentBounded2DListEXT-bounds-parameter) `bounds` **must** be a pointer to an array of `boundCount` [XrSpatialBounded2DDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBounded2DDataEXT) structures
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialComponentBounded2DListEXT-boundCount-arraylength) The `boundCount` parameter **must** be greater than `0`

###### Configuration

If `XR_SPATIAL_COMPONENT_TYPE_BOUNDED_2D_EXT` is enumerated in [XrSpatialCapabilityComponentTypesEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityComponentTypesEXT) :: `componentTypes` for some capability, the application **can** enable it by including the enum value in the [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityConfigurationBaseHeaderEXT) :: `enabledComponents` list. This component does not require any special configuration to be included in the next chain of [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityConfigurationBaseHeaderEXT) .

### Bounded 3D

###### Component data

`XR_SPATIAL_COMPONENT_TYPE_BOUNDED_3D_EXT` uses [XrBoxf](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrBoxf) for its data.

###### Component list structure to query data

The [XrSpatialComponentBounded3DListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentBounded3DListEXT) structure is defined as:

    typedef struct XrSpatialComponentBounded3DListEXT {
        XrStructureType    type;
        void*              next;
        uint32_t           boundCount;
        XrBoxf*            bounds;
    } XrSpatialComponentBounded3DListEXT;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.
- `boundCount` is a `uint32_t` describing the count of elements in the `bounds` array.
- `bounds` is an array of [XrBoxf](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrBoxf) .

The runtime **must** return `XR_ERROR_VALIDATION_FAILURE` from [xrQuerySpatialComponentDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrQuerySpatialComponentDataEXT) if [XrSpatialComponentBounded3DListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentBounded3DListEXT) is in the next chain of [XrSpatialComponentDataQueryResultEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentDataQueryResultEXT) :: `next` but [XrSpatialComponentDataQueryConditionEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentDataQueryConditionEXT) ::componentTypeCount is not zero and `XR_SPATIAL_COMPONENT_TYPE_BOUNDED_3D_EXT` is not included in [XrSpatialComponentDataQueryConditionEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentDataQueryConditionEXT) :: `componentTypes` .

The runtime **must** return `XR_ERROR_SIZE_INSUFFICIENT` from [xrQuerySpatialComponentDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrQuerySpatialComponentDataEXT) if `boundCount` is less than [XrSpatialComponentDataQueryResultEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentDataQueryResultEXT) :: `entityIdCountOutput` .

If [xrQuerySpatialComponentDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrQuerySpatialComponentDataEXT) :: `snapshot` was created from [xrCreateSpatialDiscoverySnapshotCompleteEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialDiscoverySnapshotCompleteEXT) , then the runtime **must** provide [XrBoxf](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrBoxf) :: `center` in [XrCreateSpatialDiscoverySnapshotCompletionInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrCreateSpatialDiscoverySnapshotCompletionInfoEXT) :: `baseSpace` at [XrCreateSpatialDiscoverySnapshotCompletionInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrCreateSpatialDiscoverySnapshotCompletionInfoEXT) :: `time` .

If [xrQuerySpatialComponentDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrQuerySpatialComponentDataEXT) :: `snapshot` was created from [xrCreateSpatialUpdateSnapshotEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialUpdateSnapshotEXT) , then the runtime **must** provide [XrBoxf](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrBoxf) :: `center` in [XrSpatialUpdateSnapshotCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialUpdateSnapshotCreateInfoEXT) :: `baseSpace` at [XrSpatialUpdateSnapshotCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialUpdateSnapshotCreateInfoEXT) :: `time` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialComponentBounded3DListEXT-extension-notenabled) The `XR_EXT_spatial_entity` extension **must** be enabled prior to using [XrSpatialComponentBounded3DListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentBounded3DListEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialComponentBounded3DListEXT-type-type) `type` **must** be `XR_TYPE_SPATIAL_COMPONENT_BOUNDED_3D_LIST_EXT`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialComponentBounded3DListEXT-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialComponentBounded3DListEXT-bounds-parameter) `bounds` **must** be a pointer to an array of `boundCount` [XrBoxf](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrBoxf) structures
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialComponentBounded3DListEXT-boundCount-arraylength) The `boundCount` parameter **must** be greater than `0`

###### Configuration

If `XR_SPATIAL_COMPONENT_TYPE_BOUNDED_3D_EXT` is enumerated in [XrSpatialCapabilityComponentTypesEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityComponentTypesEXT) :: `componentTypes` for some capability, the application **can** enable it by including the enum in the [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityConfigurationBaseHeaderEXT) :: `enabledComponents` list. This component does not require any special configuration to be included in the next chain of [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityConfigurationBaseHeaderEXT) .

### Parent

###### Component data

`XR_SPATIAL_COMPONENT_TYPE_PARENT_EXT` uses `XrSpatialEntityIdEXT` for its data.

###### Component list structure to query data

The [XrSpatialComponentParentListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentParentListEXT) structure is defined as:

    typedef struct XrSpatialComponentParentListEXT {
        XrStructureType          type;
        void*                    next;
        uint32_t                 parentCount;
        XrSpatialEntityIdEXT*    parents;
    } XrSpatialComponentParentListEXT;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.
- `parentCount` is a `uint32_t` describing the count of elements in the `parents` array.
- `parents` is an array of `XrSpatialEntityIdEXT` .

The runtime **must** return `XR_ERROR_VALIDATION_FAILURE` from [xrQuerySpatialComponentDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrQuerySpatialComponentDataEXT) if [XrSpatialComponentParentListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentParentListEXT) is in the next chain of [XrSpatialComponentDataQueryResultEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentDataQueryResultEXT) :: `next` but [XrSpatialComponentDataQueryConditionEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentDataQueryConditionEXT) ::componentTypeCount is not zero and `XR_SPATIAL_COMPONENT_TYPE_PARENT_EXT` is not included in [XrSpatialComponentDataQueryConditionEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentDataQueryConditionEXT) :: `componentTypes` .

The runtime **must** return `XR_ERROR_SIZE_INSUFFICIENT` from [xrQuerySpatialComponentDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrQuerySpatialComponentDataEXT) if `parentCount` is less than [XrSpatialComponentDataQueryResultEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentDataQueryResultEXT) :: `entityIdCountOutput` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialComponentParentListEXT-extension-notenabled) The `XR_EXT_spatial_entity` extension **must** be enabled prior to using [XrSpatialComponentParentListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentParentListEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialComponentParentListEXT-type-type) `type` **must** be `XR_TYPE_SPATIAL_COMPONENT_PARENT_LIST_EXT`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialComponentParentListEXT-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialComponentParentListEXT-parents-parameter) `parents` **must** be a pointer to an array of `parentCount` `XrSpatialEntityIdEXT` values
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialComponentParentListEXT-parentCount-arraylength) The `parentCount` parameter **must** be greater than `0`

###### Configuration

If `XR_SPATIAL_COMPONENT_TYPE_PARENT_EXT` is enumerated in [XrSpatialCapabilityComponentTypesEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityComponentTypesEXT) :: `componentTypes` for some capability, the application **can** enable it by including the enum in the [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityConfigurationBaseHeaderEXT) :: `enabledComponents` list. This component does not require any special configuration to be included in the next chain of [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityConfigurationBaseHeaderEXT) .

### Mesh 3D

###### Component data

The [XrSpatialMeshDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialMeshDataEXT) structure is defined as:

    typedef struct XrSpatialMeshDataEXT {
        XrPosef               origin;
        XrSpatialBufferEXT    vertexBuffer;
        XrSpatialBufferEXT    indexBuffer;
    } XrSpatialMeshDataEXT;

### Member Descriptions

- `origin` is an [XrPosef](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrPosef) defining the origin of the mesh. All vertices of the mesh **must** be relative to this origin.
- `vertexBuffer` is an [XrSpatialBufferEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferEXT) that provides the ID for a buffer that represents the vertex buffer of the entity this component is on. The position of vertices **must** be relative to `origin` .
- `indexBuffer` is an [XrSpatialBufferEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferEXT) that provides the ID for a buffer that represents an array of triangle indices, specifying the indices of the mesh vertices in the `vertexBuffer` . The triangle indices **must** be returned in counter-clockwise order and three indices denote one triangle.

The component type using [XrSpatialMeshDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialMeshDataEXT) **must** specify the [XrSpatialBufferTypeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferTypeEXT) of the `vertexBuffer` and `indexBuffer` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialMeshDataEXT-extension-notenabled) The `XR_EXT_spatial_entity` extension **must** be enabled prior to using [XrSpatialMeshDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialMeshDataEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialMeshDataEXT-vertexBuffer-parameter) `vertexBuffer` **must** be a valid [XrSpatialBufferEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferEXT) structure
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialMeshDataEXT-indexBuffer-parameter) `indexBuffer` **must** be a valid [XrSpatialBufferEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferEXT) structure

###### Component list structure to query data

The [XrSpatialComponentMesh3DListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentMesh3DListEXT) structure is defined as:

    typedef struct XrSpatialComponentMesh3DListEXT {
        XrStructureType          type;
        void*                    next;
        uint32_t                 meshCount;
        XrSpatialMeshDataEXT*    meshes;
    } XrSpatialComponentMesh3DListEXT;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `meshCount` is a `uint32_t` describing the count of elements in the `meshes` array.
- `meshes` is an array of [XrSpatialMeshDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialMeshDataEXT) .

The application **can** query the mesh 3D component of the spatial entities in an [XrSpatialSnapshotEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialSnapshotEXT) by adding `XR_SPATIAL_COMPONENT_TYPE_MESH_3D_EXT` in [XrSpatialComponentDataQueryConditionEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentDataQueryConditionEXT) :: `componentTypes` and adding [XrSpatialComponentMesh3DListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentMesh3DListEXT) to the next pointer chain of [XrSpatialComponentDataQueryResultEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentDataQueryResultEXT) .

The runtime **must** return `XR_ERROR_VALIDATION_FAILURE` from [xrQuerySpatialComponentDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrQuerySpatialComponentDataEXT) if [XrSpatialComponentMesh3DListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentMesh3DListEXT) is in the next chain of [XrSpatialComponentDataQueryResultEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentDataQueryResultEXT) :: `next` but [XrSpatialComponentDataQueryConditionEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentDataQueryConditionEXT) ::componentTypeCount is not zero and `XR_SPATIAL_COMPONENT_TYPE_MESH_3D_EXT` is not included in [XrSpatialComponentDataQueryConditionEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentDataQueryConditionEXT) :: `componentTypes` .

The runtime **must** return `XR_ERROR_SIZE_INSUFFICIENT` from [xrQuerySpatialComponentDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrQuerySpatialComponentDataEXT) if `meshCount` is less than [XrSpatialComponentDataQueryResultEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentDataQueryResultEXT) :: `entityIdCountOutput` .

For the [XrSpatialMeshDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialMeshDataEXT) filled out by the runtime in the `meshes` array, the [XrSpatialBufferEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferEXT) :: `bufferType` for [XrSpatialMeshDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialMeshDataEXT) :: `vertexBuffer` **must** be `XR_SPATIAL_BUFFER_TYPE_VECTOR3F_EXT` and [XrSpatialBufferEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferEXT) :: `bufferType` for [XrSpatialMeshDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialMeshDataEXT) :: `indexBuffer` **must** be `XR_SPATIAL_BUFFER_TYPE_UINT32_EXT` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialComponentMesh3DListEXT-extension-notenabled) The `XR_EXT_spatial_entity` extension **must** be enabled prior to using [XrSpatialComponentMesh3DListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentMesh3DListEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialComponentMesh3DListEXT-type-type) `type` **must** be `XR_TYPE_SPATIAL_COMPONENT_MESH_3D_LIST_EXT`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialComponentMesh3DListEXT-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialComponentMesh3DListEXT-meshes-parameter) `meshes` **must** be a pointer to an array of `meshCount` [XrSpatialMeshDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialMeshDataEXT) structures
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialComponentMesh3DListEXT-meshCount-arraylength) The `meshCount` parameter **must** be greater than `0`

###### Configuration

If `XR_SPATIAL_COMPONENT_TYPE_MESH_3D_EXT` is enumerated in [XrSpatialCapabilityComponentTypesEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityComponentTypesEXT) :: `componentTypes` for some capability, the application **can** enable it by including the enum in the [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityConfigurationBaseHeaderEXT) :: `enabledComponents` list of the [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityConfigurationBaseHeaderEXT) derived structure of the capability that supports this component.

This component does not require any special configuration to be included in the next chain of [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityConfigurationBaseHeaderEXT) .

## Tracking state filters

The [XrSpatialFilterTrackingStateEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialFilterTrackingStateEXT) structure is defined as:

    typedef struct XrSpatialFilterTrackingStateEXT {
        XrStructureType                    type;
        const void*                        next;
        XrSpatialEntityTrackingStateEXT    trackingState;
    } XrSpatialFilterTrackingStateEXT;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `trackingState` is the [XrSpatialEntityTrackingStateEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialEntityTrackingStateEXT) for which the application wants to apply the filter.

The application **can** use [XrSpatialFilterTrackingStateEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialFilterTrackingStateEXT) in the next chain of [XrSpatialDiscoverySnapshotCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialDiscoverySnapshotCreateInfoEXT) to scope the discovery to only those entities whose tracking state is `trackingState` .

The application **can** use [XrSpatialFilterTrackingStateEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialFilterTrackingStateEXT) in the next chain of [XrSpatialComponentDataQueryConditionEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentDataQueryConditionEXT) to scope the component data query from a snapshot only to entities whose tracking state is `trackingState` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialFilterTrackingStateEXT-extension-notenabled) The `XR_EXT_spatial_entity` extension **must** be enabled prior to using [XrSpatialFilterTrackingStateEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialFilterTrackingStateEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialFilterTrackingStateEXT-type-type) `type` **must** be `XR_TYPE_SPATIAL_FILTER_TRACKING_STATE_EXT`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialFilterTrackingStateEXT-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#VUID-XrSpatialFilterTrackingStateEXT-trackingState-parameter) `trackingState` **must** be a valid [XrSpatialEntityTrackingStateEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialEntityTrackingStateEXT) value

## Example code

### Application Usage

Applications typically use the spatial entity extension in the following pattern:

- An application first enumerates the spatial capabilities of the system using [xrEnumerateSpatialCapabilitiesEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrEnumerateSpatialCapabilitiesEXT) . It then inspects the returned array of [XrSpatialCapabilityEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityEXT) and enumerates the components and features supported for each of those capabilities by using [xrEnumerateSpatialCapabilityComponentTypesEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrEnumerateSpatialCapabilityComponentTypesEXT) and [xrEnumerateSpatialCapabilityFeaturesEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrEnumerateSpatialCapabilityFeaturesEXT) respectively. This gives the application a full picture of the components that it **can** enable and the configurations the capability accepts.
- The application then creates one or many [XrSpatialContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialContextEXT) handles with specific spatial capability configurations, wherein the configurations enable \& configure a specific capability in the spatial context, and enable \& configure components for those capabilities.
- For each [XrSpatialContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialContextEXT) , the application waits to receive [XrEventDataSpatialDiscoveryRecommendedEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrEventDataSpatialDiscoveryRecommendedEXT) events for that [XrSpatialContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialContextEXT) before using [xrCreateSpatialDiscoverySnapshotAsyncEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialDiscoverySnapshotAsyncEXT) to discover spatial entities. Once this async operation is complete, the application receives a [XrSpatialSnapshotEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialSnapshotEXT) handle.
- The application queries for the entities and the component data included in this [XrSpatialSnapshotEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialSnapshotEXT) by using [xrQuerySpatialComponentDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrQuerySpatialComponentDataEXT) . The application reads the latest component data of the queried entities from structures attached to the next chain of [XrSpatialComponentDataQueryResultEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentDataQueryResultEXT) if the entity state is `XR_SPATIAL_ENTITY_TRACKING_STATE_TRACKING_EXT` .
- If there are specific entities that the application identifies as interesting and wants to get updates for over time, it creates [XrSpatialEntityEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialEntityEXT) handles for those entities by using [xrCreateSpatialEntityFromIdEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialEntityFromIdEXT) . The application gets updates for such interesting entities by using [xrCreateSpatialUpdateSnapshotEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialUpdateSnapshotEXT) and use the same [xrQuerySpatialComponentDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrQuerySpatialComponentDataEXT) function on the newly created [XrSpatialSnapshotEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialSnapshotEXT) to get the latest component data for those entities.

### Discover spatial entities \& query component data

The following example code demonstrates how to discover spatial entities for capability "Foo" query its component data.

    /****************************/
    /* Capability definition    */
    /****************************/
    // Foo capability has the following components -
    // - XR_SPATIAL_COMPONENT_TYPE_BOUNDED_2D_EXT
    #define XR_SPATIAL_CAPABILITY_FOO ((XrSpatialCapabilityEXT)1000740000U)

    #define XR_TYPE_SPATIAL_CAPABILITY_CONFIGURATION_FOO_EXT ((XrStructureType)1000740000U)
    // Derives from XrSpatialCapabilityConfigurationBaseHeaderEXT
    typedef struct XrSpatialCapabilityConfigurationFooEXT {
      XrStructureType                     type;
      const void* XR_MAY_ALIAS            next;
      XrSpatialCapabilityEXT              capability;
      uint32_t                            enabledComponentCount;
      const XrSpatialComponentTypeEXT*    enabledComponents;
    } XrSpatialCapabilityConfigurationFooEXT;

    /******************************/
    /* End capability definition  */
    /******************************/

    auto waitUntilReady = [](XrFutureEXT future) {
      XrFuturePollInfoEXT pollInfo{XR_TYPE_FUTURE_POLL_INFO_EXT};
      XrFuturePollResultEXT pollResult{XR_TYPE_FUTURE_POLL_RESULT_EXT};
      pollInfo.future = future;
      do {
        // sleep(1);
        CHK_XR(xrPollFutureEXT(instance, &pollInfo, &pollResult));
      } while (pollResult.state != XR_FUTURE_STATE_READY_EXT);
    };

    // Create a spatial spatial context
    XrSpatialContextEXT spatialContext{};
    {
      const std::array<XrSpatialComponentTypeEXT, 1> enabledComponents = {
        XR_SPATIAL_COMPONENT_TYPE_BOUNDED_2D_EXT,
      };

      // Configure Foo capability for the spatial context
      XrSpatialCapabilityConfigurationFooEXT fooConfig{XR_TYPE_SPATIAL_CAPABILITY_CONFIGURATION_FOO_EXT};
      fooConfig.capability = XR_SPATIAL_CAPABILITY_FOO;
      fooConfig.enabledComponentCount = enabledComponents.size();
      fooConfig.enabledComponents = enabledComponents.data();

      std::vector<XrSpatialCapabilityConfigurationBaseHeaderEXT*> capabilityConfigs;
      capabilityConfigs.push_back(reinterpret_cast<XrSpatialCapabilityConfigurationBaseHeaderEXT*>(&fooConfig));

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
    }

    auto discoverSpatialEntities = [&](XrSpatialContextEXT spatialContext, XrTime time) {
      // We want to look for entities that have the following components.
      std::array<XrSpatialComponentTypeEXT, 1> snapshotComponents {XR_SPATIAL_COMPONENT_TYPE_BOUNDED_2D_EXT};

      XrSpatialDiscoverySnapshotCreateInfoEXT snapshotCreateInfo{XR_TYPE_SPATIAL_DISCOVERY_SNAPSHOT_CREATE_INFO_EXT};
      snapshotCreateInfo.componentTypeCount = snapshotComponents.size();
      snapshotCreateInfo.componentTypes = snapshotComponents.data();
      XrFutureEXT future = XR_NULL_FUTURE_EXT;
      CHK_XR(xrCreateSpatialDiscoverySnapshotAsyncEXT(spatialContext, &snapshotCreateInfo, &future));

      waitUntilReady(future);

      XrCreateSpatialDiscoverySnapshotCompletionInfoEXT completionInfo{XR_TYPE_CREATE_SPATIAL_DISCOVERY_SNAPSHOT_COMPLETION_INFO_EXT};
      completionInfo.baseSpace = localSpace;
      completionInfo.time = time;
      completionInfo.future = future;

      XrCreateSpatialDiscoverySnapshotCompletionEXT completion{XR_TYPE_CREATE_SPATIAL_DISCOVERY_SNAPSHOT_COMPLETION_EXT};
      CHK_XR(xrCreateSpatialDiscoverySnapshotCompleteEXT(spatialContext, &completionInfo, &completion));
      if (completion.futureResult == XR_SUCCESS) {
        // Query for the bounded2d component data
        XrSpatialComponentTypeEXT componentToQuery = XR_SPATIAL_COMPONENT_TYPE_BOUNDED_2D_EXT;
        XrSpatialComponentDataQueryConditionEXT queryCond{XR_TYPE_SPATIAL_COMPONENT_DATA_QUERY_CONDITION_EXT};
        queryCond.componentTypes = &componentToQuery;

        XrSpatialComponentDataQueryResultEXT queryResult{XR_TYPE_SPATIAL_COMPONENT_DATA_QUERY_RESULT_EXT};
        queryResult.entityIdCapacityInput = 0;
        queryResult.entityIds = nullptr;
        queryResult.entityStateCapacityInput = 0;
        queryResult.entityStates = nullptr;
        CHK_XR(xrQuerySpatialComponentDataEXT(completion.snapshot, &queryCond, &queryResult));

        std::vector<XrSpatialEntityIdEXT> entityIds(queryResult.entityIdCountOutput);
        std::vector<XrSpatialEntityTrackingStateEXT> entityStates(queryResult.entityStateCountOutput);
        queryResult.entityIdCapacityInput = entityIds.size();
        queryResult.entityIds = entityIds.data();
        queryResult.entityStateCapacityInput = entityStates.size();
        queryResult.entityStates = entityStates.data();

        std::vector<XrSpatialBounded2DDataEXT> bounded2d(queryResult.entityIdCountOutput);
        XrSpatialComponentBounded2DListEXT boundsList{XR_TYPE_SPATIAL_COMPONENT_BOUNDED_2D_LIST_EXT};
        boundsList.boundCount = bounded2d.size();
        boundsList.bounds = bounded2d.data();
        queryResult.next = &boundsList;

        CHK_XR(xrQuerySpatialComponentDataEXT(completion.snapshot, &queryCond, &queryResult));

        for (int32_t i = 0; i < queryResult.entityIdCountOutput; ++i) {
          if (entityStates[i] == XR_SPATIAL_ENTITY_TRACKING_STATE_TRACKING_EXT) {
            // 2D extents for entity entityIds[i] is bounded2d[i].extents.
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

    CHK_XR(xrDestroySpatialContextEXT(spatialContext));

### Query buffer data

The following example code demonstrates how to get the data of a component that provides an [XrSpatialBufferEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferEXT) .

    /****************************/
    /* Component definition     */
    /****************************/
    // Foo component that provides an XrVector3f buffer
    #define XR_SPATIAL_COMPONENT_TYPE_FOO_EXT ((XrSpatialComponentTypeEXT)1000740000U)

    #define XR_TYPE_SPATIAL_COMPONENT_FOO_LIST_EXT ((XrStructureType)1000740000U)

    // XrSpatialComponentFooListEXT extends XrSpatialComponentDataQueryResultEXT
    typedef struct XrSpatialComponentFooListEXT {
        XrStructureType                   type;
        void* XR_MAY_ALIAS                next;
        uint32_t                          fooCount;
        XrSpatialBufferEXT*               foo;
    } XrSpatialComponentFooListEXT;

    /******************************/
    /* End Component definition  */
    /******************************/

    // Query for the foo component data
    XrSpatialComponentTypeEXT componentToQuery = XR_SPATIAL_COMPONENT_TYPE_FOO_EXT;
    XrSpatialComponentDataQueryConditionEXT queryCond{XR_TYPE_SPATIAL_COMPONENT_DATA_QUERY_CONDITION_EXT};
    queryCond.componentTypeCount = 1;
    queryCond.componentTypes = &componentToQuery;

    XrSpatialComponentDataQueryResultEXT queryResult{XR_TYPE_SPATIAL_COMPONENT_DATA_QUERY_RESULT_EXT};
    CHK_XR(xrQuerySpatialComponentDataEXT(snapshot, &queryCond, &queryResult));

    std::vector<XrSpatialEntityIdEXT> entityIds(queryResult.entityIdCountOutput);
    queryResult.entityIdCapacityInput = entityIds.size();
    queryResult.entityIds = entityIds.data();

    std::vector<XrSpatialBufferEXT> fooBuffers(queryResult.entityIdCountOutput);
    XrSpatialComponentFooListEXT fooList{XR_TYPE_SPATIAL_COMPONENT_FOO_LIST_EXT};
    fooList.fooCount = fooBuffers.size();
    fooList.foo = fooBuffers.data();
    queryResult.next = &fooList;

    CHK_XR(xrQuerySpatialComponentDataEXT(snapshot, &queryCond, &queryResult));

    for (int32_t i = 0; i < queryResult.entityIdCountOutput; ++i) {
      // foo component data for entity entityIds[i]
      if (fooBuffers[i].bufferType == XR_SPATIAL_BUFFER_TYPE_VECTOR3F_EXT) {
        XrSpatialBufferGetInfoEXT getInfo{XR_TYPE_SPATIAL_BUFFER_GET_INFO_EXT};
        getInfo.bufferId = fooBuffers[i].bufferId;
        uint32_t bufferCountOutput;
        CHK_XR(xrGetSpatialBufferVector3fEXT(snapshot, &getInfo, 0, &bufferCountOutput, nullptr));
        std::vector<XrVector3f> vertexBuffer(bufferCountOutput);
        CHK_XR(xrGetSpatialBufferVector3fEXT(snapshot, &getInfo, bufferCountOutput, &bufferCountOutput, vertexBuffer.data()));

        // XrVertex3f buffer for entity entityIds[i] is now available in vertexBuffer vector.
      }
    }

## Extension guidelines

- If an extension is defining a new [XrSpatialComponentTypeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentTypeEXT) which provides additional data about a spatial entity,

  - the extension **must** also define a list structure for that component which allows the application to pass an array to the runtime to fill out with the data for each of the spatial entities that satisfy [xrQuerySpatialComponentDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrQuerySpatialComponentDataEXT) :: `queryCondition` . Some examples of such list structures are [XrSpatialComponentParentListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentParentListEXT) and [XrSpatialComponentBounded2DListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentBounded2DListEXT) . If the component data size is variable and requires the application to use [the two-call idiom](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-buffer-size-parameters) to query it, the component data **should** provide an [XrSpatialBufferEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferEXT) for each variable-sized data in the list structure and it **must** specify the [XrSpatialBufferTypeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferTypeEXT) for each buffer. Application **can** then query the buffer data using functions defined in [Two-call idiom for component data](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#ext_spatial_entity_two_call_component_data) . An example of such a structure is [XrSpatialMeshDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialMeshDataEXT) which is included [XrSpatialComponentMesh3DListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentMesh3DListEXT) .
  - The extension **can** also provide structures that the application **can** chain to [XrSpatialComponentDataQueryConditionEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentDataQueryConditionEXT) :: `next` to provide additional filters for the query pertaining to the data of this component.
- Extensions **can** define structures that extend [XrSpatialDiscoverySnapshotCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialDiscoverySnapshotCreateInfoEXT) to provide additional filters for discovery. The filters for creating the snapshot **must** not affect the configuration of the spatial context, but instead are to be used to provide hints to the runtime on what entities and data are to be included in the snapshot as tracked by the current configuration of the spatial context (and therefore the current configuration of the underlying services).

- If an extension defines a new [XrSpatialCapabilityEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityEXT) ,

  - it **should** also specify the list of [XrSpatialComponentTypeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentTypeEXT) that the runtimes **must** provide on entities for that capability.
  - it **must** also provide structures derived from [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityConfigurationBaseHeaderEXT) that will allow the configuration of that capability.
- If an extension defines a new [XrSpatialCapabilityFeatureEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityFeatureEXT) , it **must** also define a corresponding configuration structure that **can** be chained to the next pointer of [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityConfigurationBaseHeaderEXT) , that the application **can** use to enable the feature when creating an [XrSpatialContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialContextEXT) .

- An extension defining a new [XrSpatialCapabilityEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityEXT) **should** follow this template for the specification -

  - Overview
  - Runtime support
  - Configuration
  - Guaranteed components
  - Example Code
- An extension defining a new [XrSpatialComponentTypeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentTypeEXT) **should** follow this template for the specification -

  - Component data
  - Component list structure to query data
  - Configuration
- When writing an api that provides the application with a `XrSpatialBufferIdEXT` , it **must** be accompanied with a [XrSpatialBufferTypeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferTypeEXT) to inform the application what the data type of the buffer is and the application **can** use an appropriate `xrGetSpatialBuffer*` function to retrieve the actual contents of the buffer.

### Semantic Label Design \& Extension Guidelines

While this extension does not define any component for conveying the semantic label information of an entity, it lays down the design rules and guidelines for any extensions that do define such a component. In the following text, " **should** " and " **must** " constrain the authors of such functionality, rather than constraining a runtime implementation or an application using the API.

- If an extension is defining semantic labels for any [XrSpatialCapabilityEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityEXT) , it **should** do so by defining a new [XrSpatialComponentTypeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentTypeEXT) as well as a new enumeration with a set of labels (a "semantic label set") to be the data for that component.
- An enumeration representing a semantic label set **must** have a value to indicate that the entity is not categorized into any of the labels of this set. The name of this enumerant **must** include 'UNCATEGORIZED', e.g. `XR_SPATIAL_PLANE_SEMANTIC_LABEL_UNCATEGORIZED_EXT` . This value indicates to applications that the runtime does recognize this entity, but that there are other semantic label sets where this entity is categorized.
- Enumeration of this newly defined [XrSpatialComponentTypeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentTypeEXT) in [xrEnumerateSpatialCapabilityComponentTypesEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrEnumerateSpatialCapabilityComponentTypesEXT) implies that the runtime supports the semantic label set (and therefore the labels defined in the set) corresponding to that component type.
- Applications express their desire to discover entities that have labels belonging to this semantic label set by including the corresponding [XrSpatialComponentTypeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentTypeEXT) in the [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityConfigurationBaseHeaderEXT) :: `enabledComponents` array of the configuration struct for the capability that the component type is enumerated for.
- It is possible that a single spatial entity has multiple components on it, each providing it with a label from their own semantic label set. Consider the following example with some hypothetical semantic label sets - `XrSpatialObjectSemanticLabel` , which might have values like chair, sofa, table etc., `XrSpatialSofaBrand` , which might have values like IKEA, Wayfair, etc., and `XrSpatialIkeaSofa` , which might have specific IKEA model names of sofas. In this scenario, the same sofa entity has all 3 components (labels from all 3 semantic label sets) on it, each giving a different granularity of information about the entity.
- If an extension is defining a new [XrSpatialComponentTypeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentTypeEXT) which provides a new semantic label set containing multiple labels in addition to the `UNCATEGORIZED` label, the extension **should** consider defining an [XrSpatialCapabilityFeatureEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityFeatureEXT) which allows applications to activate only a subset of the labels defined in the semantic label set corresponding to that component type. This subset, provided in the next chain of the capability configuration, acts as a hint for runtimes to optimize their tracking pipelines and only track the subset provided. An example of such a feature struct is provided [below](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#ext_spatial_entity_example_feature_semantic_label_subset) .
- Extensions **must** not add labels to existing semantic label set enumeration. They **must** instead define a new enumeration which contains equivalent enumerants with identical semantics and with values equal to those from the other set, in addition to the newly added enumerants. The specification of the newly defined semantic label set **must** also establish the mapping between the old label set and the new one. See example [below](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#ext_spatial_entity_example_semantic_label_extension) .

###### Example Spatial Feature Definition for Semantic Label Subset

    // New example semantic label set.
    typedef enum XrSpatialExampleSemanticLabelEXT {
      // ... label values
    } XrSpatialExampleSemanticLabelEXT;

    /*
    typedef enum XrSpatialCapabilityFeatureEXT {
      // .. existing values

      // new spatial feature value
      XR_SPATIAL_CAPABILITY_FEATURE_EXAMPLE_SEMANTIC_LABEL_SUBSET_EXT

      // .. existing values
    } XrSpatialCapabilityFeatureEXT;
    */

    // New spatial feaure configuration structure
    typedef struct XrSpatialFeatureExampleSemanticLabelSubsetEXT {
        XrStructureType                             type;
        const void* XR_MAY_ALIAS                    next;
        uint32_t                                    semanticLabelCount;
        const XrSpatialExampleSemanticLabelEXT*     semanticLabels;
    } XrSpatialFeatureExampleSemanticLabelSubsetEXT;

###### Example Spatial Semantic Label Extension

    typedef enum XrSpatialExamplePlaneSemanticLabelExtensionEXT {
        XR_SPATIAL_EXAMPLE_PLANE_SEMANTIC_LABEL_EXTENSION_UNCATEGORIZED_EXT = 1,
        XR_SPATIAL_EXAMPLE_PLANE_SEMANTIC_LABEL_EXTENSION_FLOOR_EXT = 2,
        XR_SPATIAL_EXAMPLE_PLANE_SEMANTIC_LABEL_EXTENSION_WALL_EXT = 3,
        XR_SPATIAL_EXAMPLE_PLANE_SEMANTIC_LABEL_EXTENSION_CEILING_EXT = 4,
        XR_SPATIAL_EXAMPLE_PLANE_SEMANTIC_LABEL_EXTENSION_TABLE_EXT = 5,
        XR_SPATIAL_EXAMPLE_PLANE_SEMANTIC_LABEL_EXTENSION_DOOR_EXT = 6,
        XR_SPATIAL_EXAMPLE_PLANE_SEMANTIC_LABEL_EXTENSION_WINDOW_EXT = 7,
        XR_SPATIAL_EXAMPLE_PLANE_SEMANTIC_LABEL_EXTENSION_MAX_ENUM_EXT = 0x7FFFFFFF
    } XrSpatialExamplePlaneSemanticLabelExtensionEXT;

Consider the above example where an extension defines an enumeration `XrSpatialExamplePlaneSemanticLabelExtensionEXT` in order to extend the existing [XrSpatialPlaneSemanticLabelEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialPlaneSemanticLabelEXT) with values to represent doors and windows. The specification for the new enumeration **must** include text for the following form -

    For all non-UNCATEGORIZED label enumerants in elink:XrSpatialPlaneSemanticLabelEXT,
    the runtime must: return that enumerant if and only if it returns the corresponding
    label enumerant from elink:XrSpatialExamplePlaneSemanticLabelExtensionEXT with the same value
    i.e.
    the ename:XR_SPATIAL_COMPONENT_TYPE_PLANE_SEMANTIC_LABEL_EXT value for that entity must:
    correspond with the ename:XR_SPATIAL_COMPONENT_TYPE_EXAMPLE_PLANE_SEMANTIC_LABEL_EXTENSION_EXT values
    according to the following table -

    [width="100%",options="header"]
    |====
    | XrSpatialExamplePlaneSemanticLabelExtensionEXT                | XrSpatialPlaneSemanticLabelEXT
    | XR_SPATIAL_EXAMPLE_PLANE_SEMANTIC_LABEL_EXTENSION_FLOOR_EXT   | XR_SPATIAL_PLANE_SEMANTIC_LABEL_FLOOR_EXT
    | XR_SPATIAL_EXAMPLE_PLANE_SEMANTIC_LABEL_EXTENSION_WALL_EXT    | XR_SPATIAL_PLANE_SEMANTIC_LABEL_WALL_EXT
    | XR_SPATIAL_EXAMPLE_PLANE_SEMANTIC_LABEL_EXTENSION_CEILING_EXT | XR_SPATIAL_PLANE_SEMANTIC_LABEL_CEILING_EXT
    | XR_SPATIAL_EXAMPLE_PLANE_SEMANTIC_LABEL_EXTENSION_TABLE_EXT   | XR_SPATIAL_PLANE_SEMANTIC_LABEL_TABLE_EXT
    | XR_SPATIAL_EXAMPLE_PLANE_SEMANTIC_LABEL_EXTENSION_DOOR_EXT    | XR_SPATIAL_PLANE_SEMANTIC_LABEL_UNCATEGORIZED_EXT
    | XR_SPATIAL_EXAMPLE_PLANE_SEMANTIC_LABEL_EXTENSION_WINDOW_EXT  | XR_SPATIAL_PLANE_SEMANTIC_LABEL_UNCATEGORIZED_EXT
    |====

## New Macros

- [XR_NULL_SPATIAL_BUFFER_ID_EXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XR_NULL_SPATIAL_BUFFER_ID_EXT)
- [XR_NULL_SPATIAL_ENTITY_ID_EXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XR_NULL_SPATIAL_ENTITY_ID_EXT)

## New Base Types

- `XrSpatialBufferIdEXT`
- `XrSpatialEntityIdEXT`

## New Object Types

- [XrSpatialContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialContextEXT)
- [XrSpatialEntityEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialEntityEXT)
- [XrSpatialSnapshotEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialSnapshotEXT)

## New Commands

- [xrCreateSpatialContextAsyncEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialContextAsyncEXT)
- [xrCreateSpatialContextCompleteEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialContextCompleteEXT)
- [xrCreateSpatialDiscoverySnapshotAsyncEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialDiscoverySnapshotAsyncEXT)
- [xrCreateSpatialDiscoverySnapshotCompleteEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialDiscoverySnapshotCompleteEXT)
- [xrCreateSpatialEntityFromIdEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialEntityFromIdEXT)
- [xrCreateSpatialUpdateSnapshotEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrCreateSpatialUpdateSnapshotEXT)
- [xrDestroySpatialContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrDestroySpatialContextEXT)
- [xrDestroySpatialEntityEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrDestroySpatialEntityEXT)
- [xrDestroySpatialSnapshotEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrDestroySpatialSnapshotEXT)
- [xrEnumerateSpatialCapabilitiesEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrEnumerateSpatialCapabilitiesEXT)
- [xrEnumerateSpatialCapabilityComponentTypesEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrEnumerateSpatialCapabilityComponentTypesEXT)
- [xrEnumerateSpatialCapabilityFeaturesEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrEnumerateSpatialCapabilityFeaturesEXT)
- [xrGetSpatialBufferFloatEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrGetSpatialBufferFloatEXT)
- [xrGetSpatialBufferStringEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrGetSpatialBufferStringEXT)
- [xrGetSpatialBufferUint16EXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrGetSpatialBufferUint16EXT)
- [xrGetSpatialBufferUint32EXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrGetSpatialBufferUint32EXT)
- [xrGetSpatialBufferUint8EXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrGetSpatialBufferUint8EXT)
- [xrGetSpatialBufferVector2fEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrGetSpatialBufferVector2fEXT)
- [xrGetSpatialBufferVector3fEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrGetSpatialBufferVector3fEXT)
- [xrQuerySpatialComponentDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#xrQuerySpatialComponentDataEXT)

## New Structures

- [XrCreateSpatialContextCompletionEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrCreateSpatialContextCompletionEXT)
- [XrCreateSpatialDiscoverySnapshotCompletionEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrCreateSpatialDiscoverySnapshotCompletionEXT)
- [XrCreateSpatialDiscoverySnapshotCompletionInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrCreateSpatialDiscoverySnapshotCompletionInfoEXT)
- [XrEventDataSpatialDiscoveryRecommendedEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrEventDataSpatialDiscoveryRecommendedEXT)
- [XrSpatialBounded2DDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBounded2DDataEXT)
- [XrSpatialBufferEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferEXT)
- [XrSpatialBufferGetInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferGetInfoEXT)
- [XrSpatialCapabilityComponentTypesEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityComponentTypesEXT)
- [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityConfigurationBaseHeaderEXT)
- [XrSpatialComponentDataQueryConditionEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentDataQueryConditionEXT)
- [XrSpatialComponentDataQueryResultEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentDataQueryResultEXT)
- [XrSpatialContextCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialContextCreateInfoEXT)
- [XrSpatialDiscoverySnapshotCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialDiscoverySnapshotCreateInfoEXT)
- [XrSpatialEntityFromIdCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialEntityFromIdCreateInfoEXT)
- [XrSpatialMeshDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialMeshDataEXT)
- [XrSpatialUpdateSnapshotCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialUpdateSnapshotCreateInfoEXT)
- Extending [XrSpatialComponentDataQueryResultEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentDataQueryResultEXT) :

  - [XrSpatialComponentBounded2DListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentBounded2DListEXT)
  - [XrSpatialComponentBounded3DListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentBounded3DListEXT)
  - [XrSpatialComponentMesh3DListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentMesh3DListEXT)
  - [XrSpatialComponentParentListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentParentListEXT)
- Extending [XrSpatialDiscoverySnapshotCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialDiscoverySnapshotCreateInfoEXT) , [XrSpatialComponentDataQueryConditionEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentDataQueryConditionEXT) :

  - [XrSpatialFilterTrackingStateEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialFilterTrackingStateEXT)

## New Enums

- [XrSpatialBufferTypeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialBufferTypeEXT)
- [XrSpatialCapabilityEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityEXT)
- [XrSpatialCapabilityFeatureEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialCapabilityFeatureEXT)
- [XrSpatialComponentTypeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialComponentTypeEXT)
- [XrSpatialEntityTrackingStateEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity#XrSpatialEntityTrackingStateEXT)

## New Enum Constants

- `XR_EXT_SPATIAL_ENTITY_EXTENSION_NAME`
- `XR_EXT_spatial_entity_SPEC_VERSION`
- Extending [XrObjectType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrObjectType) :

  - `XR_OBJECT_TYPE_SPATIAL_CONTEXT_EXT`
  - `XR_OBJECT_TYPE_SPATIAL_ENTITY_EXT`
  - `XR_OBJECT_TYPE_SPATIAL_SNAPSHOT_EXT`
- Extending [XrResult](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrResult) :

  - `XR_ERROR_SPATIAL_BUFFER_ID_INVALID_EXT`
  - `XR_ERROR_SPATIAL_CAPABILITY_CONFIGURATION_INVALID_EXT`
  - `XR_ERROR_SPATIAL_CAPABILITY_UNSUPPORTED_EXT`
  - `XR_ERROR_SPATIAL_COMPONENT_NOT_ENABLED_EXT`
  - `XR_ERROR_SPATIAL_COMPONENT_UNSUPPORTED_FOR_CAPABILITY_EXT`
  - `XR_ERROR_SPATIAL_ENTITY_ID_INVALID_EXT`
- Extending [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) :

  - `XR_TYPE_CREATE_SPATIAL_CONTEXT_COMPLETION_EXT`
  - `XR_TYPE_CREATE_SPATIAL_DISCOVERY_SNAPSHOT_COMPLETION_EXT`
  - `XR_TYPE_CREATE_SPATIAL_DISCOVERY_SNAPSHOT_COMPLETION_INFO_EXT`
  - `XR_TYPE_EVENT_DATA_SPATIAL_DISCOVERY_RECOMMENDED_EXT`
  - `XR_TYPE_SPATIAL_BUFFER_GET_INFO_EXT`
  - `XR_TYPE_SPATIAL_CAPABILITY_COMPONENT_TYPES_EXT`
  - `XR_TYPE_SPATIAL_COMPONENT_BOUNDED_2D_LIST_EXT`
  - `XR_TYPE_SPATIAL_COMPONENT_BOUNDED_3D_LIST_EXT`
  - `XR_TYPE_SPATIAL_COMPONENT_DATA_QUERY_CONDITION_EXT`
  - `XR_TYPE_SPATIAL_COMPONENT_DATA_QUERY_RESULT_EXT`
  - `XR_TYPE_SPATIAL_COMPONENT_MESH_3D_LIST_EXT`
  - `XR_TYPE_SPATIAL_COMPONENT_PARENT_LIST_EXT`
  - `XR_TYPE_SPATIAL_CONTEXT_CREATE_INFO_EXT`
  - `XR_TYPE_SPATIAL_DISCOVERY_SNAPSHOT_CREATE_INFO_EXT`
  - `XR_TYPE_SPATIAL_ENTITY_FROM_ID_CREATE_INFO_EXT`
  - `XR_TYPE_SPATIAL_FILTER_TRACKING_STATE_EXT`
  - `XR_TYPE_SPATIAL_UPDATE_SNAPSHOT_CREATE_INFO_EXT`

## Issues

- Does a single entity always derive from solely a single capability?

  - Resolved
  - Answer: No. It is completely upto the runtime based on its own tracking capabilities and how it wants to represent a detected entity. The spec does not prescribe any particular representation of spatial entity except for the guaranteed components of a given capability to set a minimum expectation. A runtime **may** be able to merge entities detected by separate capabilities and represent them as a single entity with the guaranteed components of all the capabilities that helped identify it. An example of this could be that tables can be detected by both a plane tracking capability and an object tracking capability, with plane tracking providing the `XR_SPATIAL_COMPONENT_TYPE_BOUNDED_2D_EXT` component on the entity and object tracking providing `XR_SPATIAL_COMPONENT_TYPE_BOUNDED_3D_EXT` . A certain runtime **may** provide the table as 2 separate entities, each with their own set of guaranteed components, while certain runtimes **may** provide just 1 entity to represent the table, and have both `XR_SPATIAL_COMPONENT_TYPE_BOUNDED_2D_EXT` and `XR_SPATIAL_COMPONENT_TYPE_BOUNDED_3D_EXT` on the same entity. What is important to note here is that a given spatial entity can have at most a single *component* of any given *component type* . Therefore, if the component data produced by the different capabilities conflicts for a certain entity, the runtime **must** represent them as 2 separate entities.

## Version History

- Revision 1, 2024-04-12 (Nihav Jain, Google)

  - Initial extension description