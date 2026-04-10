---
title: https://developer.android.com/media/camera/camerax
url: https://developer.android.com/media/camera/camerax
source: md.txt
---

# CameraX overview

# CameraX overviewPart of[Android Jetpack](https://developer.android.com/jetpack).

CameraX is a Jetpack library, built to help make camera app development easier. For new apps, we recommend starting with CameraX. It provides a consistent, easy-to-use API that works across the vast majority of Android devices, with backward-compatibility to Android 5.0 (API level 21). If you're migrating an app from Camera1, see our[Camera1 to CameraX migration guide](https://developer.android.com/training/camerax/camera1-to-camerax).  
[Get started with CameraX](https://codelabs.developers.google.com/codelabs/camerax-getting-started)

## Primary benefits

CameraX improves the developer experience in several key ways.

### Broad device compatibility

CameraX supports devices running[Android 5.0 (API level 21)](https://developer.android.com/about/versions/lollipop)and higher, representing over 98% of existing Android devices.

### Ease of use

CameraX emphasizes use cases, which allow you to focus on the task you need to get done instead of managing device-specific nuances. Most common camera use cases are supported:

- [Preview](https://developer.android.com/training/camerax/preview): View an image on the display.
- [Image analysis](https://developer.android.com/training/camerax/analyze): Access a buffer seamlessly for use in your algorithms, such as to pass to ML Kit.
- [Image capture](https://developer.android.com/training/camerax/take-photo): Save images.
- [Video capture](https://developer.android.com/training/camerax/video-capture): Save video and audio.

### Consistency across devices

![](https://developer.android.com/static/images/training/camera/camerax/testing-lab.png)

**Figure 2.**Automated CameraX test lab ensures a consistent API experience across many device types and manufacturers.

Maintaining consistent camera behavior is hard. You have to consider aspect ratio, orientation, rotation, preview size, and image size. With CameraX, these basic behaviors just work.

We maintain an automated CameraX test lab that tests a variety of camera behaviors across[a range of devices](https://developer.android.com/training/camerax/devices)and all operating system versions since Android 5.0. These tests run on an ongoing basis to identify and fix a wide range of issues.

### Camera extensions

![](https://developer.android.com/static/images/training/camera/camerax/portrait-mode.png)

**Figure 3.**An image captured with the bokeh (portrait) effect using CameraX.

CameraX has an optional[Extensions](https://developer.android.com/training/camerax/extensions-api)API that allows you to access the same features and capabilities as a device's native camera app with as few as two lines of code.

Extensions include bokeh (portrait), high dynamic range (HDR), night mode, and face retouching, all of which require device support.

### Case study

To see how CameraX has simplified development for Monzo, see[their case study](https://developer.android.com/stories/apps/monzo-camerax).

## Documentation

- [CameraX architecture](https://developer.android.com/training/camerax/architecture)
- [Configuration options](https://developer.android.com/training/camerax/configuration)
- [Implement a preview](https://developer.android.com/training/camerax/preview)
- [Image analysis](https://developer.android.com/training/camerax/analyze)
- [Image capture](https://developer.android.com/training/camerax/take-photo)
- [Video capture](https://developer.android.com/training/camerax/video-capture)
- [Camera extensions](https://developer.android.com/training/camerax/extensions-api)
- [Transform output](https://developer.android.com/training/camerax/transform-output)
- [Use case rotations](https://developer.android.com/training/camerax/orientation-rotation)
- [Lab-tested devices](https://developer.android.com/training/camerax/devices)

## Additional resources

To learn more about CameraX, consult the following additional resources.

### Codelab

<br />

- [Getting Started with CameraX](https://codelabs.developers.google.com/codelabs/camerax-getting-started)

### Code sample

- [CameraX sample apps](https://github.com/android/camera-samples/)