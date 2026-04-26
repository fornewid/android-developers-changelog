---
title: https://developer.android.com/develop/ui/views/appwidgets/previews
url: https://developer.android.com/develop/ui/views/appwidgets/previews
source: md.txt
---

To improve your app's widget picker experience, provide a generated widget
preview on Android 15 and later devices, a scaled widget preview
(by specifying a `previewLayout`) for Android 12 to
Android 14 devices, and a `previewImage` for earlier versions.

Generated widget previews allow you to create dynamic, personalized previews for
your widgets that accurately reflect how they will appear on a user's home
screen. For Android 15 and higher, they are provided
through a push API, meaning your app provides the preview at any point during
its lifecycle without receiving an explicit request from the widget host.

For more information, see [Enrich your app with live updates and widgets](https://www.youtube.com/watch?v=_Akf_u08p7U) on
YouTube.

## Add generated previews

To show Generated Widget Previews on Android 15 or later device, first set the
`compileSdk` value to 35 or later in the module `build.gradle` file to have the
ability to provide [`RemoteViews`](https://developer.android.com/reference/android/widget/RemoteViews) to the widget picker

Apps can use `setWidgetPreview` in [`AppWidgetManager`](https://developer.android.com/reference/kotlin/android/appwidget/AppWidgetManager). To prevent abuse
and mitigate system health concerns, `setWidgetPreview` is a rate-limited API.
The default limit is approximately two calls per hour.

There isn't a callback from the system to provide previews, so your app must
decide when to call `setWidgetPreviews`. The update strategy depends on your
widget's use case:

- If the widget has static information or is a quick action, set the preview when the app is first launched.
- You can set the preview once your app has data; for example, after a user sign-in or initial setup.
- You can set up a periodic task to update the previews at a chosen cadence.

The following example loads an XML widget layout resource and sets it as the
preview. A compileSdk build setting of 35 or later is
required for `setWidgetPreview` to show as a method in this snippet.

    AppWidgetManager.getInstance(appContext).setWidgetPreview(
        ComponentName(
            appContext,
            ExampleAppWidgetReceiver::class.java
        ),
        AppWidgetProviderInfo.WIDGET_CATEGORY_HOME_SCREEN,
        RemoteViews("com.example", R.layout.widget_preview)
    )https://github.com/android/snippets/blob/908c46de548e0b8489cafce12f8520a7905358ed/views/src/main/java/com/example/example/snippet/views/appwidget/AppWidgetSnippets.kt#L42-L49

## Add scalable widget previews

Starting in Android 12, the widget preview displayed in the
widget picker is scalable. You provide it as an XML layout set to the widget's
default size. Previously, the widget preview was a static drawable resource, in
some cases leading to previews inaccurately reflecting how widgets appear when
they are added to the home screen.

To implement scalable widget previews, use the
[`previewLayout`](https://developer.android.com/reference/android/appwidget/AppWidgetProviderInfo#previewLayout)
attribute of the `appwidget-provider` element to provide an XML layout instead:

    <appwidget-provider
        android:previewLayout="@layout/my_widget_preview">
    </appwidget-provider>

We recommend using the same layout as the actual widget, with realistic default
or test values. Most apps use the same `previewLayout` and `initialLayout`. For
guidance on creating accurate preview layouts, see
[Build accurate previews that include dynamic items](https://developer.android.com/develop/ui/views/appwidgets/previews#build-accurate-previews).

We recommend specifying both the `previewLayout` and `previewImage` attributes,
so that your app can fall back to using `previewImage` if the user's device
doesn't support `previewLayout`. The `previewLayout` attribute takes precedence
over the `previewImage` attribute.

## Add static widget previews for backward compatibility

To let widget pickers on Android 11 (API level 30) or lower show previews of your
widget, or as a fallback for scalable previews, specify the [`previewImage`](https://developer.android.com/reference/android/appwidget/AppWidgetProviderInfo#previewImage)
attribute.

If you change the widget's appearance, update the preview image.

This attribute is also used as a fallback for generated previews if you haven't
set one using `setWidgetPreview`.

## Build accurate previews that include dynamic items

![](https://developer.android.com/static/images/appwidgets/missing-list.png) **Figure 1:**A widget preview displaying no list items.

This section explains the recommended approach for displaying multiple items in
a widget preview for a widget with a [collection view](https://developer.android.com/guide/topics/appwidgets/collections)---that is, a
widget that uses a `ListView`, `GridView`, or `StackView`. This applies to
scalable widget previews, not generated previews.

If your widget uses one of these views, creating a scalable preview by
providing the actual widget layout directly in `previewLayout` can degrade the
experience when the widget preview displays no items. This occurs because
collection view data is set dynamically at runtime, and it looks similar to the
image shown in figure 1.

To make previews of widgets with collection views display properly in the widget
picker, we recommend maintaining a separate layout file designated for only the
preview. This separate layout file should include the following:

- The actual widget layout.
- A placeholder collection view with fake items. For example, you can mimic a `ListView` by providing a placeholder `LinearLayout` with several fake list items.

To illustrate an example for a `ListView`, start with a separate layout file:

    // res/layout/widget_preview.xml

    <LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
       android:layout_width="match_parent"
       android:layout_height="wrap_content"
       android:background="@drawable/widget_background"
       android:orientation="vertical">

        // Include the actual widget layout that contains ListView.
        <include
            layout="@layout/widget_view"
            android:layout_width="match_parent"
            android:layout_height="wrap_content" />

        // The number of fake items you include depends on the values you provide
        // for minHeight or targetCellHeight in the AppWidgetProviderInfo
        // definition.

        <TextView android:text="@string/fake_item1"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:layout_marginVertical="?attr/appWidgetInternalPadding" />

        <TextView android:text="@string/fake_item2"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:layout_marginVertical="?attr/appWidgetInternalPadding" />

    </LinearLayout>

Specify the preview layout file when providing the `previewLayout` attribute of
the `AppWidgetProviderInfo` metadata. You still specify the actual widget layout
for the `initialLayout` attribute and use the actual widget layout when
constructing a `RemoteViews` at runtime.

    <appwidget-provider
        previewLayout="@layout/widget_preview"
        initialLayout="@layout/widget_view" />

### Complex list items

The example in the previous section provides fake list items, because the list
items are [`TextView`](https://developer.android.com/reference/android/widget/TextView) objects. It can be
more complex to provide fake items if the items are complex layouts.

Consider a list item that is defined in `widget_list_item.xml` and consists of
two `TextView` objects:

    <LinearLayout  xmlns:android="http://schemas.android.com/apk/res/android"
            android:layout_width="match_parent"
            android:layout_height="wrap_content">

        <TextView android:id="@id/title"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:text="@string/fake_title" />

        <TextView android:id="@id/content"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:text="@string/fake_content" />
    </LinearLayout>

To provide fake list items, you can include the layout multiple times, but this
causes each list item to be identical. To provide unique list items, follow
these steps:

1. Create a set of attributes for the text values:

       <resources>
           <attr name="widgetTitle" format="string" />
           <attr name="widgetContent" format="string" />
       </resources>

2. Use these attributes to set the text:

       <LinearLayout  xmlns:android="http://schemas.android.com/apk/res/android"
               android:layout_width="match_parent"
               android:layout_height="wrap_content">

           <TextView android:id="@id/title"
               android:layout_width="match_parent"
               android:layout_height="wrap_content"
               android:text="?widgetTitle" />

           <TextView android:id="@id/content"
               android:layout_width="match_parent"
               android:layout_height="wrap_content"
               android:text="?widgetContent" />
       </LinearLayout>

3. Create as many styles as required for the preview. Redefine the values in
   each style:

       <resources>

           <style name="Theme.Widget.ListItem">
               <item name="widgetTitle"></item>
               <item name="widgetContent"></item>
           </style>
           <style name="Theme.Widget.ListItem.Preview1">
               <item name="widgetTitle">Fake Title 1</item>
               <item name="widgetContent">Fake content 1</item>
           </style>
           <style name="Theme.Widget.ListItem.Preview2">
               <item name="widgetTitle">Fake title 2</item>
               <item name="widgetContent">Fake content 2</item>
           </style>

       </resources>

4. Apply the styles on the fake items in the preview layout:

       <LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
          android:layout_width="match_parent"
          android:layout_height="wrap_content" ...>

           <include layout="@layout/widget_view" ... />

           <include layout="@layout/widget_list_item"
               android:theme="@style/Theme.Widget.ListItem.Preview1" />

           <include layout="@layout/widget_list_item"
               android:theme="@style/Theme.Widget.ListItem.Preview2" />

       </LinearLayout>