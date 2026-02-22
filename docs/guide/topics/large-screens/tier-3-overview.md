---
title: https://developer.android.com/guide/topics/large-screens/tier-3-overview
url: https://developer.android.com/guide/topics/large-screens/tier-3-overview
source: md.txt
---

![Tier 3 adaptive ready icon](https://developer.android.com/static/images/guide/topics/large-screens/quality-guidelines/tier-3/tier_3_icon.png)

TIER 3 --- The basic, entry-level tier of the [Adaptive app quality](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality)
guidelines.

![Depiction of three tiers with the bottom tier, tier 3, highlighted.](https://developer.android.com/static/images/guide/topics/large-screens/quality-guidelines/tier-3/tier_3_header.png)

THE FIRST STEP in creating a great app for large screens is making your app
adaptive ready.

Adaptive ready apps run full screen in landscape and portrait orientations, full
window in multi‑window mode. Apps provide basic support for external input
devices, including keyboard, mouse, trackpad, and stylus. Adaptive ready camera
apps present a camera preview that's always in the proper aspect ratio and
orientation.

App layout might not be ideal, but the app is never letterboxed, never runs in
compatibility mode, and users can complete all task flows.

## Do's and don'ts

![](https://developer.android.com/static/images/guide/topics/large-screens/quality-guidelines/tier-3/tier_3_do.png)  
check_circle

### Do

- Enable app to fill entire available display area
- Maintain state during configuration changes
- Support multi-window mode and multi-resume
- Support external keyboard, mouse, trackpad, and stylus  
![](https://developer.android.com/static/images/guide/topics/large-screens/quality-guidelines/tier-3/tier_3_dont.png)  
cancel

### Don't

- Lock app orientation when full screen or in multi‑window mode
- Set a specific app aspect ratio
- Restrict app resizability
- Restrict camera preview dimensions or orientation

## Guidelines

Follow the Tier 3 guidelines to get your app ready for large screens.
**Note:** Adaptive ready apps also fulfill the [core app quality](https://developer.android.com/docs/quality-guidelines/core-app-quality) requirements---especially the [User experience](https://developer.android.com/docs/quality-guidelines/core-app-quality#user_experience) requirements.  
![](https://developer.android.com/static/images/guide/topics/large-screens/quality-guidelines/tier-3/configuration_continuity_icon.svg)  

### [Configuration and continuity](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#t3_configuration_continuity)

Make your app adaptive ready by retaining and restoring state and resuming ongoing processes, such as media playback, during device configuration changes.

Guidelines --- [Config:Changes](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Config:Changes)  

#### What

App fills the available display area---either the entire screen or the app window in multi‑window mode---in both portrait and landscape orientations and is not [letterboxed](https://developer.android.com/guide/topics/large-screens/large-screen-compatibility-mode#letterboxing). App handles configuration changes and retains or restores its state as the device changes orientation, the app window resizes, or the device folds or unfolds.  

#### Why

Configuration changes such as device rotation, window size changes in multi-window mode, and folding or unfolding a foldable device can cause users to lose context or (even worse) data.  

#### How

Learn how to handle configuration changes and maintain app continuity in the [Configuration and continuity](https://developer.android.com/guide/topics/large-screens/configuration-and-continuity) overview.  
![](https://developer.android.com/static/images/guide/topics/large-screens/quality-guidelines/tier-3/multi-window_multi-resume_icon.svg)  

### [Multi-window and multi-resume](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#t3_multi-window_multi-resume)

Enable your app to run in multi‑window mode alongside other apps either in split‑screen mode or desktop windowing mode.

Guidelines --- [Multi-Window:Functionality](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Multi-Window:Functionality) and [Multi-Window:Multi-Resume](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Multi-Window:Multi-Resume)  

#### What

App fills the app window and is fully functional in multi‑window mode. App supports multi‑resume in multi‑window mode. App updates its UI and ongoing processes, such as media playback, when the app is not the top focused app. App manages access to exclusive resources such as cameras.  

#### Why

Large screens make multi‑window mode more usable. Multi‑window mode makes users more productive.  

#### How

Learn how to develop for multi-window mode in the [Multi-window mode and multi-resume](https://developer.android.com/guide/topics/large-screens/multi-window-mode-and-multi-resume) overview.  
![](https://developer.android.com/static/images/guide/topics/large-screens/quality-guidelines/tier-3/camera_preview_media_projection_icon.svg)  

### [Camera preview and media projection](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#t3_camera_preview_media_projection)

If your app includes a camera preview, validate the preview for orientation and aspect ratio on large screens.

Guidelines --- [Media:Camera_Preview](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Media:Camera_Preview) and [Media:Projection](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Media:Projection)  

#### What

App provides a properly proportioned and oriented camera preview in landscape and portrait orientations, folded and unfolded device states, and multi‑window mode. App supports media projection in all device configurations in the proper orientation and proportions.  

#### Why

Large screen foldables in portrait orientation can have a landscape aspect ratio. Multi‑window mode can display apps in portrait orientation in a resizable window when the device is landscape.  

#### How

For guidance about camera preview and media projection, see the [Camera preview and media projection](https://developer.android.com/guide/topics/large-screens/camera-preview-and-media-projection) overview.  
![](https://developer.android.com/static/images/guide/topics/large-screens/quality-guidelines/tier-3/keyboard_icon.svg)  

### [Keyboard, mouse, and trackpad](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#t3_keyboard_mouse_trackpad)

Support external input devices by enabling your app to handle keyboard, mouse, and trackpad actions.

Guidelines --- [Input:Keyboard](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Input:Keyboard) and [Input:Mouse_Trackpad](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Input:Mouse_Trackpad)  

#### What

App supports text input using an external keyboard. When an external keyboard is connected or disconnected, app switches between physical and virtual keyboards without relaunching the app. App supports basic mouse and trackpad input.  

#### Why

Users often connect an external keyboard or mouse to tablets. Chromebooks come with built‑in keyboards and trackpads.  

#### How

See the [Keyboard, mouse, and trackpad](https://developer.android.com/guide/topics/large-screens/keyboard-mouse-and-trackpad-tier-3) overview to learn how to add support for external input devices in your app.  
![](https://developer.android.com/static/images/guide/topics/large-screens/quality-guidelines/tier-3/stylus_basic_icon.svg)  

### [Stylus](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#t3_stylus)

Enable users to select and manipulate UI elements, including scrolling through lists, pickers, and other scrollable content, with a stylus.

On Android 14 (API level 34) and higher, support writing and editing text in text input fields using a stylus. On ChromeOS M114 and higher, enable users to write and edit text in text input fields in [`WebView`](https://developer.android.com/reference/kotlin/android/webkit/WebView) components using a stylus.

Guidelines --- [Stylus:Basic](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Stylus:Basic) and [Stylus:Text_Input](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Stylus:Text_Input)  

#### What

App supports basic stylus input such as selecting and manipulating UI elements on stylus‑equipped tablets, foldables, and ChromeOS devices.

On Android 14 and higher and ChromeOS M114 and higher, apps enable text input in [`EditText`](https://developer.android.com/reference/kotlin/android/widget/EditText) and `WebView` components, respectively.  

#### Why

Large screens are ideal for stylus‑enabled apps. Some large screen devices come equipped with a stylus.  

#### How

Basic stylus input is the same as touch input, which Android fully supports. No special development is needed to provide basic stylus input.

On Android 14 and higher, `EditText` components support input using a stylus by default; no special development required. On ChromeOS M114 and higher, `WebView` components support stylus input in text fields by default.

For more information, see the [Stylus](https://developer.android.com/guide/topics/large-screens/stylus-tier-3) overview.