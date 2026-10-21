---
title: https://developer.android.com/docs/quality-guidelines/android-xr/immersive
url: https://developer.android.com/docs/quality-guidelines/android-xr/immersive
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

The app quality guidelines for immersive experiences extend the foundational
[core app quality](https://developer.android.com/docs/quality-guidelines/core-app-quality) mobile standards.

These app quality guidelines and policies focus on spatial interactions and
capabilities that are unique to the Android XR platform on XR headsets and wired
XR glasses, as outlined in the [compatibility tier definitions](https://developer.android.com/docs/quality-guidelines/android-xr/immersive#compatibility-tier), the
[checklists](https://developer.android.com/docs/quality-guidelines/android-xr/immersive#android-xr-compatibility-checklist), and the [Android XR App Policies](https://developer.android.com/docs/quality-guidelines/android-xr/immersive#app-policies). Review these sections to
verify that your app provides a great user experience on XR headsets and wired
XR glasses.

## Immersive experiences: compatibility tier definitions

Review the following compatibility tier definitions to understand the level of
support that your app provides for immersive experiences on XR headsets and
wired XR glasses.

### Android XR compatible mobile app

An Android XR compatible mobile app represents an existing [mobile](https://developer.android.com/design/ui/mobile) app that
has not been modified to adapt to a large screen or any other form factor. This
type of app is automatically compatible with Android XR as long as it doesn't
[require any features](https://developer.android.com/guide/topics/manifest/uses-feature-element) that are unsupported, such as [telephony](https://developer.android.com/guide/topics/manifest/uses-feature-element#telephony-hw-features). Users
can complete critical task flows but with a less optimal user experience than an
[Android XR differentiated app](https://developer.android.com/docs/quality-guidelines/android-xr/immersive#android-xr-differentiated).

This type of app runs full screen on a panel in the user's environment, but its
layout might not be ideal at larger sizes. Apps that specify compact sizes in
the manifest show up accordingly. The app doesn't run in compatibility mode and
is therefore not letterboxed. The app has a functional experience of the core
input modalities provided by Android XR (eye tracking + gesture or raycast
hands) and basic support for external input devices, including keyboard, mouse,
trackpad, and game controllers. It may or may not be capable of resizing.

Android XR compatible mobile apps are automatically opted in and available on
the Google Play Store. An app that is not compatible because of unsupported
[feature requirements](https://developer.android.com/guide/topics/manifest/uses-feature-element) is not installable through the Play Store.

### Android XR compatible adaptive app

An Android XR compatible adaptive app represents an app that has implemented
layout optimizations for all screen sizes and device configurations (for
example, large screens in addition to mobile), along with enhanced support for
external input devices and multitasking. An app fulfills these requirements if
it is either [Tier 2 adaptive optimized](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#tier2) or [Tier 1 adaptive
differentiated](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#tier1) for desktop, tablets, or foldables.

Android XR compatible adaptive apps are automatically opted in and available on
the Play Store.

### Android XR differentiated app

An Android XR differentiated app has a user experience explicitly designed for
XR and it implements features that are only offered on XR. You can take full
advantage of Android XR capabilities and differentiate your app's experiences by
adding XR features (such as spatial panels), adding XR content (such as 3D
video) to your apps by developing with the Android Jetpack XR SDK, Unity, Godot,
Unreal Engine, or OpenXR.

You can use the Jetpack XR SDK to provide XR-specific capabilities such as:

- Spatial panels
- Environments
- 3D models
- Spatial audio
- 3D or spatial video and photos
- Anchors
- Other spatial UI such as orbiters

To be considered an Android XR differentiated app, an app must implement at
least one XR-specific feature or piece of XR-specific content. For certain use
cases, more features and content requirements may exist. See details in the
subsequent sections.

All apps built with Unity, Godot, Unreal Engine, or OpenXR are considered
differentiated so long as they meet the quality metrics and minimum requirements
to be considered an Android XR-differentiated app. For example, an app with low
frame rate, crashes, or other negative user experiences would not qualify.

#### Help users discover your app in the Play Store with a badge

Android XR differentiated apps automatically get a "Made for XR" badge in
the Play Store to help users discover high-quality XR experiences.

## Immersive experiences: compatibility checklist

To verify that your app provides a great user experience on XR headsets and
wired XR glasses, review the following compatibility checklists and tests.

These checklists and tests define a comprehensive set of quality requirements
for most types of Android apps.

### Android XR compatible mobile app

Your app must fulfill the [core app quality](https://developer.android.com/docs/quality-guidelines/core-app-quality) requirements.

> [!NOTE]
> **Note:** [UI and Graphics](https://developer.android.com/docs/quality-guidelines/core-app-quality#ui_and_graphics) requirements covering folding and unfolding behaviors are not applicable to XR apps.

Your app should also adhere to all applicable [accessibility guidelines](https://developer.android.com/guide/topics/ui/accessibility) for
other form factors such as phones and tablets (for example, [color
contrast](https://support.google.com/accessibility/android/answer/7158390)).

### Android XR compatible adaptive app

Any app that is either [Tier 2 adaptive optimized](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#tier2) or [Tier 1 adaptive
differentiated](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#tier1) for desktop, tablets, or foldables is also considered an
Android XR compatible adaptive app. The [adaptive app quality guidelines](https://developer.android.com/docs/quality-guidelines/large-screen-app-quality)
offer a structured approach to ensuring a great experience on Android XR, but
device state considerations such as rotation or folding/unfolding are not
required.

### Android XR-differentiated app

Because Android XR-differentiated apps are highly differentiated, some of the
listed capabilities are applicable only to specific types of apps. Choose the
capabilities that are appropriate for your app. Android apps must also comply
with [adaptive app quality guidelines](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality). See the requirements that are
appropriate for your app.

You should also follow the [guidance on designing XR-differentiated apps](https://developer.android.com/design/ui/xr/guides/get-started)
for the best possible user experience.

| **Type of app \& use case** | **Category** | **Area** | **Guidance** |
|---|---|---|---|
| **General Baseline Requirement** (Android \& OpenXR) | **Privacy \& Security** | Account sign-in (first time UX) | If your app utilizes a login system, clearly present the user's login credentials (for example, their username credentials) after successful authentication. This fosters trust by confirming the active account. Furthermore, incorporate a readily accessible menu or settings page that allows users to view and manage their account information at any time. |
| **General Baseline Requirement** (Android \& OpenXR) | **Safety and Comfort** | Strobing | To ensure the safety and well-being of all users, it's crucial to minimize the risk of strobing effects within your app. Avoid intentionally incorporating any design elements that may induce strobing. 1. If a strobing effect is absolutely necessary, ensure the flashing rate is very low (below 3 flashes per second) and the flashing area is small and subtle. 2. Consider providing an ability to disable it through settings or preferences. 3. Display a clear warning message before any strobing occurs. |
| **General Baseline Requirement** (Android \& OpenXR) | **Safety and Comfort** | Avoiding motion sickness | Follow these guidelines to avoid causing motion sickness in users: - Prioritize visual comfort by avoiding abrupt camera movements. Maintain a consistent frame of reference to avoid disorienting the user. - Don't rotate the camera over time. If the direction of the camera changes, the camera snaps to the new orientation. |
| **General Baseline Requirement** (Android \& OpenXR) | **Safety and Comfort** | Dimmer | Respect the user's established dimmer settings to prevent safety hazards. You may adjust the dimmer for an optimal experience for your app, but users can manually override at any time. |
| **General Baseline Requirement** (Android \& OpenXR) | **Input** | Interaction targets size | Interactable targets have a minimum size and a recommended size based on intended interaction distance: - Minimum size: DistanceInM x 0.868 x 48 = M - Recommended size: DistanceInM x 0.868 x 56 = M or larger <br /> When using the Jetpack XR SDK, we recommend a minimum size of 48 x 48dp, with a recommended 56 x 56dp or larger tap target size. |
| **General Baseline Requirement** (Android \& OpenXR) | **XR Technical Functionality** | Hand input | Your app supports natural hand input as a baseline interaction method for Android XR, including hand raycast requirements and gestural support for input primitives. Your app is playable or otherwise usable without the need for controllers, but can be augmented with the use of them if you choose to do so. |
| **General Baseline Requirement** (Android \& OpenXR) | **XR Technical Functionality** | Boundary | If your app is primarily focused on the real-world (`currentPassthroughOpacity` is set to a value greater than 0.5), users may actively walk around their real-world environment. Keep the central field of view clear of dense, opaque elements to prevent tripping hazards or situational unawareness. If your app is primarily focused in a virtual world (`currentPassthroughOpacity` is set to a value less than 0.5) and it's not a stationary experience, you should consider declaring a large boundary in the manifest using `PROPERTY_XR_BOUNDARY_TYPE_RECOMMENDED = XR_BOUNDARY_TYPE_LARGE`. If your app uses `XR_BOUNDARY_TYPE_LARGE`, it is fully playable without the boundary showing (within a 2.0 m radius; note, boundary passthrough begins to fade in at 1.5m radius). XR Glasses: There is no boundary on XR glasses devices. |
| **General Baseline Requirement** (Android \& OpenXR) | **Performance** | Rendering | Your app renders each frame between \<11.1ms (90Hz), and \< 13.8ms (72 Hz). |
| **General Baseline Requirement** (Android \& OpenXR) | **Performance** | Resolution | OpenXR \& Engines: Query `XR_ANDROID_recommended_resolution` to get the ideal rendering target---just as standard game engines do. |
| **General Baseline Requirement** (Android \& OpenXR) | **Performance** | App startup time | Users want to be able to interact with your app or game as quickly as possible. The definition of a good start-up or loading time varies by category, but as a general principle we recommend minimizing the time between launch and first interaction. See target durations below: - Mean cold start: Less than 2 seconds - Mean warm start: Less than 1 second For more details, see [App startup time](https://developer.android.com/topic/performance/issues/launch-time). |
| **General Baseline Requirement** (Android \& OpenXR) | **Performance** | ANRs | Your app does not crash or block the UI thread causing ANR ("Android Not Responding") errors. Your app has \<1 ANR in 99.5% of daily sessions. Your app uses Google Play's pre-launch [report](https://google.play/business/pre-launchreports/) to identify potential stability issues. After deployment, pay attention to the Android Vitals page in the Google Play console. |
| **General Baseline Requirement** (Android \& OpenXR) | **Performance** | Crash rate | Do not consume excessive system resources impacting the rest of the system and other apps, keeping a \~1% [crash rate](https://developer.android.com/topic/performance/issues/crash). |
| **Android App Baseline** (XR-differentiated) | **Visual \& User Experience** | Basic XR | Your app implements at least one XR-specific feature or piece of XR-specific content to enhance the user experience. This can include an orbiter, one or more spatial panels, environments, or 3D objects. |
| **Android App Baseline** (XR-differentiated) | **Visual \& User Experience** | Spatial panels | - Place menus, assets, and controls in a dedicated panel or orbiter. Do not include these components in the main editing panel. - When multitasking (that is, completing two or more tasks at once) with panels, create separate spatial panels. For example, you would create separate spatial panels for chat windows and lists. |
| **Android App Baseline** (XR-differentiated) | **Visual \& User Experience** | Environments | When showing a virtual environment, brightness can be distracting and fatiguing. Your app presents a safe tonal range with no spikes in brightness that conflict with UI or might cause user fatigue. UI is legible in all directions especially within the middle horizontal band of the user's gaze. (Detailed guidelines to be linked in the future) |
| **Android App Baseline** (XR-differentiated) | **Visual \& User Experience** | UI theme | Default to or highly encourage using a dark theme; light theme apps will appear very bright, fail to integrate into the user's environment, and drain the battery faster. For XR glasses, always implement a dark theme as the system uses a dark theme by default. |
| **Android App Baseline** (XR-differentiated) | **Visual \& User Experience** | Transitioning between Home Space (HSM) and Full Space (FSM) | When taking users to Full Space, your app has an entry point for users to quickly transition between Home Space and Full Space. Use an icon or label, and place the button in an easy-to-access location. |
| **Android App Baseline** (XR-differentiated) | **Visual \& User Experience** | Menu \& list scrolling | Your app updates scroll interactions (especially through carousels or vertical lists) to have physics or momentum. For example, scrolling incorporates momentum, causing content in carousels and lists to continue moving briefly after a user interaction before gradually coming to a stop (instead of stopping exactly when the user stops input). |
| **Video \& Media Functionality** | **Visual \& User Experience** | Spatial player (Android only) | Your app allows users to watch content in Full Space. Remove playback controls from an overlay on top of content and instead place it in a dedicated panel or orbiter. For panels with video playback, set the aspect ratio to remove letterboxing. |
| **Video \& Media Functionality** | **Visual \& User Experience** | Spatial audio | Consider supporting spatial audio including panel-locked audio or surround sound. |
| **Video \& Media Functionality** | **Visual \& User Experience** | Simultaneous video viewing | If your app supports multiple simultaneous video streams, the user interface makes the following information clear: - Which video streams are providing audio output - Which playback controls impact which video streams |
| **Video \& Media Functionality** | **Visual \& User Experience** | Environment | When playing video content in Full Space, your app allows users to dim passthrough (or select virtual environments on supported devices). |

## Android XR App Policies

All apps must comply with the requirements in the following policies to promote
safe and respectful user experiences on immersive devices like XR headsets and
wired XR glasses.

### App safety

As a reminder, all apps distributed through Google Play must comply with all
[Google Play Developer Policies](https://play.google/developer-content-policy/#!?modal_active=none).

The following activities are strictly prohibited, and apps must not facilitate
or promote these activities:

- Doxxing
- Facial recognition or biometric identification
- Surveillance
- Creation or dissemination of Non-Consensual Intimate Imagery (NCII)

The following bystander protections are required for all apps:

#### Camera safety

Apps that access the camera must respect bystander privacy and must comply with
the following:

| Prohibited interactions | Description |
|---|---|
| Real-time facial identification \& doxxing | Apps must not use camera sensors to run facial identification to surface bystander Personally Identifiable Information (PII). For example: names, home addresses, phone numbers, or their employer. |
| Non-consensual intimate imagery (NCII) or illegal content generation | Apps must not use camera sensors to facilitate the creation of non-consensual intimate imagery (NCII) or any illegal content generation (for example, CSAM). |

#### Audio safety

Apps utilizing the microphone array should respect bystander privacy and must
comply with the following:

| Prohibited interactions | Description |
|---|---|
| Persistent eavesdropping | Apps must not maintain persistent, background audio recording or transcription when the wearer is not actively engaged with the app on a user-initiated task. |
| Speech identification | Apps must not use the microphone array to identify non-wearer voices or bystanders. |

### LED behaviors

Apps must not do the following with respect to the device's user- and
world-facing LEDs:

| Prohibited interactions | Description |
|---|---|
| Programmatic suppression or modification | Apps must not change, dim, or disable the system-enforced world-facing LED and user-facing LED behavior based on microphone and camera access. Apps must also not encourage or direct users to change, dim, or disable the LEDs' behavior. |
| Bypassing thwart and tamper detection | Apps must not bypass or interfere with, or encourage or direct users to do so, the device's thwart detection algorithms, which are designed to programmatically stop recording if the world-facing LED is physically covered or damaged. |

*** ** * ** ***

OpenXR™ and the OpenXR logo are trademarks owned
by The Khronos Group Inc. and are registered as a trademark in China,
the European Union, Japan and the United Kingdom.