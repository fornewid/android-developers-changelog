---
title: https://developer.android.com/training/wearables/wff/build
url: https://developer.android.com/training/wearables/wff/build
source: md.txt
---

# Build and deploy a watch face

This page describes the structure of watch faces that use the Watch Face Format, as well as how to build and deploy them.

## The structure of WFF watch faces

Watch Face Format watch faces are submitted to the Play Store as AABs or APKs just like any other app. While they therefore share many of the common attributes of other apps, such as a need for an`AndroidManifest.xml`file, they have a specific structure.

1. All the content of the watch face is in the resources folder, namely`res/`
2. All the watch face definitions are in`res/raw/`, including`res/raw/watchface.xml`for the simple case and any other XML definitions that represent support for different device sizes.
3. All resources needed by the watch face are in the appropriate resources folder, just as for regular applications, for example:
   1. `/res/font`for fonts
   2. `/res/drawable`for image and animation assets
   3. `/res/values/strings.xml`for any string resources

## Build the watch face using Android Studio

Android Studio provides editor support for Watch Face Format to help you write and debug your XML definitions.
![](https://developer.android.com/static/studio/preview/features/images/declarative-watch-faces-support.gif)Android Studio support for the Watch Face Format.

Specific capabilities include the following:

- Code completion for tags and attributes based on the official Watch Face Format schemas.
- Live validation to identify missing attributes and similar syntax errors.
- Resource linking, which enables quick navigate to drawable resources, data sources, and other elements that are referenced in the XML file.
- A run configuration that lets you see your watch face on a device.

## Build the watch face using Gradle

The easiest way to see the process of how to use Gradle to build the watch face is to take a look at the[samples on GitHub](https://github.com/android/wear-os-samples/tree/main/WatchFaceFormat).

As well as building the watch face, the Gradle scripts in these projects check the watch face XML for validity using the[validator tools](https://developer.android.com/training/wearables/wff/setup#check_your_watch_face_correctness_and_performance).

## Check the watch face prior to submission to Google Play

Once you have created your watch face and familiarized yourself with the build process, perform pre-submission checks on your watch face AAB before submitting to Play.

Play performs very similar checks, so ensuring that you're passing these pre-submission checks saves you considerable time in the submission and review process.

An example of running the pre-submission checks:

These checks no only inspect how much memory the watch face is using, but also identify other issues, such as missing resources, as well as validating the XML.

For details on how to obtain and build the tool, see the[Memory Footprint Evaluator](https://github.com/google/watchface/tree/main/play-validations).