---
title: https://developer.android.com/training/run-background-service/report-status
url: https://developer.android.com/training/run-background-service/report-status
source: md.txt
---

| **Note:** This page is left here as reference for legacy apps only. See the [guide to background processing on Android](https://developer.android.com/guide/background) for recommended solutions.


This guide shows you how to report the status of a work request run in a background service
to the component that sent the request. This allows you, for example, to report the status of
the request in an [Activity](https://developer.android.com/reference/android/app/Activity) object's UI. The recommended way to send and
receive status is to use a [LocalBroadcastManager](https://developer.android.com/reference/androidx/localbroadcastmanager/content/LocalBroadcastManager), which
limits broadcast [Intent](https://developer.android.com/reference/android/content/Intent) objects to components in your own app.

## Report status from a JobIntentService


To send the status of a work request in an
[`JobIntentService`](https://developer.android.com/reference/androidx/core/app/JobIntentService) to other
components, first create an [Intent](https://developer.android.com/reference/android/content/Intent) that contains the status in its
extended data. As an option, you can add an action and data URI to this
[Intent](https://developer.android.com/reference/android/content/Intent).


Next, send the [Intent](https://developer.android.com/reference/android/content/Intent) by calling
[LocalBroadcastManager.sendBroadcast()](https://developer.android.com/reference/androidx/localbroadcastmanager/content/LocalBroadcastManager#sendBroadcast(android.content.Intent)). This sends the [Intent](https://developer.android.com/reference/android/content/Intent) to any
component in your application that has registered to receive it.
To get an instance of [LocalBroadcastManager](https://developer.android.com/reference/androidx/localbroadcastmanager/content/LocalBroadcastManager), call
[getInstance()](https://developer.android.com/reference/androidx/localbroadcastmanager/content/LocalBroadcastManager#getInstance(android.content.Context)).


For example:  

### Kotlin

```kotlin
...
// Defines a custom Intent action
const val BROADCAST_ACTION = "com.example.android.threadsample.BROADCAST"
...
// Defines the key for the status "extra" in an Intent
const val EXTENDED_DATA_STATUS = "com.example.android.threadsample.STATUS"
...
class RSSPullService : JobIntentService() {
    ...
    /*
     * Creates a new Intent containing a Uri object
     * BROADCAST_ACTION is a custom Intent action
     */
    val localIntent = Intent(BROADCAST_ACTION).apply {
        // Puts the status into the Intent
        putExtra(EXTENDED_DATA_STATUS, status)
    }
    // Broadcasts the Intent to receivers in this app.
    LocalBroadcastManager.getInstance(this).sendBroadcast(localIntent)
    ...
}
```

### Java

```java
public final class Constants {
    ...
    // Defines a custom Intent action
    public static final String BROADCAST_ACTION =
        "com.example.android.threadsample.BROADCAST";
    ...
    // Defines the key for the status "extra" in an Intent
    public static final String EXTENDED_DATA_STATUS =
        "com.example.android.threadsample.STATUS";
    ...
}
public class RSSPullService extends JobIntentService {
...
    /*
     * Creates a new Intent containing a Uri object
     * BROADCAST_ACTION is a custom Intent action
     */
    Intent localIntent =
            new Intent(Constants.BROADCAST_ACTION)
            // Puts the status into the Intent
            .putExtra(Constants.EXTENDED_DATA_STATUS, status);
    // Broadcasts the Intent to receivers in this app.
    LocalBroadcastManager.getInstance(this).sendBroadcast(localIntent);
...
}
```


The next step is to handle the incoming broadcast [Intent](https://developer.android.com/reference/android/content/Intent) objects in
the component that sent the original work request.

## Receive status broadcasts from a JobIntentService


To receive broadcast [Intent](https://developer.android.com/reference/android/content/Intent) objects, use a subclass of
[BroadcastReceiver](https://developer.android.com/reference/android/content/BroadcastReceiver). In the subclass, implement the
[BroadcastReceiver.onReceive()](https://developer.android.com/reference/android/content/BroadcastReceiver#onReceive(android.content.Context, android.content.Intent)) callback
method, which [LocalBroadcastManager](https://developer.android.com/reference/androidx/localbroadcastmanager/content/LocalBroadcastManager) invokes when it receives
an [Intent](https://developer.android.com/reference/android/content/Intent). [LocalBroadcastManager](https://developer.android.com/reference/androidx/localbroadcastmanager/content/LocalBroadcastManager)
passes the incoming [Intent](https://developer.android.com/reference/android/content/Intent) to
[BroadcastReceiver.onReceive()](https://developer.android.com/reference/android/content/BroadcastReceiver#onReceive(android.content.Context, android.content.Intent)).


For example:  

### Kotlin

```kotlin
// Broadcast receiver for receiving status updates from the IntentService.
private class DownloadStateReceiver : BroadcastReceiver() {

    override fun onReceive(context: Context, intent: Intent) {
        ...
        /*
         * Handle Intents here.
         */
        ...
    }
}
```

### Java

```java
// Broadcast receiver for receiving status updates from the IntentService.
private class DownloadStateReceiver extends BroadcastReceiver
{
    // Called when the BroadcastReceiver gets an Intent it's registered to receive
    @Override
    public void onReceive(Context context, Intent intent) {
...
        /*
         * Handle Intents here.
         */
...
    }
}
```


Once you've defined the [BroadcastReceiver](https://developer.android.com/reference/android/content/BroadcastReceiver), you can define filters
for it that match specific actions, categories, and data. To do this, create
an [IntentFilter](https://developer.android.com/reference/android/content/IntentFilter). This first snippet shows how to define the filter:  

### Kotlin

```kotlin
// Class that displays photos
class DisplayActivity : FragmentActivity() {
    ...
    override fun onCreate(savedInstanceState: Bundle?) {
        ...
        super.onCreate(savedInstanceState)
        ...
        // The filter's action is BROADCAST_ACTION
        var statusIntentFilter = IntentFilter(BROADCAST_ACTION).apply {
            // Adds a data filter for the HTTP scheme
            addDataScheme("http")
        }
        ...
```

### Java

```java
// Class that displays photos
public class DisplayActivity extends FragmentActivity {
    ...
    public void onCreate(Bundle stateBundle) {
        ...
        super.onCreate(stateBundle);
        ...
        // The filter's action is BROADCAST_ACTION
        IntentFilter statusIntentFilter = new IntentFilter(
                Constants.BROADCAST_ACTION);

        // Adds a data filter for the HTTP scheme
        statusIntentFilter.addDataScheme("http");
        ...
```


To register the [BroadcastReceiver](https://developer.android.com/reference/android/content/BroadcastReceiver) and the
[IntentFilter](https://developer.android.com/reference/android/content/IntentFilter) with the system, get an instance of
[LocalBroadcastManager](https://developer.android.com/reference/androidx/localbroadcastmanager/content/LocalBroadcastManager) and call its
[registerReceiver()](https://developer.android.com/reference/androidx/localbroadcastmanager/content/LocalBroadcastManager#registerReceiver(android.content.BroadcastReceiver, android.content.IntentFilter))
method. This next snippet shows how to register the [BroadcastReceiver](https://developer.android.com/reference/android/content/BroadcastReceiver)
and its [IntentFilter](https://developer.android.com/reference/android/content/IntentFilter):  

### Kotlin

```kotlin
        // Instantiates a new DownloadStateReceiver
        val downloadStateReceiver = DownloadStateReceiver()
        // Registers the DownloadStateReceiver and its intent filters
        LocalBroadcastManager.getInstance(this)
                .registerReceiver(downloadStateReceiver, statusIntentFilter)
        ...
```

### Java

```java
        // Instantiates a new DownloadStateReceiver
        DownloadStateReceiver downloadStateReceiver =
                new DownloadStateReceiver();
        // Registers the DownloadStateReceiver and its intent filters
        LocalBroadcastManager.getInstance(this).registerReceiver(
                downloadStateReceiver,
                statusIntentFilter);
        ...
```


A single [BroadcastReceiver](https://developer.android.com/reference/android/content/BroadcastReceiver) can handle more than one type of broadcast
[Intent](https://developer.android.com/reference/android/content/Intent) object, each with its own action. This feature allows you to
run different code for each action, without having to define a separate
[BroadcastReceiver](https://developer.android.com/reference/android/content/BroadcastReceiver) for each action. To define another
[IntentFilter](https://developer.android.com/reference/android/content/IntentFilter) for the same
[BroadcastReceiver](https://developer.android.com/reference/android/content/BroadcastReceiver), create the [IntentFilter](https://developer.android.com/reference/android/content/IntentFilter) and
repeat the call to
[registerReceiver()](https://developer.android.com/reference/androidx/localbroadcastmanager/content/LocalBroadcastManager#registerReceiver(android.content.BroadcastReceiver, android.content.IntentFilter)).
For example:  

### Kotlin

```kotlin
        /*
         * Instantiates a new action filter.
         * No data filter is needed.
         */
        statusIntentFilter = IntentFilter(ACTION_ZOOM_IMAGE)
        // Registers the receiver with the new filter
        LocalBroadcastManager.getInstance(this)
                .registerReceiver(downloadStateReceiver, statusIntentFilter)
```

### Java

```java
        /*
         * Instantiates a new action filter.
         * No data filter is needed.
         */
        statusIntentFilter = new IntentFilter(Constants.ACTION_ZOOM_IMAGE);
        // Registers the receiver with the new filter
        LocalBroadcastManager.getInstance(this).registerReceiver(
                downloadStateReceiver,
                statusIntentFilter);
```


Sending a broadcast [Intent](https://developer.android.com/reference/android/content/Intent) doesn't start or resume an
[Activity](https://developer.android.com/reference/android/app/Activity). The [BroadcastReceiver](https://developer.android.com/reference/android/content/BroadcastReceiver) for an
[Activity](https://developer.android.com/reference/android/app/Activity) receives and processes [Intent](https://developer.android.com/reference/android/content/Intent) objects even
when your app is in the background, but doesn't force your app to the foreground. If you
want to notify the user about an event that happened in the background while your app was not
visible, use a [Notification](https://developer.android.com/reference/android/app/Notification). *Never* start an
[Activity](https://developer.android.com/reference/android/app/Activity) in response to an incoming broadcast
[Intent](https://developer.android.com/reference/android/content/Intent).