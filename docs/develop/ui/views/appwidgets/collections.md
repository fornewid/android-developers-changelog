---
title: https://developer.android.com/develop/ui/views/appwidgets/collections
url: https://developer.android.com/develop/ui/views/appwidgets/collections
source: md.txt
---

Try the Compose way  
Jetpack Compose is the recommended UI toolkit for Android. Learn how to build widgets using Compose-style APIs.  
[Jetpack Glance →](https://developer.android.com/develop/ui/compose/glance/build-ui#use-scrollable)  
![](https://developer.android.com/static/images/android-compose-ui-logo.png)

<br />

Collection widgets specialize in displaying many elements of the same type, such
as collections of pictures from a gallery app, articles from a news app, or
messages from a communication app. Collection widgets typically focus on two use
cases: browsing the collection and opening an element of the collection to its
detail view. Collection widgets can scroll vertically.

These widgets use the
[`RemoteViewsService`](https://developer.android.com/reference/android/widget/RemoteViewsService) to display
collections that are backed by remote data, such as from a [content
provider](https://developer.android.com/guide/topics/providers/content-providers). The widget presents the
data using one of the following view types, which are known as *collection
views*:

[`ListView`](https://developer.android.com/reference/android/widget/ListView)
:   A view that shows items in a
    vertically scrolling list.

[`GridView`](https://developer.android.com/reference/android/widget/GridView)
:   A view that shows items in a
    two-dimensional scrolling grid.

[`StackView`](https://developer.android.com/reference/android/widget/StackView)
:   A stacked card
    view---kind of like a rolodex---where the user can flick the front
    card up or down to see the previous or next card, respectively.

[`AdapterViewFlipper`](https://developer.android.com/reference/android/widget/AdapterViewFlipper)
:   An
    adapter-backed simple
    [`ViewAnimator`](https://developer.android.com/reference/android/widget/ViewAnimator) that animates
    between two or more views. Only one child is shown at a time.

Because these collection views display collections backed by remote data, they
use an [`Adapter`](https://developer.android.com/reference/android/widget/Adapter) to bind their user
interface to their data. An `Adapter` binds individual items from a set of data
to individual [`View`](https://developer.android.com/reference/android/view/View) objects.

And because these collection views are backed by adapters, the Android framework
must include extra architecture to support their use in widgets. In the context
of a widget, the `Adapter` is replaced by a
[`RemoteViewsFactory`](https://developer.android.com/reference/android/widget/RemoteViewsService.RemoteViewsFactory),
which is a thin wrapper around the `Adapter` interface. When requested for a
specific item in the collection, the `RemoteViewsFactory` creates and returns
the item for the collection as a
[`RemoteViews`](https://developer.android.com/reference/android/widget/RemoteViews) object. To include a
collection view in your widget, implement `RemoteViewsService` and
`RemoteViewsFactory`.

`RemoteViewsService` is a service that lets a remote adapter request
`RemoteViews` objects. `RemoteViewsFactory` is an interface for an adapter
between a collection view---such as `ListView`, `GridView`, and
`StackView`---and the underlying data for that view. From the [`StackWidget`
sample](https://android.googlesource.com/platform/development/+/master/samples/StackWidget/src/com/example/android/stackwidget/StackWidgetService.java),
here is an example of the boilerplate code to implement this service and
interface:  

### Kotlin

```kotlin
class StackWidgetService : RemoteViewsService() {

    override fun onGetViewFactory(intent: Intent): RemoteViewsFactory {
        return StackRemoteViewsFactory(this.applicationContext, intent)
    }
}

class StackRemoteViewsFactory(
        private val context: Context,
        intent: Intent
) : RemoteViewsService.RemoteViewsFactory {

// See the RemoteViewsFactory API reference for the full list of methods to
// implement.

}
```

### Java

```java
public class StackWidgetService extends RemoteViewsService {
    @Override
    public RemoteViewsFactory onGetViewFactory(Intent intent) {
        return new StackRemoteViewsFactory(this.getApplicationContext(), intent);
    }
}

class StackRemoteViewsFactory implements RemoteViewsService.RemoteViewsFactory {

// See the RemoteViewsFactory API reference for the full list of methods to
// implement.

}
```

## Sample application

The code excerpts in this section are also drawn from the [`StackWidget`
sample](https://android.googlesource.com/platform/development/+/master/samples/StackWidget):
![](https://developer.android.com/static/images/appwidgets/StackWidget.png) **Figure 1.** A `StackWidget`.

This sample consists of a stack of ten views that display the values zero
through nine. The sample widget has these primary behaviors:

- The user can vertically fling the top view in the widget to display the next
  or previous view. This is a built-in `StackView` behavior.

- Without any user interaction, the widget automatically advances through its
  views in sequence, like a slideshow. This is due to the setting
  `android:autoAdvanceViewId="@id/stack_view"` in the
  `res/xml/stackwidgetinfo.xml` file. This setting applies to the view ID,
  which in this case is the view ID of the stack view.

- If the user touches the top view, the widget displays the
  [`Toast`](https://developer.android.com/reference/android/widget/Toast) message "Touched view *n* ," where
  *n* is the index (position) of the touched view. For more discussion on how
  to implement behaviors, see the [Add behavior to individual
  items](https://developer.android.com/develop/ui/views/appwidgets/collections#behavior) section.

## Implement widgets with collections

To implement a widget with collections, follow the procedure to [implement any
widget](https://developer.android.com/develop/ui/views/appwidgets), followed by a few additional steps:
modify the manifest, add a collection view to the widget layout, and modify your
`AppWidgetProvider` subclass.

### Manifest for widgets with collections

Beyond the requirements listed in [Declare a widget in the
manifest](https://developer.android.com/guide/topics/appwidgets#Manifest), you need to make it possible for widgets with
collections to bind to your `RemoteViewsService`. Do this by declaring the
service in your manifest file with the permission
[`BIND_REMOTEVIEWS`](https://developer.android.com/reference/android/Manifest.permission#BIND_REMOTEVIEWS).
This prevents other applications from freely accessing your widget's data.

For example, when creating a widget that uses `RemoteViewsService` to populate a
collection view, the manifest entry might look like this:  

    <service android:name="MyWidgetService"
        android:permission="android.permission.BIND_REMOTEVIEWS" />

In this example, `android:name="MyWidgetService"` refers to your subclass of
`RemoteViewsService`.

### Layout for widgets with collections

The main requirement for your widget layout XML file is that it include one of
the collection views: `ListView`, `GridView`, `StackView`, or
`AdapterViewFlipper`. Here is the `widget_layout.xml` file for the
[`StackWidget`
sample](https://android.googlesource.com/platform/development/+/master/samples/StackWidget/res/layout):  

    <FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"
        android:layout_width="match_parent"
        android:layout_height="match_parent">
        <StackView
            android:id="@+id/stack_view"
            android:layout_width="match_parent"
            android:layout_height="match_parent"
            android:gravity="center"
            android:loopViews="true" />
        <TextView
            android:id="@+id/empty_view"
            android:layout_width="match_parent"
            android:layout_height="match_parent"
            android:gravity="center"
            android:background="@drawable/widget_item_background"
            android:textColor="#ffffff"
            android:textStyle="bold"
            android:text="@string/empty_view_text"
            android:textSize="20sp" />
    </FrameLayout>

Note that empty views must be siblings of the collection view for which the
empty view represents empty state.

In addition to the layout file for your entire widget, create another layout
file that defines the layout for each item in the collection---for example,
a layout for each book in a collection of books. The `StackWidget` sample has
only one item layout file, `widget_item.xml`, since all items use the same
layout.

### AppWidgetProvider class for widgets with collections

As with regular widgets, the bulk of the code in your
[`AppWidgetProvider`](https://developer.android.com/reference/android/appwidget/AppWidgetProvider) subclass
typically goes in
[`onUpdate()`](https://developer.android.com/reference/android/appwidget/AppWidgetProvider#onUpdate(android.content.Context,%20android.appwidget.AppWidgetManager,%20int%5B%5D)).
The major difference in your implementation for `onUpdate()` when creating a
widget with collections is that you must call
[`setRemoteAdapter()`](https://developer.android.com/reference/android/widget/RemoteViews#setRemoteAdapter(int,%0Aandroid.content.Intent)). This tells the collection view where to get its data.
The `RemoteViewsService` can then return your implementation of
`RemoteViewsFactory`, and the widget can serve up the appropriate data. When you
call this method, pass an intent that points to your implementation of
`RemoteViewsService` and the widget ID that specifies the widget to update.

For example, here's how the `StackWidget` sample implements the `onUpdate()`
callback method to set the `RemoteViewsService` as the remote adapter for the
widget collection:  

### Kotlin

```kotlin
override fun onUpdate(
        context: Context,
        appWidgetManager: AppWidgetManager,
        appWidgetIds: IntArray
) {
    // Update each of the widgets with the remote adapter.
    appWidgetIds.forEach { appWidgetId ->

        // Set up the intent that starts the StackViewService, which
        // provides the views for this collection.
        val intent = Intent(context, StackWidgetService::class.java).apply {
            // Add the widget ID to the intent extras.
            putExtra(AppWidgetManager.EXTRA_APPWIDGET_ID, appWidgetId)
            data = Uri.parse(toUri(Intent.URI_INTENT_SCHEME))
        }
        // Instantiate the RemoteViews object for the widget layout.
        val views = RemoteViews(context.packageName, R.layout.widget_layout).apply {
            // Set up the RemoteViews object to use a RemoteViews adapter.
            // This adapter connects to a RemoteViewsService through the
            // specified intent.
            // This is how you populate the data.
            setRemoteAdapter(R.id.stack_view, intent)

            // The empty view is displayed when the collection has no items.
            // It must be in the same layout used to instantiate the
            // RemoteViews object.
            setEmptyView(R.id.stack_view, R.id.empty_view)
        }

        // Do additional processing specific to this widget.

        appWidgetManager.updateAppWidget(appWidgetId, views)
    }
    super.onUpdate(context, appWidgetManager, appWidgetIds)
}
```

### Java

```java
public void onUpdate(Context context, AppWidgetManager appWidgetManager, int[] appWidgetIds) {
    // Update each of the widgets with the remote adapter.
    for (int i = 0; i < appWidgetIds.length; ++i) {

        // Set up the intent that starts the StackViewService, which
        // provides the views for this collection.
        Intent intent = new Intent(context, StackWidgetService.class);
        // Add the widget ID to the intent extras.
        intent.putExtra(AppWidgetManager.EXTRA_APPWIDGET_ID, appWidgetIds[i]);
        intent.setData(Uri.parse(intent.toUri(Intent.URI_INTENT_SCHEME)));
        // Instantiate the RemoteViews object for the widget layout.
        RemoteViews views = new RemoteViews(context.getPackageName(), R.layout.widget_layout);
        // Set up the RemoteViews object to use a RemoteViews adapter.
        // This adapter connects to a RemoteViewsService through the specified
        // intent.
        // This is how you populate the data.
        views.setRemoteAdapter(R.id.stack_view, intent);

        // The empty view is displayed when the collection has no items.
        // It must be in the same layout used to instantiate the RemoteViews
        // object.
        views.setEmptyView(R.id.stack_view, R.id.empty_view);

        // Do additional processing specific to this widget.

        appWidgetManager.updateAppWidget(appWidgetIds[i], views);
    }
    super.onUpdate(context, appWidgetManager, appWidgetIds);
}
```

## Persist data

As described on this page, the `RemoteViewsService` subclass provides
the `RemoteViewsFactory` used to populate the remote collection view.

Specifically, perform these steps:

1. Subclass `RemoteViewsService`. `RemoteViewsService` is the service through
   which a remote adapter can request `RemoteViews`.

2. In your `RemoteViewsService` subclass, include a class that implements the
   `RemoteViewsFactory` interface. `RemoteViewsFactory` is an interface for an
   adapter between a remote collection view---such as `ListView`,
   `GridView`, `StackView`---and the underlying data for that view. Your
   implementation is responsible for making a `RemoteViews` object for each
   item in the dataset. This interface is a thin wrapper around `Adapter`.

You can't rely on a single instance of your service, or any data it contains, to
persist. Don't store data in your `RemoteViewsService` unless it is static. If
you want your widget's data to persist, the best approach is to use a
[`ContentProvider`](https://developer.android.com/reference/android/content/ContentProvider) whose data
persists beyond the process lifecycle. For example, a grocery store widget can
store the state of each grocery list item in a persistent location, such as a
SQL database.
| **Note:** See [`WeatherDataProvider.java`](https://android.googlesource.com/platform/development/+/master/samples/WeatherListWidget/src/com/example/android/weatherlistwidget/WeatherDataProvider.java) for a code sample demonstrating how to persist a widget's underlying data using `ContentProvider`.

The primary contents of the `RemoteViewsService` implementation is its
`RemoteViewsFactory`, described in the following section.

### RemoteViewsFactory interface

Your custom class that implements the `RemoteViewsFactory` interface provides
the widget with the data for the items in its collection. To do this, it
combines your widget item XML layout file with a source of data. This source of
data can be anything from a database to a simple array. In the `StackWidget`
sample, the data source is an array of `WidgetItems`. The `RemoteViewsFactory`
functions as an adapter to glue the data to the remote collection view.

The two most important methods you need to implement for your
`RemoteViewsFactory` subclass are
[`onCreate()`](https://developer.android.com/reference/android/widget/RemoteViewsService.RemoteViewsFactory#o%0AnCreate()) and
[`getViewAt()`](https://developer.android.com/reference/android/widget/RemoteViewsService.RemoteViewsFactory#%0AgetViewAt(int)).

The system calls `onCreate()` when creating your factory for the first time.
This is where you set up any connections or cursors to your data source. For
example, the `StackWidget` sample uses `onCreate()` to initialize an array of
`WidgetItem` objects. When your widget is active, the system accesses these
objects using their index position in the array and displays the text they
contain.

Here is an excerpt from the `StackWidget` sample's `RemoteViewsFactory`
implementation that shows portions of the `onCreate()` method:  

### Kotlin

```kotlin
private const val REMOTE_VIEW_COUNT: Int = 10

class StackRemoteViewsFactory(
        private val context: Context
) : RemoteViewsService.RemoteViewsFactory {

    private lateinit var widgetItems: List<WidgetItem>

    override fun onCreate() {
        // In onCreate(), set up any connections or cursors to your data
        // source. Heavy lifting, such as downloading or creating content,
        // must be deferred to onDataSetChanged() or getViewAt(). Taking
        // more than 20 seconds on this call results in an ANR.
        widgetItems = List(REMOTE_VIEW_COUNT) { index -> WidgetItem("$index!") }
        ...
    }
    ...
}
```

### Java

```java
class StackRemoteViewsFactory implements RemoteViewsService.RemoteViewsFactory {
    private static final int REMOTE_VIEW_COUNT = 10;
    private List<WidgetItem> widgetItems = new ArrayList<WidgetItem>();

    public void onCreate() {
        // In onCreate(), setup any connections or cursors to your data
        // source. Heavy lifting, such as downloading or creating content,
        // must be deferred to onDataSetChanged() or getViewAt(). Taking
        // more than 20 seconds on this call results in an ANR.
        for (int i = 0; i < REMOTE_VIEW_COUNT; i++) {
            widgetItems.add(new WidgetItem(i + "!"));
        }
        ...
    }
...
```

The `RemoteViewsFactory` method `getViewAt()` returns a `RemoteViews` object
corresponding to the data at the specified `position` in the data set. Here is
an excerpt from the `StackWidget` sample's `RemoteViewsFactory` implementation:  

### Kotlin

```kotlin
override fun getViewAt(position: Int): RemoteViews {
    // Construct a remote views item based on the widget item XML file
    // and set the text based on the position.
    return RemoteViews(context.packageName, R.layout.widget_item).apply {
        setTextViewText(R.id.widget_item, widgetItems[position].text)
    }
}
```

### Java

```java
public RemoteViews getViewAt(int position) {
    // Construct a remote views item based on the widget item XML file
    // and set the text based on the position.
    RemoteViews views = new RemoteViews(context.getPackageName(), R.layout.widget_item);
    views.setTextViewText(R.id.widget_item, widgetItems.get(position).text);
    return views;
}
```

### Add behavior to individual items

The preceding sections show how to bind your data to your widget collection. But
what if you want to add dynamic behavior to the individual items in your
collection view?

As described in [Handle events with the `onUpdate()`
class](https://developer.android.com/guide/topics/appwidgets#handle-events), you normally use
[`setOnClickPendingIntent()`](https://developer.android.com/reference/android/widget/RemoteViews#setOnClickPendingIntent(int,%0Aandroid.app.PendingIntent)) to set an object's click behavior---such as to
cause a button to launch an [`Activity`](https://developer.android.com/reference/android/app/Activity). But
this approach is not allowed for child views in an individual collection item.
For example, you can use `setOnClickPendingIntent()` to set up a global button
in the Gmail widget that launches the app, for example, but not on the
individual list items.

Instead, to add click behavior to individual items in a collection, use
[`setOnClickFillInIntent()`](https://developer.android.com/reference/android/widget/RemoteViews#setOnClickFillInIntent(int,%0Aandroid.content.Intent)). This entails setting up a pending intent template for
your collection view and then setting a fill-in intent on each item in the
collection via your `RemoteViewsFactory`.

This section uses the `StackWidget` sample to describe how to add behavior to
individual items. In the `StackWidget` sample, if the user touches the top view,
the widget displays the `Toast` message "Touched view *n* ," where *n* is the
index (position) of the touched view. This is how it works:

- The `StackWidgetProvider`---an [`AppWidgetProvider`](https://developer.android.com/reference/android/appwidget/AppWidgetProvider)
  subclass---creates a pending intent with a custom action called
  `TOAST_ACTION`.

- When the user touches a view, the intent fires and it broadcasts
  `TOAST_ACTION`.

- This broadcast is intercepted by the `StackWidgetProvider` class's
  [`onReceive()`](https://developer.android.com/reference/android/appwidget/AppWidgetProvider#onReceive(android.content.Context,%0Aandroid.content.Intent)) method, and the widget displays the `Toast` message
  for the touched view. The data for the collection items is provided by the
  `RemoteViewsFactory` through the `RemoteViewsService`.

| **Note:** The `StackWidget` sample uses a broadcast, but typically a widget launches an activity in a scenario like this.

#### Set up the pending intent template

The `StackWidgetProvider` (an
[`AppWidgetProvider`](https://developer.android.com/reference/android/appwidget/AppWidgetProvider) subclass)
sets up a pending intent. Individual items of a collection can't set up their
own pending intents. Instead, the collection as a whole sets up a pending intent
template, and the individual items set a fill-in intent to create unique
behavior on an item-by-item basis.

This class also receives the broadcast that is sent when the user touches a
view. It processes this event in its `onReceive()` method. If the intent's
action is `TOAST_ACTION`, the widget displays a `Toast` message for the current
view.  

### Kotlin

```kotlin
const val TOAST_ACTION = "com.example.android.stackwidget.TOAST_ACTION"
const val EXTRA_ITEM = "com.example.android.stackwidget.EXTRA_ITEM"

class StackWidgetProvider : AppWidgetProvider() {

    ...

    // Called when the BroadcastReceiver receives an Intent broadcast.
    // Checks whether the intent's action is TOAST_ACTION. If it is, the
    // widget displays a Toast message for the current item.
    override fun onReceive(context: Context, intent: Intent) {
        val mgr: AppWidgetManager = AppWidgetManager.getInstance(context)
        if (intent.action == TOAST_ACTION) {
            val appWidgetId: Int = intent.getIntExtra(
                    AppWidgetManager.EXTRA_APPWIDGET_ID,
                    AppWidgetManager.INVALID_APPWIDGET_ID
            )
            // EXTRA_ITEM represents a custom value provided by the Intent
            // passed to the setOnClickFillInIntent() method to indicate the
            // position of the clicked item. See StackRemoteViewsFactory in
            // https://developer.android.com/develop/ui/views/appwidgets/collections#setup-fill-in-intent for details.
            val viewIndex: Int = intent.getIntExtra(EXTRA_ITEM, 0)
            Toast.makeText(context, "Touched view $viewIndex", Toast.LENGTH_SHORT).show()
        }
        super.onReceive(context, intent)
    }

    override fun onUpdate(
            context: Context,
            appWidgetManager: AppWidgetManager,
            appWidgetIds: IntArray
    ) {
        // Update each of the widgets with the remote adapter.
        appWidgetIds.forEach { appWidgetId ->

            // Sets up the intent that points to the StackViewService that
            // provides the views for this collection.
            val intent = Intent(context, StackWidgetService::class.java).apply {
                putExtra(AppWidgetManager.EXTRA_APPWIDGET_ID, appWidgetId)
                // When intents are compared, the extras are ignored, so embed
                // the extra sinto the data so that the extras are not ignored.
                data = Uri.parse(toUri(Intent.URI_INTENT_SCHEME))
            }
            val rv = RemoteViews(context.packageName, R.layout.widget_layout).apply {
                setRemoteAdapter(R.id.stack_view, intent)

                // The empty view is displayed when the collection has no items.
                // It must be a sibling of the collection view.
                setEmptyView(R.id.stack_view, R.id.empty_view)
            }

            // This section makes it possible for items to have individualized
            // behavior. It does this by setting up a pending intent template.
            // Individuals items of a collection can't set up their own pending
            // intents. Instead, the collection as a whole sets up a pending
            // intent template, and the individual items set a fillInIntent
            // to create unique behavior on an item-by-item basis.
            val toastPendingIntent: PendingIntent = Intent(
                    context,
                    StackWidgetProvider::class.java
            ).run {
                // Set the action for the intent.
                // When the user touches a particular view, it has the effect of
                // broadcasting TOAST_ACTION.
                action = TOAST_ACTION
                putExtra(AppWidgetManager.EXTRA_APPWIDGET_ID, appWidgetId)
                data = Uri.parse(toUri(Intent.URI_INTENT_SCHEME))

                PendingIntent.getBroadcast(context, 0, this, PendingIntent.FLAG_UPDATE_CURRENT)
            }
            rv.setPendingIntentTemplate(R.id.stack_view, toastPendingIntent)

            appWidgetManager.updateAppWidget(appWidgetId, rv)
        }
        super.onUpdate(context, appWidgetManager, appWidgetIds)
    }
}
```

### Java

```java
public class StackWidgetProvider extends AppWidgetProvider {
    public static final String TOAST_ACTION = "com.example.android.stackwidget.TOAST_ACTION";
    public static final String EXTRA_ITEM = "com.example.android.stackwidget.EXTRA_ITEM";

    ...

    // Called when the BroadcastReceiver receives an Intent broadcast.
    // Checks whether the intent's action is TOAST_ACTION. If it is, the
    // widget displays a Toast message for the current item.
    @Override
    public void onReceive(Context context, Intent intent) {
        AppWidgetManager mgr = AppWidgetManager.getInstance(context);
        if (intent.getAction().equals(TOAST_ACTION)) {
            int appWidgetId = intent.getIntExtra(AppWidgetManager.EXTRA_APPWIDGET_ID,
                AppWidgetManager.INVALID_APPWIDGET_ID);
            // EXTRA_ITEM represents a custom value provided by the Intent
            // passed to the setOnClickFillInIntent() method to indicate the
            // position of the clicked item. See StackRemoteViewsFactory in
            // https://developer.android.com/develop/ui/views/appwidgets/collections#setup-fill-in-intent for details.
            int viewIndex = intent.getIntExtra(EXTRA_ITEM, 0);
            Toast.makeText(context, "Touched view " + viewIndex, Toast.LENGTH_SHORT).show();
        }
        super.onReceive(context, intent);
    }

    @Override
    public void onUpdate(Context context, AppWidgetManager appWidgetManager, int[] appWidgetIds) {
        // Update each of the widgets with the remote adapter.
        for (int i = 0; i < appWidgetIds.length; ++i) {

            // Sets up the intent that points to the StackViewService that
            // provides the views for this collection.
            Intent intent = new Intent(context, StackWidgetService.class);
            intent.putExtra(AppWidgetManager.EXTRA_APPWIDGET_ID, appWidgetIds[i]);
            // When intents are compared, the extras are ignored, so embed
            // the extras into the data so that the extras are not
            // ignored.
            intent.setData(Uri.parse(intent.toUri(Intent.URI_INTENT_SCHEME)));
            RemoteViews rv = new RemoteViews(context.getPackageName(), R.layout.widget_layout);
            rv.setRemoteAdapter(appWidgetIds[i], R.id.stack_view, intent);

            // The empty view is displayed when the collection has no items. It
            // must be a sibling of the collection view.
            rv.setEmptyView(R.id.stack_view, R.id.empty_view);

            // This section makes it possible for items to have individualized
            // behavior. It does this by setting up a pending intent template.
            // Individuals items of a collection can't set up their own pending
            // intents. Instead, the collection as a whole sets up a pending
            // intent template, and the individual items set a fillInIntent
            // to create unique behavior on an item-by-item basis.
            Intent toastIntent = new Intent(context, StackWidgetProvider.class);
            // Set the action for the intent.
            // When the user touches a particular view, it has the effect of
            // broadcasting TOAST_ACTION.
            toastIntent.setAction(StackWidgetProvider.TOAST_ACTION);
            toastIntent.putExtra(AppWidgetManager.EXTRA_APPWIDGET_ID, appWidgetIds[i]);
            intent.setData(Uri.parse(intent.toUri(Intent.URI_INTENT_SCHEME)));
            PendingIntent toastPendingIntent = PendingIntent.getBroadcast(context, 0, toastIntent,
                PendingIntent.FLAG_UPDATE_CURRENT);
            rv.setPendingIntentTemplate(R.id.stack_view, toastPendingIntent);

            appWidgetManager.updateAppWidget(appWidgetIds[i], rv);
        }
        super.onUpdate(context, appWidgetManager, appWidgetIds);
    }
}
```

#### Set the fill-in intent

Your `RemoteViewsFactory` must set a fill-in intent on each item in the
collection. This makes it possible to distinguish the individual on-click action
of a given item. The fill-in intent is then combined with the
[`PendingIntent`](https://developer.android.com/reference/android/app/PendingIntent) template to determine
the final intent that is executed when the item is tapped.  

### Kotlin

```kotlin
private const val REMOTE_VIEW_COUNT: Int = 10

class StackRemoteViewsFactory(
        private val context: Context,
        intent: Intent
) : RemoteViewsService.RemoteViewsFactory {

    private lateinit var widgetItems: List<WidgetItem>
    private val appWidgetId: Int = intent.getIntExtra(
            AppWidgetManager.EXTRA_APPWIDGET_ID,
            AppWidgetManager.INVALID_APPWIDGET_ID
    )

    override fun onCreate() {
        // In onCreate(), set up any connections or cursors to your data source.
        // Heavy lifting, such as downloading or creating content, must be
        // deferred to onDataSetChanged() or getViewAt(). Taking more than 20
        // seconds on this call results in an ANR.
        widgetItems = List(REMOTE_VIEW_COUNT) { index -> WidgetItem("$index!") }
        ...
    }
    ...

    override fun getViewAt(position: Int): RemoteViews {
        // Construct a remote views item based on the widget item XML file
        // and set the text based on the position.
        return RemoteViews(context.packageName, R.layout.widget_item).apply {
            setTextViewText(R.id.widget_item, widgetItems[position].text)

            // Set a fill-intent to fill in the pending intent template.
            // that is set on the collection view in StackWidgetProvider.
            val fillInIntent = Intent().apply {
                Bundle().also { extras ->
                    extras.putInt(EXTRA_ITEM, position)
                    putExtras(extras)
                }
            }
            // Make it possible to distinguish the individual on-click
            // action of a given item.
            setOnClickFillInIntent(R.id.widget_item, fillInIntent)
            ...
        }
    }
    ...
}
```

### Java

```java
public class StackWidgetService extends RemoteViewsService {
    @Override
    public RemoteViewsFactory onGetViewFactory(Intent intent) {
        return new StackRemoteViewsFactory(this.getApplicationContext(), intent);
    }
}

class StackRemoteViewsFactory implements RemoteViewsService.RemoteViewsFactory {
    private static final int count = 10;
    private List<WidgetItem> widgetItems = new ArrayList<WidgetItem>();
    private Context context;
    private int appWidgetId;

    public StackRemoteViewsFactory(Context context, Intent intent) {
        this.context = context;
        appWidgetId = intent.getIntExtra(AppWidgetManager.EXTRA_APPWIDGET_ID,
                AppWidgetManager.INVALID_APPWIDGET_ID);
    }

    // Initialize the data set.
    public void onCreate() {
        // In onCreate(), set up any connections or cursors to your data
        // source. Heavy lifting, such as downloading or creating
        // content, must be deferred to onDataSetChanged() or
        // getViewAt(). Taking more than 20 seconds on this call results
        // in an ANR.
        for (int i = 0; i < count; i++) {
            widgetItems.add(new WidgetItem(i + "!"));
        }
        ...
    }

    // Given the position (index) of a WidgetItem in the array, use the
    // item's text value in combination with the widget item XML file to
    // construct a RemoteViews object.
    public RemoteViews getViewAt(int position) {
        // Position always ranges from 0 to getCount() - 1.

        // Construct a RemoteViews item based on the widget item XML
        // file and set the text based on the position.
        RemoteViews rv = new RemoteViews(context.getPackageName(), R.layout.widget_item);
        rv.setTextViewText(R.id.widget_item, widgetItems.get(position).text);

        // Set a fill-intent to fill in the pending
        // intent template that is set on the collection view in
        // StackWidgetProvider.
        Bundle extras = new Bundle();
        extras.putInt(StackWidgetProvider.EXTRA_ITEM, position);
        Intent fillInIntent = new Intent();
        fillInIntent.putExtras(extras);
        // Make it possible to distinguish the individual on-click
        // action of a given item.
        rv.setOnClickFillInIntent(R.id.widget_item, fillInIntent);

        // Return the RemoteViews object.
        return rv;
    }
    ...
}
```

## Keep collection data fresh

Figure 2 illustrates the update flow in a widget that uses collections. It shows
how the widget code interacts with the `RemoteViewsFactory` and how you can
trigger updates:
![](https://developer.android.com/static/images/appwidgets/appwidget_collections.png) **Figure 2.** Interaction with `RemoteViewsFactory` during updates.

Widgets that use collections can provide users with up-to-date content. For
example, the Gmail widget gives users a snapshot of their inbox. To make this
possible, trigger your `RemoteViewsFactory` and collection view to fetch and
display new data.

To do this, use the
[`AppWidgetManager`](https://developer.android.com/reference/android/appwidget/AppWidgetManager) to call
[`notifyAppWidgetViewDataChanged()`](https://developer.android.com/reference/android/appwidget/AppWidgetManager#notifyAppWidgetViewDataChanged(int,%0Aint)). This call results in a callback to your `RemoteViewsFactory` object's
[`onDataSetChanged()`](https://developer.android.com/reference/android/widget/RemoteViewsService.RemoteViewsFactory#onDataSetChanged())
method, which lets you fetch any new data.

You can perform processing-intensive operations synchronously within the
`onDataSetChanged()` callback. You are guaranteed that this call is completed
before the metadata or view data is fetched from the `RemoteViewsFactory`. You
can also perform processing-intensive operations within the `getViewAt()`
method. If this call takes long, the loading view---specified by the
`RemoteViewsFactory` object's
[`getLoadingView()`](https://developer.android.com/reference/android/widget/RemoteViewsService.RemoteViewsFactory#getLoadingView())
method---is displayed in the corresponding position of the collection view
until it returns.

## Use RemoteCollectionItems to pass along a collection directly

Android 12 (API level 31) adds the [`setRemoteAdapter(int viewId,
RemoteViews.RemoteCollectionItems
items)`](https://developer.android.com/reference/android/widget/RemoteViews#setRemoteAdapter(int,%20android.widget.RemoteViews.RemoteCollectionItems))
method, which lets your app pass along a collection directly when populating a
collection view. If you set your adapter using this method, you don't need to
implement a `RemoteViewsFactory` and you don't need to call
`notifyAppWidgetViewDataChanged()`.

In addition to making it easier to populate your adapter, this approach also
removes the latency for populating new itemswhen users scroll down the list to
reveal a new item. This approach to setting the adapter is preferred as long as
your set of collection items is relatively small. However, for example, this
approach doesn't work well if your collection contains numerous `Bitmaps` being
passed to `setImageViewBitmap`.

If the collection doesn't use a constant set of layouts---that is, if some
items are only sometimes present---use `setViewTypeCount` to specify the
maximum number of unique layouts that the collection can contain. This lets the
adapter be reused across updates to your app widget.

Here's an example of how to implement simplified `RemoteViews` collections.  

### Kotlin

```kotlin
val itemLayouts = listOf(
        R.layout.item_type_1,
        R.layout.item_type_2,
        ...
)

remoteView.setRemoteAdapter(
        R.id.list_view,
        RemoteViews.RemoteCollectionItems.Builder()
            .addItem(/* id= */ ID_1, RemoteViews(context.packageName, R.layout.item_type_1))
            .addItem(/* id= */ ID_2, RemoteViews(context.packageName, R.layout.item_type_2))
            ...
            .setViewTypeCount(itemLayouts.count())
            .build()
)
```

### Java

```java
List<Integer> itemLayouts = Arrays.asList(
    R.layout.item_type_1,
    R.layout.item_type_2,
    ...
);

remoteView.setRemoteAdapter(
    R.id.list_view,
    new RemoteViews.RemoteCollectionItems.Builder()
        .addItem(/* id= */ ID_1, new RemoteViews(context.getPackageName(), R.layout.item_type_1))
        .addItem(/* id= */ ID_2, new RemoteViews(context.getPackageName(), R.layout.item_type_2))
        ...
        .setViewTypeCount(itemLayouts.size())
        .build()
);
```
| **Note:** When calling [`setViewTypeCount()`](https://developer.android.com/reference/android/widget/RemoteViews.RemoteCollectionItems.Builder#setViewTypeCount(int)), pass in the maximum number of different layout IDs that are used by `RemoteViews` in this collection. Otherwise, the view type count is inferred from the provided items, and the adapter is recreated when sending an update that uses additional layouts.