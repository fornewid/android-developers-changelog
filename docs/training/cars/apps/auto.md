---
title: https://developer.android.com/training/cars/apps/auto
url: https://developer.android.com/training/cars/apps/auto
source: md.txt
---

Review the following information to learn how make changes to your app's manifest
so that Android Auto can discover and interact with your app's `CarAppService`.

## Declare Android Auto support

The [Android Auto host](https://developer.android.com/training/cars/apps#key-terms-concepts) checks whether
the app has declared support for [Android Auto](https://developer.android.com/training/cars#auto).
To enable this support, include the following entry in your app's manifest:  

    <application>
        ...
        <meta-data
            android:name="com.google.android.gms.car.application"
            android:resource="@xml/automotive_app_desc"/>
        ...
    </application>

This manifest entry refers to another XML file that you create with the
path <var translate="no">AppProjectDirectory</var>`/app/src/main/res/xml/automotive_app_desc.xml`.
In that file, you declare what Android Auto capabilities your app supports.

Apps using the [Android for Cars App
Library](https://developer.android.com/reference/androidx/car/app/package-summary)
must declare the `template` capability in the `automotive_app_desc.xml` file:  

    <automotiveApp>
        <uses name="template" />
    </automotiveApp>