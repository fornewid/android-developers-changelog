---
title: https://developer.android.com/training/package-visibility/automatic
url: https://developer.android.com/training/package-visibility/automatic
source: md.txt
---

The system automatically makes some apps visible so that your app
can interact with them without needing to declare the
[`<queries>`](https://developer.android.com/guide/topics/manifest/queries-element) element. This behavior
helps support basic functionality and common use cases.
| **Note:** You can start another app's activity using either an [implicit](https://developer.android.com/guide/components/intents-filters#ExampleSend) or [explicit](https://developer.android.com/guide/components/intents-filters#ExampleExplicit) intent regardless of whether that app is visible to your app. Also, if your app targets Android 10 (API level 29) or lower, **all** apps are visible to your app automatically.

## Types of apps that are visible automatically

The following types of apps are always visible to your app, even when your app
targets Android 11 (API level 30) or higher:

- Your own app.
- [Certain system packages](https://developer.android.com/training/package-visibility/automatic#system-packages-visible-automatically), such as the media provider, that implement core Android functionality.
- The app that installed your app.
- Any app that launches an activity in your app using the [`startActivityForResult()`](https://developer.android.com/reference/kotlin/android/app/Activity#startactivityforresult) method, as described in the guide about [getting a result from an
  activity](https://developer.android.com/training/basics/intents/result).
- Any app that starts or binds to a [service](https://developer.android.com/guide/components/services) in your app.
- Any app that accesses a [content
  provider](https://developer.android.com/guide/topics/providers/content-providers) in your app.
- Any app that has a content provider that your app has been [granted URI
  permissions](https://developer.android.com/guide/topics/providers/content-provider-basics#getting-access-with-temporary-permissions) to access.
- Any app that receives input from your app. This case applies only when your app provides input as an [input method
  editor](https://developer.android.com/guide/topics/text/creating-input-method).

## System packages that are visible automatically

Some system packages that implement core Android functionality are automatically
visible to your app, even when your app targets Android 11 or
higher. The specific set of packages depends on the device that runs your app.

To view the full list of packages for a specific device, run the following
command in a terminal on your development machine:  

```
adb shell dumpsys package queries
```

In the command output, find the `forceQueryable` section. This section includes
the list of packages that the device has made visible to your app automatically.