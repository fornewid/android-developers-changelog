---
title: Add support for Android Auto to your templated app  |  Android for Cars  |  Android Developers
url: https://developer.android.com/training/cars/apps/auto
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android for Cars](https://developer.android.com/training/cars)

# Add support for Android Auto to your templated app Stay organized with collections Save and categorize content based on your preferences.



Review the following information to learn how make changes to your app's manifest
so that Android Auto can discover and interact with your app's `CarAppService`.

## Declare Android Auto support

The [Android Auto host](/training/cars/apps#key-terms-concepts) checks whether
the app has declared support for [Android Auto](/training/cars#auto).
To enable this support, include the following entry in your app's manifest:

```
<application>
    ...
    <meta-data
        android:name="com.google.android.gms.car.application"
        android:resource="@xml/automotive_app_desc"/>
    ...
</application>
```

This manifest entry refers to another XML file that you create with the
path `AppProjectDirectory/app/src/main/res/xml/automotive_app_desc.xml`.
In that file, you declare what Android Auto capabilities your app supports.

Apps using the [Android for Cars App
Library](/reference/androidx/car/app/package-summary)
must declare the `template` capability in the `automotive_app_desc.xml` file:

```
<automotiveApp>
    <uses name="template" />
</automotiveApp>
```