---
title: https://developer.android.com/develop/ui/views/layout/edge-to-edge-manually
url: https://developer.android.com/develop/ui/views/layout/edge-to-edge-manually
source: md.txt
---

Calling [`enableEdgeToEdge`](https://developer.android.com/reference/androidx/core/view/WindowCompat#enableEdgeToEdge(android.view.Window)) encapsulates the logic needed to be truly
[backward compatible](https://medium.com/androiddevelopers/is-your-app-providing-a-backward-compatible-edge-to-edge-experience-2479267073a0) and is therefore the recommended way to set up an
edge-to-edge display. Refer to the [Compose](https://developer.android.com/develop/ui/compose/system/insets-ui) and [Views](https://developer.android.com/develop/ui/views/layout/edge-to-edge) documentation
instead of this guide for the modern way to go edge-to-edge using
`enableEdgeToEdge`.

While not recommended, if your app must manually set up an edge-to-edge display
you can follow these steps:

1. Call `WindowCompat.setDecorFitsSystemWindows(window, false)`.
2. Set the system bars to transparent.
3. Handle insets.

## Lay out your app in full screen

Use [`WindowCompat.setDecorFitsSystemWindows(window, false)`](https://developer.android.com/reference/androidx/core/view/WindowCompat#setDecorFitsSystemWindows(android.view.Window,%20boolean))
to lay out your app behind the system bars, as shown in the following code
example:  

### Kotlin

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
  super.onCreate(savedInstanceState)
  WindowCompat.setDecorFitsSystemWindows(window, false)
}
```

### Java

```java
@Override
public void onCreate(Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);
  WindowCompat.setDecorFitsSystemWindows(getWindow(), false);
}
```

## Change the color of the system bars

When manually creating an edge-to-edge layout for Android 14 and older, your app
must also make the system bars transparent.

You can edit the `themes.xml` file to set the color of the status and navigation
bar as transparent and change the status bar icon color.  

    <!-- values-v29/themes.xml -->
    <style name="Theme.MyApp">
      <item name="android:navigationBarColor">
         @android:color/transparent
      </item>

      <!-- Optional: set to transparent if your app is drawing behind the status bar. -->
      <item name="android:statusBarColor">
         @android:color/transparent
      </item>

      <!-- Optional: set for a light status bar with dark content. -->
      <item name="android:windowLightStatusBar">
        true
      </item>
    </style>

| **Note:** If you prefer to disable automatic content protection on Android 10 (API level 29) or later, set [`android:enforceNavigationBarContrast`](https://developer.android.com/reference/android/view/Window#isNavigationBarContrastEnforced()), [`android:enforceStatusBarContrast`](https://developer.android.com/reference/android/view/Window#isStatusBarContrastEnforced()), or both to `false` in your theme.

You can use the `WindowInsetsControllerCompat` API instead of
`theme.xml` to control the status bar's content color. To do so, use the
[`setAppearanceLightNavigationBars()`](https://developer.android.com/reference/androidx/core/view/WindowInsetsControllerCompat#setAppearanceLightNavigationBars(boolean))
function, passing in `true` to change the foreground color of the navigation to
a light color or `false` to revert to the default color.  

### Kotlin

```kotlin
val windowInsetsController =
      ViewCompat.getWindowInsetsController(window.decorView)

windowInsetsController?.isAppearanceLightNavigationBars = true
```

### Java

```java
WindowInsetsControllerCompat windowInsetsController =
      ViewCompat.getWindowInsetsController(getWindow().getDecorView());
if (windowInsetsController == null) {
    return;
}

windowInsetsController.setAppearanceLightNavigationBars(true);
```

## Handle insets

Finally, your app must to handle insets so that critical UI avoids the
system bars and display cutout. Refer to the [Compose](https://developer.android.com/develop/ui/compose/system/insets-ui) and [Views](https://developer.android.com/develop/ui/views/layout/edge-to-edge)
documentation to learn how to handle insets.