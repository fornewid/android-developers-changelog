---
title: https://developer.android.com/about/versions/16/qpr2/download
url: https://developer.android.com/about/versions/16/qpr2/download
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
latest build. See [Get Android 16 QPR2](https://developer.android.com/about/versions/16/qpr2/get) for
other ways to get Android 16 QPR2 for testing and development.

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
<https://flash.android.com/preview/baklava-qpr2-beta3.3>.

## Flash your device manually

![](https://developer.android.com/static/images/lockups/android-stacked.svg)

You can also download the latest system image and manually flash it to your
device. See the following table to download the system image for your test
device. Manually flashing a device is useful if you need precise control over
the test environment or if you need to reinstall frequently, such as when
performing automated testing.

After you back up your device data and download the matching system image, you
can [flash the image onto your device](https://developers.google.com/android/images#instructions).

You can choose to [return to the latest public build](https://developer.android.com/about/versions/16/qpr2/download#public) at any
time.

### Device factory images

|---|---|
| **Release date** | November 10, 2025 |
| **Builds** | BP41.250916.015.A1 |
| **Emulator support** | TBA |
| **Security patch level** | 2025-10-05 |
| **Google Play services** | 25.34.34 |
| **API diff** | - [QPR2 Beta 2 → API 36.1](https://developer.android.com/sdk/api_diff/36.1-incr/changes) - [API 36 → API 36.1](https://developer.android.com/sdk/api_diff/36.1/changes) |

| Device | Download Link and SHA-256 Checksum |
|---|---|
| Pixel 6 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="oriole" data-modal-dialog-id="oriole_factory_zip">oriole_beta-bp41.250916.015-factory-95f96576.zip</button> `95f96576f2a0c4827374923805fb13057dac6258beab71313ef80e01ec362b59` |
| Pixel 6 Pro | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="raven" data-modal-dialog-id="raven_factory_zip">raven_beta-bp41.250916.015-factory-4a1cc330.zip</button> `4a1cc3302d5ec2e23482920f69ebbff218370f8e791b442bf6e7277126166123` |
| Pixel 6a | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="bluejay" data-modal-dialog-id="bluejay_factory_zip">bluejay_beta-bp41.250916.015-factory-f7eb08b7.zip</button> `f7eb08b7d1d7c643f0a22e0d281d07c0a1265155e43d3300c25626b985014309` |
| Pixel 7 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="panther" data-modal-dialog-id="panther_factory_zip">panther_beta-bp41.250916.015.a1-factory-11373be7.zip</button> `11373be7037a0d53b1aad6e409fbc256638338449b18928712f005df1bd83e97` |
| Pixel 7 Pro | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="cheetah" data-modal-dialog-id="cheetah_factory_zip">cheetah_beta-bp41.250916.015.a1-factory-181565e3.zip</button> `181565e3c34ab86e03cd998d875a32d53ef20555bbc262b939c602c40995f12e` |
| Pixel 7a | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="lynx" data-modal-dialog-id="lynx_factory_zip">lynx_beta-bp41.250916.015.a1-factory-b569f786.zip</button> `b569f786a0dddeb89b95a0f9a298f7bea043574a3bc964967af8fe93ad38d171` |
| Pixel Fold | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="felix" data-modal-dialog-id="felix_factory_zip">felix_beta-bp41.250916.015.a1-factory-b940dec5.zip</button> `b940dec5e6045e8d023eb33b655e9f52351d55ce7b9da282199354d26fbe549e` |
| Pixel Tablet | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="tangorpro" data-modal-dialog-id="tangorpro_factory_zip">tangorpro_beta-bp41.250916.015.a1-factory-9c42b0da.zip</button> `9c42b0da4e28cb6f6870f3e1a88e3ef15e0a1370aac26148bbb1d3a0e3438f9e` |
| Pixel 8 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="shiba" data-modal-dialog-id="shiba_factory_zip">shiba_beta-bp41.250916.015.a1-factory-838aae45.zip</button> `838aae45d7df24e2b463ad378476ebf7111dd49c524bb958e185123ba631a2fc` |
| Pixel 8 Pro | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="husky" data-modal-dialog-id="husky_factory_zip">husky_beta-bp41.250916.015.a1-factory-4f2dc704.zip</button> `4f2dc70427242baacd790e11dc1c8fa3ed0f407777b9f113461225c13985c30a` |
| Pixel 8a | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="akita" data-modal-dialog-id="akita_factory_zip">akita_beta-bp41.250916.015.a1-factory-8b1f6fb1.zip</button> `8b1f6fb1b8fa9f47f1688cfb48def5276d2452eed6a963f982552298fab316dc` |
| Pixel 9 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="tokay" data-modal-dialog-id="tokay_factory_zip">tokay_beta-bp41.250916.015.a1-factory-2c441aa2.zip</button> `2c441aa2273d75a82fbfc11844ad9d005f3e0a939233dd0d9511bf145d7c6a82` |
| Pixel 9 Pro | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="caiman" data-modal-dialog-id="caiman_factory_zip">caiman_beta-bp41.250916.015.a1-factory-16095a16.zip</button> `16095a163d9d5df2a56baa648311583eee32d681da0878249cccfd8e1042ab9e` |
| Pixel 9 Pro XL | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="komodo" data-modal-dialog-id="komodo_factory_zip">komodo_beta-bp41.250916.015.a1-factory-be62f918.zip</button> `be62f918f213a861b740934f9d9ce9702666e8b7d73be439671f46327d310914` |
| Pixel 9 Pro Fold | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="comet" data-modal-dialog-id="comet_factory_zip">comet_beta-bp41.250916.015.a1-factory-e262a83d.zip</button> `e262a83dee7c5001d5127bad6e61b90cafb3efda29607626afc7985b14da832d` |
| Pixel 9a | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="tegu" data-modal-dialog-id="tegu_factory_zip">tegu_beta-bp41.250916.015.a1-factory-a014e0d6.zip</button> `a014e0d625d48ed94129c6f24aa7a2e8f09854df9c4499e188a839cbed5bb736` |
| Pixel 10 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="frankel" data-modal-dialog-id="frankel_factory_zip">frankel_beta-bp41.250916.015.a1-factory-cda8438d.zip</button> `cda8438d7e8392d076fbef6c8114da9a703d7c18038dd872a8098a7a4c5a39e3` |
| Pixel 10 Pro | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="blazer" data-modal-dialog-id="blazer_factory_zip">blazer_beta-bp41.250916.015.a1-factory-2f88c020.zip</button> `2f88c0204712f4802f50652fc198d37980fc2a0a88defdcc62dbded466809d2b` |
| Pixel 10 Pro XL | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="mustang" data-modal-dialog-id="mustang_factory_zip">mustang_beta-bp41.250916.015.a1-factory-0b09bbb7.zip</button> `0b09bbb7627b24f0d46f838329ecd3a36a4edccc2b35e54fbaf5050ef49666fb` |
| Pixel 10 Pro Fold | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android QPR2 Beta" data-action="download" data-label="rango" data-modal-dialog-id="rango_factory_zip">rango_beta-bp41.250916.015.a1-factory-6c0c027c.zip</button> `6c0c027c1d12f3ea891c207797397e03002f4ee03d2120e36e113f3b53a60fa2` |

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

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 factory system image </button> [Download Android 16 factory system image](https://dl.google.com/developers/android/baklava/images/factory/oriole_beta-bp41.250916.015-factory-95f96576.zip)

*oriole_beta-bp41.250916.015-factory-95f96576.zip*

## Download Android 16 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 factory system image </button> [Download Android 16 factory system image](https://dl.google.com/developers/android/baklava/images/factory/raven_beta-bp41.250916.015-factory-4a1cc330.zip)

*raven_beta-bp41.250916.015-factory-4a1cc330.zip*

## Download Android 16 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 factory system image </button> [Download Android 16 factory system image](https://dl.google.com/developers/android/baklava/images/factory/bluejay_beta-bp41.250916.015-factory-f7eb08b7.zip)

*bluejay_beta-bp41.250916.015-factory-f7eb08b7.zip*

## Download Android 16 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 factory system image </button> [Download Android 16 factory system image](https://dl.google.com/developers/android/baklava/images/factory/panther_beta-bp41.250916.015.a1-factory-11373be7.zip)

*panther_beta-bp41.250916.015.a1-factory-11373be7.zip*

## Download Android 16 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 factory system image </button> [Download Android 16 factory system image](https://dl.google.com/developers/android/baklava/images/factory/cheetah_beta-bp41.250916.015.a1-factory-181565e3.zip)

*cheetah_beta-bp41.250916.015.a1-factory-181565e3.zip*

## Download Android 16 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 factory system image </button> [Download Android 16 factory system image](https://dl.google.com/developers/android/baklava/images/factory/lynx_beta-bp41.250916.015.a1-factory-b569f786.zip)

*lynx_beta-bp41.250916.015.a1-factory-b569f786.zip*

## Download Android 16 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 factory system image </button> [Download Android 16 factory system image](https://dl.google.com/developers/android/baklava/images/factory/felix_beta-bp41.250916.015.a1-factory-b940dec5.zip)

*felix_beta-bp41.250916.015.a1-factory-b940dec5.zip*

## Download Android 16 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 factory system image </button> [Download Android 16 factory system image](https://dl.google.com/developers/android/baklava/images/factory/tangorpro_beta-bp41.250916.015.a1-factory-9c42b0da.zip)

*tangorpro_beta-bp41.250916.015.a1-factory-9c42b0da.zip*

## Download Android 16 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 factory system image </button> [Download Android 16 factory system image](https://dl.google.com/developers/android/baklava/images/factory/shiba_beta-bp41.250916.015.a1-factory-838aae45.zip)

*shiba_beta-bp41.250916.015.a1-factory-838aae45.zip*

## Download Android 16 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 factory system image </button> [Download Android 16 factory system image](https://dl.google.com/developers/android/baklava/images/factory/husky_beta-bp41.250916.015.a1-factory-4f2dc704.zip)

*husky_beta-bp41.250916.015.a1-factory-4f2dc704.zip*

## Download Android 16 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 factory system image </button> [Download Android 16 factory system image](https://dl.google.com/developers/android/baklava/images/factory/akita_beta-bp41.250916.015.a1-factory-8b1f6fb1.zip)

*akita_beta-bp41.250916.015.a1-factory-8b1f6fb1.zip*

## Download Android 16 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 factory system image </button> [Download Android 16 factory system image](https://dl.google.com/developers/android/baklava/images/factory/tokay_beta-bp41.250916.015.a1-factory-2c441aa2.zip)

*tokay_beta-bp41.250916.015.a1-factory-2c441aa2.zip*

## Download Android 16 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 factory system image </button> [Download Android 16 factory system image](https://dl.google.com/developers/android/baklava/images/factory/caiman_beta-bp41.250916.015.a1-factory-16095a16.zip)

*caiman_beta-bp41.250916.015.a1-factory-16095a16.zip*

## Download Android 16 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 factory system image </button> [Download Android 16 factory system image](https://dl.google.com/developers/android/baklava/images/factory/komodo_beta-bp41.250916.015.a1-factory-be62f918.zip)

*komodo_beta-bp41.250916.015.a1-factory-be62f918.zip*

## Download Android 16 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 factory system image </button> [Download Android 16 factory system image](https://dl.google.com/developers/android/baklava/images/factory/comet_beta-bp41.250916.015.a1-factory-e262a83d.zip)

*comet_beta-bp41.250916.015.a1-factory-e262a83d.zip*

## Download Android 16 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 factory system image </button> [Download Android 16 factory system image](https://dl.google.com/developers/android/baklava/images/factory/tegu_beta-bp41.250916.015.a1-factory-a014e0d6.zip)

*tegu_beta-bp41.250916.015.a1-factory-a014e0d6.zip*

## Download Android 16 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 factory system image </button> [Download Android 16 factory system image](https://dl.google.com/developers/android/baklava/images/factory/frankel_beta-bp41.250916.015.a1-factory-cda8438d.zip)

*frankel_beta-bp41.250916.015.a1-factory-cda8438d.zip*

## Download Android 16 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 factory system image </button> [Download Android 16 factory system image](https://dl.google.com/developers/android/baklava/images/factory/blazer_beta-bp41.250916.015.a1-factory-2f88c020.zip)

*blazer_beta-bp41.250916.015.a1-factory-2f88c020.zip*

## Download Android 16 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 factory system image </button> [Download Android 16 factory system image](https://dl.google.com/developers/android/baklava/images/factory/mustang_beta-bp41.250916.015.a1-factory-0b09bbb7.zip)

*mustang_beta-bp41.250916.015.a1-factory-0b09bbb7.zip*

## Download Android 16 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 factory system image </button> [Download Android 16 factory system image](https://dl.google.com/developers/android/baklava/images/factory/rango_beta-bp41.250916.015.a1-factory-6c0c027c.zip)

*rango_beta-bp41.250916.015.a1-factory-6c0c027c.zip*