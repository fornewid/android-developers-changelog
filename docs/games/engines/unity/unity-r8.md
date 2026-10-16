---
title: https://developer.android.com/games/engines/unity/unity-r8
url: https://developer.android.com/games/engines/unity/unity-r8
source: md.txt
---

Although your core game logic in Unity is written in C# (compiled with IL2CPP),
Android builds include substantial Java and Kotlin bytecode (`classes.dex`) to
handle `UnityPlayerActivity` lifecycle events, Google Play services, billing,
ads, and social SDKs.

Enabling [R8](https://developer.android.com/topic/performance/app-optimization/enable-app-optimization), the default code shrinker and optimizer in the Android Gradle
Plugin (AGP), removes unused classes and methods and optimizes bytecode. This
not only decreases your app download size, but also reduces the runtime memory
footprint of memory-mapped (`mmap`) DEX pages and baseline Java process
overhead, mitigating physical memory pressure and [low memory killer (LMK)](https://developer.android.com/games/optimize/vitals/lmk)
terminations. Google Play also monitors your game's DEX optimization levels
through the [DEX code optimization](https://developer.android.com/google/play/vitals/code-optimization) metric in Android vitals.

## Default behavior and Unity version support

In Unity, code minification is **disabled by default (`false`)** for both
Release and Debug builds when creating a new project.

Unity first introduced R8 as an optional toggle in **Unity 2020.1.0f1** .
Starting in **Unity 2022.2.0f1** (and backported to **Unity 2021.3.41f1** LTS),
Unity upgraded its bundled toolchain to AGP 7.1.2+, removed legacy ProGuard
support, and runs R8 exclusively whenever minification is enabled.

| Unity version | Bundled AGP | Release default | R8 support and required configuration |
|---|---|---|---|
| **2019.4 LTS and earlier** | Earlier than 3.4 | Disabled (`false`) | **Not supported** (legacy ProGuard only). |
| **2020.1.0f1 to 2021.3.40f1** | 3.4 to 4.0 | Disabled (`false`) | **Optional** (defaults to ProGuard). Enable both **Minify \> Release** and **Use R8**. |
| **2021.3.41f1 and higher** (2021 LTS) | 7.1+ | Disabled (`false`) | **R8 only** . Enable **Minify \> Release** to run R8 automatically. |
| **2022.2.0f1 to Unity 6+** | 7.1 to 8.x | Disabled (`false`) | **R8 only** . Enable **Minify \> Release** to run R8 automatically. |

> [!NOTE]
> **Note:** Even in Unity versions where R8 is the sole minification tool, the **Minify** setting itself remains disabled by default. You must enable it in your project settings for R8 to run.

## Enable R8 in Player Settings

To enable R8 code shrinking and optimization for Release builds:

1. In the Unity Editor, open **Edit \> Project Settings** and select **Player**.
2. Select the **Android** tab and expand **Publishing Settings \> Build**.
3. Under the **Minify** section, configure the options for your Unity version:
   - **Unity 2021.3.41f1+ and 2022.2.0f1+** : Select **Release** . Unity runs R8 automatically during the `minifyReleaseWithR8` Gradle task.
   - **Unity 2020.1.0f1 to 2021.3.40f1** : Select both **Release** and **Use
     R8**.

If you automate builds using C# Editor scripts, configure these properties
through `PlayerSettings.Android`:

    using UnityEditor;

    public static class AndroidBuildConfig
    {
        public static void EnableR8ForRelease()
        {
            PlayerSettings.Android.minifyRelease = true;

            // Required only in Unity 2020.1.0f1 to 2021.3.40f1 and 2022.1 or earlier
            // (In Unity 2021.3.41f1+ and 2022.2+, R8 is always used when minification is enabled)
    #if !UNITY_2022_2_OR_NEWER
            PlayerSettings.Android.minifyWithR8 = true;
    #endif
        }
    }

## Add keep rules for JNI and reflection

Java classes and methods invoked dynamically from C# scripts using
[`AndroidJavaClass`](https://docs.unity3d.com/ScriptReference/AndroidJavaClass.html) or [`AndroidJavaObject`](https://docs.unity3d.com/ScriptReference/AndroidJavaObject.html) have
no static Java call sites. Without explicit keep rules, R8 might consider these
classes unused and strip or rename them.

To preserve your custom Java bridges:

1. In **Project Settings \> Player \> Android \> Publishing Settings \> Build** , enable **Custom Proguard File**.
2. Open the generated `Assets/Plugins/Android/proguard-user.txt` file.
3. Add `-keep` rules for classes accessed over JNI or required by third-party plugins:

    # Keep custom Java classes invoked from C# using JNI bridges
    -keep class com.example.yourgame.** { *; }

    # Keep callback interfaces passed between C# and Java
    -keep interface com.example.yourgame.IPluginCallback { *; }

## Troubleshoot common issues

This section describes how to resolve common build and runtime issues when using
R8 in Unity.

### `Missing classes detected while running R8` build errors

In Unity versions using AGP 7.0 and higher (2021.3.41f1+ and 2022.2+), R8
enforces strict missing-class checks. If a build fails with this error, inspect
the generated `missing_rules.txt` file in your build output directory (under
`Library/Bee/Android/Prj/.../build/outputs/mapping/release/missing_rules.txt` or
`Temp/gradleOut/...`) and add the required dependencies or rules to
`proguard-user.txt`. For more information about writing keep rules, see
[Customize which code to keep](https://developer.android.com/topic/performance/app-optimization/keep-code).

### R8 full mode compatibility with third-party plugins

In AGP 8.0 and higher (Unity 6+), [R8 full mode](https://developer.android.com/topic/performance/app-optimization/full-mode) is enabled by default to
perform more aggressive optimizations. If a legacy Android plugin fails at
runtime due to reflection issues, update the plugin's ProGuard rules or revert
R8 to compatibility mode:

1. In **Publishing Settings \> Build** , enable **Custom Gradle Properties
   Template**.
2. Open `Assets/Plugins/Android/gradleTemplate.properties` and add the following property:

    android.enableR8.fullMode=false