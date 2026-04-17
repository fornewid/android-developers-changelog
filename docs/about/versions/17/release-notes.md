---
title: https://developer.android.com/about/versions/17/release-notes
url: https://developer.android.com/about/versions/17/release-notes
source: md.txt
---

### Beta 4

|---|---|
| **Release date** | April 16, 2026 |
| **Builds** | CP21.260330.008 |
| **Emulator support** | x86 (64-bit), ARM (v8-A) |
| **Security patch level** | 2026-04-05 |
| **Google Play services** | 26.11.36 |

### Beta 3

|---|---|
| **Release date** | March 26, 2026 |
| **Builds** | CP21.260306.017 |
| **Emulator support** | x86 (64-bit), ARM (v8-A) |
| **Security patch level** | 2026-03-05 |
| **Google Play services** | 26.02.35 |

### Beta 2

|---|---|
| **Release date** | February 26, 2026 |
| **Builds** | CP21.260206.011 CP21.260206.011.A1 (Pixel 6 Pro, Pixel 6, Pixel 6a, Pixel 7 Pro, Pixel 7) |
| **Emulator support** | x86 (64-bit), ARM (v8-A) |
| **Security patch level** | 2026-02-05 |
| **Google Play services** | 25.49.33 |

### Beta 1

|---|---|
| **Release date** | February 13, 2026 |
| **Builds** | CP21.260116.011.B1 CP21.260116.011.A1 (Pixel 6 Pro, Pixel 6, Pixel 6a, Pixel 7 Pro, Pixel 7) |
| **Emulator support** | x86 (64-bit), ARM (v8-A) |
| **Security patch level** | 2026-01-05 |
| **Google Play services** | 25.47.33 |

### Android 17 Beta 4 (April 2026)

