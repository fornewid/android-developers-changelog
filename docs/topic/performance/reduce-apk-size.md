---
title: https://developer.android.com/topic/performance/reduce-apk-size
url: https://developer.android.com/topic/performance/reduce-apk-size
source: md.txt
---

Users often avoid downloading apps that seem too large, particularly in emerging markets where
devices connect to spotty 2G and 3G networks or work on plans with data limits. This page describes
how to reduce your app's download size, which lets more users download your app.

## Upload your app with Android App Bundles

Upload your app as an [*Android App Bundle*](https://developer.android.com/guide/app-bundle) to immediately
save app size when you publish to Google Play. Android App Bundle is an upload format that includes
all your app's compiled code and resources but defers APK generation and signing to Google Play.

Google Play's app serving model then uses your app bundle to generate and serve optimized APKs
for each user's device configuration so that they download only the code and resources they need to
run your app. You don't have to build, sign, and manage multiple APKs to support different devices,
and users get smaller, more optimized downloads.

Google Play enforces a [compressed download
size restriction](https://developer.android.com/guide/app-bundle#size_restrictions) of 200 MB for apps published with app bundles. Larger sizes
are possible using Play Feature Delivery and Play Asset Delivery but increasing your app's size can
negatively impact install success and increase uninstalls, so we recommend you apply the
guidelines described in this page to reduce your app's download size as much as possible.
| **Note:** For apps you publish to Google Play by uploading signed APKs, **compressed downloads
| are restricted to 100 MB**.

## Understand the APK structure

Before reducing the size of your app, it's helpful to understand the structure of an app's APK.
An APK file consists of a ZIP archive that contains all the files that comprise your app. These
files include Java class files, resource files, and a file containing compiled resources.

An APK contains the following directories:

- `META-INF/`: contains the `CERT.SF` and `CERT.RSA` signature files, as well as the `MANIFEST.MF` manifest file.
- `assets/`: contains the app's assets, which the app can retrieve using an [AssetManager](https://developer.android.com/reference/android/content/res/AssetManager) object.
- `res/`: contains resources that aren't compiled into `resources.arsc`.
- `lib/`: contains the compiled code that is specific to the software layer of a processor. This directory contains a subdirectory for each platform type, such as `armeabi`, `armeabi-v7a`, `arm64-v8a`, `x86`, `x86_64`, and `mips`.

An APK also contains the following files. Only `AndroidManifest.xml` is mandatory:

- `resources.arsc`: contains compiled resources. This file contains the XML content from all configurations of the `res/values/` folder. The packaging tool extracts this XML content, compiles it to binary form, and archives the content. This content includes language strings and styles, as well as paths to content that isn't included directly in the `resources.arsc` file, such as layout files and images. **Note:** Don't compress this file in your APK.
- `classes.dex`: contains the classes compiled in the DEX file format understood by the Dalvik or ART virtual machine.
- `AndroidManifest.xml`: contains the core Android manifest file. This file lists the name, version, access rights, and referenced library files of the app. The file uses Android's binary XML format.

## Reduce resource count and size

The size of your APK has an impact on how fast your app loads, how much memory it uses, and how
much power it consumes. You can make your APK smaller by reducing the number and size of the
resources it contains. In particular, you can remove resources that your app no longer uses, and you
can use scalable
[Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable) objects in
place of image files. This section discusses these methods and other ways you can reduce the
resources in your app to decrease the overall size of your APK.

### Remove unused resources

The [`lint`](https://developer.android.com/studio/write/lint) tool---a static code analyzer
included in Android Studio---detects resources in your `res/` folder that your code
doesn't reference. When the `lint` tool discovers a potentially unused resource in your
project, it prints a message like the following example:  

```
res/layout/preferences.xml: Warning: The resource R.layout.preferences appears
    to be unused [UnusedResources]
```
| **Note:** The `lint` tool doesn't scan the `assets/` folder, assets that are referenced via reflection, or library files that you link to your app. Also, it doesn't remove resources. It only alerts you to their presence.

Libraries that you add to your code might include unused resources. Gradle can automatically
remove resources on your behalf if you enable
[`shrinkResources`](https://developer.android.com/studio/build/shrink-code#shrink-resources) in your
app's `build.gradle.kts` file.  

### Kotlin

```kotlin
android {
    // Other settings.

    buildTypes {
        getByName("release") {
            minifyEnabled = true
            shrinkResources = true
            proguardFiles(getDefaultProguardFile('proguard-android.txt'), "proguard-rules.pro")
        }
    }
}
```

### Groovy

```groovy
android {
    // Other settings.

    buildTypes {
        release {
            minifyEnabled true
            shrinkResources true
            proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'
        }
    }
}
```

To use `shrinkResources`, enable code shrinking. During the build process, R8 first
removes unused code. Then, the Android Gradle plugin removes the unused resources.

For more information about code and resource shrinking, and other ways Android Studio reduces
APK size, see [Shrink, obfuscate, and optimize your app](https://developer.android.com/studio/build/shrink-code).

In Android Gradle Plugin 7.0 and later, you can declare the configurations that your app
supports. Gradle passes this information to the build system using the
[resourceConfigurations](https://developer.android.com/reference/tools/gradle-api/7.2/com/android/build/api/dsl/BaseFlavor#resourceConfigurations())
flavor and the `defaultConfig` option. The build system then prevents resources from
other unsupported configurations from appearing in the APK, reducing the APK's size. For more
information about this feature, see
[Remove unused alternative
resources](https://developer.android.com/studio/build/shrink-code#unused-alt-resources).

### Minimize resource use from libraries

When you develop an Android app, you usually use external libraries to improve your app's
usability and versatility. For example, you might reference [AndroidX](https://developer.android.com/jetpack/androidx)
to improve the user experience on earlier devices, or you can use
[Google Play Services](https://developers.google.com/android/guides/overview) to retrieve
automatic translations for text within your app.

If a library is designed for a server or desktop, it can include many objects and methods that
your app doesn't need. To include only the parts of the library that your app needs, you can edit
the library's files if the license lets you modify the library. You can also use an alternative,
mobile-friendly library to add specific functionality to your app.
| **Note:** You can use [code shrinking](https://developer.android.com/studio/build/shrink-code) to clean up some of a library's unnecessary code, but it might not remove some large internal dependencies.

### Native animated image decoding

In Android 12 (API level 31), the NDK
[ImageDecoder](https://developer.android.com/ndk/reference/group/image-decoder) API is expanded to decode
all frames and timing data from images that use the animated GIF and animated WebP file formats.

Use `ImageDecoder` instead of third-party libraries to further
[decrease APK size](https://developer.android.com/topic/performance/reduce-apk-size#minimize) and benefit from future
updates related to security and performance.

For more details about the `ImageDecoder` API, refer to the
[API reference](https://developer.android.com/ndk/reference/group/image-decoder) and the
[sample
on GitHub](https://github.com/android/ndk-samples/tree/develop/webp/image-decoder).

### Support only specific densities

Android supports different screen densities, such as the following:

- `ldpi`
- `mdpi`
- `tvdpi`
- `hdpi`
- `xhdpi`
- `xxhdpi`
- `xxxhdpi`

Although Android supports the preceding densities, you don't need to export your rasterized
assets to each density.

If you know that only a small percentage of your users have devices with specific densities,
consider whether you need to bundle those densities into your app. If you don't include resources
for a specific screen density, Android automatically scales existing resources originally designed
for other screen densities.

If your app needs only scaled images, you can save even more space by having a single variant of
an image in `drawable-nodpi/`. We recommend you include at least an `xxhdpi`
image variant in your app.

For more information about screen densities, see
[Screen sizes and densities](https://developer.android.com/about/dashboards#Screens).

### Use drawable objects

Some images don't require a static image resource. The framework can dynamically draw the image
at runtime instead. `Drawable` objects---or `<shape>` in
XML---can take up a tiny amount of space in your APK. In addition, XML `Drawable`
objects produce monochromatic images compliant with Material Design guidelines.

### Reuse resources

You can include a separate resource for variations of an image, such as tinted, shaded, or
rotated versions of the same image. However, we recommend that you reuse the same set of resources
and customizing them as needed at runtime.

Android provides several utilities to change the color of an asset, either using the
`android:tint` and `tintMode` attributes.

You can also omit resources that are only a rotated equivalent of another resource. The following
code snippet provides an example of turning a "thumb up" into a "thumb down" by pivoting at the
middle of the image and rotating it 180 degrees:  

```xml
<?xml version="1.0" encoding="utf-8"?>
<rotate xmlns:android="http://schemas.android.com/apk/res/android"
    android:drawable="@drawable/ic_thumb_up"
    android:pivotX="50%"
    android:pivotY="50%"
    android:fromDegrees="180" />
```

### Render from code

You can also reduce your APK size by procedurally rendering your images. Procedural rendering
frees up space because you no longer store an image file in your APK.

### Crunch PNG files

The `aapt` tool can optimize the image resources placed in `res/drawable/`
with lossless compression during the build process. For example, the `aapt` tool can
convert a true-color PNG that doesn't require more than 256 colors to an 8-bit PNG with a color
palette. Doing so results in an image of equal quality but a smaller memory footprint.

The `aapt` has the following limitations:

- The `aapt` tool doesn't shrink PNG files contained in the `asset/` folder.
- Image files need to use 256 or fewer colors for the `aapt` tool to optimize them.
- The `aapt` tool might inflate PNG files that are already compressed. To prevent this, you can use the `isCrunchPngs` flag to disable this process for PNG files:  

### Kotlin

```kotlin
    buildTypes.all { isCrunchPngs = false }
    
```

### Groovy

```groovy
    buildTypes.all { isCrunchPngs = false }
    
```

### Compress PNG and JPEG files

You can reduce PNG file sizes without losing image quality using tools like
[pngcrush](http://pmt.sourceforge.net/pngcrush/),
[pngquant](https://pngquant.org/), or
[zopflipng](https://github.com/google/zopfli). All of these tools
can reduce PNG file size while preserving the perceptive image quality.

The `pngcrush` tool is particularly effective. This tool iterates over PNG filters and
zlib (Deflate) parameters, using each combination of filters and parameters to compress the image.
It then chooses the configuration that yields the smallest compressed output.

To compress JPEG files, you can use tools like [packJPG](https://github.com/packjpg/packJPG) and [guetzli](https://github.com/google/guetzli).

### Use WebP file format

Instead of using PNG or JPEG files, you can also use the
[WebP](https://developers.google.com/speed/webp/) file format for your images. The WebP
format provides lossy compression and transparency, like JPG and PNG, and it can provide better
compression than either JPEG or PNG.

You can convert existing BMP, JPG, PNG or static GIF images to WebP format using Android Studio.
For more information, see [Create WebP images](https://developer.android.com/studio/write/convert-webp).

### Use vector graphics

You can use vector graphics to create resolution-independent icons and other scalable media.
You can use these graphics to greatly reduce your APK footprint. Vector images are represented in
Android as
[VectorDrawable](https://developer.android.com/reference/android/graphics/drawable/VectorDrawable)
objects. With a `VectorDrawable` object, a 100-byte file can generate a sharp image the
size of the screen.

However, it takes significantly more time for the system to render each
`VectorDrawable` object, and larger images take even longer to appear on the screen.
Therefore, consider using these vector graphics only when displaying small images.

For more information about working with `VectorDrawable` objects, see
[Drawables](https://developer.android.com/training/material/drawables).

### Use vector graphics for animated images

Don't use
[AnimationDrawable](https://developer.android.com/reference/android/graphics/drawable/AnimationDrawable)
to create frame-by-frame animations, because doing so requires that you include a separate bitmap
file for each frame of the animation, which drastically increases the size of your APK.

Instead, use
[`AnimatedVectorDrawableCompat`](https://developer.android.com/reference/androidx/vectordrawable/graphics/drawable/AnimatedVectorDrawableCompat) to create
[animated vector
drawables](https://developer.android.com/develop/ui/views/animations/drawable-animation#AnimVector).

## Reduce native and Java code

You can use the following methods to reduce the size of the Java and native codebase in your
app.

### Remove unnecessary generated code

Make sure to understand the footprint of any code which is automatically generated. For example,
many protocol buffer tools generate an excessive number of methods and classes, which can double or
triple the size of your app.

### Avoid enumerations

A single enum can add about 1.0 to 1.4 KB to your app's `classes.dex` file. These
additions can quickly accumulate for complex systems or shared libraries. If possible, consider
using the `@IntDef` annotation and [code shrinking](https://developer.android.com/studio/build/shrink-code)
to strip enumerations out and convert them to integers. This type conversion preserves all of the
type safety benefits of enums.

### Reduce the size of native binaries

If your app uses native code and the Android NDK, you can also reduce the size of the release
version of your app by optimizing your code. Two useful techniques are removing debug symbols and
not extracting native libraries.

#### Remove debug symbols

Using debug symbols makes sense if your app is in development and still requires debugging. Use
the `arm-eabi-strip` tool provided in the Android NDK to remove unnecessary debug
symbols from native libraries. Afterwards, you can compile your release build.

#### Avoid extracting native libraries

When building the release version of your app, package uncompressed `.so` files in the
APK by setting
[`useLegacyPackaging`](https://developer.android.com/reference/tools/gradle-api/7.1/com/android/build/api/dsl/JniLibsPackagingOptions#uselegacypackaging)
to `false` in your app's `build.gradle.kts` file. Disabling this flag prevents
[PackageManager](https://developer.android.com/reference/android/content/pm/PackageManager) from
copying `.so` files from the APK to the filesystem during installation. This method makes
updates of your app smaller.

## Maintain multiple lean APKs

Your APK might contain content that users download but never use, like additional language or
per-screen-density resources. To help ensure a minimal download for your users, upload your app to
Google Play [using Android App Bundles](https://developer.android.com/topic/performance/reduce-apk-size#app_bundle). Uploading app bundles lets Google
Play generate and serve optimized APKs for each user's device configuration so they download only
the code and resources they need to run your app. You don't have to build, sign, and manage multiple
APKs to support different devices, and users get smaller, more optimized downloads.

If you're not publishing your app to Google Play, you can segment your app into several APKs,
differentiated by factors such as screen size or GPU texture support.

When a user downloads your app, their device receives the correct APK based on the device's
features and settings. This way, devices don't receive assets for features that the devices don't
have. For example, if a user has a `hdpi` device, they don't need `xxxhdpi`
resources that you might include for devices with higher density displays.

For more information, see [Build multiple
APKs](https://developer.android.com/studio/build/configure-apk-splits) and [Multiple APK support](https://developer.android.com/training/multiple-apks).