---
title: https://developer.android.com/docs/quality-guidelines/android-xr
url: https://developer.android.com/docs/quality-guidelines/android-xr
source: md.txt
---

## Compatibility tier definitions

To verify that your app provides a great user experience on XR headsets and
wired XR glasses, review the following compatibility checklists and tests.

> [!WARNING]
> **Preview:** Stay tuned in the future for updates to the app quality guidelines for [augmented experiences](https://developer.android.com/develop/xr/explore/augmented) for devices like AI glasses.

The checklists and tests define a comprehensive set of quality requirements for
most types of Android apps.

### Android XR compatible mobile app

An Android XR compatible mobile app represents an existing [mobile](https://developer.android.com/design/ui/mobile) app that
has not been modified to adapt to a large screen or any other form factor. This
type of app is automatically compatible with Android XR as long as it doesn't
[require any features](https://developer.android.com/guide/topics/manifest/uses-feature-element) that are unsupported, such as [telephony](https://developer.android.com/guide/topics/manifest/uses-feature-element#telephony-hw-features). Users
can complete critical task flows but with a less optimal user experience than an
[Android XR differentiated app](https://developer.android.com/docs/quality-guidelines/android-xr#android-xr-differentiated).

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

### Android XR compatible large screen app

An Android XR compatible large screen app represents a large screen [Tier 1](https://developer.android.com/docs/quality-guidelines/large-screen-app-quality#large_screen_differentiated)
or [Tier 2](https://developer.android.com/docs/quality-guidelines/large-screen-app-quality#large_screen_optimized) app that has implemented layout optimizations for all screen
sizes and device configurations (for example, large screens in addition to
mobile), along with enhanced support for external input devices and
multitasking. Android XR compatible large screen apps are automatically opted in
and available on the Play Store.

An Android XR compatible large screen app runs full screen on a spatial panel in
the user's environment at 1024dp × 720dp. Users will be able to interact with
the app naturally using their eyes and hands, but will otherwise be very similar
to the large screen app.

### Android XR differentiated app

An Android XR differentiated app has a user experience explicitly designed for
XR and it implements features that are only offered on XR. You can take full
advantage of Android XR capabilities and differentiate your app's experiences by
adding XR features (e.g. spatial panels), adding XR content (e.g. 3D video) to
your applications by developing with Android Jetpack XR SDK, Unity, or OpenXR.

You can use the Jetpack XR SDK to provide XR-specific capabilities
including spatial panels, environments, 3D models, spatial audio, 3D / spatial
video / photos, anchors, and other spatial UI such as orbiters.

To be considered an Android XR differentiated app, an app must implement at
least one XR-specific feature or piece of XR-specific content. For certain use
cases, more features and content requirements may exist. See details below.

All apps built with Unity or OpenXR are considered differentiated. Apps built
with Unity or OpenXR must meet quality metrics and minimum requirements to be
considered an Android XR-differentiated app. For example, an app with low frame
rate, crashes, or other negative user experiences would not qualify.

## Android XR compatibility checklist

These compatibility checklists define criteria to help you assess the level of
support your app provides for XR. Levels of support include the following:

### Android XR compatible mobile app

Your app must fulfill the [core app quality](https://developer.android.com/docs/quality-guidelines/core-app-quality) requirements.

> [!NOTE]
> **Note:** [UI and Graphics](https://developer.android.com/docs/quality-guidelines/core-app-quality#ui_and_graphics) requirements covering folding and unfolding behaviors are not applicable to XR apps.

Your app should also adhere to all applicable [accessibility guidelines](https://developer.android.com/guide/topics/ui/accessibility) for
other form factors such as phones and tablets (for example, [color
contrast](https://support.google.com/accessibility/android/answer/7158390)%7B:.external%7D)).

### Android XR compatible large screen app

Any large screen [Tier 1](https://developer.android.com/docs/quality-guidelines/large-screen-app-quality#large_screen_differentiated) or [Tier 2](https://developer.android.com/docs/quality-guidelines/large-screen-app-quality#large_screen_optimized) app is considered an Android XR
compatible large screen app. The [large screen app quality guidelines](https://developer.android.com/docs/quality-guidelines/large-screen-app-quality) offer
a structured approach to ensuring a great experience on Android XR, but device
state considerations such as rotation or folding/unfolding are not required.
Similarly, Android XR does not include stylus support.

### Android XR-differentiated app

Because Android XR-differentiated apps are highly differentiated, some of the
listed capabilities are applicable only to specific types of apps. Choose the
capabilities that are appropriate for your application. Android apps must also
comply with [Large screen and mobile Android guidelines](https://developer.android.com/docs/quality-guidelines/large-screen-app-quality). See the
requirements that are appropriate for your application (some of these might turn
into potential policy updates as well).

| **Type of App / Use Case** | **Category** | **Area** | **Guidance** |
|---|---|---|---|
| **General Baseline Requirement** (Android \& OpenXR) | **Privacy \& security** | Account sign-in (first time UX) | If your app utilizes a login system, clearly present the user's login credentials (for example, their username credentials) after successful authentication. This fosters trust by confirming the active account. Furthermore, incorporate a readily accessible menu or settings page that allows users to view and manage their account information at any time. |
| **General Baseline Requirement** (Android \& OpenXR) | **Safety and Comfort** | Strobing | To ensure the safety and well-being of all users, it's crucial to minimize the risk of strobing effects within your application. Avoid intentionally incorporating any design elements that may induce strobing. 1. If strobing effect is absolutely necessary, ensure the flashing rate is very low (below 3 flashes per second) and the flashing area is small and subtle. 2. Consider providing an ability to disable it through settings or preferences. 3. Display a clear warning message before any strobing occurs. |
| **General Baseline Requirement** (Android \& OpenXR) | **Safety and Comfort** | Avoiding motion sickness | Follow these guidelines to avoid causing motion sickness in users: - Prioritize visual comfort by avoiding abrupt camera movements. Maintain a consistent frame of reference to avoid disorienting the user. - Don't rotate the camera over time. If the direction of the camera changes, the camera snaps to the new orientation. |
| **General Baseline Requirement** (Android \& OpenXR) | **Input** | Interaction targets size | Interactable targets have a minimum size and a recommended size based on intended interaction distance: - Minimum size: DistanceInM x 0.868 x 48 = M - Recommended size: DistanceInM x 0.868 x 56 = M or larger <br /> When using the Jetpack XR SDK, we recommend a minimum size of 48 x 48dp, with a recommended 56 x 56dp or larger tap target size. |
| **General Baseline Requirement** (Android \& OpenXR) | **XR Technical Functionality** | Hand input | Your app supports natural hand input as a baseline interaction method for Android XR, including hand raycast requirements and gestural support for input primitives. Your app is playable or otherwise usable without the need for controllers, but can be augmented with the use of them if you choose to do so. |
| **General Baseline Requirement** (Android \& OpenXR) | **XR Technical Functionality** | Boundary (formerly Guardian) | If your app expects users to move from their starting point (at app launch) around their physical space, it either requests passthrough or declares `PROPERTY_XR_BOUNDARY_TYPE_RECOMMENDED = XR_BOUNDARY_TYPE_LARGE` in the manifest. If your app uses `XR_BOUNDARY_TYPE_LARGE`, it is fully playable without the boundary showing (within a 2.0 m radius; note, boundary passthrough begins to fade in at 1.5m radius). |
| **General Baseline Requirement** (Android \& OpenXR) | **Performance** | Rendering | Your app renders each frame between \<11.1ms (90Hz), and \< 13.8ms (72 Hz). |
| **General Baseline Requirement** (Android \& OpenXR) | **Performance** | Resolution | Your app has a resolution of at least 1856 x 2160 per eye. |
| **General Baseline Requirement** (Android \& OpenXR) | **Performance** | App startup time | Users want to be able to interact with your app or game as quickly as possible. The definition of a good start-up or loading time varies by category, but as a general principle we recommend minimizing the time between launch and first interaction. See target durations below: - Mean cold start: Below 2 seconds - Mean warm start: Below 1 second For more details, see [App startup time](https://developer.android.com/topic/performance/vitals/launch-time). |
| **General Baseline Requirement** (Android \& OpenXR) | **Performance** | ANRs | Your app does not crash or block the UI thread causing ANR ("Android Not Responding") errors. Your app has \<1 ANR in 99.5% of daily sessions. Your app uses Google Play's pre-launch [report](https://play.google.com/console/about/pre-launchreports/) to identify potential stability issues. After deployment, pay attention to the Android Vitals page in the Google Play developer console. |
| **General Baseline Requirement** (Android \& OpenXR) | **Performance** | Crash Rate | Do not consume excessive system resources impacting the rest of the system and other apps, keeping a \~1% [crash rate](https://developer.android.com/topic/performance/vitals/crash). |
| **Android App Baseline** (XR-differentiated) | **Visual \& User experience** | Basic XR | Your app implements at least one XR-specific feature or piece of XR-specific content to enhance the user experience. This can include an orbiter, one or more spatial panels, environments, or 3D objects. |
| **Android App Baseline** (XR-differentiated) | **Visual \& User experience** | Spatial Panels | When multitasking (that is, completing two or more tasks at once) with panels, create separate spatial panels. For example, you would create separate spatial panels for chat windows and lists. |
| **Android App Baseline** (XR-differentiated) | **Visual \& User experience** | Environments | When showing a virtual environment, brightness can be distracting and fatiguing. Your app presents a safe tonal range with no spikes in brightness that conflict with UI or might cause user fatigue. UI is legible in all directions especially within the middle horizontal band of the user's gaze. (Detailed guidelines to be linked in the future) |
| **Android App Baseline** (XR-differentiated) | **Visual \& User experience** | Transitioning between Home Space (HSM) and Full Space (FSM) | When taking users to Full Space, your app has an entry point for users to quickly transition between Home Space and Full Space. Use an icon or label, and place the button in an easy-to-access location. |
| **Android App Baseline** (XR-differentiated) | **Visual \& User experience** | Spatial Panels | Place menus, assets, and controls in a dedicated panel or orbiter. Do not include these components in the main editing panel. |
| **Android App Baseline** (XR-differentiated) | **Visual \& User experience** | Menu / List Scrolling | Your app updates scroll interactions (especially through carousels or vertical lists) to have physics or momentum. For example, scrolling incorporates momentum, causing content in carousels and lists to continue moving briefly after a user interaction before gradually coming to a stop (instead of stopping exactly when the user stops input). |
| **Video / Media Functionality** | **Visual \& User experience** | Spatial Player (Android only) | Your app allows users to watch content in Full Space. Remove playback controls from an overlay on top of content and instead place it in a dedicated panel or orbiter. For panels with video playback, set the aspect ratio to remove letter boxing. |
| **Video / Media Functionality** | **Visual \& User experience** | Spatial Audio | Consider supporting spatial audio including panel-locked audio or surround sound. |
| **Video / Media Functionality** | **Visual \& User experience** | Simultaneous Video Viewing | If your app supports multiple simultaneous video streams, the user interface makes the following information clear: - Which video streams are providing audio output - Which playback controls impact which video streams |
| **Video / Media Functionality** | **Visual \& User experience** | Environment | When playing back content in Full Space, your app allows users to either dim passthrough or select virtual environments. |

*** ** * ** ***

OpenXR™ and the OpenXR logo are trademarks owned
by The Khronos Group Inc. and are registered as a trademark in China,
the European Union, Japan and the United Kingdom.