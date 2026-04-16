---
title: https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_enumerate_system_extension_properties
url: https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_enumerate_system_extension_properties
source: md.txt
---

### XR_ANDROID_enumerate_system_extension_properties

**Name String**

`XR_ANDROID_enumerate_system_extension_properties`

**Extension Type**

Instance extension

**Registered Extension Number**

725

**Revision**

1

**Ratification Status**

Not ratified

**Extension and Version Dependencies**

[OpenXR 1.0](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#versions-1.0)

**Last Modified Date**

2026-02-11

**IP Status**

No known IP claims.

**Contributors**

Spencer Quin, Google  

Nihav Jain, Google  

Kenny Vercaemer, Google

## Overview

This extension allows applications to determine which extensions are supported by the current system configuration. Even if an extension is supported by the runtime, it **may** not be supported by the present system hardware.

The [XrSystemExtensionPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_enumerate_system_extension_properties#XrSystemExtensionPropertiesANDROID) structure is defined as:

    typedef struct XrSystemExtensionPropertiesANDROID {
        XrStructureType          type;
        void*                    next;
        XrExtensionProperties    properties;
        XrBool32                 isSupported;
    } XrSystemExtensionPropertiesANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `properties` is the [XrExtensionProperties](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrExtensionProperties) with the extension name.
- `isSupported` is a boolean indicating whether the extension is currently supported by the system.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_enumerate_system_extension_properties#VUID-XrSystemExtensionPropertiesANDROID-extension-notenabled) The `XR_ANDROID_enumerate_system_extension_properties` extension **must** be enabled prior to using [XrSystemExtensionPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_enumerate_system_extension_properties#XrSystemExtensionPropertiesANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_enumerate_system_extension_properties#VUID-XrSystemExtensionPropertiesANDROID-type-type) `type` **must** be `XR_TYPE_SYSTEM_EXTENSION_PROPERTIES_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_enumerate_system_extension_properties#VUID-XrSystemExtensionPropertiesANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)

The [XrEventDataSystemPropertiesChangedANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_enumerate_system_extension_properties#XrEventDataSystemPropertiesChangedANDROID) structure is defined as:

    typedef struct XrEventDataSystemPropertiesChangedANDROID {
        XrStructureType    type;
        const void*        next;
    } XrEventDataSystemPropertiesChangedANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.

The runtime **must** queue this event when the system extension properties have changed. For example when new peripherals are connected enabling new functionality.

All calls to [xrEnumerateSystemExtensionPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_enumerate_system_extension_properties#xrEnumerateSystemExtensionPropertiesANDROID) **must** return the same values until a new [XrEventDataSystemPropertiesChangedANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_enumerate_system_extension_properties#XrEventDataSystemPropertiesChangedANDROID) event is queued.

When an application receives this event, it **should** call [xrEnumerateSystemExtensionPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_enumerate_system_extension_properties#xrEnumerateSystemExtensionPropertiesANDROID) again to determine the latest system extension properties, possibly creating or destroying trackers associated with those extensions as needed.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_enumerate_system_extension_properties#VUID-XrEventDataSystemPropertiesChangedANDROID-extension-notenabled) The `XR_ANDROID_enumerate_system_extension_properties` extension **must** be enabled prior to using [XrEventDataSystemPropertiesChangedANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_enumerate_system_extension_properties#XrEventDataSystemPropertiesChangedANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_enumerate_system_extension_properties#VUID-XrEventDataSystemPropertiesChangedANDROID-type-type) `type` **must** be `XR_TYPE_EVENT_DATA_SYSTEM_PROPERTIES_CHANGED_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_enumerate_system_extension_properties#VUID-XrEventDataSystemPropertiesChangedANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)

The [xrEnumerateSystemExtensionPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_enumerate_system_extension_properties#xrEnumerateSystemExtensionPropertiesANDROID) function is defined as:

    XrResult xrEnumerateSystemExtensionPropertiesANDROID(
        XrInstance                                  instance,
        XrSystemId                                  systemId,
        uint32_t                                    propertyCapacityInput,
        uint32_t*                                   propertyCountOutput,
        XrSystemExtensionPropertiesANDROID*         properties);

### Parameter Descriptions

- `instance` is a valid [XrInstance](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrInstance) .
- `systemId` is a valid sliink:XrSystemId of the system to retrieve the extension properties for.
- `propertyCapacityInput` is the capacity of the `properties` array, or 0 to indicate a request to retrieve the required capacity.
- `propertyCountOutput` is the number of requested extension properties.
- `properties` is an array of [XrSystemExtensionPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_enumerate_system_extension_properties#XrSystemExtensionPropertiesANDROID) structures. It **can** be `NULL` if `propertyCapacityInput` is 0.
- See the [Buffer Size Parameters](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-buffer-size-parameters) section for a detailed description of retrieving the required `properties` size.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_enumerate_system_extension_properties#VUID-xrEnumerateSystemExtensionPropertiesANDROID-extension-notenabled) The `XR_ANDROID_enumerate_system_extension_properties` extension **must** be enabled prior to calling [xrEnumerateSystemExtensionPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_enumerate_system_extension_properties#xrEnumerateSystemExtensionPropertiesANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_enumerate_system_extension_properties#VUID-xrEnumerateSystemExtensionPropertiesANDROID-instance-parameter) `instance` **must** be a valid [XrInstance](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrInstance) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_enumerate_system_extension_properties#VUID-xrEnumerateSystemExtensionPropertiesANDROID-propertyCountOutput-parameter) `propertyCountOutput` **must** be a pointer to a `uint32_t` value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_enumerate_system_extension_properties#VUID-xrEnumerateSystemExtensionPropertiesANDROID-properties-parameter) If `propertyCapacityInput` is not `0` , `properties` **must** be a pointer to an array of `propertyCapacityInput` [XrSystemExtensionPropertiesANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_enumerate_system_extension_properties#XrSystemExtensionPropertiesANDROID) structures

### Return Codes

[Success](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`

[Failure](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_HANDLE_INVALID`
- `XR_ERROR_INSTANCE_LOST`
- `XR_ERROR_RUNTIME_FAILURE`
- `XR_ERROR_SYSTEM_INVALID`
- `XR_ERROR_VALIDATION_FAILURE`

## Example

    XrInstance instance; // XrInstance previously created

    XrSystemId systemId; // XrSystemId from a previously created instance

    PFN_xrEnumerateSystemExtensionPropertiesANDROID xrEnumerateSystemExtensionPropertiesANDROID;

    // Poll events for recommended resolution changes.
    XrEventDataBuffer event = {XR_TYPE_EVENT_DATA_BUFFER};
    XrResult result = xrPollEvent(instance, &event);

    if (result == XR_SUCCESS) {
        switch (event.type) {
            case XR_TYPE_EVENT_DATA_SYSTEM_PROPERTIES_CHANGED_ANDROID:
                // It's possible that the system was lost and a new id will be returned
                XrSystemId newSystemId;
                XrSystemGetInfo getInfo = {XR_TYPE_SYSTEM_GET_INFO};
                getInfo.formFactor = XR_FORM_FACTOR_HEAD_MOUNTED_DISPLAY;
                if(XR_SUCCESS == xrGetSystem(instance, &getInfo, &newSystemId)) {
                    if(systemId != newSystemId) {
                        //Do things like recreate the session
                        systemId = newSystemId;
                    }
                }

                // Enumerate the extensions to see which ones are now supported based on hardware changes
                uint32_t extensionsCount;
                xrEnumerateSystemExtensionPropertiesANDROID(instance, systemId, 0, &extensionsCount, NULL);

                std::vector<XrSystemExtensionPropertiesANDROID> properties(extensionsCount,
                    {.type = XR_TYPE_SYSTEM_EXTENSION_PROPERTIES_ANDROID});

                XrResult result = xrEnumerateSystemExtensionPropertiesANDROID(
                    instance,
                    systemId,
                    extensionsCount,
                    &extensionsCount,
                    properties.data()
                );

                // Do something based on which extensions are now supported by the system
                break;
        }
    }

    PFN_xrEnumerateSystemExtensionPropertiesANDROID xrEnumerateSystemExtensionPropertiesANDROID;

    XrInstance instance;
    XrInstanceCreateInfo createInfo = {XR_TYPE_INSTANCE_CREATE_INFO};
    // Initialize the createInfo with appropriate values for the application
    CHK_XR(xrCreateInstance(&createInfo, &instance));

    // Get the systemId for the system.
    XrSystemId systemId;
    XrSystemGetInfo getInfo = {XR_TYPE_SYSTEM_GET_INFO};
    getInfo.formFactor = XR_FORM_FACTOR_HEAD_MOUNTED_DISPLAY;
    CHK_XR(xrGetSystem(instance, &getInfo, &systemId));

    // Enumerate the system extension properties.
    uint32_t extensionsCount;
    xrEnumerateSystemExtensionPropertiesANDROID(instance, systemId, 0, &extensionsCount, NULL);

    std::vector<XrSystemExtensionPropertiesANDROID> properties(extensionsCount,
        {.type = XR_TYPE_SYSTEM_EXTENSION_PROPERTIES_ANDROID});

    XrResult result = xrEnumerateSystemExtensionPropertiesANDROID(
        instance,
        systemId,
        extensionsCount,
        &extensionsCount,
        properties.data()
    );

## Issues

## Version History

- Revision 1, 2026-03-17 (Kenny Vercaemer)

  - Initial extension version.