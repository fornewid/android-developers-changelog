---
title: https://developer.android.com/about/versions/12/dev-support-images
url: https://developer.android.com/about/versions/12/dev-support-images
source: md.txt
---

For Pixel 6, and Pixel 6 Pro devices, Android 13 included a bootloader
update to address potential security vulnerabilities, and the *anti-rollback
counter* for those devices was incremented, preventing them from being rolled
back to Android 12.

To facilitate app development and testing, we provide modified Android 12 system
images for these Pixel devices called *Developer Support images*. Developer
Support images are system images that are based on stable, public builds of
Android 12 (API level 31) and the 12L feature drop (API level 32) that also
include an updated version of the bootloader with security fixes and an
incremented anti-rollback counter.

A Pixel 6 or 6 Pro device that is running Android 13 can be rolled back to
an Android 12 Developer Support image but can't be rolled back to any other
Android 12 images. A device that is running a Developer Support image can be
flashed to the [latest public build](https://developer.android.com/about/versions/12/dev-support-images#public) but can't be flashed back to any
previous Android 12 images.
| **Warning:** Flashing to a Developer Support build from a public build---or going back to a public build from a Developer Support build---requires a full device reset that removes all user data on the device. Make sure to [back up your data first](https://support.google.com/pixelphone/answer/7179901).

## General advisories

Developer Support builds are intended to provide a system and app experience as
close as possible to the behavior of Android 12 running on a typical user's
device. However, here are few things to keep in mind while using these builds
for development and testing:

- Developer Support builds are for developers only and aren't suitable for general use.
- Devices using developer support builds don't receive OTA security updates like other devices, and Developer Support images aren't rebuilt with the latest security fixes. Only an updated bootloader version is included, with its own security fixes and an incremented anti-rollback counter.
- Developer Support builds aren't [Compatibility Test Suite (CTS)](https://source.android.com/compatibility/cts/)‑approved, but they have passed preliminary testing and provide a stable set of APIs for developers. Apps that depend on CTS-approved builds or use SafetyNet APIs might not work normally on Android 12 Developer Support builds.

## How to provide feedback

Use the [issue tracker](https://issuetracker.google.com/issues/new?component=1234465&template=1725758)
to create new issues and to view, track, and vote for issues that you and other
developers have created.

Before creating your own issue, check the
[list of open issues](https://issuetracker.google.com/issues?q=componentid:1234465+status:open)
to see if someone else has already reported it. You can subscribe and vote for
an issue by **starring it**
![](https://developer.android.com/static/images/shared/star-issue.svg) in
the issue tracker. For more information, see
[Subscribing by starring an issue](https://developers.google.com/issue-tracker/guides/subscribe#subscribing_by_starring_an_issue).
For general help with Google Issue Tracker, see the
[documentation](https://developers.google.com/issue-tracker/).

## Flash your device

You can flash an Android 12 Developer Support build to your device in any of
these ways:

- [Flash your device using the Android Flash tool](https://developer.android.com/about/versions/12/dev-support-images#flashtool)
- [Flash your device manually](https://developer.android.com/about/versions/12/dev-support-images#flash)

### Flash your device using Android Flash Tool

Android Flash Tool lets you securely flash a system image to your supported
Pixel device. Android Flash Tool works with any Web browser that supports
WebUSB, such as Chrome or Edge 79+.

Android Flash Tool guides you step-by-step through the process of flashing your
device---there's no need to have tools installed---but you will need to unlock your
device and
[enable USB Debugging in Developer options](https://developer.android.com/studio/debug/dev-options#enable).

Connect your device over USB, then navigate to Android Flash Tool using one of
the following links and follow the onscreen guidance:

- [Flash an Android 12 (API level 31) Developer Support image](https://flash.android.com/release/12.0.0)
- [Flash a 12L (API level 32) Developer Support image](https://flash.android.com/release/12.1.0)

For complete instructions, see the
[Android Flash Tool documentation](https://source.android.com/setup/contribute/flash).

### Flash your device manually

You can also download a Developer Support image and manually flash it to your
device. See the following table to download the system image for your test
device. Manually flashing a device is useful if you need precise control over
the test environment or if you need to reinstall frequently, such as when
performing automated testing.

After you back up your device data and download the matching system image below,
you can [flash the image onto your device](https://developers.google.com/android/images#instructions).

You can choose to [return to the latest public build](https://developer.android.com/about/versions/12/dev-support-images#public) at any time.

#### Device factory images

### Pixel 6

|---|---|
| **Release date** | August 29, 2022 |
| **Android 12 (API level 31)** | Build: SQ1D.220205.004.X2 Security patch level: Feb 2022 Google Play services: 21.24.23 |
| **12L feature drop (API level 32)** | Build: SQ3A.220705.004.X2 Security patch level: Jul 2022 Google Play services: 22.26.15 |

### Pixel 6 Pro

|---|---|
| **Release date** | August 29, 2022 |
| **Android 12 (API level 31)** | Build: SQ1D.220205.004.X2 Security patch level: Feb 2022 Google Play services: 21.24.23 |
| **12L feature drop (API level 32)** | Build: SQ3A.220705.004.X2 Security patch level: Jul 2022 Google Play services: 22.26.15 |

| Device | Version | Download Link | SHA-256 Checksum |
|---|---|---|---|
| **Pixel 6** | Android 12 (API level 31) | oriole-sq1d.220205.004.x2-factory-1b9d8fc0.zip | `1b9d8fc0de380af1a9041f0267c4e31dd5e98de4c8a4d419f28e2c66e89cb68c` |
| **Pixel 6** | 12L feature drop (API level 32) | oriole-sq3a.220705.004.x2-factory-c5a02422.zip | `c5a024229cf49055559c5d2c4088754f36402222a050be30844ff5d821ed06c3` |
| **Pixel 6 Pro** | Android 12 (API level 31) | raven-sq1d.220205.004.x2-factory-ca630efc.zip | `ca630efcbbf56f41300e21e70054f66820bdfdc61aa64cf89d4fac2a9e7623b8` |
| **Pixel 6 Pro** | 12L feature drop (API level 32) | raven-sq3a.220705.004.x2-factory-56c65af2.zip | `56c65af280d45e21b53c12ef27d2d5a1155d2169c55f4d0586eb125560346219` |

## Return to a public build

You can use the Android Flash Tool to
[flash the factory image](https://flash.android.com/back-to-public) or obtain a
factory spec system image from the
[Factory Images for Nexus and Pixel Devices](https://developers.google.com/android/images)
page and then manually flash it to the device.
**Warning:** Going back to a public build from a Developer Support build requires a full device reset that removes all user data on the device. Make sure to [back up your data first](https://support.google.com/pixelphone/answer/7179901).  

## Download Android 12 Developer Support system image

Before downloading, you must agree to the following terms and conditions.  

## Terms and Conditions

Developer Support version warning: You are about to download, install, and use a Developer Support version of Android on your Pixel device. Developer Support versions may not be stable, and may contain errors and defects that can result in serious damage to computer systems, devices, applications and data. Data or metrics may be collected from the devices in the Developer Support build at the sole discretion of Google. Google makes no warranties, express or implied, with respect to the Developer Support versions. Your use is at your own risk, and not Google's. Certain functionality (including core functionality, such as your ability to place and receive calls) or applications may not work properly. You are solely responsible for any error, defect, damage or destruction due to such use, including damage to any device or loss of data. The Developer Support version of Android contains a bootloader update with the latest anti-rollback version. After installing the Developer Support version, you will no longer be able to revert to a public release Android version with a lower bootloader anti-rollback version. Switching between Developer Support and public release Android versions on your device may require you to wipe all data from your device.  
I have read and agree with the above terms and conditions  
Download Android 12 Developer Support system image [Download Android 12 Developer Support system image](https://dl.google.com/developers/android/sc/images/factory/oriole-sq1d.220205.004.x2-factory-1b9d8fc0.zip)

*oriole-sq1d.220205.004.x2-factory-1b9d8fc0.zip*  

## Download Android 12 Developer Support system image

Before downloading, you must agree to the following terms and conditions.  

## Terms and Conditions

Developer Support version warning: You are about to download, install, and use a Developer Support version of Android on your Pixel device. Developer Support versions may not be stable, and may contain errors and defects that can result in serious damage to computer systems, devices, applications and data. Data or metrics may be collected from the devices in the Developer Support build at the sole discretion of Google. Google makes no warranties, express or implied, with respect to the Developer Support versions. Your use is at your own risk, and not Google's. Certain functionality (including core functionality, such as your ability to place and receive calls) or applications may not work properly. You are solely responsible for any error, defect, damage or destruction due to such use, including damage to any device or loss of data. The Developer Support version of Android contains a bootloader update with the latest anti-rollback version. After installing the Developer Support version, you will no longer be able to revert to a public release Android version with a lower bootloader anti-rollback version. Switching between Developer Support and public release Android versions on your device may require you to wipe all data from your device.  
I have read and agree with the above terms and conditions  
Download Android 12 Developer Support system image [Download Android 12 Developer Support system image](https://dl.google.com/developers/android/sc/images/factory/raven-sq1d.220205.004.x2-factory-ca630efc.zip)

*raven-sq1d.220205.004.x2-factory-ca630efc.zip*  

## Download Android 12 Developer Support system image

Before downloading, you must agree to the following terms and conditions.  

## Terms and Conditions

Developer Support version warning: You are about to download, install, and use a Developer Support version of Android on your Pixel device. Developer Support versions may not be stable, and may contain errors and defects that can result in serious damage to computer systems, devices, applications and data. Data or metrics may be collected from the devices in the Developer Support build at the sole discretion of Google. Google makes no warranties, express or implied, with respect to the Developer Support versions. Your use is at your own risk, and not Google's. Certain functionality (including core functionality, such as your ability to place and receive calls) or applications may not work properly. You are solely responsible for any error, defect, damage or destruction due to such use, including damage to any device or loss of data. The Developer Support version of Android contains a bootloader update with the latest anti-rollback version. After installing the Developer Support version, you will no longer be able to revert to a public release Android version with a lower bootloader anti-rollback version. Switching between Developer Support and public release Android versions on your device may require you to wipe all data from your device.  
I have read and agree with the above terms and conditions  
Download Android 12 Developer Support system image [Download Android 12 Developer Support system image](https://dl.google.com/developers/android/sc/images/factory/oriole-sq3a.220705.004.x2-factory-c5a02422.zip)

*oriole-sq3a.220705.004.x2-factory-c5a02422.zip*  

## Download Android 12 Developer Support system image

Before downloading, you must agree to the following terms and conditions.  

## Terms and Conditions

Developer Support version warning: You are about to download, install, and use a Developer Support version of Android on your Pixel device. Developer Support versions may not be stable, and may contain errors and defects that can result in serious damage to computer systems, devices, applications and data. Data or metrics may be collected from the devices in the Developer Support build at the sole discretion of Google. Google makes no warranties, express or implied, with respect to the Developer Support versions. Your use is at your own risk, and not Google's. Certain functionality (including core functionality, such as your ability to place and receive calls) or applications may not work properly. You are solely responsible for any error, defect, damage or destruction due to such use, including damage to any device or loss of data. The Developer Support version of Android contains a bootloader update with the latest anti-rollback version. After installing the Developer Support version, you will no longer be able to revert to a public release Android version with a lower bootloader anti-rollback version. Switching between Developer Support and public release Android versions on your device may require you to wipe all data from your device.  
I have read and agree with the above terms and conditions  
Download Android 12 Developer Support system image [Download Android 12 Developer Support system image](https://dl.google.com/developers/android/sc/images/factory/raven-sq3a.220705.004.x2-factory-56c65af2.zip)

*raven-sq3a.220705.004.x2-factory-56c65af2.zip*