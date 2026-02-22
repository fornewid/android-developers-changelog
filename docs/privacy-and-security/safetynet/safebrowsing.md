---
title: https://developer.android.com/privacy-and-security/safetynet/safebrowsing
url: https://developer.android.com/privacy-and-security/safetynet/safebrowsing
source: md.txt
---

# SafetyNet Safe Browsing API

The SafetyNet Safe Browsing API, a library powered by[Google Play services](https://developers.google.com/android), provides services for determining whether a URL has been marked as a known threat by Google.

Your app can use this API to determine whether a particular URL has been classified by Google as a known threat. Internally, SafetyNet implements a client for the Safe Browsing Network Protocol v4 developed by Google. Both the client code and the v4 network protocol were designed to preserve users' privacy and keep battery and bandwidth consumption to a minimum. Use this API to take full advantage of Google's Safe Browsing service on Android in the most resource-optimized way, and without implementing its network protocol.

This document explains how to use the SafetyNet Safe Browsing Lookup API to check a URL for known threats.

## Terms of service

By using the Safe Browsing API, you consent to be bound by the[Terms of Service](https://developers.google.com/safe-browsing/terms). Please read and understand all applicable terms and policies before accessing the Safe Browsing API.

## Request and register an Android API key

Before using the Safe Browsing API, create and register an Android API key. For specific steps, see the page about[getting started with Safe Browsing](https://developers.google.com/safe-browsing/v4/get-started).

## Add the SafetyNet API dependency

Before using the Safe Browsing API, add the SafetyNet API to your project. If you are using Android Studio, add this dependency to your app-level Gradle file. For more information, see[Protect against security threats with SafetyNet](https://developer.android.com/training/safetynet#before-you-begin).

## Initialize the API

To use the Safe Browsing API, you must initialize the API by calling[`initSafeBrowsing()`](https://developers.google.com/android/reference/com/google/android/gms/safetynet/SafetyNetClient.html#initSafeBrowsing())and waiting for it to complete. The following code snippet provides an example:  

### Kotlin

```kotlin
Tasks.await(SafetyNet.getClient(this).initSafeBrowsing())
```

### Java

```java
Tasks.await(SafetyNet.getClient(this).initSafeBrowsing());
```
| **Note:** To minimize the impact of your app's initialization, call`initSafeBrowsing()`as early as possible in your activity's[`onResume()`](https://developer.android.com/reference/android/app/Activity#onResume())method.

## Request a URL check

Your app can use a URL check to determine whether a URL poses a known threat. Some threat types might not be of interest to your particular app. The API lets you choose which threat types are important for your needs. You can specify multiple known threat types.

### Send the URL check request

The API is agnostic to the scheme used, so you can pass the URL with or without a scheme. For example, both  

### Kotlin

```kotlin
var url = "https://www.google.com"
```

### Java

```java
String url = "https://www.google.com";
```

and  

### Kotlin

```kotlin
var url = "www.google.com"
```

### Java

```java
String url = "www.google.com";
```

are valid.

The following code demonstrates how to send a URL check request:  

### Kotlin

```kotlin
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
               // An error with the Google Play Services API contains some
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
```

### Java

```java
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
                   // An error with the Google Play Services API contains some
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
```

### Read the URL check response

Using the returned[`SafetyNetApi.SafeBrowsingResponse`](https://developers.google.com/android/reference/com/google/android/gms/safetynet/SafetyNetApi.SafeBrowsingResponse)object, call its[`getDetectedThreats()`](https://developers.google.com/android/reference/com/google/android/gms/safetynet/SafetyNetApi.SafeBrowsingResponse.html#getDetectedThreats())method, which returns a list of[`SafeBrowsingThreat`](https://developers.google.com/android/reference/com/google/android/gms/safetynet/SafeBrowsingThreat)objects. If the returned list is empty, the API didn't detect any known threats. If the list is not empty, call[`getThreatType()`](https://developers.google.com/android/reference/com/google/android/gms/safetynet/SafeBrowsingThreat.html#getThreatType())on each element in the list to determine which known threats the API detected.

To see suggested warning language, see the[Safe Browsing API Developer's Guide](https://developers.google.com/safe-browsing/v4/usage-limits#suggested-warning-language).

### Specify threat types of interest

The constants in the`SafeBrowsingThreat`class contain the currently supported threat types:

|              Threat type               |                                                 Definition                                                 |
|----------------------------------------|------------------------------------------------------------------------------------------------------------|
| `TYPE_POTENTIALLY_HARMFUL_APPLICATION` | This threat type identifies URLs of pages that are flagged as containing potentially harmful applications. |
| `TYPE_SOCIAL_ENGINEERING`              | This threat type identifies URLs of pages that are flagged as containing social engineering threats.       |

When using the API, you add threat type constants as arguments. You can add as many threat type constants as your app requires, but you can only use constants that aren't marked as deprecated.

## Shut down your Safe Browsing session

If your app doesn't need to use the Safe Browsing API for a prolonged period, check all the necessary URLs within your app and then shut down your Safe Browsing session using the[`shutdownSafeBrowsing()`](https://developers.google.com/android/reference/com/google/android/gms/safetynet/SafetyNetClient.html#shutdownSafeBrowsing())method:  

### Kotlin

```kotlin
SafetyNet.getClient(this).shutdownSafeBrowsing()
```

### Java

```java
SafetyNet.getClient(this).shutdownSafeBrowsing();
```

We recommend that you call`shutdownSafeBrowsing()`in your activity's[`onPause()`](https://developer.android.com/reference/android/app/Activity#onPause())method and that you call[`initSafeBrowsing()`](https://developers.google.com/android/reference/com/google/android/gms/safetynet/SafetyNetClient.html#initSafeBrowsing())in your activity's`onResume()`method. However, make sure that`initSafeBrowsing()`has finished executing before calling[`lookupUri()`](https://developers.google.com/android/reference/com/google/android/gms/safetynet/SafetyNetClient.html#lookupUri(java.lang.String,%20java.lang.String,%20int...)). By making sure that your session is always fresh, you reduce the possibility of internal errors in your app.

## Data collected by the SafetyNet Safe Browsing API

The SafetyNet Safe Browsing API collects the following data automatically when it communicates with the Safe Browsing service on Android:

|     Data     |                                              Description                                               |
|--------------|--------------------------------------------------------------------------------------------------------|
| App Activity | Collects hash prefix of URLs after a local hash prefix match for purposes of detecting malicious URLs. |

While we aim to be as transparent as possible, you are solely responsible for deciding how to respond to[Google Play's data safety section form](https://support.google.com/googleplay/android-developer/answer/10787469)regarding your app's user data collection, sharing, and security practices.