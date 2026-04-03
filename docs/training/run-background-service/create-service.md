---
title: Create a background service  |  Android Developers
url: https://developer.android.com/training/run-background-service/create-service
source: html-scrape
---

* [Android Developers](https://developer.android.com/)

# Create a background service Stay organized with collections Save and categorize content based on your preferences.



**Note:** `IntentService` will not work correctly when the
application is in the background on the latest versions of Android. This page is left here as
reference for legacy apps only. See the [guide to background processing
on Android](/guide/background)  for recommended solutions.

The `IntentService` class provides a straightforward structure for running
an operation on a single background thread. This allows it to handle long-running operations
without affecting your user interface's responsiveness. Also, an
`IntentService` isn't affected by most user interface lifecycle events, so it
continues to run in circumstances that would shut down an `AsyncTask`

An `IntentService` has a few limitations:

* It can't interact directly with your user interface. To put its results in the UI, you
  have to send them to an `Activity`.
* Work requests run sequentially. If an operation is running in an
  `IntentService`, and you send it another request, the request waits until
  the first operation is finished.
* An operation running on an `IntentService` can't be interrupted.

However, in most cases an `IntentService` is the preferred way to perform
simple background operations.

This guide shows you how to do the following things:

* Create your own subclass of `IntentService`.
* Create the required callback method `onHandleIntent()`.
* Define the `IntentService`
  in your manifest file.

## Handle incoming intents

To create an `IntentService` component for your app, define a class that
extends `IntentService`, and within it, define a method that
overrides `onHandleIntent()`. For example:

### Kotlin

```
class RSSPullService : IntentService(RSSPullService::class.simpleName)

    override fun onHandleIntent(workIntent: Intent) {
        // Gets data from the incoming Intent
        val dataString = workIntent.dataString
        ...
        // Do work here, based on the contents of dataString
        ...
    }
}
```

### Java

```
public class RSSPullService extends IntentService {
    @Override
    protected void onHandleIntent(Intent workIntent) {
        // Gets data from the incoming Intent
        String dataString = workIntent.getDataString();
        ...
        // Do work here, based on the contents of dataString
        ...
    }
}
```

Notice that the other callbacks of a regular `Service` component, such as
`onStartCommand()` are automatically invoked by
`IntentService`. In an `IntentService`, you should avoid
overriding these callbacks.

To learn more about creating an `IntentService`, see [Extending the
IntentService class](/guide/components/services#ExtendingIntentService).

## Define the intent service in the manifest

An `IntentService` also needs an entry in your application manifest.
Provide this entry as a
`<service>`
element that's a child of the
`<application>` element:

```
    <application
        android:icon="@drawable/icon"
        android:label="@string/app_name">
        ...
        <!--
            Because android:exported is set to "false",
            the service is only available to this app.
        -->
        <service
            android:name=".RSSPullService"
            android:exported="false"/>
        ...
    </application>
```

The attribute `android:name` specifies the class name of the
`IntentService`.

Notice that the
`<service>`
element doesn't contain an
[intent filter](/guide/components/intents-filters). The
`Activity` that sends work requests to the service uses an
explicit `Intent`, so no filter is needed. This also
means that only components in the same app or other applications with the
same user ID can access the service.

Now that you have the basic `IntentService` class, you can send work requests
to it with `Intent` objects. The procedure for constructing these objects
and sending them to your `IntentService` is described in
[Send work requests to the background service](/training/run-background-service/send-request).