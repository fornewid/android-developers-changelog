---
title: https://developer.android.com/topic/generic-system-image
url: https://developer.android.com/topic/generic-system-image
source: md.txt
---

[Video](https://www.youtube.com/watch?v=TExHLclCQG4)

A Generic System Image ([GSI](https://source.android.com/setup/build/gsi)) is a
*pure Android* implementation with unmodified Android Open Source Project (AOSP)
code, runnable on a variety of Android devices.

App developers can install and run the latest Android GSIs to perform app
testing on a variety of existing Android devices and using GSIs from different
Android OS release stages, including Developer Preview and Beta builds. Adding
GSIs to your verification and testing processes can provide you with some extra
benefits:

- Broader test coverage on a greater set of real devices
- More time to fix app compatibility issues
- More opportunities to fix compatibility issues in Android that are reported by app developers

The GSI project is [open
source](https://android.googlesource.com/platform/manifest/+/refs/heads/pie-gsi#)
and helps improve the Android ecosystem by providing more ways to improve app
and OS quality before each release of Android.
![GSI support across devices](https://developer.android.com/static/topic/generic-system-image/images/gsi-support.png) **Figure 1**: GSIs can be installed across a broad range of devices, and sometimes even for versions of Android that a device manufacturer doesn't provide their own system image for.

GSIs include the same core system functionalities for all devices that they're
installed on. In other words, a GSI does not include device manufacturer's
customizations. Because of this, you might encounter behavioral differences in
the following situations:

- Interactions that involve the UI
- Workflows that request newer hardware features

## Check device compliance

GSIs can only function on devices with the following characteristics:

- Bootloader is unlocked.
- Fully Treble-compliant.
- Launched with Android 9 (API level 28) or higher. Devices upgraded to Android 9 from an earlier version might or might not support GSIs.

> [!WARNING]
> **Warning:** Attempting to flash a GSI to a non-compliant device could result in your device becoming non-bootable. Always confirm that your device is compliant before flashing, and follow the installation steps provided by your device's manufacturer. GSIs don't support rollback, so you will need a recovery method and original system ROM to revert to the original system.

To determine whether your device can use a GSI and which GSI OS version you
should install, do the following:

1. Check for Treble support by running the following command:

   ```
   adb shell getprop ro.treble.enabled
   ```

   If the response is `false`, the device isn't compatible with GSIs and you
   shouldn't continue. If the response is `true`, continue to the next step.
2. Check for cross-version support by running the following command:

   ```
   adb shell cat /system/etc/ld.config.version_identifier.txt \
   | grep -A 20 "\[vendor\]"
   ```

   > [!NOTE]
   > **Note:** Depending on your platform, the configuration file in the preceding command may or may not have a version identifier in it.

   In the output, look in the `[vendor]` section for
   `namespace.default.isolated`.

   If the value for that attribute is `true`, then the device fully supports
   [Vendor Native Development Kit
   (VNDK)](https://source.android.com/devices/architecture/vndk) and can use
   any GSI operating system (OS) version that is newer than the on-device OS
   version. Whenever possible, use the latest GSI OS version that is available.

   If the value for the attribute is `false`, then the device isn't fully
   VNDK-compliant, and the device can use only a GSI for the same on-device OS
   version. For example, an Android 10 (API version 29) device that isn't
   VNDK-compliant can load only an Android 10 GSI image.
3. The GSI CPU architecture type must match the device's CPU architecture. To
   find the right CPU architecture for the GSI image, run the following
   command:

   ```
   adb shell getprop ro.product.cpu.abi
   ```

   Use the output to determine which GSI image to use when flashing your
   device. For example, on a Pixel 5, the output would indicate that the CPU
   architecture is `arm64-v8a`, so you would use the `arm64` type of GSI.

## Download GSIs

There are a few ways to get GSIs, depending on your development needs:

- For Android Preview GSIs and Android GSIs with GMS, download the images from the [GSI release page](https://developer.android.com/topic/generic-system-image/releases).
- For pre-built GSI images without GMS applications, download the images from
  the AOSP CI site:

  - [Android 10 (API level
    29)](https://ci.android.com/builds/branches/aosp-android10-gsi/grid)
  - [Android 11 (API level
    30)](https://ci.android.com/builds/branches/aosp-android11-gsi/grid)
  - [Android 12 (API level
    31)](https://ci.android.com/builds/branches/aosp-android12-gsi/grid)
  - [Android 13 (API level
    33)](https://ci.android.com/builds/branches/aosp-android13-gsi/grid)
- To build Android GSIs without GMS, download source code from
  [AOSP](https://source.android.com/setup/build/gsi#building-gsis) and build
  your GSIs.

> [!IMPORTANT]
> **Important:** Device manufacturers shouldn't use these versions of GSIs to run and submit compliance tests. Instead, device manufacturers should continue to refer to their existing communication channels, such as their Technical Account Managers for compliance-test-related activities.

## Install a GSI

> [!NOTE]
> **Note:** If your device has adopted [Android Verified
> Boot](https://source.android.com/security/verifiedboot/avb) (AVB), download and flash the following image to disable AVB before flashing a GSI: [vbmeta.img](https://dl.google.com/developers/android/qt/images/gsi/vbmeta.img)

Installing a GSI is device-dependent. Refer to your device's manufacturer for
the exact tools and procedures. For Google Pixel devices such as the Pixel 3 and
newer, there are several ways to install:

- Manually flashing GSI images: see [Requirements for flashing GSIs](https://source.android.com/setup/build/gsi#flashing-gsis)
- Using Dynamic System Update (DSU) for devices that already run Android 10 or higher: see the [Dynamic System Updates](https://developer.android.com/topic/dsu) page

## Give feedback

GSIs are intended to help you validate your apps on Android. We appreciate your
feedback on the images, the tools, and the process for using GSIs on your
devices.

To notify us of bugs or feature requests, use the [dedicated issue tracker
component](https://issuetracker.google.com/issues/new?component=470386&template=1147338)
for GSIs.

## Additional resources

- [Understand the impact of Generic System Images (GSI) (Android Dev Summit
  '18)](https://www.youtube.com/watch?v=Y-HmCIHD63w)