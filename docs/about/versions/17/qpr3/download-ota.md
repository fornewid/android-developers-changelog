---
title: https://developer.android.com/about/versions/17/qpr3/download-ota
url: https://developer.android.com/about/versions/17/qpr3/download-ota
source: md.txt
---

Applying an OTA image can help you recover a device that received an OTA update
for an Android 17 Beta build but wouldn't start up
after the update was installed. If you are trying to get Android 17 on your
device but you aren't trying to recover from a failed OTA update, see [Get
Android 17](https://developer.android.com/about/versions/17/get) instead.
Building on the [initial release of Android 17](https://developer.android.com/about/versions/17), we continue to update the platform with fixes and improvements that are then rolled out to supported devices. These releases happen on a quarterly cadence through *Quarterly Platform Releases* (QPRs), which are delivered both to AOSP and to Google Pixel devices as part of *Feature Drops* .

<br />

Although QPR3 doesn't include API changes, we provide images of the latest QPR
beta builds so you can test your app with these releases as needed to help make
sure that these updates work as expected for all of your users.

To find OTA images for already-released, stable versions of the platform, see
[Full OTA Images for Nexus and Pixel Devices](https://developers.google.com/android/ota).

Applying an OTA image can help you recover a device that received an OTA update
for an Android 17 QPR beta build but wouldn't start up after the update was
installed. If you are trying to get Android 17 QPR1 on your device but
you aren't trying to recover from a failed OTA update, see [Get Android 17 QPR
beta builds](https://developer.android.com/about/versions/17/qpr3/get) instead.


OTA images are available for the following Pixel devices:

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
- Pixel 11
- Pixel 11 Pro
- Pixel 11 Pro XL
- Pixel 11 Pro Fold

After you've installed a beta build to your Pixel device, your device is automatically enrolled in the [Android Beta for Pixel program](https://g.co/androidbeta) and offered continuous over-the-air (OTA) updates to the latest beta builds (including QPRs) until you choose to unenroll that device from the program.

We also deliver flashable images at each milestone, so you can choose the
approach that works best for your test environment.

Use the following links and instructions to update your supported device to the
latest build. See [Get Android 17](https://developer.android.com/about/versions/17/get) for
other ways to get Android 17 for testing and development.

## Apply an OTA image

![](https://developer.android.com/static/images/lockups/android-stacked.svg)

Download an OTA device image from the following table and apply it by following
the [updating instructions](https://developers.google.com/android/ota#instructions) listed on [Full OTA Images for Nexus and Pixel
Devices](https://developers.google.com/android/ota).

You can choose to [return to the latest public build](https://developer.android.com/about/versions/17/qpr3/download-ota#public) at any time.

<br />

> [!WARNING]
> **Warning:** Before applying an Android 17 OTA image, we strongly recommend that you [unlock the bootloader](https://source.android.com/docs/core/architecture/bootloader/locking_unlocking) on your device if possible. Unlocking the bootloader requires a full device reset that removes all user data on the device, so make sure to back up your data first.

### Device OTA Images

|---|---|
| **Release date** | October 29, 2026 |
| **Builds** | DP11.261016.003 DP11.261016.004 |
| **Emulator support** | x86 (64-bit), ARM (v8-A) |
| **Security patch level** | 2026-10-05 |
| **Google Play services** | 26.36.33 |

| Device | Download Link and SHA-256 Checksum |
|---|---|
| Pixel 6a | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 QPR1 Beta" data-action="download" data-label="bluejay" data-modal-dialog-id="bluejay_ota_zip">bluejay_beta-ota-dp11.261016.003-ae184fef.zip</button> `ae184fef76ff547808bc9678f5f6d8cffa89e53bed41152b5e90f7d9cf58d962` |
| Pixel 7 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 QPR1 Beta" data-action="download" data-label="panther" data-modal-dialog-id="panther_ota_zip">panther_beta-ota-dp11.261016.003-cb375e1b.zip</button> `cb375e1b55b5120bf7b9673a61e5e6e934e12c46d368e9fe2cd81f49804e78b7` |
| Pixel 7 Pro | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 QPR1 Beta" data-action="download" data-label="cheetah" data-modal-dialog-id="cheetah_ota_zip">cheetah_beta-ota-dp11.261016.003-e2b1d99e.zip</button> `e2b1d99e7597338b95cf2b2cd0b78882dc29ed663b4dbde20d68a29fbed7409d` |
| Pixel 7a | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 QPR1 Beta" data-action="download" data-label="lynx" data-modal-dialog-id="lynx_ota_zip">lynx_beta-ota-dp11.261016.003-b8fe2918.zip</button> `b8fe2918720130e7b4876756a5e1ade67b1c4e142b8154ca403f857bf98a3010` |
| Pixel Fold | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 QPR1 Beta" data-action="download" data-label="felix" data-modal-dialog-id="felix_ota_zip">felix_beta-ota-dp11.261016.003-f6048c9e.zip</button> `f6048c9efb6163b5b57d9817865add46a030490e19617cc7cb57049d8a07f01e` |
| Pixel Tablet | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 QPR1 Beta" data-action="download" data-label="tangorpro" data-modal-dialog-id="tangorpro_ota_zip">tangorpro_beta-ota-dp11.261016.003-59e4b157.zip</button> `59e4b157a9ca69bd6afdd5db357d5928a69747864c664b2ace9782967eab1fed` |
| Pixel 8 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 QPR1 Beta" data-action="download" data-label="shiba" data-modal-dialog-id="shiba_ota_zip">shiba_beta-ota-dp11.261016.003-c784467a.zip</button> `c784467a71d688704b80f9744c0ccf308d0395bac22a852f77116694e81ca23b` |
| Pixel 8 Pro | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 QPR1 Beta" data-action="download" data-label="husky" data-modal-dialog-id="husky_ota_zip">husky_beta-ota-dp11.261016.003-255a8d82.zip</button> `255a8d828def79c2223179a301e06caaa86c84ca959982a2eb580a9912634a24` |
| Pixel 8a | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 QPR1 Beta" data-action="download" data-label="akita" data-modal-dialog-id="akita_ota_zip">akita_beta-ota-dp11.261016.003-f1f4e20a.zip</button> `f1f4e20ae1809f1ec8b92a115418b5f1bd5b5e81084b238b75d0b841261767ec` |
| Pixel 9 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 QPR1 Beta" data-action="download" data-label="tokay" data-modal-dialog-id="tokay_ota_zip">tokay_beta-ota-dp11.261016.003-f99f2f21.zip</button> `f99f2f210ec47cd718b2fa862f74e6ea5afa98b77c53d451e3cd361540add3fb` |
| Pixel 9 Pro | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 QPR1 Beta" data-action="download" data-label="caiman" data-modal-dialog-id="caiman_ota_zip">caiman_beta-ota-dp11.261016.003-203ed262.zip</button> `203ed262f97c95496443bfbdab323d21abb52c290db40c9f9f5ab75e9a4df57b` |
| Pixel 9 Pro XL | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 QPR1 Beta" data-action="download" data-label="komodo" data-modal-dialog-id="komodo_ota_zip">komodo_beta-ota-dp11.261016.003-a4a5195f.zip</button> `a4a5195fde23db78b7b96c4d1bd95589bd96761172f90e75a08aeac5211854a8` |
| Pixel 9 Pro Fold | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 QPR1 Beta" data-action="download" data-label="comet" data-modal-dialog-id="comet_ota_zip">comet_beta-ota-dp11.261016.003-95784964.zip</button> `957849648827fbcbb65c611f5f161a5aba846022190ab4727f21bd5b712aa1c9` |
| Pixel 9a | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 QPR1 Beta" data-action="download" data-label="tegu" data-modal-dialog-id="tegu_ota_zip">tegu_beta-ota-dp11.261016.003-5d0fde5f.zip</button> `5d0fde5f6be5e722b4c858c8084818db4fd84d6000852f136449f9806ed41a13` |
| Pixel 10 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 QPR1 Beta" data-action="download" data-label="frankel" data-modal-dialog-id="frankel_ota_zip">frankel_beta-ota-dp11.261016.003-d3851177.zip</button> `d38511779668bbca181b7639b73028bc580c55caad4afc2f0cdb982347442869` |
| Pixel 10 Pro | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 QPR1 Beta" data-action="download" data-label="blazer" data-modal-dialog-id="blazer_ota_zip">blazer_beta-ota-dp11.261016.003-68ca688c.zip</button> `68ca688c3cfc119461b9615ce48e16db0ff2af80180a7077af7294edb98ecd35` |
| Pixel 10 Pro XL | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 QPR1 Beta" data-action="download" data-label="mustang" data-modal-dialog-id="mustang_ota_zip">mustang_beta-ota-dp11.261016.003-89804d1d.zip</button> `89804d1dd10462970362ea4526d3c641398399d4737628281f69b5e3ce27acb6` |
| Pixel 10 Pro Fold | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 QPR1 Beta" data-action="download" data-label="rango" data-modal-dialog-id="rango_ota_zip">rango_beta-ota-dp11.261016.003-d0414294.zip</button> `d04142941ac70b80952b3fdb6f17eeb1c812af078d919e515b2620d99aa7f548` |
| Pixel 10a | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 QPR1 Beta" data-action="download" data-label="stallion" data-modal-dialog-id="stallion_ota_zip">stallion_beta-ota-dp11.261016.003-9ac76594.zip</button> `9ac765948e484bc29168569d28e5e9f6915f93f84cee656c98f9a6601a193b52` |
| Pixel 11 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 QPR1 Beta" data-action="download" data-label="cubs" data-modal-dialog-id="cubs_ota_zip">cubs_beta-ota-dp11.261016.004-6b241c75.zip</button> `6b241c75671cbe9172f17024538ddff0146f17f1363a4c87877af61c223eb0d2` |
| Pixel 11 Pro | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 QPR1 Beta" data-action="download" data-label="grizzly" data-modal-dialog-id="grizzly_ota_zip">grizzly_beta-ota-dp11.261016.004-392214a8.zip</button> `392214a8cbc120e1e4767b98eda21d89ed48a6cd8d75e8d3ce2edfc9549834b9` |
| Pixel 11 Pro XL | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 QPR1 Beta" data-action="download" data-label="kodiak" data-modal-dialog-id="kodiak_ota_zip">kodiak_beta-ota-dp11.261016.004-82acb721.zip</button> `82acb721f690926b72c833529ea6767cdb45c346cf4923a0992889434e7cad90` |
| Pixel 11 Pro Fold | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 QPR1 Beta" data-action="download" data-label="yogi" data-modal-dialog-id="yogi_ota_zip">yogi_beta-ota-dp11.261016.004-f9c4b2f9.zip</button> `f9c4b2f99a55bc3f42fe14e8fb7415a82563a9bba28eeee6ef266212059bfb77` |

## Return to a public build

You can either use the Android Flash Tool to
[flash the factory image](https://flash.android.com/back-to-public), or obtain a factory spec system
image from the [Factory Images for Nexus and Pixel Devices](https://developers.google.com/android/images)
page and then manually flash it to the device.

> [!WARNING]
> **Warning:** Going back to a public build from a preview build (Developer Preview or Beta) requires a full device reset that removes all user data on the device. Make sure to [back up your data first](https://support.google.com/pixelphone/answer/7179901).

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 OTA system image </button> [Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/bluejay_beta-ota-dp11.261016.003-ae184fef.zip)

*bluejay_beta-ota-dp11.261016.003-ae184fef.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 OTA system image </button> [Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/panther_beta-ota-dp11.261016.003-cb375e1b.zip)

*panther_beta-ota-dp11.261016.003-cb375e1b.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 OTA system image </button> [Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/cheetah_beta-ota-dp11.261016.003-e2b1d99e.zip)

*cheetah_beta-ota-dp11.261016.003-e2b1d99e.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 OTA system image </button> [Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/lynx_beta-ota-dp11.261016.003-b8fe2918.zip)

*lynx_beta-ota-dp11.261016.003-b8fe2918.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 OTA system image </button> [Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/felix_beta-ota-dp11.261016.003-f6048c9e.zip)

*felix_beta-ota-dp11.261016.003-f6048c9e.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 OTA system image </button> [Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/tangorpro_beta-ota-dp11.261016.003-59e4b157.zip)

*tangorpro_beta-ota-dp11.261016.003-59e4b157.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 OTA system image </button> [Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/shiba_beta-ota-dp11.261016.003-c784467a.zip)

*shiba_beta-ota-dp11.261016.003-c784467a.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 OTA system image </button> [Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/husky_beta-ota-dp11.261016.003-255a8d82.zip)

*husky_beta-ota-dp11.261016.003-255a8d82.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 OTA system image </button> [Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/akita_beta-ota-dp11.261016.003-f1f4e20a.zip)

*akita_beta-ota-dp11.261016.003-f1f4e20a.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 OTA system image </button> [Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/tokay_beta-ota-dp11.261016.003-f99f2f21.zip)

*tokay_beta-ota-dp11.261016.003-f99f2f21.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 OTA system image </button> [Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/caiman_beta-ota-dp11.261016.003-203ed262.zip)

*caiman_beta-ota-dp11.261016.003-203ed262.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 OTA system image </button> [Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/komodo_beta-ota-dp11.261016.003-a4a5195f.zip)

*komodo_beta-ota-dp11.261016.003-a4a5195f.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 OTA system image </button> [Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/comet_beta-ota-dp11.261016.003-95784964.zip)

*comet_beta-ota-dp11.261016.003-95784964.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 OTA system image </button> [Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/tegu_beta-ota-dp11.261016.003-5d0fde5f.zip)

*tegu_beta-ota-dp11.261016.003-5d0fde5f.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 OTA system image </button> [Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/frankel_beta-ota-dp11.261016.003-d3851177.zip)

*frankel_beta-ota-dp11.261016.003-d3851177.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 OTA system image </button> [Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/blazer_beta-ota-dp11.261016.003-68ca688c.zip)

*blazer_beta-ota-dp11.261016.003-68ca688c.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 OTA system image </button> [Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/mustang_beta-ota-dp11.261016.003-89804d1d.zip)

*mustang_beta-ota-dp11.261016.003-89804d1d.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 OTA system image </button> [Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/rango_beta-ota-dp11.261016.003-d0414294.zip)

*rango_beta-ota-dp11.261016.003-d0414294.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 OTA system image </button> [Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/stallion_beta-ota-dp11.261016.003-9ac76594.zip)

*stallion_beta-ota-dp11.261016.003-9ac76594.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 OTA system image </button> [Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/cubs_beta-ota-dp11.261016.004-6b241c75.zip)

*cubs_beta-ota-dp11.261016.004-6b241c75.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 OTA system image </button> [Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/grizzly_beta-ota-dp11.261016.004-392214a8.zip)

*grizzly_beta-ota-dp11.261016.004-392214a8.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 OTA system image </button> [Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/kodiak_beta-ota-dp11.261016.004-82acb721.zip)

*kodiak_beta-ota-dp11.261016.004-82acb721.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 OTA system image </button> [Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/yogi_beta-ota-dp11.261016.004-f9c4b2f9.zip)

*yogi_beta-ota-dp11.261016.004-f9c4b2f9.zip*