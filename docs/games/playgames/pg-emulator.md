---
title: https://developer.android.com/games/playgames/pg-emulator
url: https://developer.android.com/games/playgames/pg-emulator
source: md.txt
---

The [Google Play Games on PC Developer Emulator](https://developer.android.com/games/playgames/emulator) is a developer-focused emulator for
Google Play Games on PC. Unlike the player experience, you can install and
debug your own packages. You also can simulate various player configurations
such as the aspect ratio, mouse emulation, and graphics backend to help you
ensure that your game performs as expected across a variety of PC
configurations.

## Starting the Emulator

Once installed, you will have a "Google Play Games Developer Emulator" start
menu element and a desktop shortcut to launch the emulator. The emulator will
remain resident in your system tray when you close the window.

> [!NOTE]
> **Note:** you cannot run the Google Play Games on PC Developer Emulator and the consumer Google Play Games on PC at the same time. You must quit one from the system tray before launching the other.

### Sign in

You are asked to sign into your Google Account the first time you run the
emulator. Use the same login credentials you plan to use for development.

You can sign out by right clicking on the system tray icon, selecting *Developer
Options* , then clicking *Force sign out*. When you do so, the emulator
immediately restarts and asks you to sign in again.

> [!CAUTION]
> **Caution:** Your local device image, including any games you have installed, is erased when you sign out.

### Navigation

After launching, you will see a typical Android home screen. Left mouse
clicks are directly translated into finger taps as in mouse emulation mode.
Games sideloaded for development appear in the application list, which you can
get to by clicking and dragging up on the desktop (emulating an upwards swipe on
a phone or tablet).

In addition to mouse translation, the Google Play Games on PC Developer Emulator provides
keyboard shortcuts to improve navigation:

- ctrl + h: press the home button
- ctrl + b: press the back button
- F11 or alt + enter: toggle between fullscreen and windowed mode
- shift + tab: open the Google Play Games on PC overlay, including the current key mappings for the Input SDK

> [!NOTE]
> **Note:** ctrl + h and ctrl + b are provided for development purposes only. Don't rely on them in your shipping game.

## Installing a game

The Google Play Games on PC Developer Emulator uses the [Android Debug Bridge (adb)](https://developer.android.com/tools/adb) to
install packages.

### adb compatibility

Current versions of `adb` are compatible with the Google Play Games on PC Developer Emulator.
Additionally a compatible version is installed at `C:\Program
Files\Google\Play Games Developer Emulator\current\emulator` when you install
the emulator.

To follow these instructions, adb should be available in your `$PATH`. You can
verify that `adb` is configured correctly with the `adb devices` command

    adb devices
    List of devices attached
    localhost:6520  device

> [!NOTE]
> **Note:** If you prefer to not modify your `$PATH` variable, run your terminal from `C:\Program Files\Google\Play Games Developer Emulator\current\emulator`. Some shells require you to type `./adb` rather than `adb` depending when doing this.

### Install the game

- Launch `Google Play Games for PC Emulator`
- Type `adb devices` in your command prompt. You should see:

      adb devices
      List of devices attached
      localhost:6520 device

- Troubleshooting:

  - If you get an error, verify that you've followed the instructions in [Adb
    compatibility](https://developer.android.com/games/playgames/pg-emulator#adb-compatibility).
  - If you don't see a device, attempt to reconnect over port `6520`:

      adb connect localhost:6520

- Type `adb install path\to\your\game.apk` to install your game. If you've
  generated an Android App Bundle (aab), see the instructions for
  [bundletool](https://developer.android.com/tools/bundletool#deploy_with_bundletool) and use `bundletool install-apks` instead.

- Run your game by either:

  - Type `adb shell monkey -p your.package.name 1` to run your game, replacing `your.package.name` with your game's package name.
  - In the Google Play Games on PC Developer Emulator, click the icon to run your game. Just like on an Android phone, you have to "swipe up" on the home screen to see the list of installed games.

## Debugging a game

Use the [Android Debug Bridge (adb)](https://developer.android.com/tools/adb) to debug as you do for any other game.
The emulator appears as a device connected via `localhost:6520`.

`adb logcat` functions as expected, as do tools that help prettify or filter
logcat output -- including Android Studio.

In addition to `adb`, logs can be accessed in your
`%LOCALAPPDATA%\Google\Play Games Developer Emulator\Logs` directory. Most
useful here is `AndroidSerial.log` which represents everything `adb logcat`
would echo from the moment the emulator starts.

> [!NOTE]
> **Note:** `%LOCALAPPDATA%` typically expands to `C:\Users\<username>\AppData\Local`

## Developer settings

The Google Play Games on PC Developer Emulator focuses on developer efficiency rather
than end user experience. This means that you have unobstructed access to the
Android system, including using the standard Android launcher instead of the
Google Play Games on PC experience, and controls over features that are
otherwise automatically enabled and disabled for players.

### Testing mouse input

During development, the Google Play Games on PC Developer Emulator defaults to touch
emulation rather than giving you direct mouse input. You can enable direct mouse
input by right clicking the system tray icon, selecting **Developer Options** ,
and then **PC mode (KiwiMouse)**.

Google Play Games on PC has two mouse modes: an emulated mode that translates
mouse clicks into single taps and a passthrough "PC mode" that lets games handle
mouse actions natively and perform pointer capture. For details on mouse input
in Google Play Games on PC see [Setup mouse input](https://developer.android.com/games/playgames/input-mouse).

In the player client, emulation is disabled by adding this to your manifest:

    <manifest ...>
      <uses-feature
          android:name="android.hardware.type.pc"
          android:required="false" />
      ...
    </manifest>

This feature flag has no effect in the development environment.

### Testing aspect ratios

The developer emulator launches in a 16:9 aspect ratio -- unlike the player
client which derives its aspect ratio from the primary display. By right
clicking on the system tray icon, selecting **Developer Options** , and then any
option in the **Display Ratio** section, you can test how the game looks on
different player's screens.

The [preferred method](https://developer.android.com/games/playgames/graphics#dynamic-display) to configure your aspect ratio
is to use `android:minAspectRatio` and `android:maxAspectRatio`.

For example,
a portrait game would have a `9/16` or `0.5625` aspect ratio so you may want to
set a max aspect ratio of `1` to prevent your game from going wider than square:

    <activity android:maxAspectRatio="1">
     ...
    </activity>

Similarly, a landscape game would be `16/9` or roughly `1.778`, so you may want
to set a min aspect ratio of `1` to prevent it from going skinnier than square:

    <activity android:minAspectRatio="1">
     ...
    </activity>

> [!NOTE]
> **Note:** In practice games don't work well as they approach square aspect ratios. You should find a value that makes sense in your own testing across Android devices.

#### What to test

If your game only supports portrait modes in the manifest, you can select **9:16
(Portrait)** in the drop-down to see how it looks on players' PCs. Otherwise
verify that your game works at the widest and narrowest landscape ratios you
support in your manifest, remembering that **16:9 (Default)** (or
**9:16 (Portrait)** if your game is portrait only) is [required for
full certification](https://developer.android.com/games/playgames/graphics#aspect-ratios).

### Testing rendering backends

Google Play Games on PC uses Vulkan to render your games, which is common to
both Android and PC environments. A sandboxing layer is used to isolate the PC
and Android environments. Since many games still use OpenGL ES for rendering,
[ANGLE](https://github.com/google/angle) will convert OpenGL ES commands to Vulkan commands
compatible with the host PC.

Similarly, Google Play Games on PC maximizes game compatibility and minimizes
developer effort by automatically converting mobile-friendly texture formats
such as ETC1 and ETC2 to PC friendly formats at runtime. For the best results,
avoid this conversion by utilizing formats supported by PC GPUs, such as DXTC or
BPTC.

#### What to test

If your game is experiencing unexpected rendering artifacts, inspect your source
graphics and consider moving to a PC-friendly format. Pay close attention to
textures used for more advanced effects, as normal or cube map issues are often
harder to spot than issues with albeido.

ANGLE's conversion of your OpenGL ES commands to Vulkan will add some overhead. Validate you're
meeting your expected performance targets and consider switching to a Vulkan
based renderer.

### Profiling your PC game

Since the emulator uses the same technology as the consumer client, it's a
suitable environment for performance profiling.

[Perfetto](https://developer.android.com/tools/perfetto) is a tool for analyzing performance on Android. You can gather and
view a Perfetto trace using the following steps:

1. In a PowerShell prompt, start a trace using [`adb`](https://developer.android.com/games/playgames/pg-emulator#adb-compatibility)

       adb shell perfetto --time 10s gfx wm sched --out /data/misc/perfetto-traces/example.trace

   1. The `--time` flag specifies the duration of the trace to gather. In this example, the trace is 10 seconds.
   2. The arguments after the `--time` flag indicate which events are to be traced. In this example `gfx` indicates graphics, `wm` window management, and `sched` process scheduling information. These are common flags for profiling games and a [full reference](https://android.googlesource.com/platform/frameworks/native/+/refs/tags/android-q-preview-5/cmds/atrace/atrace.cpp#100) is available.
   3. The `--out` flag specifies the output file, which is pulled out of the emulator onto the host machine in the next step.
2. Pull the trace from your host

       adb pull /data/misc/perfetto-traces/example.trace $HOME/Downloads/example.trace

3. Open the trace in the Perfetto UI

   1. Open [ui.perfetto.dev](https://ui.perfetto.dev/).
   2. Select **Open trace file** from the upper left corner under **Navigation**.
   3. Open the `example.trace` file you downloaded in the previous step to your `Downloads/` directory.
4. Inspect the trace in the Perfetto UI. Some tips:

   1. Each process has its own row, which can be expanded to show all the threads in that process. If you're profiling a game, it's process is likely the first row.
   2. You can zoom in and out by holding <kbd>Control</kbd> and using the scroll wheel.
   3. When using the `sched` event, there is a row for each thread showing when that thread's state is running, runnable, sleeping, or blocked.
   4. When enabling an event like `gfx`, you are able to see the various graphics calls made by various threads. You can select individual "slices" to see how long they took, or you can drag along a row causing a "slices" section to open at the bottom and show you how long all the slices took in your selected time window.

#### Graphics Profiling

> [!CAUTION]
> **Caution:** Attaching Renderdoc only works in the Developer Emulator and is not officially supported.

It is possible to perform some graphics profiling with
[RenderDoc](https://renderdoc.org/).

> [!NOTE]
> **Note:** Renderdoc can only detect the output of the emulator, after instructions from your game have been translated from the guest to the host operating system.

1. [Set the environment variable](https://developer.android.com/games/playgames/pg-emulator#environment-variables) `ANDROID_EMU_RENDERDOC` to a non-empty string (such as `"1"`).
2. [Set the environment variable](https://developer.android.com/games/playgames/pg-emulator#environment-variables) `TMP` to
   `%USERPROFILE%\AppData\LocalLow`. This tells Renderdoc to place its log files
   somewhere reachable within the emulator sandbox.

   > [!NOTE]
   > **Note:** you may need to log out and back in at this point.

3. If you are using the [Vulkan](https://developer.android.com/games/playgames/pg-emulator#testing-rendering) backend. Select
   **Graphics Settings** \> **Vulkan Instance Implicit Layers** and ensure that
   **VKLAYER_RENDERDOC_Capture** is checked.

   > [!NOTE]
   > **Note:** Changes to **Graphics Settings** require a relaunch of the emulator to take effect.

4. Launch Google Play Games on PC Developer Emulator. A RenderDoc overlay is drawn at the
   top as long as support is enabled.

5. Launch RenderDoc anytime before or after Google Play Games on PC Developer Emulator
   launches.

6. Click **File** \> **Attach to Running Instance** and select **crosvm**.

##### Specify Environment Variables

In order for Renderdoc to work, you have to add or change environment variables
in Windows. You can change environment variables using the UI, PowerShell, or
cmd.exe.

###### Use the UI

- Press Win+R to open the run dialog.
- Type `sysdm.cpl` to open the **System Properties** window.
- Select the **Advanced** tab if it isn't already active.
- Click the **Environment Variables** button.

From here you can either click the **New** button to create a new environment
variable or select a variable and click the **Edit** button to edit it.

###### Use PowerShell

In a PowerShell window, type:

    $Env:VARIABLE_NAME=VALUE

Replace `VARIABLE_NAME` and `VALUE` with the values you wish to set. For
example, to set `ANDROID_EMU_RENDERDOC` to `"1"` type:

    $Env:ANDROID_EMU_RENDERDOC="1"

###### Use cmd.exe

In a cmd.exe window, type:

    set VARIABLE_NAME=VALUE

Replace `VARIABLE_NAME` and `VALUE` with the values you wish to set. For
example, to set `ANDROID_EMU_RENDERDOC` to `"1"` type:

    set ANDROID_EMU_RENDERDOC="1"

## Tips for Android 11 (API level 30) or higher

Google Play Games on PC is updated with the latest Android releases. Here are
some tips for working with the latest version of Android.

### Keep tools up to date

Android Studio installs a version of adb that is compatible with the developer
emulator; however, some game engines include an older version of adb. In that
case, after you install the developer emulator, you can find a compatible
version of `adb` at `C:\Program Files\Google\Play Games Developer
Emulator\current\emulator`.

If you launch one version of `adb`, it terminates the other. This means that
if your game engine automatically launches its own `adb` instance, you may have
to re-launch and reconnect the version of `adb` that comes with the developer
emulator whenever you deploy.

If you are using an Android App bundle, you must install the latest version of
[Bundletool](https://developer.android.com/tools/bundletool) from the [GitHub repository](https://github.com/google/bundletool/releases).

### Scoped Storage

Android 11 (API level 30) or higher includes [scoped storage](https://developer.android.com/training/data-storage#scoped-storage), which provides
better protection to app and user data on external storage. Besides making your
game compatible with [scoped storage requirements](https://developer.android.com/games/playgames/pc-compatibility#scoped-storage), you need to perform
extra steps to load [APK Expansion Files](https://developer.android.com/google/play/expansion-files) (obb) or asset data into the
Google Play Games on PC Developer Emulator. Follow these steps if you run into issues
accessing those files from your game:

1. Create a directory that your app can read.
2. Push your expansion files to the emulator.

    adb shell mkdir /sdcard/Android/obb/com.example.game
    adb push main.com.example.game.obb /sdcard/Android/obb/com.example.game

### Package Visibility

Because of the new [package visibility](https://developer.android.com/training/package-visibility) rules, apps that target Android 11
(API level 30) or higher are blocked from querying for information about the
other apps that are installed on a device. This means that your game is blocked
from accessing Play Services when sideloaded via `adb` instead of being
installed via the Play Store. To test your IAP with a sideloaded game,
you must add a query to the package "`com.android.vending`" in your
`AndroidManifest.xml` file as follows:

    <manifest>
        <queries>
            <package android:name="com.android.vending" />
        </queries>
    </manifest>

> [!NOTE]
> **Note:** You don't need to add this in the release version of your game distributed via the Play Store.

## Installing your game in the consumer client

You cannot install a game on the consumer client until it has been listed in the
Play Games Services catalog. After your game has a single release, you
can create an [internal test track](https://play.google.com/console/about/internal-testing/) validate future updates
before release.

The player client doesn't support the developer focused features of the
Google Play Games on PC Developer Emulator. This is best used to QA the game before release
to test the end to end player experience after the initial release.