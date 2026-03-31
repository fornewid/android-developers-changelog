---
title: Set up Edge-to-edge  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/system/setup-e2e
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Set up Edge-to-edge Stay organized with collections Save and categorize content based on your preferences.



Edge-to-edge display allows your app to draw its UI behind the system bars—the
status bar, caption bar, and navigation bar—to achieve a more immersive user
experience. If you target devices running Android 15 (API level 35) or higher,
[edge-to-edge is enforced](/about/versions/15/behavior-changes-15#edge-to-edge) by default.

To correctly display content edge-to-edge on all Android versions, follow these
setup steps. Without these steps, your app might draw solid colors behind the
system bars or not animate its content synchronously with on-screen keyboard
(IME) transitions.

## 1. Enable edge-to-edge display

To enable edge-to-edge on previous Android versions, call
[`enableEdgeToEdge()`](/reference/androidx/core/view/WindowCompat#enableEdgeToEdge(android.view.Window)) in your `Activity.onCreate()` method:

```
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    enableEdgeToEdge()
    ...
}
```

By default, `enableEdgeToEdge()` makes the system bars transparent, except in
3-button navigation mode, where it applies a translucent scrim to the navigation
bar for better contrast. The color of system icons and the scrim adapts to the
system's light or dark theme.

## 2. Configure windowSoftInputMode

Set `android:windowSoftInputMode="adjustResize"` in your Activity's
`AndroidManifest.xml` entry. This setting allows your app to receive IME insets,
enabling you to adjust your layout with padding when the on-screen keyboard
appears or disappears.

```
<!-- In your AndroidManifest.xml file: -->
<activity
  android:name=".ui.MainActivity"
  android:label="@string/app_name"
  android:windowSoftInputMode="adjustResize"
  android:theme="@style/Theme.MyApplication"
  android:exported="true">
  ...
</activity>
```

## 3. Handle overlaps using insets

Once edge-to-edge is enabled, some of your app's content and UI elements might
draw behind the system bars. To prevent critical or interactive elements from
being obscured by system bars or overlapping with system gestures, you need to
handle insets.

Insets describe parts of the screen that intersect with system UI or system
gestures. The main types of insets to consider for edge-to-edge display are:

* **System bars insets:** Represent areas where system bars are displayed. Use
  these to avoid UI being obscured by system bars.
* **Display cutout insets:** Represent areas where a physical cutout (like a
  camera notch) exists on the device screen.

In Compose, You can handle insets using either rulers, padding modifiers or
inset size modifiers. See [About window insets](/develop/ui/compose/system/insets) for detailed guidance.

## Advanced topics

Consider the following for more advanced edge-to-edge use cases.

### Immersive mode

Some content, like videos or maps, benefits from a fully immersive experience
where system bars are hidden. You can hide system bars using
`WindowInsetsControllerCompat`:

```
val windowInsetsController =
    WindowCompat.getInsetsController(window, window.decorView)

// Hide the system bars.
windowInsetsController.hide(WindowInsetsCompat.Type.systemBars())

// Show the system bars.
windowInsetsController.show(WindowInsetsCompat.Type.systemBars()) For example, use either `Scaffold`,
```

### System bar colors and icons

When going edge-to-edge, your app's background might be visible behind the
system bars, so you may need to adjust system bar icon colors for better
contrast.

To change status bar icons to light or dark, use `WindowInsetsControllerCompat`:

```
// Set status bar icons to dark
WindowCompat.getInsetsController(window, window.decorView)
    .isAppearanceLightStatusBars = true

// Set status bar icons to light
WindowCompat.getInsetsController(window, window.decorView)
    .isAppearanceLightStatusBars = false
```

### System bar protection

While `enableEdgeToEdge()` provides default transparent or translucent system
bars, you might need to customize this. Consult the [Android system bars design
guidance](/design/ui/mobile/guides/foundations/system-bars) and [Edge-to-edge design guidance](/design/ui/mobile/guides/layout-and-content/edge-to-edge) to decide when to use
transparent versus translucent bars.

To make the 3-button navigation bar fully transparent instead of translucent,
you can disable contrast enforcement:

```
window.isNavigationBarContrastEnforced = false
```

For more information, see [About system bar protection](/develop/ui/compose/system/system-bars).

### Dialogs

To display full-screen dialogs edge-to-edge, call
`WindowCompat.enableEdgeToEdge` in the dialog's `onStart()` method:

```
class MyAlertDialogFragment : DialogFragment() {
    override fun onStart(){
        super.onStart()
        dialog?.window?.let { WindowCompat.enableEdgeToEdge(it) }
    }
    ...
}
```

[Next

About WindowInsetsRulers

arrow\_forward](/develop/ui/compose/system/evaluate-rulers)