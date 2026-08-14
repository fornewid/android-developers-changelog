---
title: https://developer.android.com/build/releases/agp-3-4-0-release-notes
url: https://developer.android.com/build/releases/agp-3-4-0-release-notes
source: md.txt
---

<br />

# Android Gradle Plugin 3.4.0 (April 2019)

This version of the Android plugin requires the following:

|   | Minimum version | Default version | Notes |
|---:|:---:|:---:|:---:|
| Gradle | 5.1.1 | 5.1.1 | To learn more, see [updating Gradle](https://developer.android.com/build/releases/gradle-plugin?buildsystem=ndk-build#updating-gradle). When using Gradle 5.0 and higher, the default Gradle daemon memory heap size decreases from 1 GB to 512 MB. This might result in a build performance regression. To override this default setting, specify the Gradle daemon heap size in your project's gradle.properties file. |
| SDK Build Tools | 28.0.3 | 28.0.3 | [Install](https://developer.android.com/studio/intro/update#sdk-manager) or [configure](https://developer.android.com/tools/releases/build-tools) SDK Build Tools. |

**3.4.3 (July 2020)**


This minor update supports compatibility with new default settings and
features for
[package visibility
in Android 11](https://developer.android.com/about/versions/11/privacy/package-visibility).


See the [4.0.1 release notes](https://developer.android.com/build/releases/agp-3-4-0-release-notes#4.0.1) for details.

**3.4.2 (July 2019)**


This minor update supports Android Studio 3.4.2 and includes various bug
fixes and performance improvements.
To see a list of noteable bug fixes, read the related post on the
[Release Updates blog](https://androidstudio.googleblog.com/2019/07/android-studio-342-available.html).

**3.4.1 (May 2019)**


This minor update supports Android Studio 3.4.1 and includes various bug
fixes and performance improvements.
To see a list of noteable bug fixes, read the related post on the
[Release Updates blog](https://androidstudio.googleblog.com/2019/05/android-studio-341-available.html).

<br />

<br />

## New features

- **New lint check dependency configurations:** The
  behavior of `lintChecks` has changed and a new dependency
  configuration, `lintPublish`, has been introduced to give
  you more control over which lint checks are packaged in your Android
  libraries.

  - `lintChecks`: This is an existing configuration that you should use for lint checks you want to only run when building your project locally. If you were previously using the `lintChecks` dependency configuration to include lint checks in the published AAR, you need to migrate those dependencies to instead use the new `lintPublish` configuration described below.
  - `lintPublish`: Use this new configuration in library projects for lint checks you want to include in the published AAR, as shown below. This means that projects that consume your library also apply those lint checks.

  The following code sample uses both dependency configurations in a
  local Android library project.

  ```groovy
  dependencies {
    // Executes lint checks from the ':lint' project at build time.
    lintChecks project(':lint')
    // Packages lint checks from the ':lintpublish' in the published AAR.
    lintPublish project(':lintpublish')
  }
          
  ```

  ```kotlin
  dependencies {
    // Executes lint checks from the ':lint' project at build time.
    lintChecks(project(":lint"))
    // Packages lint checks from the ':lintpublish' in the published AAR.
    lintPublish(project(":lintpublish"))
      }
          
  ```
  - In general, packaging and signing tasks should see an overall build
    speed improvement. If you notice a performance regression related to
    these tasks, please [report a bug](https://developer.android.com/studio/report-bugs).

<br />

<br />

## Behavior changes

- **Android Instant Apps Feature plugin deprecation
  warning:** If you're still using the
  `com.android.feature` plugin to build your instant app,
  Android Gradle plugin 3.4.0 will give throw you a deprecation warning.
  To make sure you can still build you instant app on future versions of
  the plugin, migrate your instant app to using
  [the dynamic feature plugin](https://developer.android.com/studio/projects/dynamic-delivery),
  which also allows you to publish both your installed and instant app
  experiences from a single Android App Bundle.

- **R8 enabled by default:** R8 integrates desugaring,
  shrinking, obfuscating, optimizing, and dexing all in one step---resulting
  in
  [noticeable build performance
  improvements](https://www.google.com/url?q=https://android-developers.googleblog.com/2018/11/r8-new-code-shrinker-from-google-is.html&sa=D&ust=1551922493258000&usg=AFQjCNH0N1wuMX645n7giw0wjikzjm3WCA). R8 was introduced in Android Gradle plugin 3.3.0 and
  is now enabled by default for both app and Android library projects
  using plugin 3.4.0 and higher.

The image below provides a high-level overview of the compile process
before R8 was introduced.
![Before R8, ProGuard was a different compile step from dexing and
desugaring.](https://developer.android.com/static/studio/images/build/r8/compile_with_d8_proguard.png)

Now, with R8, desugaring, shrinking, obfuscating, optimizing, and dexing (D8)
are all completed in one step, as illustrated below.
![With R8, desugaring, shrinking, obfuscating, optimizing, and
dexing are all performed in a single compile step.](https://developer.android.com/static/studio/images/build/r8/compile_with_r8.png)

Keep in mind, R8 is designed to work with your existing ProGuard rules, so
you'll likely not need to take any actions to benefit from R8. However,
because it's a different technology to ProGuard that's designed specifically
for Android projects, shrinking and optimization may result in removing code
that ProGuard may have not. So, in this unlikely situation, you might need
to add additional rules to keep that code in your build output.

If you experience issues using R8, read the
[R8 compatibility FAQ](https://r8.googlesource.com/r8/+/refs/heads/master/compatibility-faq.md)
to check if there's a solution to your issue. If a solution isn't documented,
please [report a bug](https://issuetracker.google.com/issues/new?component=326788&template=1025938).
You can disable R8 by adding one of the following lines to your project's
`gradle.properties` file:

          # Disables R8 for Android Library modules only.
          android.enableR8.libraries = false
          # Disables R8 for all modules.
          android.enableR8 = false
          
        
**Note:** For a given build type, if you set
`useProguard` to `false` in your app
module's `build.gradle` file, the Android Gradle plugin uses R8
to shrink your app's code for that build type, regardless of whether you
disable R8 in your project's `gradle.properties` file.

- **`ndkCompile` is deprecated:** You now get a build error if you try to use `ndkBuild` to compile your native libraries. You should instead use either CMake or ndk-build to [Add C and C++ code to your
  project](https://developer.android.com/studio/projects/add-native-code).

<br />

<br />

## Known issues

- The correct usage of unique package names are currently not enforced
  but will become more strict on later versions of the plugin. On Android
  Gradle plugin version 3.4.0, you can opt-in to check whether your
  project declares acceptable package names by adding the line below to
  your `gradle.properties` file.

                android.uniquePackageNames = true
                
              
  To learn more about setting a package name through the Android Gradle
  plugin, see
  [Set the application ID](https://developer.android.com/studio/build/configure-app-module#set_the_application_id).

<br />