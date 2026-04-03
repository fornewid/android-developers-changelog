---
title: Prepare your app for behavior changes in Wear OS 4  |  Android Developers
url: https://developer.android.com/training/wearables/versions/4/changes
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Wear OS](https://developer.android.com/training/wearables)

# Prepare your app for behavior changes in Wear OS 4 Stay organized with collections Save and categorize content based on your preferences.



Wear OS 4 is based on Android 13 (API level 33), which is several versions
higher than the version on which Wear OS 3 is based, Android 11 (API level 30).
So when you prepare your Wear OS app for use on Wear OS 4, you need to handle
the system behavior changes that take effect for all apps in [Android 12](/about/versions/12/behavior-changes-all) and
[Android 13](/about/versions/13/behavior-changes-all).

You can further improve your app's compatibility with this version of Wear OS by
[targeting Android 13 (API level 33)](/training/wearables/versions/4/update-target-sdk).

**Note:** After you update your app, test your app's behavior on real devices.

## Changes to permissions

The following changes related to permissions are most likely to affect your
Wear OS app on a device that runs Wear OS 4 or higher.

### Notification permission

![The allow option is the first button in the dialog](/static/training/wearables/images/notification-permission.svg)


**Figure 1.** The system permissions dialog that asks users to let your
Wear OS app post notifications. Users can choose between **Allow** and
**Don't allow**.

In most cases, users must grant a [notification runtime permission](/develop/ui/views/notifications/notification-permission) for your
app, including when your app posts notifications of [ongoing activities](/training/wearables/notifications/ongoing-activity).

**Note:** The notification permission doesn't apply to
[bridged notifications](/training/wearables/notifications/bridger),
as well as
[several
specific use cases that are exempt](/develop/ui/views/notifications/notification-permission#exemptions), such as those related to media
sessions.

When users install your app on a device that runs Wear OS 4 or higher, your
app's notifications are off by default. Before you post a local notification or
launch an ongoing activity, check whether your app is allowed to post
notifications by calling [`areNotificationsEnabled()`](/reference/android/app/NotificationManager#areNotificationsEnabled()). If this method
returns `true`, your app can show notifications. If your app doesn't have the
proper permission, these notifications silently fail without any runtime
exceptions being thrown.

When you request the [`POST_NOTIFICATIONS`](/reference/android/Manifest.permission#POST_NOTIFICATIONS) permission in your app, users
see the system permissions dialog that appears in figure 1.

### Background body sensors permission

On a device that runs Wear OS 4 or higher, users must grant your app permission
to get information from common body sensors, such as heart rate, in the
background.

Learn more in the guide to
[requesting background access to body sensor data](/health-and-fitness/guides/health-services/background-body-sensors).

### Approximate location permission

On a device that runs Wear OS 4 or higher, users can request that your app
retrieve only approximate location information, even when your app requests the
[`ACCESS_FINE_LOCATION`](/reference/android/Manifest.permission#ACCESS_FINE_LOCATION) runtime permission.

Check that your app can still fulfill its key use cases, such as showing a
running route, if the user grants only approximate location. In particular, when
using Health Services on Wear OS, take position errors into account.

Learn more about how the [user can grant only approximate location](/training/location/permissions#approximate-request).

## Changes to app components and navigation

The following changes related to app components and navigation are most likely
to affect your Wear OS app on a device that runs Wear OS 4 or higher.

### Intent filters block non-matching intents

When your app sends an intent to an exported component of another app that
targets Android 13 or higher, that intent is delivered if and only if it matches
an `<intent-filter>` element in the receiving app.

Learn how to [match intents to other apps' intent filters](/guide/components/intents-filters#match-intent-filter).

### Root launcher activity behavior

A launcher activity is at the *root* of a task if it declares an intent filter
that includes both [`ACTION_MAIN`](/reference/android/content/Intent#ACTION_MAIN) and [`CATEGORY_LAUNCHER`](/reference/android/content/Intent#CATEGORY_LAUNCHER).

If the user navigates away from this sort of launcher activity to the previous
screen, the system doesn't finish the launcher activity. Instead, it places the
launcher activity in the background.

Learn more about this change to [root launcher activities](/about/versions/12/behavior-changes-all#back-press) and the activity
lifecycle.

### App links verification

The system makes several changes to how Android App Links are verified. In
particular, the system [enforces a stricter intent filter syntax](/training/app-links/verify-android-applinks#add-intent-filters) for
demonstrating that URLs in a particular domain should open content directly in
your app. These changes improve the reliability of the app-linking experience,
which provides more control to app developers and end users.

To test the reliability of your declarations,
[manually invoke domain verification](/training/app-links/verify-android-applinks#manual-verification).

### System alert window UI is removed

Wear OS 4 removes the system UI for granting the [`SYSTEM_ALERT_WINDOW`](/reference/android/Manifest.permission#SYSTEM_ALERT_WINDOW)
permission. This UI is available on some devices that run Wear OS 3 and lower.

If you use [`ACTION_MANAGE_OVERLAY_PERMISSION`](/reference/android/provider/Settings#ACTION_MANAGE_OVERLAY_PERMISSION) to send users to a settings
page, where they could display your app over other apps, update your app's
logic. For example, if you rely on system alert windows to show important
messages, use [notifications](/training/wearables/notifications) instead.

## Changes to power and data management

The following changes related to power and data management are most likely
to affect your Wear OS app on a device that runs Wear OS 4.

### Restricted App Standby Bucket

The system places your app in the ["restricted" App Standby Bucket](/topic/performance/appstandby#restricted-bucket) if it's
not used for an extended period of time, or if it invokes an excessive number of
broadcasts and bindings.

### App hibernation

If the user doesn't interact with your app for a few months, the system places
your app in a [hibernation](/topic/performance/app-hibernation) state.

### Backup & Restore

Starting in Wear OS 4, if a specific Wear OS device supports cloud backup, users
can [back up their data to the cloud](/training/wearables/data/cloud-backup-restore) to transfer data off that device, and
they can restore data from the cloud to transfer data onto a new Wear OS device.

## Recommended for you

* Note: link text is displayed when JavaScript is off
* [Behavior changes: all apps](/about/versions/12/behavior-changes-all)
* [Foreground services](/develop/background-work/services/foreground-services)
* [Notification runtime permission](/develop/ui/views/notifications/notification-permission)