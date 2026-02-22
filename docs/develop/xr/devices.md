---
title: https://developer.android.com/develop/xr/devices
url: https://developer.android.com/develop/xr/devices
source: md.txt
---

Android XR is a platform that supports a variety of XR devices. Each type of XR device has different capabilities that can support immersive and augmented experiences.

## XR headsets

![A stylized illustration of an XR headset.](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg)

XR headsets use high-resolution cameras to capture the physical world and stream it to displays inside the headset.

- **Visuals**: Because the display is opaque, it can render "true black" and fully occlude the real world. This allows for complete virtual immersion (VR) where the physical environment is replaced entirely.
- **Field of View**: Headsets typically offer a wide field of view (110°+), allowing for immersive, peripheral-filling interfaces.
- **Inputs**: Primary inputs often include hand tracking, eye tracking, and optional 6DoF controllers.

### Supported tools and technologies for XR headsets

Android XR supports a variety of familiar tools and technologies to help you build immersive experiences for XR headsets:

- [**Jetpack XR SDK**](https://developer.android.com/develop/xr/jetpack-xr-sdk): Use familiar Android APIs and frameworks. You can use Jetpack Compose for XR, Android Studio, the emulator, and your preferred 3D tools to create immersive experiences.
- [**Unity**](https://developer.android.com/develop/xr/unity): Get full access to Unity's content production features, and bring apps from other platforms to Android XR. Promote smooth development with performance optimization tools, a large asset store, and a strong community.
- [**OpenXR**](https://developer.android.com/develop/xr/openxr): Streamline development with OpenXR's royalty-free open standard. Build anywhere using a common set of APIs to develop XR apps that work across a range of devices.
- [**WebXR**](https://developer.android.com/develop/xr/web): Use the power of web technologies to build XR experiences directly in a browser. WebXR makes extended reality available to anyone with a device and a supported web browser.

## Wired XR glasses

![A stylized illustration of wired XR glasses.](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg)

Wired XR glasses use additive light displays (such as waveguides) to project light onto semi-transparent lenses. Users view the physical world directly through the glass, with digital content overlaid on top.

- **Additive color \& transparency**: In an additive display, pure black renders as transparent. Darker colors are rendered by emitting less light, which effectively reduces their opacity.
- **Field of View**: The FOV is more focused, typically between 50° and 70°. While this still provides a wide-screen experience, it's narrower than a headset. UI scaling automatically adjusts content to keep it within this focused area.
- **Dimming**: Many devices use electrochromatic dimming to darken the lenses globally, helping virtual content stand out against bright physical environments.
- **Inputs**: Due to their form factor, glasses often rely on natural inputs (hands) and peripheral devices (such as phones, bluetooth keyboards/mice) rather than bulky dedicated controllers.

### Supported tools and technologies for wired XR glasses

Android XR supports a variety of familiar tools and technologies to help you build immersive experiences for wired XR glasses:

- [**Jetpack XR SDK**](https://developer.android.com/develop/xr/jetpack-xr-sdk): Use familiar Android APIs and frameworks. You can use Jetpack Compose for XR, Android Studio, the emulator, and your preferred 3D tools to create immersive experiences.
- [**Unity**](https://developer.android.com/develop/xr/unity): Get full access to Unity's content production features, and bring apps from other platforms to Android XR. Promote smooth development with performance optimization tools, a large asset store, and a strong community.
- [**OpenXR**](https://developer.android.com/develop/xr/openxr): Streamline development with OpenXR's royalty-free open standard. Build anywhere using a common set of APIs to develop XR apps that work across a range of devices.
- [**WebXR**](https://developer.android.com/develop/xr/web): Use the power of web technologies to build XR experiences directly in a browser. WebXR makes extended reality available to anyone with a device and a supported web browser.

## AI glasses

![A stylized illustration of AI glasses.](https://developer.android.com/static/images/develop/xr/ai-glasses-icon.svg)

AI Glasses are lightweight and portable for all day wear. With built-in speakers, a camera, and microphone; you can build intelligent and hands-free augmented experiences.

- **Additive color \& transparency**: Some AI glasses feature an additive display, where pure black renders as transparent. Darker colors are rendered by emitting less light, which effectively reduces their opacity.
- **Mobility**: AI glasses are lightweight and portable, letting the user wear them as they go about daily life.
- **Inputs**: Primary inputs often include physical input such as a touchpad and voice input using the microphone array.
- **AI first**: AI glasses provide a unique opportunity for new interaction design with the overlap of a new, highly-contextual and personal form factor with evolving AI patterns. For AI glasses, you will have access to the device's hardware and features, including camera, microphone, and touchpad, to fully explore new interaction patterns between AI, your app, and glasses with comfort and user safety principles in mind.

  AI glasses bring AI capabilities to the user's eyes and ears. When designing these experiences, consider patterns that recognize AI as an assistant with glanceable visuals.

### Supported tools and technologies for AI glasses

The[**Jetpack XR SDK**](https://developer.android.com/develop/xr/jetpack-xr-sdk)includes all tools you need to build augmented experiences for AI glasses. You can use[Jetpack Compose Glimmer](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer), Android Studio,[the emulator](https://developer.android.com/develop/xr/jetpack-xr-sdk/run/create-avds/ai-glasses), and[ARCore for Jetpack XR](https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore).