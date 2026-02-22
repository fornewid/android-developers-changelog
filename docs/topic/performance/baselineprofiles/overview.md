---
title: https://developer.android.com/topic/performance/baselineprofiles/overview
url: https://developer.android.com/topic/performance/baselineprofiles/overview
source: md.txt
---

[Video](https://www.youtube.com/watch?v=WWdDzXgrkmg)

Baseline Profiles improve code execution speed by about 30% from the first
launch by avoiding interpretation and [just-in-time (JIT)](https://developer.android.com/about/versions/nougat/android-7.0#jit_aot) compilation steps
for included code paths.

By shipping a Baseline Profile in an app or library, [Android Runtime (ART)](https://source.android.com/docs/core/runtime)
can optimize specified code paths through Ahead-of-Time (AOT) compilation,
providing performance enhancements for every new user and every app update. This
Profile Guided Optimization (PGO) lets apps optimize startup, reduce interaction
jank, and improve overall runtime performance for users from the first launch.

These performance enhancements directly result in improved business metrics such
as user retention, transactions, and ratings. You can read more about how
performance impacts business metrics in stories from [Josh](https://developer.android.com/stories/apps/josh), [Lyft](https://developer.android.com/stories/apps/lyft),
[TikTok](https://developer.android.com/stories/apps/tiktok), and [Zomato](https://developer.android.com/stories/apps/zomato).

## Benefits of Baseline Profiles

Baseline Profiles enable pre-compilation of code in critical user interactions,
such as app startup, navigating between screens, or scrolling through content,
making them smoother from the first time they run. By increasing the speed and
responsiveness of an app, Baseline Profiles can lead to more daily active users
and a higher average return visit rate.

Baseline Profiles help guide optimization beyond app startup by providing common
user interactions that improve app runtime from the first launch. Guided AOT
compilation doesn't rely on user devices and can be done once per release on a
development machine instead of a mobile device. By shipping releases with a
Baseline Profile, app optimizations become available much faster than by relying
on [Cloud Profiles](https://developer.android.com/topic/performance/baselineprofiles/overview#cloud-profiles) alone.

When not using a Baseline Profile, all app code is either JIT-compiled in memory
after being interpreted, or written to an `odex` file in the background when the
device is idle. After installing or updating an app, users have a suboptimal
experience from the first time they run it until new code paths are optimized.
Many apps measure performance boosts of about 30% after optimizing.

### Startup profiles

Startup profiles are similar to Baseline Profiles, but they are used at compile
time to optimize DEX layout for faster startup times, rather than for on-device
optimization. To learn more about how startup profiles differ from Baseline
Profiles, see [Compare Baseline Profiles and Startup Profiles](https://developer.android.com/topic/performance/baselineprofiles/overview#compare-baseline-startup).
For more on DEX layout optimization, see [DEX layout optimizations and startup
profiles](https://developer.android.com/topic/performance/baselineprofiles/dex-layout-optimizations).
| **Note:** We recommend using both Baseline Profiles and startup profiles to fully optimize app startup.

## Get started

To start optimizing performance in your existing app, see [Create Baseline
Profiles](https://developer.android.com/about/versions/nougat/android-7.0#jit_aot).

### Profile generation versus release builds

It is important to understand the difference in build configurations required
when *generating* Baseline and startup profile files (for example,
`baseline-prof.txt` and `startup-prof.txt`) versus when building your final
release APK that consumes these profiles.

**When generating profile files (for example, `benchmark`):**

To make sure the generated profile rules accurately match your code's method
signatures, you must turn off obfuscation and optimization (R8) for the build
variant used for profile generation. This variant must be different from your
release build variant, which has obfuscation and optimization enabled. You
achieve this by setting `isMinifyEnabled = false` for the profile generation
build variant. If you aren't using the Baseline Profile Gradle plugin, you
should also make sure that `-dontobfuscate` and `-dontoptimize` are applied. The
[Baseline Profile Gradle
Plugin](https://developer.android.com/topic/performance/baselineprofiles/create-baselineprofile)
automatically handles this configuration for you.

**When building your final release APK:**

Your release build should always have `isMinifyEnabled = true` to benefit from
obfuscation, minification, and optimization. R8 automatically rewrites the rules
from your unobfuscated profile files to match the obfuscated and optimized code
in your release APK. For [DEX layout
optimization](https://developer.android.com/topic/performance/baselineprofiles/dex-layout-optimizations)
(driven by Startup Profiles) to be effective, your release app must be
obfuscated and use R8 with all optimizations enabled.

### Minimum recommended stable versions

The dependency chain provides stable and developmental release versions. To
generate and install a Baseline Profile, use the following supported versions or
higher of Android Gradle plugin, Macrobenchmark library, and Profile Installer.
These dependencies are required at different times and work together as a
toolchain to enable an optimal Baseline Profile.

- Android Gradle plugin: `com.android.tools.build:8.0.0`
- Macrobenchmark library: `androidx.benchmark:benchmark-macro-junit4:1.4.1`
- Profile Installer: `androidx.profileinstaller:profileinstaller:1.4.1`

We recommend using the latest version of AGP to create and manage Baseline
Profiles. Here are the major functionalities that come with different versions
of AGP:

| AGP version | Features |
|---|---|
| 9.1 | **Full source set directory support (library modules):** In addition to variant-aware directories, you can declare multiple Baseline Profile source files with an arbitrary name, such as `src/free/generated/baselineProfiles/baseline-prof1.txt`, for library modules as well as app modules. |
| 8.4 | Local app installations of non-debuggable builds using the [Gradle wrapper command line tool](https://developer.android.com/build/building-cmdline) or Android Studio install Baseline Profiles, so the performance of your local release build more closely matches production. This update doesn't affect production performance of Baseline Profiles. |
| 8.3 | - **Partial source set directory support (library modules):** Declare variant-aware Baseline Profile files, such as `src/free/generated/baselineProfiles/baseline-prof.txt`, for library modules. - Baseline Profiles include [desugared classes](https://developer.android.com/studio/write/java8-support#library-desugaring). |
| 8.2 | - **R8 rewriting of rules:** D8 and R8 can transform the human-readable Baseline and Startup Profile rules to fully capture all the rules you need to optimize app performance. This lets you generate profiles from an unminified build and apply them to a minified release build. Increases Baseline Profile coverage of methods by \~30% and increases app performance by \~15%. - [**Startup Profiles:**](https://developer.android.com/topic/performance/baselineprofiles/dex-layout-optimizations) generate this type of Baseline Profile to inform layout of code within DEX. Increases startup performance by an additional \~15%, or significantly more for large apps. |
| 8.0 | **Minimum recommended version:** use the Baseline Profile Gradle plugin to generate Baseline Profiles with a single Gradle task. - **Full source set directory support (app modules):** declare multiple Baseline Profile source files, and use variant-aware directories, such as `src/free/generated/baselineProfiles/baseline-prof1.txt`. |
| 7.4 | **Minimum supported version:** apps can consume Baseline Profiles from libraries, and provide their own Baseline Profile in the `src/main/baseline-prof.txt` file. - Baseline Profiles are correctly packaged when building the APK from an app bundle ([issue #230361284](https://issuetracker.google.com/issues/230361284)). - For apps with more than one `.dex` file, Baseline Profiles are correctly packaged for the primary `.dex` file. - D8 and R8 support generating startup profiles from a build where `isMinifyEnabled` is set to `false`. |

### Variant-aware profile source settings

By using Android Gradle Plugin (AGP) version 8.0 for applications and AGP
version 8.3 for libraries, you can place Baseline Profile rules in a dedicated
source set directory, moving beyond the constraints of a single, fixed path (for
example, `src/main/baseline-prof.txt`) and enabling multiple files.

This facilitates robust variant support, enabling you to define distinct
Baseline Profiles tailored to specific build flavors and types (for example,
using directories like `src/variant/baselineProfiles/`), which makes sure
performance optimization rules are precisely applied for each unique application
or library binary.

### Profile generation example

The following is an example class to create a Baseline Profile for app startup,
as well as several navigation and scroll events using the recommended
[Macrobenchmark](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview)
library:

    class BaselineProfileGenerator {
        @get:Rule
        val baselineProfileRule = BaselineProfileRule()

        @Test
        fun appStartupAndUserJourneys() {
            baselineProfileRule.collect(packageName = PACKAGE_NAME) {
                uiAutomator {
                    // App startup journey.
                    startApp(PACKAGE_NAME)

                    // Find and click elements using the new DSL
                    onElement { textAsString() == "COMPOSE LAZYLIST" }.click()
                    onElement { viewIdResourceName == "myLazyColumn" }.also {
                        it.fling(Direction.DOWN)
                        it.fling(Direction.UP)
                    }
                    pressBack()
                }
            }
        }
    }

For more information about using the UI Automator library to automate user
journeys, see [Write automated tests with UI Automator](https://developer.android.com/about/versions/nougat/android-7.0#jit_aot).

You can see this code in full context and more detail as part of our
[performance samples on GitHub](https://github.com/android/performance-samples).
| **Note:** To learn how to use `testTag()` for accessing UI elements in Jetpack Compose, see [Interoperability with UiAutomator](https://developer.android.com/jetpack/compose/testing#uiautomator-interop).

### What to include

When using Baseline Profiles in an app, you can include app startup code and
common user interactions like navigation between screens or scrolling. You can
also gather entire flows such as registration, login, or payment. Any user
journeys that you deem critical can benefit from Baseline Profiles by improving
their runtime performance.

If you are experimenting with different approaches to improve performance,
consider including Baseline Profiles for both arms of your experiment. By doing
this, you can make your results easier to interpret by ensuring all of your
users are consistently running compiled code.

Libraries can provide their own Baseline Profiles and ship them with releases to
improve app performance. For example, see the [Use a Baseline Profile section in
Jetpack Compose performance](https://developer.android.com/jetpack/compose/performance#use-baseline).

## How Baseline Profiles work

While developing your app or library, consider defining Baseline Profiles to
cover common user interactions where rendering time or latency are important.
Here's how they work:

1. Human-readable profile rules are generated for your app and compiled into
   binary form in the app. You can find them in `assets/dexopt/baseline.prof`.
   You can then upload the Android App Bundle (AAB) to Google Play as usual.

2. Google Play processes the profile and ships it directly to users along with
   the APK. During installation, ART performs AOT compilation of the methods in
   the profile, resulting in those methods executing faster. If the profile
   contains methods used in app launch or during frame rendering, the user
   might experience faster launch times and reduced jank.

3. This flow cooperates with Cloud Profiles aggregation to fine-tune
   performance based on actual usage of the app over time.

![](https://developer.android.com/static/topic/performance/images/benchmark_images/baselineprofile_workflow.png) **Figure 1.** This diagram demonstrates the Baseline Profile workflow from upload through end-user delivery, and how that workflow relates to Cloud Profiles.

## Compare Baseline Profiles and Startup Profiles

You use the Baseline Profile Gradle Plugin to define and produce profile files.
This plugin hooks into the build process, and AGP compiles these human-readable
profile rules into a binary format---packaged as `baseline.prof` within the APK
or AAB---that ART can use effectively for on-device compilation, provided it is
smaller than 1.5 MB.

These profile files produced are typically named `startup-prof.txt` and
`baseline-prof.txt`. While their contents might sometimes appear similar,
especially if you're primarily focused on startup, they serve distinct purposes
and influence performance at different stages:

### Baseline Profile

The Baseline Profile file contains a comprehensive set of rules that the
Android Runtime (ART) uses to pre-compile frequently used code paths, which
optimizes app performance beyond just startup.

The Baseline Profile file is generally a superset of the rules found in your
Startup Profile. This file includes all rules required for app startup
optimization (generated through the `baselineProfile` Gradle task), along with
additional profiles for other critical user journeys. For example, scrolling,
and navigating different screens.

These additional, non-startup rules are generated regardless of the value of the
`includeInStartupProfile` configuration field.

### Startup Profile

The Startup Profile file contains rules specifically optimized for your app's
startup path. During compilation, D8 converts the Java bytecode into DEX format.
R8 then uses this file to influence the layout of your DEX files, making sure
that critical startup code is placed in the primary DEX file for faster
execution. You should generally set `includeInStartupProfile` to `true` only for
test scenarios essential to the app's initial display. For more information, see
[Create Startup Profiles](https://developer.android.com/topic/performance/baselineprofiles/dex-layout-optimizations).

## Cloud Profiles

Cloud Profiles offer an additional form of PGO---aggregated by Google Play
Store and distributed for install time compilation---together with Baseline
Profiles.

While Cloud Profiles are driven by real-world user interactions with the app,
they take several hours to days after an update to be distributed, limiting
their availability. Until profiles are fully distributed, app
performance is suboptimal for users of new or updated apps. Further, Cloud
Profiles only support Android devices running Android 9 (API level 28) or
higher, and only scale well for apps that have a sufficiently large user base.

## Compilation behavior across Android versions

Android Platform versions use different app compilation approaches, each with a
corresponding performance tradeoff. Baseline Profiles improve upon the previous
compilation methods by providing a profile for all installs.

| Android version | Compilation method | Optimization approach |
|---|---|---|
| 5 up to 6 (API level 21 up to 23) | Full AOT | The entire app is optimized during install, resulting in long wait times to use the app, increased RAM and disk space usage, and longer times to load code from disk, potentially increasing cold startup times. |
| 7 up to 8.1 (API level 24 up to 27) | Partial AOT (Baseline Profile) | Baseline Profiles are installed by `androidx.profileinstaller` on the first run when the app module defines this dependency. ART can improve this further by adding additional profile rules during the app's use, and compiling them when the device is idle. This optimizes for disk space and time to load code from the disk, thereby reducing wait time for the app. |
| 9 (API level 28) and higher | Partial AOT (Baseline + Cloud Profile) | Play uses Baseline Profiles during app installs to optimize the APK and Cloud profiles---if available. After installation, ART profiles are uploaded to Play, aggregated, and then provided as Cloud Profiles to other users when they install or update the app. |

## Known issues

The following are possible issues and solutions, or issues for which there are
ongoing developments for workarounds:

- Baseline Profile generation might fail due to permission settings on some
  devices, including OnePlus devices. To work around this, turn off the
  **Disable permission monitoring** option in the **Developer Options**
  settings.

- Baseline Profile generation isn't supported on Firebase Test Lab devices,
  including Gradle-managed Test Lab devices
  ([issue #285187547](https://issuetracker.google.com/issues/285187547)).

- To provide Baseline Profiles for libraries successfully, use
  Baseline Profile Gradle plugin 1.2.3 or AGP 8.3, at minimum
  ([issue #313992099](https://issuetracker.google.com/313992099)).

- If you generate Baseline Profiles with the command
  `./gradlew app:generateBaselineProfile`, the benchmarks in the test module
  also run, and the results are discarded. If this happens, you can generate
  only the Baseline Profiles by running the command with
  `-P android.testInstrumentationRunnerArguments.androidx.benchmark.enabledRules=BaselineProfile`.
  This issue has been fixed in AGP 8.2.

- The command to generate Baseline Profiles for all build types---
  `./gradlew app:generateBaselineProfile`---only generates Baseline Profiles for
  the release build type. This issue has been fixed in AGP 8.1.

- Non-Google-Play-Store app distribution channels might not support using
  Baseline Profiles at installation. Users of apps installed through these
  channels don't see the benefits until background dexopt runs---which is
  likely overnight.

- [Play Store internal app sharing](https://play.google.com/console/about/internalappsharing/)
  doesn't support Baseline Profiles; however, the
  [internal testing track](https://play.google.com/console/about/internal-testing/)
  does.

- Battery optimizations on some devices, such as Huawei devices, can interfere
  with profile installation. To help ensure that your profiles are installed
  effectively, disable any battery optimizations in your benchmark devices.

## Additional resources

- [DEX layout optimizations and startup profiles](https://developer.android.com/topic/performance/baselineprofiles/dex-layout-optimizations)
- [Improve app performance with Baseline Profiles](https://codelabs.developers.google.com/android-baseline-profiles-improve)

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Create Baseline Profiles {:#creating-profile-rules}](https://developer.android.com/topic/performance/baselineprofiles/create-baselineprofile)
- [Create and measure Baseline Profiles without Macrobenchmark](https://developer.android.com/topic/performance/baselineprofiles/manually-create-measure)
- [DEX layout optimizations and startup profiles](https://developer.android.com/topic/performance/baselineprofiles/dex-layout-optimizations)