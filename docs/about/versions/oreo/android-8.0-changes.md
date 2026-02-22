---
title: https://developer.android.com/about/versions/oreo/android-8.0-changes
url: https://developer.android.com/about/versions/oreo/android-8.0-changes
source: md.txt
---

Along with new features and capabilities, Android 8.0 (API level 26)
includes a variety of system and API behavior changes. This document
highlights some of the key changes that you should understand and account for
in your apps.


Most of these changes affect all apps, regardless of what version of
Android they target. However, several changes only affect apps targeting
Android 8.0. To maximize clarity, this
page is divided into two sections: [Changes for all apps](https://developer.android.com/about/versions/oreo/android-8.0-changes#atap) and [Changes for apps targeting
Android 8.0](https://developer.android.com/about/versions/oreo/android-8.0-changes#o-apps).

## Changes for all apps


These behavior changes apply to all apps when they
run on the Android 8.0 (API level 26) platform, regardless of the
API level that they target. All developers should review
these changes and modify their apps to support them properly,
where applicable to the app.

### Background execution limits


As one of the changes that Android 8.0 (API level 26) introduces to
improve battery life, when your app enters the
[cached](https://developer.android.com/guide/topics/processes/process-lifecycle)
state, with no active
[components](https://developer.android.com/guide/components/fundamentals#Components),
the system releases any wakelocks that the app holds.

In addition, to improve device performance, the system limits certain
behaviors by apps that are not running in the foreground. Specifically:

- Apps that are running in the background now have limits on how freely they can access background services.
- Apps cannot use their manifests to register for most implicit broadcasts (that is, broadcasts that are not targeted specifically at the app).


By default, these restrictions only apply to apps that target O. However,
users can enable these restrictions for any app from the **Settings** screen,
even if the app has not targeted O.


Android 8.0 (API level 26) also includes the following changes to specific methods:

- The `https://developer.android.com/reference/android/content/Context#startService(android.content.Intent)` method now throws an `https://developer.android.com/reference/java/lang/IllegalStateException` if an app targeting Android 8.0 tries to use that method in a situation when it isn't permitted to create background services.
- The new `Context.startForegroundService()` method starts a foreground service. The system allows apps to call `Context.startForegroundService()` even while the app is in the background. However, the app must call that service's `https://developer.android.com/reference/android/app/Service#startForeground(int, android.app.Notification)` method within five seconds after the service is created.


For more information, see
[Background Execution Limits](https://developer.android.com/about/versions/oreo/background).

### Android background location limits

In order to preserve battery, user experience, and system health,
background apps receive location updates less frequently when used on a device
running Android 8.0. This behavior change affects all apps
that receive location updates, including Google Play services.


These changes affect the following APIs:

- Fused Location Provider (FLP)
- Geofencing
- GNSS Measurements
- Location Manager
- Wi-Fi Manager

To ensure that your app runs as expected, complete the following steps:

- Review your app's logic and ensure that you're using the latest location APIs.
- Test that your app exhibits the behavior that you expect for each use case.
- Consider using the [Fused
  Location Provider (FLP)](https://developers.google.com/android/reference/com/google/android/gms/location/FusedLocationProviderApi) or geofencing to handle the use cases that depend on the user's current location.

For more information about these changes, see
[Background Location
Limits](https://developer.android.com/about/versions/oreo/background-location-limits).

### App shortcuts

Android 8.0 (API level 26) includes the following changes to app shortcuts:

- The `com.android.launcher.action.INSTALL_SHORTCUT` broadcast no longer has any effect on your app, because it is now a private, implicit broadcast. Instead, you should create an app shortcut by using the `https://developer.android.com/reference/android/content/pm/ShortcutManager#requestPinShortcut(android.content.pm.ShortcutInfo, android.content.IntentSender)` method from the `https://developer.android.com/reference/android/content/pm/ShortcutManager` class.
- The `https://developer.android.com/reference/android/content/Intent#ACTION_CREATE_SHORTCUT` intent can now create app shortcuts that you manage using the `https://developer.android.com/reference/android/content/pm/ShortcutManager` class. This intent can also create legacy launcher shortcuts that don't interact with `https://developer.android.com/reference/android/content/pm/ShortcutManager`. Previously, this intent could create only legacy launcher shortcuts.
- Shortcuts created using `https://developer.android.com/reference/android/content/pm/ShortcutManager#requestPinShortcut(android.content.pm.ShortcutInfo, android.content.IntentSender)` and shortcuts created in an activity that handles the `https://developer.android.com/reference/android/content/Intent#ACTION_CREATE_SHORTCUT` intent are now fully-fledged app shortcuts. As a result, apps can now update them using the methods in `https://developer.android.com/reference/android/content/pm/ShortcutManager`.
- Legacy shortcuts retain their functionality from previous versions of Android, but you must convert them to app shortcuts manually in your app.

To learn more about changes to app shortcuts, see the
[Pinning Shortcuts and
Widgets](https://developer.android.com/guide/topics/ui/shortcuts#pinning) feature guide.

### Locales and internationalization


Android 7.0 (API level 24) introduced the concept of being able to
specify a default Category Locale, but some APIs continued to use the
generic `https://developer.android.com/reference/java/util/Locale#getDefault()`
method, without arguments, when they should have instead used default `https://developer.android.com/reference/java/util/Locale.Category#DISPLAY` category Locale. In Android 8.0 (API level 26), the
following methods now use `https://developer.android.com/reference/java/util/Locale#getDefault(java.util.Locale.Category)`
instead of `https://developer.android.com/reference/java/util/Locale#getDefault()`:

- `https://developer.android.com/reference/java/util/Currency#getDisplayName()`
- `https://developer.android.com/reference/java/util/Currency#getSymbol()`
- `https://developer.android.com/reference/java/util/Locale#getDisplayScript()`


`https://developer.android.com/reference/java/util/Locale#getDisplayScript()` also
falls back to `https://developer.android.com/reference/java/util/Locale#getDefault()` when the
<var translate="no">displayScript</var> value specified for the `https://developer.android.com/reference/java/util/Locale`
argument is not available.


Additional locale and internationalization-related changes are as
follows:

- Calling `https://developer.android.com/reference/java/util/Currency#getDisplayName()` throws a `https://developer.android.com/reference/java/lang/NullPointerException`, matching the documented behavior.
- Time zone name parsing has changed. Previously, Android devices used the system clock value sampled at boot time to cache the time zone names used for parsing date times. As a result, parsing could be negatively affected if the system clock was wrong at boot time or in other, rarer cases.
  Now, in common cases the parsing logic uses ICU and the
  current system clock value when parsing time zone names. This
  change provides more correct results, which may differ from earlier
  Android versions when your app uses classes like
  `https://developer.android.com/reference/java/text/SimpleDateFormat`.

- Android 8.0 (API level 26) updates the version of ICU to version 58.

### Alert windows

If an app uses the `https://developer.android.com/reference/android/Manifest.permission#SYSTEM_ALERT_WINDOW`
permission and uses one of the following window types to attempt to display
alert windows above other apps and system windows:

- `https://developer.android.com/reference/android/view/WindowManager.LayoutParams#TYPE_PHONE`
- `https://developer.android.com/reference/android/view/WindowManager.LayoutParams#TYPE_PRIORITY_PHONE`
- `https://developer.android.com/reference/android/view/WindowManager.LayoutParams#TYPE_SYSTEM_ALERT`
- `https://developer.android.com/reference/android/view/WindowManager.LayoutParams#TYPE_SYSTEM_OVERLAY`
- `https://developer.android.com/reference/android/view/WindowManager.LayoutParams#TYPE_SYSTEM_ERROR`

...then these windows always appear beneath the windows that use the
`https://developer.android.com/reference/android/view/WindowManager.LayoutParams#TYPE_APPLICATION_OVERLAY` window
type. If an app targets Android 8.0 (API level 26), the app uses the
`https://developer.android.com/reference/android/view/WindowManager.LayoutParams#TYPE_APPLICATION_OVERLAY`
window type to display alert windows.

For more information, see the [Common window types for
alert windows](https://developer.android.com/about/versions/oreo/android-8.0-changes#cwt) section within the behavior changes for [Apps
targeting Android 8.0](https://developer.android.com/about/versions/oreo/android-8.0-changes#o-apps).

### Input and navigation

With the advent of Android apps on ChromeOS and other large form factors,
such as tablets, we're seeing a resurgence of keyboard navigation use within
Android apps. Within Android 8.0 (API level 26), we've re-addressed using
the keyboard as a navigation input device, resulting in a more reliable,
predictable model for arrow- and tab-based navigation.

In particular, we've made the following changes to element focus
behavior:

- If you haven't defined any focus state colors for a
  `https://developer.android.com/reference/android/view/View` object (either its foreground or background
  drawable), the framework now sets a default focus highlight color for the
  `https://developer.android.com/reference/android/view/View`. This focus highlight is a ripple drawable that's
  based on the activity's theme.

  If you don't want a `https://developer.android.com/reference/android/view/View` object to use this default
  highlight when it receives focus, set the
  `android:defaultFocusHighlightEnabled` attribute to
  `false` in the layout XML file containing the
  `https://developer.android.com/reference/android/view/View`, or pass in `false` to
  `setDefaultFocusHighlightEnabled()` in your app's UI logic.
- To test how keyboard input affects UI element focus, you can enable the **Drawing \> Show layout bounds** developer option. In Android 8.0, this option displays an "X" icon over the element that currently has focus.

Also, all toolbar elements in Android 8.0 are automatically
[keyboard navigation clusters](https://developer.android.com/about/versions/oreo/android-8.0#kbnc),
making it easier for users to navigate into and out of each toolbar as a
whole.

To learn more about how to improve support for keyboard navigation within
your app, read the [Supporting
Keyboard Navigation](https://developer.android.com/training/keyboard-input/navigation) guide.

### Web form autofill

Now that the Android [Autofill
Framework](https://developer.android.com/guide/topics/text/autofill) provides built-in support for autofill functionality, the
following methods related to `https://developer.android.com/reference/android/webkit/WebView` objects have changed
for apps installed on devices running Android 8.0 (API level 26):

`https://developer.android.com/reference/android/webkit/WebSettings`
:
    - The `https://developer.android.com/reference/android/webkit/WebSettings#getSaveFormData()` method now returns `false`. Previously, this method returned `true` instead.
    - Calling `https://developer.android.com/reference/android/webkit/WebSettings#setSaveFormData(boolean)` no longer has any effect.

`https://developer.android.com/reference/android/webkit/WebViewDatabase`
:
    - Calling `https://developer.android.com/reference/android/webkit/WebViewDatabase#clearFormData()` no longer has any effect.
    - The `https://developer.android.com/reference/android/webkit/WebViewDatabase#hasFormData()` method now returns `false`. Previously, this method returned `true` when the form contained data.

### Accessibility

Android 8.0 (API level 26) includes the following changes to accessibility:

- The accessibility framework now converts all double-tap gestures into
  `https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo.AccessibilityAction#ACTION_CLICK`
  actions. This change allows TalkBack to behave more like other
  accessibility services.

  If your app's `https://developer.android.com/reference/android/view/View` objects use custom touch
  handling, you should verify that they still work with TalkBack. You might
  just need to register the click handler that your `https://developer.android.com/reference/android/view/View`
  objects use. If TalkBack still doesn't recognize gestures performed on these
  `https://developer.android.com/reference/android/view/View` objects, override
  `https://developer.android.com/reference/android/view/View#performAccessibilityAction(int, android.os.Bundle)`.
- Accessibility services are now aware of all `https://developer.android.com/reference/android/text/style/ClickableSpan` instances within your app's `https://developer.android.com/reference/android/widget/TextView` objects.

To learn more about how to make your app more accessible, see
[Accessibility](https://developer.android.com/guide/topics/ui/accessibility).

### Networking and HTTP(S) connectivity


Android 8.0 (API level 26) includes the following behavior changes to
networking and HTTP(S) connectivity:

- OPTIONS requests with no body have a `Content-Length: 0` header. Previously they had no `Content-Length` header.
- HttpURLConnection normalizes URLs containing empty paths by appending a slash after the host or authority name with a slash. For example, it converts `http://example.com` to `http://example.com/`.
- A custom proxy selector set via ProxySelector.setDefault() only targets the address (scheme, host and port) of a requested URL. As a result, proxy selection may only be based on those values. A URL passed to a custom proxy selector does not include the requested URL's path, query parameters, or fragments.
- URIs cannot contain empty labels.
  Previously, the platform supported a workaround to accept empty labels in
  host names, which is an illegal use of URIs. This workaround was for
  compatibility with older libcore releases. Developers using the API
  incorrectly would see an ADB message: "URI example..com has empty labels in
  the hostname. This is malformed and will not be accepted in future Android
  releases."

  Android 8.0 removes this workaround; the system returns
  null for malformed URIs.

- Android 8.0's implementation of HttpsURLConnection does not perform insecure TLS/SSL protocol version fallback.
- Handling of tunneling HTTP(S) connections has changed as follows:
  - When tunneling HTTPS connection over connection, the system correctly places the port number (:443) in the Host line when sending this information to an intermediate server. Previously, the port number only occurred in the CONNECT line.
  - The system no longer sends user-agent and proxy-authorization headers from a tunneled request to the proxy server. The system no longer sends a proxy-authorization header on a
    tunneled Http(s)URLConnection to the proxy when setting up the
    tunnel. Instead, the system generates a proxy-authorization header,
    and sends it to the proxy when that proxy sends
    HTTP 407 in response to the initial request.

    Similarly, the system no longer copies the user-agent header
    from the tunneled request to the proxy request that sets up the
    tunnel. Instead, the library generates a user-agent header for that
    request.
- The `https://developer.android.com/reference/java/net/DatagramSocket#send(java.net.DatagramPacket)` method throws a SocketException if the previously executed connect() method failed.
  - DatagramSocket.connect() sets a pendingSocketException if there is an internal error. Prior to Android 8.0, a subsequent recv() call threw a SocketException even though a send() call would have succeeded. For consistency, both calls now throw a SocketException.
- InetAddress.isReachable() attempts ICMP before falling back to TCP Echo protocol.
  - Some hosts that block port 7 (TCP Echo), such as google.com, may now become reachable if they accept ICMP Echo protocol.
  - For truly unreachable hosts, this change means that twice the amount of time is spent before the call returns.

### Bluetooth


Android 8.0 (API level 26) makes the following changes to the length of
the data that the `https://developer.android.com/reference/android/bluetooth/le/ScanRecord#getBytes()`
method retrieves:

- The `https://developer.android.com/reference/android/bluetooth/le/ScanRecord#getBytes()` method makes no assumptions as to the number of bytes received. Therefore, apps should not rely on any minimum or maximum number of bytes returned. Instead, they should evaluate the length of the resulting array.
- Bluetooth 5-compatible devices may return data length exceeding the previous maximum of \~60 bytes.
- If a remote device does not provide a scan response, fewer than 60 bytes may be returned as well.

### Seamless Connectivity


Android 8.0 (API level 26) makes a number of improvements to Wi-Fi Settings to make it easier to choose
the Wi-Fi network that offers the best user experience. Specific changes include:

- Stability and reliability improvements.
- A more intuitively readable UI.
- A single, consolidated Wi-Fi Preferences menu.
- On compatible devices, automatic activation of Wi-Fi when a high quality saved network is nearby.

### Security


Android 8.0 includes the following security-related
changes:

- The platform no longer supports SSLv3.
- When establishing an HTTPS connection to a server that incorrectly implements TLS protocol-version negotiation, `https://developer.android.com/reference/javax/net/ssl/HttpsURLConnection` no longer attempts the workaround of falling back to earlier TLS protocol versions and retrying.
- Android 8.0 (API level 26) applies a Secure Computing (SECCOMP) filter to all apps. The list of allowed syscalls is restricted to those exposed through bionic. Although there are several other syscalls provided for backwards compatibility, we recommend against their use.
- Your app's `https://developer.android.com/reference/android/webkit/WebView` objects now run in multiprocess mode. Web content is handled in a separate, isolated process from the containing app's process for enhanced security.
- You can no longer assume that APKs reside in directories whose names end in -1 or -2. Apps should use `https://developer.android.com/reference/android/content/pm/ApplicationInfo#sourceDir` to get the directory, and not rely on the directory format directly.
- For information about security enhancements related to use of native libraries, see [Native Libraries](https://developer.android.com/about/versions/oreo/android-8.0-changes#nl).

In addition, Android 8.0 (API level 26) introduces the following changes related to installing
unknown apps from unknown sources:

- The value of the legacy setting `https://developer.android.com/reference/android/provider/Settings.Secure#INSTALL_NON_MARKET_APPS` is now always 1. To determine whether an unknown source can install apps using the package installer, you should instead use the return value of `https://developer.android.com/reference/android/content/pm/PackageManager#canRequestPackageInstalls()`.
- If you try to change the value of `https://developer.android.com/reference/android/provider/Settings.Secure#INSTALL_NON_MARKET_APPS` using `https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setSecureSetting(android.content.ComponentName, java.lang.String, java.lang.String)`, an `https://developer.android.com/reference/java/lang/UnsupportedOperationException` is thrown. To prevent users from installing unknown apps using unknown sources, you should instead apply the `https://developer.android.com/reference/android/os/UserManager#DISALLOW_INSTALL_UNKNOWN_SOURCES` user restriction.
- Managed profiles created on devices running Android 8.0 (API level 26) automatically have the `https://developer.android.com/reference/android/os/UserManager#DISALLOW_INSTALL_UNKNOWN_SOURCES` user restriction enabled. For existing managed profiles on devices that are upgraded to Android 8.0, the `https://developer.android.com/reference/android/os/UserManager#DISALLOW_INSTALL_UNKNOWN_SOURCES` user restriction is enabled automatically unless the profile owner has explicitly disabled this restriction (prior to upgrading) by setting `https://developer.android.com/reference/android/provider/Settings.Secure#INSTALL_NON_MARKET_APPS` to 1.

For additional details about installing unknown apps, see the
[Unknown App
Install Permissions](https://developer.android.com/studio/publish#publishing-unknown) guide.

For additional guidelines on making your app more secure, see
[Security for Android Developers](https://developer.android.com/topic/security).

### Privacy


Android 8.0 (API level 26) makes the following privacy-related
changes to the platform.

- The platform now handles identifiers differently.
  - For apps that were installed prior to an OTA to a version of Android 8.0 (API level 26) (API level 26), the value of `https://developer.android.com/reference/android/provider/Settings.Secure#ANDROID_ID` remains the same unless uninstalled and then reinstalled after the OTA. To preserve values across uninstalls after OTA, developers can associate the old and new values by using [Key/Value Backup](https://developer.android.com/guide/topics/data/keyvaluebackup.html).
  - For apps installed on a device running Android 8.0, the value of `https://developer.android.com/reference/android/provider/Settings.Secure#ANDROID_ID` is now scoped per app signing key, as well as per user. The value of `https://developer.android.com/reference/android/provider/Settings.Secure#ANDROID_ID` is unique for each combination of app-signing key, user, and device. As a result, apps with different signing keys running on the same device no longer see the same Android ID (even for the same user).
  - The value of `https://developer.android.com/reference/android/provider/Settings.Secure#ANDROID_ID` does not change on package uninstall or reinstall, as long as the signing key is the same (and the app was not installed prior to an OTA to a version of Android 8.0).
  - The value of `https://developer.android.com/reference/android/provider/Settings.Secure#ANDROID_ID` does not change even if a system update causes the package signing key to change.
  - On devices shipping with Google Play services and Advertising ID, you must use [Advertising ID.](https://support.google.com/googleplay/android-developer/answer/6048248) A simple, standard system to monetize apps, Advertising ID is a unique, user-resettable ID for advertising. It is provided by Google Play services.

    Other device manufacturers should continue
    to provide `https://developer.android.com/reference/android/provider/Settings.Secure#ANDROID_ID`.
- Querying the `net.hostname` system property produces a null result.

### Logging of uncaught exceptions


If an app installs a `https://developer.android.com/reference/java/lang/Thread.UncaughtExceptionHandler` that does
not call through to the default `https://developer.android.com/reference/java/lang/Thread.UncaughtExceptionHandler`,
the system does
not kill the app when an uncaught exception occurs. Starting from
Android 8.0 (API level 26), the system logs the exception stacktrace in this
situation; in earlier versions of the platform, the system would not have
logged the exception stacktrace.


We recommend that custom `https://developer.android.com/reference/java/lang/Thread.UncaughtExceptionHandler`
implementations always call through to
the default handler; apps that follow this recommendation are unaffected by
the change in Android 8.0.

### findViewById() signature change

All instances of the `findViewById()` method now return `
<T extends View> T` instead of `View`. This change
has the following implications:

- This may result in existing code now having ambiguous return type, for example if there is both `someMethod(View)` and `someMethod(TextView)` that takes the result of a call to `findViewById()`.
- When using Java 8 source language, this requires an explicit cast to `View` when the return type is unconstrained (for example, `assertNotNull(findViewById(...)).someViewMethod())`.
- Overrides of non-final `findViewById()` methods (for example, `Activity.findViewById()`) will need their return type updated.

### Contacts provider usage stats change


In previous versions of Android, the Contacts Provider component
allows developers to get usage data for each contact. This usage data
exposes information for each email address and each phone number associated
with a contact, including the number of times the contact has been contacted
and the last time the contact was contacted. Apps that request the
`https://developer.android.com/reference/android/Manifest.permission#READ_CONTACTS`
permission can read this data.


Apps can still read this data if they request
`https://developer.android.com/reference/android/Manifest.permission#READ_CONTACTS`
permission. In Android 8.0 (API level 26) and higher, queries for usage data return
approximations rather than exact values. The Android system maintains the
exact values internally, so this change does not affect the
auto-complete API.


This behavior change affects the following query parameters:

- `https://developer.android.com/reference/android/provider/ContactsContract.ContactOptionsColumns#TIMES_CONTACTED`
- `https://developer.android.com/reference/android/provider/ContactsContract.DataUsageStatColumns#TIMES_USED`
- `https://developer.android.com/reference/android/provider/ContactsContract.ContactOptionsColumns#LAST_TIME_CONTACTED`
- `https://developer.android.com/reference/android/provider/ContactsContract.DataUsageStatColumns#LAST_TIME_USED`

### Collection handling


`https://developer.android.com/reference/java/util/AbstractCollection#removeAll(java.util.Collection<?>)`
and `https://developer.android.com/reference/java/util/AbstractCollection#retainAll(java.util.Collection<?>)`
now always throw a `https://developer.android.com/reference/java/lang/NullPointerException`; previously, the
`https://developer.android.com/reference/java/lang/NullPointerException` was not thrown when the collection was
empty. This change makes the behavior consistent with the documentation.

### Android enterprise

Android 8.0 (API level 26) [changes the
behavior](https://developer.android.com/work/versions/Android-8.0#behavior-changes) of some APIs and features for enterprise apps, including device
policy controllers (DPCs). The changes include:

- New behaviors to help apps support work profiles on fully managed devices.
- Changes to system update handling, app verification, and authentication to increase device and system integrity.
- Improvements to the user experience for provisioning, notifications, the Recents screen, and always-on VPN.

To see the all the enterprise changes in Android 8.0 (API level 26) and learn how they might
affect your app, read [Android in the Enterprise](https://developer.android.com/work/versions/Android-8.0#behavior-changes).

## Apps targeting Android 8.0


These behavior changes apply exclusively to apps that are targeting
Android 8.0 (API level 26) or higher. Apps that compile against Android 8.0,
or set `targetSdkVersion` to Android 8.0 or higher must modify
their apps to support these behaviors properly, where applicable to the app.

### Alert windows

Apps that use the `https://developer.android.com/reference/android/Manifest.permission#SYSTEM_ALERT_WINDOW`
permission can no longer use the following window types to display alert windows
above other apps and system windows:

- `https://developer.android.com/reference/android/view/WindowManager.LayoutParams#TYPE_PHONE`
- `https://developer.android.com/reference/android/view/WindowManager.LayoutParams#TYPE_PRIORITY_PHONE`
- `https://developer.android.com/reference/android/view/WindowManager.LayoutParams#TYPE_SYSTEM_ALERT`
- `https://developer.android.com/reference/android/view/WindowManager.LayoutParams#TYPE_SYSTEM_OVERLAY`
- `https://developer.android.com/reference/android/view/WindowManager.LayoutParams#TYPE_SYSTEM_ERROR`

Instead, apps must use a new window type called
`https://developer.android.com/reference/android/view/WindowManager.LayoutParams#TYPE_APPLICATION_OVERLAY`.

When using the
`https://developer.android.com/reference/android/view/WindowManager.LayoutParams#TYPE_APPLICATION_OVERLAY` window
type to display alert windows for your app, keep the following characteristics
of the new window type in mind:

- An app's alert windows always appear under critical system windows, such as the status bar and IMEs.
- The system can move or resize windows that use the `https://developer.android.com/reference/android/view/WindowManager.LayoutParams#TYPE_APPLICATION_OVERLAY` window type to improve screen presentation.
- By opening the notification shade, users can access settings to block an app from displaying alert windows shown using the `https://developer.android.com/reference/android/view/WindowManager.LayoutParams#TYPE_APPLICATION_OVERLAY` window type.

### Content change notifications

Android 8.0 (API level 26) changes how
`https://developer.android.com/reference/android/content/ContentResolver#notifyChange(android.net.Uri, android.database.ContentObserver)`
and `https://developer.android.com/reference/android/content/ContentResolver#registerContentObserver(android.net.Uri, boolean, android.database.ContentObserver)`
behave for apps targeting Android 8.0.

These APIs now require that a valid `https://developer.android.com/reference/android/content/ContentProvider`
is defined for the authority in all Uris. Defining a valid `https://developer.android.com/reference/android/content/ContentProvider` with relevant permissions will
help defend your app against content changes from malicious apps, and prevent you
from leaking potentially private data to malicious apps.

### View focus

Clickable `https://developer.android.com/reference/android/view/View` objects are now also focusable by
default. If you want a `https://developer.android.com/reference/android/view/View` object to be clickable but not
focusable, set the
[`android:focusable`](https://developer.android.com/reference/android/view/View#attr_android:focusable) attribute to `false` in the layout
XML file containing the `https://developer.android.com/reference/android/view/View`, or pass in `false`
to `https://developer.android.com/reference/android/view/View#setFocusable(boolean)` in your app's UI
logic.

### User-agent matching in browser detection


Android 8.0 (API level 26) and higher include the
build identifier string `OPR`. Some pattern matches may
cause browser-detection logic to misidentify a non-Opera browser as Opera.
An example of such a pattern match might be:

```
if(p.match(/OPR/)){k="Opera";c=p.match(/OPR\/(\d+.\d+)/);n=new Ext.Version(c[1])}
```


To avoid issues arising from such a misidentification, use a string other than
`OPR` as a pattern-match for the Opera browser.

### Security

The following changes affect security in Android 8.0 (API level 26):

- If your app's network security configuration [opts
  out](https://developer.android.com/training/articles/security-config#CleartextTrafficPermitted) of supporting cleartext traffic, your app's `https://developer.android.com/reference/android/webkit/WebView` objects cannot access websites over HTTP. Each `https://developer.android.com/reference/android/webkit/WebView` object must use HTTPS instead.
- The **Allow unknown sources** system setting has been removed; in its place, the **Install unknown apps** permission manages unknown app installs from unknown sources. To learn more about this new permission, see the [Unknown App
  Install Permissions](https://developer.android.com/studio/publish#publishing-unknown) guide.

For additional guidelines on making your app more secure, see
[Security for Android Developers](https://developer.android.com/topic/security).

### Account access and discoverability


In Android 8.0 (API level 26), apps can no longer get access
to user accounts unless the authenticator owns the accounts or the
user grants that access. The
`https://developer.android.com/reference/android/Manifest.permission#GET_ACCOUNTS` permission
is no longer sufficient. To be granted access to an account, apps should
either use `https://developer.android.com/reference/android/accounts/AccountManager#newChooseAccountIntent(android.accounts.Account, java.util.List<android.accounts.Account>, java.lang.String[], java.lang.String, java.lang.String, java.lang.String[], android.os.Bundle)`
or an authenticator-specific
method. After getting access to accounts, an app can call
`https://developer.android.com/reference/android/accounts/AccountManager#getAccounts()`
to access them.


Android 8.0 deprecates
`https://developer.android.com/reference/android/accounts/AccountManager#LOGIN_ACCOUNTS_CHANGED_ACTION`. Apps
should instead use
`https://developer.android.com/reference/android/accounts/AccountManager#addOnAccountsUpdatedListener(android.accounts.OnAccountsUpdateListener, android.os.Handler, boolean)`
to get updates about accounts during runtime.


For information about new APIs and methods added for account access and
discoverability, see [Account Access
and Discoverability](https://developer.android.com/about/versions/oreo/android-8.0#naa) in the New APIs section of this document.

### Privacy


The following changes affect privacy in Android 8.0 (API level 26).

- The system properties `net.dns1`, `net.dns2`, `net.dns3`, and `net.dns4` are no longer available, a change that improves privacy on the platform.
- To obtain networking information such as DNS servers, apps with the `https://developer.android.com/reference/android/Manifest.permission#ACCESS_NETWORK_STATE` permission can register a `https://developer.android.com/reference/android/net/NetworkRequest` or `https://developer.android.com/reference/android/net/ConnectivityManager.NetworkCallback` object. These classes are available in Android 5.0 (API level 21) and higher.
- Build.SERIAL is deprecated. Apps needing to know the hardware serial number should instead use the new `https://developer.android.com/reference/android/os/Build#getSerial()` method, which requires the `https://developer.android.com/reference/android/Manifest.permission#READ_PHONE_STATE` permission.
- The `https://developer.android.com/reference/android/content/pm/LauncherApps` API no longer allows work profile apps to get information about the primary profile. When a user is in a work profile, the `https://developer.android.com/reference/android/content/pm/LauncherApps` API behaves as if no apps are installed in other profiles within the same profile group. As before, attempts to access unrelated profiles causes SecurityExceptions.

### Permissions

Prior to Android 8.0 (API level 26), if an app requested a permission
at runtime and the permission was granted, the system also incorrectly
granted the app the rest of the permissions that belonged to the same
permission group, and that were registered in the manifest.

For apps targeting Android 8.0, this behavior has been
corrected. The app is granted only the permissions it has explicitly
requested. However, once the user grants a permission to the app, all
subsequent requests for permissions in that permission group are
automatically granted.

For example, suppose an app lists both `https://developer.android.com/reference/android/Manifest.permission#READ_EXTERNAL_STORAGE` and
`https://developer.android.com/reference/android/Manifest.permission#WRITE_EXTERNAL_STORAGE` in its manifest.
The app requests `https://developer.android.com/reference/android/Manifest.permission#READ_EXTERNAL_STORAGE` and
the user grants it. If the app targets API level 25 or lower, the system also
grants `https://developer.android.com/reference/android/Manifest.permission#WRITE_EXTERNAL_STORAGE` at the same
time, because it belongs to the same `https://developer.android.com/reference/android/Manifest.permission_group#STORAGE` permission group and is also
registered in the manifest. If the app targets Android 8.0 (API level 26), the system grants
only `https://developer.android.com/reference/android/Manifest.permission#READ_EXTERNAL_STORAGE` at that time;
however, if the app later requests `https://developer.android.com/reference/android/Manifest.permission#WRITE_EXTERNAL_STORAGE`, the system immediately
grants that privilege without prompting the user.

### Media

- The framework can perform [automatic audio ducking](https://developer.android.com/guide/topics/media-apps/audio-focus#automatic-ducking) by itself. In this case, when another application requests focus with `AUDIOFOCUS_GAIN_TRANSIENT_MAY_DUCK`, the application that has focus reduces its volume but usually does not receive an `https://developer.android.com/reference/android/media/AudioManager.OnAudioFocusChangeListener#onAudioFocusChange(int)` callback and will not lose audio focus. New APIs are available to override this behavior for applications that need to pause instead of ducking.
- When the user takes a phone call, active media streams mute for the duration of the call.
- All audio-related APIs should use `https://developer.android.com/reference/android/media/AudioAttributes` rather than audio stream types to describe the audio playback use case. Continue to use audio stream types for volume controls only. Other uses of stream types still work (for example, the `streamType` argument to the deprecated `https://developer.android.com/reference/android/media/AudioTrack#AudioTrack(int, int, int, int, int, int)` constructor), but the system logs this as an error.
- When using an `https://developer.android.com/reference/android/media/AudioTrack`, if the application requests a large enough audio buffer, the framework will try to use the deep buffer output if it is available.
- In Android 8.0 (API level 26) the handling of [media button events](https://developer.android.com/guide/topics/media-apps/mediabuttons) is different:
  1. The handling of media buttons in a UI activity has not changed: foreground activities still get priority in handling media button events.
  2. If the foreground activity does not handle the media button event, the system routes the event to the app that most recently played audio locally. The active status, flags, and playback state of a media session are not considered when determining which app receives media button events.
  3. If the app's media session has been released, the system sends the media button event to the app's `https://developer.android.com/reference/android/support/v4/media/session/MediaButtonReceiver` if it has one.
  4. For every other case, the system discards the media button event.

### Native libraries


In apps targeting Android 8.0 (API level 26), native libraries no
longer load if they contain any load segment that is both writable and
executable. Some apps might stop working because of this change if they have
native libraries with incorrect load segments. This is a
security-hardening measure.


For more information, see [Writable and Executable Segments](https://android.googlesource.com/platform/bionic/+/master/android-changes-for-ndk-developers.md#Writable-and-Executable-Segments-Enforced-for-API-level-26).


Linker changes are tied to the API level that an app targets. If there
is a linker change at the
targeted API level, the app cannot load the library. If you are targeting
an API level lower than the API level where the linker change occurs,
logcat shows a warning.

### Collection handling


In Android 8.0 (API level 26),
`https://developer.android.com/reference/java/util/Collections#sort(java.util.List<T>)` is implemented on
top of `https://developer.android.com/reference/java/util/List#sort(java.util.Comparator<? super E>)`. The reverse
was true in Android 7.x (API levels 24 and 25):
The default implementation of `https://developer.android.com/reference/java/util/List#sort(java.util.Comparator<? super E>)`
called `https://developer.android.com/reference/java/util/Collections#sort(java.util.List<T>)`.


This change allows `https://developer.android.com/reference/java/util/Collections#sort(java.util.List<T>)`
to take advantage of optimized `https://developer.android.com/reference/java/util/List#sort(java.util.Comparator<? super E>)`
implementations, but has the following constraints:

- Implementations of `https://developer.android.com/reference/java/util/List#sort(java.util.Comparator<? super E>)`
  must not call `https://developer.android.com/reference/java/util/Collections#sort(java.util.List<T>)`,
  because doing so would result in stack overflow
  due to infinite recursion. Instead, if you want the default behavior
  in your `https://developer.android.com/reference/java/util/List` implementation, you should avoid overriding
  `sort()`.


  If a parent class implements `sort()` inappropriately, it's
  usually fine to override `https://developer.android.com/reference/java/util/List#sort(java.util.Comparator<? super E>)`
  with an implementation built on top of
  `https://developer.android.com/reference/java/util/List#toArray()`,
  `https://developer.android.com/reference/java/util/Arrays#sort(java.lang.Object[])`, and
  `https://developer.android.com/reference/java/util/ListIterator#set(E)`. For example:

  ```transact-sql
  @Override
  public void sort(Comparator<? super E> c) {
    Object[] elements = toArray();
    Arrays.sort(elements, c);
    ListIterator<E> iterator = (ListIterator<Object>) listIterator();
    for (Object element : elements) {
      iterator.next();
      iterator.set((E) element);
    }
  }
  ```


  In most cases, you can also override
  `https://developer.android.com/reference/java/util/List#sort(java.util.Comparator<? super E>)`
  with an
  implementation that delegates to different default
  implementations depending on API level. For example:

  ```transact-sql
  @Override
  public void sort(Comparator<? super E> comparator) {
    if (Build.VERSION.SDK_INT <= 25) {
      Collections.sort(this);
    } else {
      super.sort(comparator);
    }
  }
  ```


  If you're doing the latter only because you want to have a `sort()`
  method available on all API levels, consider giving it a unique name,
  such as `sortCompat()`, instead of overriding
  `sort()`.
-
  `https://developer.android.com/reference/java/util/Collections#sort(java.util.List<T>)` now counts as
  a structural modification in
  List implementations that call `sort()`. For example, in versions of
  the platform prior to Android 8.0 (API level 26), iterating over
  an `https://developer.android.com/reference/java/util/ArrayList` and calling `sort()` on it
  partway through the iteration
  would have thrown a `https://developer.android.com/reference/java/util/ConcurrentModificationException`
  if the sorting was done
  by calling `https://developer.android.com/reference/java/util/List#sort(java.util.Comparator<? super E>)`.
  `https://developer.android.com/reference/java/util/Collections#sort(java.util.List<T>)`
  did not throw an exception.


  This change makes the platform behavior more consistent: Either
  approach now results in a `https://developer.android.com/reference/java/util/ConcurrentModificationException`.

### Class-loading behavior


Android 8.0 (API level 26) checks to make sure that class loaders do not
break the assumptions of the runtime when loading new classes. These checks are
performed whether the class is referenced from Java (from
`https://developer.android.com/reference/java/lang/Class#forName(java.lang.String, boolean, java.lang.ClassLoader)`),
Dalvik bytecode, or JNI. The platform does not intercept direct calls from Java to the
`https://developer.android.com/reference/java/lang/ClassLoader#loadClass(java.lang.String)` method, nor does it check
the results of such calls. This behavior should not affect the functioning of well-behaved
class loaders.


The platform checks that the descriptor of the class that the class loader returns
matches the expected descriptor. If the returned descriptor does not match,
the platform throws a `https://developer.android.com/reference/java/lang/NoClassDefFoundError` error, and stores in
the exception a detailed message noting the discrepancy.


The platform also checks that the descriptors of the requested classes are valid. This
check catches JNI calls that indirectly load classes such as `GetFieldID()`,
passing invalid descriptors to those classes. For example, a field with signature
`java/lang/String` is not found because that signature is invalid;
it should be `Ljava/lang/String;`.


This is different from a JNI call to `FindClass()`
where `java/lang/String` is a valid fully-qualified name.


Android 8.0 (API level 26) does not support having multiple class loaders try to define classes
using the same DexFile object. An attempt to do so causes the Android runtime to throw an
`https://developer.android.com/reference/java/lang/InternalError`
error with the message "Attempt to register dex file `<filename>`
with multiple class loaders".


DexFile API is now deprecated, and you are strongly encouraged to use
one of the platform classloaders, including `PathClassLoader` or
`BaseDexClassLoader`, instead.

**Note:** You can create multiple class loaders that reference the
same APK or JAR file container from the file system. Doing so normally does not
result in much memory overhead: If DEX files in the container are stored instead of
compressed, the platform can perform an `mmap` operation on them rather than
directly extracting them. However, if the platform must extract the DEX file from the container,
referencing a DEX file in this fashion may consume a lot of memory.


In Android, all class loaders are considered parallel-capable.
When multiple threads race to load the same class with the same class
loader, the first thread to complete the operation wins, and the result is used for
the other threads. This behavior occurs regardless of whether the class loader
has returned the same class, returned a different class, or thrown an exception.
The platform silently ignores such exceptions.

**Caution:** In versions of the platform
lower than Android 8.0 (API level 26), breaking these assumptions can lead to defining the same
class multiple times, heap corruption due to class confusion,
and other undesirable effects.