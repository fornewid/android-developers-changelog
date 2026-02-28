---
title: https://developer.android.com/about/versions/16/qpr2/download-ota
url: https://developer.android.com/about/versions/16/qpr2/download-ota
source: md.txt
---

Applying an OTA image can help you recover a device that received an OTA update
for an Android 16 Beta build but wouldn't start
up after the update was installed. If you are trying to get Android 16 on your
device but you aren't trying to recover from a failed OTA update, see [Get
Android 16](https://developer.android.com/about/versions/16/qpr2/get) instead.

OTA images are available for the following Pixel devices:

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
- Pixel 10, 10 Pro, 10 Pro XL, and 10 Pro Fold

After you've installed a beta build to your Pixel device, your device is automatically enrolled in the [Android Beta for Pixel program](https://g.co/androidbeta) and offered continuous over-the-air (OTA) updates to the latest beta builds (including QPRs) until you choose to unenroll that device from the program.

We also deliver flashable images at each milestone, so you can choose the
approach that works best for your test environment.

Use the following links and instructions to update your supported device to the
latest build. See [Get Android 16 QPR2](https://developer.android.com/about/versions/16/qpr2/get) for
other ways to get Android 16 QPR2 for testing and development.

## Apply an OTA image

![](https://developer.android.com/static/images/lockups/android-stacked.svg)

Download an OTA device image from the following table and apply it by following
the [updating instructions](https://developers.google.com/android/ota#instructions) listed on [Full OTA Images for Nexus and Pixel
Devices](https://developers.google.com/android/ota).

You can choose to [return to the latest public build](https://developer.android.com/about/versions/16/qpr2/download-ota#public) at any time.

<br />

> [!WARNING]
> **Warning:** Before applying an Android 16 QPR2 OTA image, we strongly recommend that you [unlock the bootloader](https://source.android.com/docs/core/architecture/bootloader/locking_unlocking) on your device if possible. Unlocking the bootloader requires a full device reset that removes all user data on the device, so make sure to back up your data first.

### Device OTA Images

|---|---|
| **Release date** | November 10, 2025 |
| **Builds** | BP41.250916.015.A1 |
| **Emulator support** | TBA |
| **Security patch level** | 2025-10-05 |
| **Google Play services** | 25.34.34 |
| **API diff** | - [QPR2 Beta 2 → API 36.1](https://developer.android.com/sdk/api_diff/36.1-incr/changes) - [API 36 → API 36.1](https://developer.android.com/sdk/api_diff/36.1/changes) |

| Device | Download Link and SHA-256 Checksum |
|---|---|
| Pixel 6 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="oriole" data-modal-dialog-id="oriole_ota_zip">oriole_beta-ota-bp41.250916.015-c409c359.zip</button> `c409c359ee2345819e129bee7ec49fff6ff4a64655e6a2f8266d523ee2216391` |
| Pixel 6 Pro | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="raven" data-modal-dialog-id="raven_ota_zip">raven_beta-ota-bp41.250916.015-a71eea47.zip</button> `a71eea4782a11b5bdb633d23124c377c01c5388606e05f79e19ec746c9b41113` |
| Pixel 6a | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="bluejay" data-modal-dialog-id="bluejay_ota_zip">bluejay_beta-ota-bp41.250916.015-532d914f.zip</button> `532d914f43431c7c77fe7e4c1bb7af3827de5eb74caf5197074f04c1db8e19c1` |
| Pixel 7 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="panther" data-modal-dialog-id="panther_ota_zip">panther_beta-ota-bp41.250916.015.a1-ba27c821.zip</button> `ba27c82181a3922e2098705ecdab7eb560cc54e53368194531ad16423dcd025d` |
| Pixel 7 Pro | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="cheetah" data-modal-dialog-id="cheetah_ota_zip">cheetah_beta-ota-bp41.250916.015.a1-04f8bc57.zip</button> `04f8bc573f0b3ed6a27276a1d3b93dbcfcb28ade8139e265f024be63c88c8a50` |
| Pixel 7a | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="lynx" data-modal-dialog-id="lynx_ota_zip">lynx_beta-ota-bp41.250916.015.a1-487b4dab.zip</button> `487b4dabde53339dc88431d1cf24b44e0ca8bd2a7ecb554f39d4a9b47e19b044` |
| Pixel Fold | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="felix" data-modal-dialog-id="felix_ota_zip">felix_beta-ota-bp41.250916.015.a1-0a583199.zip</button> `0a583199614966e2aba196f5b196fb32460405ed7ab1e53261df6e90cafc053e` |
| Pixel Tablet | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="tangorpro" data-modal-dialog-id="tangorpro_ota_zip">tangorpro_beta-ota-bp41.250916.015.a1-6a94ca54.zip</button> `6a94ca542438017aa21f9f231dc4a08438dbe8878d1642b5afa9f830a43fca99` |
| Pixel 8 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="shiba" data-modal-dialog-id="shiba_ota_zip">shiba_beta-ota-bp41.250916.015.a1-eb90aceb.zip</button> `eb90acebce38b016a3bc7636b7a7f373f930c4543cf6047b53c31ccecd817595` |
| Pixel 8 Pro | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="husky" data-modal-dialog-id="husky_ota_zip">husky_beta-ota-bp41.250916.015.a1-414569ee.zip</button> `414569eead50ac353c0a5e87ad07a7a89765aab76edc1f3d4f0d0de9fcf2f916` |
| Pixel 8a | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="akita" data-modal-dialog-id="akita_ota_zip">akita_beta-ota-bp41.250916.015.a1-b395ee87.zip</button> `b395ee87598f1dabfdf5ac7c07c2307fbeb76593d72d79bec5cb84f7d93f439d` |
| Pixel 9 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="tokay" data-modal-dialog-id="tokay_ota_zip">tokay_beta-ota-bp41.250916.015.a1-b1148e21.zip</button> `b1148e21b31105c74eb907b8fb5d8b82603c241556bd27f5526bde769e18ff01` |
| Pixel 9 Pro | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="caiman" data-modal-dialog-id="caiman_ota_zip">caiman_beta-ota-bp41.250916.015.a1-13525131.zip</button> `13525131087d0de62a08fbb987430de4b174e981f6152d3b48d12d515a4e4571` |
| Pixel 9 Pro XL | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="komodo" data-modal-dialog-id="komodo_ota_zip">komodo_beta-ota-bp41.250916.015.a1-2e691537.zip</button> `2e691537f5e108d17d98bc4e734292fa1f70e4a4a6006941ac68dc88d71d5eb1` |
| Pixel 9 Pro Fold | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="comet" data-modal-dialog-id="comet_ota_zip">comet_beta-ota-bp41.250916.015.a1-aeb0389b.zip</button> `aeb0389b20b52e4078225f77f46e651833d7d6cee6be4620a3c5d5603f8e70bb` |
| Pixel 9a | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="tegu" data-modal-dialog-id="tegu_ota_zip">tegu_beta-ota-bp41.250916.015.a1-13ada2ed.zip</button> `13ada2ed2eaaf7341f84ac56ca3911122466fa898f9ffe71d5cb34134335a239` |
| Pixel 10 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="frankel" data-modal-dialog-id="frankel_ota_zip">frankel_beta-ota-bp41.250916.015.a1-44d384b0.zip</button> `44d384b09842aa81c0ca5008cbbe93a746a6e303ec545fabcd42fc54f6bd8556` |
| Pixel 10 Pro | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="blazer" data-modal-dialog-id="blazer_ota_zip">blazer_beta-ota-bp41.250916.015.a1-c9787129.zip</button> `c97871297861af9b8aca1b5233d9b6db106accb109b7a77797517c048ede5871` |
| Pixel 10 Pro XL | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="mustang" data-modal-dialog-id="mustang_ota_zip">mustang_beta-ota-bp41.250916.015.a1-512086bc.zip</button> `512086bc9029c13aeb7126e818a25ca724e867f3693726e28ccc420ef18578bd` |
| Pixel 10 Pro Fold | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="rango" data-modal-dialog-id="rango_ota_zip">rango_beta-ota-bp41.250916.015.a1-114579f4.zip</button> `114579f4cfd80a481e3ee8f185742c3e9439a312f2b096ea6bf1b25d0ba6516f` |

## Return to a public build

You can either use the Android Flash Tool to
[flash the factory image](https://flash.android.com/back-to-public), or obtain a factory spec system
image from the [Factory Images for Nexus and Pixel Devices](https://developers.google.com/android/images)
page and then manually flash it to the device.

> [!WARNING]
> **Warning:** Going back to a public build from a preview build (Developer Preview or Beta) requires a full device reset that removes all user data on the device. Make sure to [back up your data first](https://support.google.com/pixelphone/answer/7179901).

## Download Android 16 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 OTA system image </button> [Download Android 16 OTA system image](https://dl.google.com/developers/android/baklava/images/ota/oriole_beta-ota-bp41.250916.015-c409c359.zip)

*oriole_beta-ota-bp41.250916.015-c409c359.zip*

## Download Android 16 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 OTA system image </button> [Download Android 16 OTA system image](https://dl.google.com/developers/android/baklava/images/ota/raven_beta-ota-bp41.250916.015-a71eea47.zip)

*raven_beta-ota-bp41.250916.015-a71eea47.zip*

## Download Android 16 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 OTA system image </button> [Download Android 16 OTA system image](https://dl.google.com/developers/android/baklava/images/ota/bluejay_beta-ota-bp41.250916.015-532d914f.zip)

*bluejay_beta-ota-bp41.250916.015-532d914f.zip*

## Download Android 16 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 OTA system image </button> [Download Android 16 OTA system image](https://dl.google.com/developers/android/baklava/images/ota/panther_beta-ota-bp41.250916.015.a1-ba27c821.zip)

*panther_beta-ota-bp41.250916.015.a1-ba27c821.zip*

## Download Android 16 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 OTA system image </button> [Download Android 16 OTA system image](https://dl.google.com/developers/android/baklava/images/ota/cheetah_beta-ota-bp41.250916.015.a1-04f8bc57.zip)

*cheetah_beta-ota-bp41.250916.015.a1-04f8bc57.zip*

## Download Android 16 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 OTA system image </button> [Download Android 16 OTA system image](https://dl.google.com/developers/android/baklava/images/ota/lynx_beta-ota-bp41.250916.015.a1-487b4dab.zip)

*lynx_beta-ota-bp41.250916.015.a1-487b4dab.zip*

## Download Android 16 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 OTA system image </button> [Download Android 16 OTA system image](https://dl.google.com/developers/android/baklava/images/ota/felix_beta-ota-bp41.250916.015.a1-0a583199.zip)

*felix_beta-ota-bp41.250916.015.a1-0a583199.zip*

## Download Android 16 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 OTA system image </button> [Download Android 16 OTA system image](https://dl.google.com/developers/android/baklava/images/ota/tangorpro_beta-ota-bp41.250916.015.a1-6a94ca54.zip)

*tangorpro_beta-ota-bp41.250916.015.a1-6a94ca54.zip*

## Download Android 16 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 OTA system image </button> [Download Android 16 OTA system image](https://dl.google.com/developers/android/baklava/images/ota/shiba_beta-ota-bp41.250916.015.a1-eb90aceb.zip)

*shiba_beta-ota-bp41.250916.015.a1-eb90aceb.zip*

## Download Android 16 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 OTA system image </button> [Download Android 16 OTA system image](https://dl.google.com/developers/android/baklava/images/ota/husky_beta-ota-bp41.250916.015.a1-414569ee.zip)

*husky_beta-ota-bp41.250916.015.a1-414569ee.zip*

## Download Android 16 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 OTA system image </button> [Download Android 16 OTA system image](https://dl.google.com/developers/android/baklava/images/ota/akita_beta-ota-bp41.250916.015.a1-b395ee87.zip)

*akita_beta-ota-bp41.250916.015.a1-b395ee87.zip*

## Download Android 16 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 OTA system image </button> [Download Android 16 OTA system image](https://dl.google.com/developers/android/baklava/images/ota/tokay_beta-ota-bp41.250916.015.a1-b1148e21.zip)

*tokay_beta-ota-bp41.250916.015.a1-b1148e21.zip*

## Download Android 16 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 OTA system image </button> [Download Android 16 OTA system image](https://dl.google.com/developers/android/baklava/images/ota/caiman_beta-ota-bp41.250916.015.a1-13525131.zip)

*caiman_beta-ota-bp41.250916.015.a1-13525131.zip*

## Download Android 16 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 OTA system image </button> [Download Android 16 OTA system image](https://dl.google.com/developers/android/baklava/images/ota/komodo_beta-ota-bp41.250916.015.a1-2e691537.zip)

*komodo_beta-ota-bp41.250916.015.a1-2e691537.zip*

## Download Android 16 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 OTA system image </button> [Download Android 16 OTA system image](https://dl.google.com/developers/android/baklava/images/ota/comet_beta-ota-bp41.250916.015.a1-aeb0389b.zip)

*comet_beta-ota-bp41.250916.015.a1-aeb0389b.zip*

## Download Android 16 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 OTA system image </button> [Download Android 16 OTA system image](https://dl.google.com/developers/android/baklava/images/ota/tegu_beta-ota-bp41.250916.015.a1-13ada2ed.zip)

*tegu_beta-ota-bp41.250916.015.a1-13ada2ed.zip*

## Download Android 16 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 OTA system image </button> [Download Android 16 OTA system image](https://dl.google.com/developers/android/baklava/images/ota/frankel_beta-ota-bp41.250916.015.a1-44d384b0.zip)

*frankel_beta-ota-bp41.250916.015.a1-44d384b0.zip*

## Download Android 16 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 OTA system image </button> [Download Android 16 OTA system image](https://dl.google.com/developers/android/baklava/images/ota/blazer_beta-ota-bp41.250916.015.a1-c9787129.zip)

*blazer_beta-ota-bp41.250916.015.a1-c9787129.zip*

## Download Android 16 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 OTA system image </button> [Download Android 16 OTA system image](https://dl.google.com/developers/android/baklava/images/ota/mustang_beta-ota-bp41.250916.015.a1-512086bc.zip)

*mustang_beta-ota-bp41.250916.015.a1-512086bc.zip*

## Download Android 16 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 OTA system image </button> [Download Android 16 OTA system image](https://dl.google.com/developers/android/baklava/images/ota/rango_beta-ota-bp41.250916.015.a1-114579f4.zip)

*rango_beta-ota-bp41.250916.015.a1-114579f4.zip*