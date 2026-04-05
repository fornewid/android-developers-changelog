---
title: https://developer.android.com/games/develop/multiplatform/support-large-screen-resizability
url: https://developer.android.com/games/develop/multiplatform/support-large-screen-resizability
source: md.txt
---

# Support large screen resizability

Expanding from phones to different large screen form factors introduces considerations for how your game handles window management. On[ChromeOS](https://chromeos.dev/en/games/optimizing-games-windowing)and[Google Play Games on PC](https://developer.android.com/games/playgames/graphics), your game can run in a windowed mode over a main desktop interface. On[new Android tablets and foldables](https://developer.android.com/guide/practices/screens-distribution#maxAspectRatio)running Android 12L (API level 32) or higher with screen width \> 600dp, your game can run side by side in[split-screen mode](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-multi-window-mode#split-screen_mode)with other applications, be resized, and even be moved between the inner and outer display on[foldable devices](https://developer.android.com/develop/ui/compose/layouts/adaptive/foldables/make-your-app-fold-aware)resulting in a configuration change for window size and, on some devices, orientation.

[Resizability with Unity games](https://developer.android.com/games/engines/unity/unity-large-screen)

## Basic large screen configuration

Declare whether your game is able to handle resizability:  

    <android:resizeableActivity="true" or "false" />

If unable to support resizability, ensure the game manifest explicitly defines the minimum and maximum supported aspect ratios:  

    <!-- Render full screen between 3:2 and 21:9 aspect ratio -->
    <!-- Let the platform letterbox otherwise -->
    <activity android:minAspectRatio="1.5">
    <activity android:maxAspectRatio="2.33">

### Google Play Games on PC

For Google Play Games on PC, the platform handles window resizability while respecting the specified aspect ratio. Window size is locked to the optimal dimensions automatically. You need to support at least 16:9 aspect ratio if your primary orientation is landscape and 9:16 aspect ratio if your game is portrait mode. For the best experience, explicitly support 21:9, 16:10, and 3:2 aspect ratios for a landscape game. Window resizability is not required here but is still good to have for other form factor compatibility.

For more information and best practices, see[Configure graphics for Google Play Games on PC.](https://developer.android.com/games/playgames/graphics#aspect-ratios)

### ChromeOS and Android large screens

To maximize the viewable area for your game in full screen on ChromeOS and large screen Android devices, support[full-screen immersive mode](https://developer.android.com/develop/ui/views/layout/immersive)and hide the system bars by setting flags on[`decorView`](https://developer.android.com/reference/kotlin/android/view/Window#getdecorview), system UI visibility, or through the[`WindowInsetsCompat`](https://developer.android.com/reference/kotlin/androidx/core/view/WindowInsetsCompat)API. You'll also want to gracefully handle rotation and resizing configuration events or prevent them from happening on ChromeOS devices.

Note that on large screen Android devices, your game can run in configurations that you might not already handle. If your game doesn't support all window size and orientation configurations, the platform letterboxes your game in[compatibility mode](https://developer.android.com/guide/topics/large-screens/large-screen-compatibility-mode)and, if necessary, prompts the player before changing to an unsupported configuration.
![](https://developer.android.com/static/images/games/multiplatform/configuration_compatibility_dialog.png)**Figure 1.**Configuration compatibility dialog.

On some devices, when a player moves to an unsupported configuration, they might be prompted with an option to reload the game and recreate the activity to best fit the new window layout, which disrupts the play experience. Test your game in various multi-window mode configurations (2/3, 1/2, 1/3 window size) and verify no gameplay or UI elements become cut off or inaccessible. Additionally, test how your game responds to foldable continuity when moving between the inner and outer screen on foldable devices. If you see issues, explicitly handle these configuration events and add advanced large screen resizability support.

## Advanced large screen resizability

Your browser doesn't support the video tag.**Figure 2.**Different UIs on desktop and foldable in tabletop posture.

To get out of compatibility mode and avoid activity recreation, do the following:

1. Declare your main activity as resizable:

       <android:resizeableActivity="true" />

2. Declare explicit support for "orientation", "screenSize", "smallestScreenSize", "screenLayout", and "density" in the[`android:configChanges`](https://developer.android.com/guide/topics/manifest/activity-element#config)attribute of the`<activity>`element of your game manifest to receive[all large screen configuration events](https://developer.android.com/guide/topics/resources/runtime-changes#handle-size-based):

       <android:configChanges="screenSize | smallestScreenSize | screenLayout | orientation | keyboard |
                               keyboardHidden | density" />

3. Override[`onConfigurationChanged()`](https://developer.android.com/reference/kotlin/android/view/View#onconfigurationchanged)and handle the configuration event, including the current orientation, window size, width, and height:

   ### Kotlin

   ```kotlin
   override fun onConfigurationChanged(newConfig: Configuration) {
      super.onConfigurationChanged(newConfig)
      val density: Float = resources.displayMetrics.density
      val newScreenWidthPixels =
   (newConfig.screenWidthDp * density).toInt()
      val newScreenHeightPixels =
   (newConfig.screenHeightDp * density).toInt()

      // Configuration.ORIENTATION_PORTRAIT or ORIENTATION_LANDSCAPE
      val newScreenOrientation: Int = newConfig.orientation

      // ROTATION_0, ROTATION_90, ROTATION_180, or ROTATION_270
      val newScreenRotation: Int =
   windowManager.defaultDisplay.rotation
   }
   ```

   ### Java

   ```java
   @Override
   public void onConfigurationChanged(Configuration newConfig) {
      super.onConfigurationChanged(newConfig);
      float density = getResources().getDisplayMetrics().density;
      int newScreenWidthPixels = (int) (newConfig.screenWidthDp * density);
      int newScreenHeightPixels = (int) (newConfig.screenHeightDp * density);

      // Configuration.ORIENTATION_PORTRAIT or ORIENTATION_LANDSCAPE
      int newScreenOrientation = newConfig.orientation;

      // ROTATION_0, ROTATION_90, ROTATION_180, or ROTATION_270
      int newScreenRotation = getWindowManager().getDefaultDisplay()
              .getRotation();
   }
   ```

You can also query the[`WindowManager`](https://developer.android.com/reference/kotlin/android/view/WindowManager)to check the current device rotation. Using this metadata, check the new window dimensions and render to the full window size. This might not work in all cases due to aspect ratio differences, so alternatively, anchor your game UI to the new window size and letterbox your core gameplay content. If there are technical or design limitations preventing either approach, do your own in-engine letterboxing to preserve aspect ratio, and scale to the best possible dimensions while declaring`resizeableActivity = false`and avoiding configuration mode.

Regardless of the approach you take,[test your game in various configurations](https://developer.android.com/docs/quality-guidelines/large-screen-app-quality)(fold and unfold, different rotation changes, split‑screen mode) and ensure there are no cut‑off or overlapping in‑game UI elements, issues with touch‑target accessibility, or aspect ratio issues causing the game to become stretched, squashed, or otherwise distorted.

Additionally, larger screens usually mean bigger pixels, because you have the same number of pixels for a much larger area. This can cause pixelation for downsized render buffers or lower resolution assets. Use your highest quality assets on large screen devices and[performance profile your game](https://developer.android.com/agi)to ensure there are no issues. If your game supports multiple quality levels, ensure that it accounts for large screen devices.

### Multi-window mode

[Multi-window mode](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-multi-window-mode)enables multiple apps to share the same screen simultaneously. Multi‑window mode does not change the[activity lifecycle](https://developer.android.com/training/basics/activity-lifecycle); however, the resumed state of apps in multiple windows differs on different versions of Android (see[Activity lifecycle in multi-window mode](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-multi-window-mode#lifecycle)in[Support multi-window mode](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-multi-window-mode)).

When the player puts an app or game into multi-window mode, the system notifies the activity of a configuration change as specified in the[Advanced large screen resizability](https://developer.android.com/games/develop/multiplatform/support-large-screen-resizability#advanced_large_screen_resizability)section. A configuration change also happens when the player resizes the game or puts the game back into full‑screen mode.

There is no guarantee that the application will regain focus when it is put into multi‑window mode. Therefore, if you use any of the app state events to pause your game, do not rely on the acquire focus event ([`onWindowFocusChanged()`](https://developer.android.com/reference/android/app/Activity#onWindowFocusChanged(boolean))with focus value as true) to resume the game. Instead, use other event handlers or state change handlers such as`onConfigurationChanged()`or`onResume()`. Note that you can always use the[`isInMultiWindowMode()`](https://developer.android.com/reference/kotlin/android/app/Activity#isinmultiwindowmode)method to detect whether the current activity is running in multi-window mode.

With multi-window mode on ChromeOS, the initial window dimensions become an important consideration. A game need not be full screen, and you'll want to declare what the size of the window should be for that case. There are two recommended ways to approach this.

The first option works by using specific attributes on the[`<layout>`](https://developer.android.com/guide/topics/manifest/layout-element)tag in your Android manifest. The`defaultHeight`and`defaultWidth`attributes control the initial dimensions. Be mindful as well of the`minHeight`and`minWidth`attributes to prevent your players from resizing the game window into dimensions that you don't support. Lastly, there is the`gravity`attribute, which determines where on the screen the window appears when launched. Here's an example layout tag using these attributes:  

    <layout android:defaultHeight="500dp"
            android:defaultWidth="600dp"
            android:gravity="top|end"
            android:minHeight="450dp"
            android:minWidth="300dp" />

The second option for setting window size works through using dynamic launch bounds. By using[`setLaunchBounds(Rect)⁠⁠`](https://developer.android.com/reference/android/app/ActivityOptions#setLaunchBounds(android.graphics.Rect)), you can define the starting window dimensions. If an empty rectangle is specified, the activity is started in a maximized state.

Additionally, if you are using the Unity or Unreal game engines, ensure you are using a recent version (Unity 2019.4.40 and Unreal 5.3 or newer) that provides good support for multi-window mode.
| **Note:**
|
| - Android 12 (API level 31) makes multi-window mode the default behavior for devices with smallest width \>= 600dp. The \`resizeableActivity\` attribute indicates whether an activity can be resized. For complete details, see[Support multi-window mode](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-multi-window-mode).
| - Android 16 (API level 36) ignores screen orientation, aspect ratio, and resizability restrictions to optimize apps on devices of all sizes and configurations. See[App orientation, aspect ratio, and resizability](https://developer.android.com/develop/ui/compose/layouts/adaptive/app-orientation-aspect-ratio-resizability#exceptions)exceptions to learn how to exclude games from the Android 16 behavior.

### Foldable posture support

Use the Jetpack[WindowManager layout library](https://developer.android.com/reference/kotlin/androidx/window/layout/package-summary)to support foldable postures, such as tabletop, to increase player immersion and engagement:
![](https://developer.android.com/static/images/games/multiplatform/foldable_posture_support.png)**Figure 3.**Game in tabletop posture with main view on vertical portion of display, controls on horizontal portion.  

### Kotlin

```kotlin
fun isTableTopPosture(foldFeature : FoldingFeature?) : Boolean {
    contract { returns(true) implies (foldFeature != null) }
    return foldFeature?.state == FoldingFeature.State.HALF_OPENED &&
            foldFeature.orientation == FoldingFeature.Orientation.HORIZONTAL
}
```

### Java

```java
boolean isTableTopPosture(FoldingFeature foldFeature) {
    return (foldFeature != null) &&
           (foldFeature.getState() == FoldingFeature.State.HALF_OPENED) &&
           (foldFeature.getOrientation() == FoldingFeature.Orientation.HORIZONTAL);
}
```