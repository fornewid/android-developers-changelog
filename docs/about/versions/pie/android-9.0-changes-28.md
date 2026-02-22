---
title: https://developer.android.com/about/versions/pie/android-9.0-changes-28
url: https://developer.android.com/about/versions/pie/android-9.0-changes-28
source: md.txt
---

Android 9 (API level 28) introduces a number of changes to the Android system.
The following behavior changes apply exclusively to apps that are targeting
API level 28 or higher. Apps that set `targetSdkVersion` to API level 28 or
higher must modify
their apps to support these behaviors properly, where applicable to the app.

For changes that affect all apps running on Android 9, regardless of which API
level they target, see
[Behavior changes: all apps](https://developer.android.com/about/versions/pie/android-9.0-changes-all).

## Foreground services

Apps that target Android 9 or higher and use foreground services must request
the [`FOREGROUND_SERVICE`](https://developer.android.com/reference/android/Manifest.permission#FOREGROUND_SERVICE)
permission. This is a [normal permission](https://developer.android.com/guide/topics/permissions/normal-permissions),
so the system automatically grants it to the requesting app.

If an app that targets Android 9 or higher attempts to create a foreground service without
requesting [`FOREGROUND_SERVICE`](https://developer.android.com/reference/android/Manifest.permission#FOREGROUND_SERVICE),
the system throws a [`SecurityException`](https://developer.android.com/reference/java/lang/SecurityException).

## Privacy changes

If your app targets Android 9, you should keep the following
behavior changes in mind. These updates to device serial and DNS information
enhance user privacy.

#### Build serial number deprecation

In Android 9, [`Build.SERIAL`](https://developer.android.com/reference/android/os/Build#SERIAL) is
always set to `"UNKNOWN"` to protect users' privacy.

If your app needs to access a device's hardware serial number, you should
instead request the
[`READ_PHONE_STATE`](https://developer.android.com/reference/android/Manifest.permission#READ_PHONE_STATE)
permission, then call
[`getSerial()`](https://developer.android.com/reference/android/os/Build#getSerial()).

#### DNS privacy

Apps targeting Android 9 should honor the private DNS APIs. In particular,
apps should ensure that, if the system resolver is doing DNS-over-TLS, any
built-in DNS client either uses encrypted DNS to the same hostname as the
system, or is disabled in favor of the system resolver.

## Framework security changes

Android 9 includes several behavior changes that improve your
app's security, but these changes take effect only if your app targets API level
28 or higher.

#### Network TLS enabled by default

If your app targets Android 9 or higher, the
[`isCleartextTrafficPermitted()`](https://developer.android.com/reference/android/security/NetworkSecurityPolicy#isCleartextTrafficPermitted())
method returns `false` by default. If your app needs to enable cleartext for
specific domains, you must explicitly set `cleartextTrafficPermitted` to `true`
for those domains in your app's [Network Security
Configuration](https://developer.android.com/training/articles/security-config).

#### Web-based data directories separated by process

In order to improve app stability and data integrity in Android 9, apps cannot
share a single [`WebView`](https://developer.android.com/reference/android/webkit/WebView) data
directory among
[multiple processes](https://developer.android.com/guide/components/processes-and-threads). Typically,
such data directories store cookies, HTTP caches, and other persistent and
temporary storage related to web browsing.

In most cases, your app should use classes from the
[`android.webkit`](https://developer.android.com/reference/android/webkit/package-summary) package, such
as [`WebView`](https://developer.android.com/reference/android/webkit/WebView) and
[`CookieManager`](https://developer.android.com/reference/android/webkit/CookieManager), in only one
process. For example, you should move all
[`Activity`](https://developer.android.com/reference/android/app/Activity) objects that use a `WebView`
into the same process. You can more strictly enforce the "one process only" rule
by calling
[`disableWebView()`](https://developer.android.com/reference/android/webkit/WebView#disableWebView()) in
your app's other processes. This call prevents `WebView` from being initialized
in those other processes by mistake, even if it's being called from a dependent
library.

If your app must use instances of
[`WebView`](https://developer.android.com/reference/android/webkit/WebView) in more than one process,
you must assign a unique data directory suffix for each process, using the
[`WebView.setDataDirectorySuffix()`](https://developer.android.com/reference/android/webkit/WebView#setDataDirectorySuffix(java.lang.String))
method, before using a given instance of `WebView` in that process. This method
places web data from each process in its own directory within your app's data
directory.
| **Note:** Even if you use `setDataDirectorySuffix()`, the system doesn't share cookies and other web data across your app's process boundaries. If multiple processes in your app need access to the same web data, you need to copy it between those processes yourself. For example, you can call [`getCookie()`](https://developer.android.com/reference/android/webkit/CookieManager#getCookie(java.lang.String)) and [`setCookie()`](https://developer.android.com/reference/android/webkit/CookieManager#setCookie(java.lang.String,%20java.lang.String,%20android.webkit.ValueCallback%3Cjava.lang.Boolean%3E)) to manually transfer cookie data from one process to another.

#### Per-app SELinux domains

Apps that target Android 9 or higher cannot share data with other apps using
world-accessible Unix permissions. This change improves the integrity of the
[Android Application Sandbox](https://source.android.com/security/overview/kernel-security#the-application-sandbox),
particularly the requirement that an app's
[private data](https://developer.android.com/guide/topics/data/data-storage#filesInternal) is accessible
only by that app.

To share files with other apps, use a [content
provider](https://developer.android.com/guide/topics/providers/content-provider-basics).

## Connectivity changes

### Connectivity data counting and multipath

Within apps that target Android 9 or higher, the system counts
network traffic on networks
that aren't the current default---such as cell traffic while the device is on
Wi-Fi---and provides methods in the
[`NetworkStatsManager`](https://developer.android.com/reference/android/app/usage/NetworkStatsManager)
class to query for that traffic.

In particular,
[`getMultipathPreference()`](https://developer.android.com/reference/android/net/ConnectivityManager#getMultipathPreference(android.net.Network))
now returns a value based on the aforementioned network traffic. Beginning with
Android 9, the method returns `true` for cell data, but when more than a certain amount of
traffic accumulates in a day, it starts returning `false`. Apps running on
Android 9 must call the method and honor this hint.

The [`ConnectivityManager.NetworkCallback`](https://developer.android.com/reference/android/net/ConnectivityManager.NetworkCallback)
class now sends information about VPNs to apps. This change makes it much easier
for apps to listen for connectivity events without having to mix synchronous and
asynchronous calls and using limited APIs. Additionally, it means that
information transfer works as expected when a device is connected to multiple
Wi-Fi networks or multiple cell networks simultaneously.

### Apache HTTP client deprecation

With Android 6.0,
[we removed support for the Apache HTTP client](https://developer.android.com/about/versions/marshmallow/android-6.0-changes#behavior-apache-http-client).
Beginning with Android 9, that library is removed from the
bootclasspath and is not available to apps by default.

To continue using the Apache HTTP client, apps that target Android 9 and above
can add the following to their `AndroidManifest.xml`:

    <uses-library android:name="org.apache.http.legacy" android:required="false"/>

| **Note:** The `android:required="false"` attribute is required for apps that have a minimum SDK of 23 or lower, because on devices with API levels lower than 24, the `org.apache.http.legacy` library is not available. (On those devices, the Apache HTTP classes are available on the bootclasspath.)

As an alternative to using the runtime Apache library, apps can bundle their
own version of the `org.apache.http` library in their APK. If you do this,
you must repackage the library (with a utility like
[Jar Jar](https://github.com/shevek/jarjar)) to avoid class compatibility issues
with the classes provided in the runtime.

## UI changes

### View focus

Views with 0 area (either a width or a height is 0) are no longer focusable.

Additionally, activities no longer implicitly assign initial focus in
touch-mode. Instead, it is up to you to explicitly request initial focus, if
desired.

### CSS RGBA hex value handling

Apps that target Android 9 or higher must enable the draft
[CSS Color Module Level 4](https://drafts.csswg.org/css-color/#hex-color)
behaviour for handling 4 and 8 hex digit CSS colors.

CSS Color Module Level 4
has been supported by Chrome since release 52, but
[WebView](https://developer.android.com/reference/android/webkit/WebView) currently disables the feature
because existing Android applications were found to contain 32 bit hex colors
in the Android ordering (ARGB), which would cause rendering errors.

For example, the color `#80ff8080` is currently rendered in
[WebView](https://developer.android.com/reference/android/webkit/WebView) as opaque
light red (`#ff8080`) for apps targeting API levels 27 or lower. The leading
component (which would be interpreted by Android as the alpha component) is
currently ignored. If an app targets API level 28 or higher, `#80ff8080` is
interpreted as 50% transparent light green (`#80ff80`).

### MIME type sniffing for file: URIs

Android versions earlier than Android 9 could infer MIME types from the file
contents. Starting with Android 9 (API level 28) apps must use the
correct file extension when loading `file:` URIs in a
[WebView](https://developer.android.com/reference/android/webkit/WebView).

Using the file contents to infer MIME types can be a source of security bugs,
and this is not generally permitted by modern browsers.

If a file has a recognized file extension such as `.html`,
`.txt`, `.js`, or `.css` the MIME type will be determined by the extension.
If a file has no extension or an unrecognized one, the MIME type will be plain
text.

For example, a URI like `file:///sdcard/test.html` will be rendered as
HTML, but a URI like `file:///sdcard/test` will render as plain text,
even if the file contains HTML data.

### Document scrolling element

Android 9 properly handles the case where a document's root
element is the scrolling element.
On earlier versions, scrolling position was set on the body element, and
the root element had zero scroll values. Android 9 enables the
standards-compliant behaviour where the scrolling element *is* the root
element.

Furthermore, directly accessing `document.body.scrollTop`, `document.body.scrollLeft`,
`document.documentElement.scrollTop` or `document.documentElement.scrollLeft`
will behave differently depending on target SDK. To access viewport scroll
values, use `document.scrollingElement`, if available.

### Notifications from suspended apps

Prior to Android 9, notifications from suspended apps were canceled.
Beginning with Android 9, notifications from suspended apps are hidden until
the app is resumed.