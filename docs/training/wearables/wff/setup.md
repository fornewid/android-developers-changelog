---
title: https://developer.android.com/training/wearables/wff/setup
url: https://developer.android.com/training/wearables/wff/setup
source: md.txt
---

**Note** : This page shows you a step of the process for manually managing your
watch face configuration. If you want to design your watch face using a WYSIWYG
(what you see is what you get) style tool instead, check out the [Watch Face
Studio](https://developer.samsung.com/watch-face-studio/user-guide/index.html) guides first.

This guide includes steps on the tools that you need to configure a watch face
using the Watch Face Format, some suggestions on project structure, and a
step-by-step guide to applying the tools to create that structure.

## Get started with Android Studio

The easiest way to get started with manually developing watch faces is to use
[Android Studio](https://developer.android.com/studio). Watch face support is available in the canary channel.

1. Click *File \> New Project*
2. Under *Wear OS* , select *Basic watch face*

This creates the necessary structure for a fully-functioning watch face.

## Project structure

When you create a custom watch face that uses the Watch Face Format, the Android
App Bundle that includes the custom watch face file must be completely separate
from the Android App Bundle that contains your Wear OS app's logic. Some app
stores, including Google Play, prevent you from uploading an Android App Bundle
that includes both Wear OS logic and a custom watch face.

### Declare Watch Face Format version

In your new app's manifest file (`AndroidManifest.xml`), inspect the application
property that indicates your use of the Watch Face Format.

<br />

```xml
<property
    android:name="com.google.wear.watchface.format.version"
    android:value="4" />
```

<br />

Some features of Watch Face Format are only available in later versions. Set
this property to the lowest value that supports the features you need, to
maximize device compatibility, and also set the `minSdkVersion` to match. Learn
more about how to configure [versions](https://developer.android.com/build/configure-apk-splits) of your app.

The `<application>` element must also include the attribute
`android:hasCode="false"`. Watch Face Format bundles are resource-only and
cannot contain any code.

### Declare watch face metadata

In your app's `res/xml` resources directory, there's a file called
`watch_face_info.xml`. This is where you define your watch face's metadata:

<br />

```xml
<WatchFaceInfo>
    <Preview value="@drawable/preview" />
    <Category value="CATEGORY_EMPTY" />
    <AvailableInRetail value="true" />
    <MultipleInstancesAllowed value="true" />
    <Editable value="true" />
    <FlavorsSupported value="true" />
</WatchFaceInfo>
```

<br />

The fields in this file represent the following details:

`Preview`
:   References the drawable that contains a preview image of the watch face.

`Category`

:   Defines the watch face's category. Must be a string or a reference to a
    string, such as `@string/ref_name`. Each device manufacturer can define its own
    set of watch face categories.

    Default value: `empty_category_meta`, which groups this watch face together
    with other "empty category" watch faces at the bottom of the watch face
    picker view.

`AvailableInRetail`

:   Whether the watch face is available in the device's [retail demo
    mode](https://source.android.com/docs/core/display/retail-mode). Must be a boolean value or a reference to a boolean value
    such as `@bool/watch_face_available_in_retail`.

    Default value: `false`

`MultipleInstancesAllowed`

:   Whether the watch face can have multiple favorites. Must be a boolean value,
    or a reference to a boolean value such as
    `@bool/watch_face_multiple_instances_allowed`.

    Default value: `false`

`Editable`

:   Whether the watch face is *editable* , which means that the watch face has a
    setting or at least one non-fixed [complication](https://developer.android.com/training/wearables/tiles/complications). This is used to show or
    hide the **Edit** button for the watch face in the favorites list.

    Default value: false

### Declare watch face name

In your app's manifest file (`AndroidManifest.xml`), set the `android:label`
attribute on the `application` element to the name of your watch face.

### Declare watch face details

The structure of a basic WFF watch face document is as follows:

<br />

```xml
<WatchFace width="450" height="450">
    <Scene>
        <!-- Content to be rendered -->
    </Scene>
</WatchFace>
```

<br />

The Android Studio template provides a basic document in
`res/raw/watchface.xml`. To support different screen shapes and sizes,
[declare support for multiple shapes and sizes](https://developer.android.com/training/wearables/wff/setup#declare-shape-support).

The root element is always [`WatchFace`](https://developer.android.com/training/wearables/wff/watch-face). The `height` and `width` define the
extent of the coordinate space for use in your watch face, and the watch face
is scaled to fit the device it is being used on; `height` and `width` don't
represent actual pixels.

The Watch Face Format organizes several details about your watch face:

- *Metadata*, such as the time and step count that's shown in your watch face's preview image.
- *User configurations* , such as different color themes for your watch face, user-toggleable elements, and a choice among several elements. Watch Face Format version 2 introduces *flavors*, which can appear within a user configuration. Each flavor specifies a preset user configuration, specifying the type and style of elements that appear with the time in your watch face. These presets make it easier for you to create groups of elements that are visually pleasing. In the Wear OS companion app, users see your watch face's different flavors along a scrollable row.
- A *scene* which contains the visual elements of a watch face. Elements that appear closer to the end of the scene appear on top of other elements, so the typical order is as follows:
  - The hands for an analog clock or the text for a digital clock
  - Complications that show additional information, such as the day of the week or a user's step count
  - Other graphics that provide visual interest or decorations for the watch face, such as an image of a campsite
- *Groups* of elements, which let you modify multiple elements at the same time. You can create *variants* of these groups within a scene, which lets you selectively hide or modify content when the system enters a power-saving ambient mode.

Attributes are strongly typed and have guidelines around frequency and valid
values to avoid most sources of errors when creating a watch face.

> [!NOTE]
> **Note:** As you configure your watch face, [optimize its memory usage](https://developer.android.com/training/wearables/wff/memory-usage).

### Declare support for watch face shapes (optional)

This step is only necessary if you want to support different behavior for
different sizes of watch faces. You can skip this step if you are happy for your
watch face to scale with the size of the watch.

In your app's `res/xml` resources directory, declare the set of watch face
shapes that you support in `watch_face_shapes.xml`:

<br />

```xml
<WatchFaces>
    <WatchFace shape="CIRCLE" width="300" height="300"
        file="@raw/watchface_basic"/>
    <WatchFace shape="CIRCLE" width="450" height="450"
        file="@raw/watchface"/>
</WatchFaces>
```

<br />

Then, define your watch face appearance and behavior for each watch face shape.
If you did not define a shapes file, then you only need one file,
`watchface.xml`.

Using the example from this section, the raw XML files would be:

- `res/raw/watchface.xml`
- `res/raw/watchface_basic.xml`

### Identify watch face publisher (optional)

Optionally, in your app's manifest file, declare an arbitrary string that you
can use to identify the publisher of the watch face, or the tool name and
version that you're using:

<br />

```xml
<property
    android:name="com.google.wear.watchface.format.publisher"
    android:value="{toolName}-{toolVersion}" />
```

<br />

## Check your watch face correctness and performance

During development, and before uploading to Google Play, check that your watch
face is free from syntax errors by using the in-built Watch Face Format
validation in Android Studio. This automatically highlights errors in your code
and is version-aware.

You should also check that your watch face meets the memory usage requirements
by running the [memory footprint](https://github.com/google/watchface) tool.

- Learn more about [optimizing memory usage](https://developer.android.com/training/wearables/wff/memory-usage) and [checking memory usage](https://github.com/google/watchface/tree/main/play-validations) in preparation for publishing.
- Learn more about using the [XML validator](https://github.com/google/watchface/tree/main/third_party/wff) as part of your development cycle.

## Build your watch face app bundle

The easiest way to build and deploy your watch face is through Android Studio,
which has in-built support for watch face run configurations. After you click
the *Run* button, Android Studio deploys the watch face to the device or
emulator and sets it as the active watch face.

## Sample watch faces

Further samples of Watch Face Format projects are [available on GitHub](https://github.com/android/wear-os-samples/tree/main/WatchFaceFormat).

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [AAPT2](https://developer.android.com/tools/aapt2)
- [Jetpack Compose basics](https://developer.android.com/codelabs/jetpack-compose-basics)
- [Getting Started with CameraX](https://developer.android.com/codelabs/camerax-getting-started)