---
title: https://developer.android.com/training/cars/media/auto
url: https://developer.android.com/training/cars/media/auto
source: md.txt
---

You need to make a few changes to your app's manifest so that Android Auto
can discover and interact with your app's media browser service.
| **Important:** This guide assumes that you have already [built a media browser service](https://developer.android.com/training/cars/media#implement_browser) and you want to add support for Android Auto to your existing project. If you are new to app development for cars, see the [Android for Cars overview page](https://developer.android.com/training/cars).

## Declare media support for Android Auto

Use the following manifest entry to declare that your phone app supports
Android Auto:  

    <application>
        ...
        <meta-data android:name="com.google.android.gms.car.application"
            android:resource="@xml/automotive_app_desc"/>
        ...
    </application>

This manifest entry refers to an XML file that declares what automotive
capabilities your app supports. To indicate that you have a media app, add an
XML file named `automotive_app_desc.xml` to the `res/xml/` directory in your
project. This file should include the following content:  

    <automotiveApp>
        <uses name="media"/>
    </automotiveApp>

## Report an Android Auto Media issue

If you run into an issue while developing your media app for Android Auto, you
can report it using the
[Google Issue Tracker](https://issuetracker.google.com/issues?q=status:open+componentid:192643).
Be sure to fill out all the requested information in the issue template.

[Create a new issue](https://issuetracker.google.com/issues/new?component=192643)

Before filing a new issue, please check whether it is already reported in the issues
list. You can subscribe to and vote for issues by clicking the star for an issue in
the tracker. For more information, see
[Subscribing to an Issue](https://developers.google.com/issue-tracker/guides/subscribe#starring_an_issue).