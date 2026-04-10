---
title: https://developer.android.com/design/ui/xr/guides/foundations
url: https://developer.android.com/design/ui/xr/guides/foundations
source: md.txt
---

The Android XR system uses interactivity models similar to those in mobile and
large-screen apps to help users understand how to use XR. It includes known
patterns like the home screen, apps overview, back stack, and more.

To help you build integrated and boundless experiences, Android XR provides
natural gesture navigation, multimodal inputs, and new spatial and 3D
capabilities.

## Home Space and Full Space

A user can experience your app in two spaces, Home Space and Full Space. In Home
Space, a user is able to multitask with your app running side by side with other
apps. In Full Space, your app takes center stage as the focus of the user's
experience with full access to the immersive capabilities of Android XR.
| **Note:** Spatial capabilities can change as users interact with your app or the system. To avoid issues, your app should [check for spatial capabilities](https://developer.android.com/develop/xr/jetpack-xr-sdk/check-spatial-capabilities) to determine what's supported.


![Home Space](https://developer.android.com/static/images/design/ui/xr/guides/xr-foundations-1.jpeg)

**Home Space**

- Multiple apps run side by side so users can multitask.
- Any [compatible](https://developer.android.com/develop/xr/get-started) mobile or large screen Android app can operate in Home Space with no additional development.
- Android apps developed with [large screen-optimized guidance](https://developer.android.com/guide/topics/large-screens/tier-2-overview) adapt best.
- Home Space supports system environments. It does not support [spatial
  panels](https://developer.android.com/design/ui/xr/guides/spatial-ui), [3D models](https://developer.android.com/design/ui/xr/guides/3d-content), or an app's [spatial environments](https://developer.android.com/design/ui/xr/guides/environments).
- Apps have constrained boundaries.
- Default size: 1024 x 720dp
- Minimum size 385 x 595dp, maximum 2560 x 1800dp
- Apps launch 1.75 meters from a user.  
![Full Space](https://developer.android.com/static/images/design/ui/xr/guides/xr-foundations-2.jpeg)

**Full Space**

- One app runs at a time, with no space boundaries. All other apps are hidden.
- You can [spatialize an existing Android app](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-xr-to-existing) in Full Space.
- You can add [spatial panels](https://developer.android.com/design/ui/xr/guides/spatial-ui), [3D models](https://developer.android.com/design/ui/xr/guides/3d-content), [spatial environments](https://developer.android.com/design/ui/xr/guides/environments), or spatial audio to take advantage of the space.
- Play stereoscopic [spatial videos](https://developer.android.com/design/ui/xr/guides/spatial-ui#spatial-videos).
- Apps can overwrite the [launch position](https://developer.android.com/design/ui/xr/guides/visual-design#panel-depth) and have move and resize capabilities.
- Apps can open directly into Full Space.
- [Unity](https://docs.unity3d.com/Manual/index.html), [OpenXR](https://registry.khronos.org/OpenXR/specs/1.0/styleguide.html), and [WebXR](https://immersiveweb.dev/) apps operate in an unmanaged Full Space. Refer to each platform's documentation for specific interaction capabilities.

<br />

Alas, your browser doesn't support HTML5 video. That's OK! You can still [download the video](https://developer.android.com/static/videos/design/ui/xr/xr-foundations-3-opt.mp4) and watch it with a video player.  
**Recommendation** : Add clear visual cues to let users quickly switch between Full Space and Home Space. For example, you can use [collapse](https://fonts.google.com/icons?icon.query=collapse) and [expand](https://fonts.google.com/icons?icon.query=expand) icons for buttons to trigger transitions.

## Give users control over their environment

In Android XR, an environment is the real or virtual space that a user sees
while wearing an XR device. It is unconstrained by the physical limitations of
mobile and desktop screens.

- A spatial environment simulates a fully immersive virtual space that takes over a user's physical space. Available in Full Space only. For example, a user watches a movie in a virtual luxury cinema.
- A passthrough environment adds digital elements to a user's physical surroundings. For example, a user opens multiple large-screen apps while simultaneously seeing their real-life room.

| **Note:** Full immersion behaves differently on wired XR glasses. Users retain visibility of their physical surroundings in their periphery and through the display's inherent transparency.

[Learn how to build spatial environments in Full Space](https://developer.android.com/design/ui/xr/guides/environments).

### System environments

Users can choose environments provided by the Android XR system. These system
environments can be used in Home Space or Full Space. If an app doesn't define a
specific environment, it will inherit the system environment --- either in
passthrough or a virtual environment.

## Understanding system gestures

Android XR extends familiar mobile actions like press, pinch, and swipe to a
gesture-based navigation system.

Items are selected by pinching with the index finger and thumb on the primary
hand, which is the spatial equivalent of tapping on a touchscreen or pressing a
mouse button. A held pinch is used to scroll, move or resize windows, and select
and move UI elements or objects in 2D and 3D space.  
Alas, your browser doesn't support HTML5 video. That's OK! You can still [download the video](https://developer.android.com/static/videos/design/ui/xr/Input9.mp4) and watch it with a video player.  
A user selects items by pinching with the index finger and thumb on the primary hand.

Users navigate by facing their primary hand's palm inward, pinch and holding
their index finger and thumb. Their hand moves up, down, left, or right, and
releases to select an option. Users can set their primary hand preference in
**Input Settings**.  
Alas, your browser doesn't support HTML5 video. That's OK! You can still [download the video](https://developer.android.com/static/videos/design/ui/xr/xr-foundations-5.webm) and watch it with a video player.  
Users can open the gesture navigation menu anywhere, anytime to:

- **Go back** : Operates the same as the [back stack](https://developer.android.com/guide/components/activities/tasks-and-back-stack) on Android mobile, returning to the previous item.
- **Launcher**: Takes users to the home screen.
- **Recents**: Users can open, close, and switch apps.

## Design with multimodal inputs

It's essential to design immersive applications that are accessible to a wide
range of users. You should allow users to customize input methods to suit their
individual preferences and abilities.

To help you achieve this, Android XR supports a variety of input methods,
including hand and eye tracking, voice commands, Bluetooth-connected keyboards,
traditional and adaptive mice, trackpads, and six degrees of freedom (6DoF)
controllers. Your app should automatically work with these built-in
modalities. Since available input options vary across devices and user setups,
avoid relying on a single method. Designing for flexibility ensures your app
works well for everyone.

Make sure you provide visual or audio feedback to confirm user actions for any
interaction model you choose.

[Learn about design considerations for XR accessibility](https://developer.android.com/design/ui/xr/guides/get-started#make-app).

![5 icons representing multimodal input options: hand tracking, voice, eye
tracking, keyboard and mouse, and
controllers.](https://developer.android.com/static/images/design/ui/xr/guides/xr-foundations-4.jpg)

**Hand tracking enables natural interactions**. When developing OpenXR apps, you
can request permission from the system to access hand tracking directly and
include your own custom gestures. These should be designed to be easy to learn,
remember, and perform comfortably.

When designing gestures, keep in mind that they should be comfortable to perform
repeatedly, and not require large hand movements or frequent arm lifting, which
can be fatiguing. If you add virtual hands, ensure they are accurately tracked.

You can also design gestures that mimic real-world actions, such as picking up
or throwing. Using familiar gestures may help users understand interactions more
quickly.

Be aware that similarity to system gestures can lead to conflicts or accidental
activation of system functions.

**Voice commands are useful for hands-free interaction**. Users can dictate text
inputs and perform some app interactions with spoken instructions through
Gemini. For example, a user might say "Open Google Maps" to open that app.

**Eye tracking enables effortless interactions**, such as selecting objects by
looking at them. To minimize eye strain you can offer alternative input methods.
| **Note:** To protect user privacy, Android XR doesn't share raw eye tracking data with apps. Instead, the system displays a generic hover effect when it detects a user is looking at an interactable element, using information from the Android UI framework.

**Peripheral devices**. Android XR supports external devices like a Bluetooth
keyboard, mouse, and 6DoF controller. For controllers, ensure intuitive button
mappings, and consider allowing users to remap buttons to suit their
preferences.

## Privacy considerations

[Android's privacy recommendations](https://developer.android.com/privacy-and-security/about) apply to building XR apps. Remember to
obtain user consent before collecting any personal identifiable information,
limit user data collection to the essentials, and store it securely.

[Follow Android XR's app quality guidelines](https://developer.android.com/docs/quality-guidelines/android-xr).

*** ** * ** ***

OpenXR™ and the OpenXR logo are trademarks owned
by The Khronos Group Inc. and are registered as a trademark in China,
the European Union, Japan and the United Kingdom.