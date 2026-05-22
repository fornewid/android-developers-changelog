---
title: Enhance your widget  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/glance/enhance
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Enhance your widget Stay organized with collections Save and categorize content based on your preferences.





This guide includes details for optional widget enhancements that are
straightforward to implement and improve your users' widget experience.

## Add a name to your widget

Widgets need to have a unique name when they are displayed in the widget picker.

Widgets' names are loaded from the `label` attribute of the widget's `receiver`
element in the AndroidManifest.xml file.

```
<receiver
    ….
   android:label="Memories">
     ….
</receiver>
```

## Add a description for your widget

Starting in Android 12, provide a description for the widget
picker to display for your widget.

![A widget picker showing a widget and its description](/static/images/appwidgets/description.png)


**Figure 1.** Sample widget picker showing a widget
and its description.

Provide a description for your widget using the `description` attribute of the
`&lt;appwidget-provider&gt;` element:

```
<appwidget-provider
    android:description="@string/my_widget_description">
</appwidget-provider>
```

**Note:** Be concise. There is no character limit, but the representation and
available space for the description might differ depending on the device.

You can use the
[`descriptionRes`](/reference/android/appwidget/AppWidgetProviderInfo#descriptionRes)
attribute on previous versions of Android, but it is ignored by the widget
picker.

[Previous

arrow\_back

Create an app widget with Glance](/develop/ui/compose/glance/create-app-widget)

[Next

Enable widget configuration

arrow\_forward](/develop/ui/compose/glance/configuration)