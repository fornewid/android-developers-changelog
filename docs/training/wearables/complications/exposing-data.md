---
title: https://developer.android.com/training/wearables/complications/exposing-data
url: https://developer.android.com/training/wearables/complications/exposing-data
source: md.txt
---

Complication data sources expose information to watch face
[complications](https://developer.android.com/training/wearables/watch-faces/complications),
supplying text, images, and numbers that the watch face can render.

A data source service extends
[`SuspendingComplicationDataSourceService`](https://developer.android.com/reference/kotlin/androidx/wear/watchface/complications/datasource/SuspendingComplicationDataSourceService) to deliver useful
information directly to a watch face.

## Getting started

Add the following dependency to your app module:

```kotlin
dependencies {
  implementiation("androidx.wear.watchface:watchface-complications-data-source-ktx:1.2.1")
}
```

<br />

## Create the data source service

When complication data is needed, the Wear OS system sends update requests to your data source.
To respond to the update requests, your data source must implement the
[`onComplicationRequest()`](https://developer.android.com/reference/kotlin/androidx/wear/watchface/complications/datasource/SuspendingComplicationDataSourceService#onComplicationRequest(androidx.wear.watchface.complications.datasource.ComplicationRequest)) method of the `SuspendingComplicationDataSourceService`
class.

The Wear OS system calls `onComplicationRequest()` when it needs data from your
source---for example, when a complication using your data source becomes active or when a
fixed amount of time passes.

**Note:** When your data source provides data, the watch face
receives the raw values. The watch face is responsible for formatting the data for display.

The following code snippet shows a sample implementation:

```kotlin
class MyComplicationDataSourceService : SuspendingComplicationDataSourceService() {
    override suspend fun onComplicationRequest(request: ComplicationRequest): ComplicationData? {
        // Retrieve the latest info for inclusion in the data.
        val text = getLatestData()
        return shortTextComplicationData(text)
    }

    override fun getPreviewData(type: ComplicationType): ComplicationData? {
        return shortTextComplicationData("Event 1")
    }

    private fun shortTextComplicationData(text: String) =
        ShortTextComplicationData.Builder(
            text = PlainComplicationText.Builder(text).build(),
            contentDescription = PlainComplicationText.Builder(text).build()
        )
            // Add further optional details here such as icon, tap action, and title.
            .build()

    // ...
}
```

## Manifest declarations and permissions


Data sources must include specific declarations in their app manifest to be treated as
a data source by the Android system. This section explains the required settings for
data sources.


In your app's manifest, declare the service and add an update request action intent filter.
The manifest must also protect the service by adding the `BIND_COMPLICATION_PROVIDER`
permission to ensure that only the Wear OS system can bind to provider services.


Also, include an `android:icon` attribute in the
`service` element that provides a
single-color white icon. We recommend vector drawables for the icons.
The icon represents the data source and is shown in the complication picker.


Here's an example:

```xml
<service
    android:name=".snippets.complication.MyComplicationDataSourceService"
    android:exported="true"
    android:label="@string/my_complication_service_label"
    android:icon="@drawable/complication_icon"
    android:permission="com.google.android.wearable.permission.BIND_COMPLICATION_PROVIDER">
    <intent-filter>
        <action android:name="android.support.wearable.complications.ACTION_COMPLICATION_UPDATE_REQUEST" />
    </intent-filter>

    <!-- Supported types should be comma-separated, for example: "SHORT_TEXT,SMALL_IMAGE" -->
    <meta-data
        android:name="android.support.wearable.complications.SUPPORTED_TYPES"
        android:value="SHORT_TEXT" />
    <meta-data
        android:name="android.support.wearable.complications.UPDATE_PERIOD_SECONDS"
        android:value="300" />

    <!-- Optionally, specify a configuration activity, where the user can configure your complication. -->
    <meta-data
        android:name="android.support.wearable.complications.PROVIDER_CONFIG_ACTION"
        android:value="MY_CONFIG_ACTION" />

</service>
```

### Metadata elements


In your manifest file, notice the following metadata elements:

- `android:name="android.support.wearable.complications.SUPPORTED_TYPES"`: Specifies the types of complication data that the data source supports.
- `android:name="android.support.wearable.complications.UPDATE_PERIOD_SECONDS"`: Specifies how often the system should check for updates to the data.


When your complication data data source is active,
`UPDATE_PERIOD_SECONDS` specifies how often you want the
system to check for updates to the data. If the information shown in the
complication doesn't need to update on a regular schedule, such as when
you're [using push updates](https://developer.android.com/training/wearables/complications/exposing-data#push-updates), set this value to
`0`.


If you don't set `UPDATE_PERIOD_SECONDS` to `0`,
you must use a value of at least `300` (5 minutes), which is
the minimum update period that the system enforces, to preserve
device battery life. In addition, keep in mind that update requests
come less often when the device is in ambient mode or isn't being worn.

### Add a configuration activity


If required, a data source can include a configuration activity that is
shown to the user when the user chooses that particularly data source from the
complication picker. For example, a world clock data source might have a configuration
activity that allows the user to choose the city or time zone to display.


The example manifest includes a `meta-data` element with the
`PROVIDER_CONFIG_ACTION` key. The value of this element is the action that is used
to launch the configuration activity.


Create the configuration activity, and add an intent filter that matches the action for it in
your manifest file.

```xml
<intent-filter>
    <action android:name="MY_CONFIG_ACTION" />
    <category android:name="android.support.wearable.complications.category.PROVIDER_CONFIG" />
    <category android:name="android.intent.category.DEFAULT" />
</intent-filter>
```


The activity can obtain details of the complication slot it is configuring from the intent
within the `onCreate()` method of the activity:

```kotlin
// Keys defined on ComplicationDataSourceService
val id = intent.getIntExtra(EXTRA_CONFIG_COMPLICATION_ID, -1)
val type = intent.getIntExtra(EXTRA_CONFIG_COMPLICATION_TYPE, -1)
val source = intent.getStringExtra(EXTRA_CONFIG_DATA_SOURCE_COMPONENT)
```

The configuration activity must reside in the same package as the
provider. The configuration activity must return `RESULT_OK` or
`RESULT_CANCELED` to tell the system whether the data source
should be set:

```kotlin
setResult(RESULT_OK) // Or RESULT_CANCELED to cancel configuration
finish()
```

## Use push updates


As an alternative to specifying an update interval in your app's manifest, you can use an instance of
[`ComplicationDataSourceUpdateRequester`](https://developer.android.com/reference/androidx/wear/watchface/complications/datasource/ComplicationDataSourceUpdateRequester) to initiate updates dynamically.
To request an update, call `requestUpdate()`.

**Caution:** To preserve device battery life,
don't call `requestUpdate()` from your instance of
`ComplicationDataSourceUpdateRequester` more often than every 5 minutes on
average.

## Provide time-dependent values


Some complications need to display a value that relates to the current
time. Examples include the current date, the time until the next meeting,
or the time in another time zone.


Don't update a complication every
second or minute to keep those values up to date. Instead, specify
the values as relative to the current date or time using time-dependent text. The following
classes allow you to create these time-dependent values:

- [`TimeFormatComplicationText`](https://developer.android.com/reference/androidx/wear/watchface/complications/data/TimeFormatComplicationText) - formats a date or time value.
- [`TimeDifferenceComplicationText`](https://developer.android.com/reference/androidx/wear/watchface/complications/data/TimeDifferenceComplicationText) - counts up or down to a specified time.

## Timeline data


For complication data sources that provide a sequence of values at pre-defined times, use
[`SuspendingTimelineComplicationDataSourceService`](https://developer.android.com/reference/androidx/wear/watchface/complications/datasource/SuspendingTimelineComplicationDataSourceService).


An example of this would be a "next event" data source from a calendar app:
Instead of the system having to poll the data source regularly for the next
event, the data source can provide a timeline of events once, and then the
data source can initiate updates if the calendar changes. This minimizes the
load on the system and lets the complication show the correct event in a
timely manner:

```kotlin
class MyTimelineComplicationDataSourceService : SuspendingTimelineComplicationDataSourceService() {
    override suspend fun onComplicationRequest(request: ComplicationRequest): ComplicationDataTimeline? {
        if (request.complicationType != ComplicationType.SHORT_TEXT) {
            return ComplicationDataTimeline(
                defaultComplicationData = NoDataComplicationData(),
                timelineEntries = emptyList()
            )
        }
        // Retrieve list of events from your own datasource / database.
        val events = getCalendarEvents()
        return ComplicationDataTimeline(
            defaultComplicationData = shortTextComplicationData("No event"),
            timelineEntries = events.map {
                TimelineEntry(
                    validity = TimeInterval(it.start, it.end),
                    complicationData = shortTextComplicationData(it.name)
                )
            }
        )
    }

    override fun getPreviewData(type: ComplicationType): ComplicationData? {
        return shortTextComplicationData("Event 1")
    }

    private fun shortTextComplicationData(text: String) =
        ShortTextComplicationData.Builder(
            text = PlainComplicationText.Builder(text).build(),
            contentDescription = PlainComplicationText.Builder(text).build()
        )
            // Add further optional details here such as icon, tap action, title etc
            .build()

    // ...
}
```


The behavior of the `SuspendingTimelineComplicationDataSourceService` is as follows:

- When the current time falls within the start and end time of an entry in the timeline, the watch face uses that value.
- When the current time doesn't fall within any entry in the timeline, the default value is used. For example, in the calendar app, this could be "No event."
- If the current time falls within multiple events, the shortest event is used.

<br />

## Provide dynamic values


Starting in Wear OS 4, some complications can display values that refresh more frequently
based on values that are available directly to the platform. To provide this capability in
your complications, use
[`ComplicationData`](https://developer.android.com/reference/androidx/wear/watchface/complications/data/ComplicationData) fields that accept
[dynamic values](https://developer.android.com/training/wearables/data/dynamic). The platform evaluates and
updates these values frequently, without requiring the complication provider to be running.


Example fields include
[`GoalProgressComplicationData`'s dynamic value field](https://developer.android.com/reference/androidx/wear/watchface/complications/data/GoalProgressComplicationData#getDynamicValue()), and
[`DynamicComplicationText`](https://developer.android.com/reference/androidx/wear/watchface/complications/data/DynamicComplicationText), which can be used in any
[`ComplicationText`](https://developer.android.com/reference/androidx/wear/watchface/complications/data/ComplicationText) field. These dynamic values are based on the
[`androidx.wear.protolayout.expression`](https://developer.android.com/reference/androidx/wear/protolayout/expression/package-summary) library.


In certain situations, the platform cannot evaluate dynamic values:

- **Dynamic value is sometimes not available:** This happens, for example, when the device is off-wrist. In these situations, the platform uses the value of the [dynamic value invalidation fallback field](https://developer.android.com/reference/androidx/wear/watchface/complications/data/ComplicationData#getDynamicValueInvalidationFallback()) instead, in a [`NoDataComplicationData`'s placeholder field](https://developer.android.com/reference/androidx/wear/watchface/complications/data/NoDataComplicationData#getPlaceholder()).
- **Dynamic value is never available:** This happens on a device that is running on an older release of Wear OS 4. In this situation, the platform uses a companion fallback field, such as `https://developer.android.com/reference/androidx/wear/watchface/complications/data/DynamicComplicationText#getFallbackValue()()`.

## Related resources

- [Types and fields](https://developer.android.com/training/wearables/watch-faces/adding-complications#types-fields)
- [Wear OS samples repository](https://github.com/android/wear-os-samples)