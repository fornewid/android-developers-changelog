---
title: https://developer.android.com/about/versions/12/features/widgets
url: https://developer.android.com/about/versions/12/features/widgets
source: md.txt
---

Android 12 (API level 31) revamps the existing [Widgets
API](https://developer.android.com/guide/topics/appwidgets/overview) to improve the user and developer
experience in the platform and launchers. Use this guide to learn how to ensure
your widget is compatible with Android 12, and also as a reference for APIs for
refreshing your existing widget.

![Alt text](https://developer.android.com/static/images/appwidgets/widget-intro.png "Widget examples")

## Ensure your widget is compatible with Android 12

Widgets in Android 12 have rounded corners. When an app widget is
used on a device running Android 12 or higher, the launcher
automatically identifies the widget's background and crops it to have rounded
corners.

In this scenario, your widget may not display properly in either of the
following conditions:

- **The widget contains content in the corners**: This may cause some content
  in the corner area to be cropped.

- **The widget uses a background that is not susceptible to cropping**. This
  includes a transparent background, empty views or layouts, or any other kind
  of special background not prone to cropping. The system may not be able to
  correctly identify the background to use.

If your widget will be affected by this change, we recommend refreshing it with
rounded corners (as described in the following section) to ensure it displays
properly.

> [!CAUTION]
> **Caution:** The dimensions of rounded corners may vary across devices because the size of the corner radius is controllable by both device manufacturers (up to 16dp) and third-party launchers. We recommend refreshing the widget to help avoid unsatisfactory results.

### Use the sample

To see all these APIs in action, check out our [sample list widget](https://github.com/android/user-interface-samples/tree/main/AppWidget).

## Implement rounded corners

> [!NOTE]
> **Note:** This guidance may be outdated. Refer to [Implement
> rounded corners](https://developer.android.com/guide/topics/appwidgets#rounded-corner) for the latest guidance.

Android 12 introduces the [`system_app_widget_background_radius`](https://developer.android.com/reference/android/R.dimen#system_app_widget_background_radius)
and [`system_app_widget_inner_radius`](https://developer.android.com/reference/android/R.dimen#system_app_widget_inner_radius)
system parameters to set the radii of your widget's rounded corners.
![Tokyo weather widget](https://developer.android.com/static/images/appwidgets/widget-weather.png) **Figure 1:**Rounded corners on a widget and a view inside the widget

1 Corner of the widget.

2 Corner of a view inside the widget.

For details, see [Implement rounded corners](https://developer.android.com/guide/topics/appwidgets#rounded-corner).

## Add device theming

Starting in Android 12, a widget can use the device theme colors
for buttons, backgrounds, and other components, including light and dark themes.
This enables smoother transitions and consistency across different widgets.

See [Add device theming](https://developer.android.com/guide/topics/appwidgets/enhance#dynamic-colors) for more information.
![Widget in light mode theme](https://developer.android.com/static/images/appwidgets/example-lightmode.png) **Figure 2:**Widget in light theme ![Widgets in dark mode theme](https://developer.android.com/static/images/appwidgets/example-darkmode.png) **Figure 3:**Widget in dark theme

<br />

## Make it easier to personalize widgets

If you specify a configuration activity with the [`configure`](https://developer.android.com/reference/android/appwidget/AppWidgetProviderInfo#configure) attribute of
[`appwidget-provider`](https://developer.android.com/reference/android/appwidget/AppWidgetProviderInfo),
the App Widget host launches that activity immediately after a user adds the
widget to their home screen.

Android 12 adds new options to let you provide a better
configuration experience for users. See [Enable users to configure
widgets](https://developer.android.com/guide/topics/appwidgets/configuration) for details.

## Add new compound buttons

Android 12 adds new support for stateful behavior using the
following existing components:

- [`CheckBox`](https://developer.android.com/reference/kotlin/android/widget/CheckBox)

- [`Switch`](https://developer.android.com/reference/android/widget/Switch)

- [`RadioButton`](https://developer.android.com/reference/android/widget/RadioButton)

The widget is still stateless. Your app must store the state and register for
state change events.
![](https://developer.android.com/static/images/appwidgets/home.png) **Figure 4:**Example widget with checkboxes

For details, see [Support for stateful behavior](https://developer.android.com/guide/topics/appwidgets#stateful-behavior).

## Use improved APIs for widget sizes and layouts

Starting in Android 12, you can can take advantage of more refined size
attributes and more flexible layouts, by specifying additional widget sizing
constraints and by providing responsive layouts and exact layouts.

See [Provide flexible widget layouts](https://developer.android.com/guide/topics/appwidgets/layouts) for details.

## Improve your app's widget picker experience

Android 12 enables you to improve the widget picker experience
for your app by adding dynamic widget previews and widget descriptions. For
details, see [Add scalable widget previews to the widget
picker](https://developer.android.com/guide/topics/appwidgets/enhance#add-scalable-widget-previews) and [Add a description for
your widget](https://developer.android.com/guide/topics/appwidgets/enhance#add-widget-description).

## Enable smoother transitions

Starting in Android 12, launchers provide a smoother transition
when a user launches your app from a widget. See [Enable smoother
transitions](https://developer.android.com/guide/topics/appwidgets/enhance#enable-smoother-transitions) for details.

## Use simplified `RemoteViews` collections

Android 12 adds the
[`setRemoteAdapter(int viewId, RemoteViews.RemoteCollectionItems items)`](https://developer.android.com/reference/android/widget/RemoteViews#setRemoteAdapter(int,%20android.widget.RemoteViews.RemoteCollectionItems))
method, which lets your app pass along a collection directly when populating a
[`ListView`](https://developer.android.com/reference/android/widget/ListView). Previously, when using a
`ListView`, it was necessary to implement and declare a
`RemoteViewsService` to return
[`RemoteViewsFactory`](https://developer.android.com/reference/android/widget/RemoteViewsService.RemoteViewsFactory).

For details, see [Use `RemoteViews` collections](https://developer.android.com/guide/topics/appwidgets/collections#use-remote-collections).

## Use runtime modification of `RemoteViews`

Android 12 adds several `RemoteViews` methods that allow for runtime
modification of `RemoteViews` attributes. See the `RemoteViews` API reference
for the full list of added methods.

For details, see [Use runtime modification of
`RemoteViews`](https://developer.android.com/guide/topics/appwidgets/enhance#use-runtime-mod-of-remoteviews).