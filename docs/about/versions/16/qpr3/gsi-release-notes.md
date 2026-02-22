---
title: https://developer.android.com/about/versions/16/qpr3/gsi-release-notes
url: https://developer.android.com/about/versions/16/qpr3/gsi-release-notes
source: md.txt
---

Android [Generic System Image (GSI)](https://developer.android.com/topic/generic-system-image) binaries are available to developers for
app testing and validation purposes on [supported Treble-compliant devices](https://developer.android.com/topic/generic-system-image#device-compliance).
Developers can use these images to address
any compatibility issues with Android 16 as well as discover and report OS and
framework issues until Android 16 is officially released.

GSI binaries for Android 16
QPR2 are built from the same AOSP and
GMS sources as the [corresponding Google Pixel builds](https://developer.android.com/about/versions/16/download). These binaries
contain the same API and SDK, have a similar CTS result, and have been validated
on the following Pixel devices:

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

See the [GSI documentation](https://developer.android.com/topic/generic-system-image) for device requirements, flashing instructions,
and more information on choosing the right image type for your device.
To find GSI binaries for already-released, stable versions
of the platform, see the [Generic System Image releases](https://developer.android.com/topic/generic-system-image/releases#16-stable) page.
| **Note:** [**File GSI bugs**](https://issuetracker.google.com/issues/new?component=1109161&template=1620756) for any system-related issues you encounter. Make sure to attach a full bug report and **clearly indicate that you are using a GSI
| build** in your bug description to help the Android team find your issues and address them more quickly. For app-related issues found when using a GSI, we recommend reproducing the issue on a Pixel device before contacting the app developer directly.

## General advisories

GSI binaries offer core OS and framework capabilities that are common to all
Android 16 QPR2
beta builds, but they might be missing specific capabilities as listed and are
not intended for general use.

Before you start using a GSI, review the following general advisories:

- GSI binaries are an experimental tool intended only for use by developers who want early access to test and validate their apps.
- Using a GSI might void the warranty for your device, erase all data on your device, and might make parts of your device unusable.
- Using a GSI requires a bootloader-unlocked, Treble-compliant device that originally launched with Android 9 (API level 28) or higher.
- Apps embedded in GSIs are for evaluation usage; some apps might not function as expected.
- GSI releases aren't [Compatibility Test Suite (CTS)](https://source.android.com/compatibility/cts/)-approved. Apps that depend on CTS-approved builds might not work normally.

## Install with Android Flash Tool

**Android Flash Tool** lets you securely flash a system image
to your supported Pixel device. Android Flash Tool works with any Web browser
that supports WebUSB, such as Chrome or Edge 79+.

Android Flash Tool guides you step-by-step through the process of flashing your
device---there's no need to have tools installed---but you do need to unlock your
device and [enable USB Debugging in Developer options](https://developer.android.com/studio/debug/dev-options#enable). For
complete instructions, see the [Android Flash Tool
documentation](https://source.android.com/setup/contribute/flash).

Connect your device over USB, then, depending on the type of system image you
want to flash, navigate to Android Flash Tool using one of the following links
and follow the onscreen guidance:

- **ARM64 GSI with GMS** : <https://flash.android.com/preview/baklava-qpr3-beta2.1-gsi-gms>
- **ARM64 GSI** : <https://flash.android.com/preview/baklava-qpr3-beta2.1-gsi>

## Known issues

Android 16 GSI binaries have the following GSI-specific known issues that might
occur with some devices and builds:

- **Power Cycle**: Rebooting GSI might fail on some devices. To work around it, reboot the device into recovery mode, erase user data, perform a factory reset, and then reboot the device.
- **System partition size** : GSI + GMS file size (images named `_gsi\_gms\_arm64-*_`) might be bigger than the default dynamic system partition size on your device. To work around this issue, you can delete some non-essential dynamic partitions, such as the product partition, and flash the GSI again. For more information, see the [flashing GSIs
  documentation](https://source.android.com/setup/build/gsi#flashing-gsis).

## Downloads

    Date: February 10, 2026
    Build: CP11.251209.009.A1
    Security patch level: January 2026
    Google Play Services: 25.47.33

| Type | Download Link and SHA-256 Checksum |
|---|---|
| ARM64+GMS | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="arm64-gms" data-modal-dialog-id="a16_qpr3_gms_arm64_GSI_zip">gsi_gms_arm64-exp-CP11.251209.009.A1-14840729-89298580.zip</button> `89298580dda1280efe32b27d04b9caf5bbe19061c3716635c0d2d11640acf292` |
| ARM64 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="arm64" data-modal-dialog-id="a16_qpr3_aosp_arm64_GSI_zip">aosp_arm64-exp-CP11.251209.009.A1-14840729-59a822d9.zip</button> `59a822d9a4dd09873009f40c4b97003a2f2dab1b284f2c56b0aaa63dde7e19dd` |
| x86_64+GMS | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="x86_64-gms" data-modal-dialog-id="a16_qpr3_gms_x86_64_GSI_zip">gsi_gms_x86_64-exp-CP11.251209.009.A1-14840729-37289f85.zip</button> `37289f85ddaebb1ce1147bdb75e9d47053737e71946833f524977f492b55e035` |
| x86_64 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="x86_64" data-modal-dialog-id="a16_qpr3_aosp_x86_64_GSI_zip">aosp_x86_64-exp-CP11.251209.009.A1-14840729-f96f7906.zip</button> `f96f7906d9638b8242c20fb9651ed322937ac5195ffa2ae3df01393ad089e594` |


### Download Android 16 GSI Release

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

This is the Early Access Google Mobile Services and Android 16 GSI License Agreement ("License Agreement"). Google Mobile Services and Android 16 GSI (each defined below) are licensed to you subject to the terms of the License Agreement. The License Agreement forms a legally binding contract between you and Google in relation to your use of Google Mobile Services and Android 16 GSI.  

### 1. Definitions

1.1 "Android" means the Android software stack for devices, as made available under the Android Open Source Project, which is located at the following URL: https://source.android.com/, as updated from time to time.  

1.2 "Android 16 GSI" means Google's generic system image of Android 16 code, excluding third party extensions.  

1.3 "Google" means Google LLC, a Delaware corporation with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, United States.  

1.4 "Google Mobile Services" means a machine-readable binary code version of the following Google applications: Search, Chrome, Gmail, Maps, YouTube, and Play, and certain other associated applications, in each case, as provided under this License Agreement. Google Mobile Services are collectively referred to in the License Agreement as "GMS" or each individually as a "GMS Application".  

1.5 "GMS+GSI" refers to GMS and Android 16 GSI, collectively.  

### 2. Accepting this License Agreement

2.1 In order to use GMS+GSI, you must first agree to the License Agreement. You may not use GMS+GSI if you do not accept the License Agreement.  

2.2 By clicking to accept, you hereby agree to the terms of the License Agreement.  

2.3 You may not use GMS+GSI and may not accept the License Agreement if you are a person barred from receiving GMS+GSI under the laws of the United States or other countries, including the country in which you are resident or from which you use GMS+GSI.  

2.4 If you are agreeing to be bound by the License Agreement on behalf of your employer or other entity, you represent and warrant that you have full legal authority to bind your employer or such entity to the License Agreement. If you do not have the requisite authority, you may not accept the License Agreement or use GMS+GSI on behalf of your employer or other entity.  

### 3. GMS+GSI License from Google

3.1 Subject to the terms of the License Agreement, Google grants you a limited, worldwide, royalty-free, non-assignable, non-exclusive, and non-sublicensable license to use GMS+GSI solely for testing applications for compatibility with Android 16.  

3.2 You agree that Google or third parties own all legal right, title and interest in and to GMS+GSI, including any Intellectual Property Rights that subsist in GMS+GSI. "Intellectual Property Rights" means any and all rights under patent law, copyright law, trade secret law, trademark law, and any and all other proprietary rights. Google reserves all rights not expressly granted to you.  

3.3 You may not use GMS+GSI for any purpose not expressly permitted by the License Agreement.  

3.4 Use, reproduction and distribution of components of GMS+GSI licensed under an open source software license are governed solely by the terms of that open source software license and not the License Agreement.  

3.5 You agree that the form and nature of GMS+GSI that Google provides may change without prior notice to you and that future versions of GMS+GSI may be incompatible with applications developed on previous versions of GMS+GSI. You agree that Google may stop (permanently or temporarily) providing GMS+GSI (or any features within GMS+GSI) to you or to users generally at Google's sole discretion, without prior notice to you.  

3.6 Nothing in the License Agreement gives you a right to use any of Google's trade names, trademarks, service marks, logos, domain names, or other distinctive brand features.  

3.7 You agree that you will not remove, obscure, or alter any proprietary rights notices (including copyright and trademark notices) that may be affixed to or contained within GMS+GSI.  

3.8 You agree that you will not, and will not encourage or allow any third party to do any of the following:  
(a) distribute GMS;  
(b) copy (except for backup purposes), modify or adapt any part of GMS+GSI;  
(c) disassemble, de-compile, or otherwise reverse engineer GMS+GSI, or any part of GMS+GSI, or obtain the source code or algorithms underlying GMS+GSI;  
(d) create derivative works from or based on GMS+GSI;  
(e) provide, sell, license, sublicense, lease, lend, or disclose GMS+GSI, or any part of GMS+GSI, to any third party,; or  
(f) ship, divert, transship, transfer, export, or re-export GMS+GSI, or any component thereof, into any country or use it in any manner prohibited by any applicable export control laws, restrictions, or regulations.  

### 4. Use of GMS+GSI by You

4.1 Google agrees that it obtains no right, title or interest from you (or your licensors) under the License Agreement in or to any software applications that you may develop using GMS+GSI, including any intellectual property rights that subsist in those applications.  

4.2 You agree to ensure that any applications you develop using GMS+GSI are compliant with applicable laws, regulations and generally accepted practices or guidelines in the relevant jurisdictions (including any laws regarding the export of data or software to and from the United States or other relevant countries).  

4.3 You agree that if you use GMS+GSI to develop applications for general public users, you will protect the privacy and legal rights of those users. If the users provide you with user names, passwords, or other login information or personal information, you must make the users aware that the information will be available to your application, and you must provide legally adequate privacy notice and protection for those users. If your application stores personal or sensitive information provided by users, it must do so securely. If the user provides your application with Google Account information, your application may only use that information to access the user's Google Account when, and for the limited purposes for which, the user has given you permission to do so.  

4.4 You agree that you will not engage in any activity with GMS+GSI, including the development or distribution of an application, that interferes with, disrupts, damages, or accesses in an unauthorized manner the servers, networks, or other properties or services of any third party including, but not limited to, Google or any mobile communications carrier.  

4.5 You agree that you are solely responsible for (and that Google has no responsibility to you or to any third party for) any data, content, or resources that you create, transmit or display through Android and/or applications for Android, and for the consequences of your actions (including any loss or damage which Google may suffer) by doing so.  

4.6 You agree that you are solely responsible for (and that Google has no responsibility to you or to any third party for) any breach of your obligations under the License Agreement, any applicable third party contract or Terms of Service, or any applicable law or regulation, and for the consequences (including any loss or damage which Google or any third party may suffer) of any such breach.  

4.7 You agree that you will not use GMS+GSI to develop applications that will do any of the following prohibited activities:  
(a) intentionally create, facilitate the creation of, or exploit any security vulnerabilities in an end user's device;  
(b) interfere with an end user's expected operation and use of that end user's device;  
(c) engage in an activity that violates any applicable law or regulation;  
(d) contain any viruses, worms, trojan horses, date bombs, time bombs or the like;  
(e) serve or otherwise place any advertisements during the launch process of Android or a GMS Application;  
(f) offer, download, or install any additional products during the launch process of Android or a GMS Application;  
(g) interfere with or limit the display or acceptance of the applicable Google Terms of Service for a GMS Application;  
(h) redirect an end user away from, block access to, frame, modify, or change the look or feel of any web page or web site accessed via a GMS Application, or place anything on or near any website page that in any way implies that Google is responsible for the contents of such page;  
(i) cause any GMS Application to cease operating, or to damage, interrupt, allow access to, or interfere with any GMS Application or end user data;  
(j) modify, or interfere with the operation of, Android or GMS; or  
(k) interfere with Google's over-the-air updates of GMS Applications.  

### 5. Terminating this License Agreement

5.1 The License Agreement will continue to apply until terminated by either you or Google as set out below.  

5.2 If you want to terminate the License Agreement, you may do so by ceasing your use of GMS+GSI.  

5.3 Google may at any time, terminate the License Agreement with you if:  
(A) you have breached any provision of the License Agreement; or  
(B) Google is required to do so by law; or  
(C) Google decides to no longer provide GMS+GSI in its sole discretion.  

5.4 When the License Agreement comes to an end:  
(A) all rights and licenses granted to you under this License Agreement will immediately cease;  
(B) you will destroy all copies of GMS+GSI in your possession, including from all hard disks and memory;  
(C) neither you nor Google will be liable to the other for any damages resulting solely from termination of this License Agreement; and  
(D) any provisions of this License Agreement that under their terms or by implication ought to survive, will survive any termination of this License Agreement. This specifically includes, without limitation, Sections 2.3, 2.4, 3.3, 3.7, 3.8, 4, 5, 6, 7, 8 and 10.  

### 6. DISCLAIMER OF WARRANTIES

6.1 YOU EXPRESSLY UNDERSTAND AND AGREE THAT YOUR USE OF GMS+GSI IS AT YOUR SOLE RISK AND THAT GMS+GSI IS PROVIDED "AS IS" AND "AS AVAILABLE" WITHOUT WARRANTY OF ANY KIND FROM GOOGLE.  
6.2 YOUR USE OF GMS+GSI AND ANY MATERIAL DOWNLOADED OR OTHERWISE OBTAINED THROUGH THE USE OF GMS+GSI IS AT YOUR OWN DISCRETION AND RISK AND YOU ARE SOLELY RESPONSIBLE FOR ANY ERRORS, DEFECTS, DESTRUCTION, DAMAGE OR LOSS RESULTING FROM SUCH USE, INCLUDING DAMAGE TO YOUR COMPUTER SYSTEM OR OTHER DEVICE, LOSS OF DATA, VOIDING OF THE MANUFACTURER WARRANTY OR INCREASED VULNERABILITY OF YOUR DEVICE OR COMPUTER SYSTEM.  

6.3 GOOGLE FURTHER EXPRESSLY DISCLAIMS ALL WARRANTIES AND CONDITIONS OF ANY KIND, WHETHER EXPRESS OR IMPLIED, INCLUDING, BUT NOT LIMITED TO THE IMPLIED WARRANTIES AND CONDITIONS OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT.  

### 7. LIMITATION OF LIABILITY

7.1 YOU EXPRESSLY UNDERSTAND AND AGREE THAT GOOGLE, ITS SUBSIDIARIES AND AFFILIATES, AND ITS LICENSORS SHALL NOT BE LIABLE TO YOU UNDER ANY THEORY OF LIABILITY FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, CONSEQUENTIAL OR EXEMPLARY DAMAGES THAT MAY BE INCURRED BY YOU, INCLUDING ANY LOSS OF DATA, WHETHER OR NOT GOOGLE OR ITS REPRESENTATIVES HAVE BEEN ADVISED OF OR SHOULD HAVE BEEN AWARE OF THE POSSIBILITY OF ANY SUCH LOSSES ARISING.  

### 8. Indemnification

8.1 To the maximum extent permitted by law, you agree to defend, indemnify and hold harmless Google, its affiliates and their respective directors, officers, employees and agents from and against any and all claims, actions, suits or proceedings, as well as any and all losses, liabilities, damages, costs and expenses (including reasonable attorneys fees) arising out of or accruing from (a) your use of GMS+GSI, or (b) any non-compliance by you with the License Agreement.  

### 9. Changes to the License Agreement

9.1 Google may make changes to the License Agreement as it distributes new versions of GMS+GSI. When these changes are made, Google will make a new version of the License Agreement available on the website where GMS+GSI is made available.  

### 10. General Legal Terms

10.1 The License Agreement constitutes the whole legal agreement between you and Google and governs your use of GMS+GSI (excluding any services which Google may provide to you under a separate written agreement), and completely replaces any prior agreements between you and Google in relation to GMS+GSI.  

10.2 You agree that if Google does not exercise or enforce any legal right or remedy which is contained in the License Agreement (or which Google has the benefit of under any applicable law), this will not be taken to be a formal waiver of Google's rights and that those rights or remedies will still be available to Google.  

10.3 If any court of law, having the jurisdiction to decide on this matter, rules that any provision of the License Agreement is invalid, then that provision will be removed from the License Agreement without affecting the rest of the License Agreement. The remaining provisions of the License Agreement will continue to be valid and enforceable.  

10.4 You acknowledge and agree that each member of the group of companies of which Google is the parent shall be third party beneficiaries to the License Agreement and that such other companies shall be entitled to directly enforce, and rely upon, any provision of the License Agreement that confers a benefit on (or rights in favor of) them. Other than this, no other person or company shall be third party beneficiaries to the License Agreement.  

10.5 EXPORT RESTRICTIONS. GMS+GSI IS SUBJECT TO UNITED STATES EXPORT LAWS AND REGULATIONS. YOU MUST COMPLY WITH ALL DOMESTIC AND INTERNATIONAL EXPORT LAWS AND REGULATIONS THAT APPLY TO GMS+GSI. THESE LAWS INCLUDE RESTRICTIONS ON DESTINATIONS, END USERS AND END USE.  

10.6 The rights granted in the License Agreement may not be assigned or transferred by either you or Google without the prior written approval of the other party. Neither you nor Google shall be permitted to delegate their responsibilities or obligations under the License Agreement without the prior written approval of the other party.  

10.7 The License Agreement, and your relationship with Google under the License Agreement, shall be governed by the laws of the State of California without regard to its conflict of laws provisions. You and Google agree to submit to the exclusive jurisdiction of the courts located within the county of Santa Clara, California to resolve any legal matter arising from the License Agreement. Notwithstanding this, you agree that Google shall still be allowed to apply for injunctive remedies (or an equivalent type of urgent legal relief) in any jurisdiction.  

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 GSI Release </button> [Download Android 16 GSI Release](https://dl.google.com/developers/android/baklava/images/gsi/gsi_gms_arm64-exp-CP11.251209.009.A1-14840729-89298580.zip)

*gsi_gms_arm64-exp-CP11.251209.009.A1-14840729-89298580.zip*

### Download Android 16 GSI Release

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

This is the Early Access Google Mobile Services and Android 16 GSI License Agreement ("License Agreement"). Google Mobile Services and Android 16 GSI (each defined below) are licensed to you subject to the terms of the License Agreement. The License Agreement forms a legally binding contract between you and Google in relation to your use of Google Mobile Services and Android 16 GSI.  

### 1. Definitions

1.1 "Android" means the Android software stack for devices, as made available under the Android Open Source Project, which is located at the following URL: https://source.android.com/, as updated from time to time.  

1.2 "Android 16 GSI" means Google's generic system image of Android 16 code, excluding third party extensions.  

1.3 "Google" means Google LLC, a Delaware corporation with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, United States.  

1.4 "Google Mobile Services" means a machine-readable binary code version of the following Google applications: Search, Chrome, Gmail, Maps, YouTube, and Play, and certain other associated applications, in each case, as provided under this License Agreement. Google Mobile Services are collectively referred to in the License Agreement as "GMS" or each individually as a "GMS Application".  

1.5 "GMS+GSI" refers to GMS and Android 16 GSI, collectively.  

### 2. Accepting this License Agreement

2.1 In order to use GMS+GSI, you must first agree to the License Agreement. You may not use GMS+GSI if you do not accept the License Agreement.  

2.2 By clicking to accept, you hereby agree to the terms of the License Agreement.  

2.3 You may not use GMS+GSI and may not accept the License Agreement if you are a person barred from receiving GMS+GSI under the laws of the United States or other countries, including the country in which you are resident or from which you use GMS+GSI.  

2.4 If you are agreeing to be bound by the License Agreement on behalf of your employer or other entity, you represent and warrant that you have full legal authority to bind your employer or such entity to the License Agreement. If you do not have the requisite authority, you may not accept the License Agreement or use GMS+GSI on behalf of your employer or other entity.  

### 3. GMS+GSI License from Google

3.1 Subject to the terms of the License Agreement, Google grants you a limited, worldwide, royalty-free, non-assignable, non-exclusive, and non-sublicensable license to use GMS+GSI solely for testing applications for compatibility with Android 16.  

3.2 You agree that Google or third parties own all legal right, title and interest in and to GMS+GSI, including any Intellectual Property Rights that subsist in GMS+GSI. "Intellectual Property Rights" means any and all rights under patent law, copyright law, trade secret law, trademark law, and any and all other proprietary rights. Google reserves all rights not expressly granted to you.  

3.3 You may not use GMS+GSI for any purpose not expressly permitted by the License Agreement.  

3.4 Use, reproduction and distribution of components of GMS+GSI licensed under an open source software license are governed solely by the terms of that open source software license and not the License Agreement.  

3.5 You agree that the form and nature of GMS+GSI that Google provides may change without prior notice to you and that future versions of GMS+GSI may be incompatible with applications developed on previous versions of GMS+GSI. You agree that Google may stop (permanently or temporarily) providing GMS+GSI (or any features within GMS+GSI) to you or to users generally at Google's sole discretion, without prior notice to you.  

3.6 Nothing in the License Agreement gives you a right to use any of Google's trade names, trademarks, service marks, logos, domain names, or other distinctive brand features.  

3.7 You agree that you will not remove, obscure, or alter any proprietary rights notices (including copyright and trademark notices) that may be affixed to or contained within GMS+GSI.  

3.8 You agree that you will not, and will not encourage or allow any third party to do any of the following:  
(a) distribute GMS;  
(b) copy (except for backup purposes), modify or adapt any part of GMS+GSI;  
(c) disassemble, de-compile, or otherwise reverse engineer GMS+GSI, or any part of GMS+GSI, or obtain the source code or algorithms underlying GMS+GSI;  
(d) create derivative works from or based on GMS+GSI;  
(e) provide, sell, license, sublicense, lease, lend, or disclose GMS+GSI, or any part of GMS+GSI, to any third party,; or  
(f) ship, divert, transship, transfer, export, or re-export GMS+GSI, or any component thereof, into any country or use it in any manner prohibited by any applicable export control laws, restrictions, or regulations.  

### 4. Use of GMS+GSI by You

4.1 Google agrees that it obtains no right, title or interest from you (or your licensors) under the License Agreement in or to any software applications that you may develop using GMS+GSI, including any intellectual property rights that subsist in those applications.  

4.2 You agree to ensure that any applications you develop using GMS+GSI are compliant with applicable laws, regulations and generally accepted practices or guidelines in the relevant jurisdictions (including any laws regarding the export of data or software to and from the United States or other relevant countries).  

4.3 You agree that if you use GMS+GSI to develop applications for general public users, you will protect the privacy and legal rights of those users. If the users provide you with user names, passwords, or other login information or personal information, you must make the users aware that the information will be available to your application, and you must provide legally adequate privacy notice and protection for those users. If your application stores personal or sensitive information provided by users, it must do so securely. If the user provides your application with Google Account information, your application may only use that information to access the user's Google Account when, and for the limited purposes for which, the user has given you permission to do so.  

4.4 You agree that you will not engage in any activity with GMS+GSI, including the development or distribution of an application, that interferes with, disrupts, damages, or accesses in an unauthorized manner the servers, networks, or other properties or services of any third party including, but not limited to, Google or any mobile communications carrier.  

4.5 You agree that you are solely responsible for (and that Google has no responsibility to you or to any third party for) any data, content, or resources that you create, transmit or display through Android and/or applications for Android, and for the consequences of your actions (including any loss or damage which Google may suffer) by doing so.  

4.6 You agree that you are solely responsible for (and that Google has no responsibility to you or to any third party for) any breach of your obligations under the License Agreement, any applicable third party contract or Terms of Service, or any applicable law or regulation, and for the consequences (including any loss or damage which Google or any third party may suffer) of any such breach.  

4.7 You agree that you will not use GMS+GSI to develop applications that will do any of the following prohibited activities:  
(a) intentionally create, facilitate the creation of, or exploit any security vulnerabilities in an end user's device;  
(b) interfere with an end user's expected operation and use of that end user's device;  
(c) engage in an activity that violates any applicable law or regulation;  
(d) contain any viruses, worms, trojan horses, date bombs, time bombs or the like;  
(e) serve or otherwise place any advertisements during the launch process of Android or a GMS Application;  
(f) offer, download, or install any additional products during the launch process of Android or a GMS Application;  
(g) interfere with or limit the display or acceptance of the applicable Google Terms of Service for a GMS Application;  
(h) redirect an end user away from, block access to, frame, modify, or change the look or feel of any web page or web site accessed via a GMS Application, or place anything on or near any website page that in any way implies that Google is responsible for the contents of such page;  
(i) cause any GMS Application to cease operating, or to damage, interrupt, allow access to, or interfere with any GMS Application or end user data;  
(j) modify, or interfere with the operation of, Android or GMS; or  
(k) interfere with Google's over-the-air updates of GMS Applications.  

### 5. Terminating this License Agreement

5.1 The License Agreement will continue to apply until terminated by either you or Google as set out below.  

5.2 If you want to terminate the License Agreement, you may do so by ceasing your use of GMS+GSI.  

5.3 Google may at any time, terminate the License Agreement with you if:  
(A) you have breached any provision of the License Agreement; or  
(B) Google is required to do so by law; or  
(C) Google decides to no longer provide GMS+GSI in its sole discretion.  

5.4 When the License Agreement comes to an end:  
(A) all rights and licenses granted to you under this License Agreement will immediately cease;  
(B) you will destroy all copies of GMS+GSI in your possession, including from all hard disks and memory;  
(C) neither you nor Google will be liable to the other for any damages resulting solely from termination of this License Agreement; and  
(D) any provisions of this License Agreement that under their terms or by implication ought to survive, will survive any termination of this License Agreement. This specifically includes, without limitation, Sections 2.3, 2.4, 3.3, 3.7, 3.8, 4, 5, 6, 7, 8 and 10.  

### 6. DISCLAIMER OF WARRANTIES

6.1 YOU EXPRESSLY UNDERSTAND AND AGREE THAT YOUR USE OF GMS+GSI IS AT YOUR SOLE RISK AND THAT GMS+GSI IS PROVIDED "AS IS" AND "AS AVAILABLE" WITHOUT WARRANTY OF ANY KIND FROM GOOGLE.  
6.2 YOUR USE OF GMS+GSI AND ANY MATERIAL DOWNLOADED OR OTHERWISE OBTAINED THROUGH THE USE OF GMS+GSI IS AT YOUR OWN DISCRETION AND RISK AND YOU ARE SOLELY RESPONSIBLE FOR ANY ERRORS, DEFECTS, DESTRUCTION, DAMAGE OR LOSS RESULTING FROM SUCH USE, INCLUDING DAMAGE TO YOUR COMPUTER SYSTEM OR OTHER DEVICE, LOSS OF DATA, VOIDING OF THE MANUFACTURER WARRANTY OR INCREASED VULNERABILITY OF YOUR DEVICE OR COMPUTER SYSTEM.  

6.3 GOOGLE FURTHER EXPRESSLY DISCLAIMS ALL WARRANTIES AND CONDITIONS OF ANY KIND, WHETHER EXPRESS OR IMPLIED, INCLUDING, BUT NOT LIMITED TO THE IMPLIED WARRANTIES AND CONDITIONS OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT.  

### 7. LIMITATION OF LIABILITY

7.1 YOU EXPRESSLY UNDERSTAND AND AGREE THAT GOOGLE, ITS SUBSIDIARIES AND AFFILIATES, AND ITS LICENSORS SHALL NOT BE LIABLE TO YOU UNDER ANY THEORY OF LIABILITY FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, CONSEQUENTIAL OR EXEMPLARY DAMAGES THAT MAY BE INCURRED BY YOU, INCLUDING ANY LOSS OF DATA, WHETHER OR NOT GOOGLE OR ITS REPRESENTATIVES HAVE BEEN ADVISED OF OR SHOULD HAVE BEEN AWARE OF THE POSSIBILITY OF ANY SUCH LOSSES ARISING.  

### 8. Indemnification

8.1 To the maximum extent permitted by law, you agree to defend, indemnify and hold harmless Google, its affiliates and their respective directors, officers, employees and agents from and against any and all claims, actions, suits or proceedings, as well as any and all losses, liabilities, damages, costs and expenses (including reasonable attorneys fees) arising out of or accruing from (a) your use of GMS+GSI, or (b) any non-compliance by you with the License Agreement.  

### 9. Changes to the License Agreement

9.1 Google may make changes to the License Agreement as it distributes new versions of GMS+GSI. When these changes are made, Google will make a new version of the License Agreement available on the website where GMS+GSI is made available.  

### 10. General Legal Terms

10.1 The License Agreement constitutes the whole legal agreement between you and Google and governs your use of GMS+GSI (excluding any services which Google may provide to you under a separate written agreement), and completely replaces any prior agreements between you and Google in relation to GMS+GSI.  

10.2 You agree that if Google does not exercise or enforce any legal right or remedy which is contained in the License Agreement (or which Google has the benefit of under any applicable law), this will not be taken to be a formal waiver of Google's rights and that those rights or remedies will still be available to Google.  

10.3 If any court of law, having the jurisdiction to decide on this matter, rules that any provision of the License Agreement is invalid, then that provision will be removed from the License Agreement without affecting the rest of the License Agreement. The remaining provisions of the License Agreement will continue to be valid and enforceable.  

10.4 You acknowledge and agree that each member of the group of companies of which Google is the parent shall be third party beneficiaries to the License Agreement and that such other companies shall be entitled to directly enforce, and rely upon, any provision of the License Agreement that confers a benefit on (or rights in favor of) them. Other than this, no other person or company shall be third party beneficiaries to the License Agreement.  

10.5 EXPORT RESTRICTIONS. GMS+GSI IS SUBJECT TO UNITED STATES EXPORT LAWS AND REGULATIONS. YOU MUST COMPLY WITH ALL DOMESTIC AND INTERNATIONAL EXPORT LAWS AND REGULATIONS THAT APPLY TO GMS+GSI. THESE LAWS INCLUDE RESTRICTIONS ON DESTINATIONS, END USERS AND END USE.  

10.6 The rights granted in the License Agreement may not be assigned or transferred by either you or Google without the prior written approval of the other party. Neither you nor Google shall be permitted to delegate their responsibilities or obligations under the License Agreement without the prior written approval of the other party.  

10.7 The License Agreement, and your relationship with Google under the License Agreement, shall be governed by the laws of the State of California without regard to its conflict of laws provisions. You and Google agree to submit to the exclusive jurisdiction of the courts located within the county of Santa Clara, California to resolve any legal matter arising from the License Agreement. Notwithstanding this, you agree that Google shall still be allowed to apply for injunctive remedies (or an equivalent type of urgent legal relief) in any jurisdiction.  

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 GSI Release </button> [Download Android 16 GSI Release](https://dl.google.com/developers/android/baklava/images/gsi/gsi_gms_x86_64-exp-CP11.251209.009.A1-14840729-37289f85.zip)

*gsi_gms_x86_64-exp-CP11.251209.009.A1-14840729-37289f85.zip*

### Download Android 16 GSI Release

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

This is the Early Access Google Mobile Services and Android 16 GSI License Agreement ("License Agreement"). Google Mobile Services and Android 16 GSI (each defined below) are licensed to you subject to the terms of the License Agreement. The License Agreement forms a legally binding contract between you and Google in relation to your use of Google Mobile Services and Android 16 GSI.  

### 1. Definitions

1.1 "Android" means the Android software stack for devices, as made available under the Android Open Source Project, which is located at the following URL: https://source.android.com/, as updated from time to time.  

1.2 "Android 16 GSI" means Google's generic system image of Android 16 code, excluding third party extensions.  

1.3 "Google" means Google LLC, a Delaware corporation with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, United States.  

1.4 "Google Mobile Services" means a machine-readable binary code version of the following Google applications: Search, Chrome, Gmail, Maps, YouTube, and Play, and certain other associated applications, in each case, as provided under this License Agreement. Google Mobile Services are collectively referred to in the License Agreement as "GMS" or each individually as a "GMS Application".  

1.5 "GMS+GSI" refers to GMS and Android 16 GSI, collectively.  

### 2. Accepting this License Agreement

2.1 In order to use GMS+GSI, you must first agree to the License Agreement. You may not use GMS+GSI if you do not accept the License Agreement.  

2.2 By clicking to accept, you hereby agree to the terms of the License Agreement.  

2.3 You may not use GMS+GSI and may not accept the License Agreement if you are a person barred from receiving GMS+GSI under the laws of the United States or other countries, including the country in which you are resident or from which you use GMS+GSI.  

2.4 If you are agreeing to be bound by the License Agreement on behalf of your employer or other entity, you represent and warrant that you have full legal authority to bind your employer or such entity to the License Agreement. If you do not have the requisite authority, you may not accept the License Agreement or use GMS+GSI on behalf of your employer or other entity.  

### 3. GMS+GSI License from Google

3.1 Subject to the terms of the License Agreement, Google grants you a limited, worldwide, royalty-free, non-assignable, non-exclusive, and non-sublicensable license to use GMS+GSI solely for testing applications for compatibility with Android 16.  

3.2 You agree that Google or third parties own all legal right, title and interest in and to GMS+GSI, including any Intellectual Property Rights that subsist in GMS+GSI. "Intellectual Property Rights" means any and all rights under patent law, copyright law, trade secret law, trademark law, and any and all other proprietary rights. Google reserves all rights not expressly granted to you.  

3.3 You may not use GMS+GSI for any purpose not expressly permitted by the License Agreement.  

3.4 Use, reproduction and distribution of components of GMS+GSI licensed under an open source software license are governed solely by the terms of that open source software license and not the License Agreement.  

3.5 You agree that the form and nature of GMS+GSI that Google provides may change without prior notice to you and that future versions of GMS+GSI may be incompatible with applications developed on previous versions of GMS+GSI. You agree that Google may stop (permanently or temporarily) providing GMS+GSI (or any features within GMS+GSI) to you or to users generally at Google's sole discretion, without prior notice to you.  

3.6 Nothing in the License Agreement gives you a right to use any of Google's trade names, trademarks, service marks, logos, domain names, or other distinctive brand features.  

3.7 You agree that you will not remove, obscure, or alter any proprietary rights notices (including copyright and trademark notices) that may be affixed to or contained within GMS+GSI.  

3.8 You agree that you will not, and will not encourage or allow any third party to do any of the following:  
(a) distribute GMS;  
(b) copy (except for backup purposes), modify or adapt any part of GMS+GSI;  
(c) disassemble, de-compile, or otherwise reverse engineer GMS+GSI, or any part of GMS+GSI, or obtain the source code or algorithms underlying GMS+GSI;  
(d) create derivative works from or based on GMS+GSI;  
(e) provide, sell, license, sublicense, lease, lend, or disclose GMS+GSI, or any part of GMS+GSI, to any third party,; or  
(f) ship, divert, transship, transfer, export, or re-export GMS+GSI, or any component thereof, into any country or use it in any manner prohibited by any applicable export control laws, restrictions, or regulations.  

### 4. Use of GMS+GSI by You

4.1 Google agrees that it obtains no right, title or interest from you (or your licensors) under the License Agreement in or to any software applications that you may develop using GMS+GSI, including any intellectual property rights that subsist in those applications.  

4.2 You agree to ensure that any applications you develop using GMS+GSI are compliant with applicable laws, regulations and generally accepted practices or guidelines in the relevant jurisdictions (including any laws regarding the export of data or software to and from the United States or other relevant countries).  

4.3 You agree that if you use GMS+GSI to develop applications for general public users, you will protect the privacy and legal rights of those users. If the users provide you with user names, passwords, or other login information or personal information, you must make the users aware that the information will be available to your application, and you must provide legally adequate privacy notice and protection for those users. If your application stores personal or sensitive information provided by users, it must do so securely. If the user provides your application with Google Account information, your application may only use that information to access the user's Google Account when, and for the limited purposes for which, the user has given you permission to do so.  

4.4 You agree that you will not engage in any activity with GMS+GSI, including the development or distribution of an application, that interferes with, disrupts, damages, or accesses in an unauthorized manner the servers, networks, or other properties or services of any third party including, but not limited to, Google or any mobile communications carrier.  

4.5 You agree that you are solely responsible for (and that Google has no responsibility to you or to any third party for) any data, content, or resources that you create, transmit or display through Android and/or applications for Android, and for the consequences of your actions (including any loss or damage which Google may suffer) by doing so.  

4.6 You agree that you are solely responsible for (and that Google has no responsibility to you or to any third party for) any breach of your obligations under the License Agreement, any applicable third party contract or Terms of Service, or any applicable law or regulation, and for the consequences (including any loss or damage which Google or any third party may suffer) of any such breach.  

4.7 You agree that you will not use GMS+GSI to develop applications that will do any of the following prohibited activities:  
(a) intentionally create, facilitate the creation of, or exploit any security vulnerabilities in an end user's device;  
(b) interfere with an end user's expected operation and use of that end user's device;  
(c) engage in an activity that violates any applicable law or regulation;  
(d) contain any viruses, worms, trojan horses, date bombs, time bombs or the like;  
(e) serve or otherwise place any advertisements during the launch process of Android or a GMS Application;  
(f) offer, download, or install any additional products during the launch process of Android or a GMS Application;  
(g) interfere with or limit the display or acceptance of the applicable Google Terms of Service for a GMS Application;  
(h) redirect an end user away from, block access to, frame, modify, or change the look or feel of any web page or web site accessed via a GMS Application, or place anything on or near any website page that in any way implies that Google is responsible for the contents of such page;  
(i) cause any GMS Application to cease operating, or to damage, interrupt, allow access to, or interfere with any GMS Application or end user data;  
(j) modify, or interfere with the operation of, Android or GMS; or  
(k) interfere with Google's over-the-air updates of GMS Applications.  

### 5. Terminating this License Agreement

5.1 The License Agreement will continue to apply until terminated by either you or Google as set out below.  

5.2 If you want to terminate the License Agreement, you may do so by ceasing your use of GMS+GSI.  

5.3 Google may at any time, terminate the License Agreement with you if:  
(A) you have breached any provision of the License Agreement; or  
(B) Google is required to do so by law; or  
(C) Google decides to no longer provide GMS+GSI in its sole discretion.  

5.4 When the License Agreement comes to an end:  
(A) all rights and licenses granted to you under this License Agreement will immediately cease;  
(B) you will destroy all copies of GMS+GSI in your possession, including from all hard disks and memory;  
(C) neither you nor Google will be liable to the other for any damages resulting solely from termination of this License Agreement; and  
(D) any provisions of this License Agreement that under their terms or by implication ought to survive, will survive any termination of this License Agreement. This specifically includes, without limitation, Sections 2.3, 2.4, 3.3, 3.7, 3.8, 4, 5, 6, 7, 8 and 10.  

### 6. DISCLAIMER OF WARRANTIES

6.1 YOU EXPRESSLY UNDERSTAND AND AGREE THAT YOUR USE OF GMS+GSI IS AT YOUR SOLE RISK AND THAT GMS+GSI IS PROVIDED "AS IS" AND "AS AVAILABLE" WITHOUT WARRANTY OF ANY KIND FROM GOOGLE.  
6.2 YOUR USE OF GMS+GSI AND ANY MATERIAL DOWNLOADED OR OTHERWISE OBTAINED THROUGH THE USE OF GMS+GSI IS AT YOUR OWN DISCRETION AND RISK AND YOU ARE SOLELY RESPONSIBLE FOR ANY ERRORS, DEFECTS, DESTRUCTION, DAMAGE OR LOSS RESULTING FROM SUCH USE, INCLUDING DAMAGE TO YOUR COMPUTER SYSTEM OR OTHER DEVICE, LOSS OF DATA, VOIDING OF THE MANUFACTURER WARRANTY OR INCREASED VULNERABILITY OF YOUR DEVICE OR COMPUTER SYSTEM.  

6.3 GOOGLE FURTHER EXPRESSLY DISCLAIMS ALL WARRANTIES AND CONDITIONS OF ANY KIND, WHETHER EXPRESS OR IMPLIED, INCLUDING, BUT NOT LIMITED TO THE IMPLIED WARRANTIES AND CONDITIONS OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT.  

### 7. LIMITATION OF LIABILITY

7.1 YOU EXPRESSLY UNDERSTAND AND AGREE THAT GOOGLE, ITS SUBSIDIARIES AND AFFILIATES, AND ITS LICENSORS SHALL NOT BE LIABLE TO YOU UNDER ANY THEORY OF LIABILITY FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, CONSEQUENTIAL OR EXEMPLARY DAMAGES THAT MAY BE INCURRED BY YOU, INCLUDING ANY LOSS OF DATA, WHETHER OR NOT GOOGLE OR ITS REPRESENTATIVES HAVE BEEN ADVISED OF OR SHOULD HAVE BEEN AWARE OF THE POSSIBILITY OF ANY SUCH LOSSES ARISING.  

### 8. Indemnification

8.1 To the maximum extent permitted by law, you agree to defend, indemnify and hold harmless Google, its affiliates and their respective directors, officers, employees and agents from and against any and all claims, actions, suits or proceedings, as well as any and all losses, liabilities, damages, costs and expenses (including reasonable attorneys fees) arising out of or accruing from (a) your use of GMS+GSI, or (b) any non-compliance by you with the License Agreement.  

### 9. Changes to the License Agreement

9.1 Google may make changes to the License Agreement as it distributes new versions of GMS+GSI. When these changes are made, Google will make a new version of the License Agreement available on the website where GMS+GSI is made available.  

### 10. General Legal Terms

10.1 The License Agreement constitutes the whole legal agreement between you and Google and governs your use of GMS+GSI (excluding any services which Google may provide to you under a separate written agreement), and completely replaces any prior agreements between you and Google in relation to GMS+GSI.  

10.2 You agree that if Google does not exercise or enforce any legal right or remedy which is contained in the License Agreement (or which Google has the benefit of under any applicable law), this will not be taken to be a formal waiver of Google's rights and that those rights or remedies will still be available to Google.  

10.3 If any court of law, having the jurisdiction to decide on this matter, rules that any provision of the License Agreement is invalid, then that provision will be removed from the License Agreement without affecting the rest of the License Agreement. The remaining provisions of the License Agreement will continue to be valid and enforceable.  

10.4 You acknowledge and agree that each member of the group of companies of which Google is the parent shall be third party beneficiaries to the License Agreement and that such other companies shall be entitled to directly enforce, and rely upon, any provision of the License Agreement that confers a benefit on (or rights in favor of) them. Other than this, no other person or company shall be third party beneficiaries to the License Agreement.  

10.5 EXPORT RESTRICTIONS. GMS+GSI IS SUBJECT TO UNITED STATES EXPORT LAWS AND REGULATIONS. YOU MUST COMPLY WITH ALL DOMESTIC AND INTERNATIONAL EXPORT LAWS AND REGULATIONS THAT APPLY TO GMS+GSI. THESE LAWS INCLUDE RESTRICTIONS ON DESTINATIONS, END USERS AND END USE.  

10.6 The rights granted in the License Agreement may not be assigned or transferred by either you or Google without the prior written approval of the other party. Neither you nor Google shall be permitted to delegate their responsibilities or obligations under the License Agreement without the prior written approval of the other party.  

10.7 The License Agreement, and your relationship with Google under the License Agreement, shall be governed by the laws of the State of California without regard to its conflict of laws provisions. You and Google agree to submit to the exclusive jurisdiction of the courts located within the county of Santa Clara, California to resolve any legal matter arising from the License Agreement. Notwithstanding this, you agree that Google shall still be allowed to apply for injunctive remedies (or an equivalent type of urgent legal relief) in any jurisdiction.  

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 GSI Release </button> [Download Android 16 GSI Release](https://dl.google.com/developers/android/baklava/images/gsi/aosp_arm64-exp-CP11.251209.009.A1-14840729-59a822d9.zip)

*aosp_arm64-exp-CP11.251209.009.A1-14840729-59a822d9.zip*

### Download Android 16 GSI Release

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

This is the Early Access Google Mobile Services and Android 16 GSI License Agreement ("License Agreement"). Google Mobile Services and Android 16 GSI (each defined below) are licensed to you subject to the terms of the License Agreement. The License Agreement forms a legally binding contract between you and Google in relation to your use of Google Mobile Services and Android 16 GSI.  

### 1. Definitions

1.1 "Android" means the Android software stack for devices, as made available under the Android Open Source Project, which is located at the following URL: https://source.android.com/, as updated from time to time.  

1.2 "Android 16 GSI" means Google's generic system image of Android 16 code, excluding third party extensions.  

1.3 "Google" means Google LLC, a Delaware corporation with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, United States.  

1.4 "Google Mobile Services" means a machine-readable binary code version of the following Google applications: Search, Chrome, Gmail, Maps, YouTube, and Play, and certain other associated applications, in each case, as provided under this License Agreement. Google Mobile Services are collectively referred to in the License Agreement as "GMS" or each individually as a "GMS Application".  

1.5 "GMS+GSI" refers to GMS and Android 16 GSI, collectively.  

### 2. Accepting this License Agreement

2.1 In order to use GMS+GSI, you must first agree to the License Agreement. You may not use GMS+GSI if you do not accept the License Agreement.  

2.2 By clicking to accept, you hereby agree to the terms of the License Agreement.  

2.3 You may not use GMS+GSI and may not accept the License Agreement if you are a person barred from receiving GMS+GSI under the laws of the United States or other countries, including the country in which you are resident or from which you use GMS+GSI.  

2.4 If you are agreeing to be bound by the License Agreement on behalf of your employer or other entity, you represent and warrant that you have full legal authority to bind your employer or such entity to the License Agreement. If you do not have the requisite authority, you may not accept the License Agreement or use GMS+GSI on behalf of your employer or other entity.  

### 3. GMS+GSI License from Google

3.1 Subject to the terms of the License Agreement, Google grants you a limited, worldwide, royalty-free, non-assignable, non-exclusive, and non-sublicensable license to use GMS+GSI solely for testing applications for compatibility with Android 16.  

3.2 You agree that Google or third parties own all legal right, title and interest in and to GMS+GSI, including any Intellectual Property Rights that subsist in GMS+GSI. "Intellectual Property Rights" means any and all rights under patent law, copyright law, trade secret law, trademark law, and any and all other proprietary rights. Google reserves all rights not expressly granted to you.  

3.3 You may not use GMS+GSI for any purpose not expressly permitted by the License Agreement.  

3.4 Use, reproduction and distribution of components of GMS+GSI licensed under an open source software license are governed solely by the terms of that open source software license and not the License Agreement.  

3.5 You agree that the form and nature of GMS+GSI that Google provides may change without prior notice to you and that future versions of GMS+GSI may be incompatible with applications developed on previous versions of GMS+GSI. You agree that Google may stop (permanently or temporarily) providing GMS+GSI (or any features within GMS+GSI) to you or to users generally at Google's sole discretion, without prior notice to you.  

3.6 Nothing in the License Agreement gives you a right to use any of Google's trade names, trademarks, service marks, logos, domain names, or other distinctive brand features.  

3.7 You agree that you will not remove, obscure, or alter any proprietary rights notices (including copyright and trademark notices) that may be affixed to or contained within GMS+GSI.  

3.8 You agree that you will not, and will not encourage or allow any third party to do any of the following:  
(a) distribute GMS;  
(b) copy (except for backup purposes), modify or adapt any part of GMS+GSI;  
(c) disassemble, de-compile, or otherwise reverse engineer GMS+GSI, or any part of GMS+GSI, or obtain the source code or algorithms underlying GMS+GSI;  
(d) create derivative works from or based on GMS+GSI;  
(e) provide, sell, license, sublicense, lease, lend, or disclose GMS+GSI, or any part of GMS+GSI, to any third party,; or  
(f) ship, divert, transship, transfer, export, or re-export GMS+GSI, or any component thereof, into any country or use it in any manner prohibited by any applicable export control laws, restrictions, or regulations.  

### 4. Use of GMS+GSI by You

4.1 Google agrees that it obtains no right, title or interest from you (or your licensors) under the License Agreement in or to any software applications that you may develop using GMS+GSI, including any intellectual property rights that subsist in those applications.  

4.2 You agree to ensure that any applications you develop using GMS+GSI are compliant with applicable laws, regulations and generally accepted practices or guidelines in the relevant jurisdictions (including any laws regarding the export of data or software to and from the United States or other relevant countries).  

4.3 You agree that if you use GMS+GSI to develop applications for general public users, you will protect the privacy and legal rights of those users. If the users provide you with user names, passwords, or other login information or personal information, you must make the users aware that the information will be available to your application, and you must provide legally adequate privacy notice and protection for those users. If your application stores personal or sensitive information provided by users, it must do so securely. If the user provides your application with Google Account information, your application may only use that information to access the user's Google Account when, and for the limited purposes for which, the user has given you permission to do so.  

4.4 You agree that you will not engage in any activity with GMS+GSI, including the development or distribution of an application, that interferes with, disrupts, damages, or accesses in an unauthorized manner the servers, networks, or other properties or services of any third party including, but not limited to, Google or any mobile communications carrier.  

4.5 You agree that you are solely responsible for (and that Google has no responsibility to you or to any third party for) any data, content, or resources that you create, transmit or display through Android and/or applications for Android, and for the consequences of your actions (including any loss or damage which Google may suffer) by doing so.  

4.6 You agree that you are solely responsible for (and that Google has no responsibility to you or to any third party for) any breach of your obligations under the License Agreement, any applicable third party contract or Terms of Service, or any applicable law or regulation, and for the consequences (including any loss or damage which Google or any third party may suffer) of any such breach.  

4.7 You agree that you will not use GMS+GSI to develop applications that will do any of the following prohibited activities:  
(a) intentionally create, facilitate the creation of, or exploit any security vulnerabilities in an end user's device;  
(b) interfere with an end user's expected operation and use of that end user's device;  
(c) engage in an activity that violates any applicable law or regulation;  
(d) contain any viruses, worms, trojan horses, date bombs, time bombs or the like;  
(e) serve or otherwise place any advertisements during the launch process of Android or a GMS Application;  
(f) offer, download, or install any additional products during the launch process of Android or a GMS Application;  
(g) interfere with or limit the display or acceptance of the applicable Google Terms of Service for a GMS Application;  
(h) redirect an end user away from, block access to, frame, modify, or change the look or feel of any web page or web site accessed via a GMS Application, or place anything on or near any website page that in any way implies that Google is responsible for the contents of such page;  
(i) cause any GMS Application to cease operating, or to damage, interrupt, allow access to, or interfere with any GMS Application or end user data;  
(j) modify, or interfere with the operation of, Android or GMS; or  
(k) interfere with Google's over-the-air updates of GMS Applications.  

### 5. Terminating this License Agreement

5.1 The License Agreement will continue to apply until terminated by either you or Google as set out below.  

5.2 If you want to terminate the License Agreement, you may do so by ceasing your use of GMS+GSI.  

5.3 Google may at any time, terminate the License Agreement with you if:  
(A) you have breached any provision of the License Agreement; or  
(B) Google is required to do so by law; or  
(C) Google decides to no longer provide GMS+GSI in its sole discretion.  

5.4 When the License Agreement comes to an end:  
(A) all rights and licenses granted to you under this License Agreement will immediately cease;  
(B) you will destroy all copies of GMS+GSI in your possession, including from all hard disks and memory;  
(C) neither you nor Google will be liable to the other for any damages resulting solely from termination of this License Agreement; and  
(D) any provisions of this License Agreement that under their terms or by implication ought to survive, will survive any termination of this License Agreement. This specifically includes, without limitation, Sections 2.3, 2.4, 3.3, 3.7, 3.8, 4, 5, 6, 7, 8 and 10.  

### 6. DISCLAIMER OF WARRANTIES

6.1 YOU EXPRESSLY UNDERSTAND AND AGREE THAT YOUR USE OF GMS+GSI IS AT YOUR SOLE RISK AND THAT GMS+GSI IS PROVIDED "AS IS" AND "AS AVAILABLE" WITHOUT WARRANTY OF ANY KIND FROM GOOGLE.  
6.2 YOUR USE OF GMS+GSI AND ANY MATERIAL DOWNLOADED OR OTHERWISE OBTAINED THROUGH THE USE OF GMS+GSI IS AT YOUR OWN DISCRETION AND RISK AND YOU ARE SOLELY RESPONSIBLE FOR ANY ERRORS, DEFECTS, DESTRUCTION, DAMAGE OR LOSS RESULTING FROM SUCH USE, INCLUDING DAMAGE TO YOUR COMPUTER SYSTEM OR OTHER DEVICE, LOSS OF DATA, VOIDING OF THE MANUFACTURER WARRANTY OR INCREASED VULNERABILITY OF YOUR DEVICE OR COMPUTER SYSTEM.  

6.3 GOOGLE FURTHER EXPRESSLY DISCLAIMS ALL WARRANTIES AND CONDITIONS OF ANY KIND, WHETHER EXPRESS OR IMPLIED, INCLUDING, BUT NOT LIMITED TO THE IMPLIED WARRANTIES AND CONDITIONS OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT.  

### 7. LIMITATION OF LIABILITY

7.1 YOU EXPRESSLY UNDERSTAND AND AGREE THAT GOOGLE, ITS SUBSIDIARIES AND AFFILIATES, AND ITS LICENSORS SHALL NOT BE LIABLE TO YOU UNDER ANY THEORY OF LIABILITY FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, CONSEQUENTIAL OR EXEMPLARY DAMAGES THAT MAY BE INCURRED BY YOU, INCLUDING ANY LOSS OF DATA, WHETHER OR NOT GOOGLE OR ITS REPRESENTATIVES HAVE BEEN ADVISED OF OR SHOULD HAVE BEEN AWARE OF THE POSSIBILITY OF ANY SUCH LOSSES ARISING.  

### 8. Indemnification

8.1 To the maximum extent permitted by law, you agree to defend, indemnify and hold harmless Google, its affiliates and their respective directors, officers, employees and agents from and against any and all claims, actions, suits or proceedings, as well as any and all losses, liabilities, damages, costs and expenses (including reasonable attorneys fees) arising out of or accruing from (a) your use of GMS+GSI, or (b) any non-compliance by you with the License Agreement.  

### 9. Changes to the License Agreement

9.1 Google may make changes to the License Agreement as it distributes new versions of GMS+GSI. When these changes are made, Google will make a new version of the License Agreement available on the website where GMS+GSI is made available.  

### 10. General Legal Terms

10.1 The License Agreement constitutes the whole legal agreement between you and Google and governs your use of GMS+GSI (excluding any services which Google may provide to you under a separate written agreement), and completely replaces any prior agreements between you and Google in relation to GMS+GSI.  

10.2 You agree that if Google does not exercise or enforce any legal right or remedy which is contained in the License Agreement (or which Google has the benefit of under any applicable law), this will not be taken to be a formal waiver of Google's rights and that those rights or remedies will still be available to Google.  

10.3 If any court of law, having the jurisdiction to decide on this matter, rules that any provision of the License Agreement is invalid, then that provision will be removed from the License Agreement without affecting the rest of the License Agreement. The remaining provisions of the License Agreement will continue to be valid and enforceable.  

10.4 You acknowledge and agree that each member of the group of companies of which Google is the parent shall be third party beneficiaries to the License Agreement and that such other companies shall be entitled to directly enforce, and rely upon, any provision of the License Agreement that confers a benefit on (or rights in favor of) them. Other than this, no other person or company shall be third party beneficiaries to the License Agreement.  

10.5 EXPORT RESTRICTIONS. GMS+GSI IS SUBJECT TO UNITED STATES EXPORT LAWS AND REGULATIONS. YOU MUST COMPLY WITH ALL DOMESTIC AND INTERNATIONAL EXPORT LAWS AND REGULATIONS THAT APPLY TO GMS+GSI. THESE LAWS INCLUDE RESTRICTIONS ON DESTINATIONS, END USERS AND END USE.  

10.6 The rights granted in the License Agreement may not be assigned or transferred by either you or Google without the prior written approval of the other party. Neither you nor Google shall be permitted to delegate their responsibilities or obligations under the License Agreement without the prior written approval of the other party.  

10.7 The License Agreement, and your relationship with Google under the License Agreement, shall be governed by the laws of the State of California without regard to its conflict of laws provisions. You and Google agree to submit to the exclusive jurisdiction of the courts located within the county of Santa Clara, California to resolve any legal matter arising from the License Agreement. Notwithstanding this, you agree that Google shall still be allowed to apply for injunctive remedies (or an equivalent type of urgent legal relief) in any jurisdiction.  

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 GSI Release </button> [Download Android 16 GSI Release](https://dl.google.com/developers/android/baklava/images/gsi/aosp_x86_64-exp-CP11.251209.009.A1-14840729-f96f7906.zip)

*aosp_x86_64-exp-CP11.251209.009.A1-14840729-f96f7906.zip*