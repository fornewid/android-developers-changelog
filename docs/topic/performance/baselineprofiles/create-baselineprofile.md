---
title: https://developer.android.com/topic/performance/baselineprofiles/create-baselineprofile
url: https://developer.android.com/topic/performance/baselineprofiles/create-baselineprofile
source: md.txt
---

Automatically generate profiles for every app release using the [Jetpack
Macrobenchmark library](https://developer.android.com/macrobenchmark) and
[`BaselineProfileRule`](https://developer.android.com/reference/kotlin/androidx/benchmark/macro/junit4/BaselineProfileRule). We recommend that you
use `com.android.tools.build:gradle:8.0.0` or higher, which comes with build
improvements when using Baseline Profiles.
| **Important:** To keep installation turnaround during development low, Baseline Profiles are only installed for release builds.

These are the general steps to create a new Baseline Profile:

1. Set up the Baseline Profile module.
2. Define the JUnit test that helps generate Baseline Profiles.
3. Add the Critical User Journeys (CUJs) that you want to optimize.
4. Generate the Baseline Profile.

After you generate the Baseline Profile, benchmark it using a physical device to
measure the speed improvements.

## Create a new Baseline Profile with AGP 8.2 or higher

The easiest way to create a new Baseline Profile is to use the Baseline Profile
module template, available starting Android Studio Iguana and Android Gradle
Plugin (AGP) 8.2.

The Android Studio Baseline Profile Generator module template automates the
creation of a new module to generate and
[benchmark](https://developer.android.com/topic/performance/baselineprofiles/measure-baselineprofile)
Baseline Profiles. Running the template generates most of the typical build
configuration, Baseline Profile generation, and verification code. The template
creates code to generate and benchmark Baseline Profiles to measure app
startup.

### Set up the Baseline Profile module

To run the Baseline Profile module template, follow these steps:

1. Select **File \> New \> New Module**
2. Select the **Baseline Profile Generator** template in the **Templates** panel and configure it: ![](https://developer.android.com/static/topic/performance/images/studio/baseline-profile-generator-module-template.png) **Figure 1.** Baseline Profile Generator module template.

   The fields in the template are the following:
   - **Target application**: defines which app the Baseline Profile is generated for. When you have only a single app module in your project, there is only one item in this list.
   - **Module name**: the name you want for the Baseline Profile module being created.
   - **Package name**: the package name you want for the Baseline Profile module.
   - **Language**: whether you want the generated code to be Kotlin or Java.
   - **Build configuration language**: whether you want to use Kotlin Script (KTS) or Groovy for your build configuration scripts.
   - **Use Gradle-managed device** : if you're using [Gradle-managed devices](https://developer.android.com/studio/test/gradle-managed-devices) to test your app.
3. Click **Finish** and the new module is created. If you are using source control, you might be prompted to add the newly created module files to source control.

### Define the Baseline Profile generator

The newly created module contains tests to both generate and benchmark the
Baseline Profile and test only basic app startup. We recommend that you augment
these to include CUJs and advanced startup workflows. Make sure that any tests
related to app startup are in a `rule` block with `includeInStartupProfile` set
to `true`; conversely, for optimal performance make sure that any tests not
related to app startup are not included in a Startup Profile. App startup
optimizations are used to define a special part of a Baseline Profile called a
[Startup Profile](https://developer.android.com/topic/performance/baselineprofiles/dex-layout-optimizations).

It helps maintainability if you abstract these CUJs outside of the generated
Baseline Profile and benchmark code so that they can be used for both. This
means that changes to your CUJs are used consistently.

### Generate and install the Baseline Profile

The Baseline Profile module template adds a new run configuration to generate
the Baseline Profile. If you use product flavors, Android Studio creates
multiple run configurations so that you can generate separate Baseline Profiles
for each flavor.
| **Note:** To generate and install the Baseline Profile from the command-line interface, run the `:app:generateBaselineProfile` or `:app:generateVariantBaselineProfile` Gradle tasks.
![The Generate Baseline Profile run configuration.](https://developer.android.com/static/topic/performance/images/studio/generate-baseline-profile.png) **Figure 2.** Running this configuration generates the Baseline Profile.

When the **Generate Baseline Profile** run configuration completes, it copies
the generated Baseline Profile to the
`src/variant/generated/baselineProfiles/baseline-prof.txt`
file in the module that is being profiled. The variant options are either the
release build type or a build variant involving the release build type.

The generated Baseline Profile is originally created in `build/outputs`. The
full path is dictated by the variant or flavor of the app being profiled and
whether you use a Gradle-managed device or a connected device for profiling. If
you use the names used by the code and build configurations generated by the
template, the Baseline Profile is created in the
`build/outputs/managed_device_android_test_additional_output/nonminifiedrelease/pixel6Api31/BaselineProfileGenerator_generate-baseline-prof.txt` file. You probably won't
have to interact with this version of the generated Baseline Profile directly
unless you're manually copying it to the target modules (not recommended).

## Create a new Baseline Profile with AGP 8.1

If you aren't able to use the
[Baseline Profile module template](https://developer.android.com/topic/performance/baselineprofiles/create-baselineprofile#create-new-profile), use the
Macrobenchmark module template and the Baseline Profile Gradle plugin to create
a new Baseline Profile. We recommend you use these tools starting with Android
Studio Giraffe and AGP 8.1.
| **Note:** Automatic Baseline Profile generation with the Baseline Profile Gradle plugin is available starting with AGP 8.0, but we recommend using AGP 8.1 for a better experience.

Here are the steps to create a new Baseline Profile using the Macrobenchmark
module template and Baseline Profile Gradle plugin:

1. [Set
   up a Macrobenchmark module](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview#project-setup) in your Gradle project.
2. Define a new class called `BaselineProfileGenerator`:

   ```kotlin
   class BaselineProfileGenerator {
       @get:Rule
       val baselineProfileRule = BaselineProfileRule()

       @Test
       fun startup() = baselineProfileRule.collect(
           packageName = "com.example.app",
           profileBlock = {
               startActivityAndWait()
           }
       )
   }
   ```

   The generator can contain interactions with your app beyond app startup.
   This lets you optimize the runtime performance of your app, such as
   scrolling lists, running animations, and navigating within an
   `Activity`.
   [See
   other examples](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:benchmark/integration-tests/macrobenchmark/src/main/java/androidx/benchmark/integration/macrobenchmark/GithubBrowserBaselineProfile.kt) of tests that use `@BaselineProfileRule` to
   improve critical user journeys.
3. Add the Baseline Profile Gradle plugin
   (`libs.plugins.androidx.baselineprofile`). The plugin makes it easier
   to generate Baseline Profiles and maintain them in the future.

4. To generate the Baseline Profile, run the
   `:app:generateBaselineProfile` or
   `:app:generateVariantBaselineProfile` Gradle tasks in the
   terminal.

   Run the generator as an instrumented test
   on a rooted physical device, emulator, or
   [Gradle Managed Device](https://developer.android.com/studio/test/gradle-managed-devices).
   If you use a Gradle Managed Device, set `aosp` as the `systemImageSource`, because you need root
   access for the Baseline Profile generator.
   | **Note:** When using Jetpack Macrobenchmark 1.2.0-alpha06 and higher, you can generate the Baseline Profile on devices running Android 13 (API 33) and higher without root access.

   At the end of the generation task, the Baseline Profile is copied to
   `app/src/variant/generated/baselineProfiles`.

### Create a new Baseline Profile without templates

We recommend creating a Baseline Profile using the Android Studio
[Baseline Profile module template](https://developer.android.com/topic/performance/baselineprofiles/create-baselineprofile#create-new-profile)
(preferred) or [Macrobenchmark template](https://developer.android.com/topic/performance/baselineprofiles/create-baselineprofile#create-new-profile-8-1), but you can
also use the Baseline Profile Gradle plugin by itself. To read more about the
Baseline Profile Gradle plugin, see
[Configure your Baseline Profile generation](https://developer.android.com/topic/performance/baselineprofiles/use-baselineprofile-gradle-plugin).
| **Note:** The Baseline Profile Gradle plugin is already applied if you use the [Baseline Profile module template](https://developer.android.com/topic/performance/create-baselineprofile#create-new-profile).

Here's how to create a Baseline Profile using the Baseline Profile Gradle plugin
directly:

1. Create a new `com.android.test` module---for example, `:baseline-profile`.
2. Configure the `build.gradle.kts` file for
   `:baseline-profile`:

   1. Apply the `androidx.baselineprofile` plugin.
   2. Ensure the `targetProjectPath` points to the `:app` module.
   3. Optionally, add a [Gradle-managed device (GMD)](https://developer.android.com/studio/test/gradle-managed-devices). In the following example, it's `pixel6Api31`. If not specified, the plugin uses a connected device, either emulated or physical.
   4. Apply the configuration you want, as shown in the following example.

   ### Kotlin

   ```kotlin
   plugins {
       id("com.android.test")
       id("androidx.baselineprofile")
   }

   android {
       defaultConfig {
           ...
       }

       // Point to the app module, the module that you're generating the Baseline Profile for.
       targetProjectPath = ":app"
       // Configure a GMD (optional).
       testOptions.managedDevices.devices {
           pixel6Api31(com.android.build.api.dsl.ManagedVirtualDevice) {
               device = "Pixel 6"
               apiLevel = 31
               systemImageSource = "aosp"
           }
       }
   }

   dependencies { ... }

   // Baseline Profile Gradle plugin configuration. Everything is optional. This
   // example uses the GMD added earlier and disables connected devices.
   baselineProfile {
       // Specifies the GMDs to run the tests on. The default is none.
       managedDevices += "pixel6Api31"
       // Enables using connected devices to generate profiles. The default is
       // `true`. When using connected devices, they must be rooted or API 33 and
       // higher.
       useConnectedDevices = false
   }
   ```

   ### Groovy

   ```groovy
   plugins {
       id 'com.android.test'
       id 'androidx.baselineprofile'
   }

   android {
       defaultConfig {
           ...
       }

       // Point to the app module, the module that you're generating the Baseline Profile for.
       targetProjectPath ':app'
       // Configure a GMD (optional).
       testOptions.managedDevices.devices {
           pixel6Api31(com.android.build.api.dsl.ManagedVirtualDevice) {
               device 'Pixel 6'
               apiLevel 31
               systemImageSource 'aosp'
           }
       }
   }

   dependencies { ... }

   // Baseline Profile Gradle plugin configuration. Everything is optional. This
   // example uses the GMD added earlier and disables connected devices.
   baselineProfile {
       // Specifies the GMDs to run the tests on. The default is none.
       managedDevices ['pixel6Api31']
       // Enables using connected devices to generate profiles. The default is
       // `true`. When using connected devices, they must be rooted or API 33 and
       // higher.
       useConnectedDevices false
   }
   ```
3. Create a Baseline Profile test in the `:baseline-profile` test module. The
   following example is a test that generates a Baseline Profile for app
   startup.

   ### Kotlin

   ```kotlin
   class BaselineProfileGenerator {
   @get:Rule
   val baselineProfileRule = BaselineProfileRule()

   @Test
   fun startup() = baselineProfileRule.collect(
       packageName = "com.example.app",
       profileBlock = {
           uiAutomator { startApp(PACKAGE_NAME) }
       }
   )
   }
   ```

   ### Java

   ```java
   public class BaselineProfileGenerator {

       @Rule
       Public BaselineProfileRule baselineRule = new BaselineProfileRule();

       @Test
       Public void startupBaselineProfile() {
           baselineRule.collect(
               "com.myapp",
               (scope -> {
                   scope.startActivityAndWait();
                   Return Unit.INSTANCE;
               })
           )
       }
   }
   ```
4. Update the `build.gradle.kts` file in the app module, for example `:app`.

   1. Apply the plugin `androidx.baselineprofile`.
   2. Add a `baselineProfile` dependency to the `:baseline-profile` module.

   ### Kotlin

   ```kotlin
   plugins {
       id("com.android.application")
       id("androidx.baselineprofile")
   }

   android {
       // There are no changes to the `android` block.
       ...
   }

   dependencies {
       ...
       // Add a `baselineProfile` dependency on the `:baseline-profile` module.
       baselineProfile(project(":baseline-profile"))
   }
   ```

   ### Groovy

   ```groovy
   plugins {
       id 'com.android.application'
       id 'androidx.baselineprofile'
   }

   android {
       // No changes to the `android` block.
       ...
   }

   dependencies {
       ...
       // Add a `baselineProfile` dependency on the `:baseline-profile` module.
       baselineProfile ':baseline-profile'
   }
   ```
5. Generate the profile by running the `:app:generateBaselineProfile`
   or `:app:generateVariantBaselineProfile` Gradle tasks.

6. At the end of the generation task, the Baseline Profile is copied to
   `app/src/variant/generated/baselineProfiles`.

## Create a new Baseline Profile with AGP 7.3-7.4

It's possible to generate Baseline Profiles with AGP 7.3-7.4, but we strongly
recommend upgrading to at least AGP 8.1 so you can use the Baseline Profile
Gradle plugin and its latest features.

If you need to create Baseline Profiles with AGP 7.3-7.4, the steps are the same
as the [steps for AGP 8.1](https://developer.android.com/topic/performance/baselineprofiles/create-baselineprofile#create-new-profile-8-1), with the following
exceptions:

- Don't add the Baseline Profile Gradle plugin.
- To generate the Baseline Profiles, execute the Gradle task `./gradlew [emulator name][flavor][build type]AndroidTest`. For example, `./gradlew :benchmark:pixel6Api31BenchmarkAndroidTest`.
- You must [manually apply the generated Baseline Profile rules to your code](https://developer.android.com/topic/performance/baselineprofiles/create-baselineprofile#apply-rules).

### Manually apply generated rules

The Baseline Profile generator creates a Human Readable Format (HRF) text file
on the device and copies it to your host machine. To apply the generated profile
to your code, follow these steps:

1. Locate the HRF file in the build folder of the module you generate the
   profile in:
   `[module]/build/outputs/managed_device_android_test_additional_output/[device]`.

   Profiles follow the `[class name]-[test method name]-baseline-prof.txt`
   naming pattern, which looks like this:
   `BaselineProfileGenerator-startup-baseline-prof.txt`.
2. Copy the generated profile to `src/main/` and rename the file to
   `baseline-prof.txt`.

   | **Note:** If you're using a version of the Android Gradle plugin earlier than 8.0, the `baseline-prof.txt` file isn't shown in the **Android** view in Android Studio.
3. Add a dependency to the [ProfileInstaller library](https://developer.android.com/jetpack/androidx/releases/profileinstaller)
   in your app's `build.gradle.kts` file to enable local Baseline Profile
   compilation where [Cloud Profiles](https://developer.android.com/topic/performance/baselineprofiles/overview#cloud-profiles) aren't available. This is
   the only way to sideload a Baseline Profile locally.

       dependencies {
            implementation("androidx.profileinstaller:profileinstaller:1.4.1")
       }

4. Build the production version of your app while the applied HRF rules are
   compiled into binary form and included in the APK or AAB. Then distribute
   your app as usual.

## Benchmark the Baseline Profile

To benchmark your Baseline Profile, create a new Android Instrumented Test Run
configuration from the gutter action that executes the benchmarks defined in
the `StartupBenchmarks.kt` or `StartupBencharks.java` file. To learn more about benchmark
testing, see [Create a Macrobenchmark
class](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview#create-macrobenchmark)
and [Automate measurement with the Macrobenchmark
library](https://developer.android.com/topic/performance/baselineprofiles/measure-baselineprofile).
![](https://developer.android.com/static/topic/performance/images/studio/gutter-action.png) **Figure 3.** Run Android Tests from the gutter action.

When you run this within Android Studio, the build output contains details of
the speed improvements that the Baseline Profile provides:

```scdoc
StartupBenchmarks_startupCompilationBaselineProfiles
timeToInitialDisplayMs   min 161.8,   median 178.9,   max 194.6
StartupBenchmarks_startupCompilationNone
timeToInitialDisplayMs   min 184.7,   median 196.9,   max 202.9
```

## Capture all required code paths

The two key metrics for measuring app startup times are as follows:

[Time to initial display (TTID)](https://developer.android.com/topic/performance/vitals/launch-time#time-initial)
:   The time it takes to display the first frame of the application UI.

[Time to full display (TTFD)](https://developer.android.com/topic/performance/vitals/launch-time#time-full)
:   TTID plus the time to display content that is loaded asynchronously after the initial frame is displayed.

TTFD is reported once the
[`reportFullyDrawn()`](https://developer.android.com/reference/androidx/activity/ComponentActivity#reportFullyDrawn())
method of the
[`ComponentActivity`](https://developer.android.com/reference/androidx/activity/ComponentActivity)
is called. If `reportFullyDrawn()` is never called, the TTID is reported
instead. You might need to delay when `reportFullyDrawn()` is called until after
the asynchronous loading is complete. For example, if the UI contains a dynamic
list such as a [`RecyclerView`](https://developer.android.com/develop/ui/views/layout/recyclerview) or [lazy
list](https://developer.android.com/jetpack/compose/lists#lazy), the list might be populated by a background
task that completes after the list is first drawn and, therefore, after the UI
is marked as fully drawn. In such cases, code that runs after the UI reaches
fully drawn state isn't included in the Baseline Profile.

To include the list population as part of your Baseline Profile, get the
`FullyDrawnReporter` by using
[`getFullyDrawnReporter()`](https://developer.android.com/reference/androidx/activity/ComponentActivity#getFullyDrawnReporter())
and add a reporter to it in your app code. Release the reporter once the
background task finishes populating the list. The `FullyDrawnReporter` doesn't
call the `reportFullyDrawn()` method until all reporters are released. By doing
this, Baseline Profile includes the code paths required to populate the list.
This doesn't change the app's behavior for the user, but it lets the Baseline
Profile include all the necessary code paths.

If your app uses [Jetpack Compose](https://developer.android.com/jetpack/compose), use the following APIs to
indicate fully drawn state:

- [`ReportDrawn`](https://developer.android.com/reference/kotlin/androidx/activity/compose/package-summary#ReportDrawn()) indicates that your composable is immediately ready for interaction.
- [`ReportDrawnWhen`](https://developer.android.com/reference/kotlin/androidx/activity/compose/package-summary#ReportDrawnWhen(kotlin.Function0)) takes a predicate, such as `list.count > 0`, to indicate when your composable is ready for interaction.
- [`ReportDrawnAfter`](https://developer.android.com/reference/kotlin/androidx/activity/compose/package-summary#ReportDrawnAfter(kotlin.coroutines.SuspendFunction0)) takes a suspending method that, when it completes, indicates that your composable is ready for interaction.

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Capture Macrobenchmark metrics](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-metrics)
- [Write a Macrobenchmark](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview)
- [JankStats library](https://developer.android.com/topic/performance/jankstats)