---
title: Behavior changes: Apps targeting Android 17 or higher  |  Android Developers
url: https://developer.android.com/about/versions/17/behavior-changes-17
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Releases](https://developer.android.com/about/versions)

# Behavior changes: Apps targeting Android 17 or higher Stay organized with collections Save and categorize content based on your preferences.




Like previous releases, Android 17 includes behavior changes that might affect
your app. The following behavior changes apply exclusively to apps that are
targeting Android 17 or higher. If your app is targeting Android 17 or higher,
you should modify your app to support these behaviors, where applicable.

Be sure to also review the list of [behavior changes that affect all apps
running on Android 17](/about/versions/17/behavior-changes-all) regardless of your app's [`targetSdkVersion`](/guide/topics/manifest/uses-sdk-element#target).

**Note:** This page lists some of the more important changes. For more detailed
information, see the [Android 17 release notes](/about/versions/17/release-notes).

## Core functionality

Android 17 includes the following changes that modify or
expand various core capabilities of the Android system.

### New lock-free implementation of MessageQueue

Beginning with Android 17, apps targeting Android 17
or higher receive a new lock-free implementation of
[`android.os.MessageQueue`](/reference/android/os/MessageQueue). The new implementation improves performance and
reduces missed frames, but may break clients that reflect on `MessageQueue`
private fields and methods.

For more information, including mitigation strategies, see [MessageQueue
behavior change guidance](/about/versions/17/changes/messagequeue).

## Accessibility

Android 17 makes the following changes to improve accessibility.

### Accessibility support of complex IME physical keyboard typing

This feature introduces new [`AccessibilityEvent`](/reference/android/view/accessibility/AccessibilityEvent) and [`TextAttribute`](/reference/android/view/inputmethod/TextAttribute)
APIs to enhance screen reader spoken feedback for CJKV language input. CJKV IME
apps can now signal whether a text conversion candidate has been selected during
text composition. Apps with edit fields can specify *text change types* when
sending text changed accessibility events.
For example, apps can specify that a text change occurred during text
composition, or that a text change resulted from a commit.
Doing this enables accessibility
services such as screen readers to deliver more precise feedback based on the
nature of the text modification.

#### App adoption

* **IME Apps:** When setting composing text in edit fields, IMEs can use
  `TextAttribute.Builder.setTextSuggestionSelected()` to indicate whether a
  specific conversion candidate was selected.
* **Apps with Edit Fields:** Apps that maintain a custom `InputConnection` can
  retrieve candidate selection data by calling
  `TextAttribute.isTextSuggestionSelected()`. These apps should then call
  `AccessibilityEvent.setTextChangeTypes()` when dispatching
  `TYPE_VIEW_TEXT_CHANGED` events. Apps targeting
  Android 17 that use the standard `TextView` will have
  this feature enabled by default. (That is, `TextView` will handle retrieving
  data from the IME and setting text change types when sending events to
  accessibility services).
* **Accessibility Services:** Accessibility services that process
  `TYPE_VIEW_TEXT_CHANGED` events can call
  `AccessibilityEvent.getTextChangeTypes()` to identify the nature of the
  modification and adjust their feedback strategies accordingly.

## Security

Android 17 makes the following improvements to device and app security.

### Activity Security

In Android 17, the platform continues its shift toward a
"secure-by-default" architecture, introducing a suite of enhancements designed
to mitigate high-severity exploits such as phishing, interaction hijacking, and
confused deputy attacks. This update requires developers to explicitly opt in to
new security standards to maintain app compatibility and user protection.

Key impacts for developers include:

* **BAL hardening & improved opt-in:** We are refining Background Activity
  Launch (BAL) restrictions by extending protections to [`IntentSender`](/reference/android/content/IntentSender).
  Developers must migrate away from the legacy
  [`MODE_BACKGROUND_ACTIVITY_START_ALLOWED`](/reference/android/app/ActivityOptions#MODE_BACKGROUND_ACTIVITY_START_ALLOWED) constant. Instead, you should
  adopt granular controls like
  [`MODE_BACKGROUND_ACTIVITY_START_ALLOW_IF_VISIBLE`](/reference/android/app/ActivityOptions#MODE_BACKGROUND_ACTIVITY_START_ALLOW_IF_VISIBLE), which restricts
  activity starts to scenarios where the calling app is visible, significantly
  reducing the attack surface.
* **Adoption tools:** Developers should utilize strict mode and updated lint
  checks to identify legacy patterns and ensure readiness for future target
  SDK requirements.

### Localhost protections

To improve platform security and user privacy, Android 17
introduces a new install-time permission, `USE_LOOPBACK_INTERFACE`. This change
restricts cross-app and cross-profile communication over the loopback interface
(for example, `127.0.0.1` or `::1`), which was previously implicitly allowed
with the `INTERNET` permission. For apps targeting
Android 17 or higher, the following rules apply:

* **Mutual consent required:** cross-app and cross-profile communication is
  now blocked by default. For a connection to succeed, both the sending app
  and the receiving app must explicitly declare the `USE_LOOPBACK_INTERFACE`
  permission in their manifests.
* **Intra-app traffic exempt:** Loopback communication within the same app
  (*intra-app* communication) remains unaffected and does not require this new
  permission.
* **Target SDK behavior:**
  + App targets Android 17 or higher: The permission
    must be explicitly requested. If it is missing, socket operations (such
    as TCP connect or UDP send) fail, typically returning an `EPERM`
    (operation not permitted) error.
  + App targets API level 36 or lower: The permission is
    treated as a split permission on `INTERNET`. Apps targeting lower API
    levels are auto-granted this permission if they hold `INTERNET`.
* **Compatibility warning:** If a receiving app updates its target to
  Android 17 but fails to request this permission,
  incoming connections from other apps are be rejected, even if the sending
  app targets a lower API level.

### Enable CT by default

If an app targets Android 17 or higher,
[certificate transparency (CT)](/privacy-and-security/security-config#CertificateTransparencySummary) is enabled by default. (On Android 16, CT is
available but apps had to [opt in](/privacy-and-security/security-config#certificateTransparency).)

### Safer Native DCL—C

If your app targets Android 17 or higher, the Safer Dynamic
Code Loading (DCL) protection introduced in Android 14 for DEX and JAR files now
extends to native libraries.

All native files loaded using `System.load()` must be marked as read-only.
Otherwise, the system throws `UnsatisfiedLinkError`.

We recommend that apps avoid dynamically loading code whenever possible, as
doing so greatly increases the risk that an app can be compromised by code
injection or code tampering.

## Device form factors

Android 17 includes the following changes to improve user
experience across a range of device sizes and form factors.

### Platform API changes to ignore orientation, resizability and aspect ratio constraints on large screens (sw>=600dp)

We introduced Platform API changes in Android 16 to [ignore orientation,
aspect ratio, and resizability restrictions on large screens (sw >=
600dp)](/about/versions/16/behavior-changes-16#ignore-orientation) for apps targeting API level
36 or higher. Developers have the option to opt out of these
changes with SDK 36, but this opt-out will no longer be
available for apps that target Android 17 or higher.

For more information, see [Restrictions on orientation and resizability are
ignored](/about/versions/17/changes/ff-restrictions-ignored).