---
title: https://developer.android.com/google/play/licensing/licensing-reference
url: https://developer.android.com/google/play/licensing/licensing-reference
source: md.txt
---

# Licensing Reference

## LVL Classes and Interfaces

Table 1 lists all of the source files in the License Verification Library (LVL) available through the Android SDK. All of the files are part of the`com.android.vending.licensing`package.

**Table 1.**Summary of LVL library classes and interfaces.  

|              Category               |           Name           |                                                                                                                                                            Description                                                                                                                                                             |
|-------------------------------------|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| License check and result            | LicenseChecker           | Class that you instantiate (or subclass) to initiate a license check.                                                                                                                                                                                                                                                              |
| License check and result            | *LicenseCheckerCallback* | Interface that you implement to handle result of the license check.                                                                                                                                                                                                                                                                |
| Policy                              | *Policy*                 | Interface that you implement to determine whether to allow access to the application, based on the license response.                                                                                                                                                                                                               |
| Policy                              | ServerManagedPolicy      | Default`Policy`implementation. Uses settings provided by the licensing server to manage local storage of license data, license validity, retry.                                                                                                                                                                                    |
| Policy                              | StrictPolicy             | Alternative`Policy`implementation. Enforces licensing based on a direct license response from the server only. No caching or request retry.                                                                                                                                                                                        |
| Data obfuscation *(optional)*       | *Obfuscator*             | Interface that you implement if you are using a`Policy`(such as ServerManagedPolicy) that caches license response data in a persistent store. Applies an obfuscation algorithm to encode and decode data being written or read.                                                                                                    |
| Data obfuscation *(optional)*       | AESObfuscator            | Default Obfuscator implementation that uses AES encryption/decryption algorithm to obfuscate/unobfuscate data.                                                                                                                                                                                                                     |
| Device limitation *(optional)*      | *DeviceLimiter*          | Interface that you implement if you want to restrict use of an application to a specific device. Called from LicenseValidator. Implementing DeviceLimiter is not recommended for most applications because it requires a backend server and may cause the user to lose access to licensed applications, unless designed with care. |
| Device limitation *(optional)*      | NullDeviceLimiter        | Default DeviceLimiter implementation that is a no-op (allows access to all devices).                                                                                                                                                                                                                                               |
| Library core, no integration needed | ResponseData             | Class that holds the fields of a license response.                                                                                                                                                                                                                                                                                 |
| Library core, no integration needed | LicenseValidator         | Class that decrypts and verifies a response received from the licensing server.                                                                                                                                                                                                                                                    |
| Library core, no integration needed | ValidationException      | Class that indicates errors that occur when validating the integrity of data managed by an Obfuscator.                                                                                                                                                                                                                             |
| Library core, no integration needed | PreferenceObfuscator     | Utility class that writes/reads obfuscated data to the system's[SharedPreferences](https://developer.android.com/reference/android/content/SharedPreferences)store.                                                                                                                                                                |
| Library core, no integration needed | *ILicensingService*      | One-way IPC interface over which a license check request is passed to the Google Play client.                                                                                                                                                                                                                                      |
| Library core, no integration needed | *ILicenseResultListener* | One-way IPC callback implementation over which the application receives an asynchronous response from the licensing server.                                                                                                                                                                                                        |

## Server Response

Table 2 lists all of the license response fields returned by the licensing server.

**Table 2.**Summary of license response fields returned by the Google Play server.

