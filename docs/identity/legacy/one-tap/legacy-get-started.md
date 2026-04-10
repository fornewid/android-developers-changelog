---
title: https://developer.android.com/identity/legacy/one-tap/legacy-get-started
url: https://developer.android.com/identity/legacy/one-tap/legacy-get-started
source: md.txt
---

| **Caution:** One Tap for Android is deprecated. To ensure the continued security and usability of your app, [migrate to
| Credential Manager](https://developer.android.com/identity/sign-in/credential-manager). Credential Manager supports passkey, password, and federated identity authentication (such as Sign-in with Google), stronger security, and a more consistent user experience.

Before you add One Tap sign-in to your app, set up your Google APIs and Android
projects.

## Set up your Google APIs console project

1. Open your project in the [API Console](https://console.cloud.google.com/), or create a project if you don't already have one.
2. On the OAuth consent screen page, make sure all of the information is complete and accurate. In particular, make sure you have specified the URLs of your app's privacy policy and terms of service.
3. On the Credentials page, create an Android client ID for your app if you don't already have one. You will need to specify your app's package name and SHA-1 signature.
   1. Go to the [Credentials page](https://console.cloud.google.com/apis/credentials).
   2. Click **Create credentials \> OAuth client ID**.
   3. Select the **Android** application type.
4. On the Credentials page, create a web application client ID if you don't already have one. You can leave the Authorized JavaScript Origins and Authorized redirect URIs fields blank. This client ID represents your authentication backend server. (You would use this client ID when calling Google APIs from your server, but you need it even if you don't.)
   1. Go to the [Credentials page](https://console.cloud.google.com/apis/credentials).
   2. Click **Create credentials \> OAuth client ID**.
   3. Select the **Web application** application type.

## Include dependencies in your Android project

1. In your project-level `build.gradle` file, make sure to include Google's Maven repository (`google()`) in both your `buildscript` and `allprojects` sections.
2. Add the dependencies for [Google Play services](https://developers.google.com/android)' authentication libraries
   to your module (app-level) build file (usually `app/build.gradle`):

       apply plugin: 'com.android.application'

       dependencies {
         // ...

         implementation 'com.google.android.gms:play-services-auth:21.3.0'
       }

## Optional: Associate your app with your site

If you have a web site that shares your app's sign-in backend,
[create and publish a digital asset links file](https://developers.google.com/identity/smartlock-passwords/android/associate-apps-and-sites)
so that users who sign in on one platform can easily sign in on the other.

## Next steps

[Add One Tap sign-in flows to your app](https://developer.android.com/identity/legacy/one-tap/legacy-get-saved-credentials).