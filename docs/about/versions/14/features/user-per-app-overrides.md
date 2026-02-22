---
title: https://developer.android.com/about/versions/14/features/user-per-app-overrides
url: https://developer.android.com/about/versions/14/features/user-per-app-overrides
source: md.txt
---

Android provides overrides that change the configured behavior of apps.

Device manufacturers can apply overrides to apps on select large screen devices. Android 14 QPR1 introduces user overrides, which enable users to apply overrides to apps through device settings.

Per-app overrides are intended to improve the user experience on large screen devices. Apps can disable some overrides.

For more information about per-app overrides, see [Device compatibility mode](https://developer.android.com/guide/practices/device-compatibility-mode#user_per-app_overrides).
| **Note:** To enable your app to provide the best user experience without relying on device manufacturer or user overrides, follow the [Large screen app quality](https://developer.android.com/docs/quality-guidelines/large-screen-app-quality) guidelines.

## User overrides

Android 14 QPR1 introduces a new configuration menu that enables users to change the aspect ratio of apps to improve how apps display on large screens. The menu is implemented in device settings on select large screen devices.

On devices that have implemented the configuration menu, users choose from a list of apps and then set the app aspect ratio to various values, such as 4:3, 16:9, and full screen (aspect ratio values are configured by the device manufacturer). Users can also reset the aspect ratio to the app default, which is the value specified by a device manufacturer per‑app override (see [`OVERRIDE_MIN_ASPECT_RATIO`](https://developer.android.com/guide/topics/large-screens/large-screen-compatibility-mode#override_min_aspect_ratio)) or, if no override has been applied or the app has disabled the override, the value in the app manifest.

### Disable the overrides

Android 14 QPR1 supports the following [`PackageManager.Property`](https://developer.android.com/reference/android/content/pm/PackageManager.Property) tags, which enable you to disable or modify the aspect ratio configuration menu on devices that have implemented the override:
| **Note:** The property tags are Jetpack WindowManager [WindowProperties](https://developer.android.com/reference/kotlin/androidx/window/WindowProperties) constants, which may not be available or tested on all devices.

<br />

- **PROPERTY_COMPAT_ALLOW_USER_ASPECT_RATIO_OVERRIDE**

  To disable the user aspect ratio compatibility override, add the property to your app manifest and set the value to `false`:  

      <application>
          <property
              android:name="android.window.PROPERTY_COMPAT_ALLOW_USER_ASPECT_RATIO_OVERRIDE"
              android:value="false"/>
      </application>

  On devices that have implemented the configuration menu, your app is excluded from the list of apps in device settings; and so, users are not able to override the app's aspect ratio.

  Setting the property to `true` has no effect.

  <br />

- **PROPERTY_COMPAT_ALLOW_USER_ASPECT_RATIO_FULLSCREEN_OVERRIDE**

  To disable the full-screen option of the user aspect ratio compatibility override, add the property to your app manifest and set the value to `false`:  

      <application>
          <property
              android:name="android.window.PROPERTY_COMPAT_ALLOW_USER_ASPECT_RATIO_FULLSCREEN_OVERRIDE"
              android:value="false"/>
      </application>

  On devices that have implemented the configuration menu, the full‑screen option is removed from the list of aspect ratio options in device settings. Users are not able to apply the full‑screen override to your app.

  Setting this property to `true` has no effect.
  | **Caution:** If [`PROPERTY_COMPAT_ALLOW_USER_ASPECT_RATIO_OVERRIDE`](https://developer.android.com/about/versions/14/features/user-per-app-overrides#aspect_ratio_override) is set to `false`, this property has no effect.

| **Note:** To implement the property tags, your app must include the Jetpack [WindowManager](https://developer.android.com/jetpack/androidx/releases/window) library dependency.

**Optimize your app for large screens:** Don't set aspect ratio restrictions in your app. Use [window size classes](https://developer.android.com/develop/ui/compose/layouts/adaptive/window-size-classes) to support different layouts based on the amount of available display space.