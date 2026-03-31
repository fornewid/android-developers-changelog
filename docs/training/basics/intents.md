---
title: Interact with other apps  |  App architecture  |  Android Developers
url: https://developer.android.com/training/basics/intents
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [App architecture](https://developer.android.com/topic/architecture/intro)

# Interact with other apps Stay organized with collections Save and categorize content based on your preferences.



An Android app typically has several [activities](/guide/components/activities). Each activity displays a
user interface that lets the user perform a specific task, such as viewing a map or taking a photo.
To take the user from one activity to another, your app must use an `Intent` to define your app's "intent" to do something. When you pass an
`Intent` to the system with a method
such as `startActivity()`,
the system uses the `Intent` to identify and start the appropriate app component. Using intents
even lets your app start an activity that is contained in a separate app.

An `Intent` can be *explicit*, to start
a specific `Activity` instance,
or *implicit*, to start any
component that can handle the intended action, such as "capture a photo."

The topics in this guide show you how to use an `Intent` to perform some basic
interactions with other apps, such as starting another app, receiving a result from that app, and
making your app able to respond to intents from other apps.

## Topics

**[Sending the user to another app](/training/basics/intents/sending)**
:   Shows you how to create implicit intents to launch other apps that can perform an
    action.

**[Get a result from an activity](/training/basics/intents/result)**
:   Shows you how to start another activity and receive a result from the activity.

**[Allow other apps to start your activity](/training/basics/intents/filters)**
:   Shows you how to make activities in your app open for use by other apps by defining
    intent filters that declare the implicit intents your app accepts.

**[Package visibility filtering on Android](/training/basics/intents/package-visibility)**
:   Shows you how to make other apps visible to your app if they
    aren't visible by default. Applies only to apps that target Android 11
    (API level 30) or higher.

**[Fulfill common use cases while having limited package visibility](/training/basics/intents/package-visibility-use-cases)**
:   Shows several types of app interactions that might require you to update
    your app's manifest file so that other apps are visible to your app.
    Applies only to apps that target Android 11 (API level 30) or higher.

**[Limit loading in on-device Android containers](/training/basics/intents/limit-play-loading)**
:   Shows you how to limit your Play Store app from loading in a simulated
    Android environment app, also known as an on-device Android container.

For additional information about the topics on this page, see the following:

* [Sharing simple data](/training/sharing)
* [Sharing files](/training/secure-file-sharing)* [Integrating Application with Intents](http://android-developers.blogspot.com/2009/11/integrating-application-with-intents.html) blog post
  * [Intents and Intent
    Filters](/guide/components/intents-filters)