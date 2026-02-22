---
title: https://developer.android.com/training/tv/games
url: https://developer.android.com/training/tv/games
source: md.txt
---

The television screen presents a number of considerations that may be new to mobile game
developers. These areas include its large size, its control scheme, and the fact that all players
are viewing it simultaneously.

## Display


The two main things to keep in mind when developing games for the TV screen are designing your
your game for a landscape orientation and providing support for low latency.

### Support landscape display


A TV is always sideways: You can't turn it, and there is no portrait orientation. Always design
your TV games to be displayed in landscape mode.

### Auto low latency mode


Certain displays can perform graphics post-processing. This post-processing improves graphics
quality but can increase latency. Newer displays that support HDMI 2.1 have an *auto low
latency mode* (*ALLM* ), which minimizes latency by switching off this post-processing. For
more details on ALLM, refer to the
[HDMI 2.1 specification](https://www.hdmi.org/spec/hdmi2_1). Other
displays may support a *game mode* with similar behavior.


In Android 11 and later, a window can request that auto low latency mode or game
mode be used, if available, by requesting *minimal post-processing*. This is particularly
useful for game and videoconferencing applications, where low latency is more important than
having the best possible graphics.


To enable or disable minimal post-processing, call
[Window.setPreferMinimalPostProcessing()](https://developer.android.com/reference/android/view/Window#setPreferMinimalPostProcessing(boolean)),
or set the window's
[preferMinimalPostProcessing](https://developer.android.com/reference/android/R.attr#preferMinimalPostProcessing)
attribute to `true`. Not all displays support minimal post-processing; to find out if a
particular display does support it, call the
[Display.isMinimalPostProcessingSupported()](https://developer.android.com/reference/android/view/Display#isMinimalPostProcessingSupported()) method.

## Input devices


TVs don't have touch interfaces, so it's even more important to get your controls right and make
sure players find them intuitive and fun to use. Handling controllers
also introduces some other issues to pay attention to, like keeping track of multiple
controllers, and handling disconnects gracefully. All TV apps, including games, should handle
controllers consistently. Read [Manage TV
controllers](https://developer.android.com/training/tv/start/controllers) for more information about using TV controllers and
[Handle controllers for games](https://developer.android.com/training/tv/start/controllers#games) for specific
information about using TV controllers for games.

## Keyboard layouts


In Android 13 (API level 33) and higher, you can determine keyboard layouts using
[getKeyCodeForKeyLocation()](https://developer.android.com/reference/android/view/InputDevice#getKeyCodeForKeyLocation(int)).
For example, your game supports movement using the WASD keys, but this may not work correctly on
an AZERTY keyboard which has the A and W keys in different locations. You can get the keycodes
for the keys you expect at certain positions:  

### Kotlin

```kotlin
val inputManager: InputManager? = requireActivity().getSystemService()

inputManager?.inputDeviceIds?.map { inputManager.getInputDevice(it) }
    ?.firstOrNull { it.keyboardType == InputDevice.KEYBOARD_TYPE_ALPHABETIC }
    ?.let { inputDevice ->
        keyUp = inputDevice.getKeyCodeForKeyLocation(KeyEvent.KEYCODE_W)
        keyLeft = inputDevice.getKeyCodeForKeyLocation(KeyEvent.KEYCODE_A)
        keyDown = inputDevice.getKeyCodeForKeyLocation(KeyEvent.KEYCODE_S)
        keyRight = inputDevice.getKeyCodeForKeyLocation(KeyEvent.KEYCODE_D)
    }
```

### Java

```java
InputManager inputManager = requireActivity().getSystemService(InputManager.class);
InputDevice inputDevice = Arrays.stream(inputManager.getInputDeviceIds())
        .mapToObj(inputManager::getInputDevice)
        .filter( device -> device.getKeyboardType() == InputDevice.KEYBOARD_TYPE_ALPHABETIC)
        .filter(Objects::nonNull)
        .findFirst()
        .orElse(null);
if (inputDevice != null) {
    keyUp = inputDevice.getKeyCodeForKeyLocation(KeyEvent.KEYCODE_W);
    keyLeft = inputDevice.getKeyCodeForKeyLocation(KeyEvent.KEYCODE_A);
    keyDown = inputDevice.getKeyCodeForKeyLocation(KeyEvent.KEYCODE_S);
    keyRight = inputDevice.getKeyCodeForKeyLocation(KeyEvent.KEYCODE_D);
}
```


In this example, with an AZERTY keyboard, `keyUp` is set to
`KeyEvent.KEYCODE_Z`, `keyLeft` is set to `KeyEvent.KEYCODE_Q`,
while `keyDown` and `keyRight` are set to `KeyEvent.KEYCODE_S`
and `KeyEvent.KEYCODE_D` respectively. You can now create key event handlers for these
key codes and implement the expected behavior.

## Manifest

There are some special things games should include in the Android manifest.

### Show your game on the home screen


The Android TV home screen displays games in a separate row from regular apps.
To make your game appear in the list of games, set the
[`android:isGame`](https://developer.android.com/guide/topics/manifest/application-element#isGame) attribute to `"true"` in your app manifest's
[`<application>`](https://developer.android.com/guide/topics/manifest/application-element) tag. For example:  

```xml
<application
    ...
    android:isGame="true"
    ...
>
```

### Declare support for game controllers


Games controllers may not be available or active for users of a TV device. In order to properly
inform users that your game supports a game controller, you must include the following entry in
your app manifest:  

```xml
  <uses-feature android:name="android.hardware.gamepad" android:required="false"/>
```


**Note:** When specifying `android:hardware:gamepad` support, do not set the
`android:required` attribute to `"true"`. If you do this, users won't be able to
install your app on TV devices.

For more information about manifest entries, see
[App manifest](https://developer.android.com/guide/topics/manifest/manifest-intro).

## Google Play games services


If your game integrates [Google Play games services](https://developers.google.com/games/services/),
you should keep in mind a number of
considerations pertaining to achievements, sign-in, and saving games.

### Achievements


Your game should include at least five (earnable) achievements. Only a user controlling gameplay
from a supported input device should be able to earn achievements. For more information about
achievements and how to implement them, see [Achievements in Android](https://developers.google.com/games/services/android/achievements).

### Sign-in


Your game should attempt to sign the user in on launch. If the player declines sign-in several
times in a row, your game should stop asking. Learn more about sign-in at [Implementing sign-in on
Android](https://developers.google.com/games/services/training/signin).

### Saving


Use Google Play Services [Saved Games](https://developers.google.com/games/services/common/concepts/savedgames) to store
your game save. Your game should bind game saves to a specific Google Account, so as to be
uniquely identifiable even across devices: Whether the player is using a handset or a TV, the
game should be able to pull the game-save information from the same user account.


You should also provide an option in your game's UI to allow the player to delete locally and
cloud-stored data. You might put the option in the game's `Settings` screen. For
specifics on implementing saved games using Play Services, see [Saved Games in Android](https://developers.google.com/games/services/android/savedgames).

### Exit

Provide a consistent and obvious UI element that lets the user exit the game gracefully. This
element should be accessible with the D-pad navigation buttons. Do this instead of relying on the
Home button to provide an exit, as that is not consistent nor reliable across different controllers.

## Web


Do not enable web browsing in games for Android TV. Android TV does not support a web browser.


**Note:** You can use the [WebView](https://developer.android.com/reference/android/webkit/WebView) class for logins to
social media services.

## Networking

Games frequently need greater bandwidth to provide optimum performance, and many users prefer
ethernet to WiFi to provide that performance. Your app should check for both WiFi and ethernet
connections. If your app is for TV only, you do not need to check for 3G/LTE service as you would
for a mobile app.