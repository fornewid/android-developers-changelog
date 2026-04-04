---
title: https://developer.android.com/about/versions/15/download-ota
url: https://developer.android.com/about/versions/15/download-ota
source: md.txt
---

Building on the [initial release of Android 15](https://developer.android.com/about/versions/15), we continue to
update the platform with fixes and improvements that are then rolled out to
supported devices. These releases happen on a quarterly cadence through
*Quarterly Platform Releases* (QPRs), which are delivered both to AOSP and to
Google Pixel devices as part of *Feature Drops*.

Although these updates don't include app-impacting API changes, we provide
images of the latest QPR beta builds so you can test your app with these builds
as needed (for example, if there are upcoming features that might impact the
user experience of your app).

To find OTA images for already-released, stable versions of the platform, see
[Full OTA Images for Nexus and Pixel Devices](https://developers.google.com/android/ota).

Applying an OTA image can help you recover a device that received an OTA update
for an Android 15 QPR Beta build but wouldn't start up after the update was
installed. If you are trying to get Android 15 QPR1 on your device but you
aren't trying to recover from a failed OTA update, see [Get Android 15 QPR beta
builds](https://developer.android.com/about/versions/15/get-qpr) instead.

OTA images are available for the following Pixel devices:

- Pixel 6 and 6 Pro
- Pixel 7 and 7 Pro
- Pixel 7a
- Pixel Fold
- Pixel Tablet
- Pixel 8 and 8 Pro
- Pixel 8a
- Pixel 9, 9 Pro, 9 Pro XL, and 9 Pro Fold

After you've installed a beta build to your Pixel device, your device is
automatically enrolled in the [Android Beta for Pixel program](https://g.co/androidbeta) and offered
continuous over-the-air (OTA) updates to the latest beta builds (including QPRs)
until you choose to unenroll that device from the program. We also deliver
flashable images at each milestone, so you can choose the approach that works
best for your test environment.

Use the following links and instructions to update your supported device to the
latest build. See [Get Android 15 QPR beta builds](https://developer.android.com/about/versions/15/get-qpr) for other ways to get QPR1
for testing and development.

## Apply an OTA image

![](https://developer.android.com/static/images/lockups/android-stacked.svg)

Download an OTA device image from the following table and apply it by following
the [updating instructions](https://developers.google.com/android/ota#instructions) listed on [Full OTA Images for Nexus and Pixel
Devices](https://developers.google.com/android/ota).

You can choose to [return to the latest public build](https://developer.android.com/about/versions/15/download-ota#public) at any time.

<br />

> [!WARNING]
> **Warning:** Before applying an Android 15 OTA image, we strongly recommend that you [unlock the bootloader](https://source.android.com/docs/core/architecture/bootloader/locking_unlocking) on your device if possible. Unlocking the bootloader requires a full device reset that removes all user data on the device, so make sure to back up your data first.

### Device OTA Images

|---|---|
| **Release date** | January 21, 2025 |
| **Build** | BP11.241210.004 |
| **Emulator support** | x86 (64-bit), ARM (v8-A) |
| **Security patch level** | January 2025 |
| **Google Play services** | 24.45.32 |

| Device | Download Link and SHA-256 Checksum |
|---|---|
| Pixel 6 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 15 QPR1 Beta" data-action="download" data-label="oriole" data-modal-dialog-id="oriole_ota_zip">oriole_beta-ota-bp11.241210.004-14938039.zip</button> `149380398b0d09800bfa77aec7de061c03a3adf445f1f9b5a198bdaa6759a9a4` |
| Pixel 6 Pro | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 15 QPR1 Beta" data-action="download" data-label="raven" data-modal-dialog-id="raven_ota_zip">raven_beta-ota-bp11.241210.004-097b15ce.zip</button> `097b15cec3f40678393ff0d0a1462eddafab03468693dedc6c05f56266b617ac` |
| Pixel 7 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 15 QPR1 Beta" data-action="download" data-label="panther" data-modal-dialog-id="panther_ota_zip">panther_beta-ota-bp11.241210.004-90527d44.zip</button> `90527d44e69a76dbaba927caef35f3cbd10e8e836cf536500f5956ff881e9a6b` |
| Pixel 7 Pro | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 15 QPR1 Beta" data-action="download" data-label="cheetah" data-modal-dialog-id="cheetah_ota_zip">cheetah_beta-ota-bp11.241210.004-a175edd2.zip</button> `a175edd29997b22234342b5532871768164cc22616e8d78d33ccf41972f51e3a` |
| Pixel 7a | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 15 QPR1 Beta" data-action="download" data-label="lynx" data-modal-dialog-id="lynx_ota_zip">lynx_beta-ota-bp11.241210.004-ced7e588.zip</button> `ced7e588cbbb3d72409ef70ce7019a1a1c58cb7c2a9bc2aeebc771c22b3b85b4` |
| Pixel Fold | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 15 QPR1 Beta" data-action="download" data-label="felix" data-modal-dialog-id="felix_ota_zip">felix_beta-ota-bp11.241210.004-2543a128.zip</button> `2543a1287dc7ded0f320379878d1b6c78ee66ec413c3ad7492aa24e33f6f058b` |
| Pixel Tablet | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 15 QPR1 Beta" data-action="download" data-label="tangorpro" data-modal-dialog-id="tangorpro_ota_zip">tangorpro_beta-ota-bp11.241210.004-30ad49a0.zip</button> `30ad49a0ab7cc5a709849db4779f7871612e96af537d46d160b5d98a9936cd0e` |
| Pixel 8 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 15 QPR1 Beta" data-action="download" data-label="shiba" data-modal-dialog-id="shiba_ota_zip">shiba_beta-ota-bp11.241210.004-a1bcf4f0.zip</button> `a1bcf4f046166676abe556db517835510e80ed011c5fbdf09510a8f99cfaa75c` |
| Pixel 8 Pro | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 15 QPR1 Beta" data-action="download" data-label="husky" data-modal-dialog-id="husky_ota_zip">husky_beta-ota-bp11.241210.004-2880960c.zip</button> `2880960c52dfdd3708d681c06f1c05ac0d86aa09e40e811e3a3a7ef16302ba9f` |
| Pixel 8a | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 15 QPR1 Beta" data-action="download" data-label="akita" data-modal-dialog-id="akita_ota_zip">akita_beta-ota-bp11.241210.004-8912c2e9.zip</button> `8912c2e95bbe70077b8321d35650c587e4f67318afd0881872536f47d13dacbc` |
| Pixel 9 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 15 QPR1 Beta" data-action="download" data-label="tokay" data-modal-dialog-id="tokay_ota_zip">tokay_beta-ota-bp11.241210.004-59a15ca6.zip</button> `59a15ca6db3ef5e576ebcff0113434c44833bcc5d7f4ac091343514c6446660c` |
| Pixel 9 Pro | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 15 QPR1 Beta" data-action="download" data-label="caiman" data-modal-dialog-id="caiman_ota_zip">caiman_beta-ota-bp11.241210.004-2bf3bbcf.zip</button> `2bf3bbcfc6c3294d55769a0875b412762b987f2e43022264e4d9e6abec473238` |
| Pixel 9 Pro XL | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 15 QPR1 Beta" data-action="download" data-label="komodo" data-modal-dialog-id="komodo_ota_zip">komodo_beta-ota-bp11.241210.004-d806fbe7.zip</button> `d806fbe7b2f01da404d67d6ad8dc6488ca587792b5b31530cd49a7d3bbbdfc81` |
| Pixel 9 Pro Fold | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 15 QPR1 Beta" data-action="download" data-label="comet" data-modal-dialog-id="comet_ota_zip">comet_beta-ota-bp11.241210.004-dc44cdf1.zip</button> `dc44cdf1bf1de5eac8b8ff7919c37cb0ecb134b57e85a4a0b5faca48e18ad4aa` |

## Return to a public build

You can either use the Android Flash Tool to
[flash the factory image](https://flash.android.com/back-to-public), or obtain a factory spec system
image from the [Factory Images for Nexus and Pixel Devices](https://developers.google.com/android/images)
page and then manually flash it to the device.

> [!WARNING]
> **Warning:** Going back to a public build from a preview build (Developer Preview or Beta) requires a full device reset that removes all user data on the device. Make sure to [back up your data first](https://support.google.com/pixelphone/answer/7179901).

## Download Android 15 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 15 OTA system image </button> [Download Android 15 OTA system image](https://dl.google.com/developers/android/vic/images/ota/oriole_beta-ota-bp11.241210.004-14938039.zip)

*oriole_beta-ota-bp11.241210.004-14938039.zip*

## Download Android 15 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 15 OTA system image </button> [Download Android 15 OTA system image](https://dl.google.com/developers/android/vic/images/ota/raven_beta-ota-bp11.241210.004-097b15ce.zip)

*raven_beta-ota-bp11.241210.004-097b15ce.zip*

## Download Android 15 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 15 OTA system image </button> [Download Android 15 OTA system image](https://dl.google.com/developers/android/vic/images/ota/panther_beta-ota-bp11.241210.004-90527d44.zip)

*panther_beta-ota-bp11.241210.004-90527d44.zip*

## Download Android 15 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 15 OTA system image </button> [Download Android 15 OTA system image](https://dl.google.com/developers/android/vic/images/ota/cheetah_beta-ota-bp11.241210.004-a175edd2.zip)

*cheetah_beta-ota-bp11.241210.004-a175edd2.zip*

## Download Android 15 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 15 OTA system image </button> [Download Android 15 OTA system image](https://dl.google.com/developers/android/vic/images/ota/lynx_beta-ota-bp11.241210.004-ced7e588.zip)

*lynx_beta-ota-bp11.241210.004-ced7e588.zip*

## Download Android 15 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 15 OTA system image </button> [Download Android 15 OTA system image](https://dl.google.com/developers/android/vic/images/ota/felix_beta-ota-bp11.241210.004-2543a128.zip)

*felix_beta-ota-bp11.241210.004-2543a128.zip*

## Download Android 15 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 15 OTA system image </button> [Download Android 15 OTA system image](https://dl.google.com/developers/android/vic/images/ota/tangorpro_beta-ota-bp11.241210.004-30ad49a0.zip)

*tangorpro_beta-ota-bp11.241210.004-30ad49a0.zip*

## Download Android 15 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 15 OTA system image </button> [Download Android 15 OTA system image](https://dl.google.com/developers/android/vic/images/ota/shiba_beta-ota-bp11.241210.004-a1bcf4f0.zip)

*shiba_beta-ota-bp11.241210.004-a1bcf4f0.zip*

## Download Android 15 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 15 OTA system image </button> [Download Android 15 OTA system image](https://dl.google.com/developers/android/vic/images/ota/husky_beta-ota-bp11.241210.004-2880960c.zip)

*husky_beta-ota-bp11.241210.004-2880960c.zip*

## Download Android 15 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 15 OTA system image </button> [Download Android 15 OTA system image](https://dl.google.com/developers/android/vic/images/ota/akita_beta-ota-bp11.241210.004-8912c2e9.zip)

*akita_beta-ota-bp11.241210.004-8912c2e9.zip*

## Download Android 15 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 15 OTA system image </button> [Download Android 15 OTA system image](https://dl.google.com/developers/android/vic/images/ota/tokay_beta-ota-bp11.241210.004-59a15ca6.zip)

*tokay_beta-ota-bp11.241210.004-59a15ca6.zip*

## Download Android 15 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 15 OTA system image </button> [Download Android 15 OTA system image](https://dl.google.com/developers/android/vic/images/ota/caiman_beta-ota-bp11.241210.004-2bf3bbcf.zip)

*caiman_beta-ota-bp11.241210.004-2bf3bbcf.zip*

## Download Android 15 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 15 OTA system image </button> [Download Android 15 OTA system image](https://dl.google.com/developers/android/vic/images/ota/komodo_beta-ota-bp11.241210.004-d806fbe7.zip)

*komodo_beta-ota-bp11.241210.004-d806fbe7.zip*

## Download Android 15 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 15 OTA system image </button> [Download Android 15 OTA system image](https://dl.google.com/developers/android/vic/images/ota/comet_beta-ota-bp11.241210.004-dc44cdf1.zip)

*comet_beta-ota-bp11.241210.004-dc44cdf1.zip*