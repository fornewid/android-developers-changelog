---
title: https://developer.android.com/privacy-and-security/safetynet/recaptcha
url: https://developer.android.com/privacy-and-security/safetynet/recaptcha
source: md.txt
---

> [!WARNING]
> **Warning:** In order to help you safely grow your business, Google builds tools to protect your Android apps and games from abuse. We evolve these solutions as the abuse landscape changes. Delivering on this promise, Google is replacing the SafetyNet reCAPTCHA API with [reCAPTCHA](https://cloud.google.com/recaptcha/docs/instrument-android-apps). reCAPTCHA offers superior protection for mobile applications. We plan to gradually turn down the SafetyNet reCAPTCHA API starting in the third quarter of 2025. Details can be found in the [reCAPTCHA deprecation and shutdown policy](https://cloud.google.com/recaptcha/docs/deprecation-policy-mobile).

The SafetyNet service includes a reCAPTCHA API that you can use to protect your
app from malicious traffic.

reCAPTCHA is a free service that uses an advanced risk analysis engine to
protect your app from spam and other abusive actions. If the service suspects
that the user interacting with your app might be a bot instead of a human, it
serves a CAPTCHA that a human must solve before your app can continue executing.

> [!NOTE]
> **Note:** In order to use this API, your app must set `minSdkVersion` to `14` or higher in the `AndroidManifest.xml` file.

This document explains how to integrate the reCAPTCHA API from SafetyNet into
your app.

## Additional terms of service

By accessing or using the reCAPTCHA API, you agree to the [Google APIs Terms of
Service](https://developers.google.com/terms/) and to the following reCAPTCHA
Terms of Service.
Please read and understand all applicable terms and policies before accessing
the APIs.

### reCAPTCHA Terms of Service

You acknowledge and understand that the reCAPTCHA API works by collecting hardware and software information, such as device and application data and the results of integrity checks, and sending that data to Google for analysis. Pursuant to Section 3(d) of the Google APIs Terms of Service, you agree that if you use the APIs that it is your responsibility to provide any necessary notices or consents for the collection and sharing of this data with Google.

## Register a reCAPTCHA key pair

To register a key pair for use with the SafetyNet reCAPTCHA API, navigate to the
[reCAPTCHA Android signup site](https://www.google.com/recaptcha/admin/create),
then complete the following sequence of steps:

1. In the form that appears, provide the following information:

   - **Label:** A unique label for your key. Typically, you use the name of your company or organization.
   - **reCAPTCHA type:** Select **reCAPTCHA v2** , then **reCAPTCHA Android**.
   - **Packages:** Provide the package name of each app that uses this API key. In order for an app to use the API, the package name that you enter must exactly match the app's package name. Enter each package name on its own line.
   - **Owners:** Add an email address for each individual in your organization who monitors your app's reCAPTCHA assessments.
2. Select the **Accept the reCAPTCHA Terms of Service** checkbox.

3. **Send alerts to owners:** Select this checkbox if you want to receive
   emails about the reCAPTCHA API, then click
   **Submit**.

4. On the page that appears
   next, your public and private keys appear under **Site key** and **Secret
   key** , respectively. You use the site key when you [send the verify
   request](https://developer.android.com/privacy-and-security/safetynet/recaptcha#send-request), and you use the secret key when you [validate the
   user response token](https://developer.android.com/privacy-and-security/safetynet/recaptcha#validate-response).

## Add the SafetyNet API dependency

Before using the reCAPTCHA API, add the SafetyNet API to your project.
If you are using Android Studio, add this dependency to your app-level Gradle
file. For more information, see [SafetyNet API setup](https://developer.android.com/training/safetynet#before-you-begin).

## Use the reCAPTCHA API

This section describes how to call the reCAPTCHA API to send a CAPTCHA
verification request and receive the user response token.

### Send the verify request

To invoke the SafetyNet reCAPTCHA API, you call the
[`verifyWithRecaptcha()`](https://developers.google.com/android/reference/com/google/android/gms/safetynet/SafetyNetClient.html#verifyWithRecaptcha(java.lang.String))
method. Usually, this method corresponds to the user's selecting a UI element,
such as a button, in your activity.

When using the
`verifyWithRecaptcha()`
method in your app, you must do the following:

- Pass in your API site key as a parameter.
- Override the [`onSuccess()`](https://developers.google.com/android/reference/com/google/android/gms/tasks/OnSuccessListener.html#onSuccess(TResult)) and [`onFailure()`](https://developers.google.com/android/reference/com/google/android/gms/tasks/OnFailureListener.html#onFailure(java.lang.Exception)) methods to handle both possible outcomes of the verification request task. In particular, if the API passes an instance of [`ApiException`](https://developers.google.com/android/reference/com/google/android/gms/common/api/ApiException) into `onFailure()`, you need to handle each possible status code that you can retrieve using [`getStatusCode()`](https://developers.google.com/android/reference/com/google/android/gms/common/api/ApiException#getStatusCode()).

The following code snippet shows how to invoke this method:

### Kotlin

```kotlin
fun onClick(view: View) {
    SafetyNet.getClient(this).verifyWithRecaptcha(YOUR_API_SITE_KEY)
            .addOnSuccessListener(this as Executor, OnSuccessListener { response ->
                // Indicates communication with reCAPTCHA service was
                // successful.
                val userResponseToken = response.tokenResult
                if (response.tokenResult?.isNotEmpty() == true) {
                    // Validate the user response token using the
                    // https://developers.google.com/recaptcha/docs/verify.
                }
            })
            .addOnFailureListener(this as Executor, OnFailureListener { e ->
                if (e is ApiException) {
                    // An error occurred when communicating with the
                    // reCAPTCHA service. https://developers.google.com/android/reference/com/google/android/gms/safetynet/SafetyNetStatusCodes to
                    // handle the error appropriately.
                    Log.d(TAG, "Error: ${CommonStatusCodes.getStatusCodeString(e.statusCode)}")
                } else {
                    // A different, unknown type of error occurred.
                    Log.d(TAG, "Error: ${e.message}")
                }
            })
}
```

### Java

```java
public void onClick(View v) {
    SafetyNet.getClient(this).verifyWithRecaptcha(YOUR_API_SITE_KEY)
        .addOnSuccessListener((Executor) this,
            new OnSuccessListener<SafetyNetApi.RecaptchaTokenResponse>() {
                @Override
                public void onSuccess(SafetyNetApi.RecaptchaTokenResponse response) {
                    // Indicates communication with reCAPTCHA service was
                    // successful.
                    String userResponseToken = response.getTokenResult();
                    if (!userResponseToken.isEmpty()) {
                        // Validate the user response token using the
                        // https://developers.google.com/recaptcha/docs/verify.
                    }
                }
        })
        .addOnFailureListener((Executor) this, new OnFailureListener() {
                @Override
                public void onFailure(@NonNull Exception e) {
                    if (e instanceof ApiException) {
                        // An error occurred when communicating with the
                        // reCAPTCHA service. https://developers.google.com/android/reference/com/google/android/gms/safetynet/SafetyNetStatusCodes to
                        // handle the error appropriately.
                        ApiException apiException = (ApiException) e;
                        int statusCode = apiException.getStatusCode();
                        Log.d(TAG, "Error: " + CommonStatusCodes
                                .getStatusCodeString(statusCode));
                    } else {
                        // A different, unknown type of error occurred.
                        Log.d(TAG, "Error: " + e.getMessage());
                    }
                }
        });
}
```

### Validate the user response token

When the reCAPTCHA API executes the
`onSuccess()`
method, the user has successfully completed the CAPTCHA challenge. However, this
method only indicates that the user has solved the CAPTCHA correctly. You still
need to validate the user's response token from your backend server.

To learn how to validate the user's response token, see [Verifying the user's
response](https://developers.google.com/recaptcha/docs/verify).