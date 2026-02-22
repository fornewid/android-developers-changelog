---
title: https://developer.android.com/google/play/integrity/verdicts
url: https://developer.android.com/google/play/integrity/verdicts
source: md.txt
---

# Integrity verdicts

This page describes how to interpret and work with the returned integrity verdict. Whether you make a standard or classic API request, the integrity verdict is returned in the same format with similar content. The integrity verdict communicates information about the validity of devices, apps, and accounts. Your app's server can use the resulting payload in a decrypted, verified verdict to determine how best to proceed with a particular action or request in your app.

## Returned integrity verdict format

The payload is plain-text JSON and contains integrity signals alongside developer-provided information.

The general payload structure is as follows:  

```json
{
  "requestDetails": { ... },
  "appIntegrity": { ... },
  "deviceIntegrity": { ... },
  "accountDetails": { ... },
  "environmentDetails": { ... }
}
```

You must first check that the values in the`requestDetails`field match those of the original request before checking each integrity verdict. The following sections describe each field in more detail.

### Request details field

The`requestDetails`field contains information about the request, including developer-provided information in the`requestHash`for standard requests and the`nonce`for classic requests.

For**standard**API requests:  

```json
"requestDetails": {
  // Application package name this attestation was requested for.
  // Note that this field might be spoofed in the middle of the request.
  "requestPackageName": "com.package.name",
  // Request hash provided by the developer.
  "requestHash": "aGVsbG8gd29scmQgdGhlcmU",
  // The timestamp in milliseconds when the integrity token
  // was requested.
  "timestampMillis": "1675655009345"
}
```

These values should match those of the original request. Therefore, verify the`requestDetails`part of the JSON payload by making sure that the`requestPackageName`and`requestHash`match what was sent in the original request, as shown in the following code snippet:  

### Kotlin

```kotlin
val requestDetails = JSONObject(payload).getJSONObject("requestDetails")
val requestPackageName = requestDetails.getString("requestPackageName")
val requestHash = requestDetails.getString("requestHash")
val timestampMillis = requestDetails.getLong("timestampMillis")
val currentTimestampMillis = ...

// Ensure the token is from your app.
if (!requestPackageName.equals(expectedPackageName)
        // Ensure the token is for this specific request
    || !requestHash.equals(expectedRequestHash)
        // Ensure the freshness of the token.
    || currentTimestampMillis - timestampMillis > ALLOWED_WINDOW_MILLIS) {
        // The token is invalid! See below for further checks.
        ...
}
```

### Java

```java
RequestDetails requestDetails =
    decodeIntegrityTokenResponse
    .getTokenPayloadExternal()
    .getRequestDetails();
String requestPackageName = requestDetails.getRequestPackageName();
String requestHash = requestDetails.getRequestHash();
long timestampMillis = requestDetails.getTimestampMillis();
long currentTimestampMillis = ...;

// Ensure the token is from your app.
if (!requestPackageName.equals(expectedPackageName)
        // Ensure the token is for this specific request.
    || !requestHash.equals(expectedRequestHash)
        // Ensure the freshness of the token.
    || currentTimestampMillis - timestampMillis > ALLOWED_WINDOW_MILLIS) {
        // The token is invalid! See below for further checks.
        ...
}
```

For**classic**API requests:  

```json
"requestDetails": {
  // Application package name this attestation was requested for.
  // Note that this field might be spoofed in the middle of the
  // request.
  "requestPackageName": "com.package.name",
  // base64-encoded URL-safe no-wrap nonce provided by the developer.
  "nonce": "aGVsbG8gd29scmQgdGhlcmU",
  // The timestamp in milliseconds when the request was made
  // (computed on the server).
  "timestampMillis": "1617893780"
}
```

These values should match those of the original request. Therefore, verify the`requestDetails`part of the JSON payload by making sure that the`requestPackageName`and`nonce`match what was sent in the original request, as shown in the following code snippet:  

### Kotlin

