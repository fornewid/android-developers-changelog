---
title: https://developer.android.com/build/releases/agp-3-6-0-release-notes
url: https://developer.android.com/build/releases/agp-3-6-0-release-notes
source: md.txt
---

<br />

# Android Gradle Plugin 3.6.0 (February 2020)

This version of the Android plugin requires the following:

|   | Minimum version | Default version | Notes |
|---:|:---:|:---:|:---:|
| Gradle | 5.6.4 | 5.6.4 | To learn more, see [updating Gradle](https://developer.android.com/build/releases/gradle-plugin?buildsystem=ndk-build#updating-gradle). |
| SDK Build Tools | 28.0.3 | 28.0.3 | [Install](https://developer.android.com/studio/intro/update#sdk-manager) or [configure](https://developer.android.com/tools/releases/build-tools) SDK Build Tools. |

**3.6.4 (July 2020)**


This minor update supports compatibility with new default settings and
features for
[package visibility
in Android 11](https://developer.android.com/about/versions/11/privacy/package-visibility).


See the [4.0.1 release notes](https://developer.android.com/build/releases/agp-3-6-0-release-notes#4.0.1) for details.

## New features

This version of the Android Gradle plugin includes the following new
features.

### View Binding

View binding provides compile-time safety when referencing views in
your code. You can now replace `findViewById()` with the
auto-generated binding class reference. To start using View binding,
include the following in each module's `build.gradle` file:

```groovy
      android {
          viewBinding.enabled = true
      }
      
```

```kotlin
      android {
          viewBinding.enabled = true
      }
      
```

To learn more, read the [View
Binding documentation](https://developer.android.com/topic/libraries/view-binding).

### Support for the Maven Publish plugin

The Android Gradle plugin includes support for the
[Maven
Publish Gradle plugin](https://docs.gradle.org/current/userguide/publishing_maven.html), which allows you to publish build artifacts to
an Apache Maven repository. The Android Gradle plugin creates a
[*component*](https://docs.gradle.org/current/userguide/dependency_management_terminology.html#sub:terminology_component)
for each build variant artifact in your app or library module that you can
use to customize a
[*publication*](https://docs.gradle.org/current/userguide/publishing_maven.html#publishing_maven:publications)
to a Maven repository.

To learn more, go to the page about how to
[use the Maven Publish
plugin](https://developer.android.com/studio/build/maven-publish-plugin).

### New default packaging tool

When building the debug version of your app, the plugin uses a new
packaging tool, called *zipflinger* , to build your APK. This new
tool should provide build speed improvements. If the new packaging tool
doesn't work as you expect,
please [report a bug](https://developer.android.com/studio/report-bugs). You can revert to
using the old packaging tool by including the following in your
`gradle.properties` file:

            android.useNewApkCreator=false
          
### Native build attribution

You can now determine the length of time it takes Clang to build and
link each C/C++ file in your project. Gradle can output a Chrome trace
that contains timestamps for these compiler events so you can better
understand the time required to build your project. To output this build
attribution file, do the following:

1. Add the flag `-Pandroid.enableProfileJson=true` when
   running a Gradle build. For example:

   `gradlew assembleDebug -Pandroid.enableProfileJson=true`
2. Open the Chrome browser and type `chrome://tracing` in
   the search bar.

3. Click the **Load** button and navigate to
   `<var>project-root</var>/build/android-profile`
   to find the file. The file is named
   `profile-<var>timestamp</var>.json.gz`.

You can see the native build attribution data near the top of the
viewer:

![Native build attribution trace in Chrome](https://developer.android.com/static/studio/images/releases/native-build-attribution.png)

<br />

<br />

## Behavior changes

When using this version of the plugin, you might encounter the following
changes in behavior.

### Native libraries packaged uncompressed by
default

When you build your app, the plugin now sets
`extractNativeLibs` to `"false"` by
default. That is, your native libraries are page aligned and packaged
uncompressed. While this results in a larger upload size, your users
benefit from the following:

- Smaller app install size because the platform can access the native libraries directly from the installed APK, without creating a copy of the libraries.
- Smaller download size because Play Store compression is typically better when you include uncompressed native libraries in your APK or Android App Bundle.

If you want the Android Gradle plugin to instead package compressed
native libraries, include the following in your app's manifest:

            <application
              android:extractNativeLibs="true"
              ... >
            </application>
            
          
**Note:** The `extractNativeLibs` manifest
attribute has been replaced by the `useLegacyPackaging` DSL
option. For more information, see the release note
[Use the DSL to package compressed
native libraries](https://developer.android.com/build/releases/agp-3-6-0-release-notes#compress-native-libs-dsl).

### Default NDK version

If you download multiple versions of the NDK, the Android Gradle plugin
now selects a default version to use in compiling your source code files.
Previously, the plugin selected the latest downloaded version of the NDK.
Use the `android.ndkVersion` property in the module's
`build.gradle` file to override the plugin-selected default.

### Simplified R class generation

The Android Gradle plugin simplifies the compile classpath by
generating only one R class for each library module in your project and
sharing those R classes with other module dependencies. This optimization
should result in faster builds, but it requires that you keep the
following in mind:

- Because the compiler shares R classes with upstream module dependencies, it's important that each module in your project uses a unique package name.
- The visibility of a library's R class to other project dependencies is determined by the configuration used to include the library as a dependency. For example, if Library A includes Library B as an 'api' dependency, Library A and other libraries that depend on Library A have access to Library B's R class. However, other libraries might not have access to Library B's R class. If Library A uses the `implementation` dependency configuration. To learn more, read about [dependency
  configurations](https://developer.android.com/studio/build/dependencies#dependency_configurations).

### Remove resources missing from default
configuration

For Library modules, if you include a resource for a language that you
do not include in the default set of resources---for example, if you include
`hello_world` as a string resource in
`/values-es/strings.xml` but you don't define that resource in
`/values/strings.xml`---the Android Gradle plugin no longer
includes that resource when compiling your project. This behavior change
should result in fewer `Resource Not Found` runtime exceptions
and improved build speed.

### D8 now respects CLASS retention policy
for annotations

When compiling your app, D8 now respects when annotations apply a CLASS
retention policy, and those annotations are no longer available at
runtime. This behavior also exists when setting the app's target SDK to
API level 23, which previously allowed access to these annotations during
runtime when compiling your app using older versions of the Android Gradle
plugin and D8.

### Other behavior changes

- `aaptOptions.noCompress` is no longer case sensitive on all platforms (for both APK and bundles) and respects paths that use uppercase characters.
- Data binding is now incremental by default. To learn more, see
  [issue #110061530](https://issuetracker.google.com/110061530).

- All unit tests, including Roboelectric unit tests, are now fully
  cacheable. To learn more, see
  [issue #115873047](https://issuetracker.google.com/115873047).

<br />

<br />

## Bug fixes

This version of the Android Gradle plugin includes the following bug
fixes:

- Robolectric unit tests are now supported in library modules that use data binding. To learn more, see [issue #126775542](https://issuetracker.google.com/126775542).
- You can now run `connectedAndroidTest` tasks across multiple modules while Gradle's [parallel
  execution mode](https://guides.gradle.org/performance/#parallel_execution) is enabled.

<br />

<br />

## Known issues

This section describes known issues that exist in Android Gradle plugin
3.6.0.

### Slow performance of Android Lint task

Android Lint can take much longer to complete on some projects due to a
regression in its parsing infrastructure, resulting in slower computation
of inferred types for lambdas in certain code constructs.

The issue is reported as
[a bug in IDEA](https://youtrack.jetbrains.com/issue/IDEA-229655)
and will be fixed in Android Gradle Plugin 4.0.

### Missing Manifest class {:#agp-missing-manifest}

If your app defines custom permissions in its manifest, the Android
Gradle plugin typically generates a `Manifest.java` class that
includes your custom permissions as string constants. The plugin packages
this class with your app, so you can more easily reference those
permissions at runtime.

Generating the manifest class is broken in Android Gradle plugin 3.6.0.
If you build your app with this version of the plugin, and it references
the manifest class, you might see a `ClassNotFoundException`
exception. To resolve this issue, do one of the following:

- Reference your custom permissions by their fully-qualified name.
  For example,
  `"com.example.myapp.permission.DEADLY_ACTIVITY"`.

- Define your own constants, as shown below:

                  public final class CustomPermissions {
                    public static final class permission {
                      public static final String DEADLY_ACTIVITY="com.example.myapp.permission.DEADLY_ACTIVITY";
                    }
                  }
                  
                
<br />