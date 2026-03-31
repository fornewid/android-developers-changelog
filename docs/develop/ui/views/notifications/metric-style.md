---
title: Create a metric style notification  |  Views  |  Android Developers
url: https://developer.android.com/develop/ui/views/notifications/metric-style
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Views](https://developer.android.com/develop/ui/views/layout/declaring-layout)

# Create a metric style notification Stay organized with collections Save and categorize content based on your preferences.



Android 17 introduces the `MetricStyle` notifications template to support
health and fitness apps, timers, and travel app use cases.

![Timer example using MetricStyle](/static/images/ui/notifications/timer.png)


**Figure 1:** A `MetricStyle` notification template and Live Update for a clock app

## Capabilities

Metric style notifications have the following capabilities:

* Supports using the [`setContentTitle`](/reference/androidx/core/app/NotificationCompat.Builder#setContentTitle(java.lang.CharSequence)) method.
* Doesn't show the context text.
* Supports up to 3 [action](/reference/android/app/Notification.Action) buttons.
* Supports measurement of up to 3 metrics.
  + Each `Notification.Metric` requires a label, value, and an optional
    unit.
  + Expanded layout appearance varies depending on the number of metrics
    taken.

![The MetricStyle template in various states](/static/images/ui/notifications/metric-style.png)


**Figure 2:** Examples of the `MetricStyle` template in various
states. From left to right, always-on-display (AOD), promoted as a Live
Update, default/expanded, and default/collapsed.

## Behavior

The metric style notification changes behaviors based on its state:

* Metric units are appended to the label in the expanded state.
* The collapsed state's second line shows the metrics contents concatenated
  into a single line. The second and third metric appear only if they fit
  completely when concatenated.
* The unit is omitted in the collapsed state.
* Each metric receives equal horizontal space, regardless of its content.

## As a Live Update

When a metric style notification is promoted to a Live Update, keep in mind the
following considerations:

* No need to provide [`Notification.Builder#setContentTitle`](/reference/android/app/Notification.Builder#setContentTitle(java.lang.CharSequence)) because the
  metric value is used instead. If no title is provided, the app name is
  shown.
* If [`Notification.Builder#setSubtext`](/reference/androidx/core/app/NotificationCompat.Builder#setSubText(java.lang.CharSequence)) is provided, it is shown in the
  header line, rather than moved to a new line as for other promoted styles.
* Action buttons have the same pill visual treatment.

## Key points about the code

* The following is a list of relevant classes and reference documentation:
  + [`Notification.MetricStyle`](/reference/android/app/Notification.MetricStyle)
  + [`Notification.Metric`](/reference/android/app/Notification.Metric)
  + [`Notification.Metric.FixedFloat`](/reference/android/app/Notification.Metric.FixedFloat)
  + [`Notification.Metric.FixedInt`](/reference/android/app/Notification.Metric.FixedInt)
  + [`Notification.Metric.FixedTime`](/reference/android/app/Notification.Metric.FixedTime)
  + [`Notification.Metric.MetricValue`](/reference/android/app/Notification.Metric.MetricValue)
  + [`Notification.Metric.TimeDifference`](/reference/android/app/Notification.Metric.TimeDifference)

## See also

* [Notification.MetricStyle API reference](/reference/android/app/Notification.MetricStyle)
* [Notification.Metric API reference](/reference/android/app/Notification.Metric)
* [Notification.Action API reference](/reference/android/app/Notification.Action)