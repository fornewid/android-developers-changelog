---
title: https://developer.android.com/about/versions/11/behavior-changes-all
url: https://developer.android.com/about/versions/11/behavior-changes-all
source: md.txt
---

The Android 11 platform includes behavior changes that may
affect your app. The following behavior changes apply to *all apps* when they
run on Android 11, regardless of `targetSdkVersion`. You should
test your app and then modify it as needed to support these properly, where
applicable.

Make sure to also review the list of [behavior changes that only affect
apps targeting Android 11](https://developer.android.com/about/versions/11/behavior-changes-11).

## Privacy

Android 11 introduces a changes and restrictions to enhance user
privacy, including the following:

- **[One-time permissions](https://developer.android.com/about/versions/11/privacy/permissions#one-time):** Gives users the option to grant more temporary access to location, microphone, and camera permissions.
- **[Permission dialog
  visibility](https://developer.android.com/about/versions/11/privacy/permissions#dialog-visibility):** Repeated denials of a permission implies "don't ask again."
- **[Data access auditing](https://developer.android.com/about/versions/11/privacy/data-access-auditing):** Gain insights into where your app accesses private data, both in your app's own code and in dependent libraries' code.
- **[System alert window
  permissions](https://developer.android.com/about/versions/11/privacy/permissions#system-alert):** Certain classes of apps are automatically granted the `SYSTEM_ALERT_WINDOW` permission upon request. Also, intents that include the `ACTION_MANAGE_OVERLAY_PERMISSION` intent action always bring users to a screen in system settings.
- **[Permanent
  SIM identifiers](https://developer.android.com/training/articles/user-data-ids#mobile-service-subscriptions):** On Android 11 and higher, access to the non-resettable ICCIDs through the [`getIccId()`](https://developer.android.com/reference/android/telephony/SubscriptionInfo#getIccId%28%29) method is restricted. The method returns a non-null, empty string. To uniquely identify an installed SIM on the device, use the [`getSubscriptionId()`](https://developer.android.com/reference/android/telephony/SubscriptionInfo#getSubscriptionId()) method instead. The Subscription ID provides an index value (starting at 1) for uniquely identifying installed SIMs, including physical and electronic. The value of this identifier is stable for a given SIM unless the device is factory reset.

To learn more, see the [Privacy](https://developer.android.com/about/versions/11/privacy) page.

## Exposure Notifications

Android 11 updates the platform with the
[Exposure Notifications System](https://www.google.com/covid19/exposurenotifications/)
in mind. Users can now run Exposure Notifications apps on Android 11 without
needing to turn on the device location setting. This is an exception for the
Exposure Notifications System only, given that it has been designed in such a
way that apps using it can't infer device location through Bluetooth scanning.

To protect user privacy, all other apps are still prohibited from performing
Bluetooth scanning unless the device location setting is on and the user has
granted them location permission. You can read more in our
[Update on Exposure Notifications](https://blog.google/inside-google/company-announcements/update-exposure-notifications)
post.

## Security

### SSL sockets use Conscrypt SSL engine by default

Android's default `SSLSocket` implementation is based on [Conscrypt](https://github.com/google/conscrypt).
Since Android 11, that implementation is internally
built on top of Conscrypt's `SSLEngine`.

### Scudo Hardened Allocator

Android 11 uses the
[Scudo Hardened Allocator](https://source.android.com/devices/tech/debug/scudo)
internally to service heap allocations. Scudo is capable of detecting and mitigating
some types of memory safety violations. If you are seeing Scudo-related crashes
(for example, `Scudo ERROR:`) in native crash reports, refer to the
[Scudo troubleshooting](https://source.android.com/devices/tech/debug/scudo#Troubleshooting)
documentation.

### App usage stats

To better protect users, Android 11 stores each user's app usage
stats in [credential encrypted
storage](https://source.android.com/security/encryption/file-based). Therefore,
neither the system nor any apps can access that data unless
[`isUserUnlocked()`](https://developer.android.com/reference/android/os/UserManager#isUserUnlocked(android.os.UserHandle))
returns `true`, which occurs after one of the following takes place:

- The user unlocks their device for the first time after a system startup.
- The user switches to their account on the device.

If your app already binds to an instance of
[`UsageStatsManager`](https://developer.android.com/reference/android/app/usage/UsageStatsManager), check
that you call methods on this object after the user unlocks their device.
Otherwise, the API now returns null or empty values.

### Emulator support for 5G

Android 11 adds [5G APIs](https://developer.android.com/about/versions/11/features/5g) to enable
your apps to add cutting-edge features. To test the features as you add them,
you can use the new capabilities of the [Android SDK
emulator](https://developer.android.com/studio/run/emulator). The new
functionality was added in Emulator version 30.0.22. Selecting the 5G network
setting sets
[`TelephonyDisplayInfo`](https://developer.android.com/reference/android/telephony/TelephonyDisplayInfo) to
[`OVERRIDE_NETWORK_TYPE_NR_NSA`](https://developer.android.com/reference/android/telephony/TelephonyDisplayInfo#OVERRIDE_NETWORK_TYPE_NR_NSA),
modifies the estimated bandwidth, and allows you to set meteredness to verify
that your app responds appropriately to changes in
[`NET_CAPABILITY_TEMPORARILY_NOT_METERED`](https://developer.android.com/reference/android/net/NetworkCapabilities#NET_CAPABILITY_TEMPORARILY_NOT_METERED)
status.

![](https://developer.android.com/static/images/about/versions/11/emulator-5g.png)

## Performance and debugging

### JobScheduler API call limits debugging

Android 11 offers debugging support for apps to identify
potential `JobScheduler` API invocations that have exceeded certain rate limits.
Developers can use this facility to identify potential performance issues. For
apps with the `debuggable` manifest attribute set to true, `JobScheduler` API
invocations beyond the rate limits will return [`RESULT_FAILURE`](https://developer.android.com/reference/android/app/job/JobScheduler#RESULT_FAILURE).
Limits are set such that legitimate use cases should not be affected.

### File descriptor sanitizer (fdsan)

Android 10 introduced `fdsan` (file descriptor sanitizer).
`fdsan` detects mishandling of file descriptor ownership, such as
use-after-close and double-close. The default mode for `fdsan` is changing in
Android 11. `fdsan` now aborts upon detecting an error; the
previous behavior was to log a warning and continue. If you're seeing crashes
due to `fdsan` in your application, refer to the
[`fdsan documentation`](https://android.googlesource.com/platform/bionic/+/master/docs/fdsan.md#).

## Non-SDK interface restrictions

Android 11 includes updated lists of restricted non-SDK
interfaces based on collaboration with Android developers and the latest
internal testing. Whenever possible, we make sure that public alternatives are
available before we restrict non-SDK interfaces.

If your app does not target Android 11, some of these changes
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
non-SDK interface restrictions in Android 11](https://developer.android.com/about/versions/11/non-sdk-11). To learn more
about non-SDK interfaces generally, see [Restrictions on non-SDK
interfaces](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces).

## Maps v1 shared library removed

V1 of the Maps shared library has been completely removed in
Android 11. This library was previously deprecated and stopped
functioning for apps in Android 10. Apps that previously relied
on this shared library for devices running Android 9 (API level 28) or lower
should use the [Maps SDK for
Android](https://developers.google.com/maps/documentation/android-sdk/intro)
instead.

> [!IMPORTANT]
> **Important:** After migrating to the Maps SDK for Android, remember to remove the reference to v1 of the Maps shared library from the [`<uses-library>`](https://developer.android.com/guide/topics/manifest/uses-library-element) element in your app's manifest file. Apps can no longer use [Google Play
> filtering](https://developer.android.com/google/play/filters) with the Maps v1 shared library and the `<uses-library>` element.

## Interaction with other apps

### Share content URIs

If your app shares a content URI with another app, the intent must [grant URI
access permissions](https://developer.android.com/about/versions/11/privacy/package-visibility-use-cases#grant-uri-access)
by setting at least one of the following intent flags:
[`FLAG_GRANT_READ_URI_PERMISSION`](https://developer.android.com/reference/android/content/Intent#FLAG_GRANT_READ_URI_PERMISSION)
and
[`FLAG_GRANT_WRITE_URI_PERMISSION`](https://developer.android.com/reference/android/content/Intent#FLAG_GRANT_WRITE_URI_PERMISSION).
That way, if the other app targets Android 11, it can still access the content
URI. Your app must include the intent flags even when the content URI is
associated with a content provider that your app doesn't own.

If your app owns the content provider that's associated with the content URI,
verify that the [content provider isn't
exported](https://developer.android.com/topic/security/best-practices#disallow-access-to-your-apps-content-providers).
We already recommend this security best practice.

## Library loading

### Loading ICU common library with absolute path

Apps targeting API 28 and lower can not use `dlopen(3)` to load `libicuuc`
with the absolute path "/system/lib/libicuuc.so". For those apps,
`dlopen("/system/lib/libicuuc.so", ...)` will return a null handle.

Instead, to load the library, please use the library name as the filename, for
example `dlopen("libicuuc.so", ...)`.