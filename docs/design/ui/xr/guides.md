---
title: https://developer.android.com/design/ui/xr/guides
url: https://developer.android.com/design/ui/xr/guides
source: md.txt
---

# Design for Android XR differentiated apps

Android XR supports apps in different stages of development. It's built to minimize the effort it takes for a developer to create an app for multiple platforms and form factors.

Android XR automatically runs compatible Android apps designed for mobile and large screens. With a few adaptations, you can convert it to a differentiated app if you want to make it feel more immersive.

<br />

![An existing mobile app that hasn't been modified to adapt to a large screen or any other form factor.](https://developer.android.com/static/images/design/ui/xr/guides/xr-mobile.jpg)

**XR compatible mobile app**

An existing[mobile](https://developer.android.com/design/ui/mobile)app that hasn't been modified to adapt to a large screen or any other form factor. This type of app is automatically compatible with Android XR as long as it doesn't[require any features](https://developer.android.com/guide/topics/manifest/uses-feature-element)that are[unsupported](https://developer.android.com/develop/xr/get-started#app-manifest), such as telephony. Users can complete critical task flows. They are automatically made available on the Play Store.  
![A large screen Tier 1 or Tier 2 Android app that has implemented layout optimizations for all screen sizes and device configurations.](https://developer.android.com/static/images/design/ui/xr/guides/xr-large-screens.jpg)

**XR compatible large screen app**

A large screen[Tier 1](https://developer.android.com/docs/quality-guidelines/large-screen-app-quality#large_screen_differentiated)or[Tier 2](https://developer.android.com/docs/quality-guidelines/large-screen-app-quality#large_screen_optimized)Android app that has implemented layout optimizations for all screen sizes and device configurations (for example, large screens in addition to mobile), along with enhanced support for external input devices and multitasking. They are automatically made available on the Play Store.  
![An XR differentiated app has a user experience explicitly designed for XR, and it implements features that are only offered on XR.](https://developer.android.com/static/images/design/ui/xr/guides/xr-differentiated.jpg)

**XR differentiated app**

An XR differentiated app has a user experience explicitly designed for XR, and it implements features that are only offered on XR. You can take full advantage of Android XR capabilities and differentiate your app's experiences by adding XR features like spatial panels or XR content such as a 3D video.

<br />

## Design Android XR differentiated apps

When running in Full Space, your XR app can use features to create a sense of presence and deeper level of engagement. To take advantage of the infinite canvas, consider adding the following elements:

<br />

![A spatial panel in an XR app.](https://developer.android.com/static/images/design/ui/xr/guides/xr-spatial.jpeg)

[Spatial panels](https://developer.android.com/design/ui/xr/guides/spatial-ui)

Expand your app across a user's space without constraints. Users can move panels for a personalized experience.  
Alas, your browser doesn't support HTML5 video. That's OK! You can still[download the video](https://developer.android.com/static/videos/design/ui/xr/xr-3d-content-opt.mp4)and watch it with a video player.

[3D models](https://developer.android.com/design/ui/xr/guides/3d-content)

Encourage hands-on learning and exploration with 3D models that users can rotate, resize, and move.  
![A spatial environment in an XR app.](https://developer.android.com/static/images/design/ui/xr/guides/xr-environments.jpeg)

[Spatial environments](https://developer.android.com/design/ui/xr/guides/environments)

Transport users to a new space and heighten focus with custom-built immersive scenes.

<br />

## Tips to get started quickly

- Customize your app UI however you like, just like on Android.
- Follow Material Design's[large-screen guidelines](https://developer.android.com/docs/quality-guidelines/large-screen-app-quality)to ensure apps look and function correctly at any size.
- Follow Android XR[visual design](https://developer.android.com/design/ui/xr/guides/visual-design)recommendations for typography, colors, and[motion](https://developer.android.com/design/ui/xr/guides/motion). Consider using[Material Design components](https://m3.material.io/components)to make your app feel native to the platform.
- Identify key moments where spatial features will improve the user experience and unlock the unique capabilities of XR.
- Add clear visual cues to let users quickly switch between Full Space and Home Space. For example, you can use[collapse content](https://fonts.google.com/icons?icon.query=collapse+content)and[expand content](https://fonts.google.com/icons?icon.query=expand+content)icons for buttons to trigger transitions.