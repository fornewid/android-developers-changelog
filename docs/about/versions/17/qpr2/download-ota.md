---
title: https://developer.android.com/about/versions/17/qpr2/download-ota
url: https://developer.android.com/about/versions/17/qpr2/download-ota
source: md.txt
---

Applying an OTA image can help you recover a device that received an OTA update
for an Android 17 Beta build but wouldn't start up
after the update was installed. If you are trying to get Android 17 on your
device but you aren't trying to recover from a failed OTA update, see [Get
Android 17](https://developer.android.com/about/versions/17/get) instead.
Building on the [initial release of Android 17](https://developer.android.com/about/versions/17), we continue to update the platform with fixes and improvements that are then rolled out to supported devices. These releases happen on a quarterly cadence through *Quarterly Platform Releases* (QPRs), which are delivered both to AOSP and to Google Pixel devices as part of *Feature Drops* .

<br />

Although these updates don't include app-impacting API changes, we provide
images of the latest QPR beta builds so you can test your app with these builds
as needed (for example, if there are upcoming features that might impact the
user experience of your app).

To find OTA images for already-released, stable versions of the platform, see
[Full OTA Images for Nexus and Pixel Devices](https://developers.google.com/android/ota).

Applying an OTA image can help you recover a device that received an OTA update
for an Android 17 QPR beta build but wouldn't start up after the update was
installed. If you are trying to get Android 17 QPR1 on your device but
you aren't trying to recover from a failed OTA update, see [Get Android 17 QPR
beta builds](https://developer.android.com/about/versions/17/get-qpr) instead.


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

You can choose to [return to the latest public build](https://developer.android.com/about/versions/17/qpr2/download-ota#public) at any time.

<br />

> [!WARNING]
> **Warning:** Before applying an Android 17 OTA image, we strongly recommend that you [unlock the bootloader](https://source.android.com/docs/core/architecture/bootloader/locking_unlocking) on your device if possible. Unlocking the bootloader requires a full device reset that removes all user data on the device, so make sure to back up your data first.

### Device OTA Images

|---|---|
| **Release date** | September 24, 2026 |
| **Builds** | CP41.260831.007 |
| **Emulator support** | x86 (64-bit), ARM (v8-A) |
| **Security patch level** | 2026-08-05 |
| **Google Play services** | 26.28.33 |

| Device | Download Link and SHA-256 Checksum |
|---|---|
| Pixel 6a | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 QPR1 Beta" data-action="download" data-label="bluejay" data-modal-dialog-id="bluejay_ota_zip">bluejay_beta-ota-cp41.260831.007-3495fbaf.zip</button> `3495fbaf854078d98cf4d14c234a4592528ca93fd4896cec155bae597b60da4f` |
| Pixel 7 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 QPR1 Beta" data-action="download" data-label="panther" data-modal-dialog-id="panther_ota_zip">panther_beta-ota-cp41.260831.007-0015cf97.zip</button> `0015cf97fa759d4df0deb9f325f34390848dd44d8998eb32c4c6e815ea705fa2` |
| Pixel 7 Pro | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 QPR1 Beta" data-action="download" data-label="cheetah" data-modal-dialog-id="cheetah_ota_zip">cheetah_beta-ota-cp41.260831.007-c1cb6558.zip</button> `c1cb655879ac179682ba282362ad6ca3f8a026ec18cbe77f6066f025ab2af1bc` |
| Pixel 7a | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 QPR1 Beta" data-action="download" data-label="lynx" data-modal-dialog-id="lynx_ota_zip">lynx_beta-ota-cp41.260831.007-396c03b3.zip</button> `396c03b35488187f10b200bad0966dfc7ebf53be7e5bcb19c33f86104ef0f28f` |
| Pixel Fold | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 QPR1 Beta" data-action="download" data-label="felix" data-modal-dialog-id="felix_ota_zip">felix_beta-ota-cp41.260831.007-c3093a1b.zip</button> `c3093a1bed629a2e36e0646ea48f7799c0c0da05fcf236fab0943dc8751cbda4` |
| Pixel Tablet | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 QPR1 Beta" data-action="download" data-label="tangorpro" data-modal-dialog-id="tangorpro_ota_zip">tangorpro_beta-ota-cp41.260831.007-1c7506a5.zip</button> `1c7506a5e9d59db735a00aaff4ba25409e36a59cd802c1e6dbe293e8b624552e` |
| Pixel 8 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 QPR1 Beta" data-action="download" data-label="shiba" data-modal-dialog-id="shiba_ota_zip">shiba_beta-ota-cp41.260831.007-bb0baa1e.zip</button> `bb0baa1e25a5ef837fc966c45cfcce5f8d335726aaf6954e24545d4599cae2b2` |
| Pixel 8 Pro | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 QPR1 Beta" data-action="download" data-label="husky" data-modal-dialog-id="husky_ota_zip">husky_beta-ota-cp41.260831.007-1fd13c68.zip</button> `1fd13c68ba5379c74eeb8df1bf0409ecfc44dd61e1ee9af0cc219ab687d2d404` |
| Pixel 8a | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 QPR1 Beta" data-action="download" data-label="akita" data-modal-dialog-id="akita_ota_zip">akita_beta-ota-cp41.260831.007-b9cb7457.zip</button> `b9cb745753b4d89e6f6ba21a067d61d9e2a86c3cf6611917426e62edabcf7170` |
| Pixel 9 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 QPR1 Beta" data-action="download" data-label="tokay" data-modal-dialog-id="tokay_ota_zip">tokay_beta-ota-cp41.260831.007-9007a5b1.zip</button> `9007a5b13440594fcea7790c7621365e35cdd58c59a3feb74d38d20e5cfc7de9` |
| Pixel 9 Pro | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 QPR1 Beta" data-action="download" data-label="caiman" data-modal-dialog-id="caiman_ota_zip">caiman_beta-ota-cp41.260831.007-84233bc5.zip</button> `84233bc57d21ee0919c3b8c1237cf55d70098b7c0798c7686347317f2c1efd42` |
| Pixel 9 Pro XL | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 QPR1 Beta" data-action="download" data-label="komodo" data-modal-dialog-id="komodo_ota_zip">komodo_beta-ota-cp41.260831.007-3d0b0359.zip</button> `3d0b0359206fdfcbc3fb8d02ea617d28496242402e89e76b2130bd8f3d2b06f7` |
| Pixel 9 Pro Fold | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 QPR1 Beta" data-action="download" data-label="comet" data-modal-dialog-id="comet_ota_zip">comet_beta-ota-cp41.260831.007-384947b8.zip</button> `384947b84073a25bfecf0614c326ca0abf656c58e6c3ef813e9789254c5c65fb` |
| Pixel 9a | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 QPR1 Beta" data-action="download" data-label="tegu" data-modal-dialog-id="tegu_ota_zip">tegu_beta-ota-cp41.260831.007-77cfdc0f.zip</button> `77cfdc0f0c79929a22f31be5d523759c5f87ba7e992f762434f8c50526a086da` |
| Pixel 10 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 QPR1 Beta" data-action="download" data-label="frankel" data-modal-dialog-id="frankel_ota_zip">frankel_beta-ota-cp41.260831.007-6aaa3165.zip</button> `6aaa3165221d2ddc29b30dffee69cec2aa4ea11d036503f441e1857f940aae4f` |
| Pixel 10 Pro | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 QPR1 Beta" data-action="download" data-label="blazer" data-modal-dialog-id="blazer_ota_zip">blazer_beta-ota-cp41.260831.007-b43226be.zip</button> `b43226be2180f93e02dbfddb7a7e54cb5b945258b6a766c4fc4db3e93becb1a2` |
| Pixel 10 Pro XL | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 QPR1 Beta" data-action="download" data-label="mustang" data-modal-dialog-id="mustang_ota_zip">mustang_beta-ota-cp41.260831.007-3935e796.zip</button> `3935e796551aa1e68e44c05e57e2ab031ecbcd9429cc0f6b367d342a5b17b184` |
| Pixel 10 Pro Fold | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 QPR1 Beta" data-action="download" data-label="rango" data-modal-dialog-id="rango_ota_zip">rango_beta-ota-cp41.260831.007-2d722313.zip</button> `2d722313f7cf755520288ccd2d76bffd676c8eeb74dbd82bcb878b28a97cd076` |
| Pixel 10a | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Android 17 QPR1 Beta" data-action="download" data-label="stallion" data-modal-dialog-id="stallion_ota_zip">stallion_beta-ota-cp41.260831.007-94fcd0e3.zip</button> `94fcd0e3424d6d63f0da4f3fb6b9bca11ad5388b71fee92646cf4003faf75348` |

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

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 OTA system image </button> [Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/bluejay_beta-ota-cp41.260831.007-3495fbaf.zip)

*bluejay_beta-ota-cp41.260831.007-3495fbaf.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 OTA system image </button> [Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/panther_beta-ota-cp41.260831.007-0015cf97.zip)

*panther_beta-ota-cp41.260831.007-0015cf97.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 OTA system image </button> [Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/cheetah_beta-ota-cp41.260831.007-c1cb6558.zip)

*cheetah_beta-ota-cp41.260831.007-c1cb6558.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 OTA system image </button> [Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/lynx_beta-ota-cp41.260831.007-396c03b3.zip)

*lynx_beta-ota-cp41.260831.007-396c03b3.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 OTA system image </button> [Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/felix_beta-ota-cp41.260831.007-c3093a1b.zip)

*felix_beta-ota-cp41.260831.007-c3093a1b.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 OTA system image </button> [Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/tangorpro_beta-ota-cp41.260831.007-1c7506a5.zip)

*tangorpro_beta-ota-cp41.260831.007-1c7506a5.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 OTA system image </button> [Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/shiba_beta-ota-cp41.260831.007-bb0baa1e.zip)

*shiba_beta-ota-cp41.260831.007-bb0baa1e.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 OTA system image </button> [Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/husky_beta-ota-cp41.260831.007-1fd13c68.zip)

*husky_beta-ota-cp41.260831.007-1fd13c68.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 OTA system image </button> [Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/akita_beta-ota-cp41.260831.007-b9cb7457.zip)

*akita_beta-ota-cp41.260831.007-b9cb7457.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 OTA system image </button> [Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/tokay_beta-ota-cp41.260831.007-9007a5b1.zip)

*tokay_beta-ota-cp41.260831.007-9007a5b1.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 OTA system image </button> [Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/caiman_beta-ota-cp41.260831.007-84233bc5.zip)

*caiman_beta-ota-cp41.260831.007-84233bc5.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 OTA system image </button> [Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/komodo_beta-ota-cp41.260831.007-3d0b0359.zip)

*komodo_beta-ota-cp41.260831.007-3d0b0359.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 OTA system image </button> [Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/comet_beta-ota-cp41.260831.007-384947b8.zip)

*comet_beta-ota-cp41.260831.007-384947b8.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 OTA system image </button> [Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/tegu_beta-ota-cp41.260831.007-77cfdc0f.zip)

*tegu_beta-ota-cp41.260831.007-77cfdc0f.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 OTA system image </button> [Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/frankel_beta-ota-cp41.260831.007-6aaa3165.zip)

*frankel_beta-ota-cp41.260831.007-6aaa3165.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 OTA system image </button> [Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/blazer_beta-ota-cp41.260831.007-b43226be.zip)

*blazer_beta-ota-cp41.260831.007-b43226be.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 OTA system image </button> [Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/mustang_beta-ota-cp41.260831.007-3935e796.zip)

*mustang_beta-ota-cp41.260831.007-3935e796.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 OTA system image </button> [Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/rango_beta-ota-cp41.260831.007-2d722313.zip)

*rango_beta-ota-cp41.260831.007-2d722313.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  

All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  

Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  

WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 17 OTA system image </button> [Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/stallion_beta-ota-cp41.260831.007-94fcd0e3.zip)

*stallion_beta-ota-cp41.260831.007-94fcd0e3.zip*