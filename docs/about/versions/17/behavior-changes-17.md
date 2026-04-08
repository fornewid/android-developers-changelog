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

Beginning with Android 17, apps targeting Android 17 (API level 37)
or higher receive a new lock-free implementation of
[`android.os.MessageQueue`](/reference/android/os/MessageQueue). The new implementation improves performance and
reduces missed frames, but may break clients that reflect on `MessageQueue`
private fields and methods.

For more information, including mitigation strategies, see [MessageQueue
behavior change guidance](/about/versions/17/changes/messagequeue).

### Static final fields are now unmodifiable

Apps running on Android 17 or higher that target
Android 17 (API level 37) or higher cannot change `static final` fields. If
an app attempts to change a `static final` field by using reflection, it will
cause an `IllegalAccessException`. Attempting to modify one of these fields
through JNI APIs (such as `SetStaticLongField()`) will cause the app to crash.

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
  Android 17 (API level 37) that use the standard `TextView` will have
  this feature enabled by default. (That is, `TextView` will handle retrieving
  data from the IME and setting text change types when sending events to
  accessibility services).
* **Accessibility Services:** Accessibility services that process
  `TYPE_VIEW_TEXT_CHANGED` events can call
  `AccessibilityEvent.getTextChangeTypes()` to identify the nature of the
  modification and adjust their feedback strategies accordingly.

## Privacy

Android 17 includes the following changes to improve user privacy.

### ECH (Encrypted Client Hello) opportunistically enabled

Android 17 introduces platform support for Encrypted Client Hello (ECH), a TLS
extension that enhances user privacy by encrypting the Server Name Indication
(SNI) in the TLS handshake. This encryption helps prevent network observers from
easily identifying the specific domain your app is connecting to.

For apps targeting Android 17 (API level 37) or higher, ECH is
opportunistically used for TLS connections. ECH is active only if the networking
library used by the app (for example, HttpEngine, WebView, or OkHttp) has
integrated ECH support and the remote server also supports the ECH protocol. If
ECH cannot be negotiated, the connection automatically falls back to a standard
TLS handshake without SNI encryption.

