---
title: https://developer.android.com/training/sync-adapters/running-sync-adapter
url: https://developer.android.com/training/sync-adapters/running-sync-adapter
source: md.txt
---

**Note:** We recommended [WorkManager](https://developer.android.com/topic/libraries/architecture/workmanager)
as the recommended solution for most background processing use cases. Please reference the
[background processing guide](https://developer.android.com/guide/background) to learn which solution works best for you.


In the previous lessons in this class, you learned how to create a sync adapter component that
encapsulates data transfer code, and how to add the additional components that allow you to
plug the sync adapter into the system. You now have everything you need to install an app that
includes a sync adapter, but none of the code you've seen actually runs the sync adapter.


You should try to run your sync adapter based on a schedule or as the indirect result of some
event. For example, you may want your sync adapter to run on a regular schedule, either after a
certain period of time or at a particular time of the day. You may also want to run your sync
adapter when there are changes to data stored on the device. You should avoid running your
sync adapter as the direct result of a user action, because by doing this you don't get the full
benefit of the sync adapter framework's scheduling ability. For example, you should avoid
providing a refresh button in your user interface.


You have the following options for running your sync adapter:


When server data changes
:
    Run the sync adapter in response to a message from a server, indicating that server-based
    data has changed. This option allows you to refresh data from the server to the device
    without degrading performance or wasting battery life by polling the server.

When device data changes
:
    Run a sync adapter when data changes on the device. This option allows you to send
    modified data from the device to a server, and is especially useful if you need to ensure
    that the server always has the latest device data. This option is straightforward to
    implement if you actually store data in your content provider. If you're using a stub
    content provider, detecting data changes may be more difficult.


At regular intervals
:
    Run a sync adapter after the expiration of an interval you choose, or run it at a certain
    time every day.

On demand
:
    Run the sync adapter in response to a user action. However, to provide the best user
    experience you should rely primarily on one of the more automated options. By using
    automated options, you conserve battery and network resources.


The rest of this lesson describes each of the options in more detail.

## Run the sync adapter when server data changes


If your app transfers data from a server and the server data changes frequently, you can use
a sync adapter to do downloads in response to data changes. To run the sync adapter, have
the server send a special message to a [BroadcastReceiver](https://developer.android.com/reference/android/content/BroadcastReceiver) in your app.
In response to this message, call [ContentResolver.requestSync()](https://developer.android.com/reference/android/content/ContentResolver#requestSync(android.accounts.Account, java.lang.String, android.os.Bundle)) to signal the sync adapter framework to run your
sync adapter.


[Google Cloud Messaging](https://developer.android.com/google/gcm) (GCM) provides both the
server and device components you need to make this messaging system work. Using GCM to trigger
transfers is more reliable and more efficient than polling servers for status. While polling
requires a [Service](https://developer.android.com/reference/android/app/Service) that is always active, GCM uses a
[BroadcastReceiver](https://developer.android.com/reference/android/content/BroadcastReceiver) that's activated when a message arrives. While polling
at regular intervals uses battery power even if no updates are available, GCM only sends
messages when needed.


**Note:** If you use GCM to trigger your sync adapter via a broadcast to all
devices where your app is installed, remember that they receive your message at
roughly the same time. This situation can cause multiple instance of your sync adapter to run
at the same time, causing server and network overload. To avoid this situation for a broadcast
to all devices, you should consider deferring the start of the sync adapter for a period
that's unique for each device.


The following code snippet shows you how to run
[requestSync()](https://developer.android.com/reference/android/content/ContentResolver#requestSync(android.accounts.Account, java.lang.String, android.os.Bundle)) in response to an
incoming GCM message:  

### Kotlin

```kotlin
...
// Constants
// Content provider authority
const val AUTHORITY = "com.example.android.datasync.provider"
// Account type
const val ACCOUNT_TYPE = "com.example.android.datasync"
// Account
const val ACCOUNT = "default_account"
// Incoming Intent key for extended data
const val KEY_SYNC_REQUEST = "com.example.android.datasync.KEY_SYNC_REQUEST"
...
class GcmBroadcastReceiver : BroadcastReceiver() {
    ...
    override fun onReceive(context: Context, intent: Intent) {
        // Get a GCM object instance
        val gcm: GoogleCloudMessaging = GoogleCloudMessaging.getInstance(context)
        // Get the type of GCM message
        val messageType: String? = gcm.getMessageType(intent)
        /*
         * Test the message type and examine the message contents.
         * Since GCM is a general-purpose messaging system, you
         * may receive normal messages that don't require a sync
         * adapter run.
         * The following code tests for a a boolean flag indicating
         * that the message is requesting a transfer from the device.
         */
        if (GoogleCloudMessaging.MESSAGE_TYPE_MESSAGE == messageType
            && intent.getBooleanExtra(KEY_SYNC_REQUEST, false)) {
            /*
             * Signal the framework to run your sync adapter. Assume that
             * app initialization has already created the account.
             */
            ContentResolver.requestSync(mAccount, AUTHORITY, null)
            ...
        }
        ...
    }
    ...
}
```

### Java

```java
public class GcmBroadcastReceiver extends BroadcastReceiver {
    ...
    // Constants
    // Content provider authority
    public static final String AUTHORITY = "com.example.android.datasync.provider";
    // Account type
    public static final String ACCOUNT_TYPE = "com.example.android.datasync";
    // Account
    public static final String ACCOUNT = "default_account";
    // Incoming Intent key for extended data
    public static final String KEY_SYNC_REQUEST =
            "com.example.android.datasync.KEY_SYNC_REQUEST";
    ...
    @Override
    public void onReceive(Context context, Intent intent) {
        // Get a GCM object instance
        GoogleCloudMessaging gcm =
                GoogleCloudMessaging.getInstance(context);
        // Get the type of GCM message
        String messageType = gcm.getMessageType(intent);
        /*
         * Test the message type and examine the message contents.
         * Since GCM is a general-purpose messaging system, you
         * may receive normal messages that don't require a sync
         * adapter run.
         * The following code tests for a a boolean flag indicating
         * that the message is requesting a transfer from the device.
         */
        if (GoogleCloudMessaging.MESSAGE_TYPE_MESSAGE.equals(messageType)
            &&
            intent.getBooleanExtra(KEY_SYNC_REQUEST)) {
            /*
             * Signal the framework to run your sync adapter. Assume that
             * app initialization has already created the account.
             */
            ContentResolver.requestSync(mAccount, AUTHORITY, null);
            ...
        }
        ...
    }
    ...
}
```

## Run the sync adapter when content provider data changes


If your app collects data in a content provider, and you want to update the server whenever
you update the provider, you can set up your app to run your sync adapter automatically. To do
this, you register an observer for the content provider. When data in your content provider
changes, the content provider framework calls the observer. In the observer, call
[requestSync()](https://developer.android.com/reference/android/content/ContentResolver#requestSync(android.accounts.Account, java.lang.String, android.os.Bundle)) to tell the framework to run
your sync adapter.


**Note:** If you're using a stub content provider, you don't have any data in
the content provider and [onChange()](https://developer.android.com/reference/android/database/ContentObserver#onChange(boolean)) is
never called. In this case, you have to provide your own mechanism for detecting changes to
device data. This mechanism is also responsible for calling
[requestSync()](https://developer.android.com/reference/android/content/ContentResolver#requestSync(android.accounts.Account, java.lang.String, android.os.Bundle)) when the data changes.


To create an observer for your content provider, extend the class
[ContentObserver](https://developer.android.com/reference/android/database/ContentObserver) and implement both forms of its
[onChange()](https://developer.android.com/reference/android/database/ContentObserver#onChange(boolean)) method. In
[onChange()](https://developer.android.com/reference/android/database/ContentObserver#onChange(boolean)), call
[requestSync()](https://developer.android.com/reference/android/content/ContentResolver#requestSync(android.accounts.Account, java.lang.String, android.os.Bundle)) to start the sync adapter.


To register the observer, pass it as an argument in a call to
[registerContentObserver()](https://developer.android.com/reference/android/content/ContentResolver#registerContentObserver(android.net.Uri, boolean, android.database.ContentObserver)). In
this call, you also have to pass in a content URI for the data you want to watch. The content
provider framework compares this watch URI to content URIs passed in as arguments to
[ContentResolver](https://developer.android.com/reference/android/content/ContentResolver) methods that modify your provider, such as
[ContentResolver.insert()](https://developer.android.com/reference/android/content/ContentResolver#insert(android.net.Uri, android.content.ContentValues)). If there's a match, your
implementation of [ContentObserver.onChange()](https://developer.android.com/reference/android/database/ContentObserver#onChange(boolean))
is called.


The following code snippet shows you how to define a [ContentObserver](https://developer.android.com/reference/android/database/ContentObserver)
that calls [requestSync()](https://developer.android.com/reference/android/content/ContentResolver#requestSync(android.accounts.Account, java.lang.String, android.os.Bundle)) when a table
changes:  

### Kotlin

```kotlin
// Constants
// Content provider scheme
const val SCHEME = "content://"
// Content provider authority
const val AUTHORITY = "com.example.android.datasync.provider"
// Path for the content provider table
const val TABLE_PATH = "data_table"
...
class MainActivity : FragmentActivity() {
    ...
    // A content URI for the content provider's data table
    private lateinit var uri: Uri
    // A content resolver for accessing the provider
    private lateinit var mResolver: ContentResolver
    ...
    inner class TableObserver(...) : ContentObserver(...) {
        /*
         * Define a method that's called when data in the
         * observed content provider changes.
         * This method signature is provided for compatibility with
         * older platforms.
         */
        override fun onChange(selfChange: Boolean) {
            /*
             * Invoke the method signature available as of
             * Android platform version 4.1, with a null URI.
             */
            onChange(selfChange, null)
        }

        /*
         * Define a method that's called when data in the
         * observed content provider changes.
         */
        override fun onChange(selfChange: Boolean, changeUri: Uri?) {
            /*
             * Ask the framework to run your sync adapter.
             * To maintain backward compatibility, assume that
             * changeUri is null.
             */
            ContentResolver.requestSync(account, AUTHORITY, null)
        }
        ...
    }
    ...
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        ...
        // Get the content resolver object for your app
        mResolver = contentResolver
        // Construct a URI that points to the content provider data table
        uri = Uri.Builder()
                .scheme(SCHEME)
                .authority(AUTHORITY)
                .path(TABLE_PATH)
                .build()
        /*
         * Create a content observer object.
         * Its code does not mutate the provider, so set
         * selfChange to "false"
         */
        val observer = TableObserver(false)
        /*
         * Register the observer for the data table. The table's path
         * and any of its subpaths trigger the observer.
         */
        mResolver.registerContentObserver(uri, true, observer)
        ...
    }
    ...
}
```

### Java

```java
public class MainActivity extends FragmentActivity {
    ...
    // Constants
    // Content provider scheme
    public static final String SCHEME = "content://";
    // Content provider authority
    public static final String AUTHORITY = "com.example.android.datasync.provider";
    // Path for the content provider table
    public static final String TABLE_PATH = "data_table";
    // Account
    public static final String ACCOUNT = "default_account";
    // Global variables
    // A content URI for the content provider's data table
    Uri uri;
    // A content resolver for accessing the provider
    ContentResolver mResolver;
    ...
    public class TableObserver extends ContentObserver {
        /*
         * Define a method that's called when data in the
         * observed content provider changes.
         * This method signature is provided for compatibility with
         * older platforms.
         */
        @Override
        public void onChange(boolean selfChange) {
            /*
             * Invoke the method signature available as of
             * Android platform version 4.1, with a null URI.
             */
            onChange(selfChange, null);
        }
        /*
         * Define a method that's called when data in the
         * observed content provider changes.
         */
        @Override
        public void onChange(boolean selfChange, Uri changeUri) {
            /*
             * Ask the framework to run your sync adapter.
             * To maintain backward compatibility, assume that
             * changeUri is null.
             */
            ContentResolver.requestSync(mAccount, AUTHORITY, null);
        }
        ...
    }
    ...
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        ...
        // Get the content resolver object for your app
        mResolver = getContentResolver();
        // Construct a URI that points to the content provider data table
        uri = new Uri.Builder()
                  .scheme(SCHEME)
                  .authority(AUTHORITY)
                  .path(TABLE_PATH)
                  .build();
        /*
         * Create a content observer object.
         * Its code does not mutate the provider, so set
         * selfChange to "false"
         */
        TableObserver observer = new TableObserver(false);
        /*
         * Register the observer for the data table. The table's path
         * and any of its subpaths trigger the observer.
         */
        mResolver.registerContentObserver(uri, true, observer);
        ...
    }
    ...
}
```

## Run the sync adapter periodically


You can run your sync adapter periodically by setting a period of time to wait between runs,
or by running it at certain times of the day, or both. Running your sync adapter
periodically allows you to roughly match the update interval of your server.


Similarly, you can upload data from the device when your server is relatively idle, by
scheduling your sync adapter to run at night. Most users leave their powered on and plugged in
at night, so this time is usually available. Moreover, the device is not running other tasks at
the same time as your sync adapter. If you take this approach, however, you need to ensure that
each device triggers a data transfer at a slightly different time. If all devices run your
sync adapter at the same time, you are likely to overload your server and cell provider data
networks.


In general, periodic runs make sense if your users don't need instant updates, but expect to
have regular updates. Periodic runs also make sense if you want to balance the availability of
up-to-date data with the efficiency of smaller sync adapter runs that don't over-use device
resources.


To run your sync adapter at regular intervals, call
[addPeriodicSync()](https://developer.android.com/reference/android/content/ContentResolver#addPeriodicSync(android.accounts.Account, java.lang.String, android.os.Bundle, long)). This schedules your
sync adapter to run after a certain amount of time has elapsed. Since the sync adapter framework
has to account for other sync adapter executions and tries to maximize battery efficiency, the
elapsed time may vary by a few seconds. Also, the framework won't run your sync adapter if the
network is not available.


Notice that [addPeriodicSync()](https://developer.android.com/reference/android/content/ContentResolver#addPeriodicSync(android.accounts.Account, java.lang.String, android.os.Bundle, long)) doesn't
run the sync adapter at a particular time of day. To run your sync adapter at roughly the
same time every day, use a repeating alarm as a trigger. Repeating alarms are described in more
detail in the reference documentation for [AlarmManager](https://developer.android.com/reference/android/app/AlarmManager). If you use the
method [setInexactRepeating()](https://developer.android.com/reference/android/app/AlarmManager#setInexactRepeating(int, long, long, android.app.PendingIntent)) to set
time-of-day triggers that have some variation, you should still randomize the start time to
ensure that sync adapter runs from different devices are staggered.


The method [addPeriodicSync()](https://developer.android.com/reference/android/content/ContentResolver#addPeriodicSync(android.accounts.Account, java.lang.String, android.os.Bundle, long)) doesn't
disable [setSyncAutomatically()](https://developer.android.com/reference/android/content/ContentResolver#setSyncAutomatically(android.accounts.Account, java.lang.String, boolean)),
so you may get multiple sync runs in a relatively short period of time. Also, only a few
sync adapter control flags are allowed in a call to
[addPeriodicSync()](https://developer.android.com/reference/android/content/ContentResolver#addPeriodicSync(android.accounts.Account, java.lang.String, android.os.Bundle, long)); the flags that are
not allowed are described in the referenced documentation for
[addPeriodicSync()](https://developer.android.com/reference/android/content/ContentResolver#addPeriodicSync(android.accounts.Account, java.lang.String, android.os.Bundle, long)).


The following code snippet shows you how to schedule periodic sync adapter runs:  

### Kotlin

```kotlin
// Content provider authority
const val AUTHORITY = "com.example.android.datasync.provider"
// Account
const val ACCOUNT = "default_account"
// Sync interval constants
const val SECONDS_PER_MINUTE = 60L
const val SYNC_INTERVAL_IN_MINUTES = 60L
const val SYNC_INTERVAL = SYNC_INTERVAL_IN_MINUTES * SECONDS_PER_MINUTE
...
class MainActivity : FragmentActivity() {
    ...
    // A content resolver for accessing the provider
    private lateinit var mResolver: ContentResolver

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        ...
        // Get the content resolver for your app
        mResolver = contentResolver
        /*
         * Turn on periodic syncing
         */
        ContentResolver.addPeriodicSync(
                mAccount,
                AUTHORITY,
                Bundle.EMPTY,
                SYNC_INTERVAL)
        ...
    }
    ...
}
```

### Java

```java
public class MainActivity extends FragmentActivity {
    ...
    // Constants
    // Content provider authority
    public static final String AUTHORITY = "com.example.android.datasync.provider";
    // Account
    public static final String ACCOUNT = "default_account";
    // Sync interval constants
    public static final long SECONDS_PER_MINUTE = 60L;
    public static final long SYNC_INTERVAL_IN_MINUTES = 60L;
    public static final long SYNC_INTERVAL =
            SYNC_INTERVAL_IN_MINUTES *
            SECONDS_PER_MINUTE;
    // Global variables
    // A content resolver for accessing the provider
    ContentResolver mResolver;
    ...
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        ...
        // Get the content resolver for your app
        mResolver = getContentResolver();
        /*
         * Turn on periodic syncing
         */
        ContentResolver.addPeriodicSync(
                mAccount,
                AUTHORITY,
                Bundle.EMPTY,
                SYNC_INTERVAL);
        ...
    }
    ...
}
```

## Run the sync adapter on demand


Running your sync adapter in response to a user request is the least preferable strategy
for running a sync adapter. The framework is specifically designed to conserve battery power
when it runs sync adapters according to a schedule. Options that run a sync in response to data
changes use battery power effectively, since the power is used to provide new data.


In comparison, allowing users to run a sync on demand means that the sync runs by itself, which
is inefficient use of network and power resources. Also, providing sync on demand leads users to
request a sync even if there's no evidence that the data has changed, and running a sync that
doesn't refresh data is an ineffective use of battery power. In general, your app should either
use other signals to trigger a sync or schedule them at regular intervals, without user input.


However, if you still want to run the sync adapter on demand, set the sync adapter flags for a
manual sync adapter run, then call
[ContentResolver.requestSync()](https://developer.android.com/reference/android/content/ContentResolver#requestSync(android.accounts.Account, java.lang.String, android.os.Bundle)).


Run on demand transfers with the following flags:


[SYNC_EXTRAS_MANUAL](https://developer.android.com/reference/android/content/ContentResolver#SYNC_EXTRAS_MANUAL)
:
    Forces a manual sync. The sync adapter framework ignores the existing settings,
    such as the flag set by [setSyncAutomatically()](https://developer.android.com/reference/android/content/ContentResolver#setSyncAutomatically(android.accounts.Account, java.lang.String, boolean)).


[SYNC_EXTRAS_EXPEDITED](https://developer.android.com/reference/android/content/ContentResolver#SYNC_EXTRAS_EXPEDITED)
:
    Forces the sync to start immediately. If you don't set this, the system may wait several
    seconds before running the sync request, because it tries to optimize battery use by
    scheduling many requests in a short period of time.


The following code snippet shows you how to call
[requestSync()](https://developer.android.com/reference/android/content/ContentResolver#requestSync(android.accounts.Account, java.lang.String, android.os.Bundle)) in response to a button
click:  

### Kotlin

```kotlin
// Constants
// Content provider authority
val AUTHORITY = "com.example.android.datasync.provider"
// Account type
val ACCOUNT_TYPE = "com.example.android.datasync"
// Account
val ACCOUNT = "default_account"
...
class MainActivity : FragmentActivity() {
    ...
    // Instance fields
    private lateinit var mAccount: Account
    ...
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        ...
        /*
         * Create the placeholder account. The code for CreateSyncAccount
         * is listed in the lesson Creating a Sync Adapter
         */

        mAccount = createSyncAccount()
        ...
    }

    /**
     * Respond to a button click by calling requestSync(). This is an
     * asynchronous operation.
     *
     * This method is attached to the refresh button in the layout
     * XML file
     *
     * @param v The View associated with the method call,
     * in this case a Button
     */
    fun onRefreshButtonClick(v: View) {
        // Pass the settings flags by inserting them in a bundle
        val settingsBundle = Bundle().apply {
            putBoolean(ContentResolver.SYNC_EXTRAS_MANUAL, true)
            putBoolean(ContentResolver.SYNC_EXTRAS_EXPEDITED, true)
        }
        /*
         * Request the sync for the default account, authority, and
         * manual sync settings
         */
        ContentResolver.requestSync(mAccount, AUTHORITY, settingsBundle)
    }
```

### Java

```java
public class MainActivity extends FragmentActivity {
    ...
    // Constants
    // Content provider authority
    public static final String AUTHORITY =
            "com.example.android.datasync.provider";
    // Account type
    public static final String ACCOUNT_TYPE = "com.example.android.datasync";
    // Account
    public static final String ACCOUNT = "default_account";
    // Instance fields
    Account mAccount;
    ...
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        ...
        /*
         * Create the placeholder account. The code for CreateSyncAccount
         * is listed in the lesson Creating a Sync Adapter
         */

        mAccount = CreateSyncAccount(this);
        ...
    }
    /**
     * Respond to a button click by calling requestSync(). This is an
     * asynchronous operation.
     *
     * This method is attached to the refresh button in the layout
     * XML file
     *
     * @param v The View associated with the method call,
     * in this case a Button
     */
    public void onRefreshButtonClick(View v) {
        // Pass the settings flags by inserting them in a bundle
        Bundle settingsBundle = new Bundle();
        settingsBundle.putBoolean(
                ContentResolver.SYNC_EXTRAS_MANUAL, true);
        settingsBundle.putBoolean(
                ContentResolver.SYNC_EXTRAS_EXPEDITED, true);
        /*
         * Request the sync for the default account, authority, and
         * manual sync settings
         */
        ContentResolver.requestSync(mAccount, AUTHORITY, settingsBundle);
    }
```