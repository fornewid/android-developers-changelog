---
title: https://developer.android.com/identity/legacy/gsi
url: https://developer.android.com/identity/legacy/gsi
source: md.txt
---

# Start integrating Google Sign-In into your Android app

| **Warning:**
|
| **The Google Sign-In for Android API is outdated and no longer supported.** To ensure the continued security and usability of your app,[migrate your Sign in with Google implementation to Credential Manager](https://developer.android.com/identity/sign-in/credential-manager-siwg)today. Credential Manager supports passkey, password, and federated identity authentication (such as Sign-in with Google), stronger security, and a more consistent user experience.
|
| **For Wear developers:**Credential Manager is supported in Wear OS 5.1 and later on selected watches. Developers actively supporting Wear OS 3, 4 and 5.0 devices with Sign in with Google should continue using Google Sign-in for Android for your Wear applications. Sign in with Google support will be available on Credential Manager APIs for these versions of WearOS at a later date.

Before you can start integrating Google Sign-In in your own app, you must configure a Google API Console project and set up your Android Studio project. The steps on this page do just that. The[next steps](https://developer.android.com/identity/legacy/gsi#next-steps)then describe how to integrate Google Sign-In into your app.

## Prerequisites

Google Sign-In for Android has the following requirements:

- A compatible Android-powered device that runs Android 6.0 or newer and includes the Google Play Store or an emulator with an Android Virtual Device (AVD) that runs the Google APIs platform based on Android 4.2.2 or newer and has Google Play services version 15.0.0 or newer.
- The latest version of the Android SDK, including the SDK Tools component. The SDK is available from the Android SDK Manager in Android Studio.
- A project configured to compile against Android 6.0 (Marshmallow) or newer.

This guide is written for users of Android Studio, which is the recommended development environment.

## Add Google Play services

In your project's top-level`build.gradle`file, verify that Google's Maven repository is included:  

    allprojects {
        repositories {
            google()

            // If you're using a version of Gradle lower than 4.1, you must instead use:
            // maven {
            //     url 'https://maven.google.com'
            // }
        }
    }

Then, in your app-level`build.gradle`file, declare[Google Play services](https://developers.google.com/android)as a dependency:  

    apply plugin: 'com.android.application'
        ...

        dependencies {
            implementation 'com.google.android.gms:play-services-auth:21.3.0'
        }

## Configure a Google API Console project

1. Open your project in the[API console](https://console.cloud.google.com/), or create a project if you don't already have one.
2. On the**OAuth consent screen**page, make sure all of the information is complete and accurate.
3. On the**Credentials** page, create an**Android** type client ID for your app if you don't already have one. You will need to specify your app's package name and SHA-1 certificate fingerprint. See[Authenticating Your Client](https://developers.google.com/android/guides/client-auth)for more information.

## Get your backend server's OAuth 2.0 client ID

If your app[authenticates with a backend server](https://developers.google.com/identity/sign-in/android/backend-auth)or[accesses Google APIs from your backend server](https://developer.android.com/identity/legacy/gsi/offline-access), you need to get the OAuth 2.0 client ID that represents your backend server.

To create a client ID for your server:

1. Open your project in the[API console](https://console.cloud.google.com/).

2. On the**Credentials** page, create a**Web application** type client ID. Take note of the client ID string, which you will need to pass to the`requestIdToken`or`requestServerAuthCode`method when you create the`GoogleSignInOptions`object.

## Next steps

Now that you have configured a Google API Console project and set up your Android Studio project, you can[integrate Google Sign-In](https://developer.android.com/identity/legacy/gsi/legacy-sign-in)into your app.