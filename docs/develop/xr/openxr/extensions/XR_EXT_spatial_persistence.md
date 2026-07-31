---
title: https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence
url: https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence
source: md.txt
---

### XR_EXT_spatial_persistence

**Name String**

`XR_EXT_spatial_persistence`

**Extension Type**

Instance extension

**Registered Extension Number**

764

**Revision**

1

**Ratification Status**

Ratified

**Extension and Version Dependencies**

`XR_EXT_spatial_entity`  

and  

`XR_EXT_future`

**Contributors**

Nihav Jain, Google  

Jared Finder, Google  

Natalie Fleury, Meta  

Yuichi Taguchi, Meta  

Ron Bessems, Meta  

Yin Li, Microsoft  

Jimmy Alamparambil, ByteDance  

Zhipeng Liu, ByteDance  

Jun Yan, ByteDance

## Overview

This extension allows applications to discover and correlate spatial entities across application sessions, OpenXR sessions and multiple OpenXR spatial contexts within a session. The `XR_EXT_spatial_entity` extension established that an entity within an [XrSpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextEXT) is represented by an `XrSpatialEntityIdEXT` . This extension extends on that concept by establishing that an entity, if persisted, is represented by an [XrUuid](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrUuid) across application and OpenXR sessions i.e. an application **can** use the [XrUuid](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrUuid) provided by this extension to identify an entity across sessions. This extension also provides useful overlaps with the `XR_EXT_spatial_entity` extension to discover persisted entities in the user's environment and the ability to query their component data.

## Spatial Persistence Context

### Create a spatial persistence context

    XR_DEFINE_HANDLE(XrSpatialPersistenceContextEXT)

The [XrSpatialPersistenceContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialPersistenceContextEXT) handle represents the connection to a persistent spatial entity storage.

