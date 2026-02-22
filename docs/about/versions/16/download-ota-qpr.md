---
title: https://developer.android.com/about/versions/16/download-ota-qpr
url: https://developer.android.com/about/versions/16/download-ota-qpr
source: md.txt
---

Building on the [initial release of Android 16](https://developer.android.com/about/versions/16), we continue to update the platform with fixes and improvements that are then rolled out to supported devices. These releases happen on a quarterly cadence through *Quarterly Platform Releases* (QPRs), which are delivered both to AOSP and to Google Pixel devices as part of *Feature Drops* .

<br />

Although these updates don't include app-impacting API changes, we provide
images of the latest QPR beta builds so you can test your app with these builds
as needed (for example, if there are upcoming features that might impact the
user experience of your app).

To find OTA images for already-released, stable versions of the platform, see
[Full OTA Images for Nexus and Pixel Devices](https://developers.google.com/android/ota).
Applying an OTA image can help you recover a device that received an OTA update
for an Android 16 QPR Beta build but wouldn't start up after the update was
installed. If you are trying to get Android 16 QPR1 on your device but you
aren't trying to recover from a failed OTA update, see [Get Android 16 QPR beta
builds](https://developer.android.com/about/versions/16/get-qpr) instead.
OTA images are available for the following Pixel devices:
\* Pixel 6 and 6 Pro
\* Pixel 7, 7a, and 7 Pro
\* Pixel Fold
\* Pixel Tablet
\* Pixel 8, 8a, and 8 Pro
\* Pixel 9, 9a, 9 Pro, 9 Pro XL, and 9 Pro Fold

After you've installed a beta build to your Pixel device, your device is
automatically enrolled in the [Android Beta for Pixel program](https://g.co/androidbeta) and offered
continuous over-the-air (OTA) updates to the latest beta builds (including QPRs)
until you choose to unenroll that device from the program. We also deliver
flashable images at each milestone, so you can choose the approach that works
best for your test environment.
Use the following links and instructions to update your supported device to the
latest build. See [Get Android 16 QPR beta builds](https://developer.android.com/about/versions/16/get-qpr) for other ways to get QPR1
for testing and development.

## Apply an OTA image

![](https://developer.android.com/static/images/lockups/android-stacked.svg)
Download an OTA device image from the following table and apply it by following
the [updating instructions](https://developers.google.com/android/ota#instructions) listed on [Full OTA Images for Nexus and Pixel
Devices](https://developers.google.com/android/ota).
You can choose to [return to the latest public build](https://developer.android.com/about/versions/16/download-ota-qpr#public) at any time.

<br />

Warning: Before applying an Android 16 OTA image, we strongly recommend that you [unlock the bootloader](https://source.android.com/docs/core/architecture/bootloader/locking_unlocking) on your device if possible. Unlocking the bootloader requires a full device reset that removes all user data on the device, so make sure to back up your data first.

<br />

### Device OTA Images

| Device | Download Link and SHA-256 Checksum |
|---|---|
| Pixel 6 | oriole_beta-ota-bp31.250610.009-a8931292.zip `a8931292a44a1aed223cc8c75a2d96fe2e8978f0e1985f644235eb295db3eb4d` |
| Pixel 6 Pro | raven_beta-ota-bp31.250610.009-d50cbe02.zip `d50cbe0284585a39436278c79218ab9f9f6004464c81a42478c46cf2a3ffa4dc` |
| Pixel 6a | bluejay_beta-ota-bp31.250610.009-d3bb37f4.zip `d3bb37f4f58c6eea6ec1e61f0be8de66434c72cf7294b6efe661edec3cbac2b7` |
| Pixel 7 | panther_beta-ota-bp31.250610.009-87945fd4.zip `87945fd4aece5bbf32bd0d12f0cc23e1dec1416afee3904fc9107bdde80467fe` |
| Pixel 7 Pro | cheetah_beta-ota-bp31.250610.009-7bcf96be.zip `7bcf96be8b7645f4cf971bda3d2a380207c45d140db1021d4f02168b19297638` |
| Pixel 7a | lynx_beta-ota-bp31.250610.009-d8735e68.zip `d8735e68ea115b2c6bfd9ec1ab7070b538dbae58d21e25048c84e054336ffc02` |
| Pixel Fold | felix_beta-ota-bp31.250610.009-c6c20143.zip `c6c2014385605fd967a873336a93efbd267a03cbd99c78b7ed800f7dcf20fc22` |
| Pixel Tablet | tangorpro_beta-ota-bp31.250610.009.a1-fdf5e8bc.zip `fdf5e8bcf0cb66b9174b3de01af3991a1ed70f2a5d87661d82a929e7da676ab0` |
| Pixel 8 | shiba_beta-ota-bp31.250610.009-eac96fbd.zip `eac96fbd7f21124b08fa73cbdb8799a185650e547c54bd2e3786b883286ff982` |
| Pixel 8 Pro | husky_beta-ota-bp31.250610.009-6f2fad5a.zip `6f2fad5a5cd82c1b1746d771d2e517d387a8288803547f6fc920d3e9f54be080` |
| Pixel 8a | akita_beta-ota-bp31.250610.009-a7be43a9.zip `a7be43a9c89d9aa0c670ba248c491923af0e303db5869e3b7a321cb42d6a3348` |
| Pixel 9 | tokay_beta-ota-bp31.250610.009-71027e34.zip `71027e34f431caabb68ff7b3c5613ed1d3b7b2578251431d52aadd91972f28a7` |
| Pixel 9 Pro | caiman_beta-ota-bp31.250610.009-346d05e4.zip `346d05e49a4a57f3c1ad5896fa6d6a344e394c16642746cc359dc0a007f06b10` |
| Pixel 9 Pro XL | komodo_beta-ota-bp31.250610.009-d04c8659.zip `d04c86594d1c5f8d3673ba5155c5eaa2b23687110695f2f579477fe894cc8aa3` |
| Pixel 9 Pro Fold | comet_beta-ota-bp31.250610.009-f9a36227.zip `f9a36227dc5782ae30df6d2af6ab4410a2a3d1346fe10f314f3e8b593203fcab` |
| Pixel 9a | tegu_beta-ota-bp31.250610.009-4de94f08.zip `4de94f08c92211713553b3e1f62e13c9d864baa3a6578588264b58af9ff973ba` |

## Return to a public build

You can either use the Android Flash Tool to
[flash the factory image](https://flash.android.com/back-to-public), or obtain a factory spec system
image from the [Factory Images for Nexus and Pixel Devices](https://developers.google.com/android/images)
page and then manually flash it to the device.
**Warning:** Going back to a public build from a preview build (Developer Preview or Beta) requires a full device reset that removes all user data on the device. Make sure to [back up your data first](https://support.google.com/pixelphone/answer/7179901).  

## Download Android 16 QPR2

Before downloading, you must agree to the following terms and conditions.  

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.  
I have read and agree with the above terms and conditions  
Download Android 16 QPR2 [Download Android 16 QPR2](https://dl.google.com/developers/android/baklava/images/ota/oriole_beta-ota-bp31.250610.009-a8931292.zip)

*oriole_beta-ota-bp31.250610.009-a8931292.zip*  

## Download Android 16 QPR2

Before downloading, you must agree to the following terms and conditions.  

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.  
I have read and agree with the above terms and conditions  
Download Android 16 QPR2 [Download Android 16 QPR2](https://dl.google.com/developers/android/baklava/images/ota/raven_beta-ota-bp31.250610.009-d50cbe02.zip)

*raven_beta-ota-bp31.250610.009-d50cbe02.zip*  

## Download Android 16 QPR2

Before downloading, you must agree to the following terms and conditions.  

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.  
I have read and agree with the above terms and conditions  
Download Android 16 QPR2 [Download Android 16 QPR2](https://dl.google.com/developers/android/baklava/images/ota/panther_beta-ota-bp31.250610.009-87945fd4.zip)

*panther_beta-ota-bp31.250610.009-87945fd4.zip*  

## Download Android 16 QPR2

Before downloading, you must agree to the following terms and conditions.  

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.  
I have read and agree with the above terms and conditions  
Download Android 16 QPR2 [Download Android 16 QPR2](https://dl.google.com/developers/android/baklava/images/ota/cheetah_beta-ota-bp31.250610.009-7bcf96be.zip)

*cheetah_beta-ota-bp31.250610.009-7bcf96be.zip*  

## Download Android 16 QPR2

Before downloading, you must agree to the following terms and conditions.  

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.  
I have read and agree with the above terms and conditions  
Download Android 16 QPR2 [Download Android 16 QPR2](https://dl.google.com/developers/android/baklava/images/ota/lynx_beta-ota-bp31.250610.009-d8735e68.zip)

*lynx_beta-ota-bp31.250610.009-d8735e68.zip*  

## Download Android 16 QPR2

Before downloading, you must agree to the following terms and conditions.  

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.  
I have read and agree with the above terms and conditions  
Download Android 16 QPR2 [Download Android 16 QPR2](https://dl.google.com/developers/android/baklava/images/ota/felix_beta-ota-bp31.250610.009-c6c20143.zip)

*felix_beta-ota-bp31.250610.009-c6c20143.zip*  

## Download Android 16 QPR2

Before downloading, you must agree to the following terms and conditions.  

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.  
I have read and agree with the above terms and conditions  
Download Android 16 QPR2 [Download Android 16 QPR2](https://dl.google.com/developers/android/baklava/images/ota/tangorpro_beta-ota-bp31.250610.009.a1-fdf5e8bc.zip)

*tangorpro_beta-ota-bp31.250610.009.a1-fdf5e8bc.zip*  

## Download Android 16 QPR2

Before downloading, you must agree to the following terms and conditions.  

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.  
I have read and agree with the above terms and conditions  
Download Android 16 QPR2 [Download Android 16 QPR2](https://dl.google.com/developers/android/baklava/images/ota/shiba_beta-ota-bp31.250610.009-eac96fbd.zip)

*shiba_beta-ota-bp31.250610.009-eac96fbd.zip*  

## Download Android 16 QPR2

Before downloading, you must agree to the following terms and conditions.  

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.  
I have read and agree with the above terms and conditions  
Download Android 16 QPR2 [Download Android 16 QPR2](https://dl.google.com/developers/android/baklava/images/ota/husky_beta-ota-bp31.250610.009-6f2fad5a.zip)

*husky_beta-ota-bp31.250610.009-6f2fad5a.zip*  

## Download Android 16 QPR2

Before downloading, you must agree to the following terms and conditions.  

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.  
I have read and agree with the above terms and conditions  
Download Android 16 QPR2 [Download Android 16 QPR2](https://dl.google.com/developers/android/baklava/images/ota/akita_beta-ota-bp31.250610.009-a7be43a9.zip)

*akita_beta-ota-bp31.250610.009-a7be43a9.zip*  

## Download Android 16 QPR2

Before downloading, you must agree to the following terms and conditions.  

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.  
I have read and agree with the above terms and conditions  
Download Android 16 QPR2 [Download Android 16 QPR2](https://dl.google.com/developers/android/baklava/images/ota/tokay_beta-ota-bp31.250610.009-71027e34.zip)

*tokay_beta-ota-bp31.250610.009-71027e34.zip*  

## Download Android 16 QPR2

Before downloading, you must agree to the following terms and conditions.  

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.  
I have read and agree with the above terms and conditions  
Download Android 16 QPR2 [Download Android 16 QPR2](https://dl.google.com/developers/android/baklava/images/ota/caiman_beta-ota-bp31.250610.009-346d05e4.zip)

*caiman_beta-ota-bp31.250610.009-346d05e4.zip*  

## Download Android 16 QPR2

Before downloading, you must agree to the following terms and conditions.  

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.  
I have read and agree with the above terms and conditions  
Download Android 16 QPR2 [Download Android 16 QPR2](https://dl.google.com/developers/android/baklava/images/ota/komodo_beta-ota-bp31.250610.009-d04c8659.zip)

*komodo_beta-ota-bp31.250610.009-d04c8659.zip*  

## Download Android 16 QPR2

Before downloading, you must agree to the following terms and conditions.  

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.  
I have read and agree with the above terms and conditions  
Download Android 16 QPR2 [Download Android 16 QPR2](https://dl.google.com/developers/android/baklava/images/ota/comet_beta-ota-bp31.250610.009-f9a36227.zip)

*comet_beta-ota-bp31.250610.009-f9a36227.zip*  

## Download Android 16 QPR2

Before downloading, you must agree to the following terms and conditions.  

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.  
I have read and agree with the above terms and conditions  
Download Android 16 QPR2 [Download Android 16 QPR2](https://dl.google.com/developers/android/baklava/images/ota/tegu_beta-ota-bp31.250610.009-4de94f08.zip)

*tegu_beta-ota-bp31.250610.009-4de94f08.zip*