---
title: https://developer.android.com/distribute/play-policies
url: https://developer.android.com/distribute/play-policies
source: md.txt
---

![](http://developer.android.com/static/images/hero-illustrations/play-policies-hero.svg)

### Upcoming Android and Google Play deadlines

Our platform and policies constantly evolve to improve the user experience and create a safer ecosystem. This page is updated with the latest information about these policies, including any changes you may be required to make. Thanks for keeping your apps and games up to date. [Google Play Developer Policy Center](https://play.google.com/about/developer-content-policy/)

*** ** * ** ***

[![](http://developer.android.com/static/distribute/images/play-protection.svg)](https://security.googleblog.com/2026/02/keeping-google-play-android-app-ecosystem-safe-2025.html)

### [Keeping Google Play safe in 2025](https://security.googleblog.com/2026/02/keeping-google-play-android-app-ecosystem-safe-2025.html)

Safety is at the heart of everything we do. Learn how we're investing in world-class defenses, proactively stopping threats and providing stronger protections for your business. [Read more](https://security.googleblog.com/2026/02/keeping-google-play-android-app-ecosystem-safe-2025.html) [![](http://developer.android.com/static/images/picto-icons/security-2.svg)](https://android-developers.googleblog.com/2025/12/building-safer-android-and-google-play.html)

### [Building a safer Android and Google Play, together](https://android-developers.googleblog.com/2025/12/building-safer-android-and-google-play.html)

Learn about our ongoing work to maintain a thriving ecosystem where your business can flourish. From simpler ways for building secure apps to stronger, proactive protections for your business and users, see how we're investing in a safer future for everyone. [Read more](https://android-developers.googleblog.com/2025/12/building-safer-android-and-google-play.html)

## Timeline

| Date | Policy Update |
|---|---|
| August 26, 2026 | We're expanding our [Families Policy Requirements](https://support.google.com/googleplay/android-developer/answer/17122218#families-policy) policy to prohibit developers of anonymous chat apps from targeting children. |
| August 26, 2026 | We're expanding our [Age-Restricted Content and Functionality](https://support.google.com/googleplay/android-developer/answer/17036597) policy to apply to anonymous chat and random chat apps. |
| August 26, 2026 | We're expanding our [Child Safety Standards](https://support.google.com/googleplay/android-developer/answer/17122524#child_safety) policy to apply to anonymous chat and random chat apps. |
| September 30, 2026 | [Android developer verification](https://developer.android.com/developer-verification) goes into effect. Apps from participating stores in Brazil, Indonesia, Singapore, and Thailand must be registered by a verified developer to be installed on certified Android devices. <br /> We're also updating [Play Console requirements](https://support.google.com/googleplay/android-developer/answer/10788890) to meet Android developer verification requirements. While 99% of apps on Play have been registered automatically, you should check your [Play Console Home page](https://play.google.com/console/u/0/developers/5700313618786177705/android-developer-verification) to register any remaining apps to avoid global removal from Google Play and ensure a seamless user installation experience. |
| January 27, 2027 | We're removing geofencing as an approved [foreground services use case](https://support.google.com/googleplay/android-developer/answer/13392821). Developers can instead use the [Geofence API](https://developer.android.com/develop/sensors-and-location/location/geofencing#RequestGeofences) for this use case. |
| January 27, 2027 | We're introducing the [Contacts Permission](https://support.google.com/googleplay/android-developer/answer/16909972#contacts-permissions) policy to govern broad access of users' contacts. Apps that don't need broad access must use the [Android Contact Picker](https://developer.android.com/about/versions/17/features/contact-picker), a more secure, easy-to-integrate alternative that minimizes data collection and improves user safety. |
| January 27, 2027 | We're updating the [Location Permissions](https://support.google.com/googleplay/android-developer/answer/16909972#location-permissions) policy. To meet our minimum scope requirements, apps targeting Android 17 (API 37+) must now implement the Android location button for one-time or infrequent precise location requests. If your app's core functionality requires broader **ACCESS_FINE_LOCATION** access, you must submit a Play Console declaration justifying why the location button or coarse location is insufficient. |
| January 27, 2027 | Our [SMS and Call Log Permissions](https://support.google.com/googleplay/android-developer/answer/10208820?sjid=17577182363882827718-NC&visit_id=639160341729576617-3917463334&rd=1#zippy=%2Calternatives-to-common-uses) policy will no longer permit account verification via phone call as a use case for the READ_CALL_LOG permission. To securely verify accounts without requiring sensitive app permissions, use the [Digital Credentials API](https://developer.android.com/identity/digital-credentials/phone-number-verification) instead, either directly or through a verification provider built upon it, or the [SMS Retriever API](https://developer.android.com/identity/sms-retriever). Please refer to [this page](https://developer.android.com/privacy-and-security/minimize-permission-requests#verify-phone-number) for additional alternative APIs. |
| January 27, 2027 | [Subscriptions with ongoing eligibility-based discounts](https://support.google.com/googleplay/android-developer/answer/18204939), such as student plans, must clearly disclose eligibility criteria, the verification process, and post-eligibility pricing and benefit changes. |
| April 14, 2027 | [AppFunctions API](https://support.google.com/googleplay/android-developer/answer/16909972#appfunctions): Developers building AppFunctions must comply with all existing Google Play policies. AppFunctions are strictly prohibited from deceiving or manipulating AI agents, bypassing security controls, or interfering with other applications. |
| August 25, 2027 | [Local Network Permission](https://support.google.com/googleplay/android-developer/answer/16909972#local_network): This permission is restricted to apps that need it for core functionality when device pickers are insufficient. Apps targeting Android 17 or higher (API 37+) must submit a Play Console declaration to use this permission. |
| August 25, 2027 | [Manage Contacts Permission](https://support.google.com/googleplay/android-developer/answer/16909972#manage_contacts): This permission is restricted to apps that need it for core functionality when system pickers are insufficient and apps must submit a Play Console declaration to use it. All other apps must use narrowly scoped platform intents. |

## Featured changes

[![](http://developer.android.com/static/images/cluster-illustrations/policy.svg)](https://support.google.com/googleplay/android-developer/answer/18100766)

### [Comply with October 2026 policy updates](https://support.google.com/googleplay/android-developer/answer/18100766)

We regularly update our policies as part of our commitment to making Google Play the safest and most trusted experience possible. [Policy Center](https://support.google.com/googleplay/android-developer/answer/18100766) [Policybytes Video](https://goo.gle/policybytes426)

## Past deadlines

[![](http://developer.android.com/static/images/cluster-illustrations/policy.svg)](https://support.google.com/googleplay/android-developer/answer/17134731)

### [Comply with July 2026 policy updates](https://support.google.com/googleplay/android-developer/answer/17134731)

We regularly update our policies as part of our commitment to making Google Play the safest and most trusted experience possible. [Policy Center](https://support.google.com/googleplay/android-developer/answer/17134731) [Policybytes Video](https://goo.gle/policybytes326)