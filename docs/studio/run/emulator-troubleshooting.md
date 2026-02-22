---
title: https://developer.android.com/studio/run/emulator-troubleshooting
url: https://developer.android.com/studio/run/emulator-troubleshooting
source: md.txt
---

# Troubleshoot known issues with Android Emulator

This page lists known issues, workarounds, and troubleshooting tips for the Android Emulator. If you encounter an issue not listed here or are unable to successfully use a workaround listed here,[report a bug](https://developer.android.com/studio/report-bugs#emulator-bugs).
| **Note:** If the emulator runs but performs poorly in general, you might need to[configure hardware acceleration](https://developer.android.com/studio/run/emulator-acceleration)for the emulator.

## General issues

*** ** * ** ***

## Google maps not showing in Android Emulator extended controls

Android Emulator versions prior to version 34.2.13 will no longer have a functional Google maps in the extended controls starting in mid-May. Older emulators ship with a version of Chromium that is incompatible with the Google maps Javascript API.

## Check for adequate disk space

To avoid crashes and hangs due to lack of free disk space, the emulator checks for sufficient free disk space on startup and doesn't start unless at least 5 GB is free. If the emulator fails to start, check whether you have adequate free disk space.

## Antivirus software

Because many security and antivirus software packages work by monitoring every read and write operation, use of such software can decrease the performance of tools like the Android Emulator.

Many antivirus packages provide the ability to add specific applications to a list of trusted applications, which enables the listed applications to operate without performance degradation. If you are experiencing poor performance with saving or loading AVD snapshots, you might improve this performance by adding the Android Emulator application as a trusted application in your antivirus software.

The performance impact differs between antivirus software packages. If you have additional antivirus software installed beyond what is included with your operating system, you can run simple tests to determine which antivirus software has a greater performance effect on emulator load and save operations.

Some antivirus software may be incompatible with the Android Emulator.

If you're using Avast software and are having trouble running the Android Emulator, disable**Use nested virtualization when available** and**Enable Hardware assisted virtualization** in the Avast**Troubleshooting**settings. In addition, after Avast hardware virtualization is disabled, ensure that HAXM is set up properly again with a full reinstallation of the latest HAXM from the SDK Manager.

On Windows, sometimes the AVD freezes with HAXM and the issue can be resolved by uninstalling McAfee completely.

## Windows: Free RAM and commit charge

When the emulator starts, it needs to initialize the Android guest operating system's RAM. On Windows, the emulator requests that Windows account for the full size of guest memory at start time, even though during actual operation, the memory may be paged in on demand. The emulator requests the full amount of guest memory at start time because Windows is conservative in ensuring that there is enough physical RAM and pagefile available to hold the entire potential working set. This request prepares for the worst case, where all guest memory is touched quickly without any opportunity to discard or otherwise free memory.

Sometimes, when the emulator asks Windows to account for this full guest memory size, the request exceeds the current*commit limit*, which is the total of the available physical RAM and pagefile. In this case, Windows can't guarantee that the worst-case working set fits in either physical RAM or pagefile, and the emulator fails to start.

In typical cases, the amount of hard drive space allocated for the pagefile plus physical RAM is more than enough for most use cases of the emulator. However, if you experience failures to start the emulator because of exceeding the commit limit, we recommend examining the current commit charge, which can be seen in the**Performance**tab in the Windows Task Manager. To open the Task Manager, press Ctrl+Shift+Esc.

To lower the likelihood of exceeding the commit limit in various ways:

- Free physical RAM before launching the emulator by closing unused applications and files.
- Disable third-party memory management and memory compression utilities. These utilities can inefficiently cause an excess commit charge and bring your system closer to the commit limit.
- Use a*system managed size*for the Windows pagefile, which can more flexibly and dynamically increase the pagefile size, and therefore the commit limit, in response to increased demand from the emulator and other applications.

  For more information on commit charges and why a flexible setting works best, read[this Microsoft article](https://blogs.technet.microsoft.com/markrussinovich/2008/11/17/pushing-the-limits-of-windows-virtual-memory/).

## Multi-touch does not work in tool window

Multi-touch gestures, including two-finger panning, don't work when the emulator is running in a tool window. To enable multi-touch,[launch the emulator in a separate window](https://developer.android.com/studio/run/advanced-emulator-usage#standalone-window).

## Emulator degrades Bluetooth audio output

If you are using a Bluetooth headset, you might notice that the Bluetooth headphone audio output degrades when the emulator runs ([issue 183139207](https://issuetracker.google.com/issues/183139207)). This happens because when the emulator launches, it turns on the headset's microphone, which causes the headset to switch the duplex mode with reduced quality.

To avoid this problem, disable the microphone in the emulator by adding`hw.audioInput=no`to the`config.ini`file of the Android Virtual Device (AVD). To find an AVD's`config.ini`file, go to the AVD in the Device Manager, click its overflow menu, and select**Show on Disk**.

## Android Virtual Devices fail to launch on ChromeOS

On ChromeOS, Android Virtual Devices (AVDs) might fail to launch because the`libnss3`dependency is missing. To launch the AVDs successfully, run`sudo apt install libnss3`to manually install the`libnss3`library.

## Wrist tilt sensor warnings on Wear OS

On Wear OS, the emulator might repeatedly log the following message regarding the wrist tilt sensor:`the host has not provided value yet for sensorHandle=16`

Developers can safely ignore these warnings.

## Embedded emulator window too small

On machines with lower resolution, such as 1024x768, it can be difficult to read the emulator screen when it runs in a tool window in Android Studio. To give the emulator more space, close the**Device Manager** tool window if it's open. You can also pull the emulator window out of Android Studio. To do so, in the emulator window, click on**Settings \> View Mode** and select**Window** instead of**Dock Pinned**.

## Graphics issues

*** ** * ** ***

## Android Emulator runs slowly after an update

A number of external factors can cause the Android Emulator to begin running slowly after an update. To begin troubleshooting, we recommend the following steps:

- If you have an Intel GPU (and in particular, the Intel HD 4000), ensure you have downloaded and installed the latest Intel graphics driver.
- If your machine has both an Intel GPU and a discrete GPU, disable the Intel GPU in Device Manager to ensure you are using the discrete GPU.
- Run the emulator using the`-gpu swiftshader`mode. For more information about configuring graphics acceleration options on the command line, see[Configure hardware acceleration](https://developer.android.com/studio/run/emulator-acceleration#command-gpu).
- Ensure that your router is not using IPv6 addresses if you don't have an IPv6 connection.

If you are still experiencing problems with the Android Emulator running slowly,[report a bug](https://developer.android.com/studio/report-bugs#emulator-bugs)and include the necessary Android Emulator details so we can investigate.

## Error: vulkan-1.dll cannot be found

If the emulator fails to launch due to the error`vulkan-1.dll cannot be found`, you probably need to update the emulator. To update the emulator in Android Studio, go to**Tools \> SDK Manager**and install the latest stable version of Android platform.

Alternatively, if you don't need any apps that use the[Vulkan](https://developer.android.com/ndk/guides/graphics/getting-started)graphics library, turn off Vulkan by[launching the emulator from the command line](https://developer.android.com/studio/run/emulator-commandline)with the flag`-feature -Vulkan`.

## Unable to create a snapshot

Creating a[snapshot](https://developer.android.com/studio/run/advanced-emulator-usage#snapshots)of the emulator that includes the[Vulkan](https://developer.android.com/ndk/guides/graphics/getting-started)graphics library is not supported. To run the emulator without Vulkan,[launch the emulator from the command line](https://developer.android.com/studio/run/emulator-commandline)with the flag`-feature -Vulkan`. Alternatively, you can uninstall and avoid using apps with Vulkan, such as Chrome on API 30 or higher, if you want to use snapshots as part of your development workflow.

## Cannot open webpage correctly

Starting with API level 30, Chrome uses the[Vulkan](https://developer.android.com/ndk/guides/graphics/getting-started)graphics library as its rendering backend, and it could have compatibility issues on certain machines. If Chrome does not render correctly for you, try to[launch the emulator from the command line](https://developer.android.com/studio/run/emulator-commandline)with the flag`-feature -Vulkan`.

## GPU Driver Warning - Falling Back To Software

If you are receiving a warning about GPU driver falling back, you might be on an unsupported GPU. By default it uses auto which might pick software rendering. If you choose hardware you should be able to force it to use hardware rendering (it might still pop a warning message).

For non-playstore images, you could do it in device manager -\> 3 dots -\> edit. For playstore images, you would need to manually edit those 2 config files:

\~/.android/your_avd_name.avd/config.ini

\~/.android/your_avd_name.avd/hardware-qemu.ini

and change`hw.gpu.mode`to`host`

Note that doing so might reduce the stability of the emulator. See[bug](https://issuetracker.google.com/issues/229642759)for more details.

## Emulator does not boot on Windows Chrome Remote Desktop

If Emulator does not boot while using Chrome Remote Desktop on Windows, the current recommended workaround is to use-gpu flag like -gpu host or -gpu swiftshader.

## Emulator terminated with exit code -1073741511 (Windows 8.1 or Windows 10 N)

The reason is likely because your system (ex:C:\\Windows\\System32 (64-bit system)) is missing msvcp140.dll, msvcp140_1.dll and msvcp140_2.dll In the past, users who have reported this issue were able to fix it by installing (or reinstalling) Windows Media Feature which is optional in Windows 10 N versions.

A similar issue can be seen with Windows 8.1.

Check with the microsoft website how to install the Windows Media Feature.

Note that Windows 8.1 is no longer supported, not only by Android Studio and the Android Emulator, but also by Microsoft (since 2023). A similar comment can also be made with Windows 10, as Microsoft announced that support for Windows 10 ends on October 14, 2025. While we understand the need for a solution on Windows 8.1/Windows 10, continuing development and support for older operating systems presents challenges that can impact the stability and performance of the emulator for the majority of our users.

As a potential workaround (but unsupported), if you're unable to upgrade your operating system, you may attempt to find an older version of the Android Emulator in our archive (https://developer.android.com/studio/emulator_archive last stable being 32.1.11) that might be compatible with Windows 8.1. Note that these lower versions are unsupported and may not function correctly, and we strongly advise against using them with newer versions of Android (like API 34 and above).

For the best experience with the Android Emulator, we recommend upgrading to a supported operating system.

We apologize for any inconvenience this may cause.

## Emulator behaves incorrectly on macOS in hardware rendering mode

On Mac devices with Apple Silicon, the emulator uses the[MoltenVK](https://github.com/KhronosGroup/MoltenVK)library for Vulkan API when hardware rendering mode is selected. While MoltenVK generally provides much better performance, the library doesn't support all Vulkan features. In case of compatibility issues, like shader compilation failures, graphical glitches or crashes in your apps, change the rendering mode to software through the AVD settings, or use the`-gpu swiftshader`command line argument.

Alternatively, you can disable Vulkan support with the`-feature -Vulkan`argument to keep using hardware acceleration on GLES apps.

## Network issues

*** ** * ** ***

## No internet: server DNS address cannot be found

If the emulator cannot connect to the internet, try[launching the emulator from the command line](https://developer.android.com/studio/run/emulator-commandline)using the option`-dns-server "2001:4860:4860::8844,2001:4860:4860::8888,8.8.8.8,8.8.4.4"`. This command supplies a comma-separated list of Google Public DNS IP addresses. For more information about Google Public DNS, see[Google Public DNS for your devices](https://developers.google.com/speed/public-dns/docs/using).

## No internet: DNS resolution issues

Sometimes DNS addresses in the`/etc/resolv.conf`file don't work properly. You can work around this issue by[launching the emulator from the command line](https://developer.android.com/studio/run/emulator-commandline)using the option`-dns-server 8.8.8.8`or`-dns.server 2001:4860:4860::8888`to connect over an IPv6-only network.

## Old issues (on deprecated emulators or old systems)

*** ** * ** ***

## Unable to launch AVD

An AVD might not launch if a crash report for a newer emulator exists ([issue #281725854](https://issuetracker.google.com/281725854)). This issue occurs only for users who update from canary version 33.x to 32.1.13, had a crash the last time they ran the 33.x version, and haven't rebooted their AVD since, so the`%TEMP%`or`/tmp`directory is still on. If you're experiencing this issue, try clearing the`%TEMP%`directory (`/tmp`on Linux or macOS).

## Windows: Emulator fails to launch if there is Unicode in the AVD name

On Windows, when the Device Manager creates an Android Virtual Device (AVD), it by default creates the AVD at`C:\Users\<name>\.android\avd`. However, if the AVD name (`<name>`) has Unicode, the emulator cannot launch the AVD properly using this default location.

This issue is fixed in Emulator 31.3.6 and higher. To solve this issue, update the emulator by selecting**Tools \> SDK Manager**.

Alternatively, to work around this issue, set the environment variable`ANDROID_SDK_HOME`to a custom directory before creating an AVD. For example, create the directory`C:\Android\home`, and then set`ANDROID_SDK_HOME`to this newly created directory. To learn more, see[Environment variables](https://developer.android.com/studio/command-line/variables).

## Hypervisors cannot emulate certain CPU features required by x86 Android systems

Hypervisors generally cannot emulate certain CPU features, such as[Streaming SIMD Extensions (SSE)](https://en.wikipedia.org/wiki/Streaming_SIMD_Extensions), required by x86 Android systems.