[Android 17 is on its last scheduled beta with Beta 4](https://android-developers.googleblog.com/2026/04/the-fourth-beta-of-android-17.html),
so perform your final compatibility testing and start publishing
your Android 17-targeted apps to the Google Play Store.

If you develop an Android SDK, library, tool, or game engine,
it's critical to prepare any necessary updates now to prevent
your downstream app and game developers from being blocked by
compatibility issues and allow them to target the latest SDK
features. Make sure to let your downstream developers know if
updates are needed to fully support Android 17.

#### App Memory Limits

Android 17 beta 4 introduces conservative, app memory limits to
improve system stability. If your app is killed by these limits,
[ApplicationExitInfo.getDescription](https://developer.android.com/reference/android/app/ApplicationExitInfo#getDescription()) will contain "MemoryLimiter". You can also use [trigger-based profiling](https://developer.android.com/topic/performance/tracing/profiling-manager/trigger-based-capture) to capture heap dumps when limits are hit using [TRIGGER_TYPE_ANOMALY](https://developer.android.com/reference/android/os/ProfilingTrigger#TRIGGER_TYPE_ANOMALY).

#### Background audio hardening changes

Starting in Android 17, the audio framework enforces restrictions on background audio interactions including audio playback, audio focus requests, and volume change APIs. Based on your feedback, we've made some changes since beta 2,including targetSDK gating while-in-use FGS enforcement and exempting alarm audio. Full details available in the
[updated guidance](https://developer.android.com/versions/17/changes/bg-audio).

### Top Issues fixed in Beta 4

- *An issue where webpage URLs were automatically included when sharing screenshots from the capture preview, causing unwanted links to be shared with image files. ([**Issue #444631269**](https://issuetracker.google.com/issues/444631269))*
- *An accessibility issue caused the device to become completely unresponsive and unusable. ([**Issue #484755628**](https://issuetracker.google.com/issues/484755628))*
- *An issue where the media control widget could disappear or fail to navigate between multiple active media sessions. ([**Issue #457008153**](https://issuetracker.google.com/issues/457008153), [**Issue #466760800**](https://issuetracker.google.com/issues/466760800), [**Issue #497131275**](https://issuetracker.google.com/issues/497131275), [**Issue #499041878**](https://issuetracker.google.com/issues/499041878))*
- *An issue where dream services failed to correctly process key events, trigger keyguard bouncer prompts, or execute service lifecycle callbacks. ([**Issue #485661973**](https://issuetracker.google.com/issues/485661973))*
- *An issue that prevented users from successfully downloading and applying cinematic or local weather wallpaper effects. ([**Issue #475924636**](https://issuetracker.google.com/issues/475924636))*
- *An issue where the device would freeze and spontaneously restart while typing in messaging applications. ([**Issue #478417840**](https://issuetracker.google.com/issues/478417840))*
- *A critical system instability issue that causes the device to hang and crash during normal usage. ([**Issue #427436873**](https://issuetracker.google.com/issues/427436873), [**Issue #428838049**](https://issuetracker.google.com/issues/428838049))*
- *An issue causing devices to experience significantly reduced charging speeds when approaching the 80% battery limit, resulting in long delays before the device reaches its target charge and enters bypass mode. ([**Issue #485148344**](https://issuetracker.google.com/issues/485148344), [**Issue #490178498**](https://issuetracker.google.com/issues/490178498))*
- *A rendering issue that caused multicolored horizontal lines to randomly obscure the device display. ([**Issue #478953060**](https://issuetracker.google.com/issues/478953060), [**Issue #478177624**](https://issuetracker.google.com/issues/478177624), [**Issue #483765859**](https://issuetracker.google.com/issues/483765859), [**Issue #487263076**](https://issuetracker.google.com/issues/487263076))*
- *Pulling down the notification drawer while a feedback report is in progress can cause a System UI crash and device freeze. ([**Issue #488920581**](https://issuetracker.google.com/issues/488920581))*
- *Critical system components including Pixel Launcher and navigation may crash or become unresponsive for several minutes after a device reboot. ([**Issue #317282987**](https://issuetracker.google.com/issues/317282987), [**Issue #316689583**](https://issuetracker.google.com/issues/316689583), [**Issue #316188779**](https://issuetracker.google.com/issues/316188779))*
- *An accessibility issue that prevents users from properly interacting with apps after minimizing and returning to a split-screen view. ([**Issue #490735259**](https://issuetracker.google.com/issues/490735259))*
- *An issue that prevented Bluetooth from being re-enabled after it was turned off via the system settings or quick settings panel. ([**Issue #498320401**](https://issuetracker.google.com/issues/498320401))*
- *Notifications marked with setSilent(true) may unexpectedly play alert sounds on Android 16 when multiple notifications are present in the shade. ([**Issue #467164528**](https://issuetracker.google.com/issues/467164528))*
- *Wi-Fi analyzer applications fail to detect any available Wi-Fi signals, preventing network scanning and signal monitoring. ([**Issue #488493098**](https://issuetracker.google.com/issues/488493098), [**Issue #488244938**](https://issuetracker.google.com/issues/488244938), [**Issue #491531212**](https://issuetracker.google.com/issues/491531212), [**Issue #490566133**](https://issuetracker.google.com/issues/490566133), [**Issue #488742605**](https://issuetracker.google.com/issues/488742605), [**Issue #488437847**](https://issuetracker.google.com/issues/488437847), [**Issue #489664292**](https://issuetracker.google.com/issues/489664292), [**Issue #492229996**](https://issuetracker.google.com/issues/492229996), [**Issue #492403933**](https://issuetracker.google.com/issues/492403933), [**Issue #492078596**](https://issuetracker.google.com/issues/492078596), [**Issue #493259320**](https://issuetracker.google.com/issues/493259320), [**Issue #490313462**](https://issuetracker.google.com/issues/490313462), [**Issue #494716049**](https://issuetracker.google.com/issues/494716049), [**Issue #495146669**](https://issuetracker.google.com/issues/495146669), [**Issue #490268954**](https://issuetracker.google.com/issues/490268954), [**Issue #496870370**](https://issuetracker.google.com/issues/496870370), [**Issue #497174811**](https://issuetracker.google.com/issues/497174811), [**Issue #496927303**](https://issuetracker.google.com/issues/496927303), [**Issue #497726865**](https://issuetracker.google.com/issues/497726865), [**Issue #498299558**](https://issuetracker.google.com/issues/498299558), [**Issue #496860223**](https://issuetracker.google.com/issues/496860223), [**Issue #498454519**](https://issuetracker.google.com/issues/498454519), [**Issue #499751486**](https://issuetracker.google.com/issues/499751486), [**Issue #491171326**](https://issuetracker.google.com/issues/491171326))*

### Android 17 Beta 3 (March 2026)

[Android 17 has officially reached Platform Stability with Beta 3](https://android-developers.googleblog.com/2026/03/the-third-beta-of-android-17.html). The API
surface is now locked, meaning it is time to perform final compatibility
testing and publish your Android 17-targeted apps to the Google Play Store.

If you develop an SDK, library, tool, or game engine, it is critical to release
your updates now so downstream developers are not blocked from targeting the
latest SDK features.

Following is a summary of new capabilities, behavior changes,
and enhancements introduced in Android 17 beta 3:

#### Media and Camera Enhancements

- **Photo Picker Customization:** You can now modify the grid view aspect ratio of the photo picker. Using the `https://developer.android.com/reference/android/widget/photopicker/PhotoPickerUiCustomizationParams` API, you can switch from the default 1:1 square to a 9:16 portrait display, allowing for better UI integration.
- **RAW14 Image Format:** Professional camera apps can now capture 14-bit per pixel RAW images using the new `https://developer.android.com/reference/android/graphics/ImageFormat#RAW14` constant, allowing for maximum detail and color depth from compatible sensors.
- **Vendor-Defined Camera Extensions:** Hardware partners can now define custom camera extension modes (e.g., 'Super Resolution' or AI enhancements). Query these via the `https://developer.android.com/reference/android/hardware/camera2/CameraExtensionCharacteristics#isExtensionSupported(int)` API.
- **Camera Device Type APIs:** Identify whether a camera is built-in hardware, an external USB webcam, or a virtual camera.
- **Bluetooth LE Audio Hearing Aids:** A new device category (`https://developer.android.com/reference/android/media/AudioDeviceInfo#TYPE_BLE_HEARING_AID`) allows apps to distinguish hearing aids from generic LE Audio headsets, enabling tailored UI iconography.
- **Granular Hearing Aid Audio Routing:** Users can independently route system sounds (notifications, ringtones, alarms) to either connected hearing aids or the device speaker. This is handled at the system level and requires no API changes.
- **Extended HE-AAC Software Encoder:** A new system-provided encoder (`c2.android.xheaac.encoder`) supports high and low bitrates for significantly better audio in low-bandwidth conditions, including mandatory support for loudness metadata to ensure consistent volume.

#### Performance and Battery

- **Reduced Wakelocks for Idle Alarms:** A new callback-based variant of `https://developer.android.com/reference/android/app/AlarmManager#setExactAndAllowWhileIdle(int,%20long,%20java.lang.String,%20java.util.concurrent.Executor,%20android.app.AlarmManager.OnAlarmListener)` accepts an `https://developer.android.com/reference/android/app/AlarmManager.OnAlarmListener` instead of a `https://developer.android.com/reference/android/app/PendingIntent`. This reduces power consumption and long partial wakelocks for apps (like medical monitors or messaging sockets) that need precise callbacks during Doze or Battery Saver modes.

#### Privacy and Security

- **System-Provided Location Button:** You can embed a secure, system-rendered location button via Jetpack. Tapping it grants your app precise location access for the current session only, without triggering a system dialog. Requires the `https://developer.android.com/reference/android/Manifest.permission#USE_LOCATION_BUTTON` permission.
- **Discrete Password Visibility:** "Show passwords" settings are now split between touch inputs (briefly echoes the last character) and physical keyboards (hidden immediately by default). Standard framework components respect this automatically; custom fields should migrate to the `https://developer.android.com/reference/android/text/ShowSecretsSetting` API.
- **Post-Quantum Cryptography (PQC) Hybrid Signing:** Android introduces the v3.2 APK Signature Scheme, combining classical signatures (RSA/Elliptic Curve) with ML-DSA signatures. This prepares apps for NIST standards and quantum computing advancements.

#### User Experience and System UI

- **Widget Support on External Displays:** Improved visual consistency for widgets across different pixel densities. `https://developer.android.com/reference/android/widget/RemoteViews#setViewPadding(int,%20float,%20float,%20float,%20float,%20int)` now accepts complex units (DP/SP), and widgets can retrieve specific `https://developer.android.com/reference/android/util/DisplayMetrics` via `https://developer.android.com/reference/android/appwidget/AppWidgetManager#OPTION_APPWIDGET_DISPLAY_ID`.
- **Desktop Interactive Picture-in-Picture (iPiP):** Apps can request to be moved to a "pinned" windowing layer during desktop mode (default on external displays). These pinned windows remain interactive and always-on-top. Requires `https://developer.android.com/about/versions/17/android.Manifest.permission.USE_PINNED_WINDOWING_LAYER` and PiP permissions.
- **Hidden Home Screen App Labels:** Users can now hide app labels on the home screen. Ensure your app icon is highly recognizable!
- **Redesigned Screen Recording:** A new floating toolbar improves recording controls and capture settings for creators. The UI is automatically excluded from the final video.
- **Bubbles:** The windowing mode feature introduced in Beta 2 is now fully enabled.

#### Core Functionality \& Health

- **VPN App Exclusion Settings:** VPN apps can use the `https://developer.android.com/reference/android/provider/Settings#ACTION_VPN_APP_EXCLUSION_SETTINGS` intent to launch a system-managed screen where users can select specific apps to bypass the VPN tunnel (split-tunneling).
- **Dynamic System Font Fallback:** Android now supports runtime updates to the font fallback chain, delivering updated emojis and typography without a full OS update.
- **OpenJDK 21 \& 25 Updates:** Integration of modern OpenJDK features, including updated Unicode support and enhanced SSL support for named groups in TLS.
- **Health Connect Device Data Providers (DDPs):** Health Connect can now distinguish between data generated by apps and data originating directly from system-verified hardware (like Wear OS watches or the phone itself).

### Top Issues fixed in Beta 3

- *A system-level regression in Android 16 process lifecycle management that caused frequent, random app restarts and screen flickering, which previously led to lost user progress and interrupted app states across multiple third-party applications. (**[Issue #440017096](https://issuetracker.google.com/issues/440017096)**)*
- *An issue where Expanded Dark Mode failed to apply to apps in Work and Private profiles. (**[Issue #476409380](https://issuetracker.google.com/issues/476409380)**)*
- *A camera failure that prevented users from switching to the 5x telephoto lens. (**[Issue #485610295](https://issuetracker.google.com/issues/485610295)** , **[Issue #488274607](https://issuetracker.google.com/issues/488274607)**)*
- *Stuttering and erratic behavior during ultra-wide to wide lens transitions. (**[Issue #452650681](https://issuetracker.google.com/issues/452650681)**)*
- *A system hang that caused the lock screen to become unresponsive after disconnecting from Android Auto or locking the device. (**[Issue #457527675](https://issuetracker.google.com/issues/457527675)**)*
- *A system instability issue causing device freezes and reboots when using Android Auto. (**[Issue #455555269](https://issuetracker.google.com/issues/455555269)** , **[Issue #457973643](https://issuetracker.google.com/issues/457973643)**)*
- *A system instability issue causing frequent spontaneous reboots and device hangs. (**[Issue #485892529](https://issuetracker.google.com/issues/485892529)** , **[Issue #488619007](https://issuetracker.google.com/issues/488619007)** , **[Issue #488482317](https://issuetracker.google.com/issues/488482317)** , **[Issue #485627106](https://issuetracker.google.com/issues/485627106)** , **[Issue #489454751](https://issuetracker.google.com/issues/489454751)** , **[Issue #487638484](https://issuetracker.google.com/issues/487638484)** , **[Issue #487604772](https://issuetracker.google.com/issues/487604772)** , **[Issue #485385078](https://issuetracker.google.com/issues/485385078)**)*
- *A regression that caused unexpected device reboots. (**[Issue #420999948](https://issuetracker.google.com/issues/420999948)** , **[Issue #426316038](https://issuetracker.google.com/issues/426316038)**)*
- *A crash during rapid audio focus changes. (**[Issue #477151825](https://issuetracker.google.com/issues/477151825)**)*
- *A Bluetooth pairing hang of up to 150 seconds. (**[Issue #466163481](https://issuetracker.google.com/issues/466163481)**)*
- *A system-level instability causing spontaneous reboots during idle periods. (**[Issue #297421786](https://issuetracker.google.com/issues/297421786)** , **[Issue #300558078](https://issuetracker.google.com/issues/300558078)** , **[Issue #301726714](https://issuetracker.google.com/issues/301726714)** , **[Issue #310348072](https://issuetracker.google.com/issues/310348072)** , **[Issue #321233271](https://issuetracker.google.com/issues/321233271)** , **[Issue #320461892](https://issuetracker.google.com/issues/320461892)** , **[Issue #348326714](https://issuetracker.google.com/issues/348326714)** , **[Issue #348297618](https://issuetracker.google.com/issues/348297618)** , **[Issue #348290709](https://issuetracker.google.com/issues/348290709)** , **[Issue #348242411](https://issuetracker.google.com/issues/348242411)** , **[Issue #348217723](https://issuetracker.google.com/issues/348217723)** , **[Issue #348541549](https://issuetracker.google.com/issues/348541549)** , **[Issue #348770195](https://issuetracker.google.com/issues/348770195)** , **[Issue #348786196](https://issuetracker.google.com/issues/348786196)** , **[Issue #348766331](https://issuetracker.google.com/issues/348766331)** , **[Issue #349273927](https://issuetracker.google.com/issues/349273927)** , **[Issue #349977622](https://issuetracker.google.com/issues/349977622)** , **[Issue #350685466](https://issuetracker.google.com/issues/350685466)** , **[Issue #351357895](https://issuetracker.google.com/issues/351357895)** , **[Issue #352743431](https://issuetracker.google.com/issues/352743431)** , **[Issue #354467134](https://issuetracker.google.com/issues/354467134)** , **[Issue #355126951](https://issuetracker.google.com/issues/355126951)** , **[Issue #355602077](https://issuetracker.google.com/issues/355602077)** , **[Issue #355239966](https://issuetracker.google.com/issues/355239966)** , **[Issue #357282489](https://issuetracker.google.com/issues/357282489)** , **[Issue #358040619](https://issuetracker.google.com/issues/358040619)** , **[Issue #358344787](https://issuetracker.google.com/issues/358344787)** , **[Issue #360475166](https://issuetracker.google.com/issues/360475166)** , **[Issue #360461108](https://issuetracker.google.com/issues/360461108)** , **[Issue #360120511](https://issuetracker.google.com/issues/360120511)** , **[Issue #360968601](https://issuetracker.google.com/issues/360968601)** , **[Issue #361916913](https://issuetracker.google.com/issues/361916913)** , **[Issue #362650982](https://issuetracker.google.com/issues/362650982)** , **[Issue #363213047](https://issuetracker.google.com/issues/363213047)** , **[Issue #363464720](https://issuetracker.google.com/issues/363464720)** , **[Issue #363205584](https://issuetracker.google.com/issues/363205584)** , **[Issue #361007622](https://issuetracker.google.com/issues/361007622)** , **[Issue #364849917](https://issuetracker.google.com/issues/364849917)** , **[Issue #365338167](https://issuetracker.google.com/issues/365338167)** , **[Issue #370154739](https://issuetracker.google.com/issues/370154739)** , **[Issue #370041210](https://issuetracker.google.com/issues/370041210)**)*
- *An issue where incoming calls failed to trigger device vibration. (**[Issue #473464803](https://issuetracker.google.com/issues/473464803)** , **[Issue #470955250](https://issuetracker.google.com/issues/470955250)**)*
- *A conflict where Battery Saver remained active indefinitely when an 80% charging limit was enabled. (**[Issue #366996806](https://issuetracker.google.com/issues/366996806)**)*
- *A display rendering issue that caused visual artifacts when interacting with Google Message notifications from the lock screen. (**[Issue #486491783](https://issuetracker.google.com/issues/486491783)** , **[Issue #486806705](https://issuetracker.google.com/issues/486806705)** , **[Issue #485168942](https://issuetracker.google.com/issues/485168942)**)*
- *An issue where notifications occasionally failed to dismiss or reappeared. (**[Issue #454647834](https://issuetracker.google.com/issues/454647834)**)*
- *A rendering issue causing visual artifacts during back-navigation transitions. (**[Issue #485316132](https://issuetracker.google.com/issues/485316132)**)*
- *An issue where system status bar icons would randomly disappear, preventing users from seeing battery or network levels. (**[Issue #473447873](https://issuetracker.google.com/issues/473447873)** , **[Issue #484689844](https://issuetracker.google.com/issues/484689844)** , **[Issue #484382982](https://issuetracker.google.com/issues/484382982)** , **[Issue #472268834](https://issuetracker.google.com/issues/472268834)** , **[Issue #489158801](https://issuetracker.google.com/issues/489158801)** , **[Issue #484569035](https://issuetracker.google.com/issues/484569035)**)*

### Android 17 Beta 2 (February 2026)

[Beta 2 is now available](https://android-developers.googleblog.com/2026/02/the-second-beta-of-android-17.html).
Similar to beta 1, this release is suitable for development, testing, and
general use. However, Android 17 is still in active development, so the Android
system and apps running on it **might not always work as expected**.

### What's new in Beta 2

#### **User Experience \& System UI**

- **Bubbles:** Users can now bubble any app by long-pressing launcher icons. On large screens, a new **bubble bar** in the taskbar manages organized and anchored bubbles. Apps should follow [multi-window guidelines](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-multi-window-mode).
- **EyeDropper API:** A new system API allows apps to capture pixel colors from anywhere on the display without requiring screen capture permissions.
- **Contacts Picker:** The [`ACTION_PICK_CONTACTS`](https://developer.android.com/reference/kotlin/android/provider/ContactsPickerSessionContract#ACTION_PICK_CONTACTS:kotlin.String) intent provides a system-level picker. It grants temporary, session-based access to specific fields, reducing the need for full [`READ_CONTACTS`](https://developer.android.com/reference/android/Manifest.permission#READ_CONTACTS) permissions.
- **Touchpad Pointer Capture:** By default, captured touchpads now behave like mice, reporting relative movement and gestures instead of raw finger coordinates. Legacy absolute mode remains available via `POINTER_CAPTURE_MODE_ABSOLUTE`.
- **Interactive Chooser:** Apps can use [`getInitialRestingBounds`](https://developer.android.com/reference/kotlin/android/service/chooser/ChooserSession#getinitialrestingbounds) on a [`ChooserSession`](https://developer.android.com/reference/android/service/chooser/ChooserSession) to identify the final UI position of the Chooser for better layout adjustments.

#### **Connectivity \& Cross-Device**

- **Cross-device Handoff:** The new [Handoff API](https://developer.android.com/reference/kotlin/android/app/Activity#sethandoffenabled) enables state resumption across devices (e.g., phone to tablet) via [`CompanionDeviceManager`](https://developer.android.com/reference/android/companion/CompanionDeviceManager).
- **Advanced Ranging:**
  - **UWB DL-TDOA:** Supports FiRA 4.0 for privacy-preserving indoor navigation.
  - **Proximity Detection:** Implements WiFi Alliance specs for improved WiFi-based ranging.
- **Data Plan Enhancements:** Apps can query carrier-allocated downlink/uplink max rates for streaming using [`getStreamingAppMaxDownlinkKbps`](https://developer.android.com/reference/kotlin/android/telephony/SubscriptionInfo#getstreamingappmaxdownlinkkbps) and [`getStreamingAppMaxUplinkKbps`](https://developer.android.com/reference/kotlin/android/telephony/SubscriptionInfo#getstreamingappmaxuplinkkbps).

#### **Core Functionality, Privacy \& Performance**

- **Local Network Access:** Android 17 introduces the [`ACCESS_LOCAL_NETWORK`](https://developer.android.com/reference/kotlin/android/Manifest.permission#access_local_network) permission (part of the [`NEARBY_DEVICES`](https://developer.android.com/reference/android/Manifest.permission_group#NEARBY_DEVICES) group) to protect LAN communication.
- **Time Zone Broadcast:** A new intent, [`ACTION_TIMEZONE_OFFSET_CHANGED`](https://developer.android.com/reference/kotlin/android/content/Intent#action_timezone_offset_changed), triggers specifically on offset changes like DST transitions.
- **NPU Management:** Apps targeting Android 17 must declare the [FEATURE_NEURAL_PROCESSING_UNIT](https://developer.android.com/reference/kotlin/android/content/pm/PackageManager#feature_neural_processing_unit) hardware feature to directly access the NPU.
- **ICU 78:** Updated internationalization libraries support [Unicode 17](https://blog.unicode.org/2025/10/icu-78-released.html).
- **SMS OTP Protection:** To prevent hijacking, Android 17 delays programmatic access to OTP messages by three hours for most apps. Developers should transition to [SMS Retriever](https://developer.android.com/identity/sms-retriever) or [SMS User Consent](https://developer.android.com/identity/sms-retriever/user-consent/overview) APIs.

### Top Issues fixed in Beta 2

- *A platform stability regression in Android 16 that caused active apps to unexpectedly restart or refresh, preventing lost user progress and intermittent UI flickering during app usage. ([**Issue #440017096**](https://issuetracker.google.com/issues/440017096))*
- *A UI layout regression in the Recent Apps screen for users with German-language settings. ([**Issue #476830557**](https://issuetracker.google.com/issues/476830557), [**Issue #486511401**](https://issuetracker.google.com/issues/486511401))*
- *Improved video streaming reliability by enabling developers to confirm temporal layering support via getOutputFormat after encoder configuration to address missing frame dependency metadata. ([**Issue #306222291**](https://issuetracker.google.com/issues/306222291))*
- *A bug where the Clock screensaver omitted the leading zero in 24-hour format during low-light mode. ([**Issue #444255729**](https://issuetracker.google.com/issues/444255729))*
- *An issue where closing a folder blocked immediate subsequent interactions like opening another folder or switching screens. ([**Issue #470541347**](https://issuetracker.google.com/issues/470541347), [**Issue #471533397**](https://issuetracker.google.com/issues/471533397), [**Issue #477848604**](https://issuetracker.google.com/issues/477848604))*
- *A system crash and spontaneous reboot issue that interrupted device usage. ([**Issue #413562426**](https://issuetracker.google.com/issues/413562426))*
- *A critical system instability causing device freezes and reboots during app transitions or service calls. ([**Issue #419070024**](https://issuetracker.google.com/issues/419070024), [**Issue #428572458**](https://issuetracker.google.com/issues/428572458), [**Issue #430393241**](https://issuetracker.google.com/issues/430393241), [**Issue #424912278**](https://issuetracker.google.com/issues/424912278), [**Issue #431440391**](https://issuetracker.google.com/issues/431440391), [**Issue #426346396**](https://issuetracker.google.com/issues/426346396))*
- *A System UI deadlock that caused lock screen unresponsiveness and display hangs after disconnecting from Android Auto. ([**Issue #457527675**](https://issuetracker.google.com/issues/457527675))*
- *A UI typo in the system location permission disclosure dialog where the Back button was incorrectly displayed as 'Bac'. ([**Issue #460242870**](https://issuetracker.google.com/issues/460242870), [**Issue #477245738**](https://issuetracker.google.com/issues/477245738))*
- *An issue where Live Translate and Rules were incorrectly categorized in the System menu. ([**Issue #476754995**](https://issuetracker.google.com/issues/476754995))*
- *A critical System UI crash and subsequent device instability triggered by repeated navigation into Display and Touch settings. ([**Issue #474486679**](https://issuetracker.google.com/issues/474486679))*
- *A persistent crash that prevented users from opening Wallpaper \& style settings from the home screen. ([**Issue #478520173**](https://issuetracker.google.com/issues/478520173))*
- *A UI layout issue in the Wireless Debugging QR scanner where the back arrow overlapped the QR icon. ([**Issue #474769647**](https://issuetracker.google.com/issues/474769647))*
- *An issue in the Sound settings where ringtone previews failed to play upon selection. ([**Issue #355086959**](https://issuetracker.google.com/issues/355086959), [**Issue #375840924**](https://issuetracker.google.com/issues/375840924), [**Issue #381007949**](https://issuetracker.google.com/issues/381007949), [**Issue #381077928**](https://issuetracker.google.com/issues/381077928), [**Issue #419301121**](https://issuetracker.google.com/issues/419301121), [**Issue #452646483**](https://issuetracker.google.com/issues/452646483), [**Issue #468837747**](https://issuetracker.google.com/issues/468837747))*
- *A bug that caused redundant notifications to appear following a system update by improving the notification service logic to correctly clear stale alerts during the post-update initialization process. ([**Issue #454647834**](https://issuetracker.google.com/issues/454647834))*
- *A GPU shader compiler optimization bug on Pixel 6 Pro that caused specific GLSL mathematical expressions to evaluate incorrectly as constants, resulting in visual rendering artifacts in apps. ([**Issue #473226715**](https://issuetracker.google.com/issues/473226715))*

### Android 17 Beta 1 (February 2026)

[Beta 1 is now available](https://android-developers.googleblog.com/2026/02/the-first-beta-of-android-17.html),
with the latest features and changes to try with your apps. This release is suitable for development,
testing, and general use. However, Android 17 is still in active development, so
the Android system and apps running on it **might not always work as expected**.

As with previous versions, Android 17 includes system changes. In some cases,
these changes can affect apps until they are updated to support Android 17, so
you might see impacts ranging from minor issues to more significant limitations.
In general, most apps will work as expected, as will most APIs and features.

### What's new in Beta 1

Android 17 continues our work for more adaptable Android apps, introduces significant
enhancements to camera and media capabilities, new tools for optimizing connectivity,
and expanded profiles for companion devices. Highlights include:

#### User Interface \& Windowing

##### Mandatory Large Screen Adaptivity

Apps targeting **Android 17 (API level 37)** running on large screens ([sw ≥ 600dp](https://developer.android.com/guide/topics/large-screens/support-different-screen-sizes)) can no longer opt-out of resizing or orientation changes.

- **Ignored Attributes** : [`screenOrientation`](https://developer.android.com/guide/topics/manifest/activity-element#screen), [`resizeableActivity`](https://developer.android.com/guide/topics/manifest/activity-element#resizeableActivity), [`minAspectRatio`](https://developer.android.com/guide/topics/manifest/activity-element#minaspectratio), and [`maxAspectRatio`](https://developer.android.com/guide/topics/manifest/activity-element#maxaspectratio) are ignored on large screens.
- **Exemptions** : Devices smaller than 600dp and apps categorized as Games (`android:appCategory`).

##### Optimized Configuration Changes

To prevent state loss, the system **no longer restarts Activities** by default
for specific configuration changes, including:

- [`CONFIG_KEYBOARD`](https://developer.android.com/reference/android/content/pm/ActivityInfo#CONFIG_KEYBOARD) / [`CONFIG_KEYBOARD_HIDDEN`](https://developer.android.com/reference/android/content/pm/ActivityInfo#CONFIG_KEYBOARD)
- [`CONFIG_NAVIGATION`](https://developer.android.com/reference/android/content/pm/ActivityInfo#CONFIG_NAVIGATION)
- [`CONFIG_TOUCHSCREEN`](https://developer.android.com/reference/android/content/pm/ActivityInfo#CONFIG_TOUCHSCREEN)
- [`CONFIG_COLOR_MODE`](https://developer.android.com/reference/android/content/pm/ActivityInfo#CONFIG_COLOR_MODE)
- [`CONFIG_UI_MODE`](https://developer.android.com/reference/android/content/pm/ActivityInfo#CONFIG_UI_MODE) (only when the UI mode changes to [`UI_MODE_TYPE_DESK`](https://developer.android.com/reference/android/content/res/Configuration#UI_MODE_TYPE_DESK) or from [`UI_MODE_TYPE_DESK`](https://developer.android.com/reference/android/content/res/Configuration#UI_MODE_TYPE_DESK) to another type)

**Action Required**: If your app relies on restarts to reload resources for
these events, you must explicitly opt-in using the new
android:recreateOnConfigChanges manifest attribute.

#### Performance \& Runtime

- **Lock-free MessageQueue** : A new lock-free implementation of [`android.os.MessageQueue`](https://developer.android.com/reference/android/os/MessageQueue) reduces missed frames.
- **Generational Garbage Collection**: ART's Concurrent Mark-Compact collector now supports generational GC, prioritizing frequent, low-cost "young generation" collections.
- **New Profiling Triggers** : [`ProfilingManager`](https://developer.android.com/reference/android/os/ProfilingManager) adds triggers for [`COLD_START`](https://developer.android.com/reference/android/os/ProfilingTrigger#TRIGGER_TYPE_COLD_START), [`OOM`](https://developer.android.com/reference/android/os/ProfilingTrigger#TRIGGER_TYPE_OOM), and [`KILL_EXCESSIVE_CPU_USAGE`](https://developer.android.com/reference/android/os/ProfilingTrigger#TRIGGER_TYPE_KILL_EXCESSIVE_CPU_USAGE).
- **Notification Restrictions**: Strict size limits enforced on custom notification views to reduce memory usage.

#### Media \& Camera

##### Camera

- **Dynamic Session Updates** : Use [`CameraCaptureSession.updateOutputConfigurations()`](https://developer.android.com/reference/android/hardware/camera2/CameraCaptureSession#updateOutputConfigurations(java.util.List%3Candroid.hardware.camera2.params.OutputConfiguration%3E)) to switch use cases (e.g., Photo to Video) without closing the session or causing glitches.

##### Audio \& Video

- **Constant Quality for Video Recording** : [setVideoEncodingQuality()](https://developer.android.com/reference/android/media/MediaRecorder#setVideoQuality(int)) in [MediaRecorder](https://developer.android.com/reference/android/media/MediaRecorder) allows you to configure a constant quality (CQ) mode for video encoders.
- **Background Audio Hardening**: Audio playback, focus requests, and volume changes initiate silently (fail) if the app is not in a valid lifecycle state.
- **VVC Support** : Added platform support for [Versatile Video Coding (H.266)](https://developer.android.com/guide/topics/media/media-formats#video-formats).

#### Privacy \& Security

- **Cleartext Deprecation** : [`android:usesCleartextTraffic`](https://developer.android.com/guide/topics/manifest/application-element#usesCleartextTraffic) will be deprecated in a future release, gated on the future SDK level. Apps relying on this attribute will default to blocking cleartext; migrate to [**Network Security Configuration**](https://developer.android.com/training/articles/security-config).
- **HPKE Hybrid Cryptography** : Introduced a public [Service Provider Interface](https://developer.android.com/reference/android/crypto/hpke/HpkeSpi) for an implementation of HPKE hybrid cryptography.

#### Connectivity \& Tools

- [**Companion Device Manager**](https://developer.android.com/guide/topics/connectivity/companion-device-pairing):
  - **New Profiles** : [Medical Devices](https://developer.android.com/reference/android/companion/AssociationRequest#DEVICE_PROFILE_MEDICAL) and [Fitness Trackers](https://developer.android.com/reference/android/companion/AssociationRequest#DEVICE_PROFILE_FITNESS_TRACKER).
  - **Unified Permission Dialog** : [`setExtraPermissions`](https://developer.android.com/reference/android/companion/AssociationRequest.Builder#setExtraPermissions(java.util.Set%3Cjava.lang.String%3E)) bundles nearby permissions into the association dialog.