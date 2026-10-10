---
title: https://developer.android.com/studio/platform/intro
url: https://developer.android.com/studio/platform/intro
source: md.txt
---

Android Studio for Platform (ASfP) is the official integrated development
environment (IDE) for Android platform development. Built on IntelliJ IDEA
2026.2, ASfP streamlines code navigation, building, debugging, and testing for
engineers working in the Android Open Source Project (AOSP).

## Why use ASfP?

ASfP addresses the specific scale and build requirements of platform development
beyond standard Android app projects. It integrates directly with large AOSP
source trees and the Soong build system to support multi-language platform
workflows.

## Key features

- **AOSP and Soong (`Android.bp`) integration** : Build Soong targets and run
  or debug `android_test`, `cc_test`, and `rust_test` modules from gutter
  icons inside `Android.bp` files, jump from any source file to its
  `Android.bp` module declaration (**Open Corresponding Android.bp File** ),
  and manage syncs with **Partial Sync** , **No-Build Sync** , and **Sync and
  Full Build** modes.

- **Project setup and shareable templates** : Scope your workspace using the
  `.asfp-project` YAML file, restore cached project model snapshots on startup
  with the IntelliJ Workspace Model, and share configurations across your
  team with **Import from template** and **Export to template** . For more
  information, see [Projects overview and Soong workflows](https://developer.android.com/studio/platform/projects).

- **Cuttlefish virtual device management and multi-screen mirroring** : Create
  and manage multidevice Cuttlefish virtual device setups in **Device
  Manager** using your local AOSP checkout, and use multi-screen display
  mirroring in the dedicated **Cuttlefish** tool window for Android Automotive
  OS (AAOS) and Software-Defined Vehicle (SDV) development.

- **AI in Android Studio and Built-in Agent with platform tools** : Use the
  **Built-in Agent** in [AI in Android Studio](https://developer.android.com/ai-in-android) to plan
  multi-step edits, build Soong targets, and run `atest` platform tests inside
  the IDE. It supports built-in Gemini models, Gemini Code Assist, Gemini
  Enterprise, and Bring Your Own Model (BYOM) endpoints.

- **Multi-language code editing** : Get code completion, cross-module
  navigation, refactoring, and real-time analysis for Kotlin, Java, C, C++,
  Rust, and `Android.bp` files.

- **Platform debugging (Attach tab and LLDB)** : Select **Run** \> **Attach to
  Android Process** to open the **Attach** tab in the **Debug** tool window.
  Inspect loaded shared libraries (`.so`), ELF **Build IDs** , and checkmark
  icons verifying local symbols under
  `out/target/product/<device>/symbols`, and then attach the **Java
  debugger** , **Native debugger** , or both. For more information, see
  [Debug platform code](https://developer.android.com/studio/platform/debug).

- **Integrated testing (`atest` and LLDB)** : Run and debug tests from source
  files or `Android.bp` test modules (`android_test`, `cc_test`,
  `cc_test_host`, `rust_test`, and `rust_test_host`). ASfP determines
  **Device** versus **Host** targets (including dual-target
  `host_supported: true` modules), runs Tradefed target preparation, and
  launches targets under the Java or built-in LLDB debugger. For more
  information, see [Test platform code with atest](https://developer.android.com/studio/platform/test).

- **Built-in Rust language support** : Develop Rust code in AOSP with automatic
  `rust-analyzer` integration and built-in LLDB debugging with Rust type
  visualizers. For more information, see [Rust support in ASfP](https://developer.android.com/studio/platform/projects/rust).

- **Automatic in-IDE updates** : Receive update notifications inside the IDE
  with direct `.deb` downloads and terminal installation commands whenever
  Stable or Canary releases are published.

## Get started

- [Install Android Studio for Platform](https://developer.android.com/studio/platform/install)
- [Create or import a project](https://developer.android.com/studio/platform/projects/create-project)
- [Read the release notes](https://developer.android.com/studio/platform/releases)