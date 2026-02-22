---
title: https://developer.android.com/tools/releases/platform-tools
url: https://developer.android.com/tools/releases/platform-tools
source: md.txt
---

<br />

Android SDK Platform-Tools is a component for the Android SDK.
It includes tools that interface with the Android platform, primarily
[`adb`](https://developer.android.com/tools/adb) and
[`fastboot`](https://android.googlesource.com/platform/system/core/+/master/fastboot/#fastboot).
Although `adb` is required for Android app development, app developers will
normally just use the copy Studio installs. This download is useful if you want
to use `adb` directly from the command-line and don't have Studio installed.
(If you do have Studio installed, you might want to just use the copy it
installed because Studio will automatically update it.) `fastboot` is needed
if you want to unlock your device bootloader and flash it with a new system
image. This package used to contain `systrace`, but that has been obsoleted in
favor of Studio Profiler, gpuinspector.dev, or Perfetto.

Although some new features in `adb` and `fastboot` are available only for recent
versions of Android, they're backward compatible, so you should only need the
latest version of the SDK Platform-Tools and should file bugs if you find
exceptions.

## Downloads

If you're an Android developer, you should get the latest
SDK Platform-Tools from Android Studio's [SDK Manager](https://developer.android.com/studio/intro/update#sdk-manager) or from the
[`sdkmanager`](https://developer.android.com/studio/command-line/sdkmanager)
command-line tool. This ensures the tools are saved to the right place with
the rest of your Android SDK tools and easily updated.

But if you want just these command-line tools, use the following links:

- <button class="devsite-dialog-button button-white button-regular" data-modal-dialog-id="dac-download-windows-dialog-id"> Download SDK Platform-Tools for Windows</button>
- <button class="devsite-dialog-button button-white button-regular" data-modal-dialog-id="dac-download-mac-dialog-id"> Download SDK Platform-Tools for Mac</button>
- <button class="devsite-dialog-button button-white button-regular" data-modal-dialog-id="dac-download-linux-dialog-id"> Download SDK Platform-Tools for Linux</button>

Although these links do not change, they always point to the most recent version
of the tools.

## Revisions

#### 36.0.2 (Sep 2025)

- **adb**
  - Make legacy USB backend the default on Linux (instead of libusb) due to instability reports (device disconnection, interface read failure, and delayed netlink events preventing device detection).
  - Fix bug where Samsung devices were not properly detected [issue #404741058](https://issuetracker.google.com/404741058).
  - Fix bug where old Android devices using USB class `Miscellaneous` (0xEF) were not properly detected [issue #365009755](https://issuetracker.google.com/365009755).
  - Fix bug where last character of a file was truncated when pulled or pushed \[Windows only\] [issue #439152273](https://issuetracker.google.com/439152273).

#### 36.0.1

Never released past Canary due to [issue #439152273](https://issuetracker.google.com/439152273).

#### 36.0.0 (Apr 2025)

- **adb**
  - Re-written libusb USB backend (uses sync API instead of async API). Improves reliability and fixes memory exhaustion on Linux.
  - Libusb USB backend hot-plug now supports for Windows (enables USB speed detection).
  - Improved `server-status` now displays if mdns is enabled.
  - Fixed macOS bug where zero-length packets were not sent, resulting in stalled connection [issue #208675141](https://issuetracker.google.com/208675141).
  - Fixed use-after-free in libusb backend.

#### 35.0.2 (July 2024)

- **adb**
  - Fix openscreen mDNS backend bug bringing down server on truncated query [issue #294120933](https://issuetracker.google.com/issues/294120933).
  - Make openscreen mDNS backend work on macOS.
  - Make openscreen mDNS backend default on all platforms.
  - Support to detect USB SuperSpeed+ (current and negotiated speeds) for diagnostic purposes.
  - Graceful shutdown: Release all USB interfaces on shutdown (all OSes).

#### 35.0.1 (March 2024)

- **adb**
  - Switch to libusb 1.0.27

#### 35.0.0 (February 2024)

- **adb**
  - Switch to libusb as the default on Linux [issue #270205252](https://issuetracker.google.com/issues/270205252).
  - Fix adb startup on hosts without USB.
  - Fix adb hangs caused by USB devices incorrectly reporting zero-length descriptors [issue #302212871](https://issuetracker.google.com/issues/302212871).
  - Fix return code of `adb shell` when device disconnects [issue #321787891](https://issuetracker.google.com/issues/321787891).
- **fastboot**
  - Limit the maximum size of the incoming packet queue.
  - Remove bottlenecks that previously limited download speeds to around 120MB/s. Now fastboot can saturate a SuperSpeed+ bus and achieve speeds up to 980MB/s, depending on the device.

#### 34.0.5 (October 2023)

- **adb**
  - adb now defaults to libusb on macOS to address [issue #270205252](https://issuetracker.google.com/issues/270205252).
  - Previously, adb responded with a successful code when wireless pairing fails. Resolved this by returning a failure code (1) and user-facing error (`error: protocol fault (couldn't read status message...)`). `echo $?` now reports `1`.
  - `adb wait-for-disconnect` is now operational for non-USB (wireless debugging).
  - Added new DbC interface for future support of ChromeOS over adb.
- **fastboot**
  - Fixed flashall on Pixel 3 devices.

#### 34.0.4 (July 2023)

- **adb**
  - Propagate `-a (gListenAll)` when adb forks an adb host server (previously, the flag only worked for `adb -a server nodaemon`)
  - Faster root and unroot
  - Reland `Flag(env) guarding clear endpoint (device)
    feature for OSX usb start.` ([issue #270205252](https://issuetracker.google.com/issues/270205252)).
- **fastboot**
  - Mac: remove retries on invalid IO iterator (flashing failure with LIBUSB_TRANSFER_CANCELLED)
  - Windows: fix "Sparse file is too large or invalid" when using "flashall"
  - All platforms: fix "ANDROID_PRODUCT_OUT not set" when using "update"

#### 34.0.1 (March 2023)

- **adb**
  - macOS: Reverted "unstable connectivity (MacBook high speed cable)" resolution due to adb install hang ([issue #270205252](https://issuetracker.google.com/issues/270205252)).
- **fastboot**
  - Windows: Fixed "mke2fs: Illegal or malformed device name while trying to determine filesystem size" error introduced in Platform tools 34.0.0 ([issue #271039230](https://issuetracker.google.com/issues/271039230)).

#### 34.0.0 RC2 (March 2023)

- Updated with the release of Android 14 Developer Preview 2 (no updates to adb and fastboot).

#### 34.0.0 (February 2023)

- **adb**
  - Fixed zero length packet sends for macOS [(issuetracker: 208675141)](https://issuetracker.google.com/issues/208675141).
  - Addressed unstable connectivity (MacBook high speed cable): frequent adb disconnects.
  - Improved error message for adb push with insufficient number of arguments.
- **fastboot**
  - Improved flashing: `flashall` will now skip reboots to userspace if it can.
  - Fixed zero length packet sends for macOS [(issuetracker: 208675141)](https://issuetracker.google.com/issues/208675141).
  - Fixed flashing recovery.img resulting in wrong AVB footer.

#### 33.0.3 (Aug 2022)

- **adb**
  - Don't retry `adb root` if first attempt failed.
  - Fix track-devices duplicate entry.
  - Add receive windowing (increase throughput on high-latency connections).
  - More specific error messages in the "more than one device" failure cases.
  - Reject unexpected reverse forward requests.
  - Fix install-multi-package on Windows.
- **fastboot**
  - Remove e2fsdroid as part of SDK platform-tools.
  - Print OemCmdHandler return message on success.

#### 33.0.2 (May 2022)

- **fastboot**
  - Support for the `vendor_kernel_boot` partition.

#### 33.0.1 (March 2022)

- **adb**
  - Fixes Windows mdns crashes.
  - Fixes enable-verity/disable-verity on old devices.
  - Fixes "install multiple" on old devices
  - Improves the help output to include all supported compression methods.
- **systrace**
  - Removed. Use Studio Profiler/gpuinspector.dev/Perfetto instead.

#### 33.0.0 (February 2022)

- **adb**
  - Fixes the issue introduced in 32.0.0 of crashes when run without any arguments.

#### 32.0.0 (January 2022)

- **adb**
  - Universal binary for Apple M1 devices.
  - Known issue: this version crashes when run without any arguments.

#### 31.0.3 (August 2021)

- **fastboot**
  - Support flashing vbmeta_vendor.img for fastboot flashall / update.

#### 31.0.2 (April 2021)

- **adb**
  - Support forwarding to vsock on linux.
  - Fix bug in `adb track-devices` where devices over wireless debugging wouldn't immediately receive updates.
  - Implement preliminary support for mDNS device discovery without a separately installed mDNS service. This is currently disabled by default, and can be enabled by setting the environment variable `ADB_MDNS_OPENSCREEN` to 1 when starting the adb server.
- **fastboot**
  - Don't fail when unable to get boot partition size.
  - Derive device locked state from property instead of parsing the kernel command line.

#### 31.0.1 (March 2021)

- **adb**
  - Reduce TCP keepalive interval.
  - Improve incremental installation performance.
- **fastboot**
  - Add support for compressed snapshot merges.
  - Restore legacy A/B support.

#### 31.0.0 (February 2021)

- **adb**
  - Disable compression on pull by default.

#### 30.0.5 (November 2020)

- **adb**
  - Improve performance of `adb push` when pushing many files over a high-latency connection.
  - Improve `adb push/pull` performance on Windows.
  - Fix `adb push --sync` with multiple inputs.
  - Improve performance of incremental apk installation.
  - Improve error handling for incremental apk installation.

#### 30.0.4 (July 2020)

- **adb**
  - Fix fallback to non-incremental apk installation on pre-Android 11 devices.
  - Fix `adb install-multi-package`.
  - Fix some more crashes related to adb wireless pairing.
  - Improve some error messages.
- **fastboot**
  - Improve console output on `fastboot oem` commands.
  - Fix `fastboot flashall` on older devices such as Nexus 7.

#### 30.0.3 (June 2020)

- **adb**
  - Fix installation of APKs signed with v4 signature scheme on pre-Android 11 devices.
  - Fix crash when authenticating without `ADB_VENDOR_KEYS`.
  - Fix crash when using `adb -H`.

#### 30.0.2 (June 2020)

- **adb**
  - Improve adb wireless pairing.
  - Fix hang in `adb logcat` when run before a device is connected.
  - Add `adb transport-id` to allow scripts to safely wait for a device to go away after root/unroot/reboot.

#### 30.0.1 (May 2020)

- **adb**
  - Disable adb mdns auto-connection by default. This can be reenabled with the `ADB_MDNS_AUTO_CONNECT` environment variable.
  - Improve performance of `adb install-multi` on Android 10 or newer devices.
  - Fix timeout when using `adb root/unroot` on a device connected over TCP.
  - Update support for wireless pairing.

#### 30.0.0 (April 2020)

- **adb**
  - Add initial support for [wireless pairing](https://developer.android.com/about/versions/11/features#wireless-adb).
  - Add support for [incremental APK installation](https://developer.android.com/about/versions/11/features#incremental).
  - Implement client-side support for compression of `adb {push, pull, sync}` when used with an Android 11 device.
  - Improve performance of `adb push` on high-latency connections.
  - Improve push/pull performance on Windows.

#### 29.0.6 (February 2020)

- **adb**
  - 64-bit size/time support for `adb ls` when used with an Android 11 device.
  - Support listening on `::1` on POSIX.
  - Client support for WinUSB devices that publish a WinUSB descriptor (required for Android 11) should no longer require a USB driver to be installed.
  - Fix hang when using `adb install` on something that isn't actually a file.

#### 29.0.5 (October 2019)

- **adb**
  - Slight performance improvement on Linux when using many simultaneous connections.
  - Add `--fastdeploy` option to `adb install`, for incremental updates to APKs while developing.

#### 29.0.4 (September 2019)

- **adb**
  - Hotfix for native debugging timeout with LLDB (see [issue #134613180](https://issuetracker.google.com/134613180)). This also fixes a related bug in the Android Studio Profilers that causes an `AdbCommandRejectedException`, which you can see in the `idea.log` file.

#### 29.0.3 (September 2019)

- **adb**
  - `adb forward --list` works with multiple devices connected.
  - Fix devices going offline on Windows.
  - Improve `adb install` output and help text.
  - Restore previous behavior of `adb connect <host>` without specifying port.

#### 29.0.2 (July 2019)

- **adb**
  - Fixes a Windows heap integrity crash.
- **fastboot**
  - Adds support for partition layout of upcoming devices.

#### 29.0.1 (June 2019)

- **adb**
  - Hotfix for Windows crashes (https://issuetracker.google.com/134613180)

#### 29.0.0 (June 2019)

- **adb**
  - `adb reconnect` performs a USB reset on Linux.
  - On Linux, when connecting to a newer adb server, instead of killing the server and starting an older one, adb attempts to launch the newer version transparently.
  - `adb root` waits for the device to reconnect after disconnecting. Previously, `adb root; adb wait-for-device` could mistakenly return immediately if `adb wait-for-device` started before adb noticed that the device had disconnected.
- **fastboot**
  - Disables an error message that occurred when fastboot attempted to open the touch bar or keyboard on macOS.

#### 28.0.2 (March 2019)

- **adb**
  - Fixes flakiness of `adb shell` port forwarding that leads to "Connection reset by peer" error message.
  - Fixes authentication via `ADB_VENDOR_KEYS` when reconnecting devices.
  - Fixes authentication---when the private key used for authentication does not match the public key---by calculating the public key from the private key, instead of assuming that they match.
- **fastboot**
  - Adds support for dynamic partitions.
- **Updated Windows requirements**
  - The platform tools now depend on the Windows Universal C Runtime, which is usually installed by default via Windows Update. If you see errors mentioning missing DLLs, you may need to manually fetch and install the [runtime
    package](https://support.microsoft.com/en-ca/help/2999226/update-for-universal-c-runtime-in-windows).

#### 28.0.1 (September 2018)

- **adb**
  - Add support for reconnection of TCP connections. Upon disconnection, adb will attempt to reconnect for up to 60 seconds before abandoning a connection.
  - Fix Unicode console output on Windows. (Thanks to external contributor Spencer Low!)
  - Fix a file descriptor double-close that can occur, resulting in connections being closed when an `adb connect` happens simultaneously.
  - Fix `adb forward --list` when used with more than one device connected.
- **fastboot**
  - Increase command timeout to 30 seconds, to better support some slow bootloader commands.

#### 28.0.0 (June 2018)

- **adb** :
  - Add support for checksum-less operation with devices running Android P, which improves throughput by up to 40%.
  - Sort output of `adb devices` by connection type and device serial.
  - Increase the socket listen backlog to allow for more simultaneous adb commands.
  - Improve error output for `adb connect`.
- **fastboot** :
  - Improve output format, add a verbose output mode (`-v`).
  - Clean up help output.
  - Add `product.img` and `odm.img` to the list of partitions flashed by `fastboot flashall`.
  - Avoid bricking new devices when using a too-old version of fastboot by allowing factory image packages to require support for specific partitions.

#### 27.0.1 (December 2017)

- **adb:** fixes an assertion failure on MacOS that occurred when connecting devices using USB 3.0.
- **Fastboot:** On Windows, adds support for wiping devices that use F2FS (Flash-Friendly File System).

#### 27.0.0 (December 2017)

- Re-fixes the macOS 10.13 fastboot bug first fixed in 26.0.1, but re-introduced in 26.0.2.

#### 26.0.2 (October 2017)

- Add fastboot support for Pixel 2 devices.

#### 26.0.1 (September 2017)

- Fixed fastboot problems on macOS 10.13 High Sierra ([bug 64292422](https://issuetracker.google.com/64292422)).

#### 26.0.0 (June 2017)

- Updated with the release of Android O final SDK (API level 26).

#### 25.0.5 (April 24, 2017)

- Fixed adb sideload of large updates on Windows, manifesting as
  "std::bad_alloc" ([bug
  37139736](https://issuetracker.google.com/37139736)).

- Fixed adb problems with some Windows firewalls, manifesting as "cannot open
  transport registration socketpair"
  ([bug 37139725](https://issuetracker.google.com/37139725)).

- Both `adb --version` and `fastboot --version` now include the install path.

- Changed adb to not resolve `localhost` to work around misconfigured VPN.

- Changed adb to no longer reset USB devices on Linux, which could affect
  other attached USB devices.

#### 25.0.4 (March 16, 2017)

- Added experimental libusb support to Linux and Mac adb

To use the libusb backend, set the environment variable ADB_LIBUSB=true before
launching a new adb server. The new `adb host-features` command will tell you
whether or not you're using libusb.

To restart adb with libusb and check that it worked, use `adb kill-server;
ADB_LIBUSB=1 adb start-server; adb host-features`. The output should include
"libusb".

In this release, the old non-libusb implementation remains the default.

- fastboot doesn't hang 2016 MacBook Pros anymore
  ([bug
  231129](https://code.google.com/p/android/issues/detail?id=231129))

- Fixed Systrace command line capture on Mac

#### 25.0.3 (December 16, 2016)

- Fixed fastboot bug causing Android Things devices to fail to flash

#### 25.0.2 (December 12, 2016)

- Updated with the Android N MR1 Stable release (API 25)

#### 25.0.1 (November 22, 2016)

- Updated with the release of Android N MR1 Developer Preview 2 release (API 25)

#### 25.0.0 (October 19, 2016)

- Updated with the release of Android N MR1 Developer Preview 1 release (API 25)

#### 24.0.4 (October 14, 2016)

- Updated to address issues in ADB and Mac OS Sierra

## Download Android SDK Platform-Tools

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

This is the Android Software Development Kit License Agreement

### 1. Introduction

1.1 The Android Software Development Kit (referred to in the License Agreement as the "SDK" and specifically including the Android system files, packaged APIs, and Google APIs add-ons) is licensed to you subject to the terms of the License Agreement. The License Agreement forms a legally binding contract between you and Google in relation to your use of the SDK. 1.2 "Android" means the Android software stack for devices, as made available under the Android Open Source Project, which is located at the following URL: https://source.android.com/, as updated from time to time. 1.3 A "compatible implementation" means any Android device that (i) complies with the Android Compatibility Definition document, which can be found at the Android compatibility website (https://source.android.com/compatibility) and which may be updated from time to time; and (ii) successfully passes the Android Compatibility Test Suite (CTS). 1.4 "Google" means Google LLC, organized under the laws of the State of Delaware, USA, and operating under the laws of the USA with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, USA.

### 2. Accepting this License Agreement

2.1 In order to use the SDK, you must first agree to the License Agreement. You may not use the SDK if you do not accept the License Agreement. 2.2 By clicking to accept and/or using this SDK, you hereby agree to the terms of the License Agreement. 2.3 You may not use the SDK and may not accept the License Agreement if you are a person barred from receiving the SDK under the laws of the United States or other countries, including the country in which you are resident or from which you use the SDK. 2.4 If you are agreeing to be bound by the License Agreement on behalf of your employer or other entity, you represent and warrant that you have full legal authority to bind your employer or such entity to the License Agreement. If you do not have the requisite authority, you may not accept the License Agreement or use the SDK on behalf of your employer or other entity.

### 3. SDK License from Google

3.1 Subject to the terms of the License Agreement, Google grants you a limited, worldwide, royalty-free, non-assignable, non-exclusive, and non-sublicensable license to use the SDK solely to develop applications for compatible implementations of Android. 3.2 You may not use this SDK to develop applications for other platforms (including non-compatible implementations of Android) or to develop another SDK. You are of course free to develop applications for other platforms, including non-compatible implementations of Android, provided that this SDK is not used for that purpose. 3.3 You agree that Google or third parties own all legal right, title and interest in and to the SDK, including any Intellectual Property Rights that subsist in the SDK. "Intellectual Property Rights" means any and all rights under patent law, copyright law, trade secret law, trademark law, and any and all other proprietary rights. Google reserves all rights not expressly granted to you. 3.4 You may not use the SDK for any purpose not expressly permitted by the License Agreement. Except to the extent required by applicable third party licenses, you may not copy (except for backup purposes), modify, adapt, redistribute, decompile, reverse engineer, disassemble, or create derivative works of the SDK or any part of the SDK. 3.5 Use, reproduction and distribution of components of the SDK licensed under an open source software license are governed solely by the terms of that open source software license and not the License Agreement. 3.6 You agree that the form and nature of the SDK that Google provides may change without prior notice to you and that future versions of the SDK may be incompatible with applications developed on previous versions of the SDK. You agree that Google may stop (permanently or temporarily) providing the SDK (or any features within the SDK) to you or to users generally at Google's sole discretion, without prior notice to you. 3.7 Nothing in the License Agreement gives you a right to use any of Google's trade names, trademarks, service marks, logos, domain names, or other distinctive brand features. 3.8 You agree that you will not remove, obscure, or alter any proprietary rights notices (including copyright and trademark notices) that may be affixed to or contained within the SDK.

### 4. Use of the SDK by You

4.1 Google agrees that it obtains no right, title or interest from you (or your licensors) under the License Agreement in or to any software applications that you develop using the SDK, including any intellectual property rights that subsist in those applications. 4.2 You agree to use the SDK and write applications only for purposes that are permitted by (a) the License Agreement and (b) any applicable law, regulation or generally accepted practices or guidelines in the relevant jurisdictions (including any laws regarding the export of data or software to and from the United States or other relevant countries). 4.3 You agree that if you use the SDK to develop applications for general public users, you will protect the privacy and legal rights of those users. If the users provide you with user names, passwords, or other login information or personal information, you must make the users aware that the information will be available to your application, and you must provide legally adequate privacy notice and protection for those users. If your application stores personal or sensitive information provided by users, it must do so securely. If the user provides your application with Google Account information, your application may only use that information to access the user's Google Account when, and for the limited purposes for which, the user has given you permission to do so. 4.4 You agree that you will not engage in any activity with the SDK, including the development or distribution of an application, that interferes with, disrupts, damages, or accesses in an unauthorized manner the servers, networks, or other properties or services of any third party including, but not limited to, Google or any mobile communications carrier. 4.5 You agree that you are solely responsible for (and that Google has no responsibility to you or to any third party for) any data, content, or resources that you create, transmit or display through Android and/or applications for Android, and for the consequences of your actions (including any loss or damage which Google may suffer) by doing so. 4.6 You agree that you are solely responsible for (and that Google has no responsibility to you or to any third party for) any breach of your obligations under the License Agreement, any applicable third party contract or Terms of Service, or any applicable law or regulation, and for the consequences (including any loss or damage which Google or any third party may suffer) of any such breach.

### 5. Your Developer Credentials

5.1 You agree that you are responsible for maintaining the confidentiality of any developer credentials that may be issued to you by Google or which you may choose yourself and that you will be solely responsible for all applications that are developed under your developer credentials.

### 6. Privacy and Information

6.1 In order to continually innovate and improve the SDK, Google may collect certain usage statistics from the software including but not limited to a unique identifier, associated IP address, version number of the software, and information on which tools and/or services in the SDK are being used and how they are being used. Before any of this information is collected, the SDK will notify you and seek your consent. If you withhold consent, the information will not be collected. 6.2 The data collected is examined in the aggregate to improve the SDK and is maintained in accordance with Google's Privacy Policy, which is located at the following URL: https://policies.google.com/privacy 6.3 Anonymized and aggregated sets of the data may be shared with Google partners to improve the SDK.

### 7. Third Party Applications

7.1 If you use the SDK to run applications developed by a third party or that access data, content or resources provided by a third party, you agree that Google is not responsible for those applications, data, content, or resources. You understand that all data, content or resources which you may access through such third party applications are the sole responsibility of the person from which they originated and that Google is not liable for any loss or damage that you may experience as a result of the use or access of any of those third party applications, data, content, or resources. 7.2 You should be aware the data, content, and resources presented to you through such a third party application may be protected by intellectual property rights which are owned by the providers (or by other persons or companies on their behalf). You may not modify, rent, lease, loan, sell, distribute or create derivative works based on these data, content, or resources (either in whole or in part) unless you have been specifically given permission to do so by the relevant owners. 7.3 You acknowledge that your use of such third party applications, data, content, or resources may be subject to separate terms between you and the relevant third party. In that case, the License Agreement does not affect your legal relationship with these third parties.

### 8. Using Android APIs

8.1 Google Data APIs 8.1.1 If you use any API to retrieve data from Google, you acknowledge that the data may be protected by intellectual property rights which are owned by Google or those parties that provide the data (or by other persons or companies on their behalf). Your use of any such API may be subject to additional Terms of Service. You may not modify, rent, lease, loan, sell, distribute or create derivative works based on this data (either in whole or in part) unless allowed by the relevant Terms of Service. 8.1.2 If you use any API to retrieve a user's data from Google, you acknowledge and agree that you shall retrieve data only with the user's explicit consent and only when, and for the limited purposes for which, the user has given you permission to do so. If you use the Android Recognition Service API, documented at the following URL: <https://developer.android.com/reference/android/speech/RecognitionService>, as updated from time to time, you acknowledge that the use of the API is subject to the Data Processing Addendum for Products where Google is a Data Processor, which is located at the following URL: <https://privacy.google.com/businesses/gdprprocessorterms/>, as updated from time to time. By clicking to accept, you hereby agree to the terms of the Data Processing Addendum for Products where Google is a Data Processor.

### 9. Terminating this License Agreement

9.1 The License Agreement will continue to apply until terminated by either you or Google as set out below. 9.2 If you want to terminate the License Agreement, you may do so by ceasing your use of the SDK and any relevant developer credentials. 9.3 Google may at any time, terminate the License Agreement with you if: (A) you have breached any provision of the License Agreement; or (B) Google is required to do so by law; or (C) the partner with whom Google offered certain parts of SDK (such as APIs) to you has terminated its relationship with Google or ceased to offer certain parts of the SDK to you; or (D) Google decides to no longer provide the SDK or certain parts of the SDK to users in the country in which you are resident or from which you use the service, or the provision of the SDK or certain SDK services to you by Google is, in Google's sole discretion, no longer commercially viable. 9.4 When the License Agreement comes to an end, all of the legal rights, obligations and liabilities that you and Google have benefited from, been subject to (or which have accrued over time whilst the License Agreement has been in force) or which are expressed to continue indefinitely, shall be unaffected by this cessation, and the provisions of paragraph 14.7 shall continue to apply to such rights, obligations and liabilities indefinitely.

### 10. DISCLAIMER OF WARRANTIES

10.1 YOU EXPRESSLY UNDERSTAND AND AGREE THAT YOUR USE OF THE SDK IS AT YOUR SOLE RISK AND THAT THE SDK IS PROVIDED "AS IS" AND "AS AVAILABLE" WITHOUT WARRANTY OF ANY KIND FROM GOOGLE. 10.2 YOUR USE OF THE SDK AND ANY MATERIAL DOWNLOADED OR OTHERWISE OBTAINED THROUGH THE USE OF THE SDK IS AT YOUR OWN DISCRETION AND RISK AND YOU ARE SOLELY RESPONSIBLE FOR ANY DAMAGE TO YOUR COMPUTER SYSTEM OR OTHER DEVICE OR LOSS OF DATA THAT RESULTS FROM SUCH USE. 10.3 GOOGLE FURTHER EXPRESSLY DISCLAIMS ALL WARRANTIES AND CONDITIONS OF ANY KIND, WHETHER EXPRESS OR IMPLIED, INCLUDING, BUT NOT LIMITED TO THE IMPLIED WARRANTIES AND CONDITIONS OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT.

### 11. LIMITATION OF LIABILITY

11.1 YOU EXPRESSLY UNDERSTAND AND AGREE THAT GOOGLE, ITS SUBSIDIARIES AND AFFILIATES, AND ITS LICENSORS SHALL NOT BE LIABLE TO YOU UNDER ANY THEORY OF LIABILITY FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, CONSEQUENTIAL OR EXEMPLARY DAMAGES THAT MAY BE INCURRED BY YOU, INCLUDING ANY LOSS OF DATA, WHETHER OR NOT GOOGLE OR ITS REPRESENTATIVES HAVE BEEN ADVISED OF OR SHOULD HAVE BEEN AWARE OF THE POSSIBILITY OF ANY SUCH LOSSES ARISING.

### 12. Indemnification

12.1 To the maximum extent permitted by law, you agree to defend, indemnify and hold harmless Google, its affiliates and their respective directors, officers, employees and agents from and against any and all claims, actions, suits or proceedings, as well as any and all losses, liabilities, damages, costs and expenses (including reasonable attorneys fees) arising out of or accruing from (a) your use of the SDK, (b) any application you develop on the SDK that infringes any copyright, trademark, trade secret, trade dress, patent or other intellectual property right of any person or defames any person or violates their rights of publicity or privacy, and (c) any non-compliance by you with the License Agreement.

### 13. Changes to the License Agreement

13.1 Google may make changes to the License Agreement as it distributes new versions of the SDK. When these changes are made, Google will make a new version of the License Agreement available on the website where the SDK is made available.

### 14. General Legal Terms

14.1 The License Agreement constitutes the whole legal agreement between you and Google and governs your use of the SDK (excluding any services which Google may provide to you under a separate written agreement), and completely replaces any prior agreements between you and Google in relation to the SDK. 14.2 You agree that if Google does not exercise or enforce any legal right or remedy which is contained in the License Agreement (or which Google has the benefit of under any applicable law), this will not be taken to be a formal waiver of Google's rights and that those rights or remedies will still be available to Google. 14.3 If any court of law, having the jurisdiction to decide on this matter, rules that any provision of the License Agreement is invalid, then that provision will be removed from the License Agreement without affecting the rest of the License Agreement. The remaining provisions of the License Agreement will continue to be valid and enforceable. 14.4 You acknowledge and agree that each member of the group of companies of which Google is the parent shall be third party beneficiaries to the License Agreement and that such other companies shall be entitled to directly enforce, and rely upon, any provision of the License Agreement that confers a benefit on (or rights in favor of) them. Other than this, no other person or company shall be third party beneficiaries to the License Agreement. 14.5 EXPORT RESTRICTIONS. THE SDK IS SUBJECT TO UNITED STATES EXPORT LAWS AND REGULATIONS. YOU MUST COMPLY WITH ALL DOMESTIC AND INTERNATIONAL EXPORT LAWS AND REGULATIONS THAT APPLY TO THE SDK. THESE LAWS INCLUDE RESTRICTIONS ON DESTINATIONS, END USERS AND END USE. 14.6 The rights granted in the License Agreement may not be assigned or transferred by either you or Google without the prior written approval of the other party. Neither you nor Google shall be permitted to delegate their responsibilities or obligations under the License Agreement without the prior written approval of the other party. 14.7 The License Agreement, and your relationship with Google under the License Agreement, shall be governed by the laws of the State of California without regard to its conflict of laws provisions. You and Google agree to submit to the exclusive jurisdiction of the courts located within the county of Santa Clara, California to resolve any legal matter arising from the License Agreement. Notwithstanding this, you agree that Google shall still be allowed to apply for injunctive remedies (or an equivalent type of urgent legal relief) in any jurisdiction. *July 27, 2021* I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android SDK Platform-Tools for Windows </button> [Download Android SDK Platform-Tools
for
Windows](https://dl.google.com/android/repository/platform-tools-latest-windows.zip)

*platform-tools-latest-windows.zip*

<br />

## Download Android SDK Platform-Tools

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

This is the Android Software Development Kit License Agreement

### 1. Introduction

1.1 The Android Software Development Kit (referred to in the License Agreement as the "SDK" and specifically including the Android system files, packaged APIs, and Google APIs add-ons) is licensed to you subject to the terms of the License Agreement. The License Agreement forms a legally binding contract between you and Google in relation to your use of the SDK. 1.2 "Android" means the Android software stack for devices, as made available under the Android Open Source Project, which is located at the following URL: https://source.android.com/, as updated from time to time. 1.3 A "compatible implementation" means any Android device that (i) complies with the Android Compatibility Definition document, which can be found at the Android compatibility website (https://source.android.com/compatibility) and which may be updated from time to time; and (ii) successfully passes the Android Compatibility Test Suite (CTS). 1.4 "Google" means Google LLC, organized under the laws of the State of Delaware, USA, and operating under the laws of the USA with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, USA.

### 2. Accepting this License Agreement

2.1 In order to use the SDK, you must first agree to the License Agreement. You may not use the SDK if you do not accept the License Agreement. 2.2 By clicking to accept and/or using this SDK, you hereby agree to the terms of the License Agreement. 2.3 You may not use the SDK and may not accept the License Agreement if you are a person barred from receiving the SDK under the laws of the United States or other countries, including the country in which you are resident or from which you use the SDK. 2.4 If you are agreeing to be bound by the License Agreement on behalf of your employer or other entity, you represent and warrant that you have full legal authority to bind your employer or such entity to the License Agreement. If you do not have the requisite authority, you may not accept the License Agreement or use the SDK on behalf of your employer or other entity.

### 3. SDK License from Google

3.1 Subject to the terms of the License Agreement, Google grants you a limited, worldwide, royalty-free, non-assignable, non-exclusive, and non-sublicensable license to use the SDK solely to develop applications for compatible implementations of Android. 3.2 You may not use this SDK to develop applications for other platforms (including non-compatible implementations of Android) or to develop another SDK. You are of course free to develop applications for other platforms, including non-compatible implementations of Android, provided that this SDK is not used for that purpose. 3.3 You agree that Google or third parties own all legal right, title and interest in and to the SDK, including any Intellectual Property Rights that subsist in the SDK. "Intellectual Property Rights" means any and all rights under patent law, copyright law, trade secret law, trademark law, and any and all other proprietary rights. Google reserves all rights not expressly granted to you. 3.4 You may not use the SDK for any purpose not expressly permitted by the License Agreement. Except to the extent required by applicable third party licenses, you may not copy (except for backup purposes), modify, adapt, redistribute, decompile, reverse engineer, disassemble, or create derivative works of the SDK or any part of the SDK. 3.5 Use, reproduction and distribution of components of the SDK licensed under an open source software license are governed solely by the terms of that open source software license and not the License Agreement. 3.6 You agree that the form and nature of the SDK that Google provides may change without prior notice to you and that future versions of the SDK may be incompatible with applications developed on previous versions of the SDK. You agree that Google may stop (permanently or temporarily) providing the SDK (or any features within the SDK) to you or to users generally at Google's sole discretion, without prior notice to you. 3.7 Nothing in the License Agreement gives you a right to use any of Google's trade names, trademarks, service marks, logos, domain names, or other distinctive brand features. 3.8 You agree that you will not remove, obscure, or alter any proprietary rights notices (including copyright and trademark notices) that may be affixed to or contained within the SDK.

### 4. Use of the SDK by You

4.1 Google agrees that it obtains no right, title or interest from you (or your licensors) under the License Agreement in or to any software applications that you develop using the SDK, including any intellectual property rights that subsist in those applications. 4.2 You agree to use the SDK and write applications only for purposes that are permitted by (a) the License Agreement and (b) any applicable law, regulation or generally accepted practices or guidelines in the relevant jurisdictions (including any laws regarding the export of data or software to and from the United States or other relevant countries). 4.3 You agree that if you use the SDK to develop applications for general public users, you will protect the privacy and legal rights of those users. If the users provide you with user names, passwords, or other login information or personal information, you must make the users aware that the information will be available to your application, and you must provide legally adequate privacy notice and protection for those users. If your application stores personal or sensitive information provided by users, it must do so securely. If the user provides your application with Google Account information, your application may only use that information to access the user's Google Account when, and for the limited purposes for which, the user has given you permission to do so. 4.4 You agree that you will not engage in any activity with the SDK, including the development or distribution of an application, that interferes with, disrupts, damages, or accesses in an unauthorized manner the servers, networks, or other properties or services of any third party including, but not limited to, Google or any mobile communications carrier. 4.5 You agree that you are solely responsible for (and that Google has no responsibility to you or to any third party for) any data, content, or resources that you create, transmit or display through Android and/or applications for Android, and for the consequences of your actions (including any loss or damage which Google may suffer) by doing so. 4.6 You agree that you are solely responsible for (and that Google has no responsibility to you or to any third party for) any breach of your obligations under the License Agreement, any applicable third party contract or Terms of Service, or any applicable law or regulation, and for the consequences (including any loss or damage which Google or any third party may suffer) of any such breach.

### 5. Your Developer Credentials

5.1 You agree that you are responsible for maintaining the confidentiality of any developer credentials that may be issued to you by Google or which you may choose yourself and that you will be solely responsible for all applications that are developed under your developer credentials.

### 6. Privacy and Information

6.1 In order to continually innovate and improve the SDK, Google may collect certain usage statistics from the software including but not limited to a unique identifier, associated IP address, version number of the software, and information on which tools and/or services in the SDK are being used and how they are being used. Before any of this information is collected, the SDK will notify you and seek your consent. If you withhold consent, the information will not be collected. 6.2 The data collected is examined in the aggregate to improve the SDK and is maintained in accordance with Google's Privacy Policy, which is located at the following URL: https://policies.google.com/privacy 6.3 Anonymized and aggregated sets of the data may be shared with Google partners to improve the SDK.

### 7. Third Party Applications

7.1 If you use the SDK to run applications developed by a third party or that access data, content or resources provided by a third party, you agree that Google is not responsible for those applications, data, content, or resources. You understand that all data, content or resources which you may access through such third party applications are the sole responsibility of the person from which they originated and that Google is not liable for any loss or damage that you may experience as a result of the use or access of any of those third party applications, data, content, or resources. 7.2 You should be aware the data, content, and resources presented to you through such a third party application may be protected by intellectual property rights which are owned by the providers (or by other persons or companies on their behalf). You may not modify, rent, lease, loan, sell, distribute or create derivative works based on these data, content, or resources (either in whole or in part) unless you have been specifically given permission to do so by the relevant owners. 7.3 You acknowledge that your use of such third party applications, data, content, or resources may be subject to separate terms between you and the relevant third party. In that case, the License Agreement does not affect your legal relationship with these third parties.

### 8. Using Android APIs

8.1 Google Data APIs 8.1.1 If you use any API to retrieve data from Google, you acknowledge that the data may be protected by intellectual property rights which are owned by Google or those parties that provide the data (or by other persons or companies on their behalf). Your use of any such API may be subject to additional Terms of Service. You may not modify, rent, lease, loan, sell, distribute or create derivative works based on this data (either in whole or in part) unless allowed by the relevant Terms of Service. 8.1.2 If you use any API to retrieve a user's data from Google, you acknowledge and agree that you shall retrieve data only with the user's explicit consent and only when, and for the limited purposes for which, the user has given you permission to do so. If you use the Android Recognition Service API, documented at the following URL: <https://developer.android.com/reference/android/speech/RecognitionService>, as updated from time to time, you acknowledge that the use of the API is subject to the Data Processing Addendum for Products where Google is a Data Processor, which is located at the following URL: <https://privacy.google.com/businesses/gdprprocessorterms/>, as updated from time to time. By clicking to accept, you hereby agree to the terms of the Data Processing Addendum for Products where Google is a Data Processor.

### 9. Terminating this License Agreement

9.1 The License Agreement will continue to apply until terminated by either you or Google as set out below. 9.2 If you want to terminate the License Agreement, you may do so by ceasing your use of the SDK and any relevant developer credentials. 9.3 Google may at any time, terminate the License Agreement with you if: (A) you have breached any provision of the License Agreement; or (B) Google is required to do so by law; or (C) the partner with whom Google offered certain parts of SDK (such as APIs) to you has terminated its relationship with Google or ceased to offer certain parts of the SDK to you; or (D) Google decides to no longer provide the SDK or certain parts of the SDK to users in the country in which you are resident or from which you use the service, or the provision of the SDK or certain SDK services to you by Google is, in Google's sole discretion, no longer commercially viable. 9.4 When the License Agreement comes to an end, all of the legal rights, obligations and liabilities that you and Google have benefited from, been subject to (or which have accrued over time whilst the License Agreement has been in force) or which are expressed to continue indefinitely, shall be unaffected by this cessation, and the provisions of paragraph 14.7 shall continue to apply to such rights, obligations and liabilities indefinitely.

### 10. DISCLAIMER OF WARRANTIES

10.1 YOU EXPRESSLY UNDERSTAND AND AGREE THAT YOUR USE OF THE SDK IS AT YOUR SOLE RISK AND THAT THE SDK IS PROVIDED "AS IS" AND "AS AVAILABLE" WITHOUT WARRANTY OF ANY KIND FROM GOOGLE. 10.2 YOUR USE OF THE SDK AND ANY MATERIAL DOWNLOADED OR OTHERWISE OBTAINED THROUGH THE USE OF THE SDK IS AT YOUR OWN DISCRETION AND RISK AND YOU ARE SOLELY RESPONSIBLE FOR ANY DAMAGE TO YOUR COMPUTER SYSTEM OR OTHER DEVICE OR LOSS OF DATA THAT RESULTS FROM SUCH USE. 10.3 GOOGLE FURTHER EXPRESSLY DISCLAIMS ALL WARRANTIES AND CONDITIONS OF ANY KIND, WHETHER EXPRESS OR IMPLIED, INCLUDING, BUT NOT LIMITED TO THE IMPLIED WARRANTIES AND CONDITIONS OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT.

### 11. LIMITATION OF LIABILITY

11.1 YOU EXPRESSLY UNDERSTAND AND AGREE THAT GOOGLE, ITS SUBSIDIARIES AND AFFILIATES, AND ITS LICENSORS SHALL NOT BE LIABLE TO YOU UNDER ANY THEORY OF LIABILITY FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, CONSEQUENTIAL OR EXEMPLARY DAMAGES THAT MAY BE INCURRED BY YOU, INCLUDING ANY LOSS OF DATA, WHETHER OR NOT GOOGLE OR ITS REPRESENTATIVES HAVE BEEN ADVISED OF OR SHOULD HAVE BEEN AWARE OF THE POSSIBILITY OF ANY SUCH LOSSES ARISING.

### 12. Indemnification

12.1 To the maximum extent permitted by law, you agree to defend, indemnify and hold harmless Google, its affiliates and their respective directors, officers, employees and agents from and against any and all claims, actions, suits or proceedings, as well as any and all losses, liabilities, damages, costs and expenses (including reasonable attorneys fees) arising out of or accruing from (a) your use of the SDK, (b) any application you develop on the SDK that infringes any copyright, trademark, trade secret, trade dress, patent or other intellectual property right of any person or defames any person or violates their rights of publicity or privacy, and (c) any non-compliance by you with the License Agreement.

### 13. Changes to the License Agreement

13.1 Google may make changes to the License Agreement as it distributes new versions of the SDK. When these changes are made, Google will make a new version of the License Agreement available on the website where the SDK is made available.

### 14. General Legal Terms

14.1 The License Agreement constitutes the whole legal agreement between you and Google and governs your use of the SDK (excluding any services which Google may provide to you under a separate written agreement), and completely replaces any prior agreements between you and Google in relation to the SDK. 14.2 You agree that if Google does not exercise or enforce any legal right or remedy which is contained in the License Agreement (or which Google has the benefit of under any applicable law), this will not be taken to be a formal waiver of Google's rights and that those rights or remedies will still be available to Google. 14.3 If any court of law, having the jurisdiction to decide on this matter, rules that any provision of the License Agreement is invalid, then that provision will be removed from the License Agreement without affecting the rest of the License Agreement. The remaining provisions of the License Agreement will continue to be valid and enforceable. 14.4 You acknowledge and agree that each member of the group of companies of which Google is the parent shall be third party beneficiaries to the License Agreement and that such other companies shall be entitled to directly enforce, and rely upon, any provision of the License Agreement that confers a benefit on (or rights in favor of) them. Other than this, no other person or company shall be third party beneficiaries to the License Agreement. 14.5 EXPORT RESTRICTIONS. THE SDK IS SUBJECT TO UNITED STATES EXPORT LAWS AND REGULATIONS. YOU MUST COMPLY WITH ALL DOMESTIC AND INTERNATIONAL EXPORT LAWS AND REGULATIONS THAT APPLY TO THE SDK. THESE LAWS INCLUDE RESTRICTIONS ON DESTINATIONS, END USERS AND END USE. 14.6 The rights granted in the License Agreement may not be assigned or transferred by either you or Google without the prior written approval of the other party. Neither you nor Google shall be permitted to delegate their responsibilities or obligations under the License Agreement without the prior written approval of the other party. 14.7 The License Agreement, and your relationship with Google under the License Agreement, shall be governed by the laws of the State of California without regard to its conflict of laws provisions. You and Google agree to submit to the exclusive jurisdiction of the courts located within the county of Santa Clara, California to resolve any legal matter arising from the License Agreement. Notwithstanding this, you agree that Google shall still be allowed to apply for injunctive remedies (or an equivalent type of urgent legal relief) in any jurisdiction. *July 27, 2021* I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android SDK Platform-Tools for Mac </button> [Download Android SDK Platform-Tools
for
Mac](https://dl.google.com/android/repository/platform-tools-latest-darwin.zip)

*platform-tools-latest-darwin.zip*

<br />

## Download Android SDK Platform-Tools

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

This is the Android Software Development Kit License Agreement

### 1. Introduction

1.1 The Android Software Development Kit (referred to in the License Agreement as the "SDK" and specifically including the Android system files, packaged APIs, and Google APIs add-ons) is licensed to you subject to the terms of the License Agreement. The License Agreement forms a legally binding contract between you and Google in relation to your use of the SDK. 1.2 "Android" means the Android software stack for devices, as made available under the Android Open Source Project, which is located at the following URL: https://source.android.com/, as updated from time to time. 1.3 A "compatible implementation" means any Android device that (i) complies with the Android Compatibility Definition document, which can be found at the Android compatibility website (https://source.android.com/compatibility) and which may be updated from time to time; and (ii) successfully passes the Android Compatibility Test Suite (CTS). 1.4 "Google" means Google LLC, organized under the laws of the State of Delaware, USA, and operating under the laws of the USA with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, USA.

### 2. Accepting this License Agreement

2.1 In order to use the SDK, you must first agree to the License Agreement. You may not use the SDK if you do not accept the License Agreement. 2.2 By clicking to accept and/or using this SDK, you hereby agree to the terms of the License Agreement. 2.3 You may not use the SDK and may not accept the License Agreement if you are a person barred from receiving the SDK under the laws of the United States or other countries, including the country in which you are resident or from which you use the SDK. 2.4 If you are agreeing to be bound by the License Agreement on behalf of your employer or other entity, you represent and warrant that you have full legal authority to bind your employer or such entity to the License Agreement. If you do not have the requisite authority, you may not accept the License Agreement or use the SDK on behalf of your employer or other entity.

### 3. SDK License from Google

3.1 Subject to the terms of the License Agreement, Google grants you a limited, worldwide, royalty-free, non-assignable, non-exclusive, and non-sublicensable license to use the SDK solely to develop applications for compatible implementations of Android. 3.2 You may not use this SDK to develop applications for other platforms (including non-compatible implementations of Android) or to develop another SDK. You are of course free to develop applications for other platforms, including non-compatible implementations of Android, provided that this SDK is not used for that purpose. 3.3 You agree that Google or third parties own all legal right, title and interest in and to the SDK, including any Intellectual Property Rights that subsist in the SDK. "Intellectual Property Rights" means any and all rights under patent law, copyright law, trade secret law, trademark law, and any and all other proprietary rights. Google reserves all rights not expressly granted to you. 3.4 You may not use the SDK for any purpose not expressly permitted by the License Agreement. Except to the extent required by applicable third party licenses, you may not copy (except for backup purposes), modify, adapt, redistribute, decompile, reverse engineer, disassemble, or create derivative works of the SDK or any part of the SDK. 3.5 Use, reproduction and distribution of components of the SDK licensed under an open source software license are governed solely by the terms of that open source software license and not the License Agreement. 3.6 You agree that the form and nature of the SDK that Google provides may change without prior notice to you and that future versions of the SDK may be incompatible with applications developed on previous versions of the SDK. You agree that Google may stop (permanently or temporarily) providing the SDK (or any features within the SDK) to you or to users generally at Google's sole discretion, without prior notice to you. 3.7 Nothing in the License Agreement gives you a right to use any of Google's trade names, trademarks, service marks, logos, domain names, or other distinctive brand features. 3.8 You agree that you will not remove, obscure, or alter any proprietary rights notices (including copyright and trademark notices) that may be affixed to or contained within the SDK.

### 4. Use of the SDK by You

4.1 Google agrees that it obtains no right, title or interest from you (or your licensors) under the License Agreement in or to any software applications that you develop using the SDK, including any intellectual property rights that subsist in those applications. 4.2 You agree to use the SDK and write applications only for purposes that are permitted by (a) the License Agreement and (b) any applicable law, regulation or generally accepted practices or guidelines in the relevant jurisdictions (including any laws regarding the export of data or software to and from the United States or other relevant countries). 4.3 You agree that if you use the SDK to develop applications for general public users, you will protect the privacy and legal rights of those users. If the users provide you with user names, passwords, or other login information or personal information, you must make the users aware that the information will be available to your application, and you must provide legally adequate privacy notice and protection for those users. If your application stores personal or sensitive information provided by users, it must do so securely. If the user provides your application with Google Account information, your application may only use that information to access the user's Google Account when, and for the limited purposes for which, the user has given you permission to do so. 4.4 You agree that you will not engage in any activity with the SDK, including the development or distribution of an application, that interferes with, disrupts, damages, or accesses in an unauthorized manner the servers, networks, or other properties or services of any third party including, but not limited to, Google or any mobile communications carrier. 4.5 You agree that you are solely responsible for (and that Google has no responsibility to you or to any third party for) any data, content, or resources that you create, transmit or display through Android and/or applications for Android, and for the consequences of your actions (including any loss or damage which Google may suffer) by doing so. 4.6 You agree that you are solely responsible for (and that Google has no responsibility to you or to any third party for) any breach of your obligations under the License Agreement, any applicable third party contract or Terms of Service, or any applicable law or regulation, and for the consequences (including any loss or damage which Google or any third party may suffer) of any such breach.

### 5. Your Developer Credentials

5.1 You agree that you are responsible for maintaining the confidentiality of any developer credentials that may be issued to you by Google or which you may choose yourself and that you will be solely responsible for all applications that are developed under your developer credentials.

### 6. Privacy and Information

6.1 In order to continually innovate and improve the SDK, Google may collect certain usage statistics from the software including but not limited to a unique identifier, associated IP address, version number of the software, and information on which tools and/or services in the SDK are being used and how they are being used. Before any of this information is collected, the SDK will notify you and seek your consent. If you withhold consent, the information will not be collected. 6.2 The data collected is examined in the aggregate to improve the SDK and is maintained in accordance with Google's Privacy Policy, which is located at the following URL: https://policies.google.com/privacy 6.3 Anonymized and aggregated sets of the data may be shared with Google partners to improve the SDK.

### 7. Third Party Applications

7.1 If you use the SDK to run applications developed by a third party or that access data, content or resources provided by a third party, you agree that Google is not responsible for those applications, data, content, or resources. You understand that all data, content or resources which you may access through such third party applications are the sole responsibility of the person from which they originated and that Google is not liable for any loss or damage that you may experience as a result of the use or access of any of those third party applications, data, content, or resources. 7.2 You should be aware the data, content, and resources presented to you through such a third party application may be protected by intellectual property rights which are owned by the providers (or by other persons or companies on their behalf). You may not modify, rent, lease, loan, sell, distribute or create derivative works based on these data, content, or resources (either in whole or in part) unless you have been specifically given permission to do so by the relevant owners. 7.3 You acknowledge that your use of such third party applications, data, content, or resources may be subject to separate terms between you and the relevant third party. In that case, the License Agreement does not affect your legal relationship with these third parties.

### 8. Using Android APIs

8.1 Google Data APIs 8.1.1 If you use any API to retrieve data from Google, you acknowledge that the data may be protected by intellectual property rights which are owned by Google or those parties that provide the data (or by other persons or companies on their behalf). Your use of any such API may be subject to additional Terms of Service. You may not modify, rent, lease, loan, sell, distribute or create derivative works based on this data (either in whole or in part) unless allowed by the relevant Terms of Service. 8.1.2 If you use any API to retrieve a user's data from Google, you acknowledge and agree that you shall retrieve data only with the user's explicit consent and only when, and for the limited purposes for which, the user has given you permission to do so. If you use the Android Recognition Service API, documented at the following URL: <https://developer.android.com/reference/android/speech/RecognitionService>, as updated from time to time, you acknowledge that the use of the API is subject to the Data Processing Addendum for Products where Google is a Data Processor, which is located at the following URL: <https://privacy.google.com/businesses/gdprprocessorterms/>, as updated from time to time. By clicking to accept, you hereby agree to the terms of the Data Processing Addendum for Products where Google is a Data Processor.

### 9. Terminating this License Agreement

9.1 The License Agreement will continue to apply until terminated by either you or Google as set out below. 9.2 If you want to terminate the License Agreement, you may do so by ceasing your use of the SDK and any relevant developer credentials. 9.3 Google may at any time, terminate the License Agreement with you if: (A) you have breached any provision of the License Agreement; or (B) Google is required to do so by law; or (C) the partner with whom Google offered certain parts of SDK (such as APIs) to you has terminated its relationship with Google or ceased to offer certain parts of the SDK to you; or (D) Google decides to no longer provide the SDK or certain parts of the SDK to users in the country in which you are resident or from which you use the service, or the provision of the SDK or certain SDK services to you by Google is, in Google's sole discretion, no longer commercially viable. 9.4 When the License Agreement comes to an end, all of the legal rights, obligations and liabilities that you and Google have benefited from, been subject to (or which have accrued over time whilst the License Agreement has been in force) or which are expressed to continue indefinitely, shall be unaffected by this cessation, and the provisions of paragraph 14.7 shall continue to apply to such rights, obligations and liabilities indefinitely.

### 10. DISCLAIMER OF WARRANTIES

10.1 YOU EXPRESSLY UNDERSTAND AND AGREE THAT YOUR USE OF THE SDK IS AT YOUR SOLE RISK AND THAT THE SDK IS PROVIDED "AS IS" AND "AS AVAILABLE" WITHOUT WARRANTY OF ANY KIND FROM GOOGLE. 10.2 YOUR USE OF THE SDK AND ANY MATERIAL DOWNLOADED OR OTHERWISE OBTAINED THROUGH THE USE OF THE SDK IS AT YOUR OWN DISCRETION AND RISK AND YOU ARE SOLELY RESPONSIBLE FOR ANY DAMAGE TO YOUR COMPUTER SYSTEM OR OTHER DEVICE OR LOSS OF DATA THAT RESULTS FROM SUCH USE. 10.3 GOOGLE FURTHER EXPRESSLY DISCLAIMS ALL WARRANTIES AND CONDITIONS OF ANY KIND, WHETHER EXPRESS OR IMPLIED, INCLUDING, BUT NOT LIMITED TO THE IMPLIED WARRANTIES AND CONDITIONS OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT.

### 11. LIMITATION OF LIABILITY

11.1 YOU EXPRESSLY UNDERSTAND AND AGREE THAT GOOGLE, ITS SUBSIDIARIES AND AFFILIATES, AND ITS LICENSORS SHALL NOT BE LIABLE TO YOU UNDER ANY THEORY OF LIABILITY FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, CONSEQUENTIAL OR EXEMPLARY DAMAGES THAT MAY BE INCURRED BY YOU, INCLUDING ANY LOSS OF DATA, WHETHER OR NOT GOOGLE OR ITS REPRESENTATIVES HAVE BEEN ADVISED OF OR SHOULD HAVE BEEN AWARE OF THE POSSIBILITY OF ANY SUCH LOSSES ARISING.

### 12. Indemnification

12.1 To the maximum extent permitted by law, you agree to defend, indemnify and hold harmless Google, its affiliates and their respective directors, officers, employees and agents from and against any and all claims, actions, suits or proceedings, as well as any and all losses, liabilities, damages, costs and expenses (including reasonable attorneys fees) arising out of or accruing from (a) your use of the SDK, (b) any application you develop on the SDK that infringes any copyright, trademark, trade secret, trade dress, patent or other intellectual property right of any person or defames any person or violates their rights of publicity or privacy, and (c) any non-compliance by you with the License Agreement.

### 13. Changes to the License Agreement

13.1 Google may make changes to the License Agreement as it distributes new versions of the SDK. When these changes are made, Google will make a new version of the License Agreement available on the website where the SDK is made available.

### 14. General Legal Terms

14.1 The License Agreement constitutes the whole legal agreement between you and Google and governs your use of the SDK (excluding any services which Google may provide to you under a separate written agreement), and completely replaces any prior agreements between you and Google in relation to the SDK. 14.2 You agree that if Google does not exercise or enforce any legal right or remedy which is contained in the License Agreement (or which Google has the benefit of under any applicable law), this will not be taken to be a formal waiver of Google's rights and that those rights or remedies will still be available to Google. 14.3 If any court of law, having the jurisdiction to decide on this matter, rules that any provision of the License Agreement is invalid, then that provision will be removed from the License Agreement without affecting the rest of the License Agreement. The remaining provisions of the License Agreement will continue to be valid and enforceable. 14.4 You acknowledge and agree that each member of the group of companies of which Google is the parent shall be third party beneficiaries to the License Agreement and that such other companies shall be entitled to directly enforce, and rely upon, any provision of the License Agreement that confers a benefit on (or rights in favor of) them. Other than this, no other person or company shall be third party beneficiaries to the License Agreement. 14.5 EXPORT RESTRICTIONS. THE SDK IS SUBJECT TO UNITED STATES EXPORT LAWS AND REGULATIONS. YOU MUST COMPLY WITH ALL DOMESTIC AND INTERNATIONAL EXPORT LAWS AND REGULATIONS THAT APPLY TO THE SDK. THESE LAWS INCLUDE RESTRICTIONS ON DESTINATIONS, END USERS AND END USE. 14.6 The rights granted in the License Agreement may not be assigned or transferred by either you or Google without the prior written approval of the other party. Neither you nor Google shall be permitted to delegate their responsibilities or obligations under the License Agreement without the prior written approval of the other party. 14.7 The License Agreement, and your relationship with Google under the License Agreement, shall be governed by the laws of the State of California without regard to its conflict of laws provisions. You and Google agree to submit to the exclusive jurisdiction of the courts located within the county of Santa Clara, California to resolve any legal matter arising from the License Agreement. Notwithstanding this, you agree that Google shall still be allowed to apply for injunctive remedies (or an equivalent type of urgent legal relief) in any jurisdiction. *July 27, 2021* I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android SDK Platform-Tools for Linux </button> [Download Android SDK Platform-Tools
for
Linux](https://dl.google.com/android/repository/platform-tools-latest-linux.zip)

*platform-tools-latest-linux.zip*

<br />