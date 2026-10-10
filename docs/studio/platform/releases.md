---
title: https://developer.android.com/studio/platform/releases
url: https://developer.android.com/studio/platform/releases
source: md.txt
---

Android Studio for Platform (ASfP) is the official IDE for Android platform
development. This page summarizes the latest features, platform-specific
enhancements, and quality improvements available in ASfP.

## 2026 platform feature drops (Rabbit \| 2026.2 and Panda 2 \| 2025.3.2)

Built on the **IntelliJ 2026.2** base platform, recent releases of ASfP deliver
major improvements to project setup and startup reliability, Soong build
integration, AI agent capabilities, Cuttlefish virtual device management,
C, C++, Rust, and hybrid debugging, and platform testing.

### Project setup, templates, and sync performance

- **Workspace Model project architecture**: Project construction has been migrated to the IntelliJ Workspace Model APIs, streamlining initial project setup and improving IDE stability across large AOSP source trees.
- **Instant startup with project model snapshots**: ASfP now caches and restores your project model from snapshots on startup, eliminating redundant initial indexing delays when reopening large AOSP workspaces.
- **Shareable project templates (import and export)** :
  - **Import from template** : Bootstrap a new AOSP project in the setup wizard by selecting **Import from template** and pointing to a shared `.asfp-project` YAML file.
  - **Export to template** : Share your project configuration with teammates by right-clicking the `.asfp-project` editor tab (or from the **ASfP \>
    Project** menu) and selecting **Export to Template**.
- **Enhanced setup wizard options** : Configure custom build **Environment
  Variables** and enable **Soong Partial Compile** (`SOONG_PARTIAL_COMPILE`) directly during project creation.
- **Flexible sync modes** :
  - **Partial Sync**: Sync specific modules or directories without running a full repository sync.
  - **No-Build Sync**: Refresh IDE project structure and module roots quickly without triggering a Soong build.
  - **Sync and Full Build**: Trigger a combined project sync and full Soong build in a single action.
- **Optimized search scopes and symlink support** : Contents inside the `out/` directory and generated `gen` IMLs are automatically excluded from project search scopes to keep file and symbol lookups fast and noise-free. ASfP also supports symlinked source roots across AOSP repositories.

### In-editor `Android.bp` build, deploy, and editor intelligence

- **Build, run, and debug gutter icons in `Android.bp`** : Every named module in `Android.bp` includes a **Build** gutter icon next to `name:`, while test modules (`*_test` and `*_test_host`) and `android_app` modules include a **Run** gutter icon to run or debug targets directly from the editor.
- **Contextual deploy and flash run configurations** : Create and launch **Soong Deploy** run configurations from deployable targets in `Android.bp` files, supporting deployment through `adb`, custom shell scripts, `adevice`, or `flashall` with pre-run Soong build hooks.
- **Open Corresponding Android.bp File and editor intelligence** : Right-click any source file or directory and select **Open Corresponding Android.bp
  File** to jump to its module declaration (resolving `defaults` chains, globs, and symlinks). Inside `Android.bp`, **Ctrl+click** module or `srcs` references, view clickable **`N Usages`** inlay hints, and hold the pointer over properties (including scoped `target.*`, `arch.*`, and `multilib.*` properties) for inline Soong documentation.
- **Dedicated Soong tool window** : Monitor Soong sync and build progress with task status indicators, trigger build actions, and run Soong commands from the **Soong** tool window.

### Cuttlefish virtual device management and multi-screen mirroring

- **Multidevice setup in Device Manager** : Create and manage multidevice Cuttlefish virtual device setups directly in **Device Manager** using your local AOSP checkout.
- **Multi-screen display mirroring in the Cuttlefish tool window** : Use built-in Cuttlefish multi-screen display mirroring in the dedicated **Cuttlefish** tool window---built for multi-display Android Automotive OS (AAOS) and Software-Defined Vehicle (SDV) development.

### AI in Android Studio and Built-in Agent for platform development

- **Built-in Agent with Soong build and test tools** : **AI in Android Studio** integrates platform-specific Soong build and `atest` execution tools into the **Built-in Agent** , allowing the agent to plan multi-step edits, compile Soong targets, and run `atest` platform tests with structured results inline.
- **Enterprise and BYOM support** : Access **AI in Android Studio** using built-in Gemini models, Gemini Code Assist, Gemini Enterprise licenses, or connect custom model endpoints using **Bring Your Own Model (BYOM)** with your own API keys.

