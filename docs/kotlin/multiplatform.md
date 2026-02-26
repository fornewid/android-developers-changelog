---
title: https://developer.android.com/kotlin/multiplatform
url: https://developer.android.com/kotlin/multiplatform
source: md.txt
---

![](http://developer.android.com/static/images/picto-icons/kmp.svg)

### Kotlin Multiplatform

Write a single codebase that runs on multiple platforms with Kotlin Multiplatform.

[Kotlin Multiplatform (KMP)](https://kotlinlang.org/multiplatform/) is officially supported by Google for sharing business logic between Android and iOS. Kotlin Multiplatform is [stable and production-ready](https://kotlinlang.org/docs/multiplatform/supported-platforms.html#current-platform-stability-levels-for-the-core-kotlin-multiplatform-technology).
With JetBrains' [Compose Multiplatform (CMP)](https://www.jetbrains.com/compose-multiplatform/), developers can also share UI across platforms.
[![](http://developer.android.com/static/images/cluster-illustrations/play-webinar-16-9.svg)](http://developer.android.com/courses/pathways/kotlin-multiplatform) Pathway

### [Basics of Kotlin Multiplatform](http://developer.android.com/courses/pathways/kotlin-multiplatform)

Start your journey into multi-platform development today. This pathway will guide you through the essentials of Kotlin Multiplatform, from setting up your project, sharing code, and using platform-specific APIs, to migrating the Room Database to Kotlin Multiplatform. [Learn \& earn a badge](http://developer.android.com/courses/pathways/kotlin-multiplatform) [![](http://developer.android.com/static/images/cluster-illustrations/android-development-kit-16-9.svg)](https://plugins.jetbrains.com/plugin/14936-kotlin-multiplatform) Android Studio Plugin

### [Kotlin Multiplatform Plugin](https://plugins.jetbrains.com/plugin/14936-kotlin-multiplatform)

We recommend installing the Kotlin Multiplatform Android Studio Plugin developed by JetBrains to improve the development experience within Android Studio.

- **New project wizard**: Create a new multiplatform project within the IDE.
- **Preflight checks**: Preflight checks help you configure your environment.
- **Run configurations**: Run, debug, and test applications on both iOS and Android directly from the IDE.
- **Basic Swift support in the IDE**: Get basic Swift support in the IDE, including cross-language debugging tools, navigation, and quick documentation.
[Go to JetBrains Marketplace](https://plugins.jetbrains.com/plugin/14936-kotlin-multiplatform)

## Benefits of Kotlin Multiplatform

With Kotlin Multiplatform, you can choose what to share across platforms, from just core business logic to the entire application. The following are some of its key benefits:

### Deduplicate code

Your complex business logic doesn't have to be duplicated on each platform.

### No complete rewrite

With Kotlin Multiplatform, you don't need to rewrite your whole application to start sharing code between platforms.

### Native performance

Kotlin Multiplatform compiles into the native way the target platform runs code, delivering performance on par with native implementations.

## Kotlin Multiplatform and Jetpack libraries

Many of our Jetpack libraries have already been migrated to be KMP-ready. The following Jetpack libraries provide KMP support:


![Android logo](https://developer.android.com/static/images/logos/android.svg)
**Built by Android**

![JetBrains logo](https://developer.android.com/static/images/logos/jetbrains.svg)
**Built by JetBrains**


**Not supported**

| Library | Latest Release | Android | iOS | JVM | Web |
|---|---|---|---|---|---|
| [annotation](https://developer.android.com/jetpack/androidx/releases/annotation) | February 11, 2026 - [1.9.1](https://developer.android.com/jetpack/androidx/releases/annotation#1.9.1) | ![](https://developer.android.com/static/images/logos/android.svg) | ![](https://developer.android.com/static/images/logos/android.svg) | ![](https://developer.android.com/static/images/logos/android.svg) | ![](https://developer.android.com/static/images/logos/android.svg) |
| [collection](https://developer.android.com/jetpack/androidx/releases/collection) | February 11, 2026 - [1.5.0](https://developer.android.com/jetpack/androidx/releases/collection#1.5.0) - [1.6.0-rc01](https://developer.android.com/jetpack/androidx/releases/collection#1.6.0-rc01) | ![](https://developer.android.com/static/images/logos/android.svg) | ![](https://developer.android.com/static/images/logos/android.svg) | ![](https://developer.android.com/static/images/logos/android.svg) | ![](https://developer.android.com/static/images/logos/android.svg) |
| [compose](https://developer.android.com/jetpack/androidx/releases/compose-runtime) | February 25, 2026 - [1.10.4](https://developer.android.com/jetpack/androidx/releases/compose-runtime#1.10.4) - [1.11.0-alpha06](https://developer.android.com/jetpack/androidx/releases/compose-runtime#1.11.0-alpha06) | ![](https://developer.android.com/static/images/logos/android.svg) | ![](https://developer.android.com/static/images/logos/jetbrains.svg) | ![](https://developer.android.com/static/images/logos/jetbrains.svg) | ![](https://developer.android.com/static/images/logos/jetbrains.svg) |
| [datastore](https://developer.android.com/jetpack/androidx/releases/datastore) <br /> <br /> [Documentation](https://developer.android.com/kotlin/multiplatform/datastore) | February 25, 2026 - [1.2.0](https://developer.android.com/jetpack/androidx/releases/datastore#1.2.0) - [1.3.0-alpha06](https://developer.android.com/jetpack/androidx/releases/datastore#1.3.0-alpha06) | ![](https://developer.android.com/static/images/logos/android.svg) | ![](https://developer.android.com/static/images/logos/android.svg) | ![](https://developer.android.com/static/images/logos/android.svg) | ![](https://developer.android.com/static/images/logos/android.svg) |
| [lifecycle](https://developer.android.com/jetpack/androidx/releases/lifecycle) <br /> <br /> [Documentation](https://kotlinlang.org/docs/multiplatform/compose-lifecycle.html) | February 25, 2026 - [2.10.0](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.10.0) - [2.11.0-alpha01](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.11.0-alpha01) | ![](https://developer.android.com/static/images/logos/android.svg) | ![](https://developer.android.com/static/images/logos/android.svg) | ![](https://developer.android.com/static/images/logos/android.svg) | ![](https://developer.android.com/static/images/logos/android.svg) |
| [viewModel](https://developer.android.com/jetpack/androidx/releases/lifecycle) <br /> <br /> [Documentation](https://developer.android.com/kotlin/multiplatform/viewmodel) | February 25, 2026 - [2.10.0](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.10.0) - [2.11.0-alpha01](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.11.0-alpha01) | ![](https://developer.android.com/static/images/logos/android.svg) | ![](https://developer.android.com/static/images/logos/android.svg) | ![](https://developer.android.com/static/images/logos/android.svg) | ![](https://developer.android.com/static/images/logos/android.svg) |
| [viewModel-compose](https://developer.android.com/jetpack/androidx/releases/lifecycle) <br /> <br /> [Documentation](https://kotlinlang.org/docs/multiplatform/compose-viewmodel.html) | February 25, 2026 - [2.10.0](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.10.0) - [2.11.0-alpha01](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.11.0-alpha01) | ![](https://developer.android.com/static/images/logos/android.svg) | ![](https://developer.android.com/static/images/logos/jetbrains.svg) | ![](https://developer.android.com/static/images/logos/jetbrains.svg) | ![](https://developer.android.com/static/images/logos/jetbrains.svg) |
| [navigation](https://developer.android.com/jetpack/androidx/releases/navigation) <br /> <br /> [Documentation](https://kotlinlang.org/docs/multiplatform/compose-navigation.html) | January 28, 2026 - [2.9.7](https://developer.android.com/jetpack/androidx/releases/navigation#2.9.7) | ![](https://developer.android.com/static/images/logos/android.svg) | ![](https://developer.android.com/static/images/logos/jetbrains.svg) | ![](https://developer.android.com/static/images/logos/jetbrains.svg) | ![](https://developer.android.com/static/images/logos/jetbrains.svg) |
| [navigation3](https://developer.android.com/jetpack/androidx/releases/navigation3) | February 25, 2026 - [1.0.1](https://developer.android.com/jetpack/androidx/releases/navigation3#1.0.1) - [1.1.0-alpha05](https://developer.android.com/jetpack/androidx/releases/navigation3#1.1.0-alpha05) | ![](https://developer.android.com/static/images/logos/android.svg) | ![](https://developer.android.com/static/images/logos/jetbrains.svg) | ![](https://developer.android.com/static/images/logos/jetbrains.svg) | ![](https://developer.android.com/static/images/logos/jetbrains.svg) |
| [navigationevent](https://developer.android.com/jetpack/androidx/releases/navigationevent) | February 25, 2026 - [1.0.2](https://developer.android.com/jetpack/androidx/releases/navigationevent#1.0.2) - [1.1.0-alpha01](https://developer.android.com/jetpack/androidx/releases/navigationevent#1.1.0-alpha01) | ![](https://developer.android.com/static/images/logos/android.svg) | ![](https://developer.android.com/static/images/logos/jetbrains.svg) | ![](https://developer.android.com/static/images/logos/jetbrains.svg) | ![](https://developer.android.com/static/images/logos/jetbrains.svg) |
| [paging](https://developer.android.com/jetpack/androidx/releases/paging) | February 11, 2026 - [3.4.1](https://developer.android.com/jetpack/androidx/releases/paging#3.4.1) | ![](https://developer.android.com/static/images/logos/android.svg) | ![](https://developer.android.com/static/images/logos/android.svg) | ![](https://developer.android.com/static/images/logos/android.svg) | ![](https://developer.android.com/static/images/logos/android.svg) |
| [room](https://developer.android.com/jetpack/androidx/releases/room) <br /> <br /> [Documentation](https://developer.android.com/kotlin/multiplatform/room) | November 19, 2025 - [2.8.4](https://developer.android.com/jetpack/androidx/releases/room#2.8.4) | ![](https://developer.android.com/static/images/logos/android.svg) | ![](https://developer.android.com/static/images/logos/android.svg) | ![](https://developer.android.com/static/images/logos/android.svg) |   |
| [savedstate](https://developer.android.com/jetpack/androidx/releases/savedstate) | November 5, 2025 - [1.4.0](https://developer.android.com/jetpack/androidx/releases/savedstate#1.4.0) | ![](https://developer.android.com/static/images/logos/android.svg) | ![](https://developer.android.com/static/images/logos/android.svg) | ![](https://developer.android.com/static/images/logos/android.svg) | ![](https://developer.android.com/static/images/logos/android.svg) |
| [sqlite](https://developer.android.com/jetpack/androidx/releases/sqlite) <br /> <br /> [Documentation](https://developer.android.com/kotlin/multiplatform/sqlite) | November 19, 2025 - [2.6.2](https://developer.android.com/jetpack/androidx/releases/sqlite#2.6.2) | ![](https://developer.android.com/static/images/logos/android.svg) | ![](https://developer.android.com/static/images/logos/android.svg) | ![](https://developer.android.com/static/images/logos/android.svg) | ![](https://developer.android.com/static/images/logos/android.svg) |

If you have feedback on these libraries, share it through the [issue tracker](https://issuetracker.google.com/issues/new?component=1337890&template=1803002).

Libraries published by JetBrains wrap Android artifacts together with artifacts for other platforms so you can seamlessly consume any and all of them in your multiplatform projects. To learn about the underlying publishing process, see [How multiplatform Jetpack libraries are packaged](https://kotlinlang.org/docs/multiplatform/compose-multiplatform-jetpack-libraries.html).

## Tools support

You can open, edit, and run multiplatform projects in Android Studio.

### [KMP module wizard](http://developer.android.com/kotlin/multiplatform/migrate)

You can start migrating to KMP by creating a KMP shared module within Android Studio. This module automatically applies all the necessary plugins, including the Android-KMP plugin, to start developing Android and iOS apps. [Add KMP to your project](http://developer.android.com/kotlin/multiplatform/migrate)

### [Live Edit for JetBrains' Compose Multiplatform](http://developer.android.com/develop/ui/compose/tooling/iterative-development)

Live Edit works when building on Android Devices editing any code within the project, not just in `androidMain`. [Learn more](http://developer.android.com/develop/ui/compose/tooling/iterative-development)

### [Previews for JetBrains' Compose Multiplatform](http://developer.android.com/develop/ui/compose/tooling/previews)

Previews for Jetpack Compose are also available for JetBrains' Compose Multiplatform from the `commonMain` source set. [Learn more](http://developer.android.com/develop/ui/compose/tooling/previews)

## Apps built with Kotlin Multiplatform

Many apps are already successfully using Kotlin Multiplatform. ![](http://developer.android.com/static/images/kotlin/kmp-apps/blinkit.png) Blinkit ![](http://developer.android.com/static/images/kotlin/kmp-apps/cash-app.svg) Cash App ![](http://developer.android.com/static/images/kotlin/kmp-apps/duolingo.svg) Duolingo ![](http://developer.android.com/static/images/kotlin/kmp-apps/forbes.png) Forbes ![](http://developer.android.com/static/images/kotlin/kmp-apps/google-docs.svg) Google Docs ![](http://developer.android.com/static/images/kotlin/kmp-apps/jiohotstar.png) JioHotstar ![](http://developer.android.com/static/images/kotlin/kmp-apps/stone.svg) Stone ![](http://developer.android.com/static/images/kotlin/kmp-apps/swiggy.svg) Swiggy ![](http://developer.android.com/static/images/kotlin/kmp-apps/ultrahuman.svg) Ultrahuman ![](http://developer.android.com/static/images/kotlin/kmp-apps/wrike.svg) Wrike ![](http://developer.android.com/static/images/kotlin/kmp-apps/zomato.png) Zomato

## Supported platforms in Jetpack

Jetpack library releases for officially supported platforms---Android and iOS---maintain the same quality and compatibility requirements. However, as we work to expand Jetpack's Kotlin Multiplatform support to other platforms, the tooling and infrastructure support may be a work in progress.

### Tier 1

Code is fully tested in CI; including both host-side and on-device tests. We're tracking source and binary compatibility in accordance with our [semantic versioning policies](https://developer.android.com/jetpack/androidx/versions).

- **Android**
- **JVM**
- **iOS**

### Tier 2

Code is partially tested on CI; limited to host-side tests. We don't track source or binary compatibility.

- **macOS**
- **Linux**

### Tier 3

Code is untested on CI. No source or binary compatibility tracking.

- **watchOS**
- **tvOS**
- **Windows**
- **JavaScript**
- **WASM**

## Additional resources

For further information about the overall multiplatform ecosystem and more advanced configurations, see the official [Kotlin Multiplatform documentation](https://kotlinlang.org/docs/multiplatform-intro.html). [![](http://developer.android.com/static/images/picto-icons/layout.svg)](https://github.com/android/kotlin-multiplatform-samples)

### [Kotlin Multiplatform samples](https://github.com/android/kotlin-multiplatform-samples)

A set of Kotlin Multiplatform samples that demonstrate how to use the Jetpack libraries for Android and iOS. [Sample](https://github.com/android/kotlin-multiplatform-samples) [![](http://developer.android.com/static/images/picto-icons/theming.svg)](http://developer.android.com/codelabs/kmp-get-started)

### [Get started with Kotlin Multiplatform](http://developer.android.com/codelabs/kmp-get-started)

Guided onboarding on how to add KMP to your project. [Codelab](http://developer.android.com/codelabs/kmp-get-started) [![](http://developer.android.com/static/images/picto-icons/graph-line.svg)](http://developer.android.com/codelabs/kmp-migrate-room)

### [Migrate Room to Kotlin Multiplatform](http://developer.android.com/codelabs/kmp-migrate-room)

Guided migration of Android-only Room to KMP. [Codelab](http://developer.android.com/codelabs/kmp-migrate-room) [![](http://developer.android.com/static/images/picto-icons/kmp.svg)](https://kotlinlang.org/docs/multiplatform/get-started.html)

### [In-depth Guidance](https://kotlinlang.org/docs/multiplatform/get-started.html)

More in-depth guidance is available in Kotlin Multiplatform documentation hub on Kotlinlang.org. [Documentation](https://kotlinlang.org/docs/multiplatform/get-started.html) [Video](https://www.youtube.com/watch?v=gP5Y-ct6QXI) Learn what Kotlin Multiplatform is, how it works, and the benefits of using it. [Video](https://www.youtube.com/watch?v=gP5Y-ct6QXI)