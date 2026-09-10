---
title: Factory images for Google Pixel  |  Android Developers
url: https://developer.android.com/about/versions/17/qpr2/download
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
* Pixel 10a
* Pixel 11
* Pixel 11 Pro
* Pixel 11 Pro XL
* Pixel 11 Pro Fold

After you've flashed a beta build to your Pixel device, your device is
automatically enrolled in the [Android Beta for Pixel program](https://g.co/androidBeta) and offered
continuous over-the-air (OTA) updates to the latest beta builds (including QPRs)
until you choose to unenroll that device from the program. We also
deliver flashable images at each milestone, so you can choose the approach that
works best for your test environment.

Use the following links and instructions to update your supported device to the
latest build. See [Get
Android 17 QPR beta builds](/about/versions/17/get-qpr) for other ways to get
QPR1 for testing and development.

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
<https://flash.android.com/preview/cinnamonbun-qpr2-beta4>.

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
| **Release date** | August 28, 2026 |
| **Builds** | CP41.260814.003.A2 CP41.260814.003.B1 CP41.260814.003.C2 |
| **Emulator support** | x86 (64-bit), ARM (v8-A) |
| **Security patch level** | 2026-08-05 |
| **Google Play services** | 26.28.33 |

| Device | Download Link and SHA-256 Checksum |
| --- | --- |
| Pixel 6a | bluejay\_beta-cp41.260814.003.a2-factory-fb253ac7.zip  `fb253ac75dbbdf1afe9909b7de6ddabb40f72743556c3be54233ad905be70703` |
| Pixel 7 | panther\_beta-cp41.260814.003.a2-factory-a4686a9f.zip  `a4686a9f3739ade491f04f73ed17367eafadf67964b7be72fa87becbecee4b4c` |
| Pixel 7 Pro | cheetah\_beta-cp41.260814.003.a2-factory-a7faa0de.zip  `a7faa0def914caeb4237b2a303d9b99d080a9a7a9446865683bd3111a9bc6b3b` |
| Pixel 7a | lynx\_beta-cp41.260814.003.a2-factory-6bd1f053.zip  `6bd1f053b11cf61d910fa8f2b145fc11dc64852f871af4e3c0823b640f1ea1cb` |
| Pixel Fold | felix\_beta-cp41.260814.003.a2-factory-dcc92785.zip  `dcc92785e55eb70eb7c729d004b36b85c088ae4bbdbe4023c03085f33807755b` |
| Pixel Tablet | tangorpro\_beta-cp41.260814.003.a2-factory-7f643cdc.zip  `7f643cdcf8d864274512637821bc4a83d2e98594f22487110b35df082e6125fa` |
| Pixel 8 | shiba\_beta-cp41.260814.003.b1-factory-b83635b1.zip  `b83635b150e093f9aa86e333a4f28ffd3e1bd7dd4da4d6cb9c8226039e6bc156` |
| Pixel 8 Pro | husky\_beta-cp41.260814.003.b1-factory-5c620f38.zip  `5c620f38e80d0974adc669c6592a6108caa1e0e6de9f120ba6b376af174edf57` |
| Pixel 8a | akita\_beta-cp41.260814.003.b1-factory-06d1cf37.zip  `06d1cf370efcc18d5ea218e7037d664fc461e4c9ea50e55971bdf72c25b93697` |
| Pixel 9 | tokay\_beta-cp41.260814.003.b1-factory-a685aace.zip  `a685aacee2ec5482759c136e346c066c50c0562bf3664d9be89f85382e31d055` |
| Pixel 9 Pro | caiman\_beta-cp41.260814.003.b1-factory-74f277ea.zip  `74f277ead6b667ee82a2f3eb5804c7fc05332cd55693b811b2486a918272ce51` |
| Pixel 9 Pro XL | komodo\_beta-cp41.260814.003.b1-factory-22e33252.zip  `22e332521bdbb70dab4b57f450babaf451b82439bcd7a6bc2eb9bd5796469aa9` |
| Pixel 9 Pro Fold | comet\_beta-cp41.260814.003.b1-factory-be1a71b5.zip  `be1a71b55eb73554b717ce4e685695272ff200bd5b9a498bf12f2dd2516b99a3` |
| Pixel 9a | tegu\_beta-cp41.260814.003.b1-factory-315d7da3.zip  `315d7da33bfe472cf2e0e17dd8a1cfcd607682c983d2aef39c6a3be36b73bc6f` |
| Pixel 10 | frankel\_beta-cp41.260814.003.b1-factory-5e6de404.zip  `5e6de404cfef0a836c93fcb1e88a680318bf92ed02aa230f50b833c3c75d4e79` |
| Pixel 10 Pro | blazer\_beta-cp41.260814.003.b1-factory-de72c1ea.zip  `de72c1eaf67e48175a0e2ed5ee251eaa801c0b9fd7c8118392d14c5c08a1180e` |
| Pixel 10 Pro XL | mustang\_beta-cp41.260814.003.b1-factory-84bd89d7.zip  `84bd89d7cd7e5c4298af99ccbfa0e5a92be57d279c5d10709efb5c16caba8de3` |
| Pixel 10 Pro Fold | rango\_beta-cp41.260814.003.b1-factory-46a76c8c.zip  `46a76c8c1dc0c879cc3ff572daf5cab3b10d633e323b086d5b05ed2f64b53427` |
| Pixel 10a | stallion\_beta-cp41.260814.003.b1-factory-ac15a357.zip  `ac15a35758d2b2a1afdd2a1f40fb30b92db167042747f0afa88dd6bfcc7e94e7` |
| Pixel 11 | cubs\_beta-cp41.260814.003.c2-factory-36bc5e6a.zip  `36bc5e6a5909a46561a921fc0429e5e9790cb27a46338d7a8b514cfbe0968c7a` |
| Pixel 11 Pro | grizzly\_beta-cp41.260814.003.c2-factory-6b68d2d6.zip  `6b68d2d6ef7ddbb73be07bc8e0221b232982a39f7351a8162b4f75fb60d6fa83` |
| Pixel 11 Pro XL | kodiak\_beta-cp41.260814.003.c2-factory-f05888cd.zip  `f05888cde52d616a299676903886f0b2f627e01f02550723d9c5c75b07ae3e23` |
| Pixel 11 Pro Fold | yogi\_beta-cp41.260814.003.c2-factory-aa164c9a.zip  `aa164c9ac4ac9ff34b8f3acf2315c1fc4a9ee5a9c96ee49a8813ca82291676d3` |

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
[Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/bluejay_beta-cp41.260814.003.a2-factory-fb253ac7.zip)

*bluejay\_beta-cp41.260814.003.a2-factory-fb253ac7.zip*

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
[Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/panther_beta-cp41.260814.003.a2-factory-a4686a9f.zip)

*panther\_beta-cp41.260814.003.a2-factory-a4686a9f.zip*

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
[Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/cheetah_beta-cp41.260814.003.a2-factory-a7faa0de.zip)

*cheetah\_beta-cp41.260814.003.a2-factory-a7faa0de.zip*

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
[Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/lynx_beta-cp41.260814.003.a2-factory-6bd1f053.zip)

*lynx\_beta-cp41.260814.003.a2-factory-6bd1f053.zip*

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
[Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/felix_beta-cp41.260814.003.a2-factory-dcc92785.zip)

*felix\_beta-cp41.260814.003.a2-factory-dcc92785.zip*

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
[Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/tangorpro_beta-cp41.260814.003.a2-factory-7f643cdc.zip)

*tangorpro\_beta-cp41.260814.003.a2-factory-7f643cdc.zip*

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
[Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/shiba_beta-cp41.260814.003.b1-factory-b83635b1.zip)

*shiba\_beta-cp41.260814.003.b1-factory-b83635b1.zip*

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
[Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/husky_beta-cp41.260814.003.b1-factory-5c620f38.zip)

*husky\_beta-cp41.260814.003.b1-factory-5c620f38.zip*

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
[Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/akita_beta-cp41.260814.003.b1-factory-06d1cf37.zip)

*akita\_beta-cp41.260814.003.b1-factory-06d1cf37.zip*

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
[Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/tokay_beta-cp41.260814.003.b1-factory-a685aace.zip)

*tokay\_beta-cp41.260814.003.b1-factory-a685aace.zip*

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
[Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/caiman_beta-cp41.260814.003.b1-factory-74f277ea.zip)

*caiman\_beta-cp41.260814.003.b1-factory-74f277ea.zip*

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
[Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/komodo_beta-cp41.260814.003.b1-factory-22e33252.zip)

*komodo\_beta-cp41.260814.003.b1-factory-22e33252.zip*

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
[Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/comet_beta-cp41.260814.003.b1-factory-be1a71b5.zip)

*comet\_beta-cp41.260814.003.b1-factory-be1a71b5.zip*

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
[Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/tegu_beta-cp41.260814.003.b1-factory-315d7da3.zip)

*tegu\_beta-cp41.260814.003.b1-factory-315d7da3.zip*

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
[Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/frankel_beta-cp41.260814.003.b1-factory-5e6de404.zip)

*frankel\_beta-cp41.260814.003.b1-factory-5e6de404.zip*

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
[Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/blazer_beta-cp41.260814.003.b1-factory-de72c1ea.zip)

*blazer\_beta-cp41.260814.003.b1-factory-de72c1ea.zip*

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
[Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/mustang_beta-cp41.260814.003.b1-factory-84bd89d7.zip)

*mustang\_beta-cp41.260814.003.b1-factory-84bd89d7.zip*

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
[Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/rango_beta-cp41.260814.003.b1-factory-46a76c8c.zip)

*rango\_beta-cp41.260814.003.b1-factory-46a76c8c.zip*

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
[Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/stallion_beta-cp41.260814.003.b1-factory-ac15a357.zip)

*stallion\_beta-cp41.260814.003.b1-factory-ac15a357.zip*

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
[Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/cubs_beta-cp41.260814.003.c2-factory-36bc5e6a.zip)

*cubs\_beta-cp41.260814.003.c2-factory-36bc5e6a.zip*

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
[Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/grizzly_beta-cp41.260814.003.c2-factory-6b68d2d6.zip)

*grizzly\_beta-cp41.260814.003.c2-factory-6b68d2d6.zip*

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
[Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/kodiak_beta-cp41.260814.003.c2-factory-f05888cd.zip)

*kodiak\_beta-cp41.260814.003.c2-factory-f05888cd.zip*

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
[Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/yogi_beta-cp41.260814.003.c2-factory-aa164c9a.zip)

*yogi\_beta-cp41.260814.003.c2-factory-aa164c9a.zip*