---
title: Create a call style notification for call apps  |  Views  |  Android Developers
url: https://developer.android.com/develop/ui/views/notifications/call-style
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Views](https://developer.android.com/develop/ui/views/layout/declaring-layout)

# Create a call style notification for call apps Stay organized with collections Save and categorize content based on your preferences.



On Android 12.0 (API level 31) and later, the system provides the
[`CallStyle`](/reference/android/app/Notification.CallStyle) notification template to distinguish call notifications from
other types of notifications. Use this template to create incoming or
ongoing call notifications. The template supports large-format notifications
that include caller information and required actions such as answering or
declining calls.

Because incoming and ongoing calls are high priority events, these notifications
receive top priority in the notification shade. This ranking also enables the
system to forward these prioritized calls to other devices.

The `CallStyle` notification template includes the following required actions:

* **Answer** or **Decline** for incoming calls.
* **Hang up** for ongoing calls.
* **Answer** or **Hang up** for call screening.

Actions in this style appear as buttons, with the system automatically adding
appropriate icons and text. Manual labeling of the buttons is not supported.
For more information about notification design principles, see
[Notifications](/design/ui/mobile/guides/home-screen/notifications).

![Call style notifications with labelled buttons](/static/images/ui/notifications/CallStyle.png)


**Figure 1.** CallStyle template for incoming and ongoing calls.

The required actions are passed as intents, such as `hangupIntent` and
`answerIntent` in the following sections. Each of these are a reference to a
token maintained by the system. The token is a lightweight object that
can be passed between different apps and processes. The system is
responsible for managing the lifetime of the token and ensuring that the
`PendingIntent` is usable even if the app that created it is no longer
running. When you give another app a `PendingIntent`, you are granting
it the permission to perform the operation specified, such as decline or answer.
This permission is granted even if the app that created the intent
is not currently running. For more information, see the reference documentation
for [`PendingIntent`](/reference/android/app/PendingIntent).

Starting in Android 14 (API level 34), you can configure call notifications
to be non-dismissible. To do so, use `CallStyle` notifications with the
[`Notification.FLAG_ONGOING_EVENT`](/reference/android/app/Notification#FLAG_ONGOING_EVENT) through
[`Notification.Builder#setOngoing(true)`](/reference/android/app/Notification.Builder#setOngoing(boolean)).

The following are examples of using various methods with the `CallStyle`
notification.

### Kotlin

```
// Create a new call, setting the user as the caller.
val incomingCaller = Person.Builder()
    .setName("Jane Doe")
    .setImportant(true)
    .build()
```

### Java

```
// Create a new call with the user as the caller.
Person incomingCaller = new Person.Builder()
    .setName("Jane Doe")
    .setImportant(true)
    .build();
```

## Incoming call

Use the `forIncomingCall()` method to create a call style notification for an
incoming call.

### Kotlin

```
// Create a call style notification for an incoming call.
val builder = Notification.Builder(context, CHANNEL_ID)
    .setContentIntent(contentIntent)
    .setSmallIcon(smallIcon)
    .setStyle(
         Notification.CallStyle.forIncomingCall(caller, declineIntent, answerIntent))
    .addPerson(incomingCaller)
```

### Java

```
// Create a call style notification for an incoming call.
Notification.Builder builder = Notification.Builder(context, CHANNEL_ID)
    .setContentIntent(contentIntent)
    .setSmallIcon(smallIcon)
    .setStyle(
        Notification.CallStyle.forIncomingCall(caller, declineIntent, answerIntent))
    .addPerson(incomingCaller);
```

## Ongoing call

Use the `forOngoingCall()` method to create a call style notification for an
ongoing call.

### Kotlin

```
// Create a call style notification for an ongoing call.
val builder = Notification.Builder(context, CHANNEL_ID)
    .setContentIntent(contentIntent)
    .setSmallIcon(smallIcon)
    .setStyle(
         Notification.CallStyle.forOngoingCall(caller, hangupIntent))
    .addPerson(second_caller)
```

### Java

```
// Create a call style notification for an ongoing call.
Notification.Builder builder = new Notification.Builder(context, CHANNEL_ID)
    .setContentIntent(contentIntent)
    .setSmallIcon(smallIcon)
    .setStyle(
        Notification.CallStyle.forOngoingCall(caller, hangupIntent))
    .addPerson(second_caller);
```

## Screen a call

Use the `forScreeningCall()` method to create a call style notification for
screening a call.

### Kotlin

```
// Create a call style notification for screening a call.
val builder = Notification.Builder(context, CHANNEL_ID)
    .setContentIntent(contentIntent)
    .setSmallIcon(smallIcon)
    .setStyle(
         Notification.CallStyle.forScreeningCall(caller, hangupIntent, answerIntent))
    .addPerson(second_caller)
```

### Java

```
// Create a call style notification for screening a call.
Notification.Builder builder = new Notification.Builder(context, CHANNEL_ID)
    .setContentIntent(contentIntent)
    .setSmallIcon(smallIcon)
    .setStyle(
        Notification.CallStyle.forScreeningCall(caller, hangupIntent, answerIntent))
    .addPerson(second_caller);
```

## Provide compatibility across more Android versions

Associate `CallStyle` notifications on API versions 30 or earlier with a
foreground service in order to assign them the high rank they are given in API
level 31 or later. Additionally, `CallStyle` notifications on API version 30
or earlier can achieve a similar ranking by marking the notification as
colorized, using the [`setColorized()`](/reference/android/app/Notification.Builder#setColorized(boolean)) method.

Use the Telecom APIs with `CallStyle` notifications. For more information, see
[Telecom framework overview](/guide/topics/connectivity/telecom).