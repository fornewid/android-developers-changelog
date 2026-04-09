---
title: Report work status  |  Android Developers
url: https://developer.android.com/training/run-background-service/report-status
source: html-scrape
---

* [Android Developers](https://developer.android.com/)

# Report work status Stay organized with collections Save and categorize content based on your preferences.




**Note:** This page is left here as reference for legacy apps only.
See the [guide to background processing on Android](/guide/background)  for recommended
solutions.

This guide shows you how to report the status of a work request run in a background service
to the component that sent the request. This allows you, for example, to report the status of
the request in an `Activity` object's UI. The recommended way to send and
receive status is to use a `LocalBroadcastManager`, which
limits broadcast `Intent` objects to components in your own app.

## Report status from a JobIntentService

To send the status of a work request in an
[`JobIntentService`](/reference/androidx/core/app/JobIntentService) to other
components, first create an `Intent` that contains the status in its
extended data. As an option, you can add an action and data URI to this
`Intent`.

Next, send the `Intent` by calling
`LocalBroadcastManager.sendBroadcast()`. This sends the `Intent` to any
component in your application that has registered to receive it.
To get an instance of `LocalBroadcastManager`, call
`getInstance()`.

For example:

### Kotlin

```
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

```
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

The next step is to handle the incoming broadcast `Intent` objects in
the component that sent the original work request.

## Receive status broadcasts from a JobIntentService

To receive broadcast `Intent` objects, use a subclass of
`BroadcastReceiver`. In the subclass, implement the
`BroadcastReceiver.onReceive()` callback
method, which `LocalBroadcastManager` invokes when it receives
an `Intent`. `LocalBroadcastManager`
passes the incoming `Intent` to
`BroadcastReceiver.onReceive()`.

For example:

### Kotlin

```
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

```
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

Once you've defined the `BroadcastReceiver`, you can define filters
for it that match specific actions, categories, and data. To do this, create
an `IntentFilter`. This first snippet shows how to define the filter:

### Kotlin

```
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

```
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

To register the `BroadcastReceiver` and the
`IntentFilter` with the system, get an instance of
`LocalBroadcastManager` and call its
`registerReceiver()`
method. This next snippet shows how to register the `BroadcastReceiver`
and its `IntentFilter`:

### Kotlin

```
        // Instantiates a new DownloadStateReceiver
        val downloadStateReceiver = DownloadStateReceiver()
        // Registers the DownloadStateReceiver and its intent filters
        LocalBroadcastManager.getInstance(this)
                .registerReceiver(downloadStateReceiver, statusIntentFilter)
        ...
```

### Java

```
        // Instantiates a new DownloadStateReceiver
        DownloadStateReceiver downloadStateReceiver =
                new DownloadStateReceiver();
        // Registers the DownloadStateReceiver and its intent filters
        LocalBroadcastManager.getInstance(this).registerReceiver(
                downloadStateReceiver,
                statusIntentFilter);
        ...
```

A single `BroadcastReceiver` can handle more than one type of broadcast
`Intent` object, each with its own action. This feature allows you to
run different code for each action, without having to define a separate
`BroadcastReceiver` for each action. To define another
`IntentFilter` for the same
`BroadcastReceiver`, create the `IntentFilter` and
repeat the call to
`registerReceiver()`.
For example:

### Kotlin

```
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

```
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

Sending a broadcast `Intent` doesn't start or resume an
`Activity`. The `BroadcastReceiver` for an
`Activity` receives and processes `Intent` objects even
when your app is in the background, but doesn't force your app to the foreground. If you
want to notify the user about an event that happened in the background while your app was not
visible, use a `Notification`. *Never* start an
`Activity` in response to an incoming broadcast
`Intent`.