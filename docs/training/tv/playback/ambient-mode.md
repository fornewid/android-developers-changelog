---
title: Ambient Mode  |  Android TV  |  Android Developers
url: https://developer.android.com/training/tv/playback/ambient-mode
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android TV](https://developer.android.com/training/tv)

# Ambient Mode Stay organized with collections Save and categorize content based on your preferences.




Ambient Mode is a screensaver built into Google TV and Android TV. Its purpose
is to avoid displaying static images for extended periods. This is important
for display technologies, such as OLED, which may be susceptible to screen burn.

The OS will put the device into Ambient Mode after 10 minutes of user
inactivity. After a further period of user inactivity (defined by the device
Energy Saver setting) the OS will enter Energy Saver mode,
powering the display off. Media playback apps may prevent the device
from entering Ambient Mode, despite the user not interacting with it, for
example, while watching a movie.

If the user interacts with the device within 30 minutes of entering Ambient
Mode, the app that was active when Ambient Mode was entered will be restored.
If the user interacts with the device more than 30 minutes after entering
Ambient Mode, they will be returned to the Home screen.
When the user starts the device using the power button while it's in Energy
Saver mode, they will be taken to the Home screen. Alternatively, if the user
starts the device while it's in Energy Saver mode using specific app buttons
(for example, YouTube) they will be taken directly to that app.

**Note:** It is important to ensure that your app meets
[the Ambient Mode requirements](/docs/quality-guidelines/tv-app-quality#ambient-mode)
when submitting it to Google Play.

## Video playback

For video playback, it's important to [prevent the device entering Ambient Mode
during user-initiated playback](/docs/quality-guidelines/tv-app-quality#TV-BU)
to provide an uninterrupted viewing experience. However, apps should *not*
prevent devices from entering Ambient Mode when playback is stopped or paused.

## Audio playback

For audio playback, apps
[should not prevent Ambient Mode during playback](/docs/quality-guidelines/tv-app-quality#TV-BA)
unless they implement their own screensaver with non-static imagery.
Audio playback will continue while Ambient Mode is active.

Audio playback on Android will implicitly hold a
[partial wake lock](/reference/android/os/PowerManager#PARTIAL_WAKE_LOCK).
This will *not* prevent the device from entering Ambient Mode, but *will*
prevent the subsequent transition to Energy Saver mode. Playback will therefore
continue even after the device enters Ambient Mode, but the device will be
prevented from going to sleep to allow uninterrupted playback.

## Preventing Ambient Mode

It is possible to prevent the OS from putting the device into Ambient Mode, but
this must be used in accordance with
[Ambient Mode requirements](/docs/quality-guidelines/tv-app-quality#ambient-mode).
App developers cannot prevent the device from entering
Energy Saver mode.

Apps can prevent the screen from turning off by setting a flag on the
[`Window`](/reference/android/view/Window):

### Kotlin

```
requireActivity().window.addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON)
```

### Java

```
requireActivity().getWindow().addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON);
```

Ambient Mode will be disabled while this flag is set. To re-enable it you must
clear the flag:

### Kotlin

```
requireActivity().window.clearFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON)
```

### Java

```
requireActivity().getWindow().clearFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON);
```

**Note:** You must only prevent the device from entering Ambient Mode for user-initiated playback sessions. If your app is
[automatically playing video or animations](/docs/quality-guidelines/tv-app-quality#TV-BY),
you must *not* set the
[`FLAG_KEEP_SCREEN_ON`](/reference/android/view/WindowManager.LayoutParams#FLAG_KEEP_SCREEN_ON)
flag.

[Previous

arrow\_back

Add a guided step](/training/tv/playback/leanback/guided-step)

[Next

Playback controls on TV

arrow\_forward](/training/tv/playback/controls)