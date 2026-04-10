---
title: https://developer.android.com/develop/connectivity/network-ops/managing
url: https://developer.android.com/develop/connectivity/network-ops/managing
source: md.txt
---

This lesson describes how to write applications that have fine-grained control
over their usage of network resources. If your application performs a lot of
network operations, you should provide user settings that allow users to control
your app's data habits, such as how often your app syncs data, whether to
perform uploads/downloads only when on Wi-Fi, whether to use data while roaming,
and so on. With these controls available to them, users are much less likely to
disable your app's access to background data when they approach their limits,
because they can instead precisely control how much data your app uses.

To learn more about the network usage of your app, including the number and
types of network connections over a period of time, read [Web
apps](https://developer.android.com/guide/webapps) and [Inspect network traffic with network
profiler](https://developer.android.com/studio/profile/network-profiler). For general guidelines on how to
write apps that minimize the battery life impact of downloads and network
connections, see [Optimize battery life](https://developer.android.com/training/monitoring-device-state) and
[Transfer data without draining the battery](https://developer.android.com/training/efficient-downloads).

You can also check out the [NetworkConnect
sample](https://github.com/android/connectivity-samples/tree/main/NetworkConnect).

## Check a device's network connection

A device can have various types of network connections. This lesson focuses on
using either a Wi-Fi or a mobile network connection. For the full list of
possible network types, see
[`ConnectivityManager`](https://developer.android.com/reference/android/net/ConnectivityManager).

Wi-Fi is typically faster. Also, mobile data is often metered, which can get
expensive. A common strategy for apps is to only fetch large data if a Wi-Fi
network is available.

Before you perform network operations, it's good practice to check the state of
network connectivity. Among other things, this could prevent your app from
inadvertently using the wrong radio. If a network connection is unavailable,
your application should respond gracefully. To check the network connection, you
typically use the following classes:

- `ConnectivityManager`: Answers queries about the state of network connectivity. It also notifies applications when network connectivity changes.
- [`NetworkInfo`](https://developer.android.com/reference/android/net/NetworkInfo): Describes the status of a network interface of a given type (currently either Mobile or Wi-Fi).

This code snippet tests network connectivity for Wi-Fi and mobile. It determines
whether these network interfaces are available (that is, whether network
connectivity is possible) and/or connected (that is, whether network
connectivity exists and if it is possible to establish sockets and pass data):

### Kotlin

```kotlin
private const val DEBUG_TAG = "NetworkStatusExample"
...
val connMgr = getSystemService(Context.CONNECTIVITY_SERVICE) as ConnectivityManager
var isWifiConn: Boolean = false
var isMobileConn: Boolean = false
connMgr.allNetworks.forEach { network ->
    connMgr.getNetworkInfo(network).apply {
        if (type == ConnectivityManager.TYPE_WIFI) {
            isWifiConn = isWifiConn or isConnected
        }
        if (type == ConnectivityManager.TYPE_MOBILE) {
            isMobileConn = isMobileConn or isConnected
        }
    }
}
Log.d(DEBUG_TAG, "Wifi connected: $isWifiConn")
Log.d(DEBUG_TAG, "Mobile connected: $isMobileConn")
```

### Java

```java
private static final String DEBUG_TAG = "NetworkStatusExample";
...
ConnectivityManager connMgr =
        (ConnectivityManager) getSystemService(Context.CONNECTIVITY_SERVICE);
boolean isWifiConn = false;
boolean isMobileConn = false;
for (Network network : connMgr.getAllNetworks()) {
    NetworkInfo networkInfo = connMgr.getNetworkInfo(network);
    if (networkInfo.getType() == ConnectivityManager.TYPE_WIFI) {
        isWifiConn |= networkInfo.isConnected();
    }
    if (networkInfo.getType() == ConnectivityManager.TYPE_MOBILE) {
        isMobileConn |= networkInfo.isConnected();
    }
}
Log.d(DEBUG_TAG, "Wifi connected: " + isWifiConn);
Log.d(DEBUG_TAG, "Mobile connected: " + isMobileConn);
```

Note that you should not base decisions on whether a network is "available." You
should always check
[`isConnected()`](https://developer.android.com/reference/android/net/NetworkInfo#isConnected()) before
performing network operations, since `isConnected()` handles cases like flaky
mobile networks, airplane mode, and restricted background data.

A more concise way of checking whether a network interface is available is as
follows. The method
[`getActiveNetworkInfo()`](https://developer.android.com/reference/android/net/ConnectivityManager#getActiveNetworkInfo())
returns a `NetworkInfo` instance
representing the first connected network interface it can find, or `null` if
none of the interfaces is connected (meaning that an internet connection is not
available):

### Kotlin

```kotlin
fun isOnline(): Boolean {
    val connMgr = getSystemService(Context.CONNECTIVITY_SERVICE) as ConnectivityManager
    val networkInfo: NetworkInfo? = connMgr.activeNetworkInfo
    return networkInfo?.isConnected == true
}
```

### Java

```java
public boolean isOnline() {
    ConnectivityManager connMgr = (ConnectivityManager)
            getSystemService(Context.CONNECTIVITY_SERVICE);
    NetworkInfo networkInfo = connMgr.getActiveNetworkInfo();
    return (networkInfo != null && networkInfo.isConnected());
}
```

To query more fine-grained state you can use
[`NetworkInfo.DetailedState`](https://developer.android.com/reference/android/net/NetworkInfo.DetailedState),
but this should seldom be necessary.

## Manage network usage

You can implement a preferences activity that gives users explicit control over
your app's usage of network resources. For example:

- You might allow users to upload videos only when the device is connected to a Wi-Fi network.
- You might sync (or not) depending on specific criteria such as network availability, time interval, and so on.

To write an app that supports network access and managing network usage, your
manifest must have the right permissions and intent filters.

- The manifest excerpted later in this section includes the following permissions:
  - [`android.permission.INTERNET`](https://developer.android.com/reference/android/Manifest.permission#INTERNET) --- Allows applications to open network sockets.
  - [`android.permission.ACCESS_NETWORK_STATE`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_NETWORK_STATE) --- Allows applications to access information about networks.
- You can declare the intent filter for the [`ACTION_MANAGE_NETWORK_USAGE`](https://developer.android.com/reference/android/content/Intent#ACTION_MANAGE_NETWORK_USAGE) action to indicate that your application defines an activity that offers options to control data usage. `ACTION_MANAGE_NETWORK_USAGE` shows settings for managing the network data usage of a specific application. When your app has a settings activity that allows users to control network usage, you should declare this intent filter for that activity.

In the sample application, this action is handled by the class
`SettingsActivity`, which displays a preferences UI to let users decide when to
download a feed.

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.android.networkusage"
    ...>

    <uses-sdk android:minSdkVersion="4"
           android:targetSdkVersion="14" />

    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />

    <application
        ...>
        ...
        <activity android:label="SettingsActivity" android:name=".SettingsActivity">
             <intent-filter>
                <action android:name="android.intent.action.MANAGE_NETWORK_USAGE" />
                <category android:name="android.intent.category.DEFAULT" />
          </intent-filter>
        </activity>
    </application>
</manifest>
```

Apps that deal with sensitive user data, and which target Android 11 and
higher, can grant per-process network access. By explicitly specifying which
processes are allowed network access, you isolate all code that doesn't need to
upload data.

While not guaranteed to prevent your app from accidentally uploading data, it
does provide a way for you to reduce the chance of bugs in your app causing a
data leak.

The following shows a sample of a manifest file that uses the per-process
functionality:

    <processes>
        <process />
        <deny-permission android:name="android.permission.INTERNET" />
        <process android:process=":withoutnet1" />
        <process android:process="com.android.cts.useprocess.withnet1">
            <allow-permission android:name="android.permission.INTERNET" />
        </process>
        <allow-permission android:name="android.permission.INTERNET" />
        <process android:process=":withoutnet2">
            <deny-permission android:name="android.permission.INTERNET" />
        </process>
        <process android:process="com.android.cts.useprocess.withnet2" />
    </processes>

## Implement a preference activity

As you can see in the manifest excerpt earlier in this topic, the sample app's
activity `SettingsActivity` has an intent filter for the
`ACTION_MANAGE_NETWORK_USAGE` action. `SettingsActivity` is a subclass of
[`PreferenceActivity`](https://developer.android.com/reference/android/preference/PreferenceActivity). It
displays a preferences screen (shown in figure 1) that lets users specify the
following:

- Whether to display summaries for each XML feed entry, or just a link for each entry.
- Whether to download the XML feed if any network connection is available, or only if Wi-Fi is available.

![Preferences panel](https://developer.android.com/static/images/training/basics/network-settings1.png) ![Setting a network preference](https://developer.android.com/static/images/training/basics/network-settings2.png)

**Figure 1.** Preferences activity.

Here is `SettingsActivity`. Note that it implements
[`OnSharedPreferenceChangeListener`](https://developer.android.com/reference/android/content/SharedPreferences.OnSharedPreferenceChangeListener).
When a user changes a preference, it fires
[`onSharedPreferenceChanged()`](https://developer.android.com/reference/android/content/SharedPreferences.OnSharedPreferenceChangeListener#onSharedPreferenceChanged(android.content.SharedPreferences,%20java.lang.String)),
which sets `refreshDisplay` to true. This causes the display to refresh when the
user returns to the main activity:

### Kotlin

```kotlin
class SettingsActivity : PreferenceActivity(), OnSharedPreferenceChangeListener {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // Loads the XML preferences file
        addPreferencesFromResource(R.xml.preferences)
    }

    override fun onResume() {
        super.onResume()

        // Registers a listener whenever a key changes
        preferenceScreen?.sharedPreferences?.registerOnSharedPreferenceChangeListener(this)
    }

    override fun onPause() {
        super.onPause()

        // Unregisters the listener set in onResume().
        // It's best practice to unregister listeners when your app isn't using them to cut down on
        // unnecessary system overhead. You do this in onPause().
        preferenceScreen?.sharedPreferences?.unregisterOnSharedPreferenceChangeListener(this)
    }

    // When the user changes the preferences selection,
    // onSharedPreferenceChanged() restarts the main activity as a new
    // task. Sets the refreshDisplay flag to "true" to indicate that
    // the main activity should update its display.
    // The main activity queries the PreferenceManager to get the latest settings.

    override fun onSharedPreferenceChanged(sharedPreferences: SharedPreferences, key: String) {
        // Sets refreshDisplay to true so that when the user returns to the main
        // activity, the display refreshes to reflect the new settings.
        NetworkActivity.refreshDisplay = true
    }
}
```

### Java

```java
public class SettingsActivity extends PreferenceActivity implements OnSharedPreferenceChangeListener {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        // Loads the XML preferences file
        addPreferencesFromResource(R.xml.preferences);
    }

    @Override
    protected void onResume() {
        super.onResume();

        // Registers a listener whenever a key changes
        getPreferenceScreen().getSharedPreferences().registerOnSharedPreferenceChangeListener(this);
    }

    @Override
    protected void onPause() {
        super.onPause();

       // Unregisters the listener set in onResume().
       // It's best practice to unregister listeners when your app isn't using them to cut down on
       // unnecessary system overhead. You do this in onPause().
       getPreferenceScreen().getSharedPreferences().unregisterOnSharedPreferenceChangeListener(this);
    }

    // When the user changes the preferences selection,
    // onSharedPreferenceChanged() restarts the main activity as a new
    // task. Sets the refreshDisplay flag to "true" to indicate that
    // the main activity should update its display.
    // The main activity queries the PreferenceManager to get the latest settings.

    @Override
    public void onSharedPreferenceChanged(SharedPreferences sharedPreferences, String key) {
        // Sets refreshDisplay to true so that when the user returns to the main
        // activity, the display refreshes to reflect the new settings.
        NetworkActivity.refreshDisplay = true;
    }
}
```

## Respond to preference changes

When the user changes preferences in the settings screen, it typically has
consequences for the app's behavior. In this snippet, the app checks the
preferences settings in `onStart()`. if there is a match between the setting and
the device's network connection (for example, if the setting is `"Wi-Fi"` and the
device has a Wi-Fi connection), the app downloads the feed and refreshes the
display.

### Kotlin

```kotlin
class NetworkActivity : Activity() {

    // The BroadcastReceiver that tracks network connectivity changes.
    private lateinit var receiver: NetworkReceiver

    public override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // Registers BroadcastReceiver to track network connection changes.
        val filter = IntentFilter(ConnectivityManager.CONNECTIVITY_ACTION)
        receiver = NetworkReceiver()
        this.registerReceiver(receiver, filter)
    }

    public override fun onDestroy() {
        super.onDestroy()
        // Unregisters BroadcastReceiver when app is destroyed.
        this.unregisterReceiver(receiver)
    }

    // Refreshes the display if the network connection and the
    // pref settings allow it.

    public override fun onStart() {
        super.onStart()

        // Gets the user's network preference settings
        val sharedPrefs = PreferenceManager.getDefaultSharedPreferences(this)

        // Retrieves a string value for the preferences. The second parameter
        // is the default value to use if a preference value is not found.
        sPref = sharedPrefs.getString("listPref", "Wi-Fi")

        updateConnectedFlags()

        if (refreshDisplay) {
            loadPage()
        }
    }

    // Checks the network connection and sets the wifiConnected and mobileConnected
    // variables accordingly.
    fun updateConnectedFlags() {
        val connMgr = getSystemService(Context.CONNECTIVITY_SERVICE) as ConnectivityManager

        val activeInfo: NetworkInfo? = connMgr.activeNetworkInfo
        if (activeInfo?.isConnected == true) {
            wifiConnected = activeInfo.type == ConnectivityManager.TYPE_WIFI
            mobileConnected = activeInfo.type == ConnectivityManager.TYPE_MOBILE
        } else {
            wifiConnected = false
            mobileConnected = false
        }
    }

    // Uses AsyncTask subclass to download the XML feed from stackoverflow.com.
    fun loadPage() {
        if (sPref == ANY && (wifiConnected || mobileConnected) || sPref == WIFI && wifiConnected) {
            // AsyncTask subclass
            DownloadXmlTask().execute(URL)
        } else {
            showErrorPage()
        }
    }

    companion object {

        const val WIFI = "Wi-Fi"
        const val ANY = "Any"
        const val SO_URL = "http://stackoverflow.com/feeds/tag?tagnames=android&sort;=newest"

        // Whether there is a Wi-Fi connection.
        private var wifiConnected = false
        // Whether there is a mobile connection.
        private var mobileConnected = false
        // Whether the display should be refreshed.
        var refreshDisplay = true

        // The user's current network preference setting.
        var sPref: String? = null
    }
...

}
```

### Java

```java
public class NetworkActivity extends Activity {
    public static final String WIFI = "Wi-Fi";
    public static final String ANY = "Any";
    private static final String URL = "http://stackoverflow.com/feeds/tag?tagnames=android&sort;=newest";

    // Whether there is a Wi-Fi connection.
    private static boolean wifiConnected = false;
    // Whether there is a mobile connection.
    private static boolean mobileConnected = false;
    // Whether the display should be refreshed.
    public static boolean refreshDisplay = true;

    // The user's current network preference setting.
    public static String sPref = null;

    // The BroadcastReceiver that tracks network connectivity changes.
    private NetworkReceiver receiver = new NetworkReceiver();

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        // Registers BroadcastReceiver to track network connection changes.
        IntentFilter filter = new IntentFilter(ConnectivityManager.CONNECTIVITY_ACTION);
        receiver = new NetworkReceiver();
        this.registerReceiver(receiver, filter);
    }

    @Override
    public void onDestroy() {
        super.onDestroy();
        // Unregisters BroadcastReceiver when app is destroyed.
        if (receiver != null) {
            this.unregisterReceiver(receiver);
        }
    }

    // Refreshes the display if the network connection and the
    // pref settings allow it.

    @Override
    public void onStart () {
        super.onStart();

        // Gets the user's network preference settings
        SharedPreferences sharedPrefs = PreferenceManager.getDefaultSharedPreferences(this);

        // Retrieves a string value for the preferences. The second parameter
        // is the default value to use if a preference value is not found.
        sPref = sharedPrefs.getString("listPref", "Wi-Fi");

        updateConnectedFlags();

        if(refreshDisplay){
            loadPage();
        }
    }

    // Checks the network connection and sets the wifiConnected and mobileConnected
    // variables accordingly.
    public void updateConnectedFlags() {
        ConnectivityManager connMgr = (ConnectivityManager)
                getSystemService(Context.CONNECTIVITY_SERVICE);

        NetworkInfo activeInfo = connMgr.getActiveNetworkInfo();
        if (activeInfo != null && activeInfo.isConnected()) {
            wifiConnected = activeInfo.getType() == ConnectivityManager.TYPE_WIFI;
            mobileConnected = activeInfo.getType() == ConnectivityManager.TYPE_MOBILE;
        } else {
            wifiConnected = false;
            mobileConnected = false;
        }
    }

    // Uses AsyncTask subclass to download the XML feed from stackoverflow.com.
    public void loadPage() {
        if (((sPref.equals(ANY)) && (wifiConnected || mobileConnected))
                || ((sPref.equals(WIFI)) && (wifiConnected))) {
            // AsyncTask subclass
            new DownloadXmlTask().execute(URL);
        } else {
            showErrorPage();
        }
    }
...

}
```

## Detect connection changes

The final piece of the puzzle is the
[`BroadcastReceiver`](https://developer.android.com/reference/android/content/BroadcastReceiver) subclass,
`NetworkReceiver`. When the device's network connection changes,
`NetworkReceiver` intercepts the action
[`CONNECTIVITY_ACTION`](https://developer.android.com/reference/android/net/ConnectivityManager#CONNECTIVITY_ACTION),
determines what the network connection status is, and sets the flags
`wifiConnected` and `mobileConnected` to true/false accordingly. The upshot is
that the next time the user returns to the app, the app will only download the
latest feed and update the display if `NetworkActivity.refreshDisplay` is set to
`true`.

Setting up a `BroadcastReceiver` that gets called unnecessarily can be a drain
on system resources. The sample application registers the `BroadcastReceiver`
`NetworkReceiver` in
[`onCreate()`](https://developer.android.com/reference/android/app/Activity#onCreate(android.os.Bundle)),
and it unregisters it in
[`onDestroy()`](https://developer.android.com/reference/android/app/Activity#onDestroy()). This is more
lightweight than declaring a `<receiver>` in the manifest. When you
declare a `<receiver>` in the manifest, it can wake up your app at any
time, even if you haven't run it for weeks. By registering and unregistering
`NetworkReceiver` within the main activity, you ensure that the app won't
be woken up after the user leaves the app. If you do declare a
`<receiver>` in the manifest and you know exactly where you need it, you
can use
[`setComponentEnabledSetting()`](https://developer.android.com/reference/android/content/pm/PackageManager#setComponentEnabledSetting(android.content.ComponentName,%20int,%20int))
to enable and disable it as appropriate.

Here is `NetworkReceiver`:

### Kotlin

```kotlin
class NetworkReceiver : BroadcastReceiver() {

    override fun onReceive(context: Context, intent: Intent) {
        val conn = context.getSystemService(Context.CONNECTIVITY_SERVICE) as ConnectivityManager
        val networkInfo: NetworkInfo? = conn.activeNetworkInfo

        // Checks the user prefs and the network connection. Based on the result, decides whether
        // to refresh the display or keep the current display.
        // If the userpref is Wi-Fi only, checks to see if the device has a Wi-Fi connection.
        if (WIFI == sPref && networkInfo?.type == ConnectivityManager.TYPE_WIFI) {
            // If device has its Wi-Fi connection, sets refreshDisplay
            // to true. This causes the display to be refreshed when the user
            // returns to the app.
            refreshDisplay = true
            Toast.makeText(context, R.string.wifi_connected, Toast.LENGTH_SHORT).show()

            // If the setting is ANY network and there is a network connection
            // (which by process of elimination would be mobile), sets refreshDisplay to true.
        } else if (ANY == sPref && networkInfo != null) {
            refreshDisplay = true

            // Otherwise, the app can't download content--either because there is no network
            // connection (mobile or Wi-Fi), or because the pref setting is WIFI, and there
            // is no Wi-Fi connection.
            // Sets refreshDisplay to false.
        } else {
            refreshDisplay = false
            Toast.makeText(context, R.string.lost_connection, Toast.LENGTH_SHORT).show()
        }
    }
}
```

### Java

```java
public class NetworkReceiver extends BroadcastReceiver {

    @Override
    public void onReceive(Context context, Intent intent) {
        ConnectivityManager conn =  (ConnectivityManager)
            context.getSystemService(Context.CONNECTIVITY_SERVICE);
        NetworkInfo networkInfo = conn.getActiveNetworkInfo();

        // Checks the user prefs and the network connection. Based on the result, decides whether
        // to refresh the display or keep the current display.
        // If the userpref is Wi-Fi only, checks to see if the device has a Wi-Fi connection.
        if (WIFI.equals(sPref) && networkInfo != null
            && networkInfo.getType() == ConnectivityManager.TYPE_WIFI) {
            // If device has its Wi-Fi connection, sets refreshDisplay
            // to true. This causes the display to be refreshed when the user
            // returns to the app.
            refreshDisplay = true;
            Toast.makeText(context, R.string.wifi_connected, Toast.LENGTH_SHORT).show();

        // If the setting is ANY network and there is a network connection
        // (which by process of elimination would be mobile), sets refreshDisplay to true.
        } else if (ANY.equals(sPref) && networkInfo != null) {
            refreshDisplay = true;

        // Otherwise, the app can't download content--either because there is no network
        // connection (mobile or Wi-Fi), or because the pref setting is WIFI, and there
        // is no Wi-Fi connection.
        // Sets refreshDisplay to false.
        } else {
            refreshDisplay = false;
            Toast.makeText(context, R.string.lost_connection, Toast.LENGTH_SHORT).show();
        }
    }
}
```