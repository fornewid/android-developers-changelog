---
title: https://developer.android.com/docs/quality-guidelines/build-for-billions/device-capacity
url: https://developer.android.com/docs/quality-guidelines/build-for-billions/device-capacity
source: md.txt
---

# Device capability for billions

Reaching new users means supporting an increasing variety of Android platform versions and device specifications. To improve the user experience, optimize for common RAM configurations, and screen sizes and resolutions.

## Support multiple screen sizes

Your app can provide a better user experience for billions of users if it supports screens of various sizes and resolutions. This section describes a few ways you can do this.

### Use density-independent pixels (dp)

- Defining layout dimensions with pixels doesn't work well because different screens have different pixel densities, so the same number of pixels may correspond to different physical sizes on different devices.
- To overcome this Android supports the density-independent pixel (dp), which corresponds to the physical size of a pixel at 160 dots per inch (mdpi density).
- Defining layouts with dp ensures that the physical size of your user interface is consistent regardless of device. Visit the Android guide on[Supporting Multiple Screens](https://developer.android.com/guide/practices/screens_support)for best practices on using density-independent pixels.

### Test text and graphics on ldpi and mdpi screen densities

- Test to ensure that your text and graphics work well on low- and medium-density (ldpi and mdpi) screens because these are[common densities](https://developer.android.com/about/dashboards#Screens), especially in lower-cost devices. Look out for text that may be unclear on lower-density screens, where fine details aren't visible.
- Devices with lower-density screens tend to have lower hardware specifications. To ensure that your app performs well on these devices, consider reducing or eliminating heavy graphics processing loads, such as animations and transitions.
- For more information about supporting different densities, see the Android training on[Supporting Different Densities](https://developer.android.com/training/multiscreen/screendensities).

### Test layouts on small and medium screen sizes

- Validate that your layouts scale down by testing on smaller screens. As screen sizes shrink, be very selective about visible UI elements, because there is limited space for them.
- The Material Design guidelines describe[metrics and keylines](https://material.io/archive/guidelines/layout/metrics-keylines.html)to ensure that your layouts can scale across screen densities.
- For more information about supporting different screen sizes, see the Android training on[Supporting Different Screen Sizes](https://developer.android.com/training/multiscreen/screensizes).

## Provide backward compatibility

Not all of your users may be using devices powered by the latest, greatest version of the Android platform. Here are some ways you can improve backward compatibility, helping make your app available to as many people as possible.

### Set your`targetSdkVersion`and`minSdkVersion`appropriately

- Apps should build and target the most recent version of Android to ensure they offer the most current behavior across a broad range of devices; this still provides backward compatibility to older versions. Here are the best practices for targeting API levels appropriately:
  - [`targetSdkVersion`](https://developer.android.com/guide/topics/manifest/uses-sdk-element#target)should be the latest version of Android. Targeting the most recent version ensures that your app inherits newer runtime behaviors when running newer versions of Android. Be sure to test your app on newer Android versions when updating the`targetSdkVersion`as it can affect app behavior.
  - [`minSdkVersion`](https://developer.android.com/guide/topics/manifest/uses-sdk-element#min)Sets the minimum supported Android version. Setting`minSdkVersion`also results in the Android build tools reporting incorrect use of new APIs that might not be available in older versions of the platform. By doing so, you are protected from inadvertently breaking backward compatibility.
- Consult the[Android dashboards](https://developer.android.com/about/dashboards#Platform), the[Google Play Developer Console](https://play.google.com/console/)for your app, and industry research in your target markets to gauge which versions of Android to target, based on your target users.

### Use the Android Support libraries

- Ensure your app provides a consistent experience across OS versions by using the[Android Support Library](https://developer.android.com/topic/libraries/support-library). This library provides backward-compatible versions of Android framework APIs as well as features that are only available through the library APIs such as`AppCompatActivity`and the Material Design Support Library.
- Some of the highlights include:
  - v4 and v7 support library: Many framework APIs for older versions of Android such as[ViewPager](https://developer.android.com/reference/androidx/viewpager/widget/ViewPager),[ActionBar](https://developer.android.com/reference/android/app/ActionBar),[RecyclerView](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView), and[Palette](https://developer.android.com/reference/androidx/palette/graphics/Palette).
  - [Material Design support library](https://developer.android.com/tools/support-library/features#material-design): APIs to support adding Material Design components and patterns to your apps.
  - [Multidex support library](https://developer.android.com/topic/libraries/support-library/packages#multidex): provides support for large apps that have more than 65K methods. This can happen if your app is using many libraries.
- For more information about the available support libraries, see the[Support Libraries Features](https://developer.android.com/tools/support-library/features)section of the Android Developer site.

### Use Google Play services

- Google Play services brings the best of Google APIs independent of Android platform version. Consider using features from Google Play services to offer the most streamlined Google experience on Android devices.
- Google Play services also include useful APIs such as[`GcmNetworkManager`](https://developers.google.com/android/reference/com/google/android/gms/gcm/GcmNetworkManager), which provides much of Android 5.0's[JobScheduler](https://developer.android.com/reference/android/app/job/JobScheduler)API for older versions of Android.
- Updates to Google Play services are distributed automatically by the Google Play Store, and new versions of the client library are delivered through the Android SDK Manager.

## Use memory efficiently

Memory is an unsung hero of the user experience. Good memory management can make your app more stable and more performant; in some cases, its effective use may be the only thing making your app usable at all. Here are some ways you can help your app use memory wisely.

### Reduce memory footprint on low-cost devices

- Adjust your memory footprint dynamically to ensure compatibility across devices with different RAM configurations.
- Methods such as[isLowRamDevice()](https://developer.android.com/reference/android/app/ActivityManager#isLowRamDevice())and[getMemoryClass()](https://developer.android.com/reference/android/app/ActivityManager#getMemoryClass())help determine memory constraints at runtime. Based on this information, you can scale down your memory use. As an example, you can use lower resolution images on low memory devices.
- For more information about managing your app's memory, see the Android training on[Managing Your App's Memory](https://developer.android.com/topic/performance/memory).

### Avoid long-running processes

- Long-running processes stay resident in memory and can slow down the device. In most situations, your app should wake up for a given event, process data, and shut down. You should use[Firebase Cloud Messaging (FCM)](https://firebase.google.com/docs/cloud-messaging/)and[`GcmNetworkManager`](https://developers.google.com/android/reference/com/google/android/gms/gcm/GcmNetworkManager)to avoid long running background services and reduce memory pressure on the user's device.

### Benchmark memory use

Android Studio provides memory benchmarking and profiling tools, enabling you to measure memory use at run time. Benchmarking your app's memory footprint enables you to monitor memory use over multiple versions of the app. This can help catch unintentional memory footprint growth. Use the Memory Profiler tool to do the following:

- Find out whether undesirable garbage collection (GC) event patterns might be causing performance problems.
- Identify object types that get or stay allocated unexpectedly or unnecessarily.
- Identify where in your code the problem might be.

For more information about benchmarking memory use, see[View the Heap and Allocations with Memory Profiler](https://developer.android.com/studio/profile/memory-profiler).

## Optimize for devices running Android (Go edition)

Android (Go edition) is an optimized experience for entry-level devices with ≤1GB RAM, starting with Android Oreo (Go edition). To ensure your app runs great on Android (Go edition) devices, you should should take into account the following guidelines:

- [targetSdkVersion](https://developer.android.com/guide/topics/manifest/uses-sdk-element#target)should be the latest version of Android. Android (Go edition) devices only run Android Oreo (API 27 or higher).
- The app should run smoothly on devices with ≤1GB RAM. Keep in mind the memory optimizations listed in[Use memory efficiently](https://developer.android.com/docs/quality-guidelines/build-for-billions/device-capacity#memory)above and use[Android vitals](https://developer.android.com/topic/performance/vitals)to identify and fix bad behaviors like slow rendering and frozen frames.
- [Picture in picture](https://developer.android.com/guide/topics/ui/picture-in-picture)(PIP) might be disabled on devices. Before your app uses PIP, check to be sure it is available by calling[hasSystemFeature(PackageManager.FEATURE_PICTURE_IN_PICTURE)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String)).
- The on-device app size should be smaller than 40MB.
- The Proportional Set Size (PSS) of the app's RAM usage should not exceed 90MB. For games, the PSS of the game's RAM usage should not exceed 150MB. For more information about PSS, see the[Investigating Your RAM Usage](https://developer.android.com/studio/profile/memory-profiler)guide.
- The startup time of the app should be minimal and under 5 seconds.
- [`SYSTEM_ALERT_WINDOW`](https://developer.android.com/reference/android/Manifest.permission#SYSTEM_ALERT_WINDOW)(which allows apps to draw a window on top of other apps) might be disabled on Android Go devices that have low RAM. Before drawing over other apps, check whether your app has this authorization by calling[Settings.canDrawOverlays()](https://developer.android.com/reference/android/provider/Settings#canDrawOverlays(android.content.Context)). If your app cannot get the permission, gracefully degrade your app so that the user can continue using your app, possibly by disabling the feature that requires the`SYSTEM_ALERT_WINDOW`permission.

We recommend that most developers optimize their existing app, which will be available on all Android (Go edition) devices, because making your app run faster and lighter will benefit your whole audience. You can use the[Multiple APK feature](https://developer.android.com/google/play/publishing/multiple-apks)on the Play Console to distribute a specific APK for Android (Go edition) devices but you should only do so without compromising the experience (e.g. you should avoid removing features). The APK targeting Android (Go edition) devices needs to declare`<uses-feature android:name="android.hardware.ram.low" android:required="true">`, target at least API Level 26, and have a higher version code than the non-Go edition APK.
| **Note:**If you are designing a completely different app, with a new experience and a different set of features, you might decide to launch an Android (Go edition) specific app, with a unique application package. This would also have a unique Play Store listing, with its own ratings and install count, and this may be confusing for users on the Play Store. For the majority of developers, we recommend using Multiple APK to target Android (Go edition) devices, instead of creating two distinct and separate apps.

## Related

## Additional resources

To learn more about supporting a variety of devices, view the following resource:

### Blog posts

- [To Make Apps Accessible, Make Them Compatible with Different Devices](https://medium.com/google-design/to-make-apps-accessible-make-them-compatible-with-different-devices-11298c6d3f06)