### Platform debugging (Attach tab in the Debug tool window and LLDB)

- **Pinned Attach tab (Run \> Attach to Android Process)** :
  - **Loaded shared libraries (Libraries), Build ID, and symbols** : Inspect loaded `.so` libraries and 8-character ELF **Build IDs** before attaching. ASfP matches each Build ID against `out/target/product/<device>/symbols` (`symbols/.build-id` index), displaying a checkmark icon when verified (hold the pointer over a verified row to view the resolved `.debug` path) or a warning icon if symbols are missing.
  - **Java, C++, and Rust attach** : Select **Java debugger** , **Native
    debugger** , or both to open linked `<process> (<pid>)` and `<process>
    (<pid>)-jdwp` debug tabs. Selecting a C++ or Rust service hides **Java
    debugger** and displays **Java debugging unavailable, not a Java
    process.**
  - **One-click Root Device and Enable JDWP** : Filter with **Show system
    processes** , click **Root Device** to run `adb root` (**Device is
    rooted** ), or click **Enable JDWP** to set `persist.debug.dalvik.vm.jdwp.enabled=1` and reboot `userdebug` devices.
- **LLDB debugger enhancements, Rust visualizers, and ART signal
  pass-through** :
  - Built-in `lldb-dap` sessions support conditional breakpoints, C++ and Rust exception breakpoints, inline variable values in the editor, **Drop
    Frame** , smart **Step Into** , and automatic Rust pretty-printers (`String`, `Vec`, `HashMap`, `Option`) from AOSP prebuilts.
  - Attaching LLDB to ART and JNI processes automatically passes through internal ART `SIGSEGV` and `SIGBUS` null-check or GC signals without spurious stops.
  - `rust-analyzer` is auto-detected from `prebuilts/rust-toolchain/linux-x86/stable/rust-analyzer` (with fallback to `prebuilts/rust/linux-x86/stable/rust-analyzer`), and spurious `'proc-macro' not found` notifications on generated `out/soong/.intermediates` files are suppressed.

### Platform testing and `cc_test` and `rust_test` debugging

- **Debug `android_test`, `cc_test`, and `rust_test` targets** : Launch debug sessions from `Android.bp` or test method gutter icons:
  - `android_test` modules launch using `atest --wait-for-debugger` and attach the Java debugger.
  - `cc_test`, `cc_test_host`, `rust_test`, and `rust_test_host` modules launch directly under built-in LLDB using **Build Native Test Module** and **Deploy with atest** (`atest --collect-tests-only
    --disable-teardown`) before-launch tasks.
- **Dual-target `host_supported: true` and per-machine LLDB templates** : For `cc_test` and `rust_test` modules with `host_supported: true`, both **Run
  on: Device** and **Host** radio buttons are enabled in **Soong Test** configurations with independent per-target LLDB settings cards, **Program
  arguments** , **atest arguments** , and **Launch JSON** (**DAP Settings**).

### In-IDE updates and platform quality

- **Automatic in-IDE update notifications** : Starting with **ASfP 2026.2.2
  Canary 1** , ASfP automatically checks for new releases in the background and notifies you in the IDE through the **Android Studio and Plugin Updates** dialog, with a **Download** button for the latest `.deb` package and terminal installation instructions. Check for updates at any time using **Help \> Check for Updates**.
- **Persistent `-current-linux.deb` channel links** : For automated scripts and command-line setups, the latest Stable and Canary packages are accessible at persistent URLs: `https://dl.google.com/android/asfp/asfp-current-linux.deb` (Stable) and `https://dl.google.com/android/asfp/asfp-canary-current-linux.deb` (Canary).
- **On-disk version mismatch detection** : ASfP detects when the underlying `.deb` installation on disk has been updated while the IDE is running and prompts you with a notification to restart cleanly.
- **Default AOSP copyright and commit inspections**: Includes a pre-configured default AOSP copyright header profile and commit message formatting inspections tailored for platform contributions.
- **Increased default memory allocation** : Default maximum heap size has been increased from 20 GB to **30 GB** to support large AOSP source trees.