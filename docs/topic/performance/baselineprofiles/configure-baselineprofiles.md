---
title: https://developer.android.com/topic/performance/baselineprofiles/configure-baselineprofiles
url: https://developer.android.com/topic/performance/baselineprofiles/configure-baselineprofiles
source: md.txt
---

The Baseline Profile Gradle plugin makes it easier to generate and maintain
[Baseline Profiles](https://developer.android.com/topic/performance/baselineprofiles/overview). It helps you
do the following tasks:

- [Create new Baseline Profiles for your app](https://developer.android.com/topic/performance/baselineprofiles/create-baselineprofile#create-baselineprofile-plugin).
- [Create new Baseline Profiles for your library](https://developer.android.com/topic/performance/baselineprofiles/create-baselineprofile-library).
- Customize your Baseline Profile generation.

This page explains how to use the Baseline Profile Gradle plugin to customize
the generation of your Baseline Profiles.

## Plugin requirements

- AGP 8.0 or higher
- Dependency on the [latest Gradle plugin version](https://maven.google.com/web/index.html?q=benchmark#androidx.benchmark:benchmark-baseline-profile-gradle-plugin)

## Use a Gradle Managed Devices to generate Baseline Profiles

To use a [Gradle Managed Device (GMD)](https://developer.android.com/studio/test/gradle-managed-devices) to
generate your Baseline Profile, add one in the `build.gradle.kts` configuration
of the profile producer module---likely the `:baselineprofile` test module---as
shown in the following example:

### Kotlin

```kotlin
android {
   testOptions.managedDevices.devices {
       create<com.android.build.api.dsl.ManagedVirtualDevice>("pixel6Api31") {
           device = "Pixel 6"
           apiLevel = 31
           systemImageSource = "aosp"
       }
   }
}
```

### Groovy

```groovy
android {
   testOptions.managedDevices.devices {
       pixel6Api31(ManagedVirtualDevice) {
           device 'Pixel 6'
           apiLevel = 31
           systemImageSource 'aosp'
       }
   }
}
```

Use the GMD to generate Baseline Profiles by adding it to the Baseline Profile
Gradle plugin configuration as follows, in the `build.gradle.kts` of the
`:baselineprofile` test module:

### Kotlin

```kotlin
baselineProfile {
    managedDevices += "pixel6Api31"
}
```

### Groovy

```groovy
baselineProfile {
    managedDevices = ['pixel6Api31']
}
```

When you use a GMD to generate Baseline Profiles, set `useConnectedDevices` to
`false`, in your `:baselineprofile` test module:

### Kotlin

```kotlin
baselineProfile {
    ...
    useConnectedDevices = false
}
```

### Groovy

```groovy
baselineProfile {
    ...
    useConnectedDevices false
}
```

## Generate Baseline Profiles for different variants

You can generate Baseline Profiles per variant, per flavor, or as a single file
to utilize for all variants. Control this behavior through the merge setting, as
shown in the following example, in the `build.gradle.kts` of the
application or library module.

### Kotlin

```kotlin
baselineProfile {
    mergeIntoMain = true
}
```

### Groovy

```groovy
baselineProfile {
    mergeIntoMain true
}
```

To merge the generated profiles for all variants into a single profile, set
`mergeIntoMain` to `true`. It isn't possible to generate per-variant Baseline
Profiles when this setting is `true`, so there's a single Gradle task called
`generateBaselineProfile`. The profile is output at
`src/main/generated/baselineProfiles`.

To disable merging and have one profile per variant, set `mergeIntoMain` to
`false`. In this case, multiple variant-specific Gradle tasks exist. For
example, when there are two flavors---such as free and paid---and one
release build type, the tasks are the following:

    * `generateFreeReleaseBaselineProfile`
    * `generatePaidReleaseBaselineProfile`
    * `generateReleaseBaselineProfile`

To specify the merging behavior per variant, use the following code:

### Kotlin

```kotlin
baselineProfile {
    variants {
        freeRelease {
            mergeIntoMain = true
        }
    }
}
```

### Groovy

```groovy
baselineProfile {
    variants {
        freeRelease {
            mergeIntoMain true
        }
    }
}
```

In the preceding example, the variants where the flag is set to `true` are all
merged into `src/main/generated/baselineProfiles`, while the profiles for the
variants where the flag is set to `false` are kept in the folder
`src/<variant>/generated/baselineProfiles`.

By default, `mergeIntoMain` is set to `true` for libraries and `false` for apps.

## Automatically generate Baseline Profiles when assembling a new release

You can configure Baseline Profiles to automatically generate with every release
build, instead of manually using the task `generateBaselineProfile`. With
automatic generation, the most updated profile is included in the release build.

To enable automatic generation for release builds, use the
`automaticGenerationDuringBuild` flag:

### Kotlin

```kotlin
baselineProfile {
    automaticGenerationDuringBuild = true
}
```

### Groovy

```groovy
baselineProfile {
    automaticGenerationDuringBuild true
}
```

Setting the `automaticGenerationDuringBuild` flag to `true` triggers the
generation of a new Baseline Profile for each release assembly. This means that
running an assemble release build task, such as `./gradlew:app:assembleRelease`,
also triggers `:app:generateReleaseBaselineProfile`, starts the Baseline Profile
instrumentation tests, and builds the Baseline Profile build on which they run.
While automatic generation helps users gain the best performance benefit, it
also increases the build time because of the double build and instrumentation
tests.

> [!NOTE]
> **Note:** You can always explicitly run the Baseline Profile generation and assemble a release build with `./gradlew :app:generateReleaseBaseline :app:assembleRelease`, in which case the Baseline Profile is generated first and then packaged with the assembled release version.

You can also specify this behavior per variant, as shown in the following
example:

### Kotlin

```kotlin
baselineProfile {
    variants {
        freeRelease {
            automaticGenerationDuringBuild = true
        }
    }
}
```

### Groovy

```groovy
baselineProfile {
    variants {
        freeRelease {
            automaticGenerationDuringBuild true
        }
    }
}
```

In the preceding example, the task `generateFreeReleaseBaselineProfile` runs
when starting `assembleFreeRelease`. This helps when the user wants to have, for
example, a `release` for distribution build that always generates the profile
when building, and a `releaseWithoutProfile` build for internal testing.

Instead of adding a new variant without a Baseline Profile, you can also disable
generation from the command line like this:

    ./gradlew assembleRelease -Pandroid.baselineProfile.automaticGenerationDuringBuild=false

## Store Baseline Profiles into sources

You can store Baseline Profiles in the source directory through the `saveInSrc`
flag in the `build.gradle.kts` of the application or library module:

- `true`: the Baseline Profile is stored in `src/<variant>/generated/baselineProfiles`. This lets you commit the latest generated profile with your sources.
- `false`: the Baseline Profile is stored in the intermediate files in the build directory. This way, when committing your code, you don't save the latest generated profile.

### Kotlin

```kotlin
baselineProfile {
    saveInSrc = true
}
```

### Groovy

```groovy
baselineProfile {
    saveInSrc true
}
```

You can also specify this behavior per variant:

### Kotlin

```kotlin
baselineProfile {
    variants {
        freeRelease {
            saveInSrc = true
        }
    }
}
```

### Groovy

```groovy
baselineProfile {
    variants {
        freeRelease {
            saveInSrc true
        }
    }
}
```

## Disable warnings

By default, the Baseline Profile Gradle Plugin warns you of situations that
might cause issues. To disable the warnings, you can set the relevant option to
`false` in your `build.gradle.kts` file. Here are the warning options:

    baselineProfile {
        warnings {

            /**
            * Warn when the Android Gradle Plugin version is higher than the max
            * tested one.
            */
            maxAgpVersion = true

            /**
            * Warn when a benchmark or baseline profile variant has been disabled.
            */
            disabledVariants = true

            /**
            * Warn that running `generateBaselineProfile` with AGP 8.0 doesn't
            * support running instrumentation tests for multiple build types at
            * once.
            */
            multipleBuildTypesWithAgp80 = true

            /**
            * Warn when no baseline profiles are generated after running the
            * generate baseline profile command.
            */
            noBaselineProfileRulesGenerated = true

            /**
            * Warn when no startup profiles are generated after running the generate
            * baseline profile command.
            */
            noStartupProfileRulesGenerated = true
        }
    }

## Filter profile rules

The Baseline Profile Gradle plugin lets you filter the Baseline Profile rules
generated. This is particularly helpful for libraries, if you want to exclude
profile rules for classes and methods that are part of other dependencies of the
sample app or the library itself. The filters can include and exclude specific
packages and classes. When you only specify excludes, only matching Baseline
Profile rules are excluded and everything else is included.

The filters specification can be any of the following:

- Package name ending with double wildcards to match the specified package and all subpackages. For example, `com.example.**` matches `com.example.method` and `com.example.method.bar`.
- Package name ending with wildcard to match specified package only. For example, `com.example.*` matches `com.example.method` but doesn't match `com.example.method.bar`.
- Class names to match a specific class---for example, `com.example.MyClass`.

The following examples show how to include and exclude specific packages:

### Kotlin

```kotlin
baselineProfile {
    filter {
        include("com.somelibrary.widget.grid.**")
        exclude("com.somelibrary.widget.grid.debug.**")
        include("com.somelibrary.widget.list.**")
        exclude("com.somelibrary.widget.list.debug.**")
        include("com.somelibrary.widget.text.**")
        exclude("com.somelibrary.widget.text.debug.**")
    }
}
```

### Groovy

```groovy
baselineProfile {
    filter {
        include 'com.somelibrary.widget.grid.**'
        exclude 'com.somelibrary.widget.grid.debug.**'
        include 'com.somelibrary.widget.list.**'
        exclude 'com.somelibrary.widget.list.debug.**'
        include 'com.somelibrary.widget.text.**'
        exclude 'com.somelibrary.widget.text.debug.**'
    }
}
```

Customize the filter rules for different variants as follows:

### Kotlin

```kotlin
// Non-specific filters applied to all the variants.
baselineProfile {
    filter { include("com.myapp.**") }
}

// Flavor-specific filters.
baselineProfile {
    variants {
        free {
            filter {
                include("com.myapp.free.**")
            }
        }
        paid {
            filter {
                include("com.myapp.paid.**")
            }
        }
    }
}

// Build-type-specific filters.
baselineProfile {
    variants {
        release {
            filter {
                include("com.myapp.**")
            }
        }
    }
}

// Variant-specific filters.
baselineProfile {
    variants {
        freeRelease {
            filter {
                include("com.myapp.**")
            }
        }
    }
}
```

### Groovy

```groovy
// Non-specific filters applied to all the variants.
baselineProfile {
    filter { include 'com.myapp.**' }
}

// Flavor-specific filters.
baselineProfile {
    variants {
        free {
            filter {
                include 'com.myapp.free.**'
            }
        }
        paid {
            filter {
                include 'com.myapp.paid.**'
            }
        }
    }
}

// Build-type specific filters.
baselineProfile {
    variants {
        release {
            filter {
                include 'com.myapp.**'
            }
        }
    }
}

// Variant-specific filters.
baselineProfile {
    variants {
        freeRelease {
            filter {
                include 'com.myapp.**'
            }
        }
    }
}
```

> [!NOTE]
> **Note:** Filters for a specific variant (`freeRelease`), are added to the flavor-level (`free`) filters, build-level (`release`) filters, and global filters specified outside the `variants` block.

You can also filter rules using the [`filterPredicate`](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:benchmark/benchmark-macro-junit4/src/main/java/androidx/benchmark/macro/junit4/BaselineProfileRule.kt;l=67;drc=4f34c5b0ef80804dcb9838902aa89f5f813560d9) argument in
`BaselineProfileRule.collect()`, but we recommend using the Gradle plugin to
filter because it provides a simpler way to filter subpackages and a single
place to configure the entire module.

## Customize benchmark and Baseline Profile build types

The Baseline Profile Gradle plugin creates additional build types to generate
the profiles and to run benchmarks. These build types are prefixed with
`benchmark` and `nonMinified`. For example, for the `release` build type, the
plugin creates the `benchmarkRelease` and `nonMinifiedRelease` build types.
These build types are automatically configured for the specific use case and
don't generally need any customization. But there are some cases in which it
might still be useful to apply some custom options, for example to apply a
different signing config.

You can customize the automatically generated build types using a subset of
build type properties; properties that aren't usable are overridden.
The following example shows how to customize the additional build types and
which properties are overridden:

### Kotlin

```kotlin
android {
    buildTypes {
        release {
            ...
        }
        create("benchmarkRelease") {
            // Customize properties for the `benchmarkRelease` build type here.
            // For example, you can change the signing config (by default
            // it's the same as for the `release` build type).
            signingConfig = signingConfigs.getByName("benchmarkRelease")
        }
        create("nonMinifiedRelease") {
            // Customize properties for the `nonMinifiedRelease` build type here.
            signingConfig = signingConfigs.getByName("nonMinifiedRelease")

            // From Baseline Profile Gradle plugin 1.2.4 and higher, you can't
            // customize the following properties, which are always overridden to
            // avoid breaking Baseline Profile generation:
            //
            // isJniDebuggable = false
            // isDebuggable = false
            // isMinifyEnabled = false
            // isShrinkResources = false
            // isProfileable = true
            // enableAndroidTestCoverage = false
            // enableUnitTestCoverage = false
        }
    }
}
```

### Groovy

```groovy
android {
    buildTypes {
        release {
            ...
        }
        benchmarkRelease {
            // Customize properties for the `benchmarkRelease` build type here.
            // For example, you can change the signing config (by default it's the
            // same as for the `release` build type.)
            signingConfig = signingConfigs.benchmarkRelease
        }
        nonMinifiedRelease {
            // Customize properties for the `nonMinifiedRelease` build type here.
            signingConfig = signingConfigs.nonMinifiedRelease

            // From Baseline Profile Gradle plugin 1.2.4 and higher, you can't use
            // the following properties, which are always overridden to avoid breaking
            // Baseline Profile generation:
            //
            // isJniDebuggable = false
            // isDebuggable = false
            // isMinifyEnabled = false
            // isShrinkResources = false
            // isProfileable = true
            // enableAndroidTestCoverage = false
            // enableUnitTestCoverage = false       
        }
    }
}
```

## Additional notes

When creating Baseline Profiles, here are some additional things to be aware of:

- *Compiled* Baseline Profiles must be smaller than 1.5 MB. This doesn't
  apply to the text format in your source files, which are typically much
  larger prior to compilation. Verify the size of your binary Baseline
  Profile by locating it in the output artifact under
  `assets/dexopt/baseline.prof` for APK or
  `BUNDLE-METADATA/com.android.tools.build.profiles/baseline.prof` for AAB.

  > [!TIP]
  > **Tip:** In Android Studio Flamingo (2022.2.1) or later, verify the size in the [APK Analyzer](https://developer.android.com/studio/debug/apk-analyzer).

- Broad rules that compile too much of the application can slow down startup
  due to increased disk access. If you're just starting with Baseline
  Profiles, don't worry about this. However, depending on your app and the
  size and number of journeys, adding a lot of journeys can result in
  suboptimal performance. Test the performance of your app by trying different
  profiles and verifying that the performance doesn't regress after the
  additions.

## Codelabs

### [Inspect app performance with Macrobenchmark](https://developer.android.com/codelabs/android-macrobenchmark-inspect)

Dive into macrobenchmarking to measure performance. [Learn more](https://developer.android.com/codelabs/android-macrobenchmark-inspect)

### [Improve app performance with Baseline Profiles](https://developer.android.com/codelabs/android-baseline-profiles-improve)

Generate a custom Baseline Profile tailored to an Android app and verify its effectiveness. [Learn more](https://developer.android.com/codelabs/android-baseline-profiles-improve)