|     Field      |                                                                                                                                                                                                                                                                                                                                                                                                                              Description                                                                                                                                                                                                                                                                                                                                                                                                                               |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `responseCode` | The response code returned by the licensing server. The response codes are outlined in[Server Response Codes](https://developer.android.com/google/play/licensing/licensing-reference#server-response-codes).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `signedData`   | A string concatenation holding the data returned by the licensing server, as follows:`responseCode|nonce|packageName|versionCode|userId|timestamp:extras`. - `responseCode`: The response code returned by the licensing server. - `nonce`: Nonce identifier of the request. - `packageName`: The package name of the app to check the license for. - `versionCode`: The version code of the app to check the license for. - `userId`: A unique ID for the user per app, where the same user gets a different ID for a different app. - `timestamp`: The number of milliseconds from the epoch of 1970-01-01 00:00:00 UTC to the request. - `extras`: Additional information to assist in the license management of the app. The extra fields are outlined in[Server Response Extras](https://developer.android.com/google/play/licensing/licensing-reference#extras). |
| `signature`    | The signature of the`signedData`using an app-specific key.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

## Server Response Codes

Table 3 lists all of the license response codes supported by the licensing server. In general, an application should handle all of these response codes. By default, the LicenseValidator class in the LVL provides all of the necessary handling of these response codes for you.

**Table 3.**Summary of response codes returned by the Google Play server in a license response.

|        Response Code         | Integer-value representation |                                                                               Description                                                                               | Signed? |       Extras        |                                                                                                                                            Comments                                                                                                                                            |
|------------------------------|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `LICENSED`                   | `0`                          | The application is licensed to the user. The user has purchased the application, or is authorized to download and install the alpha or beta version of the application. | Yes     | `VT`,`GT`,`GR`      | *Allow access according to`Policy`constraints.*                                                                                                                                                                                                                                                |
| `LICENSED_OLD_KEY`           | `2`                          | The application is licensed to the user, but there is an updated application version available that is signed with a different key.                                     | Yes     | `VT`,`GT`,`GR`,`UT` | *Optionally allow access according to`Policy`constraints.* Can indicate that the key pair used by the installed application version is invalid or compromised. The application can allow access if needed or inform the user that an upgrade is available and limit further use until upgrade. |
| `NOT_LICENSED`               | `1`                          | The application is not licensed to the user.                                                                                                                            | No      |                     | *Do not allow access.*                                                                                                                                                                                                                                                                         |
| `ERROR_CONTACTING_SERVER`    | `257`                        | Local error --- the Google Play application was not able to reach the licensing server, possibly because of network availability problems.                              | No      |                     | *Retry the license check according to`Policy`retry limits.*                                                                                                                                                                                                                                    |
| `ERROR_SERVER_FAILURE`       | `4`                          | Server error --- the server could not load the application's key pair for licensing.                                                                                    | No      |                     | *Retry the license check according to`Policy`retry limits.*                                                                                                                                                                                                                                    |
| `ERROR_INVALID_PACKAGE_NAME` | `258`                        | Local error --- the application requested a license check for a package that is not installed on the device.                                                            | No      |                     | *Do not retry the license check.* Typically caused by a development error.                                                                                                                                                                                                                     |
| `ERROR_NON_MATCHING_UID`     | `259`                        | Local error --- the application requested a license check for a package whose UID (package, user ID pair) does not match that of the requesting application.            | No      |                     | *Do not retry the license check.* Typically caused by a development error.                                                                                                                                                                                                                     |
| `ERROR_NOT_MARKET_MANAGED`   | `3`                          | Server error --- the application (package name) was not recognized by Google Play.                                                                                      | No      |                     | *Do not retry the license check.* Can indicate that the application was not published through Google Play or that there is a development error in the licensing implementation.                                                                                                                |

**Note:** As documented in[Setting Up The Testing Environment](https://developer.android.com/google/play/licensing/setting-up#test-env), the response code can be manually overridden for the application developer and any registered test users via the Google Play Console.

**Note:** Previously you could test an app by uploading an unpublished "draft" version. This functionality is no longer supported; instead, you must publish it to the alpha or beta distribution channel. For more information, see[Draft Apps are No Longer Supported](https://developer.android.com/google/play/billing/billing_testing#draft_apps).

## Server Response Extras

To assist your application in managing access to the application across the application refund period and provide other information, The licensing server includes several pieces of information in the license responses. Specifically, the service provides recommended values for the application's license validity period, retry grace period, maximum allowable retry count, and other settings. If your application uses[APK expansion files](https://developer.android.com/google/play/expansion-files), the response also includes the file names, sizes, and URLs. The server appends the settings as key-value pairs in the license response "extras" field.

Any`Policy`implementation can extract the extras settings from the license response and use them as needed. The LVL default`Policy`implementation,[`ServerManagedPolicy`](https://developer.android.com/google/play/licensing/adding-licensing#ServerManagedPolicy), serves as a working implementation and an illustration of how to obtain, store, and use the settings.

**Table 4.**Summary of license-management settings supplied by the Google Play server in a license response.

|           Extra            |                                                                                                                                                                                             Description                                                                                                                                                                                             |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `VT`                       | License validity timestamp. Specifies the date/time at which the current (cached) license response expires and must be rechecked on the licensing server. See the section below about[License validity period](https://developer.android.com/google/play/licensing/licensing-reference#VT).                                                                                                         |
| `GT`                       | Grace period timestamp. Specifies the end of the period during which a Policy may allow access to the application, even though the response status is`RETRY`. The value is managed by the server, however a typical value would be 5 or more days. See the section below about[Retry period and maximum retry count](https://developer.android.com/google/play/licensing/licensing-reference#GTGR). |
| `GR`                       | Maximum retries count. Specifies how many consecutive`RETRY`license checks the`Policy`should allow, before denying the user access to the application. The value is managed by the server, however a typical value would be "10" or higher. See the section below about[Retry period and maximum retry count](https://developer.android.com/google/play/licensing/licensing-reference#GTGR).        |
| `UT`                       | Update timestamp. Specifies the day/time when the most recent update to this application was uploaded and published. The server returns this extra only for`LICENSED_OLD_KEYS`responses, to allow the`Policy`to determine how much time has elapsed since an update was published with new licensing keys before denying the user access to the application.                                        |
| `FILE_URL1`or`FILE_URL2`   | The URL for an expansion file (1 is for the main file, 2 is the patch file). Use this to download the file over HTTP.                                                                                                                                                                                                                                                                               |
| `FILE_NAME1`or`FILE_NAME2` | The expansion file's name (1 is for the main file, 2 is the patch file). You must use this name when saving the file on the device.                                                                                                                                                                                                                                                                 |
| `FILE_SIZE1`or`FILE_SIZE2` | The size of the file in bytes (1 is for the main file, 2 is the patch file). Use this to assist with downloading and to ensure that enough space is available on the device's shared storage location before downloading.                                                                                                                                                                           |

#### License validity period

The Google Play licensing server sets a license validity period for all downloaded applications. The period expresses the interval of time over which an application's license status should be considered as unchanging and cacheable by a licensing`Policy`in the application. The licensing server includes the validity period in its response to all license checks, appending an end-of-validity timestamp to the response as an extra under the key`VT`. A`Policy`can extract the VT key value and use it to conditionally allow access to the application without rechecking the license, until the validity period expires.

The license validity signals to a licensing`Policy`when it must recheck the licensing status with the licensing server. It is*not* intended to imply whether an application is actually licensed for use. That is, when an application's license validity period expires, this does not mean that the application is no longer licensed for use --- rather, it indicates only that the`Policy`must recheck the licensing status with the server. It follows that, as long as the license validity period has not expired, it is acceptable for the`Policy`to cache the initial license status locally and return the cached license status instead of sending a new license check to the server.

The licensing server manages the validity period as a means of helping the application properly enforce licensing across the refund period offered by Google Play for paid applications. It sets the validity period based on whether the application was purchased and, if so, how long ago. Specifically, the server sets a validity period as follows:

- For a paid application, the server sets the initial license validity period so that the license response remains valid for as long as the application is refundable. A licensing`Policy`in the application may cache the result of the initial license check and does not need to recheck the license until the validity period has expired.
- When an application is no longer refundable, the server sets a longer validity period --- typically a number of days.
- For a free application, the server sets the validity period to a very high value (`long.MAX_VALUE`). This ensures that, provided the`Policy`has cached the validity timestamp locally, it will not need to recheck the license status of the application in the future.

The`ServerManagedPolicy`implementation uses the extracted timestamp (`mValidityTimestamp`) as a primary condition for determining whether to recheck the license status with the server before allowing the user access to the application.

#### Retry period and maximum retry count

In some cases, system or network conditions can prevent an application's license check from reaching the licensing server, or prevent the server's response from reaching the Google Play client application. For example, the user might launch an application when there is no cell network or data connection available---such as when on an airplane---or when the network connection is unstable or the cell signal is weak.

When network problems prevent or interrupt a license check, the Google Play client notifies the application by returning a`RETRY`response code to the`Policy`'s`processServerResponse()`method. In the case of system problems, such as when the application is unable to bind with Google Play's`ILicensingService`implementation, the`LicenseChecker`library itself calls the Policy`processServerResponse()`method with a`RETRY`response code.

In general, the`RETRY`response code is a signal to the application that an error has occurred that has prevented a license check from completing.

The Google Play server helps an application to manage licensing under error conditions by setting a retry "grace period" and a recommended maximum retries count. The server includes these values in all license check responses, appending them as extras under the keys`GT`and`GR`.

The application`Policy`can extract the`GT`and`GR`extras and use them to conditionally allow access to the application, as follows:

- For a license check that results in a`RETRY`response, the`Policy`should cache the`RETRY`response code and increment a count of`RETRY`responses.
- The`Policy`should allow the user to access the application, provided that either the retry grace period is still active or the maximum retries count has not been reached.

The`ServerManagedPolicy`uses the server-supplied`GT`and`GR`values as described above. The example below shows the conditional handling of the retry responses in the`allow()`method. The count of`RETRY`responses is maintained in the`processServerResponse()`method, not shown.  

### Kotlin

```kotlin
fun allowAccess(): Boolean {
    val ts = System.currentTimeMillis()
    return when(lastResponse) {
        LICENSED -> {
            // Check if the LICENSED response occurred within the validity timeout.
            ts <= validityTimestamp  // Cached LICENSED response is still valid.
        }
        RETRY -> {
            ts < lastResponseTime + MILLIS_PER_MINUTE &&
                    // Only allow access if we are within the retry period
                    // or we haven't used up our max retries.
                    (ts <= retryUntil || retryCount <= maxRetries)
        }
        else -> false
    }
}
```

### Java

```java
public boolean allowAccess() {
    long ts = System.currentTimeMillis();
    if (lastResponse == LicenseResponse.LICENSED) {
        // Check if the LICENSED response occurred within the validity timeout.
        if (ts <= validityTimestamp) {
            // Cached LICENSED response is still valid.
            return true;
        }
    } else if (lastResponse == LicenseResponse.RETRY &&
                ts < lastResponseTime + MILLIS_PER_MINUTE) {
        // Only allow access if we are within the retry period
        // or we haven't used up our max retries.
        return (ts <= retryUntil || retryCount <= maxRetries);
    }
    return false;
}
```