The [xrCreateSpatialPersistenceContextAsyncEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#xrCreateSpatialPersistenceContextAsyncEXT) function is defined as:

    XrResult xrCreateSpatialPersistenceContextAsyncEXT(
        XrSession                                   session,
        const XrSpatialPersistenceContextCreateInfoEXT* createInfo,
        XrFutureEXT*                                future);

### Parameter Descriptions

- `session` is an [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) in which the spatial persistence context will be active.
- `createInfo` is the [XrSpatialPersistenceContextCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialPersistenceContextCreateInfoEXT) used to specify the spatial persistence context parameters.
- `future` is a pointer to an `XrFutureEXT` .

An application **can** create an [XrSpatialPersistenceContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialPersistenceContextEXT) handle using the [xrCreateSpatialPersistenceContextAsyncEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#xrCreateSpatialPersistenceContextAsyncEXT) function and configure the scope of the persistence context in `createInfo` .

The runtime **must** return `XR_ERROR_SPATIAL_PERSISTENCE_SCOPE_UNSUPPORTED_EXT` if [XrSpatialPersistenceContextCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialPersistenceContextCreateInfoEXT) :: `scope` is not enumerated by [xrEnumerateSpatialPersistenceScopesEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#xrEnumerateSpatialPersistenceScopesEXT) .

If a runtime enforces a permission system to control application access to the persistence storage represented by [XrSpatialPersistenceContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialPersistenceContextEXT) , then the runtime **must** return `XR_ERROR_PERMISSION_INSUFFICIENT` if those permissions have not been granted to this application.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#VUID-xrCreateSpatialPersistenceContextAsyncEXT-extension-notenabled) The `XR_EXT_spatial_persistence` extension **must** be enabled prior to calling [xrCreateSpatialPersistenceContextAsyncEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#xrCreateSpatialPersistenceContextAsyncEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#VUID-xrCreateSpatialPersistenceContextAsyncEXT-session-parameter) `session` **must** be a valid [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#VUID-xrCreateSpatialPersistenceContextAsyncEXT-createInfo-parameter) `createInfo` **must** be a pointer to a valid [XrSpatialPersistenceContextCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialPersistenceContextCreateInfoEXT) structure
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#VUID-xrCreateSpatialPersistenceContextAsyncEXT-future-parameter) `future` **must** be a pointer to an `XrFutureEXT` value

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
- `XR_ERROR_SPATIAL_PERSISTENCE_SCOPE_UNSUPPORTED_EXT`
- `XR_ERROR_VALIDATION_FAILURE`

The [XrSpatialPersistenceContextCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialPersistenceContextCreateInfoEXT) structure is defined as:

    typedef struct XrSpatialPersistenceContextCreateInfoEXT {
        XrStructureType                 type;
        const void*                     next;
        XrSpatialPersistenceScopeEXT    scope;
    } XrSpatialPersistenceContextCreateInfoEXT;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.
- `scope` is an [XrSpatialPersistenceScopeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialPersistenceScopeEXT) defining the storage scope of the persistence context.

The [XrSpatialPersistenceContextCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialPersistenceContextCreateInfoEXT) structure describes the information to create an [XrSpatialPersistenceContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialPersistenceContextEXT) handle.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#VUID-XrSpatialPersistenceContextCreateInfoEXT-extension-notenabled) The `XR_EXT_spatial_persistence` extension **must** be enabled prior to using [XrSpatialPersistenceContextCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialPersistenceContextCreateInfoEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#VUID-XrSpatialPersistenceContextCreateInfoEXT-type-type) `type` **must** be `XR_TYPE_SPATIAL_PERSISTENCE_CONTEXT_CREATE_INFO_EXT`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#VUID-XrSpatialPersistenceContextCreateInfoEXT-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#VUID-XrSpatialPersistenceContextCreateInfoEXT-scope-parameter) `scope` **must** be a valid [XrSpatialPersistenceScopeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialPersistenceScopeEXT) value

    typedef enum XrSpatialPersistenceScopeEXT {
        XR_SPATIAL_PERSISTENCE_SCOPE_SYSTEM_MANAGED_EXT = 1,
        XR_SPATIAL_PERSISTENCE_SCOPE_LOCAL_ANCHORS_EXT = 1000781000,
        XR_SPATIAL_PERSISTENCE_SCOPE_MAX_ENUM_EXT = 0x7FFFFFFF
    } XrSpatialPersistenceScopeEXT;

The [XrSpatialPersistenceScopeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialPersistenceScopeEXT) enumeration identifies the different types of persistence context scopes.

The enums have the following meanings:

Enum Description

`XR_SPATIAL_PERSISTENCE_SCOPE_SYSTEM_MANAGED_EXT`

Provides the application with read-only access (i.e. application cannot modify the store associated with this scope) to spatial entities persisted and managed by the system. The application **can** use the UUID in the persistence component for this scope to correlate entities across spatial contexts and device reboots.

`XR_SPATIAL_PERSISTENCE_SCOPE_LOCAL_ANCHORS_EXT`

Persistence operations and data access is limited to spatial anchors, on the same device, for the same user and same app (Added by the `XR_EXT_spatial_persistence_operations` extension)

The [xrEnumerateSpatialPersistenceScopesEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#xrEnumerateSpatialPersistenceScopesEXT) function is defined as:

    XrResult xrEnumerateSpatialPersistenceScopesEXT(
        XrInstance                                  instance,
        XrSystemId                                  systemId,
        uint32_t                                    persistenceScopeCapacityInput,
        uint32_t*                                   persistenceScopeCountOutput,
        XrSpatialPersistenceScopeEXT*               persistenceScopes);

### Parameter Descriptions

- `instance` is a handle to an [XrInstance](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrInstance) .
- `systemId` is the `XrSystemId` whose spatial persistence scopes will be enumerated.
- `persistenceScopeCapacityInput` is the capacity of the `persistenceScopes` array, or 0 to indicate a request to retrieve the required capacity.
- `persistenceScopeCountOutput` is the number of persistence scopes, or the required capacity in the case that `persistenceScopeCapacityInput` is insufficient.
- `persistenceScopes` is an array of [XrSpatialPersistenceScopeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialPersistenceScopeEXT) . It **can** be `NULL` if `persistenceScopeCapacityInput` is 0.
- See [Buffer Size Parameters](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-buffer-size-parameters) chapter for a detailed description of retrieving the required `persistenceScopes` size.

The application **can** enumerate the list of spatial persistence scopes supported by a given `XrSystemId` using [xrEnumerateSpatialPersistenceScopesEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#xrEnumerateSpatialPersistenceScopesEXT) .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#VUID-xrEnumerateSpatialPersistenceScopesEXT-extension-notenabled) The `XR_EXT_spatial_persistence` extension **must** be enabled prior to calling [xrEnumerateSpatialPersistenceScopesEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#xrEnumerateSpatialPersistenceScopesEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#VUID-xrEnumerateSpatialPersistenceScopesEXT-instance-parameter) `instance` **must** be a valid [XrInstance](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrInstance) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#VUID-xrEnumerateSpatialPersistenceScopesEXT-persistenceScopeCountOutput-parameter) `persistenceScopeCountOutput` **must** be a pointer to a `uint32_t` value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#VUID-xrEnumerateSpatialPersistenceScopesEXT-persistenceScopes-parameter) If `persistenceScopeCapacityInput` is not `0` , `persistenceScopes` **must** be a pointer to an array of `persistenceScopeCapacityInput` [XrSpatialPersistenceScopeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialPersistenceScopeEXT) values

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

The [xrCreateSpatialPersistenceContextCompleteEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#xrCreateSpatialPersistenceContextCompleteEXT) function is defined as:

    XrResult xrCreateSpatialPersistenceContextCompleteEXT(
        XrSession                                   session,
        XrFutureEXT                                 future,
        XrCreateSpatialPersistenceContextCompletionEXT* completion);

### Parameter Descriptions

- `session` is the [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) previously passed to [xrCreateSpatialPersistenceContextAsyncEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#xrCreateSpatialPersistenceContextAsyncEXT) :: `session` .
- `future` is the `XrFutureEXT` received from [xrCreateSpatialPersistenceContextAsyncEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#xrCreateSpatialPersistenceContextAsyncEXT) .
- `completion` is a pointer to an [XrCreateSpatialPersistenceContextCompletionEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrCreateSpatialPersistenceContextCompletionEXT) .

[xrCreateSpatialPersistenceContextCompleteEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#xrCreateSpatialPersistenceContextCompleteEXT) completes the asynchronous operation started by [xrCreateSpatialPersistenceContextAsyncEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#xrCreateSpatialPersistenceContextAsyncEXT) . The runtime **must** return `XR_ERROR_FUTURE_PENDING_EXT` if `future` is not in ready state. The runtime **must** return `XR_ERROR_FUTURE_INVALID_EXT` if `future` has already been completed or cancelled.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#VUID-xrCreateSpatialPersistenceContextCompleteEXT-extension-notenabled) The `XR_EXT_spatial_persistence` extension **must** be enabled prior to calling [xrCreateSpatialPersistenceContextCompleteEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#xrCreateSpatialPersistenceContextCompleteEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#VUID-xrCreateSpatialPersistenceContextCompleteEXT-session-parameter) `session` **must** be a valid [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#VUID-xrCreateSpatialPersistenceContextCompleteEXT-completion-parameter) `completion` **must** be a pointer to an [XrCreateSpatialPersistenceContextCompletionEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrCreateSpatialPersistenceContextCompletionEXT) structure

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

The [XrCreateSpatialPersistenceContextCompletionEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrCreateSpatialPersistenceContextCompletionEXT) structure is defined as:

    typedef struct XrCreateSpatialPersistenceContextCompletionEXT {
        XrStructureType                         type;
        void*                                   next;
        XrResult                                futureResult;
        XrSpatialPersistenceContextResultEXT    createResult;
        XrSpatialPersistenceContextEXT          persistenceContext;
    } XrCreateSpatialPersistenceContextCompletionEXT;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `futureResult` is the [XrResult](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrResult) of the spatial persistence context creation operation.
- `createResult` is the [XrSpatialPersistenceContextResultEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialPersistenceContextResultEXT) of the spatial persistence context creation operation.
- `persistenceContext` is an [XrSpatialPersistenceContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialPersistenceContextEXT) created using the data and configuration in [xrCreateSpatialPersistenceContextAsyncEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#xrCreateSpatialPersistenceContextAsyncEXT) :: `createInfo` .

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
- `XR_ERROR_PERMISSION_INSUFFICIENT`

If `futureResult` and `createResult` are both success codes, `persistenceContext` **must** be valid. If `persistenceContext` is valid, it **must** remain so within the lifecycle of [xrCreateSpatialPersistenceContextAsyncEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#xrCreateSpatialPersistenceContextAsyncEXT) :: `session` or until the application uses [xrDestroySpatialPersistenceContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#xrDestroySpatialPersistenceContextEXT) with `persistenceContext` , whichever comes first.

The runtime **must** set `createResult` only if `futureResult` is a success code.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#VUID-XrCreateSpatialPersistenceContextCompletionEXT-extension-notenabled) The `XR_EXT_spatial_persistence` extension **must** be enabled prior to using [XrCreateSpatialPersistenceContextCompletionEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrCreateSpatialPersistenceContextCompletionEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#VUID-XrCreateSpatialPersistenceContextCompletionEXT-type-type) `type` **must** be `XR_TYPE_CREATE_SPATIAL_PERSISTENCE_CONTEXT_COMPLETION_EXT`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#VUID-XrCreateSpatialPersistenceContextCompletionEXT-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#VUID-XrCreateSpatialPersistenceContextCompletionEXT-futureResult-parameter) `futureResult` **must** be a valid [XrResult](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrResult) value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#VUID-XrCreateSpatialPersistenceContextCompletionEXT-createResult-parameter) `createResult` **must** be a valid [XrSpatialPersistenceContextResultEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialPersistenceContextResultEXT) value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#VUID-XrCreateSpatialPersistenceContextCompletionEXT-persistenceContext-parameter) `persistenceContext` **must** be a valid [XrSpatialPersistenceContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialPersistenceContextEXT) handle

    typedef enum XrSpatialPersistenceContextResultEXT {
        XR_SPATIAL_PERSISTENCE_CONTEXT_RESULT_SUCCESS_EXT = 0,
        XR_SPATIAL_PERSISTENCE_CONTEXT_RESULT_ENTITY_NOT_TRACKING_EXT = -1000781001,
        XR_SPATIAL_PERSISTENCE_CONTEXT_RESULT_PERSIST_UUID_NOT_FOUND_EXT = -1000781002,
        XR_SPATIAL_PERSISTENCE_CONTEXT_RESULT_MAX_ENUM_EXT = 0x7FFFFFFF
    } XrSpatialPersistenceContextResultEXT;

The [XrSpatialPersistenceContextResultEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialPersistenceContextResultEXT) enumeration identifies the different types of result codes for a persistence operation. Failures during persistence operations are not always in control of the application and this enumeration is used for conveying such cases. Similar to [XrResult](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrResult) , success codes in the [XrSpatialPersistenceContextResultEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialPersistenceContextResultEXT) enumeration are non-negative values, and failure codes are negative values.

The enums have the following meanings:

Enum Description

`XR_SPATIAL_PERSISTENCE_CONTEXT_RESULT_SUCCESS_EXT`

The persistence context operation was a success.

`XR_SPATIAL_PERSISTENCE_CONTEXT_RESULT_ENTITY_NOT_TRACKING_EXT`

The persistence operation failed because the entity could not be tracked by the runtime. (Added by the `XR_EXT_spatial_persistence_operations` extension)

`XR_SPATIAL_PERSISTENCE_CONTEXT_RESULT_PERSIST_UUID_NOT_FOUND_EXT`

The provided persist UUID was not found in the storage. (Added by the `XR_EXT_spatial_persistence_operations` extension)

### Destroy the spatial persistence context

The [xrDestroySpatialPersistenceContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#xrDestroySpatialPersistenceContextEXT) function is defined as:

    XrResult xrDestroySpatialPersistenceContextEXT(
        XrSpatialPersistenceContextEXT              persistenceContext);

### Parameter Descriptions

- `persistenceContext` is an [XrSpatialPersistenceContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialPersistenceContextEXT) previously created by [xrCreateSpatialPersistenceContextAsyncEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#xrCreateSpatialPersistenceContextAsyncEXT) .

The application **can** use [xrDestroySpatialPersistenceContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#xrDestroySpatialPersistenceContextEXT) to release the `persistenceContext` handle when it is finished with spatial persistence tasks.

The runtime **must** not destroy the underlying resources for `persistenceContext` when [xrDestroySpatialPersistenceContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#xrDestroySpatialPersistenceContextEXT) is called if there are any valid [XrSpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextEXT) handles that `persistenceContext` was linked to via [XrSpatialContextPersistenceConfigEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialContextPersistenceConfigEXT) . This is because the persistence context's resources are still used by the spatial context for discovering persisted entities. Destroying the persistence context handle in such a situation only removes the application's access to these resources.

The resources for a destroyed [XrSpatialPersistenceContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialPersistenceContextEXT) **must** be freed when all the [XrSpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextEXT) handles the persistence context was linked to are destroyed.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#VUID-xrDestroySpatialPersistenceContextEXT-extension-notenabled) The `XR_EXT_spatial_persistence` extension **must** be enabled prior to calling [xrDestroySpatialPersistenceContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#xrDestroySpatialPersistenceContextEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#VUID-xrDestroySpatialPersistenceContextEXT-persistenceContext-parameter) `persistenceContext` **must** be a valid [XrSpatialPersistenceContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialPersistenceContextEXT) handle

### Thread Safety

- Access to `persistenceContext` , and any child handles, **must** be externally synchronized

### Return Codes

[Success](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`

[Failure](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_HANDLE_INVALID`
- `XR_ERROR_RUNTIME_FAILURE`

## Discover persisted entities

### Persistence component

Persisted spatial entities have the persistence component on them which the runtime **must** include in the discovery and update snapshots if `XR_SPATIAL_COMPONENT_TYPE_PERSISTENCE_EXT` is enabled during the creation of [XrSpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextEXT) and included in [XrSpatialDiscoverySnapshotCreateInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialDiscoverySnapshotCreateInfoEXT) :: `componentTypes` or [XrSpatialUpdateSnapshotCreateInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialUpdateSnapshotCreateInfoEXT) :: `componentTypes` .

###### Component Data

The [XrSpatialPersistenceDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialPersistenceDataEXT) structure is defined as:

    typedef struct XrSpatialPersistenceDataEXT {
        XrUuid                          persistUuid;
        XrSpatialPersistenceStateEXT    persistState;
    } XrSpatialPersistenceDataEXT;

### Member Descriptions

- `persistUuid` is an [XrUuid](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrUuid) .
- `persistState` is an [XrSpatialPersistenceStateEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialPersistenceStateEXT) representing the persistence state of `persistUuid`

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#VUID-XrSpatialPersistenceDataEXT-extension-notenabled) The `XR_EXT_spatial_persistence` extension **must** be enabled prior to using [XrSpatialPersistenceDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialPersistenceDataEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#VUID-XrSpatialPersistenceDataEXT-persistState-parameter) `persistState` **must** be a valid [XrSpatialPersistenceStateEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialPersistenceStateEXT) value

    typedef enum XrSpatialPersistenceStateEXT {
        XR_SPATIAL_PERSISTENCE_STATE_LOADED_EXT = 1,
        XR_SPATIAL_PERSISTENCE_STATE_NOT_FOUND_EXT = 2,
        XR_SPATIAL_PERSISTENCE_STATE_MAX_ENUM_EXT = 0x7FFFFFFF
    } XrSpatialPersistenceStateEXT;

The [XrSpatialPersistenceStateEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialPersistenceStateEXT) enumeration identifies the different states of the persisted uuid.

The enums have the following meanings:

Enum Description

`XR_SPATIAL_PERSISTENCE_STATE_LOADED_EXT`

The persisted UUID has been successfully loaded from the storage.

`XR_SPATIAL_PERSISTENCE_STATE_NOT_FOUND_EXT`

The persisted UUID was not found in the storage and was either removed from it or never was in it.

###### Component list structure to query data

The [XrSpatialComponentPersistenceListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialComponentPersistenceListEXT) structure is defined as:

    typedef struct XrSpatialComponentPersistenceListEXT {
        XrStructureType                 type;
        void*                           next;
        uint32_t                        persistDataCount;
        XrSpatialPersistenceDataEXT*    persistData;
    } XrSpatialComponentPersistenceListEXT;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.
- `persistDataCount` is a `uint32_t` describing the count of elements in the `persistData` array.
- `persistData` is an array of [XrSpatialPersistenceDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialPersistenceDataEXT) .

The runtime **must** return `XR_ERROR_VALIDATION_FAILURE` from [xrQuerySpatialComponentDataEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrQuerySpatialComponentDataEXT) if [XrSpatialComponentPersistenceListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialComponentPersistenceListEXT) is in the next chain of [XrSpatialComponentDataQueryResultEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryResultEXT) :: `next` but `XR_SPATIAL_COMPONENT_TYPE_PERSISTENCE_EXT` is not included in [XrSpatialComponentDataQueryConditionEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryConditionEXT) :: `componentTypes` .

The runtime **must** return `XR_ERROR_SIZE_INSUFFICIENT` from [xrQuerySpatialComponentDataEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrQuerySpatialComponentDataEXT) if `persistDataCount` is less than [XrSpatialComponentDataQueryResultEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryResultEXT) :: `entityIdCountOutput` .

Unlike the other components, the runtime **must** set the data for `XR_SPATIAL_COMPONENT_TYPE_PERSISTENCE_EXT` regardless of the [XrSpatialEntityTrackingStateEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialEntityTrackingStateEXT) .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#VUID-XrSpatialComponentPersistenceListEXT-extension-notenabled) The `XR_EXT_spatial_persistence` extension **must** be enabled prior to using [XrSpatialComponentPersistenceListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialComponentPersistenceListEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#VUID-XrSpatialComponentPersistenceListEXT-type-type) `type` **must** be `XR_TYPE_SPATIAL_COMPONENT_PERSISTENCE_LIST_EXT`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#VUID-XrSpatialComponentPersistenceListEXT-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#VUID-XrSpatialComponentPersistenceListEXT-persistData-parameter) `persistData` **must** be a pointer to an array of `persistDataCount` [XrSpatialPersistenceDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialPersistenceDataEXT) structures
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#VUID-XrSpatialComponentPersistenceListEXT-persistDataCount-arraylength) The `persistDataCount` parameter **must** be greater than `0`

###### Configuration

If `XR_SPATIAL_COMPONENT_TYPE_PERSISTENCE_EXT` is enumerated in [XrSpatialCapabilityComponentTypesEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityComponentTypesEXT) :: `componentTypes` for some capability, the application **can** enable it by including the enum in the [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityConfigurationBaseHeaderEXT) :: `enabledComponents` list. This component does not require any special configuration to be included in the next chain of [XrSpatialCapabilityConfigurationBaseHeaderEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialCapabilityConfigurationBaseHeaderEXT) . If the application is including `XR_SPATIAL_COMPONENT_TYPE_PERSISTENCE_EXT` in the enabled component list, it **must** also include [XrSpatialContextPersistenceConfigEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialContextPersistenceConfigEXT) in the next chain of [XrSpatialContextCreateInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextCreateInfoEXT) otherwise the runtime **must** return `XR_ERROR_SPATIAL_CAPABILITY_CONFIGURATION_INVALID_EXT` from [xrCreateSpatialContextAsyncEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateSpatialContextAsyncEXT) .

### Configure spatial context with persistence contexts

The [XrSpatialContextPersistenceConfigEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialContextPersistenceConfigEXT) structure is defined as:

    typedef struct XrSpatialContextPersistenceConfigEXT {
        XrStructureType                          type;
        const void*                              next;
        uint32_t                                 persistenceContextCount;
        const XrSpatialPersistenceContextEXT*    persistenceContexts;
    } XrSpatialContextPersistenceConfigEXT;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.
- `persistenceContextCount` is a `uint32_t` describing the count of elements in the `persistenceContexts` array.
- `persistenceContexts` is an an array of [XrSpatialPersistenceContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialPersistenceContextEXT) .

An application **can** add [XrSpatialContextPersistenceConfigEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialContextPersistenceConfigEXT) to the next chain of [XrSpatialContextCreateInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextCreateInfoEXT) . This will configure the created [XrSpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextEXT) with `persistenceContexts` and allow the application to discover the spatial entities persisted in the storage represented by the [XrSpatialPersistenceContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialPersistenceContextEXT) handles in `persistenceContexts` .

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#VUID-XrSpatialContextPersistenceConfigEXT-extension-notenabled) The `XR_EXT_spatial_persistence` extension **must** be enabled prior to using [XrSpatialContextPersistenceConfigEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialContextPersistenceConfigEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#VUID-XrSpatialContextPersistenceConfigEXT-type-type) `type` **must** be `XR_TYPE_SPATIAL_CONTEXT_PERSISTENCE_CONFIG_EXT`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#VUID-XrSpatialContextPersistenceConfigEXT-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#VUID-XrSpatialContextPersistenceConfigEXT-persistenceContexts-parameter) `persistenceContexts` **must** be a pointer to an array of `persistenceContextCount` valid [XrSpatialPersistenceContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialPersistenceContextEXT) handles
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#VUID-XrSpatialContextPersistenceConfigEXT-persistenceContextCount-arraylength) The `persistenceContextCount` parameter **must** be greater than `0`

### Create discovery snapshot

###### Discover entities with specific UUIDs

The [XrSpatialDiscoveryPersistenceUuidFilterEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialDiscoveryPersistenceUuidFilterEXT) structure is defined as:

    typedef struct XrSpatialDiscoveryPersistenceUuidFilterEXT {
        XrStructureType    type;
        const void*        next;
        uint32_t           persistedUuidCount;
        const XrUuid*      persistedUuids;
    } XrSpatialDiscoveryPersistenceUuidFilterEXT;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain. No such structures are defined in core OpenXR or this extension.
- `persistedUuidCount` is a `uint32_t` describing the count of elements in the `persistedUuids` array
- `persistedUuids` is an array of [XrUuid](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrUuid) .

The application **can** use [XrSpatialDiscoveryPersistenceUuidFilterEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialDiscoveryPersistenceUuidFilterEXT) in the next chain of [XrSpatialDiscoverySnapshotCreateInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialDiscoverySnapshotCreateInfoEXT) to scope the discovery operation to just the entities whose persisted UUIDs are in the set of the UUIDs provided in `persistedUuids` .

If the application adds [XrSpatialDiscoveryPersistenceUuidFilterEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialDiscoveryPersistenceUuidFilterEXT) in the next chain of [XrSpatialDiscoverySnapshotCreateInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialDiscoverySnapshotCreateInfoEXT) but the [xrCreateSpatialDiscoverySnapshotAsyncEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateSpatialDiscoverySnapshotAsyncEXT) :: `spatialContext` was not configured with any [XrSpatialPersistenceContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialPersistenceContextEXT) using [XrSpatialContextPersistenceConfigEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialContextPersistenceConfigEXT) , the runtime **must** return `XR_ERROR_VALIDATION_FAILURE` from [xrCreateSpatialDiscoverySnapshotAsyncEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateSpatialDiscoverySnapshotAsyncEXT) .

The runtime **must** treat the [XrSpatialDiscoveryPersistenceUuidFilterEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialDiscoveryPersistenceUuidFilterEXT) filter as an 'AND' condition with any other filters provided in [XrSpatialDiscoverySnapshotCreateInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialDiscoverySnapshotCreateInfoEXT) or its next chain. The runtime **must** treat the `persistedUuids` array itself as an 'OR' condition i.e. filter for entities that have any of the UUIDs provided in that array.

The runtime **must** include one entry in the created snapshot for each of the UUIDs in `persistedUuids` for which it was able to determine the [XrSpatialPersistenceStateEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialPersistenceStateEXT) state at this time.

- If the runtime has successfully found the UUID in its storage, then -

  - The runtime **must** set the [XrSpatialPersistenceStateEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialPersistenceStateEXT) in the [XrSpatialPersistenceDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialPersistenceDataEXT) of this entity to `XR_SPATIAL_PERSISTENCE_STATE_LOADED_EXT` .
  - The runtime **must** include a valid `XrSpatialEntityIdEXT` for this entity in the created snapshot.
  - The runtime **must** set the [XrSpatialEntityTrackingStateEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialEntityTrackingStateEXT) of that entity to `XR_SPATIAL_ENTITY_TRACKING_STATE_TRACKING_EXT` if it is actively tracking the entity and has valid data for its components. Otherwise, the runtime **must** set the [XrSpatialEntityTrackingStateEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialEntityTrackingStateEXT) to `XR_SPATIAL_ENTITY_TRACKING_STATE_PAUSED_EXT` .
- If the runtime has determined that the UUID is not present in its storage (regardless of whether that UUID was never in the storage or has was present once but has since been unpersisted), then -

  - The runtime **must** set the [XrSpatialPersistenceStateEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialPersistenceStateEXT) in the [XrSpatialPersistenceDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialPersistenceDataEXT) of this entity to `XR_SPATIAL_PERSISTENCE_STATE_NOT_FOUND_EXT` to indicate to the application that this UUID is no longer present in the storage.
  - The runtime **must** set the `XrSpatialEntityIdEXT` for this entity in the created snapshot to [XR_NULL_SPATIAL_ENTITY_ID_EXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_NULL_SPATIAL_ENTITY_ID_EXT) .
  - The runtime **must** set the [XrSpatialEntityTrackingStateEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialEntityTrackingStateEXT) of that entity to `XR_SPATIAL_ENTITY_TRACKING_STATE_STOPPED_EXT` to indicate to the application that this entity will never be tracked.
- If the runtime was not able to determine if the UUID is present in its storage or not, it **must** not include it in the snapshot.

The application **can** also use [XrSpatialDiscoveryPersistenceUuidFilterEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialDiscoveryPersistenceUuidFilterEXT) in the next chain of [XrSpatialComponentDataQueryConditionEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryConditionEXT) to query for entities of specific UUIDs in existing snapshots. When used with [XrSpatialComponentDataQueryConditionEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryConditionEXT) , if [XrSpatialDiscoveryPersistenceUuidFilterEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialDiscoveryPersistenceUuidFilterEXT) :: `persistedUuids` contains any [XrUuid](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrUuid) that is not in the [XrSpatialSnapshotEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialSnapshotEXT) , the runtime **must** not include an entry for that [XrUuid](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrUuid) in the query result. Also, the order (sequence) of entities in the query result **may** not match the order of UUIDs provided in [XrSpatialDiscoveryPersistenceUuidFilterEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialDiscoveryPersistenceUuidFilterEXT) :: `persistedUuids` . Application **should** include `XR_SPATIAL_COMPONENT_TYPE_PERSISTENCE_EXT` in [XrSpatialComponentDataQueryConditionEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryConditionEXT) :: `componentTypes` and [XrSpatialComponentPersistenceListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialComponentPersistenceListEXT) in the next chain of [XrSpatialComponentDataQueryResultEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryResultEXT) and then check the [XrSpatialPersistenceDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialPersistenceDataEXT) :: `persistUuid` of the each query result index to understand which UUID the current result index corresponds to.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#VUID-XrSpatialDiscoveryPersistenceUuidFilterEXT-extension-notenabled) The `XR_EXT_spatial_persistence` extension **must** be enabled prior to using [XrSpatialDiscoveryPersistenceUuidFilterEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialDiscoveryPersistenceUuidFilterEXT)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#VUID-XrSpatialDiscoveryPersistenceUuidFilterEXT-type-type) `type` **must** be `XR_TYPE_SPATIAL_DISCOVERY_PERSISTENCE_UUID_FILTER_EXT`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#VUID-XrSpatialDiscoveryPersistenceUuidFilterEXT-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#VUID-XrSpatialDiscoveryPersistenceUuidFilterEXT-persistedUuids-parameter) `persistedUuids` **must** be a pointer to an array of `persistedUuidCount` [XrUuid](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrUuid) structures
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#VUID-XrSpatialDiscoveryPersistenceUuidFilterEXT-persistedUuidCount-arraylength) The `persistedUuidCount` parameter **must** be greater than `0`

###### Discover all persisted entities

If the application uses [xrCreateSpatialDiscoverySnapshotAsyncEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrCreateSpatialDiscoverySnapshotAsyncEXT) without [XrSpatialDiscoveryPersistenceUuidFilterEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialDiscoveryPersistenceUuidFilterEXT) and with an [XrSpatialContextEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextEXT) which has been configured with an [XrSpatialPersistenceContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialPersistenceContextEXT) , then the runtime **must** include those entities in the created snapshot that are persisted in the storage represented by [XrSpatialPersistenceContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialPersistenceContextEXT) and satisfy the filters provided in [XrSpatialDiscoverySnapshotCreateInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialDiscoverySnapshotCreateInfoEXT) . For those entities -

- The runtime **must** set the [XrSpatialPersistenceStateEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialPersistenceStateEXT) in the [XrSpatialPersistenceDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialPersistenceDataEXT) of this entity to `XR_SPATIAL_PERSISTENCE_STATE_LOADED_EXT` .
- The runtime **must** include a valid `XrSpatialEntityIdEXT` for this entity in the created snapshot.
- The runtime **must** set the [XrSpatialEntityTrackingStateEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialEntityTrackingStateEXT) of that entity to `XR_SPATIAL_ENTITY_TRACKING_STATE_TRACKING_EXT` if it is actively tracking the entity and has valid data for its components. Otherwise, the runtime **must** set the [XrSpatialEntityTrackingStateEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialEntityTrackingStateEXT) to `XR_SPATIAL_ENTITY_TRACKING_STATE_PAUSED_EXT` .

## New Object Types

- [XrSpatialPersistenceContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialPersistenceContextEXT)

## New Commands

- [xrCreateSpatialPersistenceContextAsyncEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#xrCreateSpatialPersistenceContextAsyncEXT)
- [xrCreateSpatialPersistenceContextCompleteEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#xrCreateSpatialPersistenceContextCompleteEXT)
- [xrDestroySpatialPersistenceContextEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#xrDestroySpatialPersistenceContextEXT)
- [xrEnumerateSpatialPersistenceScopesEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#xrEnumerateSpatialPersistenceScopesEXT)

## New Structures

- [XrCreateSpatialPersistenceContextCompletionEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrCreateSpatialPersistenceContextCompletionEXT)
- [XrSpatialPersistenceContextCreateInfoEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialPersistenceContextCreateInfoEXT)
- [XrSpatialPersistenceDataEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialPersistenceDataEXT)
- Extending [XrSpatialComponentDataQueryResultEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryResultEXT) :

  - [XrSpatialComponentPersistenceListEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialComponentPersistenceListEXT)
- Extending [XrSpatialContextCreateInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialContextCreateInfoEXT) :

  - [XrSpatialContextPersistenceConfigEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialContextPersistenceConfigEXT)
- Extending [XrSpatialDiscoverySnapshotCreateInfoEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialDiscoverySnapshotCreateInfoEXT) , [XrSpatialComponentDataQueryConditionEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentDataQueryConditionEXT) :

  - [XrSpatialDiscoveryPersistenceUuidFilterEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialDiscoveryPersistenceUuidFilterEXT)

## New Enums

- [XrSpatialPersistenceContextResultEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialPersistenceContextResultEXT)
- [XrSpatialPersistenceScopeEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialPersistenceScopeEXT)
- [XrSpatialPersistenceStateEXT](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence#XrSpatialPersistenceStateEXT)

## New Enum Constants

- `XR_EXT_SPATIAL_PERSISTENCE_EXTENSION_NAME`
- `XR_EXT_spatial_persistence_SPEC_VERSION`
- Extending [XrObjectType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrObjectType) :

  - `XR_OBJECT_TYPE_SPATIAL_PERSISTENCE_CONTEXT_EXT`
- Extending [XrResult](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrResult) :

  - `XR_ERROR_SPATIAL_PERSISTENCE_SCOPE_UNSUPPORTED_EXT`
- Extending [XrSpatialComponentTypeEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSpatialComponentTypeEXT) :

  - `XR_SPATIAL_COMPONENT_TYPE_PERSISTENCE_EXT`
- Extending [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) :

  - `XR_TYPE_CREATE_SPATIAL_PERSISTENCE_CONTEXT_COMPLETION_EXT`
  - `XR_TYPE_SPATIAL_COMPONENT_PERSISTENCE_LIST_EXT`
  - `XR_TYPE_SPATIAL_CONTEXT_PERSISTENCE_CONFIG_EXT`
  - `XR_TYPE_SPATIAL_DISCOVERY_PERSISTENCE_UUID_FILTER_EXT`
  - `XR_TYPE_SPATIAL_PERSISTENCE_CONTEXT_CREATE_INFO_EXT`

## Example Code

### Create Persistence Context

    // Check if the required persistence scope supported
    uint32_t scopeCount;
    CHK_XR(xrEnumerateSpatialPersistenceScopesEXT(instance, systemId, 0, &scopeCount, nullptr));
    std::vector<XrSpatialPersistenceScopeEXT> persistenceScopes(scopeCount);
    CHK_XR(xrEnumerateSpatialPersistenceScopesEXT(instance, systemId, scopeCount, &scopeCount, persistenceScopes.data()));

    if (std::find(persistenceScopes.begin(), persistenceScopes.end(), XR_SPATIAL_PERSISTENCE_SCOPE_SYSTEM_MANAGED_EXT) == persistenceScopes.end()) {
      return;
    }

    XrSpatialPersistenceContextEXT persistenceContext{};

    XrSpatialPersistenceContextCreateInfoEXT persistenceContextCreateInfo{XR_TYPE_SPATIAL_PERSISTENCE_CONTEXT_CREATE_INFO_EXT};
    persistenceContextCreateInfo.scope = XR_SPATIAL_PERSISTENCE_SCOPE_SYSTEM_MANAGED_EXT;
    XrFutureEXT createContextFuture;
    CHK_XR(xrCreateSpatialPersistenceContextAsyncEXT(session, &persistenceContextCreateInfo, &createContextFuture));

    waitUntilReady(createContextFuture);

    XrCreateSpatialPersistenceContextCompletionEXT completion{XR_TYPE_CREATE_SPATIAL_PERSISTENCE_CONTEXT_COMPLETION_EXT};
    CHK_XR(xrCreateSpatialPersistenceContextCompleteEXT(session, createContextFuture, &completion));
    if (completion.futureResult != XR_SUCCESS || completion.createResult != XR_SPATIAL_PERSISTENCE_CONTEXT_RESULT_SUCCESS_EXT) {
      return;
    }

    persistenceContext = completion.persistenceContext;

    // ...
    // Connect persistence context to a spatial context and discover persisted entities.
    // ...

    CHK_XR(xrDestroySpatialPersistenceContextEXT(persistenceContext));

### Connect Persistence Context to a Spatial Context

    // Note: Anchor capability is just used as an example here. Persistence can be
    // supported by other capabilities too. xrEnumerateSpatialCapabilityComponentTypesEXT() can
    // be used to check if a certain capability supports persistence.
    if (!isSpatialCapabilitySupported(instance, systemId, XR_SPATIAL_CAPABILITY_ANCHOR_EXT)) {
      return;
    }

    const bool supportsPersistenceComponent = isSpatialComponentSupported(instance, systemId, XR_SPATIAL_CAPABILITY_ANCHOR_EXT, XR_SPATIAL_COMPONENT_TYPE_PERSISTENCE_EXT);

    // Create a spatial spatial context
    XrSpatialContextEXT spatialContext{};
    {

      std::vector<XrSpatialComponentTypeEXT> enabledComponents = {
        XR_SPATIAL_COMPONENT_TYPE_ANCHOR_EXT,
      };

      if (supportsPersistenceComponent) {
        enabledComponents.push_back(XR_SPATIAL_COMPONENT_TYPE_PERSISTENCE_EXT);
      }

      XrSpatialCapabilityConfigurationAnchorEXT anchorConfig{XR_TYPE_SPATIAL_CAPABILITY_CONFIGURATION_ANCHOR_EXT};
      anchorConfig.capability = XR_SPATIAL_CAPABILITY_ANCHOR_EXT;
      anchorConfig.enabledComponentCount = enabledComponents.size();
      anchorConfig.enabledComponents = enabledComponents.data();

      std::array<XrSpatialCapabilityConfigurationBaseHeaderEXT*, 1> capabilityConfigs = {
        reinterpret_cast<XrSpatialCapabilityConfigurationBaseHeaderEXT*>(&anchorConfig),
      };

      XrSpatialContextCreateInfoEXT spatialContextCreateInfo{XR_TYPE_SPATIAL_CONTEXT_CREATE_INFO_EXT};
      spatialContextCreateInfo.capabilityConfigCount = capabilityConfigs.size();
      spatialContextCreateInfo.capabilityConfigs = capabilityConfigs.data();

      XrSpatialContextPersistenceConfigEXT persistenceConfig{XR_TYPE_SPATIAL_CONTEXT_PERSISTENCE_CONFIG_EXT};
      persistenceConfig.persistenceContextCount = 1;
      persistenceConfig.persistenceContexts = &persistenceContext;

      if (supportsPersistenceComponent) {
        spatialContextCreateInfo.next = &persistenceConfig;
      }

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

    // ...
    // Discover persisted anchors.
    // ...

    CHK_XR(xrDestroySpatialContextEXT(spatialContext));

### Discover all persisted entities

    XrFutureEXT future = XR_NULL_FUTURE_EXT;

    // We want to look for entities that have the following components.
    std::vector<XrSpatialComponentTypeEXT> snapshotComponents = {
      XR_SPATIAL_COMPONENT_TYPE_PERSISTENCE_EXT,
    };

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

        std::vector<XrSpatialPersistenceDataEXT> persistenceData(queryResult.entityIdCountOutput);
        XrSpatialComponentPersistenceListEXT persistenceDataList{XR_TYPE_SPATIAL_COMPONENT_PERSISTENCE_LIST_EXT};
        persistenceDataList.persistDataCount = persistenceData.size();
        persistenceDataList.persistData = persistenceData.data();
        queryResult.next = &persistenceDataList;

        CHK_XR(xrQuerySpatialComponentDataEXT(completion.snapshot, &queryCond, &queryResult));

        for (int32_t i = 0; i < queryResult.entityIdCountOutput; ++i) {
          // persistenceData[i].persistUuid is the UUID of the persisted entity whose entity ID is entityIds[i].
          // The persistenceData array is essentially the uuids persisted in the scope that the current
          // XrSpatialPersistenceContextEXT is configured with.
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

### Discover entities with specific UUIDs

    XrFutureEXT future = XR_NULL_FUTURE_EXT;

    // Load up the uuids that the app has stored on its own i.e. the uuids it is interested in.
    std::vector<XrUuid> uuidsStoredByApp = loadPersistedUuids();

    // We want to look for entities that have the following components.
    std::vector<XrSpatialComponentTypeEXT> snapshotComponents = {
      XR_SPATIAL_COMPONENT_TYPE_PERSISTENCE_EXT,
    };

    auto discoverSpatialEntities = [&](XrSpatialContextEXT spatialContext, XrTime time) {
      XrSpatialDiscoveryPersistenceUuidFilterEXT persistenceFilter{XR_TYPE_SPATIAL_DISCOVERY_PERSISTENCE_UUID_FILTER_EXT};
      persistenceFilter.persistedUuidCount = uuidsStoredByApp.size();
      persistenceFilter.persistedUuids = uuidsStoredByApp.data();

      XrSpatialDiscoverySnapshotCreateInfoEXT snapshotCreateInfo{XR_TYPE_SPATIAL_DISCOVERY_SNAPSHOT_CREATE_INFO_EXT};
      snapshotCreateInfo.componentTypeCount = snapshotComponents.size();
      snapshotCreateInfo.componentTypes = snapshotComponents.data();
      snapshotCreateInfo.next = &persistenceFilter;

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

        std::vector<XrSpatialPersistenceDataEXT> persistenceData(queryResult.entityIdCountOutput);
        XrSpatialComponentPersistenceListEXT persistenceDataList{XR_TYPE_SPATIAL_COMPONENT_PERSISTENCE_LIST_EXT};
        persistenceDataList.persistDataCount = persistenceData.size();
        persistenceDataList.persistData = persistenceData.data();
        queryResult.next = &persistenceDataList;

        CHK_XR(xrQuerySpatialComponentDataEXT(completion.snapshot, &queryCond, &queryResult));

        for (int32_t i = 0; i < queryResult.entityIdCountOutput; ++i) {
          if (persistenceData[i].persistState == XR_SPATIAL_PERSISTENCE_STATE_LOADED_EXT) {
            // persistenceData[i].persistUuid, requested by the app, is present in the persistence scope
            // and its corresponding entity ID and state are entityIds[i] & entityStates[i] respectively.
          } else if (persistenceData[i].persistState == XR_SPATIAL_PERSISTENCE_STATE_NOT_FOUND_EXT) {
            // persistenceData[i].persistUuid, requested by the app, is NOT present in the persistence scope
            // and its corresponding entity ID (entityIds[i]) would be XR_NULL_SPATIAL_ENTITY_ID_EXT
            // and tracking state (entityStates[i]) would be XR_SPATIAL_ENTITY_TRACKING_STATE_STOPPED_EXT.
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

## Issues

## Version History

- Revision 1, 2024-08-29 (Nihav Jain, Google)

  - Initial extension description