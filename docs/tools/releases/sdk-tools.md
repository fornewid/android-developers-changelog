---
title: https://developer.android.com/tools/releases/sdk-tools
url: https://developer.android.com/tools/releases/sdk-tools
source: md.txt
---

# SDK Tools release notes

| **Note:** This SDK Tools package is deprecated and no longer receiving updates. Instead, use the new[Android SDK Command-Line tools](https://developer.android.com/studio#cmdline-tools)package. For updates on the new command-line tools package, see the[Android SDK Command-Line Tools release notes](https://developer.android.com/studio/releases/cmdline-tools).
|
| In addition, we are discontinuing an old way of updating artifacts for the SDK manager. This change only affects Android Studio 2.2 and lower. Going forward, we will no longer publish updates with this older XML format. Users of older versions of Android Studio, the old command-line SDK Manager, or the old SDK Manager UI will not receive updates to the SDK components via the SDK Manager. Although your current builds should continue to work, if you'd like to update SDK components, use the new[command-line tools](https://developer.android.com/studio#cmdline-tools).
|
| If you install Android Studio 2.2 or lower, you won't be able to re-download the components. In order to download components via the SDK manager, upgrade to a newer version of Android Studio.

Android SDK Tools is a component for the Android SDK. It includes development and debugging tools for Android.

## Revisions

The sections below provide notes about successive releases of the SDK Tools, as denoted by revision number. To ensure you have the latest version, check[SDK Manager](https://developer.android.com/studio/intro/update#sdk-manager)for updates.
SDK Tools, Revision 26.1.1*(September 2017)*

Changes:
:
    - A command-line version of the Apk Analyzer has been added in`tools/bin/apkanalyzer`. It offers the same features as the Apk Analyzer in Android Studio and can be integrated into build/CI servers and scripts for tracking size regressions, generating reports, and so on.
    - ProGuard rules files under tools/proguard are no longer used by the Android Plugin for Gradle. Added a comment to explain that.
SDK Tools, Revision 26.0.2*(April 2017)*

Changes:
:
    - When creating an AVD with`avdmanager`, it is no longer necessary to specify`--tag`if the package specified by`--package`only contains a single image (as is the case for all images currently distributed by Google).
SDK Tools, Revision 26.0.1*(March 2017)*

Changes:
:
    - Hierarchy Viewer and Pixel Perfect tools returned to[Android Device Monitor](https://developer.android.com/studio/profile/monitor)(the command-line versions are still removed, as of revision 25.3.0)
SDK Tools, Revision 26.0.0*(March 2017)*

Dependencies:
:
    - Android SDK Platform-Tools revision 24 or later.

Changes:
:
    - `tools/android`now attempts to reproduce the functionality of`android`in tools prior to version 25.3.0 by invoking the new tools.
      - All`avd`,`target`, and`device`commands should work as before.
      - `sdk`commands will be translated to similar commands using`tools/bin/sdkmanager`on a best-effort basis.
    - `tools/bin/avdmanager`now supports the`list target`command.
SDK Tools, Revision 25.3.0*(March 2017)*

Dependencies:
:
    - Android SDK Platform-Tools revision 24 or later.

Changes:
:
    - Android Emulator is removed from this package and moved to a different SDK directory. See the new[Android Emulator Release Notes](https://developer.android.com/studio/releases/emulator). This change is backward compatible with older Android Studio versions.
    - `android avd`command-line functionality replaced with new[`avdmanager`](https://developer.android.com/studio/command-line/avdmanager)tool.
    - Obsolete/deprecated tools have been removed:
      - `android`
      - `ddms`(instead see[Using DDMS](https://developer.android.com/studio/profile/ddms))
      - `draw9patch`(instead see[Draw 9-patch](https://developer.android.com/studio/write/draw9patch))
      - `hierarchyviewer`(instead see[Profile Your Layout with Hierarchy Viewer](https://developer.android.com/studio/profile/hierarchy-viewer))
      - `traceview`(instead see[Profiling with Traceview and dmtracedump](https://developer.android.com/studio/profile/traceview))
      - `ant`scripts
      - Project and activity templates
    - Executables have been moved to`bin/`:
      - `jobb`
      - `lint`
      - `monkeyrunner`
      - `screenshot2`
      - `Uiautomatorviewer`
    - Enhanced[`sdkmanager`](https://developer.android.com/studio/command-line/sdkmanager):
      - View and accept all licenses from the command line
      - Improved verbose-mode package list
SDK Tools, Revision 25.2.5*(January 2017)*

Dependencies:
:
    - Android SDK Platform-Tools revision 24 or later.

Android Emulator bug fixes:
:
    - Fixed a crash on async socket reconnect.
    - Fixed a crash on Mac when`glDeleteTextures()`is called after the corresponding context was destroyed.
SDK Tools, Revision 25.2.4*(December 2016)*

Dependencies:
:
    - Android SDK Platform-tools revision 24 or later.

Android Emulator bug fixes:
:
    - Fixed a crash in gles pipe when accessing a closed one.
    - Fixed a rare crash if emulator is closed during location loading.
SDK Tools, Revision 25.2.3*(November 2016)*

Dependencies:
:
    - Android SDK Platform-tools revision 24 or later.

Added new[`sdkmanager`](https://developer.android.com/studio/command-line/sdkmanager)command line tool to view, install, update, and uninstall individual Android SDK packages.
New Android Emulator features and bug fixes:
:
    - Fixed`-gpu guest`([issue 227447](https://code.google.com/p/android/issues/detail?id=227447)).
    - Added support for WebP image decoding.
    - Added support for ETC2 texture decompression.
SDK Tools, Revision 25.2.2*(September 2016)*

Dependencies:
:
    - Android SDK Platform-tools revision 23 or later.

New Android Emulator features:
:
    - Added new**Virtual** **Sensors** and**Cellular** \>**Signal Strength**extended controls.
    - Added an**LTE** option to the**Cellular** \>**Network type**extended controls.
    - Added simulated vertical swipes for scrolling through vertical menus with a mouse wheel.
SDK Tools, Revision 25.1.6*(May 2016)*

Dependencies:
:
    - Android SDK Platform-tools revision 23 or later.

General Notes:
:
    - To improve the security of the Android Emulator and to address a reported security vulnerability, the Android Emulator Console now requires[authentication](https://developer.android.com/studio/run/emulator-commandline#console-session)before you can enter commands. Enter the`auth `*auth_token*command after you`telnet`to an emulator instance.*auth_token*must match the contents of the`.emulator_console_auth_token`file in your home directory.
SDK Tools, Revision 25.0.0*(April 2016)*

**Android Emulator 2.0**:
:
    - Performance improvements:
      - Emulator now uses CPU acceleration on x86 emulator system images by default.
      - Added[SMP](https://developer.android.com/training/articles/smp)support to take advantage of host multi-core architecture when emulating Android 6.0 (API level 23) or higher, resulting in much better performance and speed than the physical counterpart. Also with SMP support, you can test apps that specifically target multi-core Android devices.
      - Improved data and APK push-pull protocol between the[Android Debug Bridge](https://developer.android.com/tools/help/adb)and devices running Android 5.0 (API level 21) or higher. See speed improvements up to five times faster than using a physical device.
    - Extended UI controls and a floating toolbar provide easy access to features previously available only through the command line, such as taking screen captures, adjusting the battery level, rotating the screen, and managing virtual calls.
    - Upload KML and GPX files to play back a set of custom location points.
    - Dynamically resize the emulator by dragging a corner or zoom into the emulator window.
    - Install APKs or add media files to the emulator's internal SD card by dragging and dropping files into the emulator window.
    - Simulate multi-touch input. While interacting with the emulator screen, enter multi-touch mode by holding down the**Ctrl** key on Windown/Linux, or**Command**key on Mac OSX.
    - The Android Emulator works best with Android Studio 2.0. To find out more about what's included in the newest version of the official Android IDE,[read the release notes](https://developer.android.com/tools/revisions/studio#Revisions).
    - Read the documentation to find out more about[using the Android Emulator](https://developer.android.com/tools/devices/emulator).
SDK Platform-tools, Revision 23.1.0*(December 2015)*

General Notes:
:
    - Changed Linux requirements for Android SDK Platform-tools revision 23.1.0 and later: it now requires 64-bit Linux.
SDK Tools, Revision 24.4.1*(October 2015)*

Dependencies:
:
    - Android SDK Platform-tools revision 23 or later.

General Notes:
:
    - Fixed a problem where the emulator title bar was hidden off screen. ([Issue 178344](http://code.google.com/p/android/issues/detail?id=178344))
    - Enabled the emulator to resize the user data partition by including e2fsprogs binaries. ([Issue 189030](http://code.google.com/p/android/issues/detail?id=189030))
    - Fixed a regression on the 32-bit Windows OS where the emulator fails to boot Android 6.0 (API level 23) through Android 5.0 (API level 21) system images. ([Issue 188326](http://code.google.com/p/android/issues/detail?id=188326))
SDK Tools, Revision 24.4.0*(October 2015)*

Dependencies:
:
    - Android SDK Platform-tools revision 23 or later.

General Notes:
:
    - Updated the emulator so it can display an upgrade notification when a new version is available.
    - Added the ability for the emulator to send basic crash reports. You*must*opt-in through Android Studio preferences to enable crash report transmission.
SDK Tools, Revision 24.3.4*(August 2015)*

Dependencies:
:
    - Android SDK Platform-tools revision 23 or later.

General Notes:
:
    - Added support for Android 6.0 (API level 23) platform.

Emulator:
:
    - Improved emulator performance on multi-core Windows desktops. ([Issue 101040](http://b.android.com/101040))
    - Added support for GPU emulation on Windows and Linux platforms using the`-gpu mesa`command line option.
    - Enabled support for running emulators with GPU emulation through remote desktop services, including Chrome Remote Desktop, Windows Terminal Services, and NoMachine.
    - Added support for emulators with 280 dpi and 360 dpi screen resolutions.
    - Improved support for GLES 2.0 extensions.
    - Fixed several issues with GPU emulation support.
    - Added support for setting the storage size on emulators using Android 4.4 (API level 19) and higher. ([Issue 75141](http://b.android.com/75141))
    - Fixed problem with sending long SMS messages between emulators. ([Issue 3539](http://b.android.com/3539))
    - Fixed issue with emulator getting incorrect time from location objects. ([Issue 27272](http://b.android.com/27272))
    - Added handling for unusual characters in paths and file names when starting emulators. ([Issue 35889](http://b.android.com/35889))
SDK Tools, Revision 24.3.3*(June 2015)*

Dependencies:
:
    - Android SDK Platform-tools revision 19 or later.

General Notes:
:
    - Fixed issues with using Ant build tasks with the Eclipse ADT build structure.
    - Fixed the emulator boot problem on Mac OS X 10.8.5.
SDK Tools, Revision 24.3.2*(June 2015)*

Dependencies:
:
    - Android SDK Platform-tools revision 19 or later.

General Notes:
:
    - Fixed issues with the ARM 64-bit emulator.
SDK Tools, Revision 24.3.1*(June 2015)*

Dependencies:
:
    - Android SDK Platform-tools revision 19 or later.

General Notes:
:
    - Fixed issue with the`root/`and`lib/`folders.

    **Caution:**This release is known to contain issues which prevent builds from completing. We strongly recommend that you update to SDK Tools 24.3.2 as soon as possible.
SDK Tools, Revision 24.3.0*(June 2015)*

Dependencies:
:
    - Android SDK Platform-tools revision 19 or later.

General Notes:
:
    - Fixed several minor emulator issues.

    **Caution:**This release is known to contain issues which prevent builds from completing. We strongly recommend that you update to SDK Tools 24.3.2 as soon as possible.
SDK Tools, Revision 24.2.0*(May 2015)*

Dependencies:
:
    - Android SDK Platform-tools revision 19 or later.

General Notes:
:
    - Fixed several minor emulator issues.
SDK Tools, Revision 24.1.2*(February 2015)*

Dependencies:
:
    - Android SDK Platform-tools revision 19 or later.

General Notes:
:
    - Fixed boot failures of MIPS system images on Mac OS X.
    - Fixed AVD screen capture issues when using GPU emulation.
    - Fixed memory leaks in emulator system.
SDK Tools, Revision 24.0.2*(December 2014)*

Dependencies:
:
    - Android SDK Platform-tools revision 19 or later.

General Notes:
:
    - Fixed issue with creating projects and activities from templates using Eclipse ADT.
SDK Tools, Revision 24.0.1*(December 2014)*

Dependencies:
:
    - Android SDK Platform-tools revision 19 or later.

General Notes:
:
    - Fixed Java detection issue on 32-bit Windows systems.
SDK Tools, Revision 24.0.0*(December 2014)*

Dependencies:
:
    - Android SDK Platform-tools revision 19 or later.

General Notes:
:
    - Added support for Android Studio 1.0 and emulator enhancements.
SDK Tools, Revision 23.0.5*(October 2014)*

Dependencies:
:
    - Android SDK Platform-tools revision 19 or later.
    - If you are developing in Eclipse with ADT, note that this version of SDK Tools is designed for use with ADT 23.0.4 and later. If you haven't already, update your ADT Plugin to 23.0.4.
    - If you are developing outside Eclipse, you must have[Apache Ant](http://ant.apache.org/)1.8 or later.

General Notes:
:
    - Fixed Windows 32-bit compilation issue.
SDK Tools, Revision 23.0.4*(October 2014)*

Dependencies:
:
    - Android SDK Platform-tools revision 19 or later.
    - If you are developing in Eclipse with ADT, note that this version of SDK Tools is designed for use with ADT 23.0.4 and later. If you haven't already, update your ADT Plugin to 23.0.4.
    - If you are developing outside Eclipse, you must have[Apache Ant](http://ant.apache.org/)1.8 or later.

General Notes:
:
    - Fixed duplicate devices in AVD for Wear and TV.
SDK Tools, Revision 23.0.2*(July 2014)*

Dependencies:
:
    - Android SDK Platform-tools revision 19 or later.
    - If you are developing in Eclipse with ADT, note that this version of SDK Tools is designed for use with ADT 23.0.2 and later. If you haven't already, update your ADT Plugin to 23.0.2.
    - If you are developing outside Eclipse, you must have[Apache Ant](http://ant.apache.org/)1.8 or later.

General Notes:
:
    - Added ProGuard`.bat`files that were missing.
    - Added the`proguard-android.txt`file that was missing.
    - Renamed the`lombok-ast-0.2.2.jar`file to`lombok-ast.jar`, which should allow running lint from the command line.
SDK Tools, Revision 23.0.0*(June 2014)*

Dependencies:
:
    - Android SDK Platform-tools revision 19 or later.
    - If you are developing in Eclipse with ADT, note that this version of SDK Tools is designed for use with ADT 23.0.0 and later. If you haven't already, update your ADT Plugin to 23.0.0.
    - If you are developing outside Eclipse, you must have[Apache Ant](http://ant.apache.org/)1.8 or later.

General Notes:
:
    - Added the Android Wear tools and system images.
SDK Tools, Revision 22.6.4*(June 2014)*

Dependencies:
:
    - Android SDK Platform-tools revision 18 or later.
    - If you are developing in Eclipse with ADT, note that this version of SDK Tools is designed for use with ADT 22.6.3 and later. If you haven't already, update your ADT Plugin to 22.6.3.
    - If you are developing outside Eclipse, you must have[Apache Ant](http://ant.apache.org/)1.8 or later.

General Notes:
:
    - Fixed an issue with the x86 emulator that caused Google Maps to crash. ([Issue 69385](http://b.android.com/69385))
    - Fixed minor OpenGL issues.
SDK Tools, Revision 22.6.3*(April 2014)*

Dependencies:
:
    - Android SDK Platform-tools revision 18 or later.
    - If you are developing in Eclipse with ADT, note that this version of SDK Tools is designed for use with ADT 22.6.3 and later. If you haven't already, update your ADT Plugin to 22.6.3.
    - If you are developing outside Eclipse, you must have[Apache Ant](http://ant.apache.org/)1.8 or later.

General Notes:
:
    - Fixed a problem where the AVD manager allowed creating Android Wear virtual devices with a target API Level lower than 19.
    - Fixed the description of Android Wear system images in the SDK Manager.

Known Issues:

:   When you create an Android Wear virtual device in the AVD manager, a target API Level lower than 19 may be selected by default. Make sure you select the target API Level 19 when creating Android Wear virtual devices.

SDK Tools, Revision 22.6.2*(March 2014)*

Dependencies:
:
    - Android SDK Platform-tools revision 18 or later.
    - If you are developing in Eclipse with ADT, note that this version of SDK Tools is designed for use with ADT 22.6.2 and later. If you haven't already, update your ADT Plugin to 22.6.2.
    - If you are developing outside Eclipse, you must have[Apache Ant](http://ant.apache.org/)1.8 or later.

General Notes:
:
    - Fixed a problem where the SDK Manager threw a`NullPointerException`after removing a virtual device that was created using the Android Wear system image. ([Issue 67588](http://b.android.com/67588))
    - Fixed a problem with Nexus 5 Android virtual devices created from the command line where the SD card file system was read-only.
SDK Tools, Revision 22.6.1*(March 2014)*

Dependencies:
:
    - Android SDK Platform-tools revision 18 or later.
    - If you are developing in Eclipse with ADT, note that this version of SDK Tools is designed for use with ADT 22.6.1 and later. If you haven't already, update your ADT Plugin to 22.6.1.
    - If you are developing outside Eclipse, you must have[Apache Ant](http://ant.apache.org/)1.8 or later.

General Notes:
:
    - Fixed a problem where the Android Virtual Device Manager could not create new virtual devices. ([Issue 66661](http://b.android.com/66661))
    - Fixed a problem with virtual devices created using ADT 22.3 or earlier.

      If you created an Android Virtual Device using ADT 22.3 or earlier, the AVD may be listed as*broken* in the AVD Manager in 22.6.1. To fix this problem, select the virtual device on the AVD Manager and click**Repair**.
    - Fixed a problem with the command line tools when creating virtual devices. ([Issue 66740](http://b.android.com/66740))
    - Fixed a problem with the command line`lint`script.

Known Issues:

:   When you create an Android virtual device using the Nexus 5 device definition, you must enable the*Use Host GPU*option, otherwise the virtual device will not start.

SDK Tools, Revision 22.6*(March 2014)*

Dependencies:
:
    - Android SDK Platform-tools revision 18 or later.
    - If you are developing in Eclipse with ADT, note that this version of SDK Tools is designed for use with ADT 22.6.0 and later. If you haven't already, update your ADT Plugin to 22.6.0.
    - If you are developing outside Eclipse, you must have[Apache Ant](http://ant.apache.org/)1.8 or later.

General Notes:
:
    - The command line`lint`script (`tools\lint.bat`on Windows platforms,`tools/lint`on other platforms) and the`lint`target on`ant`builds fail with the following error:

      `Exception in thread "main" java.lang.NoClassDefFoundError:
      lombok/ast/AstVisitor`

      As a temporary workaround, rename the file`tools\lib\lombok-ast-0.2.2.jar`to`tools\lib\lombok-ast.jar`. We will release an updated version of the tools with a fix for this issue as soon as possible.
    - Added support for Java 7 language features like multi-catch, try-with-resources, and the diamond operator. These features require version 19 or higher of the Build Tools. Try-with-resources requires`minSdkVersion`19; the rest of the new language features require`minSdkVersion`8 or higher.
    - Added new lint checks:
      - Security:
        - Look for code potentially affected by a`SecureRandom`vulnerability.
        - Check that calls to`checkPermission`use the return value.
      - Check that production builds do not use mock location providers.
      - Look for manifest values that are overwritten by values from Gradle build scripts.
    - Fixed a number of minor issues in the SDK and build system.
    - Emulator:
      - Fixed a problem with the emulator shutting down immediately for Android 1.5 on the Nexus One and Nexus S devices. ([Issue 64945](http://b.android.com/64945))
      - Fixed a problem with port numbers longer than four digits. ([Issue 60024](http://b.android.com/60024))
      - Fixed battery errors for the Nexus One and Nexus S devices. ([Issue 39959](http://b.android.com/39959))
      - Fixed a problem with paths or arguments that contain spaces on Windows platforms. ([Issue 18317](http://b.android.com/18317))
      - Fixed a problem with long path values on Windows platforms. ([Issue 33336](http://b.android.com/33336))
      - Fixed a problem with the`-snapshot-list`command line option on 64-bit systems. ([Issue 34233](http://b.android.com/34233))
    - Fixed an issue with RenderScript support. Using RenderScript support mode now requires version 19.0.3 of the Build Tools.
SDK Tools, Revision 22.3*(October 2013)*

Dependencies:
:
    - Android SDK Platform-tools revision 18 or later.
    - If you are developing in Eclipse with ADT, note that this version of SDK Tools is designed for use with ADT 22.3.0 and later. If you haven't already, update your ADT Plugin to 22.3.0.
    - If you are developing outside Eclipse, you must have[Apache Ant](http://ant.apache.org/)1.8 or later.

General Notes:
:
    - Added support for Android 4.4 (API level 19).
    - Fixed a number of minor bugs in the SDK and build system.
SDK Tools, Revision 22.2.1*(September 2013)*

Dependencies:
:
    - Android SDK Platform-tools revision 16 or later.
    - If you are developing in Eclipse with ADT, note that this version of SDK Tools is designed for use with ADT 22.2.1 and later. If you haven't already, update your ADT Plugin to 22.2.1.
    - If you are developing outside Eclipse, you must have[Apache Ant](http://ant.apache.org/)1.8 or later.

General Notes:
:
    - Fixed problem with templates that causes the new project wizard to hang. ([Issue 60149](http://b.android.com/60149))
    - Fixed crash when using the lint command line tool because of mis-matched library dependency. ([Issue 60190](http://b.android.com/60190))
SDK Tools, Revision 22.2*(September 2013)*

Dependencies:
:
    - Android SDK Platform-tools revision 16 or later.
    - If you are developing in Eclipse with ADT, note that this version of SDK Tools is designed for use with ADT 22.2 and later. If you haven't already, update your ADT Plugin to 22.2.
    - If you are developing outside Eclipse, you must have[Apache Ant](http://ant.apache.org/)1.8 or later.

General Notes:
:
    - Updated build tools to allow use of RenderScript on older versions of Android using new features in the[Support Library](https://developer.android.com/tools/support-library/features#v8).
    - Moved the Systrace tool to the`>sdk</platform-tools/`directory.
    - Modified Tracer for OpenGL ES to support OpenGL ES 3.0.
    - Lint
      - Fixed problem with lint not detecting custom namespaces. ([Issue 55673](http://b.android.com/55673))
      - Fixed problem with the XML report including invalid characters. ([Issue 56205](http://b.android.com/56205))
      - Fixed command-line execution of lint to work in headless mode to support execution by build servers. ([Issue 55820](http://b.android.com/55820))
    - Improved support for path names with spaces in the Windows command-line tools.
SDK Tools, Revision 22.0.5*(July 2013)*

Dependencies:
:
    - Android SDK Platform-tools revision 16 or later.
    - If you are developing in Eclipse with the ADT Plugin, note that this version of SDK Tools is designed for use with ADT 22.0.5 and later. If you haven't already, update ADT to 22.0.5.
    - This version of the SDK Tools is designed to work with Android Studio 0.2.x and later.
    - If you are developing without an integrated development environment (IDE), you must have[Apache Ant](http://ant.apache.org/)1.8 or later.

General Notes:
:
    - Fixed RenderScript compilation issue for Windows platforms with ant.
    - Updated[Systrace](https://developer.android.com/tools/help/systrace)to work with the Android 4.3 platform image.
    - Fixed packaging of RenderScript compiler.
    - Build tools 18.0.0 is obsolete and 18.0.1 should be used instead.
SDK Tools, Revision 22.0.4*(July 2013)*

Dependencies:
:
    - Android SDK Platform-tools revision 16 or later.
    - If you are developing in Eclipse with the ADT Plugin, note that this version of SDK Tools is designed for use with ADT 22.0.4 and later. If you haven't already, update ADT to 22.0.4.
    - This version of the SDK Tools is designed to work with Android Studio 0.2.x and later.
    - If you are developing without an integrated development environment (IDE), you must have[Apache Ant](http://ant.apache.org/)1.8 or later.

General Notes:
:
    - Fixed problem with compiling RenderScript code.
SDK Tools, Revision 22.0.1*(May 2013)*

Dependencies:
:
    - Android SDK Platform-tools revision 16 or later.
    - If you are developing in Eclipse with ADT, note that this version of SDK Tools is designed for use with ADT 22.0.1 and later. If you haven't already, update your ADT Plugin to 22.0.1.
    - If you are developing outside Eclipse, you must have[Apache Ant](http://ant.apache.org/)1.8 or later.

General Notes:
:
    - Fixed issue with Lint ServiceCast check and fully qualified class names. ([Issue 55403](http://code.google.com/p/android/issues/detail?id=55403))
    - Fixed crash issue with Lint ArraySizeDetector check. ([Issue 54887](http://code.google.com/p/android/issues/detail?id=54887))
    - Fixed a problem with the monkeyrunner tool failing to import standard python classes. ([Issue 55632](http://code.google.com/p/android/issues/detail?id=55632))
    - Fixed a problem with DDMS monitor not opening heap and network statistics views due to a class not found exception. ([Issue 55394](http://code.google.com/p/android/issues/detail?id=55394))
SDK Tools, Revision 22*(May 2013)*

Dependencies:
:
    - Android SDK Platform-tools revision 16 or later.
    - If you are developing in Eclipse with ADT, note that this version of SDK Tools is designed for use with ADT 22.0.0 and later. If you haven't already, update your ADT Plugin to 22.0.0.
    - If you are developing outside Eclipse, you must have[Apache Ant](http://ant.apache.org/)1.8 or later.

General Notes:
:
    - Changed the structure of the SDK by adding a new build tool SDK Component, which is based on the existing platform-tools component. This change decouples the build tools versions from the IDE versions, allowing updates to the tools without requiring an IDE update.
    - Updated tools to allow libraries to share the same package name as the applications that use them.
    - Updated`draw9patch`tool to allow easier changing of markers.
    - Added new Lint checks, including checks for layout consistency,[RelativeLayout](https://developer.android.com/reference/android/widget/RelativeLayout)siblings,[Parcel](https://developer.android.com/reference/android/os/Parcel)creator, JavaScript interfaces,[Service](https://developer.android.com/reference/android/app/Service)casting, quantity strings, manifest typos, orientation tags in layouts, overlapping names for 9-patches and images, and class existence checks.
    - Updated build tools to sign applications using the BouncyCastle library instead of relying on Sun JVM specific APIs.
    - Released some of the Android tools into[Maven Central](http://www.maven.org)to assist third-party tool developers. The following tools are available in the repository:`manifest-merger`,`common/sdk_common`,`ddmlib`,`dvlib`,`layoutlib_api`,`sdklib`, and`lint`.

Bug fixes:
:
    - Fixed a number of minor bugs in the SDK and build system.
SDK Tools, Revision 21.1*(February 2013)*

Dependencies:
:
    - Android SDK Platform-tools revision 16 or later.
    - If you are developing in Eclipse with ADT, note that this version of SDK Tools is designed for use with ADT 21.1.0 and later. If you haven't already, update your ADT Plugin to 21.1.0.
    - If you are developing outside Eclipse, you must have[Apache Ant](http://ant.apache.org/)1.8 or later.

General Notes:
:
    - Improved error reporting in`dx`when dex merging fails in the build system.
    - Added more than 15 new Lint checks, including checks for overriding older APIs, XML resource problems, graphic asset issues and manifest tags.
    - Added new aapt feature to compile resources.
SDK Tools, Revision 21.0.1*(December 2012)*

Dependencies:
:
    - Android SDK Platform-tools revision 16 or later.
    - If you are developing in Eclipse with ADT, note that this version of SDK Tools is designed for use with ADT 21.0.1 and later. If you haven't already, update your ADT Plugin to 21.0.1.
    - If you are developing outside Eclipse, you must have[Apache Ant](http://ant.apache.org/)1.8 or later.

General Notes:
:
    - Build
      - Updated build to detect and handle package name conflicts between an application and the libraries it depends on. Libraries cannot share package names unless all of them share the same package name. ([Issue 40152](http://code.google.com/p/android/issues/detail?id=40152),[Issue 40273](http://code.google.com/p/android/issues/detail?id=40273))
      - Added a flag to disable dex merging to deal with cases where merging could generate a broken dex file. If this happens to your project, add the following setting to your`project.properties`file:`dex.disable.merger=true`This setting causes the build system to revert to the older, slower dex processing that does not pre-dex libraries.
    - RenderScript
      - Added support for[Filterscript](https://developer.android.com/guide/topics/renderscript/compute#filterscript)compilation.
      - Added new project setting to control the RenderScript compilation target separately from an Android project. Adding the following line to a`project.properties`file causes RenderScript code to be compiled for Android API Level 17, while the containing application can target a different (lower) API level:  

        ```
        renderscript.target = 17
        ```
        Previously, the RenderScript compilation target was tied to the`android:minSdkVersion`setting in the manifest. ([Issue 40487](http://code.google.com/p/android/issues/detail?id=40487))

Bug fixes:
:
    - Lint
      - Corrected check for`0px`values in style XML elements. ([Issue 39601](http://code.google.com/p/android/issues/detail?id=39601))
      - Fixed incorrect flagging of formatting strings. ([Issue 39758](http://code.google.com/p/android/issues/detail?id=39758))
      - Fixed problem where`tools:ignore`directive in the manifest file was ignored by the Lint tool. ([Issue 40136](http://code.google.com/p/android/issues/detail?id=40136))
      - Fixed problem with flagging a wakelock release inside a conditional. ([Issue 40424](http://code.google.com/p/android/issues/detail?id=40424))
      - Fixed incorrect reporting of missing`layout_width`and`layout_height`XML fields. ([Issue 38958](http://code.google.com/p/android/issues/detail?id=38958))
      - Fixed handling of custom namespace attributes.
      - Added fixes for filtering out library project warnings.
      - Removed warnings about missing classes before a build.
    - Fixed problem with UI Automator Viewer execution script where Android tools directory is not set.
    - Fixed problem with the SDK Manager so that it auto-selects the most recently released platform on startup.
    - Fixed Java finding script to look for the currently supported version of Java (1.6 or higher).
    - Fixed the SDK Manager launcher in the ADT bundle so that it can properly launch the SDK Manager program when it is placed at the root of the bundle.
SDK Tools, Revision 21*(November 2012)*

Dependencies:
:
    - Android SDK Platform-tools revision 16 or later.
    - If you are developing in Eclipse with ADT, note that this version of SDK Tools is designed for use with ADT 21.0.0 and later. If you haven't already, update your ADT Plugin to 21.0.0.
    - If you are developing outside Eclipse, you must have[Apache Ant](http://ant.apache.org/)1.8 or later.

General Notes:
:
    - Build System
      - Added a flag that sets*jumbo mode* for DEX files, which allows a larger number of strings in the DEX files. Enable this mode by adding the following line to the`project.properties`file of your project:  

        ```
        dex.force.jumbo=true
        ```
      - Improved the build time by pre-dexing libraries (both JAR files and library projects).
      - Updated the build to generate`R`resource classes for library projects with only the IDs needed by the libraries, reducing the risk of hitting DEX file limits for fields and methods.
      - Improved the build so that several editing features (code completion, resource chooser, go to declaration) properly handle library project resources.
    - Lint
      - Added over 25 new lint rules for resources, locale settings, layout files, incorrect use of[SparseArray](https://developer.android.com/reference/android/util/SparseArray)and[PowerManager.WakeLock](https://developer.android.com/reference/android/os/PowerManager.WakeLock)and manifest issues.
      - Updated reporting to include errors in library projects if the library project is in the list of projects to be checked.
      - Added a new`lint`target to the Ant build system for easier integration with continuous build systems.
      - Added new`--sources`and`--classpath`arguments to point to sources with different directory structures.
      - Improved the XML export function to support the[Jenkins Lint plugin](https://wiki.jenkins-ci.org/display/JENKINS/Android+Lint+Plugin).
      - Added support for class file flow analysis.
    - Android Virtual Devices (AVD)
      - Added new**Device Definitions**tab in the AVD Manager for configuring standard size and Nexus virtual devices.
      - Improved emulators so that they launch with a skin that is dynamically generated and reflects the actual hardware configured in the AVD Manager.
      - Improved support for developing Android apps on MIPS-based devices with new MIPS System Images for Android Virtual Devices.
    - Added`jobb`tool for creating and encrypting[APK Expansion Files](https://developer.android.com/google/play/expansion-files). ([more info](https://developer.android.com/tools/help/jobb))
    - Improved the Android JUnit test runner to allow a test to be run on all connected devices simultaneously.

Bug fixes:
:
    - Fixed manifest merger to properly adapt library classes in the merged manifest.
SDK Tools, Revision 20.0.3*(August 2012)*

Dependencies:
:
    - Android SDK Platform-tools revision 12 or later.
    - If you are developing in Eclipse with ADT, note that this version of SDK Tools is designed for use with ADT 20.0.3 and later. If you haven't already, update your ADT Plugin to 20.0.3.
    - If you are developing outside Eclipse, you must have[Apache Ant](http://ant.apache.org/)1.8 or later.

Bug fixes:
:
    - Fixed problem with cached download lists in SDK Manager.
SDK Tools, Revision 20.0.1*(July 2012)*

Dependencies:
:
    - Android SDK Platform-tools revision 12 or later.
    - If you are developing in Eclipse with ADT, note that this version of SDK Tools is designed for use with ADT 20.0.1 and later. If you haven't already, update your ADT Plugin to 20.0.1.
    - If you are developing outside Eclipse, you must have[Apache Ant](http://ant.apache.org/)1.8 or later.

Bug fixes:
:
    - Fixed wrong check on build state that forced repetitive Java code recompilation.
    - Fixed problems with running more than one emulator and running multiple emulators with GPU acceleration.
    - Improved resize algorithm for better rendering on scaled emulator windows.
    - Fixed a bug in the`lint`check for unprotected broadcast receivers to ignore unprotected receivers for default Android actions.
    - Fixed build issue for projects using RenderScript.
    - Fixed memory leak in the emulator.
SDK Tools, Revision 20*(June 2012)*

Dependencies:
:
    - Android SDK Platform-tools revision 12 or later.
    - If you are developing in Eclipse with ADT, note that this version of SDK Tools is designed for use with ADT 20.0.0 and later. If you haven't already, we highly recommend updating your ADT Plugin to 20.0.0.
    - If you are developing outside Eclipse, you must have[Apache Ant](http://ant.apache.org/)1.8 or later.

General notes:
:
    - Added new Device Monitor application, grouping Android debugging tools into a single application, including ddms, traceview, hierarchyviewer and Tracer for GLES. ([more info](https://developer.android.com/tools/help/gltracer))
    - Added new System Trace new tool for tracing Android system activity. This tool allow you to capture a slice of system activity, plus additional information tagged from the**Settings \> Developer Options \> Monitoring: Enable traces**or with specific calls added to your application code.
    - Build System
      - Added automatic merging of library project manifest files into the including project's manifest. Enable this feature with the`manifestmerger.enabled`property.
      - Added automatic ProGuard support for the`aapt -G`flag. This change causes the build system to generate a temporary ProGuard`keep-rules`file containing classes that are referenced from XML files (such as custom views) and pass this to ProGuard at shrink time. This can make the resulting APK much smaller when using just a small portion of a large library project (such as the Android Support library), since the catch-all rules to keep all custom views from the default ProGuard configuration file have also been removed.
      - Added two ProGuard configuration files for use in projects:`proguard-android-optimize.txt`which enables optimizations and`proguard-android.txt`which disables them.
    - SDK Manager
      - Improved caching to reduce downloading of repository definitions.
      - Added**Tools \> Manage Add-on Sites**option to improve performance by allowing temporary deactivation of third-party sites if they are loading slowly.
      - Added settings for the SDK Manager download cache (**SDK Manager \> Tools \> Options**).

Bug fixes:
:
    - Build
      - Fixed problem where test projects did not have access to the full classpath of tested projects, including Library Projects and third-party jars.
      - Fixed deployment logic so that applications with embedded tests can now be deployed and tested like test applications, including code coverage information.
      - Fixed Ant support for testing projects with libraries.
SDK Tools, Revision 19*(April 2012)*

**Note:** This update of SDK Tools is only available through the[Android SDK Manager](https://developer.android.com/studio/intro/update). Use this tool to download and install this update.

Dependencies:
:
    - Android SDK Platform-tools revision 9 or later.
    - If you are developing in Eclipse with ADT, note that this version of SDK Tools is designed for use with ADT 18.0.0 and later. If you haven't already, we highly recommend updating your ADT Plugin to 18.0.0.
    - If you are developing outside Eclipse, you must have[Apache Ant](http://ant.apache.org/)1.8 or later.

Bug fixes:
:
    - Fixed an issue that prevented some developers from running the emulator with GPU acceleration.
SDK Tools, Revision 18*(April 2012)*

**Important:**To download the new Android 4.0 system components from the Android SDK Manager, you must first update the SDK tools to revision 14 or later and restart the Android SDK Manager. If you do not, the Android 4.0 system components will not be available for download.

Dependencies:
:
    - Android SDK Platform-tools revision 9 or later.
    - If you are developing in Eclipse with ADT, note that this version of SDK Tools is designed for use with ADT 18.0.0 and later. If you haven't already, we highly recommend updating your ADT Plugin to 18.0.0.
    - If you are developing outside Eclipse, you must have[Apache Ant](http://ant.apache.org/)1.8 or later.

General notes:
:
    - Updated the SdkController app to encapsulate both sensor and multitouch emulation functionality.

Bug fixes:
:
    - Fixed Ant issues where some jar libraries in the`libs/`folder are not picked up in some cases.
SDK Tools, Revision 17*(March 2012)*

**Important:**To download the new Android 4.0 system components from the Android SDK Manager, you must first update the SDK tools to revision 14 or later and restart the Android SDK Manager. If you do not, the Android 4.0 system components will not be available for download.

Dependencies:
:
    - Android SDK Platform-tools revision 9 or later.
    - If you are developing in Eclipse with ADT, note that this version of SDK Tools is designed for use with ADT 17.0.0 and later. If you haven't already, we highly recommend updating your ADT Plugin to 17.0.0.
    - If you are developing outside Eclipse, you must have[Apache Ant](http://ant.apache.org/)1.8 or later.

General notes:
:
    - Emulator
      - Added support for hardware accelerated graphics rendering. This feature requires an API Level 15, Revision 3 or later system image. ([more info](https://developer.android.com/tools/devices/emulator#accel-graphics))
      - Added support for running Android x86 system images in virtualization mode on Windows and Mac OS X. ([more info](https://developer.android.com/tools/devices/emulator#accel-vm))

        **Note:**Use the Android SDK Manager to download and install x86 system images. Android x86 system images are not available for all API levels.
      - Added experimental support for multi-touch input by enabing the emulator to receive touch input from a USB-tethered physical Android device. ([more info](http://tools.android.com/tips/hardware-emulation))
    - Added viewing of live detailed network usage of an app in DDMS. ([more info](http://tools.android.com/recent/detailednetworkusageinddms))
    - ProGuard
      - Updated the bundled ProGuard tool to version 4.7. In addition to many new features, this update fixes the`Conversion to Dalvik format failed with error 1`error some users have experienced.
      - Updated the default`proguard.cfg`file with better default flags for Android.
      - Split the ProGuard configuration file has been in half, with project specific flags kept in project and the generic Android flags distributed (and updated) with the tools themselves.
    - Build
      - Added a feature that allows you to run some code only in debug mode. Builds now generate a class called`BuildConfig`containing a`DEBUG`constant that is automatically set according to your build type. You can check the (`BuildConfig.DEBUG`) constant in your code to run debug-only functions.
      - Fixed issue when a project and its libraries include the same jar file in their libs folder. ([more info](http://tools.android.com/recent/dealingwithdependenciesinandroidprojects))
      - Added support for custom views with custom attributes in libraries. Layouts using custom attributes must use the namespace URI`http://schemas.android.com/apk/res-auto`instead of the URI that includes the app package name. This URI is replaced with the app specific one at build time.
    - Lint
      - Updated Lint to check Android application code. Lint rules which previously performed pattern based searches in the application code (such as the unused resource check) have been rewritten to use the more accurate Java-style parse trees.
      - Added support for checking library projects. This change means that rules such as the unused resource check properly handle resources declared in a library project and referenced in a downstream project.
      - Added ability to suppress Lint warnings in Java code with the new`@SuppressLint`annotation, and in XML files with the new tools: namespace and ignore attribute. ([more info](http://tools.android.com/recent/ignoringlintwarnings))
      - New Lint checks:
        - Added check for Android API calls that require a version of Android higher than the minimum supported version. You can use the new`@TargetApi`annotation to suppress warnings when the code is wrapped in a system version condition. ([more info](http://tools.android.com/recent/lintapicheck))
        - Added over 20 new Lint rules, including checks for[performance](http://tools.android.com/recent/lintperformancechecks), XML layouts, manifest and file handling.
SDK Tools, Revision 16*(December 2011)*

**Important:**To download the new Android 4.0 system components from the Android SDK Manager, you must first update the SDK tools to revision 14 or later and restart the Android SDK Manager. If you do not, the Android 4.0 system components will not be available for download.

Dependencies:
:
    - Android SDK Platform-tools revision 9 or later.
    - If you are developing in Eclipse with ADT, note that this version of SDK Tools is designed for use with ADT 16.0.0 and later. If you haven't already, we highly recommend updating your ADT Plugin to 16.0.0.
    - If you are developing outside Eclipse, you must have[Apache Ant](http://ant.apache.org/)1.8 or later.

General notes:
:
    - Added Lint tools to detect common errors in Android projects. ([more info](http://tools.android.com/recent/lint))
    - Added sensor emulation support, which allows the emulator to read sensor data from a physical Android device. ([more info](http://tools.android.com/recent/sensoremulation))
    - Added support for using a webcam to emulate a camera on Mac OS X.

Bug fixes:
:
    - Snapshots now work for Android 4.0 system images.
    - Fixed several small issues for the build file. ([Issue 21023](http://code.google.com/p/android/issues/detail?id=21023),[Issue 21267](http://code.google.com/p/android/issues/detail?id=21267),[Issue 21465](http://code.google.com/p/android/issues/detail?id=21465),[Issue 21525](http://code.google.com/p/android/issues/detail?id=21525)).
SDK Tools, Revision 15*(October 2011)*

**Important:**To download the new Android 4.0 system components from the Android SDK Manager, you must first update the SDK tools to revision 14 or later and restart the Android SDK Manager. If you do not, the Android 4.0 system components will not be available for download.

Dependencies:
:
    - Android SDK Platform-tools revision 9 or later.
    - If you are developing in Eclipse with ADT, note that this version of SDK Tools is designed for use with ADT 15.0.0 and later. If you haven't already, we highly recommend updating your[ADT Plugin](https://developer.android.com/tools/sdk/eclipse-adt)to 15.0.0.
    - If you are developing outside Eclipse, you must have[Apache Ant](http://ant.apache.org/)1.8 or later.

Bug fixes:
:
    - Fixed emulator crash on Linux due to improper webcam detection ([Issue 20952](http://code.google.com/p/android/issues/detail?id=20952)).
    - Fixed emulator issue when using the`-wipe-data`argument.
    - Fixed build issue when using RenderScript in projects that target API levels 11-13 ([Issue 21006](http://code.google.com/p/android/issues/detail?id=21006)).
    - Fixed issue when creating an AVD using the GoogleTV addon ([Issue 20963](http://code.google.com/p/android/issues/detail?id=20963)).
    - Fixed`ant test`([Issue 20979](http://code.google.com/p/android/issues/detail?id=20979)).
    - Fixed`android update project`([Issue 20535](http://code.google.com/p/android/issues/detail?id=20535)).
    - Fixed scrolling issue in the new Logcat panel of DDMS.
    - Fixed issue with MonkeyRunner ([Issue 20964](http://code.google.com/p/android/issues/detail?id=20964)).
    - Fixed issues in the SDK Manager ([Issue 20939](http://code.google.com/p/android/issues/detail?id=20939),[Issue 20607](http://code.google.com/p/android/issues/detail?id=20607)).
SDK Tools, Revision 14*(October 2011)*

**Important:**To download the new Android 4.0 system components from the Android SDK Manager, you must first update the SDK tools to revision 14 and restart the Android SDK Manager. If you do not, the Android 4.0 system components will not be available for download.

Dependencies:
:
    - Android SDK Platform-tools revision 8 or later.
    - If you are developing in Eclipse with ADT, note that this version of SDK Tools is designed for use with ADT 14.0.0 and later. If you haven't already, we highly recommend updating your[ADT Plugin](https://developer.android.com/tools/sdk/eclipse-adt)to 14.0.0.
    - If you are developing outside Eclipse, you must have[Apache Ant](http://ant.apache.org/)1.8 or later.

General notes:
:
    - Added webcam support to Android 4.0 or later platforms to emulate rear-facing cameras when one webcam is present, and to emulate both rear-facing and front-facing cameras when two webcams are present. Webcam support is for Windows and Linux only. Mac support will come in a later release.
    - Changed`default.properties`to`project.properties`and`build.properties`to`ant.properties`. Any existing projects that you build with Ant must be updated with the`android update project`command.
    - Changed Ant`build.xml`file to support improvements to the build system and added and modified Ant commands to support these changes. For a list of Ant commands, see the[Ant Command Reference](https://developer.android.com/tools/building/building-cmdline#AntReference).
    - Changed how library projects are built.
    - Improved incremental builds, so that resource compilation runs less frequently. Builds no longer run when you edit strings or layouts (unless you add a new`id`) and no longer run once for each library project.
    - Introduced a "PNG crunch cache" that only runs on modified PNG files, instead of crunching all existing PNG files, all the time.
    - Revamped the SDK Manager UI ([more info](http://tools.android.com/recent/newsdkmanager)).

    For a complete overview of the build system changes and what you need to do to support them, see the[Android Tools Project site](http://tools.android.com/recent/buildchangesinrevision14).
SDK Tools, Revision 13*(September 2011)*

Dependencies:

:   If you are developing in Eclipse with ADT, note that this version of SDK Tools is designed for use with ADT 12.0.0 and later. If you haven't already, we highly recommend updating your[ADT Plugin](https://developer.android.com/tools/sdk/eclipse-adt)to 12.0.0.

    If you are developing outside Eclipse, you must have[Apache Ant](http://ant.apache.org/)1.8 or later.

General notes:
:
    - Fix compilation issue in Ant (`dex`step) when paths have spaces.
    - Fix issue in emulator installation when paths have spaces.
    - Fix issue when AVD paths have spaces.
    - Fix rendering issue when using emulator scaling ([see more](http://code.google.com/p/android/issues/detail?id=18299)).
SDK Tools, Revision 12*(July 2011)*

Dependencies:

:   If you are developing in Eclipse with ADT, note that this version of SDK Tools is designed for use with ADT 12.0.0 and later. If you haven't already, we highly recommend updating your[ADT Plugin](https://developer.android.com/tools/sdk/eclipse-adt)to 12.0.0.

    If you are developing outside Eclipse, you must have[Apache Ant](http://ant.apache.org/)1.8 or later.

General notes:
:
    - The AVD manager and emulator can now use system images compiled for ARM v7 and x86 CPUs.
SDK Tools, Revision 11*(May 2011)*

Dependencies:

:   If you are developing in Eclipse with ADT, note that this version of SDK Tools is designed for use with ADT 10.0.1 and later. If you haven't already, we highly recommend updating your[ADT Plugin](https://developer.android.com/tools/sdk/eclipse-adt)to 10.0.1.

    If you are developing outside Eclipse, you must have[Apache Ant](http://ant.apache.org/)1.8 or later.

General notes:
:
    - Miscellaneous emulator changes to support Android 3.1.
SDK Tools, Revision 10*(February 2011)*

Dependencies:

:   If you are developing in Eclipse with ADT, note that this version of SDK Tools is designed for use with ADT 10.0.0 and later. After installing SDK Tools r10, we highly recommend updating your ADT Plugin to 10.0.0.

    If you are developing outside Eclipse, you must have[Apache Ant](http://ant.apache.org/)1.8 or later.

General notes:
:
    - The tools now automatically generate Java Programming Language source files (in the`gen`directory) and bytecode (in the`res/raw`directory) from your native`.rs`files
SDK Tools, Revision 9*(January 2011)*

Dependencies:

:   If you are developing in Eclipse with ADT, note that this version of SDK Tools is designed for use with ADT 9.0.0 and later. After installing SDK Tools r9, we highly recommend updating your ADT Plugin to 9.0.0.

    If you are developing outside Eclipse, you must have[Apache Ant](http://ant.apache.org/)1.8 or later.

Upgrading to SDK Tools r9:

:   If you are upgrading to SDK Tools r9 from SDK Tools r7 or earlier, the default installed location for the`adb`tool has changed from`<`*SDK*`>/tools/adb`to`<`*SDK*`>/platform-tools/adb`. This means that you should add the new location to your PATH and modify any custom build scripts to reference the new location. Copying the`adb`executable from the new location to the old is not recommended, since subsequent updates to the SDK Tools will delete the file.

General notes:
:
    - The default ProGuard configuration,`proguard.cfg`, now ignores the following classes:
      - classes that extend[Preference](https://developer.android.com/reference/android/preference/Preference)
      - classes that extend[BackupAgentHelper](https://developer.android.com/reference/android/app/backup/BackupAgentHelper)
    - Ant lib rules now allow you to override`java.encoding`,`java.source`, and`java.target`properties.
    - The default encoding for the`javac`Ant task is now UTF-8.
    - The LogCat view in DDMS now properly displays UTF-8 characters.
    - The SDK Manager is more reliable on Windows. For details on the improvements, see the[Android Tools Project Site](http://tools.android.com/recent/sdkmanagerfixes).
    - Early look at the new snapshot feature: To improve startup time for the emulator, you can enable snapshots for the system state. The emulator will then restore to the state when it last closed almost instantly.**Note:**The snapshot feature is still under active development and might not always perform as expected.
    - Fixed the missing JAR file error that prevented`draw9patch`from running.
    - Fixed the Windows launch scripts`hierarchyviewer`and`ddms`to support the new location of`adb`.
    - Known issues with emulator performance: Because the Android emulator must simulate the ARM instruction set architecture on your computer, emulator performance is slow. We're working hard to resolve the performance issues and it will improve in future releases.
SDK Tools, Revision 8*(December 2010)*

Dependencies:

:   If you are developing in Eclipse with ADT, note that this version of SDK Tools is designed for use with ADT 8.0.0 and later. After installing SDK Tools r8, we highly recommend updating your ADT Plugin to 8.0.0.

    If you are developing outside Eclipse, you must have[Apache Ant](http://ant.apache.org/)1.8 or later.

    Also note that SDK Tools r8 requires a new SDK component called*Platform-tools* . The new Platform-tools component lets all SDK platforms (Android 2.1, Android 2.2, and so on) use the same (latest) version of build tools such as`adb`,`aapt`,`aidl`, and`dx`. To download the Platform-tools component, use the[Android SDK Manager](https://developer.android.com/studio/intro/update).

Upgrading from SDK Tools r7:

:   If you are upgrading to SDK Tools r8 from an earlier version, note that the the default installed location for the`adb`tool has changed from`<`*SDK*`>/tools/adb`to`<`*SDK*`>/platform-tools/adb`. This means that you should add the new location to your PATH and modify any custom build scripts to reference the new location. Copying the`adb`executable from the new location to the old is not recommended, since subsequent updates to the SDK Tools will delete the file.

General notes:
:
    - All SDK platforms now support Library Projects.
    - Support for a true debug build. Developers no longer need to add the`android:debuggable`attribute to the`<application>`tag in the manifest --- the build tools add the attribute automatically. In Eclipse/ADT, all incremental builds are assumed to be debug builds, so the tools insert`android:debuggable="true"`. When exporting a signed release build, the tools do not add the attribute. In Ant, a`ant debug`command automatically inserts the`android:debuggable="true"`attribute, while`ant release`does not. If`android:debuggable="true"`is manually set, then`ant release`will actually do a debug build, rather than a release build.
    - Automatic ProGuard support in release builds. Developers generate a ProGuard configuration file using the`android`tool --- the build tools then automatically run ProGuard against the project sources during the build. For more information, see the[ProGuard](https://developer.android.com/tools/help/proguard)documentation.
    - New overridable Ant javac properties:`java.encoding`,`java.source`, and`java.target`(default values are "ascii", "1.5", and "1.5", respectively).
    - New UI for the HierarchyViewer tool.
SDK Tools, Revision 7*(September 2010)*

Dependencies:

:   If you are developing in Eclipse with ADT, note that this version of SDK Tools is designed for use with ADT 0.9.8 and later. After installing SDK Tools r7, we highly recommend updating your ADT Plugin to 0.9.8.

General notes:
:
    - Added support for library projects that depend on other library projects.
    - Adds support for aidl files in library projects.
    - Adds support for extension targets in Ant build to perform tasks between the normal tasks:`-pre-build`,`-pre-compile`, and`-post-compile`.
    - Adds support for "headless" SDK update. See`android -h update sdk`for more information.
    - Fixes location control in DDMS to work in any locale not using '.' as a decimal point.
SDK Tools, Revision 6*(May 2010)*

Dependencies:

:   If you are developing in Eclipse with ADT, note that this version of SDK Tools is designed for use with ADT 0.9.7 and later. After installing SDK Tools r6, we highly recommend updating your ADT Plugin to 0.9.7.

Library projects:

:   The SDK Tools now support the use of*library projects* during development, a capability that lets you store shared Android application code and resources in a separate development project. You can then reference the library project from other Android projects and, at build time, the tools compile the shared code and resources as part of the dependent applications. More information about this feature is available in the[Creating and Managing Projects](https://developer.android.com/tools/projects#LibraryProjects)document.

    If you are developing in Eclipse,[ADT](https://developer.android.com/tools/sdk/eclipse-adt)provides the equivalent library project support.
SDK Tools, Revision 5*(March 2010)*

Dependencies:
:
    - If you are developing in Eclipse with ADT, note that this version of SDK Tools is designed for use with ADT 0.9.6 and later. After installing SDK Tools r5, we highly recommend updating your ADT Plugin to 0.9.6.
    - For Mac OS platforms, OS X 10.4.x (Tiger) is no longer officially supported.

SDK and AVD Manager:
:
    - Fixes SSL download for the standalone version of the SDK Updater.
    - Fixes issue with 64-bit JVM on Windows.
    - Adds support for platform samples components.
    - Improves support for dependency between components.
    - AVDs now sorted by API level.
    - The AVD creation dialog now enforces a minimum SD card size of 9MB.
    - Prevents deletion of running AVDs.
    - Settings are now automatically saved, no need to click "Apply".

Emulator:
:
    - Emulator now requires SD card to be 9MB or more.

Layoutopt:
:
    - Fixes`layoutopt.bat`to execute correctly on Windows.
SDK Tools, Revision 4*(December 2009)*

Dependencies:

:   This version of SDK Tools is compatible with ADT 0.9.5 and later, but not compatible with earlier versions. If you are developing in Eclipse with ADT, you**must**update your ADT plugin to version 0.9.5 or higher if you install SDK Tools r4 in your SDK.

General notes:
:
    - Launcher script now forces GDK_NATIVE_WINDOW=true (linux only), to fix a compatibility issue between GTK and SWT.

Android SDK and AVD Manager:
:
    - AVD Launch dialog now shows scale value.
    - Fixes potential NPE in SDK Manager on AVD launch, for older AVD with no skin name specified.
    - Fixes XML validation issue in on older Java versions.
    - No longer forces the use of Java 1.5 on Mac OS X.

Emulator:
:
    - No longer limits the size of the system partition.

Ant build tools:
:
    - .apk packaging now properly ignores vi swap files as well as hidden files.
SDK Tools, Revision 3*(October 2009)*

Dependencies:

:   This version of SDK Tools is compatible with ADT 0.9.4 and later, but not compatible with earlier versions. If you are developing in Eclipse with ADT, you**must**update your ADT plugin to version 0.9.4 or higher if you install SDK Tools r3 in your SDK.

Android tool:
:
    - Adds new`android create test-project`and`android update
      test-project`commands to allow for greater flexibility in the location of the main and test projects.

DDMS:
:
    - Adds a button to dump HPROF file for running applications (app must be able to write to the sdcard).
    - Button to start/stop profiling of a running application (app must be able to write to the sdcard). Upon stop, Traceview will automatically be launched to display the trace.
    - Fixed DDMS, Traceview, and the AVD Manager/SDK Updater to run on Mac OS X 10.6.
    - Fixed screenshot support for devices running 32-bit framebuffer.

Android SDK and AVD Manager:
:
    - Provides a new UI that lets you set options for controlling the emulator skin, screen size/density, and scale factor used when launching an AVD.
    - Provides improved AVD creation UI, which lets you customize the hardware properties of your AVDs.
    - Now enforces dependencies between platforms and tools components, and between SDK add-ons and platforms.

Layoutopt, a new tool for optimizing layouts:

:   The SDK Tools r3 package includes`layoutopt`, a new command-line tool that helps you optimize your layout hierarchies. When run against your layout files, the tool analyzes their hierarchies and notifies you of inefficiencies and other potential issues. The tool also provides simple solutions for the issues it finds. For usage, see[layoutopt](https://developer.android.com/tools/help/layoutopt).