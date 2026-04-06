---
title: Implicit broadcast exceptions  |  Background work  |  Android Developers
url: https://developer.android.com/develop/background-work/background-tasks/broadcasts/broadcast-exceptions
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [Background work](https://developer.android.com/develop/background-work)
* [Guides](https://developer.android.com/develop/background-work/background-tasks)

# Implicit broadcast exceptions Stay organized with collections Save and categorize content based on your preferences.




As part of the Android 8.0 (API level 26) [background execution
limits](/about/versions/oreo/background#broadcasts), apps that target the
API level 26 or higher can't register broadcast receivers for implicit
broadcasts in their manifest unless the broadcast is sent specifically to them.
However, several broadcasts are exempted from these limitations. Apps can
continue to register listeners for the following broadcasts, no matter what API
level the apps target.

**Note:** Even though these implicit broadcasts still work in the
background, avoid registering listeners for them.

`ACTION_LOCKED_BOOT_COMPLETED`, `ACTION_BOOT_COMPLETED`
:   Exempted because these broadcasts are sent only once, at first boot,
    and many apps need to receive these broadcasts, such as to schedule jobs and alarms.

`ACTION_USER_INITIALIZE`, `android.intent.action.USER_ADDED`, `android.intent.action.USER_REMOVED`
:   Privileged permissions protect these broadcasts, so most normal
    apps can't receive them anyway.

`android.intent.action.TIME_SET`, `ACTION_TIMEZONE_CHANGED`, `ACTION_NEXT_ALARM_CLOCK_CHANGED`
:   Clock apps might need to receive these broadcasts to update alarms when the
    time, timezone, or alarms change.

`ACTION_LOCALE_CHANGED`
:   Only sent when the locale changes, which is not often. Apps might need to
    update their data when the locale changes.

`ACTION_USB_ACCESSORY_ATTACHED`, `ACTION_USB_ACCESSORY_DETACHED`, `ACTION_USB_DEVICE_ATTACHED`, `ACTION_USB_DEVICE_DETACHED`
:   When an app needs to know about these USB-related events, there is no
    good alternative to registering for the broadcast.

`BluetoothHeadset.ACTION_CONNECTION_STATE_CHANGED`, `BluetoothA2dp.ACTION_CONNECTION_STATE_CHANGED`, `ACTION_ACL_CONNECTED`, `ACTION_ACL_DISCONNECTED`
:   User experience is not likely to suffer if apps receive broadcasts for these
    Bluetooth events.

`ACTION_CARRIER_CONFIG_CHANGED`, `TelephonyIntents.ACTION_*_SUBSCRIPTION_CHANGED`, `TelephonyIntents.SECRET_CODE_ACTION`, `ACTION_PHONE_STATE_CHANGED`, `ACTION_PHONE_ACCOUNT_REGISTERED`, `ACTION_PHONE_ACCOUNT_UNREGISTERED`
:   OEM telephony apps might need to receive these broadcasts.

`LOGIN_ACCOUNTS_CHANGED_ACTION`
:   Some apps need to know about changes to login accounts so they can set up
    scheduled operations for the new and changed accounts.

`ACTION_ACCOUNT_REMOVED`
:   Apps that have visibility into an account receive this broadcast when the
    account is removed. If this is the only account change that the app needs
    to act on, we recommend that the app use this broadcast
    instead of the deprecated
    `LOGIN_ACCOUNTS_CHANGED_ACTION`.

`ACTION_PACKAGE_DATA_CLEARED`
:   Only sent when the user explicitly clears their data from Settings,
    so broadcast receivers are unlikely to significantly affect user experience.

`ACTION_PACKAGE_FULLY_REMOVED`
:   Some apps need to update their stored data when another package is
    removed. For those apps, there is no good alternative to registering for this
    broadcast.

    **Note:** Other package-related broadcasts (such as `ACTION_PACKAGE_REPLACED`) are *not* exempted from
    the background execution restrictions. These broadcasts are common enough that there is a
    potential performance impact to exempting them.

`ACTION_NEW_OUTGOING_CALL`
:   Apps that take action in response to users placing calls need to receive this
    broadcast.

`ACTION_DEVICE_OWNER_CHANGED`
:   This broadcast is not sent very often. Some apps need to receive it, so that
    they know that the device's security status changed.

`ACTION_EVENT_REMINDER`
:   Sent by the [calendar
    provider](/guide/topics/providers/calendar-provider) to post an event
    reminder to the calendar app. Since the calendar provider doesn't know what
    the calendar app is, this broadcast must be implicit.

`ACTION_MEDIA_MOUNTED`, `ACTION_MEDIA_CHECKING`, `ACTION_MEDIA_UNMOUNTED`, `ACTION_MEDIA_EJECT`, `ACTION_MEDIA_UNMOUNTABLE`, `ACTION_MEDIA_REMOVED`, `ACTION_MEDIA_BAD_REMOVAL`
:   These broadcasts are sent as a result of the user's physical interactions with
    the device, like installing or removing storage volumes, or as part of
    boot initialization, as available volumes get mounted. They aren't a common
    occurrence, and are usually under the user’s control.

`SMS_RECEIVED_ACTION`, `WAP_PUSH_RECEIVED_ACTION`
:   SMS recipient apps rely on these broadcasts.