---
title: https://developer.android.com/about/versions/17/download
url: https://developer.android.com/about/versions/17/download
source: md.txt
---

If you are a developer with a supported Google Pixel device, you can manually
update that device to the latest build for testing and development. Flashing a
factory image requires a full device reset, so make sure to [back up your
data](https://support.google.com/pixelphone/answer/7179901) first. Builds are available for the following Pixel devices:

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

After you've flashed a developer preview build to your Pixel device, you're automatically offered over-the-air (OTA) updates of later preview builds. We also deliver flashable images at each milestone, so you can choose the approach that works best for your test environment.

<br />

Use the following links and instructions to update your supported device to the
latest build. See [Get Android 17](https://developer.android.com/about/versions/17/get) for
other ways to get Android 17 for testing and development.

> [!WARNING]
> **Warning:** Flashing to a dp build from a production build---or going back to a production build from a dp build---requires a full device reset that removes all user data on the device. Make sure to [back up the data from your
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
<https://flash.android.com/preview/cinnamonbun-beta2>.

## Flash your device manually

![](https://developer.android.com/static/images/lockups/android-stacked.svg)

You can also download the latest system image and manually flash it to your
device. See the following table to download the system image for your test
device. Manually flashing a device is useful if you need precise control over
the test environment or if you need to reinstall frequently, such as when
performing automated testing.

After you back up your device data and download the matching system image, you
can [flash the image onto your device](https://developers.google.com/android/images#instructions).

You can choose to [return to the latest public build](https://developer.android.com/about/versions/17/download#public) at any
time.

### Device factory images

|---|---|
| **Release date** | February 26, 2026 |
| **Builds** | CP21.260206.011 CP21.260206.011.A1 (Pixel 6 Pro, Pixel 6, Pixel 6a, Pixel 7 Pro, Pixel 7) |
| **Emulator support** | x86 (64-bit), ARM (v8-A) |
| **Security patch level** | 2026-02-05 |
| **Google Play services** | 25.49.33 |

| Device | Download Link and SHA-256 Checksum |
|---|---|
| Pixel 6 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 DP" data-action="download" data-label="oriole" data-modal-dialog-id="oriole_factory_zip">oriole_beta-cp21.260206.011.a1-factory-6e365133.zip</button> `6e3651331070c7d3df47733dfef655b651b8b228a3fcfa471124669ecd14d01b` |
| Pixel 6 Pro | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 DP" data-action="download" data-label="raven" data-modal-dialog-id="raven_factory_zip">raven_beta-cp21.260206.011.a1-factory-56dd53a6.zip</button> `56dd53a668c7da6af53c1ea3d2bd024a867551f380e8a167a048141f8cb64745` |
| Pixel 7 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 DP" data-action="download" data-label="panther" data-modal-dialog-id="panther_factory_zip">panther_beta-cp21.260206.011.a1-factory-a09c977d.zip</button> `a09c977df018949d056a151a4262c8ca03c1d0c4a9e279db2512e92b903abce4` |
| Pixel 7 Pro | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 DP" data-action="download" data-label="cheetah" data-modal-dialog-id="cheetah_factory_zip">cheetah_beta-cp21.260206.011.a1-factory-b8bdf1c1.zip</button> `b8bdf1c1bf0c755beb861752bb36387e5231b43d1d3dcb92b4f1065ba2b6454e` |
| Pixel 7a | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 DP" data-action="download" data-label="lynx" data-modal-dialog-id="lynx_factory_zip">lynx_beta-cp21.260206.011-factory-3d149a71.zip</button> `3d149a71f7ee9afae94ccfb85464b9821808d449a57786f5dd74f87878e02964` |
| Pixel Fold | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 DP" data-action="download" data-label="felix" data-modal-dialog-id="felix_factory_zip">felix_beta-cp21.260206.011-factory-12b653e1.zip</button> `12b653e12b863ef00ec70c464d86fd72993f31add0979816d0994f7238dc19ae` |
| Pixel Tablet | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 DP" data-action="download" data-label="tangorpro" data-modal-dialog-id="tangorpro_factory_zip">tangorpro_beta-cp21.260206.011-factory-bc23832a.zip</button> `bc23832a89d4552c17c1c085aa68ff6d53363e718dfe5534d85ccfe3a2791cf7` |
| Pixel 8 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 DP" data-action="download" data-label="shiba" data-modal-dialog-id="shiba_factory_zip">shiba_beta-cp21.260206.011-factory-293b19b1.zip</button> `293b19b1c599e63ffa84b1ec3cc010d47595e4b4d918cc5ca80c0326c67dbca3` |
| Pixel 8 Pro | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 DP" data-action="download" data-label="husky" data-modal-dialog-id="husky_factory_zip">husky_beta-cp21.260206.011-factory-71e41dd0.zip</button> `71e41dd0a50877aab5ef4b7b5c886cb78d617e77c4baee214dad9d80e5d8a257` |
| Pixel 8a | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 DP" data-action="download" data-label="akita" data-modal-dialog-id="akita_factory_zip">akita_beta-cp21.260206.011-factory-769d4393.zip</button> `769d43931cb9c4cf0792073f0788a5a52529693555aca1d91b96d01e884c7efe` |
| Pixel 9 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 DP" data-action="download" data-label="tokay" data-modal-dialog-id="tokay_factory_zip">tokay_beta-cp21.260206.011-factory-d9859169.zip</button> `d9859169262e10324645896e9d9abd914668febf86b6e37b0c1bb4f1b8a7839e` |
| Pixel 9 Pro | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 DP" data-action="download" data-label="caiman" data-modal-dialog-id="caiman_factory_zip">caiman_beta-cp21.260206.011-factory-12b29627.zip</button> `12b29627cf2b3ce0c0a65a55164d6ced8afd83fc0c5c28628b351a429c88f2f2` |
| Pixel 9 Pro XL | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 DP" data-action="download" data-label="komodo" data-modal-dialog-id="komodo_factory_zip">komodo_beta-cp21.260206.011-factory-15df7f8b.zip</button> `15df7f8b22356ade8f76456cfc733d5ec78e5bf1833af3950d82c0a32cf2f5c7` |
| Pixel 9 Pro Fold | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 DP" data-action="download" data-label="comet" data-modal-dialog-id="comet_factory_zip">comet_beta-cp21.260206.011-factory-cc0645a9.zip</button> `cc0645a9a27b7169db7802d7862583367c9db903259eda81615503a4dae9f7eb` |
| Pixel 9a | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 DP" data-action="download" data-label="tegu" data-modal-dialog-id="tegu_factory_zip">tegu_beta-cp21.260206.011-factory-297ab203.zip</button> `297ab203206ecd39c181ad492a2cd4676d9265d17abaf2d6f7a393ca5738f69f` |
| Pixel 10 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 DP" data-action="download" data-label="frankel" data-modal-dialog-id="frankel_factory_zip">frankel_beta-cp21.260206.011-factory-7826a404.zip</button> `7826a404902185b1a1277d0abbc56f3d4dde9965424149cea10265550bfc7375` |
| Pixel 10 Pro | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 DP" data-action="download" data-label="blazer" data-modal-dialog-id="blazer_factory_zip">blazer_beta-cp21.260206.011-factory-70e1d651.zip</button> `70e1d651dc1dafa06a6bee82a0ef6d30f1760a10788d0b84f705fde3b09e8683` |
| Pixel 10 Pro XL | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 DP" data-action="download" data-label="mustang" data-modal-dialog-id="mustang_factory_zip">mustang_beta-cp21.260206.011-factory-409b3b9b.zip</button> `409b3b9bcf0613b7ca0eae5e82a3bb5013ec9cff4581b0293adf22f2398fe614` |
| Pixel 10 Pro Fold | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 DP" data-action="download" data-label="rango" data-modal-dialog-id="rango_factory_zip">rango_beta-cp21.260206.011-factory-53047795.zip</button> `53047795cbaf933a99763ce707a005fc88a9f6a6f68325940ea7bb2c8d0513b5` |

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

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/oriole_beta-cp21.260206.011.a1-factory-6e365133.zip)

*oriole_beta-cp21.260206.011.a1-factory-6e365133.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/raven_beta-cp21.260206.011.a1-factory-56dd53a6.zip)

*raven_beta-cp21.260206.011.a1-factory-56dd53a6.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/panther_beta-cp21.260206.011.a1-factory-a09c977d.zip)

*panther_beta-cp21.260206.011.a1-factory-a09c977d.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/cheetah_beta-cp21.260206.011.a1-factory-b8bdf1c1.zip)

*cheetah_beta-cp21.260206.011.a1-factory-b8bdf1c1.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/lynx_beta-cp21.260206.011-factory-3d149a71.zip)

*lynx_beta-cp21.260206.011-factory-3d149a71.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/felix_beta-cp21.260206.011-factory-12b653e1.zip)

