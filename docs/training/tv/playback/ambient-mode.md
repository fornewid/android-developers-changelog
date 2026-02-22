---
title: https://developer.android.com/training/tv/playback/ambient-mode
url: https://developer.android.com/training/tv/playback/ambient-mode
source: md.txt
---

# Ambient Mode is a screensaver built into Google TV and Android TV. Its purpose is to avoid displaying static images for extended periods. This is important for display technologies, such as OLED, which may be susceptible to screen burn.

The OS will put the device into Ambient Mode after 10 minutes of user inactivity. After a further period of user inactivity (defined by the device Energy Saver setting) the OS will enter Energy Saver mode, powering the display off. Media playback apps may prevent the device from entering Ambient Mode, despite the user not interacting with it, for example, while watching a movie.

If the user interacts with the device within 30 minutes of entering Ambient Mode, the app that was active when Ambient Mode was entered will be restored. If the user interacts with the device more than 30 minutes after entering Ambient Mode, they will be returned to the Home screen. When the user starts the device using the power button while it's in Energy Saver mode, they will be taken to the Home screen. Alternatively, if the user starts the device while it's in Energy Saver mode using specific app buttons (for example, YouTube) they will be taken directly to that app.
| **Note:** It is important to ensure that your app meets[the Ambient Mode requirements](https://developer.android.com/docs/quality-guidelines/tv-app-quality#ambient-mode)when submitting it to Google Play.

## Video playback

For video playback, it's important to[prevent the device entering Ambient Mode during user-initiated playback](https://developer.android.com/docs/quality-guidelines/tv-app-quality#TV-BU)to provide an uninterrupted viewing experience. However, apps should*not*prevent devices from entering Ambient Mode when playback is stopped or paused.

## Audio playback

For audio playback, apps[should not prevent Ambient Mode during playback](https://developer.android.com/docs/quality-guidelines/tv-app-quality#TV-BA)unless they implement their own screensaver with non-static imagery. Audio playback will continue while Ambient Mode is active.

Audio playback on Android will implicitly hold a[partial wake lock](https://developer.android.com/reference/android/os/PowerManager#PARTIAL_WAKE_LOCK). This will*not* prevent the device from entering Ambient Mode, but*will*prevent the subsequent transition to Energy Saver mode. Playback will therefore continue even after the device enters Ambient Mode, but the device will be prevented from going to sleep to allow uninterrupted playback.

## Preventing Ambient Mode

It is possible to prevent the OS from putting the device into Ambient Mode, but this must be used in accordance with[Ambient Mode requirements](https://developer.android.com/docs/quality-guidelines/tv-app-quality#ambient-mode). App developers cannot prevent the device from entering Energy Saver mode.

Apps can prevent the screen from turning off by setting a flag on the[`Window`](https://developer.android.com/reference/android/view/Window):  

### Kotlin

```kotlin
requireActivity().window.addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON)
```

### Java

```java
requireActivity().getWindow().addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON);
```

Ambient Mode will be disabled while this flag is set. To re-enable it you must clear the flag:  

### Kotlin

```kotlin
requireActivity().window.clearFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON)
```

### Java

```java
requireActivity().getWindow().clearFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON);
```
| **Note:** You must only prevent the device from entering Ambient Mode for user-initiated playback sessions. If your app is[automatically playing video or animations](https://developer.android.com/docs/quality-guidelines/tv-app-quality#TV-BY), you must*not* set the[`FLAG_KEEP_SCREEN_ON`](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#FLAG_KEEP_SCREEN_ON)flag.