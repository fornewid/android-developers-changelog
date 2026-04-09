---
title: https://developer.android.com/privacy-and-security/risks/android-exported
url: https://developer.android.com/privacy-and-security/risks/android-exported
source: md.txt
---

# android:exported

<br />

**OWASP category:** [MASVS-PLATFORM: Platform Interaction](https://mas.owasp.org/MASVS/09-MASVS-PLATFORM)

## Overview

The`android:exported`[attribute](https://developer.android.com/guide/topics/manifest/activity-element#exported)sets whether a component (activity, service, broadcast receiver, etc.) can be launched by components of other applications:

- If`true`, any app can access the activity and launch it by its exact class name.
- If`false`, only components of the same application, applications with the same user ID, or privileged system components can launch the activity.

The logic behind the default value of this attribute changed over time and was different depending on the component types and Android versions. For example, on API level 16 (Android 4.1.1) or lower the value for`<provider>`elements is set to`true`by default. Not setting this attribute explicitly carries the risk of having different default values between some devices.

## Impact

The situation with different default values means you could accidentally expose internal application components. A few examples of the consequences could be the following:

Denial of service attacks. Other apps inappropriately accessing internal components to modify your app's internal functionality. Leaking of sensitive data. Code execution in the context of the vulnerable application.

## Mitigations

Always explicitly set the`android:exported`attribute. This will leave no room for interpretation and clearly signal your intention with regard to a component's visibility.

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [# Key management {:#key-management}](https://developer.android.com/topic/security/data)
- [Run embedded DEX code directly from APK](https://developer.android.com/topic/security/dex)
- [Tapjacking](https://developer.android.com/topic/security/risks/tapjacking)