*felix_beta-cp21.260206.011-factory-12b653e1.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/tangorpro_beta-cp21.260206.011-factory-bc23832a.zip)

*tangorpro_beta-cp21.260206.011-factory-bc23832a.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/shiba_beta-cp21.260206.011-factory-293b19b1.zip)

*shiba_beta-cp21.260206.011-factory-293b19b1.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/husky_beta-cp21.260206.011-factory-71e41dd0.zip)

*husky_beta-cp21.260206.011-factory-71e41dd0.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/akita_beta-cp21.260206.011-factory-769d4393.zip)

*akita_beta-cp21.260206.011-factory-769d4393.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/tokay_beta-cp21.260206.011-factory-d9859169.zip)

*tokay_beta-cp21.260206.011-factory-d9859169.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/caiman_beta-cp21.260206.011-factory-12b29627.zip)

*caiman_beta-cp21.260206.011-factory-12b29627.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/komodo_beta-cp21.260206.011-factory-15df7f8b.zip)

*komodo_beta-cp21.260206.011-factory-15df7f8b.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/comet_beta-cp21.260206.011-factory-cc0645a9.zip)

*comet_beta-cp21.260206.011-factory-cc0645a9.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/tegu_beta-cp21.260206.011-factory-297ab203.zip)

*tegu_beta-cp21.260206.011-factory-297ab203.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/frankel_beta-cp21.260206.011-factory-7826a404.zip)

*frankel_beta-cp21.260206.011-factory-7826a404.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/blazer_beta-cp21.260206.011-factory-70e1d651.zip)

*blazer_beta-cp21.260206.011-factory-70e1d651.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/mustang_beta-cp21.260206.011-factory-409b3b9b.zip)

*mustang_beta-cp21.260206.011-factory-409b3b9b.zip*

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 factory system image </button> [Download Android 17 factory system image](https://dl.google.com/developers/android/cinnamonbun/images/factory/rango_beta-cp21.260206.011-factory-53047795.zip)

*rango_beta-cp21.260206.011-factory-53047795.zip*