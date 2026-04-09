---
title: Privacy in Android 11  |  Platform  |  Android Developers
url: https://developer.android.com/about/versions/11/privacy
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Platform](https://developer.android.com/about)
* [Releases](https://developer.android.com/about/versions)

Stay organized with collections

Save and categorize content based on your preferences.




### Privacy in Android 11

Android 11 builds upon earlier versions of Android, adding features and updates to keep users secure and increase transparency and control. All developers should review the privacy features and test their apps. Impacts can vary based on each app's core functionality, targeting, and other factors.

To learn more about the key changes that take effect in Android 11, look through the following sections.

## Top privacy changes

This table summarizes the key changes related to privacy that are taking effect in Android 11.

|  | Privacy change | Apps affected | Mitigation strategy |
| --- | --- | --- | --- |
|  | **Scoped storage enforcement** Apps that target Android 11 or higher are always subject to scoped storage behaviors | Apps that target Android 11 or higher, as well as apps that target Android 10 and haven't set `requestLegacyExternalStorage` to `true` to opt out of scoped storage | Update your app to work with scoped storage  [Learn more about the scoped storage changes](/about/versions/11/privacy/storage) |
|  | **One-time permissions** Users can grant temporary access to location, microphone, and camera using one-time permissions | Apps that run on Android 11 or higher and request location, microphone, or camera permissions | Check that your app has a permission before attempting to access data that's guarded by that permission [Follow best practices for requesting permissions](/training/permissions/requesting) |
|  | **Permissions auto-reset** If users haven't interacted with an app for a few months on Android 11 or higher, the system auto-resets the app's sensitive permissions | Apps that target Android 11 or higher and perform most of their work in the background | Ask the user to prevent the system from resetting your app's permissions  [Learn more about permissions auto-reset](/about/versions/11/privacy/permissions#auto-reset) |
|  | **Background location access** Android 11 changes how users can grant the background location permission to apps | Apps that target Android 11 or higher and need access to [background location](/training/location/permissions#background) | Request foreground (coarse or fine) and background location permissions incrementally in separate calls to the permission request method. When necessary, explain the benefits that users receive for granting that permission  [Learn more about background location access in Android 11](/about/versions/11/privacy/location#background-location) |
|  | **Package visibility** Android 11 changes how apps query and interact with other installed apps on the same device | Apps that target Android 11 or higher and interact with other installed apps on a device | Add the [`<queries>`](/guide/topics/manifest/queries-element) element to your app's manifest  [Learn more about package visibility](/about/versions/11/privacy/package-visibility) |
|  | **Foreground services** Android 11 changes how foreground services can access location, camera, and microphone data | Apps that run on Android 11 or higher and access location, the camera, or the microphone in a foreground service | Declare the `camera` and `microphone` foreground service types for the foreground services that require access to the camera and microphone, respectively. Be aware, however, that foreground services that start while the app is in the background usually cannot access location, camera, or microphone.  [Learn more about the changes to foreground services](/about/versions/11/privacy/foreground-services) |

## Get started with privacy updates

1. **Review the privacy features:** Assess your app. Look for how your app
   [stores files and user data](/about/versions/11/privacy/storage),
   [requests permissions](/about/versions/11/privacy/permissions),
   [requests location](/about/versions/11/privacy/location). In addition, look for ways
   that your app [interacts with other
   apps](/about/versions/11/privacy/package-visibility), consider [performing an
   audit](/about/versions/11/privacy/data-access-auditing) of the data that your app accesses, and determine whether your app needs to
   update how it uses [foreground
   services](/about/versions/11/privacy/foreground-services).
2. **Test your app on Android 11:** Run your app on Android 11. Use
   [app compatibility tools](/guide/app-compatibility/test-debug) to evaluate how
   individual system changes affect your app.
3. **Update your app:** Targeting Android 11 if possible, test with
   users and publish an update.

## Android 11 news and videos