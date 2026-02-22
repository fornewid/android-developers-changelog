---
title: https://developer.android.com/jetpack/androidx/releases/navigation
url: https://developer.android.com/jetpack/androidx/releases/navigation
source: md.txt
---

# Navigation

[User Guide](https://developer.android.com/guide/navigation) [Code Sample](https://github.com/android/architecture-components-samples) [Codelab](https://codelabs.developers.google.com/codelabs/android-navigation) API Reference  
[androidx.navigation](https://developer.android.com/reference/kotlin/androidx/navigation/package-summary)  
[androidx.navigation.compose](https://developer.android.com/reference/kotlin/androidx/navigation/compose/package-summary)  
[androidx.navigation.dynamicfeatures](https://developer.android.com/reference/kotlin/androidx/navigation/dynamicfeatures/package-summary)  
[androidx.navigation.dynamicfeatures.fragment](https://developer.android.com/reference/kotlin/androidx/navigation/dynamicfeatures/fragment/package-summary)  
[androidx.navigation.dynamicfeatures.fragment.ui](https://developer.android.com/reference/kotlin/androidx/navigation/dynamicfeatures/fragment/ui/package-summary)  
[androidx.navigation.fragment](https://developer.android.com/reference/kotlin/androidx/navigation/fragment/package-summary)  
[androidx.navigation.fragment.compose](https://developer.android.com/reference/kotlin/androidx/navigation/fragment/compose/package-summary)  
[androidx.navigation.testing](https://developer.android.com/reference/kotlin/androidx/navigation/testing/package-summary)  
[androidx.navigation.ui](https://developer.android.com/reference/kotlin/androidx/navigation/ui/package-summary)  
Navigation is a framework for navigating between 'destinations' within an Android application that provides a consistent API whether destinations are implemented as Fragments, Activities, or other components.

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| January 28, 2026 | [2.9.7](https://developer.android.com/jetpack/androidx/releases/navigation#2.9.7) | - | - | - |

## Declaring dependencies

To add a dependency on Navigation, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
plugins {
  // Kotlin serialization plugin for type safe routes and navigation arguments
  id 'org.jetbrains.kotlin.plugin.serialization' version '2.0.21'
}
  
dependencies {
  def nav_version = "2.9.7"

  // Jetpack Compose Integration
  implementation "androidx.navigation:navigation-compose:$nav_version"

  // Views/Fragments Integration
  implementation "androidx.navigation:navigation-fragment:$nav_version"
  implementation "androidx.navigation:navigation-ui:$nav_version"

  // Feature module support for Fragments
  implementation "androidx.navigation:navigation-dynamic-features-fragment:$nav_version"

  // Testing Navigation
  androidTestImplementation "androidx.navigation:navigation-testing:$nav_version"

  // JSON serialization library, works with the Kotlin serialization plugin.
  implementation "org.jetbrains.kotlinx:kotlinx-serialization-json:1.7.3"
}
```

### Kotlin

```kotlin
plugins {
  // Kotlin serialization plugin for type safe routes and navigation arguments
  kotlin("plugin.serialization") version "2.0.21"
}

dependencies {
  val nav_version = "2.9.7"

  // Jetpack Compose integration
  implementation("androidx.navigation:navigation-compose:$nav_version")

  // Views/Fragments integration
  implementation("androidx.navigation:navigation-fragment:$nav_version")
  implementation("androidx.navigation:navigation-ui:$nav_version")

  // Feature module support for Fragments
  implementation("androidx.navigation:navigation-dynamic-features-fragment:$nav_version")

  // Testing Navigation
  androidTestImplementation("androidx.navigation:navigation-testing:$nav_version")

  // JSON serialization library, works with the Kotlin serialization plugin
  implementation("org.jetbrains.kotlinx:kotlinx-serialization-json:1.7.3")
}
```

### Safe Args

To add [Safe Args](https://developer.android.com/topic/libraries/architecture/navigation/navigation-pass-data#Safe-args)
to your project, include the following `classpath` in your top level `build.gradle` file:

### Groovy

```groovy
buildscript {
    repositories {
        google()
    }
    dependencies {
        def nav_version = "2.9.7"
        classpath "androidx.navigation:navigation-safe-args-gradle-plugin:$nav_version"
    }
}
```

### Kotlin

```kotlin
buildscript {
    repositories {
        google()
    }
    dependencies {
        val nav_version = "2.9.7"
        classpath("androidx.navigation:navigation-safe-args-gradle-plugin:$nav_version")
    }
}
```

You must also apply one of two available plugins.

To generate Java language code suitable for Java or mixed Java and Kotlin modules, add
this line to **your app or module's** `build.gradle` file:

### Groovy

```groovy
plugins {
  id 'androidx.navigation.safeargs'
}
```

### Kotlin

```kotlin
plugins {
    id("androidx.navigation.safeargs")
}
```

Alternatively, to generate Kotlin code suitable for Kotlin-only modules add:

### Groovy

```groovy
plugins {
  id 'androidx.navigation.safeargs.kotlin'
}
```

### Kotlin

```kotlin
plugins {
    id("androidx.navigation.safeargs.kotlin")
}
```

You must have `android.useAndroidX=true` in your
[`gradle.properties` file](https://developer.android.com/studio/build#properties-files) as per
[Migrating to AndroidX](https://developer.android.com/jetpack/androidx/migrate#migrate)).

For information on using Kotlin extensions, see the [ktx documentation](https://developer.android.com/kotlin/ktx).

For more information about dependencies, see [Add Build Dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:409828+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=409828&template=1093757)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Version 2.9

### Version 2.9.7

January 28, 2026

`androidx.navigation:navigation-*:2.9.7` is released. Version 2.9.7 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/35a9607626f7b80b5418beb35a698f22307e6be3..b96b5bbc32fcbc06328fef80c17f1dda4533fb4b/navigation).

**Bug Fixes**

- Navigation `SafeArgs` no longer has configuration caching issues when being used with Google Services. ([I57cda](https://android-review.googlesource.com/#/q/I57cda144676def56d47091ed93e25c9fe068d6f3), [b/458071608](https://issuetracker.google.com/issues/458071608))
- Fixed the test `SavedStateHandle` constructor in navigation-testing not decoding `List<String>`. ([I26aac](https://android-review.googlesource.com/#/q/I26aac57f7b645c6419a9b770052e08fa8f5d6ad3),[b/454180135](https://issuetracker.google.com/issues/454180135))

### Version 2.9.6

November 05, 2025

`androidx.navigation:navigation-*:2.9.6` is released. Version 2.9.6 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/312fd656536cad70baa4b54621f396d2bd72543f..35a9607626f7b80b5418beb35a698f22307e6be3/navigation).

**Bug Fixes**

- The Navigation `SafeArgs` plugin has been migrated to the modern Android Gradle Plugin APIs which should ensure it is compatible with all AGP 8.4.2+ releases. As a result of these changes, the output directory for files generated by the plugin has been changed to the default location provided by AGP. ([Ie09d6](https://android-review.googlesource.com/#/q/Ie09d6947cd45dba0c9300d1c5d6f5c100bb0f736), [I7c431](https://android-review.googlesource.com/#/q/I7c431915405539e350c26c49ce7b62782ba9fa6d), [b/203559535](https://issuetracker.google.com/issues/203559535), [b/293920476](https://issuetracker.google.com/issues/293920476), [b/269532448](https://issuetracker.google.com/issues/269532448), [b/443261197](https://issuetracker.google.com/issues/443261197))
- Navigation `SafeArgs` plugin will no longer require setting the `useAndroidX` property when being used with AGP 9.0.0-alpha04+. ([I6c3a4](https://android-review.googlesource.com/#/q/I6c3a4eecab1c0927d72742952acdf4aa135b7c7e), [b/444746731](https://issuetracker.google.com/issues/444746731), [b/443106400](https://issuetracker.google.com/issues/443106400))

### Version 2.9.5

September 24, 2025

`androidx.navigation:navigation-*:2.9.5` is released. Version 2.9.5 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1e9b26d010201e0d7ad45f01e64592157cd0d466..312fd656536cad70baa4b54621f396d2bd72543f/navigation).

**Bug Fixes**

- Navigation Safe Args can now handle AGP 9.0's support for builtin kotlin. ([I1d9d76](https://android-review.googlesource.com/#/q/I1d9d76416ff68773269b7825cf912c373f044bec))

**Dependency Update**

- The Navigation Safe Args Plugin now depends on Android Gradle Plugin version 8.4.2. ([b/431847270](https://issuetracker.google.com/431847270), [I5932a](https://android-review.googlesource.com/#/q/I5932a51aea95632deb87c1af28dcb9a8a7eda410))

### Version 2.9.4

September 10, 2025

`androidx.navigation:navigation-*:2.9.4` is released. Version 2.9.4 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b6f111de71da23f7fde5f5c490ad3d17e65de65d..1e9b26d010201e0d7ad45f01e64592157cd0d466/navigation).

**Bug Fixes**

- Prevent crash when a predictive back event is delivered mid-frame after the handler was disabled in a `NavHost` transition. ([I5667c](https://android-review.googlesource.com/#/q/I5667ccf8b9f2dab46bf849be85493766b564e004), [b/384186542](https://issuetracker.google.com/issues/384186542))

### Version 2.9.3

July 30, 2025

`androidx.navigation:navigation-*:2.9.3` is released. Version 2.9.3 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ebd8d05044b7d9e6f4cf56a38d473fbe1ee67e94..b6f111de71da23f7fde5f5c490ad3d17e65de65d/navigation).

**Bug Fixes**

- Fixed an error in `NavController` that caused a `ConcurrentModificationException` when using `OnDestinationChangedListeners`. ([If7406](https://android-review.googlesource.com/#/q/I67fb7a09a28267fe715b36acf38426d9848c41ff), [b/417784831](https://issuetracker.google.com/issues/417784831))
- Fixed an error when using `navigate(uri, navOptions,navigationExtras)` where the extras were being ignored. ([I67fb7](https://android-review.googlesource.com/#/q/I67fb7a09a28267fe715b36acf38426d9848c41ff), [b/430336813](https://issuetracker.google.com/issues/430336813))

### Version 2.9.2

July 16, 2025

`androidx.navigation:navigation-*:2.9.2` is released. Version 2.9.2 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/26d64f2a00c1485431abb846f234756531ed225c..ebd8d05044b7d9e6f4cf56a38d473fbe1ee67e94/navigation).

**Bug Fixes**

- Fixed an issue with the entry not resuming when the dialog above the entry is dismissed ([Idb20e](https://android-review.googlesource.com/#/q/Idb20ebbc9dda76bdd12db1412cd6c9915c814e57), [b/418746335](https://issuetracker.google.com/issues/418746335))
- Fixed `MissingFieldException` error when testing `SavedStateHandle` with type safe routes while using custom `NavTypes`. ([I2f843](https://android-review.googlesource.com/#/q/I2f843b44222d3608e5f9a46f59e537dd6ab5e1a2), [b/421002511](https://issuetracker.google.com/issues/421002511))

### Version 2.9.1

July 2, 2025

`androidx.navigation:navigation-*:2.9.1` is released. Version 2.9.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/69bddec17be2c4afeb216869d5f4e1e8e6cc52cc..26d64f2a00c1485431abb846f234756531ed225c/navigation).

**Bug Fixes**

- Fixed an issue that caused `NavEntries` that were instantiated using single top to never go beyond CREATED in their `Lifecycle.State`. ([I043ba](https://android-review.googlesource.com/#/q/I043ba6789aa7871ab566e7176d4cb78bdbb69c66), [b/421095236](https://issuetracker.google.com/issues/421095236))

### Version 2.9.0

May 7, 2025

`androidx.navigation:navigation-*:2.9.0` is released. Version 2.9.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4eb62506f8e9a7f12ec551b42b5ded5874990416..69bddec17be2c4afeb216869d5f4e1e8e6cc52cc/navigation).

**Important changes since 2.8.0**

- Navigation Safe Args actions are now generated with the `@CheckResult` annotation to ensure they are used.

**SupportingPane Interface**

- Custom Navigators can now mark their destinations as implementing the `SupportingPane` interface which indicates to the `NavController` that these destinations will be shown alongside other destinations. By using this interface, multiple destinations can be `RESUMED` at the same time, for instance.

**Compose Kotlin Multiplatform**

- Navigation now offers a new common `NavController.handleDeepLink()` function that takes a `NavDeepLinkRequest` instead of an `Intent`. This allows platforms other than Android to properly handle deep links. Thanks Konstantin Tskhovrebov!
- Navigation now offers `NavUri`, a new common parser function that is a compatible API for Android's URI on other platforms. This makes it possible to create a URI in a platform agnostic way. Thanks Konstantin Tskhovrebov!

**Type Safe functions**

- The type safe APIs that were previously only accessible via `reified` methods i.e., `composable<YourScreen>` now have non-reified versions that directly take a `KClass` instance.
- Navigation type safety now supports value classes as a route or as the argument type of a route.

### Version 2.9.0-rc01

April 23, 2025

`androidx.navigation:navigation-*:2.9.0-rc01` is released. Version 2.9.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/64e37c2d3d42028c9ab14070feedcab6b5a9e982..8457d8ec6c9d17f1e3f4364453443a45b0ec44a4/navigation).

**Bug Fixes**

- Removed all non-android platform targets from Jetpack Navigation as those targets do not actually work. Stubs for different platforms are now provided instead.([I2877d](https://android-review.googlesource.com/#/q/I2877d33175c362e8256582f7e40f5854d20fddbb))

### Version 2.9.0-beta01

April 9, 2025

`androidx.navigation:navigation-*:2.9.0-beta01` is released. Version 2.9.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/78132378b67c86698d1ade3dc368c9f15d738a71..64e37c2d3d42028c9ab14070feedcab6b5a9e982/navigation).

**API Changes**

- The common API of `parseStringAsNavUri` has been changed to a `NavUri` factory function that takes a String. ([I4db6e](https://android-review.googlesource.com/#/q/I4db6eeb13f86b3dbd987f9b55a49e9a45a8d0b38), [b/403616316](https://issuetracker.google.com/issues/403616316))

**Dependency Updates**

- This library now targets Kotlin 2.0 language level and requires KGP 2.0.0 or newer. ([Idb6b5](https://android-review.googlesource.com/#/q/Idb6b5d6ae1625ab870ffe74f9790ffabc82a63b4))

### Version 2.9.0-alpha09

March 26, 2025

`androidx.navigation:navigation-*:2.9.0-alpha09` is released. Version 2.9.0-alpha09 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/7a145e052ae61e272e91ffe285e9451b8ab71870..78132378b67c86698d1ade3dc368c9f15d738a71/navigation).

**New Features**

- The `navigation-testing` module now supports on desktop, linux, macOS and iOS in addition to android. ([I2b770](https://android-review.googlesource.com/#/q/I2b7707a56f263be30420cae57e3b38480d7f0625), [b/398265336](https://issuetracker.google.com/398265336))
- `NavType` is now supported on desktop, linux, macOS and iOS in addition to android. ([I297d8](https://android-review.googlesource.com/#/q/I297d8846859aaa719b179c7e69e993d0d6e28fd6))

### Version 2.9.0-alpha08

March 12, 2025

`androidx.navigation:navigation-*:2.9.0-alpha08` is released. Version 2.9.0-alpha08 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/fd7408b73d9aac0f18431c22580d9ab612278b1e..7a145e052ae61e272e91ffe285e9451b8ab71870/navigation).

**Bug Fixes**

- From [Navigation `2.8.9`](https://developer.android.com/jetpack/androidx/releases/navigation#2.8.9): Fixed a regression found in [Navigation 2.8.8](https://developer.android.com/jetpack/androidx/releases/navigation#2.8.8) that required a deep link to match all of the fields of a deep link request or intent exactly in order to be considered a match. This caused deep links that contained partial field matches and did not have others to no longer work. ([Ie5e36](https://android-review.googlesource.com/#/q/Ie5e36911112218baf8c53ee142f1366caa31a8b2), [b/399826566](https://issuetracker.google.com/issues/399826566))

**External Contribution**

- New common parser function to create a `NavUri`. Thanks Konstantin Tskhovrebov! ([If0a6a](https://android-review.googlesource.com/#/q/If0a6a5e27fc9ea026deb0bb35cf51665db7dedcf))

### Version 2.9.0-alpha07

February 26, 2025

`androidx.navigation:navigation-*:2.9.0-alpha07` is released. Version 2.9.0-alpha07 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/24c00eb294d9cda579d8d6e48a29497fe0f8d3f7..fd7408b73d9aac0f18431c22580d9ab612278b1e/navigation).

**Bug Fixes**

- Fixed an issue where attempting to `saveState` with non-inclusive pop would result in a null savedState that could cause a crash on restoration. ([I9f3e8](https://android-review.googlesource.com/#/q/I9f3e8d272db222041c7e611932e4c2b7b4fa50c1), [b/395091644](https://issuetracker.google.com/issues/395091644))
- From [Navigation 2.8.8](https://developer.android.com/jetpack/androidx/releases/navigation#2.8.8): `NavDeepLink` matching has been fixed where a deeplink and a deeplink request have to match exactly on uri, action, and mime. Matching is no longer allowed if only one or two fields match. ([I3b029](https://android-review.googlesource.com/#/q/I3b0295caa6324cc707d080856e88e62b4c3cd4d5), [b/395712033](https://issuetracker.google.com/issues/395712033))
- From [Navigation 2.8.8](https://developer.android.com/jetpack/androidx/releases/navigation#2.8.8): Fixed a bug where routes with wildcard paths do not match with an added deeplink ([I7ea92](https://android-review.googlesource.com/#/q/I7ea9206cbecb6ca3d74fbca7721bd2e40e3f915d), [b/389970341](https://issuetracker.google.com/issues/389970341))

**External Contribution**

- Extract a navigation-common, navigation-runtime, and navigation-compose APIs to the common platform. Thanks Konstantin Tskhovrebov! ([I1e626](https://android-review.googlesource.com/#/q/I1e626d27141ce0a86f0df99b4ec7e8cae13b3098), [Ica76f](https://android-review.googlesource.com/#/q/Ica76f79e19d7d694fa80d9a764b6bf763064c9bb), [Idf479](https://android-review.googlesource.com/#/q/Idf4791212e74ce0b44f7aca3923e5ff55dc23faf))

**Known Issues**

- Due to the work to address [b/395712033](https://issuetracker.google.com/issues/395712033), deeplinks are incorrectly required to have all of the same fields as the deeplink request and/or the `Intent`. Deeplinks should only be required to match the fields that they have, and the non-included fields should be ignored. This has been fixed for a later release as part of [b/399826566](https://issuetracker.google.com/issues/399826566).

### Version 2.9.0-alpha06

February 12, 2025

`androidx.navigation:navigation-*:2.9.0-alpha06` is released. Version 2.9.0-alpha06 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6c0a0880e6edc4cafbecd784a98619d0813d1025..24c00eb294d9cda579d8d6e48a29497fe0f8d3f7/navigation).

**New Features**

- Navigation Safe Args actions are now generated with the `@CheckResult` annotation to ensure they are used. ([I14d4c](https://android-review.googlesource.com/#/q/I14d4c00fe8fc0e994b962776e1f10b4a8a63ece4), [b/356323084](https://issuetracker.google.com/issues/356323084))

**Bug Fixes**

- Fixed an error in `NavController` where the backStack states were incorrectly attempted to be restored into an array when they were saved into a list. ([Idfb9b](https://android-review.googlesource.com/#/q/Idfb9bebc9d733a3e55f00f48c357cfe1e00e27b4))
- From [Navigation `2.8.7`](https://developer.android.com/jetpack/androidx/releases/navigation#2.8.7): Navigation Safe Args now provides support for composable destinations. ([I35320](https://android-review.googlesource.com/#/q/I353205e72fe2896cae7ca1f563bfe58798e59578), [b/362791955](https://issuetracker.google.com/issues/362791955))

### Version 2.9.0-alpha05

January 29, 2025

`androidx.navigation:navigation-*:2.9.0-alpha05` is released. Version 2.9.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/46295bc0b75a16f452e8e0090e8de41073d4dbb6..6c0a0880e6edc4cafbecd784a98619d0813d1025/navigation).

**Bug Fixes**

- Fix an issue that caused an unexpected scale animation when using Navigation Compose. ([I480f4](https://android-review.googlesource.com/#/q/I480f4d89ffc7e2dfa536a592a8fc7b6c759be1a4), [b/353294030](https://issuetracker.google.com/issues/353294030))
- From [Navigation `2.8.6`](https://developer.android.com/jetpack/androidx/releases/navigation#2.8.6): `NavDestination` labels provided through XML will be parsed via `NavType.get` to ensure custom `NavType` logic is respected. ([I7ec2f](https://android-review.googlesource.com/#/q/I7ec2f3e410b616e8933c8f5dd8015869906fb263), [b/388100796](https://issuetracker.google.com/issues/388100796))
- From [Navigation `2.8.6`](https://developer.android.com/jetpack/androidx/releases/navigation#2.8.6): When navigating to activity with `dataPattern`, `ActivityNavigator` will now try to encode the arg value with the argument's `NavType`. ([I16376](https://android-review.googlesource.com/#/q/I163763c46090ae9b4c8ee75d52142986e507c0c3), [b/383616432](https://issuetracker.google.com/issues/383616432))
- From [Navigation `2.8.5`](https://developer.android.com/jetpack/androidx/releases/navigation#2.8.5): Fixed an issue that caused an unexpected scale animation when using Navigation Compose and calling navigate in the same frame that the current animation is ending. ([I26cb1](https://android-review.googlesource.com/#/q/I26cb142affb046e94b34b9501e5405ddcf276fcf), [b/353294030](https://issuetracker.google.com/issues/353294030))

### Version 2.9.0-alpha04

December 11, 2024

`androidx.navigation:navigation-*:2.9.0-alpha04` is released. Version 2.9.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6f09cf2ae979e48fdb19485f757a033e4a34bb82..46295bc0b75a16f452e8e0090e8de41073d4dbb6/navigation).

**New Features**

- The type safe APIs that were previously only accessible via `reified` methods i.e., `composable<YourScreen>` now have non-reified versions that directly take a `KClass` instance.([Ia7eed](https://android-review.googlesource.com/#/q/Ia7eed5b9c0fe15834468d3eccc489c2dc3edca74), [Id2879](https://android-review.googlesource.com/#/q/Id28791416c67c0b4930370ded037ffb3c40922b6), [Ibf244](https://android-review.googlesource.com/#/q/Ibf24453e66d69c00d4ffb3abe4dc5a1f3782ad09), [I17d79](https://android-review.googlesource.com/#/q/I17d79479d8a1f2acda8f6767a40ff19773235d9d), [Id09d2](https://android-review.googlesource.com/#/q/Id09d2f511e9844b0618140781f07bebe1e7deb77), [I54696](https://android-review.googlesource.com/#/q/I54696ee5ce64305386de64654c6ce15f3a1fd741), [Ia47be](https://android-review.googlesource.com/#/q/Ia47be2a0ac9e2b8ef5def4aa808b939e15259d2a), [I93281](https://android-review.googlesource.com/#/q/I93281ed88fe3be9e6c68a2d5f16d9e0f335c999d), [Ic1bf0](https://android-review.googlesource.com/#/q/Ic1bf09bdd59e0d96db7edb89276ac31a977d6602), [Iba4ee](https://android-review.googlesource.com/#/q/Iba4ee26b906c09e7ec47b7e940cf689788c117e8), [If56a5](https://android-review.googlesource.com/#/q/If56a553a4d2608a5eb059ea684e566a4feae955b), [Icf969](https://android-review.googlesource.com/#/q/Icf9692ffcf3103b1ec0c6b98e436eec09f7f9d9d), [I67644](https://android-review.googlesource.com/#/q/I676443ef1ac6cbb7464fb5677c8639ef1786272d), [I6f788](https://android-review.googlesource.com/#/q/I6f7884836f74d263d9d342df1593c61a9b9835ba), [b/382094941](https://issuetracker.google.com/issues/382094941), [b/366291612](https://issuetracker.google.com/issues/366291612), [b/381938808](https://issuetracker.google.com/issues/381938808))

The table below provides the reified and KClass APIs.

| reified | KClass |
|---|---|
| `composable<TestClass> { }` | `composable(TestClass::class) { }` |
| `navigation<NestedGraph>(startDestination = TestClass::class)` | `navigation(route = NestedGraph::class, startDestination = TestClass::class)` |
| `dialog<TestClass> {}` | `dialog(TestClass::class) {}` |
| `navDeepLink<TestClass>(baseUri)` | `navDeepLink(TestClass::class, baseUri)` |
| `NavDeepLink.Builder.setUriPattern<TestClass>(baseUri)` | `NavDeepLink.Builder.setUriPattern(TestClass::class, baseUri)` |
| `NavDestinationBuilder.deepLink<TestDeepLink>(baseUri) { }` | `NavDestinationBuilder.deepLink(TestDeepLink::class, baseUri) { }` |
| `navController.getBackStackEntry<TestClass>()` | `navController.getBackStackEntry(TestClass::class)` |
| `navController.popBackStack<TestClass>(true)` | `navController.popBackStack(TestClass::class, true)` |
| `navController.clearBackStack<TestClass>()` | `navController.clearBackStack(TestClass::class)` |
| `NavOptions.setPopUpTo<TestClass>()` | `NavOptions.setPopUpTo(TestClass::class)` |
| `navOptions { popUpTo<TestClass> {...} }` | `navOptions { popUpTo(TestClass::class) {...} }` |
| `NavGraph.setStartDestination<TestClass>()` | `NavGraph.setStartDestination(TestClass::class)` |
| `NavGraph.findNode<TestClass>()` | `NavGraph.findNode(TestClass::class)` |
| `backStackEntry.toRoute<TestClass>()` | `backStackEntry.toRoute(TestClass::class)` |
| `savedStateHandle.toRoute<TestClass>()` | `savedStateHandle.toRoute(TestClass::class)` |

**API Changes**

- The kotlin-specific `NavGraph.setStartDestination` overload for type safety is hidden from Java sources. ([Ic640c](https://android-review.googlesource.com/#/q/Ic640c37f3cef5578022866529a8e576eba8d745d), [b/364634035](https://issuetracker.google.com/issues/364634035))

**Bug Fixes**

- From [Navigation `2.8.5`](https://developer.android.com/jetpack/androidx/releases/navigation#2.8.5): Fixed an issue where `NavHost` could throw an exception inside of the `PredictiveBackHandler` if the back stack is popped down to 1 entry and a system back are triggered in the same frame. ([I1a429](https://android-review.googlesource.com/#/q/I1a4297a10f2d0da8c8477644b9250c61e4792923), [b/375343407](https://issuetracker.google.com/issues/375343407))
- From [Navigation `2.8.5`](https://developer.android.com/jetpack/androidx/releases/navigation#2.8.5): Fixed `NavDestination` `NullPointerException` when updating a graph's `startDestination`. ([I99421](https://android-review.googlesource.com/#/q/I99421bf1e4aef9802873d9d78fbc6fafc15a21ba), [b/361560785](https://issuetracker.google.com/issues/361560785))

**External Contribution**

- From [Navigation `2.8.5`](https://developer.android.com/jetpack/androidx/releases/navigation#2.8.5): Navigation type safety now supports `List<Enum>` as an argument type of a route without requiring any custom `NavType`. Thanks [Csaba Kozák](https://github.com/WonderCsabo)! ([GH-725](https://github.com/androidx/androidx/pull/725), [b/375559962](https://issuetracker.google.com/375559962))

### Version 2.9.0-alpha03

November 13, 2024

`androidx.navigation:navigation-*:2.9.0-alpha03` is released. Version 2.9.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ccd90a76bd7c4acf4f4f01eca76350e383bc441e..6f09cf2ae979e48fdb19485f757a033e4a34bb82/navigation).

**New Features**

- Navigation type safety now supports value classes as a route or as the argument type of a route. ([I9344a](https://android-review.googlesource.com/#/q/I9344a33fe10d53701e53635af93176654957afb2), [b/374347483](https://issuetracker.google.com/issues/374347483))

**Bug Fixes**

- Fixed a `ConcurrentModificationException` that could occur when a `LifecycleObserver` attached to a `NavBackStackEntry` triggers a change to the back stack when the host `LifecycleOwner` such as the containing Activity or Fragment changes its lifecycle state. ([Ia9494](https://android-review.googlesource.com/#/q/Ia9494e9967aa45a7613c49d7530f524f5400d1ca))

### Version 2.9.0-alpha02

October 30, 2024

`androidx.navigation:navigation-*:2.9.0-alpha02` is released. Version 2.9.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b8a68b0896897fa158508d73a31998a26161d9a7..ccd90a76bd7c4acf4f4f01eca76350e383bc441e/navigation).

**External Contribution**

- New common `NavController.handleDeepLink(request: NavDeepLinkRequest)` method. Thanks Konstantin Tskhovrebov! ([I3e228](https://android-review.googlesource.com/#/q/I3e22808b36e691658494191797056b7e3c4b4419))

### Version 2.9.0-alpha01

October 16, 2024

`androidx.navigation:navigation-*:2.9.0-alpha01` is released. Version 2.9.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/56650b920c78899081a1a16fdb81dab72753b5ef..b8a68b0896897fa158508d73a31998a26161d9a7/navigation).

**New Features**

- Custom Navigators can now mark their destinations as implementing the `SupportingPane` interface which indicates to the `NavController` that these destinations will be shown alongside other destinations. By using this interface, multiple destinations can be `RESUMED` at the same time, for instance. ([Id5559](https://android-review.googlesource.com/#/q/Id5559bdaf3e31fb6d6fb66be0b451627c075d342))
- From [Navigation `2.8.3`](https://developer.android.com/jetpack/androidx/releases/navigation#2.8.3): Added new lint checks for the `navigation-common`, `navigation-runtime`, and `navigation-compose` modules to help identify any type-safe routes that are not correctly annotated with `@Serializable`. This check is applied to all `NavGraphBuilder` and `NavDeepLinkBuilder` extension functions. ([I4a259](https://android-review.googlesource.com/#/q/I4a259b5544e4e4655c4bdee812d64f3b2a1947bd), [I95402](https://android-review.googlesource.com/#/q/I954023cd0cb4a5ee7d08647cf9a8139b0c8ae9d9), [Ie601a](https://android-review.googlesource.com/#/q/Ie601a15449b1561154bd3ae5d990e006a371c7c6), [Id8c6e](https://android-review.googlesource.com/#/q/Id8c6ef1ee0839a43864afac58a5437ad1379e25f), [I28bda](https://android-review.googlesource.com/#/q/I28bda5541ec144f17668302d56ecaef4011becb3), [b/362725816](https://issuetracker.google.com/issues/362725816))
- From [Navigation `2.8.3`](https://developer.android.com/jetpack/androidx/releases/navigation#2.8.3): Added new lint checks for the `navigation-common`, `navigation-runtime`, and `navigation-compose` modules to help identify any type-safe routes with Enum arguments that are not correctly annotated with `@Keep`. This check is applied to all `NavGraphBuilder` and `NavDeepLinkBuilder` extension functions. ([I4a259](https://android-review.googlesource.com/#/q/I4a259b5544e4e4655c4bdee812d64f3b2a1947bd), [I95402](https://android-review.googlesource.com/#/q/I954023cd0cb4a5ee7d08647cf9a8139b0c8ae9d9), [Ie601a](https://android-review.googlesource.com/#/q/Ie601a15449b1561154bd3ae5d990e006a371c7c6), [Id8c6e](https://android-review.googlesource.com/#/q/Id8c6ef1ee0839a43864afac58a5437ad1379e25f), [I2b46f](https://android-review.googlesource.com/#/q/I2b46fbc3b5be6251d89e902e315f50f20c46ce19), [b/358687142](https://issuetracker.google.com/issues/358687142))

**Behavior Changes**

- Attempting to use a `NavController` that has been previously `DESTROYED` will now cause an `IllegalStateException`. ([I520da](https://android-review.googlesource.com/#/q/I520da520adf9f99d887e63c0255afe97ecefdab5), [b/369616172](https://issuetracker.google.com/issues/369616172))

**Bug Fixes**

- Update Enum class not found exception to suggest using `@Keep` annotation in case the Enum class gets erased in minified builds. ([I90e79](https://android-review.googlesource.com/#/q/I90e79cc476c21ab0ad3b172af65c436817665ef7), [b/358137294](https://issuetracker.google.com/issues/358137294))

**Known Issues**

- There is an issue with the new lint rules that were added in `Navigation 2.8.*` that cause an `Obsolete custom lint check` error when attempting to run lint with Android Gradle Plugin 8.4+. ([b/368070326](https://issuetracker.google.com/issues/368070326), [b/371463741](https://issuetracker.google.com/issues/371463741))

## Version 2.8

### Version 2.8.9

March 12, 2025

`androidx.navigation:navigation-*:2.8.9` is released. Version 2.8.9 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/f8393fac98d1b3e0724b7731ba8dbceb0eec819b..d42dd5f65a0287fd6d7cd115894bc58cbd52885e/navigation).

**Bug Fixes**

- Fixed a regression found in [Navigation 2.8.8](https://developer.android.com/jetpack/androidx/releases/navigation#2.8.8) that required a deep link to match all of the fields of a deep link request or intent exactly in order to be considered a match. This caused deep links that contained partial field matches and did not have others to no longer work. ([Ie5e36](https://android-review.googlesource.com/#/q/Ie5e36911112218baf8c53ee142f1366caa31a8b2), [b/399826566](https://issuetracker.google.com/issues/399826566))

### Version 2.8.8

February 26, 2025

`androidx.navigation:navigation-*:2.8.8` is released. Version 2.8.8 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/5eb029f77fd2568df6aed4e3dd57a03f69288f34..f8393fac98d1b3e0724b7731ba8dbceb0eec819b/navigation).

**Bug Fixes**

- Fixed a bug where routes with wildcard paths do not match with an added deeplink. ([I7ea92](https://android-review.googlesource.com/#/q/I7ea9206cbecb6ca3d74fbca7721bd2e40e3f915d), [b/389970341](https://issuetracker.google.com/issues/389970341))
- `NavDeepLink` matching has been fixed where a deeplink and a deeplink request have to match exactly on uri, action, and mime. Matching is no longer allowed if only one or two fields match. ([I3227f](https://android-review.googlesource.com/#/q/I3227f41f447e117f1170b00726edd2fedc9aefb5), [b/395712033](https://issuetracker.google.com/issues/395712033))

**Known Issues**

- Due to the work to address [b/395712033](https://issuetracker.google.com/issues/395712033), deeplinks are incorrectly required to have all of the same fields as the deeplink request and/or the `Intent`. Deeplinks should only be required to match the fields that they have, and the non-included fields should be ignored. This has been fixed for a later release as part of [b/399826566](https://issuetracker.google.com/issues/399826566).

### Version 2.8.7

February 12, 2025

`androidx.navigation:navigation-*:2.8.7` is released. Version 2.8.7 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/51594ca1bcc0285e14781d71f0bb0faf255ddab2..5eb029f77fd2568df6aed4e3dd57a03f69288f34/navigation).

**Bug Fixes**

- Navigation Safe Args now provides support for composable destinations. ([I35320](https://android-review.googlesource.com/#/q/I353205e72fe2896cae7ca1f563bfe58798e59578), [b/362791955](https://issuetracker.google.com/issues/362791955))

### Version 2.8.6

January 29, 2025

`androidx.navigation:navigation-*:2.8.6` is released. Version 2.8.6 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4d3a39c79e99cb8cc27cbf8da139bc98c56780c6..51594ca1bcc0285e14781d71f0bb0faf255ddab2/navigation).

**Bug Fixes**

- `NavDestination` labels provided through XML will be parsed via `NavType.get` to ensure custom `NavType` logic is respected. ([Id366d](https://android-review.googlesource.com/#/q/Id366d0d5bff908cb8ec38c310a991a107bf8af54), [b/388100796](https://issuetracker.google.com/issues/388100796))
- When navigating to activity with `dataPattern`, `ActivityNavigator` will now try to encode the arg value with the argument's `NavType`. ([I1a71d](https://android-review.googlesource.com/#/q/I1a71db1d4e84b363196cdb121814c4a27dc97074), [b/383616432](https://issuetracker.google.com/issues/383616432))

### Version 2.8.5

December 11, 2024

`androidx.navigation:navigation-*:2.8.5` is released. Version 2.8.5 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6754f1118fa8ad573c67255da26c0eecf2531589..31321b807270f38175045861a586853dba5cb96b/navigation).

**Bug Fixes**

- Fixed an issue where `NavHost` could throw an exception inside of the `PredictiveBackHandler` if the back stack is popped down to 1 entry and a system back are triggered in the same frame. ([I1a429](https://android-review.googlesource.com/#/q/I1a4297a10f2d0da8c8477644b9250c61e4792923), [b/375343407](https://issuetracker.google.com/issues/375343407))
- Fixed `NavDestination` `NullPointerException` when updating a graph's `startDestination`. ([I99421](https://android-review.googlesource.com/#/q/I99421bf1e4aef9802873d9d78fbc6fafc15a21ba), [b/361560785](https://issuetracker.google.com/issues/361560785))
- Fixed an issue that caused an unexpected scale animation when using Navigation Compose and calling navigate in the same frame that the current animation is ending. ([I26cb1](https://android-review.googlesource.com/#/q/I26cb142affb046e94b34b9501e5405ddcf276fcf), [b/353294030](https://issuetracker.google.com/issues/353294030))
- Fixed a `ConcurrentModificationException` that could occur when a `LifecycleObserver` attached to a `NavBackStackEntry` triggers a change to the back stack when the host `LifecycleOwner` such as the containing Activity or Fragment changes its lifecycle state. ([Ia9494](https://android-review.googlesource.com/#/q/Ia9494e9967aa45a7613c49d7530f524f5400d1ca))

**External Contribution**

- Navigation type safety now supports `List<Enum>` as an argument type of a route without requiring any custom `NavType`. Thanks [Csaba Kozák](https://github.com/WonderCsabo)! ([GH-725](https://github.com/androidx/androidx/pull/725), [b/375559962](https://issuetracker.google.com/375559962))

### Version 2.8.4

November 13, 2024

`androidx.navigation:navigation-*:2.8.4` is released. Version 2.8.4 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/2822fa81f0a1cf4c14abd0e8ad3a56799ad79eee..6754f1118fa8ad573c67255da26c0eecf2531589/navigation).

**New Features**

- From [Navigation `2.9.0-alpha03`](https://developer.android.com/jetpack/androidx/releases/navigation#2.9.0-alpha03): Navigation type safety now supports value class as route or as the argument type of a route ([I9344a](https://android-review.googlesource.com/#/q/I9344a33fe10d53701e53635af93176654957afb2), [b/374347483](https://issuetracker.google.com/issues/374347483))

**Bug Fixes**

- From [Navigation `2.9.0-alpha01`](https://developer.android.com/jetpack/androidx/releases/navigation#2.9.0-alpha01): Attempting to use a `NavController` that has been previously `DESTROYED` will now cause an `IllegalStateException`. ([I520da](https://android-review.googlesource.com/#/q/I520da520adf9f99d887e63c0255afe97ecefdab5), [b/369616172](https://issuetracker.google.com/issues/369616172))

### Version 2.8.3

October 16, 2024

`androidx.navigation:navigation-*:2.8.3` is released. Version 2.8.3 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/56650b920c78899081a1a16fdb81dab72753b5ef..2822fa81f0a1cf4c14abd0e8ad3a56799ad79eee/navigation).

**New Features**

- Added new lint checks for the `navigation-common`, `navigation-runtime`, and `navigation-compose` modules to help identify any type-safe routes that are not correctly annotated with `@Serializable`. This check is applied to all `NavGraphBuilder` and `NavDeepLinkBuilder` extension functions. ([I4a259](https://android-review.googlesource.com/#/q/I4a259b5544e4e4655c4bdee812d64f3b2a1947bd), [I95402](https://android-review.googlesource.com/#/q/I954023cd0cb4a5ee7d08647cf9a8139b0c8ae9d9), [Ie601a](https://android-review.googlesource.com/#/q/Ie601a15449b1561154bd3ae5d990e006a371c7c6), [Id8c6e](https://android-review.googlesource.com/#/q/Id8c6ef1ee0839a43864afac58a5437ad1379e25f), [I28bda](https://android-review.googlesource.com/#/q/I28bda5541ec144f17668302d56ecaef4011becb3), [b/362725816](https://issuetracker.google.com/issues/362725816))
- Added new lint checks for the `navigation-common`, `navigation-runtime`, and `navigation-compose` modules to help identify any type-safe routes with Enum arguments that are not correctly annotated with `@Keep`. This check is applied to all `NavGraphBuilder` and `NavDeepLinkBuilder` extension functions. ([I4a259](https://android-review.googlesource.com/#/q/I4a259b5544e4e4655c4bdee812d64f3b2a1947bd), [I95402](https://android-review.googlesource.com/#/q/I954023cd0cb4a5ee7d08647cf9a8139b0c8ae9d9), [Ie601a](https://android-review.googlesource.com/#/q/Ie601a15449b1561154bd3ae5d990e006a371c7c6), [Id8c6e](https://android-review.googlesource.com/#/q/Id8c6ef1ee0839a43864afac58a5437ad1379e25f), [I2b46f](https://android-review.googlesource.com/#/q/I2b46fbc3b5be6251d89e902e315f50f20c46ce19), [b/358687142](https://issuetracker.google.com/issues/358687142))

**Bug Fixes**

- Fixed an issue where the new lint rules that were added in `Navigation 2.8.*` would cause an `Obsolete custom lint check` error when attempting to run lint with Android Gradle Plugin 8.4+. ([I1be3d](https://android-review.googlesource.com/#/q/I1be3d7dc113f799e17314008efc5d914c6cb8ee7), [b/368070326](https://issuetracker.google.com/issues/368070326), [b/371463741](https://issuetracker.google.com/issues/371463741))

**Known Issues**

- Navigation lint will throw an Obsolete custom lint check error when attempting to run lint with Lint 16 (AGP 8.7) or higher. ([b/371926651](https://issuetracker.google.com/issues/371926651))

### Version 2.8.2

October 2, 2024

`androidx.navigation:navigation-*:2.8.2` is released. Version 2.8.2 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e5c636f0655470cfa3dac640d9454331d1197d80..56650b920c78899081a1a16fdb81dab72753b5ef/navigation).

**New Features**

- Navigation Type Safety now supports Serializable classes that include a `Double`, `Double?`, `DoubleArray`, `DoubleArray?`, `List<Double>`, and `List<Double>?` without requiring any custom `NavType`. ([I570eb](https://android-review.googlesource.com/#/q/I570ebef5242e1bc3e8ee3f5d58b4aa2d677abaee), [Ibc4c0](https://android-review.googlesource.com/#/q/Ibc4c02fa77e416c1c007209fb358a0d1c34389db), [I37461](https://android-review.googlesource.com/#/q/I374616d825fff71394721b51e01be5257899663c), [I5bed4](https://android-review.googlesource.com/#/q/I5bed4745773efa2e8a57fcdacc77cc16b1845067), [b/359245753](https://issuetracker.google.com/issues/359245753))

**Bug Fixes**

- Improved the error message for when Navigation fails to map a route's argument to a `NavType`, the new error message will contain the argument name, argument fully qualified name, and the route's fully qualified name. ([Id8416](https://android-review.googlesource.com/#/q/Id84161f47630fe76d85af01bb06c7f3a13d372bb), [b/346264232](https://issuetracker.google.com/issues/346264232))

### Version 2.8.1

September 18, 2024

`androidx.navigation:navigation-*:2.8.1` is released. Version 2.8.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/89b0ab6acbda86348e82091c6e1909c6ad69cea3..e5c636f0655470cfa3dac640d9454331d1197d80/navigation).

**New Features**

- Added a new lint rule to ensure the use of the `popBackStack` function that takes a reified class type when attempting to `popBackStack` using type-safe APIs. ([Ief161](https://android-review.googlesource.com/#/q/Ief1614a3ff15937b173536a43ba3f0de3c4d8b8a), [b/358095343](https://issuetracker.google.com/issues/358095343))

**Bug Fixes**

- Navigation now requires that the route passed to a `NavGraph`'s `startDestination` contains the values for all required arguments, which includes arguments that are non-nullable and have no default value. ([I18e74](https://android-review.googlesource.com/#/q/I18e7401ac7a4d322db2add9b0f2781196d4d3257), [b/362594265](https://issuetracker.google.com/issues/362594265))
- Navigation safe args has added support for non-nullable strings such that "null" values will be parsed and stored into the bundle as is. This departs from existing behavior where "null" values are parsed into a null object. This change only applies to non-nullable String types. Nullable strings remain unchanged. ([I08b4a](https://android-review.googlesource.com/#/q/I08b4a9ce5e295a1bddb7baaf9b09af6367a2faa9), [b/348936238](https://issuetracker.google.com/issues/348936238))
- A `NavDestination` can no longer be deeplinked into except through a deep link that was explicitly added to the destination. This also means that you can only navigate to a destination's route with the navigate function overload that takes a string route. This fixes a vulnerability that made it possible to deep link to a potentially protected destination. ([Ie30e6](https://android-review.googlesource.com/#/q/Ie30e6c782fc511f1868dfab0d5ab11eab2bf8c4f))

**Dependency Update**

- Navigation Safe Args now depends on Kotlin 1.9.24, rather than Kotlin 2.X, ensuring that developers are not forced to update. ([a4129a](https://android.googlesource.com/platform/frameworks/support/+/a4129ad752cb16484a021f26d63126381ffa5392))
- Navigation Compose now depends on [Compose `1.7.2`](https://developer.android.com/jetpack/androidx/releases/compose-animation#1.7.2).

### Version 2.8.0

September 4, 2024

`androidx.navigation:navigation-*:2.8.0` is released. Version 2.8.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c19eabc8b1f7d6b3b33ce697447d6c98a4f336dd..89b0ab6acbda86348e82091c6e1909c6ad69cea3/navigation).

**Important changes since 2.7.0**

**Navigation Kotlin DSL Type-Safety**

- Navigation now provides type-safety for the Kotlin DSL (used by Navigation Compose) using Kotlin Serialization to allow you to define destinations in your navigation graph via type safe objects and data classes:

        // Define a home destination that doesn't take any arguments
        @Serializable
        object Home

        // Define a profile destination that takes an ID
        @Serializable
        data class Profile(val id: String)

        // Now define your NavHost using type safe objects
        NavHost(navController, startDestination = Home) {
            composable<Home> {
                HomeScreen(onNavigateToProfile = { id ->
                    navController.navigate(Profile(id))
                })
            }
            composable<Profile> { backStackEntry ->
                val profile: Profile = backStackEntry.toRoute()
                ProfileScreen(profile)
            }
        }

See the [Navigation Compose meet Type Safety blog post](https://medium.com/androiddevelopers/navigation-compose-meet-type-safety-e081fb3cf2f8) for more information.

**Navigation Compose Predictive Back**

- Navigation Compose now provides support for Predictive in-app back via the new `SeekableTransitionState` APIs from compose-animation. This allows you to use the back gesture to see the previous destination with your custom Transition before deciding to either commit the transaction via the completed gesture or cancel.

**Navigation Fragment Composable**

- Added a new `navigation-fragment-compose` artifact that includes a `ComposableNavHostFragment` alternative to `NavHostFragment` that allows you to add composable destinations to your Navigation XML files. Each `composable` destination must be expressed as a top-level, no argument `@Composable` method whose fully qualified name is used as the `android:name` attribute on each destination. When navigating to one of these destinations, a containing fragment is created to display the composable content.

      // In HomeScreen.kt
      @Composable
      fun HomeScreen() {
        // Your Composable content here
      }

      // In your navigation.xml
      <composable
        android:id="@+id/home_screen"
        android:name="com.example.HomeScreenKt\$HomeScreen" />

**Other Changes**

- Navigation Compose now depends on Compose 1.7.0.
- Navigation now provides a new `CollectionNavType<T>` class, a subclass of `NavType<T>` for collection-based arguments such as list, arrays, maps. All of the default `NavType` arrays (`IntArrayType`, `LongArrayType`, `FloatArrayType`, `BoolArrayType`, and `StringArrayType`) now inherit from this new class.
- `NavType` now has built-in support for Lists of Int, String, Boolean, Float, and Long.

### Version 2.8.0-rc01

August 21, 2024

`androidx.navigation:navigation-*:2.8.0-rc01` is released. Version 2.8.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/9130b719318a69f2f3eaf82c32b131232fd721cb..c19eabc8b1f7d6b3b33ce697447d6c98a4f336dd/navigation).

**Bug Fixes**

- Fix navigation crash when passing in top level Enum classes as type safe arguments. ([I0ba76](https://android-review.googlesource.com/#/q/I0ba7670109e378668548a47dd6981a5b1a2f5aba), [b/358137294](https://issuetracker.google.com/issues/358137294))
- Navigation 2.8 now correctly works with SDK 34 and will not swap over to SDK 35 until the 2.9 release along with the rest of the AndroidX libraries. ([b/358798728](https://issuetracker.google.com/issues/358798728))

### Version 2.8.0-beta07

August 7, 2024

`androidx.navigation:navigation-*:2.8.0-beta07` is released. Version 2.8.0-beta07 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/8b5ab34869fa8731b13a77763ea92989ce4ef70d..9130b719318a69f2f3eaf82c32b131232fd721cb/navigation).

**Known Issues**

- Due to [b/358137294](https://issuetracker.google.com/issues/358137294), only Enums nested in another class are supported out of the box. Top level Enums will be supported in the next release.

**Bug Fixes**

- When navigating to duplicate or shared destinations, navigation will prioritize going to the closest matching destination from the current location in the graph. ([Ic89a4](https://android-review.googlesource.com/#/q/Ic89a41d2a54f36fca6c41f2f7ea948f8c13b2bd5), [b/352006850](https://issuetracker.google.com/issues/352006850))
- Navigation in safe args now has added a new `NavType.EnumType`. This means `Enum` types no longer require custom `NavType`s. Note that the `Enum`'s `SerialName` must be the default fully qualified name. ([I66d22](https://android-review.googlesource.com/#/q/I66d22e2004a9c996688f082f1732b7f4c4e8ca24), [b/346475493](https://issuetracker.google.com/issues/346475493))
- Navigation in safe args has added built-in support for nullable argument types including `Int?`,`Long?`, `Float?`, `Boolean?`, and `Enum<*>?`. ([I32d13](https://android-review.googlesource.com/#/q/I32d131926d08b01151c22d35f7a2d3389d5a1f56),[I1c580](https://android-review.googlesource.com/#/q/I1c580e271cab940b11378f85bd0a5175c503e2f5),[Ifba66](https://android-review.googlesource.com/#/q/Ifba6679f9214b477802567403d8ae97203a30303),[I978b0](https://android-review.googlesource.com/#/q/I978b0c52b9847518f77d5f238ef8461da9dc485b),[Ide076](https://android-review.googlesource.com/#/q/Ide076fd4f77daf8373d71e093f833920aba9b911) , [b/351994237](https://issuetracker.google.com/issues/351994237))
- The `NavGraph`'s `startDestination` will now use the default argument values if the `startDestination` route passed to the `NavGraph` is exactly equal to the `startDestination.route`. ([I13762](https://android-review.googlesource.com/#/q/I137626c99c62ec57db4a44448dd7cdf61209f264), [b/354046047](https://issuetracker.google.com/issues/354046047))

### Version 2.8.0-beta06

July 24, 2024

`androidx.navigation:navigation-*:2.8.0-beta06` is released. Version 2.8.0-beta06 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/56579bc30499ce39f0d7a6713a065b00c6194206..8b5ab34869fa8731b13a77763ea92989ce4ef70d/navigation).

**Bug Fixes**

- Fixed an issue where the `WrongStartDestinationType` lint checks did not check for Companion objects on the passed in class type, causing lint to fail to detect the error. ([I92b09](https://android-review.googlesource.com/#/q/I92b095af135ce0cffd5cd251de65a3ee70d813c8))

### Version 2.8.0-beta05

July 10, 2024

`androidx.navigation:navigation-*:2.8.0-beta05` is released. Version 2.8.0-beta05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/5299742c3cf8497f1690c2399056af490673d29e..56579bc30499ce39f0d7a6713a065b00c6194206/navigation).

**Bug Fixes**

- Fix `singleTop` navigation crash when nested `NavGraphs` share the same `startDestination` route. ([I17b94](https://android-review.googlesource.com/#/q/I17b9466ce3411e0113d1f9a56faa8706577abc72), [b/294408596](https://issuetracker.google.com/issues/294408596))

### Version 2.8.0-beta04

June 26, 2024

`androidx.navigation:navigation-*:2.8.0-beta04` is released. Version 2.8.0-beta04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/9de5bf61f1fad1fd6da2b64fe350d3aa39dc5de1..5299742c3cf8497f1690c2399056af490673d29e/navigation).

**Bug Fixes**

- Navigation now supports navigating with empty strings in path arguments. ([Ic5dbd](https://android-review.googlesource.com/#/q/Ic5dbdd3b4786f62f4544a70b6786a269da8a37cc), [b/339481310](https://issuetracker.google.com/issues/339481310))
- Improve error message for custom serializers declared directly on class fields via `@Serializable(with =...)` to clarify that this is currently an unsupported feature. ([I052b0](https://android-review.googlesource.com/#/q/I052b0e6a34c7e38520723e7c00a920dc7abe4eb7), [b/341319151](https://issuetracker.google.com/issues/341319151))
- `SavedStateHandleFactory` test api can now be used in non-android tests but will require Robolectric to support argument parsing with Bundles. ([I76cdc](https://android-review.googlesource.com/#/q/I76cdc4b40474680dbdb58e6b8a6451f0e228f9b1), [b/340966212](https://issuetracker.google.com/issues/340966212))
- Fixed crash from restoring state when resuming the app after process death with using Type-Safe Navigation in Compose. ([Ia8f38](https://android-review.googlesource.com/#/q/Ia8f38fc59b8e4dac1910c5a593e1ec0585e59456), [b/341801005](https://issuetracker.google.com/issues/341801005))
- Fixed an issue in Navigation Compose where after canceling the Predictive Back Gesture, the `NavBackStackEntry` that the user returns to never returns back to the `RESUMED` Lifecycle State. This also ensures the returning destination correctly animates back in instead of snapping into place after a fling. ([I97a0c](https://android-review.googlesource.com/#/q/I97a0c5fe7fe661a2fadfbb01346676482d426028), [b/346608857](https://issuetracker.google.com/issues/346608857))
- When using Predictive back with Navigation Compose, the destination being popped will now have the proper z-order, correctly animating on top of the incoming destination. ([I2077b](https://android-review.googlesource.com/#/q/I2077b399fc9bc9a846da6ed17d63d002c8e8122f), [b/345993681](https://issuetracker.google.com/issues/345993681))

### Version 2.8.0-beta03

June 12, 2024

`androidx.navigation:navigation-*:2.8.0-beta03` is released. Version 2.8.0-beta03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/473554f275109d78164adca6b6cea539aed8b68b..9de5bf61f1fad1fd6da2b64fe350d3aa39dc5de1/navigation).

**API Changes**

- `CollectionNavType` has a new abstract `emptyCollection()` method. Override this to handle an empty collection passed in as an argument. ([Ie4d84](https://android-review.googlesource.com/#/q/Ie4d8464050a7164176c2aee55518b03a5db704ad), [b/341723133](https://issuetracker.google.com/issues/341723133))

**Bug Fixes**

- Added documentation on `NavType.serializeAsValue` and `serializeAsValues` to highlight that the final outputs should be Uri encoded. ([Ida6bd](https://android-review.googlesource.com/#/q/Ida6bd848fb1e3d8e26277eff0f214e1d40907063), [b/344943214](https://issuetracker.google.com/issues/344943214))
- Fixed crash when calling `toRoute<T>` with a null `CollectionNavType` argument. When navigating with a null `CollectionNavType`, the output argument will be the default value declared on your Serializable class, or the return value of `emptyCollection()` if there is no default value. ([I84158](https://android-review.googlesource.com/#/q/I84158320503bc04052de8f80022f83d86e23cc15), [Id630f](https://android-review.googlesource.com/#/q/Id630fb148782fbb34d3c236f5d8bb363fba7ef91), [b/342672856](https://issuetracker.google.com/issues/342672856))

### Version 2.8.0-beta02

May 29, 2024

`androidx.navigation:navigation-*:2.8.0-beta02` is released. Version 2.8.0-beta02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6a69101fd0edc8d02aa316df1f43e0552fd2d7c4..473554f275109d78164adca6b6cea539aed8b68b/navigation).

**Bug Fixes**

- Fixed `ClassCastException` crash when using `NavBackStackEntry.toRoute` with a nullable custom `NavType`. ([I1c29b](https://android-review.googlesource.com/#/q/I1c29be47a230c2c991aa24924c57b6a3f97ecd5d), [b/342239473](https://issuetracker.google.com/issues/342239473))
- Fixed Navigation back stack state restoration issues caused when attempting to restore a back stack entry that is not reachable via id from the current destination. Since routes are backed by ids, destinations built with routes were also affected. This also fixes a crash caused by calling `clearBackStack()` that had the same underlying issue. ([I423c3](https://android-review.googlesource.com/#/q/I423c3f6d8ee27be46450dcb53c28272fe0a1e085), [b/339908057](https://issuetracker.google.com/issues/339908057))

### Version 2.8.0-beta01

May 14, 2024

`androidx.navigation:navigation-*:2.8.0-beta01` is released. Version 2.8.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/fbd1ac175922f44c69a13545d194066ee428b342..6a69101fd0edc8d02aa316df1f43e0552fd2d7c4/navigation).

**API Changes**

- `SavedStateHandle.toRoute()` now takes in a `typeMap` parameter for custom argument types. ([Ie39fb](https://android-review.googlesource.com/#/q/Ie39fb2afad346928a34bc309513fa17f16cefa8c), [b/339026523](https://issuetracker.google.com/issues/339026523))
- Added a test API to `navigation-testing` to to create a `SavedStateHandle` from a Kotlin Serializable object. ([Id4867](https://android-review.googlesource.com/#/q/Id48671016d00799beb416338e2f0ac1c702f338e), [b/339080702](https://issuetracker.google.com/issues/339080702))

**Bug Fixes**

- Missing parameter docs for Navigation Kotlin DSL functions have been added. ([I26a36](https://android-review.googlesource.com/#/q/I26a36a85ab4b2d2b68c5e2ba58d3aeff6c1d54ca))

### Version 2.8.0-alpha08

May 1, 2024

`androidx.navigation:navigation-*:2.8.0-alpha08` is released. Version 2.8.0-alpha08 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/a0c81b50a8c175a7992821bb8eff152cc37e7a3c..fbd1ac175922f44c69a13545d194066ee428b342/navigation).

**Safe Args in Navigation Compose**

- The work to support compile time type safety for [Navigation Compose](https://developer.android.com/develop/ui/compose/navigation) and users of the [Navigation Kotlin DSL](https://developer.android.com/guide/navigation/design/kotlin-dsl) based on Kotlin Serialization has completed and previously experimental APIs are now stable. ([Iea94d](https://android-review.googlesource.com/#/q/Iea94de164795b79e99b8f1c2661e06ca6639b2bc), [I0eb0d](https://android-review.googlesource.com/#/q/I0eb0db9fe1dc51c25545d5ef2e915e181d3a9dae), [I873b7](https://android-review.googlesource.com/#/q/I873b7d2beee8a589858e84f8e6f95f295c51e6b9), [I3a64b](https://android-review.googlesource.com/#/q/I3a64b21c11307c1cb409e2bb47e292021d55c0b7), [I6c3a2](https://android-review.googlesource.com/#/q/I6c3a2109d99a3c40102b8a81d7a8bc17746c6a93), [I11f0b](https://android-review.googlesource.com/#/q/I11f0bb08a3f2f220f3ba8ba2d72890cd16e56ef3), [Ic3032](https://android-review.googlesource.com/#/q/Ic30322fdcc6ab6abd383758d996d4007e1bf6375), [I8d394](https://android-review.googlesource.com/#/q/I8d3948948e68b65f05c5bb943daba3deda64db2e), [I95710](https://android-review.googlesource.com/#/q/I95710b70ebbfa839f1809df21049d5c50ab74c4c), [Ice060](https://android-review.googlesource.com/#/q/Ice0608f7b128f367760d4617d6b7f770d46618c7), [Id0e55](https://android-review.googlesource.com/#/q/Id0e55c3e938d28c034aa2b6f2a23e815b0d8bfb9), [I45f8b](https://android-review.googlesource.com/#/q/I45f8b649fc3f5e9d738c432c4a53f23db7ab931e), [Idcdaf](https://android-review.googlesource.com/#/q/Idcdaf353295d64d8162a8e2f792ccd2cdaccee4a), [If5380](https://android-review.googlesource.com/#/q/If5380f1943f2a3dc1ff733ed3cfab5f1328c618a), [I08b23](https://android-review.googlesource.com/#/q/I08b231168eaedeabcd4add210daa96a99dc5807e), [Ia5c59](https://android-review.googlesource.com/#/q/Ia5c59da2d7d4e40db08e4fe29167ecc543df8a95), [b/188693139](https://issuetracker.google.com/issues/188693139))

This functionality uses [Kotlin Serialization](https://kotlinlang.org/docs/serialization.html) to allow you to define destinations in your navigation graph via type safe objects and data classes:

      // Define a home destination that doesn't take any arguments
      @Serializable
      object Home

      // Define a profile destination that takes an ID
      @Serializable
      data class Profile(val id: String)

      // Now define your NavHost using type safe objects
      NavHost(navController, startDestination = Home) {
          composable<Home> {
              HomeScreen(onNavigateToProfile = { id ->
                  navController.navigate(Profile(id))
              })
          }
          composable<Profile> { backStackEntry ->
              val profile: Profile = backStackEntry.toRoute()
              ProfileScreen(profile)
          }
      }

See the [Navigation Compose meet Type Safety blog post](https://medium.com/androiddevelopers/navigation-compose-meet-type-safety-e081fb3cf2f8) for more information.

**New Features**

- The `navigation-fragment-compose` artifact now provides a `LocalFragment` composition local to composable methods within a `ComposableFragment`. ([If35e5](https://android-review.googlesource.com/#/q/If35e5405bbd94fd5f45c1cc0dfe3d74278d64a09))
- `NavType` now has built-in support for Lists of Int, String, Boolean, Float, and Long. ([I4b6dd](https://android-review.googlesource.com/#/q/I4b6dd5ee05083c9b920eb886354384a9f55dc4aa), [Ia914c](https://android-review.googlesource.com/#/q/Ia914c3739d9c3659909826b9eeaed7f74da39345), [b/188693139](https://issuetracker.google.com/issues/188693139))

### Version 2.8.0-alpha07

April 17, 2024

`androidx.navigation:navigation-*:2.8.0-alpha07` is released. Version 2.8.0-alpha07 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/02b55f664eba38e42e362e1af3913be1df552d55..a0c81b50a8c175a7992821bb8eff152cc37e7a3c/navigation).

**New Features**

- Adds a new `navigation-fragment-compose` artifact that includes a `ComposableNavHostFragment` alternative to `NavHostFragment` that allows you to add `composable` destinations to your Navigation XML files. Each `composable` destination must be expressed as a top-level, no argument `@Composable` method whose fully qualified name is used as the `android:name` attribute on each destination. When navigating to one of these destinations, a containing fragment is created to display the composable content. ([I0ef2e](https://android-review.googlesource.com/#/q/I0ef2e5897128d18d1b374f3617c7095022ca7c0e), [b/265480755](https://issuetracker.google.com/issues/265480755))

      // In HomeScreen.kt
      @Composable
      fun HomeScreen() {
        // Your Composable content here
      }

      // In your navigation.xml
      <composable
        android:id="@+id/home_screen"
        android:name="com.example.HomeScreenKt\$HomeScreen" />

**API Changes**

- Support for Safe Args in Navigation Compose using an approach based on Kotlin Serialization continued. These APIs are *not finished* and are marked with the `ExperimentalSafeArgsApi` annotation. This annotation will be removed when the entire API surface is complete in a future release. ([Iefd95](https://android-review.googlesource.com/#/q/Iefd951a986bd24057701fa2be24298fe691e0929), [I409c8](https://android-review.googlesource.com/#/q/I409c87eea0b64195a49980c115a3581a52d3e975), [I5b5ac](https://android-review.googlesource.com/#/q/I5b5ac494f3d444d6d11f17d7c60168c6c094390e), [I7e753](https://android-review.googlesource.com/#/q/I7e753bebb4576fc9ddb2872b8b11cd97e1b4efe3), [I960f8](https://android-review.googlesource.com/#/q/I960f8941527db5a4f6a527b303bbd22f56d368bc), [I3eabd](https://android-review.googlesource.com/#/q/I3eabd8a83cb2153c3d3bc03a58cd02d7d8e7293d), [I8ed5a](https://android-review.googlesource.com/#/q/I8ed5a1d9e9d7aeac6ea3f3993777425a47f597ef), [Ied2c9](https://android-review.googlesource.com/#/q/Ied2c9c8208cd7adc5c2e848b2e166d857afc8165), [I9b73c](https://android-review.googlesource.com/#/q/I9b73c5cafcb80ea92d6ecb03677a5128fb7fb944), [I554db](https://android-review.googlesource.com/#/q/I554db9e95f298f0c0ca51d4b7dc76087c20f9272), [Ib3aba](https://android-review.googlesource.com/#/q/Ib3aba24336deb730aabd222f37eaefefca8006cf), [Ia668d](https://android-review.googlesource.com/#/q/Ia668dffcae8b255bf5db75b6c149983d973d2b06), [b/188693139](https://issuetracker.google.com/issues/188693139))

### Version 2.8.0-alpha06

April 3, 2024

`androidx.navigation:navigation-*:2.8.0-alpha06` is released. Version 2.8.0-alpha06 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/a57d7d17753695012b58c9ce7ad55a8d39157e62..02b55f664eba38e42e362e1af3913be1df552d55/navigation).

**API Changes**

- Support for Safe Args in Navigation Compose using an approach based on Kotlin Serialization has begun. These APIs are **not finished** and are marked with the `ExperimentalSafeArgsApi` annotation. This annotation will be removed when the entire API surface is complete in a future release. ([I644e7](https://android-review.googlesource.com/#/q/I644e72c129b4daca1a46fa428c31ab47c1b85a31), [I98896](https://android-review.googlesource.com/#/q/I988961680ed82f45623dba5bb162abb4b139b7c3), [I2a1c5](https://android-review.googlesource.com/#/q/I2a1c5774acd0df889dd1962aa04dd3bb3a48404d), [I43a51](https://android-review.googlesource.com/#/q/I43a5123b9efd91a36b9fbaf4e27eef874884f9e7), [I836a1](https://android-review.googlesource.com/#/q/I836a1559471fca7594653ea9e4e6a53b0d1b7ff0), [Ic5eec](https://android-review.googlesource.com/#/q/Ic5eec01d3e3ac195db2b9a717bcc58bdc55af652), [I39407](https://android-review.googlesource.com/#/q/I394079e5daad4d7d2beb427fc42e2a211cb89222), [I24e41](https://android-review.googlesource.com/#/q/I24e4116e5accdcb6ef432f6e4bb808b803c48b01), [If9e14](https://android-review.googlesource.com/#/q/If9e14e8c4d04bbb57f873a305a7314d235ab8af9), [Ibb13e](https://android-review.googlesource.com/#/q/Ibb13e8d564e505bb082a173d1d2a2525193968a6), [If44d3](https://android-review.googlesource.com/#/q/If44d34757c454d628e2e73794047a5a23c37308a), [Icb70f](https://android-review.googlesource.com/#/q/Icb70f85a4fdfd7b8c472bd4a282e446e86ae8dde), [I8972f](https://android-review.googlesource.com/#/q/I8972f003efa07fd275d397bf31237d6b3f3e38d1), [I1d432](https://android-review.googlesource.com/#/q/I1d4328c2ff048d4e1d889f973e2ec0dc3979cadb), [Icf32b](https://android-review.googlesource.com/#/q/Icf32b1b03afd4c11031cc3ca8316c7a9c10c131a), [I20a14](https://android-review.googlesource.com/#/q/I20a147e037ff80f0cab34276275890e683fa8367), [I262aa](https://android-review.googlesource.com/#/q/I262aa2eeccc792ae6c1c5b70e6b3d82eed3a3049), [I7de99](https://android-review.googlesource.com/#/q/I7de995f0621e397de971a943fcf97b6f3fe9f566), [I35990](https://android-review.googlesource.com/#/q/I35990712aac099ab47f86ca10af8d8886aca5327), [I1033d](https://android-review.googlesource.com/#/q/I1033daaefa341eb1054a9b00b0fce0b5317adca8), [b/188693139](https://issuetracker.google.com/issues/188693139))

**Bug Fixes**

- `NavHost` now used `Alignment.TopStart` as the default contentAlignment argument. This puts it in line with the default for `AnimatedContent` and fixes some instances of an unexpected scale from center transition. ([I09e72](https://android-review.googlesource.com/#/q/I09e7260d31cb571039629acd83b58eaf000a2493), [b/330111602](https://issuetracker.google.com/issues/330111602))
- When flicking the predictive back gesture while using Navigation Compose, the `NavHost` will now correctly complete the custom transition instead of immediately finishing. ([I99017](https://android-review.googlesource.com/#/q/I990176d94411c24e5ce6f59b1aeb9b6be39cca6f), [b/327292110](https://issuetracker.google.com/issues/327292110))

### Version 2.8.0-alpha05

March 20, 2024

`androidx.navigation:navigation-*:2.8.0-alpha05` is released. Version 2.8.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/638a8d3a474af45f6ad5fdc3d6d1836ea42d1778..a57d7d17753695012b58c9ce7ad55a8d39157e62/navigation).

**New Features**

- You can now pass arguments to `NavGraph`'s `startDestination` directly in the `startDestination` route without relying on `defaultValue`. This applies to nested `NavGraph` `startDestinations` as well. ([I0e0b5](https://android-review.googlesource.com/#/q/I0e0b5a7c2bf2e77a8d7a46c91974509104e742a9), [b/109505019](https://issuetracker.google.com/issues/109505019), [b/188693139](https://issuetracker.google.com/issues/188693139))

**API Changes**

- Added new abstract `CollectionNavType<T>` class, a subclass of `NavType<T>` for collection-based arguments such as list, arrays, maps. ([Ic6d63](https://android-review.googlesource.com/#/q/Ic6d63bfaf44a35708e63a091265a84f339579e78), [b/188693139](https://issuetracker.google.com/issues/188693139))
- All of the default `NavType` arrays (`IntArrayType`, `LongArrayType`, `FloatArrayType`, `BoolArrayType`, and `StringArrayType`) are now of type `CollectionNavType` ([Idcf79](https://android-review.googlesource.com/#/q/Idcf796fd63e0ef2fc17cf40ccee98ac64c3b6641), [b/188693139](https://issuetracker.google.com/issues/188693139))
- `NavType` now provides a new open `valueEquals` API that determines if two values of the same type are equal to one another. ([I6cb97](https://android-review.googlesource.com/#/q/I6cb97c9b4a9992c5358f76c6940c2d9b78149f26), [b/327229511](https://issuetracker.google.com/issues/327229511))

**Bug Fixes**

- Query parameters in deep links now allows values in the form of curly braces around argument name (i.e. `{argName}`) as valid values for string-based `NavTypes`. This fixes an issue where such a value would be considered invalid (or absence of value) for all types. ([I18302](https://android-review.googlesource.com/#/q/I183028e2f77d63158a9a567c43da016722397cb8), [b/327274038](https://issuetracker.google.com/issues/327274038))
- `NavController` functions that support routes such as `navigate` or `popBackStack` can now properly match routes filled with arguments of Array `NavTypes`. ([Iea805](https://android-review.googlesource.com/#/q/Iea8056fe8293e65a80ed53d0e0522967fdb12af1), [b/327229511](https://issuetracker.google.com/issues/327229511))

### Version 2.8.0-alpha04

March 6, 2024

`androidx.navigation:navigation-*:2.8.0-alpha04` is released. Version 2.8.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e1b82c49c59d8e976ce558aba5586f6c61bc9054..638a8d3a474af45f6ad5fdc3d6d1836ea42d1778/navigation).

**New Features**

- You can now specify the `SizeTranform` for your transitions in Navigation Compose by defining them as part of the initialization for the `composable` and/or `navigation` functions. ([I91062](https://android-review.googlesource.com/#/q/I91062221a47601b40ced80dc1a31f170351e9f5a), [b/296912651](https://issuetracker.google.com/issues/296912651))

**Bug Fixes**

- Fixed an issue where `NavHost` in Compose Navigation failed to properly show the transition when using System Back without a gesture. ([Iceeae](https://android-review.googlesource.com/#/q/Iceeae260189dd12af8cb3fe690523646a90f57de), [b/325998468](https://issuetracker.google.com/issues/325998468))

### Version 2.8.0-alpha03

February 21, 2024

`androidx.navigation:navigation-*:2.8.0-alpha03` is released. [Version 2.8.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ca2a8cf8da3a3502fccc593974f8085653e38261..e1b82c49c59d8e976ce558aba5586f6c61bc9054/navigation)

**API Changes**

- `NavBackStackEntry.savedStateHandle` is now marked as `@MainThread` as it uses code that is required to be on the main thread anyway. ([Ibb988](https://android-review.googlesource.com/#/q/Ibb98890fa424cb8193f7be2e98e74fbd124eef88), [b/299523245](https://issuetracker.google.com/issues/299523245))

**Bug Fixes**

- Fixed an issue in Navigation that caused `NavGraph` ViewModels to be `DESTROYED` too soon because the associated entry's `ViewModel` was not part of the saved state. ([Ib6bb7](https://android-review.googlesource.com/#/q/Ib6bb7d1d2f1af928a23a2647b1800eb4bb37d39d), [b/317581849](https://issuetracker.google.com/317581849))

**Dependency Update**

- Navigation Compose now depends on [Compose 1.7.0-alpha03](https://developer.android.com/releases/compose-animation#1.7.0-alpha03).

### Version 2.8.0-alpha02

February 7, 2024

`androidx.navigation:navigation-*:2.8.0-alpha02` is released. [Version 2.8.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/51191bc12f96f233fc08995e1b4e8ff8b88bc7ce..ca2a8cf8da3a3502fccc593974f8085653e38261/navigation)

**New Features**

- Navigation Compose now provides support for Predictive in-app back via the new `SeekableTransitionState` APIs from compose-animation. This allows you to use the back gesture to see the previous destination with your custom Transition before deciding to either commit the transaction via the completed gesture or cancel. ([I8b8e9](https://android-review.googlesource.com/#/q/I8b8e96ed158952c8d8b52a3bc90f495c4254552b))

### Version 2.8.0-alpha01

January 24, 2024

`androidx.navigation:navigation-*:2.8.0-alpha01` is released. [Version 2.8.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/0d7cf764d03cdb757f2b9eba55d0871a61833fbb..51191bc12f96f233fc08995e1b4e8ff8b88bc7ce/navigation)

**Bug Fixes**

- Fixed `BackStackState` leak where multiple `saveState` calls on a destination would result in multiple states to be saved, but only the first one could be restored. ([I598b0](https://android-review.googlesource.com/#/q/I598b01c379f61818e96126fb8e3d3ef1f9d084cd), [b/309559751](https://issuetracker.google.com/issues/309559751))
- Fixed an issue where non-String arguments would not be properly displayed when using the `NavigationUI` helpers to populate the title of app bars. ([#636](https://github.com/androidx/androidx/pull/636), [b/316676794](https://issuetracker.google.com/316676794))

**Dependency Update**

- Navigation Compose now depends on [Compose `1.7.0-alpha01`](https://developer.android.com/jetpack/androidx/releases/compose-animation#1.7.0-alpha01) fixing an issue that could cause an unexpected scale animation. ([b/297258205](https://issuetracker.google.com/issues/297258205))

**External Contribution**

- Thanks [SimonMarquis](https://github.com/SimonMarquis) for fixing the display issue for non-String arguments when using the `NavigationUI` helpers to populate the title of app bars.

## Version 2.7.7

### Version 2.7.7

February 7, 2024

`androidx.navigation:navigation-*:2.7.7` is released. [Version 2.7.7 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/0d7cf764d03cdb757f2b9eba55d0871a61833fbb..ac8c84b6a2138a6755bafc2b2e56dbddbaf45542/navigation)

**Bug Fixes**

- Backported from [Navigation `2.8.0-alpha01`](https://developer.android.com/jetpack/androidx/releases/navigation#2.8.0-alpha01): Fixed `BackStackState` leak where multiple `saveState()` calls on a single `NavBackStackEntry` would result in multiple states being saved, but only the first saved state could be restored. ([I598b0](https://android-review.googlesource.com/#/q/I598b01c379f61818e96126fb8e3d3ef1f9d084cd), [b/309559751](https://issuetracker.google.com/issues/309559751))
- Backported from [Navigation `2.8.0-alpha01`](https://developer.android.com/jetpack/androidx/releases/navigation#2.8.0-alpha01): Fixed an issue where non-String arguments would not be properly displayed when using the `NavigationUI` helpers to populate the title of app bars. ([#636](https://github.com/androidx/androidx/pull/636), [b/316676794](https://issuetracker.google.com/316676794))

**External Contribution**

- Thanks [SimonMarquis](https://github.com/SimonMarquis) for fixing the display issue for non-String arguments when using the `NavigationUI` helpers to populate the title of app bars.

## Version 2.7.6

### Version 2.7.6

December 13, 2023

`androidx.navigation:navigation-*:2.7.6` is released. [Version 2.7.6 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/93793630001ce27b6709c8bb6b73711313cc9d5d..0d7cf764d03cdb757f2b9eba55d0871a61833fbb/navigation)

**Bug Fixes**

- The `NavGraph` `equals()` function now correctly considers the nodes of the other graph instead of just the calling one. This will ensure that graphs that have nodes with different ids will no longer be considered equal ([I401cb](https://android-review.googlesource.com/#/q/I401cb2f6f71d0bc914afeea6057e0d8c34dfc840), [b/311414915](https://issuetracker.google.com/issues/311414915))

## Version 2.7.5

### Version 2.7.5

November 1, 2023

`androidx.navigation:navigation-*:2.7.5` is released. [Version 2.7.5 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ace3a9ea98b0b126ae715bacad4d4e65853b3a83..93793630001ce27b6709c8bb6b73711313cc9d5d/navigation)

**Performance Improvements**

- Greatly improved the performance (both in terms of time and number of allocations) of comparing two graphs. This means that calls such as `setGraph` which internally compare the new graph to the existing one are much faster and result in fewer skipped frames. Thank you [Michał Z](https://github.com/mzgreen) for the thorough analysis that led to this improvement. ([I6ad62](https://android-review.googlesource.com/#/q/I6ad62bef1fb9bbbe8a91839a6e24e1f85a8982e2))
- `NavHost` will now render the start destination on the first composition pass instead of needing to wait for the second pass to read updated state. ([I439a7](https://android-review.googlesource.com/#/q/I439a7fe894907b1ebee251134113acb08973083c), [b/304852206](https://issuetracker.google.com/issues/304852206))

**Bug Fixes**

- Fixed an issue where your back stack would be popped if you called `setGraph` more than once with the exact same graph only if there was a destination in your graph that contained an action linking two destinations. ([Ieaed7](https://android-review.googlesource.com/#/q/Ieaed7edf02f70696cd0a3558cfe8d7960d1cddd4))
- Dialogs that were navigated to and dismissed in quick succession will no longer leak into the list of `NavController.visibleEntries`. ([I67586](https://android-review.googlesource.com/#/q/I67586735d33659e524ca7b2e4ae44b2df3494f3e), [b/287969970](https://issuetracker.google.com/issues/287969970))
- When an entry is popped followed by a configuration change, the entry's `ViewModel` will now be cleared properly if `saveState` is false. ([Idf242](https://android-review.googlesource.com/#/q/Idf242239ceeb731c3375ef507a2cc854d85743c7), [b/298164648](https://issuetracker.google.com/issues/298164648))
- Fixed an issue where `NavController` could handle the same deep link more than once if the back stack was entirely empty before a configuration change or call to `setGraph` only when the incoming Intent had the `FLAG_ACTIVITY_NEW_TASK` flag set. ([I73c7f](https://android-review.googlesource.com/#/q/I73c7f78a55eb283ac4b2fa7b10f6ea05a8fd8db7))

**Dependency Updates**

- Navigation with Fragments now depends on [Fragment 1.6.2](https://developer.android.com/jetpack/androidx/releases/fragment#1.6.2), fixing an issue where the `ViewModel` instances of nested fragments would not be cleared when calling `clearBackStack`.

## Version 2.7.4

### Version 2.7.4

October 4, 2023

`androidx.navigation:navigation-*:2.7.4` is released. [Version 2.7.4 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9b231e7159d02a45b1489dc2bbe3957077565c18..ace3a9ea98b0b126ae715bacad4d4e65853b3a83/navigation)

**New Features**

- Added support for `popUpTo` to use routes with arguments to allow popping back to a specific entry that uses those exact arguments, matching the support found in `popBackStack`. ([I731f4](https://android-review.googlesource.com/#/q/I731f4cf31dff5832e1203265c0420ac7baa10d49), [b/299255572](https://issuetracker.google.com/issues/299255572))

**Bug Fixes**

- Fix issue where interrupting a navigate with another navigate with `popUpTo` will cause `FragmentNavigator` to crash. ([I3c848](https://android-review.googlesource.com/#/q/I3c8483110b22e6e7d4b31cde88f2391784d9007d), [b/301887045](https://issuetracker.google.com/issues/301887045))
- Fixed issue where system back press caused the `currentDestination` to not be updated correctly to match the displayed Fragment. ([Id0d6c](https://android-review.googlesource.com/#/q/Id0d6ca28ac2e6c8521784bf0bf569efee7a862dc), [b/289877514](https://issuetracker.google.com/issues/289877514))
- `DialogFragment` lifecycle will now properly move to `RESUMED` state when the dialog above it is dismissed. ([I88f0d](https://android-review.googlesource.com/#/q/I88f0d4833a14e21a0f3855c7f0346864a1b3fba7), [b/301811387](https://issuetracker.google.com/issues/301811387))

## Version 2.7.3

### Version 2.7.3

September 20, 2023

`androidx.navigation:navigation-*:2.7.3` is released. [Version 2.7.3 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/33b98d60f650a2e97f01fff71ce0eef1c8a3b2d7..9b231e7159d02a45b1489dc2bbe3957077565c18/navigation)

**Bug Fixes**

- Fixed an issue in Navigation with Fragments that caused the `visibleEntries` list to contain incorrect entries. ([I5caa9](https://android-review.googlesource.com/#/q/I5caa9af1b5bd7084e76d7daf9515f7430bf2489d), [b/288520638](https://issuetracker.google.com/288520638))
- Fixed an issue that caused Floating Window destination (i.e. `Dialogs`, `Bottomsheets`, etc) to never get a `RESUMED` Lifecycle callback. ([I3b866](https://android-review.googlesource.com/#/q/I3b866a44291e7bd7af742562ae0619cd83929a1a), [b/287505132](https://issuetracker.google.com/287505132))

## Version 2.7.2

### Version 2.7.2

September 6, 2023

`androidx.navigation:navigation-*:2.7.2` is released. [Version 2.7.2 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/fd8660753c8ba907ddedda62ae5a37ba7bceffc0..33b98d60f650a2e97f01fff71ce0eef1c8a3b2d7/navigation)

**Bug Fixes**

- Navigation now depends on [Lifecycle `2.6.2`](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.6.2), fixing an interaction between `rememberSaveable` and Navigation Compose's `NavHost` that would cause the `rememberSaveable` state of destinations and any `ViewModel` owned `SavedStateHandle` instances from being properly restored after process death and recreation. ([b/298059596](https://issuetracker.google.com/issues/298059596), [b/289436035](https://issuetracker.google.com/issues/289436035))
- Fixed an issue when showing multiple dialogs in Navigation Compose simultaneously where the partially obscured dialogs (e.g., not the topmost dialog) would be in the `CREATED` Lifecycle state rather than the `STARTED` state. ([aosp/2728520](https://android-review.googlesource.com/c/platform/frameworks/support/+/2728520), [b/289257213](https://issuetracker.google.com/issues/289257213))
- Fixed an issue when showing multiple dialogs in Navigation Compose simultaneously where dismissing the topmost dialog would cause the new topmost dialog to be stuck in the `STARTED` Lifecycle state rather than correctly moving to `RESUMED`. ([aosp/2629401](https://android-review.googlesource.com/c/platform/frameworks/support/+/2629401), [b/286371387](https://issuetracker.google.com/issues/286371387))
- Navigation Safe Args no longer instantiates its task eagerly if it is not actually being executed. ([I0e385](https://android-review.googlesource.com/#/q/I0e385ae46f667c2b72cad31ca8c8c84aa8965605), [b/260322841](https://issuetracker.google.com/issues/260322841))

**Dependency Update**

- Navigation Compose now depends on Compose 1.5.1.

## Version 2.7.1

### Version 2.7.1

August 23, 2023

`androidx.navigation:navigation-*:2.7.1` is released. [Version 2.7.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ac88ab16827b2945b6f026fe517f8e300cfbd0b2..fd8660753c8ba907ddedda62ae5a37ba7bceffc0/navigation)

**Bug Fixes**

- Fixed an issues in Navigation with Compose where when using a `Scaffold` it was possible to get an error for trying to access a `Lifecycle.State.DESTROYED` `ViewModel`. ([I1dc11](https://android-review.googlesource.com/#/q/I1dc115fc2b454d68c1a23c78e72707d6d4c739a5), [b/268422136](https://issuetracker.google.com/issues/268422136))

## Version 2.7.0

### Version 2.7.0

August 9, 2023

`androidx.navigation:navigation-*:2.7.0` is released. [Version 2.7.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a554ff273c1449c2dc482c764272981cef7496f1..ac88ab16827b2945b6f026fe517f8e300cfbd0b2/navigation)

**Important changes since 2.6.0**

**Animations from Accompanist**

Now that `AnimatedContent` is stable, we were able to move the code from [Accompanist Navigation Animation](https://google.github.io/accompanist/navigation-animation/) back into Navigation Compose itself.

This means all of the support for setting custom transitions that existed in `AnimatedNavHost` is directly supported in `NavHost`.

No additional changes will be made to Accompanist Navigation Animation and we'll be formally deprecating it soon, along with guidance on how to migrate back to Navigation Compose itself, but it'll be the inverse of the [migration guide](https://google.github.io/accompanist/navigation-animation/#migration) with no other API changes required if you're already using the latest Accompanist alpha (`0.31.2-alpha`). ([b/197140101](https://issuetracker.google.com/197140101))

**Bug Fixes**

- NavHost in Navigation Compose now correctly intercepts system back calls even after the Activity has been STOPPED and RESUMED. ([Icb6de](https://android-review.googlesource.com/#/q/Icb6deab996d122487243f0d3d775af8c15fc7c25), [b/279118447](https://issuetracker.google.com/279118447))

**Dependency Updates**

- Navigation now depends on Compose `1.5.0` up from `1.1.0`.

### Version 2.7.0-rc01

July 26, 2023

`androidx.navigation:navigation-*:2.7.0-rc01` is released. [Version 2.7.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5ec99c7e5f3bc9f81382e788f9ff4151dcb73bc1..a554ff273c1449c2dc482c764272981cef7496f1/navigation)

**Bug Fixes**

- Fixed an issue where the `EnterTransition` and `ExitTransition` lambdas created as part of the `NavHost` could potentially remain in memory even after the `NavHost` is removed from composition. ([I893d0](https://android-review.googlesource.com/#/q/I893d0a0e36b512afe60a5af892cd84995af02015))

**Known Issues**

- There is an issue from Navigation 2.6.x that when navigating with popUpTo it is possible to cause an `IllegalArgumentException`. It is possible that this exception can be avoided by restructuring your graph, similar to the advice suggested [here](https://issuetracker.google.com/287133013#comment4). ([b/287133013](https://issuetracker.google.com/287133013))

### Version 2.7.0-beta02

June 28, 2023

`androidx.navigation:navigation-*:2.7.0-beta02` is released. [Version 2.7.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6e6b38595c10b8edd5d40a9bc9d4e294fc4f8160/navigation)

**Bug Fixes**

- Navigation Compose now has the right z-order for custom transitions that use navigate with the `popUpTo` option.([/Ib1c3a](https://android-review.googlesource.com/#/q/Ib1c3a329755b2cbec3d28568d03d73e5aa9b9128), [b/285153947](https://issuetracker.google.com/285153947))

### Version 2.7.0-beta01

June 7, 2023

`androidx.navigation:navigation-*:2.7.0-beta01` is released. [Version 2.7.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8414543ac278cf2f64d4c73dc7d336cb0af05fb8..73f902dee011bfe400d8a0330bfd8d4bb632065f/navigation)

**Bug Fixes**

- `NavHost` in Navigation Compose now correctly intercepts system back calls even after the `Activity` has been `STOPPED` and `RESUMED`. ([Icb6de](https://android-review.googlesource.com/#/q/Icb6deab996d122487243f0d3d775af8c15fc7c25), [b/279118447](https://issuetracker.google.com/issues/279118447))

### Version 2.7.0-alpha01

May 24, 2023

`androidx.navigation:navigation-*:2.7.0-alpha01` is released. [Version 2.7.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9b9f336027bb825e6916e31ac2d761c53751420d..8414543ac278cf2f64d4c73dc7d336cb0af05fb8/navigation)

**Animations from Accompanist**

Now that `AnimatedContent` is stable, we were able to move the code from [Accompanist Navigation Animation](https://google.github.io/accompanist/navigation-animation/) back into Navigation Compose itself.

This means all of the support for setting custom transitions that existed in `AnimatedNavHost` is directly supported in `NavHost`.

No additional changes will be made to Accompanist Navigation Animation and we'll be formally deprecating it soon, along with guidance on how to migrate back to Navigation Compose itself, but it'll be the inverse of the [migration guide](https://google.github.io/accompanist/navigation-animation/#migration) with no other API changes required if you're already using the latest Accompanist alpha (`0.31.2-alpha`). ([b/197140101](https://issuetracker.google.com/issues/197140101))

**Bug Fixes**

- From [Navigation `2.6.0-rc02`](https://developer.android.com/jetpack/androidx/releases/navigation#2.6.0-rc02): Fixed an issue with Navigation in Fragments where navigating with `popUpTo` and popping a fragment off the back stack without recreating its view would cause system back to stop working. ([Ieb8d4](https://android-review.googlesource.com/#/q/Ieb8d4e6a18f8c223ff3193ea4348fb6065e9de94), [b/281726455](https://issuetracker.google.com/issues/281726455))

**Dependency Updates**

- Navigation now depends on Compose `1.5.0-beta01`.

## Version 2.6.0

### Version 2.6.0

June 7, 2023

`androidx.navigation:navigation-*:2.6.0` is released. [Version 2.6.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/40ef6498a60cb43bab0aaed607cbff5d4d6156cb..e6702c06ff2c1c7fa8c3aee245f93921d2b50af7/navigation)

**Important changes to Navigation since 2.5.0**

- `NavBackStackEntry`'s `arguments` and the `arguments` passed to an `OnDestinationChangedListener` are now only a copy of the immutable arguments that were created when you navigated to the destination. This means any changes made to those Bundles will not be reflected in subsequent accesses to the `arguments` or other `OnDestinationChangedListener` instances.
- `NavDeepLink` now supports default values for arrays, which allows support for repeated query params that will map to the argument's array type. `NavType` also now includes a default method which can be overridden to combine two parsed values.
- Custom subclasses of `NavType` can now override `serializeAsValue` to serialize a value into a String, allowing both serialization and deserialization (via `parseValue`) to be entirely encapsulated in the `NavType` class. `StringType` now overrides this method to call `Uri.encode` on the given `String`.

**Important changes to Navigation Compose since 2.5.0**

- When previewing a composable with `NavHost`, it will now show the NavGraph's `startDestination` by default.
- `NavController.popBackStack(route)`, `NavController.getBackStackEntry(route)`, `NavController.clearBackStack(route)` now all support routes with arguments partially or fully filled in. Note that the arguments have to be an exact match with the entry's arguments.
- Attempting to create an empty `NavDeepLink` using the `navDeepLink` Kotlin DSL will now result in a lint warning indicating that a deep link needs an uri, action, and/or mimetype to be valid.

**Important changes to Navigation with Fragments since 2.5.0**

- `NavHostFragment` no longer intercepts the system back button itself. This allows the underlying `FragmentManager` to handle system back. This allows [Fragment `1.7.0-alpha01`](https://developer.android.com/jetpack/androidx/releases/fragment#1.7.0-alpha01) and higher to provide an In-App Predictive Back animation on Android U devices.
- When using Navigation with Fragments, attempting to manually do a `FragmentTransaction` that adds a fragment to the `FragmentManager`'s back stack will now throw an `IllegalArgumentException`. You should always add fragments via the `navigate()` API.
- When using the exact string `${applicationId}` as the placeholder in the `app:data` and `app:dataPattern` attributes in the activity element of a navigation XML file, the placeholder will be automatically filled in with the `packageName` of the context upon inflation.
- The `FragmentNavigator` now uses the transition APIs when navigating and popping `NavBackStackEntries`. This means that the `NavBackStackEntry` `Lifecycle` will now wait for the entering and exiting fragment special effects to complete before moving their final `Lifecycle.State`.
- The `DialogFragmentNavigator` now uses the transition APIs when navigating and popping `NavBackStackEntries`. This means that the `NavBackStackEntry` `Lifecycle` will now wait for the `DialogFragment` `Lifecycle` to move to `DESTROYED` before moving to `DESTROYED` itself.
- `NavHostFragment` now allows you to retrieve the `NavController` as soon as the `NavHostFragment` is attached to the `FragmentManager`, rather than only after `onCreate()`.
- Navigation's support for Dynamic Feature Modules now depend on the granular Play Feature Delivery Library.
- Navigation Safe Args now depends on Android Gradle Plugin version 7.3.0. This means it is now only compatible with versions 7.3.0+.

**Important changes to NavigationUI since 2.5.0**

- When passing the ID of a navigation graph to `AppBarConfiguration` (such as via a `Menu`), `NavigationUI` now only considers the start destination of that navigation graph as a top level destination, rather than incorrectly marking every destination within the graph as a top level destination. The behavior of passing the ID of an individual destination is unchanged. This same functionality is available to your own code via the new `isTopLevelDestination` function on `AppBarConfiguration`.
- The `setupWithNavController` integrations in `NavigationUI` for working with the top app bar will now parse `R.string` values for `ReferenceType` arguments found in your `android:label` into their String values instead of outputting the auto-generated resource integer.
- `NavigationUI` now provides logs when it fails to navigate via a selected `MenuItem`.

### Version 2.6.0-rc02

May 24, 2023

`androidx.navigation:navigation-*:2.6.0-rc02` is released. [Version 2.6.0-rc02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9b9f336027bb825e6916e31ac2d761c53751420d..40ef6498a60cb43bab0aaed607cbff5d4d6156cb/navigation)

**Bug Fixes**

- Fixed an issue with Navigation in Fragments where navigating with `popUpTo` and popping a fragment off the back stack without recreating its view would cause system back to stop working. ([Ieb8d4](https://android-review.googlesource.com/#/q/Ieb8d4e6a18f8c223ff3193ea4348fb6065e9de94), [b/281726455](https://issuetracker.google.com/issues/281726455))

### Version 2.6.0-rc01

May 10, 2023

`androidx.navigation:navigation-*:2.6.0-rc01` is released. [Version 2.6.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/01bd392d5702480f8bfe61a8f8bbbea64cf362a0..9b9f336027bb825e6916e31ac2d761c53751420d/navigation)

**Bug Fixes**

- Fixed an issue in Navigation with fragments where removing a fragment via navigate with `popUpTo` in its `onResume()` lifecycle callback would cause an `IllegalStateException`. ([I21884](https://android-review.googlesource.com/#/q/I21884c268cf213caacabe19db38fd49a1ac829fa), [b/279644470](https://issuetracker.google.com/issues/279644470))

### Version 2.6.0-beta01

April 19, 2023

`androidx.navigation:navigation-*:2.6.0-beta01` is released. [Version 2.6.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1691115db9e0e4fbbaa2d2250992d98c61de9ed6..01bd392d5702480f8bfe61a8f8bbbea64cf362a0/navigation)

**New Features**

- `NavBackStackEntry` now provides a custom `toString` implementation. ([Iff00b](https://android-review.googlesource.com/#/q/Iff00bfa2c625e9828d5c9cf19c566069fffc6afe))

**Bug Fixes**

- When using Navigation with Fragments, attempting to manually do a `FragmentTransaction` that adds a fragment to the `FragmentManager`'s back stack will now throw an `IllegalArgumentException`. You should always add fragments via the `navigate()` API. ([I6d38e](https://android-review.googlesource.com/#/q/I6d38e3fac4b7552881655d18304d5efec6168d03))
- When there is a `navigate` that adds an entry and a `popBackStack` that removes it in the same frame, the resulting top entry on the back stack will now consistently make it back to the `RESUMED` `Lifecycle.State`. ([Id8067](https://android-review.googlesource.com/#/q/Id80678cf8856ca2de55c8adbc19b33fa0f8fbec9), [b/276495952](https://issuetracker.google.com/issues/276495952))

### Version 2.6.0-alpha09

April 5, 2023

`androidx.navigation:navigation-*:2.6.0-alpha09` is released. [Version 2.6.0-alpha09 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f50d0aafadd4964d658f64172cbfc3f78371efc8..a200cb82769634cecdb118ec4f0bfdf0b086e597/navigation)

**Bug Fixes**

- Fixed checks for invalid route such that if a `NavDestination` contains non-nullable `NavArgument`, this destination's route must contain placeholders for args named the same as the non-nullable `NavArgument`. ([Ic62bf](https://android-review.googlesource.com/#/q/Ic62bfa7c99202fa789dd0733bca834743f1ad39c), [b/274697949](https://issuetracker.google.com/issues/274697949))
- Deeplink navigations based on `Action/MimeType` will now fail if the navigation operation is missing a non-nullable `NavArgument` required by the `NavDestination` that the `Action/MimeType` matches with. ([Ibfa17](https://android-review.googlesource.com/#/q/Ibfa17dd8043e478e330af5cbb4df865b8e494836), [b/271777424](https://issuetracker.google.com/issues/271777424))
- When `NavController` sets a graph with the same route and destinations as the previous graph, it now properly replaces its current graph nodes and its back stack destinations with new instances. This fixes a crash when using `onLaunchSingleTop` without saving state in Navigation Compose. This also fixes an error where navigating to destinations associated with the root graph builds and incorrect back stack. ([I5bc58](https://android-review.googlesource.com/q/I5bc582e315578ee53383596070ee3ea4a23aed69), [b/275258161](https://issuetracker.google.com/275258161), [b/275407804](https://issuetracker.google.com/275407804))

### Version 2.6.0-alpha08

March 22, 2023

`androidx.navigation:navigation-*:2.6.0-alpha08` is released. [Version 2.6.0-alpha08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bf83b7ca1e086138c9ffa3ed2a530db3b038c79a..5e7d256f82fbafb6d059ab7b18fddd87c7531553/navigation)

**New Features**

- `NavHostFragment` now allows you to retrieve the `NavController` as soon as the `NavHostFragment` is attached to the `FragmentManager`, rather than only after `onCreate()`. ([Ic6382](https://android-review.googlesource.com/#/q/Ic638294d888c7c2002b6107d248d2d423a5614ee), [b/220186282](https://issuetracker.google.com/issues/220186282))

**Bug Fixes**

- Fixed a `NullPointerException` when popping a nested graph that includes a non-nullable argument. ([6b3581](https://android.googlesource.com/platform/frameworks/support/+/6b358154b794a0456b089ac8e548bfb830dd6c22), [b/249988437](https://issuetracker.google.com/249988437))
- When using system back after doing a navigate with `popUpTo`, the state of the `NavController` will pop to the correct entry. ([I3a8ec](https://android-review.googlesource.com/#/q/I3a8ec072ba6d1655ab054cc081961825909088e6), [b/270447657](https://issuetracker.google.com/issues/270447657))
- `FragmentNavigator` will now properly pop entries when the back stack is popped via system back or `popBackStack()` and whether or not the transaction uses effects for the fragment. ([I81bdf](https://android-review.googlesource.com/#/q/I81bdf764c4dfb070b74017f00bbd7ba740f831c4))
- Adding fragments to the `FragmentNavigator`'s `FragmentManager` without using navigation will no longer cause a crash. ([b17204](https://android.googlesource.com/platform/frameworks/support/+/b17204359581a71c427d7519a6cfc1825141ed72), [b/274167493](https://issuetracker.google.com/274167493))

**Dependency Updates**

- Navigation now depends on [Lifecycle `2.6.1`](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.6.1). ([586fe7](https://android.googlesource.com/platform/frameworks/support/+/586fe7d84e657d9bbc6d3cb3cbb8954f715df557))
- Navigation now depends on [SavedState `1.2.1`](https://developer.android.com/jetpack/androidx/releases/savedstate#1.2.1). ([078e4e](https://android.googlesource.com/platform/frameworks/support/+/078e4ef4d6b3475ed3a453ea7ba0d03e6bdc02c3))
- Navigation now depends on [ProfileInstaller `1.3.0`](https://developer.android.com/jetpack/androidx/releases/profileinstaller#1.3.0). ([512f0c](https://android.googlesource.com/platform/frameworks/support/+/512f0c047e135deb054d7764677f981ffdbb1817))

### Version 2.6.0-alpha07

March 8, 2023

`androidx.navigation:navigation-*:2.6.0-alpha07` is released. [Version 2.6.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/87533b4ff06971ed59028936cd9b6da988cd4522..bf83b7ca1e086138c9ffa3ed2a530db3b038c79a/navigation)

**Bug Fixes**

- The `getBackStackEntry`, `popBackStack`, `clearBackStack` API variants that take routes now take route patterns with nullable arguments and nullable query params ([I22294](https://android-review.googlesource.com/#/q/I222940d306f94c737600eb0381228c7594808bfa), [b/269302500](https://issuetracker.google.com/issues/269302500))
- Fixed an issue where calling `clearBackStack()` from the `NavController` would not clear the saved state in the fragment manager associated with the cleared back stack. ([Ic1cce](https://android-review.googlesource.com/#/q/Ic1cce69633d6f954f7a2f2600a7426bbb241713f), [b/271190202](https://issuetracker.google.com/issues/271190202))
- Fixed a regression in 2.6.0-alpha06 that caused the wrong `MenuItem` in the `BottomNavigationView` to be highlighted when using System back between tabs. ([I634f6](https://android-review.googlesource.com/#/q/I634f6047b7016bcb8b690047605a6f66b2dc1438), [b/270447657](https://issuetracker.google.com/issues/270447657))
- Fixed regression in 2.6.0-alpha06 that caused `NavBackStackEntry`s not to be moved to the RESUMED state when using `Animation`s. ([Ib3589](https://android-review.googlesource.com/#/q/Ib35896636c187da5bd11ea06234a3ea815fdeb68), [b/269646882](https://issuetracker.google.com/issues/269646882))

### Version 2.6.0-alpha06

February 22, 2023

`androidx.navigation:navigation-*:2.6.0-alpha06` is released. [Version 2.6.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/2ea70540638fa56f90e00b5a8b84781a400a49a1..87533b4ff06971ed59028936cd9b6da988cd4522/navigation)

**New features**

- When previewing a composable with `NavHost`, it will now show the NavGraph's `startDestination` by default. ([I2b89f](https://android-review.googlesource.com/#/q/I2b89f0e3957f9727912b94e20efdfb6b115b97e9))

**API Changes**

- All `NavController` `navigate` overloads are now annotated with `@MainThread` to ensure that they are called on the main thread. ([I2c0b0](https://android-review.googlesource.com/#/q/I2c0b03cf115708fd40d0eee6359bae7302141105), [b/263427111](https://issuetracker.google.com/issues/263427111))

**Bug Fixes**

- Fixed a crash when attempting to navigate while using Dynamic Fragment Navigation. ([I3ee29](https://android-review.googlesource.com/#/q/I3ee29ea33f2cc7f7221b79d4d17399c725a6a4df), [b/268360479](https://issuetracker.google.com/issues/268360479))
- Fixed bug where navigating to another fragment via system back button does not update bottom bar to the correct selected item ([If559f](https://android-review.googlesource.com/#/q/If559faaccdf57f49f637eafe7be8a069d217db81), [b/269044426](https://issuetracker.google.com/issues/269044426))

**Known Issues**

- When using Navigation with Fragments, the `NavBackStackEntry`'s Lifecycle fails to reach `RESUMED` when using [`Animation`](https://developer.android.com/reference/android/view/animation/Animation) APIs. ([b/269646882](https://issuetracker.google.com/269646882))
- When using Navigation with Fragments, and navigating with `BottomNavigation`, if you attempt to restore a back stack with multiple entries, the `BottomMenuItem` is not correctly updated. ([b/270447657](https://issuetracker.google.com/270447657))
- When using Navigation with Fragments, after restoring the state the `NavBackStackEntry` `Lifecycle` does not get `DESTROYED` when its fragment is `DESTROYED` . ([b/270610768](https://issuetracker.google.com/270610768))

### Version 2.6.0-alpha05

February 8, 2023

`androidx.navigation:navigation-*:2.6.0-alpha05` is released. [Version 2.6.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a1e318590b217ecfce1b2de17eed2f18b6a680bb..2ea70540638fa56f90e00b5a8b84781a400a49a1/navigation)

**New Features**

- `NavController.popBackStack(route)`, `NavController.getBackStackEntry(route)`, `NavController.clearBackStack(route)` now all support routes with arguments partially or fully filled in. Note that the arguments have to be an exact match with the entry's arguments. ([Iebd28](https://android-review.googlesource.com/#/q/Iebd2816e5a0a10b324bc03d51a25b4cf58922864), [Ic678c](https://android-review.googlesource.com/#/q/Ic678cf67db0f47f7b2778b039242773767735f2c), [I3b37b](https://android-review.googlesource.com/#/q/I3b37b5d2dd9423bf095cce5632f5208abfe49d70), [b/257514373](https://issuetracker.google.com/issues/257514373))
- The `FragmentNavigator` now uses the transition APIs when navigating and popping `NavBackStackEntries`. This means that the `NavBackStackEntry` `Lifecycle` will now wait for the entering and exiting fragment special effects to complete before moving their final `Lifecycle.State`. ([I3cb19](https://android-review.googlesource.com/#/q/I3cb193646619c371ce4024b19d709fbbfada32be), [b/238686802](https://issuetracker.google.com/issues/238686802))
- The `DialogFragmentNavigator` now uses the transition APIs when navigating and popping `NavBackStackEntries`. This means that the `NavBackStackEntry` `Lifecycle` will now wait for the `DialogFragment` `Lifecycle` to move to `DESTROYED` before moving to `DESTROYED` itself. ([I53ee5](https://android-review.googlesource.com/#/q/I53ee5ff20ea8dd04dfffbce10015504a9bdca135), [b/261213893](https://issuetracker.google.com/issues/261213893))

**API Changes**

- `NavigatorState` now provides the `prepareForTransition` API to allow `Navigator`s to move `NavBackStackEntries` to intermediate `Lifecycle.State`s. ([I42c21](https://android-review.googlesource.com/#/q/I42c214311d1ab67f589f5749a62133ec564044f4), [b/238686802](https://issuetracker.google.com/issues/238686802))
- You can now access the back stack associated with a `NavGraphNavigator` or a `ComposeNavigator` via a `backstack` property. `ComposeNavigator` also now exposes the `onTransitionComplete()` callback to mark a `NavBackStackEntry` that has executed a navigate or `popBackStack` operation as complete. ([I02062](https://android-review.googlesource.com/#/q/I02062bf587450aad6d99fd2bbca19dd3c178d4fe), [I718db](https://android-review.googlesource.com/#/q/I718dbcf2549d755b283292002cdfd9df9dc4bf26), [b/257519195](https://issuetracker.google.com/issues/257519195))

**Bug Fixes**

- Navigator state will now no-op when using the `push/popWithTransition` APIs and the entry is already being handled. ([Iadbfa](https://android-review.googlesource.com/#/q/Iadbfaef1a0d6269bcc974058e09aed30de3611a7), [b/261213893](https://issuetracker.google.com/issues/261213893))
- When using `launchSingleTop` with a nested `NavGraph` all destinations starting from original destination to its `startDestination` will only be properly added to the top of the backstack. ([Id4bea](https://android-review.googlesource.com/#/q/Id4bea16aff3dd776826fc6d746475e293eb64b0e), [b/253256629](https://issuetracker.google.com/issues/253256629))
- Navigation will now properly replace the `DialogFragment` instance when navigating to the same destination with the `launchSingleTop` flag set to true. ([I45b5a](https://android-review.googlesource.com/#/q/I45b5a3bd6f538c1b97573f269414ecf6e06e4d81), [b/149572817](https://issuetracker.google.com/issues/149572817))
- Navigation SafeArgs will no longer cause a compilation error when using arguments that are exactly 19 characters long. ([Id60bc](https://android-review.googlesource.com/#/q/Id60bcbd017753261a97b002d76960e1e2b1d18ed), [b/257110095](https://issuetracker.google.com/issues/257110095))

### Version 2.6.0-alpha04

November 9, 2022

`androidx.navigation:navigation-*:2.6.0-alpha04` is released. [Version 2.6.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/548c8ac2570ae6cf15798fea1380491f7d93796b..a1e318590b217ecfce1b2de17eed2f18b6a680bb/navigation)

**New Features**

- Custom subclasses of `NavType` can now override `serializeAsValue` to serialize a value into a String, allowing both serialization and deserialization (via `parseValue`) to be entirely encapsulated in the `NavType` class. `StringType` now overrides this method to call `Uri.encode` on the given `String`. ([Ie5213](https://android-review.googlesource.com/#/q/Ie52134e58058b8b33b9b0810fab2b342dffb6ec9), [b/247637434](https://issuetracker.google.com/issues/247637434))
- `NavigationUI` now provides logs when it fails to navigate via a selected `MenuItem`. ([I2af5a](https://android-review.googlesource.com/#/q/I2af5a295550cb72c05b7e1308be8db325234bd22), [b/247730357](https://issuetracker.google.com/issues/247730357))

**Bug Fixes**

- Navigation deep links are now parsed lazily instead of on graph initialization which could improve app performance at start up. ([Iab0ab](https://android-review.googlesource.com/#/q/Iab0abc79fcc65dc435327f199df6b469d4bcee86))
- Fixed crash caused by navigating up after deep linking to a destination with null default arguments. ([I51c24](https://android-review.googlesource.com/#/q/I51c240a957f6fb6a9f91c5564551e1ee23af374f), [b/243183636](https://issuetracker.google.com/issues/243183636))

**Dependency Update**

- Navigation's support for Dynamic Feature Modules now depend on the granular Play Feature Delivery Library. ([Ib4ddc](https://android-review.googlesource.com/#/q/Ib4ddca6bdd26012bffc5426e50869338faa40d22))
- Navigation Safe Args now depends on Android Gradle Plugin version 7.3.0. This means it is now only compatible with versions 7.3.0+. ([I47e49](https://android-review.googlesource.com/#/q/I47e49a258f82d072eb3559c97ac0937cf3f1b14b))

### Version 2.6.0-alpha03

October 24, 2022

`androidx.navigation:navigation-*:2.6.0-alpha03` is released. [Version 2.6.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4586cf6e518f0c59410ef2b291e34ff9fdcff4e1..548c8ac2570ae6cf15798fea1380491f7d93796b/navigation)

**Bug Fixes**

- From [Navigation `2.5.3`](https://developer.android.com/jetpack/androidx/releases/navigation#2.5.3): `NavHost` will no longer cause a `NoSuchElementException` when there is no destination available for the `Crossfade` to compose. It will now just skip the composition. ([Ieb46e](https://android-review.googlesource.com/#/q/Ieb46e8bbcbcde6183a2ab07fba24b18756a4ae2f), [b/253299416](https://issuetracker.google.com/issues/253299416))
- From [Navigation `2.5.3`](https://developer.android.com/jetpack/androidx/releases/navigation#2.5.3): Fixed an issue where saved Compose state (e.g., usages of `rememberSaveable`) were not being forgotten and removed when a destination was popped off the back stack. ([I64949](https://android-review.googlesource.com/#/q/I649492142419b56d9ef5ab768a2cfe7662f026e2))

**Dependency Updates**

- Navigation now depends on [Fragment `1.5.4`](https://developer.android.com/jetpack/androidx/releases/fragment#1.5.4). ([Icd424](https://android-review.googlesource.com/#/q/Icd424c6aefb33f1517d47f4a5b9327ef38711b13))

### Version 2.6.0-alpha02

October 5, 2022

`androidx.navigation:navigation-*:2.6.0-alpha02` is released. [Version 2.6.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/cce7b70f6a5ebf955cf748a73c18b63228b22c74..4586cf6e518f0c59410ef2b291e34ff9fdcff4e1/navigation)

**Behavior Changes**

- When passing the ID of a navigation graph to `AppBarConfiguration` (such as via a `Menu`), `NavigationUI` now only considers the start destination of that navigation graph as a top level destination, rather than incorrectly marking every destination within the graph as a top level destination. The behavior of passing the ID of an individual destination is unchanged. This same functionality is available to your own code via the new `isTopLevelDestination` function on `AppBarConfiguration`. ([Ie936e](https://android-review.googlesource.com/#/q/Ie936ece98a80c2a13fbfb77b83a0ba86e926ebd9), [b/238496771](https://issuetracker.google.com/issues/238496771))

**Bug Fixes**

- The `navigation:navigation-fragment` component now depends on Fragment version `1.5.2`. ([I00ba4](https://android-review.googlesource.com/#/q/I00ba4999d13e3330ffd8b260dc856c6e142dd644))
- The selected menu item will no longer be updated when navigating to a `FloatingWindow` destination such as a dialog. ([I4cde8](https://android-review.googlesource.com/#/q/I4cde820ed7dd61a1a6cb7803f81e704e4b446a0b), [b/240308330](https://issuetracker.google.com/issues/240308330))

### Version 2.6.0-alpha01

September 7, 2022

`androidx.navigation:navigation-*:2.6.0-alpha01` is released. [Version 2.6.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ca314fbfe623461cccbca66d6b874e7ceedb1bb8..cce7b70f6a5ebf955cf748a73c18b63228b22c74/navigation)

**New Features**

- The `setupWithNavController` integrations in `NavigationUI` for working with the top app bar will now parse `R.string` values for `ReferenceType` arguments found in your `android:label` into their String values instead of outputting the auto-generated resource integer. ([I5f803](https://android-review.googlesource.com/#/q/I5f803f69cb9820f7be85cb7642c8fb0f475285f7), [b/167959935](https://issuetracker.google.com/issues/167959935))
- `NavDeepLink` now supports default values for arrays, which allows support for repeated query params that will map to the argument's array type. `NavType` also now includes a default method which can be overridden to combine two parsed values. ([Id68c3](https://android-review.googlesource.com/#/q/Id68c3153e38412add55a8ddef3cd9b1c339677b0), [b/209977108](https://issuetracker.google.com/issues/209977108))
- When using the exact string `${applicationId}` as the placeholder in the `app:data` and `app:dataPattern` attributes in the activity element of a navigation XML file, the placeholder will be automatically filled in with the `packageName` of the context upon inflation. ([Iaabde](https://android-review.googlesource.com/#/q/Iaabde79a03b4d9b54bf1633d4abf4c297dd30de8), [b/234223561](https://issuetracker.google.com/issues/234223561))
- Attempting to create an empty `NavDeepLink` using the `navDeepLink` Kotlin DSL will now result in a lint warning indicating that a deep link needs an uri, action, and/or mimetype to be valid. ([I08d2f](https://android-review.googlesource.com/#/q/I08d2feba9b90ee934b8834c5573914fa44d7dc45), [b/154038883](https://issuetracker.google.com/issues/154038883))

**API Changes**

- Added new `NavDestination` extension function to parse dynamic labels with arguments in the form of `android:label="{arg}"` into String. Supports `ReferenceType` arguments by parsing `R.string` values into their String values. ([I07d89](https://android-review.googlesource.com/#/q/I07d89975d5126b1da35f9eccb7c257a83749b66d), [b/236269380](https://issuetracker.google.com/issues/236269380))

**Behavior Changes**

- NavBackStackEntry's `arguments` and the `arguments` passed to an `OnDestinationChangedListener` are now only a copy of the immutable arguments that were created when you navigated to the destination. This means any changes made to those Bundles will not be reflected in subsequent accesses to the `arguments` or other `OnDestinationChangedListener` instances. ([I676f5](https://android-review.googlesource.com/#/q/I676f53df9aa311d51c5da1ae11d57b51bb149b7d))

**Bug Fixes**

- From [Navigation `2.5.2`](https://developer.android.com/jetpack/androidx/releases/navigation#2.5.2): Dynamic Navigation now properly attempts to install Activity destinations from other modules before navigating to them. ([Ia2c16](https://android-review.googlesource.com/#/q/Ia2c1645426d2f6a5958a10379a99f2aade3dd03a), [b/240292838](https://issuetracker.google.com/issues/240292838))
- From [Navigation `2.5.2`](https://developer.android.com/jetpack/androidx/releases/navigation#2.5.2): Navigation will now properly replace the Fragment instance when navigating to the same destination and setting the `launchSingleTop` flag to true. ([I5a2f1](https://android-review.googlesource.com/#/q/I5a2f15e1c2a9a4bc5bae6f5d016a9b06b76aa448), [b/237374580](https://issuetracker.google.com/issues/237374580))
- From [Navigation `2.5.2`](https://developer.android.com/jetpack/androidx/releases/navigation#2.5.2): Fixed `IllegalStateException` caused by navigating to a double nested graph that shares a parent with a new popped start destination. ([I9f7cb](https://android-review.googlesource.com/#/q/I9f7cb2445e6021c6ab4cb81d62612411249c1257), [b/243778589](https://issuetracker.google.com/issues/243778589))

## Version 2.5

### Version 2.5.3

October 24, 2022

`androidx.navigation:navigation-*:2.5.3` is released. [Version 2.5.3 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/872530398dbfbbde210f8587ef252ba61ab10a2d..7c18fd081d3256c2eb05cc540447dc8106e923be/navigation)

**Bug Fixes**

- `NavHost` will no longer cause a `NoSuchElementException` when there is no destination available for the `Crossfade` to compose. It will now just skip the composition. ([Ieb46e](https://android-review.googlesource.com/#/q/Ieb46e8bbcbcde6183a2ab07fba24b18756a4ae2f), [b/253299416](https://issuetracker.google.com/issues/253299416))
- Fixed an issue where saved Compose state (e.g., usages of `rememberSaveable`) were not being forgotten and removed when a destination was popped off the back stack. ([I64949](https://android-review.googlesource.com/#/q/I649492142419b56d9ef5ab768a2cfe7662f026e2))

### Version 2.5.2

September 7, 2022

`androidx.navigation:navigation-*:2.5.2` is released. [Version 2.5.2 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ca314fbfe623461cccbca66d6b874e7ceedb1bb8..872530398dbfbbde210f8587ef252ba61ab10a2d/navigation)

**Bug Fixes**

- Dynamic Navigation now properly attempts to install Activity destinations from other modules before navigating to them. ([Ia2c16](https://android-review.googlesource.com/#/q/Ia2c1645426d2f6a5958a10379a99f2aade3dd03a), [b/240292838](https://issuetracker.google.com/issues/240292838))
- Navigation will now properly replace the Fragment instance when navigating to the same destination and setting the `launchSingleTop` flag to true. ([I5a2f1](https://android-review.googlesource.com/#/q/I5a2f15e1c2a9a4bc5bae6f5d016a9b06b76aa448), [b/237374580](https://issuetracker.google.com/issues/237374580))
- Fixed `IllegalStateException` caused by navigating to a double nested graph that shares a parent with a new popped start destination. ([I9f7cb](https://android-review.googlesource.com/#/q/I9f7cb2445e6021c6ab4cb81d62612411249c1257), [b/243778589](https://issuetracker.google.com/issues/243778589))

**Dependency Update**

- Navigation `2.5.2` now depends on [Fragment `1.5.2`](https://developer.android.com/jetpack/androidx/releases/fragment#1.5.2). ([aosp/2178734](https://android-review.googlesource.com/c/platform/frameworks/support/+/2178734))

### Version 2.5.1

July 27, 2022

`androidx.navigation:navigation-*:2.5.1` is released. [Version 2.5.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/56365a25722236a5e107d81e22ce0d3c80861802..ca314fbfe623461cccbca66d6b874e7ceedb1bb8/navigation)

**Bug Fixes**

- `Navigation Safe Args` will no longer cause deprecation warnings in generated classes when using custom argument types that are saved in a `Bundle`. ([Id86ed](https://android-review.googlesource.com/#/q/Id86edf231b90176b5a0f03239bff628171a0284c), [b/237725966](https://issuetracker.google.com/issues/237725966))

**Dependency Updates**

- The Navigation library now depends on [Lifecycle `2.5.1`](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.5.1). ([Ib4451](https://android-review.googlesource.com/#/q/Ib44513cf0c7f96fe996b23ced62ab82da0146f21))
- The Navigation library now depends on [Activity `1.5.1`](https://developer.android.com/jetpack/androidx/releases/activity#1.5.1). ([I3efe8](https://android-review.googlesource.com/#/q/I3efe89a890713d7c9c8ecb9344c48ba4e4b881b7))
- The Navigation library now depends on [Fragment `1.5.1`](https://developer.android.com/jetpack/androidx/releases/fragment#1.5.1). ([I56177](https://android-review.googlesource.com/#/q/I561770ed155317788b7179540d336c5abf24b71b))

### Version 2.5.0

June 29, 2022

`androidx.navigation:navigation-*:2.5.0` is released. [Version 2.5.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d4d9ac459e2261cd015398c13a79548e4d10f5bf..56365a25722236a5e107d81e22ce0d3c80861802/navigation)

**Important changes since 2.4.0**

- **CreationExtras Integration** - `Navigation` now has the ability to provide a stateless `ViewModelProvider.Factory` via [Lifecycle `2.5.0`](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.5.0)'s `CreationExtras`.

**Navigation SafeArgs**

- `Navigation Safe Args` has upgraded the `Android Gradle Plugin` dependency to rely on `7.0.4`, dropping compatibility for AGP versions before `7.0`.
- Added support for the namespace build.gradle attribute to be used instead of applicationId.

**Other Changes**

- The `visibleEntries` API is no longer experimental and provides a function to retrieve all of the entries whose destination is currently visible according to the `NavController`.

### Version 2.5.0-rc02

June 15, 2022

`androidx.navigation:navigation-*:2.5.0-rc02` is released. [Version 2.5.0-rc02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c5a5a93e0561b4cdac8767f117afae230c0a3a8f..d4d9ac459e2261cd015398c13a79548e4d10f5bf/navigation)

**Bug Fixes**

- Fixed a crash caused by fast switching between bottom destinations when using the Navigation Compose `NavHost`. ([I3979a](https://android-review.googlesource.com/#/q/I3979acdda0b6715fcf96bb1948ad6f5e6ba87388), [b/234054916](https://issuetracker.google.com/issues/234054916))
- `Navigation SafeArgs` will no longer crash when using an `applicationIdSuffix` and namespace with either no `applicationId` present, or when the `applicationId` and namespace differ. ([I754b1](https://android-review.googlesource.com/#/q/I754b1fffe44bdb142ae818187cad6cd7fdc9080a), [b/233119646](https://issuetracker.google.com/issues/233119646))
- `NavArgument` now has a custom `toString()` function to show the internal values of the argument. ([I900a8](https://android-review.googlesource.com/#/q/I900a8f28b0c801109522634d00aaab16de057e83))

### Version 2.5.0-rc01

May 11, 2022

`androidx.navigation:navigation-*:2.5.0-rc01` is released. [Version 2.5.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c0a89ec374961b3015097ab307ebb8196dbe3888..c5a5a93e0561b4cdac8767f117afae230c0a3a8f/navigation)

**New Features**

- Added a new lint rule to warn against placing `<deeplink>` elements inside `<activity>` elements in your `navigation.xml` file.([Ic15a5](https://android-review.googlesource.com/#/q/Ic15a5ec165620b7ef5b3f03538cc83b5576add8d), [b/178403185](https://issuetracker.google.com/178403185))

**Bug Fixes**

- Composable scopes in `NavHost` and `DialogHost` are now disposed in the expected order, i.e. inner composabled are disposed before outer composables. ([I157e6](https://android-review.googlesource.com/#/q/I157e609fb0609265eef381f729285bf769b56a7c))
- Navigation SafeArgs now uses `PathSensitivity.RELATIVE` in the `ArgumentsGenerationTask` to allow for cache relocatability. This means the cache entry can now be re-used from a CI build to a local build. ([I5f67c](https://android-review.googlesource.com/#/q/I5f67ced6e860f301678ba9f6e77683f1061ebf59), [b/173420454](https://issuetracker.google.com/issues/173420454))
- The `UnrememberedGetBackStackEntryDetector` lint rule has been updated to ensure that the `remember` call surrounding the call to `getBackStackEntry()` also passes in a `NavBackStackEntry` object as a key.([Ib7081](https://android-review.googlesource.com/#/q/Ib708126a32c865f758d5967ea177cc9d2c7692d5), [b/227382831](https://issuetracker.google.com/227382831))

### Version 2.5.0-beta01

April 20, 2022

`androidx.navigation:navigation-*:2.5.0-beta01` is released. [Version 2.5.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7ca43e00a517eaeeedc0a21f482b17f06e3d2181..c0a89ec374961b3015097ab307ebb8196dbe3888/navigation)

**Bug Fixes**

- `DialogNavigator` now uses `popWithTransition` when executing a `dismiss()` call. This fixes a race condition when using a `ViewModel` within `dialog` destination that would cause an `IllegalStateException` when dismissing the Dialog by either using system back or tapping outside of the dialog to exit. ([Id7376](https://android-review.googlesource.com/#/q/Id7376c0b8db5be869d8ff53185e15b0603bf8582), [b/226552301](https://issuetracker.google.com/issues/226552301))

**Dependency Updates**

- Navigation now depends on [Lifecycle `2.5.0-beta01`](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.5.0-beta01), fixing an `IllegalStateException` when nesting one `NavHost` within another `NavHost` in a non-primary bottom navigation tab when using multiple back stacks.

### Version 2.5.0-alpha04

April 6, 2022

`androidx.navigation:navigation-*:2.5.0-alpha04` is released. [Version 2.5.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9b2b3d8efd5f00bd4af903bbaa926f6a712d0bd8..7ca43e00a517eaeeedc0a21f482b17f06e3d2181/navigation)

**API Changes**

- `visibleEntries` is no longer experimental. ([I4829f](https://android-review.googlesource.com/#/q/I4829fb8402901ea9e7ef31262f4b1c7ac3e26818), [b/225394514](https://issuetracker.google.com/issues/225394514))

**Bug Fixes**

- NavHost now depend on `visibleEntries` from the `NavController` to determine which entries to compose. This means that when using nested NavHost the inner `NavHost` should now properly animate out. ([I4ba2b](https://android-review.googlesource.com/#/q/I4ba2b542821154a76566f9c02cf7a95599a30f14), [b/225394514](https://issuetracker.google.com/issues/225394514))
- The `visibleEntries` `StateFlow` provided by `NavController` is now based on the entry max Lifecycle state instead of the current Lifecycle state. This means that even if the host lifecycle of the `navController` goes below STARTED, the list of visible entires will remain the same. ([I9e2a8](https://android-review.googlesource.com/#/q/I9e2a810f261e9dc1e61417b168427b3bf597fbd5), [b/225394514](https://issuetracker.google.com/issues/225394514))
- `SavedStateViewFactory` now supports using `CreationExtras` even when it was initialized with a `SavedStateRegistryOwner`. If extras are provided, the initialized arguments are ignored. ([I6c43b](https://android-review.googlesource.com/#/q/I6c43bfd75888cb4b8bdd610cd07d4962aaba37ea), [b/224844583](https://issuetracker.google.com/issues/224844583))
- `NavDeepLink` can now parse Uris with a single query parameter with no value. ([I0efe8](https://android-review.googlesource.com/#/q/I0efe8852542de7d50677499fcd7d32d905163908), [b/148905489](https://issuetracker.google.com/issues/148905489))
- Empty string are now considered as valid arguments in deep links. ([I70a0d](https://android-review.googlesource.com/#/q/I70a0d1b47db028d829014f21763f95bb76fa8e3c), [b/217399862](https://issuetracker.google.com/issues/217399862))
- `Navigation Safe Args` will no longer crash when using namespaces and no `AndroidManifest.xml` is present. ([I17ccf](https://android-review.googlesource.com/#/q/I17ccf95b5f4137762d7c3db0503ec394812e89e8), [b/227229815](https://issuetracker.google.com/issues/227229815))

### Version 2.5.0-alpha03

February 23, 2022

`androidx.navigation:navigation-*:2.5.0-alpha03` is released. [Version 2.5.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/db2ecbef194afcddfaede22e1d884a8959a9277c..9b2b3d8efd5f00bd4af903bbaa926f6a712d0bd8/navigation)

**API Changes**

- You can now pass in `CreationExtras` to `by navGraphViewModels` to create a `ViewModel`. ([I29217](https://android-review.googlesource.com/#/q/I2921777b099bc0682008bd44728f1f678ca29dbd), [b/217618359](https://issuetracker.google.com/issues/217618359))

**Bug Fixes**

- `NavDeepLinks` now properly support encoded new line characters embedded in routes/deep link URIs. ([I513d1](https://android-review.googlesource.com/#/q/I513d1fca7c3921bb3c3b006e3d88853a210bd204), [b/217815060](https://issuetracker.google.com/issues/217815060))
- `CreationExtras` will now work correctly when used with `NavBackStackEntries` to create ViewModels. ([I69161](https://android-review.googlesource.com/#/q/I6916116b1aa5d88d31e36e101040b1999f98095c), [b/217617710](https://issuetracker.google.com/issues/217617710))
- Navigation Safe Args now supports using the namespace defined in the `build.gradle` in place of the package in the AndroidManifest. ([I659ef](https://android-review.googlesource.com/#/q/I659efc0f5b74619f5fe3ffb882c96ccb360670b7), [b/217414933](https://issuetracker.google.com/issues/217414933))

### Version 2.5.0-alpha02

February 9, 2022

`androidx.navigation:navigation-*:2.5.0-alpha02` is released. [Version 2.5.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9dceceb54300ed028a7e8fc7a3454f270337ffde..db2ecbef194afcddfaede22e1d884a8959a9277c/navigation)

**Bug Fixes**

- From [Navigation `2.4.1`](https://developer.android.com/jetpack/androidx/releases/navigation#2.4.1): The `NavHostFragment` will now properly set the `OnBackPressedDispatcher` when using viewbinding with nested graphs. ([Ifbb51](https://android-review.googlesource.com/#/q/Ifbb512720e49b4cd49b1ba337f5aa6bcebd1a303), [b/214577959](https://issuetracker.google.com/issues/214577959))
- From [Navigation `2.4.1`](https://developer.android.com/jetpack/androidx/releases/navigation#2.4.1): When deep linking through multiple nested `NavGraph`s the back stack will now properly include intermediate start destinations. ([I504c0](https://android-review.googlesource.com/#/q/I504c04d2cc4381af22405266192ea0f5094f9c16), [b/214383060](https://issuetracker.google.com/issues/214383060))

### Version 2.5.0-alpha01

January 26, 2022

`androidx.navigation:navigation-*:2.5.0-alpha01` is released. [Version 2.5.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ee27dabb830fecc2bb6899cb460d977a31d90612..9dceceb54300ed028a7e8fc7a3454f270337ffde/navigation)

**New Features**

- `NavBackStackEntry` now integrates with ViewModel CreationExtras, introduced as part of [Lifecycle `2.5.0-alpha01`](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.5.0-alpha01). ([Ib9fe2](https://android-review.googlesource.com/#/q/Ib9fe2eadbad3bb89e1685e3f3409acca92ab5b95), [b/207012490](https://issuetracker.google.com/issues/207012490))

**Bug Fixes**

- Fixed an issue where accessing a `ViewModel` created via `by navGraphViewModels()` from a Fragment's `onCreate()` would fail with an `IllegalStateException`. ([I8a14d](https://android-review.googlesource.com/#/q/I8a14dd596195d4ddfa8199c8023a7aedcd286113))
- `NavDeepLink`s will no longer unnecessarily decode args twice, meaning that the proper args are now passed to your final destination. ([I31b0a](https://android-review.googlesource.com/#/q/I31b0aa2e770650f483a3f75257c57035af298d9f), [b/210711399](https://issuetracker.google.com/issues/210711399))

**Safe Args**

- Safe Args now depends on Android Gradle Plugin version 7.0.4. This means that Navigation Safe Args will no longer be compatible with Android Studio versions prior to 7.0, but is now compatible with Android Gradle Plugin 7.1.0 and higher. ([I41c88](https://android-review.googlesource.com/#/q/I41c88ee06ad827c61cb1bbdc5ba58b3d56155caf), [b/213086135](https://issuetracker.google.com/issues/213086135), [b/207670704](https://issuetracker.google.com/issues/207670704))

## Version 2.4.2

### Version 2.4.2

April 6, 2022

`androidx.navigation:navigation-*:2.4.2` is released. [Version 2.4.2 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/74c6bf00f1309f5066b20ceb18fe9493896f0eac..84af66c94fd924400737747502ac35e96743a941/navigation)

**Bug Fixes**

- Backported from [Navigation `2.5.0-alpha03`](https://developer.android.com/jetpack/androidx/releases/navigation#2.5.0-alpha03): `NavDeepLinks` now properly support encoded new line characters embedded in routes/deep link URIs. ([I513d1](https://android-review.googlesource.com/#/q/I513d1fca7c3921bb3c3b006e3d88853a210bd204), [b/217815060](https://issuetracker.google.com/issues/217815060))
- Backported from [Navigation `2.5.0-alpha03`](https://developer.android.com/jetpack/androidx/releases/navigation#2.5.0-alpha03): Navigation SafeArgs now supports using the namespace defined in the `build.gradle` in place of the package in the AndroidManifest. ([I659ef](https://android-review.googlesource.com/#/q/I659efc0f5b74619f5fe3ffb882c96ccb360670b7), [b/217414933](https://issuetracker.google.com/issues/217414933))
- Backported from [Navigation `2.5.0-alpha04`](https://developer.android.com/jetpack/androidx/releases/navigation#2.5.0-alpha04): `Navigation Safe Args` will no longer crash when using namespaces and no `AndroidManifest.xml` is present. ([I17ccf](https://android-review.googlesource.com/#/q/I17ccf95b5f4137762d7c3db0503ec394812e89e8), [b/227229815](https://issuetracker.google.com/issues/227229815))
- Backported from [Navigation `2.5.0-alpha04`](https://developer.android.com/jetpack/androidx/releases/navigation#2.5.0-alpha04): Empty string are now considered as valid arguments in deep links. ([I70a0d](https://android-review.googlesource.com/#/q/I70a0d1b47db028d829014f21763f95bb76fa8e3c), [b/217399862](https://issuetracker.google.com/issues/217399862))

## Version 2.4.1

### Version 2.4.1

February 9, 2022

`androidx.navigation:navigation-*:2.4.1` is released. [Version 2.4.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/06c50aeb46902c0559e3fdaf3bb0ea031f910e78..74c6bf00f1309f5066b20ceb18fe9493896f0eac/navigation)

**Bug Fixes**

- The `NavHostFragment` will now properly set the `OnBackPressedDispatcher` when using viewbinding with nested graphs. ([Ifbb51](https://android-review.googlesource.com/#/q/Ifbb512720e49b4cd49b1ba337f5aa6bcebd1a303), [b/214577959](https://issuetracker.google.com/issues/214577959))
- When deep linking through multiple nested `NavGraph`s the back stack will now properly include intermediate start destinations. ([I504c0](https://android-review.googlesource.com/#/q/I504c04d2cc4381af22405266192ea0f5094f9c16), [b/214383060](https://issuetracker.google.com/issues/214383060))
- Backported from [Navigation `2.5.0-alpha01`](https://developer.android.com/jetpack/androidx/releases/navigation#2.5.0-alpha01): Fixed an issue where accessing a ViewModel created via `by navGraphViewModels()` from a Fragment's `onCreate()` would fail with an `IllegalStateException`. ([I8a14d](https://android-review.googlesource.com/#/q/I8a14dd596195d4ddfa8199c8023a7aedcd286113))
- Backported from [Navigation `2.5.0-alpha01`](https://developer.android.com/jetpack/androidx/releases/navigation#2.5.0-alpha01): `NavDeepLink`s no longer unnecessarily decode args twice, meaning that the properly decoded args are now passed to your final destination. ([I31b0a](https://android-review.googlesource.com/#/q/I31b0aa2e770650f483a3f75257c57035af298d9f), [b/210711399](https://issuetracker.google.com/issues/210711399))
- Backported from [Navigation `2.5.0-alpha01`](https://developer.android.com/jetpack/androidx/releases/navigation#2.5.0-alpha01): Safe Args now depends on Android Gradle Plugin version 7.0.4. This means that Navigation Safe Args will no longer be compatible with Android Studio versions prior to 7.0, but is now compatible with Android Gradle Plugin 7.1.0 and higher. ([I41c88](https://android-review.googlesource.com/#/q/I41c88ee06ad827c61cb1bbdc5ba58b3d56155caf), [b/213086135](https://issuetracker.google.com/issues/213086135), [b/207670704](https://issuetracker.google.com/issues/207670704))

## Version 2.4.0

### Version 2.4.0

January 26, 2022

`androidx.navigation:navigation-*:2.4.0` is released. [Version 2.4.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ee27dabb830fecc2bb6899cb460d977a31d90612..06c50aeb46902c0559e3fdaf3bb0ea031f910e78/navigation)

**Important changes since 2.3.0**

- All Navigation artifacts have been rewritten in Kotlin. This has improved the nullability of classes using generics (such as `NavType` subclasses). All Kotlin extension functions that used to be part of the `-ktx` artifacts have been moved to their respective main artifacts. The `-ktx` artifacts will continue to be published, but are completely empty.
- The `navigation-fragment` artifact now contains a prebuilt implementation of a [two pane layout](https://developer.android.com/guide/topics/ui/layout/twopane) via the new `AbstractListDetailFragment`. This fragment uses a `SlidingPaneLayout` to manage a list pane (which your subclass provides) and a detail pane, which uses a `NavHostFragment` as its implementation, as seen in our [example implementation](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:navigation/integration-tests/testapp/src/main/java/androidx/navigation/testapp/TwoPaneFragment.kt).
- The `currentBackStackEntryAsFlow()` method on `NavController` provides a `Flow` that emits whenever the current `NavBackStackEntry` changes. This flow can be used as an alternative to manually managing an `OnDestinationChangedListener`.
- NavController now offers the ability to retrieve a list of all visible `NavBackStackEntry` instances as a `StateFlow` via the experimental `visibleEntries` property.
- It is now possible to extend the `NavType` class to create custom NavTypes. Custom types are supported only when building your navigation graph programmatically, such as via the [Navigation Graph Kotlin DSL](https://developer.android.com/guide/navigation/navigation-kotlin-dsl).
- Navigation now provides`findStartDestination()` and `getHierarchy()` APIs that can be used to help implement custom NavigationUI. `findStartDestination()` is an extension function on `NavGraph` that will locate the actual start destination that will be displayed when you navigate to the graph, even if the `startDestination` is itself a nested `NavGraph`. `getHierarchy()` is a function on `NavDestination` that can be used to verify if a given destination is within the hierarchy of another.

      val matchingRoute: Boolean = destination.hierarchy.any { it.route == routeToFind }

- `NavigationUI` methods that took a `BottomNavigationView` have been updated to instead take its superclass introduced in Material `1.4.0`, `NavigationBarView`. This allows these methods to be used with the `NavigationRailView`.

- When inflating an `<action>` element via XML, animation attributes can use attributes pulled from your theme using the `app:enterAnim="?attr/transitionEnter"` syntax.

- Safe Args now generates a `fromSavedStateHandle()` method for each `NavArgs` class. ([#122](https://github.com/androidx/androidx/pull/122), [b/136967621](https://issuetracker.google.com/136967621))

      class HomeViewModel(savedStateHandle: SavedStateHandle) : ViewModel() {
        // Create a HomeDestinationArgs class with type safe accessors for each argument
        // defined on your destination
        private val args = HomeDestinationArgs.fromSavedStateHandle(savedStateHandle)
      }

**Navigation Routes and the Kotlin DSL**

Previous versions of Navigation relied on each destination having a constant integer ID that would uniquely identify it from its sibling destinations and allow you to `navigate()` to that destination either directly or via an action. While this continues to be valid and useful, particularly in cases where you are defining your navigation graph in XML and can use auto-generated `R.id` constants or Safe Args (which uses those constants to generate code at build time), this system of unique integers did not capture the semantic meaning and expressiveness needed to support fully dynamic graphs built programmatically at runtime via the [Navigation Kotlin DSL](https://developer.android.com/guide/navigation/navigation-kotlin-dsl).

This release introduces a new option for uniquely identifying a destination in a navigation graph by its **route** . A **route** is a `String` that defines the unique path to a destination. All Kotlin DSL methods that took a destination ID are now deprecated and replaced with an equivalent API that takes a route.

Each route should be treated as the 'path' part of a `Uri` that defines that destination, e.g., `home`, `profile/{userId}`, `profile/{userId}/friends`, etc. When the identity of a destination is associated with a specific piece of content, those dynamic arguments should be part of the route, following the same rules as [implicit deep links](https://developer.android.com/guide/navigation/navigation-deep-link#implicit).

All `NavController` APIs that used to only take an ID now have an overload that takes a route `String`. This includes `navigate()`, `popBackStack()`, `popUpTo()`, and `getBackStackEntry()`.

This has had some API implications:

- The `popUpTo` Kotlin property on the Kotlin DSL has been deprecated in favor of `popUpToId`.
- The `getStartDestination()` API has been deprecated in favor of `getStartDestinationId()`.

Unlike when navigating by ID, navigating by route follows the same rules as [implicit deep links](https://developer.android.com/guide/navigation/navigation-deep-link#implicit) in that you can directly navigate to any destination in any nested graph, ensuring that these routes are usable in [multi-module projects](https://developer.android.com/guide/navigation/navigation-multi-module) without explicitly adding an externally visible deep link to each destination.

**Navigation Compose**

The `navigation-compose` artifact provides integration between the [Navigation Component](https://developer.android.com/navigation) and [Jetpack Compose](https://developer.android.com/jetpack/compose). It uses `@Composable` functions as the destinations in your application.

This release provides:

- A `NavHost` composable that allows you to construct your navigation graph via a Kotlin DSL, using `composable` and `dialog` destinations, plus support for optional Navigators such as those from [Accompanist Navigation Material](https://google.github.io/accompanist/navigation-material/).
- Mandatory support for crossfading between destinations. [Accompanist Navigation Animation](https://google.github.io/accompanist/navigation-animation/) can be used to control the enter and exit transitions using experimental Compose APIs.
- Scoping of a `Lifecycle` to each composable destination. Each destination only reaches the `RESUMED` state when any entering transitions finish and immediately drops to `STARTED` when any exiting transitions start, thus allowing you to avoid all `IllegalStateException` and multi-touch issues by only triggering a `navigate` call when the `Lifecycle` is `RESUMED`.
- Scoping of `ViewModel` (via the `viewModel()` API of [Lifecycle ViewModel Compose `2.4.0`](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.4.0) or `hiltViewModel()` of [Hilt Navigation Compose `1.0.0`](https://developer.android.com/jetpack/androidx/releases/hilt#hilt-navigation-compose-1.0.0) at the destination level, providing a scope that survives configuration changes and being on the back stack (when your Composable content is otherwise disposed) and a signal in the ViewModel's `onCleared()` that indicates the permanent disposal and cleaning up of state associated with that `NavBackStackEntry`.
- Scoping of `rememberSaveable` state at a destination level, ensuring that all composable state is saved and restored automatically when you return to a destination.
- Full support for saving and restoring the state of the `NavController` and its destination's state after process death and recreation.
- Automatic integration with the system back button.
- Support for passing arguments, attaching deep links to destinations, and returning a result to previous destinations.

- Compose specific helpers in `rememberNavController()` and `currentBackStackEntryAsState()` to allow [hoisting state](https://developer.android.com/jetpack/compose/state#state-hoisting) and connecting the `NavController` to composables outside of the `NavHost` (such as a bottom navigation bar).

    val navController = rememberNavController()
    Scaffold { innerPadding ->
        NavHost(navController, "home", Modifier.padding(innerPadding)) {
            composable("home") {
                // This content fills the area provided to the NavHost
                HomeScreen()
            }
            dialog("detail_dialog") {
                // This content will be automatically added to a Dialog() composable
                // and appear above the HomeScreen or other composable destinations
                DetailDialogContent()
            }
        }
    }

See the [Compose Navigation guide](https://developer.android.com/jetpack/compose/navigation) for more information.

**Multiple back stacks**

The NavController is responsible for managing the back stack of destinations, adding destinations to the back stack when you `navigate()` to them and removing them when you call `popBackStack()` or trigger the system back button. The existing [`NavOptions`](https://developer.android.com/reference/kotlin/androidx/navigation/NavOptions) class and the integration into `<action>` elements in the navigation graph XML has been expanded to support saving and restoring the back stack.

As part of this change, the `NavigationUI` methods of `onNavDestinationSelected()`, `BottomNavigationView.setupWithNavController()` and `NavigationView.setupWithNavController()` now automatically save and restore the state of popped destinations, enabling support for multiple back stacks without any code changes. When using Navigation with Fragments, this is the recommended way to integrate with multiple back stacks.

The underlying APIs for saving and restoring the state are exposed via a number of surfaces:

- In Navigation XML, the `<action>` element can now use the boolean attributes of `app:popUpToSaveState` and `app:restoreState` to save the state of any destinations popped via `app:popUpTo` and restore the state associated with the destination passed as the `app:destination`:

      <action
        android:id="@+id/swap_stack"
        app:destination="@id/second_stack"
        app:restoreState="true"
        app:popUpTo="@id/first_stack_start_destination"
        app:popUpToSaveState="true" />

- In the [`navOptions` Kotlin DSL](https://developer.android.com/reference/kotlin/androidx/navigation/package-summary#navoptions), you can add the `restoreState` boolean property and the `saveState` boolean property on the [`popUpTo` builder](https://developer.android.com/reference/kotlin/androidx/navigation/NavOptionsBuilder#popupto):

      // Use the navigate() method that takes a navOptions DSL Builder
      navController.navigate(selectedBottomNavRoute) {
        launchSingleTop = true
        restoreState = true
        popUpTo(navController.graph.findStartDestination().id) {
          saveState = true
        }
      }

- In manually building a `NavOptions` object via the [`NavOptions.Builder`](https://developer.android.com/reference/kotlin/androidx/navigation/NavOptions.Builder), you can use the `setRestoreState()` and new overload to `setPopUpTo()` that takes an additional `saveState` parameter.

      NavOptions navOptions = new NavOptions.Builder()
        .setLaunchSingleTop(true)
        .setRestoreState(true)
        .setPopUpTo(NavGraph.findStartDestination(navController.getGraph()).getId(),
          false, // inclusive
          true) // saveState
        .build();
      navController.navigate(selectedBottomNavId, null, navOptions);

- Programmatic calls to [`popBackStack()`](https://developer.android.com/reference/kotlin/androidx/navigation/NavController#popbackstack) can now include an additional `saveState` parameter.

- You can use the `clearBackStack()` method to clear any state that was saved with `popBackStack()` or `popUpToSaveState`.

In all cases, the `NavController` will save and restore the state of each `NavBackStackEntry`, including any navigation destination scoped `ViewModel` instances. The [`Navigator`](https://developer.android.com/reference/kotlin/androidx/navigation/Navigator) APIs have been updated to enable each `Navigator` to support saving and restoring their own state.

**Behavior changes**

- `NavDeepLinkBuilder` now adds `PendingIntent.FLAG_IMMUTABLE` to the `PendingIntent` returned by `createPendingIntent()`, ensuring that this API works as expected when targeting Android 12.
- Navigation now depends on [Lifecycle `2.3.1`](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.3.1) and now marks `setGraph()`, `popBackStack()`, `navigateUp()`, and `navigate()`, the methods that update the `NavBackStackEntry` `Lifecycle`, as `@MainThread`, aligning Navigation with the main thread enforcement introduced in Lifecycle `2.3.0`.
- Deep links now verify that all required arguments (those without default values) are present in the `Uri`.
- `NavDeepLink` parsed arguments now consider pound signs in the same way as question marks as a separator between path segments, preventing an argument from spanning across the pound sign.
- When generating actions, Kotlin code generated from Safe Args now puts arguments without default values before those with default values as parameters.
- When generating arguments, Safe Args now puts parameters without default values before those with default values.
- Safe-Args now depends on Android Gradle Plugin 4.2.0. This means you should no longer get the using `applicationIdTextResource` warning.

**Known issues**

- Fixed in [Navigation `2.5.0-alpha01`](https://developer.android.com/jetpack/androidx/releases/navigation#2.5.0-alpha01): accessing a `ViewModel` created via `by navGraphViewModels()` from a Fragment's `onCreate()` will fail with an `IllegalStateException`. ([b/213504272](https://issuetracker.google.com/213504272))
- Fixed in [Navigation `2.5.0-alpha01`](https://developer.android.com/jetpack/androidx/releases/navigation#2.5.0-alpha01): Safe Args 2.4.0 is incompatible with Android Gradle Plugin 7.1.0 and higher. ([b/213086135](https://issuetracker.google.com/213086135))
- Deep linking with multiple nested nav graphs doesn't correctly create the full backstack. ([b/214383060](https://issuetracker.google.com/214383060))

### Version 2.4.0-rc01

December 15, 2021

`androidx.navigation:navigation-*:2.4.0-rc01` is released. [Version 2.4.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f07d12061370a603549747200c79b60239706330..ee27dabb830fecc2bb6899cb460d977a31d90612/navigation)

**Behavior changes**

- `NavDeepLink` parsed arguments now consider pound signs in the same way as question marks as a separator between arguments. ([I21309](https://android-review.googlesource.com/#/q/I213095f3a5a34962657feb0e8631589765b0a1ca), [b/180042703](https://issuetracker.google.com/issues/180042703))

**Bug Fixes**

- Deeplinks will no longer ignore arguments with values that are the same as the name of the placeholder. ([If8017](https://android-review.googlesource.com/#/q/If8017489c9f36da2f20876313356f42ae8bfc208), [b/207389470](https://issuetracker.google.com/issues/207389470))
- `NavController` will no longer crash when popping a nested destination using transitions after the `NavController` has been restored. ([I0f7c9](https://android-review.googlesource.com/#/q/I0f7c990620f9e16cb96e2076ce0104916a47e0f0), [b/205021623](https://issuetracker.google.com/issues/205021623))
- The error message when using an invalid `startDestination` will now default to the start destination's route if one is available. ([I86b9d](https://android-review.googlesource.com/#/q/I86b9d0aff3e758729e83b08f7aa538d4547782e7), [b/208041894](https://issuetracker.google.com/issues/208041894))

**Navigation Compose Bug Fixes**

- Fixed potential crash caused by fast switching between the start destination and another destination using bottom nav menu items. ([Ic8976](https://android-review.googlesource.com/#/q/Ic89766e6f0527af0cd3e793643c38ea9e1f2a272), [b/208887901](https://issuetracker.google.com/issues/208887901))
- Dialog destination are now properly restored on top of the screen after config changes or process death. ([I4c0dc](https://android-review.googlesource.com/#/q/I4c0dce39bbbe26d05d0cb60c65c6e5fcfbbc62b2), [b/207386169](https://issuetracker.google.com/issues/207386169))
- Fixed an issue where attempting to retrieve a `ViewModel` from a dialog's `NavBackStackEntry` would fail when the dialog was dismissed. ([I6b96d](https://android-review.googlesource.com/#/q/I6b96d1ce4bcd703340c1d20968d2416c56b9fe46), [b/206465487](https://issuetracker.google.com/issues/206465487))
- Fixed an issue when using `activity` destinations with Navigation Compose's `NavHost` that would result in infinite recompositions. ([I8f64c](https://android-review.googlesource.com/#/q/I8f64c2edbd87f77662f8b92a6101c179a1eee585))
- Fixed a leak in Navigation Compose where it was holding on to a reference of the old activity after a config change or process death. ([I4efcb](https://android-review.googlesource.com/#/q/I4efcb0709b3864dde243d011548d801fcef24159), [b/204905432](https://issuetracker.google.com/issues/204905432))

**Safe Args Bug Fixes**

- `SafeArgs` no longer crashes when attempting to restore custom parcelable arrays after process death. ([I618e8](https://android-review.googlesource.com/#/q/I618e8b5027ef6c8b95c1696eddf3bdf7dd15ac4d), [b/207315994](https://issuetracker.google.com/issues/207315994))
- Fixed a bug in safe args that would not allow boolean arrays to have a `null` value. ([I8c396](https://android-review.googlesource.com/#/q/I8c396c8f174d5924bb5ee147261de158256fba94), [b/174787525](https://issuetracker.google.com/issues/174787525))

### Version 2.4.0-beta02

November 3, 2021

`androidx.navigation:navigation-*:2.4.0-beta02` is released. [Version 2.4.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4414c046f9f3ceed61638de755aac5f976f4d4b7..f07d12061370a603549747200c79b60239706330/navigation)

**API Changes**

- The handling of both explicit and implicit deep links now automatically adds the `saveState` flag when navigating to another graph, ensuring that code such as `NavigationUI.setupWithNavController` and code using multiple back stacks works as expected. ([Ic8807](https://android-review.googlesource.com/#/q/Ic8807b65fbcaf8d859f2ac35a45d508d2714231e))

**Behavior Changes**

- Deep link patterns are now compiled lazily in NavDeepLink instead of during inflation. This should improve the inflation time of navigation graphs that include deep links. ([b8d257](https://android-review.googlesource.com/#/q/b8d257d8ea213126b304813c6d70cc5986e97d3e), [b/184149935](https://issuetracker.google.com/issues/184149935))

**Bug Fixes**

- Fixed an issue where NavBackStackEntries were being pushed down to `Lifecycle.State.CREATED` after moving to `Lifecycle.State.STARTED` when the `NavHost` is added directly to the activity's `setContent()`. ([Ia5ac1](https://android-review.googlesource.com/#/q/Ia5ac1c2c7e83f90780dd85187519c08debaa6eca), [b/203536683](https://issuetracker.google.com/issues/203536683))
- Fixed a race condition where popping a `DialogFragment` destination off of the back stack before the dialog was actually shown would not actually dismiss the dialog, resulting in a crash when the errant dialog was manually dismissed by the user. ([I687e5](https://android-review.googlesource.com/#/q/I687e5c540686b7eedf96a2c8875e6e456840ca69))
- Fixed an issue where the `onNavDestinationSelected` API on `NavigationUI` would return `true` even if you didn't actually `navigate()` to that navigation graph. It now uses the same logic used internally by `setupWithNavController` to only select the `MenuItem` associated with the current destination using the `hierarchy` of the destination. ([I2b053](https://android-review.googlesource.com/#/q/I2b053225195ac72ee7e2e6aabebcbb0b97418ec0))

### Version 2.4.0-beta01

October 27, 2021

`androidx.navigation:navigation-*:2.4.0-beta01` is released. [Version 2.4.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/418e77ded6b319212f986a3d211532a4b89f2468..4414c046f9f3ceed61638de755aac5f976f4d4b7/navigation)

**New Features**

- You can now use `by navGraphViewModel` with a route as an alternative to using an ID so as to better support using the Navigation Kotlin DSL with Fragments. ([I901e3](https://android-review.googlesource.com/#/q/I901e3832099e6e2a698e41af1e5e5d9bef7634d5), [b/201446416](https://issuetracker.google.com/issues/201446416))

**API Changes**

- The `visibleEntries` API is now experimental. ([I93f6f](https://android-review.googlesource.com/#/q/I93f6fce8ecad6a57aad12aa042c1b1a5e5f9f004))

**Bug Fixes**

- ViewModels will no longer be destroyed when transitions are interrupted by navigating back and forth between the same screens ([Id52d8](https://android-review.googlesource.com/#/q/Id52d8102f24b4b7d62ca2dd4c36c74c1ab7c11e5), [b/200817333](https://issuetracker.google.com/issues/200817333))
- Nullable `NavDeepLink` arguments no longer require a default value when adding deep links to `NavDestination`s. ([I5aad4](https://android-review.googlesource.com/#/q/I5aad4e1e7cc53857d050d328d099f813bc0dd0d9), [b/201320030](https://issuetracker.google.com/issues/201320030))
- NavBackStackEntries now with different Lifecycles are not longer considered equal. This means NavHost will properly recompose all destinations when doing navigation with singleTop and when reselecting bottom menu items. ([I1b351](https://android-review.googlesource.com/#/q/I1b3510b238d3c4e6ed5cc86a6fddf795bd9acb02), [b/196997433](https://issuetracker.google.com/issues/196997433))
- Fixed an issue with `AbstractListDetailFragment` that caused the `layout_width` and `layout_weight` attributes on the list pane returned by `onCreateListPaneView()` to be incorrectly handled or ignored. ([f5fbf3](https://android-review.googlesource.com/#/q/f5fbf3227a0d9111f8d284398ad58554429046cb))
- The visual state of dialog destinations now correctly stays in sync with the `DialogFragmentNavigator`'s state. This means that manually calling the asynchronous `dismiss()` API for `DialogFragment` now properly clears all dialog destinations above the now dismissed dialog. This does not affect cases where you use `popUpTo` or `popBackStack()` to dismiss your dialog. ([I77ba2](https://android-review.googlesource.com/#/q/I77ba23fb7a816fc555d0c383213cac01cbafee43))
- `AbstractAppBarOnDestinationChangedListener` now has clearer error messaging for `onDestinationChanged()`. ([Ie742d](https://android-review.googlesource.com/#/q/Ie742de2163740a4050d4c80f3f))

### Version 2.4.0-alpha10

September 29, 2021

`androidx.navigation:navigation-*:2.4.0-alpha10` is released. [Version 2.4.0-alpha10 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1a3dcfb231517d6104969f17063fcc6c97ba6eeb..1f6bc4d47b7be46a5af151ed726e84db0a1cf9f9/navigation)

**New Features**

- NavController now offers the ability to retrieve a list of all visible `NavBackStackEntry` instances via the `visibleEntries` StateFlow ([Ia964e](https://android-review.googlesource.com/#/q/Ia964e808d2e2a2c3d3e60eea7713ce86fec7ee0d))
- `rememberNavController()` now takes a optional set of `Navigator` instances that will be added to the returned `NavController` to better support optional Navigators such as those from [Accompanist Navigation Material](https://google.github.io/accompanist/navigation-material/). ([I4619e](https://android-review.googlesource.com/#/q/I4619e6c4b47fc76c45a64c68085519fd8d18f699))

**Bug Fixes**

- Dynamic Navigation will no longer crash when the Activity is recreated. ([Ifa6a3](https://android-review.googlesource.com/#/q/Ifa6a3e2f563bbe181cb1fdfb8460217e77bb9338), [b/197942869](https://issuetracker.google.com/issues/197942869))
- Fixed an issue with the system back button that occurs only after popping back to a composable destination that contains a `NavHost`. ([3ed148](https://android-review.googlesource.com/#/q/3ed14822dae6a7c72b8a070992800e0ebc7b5f39), [b/195668143](https://issuetracker.google.com/issues/195668143))
- SafeArgs now generates the arguments for `fromBundle()` and `fromSavedStateHandle()` in the proper parameter order. ([I824a8](https://android-review.googlesource.com/#/q/I824a871363ff0aaf5fa5ef608f103582e7abfc61), [b/200059831](https://issuetracker.google.com/issues/200059831))

### Version 2.4.0-alpha09

September 15, 2021

`androidx.navigation:navigation-*:2.4.0-alpha09` is released. [Version 2.4.0-alpha09 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/47e81d1c497b8a57534a460c277855db1b0257ae..1a3dcfb231517d6104969f17063fcc6c97ba6eeb/navigation)

**New Features**

- You can now use the `clearBackStack()` method to clear any state that was saved with `popBackStack()` or `popUpToSaveState`. ([I80a0f](https://android-review.googlesource.com/#/q/I80a0f7baf982d750383a7db7aa9311b4f8e2a77d))
- You can now pass in a list of arguments and/or deep links to your nested navigation graph's builder and they will automatically be added to the resulting graph. ([I8a470](https://android-review.googlesource.com/#/q/I8a47074b68f36d9195f353ef7c726c75b8e1a73f), [b/182545357](https://issuetracker.google.com/issues/182545357))

**API Changes**

- The `navArgument` Kotlin DSL function is now part of `navigation-common` instead of `navigation-compose`. This will require updating imports to continue to use this function. ([I1d095](https://android-review.googlesource.com/#/q/I1d0958743bb7a5df957968c091e16078f3ffa8f1))

**Behavior Changes**

- When generating arguments, Safe Args now puts parameters without default values before those with default values. ([I89709](https://android-review.googlesource.com/#/q/I8970968c48deb3a1437437df9a3db696ed497372), [b/198493585](https://issuetracker.google.com/issues/198493585))

**Bug Fixes**

- When using Navigation Compose, NavGraphs will only be `DESTROYED` once all their children are `DESTROYED`. ([I86552](https://android-review.googlesource.com/#/q/I86552cc841eee95858ff23a1fce895e5d47c9746), [b/198741720](https://issuetracker.google.com/issues/198741720))
- Nullable `NavDeepLink` arguments no longer require a default value. ([Ia14ef](https://android-review.googlesource.com/#/q/Ia14ef04bfe5b25942163688f40adacc30fa7e044), [b/198689811](https://issuetracker.google.com/issues/198689811))
- Calling `setGraph()` with a new graph will now also clear any saved back stacks in addition to its previous behavior of popping the back stack. ([I97f96](https://android-review.googlesource.com/#/q/I97f96a65efea43d4341c9572c3c1c63f343ab6ed))
- Fixed an issue where `OnDestinationChangedListener` instances and the `currentBackStackEntryFlow` were not notified when using `launchSingleTop`. ([Iaaebc](https://android-review.googlesource.com/#/q/Iaaebc611c1134bec9a31a088742f66c30888f0f4))

**Dependency Updates**

- Navigation Compose now depends on [Activity Compose 1.3.1](https://developer.android.com/jetpack/androidx/releases/activity#1.3.1). ([I05829](https://android-review.googlesource.com/#/q/I05829230af5c04cb1a284a5f6c9bcb14f24b0fc1))
- Navigation Compose now depends on [Lifecycle ViewModel Compose `2.4.0-beta01`](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.4.0-beta01). ([Ib86a3](https://android-review.googlesource.com/#/q/Ib86a3ced486d87cd214b696123335ab8c5dd120b))

### Version 2.4.0-alpha08

September 1, 2021

`androidx.navigation:navigation-*:2.4.0-alpha08` is released. [Version 2.4.0-alpha08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1e0ab9e58c3c2ebe8152b7507938aef7e9c1acdc..47e81d1c497b8a57534a460c277855db1b0257ae/navigation)

**New Features**

- It is now possible to extend the `NavType` class to create custom NavTypes. Custom types are supported only when building your navigation graph programmatically, such as via the [Navigation Graph Kotlin DSL](https://developer.android.com/guide/navigation/navigation-kotlin-dsl). ([I78440](https://android-review.googlesource.com/#/q/I78440758311840441dd785cfaed6795fff2b56da), [b/196871885](https://issuetracker.google.com/issues/196871885))

**Behavior Changes**

- When generating actions, Kotlin code generated from Safe Args now puts arguments without default values before those with default values as parameters. ([Idb697](https://android-review.googlesource.com/#/q/Idb69783a3b0efe53de8f3e04a978dd6b979a0e04), [b/188855904](https://issuetracker.google.com/issues/188855904))
- Deep links now verify that all required arguments (those without default values) are present in the `Uri`. ([#204](https://github.com/androidx/androidx/pull/204), [b/185527157](https://issuetracker.google.com/issues/185527157))

**Bug Fixes**

- Using `getBackStackEntry` and `previousBackStackEntry` inside composable(), in conjunction with `remember()`, will no longer cause an exception for no destination being on the back stack. ([I75138](https://android-review.googlesource.com/#/q/I75138d24d27dac83b5301507161578ac811454e3), [b/194313238](https://issuetracker.google.com/issues/194313238))
- Navigation Compose now properly recomposes when changing back stack arguments and using `launchSingleTop=true`. ([Iebd69](https://android-review.googlesource.com/#/q/Iebd698c9e310ad84ce65238c8a5a33db86a9f1f7), [b/186392337](https://issuetracker.google.com/issues/186392337))
- There will no longer be an `ArrayIndexOutOfBoundsException` when calling `setGraph` with a graph with 13 or 29 destinations. ([I1a9f1](https://android-review.googlesource.com/#/q/I1a9f17c4616bc38dd3dd89cb1da29814c3dfd512), [b/195171984](https://issuetracker.google.com/issues/195171984))
- The SafeArgs java generator should no longer cause lint warnings when generating Args classes. ([I1a666](https://android-review.googlesource.com/#/q/I1a6661b10b8e380aaa9fcfd1fc710c35b047bd6d), [b/185843837](https://issuetracker.google.com/issues/185843837))

**External Contribution**

- Thanks [ospixd](https://github.com/osipxd) for ensuring that deep links verify that all required arguments (those without default values) are present in the `Uri`. ([#204](https://github.com/androidx/androidx/pull/204), [b/185527157](https://issuetracker.google.com/issues/185527157))

### Version 2.4.0-alpha07

August 18, 2021

`androidx.navigation:navigation-*:2.4.0-alpha07` is released. [Version 2.4.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/175c082bd7563f6414a75b30d2ce3d167c5e7f3a..1e0ab9e58c3c2ebe8152b7507938aef7e9c1acdc/navigation)

**Bug Fixes**

- Navigation Compose now properly saves state after configuration changes and when changing graphs while using the multiple back stack feature. ([If5a3d](https://android-review.googlesource.com/#/q/If5a3d68c4a610f008ab6823a3982f0d0c312083a), [b/195141957](https://issuetracker.google.com/issues/195141957))
- Re-selecting the same tab when using navigation compose with multiple back stacks will no longer result in a blank screen. ([I860dc](https://android-review.googlesource.com/#/q/I860dc9f2cc2516924c03dba491a37aa8ace99bb3), [b/194925622](https://issuetracker.google.com/issues/194925622))
- `NavHost` now observes for changes in the `Lifecycle.State` of `NavBackStackEntry`s which means using a `NavHost` in a fragment now will properly be recomposed as the lifecycle changes instead of resulting in a blank screen. ([I4eb85](https://android-review.googlesource.com/#/q/I4eb8586e4db4bebfac63525e9dcdab11b57fcff5), [b/195864489](https://issuetracker.google.com/issues/195864489))
- Fixed an issue where dismissing a `DialogFragment` would not correctly update the `NavController` state after recreating your activity (i.e., after a configuration change). ([Icd72b](https://android-review.googlesource.com/#/q/Icd72b58ece54484b576b44fc2fb9dbf68ccb9ab9))
- Fixed an issue where popping a dialog destination would not update the NavController's system back button handling, potentially causing the NavController to intercept the back button even though it does not have any back stack to pop. ([If3b34](https://android-review.googlesource.com/#/q/If3b3464fea674b146f071448373afbac49f8cdc5))
- Safe-args now automatically generates a `toSavedStateHandle` method for arguments which can be used to test your `ViewModel` code. ([If1e2d](https://android-review.googlesource.com/#/q/If1e2debe0126482e571cae59bcc89e27db63483d), [b/193353880](https://issuetracker.google.com/issues/193353880))

### Version 2.4.0-alpha06

August 4, 2021

`androidx.navigation:navigation-*:2.4.0-alpha06` is released. [Version 2.4.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/97264aa4532db7f7db1ffb3f42f3a9204971dbfc..d725303accfa9be6d5c3d61c7603ed1b9a780cbd/navigation)

**API Changes**

- The `requireSlidingPaneLayout()` and `requireDetailPaneNavHostFragment()` methods on `AbstractListDetailFragment` have been renamed to `getSlidingPaneLayout()` and `getDetailPaneNavHostFragment()`, respectively. ([I34a08](https://android-review.googlesource.com/#/q/I34a0844edbccd871c37de5caf9cd4af62a7d0821))

**Behavior Changes**

- When navigating with animations (like `Crossfade`), the new destination's `Lifecycle` will now only reach the `RESUMED` when the animation completes. ([If0543](https://android-review.googlesource.com/#/q/If0543dd1c20e7338078115e98b5585623f9b8f1c), [b/172112072](https://issuetracker.google.com/issues/172112072), [b/194301889](https://issuetracker.google.com/issues/194301889))
- Navigation Compose's `NavHost` now sets the graph as part of the first composition. ([Ieb7be](https://android-review.googlesource.com/#/q/Ieb7be7689ab5c40cfcc52fefd70a87b406ce8c60))

**Bug Fixes**

- Popping the last destination of a navigation graph no longer throws a `ClassCastException`. ([If0543](https://android-review.googlesource.com/#/q/If0543dd1c20e7338078115e98b5585623f9b8f1c), [b/172112072](https://issuetracker.google.com/issues/172112072), [b/194301889](https://issuetracker.google.com/issues/194301889))
- Fixed a `NullPointerException` that would occur when adding a deep link without a `Uri` and navigating via a route or deep link. ([938a0c](https://android-review.googlesource.com/#/q/938a0cc7f71bf0c8c7556ef7fe2f772f9d0ec07c), [b/193805425](https://issuetracker.google.com/193805425))
- Fixed an issue in Navigation Compose where a deep linked `NavBackStackEntry` would not reach the `RESUMED` state. ([I192c5](https://android-review.googlesource.com/#/q/I192c5d5922901f94ea0cf5abe7a922c0a63cc033))
- Fixed an issue where popping a dialog destination would not update the NavController's system back button handling, potentially causing the NavController to intercept the back button even though it does not have any back stack to pop. ([aosp/1782668](https://android-review.googlesource.com/c/platform/frameworks/support/+/1782668))

### Version 2.4.0-alpha05

July 21, 2021

`androidx.navigation:navigation-*:2.4.0-alpha05` is released. [Version 2.4.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/19ae3a88ff0824d615355b492cb56049e16991f2..97264aa4532db7f7db1ffb3f42f3a9204971dbfc/navigation)

**Behavior Changes**

- Navigation Compose's `NavHost` now always uses Crossfades when navigating through destinations. ([I07049](https://android-review.googlesource.com/#/q/I07049268d9c78bfbc6bb49f94bf2a1284d4f1180), [b/172112072](https://issuetracker.google.com/issues/172112072))
- You can now make changes to the graph of a NavHost. Graphs with the same startDestination and destinations in the graph will be considered equal and will not clear the `NavController` back stack. ([I0b8db](https://android-review.googlesource.com/#/q/I0b8dbcea4186232c3280c4a43be11e4fafcc6ce3), [b/175392262](https://issuetracker.google.com/issues/175392262))

**Bug Fixes**

- Fixed a `NoSuchElementException` when calling `popBackStack()` from within a `LifecycleObserver` attached to a `NavBackStackEntry` caused by reentrant updates to the NavController's state. ([I64621](https://android-review.googlesource.com/#/q/I646215354c80b1c4571c7351b782db9897d1ddc2))
- `AbstractListDetailFragment` now allows `SlidingPaneLayout` to be completely stripped from your APK when `AbstractListDetailFragment` is not used. ([I611ad](https://android-review.googlesource.com/#/q/I611adc2ebb2f61e7a51b2d9299902ff4656c6025))
- `NavGraph` and `NavDestination` now override the equals method so two objects with the same values will be considered equal. ([I166eb](https://android-review.googlesource.com/#/q/I166eb54122cabc12cc569daea8eefcf8e0ec95a7), [b/175392262](https://issuetracker.google.com/issues/175392262))

### Version 2.4.0-alpha04

July 1, 2021

`androidx.navigation:navigation-*:2.4.0-alpha04` is released. [Version 2.4.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ccf79f53033e665475116a4e78ff124df2a52c4b..19ae3a88ff0824d615355b492cb56049e16991f2/navigation)

**New Features**

- The `navigation-fragment` artifact now contains a prebuilt implementation of a [two pane layout](https://developer.android.com/guide/topics/ui/layout/twopane) via the new `AbstractListDetailFragment`. This fragment uses a `SlidingPaneLayout` to manage a list pane (which your subclass provides) and a detail pane, which uses a `NavHostFragment` as its implementation, as seen in our [example implementation](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:navigation/integration-tests/testapp/src/main/java/androidx/navigation/testapp/TwoPaneFragment.kt). ([Iac4be](https://android-review.googlesource.com/#/q/Iac4be7b764ced86cdbff3c696c2cbdf2741eb81c), [b/191276636](https://issuetracker.google.com/issues/191276636))
- The `NavHost` of the `navigation-compose` artifact now supports `dialog` destinations in addition to `composable` destinations. These dialog destinations will each be shown within a Composable `Dialog`, floating above the current `composable` destination. ([I011d0](https://android-review.googlesource.com/#/q/I011d03df5689a72e938d755c9c6da2b0f72eb162))

    val navController = rememberNavController()
        Scaffold { innerPadding ->
            NavHost(navController, "home", Modifier.padding(innerPadding)) {
                composable("home") {
                    // This content fills the area provided to the NavHost
                    HomeScreen()
                }
                dialog("detail_dialog") {
                    // This content will be automatically added to a Dialog() composable
                    // and appear above the HomeScreen or other composable destinations
                    DetailDialogContent()
                }
            }
        }

**API Changes**

- The `add` function in `NavigatorState` has been renamed to `push`. All current calls to `add()` will need to be changed to push(). ([Ie89fc](https://android-review.googlesource.com/#/q/Ie89fcbcf0753d6918f91450e322b156ff2fd6e9b), [b/172112072](https://issuetracker.google.com/issues/172112072))
- Custom `Navigator` instances can now use the `pushWithTransaction` and `popWithTransition` APIs on `NavigatorState` to push or pop a destination asynchronously. Note that this APIs are not yet used by any of the included navigators. ([Ic4d7c](https://android-review.googlesource.com/#/q/Ic4d7cc6530bf576c4d812d1fd0c5a2697874d384), [b/172112072](https://issuetracker.google.com/issues/172112072))

**Behavior Changes**

- `NavDeepLinkBuilder` now adds `PendingIntent.FLAG_IMMUTABLE` to the `PendingIntent` returned by `createPendingIntent()`, ensuring that this API works as expected when targeting Android 12. ([If8c52](https://android-review.googlesource.com/#/q/If8c522f9719dd134f6518c4241acab1a791aa656))

**Bug Fixes**

- Fixed an issue with `<include-dynamic>` where arguments passed to the graph would not be correctly passed to the dynamically included graph. ([I3e115](https://android-review.googlesource.com/#/q/I3e11572a629c34aaee290fb1255f258ebf632d75))
- Fixed a `NullPointerException` when navigating to a destination using a `string[]` argument with a default value of `@null`. ([I1fbe8](https://android-review.googlesource.com/#/q/I1fbe8da49d9652a842852778e9935e2426984ea9))
- Add ProGuard rules for `@Navigator.Name`, fixing issues when using R8 3.1 full mode. ([I2add9](https://android-review.googlesource.com/#/q/I2add9f695eede9d912de6710745a37f088050cac), [b/191654433](https://issuetracker.google.com/issues/191654433))
- SafeArgs will no longer fail when building your app with `Kotlin` versions before `1.5.0`. ([Icd1ff](https://android-review.googlesource.com/#/q/Icd1ff3c64f220f4b310934c2edf910d6aae01475), [b/190739257](https://issuetracker.google.com/issues/190739257))

### Version 2.4.0-alpha03

June 16, 2021

`androidx.navigation:navigation-*:2.4.0-alpha03` is released. [Version 2.4.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/86ff5b4bb956431ec884586ce0aea0127e189ec4..ccf79f53033e665475116a4e78ff124df2a52c4b/navigation)

**Bug Fixes**

- Fixed an issue where two `navigate()` calls were needed to navigate to an included dynamic graph. ([I7785c](https://android-review.googlesource.com/#/q/I7785c40969a40b30b34acd6eedd896b44c3200a1), [b/188859835](https://issuetracker.google.com/issues/188859835))
- Fixed a regression introduced in [Navigation `2.4.0-alpha01`](https://developer.android.com/jetpack/androidx/releases/navigation#2.4.0-alpha01) where `setupActionBarWithNavController()` would not properly remove the Up icon when you are on a top level destination. ([I5d443](https://android-review.googlesource.com/#/q/I5d4439021161f544d664a822e1c422ff60c91e1b), [b/189868637](https://issuetracker.google.com/issues/189868637))
- Fixed an `IllegalStateException` when calling `popBackStack()` after previously popping the root graph of the NavController. ([I2a330](https://android-review.googlesource.com/#/q/I2a330acdd339aece36455aa0da37d0609767552c), [b/190265699](https://issuetracker.google.com/issues/190265699))
- ProGuard rules for `by navArgs()` now properly apply when using `navigation-common` or any artifacts that depend on it. ([I68800](https://android-review.googlesource.com/#/q/I688009632403c98afe728d856ce91cd056ef32a5), [b/190082521](https://issuetracker.google.com/issues/190082521))
- An `OnDestinationChangedListener` that calls `navigate()` the first time it receives a callback now properly get a second callback with the destination it navigated to. ([Ie5f9e](https://android-review.googlesource.com/#/q/Ie5f9e0f8dec404775c99a0e90c1cde8a9e059550), [b/190228815](https://issuetracker.google.com/issues/190228815))
- Safe Args no longer crashes when using it with dynamic feature modules and AGP 7.0+. ([I69518](https://android-review.googlesource.com/#/q/I6951812da260e739a2d515fb9b3782b90c75642d), [b/189966576](https://issuetracker.google.com/issues/189966576))

**Known Issue**

- Safe Args will fail with an `Unable to find method ''java.lang.String kotlin.text.CarsKt.titleCase(char, java.util.Locale)''` error when using Gradle `6.7.0` due to a dependency on an older version of Kotlin. This can be worked around by updating to use Gradle 7.0. ([b/190739257](https://issuetracker.google.com/190739257))

### Version 2.4.0-alpha02

June 2, 2021

`androidx.navigation:navigation-*:2.4.0-alpha02` is released. [Version 2.4.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/66681ad83c328d0dd821b943bb3d375f02c1db61..86ff5b4bb956431ec884586ce0aea0127e189ec4/navigation)

**New Features**

- Routes are now supported for Activity, Fragment and Dialog destinations, as well as throughout the DynamicNavigation Kotlin DSL. ([Ib5544](https://android-review.googlesource.com/#/q/Ib5544bd128a17f0dc681e105a1ce4a8a28945bc3), [Ia617b](https://android-review.googlesource.com/#/q/Ia617ba47da5c4995fd21ce2becdf527ac6ade4e9), [I22f96](https://android-review.googlesource.com/#/q/I22f963d5b533066670384c1af7fc7556f57b4163), [b/188914648](https://issuetracker.google.com/issues/188914648), [b/188901565](https://issuetracker.google.com/issues/188901565))
- `NavigationUI` has temporarily added experimental APIs to allow opting out of saving your state. While always saving the state is the correct behavior, there are still uses of deprecated libraries (i.e. retained fragments), that cannot be supported when saving the state so this gives an opportunity for apps to slowly convert away from any unsupported APIs. ([Idf93c](https://android-review.googlesource.com/#/q/Idf93c093c0f3729148c78c1de9d36a0f10fbb31f))
- Navigation now provides`findDestination()` and `getHierarchy()` APIs that can be used to help implement custom NavigationUI. `findDestination()` is an extension function on `NavGraph` that will locate a destination within the graph. `getHierarchy()` is a function on `NavDestination` that can be used to verify if a given destination is within the hierarchy of another.([I2932f](https://android-review.googlesource.com/#/q/I2932fc4ddba6f381e5e353ee30d2233140e5a674), [b/188183365](https://issuetracker.google.com/issues/188183365))

      val matchingRoute: Boolean = destination.hierarchy.any { it.route == routeToFind }

- NavigationUI methods that took a `BottomNavigationView` have been updated to instead take its superclass introduced in Material `1.4.0`, `NavigationBarView`. This allows these methods to be used with the `NavigationRailView`. ([Ib0b36](https://android-review.googlesource.com/#/q/Ib0b36d933571daab2e94a79d524388c282a8c23c), [b/182938895](https://issuetracker.google.com/issues/182938895))

- When inflating an `<action>` element via XML, animation attributes can
  use attributes pulled from your theme using the
  `app:enterAnim="?attr/transitionEnter"` syntax. ([I07bc1](https://android-review.googlesource.com/#/q/I07bc1fbfd65e0c36c0cd8f1210efc1e82810f3dd), [b/178291654](https://issuetracker.google.com/issues/178291654))

**API Changes**

- Kotlin DSL builders that use an ID have been deprecated and should be replaced with builders that use routes ([I85b42](https://android-review.googlesource.com/#/q/I85b42c2dff5f5eddffd67f37b51c45b03f24c87a), [b/188816479](https://issuetracker.google.com/issues/188816479)) ([I9f58f](https://android-review.googlesource.com/#/q/I9f58f08400e8d7990784bdf27481c0ac2f34dedf), [b/188816479](https://issuetracker.google.com/issues/188816479))

**Bug Fixes**

- `DialogFragmentNavigator` now uses the `NavigatorState.pop()` API to inform the `NavController` when a dialog is dismissed by hitting the system back button or clicking outside of it, ensuring that the `NavController` state is always in sync with the Navigator's state. ([I2ead9](https://android-review.googlesource.com/#/q/I2ead97ae3d392d40e9312f3212e6bea02bf3343e))
- Navigation no longer gives a `ConcurrentModificationException` when
  using manipulating the list of `OnDestinationChangedListeners` from with an `onDestinationChanged` callback. ([Ib1707](https://android-review.googlesource.com/#/q/Ib17074c773ed9462c6a69ad384c23e28fa8abaf6), [b/188860458](https://issuetracker.google.com/issues/188860458))

- Safe Args no longer crashes when attempting to generate
  direction properties in Kotlin. ([Id2416](https://android-review.googlesource.com/#/q/Id2416d7d7c52888fb9ec9bdbb80afcc7d2a1bf3e), [b/188564435](https://issuetracker.google.com/issues/188564435))

- The setId method on NavDestination is now properly annotated
  with `@IdRes`, so it only accepts resource ids. ([I69b80](https://android-review.googlesource.com/#/q/I69b80a6a63c4db257385c96bd07ad21f7665dcb8))

- The int parameter of `findNode` is now `resId` instead of
  `resid`. ([I7711d](https://android-review.googlesource.com/#/q/I7711dafc332d1b06dfe48295bdf1cc05b23cf040))

**Dependency Update**

- Safe-Args now depends on Android Gradle Plugin 4.2.0. This means you should no longer get the using `applicationIdTextResource` warning. ([I6d67b](https://android-review.googlesource.com/#/q/I6d67ba2067b42b57463efe5872f345058379ab40), [b/172824579](https://issuetracker.google.com/issues/172824579))

### Version 2.4.0-alpha01

May 18, 2021

`androidx.navigation:navigation-*:2.4.0-alpha01` is released. [Version 2.4.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3a949c2a53232f2253802f435d043677db8cecba..66681ad83c328d0dd821b943bb3d375f02c1db61/navigation)

**New Features**

- The `currentBackStackEntryAsFlow()` method on `NavController` provides a `Flow` that emits whenever the current `NavBackStackEntry` changes. This flow can be used as an alternative to manually managing an `OnDestinationChangedListener`. ([I19c4a](https://android-review.googlesource.com/#/q/I19c4a18a70cb04543b50a39fc9eb35daccb8fa69), [#89](https://github.com/androidx/androidx/pull/89), [b/163947280](https://issuetracker.google.com/163947280))

**Multiple back stacks**

The NavController is responsible for managing the back stack of destinations, adding destinations to the back stack when you `navigate()` to them and removing them when you call `popBackStack()` or trigger the system back button. The existing [`NavOptions`](https://developer.android.com/reference/kotlin/androidx/navigation/NavOptions) class and the integration into `<action>` entries in the navigation graph XML has been expanded to support saving and restoring the back stack. ([b/80029773](https://issuetracker.google.com/80029773))

As part of this change, the `NavigationUI` methods of `onNavDestinationSelected()`, `BottomNavigationView.setupWithNavController()` and `NavigationView.setupWithNavController()` now automatically save and restore the state of popped destinations, enabling support for multiple back stacks without any code changes. When using Navigation with Fragments, this is the recommended way to integrate with multiple back stacks. ([Ie07ca](https://android-review.googlesource.com/#/q/Ie07ca3089faca25e56e58293b49f32b795e1f30a))

The underlying APIs for saving and restoring the state are exposed via a number of surfaces:

- In Navigation XML, the `<action>` element can now use the boolean attributes of `app:popUpToSaveState` and `app:restoreState` to save the state of any destinations popped via `app:popUpTo` and restore the state associated with the destination passed as the `app:destination`:

      <action
        android:id="@+id/swap_stack"
        app:destination="@id/second_stack"
        app:restoreState="true"
        app:popUpTo="@id/first_stack_start_destination"
        app:popUpToSaveState="true" />

- In the [`navOptions` Kotlin DSL](https://developer.android.com/reference/kotlin/androidx/navigation/package-summary#navoptions), you can add the `restoreState` boolean property and the `saveState` boolean property on the [`popUpTo` builder](https://developer.android.com/reference/kotlin/androidx/navigation/NavOptionsBuilder#popupto):

      // Use the navigate() method that takes a navOptions DSL Builder
      navController.navigate(selectedBottomNavRoute) {
        launchSingleTop = true
        restoreState = true
        popUpTo(navController.graph.startDestinationId) {
          saveState = true
        }
      }

- In manually building a `NavOptions` object via the [`NavOptions.Builder`](https://developer.android.com/reference/kotlin/androidx/navigation/NavOptions.Builder), you can use the `setRestoreState()` and new overload to `setPopUpTo()` that takes an additional `saveState` parameter.

      NavOptions navOptions = new NavOptions.Builder()
        .setLaunchSingleTop(true)
        .setRestoreState(true)
        .setPopUpTo(navController.getGraph().getStartDestinationId(),
          false, // inclusive
          true) // saveState
        .build();
      navController.navigate(selectedBottomNavId, null, navOptions);

- Programmatic calls to [`popBackStack()`](https://developer.android.com/reference/kotlin/androidx/navigation/NavController#popbackstack) can now include an additional `saveState` parameter.

In all cases, the `NavController` will save and restore the state of each `NavBackStackEntry`, including any navigation destination scoped `ViewModel` instances. The [`Navigator`](https://developer.android.com/kotlin/androidx/navigation/Navigator) APIs have been updated to enable each `Navigator` to support saving and restoring their own state.

The `ComposeNavigator` used for `composable` destinations in Navigation Compose and the `FragmentNavigator` and `DynamicFragmentNavigator` used for `<fragment>` destinations in Navigation with Fragments have both been updated to use the new Navigator APIs and support saving and restoring state.

**Navigation Routes**

A **route** is a `String` that uniquely identifies a destination. While previously only used in [Navigation Compose](https://developer.android.com/jetpack/compose/navigation), this concept has now graduated to become a part of the core Navigation APIs. This provides an alternative to using integer IDs when constructing your graph through the [Navigation Kotlin DSL](https://developer.android.com/guide/navigation/navigation-kotlin-dsl). ([b/172823546](https://issuetracker.google.com/172823546))

All APIs that used to only take an ID now have an overload that takes a route `String`. This includes `navigate()`, `popBackStack()`, `popUpTo()`, and `getBackStackEntry()`.

This has had some API implications:

- The `popUpTo` kotlin property on the Kotlin DSL has been deprecated in favor of `popUpToId`. ([I59c73](https://android-review.googlesource.com/#/q/I59c73c383b84eb2b36472966aedff1b53957e26d), [b/172823546](https://issuetracker.google.com/issues/172823546))
- The `getStartDestination()` API has been deprecated in favor of `getStartDestinationId()`. ([I0887f](https://android-review.googlesource.com/#/q/I0887ffe673bea453b69dff286d5dc142ce4ef462), [b/172823546](https://issuetracker.google.com/issues/172823546))

For developers upgrading from previous versions of Navigation Compose to Navigation Compose `2.4.0-alpha01`, this means that the following imports on extension methods are no longer necessary and should be removed:

    import androidx.navigation.compose.navigation
    import androidx.navigation.compose.createGraph
    import androidx.navigation.compose.getBackStackEntry
    import androidx.navigation.compose.navigate
    import androidx.navigation.compose.popUpTo

The `KEY_ROUTE` argument has been replaced with the `route` property on `NavDestination`, allowing you to call `navBackStackEntry.destination.route` directly.

**API Changes**

- All Navigation artifacts have been rewritten in Kotlin. This has improved the nullability of classes using generics (such as `NavType` subclasses). All Kotlin extension functions that used to be part of the `-ktx` artifacts have been moved to their respective main artifacts. The `-ktx` artifacts will continue to be published, but are completely empty. ([b/184292145](https://issuetracker.google.com/issues/184292145))
- `NavDeepLinkBuilder` now supports adding multiple distinct destinations to the generated back stack. ([I3ee0d](https://android-review.googlesource.com/#/q/I3ee0d5251ec1047774aa4e826b25a6d8cf4ec28d), [b/147913689](https://issuetracker.google.com/147913689))
- Add factory functions for `DynamicNavHostFragment` ([Icd515](https://android-review.googlesource.com/#/q/Icd51523a8f3cc3f93fffc1796c6a270bc28eaede), [b/175222619](https://issuetracker.google.com/issues/175222619))
- The unique ID of a `NavBackStackEntry` is now exposed as part of its public API. ([Ie033a](https://android-review.googlesource.com/#/q/Ie033a9056cead23ef9bcff1c52e67172c459b0f2))
- The `name` and `argument` fields and destructuring functions of `NamedNavArgument` are now public. ([#174](https://github.com/androidx/androidx/pull/174), [b/181320559](https://issuetracker.google.com/181320559))
- Introduced a new `NavBackStackEntry#provideToCompositionLocals` extension that provides the `NavBackStackEntry` to the relevant composition locals. ([#175](https://github.com/androidx/androidx/pull/175), [b/187229439](https://issuetracker.google.com/issues/187229439))

**Safe Args**

- Safe Args now generates a `fromSavedStateHandle()` method for each `NavArgs` class. ([#122](https://github.com/androidx/androidx/pull/122), [b/136967621](https://issuetracker.google.com/136967621))

      class HomeViewModel(savedStateHandle: SavedStateHandle) : ViewModel() {
        // Create a HomeDestinationArgs class with type safe accessors for each argument
        // defined on your destination
        private val args = HomeDestinationArgs.fromSavedStateHandle(savedStateHandle)
      }

- Updated Safe Args to depend on KotlinPoet `1.8.0`. ([#172](https://github.com/androidx/androidx/pull/172), [b/183990444](https://issuetracker.google.com/issues/183990444))

**Behavior Changes**

- Navigation now depends on [Lifecycle `2.3.1`](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.3.1) and now marks `setGraph()`, `popBackStack()`, `navigateUp()`, and `navigate()`, the methods that update the `NavBackStackEntry` `Lifecycle`, as `@MainThread`, aligning Navigation with the main thread enforcement introduced in Lifecycle `2.3.0`. ([b/171125856](https://issuetracker.google.com/171125856))
- Parsing Enum arguments from deep links is now case insensitive, allowing a deep link like `http://www.example.com/red` to match a `www.example.com/{color}` deep link even when the enum has the value of `RED`. ([#152](https://github.com/androidx/androidx/pull/152), [b/135857840](https://issuetracker.google.com/issues/135857840))

**Compose Compatibility**

- `androidx.navigation:navigation-compose:2.4.0-alpha01` is only compatible with Compose version `1.0.0-beta07` and above.

**Bug Fixes**

- Fixed an issue where trailing argument placeholders would take precedence over deep links that have a matching exact suffix. ([#153](https://github.com/androidx/androidx/pull/153), [b/184072811](https://issuetracker.google.com/issues/184072811))
- `NavHostFragment` now supports custom Navigators that use the same `@Navigator.Name("dialog")` as the default `DialogFragmentNavigator`. ([Ib1c2c](https://android-review.googlesource.com/#/q/Ib1c2cc38e7a621d133be1f4c3692e62913450dda), [b/175979140](https://issuetracker.google.com/175979140))
- Improved the behavior of `NavigatorProvider#addNavigator` to ensure that calling it repeatedly with the same instance does not cause issues. ([#176](https://github.com/androidx/androidx/pull/176), [b/187443146](https://issuetracker.google.com/issues/187443146))

**External Contributions**

- Thanks [simonschiller](https://github.com/simonschiller) for building support for Safe Args generating a `fromSavedStateHandle()` method for each `NavArgs` class. ([#122](https://github.com/androidx/androidx/pull/122), [b/136967621](https://issuetracker.google.com/136967621))
- Thanks [Bradleycorn](https://github.com/Bradleycorn) for making parsing Enum arguments from deep links case insensitive. ([#152](https://github.com/androidx/androidx/pull/152), [b/135857840](https://issuetracker.google.com/issues/135857840))
- Thanks [osipxd](https://github.com/osipxd) for fixing an issue where trailing argument placeholders would take precedence over deep links that have a matching exact suffix. ([#153](https://github.com/androidx/androidx/pull/153), [b/184072811](https://issuetracker.google.com/issues/184072811))
- Thanks [tatocaster](https://github.com/tatocaster) for updating Safe Args to depend on KotlinPoet `1.8.0`. ([#172](https://github.com/androidx/androidx/pull/172), [b/183990444](https://issuetracker.google.com/issues/183990444))
- Thanks [jossiwolf](https://github.com/jossiwolf) for making the `name` and `argument` fields and destructuring functions of `NamedNavArgument` public. ([#174](https://github.com/androidx/androidx/pull/174), [b/181320559](https://issuetracker.google.com/181320559))
- Thanks [jossiwolf](https://github.com/jossiwolf) for introducing a new `NavBackStackEntry#provideToCompositionLocals` extension that provides the `NavBackStackEntry` to the relevant composition locals. ([#175](https://github.com/androidx/androidx/pull/175), [b/187229439](https://issuetracker.google.com/issues/187229439))
- Thanks [jossiwolf](https://github.com/jossiwolf) for improved the behavior of `NavigatorProvider#addNavigator` to ensure that calling it repeatedly with the same instance does not cause issues. ([#176](https://github.com/androidx/androidx/pull/176), [b/187443146](https://issuetracker.google.com/issues/187443146))

## Navigation Compose Version 1.0.0

| **Note:** Navigation Compose has aligned versioning with the rest of `androidx.navigation` as of `2.4.0-alpha01`. `androidx.navigation:navigation-compose:1.0.0-alpha11` became `androidx.navigation:navigation-compose:2.4.0-alpha01`.

### Version 1.0.0-alpha10

April 7, 2021

`androidx.navigation:navigation-compose:1.0.0-alpha10` is released. [Version 1.0.0-alpha10 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/52fbd7ed5b07ca4431fa828325a1f8da45b02e51..0e6e72e136ada934db74265667417524ba0ba04f/navigation/navigation-compose)

**API Changes**

- `NavHost` now accepts a `Modifier`, which is passed down to the composable container that wraps the destination composables. ([I85aca](https://android-review.googlesource.com/#/q/I85aca06d44b0a1f55b7a8ef5ca7dae34577d28fa), [b/175125483](https://issuetracker.google.com/issues/175125483))

**Bug Fixes**

- `NavHost` now works even when an `OnBackPressedDispatcherOwner` is not found, such is the case when previewing the `NavHost`. ([I7d8b4](https://android-review.googlesource.com/#/q/I7d8b4662b2d30515a4536e212bf6631357a5357f))
- Navigation Compose now depends on [Navigation `2.3.5`](https://developer.android.com/jetpack/androidx/releases/navigation#2.3.5), fixing an issue when using `BackHandler` inside a `NavHost` destination. ([I7e63b](https://android-review.googlesource.com/#/q/I7e63b32c93deaee60b1d5e132d3fa255c3ba85e2), [b/182284739](https://issuetracker.google.com/issues/182284739))

### Version 1.0.0-alpha09

March 10, 2021

`androidx.navigation:navigation-compose:1.0.0-alpha09` is released. [Version 1.0.0-alpha09 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4b6cff92e45f1d4467086aa2c6aa0248b4883950..52fbd7ed5b07ca4431fa828325a1f8da45b02e51/navigation/navigation-compose)

**API Changes**

- `LocalViewModelStoreOwner.current` now returns a nullable `ViewModelStoreOwner` to better determine whether a `ViewModelStoreOwner` is available in the current composition. APIs that require a `ViewModelStoreOwner`, such as `viewModel()` and `NavHost`, still throw an exception if a `ViewModelStoreOwner` is not set. ([Idf39a](https://android-review.googlesource.com/#/q/Idf39af28f00e0c0522a897a1202385d21da828be))

**Bug Fixes**

- Navigation Compose now depends on [Navigation 2.3.4](https://developer.android.com/jetpack/androidx/releases/navigation#2.3.4) which includes the fix for attempting to set the same ViewModelStore object after the graph has been set. ([I65c24](https://android-review.googlesource.com/#/q/I65c24fcd5674c1ac72715c612854aac62c2eda88), [b/177825470](https://issuetracker.google.com/issues/177825470))

### Version 1.0.0-alpha08

February 24, 2021

`androidx.navigation:navigation-compose:1.0.0-alpha08` is released. [Version 1.0.0-alpha08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/602cf9bff5e74e4355760aa47d3fc73a2e6d779b..4b6cff92e45f1d4467086aa2c6aa0248b4883950/navigation/navigation-compose)

**New Features**

- `NavHost` now populates the `LocalSavedStateRegistryOwner` CompositionLocal with that destination's `NavBackStackEntry`, ensuring that any state directly saved into the `SavedStateRegistry` will be saved and restored alongside the destination. ([I435d7](https://android-review.googlesource.com/#/q/I435d70ef0cfa8059e0d490cd5e4ed141b690ec59), [b/179469431](https://issuetracker.google.com/issues/179469431))

| **Note:** Navigation Compose 1.0.0-alpha08 is only compatible with Compose 1.0.0-beta01.

### Version 1.0.0-alpha07

February 10, 2021

`androidx.navigation:navigation-compose:1.0.0-alpha07` is released. [Version 1.0.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6950aab50fe6c9f7e9d97cf865161f2d3999eb9e..602cf9bff5e74e4355760aa47d3fc73a2e6d779b/navigation/navigation-compose)

**Dependency Updates**

- Navigation Compose now depends on [Lifecycle ViewModel Compose 1.0.0-alpha01](https://developer.android.com/jetpack/androidx/releases/lifecycle#viewmodel-compose-1.0.0-alpha01) to provide `viewModel()` support to `composable` destinations. ([I7a374](https://android-review.googlesource.com/#/q/I7a374b76168a6387e585337c131a988bddcb912b))
- `NavHost` now uses the new `LocalOnBackPressedDispatcherOwner` from [Activity-Compose 1.3.0-alpha01](https://developer.android.com/jetpack/androidx/releases/activity#1.3.0-alpha01) to get the `OnBackPressedDispatcher` that is set on the `NavController`. ([I65b12](https://android-review.googlesource.com/#/q/I65b12306c42364d26e1819145ab378b02b2ff0f5))

| **Note:** Navigation Compose `1.0.0-alpha07` is only compatible with Compose `1.0.0-alpha12`.

### Version 1.0.0-alpha06

January 28, 2021

`androidx.navigation:navigation-compose:1.0.0-alpha06` is released. [Version 1.0.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6207afb1646d302c5d29c2c67d332b48db87fb27..aee18b103203a91ee89df91f0af5df2ecff356d6/navigation/navigation-compose)

**API Changes**

- Added a `getBackStackEntry(route: String)` extension method on `NavController` that returns the associated `NavBackStackEntry`. ([If8931](https://android-review.googlesource.com/#/q/If89316ee73218d779dfaa593eeba53a44d9dfb50))

| **Note:** Navigation Compose `1.0.0-alpha06` is only compatible with Compose `1.0.0-alpha11`.

### Version 1.0.0-alpha05

January 13, 2021

`androidx.navigation:navigation-compose:1.0.0-alpha05` is released. [Version 1.0.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/72f02c12e4709ab41ae0fea9a8a668d5267a1df8..6207afb1646d302c5d29c2c67d332b48db87fb27/navigation/navigation-compose)

Updated to depend on Compose 1.0.0-alpha10.

### Version 1.0.0-alpha04

December 16, 2020

`androidx.navigation:navigation-compose:1.0.0-alpha04` is released. [Version 1.0.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/10b5e9fd366c1c413d5576aed50a305d300938e1..72f02c12e4709ab41ae0fea9a8a668d5267a1df8/navigation/navigation-compose)

- Updated for compatibility with Compose `1.0.0-alpha09`.

| **Note:** Navigation Compose `1.0.0-alpha04` is only compatible with Compose `1.0.0-alpha09`.

### Version 1.0.0-alpha03

December 2, 2020

`androidx.navigation:navigation-compose:1.0.0-alpha03` is released. [Version 1.0.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/2d49f9fa892a0d067580a871f3aa0cd6764f4c3b..10b5e9fd366c1c413d5576aed50a305d300938e1/navigation/navigation-compose)

**Bug Fixes**

- Fixed an issue where `popBackStack()` and `navigateUp()` would not work after a configuration change or process death and recreation. ([Icea47](https://android-review.googlesource.com/#/q/Icea477e53970d8fcd22a698ed2feca1734503896), [b/173281473](https://issuetracker.google.com/issues/173281473))
- Navigating to a nested graph within your NavHost now works properly. ([I0948d](https://android-review.googlesource.com/#/q/I0948d85d73e1e7a9e37a43bc2f9267e0cd7b6355), [b/173647694](https://issuetracker.google.com/issues/173647694))

| **Note:** Navigation Compose `1.0.0-alpha03` is only compatible with Compose `1.0.0-alpha08`.

### Version 1.0.0-alpha02

November 11, 2020

`androidx.navigation:navigation-compose:1.0.0-alpha02` is released. [Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/234e23e470a5e7f81291f6acd12d538146dc010b..2d49f9fa892a0d067580a871f3aa0cd6764f4c3b/navigation/navigation-compose)

**API Changes**

- Navigation compose now support NavOptions for using popUpTo and launchSingleTop operations ([If96c3](https://android-review.googlesource.com/#/q/If96c3a3f99f29c6e2e88d64285b7af46ad3835c2), [b/171468994](https://issuetracker.google.com/issues/171468994))
- Added a navigation function that takes a route instead of an ID that allows you to construct nested graphs in the Navigation Compose DSL. ([I1661d](https://android-review.googlesource.com/#/q/I1661dbcd4c385ca7ea0961e00d2e6ce1a7429655))
- startDestination now comes before the route in the list of a parameters for a NavHost ([Ie620e](https://android-review.googlesource.com/#/q/Ie620e9208948db572ab70ee6be09f3dafb605bd7))
- You can now create a graph using the route as a start destination outside of a NavHost composable. ([Iceb75](https://android-review.googlesource.com/#/q/Iceb753387e02e654b0835826c8428bef78c4cf50))

### Version 1.0.0-alpha01

October 28, 2020

`android.navigation:navigation-compose:1.0.0-alpha01` is released. [Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/234e23e470a5e7f81291f6acd12d538146dc010b/navigation/navigation-compose)

**New Features**

The `navigation-compose` artifact provides integration between the [Navigation Component](https://developer.android.com/navigation) and [Jetpack Compose](https://developer.android.com/jetpack/compose). It uses `@Composable` functions as the destinations in your application.

This initial release provides:

- A `NavHost` composable that allows you to construct your navigation graph via a Kotlin DSL.
- Scoping of lifecycle, `ViewModel`, and remembered state at the destination level.
- Automatic integration with the system back button.
- Support for passing arguments, attaching deep links to destinations, and returning a result to previous destinations.
- Compose specific helpers in `rememberNavController()` and `currentBackStackEntryAsState()` to allow [hoisting state](https://developer.android.com/jetpack/compose/state#separate-internal-state-from-UI-composables) and connecting the `NavController` to composables outside of the `NavHost` (such as a bottom navigation bar).

See the [Compose Navigation guide](https://developer.android.com/jetpack/compose/navigation) for more information.

## Version 2.3.5

### Version 2.3.5

April 7, 2021

`androidx.navigation:navigation-*:2.3.5` is released. [Version 2.3.5 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ac398a3ebf3b1e2659e61710acf5220ba17dfc11..3a949c2a53232f2253802f435d043677db8cecba/navigation)

**New Features**

- When navigating using a `NavDeepLinkRequest` or `Uri`, you can now access the `Uri`, action, and mime type in the resulting destination by getting the intent from arguments via [`KEY_DEEP_LINK_INTENT`](https://developer.android.com/reference/kotlin/androidx/navigation/NavController#key_deep_link_intent), mirroring the functionality already available for external deep linking. ([I975c3](https://android-review.googlesource.com/#/q/I975c3ed3958575cd6213c0a97ef2c4c8071c7a71), [b/181521877](https://issuetracker.google.com/issues/181521877))

**Bug Fixes**

- `OnBackPressedCallbacks` added to a dispatcher with the `NavBackStackEntry` as the LifecycleOwner now properly intercept back after the Activity Lifecycle is `STOPPED`, then `STARTED` ([Iff94f](https://android-review.googlesource.com/#/q/Iff94f9efa9739fa49166ddb2dc11b50d2a4c4a8c), [b/182284739](https://issuetracker.google.com/issues/182284739))
- Deep link domain parsing is now case insensitive, ensuring that `www.example.com` matches both `www.example.com` and `www.Example.com`. Note that query parameter names are still case sensitive. ([#144](https://github.com/androidx/androidx/pull/144), [b/153829033](https://issuetracker.google.com/issues/153829033))
- Fixed a `NullPointerException` that could occur when a destination has multiple non-nullable default arguments and you navigate to that destination while only overriding a subset of those arguments. ([aosp/1644827](https://android-review.googlesource.com/c/platform/frameworks/support/+/1644827))

**Dependency Updates**

- The Navigation Safe Args Gradle Plugin now depends on Kotlin Gradle Plugin 1.4.31. ([aosp/1661058](https://android-review.googlesource.com/c/platform/frameworks/support/+/1661058), [b/181156413](https://issuetracker.google.com/issues/181156413))

**External Contribution**

- Thanks [`bentrengrove`](https://github.com/bentrengrove) for the pull request making deep link domain parsing case insensitive. ([#144](https://github.com/androidx/androidx/pull/144), [b/153829033](https://issuetracker.google.com/issues/153829033))

## Version 2.3.4

### Version 2.3.4

March 10, 2021

`androidx.navigation:navigation-*:2.3.4` is released. [Version 2.3.4 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/2295caa3f58e03d553783241bde8e36b8c14acc9..ac398a3ebf3b1e2659e61710acf5220ba17dfc11/navigation)

**New Features**

- `ReferenceType` arguments can now be properly parsed when sent as part of a deeplink URI. This supports both the raw integer value as well as hex values prefixed by `0x`. ([#127](https://github.com/androidx/androidx/pull/127), [b/179166693](https://issuetracker.google.com/issues/179166693))
- The `android:defaultValue` for an argument with `app:argType="float"` now supports integer default values, allowing you to use `android:defaultValue="0"`rather than requiring the use of `0.0`. ([#117](https://github.com/androidx/androidx/pull/117), [b/173766247](https://issuetracker.google.com/issues/173766247))

**Bug Fixes**

- Fix stuck installation progress when using Navigation's support for dynamic features. ([Ib27a7](https://android-review.googlesource.com/#/q/Ib27a77bc4572fc69cea38d738255c987449d6137), [b/169636207](https://issuetracker.google.com/issues/169636207))
- Calling `setViewModelStore` or `setLifecycleOwner` with the same object that has already been set will now be a no-op ([Idf491](https://android-review.googlesource.com/#/q/Idf491fa68c0771dd617832cefe4c03e8ea85dae7), [b/177825470](https://issuetracker.google.com/issues/177825470))
- Safe-Args now adds suppress annotations on the proper methods when using java. ([I8fbc5](https://android-review.googlesource.com/#/q/I8fbc577e6e16bc8b2441377df1a59f9f59abae56), [b/179463137](https://issuetracker.google.com/issues/179463137))

**External Contributions**

- Thanks [`JvmName`](https://github.com/JvmName) for the pull request to ensure that `ReferenceType` arguments can now be properly parsed when sent as part of a deeplink URI. ([#127](https://github.com/androidx/androidx/pull/127), [b/179166693](https://issuetracker.google.com/issues/179166693))
- Thanks [`tatocaster`](https://github.com/tatocaster) for the pull request to allow the `defaultValue` for an argument with `app:argType="float"` now supports integer default values. ([#117](https://github.com/androidx/androidx/pull/117), [b/173766247](https://issuetracker.google.com/issues/173766247))

## Version 2.3.3

### Version 2.3.3

January 27, 2021

`androidx.navigation:navigation-*:2.3.3` is released. [Version 2.3.3 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/722c6ca874bb106de216eddb5133c44b6921aaf9..2295caa3f58e03d553783241bde8e36b8c14acc9/navigation)

**Bug Fixes**

- There is no longer a crash when popping a `NavBackStackEntry` before its `Lifecycle` is moved to `CREATED`. ([Ie3ba3](https://android-review.googlesource.com/#/q/Ie3ba3e34e3e4f4982bfc87b38b1d2764d10238a0))
- Fixed regression caused by [b/171364502](https://issuetracker.google.com/issues/171364502) where navigating to an activity with an animation resource value of `0` caused a `ResourceNotFoundException`. ([I7aedb](https://android-review.googlesource.com/#/q/I7aedb282e3bd4534758035fe17bfcdb3287be604), [b/176819931](https://issuetracker.google.com/issues/176819931))

## Version 2.3.2

### Version 2.3.2

December 2, 2020

`androidx.navigation:navigation-*:2.3.2` is released. [Version 2.3.2 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/76e4783df885f268f5aa76eee474c79167279a8a..722c6ca874bb106de216eddb5133c44b6921aaf9/navigation)

**Bug Fixes**

- Fixed a regression in `NavigationUI` where using an `<activity>` destination with `onNavDestinationSelected` would fail to navigate to the Activity. ([I22e34](https://android-review.googlesource.com/#/q/I22e34487faa43e2024a407047956c18b85923b52), [b/171364502](https://issuetracker.google.com/issues/171364502))
- Fixed an issue where `navigation-dynamic-features-fragment` would result in navigating to the newly installed destination multiple times. ([aosp/1486056](https://android-review.googlesource.com/1486056), [b/169636207](https://issuetracker.google.com/169636207))
- Fixed an issue where default arguments would not be sent to `OnDestinationChangedListener` instances when using `launchSingleTop`. ([I2c5cb](https://android-review.googlesource.com/#/q/I2c5cbc0bb904880f76b2d3660f9800ec9a50fe14))
- Fixed an issue where navigating to a nested navigation graph would not create a new graph instance on the back stack. ([Ifc831](https://android-review.googlesource.com/#/q/Ifc8318d58fedcfe71ed9a486fe43f963ebb4a330))
- Fixed an issue where using `navigate()` with a `popUpTo` that removed the last destination in a navigation graph would not immediately destroy and remove the navigation graph itself from the back stack. ([I910a3](https://android-review.googlesource.com/#/q/I910a3aadd9add3932285cc9aefbb4cfc45ec178b))
- Navigation SafeArgs now uses KotlinPoet version 1.7.2 which adds support for Kotlin's explicit API mode. ([I918b5](https://android-review.googlesource.com/#/q/I918b59356727391e3caa909089aee8a19c3ea4d5))
- `NavHostFragment.findNavController(Fragment)` now also checks the root decor view of a DialogFragment in addition to the existing checks of the Fragment hierarchy and Fragment's view hierarchy. This allows you to test dialog fragments that use Navigation with `FragmentScenario` and `Navigation.setViewNavController()`. ([I69e0d](https://android-review.googlesource.com/#/q/I69e0d4f69ce830d85e0697df410e62bb6333c8ac))

## Version 2.3.1

### Version 2.3.1

October 14, 2020

`androidx.navigation:navigation-*:2.3.1` is released. [Version 2.3.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/654b8a76ea3c162fc3f9d84f3484ebadda0bbb9f..76e4783df885f268f5aa76eee474c79167279a8a/navigation)

**New Features**

- Default Animator resources have been added to Navigation UI and are recommended over the default animation resources. ([b/167430145](https://issuetracker.google.com/167430145))
- NavOptions now overrides the hashcode and equals methods ([b/161586466](https://issuetracker.google.com/161586466))
- Navigation now includes the current destination in the "No destination with ID" IllegalArgumentException, which should improve the developer debugging experience. ([b/168311416](https://issuetracker.google.com/168311416))

**Bug Fixes**

- Safe Args will no longer wrap the return line, even if the generated argument class name is longer than 100 characters. ([b/168584987](https://issuetracker.google.com/168584987))

**Dependency Changes**

- `navigation-ui` now depends on [DrawerLayout 1.1.1](https://developer.android.com/jetpack/androidx/releases/drawerlayout#1.1.1), ensuring that `NavigationUI` is able to open the drawer even when using `LOCK_MODE_LOCKED_CLOSED` or `LOCK_MODE_LOCKED_OPEN`. ([b/162253907](https://issuetracker.google.com/162253907))
- Safe Args now depends on KotlinPoet 1.6.0 ([aosp/1435911](https://android-review.googlesource.com/c/platform/frameworks/support/+/1435911))
- Safe Args now depends on AGP 4.0.1 ([aosp/1442337](https://android-review.googlesource.com/c/platform/frameworks/support/+/1442337))

## Version 2.3.0

| **Note:** This version is dependent on the Java 8 programming language. Please read [Use Java 8 language features](https://developer.android.com/studio/write/java8-support) to learn how to use it in your project.

### Version 2.3.0

June 24, 2020

`androidx.navigation:navigation-*:2.3.0` is released. [Version 2.3.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/098293bcdb2b40862b3e287d38dd82ac8a9c6d38..654b8a76ea3c162fc3f9d84f3484ebadda0bbb9f/navigation)

**Major changes since 2.2.0**

- **Feature Module integration** : The `navigation-dynamic-features-runtime` and `navigation-dynamic-features-fragment` artifacts allow you to navigate to destinations that are defined in feature modules, automatically handling the installation of the feature modules as needed. See [Navigate with feature modules](https://developer.android.com/guide/navigation/navigation-dynamic) for more information.
- **Navigation Testing** : The `navigation-testing` artifact provides a `TestNavHostController` that allows you to set the current destination and verify the back stack after navigation operations. See [Test Navigation](https://developer.android.com/guide/navigation/navigation-testing) for more information.
- **Returning a Result** : The `NavBackStackEntry` associated with each destination on the Navigation back stack now allows you to access a [`SavedStateHandle`](https://developer.android.com/reference/androidx/lifecycle/SavedStateHandle) suitable for storing small amounts of saved state that should be associated with a particular back stack entry. See [Returning a result to the previous Destination](https://developer.android.com/guide/navigation/navigation-programmatic#returning_a_result) for more information.
- **`NavigationUI` support for `Openable`** : All usages of `DrawerLayout` in `NavigationUI` have been replaced with the more generic [`Openable`](https://developer.android.com/reference/androidx/customview/widget/Openable) interface added in [CustomView `1.1.0`](https://developer.android.com/jetpack/androidx/releases/customview#1.1.0) and implemented by `DrawerLayout` in [DrawerLayout `1.1.0`](https://developer.android.com/jetpack/androidx/releases/drawerlayout#1.1.0).
- **Action and Mime Type support in deep links** : Deep linking has been expanded to support `app:action` and `app:mimeType` in addition to the `app:uri` previously available. `NavController` now supports navigating by any combination of these fields via the new `NavDeepLinkRequest` class. See [Navigate using NavDeepLinkRequest](https://developer.android.com/guide/navigation/navigation-navigate#uri) for more information.

| **Note:** Support for adding an action and mime type in the visual editor is available in Android Studio 4.1 Canary 10 and higher.

**Known Issues**

- Support for deep link actions and mime types is not yet available in [Manifest Merger](https://issuetracker.google.com/issues/154166825). Until that work is completed, any generated `<intent-filter>` elements from the `<nav-graph>` element in your manifest won't include your mime type in its `<data>` element or your custom `<action>`. You must manually add an appropriate `<intent-filter>` to your manifest.

### Version 2.3.0-rc01

June 10, 2020

`androidx.navigation:navigation-*:2.3.0-rc01` is released. [Version 2.3.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ccc6e95c574b66563952c33fbe26888b93a0e0cb..098293bcdb2b40862b3e287d38dd82ac8a9c6d38/navigation)

**Bug Fixes**

- Fixed a `NullPointerException` when replacing an instance of a destination with no arguments with another instance *with* arguments with `singleTop`. ([b/158006669](https://issuetracker.google.com/issues/158006669))
- All `destination is unknown` exceptions thrown by `NavController` now have additional debugging information to help determine the state of the `NavController`. ([b/157764916](https://issuetracker.google.com/issues/157764916))

### Version 2.3.0-beta01

May 20, 2020

`androidx.navigation:navigation-*:2.3.0-beta01` are released. [Version 2.3.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/942518f415d35ff9f2ff78f312c076c673468877..ccc6e95c574b66563952c33fbe26888b93a0e0cb/navigation)

**Bug Fixes**

- Fixed an issue where the `Lifecycle` of the `NavBackStackEntry` would not be properly updated after process death. ([b/155218371](https://issuetracker.google.com/issues/155218371))
- `OnDestinationChangedListener` instances registered before calling `setGraph()` are now properly sent the restored destination after a process death. ([b/155218371](https://issuetracker.google.com/issues/155218371))
- When using `singleTop`, the `NavBackStackEntry` now correctly has its arguments updated and the updated arguments are sent to all `OnDestinationChangeListener` instances. ([b/156545508](https://issuetracker.google.com/issues/156545508))

**Dependency Updates**

- The `NavigationUI` artifact now depends on [CustomView `1.1.0-rc01`](https://developer.android.com/jetpack/androidx/releases/customview#1.1.0-rc01) and [DrawerLayout `1.1.0-rc01`](https://developer.android.com/jetpack/androidx/releases/drawerlayout#1.1.0-rc01). ([aosp/1309696](https://android-review.googlesource.com/1309696))

### Version 2.3.0-alpha06

April 29, 2020

`androidx.navigation:navigation-*:2.3.0-alpha06` is released. ([Version 2.3.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/24daa503442fcd3e44ada60cf1da41df2815c045..942518f415d35ff9f2ff78f312c076c673468877/navigation))

**New Features**

- Deep linking has been expanded to support `app:action` and `app:mimeType` in addition to the `app:uri` previously available. NavController now supports navigating by any combination of these fields via the new `NavDeepLinkRequest` class. ([b/136573074](https://issuetracker.google.com/issues/136573074), [b/135334841](https://issuetracker.google.com/issues/135334841))

| **Note:** Support for deep link actions and mime types is not yet available in Android Studio or in [Manifest Merger](https://issuetracker.google.com/issues/154166825). Until those are completed, you won't see the new attributes in the visual editor and any generated `<intent-filter>` elements won't include your mime type in its `<data>` element or your custom `<action>`. You can add the attributes manually to the `<deeplink>` element in XML and manually add an `<intent-filter>` to your manifest, respectively.

**API Changes**

- Greatly expanded the Kotlin DSL support for Dynamic Navigation destinations. ([b/148969800](https://issuetracker.google.com/issues/148969800))

**Bug Fixes**

- Fixed an issue where deep link Intents would be ignored when using a nested start destination. ([b/154532067](https://issuetracker.google.com/issues/154532067))

### Version 2.3.0-alpha05

April 15, 2020

`androidx.navigation:navigation-*:2.3.0-alpha05` is released. [Version 2.3.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8744680798c115f612a99148c5a5c3ad4bd6fbf5..24daa503442fcd3e44ada60cf1da41df2815c045/navigation)

**New Features**

- For [dynamic graph includes](https://developer.android.com/guide/navigation/navigation-dynamic#included) using `<include-dynamic>`, you no longer need to specify `app:graphPackage` and a default one will be used by adding `moduleName` suffix to the `applicationId` after a dot. If you do need to customize your `graphPackage`, an `${applicationId}` placeholder is now supported. ([b/152696768](https://issuetracker.google.com/issues/152696768))
- The Navigation Graph Kotlin DSL now exposes a `defaultArguments` `Map` for actions, mirroring the ability to set default values on `<action>` elements in Navigation XML files. ([b/150345605](https://issuetracker.google.com/issues/150345605))

**Bug Fixes**

- From [Navigation 2.2.2](https://developer.android.com/androidx/releases/navigation#2.2.2): Fixed an `IllegalStateException` when deep linking to the start destination of your graph when you have multiple `NavHostFragment` instances in your Activity. ([b/147378752](https://issuetracker.google.com/issues/147378752))

**Dependency updates**

- Navigation now depends on [Fragment `1.2.4`](https://developer.android.com/jetpack/androidx/releases/fragment#1.2.4). ([aosp/1277325](https://android-review.googlesource.com/1277325))
- Dynamic Navigation now depends on [Play Core `1.7.2`](https://developer.android.com/reference/com/google/android/play/core/release-notes#1-7-2). ([aosp/1282257](https://android-review.googlesource.com/1282257))

### Version 2.3.0-alpha04

March 18, 2020

`androidx.navigation:navigation-*:2.3.0-alpha04` is released. [Version 2.3.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/666ae665acfcfa2a20eccc18e4494808169742f4..8744680798c115f612a99148c5a5c3ad4bd6fbf5/navigation)

**New Features**

- Added support for feature module activity and fragment destinations in the Navigation Kotlin DSL. ([b/148969800](https://issuetracker.google.com/issues/148969800))

**API Changes**

- The `DynamicExtras` class no longer uses a builder pattern and can now be constructed directly. ([aosp/1253671](https://android-review.googlesource.com/1253671))
- `DynamicActivityNavigator` now takes a `Context` in its constructor rather than an `Activity`. ([aosp/1250252](https://android-review.googlesource.com/1250252))

**Bug Fixes**

- `NavigationUI` no longer ignores empty labels (i.e., a destination with `android:label=""`) and now correctly sets the title to an empty string. ([b/148679860](https://issuetracker.google.com/issues/148679860))

**Dependency Updates**

- The Navigation Dynamic Features artifacts now depend on Play Core `1.6.5`. ([b/149556401](https://issuetracker.google.com/issues/149556401))

### Version 2.3.0-alpha03

March 4, 2020

`androidx.navigation:navigation-*:2.3.0-alpha03` is released. [Version 2.3.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6f7b9ed69dc63e3c2c2b02ee1155b6009a9d5f82..666ae665acfcfa2a20eccc18e4494808169742f4/navigation)

**API Changes**

- Instead of relying on the concrete `DrawerLayout` class, `AppBarConfiguration` now uses the `Openable` interface introduced in [CustomView `1.1.0-alpha02`](https://developer.android.com/jetpack/androidx/releases/customview#1.1.0-alpha02) (which `DrawerLayout` implements as of [DrawerLayout `1.1.0-alpha04`](https://developer.android.com/jetpack/androidx/releases/drawerlayout#1.1.0-alpha03)), allowing you to use custom implementations of `Openable` with `NavigationUI`. ([b/129030452](https://developer.android.com/issuetracker.google.com/issues/129030452))

**Bug Fixes**

- The `navigation-common-ktx` ProGuard rules now correctly only keep the `NavArgs` classes that are used rather than all `NavArgs` instances. ([b/150213558](https://issuetracker.google.com/issues/150213558))

**Dependency changes**

- Navigation has reverted its dependency on Core `1.2.0` and now depends on Core `1.1.0` to avoid forcing developers to move to a newer dependency when Navigation does not depend on any new APIs in Core `1.2.0`.

### Version 2.3.0-alpha02

February 19, 2020

`androidx.navigation:navigation-*:2.3.0-alpha02` is released. [Version 2.3.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a670497cb9ff2d13701f20ef5f25f14dd4548f22..6f7b9ed69dc63e3c2c2b02ee1155b6009a9d5f82/navigation)

**New Features**

- The `NavBackStackEntry` now allows you to access a [`SavedStateHandle`](https://developer.android.com/reference/androidx/lifecycle/SavedStateHandle) suitable for storing small amounts of saved state that should be associated with a particular back stack entry. See [Returning a result](https://developer.android.com/guide/navigation/navigation-programmatic#returning_a_result) for an example use case. ([b/79672220](https://issuetracker.google.com/issues/79672220))

**API Changes**

- Convenience methods of `getCurrentBackStackEntry()` and `getPreviousBackStackEntry()` have been added to make it easier to retrieve a `NavBackStackEntry` for the current and previous destinations. ([b/79672220](https://issuetracker.google.com/issues/79672220))

**Bug Fixes**

- `navigateUp()` now passes the current destination's arguments and the [`KEY_DEEP_LINK_INTENT`](https://developer.android.com/reference/androidx/navigation/NavController#KEY_DEEP_LINK_INTENT) to the previous destination when launching your app on your own task stack. ([b/147456890](https://issuetracker.google.com/issues/147456890))

**Dependency changes**

- Navigation now depends on [Core `1.2.0`](https://developer.android.com/jetpack/androidx/releases/core#1.2.0).

### Version 2.3.0-alpha01

February 5, 2020

`androidx.navigation:navigation-*:2.3.0-alpha01` is released. [Version 2.3.0-alpha01 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/1420d9e061d8a0ff92bf7b3d28a6bdc4f20d13f5..a670497cb9ff2d13701f20ef5f25f14dd4548f22/navigation).

**New features**

- The new `navigation-testing` artifact provides a `TestNavHostController` class. This class provides an alternative to using a mock `NavController` when [testing Navigation](https://developer.android.com/guide/navigation/navigation-testing) that allows you to set the current destination and verify the back stack after navigation operations. ([b/140884273](https://issuetracker.google.com/issues/140884273))
- The new `navigation-dynamic-features-fragment` (and its transitive dependency, `navigation-dynamic-features-runtime`) allows you to include destinations or entire navigation graphs (via `<include-dynamic>`) from [feature modules](https://developer.android.com/guide/app-bundle/dynamic-delivery), providing seamless installation of on-demand feature modules when navigating to those destinations. See [Navigate with feature modules](https://developer.android.com/guide/navigation/navigation-dynamic) for more information. ([b/132170186](https://issuetracker.google.com/issues/132170186))

**Bug fixes**

- From [Navigation `2.2.1`](https://developer.android.com/jetpack/androidx/releases/navigation#2.2.1): Deep links without query parameters now correctly ignore any query parameters rather than appending them to trailing `{argument}` elements or not matching the deep link. ([b/147447512](https://issuetracker.google.com/issues/147447512))
- From [Navigation `2.2.1`](https://developer.android.com/jetpack/androidx/releases/navigation#2.2.1): The `navigation-ui` ProGuard rules for `DrawerArrowDrawable` have been updated to ensure that `android.enableJetifier=true` is not required. ([b/147610424](https://issuetracker.google.com/issues/147610424))
- From [Navigation `2.2.1`](https://developer.android.com/jetpack/androidx/releases/navigation#2.2.1): The `navigation-common-ktx` module now has a unique manifest package name instead of sharing the same manifest package name as `navigation-runtime-ktx`. ([aosp/1141947](https://android-review.googlesource.com/1141947/))

**Dependency updates**

- From [Navigation `2.2.1`](https://developer.android.com/jetpack/androidx/releases/navigation#2.2.1): Navigation `2.2.1` now depends on [Lifecycle ViewModel SavedState `2.2.0`](https://developer.android.com/jetpack/androidx/releases/lifecycle#viewmodel-savedstate-2.2.0) and [Fragment `1.2.1`](https://developer.android.com/jetpack/androidx/releases/fragment#1.2.1).

## Version 2.2.2

| **Note:** This version is dependent on the Java 8 programming language. Please read [Use Java 8 language features](https://developer.android.com/studio/write/java8-support) to learn how to use it in your project.

### Version 2.2.2

April 15, 2020

`androidx.navigation:navigation-*:2.2.2` are released. [Version 2.2.2 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3758a176b024534e6af6095fbd2f966627453d36..283af54f404f00bb16e7cbb90354681924d21ded/navigation)

**Bug Fixes**

- Fixed an `IllegalStateException` when deep linking to the start destination of your graph when you have multiple `NavHostFragment` instances in your Activity. ([b/147378752](https://issuetracker.google.com/issues/147378752))
- `NavigationUI` no longer ignores empty labels (i.e., a destination with `android:label=""`) and now correctly sets the title to an empty string. This was previously released in [Navigation 2.3.0-alpha04](https://developer.android.com/androidx/releases/navigation#2.3.0-alpha04). ([b/148679860](https://issuetracker.google.com/issues/148679860))
- The `navigation-common-ktx` ProGuard rules now correctly only keep the `NavArgs` classes that are used rather than all `NavArgs` instances. This was previously released in [Navigation 2.3.0-alpha03](https://developer.android.com/androidx/releases/navigation#2.3.0-alpha03). ([b/150213558](https://issuetracker.google.com/issues/150213558)

**Dependency updates**

- Navigation now depends on [Fragment `1.2.4`](https://developer.android.com/jetpack/androidx/releases/fragment#1.2.4). ([aosp/1277325](https://android-review.googlesource.com/1277325))

## Version 2.2.1

| **Note:** This version is dependent on the Java 8 programming language. Please read [Use Java 8 language features](https://developer.android.com/studio/write/java8-support) to learn how to use it in your project.

### Version 2.2.1

February 5, 2020

`androidx.navigation:navigation-*:2.2.1` is released. [Version 2.2.1 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/1420d9e061d8a0ff92bf7b3d28a6bdc4f20d13f5..3758a176b024534e6af6095fbd2f966627453d36/navigation).

**Bug fixes**

- Deep links without query parameters now correctly ignore any query parameters rather than appending them to trailing `{argument}` elements or not matching the deep link. ([b/147447512](https://issuetracker.google.com/issues/147447512))
- The `navigation-ui` ProGuard rules for `DrawerArrowDrawable` have been updated to ensure that `android.enableJetifier=true` is not required. ([b/147610424](https://issuetracker.google.com/issues/147610424))
- The `navigation-common-ktx` module now has a unique manifest package name instead of sharing the same manifest package name as `navigation-runtime-ktx`. ([aosp/1141947](https://android-review.googlesource.com/1141947/))

**Dependency updates**

- Navigation `2.2.1` now depends on [Lifecycle ViewModel SavedState `2.2.0`](https://developer.android.com/jetpack/androidx/releases/lifecycle#viewmodel-savedstate-2.2.0) and [Fragment `1.2.1`](https://developer.android.com/jetpack/androidx/releases/fragment#1.2.1).

## Version 2.2.0

| **Note:** This version is dependent on the Java 8 programming language. Please read [Use Java 8 language features](https://developer.android.com/studio/write/java8-support) to learn how to use it in your project.

### Version 2.2.0

January 22, 2020

`androidx.navigation:navigation-*:2.2.0` is released. [Version 2.2.0 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/ecc5b7be8afa070b3e8381ad059773453c860324..1420d9e061d8a0ff92bf7b3d28a6bdc4f20d13f5/navigation).

**Important changes since 2.1.0**

- **NavBackStackEntry** : You can now call `NavController.getBackStackEntry()`, passing in the ID of a destination or navigation graph on the back stack. The returned `NavBackStackEntry` provides a Navigation-driven `LifecycleOwner`, `ViewModelStoreOwner` (the same returned by `NavController.getViewModelStoreOwner()`), and `SavedStateRegistryOwner`, in addition to providing the arguments used to start that destination.
- **Lifecycle ViewModel SavedState Integration** : `SavedStateViewModelFactory` is now the default factory used when using `by navGraphViewModels()` or the `ViewModelProvider` constructor with a `ViewModelStoreOwner` returned by `NavController.getBackStackEntry()` or `NavController.getViewModelStoreOwner()`.
- **Query Parameter Support for Deep Links**: Deep links with query parameters now support reordered query parameters; arguments that have a default value or are nullable are now optional when matching deep links.
- **Improved Animation Support** : `NavHostFragment` now uses `FragmentContainerView` from [Fragment 1.2.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.2.0), fixing animation z-ordering issues and window insets dispatching to Fragments.

### Version 2.2.0-rc04

December 18, 2019

`androidx.navigation:navigation-*:2.2.0-rc04` is released. [Version 2.2.0-rc04 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/ac0a968ffb9334b853a1799aba7dac42fed70b5f..f251e0f6da084dca812052169c8f2032a3151604/navigation).

**Bug fixes**

- Adjusted the default fade animations used by `navigation-ui` to match the adjusted fade animations in [Fragment `1.2.0-rc04`](https://developer.android.com/jetpack/androidx/releases/fragment#1.2.0-rc04). ([b/145769814](https://issuetracker.google.com/issues/145769814))

### Version 2.2.0-rc03

December 4, 2019

`androidx.navigation:navigation-*:2.2.0-rc03` is released. [Version 2.2.0-rc03 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/b0b973c9bc89f9ad3efe3c06e41b72957f032a99..ac0a968ffb9334b853a1799aba7dac42fed70b5f/navigation).

**Bug fixes**

- Fixed an issue with deep link parsing when using query parameters and an argument as the last part of the path that prevented more than one character of the final path argument from being parsed. ([b/144554689](https://issuetracker.google.com/issues/144554689))
- Fixed an issue with deep link parsing where optional parameters would receive `"@null"` instead of `null`. ([b/141613546](https://issuetracker.google.com/issues/141613546))
- `NavHostFragment` now correctly restores the graph after a configuration change when used with `FragmentContainerView`. ([b/143752103](https://issuetracker.google.com/issues/143752103))

**Dependency changes**

- Navigation now depends on Lifecycle `2.2.0-rc03`, Lifecycle ViewModel SavedState `1.0.0-rc03`, Activity `1.1.0-rc03`, and Fragment `1.2.0-rc03` where appropriate.

### Version 2.2.0-rc02

November 7, 2019

`androidx.navigation:navigation-*:2.2.0-rc02` is released. [Version 2.2.0-rc02 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/c378b9a2eae63d2701c82b0144af36e33d15c26a..b0b973c9bc89f9ad3efe3c06e41b72957f032a99/navigation).

**Dependency changes**

- Navigation now depends on androidx.lifecycle `2.2.0-rc02`.

### Version 2.2.0-rc01

October 23, 2019

`androidx.navigation:navigation-*:2.2.0-rc01` is released with no changes since `2.2.0-beta01`. [Version 2.2.0-rc01 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/2180ea57914af961d4f2bb43802b42ae0d1802e0..c378b9a2eae63d2701c82b0144af36e33d15c26a/navigation).

### Version 2.2.0-beta01

October 9, 2019

`androidx.navigation:navigation-*:2.2.0-beta01` is released. [Version 2.2.0-beta01 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/b08258a10a1c5db71bfaaeee2220bbc5e775fe5f..2180ea57914af961d4f2bb43802b42ae0d1802e0/navigation).

**New features**

- `NavDestination` and its subclasses now override `toString()` to provide more helpful information when debugging. ([b/141264986](https://issuetracker.google.com/issues/141264986))

**Behavior changes**

- Extra query parameters are now ignored when matching deep links rather than causing the match to fail. ([b/141482822](https://issuetracker.google.com/issues/141482822))

**Bug fixes**

- Fixed an issue where arguments in a deep link's path would be ignored if query parameters were also specified. ([b/141505755](https://issuetracker.google.com/issues/141505755))
- The `navArgs()` Kotlin extension on `Activity` now has a better error message when there are no extras. ([b/141408999](https://issuetracker.google.com/issues/141408999))
- Safe Args generated `Directions` Java classes now contain default values. ([b/141099045](https://issuetracker.google.com/issues/141099045))
- Safe Args generated `Args` Java classes now contain default values. ([b/140123727](https://issuetracker.google.com/issues/140123727))
- When using a `Toolbar`, `NavigationUI` no longer animates the text change when moving between two top level destinations. ([b/140848160](https://issuetracker.google.com/issues/140848160))

### Version 2.2.0-alpha03

September 18, 2019

`androidx.navigation:navigation-*:2.2.0-alpha03` is released. [Version 2.2.0-alpha03 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/2d0a22f1ddeb3b7e9d0002f0e089a25b7ef64f1c..391dc4bc729d2973a6e6e57916d3008c58026e56/navigation).

**Behavior changes**

- Calling `setViewModelStore()` after calling `setGraph` now results in an `IllegalStateException`. This should always be set by the `NavHost` as part of the initial setup to ensure that all `NavBackStackEntry` instances have a consistent storage for `ViewModel` instances. ([aosp/1111821](https://android-review.googlesource.com/1111821))

**Bug fixes**

- Fixed a `ConcurrentModificationException` when using `ViewModel` instances attached to multiple different navigation graph scoped `ViewModelStore` instances. ([aosp/1112257](https://android-review.googlesource.com/1112257))

### Version 2.2.0-alpha02

September 5, 2019

`androidx.navigation:navigation-*:2.2.0-alpha02` is released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/23fecdb1097a69a528ab6109f661b4e46123aecc..2d0a22f1ddeb3b7e9d0002f0e089a25b7ef64f1c/navigation).

**New features**

- Deep links with query parameters now support reordered query parameters; arguments that have a default value or are nullable are now optional when matching deep links. ([b/133273839](https://issuetracker.google.com/issues/133273839))
- You can now call `NavController.getBackStackEntry()`, passing in the ID of a destination or navigation graph on the back stack. The returned `NavBackStackEntry` provides a Navigation-driven `LifecycleOwner`, `ViewModelStoreOwner` (the same returned by `NavController.getViewModelStoreOwner()`), and `SavedStateRegistryOwner`, in addition to providing the arguments used to start that destination. ([aosp/1101691](https://android-review.googlesource.com/1101691), [aosp/1101710](https://android-review.googlesource.com/1101710))

**Bug fixes**

- Fixed an issue where adding a `NavHostFragment` to `ViewPager2` failed with an `IllegalArgumentException`. ([b/133640271](https://issuetracker.google.com/issues/133640271))
- `NavInflater` now avoids calling `getResourceName()` unnecessarily, speeding up inflation time by up to 40%. ([b/139213740](https://issuetracker.google.com/issues/139213740))

### Version 2.2.0-alpha01

August 7, 2019

`androidx.navigation:navigation-*:2.2.0-alpha01` is released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/e08a521e6ca90dc09329823c31c733d69a1164cf..23fecdb1097a69a528ab6109f661b4e46123aecc/navigation).

**New features**

- `SavedStateViewModelFactory` is now the default factory used when using `by navGraphViewModels()` or the `ViewModelProvider` constructor with a `ViewModelStoreOwner` returned by `NavController.getViewModelStoreOwner()`. ([b/135716331](https://issuetracker.google.com/issues/135716331))

**API changes**

- From [Navigation `2.1.0-rc01`](https://developer.android.com/jetpack/androidx/releases/navigation#2.1.0-rc01): The deprecated `getViewModelStore()` API on `NavController` introduced in `2.1.0-alpha02` has been removed. ([aosp/1091021](https://android-review.googlesource.com/1091021))

**Bug fixes**

- `NavHostFragment` now uses `FragmentContainerView`, fixing animation z-ordering issues and window insets dispatching to Fragments. ([b/137310379](https://issuetracker.google.com/issues/137310379))

## Version 2.1.0

### Version 2.1.0

September 5, 2019

`androidx.navigation:navigation-*:2.1.0` is released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/d86f26b9b2b958f75b4f23161344cec32237c9ca..73f368c10e67f70c624a53d53828686746bf51bf/navigation).

**Important changes since 2.0.0**

- **Scoping ViewModels to a navigation graph** : You can now create ViewModels that are scoped at the navigation graph level using the `by navGraphViewModels()` property delegate for Kotlin users using the `-ktx` libraries or by using the `getViewModelStoreOwner()` API added to `NavController`. See [Share UI-related data between destinations](https://developer.android.com/guide/navigation/navigation-programmatic#share_ui-related_data_between_destinations_with_viewmodel) for more information.
- **Dialog destinations** : You can now create `<dialog>` destinations that will show a `DialogFragment` when you `navigate` to them. `NavHostFragment` supports dialog destinations by default. See [Create a destination from a DialogFragment](https://developer.android.com/guide/navigation/navigation-create-destinations#create-dialog) for more information.
- **Navigating by Uri** : You can now `navigate` using a `Uri`, which uses the `<deepLink>` you've added to a destination to navigate there. See [Navigate using Uri](https://developer.android.com/guide/navigation/navigation-navigate#uri) for more information.
- **NavHostController** : APIs used specifically for constructing a custom `NavHost` have been moved to `NavHostController`, allowing implementations to connect their `NavController` to the hosting `LifecycleOwner`, `OnBackPressedDispatcher`, and `ViewModelStore`.

### Version 2.1.0-rc01

August 7, 2019

`androidx.navigation:navigation-*:2.1.0-rc01` is released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/ec4f7aa322b7f2b5aa14aff6dca9475b0df1345c..d86f26b9b2b958f75b4f23161344cec32237c9ca/navigation).

**API changes**

- The deprecated `getViewModelStore()` API on `NavController` introduced in `2.1.0-alpha02` has been removed. ([aosp/1091021](https://android-review.googlesource.com/1091021))

### Version 2.1.0-beta02

July 19, 2019

`androidx.navigation:*:2.1.0-beta02` is released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/e08a521e6ca90dc09329823c31c733d69a1164cf..ec4f7aa322b7f2b5aa14aff6dca9475b0df1345c/navigation).
| **Note:** This version is dependent on the Java 8 programming language. Please read [Use Java 8 language features](https://developer.android.com/studio/write/java8-support) to learn how to use it in your project.

**Bug fixes**

- Removed unintentional jacoco dependency that was introduced in `2.1.0-beta01`. ([b/137782950](https://issuetracker.google.com/issues/137782950))

### Version 2.1.0-beta01

July 17, 2019

`androidx.navigation:*:2.1.0-beta01` is released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/498e1c39f543ee174434d4fc26e26219c298e9cd..e08a521e6ca90dc09329823c31c733d69a1164cf/navigation).
| **Caution:** This version contains an unintentional dependency on `org.jacoco:org.jacoco.agent:0.8.3`, which can cause a build failure. Please update to the latest version, in which this dependency has been removed.
| **Note:** This version is dependent on the Java 8 programming language. Please read [Use Java 8 language features](https://developer.android.com/studio/write/java8-support) to learn how to use it in your project.

**New features**

- `NavigationUI` now animates the removal of the Up button when using `setupWithNavController()` with a `Toolbar` or `CollapsingToolbarLayout`. ([b/131403621](https://issuetracker.google.com/issues/131403621))

**Bug fixes**

- Fixed a timing issue when using multiple NavHostFragments with the same container with `findNavController()`. ([b/136021571](https://issuetracker.google.com/issues/136021571))

### Version 2.1.0-alpha06

July 2, 2019

`androidx.navigation:*:2.1.0-alpha06` is released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/067bb2bdba5ad5259e147e5f36ec20c5efa9ae42..498e1c39f543ee174434d4fc26e26219c298e9cd/navigation).
| **Note:** This version is dependent on the Java 8 programming language. Please read [Use Java 8 language features](https://developer.android.com/studio/write/java8-support) to learn how to use it in your project.

**New features**

- The `app:navGraph` attribute used by NavHostFragment has now been moved to the `navigation-runtime` artifact. Custom navigators that can be added via XML should use this attribute to gain integration with the Navigation Editor's Host panel. ([b/133880955](https://issuetracker.google.com/issues/133880955))

**API changes**

- The `getViewModelStore()` API on `NavController` has been deprecated in favor of the new `getViewModelStoreOwner()` method that returns a `ViewModelStoreOwner`. ([aosp/987010](https://android-review.googlesource.com/987010))
- The implementation of floating window destinations, such as `<dialog>` destinations, has been generalized into a marker interface, `FloatingWindow`, that all `<dialog>` destinations now implement. NavigationUI methods for interacting with the top app bar now ignore `FloatingWindow` destinations. ([b/133600763](https://issuetracker.google.com/issues/133600763))

**Behavior changes**

- Navigation now correctly keeps its state in sync with what is seen on the screen when using a `<dialog>` destination. As a consequence, Navigation now automatically pops `<dialog>` destinations when you navigate to a non-dialog and non-activity destination, such as a `<fragment>` destination. ([b/134089818](https://issuetracker.google.com/issues/134089818))

**Bug fixes**

- Navigation now suppresses the animation that occurs when recreating the activity when handling a deep link, fixing a visual flash. ([b/130362979](https://issuetracker.google.com/issues/130362979))
- Fixed a bug where the Navigation back stack would be out of sync when popping a Fragment as the initial fragment is being added. ([b/133832218](https://issuetracker.google.com/issues/133832218))

### Version 2.1.0-alpha05

June 5, 2019

`androidx.navigation:*:2.1.0-alpha05` is released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/a2937df81230da03ed4121b65f7ef3eab0d9a42e..a3fc6e9c32e6438770cdb7201eaa1d6477521d82/navigation).

**API changes**

- Host related APIs on `NavController` have been renamed and moved to a new subclass of `NavController`, `NavHostController`. ([aosp/966091](https://android-review.googlesource.com/966091))
- The `NavController` `setHostOnBackPressedDispatcherOwner()` method has been replaced with `NavHostController`'s `setOnBackPressedDispatcher()` method and now requires that you call `setLifecycleOwner()` prior to calling it. ([aosp/965409](https://android-review.googlesource.com/965409))
- `NavHostController` now contains a `enableOnBackPressed(boolean)` method that replaces the `NavHostOnBackPressedManager` class that was previously returned by `setHostOnBackPressedDispatcherOwner()`. ([aosp/966091](https://android-review.googlesource.com/966091))

**Bug fixes**

- Fixed an issue where the back stack was not correct after navigating by URI. ([b/132509387](https://issuetracker.google.com/issues/132509387))
- Deep links automatically handled by NavController now only trigger once. ([b/132754763](https://issuetracker.google.com/issues/132754763))

### Version 2.1.0-alpha04

May 16, 2019

`androidx.navigation:*:2.1.0-alpha04` is released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/d339df058031dadca4676524c5c184e559553a2e..a2937df81230da03ed4121b65f7ef3eab0d9a42e/navigation).

**Bug fixes**

- `NavHostFragment` correctly respects `app:defaultNavHost` when intercepting the system Back button events, fixing a regression in Navigation `2.1.0-alpha03`. [b/132077777](https://issuetracker.google.com/issues/132077777)
- `DialogFragmentNavigator` now correctly handles `popBackStack()` and `navigateUp()` operations. [b/132576764](https://issuetracker.google.com/issues/132576764)
- Fixed an `IllegalStateException: unknown destination during restore` issue when repeatedly navigating between nested graphs. [b/131733658](https://issuetracker.google.com/issues/131733658)

### Version 2.1.0-alpha03

May 7, 2019

`androidx.navigation:*:2.1.0-alpha03` is released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/3cc9b77742508c095f3268b60956967bce46f0ed..d339df058031dadca4676524c5c184e559553a2e/navigation).

**Known Issues**

- NavHostFragment continues to intercept the system Back button despite using `app:defaultNavHost="false"` [b/132077777](https://issuetracker.google.com/issues/132077777)

**New features**

- You can now create `<dialog>` destinations that will show a `DialogFragment` when you `navigate` to them. `NavHostFragment` supports dialog destinations by default. [b/80267254](https://issuetracker.google.com/issues/80267254)
- In addition to calling `navigate` with a resource id or a `NavDirections` instance, you can now navigate via a `Uri`, which uses the `<deepLink>` you've added to a destination to navigate to the correct destination. [b/110412864](https://issuetracker.google.com/issues/110412864)

**Behavior changes**

- The default animations provided by NavigationUI have been sped up from 400ms to 220ms to match the default animation speed of activities and fragments. [b/130055522](https://issuetracker.google.com/issues/130055522)

**API changes**

- The `createFragmentNavigator()` method of `NavHostFragment` has been deprecated and its functionality moved to the new `onCreateNavController()` method to make it more clear that this is the correct entry point of adding custom Navigators when subclassing `NavHostFragment`. [b/122802849](https://issuetracker.google.com/issues/122802849)
- A `hasDeepLink()` method has been added to `NavDestination` to allow you to check if a given `Uri` can be handled by that destination or, in the case of a `NavGraph`, any destination in the navigation graph. [b/117437718](https://issuetracker.google.com/issues/117437718)

**Bug fixes**

- Default arguments are now correctly passed to `OnDestinationChangedListener` instances. [b/130630686](https://issuetracker.google.com/issues/130630686)
- `NavHostFragment` now intercepts system Back events using the `OnBackPressedDispatcher`, fixing an issue when doing conditional navigation in Fragment lifecycle methods upon returning to a Fragment. [b/111598096](https://issuetracker.google.com/issues/111598096)
- For Safe Args, an `android:defaultValue="@null"` with an unspecified `app:argType` is now properly inferred as a `string` argument. [b/129629192](https://issuetracker.google.com/issues/129629192)

### Version 2.1.0-alpha02

April 3, 2019

`androidx.navigation:*:2.1.0-alpha02` is released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/d0b1a77198af283997fb25e6ca3f083fbf535179..3cc9b77742508c095f3268b60956967bce46f0ed/navigation).

**New features**

- You can now create ViewModels that are scoped at a navigation graph level via the `by navGraphViewModels()` property delegate for Kotlin users or by using the `getViewModelStore()` API added to `NavController`. [b/111614463](https://issuetracker.google.com/issues/111614463)

**API changes**

- You can now add an `app:targetPackage` to an `<activity>` destination to limit the matching package name. It supports `app:targetPackage="${applicationId}"` for restricting the package to your own application id. [b/110975456](https://issuetracker.google.com/issues/110975456)

**Bug fixes**

- The `android:name` for `<activity>` destinations is no longer parsed into a Class at inflation time, preventing ClassNotFoundExceptions when using dynamic features. [b/124538597](https://issuetracker.google.com/issues/124538597)

### Version 2.1.0-alpha01

March 19, 2019

This is the first alpha release of Navigation `2.1.0`.

**Dependency changes**

- Navigation now depends on `androidx.core:core:1.0.1` and `androidx.fragment:fragment:1.1.0-alpha05`. This release also removes the dependency on `androidx.legacy:legacy-support-core-utils:1.0.0`. [b/128632612](https://issuetracker.google.com/128632612)

**API Changes**

- A new `Navigation.createNavigateOnClickListener(NavDirections)` method has been added as an alternative to creating a click listener with a resource ID and Bundle. [b/127631752](https://issuetracker.google.com/127631752)
- `FragmentNavigator.instantiateFragment` is now deprecated. The default implementation now uses `FragmentFactory` to instantiate Fragments. [b/119054429](https://issuetracker.google.com/119054429)

**Bug Fixes**

- Navigation no longer sends a null `Bundle` when there are arguments attached to a destination, fixing an issue when using `android:defaultValue="@null"`. [b/128531879](https://issuetracker.google.com/128531879)
- Safe Args now depends on KotlinPoet 1.1.0, fixing an issue with extremely long package names. [b/123654948](https://issuetracker.google.com/123654948)

## Version 2.0.0

### Version 2.0.0

March 14, 2019

Navigation `2.0.0` is released with no changes from `2.0.0-rc02`.

### Version 2.0.0-rc02

March 6, 2019

Navigation 2.0.0-rc02 provides new artifacts with the `androidx.navigation`
group ID and changes its dependencies to the AndroidX equivalents.

The behavior of 2.0.0-rc02 is identical to behavior to Navigation 1.0.0-rc02
and no changes to your code should be required to update from 1.0.0-rc02
besides updating your dependencies to match the
[new dependencies](https://developer.android.com/jetpack/androidx/releases/navigation#declaring_dependencies).

Your project must have
[migrated to AndroidX](https://developer.android.com/jetpack/androidx/migrate) to use 2.X releases of
Navigation. Navigation 1.0 stable will be the last release using the Support
Library dependencies; all future development beyond 1.0 will be based on
AndroidX and build upon the 2.0 stable release.

## Pre-AndroidX Dependencies

For the pre-AndroidX versions of Navigation, include these dependencies:

    dependencies {
        def nav_version = "1.0.0"

        implementation "android.arch.navigation:navigation-fragment:$nav_version" // For Kotlin use navigation-fragment-ktx
        implementation "android.arch.navigation:navigation-ui:$nav_version" // For Kotlin use navigation-ui-ktx
    }

For [Safe args](https://developer.android.com/topic/libraries/architecture/navigation/navigation-pass-data#Safe-args), add the
following **classpath** in your **top level** `build.gradle` file

    buildscript {
        repositories {
            google()
        }
        dependencies {
            classpath "android.arch.navigation:navigation-safe-args-gradle-plugin:1.0.0"
        }
    }

## Version 1.0.0

### Version 1.0.0

March 14, 2019

Navigation `1.0.0` is released with no changes from `1.0.0-rc02`.

### Version 1.0.0-rc02

February 26, 2019

This is the second release candidate for Navigation's 1.0.0 stable release.
This release contains a number of bug fixes.

**Bug Fixes**

- Fixed an issue where `popBackStack()` would be ignored if the root graph did not have an ID [b/126251695](https://issuetracker.google.com/126251695)
- `navigateUp()` now correctly handles navigating back to your app's task when called after handling a deep link without `FLAG_ACTIVITY_NEW_TASK` [b/126082008](https://issuetracker.google.com/126082008)
- Fixed an issue with `ActivityNavigator.applyPopAnimationsToPendingTransition` not applying the correct pop exit animation [b/126237567](https://issuetracker.google.com/126237567)
- Kotlin code generated by Safe Args now properly escapes Kotlin keywords such as `in` and `fun` in the package name associated with the `R` class. [b/126020455](https://issuetracker.google.com/126020455)

### Version 1.0.0-rc01

February 21, 2019

This is a release candidate for Navigation's 1.0.0 stable release. This
release contains one bug fix.

**Bug Fixes**

- Fixed an issue when using Fragments and `singleTop` navigation operations [b/124294805](https://issuetracker.google.com/124294805)

### Version 1.0.0-beta02

February 12, 2019

This release includes a number of minor improvements and important bug fixes.

**New Features**

- You can now use `0` as an `android:defaultValue` for `reference` arguments. [b/124248602](https://issuetracker.google.com/124248602)

**Behavior changes**

- Exact deep link matches are now prioritized over deep links with `.*` or argument matches. [b/123969518](https://issuetracker.google.com/123969518)

**Bug Fixes**

- `popBackStack()` and `navigateUp` now correctly return `false` when popping the last destination on the back stack, fixing a regression introduced in `1.0.0-beta01`. [b/123933201](https://issuetracker.google.com/123933201)
- Navigation now correctly sets the `ClassLoader` during restoration of saved instance state, avoiding issues when using custom classes in `Navigator` saved state or in arguments sent to a `NavDestination`. [b/123893858](https://issuetracker.google.com/123893858)
- Safe Args generated NavArgs classes no longer crash when restoring a `Parcelable[]` argument from saved instance state. [b/123963545](https://issuetracker.google.com/123963545)
- Safe Args now properly cleans up unnecessary generated Kotlin classes. [b/124120883](https://issuetracker.google.com/124120883)

### Version 1.0.0-beta01

February 4, 2019

This is the first beta release of Navigation; moving forward, the Navigation
API is expected to stay stable until the next version unless there is a
critical problem. This release contains some bug fixes and behavior changes.

**Behavior changes**

- Navigation now ensures that argument default values are treated identically at runtime and through Safe Args. As a consequence, only arguments with an `app:argType="reference"` can have a default value point to another resource (for example, `@color/colorPrimary`). Attempting to use a reference default value with a different `app:argType` will result in an exception when parsing the navigation XML. [b/123551990](https://issuetracker.google.com/123551990)
- Safe Args now depends on Android Gradle Plugin 3.3.0 [aosp/888413](https://android-review.googlesource.com/888413)
- Safe Args now depends on Kotlin 1.3.20 [aosp/888414](https://android-review.googlesource.com/888414)

**Bug Fixes**

- Safe Args can now be used in library and feature modules on all versions of the Android Gradle Plugin. [b/121304903](https://issuetracker.google.com/121304903)
- Fixed a regression that would cause a single `popBackStack()` operation to pop all copies of a destination off the top of the back stack, rather than just a single destination at a time. [b/123552990](https://issuetracker.google.com/123552990)
- Fixed an issue where the `FragmentNavigator` state would desynchronize with the `NavController`'s state, causing an `IllegalStateException` when attempting to restore the back stack. [b/123803044](https://issuetracker.google.com/123803044)
- Fixed an issue where the `NavigationUI` handled back arrow would not appear when using ProGuard with obfuscation. [b/123449431](https://issuetracker.google.com/123449431)
- The code generated by Safe Args now properly handles using an `app:argType` pointing to a static inner class in the format `.OuterClass$InnerClass`. [b/123736741](https://issuetracker.google.com/123736741)
- The Java code generated by Safe Args now properly handles global actions and deeply nested destinations. [b/123347762](https://issuetracker.google.com/123347762)

### Version 1.0.0-alpha11

January 23, 2019

This is a hotfix release of `1.0.0-alpha10` that fixes an issue with Safe Args.

**Bug Fixes**

- Fixes an issue where Safe Args would fail to import the Directions class associated with global actions. [b/123307342](https://issuetracker.google.com/123307342)

### Version 1.0.0-alpha10

January 23, 2019

**Known Issues**

- Safe Args fails to import the Directions class associated with global actions. [b/123307342](https://issuetracker.google.com/123307342)

This release contains breaking API changes;
please see the *Breaking Changes* section below.

**New Features**

- Kotlin users can now use the `by navArgs()` property delegate to lazily get a reference to a Safe Args generated `NavArgs` class in an `Activity` or `Fragment`. [b/122603367](https://issuetracker.google.com/122603367)
- Safe Args now allows you to generate Kotlin code by applying the `androidx.navigation.safeargs.kotlin` plugin. The Kotlin code is built specifically for Kotlin only modules, using default arguments and immutable classes over the builder pattern that is still available via the previous `androidx.navigation.safeargs` plugin. [b/110263087](https://issuetracker.google.com/110263087)

**Behavior Changes**

- Matching deep links are now biased towards the deep link that has the most matching arguments. [b/118393029](https://issuetracker.google.com/118393029)
- Calling `setGraph()` on a `NavController` will now reset the back stack. [b/111450672](https://issuetracker.google.com/111450672)
- Unknown deep links no longer throw an `IllegalStateException`, but are ignored, fixing issues with nested or multiple `NavHostFragment`s. [b/121340440](https://issuetracker.google.com/121340440)

**Breaking Changes**

- The `NavOptions.applyPopAnimationsToPendingTransition()` method for applying pop animations to an Activity has been moved to `ActivityNavigator`. [b/122413117](https://issuetracker.google.com/122413117)
- Safe Args now avoids duplicating identical classes for actions without arguments. The return type for no argument methods in generated NavDirections classes is now `NavDirections`. [b/123233147](https://issuetracker.google.com/123233147)
- Safe Args generated Directions classes no longer have a public constructor - you should only be interacting with the generated static methods. [b/123031660](https://issuetracker.google.com/123031660)
- Safe Args generated `NavDirections` classes no longer have a public constructor - they should only be generated via the static methods in the generated Directions classes. [b/122963206](https://issuetracker.google.com/122963206)
- The returned `Bundle` from `NavDirections`' `getArguments()` is now marked as `@NonNull` rather than `@Nullable`. [b/123243957](https://issuetracker.google.com/123243957)

**Bug Fixes**

- `NavDeepLinkBuilder` now correctly handles multiple simultaneous `PendingIntent`s to the same destination by using the arguments you pass in to determine the uniqueness. [b/120042732](https://issuetracker.google.com/120042732)
- `NavController` now correctly handles `popBackStack()` operations when using a nested `NavHostFragment` or other child Fragments with a back stack. [b/122770335](https://issuetracker.google.com/122770335)
- `NavigationUI` now correctly sets the content description of the Up button. [b/120395362](https://issuetracker.google.com/120395362)
- Safe Args generated Directions classes now correctly handle global actions that have the same id as an action on a destination. [b/122962504](https://issuetracker.google.com/122962504)
- Safe Args generated `NavDirections` classes now correctly have equal `hashCode()` values when `equals()` would return true. [b/123043662](https://issuetracker.google.com/123043662)
- `FragmentNavigator` now throws a better error message if you attempt to do custom `FragmentTransactions` on the `NavHostFragment`'s `FragmentManager`. You should always use `getChildFragmentManager()`. [b/112927148](https://issuetracker.google.com/112927148)

### Version 1.0.0-alpha09

December 18, 2018

This release contains breaking API changes;
please see the *Breaking Changes* section below.

We have chosen not to continue development of the
`android.arch.navigation:navigation-testing` artifact. While it has proven
helpful for internal testing of `NavController`, we strongly recommend
alternate testing strategies, such as mocking the `NavController` instance
in order to verify that the correct `navigate()` calls are being done. This
approach is discussed in detail in the
[Single Activity talk at AndroidDevSummit 2018](https://www.youtube.com/watch?v=2k8x8V77CrU)
and we'll be working on additional documentation specifically around testing
with Navigation.

**New Features**

- `MenuItem`s with `menuCategory="secondary"` will no longer pop the back stack when used with `NavigationUI` methods. [b/120104424](https://issuetracker.google.com/120104424)
- `AppBarConfiguration` now allows you to set a fallback [`OnNavigateUpListener`](https://developer.android.com/reference/androidx/navigation/AppBarConfiguration.OnNavigateUpListener) instance which will be called when `navController.navigateUp()` returns `false`. [b/79993862](https://issuetracker.google.com/79993862) [b/120690961](https://issuetracker.google.com/120690961)

**Breaking Changes**

- When using an `<argument>` with an `argType="reference"`, Navigation no longer parses the reference, instead providing the raw resource ID itself. [b/111736515](https://issuetracker.google.com/111736515)
- [`onNavDestinationSelected()`](https://developer.android.com/reference/androidx/navigation/ui/NavigationUI#onNavDestinationSelected(android.view.MenuItem,%20androidx.navigation.NavController)) now pops back to the start destination of your navigation graph by default, making them consistent with the `setup` methods. Add `menuCategory="secondary"` to your `MenuItem` to avoid popping the back stack. [aosp/852869](https://android-review.googlesource.com/852869)
- The `fromBundle()` methods of generated `Args` classes now take a non-null `Bundle` instead of a nullable `Bundle` [aosp/845616](https://android-review.googlesource.com/845616)

**Bug Fixes**

- Arguments are now properly parsed from deep links as the correct `argType` instead of always as strings [b/110273284](https://issuetracker.google.com/110273284)
- Navigation now correctly exports its public resources [b/121059552](https://issuetracker.google.com/121059552)
- Safe Args is now compatible with Android Gradle Plugin 3.4 Canary 4 and higher [b/119662045](https://issuetracker.google.com/119662045)

### Version 1.0.0-alpha08

December 6, 2018

This release contains breaking API changes;
please see the *Breaking Changes* section below.

**New Features**

- Destination labels, when used with `NavigationUI` methods, will now automatically replace `{argName}` instances in your `android:label` with the correct argument [b/80267266](https://issuetracker.google.com/80267266)
- Navigation now depends on Support Library 28.0.0 [b/120293333](https://issuetracker.google.com/120293333)

**Breaking Changes**

- `OnNavigatedListener` has been renamed to `OnDestinationChangedListener` [b/118670572](https://issuetracker.google.com/118670572)
- `OnDestinationChangedListener` now also passes the `Bundle` of arguments [aosp/837142](https://android-review.googlesource.com/837142)
- The `app:clearTask` and `app:launchDocument` attributes and their associated methods have been removed. Use `app:popUpTo` with the root of your graph to remove all destinations from your back stack. [b/119628354](https://issuetracker.google.com/119628354)
- `ActivityNavigator.Extras` now uses a `Builder` pattern and adds the ability to set any `Intent.FLAG_ACTIVITY_` flags [aosp/828140](https://android-review.googlesource.com/828140)
- `NavController.onHandleDeepLink` has been renamed to `handleDeepLink` [aosp/836063](https://android-review.googlesource.com/836063)
- Many classes and methods not meant for subclassing, such as `NavOptions`, `NavInflater`, `NavDeepLinkBuilder`, and `AppBarConfiguration`, have been made `final` [aosp/835681](https://android-review.googlesource.com/835681)
- The deprecated `NavHostFragment.setGraph()` method has been removed [aosp/835684](https://android-review.googlesource.com/835684)
- The deprecated `NavigationUI.navigateUp(DrawerLayout, NavController)` method has been removed. [aosp/835684](https://android-review.googlesource.com/835684)
- Fragment creation has been moved to `FragmentNavigator`, making it easier to delegate Fragment creation to a `FragmentFactory`. [b/119054429](https://issuetracker.google.com/119054429)
- The constructor for `NavGraphNavigator` no longer takes a `Context` [aosp/835340](https://android-review.googlesource.com/835340)
- [NavigatorProvider](https://developer.android.com/reference/androidx/navigation/NavigatorProvider) is now a class, rather than an interface. The `NavigatorProvider` returned by [`getNavigatorProvider()`](https://developer.android.com/reference/androidx/navigation/NavController#getNavigatorProvider()) has not changed its functionality. [aosp/830660](https://android-review.googlesource.com/830660)
- `NavDestination.navigate()` has been removed. Call `navigate()` on the `Navigator` instead. [aosp/830663](https://android-review.googlesource.com/830663)
- Significant refactoring of `Navigator`, removing the need for `OnNavigatorNavigatedListener` and instead having `navigate` return the `NavDestination` that was navigated to.
- `Navigator` instances can no longer send pop events to the `NavController`. Consider using a [`OnBackPressedCallback`](https://developer.android.com/reference/androidx/activity/OnBackPressedCallback) to intercept back button presses and call `navController.popBackStack()`. [aosp/833716](https://android-review.googlesource.com/833716)

**Bug Fixes**

- `popUpTo` now works consistently when the destination is a `<navigation>` element [b/116831650](https://issuetracker.google.com/116831650)
- Fixed a number of bugs that resulted in an `IllegalArgumentException` when using nested graphs [b/118713731](https://issuetracker.google.com/118713731) [b/113611083](https://issuetracker.google.com/113611083) [b/113346925](https://issuetracker.google.com/113346925) [b/113305559](https://issuetracker.google.com/113305559)
- The `dataPattern` attribute of `<activity>` destinations will now populate arguments from non-String arguments by calling `toString()` [b/120161365](https://issuetracker.google.com/120161365)

**Safe Args**

- Safe Args supports Serializable objects, including Enum values. Enum types can set a default value by using the enum literal without the class name (e.g. `app:defaultValue="READ"`) [b/111316353](https://issuetracker.google.com/111316353)
- Safe Args supports arrays of all supported types [b/111487504](https://issuetracker.google.com/111487504)
- Safe Args now ignores subfolders of resource directories [b/117893516](https://issuetracker.google.com/117893516)
- Safe Args adds `@Override` annotations where appropriate [b/117145301](https://issuetracker.google.com/117145301)

### Version 1.0.0-alpha07

October 29, 2018

**New Features**

- A new [AppBarConfiguration](https://developer.android.com/reference/androidx/navigation/ui/AppBarConfiguration) class allows you to customize which destinations are considered *top-level* destinations. See the [updated documentation](https://developer.android.com/topic/libraries/architecture/navigation/navigation-ui) for details. [b/117333663](https://issuetracker.google.com/117333663)
- You can now pass arguments to the start destination of your graph [b/110300470](https://issuetracker.google.com/110300470)
- Deep links now support custom schemes with periods, hyphens, and plus signs. [b/112806402](https://issuetracker.google.com/112806402)

**Breaking Changes**

- The `navigation-testing-ktx` module has been folded into the `navigation-testing artifact` and will no longer be published.
- The `navigation-testing` artifact now has a dependency on the Kotlin standard library. The API has been changed to be more consistent with Kotlin conventions, but you can continue to use it for tests written in Java.
- Metadata manifest registered navigation graphs are no longer supported. [b/118355937](https://issuetracker.google.com/118355937)
- Actions can no longer be attached to \<activity\> destinations. [aosp/785539](https://android-review.googlesource.com/c/platform/frameworks/support/+/785539)

**Bug Fixes**

- Deep links now correctly parse query parameters. [b/110057514](https://issuetracker.google.com/110057514)
- Activity destinations now correctly apply all enter and exit animations. [b/117145284](https://issuetracker.google.com/117145284)
- Fixed crash that occurs after configuration changes when using custom Navigators. [b/110763345](https://issuetracker.google.com/110763345)

**Safe Args**

- Safe args now have a fixed dependency on Android Gradle Plugin 3.2.1. [b/113167627](https://issuetracker.google.com/113167627)
- Directions can now be generated for inner classes. [b/117407555](https://issuetracker.google.com/117407555)
- Fixed an issue with generating Directions to an \<include\> graph. [b/116542123](https://issuetracker.google.com/116542123)

### Version 1.0.0-alpha06

September 20, 2018

**New Features**

- Shared Element Transitions for Fragment and Activity destinations are now supported [b/79665225](https://issuetracker.google.com/79665225). For more information, see [Implement navigation with the Navigation Architecture Component](https://developer.android.com/topic/libraries/architecture/navigation/navigation-implementing#shared-element)
- Selecting an item in `NavigationView` will now close any containing bottom sheet [b/112158843](https://issuetracker.google.com/112158843)

**API Changes**

- **Breaking Change:** The Navigator `navigate()` method now takes a `Navigator.Extras` parameter.
- NavController's `getGraph()` method is now `NonNull` [b/112243286](https://issuetracker.google.com/112243286)

**Bug Fixes**

- `NavigationUI.setupWithNavController()` no longer leaks views if used with views from individual destinations [b/111961977](https://issuetracker.google.com/111961977)
- Navigator `onSaveState()` is now only called once [b/112627079](https://issuetracker.google.com/112627079)

**Safe Args**

- Navigation destination Directions classes now extend their parent's Directions class if it exists [b/79871405](https://issuetracker.google.com/79871405)
- Directions and Args classes now have a useful `toString()` implementation [b/111843389](https://issuetracker.google.com/111843389)

### Version 1.0.0-alpha05

August 10, 2018

**Bug Fixes**

- Fix a bug which cause incorrect backstack behavior. [b/111907708](https://issuetracker.google.com/issues/111907708)
- Fix a bug in `equals()` of Generated Args classes. [b/111450897](https://issuetracker.google.com/issues/111450897)
- Fix a build failure in Safe Args. [b/109409713](https://issuetracker.google.com/issues/109409713)
- Fix a conversion from resource identifiers to java names [b/111602491](https://issuetracker.google.com/issues/111602491)
- Fix error messages about nullability in Safe Args plugin.
- Add missing nullability annotations.

### Version 1.0.0-alpha04

July 19, 2018

Navigation `1.0.0-alpha04` and the associated Safe Args gradle plugin contains a number of API changes, behavior changes, and bug fixes.

**API / Behavior Changes**

- NavHostFragment will always set the current Fragment as the primary navigation fragment, ensuring that child fragment managers are popped before the outer NavController is popped [b/111345778](https://issuetracker.google.com/issues/111345778)

**Safe Args**

- **Breaking Change:** `app:type` has been changed to `app:argType` to avoid conflicts with other libraries such as ConstraintLayout 2.0.0-alpha1 [b/111110548](https://issuetracker.google.com/issues/111110548)
- Error messages from Safe Args are now clickable [b/111534438](https://issuetracker.google.com/issues/111534438)
- Args classes now confirms that `NonNull` attributes are actually not null [b/111451769](https://issuetracker.google.com/issues/111451769)
- Additional `NonNull` annotations have been added to NavDirections and Args generated classes [b/111455455](https://issuetracker.google.com/issues/111455455) [b/111455456](https://issuetracker.google.com/issues/111455456)

**Bug Fixes**

- Fixed an issue with the system back button after deep linking to a fragment destination [b/111515685](https://issuetracker.google.com/issues/111515685)

### Version 1.0.0-alpha03

July 12, 2018

Navigation `1.0.0-alpha03` and the associated Safe Args gradle plugin contains a number of API changes, behavior changes, and bug fixes.

**API / Behavior Changes**

- A NavigationUI.setupWithNavController method for Toolbar has been added [b/109868820](https://issuetracker.google.com/issues/109868820)
- A NavigationUI.setupWithNavController method for CollapsingToolbarLayout has been added [b/110887183](https://issuetracker.google.com/issues/110887183)
- popBackStack() now returns false when the back stack is empty or when the given destination ID is not in the back stack [b/110893637](https://issuetracker.google.com/issues/110893637)
- FragmentNavigator now ignores navigation operations after FragmentManager has saved state, avoiding "Can not perform this action after onSaveInstanceState" exceptions [b/110987825](https://issuetracker.google.com/issues/110987825)

**Safe Args**

- **Breaking Change:** Non-alphanumeric characters in action and argument names will be replaced by camel casing in the respective NavDirections method names
  - E.g. `DemoController.index` will become `setDemoControllerIndex` [b/79995048](https://issuetracker.google.com/issues/79995048)
  - E.g. `action_show_settings` will become `actionShowSettings` [b/79642240](https://issuetracker.google.com/issues/79642240)
- **Breaking Change:** Arguments are now considered non-null by default. To allow null values on string and parcelable arguments, add `app:nullable="true"` [b/79642307](https://issuetracker.google.com/issues/79642307)
- You can now use `app:type="long"` with defaultValues in the form of "123L" [b/79563966](https://issuetracker.google.com/issues/79563966)
- Parcelable arguments are now supported, using a fully qualified class name for `app:type`. The only default value supported is `"@null"` [b/79563966](https://issuetracker.google.com/issues/79563966)
- Args classes now implement `equals()` and `hashCode()` [b/79642246](https://issuetracker.google.com/issues/79642246)
- The Safe Args plugin can now be applied to library projects [b/80036553](https://issuetracker.google.com/issues/80036553)
- The Safe Args plugin can now be applied to feature projects [b/110011752](https://issuetracker.google.com/issues/110011752)

**Bug Fixes**

- Fixed issues when navigating during Fragment lifecycle methods [b/109916080](https://issuetracker.google.com/issues/109916080)
- Fixed issues when navigating through nested graphs multiple times [b/110178671](https://issuetracker.google.com/issues/110178671)
- Fixed issues when using `setPopUpTo` with the first destination in the graph [b/109909461](https://issuetracker.google.com/issues/109909461)
- Fixed issue where all `app:defaultValue` values were being passed as Strings [b/110710788](https://issuetracker.google.com/issues/110710788)
- aapt2 bundled with Android Gradle Plugin 3.2 Beta 01 now adds keep rules for every `android:name` attribute in Navigation XML files [b/79874119](https://issuetracker.google.com/issues/79874119)
- Fixed memory leak when replacing the default FragmentNavigator [b/110900142](https://issuetracker.google.com/issues/110900142)

### Version 1.0.0-alpha02

June 7, 2018

**Behavior Changes**

- `FragmentNavigator` now uses `setReorderingAllowed(true)`. [b/109826220](https://issuetracker.google.com/issues/109826220)

- Navigation now URLDecodes arguments parsed from deep links URLs. [b/79982454](https://issuetracker.google.com/issues/79982454)

**Bug Fixes**

- Fixed an `IllegalStateException` when calling navigate from Fragment lifecycle methods. [b/79632233](https://issuetracker.google.com/issues/79632233)

- Navigation now depends on Support Library 27.1.1 to fix flickering when using animations. [b/80160903](https://issuetracker.google.com/issues/80160903)

- Fixed an `IllegalArgumentException` when using defaultNavHost="true" as a child fragment. [b/79656847](https://issuetracker.google.com/issues/79656847)

- Fixed a `StackOverflowError` when using NavDeepLinkBuilder. [b/109653065](https://issuetracker.google.com/issues/109653065)

- Fixed an `IllegalArgumentException` when navigating back to a nested graph. [b/80453447](https://issuetracker.google.com/issues/80453447)

- Fixed an issue with overlapping Fragments when using `launchSingleTop`. [b/79407969](https://issuetracker.google.com/issues/79407969)

- Navigation now builds the correct synthetic back stack for nested graphs. [b/79734195](https://issuetracker.google.com/issues/79734195)

- NavigationUI will now highlight the correct item when using a nested graph as a `MenuItem`. [b/109675998](https://issuetracker.google.com/issues/109675998)

**API Changes**

- The `clearTask` attribute for actions and the associated API in `NavOptions` has been deprecated. [b/80338878](https://issuetracker.google.com/issues/80338878)

- The `launchDocument` attribute for actions and the associated API in `NavOptions` has been deprecated. [b/109806636](https://issuetracker.google.com/issues/109806636)

### Version 1.0.0-alpha01

May 8, 2018

[Navigation](https://developer.android.com/topic/libraries/architecture/navigation/navigation-implementing) provides a framework for building in-app
navigation. This initial release is `1.0.0-alpha01`.