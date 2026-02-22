---
title: https://developer.android.com/guide/playcore/in-app-updates
url: https://developer.android.com/guide/playcore/in-app-updates
source: md.txt
---

When your users keep your app up to date on their devices, they can try new
features, as well as benefit from performance improvements and bug fixes.
Although some users enable background updates when their device is connected to
an unmetered connection, other users might need to be reminded to install
updates. In-app updates is a Google Play Core libraries feature that prompts
active users to update your app.

The in-app updates feature is supported on devices running Android 5.0 (API
level 21) or higher. Additionally, in-app updates are only supported for Android
mobile devices, Android tablets, and ChromeOS devices.
| **Note:** In-app updates are not compatible with apps that use APK expansion files (`.obb` files).

## Update flows

Your app can use the Google Play Core libraries to support the following UX
flows for in-app updates:

### Flexible updates

Flexible updates provide background download and installation with graceful
state monitoring. This UX flow is appropriate when it's acceptable for the user
to use the app while downloading the update. For example, you might want to
encourage users to try a new feature that's not critical to the core
functionality of your app.
![](https://developer.android.com/static/images/app-bundle/flexible_flow.png)


**Figure 1.** An example of a flexible update flow.

<br />

### Immediate updates

Immediate updates are fullscreen UX flows that require the user to update and
restart the app in order to continue using it. This UX flow is best for cases
where an update is critical to the core functionality of your app. After a user
accepts an immediate update, Google Play handles the update installation and app
restart.
![](https://developer.android.com/static/images/app-bundle/immediate_flow.png)


**Figure 2.** An example of an immediate update flow.

<br />

## Support in-app updates in your app

Learn how to support in-app updates in your app, depending on your development
environment:

- [Kotlin or Java](https://developer.android.com/guide/playcore/in-app-updates/kotlin-java)
- [Native (C/C++)](https://developer.android.com/guide/playcore/in-app-updates/native)
- [Unity](https://developer.android.com/guide/playcore/in-app-updates/unity)
- [Unreal Engine](https://developer.android.com/guide/playcore/in-app-updates/unreal-engine)

## Terms of service

By accessing or using the Play In-App Updates Library, you agree to the [Play
Core Software Development Kit Terms of Service](https://developer.android.com/guide/playcore#license). Read and understand all
applicable terms and policies before accessing the library.

## Data safety

The Play Core libraries are your app's runtime interface with the Google Play
Store. When you use Play Core in your app, the Play Store runs its own
processes, including handling data as governed by the [Google Play Terms of
Service](https://play.google.com/about/play-terms/index.html). The following information describes how the Play Core libraries
handle data to process specific requests from your app.

### In-app updates

|---|---|
| Data collected on usage | Device metadata Application version List of modules and asset packs installed |
| Purpose of data collection | The data collected is used to determine if an update is available and what the size of the update is expected to be. |
| Data encryption | Data is encrypted. |
| Data sharing | Data is not transferred to any third parties. |
| Data deletion | Data is deleted following a fixed retention period. |

While we aim to be as transparent as possible, you are solely responsible for
deciding how to respond to Google Play's data safety section form regarding your
app's user data collection, sharing, and security practices.