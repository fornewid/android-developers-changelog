---
title: https://developer.android.com/studio/releases/emulator
url: https://developer.android.com/studio/releases/emulator
source: md.txt
---

[Android Emulator](https://developer.android.com/studio/run/emulator) is included with Android Studio.

Versions of the emulator prior to 25.3.0 were distributed as part of the Android
SDK Tools.

To ensure you have the latest version, check the
[SDK Manager](https://developer.android.com/studio/intro/update#sdk-manager) for updates.

To download previous versions of Android Emulator, see the
[Emulator download archive](https://developer.android.com/studio/emulator_archive).

For release notes for Emulator versions prior to 25.3.0, see the
[Android SDK Tools release notes](https://developer.android.com/studio/releases/sdk-tools).

To see what issues have been fixed in the most recent versions of Android
Emulator, see the
[closed issues](https://developer.android.com/studio/releases/fixed-bugs/emulator/36).

For known issues and troubleshooting, please see [Emulator Troubleshooting](https://developer.android.com/studio/run/emulator-troubleshooting).

## 36.4.9 Stable (Feb 10, 2026)

- To streamline GPU selection within the user interface, the Android Emulator
  extended controls now includes specific Hardware and Software options. For
  command line users, '-gpu software' option can now be used to select the best
  available GLES and Vulkan software rendering backends for your system

- Enabled Lavapipe as the default graphics software renderer to improve Vulkan compatibility across all platforms

- Vulkan Improvements:

  - Updated the Vulkan loader bundled with the emulator
  - Fixed various invalid usage cases on Vulkan backend
  - Added support for using SkiaVk on systemui with graphics queue emulation on new system images
  - Added support for Vulkan composition to disable GL usages on the host. This is enabled by default for XR images and can be enabled with '-feature VulkanNativeSwapchain' command line option.
- \[Bug Fix\][Issue #471008659](https://issuetracker.google.com/471008659) Memory leak on the Host side of the emulator when opening/closing activities

## 36.4.3 Canary (Dec 8, 2025)

**New AI Glasses Emulator**

We added a new, experimental AI Glasses emulator for developing and testing apps
built with the Jetpack XR SDK for AI Glasses. You can run a glasses emulator
along with a phone emulator, pair them and do typical interactions that
you would run on the glasses. See [Creating Virtual AI Glasses
Devices](https://developer.android.com/develop/xr/jetpack-xr-sdk/run/create-avds/ai-glasses) for information
about installing the AI Glasses emulator and setting up your development
environment.

The AI Glasses emulator is an experimental tool. Expect issues, specifically on
re-pairing glasses to phone emulators and Touchpad UI interactions.

**New XR Glasses Emulator**

We extended the previously launched Android XR emulator for OST (Optical See
Through) XR Glasses. You can use the XR Glasses emulator to preview your app
with the approximate FOV and resolution of the XR glasses device. See [Creating
Virtual XR Glasses
Devices](https://developer.android.com/develop/xr/jetpack-xr-sdk/run/create-avds/xr-headsets-glasses) for
information about installing the XR Glasses emulator and setting up your
development environment.

The XR Glasses emulator and AI Glasses emulator are experimental tools. Expect
issues, specifically on some Windows GPU and driver configurations (see
[Windows system requirements](https://developer.android.com/studio/install#windows)).

**Known Issues**

- [Emulator issues](https://issuetracker.google.com/hotlists/7655515)

- [AI Glasses issues](https://issuetracker.google.com/issues?q=componentid:1970526)

Your feedback will help us to improve and guide future feature
prioritization. See [Report a bug](https://developer.android.com/studio/report-bugs) for information on
reporting bugs related
to Android Studio or Android Emulator.

## 36.3.10 Stable (Dec 4, 2025)

- \[Bug Fix\][Issue #452843321](https://issuetracker.google.com/452843321) Degraded performance when pushing large files into the emulator on Android API 34 and later.

- Fix Vulkan composition crashes when video codecs run in gpu texture mode.

- Fix Emulator crashes on touchscreen event when running with -debug-events.

## 36.2.12 Patch (Oct 13, 2025)

- Fix crash on Windows that occurred when launching a vulkan app in software rendering mode

## 36.2.11 Stable (Oct 9, 2025)

- HAXM support is removed from the Emulator. If you try to create an AVD with
  HAXM, will see a banner reporting missing a hypervisor and an action link to
  install AEHD.

  ![Banner displayed when user tries to create a new AVD with HAXM](https://screenshot.googleplex.com/7W8674ZekzyfpH3.png)
  For information on uninstalling HAXM, see [HAXM Uninstall](https://developer.android.com/studio/run/emulator-acceleration#haxm-uninstall).
- Fix to ensure Intel GPU uses OpenGL ES 3.0 to avoid driver crash

- \[Bug Fix\][Issue #340322888](https://issuetracker.google.com/340322888) Can't start AVD when there are not empty space on device

- \[Bug Fix\][Issue #150758736](https://issuetracker.google.com/150758736) Intermittent single-byte data loss on TCP connections in emulator

- \[Bug Fix\][Issue #434774381](https://issuetracker.google.com/434774381) Guest kernel crashed after quick boot for API 36 and 35 (maybe more) on Windows 11 using WHPX on i7-11850H

## 36.1.9 Stable (Jul 31, 2025)

- \[Bug Fix\][Issue #419157428](https://issuetracker.google.com/419157428) UTF-8 characters in the username or in the AVD path could prevent the emulator to start

- \[Bug Fix\][Issue #423670833](https://issuetracker.google.com/423670833) Android Emulator crashes on btrfs file system

- **Note:** If you are experiencing issues with launching the emulator on X11,
  then consider using software rendering. See
  [Configure graphics acceleration](https://developer.android.com/studio/run/emulator-acceleration#avd-gpu)
  for how to configure software rendering.

## 35.6.11 Stable (Jun 24, 2025)

- AMD and Nvidia GPU support has been improved on Windows and Linux for XR Emulation

- XR AVD can be run as embedded in the Android Studio running windows

- Improvement of crash report details on Windows to enable Emulator's complete dump

- \[Bug Fix\][Issue #410485043](https://issuetracker.google.com/410485043) Android Emulator XR Device crashes with Vulkan error

- \[Bug Fix\][Issue #388718417](https://issuetracker.google.com/388718417) libndk_translation.so aborts and causes a crash in Arm64AesEncode

## 35.5.10 Stable (May 6, 2025)

- Added additional CPU compatibility checks with error messages (ex: insufficient disk space)

- Fixed bugs related to Vulkan memory management and invalid use cases

- Vulkan snapshot support is checked and skipped correctly when running over a terminal

- Added support for VK_KHR_multiview extension and A1R5G5B5 texture format

- Pixel 9a AVD added

## 35.4.9 Stable (Feb 25, 2025)

- Added a drop-down menu in extended controls for Guest GLES driver preferences

- \[Bug Fix\][Issue #389330750](https://issuetracker.google.com/389330750) Sending SMS to emulator with Ñ character splits the message

- \[Bug Fix\][Issue #382180488](https://issuetracker.google.com/382180488) Function "emuglConfig_get_vulkan_hardware_gpu_support_info" crashing due to zero Vulkan devices detected

- **Note:** Android XR Emulator are only available in Canary versions of Studio

## 35.3.11 Stable (Jan 9, 2025)

- \[Bug Fix\][Issue #368059211](https://issuetracker.google.com/368059211) Android Auto OS programmatic access to VHAL not working using Car Service API

- \[Bug Fix\][Issue #348598513](https://issuetracker.google.com/348598513) Emulator has unnecessary thread-unsafe public method in a multi-threaded lock

- \[Bug Fix\][Issue #356896486](https://issuetracker.google.com/356896486) Really disable Vulkan API calls when running with -feature -Vulkan

## 35.4.4 Canary (Dec 12, 2024)

**New Android XR Emulator**

We added a new, experimental Android XR emulator for developing and testing apps
built with the [Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk) for headsets. See
[Jetpack XR SDK Setup](https://developer.android.com/develop/xr/jetpack-xr-sdk/setup) for information about
installing the Android XR emulator and setting up your development environment.

The Android XR emulator is an experimental tool. We decided to share early with
you nevertheless - to allow you to test early on. Expect issues, specifically on
some Windows GPU and driver configurations. Issues might also arise around
compatibility testing of existing 2D mobile Apps. Your feedback will help us to
improve and guide future feature prioritization.

So far, the Android XR emulator has been tested on the following HW
configurations:

- Mac (ARM)
- Windows 11
  - nVidia GPU, 4GB of vRAM, driver version 553.35 or later
- 16 GB of RAM or more
- 8 Cores or more

**Known Issues**

Emulator - Stability and performance:

- Critical system locks or crashes during boot or while running applications can happen on some Windows configurations. Please make sure the Windows Hypervisor Platform (WHPX) is enabled by following the [Android Studio Developer's Guide to enable WHPX](https://developer.android.com/studio/run/emulator-acceleration#vm-windows-whpx).
- Issues such as non-responsive AVD or UI elements on laptops after a suspend-resume cycle (such as closing a laptop and opening it).
- Occasional crashes when switching applications from "home screen mode" to "full screen mode"
- Gemini APIs are not yet available; the Gemini API starter template App will crash.

Emulator - Simulating input and output:

- Virtual keypad for search and edit fields may only be partially visible in the field of view
- Elements cannot be moved in z-direction (in and out of screen) using mouse and keyboard

- AVD microphone host audio input instability may result in AVD reboots and crashes.

- Sound sometimes has static or is distorted.

- When the camera is moved out of the virtual living room, rendering errors are visible.

- Windows configurations display darker than usual colors.

- Audio no longer functions after leaving the emulator idle and locking the screen on macOS. (A restart of the emulator will restore it.)

- Network connection breaks when the host machine changes Wi-Fi.

- With Caps Lock enabled, lower case letters are still typed.

- Scrolling using the trackpad on Mac is not smooth.

- Click-and-drag scrolling on some UI elements might not work by design. If not, use the mouse wheel to scroll instead.

- Blurry text,UI, and other glitches in Chrome on some Windows system configurations. Likely workaround: [Enabling WHP](https://developer.android.com/studio/run/emulator-acceleration#vm-windows-whpx).

Emulator - Simulating planes and anchors:

- Anchors sometimes don't respawn near the same location
- Movable panes may not anchor to walls or ceiling
- Simulated planes don't match the physical layout of the 3D room in passthrough mode
- Overall limited areas to anchor objects in virtual room
- Small visible artifact in the passthrough view on Windows
- In some cases, placing anchors can crash the App
- Black lines may appear on top of Apps when moving Apps close to the ground on Windows

Emulator - Others:

- Emulator only starts in "standalone" mode. "Embedded" mode (embedded UI) is not supported yet.
- Logging in with accounts on the emulator on Windows may cause the emulator to stop responding
- UI content of windows may disappear after resizing (workaround: pressing "Home" button)
- In the JXRCore ActivityPanelTest App the secondary panel is not displayed initially
- Quick settings items might disappear from system settings after an extended period.
- The emulator UI may appear outside of the screen region initially. If so, adjust the size of the emulator window slightly and it should snap back into place.
- Emulator might not startup when using Chrome Remote Desktop on Windows
- OpenXR is so far not supported on the emulator and OpenXR apps might crash the emulator
- Rare failures when trying to submit bug reports using Android Studio extended settings on Windows
- "Navigating back" icon is not visible correctly on Settings app until cursor hovers close to it on Mac
- In some cases, building may err when using the "Baseline Profile" module as part of an XR template project
- "XR Talkback" accessibility is so far only partially integrated into emulator

Scene Viewer App:

- Moving elements within Scene Viewer may cause it to crash. To work around this issue, move the head position away from its initial position slightly (e.g. by using pan, dolly, WASD, etc.) before attempting to move the element.
- The 1:1 real size feature won't work correctly if the real size of the 3D model is less than or greater than the scale min and max limits (currently set to 20 cm and 70 m respectively)
- The 3D model could jump on the first frame after loading

## 35.2.10 (Oct 1, 2024)

- New Pixel AVDs added including Pixel 9, Pixel 9 Pro, Pixel 9 Pro XL, and Pixel 9 Pro Fold
- Added new Tablet system image for Vanilla Ice Cream (API 35)

## 35.1.20 (Aug 29, 2024)

- Added Pixel 8a AVD
- Various bug fixes for foldable
- Qt update and fixes to qt related crashes and hangs
- \[Bug Fix\] Fix to crashes and freeze on Windows with applications using Vulkan

## 34.2.16 (July 9, 2024)

- \[Bug Fix\] UI freezes that occur on Pixel Fold during fold/unfold
- \[Bug Fix\] Incorrect display of Android version as Android Vanilla Ice Cream Preview instead of API 35 on Mac M1.
- \[Bug Fix\] [Issue #296162661](https://issuetracker.google.com/296162661): HasSystemFeature FEATURE_SENSOR_HINGE_ANGLE returns true on Pixel C tablet emulator

## 34.2.15 (May 31, 2024)

- Various crash fixes related to swangle mode and advertiser cleanup

## 34.2.14 (May 20, 2024)

Tested with Android Studio Jellyfish Stable Patch 1.

- \[Bug Fix\] Snapshot sometimes hangs on embedded emulator
- \[Bug Fix\] 'No' and 'Cancel' buttons are not working properly on snapshot
- \[Bug Fix\] Directional pad buttons are not working
- \[Bug Fix\] Fixed the issue seen on Windows preventing the emulator to start in some conditions when using GPU modes with ANGLE, and returning the error message "Failed to initialize GL emulation" in the log. Note that starting the emulator by command line with the option `-gpu swangle_indirect` might still generate this error with this version. If you still want to start the emulator using a command line on Windows with Software graphics rendering with this version, please use `-gpu swiftshader_indirect`
- \[Bug Fix\] Location shortcut on keyboard loads an unusable map
- \[Bug Fix\] While setting location, the "save route" dialog is missing

## 34.2.13 (April 30, 2024)

Tested with Android Studio Jellyfish Stable.

- Update to Qt 6.5.3
- Compatibility for the Google Maps API updates used in the Location features in the Extended Controls of the emulator, occurring at the end of May.
- High impact crash fixes
- Various fixes to Pixel AVDs
- Update the graphics library used for software rendering
- \[Bug Fix\][Issue 225541819](https://issuetracker.google.com/225541819) Starting Chrome crashes Emulator on x86_64
- \[Bug Fix\][Issue 314614435](https://issuetracker.google.com/issues/314614435) `-http-proxy` switch is parsed incorrectly

## 34.1.20 (April 1, 2024)

Tested with Android Studio Iguana Stable.

- \[Bug Fix\] [Issue #314614435](https://issuetracker.google.com/314614435): Fix issue where `-http-proxy` switch is parsed incorrectly

## 34.1.19 (March 7, 2024)

Tested with Android Studio Iguana Stable.

- \[Bug Fix\] [Issue #312677259](https://issuetracker.google.com/312677259): Fixed screen freeze in embedded emulator after resizing window.

## 34.1.18 (Feb 29, 2024)

Tested with Android Studio Iguana Stable.

- Devices were added to Emulator including:
  - Pixel Fold
  - Pixel Tablet
  - Pixel 8
  - Pixel 8 Pro
  - Pixel 7a
- gRPC Integration Test: gRPC endpoints are now available to instrumented tests running inside the emulator that would enable testing of realistic scenarios. This feature enables developers to safely interact with the gRPC endpoint hosted by the Android Emulator from within Android instrumentation tests.
- Various bug fixes
  - [Bug Fix](https://issuetracker.google.com/203793073): Improvements in fold device usability
  - [Bug Fix](https://issuetracker.google.com/155427725): Adjust the position of the Emulator after rotation
  - Crash fixes

## 33.1.24 (Dec 28, 2023)

Tested with Android Studio Hedgehog Stable and Iguana Beta 1.

- Fix Emulator webcam issue that doesn't allow screen record in mp4 format.
- Fix Emulator crash on the Pixel Fold AVD when it is unfolded during a screen recording.
- Fix issue where Pixel Fold shows a different phone skin with a detached keyboard and is unusable (fixed on Windows, Mac Intel, and Linux)
- Fix glitch in appearance in Virtual sensors in Standalone mode (fixed on Windows, Mac Intel, and Linux)
- Provide fixes for some crashes, especially while closing the emulator, were fixed

## 33.1.23 (Nov 30, 2023)

Tested with Android Studio Giraffe Patch 4 and Hedgehog Stable.

- New foldable implementation to better emulate Pixel Fold device, works with latest API 34
- Graphics backend upgrade: We've implemented the gfxstream protocol for our graphics backend, This enhancement elevates the overall graphics performance and stability of your system. In addition, introducing Vulkan 1.3 support beginning with system image with API 34
- [Feature Request](https://issuetracker.google.com/242496928): Option to disable pinch-to-zoom gesture or reassign its hotkey
- \[Bug Fix\] [Issue #302562962](https://issuetracker.google.com/302562962) Fix Emulator webcam crash when using MacOS sonoma
- \[Bug Fix\] [Issue #293503871](https://issuetracker.google.com/293503871) Fix issue where 'Microphone' setting is not saved when Emulator is restarted
- \[Bug Fix\] [Issue #270386314](https://issuetracker.google.com/270386314) Fix animation error where sidebar stays open once the AVD screen minimized
- \[Bug Fix\] [Issue #154896775](https://issuetracker.google.com/154896775) Fix bug submission tool

## 32.1.15 (Aug 29, 2023)

Tested with Android Studio Giraffe Patch 1 and Hedgehog Canary 16.

- Comply with GAS HW requirements for Sensors in AAE Emulator
- \[Bug Fix\] [Issue #266201208](https://issuetracker.google.com/266201208) Hebrew SMS is not sent on API 33
- \[Bug Fix\] [Issue #257097404](https://issuetracker.google.com/257097404) Emulator doesn't show correct time after the host is waken up on API 29 and 30
- \[Bug Fix\] [Issue #228201899](https://issuetracker.google.com/228201899) Can't see google maps inside Android Emulator Extended Controls

## 32.1.14 (June 27, 2023)

Tested with Android Studio Hedgehog Canary 8, Giraffe Beta 5, and Flamingo
Stable.

- Fix emulator camera orientations \& distortions.
- \[Bug Fix\] [Issue #257097404](https://issuetracker.google.com/257097404) "Emulator doesn't show correct time after the host is waken up". This bug is still reproducible for API 29 and API 30.
- \[Bug Fix\] [Issue #243456582](https://issuetracker.google.com/243456582) "Android releases after API 30 might not start correctly in emulator on Mac M1 machines"

## 32.1.13 (May 22, 2023)

Tested with Android Studio Hedgehog Canary 2, Giraffe Beta 1, and Flamingo Stable.

- Add support for Pixel Fold and Pixel Tablet AVDs.
- Improve gLinux crash issue.
- \[Bug Fix\] [Issue #215231636](https://issuetracker.google.com/215231636) "Emulator with API above API 30 not working in Intel 12th gen processor".
- \[Bug Fix\] [Issue #275397905](https://issuetracker.google.com/275397905) Highlevel of crash on Android Emulator M1 when moving cursor focus in and out of the emulator repeatedly.
- Known issue with AVD launch when a crash report of a newer emulator exists. See [Emulator Troubleshooting](https://developer.android.com/studio/run/emulator-troubleshooting) for more information.

## 32.1.12 (March 21, 2023)

Tested with Android Studio Giraffe Canary 10, Flamingo RC, and Electric Eel Patch 2.

- \[Bug Fix\] [Issue #267647323](https://issuetracker.google.com/267647323) Network doesn't work on Emulator started from Android Studio
- \[Bug Fix\] [Issue #268498686](https://issuetracker.google.com/268498686) Emulator screen is flickering
- \[Bug Fix\] [Issue #270034824](https://issuetracker.google.com/270034824) Emulator performance degraded after updating to version 33.1.1
- \[Bug Fix\] [Issue #225541819](https://issuetracker.google.com/225541819) Starting Chrome crashes Emulator on x86_64
- \[Bug Fix\] [Issue #257097404](https://issuetracker.google.com/257097404) Emulator doesn't show correct time after the host is waken up
- Add crash reporting for Apple M1 devices

## 32.1.11 (February 8, 2023)

Tested with Android Studio Giraffe Canary 2, Flamingo Beta 1, and Electric Eel Patch 1.
| **Note:** [Android 14](https://developer.android.com/about) is only compatible with Emulator 32 and higher.

- Network speed optimizations
- Mouse support in Embedded Emulator
- Virtio-snd improvements
- Disable the usage of symlinks while unzipping the Android Emulator during installation
- Fix crash in emulator-check

## 31.3.14 (December 13, 2022)

Tested with Android Studio Dolphin, Electric Eel RC1, and Flamingo Canary 9.

- \[Bug Fix\] Fix AVD crashes that occur when logging in to Play Store.

## 31.3.13 (October 27, 2022)

Tested with Android Studio Dolphin, Electric Eel Beta 2, and Flamingo Canary 5.

- \[Bug Fix\] [Issue #249948338:](https://issuetracker.google.com/249948338) Time zone parameter not functioning
- \[Bug Fix\] [Issue #249366543:](https://issuetracker.google.com/249366543) Emulator -dns-server option does not work after API 31

## 31.3.12 (October 10, 2022)

Tested with Android Studio Dolphin and Electric Eel Beta 1.

This update includes the following improvements and fixes:

- \[Bug Fix\] [Issue #247843000:](https://issuetracker.google.com/247843000) AVD relative path handling error
- Increase disk size for API 24 and later

## 31.3.11 (September 23, 2022)

Tested with Android Studio Dolphin and Electric Eel Canary 10.

This update includes the following improvements and fixes:

- \[Bug Fix\] Embedded Emulator AVD crash on Extended Controls Window
- \[Bug Fix\] [Issue #183139207:](https://issuetracker.google.com/183139207) Audio issues associated with Emulator activating microphone
- \[Bug Fix\] [Issue #229764024:](https://issuetracker.google.com/229764024) AVD sticky touch bug that results in UI behavior issues
- \[Bug Fix\] Error with launching API 33 AVD on Mac M1.
- \[Bug Fix\] [Issue #243053479:](https://issuetracker.google.com/243053479) Slow network speed after updating Emulator
- \[Bug Fix\] [Issue #244617627:](https://issuetracker.google.com/244617627) Nonfunctioning Maps location on Windows and Linux
- \[Bug Fix\] [Issue #232971796:](https://issuetracker.google.com/232971796) Nonfunctioning "call device" button on the Extended Controls \> Phone page
- Update Android Emulator to minigbm
- Migration of build scripts to Python3

## 31.3.10 (August 18, 2022)

Tested with Android Studio Dolphin Beta 5 and Electric Eel Canary 9.

Standalone downloads of the emulator are now available. If you're experiencing
any issues or crashes with this latest stable release, please
[file a bug](https://developer.android.com/studio/report-bugs#emulator-bugs)
and consider downloading a previously working version
from the
[emulator download archives](https://developer.android.com/studio/emulator_archive).

This update includes the following improvements and fixes:

- Better unicode path support on Windows
- Better handling of emulator shutdown so a new launch of the same AVD could succeed.
- Updated foldable AVD design and default settings
- Updated Wear emulator buttons
- gRPC audio streaming improvements
- Resizable emulator console command added
- Chrome Fix for API 31
- \[Bug Fix\] Google Account Auth Failed with GmsCore v21.42.18

## 31.2.10 (April 20, 2022)

Tested with Android Studio Dolphin Canary 8 and Chipmunk RC 1.

This update includes the following improvements and fixes:

- Add utility to load Vulkan functions with fallbacks
- \[Bug Fix\] Fix gcc8 build error

## 31.2.9 (March 23, 2022)

Tested with Android Studio Dolphin Canary 7.

This update includes the following fix:

- \[Bug Fix\] Ignore memory pressure when saving snapshot on M1

## 31.2.8 (February 7, 2022)

Tested with Android Studio Bumblebee Patch 1 and Chipmunk Canary 6.

This update includes the following improvements and fixes:

- \[Bug Fix\] Unable to sign in to the apps
- \[Bug Fix\] [Issue #215368358:](https://issuetracker.google.com/issues/215368358) "adb reboot" on Intel platform will crash avd with "vcpu shutdown request"

## 31.2.7 (February 1, 2022)

Tested with Android Studio Bumblebee Patch 1 and Chipmunk Canary 6.

This update includes the following fix:

- \[Bug fix\] Emulator hanging error on M1 machines.

## 31.2.6 (January 20, 2022)

Tested with Android Studio Arctic Fox, Bumblebee Beta 4, and Chipmunk Canary 6.

This update includes the following improvements and fixes:

- Added wear buttons to Wear OS emulator.
- Made all vehicle properties editable in VHAL tab.
- \[Bug Fix\] Google Account Auth Failed with GmsCore v21.42.18.
- \[Bug Fix\] Netshaper didn't work well with VirtioWifi.
- \[Bug Fix\] Event mouse console command didn't work.
- Added KVM check for local AVD creation.

## 31.1.3 (January 18, 2022)

This update includes the following improvements and fixes:

- Enabled console ports for Fuchsia.
- When resizing a multi-display window, orientation is ignored.
- Wi-Fi: Added support for filtering out unicast packets based on MAT mac address.
- Wi-Fi: Fixed crash when vmnet is in use.

## 30.9.5 (December 15, 2021)

This update includes the following improvements and fixes:

- Added ability to easily resize to a desktop or tablet sized window.
- Added support for multi-touch input from compatible host devices.
- VirtioWifi: Added support for tap network.
- Enabled Rotary Input for Wear System Images.
- Fixed the gRPC audio configuration issue.
- Updated SensorReplay Emulator Playback to support standard Android sensors.
- Connected the emulator to peripherals and devices using USB with USB pass through.

## 30.4.5 (February 23, 2021)

This update includes the following improvements and fixes:

- macOS: Fixed issues with audio input distortion.
- Added support for virtio-vsock in userspace.
- Future system images will use virtio-console for logcat and kernel messages.
- Speed up Vulkan rendering.
- Added support for snapshot debugging on test failure.
- virtio-gpu: updated definitions to support latest blob resource enums.
- Added snapshot support for the 'asg' type graphics transports.
- macOS: Added support for building against macOS SDK 11.1+.
- KVMclock enabled by default on newer system images.
- Added support for a heart rate sensor to Wear emulators.
- Removed libportability Vulkan backend.
- Added support for more features in modem simulator.

## 30.0.26 (August 16, 2020)

This update includes several new features, improvements to existing features,
and bug fixes.

### Foldables support with virtual hinge sensor and 3D view

- Added support for hinge sensors for foldable devices. This requires a future
  Android 11 system image and AVD configuration. 3D foldable view and hinge
  parameters are now integrated with the existing foldable presets. The following
  can be a used with, for instance, the 7.3 foldable AVD's `config.ini` file:

      hw.sensor.hinge = yes
      hw.sensor.hinge.count = 1
      hw.sensor.hinge.type = 1
      hw.sensor.hinge.ranges = 180-360
      hw.sensor.hinge.defaults = 180
      hw.sensor.hinge.areas = 54.7-0
      hw.sensor.posture_list=4, 3
      hw.sensor.hinge_angles_posture_definitions=210-360, 180-210
      hw.sensor.hinge.fold_to_displayRegion.0.1_at_posture=4

- Foldable devices now also carry a sub-type parameter. The `config.ini`
  property `hw.sensor.hinge.sub_type = hinge/fold` is now available. See the
  [Developing for Android 11 with the Android
  Emulator](https://medium.com/androiddevelopers/developing-for-android-11-with-the-android-emulator-a9486af2d7ef)
  blogpost to read more.

- Hinge sensor is now enabled by default.

- If a foldable device is configured, the emulator now sends hinge angle sensors
  updates and posture changes to the guest. Existing foldable devices will now
  update hinge sensor angle and posture when the toolbar's fold or unfold buttons
  are pressed.

  ![](https://developer.android.com/static/studio/images/releases/emu-hinge-angle.gif)

### Emulator for ARM64 hosts

- Linux emulator source code now supports cross compilation from x86_64 to arm64
  hosts, enabling running arm64 system images with KVM virtualization. Currently,
  only `-gpu swiftshader_indirect` (Swiftshader arm64 host rendering) is
  supported, but a compatible set of host GPU libEGL/libGLESv2 libraries may also
  be used by replacing lib64/gles_swiftshader with them and then relaunching with
  `-gpu swiftshader_indirect`. Snapshots may also not be working (add
  `-no-snapshot` to the command line). Instructions:

      mkdir emu
      cd emu
      repo init -u https://android.googlesource.com/platform/manifest -b emu-master-dev --depth=1
      repo sync -qcj 12
      cd external/qemu
      pip install absl-py
      pip install urlfetch
      sudo apt-get install crossbuild-essential-arm64
      python android/build/python/cmake.py --noqtwebengine --noshowprefixforinfo --target linux_aarch64

- Support for Apple Silicon is in progress.

### virtio-gpu support

- Added support on the host side for upcoming virtio-gpu host coherent blob resources.
- Due to how emulator rendering works, we now process virtio-gpu virtqueue in the vcpu thread (because rendering is offloaded to other threads anyway). virtio-gpu rendering will be enabled in a future system image and emulator version.
- In a future system image the emulator will be able to run all graphics with a virtio-gpu based stack.

### Other new features and enhancements

- USB passthrough is now available on Windows using `-qemu -usb -device
  usb-host,vendorid=<usb-vendor-id>,productid=<usb-product-id>`. (This should also have been workng on Linux and macOS already)
- Updated WebRTC libraries to M83.
- The emulator now supports audio streaming in containers over WebRTC.
- darwinn pipe endpoint has been removed.
- CUDA VPx decode for video is now available, if CUDA VPx decode is available in hardware, via the environment variable `ANDROID_EMU_MEDIA_DECODER_CUDA_VPX=1`.
- On macOS, SSE 4.1 and 4.2 are now available from inside the Android guest.
- On macOS, INVTSC is now enabled by default. This can improve accuracy of time measurements from the guest.
- We now track which extended control pane was selected by the user in metrics.
- Linux emulator now uses KVM paravirtualized clock when the guest kernel version is \>= 5.4 (R system images or later).
- Emulator now uses LZ4 to decompress guest kernels, making it compatible with the modern kernel pipeline.
- Added console commands to obtain the emulator AVD directory, discovery file
  path in the Studio-embedded use case, and path to snapshots:

  ```
  adb emu avd path # Obtains path to AVD directory
  adb emu avd discoverypath # Obtains path to discovery file
  adb emu avd snapshotspath # Obtains path to snapshots folder
  adb emu avd snapshotpath <snapshotName> # Obtains path to the folder that stores the snapshot for the snapshot with name <snapshotName>
  ```
- To make it easier to save vertical screen space, we've added an option to hide
  the device frame for the current AVD in **Extended Controls \> Settings** . To
  globally hide device frames for all AVDs, we've made available the
  `NoDeviceFrame` feature flag, which can be activated via launching the emulator
  from the command line with `-feature NoDevice` frame, or to lock it in, adding
  `NoDeviceFrame = on` to `~/.android/advancedFeatures.ini` (Create this file if
  it doesn't exist already).

- Added a drop down item in cellular page to turn on and turn off meterdness
  support, this is a no-op for older system images that do not support the 5G
  meterdness toggle.

  - Also added console command for the same purpose: `gsm meter on|off`
- Upgraded toolchain / build to C++17.

### Fixes: embedded emulator

- Clipboard should now work.
- Fixed issue where uppercase characters were delivered as lower case characters in the emulator.
- Fixed loading console token from a unicode path in windows.
- Fixed `SO_REUSEPORT` error message on linux.
- Fixed a snapshot corruption issue when sending snapshot commands through gRPC, as well as when pressing the snapshot save button in Android Studio embedded emulator.
- When using the Linux emulator embedded in Studio, we found that if this is
  done through Chrome Remote Desktop, there is a bug where `XDG_RUNTIME_DIR` is
  not set and may cause the embedded emulator to fail to appear due to the
  emulator discovery files being placed in `XDG_RUNTIME_DIR`. You can check the
  status of the [corresponding issue in the Chrome issue
  tracker](https://bugs.chromium.org/p/chromium/issues/detail?id=1077449).

  As a workaround, the emulator now falls back to using discovery files in a
  possibly-different directory that is based on user UID: `/run/user/&lt;uid>`.
- Embedded emulator: Devices with rounded corners/notches now properly change
  their layout to make room for the corners and notch. This requires a cold boot
  of those emulators.

- gRPC endpoint now supports sending SMS to the device.

### General fixes

- We've seen compatibility issues running the Windows emulator with Riot Vanguard active. The Windows emulator now detects Vanguard anti-cheat and pops up a warning message if Vanguard is detected.
- Fixed `FD_SETSIZE` error on Windows. We now use `WSAEventSelect()` instead of `select()` for establishing non-blocking connections to loopback servers.
- Added F16C CPUID feature support to Linux emulator with fixes issues running some ARM64 applications through NDK translation; macOS/Windows in progress.
- Fixed gpx/kml route playback to follow timestamps.
- Fixed bouncing icon on launch for MacOs.
- If `hw.audioInput=no` and `hw.audioOutput=no` in `config.ini`, emulator audio is now properly disabled.
- Fixed an issue where if the emulator window was minimized while the extended controls window was open but not active, the extended controls window would keep showing up when resizing the emulator window. We will completely remove the behavior (the case with active extended controls window) in a future update.
- Fixed a flaky bug with Wi-Fi not connected when the emulator starts.
- Fixed hang-on-exit when emulator issues shell commands with long or indefinite timeouts.
- Updated pc-bios with fixes to better support large images passed to `-initrd`; previous BIOS used a very inefficient method.
- Fixed crash during termination when `-wifi-server-port` option is used.
- The emulator now prints a warning if unsupported options are passed to `-prop` (Only qemu.\* props are supported).
- When building the emulator on Windows, there should be less chance of seeing flaky failures to write to files. For more information, see the [Windows build
  instructions](https://android.googlesource.com/platform/external/qemu/+/refs/heads/emu-master-dev/android/docs/WINDOWS-DEV.md).
- Disabled Zoom button for foldable AVDs, which was causing issues.
- Emulator now correctly reports boot time coming from a device reboot.
- Linux: In the case where there are insufficient KVM permissions, the emulator now prints debugging instructions more promptly.
- Fixed issue where the emulator could not boot recent system images with no acceleration.
- Fixed memory corruption or crash on start from a boot-completed detector.
- Fixed memory leak during long screen recording sessions.
- Emulator icons updated to reflect Studio 4.1 branding.
- Added better support for detecting remote sessions on Windows.

### Fixes: graphics and video decode

- Fixed an issue where latest Asphalt 9 game rendered with a black screen.
- Removed spam about flushing mapped buffer with `NULL`.
- Fixed a race condition when tearing down Vulkan state when a guest Vulkan app exited.
- Vulkan ASTC/ETC2 emulation shaders are now baked into the libOpenglRender library. This will be more reliable versus reading from the filesystem.
- Fixed an issue in Vulkan where if running with a Vulkan 1.0 instance on the host, `vkGetImageMemoryRequirements2KHR` would incorrectly clear the returned `VkMemoryRequirements2` struct's `pNext` field.
- Fixed a memory leak in Vulkan renderer.
- Fixed a recent regression where GLSL ES 1.00 shaders with variable names like `isampler2D` failed to compile.
- Updated ANGLE shader translator with various fixes that address possible failure to compile shaders on Linux.
- We now crash the emulator if the basic framebuffer blit shader fails to compile, in order to keep track of the phenomenon.
- Updated ANGLE shader translator to keep up with upstream ANGLE. This fixed an issue around memory corruption when translating and constant-folding OpenGL ES shaders that used non-square matrices. The shader translator is now a separate shared library, `libshadertranslator.dll`.
- Fixed an issue on Vulkan initialization on some GPU drivers, where certain 1.1 device functions were not found.
- Vulkan: We've reverted back to using the prebuilt loader as favoring the system Vulkan loader caused issues in some setups; will figure out a better solution.
- Fixed issue when using Vulkan external memory where it could have been imported mismatching memory type indices on the host.
- Fixed issue in emulation of `GL_ALIASED_POINT_SIZE_RANGE` where the enum was not supported on the host.
- Fixed issue where on some host GPUs, Skia shaders could not compile due to errors related to `GL_EXT_shader_framebuffer_fetch`.
- Since our copy of the D3D9 ANGLE renderer was removed a few versions ago, we now also auto switch users who were on that renderer to d3d11 ANGLE if it was selected in the UI preferences.
- More debug info has been added to WGL initialization on Windows in order to trace failures.
- When `hw.gltransport=virtio-gpu-pipe`, performance is improved by not spinning on the host in transfers from host to guest.
- Added more debug logging for when OpenGLES emulation fails to initialize.
- Fixed an issue with Youtube videos flickering or not showing up on snapshot load.
- Switched back to software decode for libvpx for now as we've seen issues with CUDA hardware decode of libvpx. If you have a supported CUDA hardware decode implementation on the host side, hardware decode of libvpx can be re-enabled via the environment variable `ANDROID_EMU_MEDIA_DECODER_CUDA_VPX=1`.

## 30.0.10 (April 30, 2020)

This update includes support for running the emulator directly in Android Studio
and virtual devices with Freeform Window Mode activated by default.

### Run the Emulator in Android Studio

The Android Emulator can now be [run directly in Android
Studio](https://developer.android.com/studio/preview/features#run-emulator-studio).
Use this feature to conserve screen real estate, to navigate quickly between
the emulator and the editor window using hotkeys, and to organize your IDE
and emulator workflow in a single application window.

### Freeform Window Mode

You can now create an AVD that has Freeform Window Mode enabled by selecting
the 13.5" Freeform tablet hardware profile when creating a virtual device in
Android Studio. This hardware profile requires a system image with Android 11
Developer Preview 3 or higher.

### Known issues

Resizing freeform windows is currently broken due to issues transferring
focus to the Window Manager. This will be addressed in a future Android 11
system image release.

## 30.0.0 (February 19, 2020)

This update includes Android 11 (API level 30) system images and improved
performance when running ARM binaries.

### Android 11 system images

You can now create an AVD that runs Android 11 by selecting either of the
available API level 30 system images:

- **x86**: Includes both x86 and ARMv7 ABIs.
- **x86_64**: Includes x86, x86_64, ARMv7 and ARM64 ABIs.

### Support for ARM binaries on Android 9 and 11 system images

If you were previously unable to use the Android Emulator because your app
depended on ARM binaries, you can now use the Android 9 x86 system image or any
Android 11 system image to run your app -- it is no longer necessary to
download a specific system image to run ARM binaries. These Android 9 and
Android 11 system images support ARM by default and provide dramatically
improved performance when compared to those with full ARM emulation.

### Known issues

- Some ARMv7 binaries fail to run on Android 11 x86 and x86_64 system images. Consider building for ARM64 when targeting Android 11.

## 29.0.11 (May 29, 2019)

This update includes the following improvements and fixes:

- Windows: The emulator now relies on the `libgcc` DLL that we ship instead of being compiled with `libgcc` statically.
- Linux: Added logcat support to the gRPC API. For more information about gRPC, see [gRPC streaming emulator (Linux)](https://developer.android.com/studio/releases/emulator#29.0.6-grpc).
- The emulator now includes a headless build for 32-bit x86 guests (`qemu-system-i386`). This feature enables x86 32-bit images for API levels 26 and lower to run with the headless build. Note that for 32-bit x86 guests with API 27 and later, the emulator uses the 64-bit engine (`qemu-system-x86_64`) because in these system images, while the userspace is 32-bit, the kernel is 64-bit. Android Studio uses the kernel to select emulation engines.
- You can now specify custom Qt library paths using the `ANDROID_QT_LIB_PATH` environment variable.
- You can now run the emulator with previous binaries that use QEMU1 if the QEMU1 executables (`emulator[64]-[x86|arm|etc]`) are placed in the emulator directory.
- Windows: Fixed an issue that could sometimes cause the emulator to fail to start with a "vCPU shutdown request" message.
- Fixed an issue with an unnecessary pipeline barrier in emulated compressed textures in Vulkan.
- Fixed an error that occurred with http proxy requests when chunked transfer encoding was used. For more information, see the [commit details](https://android.googlesource.com/platform/external/qemu/+/1a15692cded92d66dea1a51389a3c4b9e3b3631a).

## 29.0.9 (May 7, 2019)

This update includes the following fix:

- Windows: Fixed an issue where the virtual scene camera and webcam would not work on the emulator.

## 29.0.8 (May 6, 2019)

This update includes the following improvements and fixes:

- Added support for multiple virtual hardware displays when there's a guest service to enumerate and set each display. Multiple virtual hardware displays will be included in a future emulator system image update.
- Added a new command line option: `-delay-adb`. This option suppresses processing of ADB packets until the guest has completed booting (off a cold boot). This option helps resolve issues that could occur if you use the emulator in a CI environment that reboots the emulator and uses DDMS at the same time.
- Fixed an error that occurred when snapshots are loaded where `glIsRenderbuffer` would return the incorrect value.
- Fixed some issues with stale state when the Android guest reboots.
- Windows: Fixed issues that prevented the emulator from starting when the Windows username had non-ASCII characters or spaces.

### Known issues

- The Snapshots UI is disabled for Automotive system images because snapshots aren't currently supported for these system images.

## 29.0.6 (May 1, 2019)

This update includes several new features, improvements to existing features,
and bug fixes.

### Removal of QEMU1 and 32-bit Windows support

To better maintain the emulator, we no longer ship QEMU1 and 32-bit Windows
binaries. If you are using Windows 32-bit, you cannot upgrade to version 29.0.6.

### Requirements for Android Q system images

If you want to run an AVD that uses an Android Q system image, you must now use
version 29.0.6 (this release version) or higher.

### Project Marble Improvements

This update continues our work on the [Project Marble](https://youtu.be/ei_5R0CvLm4?t=2286)
initiative that was announced at the [Android Developer Summit](https://developer.android.com/dev-summit)
in November 2018. For more information about other Project Marble improvements
in previous releases, see [Android Emulator: Project Marble Improvements](https://medium.com/androiddevelopers/android-emulator-project-marble-improvements-1175a934941e).

For this update, most of our Project Marble efforts were dedicated to reducing
emulator resource usage, such as reducing the emulator's CPU usage while idle.
We've also included changes that make it easier to work with the emulator in a
wider variety of environments, and we've addressed general quality issues.

The following sections describe the Project Marble improvements that are
included with this update:

#### Improvements for host audio behavior

Starting with version 28.0.3, the emulator [blocks audio input](https://developer.android.com/studio/releases/emulator#disable-host-audio)
from the host by default.

If you want to use the host audio data, you can enable that option by going to
**Extended Controls \> Microphone** and enabling **Virtual microphone uses host
audio input**. This option is automatically disabled whenever the emulator is
restarted.

If you are using the command line, you can also enable host audio using the
`-allow-host-audio` option, and you can use the following ADB commands to turn
host audio data on or off, respectively:

- `adb emu avd hostmicon`
- `adb emu avd hostmicoff`

#### Improvements for headless emulator builds

Starting with version 28.0.25, the emulator includes a [headless build option](https://developer.android.com/studio/releases/emulator#headless-build)
that can run without the UI. You can use headless builds to help you set up the
emulator for Docker and continuous integration (CI) workflows.
| **Note:** Although the emulator binary with the `-no-window` flag is still available, the headless build is meant to supersede `-no-window`.

With this update, we've made further improvements to allow the emulator to run
with a minimum number of dependencies. On Linux, headless builds no longer
include the `pulseaudio` or `libX11` libraries. The system-dependent shared
libraries that are not packaged with the emulator has been reduced to the
following list:

- `Linux-vdso.so.1`
- `Libutil.so.1`
- `Libm.so.6`
- `Libdl.so.2`
- `Librt.so.1`
- `Libpthread.so.0`
- `Libgcc_s.so.1`
- `Libc.so.6`
- `ld-linux-x86-64.so.2`

#### Upgraded Qt UI libraries to 5.12 LTS

This update includes the following improvements from the Qt 5.12 LTS release:

- To avoid crashes in Qt's `libpng` decoding when starting certain system images, the emulator now uses its own copy of `libpng` to decode PNG images.
- To address issues with some Linux installs containing incompatible versions of some Qt dependent libraries, we now package `libfreetype`, `libsoftokn`, `libsqlite3`, and `libxkbcommon` with the emulator.
- The emulator now uses the platform's native windowing libraries to get monitor dimensions, instead of using the Qt libraries that returned unreliable results.

#### Automatic CPU optimizations after cold boot

To address CPU usage, the emulator now runs the following ADB commands on a cold
boot after it receives a `boot complete` signal:

`adb shell settings put screen_off_timeout 214783647`
:   This command increases the screen off timeout so the emulator can be used in
    battery mode without charging. In battery mode, background CPU usage is greatly
    reduced.
:   In AC charging mode, GMSCore background operations such as app updates can take
    over all the device's CPU cores---and by extension, the user's machine---with no
    warning.

`adb shell pm revoke com.google.android.googlequicksearchbox android.permission.RECORD_AUDIO`
:   This command revokes microphone permissions for the Google search app, which
    greatly reduces background CPU usage on the home screen and in the launcher when
    the Google search app is active.
:   This command is run in addition to the emulator's default behavior of
    [disabling host audio](https://developer.android.com/studio/releases/emulator#disable-host-audio) for the host. Furthermore, this
    automatically provides the CPU usage mitigation described for
    [hotword detection](https://developer.android.com/studio/releases/emulator#hotword-detection) from the 28.0.23 release.
| **Note:** The emulator does not run these ADB commands when using system images with API level 25 and lower because those system images cannot communicate a reliable `boot complete` signal back to the host.

#### New environment variables for performance monitoring

You can now use two new environment variables to enable detailed monitoring of
the emulator's performance and resource usage.

`SHOW_PERF_STATS=1`
:   This environment variable enables tracking of both CPU and RAM usage. Tracking
    for RAM usage distinguishes between graphics usage and total resident memory.

`ANDROID_EMU_TRACING=1`
:   This environment variable enables printing every time an input or graphics
    operation takes a long time (longer than 1 ms).
:   We're also using this environment variable to help diagnose issues that
    Windows users have experienced with more jank (dropped frames) than users
    experience on macOS or Linux.

#### General Project Marble improvements

This update also includes the following general improvements that are part of the Project Marble initiative:

- You can now immediately pause all vCPUs on the emulator via the following console commands:
  - `adb emu avd pause`
  - `adb emu avd resume`
- Greatly reduced overhead of OpenGL drawing. This improvement reduces CPU usage while the emulator is playing animations.
- Restored support for mainline QEMU's e1000 virtual network device. You can use this device to set up the emulator in a bridged network environment. In a bridged network environment, the emulator is shown on the host network and the host network is shown on the emulator.
- QEMU 2.12-appropriate BIOS binaries are now used to start up the emulator.
- Upgraded `ffmpeg` version to 3.4.5 for video encoding and decoding.
- Greatly reduced overhead of QEMU main loop I/O on macOS by replacing the main loop that was based on `select()` with a main loop that is based on `kqueue`.
- Logcat buffer size increased to 2 MB to address issues with flaky unexpected EOF when running logcat with the emulator.
- The emulator now exports the `LC_ALL=C` environment variable by default. This change addresses crashes and incompatibility issues associated with running the emulator in different locales.
- You can now track the CPU and RAM usage of the emulator using performance stats that you can access at **Extended Controls \> Settings \> Advanced \>
  Performance Stats**. Use these stats to quickly diagnose issues if the emulator seems to be using too much CPU or RAM.
- `glReadPixels GL_IMPLEMENTATION_COLOR_READ_TYPE` now uses the host GPU's result instead of an emulated one. This change helps fix issues where images and assets do not display because of improper format for readback.
- Added support for the OpenGL ES extensions `GL_EXT_texture_format_BGRA8888` and `GL_APPLE_texture_format_BGRA8888` if these extensions are supported by the host.
- Added more diagnostic info to the Bugreport UI. In addition, you can access bug reports from the console using the following commands:
  - `telnet localhost 5554`
  - `avd bugreport`
- On Android Q system images, the emulator increases its minimum RAM size to 2 GB.
- Added more logging and printing whenever OpenGL or the hypervisor fails to initialize.
- If the emulator cannot start a concurrent `-read-only` instance of an AVD, the emulator now attempts to relaunch the `-read-only` AVD 3 more times over 3 seconds. This change increases the likelihood that the emulator will be able to launch concurrent `-read-only` instances an AVD if other writable instances of that AVD are not done cleaning up stale files.
- For upcoming system images, the emulator now supports Hardware Composer 2.0. This change should lower the driver overhead when running most animations.
- The emulator build is now based on CMake/Ninja.
- In the emulator extended controls UI, divider lines in the keyboard shortcuts table have been restored.
- Users can now opt-in to provide our team with CPU and RAM usage metrics in a 10 second interval. We use these metrics to enrich our data about emulator resource usage with different use cases from our users, which allows us to make the emulator more efficient and responsive.

#### General Project Marble fixes

This update also includes the following general fixes that are part of the
Project Marble initiative:

- Fixed issues with twitching and incorrect frames that were displayed on systems with Intel GPUs when using Android Q system images.
- Fixed issues where a black screen was displayed when using Android Q system images with Pixel 2 XL skins (or any skin that has a notch or rounded corners).
- Fixed an issue where the `-partition-size` command line option would not set the data partition size.
- Fixed an issue where pulseaudio on the Linx emulator would spin and take up an entire CPU core in some situations.
- Fixed issues with out of bounds memory access when processing compressed textures.
- Fixed GL errors that occurred on the host in `glTexSubImage2D` when updating certain gralloc buffers (with format RGB 565, RGB10A2, RGB(A)16F).
- Fixed a [display issue](https://www.reddit.com/r/androiddev/comments/b0rzjl/loving_android_qs_rainbow_theme_epilepsy_warning/) in Android Q system images with snapshots where the notification shade's geometry was rendered with an improper instance divisor setting.
- Fixed a few hard-to-reproduce crash and freeze issues on launch that happened due to Qt losing signals or having flaky, inconsistent states on startup.
- Fixed numerous concurrency issues. We are now able to build the Linux emulator with ThreadSanitizer (TSAN), which can easily uncover bugs that are otherwise difficult to reproduce.
- For Linux users: we have found that on certain host kernels, the guest Android kernel can error out and exit in KVM with a generic hardware error. The emulator will now `abort()` when this happens in order to increase debuggability (previously, the emulator just hung).
- For Linux users: for convenience with CI setups, you can use the new `-stdouterr-file <file-name>` command line option to redirect both `stdout` and `stderr` to a file.
- Fixed an issue where `SO_REUSEADDR` was used incorrectly. For more information, see the [commit details](https://android.googlesource.com/platform/external/qemu/+/bf36ae9b8ad1bc5ac7c4e6184f8cdf16ce65b67b).
- Fixed a long-standing issue with the Windows emulator where sub-processes, such as ADB commands, failed to start if the username had spaces in it.
- Fixed an issue with missing initialization of RCU in HAXM vCPU threads. This fix can possibly address some crashes and race conditions.
- Fixed a crash that happened with certain patterns of saving and loading snapshots from the snapshots UI using recent Android Q system images.
- Fixed an issue where the virtual scene camera would be blank when the emulator was initialized from a snapshot if an AR macro was playing when that snapshot was saved.
- Fixed an issue where some users with remote desktop setups got a black screen when launching the emulator on Linux. To avoid this, the emulator now explicitly configures `MESA_RGB_VISUAL`. For more information, see the [commit details](https://android.googlesource.com/platform/external/qemu/+/2fceacb84d6b40be22ae6a171c37d3f106287e60).
- Fixed [an issue](https://issuetracker.google.com/127956599) where the rotate buttons would appear on TV AVDs.
- Fixed [an issue](https://issuetracker.google.com/128455869) where if emulator was set always on top, the extended controls window appeared every time the emulator was rotated.

### Hardware profiles for foldable devices

The emulator now includes hardware profiles for foldable devices. To use these
new hardware profiles, you must be using Android Studio 3.5 Canary 10 or higher.

There are two foldable hardware profiles that you can use to create an AVD:

- 7.3" Foldable: 1536x2152 unfolded, 4.6" 840x1960 folded
- 8" Foldable: 2200x2480 unfolded, 6.6" 1480x2480 folded

When you run the emulator using one of these hardware profiles, you can fold and
unfold the device using the [fold and unfold actions](https://developer.android.com/studio/run/emulator#tasks)
in the emulator toolbar, [console commands](https://developer.android.com/studio/run/emulator-console#querycontrol),
or the following keyboard shortcuts:

- Fold: `Ctrl + F` (`Command + F` on macOS)
- Unfold: `Ctrl + U` (`Command + U` on macOS)

### AR macros

The emulator now includes AR macros that can help you test common AR actions.
For example, you can use a macro to reset all the device's sensors to their
default state.

For more information, see [Test common AR actions with macros](https://developer.android.com/studio/run/advanced-emulator-usage#ar-macros).

### Vulkan support (Windows, Linux)

Windows and Linux users can now test Vulkan apps with the Android Emulator up to
Vulkan 1.1 when using a compatible system image (Android Q Beta 3 or higher for
Vulkan 1.1, Android Q Beta 2 for Vulkan 1.0) and a compatible host GPU (this
includes most Intel, NVIDIA, and AMD GPUs from 2014 and later).

To enable Vulkan support, you must add the following feature flags to your
`~/.android/advancedFeatures.ini` file (create the file if it doesn't exist):

- `Vulkan = on`
- `GLDirectMem = on`

| **Note:** Snapshots can't currently be used while Vulkan is enabled. If you enable Vulkan support, the current quickboot snapshot is invalidated.

#### Initial support for ROM developers

ROM developers who are building the `sdk_phone_x86` or `sdk_phone_x86_64`
(`userdebug`, `eng` variants) targets on AOSP `master` branch can now run a
Vulkan-enabled emulator.

This support is still experimental and is mainly for developers who work on
system images, drivers, and game engines. Many extensions are still missing.
However, `HOST_COHERENT` memory is supported, and you should now be able to
run the [Vulkan API Tutorial Samples](https://github.com/googlesamples/android-vulkan-tutorials).

If you are using linux, you can try this by using the following commands:

    mkdir aosp-master
    cd aosp-master
    repo init -u https://android.googlesource.com/platform/manifest -b master --depth=1
    repo sync -c -j12
    . build/envsetup.sh
    lunch sdk_phone_x86_64-userdebug
    make -j12
    emulator -no-snapshot -feature Vulkan,GLDirectMem

#### Skia rendering with Vulkan

NVIDIA and AMD GPUs that support Vulkan also support zero-copy interop with
OpenGL via the `GL_EXT_memory_objects` extension. The emulator leverages this
capability to provide a complete way to render the Android UI using the Skia
Vulkan APIs.

If you have an NVIDIA or AMD GPU that supports Vulkan, use the following
commands to test the Skia rendering with a compatible system image (Android Q
Beta 3 and higher):

    adb shell
    su
    setprop debug.hwui.renderer skiavk
    stop
    start

#### macOS support for Vulkan

macOS support is still experimental, but the emulator already includes the
[Swiftshader](https://swiftshader.googlesource.com/SwiftShader/),
[MoltenVK](https://github.com/KhronosGroup/MoltenVK), and
libportability ([gfx-rs](https://github.com/gfx-rs/gfx)) APIs.
You can experiment with these APIs by setting the following environment
variables:

- Swiftshader: `ANDROID_EMU_VK_ICD=swiftshader`
- MoltenVK: `ANDROID_EMU_VK_ICD=moltenvk`
- libportability: `ANDROID_EMU_VK_ICD=portability`

#### Known issues

HAXM can sometimes fail to map Vulkan coherent memory to the guest and shuts
down the emulator. This is addressed in an upcoming HAXM update.

### gRPC streaming emulator (Linux)

We're always trying to make the emulator as versatile as possible by allowing
host GPU rendering and interactivity in the widest range of running contexts.
Our CI and remote desktop users have the following long-standing issues:

- Programmatically sending input commands to the emulator involves either running adb shell commands that can experience high overhead, or using the telnet console, which is faster, but might not work with certain network configurations.
- CI users often run emulators headless, which can make it difficult to notice issues that require the screen to be visible or interactive.
- Remote desktop users often can't interact with the emulator when using host GPU rendering because GPU rendering is often tied to the host's non-virtual displays.

To address this, when running on a Linux machine, the emulator now serves a
gRPC service. [gRPC](https://grpc.io/) is a general framework
for RPC that works over HTTP.
| **Caution:** This feature is still experimental and is meant to be used from the same machine the emulator is running on. Do not run the service remotely unless you understand and accept the security risks.

By default, the emulator gRPC service is disabled, but you can activate the
service using the following command line option, where `<port>`
is the port which the emulator should serve gRPC requests (usually `5556`):

```
-grpc <port>
```
| **Caution:** Do not run the service on a port that is not secured from remote users.

Once the service is started, gRPC commands can then be issued from clients. The
current set of commands allows both sending input events and receiving
screenshots. These commands help address the following issues:

- Input commands can be sent to the emulator with low overhead over HTTP. HTTP also enables commands to be sent in additional network configurations.
- Screenshot commands can be sent to query the current screen, even if the emulator is running headless. For interactivity, input events can also be sent back to the emulator.
- Remote desktop users can run the emulator headless on the main display with GPU accelerated rendering while using gRPC to get screenshots and send input events in order to interact with the emulator.

For a complete list of the commands that are available, see
[this protobuf](https://android.googlesource.com/platform/external/qemu/+/refs/heads/emu-master-dev/android/android-grpc/android/emulation/control/emulator_controller.proto).

To help you get started with gRPC, we've provided some [sample clients](https://android.googlesource.com/platform/external/qemu/+/refs/heads/emu-master-dev/android/android-grpc/docs/grpc-samples)
that you can refer to.

Currently, this includes the following samples:

- A Go-based service that can be used to query emulator states.
- A React app that demonstrates remote interactivity via screenshot and input RPCs. This sample requires protobuf version 3.7.0 or higher.
- A Python sample that queries the emulator's VM configuration and then sends a series of commands.

## 28.0.25 (March 29, 2019)

This update includes the following improvements and fixes:

### Headless emulator build

The emulator has been difficult to set up with Docker and other continuous
integration (CI) workflows due to the implicit expectations of the system being
able to support Qt along with its shared library dependencies
(among other issues).

As a first step to address this, we've introduced a variant of the emulator
launcher with QEMU executables that does not depend on Qt. On Linux, there is
still a link to `libX11`, but we hope to remove that soon as well.

To use the headless emulator, run the emulator from the command line as usual,
but replace the emulator binary invocation with `emulator-headless`. For more
information, see the [28.1.8 Canary](https://androidstudio.googleblog.com/2019/02/emulator-2818-canary.html)
release update.

- Fixed twitching and incorrect frame display on Intel GPUs when running Android Q system images.
- Fixed issues where black screen would display when using Android Q system images with Pixel 2 XL skins.
- The latest BIOS binaries are now used to start up the emulator. This change can help reduce "vCPU shutdown request" errors that happen sometimes when launching the emulator on Windows.
- Backported a fix for the ["wrong display when resuming Android Q system images from a snapshot" issue](https://www.reddit.com/r/androiddev/comments/b0rzjl/loving_android_qs_rainbow_theme_epilepsy_warning/).
- Users were experiencing ["unauthorized" emulators issues](https://www.reddit.com/r/androiddev/comments/b35cgl/psa_do_not_use_platformtools_2802_with_the/) due to an incompatible change in ADB in platform-tools 28.0.2. You can now safely use ADB from platform-tools 28.0.2 with the emulator. If you are experiencing problems with "unauthorized" emulators, do the following troubleshooting steps:
  1. Exit all emulators.
  2. Delete both the `~/.android/adbkey` and `~/.android/adbkey.pub` files.
  3. Run the following command: `adb kill-server`
  4. Run the following command: `adb devices`
  5. Wipe the AVD data.
  6. Relaunch the emulator.

## 28.0.23 (January 29, 2019)

This update includes the following improvements and fixes:

### Host audio input disabled by default

A [recent post on Reddit](https://www.reddit.com/r/androiddev/comments/aipv3i/til_the_android_emulator_responds_to_ok_google/)
detailed how the guest Android OS would always be using the host microphone's
audio, and thereby allowing "Ok Google" to work unexpectedly. We're sorry about
this and will work with the Android team to make sure hotword detection is
disabled in the system image as well.

To address this, we've made the following changes:

- Actual host audio data is now squelched by default. When the guest uses the microphone, silence is passed over instead of the host's audio.
- If you want to use the host audio data, you can now enable that option by going to **Extended Controls \> Microphone** and enabling **Virtual microphone
  uses host audio input**. This option is automatically disabled whenever the emulator is restarted.

### Updates on CPU usage investigations

During our Project Marble investigations, we've noticed that high CPU usage on
the emulator generally falls into the following three categories:

#### At idle: Automatic app updates in Play Store images

We found that at random intervals, all apps installed get updated, even when the
user is not logged in. During the process, CPU usage is driven to the number of
cores x 100% (typically \~400%) in GMSCore and dex2oat. You can mitigate this
issue by disabling auto app updates in the Play Store app.

#### At idle: Hotword detection

When on the home screen and without any app foregrounded, there can be a great
deal of CPU usage (\~25% with spikes to 50%). This is caused by hotword detection
that constantly pings the host. You cannot mitigate this issue by disabling host
audio input because the CPU cost is primarily caused by the time that it takes
to travel to the guest from the host. However, you can mitigate this issue by
revoking microphone permissions from the Google app.

#### While active, sometimes at idle: Animations

The third source of high CPU usage is animations. We have found that by
optimizing the graphics driver stack we can also reduce CPU usage even when the
emulator is not idle. We will be rolling out graphics driver optimizations
incrementally as part of Project Marble.

## 28.0.22 (December 21, 2018)

This update includes the following improvements and fixes:

- Fixed a long-standing issue where in some settings, the Mac emulator would reboot or kernel panic on Quickboot save. ([Issue 120951634](https://issuetracker.google.com/issues/120951634))
- When using a mapped file as the RAM snapshot, the emulator now unmaps the file mapping explicitly on exit.

## 28.0.20 (December 11, 2018)

This update includes the following improvements and fixes:

- Fixed an issue on Windows that caused the emulator to freeze on snapshot load with certain models of Intel GPUs.
- Fixed an issue that caused an `unauthorized` ADB device state when using a non-standard `ANDROID_SDK_HOME` location.
- Fixed an issue on Windows that caused the emulator to crash when booting system images with CPU acceleration disabled.
- Fixed the pixelated emulator display issue. Downsampling should now be working.
- Fixed an issue on macOS 10.14+ where the virtual scene camera mouselook control could become too sensitive due to an interaction with new accessibility security settings.
- Fixed an error in timezone calculation that could cause the emulator clock to sporadically change.
- Fixed rendering errors in various cocos2d and Unreal engine apps.
- Added support in the emulator for [Wi-Fi peer-to-peer](https://developer.android.com/guide/topics/connectivity/wifip2p). Two emulators can now talk to each other directly via Wi-Fi if using the latest Pie Play Store image. To use Wi-Fi peer-to-peer, start two AVDs with the same `-wifi-server-port` and `-wifi-client-port` arguments:
  - `emulator @<server-avd-name> -wifi-server-port 9999`
  - `emulator @<client-avd-name>-wifi-client-port 9999`
- Added support for more webcams on Windows by taking any incompatible frame sizes and dynamically resizing them to fit the camera setting in the Android guest.

## 28.0.16 (November 2018)

This update includes several new features, improvements to existing features,
and bug fixes.

### Resource usage

The emulator now uses less RAM overall, especially when using system images with
API level 28 or higher. These system images include improved memory usage for
guest-side graphics drivers.

In addition, we have also improved resource usage in the following areas:

- Reduced emulator memory usage during long-running tests. If you still experience issues with memory usage during long-running tests, please create an issue that describes your use case in [Issue Tracker](https://issuetracker.google.com/issues/new?component=192727&template=843117).
- Reduced CPU usage when running apps with animations.
- Fixed an issue where the QEMU AIO context could leak on Windows.

| **Note:** Some Windows emulator users could not launch emulators due to exceeding the RAM commit charge. For help with this issue, see the [emulator Troubleshooting page](https://developer.android.com/studio/run/emulator-troubleshooting#windows_free_ram_and_commit_charge).

### Run multiple instances of a single AVD concurrently

You can now launch multiple instances of the same AVD and run them concurrently.
Instances that you launch after the first instance are read-only, and their
changes to the guest virtual disk are discarded on exit.

To run multiple instances of the same AVD at the same time, launch any instances
after the first instance from the command line using the `-read-only` flag.

This feature is made possible by copying the QCOW2 files associated with the
writable parts of the Android image. To help you manage disk space, we have also
bundled the `qemu-img` command line tool to allow you to pre-commit QCOW2
files before launching multiple instances.

In addition, when used in tandem with the [File-backed guest RAM snapshots](https://developer.android.com/studio/releases/emulator#file-backed-guest-RAM-snapshots) feature, multiple AVD instances share the
primary AVD Quickboot snapshot as a common source of copy-on-write guest RAM.
This property means that the instances share much of their RAM in common. Use
this feature to run tests that require multiple devices to run in parallel.

We appreciate your feedback on possible use cases that are part of your normal
interactive or CI workflow. Please create or upvote issues in [Issue
Tracker](https://issuetracker.google.com/issues?q=componentid:192727).

### File-backed guest RAM snapshots

By pre-allocating and mapping guest RAM as a file, the emulator can now save
Quickboot snapshots during runtime, instead of doing all of the work on exit. If
you currently experience long save times when closing your emulators, enable
this feature to improve your Quickboot performance. By default, a Quickboot
snapshot is saved on exit and loaded again every time, like suspending and
waking a real device.

Because Android guest RAM is now auto-saved by default, if you want to define a
device state and repeatedly load from that state, you need to tell the emulator
to discard changes after each session. You can do this in the following ways:

- Use the `-no-snapshot-save` or `-read-only` flags when launching the emulator from the command line.
- Go to **Extended Controls \> Snapshots \> Settings** and switch **Auto-save
  current state to Quickboot?** to **No**.
- You will need to restart the emulator after selecting this option. If the emulator is set to auto-save, you can run the following command to set a checkpoint:

  ```
  adb emu avd snapshot remap 0
  ```
  After you run this command, the emulator Quickboot snapshot will stay at that checkpoint. Run the same command again to load the emulator from your checkpoint.

| **Note:** When you run [multiple concurrent instances of the same AVD](https://developer.android.com/studio/releases/emulator#concurrent-avd), the emulator disables auto-saving, but those instances then use any existing Quickboot RAM file as a common source of copy-on-write memory.

Snapshots that are taken and loaded through the Snapshots UI function as they
did before, with no file mapping.

Because this is a large change to how Quickboot works, we would greatly
appreciate your feedback on whether it improves Quickboot performance and what
kind of issues you encounter when using it. If you experience problems, you can
disable this feature by adding the following line to your
`~/.android/advancedFeatures.ini` file:

    QuickbootFileBacked = off

When you start the emulator from a snapshot (either using the `-snapshot`
command line option, or launching from a snapshot in the AVD manager) the
emulator disables both auto-saving for Quickboot snapshots and saving Quickboot
snapshots on exit. This reduces the chances that the Quickboot snapshot will be
unintentionally overwritten, and avoids slow fallback paths that do not use
file-backed Quickboot snapshots.

### QEMU 2.12

We have rebased our variant of QEMU from QEMU 2.9 to QEMU 2.12. This update
includes the following QEMU changes:

- <https://wiki.qemu.org/ChangeLog/2.10>
- <https://wiki.qemu.org/ChangeLog/2.11>
- <https://wiki.qemu.org/ChangeLog/2.12>

Here are some of the notable changes that impact the Android Emulator:

- x86: `gdbstub` now provides access to SSE registers.
- Disk images: Image locking is added and enabled by default. Multiple QEMU processes cannot write to the same image as long as the host supports OFD or posix locking, unless options are specified otherwise.
- `qemu-img: qemu-img resize` supports preallocation of the new parts of the image.
- QCOW2 shrinking now supported in `qemu` and `qemu-img`.

### Accessibility

- Fixed issues with screen readers and added better support for these tools in the Screen Record and Snapshot UI.
- Made the Quick Boot notification icons more accessible to users who are color blind.

### Graphics

- Fixed an out-of-bounds memory access issue that could occur for OpenGL ES vertex array pointers.
- Some older GPUs did not support OpenGL 2.1 or greater (which is required), or had other reliability issues. These issues could cause the emulator to crash on start, freeze, or be unusable on the default GPU setting. The emulator now automatically switches to the Swiftshader renderer if it detects that these GPUs are in use.
- Fixed an issue that caused the emulator to not post the correct framebuffer if `FBO != 0` was bound at the time of `eglSwapBuffers`.
- Fixed issue where the virtual Android display would only show up in the top left corner. We believe this was due to misconfigured Qt environment variables. The emulator now overrides all Qt scaling-related environment variables.
- Fixed an issue where the emulator crashed in some situations when loading GLES1 apps from a snapshot.
- Fixed concurrency issues in OpenGL and launching render threads that could result in double frees or corrupted data.
- Android Emulator now supports ASTC LDR compressed texture support (`GL_KHR_texture_compression_astc_ldr`) for system images that use API level 28 or higher.
- Most modern GPUs should now be able to launch the emulator with OpenGL ES 3.x enabled by default without using the `GLESDynamicVersion` feature flag.
- `-gpu guest` (software rendering in the guest) has been deprecated. System images for API level 28 or higher now automatically switch to using Swiftshader instead (`-gpu swiftshader_indirect`).
- If the emulator is launched from the command line using the `-no-window` flag, the default renderer is now Swiftshader.

### Location

- The emulator can now update bearing along with latitude and longitude position. The magnetometer virtual sensor adjusts itself dynamically to magnetic north by inferring motion when playing back a GPX or KML file.
- Device speed can now be set on the Location page.
- When playing back a GPX or KML file, the speed is set automatically, and is set to zero when the playback ends.
- The altitude is no longer restricted to being between -1,000 and +10,000 meters.
- Fixed an issue where the virtual GPS location would not be updated periodically unless the Extended Controls window was opened at least once.

### Camera

On Windows, more webcams are now supported because the emulator dynamically
resizes the camera frames that are delivered from the webcam. This feature also
prevents errors in frame delivery from causing the emulator to hang.

### Play Store

To address issues with running out of disk space on Play Store images, the
emulator now automatically resizes the userdata partition to 6 GB when running
with a fresh Play Store AVD.

### General quality improvements and fixes

- Some users reported that the emulator has been running slow. We identified one possible cause where the temp directory for the emulator ends up with too many stale files inside. As a workaround, the emulator no longer stores ADB liveness check files in that directory. However, it may also help to delete the contents of that folder. The folder is located in one of the following locations, depending on your operating system:
  - Windows: `C:\Users\<username>\AppData\Local\Temp\AndroidEmulator\*`
  - macOS or Linux: `/tmp/android-<username>/*`
- If the emulator is unable to start due to insufficient free RAM, an error message is now displayed. If you are on Windows and notice that there is RAM free, but you are still unable to start the emulator, the commit charge may have been exceeded. For help with this issue, see the [emulator Troubleshooting page](https://developer.android.com/studio/run/emulator-troubleshooting#windows_free_ram_and_commit_charge).
- The `-sysdir` command line option now properly overrides the inferred system image directory.
- Virtual modem now supports the model activity info `+MAI` query.
- Fixed various issues with memory leaks, memory corruption, and CPU usage. If you are experiencing crashes, memory leaks, or other high resource usage, please create an issue in [Issue Tracker](https://issuetracker.google.com/issues/new?component=192727&template=843117).
- Fixed an issue that reappeared on macOS 10.14 where using Bluetooth headsets with the emulator would degrade audio globally. To prevent this, the emulator now avoids using Bluetooth audio when running on macOS. ([Issue 37070892](https://issuetracker.google.com/issues/37070892))
- Fixed an issue on Windows where the emulator clock would not be in the correct timezone.
- Fixed emulator slowness and hangs on Linux systems with spinning harddrives (HDDs).
- Fixed some compile warnings that could lead to stack corruption on macOS.
- Fixed issues that could result in misleading reports of hanging.
- Fixed an issue with destroying thread pools that could cause a crash if one of the threads was not successfully created.
- Fixed an issue on macOS where timers would become unreliable, leading to hangs and other strange behavior. If you experience emulator hangs on macOS, please create an issue in [Issue Tracker](https://issuetracker.google.com/issues/new?component=192727&template=843117).
- Fixed an issue where closing the emulator would disable the UI, but not actually close the emulator.
- Fixed issues involving sporadic crashes, including an abort due to opening too many instances of `/dev/urandom`.
- Fixed an issue that caused the emulator to fail to start after the first time if ADB was terminated forcefully.
- The MIPS build has been removed. If you still require MIPS, please create an issue in [Issue Tracker](https://issuetracker.google.com/issues/new?component=192727&template=843117).
- Fixed an issue where ADB connections could become corrupt on snapshot load.
- Fixed an issue where the emulator window would have an afterimage or teleport offscreen when resuming a snapshot where the device orientation was different from the AVD's default orientation.
- Fixed issues involving crashes when saving snapshots.
- On Linux, btrfs filesystems can cause extreme slowdowns because the emulator automatically saves snapshots and uses copy-on-write for its virtual disk devices. We recommend cleaning out the `~/.android/avd` directory and running the following command on the empty `~/.android/avd` directory:

  ```
  chattr +C
  ```
  This creates new snapshots in a folder where copy-on-write is disabled.

### HAXM 7.3.2

We would like to mention HAXM 7.3.2 again because it must be installed in order
for recent system images to run properly on the emulator. HAXM 7.3.2 should
already be available in the Stable channel, and can also be installed manually
from <https://github.com/intel/haxm/releases>.

Here are a couple of the issues that this version of HAXM resolved:

- Fixed random crashes of guest OSes that use a recent Linux kernel (\>= 4.6). For example, Ubuntu 18.04 ([#39](https://github.com/intel/haxm/issues/39), [#74](https://github.com/intel/haxm/issues/74)).
- Fixed an x86 instruction emulator bug that could lead to a host crash ([#93](https://github.com/intel/haxm/issues/93)).

### 32-bit Windows deprecation

Due to low usage and high maintenance costs, we are planning to deprecate the
32-bit version of the Android Emulator that runs on Windows. We will roll out a
transition plan before removal and end-of-life for the 32-bit version of the
Android Emulator. However, we are actively seeking any feedback or concerns with
this future change.

Please let us know in [Issue Tracker](https://issuetracker.google.com/issues/new?component=192727&template=843117)
if you currently rely on the 32-bit version of the Android Emulator that runs on
Windows and tell us how we can best work with you going forward.

## 27.3.10 (August 2018)

This update includes the following bug fix:

### RAM size configuration fix

Some users reported that the emulator has been running slow. We identified one
possible cause where the AVD RAM size in the AVD's `config.ini` file was being
set incorrectly.

To mitigate this, the emulator increases the minimum RAM level for images that
use API level 26 or higher to the Android Studio default level of 1536 MB. If
your AVD's `config.ini` file is not listing `hw.ramSize` in megabytes,
please create an issue in [Issue Tracker](https://issuetracker.google.com/issues/new?component=192727&template=843117).
You can find the `config.ini` file in the following location:

`~/.android/avd/<avdname>.avd/config.ini`

## 27.3.9 (July 2018)

This update includes the following improvements and bug fixes:

### Improved error messages for Windows Hypervisor Platform

Some users were having difficulty diagnosing why the Windows Hypervisor Platform
(WHPX) failed to initialize when they activated a WHPX emulator. To help you
diagnose these issues, we have added more informative error messages. You can
enable these error messages by running the emulator from the command line using
the `-verbose` flag.
| **Note:** For users with Hyper-V based setups, you must enable the **Windows
| Hypervisor Platform** feature before you can activate a WHPX emulator. For more information, see [Configuring VM acceleration with Windows HypervisorPlatform](https://developer.android.com/studio/run/emulator-acceleration#vm-windows-hyperv-intel).

### General fixes

- Fixed OpenGL errors that occur when loading a snapshot in the camera app.

## 27.3.8 (July 2018)

This update includes several new features, improvements to existing features,
and bug fixes.

### Snapshots

You can now save multiple AVD snapshots for a given device configuration and
choose which of the saved snapshots to load when you start the emulator.

Starting with Android Studio 3.2 Canary 13, each device configuration includes
a control in the advanced settings in the Virtual Device Configuration dialog
with which you can you can specify which AVD snapshot to load when starting the
AVD.

To accommodate this expansion of the snapshot features, we have added a
**Snapshots** category to the **Extended controls** dialog. This new pane
contains controls for saving and loading AVD snapshots, including the controls
for saving and loading the quick-boot snapshot that had previously been in the
**Settings** pane.

You can edit the name and description of each saved snapshot.

For details, see [Snapshots](https://developer.android.com/studio/run/advanced-emulator-usage#snapshots).

### HAXM 7.2.0

HAXM 7.2.0 is now available in all channels.

This update includes bug fixes and improved support for large amounts of RAM.
Also, with this HAXM update and Emulator 27.3 and later, snapshots load their
contents into RAM on demand rather than loading the entire snapshot when the
virtual device starts. This change should greatly decrease the time needed to
load a snapshot.

For details, see [Configuring VM acceleration](https://developer.android.com/studio/run/emulator-acceleration#accel-vm).

## 27.2.9 (May 2018)

This update includes several new features, improvements to existing features,
and bug fixes.

### Screen recording

You can now record video and audio from the Android Emulator and save the
recording to a WebM or animated GIF file.

The screen recording controls are in the **Screen record** tab of the [**Extended
Controls**](https://developer.android.com/studio/run/advanced-emulator-usage#extended) window.

**Tip:** You can also open the screen recording controls by
pressing Control + Shift + R (Command + Shift + R on Mac).

To begin screen recording, click the **Start recording** button in the **Screen
record** tab. To stop recording, click **Stop recording**.

Controls for playing and saving the recorded video are at the bottom of the
**Screen record** tab. To save the video, choose **WebM** or **GIF** from the
menu at the bottom of the tab and click **Save**.

You can also record and save a screen recording from the emulator using the
following command on the command line:

`adb emu screenrecord start --time-limit 10 [path to save video]/sample_video.webm`

### Screenshots

You can take screenshots from the command line with either of the following
commands:

- `screenrecord screenshot [destination-directory]`
- `adb emu screenrecord screenshot [destination-directory]`

Screenshots are saved in PNG format.

### Virtual scene camera and ARCore

Developing and testing augmented reality apps (AR) with
[ARCore](https://developers.google.com/ar/discover/) is now even easier with the
new virtual scene camera, which allows you to experiment with your AR experience
within a virtual environment.

For information on using the virtual scene camera in the emulator, see
[Run AR apps in Android Emulator](https://developers.google.com/ar/develop/java/emulator).

### Google Play Store on Pixel device images

The Google Play Store is now enabled for Pixel and Pixel 2 device images. This
is indicated in the [AVD Manager](https://developer.android.com/studio/run/managing-avds) in Android Studio
3.2 and later with the Google Play logo in the **Play Store** column. AVDs with
Google Play Store enabled have a **Google Play** tab in the **Extended controls**
dialog that provides a convenient button for updating Google Play services on
the device.

### Snapshots

You can now load a [Quick Boot snapshot](https://developer.android.com/studio/run/emulator#quickboot)
without restarting the emulator. To load a snapshot, open the
[**Extended Controls**](https://developer.android.com/studio/run/emulator#extended) window to the **Settings**
page and click the **Load Now** button.

We have made many improvements to the loading and saving of snapshots to
improve efficiency of resource usage and to minimize the time that each
operation takes. If you still experience unusually long saves, please
[file an issue](https://issuetracker.google.com/issues?q=componentid:192727),
providing details of your CPU, RAM, and settings of any antivirus / firewall /
security software that is running.

### Rendering with Skia

When using images for API 27 or later, the emulator can render the Android UI
with [Skia](https://skia.org/), which can render more smoothly and efficiently.

For now, use of Skia requires that you explicitly enable it.

To enable Skia rendering, use the following commands in adb shell:

```
  su
  setprop debug.hwui.renderer skiagl
  stop
  start
```

<br />

### Camera

On Windows, Android Emulator now uses Media Foundation as the webcam back end,
which greatly improves performance and frame rate for webcam capture, up to 720p
30 FPS.

On Mac, you can now use webcam0 and webcam1 together.

### Miscellaneous

The `-phone-number-prefix` command-line option has been changed to
`-phone-number [number]`, which allows setting of the full
phone number.

You can now use alphanumeric SMS addresses.

### Fixes

- The Linux version of the Android Emulator is now built using a modern Clang C++ toolchain. This change fixes the issue of the emulator failing to start due to libGL and libstdc++ errors.
- Fixed several causes of crashes and hangs.
- To avoid crashes and hangs caused by not having enough free disk space, the emulator now checks for sufficient free disk space on startup, and will not start unless at least 2 GB is free.
- Fixed an issue that prevented some Unity games from rendering.
- Fixed DNS issue that caused the emulator to be unable to connect to the network.
- Fixed an issue that caused changes to the internal storage allocated to an AVD through the Virtual Device Configuration dialog to not work.
- Fixed an issue of many adb processes being created and not properly shut down.
- Fixed an issue that caused the rotate buttons and other parts of the UI to become unresponsive unless the Extended controls window was open.
- Fixed an issue that caused copy and paste from the host to not work unless the Extended controls dialog was opened at least once.
- The frameless emulator's resize rectangle has been updated to better follow the emulator's visual theme.
- Telephone and SMS are now properly deactivated when airplane mode is on.
- Fixed an issue that caused SMS and cellular functionality to be disabled after loading a snapshot.
- You will no longer receive false warning messages saying `"Unable to open... \pstore.bin. Permission denied."`
- Fixed an issue that prevented re-positioning the AVD on some Mac screens.
- Fixed issues with flickering and blank screens on newer MacBook Pro computers when running AVDs with Pixel 2 XL skins.
- Fixed issues with blank screens when switching into zoomed mode while a frameless emulator was active.
- Fixed an issue that caused the device skin and emulator contents to scroll out of sync when zoomed in.

If you are still experiencing hangs or other instabilities, please
[file an issue](https://issuetracker.google.com/issues?q=componentid:192727).

## 27.1.12 (March 2018)

This update includes fixes for the following issues:

- Bluetooth audio quality degraded after starting the emulator. ([Issue 37095756](https://issuetracker.google.com/issues/37095756))
- Locations sent to one emulator were sent to all of them. ([Issue 73450633](https://issuetracker.google.com/issues/73450633))
- GPS location set using the console was overridden by values set using **Extended Controls \> Location** in the graphical user interface. ([Issue 73471760](https://issuetracker.google.com/issues/73471760))

If you are still experiencing hangs or other instabilities, please
[file an issue](https://issuetracker.google.com/issues?q=componentid:192727).

With this update, a current system image, and a preview version of Android
Studio, you can use Android Emulator to run augmented reality applications built
with ARCore. For detailed requirements and instructions, see
[Run AR apps in Android Emulator](https://developers.google.com/ar/develop/java/emulator).

## 27.1.10 (February 2018)

- Camera capture resolution

  720p frames can now be captured from an attached webcam.

  To work with Android 8.1 (API level 27) and higher system images, any
  attached webcam must have the capability to capture 720p frames.
- Fixes

  - Fixed an issue that caused webcam capture to sometimes output a distorted or all-green image.
  - Fixed an issue that made it possible to see the following message even when there was no actual hang: "emulator: ERROR: detected a hanging thread 'Qt event loop'. No response for 15000 ms".

If you are still experiencing hangs or other instabilities, please
[file an issue](https://issuetracker.google.com/issues?q=componentid:192727).

## 27.1.7 (February 2018)

- Frameless emulator window:

  By default, emulators with device skin files are now shown without a
  surrounding window frame. To show the surrounding window frame, enable
  **Show window frame around device** in the Settings pane of the [Extended
  Controls](https://developer.android.com/studio/run/emulator#extended) window.
- Quick Boot improvements to make working with AVD snapshots more efficient:

  - You can save an AVD snapshot at any time using the **Save Now** button in the Settings pane of the [Extended Controls](https://developer.android.com/studio/run/emulator#extended) dialog box.
  - The emulator reduces the time that it takes to save a snapshot in many cases by saving only the difference between the current state and the previously saved snapshot.

  For details, see the [Quick Boot](https://developer.android.com/studio/run/emulator#quickboot)
  documentation.
- The emulator has been updated to use QEMU 2.9.

  Some notable improvements include the following:
  - Optimized I/O and finer-grained I/O thread locking for greater performance.
  - Fixed bugs since QEMU 2.8 (26.1.4).
  - New implementation of the HAXM back end.

  See the full list of changes in the [QEMU 2.9 change log](https://wiki.qemu.org/ChangeLog/2.9).
- Swiftshader implementation conforming to OpenGL ES 3.0:

  The emulator's Swiftshader renderer now conforms fully with OpenGL ES 3.0.
  For details of the Swiftshader renderer, see the **Settings \> Advanced**
  section of [Extended Controls](https://developer.android.com/studio/run/emulator#extended).
- Fixes

  - Fixed an issue where clipboard sharing was not working unless the **Enable
    clipboard sharing** option was toggled off and on.
  - Fixed a hang when using the Swiftshader rendering back end with low-resolution AVDs.

## 27.0.5 (January 2018)

- ANGLE for rendering on Windows is now disabled by default.

  If ANGLE works better for you, you can re-enable it with command line
  flag `-gpu angle_indirect`. Or, open the Extended controls window, navigate
  to **Settings \> Advanced** , and select **ANGLE D3D11** for
  the OpenGL ES renderer setting.
- Fixed an issue where Shift+B does not type a capital B character.

## 27.0.2 (December 2017)

- New Quick Boot feature provides faster emulator start times, based on a
  snapshot of your AVD instance.

  Quick Boot is enabled by default for all AVDs. Although the first time you
  start an AVD it must perform a cold boot (just like powering on a device),
  all subsequent starts are fast and the system is restored to the state at
  which you closed the emulator (similar to waking a device).

  If you want to control when the emulator saves a snapshot, open the
  emulator's [Extended controls window](https://developer.android.com/studio/run/emulator#extended)
  and click **Settings** . Here, you can select one of the following settings
  for **Save quick boot state on exit**:
  - **Yes**: Always save quick boot snapshot when you close the emulator. This is the default.
  - **No**: Never save quick boot snapshot; always perform a cold boot.
  - **Ask**: Prompt whether or not to save quick boot snapshot when you close the emulator.

  Your selection applies only to the currently open AVD.

  For more information, see the [Quick Boot documentation](https://developer.android.com/studio/run/emulator#quickboot).
- Added support for Mac OpenGL ES 3 (for system images using API level 24 and
  higher, Google APIs, and the x86 ABI).

- For added stability in OpenGL ES 2+ apps, emulator now uses OpenGL core
  profile if available.

- New options for rendering with Swiftshader / ANGLE:

  - `-gpu swiftshader_indirect`: Faster, more stable variant of Swiftshader that works with Quick Boot.
  - `-gpu angle_indirect` (Windows only): More stable variant of ANGLE D3D that also works with Quick Boot.

  The older `-gpu swiftshader` and `-gpu angle` options are now deprecated.
  In the Extended controls window, the "SwiftShader" and "ANGLE" options for
  the OpenGL ES renderer setting in **Settings \> Advanced** now use the
  `*_indirect` variants.
- Various other bug fixes.

## 26.1.4 (August 2017)

This is a minor release with bug fixes and the following
improvements to GPU configuration:

- Enable boot animation when running on ANGLE renderer
- Disable GLES3 when running on ANGLE renderer

## 26.1.3 (August 2017)

This is a minor release with bug fixes, performance improvements, and small
feature changes.

- This version is now required to use the latest Android 8.0 system images. They are [Treble-compliant](https://android-developers.googleblog.com/2017/05/here-comes-treble-modular-base-for.html), featuring separate `vendor.img` partitions.
- New HAXM 6.2.0 now available (check the SDK Manager) and includes the following updates:
  - Improved memory usage. The peak working set of memory pinned by HAXM is no longer equal to the size of the AVD's RAM; instead, memory is paged in on demand. This should help the emulator run more reliably on machines with lower amounts of RAM.
  - The emulator with HAXM 6.2.0 can now boot faster on macOS, skipping a lengthy initialization phase.
- Improvements to GPU configuration
  - Fixed issues with black screen on boot when performing guest-side software rendering by falling back to host-side software rendering with Swiftshader. Latest revisions of system images for API levels 19 - 25 with Google APIs should have working guest-side rendering.
  - Fixed an issue where the emulator was switched to a software renderer due to detecting the presence of older Intel GPUs, but the emulator was actually running on a discrete GPU. Which GPUs will be switched to use ANGLE or Swiftshader rendering is determined as follows:
    - Older Intel iGPUs have driver issues on both OpenGL and ANGLE D3D drivers. Users with Intel HD Graphics 3xxx and older will use Swiftshader.
    - Some users reported the inability to use API level 25 images because of a bug in which "Pixel Launcher keeps stopping." This seems to be a driver issue in some Intel HD 4xxx models. So they will be switched to use ANGLE automatically.
  - For best results with GPU emulation, we recommend either to use a discrete NVIDIA or AMD GPU, or a newer Intel GPU (Iris, HD 5xxx, HD 5xx/6xx).
  - Fixed an issue where the emulator would fail to start (OpenGL emulation failed to initialize) if the AVD was configured with `hw.gpu.mode=host` and the emulator was launched in a remote desktop client.
  - Clarified "OpenGL ES API level (requires restart)" settings; added an option to downgrade from OpenGL ES 3 to OpenGL ES 2 if experiencing issues or needing to test on lower OpenGL ES API levels.
  - Mesa renderer is deprecated; `hw.gpu.mode=mesa` will now be automatically switched to use Swiftshader on the host.
- Improvements for macOS:
  - The emulator is now fully compatible with macOS 10.13 High Sierra through either Hypervisor.Framework or HAXM 6.2.0.
  - Hypervisor.framework is now enabled by default on macOS for 32-bit x86 images to improve performance and macOS compatibility. If you experience issues with it specifically, please file a bug report and append `HVF = off` to `~/.android/advancedFeatures.ini` (create this file if it doesn't exist).
  - Fixed issues with no internet / failure to attach debugger while using Hypervisor.framework.
  - To enhance compatibility and performance of webcam capture, the QTKit-based camera capture has been replaced with a buffered one based on AVFoundation.
- Added support for Wi-Fi in some system images (currently only API level 25). An access point called "AndroidWifi" is available and Android automatically connects to it. Wi-Fi support can be disabled by running the emulator with the command line parameter `-feature -Wifi`.
- Some users raised the concern that the fixed-size Play Store system images did not have sufficient storage. As such, we've increased the size to 2 GB by default (up from 800 MB).
- Added a keyboard shortcut (Ctrl+Shift+U) to open the bug reporting UI page directly from the settings page.
- Fixed an issue where if an older CPU with Intel x86 EPT but without UG was used, the emulator would fail to boot if more than one core was configured.
- Fixed an issue where HyperV would be improperly detected if the emulator was itself running in a Xen hypervisor.
- Fixed an issue where the emulator would crash on start in some Linux configurations.

## 26.1.2 (July 2017)

This release includes new features and performance improvements.

- Added the ability to define a custom HTTP proxy configuration in the
  extended controls (click **More** ![](https://developer.android.com/static/studio/images/buttons/emulator-extended-controls.png),
  and then click **Settings** and
  **Proxy**). By default, the emulator uses the Android Studio HTTP proxy
  settings, but this screen allows you to define a manual proxy configuration.

  ![](https://developer.android.com/static/studio/images/run/emulator-proxy-settings_2x.png)
- Added VNC support for guest mode GPU so emulator can be remotely viewed and
  controlled. For example, you can launch the emulator and let VNC listen to
  port 5901 as follows:

  1. Execute: `emulator -gpu guest -avd avd_name
     -no-window -qemu -vnc :1`
  2. Open a VNC viewer, such as tightvnc viewer, to connect to port 5901.

     - To use Mac's built-in screen sharing client, a VNC password is
       required when launching the emulator. To set a password, use this
       command:

       `emulator -gpu guest -avd avd_name -no-window -qemu
       -vnc :1,password -monitor stdio`

       And then enter `change vnc password` into the console, and enter a
       password.

  Android O is not currently supported for VNC mode.
- Added a **File a bug** button in the extended controls Help screen
  (Click **More** ![](https://developer.android.com/static/studio/images/buttons/emulator-extended-controls.png),
  and then click **Help** and **Emulator help** ). Clicking **File a bug**
  opens a dialog where you can see the bug report details such as the
  screenshot, the AVD configuration info,
  and a bug report log. You can then save the report for yourself or
  [report emulator issues](https://developer.android.com/studio/report-bugs#emulator-bugs).

- Added gyroscope sensor to emulator and virtual sensors panel. This requires
  a system image with gyroscope support to work (currently API level 24
  and 25).

- Added host-preferred DNS to Qemu DNS list on Windows, when multiple virtual
  network interfaces on the host introduce multiple DNS addresses which are
  not functional for the emulator.

- Added experimental macOS Hypervisor.Framework support for 32-bit x86 images
  on macOS 10.10+ through server flags, which should improve boot time and
  performance.

  - If you experience problems with it, add the line `HVF = off` in `~/.android/advancedFeatures.ini`.
- OpenGL ES 3.x is now enabled by default for system images and host GPUs that
  support OpenGL ES 3. Currently, only Android O (API level 26) and
  Windows/Linux hosts support OpenGL ES 3.

  - If you experience problems with OpenGL ES 3, add the line `GLESDynamicVersion = off` in `~/.android/advancedFeatures.ini`.
- Emulator now uses offscreen OpenGL FBOs for all rendering except final
  display image posting, which should help with color consistency issues
  across platforms.

- After collecting data on sudden emulator slowdown issues, we have determined
  that the problem may have to do with some interaction between older Intel
  OpenGL drivers and Windows updates. As such, users with Intel HD 4000, 3000,
  2000 (and related GPUs) now have rendering set by default to either a D3D
  renderer (ANGLE) or Swiftshader (software renderer).

## 26.0.0 (March 2017)

<br />

This release is compatible with API level 26. It also includes a number of
performance improvements and bug fixes.

<br />


**Minor revision 26.0.3 (May 2017)**

- Adds online-updateable feature flags for quickly addressing issues stemming from problematic hardware configurations. This allows Google to roll out fixes and features that are dependent on user configurations by updating server-side flags. If you notice issues with specific hardware, please [report a bug](https://developer.android.com/studio/report-bugs) so we can investigate the problem.
- New support for [rotary
  input](https://developer.android.com/training/wearables/ui/rotary-input) for Android Wear API level 25 system images. To emulate the rotary input dial on a Wear device, click the **Rotary Input** tab on the extended window.
- The Crash Reporting dialog is now resizable and no longer resets **When to send crash reports** to **Ask** without input.
- The 32-bit emulator now requires that the maximum AVD RAM size be less than or equal to 512 MB, in order prevent the emulator from running out of room in the 2 GB virtual address space.
- Adds support for absolute paths in emulator images.
- Adds a new tab in the extended window for Google Play Store images that displays the Play Services version and a button to check for updates to Play Services.
- Adds a dropdown to select the OpenGL renderer on the Emulator Settings page. If you are experiencing issues with the OpenGL driver on a Windows machine, try using the ANGLE (D3D11) or ANGLE (D3D9) options (requires a restart). If you are experiencing issues with the OpenGL driver on a non-Windows machine, try using the Swiftshader software renderer (requires a restart).
- Fixes a rare crash on exit when the emulator receives both `exit` and `minimize` commands.
- Fixes a scaling issue when changing displays on a Mac machine. ([Issue
  268296](https://code.google.com/p/android/issues/detail?id=268296))
- Fixes an issue where the emulator takes 300% of the CPU and holds it after resuming the host computer from sleep or when the emulator has been running for a long time.
- Fixes a crash when the emulator is shutting down.
**Updates with HAXM v6.1.1 (March 2017)**

**Note:** HAXM v6.1.1 is available for Mac
users through the [SDK
Manager](https://developer.android.com/studio/intro/update#sdk-manager) as of March 30th, and will be available for Windows users soon.

Version 26.0.0 of the Android Emulator supports HAXM v6.1.1, which
includes the following updates:

- Enables Performance Monitoring Units (PMU) emulation. ([Issue 223377](http://b.android.com/223377))
- Fixes coexistence with VirtualBox and Docker on Macs. ([Issue 197915](http://b.android.com/197915))
- Revises the installation error message displayed when the installer fails to detect Intel VT-x on Windows, usually because Hyper-V is enabled.
- Adds support for accelerating the Android Emulator in a Hyper-V-based Windows VM. This update requires that the host Hyper-V instance (the one that manages the Windows VM/guest) use the latest version of Hyper-V with nested virtualization enabled. Hyper-V must be *disabled* in the guest Hyper-V instance (the Windows VM).

### Dependencies

- Android SDK Platform-Tools revision 25.0.4 or later.
- Android SDK Tools revision 26.0.0 or later.

### New features and bug fixes

- Compatible with API level 26.
- Fully GLES 2.0 compliant. Given a host GPU that has conformant desktop OpenGL drivers, the emulator now passes 100% of the Android CTS dEQP-GLES2 [`mustpass`
  list](https://source.android.com/devices/graphics/cts-integration.md). This has been released for API level 24 x86 images (revision 11 and higher) and will soon be included for all system images.
- Improved video playback performance. The emulator now stores all video color buffers in host/guest shared memory and performs necessary final YUV to RGB conversion in the GPU. 1080p30 should be well within reach of most systems now. This has been released for API level 24 x86 images (revision 11 and higher) and will soon be included for all system images.
- The emulator now correctly unregisters itself from the `adb
  devices` list on exit and closes open TCP ports on Linux machines.
- adb connections are now more reliable. A running emulator is detected faster and doesn't go into "offline" or "unauthorized" status anymore.

## 25.3.0 (March 2017)

As of this release, the Android Emulator will be released separately from
the SDK Tools. This release contains a variety of performance
improvements, new features, and bug fixes.

<br />

**Minor revision 25.3.1 (March 2017)**

- Fixed a crash occurring on some GPU configurations by disabling GLAsyncSwap by default. This feature was added in 25.3.0 to improve frame timing and frames per second for games and video, but causes the emulator to fail on some unknown machine configurations. You can manually enable it by opening the `android_sdk/emulator/lib/advancedFeatures.ini` file and setting `GLAsyncSwap = on`.

<br />

### Dependencies

- Android SDK Platform-Tools revision 24 or later.
- Android SDK Tools revision 25.3.0.

### New features and bug fixes

- Updated emulation engine to QEMU 2.7, including all recent bug fixes, improved performance, and new features.
- New IPv6 support.
- The emulator now uses SwiftShader as a pure software renderer on the host.
- Android Pipe performance improvements: Android Pipe, the main communication channel between the emulator and Android OS, is now an order of magnitude faster, has lower latency and offers better multi-threaded performance. This causes a number of performance improvements for the emulator, including:
  - Improved ADB push/pull speed.
  - Better 3D acceleration support.
  - Increased overall responsiveness of the emulator.
  - Improved graphics performance.
- The emulator now uses GPU-side buffers (glBindBuffers / glBufferData) when the guest requests them, decreasing CPU overhead in some apps.
- Improved audio support.
- Faster disk I/O: The emulator now uses separate threads to dispatch disk I/O, resulting in lower latency and better throughput (\~1.5x sequential I/O speed, \~5x random access I/O speed). This also reduces the number of flushes to disk, resulting in much lower physical device load.
- The emulator now uses sparse files for disk boots on Windows machines, speeding up both first boot and "wipe-data" boots. When creating or resetting an AVD, the emulator now writes 100-200 MB of data to disk, instead of 2 GB or more.
- Various GUI enhancements:
  - The emulator now uses Qt 5.7.0, which includes bug fixes and performance improvements.
  - UI initialization no longer attempts to load all emulator executables as Qt plugins, so it's dramatically shorter, especially on HDDs.
  - UI interactions are now faster and smoother, including rotation, window resizing, and extended controls window loading and closing.

*** ** * ** ***

OpenXR™ and the OpenXR logo are trademarks owned
by The Khronos Group Inc. and are registered as a trademark in China,
the European Union, Japan and the United Kingdom.