---
title: https://developer.android.com/training/run-background-service/create-service
url: https://developer.android.com/training/run-background-service/create-service
source: md.txt
---

# Create a background service

| **Note:** `IntentService`will not work correctly when the application is in the background on the latest versions of Android. This page is left here as reference for legacy apps only. See the[guide to background processing on Android](https://developer.android.com/guide/background)for recommended solutions.

The[IntentService](https://developer.android.com/reference/android/app/IntentService)class provides a straightforward structure for running an operation on a single background thread. This allows it to handle long-running operations without affecting your user interface's responsiveness. Also, an[IntentService](https://developer.android.com/reference/android/app/IntentService)isn't affected by most user interface lifecycle events, so it continues to run in circumstances that would shut down an[AsyncTask](https://developer.android.com/reference/android/os/AsyncTask)

An[IntentService](https://developer.android.com/reference/android/app/IntentService)has a few limitations:

- It can't interact directly with your user interface. To put its results in the UI, you have to send them to an[Activity](https://developer.android.com/reference/android/app/Activity).
- Work requests run sequentially. If an operation is running in an[IntentService](https://developer.android.com/reference/android/app/IntentService), and you send it another request, the request waits until the first operation is finished.
- An operation running on an[IntentService](https://developer.android.com/reference/android/app/IntentService)can't be interrupted.

However, in most cases an[IntentService](https://developer.android.com/reference/android/app/IntentService)is the preferred way to perform simple background operations.

This guide shows you how to do the following things:

- Create your own subclass of[IntentService](https://developer.android.com/reference/android/app/IntentService).
- Create the required callback method[onHandleIntent()](https://developer.android.com/reference/android/app/IntentService#onHandleIntent(android.content.Intent)).
- Define the[IntentService](https://developer.android.com/reference/android/app/IntentService)in your manifest file.

## Handle incoming intents

To create an[IntentService](https://developer.android.com/reference/android/app/IntentService)component for your app, define a class that extends[IntentService](https://developer.android.com/reference/android/app/IntentService), and within it, define a method that overrides[onHandleIntent()](https://developer.android.com/reference/android/app/IntentService#onHandleIntent(android.content.Intent)). For example:  

### Kotlin

```kotlin
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

```java
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

Notice that the other callbacks of a regular[Service](https://developer.android.com/reference/android/app/Service)component, such as[onStartCommand()](https://developer.android.com/reference/android/app/Service#onStartCommand(android.content.Intent, int, int))are automatically invoked by[IntentService](https://developer.android.com/reference/android/app/IntentService). In an[IntentService](https://developer.android.com/reference/android/app/IntentService), you should avoid overriding these callbacks.

To learn more about creating an`IntentService`, see[Extending the IntentService class](https://developer.android.com/guide/components/services#ExtendingIntentService).

## Define the intent service in the manifest

An[IntentService](https://developer.android.com/reference/android/app/IntentService)also needs an entry in your application manifest. Provide this entry as a[<service>](https://developer.android.com/guide/topics/manifest/service-element)element that's a child of the[<application>](https://developer.android.com/guide/topics/manifest/application-element)element:  

```xml
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

The attribute`android:name`specifies the class name of the[IntentService](https://developer.android.com/reference/android/app/IntentService).

Notice that the[<service>](https://developer.android.com/guide/topics/manifest/service-element)element doesn't contain an[intent filter](https://developer.android.com/guide/components/intents-filters). The[Activity](https://developer.android.com/reference/android/app/Activity)that sends work requests to the service uses an explicit[Intent](https://developer.android.com/reference/android/content/Intent), so no filter is needed. This also means that only components in the same app or other applications with the same user ID can access the service.

Now that you have the basic[IntentService](https://developer.android.com/reference/android/app/IntentService)class, you can send work requests to it with[Intent](https://developer.android.com/reference/android/content/Intent)objects. The procedure for constructing these objects and sending them to your[IntentService](https://developer.android.com/reference/android/app/IntentService)is described in[Send work requests to the background service](https://developer.android.com/training/run-background-service/send-request).