```kotlin
val requestDetails = JSONObject(payload).getJSONObject("requestDetails")
val requestPackageName = requestDetails.getString("requestPackageName")
val nonce = requestDetails.getString("nonce")
val timestampMillis = requestDetails.getLong("timestampMillis")
val currentTimestampMillis = ...

// Ensure the token is from your app.
if (!requestPackageName.equals(expectedPackageName)
        // Ensure the token is for this specific request. See 'Generate a nonce'
        // section of the doc on how to store/compute the expected nonce.
    || !nonce.equals(expectedNonce)
        // Ensure the freshness of the token.
    || currentTimestampMillis - timestampMillis > ALLOWED_WINDOW_MILLIS) {
        // The token is invalid! See below for further checks.
        ...
}
```

### Java

```java
JSONObject requestDetails =
    new JSONObject(payload).getJSONObject("requestDetails");
String requestPackageName = requestDetails.getString("requestPackageName");
String nonce = requestDetails.getString("nonce");
long timestampMillis = requestDetails.getLong("timestampMillis");
long currentTimestampMillis = ...;

// Ensure the token is from your app.
if (!requestPackageName.equals(expectedPackageName)
        // Ensure the token is for this specific request. See 'Generate a nonce'
        // section of the doc on how to store/compute the expected nonce.
    || !nonce.equals(expectedNonce)
        // Ensure the freshness of the token.
    || currentTimestampMillis - timestampMillis > ALLOWED_WINDOW_MILLIS) {
        // The token is invalid! See below for further checks.
        ...
}
```

### Application integrity field

The`appIntegrity`field contains package-related information.  

```json
"appIntegrity": {
  // PLAY_RECOGNIZED, UNRECOGNIZED_VERSION, or UNEVALUATED.
  "appRecognitionVerdict": "PLAY_RECOGNIZED",
  // The package name of the app.
  // This field is populated iff appRecognitionVerdict != UNEVALUATED.
  "packageName": "com.package.name",
  // The sha256 digest of app certificates (base64-encoded URL-safe).
  // This field is populated iff appRecognitionVerdict != UNEVALUATED.
  "certificateSha256Digest": ["6a6a1474b5cbbb2b1aa57e0bc3"],
  // The version of the app.
  // This field is populated iff appRecognitionVerdict != UNEVALUATED.
  "versionCode": "42"
}
```

`appRecognitionVerdict`can have the following values:

`PLAY_RECOGNIZED`
:   The app and certificate match the versions distributed by Google Play.

`UNRECOGNIZED_VERSION`
:   The certificate or package name does not match Google Play records.

`UNEVALUATED`
:   Application integrity was not evaluated. A necessary requirement was missed, such as the device not being trustworthy enough.

To ensure that the token was generated by an app that was created by you, verify that the application integrity is as expected, as shown in the following code snippet:  

### Kotlin

```kotlin
val appIntegrity = JSONObject(payload).getJSONObject("appIntegrity")
val appRecognitionVerdict = appIntegrity.getString("appRecognitionVerdict")

if (appRecognitionVerdict == "PLAY_RECOGNIZED") {
    // Looks good!
}
```

### Java

```java
JSONObject appIntegrity =
    new JSONObject(payload).getJSONObject("appIntegrity");
String appRecognitionVerdict =
    appIntegrity.getString("appRecognitionVerdict");

if (appRecognitionVerdict.equals("PLAY_RECOGNIZED")) {
    // Looks good!
}
```

You can also check the app package name, app version, and app certificates manually.

### Device integrity field

The`deviceIntegrity`field can contain a single value,`deviceRecognitionVerdict`, that has one or more labels representing how well a device can enforce app integrity. If a device does not meet the criteria of any labels, then the`deviceIntegrity`field omits`deviceRecognitionVerdict`.  

```json
"deviceIntegrity": {
  // "MEETS_DEVICE_INTEGRITY" is one of several possible values.
  "deviceRecognitionVerdict": ["MEETS_DEVICE_INTEGRITY"]
}
```

