---
title: https://developer.android.com/guide/topics/androidgo
url: https://developer.android.com/guide/topics/androidgo
source: md.txt
---

# Android (Go edition)

The Android operating system brings the power of computing to everyone. This vision applies to all users, including those on entry-level phones that face real constraints across data, storage, memory, and more. When Android (Go edition) was[first announced in 2017](https://www.blog.google/products/android/2bn-milestone), entry-level phones accounted for more than half of all device shipments globally.

With this in mind, Android (Go edition) helps to provide an optimized experience for low-RAM devices. By tailoring the OS configuration and making key trade-offs, we're able to improve speed and performance for low-end devices and offer a quality phone experience for people around the world.

Android (Go edition) helps to fulfill our mission: to empower people with affordable, reliable smartphones and the opportunities they enable.

## Android (Go edition) specifications

Android (Go edition) is a mobile operating system built for entry-level smartphones with less RAM than standard in higher-end devices. Android (Go edition) runs much lighter and saves data, letting Original Equipment Manufacturers (OEMs) build affordable, entry-level devices that empower people with possibility.

### Minimum hardware requirements

There are minimum RAM requirements for devices to run Android (Go edition), depending on the version of Android you are running. For a list of these requirements, see the following table. For full Android (Go edition) device capability specifications, see[Optimize for devices running Android (Go edition)](https://developer.android.com/docs/quality-guidelines/build-for-billions/device-capacity#androidgo).

| Release | Android 8.1 (API level 27) | Android 9 (API level 28) | Android 10 (API level 29) | Android 11 (API level 30) | Android 12 (API level 31) | Android 13 (API level 33) |
|---------|----------------------------|--------------------------|---------------------------|---------------------------|---------------------------|---------------------------|
| Min RAM | 512MB                      | 512MB                    | 512MB                     | 1GB                       | 1GB                       | 2GB                       |

Android (Go edition) as an operating system is optimized for these constraints. With a kernel that understands app priority, Android (Go edition) reclaims program memory without impacting the end-user experience, making app usage and navigation seamless.

## Differences from Android

Android (Go edition) is part of the main Android platform and is simply a configuration of Android platform OS. Any app built for the main Android platform can technically run on Go. However, be mindful that there are significant built-in performance, network, and battery limitations. Remember, even if your app complies with the hardware specifications of a given device, including features that aren't supported by Android (Go edition) can cause compatibility issues.

The following features are disabled by default on Android (Go edition):

- Picture-in-picture support
- System alert Window permission (draw over other apps)
- Split-screen or multi-screen window
- Live wallpapers
- Multi-display
- Shortcuts or deep shortcuts in the launcher
- Reduced maximum width and height of any image in remote view
- VR mode

| **Note:** This is not a comprehensive list and there may be other minor features disabled on Android (Go edition).

## What's new

We're constantly making phones powered by Android (Go edition) more accessible with additional performance optimizations and features for entry-level devices, like translation, app switching, and data saving.

For more information on the recent development additions, see[Android 13 (Go edition): Easier to update and tailored just for you)](https://blog.google/products/android/android-13-go-edition/).