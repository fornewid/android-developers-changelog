---
title: https://developer.android.com/training/wearables/wff/weather
url: https://developer.android.com/training/wearables/wff/weather
source: md.txt
---

Since version 2, the Watch Face Format includes support for weather data.
This data covers a range of metrics and timeframes, from the current conditions
to hourly and daily forecasts.

Weather is accessed using *expressions* . For example, to show the current
weather conditions in a [`<Text>`](https://developer.android.com/training/wearables/wff/group/part/text/text) element, use an expression similar to
the following:

<br />

```xml
<PartText x="100" y="100" width="200" height="50">
    <Text>
        <Font family="SYNC_TO_DEVICE" size="16">
            <Template><![CDATA[Today's weather: %s]]>
                <Parameter expression="[WEATHER.CONDITION_NAME]"/>
            </Template>
        </Font>
    </Text>
</PartText>
```

<br />

## Availability

Before you access other members of the `[WEATHER.*]` object, check the
`[WEATHER.IS_AVAILABLE]` value:

<br />

```xml
<Condition>
    <Expressions>
        <Expression name="is_weather_available">[WEATHER.IS_AVAILABLE]</Expression>
    </Expressions>
    <Compare expression="is_weather_available">
        <!-- Weather is available, so show the weather data. -->
    </Compare>
    <Default>
        <!-- Weather isn't available, so show an appropriate message. -->
    </Default>
</Condition>
```

<br />

You should also check for `[WEATHER.IS_ERROR]`, which indicates an error in
loading weather data.

Note that `[WEATHER.IS_AVAILABLE]` and `[WEATHER.IS_ERROR]` can both be true,
where the data is stale and attempts to refresh the data failed. In such cases,
the available weather can be shown, along with an indicator to show that there
was an error in fetching new data.

## Freshness of data

The timestamp of the available data can be accessed using
`[WEATHER.LAST_UPDATED]` which is a Unix epoch timestamp in milliseconds.

This value can be formatted using the [`icuText(,)`](https://developer.android.com/training/wearables/wff/common/attributes/arithmetic-expression#functions) method to obtain a
human-readable representation, as demonstrated in the [weather sample](https://github.com/android/wear-os-samples/tree/main/WatchFaceFormat/Weather).

## Weather conditions

The current conditions are available in `[WEATHER.CONDITION]`, with a
human-readable version in `[WEATHER.CONDITION_NAME]`.

The values for `[WEATHER.CONDITION]` can be seen in [data sources](https://developer.android.com/training/wearables/wff/common/attributes/source-type). For
example, `4` represents `HEAVY_RAIN`.

> [!NOTE]
> **Note:** If the watch face represents the current conditions, we strongly recommend you handle **all** potential values in the `[WEATHER.CONDITION]` enumeration.

## Other metrics

Watch Face Format provides a range of additional metrics, such as
`[WEATHER.TEMPERATURE]` and `[WEATHER.UV_INDEX]`. For the full details
of available metrics, including units and data types, visit the
[data sources](https://developer.android.com/training/wearables/wff/common/attributes/source-type) reference page.

## Hourly and daily forecasts

You can access forecast conditions for a specific hour or day in the future
as follows:

- `[WEATHER.HOURS.1.CONDITION]` - the forecast conditions 1 hour from now.
- `[WEATHER.DAYS.2.CONDITION]` - the forecast conditions 2 days from now.

Hourly data can be available up to 8 hours ahead, and daily data up to 5 days
ahead. However, the watch face should always check for the availability of
forecast data. A different range of hours or days might be available at
different times, or different devices. For example, to check whether forecast
data is available for 1 hour from now, use `[WEATHER.HOURS.1.IS_AVAILABLE]`.

> [!NOTE]
> **Note:** If your watch face renders a `CONDITION` for forecast data, we strongly recommend that you handle **all** potential values in the `CONDITION` enumeration.

Daily and hourly forecasts also feature a range of metrics, such as
`[WEATHER.HOURS.<N>.TEMPERATURE]` and
`[WEATHER.DAYS.<N>.CHANCE_OF_PRECIPITATION]`. For the full details
of available metrics, including units and data types, visit the
[data sources](https://developer.android.com/training/wearables/wff/common/attributes/source-type) reference page.

## Testing with weather data

To obtain weather data, the Wear OS device must be aware of the device location.

To conserve power, the watch doesn't use the onboard GPS sensor to
determine a location for the weather forecast, and instead relies on location
from a connected handheld device or from available networks.

To make location data available for testing, do one of the following:

- [Pair your Wear OS emulator](https://developer.android.com/training/wearables/get-started/connect-phone) with a physical or emulator phone.
- Simulate location through the following adb command:

    adb unroot
    adb shell cmd location set-location-enabled true
    adb root
    adb shell appops set 0 android:mock_location allow
    adb shell cmd location providers add-test-provider gps
    adb shell cmd location providers set-test-provider-enabled gps true
    adb shell cmd location providers set-test-provider-location gps --location 37.773972,-122.431297

## Further details

For a complete example of accessing and rendering weather data, see the
[GitHub sample](https://github.com/android/wear-os-samples/tree/main/WatchFaceFormat/Weather).

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Change focus behavior](https://developer.android.com/develop/ui/compose/touch-input/focus/change-focus-behavior)
- [Side-effects in Compose](https://developer.android.com/develop/ui/compose/side-effects)
- [AGSL Quick Reference](https://developer.android.com/develop/ui/views/graphics/agsl/agsl-quick-reference)