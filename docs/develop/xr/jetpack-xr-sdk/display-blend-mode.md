---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/display-blend-mode
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/display-blend-mode
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) ![](https://developer.android.com/static/images/develop/xr/ai-glasses-icon.svg) Audio \&  
Display Glasses [](https://developer.android.com/develop/xr/devices#audio-display) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

Different types of devices have different types of display characteristics. Your
app can check the display characteristics of the device it is running on to
adapt your content to make sure it is
[displayed in the best possible way](https://developer.android.com/design/ui/xr/guides/get-started#display-technologies).

## The types of display blend modes

A [`DisplayBlendMode`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/DisplayBlendMode) value describes how the imagery is
overlaid on top of the real world. The display technology fundamentally changes
how digital content blends with the physical world.
Alas, your browser doesn't support HTML5 video. That's OK! You can still [download the
video](https://developer.android.com/static/images/design/ui/xr/additive-display.mp4) and watch it with a video player.

### Additive blending

When the current display blend mode is [`ADDITIVE`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/DisplayBlendMode#ADDITIVE()), black pixels
appear transparent. This is often used by devices with transparent lenses that
directly allow the user's environment to pass through to the user's eyes. The
device can only add more light to the surface.

Concretely, this means that virtual content is added to the real world by adding
the pixel values for each of red, green, and blue components. Alpha is ignored,
and black pixels appear see-through.

### Alpha blending

When the current display blend mode is [`ALPHA_BLEND`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/DisplayBlendMode#ALPHA_BLEND()), virtual
content is added to the real world by alpha blending the pixel values based on
the alpha component. This is the case with XR headsets, which use an opaque
display to render content. The brightness of each pixel can be controlled and
pixels can be set to appear black. Depending on the active [spatial
environment](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-environments), these pixels might represent the real world
through a camera stream, or a digital environment.

### No display

When the current display blend mode is [`NO_DISPLAY`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/DisplayBlendMode#NO_DISPLAY()),
the device cannot display any pixels.

## Obtain the current `DisplayBlendMode`

To check the active [`DisplayBlendMode`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/DisplayBlendMode), use
[`XrDevice.getPreferredDisplayBlendMode`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/XrDevice#getCurrentDevice(androidx.xr.runtime.Session)):


```kotlin
val preferredDisplayBlendMode =
    XrDevice.getCurrentDevice(session).getPreferredDisplayBlendMode()
when (preferredDisplayBlendMode) {
    ADDITIVE -> {
        // Virtual content is added to the real world by adding the pixel values for each of
        // Red, Green, and Blue components. Alpha is ignored. Black pixels will appear transparent.
    }

    ALPHA_BLEND -> {
        // Virtual content is added to the real world by alpha blending the pixel values based
        // on the Alpha component.
    }

    NO_DISPLAY -> {
        // Device doesn't have a display.
    }
}
```

<br />

## Learn more

- [Design for different types of display technologies](https://developer.android.com/design/ui/xr/guides/get-started#display-technologies)