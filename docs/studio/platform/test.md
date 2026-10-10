---
title: https://developer.android.com/studio/platform/test
url: https://developer.android.com/studio/platform/test
source: md.txt
---

Android Studio for Platform (ASfP) integrates with `atest` and Soong test
modules so you can run and debug platform tests on your Linux host machine,
connected device, or Cuttlefish virtual device from the IDE.

## Prerequisites

- Open an ASfP project configured with your AOSP checkout and `lunch` target.
- For device tests, connect a physical device or launch a Cuttlefish virtual device running a matching build.

## Run and debug tests

You can launch platform tests and debug sessions from several places in ASfP:

- **`Android.bp` test targets** : Open an `Android.bp` file and click **Run** in the gutter next to any test module (`*_test` or `*_test_host`):
  - **Run** : Available for all Soong test module types (`android_test`, `java_test_host`, `cc_test`, `rust_test`, `python_test`, `sh_test`, and `android_robolectric_test`).
  - **Debug** : Available for `android_test` modules (attached with the Java debugger using `atest --wait-for-debugger`) and C++ or Rust test modules (`cc_test`, `cc_test_host`, `rust_test`, and `rust_test_host`, launched under ASfP's built-in LLDB debugger).
- **Source file gutter icons** : Click **Run** next to a test class or `@Test` method in your source code to run or debug that specific test.
- **Right-click context menu** : Right-click a test file, class, method, or `Android.bp` module and select **Run** or **Debug**.
- **Built-in Agent (AI in Android Studio)** : In the **Agent** tool window, the Built-in Agent can run `atest` targets to verify changes after editing code.
- **Integrated terminal** : Open **View \> Tool Windows \> Terminal** to run `atest` commands directly.

## Smart test configuration and debugging

When you launch a test from the gutter or context menu, ASfP creates and
configures a **Soong Test** run configuration using your `Android.bp` module
graph.

### Debug `android_test` Java and Kotlin targets

Click the gutter icon next to an `android_test` module in `Android.bp`, or next
to a Java or Kotlin JUnit class or `@Test` method, and then select **Debug
'\<TestName\>'** . From a source file gutter, ASfP picks the nearest enclosing
`android_test` module whose `srcs` include the file and names the configuration
`<module>`, `<module>:<SimpleClass>`, or `<module>:<SimpleClass>#<method>`.

ASfP runs `atest` with `--wait-for-debugger`, reads the target `package`
attribute from the module's `AndroidManifest.xml`, waits for that process on the
connected device, and attaches the Java debugger.

![Debugging an android_test method from the editor gutter](https://developer.android.com/static/studio/platform/images/asfp-test-debug-popup.png)

### Debug `cc_test` and `rust_test` targets under LLDB

To debug a C++ or Rust test module (`cc_test`, `cc_test_host`, `rust_test`, or
`rust_test_host`), click the `Android.bp` gutter icon and select **Debug
'\<TestName\>'** . ASfP launches the compiled test binary under its built-in LLDB
debugger instead of running it through `atest`.

### Configure the Soong Test run configuration

Open **Run \> Edit Configurations** and select a **Soong Test** configuration to
customize how tests build, deploy, and launch:

- **Module auto-completion and `Android.bp` navigation** : The **Module** field auto-completes from indexed Soong test modules in your project. Click **Go
  to Android.bp** next to the field to jump to the module's declaration in `Android.bp`.
- **Run on: Device or Host (including `host_supported: true`)** : ASfP evaluates the module rule and its transitive `defaults` chain (`host_supported`, `device_supported`, `enabled`, `target.android.enabled`, and `target.host.enabled`):
  - **Dual-target tests (`cc_test` and `rust_test` with
    `host_supported: true`)** : Both **Device** and **Host** radio buttons are available (defaulting to **Device** ). **Device** and **Host** each maintain their own independent LLDB debugger template. Switching **Run
    on** between **Device** and **Host** swaps between the remote device `lldb-server` configuration and the local host binary configuration while preserving customizations made on each target.
  - **Single-target tests** : If a C++ or Rust test only builds for one environment (such as a device-only `cc_test` or a host-only `cc_test_host` or `rust_test_host`), ASfP selects the supported target and disables the unsupported radio button with an explanatory tooltip: "`<module> (<ruleType>) doesn't build for the host or device.`"
- **Before launch tasks (Build Native Test Module and Deploy with atest)** : Every **Soong Test** configuration includes two **Before launch** tasks by default:
  - **Build Native Test Module** : Builds `<module>-target` (for **Device** ) or `<module>-host` (for **Host**) before starting LLDB.
  - **Deploy with atest** : When debugging on **Device** , runs `atest
    <module> --collect-tests-only --disable-teardown -it -s <serial> --
    --abi <abi>` so Tradefed pushes test dependencies and executes target preparers before LLDB launches the binary. Hold the pointer over the **Deploy with atest** chip to preview the exact `atest` command. For faster iteration once dependencies are already on the device, remove **Deploy with atest** so ASfP pushes only the test binary directly. When you select **Run on: Host** , ASfP automatically skips **Deploy with
    atest**.
- **Modify options and Debugger (LLDB options cards)** : Use **Modify options** to add optional configuration fields:
  - **Program arguments** (*Operating System* , C++ and Rust tests only): Extra arguments passed directly to the `cc_test` or `rust_test` binary after the `--gtest_filter` or `libtest` filter when debugging.
  - **atest arguments** (*Test* ): Extra flags passed to `atest` when running the test or when preparing a device with **Deploy with atest**.
  - **Debugger** (*C++ and Rust tests only* ): Shown when **Module** is a `cc_test*` or `rust_test*` target. Toggle **LLDB options** cards (such as *Stop on entry* , *Cache symbols across sessions* , *Load symbols on
    demand* , or *With Rust visualizers* for Rust tests), click **Reset to
    defaults** to reset the active **Device** or **Host** template, or add **Symbol directories** , **Init, Pre-run, Post-run, or Exit commands** , and **Launch JSON** (**DAP Settings** ) from **Modify options \>
    Debugger**.

![Soong Test run configuration showing Before launch tasks, Device or Host targets, and LLDB options](https://developer.android.com/static/studio/platform/images/asfp-soong-test-config.png)

## View test results

Test execution progress, pass or fail status, stack traces, and device logs
appear in real time inside the **Run** or **Debug** tool window in ASfP.

## Tips for testing

- **Run targeted tests**: Test individual methods from the editor gutter without running an entire test suite.
- **Use Cuttlefish snapshots**: When running device tests on Cuttlefish virtual devices, use snapshots to restore a clean device state between runs.
- **Inspect Soong build logs** : If a test fails to compile before running, check the **Soong** tool window for compiler diagnostics.