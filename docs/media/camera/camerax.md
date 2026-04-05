---
title: CameraX overview  |  Android media  |  Android Developers
url: https://developer.android.com/media/camera/camerax
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Camera & media dev center](https://developer.android.com/media)
* [Guides](https://developer.android.com/media/guides)

Stay organized with collections

Save and categorize content based on your preferences.




# CameraX overview   Part of [Android Jetpack](/jetpack).

CameraX is a Jetpack library, built to help make camera app development easier.
For new apps, we recommend starting with CameraX. It provides a consistent,
easy-to-use API that works across the vast majority of Android devices, with
backward-compatibility to Android 5.0 (API level 21). If you're migrating an app
from Camera1, see our
[Camera1 to CameraX migration guide](/training/camerax/camera1-to-camerax).

[Get started with CameraX](https://codelabs.developers.google.com/codelabs/camerax-getting-started)

## Primary benefits

CameraX improves the developer experience in several key ways.

### Broad device compatibility

CameraX supports devices running
[Android 5.0 (API level 21)](/about/versions/lollipop) and higher,
representing over 98% of existing Android devices.

### Ease of use

CameraX emphasizes use cases, which allow you to focus on the task you need
to get done instead of managing device-specific nuances.
Most common camera use cases are supported:

* [Preview](/training/camerax/preview): View an image on the display.
* [Image analysis](/training/camerax/analyze): Access a buffer seamlessly for
  use in your algorithms, such as to pass to ML Kit.
* [Image capture](/training/camerax/take-photo): Save images.
* [Video capture](/training/camerax/video-capture): Save video and audio.

### Consistency across devices

![](/static/images/training/camera/camerax/testing-lab.png)

**Figure 2.** Automated CameraX test lab ensures a consistent API
experience across many device types and manufacturers.

Maintaining consistent camera behavior is hard. You have to consider
aspect ratio, orientation, rotation, preview size, and image size.
With CameraX, these basic behaviors just work.

We maintain an automated CameraX test lab that tests a variety of camera
behaviors across [a range of devices](/training/camerax/devices)
and all operating system versions since Android 5.0. These tests
run on an ongoing basis to identify and fix a wide range of issues.

### Camera extensions

![](/static/images/training/camera/camerax/portrait-mode.png)

**Figure 3.** An image captured with
the bokeh (portrait) effect using CameraX.

CameraX has an optional [Extensions](/training/camerax/extensions-api) API that
allows you to access the same features and capabilities as a device's native
camera app with as few as two lines of code.

Extensions include bokeh (portrait), high dynamic range (HDR),
night mode, and face retouching, all of which require device support.

### Case study

To see how CameraX has simplified development for Monzo,
see [their case study](/stories/apps/monzo-camerax).

## Documentation

* [CameraX architecture](/training/camerax/architecture)
* [Configuration options](/training/camerax/configuration)
* [Implement a preview](/training/camerax/preview)
* [Image analysis](/training/camerax/analyze)
* [Image capture](/training/camerax/take-photo)
* [Video capture](/training/camerax/video-capture)
* [Camera extensions](/training/camerax/extensions-api)
* [Transform output](/training/camerax/transform-output)
* [Use case rotations](/training/camerax/orientation-rotation)
* [Lab-tested devices](/training/camerax/devices)

## Additional resources

To learn more about CameraX, consult the following additional resources.

### Codelab

- [Getting Started with CameraX](https://codelabs.developers.google.com/codelabs/camerax-getting-started)

### Code sample

- [CameraX sample apps](https://github.com/android/camera-samples/)