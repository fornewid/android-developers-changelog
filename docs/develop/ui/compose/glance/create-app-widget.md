---
title: https://developer.android.com/develop/ui/compose/glance/create-app-widget
url: https://developer.android.com/develop/ui/compose/glance/create-app-widget
source: md.txt
---

The following sections describe how to create a simple app widget with Glance.

> [!IMPORTANT]
> **Key Point:** Glance provides a modern approach to build app widgets using Compose, but is restricted by the limitations of `AppWidgets` and `RemoteViews`. Therefore, Glance uses different *composables* from the Jetpack Compose UI.

## Declare the `AppWidget` in the Manifest

After completing the [setup steps](https://developer.android.com/develop/ui/compose/glance/setup), declare the [`AppWidget`](https://developer.android.com/guide/topics/appwidgets) and its
metadata in your app.

1. Extend the `AppWidget` receiver from `GlanceAppWidgetReceiver`:


   ```kotlin
   class MyAppWidgetReceiver : GlanceAppWidgetReceiver() {
       override val glanceAppWidget: GlanceAppWidget = TODO("Create GlanceAppWidget")
   }
   ```

   <br />

2. Register the provider of the app widget in your `AndroidManifest.xml` file
   and the associated metadata file:

           <receiver android:name=".glance.MyReceiver"
           android:exported="true">
           <intent-filter>
               <action android:name="android.appwidget.action.APPWIDGET_UPDATE" />
           </intent-filter>
           <meta-data
               android:name="android.appwidget.provider"
               android:resource="@xml/my_app_widget_info" />
       </receiver>https://github.com/android/snippets/blob/fbed24d5695413cfd86b4b2c6b6faf0a3a2eadb8/compose/snippets/src/main/AndroidManifest.xml#L60-L68

## Add the `AppWidgetProviderInfo` metadata

Next, follow the [Create a simple widget](https://developer.android.com/guide/topics/appwidgets#MetaData) guide to create and define the app
widget info in the `@xml/my_app_widget_info` file.

The only difference for Glance is that there is no `initialLayout` XML, but
you must define one. You can use the predefined loading layout provided in
the library:

    <appwidget-provider xmlns:android="http://schemas.android.com/apk/res/android"
        android:initialLayout="@layout/glance_default_loading_layout">
    </appwidget-provider>https://github.com/android/snippets/blob/fbed24d5695413cfd86b4b2c6b6faf0a3a2eadb8/compose/snippets/src/main/res/xml/my_app_widget_info.xml#L18-L20

## Define `GlanceAppWidget`

1. Create a new class that extends from [`GlanceAppWidget`](https://developer.android.com/reference/kotlin/androidx/glance/appwidget/GlanceAppWidget) and overrides the
   `provideGlance` method. This is the method where you can load data that is
   needed to render your widget:

   > [!NOTE]
   > **Note:** `provideGlance` runs on the main thread. To perform any long running operations in `provideGlance`, switch to another thread using `withContext`. See [Use coroutines for main-safety](https://developer.android.com/kotlin/coroutines/coroutines-adv#main-safety) for more details on how to run outside of the main thread.


   ```kotlin
   class MyAppWidget : GlanceAppWidget() {

       override suspend fun provideGlance(context: Context, id: GlanceId) {

           // In this method, load data needed to render the AppWidget.
           // Use `withContext` to switch to another thread for long running
           // operations.

           provideContent {
               // create your AppWidget here
               Text("Hello World")
           }
       }
   }
   ```

   <br />

2. Instantiate it in the `glanceAppWidget` on your `GlanceAppWidgetReceiver`:


   ```kotlin
   class MyAppWidgetReceiver : GlanceAppWidgetReceiver() {

       // Let MyAppWidgetReceiver know which GlanceAppWidget to use
       override val glanceAppWidget: GlanceAppWidget = MyAppWidget()
   }
   ```

   <br />

You've now configured an `AppWidget` using Glance.

## Create UI

The following snippet demonstrates how to create the UI:


```kotlin
/* Import Glance Composables
 In the event there is a name clash with the Compose classes of the same name,
 you may rename the imports per https://kotlinlang.org/docs/packages.html#imports
 using the `as` keyword.

import androidx.glance.Button
import androidx.glance.layout.Column
import androidx.glance.layout.Row
import androidx.glance.text.Text
*/
class MyAppWidget : GlanceAppWidget() {

    override suspend fun provideGlance(context: Context, id: GlanceId) {
        // Load data needed to render the AppWidget.
        // Use `withContext` to switch to another thread for long running
        // operations.

        provideContent {
            // create your AppWidget here
            MyContent()
        }
    }

    @Composable
    private fun MyContent() {
        Column(
            modifier = GlanceModifier.fillMaxSize(),
            verticalAlignment = Alignment.Top,
            horizontalAlignment = Alignment.CenterHorizontally
        ) {
            Text(text = "Where to?", modifier = GlanceModifier.padding(12.dp))
            Row(horizontalAlignment = Alignment.CenterHorizontally) {
                Button(
                    text = "Home",
                    onClick = actionStartActivity<MyActivity>()
                )
                Button(
                    text = "Work",
                    onClick = actionStartActivity<MyActivity>()
                )
            }
        }
    }
}
```

<br />

The preceding code sample does the following:

- In the top level [`Column`](https://developer.android.com/reference/kotlin/androidx/glance/layout/package-summary#column), items are placed vertically one after each other.
- The `Column` expands its size to match the available space (via the [`GlanceModifier`](https://developer.android.com/reference/kotlin/androidx/glance/GlanceModifier)) and aligns its content to the top (`verticalAlignment`) and centers it horizontally (`horizontalAlignment`).
- The `Column`'s content is defined using the lambda. The order matters.
  - The first item in the `Column` is a `Text` component with `12.dp` of padding.
  - The second item is a [`Row`](https://developer.android.com/reference/kotlin/androidx/glance/layout/package-summary#row), where items are placed horizontally one after each other, with two [`Buttons`](https://developer.android.com/reference/kotlin/androidx/glance/package-summary#button) centered horizontally (`horizontalAlignment`). The final display depends on the available space. The following image is an example of what it may look like:

![destination_widget](https://developer.android.com/static/develop/ui/compose/images/destination_widget.png) **Figure 1.** An example UI.

You can change the alignment values or apply different modifier values (such as
padding) to change the placement and size of the components. See the [reference
documentation](https://developer.android.com/reference/kotlin/androidx/glance/package-summary) for a full list of components, parameters, and available
modifiers for each class.