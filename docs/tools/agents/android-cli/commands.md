---
title: https://developer.android.com/tools/agents/android-cli/commands
url: https://developer.android.com/tools/agents/android-cli/commands
source: md.txt
---

The `android` command-line tool provides commands for scaffolding projects,
running apps, managing virtual devices, inspecting UI layouts, and integrating
with Android Studio.

## Summary of commands

| Command | Description |
|---|---|
| [`analyze`](https://developer.android.com/tools/agents/android-cli/commands/analyze) | Analyzes the file(s) (AAB, APK, JAR, AAR) at the given location(s) and reports back all available details. |
| [`auth`](https://developer.android.com/tools/agents/android-cli/commands/auth) | Authentication commands. Log in to and out of Google services for Android CLI. |
| [`build`](https://developer.android.com/tools/agents/android-cli/commands/build) | Build android artifacts. |
| [`completion`](https://developer.android.com/tools/agents/android-cli/commands/completion) | Installs shell autocomplete configuration for Android CLI in the current user profile. |
| [`create`](https://developer.android.com/tools/agents/android-cli/commands/create) | Creates a new Android project from available templates. You can specify the project name, output directory, `minSdk` value, and dry-run execution. |
| [`describe`](https://developer.android.com/tools/agents/android-cli/commands/describe) | Analyzes an Android project to generate descriptive metadata. This command identifies and outputs the paths to JSON files that detail the project's structure, including build targets and their corresponding output artifact locations (such as APKs). This information enables other tools and commands to locate build artifacts efficiently. |
| [`device`](https://developer.android.com/tools/agents/android-cli/commands/device) | Manage Android devices. Mirror connected devices or emulators in a desktop window and manage remote physical device reservations. |
| [`docs`](https://developer.android.com/tools/agents/android-cli/commands/docs) | Searches and fetches developer documentation from the official Android Knowledge Base. |
| [`emulator`](https://developer.android.com/tools/agents/android-cli/commands/emulator) | Manages Android Virtual Devices (AVDs). Includes commands to start, stop, list, and view details about emulators. |
| [`help`](https://developer.android.com/tools/agents/android-cli/commands/help) | Shows the help information for a specified command. |
| [`info`](https://developer.android.com/tools/agents/android-cli/commands/info) | Prints environment information including SDK location and configuration variables. |
| [`init`](https://developer.android.com/tools/agents/android-cli/commands/init) | Initializes the environment for Android CLI. Sets up required configurations, directories, and default skills. |
| [`input`](https://developer.android.com/tools/agents/android-cli/commands/input) | Interact with Android apps by performing gestures and key events on UI elements. |
| [`install`](https://developer.android.com/tools/agents/android-cli/commands/install) | Installs an Android app (one or more APKs) on a connected device or emulator without activating any components, using incremental optimizations for faster deployment than `adb`. |
| [`layout`](https://developer.android.com/tools/agents/android-cli/commands/layout) | Returns the layout tree of an app. |
| [`preview`](https://developer.android.com/tools/agents/android-cli/commands/preview) | Renders Jetpack Compose @Preview functions to PNG images and optionally exports component tree JSON files. Runs without a device or an IDE. |
| [`profiler`](https://developer.android.com/tools/agents/android-cli/commands/profiler) | Profiles Android apps, games, and devices. |
| [`run`](https://developer.android.com/tools/agents/android-cli/commands/run) | Deploys and launches an Android app on a connected device or emulator. |
| [`screen`](https://developer.android.com/tools/agents/android-cli/commands/screen) | Captures and inspects the screen of a connected Android device or emulator. |
| [`sdk`](https://developer.android.com/tools/agents/android-cli/commands/sdk) | Manages the Android SDK installation. Includes commands to install, update, remove, and list available and installed SDK packages. |
| [`signals`](https://developer.android.com/tools/agents/android-cli/commands/signals) | Queries app stability and field telemetry from Crashlytics. |
| [`skills`](https://developer.android.com/tools/agents/android-cli/commands/skills) | Manages Android CLI skills. Includes commands to install, remove, list, and search for skills by keyword. |
| [`studio`](https://developer.android.com/tools/agents/android-cli/commands/studio) | Connects Android CLI to a running Android Studio instance to analyze files, find declarations and usages, render Compose previews, and look up library versions. |
| [`update`](https://developer.android.com/tools/agents/android-cli/commands/update) | Updates Android CLI to the latest version. |