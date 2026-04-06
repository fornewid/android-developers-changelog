---
title: https://developer.android.com/privacy-and-security/risks/tapjacking
url: https://developer.android.com/privacy-and-security/risks/tapjacking
source: md.txt
---

# Tapjacking

<br />

**OWASP category:** [MASVS-PLATFORM: Platform Interaction](https://mas.owasp.org/MASVS/09-MASVS-PLATFORM)

## Overview

Tapjacking is the Android-app equivalent of the[clickjacking web vulnerability](https://owasp.org/www-community/attacks/Clickjacking): A malicious app tricks the user into clicking a security-relevant control (confirmation button etc.) by obscuring the UI with an overlay or by other means. On this page, we differentiate two attack variants: Full and partial occlusion. In full occlusion, the attacker overlays the touch area, while in partial occlusion, the touch area remains unobscured.

## Impact

Tapjacking attacks are used to trick users into performing certain actions. The impact depends on the action targeted by the attacker.

## Risk: Full occlusion

In full occlusion, the attacker overlays the touch area to hijack the touch event:

![Full occlusion image](https://developer.android.com/static/privacy-and-security/risks/images/tapjacking/full_occlusion.png "Full occlusion")

### Mitigations

Full occlusion is prevented by setting`View.setFilterTouchesWhenObscured(true)`in the code. This blocks touches passed by an overlay. If you prefer a declarative approach, you can also add`android:filterTouchesWhenObscured="true"`in the layout file for the[`View`](https://developer.android.com/reference/android/view/View#security)object that you want to protect.
| **Note:** Android S (12, SDK 31) and higher prevent full occlusion attacks by default, by blocking touch events from non-trusted overlays from another UID.  
|
| However, there is a caveat: for System Alert Window (SAW) and window animations, only touches from layers with opacity \>= 0.8 are blocked. The reasoning behind this behavior is that SAW requires users to grant permission, and blocking all events for time-limited animations might hurt the user experience.

*** ** * ** ***

## Risk: Partial occlusion

In partial occlusion attacks, the touch area remains unobscured:

![Partial occlusion image](https://developer.android.com/static/privacy-and-security/risks/images/tapjacking/partial_occlusion.png "Partial occlusion")

### Mitigations

You can mitigate partial occlusion by manually ignoring touch events that have the`FLAG_WINDOW_IS_PARTIALLY_OBSCURED`flag. There are no default protections against this scenario.
| **Note:** **Potential caveat:**This mitigation can interfere with benign apps. In some cases, rolling out this fix isn't possible, as it would negatively affect the user experience when the partial occlusion is caused by a benign application.

**Android 16 and`accessibilityDataSensitive`:** Starting with Android 16 (API level 16) and higher, developers can use the`accessibilityDataSensitive`flag to further protect sensitive data from malicious accessibility services that are not legitimate accessibility tools. When this flag is set on sensitive views (e.g., login screens, transaction confirmation screens), it restricts apps with accessibility permission from reading or interacting with the sensitive data unless they are declared as an`isA11yTool=true`in their manifest. This provides a more robust, system-level protection against eavesdropping and click injection attacks that are characteristic of partial occlusion scenarios. Developers can often implicitly enable`accessibilityDataSensitive`by specifying`android:filterTouchesWhenObscured="true"`in their layout files.

*** ** * ** ***

## Specific risks

This section gathers risks that require non-standard mitigation strategies or were mitigated at certain SDK level and are here for completeness.

### Risk: android.Manifest.permission.SYSTEM_ALERT_WINDOW

The[`SYSTEM_ALERT_WINDOW`](https://developer.android.com/reference/android/Manifest.permission#SYSTEM_ALERT_WINDOW)permission allows an app to create a window shown on top of all apps.

#### Mitigations

Newer versions of Android have introduced several mitigations, including the following:

- On Android 6 (API level 23) and higher, users have to explicitly grant the permission for the app to create an overlay window.
- On Android 12 (API level 31) and higher, apps can pass`true`into[`Window.setHideOverlayWindows()`](https://developer.android.com/reference/android/view/Window#setHideOverlayWindows(boolean)).

*** ** * ** ***

### Risk: Custom toast

An attacker can use`Toast.setView()`to customize a[toast](https://developer.android.com/guide/topics/ui/notifiers/toasts)message's appearance. On Android 10 (API level 29) and lower, malicious apps could launch such toasts from the background.

#### Mitigations

If an app targets Android 11 (API level 30) or higher, the system blocks background custom toasts. However, this mitigation can be evaded in some circumstances using*Toast burst*, where the attacker queues multiple toasts while in the foreground and they keep getting launched even after an app goes to the background.

Background toasts and toast burst attacks are fully mitigated as of Android 12 (API level 31).

*** ** * ** ***

### Risk: Activity sandwich

If a malicious app manages to convince a user to open it, it can still launch an activity from the victim app and subsequently overlay it with its own activity, forming an*activity sandwich*and creating a partial occlusion attack.

#### Mitigations

See general mitigations for partial occlusion. For defense in-depth, make sure that you don't export activities that don't need to be exported to prevent an attacker from sandwiching them.

*** ** * ** ***

## Resources

- [Play Store target API level policy changes](https://android-developers.googleblog.com/2019/02/expanding-target-api-level-requirements.html)

- [UI redressing and accessibility service-based Android attacks](http://Cloak-and-dagger.org)

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [android:exported](https://developer.android.com/topic/security/risks/android-exported)
- [# Key management {:#key-management}](https://developer.android.com/topic/security/data)
- [Run embedded DEX code directly from APK](https://developer.android.com/topic/security/dex)