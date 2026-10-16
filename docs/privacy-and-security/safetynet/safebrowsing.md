---
title: https://developer.android.com/privacy-and-security/safetynet/safebrowsing
url: https://developer.android.com/privacy-and-security/safetynet/safebrowsing
source: md.txt
---

The SafetyNet Safe Browsing API, a library powered by
[Google Play services](https://developers.google.com/android),
provides services for determining whether a URL has been marked as
a known threat by Google.

Your app can use this API to determine whether a particular URL has been
classified by Google as a known threat. Internally, SafetyNet implements a
client for the Safe Browsing Network Protocol v4 developed by Google. Both the
client code and the v4 network protocol were designed to preserve users'
privacy and keep battery and bandwidth consumption to a minimum. Use this API
to take full advantage of Google's Safe Browsing service on Android in the
most resource-optimized way, and without implementing its network protocol.

The new **version 5 (v5)** update introduces significant improvements in data
freshness and privacy through the use of **Oblivious HTTP**.

This document explains how to use the SafetyNet Safe Browsing Lookup API to
check a URL for known threats.

## Terms of service

By using the Safe Browsing API, you consent to be bound by the
[Terms of Service](https://developers.google.com/safe-browsing/terms).
Read and understand all applicable terms and policies before accessing
the Safe Browsing API.

## Request and register an Android API key

Before using the Safe Browsing API, create and register an Android API key. For
specific steps, see the page about
[getting started with Safe Browsing](https://developers.google.com/safe-browsing/v4/get-started).

In v5, you provide this API key when creating the `SafeBrowsingClient` instance.

## Add the SafetyNet API dependency

Before using the Safe Browsing API, add the SafetyNet API to your
project. If you are using Android Studio, add this dependency
to your app-level Gradle file. For more information, see
[Protect against security threats with SafetyNet](https://developer.android.com/training/safetynet#before-you-begin).

## Initialize the API

To use the Safe Browsing API, you must initialize the API by calling
[`initSafeBrowsing`](https://developers.google.com/android/reference/com/google/android/gms/safetynet/SafetyNetClient.html#initSafeBrowsing())
and waiting for it to complete. The following code snippet provides an example:

### Kotlin

    Tasks.await(SafetyNet.getClient(this).initSafeBrowsing)

### Java

    Tasks.await(SafetyNet.getClient(this).initSafeBrowsing);

> [!NOTE]
> **Note:** To minimize the impact of your app's initialization, call `initSafeBrowsing` as early as possible in your activity's [`onResume`](https://developer.android.com/reference/android/app/Activity#onResume()) method.

In v5, GmsCore offers the Safe Browsing client. You must obtain a
`SafeBrowsingClient` instance. We streamlined the API surface to increase
efficiency and reduce bloat.

    // Draft interface for the new client
    public interface SafeBrowsingClient extends HasApiKey<SafeBrowsingApiOptions> {
      Task<SafeBrowsingResponse> lookupUri(String uri, @ThreatType List<Integer> threatTypes, @Protocol int protocol);
      Task<SupportedThreatTypesResponse> getSupportedThreatTypes();
    }

## Request a URL check

Use the `lookupUri` method to check if a URI poses a threat. You must specify
the intended protocol, which can be either the **local blocklist** (v4) or
**real-time protection** (v5) .

### Send the URL check request

The API is independent to the scheme used, so you can pass
the URL with or without a scheme. For example, both

### Kotlin

    var url = "https://www.google.com"

### Java

    String url = "https://www.google.com";

and

### Kotlin

    var url = "www.google.com"

### Java

    String url = "www.google.com";


are valid.

The following code demonstrates how to send a URL check request:

### Kotlin

    SafetyNet.getClient(this).lookupUri(
           url,
           SAFE_BROWSING_API_KEY,
           SafeBrowsingThreat.TYPE_POTENTIALLY_HARMFUL_APPLICATION,
           SafeBrowsingThreat.TYPE_SOCIAL_ENGINEERING
    )
           .addOnSuccessListener(this) { sbResponse ->
               // Indicates communication with the service was successful.
               // Identify any detected threats.
               if (sbResponse.detectedThreats.isEmpty()) {
                   // No threats found.
               } else {
                   // Threats found!
               }
           }
           .addOnFailureListener(this) { e: Exception ->
               if (e is ApiException) {
                   // An error with the Google Play services API contains some
                   // additional details.
                   Log.d(TAG, "Error: ${CommonStatusCodes.getStatusCodeString(e.statusCode)}")

                   // Note: If the status code, s.statusCode,
                   // is SafetyNetStatusCode.SAFE_BROWSING_API_NOT_INITIALIZED,
                   // you need to call initSafeBrowsing(). It means either you
                   // haven't called initSafeBrowsing() before or that it needs
                   // to be called again due to an internal error.
               } else {
                   // A different, unknown type of error occurred.
                   Log.d(TAG, "Error: ${e.message}")
               }
           }

### Java

    SafetyNet.getClient(this).lookupUri(url,
             SAFE_BROWSING_API_KEY,
             SafeBrowsingThreat.TYPE_POTENTIALLY_HARMFUL_APPLICATION,
             SafeBrowsingThreat.TYPE_SOCIAL_ENGINEERING)
       .addOnSuccessListener(this,
           new OnSuccessListener<SafetyNetApi.SafeBrowsingResponse>() {
               @Override
               public void onSuccess(SafetyNetApi.SafeBrowsingResponse sbResponse) {
                   // Indicates communication with the service was successful.
                   // Identify any detected threats.
                   if (sbResponse.getDetectedThreats().isEmpty()) {
                       // No threats found.
                   } else {
                       // Threats found!
                   }
            }
       })
       .addOnFailureListener(this, new OnFailureListener() {
               @Override
               public void onFailure(@NonNull Exception e) {
                   // An error occurred while communicating with the service.
                   if (e instanceof ApiException) {
                       // An error with the Google Play services API contains some
                       // additional details.
                       ApiException apiException = (ApiException) e;
                       Log.d(TAG, "Error: " + CommonStatusCodes
                           .getStatusCodeString(apiException.getStatusCode()));

                       // Note: If the status code, apiException.getStatusCode(),
                       // is SafetyNetStatusCode.SAFE_BROWSING_API_NOT_INITIALIZED,
                       // you need to call initSafeBrowsing(). It means either you
                       // haven't called initSafeBrowsing() before or that it needs
                       // to be called again due to an internal error.
                   } else {
                       // A different, unknown type of error occurred.
                       Log.d(TAG, "Error: " + e.getMessage());
                   }
               }
       });

The updated lookupUri signature takes the URI, a list of threat types,
and the protocol.

    val threatTypes = listOf(ThreatType.TYPE_SOCIAL_ENGINEERING, ThreatType.TYPE_MALWARE)
    val protocol = Protocol.REAL_TIME // or Protocol.LOCAL_BLOCK_LIST

    safeBrowsingClient.lookupUri(url, threatTypes, protocol)
        .addOnSuccessListener { response ->
            if (response.detectedThreats.isEmpty()) {
                // No threats found
            } else {
                // Threats detected!
            }
        }

### Read the URL check response

Using the returned
[`SafetyNetApi.SafeBrowsingResponse`](https://developers.google.com/android/reference/com/google/android/gms/safetynet/SafetyNetApi.SafeBrowsingResponse)
object, call its
[`getDetectedThreats`](https://developers.google.com/android/reference/com/google/android/gms/safetynet/SafetyNetApi.SafeBrowsingResponse.html#getDetectedThreats())
method, which returns a list of
[`SafeBrowsingThreat`](https://developers.google.com/android/reference/com/google/android/gms/safetynet/SafeBrowsingThreat)
objects. If the returned list is empty, the API didn't detect any known threats.
If the list is not empty, call
[`getThreatType`](https://developers.google.com/android/reference/com/google/android/gms/safetynet/SafeBrowsingThreat.html#getThreatType())
on each element in the list to determine which known threats the API detected.

To see suggested warning language, see the
[Safe Browsing API Developer's Guide](https://developers.google.com/safe-browsing/v4/usage-limits#suggested-warning-language).

### Specify threat types of interest

The constants in the `SafeBrowsingThreat` class contain the
currently supported threat types:

| Threat type | Definition |
|---|---|
| `TYPE_POTENTIALLY_HARMFUL_APPLICATION` | This threat type identifies URLs of pages that are flagged as containing potentially harmful applications. |
| `TYPE_SOCIAL_ENGINEERING` | This threat type identifies URLs of pages that are flagged as containing social engineering threats. |

When using the API, you add threat type constants as arguments. You can add as
many threat type constants as your app requires, but you can only use constants
that aren't marked as deprecated.

## Shut down your Safe Browsing session

If your app doesn't need to use the Safe Browsing API for a prolonged period,
check all the necessary URLs within your app and then shut down your
Safe Browsing session using the
[`shutdownSafeBrowsing`](https://developers.google.com/android/reference/com/google/android/gms/safetynet/SafetyNetClient.html#shutdownSafeBrowsing())
method:

### Kotlin

    SafetyNet.getClient(this).shutdownSafeBrowsing()

### Java

    SafetyNet.getClient(this).shutdownSafeBrowsing();

We recommend that you call `shutdownSafeBrowsing` in your
activity's [`onPause`](https://developer.android.com/reference/android/app/Activity#onPause()) method
and that you call
[`initSafeBrowsing`](https://developers.google.com/android/reference/com/google/android/gms/safetynet/SafetyNetClient.html#initSafeBrowsing())
in your activity's `onResume` method. However,
make sure that `initSafeBrowsing` has finished executing before
calling
[`lookupUri`](https://developers.google.com/android/reference/com/google/android/gms/safetynet/SafetyNetClient.html#lookupUri(java.lang.String,%20java.lang.String,%20int...))
By making sure that your session is always
fresh, you reduce the possibility of internal errors in your app.

## Real-time protection details

The v5 update introduces a **real-time protection** mode that circumvents data
staleness issues (which could reach 20-50 minutes in v4).
It shifts from an **allow-by-default** to a **check-by-default** protocol,
enhancing protection against fast-propagating threats.
In real-time mode, clients maintain a local database and a **Global Cache of
likely-benign sites** to provide near-real-time protection with the freshest
threat data.

> [!NOTE]
> **Note:** The client periodically syncs a global cache to reduce network latency for common sites.

## Supported threat types

The API lets you choose which threat types are important for your needs.
The v5 API supports a wider range of threat types:

| Threat Type Constant | Description |
|---|---|
| NO_THREAT | No threat. |
| TYPE_MALWARE | General malware threats. |
| TYPE_UNWANTED_SOFTWARE | Unwanted software or applications. |
| TYPE_POTENTIALLY_HARMFUL_APPLICATION | Apps that may harm the device or user. |
| TYPE_SOCIAL_ENGINEERING | Phishing and other deceptive sites. |
| TYPE_TRICK_TO_BILL | Pages that trick users into billing actions. |
| TYPE_BETTER_ADS_VIOLATION | Sites violating better ads standards. |
| TYPE_MALWARE_OFFLINE | Offline malware. |
| TYPE_ABUSIVE_EXPERIENCE_VIOLATION | Violations that result in a bad experience for the user. |
| TYPE_HIGH_CONFIDENCE_ALLOW_LIST | High confidence allow list |

## Data collected by the SafetyNet Safe Browsing API

The SafetyNet Safe Browsing API collects the following data automatically when
it communicates with the Safe Browsing service on Android:

| Data | Description |
|---|---|
| App Activity | Collects hash prefix of URLs after a local hash prefix match for purposes of detecting malicious URLs. |

The SafetyNet Safe Browsing API collects the hash prefix of URLs for detecting
malicious URLs. Version 5 implements **Oblivious HTTP** to further protect
user data during these lookups.

> [!NOTE]
> **Note:** Safe Browsing v5 is designed to migrate from v4 without requiring a reset of the local database.

While we aim to be as transparent as possible, you are solely responsible for
deciding how to respond to
[Google Play's data safety section form](https://support.google.com/googleplay/android-developer/answer/10787469)
regarding your app's user data collection, sharing, and security practices.