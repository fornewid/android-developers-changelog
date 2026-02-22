---
title: https://developer.android.com/google/play/app-updates
url: https://developer.android.com/google/play/app-updates
source: md.txt
---

# How app updates work

This guide explains how the Android platform and Google Play handle app updates and discusses various options for developers who publish their apps on multiple app stores.

## How Android handles app updates

Every Android app has a unique[application ID](https://developer.android.com/studio/build/configure-app-module#set-application-id)that looks like a Java or Kotlin package name, such as`com.example.myapp`. This ID uniquely identifies each app on the device. Android devices can only have one app with a given application ID installed at a time.

In order for an update to be accepted by the Android platform, the following conditions must be met:

- The application ID of the update must be the same as the installed app.
- The signing certificate of the update must be the same as the signing certificate of the installed app, or it must contain a valid[proof-of-rotation](https://source.android.com/docs/security/features/apksigning/v3).
- The version code of the update must be higher or equal to the version code of the installed app.
- In some cases, the user may need to[accept the update](https://developer.android.com/reference/android/content/pm/PackageInstaller.SessionParams#setRequireUserAction(int)).

Note that there is no built-in prevention against different installers updating an app when the updates have the same signing certificate and the same or higher version code.

To install an app that doesn't meet the conditions above, a user must first uninstall the currently installed version, which erases all app data from the device.

## How Google Play updates apps

Google Play's approach to updating apps is based on the following principles:

- **Keep users up to date.**Keeping apps up to date is recommended to keep users safe from security issues and benefit from the latest feature improvements.
- **Respect user choice.**Google Play updates apps that are associated with users' accounts and based on their chosen update preferences, such as allowing or disallowing the use of metered data.
- **Respect developer choice.**Google Play uses the developers' configuration options when determining app updates.
- **Avoid wasted resources.**Conserve battery life by optimizing when updates are downloaded, and minimize data use using techniques such as compression and patching.

For a given app installed on a device, Google Play updates the app if it meets the following conditions:

- The app is[published on Google Play](https://developer.android.com/google/play/app-updates#published-on-play)with the same application ID.
- The published app's signing certificate matches the currently installed version's signing certificate, or it contains a valid[proof-of-rotation](https://source.android.com/docs/security/features/apksigning/v3).
- The app is[part of the user's library](https://developer.android.com/google/play/app-updates#user-library), or was preloaded by an OEM.
- The app is available for this user and this device, according to the developer-defined targeting options.
- The installed app is[out of date](https://developer.android.com/google/play/app-updates#out-of-date), compared to the version available on Google Play.

As long as these conditions are met, Google Play is able to update the app. The subsections below provide detail on some of the conditions listed.

Note that there are other times when Google Play downloads app content or performs maintenance on app binaries on developers' behalf without changing the Android version code---for example, when completing partial downloads or downloading on-demand[splits](https://developer.android.com/reference/tools/gradle-api/7.4/com/android/build/api/dsl/Splits).

### Published on Google Play

Google Play uses the application ID to uniquely identify applications published on Google Play. This condition is met if the installed app's application ID matches the application ID of an app published on Google Play.

### Part of user's library

This condition is met if one of the following is true:

- Any active Google Account on the device has previously acquired the app by tapping the install or purchase button on Google Play.
- The OEM preloaded the app as part of the system image.

Users also have the ability to manually remove apps from their[libraries](https://play.google.com/apps).

### Out of date

Google Play determines whether an app installed on a device is out of date by looking at the version code---if the version available for download on Google Play has a higher version code than the installed version, then Google Play considers the installed app to be out of date.

## Apps on multiple app stores

There are a few ways that you can control cross-store updates when you publish an app on multiple app stores. The following sections cover these options and their potential benefits and drawbacks.

### Prevent cross-store updates

You might want to prevent each app store from performing any cross-store app updates for your app. You might choose to do this if the content of your app is different on each app store. This can be achieved by publishing the app with two different application IDs, or by publishing the app with the same application ID and two different signing keys.

You might want to minimize reuse of your signing key to reduce risk from a key compromise, and so use a different app signing key for each app store. Doing so would prevent cross-store updates.

Regardless of which approach you choose, Android treats apps without a matching application ID and signing key as incompatible. A user wishing to switch from one store to another will need to delete the installed app---which will delete all data associated with that app---and reinstall from the other store.

### Allow cross-store updates

You might want to allow each app store to perform cross-store app updates for your app. You might choose to do this if you distribute your app with the same content on all app stores and you want to prioritize users being up to date. As long as you use the same application ID and signing keys across all app stores where you publish your app, then each app store has the ability to update installations of your app regardless of where the user downloaded the app initially.

However, this can lead to unpredictable behavior for your users depending on how each app store chooses to implement cross-store app updates. For example, a user might disable updates from one store, not realizing that another store might continue to provide updates.

If you previously allowed cross-store updates but you want to start preferring a particular update source when it's present on the device, you can release your app with a higher version code on your preferred app store and continue to release with lower version codes on other app stores. Once the higher version code update from the preferred source has been installed, the other app stores will not be able to cross-update on that device.