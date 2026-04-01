---
title: Track metrics for your widget  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/glance/metrics
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Track metrics for your widget Stay organized with collections Save and categorize content based on your preferences.




Android 16 includes additional metrics APIs that are more granular. These
metrics track tap actions such as a button click, scroll, impressions, and the
widget's size and position.

**Note:** Testing widget engagement metrics requires a compileSdk of 36.1 or
higher and a device running Android 16 or higher. Test with a physical device
for the best results. For more information, see
[Get Android 16 QPR2 Beta on a Google Pixel device](/about/versions/16/qpr2/get).

The main API is [`AppWidgetEvent`](/reference/android/appwidget/AppWidgetEvent#getClickedIds%28%29). Use `WorkManager` to create a periodic
worker that captures widget engagement, whether daily, weekly, or whenever
your app is opened.

See the following snippet for an example of tracking clicks, scrolls and
impression length.

```
@RequiresApi(Build.VERSION_CODES_FULL.BAKLAVA_1)
fun getWidgetEngagementMetrics(context: Context) {
    val manager = AppWidgetManager.getInstance(context)

    val endTime = System.currentTimeMillis()
    val startTime = endTime - (24 * 60 * 60 * 1000) // a day ago

    val events = manager.queryAppWidgetEvents(startTime, endTime)

    if (events.isEmpty()) {
        Log.d(TAG, "No events found for the given time range.")
    }

    val metrics = hashMapOf(
        "clicks" to 0L,
        "scrolls" to 0L,
        "totalImpressionLength" to 0L
    )

    for (event in events) {

        Log.d(TAG, "Event Start: ${event.start}")
        Log.d(TAG, "Event End: ${event.end}")

        val widgetId = event.appWidgetId

        // Tap actions
        val clickedIds = event.clickedIds
        if (clickedIds?.isNotEmpty() == true) {
            metrics["clicks"] = metrics.getValue("clicks") + clickedIds.size
            // Log or analyze which components were clicked.
            for (id in clickedIds) {
                Log.d(TAG, "Widget $widgetId: Tap event on component with ID $id")
            }
        }

        // Scroll events
        val scrolledIds = event.scrolledIds
        if (scrolledIds?.isNotEmpty() == true) {
            metrics["scrolls"] = metrics.getValue("scrolls") + scrolledIds.size
            // Log or analyze which lists were scrolled.
            for (id in scrolledIds) {
                Log.d(TAG, "Widget $widgetId: Scroll event in list with ID/tag $id")
            }
        }

        // Impressions
        metrics["totalImpressionLength"] = metrics.getValue("totalImpressionLength") + event.visibleDuration.toMillis()
        Log.d(
            TAG,
            "Widget $widgetId: Impression event with duration " + event.visibleDuration.toMillis() + "ms"
        )

        // Position
        val position = event.position
        if (position != null) {
            Log.d(
                TAG,
                "Widget $widgetId: left=${position.left}, right=${position.right}, top=${position.top}, bottom=${position.bottom}"
            )
        }
    }
    Log.d("WidgetMetrics", "Metrics: $metrics")
}

GlanceMetrics.kt
```

To preserve system health, events are reported once an hour by default although
device manufacturers may change the reporting window. For example, on Pixel
devices if a user scrolls the same list in your widget 10 times in an hour, only
1 scroll event will be counted for that hour.

For testing, you can set the following attribute to a specified time and restart
your test device. In the following example, the report window is set to 0 ms and
events are reported immediately.

```
adb shell device_config override systemui widget_events_report_interval_ms 0
```

In order to set a custom tag for reporting clicks and scrolls, you can use
[RemoteViews.setAppWidgetEventTag](/reference/android/widget/RemoteViews#setAppWidgetEventTag(int,%20int)) on a view within your `RemoteViews`
layout. This integer tag is used when you query for `AppWidgetEvents` that
include clicks or scrolls on this view.

[Previous

arrow\_back

Handle user interaction with Glance](/develop/ui/compose/glance/user-interaction)

[Next

Manage and update GlanceAppWidget

arrow\_forward](/develop/ui/compose/glance/glance-app-widget)