---
title: Create an app widget with Glance  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/glance/create-app-widget
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Create an app widget with Glance Stay organized with collections Save and categorize content based on your preferences.



The following sections describe how to create a simple app widget with Glance.

**Key Point:** Glance provides a modern approach to build app widgets using Compose,
but is restricted by the limitations of `AppWidgets` and `RemoteViews`.
Therefore, Glance uses different *composables* from the Jetpack Compose UI.

## Declare the `AppWidget` in the Manifest

After completing the [setup steps](/develop/ui/compose/glance/setup), declare the [`AppWidget`](/guide/topics/appwidgets) and its
metadata in your app.

1. Extend the `AppWidget` receiver from `GlanceAppWidgetReceiver`:

   ```
   class MyAppWidgetReceiver : GlanceAppWidgetReceiver() {
       override val glanceAppWidget: GlanceAppWidget = TODO("Create GlanceAppWidget")
   }

   GlanceSnippets.kt
   ```
2. Register the provider of the app widget in your `AndroidManifest.xml` file
   and the associated metadata file:

   ```
       <receiver android:name=".glance.MyReceiver"
       android:exported="true">
       <intent-filter>
           <action android:name="android.appwidget.action.APPWIDGET_UPDATE" />
       </intent-filter>
       <meta-data
           android:name="android.appwidget.provider"
           android:resource="@xml/my_app_widget_info" />
   </receiver>

   AndroidManifest.xml
   ```

## Add the `AppWidgetProviderInfo` metadata

Next, follow the [Create a simple widget](/guide/topics/appwidgets#MetaData) guide to create and define the app
widget info in the `@xml/my_app_widget_info` file.

The only difference for Glance is that there is no `initialLayout` XML, but
you must define one. You can use the predefined loading layout provided in
the library:

```
<appwidget-provider xmlns:android="http://schemas.android.com/apk/res/android"
    android:initialLayout="@layout/glance_default_loading_layout">
</appwidget-provider>

my_app_widget_info.xml
```

## Define `GlanceAppWidget`

1. Create a new class that extends from [`GlanceAppWidget`](/reference/kotlin/androidx/glance/appwidget/GlanceAppWidget) and overrides the
   `provideGlance` method. This is the method where you can load data that is
   needed to render your widget:

   **Note:** `provideGlance` runs on the main thread. To perform any long running
   operations in `provideGlance`, switch to another thread using
   `withContext`. See [Use coroutines for main-safety](/kotlin/coroutines/coroutines-adv#main-safety) for more details on
   how to run outside of the main thread.

   ```
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

   GlanceSnippets.kt
   ```
2. Instantiate it in the `glanceAppWidget` on your `GlanceAppWidgetReceiver`:

   ```
   class MyAppWidgetReceiver : GlanceAppWidgetReceiver() {

       // Let MyAppWidgetReceiver know which GlanceAppWidget to use
       override val glanceAppWidget: GlanceAppWidget = MyAppWidget()
   }

   GlanceSnippets.kt
   ```

You've now configured an `AppWidget` using Glance.

## Create UI

The following snippet demonstrates how to create the UI:

```
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

GlanceSnippets.kt
```

The preceding code sample does the following:

* In the top level [`Column`](/reference/kotlin/androidx/glance/layout/package-summary#column), items are placed vertically one after each
  other.
* The `Column` expands its size to match the available space (via the
  [`GlanceModifier`](/reference/kotlin/androidx/glance/GlanceModifier) and aligns its content to the top (`verticalAlignment`)
  and centers it horizontally (`horizontalAlignment`).
* The `Column`'s content is defined using the lambda. The order matters.
  + The first item in the `Column` is a `Text` component with `12.dp` of
    padding.
  + The second item is a [`Row`](/reference/kotlin/androidx/glance/layout/package-summary#row), where items are placed horizontally one
    after each other, with two [`Buttons`](/reference/kotlin/androidx/glance/package-summary#button) centered horizontally
    (`horizontalAlignment`). The final display depends on the available space.
    The following image is an example of what it may look like:

![destination_widget](/static/develop/ui/compose/images/destination_widget.png)


**Figure 1.** An example UI.

You can change the alignment values or apply different modifier values (such as
padding) to change the placement and size of the components. See the [reference
documentation](/reference/kotlin/androidx/glance/package-summary) for a full list of components, parameters, and available
modifiers for each class.

[Previous

arrow\_back

Glance setup](/develop/ui/compose/glance/setup)

[Next

Add generated previews to your widget picker

arrow\_forward](/develop/ui/compose/glance/generated-previews)