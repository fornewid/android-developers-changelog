---
title: https://developer.android.com/about/versions/17/qpr2/download
url: https://developer.android.com/about/versions/17/qpr2/download
source: md.txt
---

If you are a developer with a supported Google Pixel device, you can manually
update that device to the latest build for testing and development. Flashing a
factory image requires a full device reset, so make sure to [back up your
data](https://support.google.com/pixelphone/answer/7179901) first. Builds are available for the following Pixel devices:

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

Use the following links and instructions to update your supported device to the
latest build. See [Get
Android 17 QPR beta builds](https://developer.android.com/about/versions/17/get-qpr) for other ways to get
QPR1 for testing and development.

> [!WARNING]
> **Warning:** Flashing to a beta build from a production build---or going back to a production build from a beta build---requires a full device reset that removes all user data on the device. Make sure to [back up the data from your
> Pixel](https://support.google.com/pixelphone/answer/7179901) first.

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
<https://flash.android.com/preview/cinnamonbun-qpr2-beta3>.

## Flash your device manually

![](https://developer.android.com/static/images/lockups/android-stacked.svg)

You can also download the latest system image and manually flash it to your
device. See the following table to download the system image for your test
device. Manually flashing a device is useful if you need precise control over
the test environment or if you need to reinstall frequently, such as when
performing automated testing.

After you back up your device data and download the matching system image, you
can [flash the image onto your device](https://developers.google.com/android/images#instructions).

You can choose to [return to the latest public build](https://developer.android.com/about/versions/17/qpr2/download#public) at any
time.

### Device factory images

|---|---|
| **Release date** | August 14, 2026 |
| **Builds** | CP41.260731.005.A2 CP41.260731.005.B1 |
| **Emulator support** | x86 (64-bit), ARM (v8-A) |
| **Security patch level** | 2026-08-05 |
| **Google Play services** | 26.26.34 |

| Device | Download Link and SHA-256 Checksum |
|---|---|
| Pixel 6a | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 Beta" data-action="download" data-label="bluejay" data-modal-dialog-id="bluejay_factory_zip">bluejay_beta-cp41.260731.005.a2-factory-619869e2.zip</button> `619869e2de5bb0a813e4683c6ad71f12fbb22586c08968a3700a0b0694190332` |
| Pixel 7 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 Beta" data-action="download" data-label="panther" data-modal-dialog-id="panther_factory_zip">panther_beta-cp41.260731.005.a2-factory-dbb346c9.zip</button> `dbb346c945e3385bc53132ea195b002e63e961c5b81a7aa2e786c1e068e039b9` |
| Pixel 7 Pro | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 Beta" data-action="download" data-label="cheetah" data-modal-dialog-id="cheetah_factory_zip">cheetah_beta-cp41.260731.005.a2-factory-fa8d63e8.zip</button> `fa8d63e83af2c5a48c3af957d6104ba323b89b4269a37ade3c96b3dcbdcdbc3c` |
| Pixel 7a | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 Beta" data-action="download" data-label="lynx" data-modal-dialog-id="lynx_factory_zip">lynx_beta-cp41.260731.005.a2-factory-9b732add.zip</button> `9b732add8146ffb24b681c5c9b91d1774b9a128775dabfb5d75f8049641f6f2d` |
| Pixel Fold | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 Beta" data-action="download" data-label="felix" data-modal-dialog-id="felix_factory_zip">felix_beta-cp41.260731.005.a2-factory-7b7c2d5b.zip</button> `7b7c2d5bd19e549c1eeef4fbc9ca5a47b40d80e337e9800dd0dba5cce7cc2703` |
| Pixel Tablet | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 Beta" data-action="download" data-label="tangorpro" data-modal-dialog-id="tangorpro_factory_zip">tangorpro_beta-cp41.260731.005.a2-factory-467d549b.zip</button> `467d549b962166d27d297e7c3055448852fab207d96eff264808b30e786424eb` |
| Pixel 8 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 Beta" data-action="download" data-label="shiba" data-modal-dialog-id="shiba_factory_zip">shiba_beta-cp41.260731.005.b1-factory-36fb6e7b.zip</button> `36fb6e7b19944a03aab29e91f4a2ecd6167fe2f32a9203e2eb4fce18a133743e` |
| Pixel 8 Pro | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 Beta" data-action="download" data-label="husky" data-modal-dialog-id="husky_factory_zip">husky_beta-cp41.260731.005.b1-factory-6d6e55e5.zip</button> `6d6e55e593d0aea17e9709625152ecda8df495ebd0b9f0cf423985bd1b28f3a2` |
| Pixel 8a | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 Beta" data-action="download" data-label="akita" data-modal-dialog-id="akita_factory_zip">akita_beta-cp41.260731.005.b1-factory-aab771dd.zip</button> `aab771dda862e68bbaa13bd4aebc0845dca0068df4b3a7e535d186da6d994053` |
| Pixel 9 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 Beta" data-action="download" data-label="tokay" data-modal-dialog-id="tokay_factory_zip">tokay_beta-cp41.260731.005.b1-factory-8fa73885.zip</button> `8fa738854d3761abd31633e1fc89bd2dc361b6bb8c86b1e4734d1410c13cb289` |
| Pixel 9 Pro | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 Beta" data-action="download" data-label="caiman" data-modal-dialog-id="caiman_factory_zip">caiman_beta-cp41.260731.005.b1-factory-e039b362.zip</button> `e039b362c82e2c442721a474cfea5dc2af5665df4b81270a095c7603256e0492` |
| Pixel 9 Pro XL | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 Beta" data-action="download" data-label="komodo" data-modal-dialog-id="komodo_factory_zip">komodo_beta-cp41.260731.005.b1-factory-5f125cf8.zip</button> `5f125cf8d08c75690ee9a174254a55924bd230002af8316a086dcd427be97065` |
| Pixel 9 Pro Fold | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 Beta" data-action="download" data-label="comet" data-modal-dialog-id="comet_factory_zip">comet_beta-cp41.260731.005.b1-factory-b72408c1.zip</button> `b72408c1773b0b09c91f7b8327f954f8227fc41bc55ed4db6074839b62e3cf20` |
| Pixel 9a | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 Beta" data-action="download" data-label="tegu" data-modal-dialog-id="tegu_factory_zip">tegu_beta-cp41.260731.005.b1-factory-e29d2c1c.zip</button> `e29d2c1c4df112f3db6a105d368768d376c25efc821fd63aff2f825bfa6452e4` |
| Pixel 10 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 Beta" data-action="download" data-label="frankel" data-modal-dialog-id="frankel_factory_zip">frankel_beta-cp41.260731.005.b1-factory-e72f83f3.zip</button> `e72f83f35e3083a57643f6e12ee43a91846967cca51ff65f4c2505f851342562` |
| Pixel 10 Pro | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 Beta" data-action="download" data-label="blazer" data-modal-dialog-id="blazer_factory_zip">blazer_beta-cp41.260731.005.b1-factory-45f403a2.zip</button> `45f403a2dc3e2df1d5f03e7677ad9333b06566858969e14edc5b61795879465d` |
| Pixel 10 Pro XL | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 Beta" data-action="download" data-label="mustang" data-modal-dialog-id="mustang_factory_zip">mustang_beta-cp41.260731.005.b1-factory-17f39573.zip</button> `17f39573fc426443f97062ada4bd022825a5cb768783ff28fa9aa98240ed9f1d` |
| Pixel 10 Pro Fold | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 Beta" data-action="download" data-label="rango" data-modal-dialog-id="rango_factory_zip">rango_beta-cp41.260731.005.b1-factory-a0b4ffb1.zip</button> `a0b4ffb132640170eaca96489b4d797a74338cfa5cc32eaad5d6c676dae9a62b` |
| Pixel 10a | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 Beta" data-action="download" data-label="stallion" data-modal-dialog-id="stallion_factory_zip">stallion_beta-cp41.260731.005.b1-factory-26c778ed.zip</button> `26c778ed0662e22ee27b2850f12241d938019165db9dbae08661824d40844a48` |

## Return to a public build

You can either use the Android Flash Tool to
[flash the factory image](https://flash.android.com/back-to-public), or obtain a factory spec system
image from the [Factory Images for Nexus and Pixel Devices](https://developers.google.com/android/images)
page and then manually flash it to the device.

> [!WARNING]
> **Warning:** Going back to a public build from a preview build (Developer Preview or Beta) requires a full device reset that removes all user data on the device. Make sure to [back up your data first](https://support.google.com/pixelphone/answer/7179901).

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/bluejay_beta-cp41.260731.005.a2-factory-619869e2.zip)

*bluejay_beta-cp41.260731.005.a2-factory-619869e2.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/panther_beta-cp41.260731.005.a2-factory-dbb346c9.zip)

*panther_beta-cp41.260731.005.a2-factory-dbb346c9.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/cheetah_beta-cp41.260731.005.a2-factory-fa8d63e8.zip)

*cheetah_beta-cp41.260731.005.a2-factory-fa8d63e8.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/lynx_beta-cp41.260731.005.a2-factory-9b732add.zip)

*lynx_beta-cp41.260731.005.a2-factory-9b732add.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/felix_beta-cp41.260731.005.a2-factory-7b7c2d5b.zip)

*felix_beta-cp41.260731.005.a2-factory-7b7c2d5b.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/tangorpro_beta-cp41.260731.005.a2-factory-467d549b.zip)

*tangorpro_beta-cp41.260731.005.a2-factory-467d549b.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/shiba_beta-cp41.260731.005.b1-factory-36fb6e7b.zip)

*shiba_beta-cp41.260731.005.b1-factory-36fb6e7b.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/husky_beta-cp41.260731.005.b1-factory-6d6e55e5.zip)

*husky_beta-cp41.260731.005.b1-factory-6d6e55e5.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/akita_beta-cp41.260731.005.b1-factory-aab771dd.zip)

