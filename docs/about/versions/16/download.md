---
title: https://developer.android.com/about/versions/16/download
url: https://developer.android.com/about/versions/16/download
source: md.txt
---

If you are a developer with a supported Google Pixel device, you can manually
update that device to the latest build for testing and development. Flashing a
factory image requires a full device reset, so make sure to [back up your
data](https://support.google.com/pixelphone/answer/7179901) first. Builds are available for the following Pixel devices:

- Pixel 6 and 6 Pro
- Pixel 6a
- Pixel 7 and 7 Pro
- Pixel 7a
- Pixel Fold
- Pixel Tablet
- Pixel 8 and 8 Pro
- Pixel 8a
- Pixel 9, 9 Pro, 9 Pro XL, and 9 Pro Fold
- Pixel 9a

After you've flashed a beta build to your Pixel device, your device is automatically enrolled in the [Android Beta for Pixel program](https://g.co/androidbeta) and offered continuous over-the-air (OTA) updates to the latest beta builds (including QPRs) until you choose to unenroll that device from the program. We also deliver flashable images at each milestone, so you can choose the approach that works best for your test environment.

<br />

Use the following links and instructions to update your supported device to the
latest build. See [Get
Android 16 QPR beta builds](https://developer.android.com/about/versions/16/get-qpr) for other ways to get
QPR2 for testing and development.
| **Warning:** Flashing to a beta build from a production build---or going back to a production build from a beta build---requires a full device reset that removes all user data on the device. Make sure to [back up the data from your
| Pixel](https://support.google.com/pixelphone/answer/7179901) first.

## Flash your device using Android Flash Tool

**Android Flash Tool** lets you securely flash a system image
to your supported Pixel device. Android Flash Tool works with any Web browser
that supports WebUSB, such as Chrome or Edge 79+.

Android Flash Tool guides you step-by-step through the process of flashing your
device---there's no need to have tools installed---but you do need to unlock your
device and [enable USB Debugging in Developer options](https://developer.android.com/studio/debug/dev-options#enable). For
complete instructions, see the [Android Flash Tool
documentation](https://source.android.com/setup/contribute/flash).

Connect your device over USB, then navigate to Android Flash Tool using the
following link and follow the onscreen guidance:
<https://flash.android.com/preview/baklava-qpr1-beta3.1>.

## Flash your device manually

![](https://developer.android.com/static/images/lockups/android-stacked.svg)

You can also download the latest system image and manually flash it to your
device. See the following table to download the system image for your test
device. Manually flashing a device is useful if you need precise control over
the test environment or if you need to reinstall frequently, such as when
performing automated testing.

After you back up your device data and download the matching system image, you
can [flash the image onto your device](https://developers.google.com/android/images#instructions).

You can choose to [return to the latest public build](https://developer.android.com/about/versions/16/download#public) at any
time.

### Device factory images

|---|---|
| **Release date** | August 14, 2025 |
| **Builds** | BP31.250610.009 BP31.250610.009.A1 (Pixel Tablet) |
| **Emulator support** | x86 (64-bit), ARM (v8-A) |
| **Security patch level** | July 2025 |
| **Google Play services** | 25.20.39 |

| Device | Download Link and SHA-256 Checksum |
|---|---|
| Pixel 6 | oriole_beta-bp31.250610.009-factory-55b4d2fb.zip `55b4d2fb7960977832a59ff06c3f773b05b703fca8fe9e8ac8cc5ac01adb13bf` |
| Pixel 6 Pro | raven_beta-bp31.250610.009-factory-c8489c65.zip `c8489c6592da74d0cbd3d00eb685be1c5acf3784830c693098a88f1fbcc18a8a` |
| Pixel 7 | panther_beta-bp31.250610.009-factory-05412f61.zip `05412f61d102d142ba75fcffdc81fb582ebd86405d60651774e732e474876e15` |
| Pixel 7 Pro | cheetah_beta-bp31.250610.009-factory-09a15154.zip `09a15154371e70c73206ff9d1c2b76ccca244f209f256443957eb62e33f8486d` |
| Pixel 7a | lynx_beta-bp31.250610.009-factory-1687ed0d.zip `1687ed0daa1ef0216ddbfaa55dfd8e8671d356a0956bf00d52a60415676f8e5c` |
| Pixel Fold | felix_beta-bp31.250610.009-factory-e81742ee.zip `e81742eeb6de9ff9c645cc7020582d28a05ae4ebb43d6c542051f8dbe167d34c` |
| Pixel Tablet | tangorpro_beta-bp31.250610.009.a1-factory-215f9306.zip `215f9306fcc0a6ce5c4c5704e88ba4a38f3768e160256786000eceffdb4c9313` |
| Pixel 8 | shiba_beta-bp31.250610.009-factory-d03d122e.zip `d03d122e081d3023d23565dbb2ea93757a514235c3817891c8ce5419b4c30bd1` |
| Pixel 8 Pro | husky_beta-bp31.250610.009-factory-f8edd5b7.zip `f8edd5b7a72c9a5d4bad64d5e70594fb2fab0ee6ef9c8b0ee46c324c905d5801` |
| Pixel 8a | akita_beta-bp31.250610.009-factory-da36a8f4.zip `da36a8f4ec90d5bdd7a2b4b6fa2f6e07549eef77f1900567b7eda9331e32cd7e` |
| Pixel 9 | tokay_beta-bp31.250610.009-factory-e16c40af.zip `e16c40af1da3bb491f17201e83526cb18cce1e3af3f48ba4bbe815da7df966a3` |
| Pixel 9 Pro | caiman_beta-bp31.250610.009-factory-7bad5521.zip `7bad5521018df6aa3b3e7cefaf0ee1b74ea2be4140376e66bf25c06b432da886` |
| Pixel 9 Pro XL | komodo_beta-bp31.250610.009-factory-88a642fc.zip `88a642fcc860a7ae93088e70c7c2c663a62a737cd7ff384f34b84fddcffacf71` |
| Pixel 9 Pro Fold | comet_beta-bp31.250610.009-factory-11ad869b.zip `11ad869bf8e2b04ec56765fc1ea65a84aaf7c89d9bd642e75e0e8f437b41d98c` |
| Pixel 9a | tegu_beta-bp31.250610.009-factory-41249425.zip `412494257616877fc3338e6cc634fb164bdfcd9151e68944392997759a5369a6` |

## Return to a public build

You can either use the Android Flash Tool to
[flash the factory image](https://flash.android.com/back-to-public), or obtain a factory spec system
image from the [Factory Images for Nexus and Pixel Devices](https://developers.google.com/android/images)
page and then manually flash it to the device.
**Warning:** Going back to a public build from a preview build (Developer Preview or Beta) requires a full device reset that removes all user data on the device. Make sure to [back up your data first](https://support.google.com/pixelphone/answer/7179901).  

## Download Android 16 factory system image

Before downloading, you must agree to the following terms and conditions.  

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.  
I have read and agree with the above terms and conditions  
Download Android 16 factory system image [Download Android 16 factory system image](https://dl.google.com/developers/android/baklava/images/factory/oriole_beta-bp31.250610.009-factory-55b4d2fb.zip)

*oriole_beta-bp31.250610.009-factory-55b4d2fb.zip*  

## Download Android 16 factory system image

Before downloading, you must agree to the following terms and conditions.  

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.  
I have read and agree with the above terms and conditions  
Download Android 16 factory system image [Download Android 16 factory system image](https://dl.google.com/developers/android/baklava/images/factory/raven_beta-bp31.250610.009-factory-c8489c65.zip)

*raven_beta-bp31.250610.009-factory-c8489c65.zip*  

## Download Android 16 factory system image

Before downloading, you must agree to the following terms and conditions.  

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.  
I have read and agree with the above terms and conditions  
Download Android 16 factory system image [Download Android 16 factory system image](https://dl.google.com/developers/android/baklava/images/factory/panther_beta-bp31.250610.009-factory-05412f61.zip)

*panther_beta-bp31.250610.009-factory-05412f61.zip*  

## Download Android 16 factory system image

Before downloading, you must agree to the following terms and conditions.  

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.  
I have read and agree with the above terms and conditions  
Download Android 16 factory system image [Download Android 16 factory system image](https://dl.google.com/developers/android/baklava/images/factory/cheetah_beta-bp31.250610.009-factory-09a15154.zip)

*cheetah_beta-bp31.250610.009-factory-09a15154.zip*  

## Download Android 16 factory system image

Before downloading, you must agree to the following terms and conditions.  

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.  
I have read and agree with the above terms and conditions  
Download Android 16 factory system image [Download Android 16 factory system image](https://dl.google.com/developers/android/baklava/images/factory/lynx_beta-bp31.250610.009-factory-1687ed0d.zip)

*lynx_beta-bp31.250610.009-factory-1687ed0d.zip*  

## Download Android 16 factory system image

Before downloading, you must agree to the following terms and conditions.  

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.  
I have read and agree with the above terms and conditions  
Download Android 16 factory system image [Download Android 16 factory system image](https://dl.google.com/developers/android/baklava/images/factory/felix_beta-bp31.250610.009-factory-e81742ee.zip)

*felix_beta-bp31.250610.009-factory-e81742ee.zip*  

## Download Android 16 factory system image

Before downloading, you must agree to the following terms and conditions.  

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.  
I have read and agree with the above terms and conditions  
Download Android 16 factory system image [Download Android 16 factory system image](https://dl.google.com/developers/android/baklava/images/factory/tangorpro_beta-bp31.250610.009.a1-factory-215f9306.zip)

*tangorpro_beta-bp31.250610.009.a1-factory-215f9306.zip*  

## Download Android 16 factory system image

Before downloading, you must agree to the following terms and conditions.  

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.  
I have read and agree with the above terms and conditions  
Download Android 16 factory system image [Download Android 16 factory system image](https://dl.google.com/developers/android/baklava/images/factory/shiba_beta-bp31.250610.009-factory-d03d122e.zip)

*shiba_beta-bp31.250610.009-factory-d03d122e.zip*  

## Download Android 16 factory system image

Before downloading, you must agree to the following terms and conditions.  

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.  
I have read and agree with the above terms and conditions  
Download Android 16 factory system image [Download Android 16 factory system image](https://dl.google.com/developers/android/baklava/images/factory/husky_beta-bp31.250610.009-factory-f8edd5b7.zip)

*husky_beta-bp31.250610.009-factory-f8edd5b7.zip*  

## Download Android 16 factory system image

Before downloading, you must agree to the following terms and conditions.  

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.  
I have read and agree with the above terms and conditions  
Download Android 16 factory system image [Download Android 16 factory system image](https://dl.google.com/developers/android/baklava/images/factory/akita_beta-bp31.250610.009-factory-da36a8f4.zip)

*akita_beta-bp31.250610.009-factory-da36a8f4.zip*  

## Download Android 16 factory system image

Before downloading, you must agree to the following terms and conditions.  

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.  
I have read and agree with the above terms and conditions  
Download Android 16 factory system image [Download Android 16 factory system image](https://dl.google.com/developers/android/baklava/images/factory/tokay_beta-bp31.250610.009-factory-e16c40af.zip)

*tokay_beta-bp31.250610.009-factory-e16c40af.zip*  

## Download Android 16 factory system image

Before downloading, you must agree to the following terms and conditions.  

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.  
I have read and agree with the above terms and conditions  
Download Android 16 factory system image [Download Android 16 factory system image](https://dl.google.com/developers/android/baklava/images/factory/caiman_beta-bp31.250610.009-factory-7bad5521.zip)

*caiman_beta-bp31.250610.009-factory-7bad5521.zip*  

## Download Android 16 factory system image

Before downloading, you must agree to the following terms and conditions.  

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.  
I have read and agree with the above terms and conditions  
Download Android 16 factory system image [Download Android 16 factory system image](https://dl.google.com/developers/android/baklava/images/factory/komodo_beta-bp31.250610.009-factory-88a642fc.zip)

*komodo_beta-bp31.250610.009-factory-88a642fc.zip*  

## Download Android 16 factory system image

Before downloading, you must agree to the following terms and conditions.  

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.  
I have read and agree with the above terms and conditions  
Download Android 16 factory system image [Download Android 16 factory system image](https://dl.google.com/developers/android/baklava/images/factory/comet_beta-bp31.250610.009-factory-11ad869b.zip)

*comet_beta-bp31.250610.009-factory-11ad869b.zip*  

## Download Android 16 factory system image

Before downloading, you must agree to the following terms and conditions.  

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.  
I have read and agree with the above terms and conditions  
Download Android 16 factory system image [Download Android 16 factory system image](https://dl.google.com/developers/android/baklava/images/factory/tegu_beta-bp31.250610.009-factory-41249425.zip)

*tegu_beta-bp31.250610.009-factory-41249425.zip*