By default,`deviceRecognitionVerdict`can contain the following:

`MEETS_DEVICE_INTEGRITY`
:   The app is running on a genuine and certified Android device. On Android 13 and higher, there is hardware-backed proof that the device bootloader is locked and the loaded Android OS is a certified device manufacturer image.

Empty (a blank value)
:   The app is running on a device that has signs of attack (such as API hooking) or system compromise (such as being rooted), or the app is not running on a physical device (such as an emulator that does not pass Google Play integrity checks).

To ensure that the token came from a trustworthy device, verify the`deviceRecognitionVerdict`is as expected, as shown in the following code snippet:  

### Kotlin

```kotlin
val deviceIntegrity =
    JSONObject(payload).getJSONObject("deviceIntegrity")
val deviceRecognitionVerdict =
    if (deviceIntegrity.has("deviceRecognitionVerdict")) {
        deviceIntegrity.getJSONArray("deviceRecognitionVerdict").toString()
    } else {
        ""
    }

if (deviceRecognitionVerdict.contains("MEETS_DEVICE_INTEGRITY")) {
    // Looks good!
}
```

### Java

```java
JSONObject deviceIntegrity =
    new JSONObject(payload).getJSONObject("deviceIntegrity");
String deviceRecognitionVerdict =
    deviceIntegrity.has("deviceRecognitionVerdict")
    ? deviceIntegrity.getJSONArray("deviceRecognitionVerdict").toString()
    : "";

if (deviceRecognitionVerdict.contains("MEETS_DEVICE_INTEGRITY")) {
    // Looks good!
}
```

