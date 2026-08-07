---
title: https://developer.android.com/develop/xr/check-mobile-app-readiness
url: https://developer.android.com/develop/xr/check-mobile-app-readiness
source: md.txt
---

<br />

<br />

Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

Existing 2D mobile apps are automatically compatible with Android XR headsets and wired XR glasses devices as long as they don't [require any features](https://developer.android.com/guide/topics/manifest/uses-feature-element) that are unsupported, such as [telephony](https://developer.android.com/guide/topics/manifest/uses-feature-element#telephony-hw-features). Users can complete critical task flows in an Android XR compatible app, but they'll have a [less-optimal user experience](https://developer.android.com/docs/quality-guidelines/android-xr#android-xr). Ideally, you should design a [differentiated experience for XR](https://developer.android.com/docs/quality-guidelines/android-xr#android-xr-differentiated) that implements features that are only offered on XR devices. For more information, see our [developer guide for bringing your app into 3D with XR](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-xr-to-existing).

However, while you develop spatial features for your app, you can also optimize your existing app experience for users who have it on their Android XR devices today. To achieve this, follow the adaptive app quality guidelines and aim for at least [Tier 2](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/tier-2) support. As you begin, review the sections in this guide, which highlight the areas you can focus on to promote a great experience for your users on Android XR.

## Check your app

Check your app for each of the following categories that commonly affect an app's experience on Android XR. For each category, see the related adaptive app guidelines and developer guides to help you build a great adaptive experience.
![](https://developer.android.com/static/images/guide/topics/large-screens/quality-guidelines/tier-3/configuration_continuity_icon.svg)

### Display and orientation

Many common issues in Android XR are caused by assumptions about a device's orientation and screen configuration.

#### What to check

- **Natural orientation mismatches** : Most mobile phones have a natural orientation ([`Surface.ROTATION_0`](https://developer.android.com/reference/kotlin/android/view/Surface#rotation_0)) that corresponds to portrait mode, whereas many XR devices use landscape as their natural orientation.
- **Avoid orientation hardcoding**: Hardcoding an app's orientation can prevent it from adapting to different screens and form factors.
- **Configuration changes**: Make sure your app handles configuration changes. Don't assume a device is a mobile phone when laying out your app.
- **Layout and rendering**: XR devices like XR headsets and wired XR glasses can have very high resolution displays. Check specific window bounds instead of the physical display size to avoid overly large or cropped UI elements. Don't place app content and interactive buttons too close to the edge of a window to avoid clipping.

#### Guidance

- **Developer guides** :
  - [App orientation restricted on phones but not on large screens](https://developer.android.com/develop/adaptive-apps/cookbook/orientation-restriction)
  - [App orientation, aspect ratio, and resizability](https://developer.android.com/develop/ui/compose/layouts/adaptive/app-orientation-aspect-ratio-resizability)
  - [Configuration and continuity](https://developer.android.com/guide/topics/large-screens/configuration-and-continuity)
- **Adaptive app guidelines** :
  - [Config_Changes](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/tier-3#t3_configuration_continuity)
![](https://developer.android.com/static/images/guide/topics/large-screens/quality-guidelines/tier-3/multi-window_multi-resume_icon.svg)

### Dynamic resizing and multi-window

XR headsets and wired XR glasses feature spatial environments where app windows can be resized and repositioned freely.

#### What to check

- **Support window resizing**: Your app should maintain user progress, scroll position, and text input during and after resizing events. In addition, make sure you adapt your app's UI to the new window dimensions.

#### Guidance

- **Developer guides** :
  - [Support multi-window mode](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-multi-window-mode)
  - [Use window size classes](https://developer.android.com/develop/ui/compose/layouts/adaptive/use-window-size-classes)
  - [Multi-window mode and multi-resume](https://developer.android.com/guide/topics/large-screens/multi-window-mode-and-multi-resume)
- **Adaptive app guidelines** :
  - [Multi-Window_Functionality](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/tier-3#t3_multi-window_multi-resume)
![](https://developer.android.com/static/images/guide/topics/large-screens/quality-guidelines/tier-3/camera_preview_media_projection_icon.svg)

### Cameras

Camera apps require special considerations for sensors and the virtual, front-facing cameras on XR headsets and wired XR glasses.

#### What to check

- **Natural device orientation**: XR devices often use a landscape orientation as their natural orientation. The system counts camera sensor rotation values relative to the device's natural orientation. This means that on XR devices, when the camera sensor is at 0 degrees of rotation, the orientation would usually be landscape, whereas on a phone, the orientation would usually be portrait. For this reason, don't assume either the device or camera sensor orientation based on the rotation angle value.
- **Virtual front-facing cameras**: Unlike a mobile phone, XR devices with a front-facing camera provide a virtual, avatar view of the user. This virtual view might be flipped horizontally, so your app shouldn't assume a certain orientation.

#### Guidance

- **Developer guides** :
  - [CameraX use case rotations](https://developer.android.com/media/camera/camerax/orientation-rotation)
  - [Implement a preview](https://developer.android.com/media/camera/camerax/preview)
  - [Camera preview and media projection](https://developer.android.com/guide/topics/large-screens/camera-preview-and-media-projection)
- **Adaptive app guidelines** :
  - [Camera_Preview](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/tier-3#t3_camera_preview_media_projection)
![](https://developer.android.com/static/images/guide/topics/large-screens/quality-guidelines/tier-3/keyboard_icon.svg)

### Input

Apps should support the variety of input methods supported on XR headsets and wired XR glasses.

#### What to check

- **Touch targets**: Use larger touch targets than other form factors to increase precision, comfort, and usability.
- **Keyboard support**: Test your app with both the system virtual keyboard and external keyboards.
- **Gamepad support**: Support game controllers while navigating app menus and during gameplay.

#### Guidance

- **Developer guides** :
  - [Targets in Android XR](https://developer.android.com/design/ui/xr/guides/visual-design#targets-android)
  - [Input compatibility on large screens](https://developer.android.com/develop/ui/compose/touch-input/input-compatibility-on-large-screens)
  - [Support game controllers](https://developer.android.com/games/sdk/game-controller/overview)
  - [Handle controller actions](https://developer.android.com/games/sdk/game-controller/controller-input)
  - [Keyboard, mouse, and trackpad](https://developer.android.com/guide/topics/large-screens/keyboard-mouse-and-trackpad-tier-3)
- **Adaptive app guidelines** :
  - [Touch_Targets](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/tier-2#t2_user_interface) (see [Targets in Android XR](https://developer.android.com/design/ui/xr/guides/visual-design#targets-android) for XR-specific target sizes)
  - [Keyboard_Input](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/tier-3#t3_keyboard_mouse_trackpad)
![](https://developer.android.com/static/images/guide/topics/large-screens/quality-guidelines/tier-1/multitasking_multi-instance_icon.svg)

### System lifecycle

Apps should handle system lifecycle events gracefully.

#### What to check

- **Audio and video continuity during resizing**: Media playback should stay synchronized during window resizing.
- **Audio and video continuity when doffing and donning**: Media playback should resume where it left off when a user takes the device off or puts it back on.

#### Guidance

- **Developer guides** :
  - [Introduction to Jetpack Media3](https://developer.android.com/media/media3)
  - [Background playback with a MediaSessionService](https://developer.android.com/media/media3/session/background-playback)
  - [Multi-resume](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-multi-window-mode#multi-resume)
  - [Multi-window mode and multi-resume](https://developer.android.com/guide/topics/large-screens/multi-window-mode-and-multi-resume)
- **Adaptive app guidelines** :
  - [Config_Changes](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/tier-3#t3_configuration_continuity)
  - [Multi-Resume](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/tier-3#t3_multi-window_multi-resume)