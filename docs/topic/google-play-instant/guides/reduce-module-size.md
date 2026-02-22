---
title: https://developer.android.com/topic/google-play-instant/guides/reduce-module-size
url: https://developer.android.com/topic/google-play-instant/guides/reduce-module-size
source: md.txt
---

**Warning:** Google Play Instant will no longer be available. Starting December 2025, Instant Apps cannot be published through Google Play, and all[Google Play services Instant APIs](https://developers.google.com/android/reference/com/google/android/gms/instantapps/package-summary)will no longer work. Users will no longer be served Instant Apps by Play using any mechanism.

We're making this change based on developer feedback and our continuous investments to improve the ecosystem since the introduction of Google Play Instant.

To continue optimizing for user growth, we encourage developers to refer users to their regular app or game, using[deeplinks](https://support.google.com/googleplay/android-developer/answer/12463044)to redirect them to specific journeys or features when relevant.

Google Play Instant provides rich, native experiences at the tap of a web link. People can experience your app without upfront installation, enabling a higher level and quality of engagement. To make an instant app load as quickly as a typical mobile webpage does, though, you need to create a well-structured, efficient instant app. The smaller your instant app's binary, the faster it loads and the smoother the user experience is.

This document conveys best practices for managing your app's structure and binary size to enable a smooth instant app experience. You can apply these same practices to benefit your installable app, too.

## Refactor into multiple feature modules

The largest improvement to your app's binary size occurs when you refactor the app into multiple feature modules. Start with a[base feature module](https://developer.android.com/topic/google-play-instant/getting-started/create-base-feature-module), then extract thematically-related workflows into their own feature modules. Assign a starting activity and unique URL to each feature module so that users can complete the module's workflow successfully.

As you create feature modules, keep the base feature module as small as possible. In particular, pay close attention to the parts of your app that require access to your dependent libraries. If only one feature module uses a given library, import that library in the feature module itself, not the base feature module. Keep in mind that, in order to release an instant app for a particular feature module, the**total** size of that feature module and the base feature module must be less than15 MB.
| **Note:** If your instant experience contains more methods than the DEX limit of 65,536 methods, you can still[enable multidex](https://developer.android.com/studio/build/multidex)and publish your instant experience, provided that your app satisfies the total size limit.

### Best practices

When refactoring your app, keep the following best practices in mind:

Use the same codebase for both app types
:   You can simplify your app's project management process by using the same modular codebase to create**both**your installed app and your instant apps.

Design for multiple feature modules
:   Even if your app has only one workflow and requires only a single feature module for now, it's still a good idea to design for multiple feature modules. That way, you can add existing modules to your app without affecting the original feature module's size.

Don't focus on the feature module size limit at the beginning
:   Feature module size limits don't apply to locally-built binaries. You can also release an instant app through the**internal test** track, which enforces a15 MBlimit on feature module sizes. Only the**alpha** and**production** tracks enforce the15 MBlimit.

## Update app resources

Some apps, particularly those that have longer codebase histories, contain resources that your app's binaries no longer use. As you look for ways to make your app's modules smaller, consider the following common sources of unneeded code.

### Reduce file size of images

You can significantly reduce the total size of your app's drawables by using the[WebP](https://blog.chromium.org/2010/09/webp-new-image-format-for-web.html)file format instead of PNG. Google Play Instant provides complete support for WebP, including transparency and lossless compression, so image quality remains the same.
| **Note:** The one exception to this rule is your app's launcher icon: it must use the PNG format. This rule has minimal impact on your app's total size, however, because most projects store launcher icons in the`mipmap`directory.

If possible, remove all backward compatibility requirements for using other PNG images. If you must use PNG images, place them in the module that's used to build and install your app.
| **Note:** You can save even more space by converting your app's images to[vector drawables](https://developer.android.com/guide/topics/graphics/vector-drawable-resources). Unlike the conversion from PNG to WebP, however, you need to change your app's code to use vector drawables.

### Remove unused languages

If your app supports multiple languages, reduce as many localized resources as you can. This step is particularly useful to complete if you use an "app compat" library, such as[`android.support.v7.appcompat`](https://developer.android.com/reference/android/support/v7/appcompat/package-summary). This library includes messages in many languages, some of which your app might not support.

To learn more, check out how to[remove unused alternative resources](https://developer.android.com/studio/build/shrink-code#unused-alt-resources), particularly unused languages.

### Remove extra files

Your app might no longer use some of the resources that you've imported into your project. To help remove these resources, Android Studio has a Lint check for this specific situation. To use the tool, complete the following steps:

1. Press**Control+Alt+Shift+I** (**Command+Alt+Shift+I**on Mac OS).
2. In the dialog that appears, type`"unused resources"`.
3. Select the**Unused resources**option to start the resource usage inspection process.

If any large resources remain in your app, consider whether it's possible to unpackage them from your app and download them as standalone files after the user starts interacting with your app. This sort of image-loading deferral usually requires a code change, but it can substantially reduce your instant app's file size by downloading only the resources that a user explicitly requests.

## Remove unused libraries

As an app grows in scope, it can take on a surprising number of dependencies, particularly one of the following types:

- **Native libraries:**Libraries that contain native code that your instant app never runs.
- **Transitive dependencies:**Libraries upon which your app's imported libraries depend.

Android Studio has several useful tools for identifying any extraneous dependencies in your app's project:

External libraries

:   Android Studio's**Project** view includes an**External Libraries**section.

    This section contains every library that your app uses, including native code and all transitive dependencies. In this view, look for unused or dupicate libraries that your app doesn't require.

APK Analyzer

:   You can use the[APK Analyzer](https://developer.android.com/studio/debug/apk-analyzer)tool to compare different builds, including instant app builds.

After you've determined which libraries your app doesn't need, exclude them by adding lines similar to the following to your Gradle build file:

\<feature_module\>/build.gradle  

### Groovy

```groovy
dependencies {
    implementation('some-important-but-large-library') {
        exclude group: 'com.example.imgtools', module: 'native'
    }
}
```

### Kotlin

```kotlin
dependencies {
    implementation('some-important-but-large-library') {
        exclude(group = "com.example.imgtools", module = "native")
    }
}
```

For more information on reducing the total import size of your app's dependencies, see Gradle's guide to[Dependency Management](https://docs.gradle.org/current/userguide/core_dependency_management.html).

## Implement cloud delivery of assets

If you need to shrink the size down further, you might need to rely on[cloud delivery of assets](https://developer.android.com/topic/google-play-instant/getting-started/cloud-delivery-assets).