---
title: https://developer.android.com/docs/quality-guidelines/tv-app-quality
url: https://developer.android.com/docs/quality-guidelines/tv-app-quality
source: md.txt
---

Users have different expectations when watching TV than when they are using a
phone or tablet. A typical TV user sits about 10 feet away from the screen,
so small details are less noticeable and small text is hard to read. Since
users sit away from a TV, they must use a remote control device to navigate
and make selections rather than touching elements on the screen. These
differences significantly affect the requirements for what makes a good TV
user experience.

The first step toward creating a great experience for TV users is to review
and follow the [Android TV design guidelines](https://developer.android.com/design/tv). To
understand the fundamental implementation requirements for a TV app, also
review the [Build TV Apps](https://developer.android.com/training/tv/start) training.

For information about how to publish your TV apps in Google Play, see
[Distribute to Android TV](https://developer.android.com/training/tv/publishing/checklist#distribute-to-android-tv).

## Visual design and user interaction

The following criteria help ensure that your app follows critical design and
interaction patterns for a consistent, intuitive, and enjoyable user
experience on TV devices.

| Type | Test | Description |
|---|---|---|
| Launcher | TV-LM | The app displays a launcher icon in the Android TV Launcher after installation. For more information, see [Declare a TV activity](https://developer.android.com/training/tv/start/start#tv-activity). |
| Launcher | TV-LB | The app displays both a 320x180 pixel full-size banner and at least a 160x160 pixel (at `xhdpi` density) app icon as its launcher icons in the Android TV Launcher. For more information, see [Android TV app icon and banner guidelines](https://developer.android.com/design/ui/tv/guides/system/tv-app-icon-guidelines). |
| Launcher | TV-BN | The app launch banner contains the name of the app. |
| Launcher | TV-LG | If the app is a game, it appears in the Games row in the Android TV Launcher. For more information, see [Show your game on the home screen](https://developer.android.com/training/tv/games#Launcher). |
| Launcher | TV-LS | The app runs successfully and without error messages, including during installation, loading, and testing. For more information, see [Run TV apps](https://developer.android.com/training/tv/start/start#run). |
| Layout | TV-LO | All app interfaces are presented in landscape orientation and without vertical letterboxing/pillarboxing. Only black color may be used for bars on original format videos. For more information, see [Build basic TV layouts](https://developer.android.com/training/tv/start/layouts#structure). |
| Layout | TV-OV | The app does not display any text or functionality that is partially cut off by the edges of the screen. For more information, see [Overscan](https://developer.android.com/training/tv/start/layouts#overscan). |
| Layout | TV-TR | The app does not partially obscure other apps. The app fills the entire screen and has a non-transparent background. |
| Navigation | TV-DP | The app functionality is navigable using five-way D-pad controls---unless the app requires a game controller, as specified in the TV-GP criterion in the Controllers section of the Functionality table that follows. For more information, see [TV Navigation](https://developer.android.com/training/tv/start/navigation#d-pad-navigation). |
| Navigation | TV-DK | If the app requires a game controller, as specified in the TV-GP criterion, all functionality is navigable using standard Android game controller keys. For more information, see [Process gamepad button presses](https://developer.android.com/training/game-controllers/controller-input#button). |
| Navigation | TV-DM | The app does not depend on a remote control device having a Menu button to access user interface controls. |
| Navigation | TV-DB | Back button presses lead back to the Android TV home screen. For more information, see [Provide appropriate Back-button behavior](https://developer.android.com/training/tv/start/controllers#back-button). |
| Navigation | TV-DL | If the app has a live TV feed integrated on the Live tab, the app meets frictionless playback and direct-back requirements. For more information, see [Back Button](https://developer.android.com/training/tv/start/navigation#back_button). |
| Search | TV-SB | An in-app search query shows up in the search box, similar to the user interface provided by `https://developer.android.com/reference/androidx/leanback/app/SearchFragment`, and results are relevant to that query. For more information, see [Search within TV apps](https://developer.android.com/training/tv/discovery/in-app-search). |

## Functionality and performance

These criteria help verify that your app is configured correctly and provides
the expected functional behavior.

| Type | Test | Description |
|---|---|---|
| SDK | TV-PS | In addition to the [core performance and stability requirements](https://developer.android.com/docs/quality-guidelines/core-app-quality#ps), your app must support commonly used Android TV devices by setting a [minimum Android SDK version](https://developer.android.com/guide/topics/manifest/uses-sdk-element#min) of 31 or lower. |
| Manifest | TV-ML | The app manifest sets an intent type of `https://developer.android.com/reference/android/content/Intent#ACTION_MAIN` with category `https://developer.android.com/reference/android/content/Intent#CATEGORY_LEANBACK_LAUNCHER`. For more information, see [Declare a TV activity](https://developer.android.com/training/tv/start/start#tv-activity). |
| Manifest | TV-MT | The app manifest sets the hardware feature `android.hardware.touchscreen` and others listed in the "Declare hardware requirements for TV" to not required. For more information, see [Declare hardware requirements for TV](https://developer.android.com/training/tv/start/hardware#declare-hardware-requirements). |
| Game Controllers | TV-GP | If the app uses a game controller as its primary input method, it declares the appropriate requirement with the [`<uses-feature>`](https://developer.android.com/guide/topics/manifest/uses-feature-element) manifest tag. For more information, see [Declare support for game controllers](https://developer.android.com/training/tv/games#gamepad). |
| Game Controllers | TV-GC | If the app provides visual instructions for using game controllers, the instructions are free of branding and show a compatible button layout. For more information, see [Handle controllers for games](https://developer.android.com/training/tv/start/controllers#games). |
| Advertising | TV-AP | The app offers interaction with advertising using D-pad controls. For more information, see [Enable D-pad navigation](https://developer.android.com/training/tv/start/navigation#enable_d-pad_navigation). |
| Advertising | TV-AD | For advertising that uses fullscreen, non-video ads, the app lets the user immediately dismiss the ad with D-pad or gamepad controls. |
| Advertising | TV-AU | For advertising that uses clickable, non-fullscreen, non-video ads, the app does not let ads link to a web URL. |
| Advertising | TV-AA | For advertising that uses clickable, non-fullscreen, non-video ads, the app does not let ads link to another app that is not available on TV devices. |
| Web Content | TV-WB | For web content, the app may only use `https://developer.android.com/reference/android/webkit/WebView` components. The app may not attempt to launch a web browser app. |
| Media Playback | TV-NP | If the app continues to play audio after the user returns to the home screen or switches to another app, the app provides a *Now Playing* card on the home screen recommendation row so users can return to the app to control playback. For more information, see [Display a Now Playing card](https://developer.android.com/training/tv/playback/now-playing). We recommend that you pause video when the user switches out of the app, and don't integrate video with the *Now Playing* card. |
| Media Playback | TV-PA | If the app provides a *Now Playing* card, selecting this card takes the user to a screen that lets them pause playback. |
| Media Playback | TV-PP | If the app plays video or music content, the app toggles between playing and pausing media playback when a play or pause key event is sent during playback. For more information, see [`KEYCODE_MEDIA_PLAY_PAUSE`](https://developer.android.com/reference/android/view/KeyEvent#KEYCODE_MEDIA_PLAY_PAUSE). |
| Media Playback | TV-PC | While a video or audio is playing, pressing the D-pad center button pauses the media that is playing. When playback is paused, pressing the D-pad center button resumes playback. The D-pad left and right buttons fast-forward and rewind the current track, respectively. For more information, see [Media events](https://developer.android.com/training/tv/start/controllers#media-events). |
| Media Playback | TV-PN | Items are added to the Watch Next channel based on the [Watch Next guidelines for app developers](https://developer.android.com/training/tv/discovery/guidelines-app-developers). |
| Ambient Mode | TV-BU | When there is user-initiated active video playback, the app prevents the device from going into Ambient Mode. For more information, see [Ambient Mode](https://developer.android.com/training/tv/playback/ambient-mode). |
| Ambient Mode | TV-BY | When there is no user-initiated active video playback or animation, the app does not prevent the device from going into Ambient Mode. |
| Ambient Mode | TV-BA | For audio-only playback, the app does not prevent the device from going into Ambient Mode unless the app implements an experience of non-static imagery, such as music videos or images, while music is playing. |
| Memory |
| Memory | TV-ME | For low RAM devices (where [ActivityManager.isLowRamDevice()](https://developer.android.com/reference/android/app/ActivityManager#isLowRamDevice()) returns true), the maximum memory usage ([Anon+Swap](https://developer.android.com/training/tv/playback/memory#anon-swap-memory) + [Graphics](https://developer.android.com/training/tv/playback/memory#graphics-memory) + [File Memory](https://developer.android.com/training/tv/playback/memory#file-memory)) of a foreground app must remain within the limits (including specific measurement mechanisms and caveats) defined in \[Optimize memory usage.\]\[optimize-memory-usage\] |
| Memory |

## Google Play

Follow these requirements to configure your app consistently with other
listings and classifications on Google Play:

| Type | Test | Description |
|---|---|---|
| Picture-in-picture | TV-IC | The app sets the proper metadata to categorize its usage of picture-in-picture to one of the permitted usage types. It also declares a title and subtitle that accurately represent what this PIP is being used for. For more information, see [Multitasking on TV](https://developer.android.com/training/tv/start/multitasking#usage-types). |
| Picture-in-picture | TV-IP | While in picture-in-picture, the app does not display promotional material or advertising that is not inherently part of the content source. |
| Picture-in-picture | TV-IQ | While in picture-in-picture mode, the app does not degrade the experience of another fullscreen activity. The app shouldn't use excessive resources, take over audio focus, interfere with the active MediaSession, or request a disproportionate number of decoder sessions. |
| Picture-in-picture | TV-IH | The app does not show any UI controls or navigable elements while in picture-in-picture mode. Apps may expose certain [user controls](https://developer.android.com/develop/ui/views/picture-in-picture) directly in the PiP window. |
| Picture-in-picture | TV-IE | Entering picture-in picture mode requires explicit and intentional action by the user within the app. The app does not automatically enter PiP (`https://developer.android.com/reference/android/app/PictureInPictureParams.Builder#setAutoEnterEnabled(boolean)` set to `false`) unless the user is in an ongoing call. |
| Picture-in-picture | TV-IS | The app must not show any UI to enter PiP if picture-in-picture mode is [disabled](https://developer.android.com/guide/topics/ui/picture-in-picture#best) on a device. |
| Picture-in-picture | TV-IX | The app uses picture-in-picture mode only for the continuation of an ongoing activity. The picture-in-picture experience does not incentivize or encourage users to return to the fullscreen view of the app during the ongoing or after the activity has concluded. |
| Play Policies | TV-G1 | The use of [Android App Bundles](https://developer.android.com/guide/app-bundle) is mandatory for all new and existing TV apps in the Google Play Store. |
| Play Policies | TV-G2 | Your app must follow the [Play Developer Policy Center](https://play.google.com/about/developer-content-policy/) requirements. |
| Play Policies | TV-G6 | From August 1, 2026, your app must [support 64-bit architectures](https://developer.android.com/google/play/requirements/64-bit). |
| Play Policies | TV-G7 | From August 1, 2026, your app must [support 16 KB page sizes](https://developer.android.com/guide/practices/page-sizes). |
| App details page | TV-G3 | App functionality works as expected or as described in the app's Google Play Store listing. |
| App details page | TV-G4 | App submission has uploaded at least one unaltered, high resolution screenshot that accurately depicts the current version of your TV app experience. |
| Login Credentials | TV-G5 | For apps with paid features, you must provide login credentials in the Google Play Console for testing of the full app experience. For more information, see [App Access in Prepare your app for review](https://support.google.com/googleplay/android-developer/answer/9859455). |

## Frequently asked questions

**After I submit my app, how will find out if my app does not meet all the
requirements for TV devices?**

If your app doesn't meet the usability requirements described on this page, the
Play Store team will contact you through the email address specified in the
[Google Play Console](https://play.google.com/console/) account associated with
the app.

> [!CAUTION]
> **Caution:** Make sure your app includes the [required manifest
> entries](https://developer.android.com/training/tv/start/start#tv-activity) for TV devices. Otherwise, your app won't be considered a TV app and won't be reviewed for TV usability requirements.

**My app targets form factors other than just TV devices. If my app does not
meet the TV device requirements, will my new or updated app still appear on
Google Play for other devices?**

Updates to your Google Play store listing can only be published if all changes
are approved. If an update of a form-factor-specific artifact is blocking
further updates to your listing for other devices such as phones or tablets,
you may want to remove that artifact by replacing it with an empty submission
until you can address the requirements.

**If my app meets the publishing requirements, when will it be available in
the Google Play Store on TV devices?**

Apps that meet the requirements for TV will appear on the Play Store on TV
devices immediately.

## Change notes

### January 2026

- Play Policies

  - New criterion, [TV-G6](https://developer.android.com/docs/quality-guidelines/tv-app-quality#TV-G6):

    From August 1, 2026, your app must
    [support 64-bit architectures](https://developer.android.com/google/play/requirements/64-bit).
  - New criterion, [TV-G7](https://developer.android.com/docs/quality-guidelines/tv-app-quality#TV-G7):

    From August 1, 2026, your app must
    [support 16 KB page sizes](https://developer.android.com/guide/practices/page-sizes).

### December 2025

- Expected Performance

  - New criterion, [TV-PS](https://developer.android.com/docs/quality-guidelines/tv-app-quality#TV-PS):

    In addition to the
    [core performance and stability requirements](https://developer.android.com/docs/quality-guidelines/core-app-quality#ps), your
    app must support commonly used Android TV devices by setting a
    [minimum Android SDK version](https://developer.android.com/guide/topics/manifest/uses-sdk-element#min) of 31 or lower.

### November 2024

- Functionality and Performance

  - New criterion, [TV-ME](https://developer.android.com/docs/quality-guidelines/tv-app-quality#TV-ME):

    For low RAM devices (where
    [`ActivityManager.isLowRamDevice()`](https://developer.android.com/reference/android/app/ActivityManager#isLowRamDevice()) returns true),
    the maximum memory usage ([Anon+Swap](https://developer.android.com/training/tv/playback/memory#anon-swap-memory) +
    [Graphics](https://developer.android.com/training/tv/playback/memory#graphics-memory) + [File Memory](https://developer.android.com/training/tv/playback/memory#file-memory)) of a
    foreground app must remain within the limits (including specific
    measurement mechanisms and caveats) defined in [Optimize memory
    usage.](https://developer.android.com/training/tv/playback/memory)

### May 2024

- Media Playback

  - Updated criterion, [TV-NP](https://developer.android.com/docs/quality-guidelines/tv-app-quality#TV-NP):

    The criterion was updated to apply only to **audio** playback, not
    video. We now also recommend pausing video when your app is in the
    background.