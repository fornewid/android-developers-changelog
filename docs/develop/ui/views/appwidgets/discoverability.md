---
title: https://developer.android.com/develop/ui/views/appwidgets/discoverability
url: https://developer.android.com/develop/ui/views/appwidgets/discoverability
source: md.txt
---

On devices running Android 8.0 (API level 26) and higher, launchers that let
users create [pinned shortcuts](https://developer.android.com/guide/topics/ui/shortcuts#shortcut-types) also
let them pin widgets onto their home screen. Similar to pinned shortcuts, these
*pinned widgets* give users access to specific tasks in your app and can be
added to the home screen directly from the app, as shown in the following video.
![Example of responsive layout](https://developer.android.com/static/images/appwidgets/widget_pinning.gif) **Figure 2.**Example of pinning a widget.

## Let users pin a widget

In your app, you can create a request for the system to pin a widget onto a
supported launcher by completing the following steps:

1. Make sure you [declare a widget in your app's manifest file](https://developer.android.com/guide/topics/appwidgets#Manifest).

2. Call the
   [`requestPinAppWidget()`](https://developer.android.com/reference/android/appwidget/AppWidgetManager#requestPinAppWidget(android.content.ComponentName,%20android.os.Bundle,%20android.app.PendingIntent))
   method, as shown in the following code snippet:

### Kotlin

```kotlin
val appWidgetManager = AppWidgetManager.getInstance(context)
val myProvider = ComponentName(context, ExampleAppWidgetProvider::class.java)

if (appWidgetManager.isRequestPinAppWidgetSupported()) {
    // Create the PendingIntent object only if your app needs to be notified
    // when the user chooses to pin the widget. Note that if the pinning
    // operation fails, your app isn't notified. This callback receives the ID
    // of the newly pinned widget (EXTRA_APPWIDGET_ID).
    val successCallback = PendingIntent.getBroadcast(
            /* context = */ context,
            /* requestCode = */ 0,
            /* intent = */ Intent(...),
            /* flags = */ PendingIntent.FLAG_UPDATE_CURRENT)

    appWidgetManager.requestPinAppWidget(myProvider, null, successCallback)
}
```

### Java

```java
AppWidgetManager appWidgetManager = AppWidgetManager.getInstance(context);
ComponentName myProvider = new ComponentName(context, ExampleAppWidgetProvider.class);

if (appWidgetManager.isRequestPinAppWidgetSupported()) {
    // Create the PendingIntent object only if your app needs to be notified
    // when the user chooses to pin the widget. Note that if the pinning
    // operation fails, your app isn't notified. This callback receives the ID
    // of the newly pinned widget (EXTRA_APPWIDGET_ID).
    PendingIntent successCallback = PendingIntent.getBroadcast(
            /* context = */ context,
            /* requestCode = */ 0,
            /* intent = */ new Intent(...),
            /* flags = */ PendingIntent.FLAG_UPDATE_CURRENT);

    appWidgetManager.requestPinAppWidget(myProvider, null, successCallback);
}
```

> [!NOTE]
> **Note:** If your app doesn't need to be notified of whether the system successfully pins a widget onto a supported launcher, you can pass in `null` as the third argument to `requestPinAppWidget()`.

## Related design guidance

Users discover and add your widget through the widget picker or from within your
app when the widget's functionality is most relevant. For more information, see
[Discovery and promotion](https://developer.android.com/design/ui/mobile/guides/widgets/discovery-promotion).