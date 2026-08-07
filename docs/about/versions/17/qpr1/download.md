---
title: https://developer.android.com/about/versions/17/qpr1/download
url: https://developer.android.com/about/versions/17/qpr1/download
source: md.txt
---

If you are a developer with a supported Google Pixel device, you can manually update that device to the latest build for testing and development. Flashing a factory image requires a full device reset, so make sure to [back up your data](https://support.google.com/pixelphone/answer/7179901) first. Builds are available for the following Pixel devices:

- Pixel 6
- Pixel 6 Pro
- Pixel 6a
- Pixel 7
- Pixel 7 Pro
- Pixel 7a
- Pixel Tablet
- Pixel Fold
- Pixel 8
- Pixel 8 Pro
- Pixel 8a
- Pixel 9
- Pixel 9 Pro
- Pixel 9 Pro XL
- Pixel 9 Pro Fold
- Pixel 9a
- Pixel 10
- Pixel 10 Pro
- Pixel 10 Pro XL
- Pixel 10 Pro Fold
- Pixel 10a

After you've flashed a beta build to your Pixel device, your device is automatically enrolled in the [Android Beta for Pixel program](https://g.co/androidBeta) and offered continuous over-the-air (OTA) updates to the latest beta builds (including QPRs) until you choose to unenroll that device from the program. We also deliver flashable images at each milestone, so you can choose the approach that works best for your test environment.

<br />

Use the following links and instructions to update your supported device to the latest build. See [Get Android 17 QPR beta builds](https://developer.android.com/about/versions/17/get-qpr) for other ways to get QPR1 for testing and development.

> [!WARNING]
> **Warning:** Flashing to a beta build from a production build---or going back to a production build from a beta build---requires a full device reset that removes all user data on the device. Make sure to [back up the data from your Pixel](https://support.google.com/pixelphone/answer/7179901) first.

## Flash your device using Android Flash Tool

**Android Flash Tool** lets you securely flash a system image to your supported Pixel device. Android Flash Tool works with any Web browser that supports WebUSB, such as Chrome or Edge 79+.

Android Flash Tool guides you step-by-step through the process of flashing your device---there's no need to have tools installed---but you do need to unlock your device and [enable USB Debugging in Developer options](https://developer.android.com/studio/debug/dev-options#enable). For complete instructions, see the [Android Flash Tool documentation](https://source.android.com/setup/contribute/flash).

Connect your device over USB, then navigate to Android Flash Tool using the following link and follow the onscreen guidance: <https://flash.android.com/preview/cinnamonbun-qpr1-beta8>.

## Flash your device manually


![](https://developer.android.com/static/images/lockups/android-stacked.svg)

You can also download the latest system image and manually flash it to your device. See the following table to download the system image for your test device. Manually flashing a device is useful if you need precise control over the test environment or if you need to reinstall frequently, such as when performing automated testing.

After you back up your device data and download the matching system image, you can [flash the image onto your device](https://developers.google.com/android/images#instructions).

You can choose to [return to the latest public build](https://developer.android.com/about/versions/17/qpr1/download#public) at any time.

### Device factory images

|---|---|
| **Release date** | June 1, 2026 |
| **Builds** | CP21.260330.011 |
| **Emulator support** | x86 (64-bit), ARM (v8-A) |
| **Security patch level** | 2026-05-05 |
| **Google Play services** | 26.11.36 |

| Device | Download Link and SHA-256 Checksum |
|---|---|
| Pixel 6 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 Beta" data-action="download" data-label="oriole" data-modal-dialog-id="oriole_factory_zip">oriole_beta-cp31.260623.010-factory-14dd118c.zip</button> `14dd118c10d83554db008ec19121afccb273b4509cee959d65ada282a0ac5b36` |
| Pixel 6 Pro | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 Beta" data-action="download" data-label="raven" data-modal-dialog-id="raven_factory_zip">raven_beta-cp31.260623.010-factory-7750baa4.zip</button> `7750baa495ee8887baa0027edcc87d880d95df68a613e6cf6ea2e7599612b9f8` |
| Pixel 6a | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 Beta" data-action="download" data-label="bluejay" data-modal-dialog-id="bluejay_factory_zip">bluejay_beta-cp31.260623.010-factory-2756863a.zip</button> `2756863a8e5f1b803f33176513d6fe35d6c1b9cae82ed207faa121700811861f` |
| Pixel 7 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 Beta" data-action="download" data-label="panther" data-modal-dialog-id="panther_factory_zip">panther_beta-cp31.260623.010-factory-f751afb8.zip</button> `f751afb8027df7bcb5055478eb6c3d42ad943f9525ed28e24a28897b43ffa4ae` |
| Pixel 7 Pro | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 Beta" data-action="download" data-label="cheetah" data-modal-dialog-id="cheetah_factory_zip">cheetah_beta-cp31.260623.010-factory-bc7363a1.zip</button> `bc7363a1c0d9ef7b202ee9ad4617d985da8d26657885ad0c4353d74cc9a3cbae` |
| Pixel 7a | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 Beta" data-action="download" data-label="lynx" data-modal-dialog-id="lynx_factory_zip">lynx_beta-cp31.260623.010-factory-77a1ae60.zip</button> `77a1ae6075a33bc8438afbc63fe87c7a5c2ccbb6c1225db73ff1b173bdad6976` |
| Pixel Fold | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 Beta" data-action="download" data-label="felix" data-modal-dialog-id="felix_factory_zip">felix_beta-cp31.260623.010-factory-401c7136.zip</button> `401c713648b159a2f2bdd7bd3a1bb00c58012966fb7107c8a00243d119a48c60` |
| Pixel Tablet | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 Beta" data-action="download" data-label="tangorpro" data-modal-dialog-id="tangorpro_factory_zip">tangorpro_beta-cp31.260623.010-factory-8d540bd0.zip</button> `8d540bd0f6225eaa13d34ce91f72edc0c572ba99b463070300f944ba6f76a98c` |
| Pixel 8 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 Beta" data-action="download" data-label="shiba" data-modal-dialog-id="shiba_factory_zip">shiba_beta-cp31.260623.010-factory-6cf00c06.zip</button> `6cf00c06ca4ea8541f9a6e4f0025a6c5ff9f58226c0782cd6689246073b19285` |
| Pixel 8 Pro | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 Beta" data-action="download" data-label="husky" data-modal-dialog-id="husky_factory_zip">husky_beta-cp31.260623.010-factory-221f56a9.zip</button> `221f56a9df67bbc7bb8268efe4deb142c50f36237e79d4acda0a9d0609ee893b` |
| Pixel 8a | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 Beta" data-action="download" data-label="akita" data-modal-dialog-id="akita_factory_zip">akita_beta-cp31.260623.010-factory-e7c53e56.zip</button> `e7c53e56ac25861ce148e29f1c3d8ed07da75a2614824b991659de43f747a2be` |
| Pixel 9 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 Beta" data-action="download" data-label="tokay" data-modal-dialog-id="tokay_factory_zip">tokay_beta-cp31.260623.010-factory-b54666e3.zip</button> `b54666e36820af44c7b137cc1d2f8bcb9fbed581ac16d17f323121007576de62` |
| Pixel 9 Pro | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 Beta" data-action="download" data-label="caiman" data-modal-dialog-id="caiman_factory_zip">caiman_beta-cp31.260623.010-factory-9ba80c0a.zip</button> `9ba80c0a3f13d3687d396a2dbf9c4c95888b7b10172ba3c85366a04f797f374d` |
| Pixel 9 Pro XL | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 Beta" data-action="download" data-label="komodo" data-modal-dialog-id="komodo_factory_zip">komodo_beta-cp31.260623.010-factory-247fc418.zip</button> `247fc4185aaf790ec37916239a115f0d84ac6824c5ba408363a8552b59f65d51` |
| Pixel 9 Pro Fold | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 Beta" data-action="download" data-label="comet" data-modal-dialog-id="comet_factory_zip">comet_beta-cp31.260623.010-factory-d22bb6bd.zip</button> `d22bb6bd1ee52599113c42d174fbd4fa1577c89f030aa7129b6e65e0eba1da0b` |
| Pixel 9a | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 Beta" data-action="download" data-label="tegu" data-modal-dialog-id="tegu_factory_zip">tegu_beta-cp31.260623.010-factory-cefe52af.zip</button> `cefe52afa3562862bfb3fe368cb54662c5d882e203b3cc52d3120322db7d35b4` |
| Pixel 10 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 Beta" data-action="download" data-label="frankel" data-modal-dialog-id="frankel_factory_zip">frankel_beta-cp31.260623.010-factory-93db3e86.zip</button> `93db3e861503be6f7ef8658dc9e1f3b76c30c109c570bdc77f90db8c1020f1e9` |
| Pixel 10 Pro | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 Beta" data-action="download" data-label="blazer" data-modal-dialog-id="blazer_factory_zip">blazer_beta-cp31.260623.010-factory-5ed50581.zip</button> `5ed50581280badbabb65e871f93eeef1ff21b760c3ca270776e70b6298e411f6` |
| Pixel 10 Pro XL | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 Beta" data-action="download" data-label="mustang" data-modal-dialog-id="mustang_factory_zip">mustang_beta-cp31.260623.010-factory-3b8c98dc.zip</button> `3b8c98dcdd994131afe28d4e100c08f92db215fa697ede3eb7fa28e57f560cd9` |
| Pixel 10 Pro Fold | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 Beta" data-action="download" data-label="rango" data-modal-dialog-id="rango_factory_zip">rango_beta-cp31.260623.010-factory-39d4ef35.zip</button> `39d4ef355bcad1b41879d335a99a6bbfd1d86c827202feb816698b361d6b0b7b` |
| Pixel 10a | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 Beta" data-action="download" data-label="stallion" data-modal-dialog-id="stallion_factory_zip">stallion_beta-cp31.260623.010-factory-2ad635a0.zip</button> `2ad635a03c8e3419789f862e6087878c2f744f3d695a422dc3eadfc70e8b6e5d` |

## Return to a public build

You can either use the Android Flash Tool to [flash the factory image](https://flash.android.com/back-to-public), or obtain a factory spec system image from the [Factory Images for Nexus and Pixel Devices](https://developers.google.com/android/images) page and then manually flash it to the device.

> [!WARNING]
> **Warning:** Going back to a public build from a preview build (Developer Preview or Beta) requires a full device reset that removes all user data on the device. Make sure to [back up your data first](https://support.google.com/pixelphone/answer/7179901).

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/oriole_beta-cp31.260623.010-factory-14dd118c.zip)

*oriole_beta-cp31.260623.010-factory-14dd118c.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/raven_beta-cp31.260623.010-factory-7750baa4.zip)

*raven_beta-cp31.260623.010-factory-7750baa4.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/bluejay_beta-cp31.260623.010-factory-2756863a.zip)

*bluejay_beta-cp31.260623.010-factory-2756863a.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/panther_beta-cp31.260623.010-factory-f751afb8.zip)

*panther_beta-cp31.260623.010-factory-f751afb8.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/cheetah_beta-cp31.260623.010-factory-bc7363a1.zip)

*cheetah_beta-cp31.260623.010-factory-bc7363a1.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/lynx_beta-cp31.260623.010-factory-77a1ae60.zip)

*lynx_beta-cp31.260623.010-factory-77a1ae60.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/felix_beta-cp31.260623.010-factory-401c7136.zip)

*felix_beta-cp31.260623.010-factory-401c7136.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/tangorpro_beta-cp31.260623.010-factory-8d540bd0.zip)

