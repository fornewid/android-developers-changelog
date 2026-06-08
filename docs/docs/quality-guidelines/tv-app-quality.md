---
title: https://developer.android.com/docs/quality-guidelines/tv-app-quality
url: https://developer.android.com/docs/quality-guidelines/tv-app-quality
source: md.txt
---

Users have different expectations when watching TV than when they are using a
phone or tablet. A typical TV user sits about 10 feet away from the screen, so
small details are less noticeable and small text is hard to read. Since users
sit away from a TV, they must use a remote control device to navigate and make
selections rather than touching elements on the screen. These differences
significantly affect the requirements for what makes a good TV user experience.

The first step toward creating a great experience for TV users is to review and
follow the [Android TV design guidelines](https://developer.android.com/design/tv). To understand the
fundamental implementation requirements for a TV app, also review the [Build TV
Apps](https://developer.android.com/training/tv/start) training.

## TV app compatibility checklists

The compatibility checklists define criteria to help you assess the level of
support your app provides for Android TV OS.

Levels of support include the following:

![Icon for Tier 3 TV Ready](https://developer.android.com/static/images/docs/quality-guidelines/tier-3/tier_3_icon.svg)

### [Tier 3 - TV Ready](https://developer.android.com/docs/quality-guidelines/tv-app-quality#tier3_checklist)

Your app meets the fundamental requirements to run on Android TV OS devices.

![Icon for Tier 2 TV Optimized](https://developer.android.com/static/images/docs/quality-guidelines/tier-2/tier_2_icon.svg)

### [Tier 2 - TV Optimized](https://developer.android.com/docs/quality-guidelines/tv-app-quality#tier2_checklist)

Your app provides a more tailored and seamless experience for Android TV OS
devices.

![Icon for Tier 1 TV Differentiated](https://developer.android.com/static/images/docs/quality-guidelines/tier-1/tier_1_icon.svg)

### [Tier 1 - TV Differentiated](https://developer.android.com/docs/quality-guidelines/tv-app-quality#tier1_checklist)

Your app provides a premium experience that takes full advantage of advanced
Android TV OS capabilities.

## Tier 3 - TV Ready

| Type | Test | Description |
|---|---|---|
| Launcher | TV-LM | The app displays a launcher icon in the Android TV Launcher after installation. For more information, see [Declare a TV activity](https://developer.android.com/training/tv/start/start#tv-activity). |
| Launcher | TV-LB | The app displays both a 320x180 pixel full-size banner and at least a 160x160 pixel (at xhdpi density) app icon as its launcher icons in the Android TV Launcher. For more information, see [Android TV app icon and banner guidelines](https://developer.android.com/design/ui/tv/guides/system/tv-app-icon-guidelines). |
| Launcher | TV-BN | The app launch banner contains the name of the app. |
| Launcher | TV-LG | If the app is a game, it appears in the Games row in the Android TV Launcher. For more information, see [Show your game on the home screen](https://developer.android.com/training/tv/games#Launcher). |
| Launcher | TV-LS | The app runs successfully and without error messages, including during installation, loading, and testing. For more information, see [Run TV apps](https://developer.android.com/training/tv/start/start#run). |
| Layout | TV-LO | The app supports landscape orientation without vertical letterboxing or pillarboxing. Use only black for bars on original-format videos. For more information, see [Build basic TV layouts](https://developer.android.com/training/tv/start/layouts#structure). |
| Layout | TV-OV | The app does not display any text or functionality that is partially cut off by the edges of the screen. For more information, see [Overscan](https://developer.android.com/training/tv/start/layouts#overscan). |
| Layout | TV-TR | The app does not partially obscure other apps. The app fills the entire screen and has a non-transparent background. |
| Navigation | TV-DP | The app functionality is navigable using five-way D-pad controls---unless the app requires a game controller, as specified in the TV-GP criterion in the Controllers section of the Functionality table that follows. For more information, see [TV Navigation](https://developer.android.com/training/tv/start/navigation#d-pad-navigation). |
| Navigation | TV-DK | If the app requires a game controller, as specified in the TV-GP criterion, all functionality is navigable using standard Android game controller keys. For more information, see [Process gamepad button presses](https://developer.android.com/training/game-controllers/controller-input#button). |
| Navigation | TV-DM | The app does not depend on a remote control device having a Menu button to access user interface controls. |
| Navigation | TV-DB | Back button presses lead back to the Android TV home screen. For more information, see [Provide appropriate Back-button behavior](https://developer.android.com/training/tv/start/controllers#back-button). |
| Navigation | TV-DL | If the app has a live TV feed integrated on the Live tab, the app meets frictionless playback and direct-back requirements. For more information, see [Back Button](https://developer.android.com/training/tv/start/navigation#back_button). |
| SDK | TV-PS | In addition to the core performance and stability requirements, the app declares support for commonly used Android TV devices by setting a minimum Android SDK version of 31 or lower by setting the minSdkVersion value. |
| Manifest | TV-ML | The app manifest sets an intent type of [`ACTION_MAIN`](https://developer.android.com/reference/android/content/Intent#ACTION_MAIN) with category [`CATEGORY_LEANBACK_LAUNCHER`](https://developer.android.com/reference/android/content/Intent#CATEGORY_LEANBACK_LAUNCHER). For more information, see [Declare a TV activity](https://developer.android.com/training/tv/start/start#tv-activity). |
| Manifest | TV-MT | The app manifest sets the hardware feature android.hardware.touchscreen and others listed in the "Declare hardware requirements for TV" to not required. For more information, see [Declare hardware requirements for TV](https://developer.android.com/training/tv/start/hardware#declare-hardware-requirements). |
| Game Controllers | TV-GP | If the app uses a game controller as its primary input method, it declares the appropriate requirement with the [`<uses-feature>`](https://developer.android.com/guide/topics/manifest/uses-feature-element) manifest tag. For more information, see [Declare support for game controllers](https://developer.android.com/training/tv/games#gamepad). |
| Game Controllers | TV-GC | If the app provides visual instructions for using game controllers, the instructions are free of branding and show a compatible button layout. For more information, see [Handle controllers for games](https://developer.android.com/training/tv/start/controllers#games). |
| Advertising | TV-AP | The app offers interaction with advertising using D-pad controls. For more information, see [Enable D-pad navigation](https://developer.android.com/training/tv/start/navigation#enable_d-pad_navigation). |
| Advertising | TV-AD | For advertising that displays full screen, non-video ads, the app lets the user immediately dismiss the ad with D-pad or gamepad controls. |
| Advertising | TV-AU | For advertising that uses clickable, non-fullscreen, non-video ads, the app does not let ads link to a web URL. |
| Advertising | TV-AA | For advertising that uses clickable, non-fullscreen, non-video ads, the app does not let ads link to another app that is not available on TV devices. |
| Web Content | TV-WB | For web content, the app must only use [`WebView`](https://developer.android.com/reference/android/webkit/WebView) components. The app must not attempt to launch a web browser app. |
| Media Playback | TV-NP | If the app continues to play audio after the user returns to the home screen or switches to another app, the app provides media controls in the system UI (such as a card or notification) so users can return to the app to control playback. For more information, see [Display a Now Playing card](https://developer.android.com/training/tv/playback/now-playing). Video apps must not use these media controls, and video must be paused when the user switches out of the app. |
| Media Playback | TV-PA | If the app provides media controls on the system UI, selecting them takes the user to a screen that lets the user pause playback. |
| Media Playback | TV-PN | Items added for resumed watching adhere to the [guidelines for app developers](https://developer.android.com/training/tv/discovery/guidelines-app-developers). |
| Media Playback | TV-PC | While a video or audio is playing, pressing the D-pad center button pauses the media that is playing. When playback is paused, pressing the D-pad center button resumes playback. The D-pad left and right buttons fast-forward and rewind the current track, respectively. For more information, see [Media events](https://developer.android.com/training/tv/start/controllers#media-events). |
| Media Playback | TV-PP | If the app plays video or music content, the app toggles between playing and pausing media playback when a play or pause key event is sent during playback. For more information, see [`KEYCODE_MEDIA_PLAY_PAUSE`](https://developer.android.com/reference/android/view/KeyEvent#KEYCODE_MEDIA_PLAY_PAUSE). |
| Ambient Mode | TV-BU | When there is user-initiated active video playback, the app prevents the device from going into Ambient Mode. For more information, see [Ambient Mode](https://developer.android.com/training/tv/playback/ambient-mode). |
| Ambient Mode | TV-BY | When there is no user-initiated active video playback or animation, the app does not prevent the device from going into Ambient Mode. |
| Ambient Mode | TV-BA | For audio-only playback, the app does not prevent the device from going into Ambient Mode unless the app implements an experience of non-static imagery, such as music videos or images, while music is playing. |
| Picture-in-Picture | TV-IC | If the app uses picture-in-picture, it sets the proper metadata to categorize its usage of picture-in-picture to one of the permitted usage types. It also declares a title and subtitle that accurately represent what this PIP is being used for. For more information, see [Multitasking on TV](https://developer.android.com/training/tv/start/multitasking#usage-types). |
| Picture-in-Picture | TV-IP | While in picture-in-picture, the app does not display promotional material or advertising that is not inherently part of the content source. |
| Picture-in-Picture | TV-IQ | While in picture-in-picture mode, the app does not degrade the experience of another fullscreen activity. The app shouldn't use excessive resources, take over audio focus, interfere with the active MediaSession, or request a disproportionate number of decoder sessions. |
| Picture-in-Picture | TV-IH | While in picture-in-picture mode, the app does not show any UI controls or navigable elements. Apps may expose certain user controls directly in the PiP window. |
| Picture-in-Picture | TV-IE | Entering picture-in picture mode requires explicit and intentional action by the user within the app. The app does not automatically enter PiP ([`setAutoEnterEnabled`](https://developer.android.com/reference/android/app/PictureInPictureParams.Builder#setAutoEnterEnabled(boolean)) set to `false`) unless the user is in an ongoing call. |
| Picture-in-Picture | TV-IS | The app must not show any UI to enter PiP if picture-in-picture mode is disabled on a device. |
| Picture-in-Picture | TV-IX | The app uses picture-in-picture mode only for the continuation of an ongoing activity. The picture-in-picture experience does not incentivize or encourage users to return to the fullscreen view of the app during the ongoing or after the activity has concluded. |
| Memory | TV-ME | For low RAM devices (where [`ActivityManager.isLowRamDevice()`](https://developer.android.com/reference/android/app/ActivityManager#isLowRamDevice()) returns `true`), the maximum memory usage (Anon+Swap + Graphics + File Memory) of a foreground app must remain within the limits (including specific measurement mechanisms and caveats) defined in [Optimize memory usage.](https://developer.android.com/training/tv/playback/memory) |
| Google Play | TV-G1 | The use of Android App Bundles is mandatory for all new and existing TV apps in the Google Play Store. |
| Google Play | TV-G2 | The app must follow the Play Developer Policy Center requirements. |
| Google Play | TV-G6 | From August 1, 2026, TV apps must support 64-bit architectures and comply with [16 KB page size](https://developer.android.com/guide/practices/page-sizes) requirements. |
| App Details Page | TV-G3 | App functionality works as expected or as described in the app's Google Play Store listing. |
| App Details Page | TV-G4 | App submission has uploaded at least one unaltered, high resolution screenshot that accurately depicts the current version of the TV app experience. |
| Login Credentials | TV-G5 | For apps requiring users to sign in, you must provide login credentials in the Google Play Console for testing of the full app experience. For more information, see [App Access in Prepare your app for review](https://support.google.com/googleplay/android-developer/answer/9859455). |

## Tier 2 - TV Optimized

| Type | Test | Description |
|---|---|---|
| Performance | TV-BP | The app includes [Baseline Profiles](https://developer.android.com/topic/performance/baselineprofiles/overview) to improve overall performance, such as app startup and reducing jank. |
| UI | TV-4K | The app is compatible with 4K by providing high-resolution assets within the app, including the app icon, banner, content cards, and other assets in the app. |
| Connectivity | TV-CT | If the app has a mobile counterpart that supports Cast, the TV app integrates with [TV Cast Receiver (Cast Connect)](https://developer.android.com/guide/topics/media/cast/connect/tv-receiver) to allow users to cast content from their phone or tablet to the TV. |
| Login | TV-LI | Login interface: Users are able to login using mobile or Google Account for seamless login. |
| Login | TV-LC | The app securely stores user credentials or automatically logs in returning users through token-based authentication or secure storage methods. This significantly reduces friction for subsequent uses after the initial setup. |
| Voice | TV-VS | The app integrates voice search capabilities for natural language content discovery. Integration helps users input search queries without needing to use a software keyboard, especially if the app uses a custom keyboard that does not support voice input. For example, the app can enable Gboard for voice input or provide a microphone button next to the search text field to trigger voice recognition. |
| Voice | TV-VC | The app integrates voice commands for playback and navigation by [implementing `MediaSession`](https://developer.android.com/media/media3/session/control-playback). |
| Game Controllers | TV-GF | The game fully supports both physical game controllers and virtual gamepads. |

## Tier 1 - TV Differentiated

| Type | Test | Description |
|---|---|---|
| Engage | TV-EC | The app submits content entity types for users to resume watching, such as picking up an interrupted movie or watching the next episode of a series, through the Engage SDK. |
| Engage | TV-ER | The app submits relevant content entity types to enable recommendations to be surfaced through the Engage SDK. |
| Device Capabilities | TV-PI | The app selects a TV's preset picture profile for relevant content (cinema profile for movies, low latency / high contrast for live sports or games) |
| Device Capabilities | TV-AO | The app reacts seamlessly to audio output switching by selecting the best audio channel for supported output devices (e.g. a stereo channel for headphones or 5.1 for surround speakers) |
| Device Capabilities | TV-FR | The app supports requesting the framerate of the content, such that the display may switch to the correct playback mode and avoid jitter (e.g. 50 Hz for 50 fps content) |
| Device Capabilities | TV-TO | The app supports touch and click to enable compatibility with pointer remotes and touchscreen displays. UI components display a hover state when the cursor is above a component that can be interacted with, components can be clicked and scrollable containers can be scrolled vertically and horizontally. |
| Device Capabilities | TV-SA | The app supports spatial audio for an immersive listening experience. For example, the app may use the [IAMF](https://aomediacodec.github.io/iamf/) codec. |
| Accessibility | TV-AX | The app implements enhanced accessibility options, such as audio descriptions, subtitle display (including preferred subtitle styles and high-contrast mode), general high-contrast UI mode, simplified navigation modes and adjustable playback speed. Demonstrates a deep commitment to inclusivity, ensuring a premium experience that's accessible and enjoyable for all. |
| AI | TV-AI | The app implements experiences featuring AppFunctions or in-app AI. |

> [!NOTE]
> **Note:** We recommend inviting users to leave [ratings and reviews](https://developer.android.com/guide/playcore/in-app-review) from within the app if your app is differentiating TV app (tier 1). Similarly, you can drive installs from mobile by integrating with [cross-device install prompts](https://developer.android.com/guide/playcore/install-prompt).

## Frequently asked questions

**After I submit my app, how will find out if my app does not meet all the
requirements for TV devices?**

If your app doesn't meet the usability requirements described on this page, the
Play Store team will contact you through the email address specified in the
[Google Play Console](https://play.google.com/console/) account associated with the app.

> [!CAUTION]
> **Caution:** Make sure your app includes the [required manifest entries](https://developer.android.com/training/tv/start/start#tv-activity) for TV devices. Otherwise, your app won't be considered a TV app and won't be reviewed for TV usability requirements.

> [!NOTE]
> **Note:** For information about how to publish your app on Google Play, see [Distribute to Android TV](https://developer.android.com/training/tv/publishing/checklist#distribute-to-android-tv).

**My app targets form factors other than just TV devices. If my app does not
meet the TV device requirements, will my new or updated app still appear on
Google Play for other devices?**

Updates to your Google Play store listing can only be published if all changes
are approved. If an update of a form-factor-specific artifact is blocking
further updates to your listing for other devices such as phones or tablets, you
may want to remove that artifact by replacing it with an empty submission until
you can address the requirements.

**If my app meets the publishing requirements, when will it be available in the
Google Play Store on TV devices?**

Apps that meet the requirements for TV will appear on the Play Store on TV
devices immediately.

## Change notes

### May 2026

- TV App Quality Tiers
  - Added TV Optimized (tier 2) and TV Differentiated (tier 1) quality criteria to clarify premium TV experiences beyond the minimum submission requirements (tier 3).
- Search

  - Removed criterion `TV-SB`:

    In-app search is no longer required as we recommend integrating with
    Engage SDK ([`TV-EC`](https://developer.android.com/docs/quality-guidelines/tv-app-quality#TV-EC), [`TV-ER`](https://developer.android.com/docs/quality-guidelines/tv-app-quality#TV-ER)).
- Play Policies

  - Removed criterion `TV-G7` and updated criterion [TV-G6](https://developer.android.com/docs/quality-guidelines/tv-app-quality#TV-G6):

    Included
    [16 KB page sizes](https://developer.android.com/guide/practices/page-sizes) as part of 64-bit requirements.

### January 2026

- Play Policies

  - New criterion, [`TV-G6`](https://developer.android.com/docs/quality-guidelines/tv-app-quality#TV-G6):

    From August 1, 2026, your app must
    [support 64-bit architectures](https://developer.android.com/google/play/requirements/64-bit).
  - New criterion, `TV-G7`:

    From August 1, 2026, your app must
    [support 16 KB page sizes](https://developer.android.com/guide/practices/page-sizes).

### December 2025

- Expected Performance

  - New criterion, [`TV-PS`](https://developer.android.com/docs/quality-guidelines/tv-app-quality#TV-PS):

    In addition to the
    [core performance and stability requirements](https://developer.android.com/docs/quality-guidelines/core-app-quality#ps), your
    app must support commonly used Android TV devices by setting a [minimum
    Android SDK version](https://developer.android.com/guide/topics/manifest/uses-sdk-element#min) of 31 or lower.

### November 2024

- Functionality and Performance

  - New criterion, [`TV-ME`](https://developer.android.com/docs/quality-guidelines/tv-app-quality#TV-ME):

    For low RAM devices (where
    [`ActivityManager.isLowRamDevice()`](https://developer.android.com/reference/android/app/ActivityManager#isLowRamDevice()) returns `true`),
    the maximum memory usage ([Anon+Swap](https://developer.android.com/training/tv/playback/memory#anon-swap-memory) +
    [Graphics](https://developer.android.com/training/tv/playback/memory#graphics-memory) + [File Memory](https://developer.android.com/training/tv/playback/memory#file-memory)) of a
    foreground app must remain within the limits (including specific
    measurement mechanisms and caveats) defined in [Optimize memory
    usage.](https://developer.android.com/training/tv/playback/memory)

### May 2024

- Media Playback

  - Updated criterion, [`TV-NP`](https://developer.android.com/docs/quality-guidelines/tv-app-quality#TV-NP):

    The criterion was updated to apply only to **audio** playback, not
    video. We now also recommend pausing video when your app is in the
    background.