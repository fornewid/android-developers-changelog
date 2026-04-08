---
title: https://developer.android.com/google/play/integrity/error-codes
url: https://developer.android.com/google/play/integrity/error-codes
source: md.txt
---

# Handle Play Integrity API error codes

If your app makes a Play Integrity API request and the call fails, your app receives an error code. These errors can happen for various reasons, such as environmental issues like a poor network connection, problems with your API integration, or malicious activity and active attacks. The type of error code returned depends on the type of request:

- Standard requests: The API returns a[StandardIntegrityErrorCode](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode).
- Classic requests: The API returns a[IntegrityErrorCode](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityErrorCode).

| **Note:** If the error is due to transient conditions, you should retry the call. If the conditions are not transient, you should not retry the call.

## Retry strategies

Use exponential backoff for Play Integrity operations that happen in the background and don't affect the user experience while the user is in session.

For example, it is appropriate to implement this when acknowledging new purchases because this operation can happen in the background, and acknowledgment doesn't need to happen in real time if an error occurs.

After the first failure, start with an initial delay of 5 seconds before retrying.

Implement a retry strategy with a maximum number of attempts as an exit condition using an exponentially increased delay each time (10s, 20s).

While performing these retry attempts, check for a network connection and don't overload the device.

If you continue to see errors after three retry attempts, treat the outcome as if the client has failed all integrity checks. The error can be for several reasons, including (but not limited to): an overloaded device, network connection issues, or an attempt by an attacker.

## Error codes values for the java library

