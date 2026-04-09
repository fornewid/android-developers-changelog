---
title: OTA images for Google Pixel  |  Android Developers
url: https://developer.android.com/about/versions/17/download-ota
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Releases](https://developer.android.com/about/versions)

# OTA images for Google Pixel Stay organized with collections Save and categorize content based on your preferences.



Applying an OTA image can help you recover a device that received an OTA update
for an Android 17 Beta build but wouldn't start up
after the update was installed. If you are trying to get Android 17 on your
device but you aren't trying to recover from a failed OTA update, see [Get
Android 17](/about/versions/17/get) instead.

OTA images are available for the following Pixel devices:

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

After you've installed a beta build to your Pixel device, your device is
automatically enrolled in the [Android Beta for Pixel program](https://g.co/androidbeta) and offered
continuous over-the-air (OTA) updates to the latest beta builds (including QPRs)
until you choose to unenroll that device from the program.

We also deliver flashable images at each milestone, so you can choose the
approach that works best for your test environment.

Use the following links and instructions to update your supported device to the
latest build. See [Get Android 17](/about/versions/17/get) for
other ways to get Android 17 for testing and development.

## Apply an OTA image

![](/static/images/lockups/android-stacked.svg)

Download an OTA device image from the following table and apply it by following
the [updating instructions](https://developers.google.com/android/ota#instructions) listed on [Full OTA Images for Nexus and Pixel
Devices](https://developers.google.com/android/ota).

You can choose to [return to the latest public build](#public) at any time.

**Warning:** Before applying an Android 17 OTA image, we strongly recommend that you
[unlock the bootloader](https://source.android.com/docs/core/architecture/bootloader/locking_unlocking) on your device if possible. Unlocking the bootloader
requires a full device reset that removes all user data on the device, so make
sure to back up your data first.

### Device OTA Images

|  |  |
| --- | --- |
| **Release date** | March 26, 2026 |
| **Builds** | CP21.260306.017 |
| **Emulator support** | x86 (64-bit), ARM (v8-A) |
| **Security patch level** | 2026-03-05 |
| **Google Play services** | 26.02.35 |

| Device | Download Link and SHA-256 Checksum |
| --- | --- |
| Pixel 6 | oriole\_beta-ota-cp21.260306.017-1cd38395.zip  `1cd3839587c2be85a90cfabec0518818700fd1e00d28fe8e2b51313076e8953d` |
| Pixel 6 Pro | raven\_beta-ota-cp21.260306.017-9c93f9cd.zip  `9c93f9cdfb2dc1c03fc977204763d7e8bc4932f5be96277418563d97064f3c24` |
| Pixel 6a | bluejay\_beta-ota-cp21.260306.017-f668dde4.zip  `f668dde455702005048afaf9a95181669298f2bbd83d1ac03ef38a6fe10b2edc` |
| Pixel 7 | panther\_beta-ota-cp21.260306.017-de3c78ee.zip  `de3c78eee79aeed6200b8a7c2c998b94a67691c2ed888254abd8774fbfcfae93` |
| Pixel 7 Pro | cheetah\_beta-ota-cp21.260306.017-df0d12e3.zip  `df0d12e37cea800f87ec77bf9ed3d3185ef006afe93c1344bed38c47b5a87f16` |
| Pixel 7a | lynx\_beta-ota-cp21.260306.017-16a37b46.zip  `16a37b46d4c325d435e9bb480b70c36a21016d543e10c19db7d45d238d023888` |
| Pixel Fold | felix\_beta-ota-cp21.260306.017-1016c563.zip  `1016c563d40dd53afb5d84ae430951899a09281ab687f6825b2f8bb2f33cfb2e` |
| Pixel Tablet | tangorpro\_beta-ota-cp21.260306.017-be05155b.zip  `be05155bb52f73e4d3ceb4eb712b537f6e58eda64dd8ce397e1cc71a89f291f9` |
| Pixel 8 | shiba\_beta-ota-cp21.260306.017-0f5bc69c.zip  `0f5bc69c007d104350013858941ada6ad26cc3a3e70674b9390bcaa1a4d81e1d` |
| Pixel 8 Pro | husky\_beta-ota-cp21.260306.017-908488d1.zip  `908488d19ee9a289daef7e31fa6bd9b477744186cc97493677db1c5fdd66a25b` |
| Pixel 8a | akita\_beta-ota-cp21.260306.017-05081860.zip  `050818601db13ea191db3a252008b501599105802290a0bf1aa7a6bf4abf4fce` |
| Pixel 9 | tokay\_beta-ota-cp21.260306.017-beaa6d0b.zip  `beaa6d0bf5d558843dbc3c27201deaf93fe61aef6e2b59e3a86576a3ba9d89a3` |
| Pixel 9 Pro | caiman\_beta-ota-cp21.260306.017-0e914787.zip  `0e914787d8bb2b0c5459aa8a1f99892d28244bc66fb2dc28a28b482f185967f4` |
| Pixel 9 Pro XL | komodo\_beta-ota-cp21.260306.017-115abfb1.zip  `115abfb19d86b9f6b7dfaae8237b97eed94e56e524685b0f0d7aae184f693e1f` |
| Pixel 9 Pro Fold | comet\_beta-ota-cp21.260306.017-ec1c4417.zip  `ec1c4417ec4fef1373c190e54f9b93bd7a031ca5df97ee6f5460b959396abc3e` |
| Pixel 9a | tegu\_beta-ota-cp21.260306.017-879c9383.zip  `879c93832919303ba4d6a12a727f44538ea86273052c2fc003f4aab8663857b2` |
| Pixel 10 | frankel\_beta-ota-cp21.260306.017-06d6da53.zip  `06d6da53e2954668533e935b13166ae3e2bde23ab19c598341c11aff36e41e59` |
| Pixel 10 Pro | blazer\_beta-ota-cp21.260306.017-93988f0d.zip  `93988f0d5ec7e627104ab6ccf104d316c42f2da71c9254a3d55b72718526c9e7` |
| Pixel 10 Pro XL | mustang\_beta-ota-cp21.260306.017-3da744d3.zip  `3da744d349401de4fafcdd298f5ecc2f42f0128e850d91cd79c457e9585ac5ee` |
| Pixel 10 Pro Fold | rango\_beta-ota-cp21.260306.017-595cf59e.zip  `595cf59e464009633965564f614e697f608dbbbe5ac2fbc6229ee72576b227f2` |

## Return to a public build

You can either use the Android Flash Tool to
[flash the factory image](https://flash.android.com/back-to-public), or obtain a factory spec system
image from the [Factory Images for Nexus and Pixel Devices](https://developers.google.com/android/images)
page and then manually flash it to the device.

**Warning:** Going back to a public build from a preview build (Developer Preview
or Beta) requires a full device reset that removes all user data on the device.
Make sure to [back up your data first](https://support.google.com/pixelphone/answer/7179901).

## Download Android 17 OTA system image

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

Download Android 17 OTA system image
[Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/oriole_beta-ota-cp21.260306.017-1cd38395.zip)

*oriole\_beta-ota-cp21.260306.017-1cd38395.zip*

## Download Android 17 OTA system image

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

Download Android 17 OTA system image
[Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/raven_beta-ota-cp21.260306.017-9c93f9cd.zip)

*raven\_beta-ota-cp21.260306.017-9c93f9cd.zip*

## Download Android 17 OTA system image

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

Download Android 17 OTA system image
[Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/bluejay_beta-ota-cp21.260306.017-f668dde4.zip)

*bluejay\_beta-ota-cp21.260306.017-f668dde4.zip*

## Download Android 17 OTA system image

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

Download Android 17 OTA system image
[Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/panther_beta-ota-cp21.260306.017-de3c78ee.zip)

*panther\_beta-ota-cp21.260306.017-de3c78ee.zip*

## Download Android 17 OTA system image

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

Download Android 17 OTA system image
[Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/cheetah_beta-ota-cp21.260306.017-df0d12e3.zip)

*cheetah\_beta-ota-cp21.260306.017-df0d12e3.zip*

## Download Android 17 OTA system image

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

Download Android 17 OTA system image
[Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/lynx_beta-ota-cp21.260306.017-16a37b46.zip)

*lynx\_beta-ota-cp21.260306.017-16a37b46.zip*

## Download Android 17 OTA system image

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

Download Android 17 OTA system image
[Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/felix_beta-ota-cp21.260306.017-1016c563.zip)

*felix\_beta-ota-cp21.260306.017-1016c563.zip*

## Download Android 17 OTA system image

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

Download Android 17 OTA system image
[Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/tangorpro_beta-ota-cp21.260306.017-be05155b.zip)

*tangorpro\_beta-ota-cp21.260306.017-be05155b.zip*

## Download Android 17 OTA system image

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

Download Android 17 OTA system image
[Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/shiba_beta-ota-cp21.260306.017-0f5bc69c.zip)

*shiba\_beta-ota-cp21.260306.017-0f5bc69c.zip*

## Download Android 17 OTA system image

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

Download Android 17 OTA system image
[Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/husky_beta-ota-cp21.260306.017-908488d1.zip)

*husky\_beta-ota-cp21.260306.017-908488d1.zip*

## Download Android 17 OTA system image

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

Download Android 17 OTA system image
[Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/akita_beta-ota-cp21.260306.017-05081860.zip)

*akita\_beta-ota-cp21.260306.017-05081860.zip*

## Download Android 17 OTA system image

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

Download Android 17 OTA system image
[Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/tokay_beta-ota-cp21.260306.017-beaa6d0b.zip)

*tokay\_beta-ota-cp21.260306.017-beaa6d0b.zip*

## Download Android 17 OTA system image

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

Download Android 17 OTA system image
[Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/caiman_beta-ota-cp21.260306.017-0e914787.zip)

*caiman\_beta-ota-cp21.260306.017-0e914787.zip*

## Download Android 17 OTA system image

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

Download Android 17 OTA system image
[Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/komodo_beta-ota-cp21.260306.017-115abfb1.zip)

*komodo\_beta-ota-cp21.260306.017-115abfb1.zip*

## Download Android 17 OTA system image

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

Download Android 17 OTA system image
[Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/comet_beta-ota-cp21.260306.017-ec1c4417.zip)

*comet\_beta-ota-cp21.260306.017-ec1c4417.zip*

## Download Android 17 OTA system image

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

Download Android 17 OTA system image
[Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/tegu_beta-ota-cp21.260306.017-879c9383.zip)

*tegu\_beta-ota-cp21.260306.017-879c9383.zip*

## Download Android 17 OTA system image

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

Download Android 17 OTA system image
[Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/frankel_beta-ota-cp21.260306.017-06d6da53.zip)

*frankel\_beta-ota-cp21.260306.017-06d6da53.zip*

## Download Android 17 OTA system image

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

Download Android 17 OTA system image
[Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/blazer_beta-ota-cp21.260306.017-93988f0d.zip)

*blazer\_beta-ota-cp21.260306.017-93988f0d.zip*

## Download Android 17 OTA system image

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

Download Android 17 OTA system image
[Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/mustang_beta-ota-cp21.260306.017-3da744d3.zip)

*mustang\_beta-ota-cp21.260306.017-3da744d3.zip*

## Download Android 17 OTA system image

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

Download Android 17 OTA system image
[Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/rango_beta-ota-cp21.260306.017-595cf59e.zip)

*rango\_beta-ota-cp21.260306.017-595cf59e.zip*