---
title: https://developer.android.com/privacy-and-security/safetynet/verify-apps
url: https://developer.android.com/privacy-and-security/safetynet/verify-apps
source: md.txt
---

# SafetyNet Verify Apps API

| **Note:** We recommend using the Play Integrity API to check the status of Play Protect on a device because it offers several benefits over the SafetyNet Verify Apps API.[Learn more](https://developer.android.com/google/play/integrity/overview).

The SafetyNet Verify Apps API, a library powered by[Google Play services](https://developers.google.com/android), lets your app interact programmatically with the[Verify Apps](https://support.google.com/accounts/answer/2812853)feature on a device, protecting the device against potentially harmful apps.

If your app handles sensitive user data, such as financial information, it's important to confirm that the user's device is protected against malicious apps and doesn't have any apps that could impersonate your app or perform other malicious actions. If the device's security doesn't meet the minimum security posture, you can disable functionality within your own app to reduce the danger to the user.

As part of its continuing commitment to make the Android ecosystem as safe as possible, Google monitors and profiles the behavior of Android apps. If the Verify Apps feature detects a potentially dangerous app, all users who have installed the app are notified and encouraged to promptly uninstall the app. This process protects the security and privacy of these users.

The SafetyNet Verify Apps API lets you leverage this feature to protect your app's data. By using this API, you can determine whether a user's device is protected by the Verify Apps feature, encourage users who aren't already using the feature to opt in to its protection, and identify any known potentially harmful apps that are installed on the device.

## Additional terms of service

By accessing or using the SafetyNet APIs, you agree to the[Google APIs Terms of Service](https://developers.google.com/terms/)and to the following Verify Apps API Terms of Service. Please read and understand all applicable terms and policies before accessing the APIs.  

### Verify Apps API Terms of Service

The analyses of apps that identify potential harmful apps may yield both false positives and false negatives. The results (or lack thereof) returned from this API suite are presented to the best of our understanding. You acknowledge and understand that the results returned by this SafetyNet API suite are not guaranteed to be accurate at all times.

## Add the SafetyNet API dependency

Before using the Verify Apps API, add the SafetyNet API to your project. If you are using Android Studio, add this dependency to your app-level Gradle file. For more information, see[SafetyNet API setup](https://developer.android.com/training/safetynet#before-you-begin).

## Enable app verification

The SafetyNet Verify Apps API provides two methods for enabling the Verify Apps feature. You can determine whether app verification is enabled using[`isVerifyAppsEnabled()`](https://developers.google.com/android/reference/com/google/android/gms/safetynet/SafetyNetClient#isVerifyAppsEnabled()), and you can request enabling of app verification using[`enableVerifyApps()`](https://developers.google.com/android/reference/com/google/android/gms/safetynet/SafetyNetClient#enableVerifyApps()).

The difference between these two methods is that while`isVerifyAppsEnabled()`reports the current status of the Verify Apps feature,`enableVerifyApps()`explicitly asks the user for consent to use the feature. If you want your app to just be aware of the feature's status to make a security-driven decision, your app should call`isVerifyAppsEnabled()`. However, if you want to be sure that your app can list potentially harmful installed apps, you should call`enableVerifyApps()`instead.

### Determine whether app verification is enabled

The asynchronous`isVerifyAppsEnabled()`method lets your app determine whether the user is enrolled in the Verify Apps feature. This method returns a[`VerifyAppsUserResponse`](https://developers.google.com/android/reference/com/google/android/gms/safetynet/SafetyNetApi.VerifyAppsUserResponse)object, which contains information regarding all actions that the user has taken related to the Verify Apps feature, including enabling it.

The following code snippet shows how to create the callback associated with this method:  

### Kotlin

```kotlin
SafetyNet.getClient(this)
        .isVerifyAppsEnabled
        .addOnCompleteListener { task ->
            if (task.isSuccessful) {
                if (task.result.isVerifyAppsEnabled) {
                    Log.d("MY_APP_TAG", "The Verify Apps feature is enabled.")
                } else {
                    Log.d("MY_APP_TAG", "The Verify Apps feature is disabled.")
                }
            } else {
                Log.e("MY_APP_TAG", "A general error occurred.")
            }
        }
```

### Java

```java
SafetyNet.getClient(this)
    .isVerifyAppsEnabled()
    .addOnCompleteListener(new OnCompleteListener<VerifyAppsUserResponse>() {
        @Override
        public void onComplete(Task<VerifyAppsUserResponse> task) {
            if (task.isSuccessful()) {
                VerifyAppsUserResponse result = task.getResult();
                if (result.isVerifyAppsEnabled()) {
                    Log.d("MY_APP_TAG", "The Verify Apps feature is enabled.");
                } else {
                    Log.d("MY_APP_TAG", "The Verify Apps feature is disabled.");
                }
            } else {
                Log.e("MY_APP_TAG", "A general error occurred.");
            }
        }
    });
```

### Request enabling of app verification

The asynchronous`enableVerifyApps()`method lets your app invoke a dialog requesting that the user enable the Verify Apps feature. This method returns a`VerifyAppsUserResponse`object, which contains information regarding all actions that the user has taken related to the Verify Apps feature, including whether they've given consent to enable it.

The following code snippet shows how to create the callback associated with this method:  

### Kotlin

```kotlin
SafetyNet.getClient(this)
        .enableVerifyApps()
        .addOnCompleteListener { task ->
            if (task.isSuccessful) {
                if (task.result.isVerifyAppsEnabled) {
                    Log.d("MY_APP_TAG", "The user gave consent to enable the Verify Apps feature.")
                } else {
                    Log.d(
                            "MY_APP_TAG",
                            "The user didn't give consent to enable the Verify Apps feature."
                    )
                }
            } else {
                Log.e("MY_APP_TAG", "A general error occurred.")
            }
        }
```

### Java

```java
SafetyNet.getClient(this)
    .enableVerifyApps()
    .addOnCompleteListener(new OnCompleteListener<VerifyAppsUserResponse>() {
        @Override
        public void onComplete(Task<VerifyAppsUserResponse> task) {
            if (task.isSuccessful()) {
                VerifyAppsUserResponse result = task.getResult();
                if (result.isVerifyAppsEnabled()) {
                    Log.d("MY_APP_TAG", "The user gave consent " +
                          "to enable the Verify Apps feature.");
                } else {
                    Log.d("MY_APP_TAG", "The user didn't give consent " +
                          "to enable the Verify Apps feature.");
                }
            } else {
                Log.e("MY_APP_TAG", "A general error occurred.");
            }
        }
    });
```

Your app can encounter one or more unusual conditions when using this method:

- If the Verify Apps feature is already enabled, the dialog doesn't appear, and the API behaves as if the user gave consent to enable this feature.
- If the user navigates away from the dialog, the dialog is destroyed, and the API assumes that the user didn't give consent to enable this feature.
- If your app and another app call this method simultaneously, only one dialog appears, and all apps receive identical return values from the method.

## List potentially harmful installed apps

The asynchronous[`listHarmfulApps()`](https://developers.google.com/android/reference/com/google/android/gms/safetynet/SafetyNetClient#listHarmfulApps())method lets you obtain a list of any known potentially harmful apps that the user has installed on their device. This list includes categories for the identified potentially harmful apps so that your app can take appropriate action.
| **Note:** This method provides only the potentially harmful apps that are associated with the currently active user or account.

The following code snippet shows how to create the callback associated with this method:  

### Kotlin

```kotlin
SafetyNet.getClient(this)
        .listHarmfulApps()
        .addOnCompleteListener { task ->
            Log.d(TAG, "Received listHarmfulApps() result")

            if (task.isSuccessful) {
                val result = task.result
                val scanTimeMs = result.lastScanTimeMs

                val appList = result.harmfulAppsList
                if (appList?.isNotEmpty() == true) {
                    Log.e("MY_APP_TAG", "Potentially harmful apps are installed!")

                    for (harmfulApp in appList) {
                        Log.e("MY_APP_TAG", "Information about a harmful app:")
                        Log.e("MY_APP_TAG", "  APK: ${harmfulApp.apkPackageName}")
                        Log.e("MY_APP_TAG", "  SHA-256: ${harmfulApp.apkSha256}")

                        // Categories are defined in VerifyAppsConstants.
                        Log.e("MY_APP_TAG", "  Category: ${harmfulApp.apkCategory}")
                    }
                } else {
                    Log.d("MY_APP_TAG", "There are no known potentially harmful apps installed.")
                }
            } else {
                Log.d(
                        "MY_APP_TAG",
                        "An error occurred. Call isVerifyAppsEnabled() to ensure that the user "
                                + "has consented."
                )
            }
        }
```

### Java

```java
SafetyNet.getClient(this)
    .listHarmfulApps()
    .addOnCompleteListener(new OnCompleteListener<HarmfulAppsResponse>() {
        @Override
        public void onComplete(Task<HarmfulAppsResponse> task) {
            Log.d(TAG, "Received listHarmfulApps() result");

            if (task.isSuccessful()) {
                HarmfulAppsResponse result = task.getResult();
                long scanTimeMs = result.getLastScanTimeMs();

                List<HarmfulAppsData> appList = result.getHarmfulAppsList();
                if (appList.isEmpty()) {
                    Log.d("MY_APP_TAG", "There are no known " +
                          "potentially harmful apps installed.");
                } else {
                    Log.e("MY_APP_TAG",
                          "Potentially harmful apps are installed!");

                    for (HarmfulAppsData harmfulApp : appList) {
                        Log.e("MY_APP_TAG", "Information about a harmful app:");
                        Log.e("MY_APP_TAG",
                              "  APK: " + harmfulApp.apkPackageName);
                        Log.e("MY_APP_TAG",
                              "  SHA-256: " + harmfulApp.apkSha256);

                        // Categories are defined in VerifyAppsConstants.
                        Log.e("MY_APP_TAG",
                              "  Category: " + harmfulApp.apkCategory);
                    }
                }
            } else {
                Log.d("MY_APP_TAG", "An error occurred. " +
                      "Call isVerifyAppsEnabled() to ensure " +
                      "that the user has consented.");
            }
        }
    });
```