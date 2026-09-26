---
title: https://developer.android.com/tools/agents/android-cli/commands/studio_version-lookup
url: https://developer.android.com/tools/agents/android-cli/commands/studio_version-lookup
source: md.txt
---

Looks up the latest available versions of Maven artifacts, Android versions, and SDK tools.

## Usage

    android studio version-lookup [-h] [--pid=PARAM] [--project=PARAM] <artifacts...>

## Options

- `-h,--help` - Shows the help message for the specified command.
- `--pid=PARAM` - The PID of the Android Studio instance to connect to.
- `--project=PARAM` - The name or path of the project open in Android Studio to query. Use [`android studio check`](https://developer.android.com/tools/agents/android-cli/commands/studio_check) to get the names of available projects.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Positional arguments

- `<artifacts...>` - A space-separated list of identifiers, one for each library or tool to look up. The reply is a formatted list detailing the current stable and preview versions for each identifier.

The identifiers can be one of the following:
- `groupId:artifactId` for Maven libraries, such as `androidx.window:window`
- `pluginId` for Gradle plugins, such as `com.android.application`
- `gradle`, for the Gradle build tool
- `studio`, for Android Studio
- `agp`, for Android Gradle plugin
- `ndk`, for the Android NDK
- `sdk`, for the Android SDK
- `emulator`, for the Android Emulator
- `adb`, for the Android Debug Bridge (ADB)
- `compose`, for the Compose BOM
- `kotlin`, for the Kotlin language and runtime
- `android`, for Android versions
- `platform-tools`, for Android SDK Platform-Tools
- `cmdline-tools`, for Android SDK Command-line Tools
- `build-tools`, for Android SDK Build-Tools

## Description

`android studio version-lookup` queries repositories such as Google Maven to look up the latest stable and preview versions of Maven libraries, Gradle plugins, Android platforms, and SDK tools.

Requires Android Studio Quail 2 or higher.

### Specify supported identifiers

You can query multiple space-separated identifiers in a single command:

- **Maven libraries** : Use `groupId:artifactId` notation (for example, `androidx.window:window` or `androidx.compose.ui:ui`).
- **Gradle plugins** : Use the plugin ID (for example, `com.android.application`).
- **Keywords** :
  - `gradle` (Gradle build tool)
  - `studio` (Android Studio)
  - `agp` (Android Gradle plugin)
  - `ndk` (Android NDK)
  - `sdk` (Android SDK)
  - `emulator` (Android Emulator)
  - `adb` (Android Debug Bridge)
  - `compose` (Jetpack Compose BOM)
  - `kotlin` (Kotlin runtime and compiler)
  - `android` (Android OS versions)
  - `platform-tools` (Android SDK Platform-Tools)
  - `cmdline-tools` (Android SDK Command-line Tools)
  - `build-tools` (Android SDK Build-Tools)

### Examples

Look up the latest versions of Compose UI, the Android app plugin, AGP, and Kotlin:

    android studio version-lookup \
      androidx.compose.ui:ui \
      com.android.application \
      agp \
      kotlin