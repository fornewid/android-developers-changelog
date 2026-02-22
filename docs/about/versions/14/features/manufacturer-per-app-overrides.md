---
title: https://developer.android.com/about/versions/14/features/manufacturer-per-app-overrides
url: https://developer.android.com/about/versions/14/features/manufacturer-per-app-overrides
source: md.txt
---

Android provides overrides that change the configured behavior of apps. For example, the [`FORCE_RESIZE_APP`](https://developer.android.com/guide/topics/large-screens/large-screen-compatibility-mode#force_resize_app) override instructs the system to resize the app to fit display dimensions even if [`resizeableActivity="false"`](https://developer.android.com/guide/topics/manifest/application-element#resizeableActivity) is set in the app manifest.

Device manufacturers apply overrides to apps on select large screen devices.

Per-app overrides are intended to improve the user experience on large screen devices. Apps can disable some overrides.

For more information about per-app overrides, see [Device compatibility mode](https://developer.android.com/guide/practices/device-compatibility-mode).
| **Note:** To enable your app to provide the best user experience without relying on overrides, follow the [Large screen app quality](https://developer.android.com/docs/quality-guidelines/large-screen-app-quality) guidelines.

## Device manufacturer overrides

Device manufacturers apply overrides to apps to improve the user experience on tablets, foldables, and other large screen devices. For a complete list of overrides, see [Device compatibility mode](https://developer.android.com/guide/practices/device-compatibility-mode#per-app_overrides).

### Disable the overrides

[`PackageManager.Property`](https://developer.android.com/reference/android/content/pm/PackageManager.Property) tags enable apps to disable device manufacturer overrides. Android 14 introduces the following tags:

<br />

- **PROPERTY_COMPAT_ALLOW_RESIZEABLE_ACTIVITY_OVERRIDES**

  To disable the [`FORCE_RESIZE_APP`](https://developer.android.com/guide/topics/large-screens/large-screen-compatibility-mode#force_resize_app) and [`FORCE_NON_RESIZE_APP`](https://developer.android.com/guide/topics/large-screens/large-screen-compatibility-mode#force_non_resize_app) overrides, set the property to false in your app manifest:  

      <application>
          <property
              android:name="android.window.PROPERTY_COMPAT_ALLOW_RESIZEABLE_ACTIVITY_OVERRIDES"
              android:value="false"/>
      </application>

  **Optimize your app for large screens:** Make your app resizable and implement responsive/adaptive layouts for an optimal user experience on displays of all sizes.

  <br />

- **PROPERTY_COMPAT_ALLOW_MIN_ASPECT_RATIO_OVERRIDE**

  To disable [`OVERRIDE_MIN_ASPECT_RATIO`](https://developer.android.com/guide/topics/large-screens/large-screen-compatibility-mode#override_min_aspect_ratio), set the property to false in your app manifest:  

      <application>
          <property
              android:name="android.window.PROPERTY_COMPAT_ALLOW_MIN_ASPECT_RATIO_OVERRIDE"
              android:value="false"/>
      </application>

  The property also disables the following device manufacturer overrides:
  - [`OVERRIDE_MIN_ASPECT_RATIO_PORTRAIT_ONLY`](https://developer.android.com/guide/topics/large-screens/large-screen-compatibility-mode#override_min_aspect_ratio_portrait_only): Restricts configurations that force a given minimum aspect ratio for activities with portrait‑only orientation.
  - [`OVERRIDE_MIN_ASPECT_RATIO_MEDIUM`](https://developer.android.com/guide/topics/large-screens/large-screen-compatibility-mode#override_min_aspect_ratio_medium): Sets the activity's minimum aspect ratio to a medium value (3:2).
  - [`OVERRIDE_MIN_ASPECT_RATIO_LARGE`](https://developer.android.com/guide/topics/large-screens/large-screen-compatibility-mode#override_min_aspect_ratio_large): Sets the activity's minimum aspect ratio to a large value (16:9).
  - [`OVERRIDE_MIN_ASPECT_RATIO_TO_ALIGN_WITH_SPLIT_SCREEN`](https://developer.android.com/guide/topics/large-screens/large-screen-compatibility-mode#override_min_aspect_ratio_to_align_with_split_screen): Enables the use of split‑screen aspect ratio. Allows an app to use all the available space in split‑screen mode, avoiding letterboxing.
  - [`OVERRIDE_MIN_ASPECT_RATIO_EXCLUDE_PORTRAIT_FULLSCREEN`](https://developer.android.com/guide/topics/large-screens/large-screen-compatibility-mode#override_min_aspect_ratio_exclude_portrait_fullscreen): Disables the minimum aspect ratio override in portrait full screen to use all available screen space.

  **Optimize your app for large screens:** Don't set aspect ratio restrictions in your app. Create app layouts that support different screen sizes and multi‑window mode.