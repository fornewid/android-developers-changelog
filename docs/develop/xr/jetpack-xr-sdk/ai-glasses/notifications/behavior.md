---
title: Understand notification behavior for AI glasses  |  Android XR for Jetpack XR SDK  |  Android Developers
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/ai-glasses/notifications/behavior
source: html-scrape
---

The Android XR SDK has  [reached Developer Preview 3](https://android-developers.googleblog.com/2025/12/build-for-ai-glasses-with-android-xr.html), and we want your feedback! Try things out, and visit our [support page](/develop/xr/support) to reach out.

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android XR](https://developer.android.com/develop/xr)
* [Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk)
* [Guides](https://developer.android.com/develop/xr/get-started)

# Understand notification behavior for AI glasses Stay organized with collections Save and categorize content based on your preferences.



Applicable XR devices

This guidance helps you build experiences for these types of XR devices.

[Learn about XR device types →](/develop/xr/devices)

![](/static/images/develop/xr/ai-glasses-icon.svg)


AI Glasses

[Learn about XR device types →](/develop/xr/devices)

AI glasses use the standard Android notification framework, so you can notify
users across different form factors using the same notification APIs. To promote
maximum compatibility and minimize development overhead, use the Android
[`NotificationCompat`](/reference/kotlin/androidx/core/app/NotificationCompat) APIs. Android parses incoming notifications and adapts
their presentation based on the capabilities of the device.

By following the [best practices for notifications](/develop/ui/views/notifications), your existing phone
notifications can be bridged to AI glasses with little to no additional
configuration. Read the information in the following sections to understand how
the system adapts notifications for AI glasses.

## How the system determines whether to bridge a notification to AI glasses

Android uses the incoming notification's [`Notification.Style`](/reference/kotlin/androidx/core/app/NotificationCompat.Style) together with
several other criteria to determine whether or not to bridge the notification to
the user's AI glasses.

### Supported notification styles

AI glasses support a subset of Android `Notification.Style` classes. The
following notification styles are fully rendered on display AI glasses:

* [Standard style (`NotificationCompat.Style`)](/reference/kotlin/androidx/core/app/NotificationCompat.Style)

  ![Standard style
  notification](/static/images/develop/xr/jetpack-xr-sdk/glimmer/standard-notification.png)
* [`MessagingStyle`](/reference/kotlin/androidx/core/app/NotificationCompat.MessagingStyle)

  ![MessagingStyle
  notification](/static/images/develop/xr/jetpack-xr-sdk/glimmer/messagingstyle-notification.png)
* [`BigPictureStyle`](/reference/kotlin/androidx/core/app/NotificationCompat.BigPictureStyle)

  ![BigPictureStyle
  notification](/static/images/develop/xr/jetpack-xr-sdk/glimmer/bigpicturestyle-notification.png)
* [`ProgressStyle`](/reference/kotlin/androidx/core/app/NotificationCompat.ProgressStyle)
* [`MediaStyle`](/reference/kotlin/androidx/media/app/NotificationCompat.MediaStyle)
* [`CallStyle`](/reference/kotlin/androidx/core/app/NotificationCompat.CallStyle) (only when the notification [qualifies as a live
  update](/develop/ui/views/notifications/live-update))

Other notification styles (such as [`InboxStyle`](/reference/kotlin/androidx/core/app/NotificationCompat.InboxStyle)) aren't fully parsed and
rendered. For these styles, style-specific fields aren't rendered (such as the
[summary text](/reference/kotlin/androidx/core/app/NotificationCompat.InboxStyle#setSummaryText(java.lang.CharSequence)) for `InboxStyle`). Instead, the system reverts to the
standard style and renders only common fields such as the [content title](/reference/kotlin/androidx/core/app/NotificationCompat.Builder#setContentTitle(java.lang.CharSequence)).

**Note:** Custom notifications with `RemoteViews` aren't bridged to AI glasses.

### Other required criteria for bridging

Besides the notification's style, a notification must also meet the following
criteria to be bridged to AI glasses:

1. The notification isn't subject to **any** of the following user-controlled
   settings that would prevent its delivery:

   * **Glasses companion app settings**:

     + App-level toggle: By default, **app notifications are toggled off**
       in the Glasses app to help users purposefully
       decide which notifications are bridged to their AI glasses.

       This default behavior lets a user leave notifications
       enabled on their phone for a certain app, but disable them for that
       app on their AI glasses. To help a user decide whether to enable
       notifications for your app in the Glasses app,
       explain how notifications would improve their experience with your
       app.
   * **System-level notification settings on the user's phone**:

     + App-level toggle: If a user disables notifications entirely for an
       app on the phone, no notifications for that app are bridged.
     + Notification channel settings: If a user disables notifications for
       an [app-defined notification channel](/develop/ui/views/notifications/channels), no notifications for
       that channel are bridged.
   * **System-level Do Not Disturb (DND) settings on the user's phone**: AI
     glasses use the phone's DND settings. If the user's phone is in DND
     mode, notifications are also suppressed on the user's glasses.
2. The notification is assigned to a channel with [`IMPORTANCE_HIGH`](/reference/kotlin/android/app/NotificationManager#importance_high) or
   [`IMPORTANCE_MAX`](/reference/kotlin/android/app/NotificationManager#importance_max).
3. The [notification's title](/reference/kotlin/android/app/Notification#extra_title) isn't `null` or empty.
4. The notification isn't marked with [`FLAG_LOCAL_ONLY`](/reference/kotlin/android/app/Notification#flag_local_only). If this flag is
   set, the notification is restricted to the primary device.
5. The notification isn't an [ongoing notification](/reference/kotlin/android/app/Notification.Builder#setongoing), such as a persistent
   background task, unless it [qualifies as a Live Update notification](/develop/ui/views/notifications/live-update).

## How Live Update notifications are bridged to AI glasses

[Live Update notifications](/develop/ui/views/notifications/live-update) are a specialized class of notifications designed
for ongoing, user-initiated activities that require real-time monitoring, such
as rideshare ETAs, turn-by-turn navigation, or active calls. Unlike regular
notifications, live updates remain active to provide a continuous stream of
information that are surfaced prominently across the system UI.

For display AI glasses, live updates are rendered in two primary locations:

* **Home screen**: Live Update notifications appear on the Home canvas as
  [cards](/design/ui/ai-glasses/guides/components/cards). If multiple live updates are active, the system uses a
  [stack](/design/ui/ai-glasses/guides/components/stack) instead.
* **System bar**: When the user is inside another app or experience, live
  updates appear as status chips in the [system bar](/design/ui/ai-glasses/guides/surfaces/sysui#system-bar). These chips appear
  briefly whenever a status change occurs. If the display is asleep,
  a status chip automatically wakes the screen to signal a status change, so
  the user stays informed without manual interaction.

If a live update notification uses a [supported notification style](#notification-styles) for AI
glasses, it is fully parsed and rendered. Live Updates notifications that use
other notification styles (such as [`BigTextStyle`](/reference/kotlin/androidx/core/app/NotificationCompat.BigTextStyle)) aren't fully parsed,
and the system adapts them to a standard style notification instead.

## Available notification actions for display AI glasses

On display AI glasses, incoming notifications appear as [heads-up
notifications](/develop/ui/views/notifications#Heads-up) (HUNs). For `MessagingStyle` notifications, your app can use
a [direct reply](/develop/ui/views/notifications/build-notification#reply-action) action. Users can tap to expand for more details and reply.
For all other notification styles, the only available option is the
system-provided clear action.

When using direct reply, users can reply with the voice or select from a smart
reply list by scrolling forward. For smart replies, you can use our [on-device
AI](https://developers.google.com/ml-kit/language/smart-reply/android)
to suggest short, relevant replies.

[Previous

arrow\_back

Overview](/develop/xr/jetpack-xr-sdk/ai-glasses/notifications)

[Next

Start a glasses activity from a notification

arrow\_forward](/develop/xr/jetpack-xr-sdk/ai-glasses/notifications/start-activity)