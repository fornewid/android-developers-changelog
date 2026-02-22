---
title: https://developer.android.com/docs/quality-guidelines/build-for-billions/data-cost
url: https://developer.android.com/docs/quality-guidelines/build-for-billions/data-cost
source: md.txt
---

# Reduced data cost for billions

<br />

Data plans in some countries can cost upwards of 10% of a typical user's monthly income. This means that minimizing your app's download size and letting the user control how your app uses data can have a large, tangible benefit to many users. Minimizing download size also helps conserve space in internal storage, which is a scarce resource in some devices.

<br />

<br />

Here you can find some strategies to help optimize the amount of data your app uses, both over the network and in internal storage.

<br />

<br />

## Reduce app size

<br />

<br />

Reducing app size is one of the fundamental ways you can help your user consume less data, in terms of both network data and internal storage. This section describes several approaches to reducing app size.

<br />

<br />

### Reduce APK graphical asset size

<br />

<br />

- Graphical assets are often the largest contributor to the size of the APK. Optimizing these can result in smaller downloads and thus faster installation times for users.
- For graphical assets such as icons, use the Scalable Vector Graphics (SVG) format. SVG images are tiny in size compared to bitmap graphics and can be rendered at runtime to any resolution. The[Android Support Library](https://developer.android.com/tools/support-library)provides a backward-compatible implementation for vector resources to Android 2.1 (API level 7). Get started with vectors with[this Medium post](https://medium.com/@chrisbanes/appcompat-v23-2-age-of-the-vectors-91cbafa87c88).
- For non-vector images, such as photos, use[WebP](https://developers.google.com/speed/webp/)to reduce image load times and save network bandwidth. WebP is proven to result in smaller file sizes than its PNG and JPG counterparts, with at least the same image quality. Even at lossy settings, WebP can produce a nearly identical image to the original. Android has included lossy WebP support since Android 4.0 (API level 14: Ice Cream Sandwich) and support for lossless, transparent WebP since Android 4.2 (API level 17: Jelly Bean).
- If you have many large images across multiple densities, consider using[Multiple APK support](https://developer.android.com/google/play/publishing/multiple-apks)to split your APK by density. This results in builds targeted for specific densities, meaning users with low-density devices won't have to incur the penalty of downloading unused high-density assets.
- For more information about reducing APK size, see[Reduce APK Size](https://developer.android.com/topic/performance/reduce-apk-size)and[Shrink Your Code and Resources](https://developer.android.com/studio/build/shrink-code). In addition, you can find a detailed guide on reducing APK size in this[series of Medium posts](https://medium.com/@wkalicinski/smallerapk-part-4-multi-apk-through-abi-and-density-splits-477083989006).

### Reduce code size

- Every library in your Android project is adding potentially unused code to the APK. Be particularly careful about using external libraries because not all libraries are designed for use in mobile apps. Ensure that the libraries your app is using are optimized for mobile use.
- Consider optimizing your compiled code using a tool such as[ProGuard](https://developer.android.com/tools/help/proguard). ProGuard identifies code that isn't being used and removes it from your APK. Also[enable resource shrinking](http://tools.android.com/tech-docs/new-build-system/resource-shrinking)at build time by setting`minifyEnabled=true`,`shrinkResources=true`in`build.gradle`---this automatically removes unused resources from your APK.
- When using Google Play services, you should[selectively include](https://developer.android.com/google/play-services/setup#add_google_play_services_to_your_project)only the necessary APIs into your APK.
- For more information on reducing code size in your APK, see the Android training on how to[Avoid dependency injection frameworks](https://developer.android.com/training/articles/memory#DependencyInjection).

### Allow app to be moved to external (SD) storage

- Low-cost devices often come with little on-device storage. Users can extend this with SD cards; however, apps need to explicitly declare that they support being installed to external storage before users can move them.
- Allow your app to be installed to external storage using the[`
  android:installLocation`](https://developer.android.com/guide/topics/manifest/manifest-element#install)flag in your AndroidManifest.xml. For more information on enabling your app to be moved to external storage, see the Android guide on[App Install Location](https://developer.android.com/guide/topics/data/install-location).

<br />

### Reduce post-install app disk use

<br />

- Keeping your app's disk use low means that users are less likely to uninstall your app when the device is low on free space. It's important to apply bounds around your caches---this prevents your app's disk use from growing indefinitely. Be sure you put your cached data in[getCacheDir()](https://developer.android.com/reference/android/content/Context#getCacheDir())---the system can delete files placed here as needed, so they won't show up as storage committed to the app.

<br />

## Offer configurable network use

The Android platform includes a number of ways you can give the user control over your app's network use, optimizing it for their own needs. For example, on first use, your app can walk the user through a variety of network-related settings. You can also provide a network preferences screen from outside the app.

### Provide onboarding experiences for users' network choices

<br />

- Apps that allow users to reduce data use are well received, even if they have heavy data requirements. If your app uses a considerable amount of bandwidth (for example, video streaming apps), you can provide an onboarding experience for users to configure network use. For example, you could allow the user to force lower-bitrate video streams on cellular networks.
- Additional settings for users to control data syncing, prefetching, and network use behavior (for example, prefetch all starred news categories on Wi-Fi only), also help users tailor your app's behavior to their needs.
- For more information on managing network use, see the Android training on[Managing Network Usage](https://developer.android.com/training/basics/network-ops/managing).

### Provide a network preferences screen

- You can navigate to the app's network settings from outside the app by means of a network preferences screen. You can invoke this screen from either the system settings screen or the system data usage screen.
- To provide a network preferences screen that users can access from within your app as well as from the system settings, in your app include an activity that supports the[ACTION_MANAGE_NETWORK_USAGE](https://developer.android.com/reference/android/content/Intent#ACTION_MANAGE_NETWORK_USAGE)action.
- For further information on adding a network preferences screen, see the Android training on[Implementing a Preferences Activity](https://developer.android.com/training/basics/network-ops/managing#prefs).

<br />

## Additional resources

To learn more about this topic, view the following additional resources:

### Blog posts

- [Nurture trust through cost transparency](https://medium.com/google-design/nurture-trust-through-cost-transparency-b61a5947d2fc)