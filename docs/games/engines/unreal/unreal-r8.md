---
title: https://developer.android.com/games/engines/unreal/unreal-r8
url: https://developer.android.com/games/engines/unreal/unreal-r8
source: md.txt
---

Although your core game logic in Unreal Engine is written in C++ or Blueprints,
Android packaging compiles Java and Kotlin bytecode (`classes.dex`) to handle
`GameActivity` lifecycle events, Google Play services, billing, audio, and
analytics plugins.

[R8](https://developer.android.com/topic/performance/app-optimization/enable-app-optimization), the default code shrinker and optimizer in the Android Gradle Plugin
(AGP), removes unused classes and methods and optimizes bytecode. This not only
decreases your package download size, but also reduces the runtime memory
footprint of memory-mapped (`mmap`) DEX pages and baseline Java process
overhead, mitigating physical memory pressure and [low memory killer (LMK)](https://developer.android.com/games/optimize/vitals/lmk)
terminations. Google Play also monitors your game's DEX optimization levels
through the [DEX code optimization](https://developer.android.com/google/play/vitals/code-optimization) metric in Android vitals.

## Default behavior and Unreal Engine version support

Starting in **UE 4.22.0** , Unreal Engine's `UEDeployAndroid.cs` injects
`minifyEnabled true` into the generated Android Release build configuration
(`buildAdditions.gradle`) by default. Because **UE 4.25** upgraded the bundled
toolchain to AGP 4.0.0, **R8 is enabled by default (`true`)** on all Release
(Shipping and Distribution) builds in UE 4.25 and higher without additional
setup.

| Unreal Engine version | Bundled AGP | Release default | Debug default | Behavior |
|---|---|---|---|---|
| **UE 4.21 and earlier** | Legacy Gradle or Ant | Disabled (`false`) | Disabled (`false`) | No `minifyEnabled` configuration injected by the engine. |
| **UE 4.22 to 4.24** | Earlier than 3.4 | **Enabled (ProGuard)** | Disabled (`false`) | `minifyEnabled true` enabled by default in Release builds (runs ProGuard). |
| **UE 4.25 to 5.3** | 4.0.0 | **Enabled (R8)** | Disabled (`false`) | AGP 4.0 adoption runs **R8 by default** in Release builds. |
| **UE 5.4 to 5.7** | 7.4.2 | **Enabled (R8)** | Disabled (`false`) | AGP 7.x removes legacy `useProguard` options; R8 runs exclusively. |
| **UE 5.8 (5.8.3+)** | 8.13.0 | **Enabled (R8)** | Disabled (`false`) | Uses AGP 8.x and modern R8 optimization pipelines by default. |

## Release and Debug build differences

UnrealBuildTool (`UEDeployAndroid.cs`) configures the generated
`buildAdditions.gradle` file differently for Release and Debug builds:

    buildTypes {
        release {
            signingConfig signingConfigs.release
            minifyEnabled true
            proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'
        }
        debug {
            debuggable true
            signingConfig signingConfigs.debug
        }
    }

- **Release (Shipping or Distribution)** : Sets `minifyEnabled true` and applies `proguard-rules.pro` by default, running R8 code shrinking and obfuscation.
- **Debug (Development)** : Enables `debuggable true` and omits `minifyEnabled` (defaulting to `false`) to preserve fast build iteration and symbol debugging.

## Add keep rules using Unreal Plugin Language (UPL)

Because R8 runs automatically on Release builds in UE 4.25 and higher, you must
preserve Java classes reached only through C++ JNI (`JNIEnv->FindClass`,
`GetMethodID`) or the manifest. Classes without Java call sites are treated as
unused and stripped by R8, which can cause features that work in Development
builds to fail with `ClassNotFoundException` or `NoSuchMethodError` in Shipping
builds.

Use the `<proguardAdditions>` tag in an [Unreal Plugin Language
(UPL)](https://dev.epicgames.com/documentation/unreal-engine/using-unreal-plugin-language-for-mobile-projects-in-unreal-engine) XML file to merge custom keep rules into
`proguard-rules.pro` during packaging. Add the following block to your project
or plugin `*_UPL.xml` file:

    <root xmlns:android="http://schemas.android.com/apk/res/android">
        <proguardAdditions>
            <insert>
                -keep class com.epicgames.unreal.** { *; }
                -keep class com.example.plugin.** { public *; }
                -dontwarn com.example.plugin.**
            </insert>
        </proguardAdditions>
    </root>

## Troubleshoot common issues

This section describes how to resolve common packaging and runtime issues when
using R8 in Unreal Engine.

### Temporarily disable R8 for debugging

To isolate whether a Release-only crash is caused by R8 stripping required
classes, insert `DISABLE_MINIFY=1` under `<gradleProperties>` in your UPL file.
When present, `UEDeployAndroid.cs` generates `minifyEnabled false`:

    <gradleProperties>
        <insert>
            DISABLE_MINIFY=1
        </insert>
    </gradleProperties>

> [!CAUTION]
> **Caution:** Use `DISABLE_MINIFY=1` only for debugging. For production Release builds, remove this property and add the required `-keep` rules to `<proguardAdditions>` so your game retains R8 memory and size optimizations. For more information about writing keep rules, see [Customize which code to
> keep](https://developer.android.com/topic/performance/app-optimization/keep-code).

### `Missing classes detected while running R8` packaging errors

In UE 5.4 and higher (AGP 7.4.2+), R8 enforces strict missing-class checks. If
packaging fails with this error, inspect `missing_rules.txt` in your
intermediate build directory (under
`Intermediate/Android/.../gradle/app/build/outputs/mapping/release/missing_rules.txt`)
and add the missing library dependencies or required rules to
`<proguardAdditions>` in your UPL file.

### R8 full mode compatibility with third-party SDKs

In UE 5.8 and higher (AGP 8.13.0+), [R8 full mode](https://developer.android.com/topic/performance/app-optimization/full-mode) is enabled by default to
perform more aggressive optimizations. If a legacy third-party Android SDK fails
at runtime due to reflection issues, update the plugin's ProGuard rules or
revert R8 to compatibility mode by adding the following property to your UPL
file:

    <gradleProperties>
        <insert>
            android.enableR8.fullMode=false
        </insert>
    </gradleProperties>