---
title: https://developer.android.com/develop/ui/compose/system/setup-e2e
url: https://developer.android.com/develop/ui/compose/system/setup-e2e
source: md.txt
---

To allow your app full control over where it draws content, follow these setup
steps. Without these steps, your app may draw black or solid colors behind the
system UI, or not animate synchronously with the software keyboard.

1. Target Android 15 (API level 35) or higher to [enforce edge-to-edge](https://developer.android.com/about/versions/15/behavior-changes-15#edge-to-edge) on Android 15 and higher. Your app displays behind the system UI. You can adjust your app's UI by handling insets.
2. Optionally, call [`enableEdgeToEdge()`](https://developer.android.com/reference/androidx/core/view/WindowCompat#enableEdgeToEdge(android.view.Window)) in [`Activity.onCreate()`](https://developer.android.com/reference/android/app/Activity#onCreate(android.os.Bundle)), which lets your app be edge-to-edge on previous Android versions.
3. Set `android:windowSoftInputMode="adjustResize"` in your Activity's
   `AndroidManifest.xml` entry. This setting allows your app to receive the size
   of the software IME as insets, which helps you apply the appropriate layout
   and padding when the IME appears and disappears in your app.

       <!-- In your AndroidManifest.xml file: -->
       <activity
         android:name=".ui.MainActivity"
         android:label="@string/app_name"
         android:windowSoftInputMode="adjustResize"
         android:theme="@style/Theme.MyApplication"
         android:exported="true">

4. Handle insets so your critical UI doesn't overlap with the system bars or
   display cutout. You can handle insets using either [rulers](https://developer.android.com/develop/ui/compose/system/evaluate-rulers),
   [padding modifiers](https://developer.android.com/develop/ui/compose/system/setup-e2e#padding-modifiers) or [inset size modifiers](https://developer.android.com/develop/ui/compose/system/setup-e2e#inset-size).
   Some [Material Components](https://developer.android.com/develop/ui/compose/system/material-insets) automatically handle insets or have parameters to
   facilitate handling insets like [`Scaffold`](https://developer.android.com/develop/ui/compose/system/material-insets#scaffold)'s `PaddingValues` parameter.
   Choose one inset handling approach. For example, use either `Scaffold`,
   `Modifier.safeDrawingPadding()`, or
   `Modifier.fitInside(WindowInsetsRulers.SafeDrawing.current)` as these approaches
   are often interchangeable.