*akita_beta-cp41.260731.005.b1-factory-aab771dd.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/tokay_beta-cp41.260731.005.b1-factory-8fa73885.zip)

*tokay_beta-cp41.260731.005.b1-factory-8fa73885.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/caiman_beta-cp41.260731.005.b1-factory-e039b362.zip)

*caiman_beta-cp41.260731.005.b1-factory-e039b362.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/komodo_beta-cp41.260731.005.b1-factory-5f125cf8.zip)

*komodo_beta-cp41.260731.005.b1-factory-5f125cf8.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/comet_beta-cp41.260731.005.b1-factory-b72408c1.zip)

*comet_beta-cp41.260731.005.b1-factory-b72408c1.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/tegu_beta-cp41.260731.005.b1-factory-e29d2c1c.zip)

*tegu_beta-cp41.260731.005.b1-factory-e29d2c1c.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/frankel_beta-cp41.260731.005.b1-factory-e72f83f3.zip)

*frankel_beta-cp41.260731.005.b1-factory-e72f83f3.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/blazer_beta-cp41.260731.005.b1-factory-45f403a2.zip)

*blazer_beta-cp41.260731.005.b1-factory-45f403a2.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/mustang_beta-cp41.260731.005.b1-factory-17f39573.zip)

*mustang_beta-cp41.260731.005.b1-factory-17f39573.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/rango_beta-cp41.260731.005.b1-factory-a0b4ffb1.zip)

*rango_beta-cp41.260731.005.b1-factory-a0b4ffb1.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/stallion_beta-cp41.260731.005.b1-factory-26c778ed.zip)

*stallion_beta-cp41.260731.005.b1-factory-26c778ed.zip*