To allow apps to customize this behavior, Android 17 adds a new
[`<domainEncryption>`](/privacy-and-security/security-config#domainEncryption) element to the Network Security Configuration file.
Developers can use `<domainEncryption>` within `<base-config>` or
`<domain-config>` tags to select an ECH mode (for example,
`"opportunistic"`, `"enabled"`, or `"disabled"`) on a global or per-domain
basis.

For more information, see the [Encrypted Client Hello](/privacy-and-security/security-config#EncryptedClientHelloSummary) documentation.

### Local network permission required for apps targeting Android 17

Android 17 introduces the [`ACCESS_LOCAL_NETWORK`](/reference/android/Manifest.permission#ACCESS_LOCAL_NETWORK) runtime permission
to protect users from unauthorized local network access. Because this falls
under the existing `NEARBY_DEVICES` permission group, users who have already
granted other `NEARBY_DEVICES` permissions aren't prompted again. This new
requirement prevents malicious apps from exploiting unrestricted local network
access for covert user tracking and fingerprinting. By declaring and requesting
this permission, your app can discover and connect to devices on the local area
network (LAN), such as smart home devices or casting receivers.

Apps targeting Android 17 (API level 37) or higher now have two paths to
maintain communication with LAN devices: Adopt system-mediated,
privacy-preserving device pickers to skip the permission prompt, or explicitly
request this new permission at runtime to maintain local network communication.

For more information, see the [Local network permission](/privacy-and-security/local-network-permission) documentation.

**Note:** In Android 16, apps could opt in to local network permissions.
Beginning with Android 17, enforcement is mandatory for apps that target
Android 17 (API level 37) or higher.

### Hiding passwords from physical devices

If an app targets Android 17 (API level 37) or higher and the user is using
a physical input device (for example, an external keyboard), the Android
operating system applies the new `show_passwords_physical` setting to all
characters in the password field. By default, that setting hides all password
characters.

The Android system shows the last-typed password character to help the user see
if they mistyped the password. However, this is much less necessary with larger
external keyboards. In addition, devices with external keyboards often have
larger displays, which increases the danger of someone seeing the typed
password.

If the user is using the device's touchscreen, the system applies the new
`show_passwords_touch` setting.

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

### Enable CT by default

If an app targets Android 17 (API level 37) or higher,
[certificate transparency (CT)](/privacy-and-security/security-config#CertificateTransparencySummary) is enabled by default. (On Android 16, CT is
available but apps had to [opt in](/privacy-and-security/security-config#certificateTransparency).)

### Safer Native DCL—C

If your app targets Android 17 (API level 37) or higher, the Safer Dynamic
Code Loading (DCL) protection introduced in Android 14 for DEX and JAR files now
extends to native libraries.

All native files loaded using `System.load()` must be marked as read-only.
Otherwise, the system throws `UnsatisfiedLinkError`.

We recommend that apps avoid dynamically loading code whenever possible, as
doing so greatly increases the risk that an app can be compromised by code
injection or code tampering.

### Restrict PII fields in CP2 data view

For apps targeting Android 17 (API level Android 17 (API level 37)) and
higher, Contacts Provider 2 (CP2) restricts certain columns containing
Personally Identifiable Information (PII) from the data view. When this change
is enabled, these columns are removed from the data view to enhance user
privacy.
The restricted columns include:

* [`ACCOUNT_NAME`](/reference/android/provider/ContactsContract.SyncColumns#ACCOUNT_NAME)
* [`ACCOUNT_TYPE`](/reference/android/provider/ContactsContract.SyncColumns#ACCOUNT_TYPE)
* [`ACCOUNT_TYPE_AND_DATA_SET`](/reference/android/provider/ContactsContract.RawContactsColumns#ACCOUNT_TYPE_AND_DATA_SET)

Apps that are using these columns from [`ContactsContract.Data`](/reference/android/provider/ContactsContract.Data)
can extract them from [`ContactsContract.RawContacts`](/reference/android/provider/ContactsContract.RawContacts)
instead, by joining with [`RAW_CONTACT_ID`](/reference/android/provider/ContactsContract.DataColumns#RAW_CONTACT_ID).

### Enforce strict SQL checks in CP2

For apps targeting Android 17 (API level Android 17 (API level 37)) and
higher, Contacts Provider 2 (CP2) enforces strict SQL query validation when
the [`ContactsContract.Data`](/reference/android/provider/ContactsContract.Data) table is accessed without
[`READ_CONTACTS`](/reference/android/Manifest.permission#READ_CONTACTS) permission.

With this change, if an app doesn't have [`READ_CONTACTS`](/reference/android/Manifest.permission#READ_CONTACTS)
permission, [`StrictColumns`](/reference/android/database/sqlite/SQLiteQueryBuilder#setStrictColumns(boolean)) and
[`StrictGrammar`](/reference/android/database/sqlite/SQLiteQueryBuilder#setStrictGrammar(boolean)) options are set when querying
the [`ContactsContract.Data`](/reference/android/provider/ContactsContract.Data) table. If a query
uses a pattern that isn't compatible with these, it will be
rejected and cause an exception to be thrown.

## Device form factors

Android 17 includes the following changes to improve user
experience across a range of device sizes and form factors.

### Platform API changes to ignore orientation, resizability and aspect ratio constraints on large screens (sw>=600dp)

We introduced Platform API changes in Android 16 to [ignore orientation,
aspect ratio, and resizability restrictions on large screens (sw >=
600dp)](/about/versions/16/behavior-changes-16#ignore-orientation) for apps targeting API level
36 or higher. Developers have the option to opt out of these
changes with SDK 36, but this opt-out will no longer be
available for apps that target Android 17 (API level 37) or higher.

For more information, see [Restrictions on orientation and resizability are
ignored](/about/versions/17/changes/ff-restrictions-ignored).