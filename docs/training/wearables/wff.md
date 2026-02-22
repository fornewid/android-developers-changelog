---
title: https://developer.android.com/training/wearables/wff
url: https://developer.android.com/training/wearables/wff
source: md.txt
---

**Note:**As of January 2026, the Watch Face Format is required for
installing watch faces on all Wear OS devices.

Learn more about the user-facing changes in this
[Help Center
article](https://support.google.com/wearos/thread/284572445).  
![](https://developer.android.com/static/images/watch-faces/watch-face-creators.png)

A watch face is the first thing a user sees when they look at their watch,
making it the most frequently used surface of Wear OS. Users rely on watch faces
to customize their watches to suit their style and provide quick information at
a glance.

## Options for creating watch faces

The Watch Face format (WFF) makes it easier than ever to build a watch face.
Created in partnership with Samsung, the Watch Face Format is a declarative XML
format to configure the appearance and behavior of watch faces. Unlike other
watch face APIs, where your APK must include the code to render the watch face,
the Watch Face Format only requires resources and declarative instructions. The
Wear OS platform handles the logic needed to render the watch face so you can
focus on your creative ideas, rather than code optimizations or battery
performance.

Watch faces built with this format require less maintenance and fewer updates
than those built using the legacy Jetpack Watch Face libraries. For example, you
don't need to update your watch face to benefit from improvements in performance
or battery consumption, or to get the latest bug fixes.

We provide several ways to create a watch face:

- If you prefer a What-You-See-Is-What-You-Get style tool that lets you design the watch face directly, use [Watch Face Studio](https://developer.samsung.com/watch-face-studio/overview.html), which we support in partnership with Samsung.
- If you're comfortable using [Figma](https://www.figma.com/design/) as a designer, or if you're looking to accelerate the first few steps of creating a watch face as a developer, use [Watch Face Designer](https://developer.android.com/training/wearables/watch-face-designer), which you access using a plug-in within Figma.
- If you prefer to manage your watch configuration manually and publish to
  your own app store, you can define watch faces using XML.
  Android Studio includes support for [building watch faces](https://developer.android.com/training/wearables/wff/build#android-studio) that use
  Watch Face Format. You can then visualize these watch faces by running them
  on a device.

  | **Note:** The guides on how to [represent the time](https://developer.android.com/training/wearables/wff/time), and subsequent guides within this part of the documentation, target developers who either use XML or build custom tools to create watch faces using Watch Face Format.

After you've created your watch face, you can publish it in several different
ways, such as through [Google Play](https://support.google.com/googleplay/android-developer/answer/13560201) or using [Watch Face Push](https://developer.android.com/training/wearables/watch-face-push).

## About the format

At the heart of a Watch Face Format (WFF) watch face is a document that defines
the layout and behavior of the watch face. This document is written in XML,
conforming to the WFF specification.

The Wear OS system includes a watch face renderer component. This component
parses your WFF XML document and renders a watch face from it. Other resources,
such as images and fonts, are pulled in as necessary.

This approach means you only need to spend time describing how the watch
face should look, and Wear OS handles all of the code for drawing the watch
face.

To deploy a Watch Face Format watch face to a device, package the XML document
in a standard AAB or APK package.

The following diagram shows an overview of the approach:
![How the Wear OS system renders a watch face from a
Watch Face Format XML document.](https://developer.android.com/static/wear/images/wff/watch-face-format-rendering.svg)

## Versioning in WFF

As WFF evolves, additional features are added, represented by more elements,
attributes, and data sources that all use the Watch Face Format.

For example, WFF version 2 introduced Weather support as a data source, which
is not available in WFF version 1.

When designing your watch face, be aware of which features you
want to use and their version availability. The reference guide marks
all features with their availability.

Each version of WFF aligns with a Wear OS release:

| WFF version | Minimum Wear OS version | Minimum API level |
|---|---|---|
| 1 | 4 | 33 |
| 2 | 5 | 34 |
| 3 | 5.1 | 35 |
| 4 | 6 | 36 |

[See this guidance](https://developer.android.com/training/wearables/wff/setup#declare-wff-use) for configuring your `AndroidManifest.xml` and Gradle
build file appropriately.

## Learn more

Learn more about the Watch Face Format in these guides:

- [Available features](https://developer.android.com/training/wearables/wff/features): Explore the watch face capabilities that each version of Watch Face Format supports.
- [Design guidelines](https://developer.android.com/design/ui/wear/guides/surfaces/watch-faces): Learn best practices for your watch face's layout and user experience.
- [Watch Face Designer](https://developer.android.com/training/wearables/watch-face-designer): Learn how to use the Figma plugin to create your watch face.
- [Setup](https://developer.android.com/training/wearables/wff/setup): Configure an Android App Bundle that supports the Watch Face Format.
- [GitHub samples](https://github.com/android/wear-os-samples/tree/main/WatchFaceFormat): Get started by building sample watch faces and deploying them on the Wear OS emulator or your physical device.
- [Optimize memory usage](https://developer.android.com/training/wearables/wff/memory-usage): Learn how to configure your watch face so the system consumes as little memory as possible when rendering your watch face.
- [XML reference](https://developer.android.com/training/wearables/wff/watch-face): Explore the individual elements that are parts of a Watch Face Format file. The root element is always `WatchFace`. Note: To view features from a specific Watch Face Format version in the XML reference, check that the appropriate version button is selected at the top of the documentation page.
- [Publishing guide](https://support.google.com/googleplay/android-developer/answer/13560201): Learn how to publish and monetize your watch face through the Play Store and alternative methods.
- [WFF and memory validator](https://github.com/google/watchface): Use these open source tools to check your Watch Face Format file for errors and confirm acceptable memory usage before submitting to Google Play.