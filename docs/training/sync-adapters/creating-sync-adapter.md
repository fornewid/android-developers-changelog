---
title: https://developer.android.com/training/sync-adapters/creating-sync-adapter
url: https://developer.android.com/training/sync-adapters/creating-sync-adapter
source: md.txt
---

**Note:** We recommended [WorkManager](https://developer.android.com/topic/libraries/architecture/workmanager)
as the recommended solution for most background processing use cases. Please reference the
[background processing guide](https://developer.android.com/guide/background) to learn which solution works best for you.


The sync adapter component in your app encapsulates the code for the tasks that transfer
data between the device and a server. Based on the scheduling and triggers you provide in
your app, the sync adapter framework runs the code in the sync adapter component. To add a
sync adapter component to your app, you need to add the following pieces:


Sync adapter class.
:
    A class that wraps your data transfer code in an interface compatible with the sync adapter
    framework.


Bound [Service](https://developer.android.com/reference/android/app/Service).
:
    A component that allows the sync adapter framework to run the code in your sync adapter
    class.


Sync adapter XML metadata file.
:
    A file containing information about your sync adapter. The framework reads this file to
    find out how to load and schedule your data transfer.


Declarations in the app manifest.
:
    XML that declares the bound service and points to sync adapter-specific metadata.


This lesson shows you how to define these elements.

## Create a sync adapter class


In this part of the lesson you learn how to create the sync adapter class that encapsulates the
data transfer code. Creating the class includes extending the sync adapter base class, defining
constructors for the class, and implementing the method where you define the data transfer
tasks.

### Extend the base sync adapter class


To create the sync adapter component, start by extending
[AbstractThreadedSyncAdapter](https://developer.android.com/reference/android/content/AbstractThreadedSyncAdapter) and writing its constructors. Use the
constructors to run setup tasks each time your sync adapter component is created from
scratch, just as you use [Activity.onCreate()](https://developer.android.com/reference/android/app/Activity#onCreate(android.os.Bundle)) to set up an
activity. For example, if your app uses a content provider to store data, use the constructors
to get a [ContentResolver](https://developer.android.com/reference/android/content/ContentResolver) instance. Since a second form of the
constructor was added in Android platform version 3.0 to support the `parallelSyncs`
argument, you need to create two forms of the constructor to maintain compatibility.


**Note:** The sync adapter framework is designed to work with sync adapter
components that are singleton instances. Instantiating the sync adapter component is covered
in more detail in the section
[Bind the Sync Adapter to the Framework](https://developer.android.com/training/sync-adapters/creating-sync-adapter#CreateSyncAdapterService).


The following example shows you how to implement
[AbstractThreadedSyncAdapter](https://developer.android.com/reference/android/content/AbstractThreadedSyncAdapter)and its constructors:  

### Kotlin

```kotlin
/**
 * Handle the transfer of data between a server and an
 * app, using the Android sync adapter framework.
 */
class SyncAdapter @JvmOverloads constructor(
        context: Context,
        autoInitialize: Boolean,
        /**
         * Using a default argument along with @JvmOverloads
         * generates constructor for both method signatures to maintain compatibility
         * with Android 3.0 and later platform versions
         */
        allowParallelSyncs: Boolean = false,
        /*
         * If your app uses a content resolver, get an instance of it
         * from the incoming Context
         */
        val mContentResolver: ContentResolver = context.contentResolver
) : AbstractThreadedSyncAdapter(context, autoInitialize, allowParallelSyncs) {
    ...
}
```

### Java

```java
/**
 * Handle the transfer of data between a server and an
 * app, using the Android sync adapter framework.
 */
public class SyncAdapter extends AbstractThreadedSyncAdapter {
    ...
    // Global variables
    // Define a variable to contain a content resolver instance
    ContentResolver contentResolver;
    /**
     * Set up the sync adapter
     */
    public SyncAdapter(Context context, boolean autoInitialize) {
        super(context, autoInitialize);
        /*
         * If your app uses a content resolver, get an instance of it
         * from the incoming Context
         */
        contentResolver = context.getContentResolver();
    }
    ...
    /**
     * Set up the sync adapter. This form of the
     * constructor maintains compatibility with Android 3.0
     * and later platform versions
     */
    public SyncAdapter(
            Context context,
            boolean autoInitialize,
            boolean allowParallelSyncs) {
        super(context, autoInitialize, allowParallelSyncs);
        /*
         * If your app uses a content resolver, get an instance of it
         * from the incoming Context
         */
        contentResolver = context.getContentResolver();
        ...
    }
```

### Add the data transfer code


The sync adapter component does not automatically do data transfer. Instead, it
encapsulates your data transfer code, so that the sync adapter framework can run the
data transfer in the background, without involvement from your app. When the framework is ready
to sync your application's data, it invokes your implementation of the method
[onPerformSync()](https://developer.android.com/reference/android/content/AbstractThreadedSyncAdapter#onPerformSync(android.accounts.Account, android.os.Bundle, java.lang.String, android.content.ContentProviderClient, android.content.SyncResult)).


To facilitate the transfer of data from your main app code to the sync adapter component,
the sync adapter framework calls
[onPerformSync()](https://developer.android.com/reference/android/content/AbstractThreadedSyncAdapter#onPerformSync(android.accounts.Account, android.os.Bundle, java.lang.String, android.content.ContentProviderClient, android.content.SyncResult)) with the
following arguments:


Account
:
    An [Account](https://developer.android.com/reference/android/accounts/Account) object associated with the event that triggered
    the sync adapter. If your server doesn't use accounts, you don't need to use the
    information in this object.


Extras
:
    A [Bundle](https://developer.android.com/reference/android/os/Bundle) containing flags sent by the event that triggered the sync
    adapter.


Authority
:
    The authority of a content provider in the system. Your app has to have access to
    this provider. Usually, the authority corresponds to a content provider in your own app.


Content provider client
:
    A [ContentProviderClient](https://developer.android.com/reference/android/content/ContentProviderClient) for the content provider pointed to by the
    authority argument. A [ContentProviderClient](https://developer.android.com/reference/android/content/ContentProviderClient) is a lightweight public
    interface to a content provider. It has the same basic functionality as a
    [ContentResolver](https://developer.android.com/reference/android/content/ContentResolver). If you're using a content provider to store data
    for your app, you can connect to the provider with this object. Otherwise, you can ignore
    it.


Sync result
:
    A [SyncResult](https://developer.android.com/reference/android/content/SyncResult) object that you use to send information to the sync
    adapter framework.


The following snippet shows the overall structure of
[onPerformSync()](https://developer.android.com/reference/android/content/AbstractThreadedSyncAdapter#onPerformSync(android.accounts.Account, android.os.Bundle, java.lang.String, android.content.ContentProviderClient, android.content.SyncResult)):  

### Kotlin

```kotlin
/*
 * Specify the code you want to run in the sync adapter. The entire
 * sync adapter runs in a background thread, so you don't have to set
 * up your own background processing.
 */
override fun onPerformSync(
        account: Account,
        extras: Bundle,
        authority: String,
        provider: ContentProviderClient,
        syncResult: SyncResult
) {
    /*
     * Put the data transfer code here.
     */
}
```

### Java

```java
/*
 * Specify the code you want to run in the sync adapter. The entire
 * sync adapter runs in a background thread, so you don't have to set
 * up your own background processing.
 */
@Override
public void onPerformSync(
        Account account,
        Bundle extras,
        String authority,
        ContentProviderClient provider,
        SyncResult syncResult) {
    /*
     * Put the data transfer code here.
     */
}
```


While the actual implementation of
[onPerformSync()](https://developer.android.com/reference/android/content/AbstractThreadedSyncAdapter#onPerformSync(android.accounts.Account, android.os.Bundle, java.lang.String, android.content.ContentProviderClient, android.content.SyncResult)) is specific to
your app's data synchronization requirements and server connection protocols, there are a few
general tasks your implementation should perform:


Connecting to a server
:
    Although you can assume that the network is available when your data transfer starts, the
    sync adapter framework doesn't automatically connect to a server.


Downloading and uploading data
:
    A sync adapter doesn't automate any data transfer tasks. If you want to download
    data from a server and store it in a content provider, you have to provide the code that
    requests the data, downloads it, and inserts it in the provider. Similarly, if you want to
    send data to a server, you have to read it from a file, database, or provider, and send
    the necessary upload request. You also have to handle network errors that occur while your
    data transfer is running.


Handling data conflicts or determining how current the data is
:
    A sync adapter doesn't automatically handle conflicts between data on the server and data
    on the device. Also, it doesn't automatically detect if the data on the server is newer than
    the data on the device, or vice versa. Instead, you have to provide your own algorithms for
    handling this situation.


Clean up.
:
    Always close connections to a server and clean up temp files and caches at the end of
    your data transfer.


**Note:** The sync adapter framework runs
[onPerformSync()](https://developer.android.com/reference/android/content/AbstractThreadedSyncAdapter#onPerformSync(android.accounts.Account, android.os.Bundle, java.lang.String, android.content.ContentProviderClient, android.content.SyncResult)) on a
background thread, so you don't have to set up your own background processing.


In addition to your sync-related tasks, you should try to combine your regular
network-related tasks and add them to
[onPerformSync()](https://developer.android.com/reference/android/content/AbstractThreadedSyncAdapter#onPerformSync(android.accounts.Account, android.os.Bundle, java.lang.String, android.content.ContentProviderClient, android.content.SyncResult)).
By concentrating all of your network tasks in this method, you conserve the battery power that's
needed to start and stop the network interfaces. To learn more about making network access more
efficient, see the training class [Transferring Data Without Draining the Battery](https://developer.android.com/training/efficient-downloads), which describes several network access
tasks you can include in your data transfer code.

## Bind the sync adapter to the framework


You now have your data transfer code encapsulated in a sync adapter component, but you have
to provide the framework with access to your code. To do this, you need to create a bound
[Service](https://developer.android.com/reference/android/app/Service) that passes a special Android binder object from the sync adapter
component to the framework. With this binder object, the framework can invoke the
[onPerformSync()](https://developer.android.com/reference/android/content/AbstractThreadedSyncAdapter#onPerformSync(android.accounts.Account, android.os.Bundle, java.lang.String, android.content.ContentProviderClient, android.content.SyncResult)) method and
pass data to it.


Instantiate your sync adapter component as a singleton in the
[onCreate()](https://developer.android.com/reference/android/app/Service#onCreate()) method of the service. By instantiating
the component in [onCreate()](https://developer.android.com/reference/android/app/Service#onCreate()), you defer
creating it until the service starts, which happens when the framework first tries to run your
data transfer. You need to instantiate the component in a thread-safe manner, in case the sync
adapter framework queues up multiple executions of your sync adapter in response to triggers or
scheduling.


For example, the following snippet shows you how to create a class that implements the
bound [Service](https://developer.android.com/reference/android/app/Service), instantiates your sync adapter component, and gets the
Android binder object:  

### Kotlin

```kotlin
package com.example.android.syncadapter
/**
 * Define a Service that returns an [android.os.IBinder] for the
 * sync adapter class, allowing the sync adapter framework to call
 * onPerformSync().
 */
class SyncService : Service() {
    /*
     * Instantiate the sync adapter object.
     */
    override fun onCreate() {
        /*
         * Create the sync adapter as a singleton.
         * Set the sync adapter as syncable
         * Disallow parallel syncs
         */
        synchronized(sSyncAdapterLock) {
            sSyncAdapter = sSyncAdapter ?: SyncAdapter(applicationContext, true)
        }
    }

    /**
     * Return an object that allows the system to invoke
     * the sync adapter.
     *
     */
    override fun onBind(intent: Intent): IBinder {
        /*
         * Get the object that allows external processes
         * to call onPerformSync(). The object is created
         * in the base class code when the SyncAdapter
         * constructors call super()
         *
         * We should never be in a position where this is called before
         * onCreate() so the exception should never be thrown
         */
        return sSyncAdapter?.syncAdapterBinder ?: throw IllegalStateException()
    }

    companion object {
        // Storage for an instance of the sync adapter
        private var sSyncAdapter: SyncAdapter? = null
        // Object to use as a thread-safe lock
        private val sSyncAdapterLock = Any()
    }
}
```

### Java

```java
package com.example.android.syncadapter;
/**
 * Define a Service that returns an <code><a href="/reference/android/os/IBinder.html">IBinder</a></code> for the
 * sync adapter class, allowing the sync adapter framework to call
 * onPerformSync().
 */
public class SyncService extends Service {
    // Storage for an instance of the sync adapter
    private static SyncAdapter sSyncAdapter = null;
    // Object to use as a thread-safe lock
    private static final Object sSyncAdapterLock = new Object();
    /*
     * Instantiate the sync adapter object.
     */
    @Override
    public void onCreate() {
        /*
         * Create the sync adapter as a singleton.
         * Set the sync adapter as syncable
         * Disallow parallel syncs
         */
        synchronized (sSyncAdapterLock) {
            if (sSyncAdapter == null) {
                sSyncAdapter = new SyncAdapter(getApplicationContext(), true);
            }
        }
    }
    /**
     * Return an object that allows the system to invoke
     * the sync adapter.
     *
     */
    @Override
    public IBinder onBind(Intent intent) {
        /*
         * Get the object that allows external processes
         * to call onPerformSync(). The object is created
         * in the base class code when the SyncAdapter
         * constructors call super()
         */
        return sSyncAdapter.getSyncAdapterBinder();
    }
}
```


**Note:** To see a more detailed example of a bound service for a sync adapter,
see the sample app.

## Add the account required by the framework


The sync adapter framework requires each sync adapter to have an account type. You declared
the account type value in the section
[Add the Authenticator Metadata File](https://developer.android.com/training/sync-adapters/creating-authenticator#CreateAuthenticatorFile). Now you have to set up this account type in the
Android system. To set up the account type, add a placeholder account that uses the account type
by calling [addAccountExplicitly()](https://developer.android.com/reference/android/accounts/AccountManager#addAccountExplicitly(android.accounts.Account, java.lang.String, android.os.Bundle)).


The best place to call the method is in the
[onCreate()](https://developer.android.com/reference/androidx/fragment/app/FragmentActivity#onCreate(android.os.Bundle)) method of your app's
opening activity. The following code snippet shows you how to do this:  

### Kotlin

```kotlin
...
// Constants
// The authority for the sync adapter's content provider
const val AUTHORITY = "com.example.android.datasync.provider"
// An account type, in the form of a domain name
const val ACCOUNT_TYPE = "example.com"
// The account name
const val ACCOUNT = "placeholderaccount"
...
class MainActivity : FragmentActivity() {

    // Instance fields
    private lateinit var mAccount: Account
    ...
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
       ...
        // Create the placeholder account
        mAccount = createSyncAccount()
       ...
    }
    ...
    /**
     * Create a new placeholder account for the sync adapter
     */
    private fun createSyncAccount(): Account {
        val accountManager = getSystemService(Context.ACCOUNT_SERVICE) as AccountManager
        return Account(ACCOUNT, ACCOUNT_TYPE).also { newAccount ->
            /*
             * Add the account and account type, no password or user data
             * If successful, return the Account object, otherwise report an error.
             */
            if (accountManager.addAccountExplicitly(newAccount, null, null)) {
                /*
                 * If you don't set android:syncable="true" in
                 * in your <provider> element in the manifest,
                 * then call context.setIsSyncable(account, AUTHORITY, 1)
                 * here.
                 */
            } else {
                /*
                 * The account exists or some other error occurred. Log this, report it,
                 * or handle it internally.
                 */
            }
        }
    }
    ...
}
```

### Java

```java
public class MainActivity extends FragmentActivity {
    ...
    ...
    // Constants
    // The authority for the sync adapter's content provider
    public static final String AUTHORITY = "com.example.android.datasync.provider";
    // An account type, in the form of a domain name
    public static final String ACCOUNT_TYPE = "example.com";
    // The account name
    public static final String ACCOUNT = "placeholderaccount";
    // Instance fields
    Account mAccount;
    ...
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        ...
        // Create the placeholder account
        mAccount = CreateSyncAccount(this);
        ...
    }
    ...
    /**
     * Create a new placeholder account for the sync adapter
     *
     * @param context The application context
     */
    public static Account CreateSyncAccount(Context context) {
        // Create the account type and default account
        Account newAccount = new Account(
                ACCOUNT, ACCOUNT_TYPE);
        // Get an instance of the Android account manager
        AccountManager accountManager =
                (AccountManager) context.getSystemService(
                        ACCOUNT_SERVICE);
        /*
         * Add the account and account type, no password or user data
         * If successful, return the Account object, otherwise report an error.
         */
        if (accountManager.addAccountExplicitly(newAccount, null, null)) {
            /*
             * If you don't set android:syncable="true" in
             * in your <provider> element in the manifest,
             * then call context.setIsSyncable(account, AUTHORITY, 1)
             * here.
             */
        } else {
            /*
             * The account exists or some other error occurred. Log this, report it,
             * or handle it internally.
             */
        }
    }
    ...
}
```

## Add the sync adapter metadata file


To plug your sync adapter component into the framework, you need to provide the framework
with metadata that describes the component and provides additional flags. The metadata specifies
the account type you've created for your sync adapter, declares a content provider authority
associated with your app, controls a part of the system user interface related to sync adapters,
and declares other sync-related flags. Declare this metadata in a special XML file stored in
the `/res/xml/` directory in your app project. You can give any name to the file,
although it's usually called `syncadapter.xml`.


This XML file contains a single XML element `<sync-adapter>` that has the
following attributes:

`android:contentAuthority`
:
    The URI authority for your content provider. If you created a stub content provider for
    your app in the previous lesson [Creating a Stub Content Provider](https://developer.android.com/training/sync-adapters/creating-stub-provider), use the value you specified for the
    attribute
    [android:authorities](https://developer.android.com/guide/topics/manifest/provider-element#auth)
    in the [<provider>](https://developer.android.com/guide/topics/manifest/provider-element) element you added to your app manifest. This attribute is
    described in more detail in the section
    [Declare the Provider in the Manifest](https://developer.android.com/training/sync-adapters/creating-stub-provider#DeclareProvider).


    If you're transferring data from a content provider to a server with your sync adapter, this
    value should be the same as the content URI authority you're using for that data. This value
    is also one of the authorities you specify in the
    [android:authorities](https://developer.android.com/guide/topics/manifest/provider-element#auth)
    attribute of the [<provider>](https://developer.android.com/guide/topics/manifest/provider-element) element that declares your provider in your app manifest.

`android:accountType`
:
    The account type required by the sync adapter framework. The value must be the same
    as the account type value you provided when you created the authenticator metadata file, as
    described in the section [Add the Authenticator Metadata File](https://developer.android.com/training/sync-adapters/creating-authenticator#CreateAuthenticatorFile). It's also the value you specified for the
    constant `ACCOUNT_TYPE` in the code snippet in the section
    [Add the Account Required by the Framework](https://developer.android.com/training/sync-adapters/creating-sync-adapter#CreateAccountTypeAccount).

Settings attributes
:


    `android:userVisible`
    :
        Sets the visibility of the sync adapter's account type. By default, the
        account icon and label associated with the account type are visible in the
        **Accounts** section of the system's Settings app, so you should make your sync
        adapter invisible unless you have an account type or domain that's easily associated
        with your app. If you make your account type invisible, you can still allow users to
        control your sync adapter with a user interface in one of your app's activities.


    `android:supportsUploading`
    :
        Allows you to upload data to the cloud. Set this to `false` if your app only
        downloads data.


    `android:allowParallelSyncs`
    :
        Allows multiple instances of your sync adapter component to run at the same time.
        Use this if your app supports multiple user accounts and you want to allow multiple
        users to transfer data in parallel. This flag has no effect if you never run
        multiple data transfers.


    `android:isAlwaysSyncable`
    :
        Indicates to the sync adapter framework that it can run your sync adapter at any
        time you've specified. If you want to programmatically control when your sync
        adapter can run, set this flag to `false`, and then call
        [requestSync()](https://developer.android.com/reference/android/content/ContentResolver#requestSync(android.accounts.Account, java.lang.String, android.os.Bundle)) to run the
        sync adapter. To learn more about running a sync adapter, see the lesson
        [Running a Sync Adapter](https://developer.android.com/training/sync-adapters/running-sync-adapter)


The following example shows the XML for a sync adapter that uses a single placeholder account and
only does downloads.  

```xml
<?xml version="1.0" encoding="utf-8"?>
<sync-adapter
        xmlns:android="http://schemas.android.com/apk/res/android"
        android:contentAuthority="com.example.android.datasync.provider"
        android:accountType="com.android.example.datasync"
        android:userVisible="false"
        android:supportsUploading="false"
        android:allowParallelSyncs="false"
        android:isAlwaysSyncable="true"/>
```

## Declare the sync adapter in the manifest


Once you've added the sync adapter component to your app, you have to request permissions
related to using the component, and you have to declare the bound [Service](https://developer.android.com/reference/android/app/Service)
you've added.


Since the sync adapter component runs code that transfers data between the network and the
device, you need to request permission to access the Internet. In addition, your app needs
to request permission to read and write sync adapter settings, so you can control the sync
adapter programmatically from other components in your app. You also need to request a
special permission that allows your app to use the authenticator component you created
in the lesson [Creating a Stub Authenticator](https://developer.android.com/training/sync-adapters/creating-authenticator).


To request these permissions, add the following to your app manifest as child elements of
[<manifest>](https://developer.android.com/guide/topics/manifest/manifest-element):


[android.permission.INTERNET](https://developer.android.com/reference/android/Manifest.permission#INTERNET)
:
    Allows the sync adapter code to access the Internet so that it can download or upload data
    from the device to a server. You don't need to add this permission again if you were
    requesting it previously.


[android.permission.READ_SYNC_SETTINGS](https://developer.android.com/reference/android/Manifest.permission#READ_SYNC_SETTINGS)
:
    Allows your app to read the current sync adapter settings. For example, you need this
    permission in order to call [getIsSyncable()](https://developer.android.com/reference/android/content/ContentResolver#getIsSyncable(android.accounts.Account, java.lang.String)).


[android.permission.WRITE_SYNC_SETTINGS](https://developer.android.com/reference/android/Manifest.permission#WRITE_SYNC_SETTINGS)
:
    Allows your app to control sync adapter settings. You need this permission in order to
    set periodic sync adapter runs using [addPeriodicSync()](https://developer.android.com/reference/android/content/ContentResolver#addPeriodicSync(android.accounts.Account, java.lang.String, android.os.Bundle, long)). This permission is **not** required to call
    [requestSync()](https://developer.android.com/reference/android/content/ContentResolver#requestSync(android.accounts.Account, java.lang.String, android.os.Bundle)). To learn more about
    running the sync adapter, see [Running A Sync Adapter](https://developer.android.com/training/sync-adapters/running-sync-adapter).


The following snippet shows how to add the permissions:  

```xml
<manifest>
...
    <uses-permission
            android:name="android.permission.INTERNET"/>
    <uses-permission
            android:name="android.permission.READ_SYNC_SETTINGS"/>
    <uses-permission
            android:name="android.permission.WRITE_SYNC_SETTINGS"/>
    <uses-permission
            android:name="android.permission.AUTHENTICATE_ACCOUNTS"/>
...
</manifest>
```


Finally, to declare the bound [Service](https://developer.android.com/reference/android/app/Service) that the framework uses to
interact with your sync adapter, add the following XML to your app manifest as a child element
of [<application>](https://developer.android.com/guide/topics/manifest/application-element):  

```xml
        <service
                android:name="com.example.android.datasync.SyncService"
                android:exported="false"
                android:process=":sync">
            <intent-filter>
                <action android:name="android.content.SyncAdapter"/>
            </intent-filter>
            <meta-data android:name="android.content.SyncAdapter"
                    android:resource="@xml/syncadapter" />
        </service>
```


The
[<intent-filter>](https://developer.android.com/guide/topics/manifest/intent-filter-element)
element sets up a filter that's triggered by the intent action
`android.content.SyncAdapter`, sent by the system to run the sync adapter. When the filter
is triggered, the system starts the bound service you've created, which in this example is
`SyncService`. The attribute
[android:exported="false"](https://developer.android.com/guide/topics/manifest/service-element#exported)
allows only your app and the system to access the
[Service](https://developer.android.com/reference/android/app/Service). The attribute
[android:process=":sync"](https://developer.android.com/guide/topics/manifest/service-element#proc)
tells the system to run the [Service](https://developer.android.com/reference/android/app/Service) in a global shared process named
`sync`. If you have multiple sync adapters in your app they can share this process,
which reduces overhead.


The
[<meta-data>](https://developer.android.com/guide/topics/manifest/meta-data-element)
element provides the name of the sync adapter metadata XML file you created previously.
The
[android:name](https://developer.android.com/guide/topics/manifest/meta-data-element#nm)
attribute indicates that this metadata is for the sync adapter framework. The
[android:resource](https://developer.android.com/guide/topics/manifest/meta-data-element#rsrc)
element specifies the name of the metadata file.


You now have all of the components for your sync adapter. The next lesson shows you how to
tell the sync adapter framework to run your sync adapter, either in response to an event or on
a regular schedule.