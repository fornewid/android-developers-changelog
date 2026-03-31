---
title: Create an advanced widget  |  Views  |  Android Developers
url: https://developer.android.com/develop/ui/views/appwidgets/advanced
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Views](https://developer.android.com/develop/ui/views/layout/declaring-layout)

# Create an advanced widget Stay organized with collections Save and categorize content based on your preferences.




Try the Compose way

Jetpack Compose is the recommended UI toolkit for Android. Learn how to build widgets using Compose-style APIs.

[Jetpack Glance →](https://developer.android.com/develop/ui/compose/glance)

![](/static/images/android-compose-ui-logo.png)

This page explains recommended practices for creating a more advanced widget for
a better user experience.

## Optimizations for updating widget content

Updating widget content can be computationally expensive. To save battery
consumption, optimize the update type, frequency, and timing.

### Types of widget updates

There are three ways to update a widget: a full update, a partial update, and,
in the case of a collection widget, a data refresh. Each has different
computational costs and ramifications.

The following describes each update type and provides code snippets for each.

* **Full update:** call [`AppWidgetManager.updateAppWidget(int,
  android.widget.RemoteViews)`](/reference/android/appwidget/AppWidgetManager#updateAppWidget(int,%20android.widget.RemoteViews))
  to fully update the widget. This replaces the previously provided
  [`RemoteViews`](/reference/android/widget/RemoteViews) with a new
  `RemoteViews`. This is the most computationally expensive update.

  ### Kotlin

  ```
  val appWidgetManager = AppWidgetManager.getInstance(context)
  val remoteViews = RemoteViews(context.getPackageName(), R.layout.widgetlayout).also {
  setTextViewText(R.id.textview_widget_layout1, "Updated text1")
  setTextViewText(R.id.textview_widget_layout2, "Updated text2")
  }
  appWidgetManager.updateAppWidget(appWidgetId, remoteViews)
  ```

  ### Java

  ```
  AppWidgetManager appWidgetManager = AppWidgetManager.getInstance(context);
  RemoteViews remoteViews = new RemoteViews(context.getPackageName(), R.layout.widgetlayout);
  remoteViews.setTextViewText(R.id.textview_widget_layout1, "Updated text1");
  remoteViews.setTextViewText(R.id.textview_widget_layout2, "Updated text2");
  appWidgetManager.updateAppWidget(appWidgetId, remoteViews);
  ```
* **Partial update:** call
  [`AppWidgetManager.partiallyUpdateAppWidget`](/reference/android/appwidget/AppWidgetManager#partiallyUpdateAppWidget(int,%20android.widget.RemoteViews))
  to update parts of the widget. This merges the new `RemoteViews` with the
  previously provided `RemoteViews`. This method is ignored if a widget
  doesn't receive at least one full update through [`updateAppWidget(int[],
  RemoteViews)`](/reference/android/appwidget/AppWidgetManager#updateAppWidget(android.content.ComponentName,%20android.widget.RemoteViews)).

  ### Kotlin

  ```
  val appWidgetManager = AppWidgetManager.getInstance(context)
  val remoteViews = RemoteViews(context.getPackageName(), R.layout.widgetlayout).also {
  setTextViewText(R.id.textview_widget_layout, "Updated text")
  }
  appWidgetManager.partiallyUpdateAppWidget(appWidgetId, remoteViews)
  ```

  ### Java

  ```
  AppWidgetManager appWidgetManager = AppWidgetManager.getInstance(context);
  RemoteViews remoteViews = new RemoteViews(context.getPackageName(), R.layout.widgetlayout);
  remoteViews.setTextViewText(R.id.textview_widget_layout, "Updated text");
  appWidgetManager.partiallyUpdateAppWidget(appWidgetId, remoteViews);
  ```
* **Collection data refresh:** call
  [`AppWidgetManager.notifyAppWidgetViewDataChanged`](/reference/android/appwidget/AppWidgetManager#notifyAppWidgetViewDataChanged(int,%20int))
  to invalidate the data of a collection view in your widget. This triggers
  [`RemoteViewsFactory.onDataSetChanged`](/reference/android/widget/RemoteViewsService.RemoteViewsFactory#onDataSetChanged()).
  In the interim, the old data is displayed in the widget. You can safely
  perform expensive tasks synchronously with this method.

  ### Kotlin

  ```
  val appWidgetManager = AppWidgetManager.getInstance(context)
  appWidgetManager.notifyAppWidgetViewDataChanged(appWidgetId, R.id.widget_listview)
  ```

  ### Java

  ```
  AppWidgetManager appWidgetManager = AppWidgetManager.getInstance(context);
  appWidgetManager.notifyAppWidgetViewDataChanged(appWidgetId, R.id.widget_listview);
  ```

You can call these methods from anywhere in your app, as long as the app has the
same UID as the corresponding
[`AppWidgetProvider`](/reference/android/appwidget/AppWidgetProvider) class.

### Determine how often to update a widget

Widgets are updated periodically depending on the value provided for the
[`updatePeriodMillis`](/reference/android/appwidget/AppWidgetProviderInfo#updatePeriodMillis)
attribute. The widget can update in response to user interaction, broadcast
updates, or both.

#### Update periodically

You can control the frequency of the periodic update by specifying a value for
`AppWidgetProviderInfo.updatePeriodMillis` in the `appwidget-provider` XML. Each
update triggers the `AppWidgetProvider.onUpdate()` method, which is where you
can place the code to update the widget. However, consider the [alternatives for
broadcast receiver updates](#broadcastreceiver-duration) described in a
following section if your widget needs to load data asynchronously or takes more
than 10 seconds to update, because after 10 seconds, the system considers a
`BroadcastReceiver` to be non-responsive.

`updatePeriodMillis` doesn't support values of less than 30 minutes. However, if
you want to disable periodic updates, you can specify 0.

You can let users adjust the frequency of updates in a configuration. For
example, they might want a stock ticker to update every 15 minutes or only four
times a day. In this case, set the `updatePeriodMillis` to 0 and use
[`WorkManager`](/topic/libraries/architecture/workmanager) instead.

**Note:** Using repeating tasks with `WorkManager` is a good option, but similar
power restrictions apply. See [App Standby
Buckets](/about/versions/pie/power#buckets) for more information.

#### Update in response to a user interaction

Here are some recommended ways to update the widget based on user interaction:

* **From an activity of the app:** directly call
  `AppWidgetManager.updateAppWidget` in response to a user interaction, such
  as a user's tap.
* **From remote interactions, such as a notification or an app widget:**
  construct a `PendingIntent`, then update the widget from the invoked
  `Activity`, `Broadcast`, or `Service`. You can choose your own priority. For
  example, if you select a `Broadcast` for the `PendingIntent`, you can choose
  a [foreground broadcast](#broadcastreceiver-priority) to give the
  `BroadcastReceiver` priority.

#### Update in response to a broadcast event

An example of a broadcast event that requires a widget to update is when the
user takes a photo. In this case, you want to update the widget when a new photo
is detected.

You can schedule a job with `JobScheduler` and specify a broadcast as the
trigger using the
[`JobInfo.Builder.addTriggerContentUri`](/reference/android/app/job/JobInfo.Builder#addTriggerContentUri(android.app.job.JobInfo.TriggerContentUri))
method.

You can also register a `BroadcastReceiver` for the broadcast—for example,
listening for
[`ACTION_LOCALE_CHANGED`](/reference/android/content/Intent#ACTION_LOCALE_CHANGED).
However, because this consumes device resources, use this with care and listen
only to the specific broadcast. With the introduction of [broadcast
limitations](/about/versions/oreo/background#broadcasts) in Android
7.0 (API level 24) and Android 8.0 (API level 26), apps can't register implicit
broadcasts in their manifests, with certain
[exceptions](/guide/components/broadcast-exceptions).

### Considerations when updating a widget from a BroadcastReceiver

If the widget is updated from a `BroadcastReceiver`, including
`AppWidgetProvider`, be aware of the following considerations regarding the
duration and priority of a widget update.

#### Duration of the update

As a rule, the system lets broadcast receivers, which usually run in the app’s
main thread, run for up to 10 seconds before considering them non-responsive and
triggering an [Application Not
Responding](/topic/performance/vitals/anr) (ANR) error. To avoid blocking the
main thread while handling the broadcast, use the
[`goAsync`](/reference/android/content/BroadcastReceiver#goAsync()) method. If it takes
longer to update the widget, consider scheduling a task
using [`WorkManager`](/reference/androidx/work/WorkManager).

```
Caution: Any work you do here blocks further broadcasts until it completes,
so it can slow the receiving of later events.
```

See [Security considerations and best
practices](/guide/components/broadcasts#security-and-best-practices) for more
information.

#### Priority of the update

By default, broadcasts—including those made using
`AppWidgetProvider.onUpdate`—run as background processes. This means
overloaded system resources can cause a delay in the invocation of the broadcast
receiver. To prioritize the broadcast, make it a foreground process.

For example, add the
[`Intent.FLAG_RECEIVER_FOREGROUND`](/reference/android/content/Intent#FLAG_RECEIVER_FOREGROUND)
flag to the `Intent` passed to the `PendingIntent.getBroadcast` when the user
taps on a certain part of the widget.