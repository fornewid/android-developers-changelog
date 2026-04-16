---
title: https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth
url: https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth
source: md.txt
---

### XR_ANDROID_google_cloud_auth

**Name String**

`XR_ANDROID_google_cloud_auth`

**Extension Type**

Instance extension

**Registered Extension Number**

788

**Revision**

1

**Ratification Status**

Not ratified

**Extension and Version Dependencies**

`XR_EXT_future`

**Last Modified Date**

2025-12-18

**IP Status**

No known IP claims.

**Contributors**

John Ullman, Google  

Ben King, Google  

Nihav Jain, Google  

Jared Finder, Google

## Overview

This extension enables the use of Google Cloud-based extensions by allowing the application to provide auth credentials for Google Cloud APIs. The developer **must** use the Google Cloud Console ( <https://console.cloud.google.com/> ) to create a Google Cloud project for the application. This extension requires the extension `XR_EXT_future` .

During development, the application **can** debug issues with their Google Cloud setup using the extension `XR_EXT_debug_utils` . If the application has a Debug Messenger, and a potentially actionable error occurs in the runtime when sending a request to Google Cloud on behalf of the application, the runtime invokes the messenger's callback with an error message. In this case, the developer **should** consult the error message and all available documentation, and then ensure that the application and Google Cloud project are properly setup to use Google Cloud APIs. The runtime **must** use message type `XR_DEBUG_UTILS_MESSAGE_TYPE_GENERAL_BIT_EXT` , severity `XR_DEBUG_UTILS_MESSAGE_SEVERITY_ERROR_BIT_EXT` , and messageId "GoogleCloudError".

## Authentication

The [XrGoogleCloudAuthInfoBaseHeaderANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#XrGoogleCloudAuthInfoBaseHeaderANDROID) structure is defined as:

    typedef struct XrGoogleCloudAuthInfoBaseHeaderANDROID {
        XrStructureType    type;
        const void*        next;
    } XrGoogleCloudAuthInfoBaseHeaderANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.

This structure is not directly used in the API but is extended by other structures that **can** be used with [xrSetGoogleCloudAuthAsyncANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#xrSetGoogleCloudAuthAsyncANDROID) to provide authentication credentials.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#VUID-XrGoogleCloudAuthInfoBaseHeaderANDROID-extension-notenabled) The `XR_ANDROID_google_cloud_auth` extension **must** be enabled prior to using [XrGoogleCloudAuthInfoBaseHeaderANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#XrGoogleCloudAuthInfoBaseHeaderANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#VUID-XrGoogleCloudAuthInfoBaseHeaderANDROID-type-type) `type` **must** be one of the following XrStructureType values: `XR_TYPE_GOOGLE_CLOUD_AUTH_INFO_API_KEY_ANDROID` , `XR_TYPE_GOOGLE_CLOUD_AUTH_INFO_KEYLESS_ANDROID` , `XR_TYPE_GOOGLE_CLOUD_AUTH_INFO_TOKEN_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#VUID-XrGoogleCloudAuthInfoBaseHeaderANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains) . See also: [XrGoogleCloudAuthErrorResultANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#XrGoogleCloudAuthErrorResultANDROID)

The [XrGoogleCloudAuthInfoApiKeyANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#XrGoogleCloudAuthInfoApiKeyANDROID) structure is defined as:

    typedef struct XrGoogleCloudAuthInfoApiKeyANDROID {
        XrStructureType    type;
        const void*        next;
        const char*        apiKey;
    } XrGoogleCloudAuthInfoApiKeyANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `apiKey` is a pointer to a string representing the API key.

When this structure is passed to [xrSetGoogleCloudAuthAsyncANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#xrSetGoogleCloudAuthAsyncANDROID) , the `apiKey` member **must** be a nonempty ASCII string with no spaces or control characters, otherwise the runtime **must** return `XR_ERROR_VALIDATION_FAILURE` .

`apiKey` **must** further satisfy the following conditions:

- It **must** be a valid API Key generated for your Google Cloud project.
- Your Google Cloud project **must** enable the relevant Google Cloud APIs (specified by the depending extensions).
- If the API Key has restrictions, the restrictions **must** allow the relevant Google Cloud APIs and your application.

Otherwise, the call to [xrSetGoogleCloudAuthAsyncANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#xrSetGoogleCloudAuthAsyncANDROID) will succeed but all calls to functions that depend on cloud authorization will act as documented for cloud failures in the extension that defines those functions. If a function **can** report a failure and the application chains [XrGoogleCloudAuthErrorResultANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#XrGoogleCloudAuthErrorResultANDROID) to the output parameter of that function, the runtime **must** set [XrGoogleCloudAuthErrorResultANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#XrGoogleCloudAuthErrorResultANDROID) :: `error` to `XR_GOOGLE_CLOUD_AUTH_ERROR_ANDROID` to indicate this error.

The asynchronous operation will complete with `XR_SUCCESS` once the API key is validated for formatting and stored by the runtime.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#VUID-XrGoogleCloudAuthInfoApiKeyANDROID-extension-notenabled) The `XR_ANDROID_google_cloud_auth` extension **must** be enabled prior to using [XrGoogleCloudAuthInfoApiKeyANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#XrGoogleCloudAuthInfoApiKeyANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#VUID-XrGoogleCloudAuthInfoApiKeyANDROID-type-type) `type` **must** be `XR_TYPE_GOOGLE_CLOUD_AUTH_INFO_API_KEY_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#VUID-XrGoogleCloudAuthInfoApiKeyANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#VUID-XrGoogleCloudAuthInfoApiKeyANDROID-apiKey-parameter) `apiKey` **must** be a null-terminated UTF-8 string

The [XrGoogleCloudAuthInfoTokenANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#XrGoogleCloudAuthInfoTokenANDROID) structure is defined as:

    typedef struct XrGoogleCloudAuthInfoTokenANDROID {
        XrStructureType    type;
        const void*        next;
        const char*        authToken;
    } XrGoogleCloudAuthInfoTokenANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `authToken` is a pointer to a string representing the auth token.

When this structure is passed to [xrSetGoogleCloudAuthAsyncANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#xrSetGoogleCloudAuthAsyncANDROID) , the `authToken` member **must** be a nonempty ASCII string with no spaces or control characters, otherwise the runtime **must** return `XR_ERROR_VALIDATION_FAILURE` . `authToken` **must** further satisfy the following conditions:

- It **must** be a valid and unexpired credential generated for your Google Cloud project.
- Your Google Cloud project **must** enable the relevant Google Cloud APIs (specified by the depending extensions).
- The credential **must** be one of:

  - An OAuth2 access token with the relevant scopes, generated by signing into a Google account with your application, OR
  - A Signed JWT token with the relevant claims, generated by a Service Account from your Google Cloud project.

The requirements in each case are specified by the depending extensions. Otherwise, the call to [xrSetGoogleCloudAuthAsyncANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#xrSetGoogleCloudAuthAsyncANDROID) will succeed but all calls to functions that depend on cloud authorization will act as documented for cloud failures in the extension that defines those functions. If a function **can** report a failure and the application chains [XrGoogleCloudAuthErrorResultANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#XrGoogleCloudAuthErrorResultANDROID) to the output parameter of that function, the runtime **must** set [XrGoogleCloudAuthErrorResultANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#XrGoogleCloudAuthErrorResultANDROID) :: `error` to `XR_GOOGLE_CLOUD_AUTH_ERROR_ANDROID` to indicate this error.

The application **must** proactively pass in a new token via [xrSetGoogleCloudAuthAsyncANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#xrSetGoogleCloudAuthAsyncANDROID) before the old token expires. The runtime **must** use the latest token passed in by the application when starting a new network request.

The asynchronous operation will complete with `XR_SUCCESS` once the token is validated for formatting and stored by the runtime.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#VUID-XrGoogleCloudAuthInfoTokenANDROID-extension-notenabled) The `XR_ANDROID_google_cloud_auth` extension **must** be enabled prior to using [XrGoogleCloudAuthInfoTokenANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#XrGoogleCloudAuthInfoTokenANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#VUID-XrGoogleCloudAuthInfoTokenANDROID-type-type) `type` **must** be `XR_TYPE_GOOGLE_CLOUD_AUTH_INFO_TOKEN_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#VUID-XrGoogleCloudAuthInfoTokenANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#VUID-XrGoogleCloudAuthInfoTokenANDROID-authToken-parameter) `authToken` **must** be a null-terminated UTF-8 string

The [XrGoogleCloudAuthInfoKeylessANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#XrGoogleCloudAuthInfoKeylessANDROID) structure is defined as:

    typedef struct XrGoogleCloudAuthInfoKeylessANDROID {
        XrStructureType    type;
        const void*        next;
    } XrGoogleCloudAuthInfoKeylessANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.

When this structure is passed to [xrSetGoogleCloudAuthAsyncANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#xrSetGoogleCloudAuthAsyncANDROID) , the runtime **may** generate credentials dynamically (e.g. on Android, the runtime communicates with Google Play Services from the application process). If Keyless Auth is not properly setup, the runtime **may** return `XR_ERROR_KEYLESS_AUTH_NOT_SETUP_ANDROID` synchronously.

The asynchronous operation will perform the necessary network requests to fetch credentials. The result of this operation will be returned in the [XrFutureCompletionEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrFutureCompletionEXT) :: `futureResult` from [xrSetGoogleCloudAuthCompleteANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#xrSetGoogleCloudAuthCompleteANDROID) . If the future result is `XR_SUCCESS` , Keyless Auth credentials were successfully applied. If the future result is `XR_ERROR_KEYLESS_AUTH_FAILED_ANDROID` , the application **may** try again later.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#VUID-XrGoogleCloudAuthInfoKeylessANDROID-extension-notenabled) The `XR_ANDROID_google_cloud_auth` extension **must** be enabled prior to using [XrGoogleCloudAuthInfoKeylessANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#XrGoogleCloudAuthInfoKeylessANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#VUID-XrGoogleCloudAuthInfoKeylessANDROID-type-type) `type` **must** be `XR_TYPE_GOOGLE_CLOUD_AUTH_INFO_KEYLESS_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#VUID-XrGoogleCloudAuthInfoKeylessANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)

The [xrSetGoogleCloudAuthAsyncANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#xrSetGoogleCloudAuthAsyncANDROID) function is defined as:

    XrResult xrSetGoogleCloudAuthAsyncANDROID(
        XrSession                                   session,
        const XrGoogleCloudAuthInfoBaseHeaderANDROID* authInfo,
        XrFutureEXT*                                future);

### Parameter Descriptions

- `session` is the [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) that will use the credentials.
- `authInfo` is a pointer to a struct specifying the authentication method and parameters, with its [XrGoogleCloudAuthInfoBaseHeaderANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#XrGoogleCloudAuthInfoBaseHeaderANDROID) :: `type` field indicating the specific struct.
- `future` is a pointer to an `XrFutureEXT` handle in which the created future is returned, or [XR_NULL_HANDLE](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_NULL_HANDLE) if the function did not return `XR_SUCCESS` .

Set the credentials used to authenticate with Google Cloud. This operation is asynchronous. Call [xrPollFutureEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#xrPollFutureEXT) to check the ready state on the future. Once the future is in the ready state, call [xrSetGoogleCloudAuthCompleteANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#xrSetGoogleCloudAuthCompleteANDROID) to retrieve the result.

The `authInfo` parameter **must** be a pointer to a struct whose [XrGoogleCloudAuthInfoBaseHeaderANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#XrGoogleCloudAuthInfoBaseHeaderANDROID) :: `type` member identifies the authentication method to be used, and which extends [XrGoogleCloudAuthInfoBaseHeaderANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#XrGoogleCloudAuthInfoBaseHeaderANDROID) (e.g. [XrGoogleCloudAuthInfoApiKeyANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#XrGoogleCloudAuthInfoApiKeyANDROID) ).

The specific requirements, behaviors, and error conditions (both synchronous and asynchronous) for each authentication method are described in the documentation for their respective data structs.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#VUID-xrSetGoogleCloudAuthAsyncANDROID-extension-notenabled) The `XR_ANDROID_google_cloud_auth` extension **must** be enabled prior to calling [xrSetGoogleCloudAuthAsyncANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#xrSetGoogleCloudAuthAsyncANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#VUID-xrSetGoogleCloudAuthAsyncANDROID-session-parameter) `session` **must** be a valid [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#VUID-xrSetGoogleCloudAuthAsyncANDROID-authInfo-parameter) `authInfo` **must** be a pointer to a valid [XrGoogleCloudAuthInfoBaseHeaderANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#XrGoogleCloudAuthInfoBaseHeaderANDROID) -based structure. See also: [XrGoogleCloudAuthInfoApiKeyANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#XrGoogleCloudAuthInfoApiKeyANDROID) , [XrGoogleCloudAuthInfoKeylessANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#XrGoogleCloudAuthInfoKeylessANDROID) , [XrGoogleCloudAuthInfoTokenANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#XrGoogleCloudAuthInfoTokenANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#VUID-xrSetGoogleCloudAuthAsyncANDROID-future-parameter) `future` **must** be a pointer to an `XrFutureEXT` value

### Return Codes

[Success](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS`
- `XR_SESSION_LOSS_PENDING`

[Failure](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_FUNCTION_UNSUPPORTED`
- `XR_ERROR_HANDLE_INVALID`
- `XR_ERROR_INSTANCE_LOST`
- `XR_ERROR_KEYLESS_AUTH_NOT_SETUP_ANDROID`
- `XR_ERROR_RUNTIME_FAILURE`
- `XR_ERROR_SESSION_LOST`
- `XR_ERROR_VALIDATION_FAILURE`

The [xrSetGoogleCloudAuthCompleteANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#xrSetGoogleCloudAuthCompleteANDROID) function is defined as:

    XrResult xrSetGoogleCloudAuthCompleteANDROID(
        XrSession                                   session,
        XrFutureEXT                                 future,
        XrFutureCompletionEXT*                      completion);

### Parameter Descriptions

- `session` is the [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) used to start the operation.
- `future` is the `XrFutureEXT` to complete.
- `completion` is a pointer to an [XrFutureCompletionEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrFutureCompletionEXT) filled in by the runtime.

### Future Return Codes

[XrFutureCompletionEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrFutureCompletionEXT) :: `futureResult` values:

[Success](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-successcodes)

- `XR_SUCCESS` : Credentials were successfully applied.

[Failure](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-errorcodes)

- `XR_ERROR_KEYLESS_AUTH_FAILED_ANDROID` : Keyless Auth failed. The application **can** try again later. The application or developer **may** also check certain preconditions for success (e.g. on Android, the device **must** have an up-to-date installation of Google Play Services and these services **must** be functioning properly).

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#VUID-xrSetGoogleCloudAuthCompleteANDROID-extension-notenabled) The `XR_ANDROID_google_cloud_auth` extension **must** be enabled prior to calling [xrSetGoogleCloudAuthCompleteANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#xrSetGoogleCloudAuthCompleteANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#VUID-xrSetGoogleCloudAuthCompleteANDROID-session-parameter) `session` **must** be a valid [XrSession](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrSession) handle
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#VUID-xrSetGoogleCloudAuthCompleteANDROID-completion-parameter) `completion` **must** be a pointer to an [XrFutureCompletionEXT](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrFutureCompletionEXT) structure

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
- `XR_ERROR_RUNTIME_FAILURE`
- `XR_ERROR_SESSION_LOST`
- `XR_ERROR_VALIDATION_FAILURE`

## Google Cloud Auth Errors

The [XrGoogleCloudAuthErrorANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#XrGoogleCloudAuthErrorANDROID) enumeration is defined as:

    typedef enum XrGoogleCloudAuthErrorANDROID {
        XR_GOOGLE_CLOUD_AUTH_ERROR_NONE_ANDROID = 0,
        XR_GOOGLE_CLOUD_AUTH_ERROR_QUOTA_EXCEEDED_ANDROID = -1,
        XR_GOOGLE_CLOUD_AUTH_ERROR_UNREACHABLE_ANDROID = -2,
        XR_GOOGLE_CLOUD_AUTH_ERROR_ANDROID = -3,
        XR_GOOGLE_CLOUD_AUTH_ERROR_MAX_ENUM_ANDROID = 0x7FFFFFFF
    } XrGoogleCloudAuthErrorANDROID;

The enumerants have the following values:

Enum Description

`XR_GOOGLE_CLOUD_AUTH_ERROR_NONE_ANDROID`

No error occurred when invoking a Google Cloud API.

`XR_GOOGLE_CLOUD_AUTH_ERROR_QUOTA_EXCEEDED_ANDROID`

Quota exceeded when invoking a Google Cloud API.

`XR_GOOGLE_CLOUD_AUTH_ERROR_UNREACHABLE_ANDROID`

Failed to reach a Google Cloud API, possibly due to network connectivity issues or server availability.

`XR_GOOGLE_CLOUD_AUTH_ERROR_ANDROID`

An auth error occurred when invoking a Google Cloud API.

The [XrGoogleCloudAuthErrorResultANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#XrGoogleCloudAuthErrorResultANDROID) structure is defined as:

    typedef struct XrGoogleCloudAuthErrorResultANDROID {
        XrStructureType                  type;
        void*                            next;
        XrGoogleCloudAuthErrorANDROID    error;
    } XrGoogleCloudAuthErrorResultANDROID;

### Member Descriptions

- `type` is the [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) of this structure.
- `next` is `NULL` or a pointer to the next structure in a structure chain.
- `error` is the [XrGoogleCloudAuthErrorANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#XrGoogleCloudAuthErrorANDROID) detailing the cause of the error of an operation accessing Google Cloud.

If an operation fails due to Google Cloud Authentication, this struct **may** be chained to the operational result struct to provide more information about the error.

### Valid Usage (Implicit)

- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#VUID-XrGoogleCloudAuthErrorResultANDROID-extension-notenabled) The `XR_ANDROID_google_cloud_auth` extension **must** be enabled prior to using [XrGoogleCloudAuthErrorResultANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#XrGoogleCloudAuthErrorResultANDROID)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#VUID-XrGoogleCloudAuthErrorResultANDROID-type-type) `type` **must** be `XR_TYPE_GOOGLE_CLOUD_AUTH_ERROR_RESULT_ANDROID`
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#VUID-XrGoogleCloudAuthErrorResultANDROID-next-next) `next` **must** be `NULL` or a valid pointer to the [next structure in a structure chain](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#valid-usage-for-structure-pointer-chains)
- [](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#VUID-XrGoogleCloudAuthErrorResultANDROID-error-parameter) `error` **must** be a valid [XrGoogleCloudAuthErrorANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#XrGoogleCloudAuthErrorANDROID) value

## Example code

    XrSession session; // previously initialized
    XrInstance instance; // previously initialized
    XrFutureEXT future = XR_NULL_HANDLE;

    // The function pointers are previously initialized using
    // xrGetInstanceProcAddr.
    PFN_xrPollFutureEXT xrPollFutureEXT; // previously initialized
    PFN_xrSetGoogleCloudAuthAsyncANDROID xrSetGoogleCloudAuthAsyncANDROID; // previously initialized
    PFN_xrSetGoogleCloudAuthCompleteANDROID xrSetGoogleCloudAuthCompleteANDROID; // previously initialized

    auto waitUntilReady = [&](XrFutureEXT future) {
      XrFuturePollInfoEXT pollInfo{XR_TYPE_FUTURE_POLL_INFO_EXT};
      XrFuturePollResultEXT pollResult{XR_TYPE_FUTURE_POLL_RESULT_EXT};
      pollInfo.future = future;
      do {
        // sleep(1);
        xrPollFutureEXT(instance, &pollInfo, &pollResult);
      } while (pollResult.state != XR_FUTURE_STATE_READY_EXT);
    };

    // Set Google Cloud auth via API key.
    XrGoogleCloudAuthInfoApiKeyANDROID authApiKey{XR_TYPE_GOOGLE_CLOUD_AUTH_INFO_API_KEY_ANDROID};
    authApiKey.apiKey = "MYAPIKEY";
    XrResult result = xrSetGoogleCloudAuthAsyncANDROID(
        session, reinterpret_cast<XrGoogleCloudAuthInfoBaseHeaderANDROID*>(&authApiKey), &future);

    // Or, set Google Cloud auth via auth token:
    XrGoogleCloudAuthInfoTokenANDROID authToken{XR_TYPE_GOOGLE_CLOUD_AUTH_INFO_TOKEN_ANDROID};
    authToken.authToken = "MYAUTHTOKEN";
    result = xrSetGoogleCloudAuthAsyncANDROID(
        session, reinterpret_cast<XrGoogleCloudAuthInfoBaseHeaderANDROID*>(&authToken), &future);

    // Or, set Google Cloud auth via keyless auth:
    XrGoogleCloudAuthInfoKeylessANDROID authKeyless{XR_TYPE_GOOGLE_CLOUD_AUTH_INFO_KEYLESS_ANDROID};
    result = xrSetGoogleCloudAuthAsyncANDROID(
        session, reinterpret_cast<XrGoogleCloudAuthInfoBaseHeaderANDROID*>(&authKeyless),
        &future);

    // Check the result of the auth setup.
    if (result == XR_ERROR_VALIDATION_FAILURE) {
      // The credentials were invalid.
    } else if (result == XR_ERROR_KEYLESS_AUTH_NOT_SETUP_ANDROID) {
      // Keyless auth was not properly setup.
    } else if (result == XR_SUCCESS) {
      waitUntilReady(future);
      XrFutureCompletionEXT completion{XR_TYPE_FUTURE_COMPLETION_EXT};
      xrSetGoogleCloudAuthCompleteANDROID(session, future, &completion);

      if (completion.futureResult == XR_SUCCESS) {
        // Credentials were successfully applied.
      } else if (completion.futureResult == XR_ERROR_KEYLESS_AUTH_FAILED_ANDROID) {
        // An error occurred when setting keyless auth credentials. This error may be retried.
      }
    }

## New Commands

- [xrSetGoogleCloudAuthAsyncANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#xrSetGoogleCloudAuthAsyncANDROID)
- [xrSetGoogleCloudAuthCompleteANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#xrSetGoogleCloudAuthCompleteANDROID)

## New Structures

- [XrGoogleCloudAuthInfoApiKeyANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#XrGoogleCloudAuthInfoApiKeyANDROID)
- [XrGoogleCloudAuthInfoBaseHeaderANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#XrGoogleCloudAuthInfoBaseHeaderANDROID)
- [XrGoogleCloudAuthInfoKeylessANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#XrGoogleCloudAuthInfoKeylessANDROID)
- [XrGoogleCloudAuthInfoTokenANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#XrGoogleCloudAuthInfoTokenANDROID)
- Extending [XrGoogleCloudAuthInfoBaseHeaderANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#XrGoogleCloudAuthInfoBaseHeaderANDROID) :

  - [XrGoogleCloudAuthErrorResultANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#XrGoogleCloudAuthErrorResultANDROID)

## New Enums

- [XrGoogleCloudAuthErrorANDROID](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_google_cloud_auth#XrGoogleCloudAuthErrorANDROID)

## New Enum Constants

- `XR_ANDROID_GOOGLE_CLOUD_AUTH_EXTENSION_NAME`
- `XR_ANDROID_google_cloud_auth_SPEC_VERSION`
- Extending [XrResult](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrResult) :

  - `XR_ERROR_KEYLESS_AUTH_FAILED_ANDROID`
  - `XR_ERROR_KEYLESS_AUTH_NOT_SETUP_ANDROID`
- Extending [XrStructureType](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrStructureType) :

  - `XR_TYPE_GOOGLE_CLOUD_AUTH_ERROR_RESULT_ANDROID`
  - `XR_TYPE_GOOGLE_CLOUD_AUTH_INFO_API_KEY_ANDROID`
  - `XR_TYPE_GOOGLE_CLOUD_AUTH_INFO_KEYLESS_ANDROID`
  - `XR_TYPE_GOOGLE_CLOUD_AUTH_INFO_TOKEN_ANDROID`

## Issues

- Revision 1, 2025-12-18 (Ben King)

  - Initial extension description.