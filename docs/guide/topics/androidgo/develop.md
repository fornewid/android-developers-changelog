---
title: https://developer.android.com/guide/topics/androidgo/develop
url: https://developer.android.com/guide/topics/androidgo/develop
source: md.txt
---

# Develop for Android (Go edition)

Building applications for use on Android (Go edition) devices requires special attention to performance optimizations and resource usage. There are two main components to understand when building for Android (Go edition): the operating system (OS) and the Google Play Store.

## Operating system compatibility

It's very important to develop an*OS-aware* app when developing for Android (Go edition). By OS-aware, we mean that your app can detect and adapt to Android (Go edition) users. For instance, the[`isLowRamDevice()`](https://developer.android.com/reference/android/app/ActivityManager#isLowRamDevice())flag enables your app to detect whether it is running on a low-memory device and behave accordingly.

By knowing the OS of your users, you can limit certain functionalities that aren't available on Go devices, like drawing over other apps or using multi-display. For a full list of app limitations on Go, see[Differences from Android](https://developer.android.com/guide/topics/androidgo#differences-from-android).

### Importance of POST-boot RAM

There are instances where processes and tasks can run persistently in the background, either from the system or apps from the Play Store. For example, when a device restarts, there is a`BOOT_COMPLETED`broadcast that might be a requirement from many services or apps running on a user's device. This persistent broadcast can lead to apps not launching, or having foreground tasks fail, due to low memory on a device.

All apps on a user's device directly impact memory availability. If these apps initiate broadcasts or services, then it becomes mandatory for Android (Go edition) apps to query post-boot system memory availability on a user's device as it directly impacts the end-user experience.

### Developer choices

When it comes to making choices for your application as a developer, you should ensure your app can run with Android (Go edition) limitations in mind. Sometimes, allowing users to simply disable a specific feature is not enough, as apps might require those features to be enabled to run properly. For a list of the most common limitations on Android (Go edition), see[Differences from Android](https://developer.android.com/guide/topics/androidgo#differences_from_main_android).

## Google Play Store

The Google Play Store looks, feels, and operates the same on both Android (Go edition) and Android. However, on Go devices, the Play Store may recommend apps that are optimized for Android (Go edition).