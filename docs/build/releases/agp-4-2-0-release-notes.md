---
title: Android Studio  |  Android Developers
url: https://developer.android.com/build/releases/agp-4-2-0-release-notes
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Android Studio](https://developer.android.com/studio)
* [Gradle build guides](https://developer.android.com/build/releases/past-releases)

Stay organized with collections

Save and categorize content based on your preferences.



# Android Gradle Plugin 4.2.0 (March 2021)

## Compatibility

|  | Minimum version | Default version | Notes |
| --- | --- | --- | --- |
| Gradle | 6.7.1 | N/A | To learn more, see [updating Gradle](/build/releases/gradle-plugin?buildsystem=ndk-build#updating-gradle). |
| SDK Build Tools | 30.0.2 | 30.0.2 | [Install](/studio/intro/update#sdk-manager) or [configure](/tools/releases/build-tools) SDK Build Tools. |
| NDK | N/A | 21.4.7075529 | [Install](/studio/projects/install-ndk#specific-version) or [configure](/studio/projects/install-ndk#apply-specific-version) a different version of the NDK. |

## New features

This version of the Android Gradle plugin includes the following new features.

### Java language version 8 by default

Starting in version 4.2, AGP will use the Java 8 language level by default.
Java 8 provides access to a number of newer language features including lambda
expressions, method references, and static interface methods. For the full list
of supported features see the [Java 8 documentation](/studio/write/java8-support#supported_features).

To keep the old behavior, specify Java 7 explicitly in your module-level
`build.gradle.kts` or `build.gradle` file:

```
// build.gradle
android {
  ...
  compileOptions {
    sourceCompatibility JavaVersion.VERSION_1_7
    targetCompatibility JavaVersion.VERSION_1_7
  }
  // For Kotlin projects, compile to Java 6 instead of 7
  kotlinOptions {
    jvmTarget = "1.6"
  }
}
```

```
// build.gradle.kts
android {
  ...
  compileOptions {
    sourceCompatibility = JavaVersion.VERSION_1_7
    targetCompatibility = JavaVersion.VERSION_1_7
  }
  // For Kotlin projects, compile to Java 6 instead of 7
  kotlinOptions {
    jvmTarget = "1.6"
  }
}
```

### New JVM resource compiler

A new JVM resource compiler in Android Gradle plugin 4.2 tool replaces portions
of the [AAPT2 resource compiler](/studio/command-line/aapt2), potentially
improving build performance, especially on Windows machines. The new JVM
resource compiler is enabled by default.

### v3 and v4 signing now supported

Android Gradle Plugin 4.2 now supports [APK v3](https://source.android.com/security/apksigning/v3)
and [APK v4](https://source.android.com/security/apksigning/v4) signing formats.
To enable one or both of these formats in your
build, add the following properties to your module-level `build.gradle`
or `build.gradle.kts` file:

```
// build.gradle
android {
  ...
  signingConfigs {
    config {
        ...
        enableV3Signing true
        enableV4Signing true
    }
  }
}
```

```
// build.gradle.kts
android {
  ...
  signingConfigs {
      config {
          ...
          enableV3Signing = true
          enableV4Signing = true
      }
  }
}
```

APK v4 signing allows you to quickly deploy large APKs using the [ADB
Incremental APK installation](/about/versions/11/features#incremental) in
Android 11. This new flag takes care of the APK signing step in the deployment
process.

### Configure app signing per variant

It is now possible to [enable or disable app signing](/reference/tools/gradle-api/4.2/com/android/build/api/variant/SigningConfig#summary) in Android Gradle
plugin per variant.

This example demonstrates how to set app signing per variant using the
[`onVariants()`](/reference/tools/gradle-api/4.2/com/android/build/api/extension/AndroidComponentsExtension#onvariants)
method in either Kotlin or Groovy:

```
androidComponents {
    onVariants(selector().withName("fooDebug"), {
        signingConfig.enableV1Signing.set(false)
        signingConfig.enableV2Signing.set(true)
    })
```

### New Gradle property: `android.native.buildOutput`

To reduce clutter in build output, AGP 4.2 filters messages
from native builds that use [CMake](/ndk/guides/cmake) and [`ndk-build`](/ndk/guides/ndk-build),
displaying only C/C++ compiler output by default. Previously, a line of output
was generated for every file that was built, resulting in a large quantity of
informational messages.

If you would like to see the entirety of the native output, set the new
Gradle property `android.native.buildOutput` to `verbose`.

You can set this property in either the `gradle.properties` file or through the
command line.

*gradle.properties*   
`android.native.buildOutput=verbose`

*Command line*   
`-Pandroid.native.buildOutput=verbose`

The default value of this property is `quiet`.

## Behavior change for gradle.properties files

Starting in AGP 4.2, it is no longer possible to override Gradle properties
from subprojects. In other words, if you declare a property in a
`gradle.properties` file in a subproject instead of the root
project, it will be ignored.

As an example, in previous releases, AGP would read values from
`<var>projectDir</var>/gradle.properties`,
`<var>projectDir</var>/app/gradle.properties`,
`<var>projectDir</var>/library/gradle.properties`,
etc. For app modules, if the same Gradle property was present in both
`<var>projectDir</var>/gradle.properties`
and
`<var>projectDir</var>/app/gradle.properties`,
the value from
`<var>projectDir</var>/app/gradle.properties`
would take precedence.

In AGP 4.2, this behavior has been changed, and AGP won't load values from
`gradle.properties` in subprojects (e.g.,
`<var>projectDir</var>/app/gradle.properties`).
This change reflects the
[new Gradle behavior](https://docs.gradle.org/current/userguide/build_environment.html#sec:gradle_configuration_properties) and supports
[configuration caching](https://medium.com/androiddevelopers/configuration-caching-deep-dive-bcb304698070)

For more information on setting values in `gradle.properties`
files, see the
[Gradle docs](https://docs.gradle.org/current/userguide/build_environment.html#sec:gradle_configuration_properties      class=).

## Gradle compatibility and configuration changes

When running in Android Studio, the Gradle build tool uses Studio's bundled JDK.
In previous releases, JDK 8 was bundled with Studio. In 4.2,
however, JDK 11 is now bundled instead. When using the new bundled JDK to run
Gradle, this may result in some incompatibility or impact JVM performance
due to changes to the garbage collector. These issues are described below.

**Note:** Although we recommend running Gradle with JDK 11, it is
possible to change the JDK used to run Gradle in the
[**Project Structure**](/studio/projects#ProjectStructure)
dialog. Changing this setting will only change the JDK used to run Gradle, and
will not change the JDK used to run Studio itself.

### Studio compatibility with Android Gradle plugin (AGP)

Android Studio 4.2 can open projects that use AGP 3.1 and
higher provided that AGP is running Gradle 4.8.1 and higher. For more
information about Gradle compatibility, see
[Update Gradle](#updating-gradle).

### Optimizing Gradle builds for JDK 11

This update to JDK 11 impacts the default configuration of the JVM garbage
collector, since JDK 8 uses the parallel garbage collector while JDK 11 uses
[the
G1 garbage collector](https://docs.oracle.com/javase/9/gctuning/garbage-first-garbage-collector.htm#JSGCT-GUID-ED3AB6D3-FD9B-4447-9EDF-983ED2F7A573).

To potentially improve build performance, we recommend
[testing your Gradle builds](/studio/build/profile-your-build) with the
parallel garbage collector. In `gradle.properties` set the following:

```
org.gradle.jvmargs=-XX:+UseParallelGC
```

If there are other options already set in this field, add a new option:

```
org.gradle.jvmargs=-Xmx1536m -XX:+UseParallelGC
```

To measure build speed with different configurations, see
[Profile your build](/studio/build/profile-your-build).

## DEX files uncompressed in APKs when `minSdk` = 28 or higher

AGP now packages DEX files uncompressed in APKs by default when `minSdk` = 28 or
higher. This causes an increase in APK size, but it results in a smaller
installation size on the device, and the download size is roughly the same.

To force AGP to instead package the DEX files compressed, you can add the
following to your `build.gradle` file:

```
android {
    packagingOptions {
        dex {
            useLegacyPackaging true
        }
    }
}
```

## Use the DSL to package compressed native libraries

We recommend packaging native libraries in uncompressed form, because this
results in a smaller app install size, smaller app download size, and faster app
loading time for your users. However, if you want the Android Gradle plugin to
package compressed native libraries when building your app, set
[`useLegacyPackaging`](/reference/tools/gradle-api/7.1/com/android/build/api/dsl/JniLibsPackagingOptions#uselegacypackaging)
to `true` in your app's `build.gradle` file:

```
android {
    packagingOptions {
        jniLibs {
            useLegacyPackaging true
        }
    }
}
```

The flag `useLegacyPackaging` replaces the manifest attribute `extractNativeLibs`. For more background, see the release note
[Native libraries packaged uncompressed by default](/build/releases/past-releases/agp-3-6-0-release-notes#extractNativeLibs).