---
title: Know which packages are visible automatically  |  App architecture  |  Android Developers
url: https://developer.android.com/training/package-visibility/automatic
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [App architecture](https://developer.android.com/topic/architecture/intro)

# Know which packages are visible automatically Stay organized with collections Save and categorize content based on your preferences.




The system automatically makes some apps visible so that your app
can interact with them without needing to declare the
[`<queries>`](/guide/topics/manifest/queries-element) element. This behavior
helps support basic functionality and common use cases.

**Note:** You can start another app's activity using either an
[implicit](/guide/components/intents-filters#ExampleSend) or
[explicit](/guide/components/intents-filters#ExampleExplicit) intent regardless
of whether that app is visible to your app. Also, if your app targets
Android 10 (API level 29) or lower, **all** apps are visible to your app
automatically.

## Types of apps that are visible automatically

The following types of apps are always visible to your app, even when your app
targets Android 11 (API level 30) or higher:

* Your own app.
* [Certain system packages](#system-packages-visible-automatically), such as the
  media provider, that implement core Android functionality.
* The app that installed your app.
* Any app that launches an activity in your app using the
  [`startActivityForResult()`](/reference/kotlin/android/app/Activity#startactivityforresult) method,
  as described in the guide about [getting a result from an
  activity](/training/basics/intents/result).
* Any app that starts or binds to a [service](/guide/components/services) in
  your app.
* Any app that accesses a [content
  provider](/guide/topics/providers/content-providers) in your app.
* Any app that has a content provider that your app has been [granted URI
  permissions](/guide/topics/providers/content-provider-basics#getting-access-with-temporary-permissions)
  to access.
* Any app that receives input from your app. This case applies only when your
  app provides input as an [input method
  editor](/guide/topics/text/creating-input-method).

## System packages that are visible automatically

Some system packages that implement core Android functionality are automatically
visible to your app, even when your app targets Android 11 or
higher. The specific set of packages depends on the device that runs your app.

To view the full list of packages for a specific device, run the following
command in a terminal on your development machine:

```
adb shell dumpsys package queries
```

In the command output, find the `forceQueryable` section. This section includes
the list of packages that the device has made visible to your app automatically.

[Previous

arrow\_back

About package visibility](/training/package-visibility)

[Next

Declare package visibility needs

arrow\_forward](/training/package-visibility/declaring)