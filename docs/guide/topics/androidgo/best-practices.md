---
title: https://developer.android.com/guide/topics/androidgo/best-practices
url: https://developer.android.com/guide/topics/androidgo/best-practices
source: md.txt
---

# Best practices for Android (Go edition) development

Follow these best practices and answers to common questions when starting to develop or optimize your app for Android (Go edition).

- Don't add any excessive permissions to your app.
- Minimize app activity when in the background and when the device is running on low power.
- Avoid using wake locks because they prevent the device from going into low-power states.
- Batch network activity to reduce the number of wakeups. You can use[WorkManager](https://developer.android.com/topic/libraries/architecture/workmanager)to schedule tasks and let the system batch operations.
- Validate that your layouts scale down by testing on smaller screens.
- Methods such as[`isLowRamDevice()`](https://developer.android.com/reference/android/app/ActivityManager#isLowRamDevice())and[`getMemoryClass()`](https://developer.android.com/reference/android/app/ActivityManager#getMemoryClass())help determine memory constraints at runtime. Using this information, you can scale down your memory use. For example, you can use lower resolution images on low memory devices.
- Allow your app to be installed to external storage using the[`android:installLocation`](https://developer.android.com/guide/topics/manifest/manifest-element#install)flag in your`AndroidManifest.xml`file.
- If you're looking to build for a larger-scaled audience, take a look at the[Build for billions](https://developer.android.com/topic/billions)documentation.

## Optimize for Go or start fresh

Many developers looking to launch apps on Android Go may wonder if they should optimize their existing app or develop an entirely new one. This choice depends on many factors, including how many development resources you have, whether or not you can keep features in your app that are optimized for these devices, and what type of distribution scenarios you want to enable for end-users around the world.

One app for all
:   Use the same app for Android (Go edition) devices and all other devices with an identical experience. In this case, you are optimizing your existing app to run well on these devices, and your existing users gain performance benefits from those optimizations. We highly encourage you to use the[Android App Bundle](https://developer.android.com/guide/app-bundle)to experience significant size savings without having to refactor your code.

Two apps
:   Create a new "light" app and target Android (Go edition) devices. You can leave your existing app as is. The "lite" app can still target all devices in all locales as there is no requirement for this "lite" app to only target Android (Go edition) devices.