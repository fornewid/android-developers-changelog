---
title: https://developer.android.com/develop/ui/views/appwidgets/layouts
url: https://developer.android.com/develop/ui/views/appwidgets/layouts
source: md.txt
---

Try the Compose way  
Jetpack Compose is the recommended UI toolkit for Android. Learn how to build widgets using Compose-style APIs.  
[Jetpack Glance →](https://developer.android.com/develop/ui/compose/glance/build-ui#define-sizemode)  
![](https://developer.android.com/static/images/android-compose-ui-logo.png)

<br />

This page describes refinements for widget sizing and greater flexibility
introduced in Android 12 (API level 31). It also details how to
[determine a size for your widget](https://developer.android.com/develop/ui/views/appwidgets/layouts#anatomy_determining_size).

## Use improved APIs for widget sizes and layouts

Starting with Android 12 (API level 31), you can provide more refined size
attributes and flexible layouts by doing the following, as described in the
sections that follow:

1. [Specify additional widget sizing constraints.](https://developer.android.com/develop/ui/views/appwidgets/layouts#specify-widget-size-constraints)

2. Providing [responsive layouts](https://developer.android.com/develop/ui/views/appwidgets/layouts#provide-responsive-layouts) or [exact
   layouts.](https://developer.android.com/develop/ui/views/appwidgets/layouts#provide-exact-layouts)

In previous versions of Android, it is possible to get the size ranges of a
widget using the
[`OPTION_APPWIDGET_MIN_WIDTH`](https://developer.android.com/reference/android/appwidget/AppWidgetManager#OPTION_APPWIDGET_MIN_WIDTH),
[`OPTION_APPWIDGET_MIN_HEIGHT`](https://developer.android.com/reference/android/appwidget/AppWidgetManager#OPTION_APPWIDGET_MIN_HEIGHT),
[`OPTION_APPWIDGET_MAX_WIDTH`](https://developer.android.com/reference/android/appwidget/AppWidgetManager#OPTION_APPWIDGET_MAX_WIDTH),
and [`OPTION_APPWIDGET_MAX_HEIGHT`](https://developer.android.com/reference/android/appwidget/AppWidgetManager#OPTION_APPWIDGET_MAX_HEIGHT)
extras and then estimate the widget's size, but that logic doesn't work in all
situations. For widgets targeting Android 12 or higher, we recommend
providing [responsive](https://developer.android.com/develop/ui/views/appwidgets/layouts#provide-responsive-layouts) or [exact
layouts](https://developer.android.com/develop/ui/views/appwidgets/layouts#provide-exact-layouts).

### Specify additional widget sizing constraints

Android 12 adds APIs letting you ensure your widget is
sized more reliably across different devices with varying screen sizes.

In addition to the existing [`minWidth`](https://developer.android.com/reference/android/appwidget/AppWidgetProviderInfo#minWidth),
[`minHeight`](https://developer.android.com/reference/android/appwidget/AppWidgetProviderInfo#minHeight),
[`minResizeWidth`](https://developer.android.com/reference/android/appwidget/AppWidgetProviderInfo#minResizeWidth),
and [`minResizeHeight`](https://developer.android.com/reference/android/appwidget/AppWidgetProviderInfo#minResizeHeight)
attributes, use the following new `appwidget-provider` attributes:

- [`targetCellWidth`](https://developer.android.com/reference/android/appwidget/AppWidgetProviderInfo#targetCellWidth)
  and [`targetCellHeight`](https://developer.android.com/reference/android/appwidget/AppWidgetProviderInfo#targetCellHeight):
  define the target size of the widget in terms of launcher grid cells. If
  defined, these attributes are used instead of `minWidth` or `minHeight`.

- [`maxResizeWidth`](https://developer.android.com/reference/android/appwidget/AppWidgetProviderInfo#maxResizeWidth)
  and [`maxResizeHeight`](https://developer.android.com/reference/android/appwidget/AppWidgetProviderInfo#maxResizeHeight):
  define the maximum size that the launcher allows the user to resize the widget to.

The following XML shows how to use the sizing attributes.  

    <appwidget-provider
      ...
      android:targetCellWidth="3"
      android:targetCellHeight="2"
      android:maxResizeWidth="250dp"
      android:maxResizeHeight="110dp">
    </appwidget-provider>

### Provide responsive layouts

If the layout needs to change depending on the size of the widget, we recommend
creating a small set of layouts, each valid for a range of sizes. If this
isn't possible, another option is to provide layouts based on the [exact widget
size at runtime](https://developer.android.com/develop/ui/views/appwidgets/layouts#provide-exact-layouts), as described in this page.

This feature allows for smoother scaling and overall better system
health, because the system doesn't have to wake up the app every time
it displays the widget in a different size.

The following code example shows how to provide a list of layouts.  

### Kotlin

```kotlin
override fun onUpdate(...) {
    val smallView = ...
    val tallView = ...
    val wideView = ...

    val viewMapping: Map<SizeF, RemoteViews> = mapOf(
            SizeF(150f, 100f) to smallView,
            SizeF(150f, 200f) to tallView,
            SizeF(215f, 100f) to wideView
    )
    val remoteViews = RemoteViews(viewMapping)

    appWidgetManager.updateAppWidget(id, remoteViews)
}
```

### Java

```java
@Override
public void onUpdate(...) {
    RemoteViews smallView = ...;
    RemoteViews tallView = ...;
    RemoteViews wideView = ...;

    Map<SizeF, RemoteViews> viewMapping = new ArrayMap<>();
    viewMapping.put(new SizeF(150f, 100f), smallView);
    viewMapping.put(new SizeF(150f, 200f), tallView);
    viewMapping.put(new SizeF(215f, 100f), wideView);
    RemoteViews remoteViews = new RemoteViews(viewMapping);

    appWidgetManager.updateAppWidget(id, remoteViews);
}
```

Assume the widget has the following attributes:  

    <appwidget-provider
        android:minResizeWidth="160dp"
        android:minResizeHeight="110dp"
        android:maxResizeWidth="250dp"
        android:maxResizeHeight="200dp">
    </appwidget-provider>

The preceding code snippet means the following:

- `smallView` supports from 160dp (`minResizeWidth`) × 110dp (`minResizeHeight`) to 160dp × 199dp (next cutoff point - 1dp).
- `tallView` supports from 160dp × 200dp to 214dp (next cutoff point - 1) × 200dp.
- `wideView` supports from 215dp × 110dp (`minResizeHeight`) to 250dp
  (`maxResizeWidth`) × 200dp (`maxResizeHeight`).

  | **Note:** It's possible for the widget's size to be larger than `maxResizeWidth` × `maxResizeHeight`. See [Widget sizing
  | attributes](https://developer.android.com/guide/topics/appwidgets#widget-sizing-attributes) for more details.

Your widget must support the size range from `minResizeWidth` ×
`minResizeHeight` to `maxResizeWidth` × `maxResizeHeight`. Within that range,
you can decide the cutoff point to switch layouts.
![Example of responsive layout](https://developer.android.com/static/images/appwidgets/size-range.gif) **Figure 1.**Example of a responsive layout.

### Provide exact layouts

If a small set of responsive layouts isn't feasible, you can instead provide
different layouts tailored to the sizes at which the widget is shown. This is
typically two sizes for phones (portrait and landscape mode) and four sizes for
foldables.

To implement this solution, your app needs to perform the following steps:

1. Overload [`AppWidgetProvider.onAppWidgetOptionsChanged()`](https://developer.android.com/reference/android/appwidget/AppWidgetProvider#onAppWidgetOptionsChanged(android.content.Context,%20android.appwidget.AppWidgetManager,%20int,%20android.os.Bundle)),
   which is called when the set of sizes changes.

2. Call [`AppWidgetManager.getAppWidgetOptions()`](https://developer.android.com/reference/android/appwidget/AppWidgetManager#getAppWidgetOptions(int)),
   which returns a [`Bundle`](https://developer.android.com/reference/android/os/Bundle) containing the sizes.

3. Access the [`AppWidgetManager.OPTION_APPWIDGET_SIZES`](https://developer.android.com/reference/android/appwidget/AppWidgetManager#OPTION_APPWIDGET_SIZES) key from the `Bundle`.

| **Note:** Providing the list of sizes is the launcher's responsibility. If the device has a launcher that doesn't support that field, the list of sizes might be empty or null.

The following code example shows how to provide exact layouts.  

### Kotlin

```kotlin
override fun onAppWidgetOptionsChanged(
        context: Context,
        appWidgetManager: AppWidgetManager,
        id: Int,
        newOptions: Bundle?
) {
    super.onAppWidgetOptionsChanged(context, appWidgetManager, id, newOptions)
    // Get the new sizes.
    val sizes = newOptions?.getParcelableArrayList<SizeF>(
            AppWidgetManager.OPTION_APPWIDGET_SIZES
    )
    // Check that the list of sizes is provided by the launcher.
    if (sizes.isNullOrEmpty()) {
        return
    }
    // Map the sizes to the RemoteViews that you want.
    val remoteViews = RemoteViews(sizes.associateWith(::createRemoteViews))
    appWidgetManager.updateAppWidget(id, remoteViews)
}

// Create the RemoteViews for the given size.
private fun createRemoteViews(size: SizeF): RemoteViews { }
```

### Java

```java
@Override
public void onAppWidgetOptionsChanged(
    Context context, AppWidgetManager appWidgetManager, int appWidgetId, Bundle newOptions) {
    super.onAppWidgetOptionsChanged(context, appWidgetManager, appWidgetId, newOptions);
    // Get the new sizes.
    ArrayList<SizeF> sizes =
        newOptions.getParcelableArrayList(AppWidgetManager.OPTION_APPWIDGET_SIZES);
    // Check that the list of sizes is provided by the launcher.
    if (sizes == null || sizes.isEmpty()) {
      return;
    }
    // Map the sizes to the RemoteViews that you want.
    Map<SizeF, RemoteViews> viewMapping = new ArrayMap<>();
    for (SizeF size : sizes) {
        viewMapping.put(size, createRemoteViews(size));
    }
    RemoteViews remoteViews = new RemoteViews(viewMapping);
    appWidgetManager.updateAppWidget(id, remoteViews);
}

// Create the RemoteViews for the given size.
private RemoteViews createRemoteViews(SizeF size) { }
```

## Determine a size for your widget

Each widget must define a `targetCellWidth` and `targetCellHeight` for devices
running Android 12 or higher---or `minWidth` and `minHeight` for all
versions of Android---indicating the minimum amount of space it consumes
by default. However, when users add a widget to their home screen, it generally
occupies more than the minimum width and height you specify.

Android home screens offer users a grid of available spaces onto which they can
place widgets and icons. This grid can vary by device; for example, many
handsets offer a 5x4 grid, and tablets can offer a larger grid. When your widget
is added, it is stretched to occupy the minimum number of cells,
horizontally and vertically, required to satisfy constraints for its
`targetCellWidth` and `targetCellHeight` on devices running
Android 12 or higher, or `minWidth` and `minHeight` constraints on
devices running Android 11 (API level 30) or lower.

Both the width and height of a cell and the size of the automatic margins applied
to widgets can vary across devices. Use the following table to roughly estimate
your widget's minimum dimensions in a typical 5x4 grid handset, given the
number of occupied grid cells you want:

| Number of cells (width x height) | Available size in portrait mode (dp) | Available size in landscape mode (dp) |
|---|---|---|
| 1x1 | 57x102dp | 127x51dp |
| 2x1 | 130x102dp | 269x51dp |
| 3x1 | 203x102dp | 412x51dp |
| 4x1 | 276x102dp | 554x51dp |
| 5x1 | 349x102dp | 697x51dp |
| 5x2 | 349x220dp | 697x117dp |
| 5x3 | 349x337dp | 697x184dp |
| 5x4 | 349x455dp | 697x250dp |
| ... | ... | ... |
| n x m | (73n - 16) x (118m - 16) | (142n - 15) x (66m - 15) |

| **Note:** The preceding table shows the available sizes on a Google Pixel 4 to demonstrate the rough estimation of general available sizes in both portrait and landscape modes.

Use the portrait mode cell sizes to inform the values you provide for
the `minWidth`, `minResizeWidth`, and `maxResizeWidth` attributes. Similarly,
use the landscape mode cell sizes to inform the values you provide
for the `minHeight`, `minResizeHeight`, and `maxResizeHeight` attributes.

The reason for this is that the cell width is typically smaller in portrait mode
than in landscape mode---and, similarly, the cell height is typically
smaller in landscape mode than in portrait mode.

For example, if you want your widget width to be resizable down to one cell on
a Google Pixel 4, you need to set your `minResizeWidth` to at most 56dp
to make sure the value for the `minResizeWidth` attribute is smaller
than 57dp---because a cell is at least 57dp wide in portrait.
Similarly, if you want your widget height to be resizable in one cell on the
same device, you need to set your `minResizeHeight` to at most 50dp to make sure
the value for the `minResizeHeight` attribute is smaller than
51dp---because one cell is at least 51dp high in landscape mode.

Each widget is resizable within the size ranges between the
`minResizeWidth`/`minResizeHeight` and `maxResizeWidth`/`maxResizeHeight`
attributes, which means it needs to adapt to any size ranges between them.
| **Note:** As mentioned previously, it's possible for the widget's size to be larger than `maxResizeWidth` x `maxResizeHeight`. See [Widget sizing
| attributes](https://developer.android.com/guide/topics/appwidgets#widget-sizing-attributes) for more details.

For example, to set the default size of the widget on placement, you can
set the following attributes:  

    <appwidget-provider
        android:targetCellWidth="3"
        android:targetCellHeight="2"
        android:minWidth="180dp"
        android:minHeight="110dp">
    </appwidget-provider>

This means the widget's default size is 3x2 cells, as specified by the
`targetCellWidth` and `targetCellHeight` attributes---or 180×110dp, as
specified by `minWidth` and `minHeight` for devices running
Android 11 or lower. In the latter case, the size in cells can
vary depending on the device.

Also, to set the supported size ranges of your widget, you can set the following
attributes:  

    <appwidget-provider
        android:minResizeWidth="180dp"
        android:minResizeHeight="110dp"
        android:maxResizeWidth="530dp"
        android:maxResizeHeight="450dp">
    </appwidget-provider>

As specified by the preceding attributes, the width of the widget is
resizable from 180dp to 530dp, and its height is resizable from 110dp to 450dp.
The widget is then resizable from 3x2 to 5x2 cells, as long as the following
conditions are present:

- The device has the 5x4 grid.
- The mapping between the number of cells and the available size in dps follows the [table showing estimation of minimum
  dimensions](https://developer.android.com/develop/ui/views/appwidgets/layouts#estimate-minimum-dimensions) in this page.
- The widget adapts to that size range.

### Kotlin

```kotlin
val smallView = RemoteViews(context.packageName, R.layout.widget_weather_forecast_small)
val mediumView = RemoteViews(context.packageName, R.layout.widget_weather_forecast_medium)
val largeView = RemoteViews(context.packageName, R.layout.widget_weather_forecast_large)

val viewMapping: Map<SizeF, RemoteViews> = mapOf(
        SizeF(180f, 110f) to smallView,
        SizeF(270f, 110f) to mediumView,
        SizeF(270f, 280f) to largeView
)

appWidgetManager.updateAppWidget(appWidgetId, RemoteViews(viewMapping))
```

### Java

```java
RemoteViews smallView = 
    new RemoteViews(context.getPackageName(), R.layout.widget_weather_forecast_small);
RemoteViews mediumView = 
    new RemoteViews(context.getPackageName(), R.layout.widget_weather_forecast_medium);
RemoteViews largeView = 
    new RemoteViews(context.getPackageName(), R.layout.widget_weather_forecast_large);

Map<SizeF, RemoteViews> viewMapping = new ArrayMap<>();
viewMapping.put(new SizeF(180f, 110f), smallView);
viewMapping.put(new SizeF(270f, 110f), mediumView);
viewMapping.put(new SizeF(270f, 280f), largeView);
RemoteViews remoteViews = new RemoteViews(viewMapping);

appWidgetManager.updateAppWidget(id, remoteViews);
```

Assume the widget uses the responsive layouts defined in the preceding
code snippets. This means the layout specified as
`R.layout.widget_weather_forecast_small` is used from 180dp (`minResizeWidth`) x
110dp (`minResizeHeight`) to 269x279dp (next cutoff points - 1). Similarly,
`R.layout.widget_weather_forecast_medium` is used from 270x110dp to 270x279dp,
and `R.layout.widget_weather_forecast_large` is used from 270x280dp to
530dp (`maxResizeWidth`) x 450dp (`maxResizeHeight`).

As the user resizes the widget, its appearance changes to adapt to each size in
cells, as shown in the following examples.
![Example weather widget in the smallest 3x2-grid size. The UI shows
the location name (Tokyo), temperature (14°), and symbol indicating
partially cloudy weather.](https://developer.android.com/static/images/appwidgets/weather-size-3x2.png) **Figure 2.** 3x2 `R.layout.widget_weather_forecast_small`.

<br />

![Example weather widget in a 4x2 'medium' size. Resizing the widget
this way builds on all of the UI from the previous widget size,
and adds the label 'Mostly cloudy' and a forecast of temperatures from
4pm through 7pm.](https://developer.android.com/static/images/appwidgets/weather-size-4x2.png) **Figure 3.** 4x2 `R.layout.widget_weather_forecast_medium`.

<br />

![Example weather widget in a 5x2 'medium' size. Resizing the widget
this way results in the same UI as the previous size, except it is
stretched by one cell length to take up more horizontal space.](https://developer.android.com/static/images/appwidgets/weather-size-5x2.png) **Figure 4.** 5x2 `R.layout.widget_weather_forecast_medium`.

<br />

![Example weather widget in a 5x3 'large' size. Resizing the widget
this way builds on all of the UI from the previous widget sizes,
and adds a view inside the widget containing a forecast of the weather
on Tuesday and Wednesday. Symbols indicating sunny or rainy weather
and high and low temperatures for each day.](https://developer.android.com/static/images/appwidgets/weather-size-5x3.png) **Figure 5.** 5x3 `R.layout.widget_weather_forecast_large`.

<br />

![Example weather widget in a 5x4 'large' size. Resizing the widget
this way builds on all of the UI from the previous widget sizes,
and adds Thursday and Friday (and their corresponding symbols
indicating the type of weather as well as high and low temperature
for each day).](https://developer.android.com/static/images/appwidgets/weather-size-5x4.png) **Figure 6.** 5x4 `R.layout.widget_weather_forecast_large`.