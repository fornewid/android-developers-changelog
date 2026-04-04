---
title: Factory images for Google Pixel  |  Android Developers
url: https://developer.android.com/about/versions/17/download
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Releases](https://developer.android.com/about/versions)

# Factory images for Google Pixel Stay organized with collections Save and categorize content based on your preferences.




If you are a developer with a supported Google Pixel device, you can manually
update that device to the latest build for testing and development. Flashing a
factory image requires a full device reset, so make sure to [back up your
data](https://support.google.com/pixelphone/answer/7179901) first. Builds are available for the following Pixel devices:

* Pixel 6
* Pixel 6 Pro
* Pixel 6a
* Pixel 7
* Pixel 7 Pro
* Pixel 7a
* Pixel Tablet
* Pixel Fold
* Pixel 8
* Pixel 8 Pro
* Pixel 8a
* Pixel 9
* Pixel 9 Pro
* Pixel 9 Pro XL
* Pixel 9 Pro Fold
* Pixel 9a
* Pixel 10
* Pixel 10 Pro
* Pixel 10 Pro XL
* Pixel 10 Pro Fold

After you've flashed a beta build to your Pixel device, your device is
automatically enrolled in the [Android Beta for Pixel program](https://g.co/androidBeta) and offered
continuous over-the-air (OTA) updates to the latest beta builds (including QPRs)
until you choose to unenroll that device from the program. We also
deliver flashable images at each milestone, so you can choose the approach that
works best for your test environment.

Use the following links and instructions to update your supported device to the
latest build. See [Get Android 17](/about/versions/17/get) for
other ways to get Android 17 for testing and development.

**Warning:** Flashing to a beta build from a
production build—or going back to a production build from a
beta build—requires a full device reset that
removes all user data on the device. Make sure to [back up the data from your
Pixel](https://support.google.com/pixelphone/answer/7179901) first.

## Flash your device using Android Flash Tool

**Android Flash Tool** lets you securely flash a system image
to your supported Pixel device. Android Flash Tool works with any Web browser
that supports WebUSB, such as Chrome or Edge 79+.

Android Flash Tool guides you step-by-step through the process of flashing your
device—there's no need to have tools installed—but you do need to unlock your
device and [enable USB Debugging in Developer options](/studio/debug/dev-options#enable). For
complete instructions, see the [Android Flash Tool
documentation](https://source.android.com/setup/contribute/flash).

Connect your device over USB, then navigate to Android Flash Tool using the
following link and follow the onscreen guidance:
<https://flash.android.com/preview/cinnamonbun-beta3>.

## Flash your device manually

![](/static/images/lockups/android-stacked.svg)

You can also download the latest system image and manually flash it to your
device. See the following table to download the system image for your test
device. Manually flashing a device is useful if you need precise control over
the test environment or if you need to reinstall frequently, such as when
performing automated testing.

After you back up your device data and download the matching system image, you
can [flash the image onto your device](https://developers.google.com/android/images#instructions).

You can choose to [return to the latest public build](#public) at any
time.

### Device factory images

|  |  |
| --- | --- |
| **Release date** | March 26, 2026 |
| **Builds** | CP21.260306.017 |
| **Emulator support** | x86 (64-bit), ARM (v8-A) |
| **Security patch level** | 2026-03-05 |
| **Google Play services** | 26.02.35 |

| Device | Download Link and SHA-256 Checksum |
| --- | --- |
| Pixel 6 | oriole\_beta-cp21.260306.017-factory-8cc4c614.zip  `8cc4c61499a8bb4b4da6231e28790379a1031f898534c8aac4bcb7417348d593` |
| Pixel 6 Pro | raven\_beta-cp21.260306.017-factory-534a9690.zip  `534a9690150ad07d374f06d70618e7768418f0135a90de8eff67b4830efaf812` |
| Pixel 6a | bluejay\_beta-cp21.260306.017-factory-5c81c904.zip  `5c81c90431443a13874225a9ee704cacacdb5e1bde3d9dfa8a0f8cef06600cfa` |
| Pixel 7 | panther\_beta-cp21.260306.017-factory-7920a79e.zip  `7920a79eb2ca6441deb3f9e904cc9c5f5b123e268155ea56db0ca8747c296783` |
| Pixel 7 Pro | cheetah\_beta-cp21.260306.017-factory-02c7f7d6.zip  `02c7f7d652674a88c09bbbaea4170d28e381b0a6ca5aad3ce76436016172893e` |
| Pixel 7a | lynx\_beta-cp21.260306.017-factory-a6b0179f.zip  `a6b0179ff8ca974fee2d917dc140bcd8851d2f8e4232f2e84b01ab61313d7c94` |
| Pixel Fold | felix\_beta-cp21.260306.017-factory-6c834eda.zip  `6c834eda9d53d92290f011063ece42171ae22207460704b8209645b55faf45cd` |
| Pixel Tablet | tangorpro\_beta-cp21.260306.017-factory-08beb16a.zip  `08beb16ab304eac515939ab99b439474163d27c4c8a25546850ae58ead20b276` |
| Pixel 8 | shiba\_beta-cp21.260306.017-factory-ce24f9b3.zip  `ce24f9b3760562fe8e71c3d48cb8d22299e7ed58fe0541684d4af8ffe6927ba1` |
| Pixel 8 Pro | husky\_beta-cp21.260306.017-factory-41be1dba.zip  `41be1dbaad2d685cc8f55bdc8415149c53c07c674fbe403956e74fdb4370610f` |
| Pixel 8a | akita\_beta-cp21.260306.017-factory-002d1038.zip  `002d10382a3fd39f97da1804bdc8b8fce585a8704169fa5c7cf5167b608fb9a1` |
| Pixel 9 | tokay\_beta-cp21.260306.017-factory-72bc1249.zip  `72bc12492eeb5fad1e8823ef607ba06fb8a3f7e3db1585a38b41f65ac020641b` |
| Pixel 9 Pro | caiman\_beta-cp21.260306.017-factory-329731c5.zip  `329731c51ab4e4ad3c03db8606e108b75117dc9408004aee844ec70764a823b7` |
| Pixel 9 Pro XL | komodo\_beta-cp21.260306.017-factory-77babdbe.zip  `77babdbe1806742197f9829c01063f436c54f80f4b3fb1ffe6d3b9f7e43a6b55` |
| Pixel 9 Pro Fold | comet\_beta-cp21.260306.017-factory-186d9aef.zip  `186d9aefd8c977c8942d9ca03a20d0e7217321b36a8b99f2cc752b3f9216dd55` |
| Pixel 9a | tegu\_beta-cp21.260306.017-factory-c0263c49.zip  `c0263c4998f58ec251cc915a1cf4833f3cfb602ea449866f9b08967a6241a06e` |
| Pixel 10 | frankel\_beta-cp21.260306.017-factory-a7f51471.zip  `a7f5147198ebe05daddbc4cffefc6ed4f4a013f6f220e15f36687f5f7c62b656` |
| Pixel 10 Pro | blazer\_beta-cp21.260306.017-factory-b50f051f.zip  `b50f051fd2cf5a7fd80ac19a5a4f71cf4d2aa5fa7b531a7a4e87903c8b29efaf` |
| Pixel 10 Pro XL | mustang\_beta-cp21.260306.017-factory-2163e750.zip  `2163e750d627d034bb2eaff6171cb9da964155f3c8a86c6121988348cd5ecab0` |
| Pixel 10 Pro Fold | rango\_beta-cp21.260306.017-factory-61fbd76d.zip  `61fbd76db374d38b59d140da3219b0f91c1aa8d9bc287a87856748b799a0cd57` |

## Return to a public build

You can either use the Android Flash Tool to
[flash the factory image](https://flash.android.com/back-to-public), or obtain a factory spec system
image from the [Factory Images for Nexus and Pixel Devices](https://developers.google.com/android/images)
page and then manually flash it to the device.

**Warning:** Going back to a public build from a preview build (Developer Preview
or Beta) requires a full device reset that removes all user data on the device.
Make sure to [back up your data first](https://support.google.com/pixelphone/answer/7179901).

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software
Development Kit License Agreement (available at
https://developer.android.com/studio/terms and such URL may be updated or
changed by Google from time to time), which will terminate when Google issues a
final release version.  
  
Your testing and feedback are important part of the development process and by
using the SDK, you acknowledge that (i) implementation of some features are
still under development, (ii) you should not rely on the SDK having the full
functionality of a stable release; (iii) you agree not to publicly distribute or
ship any application using this SDK as this SDK will no longer be supported
after the official Android SDK is released; and (iv) you agree that Google may
deliver elements of the SDK to your devices via auto-update (OTA or otherwise,
in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE
AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE
RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN
RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE
OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.

I have read and agree with the above terms and conditions

Download Android 17 factory system image
[Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/oriole_beta-cp21.260306.017-factory-8cc4c614.zip)

*oriole\_beta-cp21.260306.017-factory-8cc4c614.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software
Development Kit License Agreement (available at
https://developer.android.com/studio/terms and such URL may be updated or
changed by Google from time to time), which will terminate when Google issues a
final release version.  
  
Your testing and feedback are important part of the development process and by
using the SDK, you acknowledge that (i) implementation of some features are
still under development, (ii) you should not rely on the SDK having the full
functionality of a stable release; (iii) you agree not to publicly distribute or
ship any application using this SDK as this SDK will no longer be supported
after the official Android SDK is released; and (iv) you agree that Google may
deliver elements of the SDK to your devices via auto-update (OTA or otherwise,
in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE
AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE
RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN
RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE
OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.

I have read and agree with the above terms and conditions

Download Android 17 factory system image
[Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/raven_beta-cp21.260306.017-factory-534a9690.zip)

*raven\_beta-cp21.260306.017-factory-534a9690.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software
Development Kit License Agreement (available at
https://developer.android.com/studio/terms and such URL may be updated or
changed by Google from time to time), which will terminate when Google issues a
final release version.  
  
Your testing and feedback are important part of the development process and by
using the SDK, you acknowledge that (i) implementation of some features are
still under development, (ii) you should not rely on the SDK having the full
functionality of a stable release; (iii) you agree not to publicly distribute or
ship any application using this SDK as this SDK will no longer be supported
after the official Android SDK is released; and (iv) you agree that Google may
deliver elements of the SDK to your devices via auto-update (OTA or otherwise,
in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE
AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE
RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN
RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE
OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.

I have read and agree with the above terms and conditions

Download Android 17 factory system image
[Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/bluejay_beta-cp21.260306.017-factory-5c81c904.zip)

*bluejay\_beta-cp21.260306.017-factory-5c81c904.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software
Development Kit License Agreement (available at
https://developer.android.com/studio/terms and such URL may be updated or
changed by Google from time to time), which will terminate when Google issues a
final release version.  
  
Your testing and feedback are important part of the development process and by
using the SDK, you acknowledge that (i) implementation of some features are
still under development, (ii) you should not rely on the SDK having the full
functionality of a stable release; (iii) you agree not to publicly distribute or
ship any application using this SDK as this SDK will no longer be supported
after the official Android SDK is released; and (iv) you agree that Google may
deliver elements of the SDK to your devices via auto-update (OTA or otherwise,
in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE
AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE
RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN
RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE
OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.

I have read and agree with the above terms and conditions

Download Android 17 factory system image
[Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/panther_beta-cp21.260306.017-factory-7920a79e.zip)

*panther\_beta-cp21.260306.017-factory-7920a79e.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software
Development Kit License Agreement (available at
https://developer.android.com/studio/terms and such URL may be updated or
changed by Google from time to time), which will terminate when Google issues a
final release version.  
  
Your testing and feedback are important part of the development process and by
using the SDK, you acknowledge that (i) implementation of some features are
still under development, (ii) you should not rely on the SDK having the full
functionality of a stable release; (iii) you agree not to publicly distribute or
ship any application using this SDK as this SDK will no longer be supported
after the official Android SDK is released; and (iv) you agree that Google may
deliver elements of the SDK to your devices via auto-update (OTA or otherwise,
in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE
AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE
RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN
RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE
OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.

I have read and agree with the above terms and conditions

Download Android 17 factory system image
[Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/cheetah_beta-cp21.260306.017-factory-02c7f7d6.zip)

*cheetah\_beta-cp21.260306.017-factory-02c7f7d6.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software
Development Kit License Agreement (available at
https://developer.android.com/studio/terms and such URL may be updated or
changed by Google from time to time), which will terminate when Google issues a
final release version.  
  
Your testing and feedback are important part of the development process and by
using the SDK, you acknowledge that (i) implementation of some features are
still under development, (ii) you should not rely on the SDK having the full
functionality of a stable release; (iii) you agree not to publicly distribute or
ship any application using this SDK as this SDK will no longer be supported
after the official Android SDK is released; and (iv) you agree that Google may
deliver elements of the SDK to your devices via auto-update (OTA or otherwise,
in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE
AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE
RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN
RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE
OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.

I have read and agree with the above terms and conditions

Download Android 17 factory system image
[Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/lynx_beta-cp21.260306.017-factory-a6b0179f.zip)

*lynx\_beta-cp21.260306.017-factory-a6b0179f.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software
Development Kit License Agreement (available at
https://developer.android.com/studio/terms and such URL may be updated or
changed by Google from time to time), which will terminate when Google issues a
final release version.  
  
Your testing and feedback are important part of the development process and by
using the SDK, you acknowledge that (i) implementation of some features are
still under development, (ii) you should not rely on the SDK having the full
functionality of a stable release; (iii) you agree not to publicly distribute or
ship any application using this SDK as this SDK will no longer be supported
after the official Android SDK is released; and (iv) you agree that Google may
deliver elements of the SDK to your devices via auto-update (OTA or otherwise,
in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE
AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE
RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN
RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE
OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.

I have read and agree with the above terms and conditions

Download Android 17 factory system image
[Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/felix_beta-cp21.260306.017-factory-6c834eda.zip)

*felix\_beta-cp21.260306.017-factory-6c834eda.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software
Development Kit License Agreement (available at
https://developer.android.com/studio/terms and such URL may be updated or
changed by Google from time to time), which will terminate when Google issues a
final release version.  
  
Your testing and feedback are important part of the development process and by
using the SDK, you acknowledge that (i) implementation of some features are
still under development, (ii) you should not rely on the SDK having the full
functionality of a stable release; (iii) you agree not to publicly distribute or
ship any application using this SDK as this SDK will no longer be supported
after the official Android SDK is released; and (iv) you agree that Google may
deliver elements of the SDK to your devices via auto-update (OTA or otherwise,
in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE
AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE
RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN
RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE
OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.

I have read and agree with the above terms and conditions

Download Android 17 factory system image
[Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/tangorpro_beta-cp21.260306.017-factory-08beb16a.zip)

*tangorpro\_beta-cp21.260306.017-factory-08beb16a.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software
Development Kit License Agreement (available at
https://developer.android.com/studio/terms and such URL may be updated or
changed by Google from time to time), which will terminate when Google issues a
final release version.  
  
Your testing and feedback are important part of the development process and by
using the SDK, you acknowledge that (i) implementation of some features are
still under development, (ii) you should not rely on the SDK having the full
functionality of a stable release; (iii) you agree not to publicly distribute or
ship any application using this SDK as this SDK will no longer be supported
after the official Android SDK is released; and (iv) you agree that Google may
deliver elements of the SDK to your devices via auto-update (OTA or otherwise,
in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE
AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE
RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN
RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE
OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.

I have read and agree with the above terms and conditions

Download Android 17 factory system image
[Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/shiba_beta-cp21.260306.017-factory-ce24f9b3.zip)

*shiba\_beta-cp21.260306.017-factory-ce24f9b3.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software
Development Kit License Agreement (available at
https://developer.android.com/studio/terms and such URL may be updated or
changed by Google from time to time), which will terminate when Google issues a
final release version.  
  
Your testing and feedback are important part of the development process and by
using the SDK, you acknowledge that (i) implementation of some features are
still under development, (ii) you should not rely on the SDK having the full
functionality of a stable release; (iii) you agree not to publicly distribute or
ship any application using this SDK as this SDK will no longer be supported
after the official Android SDK is released; and (iv) you agree that Google may
deliver elements of the SDK to your devices via auto-update (OTA or otherwise,
in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE
AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE
RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN
RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE
OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.

I have read and agree with the above terms and conditions

Download Android 17 factory system image
[Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/husky_beta-cp21.260306.017-factory-41be1dba.zip)

*husky\_beta-cp21.260306.017-factory-41be1dba.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software
Development Kit License Agreement (available at
https://developer.android.com/studio/terms and such URL may be updated or
changed by Google from time to time), which will terminate when Google issues a
final release version.  
  
Your testing and feedback are important part of the development process and by
using the SDK, you acknowledge that (i) implementation of some features are
still under development, (ii) you should not rely on the SDK having the full
functionality of a stable release; (iii) you agree not to publicly distribute or
ship any application using this SDK as this SDK will no longer be supported
after the official Android SDK is released; and (iv) you agree that Google may
deliver elements of the SDK to your devices via auto-update (OTA or otherwise,
in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE
AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE
RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN
RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE
OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.

I have read and agree with the above terms and conditions

Download Android 17 factory system image
[Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/akita_beta-cp21.260306.017-factory-002d1038.zip)

*akita\_beta-cp21.260306.017-factory-002d1038.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software
Development Kit License Agreement (available at
https://developer.android.com/studio/terms and such URL may be updated or
changed by Google from time to time), which will terminate when Google issues a
final release version.  
  
Your testing and feedback are important part of the development process and by
using the SDK, you acknowledge that (i) implementation of some features are
still under development, (ii) you should not rely on the SDK having the full
functionality of a stable release; (iii) you agree not to publicly distribute or
ship any application using this SDK as this SDK will no longer be supported
after the official Android SDK is released; and (iv) you agree that Google may
deliver elements of the SDK to your devices via auto-update (OTA or otherwise,
in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE
AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE
RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN
RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE
OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.

I have read and agree with the above terms and conditions

Download Android 17 factory system image
[Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/tokay_beta-cp21.260306.017-factory-72bc1249.zip)

*tokay\_beta-cp21.260306.017-factory-72bc1249.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software
Development Kit License Agreement (available at
https://developer.android.com/studio/terms and such URL may be updated or
changed by Google from time to time), which will terminate when Google issues a
final release version.  
  
Your testing and feedback are important part of the development process and by
using the SDK, you acknowledge that (i) implementation of some features are
still under development, (ii) you should not rely on the SDK having the full
functionality of a stable release; (iii) you agree not to publicly distribute or
ship any application using this SDK as this SDK will no longer be supported
after the official Android SDK is released; and (iv) you agree that Google may
deliver elements of the SDK to your devices via auto-update (OTA or otherwise,
in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE
AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE
RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN
RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE
OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.

I have read and agree with the above terms and conditions

Download Android 17 factory system image
[Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/caiman_beta-cp21.260306.017-factory-329731c5.zip)

*caiman\_beta-cp21.260306.017-factory-329731c5.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software
Development Kit License Agreement (available at
https://developer.android.com/studio/terms and such URL may be updated or
changed by Google from time to time), which will terminate when Google issues a
final release version.  
  
Your testing and feedback are important part of the development process and by
using the SDK, you acknowledge that (i) implementation of some features are
still under development, (ii) you should not rely on the SDK having the full
functionality of a stable release; (iii) you agree not to publicly distribute or
ship any application using this SDK as this SDK will no longer be supported
after the official Android SDK is released; and (iv) you agree that Google may
deliver elements of the SDK to your devices via auto-update (OTA or otherwise,
in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE
AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE
RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN
RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE
OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.

I have read and agree with the above terms and conditions

Download Android 17 factory system image
[Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/komodo_beta-cp21.260306.017-factory-77babdbe.zip)

*komodo\_beta-cp21.260306.017-factory-77babdbe.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software
Development Kit License Agreement (available at
https://developer.android.com/studio/terms and such URL may be updated or
changed by Google from time to time), which will terminate when Google issues a
final release version.  
  
Your testing and feedback are important part of the development process and by
using the SDK, you acknowledge that (i) implementation of some features are
still under development, (ii) you should not rely on the SDK having the full
functionality of a stable release; (iii) you agree not to publicly distribute or
ship any application using this SDK as this SDK will no longer be supported
after the official Android SDK is released; and (iv) you agree that Google may
deliver elements of the SDK to your devices via auto-update (OTA or otherwise,
in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE
AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE
RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN
RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE
OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.

I have read and agree with the above terms and conditions

Download Android 17 factory system image
[Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/comet_beta-cp21.260306.017-factory-186d9aef.zip)

*comet\_beta-cp21.260306.017-factory-186d9aef.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software
Development Kit License Agreement (available at
https://developer.android.com/studio/terms and such URL may be updated or
changed by Google from time to time), which will terminate when Google issues a
final release version.  
  
Your testing and feedback are important part of the development process and by
using the SDK, you acknowledge that (i) implementation of some features are
still under development, (ii) you should not rely on the SDK having the full
functionality of a stable release; (iii) you agree not to publicly distribute or
ship any application using this SDK as this SDK will no longer be supported
after the official Android SDK is released; and (iv) you agree that Google may
deliver elements of the SDK to your devices via auto-update (OTA or otherwise,
in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE
AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE
RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN
RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE
OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.

I have read and agree with the above terms and conditions

Download Android 17 factory system image
[Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/tegu_beta-cp21.260306.017-factory-c0263c49.zip)

*tegu\_beta-cp21.260306.017-factory-c0263c49.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software
Development Kit License Agreement (available at
https://developer.android.com/studio/terms and such URL may be updated or
changed by Google from time to time), which will terminate when Google issues a
final release version.  
  
Your testing and feedback are important part of the development process and by
using the SDK, you acknowledge that (i) implementation of some features are
still under development, (ii) you should not rely on the SDK having the full
functionality of a stable release; (iii) you agree not to publicly distribute or
ship any application using this SDK as this SDK will no longer be supported
after the official Android SDK is released; and (iv) you agree that Google may
deliver elements of the SDK to your devices via auto-update (OTA or otherwise,
in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE
AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE
RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN
RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE
OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.

I have read and agree with the above terms and conditions

Download Android 17 factory system image
[Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/frankel_beta-cp21.260306.017-factory-a7f51471.zip)

*frankel\_beta-cp21.260306.017-factory-a7f51471.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software
Development Kit License Agreement (available at
https://developer.android.com/studio/terms and such URL may be updated or
changed by Google from time to time), which will terminate when Google issues a
final release version.  
  
Your testing and feedback are important part of the development process and by
using the SDK, you acknowledge that (i) implementation of some features are
still under development, (ii) you should not rely on the SDK having the full
functionality of a stable release; (iii) you agree not to publicly distribute or
ship any application using this SDK as this SDK will no longer be supported
after the official Android SDK is released; and (iv) you agree that Google may
deliver elements of the SDK to your devices via auto-update (OTA or otherwise,
in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE
AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE
RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN
RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE
OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.

I have read and agree with the above terms and conditions

Download Android 17 factory system image
[Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/blazer_beta-cp21.260306.017-factory-b50f051f.zip)

*blazer\_beta-cp21.260306.017-factory-b50f051f.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software
Development Kit License Agreement (available at
https://developer.android.com/studio/terms and such URL may be updated or
changed by Google from time to time), which will terminate when Google issues a
final release version.  
  
Your testing and feedback are important part of the development process and by
using the SDK, you acknowledge that (i) implementation of some features are
still under development, (ii) you should not rely on the SDK having the full
functionality of a stable release; (iii) you agree not to publicly distribute or
ship any application using this SDK as this SDK will no longer be supported
after the official Android SDK is released; and (iv) you agree that Google may
deliver elements of the SDK to your devices via auto-update (OTA or otherwise,
in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE
AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE
RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN
RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE
OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.

I have read and agree with the above terms and conditions

Download Android 17 factory system image
[Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/mustang_beta-cp21.260306.017-factory-2163e750.zip)

*mustang\_beta-cp21.260306.017-factory-2163e750.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software
Development Kit License Agreement (available at
https://developer.android.com/studio/terms and such URL may be updated or
changed by Google from time to time), which will terminate when Google issues a
final release version.  
  
Your testing and feedback are important part of the development process and by
using the SDK, you acknowledge that (i) implementation of some features are
still under development, (ii) you should not rely on the SDK having the full
functionality of a stable release; (iii) you agree not to publicly distribute or
ship any application using this SDK as this SDK will no longer be supported
after the official Android SDK is released; and (iv) you agree that Google may
deliver elements of the SDK to your devices via auto-update (OTA or otherwise,
in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE
AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE
RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN
RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE
OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.

I have read and agree with the above terms and conditions

Download Android 17 factory system image
[Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/rango_beta-cp21.260306.017-factory-61fbd76d.zip)

*rango\_beta-cp21.260306.017-factory-61fbd76d.zip*