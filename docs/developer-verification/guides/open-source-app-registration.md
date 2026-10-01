---
title: https://developer.android.com/developer-verification/guides/open-source-app-registration
url: https://developer.android.com/developer-verification/guides/open-source-app-registration
source: md.txt
---

This guide explains how to register your apps on open source platforms. The
process is similar to [distributing your app](https://developer.android.com/developer-verification/guides/full-distribution) through other stores. While you
don't have to register your app in order to continue distributing them on open
source platforms, doing so will let your users continue with the same install
experience they have today.

Before you begin, set up an [Android Developer Console](https://android.google.com/developerconsole/developers) account or [Google
Play Console](https://play.google.com/console/developers) account. If you don't have an account, sign up by following the
[developer verification guide](https://developer.android.com/developer-verification).

> [!NOTE]
> **Note:** If you are distributing the app through a store that integrates with the [Android Developer Console API](https://developer.android.com/developer-verification/guides/developer-console-api), the store can handle the package name and key registration process on your behalf. You still need a verified Android Developer Console account or Play Console account to link the app to your identity.

## Choose how users install your app

Depending on whether you verify and register, users can install your app in one
of two ways:

- **No changes for your users.** Register your apps to your verified identity so users can install it just like they always have.
- **Advanced flow setup.** If you prefer not to register your app, users can enable advanced flow on their device. This one-time setup allows them to install apps from unverified developers.

## Register a new app

Complete the following steps to register a new app.

1. In the [Android Developer Console](https://android.google.com/developerconsole/developers) or the Android developer verification tab on [Google Play Console](https://play.google.com/console/u/0/developers/android-developer-verification), click **Register package name**.
2. Enter the package name of your new app, and click **Next**.
3. Click **Add key** , and enter the SHA-256 certificate fingerprint of your signing key. See the [Help Center guide](https://support.google.com/android-developer-console/answer/16641489) for instructions on extracting the fingerprint. If the open source platform uses your signing key to distribute the app, you don't need to complete any further steps.
4. If the open source platform re-signs the app with their key, download the platform-signed APK after you publish the app on the platform.
5. Extract the SHA-256 certificate fingerprint from the APK.
6. In the console, go to your registered app, click **Add key** , and enter the extracted SHA-256 certificate fingerprint. If you receive a prompt to verify ownership, click **Verify** , and follow steps 9 through 12 in the [Register
   an existing app](https://developer.android.com/developer-verification/guides/open-source-app-registration#register-an-existing-app) section. This prompt appears in the rare case that the new app gets installed on 50 or more Android devices from the platform before you register the platform's key.

## Register an existing app

If the open source app platform uses your signing key to distribute the app,
follow the existing [package name registration guide](https://support.google.com/googleplay/android-developer/answer/16761053).

To register an existing app that the open source platform re-signs with their
key, complete the following steps:

1. Download the platform-signed APK from the open source platform.
2. Extract the SHA-256 certificate fingerprint from the APK. See the [Help
   Center guide](https://support.google.com/android-developer-console/answer/16641489) for instructions on extracting the fingerprint.
3. In the [Android Developer Console](https://android.google.com/developerconsole/developers) or the Android developer verification page on [Google Play Console](https://play.google.com/console/u/0/developers/android-developer-verification), click **Register package name**.
4. Enter the package name of your existing app, and click **Next**.
5. Click **Select key** . If the app has fewer than 50 known installs, click **Add key**, and enter the SHA-256 certificate fingerprint instead.
6. Select the extracted SHA-256 certificate fingerprint from the list of eligible fingerprints. If the fingerprint isn't listed, click **Show another
   way to register** , click **Show fingerprints for other keys**, and select the fingerprint from that list.
7. Click **Add key**.
8. Click **Upload APK**.
9. Copy the provided snippet, go to your app's source tree, create a file named `adi-registration.properties` in the `assets` folder, and paste the snippet in the file.
10. Publish the new app version containing the snippet to the open source platform.
11. Download the new APK version from the platform.
12. Upload the APK to the console.