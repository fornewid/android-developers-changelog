---
title: Enable users to configure app widgets  |  Views  |  Android Developers
url: https://developer.android.com/develop/ui/views/appwidgets/configuration
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Views](https://developer.android.com/develop/ui/views/layout/declaring-layout)

# Enable users to configure app widgets Stay organized with collections Save and categorize content based on your preferences.





App widgets can be configurable. For example, a clock widget can let users
configure which time zone to display.

If you want to let users configure your widget’s settings, create a widget
configuration [`Activity`](/reference/android/app/Activity).

## Declare the configuration activity

Declaring the configuration activity in the manifest and linking it inside your
provider XML metadata is identical across both Views-based and Glance-based app
widgets.

To learn how to declare the configuration activity, see the Compose-first
[Declare the configuration activity section](/develop/ui/compose/glance/configuration#declare) in the Glance configuration
documentation.

## Implement the configuration activity

Because configuration activities are standard components called by the platform
launcher, their basic lifecycle callbacks must follow the system's return value
rules.

To learn how to implement a configuration activity, check the Compose-first
[Implement the configuration activity section](/develop/ui/compose/glance/configuration#implement) in the Glance documentation.

### Update the widget from the configuration activity

In traditional Views-based widgets, you update the widget upon configuration
completion using the `AppWidgetManager` and a `RemoteViews` layout instance.

If you are building a legacy Views-based widget and need to update the
RemoteViews layout, reference the traditional [Views Update sample code on
GitHub](https://github.com/android/user-interface-samples/blob/main/AppWidget/app/src/main/java/com/example/android/appwidget/rv/list/ListWidgetConfigureActivity.kt). For modern Compose-first widgets, see the [Update from the
configuration activity section](/develop/ui/compose/glance/configuration#update) in the Glance documentation.

## Widget configuration options

Widget behaviors (such as allowing reconfiguration later or skipping initial
configuration setup steps altogether) are registered inside metadata attributes
using standard Android 12 flags.

To learn how to leverage dynamic widget options, see the Compose-first [Widget
configuration options section](/develop/ui/compose/glance/configuration#widget-config-options) in the Glance configuration documentation.

### Enable users to reconfigure placed widgets

To understand how to add custom reconfigurable setup triggers, see the
Compose-first [Enable users to reconfigure placed widgets section](/develop/ui/compose/glance/configuration#reconfigure-widgets) in the
Glance documentation.

### Use the widget's default configuration

To learn how to skip configuration setups by default, see the Compose-first [Use
the widget's default configuration section](/develop/ui/compose/glance/configuration#use-default) in the Glance documentation.