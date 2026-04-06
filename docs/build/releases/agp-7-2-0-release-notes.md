---
title: https://developer.android.com/build/releases/agp-7-2-0-release-notes
url: https://developer.android.com/build/releases/agp-7-2-0-release-notes
source: md.txt
---

# Android Gradle Plugin 7.2.0 (May 2022)

Android Gradle plugin 7.2.0 is a major release that includes a variety of
new features and improvements.
**7.2.2 (August 2022)**

This minor update corresponds to the release of Android Studio Chipmunk
Patch 2 and includes the following bug fixes:

- [Issue #232438924](https://issuetracker.google.com/issues/232438924): AndroidGradlePlugin version 7.2 breaks transform API when used along with ASM API
- [Issue #231037948](https://issuetracker.google.com/issues/231037948): AGP 7.2.0-rc01 :buildSrc:generatePrecompiledScriptPluginAccessors - shadow/bundletool/com/android/prefs/AndroidLocation$AndroidLocationException

**7.2.1 (May 2022)**


This minor update corresponds to the release of Android Studio Chipmunk
Patch 1 and includes the following bug fixes:

- [Issue #230361284](https://issuetracker.google.com/issues/230361284): bundletool does not package baseline profiles correctly


To see the other bug fixes included in this release, see the
[Android Studio Chipmunk Patch 1
release notes](https://developer.android.com/studio/releases#patch-releases).

## Compatibility

|   | Minimum version | Default version | Notes |
|---:|:---:|:---:|:---:|
| Gradle | 7.3.3 | 7.3.3 | To learn more, see [updating Gradle](https://developer.android.com/build/releases/gradle-plugin?buildsystem=ndk-build#updating-gradle). |
| SDK Build Tools | 30.0.3 | 30.0.3 | [Install](https://developer.android.com/studio/intro/update#sdk-manager) or [configure](https://developer.android.com/tools/releases/build-tools) SDK Build Tools. |
| NDK | N/A | 21.4.7075529 | [Install](https://developer.android.com/studio/projects/install-ndk#specific-version) or [configure](https://developer.android.com/studio/projects/install-ndk#apply-specific-version) a different version of the NDK. |
| JDK | 11 | 11 | To learn more, see [setting the JDK version](https://developer.android.com/studio/intro/studio-config#jdk). |

## Jetifier warning and check in Build Analyzer

Build Analyzer now displays a warning if your project's
`gradle.properties` file includes
`android.enableJetifier=true`. This flag was introduced in a
previous version of Android Studio to enable AndroidX for libraries that don't
support AndroidX natively. However, the library ecosystem has mostly moved to
support AndroidX natively and the Jetifier flag is probably no longer needed by
your project. Additionally, the flag can lead to slower build performance. If
you see this warning, you can run a check within Build Analyzer to confirm if
the flag can be removed.

## Support for test fixtures

Starting with Android Studio Chipmunk Beta 1, Android Studio supports both
Android and Java test fixtures. See Gradle's guide on [using test fixtures](https://docs.gradle.org/current/userguide/java_testing.html#sec:java_test_fixtures){:.external}
for more information on the test fixtures feature and how to use it in a Java project.

To enable test fixtures in your Android library module, add the following to
your library-level `build.gradle` file:

    android {
      testFixtures {
        enable true
        // enable testFixtures's android resources (disabled by default)
        // androidResources true
      }
    }

By default, publishing your library also publishes the test fixtures AAR with
the main library. The Gradle Module Metadata file will contain information for
Gradle to be able to consume the right artifact when requesting the
`testFixtures` component.

To disable publishing the test fixtures AAR of a library in the release variant,
add the following to your library-level `build.gradle` file:

    afterEvaluate {
      components.release.withVariantsFromConfiguration(
        configurations.releaseTestFixturesVariantReleaseApiPublication) { skip() }
      components.release.withVariantsFromConfiguration(
        configurations.releaseTestFixturesVariantReleaseRuntimePublication) { skip() }
    }

To consume the test fixtures AAR of a published Android library, you can use
Gradle's helper method `testFixtures()`.

    dependencies {
      testImplementation testFixtures('com.example.company:publishedLib:1.0')
    }

By default, lint will analyze test fixtures sources. You can configure
lint to ignore test fixtures sources as follows:

    android {
      lint {
        ignoreTestFixturesSources true
      }
    }

## Duplicate content roots not supported

Starting with AGP 7.2, you can no longer share the same source
directory across multiple source sets. For example, you can't use the same
test sources for both unit tests and instrumentation tests. To learn more,
see [Change the
default source sets configurations](https://developer.android.com/studio/build/build-variants#configure-sourcesets).