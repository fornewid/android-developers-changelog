---
title: https://developer.android.com/develop/xr/openxr/extensions/XR_KHR_extended_struct_name_lengths
url: https://developer.android.com/develop/xr/openxr/extensions/XR_KHR_extended_struct_name_lengths
source: md.txt
---

### XR_KHR_extended_struct_name_lengths

**Name String**

`XR_KHR_extended_struct_name_lengths`

**Extension Type**

Instance extension

**Registered Extension Number**

149

**Revision**

2

**Ratification Status**

Ratified

**Extension and Version Dependencies**

[OpenXR 1.0](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#versions-1.0)

**Last Modified Date**

2025-12-04

**IP Status**

No known IP claims.

**Contributors**

Matthew Langille, Meta Platforms  

Andreas Selvik, Meta Platforms  

Rylie Pavlik, Collabora, Ltd.

## Overview

This extension extends the maximum struct name sizes and provides a new function to access these new extended names.

[xrStructureTypeToString2KHR](https://developer.android.com/develop/xr/openxr/extensions/XR_KHR_extended_struct_name_lengths#xrStructureTypeToString2KHR) is provided to allow retrieving the string names of structure type enumerants with lengths that exceed the original limit of 63 bytes (64 bytes including the null terminator). [xrStructureTypeToString2KHR](https://developer.android.com/develop/xr/openxr/extensions/XR_KHR_extended_struct_name_lengths#xrStructureTypeToString2KHR) returns name strings for structure type enumerants up to 255 bytes in length (256 bytes including the null terminator). An application **can** use [xrStructureTypeToString2KHR](https://developer.android.com/develop/xr/openxr/extensions/XR_KHR_extended_struct_name_lengths#xrStructureTypeToString2KHR) as a drop-in replacement for [xrStructureTypeToString](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrStructureTypeToString) , as it works with all structure type enumerants, regardless of string name length.

## Retrieving Structure Type Enumerant Strings

If the original [xrStructureTypeToString](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrStructureTypeToString) is used to retrieve string names for structure type enumerants with name lengths in excess of 63 bytes, its behavior is clarified as follows. [xrStructureTypeToString](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrStructureTypeToString) **must** populate the buffer with the correct name, except that the string **must** be truncated at a codepoint boundary to fit within the available buffer. That is, the returned string **must** always be valid UTF-8.

The [xrStructureTypeToString2KHR](https://developer.android.com/develop/xr/openxr/extensions/XR_KHR_extended_struct_name_lengths#xrStructureTypeToString2KHR) function is defined as:

    XrResult xrStructureTypeToString2KHR(
        XrInstance                                  instance,
        XrStructureType                             value,
        char                                        buffer[XR_MAX_STRUCTURE_NAME_SIZE_EXTENDED_KHR]);

### Parameter Descriptions

- `instance` is the handle of the instance to ask for the string.
- `value` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) value to turn into a string.
- `buffer` is the buffer that will be used to return the string in.

Returns the name of the provided [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) value by copying a valid null-terminated UTF-8 string into `buffer` .

In all cases the returned string **must** be one of:

### Structure Type String Output Values

- The literal string defined for the provided numeric value in the core specification or extension. (e.g. the value of `XR_TYPE_INSTANCE_CREATE_INFO` results in the string `XR_TYPE_INSTANCE_CREATE_INFO` )
- `XR_UNKNOWN_STRUCTURE_TYPE_` concatenated with the structure type number expressed as a decimal number.

For structure type enumerants whose names fit within the original size limit of 63 bytes, [xrStructureTypeToString2KHR](https://developer.android.com/develop/xr/openxr/extensions/XR_KHR_extended_struct_name_lengths#xrStructureTypeToString2KHR) **must** return the same resultant string as [xrStructureTypeToString](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrStructureTypeToString) , up to the null terminator.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_KHR_extended_struct_name_lengths#VUID-xrStructureTypeToString2KHR-extension-notenabled) The `XR_KHR_extended_struct_name_lengths` extension **must** be enabled prior to calling [xrStructureTypeToString2KHR](https://developer.android.com/develop/xr/openxr/extensions/XR_KHR_extended_struct_name_lengths#xrStructureTypeToString2KHR)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_KHR_extended_struct_name_lengths#VUID-xrStructureTypeToString2KHR-instance-parameter) `instance` **must** be a valid [XrInstance](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrInstance) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_KHR_extended_struct_name_lengths#VUID-xrStructureTypeToString2KHR-value-parameter) `value` **must** be a valid [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) value
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_KHR_extended_struct_name_lengths#VUID-xrStructureTypeToString2KHR-buffer-parameter) `buffer` **must** be a character array of length `XR_MAX_STRUCTURE_NAME_SIZE_EXTENDED_KHR`

### Return Codes

[Success](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`

[Failure](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_HANDLE_INVALID`
- `XR_ERROR_INSTANCE_LOST`
- `XR_ERROR_RUNTIME_FAILURE`
- `XR_ERROR_VALIDATION_FAILURE`

The `XR_MAX_STRUCTURE_NAME_SIZE_EXTENDED_KHR` enumerant defines the size of the buffer passed to [xrStructureTypeToString2KHR](https://developer.android.com/develop/xr/openxr/extensions/XR_KHR_extended_struct_name_lengths#xrStructureTypeToString2KHR) .

    #define XR_MAX_STRUCTURE_NAME_SIZE_EXTENDED_KHR 256

## New Commands

- [xrStructureTypeToString2KHR](https://developer.android.com/develop/xr/openxr/extensions/XR_KHR_extended_struct_name_lengths#xrStructureTypeToString2KHR)

## New Enum Constants

- `XR_KHR_EXTENDED_STRUCT_NAME_LENGTHS_EXTENSION_NAME`
- `XR_KHR_extended_struct_name_lengths_SPEC_VERSION`
- `XR_MAX_STRUCTURE_NAME_SIZE_EXTENDED_KHR`

**Version History**

- Revision 1, 2024-02-29 (Matthew Langille)

  - Initial extension description
- Revision 2, 2025-12-04 (Kenny Vercaemer)

  - Fix structure name length specification