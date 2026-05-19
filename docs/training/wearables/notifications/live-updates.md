---
title: Live Updates  |  Wear OS  |  Android Developers
url: https://developer.android.com/training/wearables/notifications/live-updates
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Wear OS](https://developer.android.com/training/wearables)

# Live Updates Stay organized with collections Save and categorize content based on your preferences.





Starting with Wear OS 7, [Live Updates](/develop/ui/views/notifications/live-update) can be displayed on Wear OS devices
either as locally generated notifications or as bridged notifications.

The API for creating Live Updates is the same as for Live Updates on the phone.
This guide covers additional considerations when working with Live Updates and
Wear OS.

For full guidance on working with the Live Updates API see the existing
[guidance](/develop/ui/views/notifications/live-update).

## Bridged Live Updates

Live Updates may bridge from the phone, however note that:

1. This is not guaranteed: OEMs can set their own configuration for bridging
   Live Updates.
2. Frequent updates may cause data to be hidden in order to conserve battery.

See the guidance on constructing Live Updates for [battery efficiency](#battery-considerations).

## Local Live Updates

Create local Live Update notifications in exactly the same way shown in the
Live Updates [API guidance](/develop/ui/views/notifications/live-update).

## Battery considerations

1. Whether posting locally or creating notifications that bridge from the
   phone, seek a balance between the frequency of the updates and the
   usefulness of the data.

   Specifically, to show time counting up or down, or the countdown to a
   specific time (e.g. ETA), use the [when guidance](/develop/ui/views/notifications/live-update#when-time) as opposed to
   regularly updating the Live Update from your app.
2. [`MetricStyle`](/develop/ui/views/notifications/metric-style) is not supported on Wear. The notification will be shown
   but without metrics.

## Appearance on Wear OS

The following is an example of a Live Update bridged to Wear OS, shown alongside
the same Live Update on the phone.

![Live Update side-by-side comparison](https://developer.android.com/training/wearables/images/live_update.png)


**Figure 1.**: Wear OS and phone Live update side-by-side

### Status Chips

In particular on Wear OS, note the value of [Status Chips](/develop/ui/views/notifications/live-update#status-chips). These may show
on the watch face or in the notification tray, depending on the device, and can
convey critical information or real-time ETAs / timers.

![Status Chip shown for Live Update](https://developer.android.com/training/wearables/images/status_in_tray.png)


**Figure 2.**: Status Chip in the notification tray



## Recommended for you

* Note: link text is displayed when JavaScript is off
* [Create a notification {:#notification}](/develop/ui/views/notifications/build-notification)
* [Engage Wear OS users in new ways with the Ongoing Activity API](/codelabs/ongoing-activity)
* [Create an expandable notification {:#expandable-notification}](/develop/ui/views/notifications/expanded)