*tangorpro_beta-cp31.260623.010-factory-8d540bd0.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/shiba_beta-cp31.260623.010-factory-6cf00c06.zip)

*shiba_beta-cp31.260623.010-factory-6cf00c06.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/husky_beta-cp31.260623.010-factory-221f56a9.zip)

*husky_beta-cp31.260623.010-factory-221f56a9.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/akita_beta-cp31.260623.010-factory-e7c53e56.zip)

*akita_beta-cp31.260623.010-factory-e7c53e56.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/tokay_beta-cp31.260623.010-factory-b54666e3.zip)

*tokay_beta-cp31.260623.010-factory-b54666e3.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/caiman_beta-cp31.260623.010-factory-9ba80c0a.zip)

*caiman_beta-cp31.260623.010-factory-9ba80c0a.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/komodo_beta-cp31.260623.010-factory-247fc418.zip)

*komodo_beta-cp31.260623.010-factory-247fc418.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/comet_beta-cp31.260623.010-factory-d22bb6bd.zip)

*comet_beta-cp31.260623.010-factory-d22bb6bd.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/tegu_beta-cp31.260623.010-factory-cefe52af.zip)

*tegu_beta-cp31.260623.010-factory-cefe52af.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/frankel_beta-cp31.260623.010-factory-93db3e86.zip)

*frankel_beta-cp31.260623.010-factory-93db3e86.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/blazer_beta-cp31.260623.010-factory-5ed50581.zip)

*blazer_beta-cp31.260623.010-factory-5ed50581.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/mustang_beta-cp31.260623.010-factory-3b8c98dc.zip)

*mustang_beta-cp31.260623.010-factory-3b8c98dc.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/rango_beta-cp31.260623.010-factory-39d4ef35.zip)

*rango_beta-cp31.260623.010-factory-39d4ef35.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/stallion_beta-cp31.260623.010-factory-2ad635a0.zip)

*stallion_beta-cp31.260623.010-factory-2ad635a0.zip*