If you are having problems with your testing device meeting device integrity, make sure the factory ROM is installed (for example, by resetting the device) and that the bootloader is locked. You can also[create Play Integrity API tests in your Play Console](https://developer.android.com/google/play/integrity/additional-tools#create-tests).

### Conditional device labels

If your app is being released to[Google Play Games for PC](https://developer.android.com/games/playgames/overview), the`deviceRecognitionVerdict`can also contain the following label:

`MEETS_VIRTUAL_INTEGRITY`
:   The app is running on an Android-powered emulator with Google Play services. The emulator passes system integrity checks and meets core Android compatibility requirements.

### Optional device information and device recall

If you[opt in to receive additional labels](https://developer.android.com/google/play/integrity/setup#configure-api)in the integrity verdict,`deviceRecognitionVerdict`can contain the following additional labels:

`MEETS_BASIC_INTEGRITY`
:   The app is running on a device that passes basic system integrity checks. The device bootloader can be locked or unlocked, and the boot state can be verified or unverified. The device may not be certified, in which case Google cannot provide any security, privacy, or app compatibility assurances. On Android 13 and higher, the`MEETS_BASIC_INTEGRITY`verdict requires only that the attestation[root of trust](https://developer.android.com/privacy-and-security/security-key-attestation#root_certificate)is provided by Google.

`MEETS_STRONG_INTEGRITY`
:   The app is running on a genuine and certified Android device with a recent security update.

    - On Android 13 and higher, the`MEETS_STRONG_INTEGRITY`verdict requires`MEETS_DEVICE_INTEGRITY`and security updates in the last year for all partitions of the device, including an Android OS partition patch and a vendor partition patch.
    - On Android 12 and lower, the`MEETS_STRONG_INTEGRITY`verdict only requires hardware-backed proof of boot integrity and**does not** require the device to have a recent security update. Therefore, when using the`MEETS_STRONG_INTEGRITY`, it is recommended to also take into account the Android SDK version in the`deviceAttributes`field.

A single device will return multiple device labels in the device integrity verdict if each of the label's criteria is met.

#### Device attributes

You can also opt in to device attributes, which tells the Android SDK version of the Android OS running on the device. In the future, it may be extended with other device attributes.

The SDK version value is the Android SDK version number defined in[`Build.VERSION_CODES`](https://developer.android.com/reference/android/os/Build.VERSION_CODES). The SDK version is not evaluated if a necessary requirement was missed. In this case, the`sdkVersion`field is unset; thus, the`deviceAttributes`field is empty. This could happen because:

- The device is not trustworthy enough.
- There were technical issues on the device.

<br />

If you opt in to receive`deviceAttributes`, the`deviceIntegrity`field will have the following extra field:  

```json
"deviceIntegrity": {
  "deviceRecognitionVerdict": ["MEETS_DEVICE_INTEGRITY"],
  "deviceAttributes": {
    // 33 is one possible value, which represents Android 13 (Tiramisu).
    "sdkVersion": 33
  }
}
```

In case the SDK version is not evaluated, the`deviceAttributes`field will be set as the following:  

```json
"deviceIntegrity": {
  "deviceRecognitionVerdict": ["MEETS_DEVICE_INTEGRITY"],
  "deviceAttributes": {}  // sdkVersion field is not set.
}
```

#### Recent device activity

You can also opt in to recent device activity, which tells you how many times your app requested an integrity token on a specific device in the last hour. You can use recent device activity to protect your app against unexpected, hyperactive devices that could be an indication of an active attack. You can decide how much to trust each recent device activity level based on how many times you expect your app installed on a typical device to request an integrity token each hour.

If you opt in to receive`recentDeviceActivity`the`deviceIntegrity`field will have two values:  

```json
"deviceIntegrity": {
  "deviceRecognitionVerdict": ["MEETS_DEVICE_INTEGRITY"],
  "recentDeviceActivity": {
    // "LEVEL_2" is one of several possible values.
    "deviceActivityLevel": "LEVEL_2"
  }
}
```

The`deviceActivityLevel`definitions differ between modes and can have one of the following values:

| **Recent device activity level** | **Standard API integrity token requests on this device in the last hour per app** | **Classic API integrity token requests on this device in the last hour per app** |
|----------------------------------|-----------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| `LEVEL_1`(lowest)                | 10 or fewer                                                                       | 5 or fewer                                                                       |
| `LEVEL_2`                        | Between 11 and 25                                                                 | Between 6 and 10                                                                 |
| `LEVEL_3`                        | Between 26 and 50                                                                 | Between 11 and 15                                                                |
| `LEVEL_4`(highest)               | More than 50                                                                      | More than 15                                                                     |
| `UNEVALUATED`                    | Recent device activity was not evaluated. This could happen because: - The device is not trustworthy enough. - The version of your app installed on the device is unknown to Google Play. - Technical issues on the device. ||

| **Note:** Level definitions are approximate.

#### Device recall (beta)

You can also opt in to[device recall](https://developer.android.com/google/play/integrity/device-recall), which lets you store some custom, per-device data with specific devices that you can reliably retrieve when your app is installed again later on the same device. After requesting an integrity token, you make a separate server-to-server call to[modify device recall values](https://developer.android.com/google/play/integrity/device-recall#modify-recall)for a specific device.

If you opt in to`deviceRecall`, the`deviceIntegrity`field will contain the device recall information that you set for the specific device:  

    "deviceIntegrity": {
      "deviceRecognitionVerdict": ["MEETS_DEVICE_INTEGRITY"],
      "deviceRecall": {
        "values": {
          "bitFirst": true,
          "bitSecond": false,
          "bitThird": true
        },
        "writeDates": {
          // Write time in YYYYMM format in UTC.
          "yyyymmFirst": 202401,
          // Note that yyyymmSecond is not set because bitSecond is false.
          "yyyymmThird": 202310
        }
      }
    }

The`deviceRecall`is split in two fields:

- `values`: Recall the bit values that you previously set for this device.
- `writeDates`: Recall the bit write dates in UTC accurate to the year and month. The write date of a recall bit will be updated every time the bit is set to`true`and will be removed when the bit is set to`false`.

In the case when device recall information is unavailable, the device recall value will be empty:  

    "deviceIntegrity": {
      "deviceRecognitionVerdict": ["MEETS_DEVICE_INTEGRITY"],
      "deviceRecall": {
        "values": {},
        "writeDates": {}
      }
    }

### Account details field

The`accountDetails`field contains a single value,`appLicensingVerdict`, that represents app's Google Play licensing status for the user account that's signed in on the device. If the user account has the Play license for the app, that means they downloaded it or bought it from Google Play.  

```json
"accountDetails": {
  // This field can be LICENSED, UNLICENSED, or UNEVALUATED.
  "appLicensingVerdict": "LICENSED"
}
```

`appLicensingVerdict`can have one of the following values:

`LICENSED`
:   The user has an app entitlement. In other words, the user installed or updated your app from Google Play on their device.
| **Note:** On some older devices the user keeps the app entitlement after uninstalling the app, so the user account will still be licensed if the user later obtains the same app another way.

`UNLICENSED`
:   The user doesn't have an app entitlement. This happens when, for example, the user sideloads your app or doesn't acquire it from Google Play. You can show the[GET_LICENSED](https://developer.android.com/google/play/integrity/remediation#get-licensed-dialog)dialog to users to remedy this.

`UNEVALUATED`

:   Licensing details were not evaluated because a necessary requirement was missed.

    This could happen for several reasons, including the following:

    - The device is not trustworthy enough.
    - The version of your app installed on the device is unknown to Google Play.
    - The user is not signed in to Google Play.

To check that the user has an app entitlement for your app, verify that the`appLicensingVerdict`is as expected, as shown in the following code snippet:  

### Kotlin

```kotlin
val accountDetails = JSONObject(payload).getJSONObject("accountDetails")
val appLicensingVerdict = accountDetails.getString("appLicensingVerdict")

if (appLicensingVerdict == "LICENSED") {
    // Looks good!
}
```

### Java

```java
JSONObject accountDetails =
    new JSONObject(payload).getJSONObject("accountDetails");
String appLicensingVerdict = accountDetails.getString("appLicensingVerdict");

if (appLicensingVerdict.equals("LICENSED")) {
    // Looks good!
}
```

### Environment details field

You can also opt in to additional signals about the environment. App access risk tells your app if there are other apps running that could be used to capture the screen, display overlays, or control the device. The Play Protect verdict tells you if Google Play Protect is enabled on the device and whether it has found known malware.

If you have opted in to the App Access Risk verdict or the Play Protect verdict in your Google Play Console, then your API response will include the`environmentDetails`field. The`environmentDetails`field can contain two values,`appAccessRiskVerdict`and`playProtectVerdict`.

#### App access risk verdict

Once enabled, the`environmentDetails`field in the[Play Integrity API payload](https://developer.android.com/google/play/integrity/verdict#returned-payload-format)will contain the new app access risk verdict.  

    {
      "requestDetails": { ... },
      "appIntegrity": { ... },
      "deviceIntegrity": { ... },
      "accountDetails": { ... },
      "environmentDetails": {
          "appAccessRiskVerdict": {
              // This field contains one or more responses, for example the following.
              "appsDetected": ["KNOWN_INSTALLED", "UNKNOWN_INSTALLED", "UNKNOWN_CAPTURING"]
          }
     }
    }

| **Note:** In standard requests, the app access risk verdict is only available when using Play Integrity API library version[1.4.0](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/release-notes#1-4-0)or higher for Kotlin or Java. App access risk increases the latency of standard requests, but latency-sensitive standard requests that don't require the app access risk verdict can use the`verdictOptOut`parameter to opt out of this verdict on a per-request basis. App access risk also requires the device to be running Android Marshmallow (API level 23) or higher.

If app access risk was evaluated,`appAccessRiskVerdict`contains the field`appsDetected`with one or more responses. These responses fall into one of the following two groups depending on the install source of the detected apps:

- **Play or system apps** : Apps that are installed by Google Play or preloaded by the device manufacturer on the device's system partition (identified with[`FLAG_SYSTEM`](https://developer.android.com/reference/android/content/pm/ApplicationInfo#FLAG_SYSTEM)). Responses for such apps are prefixed by`KNOWN_`.

- **Other apps** : Apps that are not installed by Google Play. This excludes apps preloaded on the system partition by the device manufacturer. Responses for such apps are prefixed by`UNKNOWN_`.

| **Note:** Detected apps that are**only** installed in another profile on the device, such as a[work profile](https://support.google.com/work/android/answer/6191949), will have the`UNKNOWN_`response prefix regardless of their install source. For example, if the app requesting the app access risk verdict is in a work profile and an app installed by Google Play in the user profile is running that could capture the screen, it will return`UNKNOWN_CAPTURING`instead of`KNOWN_CAPTURING`.

The following responses can be returned:

`KNOWN_INSTALLED`,`UNKNOWN_INSTALLED`
:   There are apps installed that match the corresponding install source.

`KNOWN_CAPTURING`,`UNKNOWN_CAPTURING`
:   There are apps running that have permissions enabled that could be used to view the screen while your app is running. This excludes any verified accessibility services known to Google Play running on the device.

`KNOWN_CONTROLLING`,`UNKNOWN_CONTROLLING`
:   There are apps running that have permissions enabled that could be used to control the device and directly control inputs into your app and could be used to capture inputs and outputs of your app. This excludes any verified accessibility services known to Google Play running on the device.

`KNOWN_OVERLAYS`,`UNKNOWN_OVERLAYS`
:   There are apps running that have permissions enabled that could be used to display overlays on your app. This excludes any verified accessibility services known to Google Play running on the device.

Empty (a blank value)

:   App access risk is not evaluated if a necessary requirement was missed. In this case the`appAccessRiskVerdict`field is empty. This could happen for several reasons, including the following:

    - The device is not trustworthy enough.
    - The device form factor is not a phone, tablet, or foldable.
    - The device is not running Android 6 (API level 23) or higher.
    - The version of your app installed on the device is unknown to Google Play.
    - The version of the Google Play Store on the device is outdated.
    - The user account does not have a Play license.
    - A standard request was used with the`verdictOptOut`parameter.
    - A standard request was used with a Play Integrity API library version that doesn't yet support app access risk for standard requests.

App access risk automatically excludes verified accessibility services that have been through an enhanced Google Play accessibility review (installed by any app store on the device). "Excluded" means that verified accessibility services running on the device won't return a capturing, controlling, or overlays response in the app access risk verdict. To request an enhanced Google Play accessibility review for your accessibility app, publish it on Google Play ensuring that your app has the`isAccessibilityTool`flag set to true in your app's manifest, or[request a review](https://issuetracker.google.com/issues/new?component=1152695&template=1949138).

##### Example app access risk verdicts

The following table gives some examples of app access risk verdicts and what they mean (this table does not list every possible result):

|                                  Example app access risk verdict response                                  |                                                                                                                                           Interpretation                                                                                                                                           |
|------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `appsDetected:` `["KNOWN_INSTALLED"]`                                                                      | There are only apps installed that are recognized by Google Play or preloaded on the system partition by the device manufacturer. There are no apps running that would result in the capturing, controlling, or overlays verdicts.                                                                 |
| `appsDetected:` `["KNOWN_INSTALLED",` `"UNKNOWN_INSTALLED",` `"UNKNOWN_CAPTURING"]`                        | There are apps installed by Google Play or preloaded on the system partition by the device manufacturer. There are other apps running and have permissions enabled that could be used to view the screen or capture other inputs and outputs.                                                      |
| `appsDetected:` `["KNOWN_INSTALLED",` `"KNOWN_CAPTURING",` `"UNKNOWN_INSTALLED",` `"UNKNOWN_CONTROLLING"]` | There are Play or system apps running that have permissions enabled that could be used to view the screen or capture other inputs and outputs. There are also other apps running that have permissions enabled that could be used to control the device and directly control inputs into your app. |
| `appAccessRiskVerdict: {}`                                                                                 | App access risk is not evaluated because a necessary requirement was missed. For example, the device was not trustworthy enough.                                                                                                                                                                   |

Depending on your risk level, you can decide what combination of verdicts are acceptable to proceed and what verdicts you want to take action on. The following code snippet illustrates an example of verifying that there are no apps running that could capture the screen or control your app:  

### Kotlin

```kotlin
val environmentDetails =
    JSONObject(payload).getJSONObject("environmentDetails")
val appAccessRiskVerdict =
    environmentDetails.getJSONObject("appAccessRiskVerdict")

if (appAccessRiskVerdict.has("appsDetected")) {
    val appsDetected = appAccessRiskVerdict.getJSONArray("appsDetected").toString()
    if (!appsDetected.contains("CAPTURING") && !appsDetected.contains("CONTROLLING")) {
        // Looks good!
    }
}
```

### Java

```java
JSONObject environmentDetails =
    new JSONObject(payload).getJSONObject("environmentDetails");
JSONObject appAccessRiskVerdict =
    environmentDetails.getJSONObject("appAccessRiskVerdict");

if (appAccessRiskVerdict.has("appsDetected")) {
    String appsDetected = appAccessRiskVerdict.getJSONArray("appsDetected").toString()
    if (!appsDetected.contains("CAPTURING") && !appsDetected.contains("CONTROLLING")) {
        // Looks good!
    }
}
```

##### Remediate app access risk verdicts

Depending on your risk level, you can decide what app access risk verdicts you want to take action on before letting the user complete a request or action. There are optional Google Play prompts you can show to the user after checking the app access risk verdict. You can show[CLOSE_UNKNOWN_ACCESS_RISK](https://developer.android.com/google/play/integrity/remediation#close-unknown-access-risk-dialog)to ask the user to close unknown apps causing the app access risk verdict or you can show[CLOSE_ALL_ACCESS_RISK](https://developer.android.com/google/play/integrity/remediation#close-all-access-risk-dialog)to ask the user to close all apps (known and unknown) causing the app access risk verdict.

#### Play Protect verdict

Once enabled, the`environmentDetails`field in the[Play Integrity API payload](https://developer.android.com/google/play/integrity/verdict#returned-payload-format)will contain the Play Protect verdict:  

    "environmentDetails": {
      "playProtectVerdict": "NO_ISSUES"
    }

`playProtectVerdict`can have one of the following values:

`NO_ISSUES`
:   Play Protect is turned on and did not find any app issues on the device.

`NO_DATA`
:   Play Protect is turned on but no scan has been performed yet. The device or the Play Store app may have been recently reset.

`POSSIBLE_RISK`
:   Play Protect is turned off.

`MEDIUM_RISK`
:   Play Protect is turned on and has found potentially harmful apps installed on the device.

`HIGH_RISK`
:   Play Protect is turned on and has found dangerous apps installed on the device.

`UNEVALUATED`

:   The Play Protect verdict was not evaluated.

    This could happen for several reasons, including the following:

    - The device is not trustworthy enough.
    - The user account does not have a Play license.

#### Guidance on using the Play Protect verdict

Your app's backend server can decide how to act based on the verdict based on your risk tolerance. Here are some suggestions and potential user actions:

`NO_ISSUES`
:   Play Protect is on and hasn't found any issues so no user action is required.

`POSSIBLE_RISK`and`NO_DATA`
:   When receiving these verdicts, ask the user to check that Play Protect is on and has performed a scan.`NO_DATA`should appear only in rare circumstances.

`MEDIUM_RISK`and`HIGH_RISK`
:   Depending on your risk tolerance, you can ask the user to launch Play Protect and take action on the Play Protect warnings. If the user can't fulfill these requirements you could block them from the server action.