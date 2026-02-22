---
title: https://developer.android.com/google/play/requirements/64-bit
url: https://developer.android.com/google/play/requirements/64-bit
source: md.txt
---

Apps published on Google Play need to support
[64-bit architectures](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html). Adding a 64-bit version of your app
provides performance improvements and sets you up for devices with 64-bit-only
hardware.

The following steps ensure that your 32-bit app supports 64-bit devices.

## Assess your app

If your app uses only code written in the Java programming language or in
Kotlin, including all libraries or SDKs, then your app supports 64-bit devices.
If your app uses any native code, or you are unsure if it does, then assess your
app.

### Quick status check

Go to the Play Console and take a look at existing releases to see whether they
are compliant.

![](https://developer.android.com/static/google/play/requirements/images/64bit/console_release_status.png)

Play Console also shows warnings that apply to your draft releases if there are
any issues related to the 64-bit requirement. The following image is an example.

![](https://developer.android.com/static/google/play/requirements/images/64bit/console_warning.png)

If an alert appears, see the following steps to make your app compatible with
64-bit devices.

### Does your app use native code?

Your app makes use of native code if it:

- Uses any C/C++ (native) code in your app.
- Links with any third party native libraries.
- Is built by a third-party app builder that uses native libraries.

### Does your app include 64-bit libraries?

Inspect the structure of your APK file. When built, the APK is packaged with any
native libraries needed by the app. Native libraries are stored in various
folders based on the [ABI](https://developer.android.com/ndk/guides/abis#sa). It isn't required to support every
64-bit architecture, but for each native 32-bit architecture you support you
must include the corresponding 64-bit architecture.

For the *ARM* architecture, the 32-bit libraries are located in **armeabi-v7a** .
The 64-bit equivalent is **arm64-v8a**.

For the *x86* architecture, look for **x86** for 32-bit and **x86_64** for
64-bit.

Ensure that you have native libraries in both of these folders. To recap:

| Platform | 32-bit libraries folder | 64-bit libraries folder |
|---|---|---|
| ARM | `lib/armeabi-v7a` | `lib/arm64-v8a` |
| x86 | `lib/x86` | `lib/x86_64` |

Note that depending on your app, there may or may not be exactly the same set of
libraries in each folder. The goal is to ensure that your app runs correctly in
a 64-bit-only environment.

In a typical case, an APK or bundle that's built for both 32-bit and 64-bit
architectures has folders for both ABIs, each with a corresponding set of native
libraries. If there's no support for 64-bit, you might see a 32-bit ABI folder
but not a 64-bit folder.

### Look for native libraries using APK Analyzer

[APK Analyzer](https://developer.android.com/studio/debug/apk-analyzer) is a tool that lets you evaluate various
aspects of a built APK. Use it to find any native libraries, and ensure 64-bit
libraries are present.

1. Open *Android Studio* , and **open any project**.
2. From the menu, select **Build \> Analyze APK**...

   ![launch APK analyzer](https://developer.android.com/static/google/play/requirements/images/64bit/image1.png)
3. Choose the APK you want to evaluate.

4. Look within the **lib** folder, which hosts '.so' files if any. If there are
   none, then your app supports 64-bit devices and no further action is
   required. If you see **armeabi-v7a** or **x86**, then you have 32-bit
   libraries.

5. Check to see if you have similar '.so' files in the **arm64-v8a** or
   **x86_64** folder.

   ![launch APK analyzer](https://developer.android.com/static/google/play/requirements/images/64bit/image2.png)
6. If you don't have any **arm64-v8a** or **x86_64** libraries, update your
   build process to start building and packaging those artifacts in your APK.

7. If you already see both libraries being packaged, you can skip ahead to
   [testing your app on 64-bit hardware](https://developer.android.com/google/play/requirements/64-bit#test-64-bit-hardware).

### Look for native libraries by unzipping APKs

APK files are structured like zip files. With the command line or any other
extraction tool, extract the APK file. Depending on your extraction tool, you
might have to rename the file to .zip.

Browse the files that are extracted, following the guidance above to determine
if your app supports 64-bit devices. You can run the following command example
from the command line:  

    :: Command Line
    > zipinfo -1 YOUR_APK_FILE.apk | grep \.so$
    lib/armeabi-v7a/libmain.so
    lib/armeabi-v7a/libmono.so
    lib/armeabi-v7a/libunity.so
    lib/arm64-v8a/libmain.so
    lib/arm64-v8a/libmono.so
    lib/arm64-v8a/libunity.so

Note in this example the presence of **armeabi-v7a** and **arm64-v8a**
libraries, which means the app supports 64-bit architectures.

## Build your app with 64-bit libraries

The following instructions outline how to build 64-bit libraries. Note that
these steps only cover building code and libraries that you are able to build
from source.
| **Note:** If you are using any external SDKs or libraries, ensure you are using 64-bit versions by following [the preceding steps](https://developer.android.com/google/play/requirements/64-bit#assess-your-app). Reach out to the SDK or library owner if a 64-bit version is not available and take this into account when planning your support for 64-bit devices.

### Build with Android Studio or Gradle

Most Android Studio projects use Gradle as the underlying build system, so this
section applies to both cases. To enable builds for your native code, add
**arm64-v8a** and/or **x86_64** , depending on the architectures you want to
support, to the [ndk.abiFilters](https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.NdkOptions.html) setting in your app's
'build.gradle' file:  

### Groovy

```groovy
// Your app's build.gradle
plugins {
  id 'com.android.app'
}

android {
   compileSdkVersion 27
   defaultConfig {
       appId "com.google.example.64bit"
       minSdkVersion 15
       targetSdkVersion 28
       versionCode 1
       versionName "1.0"
       ndk.abiFilters 'armeabi-v7a','arm64-v8a','x86','x86_64'
// ...
```

### Kotlin

```kotlin
// Your app's build.gradle
plugins {
    id("com.android.app")
}

android {
    compileSdkVersion(27)
    defaultConfig {
        appId = "com.google.example.64bit"
        minSdkVersion(15)
        targetSdkVersion(28)
        versionCode = 1
        versionName = "1.0"
        ndk {
            abiFilters += listOf("armeabi-v7a","arm64-v8a","x86","x86_64")
        }
// ...
```

### Build with CMake

If your app is built using [CMake](https://developer.android.com/ndk/guides/cmake#options), you can build for 64-bit
ABIs by passing the
**arm64-v8a** into the '-DANDROID_ABI' parameter:  

    :: Command Line
    > cmake -DANDROID_ABI=arm64-v8a ... or
    > cmake -DANDROID_ABI=x86_64 ...

| **Note:** This option has no effect when using `externalNativeBuild`. See the [Building with Gradle](https://developer.android.com/google/play/requirements/64-bit#android-studio-gradle) section.

### Build with ndk-build

If your app is built with [ndk-build](https://developer.android.com/ndk/guides/ndk-build), you can build for
64-bit ABIs by modifying your ['Application.mk'](https://developer.android.com/ndk/guides/application_mk) file using
the `APP_ABI` variable:  

    APP_ABI := armeabi-v7a arm64-v8a x86 x86_64

| **Note:** This option has no effect when using `externalNativeBuild`. See the [Building with Gradle](https://developer.android.com/google/play/requirements/64-bit#android-studio-gradle) section.

### Port 32-bit code to 64-bit

If your code already runs on the desktop or iOS, you shouldn't need to do any
extra work for Android. If this is the first time your code has been built for a
64-bit system, the main issue you must address is that pointers no longer fit in
32-bit integer types like `int`.

Update code that stores pointers in types such as `int`, `unsigned`, or
`uint32_t`. On Unix systems, `long` matches the pointer size, but this isn't
true on Windows. Instead, use the intention-revealing types `uintptr_t` or
`intptr_t`. To store the difference between two pointers, use the `ptrdiff_t`
type.

You should always prefer the specific, fixed-width integer types defined in
[`<stdint.h>`](https://en.cppreference.com/w/c/types/integer) rather than non fixed-width types such as
`int` or `long`, even for non-pointers.

Use the following compiler flags to catch cases where your code is incorrectly
converting between pointers and integers:  

    -Werror=pointer-to-int-cast
    -Werror=int-to-pointer-cast
    -Werror=shorten-64-to-32

Java classes with `int` fields that hold pointers to C/C++ objects have the same
problem. Search for `jint` in your JNI source and ensure that you switch to
`long` on the Java side and `jlong` on the C++ side.
| **Note:** Crashes that stem from pointers being truncated manifest as a SIGSEGV where the top 32 bits of the fault address are all zero.

Implicit function declarations are a lot more dangerous for 64-bit code. C/C++
assume that the return type of an implicitly declared function (that is, a
function that the compiler hasn't seen a declaration for) is `int`. If the
actual return type of your function is a pointer, this works fine on a 32-bit
system where your pointer fits into an int. However, on a 64-bit system, the
compiler drops the top half of your pointer. For example:  

    // This function returns a pointer:
    // extern char* foo();

    // If you don't include a header that declares it,
    // when the compiler sees this:
    char* result = foo();

    // Instead of compiling that to:
    result = foo();

    // It compiles to something equivalent to:
    result = foo() & 0xffffffff;

    // Which will then cause a SIGSEGV if you try to dereference `result`.

The following compiler flag turns implicit function declaration warnings into
errors so that you can find and fix this problem more easily:  

    -Werror=implicit-function-declaration

If you have inline assembler, rewrite it or use a plain C/C++ implementation.

If you have hard-coded sizes of types (8 or 16 bytes, for example), replace them
with the equivalent `sizeof(T)` expression, such as `sizeof(void*)`.

If you need to conditionally compile different code for 32-bit than 64-bit, you
can use the `#if defined(__LP64__)` for generic 32/64 differences, or `__arm__`,
`__aarch64__` (arm64), `__i386__` (x86), and `__x86_64__` for the specific
architectures supported by Android.

Adjust format strings for `printf` or `scanf`-like functions, as the traditional
format specifiers don't allow you to specify 64-bit types in a way that's
correct for both 32-bit and 64-bit devices. The `PRI` and `SCN` macros in
[`<inttypes.h>`](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/inttypes.h.html) solve this problem, `PRIxPTR` and `SCNxPTR`
for writing and reading hex pointers; and `PRId64` and `SCNd64` for writing and
reading 64-bit values portably.

When shifting, you may need to use `1ULL` to get a 64-bit constant to shift
rather than using `1`, which is only 32 bits.

### Mitigate size increases with Android App Bundle

Adding 64-bit architecture support to your app can cause your APK size to grow.
We strongly recommend taking advantage of the
[Android App Bundle](https://developer.android.com/platform/technology/app-bundle) feature to minimize the size impact of
including both 32- and 64-bit native code in the same APK.

### Game developers

The three most-used engines support 64-bit:

- Unreal since 2015
- Cocos2d since 2015
- Unity since 2018

### Unity developers

#### Upgrade to capable versions

Unity provides 64-bit support with versions [2018.2](https://blogs.unity3d.com/2018/07/10/2018-2-is-now-available/) and
[2017.4.16](https://unity3d.com/unity/whatsnew/unity-2017.4.16).

If you are on a version of Unity that does not support 64-bit, determine the
version you want to upgrade to and follow the [guides](https://docs.unity3d.com/Manual/UpgradeGuides.html) that
Unity provides to migrate your environment, ensuring your app is upgraded to a
version that can build 64-bit libraries. Unity recommends you have access to the
latest features and updates by [upgrading to the latest LTS](https://blogs.unity3d.com/2018/04/09/new-plans-for-unity-releases-introducing-the-tech-and-long-term-support-lts-streams/)
version of the editor.

Here's a chart that outlines the various Unity versions and what you should do:

| Unity Version | **Version supports 64-bit?** | **Recommended course of action** |
|---|---|---|
| 2020.x | ✔️ | Ensure your build settings output 64-bit libraries. |
| 2019.x | ✔️ | Ensure your build settings output 64-bit libraries. |
| 2018.4 (LTS) | ✔️ | Ensure your build settings output 64-bit libraries. |
| 2018.3 | ✔️ | Ensure your build settings output 64-bit libraries. |
| 2018.2 | ✔️ | Ensure your build settings output 64-bit libraries. |
| 2018.1 | ➖ | Has experimental 64-bit support. |
| 2017.4 (LTS) | ✔️ | Supported as of [2017.4.16](https://unity.com/releases/editor/whats-new/2017.4.16). Ensure your build settings output 64-bit libraries. |
| 2017.3 | ✖️ | Upgrade to version that supports 64-bit. |
| 2017.2 | ✖️ | Upgrade to version that supports 64-bit. |
| 2017.1 | ✖️ | Upgrade to version that supports 64-bit. |
| \<=5.6 | ✖️ | Upgrade to version that supports 64-bit. |

#### Change build settings to output 64-bit libraries

If you are using a version of Unity that supports 64-bit Android libraries, you
can generate a 64-bit version of your app by adjusting your build settings. Use
the [IL2CPP backend](https://blogs.unity3d.com/2017/12/20/meeting-google-play-requirements-in-the-future/) as your Scripting Backend. To set up
your Unity project to build 64-bit architecture, do the following:

1. Go to **Build Settings** and ensure you are building for Android by verifying that the Unity symbol is next to **Android** under **Platform** . 1. If the Unity symbol is not next to the Android platform, select **Android** and click **Switch Platform.**
2. Click **Player settings.**

   ![Player settings in Unity](https://developer.android.com/static/google/play/requirements/images/64bit/image4.png)
3. Navigate to **Player Settings Panel \> Settings for Android \> Other
   settings \> Configuration**

4. Set **Scripting Backend** to **IL2CPP.**

5. Select the **Target Architecture \> ARM64** checkbox.

   ![set target architectures in Unity](https://developer.android.com/static/google/play/requirements/images/64bit/image3.png)
6. Build as normal!

Note that building for ARM64 requires all your assets to be built specifically
for that platform. Follow Unity's [guidance](https://docs.unity3d.com/Manual/ReducingFilesize.html) for reducing APK
size, and consider taking advantage of the
[Android App Bundle](https://developer.android.com/platform/technology/app-bundle) feature to help mitigate this increase
in size.

## Multi-APK and 64-bit compliance

If you are using Google Play's [multiple-APK support](https://developer.android.com/google/play/publishing/multiple-apks) to
publish your app, note that compliance with the 64-bit requirement is evaluated
at the release level. However, the 64-bit requirement does not apply to APKs or
app bundles that are not distributed to devices running Android 9 Pie or later.

If one of your APKs is marked as not being compliant, but is an earlier version
and it's not possible to bring it into compliance, one strategy is to add a
`maxSdkVersion="27"` attribute in the [`uses-sdk`](https://developer.android.com/guide/topics/manifest/uses-sdk-element) element in
that APK's manifest. This APK isn't delivered to devices running Android 9 Pie
or later, and no longer blocks compliance.

## RenderScript and 64-bit compliance

If your app uses RenderScript and was built with an earlier version of the
Android tools, you might see 64-bit compliance issues for the app. With build
tools earlier than 21.0.0, the compiler may generate bitcode into an external
`.bc` file. These legacy `.bc` files are no longer supported for 64-bit
architectures, so the presence of the file in your APK causes the compliance
issue.

To fix the issue, remove any`.bc` files in your project, upgrade your
environment to `build-tools-21.0.0` or later, and set the
[`renderscriptTargetApi`](https://developer.android.com/guide/topics/renderscript/compute) in Android Studio to 21+, to tell
the compiler to not emit `.bc` files. Then, rebuild your app, inspect for `.bc`
files, and upload to Play Console.

## Test your app on 64-bit hardware

The 64-bit version of your app should offer the same quality and feature set as
the 32-bit version. Test your app to make sure that users on the latest 64-bit
devices have a great experience in your app.

### 64-bit-only devices

Whenever possible, we recommend testing your app in a strict 64-bit-only
environment using one of the following options:

- [Google Pixel with a 64-bit-only system image](https://developer.android.com/google/play/requirements/64-bit#64-bit-pixel)
- [Android Emulator](https://developer.android.com/google/play/requirements/64-bit#64-bit-emulator)

#### Google Pixel with a 64-bit-only system image

To facilitate app development and testing, we've provided special system images
with a strict 64-bit-only environment for some Pixel devices. These 64-bit-only
images were originally provided concurrently with standard factory system images
for the Android 13 and 14 preview releases, but you can continue to use them as
you test your app for 64-bit compatibility.
| **Caution:** While you can switch a single test device between 64-bit-only system images that are based on different Android versions, you must first [return the
| device to the latest stable, public build](https://developer.android.com/google/play/requirements/64-bit#public) before flashing the 64-bit-only image for the other version of the Android platform.

##### Get a 64-bit-only image

Similar to factory system images, you can flash a 64-bit-only image to your
device [using the Android Flash Tool](https://developer.android.com/google/play/requirements/64-bit#flashtool) or by [flashing your
device manually](https://developer.android.com/google/play/requirements/64-bit#flash), as described in the following sections.
| **Note:** While the [Pixel 7 and Pixel 7 Pro were the first Android phones to launch
| with support for only 64-bit apps](https://android-developers.googleblog.com/2022/10/64-bit-only-devices.html), these devices launched with Android 13 system images that include a 32-bit file system and 32-bit system libraries to handle compatibility edge cases. For this reason, if you have either a Pixel 7 or Pixel 7 Pro, as well as a Pixel device with an available 64-bit-only system image, use the device with the 64-bit-only image to create a better-controlled environment for testing 64-bit compatibility.

##### Flash your device using Android Flash Tool

**Android Flash Tool** lets you securely flash a system image
to your supported Pixel device. Android Flash Tool works with any Web browser
that supports WebUSB, such as Chrome or Edge 79+.

Android Flash Tool guides you step-by-step through the process of flashing your
device---there's no need to have tools installed---but you do need to unlock your
device and [enable USB Debugging in Developer options](https://developer.android.com/studio/debug/dev-options#enable). For
complete instructions, see the [Android Flash Tool
documentation](https://source.android.com/setup/contribute/flash).

Connect your device over USB, then, depending on the type of system image you
want to flash, navigate to Android Flash Tool using one of the following links
and follow the onscreen guidance:

- **Android 14 (Beta 5.2) 64-bit-only system images**

  Select the device you are trying to flash:
  - [Pixel 4a (5G)](https://flash.android.com/build/UPB5.230623.005?target=bramble_64-user)
  - [Pixel 5](https://flash.android.com/build/UPB5.230623.005?target=redfin_64-user)
  - [Pixel 6](https://flash.android.com/build/UPB5.230623.005?target=oriole_64-user)
  - [Pixel 6 Pro](https://flash.android.com/build/UPB5.230623.005?target=raven_64-user)
- **Android 13 (QPR3 Beta 3.2) 64-bit-only system images**

  Select the device you are trying to flash:
  - [Pixel 4a (5G)](https://flash.android.com/build/T3B3.230413.009?target=bramble_64-user)
  - [Pixel 5](https://flash.android.com/build/T3B3.230413.009?target=redfin_64-user)
  - [Pixel 6](https://flash.android.com/build/T3B3.230413.009?target=oriole_64-user)
  - [Pixel 6 Pro](https://flash.android.com/build/T3B3.230413.009?target=raven_64-user)

##### Flash your device manually

You can also download the latest system image and manually flash it to your
device. See the following table to download the system image for your test
device. Manually flashing a device is useful if you need precise control over
the test environment or if you need to reinstall frequently, such as when
performing automated testing.

After you back up your device data and download the matching system image, you
can [flash the image onto your device](https://developers.google.com/android/images#instructions).

You can choose to [return to the latest public build](https://developer.android.com/google/play/requirements/64-bit#public) at any
time.

###### 64-bit-only factory images for Android 14 (Beta 5.3)

These images provide a strict 64-bit-only environment for testing 64-bit app
compatibility. These 64-bit-only configurations are for developer use only.

| Device | Download Link | SHA-256 Checksum |
|---|---|---|
| Pixel 4a (5G) | bramble_beta_64-upb5.230623.006-factory-7e6731fa.zip | `7e6731fab811ae389f5ff882d5c5a2b8b942b8363b22bbcc038b39d7c539e60a` |
| Pixel 5 | redfin_beta_64-upb5.230623.006-factory-c4da6a19.zip | `c4da6a19086a02f2cd2fa7a4054e870916954b8e5a61e9a07ee942c537e4b45a` |
| Pixel 6 | oriole_beta_64-upb5.230623.006-factory-98943384.zip | `98943384284cbc7323b8867d84c36151757f67ae7633012fb69cb5d6bec2b554` |
| Pixel 6 Pro | raven_beta_64-upb5.230623.006-factory-67ec40be.zip | `67ec40be5bd05a40fa5dabc1ce6795aae75d1904193d52e2da00425ed7cb895b` |

###### 64-bit-only factory images for Android 13 (QPR3 Beta 3.2)

These images provide a strict 64-bit-only environment for testing 64-bit app
compatibility. These 64-bit-only configurations are for developer use only.

| Device | Download Link | SHA-256 Checksum |
|---|---|---|
| Pixel 4a (5G) | bramble_64-t3b3.230413.009-factory-b4be4092.zip | `b4be40924f62c3c2b3ed20a9f7fa4303aa9c39649d778eb96f86c867fe3ae59a` |
| Pixel 5 | redfin_64-t3b3.230413.009-factory-6e5e027a.zip | `6e5e027a4f64f9f786db9bb69d50d1a551c3f6aad893ae450e1f8279ea1b761a` |
| Pixel 6 | oriole_64-t3b3.230413.009-factory-becb9b81.zip | `becb9b81a5bddad67a4ac32d30a50dcb372b9d083cb7c046e5180510e479a0b8` |
| Pixel 6 Pro | raven_64-t3b3.230413.009-factory-b0ef544e.zip | `b0ef544ed2312ac44dc827f24999281b147c11d76356c2d06b2c57a191c60480` |

##### Return to a public build

You can either use the Android Flash Tool to
[flash the factory image](https://flash.android.com/back-to-public), or obtain a factory spec system
image from the [Factory Images for Nexus and Pixel Devices](https://developers.google.com/android/images)
page and then manually flash it to the device.
| **Warning:** Going back to a public build from a preview build (Developer Preview or Beta) requires a full device reset that removes all user data on the device. Make sure to [back up your data first](https://support.google.com/pixelphone/answer/7179901).

#### Android Emulator

Starting in Android 12 (API level 31), Android Emulator system images are 64-bit
only. [Create an Android Virtual Device (AVD)](https://developer.android.com/studio/run/managing-avds#createavd) using a system
image with Android 12 (API level 31) or higher to get a strict 64-bit-only
environment for app testing.

### Other device options

If you don't have one of these devices or can't use the Android Emulator, your
next best option is to use a device that is 64-bit capable, such as a Google
Pixel or other recent flagship devices from other device manufacturers.

### Install and test your app

The easiest way to test your APK is to install the app using Android Debug
Bridge (adb). In most cases, you can supply `--abi` as a parameter to indicate
which libraries to install to the device. This installs the app with only the
64-bit libraries on the device.  

    :: Command Line
    # A successful install:
    > adb install --abi armeabi-v7a YOUR_APK_FILE.apk
    Success

    # If your APK does not have the 64-bit libraries:
    > adb install --abi arm64-v8a YOUR_APK_FILE.apk
    adb: failed to install YOUR_APK_FILE.apk: Failure [INSTALL_FAILED_NO_MATCHING_ABIS: Failed to extract native libraries, res=-113]

    # If your device does not support 64-bit, an emulator, for example:
    > adb install --abi arm64-v8a YOUR_APK_FILE.apk
    ABI arm64-v8a not supported on this device

Once you have installed successfully, test your app like you normally would to
ensure the quality is the same as the 32-bit version.

### Check for known compatibility issues

As you test, check your app for the following issues that affect apps when
running on 64-bit devices. Even if your app doesn't depend on the affected
libraries directly, third-party libraries and SDKs in your app's dependencies
might.

#### SoLoader

If you are using the native code loader SDK
[SoLoader](https://github.com/facebook/SoLoader), update to v0.10.4 or higher. If your
app uses SDKs that depend on SoLoader, make sure to also update to the latest
stable version of the affected SDKs.

SoLoader v0.9.0 and lower assume that system libraries are present in
`/vendor/lib:/system/lib`. This bug is not observable in devices like the Pixel
7 where the path exists, but this assumption causes crashes in devices that only
have system libraries in `/vendor/lib64:/system/lib64`.

For more information on fixing this and other issues caused by SoLoader, see the
[corresponding answer in the Google Help Center](https://support.google.com/faqs/answer/12576726).

#### OpenSSL

If you are using the OpenSSL library, update to OpenSSL 1.1.1i or higher. If
your app uses SDKs that provide communication using HTTPS, or other SDKs that
depend on OpenSSL, make sure to also update to the latest version of the SDK
that uses a newer OpenSSL version. Reach out to the SDK provider if one is not
available.

[ARMv8.3 PAC](https://developer.arm.com/documentation/102433/0100/Return-oriented-programming) enables hardware-assisted control
flow integrity by authenticating pointers at runtime. Earlier versions of
OpenSSL use these capabilities incorrectly, causing runtime crashes in all
devices with processors based on ARMv8.3a and above.

For more information on fixing this and other issues caused by OpenSSL, see the
[corresponding answer in the Google Help Center](https://support.google.com/faqs/answer/12576638).

#### BTI

ARMv8.5 and higher use Branch Target Instructions (BTIs) to help protect against
[JOP attacks](https://developer.arm.com/documentation/102433/0100/Jump-oriented-programming). Earlier versions of obfuscation
SDKs that branch into random offsets of libraries built with BTI can cause apps
to crash. Since the instructions are encoded as
[HINTs](https://developer.arm.com/documentation/ddi0602/2021-12/Base-Instructions/HINT--Hint-instruction-), this bug is not observable in devices
that don't support BTI.

## Publish

When you feel like your app is ready, publish as normal. As always, continue to
follow the best practices for deploying your app. We recommend taking advantage
of [closed testing tracks](https://support.google.com/googleplay/android-developer/answer/3131213) to rollout to a limited number of
users to ensure the quality of your app is consistent.

As when rolling out an major update, make sure you have thoroughly tested on
64-bit-capable devices before publishing to a larger audience.  

## Download Android 14 factory system image (64-bit-only)

Before downloading, you must agree to the following terms and conditions.  

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.  
I have read and agree with the above terms and conditions  
Download Android 14 factory system image (64-bit-only) [Download Android 14 factory system image (64-bit-only)](https://dl.google.com/developers/android/udc/images/factory/bramble_beta_64-upb5.230623.006-factory-7e6731fa.zip)

*bramble_beta_64-upb5.230623.006-factory-7e6731fa.zip*  

## Download Android 14 factory system image (64-bit-only)

Before downloading, you must agree to the following terms and conditions.  

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.  
I have read and agree with the above terms and conditions  
Download Android 14 factory system image (64-bit-only) [Download Android 14 factory system image (64-bit-only)](https://dl.google.com/developers/android/udc/images/factory/redfin_beta_64-upb5.230623.006-factory-c4da6a19.zip)

*redfin_beta_64-upb5.230623.006-factory-c4da6a19.zip*  

## Download Android 14 factory system image (64-bit-only)

Before downloading, you must agree to the following terms and conditions.  

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.  
I have read and agree with the above terms and conditions  
Download Android 14 factory system image (64-bit-only) [Download Android 14 factory system image (64-bit-only)](https://dl.google.com/developers/android/udc/images/factory/oriole_beta_64-upb5.230623.006-factory-98943384.zip)

*oriole_beta_64-upb5.230623.006-factory-98943384.zip*  

## Download Android 14 factory system image (64-bit-only)

Before downloading, you must agree to the following terms and conditions.  

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.  
I have read and agree with the above terms and conditions  
Download Android 14 factory system image (64-bit-only) [Download Android 14 factory system image (64-bit-only)](https://dl.google.com/developers/android/udc/images/factory/raven_beta_64-upb5.230623.006-factory-67ec40be.zip)

*raven_beta_64-upb5.230623.006-factory-67ec40be.zip*  

## Download Android 13 factory system image (64-bit-only)

Before downloading, you must agree to the following terms and conditions.  

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.  
I have read and agree with the above terms and conditions  
Download Android 13 factory system image (64-bit-only) [Download Android 13 factory system image (64-bit-only)](https://dl.google.com/developers/android/tm/images/factory/bramble_64-t3b3.230413.009-factory-b4be4092.zip)

*bramble_64-t3b3.230413.009-factory-b4be4092.zip*  

## Download Android 13 factory system image (64-bit-only)

Before downloading, you must agree to the following terms and conditions.  

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.  
I have read and agree with the above terms and conditions  
Download Android 13 factory system image (64-bit-only) [Download Android 13 factory system image (64-bit-only)](https://dl.google.com/developers/android/tm/images/factory/redfin_64-t3b3.230413.009-factory-6e5e027a.zip)

*redfin_64-t3b3.230413.009-factory-6e5e027a.zip*  

## Download Android 13 factory system image (64-bit-only)

Before downloading, you must agree to the following terms and conditions.  

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.  
I have read and agree with the above terms and conditions  
Download Android 13 factory system image (64-bit-only) [Download Android 13 factory system image (64-bit-only)](https://dl.google.com/developers/android/tm/images/factory/oriole_64-t3b3.230413.009-factory-becb9b81.zip)

*oriole_64-t3b3.230413.009-factory-becb9b81.zip*  

## Download Android 13 factory system image (64-bit-only)

Before downloading, you must agree to the following terms and conditions.  

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.  
I have read and agree with the above terms and conditions  
Download Android 13 factory system image (64-bit-only) [Download Android 13 factory system image (64-bit-only)](https://dl.google.com/developers/android/tm/images/factory/raven_64-t3b3.230413.009-factory-b0ef544e.zip)

*raven_64-t3b3.230413.009-factory-b0ef544e.zip*