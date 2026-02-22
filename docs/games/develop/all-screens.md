---
title: https://developer.android.com/games/develop/all-screens
url: https://developer.android.com/games/develop/all-screens
source: md.txt
---

# Develop games for all screens

When developing a game for Android, it's important to anticipate the variety of possible player experiences and remain adaptive to a player's real-time interaction needs. By supporting different player experiences, you increase gameplay flexibility, helping you expand your game's reach.

Specific differences in player experience include the following:

- **Device form factors:**Although phones provide the traditional Android device experience, it's possible to interact with games on other form factors. ChromeOS devices can run an Android container that displays your game. Tablets that can run Android support several different levels of fidelity. Android TV devices support more detail-rich and more immersive experiences. Players can simulate a multi-window environment by using a display extension tool. And when using foldables, players can change the size of the screen during a gameplay session.
- **Interaction methods:**Players can provide input by touching a device's screen, but they can also use a mouse, touchpad, keyboard, or controller instead. In addition, the availability of display extension tools and foldable devices allows players to experience your game on a larger screen, making longer gameplay sessions and more complex interfaces more feasible.
- **Hardware support:**Some Android-powered devices don't have hardware that is more typical in a handheld device, such as a rear-facing camera, a GPS, and network connectivity. Your game should adapt to the hardware that's available and gracefully handle situations where certain features aren't available.

This guide presents best practices related to developing your game for different types of screens and user interactions. This guide also provides suggestions on designing your game and developing an effective testing strategy.

## Game design best practices

When planning your game's design and architecture, follow the best practices described in the following sections.

### Respond to configuration changes manually