|      | [`IntegrityErrorCode`](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityErrorCode) | [`StandardIntegrityErrorCode`](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode) |
|------|-------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| -1   | [`API_NOT_AVAILABLE`](https://developer.android.com/google/play/integrity/error-codes#iErr_1)                                                         | [`API_NOT_AVAILABLE`](https://developer.android.com/google/play/integrity/error-codes#iErr_1)                                                                         |
| -2   | [`PLAY_STORE_NOT_FOUND`](https://developer.android.com/google/play/integrity/error-codes#iErr_2)                                                      | [`PLAY_STORE_NOT_FOUND`](https://developer.android.com/google/play/integrity/error-codes#iErr_2)                                                                      |
| -3   | [`NETWORK_ERROR`](https://developer.android.com/google/play/integrity/error-codes#iErr_3)                                                             | [`NETWORK_ERROR`](https://developer.android.com/google/play/integrity/error-codes#iErr_3)                                                                             |
| -4   | [`PLAY_STORE_ACCOUNT_NOT_FOUND`](https://developer.android.com/google/play/integrity/error-codes#iErr_4)                                              |                                                                                                                                                                       |
| -5   | [`APP_NOT_INSTALLED`](https://developer.android.com/google/play/integrity/error-codes#iErr_5)                                                         | [`APP_NOT_INSTALLED`](https://developer.android.com/google/play/integrity/error-codes#iErr_5)                                                                         |
| -6   | [`PLAY_SERVICES_NOT_FOUND`](https://developer.android.com/google/play/integrity/error-codes#iErr_6)                                                   | [`PLAY_SERVICES_NOT_FOUND`](https://developer.android.com/google/play/integrity/error-codes#iErr_6)                                                                   |
| -7   | [`APP_UID_MISMATCH`](https://developer.android.com/google/play/integrity/error-codes#iErr_7)                                                          | [`APP_UID_MISMATCH`](https://developer.android.com/google/play/integrity/error-codes#iErr_7)                                                                          |
| -8   | [`TOO_MANY_REQUESTS`](https://developer.android.com/google/play/integrity/error-codes#iErr_8)                                                         | [`TOO_MANY_REQUESTS`](https://developer.android.com/google/play/integrity/error-codes#iErr_8)                                                                         |
| -9   | [`CANNOT_BIND_TO_SERVICE`](https://developer.android.com/google/play/integrity/error-codes#iErr_9)                                                    | [`CANNOT_BIND_TO_SERVICE`](https://developer.android.com/google/play/integrity/error-codes#iErr_9)                                                                    |
| -10  | [`NONCE_TOO_SHORT`](https://developer.android.com/google/play/integrity/error-codes#iErr_10)                                                          |                                                                                                                                                                       |
| -11  | [`NONCE_TOO_LONG`](https://developer.android.com/google/play/integrity/error-codes#iErr_11)                                                           |                                                                                                                                                                       |
| -12  | [`GOOGLE_SERVER_UNAVAILABLE`](https://developer.android.com/google/play/integrity/error-codes#iErr_12)                                                | [`GOOGLE_SERVER_UNAVAILABLE`](https://developer.android.com/google/play/integrity/error-codes#iErr_12)                                                                |
| -13  | [`NONCE_IS_NOT_BASE64`](https://developer.android.com/google/play/integrity/error-codes#iErr_13)                                                      |                                                                                                                                                                       |
| -14  | [`PLAY_STORE_VERSION_OUTDATED`](https://developer.android.com/google/play/integrity/error-codes#iErr_14)                                              | [`PLAY_STORE_VERSION_OUTDATED`](https://developer.android.com/google/play/integrity/error-codes#iErr_14)                                                              |
| -15  | [`PLAY_SERVICES_VERSION_OUTDATED`](https://developer.android.com/google/play/integrity/error-codes#iErr_15)                                           | [`PLAY_SERVICES_VERSION_OUTDATED`](https://developer.android.com/google/play/integrity/error-codes#iErr_15)                                                           |
| -16  | [`CLOUD_PROJECT_NUMBER_IS_INVALID`](https://developer.android.com/google/play/integrity/error-codes#iErr_16)                                          | [`CLOUD_PROJECT_NUMBER_IS_INVALID`](https://developer.android.com/google/play/integrity/error-codes#iErr_16)                                                          |
| -17  | [`CLIENT_TRANSIENT_ERROR`](https://developer.android.com/google/play/integrity/error-codes#iErr_18)                                                   | [`REQUEST_HASH_TOO_LONG`](https://developer.android.com/google/play/integrity/error-codes#iErr_17)                                                                    |
| -18  |                                                                                                                                                       | [`CLIENT_TRANSIENT_ERROR`](https://developer.android.com/google/play/integrity/error-codes#iErr_18)                                                                   |
| -19  |                                                                                                                                                       | [`INTEGRITY_TOKEN_PROVIDER_INVALID`](https://developer.android.com/google/play/integrity/error-codes#iErr_19)                                                         |
| -100 | [`INTERNAL_ERROR`](https://developer.android.com/google/play/integrity/error-codes#iErr_100)                                                          | [`INTERNAL_ERROR`](https://developer.android.com/google/play/integrity/error-codes#iErr_100)                                                                          |

## Additional error codes values for the native library

|      | [`IntegrityErrorCode`](https://developer.android.com/reference/native/play/core/group/integrity#group__integrity_1gaf9eae9c6d1e03ee0d21395087c0bfac1) | [`StandardIntegrityErrorCode`](https://developer.android.com/reference/native/play/core/group/integrity#group__integrity_1gade0d369f226c3a93cb70dbeba6b89601) |
|------|-------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| -100 | [`INTEGRITY_INTERNAL_ERROR`](https://developer.android.com/google/play/integrity/error-codes#iErrC100)                                                | [`STANDARD_INTEGRITY_INTERNAL_ERROR`](https://developer.android.com/google/play/integrity/error-codes#iErrC100)                                               |
| -101 | [`INTEGRITY_INITIALIZATION_NEEDED`](https://developer.android.com/google/play/integrity/error-codes#iErrC101)                                         | [`STANDARD_INTEGRITY_INITIALIZATION_NEEDED`](https://developer.android.com/google/play/integrity/error-codes#iErrC101)                                        |
| -102 | [`INTEGRITY_INITIALIZATION_FAILED`](https://developer.android.com/google/play/integrity/error-codes#iErrC102)                                         | [`STANDARD_INTEGRITY_INITIALIZATION_FAILED`](https://developer.android.com/google/play/integrity/error-codes#iErrC102)                                        |
| -103 | [`INTEGRITY_INVALID_ARGUMENT`](https://developer.android.com/google/play/integrity/error-codes#iErrC103)                                              | [`STANDARD_INTEGRITY_INVALID_ARGUMENT`](https://developer.android.com/google/play/integrity/error-codes#iErrC103)                                             |

## Retryable error codes

The cause of these errors is sometimes due to transient conditions, and thus you should retry the call.

### [`NETWORK_ERROR`](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode#NETWORK_ERROR)(Error Code -3)

This error indicates that there was a problem with the network connection between the device and Play systems.

#### Possible resolution

1. Use the[`GET_INTEGRITY`](https://developer.android.com/google/play/integrity/remediation#get-integrity-dialog)or[`GET_STRONG_INTEGRITY`](https://developer.android.com/google/play/integrity/remediation#get-strong-integrity-dialog)dialog to initiate a Play-guided experience that helps the user establish and confirm network connectivity.
2. Ask the user to check for network connectivity, and use basic retries or exponential backoff, depending on which action triggered the error.

#### See also

[`NETWORK_ERROR`](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityErrorCode#NETWORK_ERROR)for classic requests.

### [`TOO_MANY_REQUESTS`](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode#TOO_MANY_REQUESTS)(Error Code -8)

The calling app is making too many requests to the API and has been throttled, or your app has exceeded its daily request quota.

#### Possible resolution

1. Retry with an exponential backoff.
2. Request to[increase your daily maximum](https://developer.android.com/google/play/integrity/setup#increase-daily)number of requests

#### See also

[`TOO_MANY_REQUESTS`](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityErrorCode#TOO_MANY_REQUESTS)for classic requests.

### [`GOOGLE_SERVER_UNAVAILABLE`](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode#GOOGLE_SERVER_UNAVAILABLE)(Error Code -12)

Unknown internal Google server error.

#### Possible resolution

Retry with an exponential backoff. Consider[filing a bug](https://issuetracker.google.com/issues/new?component=1152695&template=1655477)if it fails consistently.

#### See also

[`GOOGLE_SERVER_UNAVAILABLE`](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityErrorCode#GOOGLE_SERVER_UNAVAILABLE)for classic requests.

### [`CLIENT_TRANSIENT_ERROR`](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode#CLIENT_TRANSIENT_ERROR)(Error Code -18)

Transient error has occurred on the client device.

For Standard API requests, this is supported as of version 1.3.0 of the[Play Integrity API library for Kotlin and Java](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/release-notes#1-3-0),[Google Play Integrity Plugin for Unity](https://developers.google.com/unity/packages#play_integrity_api)1.3.0 or higher and[Play Core Native SDK](https://developer.android.com/guide/playcore/native#play_core_native_sdk)1.13.0 or higher.

#### Possible resolution

Retry with an exponential backoff.

#### See also

[`CLIENT_TRANSIENT_ERROR`](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityErrorCode#CLIENT_TRANSIENT_ERROR)for classic requests.

**Note:**When reported while using a Classic API request, the value returned is -17.

### [`INTERNAL_ERROR`](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode#INTERNAL_ERROR)(Error Code -100)

Unknown internal error.

#### Possible resolution

Retry with an exponential backoff. Consider filing a bug if it fails consistently.

#### See also

[`INTERNAL_ERROR`](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityErrorCode#INTERNAL_ERROR)for classic requests.

### [`STANDARD_INTEGRITY_INTERNAL_ERROR`](https://developer.android.com/reference/native/play/core/group/integrity#group__integrity_1ggade0d369f226c3a93cb70dbeba6b89601a7430edd4361bdca9585a38971c32174f)(Error Code -100)

Unknown internal error.

#### Possible resolution

Retry with an exponential backoff. Consider filing a bug if it fails consistently.

#### See also

See[`INTEGRITY_INTERNAL_ERROR`](https://developer.android.com/reference/native/play/core/group/integrity#group__integrity_1ggaf9eae9c6d1e03ee0d21395087c0bfac1a5e97a5a309ee2448717440633b9fab87)for classic requests.

### [`STANDARD_INTEGRITY_INITIALIZATION_FAILED`](https://developer.android.com/reference/native/play/core/group/integrity#group__integrity_1ggade0d369f226c3a93cb70dbeba6b89601ac3439c555b8c3b4996f518e255e5a45a)(Error Code -102)

There was an error initializing the Standard Integrity API.

#### Possible resolution

Retry with an exponential backoff. Consider filing a bug if it fails consistently.

#### See also

See[`INTEGRITY_INITIALIZATION_FAILED`](https://developer.android.com/reference/native/play/core/group/integrity#group__integrity_1ggaf9eae9c6d1e03ee0d21395087c0bfac1a5e97a5a309ee2448717440633b9fab87)for classic requests.

## Non-Retryable Error Codes

Automatic retries are unlikely to help in these cases. However, a manual retry may help if the user addresses the condition that caused the issue. For example, if the user updates their Play Store version to a supported version, then a manual retry of the initial operation could work.

### [`API_NOT_AVAILABLE`](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode#API_NOT_AVAILABLE)(Error Code -1)

The Play Store version installed on the device might be old and the Integrity API not available. Another possibility is that Integrity API is not enabled in Google Play Console.

#### Possible resolution

- Make sure that Integrity API is enabled in Google Play Console.
- Ask the user to update the Play Store.

#### See also

See[`API_NOT_AVAILABLE`](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityErrorCode#API_NOT_AVAILABLE)for classic request.

### [`PLAY_STORE_NOT_FOUND`](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode#PLAY_STORE_NOT_FOUND)(Error Code -2)

No official Play Store app was found on the device.

#### Possible resolution

Ask the user to install or enable Google Play Store.

#### See also

See[`PLAY_STORE_NOT_FOUND`](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityErrorCode#PLAY_STORE_NOT_FOUND)for classic request.

### [`PLAY_STORE_ACCOUNT_NOT_FOUND`](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityErrorCode#PLAY_STORE_ACCOUNT_NOT_FOUND)(Error Code -4)

**Note:** This is only reported for classic request through`IntegrityErrorCode`.

No Play Store account is found on the device. Note that the Play Integrity API now supports unauthenticated requests. This error code is used only for older Play Store versions that lack support.

#### Possible resolution

Ask the user to update and sign in to the Google Play Store.

### [`APP_NOT_INSTALLED`](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode#APP_NOT_INSTALLED)(Error Code -5)

The calling app is not installed. Something is wrong (possibly an attack).

#### Possible resolution

Non-actionable. Treat the outcome as if the client has failed all integrity checks.

#### See also

See[`APP_NOT_INSTALLED`](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityErrorCode#APP_NOT_INSTALLED)for classic request.

### [`PLAY_SERVICES_NOT_FOUND`](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode#PLAY_SERVICES_NOT_FOUND)(Error Code -6)

Play services are unavailable or need to be updated.

#### Possible resolution

1. Use the[`GET_INTEGRITY`](https://developer.android.com/google/play/integrity/remediation#get-integrity-dialog)or[`GET_STRONG_INTEGRITY`](https://developer.android.com/google/play/integrity/remediation#get-strong-integrity-dialog)dialog to initiate a Play-guided experience that helps the user to install, update or enable Play services.
2. Ask the user to install, update, or enable Play services.

#### See also

See[`APP_NOT_INSTALLED`](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityErrorCode#PLAY_SERVICES_NOT_FOUND)for classic request.

### [`APP_UID_MISMATCH`](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode#APP_UID_MISMATCH)(Error Code -7)

The calling app UID (user ID) does not match the one from Package Manager.

#### Possible resolution

Non-actionable. Treat the outcome as if the client has failed all integrity checks.

#### See also

See[`APP_UID_MISMATCH`](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityErrorCode#APP_UID_MISMATCH)for classic request.

### [`CANNOT_BIND_TO_SERVICE`](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode#CANNOT_BIND_TO_SERVICE)(Error Code -9)

Binding to the service in the Play Store has failed. This can be due to having an old Play Store version installed on the device.

#### Possible resolution

Ask the user to update the Google Play Store.

#### See also

See[`CANNOT_BIND_TO_SERVICE`](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityErrorCode#CANNOT_BIND_TO_SERVICE)for classic request.

### [`NONCE_TOO_SHORT`](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityErrorCode#NONCE_TOO_SHORT)(Error Code -10)

**Note:** This is only reported for classic request through`IntegrityErrorCode`.

Nonce length is too short. The nonce must be a minimum of 16 bytes before base64 encoding.

#### Possible resolution

Retry with a longer nonce.

### [`NONCE_TOO_LONG`](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityErrorCode#NONCE_TOO_LONG)(Error Code -11)

**Note:** This is only reported for classic request through`IntegrityErrorCode`.

Nonce length is too long. The nonce must be less than 500 bytes before base64 encoding.

#### Possible resolution

Retry with a shorter nonce.

### [`NONCE_IS_NOT_BASE64`](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityErrorCode#NONCE_IS_NOT_BASE64)(Error Code -13)

**Note:** This is only reported for classic request through`IntegrityErrorCode`.

Nonce is not encoded as a base64 web-safe no-wrap string.

#### Possible resolution

Retry with a nonce in the correct format.

### [`PLAY_STORE_VERSION_OUTDATED`](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode#PLAY_STORE_VERSION_OUTDATED)(Error Code -14)

Google Play Store app needs to be updated.

#### Possible resolution

Ask the user to update the Google Play Store.

#### See also

See[`PLAY_STORE_VERSION_OUTDATED`](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityErrorCode#PLAY_STORE_VERSION_OUTDATED)for classic request.

### [`PLAY_SERVICES_VERSION_OUTDATED`](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode#PLAY_SERVICES_VERSION_OUTDATED)(Error Code -15)

Google Play services need to be updated.

#### Possible resolution

1. Use the[`GET_INTEGRITY`](https://developer.android.com/google/play/integrity/remediation#get-integrity-dialog)or[`GET_STRONG_INTEGRITY`](https://developer.android.com/google/play/integrity/remediation#get-strong-integrity-dialog)dialog to initiate a Play-guided experience that helps the user to update Google Play services.
2. Ask the user to update Google Play services.

#### See also

See[`PLAY_SERVICES_VERSION_OUTDATED`](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityErrorCode#PLAY_SERVICES_VERSION_OUTDATED)for classic request.

### [`CLOUD_PROJECT_NUMBER_IS_INVALID`](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode#CLOUD_PROJECT_NUMBER_IS_INVALID)(Error Code -16)

The provided cloud project number is invalid.

#### Possible resolution

Use the Cloud project number for the Cloud project for which you enabled Play Integrity API.

#### See also

See[`CLOUD_PROJECT_NUMBER_IS_INVALID`](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityErrorCode#CLOUD_PROJECT_NUMBER_IS_INVALID)for classic request.

### [`REQUEST_HASH_TOO_LONG`](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode#REQUEST_HASH_TOO_LONG)(Error Code -17)

**Note:** This is only reported when using standard request through`StandardIntegrityErrorCode`.

The provided`requestHash`is too long. The`requestHash`length must be less than 500 characters.

#### Possible resolution

Retry with a shorter`requestHash`.

### [`INTEGRITY_TOKEN_PROVIDER_INVALID`](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode#INTEGRITY_TOKEN_PROVIDER_INVALID)(Error Code -19)

**Note:** This is only reported for standard request through`StandardIntegrityErrorCode`.

The`StandardIntegrityTokenProvider`is no longer valid. This can happen because the token provider expired or the user cleared the Play Store app's data, which removed the token provider.

This error code is available only for Standard API requests, where it is supported as of library version 1.3.0 for the Kotlin and Java programming languages, Google Play Integrity Plugin for Unity 1.3.0 or higher and Play Core Native SDK 1.13.0 or higher.

#### Possible resolution

Request a new integrity token provider.

### [`STANDARD_INTEGRITY_INITIALIZATION_NEEDED`](https://developer.android.com/reference/native/play/core/group/integrity#group__integrity_1ggade0d369f226c3a93cb70dbeba6b89601aa8faf582b855a79456116940366c1b63)(Error Code -101)

`StandardIntegrityManager`is not initialized.

#### Possible resolution

Call[`StandardIntegrityManager_init()`](https://developer.android.com/reference/native/play/core/group/integrity#group__integrity_1gaaf0091c762d6849a6906a3f21ea22671)first.

#### See also

See[`INTEGRITY_INITIALIZATION_NEEDED`](https://developer.android.com/reference/native/play/core/group/integrity#group__integrity_1ggaf9eae9c6d1e03ee0d21395087c0bfac1ad76b1d459925665e0ab487ec30e6fb4c)for Classic Requests

### [`STANDARD_INTEGRITY_INVALID_ARGUMENT`](https://developer.android.com/reference/native/play/core/group/integrity#group__integrity_1ggade0d369f226c3a93cb70dbeba6b89601a78857bcc3411049517d5eac4af9115c8)(Error Code -103)

Invalid argument passed to the Standard Integrity API.

#### Possible resolution

Retry with the correct argument.

#### See also

See[`INTEGRITY_INVALID_ARGUMENT`](https://developer.android.com/reference/native/play/core/group/integrity#group__integrity_1ggaf9eae9c6d1e03ee0d21395087c0bfac1a996161e5beb0d9669bebe448e0f1e468)for Classic Requests.