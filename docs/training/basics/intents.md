---
title: https://developer.android.com/training/basics/intents
url: https://developer.android.com/training/basics/intents
source: md.txt
---

# Interact with other apps

An Android app typically has several[activities](https://developer.android.com/guide/components/activities). Each activity displays a user interface that lets the user perform a specific task, such as viewing a map or taking a photo. To take the user from one activity to another, your app must use an[Intent](https://developer.android.com/reference/android/content/Intent)to define your app's "intent" to do something. When you pass an`Intent`to the system with a method such as[startActivity()](https://developer.android.com/reference/android/app/Activity#startActivity(android.content.Intent)), the system uses the`Intent`to identify and start the appropriate app component. Using intents even lets your app start an activity that is contained in a separate app.

An`Intent`can be*explicit* , to start a specific[Activity](https://developer.android.com/reference/android/app/Activity)instance, or*implicit*, to start any component that can handle the intended action, such as "capture a photo."

The topics in this guide show you how to use an`Intent`to perform some basic interactions with other apps, such as starting another app, receiving a result from that app, and making your app able to respond to intents from other apps.

## Topics

**[Sending the user to another app](https://developer.android.com/training/basics/intents/sending)**
:   Shows you how to create implicit intents to launch other apps that can perform an action.

**[Get a result from an activity](https://developer.android.com/training/basics/intents/result)**
:   Shows you how to start another activity and receive a result from the activity.

**[Allow other apps to start your activity](https://developer.android.com/training/basics/intents/filters)**
:   Shows you how to make activities in your app open for use by other apps by defining intent filters that declare the implicit intents your app accepts.

**[Package visibility filtering on Android](https://developer.android.com/training/basics/intents/package-visibility)**
:   Shows you how to make other apps visible to your app if they aren't visible by default. Applies only to apps that target Android 11 (API level 30) or higher.

**[Fulfill common use cases while having limited package visibility](https://developer.android.com/training/basics/intents/package-visibility-use-cases)**
:   Shows several types of app interactions that might require you to update your app's manifest file so that other apps are visible to your app. Applies only to apps that target Android 11 (API level 30) or higher.

**[Limit loading in on-device Android containers](https://developer.android.com/training/basics/intents/limit-play-loading)**
:   Shows you how to limit your Play Store app from loading in a simulated Android environment app, also known as an on-device Android container.

For additional information about the topics on this page, see the following:

- [Sharing simple data](https://developer.android.com/training/sharing)
- [Sharing files](https://developer.android.com/training/secure-file-sharing)
- [Integrating Application with Intents](http://android-developers.blogspot.com/2009/11/integrating-application-with-intents.html)blog post
- [Intents and Intent Filters](https://developer.android.com/guide/components/intents-filters)