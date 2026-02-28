---
title: https://developer.android.com/about/versions/16/qpr3/download
url: https://developer.android.com/about/versions/16/qpr3/download
source: md.txt
---

To find factory images for already-released, stable versions of the platform,
see [Factory Images for Nexus and Pixel Devices](https://developers.google.com/android/images).

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
- Pixel 10, 10 Pro, 10 Pro XL, and 10 Pro Fold

After you've flashed a beta build to your Pixel device, your device is
automatically enrolled in the [Android Beta for Pixel program](https://g.co/androidbeta) and offered
continuous over-the-air (OTA) updates to the latest beta builds (including QPRs)
until you choose to unenroll that device from the program. We also
deliver flashable images at each milestone, so you can choose the approach that
works best for your test environment.

Use the following links and instructions to update your supported device to the
latest build. See [Get Android 16 QPR3](https://developer.android.com/about/versions/16/qpr3/get) for
other ways to get Android 16 QPR3 for testing and development.

> [!WARNING]
> **Warning:** Flashing to a beta build from a production build---or going back to a production build from a beta build---requires a full device reset that removes all user data on the device. Make sure to [back up the data from
> your Pixel](https://support.google.com/pixelphone/answer/7179901) first.

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
<https://flash.android.com/preview/baklava-qpr3-beta2.1>.

## Flash your device manually

![](https://developer.android.com/static/images/lockups/android-stacked.svg)

You can also download the latest system image and manually flash it to your
device. See the following table to download the system image for your test
device. Manually flashing a device is useful if you need precise control over
the test environment or if you need to reinstall frequently, such as when
performing automated testing.

After you back up your device data and download the matching system image, you
can [flash the image onto your device](https://developers.google.com/android/images#instructions).

You can choose to [return to the latest public build](https://developer.android.com/about/versions/16/qpr3/download#public) at any
time.

### Device factory images

|---|---|
| **Release date** | February 10, 2026 |
| **Builds** | CP11.251209.009.A1 CP11.251209.009 (Pixel 6 Pro, Pixel 6, Pixel 6a, Pixel 7 Pro, Pixel 7) |
| **Emulator support** | TBA |
| **Security patch level** | 2026-01-05 |
| **Google Play services** | 25.47.33 |
| **API diff** | - [QPR2 Beta 2 → API 36.1](https://developer.android.com/sdk/api_diff/36.1-incr/changes) - [API 36 → API 36.1](https://developer.android.com/sdk/api_diff/36.1/changes) |

| Device | Download Link and SHA-256 Checksum |
|---|---|
| Pixel 6 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="oriole" data-modal-dialog-id="oriole_factory_zip">oriole_beta-cp11.251209.009-factory-889f8bc2.zip</button> `889f8bc2dd1f8d6da26dc50ab5298a07ac68ef064b7cffb38eac25b097e55ddb` |
| Pixel 6 Pro | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="raven" data-modal-dialog-id="raven_factory_zip">raven_beta-cp11.251209.009-factory-def79428.zip</button> `def79428f81e58ba896db8e4fc604582d1cde25e64de51013f6cf93cb4f08f9b` |
| Pixel 6a | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="bluejay" data-modal-dialog-id="bluejay_factory_zip">bluejay_beta-cp11.251209.009-factory-74427982.zip</button> `744279827ec68a151fd2d5af6e127bd3b00b0fb1915ac3c69c5fa0031d674f8b` |
| Pixel 7 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="panther" data-modal-dialog-id="panther_factory_zip">panther_beta-cp11.251209.009-factory-da84a2cc.zip</button> `da84a2ccafc460f0be5040d27d03027fb55e07ffed72c051df76d44914b93101` |
| Pixel 7 Pro | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="cheetah" data-modal-dialog-id="cheetah_factory_zip">cheetah_beta-cp11.251209.009-factory-e8a29fce.zip</button> `e8a29fce7dd1ddfbfaad909cd4c0ba18b67448a6e356565fc377b26d0ff0ec77` |
| Pixel 7a | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="lynx" data-modal-dialog-id="lynx_factory_zip">lynx_beta-cp11.251209.009.a1-factory-7d7abfe2.zip</button> `7d7abfe22176c5304311b0024b22854bbfe7b2ef99428e138276ece5c699e2e7` |
| Pixel Fold | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="felix" data-modal-dialog-id="felix_factory_zip">felix_beta-cp11.251209.009.a1-factory-fbcb6094.zip</button> `fbcb60944162094a43b096ec8d0e687ba9c83d25e91a9b133fed658dacd6ae8a` |
| Pixel Tablet | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="tangorpro" data-modal-dialog-id="tangorpro_factory_zip">tangorpro_beta-cp11.251209.009.a1-factory-d1f5b106.zip</button> `d1f5b1068667b2f7eb02142d206480369529d29caf503a716d8045cfc79b45b8` |
| Pixel 8 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="shiba" data-modal-dialog-id="shiba_factory_zip">shiba_beta-cp11.251209.009.a1-factory-d6e5b9db.zip</button> `d6e5b9db31e4c33dd5d7bfc158420b54aef0be5de002bdff2c098ae644d86f6a` |
| Pixel 8 Pro | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="husky" data-modal-dialog-id="husky_factory_zip">husky_beta-cp11.251209.009.a1-factory-3833fc8e.zip</button> `3833fc8e302d7e1145be26621fe60d7fa8b9614922458302ef5f510ea70a536b` |
| Pixel 8a | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="akita" data-modal-dialog-id="akita_factory_zip">akita_beta-cp11.251209.009.a1-factory-b4ecb034.zip</button> `b4ecb034e89a6dea3878c565f3b102d662ea8f976d5d7ee05efa49b819a5a4aa` |
| Pixel 9 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="tokay" data-modal-dialog-id="tokay_factory_zip">tokay_beta-cp11.251209.009.a1-factory-9236059e.zip</button> `9236059eae32b15abf7a067d736a0a21d8c17df3740b8b4d3c9b4b5d4a4fde32` |
| Pixel 9 Pro | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="caiman" data-modal-dialog-id="caiman_factory_zip">caiman_beta-cp11.251209.009.a1-factory-a6cfbcd5.zip</button> `a6cfbcd525314ed2163f2f766dcba81ea522fc304af1a1bcb9dc3e84afc531dc` |
| Pixel 9 Pro XL | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="komodo" data-modal-dialog-id="komodo_factory_zip">komodo_beta-cp11.251209.009.a1-factory-807e325a.zip</button> `807e325ac88321e720ac7fd41c8944e94edc919146aac1d763651217b0c16b57` |
| Pixel 9 Pro Fold | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="comet" data-modal-dialog-id="comet_factory_zip">comet_beta-cp11.251209.009.a1-factory-f43be024.zip</button> `f43be0244efe052ae74b7ad4d62aa3f8d12fc54319a6c40b59caa614051d0697` |
| Pixel 9a | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="tegu" data-modal-dialog-id="tegu_factory_zip">tegu_beta-cp11.251209.009.a1-factory-b8a8cdf8.zip</button> `b8a8cdf807e500facd3eb4c9fa6ba22fae1e551e5bd8668dc57325954c5259fa` |
| Pixel 10 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="frankel" data-modal-dialog-id="frankel_factory_zip">frankel_beta-cp11.251209.009.a1-factory-3dcd9752.zip</button> `3dcd97523a0c04c266fb07a8aa08913b61580b96b2098f4997ab9e0bdf0784b5` |
| Pixel 10 Pro | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="blazer" data-modal-dialog-id="blazer_factory_zip">blazer_beta-cp11.251209.009.a1-factory-c922c027.zip</button> `c922c027a9e33ad9eda5d781404727f55e87cbd537ca8e544a29b5631fa46e99` |
| Pixel 10 Pro XL | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="mustang" data-modal-dialog-id="mustang_factory_zip">mustang_beta-cp11.251209.009.a1-factory-67b1e6bc.zip</button> `67b1e6bc5ea0aefefcd47b2bf047c07e51b19c11cf8ac50e4ace5ce61a6c850f` |
| Pixel 10 Pro Fold | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="rango" data-modal-dialog-id="rango_factory_zip">rango_beta-cp11.251209.009.a1-factory-e3cd6ba1.zip</button> `e3cd6ba1aa6e9dfdbeac900e4d63ea80615d70be0593660c54a65bfbe35dde2e` |

## Return to a public build

You can either use the Android Flash Tool to
[flash the factory image](https://flash.android.com/back-to-public), or obtain a factory spec system
image from the [Factory Images for Nexus and Pixel Devices](https://developers.google.com/android/images)
page and then manually flash it to the device.

> [!WARNING]
> **Warning:** Going back to a public build from a preview build (Developer Preview or Beta) requires a full device reset that removes all user data on the device. Make sure to [back up your data first](https://support.google.com/pixelphone/answer/7179901).

## Download Android 16 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 factory system image </button> [Download Android 16 factory system image](https://dl.google.com/developers/android/baklava/images/factory/oriole_beta-cp11.251209.009-factory-889f8bc2.zip)

*oriole_beta-cp11.251209.009-factory-889f8bc2.zip*

## Download Android 16 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 factory system image </button> [Download Android 16 factory system image](https://dl.google.com/developers/android/baklava/images/factory/raven_beta-cp11.251209.009-factory-def79428.zip)

*raven_beta-cp11.251209.009-factory-def79428.zip*

## Download Android 16 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 factory system image </button> [Download Android 16 factory system image](https://dl.google.com/developers/android/baklava/images/factory/bluejay_beta-cp11.251209.009-factory-74427982.zip)

*bluejay_beta-cp11.251209.009-factory-74427982.zip*

## Download Android 16 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 factory system image </button> [Download Android 16 factory system image](https://dl.google.com/developers/android/baklava/images/factory/panther_beta-cp11.251209.009-factory-da84a2cc.zip)

*panther_beta-cp11.251209.009-factory-da84a2cc.zip*

## Download Android 16 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 factory system image </button> [Download Android 16 factory system image](https://dl.google.com/developers/android/baklava/images/factory/cheetah_beta-cp11.251209.009-factory-e8a29fce.zip)

*cheetah_beta-cp11.251209.009-factory-e8a29fce.zip*

## Download Android 16 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 factory system image </button> [Download Android 16 factory system image](https://dl.google.com/developers/android/baklava/images/factory/lynx_beta-cp11.251209.009.a1-factory-7d7abfe2.zip)

*lynx_beta-cp11.251209.009.a1-factory-7d7abfe2.zip*

## Download Android 16 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 factory system image </button> [Download Android 16 factory system image](https://dl.google.com/developers/android/baklava/images/factory/felix_beta-cp11.251209.009.a1-factory-fbcb6094.zip)

*felix_beta-cp11.251209.009.a1-factory-fbcb6094.zip*

## Download Android 16 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 factory system image </button> [Download Android 16 factory system image](https://dl.google.com/developers/android/baklava/images/factory/tangorpro_beta-cp11.251209.009.a1-factory-d1f5b106.zip)

*tangorpro_beta-cp11.251209.009.a1-factory-d1f5b106.zip*

## Download Android 16 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 factory system image </button> [Download Android 16 factory system image](https://dl.google.com/developers/android/baklava/images/factory/shiba_beta-cp11.251209.009.a1-factory-d6e5b9db.zip)

*shiba_beta-cp11.251209.009.a1-factory-d6e5b9db.zip*

## Download Android 16 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 factory system image </button> [Download Android 16 factory system image](https://dl.google.com/developers/android/baklava/images/factory/husky_beta-cp11.251209.009.a1-factory-3833fc8e.zip)

*husky_beta-cp11.251209.009.a1-factory-3833fc8e.zip*

## Download Android 16 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 factory system image </button> [Download Android 16 factory system image](https://dl.google.com/developers/android/baklava/images/factory/akita_beta-cp11.251209.009.a1-factory-b4ecb034.zip)

*akita_beta-cp11.251209.009.a1-factory-b4ecb034.zip*

## Download Android 16 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 factory system image </button> [Download Android 16 factory system image](https://dl.google.com/developers/android/baklava/images/factory/tokay_beta-cp11.251209.009.a1-factory-9236059e.zip)

*tokay_beta-cp11.251209.009.a1-factory-9236059e.zip*

## Download Android 16 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 factory system image </button> [Download Android 16 factory system image](https://dl.google.com/developers/android/baklava/images/factory/caiman_beta-cp11.251209.009.a1-factory-a6cfbcd5.zip)

*caiman_beta-cp11.251209.009.a1-factory-a6cfbcd5.zip*

## Download Android 16 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 factory system image </button> [Download Android 16 factory system image](https://dl.google.com/developers/android/baklava/images/factory/komodo_beta-cp11.251209.009.a1-factory-807e325a.zip)

*komodo_beta-cp11.251209.009.a1-factory-807e325a.zip*

## Download Android 16 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 factory system image </button> [Download Android 16 factory system image](https://dl.google.com/developers/android/baklava/images/factory/comet_beta-cp11.251209.009.a1-factory-f43be024.zip)

*comet_beta-cp11.251209.009.a1-factory-f43be024.zip*

## Download Android 16 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 factory system image </button> [Download Android 16 factory system image](https://dl.google.com/developers/android/baklava/images/factory/tegu_beta-cp11.251209.009.a1-factory-b8a8cdf8.zip)

*tegu_beta-cp11.251209.009.a1-factory-b8a8cdf8.zip*

## Download Android 16 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 factory system image </button> [Download Android 16 factory system image](https://dl.google.com/developers/android/baklava/images/factory/frankel_beta-cp11.251209.009.a1-factory-3dcd9752.zip)

*frankel_beta-cp11.251209.009.a1-factory-3dcd9752.zip*

## Download Android 16 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 factory system image </button> [Download Android 16 factory system image](https://dl.google.com/developers/android/baklava/images/factory/blazer_beta-cp11.251209.009.a1-factory-c922c027.zip)

*blazer_beta-cp11.251209.009.a1-factory-c922c027.zip*

## Download Android 16 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 factory system image </button> [Download Android 16 factory system image](https://dl.google.com/developers/android/baklava/images/factory/mustang_beta-cp11.251209.009.a1-factory-67b1e6bc.zip)

*mustang_beta-cp11.251209.009.a1-factory-67b1e6bc.zip*

## Download Android 16 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 factory system image </button> [Download Android 16 factory system image](https://dl.google.com/developers/android/baklava/images/factory/rango_beta-cp11.251209.009.a1-factory-e3cd6ba1.zip)

*rango_beta-cp11.251209.009.a1-factory-e3cd6ba1.zip*