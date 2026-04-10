---
title: https://developer.android.com/build/include-native-symbols
url: https://developer.android.com/build/include-native-symbols
source: md.txt
---

By default, native code libraries are stripped in release builds of your app.
This stripping consists of removing the symbol table and debugging information
contained in any native libraries used by your app. Stripping native code
libraries results in significant size savings; however, it's impossible to
diagnose crashes on the Google Play Console due to the missing information (such
as class and function names). To debug crashes, you must include a debug symbols
file with your app in Play Console.

## Upload a symbols file

The Google Play Console reports native crashes under [Android
vitals](https://developer.android.com/topic/performance/vitals/crash#diagnose-crashes). With a few steps, you
can generate and upload a native debug symbols file for your app. This file
enables symbolicated native crash stack traces (that include class and function
names) in Android vitals to help you debug your app in production. These steps
vary depending on the version of the Android Gradle plugin used in your project
and whether you're using an Android App Bundle (recommended) or APK.

> [!NOTE]
> **Note:** To restore symbol names in crash reports yourself, use the [ndk-stack
> tool](https://developer.android.com/ndk/guides/ndk-stack), which comes packaged with the Android NDK.

### Android Gradle plugin version 4.1 or later

If your project builds an Android App Bundle (AAB), you can configure your build
to automatically include the native debug symbols file in the AAB so it's
uploaded to the Play Console when you publish your app. To include this file in
release builds, add the following to your app's `build.gradle.kts` file:

`android.buildTypes.release.ndk.debugSymbolLevel = { SYMBOL_TABLE | FULL }`

Select the debug symbol level from the following:

- Use `SYMBOL_TABLE` to get function names in the Play Console's symbolicated stack traces. This level supports [tombstones](https://source.android.com/devices/tech/debug).
- Use `FULL` to get function names, files, and line numbers in the Play Console's symbolicated stack traces.

> [!NOTE]
> **Note:** There is a 300 MB limit for the native debug symbols file. If your debug symbols footprint is too large, use `SYMBOL_TABLE` instead of `FULL` to decrease the file size.

If your project builds an APK, use the
`android.buildTypes.release.ndk.debugSymbolLevel` setting shown earlier to
generate the native debug symbols file separately. Manually [upload the native
debug symbols
file](https://support.google.com/googleplay/android-developer/answer/9848633#upload_file)
to the Google Play Console (the process is similar to uploading a mapping file
to [deobfuscate stack traces](https://developer.android.com/topic/performance/app-optimization/test-and-troubleshoot-the-optimization#recover-original-stack-trace)).
As part of the build process, the Android Gradle plugin outputs this file in the
following project location:

`app/build/outputs/native-debug-symbols/<var>variant-name</var>/native-debug-symbols.zip`

### Android Gradle plugin version 4.0 or earlier (and other build systems)

As part of the build process, the Android Gradle plugin keeps a copy of the
unstripped libraries in a project directory. This directory structure is similar
to the following:

    app/build/intermediates/cmake/universal/release/obj/
    ├── armeabi-v7a/
    │   ├── libgameengine.so
    │   ├── libothercode.so
    │   └── libvideocodec.so
    ├── arm64-v8a/
    │   ├── libgameengine.so
    │   ├── libothercode.so
    │   └── libvideocodec.so
    ├── x86/
    │   ├── libgameengine.so
    │   ├── libothercode.so
    │   └── libvideocodec.so
    └── x86_64/
        ├── libgameengine.so
        ├── libothercode.so
        └── libvideocodec.so

> [!NOTE]
> **Note:** If you use a different build system, you could modify it to store unstripped libraries in a directory with the required structure.

1. Zip up the contents of this directory:

       cd app/build/intermediates/cmake/universal/release/obj
       zip -r symbols.zip .

2. Manually [upload the `symbols.zip` file](https://support.google.com/googleplay/android-developer/answer/9848633#upload_file) to the Google Play Console.

> [!NOTE]
> **Note:** If your file is too big, it's likely because your `.so` files contain a symbol table and also DWARF debugging info, which isn't needed to symbolicate your code. On AGP 4.0 or lower, you can remove the DWARF debugging info by running the following command:   
>
> `$OBJCOPY --strip-debug lib.so lib.so.sym`   
>
> where `$OBJCOPY` points to the specific version for the ABI you're stripping (for example, `ndk-bundle/toolchains/aarch64-linux-android-4.9/prebuilt/linux-x86_64/bin/aarch64-linux-android-objcopy`). This command is equivalent to the [`SYMBOL_TABLE` option for AGP 4.1 and higher](https://developer.android.com/build/include-native-symbols#agp-4.1).