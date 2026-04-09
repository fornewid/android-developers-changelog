---
title: https://developer.android.com/develop/ui/views/notifications/progress-centric
url: https://developer.android.com/develop/ui/views/notifications/progress-centric
source: md.txt
---

![top shade progress centric notification](https://developer.android.com/static/images/ui/notifications/progress-centric.png) **Figure 1.** A progress centric notification at the top of the shade.

Android 16 introduces a new notification template to help users seamlessly track
user initiated start-to-end journeys. These notifications will have upgraded
visibility on system surfaces and top ranking in the notification drawer.

Use [`Notification.ProgressStyle`](https://developer.android.com/reference/android/app/Notification.ProgressStyle) to stylize progress centric notifications.
Key use cases include rideshare, delivery, and navigation. Within
that class, you will find the ability to denote states and milestones in a user
journey using Points and Segments.

## Relevant classes

The following classes contain the different APIs that you use to construct a
`ProgressStyle` notification:

- [`Notification.ProgressStyle`](https://developer.android.com/reference/android/app/Notification.ProgressStyle)
- [`Notification.ProgressStyle.Point`](https://developer.android.com/reference/android/app/Notification.ProgressStyle.Point)
- [`Notification.ProgressStyle.Segment`](https://developer.android.com/reference/android/app/Notification.ProgressStyle.Segment)

## Anatomy and customization

The following images show the different parts that make up `ProgressStyle`
notifications:
![](https://developer.android.com/static/about/versions/16/images/progress-style-anatomy.png) **Figure 2.**

|---|---|
| A. Header - Subtext | [`Notification.Builder#setSubText()`](https://developer.android.com/reference/android/app/Notification.Builder#setSubText(java.lang.CharSequence)) |
| B. Header - Time | [`Notification.Builder#setWhen()`](https://developer.android.com/reference/androidx/core/app/NotificationCompat.Builder#setWhen(long)) |
| C. Content Title | [`Notification.Builder#setContentTitle()`](https://developer.android.com/reference/android/app/Notification.Builder#setContentTitle(java.lang.CharSequence)) |
| D. Content Text | [`Notification.Builder#setContentText()`](https://developer.android.com/reference/android/app/Notification.Builder#setContentText(java.lang.CharSequence)) |
| E. Progress bar | [`Notification.ProgressStyle`](https://developer.android.com/reference/android/app/Notification.ProgressStyle) |
| F. Action button | [`Notification.Builder#addAction()`](https://developer.android.com/reference/android/app/Notification.Builder#addAction(android.app.Notification.Action)) |

![](https://developer.android.com/static/about/versions/16/images/progress-style-icon-anatomy.png) **Figure 3.** Apps can set a vehicle image for the tracker icon and use segments and points to denote the rideshare experience and milestones.

## Set up

Use the right APIs and follow best practices to provide the best user experience
for progress updates.

- Set the right fields to meet [promoted visibility](https://developer.android.com/develop/ui/views/notifications#promoted-).
- Use the right visual elements to guide users. For example, rideshare apps should set a vehicle image and use the most accurate color of the vehicle in the notification using [`Notification#setLargeIcon`](https://developer.android.com/reference/androidx/core/app/NotificationCompat.Builder#setLargeIcon(android.graphics.drawable.Icon)).
- Use concise and clear language to define the progress of the user journey. Time of arrival, driver name, and state of the journey are important text that the notification should communicate.
- Provide useful and relevant [actions](https://developer.android.com/reference/android/app/Notification.Builder#addAction(android.app.Notification.Action)) in the notification that streamline the user journey. For example, providing "Tip" and "Add dish" to a newly initiated food delivery order are useful actions before delivery.
- Use [segments](https://developer.android.com/partners/android-16/live-notifications/android/app/Notification.ProgressStyle.Segment) and [points](https://developer.android.com/partners/android-16/live-notifications/android/app/Notification.ProgressStyle.Point) to denote states. For example, segments can colorize the state and duration of traffic in a rideshare journey. Points represent states for milestones such as food preparation, delivery, and passenger pickup.
- [Update](https://developer.android.com/develop/ui/views/notifications/build-notification#Updating) the progress experience to accurately reflect the actual progression of the journey. For example, changes in traffic conditions can be reflected in changes in segment colors and updates in text.

The following example shows a `ProgressStyle` notification for a rideshare app.

The example shows the use of a vehicle image for the tracker icon, and the use
of segments and points to denote the rideshare experience and milestones.

See the [sample app](https://github.com/android/platform-samples/tree/main/samples/user-interface/live-updates) to experiment with these APIs.