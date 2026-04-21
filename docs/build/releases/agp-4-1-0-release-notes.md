---
title: https://developer.android.com/build/releases/agp-4-1-0-release-notes
url: https://developer.android.com/build/releases/agp-4-1-0-release-notes
source: md.txt
---

# Android Gradle Plugin 4.1.0 (August 2020)

<br />

## Compatibility

|   | Minimum version | Default version | Notes |
|---:|:---:|:---:|:---:|
| Gradle | 6.5 | N/A | To learn more, see [updating Gradle](https://developer.android.com/build/releases/gradle-plugin?buildsystem=ndk-build#updating-gradle). |
| SDK Build Tools | 29.0.2 | 29.0.2 | [Install](https://developer.android.com/studio/intro/update#sdk-manager) or [configure](https://developer.android.com/tools/releases/build-tools) SDK Build Tools. |
| NDK | N/A | 21.1.6352462 | [Install](https://developer.android.com/studio/projects/install-ndk#specific-version) or [configure](https://developer.android.com/studio/projects/install-ndk#apply-specific-version) a different version of the NDK. |

<br />

    <p>This version of the Android plugin requires the following:</p>
    <ul>
      <li>
        <p><a href="https://docs.gradle.org/6.5.1/release-notes.html">Gradle 6.5</a>.
        To learn more, read the section about <a href="#updating-gradle">updating
        Gradle</a>.</p>
      </li>
      <li>
        <p><a href="/studio/releases/build-tools.html#notes">SDK Build Tools
        29.0.2</a> or higher.</p>
      </li>
    </ul>
    <p>The default NDK version in this release is 21.1.6352462. To install a
    different NDK version, see <a href="/studio/projects/install-ndk#specific-version">Install a specific version of the NDK</a>.</p>

<br />

## New features

This version of the Android Gradle plugin includes the following new features.

### Kotlin Script DSL support

To help improve the editing experience for Kotlin buildscript users, the DSL
and APIs of Android Gradle plugin 4.1 are now defined in a set of Kotlin
interfaces separately from their implementation classes. This means that:

- Nullability and mutability are now explicitly declared on Kotlin types.
- Documentation generated from those interfaces is published in the [Kotlin API Reference](https://developer.android.com/reference/tools/gradle-api).
- The API surface of the Android Gradle Plugin is clearly defined, to make extending Android builds less brittle in the future.

Important: If you have already adopted KTS build scripts or use Kotlin in
`buildSrc`, this may cause source compatibility breakages for certain errors
that would have manifest as run-time errors in previous releases.

Collection types that are designed to be mutated in the DSL are now uniformly
defined as:

`val collection: MutableCollectionType`

This means that it is no longer possible to write the following
in Kotlin scripts for some collections that previously supported it:

`collection = collectionTypeOf(...)`

However, mutating the collection is supported uniformly so `collection += ...`
and `collection.add(...)` should now work everywhere.

If you discover any issues when upgrading a project that uses Android Gradle
plugin Kotlin APIs and DSL, please [report a bug](https://issuetracker.google.com/issues/new?component=192709&template=842921).

### Export C/C++ dependencies from AARs

Android Gradle plugin 4.0 added the ability to
[import Prefab
packages in AAR dependencies](https://developer.android.com/studio/releases/gradle-plugin#native-dependencies). In AGP 4.1,
it's now possible to export libraries from your external native build in an
AAR for an Android Library project.

To export your native libraries, add the following to the `android` block of
your library project's `build.gradle` file:

```groovy
buildFeatures {
    prefabPublishing true
}

prefab {
    <var>mylibrary</var&;gt {
      headers "src/main/cpp/<var>mylibrary</var>/include"
    }
`<var>myotherlibrary</var> {
    headers "src/main/cpp/<var>myotherlibrary</var>/include"
}
`
}
```

```kotlin
buildFeatures {
    prefabPublishing = true
}

prefab {
    create("<var>mylibrary</var>") {
      headers = "src/main/cpp/<var>mylibrary</var>/include"
    }
`create("<var>myotherlibrary</var>") {
    headers = "src/main/cpp/<var>myotherlibrary</var>/include"
}
`
}
```

In this example, the `mylibrary` and `myotherlibrary`
libraries from either your ndk-build or CMake external native build will
be packaged in the AAR produced by your build, and each will export the
headers from the specified directory to their dependents.

**Note:** For users of Android Gradle plugin 4.0 and
above, the configuration settings for importing prebuilt native libraries
have changed. For more information, see the
[4.0 release notes](https://developer.android.com/build/releases/agp-4-1-0-release-notes#cmake-imported-targets).

<br />

<br />

### R8 support for Kotlin metadata

Kotlin uses custom metadata in Java class files to identify Kotlin language
constructs. R8 now has support for maintaining and rewriting Kotlin
metadata to fully support shrinking of Kotlin libraries and applications
using `kotlin-reflect`.

To keep Kotlin metadata, add the following keep rules:

    -keep class kotlin.Metadata { *; }

    <br />




    `-keepattributes RuntimeVisibleAnnotations`

This will instruct R8 to keep Kotlin metadata for all classes that are
directly kept.

For more information, see [Shrinking Kotlin libraries and applications using Kotlin reflection with R8](https://medium.com/androiddevelopers/shrinking-kotlin-libraries-and-applications-using-kotlin-reflection-with-r8-6fe0a0e2d115){:.external} on Medium.

### Assertions in debug builds

When you build the debug version of your app using Android Gradle
plugin 4.1.0 and higher, the built-in compiler (D8) will rewrite your app's code
to enable assertions at compile time, so you always have assertion checks
active.

<br />

<br />

## Behavior changes

### Android Gradle plugin build cache removed

The AGP build cache was removed in AGP 4.1. Previously
introduced in AGP 2.3 to complement the Gradle build cache, the AGP build cache
was superseded entirely by the Gradle build cache in AGP 4.1. This change does
not impact build time.

The `cleanBuildCache` task and the `android.enableBuildCache` and
`android.buildCacheDir` properties are deprecated and will be removed in
AGP 7.0. The `android.enableBuildCache` property currently has no effect,
while the `android.buildCacheDir` property and the `cleanBuildCache` task
will be functional until AGP 7.0 for deleting any existing AGP build cache
contents.

### App size significantly reduced for apps using code shrinking

Starting with this release, fields from R classes are
[no longer kept by default](https://issuetracker.google.com/142449264), which
may result in significant APK size savings for apps that enable code
shrinking. This should not result in a behavior change unless you
are accessing R classes by reflection, in which case it is necessary to
[add keep rules](https://developer.android.com/studio/build/shrink-code#keep-code) for those R classes.

### android.namespacedRClass property renamed to android.nonTransitiveRClass

The experimental flag `android.namespacedRClass` has been renamed to
`android.nonTransitiveRClass`.

Set in the `gradle.properties` file, this flag enables namespacing of each
library's R class so that its R class includes only the
resources declared in the library itself and none from the library's
dependencies, thereby reducing the size of the R class for that library.

### Kotlin DSL: coreLibraryDesugaringEnabled renamed

The Kotlin DSL compile option `coreLibraryDesugaringEnabled` has been
changed to [`isCoreLibraryDesugaringEnabled`](https://developer.android.com/reference/tools/gradle-api/4.1/com/android/build/api/dsl/CompileOptions#iscorelibrarydesugaringenabled).
For more information about this flag, see
[Java 8+ API desugaring support (Android Gradle Plugin 4.0.0+)](https://developer.android.com/studio/write/java8-support#library-desugaring).

### Version properties removed from BuildConfig class in library projects

For library projects only, the `BuildConfig.VERSION_NAME` and
`BuildConfig.VERSION_CODE` properties have been removed from the generated
`BuildConfig` class because these static values did not reflect the final
values of the application's version code and name, and were therefore
misleading. Additionally, these values were discarded during manifest merging.

In a future version of Android Gradle plugin, the `versionName` and
`versionCode` properties will also be removed from the DSL for libraries.
Currently, there is no way to automatically access the app version code/name
from a library sub-project.

For application modules, there is no change, you can still assign values to
`versionCode` and `versionName` in the DSL; these values will propagate to the
app's manifest and `BuildConfig` fields.

### Set the NDK path

You can set the path to your local NDK installation using the `android.ndkPath`
property in your module's `build.gradle` file.


    android {
      ndkPath "your-custom-ndk-path"
    }


    android {
      ndkPath = "your-custom-ndk-path"
    }

If you use this property together with the
[`android.ndkVersion` property](https://developer.android.com/studio/projects/install-ndk#apply-specific-version),
then this path must contain an NDK version that matches `android.ndkVersion`.

### Library unit test behavior changes

We've changed the behavior of how library unit tests are compiled and run. A
library's unit tests are now compiled and run against compile/runtime classes
of the library itself, resulting in the unit test consuming the library in the
same way external subprojects do. This configuration typically results in
better testing.

In some cases library unit tests that use data binding may encounter missing [`DataBindingComponent`](https://developer.android.com/reference/android/databinding/DataBindingComponent)
or [`BR`](https://developer.android.com/topic/libraries/data-binding/generated-binding#dynamic_variables)
classes. Those tests need to be ported to an instrumented test in the
`androidTest` project, since compiling and running against those classes in
a unit test may produce incorrect output.

## io.fabric Gradle plugin deprecated

The io.fabric Gradle plugin is deprecated and is not compatible with
version 4.1 of the Android Gradle plugin. For more information on the
deprecated Fabric SDK and migrating to the Firebase Crashlytics SDK, see
[Upgrade to the Firebase Crashlytics SDK](https://firebase.google.com/docs/crashlytics/android/get-started).

<br />