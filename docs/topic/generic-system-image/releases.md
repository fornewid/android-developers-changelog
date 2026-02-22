---
title: https://developer.android.com/topic/generic-system-image/releases
url: https://developer.android.com/topic/generic-system-image/releases
source: md.txt
---

![](https://developer.android.com/static/images/lockups/android-stacked.svg)

Android Generic System Images (GSIs) are for app developers to perform app
validation and for development purposes. You shouldn't redistribute GSIs or use
them in any other way except as specifically set forth in the license terms
enclosed in each individual download.

For more information about GSI device requirements, risks, and installation
instructions, refer to the [GSI documentation page](https://developer.android.com/topic/generic-system-image).

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

- Android 16 QPR3 (Beta)
  - **ARM64 GSI with GMS** : <https://flash.android.com/preview/baklava-qpr3-beta2.1-gsi-gms>
  - **ARM64 GSI** : <https://flash.android.com/preview/baklava-qpr3-beta2.1-gsi>
- Android 16 QPR2 (stable release)
  - **ARM64 GSI with GMS** : <https://flash.android.com/preview/baklava-qpr2-gsi-gms>
  - **ARM64 GSI** : <https://flash.android.com/preview/baklava-qpr2-gsi>
- Android 16 QPR1 (stable release)
  - **ARM64 GSI with GMS** : <https://flash.android.com/preview/baklava-qpr1-gsi-gms>
  - **ARM64 GSI** : <https://flash.android.com/preview/baklava-qpr1-gsi>
- Android 16 (stable release)
  - **ARM64 GSI with GMS** : <https://flash.android.com/preview/baklava-gsi-gms>
  - **ARM64 GSI** : <https://flash.android.com/preview/baklava-gsi>
- Android 15 QPR2 (stable release)
  - **ARM64 GSI with GMS** : <https://flash.android.com/preview/vic-qpr2-gsi-gms>
  - **ARM64 GSI** : <https://flash.android.com/preview/vic-qpr2-gsi>
- Android 15 QPR1 (stable release)
  - **ARM64 GSI with GMS** : <https://flash.android.com/preview/vic-qpr1-gsi-gms>
  - **ARM64 GSI** : <https://flash.android.com/preview/vic-qpr1-gsi>
- Android 15 initial release
  - **ARM64 GSI with GMS** : <https://flash.android.com/preview/vic-gsi-gms>
  - **ARM64 GSI** : <https://flash.android.com/preview/vic-gsi>
- Android 14 QPR1
  - **ARM64 GSI with GMS** : <https://flash.android.com/preview/udc-qpr-gsi-gms>
  - **ARM64 GSI** : <https://flash.android.com/preview/udc-qpr-gsi>
- Android 14 (initial, stable release)
  - **ARM64 GSI with GMS** : <https://flash.android.com/preview/udc-gsi-gms>
  - **ARM64 GSI** : <https://flash.android.com/preview/udc-gsi>
- Android 13 QPR3
  - **ARM64 GSI with GMS** : <https://flash.android.com/preview/tm-qpr3-gsi-gms>
  - **ARM64 GSI** : <https://flash.android.com/preview/tm-qpr3-gsi>

## Android 16 GSIs

See the following sections.

### Android 16 QPR3 (Beta)

GSI binaries for Android 16 QPR3 Beta are built from the same AOSP and GMS
sources as the [corresponding Google Pixel builds](https://developer.android.com/about/versions/16/get).
These binaries contain the same API and SDK, have a similar CTS result, and have
been validated on the following Pixel devices:

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

### Android 16 QPR2

GSI binaries for Android 16 QPR2 are built from the same AOSP and GMS
sources as the [corresponding Google Pixel builds](https://developer.android.com/about/versions/16/get).
These binaries contain the same API and SDK, have a similar CTS result, and have
been validated on the following Pixel devices:

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

    Date: December 2, 2025
    Build: BP4A.251205.006
    Security patch level: December 2025
    Google Play Services: 25.34.34

| Type | Download Link and SHA-256 Checksum |
|---|---|
| ARM64+GMS | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="arm64-gms" data-modal-dialog-id="a16_qpr2_stable_gms_arm64_GSI_zip">gsi_gms_arm64-exp-BP4A.251205.006-14401865-f8760221.zip</button> `f87602213d71f1eda90cbd3e6089cea28563d110e4ef3f70b748b2b111d4ecce` |
| ARM64 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="arm64" data-modal-dialog-id="a16_qpr2_stable_aosp_arm64_GSI_zip">aosp_arm64-exp-BP4A.251205.006-14401865-2171cf0e.zip</button> `2171cf0ea849f8eaa399f4bad2165fab80b0fd9e98d37723a705dca6c41e49ea` |
| x86_64+GMS | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="x86_64-gms" data-modal-dialog-id="a16_qpr2_stable_gms_x86_64_GSI_zip">gsi_gms_x86_64-exp-BP4A.251205.006-14401865-b41f700e.zip</button> `b41f700ef3b9d1479cdbabb73b0a4862cf91fcd9471d08cfdb7e3c7a81f37f29` |
| x86_64 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="x86_64" data-modal-dialog-id="a16_qpr2_stable_aosp_x86_64_GSI_zip">aosp_x86_64-exp-BP4A.251205.006-14401865-aa5d832e.zip</button> `aa5d832edfb7e4c05138b459b21a219039048f65bc103ac38e25e410fa561512` |


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

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 GSI Release </button> [Download Android 16 GSI Release](https://dl.google.com/developers/android/baklava/images/gsi/gsi_gms_arm64-exp-BP4A.251205.006-14401865-f8760221.zip)

*gsi_gms_arm64-exp-BP4A.251205.006-14401865-f8760221.zip*

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

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 GSI Release </button> [Download Android 16 GSI Release](https://dl.google.com/developers/android/baklava/images/gsi/gsi_gms_x86_64-exp-BP4A.251205.006-14401865-b41f700e.zip)

*gsi_gms_x86_64-exp-BP4A.251205.006-14401865-b41f700e.zip*

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

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 GSI Release </button> [Download Android 16 GSI Release](https://dl.google.com/developers/android/baklava/images/gsi/aosp_arm64-exp-BP4A.251205.006-14401865-2171cf0e.zip)

*aosp_arm64-exp-BP4A.251205.006-14401865-2171cf0e.zip*

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

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 GSI Release </button> [Download Android 16 GSI Release](https://dl.google.com/developers/android/baklava/images/gsi/aosp_x86_64-exp-BP4A.251205.006-14401865-aa5d832e.zip)

*aosp_x86_64-exp-BP4A.251205.006-14401865-aa5d832e.zip*

### Android 16 QPR1

GSI binaries for Android 16 QPR1 are built from the same AOSP and GMS
sources as the [corresponding Google Pixel builds](https://developer.android.com/about/versions/16/get).
These binaries contain the same API and SDK, have a similar CTS result, and have
been validated on the following Pixel devices:

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

    Date: September 3, 2025
    Build: BP3A.250905.014
    Security patch level: September 2025
    Google Play Services: 25.20.39

| Type | Download Link and SHA-256 Checksum |
|---|---|
| ARM64+GMS | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="arm64-gms" data-modal-dialog-id="a16_qpr1_stable_gms_arm64_GSI_zip">gsi_gms_arm64-exp-BP3A.250905.014-13873947-346aad89.zip</button> `346aad891dfc0588d655dd2300e3d2297ebffe22b181a02538c4396b6e5975dd` |
| ARM64 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="arm64" data-modal-dialog-id="a16_qpr1_stable_aosp_arm64_GSI_zip">aosp_arm64-exp-BP3A.250905.014-13873947-f9b599ff.zip</button> `f9b599ff32b5bb574575b8a33ee17ff1d3354c9482b72fb10e2d13c16c0e12bb` |
| x86_64+GMS | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="x86_64-gms" data-modal-dialog-id="a16_qpr1_stable_gms_x86_64_GSI_zip">gsi_gms_x86_64-exp-BP3A.250905.014-13873947-7566270d.zip</button> `7566270d0150753cdf9d3f798286e24da03176542a82faf48500e34c335ad806` |
| x86_64 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="x86_64" data-modal-dialog-id="a16_qpr1_stable_aosp_x86_64_GSI_zip">aosp_x86_64-exp-BP3A.250905.014-13873947-9485bc07.zip</button> `9485bc07ee64e8bcdaa28de08b04b420f484ae1605fcb65ad4eca57efb9a9606` |


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

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 GSI Release </button> [Download Android 16 GSI Release](https://dl.google.com/developers/android/baklava/images/gsi/gsi_gms_arm64-exp-BP3A.250905.014-13873947-346aad89.zip)

*gsi_gms_arm64-exp-BP3A.250905.014-13873947-346aad89.zip*

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

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 GSI Release </button> [Download Android 16 GSI Release](https://dl.google.com/developers/android/baklava/images/gsi/gsi_gms_x86_64-exp-BP3A.250905.014-13873947-7566270d.zip)

*gsi_gms_x86_64-exp-BP3A.250905.014-13873947-7566270d.zip*

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

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 GSI Release </button> [Download Android 16 GSI Release](https://dl.google.com/developers/android/baklava/images/gsi/aosp_arm64-exp-BP3A.250905.014-13873947-f9b599ff.zip)

*aosp_arm64-exp-BP3A.250905.014-13873947-f9b599ff.zip*

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

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 GSI Release </button> [Download Android 16 GSI Release](https://dl.google.com/developers/android/baklava/images/gsi/aosp_x86_64-exp-BP3A.250905.014-13873947-9485bc07.zip)

*aosp_x86_64-exp-BP3A.250905.014-13873947-9485bc07.zip*

### Android 16 (initial release)

GSI binaries for Android 16 are built from the same AOSP and GMS
sources as the [corresponding Google Pixel builds](https://developer.android.com/about/versions/16/get).
These binaries contain the same API and SDK, have a similar CTS result, and have
been validated on the following Pixel devices:

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

    Date: June 3, 2025
    Build: BP2A.250605.031.A3
    Security patch level: June 2025
    Google Play Services: 25.08.34

| Type | Download Link and SHA-256 Checksum |
|---|---|
| ARM64+GMS | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="arm64-gms" data-modal-dialog-id="a16_stable_gms_arm64_GSI_zip">gsi_gms_arm64-exp-BP2A.250605.031.A3-13578795-38e52cb0.zip</button> `38e52cb0a3331a5ee0c653a4da2401ce74598a955acbd00aa85b6326036154c5` |
| ARM64 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="arm64" data-modal-dialog-id="a16_stable_aosp_arm64_GSI_zip">aosp_arm64-exp-BP2A.250605.031.A3-13578795-82277143.zip</button> `8227714351abe504eb27920d0e95c1b672722d2b7c9c9610dad2aee768624add` |
| x86_64+GMS | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="x86_64-gms" data-modal-dialog-id="a16_stable_gms_x86_64_GSI_zip">gsi_gms_x86_64-exp-BP2A.250605.031.A3-13578795-ccf343cd.zip</button> `ccf343cd5f0261ca4d3fcc442ad45a5cdedc05a10a7056427e5381013a0b04d4` |
| x86_64 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="x86_64" data-modal-dialog-id="a16_stable_aosp_x86_64_GSI_zip">aosp_x86_64-exp-BP2A.250605.031.A3-13578795-47b1a5bc.zip</button> `47b1a5bc29f31ffb451e9bb96cf30ce200498d5aa4258d75ec8b80a22adaf0e5` |


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

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 GSI Release </button> [Download Android 16 GSI Release](https://dl.google.com/developers/android/baklava/images/gsi/gsi_gms_arm64-exp-BP2A.250605.031.A3-13578795-38e52cb0.zip)

*gsi_gms_arm64-exp-BP2A.250605.031.A3-13578795-38e52cb0.zip*

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

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 GSI Release </button> [Download Android 16 GSI Release](https://dl.google.com/developers/android/baklava/images/gsi/gsi_gms_x86_64-exp-BP2A.250605.031.A3-13578795-ccf343cd.zip)

*gsi_gms_x86_64-exp-BP2A.250605.031.A3-13578795-ccf343cd.zip*

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

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 GSI Release </button> [Download Android 16 GSI Release](https://dl.google.com/developers/android/baklava/images/gsi/aosp_arm64-exp-BP2A.250605.031.A3-13578795-82277143.zip)

*aosp_arm64-exp-BP2A.250605.031.A3-13578795-82277143.zip*

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

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 16 GSI Release </button> [Download Android 16 GSI Release](https://dl.google.com/developers/android/baklava/images/gsi/aosp_x86_64-exp-BP2A.250605.031.A3-13578795-47b1a5bc.zip)

*aosp_x86_64-exp-BP2A.250605.031.A3-13578795-47b1a5bc.zip*

### Known issues with Android 16 GSIs

Android 16 GSI binaries have the following GSI-specific known issues that might
occur with some devices and builds:

- **Power Cycle**: Rebooting GSI might fail on some devices. To work around it, reboot the device into recovery mode, erase user data, perform a factory reset, and then reboot the device.
- **System partition size** : GSI + GMS file size (images named `_gsi\_gms\_arm64-*_`) might be bigger than the default dynamic system partition size on your device. To work around this issue, you can delete some non-essential dynamic partitions, such as the product partition, and flash the GSI again. For more information, see the [flashing GSIs
  documentation](https://source.android.com/setup/build/gsi#flashing-gsis).

## Android 15 GSIs

See the following sections.

### Android 15 QPR2

GSI binaries for Android 15 QPR2 are built from the same AOSP and GMS
sources as the [corresponding Google Pixel builds](https://developer.android.com/about/versions/15/get-qpr).
These binaries contain the same API and SDK, have a similar CTS result, and have
been validated on the following Pixel devices:

- Pixel 6 and 6 Pro
- Pixel 7 and 7 Pro
- Pixel 7a
- Pixel Fold
- Pixel Tablet
- Pixel 8 and 8 Pro
- Pixel 8a
- Pixel 9, 9 Pro, 9 Pro XL, and 9 Pro Fold

    Date: April 14, 2024
    Build: BP1A.250405.005.C1
    Security patch level: April 2024
    Google Play Services: 24.45.32

| Type | Download Link and SHA-256 Checksum |
|---|---|
| ARM64+GMS | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="arm64-gms" data-modal-dialog-id="a15_qpr2_stable_gms_arm64_GSI_zip">gsi_gms_arm64-exp-BP1A.250405.005.C1-13151952-48d6db2a.zip</button> `48d6db2ad0638ff7a23bb1dcb154221ee693afe0f88340b4000bda44940ff885` |
| ARM64 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="arm64" data-modal-dialog-id="a15_qpr2_stable_aosp_arm64_GSI_zip">aosp_arm64-exp-BP1A.250405.005.C1-13151952-61d23231.zip</button> `61d232315ad773bd4820c76c175efe6a61cd8a9a257508db588032be213e15f7` |
| x86_64+GMS | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="x86_64-gms" data-modal-dialog-id="a15_qpr2_stable_gms_x86_64_GSI_zip">gsi_gms_x86_64-exp-BP1A.250405.005.C1-13151952-a080bdd6.zip</button> `a080bdd66ea02e0f46189cbb3fec542c4ae00881d03948f73306c86a1e1df479` |
| x86_64 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="x86_64" data-modal-dialog-id="a15_qpr2_stable_aosp_x86_64_GSI_zip">aosp_x86_64-exp-BP1A.250405.005.C1-13151952-12978bf9.zip</button> `12978bf94c1e8dfee598941641df2aa73d29a0f967cc00f4f36b87ac1ed77bf2` |


### Download Android 15 GSI Release

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

This is the Early Access Google Mobile Services and Android 15 GSI License Agreement ("License Agreement"). Google Mobile Services and Android 15 GSI (each defined below) are licensed to you subject to the terms of the License Agreement. The License Agreement forms a legally binding contract between you and Google in relation to your use of Google Mobile Services and Android 15 GSI.  

### 1. Definitions

1.1 "Android" means the Android software stack for devices, as made available under the Android Open Source Project, which is located at the following URL: https://source.android.com/, as updated from time to time.  

1.2 "Android 15 GSI" means Google's generic system image of Android 15 code, excluding third party extensions.  

1.3 "Google" means Google LLC, a Delaware corporation with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, United States.  

1.4 "Google Mobile Services" means a machine-readable binary code version of the following Google applications: Search, Chrome, Gmail, Maps, YouTube, and Play, and certain other associated applications, in each case, as provided under this License Agreement. Google Mobile Services are collectively referred to in the License Agreement as "GMS" or each individually as a "GMS Application".  

1.5 "GMS+GSI" refers to GMS and Android 15 GSI, collectively.  

### 2. Accepting this License Agreement

2.1 In order to use GMS+GSI, you must first agree to the License Agreement. You may not use GMS+GSI if you do not accept the License Agreement.  

2.2 By clicking to accept, you hereby agree to the terms of the License Agreement.  

2.3 You may not use GMS+GSI and may not accept the License Agreement if you are a person barred from receiving GMS+GSI under the laws of the United States or other countries, including the country in which you are resident or from which you use GMS+GSI.  

2.4 If you are agreeing to be bound by the License Agreement on behalf of your employer or other entity, you represent and warrant that you have full legal authority to bind your employer or such entity to the License Agreement. If you do not have the requisite authority, you may not accept the License Agreement or use GMS+GSI on behalf of your employer or other entity.  

### 3. GMS+GSI License from Google

3.1 Subject to the terms of the License Agreement, Google grants you a limited, worldwide, royalty-free, non-assignable, non-exclusive, and non-sublicensable license to use GMS+GSI solely for testing applications for compatibility with Android 15.  

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

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 15 GSI Release </button> [Download Android 15 GSI Release](https://dl.google.com/developers/android/vic/images/gsi/gsi_gms_arm64-exp-BP1A.250405.005.C1-13151952-48d6db2a.zip)

*gsi_gms_arm64-exp-BP1A.250405.005.C1-13151952-48d6db2a.zip*

### Download Android 15 GSI Release

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

This is the Early Access Google Mobile Services and Android 15 GSI License Agreement ("License Agreement"). Google Mobile Services and Android 15 GSI (each defined below) are licensed to you subject to the terms of the License Agreement. The License Agreement forms a legally binding contract between you and Google in relation to your use of Google Mobile Services and Android 15 GSI.  

### 1. Definitions

1.1 "Android" means the Android software stack for devices, as made available under the Android Open Source Project, which is located at the following URL: https://source.android.com/, as updated from time to time.  

1.2 "Android 15 GSI" means Google's generic system image of Android 15 code, excluding third party extensions.  

1.3 "Google" means Google LLC, a Delaware corporation with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, United States.  

1.4 "Google Mobile Services" means a machine-readable binary code version of the following Google applications: Search, Chrome, Gmail, Maps, YouTube, and Play, and certain other associated applications, in each case, as provided under this License Agreement. Google Mobile Services are collectively referred to in the License Agreement as "GMS" or each individually as a "GMS Application".  

1.5 "GMS+GSI" refers to GMS and Android 15 GSI, collectively.  

### 2. Accepting this License Agreement

2.1 In order to use GMS+GSI, you must first agree to the License Agreement. You may not use GMS+GSI if you do not accept the License Agreement.  

2.2 By clicking to accept, you hereby agree to the terms of the License Agreement.  

2.3 You may not use GMS+GSI and may not accept the License Agreement if you are a person barred from receiving GMS+GSI under the laws of the United States or other countries, including the country in which you are resident or from which you use GMS+GSI.  

2.4 If you are agreeing to be bound by the License Agreement on behalf of your employer or other entity, you represent and warrant that you have full legal authority to bind your employer or such entity to the License Agreement. If you do not have the requisite authority, you may not accept the License Agreement or use GMS+GSI on behalf of your employer or other entity.  

### 3. GMS+GSI License from Google

3.1 Subject to the terms of the License Agreement, Google grants you a limited, worldwide, royalty-free, non-assignable, non-exclusive, and non-sublicensable license to use GMS+GSI solely for testing applications for compatibility with Android 15.  

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

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 15 GSI Release </button> [Download Android 15 GSI Release](https://dl.google.com/developers/android/vic/images/gsi/gsi_gms_x86_64-exp-BP1A.250405.005.C1-13151952-a080bdd6.zip)

*gsi_gms_x86_64-exp-BP1A.250405.005.C1-13151952-a080bdd6.zip*

### Download Android 15 GSI Release

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

This is the Early Access Google Mobile Services and Android 15 GSI License Agreement ("License Agreement"). Google Mobile Services and Android 15 GSI (each defined below) are licensed to you subject to the terms of the License Agreement. The License Agreement forms a legally binding contract between you and Google in relation to your use of Google Mobile Services and Android 15 GSI.  

### 1. Definitions

1.1 "Android" means the Android software stack for devices, as made available under the Android Open Source Project, which is located at the following URL: https://source.android.com/, as updated from time to time.  

1.2 "Android 15 GSI" means Google's generic system image of Android 15 code, excluding third party extensions.  

1.3 "Google" means Google LLC, a Delaware corporation with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, United States.  

1.4 "Google Mobile Services" means a machine-readable binary code version of the following Google applications: Search, Chrome, Gmail, Maps, YouTube, and Play, and certain other associated applications, in each case, as provided under this License Agreement. Google Mobile Services are collectively referred to in the License Agreement as "GMS" or each individually as a "GMS Application".  

1.5 "GMS+GSI" refers to GMS and Android 15 GSI, collectively.  

### 2. Accepting this License Agreement

2.1 In order to use GMS+GSI, you must first agree to the License Agreement. You may not use GMS+GSI if you do not accept the License Agreement.  

2.2 By clicking to accept, you hereby agree to the terms of the License Agreement.  

2.3 You may not use GMS+GSI and may not accept the License Agreement if you are a person barred from receiving GMS+GSI under the laws of the United States or other countries, including the country in which you are resident or from which you use GMS+GSI.  

2.4 If you are agreeing to be bound by the License Agreement on behalf of your employer or other entity, you represent and warrant that you have full legal authority to bind your employer or such entity to the License Agreement. If you do not have the requisite authority, you may not accept the License Agreement or use GMS+GSI on behalf of your employer or other entity.  

### 3. GMS+GSI License from Google

3.1 Subject to the terms of the License Agreement, Google grants you a limited, worldwide, royalty-free, non-assignable, non-exclusive, and non-sublicensable license to use GMS+GSI solely for testing applications for compatibility with Android 15.  

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

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 15 GSI Release </button> [Download Android 15 GSI Release](https://dl.google.com/developers/android/vic/images/gsi/aosp_arm64-exp-BP1A.250405.005.C1-13151952-61d23231.zip)

*aosp_arm64-exp-BP1A.250405.005.C1-13151952-61d23231.zip*

### Download Android 15 GSI Release

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

This is the Early Access Google Mobile Services and Android 15 GSI License Agreement ("License Agreement"). Google Mobile Services and Android 15 GSI (each defined below) are licensed to you subject to the terms of the License Agreement. The License Agreement forms a legally binding contract between you and Google in relation to your use of Google Mobile Services and Android 15 GSI.  

### 1. Definitions

1.1 "Android" means the Android software stack for devices, as made available under the Android Open Source Project, which is located at the following URL: https://source.android.com/, as updated from time to time.  

1.2 "Android 15 GSI" means Google's generic system image of Android 15 code, excluding third party extensions.  

1.3 "Google" means Google LLC, a Delaware corporation with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, United States.  

1.4 "Google Mobile Services" means a machine-readable binary code version of the following Google applications: Search, Chrome, Gmail, Maps, YouTube, and Play, and certain other associated applications, in each case, as provided under this License Agreement. Google Mobile Services are collectively referred to in the License Agreement as "GMS" or each individually as a "GMS Application".  

1.5 "GMS+GSI" refers to GMS and Android 15 GSI, collectively.  

### 2. Accepting this License Agreement

2.1 In order to use GMS+GSI, you must first agree to the License Agreement. You may not use GMS+GSI if you do not accept the License Agreement.  

2.2 By clicking to accept, you hereby agree to the terms of the License Agreement.  

2.3 You may not use GMS+GSI and may not accept the License Agreement if you are a person barred from receiving GMS+GSI under the laws of the United States or other countries, including the country in which you are resident or from which you use GMS+GSI.  

2.4 If you are agreeing to be bound by the License Agreement on behalf of your employer or other entity, you represent and warrant that you have full legal authority to bind your employer or such entity to the License Agreement. If you do not have the requisite authority, you may not accept the License Agreement or use GMS+GSI on behalf of your employer or other entity.  

### 3. GMS+GSI License from Google

3.1 Subject to the terms of the License Agreement, Google grants you a limited, worldwide, royalty-free, non-assignable, non-exclusive, and non-sublicensable license to use GMS+GSI solely for testing applications for compatibility with Android 15.  

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

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 15 GSI Release </button> [Download Android 15 GSI Release](https://dl.google.com/developers/android/vic/images/gsi/aosp_x86_64-exp-BP1A.250405.005.C1-13151952-12978bf9.zip)

*aosp_x86_64-exp-BP1A.250405.005.C1-13151952-12978bf9.zip*

### Android 15 QPR1

GSI binaries for Android 15 QPR1 are built from the same AOSP and GMS
sources as the [corresponding Google Pixel builds](https://developer.android.com/about/versions/15/get-qpr1).
These binaries contain the same API and SDK, have a similar CTS result, and have
been validated on the following Pixel devices:

- Pixel 6 and 6 Pro
- Pixel 7 and 7 Pro
- Pixel 7a
- Pixel Fold
- Pixel Tablet
- Pixel 8 and 8 Pro
- Pixel 8a
- Pixel 9, 9 Pro, 9 Pro XL, and 9 Pro Fold

    Date: December 05, 2024
    Build: AP4A.241205.013
    Security patch level: December 2024
    Google Play Services: 24.33.33

| Type | Download Link and SHA-256 Checksum |
|---|---|
| ARM64+GMS | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="arm64-gms" data-modal-dialog-id="a15_qpr1_stable_gms_arm64_GSI_zip">gsi_gms_arm64-exp-AP4A.241205.013-12621605-f90b9f1e.zip</button> `f90b9f1ed814d6a734da1e7e7ccc4206db90bb99a68fbdcc891380c102db6c93` |
| ARM64 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="arm64" data-modal-dialog-id="a15_qpr1_stable_aosp_arm64_GSI_zip">aosp_arm64-exp-AP4A.241205.013-12621605-14e72a7c.zip</button> `14e72a7c1b6b6600ba4f7b6057c79e531bbb9aa763e9e998ab5e1a8709e5075b` |
| x86_64+GMS | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="x86_64-gms" data-modal-dialog-id="a15_qpr1_stable_gms_x86_64_GSI_zip">gsi_gms_x86_64-exp-AP4A.241205.013-12621605-32b57682.zip</button> `32b57682319b2695c96ddce37bdae25bcf2ea11bbfe5688692a5a8bda953b868` |
| x86_64 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="x86_64" data-modal-dialog-id="a15_qpr1_stable_aosp_x86_64_GSI_zip">aosp_x86_64-exp-AP4A.241205.013-12621605-422944cb.zip</button> `422944cbefde67e232c1acb486d27c7f72ce63954a58b48141f7bb2b37baccf7` |


### Download Android 15 GSI Release

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

This is the Early Access Google Mobile Services and Android 15 GSI License Agreement ("License Agreement"). Google Mobile Services and Android 15 GSI (each defined below) are licensed to you subject to the terms of the License Agreement. The License Agreement forms a legally binding contract between you and Google in relation to your use of Google Mobile Services and Android 15 GSI.  

### 1. Definitions

1.1 "Android" means the Android software stack for devices, as made available under the Android Open Source Project, which is located at the following URL: https://source.android.com/, as updated from time to time.  

1.2 "Android 15 GSI" means Google's generic system image of Android 15 code, excluding third party extensions.  

1.3 "Google" means Google LLC, a Delaware corporation with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, United States.  

1.4 "Google Mobile Services" means a machine-readable binary code version of the following Google applications: Search, Chrome, Gmail, Maps, YouTube, and Play, and certain other associated applications, in each case, as provided under this License Agreement. Google Mobile Services are collectively referred to in the License Agreement as "GMS" or each individually as a "GMS Application".  

1.5 "GMS+GSI" refers to GMS and Android 15 GSI, collectively.  

### 2. Accepting this License Agreement

2.1 In order to use GMS+GSI, you must first agree to the License Agreement. You may not use GMS+GSI if you do not accept the License Agreement.  

2.2 By clicking to accept, you hereby agree to the terms of the License Agreement.  

2.3 You may not use GMS+GSI and may not accept the License Agreement if you are a person barred from receiving GMS+GSI under the laws of the United States or other countries, including the country in which you are resident or from which you use GMS+GSI.  

2.4 If you are agreeing to be bound by the License Agreement on behalf of your employer or other entity, you represent and warrant that you have full legal authority to bind your employer or such entity to the License Agreement. If you do not have the requisite authority, you may not accept the License Agreement or use GMS+GSI on behalf of your employer or other entity.  

### 3. GMS+GSI License from Google

3.1 Subject to the terms of the License Agreement, Google grants you a limited, worldwide, royalty-free, non-assignable, non-exclusive, and non-sublicensable license to use GMS+GSI solely for testing applications for compatibility with Android 15.  

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

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 15 GSI Release </button> [Download Android 15 GSI Release](https://dl.google.com/developers/android/vic/images/gsi/gsi_gms_arm64-exp-AP4A.241205.013-12621605-f90b9f1e.zip)

*gsi_gms_arm64-exp-AP4A.241205.013-12621605-f90b9f1e.zip*

### Download Android 15 GSI Release

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

This is the Early Access Google Mobile Services and Android 15 GSI License Agreement ("License Agreement"). Google Mobile Services and Android 15 GSI (each defined below) are licensed to you subject to the terms of the License Agreement. The License Agreement forms a legally binding contract between you and Google in relation to your use of Google Mobile Services and Android 15 GSI.  

### 1. Definitions

1.1 "Android" means the Android software stack for devices, as made available under the Android Open Source Project, which is located at the following URL: https://source.android.com/, as updated from time to time.  

1.2 "Android 15 GSI" means Google's generic system image of Android 15 code, excluding third party extensions.  

1.3 "Google" means Google LLC, a Delaware corporation with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, United States.  

1.4 "Google Mobile Services" means a machine-readable binary code version of the following Google applications: Search, Chrome, Gmail, Maps, YouTube, and Play, and certain other associated applications, in each case, as provided under this License Agreement. Google Mobile Services are collectively referred to in the License Agreement as "GMS" or each individually as a "GMS Application".  

1.5 "GMS+GSI" refers to GMS and Android 15 GSI, collectively.  

### 2. Accepting this License Agreement

2.1 In order to use GMS+GSI, you must first agree to the License Agreement. You may not use GMS+GSI if you do not accept the License Agreement.  

2.2 By clicking to accept, you hereby agree to the terms of the License Agreement.  

2.3 You may not use GMS+GSI and may not accept the License Agreement if you are a person barred from receiving GMS+GSI under the laws of the United States or other countries, including the country in which you are resident or from which you use GMS+GSI.  

2.4 If you are agreeing to be bound by the License Agreement on behalf of your employer or other entity, you represent and warrant that you have full legal authority to bind your employer or such entity to the License Agreement. If you do not have the requisite authority, you may not accept the License Agreement or use GMS+GSI on behalf of your employer or other entity.  

### 3. GMS+GSI License from Google

3.1 Subject to the terms of the License Agreement, Google grants you a limited, worldwide, royalty-free, non-assignable, non-exclusive, and non-sublicensable license to use GMS+GSI solely for testing applications for compatibility with Android 15.  

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

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 15 GSI Release </button> [Download Android 15 GSI Release](https://dl.google.com/developers/android/vic/images/gsi/gsi_gms_x86_64-exp-AP4A.241205.013-12621605-32b57682.zip)

*gsi_gms_x86_64-exp-AP4A.241205.013-12621605-32b57682.zip*

### Download Android 15 GSI Release

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

This is the Early Access Google Mobile Services and Android 15 GSI License Agreement ("License Agreement"). Google Mobile Services and Android 15 GSI (each defined below) are licensed to you subject to the terms of the License Agreement. The License Agreement forms a legally binding contract between you and Google in relation to your use of Google Mobile Services and Android 15 GSI.  

### 1. Definitions

1.1 "Android" means the Android software stack for devices, as made available under the Android Open Source Project, which is located at the following URL: https://source.android.com/, as updated from time to time.  

1.2 "Android 15 GSI" means Google's generic system image of Android 15 code, excluding third party extensions.  

1.3 "Google" means Google LLC, a Delaware corporation with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, United States.  

1.4 "Google Mobile Services" means a machine-readable binary code version of the following Google applications: Search, Chrome, Gmail, Maps, YouTube, and Play, and certain other associated applications, in each case, as provided under this License Agreement. Google Mobile Services are collectively referred to in the License Agreement as "GMS" or each individually as a "GMS Application".  

1.5 "GMS+GSI" refers to GMS and Android 15 GSI, collectively.  

### 2. Accepting this License Agreement

2.1 In order to use GMS+GSI, you must first agree to the License Agreement. You may not use GMS+GSI if you do not accept the License Agreement.  

2.2 By clicking to accept, you hereby agree to the terms of the License Agreement.  

2.3 You may not use GMS+GSI and may not accept the License Agreement if you are a person barred from receiving GMS+GSI under the laws of the United States or other countries, including the country in which you are resident or from which you use GMS+GSI.  

2.4 If you are agreeing to be bound by the License Agreement on behalf of your employer or other entity, you represent and warrant that you have full legal authority to bind your employer or such entity to the License Agreement. If you do not have the requisite authority, you may not accept the License Agreement or use GMS+GSI on behalf of your employer or other entity.  

### 3. GMS+GSI License from Google

3.1 Subject to the terms of the License Agreement, Google grants you a limited, worldwide, royalty-free, non-assignable, non-exclusive, and non-sublicensable license to use GMS+GSI solely for testing applications for compatibility with Android 15.  

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

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 15 GSI Release </button> [Download Android 15 GSI Release](https://dl.google.com/developers/android/vic/images/gsi/aosp_arm64-exp-AP4A.241205.013-12621605-14e72a7c.zip)

*aosp_arm64-exp-AP4A.241205.013-12621605-14e72a7c.zip*

### Download Android 15 GSI Release

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

This is the Early Access Google Mobile Services and Android 15 GSI License Agreement ("License Agreement"). Google Mobile Services and Android 15 GSI (each defined below) are licensed to you subject to the terms of the License Agreement. The License Agreement forms a legally binding contract between you and Google in relation to your use of Google Mobile Services and Android 15 GSI.  

### 1. Definitions

1.1 "Android" means the Android software stack for devices, as made available under the Android Open Source Project, which is located at the following URL: https://source.android.com/, as updated from time to time.  

1.2 "Android 15 GSI" means Google's generic system image of Android 15 code, excluding third party extensions.  

1.3 "Google" means Google LLC, a Delaware corporation with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, United States.  

1.4 "Google Mobile Services" means a machine-readable binary code version of the following Google applications: Search, Chrome, Gmail, Maps, YouTube, and Play, and certain other associated applications, in each case, as provided under this License Agreement. Google Mobile Services are collectively referred to in the License Agreement as "GMS" or each individually as a "GMS Application".  

1.5 "GMS+GSI" refers to GMS and Android 15 GSI, collectively.  

### 2. Accepting this License Agreement

2.1 In order to use GMS+GSI, you must first agree to the License Agreement. You may not use GMS+GSI if you do not accept the License Agreement.  

2.2 By clicking to accept, you hereby agree to the terms of the License Agreement.  

2.3 You may not use GMS+GSI and may not accept the License Agreement if you are a person barred from receiving GMS+GSI under the laws of the United States or other countries, including the country in which you are resident or from which you use GMS+GSI.  

2.4 If you are agreeing to be bound by the License Agreement on behalf of your employer or other entity, you represent and warrant that you have full legal authority to bind your employer or such entity to the License Agreement. If you do not have the requisite authority, you may not accept the License Agreement or use GMS+GSI on behalf of your employer or other entity.  

### 3. GMS+GSI License from Google

3.1 Subject to the terms of the License Agreement, Google grants you a limited, worldwide, royalty-free, non-assignable, non-exclusive, and non-sublicensable license to use GMS+GSI solely for testing applications for compatibility with Android 15.  

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

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 15 GSI Release </button> [Download Android 15 GSI Release](https://dl.google.com/developers/android/vic/images/gsi/aosp_x86_64-exp-AP4A.241205.013-12621605-422944cb.zip)

*aosp_x86_64-exp-AP4A.241205.013-12621605-422944cb.zip*

### Android 15 (initial release)

GSI binaries for Android 15 are built from the same AOSP and GMS sources as the
[corresponding Google Pixel builds](https://developer.android.com/about/versions/15/get#on_pixel). These
binaries contain the same API and SDK, have a similar CTS result, and have been
validated on the following Pixel devices:

- Pixel 6 and 6 Pro
- Pixel 7 and 7 Pro
- Pixel 7a
- Pixel Fold
- Pixel Tablet
- Pixel 8 and 8 Pro
- Pixel 8a
- Pixel 9, 9 Pro, 9 Pro XL, and 9 Pro Fold

    Date: October 15, 2024
    Build: AP3A.241005.015
    Security patch level: October 2024
    Google Play Services: 24.23.37

| Type | Download Link and SHA-256 Checksum |
|---|---|
| ARM64+GMS | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="arm64-gms" data-modal-dialog-id="a15_stable_gms_arm64_GSI_zip">gsi_gms_arm64-exp-AP3A.241005.015-12366759-0fdc93fe.zip</button> `0fdc93fe82b27c177aa6dadc1c4daf69be013679e14f2f2bf1fda1ce3e9abe74` |
| ARM64 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="arm64" data-modal-dialog-id="a15_stable_aosp_arm64_GSI_zip">aosp_arm64-exp-AP3A.241005.015-12366759-3c0ee79d.zip</button> `3c0ee79d0c08977e4e287501f8378d15cdfd763d0f5c65fcf704970150b15bd8` |
| x86_64+GMS | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="x86_64-gms" data-modal-dialog-id="a15_stable_gms_x86_64_GSI_zip">gsi_gms_x86_64-exp-AP3A.241005.015-12366759-d77cb747.zip</button> `d77cb747f9a901178498b0dc63269c6d09fbbc863cd8d66513ea7a8148a95fe8` |
| x86_64 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="x86_64" data-modal-dialog-id="a15_stable_aosp_x86_64_GSI_zip">aosp_x86_64-exp-AP3A.241005.015-12366759-96716f9b.zip</button> `96716f9bff890f7336274b8bc80b3dd816b3571f881beffbfe91800ee41300f9` |


### Download Android 15 GSI Release

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

This is the Early Access Google Mobile Services and Android 15 GSI License Agreement ("License Agreement"). Google Mobile Services and Android 15 GSI (each defined below) are licensed to you subject to the terms of the License Agreement. The License Agreement forms a legally binding contract between you and Google in relation to your use of Google Mobile Services and Android 15 GSI.  

### 1. Definitions

1.1 "Android" means the Android software stack for devices, as made available under the Android Open Source Project, which is located at the following URL: https://source.android.com/, as updated from time to time.  

1.2 "Android 15 GSI" means Google's generic system image of Android 15 code, excluding third party extensions.  

1.3 "Google" means Google LLC, a Delaware corporation with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, United States.  

1.4 "Google Mobile Services" means a machine-readable binary code version of the following Google applications: Search, Chrome, Gmail, Maps, YouTube, and Play, and certain other associated applications, in each case, as provided under this License Agreement. Google Mobile Services are collectively referred to in the License Agreement as "GMS" or each individually as a "GMS Application".  

1.5 "GMS+GSI" refers to GMS and Android 15 GSI, collectively.  

### 2. Accepting this License Agreement

2.1 In order to use GMS+GSI, you must first agree to the License Agreement. You may not use GMS+GSI if you do not accept the License Agreement.  

2.2 By clicking to accept, you hereby agree to the terms of the License Agreement.  

2.3 You may not use GMS+GSI and may not accept the License Agreement if you are a person barred from receiving GMS+GSI under the laws of the United States or other countries, including the country in which you are resident or from which you use GMS+GSI.  

2.4 If you are agreeing to be bound by the License Agreement on behalf of your employer or other entity, you represent and warrant that you have full legal authority to bind your employer or such entity to the License Agreement. If you do not have the requisite authority, you may not accept the License Agreement or use GMS+GSI on behalf of your employer or other entity.  

### 3. GMS+GSI License from Google

3.1 Subject to the terms of the License Agreement, Google grants you a limited, worldwide, royalty-free, non-assignable, non-exclusive, and non-sublicensable license to use GMS+GSI solely for testing applications for compatibility with Android 15.  

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

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 15 GSI Release </button> [Download Android 15 GSI Release](https://dl.google.com/developers/android/vic/images/gsi/gsi_gms_arm64-exp-AP3A.241005.015-12366759-0fdc93fe.zip)

*gsi_gms_arm64-exp-AP3A.241005.015-12366759-0fdc93fe.zip*

### Download Android 15 GSI Release

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

This is the Early Access Google Mobile Services and Android 15 GSI License Agreement ("License Agreement"). Google Mobile Services and Android 15 GSI (each defined below) are licensed to you subject to the terms of the License Agreement. The License Agreement forms a legally binding contract between you and Google in relation to your use of Google Mobile Services and Android 15 GSI.  

### 1. Definitions

1.1 "Android" means the Android software stack for devices, as made available under the Android Open Source Project, which is located at the following URL: https://source.android.com/, as updated from time to time.  

1.2 "Android 15 GSI" means Google's generic system image of Android 15 code, excluding third party extensions.  

1.3 "Google" means Google LLC, a Delaware corporation with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, United States.  

1.4 "Google Mobile Services" means a machine-readable binary code version of the following Google applications: Search, Chrome, Gmail, Maps, YouTube, and Play, and certain other associated applications, in each case, as provided under this License Agreement. Google Mobile Services are collectively referred to in the License Agreement as "GMS" or each individually as a "GMS Application".  

1.5 "GMS+GSI" refers to GMS and Android 15 GSI, collectively.  

### 2. Accepting this License Agreement

2.1 In order to use GMS+GSI, you must first agree to the License Agreement. You may not use GMS+GSI if you do not accept the License Agreement.  

2.2 By clicking to accept, you hereby agree to the terms of the License Agreement.  

2.3 You may not use GMS+GSI and may not accept the License Agreement if you are a person barred from receiving GMS+GSI under the laws of the United States or other countries, including the country in which you are resident or from which you use GMS+GSI.  

2.4 If you are agreeing to be bound by the License Agreement on behalf of your employer or other entity, you represent and warrant that you have full legal authority to bind your employer or such entity to the License Agreement. If you do not have the requisite authority, you may not accept the License Agreement or use GMS+GSI on behalf of your employer or other entity.  

### 3. GMS+GSI License from Google

3.1 Subject to the terms of the License Agreement, Google grants you a limited, worldwide, royalty-free, non-assignable, non-exclusive, and non-sublicensable license to use GMS+GSI solely for testing applications for compatibility with Android 15.  

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

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 15 GSI Release </button> [Download Android 15 GSI Release](https://dl.google.com/developers/android/vic/images/gsi/gsi_gms_x86_64-exp-AP3A.241005.015-12366759-d77cb747.zip)

*gsi_gms_x86_64-exp-AP3A.241005.015-12366759-d77cb747.zip*

### Download Android 15 GSI Release

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

This is the Early Access Google Mobile Services and Android 15 GSI License Agreement ("License Agreement"). Google Mobile Services and Android 15 GSI (each defined below) are licensed to you subject to the terms of the License Agreement. The License Agreement forms a legally binding contract between you and Google in relation to your use of Google Mobile Services and Android 15 GSI.  

### 1. Definitions

1.1 "Android" means the Android software stack for devices, as made available under the Android Open Source Project, which is located at the following URL: https://source.android.com/, as updated from time to time.  

1.2 "Android 15 GSI" means Google's generic system image of Android 15 code, excluding third party extensions.  

1.3 "Google" means Google LLC, a Delaware corporation with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, United States.  

1.4 "Google Mobile Services" means a machine-readable binary code version of the following Google applications: Search, Chrome, Gmail, Maps, YouTube, and Play, and certain other associated applications, in each case, as provided under this License Agreement. Google Mobile Services are collectively referred to in the License Agreement as "GMS" or each individually as a "GMS Application".  

1.5 "GMS+GSI" refers to GMS and Android 15 GSI, collectively.  

### 2. Accepting this License Agreement

2.1 In order to use GMS+GSI, you must first agree to the License Agreement. You may not use GMS+GSI if you do not accept the License Agreement.  

2.2 By clicking to accept, you hereby agree to the terms of the License Agreement.  

2.3 You may not use GMS+GSI and may not accept the License Agreement if you are a person barred from receiving GMS+GSI under the laws of the United States or other countries, including the country in which you are resident or from which you use GMS+GSI.  

2.4 If you are agreeing to be bound by the License Agreement on behalf of your employer or other entity, you represent and warrant that you have full legal authority to bind your employer or such entity to the License Agreement. If you do not have the requisite authority, you may not accept the License Agreement or use GMS+GSI on behalf of your employer or other entity.  

### 3. GMS+GSI License from Google

3.1 Subject to the terms of the License Agreement, Google grants you a limited, worldwide, royalty-free, non-assignable, non-exclusive, and non-sublicensable license to use GMS+GSI solely for testing applications for compatibility with Android 15.  

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

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 15 GSI Release </button> [Download Android 15 GSI Release](https://dl.google.com/developers/android/vic/images/gsi/aosp_arm64-exp-AP3A.241005.015-12366759-3c0ee79d.zip)

*aosp_arm64-exp-AP3A.241005.015-12366759-3c0ee79d.zip*

### Download Android 15 GSI Release

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

This is the Early Access Google Mobile Services and Android 15 GSI License Agreement ("License Agreement"). Google Mobile Services and Android 15 GSI (each defined below) are licensed to you subject to the terms of the License Agreement. The License Agreement forms a legally binding contract between you and Google in relation to your use of Google Mobile Services and Android 15 GSI.  

### 1. Definitions

1.1 "Android" means the Android software stack for devices, as made available under the Android Open Source Project, which is located at the following URL: https://source.android.com/, as updated from time to time.  

1.2 "Android 15 GSI" means Google's generic system image of Android 15 code, excluding third party extensions.  

1.3 "Google" means Google LLC, a Delaware corporation with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, United States.  

1.4 "Google Mobile Services" means a machine-readable binary code version of the following Google applications: Search, Chrome, Gmail, Maps, YouTube, and Play, and certain other associated applications, in each case, as provided under this License Agreement. Google Mobile Services are collectively referred to in the License Agreement as "GMS" or each individually as a "GMS Application".  

1.5 "GMS+GSI" refers to GMS and Android 15 GSI, collectively.  

### 2. Accepting this License Agreement

2.1 In order to use GMS+GSI, you must first agree to the License Agreement. You may not use GMS+GSI if you do not accept the License Agreement.  

2.2 By clicking to accept, you hereby agree to the terms of the License Agreement.  

2.3 You may not use GMS+GSI and may not accept the License Agreement if you are a person barred from receiving GMS+GSI under the laws of the United States or other countries, including the country in which you are resident or from which you use GMS+GSI.  

2.4 If you are agreeing to be bound by the License Agreement on behalf of your employer or other entity, you represent and warrant that you have full legal authority to bind your employer or such entity to the License Agreement. If you do not have the requisite authority, you may not accept the License Agreement or use GMS+GSI on behalf of your employer or other entity.  

### 3. GMS+GSI License from Google

3.1 Subject to the terms of the License Agreement, Google grants you a limited, worldwide, royalty-free, non-assignable, non-exclusive, and non-sublicensable license to use GMS+GSI solely for testing applications for compatibility with Android 15.  

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

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 15 GSI Release </button> [Download Android 15 GSI Release](https://dl.google.com/developers/android/vic/images/gsi/aosp_x86_64-exp-AP3A.241005.015-12366759-96716f9b.zip)

*aosp_x86_64-exp-AP3A.241005.015-12366759-96716f9b.zip*

### Known issues with Android 15 GSIs

Android 15 GSI binaries have the following GSI-specific known issues that might
occur with some devices and builds:

- **Bluetooth audio**: In some cases, Bluetooth audio can't be heard after
  pairing a new device.

- **Power Cycle**: Rebooting GSI might fail on some devices. To work around
  it, reboot the device into recovery mode, erase user data, perform a factory
  reset, and then reboot the device.

- **System partition size** : GSI + GMS file size (images named
  `_gsi\_gms\_arm64-*_`) might be bigger than the default dynamic system
  partition size on your device. To work around this issue, you can delete
  some non-essential dynamic partitions, such as the product partition, and
  flash the GSI again. For more information, see the [flashing GSIs
  documentation](https://source.android.com/setup/build/gsi#flashing-gsis).

## Android 14 GSIs

See the following sections.

### Android 14 QPR1

GSI binaries for Android 14 QPR1 are built from the same AOSP and GMS sources as
the [corresponding Google Pixel builds](https://developer.android.com/about/versions/14/get#on_pixel). These
binaries contain the same API and SDK, have a similar CTS result, and have been
validated on the following Pixel devices:

- Pixel 5a
- Pixel 6 and 6 Pro
- Pixel 6a
- Pixel 7 and 7 Pro
- Pixel 7a
- Pixel Fold
- Pixel Tablet
- Pixel 8 and 8 Pro

    Date: December 05, 2023
    Build: UQ1A.231205.015
    Security patch level: December 2023
    Google Play Services: 23.32.17

| Type | Download Link and SHA-256 Checksum |
|---|---|
| ARM64+GMS | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="arm64-gms" data-modal-dialog-id="a14_qpr1_stable_gms_arm64_GSI_zip">gsi_gms_arm64-exp-UQ1A.231205.015-11084887-2026a0e7.zip</button> `2026a0e788abf09a91421a4f83b7d766bfe1ec82707e3b6a5ca74f6c65212fc8` |
| ARM64 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="arm64" data-modal-dialog-id="a14_qpr1_stable_aosp_arm64_GSI_zip">aosp_arm64-exp-UQ1A.231205.015-11084887-e291b838.zip</button> `e291b838f9e2786eb44c952ca25469745c8085cf91611397d7f620136b48c086` |
| x86_64+GMS | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="x86_64-gms" data-modal-dialog-id="a14_qpr1_stable_gms_x86_64_GSI_zip">gsi_gms_x86_64-exp-UQ1A.231205.015-11084887-5f53f7cc.zip</button> `5f53f7cc53e58357e57dbe46e475e1c50429d7e4ab9ba41be88de041a44960b9` |
| x86_64 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="x86_64" data-modal-dialog-id="a14_qpr1_stable_aosp_x86_64_GSI_zip">aosp_x86_64-exp-UQ1A.231205.015-11084887-f8788769.zip</button> `f8788769ea2497d555bd46334f9faa81697ed538cdaaacce68d72471f56cb8c5` |


### Download Android 14 GSI Release

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

This is the Early Access Google Mobile Services and Android 14 GSI License Agreement ("License Agreement"). Google Mobile Services and Android 14 GSI (each defined below) are licensed to you subject to the terms of the License Agreement. The License Agreement forms a legally binding contract between you and Google in relation to your use of Google Mobile Services and Android 14 GSI.  

### 1. Definitions

1.1 "Android" means the Android software stack for devices, as made available under the Android Open Source Project, which is located at the following URL: https://source.android.com/, as updated from time to time.  

1.2 "Android 14 GSI" means Google's generic system image of Android 14 code, excluding third party extensions.  

1.3 "Google" means Google LLC, a Delaware corporation with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, United States.  

1.4 "Google Mobile Services" means a machine-readable binary code version of the following Google applications: Search, Chrome, Gmail, Maps, YouTube, and Play, and certain other associated applications, in each case, as provided under this License Agreement. Google Mobile Services are collectively referred to in the License Agreement as "GMS" or each individually as a "GMS Application".  

1.5 "GMS+GSI" refers to GMS and Android 14 GSI, collectively.  

### 2. Accepting this License Agreement

2.1 In order to use GMS+GSI, you must first agree to the License Agreement. You may not use GMS+GSI if you do not accept the License Agreement.  

2.2 By clicking to accept, you hereby agree to the terms of the License Agreement.  

2.3 You may not use GMS+GSI and may not accept the License Agreement if you are a person barred from receiving GMS+GSI under the laws of the United States or other countries, including the country in which you are resident or from which you use GMS+GSI.  

2.4 If you are agreeing to be bound by the License Agreement on behalf of your employer or other entity, you represent and warrant that you have full legal authority to bind your employer or such entity to the License Agreement. If you do not have the requisite authority, you may not accept the License Agreement or use GMS+GSI on behalf of your employer or other entity.  

### 3. GMS+GSI License from Google

3.1 Subject to the terms of the License Agreement, Google grants you a limited, worldwide, royalty-free, non-assignable, non-exclusive, and non-sublicensable license to use GMS+GSI solely for testing applications for compatibility with Android 14.  

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

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 14 GSI Release </button> [Download Android 14 GSI Release](https://dl.google.com/developers/android/udc/images/gsi/gsi_gms_arm64-exp-UQ1A.231205.015-11084887-2026a0e7.zip)

*gsi_gms_arm64-exp-UQ1A.231205.015-11084887-2026a0e7.zip*

### Download Android 14 GSI Release

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

This is the Early Access Google Mobile Services and Android 14 GSI License Agreement ("License Agreement"). Google Mobile Services and Android 14 GSI (each defined below) are licensed to you subject to the terms of the License Agreement. The License Agreement forms a legally binding contract between you and Google in relation to your use of Google Mobile Services and Android 14 GSI.  

### 1. Definitions

1.1 "Android" means the Android software stack for devices, as made available under the Android Open Source Project, which is located at the following URL: https://source.android.com/, as updated from time to time.  

1.2 "Android 14 GSI" means Google's generic system image of Android 14 code, excluding third party extensions.  

1.3 "Google" means Google LLC, a Delaware corporation with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, United States.  

1.4 "Google Mobile Services" means a machine-readable binary code version of the following Google applications: Search, Chrome, Gmail, Maps, YouTube, and Play, and certain other associated applications, in each case, as provided under this License Agreement. Google Mobile Services are collectively referred to in the License Agreement as "GMS" or each individually as a "GMS Application".  

1.5 "GMS+GSI" refers to GMS and Android 14 GSI, collectively.  

### 2. Accepting this License Agreement

2.1 In order to use GMS+GSI, you must first agree to the License Agreement. You may not use GMS+GSI if you do not accept the License Agreement.  

2.2 By clicking to accept, you hereby agree to the terms of the License Agreement.  

2.3 You may not use GMS+GSI and may not accept the License Agreement if you are a person barred from receiving GMS+GSI under the laws of the United States or other countries, including the country in which you are resident or from which you use GMS+GSI.  

2.4 If you are agreeing to be bound by the License Agreement on behalf of your employer or other entity, you represent and warrant that you have full legal authority to bind your employer or such entity to the License Agreement. If you do not have the requisite authority, you may not accept the License Agreement or use GMS+GSI on behalf of your employer or other entity.  

### 3. GMS+GSI License from Google

3.1 Subject to the terms of the License Agreement, Google grants you a limited, worldwide, royalty-free, non-assignable, non-exclusive, and non-sublicensable license to use GMS+GSI solely for testing applications for compatibility with Android 14.  

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

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 14 GSI Release </button> [Download Android 14 GSI Release](https://dl.google.com/developers/android/udc/images/gsi/gsi_gms_x86_64-exp-UQ1A.231205.015-11084887-5f53f7cc.zip)

*gsi_gms_x86_64-exp-UQ1A.231205.015-11084887-5f53f7cc.zip*

### Download Android 14 GSI Release

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

This is the Early Access Google Mobile Services and Android 14 GSI License Agreement ("License Agreement"). Google Mobile Services and Android 14 GSI (each defined below) are licensed to you subject to the terms of the License Agreement. The License Agreement forms a legally binding contract between you and Google in relation to your use of Google Mobile Services and Android 14 GSI.  

### 1. Definitions

1.1 "Android" means the Android software stack for devices, as made available under the Android Open Source Project, which is located at the following URL: https://source.android.com/, as updated from time to time.  

1.2 "Android 14 GSI" means Google's generic system image of Android 14 code, excluding third party extensions.  

1.3 "Google" means Google LLC, a Delaware corporation with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, United States.  

1.4 "Google Mobile Services" means a machine-readable binary code version of the following Google applications: Search, Chrome, Gmail, Maps, YouTube, and Play, and certain other associated applications, in each case, as provided under this License Agreement. Google Mobile Services are collectively referred to in the License Agreement as "GMS" or each individually as a "GMS Application".  

1.5 "GMS+GSI" refers to GMS and Android 14 GSI, collectively.  

### 2. Accepting this License Agreement

2.1 In order to use GMS+GSI, you must first agree to the License Agreement. You may not use GMS+GSI if you do not accept the License Agreement.  

2.2 By clicking to accept, you hereby agree to the terms of the License Agreement.  

2.3 You may not use GMS+GSI and may not accept the License Agreement if you are a person barred from receiving GMS+GSI under the laws of the United States or other countries, including the country in which you are resident or from which you use GMS+GSI.  

2.4 If you are agreeing to be bound by the License Agreement on behalf of your employer or other entity, you represent and warrant that you have full legal authority to bind your employer or such entity to the License Agreement. If you do not have the requisite authority, you may not accept the License Agreement or use GMS+GSI on behalf of your employer or other entity.  

### 3. GMS+GSI License from Google

3.1 Subject to the terms of the License Agreement, Google grants you a limited, worldwide, royalty-free, non-assignable, non-exclusive, and non-sublicensable license to use GMS+GSI solely for testing applications for compatibility with Android 14.  

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

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 14 GSI Release </button> [Download Android 14 GSI Release](https://dl.google.com/developers/android/udc/images/gsi/aosp_arm64-exp-UQ1A.231205.015-11084887-e291b838.zip)

*aosp_arm64-exp-UQ1A.231205.015-11084887-e291b838.zip*

### Download Android 14 GSI Release

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

This is the Early Access Google Mobile Services and Android 14 GSI License Agreement ("License Agreement"). Google Mobile Services and Android 14 GSI (each defined below) are licensed to you subject to the terms of the License Agreement. The License Agreement forms a legally binding contract between you and Google in relation to your use of Google Mobile Services and Android 14 GSI.  

### 1. Definitions

1.1 "Android" means the Android software stack for devices, as made available under the Android Open Source Project, which is located at the following URL: https://source.android.com/, as updated from time to time.  

1.2 "Android 14 GSI" means Google's generic system image of Android 14 code, excluding third party extensions.  

1.3 "Google" means Google LLC, a Delaware corporation with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, United States.  

1.4 "Google Mobile Services" means a machine-readable binary code version of the following Google applications: Search, Chrome, Gmail, Maps, YouTube, and Play, and certain other associated applications, in each case, as provided under this License Agreement. Google Mobile Services are collectively referred to in the License Agreement as "GMS" or each individually as a "GMS Application".  

1.5 "GMS+GSI" refers to GMS and Android 14 GSI, collectively.  

### 2. Accepting this License Agreement

2.1 In order to use GMS+GSI, you must first agree to the License Agreement. You may not use GMS+GSI if you do not accept the License Agreement.  

2.2 By clicking to accept, you hereby agree to the terms of the License Agreement.  

2.3 You may not use GMS+GSI and may not accept the License Agreement if you are a person barred from receiving GMS+GSI under the laws of the United States or other countries, including the country in which you are resident or from which you use GMS+GSI.  

2.4 If you are agreeing to be bound by the License Agreement on behalf of your employer or other entity, you represent and warrant that you have full legal authority to bind your employer or such entity to the License Agreement. If you do not have the requisite authority, you may not accept the License Agreement or use GMS+GSI on behalf of your employer or other entity.  

### 3. GMS+GSI License from Google

3.1 Subject to the terms of the License Agreement, Google grants you a limited, worldwide, royalty-free, non-assignable, non-exclusive, and non-sublicensable license to use GMS+GSI solely for testing applications for compatibility with Android 14.  

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

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 14 GSI Release </button> [Download Android 14 GSI Release](https://dl.google.com/developers/android/udc/images/gsi/aosp_x86_64-exp-UQ1A.231205.015-11084887-f8788769.zip)

*aosp_x86_64-exp-UQ1A.231205.015-11084887-f8788769.zip*

### Android 14 (initial, stable release)

GSI binaries for Android 14 are built from the same AOSP and GMS sources as the
[corresponding Google Pixel builds](https://developer.android.com/about/versions/14/get#on_pixel). These
binaries contain the same API and SDK, have a similar CTS result, and have been
validated on the following Pixel devices:

- Pixel 4a (5G)
- Pixel 5 and 5a
- Pixel 6 and 6 Pro
- Pixel 6a
- Pixel 7 and 7 Pro
- Pixel 7a
- Pixel Fold
- Pixel Tablet
- Pixel 8 and 8 Pro

    Date: October 12, 2023
    Build: UP1A.231005.007
    Security patch level: October 2023
    Google Play Services: 23.18.18

| Type | Download Link and SHA-256 Checksum |
|---|---|
| ARM64+GMS | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="arm64-gms" data-modal-dialog-id="a14_stable_gms_arm64_GSI_zip">gsi_gms_arm64-exp-UP1A.231005.007-10754064-77f9c9df.zip</button> `77f9c9dfad87c2bfdf17300cf791827eaa84adfc7535235a1ae2c063dc6537be` |
| ARM64 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="arm64" data-modal-dialog-id="a14_stable_aosp_arm64_GSI_zip">aosp_arm64-exp-UP1A.231005.007-10754064-68dd726a.zip</button> `68dd726a861678bb5abb251719e7b95632d9d05d4f097e63e094188a81346c29` |
| x86_64+GMS | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="x86_64-gms" data-modal-dialog-id="a14_stable_gms_x86_64_GSI_zip">gsi_gms_x86_64-exp-UP1A.231005.007-10754064-a42e6bb7.zip</button> `a42e6bb7b1267bb756f87db5d36fd285a20de2b6943d6233be689144052fd788` |
| x86_64 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="x86_64" data-modal-dialog-id="a14_stable_aosp_x86_64_GSI_zip">aosp_x86_64-exp-UP1A.231005.007-10754064-84570261.zip</button> `845702612585350234877b416c7f03ded1095832b2fe5ae4e9cc8a741d33cb71` |


### Download Android 14 GSI Release

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

This is the Early Access Google Mobile Services and Android 14 GSI License Agreement ("License Agreement"). Google Mobile Services and Android 14 GSI (each defined below) are licensed to you subject to the terms of the License Agreement. The License Agreement forms a legally binding contract between you and Google in relation to your use of Google Mobile Services and Android 14 GSI.  

### 1. Definitions

1.1 "Android" means the Android software stack for devices, as made available under the Android Open Source Project, which is located at the following URL: https://source.android.com/, as updated from time to time.  

1.2 "Android 14 GSI" means Google's generic system image of Android 14 code, excluding third party extensions.  

1.3 "Google" means Google LLC, a Delaware corporation with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, United States.  

1.4 "Google Mobile Services" means a machine-readable binary code version of the following Google applications: Search, Chrome, Gmail, Maps, YouTube, and Play, and certain other associated applications, in each case, as provided under this License Agreement. Google Mobile Services are collectively referred to in the License Agreement as "GMS" or each individually as a "GMS Application".  

1.5 "GMS+GSI" refers to GMS and Android 14 GSI, collectively.  

### 2. Accepting this License Agreement

2.1 In order to use GMS+GSI, you must first agree to the License Agreement. You may not use GMS+GSI if you do not accept the License Agreement.  

2.2 By clicking to accept, you hereby agree to the terms of the License Agreement.  

2.3 You may not use GMS+GSI and may not accept the License Agreement if you are a person barred from receiving GMS+GSI under the laws of the United States or other countries, including the country in which you are resident or from which you use GMS+GSI.  

2.4 If you are agreeing to be bound by the License Agreement on behalf of your employer or other entity, you represent and warrant that you have full legal authority to bind your employer or such entity to the License Agreement. If you do not have the requisite authority, you may not accept the License Agreement or use GMS+GSI on behalf of your employer or other entity.  

### 3. GMS+GSI License from Google

3.1 Subject to the terms of the License Agreement, Google grants you a limited, worldwide, royalty-free, non-assignable, non-exclusive, and non-sublicensable license to use GMS+GSI solely for testing applications for compatibility with Android 14.  

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

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 14 GSI Release </button> [Download Android 14 GSI Release](https://dl.google.com/developers/android/udc/images/gsi/gsi_gms_arm64-exp-UP1A.231005.007-10754064-77f9c9df.zip)

*gsi_gms_arm64-exp-UP1A.231005.007-10754064-77f9c9df.zip*

### Download Android 14 GSI Release

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

This is the Early Access Google Mobile Services and Android 14 GSI License Agreement ("License Agreement"). Google Mobile Services and Android 14 GSI (each defined below) are licensed to you subject to the terms of the License Agreement. The License Agreement forms a legally binding contract between you and Google in relation to your use of Google Mobile Services and Android 14 GSI.  

### 1. Definitions

1.1 "Android" means the Android software stack for devices, as made available under the Android Open Source Project, which is located at the following URL: https://source.android.com/, as updated from time to time.  

1.2 "Android 14 GSI" means Google's generic system image of Android 14 code, excluding third party extensions.  

1.3 "Google" means Google LLC, a Delaware corporation with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, United States.  

1.4 "Google Mobile Services" means a machine-readable binary code version of the following Google applications: Search, Chrome, Gmail, Maps, YouTube, and Play, and certain other associated applications, in each case, as provided under this License Agreement. Google Mobile Services are collectively referred to in the License Agreement as "GMS" or each individually as a "GMS Application".  

1.5 "GMS+GSI" refers to GMS and Android 14 GSI, collectively.  

### 2. Accepting this License Agreement

2.1 In order to use GMS+GSI, you must first agree to the License Agreement. You may not use GMS+GSI if you do not accept the License Agreement.  

2.2 By clicking to accept, you hereby agree to the terms of the License Agreement.  

2.3 You may not use GMS+GSI and may not accept the License Agreement if you are a person barred from receiving GMS+GSI under the laws of the United States or other countries, including the country in which you are resident or from which you use GMS+GSI.  

2.4 If you are agreeing to be bound by the License Agreement on behalf of your employer or other entity, you represent and warrant that you have full legal authority to bind your employer or such entity to the License Agreement. If you do not have the requisite authority, you may not accept the License Agreement or use GMS+GSI on behalf of your employer or other entity.  

### 3. GMS+GSI License from Google

3.1 Subject to the terms of the License Agreement, Google grants you a limited, worldwide, royalty-free, non-assignable, non-exclusive, and non-sublicensable license to use GMS+GSI solely for testing applications for compatibility with Android 14.  

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

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 14 GSI Release </button> [Download Android 14 GSI Release](https://dl.google.com/developers/android/udc/images/gsi/gsi_gms_x86_64-exp-UP1A.231005.007-10754064-a42e6bb7.zip)

*gsi_gms_x86_64-exp-UP1A.231005.007-10754064-a42e6bb7.zip*

### Download Android 14 GSI Release

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

This is the Early Access Google Mobile Services and Android 14 GSI License Agreement ("License Agreement"). Google Mobile Services and Android 14 GSI (each defined below) are licensed to you subject to the terms of the License Agreement. The License Agreement forms a legally binding contract between you and Google in relation to your use of Google Mobile Services and Android 14 GSI.  

### 1. Definitions

1.1 "Android" means the Android software stack for devices, as made available under the Android Open Source Project, which is located at the following URL: https://source.android.com/, as updated from time to time.  

1.2 "Android 14 GSI" means Google's generic system image of Android 14 code, excluding third party extensions.  

1.3 "Google" means Google LLC, a Delaware corporation with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, United States.  

1.4 "Google Mobile Services" means a machine-readable binary code version of the following Google applications: Search, Chrome, Gmail, Maps, YouTube, and Play, and certain other associated applications, in each case, as provided under this License Agreement. Google Mobile Services are collectively referred to in the License Agreement as "GMS" or each individually as a "GMS Application".  

1.5 "GMS+GSI" refers to GMS and Android 14 GSI, collectively.  

### 2. Accepting this License Agreement

2.1 In order to use GMS+GSI, you must first agree to the License Agreement. You may not use GMS+GSI if you do not accept the License Agreement.  

2.2 By clicking to accept, you hereby agree to the terms of the License Agreement.  

2.3 You may not use GMS+GSI and may not accept the License Agreement if you are a person barred from receiving GMS+GSI under the laws of the United States or other countries, including the country in which you are resident or from which you use GMS+GSI.  

2.4 If you are agreeing to be bound by the License Agreement on behalf of your employer or other entity, you represent and warrant that you have full legal authority to bind your employer or such entity to the License Agreement. If you do not have the requisite authority, you may not accept the License Agreement or use GMS+GSI on behalf of your employer or other entity.  

### 3. GMS+GSI License from Google

3.1 Subject to the terms of the License Agreement, Google grants you a limited, worldwide, royalty-free, non-assignable, non-exclusive, and non-sublicensable license to use GMS+GSI solely for testing applications for compatibility with Android 14.  

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

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 14 GSI Release </button> [Download Android 14 GSI Release](https://dl.google.com/developers/android/udc/images/gsi/aosp_arm64-exp-UP1A.231005.007-10754064-68dd726a.zip)

*aosp_arm64-exp-UP1A.231005.007-10754064-68dd726a.zip*

### Download Android 14 GSI Release

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

This is the Early Access Google Mobile Services and Android 14 GSI License Agreement ("License Agreement"). Google Mobile Services and Android 14 GSI (each defined below) are licensed to you subject to the terms of the License Agreement. The License Agreement forms a legally binding contract between you and Google in relation to your use of Google Mobile Services and Android 14 GSI.  

### 1. Definitions

1.1 "Android" means the Android software stack for devices, as made available under the Android Open Source Project, which is located at the following URL: https://source.android.com/, as updated from time to time.  

1.2 "Android 14 GSI" means Google's generic system image of Android 14 code, excluding third party extensions.  

1.3 "Google" means Google LLC, a Delaware corporation with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, United States.  

1.4 "Google Mobile Services" means a machine-readable binary code version of the following Google applications: Search, Chrome, Gmail, Maps, YouTube, and Play, and certain other associated applications, in each case, as provided under this License Agreement. Google Mobile Services are collectively referred to in the License Agreement as "GMS" or each individually as a "GMS Application".  

1.5 "GMS+GSI" refers to GMS and Android 14 GSI, collectively.  

### 2. Accepting this License Agreement

2.1 In order to use GMS+GSI, you must first agree to the License Agreement. You may not use GMS+GSI if you do not accept the License Agreement.  

2.2 By clicking to accept, you hereby agree to the terms of the License Agreement.  

2.3 You may not use GMS+GSI and may not accept the License Agreement if you are a person barred from receiving GMS+GSI under the laws of the United States or other countries, including the country in which you are resident or from which you use GMS+GSI.  

2.4 If you are agreeing to be bound by the License Agreement on behalf of your employer or other entity, you represent and warrant that you have full legal authority to bind your employer or such entity to the License Agreement. If you do not have the requisite authority, you may not accept the License Agreement or use GMS+GSI on behalf of your employer or other entity.  

### 3. GMS+GSI License from Google

3.1 Subject to the terms of the License Agreement, Google grants you a limited, worldwide, royalty-free, non-assignable, non-exclusive, and non-sublicensable license to use GMS+GSI solely for testing applications for compatibility with Android 14.  

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

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 14 GSI Release </button> [Download Android 14 GSI Release](https://dl.google.com/developers/android/udc/images/gsi/aosp_x86_64-exp-UP1A.231005.007-10754064-84570261.zip)

*aosp_x86_64-exp-UP1A.231005.007-10754064-84570261.zip*

### Known issues with Android 14 GSIs

Android 14 GSI binaries have the following GSI-specific known issues that might
occur with some devices and builds:

- **Power Cycle**: Rebooting GSI might fail on some devices. To work around it, reboot the device into recovery mode, erase user data, perform a factory reset, and then reboot the device.
- **System partition size** : GSI + GMS file size (images named `_gsi\_gms\_arm64-*_`) might be bigger than the default dynamic system partition size on your device. To work around this issue, you can delete some non-essential dynamic partitions, such as the product partition, and flash the GSI again. For more information, see the [flashing GSIs
  documentation](https://source.android.com/setup/build/gsi#flashing-gsis).

## Android 13 GSIs

GSI binaries for Android 13 are built from the same AOSP and GMS sources as the
[corresponding Google Pixel builds](https://developer.android.com/about/versions/13/get#on_pixel). These
binaries contain the same API and SDK, have a similar CTS result, and have been
validated on the following Pixel devices:

- Pixel 4 and 4 XL
- Pixel 4a and 4a (5G)
- Pixel 5 and 5a
- Pixel 6 and 6 Pro
- Pixel 7 and 7 Pro
- Pixel Fold
- Pixel Tablet

### Android 13 QPR3

    Date: April 20, 2023
    Build: T3B3.230413.003
    Security patch level: April 2023
    Google Play Services: 23.06.18

| Type | Download Link and SHA-256 Checksum |
|---|---|
| ARM64+GMS | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="arm64-gms" data-modal-dialog-id="a13_gms_arm64_GSI_zip">gsi_gms_arm64-exp-T3B3.230413.003-9957835-c059e7b4.zip</button> `c059e7b4245c76073617504de8d43dbcea65d9d39e3c2ffdcc9c578ea0164899` |
| ARM64 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="arm64" data-modal-dialog-id="a13_aosp_arm64_GSI_zip">aosp_arm64-exp-T3B3.230413.003-9957835-d7b72a80.zip</button> `d7b72a808b1d77f047a19749cf2e218967a60dc18b611d2c44bfc0daf3dc269f` |
| x86_64+GMS | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="x86_64-gms" data-modal-dialog-id="a13_gms_x86_64_GSI_zip">gsi_gms_x86_64-exp-T3B3.230413.003-9957835-32e0e453.zip</button> `32e0e453d0347c5b1868c14678ea33c2bee41e02a59bcb677acae82abee30416` |
| x86_64 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="x86_64" data-modal-dialog-id="a13_aosp_x86_64_GSI_zip">aosp_x86_64-exp-T3B3.230413.003-9957835-3eb1f453.zip</button> `3eb1f4536c22f8785b9fe3879ec09bdb3c30f17b187945d3f80b90f9f5965743` |

### Download Android 13 GSI Release

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

This is the Early Access Google Mobile Services and Android 13 GSI License Agreement ("License Agreement"). Google Mobile Services and Android 13 GSI (each defined below) are licensed to you subject to the terms of the License Agreement. The License Agreement forms a legally binding contract between you and Google in relation to your use of Google Mobile Services and Android 13 GSI.  

### 1. Definitions

1.1 "Android" means the Android software stack for devices, as made available under the Android Open Source Project, which is located at the following URL: https://source.android.com/, as updated from time to time.  

1.2 "Android 13 GSI" means Google's generic system image of Android 13 code, excluding third party extensions.  

1.3 "Google" means Google LLC, a Delaware corporation with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, United States.  

1.4 "Google Mobile Services" means a machine-readable binary code version of the following Google applications: Search, Chrome, Gmail, Maps, YouTube, and Play, and certain other associated applications, in each case, as provided under this License Agreement. Google Mobile Services are collectively referred to in the License Agreement as "GMS" or each individually as a "GMS Application".  

1.5 "GMS+GSI" refers to GMS and Android 13 GSI, collectively.  

### 2. Accepting this License Agreement

2.1 In order to use GMS+GSI, you must first agree to the License Agreement. You may not use GMS+GSI if you do not accept the License Agreement.  

2.2 By clicking to accept, you hereby agree to the terms of the License Agreement.  

2.3 You may not use GMS+GSI and may not accept the License Agreement if you are a person barred from receiving GMS+GSI under the laws of the United States or other countries, including the country in which you are resident or from which you use GMS+GSI.  

2.4 If you are agreeing to be bound by the License Agreement on behalf of your employer or other entity, you represent and warrant that you have full legal authority to bind your employer or such entity to the License Agreement. If you do not have the requisite authority, you may not accept the License Agreement or use GMS+GSI on behalf of your employer or other entity.  

### 3. GMS+GSI License from Google

3.1 Subject to the terms of the License Agreement, Google grants you a limited, worldwide, royalty-free, non-assignable, non-exclusive, and non-sublicensable license to use GMS+GSI solely for testing applications for compatibility with Android 13.  

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

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 13 GSI Release </button> [Download Android 13 GSI Release](https://dl.google.com/developers/android/tm/images/gsi/gsi_gms_arm64-exp-T3B3.230413.003-9957835-c059e7b4.zip)

*gsi_gms_arm64-exp-T3B3.230413.003-9957835-c059e7b4.zip*

### Download Android 13 GSI Release

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

This is the Early Access Google Mobile Services and Android 13 GSI License Agreement ("License Agreement"). Google Mobile Services and Android 13 GSI (each defined below) are licensed to you subject to the terms of the License Agreement. The License Agreement forms a legally binding contract between you and Google in relation to your use of Google Mobile Services and Android 13 GSI.  

### 1. Definitions

1.1 "Android" means the Android software stack for devices, as made available under the Android Open Source Project, which is located at the following URL: https://source.android.com/, as updated from time to time.  

1.2 "Android 13 GSI" means Google's generic system image of Android 13 code, excluding third party extensions.  

1.3 "Google" means Google LLC, a Delaware corporation with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, United States.  

1.4 "Google Mobile Services" means a machine-readable binary code version of the following Google applications: Search, Chrome, Gmail, Maps, YouTube, and Play, and certain other associated applications, in each case, as provided under this License Agreement. Google Mobile Services are collectively referred to in the License Agreement as "GMS" or each individually as a "GMS Application".  

1.5 "GMS+GSI" refers to GMS and Android 13 GSI, collectively.  

### 2. Accepting this License Agreement

2.1 In order to use GMS+GSI, you must first agree to the License Agreement. You may not use GMS+GSI if you do not accept the License Agreement.  

2.2 By clicking to accept, you hereby agree to the terms of the License Agreement.  

2.3 You may not use GMS+GSI and may not accept the License Agreement if you are a person barred from receiving GMS+GSI under the laws of the United States or other countries, including the country in which you are resident or from which you use GMS+GSI.  

2.4 If you are agreeing to be bound by the License Agreement on behalf of your employer or other entity, you represent and warrant that you have full legal authority to bind your employer or such entity to the License Agreement. If you do not have the requisite authority, you may not accept the License Agreement or use GMS+GSI on behalf of your employer or other entity.  

### 3. GMS+GSI License from Google

3.1 Subject to the terms of the License Agreement, Google grants you a limited, worldwide, royalty-free, non-assignable, non-exclusive, and non-sublicensable license to use GMS+GSI solely for testing applications for compatibility with Android 13.  

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

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 13 GSI Release </button> [Download Android 13 GSI Release](https://dl.google.com/developers/android/tm/images/gsi/gsi_gms_x86_64-exp-T3B3.230413.003-9957835-32e0e453.zip)

*gsi_gms_x86_64-exp-T3B3.230413.003-9957835-32e0e453.zip*

### Download Android 13 GSI Release

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

This is the Early Access Google Mobile Services and Android 13 GSI License Agreement ("License Agreement"). Google Mobile Services and Android 13 GSI (each defined below) are licensed to you subject to the terms of the License Agreement. The License Agreement forms a legally binding contract between you and Google in relation to your use of Google Mobile Services and Android 13 GSI.  

### 1. Definitions

1.1 "Android" means the Android software stack for devices, as made available under the Android Open Source Project, which is located at the following URL: https://source.android.com/, as updated from time to time.  

1.2 "Android 13 GSI" means Google's generic system image of Android 13 code, excluding third party extensions.  

1.3 "Google" means Google LLC, a Delaware corporation with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, United States.  

1.4 "Google Mobile Services" means a machine-readable binary code version of the following Google applications: Search, Chrome, Gmail, Maps, YouTube, and Play, and certain other associated applications, in each case, as provided under this License Agreement. Google Mobile Services are collectively referred to in the License Agreement as "GMS" or each individually as a "GMS Application".  

1.5 "GMS+GSI" refers to GMS and Android 13 GSI, collectively.  

### 2. Accepting this License Agreement

2.1 In order to use GMS+GSI, you must first agree to the License Agreement. You may not use GMS+GSI if you do not accept the License Agreement.  

2.2 By clicking to accept, you hereby agree to the terms of the License Agreement.  

2.3 You may not use GMS+GSI and may not accept the License Agreement if you are a person barred from receiving GMS+GSI under the laws of the United States or other countries, including the country in which you are resident or from which you use GMS+GSI.  

2.4 If you are agreeing to be bound by the License Agreement on behalf of your employer or other entity, you represent and warrant that you have full legal authority to bind your employer or such entity to the License Agreement. If you do not have the requisite authority, you may not accept the License Agreement or use GMS+GSI on behalf of your employer or other entity.  

### 3. GMS+GSI License from Google

3.1 Subject to the terms of the License Agreement, Google grants you a limited, worldwide, royalty-free, non-assignable, non-exclusive, and non-sublicensable license to use GMS+GSI solely for testing applications for compatibility with Android 13.  

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

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 13 GSI Release </button> [Download Android 13 GSI Release](https://dl.google.com/developers/android/tm/images/gsi/aosp_arm64-exp-T3B3.230413.003-9957835-d7b72a80.zip)

*aosp_arm64-exp-T3B3.230413.003-9957835-d7b72a80.zip*

### Download Android 13 GSI Release

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

This is the Early Access Google Mobile Services and Android 13 GSI License Agreement ("License Agreement"). Google Mobile Services and Android 13 GSI (each defined below) are licensed to you subject to the terms of the License Agreement. The License Agreement forms a legally binding contract between you and Google in relation to your use of Google Mobile Services and Android 13 GSI.  

### 1. Definitions

1.1 "Android" means the Android software stack for devices, as made available under the Android Open Source Project, which is located at the following URL: https://source.android.com/, as updated from time to time.  

1.2 "Android 13 GSI" means Google's generic system image of Android 13 code, excluding third party extensions.  

1.3 "Google" means Google LLC, a Delaware corporation with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, United States.  

1.4 "Google Mobile Services" means a machine-readable binary code version of the following Google applications: Search, Chrome, Gmail, Maps, YouTube, and Play, and certain other associated applications, in each case, as provided under this License Agreement. Google Mobile Services are collectively referred to in the License Agreement as "GMS" or each individually as a "GMS Application".  

1.5 "GMS+GSI" refers to GMS and Android 13 GSI, collectively.  

### 2. Accepting this License Agreement

2.1 In order to use GMS+GSI, you must first agree to the License Agreement. You may not use GMS+GSI if you do not accept the License Agreement.  

2.2 By clicking to accept, you hereby agree to the terms of the License Agreement.  

2.3 You may not use GMS+GSI and may not accept the License Agreement if you are a person barred from receiving GMS+GSI under the laws of the United States or other countries, including the country in which you are resident or from which you use GMS+GSI.  

2.4 If you are agreeing to be bound by the License Agreement on behalf of your employer or other entity, you represent and warrant that you have full legal authority to bind your employer or such entity to the License Agreement. If you do not have the requisite authority, you may not accept the License Agreement or use GMS+GSI on behalf of your employer or other entity.  

### 3. GMS+GSI License from Google

3.1 Subject to the terms of the License Agreement, Google grants you a limited, worldwide, royalty-free, non-assignable, non-exclusive, and non-sublicensable license to use GMS+GSI solely for testing applications for compatibility with Android 13.  

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

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 13 GSI Release </button> [Download Android 13 GSI Release](https://dl.google.com/developers/android/tm/images/gsi/aosp_x86_64-exp-T3B3.230413.003-9957835-3eb1f453.zip)

*aosp_x86_64-exp-T3B3.230413.003-9957835-3eb1f453.zip*

### Android 13 (initial, stable release)

    Date: August 7, 2023
    Build: TQ3A.230805.001.A3
    Security patch level: August 2023
    Google Play Services: 22.46.19

| Type | Download Link and SHA-256 Checksum |
|---|---|
| ARM64+GMS | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="arm64-gms" data-modal-dialog-id="a13_stable_gms_arm64_GSI_zip">gsi_gms_arm64-exp-TQ3A.230805.001.A3-10454027-3adcae59.zip</button> `3adcae59c84eb57ec65b486a3dfd800ed1a3237ad6e866362c461519b211a81f` |
| ARM64 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="arm64" data-modal-dialog-id="a13_stable_aosp_arm64_GSI_zip">aosp_arm64-exp-TQ3A.230805.001.A3-10454027-66e107ed.zip</button> `66e107edaf84b74ba1572be9a4216bf7ae45b3b7f0b516ba2b7aa365ba763905` |
| x86_64+GMS | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="x86_64-gms" data-modal-dialog-id="a13_stable_gms_x86_64_GSI_zip">gsi_gms_x86_64-exp-TQ3A.230805.001.A3-10454027-608e3418.zip</button> `608e3418688802dcc158ba8509619c8d2dd3bb43896cace07a1cd12709443555` |
| x86_64 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="x86_64" data-modal-dialog-id="a13_stable_aosp_x86_64_GSI_zip">aosp_x86_64-exp-TQ3A.230805.001.A3-10454027-989de7fa.zip</button> `989de7fa2b97945220a650c5dd7f0e858d601916a1d4a8b89674211979840f33` |

### Download Android 13 GSI Release

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

This is the Early Access Google Mobile Services and Android 13 GSI License Agreement ("License Agreement"). Google Mobile Services and Android 13 GSI (each defined below) are licensed to you subject to the terms of the License Agreement. The License Agreement forms a legally binding contract between you and Google in relation to your use of Google Mobile Services and Android 13 GSI.  

### 1. Definitions

1.1 "Android" means the Android software stack for devices, as made available under the Android Open Source Project, which is located at the following URL: https://source.android.com/, as updated from time to time.  

1.2 "Android 13 GSI" means Google's generic system image of Android 13 code, excluding third party extensions.  

1.3 "Google" means Google LLC, a Delaware corporation with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, United States.  

1.4 "Google Mobile Services" means a machine-readable binary code version of the following Google applications: Search, Chrome, Gmail, Maps, YouTube, and Play, and certain other associated applications, in each case, as provided under this License Agreement. Google Mobile Services are collectively referred to in the License Agreement as "GMS" or each individually as a "GMS Application".  

1.5 "GMS+GSI" refers to GMS and Android 13 GSI, collectively.  

### 2. Accepting this License Agreement

2.1 In order to use GMS+GSI, you must first agree to the License Agreement. You may not use GMS+GSI if you do not accept the License Agreement.  

2.2 By clicking to accept, you hereby agree to the terms of the License Agreement.  

2.3 You may not use GMS+GSI and may not accept the License Agreement if you are a person barred from receiving GMS+GSI under the laws of the United States or other countries, including the country in which you are resident or from which you use GMS+GSI.  

2.4 If you are agreeing to be bound by the License Agreement on behalf of your employer or other entity, you represent and warrant that you have full legal authority to bind your employer or such entity to the License Agreement. If you do not have the requisite authority, you may not accept the License Agreement or use GMS+GSI on behalf of your employer or other entity.  

### 3. GMS+GSI License from Google

3.1 Subject to the terms of the License Agreement, Google grants you a limited, worldwide, royalty-free, non-assignable, non-exclusive, and non-sublicensable license to use GMS+GSI solely for testing applications for compatibility with Android 13.  

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

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 13 GSI Release </button> [Download Android 13 GSI Release](https://dl.google.com/developers/android/tm/images/gsi/gsi_gms_arm64-exp-TQ3A.230805.001.A3-10454027-3adcae59.zip)

*gsi_gms_arm64-exp-TQ3A.230805.001.A3-10454027-3adcae59.zip*

### Download Android 13 GSI Release

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

This is the Early Access Google Mobile Services and Android 13 GSI License Agreement ("License Agreement"). Google Mobile Services and Android 13 GSI (each defined below) are licensed to you subject to the terms of the License Agreement. The License Agreement forms a legally binding contract between you and Google in relation to your use of Google Mobile Services and Android 13 GSI.  

### 1. Definitions

1.1 "Android" means the Android software stack for devices, as made available under the Android Open Source Project, which is located at the following URL: https://source.android.com/, as updated from time to time.  

1.2 "Android 13 GSI" means Google's generic system image of Android 13 code, excluding third party extensions.  

1.3 "Google" means Google LLC, a Delaware corporation with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, United States.  

1.4 "Google Mobile Services" means a machine-readable binary code version of the following Google applications: Search, Chrome, Gmail, Maps, YouTube, and Play, and certain other associated applications, in each case, as provided under this License Agreement. Google Mobile Services are collectively referred to in the License Agreement as "GMS" or each individually as a "GMS Application".  

1.5 "GMS+GSI" refers to GMS and Android 13 GSI, collectively.  

### 2. Accepting this License Agreement

2.1 In order to use GMS+GSI, you must first agree to the License Agreement. You may not use GMS+GSI if you do not accept the License Agreement.  

2.2 By clicking to accept, you hereby agree to the terms of the License Agreement.  

2.3 You may not use GMS+GSI and may not accept the License Agreement if you are a person barred from receiving GMS+GSI under the laws of the United States or other countries, including the country in which you are resident or from which you use GMS+GSI.  

2.4 If you are agreeing to be bound by the License Agreement on behalf of your employer or other entity, you represent and warrant that you have full legal authority to bind your employer or such entity to the License Agreement. If you do not have the requisite authority, you may not accept the License Agreement or use GMS+GSI on behalf of your employer or other entity.  

### 3. GMS+GSI License from Google

3.1 Subject to the terms of the License Agreement, Google grants you a limited, worldwide, royalty-free, non-assignable, non-exclusive, and non-sublicensable license to use GMS+GSI solely for testing applications for compatibility with Android 13.  

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

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 13 GSI Release </button> [Download Android 13 GSI Release](https://dl.google.com/developers/android/tm/images/gsi/gsi_gms_x86_64-exp-TQ3A.230805.001.A3-10454027-608e3418.zip)

*gsi_gms_x86_64-exp-TQ3A.230805.001.A3-10454027-608e3418.zip*

### Download Android 13 GSI Release

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

This is the Early Access Google Mobile Services and Android 13 GSI License Agreement ("License Agreement"). Google Mobile Services and Android 13 GSI (each defined below) are licensed to you subject to the terms of the License Agreement. The License Agreement forms a legally binding contract between you and Google in relation to your use of Google Mobile Services and Android 13 GSI.  

### 1. Definitions

1.1 "Android" means the Android software stack for devices, as made available under the Android Open Source Project, which is located at the following URL: https://source.android.com/, as updated from time to time.  

1.2 "Android 13 GSI" means Google's generic system image of Android 13 code, excluding third party extensions.  

1.3 "Google" means Google LLC, a Delaware corporation with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, United States.  

1.4 "Google Mobile Services" means a machine-readable binary code version of the following Google applications: Search, Chrome, Gmail, Maps, YouTube, and Play, and certain other associated applications, in each case, as provided under this License Agreement. Google Mobile Services are collectively referred to in the License Agreement as "GMS" or each individually as a "GMS Application".  

1.5 "GMS+GSI" refers to GMS and Android 13 GSI, collectively.  

### 2. Accepting this License Agreement

2.1 In order to use GMS+GSI, you must first agree to the License Agreement. You may not use GMS+GSI if you do not accept the License Agreement.  

2.2 By clicking to accept, you hereby agree to the terms of the License Agreement.  

2.3 You may not use GMS+GSI and may not accept the License Agreement if you are a person barred from receiving GMS+GSI under the laws of the United States or other countries, including the country in which you are resident or from which you use GMS+GSI.  

2.4 If you are agreeing to be bound by the License Agreement on behalf of your employer or other entity, you represent and warrant that you have full legal authority to bind your employer or such entity to the License Agreement. If you do not have the requisite authority, you may not accept the License Agreement or use GMS+GSI on behalf of your employer or other entity.  

### 3. GMS+GSI License from Google

3.1 Subject to the terms of the License Agreement, Google grants you a limited, worldwide, royalty-free, non-assignable, non-exclusive, and non-sublicensable license to use GMS+GSI solely for testing applications for compatibility with Android 13.  

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

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 13 GSI Release </button> [Download Android 13 GSI Release](https://dl.google.com/developers/android/tm/images/gsi/aosp_arm64-exp-TQ3A.230805.001.A3-10454027-66e107ed.zip)

*aosp_arm64-exp-TQ3A.230805.001.A3-10454027-66e107ed.zip*

### Download Android 13 GSI Release

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

This is the Early Access Google Mobile Services and Android 13 GSI License Agreement ("License Agreement"). Google Mobile Services and Android 13 GSI (each defined below) are licensed to you subject to the terms of the License Agreement. The License Agreement forms a legally binding contract between you and Google in relation to your use of Google Mobile Services and Android 13 GSI.  

### 1. Definitions

1.1 "Android" means the Android software stack for devices, as made available under the Android Open Source Project, which is located at the following URL: https://source.android.com/, as updated from time to time.  

1.2 "Android 13 GSI" means Google's generic system image of Android 13 code, excluding third party extensions.  

1.3 "Google" means Google LLC, a Delaware corporation with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, United States.  

1.4 "Google Mobile Services" means a machine-readable binary code version of the following Google applications: Search, Chrome, Gmail, Maps, YouTube, and Play, and certain other associated applications, in each case, as provided under this License Agreement. Google Mobile Services are collectively referred to in the License Agreement as "GMS" or each individually as a "GMS Application".  

1.5 "GMS+GSI" refers to GMS and Android 13 GSI, collectively.  

### 2. Accepting this License Agreement

2.1 In order to use GMS+GSI, you must first agree to the License Agreement. You may not use GMS+GSI if you do not accept the License Agreement.  

2.2 By clicking to accept, you hereby agree to the terms of the License Agreement.  

2.3 You may not use GMS+GSI and may not accept the License Agreement if you are a person barred from receiving GMS+GSI under the laws of the United States or other countries, including the country in which you are resident or from which you use GMS+GSI.  

2.4 If you are agreeing to be bound by the License Agreement on behalf of your employer or other entity, you represent and warrant that you have full legal authority to bind your employer or such entity to the License Agreement. If you do not have the requisite authority, you may not accept the License Agreement or use GMS+GSI on behalf of your employer or other entity.  

### 3. GMS+GSI License from Google

3.1 Subject to the terms of the License Agreement, Google grants you a limited, worldwide, royalty-free, non-assignable, non-exclusive, and non-sublicensable license to use GMS+GSI solely for testing applications for compatibility with Android 13.  

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

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 13 GSI Release </button> [Download Android 13 GSI Release](https://dl.google.com/developers/android/tm/images/gsi/aosp_x86_64-exp-TQ3A.230805.001.A3-10454027-989de7fa.zip)

*aosp_x86_64-exp-TQ3A.230805.001.A3-10454027-989de7fa.zip*

### Known issues with Android 13 GSIs

Android 13 GSI binaries have the following GSI-specific known issues that might
occur with some devices and builds:

- **Power Cycle**: Rebooting GSI might fail on some devices. To work around it, reboot the device into recovery mode, erase user data, perform a factory reset, and then reboot the device.
- **System partition size** : GSI + GMS file size (images named `_gsi\_gms\_arm64-*_`) might be bigger than the default dynamic system partition size on your device. To work around this issue, you can delete some non-essential dynamic partitions, such as the product partition, and flash the GSI again. For more information, see the [flashing GSIs
  documentation](https://source.android.com/setup/build/gsi#flashing-gsis).

## Android 12 GSIs

GSI binaries for Android 12 are built from the same AOSP and GMS sources as the
[corresponding Google Pixel builds](https://developer.android.com/about/versions/12/get#on_pixel). These
binaries contain the same API and SDK, have a similar CTS result, and have been
validated on the following Pixel devices:

- Pixel 3 and 3 XL
- Pixel 3a and 3a XL
- Pixel 4 and 4 XL
- Pixel 4a and 4a (5G)
- Pixel 5 and Pixel 5a
- Pixel 6 and 6 Pro

    Date: July 6, 2022
    Build: SQ3A.220705.003.A1
    Security patch level: July 2022
    Google Play Services: 21.24.23

| Type | Download Link and SHA-256 Checksum |
|---|---|
| ARM64+GMS | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="arm64-gms" data-modal-dialog-id="a12_gms_arm64_GSI_zip">gsi_gms_arm64-exp-SQ3A.220705.003.A1-8672226-7230b502.zip</button> `7230b50236f01ac69dbbf62ad18051ab4d3796b921fe7c1967387517ff786681` |
| ARM64 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="arm64" data-modal-dialog-id="a12_aosp_arm64_GSI_zip">aosp_arm64-exp-SQ3A.220705.003.A1-8672226-6554a6c4.zip</button> `6554a6c462618c770648ff210500f50e48e735bdcbec57f809d95a40559f5580` |
| x86_64+GMS | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="x86_64-gms" data-modal-dialog-id="a12_gms_x86_64_GSI_zip">gsi_gms_x86_64-exp-SQ3A.220705.003.A1-8672226-e7e3f2c3.zip</button> `e7e3f2c3b55d76c6e3a46c0e9eac2093b70156b747a341a039912f7b220f39f8` |
| x86_64 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="x86_64" data-modal-dialog-id="a12_aosp_x86_64_GSI_zip">aosp_x86_64-exp-SQ3A.220705.003.A1-8672226-49fbac75.zip</button> `49fbac7526a67b8bb5dd8ce8c0259eefee56b28f491bf215959eca3144f9c8c3` |

### Download Android 12 GSI Release

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

This is the Early Access Google Mobile Services and Android 12 GSI License Agreement ("License Agreement"). Google Mobile Services and Android 12 GSI (each defined below) are licensed to you subject to the terms of the License Agreement. The License Agreement forms a legally binding contract between you and Google in relation to your use of Google Mobile Services and Android 12 GSI.  

### 1. Definitions

1.1 "Android" means the Android software stack for devices, as made available under the Android Open Source Project, which is located at the following URL: https://source.android.com/, as updated from time to time.  

1.2 "Android 12 GSI" means Google's generic system image of Android 12 code, excluding third party extensions.  

1.3 "Google" means Google LLC, a Delaware corporation with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, United States.  

1.4 "Google Mobile Services" means a machine-readable binary code version of the following Google applications: Search, Chrome, Gmail, Maps, YouTube, and Play, and certain other associated applications, in each case, as provided under this License Agreement. Google Mobile Services are collectively referred to in the License Agreement as "GMS" or each individually as a "GMS Application".  

1.5 "GMS+GSI" refers to GMS and Android 12 GSI, collectively.  

### 2. Accepting this License Agreement

2.1 In order to use GMS+GSI, you must first agree to the License Agreement. You may not use GMS+GSI if you do not accept the License Agreement.  

2.2 By clicking to accept, you hereby agree to the terms of the License Agreement.  

2.3 You may not use GMS+GSI and may not accept the License Agreement if you are a person barred from receiving GMS+GSI under the laws of the United States or other countries, including the country in which you are resident or from which you use GMS+GSI.  

2.4 If you are agreeing to be bound by the License Agreement on behalf of your employer or other entity, you represent and warrant that you have full legal authority to bind your employer or such entity to the License Agreement. If you do not have the requisite authority, you may not accept the License Agreement or use GMS+GSI on behalf of your employer or other entity.  

### 3. GMS+GSI License from Google

3.1 Subject to the terms of the License Agreement, Google grants you a limited, worldwide, royalty-free, non-assignable, non-exclusive, and non-sublicensable license to use GMS+GSI solely for testing applications for compatibility with Android 12.  

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

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 12 GSI Release </button> [Download Android 12 GSI Release](https://dl.google.com/developers/android/sc/images/gsi/gsi_gms_arm64-exp-SQ3A.220705.003.A1-8672226-7230b502.zip)

*gsi_gms_arm64-exp-SQ3A.220705.003.A1-8672226-7230b502.zip*

### Download Android 12 GSI Release

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

This is the Early Access Google Mobile Services and Android 12 GSI License Agreement ("License Agreement"). Google Mobile Services and Android 12 GSI (each defined below) are licensed to you subject to the terms of the License Agreement. The License Agreement forms a legally binding contract between you and Google in relation to your use of Google Mobile Services and Android 12 GSI.  

### 1. Definitions

1.1 "Android" means the Android software stack for devices, as made available under the Android Open Source Project, which is located at the following URL: https://source.android.com/, as updated from time to time.  

1.2 "Android 12 GSI" means Google's generic system image of Android 12 code, excluding third party extensions.  

1.3 "Google" means Google LLC, a Delaware corporation with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, United States.  

1.4 "Google Mobile Services" means a machine-readable binary code version of the following Google applications: Search, Chrome, Gmail, Maps, YouTube, and Play, and certain other associated applications, in each case, as provided under this License Agreement. Google Mobile Services are collectively referred to in the License Agreement as "GMS" or each individually as a "GMS Application".  

1.5 "GMS+GSI" refers to GMS and Android 12 GSI, collectively.  

### 2. Accepting this License Agreement

2.1 In order to use GMS+GSI, you must first agree to the License Agreement. You may not use GMS+GSI if you do not accept the License Agreement.  

2.2 By clicking to accept, you hereby agree to the terms of the License Agreement.  

2.3 You may not use GMS+GSI and may not accept the License Agreement if you are a person barred from receiving GMS+GSI under the laws of the United States or other countries, including the country in which you are resident or from which you use GMS+GSI.  

2.4 If you are agreeing to be bound by the License Agreement on behalf of your employer or other entity, you represent and warrant that you have full legal authority to bind your employer or such entity to the License Agreement. If you do not have the requisite authority, you may not accept the License Agreement or use GMS+GSI on behalf of your employer or other entity.  

### 3. GMS+GSI License from Google

3.1 Subject to the terms of the License Agreement, Google grants you a limited, worldwide, royalty-free, non-assignable, non-exclusive, and non-sublicensable license to use GMS+GSI solely for testing applications for compatibility with Android 12.  

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

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 12 GSI Release </button> [Download Android 12 GSI Release](https://dl.google.com/developers/android/sc/images/gsi/gsi_gms_x86_64-exp-SQ3A.220705.003.A1-8672226-e7e3f2c3.zip)

*gsi_gms_x86_64-exp-SQ3A.220705.003.A1-8672226-e7e3f2c3.zip*

### Download Android 12 GSI Release

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

This is the Early Access Google Mobile Services and Android 12 GSI License Agreement ("License Agreement"). Google Mobile Services and Android 12 GSI (each defined below) are licensed to you subject to the terms of the License Agreement. The License Agreement forms a legally binding contract between you and Google in relation to your use of Google Mobile Services and Android 12 GSI.  

### 1. Definitions

1.1 "Android" means the Android software stack for devices, as made available under the Android Open Source Project, which is located at the following URL: https://source.android.com/, as updated from time to time.  

1.2 "Android 12 GSI" means Google's generic system image of Android 12 code, excluding third party extensions.  

1.3 "Google" means Google LLC, a Delaware corporation with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, United States.  

1.4 "Google Mobile Services" means a machine-readable binary code version of the following Google applications: Search, Chrome, Gmail, Maps, YouTube, and Play, and certain other associated applications, in each case, as provided under this License Agreement. Google Mobile Services are collectively referred to in the License Agreement as "GMS" or each individually as a "GMS Application".  

1.5 "GMS+GSI" refers to GMS and Android 12 GSI, collectively.  

### 2. Accepting this License Agreement

2.1 In order to use GMS+GSI, you must first agree to the License Agreement. You may not use GMS+GSI if you do not accept the License Agreement.  

2.2 By clicking to accept, you hereby agree to the terms of the License Agreement.  

2.3 You may not use GMS+GSI and may not accept the License Agreement if you are a person barred from receiving GMS+GSI under the laws of the United States or other countries, including the country in which you are resident or from which you use GMS+GSI.  

2.4 If you are agreeing to be bound by the License Agreement on behalf of your employer or other entity, you represent and warrant that you have full legal authority to bind your employer or such entity to the License Agreement. If you do not have the requisite authority, you may not accept the License Agreement or use GMS+GSI on behalf of your employer or other entity.  

### 3. GMS+GSI License from Google

3.1 Subject to the terms of the License Agreement, Google grants you a limited, worldwide, royalty-free, non-assignable, non-exclusive, and non-sublicensable license to use GMS+GSI solely for testing applications for compatibility with Android 12.  

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

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 12 GSI Release </button> [Download Android 12 GSI Release](https://dl.google.com/developers/android/sc/images/gsi/aosp_arm64-exp-SQ3A.220705.003.A1-8672226-6554a6c4.zip)

*aosp_arm64-exp-SQ3A.220705.003.A1-8672226-6554a6c4.zip*

### Download Android 12 GSI Release

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

This is the Early Access Google Mobile Services and Android 12 GSI License Agreement ("License Agreement"). Google Mobile Services and Android 12 GSI (each defined below) are licensed to you subject to the terms of the License Agreement. The License Agreement forms a legally binding contract between you and Google in relation to your use of Google Mobile Services and Android 12 GSI.  

### 1. Definitions

1.1 "Android" means the Android software stack for devices, as made available under the Android Open Source Project, which is located at the following URL: https://source.android.com/, as updated from time to time.  

1.2 "Android 12 GSI" means Google's generic system image of Android 12 code, excluding third party extensions.  

1.3 "Google" means Google LLC, a Delaware corporation with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, United States.  

1.4 "Google Mobile Services" means a machine-readable binary code version of the following Google applications: Search, Chrome, Gmail, Maps, YouTube, and Play, and certain other associated applications, in each case, as provided under this License Agreement. Google Mobile Services are collectively referred to in the License Agreement as "GMS" or each individually as a "GMS Application".  

1.5 "GMS+GSI" refers to GMS and Android 12 GSI, collectively.  

### 2. Accepting this License Agreement

2.1 In order to use GMS+GSI, you must first agree to the License Agreement. You may not use GMS+GSI if you do not accept the License Agreement.  

2.2 By clicking to accept, you hereby agree to the terms of the License Agreement.  

2.3 You may not use GMS+GSI and may not accept the License Agreement if you are a person barred from receiving GMS+GSI under the laws of the United States or other countries, including the country in which you are resident or from which you use GMS+GSI.  

2.4 If you are agreeing to be bound by the License Agreement on behalf of your employer or other entity, you represent and warrant that you have full legal authority to bind your employer or such entity to the License Agreement. If you do not have the requisite authority, you may not accept the License Agreement or use GMS+GSI on behalf of your employer or other entity.  

### 3. GMS+GSI License from Google

3.1 Subject to the terms of the License Agreement, Google grants you a limited, worldwide, royalty-free, non-assignable, non-exclusive, and non-sublicensable license to use GMS+GSI solely for testing applications for compatibility with Android 12.  

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

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 12 GSI Release </button> [Download Android 12 GSI Release](https://dl.google.com/developers/android/sc/images/gsi/aosp_x86_64-exp-SQ3A.220705.003.A1-8672226-49fbac75.zip)

*aosp_x86_64-exp-SQ3A.220705.003.A1-8672226-49fbac75.zip*

### Known issues with Android 12 GSIs

Android 12 GSI binaries have the following GSI-specific known issues that might
occur with some devices and builds:

- **Phone Audio**: When using the integrated dialer, you might not hear any
  audio on the phone. This is due to a change in the telephony service
  installation location in Android 10.

- **Power Cycle**: Rebooting GSI might fail on some devices. To work around
  it, reboot the device into recovery mode, erase user data, perform a factory
  reset, and then reboot the device.

- **System partition size** : GSI + GMS file size (images named
  `_gsi\_gms\_arm64-*_`) might be bigger than the default dynamic system
  partition size on your device. To work around this issue, you can delete
  some non-essential dynamic partitions, such as the product partition, and
  flash the GSI again. For more information, see the [flashing GSIs
  documentation](https://source.android.com/setup/build/gsi#flashing-gsis).

## Android 11 GSIs

GSI binaries for Android 12 are built from the same AOSP and GMS sources as the
[corresponding Google Pixel builds](https://developer.android.com/about/versions/11/get#on_pixel). These
binaries contain the same API and SDK, have a similar CTS result, and have been
validated on the following Pixel devices:

- Pixel 2 and 2 XL
- Pixel 3 and 3 XL
- Pixel 3a and 3a XL
- Pixel 4 and 4 XL

    Date: September 8, 2020
    Build: RP1A.200720.009
    Security patch level: September 2020
    Google Play Services: 20.30.19

| Type | Download Link and SHA-256 Checksum |
|---|---|
| ARM64+GMS | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="arm64-gms" data-modal-dialog-id="RPA_gms_arm64_GSI_zip">gsi_gms_arm64-exp-RP1A.200720.009-6720564-c8273882.zip</button> `c8273882af89b07a3701771b114c2f4ddad4076942adf745b72ed8c40fa13c12` |
| ARM64 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="arm64" data-modal-dialog-id="RPA_aosp_arm64_GSI_zip">aosp_arm64-exp-RP1A.200720.009-6720564-019b517d.zip</button> `019b517dad4c3ee475302b4e8e96fe35934968a083c4edfe387611f08e2f71bc` |
| x86+GMS | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="x86-gms" data-modal-dialog-id="RPA_gms_x86_GSI_zip">gsi_gms_x86-exp-RP1A.200720.009-6720564-a5225575.zip</button> `a5225575a3b12146c399d1d0ac7661c6c10b07053fb678657cff6c712f1cd782` |
| x86_64 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="x86_64" data-modal-dialog-id="RPA_aosp_x86_64_GSI_zip">aosp_x86_64-exp-RP1A.200720.009-6720564-a541e9e4.zip</button> `a541e9e40edfdf708f071e7ee14ef21f499c5a84cff7a61268cf0a5b3dff7bf5` |

### Download Android 11 GSI Release

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

This is the Early Access Google Mobile Services and Android 11 GSI License Agreement ("License Agreement"). Google Mobile Services and Android 11 GSI (each defined below) are licensed to you subject to the terms of the License Agreement. The License Agreement forms a legally binding contract between you and Google in relation to your use of Google Mobile Services and Android 11 GSI.  

### 1. Definitions

1.1 "Android" means the Android software stack for devices, as made available under the Android Open Source Project, which is located at the following URL: https://source.android.com/, as updated from time to time.  

1.2 "Android 11 GSI" means Google's generic system image of Android 11 code, excluding third party extensions.  

1.3 "Google" means Google LLC, a Delaware corporation with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, United States.  

1.4 "Google Mobile Services" means a machine-readable binary code version of the following Google applications: Search, Chrome, Gmail, Maps, YouTube, and Play, and certain other associated applications, in each case, as provided under this License Agreement. Google Mobile Services are collectively referred to in the License Agreement as "GMS" or each individually as a "GMS Application".  

1.5 "GMS+GSI" refers to GMS and Android 11 GSI, collectively.  

### 2. Accepting this License Agreement

2.1 In order to use GMS+GSI, you must first agree to the License Agreement. You may not use GMS+GSI if you do not accept the License Agreement.  

2.2 By clicking to accept, you hereby agree to the terms of the License Agreement.  

2.3 You may not use GMS+GSI and may not accept the License Agreement if you are a person barred from receiving GMS+GSI under the laws of the United States or other countries, including the country in which you are resident or from which you use GMS+GSI.  

2.4 If you are agreeing to be bound by the License Agreement on behalf of your employer or other entity, you represent and warrant that you have full legal authority to bind your employer or such entity to the License Agreement. If you do not have the requisite authority, you may not accept the License Agreement or use GMS+GSI on behalf of your employer or other entity.  

### 3. GMS+GSI License from Google

3.1 Subject to the terms of the License Agreement, Google grants you a limited, worldwide, royalty-free, non-assignable, non-exclusive, and non-sublicensable license to use GMS+GSI solely for testing applications for compatibility with Android 11.  

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

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 11 GSI Release </button> [Download Android 11 GSI Release](https://dl.google.com/developers/android/rvc/images/gsi/gsi_gms_arm64-exp-RP1A.200720.009-6720564-c8273882.zip)

*gsi_gms_arm64-exp-RP1A.200720.009-6720564-c8273882.zip*

### Download Android 11 GSI Release

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

This is the Early Access Google Mobile Services and Android 11 GSI License Agreement ("License Agreement"). Google Mobile Services and Android 11 GSI (each defined below) are licensed to you subject to the terms of the License Agreement. The License Agreement forms a legally binding contract between you and Google in relation to your use of Google Mobile Services and Android 11 GSI.  

### 1. Definitions

1.1 "Android" means the Android software stack for devices, as made available under the Android Open Source Project, which is located at the following URL: https://source.android.com/, as updated from time to time.  

1.2 "Android 11 GSI" means Google's generic system image of Android 11 code, excluding third party extensions.  

1.3 "Google" means Google LLC, a Delaware corporation with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, United States.  

1.4 "Google Mobile Services" means a machine-readable binary code version of the following Google applications: Search, Chrome, Gmail, Maps, YouTube, and Play, and certain other associated applications, in each case, as provided under this License Agreement. Google Mobile Services are collectively referred to in the License Agreement as "GMS" or each individually as a "GMS Application".  

1.5 "GMS+GSI" refers to GMS and Android 11 GSI, collectively.  

### 2. Accepting this License Agreement

2.1 In order to use GMS+GSI, you must first agree to the License Agreement. You may not use GMS+GSI if you do not accept the License Agreement.  

2.2 By clicking to accept, you hereby agree to the terms of the License Agreement.  

2.3 You may not use GMS+GSI and may not accept the License Agreement if you are a person barred from receiving GMS+GSI under the laws of the United States or other countries, including the country in which you are resident or from which you use GMS+GSI.  

2.4 If you are agreeing to be bound by the License Agreement on behalf of your employer or other entity, you represent and warrant that you have full legal authority to bind your employer or such entity to the License Agreement. If you do not have the requisite authority, you may not accept the License Agreement or use GMS+GSI on behalf of your employer or other entity.  

### 3. GMS+GSI License from Google

3.1 Subject to the terms of the License Agreement, Google grants you a limited, worldwide, royalty-free, non-assignable, non-exclusive, and non-sublicensable license to use GMS+GSI solely for testing applications for compatibility with Android 11.  

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

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 11 GSI Release </button> [Download Android 11 GSI Release](https://dl.google.com/developers/android/rvc/images/gsi/gsi_gms_x86-exp-RP1A.200720.009-6720564-a5225575.zip)

*gsi_gms_x86-exp-RP1A.200720.009-6720564-a5225575.zip*

### Download Android 11 GSI Release

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

This is the Early Access Google Mobile Services and Android 11 GSI License Agreement ("License Agreement"). Google Mobile Services and Android 11 GSI (each defined below) are licensed to you subject to the terms of the License Agreement. The License Agreement forms a legally binding contract between you and Google in relation to your use of Google Mobile Services and Android 11 GSI.  

### 1. Definitions

1.1 "Android" means the Android software stack for devices, as made available under the Android Open Source Project, which is located at the following URL: https://source.android.com/, as updated from time to time.  

1.2 "Android 11 GSI" means Google's generic system image of Android 11 code, excluding third party extensions.  

1.3 "Google" means Google LLC, a Delaware corporation with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, United States.  

1.4 "Google Mobile Services" means a machine-readable binary code version of the following Google applications: Search, Chrome, Gmail, Maps, YouTube, and Play, and certain other associated applications, in each case, as provided under this License Agreement. Google Mobile Services are collectively referred to in the License Agreement as "GMS" or each individually as a "GMS Application".  

1.5 "GMS+GSI" refers to GMS and Android 11 GSI, collectively.  

### 2. Accepting this License Agreement

2.1 In order to use GMS+GSI, you must first agree to the License Agreement. You may not use GMS+GSI if you do not accept the License Agreement.  

2.2 By clicking to accept, you hereby agree to the terms of the License Agreement.  

2.3 You may not use GMS+GSI and may not accept the License Agreement if you are a person barred from receiving GMS+GSI under the laws of the United States or other countries, including the country in which you are resident or from which you use GMS+GSI.  

2.4 If you are agreeing to be bound by the License Agreement on behalf of your employer or other entity, you represent and warrant that you have full legal authority to bind your employer or such entity to the License Agreement. If you do not have the requisite authority, you may not accept the License Agreement or use GMS+GSI on behalf of your employer or other entity.  

### 3. GMS+GSI License from Google

3.1 Subject to the terms of the License Agreement, Google grants you a limited, worldwide, royalty-free, non-assignable, non-exclusive, and non-sublicensable license to use GMS+GSI solely for testing applications for compatibility with Android 11.  

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

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 11 GSI Release </button> [Download Android 11 GSI Release](https://dl.google.com/developers/android/rvc/images/gsi/aosp_arm64-exp-RP1A.200720.009-6720564-019b517d.zip)

*aosp_arm64-exp-RP1A.200720.009-6720564-019b517d.zip*

### Download Android 11 GSI Release

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

This is the Early Access Google Mobile Services and Android 11 GSI License Agreement ("License Agreement"). Google Mobile Services and Android 11 GSI (each defined below) are licensed to you subject to the terms of the License Agreement. The License Agreement forms a legally binding contract between you and Google in relation to your use of Google Mobile Services and Android 11 GSI.  

### 1. Definitions

1.1 "Android" means the Android software stack for devices, as made available under the Android Open Source Project, which is located at the following URL: https://source.android.com/, as updated from time to time.  

1.2 "Android 11 GSI" means Google's generic system image of Android 11 code, excluding third party extensions.  

1.3 "Google" means Google LLC, a Delaware corporation with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, United States.  

1.4 "Google Mobile Services" means a machine-readable binary code version of the following Google applications: Search, Chrome, Gmail, Maps, YouTube, and Play, and certain other associated applications, in each case, as provided under this License Agreement. Google Mobile Services are collectively referred to in the License Agreement as "GMS" or each individually as a "GMS Application".  

1.5 "GMS+GSI" refers to GMS and Android 11 GSI, collectively.  

### 2. Accepting this License Agreement

2.1 In order to use GMS+GSI, you must first agree to the License Agreement. You may not use GMS+GSI if you do not accept the License Agreement.  

2.2 By clicking to accept, you hereby agree to the terms of the License Agreement.  

2.3 You may not use GMS+GSI and may not accept the License Agreement if you are a person barred from receiving GMS+GSI under the laws of the United States or other countries, including the country in which you are resident or from which you use GMS+GSI.  

2.4 If you are agreeing to be bound by the License Agreement on behalf of your employer or other entity, you represent and warrant that you have full legal authority to bind your employer or such entity to the License Agreement. If you do not have the requisite authority, you may not accept the License Agreement or use GMS+GSI on behalf of your employer or other entity.  

### 3. GMS+GSI License from Google

3.1 Subject to the terms of the License Agreement, Google grants you a limited, worldwide, royalty-free, non-assignable, non-exclusive, and non-sublicensable license to use GMS+GSI solely for testing applications for compatibility with Android 11.  

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

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 11 GSI Release </button> [Download Android 11 GSI Release](https://dl.google.com/developers/android/rvc/images/gsi/aosp_x86_64-exp-RP1A.200720.009-6720564-a541e9e4.zip)

*aosp_x86_64-exp-RP1A.200720.009-6720564-a541e9e4.zip*

### Known issues with Android 11 GSIs

Android 11 GSI binaries have the following GSI-specific known
issues that might occur with some devices and builds:

- **Phone Audio**: When using the integrated dialer, you might not hear any
  audio on the phone. This is due to a change in the telephony service
  installation location in Android 10.

- **Power Cycle**: Rebooting GSI might fail on some devices. To work around
  it, reboot the device into recovery mode, erase user data, perform a factory
  reset, and then reboot the device.

- **System partition size** : GSI + GMS file size (images named
  `_gsi\_gms\_arm64-*_`) might be bigger than the default dynamic system
  partition size on your device. To work around this issue, you can delete
  some non-essential dynamic partitions, such as the product partition, and
  flash the GSI again. For more information, see the [flashing GSIs
  documentation](https://source.android.com/setup/build/gsi#flashing-gsis).

## Android 10 GSIs

GSI binaries for Android 10 are built from the same AOSP and GMS sources as the
[corresponding Google Pixel builds](https://developer.android.com/about/versions/10/get#on_pixel). These
binaries contain the same API and SDK, have a similar CTS result, and have been
validated on the following Pixel devices:

- Pixel and Pixel XL
- Pixel 2 and 2 XL
- Pixel 3 and 3 XL
- Pixel 3a and 3a XL

    Date: October 2019
    Security patch level: December 2019
    Google Play Services: 19.6.29

| Type | Download Link and SHA-256 Checksum |
|---|---|
| ARM64+GMS | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="arm64-gms" data-modal-dialog-id="gms_QTDP_GSI_zip">gsi_gms_arm64-exp-QJR1.191112.001-6004257.zip</button> `fb0b811bf3b2fbf9d9982de4adbab1eff678dc88c23aa731cd7321720299e4a6` |
| ARM64 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="arm64" data-modal-dialog-id="aosp_arm64_QTDP_GSI_zip">aosp_arm64-exp-QJR1.191112.001-6004257.zip</button> `0bbbf53e1164b032eace999cbd6bf0877ab636819a2e929f63079ccfe71095c7` |
| x86+GMS | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="x86-gms" data-modal-dialog-id="gms_x86_QTDP_GSI_zip">gsi_gms_x86-exp-QJR1.191112.001-6004257.zip</button> `b2efc662abc28c2dd99122e17bd6114e684fca2f0e1911fb526854eb3b620757` |
| x86_64 | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="gsi-release" data-action="download" data-label="x86_64" data-modal-dialog-id="aosp_x86_64_QTDP_GSI_zip">aosp_x86_64-exp-QJR1.191112.001-6004257.zip</button> `1c414cfe975d83d1662d1d9ee7bd8e3d26764e6af1178406e73e6fcb9ade5bee` |

## Download Android 10 GSI Release

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

This is the Early Access Google Mobile Services and Android 10 GSI License Agreement ("License Agreement"). Google Mobile Services and Android 10 GSI (each defined below) are licensed to you subject to the terms of the License Agreement. The License Agreement forms a legally binding contract between you and Google in relation to your use of Google Mobile Services and Android 10 GSI.  

### 1. Definitions

1.1 "Android" means the Android software stack for devices, as made available under the Android Open Source Project, which is located at the following URL: https://source.android.com/, as updated from time to time.  

1.2 "Android 10 GSI" means Google's generic system image of Android 10 code, excluding third party extensions.  

1.3 "Google" means Google LLC, a Delaware corporation with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, United States.  

1.4 "Google Mobile Services" means a machine-readable binary code version of the following Google applications: Search, Chrome, Gmail, Maps, YouTube, and Play, and certain other associated applications, in each case, as provided under this License Agreement. Google Mobile Services are collectively referred to in the License Agreement as "GMS" or each individually as a "GMS Application".  

1.5 "GMS+GSI" refers to GMS and Android 10 GSI, collectively.  

### 2. Accepting this License Agreement

2.1 In order to use GMS+GSI, you must first agree to the License Agreement. You may not use GMS+GSI if you do not accept the License Agreement.  

2.2 By clicking to accept, you hereby agree to the terms of the License Agreement.  

2.3 You may not use GMS+GSI and may not accept the License Agreement if you are a person barred from receiving GMS+GSI under the laws of the United States or other countries, including the country in which you are resident or from which you use GMS+GSI.  

2.4 If you are agreeing to be bound by the License Agreement on behalf of your employer or other entity, you represent and warrant that you have full legal authority to bind your employer or such entity to the License Agreement. If you do not have the requisite authority, you may not accept the License Agreement or use GMS+GSI on behalf of your employer or other entity.  

### 3. GMS+GSI License from Google

3.1 Subject to the terms of the License Agreement, Google grants you a limited, worldwide, royalty-free, non-assignable, non-exclusive, and non-sublicensable license to use GMS+GSI solely for testing applications for compatibility with Android 10.  

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

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 10 GSI Release </button> [Download Android 10 GSI Release](https://dl.google.com/developers/android/qt/images/gsi/gsi_gms_x86-exp-QJR1.191112.001-6004257.zip)

*gsi_gms_x86-exp-QJR1.191112.001-6004257.zip*

## Download Android 10 GSI Release

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

This is the Early Access Google Mobile Services and Android 10 GSI License Agreement ("License Agreement"). Google Mobile Services and Android 10 GSI (each defined below) are licensed to you subject to the terms of the License Agreement. The License Agreement forms a legally binding contract between you and Google in relation to your use of Google Mobile Services and Android 10 GSI.  

### 1. Definitions

1.1 "Android" means the Android software stack for devices, as made available under the Android Open Source Project, which is located at the following URL: https://source.android.com/, as updated from time to time.  

1.2 "Android 10 GSI" means Google's generic system image of Android 10 code, excluding third party extensions.  

1.3 "Google" means Google LLC, a Delaware corporation with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, United States.  

1.4 "Google Mobile Services" means a machine-readable binary code version of the following Google applications: Search, Chrome, Gmail, Maps, YouTube, and Play, and certain other associated applications, in each case, as provided under this License Agreement. Google Mobile Services are collectively referred to in the License Agreement as "GMS" or each individually as a "GMS Application".  

1.5 "GMS+GSI" refers to GMS and Android 10 GSI, collectively.  

### 2. Accepting this License Agreement

2.1 In order to use GMS+GSI, you must first agree to the License Agreement. You may not use GMS+GSI if you do not accept the License Agreement.  

2.2 By clicking to accept, you hereby agree to the terms of the License Agreement.  

2.3 You may not use GMS+GSI and may not accept the License Agreement if you are a person barred from receiving GMS+GSI under the laws of the United States or other countries, including the country in which you are resident or from which you use GMS+GSI.  

2.4 If you are agreeing to be bound by the License Agreement on behalf of your employer or other entity, you represent and warrant that you have full legal authority to bind your employer or such entity to the License Agreement. If you do not have the requisite authority, you may not accept the License Agreement or use GMS+GSI on behalf of your employer or other entity.  

### 3. GMS+GSI License from Google

3.1 Subject to the terms of the License Agreement, Google grants you a limited, worldwide, royalty-free, non-assignable, non-exclusive, and non-sublicensable license to use GMS+GSI solely for testing applications for compatibility with Android 10.  

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

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 10 GSI Release </button> [Download Android 10 GSI Release](https://dl.google.com/developers/android/qt/images/gsi/gsi_gms_arm64-exp-QJR1.191112.001-6004257.zip)

*gsi_gms_arm64-exp-QJR1.191112.001-6004257.zip*

## Download Android 10 GSI Release

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

This is the Early Access Google Mobile Services and Android 10 GSI License Agreement ("License Agreement"). Google Mobile Services and Android 10 GSI (each defined below) are licensed to you subject to the terms of the License Agreement. The License Agreement forms a legally binding contract between you and Google in relation to your use of Google Mobile Services and Android 10 GSI.  

### 1. Definitions

1.1 "Android" means the Android software stack for devices, as made available under the Android Open Source Project, which is located at the following URL: https://source.android.com/, as updated from time to time.  

1.2 "Android 10 GSI" means Google's generic system image of Android 10 code, excluding third party extensions.  

1.3 "Google" means Google LLC, a Delaware corporation with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, United States.  

1.4 "Google Mobile Services" means a machine-readable binary code version of the following Google applications: Search, Chrome, Gmail, Maps, YouTube, and Play, and certain other associated applications, in each case, as provided under this License Agreement. Google Mobile Services are collectively referred to in the License Agreement as "GMS" or each individually as a "GMS Application".  

1.5 "GMS+GSI" refers to GMS and Android 10 GSI, collectively.  

### 2. Accepting this License Agreement

2.1 In order to use GMS+GSI, you must first agree to the License Agreement. You may not use GMS+GSI if you do not accept the License Agreement.  

2.2 By clicking to accept, you hereby agree to the terms of the License Agreement.  

2.3 You may not use GMS+GSI and may not accept the License Agreement if you are a person barred from receiving GMS+GSI under the laws of the United States or other countries, including the country in which you are resident or from which you use GMS+GSI.  

2.4 If you are agreeing to be bound by the License Agreement on behalf of your employer or other entity, you represent and warrant that you have full legal authority to bind your employer or such entity to the License Agreement. If you do not have the requisite authority, you may not accept the License Agreement or use GMS+GSI on behalf of your employer or other entity.  

### 3. GMS+GSI License from Google

3.1 Subject to the terms of the License Agreement, Google grants you a limited, worldwide, royalty-free, non-assignable, non-exclusive, and non-sublicensable license to use GMS+GSI solely for testing applications for compatibility with Android 10.  

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

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 10 GSI Release </button> [Download Android 10 GSI Release](https://dl.google.com/developers/android/qt/images/gsi/aosp_arm64-exp-QJR1.191112.001-6004257.zip)

*aosp_arm64-exp-QJR1.191112.001-6004257.zip*

## Download Android 10 GSI Release

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

This is the Early Access Google Mobile Services and Android 10 GSI License Agreement ("License Agreement"). Google Mobile Services and Android 10 GSI (each defined below) are licensed to you subject to the terms of the License Agreement. The License Agreement forms a legally binding contract between you and Google in relation to your use of Google Mobile Services and Android 10 GSI.  

### 1. Definitions

1.1 "Android" means the Android software stack for devices, as made available under the Android Open Source Project, which is located at the following URL: https://source.android.com/, as updated from time to time.  

1.2 "Android 10 GSI" means Google's generic system image of Android 10 code, excluding third party extensions.  

1.3 "Google" means Google LLC, a Delaware corporation with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, United States.  

1.4 "Google Mobile Services" means a machine-readable binary code version of the following Google applications: Search, Chrome, Gmail, Maps, YouTube, and Play, and certain other associated applications, in each case, as provided under this License Agreement. Google Mobile Services are collectively referred to in the License Agreement as "GMS" or each individually as a "GMS Application".  

1.5 "GMS+GSI" refers to GMS and Android 10 GSI, collectively.  

### 2. Accepting this License Agreement

2.1 In order to use GMS+GSI, you must first agree to the License Agreement. You may not use GMS+GSI if you do not accept the License Agreement.  

2.2 By clicking to accept, you hereby agree to the terms of the License Agreement.  

2.3 You may not use GMS+GSI and may not accept the License Agreement if you are a person barred from receiving GMS+GSI under the laws of the United States or other countries, including the country in which you are resident or from which you use GMS+GSI.  

2.4 If you are agreeing to be bound by the License Agreement on behalf of your employer or other entity, you represent and warrant that you have full legal authority to bind your employer or such entity to the License Agreement. If you do not have the requisite authority, you may not accept the License Agreement or use GMS+GSI on behalf of your employer or other entity.  

### 3. GMS+GSI License from Google

3.1 Subject to the terms of the License Agreement, Google grants you a limited, worldwide, royalty-free, non-assignable, non-exclusive, and non-sublicensable license to use GMS+GSI solely for testing applications for compatibility with Android 10.  

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

I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android 10 GSI Release </button> [Download Android 10 GSI Release](https://dl.google.com/developers/android/qt/images/gsi/aosp_x86_64-exp-QJR1.191112.001-6004257.zip)

*aosp_x86_64-exp-QJR1.191112.001-6004257.zip*

### Known issues with Android 10 GSIs

This version of the Android 10 GSI has the following known issues that might
occur with some devices and builds:

- **Phone Audio**: When using the integrated dialer, you might not hear any
  audio on the phone. This is due to a change in the telephony service
  installation location in Android 10.

- **Power Cycle**: Rebooting GSI might fail on some devices. To work around
  it, reboot the device into recovery mode, erase user data, perform a factory
  reset, and then reboot the device.

- **System partition size** : GSI + GMS file size (images named
  `_gsi\_gms\_arm64-*_`) might be bigger than the default dynamic system
  partition size on your device. To work around this issue, you can delete
  some non-essential dynamic partitions, such as the product partition, and
  flash the GSI again. For more information, see the [flashing GSIs
  documentation](https://source.android.com/setup/build/gsi#flashing-gsis).