---
title: Debug platform code  |  Android Studio for Platform  |  Android Developers
url: https://developer.android.com/studio/platform/debug
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Android Studio for Platform](https://developer.android.com/studio/platform)
* [Getting started](https://developer.android.com/studio/platform/intro)

# Debug platform code Stay organized with collections Save and categorize content based on your preferences.




Android Studio for Platform (ASfP) provides a powerful debugger that lets you:

* Select a device to debug on.
* Set breakpoints in your Java, Kotlin, C/C++, and Rust code.
* Examine variables and evaluate expressions at runtime.

Before you use the debugger, you must flash your build to a device or emulator.

## App process (Java/Kotlin) debugging

To debug a Java or Kotlin application process:

1. Set breakpoints in your Java or Kotlin code within ASfP.
2. Select **Run > Attach Debugger to Android Process** from the menu.
3. In the **Choose Process** dialog, make sure the **Debug type** is set to
   **Java Only**.
4. Select your device from the list.
5. Choose the specific application process you want to debug.
6. Click **OK**.
7. Interact with the application on your device to hit the breakpoints.

## System process (C/C++) debugging

To debug a system process written in C or C++:

1. Verify that you have only one device or emulator running.
2. Open a terminal and run `adb root` from your AOSP checkout root: `bash
   adb root`

1. Set breakpoints in your C/C++ code within ASfP.
2. Select **Run > Attach Debugger to Android Process** from the menu.
3. In the **Choose Process** dialog, change the **Debug type** to **Native
   Only** or **Dual (Java + Native)**.
4. Check the **Show all processes** box to see system processes.
5. Select your device from the list.
6. Choose the specific system process you want to debug (such as
   `surfaceflinger` or `system_server`).
7. Click **OK**.
8. Interact with the device to hit your breakpoints.

## Rust debugging

ASfP supports Rust debugging using the Debug Adapter Protocol (DAP) with LLDB.
This section outlines how to set up CodeLLDB as a Debug Adapter Server and debug
Rust code on the host and on an Android device.

### Set up CodeLLDB as a Debug Adapter Server

1. Create a new **Debug Adapter Protocol** Run/Debug configuration:

   1. Select **Run > Edit Configurations** from the menu.
   2. Click the **+** button.
   3. Select **Debug Adapter Protocol**.
2. In the server tab, click **create a new server**.
3. In the newly opened dialog, click **Choose template** and select
   **CodeLLDB** from the list.
4. After selecting the CodeLLDB template, the new server is added with a
   predefined configuration.

   1. Enable verbose tracing by selecting **Verbose** in the **Trace**
      dropdown.
   2. Add an environment variable that specifies the path to the `lldb-server` in
      your Android source prebuilts:

   ```
       LLDB_DEBUGSERVER_PATH=REPO_ROOT/prebuilts/clang/host/linux-x86/CLANG_VERSION/runtimes_ndk_cxx/x86_64/lldb-server
       ```

   Replace `REPO_ROOT` with the absolute path to your Android source checkout.
   To find `CLANG_VERSION`, run the `get_clang_version.py` script from the root of
   your Android source tree:

   ```bash
       ./build/soong/scripts/get_clang_version.py
   ```

   1. **Do not** alter the `<<insert base directory>>` section.

### Debug Rust binaries on the host

1. Open the **Configuration** tab in your Debug Adapter Protocol Run/Debug
   configuration.
2. Select **Launch** as the **Debug Mode**.
3. Update the **Working directory** and select the **Binary file** you want to
   debug.
4. Click **OK** to save the configuration.
5. Start the debugging session by clicking the **Debug** icon next to the
   configuration.

The first time you run this, CodeLLDB downloads. You should see DAP
traces in the console. Breakpoints set in your Rust code should be hit as
expected.

### Debug Rust binaries on an Android device (Attach mode)

1. **Find the PID:** Identify the Process ID (PID) of the application you want
   to debug on the Android device.
2. **Start lldb-server on the device:** From the root of your Android source
   tree checkout, run the `lldbclient.py` script, replacing `<PID>` with the
   process ID:

   ```
   lldbclient.py --setup-forwarding vscode-lldb -p <PID>
   ```

   This script pushes the correct `lldb-server` to the device, starts it, sets
   up port forwarding (host port 5039 to device), and outputs the DAP JSON
   configuration needed for the next steps. Keep this terminal open.
3. **Start the CodeLLDB Debug Adapter on the host:**

   * Navigate to the CodeLLDB extension directory (default:
     `~/.lsp4ij/dap/codelldb/extension/adapter`).
   * Set the required environment variables and start the adapter server, replacing
     `REPO_ROOT` and `CLANG_VERSION` as determined in the server setup:

   ```
       # Sets PYTHONHOME env variable
       export PYTHONHOME=REPO_ROOT/prebuilts/clang/host/linux-x86/CLANG_VERSION/python3

       # Tell the dynamic linker where to find python libs
       export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:REPO_ROOT/prebuilts/clang/host/linux-x86/CLANG_VERSION/python3/lib

       # Starts the CodeLLDB Debugger Adapter server on port 1234
       ./codelldb --liblldb REPO_ROOT/prebuilts/clang/host/linux-x86/CLANG_VERSION/lib/liblldb.so --port 1234
   ```
4. **Configure the ASfP DAP Client:**

   1. Go back to your Debug Adapter Protocol Run/Debug configuration in ASfP.
   2. Select the **Configuration** tab.
   3. Set **Debug Mode** to **Attach**.
   4. Set **Address** to `localhost`.
   5. Set **Port** to `1234`.
   6. Paste the JSON output from the `lldbclient.py` command (Step 2) into the
      **DAP parameters (JSON)** field.
5. Click **Debug** to start the debugging session.

### Troubleshooting

* If you see the error `error: Connection shut down by remote side while
  waiting for reply to initial handshake packet`, terminate the current debug
  session, and restart the `lldb-server` on the device and the CodeLLDB
  adapter on the host.