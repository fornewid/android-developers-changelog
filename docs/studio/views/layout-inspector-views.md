---
title: https://developer.android.com/studio/views/layout-inspector-views
url: https://developer.android.com/studio/views/layout-inspector-views
source: md.txt
---

[Concepts and Jetpack Compose implementation](https://developer.android.com/studio/debug/layout-inspector)

The Layout Inspector in Android Studio lets you debug the layout of your app by
showing a view hierarchy where you can inspect the properties of each view. With
the Layout Inspector, you can compare your app layout with design mockups,
display a magnified view of your app, and examine details of its layout at
runtime. This is especially useful when your layout is built at runtime rather
than entirely in XML and the layout is behaving unexpectedly.

## View Attribute Inspection

Layout Inspector requires the following global setting to function properly:

    adb shell settings put global debug_view_attributes 1

This option generates extra information for inspection on all of the processes
on the device.

Layout Inspector automatically enables the setting when started. This causes the
current foreground `Activity` to restart. You will not see another `Activity`
restart unless the flag is manually disabled on the device.

To disable the flag, run the following adb command:

    adb shell settings delete global debug_view_attributes

Alternatively, turn off [Enable view attribute inspection](https://developer.android.com/studio/debug/dev-options#debugging) from your device's
[developer options](https://developer.android.com/studio/debug/dev-options#enable).