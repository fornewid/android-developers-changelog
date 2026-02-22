---
title: https://developer.android.com/privacy-and-security/audit-data-access
url: https://developer.android.com/privacy-and-security/audit-data-access
source: md.txt
---

You can gain insights into how your app and its dependencies access private data
from users by performing *data access auditing* . This process, available on
devices that run Android 11 (API level 30) and higher, lets you better
identify potentially unexpected data access. Your app can register an instance
of [`AppOpsManager.OnOpNotedCallback`](https://developer.android.com/reference/android/app/AppOpsManager.OnOpNotedCallback), which can perform
actions each time one of the following events occurs:

- Your app's code accesses private data. To help you determine which logical part of your app invoked the event, you can [audit data access by attribution
  tag](https://developer.android.com/privacy-and-security/audit-data-access#audit-by-attribution-tag).
- Code in a dependent library or SDK accesses private data.

Data access auditing is invoked on the thread where the data request takes
place. This means that if a third-party SDK or library in your app calls an API
that accesses private data, data access auditing lets your
`OnOpNotedCallback` examine information about the call. Usually, this
callback object can tell whether the call came from your app or the SDK by
looking at the app's current status, such as the current thread's stack trace.

## Log access of data

To perform data access auditing using an instance of
`AppOpsManager.OnOpNotedCallback`, implement the callback logic in the component
where you intend to audit data access, such as within an activity's
[`onCreate()`](https://developer.android.com/reference/android/app/Activity#onCreate(android.os.Bundle,%20android.os.PersistableBundle))
method or an application's
[`onCreate()`](https://developer.android.com/reference/android/app/Application#onCreate()) method.
| **Note:** If your app accesses data in multiple components, such as in a foreground service and in a background task, create a custom subclass of [`Application`](https://developer.android.com/reference/kotlin/android/app/Application) and define `AppOpsManager.OnOpNotedCallback` in the `onCreate()` method of your subclass.

The following code snippet defines an `AppOpsManager.OnOpNotedCallback` for
auditing data access within a single activity:  

### Kotlin

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
    val appOpsCallback = object : AppOpsManager.OnOpNotedCallback() {
        private fun logPrivateDataAccess(opCode: String, trace: String) {
            Log.i(MY_APP_TAG, "Private data accessed. " +
                    "Operation: $opCode\nStack Trace:\n$trace")
        }

        override fun onNoted(syncNotedAppOp: SyncNotedAppOp) {
            logPrivateDataAccess(
                    syncNotedAppOp.op, Throwable().stackTrace.toString())
        }

        override fun onSelfNoted(syncNotedAppOp: SyncNotedAppOp) {
            logPrivateDataAccess(
                    syncNotedAppOp.op, Throwable().stackTrace.toString())
        }

        override fun onAsyncNoted(asyncNotedAppOp: AsyncNotedAppOp) {
            logPrivateDataAccess(asyncNotedAppOp.op, asyncNotedAppOp.message)
        }
    }

    val appOpsManager =
            getSystemService(AppOpsManager::class.java) as AppOpsManager
    appOpsManager.setOnOpNotedCallback(mainExecutor, appOpsCallback)
}
```

### Java

```java
@Override
public void onCreate(@Nullable Bundle savedInstanceState,
        @Nullable PersistableBundle persistentState) {
    AppOpsManager.OnOpNotedCallback appOpsCallback =
            new AppOpsManager.OnOpNotedCallback() {
        private void logPrivateDataAccess(String opCode, String trace) {
            Log.i(MY_APP_TAG, "Private data accessed. " +
                    "Operation: $opCode\nStack Trace:\n$trace");
        }

        @Override
        public void onNoted(@NonNull SyncNotedAppOp syncNotedAppOp) {
            logPrivateDataAccess(syncNotedAppOp.getOp(),
                    Arrays.toString(new Throwable().getStackTrace()));
        }

        @Override
        public void onSelfNoted(@NonNull SyncNotedAppOp syncNotedAppOp) {
            logPrivateDataAccess(syncNotedAppOp.getOp(),
                    Arrays.toString(new Throwable().getStackTrace()));
        }

        @Override
        public void onAsyncNoted(@NonNull AsyncNotedAppOp asyncNotedAppOp) {
            logPrivateDataAccess(asyncNotedAppOp.getOp(),
                    asyncNotedAppOp.getMessage());
        }
    };

    AppOpsManager appOpsManager = getSystemService(AppOpsManager.class);
    if (appOpsManager != null) {
        appOpsManager.setOnOpNotedCallback(getMainExecutor(), appOpsCallback);
    }
}
```

The `onAsyncNoted()` and `onSelfNoted()` methods are called in specific
situations:

- [`onAsyncNoted()`](https://developer.android.com/reference/android/app/AppOpsManager.OnOpNotedCallback#onAsyncNoted(android.app.AsyncNotedAppOp))
  is called if the data access doesn't happen during your app's
  API call. The most common example is when your app registers a listener and the
  data access happens each time the listener's callback is invoked.

  The `AsyncNotedOp` argument that's passed into `onAsyncNoted()` contains a
  method called `getMessage()`. This method provides more information about
  the data access. In the case of the location callbacks, the message contains
  the system-identity-hash of the listener.
- [`onSelfNoted()`](https://developer.android.com/reference/android/app/AppOpsManager.OnOpNotedCallback#onSelfNoted(android.app.SyncNotedAppOp))
  is called in the very rare case when an app passes its own UID into
  [`noteOp()`](https://developer.android.com/reference/android/app/AppOpsManager#noteOp(java.lang.String,%20int,%20java.lang.String,%20java.lang.String,%20java.lang.String)).

## Audit data access by attribution tag

Your app might have several primary use cases, such as letting users capture
photos and share these photos with their contacts. If you develop a
multi-purpose app, you can apply an *attribution tag* to each part of your app
when you audit its data access. The `attributionTag` context is returned back
in the objects passed to the calls to [`onNoted()`](https://developer.android.com/reference/android/app/AppOpsManager.OnOpNotedCallback#onNoted(android.app.SyncNotedAppOp)).
This helps you more easily trace data access back to logical parts of your
code.

To define attribution tags in your app, complete the steps in the following
sections.

### Declare attribution tags in manifest

If your app targets Android 12 (API level 31) or higher, you must declare
attribution tags in your app's manifest file, using the format shown in the
following code snippet. If you attempt to use an attribution tag that you don't
declare in your app's manifest file, the system creates a `null` tag for you and
logs a message in Logcat.  

```xml
<manifest ...>
    <!-- The value of "android:tag" must be a literal string, and the
         value of "android:label" must be a resource. The value of
         "android:label" is user-readable. -->
    <attribution android:tag="sharePhotos"
                 android:label="@string/share_photos_attribution_label" />
    ...
</manifest>
```

### Create attribution tags

In the
[`onCreate()`](https://developer.android.com/reference/android/app/Activity#onCreate(android.os.Bundle,%20android.os.PersistableBundle))
method of the activity where you access data, such as the activity where you
request location or access the user's list of contacts, call
[`createAttributionContext()`](https://developer.android.com/reference/android/content/Context#createAttributionContext(java.lang.String)),
passing in the attribution tag that you wish to associate with a part of your
app.

The following code snippet demonstrates how to create an attribution tag for a
photo-location-sharing part of an app:  

### Kotlin

```kotlin
class SharePhotoLocationActivity : AppCompatActivity() {
    lateinit var attributionContext: Context

    override fun onCreate(savedInstanceState: Bundle?) {
        attributionContext = createAttributionContext("sharePhotos")
    }

    fun getLocation() {
        val locationManager = attributionContext.getSystemService(
                LocationManager::class.java) as LocationManager
        // Use "locationManager" to access device location information.
    }
}
```

### Java

```java
public class SharePhotoLocationActivity extends AppCompatActivity {
    private Context attributionContext;

    @Override
    public void onCreate(@Nullable Bundle savedInstanceState,
            @Nullable PersistableBundle persistentState) {
        attributionContext = createAttributionContext("sharePhotos");
    }

    public void getLocation() {
        LocationManager locationManager =
                attributionContext.getSystemService(LocationManager.class);
        if (locationManager != null) {
            // Use "locationManager" to access device location information.
        }
    }
}
```

### Include attribution tags in access logs

Update your `AppOpsManager.OnOpNotedCallback` callback so that your app's logs
include the names of the attribution tags that you defined.
| **Note:** If the return value for the attribution tag is `null`, this means that the current [`Context`](https://developer.android.com/reference/android/content/Context) object is associated with the main part of your app.

The following code snippet shows updated logic that logs attribution tags:  

### Kotlin

```kotlin
val appOpsCallback = object : AppOpsManager.OnOpNotedCallback() {
    private fun logPrivateDataAccess(
            opCode: String, attributionTag: String, trace: String) {
        Log.i(MY_APP_TAG, "Private data accessed. " +
                    "Operation: $opCode\n " +
                    "Attribution Tag:$attributionTag\nStack Trace:\n$trace")
    }

    override fun onNoted(syncNotedAppOp: SyncNotedAppOp) {
        logPrivateDataAccess(syncNotedAppOp.op,
                syncNotedAppOp.attributionTag,
                Throwable().stackTrace.toString())
    }

    override fun onSelfNoted(syncNotedAppOp: SyncNotedAppOp) {
        logPrivateDataAccess(syncNotedAppOp.op,
                syncNotedAppOp.attributionTag,
                Throwable().stackTrace.toString())
    }

    override fun onAsyncNoted(asyncNotedAppOp: AsyncNotedAppOp) {
        logPrivateDataAccess(asyncNotedAppOp.op,
                asyncNotedAppOp.attributionTag,
                asyncNotedAppOp.message)
    }
}
```

### Java

```java
@Override
public void onCreate(@Nullable Bundle savedInstanceState,
        @Nullable PersistableBundle persistentState) {
    AppOpsManager.OnOpNotedCallback appOpsCallback =
            new AppOpsManager.OnOpNotedCallback() {
        private void logPrivateDataAccess(String opCode,
                String attributionTag, String trace) {
            Log.i("MY_APP_TAG", "Private data accessed. " +
                    "Operation: $opCode\n " +
                    "Attribution Tag:$attributionTag\nStack Trace:\n$trace");
        }

        @Override
        public void onNoted(@NonNull SyncNotedAppOp syncNotedAppOp) {
            logPrivateDataAccess(syncNotedAppOp.getOp(),
                    syncNotedAppOp.getAttributionTag(),
                    Arrays.toString(new Throwable().getStackTrace()));
        }

        @Override
        public void onSelfNoted(@NonNull SyncNotedAppOp syncNotedAppOp) {
            logPrivateDataAccess(syncNotedAppOp.getOp(),
                    syncNotedAppOp.getAttributionTag(),
                    Arrays.toString(new Throwable().getStackTrace()));
        }

        @Override
        public void onAsyncNoted(@NonNull AsyncNotedAppOp asyncNotedAppOp) {
            logPrivateDataAccess(asyncNotedAppOp.getOp(),
                    asyncNotedAppOp.getAttributionTag(),
                    asyncNotedAppOp.getMessage());
        }
    };

    AppOpsManager appOpsManager = getSystemService(AppOpsManager.class);
    if (appOpsManager != null) {
        appOpsManager.setNotedAppOpsCollector(appOpsCollector);
    }
}
```