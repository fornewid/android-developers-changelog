---
title: https://developer.android.com/about/versions/12/behavior-changes-12
url: https://developer.android.com/about/versions/12/behavior-changes-12
source: md.txt
---

Like earlier releases, Android 12 includes behavior changes that
may affect your app. The following behavior changes apply exclusively to apps
that are targeting Android 12 or higher. If your app is
targeting Android 12, you should modify your app to support these behaviors
properly, where applicable.

Be sure to also review the list of [behavior changes that affect all apps
running on Android 12](https://developer.android.com/about/versions/12/behavior-changes-all).

## User experience

### Custom notifications

Android 12 changes the appearance and behavior of fully [custom notifications](https://developer.android.com/training/notify-user/custom-notification).
Previously, custom notifications were able to use the entire notification area
and provide their own layouts and styles. This resulted in anti-patterns that
could confuse users or cause layout compatibility issues on different devices.

For apps targeting Android 12, notifications with custom content views will no
longer use the full notification area; instead, the system applies a standard
template. This template ensures that custom notifications have the same
decoration as other notifications in all states, such as the notification's icon
and expansion affordances (in the collapsed state) and the notification's icon,
app name, and collapse affordance (in the expansion state). This behavior is
nearly identical to the behavior of
[`Notification.DecoratedCustomViewStyle`](https://developer.android.com/reference/android/app/Notification.DecoratedCustomViewStyle).

In this way, Android 12 makes all notifications visually consistent and easy to
scan, with a discoverable, familiar notification expansion for users.

The following illustration shows a custom notification in the standard template:

![](https://developer.android.com/static/images/about/versions/12/customizable-area.png)

The following examples show how custom notifications would render in a collapsed
and an expanded state:
![](https://developer.android.com/static/images/about/versions/12/custom-collapsed-view.png) ![](https://developer.android.com/static/images/about/versions/12/custom-expanded-view.png)

The change in Android 12 affects apps that define custom subclasses of
[`Notification.Style`](https://developer.android.com/reference/android/app/Notification.Style), or which use
[`Notification.Builder`](https://developer.android.com/reference/android/app/Notification.Builder)'s methods
[`setCustomContentView(RemoteViews)`](https://developer.android.com/reference/android/app/Notification.Builder#setCustomContentView(android.widget.RemoteViews)),
[`setCustomBigContentView(RemoteViews)`](https://developer.android.com/reference/android/app/Notification.Builder#setCustomBigContentView(android.widget.RemoteViews)),
and [`setCustomHeadsUpContentView(RemoteViews)`](https://developer.android.com/reference/android/app/Notification.Builder#setCustomHeadsUpContentView(android.widget.RemoteViews)).

If your app is using fully custom notifications, we recommend testing with the
new template as soon as possible.

1. Enable the custom notifications change:

   1. Change your app's `targetSdkVersion` to `S` to enable the new behavior.
   2. Recompile.
   3. Install your app on a device or emulator running Android 12.
2. Test all notifications that use custom views, ensuring they look as you
   expect in the shade. While testing, take these considerations into account
   and make the necessary adjustments:

   - The dimensions of custom views have changed. In general, the height
     afforded to custom notifications is less than before. In the collapsed
     state, the maximum height of the custom content has decreased from 106dp
     to 48dp. Also, there is less horizontal space.

   - All notifications are expandable for apps targeting Android 12.
     Typically, this means if you're using [`setCustomContentView`](https://developer.android.com/reference/android/app/Notification.Builder#setCustomContentView(android.widget.RemoteViews)),
     you'll also want to use [`setBigCustomContentView`](https://developer.android.com/reference/android/app/Notification.Builder#setCustomBigContentView(android.widget.RemoteViews))
     to make sure collapsed and expanded states are consistent.

   - To make sure that the "Heads Up" state looks as you expect, don't forget
     to raise the importance of the notification channel to "HIGH" (Pops on
     screen).

### Android App Links verification changes

On apps that target Android 12 or higher, the system makes
several changes to how [Android App Links are
verified](https://developer.android.com/training/app-links/verify-android-applinks#auto-verification). These
changes improve the reliability of the app-linking experience and provide more
control to app developers and end users.

If you rely on Android App Link verification to open web links in your app,
check that you use the correct format when you [add intent
filters](https://developer.android.com/training/app-links/verify-android-applinks#add-intent-filters) for
Android App Link verification. In particular, make sure that these intent
filters include the `BROWSABLE` category and support the `https` scheme.

You can also [manually
verify](https://developer.android.com/training/app-links/verify-android-applinks#auto-verification) your
app's links to test the reliability of your declarations.

### Picture-in-picture behavior improvements

Android 12 introduces behavior improvements for picture-in-picture (PiP) mode,
and recommended cosmetic improvements to transition animations for both gesture
navigation and element-based navigation.

See [Picture-in-picture
improvements](https://developer.android.com/about/versions/12/features/pip-improvements) for more
information.

### Toast redesign

In Android 12, the [toast](https://developer.android.com/reference/android/widget/Toast) view has been
redesigned. Toasts are now limited to two lines of text and show the application
icon next to the text.
![Image of Android device showing a toast popup reading
'Sending message' next to an app icon](https://developer.android.com/static/images/toast.png)

See [Toasts overview](https://developer.android.com/guide/topics/ui/notifiers/toasts) for further details.

## Security and privacy

### Approximate location

On devices that run Android 12 or higher, [users can request
approximate location
accuracy](https://developer.android.com/training/location/permissions#approximate-request) for your app.

> [!NOTE]
> **Note:** On some releases of Android 12, [this change always affects
> your app](https://developer.android.com/about/versions/12/behavior-changes-all#approximate-location), regardless of target SDK version.

### Modern SameSite cookies in WebView

Android's WebView component is based on [Chromium](https://www.chromium.org/),
the open source project that powers Google's Chrome browser. Chromium introduced
changes to the handling of third-party cookies to provide more security and
privacy and offer users more transparency and control. Starting in Android 12,
these changes are also included in `WebView` when apps target
Android 12 (API level 31) or higher.

The `SameSite` attribute of a cookie controls whether it can be sent with any
requests, or only with same-site requests. The following privacy-protecting
changes improve the default handling of third-party cookies and help protect
against unintended cross-site sharing:

- Cookies without a `SameSite` attribute are treated as `SameSite=Lax`.
- Cookies with `SameSite=None` must also specify the `Secure` attribute, meaning they require a secure context and should be sent over HTTPS.
- Links between HTTP and HTTPS versions of a site are now treated as cross-site requests, so cookies are not sent unless they are appropriately marked as `SameSite=None; Secure`.

For developers, the general guidance is to identify the cross-site cookie
dependencies in your critical user flows and ensure that the `SameSite`
attribute is explicitly set with the appropriate values where needed. You must
explicitly specify the cookies that are allowed to work across websites or
across same-site navigations that move from HTTP to HTTPS.

For complete guidance for web developers on these changes, see [SameSite Cookies
Explained](https://web.dev/samesite-cookies-explained/) and [Schemeful
SameSite](https://web.dev/schemeful-samesite/).

#### Test SameSite behaviors in your app

If your app uses WebView, or if you manage a website or service that uses
cookies, we recommend testing your flows on Android 12 WebView.
If you find issues, you might need to update your cookies to support the new
SameSite behaviors.

Watch for issues in logins and embedded content, as well as sign-in flows,
purchasing, and other authentication flows where the user starts on an insecure
page and transitions to a secure page.

To test an app with WebView, you must enable the new SameSite behaviors for the
app that you want to test by completing either of the following steps:

- Manually enable SameSite behaviors on the test device by [toggling the UI flag
  webview-enable-modern-cookie-same-site](https://chromium.googlesource.com/chromium/src/+/HEAD/android_webview/docs/developer-ui.md#Flag-UI)
  in the [WebView devtools](https://chromium.googlesource.com/chromium/src/+/HEAD/android_webview/docs/developer-ui.md#launching-webview-devtools).

  This approach lets you test on any device running Android 5.0 (API level 21)
  or higher---including Android 12---and WebView version 89.0.4385.0
  or higher.
- Compile your app to target Android 12 (API level 31) by [`targetSdkVersion`](https://developer.android.com/guide/topics/manifest/uses-sdk-element#target).

  If you use this approach, you must use a device that runs
  Android 12.

For information on remote debugging for WebView on Android, see [Get Started
with Remote Debugging Android Devices](https://developers.google.com/web/tools/chrome-devtools/remote-debugging/).

#### Other resources

For more information about the SameSite modern behaviors and rollout to Chrome
and WebView, visit the [Chromium SameSite Updates
page](https://www.chromium.org/updates/same-site). If you find a bug in WebView
or Chromium, you can report it in the public [Chromium issue
tracker](https://bit.ly/2lJMd5c).

### Motion sensors are rate-limited

To protect potentially sensitive information about users, if your app targets
Android 12 or higher, the system places a limit on the refresh
rate of data from certain motion sensors and position sensors.

Learn more about [sensor
rate-limiting](https://developer.android.com/guide/topics/sensors/sensors_overview#sensors-rate-limiting).

### App hibernation

Android 12 expands upon the [permissions auto-reset
behavior](https://developer.android.com/training/permissions/requesting#auto-reset-permissions-unused-apps)
that was introduced in Android 11 (API level 30). If your app targets
Android 12 and the user doesn't interact with your app for a few
months, the system auto-resets any granted permissions and places your app in a
*hibernation* state.

Learn more in the guide about [app
hibernation](https://developer.android.com/topic/performance/app-hibernation).

### Attribution declaration in data access auditing

The data access auditing API, introduced in Android 11 (API level 30), allows you
to [create attribution
tags](https://developer.android.com/guide/topics/data/audit-access#audit-by-attribution-tag) based on your
app's use cases. These tags make it easier for you to determine which part of
your app performs a specific type of data access.

If your app targets Android 12 or higher, you must [declare these
attribution tags](https://developer.android.com/guide/topics/data/audit-access#declare-attribution-tags) in
your app's manifest file.

### ADB backup restriction

To help protect private app data, Android 12 changes the default behavior of the
`adb backup` command. For apps that target Android 12 (API level 31) or higher,
when a user runs the `adb backup` command, app data is excluded from any other
system data that is exported from the device.

If your testing or development workflows rely on app data using `adb backup`,
you can now opt in to exporting your app's data by setting
[`android:debuggable`](https://developer.android.com/guide/topics/manifest/application-element#debug)
to `true` in your app's manifest file.

> [!CAUTION]
> **Caution:** To help protect your app's data, remember to set `android:debuggable` to `false` before releasing your app.

### Safer component exporting

If your app targets Android 12 or higher and contains
[activities](https://developer.android.com/guide/components/activities/intro-activities),
[services](https://developer.android.com/guide/components/services), or [broadcast
receivers](https://developer.android.com/guide/components/broadcasts) that use [intent
filters](https://developer.android.com/guide/components/intents-filters#Receiving), you must explicitly
declare the
[`android:exported`](https://developer.android.com/guide/topics/manifest/activity-element#exported) attribute
for these app components.

> [!WARNING]
> **Warning:** If an activity, service, or broadcast receiver uses intent filters and doesn't have an explicitly-declared value for `android:exported`, your app can't be installed on a device that runs Android 12 or higher.

If the app component includes the
[`LAUNCHER`](https://developer.android.com/reference/android/content/Intent#CATEGORY_LAUNCHER) category, set
`android:exported` to `true`. In most other cases, set `android:exported` to
`false`.

The following code snippet shows an example of a service that contains an intent
filter whose `android:exported` attribute is set to `false`:

```xml
<service android:name="com.example.app.backgroundService"
         android:exported="false">
    <intent-filter>
        <action android:name="com.example.app.START_BACKGROUND" />
    </intent-filter>
</service>
```

#### Messages in Android Studio

If your app contains an activity, service, or broadcast receiver that uses
intent filters but doesn't declare `android:exported`, the following warning
messages appear, depending on the version of Android Studio that you use:

##### Android Studio 2020.3.1 Canary 11 or later

The following messages appear:

1. The following lint warning appears in your manifest file:

       When using intent filters, please specify android:exported as well

2. When you attempt to compile your app, the following build error message
   appears:

       Manifest merger failed : Apps targeting Android 12 and higher are required \
       to specify an explicit value for android:exported when the corresponding \
       component has an intent filter defined.

##### Older versions of Android Studio

If you attempt to install the app, [Logcat](https://developer.android.com/studio/command-line/logcat)
displays the following error message:

    Installation did not succeed.
    The application could not be installed: INSTALL_FAILED_VERIFICATION_FAILURE
    List of apks:
    [0] '.../build/outputs/apk/debug/app-debug.apk'
    Installation failed due to: 'null'

### Pending intents mutability

If your app targets Android 12, you must [specify the
mutability](https://developer.android.com/guide/components/intents-filters#DeclareMutabilityPendingIntent) of
each [`PendingIntent`](https://developer.android.com/reference/android/app/PendingIntent) object that your
app creates. This additional requirement improves your app's security.

#### Test the pending intent mutability change

To determine whether your app is missing mutability declarations, look for the
following [lint warning](https://developer.android.com/studio/write/lint) in Android Studio:

    Warning: Missing PendingIntent mutability flag [UnspecifiedImmutableFlag]

### Unsafe intent launches

To improve platform security, Android 12 and higher provide a
debugging feature that [detects unsafe launches of
intents](https://developer.android.com/guide/components/intents-filters#DetectUnsafeIntentLaunches). When
the system detects such an unsafe launch, a
[StrictMode](https://developer.android.com/reference/android/os/StrictMode) violation occurs.

## Performance

### Foreground service launch restrictions

Apps that target Android 12 or higher can't [start foreground
services while running in the
background](https://developer.android.com/guide/components/foreground-services#background-start-restrictions),
except for [a few special
cases](https://developer.android.com/guide/components/foreground-services#background-start-restriction-exemptions).
If an app attempts to start a foreground service while running in the
background, an exception occurs (except for the few special cases).

Consider using WorkManager to schedule and start [expedited
work](https://developer.android.com/topic/libraries/architecture/workmanager/how-to/define-work#expedited)
while your app runs in the background. To complete time-sensitive actions that
the user requests, start foreground services within an [exact
alarm](https://developer.android.com/training/scheduling/alarms#exact).

### Exact alarm permission

To encourage apps to conserve system resources, apps that target
Android 12 and higher and set [exact
alarms](https://developer.android.com/training/scheduling/alarms#exact) must have access to the "Alarms \&
reminders" capability that appears within the **Special app access** screen in
system settings.

To obtain this special app access, request the
[`SCHEDULE_EXACT_ALARM`](https://developer.android.com/reference/android/Manifest.permission#SCHEDULE_EXACT_ALARM)
permission in the manifest.

Exact alarms should only be used for user-facing features. Learn more about the
[acceptable use cases for setting an exact
alarm](https://developer.android.com/training/scheduling/alarms#exact-acceptable-use-cases).

#### Disable the behavior change

As you prepare your app to target Android 12, you can temporarily
disable the behavior change in your debuggable [build
variant](https://developer.android.com/studio/build/build-variants) for testing purposes. To do so, complete
one of the following tasks:

- In the **Developer options** setting screen, select **App Compatibility
  Changes** . On the screen that appears, tap on your app's name, then turn off [**REQUIRE_EXACT_ALARM_PERMISSION**](https://developer.android.com/about/versions/12/reference/compat-framework-changes#require_exact_alarm_permission).
- In a terminal window on your development machine, run the following command:

  ```
  adb shell am compat disable REQUIRE_EXACT_ALARM_PERMISSION PACKAGE_NAME
  ```

### Notification trampoline restrictions

When users interact with
[notifications](https://developer.android.com/guide/topics/ui/notifiers/notifications), some apps respond to
notification taps by launching an [app
component](https://developer.android.com/guide/components/fundamentals#Components) that eventually starts the
activity that the user finally sees and interacts with. This app component is
known as a *notification trampoline*.

To improve app performance and UX, apps that target Android 12 or
higher can't start activities from [services](https://developer.android.com/guide/components/services) or
[broadcast receivers](https://developer.android.com/guide/components/broadcasts) that are used as
notification trampolines. In other words, after the user taps on a notification,
or an [action button](https://developer.android.com/training/notify-user/build-notification#Actions) within
the notification, your app cannot call
[`startActivity()`](https://developer.android.com/reference/android/content/Context#startActivity(android.content.Intent))
inside of a service or broadcast receiver.

When your app tries to start an activity from a service or broadcast receiver
that acts as a notification trampoline, the system prevents the activity from
starting, and the following message appears in
[Logcat](https://developer.android.com/studio/command-line/logcat):

    Indirect notification activity start (trampoline) from PACKAGE_NAME, \
    this should be avoided for performance reasons.

> [!NOTE]
> **Note:** While it's still possible for apps with the [`SYSTEM_ALERT_WINDOW`](https://developer.android.com/reference/android/Manifest.permission#SYSTEM_ALERT_WINDOW) permission to start activities using a notification trampoline, you should avoid this UX pattern and [use a `PendingIntent`
> instead](https://developer.android.com/about/versions/12/behavior-changes-12#notification-trampoline-update-app).

#### Identify which app components act as notification trampolines

When testing your app, after you tap on a notification, you can identify which
service or broadcast receiver acted as the notification trampoline in your app.
To do so, look at output of the following terminal command:

```
adb shell dumpsys activity service \
  com.android.systemui/.dump.SystemUIAuxiliaryDumpService
```

A section of the output includes the text "NotifInteractionLog". This section
contains the information that's necessary to identify the component that starts
as the result of a notification tap.

#### Update your app

If your app starts an activity from a service or broadcast receiver that acts as
a notification trampoline, complete the following migration steps:

1. Create a [`PendingIntent`](https://developer.android.com/reference/android/app/PendingIntent) object that is associated with the activity that users see after they tap on the notification.
2. Use the `PendingIntent` object that you created in the previous step as part of [building your
   notification](https://developer.android.com/reference/android/app/Notification.Builder#setContentIntent(android.app.PendingIntent)).

To identify the origin of the activity, in order to perform logging for example,
use extras when posting the notification. For centralized logging, use
[`ActivityLifecycleCallbacks`](https://developer.android.com/reference/android/app/Application.ActivityLifecycleCallbacks)
or [Jetpack lifecycle observers](https://developer.android.com/topic/libraries/architecture/lifecycle).

#### Toggle the behavior

When testing a debuggable version of your app, you can enable and disable this
restriction using the `NOTIFICATION_TRAMPOLINE_BLOCK` app compatibility flag.

## Backup and restore

There are changes to how backup and restore works in apps that run on and target
Android 12 (API level 31). Android backup and restore has two forms:

- **Cloud backups:** User data is stored in a user's Google Drive so that it can later be restored on that device or a new device.
- **Device-to-device (D2D) transfers:** User data is sent directly to the user's new device from their older device, such as by using a cable.

For more information on how data is backed up and restored, see [Back up user
data with Auto Backup](https://developer.android.com/guide/topics/data/autobackup) and [Back up key-value pairs with
Android Backup Service](https://developer.android.com/guide/topics/data/keyvaluebackup).

### D2D transfer functionality changes

For apps running on and targeting Android 12 and higher:

- [Specifying include and exclude rules](https://developer.android.com/guide/topics/data/autobackup#IncludingFiles) with the XML
  configuration mechanism doesn't affect D2D transfers, though it still
  affects cloud-based backup and restore (such as Google Drive backups). To
  specify rules for D2D transfers, you must use the new configuration covered
  in the next section.

- On devices from some device manufacturers, specifying
  `android:allowBackup="false"` does disable backups to Google Drive, but
  doesn't disable D2D transfers for the app.

### New include and exclude format

Apps running on and targeting Android 12 and higher use a
different format for the XML configuration. This format makes the difference
between Google Drive backup and D2D transfer explicit by requiring you to
specify include and exclude rules separately for cloud backups and for D2D
transfer.

Optionally, you can also use it to specify rules for backup, in which case the
previously-used configuration is ignored on devices running Android 12 or
higher. The older configuration is still required for devices running Android 11
or lower.

> [!NOTE]
> **Note:** If you use the new configuration format, your app will use the new behavior when running on a device with Android 12 or higher, even if you don't yet target Android 12.

#### XML format changes

The following is the format used for backup and restore configuration in Android
11 and lower:

```xml
<full-backup-content>
    <include domain=["file" | "database" | "sharedpref" | "external" |
                     "root"] path="string"
    requireFlags=["clientSideEncryption" | "deviceToDeviceTransfer"] />
    <exclude domain=["file" | "database" | "sharedpref" | "external" |
                     "root"] path="string" />
</full-backup-content>
```

The following shows the changes in the format in bold.

```xml
<data-extraction-rules>
  <cloud-backup [disableIfNoEncryptionCapabilities="true|false"]>
    ...
    <include domain=["file" | "database" | "sharedpref" | "external" |
                        "root"] path="string"/>
    ...
    <exclude domain=["file" | "database" | "sharedpref" | "external" |
                        "root"] path="string"/>
    ...
  </cloud-backup>
  <device-transfer>
    ...
    <include domain=["file" | "database" | "sharedpref" | "external" |
                        "root"] path="string"/>
    ...
    <exclude domain=["file" | "database" | "sharedpref" | "external" |
                        "root"] path="string"/>
    ...
  </device-transfer>
</data-extraction-rules>
```

For more information, see the [corresponding section](https://developer.android.com/guide/topics/data/autobackup#xml-syntax-android-12) in
the guide to backing up user data with Auto Backup.

#### Manifest flag for apps

Point your apps to the new XML configuration by using the
[`android:dataExtractionRules`](https://developer.android.com/reference/android/R.attr#dataExtractionRules) attribute in your manifest
file. When you point to the new XML configuration, the
`android:fullBackupContent` attribute that points to the old config is ignored
on devices running Android 12 or higher. The following code sample shows the new
manifest file entries:

```xml
<application
    ...
    <!-- The below attribute is ignored. -->
    android:fullBackupContent="old_config.xml"
    <!-- You can point to your new configuration using the new
         dataExtractionRules attribute . -->
    android:dataExtractionRules="new_config.xml"
    ...>
</application>
```

## Connectivity

### Bluetooth permissions

Android 12 introduces the
[`BLUETOOTH_SCAN`](https://developer.android.com/reference/android/Manifest.permission#BLUETOOTH_SCAN),
[`BLUETOOTH_ADVERTISE`](https://developer.android.com/reference/android/Manifest.permission#BLUETOOTH_ADVERTISE),
and
[`BLUETOOTH_CONNECT`](https://developer.android.com/reference/android/Manifest.permission#BLUETOOTH_CONNECT)
permissions. These permissions make it easier for apps that target
Android 12 to [interact with Bluetooth
devices](https://developer.android.com/guide/topics/connectivity/bluetooth), especially for apps that don't
require access to device location.

To prepare your device for targeting Android 12 or higher, update
your app's logic. Instead of declaring a [legacy set of Bluetooth
permissions](https://developer.android.com/guide/topics/connectivity/bluetooth/permissions#declare-android11-or-lower),
declare a [more modern set of Bluetooth
permissions](https://developer.android.com/guide/topics/connectivity/bluetooth/permissions#declare-android12-or-higher).

### Concurrent Peer-to-Peer + Internet Connection

For apps targeting Android 12 (API level 31) or higher, devices that support
concurrent peer-to-peer and internet connections can maintain simultaneous Wi-Fi
connections to both the peer device and the primary internet-providing network,
making the user experience more seamless. Apps targeting
Android 11 (API level 30) or lower still experience the legacy behavior, where
the primary Wi-Fi network is disconnected prior to connecting to the peer
device.

#### Compatibility

[`WifiManager.getConnectionInfo()`](https://developer.android.com/reference/android/net/wifi/WifiManager#getConnectionInfo())
is able to return the [`WifiInfo`](https://developer.android.com/reference/android/net/wifi/WifiInfo) for
only a single network. Because of this, the API's behavior has been changed in
the following ways in Android 12 and higher:

- If only a single Wi-Fi network is available, its `WifiInfo` is returned.
- If more than one Wi-Fi network is available and the calling app triggered a peer-to-peer connection, the `WifiInfo` corresponding to the peer device is returned.
- If more than one Wi-Fi network is available and the calling app did not trigger a peer-to-peer connection, the primary internet-providing connection's `WifiInfo` is returned.

To provide a better user experience on devices that support dual concurrent
Wi-Fi networks, we recommend all apps---especially ones that trigger
peer-to-peer connections---migrate away from calling
`WifiManager.getConnectionInfo()` and instead use
[`NetworkCallback.onCapabilitiesChanged()`](https://developer.android.com/reference/android/net/ConnectivityManager.NetworkCallback#onCapabilitiesChanged(android.net.Network,%20android.net.NetworkCapabilities))
to get all `WifiInfo` objects that match the `NetworkRequest` used to register
the `NetworkCallback`. `getConnectionInfo()` is deprecated as of
Android 12.

The following code sample shows how to get the `WifiInfo` in a
`NetworkCallback`:

### Kotlin

```kotlin
val networkCallback = object : ConnectivityManager.NetworkCallback() {
  ...
  override fun onCapabilitiesChanged(
           network : Network,
           networkCapabilities : NetworkCapabilities) {
    val transportInfo = networkCapabilities.getTransportInfo()
    if (transportInfo !is WifiInfo) return
    val wifiInfo : WifiInfo = transportInfo
    ...
  }
}
```

### Java

```java
final NetworkCallback networkCallback = new NetworkCallback() {
  ...
  @Override
  public void onCapabilitiesChanged(
         Network network,
         NetworkCapabilities networkCapabilities) {
    final TransportInfo transportInfo = networkCapabilities.getTransportInfo();
    if (!(transportInfo instanceof WifiInfo)) return;
    final WifiInfo wifiInfo = (WifiInfo) transportInfo;
    ...
  }
  ...
};
```

### mDNSResponder native API

Android 12 changes when apps can interact with the mDNSResponder daemon using
the [mDNSResponder native API](https://android.googlesource.com/platform/external/mdnsresponder/).
Previously, when an app [registered a service on the network](https://developer.android.com/training/connect-devices-wirelessly/nsd#register)
and called the [`getSystemService()`](https://developer.android.com/reference/android/content/Context#getSystemService(java.lang.String))
method, the system's NSD service started the mDNSResponder daemon, even if the
app had not called any `NsdManager` methods yet. The daemon then subscribed the
device to the all-nodes multicast groups, causing the system to wake more
frequently and use additional power. To minimize battery usage, in Android 12
and higher the system now starts the mDNSResponder daemon only when it is needed
for NSD events and stops it afterwards.

Because this change affects when the mDNSResponder daemon is available, apps
that assume that the mDNSResponder daemon will be started after calling the
`getSystemService()` method might receive messages from the system that say that
the mDNSResponder daemon is not available. Apps that use `NsdManager` and do not
use the mDNSResponder native API are unaffected by this change.

## Vendor libraries

### Vendor-supplied native shared libraries

[Non-NDK native shared libraries](https://source.android.com/devices/tech/config/namespaces_libraries#adding-additional-native-libraries)
that are provided by silicon vendors or device manufacturers are not accessible
by default if the app is targeting Android 12 (API level 31) or higher. The
libraries are accessible only when they are explicitly requested using the
[`<uses-native-library>`](https://developer.android.com/guide/topics/manifest/uses-native-library-element)
tag.

If the app is targeting Android 11 (API level 30) or lower, the
`<uses-native-library>` tag is not required. In that case, any native shared
library is accessible regardless of whether it is an NDK library.

## Updated non-SDK restrictions

Android 12 includes updated lists of restricted non-SDK
interfaces based on collaboration with Android developers and the latest
internal testing. Whenever possible, we make sure that public alternatives are
available before we restrict non-SDK interfaces.

If your app does not target Android 12, some of these changes
might not immediately affect you. However, while you can currently use some
non-SDK interfaces ([depending on your app's target API level](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces#list-names)),
using any non-SDK method or field always carries a high risk of breaking your
app.

If you are unsure if your app uses non-SDK interfaces, you can [test your
app](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces#test-for-non-sdk)
to find out. If your app relies on non-SDK interfaces, you should begin planning
a migration to SDK alternatives. Nevertheless, we understand that some apps have
valid use cases for using non-SDK interfaces. If you cannot find an alternative
to using a non-SDK interface for a feature in your app, you should [request a
new public API](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces#feature-request).

To learn more about the changes in this release of Android, see [Updates to
non-SDK interface restrictions in Android 12](https://developer.android.com/about/versions/12/non-sdk-12). To learn more
about non-SDK interfaces generally, see [Restrictions on non-SDK
interfaces](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces).