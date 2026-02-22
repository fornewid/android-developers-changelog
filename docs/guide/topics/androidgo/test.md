---
title: https://developer.android.com/guide/topics/androidgo/test
url: https://developer.android.com/guide/topics/androidgo/test
source: md.txt
---

# Test Android (Go edition) apps

Similar to devices running on the Android platform, apps on Go devices should still be performant for end-users. There are ways to minimize inefficient uses of resources, such as CPU, memory, graphics, network, or device battery.

To fix performance issues, you can use the profiling and benchmarking tools, along with the guidance provided for Android at[Profile your app performance](https://developer.android.com/studio/profile).

## Testing requirements

Here are a few key guidelines to keep in mind when profiling and testing your Android (Go edition) app:

- Test on a device that supports Android 8.1 (API level 27) or above. It's important to use real devices (if possible) instead of an emulator, as CPU performance may impact results.
- Monitor your RAM usage through tools like Android Studio[Memory Profiler](https://developer.android.com/studio/profile/memory-profiler)or[Perfetto](https://perfetto.dev/docs/data-sources/memory-counters)to keep track of how much memory is being consumed. Identifying memory leaks and memory churn can lead to a reduction in app crashes and overall jank.
  - To incrementally release memory based on certain system constraints, you can implement[`onTrimMemory`](https://developer.android.com/reference/android/content/ComponentCallbacks2#onTrimMemory(int)). This callback allows apps to release resources to help provide a more responsive system overall, and also directly benefits the end-user experience for your app by allowing the system to keep your process alive longer. For more information, see the documentation on[`ComponentCallbacks`](https://developer.android.com/reference/android/content/ComponentCallbacks2).
- Ensure that you disable all features[not supported](https://developer.android.com/guide/topics/androidgo#differences_from_android)on Android (Go edition).

## Android vitals for Go devices

To view[Android vitals](https://developer.android.com/topic/performance/vitals)statistics for your apps running on Android (Go edition) devices, navigate to the Google Play Console and set the following filters and device configurations:

- **Device type**: Android Go
- **Android version**: 8.1 \& above
- **RAM** : 2GB (as of Android 13 (API level 33) and higher). For a full list of device and hardware specifications, see[Minimum hardware specifications](https://developer.android.com/guide/topics/androidgo#hardware-reqs).

![](https://developer.android.com/static/images/performance-testing/go_filters.png)**Figure 1.**Set the following filters in the Play console to see metrics for your apps running on Android (Go edition) devices.

To view any apps running specifically on Android (Go edition) devices, you can apply the**Android Go**filter in the Device Catalog as shown in Figure 2.
![](https://developer.android.com/static/images/performance-testing/go_device_filter.png)**Figure 2.**Apply the Android Go device filter in the Play console to fetch metrics for users running on Android (Go edition) devices.