When the Android system detects a*configuration change* , such as a change in screen size, screen orientation, or input method, the system by default restarts the current activity. To preserve state within an app or game, the activity by default calls[`onSaveInstanceState()`](https://developer.android.com/reference/android/app/Activity#onSaveInstanceState(android.os.Bundle))before it restarts and[`onRestoreInstanceState()`](https://developer.android.com/reference/android/app/Activity#onRestoreInstanceState(android.os.Bundle))after it restarts. This process, however, requires the activity to reload all associated services and resources. To learn more about this default behavior,[see the guide on handling configuration changes](https://developer.android.com/guide/topics/resources/runtime-changes).

A typical gameplay session undergoes several configuration changes. If your game lets the system handle each configuration change, your game's scene is destroyed and restarted over and over, reducing your game's performance. For this reason, we**highly encourage**you to handle these configuration changes yourself in your game.

To learn how to add this configuration change logic to your game,[see the section on how to create custom configuration change handlers](https://developer.android.com/games/develop/all-screens#custom-config-change-handlers).

### Create a flexible architecture

To add support for your game on as many devices as possible, follow these best practices:

- **Deploy Android App Bundles instead of individual APKs.** [Android App Bundles](https://developer.android.com/guide/app-bundle)allow you to package artifacts of different resolutions and different architecture models, such as x86, ARM, into a single artifact. Better still, Android App Bundles support higher size limits for your game; each base APK can be as large as 150 MB, and the bundle itself can be many gigabytes in size.
- **Add support for x86 architectures.**This step improves your game's performance on devices that don't support ARM, because these devices can now execute instructions without having to translate them first.

### Add support for Vulkan

By supporting[Vulkan](https://developer.android.com/ndk/guides/graphics), your game can achieve higher graphics performance. Most devices support this graphics API.

## Create custom configuration change handlers

To declare the types of configuration changes that your game handles itself, add the[`android:configChanges`](https://developer.android.com/guide/topics/manifest/activity-element#config)attribute to each`<activity>`element in your manifest that represents a screen or complex interface.

The following code snippet demonstrates how to declare that your game takes care of screen size, screen orientation, and input method changes:  

```xml
<activity ...
    android:configChanges="screenSize|orientation|keyboard|keyboardHidden">
</activity>
```

When the declared configuration changes occur, the system now invokes a different method,[`onConfigurationChanged()`](https://developer.android.com/reference/android/app/Activity#onConfigurationChanged(android.content.res.Configuration)). Within this method, add logic to update your game's UI:

- Update the scale factor and orientation of the screen. Keep in mind that, for performance purposes, it's sometimes better to[scale your game's UI along only one dimension](https://developer.android.com/topic/performance/games#touch-to-display-latency).
- Identify the optimal input method for the player to use.

## Handle screen configuration changes

Your game handles screen size and screen orientation changes manually whenever you include the`screenSize`and`orientation`values, respectively, in an[`android:configChanges`](https://developer.android.com/guide/topics/manifest/activity-element#config)attribute. You can use these new values to update your scene's content and player input areas. For guidance on how to design your game's layout to make it easier to update,[see the guide on supporting different screen sizes](https://developer.android.com/training/multiscreen/screensizes).

In your game's implementation of`onConfigurationChanged()`, use the passed-in[`Configuration`](https://developer.android.com/reference/android/content/res/Configuration)object and the window manager's[`Display`](https://developer.android.com/reference/android/view/Display)object to determine the updated values for screen size and screen orientation, respectively.
| **Caution:** The display's rotation value depends on the device's default hardware orientation. As a result, a value of`0`indicates portrait orientation on some devices and landscape orientation on other devices.

The following code snippet shows how to obtain your game's updated screen size and orientation:  

### Kotlin

```kotlin
override fun onConfigurationChanged(newConfig: Configuration) {
    super.onConfigurationChanged(newConfig)
    val density: Float = resources.displayMetrics.density
    val newScreenWidthPixels = (newConfig.screenWidthDp * density).toInt()
    val newScreenHeightPixels = (newConfig.screenHeightDp * density).toInt()

    // Get general orientation; either Configuration.ORIENTATION_PORTRAIT or
    // Configuration.ORIENTATION_LANDSCAPE.
    val newScreenOrientation: Int = newConfig.orientation

    // Get general rotation; one of: ROTATION_0, ROTATION_90, ROTATION_180,
    // or ROTATION_270.
    val newScreenRotation: Int = windowManager.defaultDisplay.rotation
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

    // Get general orientation; either Configuration.ORIENTATION_PORTRAIT or
    // Configuration.ORIENTATION_LANDSCAPE.
    int newScreenOrientation = newConfig.orientation;

    // Get general rotation; one of: ROTATION_0, ROTATION_90, ROTATION_180,
    // or ROTATION_270.
    int newScreenRotation = getWindowManager().getDefaultDisplay()
            .getRotation();
}
```

Note that changing the pose of a foldable device changes the configuration, even if your app runs in[fullscreen mode](https://developer.android.com/games/develop/all-screens#fullscreen). As a result, your app might have to handle changes to screen size or pixel density if the user folds or unfolds the device while your game is running.

### Game-specific screen qualities

The following sections describe how to adjust how your game reacts to screen size or screen orientation changes, depending on your game's qualities:

#### Fullscreen mode

On some platforms, such as ChromeOS, Android apps and games can be windowed and resizeable by default. If your game should always run in fullscreen mode, you can set the[`android:resizeableActivity`](https://developer.android.com/guide/topics/manifest/activity-element#resizeableActivity)attribute to`false`in one of your`<activity>`elements, as shown in the following code snippet:  

```xml
<activity ...
    android:resizeableActivity="false">
</activity>
```
| **Note:** The`android:resizeableActivity`attribute affects your game only on devices running Android 7.0 (API level 24) or higher.

You can also set`android:resizeableActivity`attribute to`false`to prevent size-based configuration changes from occurring. Unless your game always runs in fullscreen mode, however, you should add this attribute only as a temporary fix for testing purposes.

#### Screen orientation

If your game depends on a device's sensors having a specific orientation, specify a value for[`android:screenOrientation`](https://developer.android.com/guide/topics/manifest/activity-element#screen)in your game's activity, as shown in the following code snippet. This setting helps prevent a scene in your game from flipping upside down unexpectedly.  

```xml
<activity ...
    android:screenOrientation="landscape">
</activity>
```

### Device-specific screen qualities

The following sections describe how to handle screen-based configuration changes given specific qualities that some devices have.

#### Aspect ratio

Some devices support different aspect ratios. For example, foldable devices are designed to support an aspect ratio of 21:9 when in the folded state. To handle this potential variety in aspect ratio, do at least one of the following:

- **Target Android 8.0 (API level 26) or higher.**
- **Make your game's scene and interface resizeable.** Set[`android:resizeableActivity`](https://developer.android.com/guide/topics/manifest/activity-element#resizeableActivity)to`true`on devices running Android 7.0 (API level 24) and higher.
- **Declare a maximum supported aspect ratio.** In a[`<meta-data>`](https://developer.android.com/guide/topics/manifest/meta-data-element)attribute associated with your game, set`android.max_aspect`to`2.4`, as shown in the following code snippet. Keep in mind, however, that aspect ratios larger than the one you've specified cause the game to appear[letterboxed](https://en.wikipedia.org/wiki/Letterboxing_(filming))within a display.

  ```xml
  <application>
  <meta-data android:name="android.max_aspect"
             android:value="2.4" />
  </application>
  ```

#### Multiple activities visible simultaneously

Many modern devices support a variety of screen layouts, including split-screen, picture-in-picture, and large display areas. When using one of these layouts, the system can make multiple activities visible at the same time.

On devices running Android 9 (API level 28) or higher, it's possible for all top visible activities to be resumed at the same time. In order for this behavior to work, however, both your game and the device's OEM need to opt into the functionality. You can add support within your game by setting`android.allow_multiple_resumed_activities`to`true`in your game's manifest, as shown in the following snippet:  

```xml
<application>
    <meta-data android:name="android.allow_multiple_resumed_activities"
               android:value="true" />
</application>
```

You can then test your game on different devices to see which of them provide the OEM support necessary for multi-resume to function properly.
| **Note:** Without support from both your game and the device's OEM, the only activity that is resumed the one that most recently received player input; all other visible activities are in either the started or paused state.

For more information on configuring your game to appear as part of a multi-window display,[see the guide on how to add multi-window support](https://developer.android.com/guide/topics/ui/multi-window).

## Handle different types of interaction models

Your game handles keyboard presence and keyboard availability manually whenever you include the`keyboard`and`keyboardHidden`values, respectively, in an[`android:configChanges`](https://developer.android.com/guide/topics/manifest/activity-element#config)attribute. You can use these new values to update your game's primary input method.

When configuring your game for supporting multiple types of user input, keep the following in mind:

- **Detect input methods rather than individual devices.**This mindset makes it easier to improve the player experience without focusing too much on the specific device that the player might have.
- **Include the`keyboardHidden`attribute in your list of manually-handled configuration changes.**That way, your game can keep track of when a keyboard is physically attached to the device but unusable.
- **Determine input methods that are currently available.** To do so, call[`getInputDeviceIds()`](https://developer.android.com/reference/android/hardware/input/InputManager#getInputDeviceIds())on game startup and after each configuration change.

  You can often determine how the player plans to interact with your game based on their preferred input device:
  - Players typically use a keyboard or game controller to perform rapid button sequences.
  - Players typically use a touchscreen or touchpad to perform more complex gestures.
  - Players typically use a mouse to perform higher-precision input.

  | **Note:** Input method availability can be volatile while players are interacting with your game. For example, they might disconnect a keyboard and plug in a controller while playing your game.

The following sections provide best practices for specific types of input devices.

### Keyboard

When creating a keyboard layout for your game, consider how the player navigates through a given scene as well as how they interact with your game's settings.

The WASD keys or arrow keys are usually best for controlling character movement. It's also best to assign a particular key for each important action or skill that a controllable character can perform within your game. To maximize the player experience, consider adding support for custom key bindings in your game.

Players should also be able to open your game's menus and navigate through them using the keyboard. The`Esc`key is a common mapping for pausing a scene and showing the game's menu.
| **Note:** Even if players interact with your game more often using a mouse or touchpad, it's important to add keyboard support to serve as an alternate input method for players with accessibility needs.

For more information on supporting keyboard input in your game, see the[guide on how to support keyboard navigation](https://developer.android.com/training/keyboard-input/navigation)as well as the[guide on how to handle keyboard actions](https://developer.android.com/training/keyboard-input/commands).

### Game controller

For more information on handling controller input in your game,[see the guide on how to support game controllers](https://developer.android.com/games/sdk/game-controller).

### Mouse or touchpad

If your game supports player input from a mouse or touchpad, keep in mind that players interact with the device in ways other than playing your game. It's important to be aware that, by requesting pointer capture, all mouse input is directed to your game. Therefore, after your game has the information it needs, release pointer capture so that players regain standard mouse control of their device.

On devices running Android 8.0 (API level 26) and higher, you can use the Mouse Capture API to assist with the pointer capture process. In games that react to high-precision input, you can get the pointer's current coordinates by calling the[`getX()`](https://developer.android.com/reference/android/view/MotionEvent#getX())and[`getY()`](https://developer.android.com/reference/android/view/MotionEvent#getY())methods.

For additional information on adding support for mouse input and touchpad input in your game, see the[guide on how to track touch and pointer movements](https://developer.android.com/training/gestures/movement)as well as the[guide on how to handle multi-touch gestures](https://developer.android.com/training/gestures/multi).

## Test your game

Before launching your game, test how it responds to configuration changes by completing the steps described in the following sections.

### Update your test plan

When validating your game's functionality, include the following test cases:

- Minimize and maximize the window that contains your game. (Doesn't apply if your game is always in fullscreen mode.)
- Change screen size.
- Change screen orientation. (Doesn't apply if your game has a fixed orientation.)
- Connect and disconnect input devices, such as keyboards and mice.
- Perform multi-resume, if your game supports it.

Also, consider updating your game's quality control system so that you can optimize for a wider variety of player experiences.

For best practices related to testing your game, see the[Fundamentals of Testing guide](https://developer.android.com/training/testing/fundamentals).

### Use testing and debugging tools

You can perform tests using a variety of tools that the platform supports:

- Emulators, including the[Android emulator](https://developer.android.com/studio/run/emulator)and[Firebase Test Lab](https://firebase.google.com/docs/test-lab).

  | **Note:** The Android emulator includes support for[Chrome OS](https://developer.android.com/topic/arc/emulator)and[foldable](https://developer.android.com/guide/topics/ui/foldables#emulators)devices.
- [System tracing](https://developer.android.com/topic/performance/tracing).

- [ChromeOS Performance Analyzer](https://www.chromium.org/chromium-os/testing/perf-data), available when running ChromeOS M75 or higher.