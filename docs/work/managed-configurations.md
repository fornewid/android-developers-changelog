---
title: https://developer.android.com/work/managed-configurations
url: https://developer.android.com/work/managed-configurations
source: md.txt
---

# Set up managed configurations

If you are developing apps for the enterprise market, you may need to satisfy particular requirements set by a organization's policies. Managed configurations, previously known as*application restrictions*, allow the organization's IT admin to remotely specify settings for apps. This capability is particularly useful for organization-approved apps deployed to a work profile.

For example, an organization might require that approved apps allow the IT admin to:

- Allow or block URLs for a web browser
- Configure whether an app is allowed to sync content via cellular, or just by Wi-Fi
- Configure the app's email settings

This guide shows how to implement managed configuration settings in your app. To view sample apps with a managed configuration, see[ManagedConfigurations](https://github.com/android/enterprise-samples/tree/main/ManagedConfigurations#readme). If you're an enterprise mobility management (EMM) developer, refer to the[Android Management API guide](https://developers.google.com/android/management).

**Note:** For historical reasons, these configuration settings are known as*restrictions,* and are implemented with files and classes that use this term (such as[RestrictionsManager](https://developer.android.com/reference/android/content/RestrictionsManager)). However, these restrictions can actually implement a wide range of configuration options, not just restrictions on app functionality.

## Remote configuration overview

Apps define the managed configuration options that can be remotely set by an IT admin. These are arbitrary settings that can be changed by a managed configuration provider. If your app is running in a work profile, the IT admin can change your app's managed configuration.

The managed configurations provider is another app running on the same device. This app is typically controlled by the IT admin. The IT admin communicates configuration changes to the managed configuration provider app. That app, in turn, changes the configurations on your app.

To provide externally managed configurations:

- Declare the managed configurations in your app manifest. Doing so allows the IT admin to read the app's configurations through Google Play APIs.
- Whenever the app resumes, use the[RestrictionsManager](https://developer.android.com/reference/android/content/RestrictionsManager)object to check the current managed configurations, and change your app's UI and behavior to conform with those configurations.
- Listen for the[ACTION_APPLICATION_RESTRICTIONS_CHANGED](https://developer.android.com/reference/android/content/Intent#ACTION_APPLICATION_RESTRICTIONS_CHANGED)intent. When you receive this broadcast, check the[RestrictionsManager](https://developer.android.com/reference/android/content/RestrictionsManager)to see what the current managed configurations are, and make any necessary changes to your app's behavior.

## Define managed configurations

Your app can support any managed configuration you want to define. You declare the app's managed configurations in a*managed configurations file*, and declare the configurations file in the manifest. Creating a configurations file allows other apps to examine the managed configurations your app provides. EMM partners can read your app's configurations by using Google Play APIs.

To define your app's remote configuration options, put the following element in your manifest's[`<application>`](https://developer.android.com/guide/topics/manifest/application-element)element:  

```xml
<meta-data android:name="android.content.APP_RESTRICTIONS"
    android:resource="@xml/app_restrictions" />
```

Create a file named`app_restrictions.xml`in your app's`res/xml`directory. The structure of that file is described in the reference for[RestrictionsManager](https://developer.android.com/reference/android/content/RestrictionsManager). The file has a single top-level`<restrictions>`element, which contains one`<restriction>`child element for every configuration option the app has.

**Note:**Do not create localized versions of the managed configuration file. Your app is only allowed to have a single managed configurations file, so configurations will be consistent for your app in all locales.

In an enterprise environment, an EMM will typically use the managed configuration schema to generate a remote console for IT admins, so the admins can remotely configure your application.

The managed configuration provider can query the app to find details on the app's available configurations, including their description text. The configurations provider and IT admin can change your app's managed configurations at any time, even when the app is not running.

For example, suppose your app can be remotely configured to allow or forbid it to download data over a cellular connection. Your app could have a`<restriction>`element like this:  

```xml
<?xml version="1.0" encoding="utf-8"?>
<restrictions xmlns:android="http://schemas.android.com/apk/res/android">

  <restriction
    android:key="downloadOnCellular"
    android:title="@string/download_on_cell_title"
    android:restrictionType="bool"
    android:description="@string/download_on_cell_description"
    android:defaultValue="true" />

</restrictions>
```

You use each configuration's`android:key`attribute to read its value from a managed configuration bundle. For this reason, each configuration must have a unique key string, and the string*cannot*be localized. It must be specified with a string literal.

**Note:** In a production app,`android:title`and`android:description`should be drawn from a localized resource file, as described in[Localizing with Resources](https://developer.android.com/guide/topics/resources/localization).

An app defines restrictions using bundles within a[bundle_array](https://developer.android.com/reference/android/content/RestrictionEntry#TYPE_BUNDLE_ARRAY). For example, an app with multiple VPN connection options could define each VPN server configuration in a[bundle](https://developer.android.com/reference/android/content/RestrictionEntry#TYPE_BUNDLE), with multiple bundles grouped together in a bundle array:  

```xml
<?xml version="1.0" encoding="utf-8"?>
<restrictions xmlns:android="http://schemas.android.com/apk/res/android" >

  <restriction
    android:key="vpn_configuration_list"
    android:restrictionType="bundle_array">
    <restriction
      android:key="vpn_configuration"
      android:restrictionType="bundle">
      <restriction
        android:key="vpn_server"
        android:restrictionType="string"/>
      <restriction
        android:key="vpn_username"
        android:restrictionType="string"/>
      <restriction
        android:key="vpn_password"
        android:restrictionType="string"/>
    </restriction>
  </restriction>

</restrictions>
```

The supported types for the`android:restrictionType`element are listed in[Table 1](https://developer.android.com/work/managed-configurations#restriction-types)and documented in the reference for[RestrictionsManager](https://developer.android.com/reference/android/content/RestrictionsManager)and[RestrictionEntry](https://developer.android.com/reference/android/content/RestrictionEntry).

**Table 1.**Restriction entry types and usage.

|                                                      Type                                                       | android:restrictionType |                                                                                              Typical usage                                                                                               |
|-----------------------------------------------------------------------------------------------------------------|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [TYPE_BOOLEAN](https://developer.android.com/reference/android/content/RestrictionEntry#TYPE_BOOLEAN)           | `"bool"`                | A boolean value, true or false.                                                                                                                                                                          |
| [TYPE_STRING](https://developer.android.com/reference/android/content/RestrictionEntry#TYPE_STRING)             | `"string"`              | A string value, such as a name.                                                                                                                                                                          |
| [TYPE_INTEGER](https://developer.android.com/reference/android/content/RestrictionEntry#TYPE_INTEGER)           | `"integer"`             | An integer with a value from[MIN_VALUE](https://developer.android.com/reference/java/lang/Integer#MIN_VALUE)to[MAX_VALUE](https://developer.android.com/reference/java/lang/Integer#MAX_VALUE).          |
| [TYPE_CHOICE](https://developer.android.com/reference/android/content/RestrictionEntry#TYPE_CHOICE)             | `"choice"`              | A string value selected from`android:entryValues`, typically presented as a single-select list.                                                                                                          |
| [TYPE_MULTI_SELECT](https://developer.android.com/reference/android/content/RestrictionEntry#TYPE_MULTI_SELECT) | `"multi-select"`        | A string array with values selected from`android:entryValues`. Use this for presenting a multi-select list where more than one entry can be selected, such as for choosing specific titles to allowlist. |
| [TYPE_NULL](https://developer.android.com/reference/android/content/RestrictionEntry#TYPE_NULL)                 | `"hidden"`              | Hidden restriction type. Use this type for information that needs to be transferred across but shouldn't be presented to the user in the UI. Stores a single string value.                               |
| [TYPE_BUNDLE_ARRAY](https://developer.android.com/reference/android/content/RestrictionEntry#TYPE_BUNDLE_ARRAY) | `"bundle_array"`        | Use this for storing arrays of restriction[bundles](https://developer.android.com/reference/android/os/Bundle). Available in Android 6.0 (API level 23).                                                 |

**Note:** `android:entryValues`are machine readable and cannot be localized. Use`android:entries`to present human-readable values that can be localized. Each entry must have a corresponding index in`android:entryValues`.

## Check managed configurations

Your app is not automatically notified when other apps change its configuration settings. Instead, you need to check what the managed configurations are when your app starts or resumes, and listen for a system intent to find out if the configurations change while your app is running.

To find out the current configuration settings, your app uses a[RestrictionsManager](https://developer.android.com/reference/android/content/RestrictionsManager)object. Your app should check for the current managed configurations at the following times:

- When the app starts or resumes, in its[onResume()](https://developer.android.com/reference/android/app/Activity#onResume())method
- When the app is notified of a configuration change, as described in[Listen for Managed Configuration Changes](https://developer.android.com/work/managed-configurations#listen-configuration)

To get a[RestrictionsManager](https://developer.android.com/reference/android/content/RestrictionsManager)object, get the current activity with[getActivity()](https://developer.android.com/reference/android/app/Fragment#getActivity()), then call that activity's[Activity.getSystemService()](https://developer.android.com/reference/android/content/Context#getSystemService(java.lang.Class<T>))method:  

### Kotlin

```kotlin
var myRestrictionsMgr =
        activity?.getSystemService(Context.RESTRICTIONS_SERVICE) as RestrictionsManager
```

### Java

```java
RestrictionsManager myRestrictionsMgr =
    (RestrictionsManager) getActivity()
        .getSystemService(Context.RESTRICTIONS_SERVICE);
```

Once you have a[RestrictionsManager](https://developer.android.com/reference/android/content/RestrictionsManager), you can get the current configuration settings by calling its[getApplicationRestrictions()](https://developer.android.com/reference/android/content/RestrictionsManager#getApplicationRestrictions())method:  

### Kotlin

```kotlin
var appRestrictions: Bundle = myRestrictionsMgr.applicationRestrictions
```

### Java

```java
Bundle appRestrictions = myRestrictionsMgr.getApplicationRestrictions();
```

**Note:** For convenience, you can also fetch the current configurations with a[UserManager](https://developer.android.com/reference/android/os/UserManager), by calling[UserManager.getApplicationRestrictions()](https://developer.android.com/reference/android/os/UserManager#getApplicationRestrictions(java.lang.String)). This method behaves exactly the same as[RestrictionsManager.getApplicationRestrictions()](https://developer.android.com/reference/android/content/RestrictionsManager#getApplicationRestrictions()).

The[getApplicationRestrictions()](https://developer.android.com/reference/android/content/RestrictionsManager#getApplicationRestrictions())method requires reading from data storage, so it should be done sparingly. Do not call this method every time you need to know the current configuration. Instead, you should call it once when your app starts or resumes, and cache the fetched managed configurations bundle. Then listen for the[ACTION_APPLICATION_RESTRICTIONS_CHANGED](https://developer.android.com/reference/android/content/Intent#ACTION_APPLICATION_RESTRICTIONS_CHANGED)intent to find out if the configuration change while your app is active, as described in[Listen for Managed Configuration Changes](https://developer.android.com/work/managed-configurations#listen-configuration).

### Reading and applying managed configurations

The[getApplicationRestrictions()](https://developer.android.com/reference/android/content/RestrictionsManager#getApplicationRestrictions())method returns a[Bundle](https://developer.android.com/reference/android/os/Bundle)containing a key-value pair for each configuration that has been set. The values are all of type`Boolean`,`int`,`String`, and`String[]`. Once you have the managed configurations[Bundle](https://developer.android.com/reference/android/os/Bundle), you can check the current configuration settings with the standard[Bundle](https://developer.android.com/reference/android/os/Bundle)methods for those data types, such as[getBoolean()](https://developer.android.com/reference/android/os/BaseBundle#getBoolean(java.lang.String))or[getString()](https://developer.android.com/reference/android/os/BaseBundle#getString(java.lang.String)).

**Note:** The managed configurations[Bundle](https://developer.android.com/reference/android/os/Bundle)contains one item for every configuration that has been explicitly set by a managed configurations provider. However, you*cannot*assume that a configuration will be present in the bundle just because you defined a default value in the managed configurations XML file.

It is up to your app to take appropriate action based on the current managed configuration settings. For example, if your app has a configuration specifying whether it can download data over a cellular connection, and you find that the configuration is set to`false`, you would have to disable data download except when the device has a Wi-Fi connection, as shown in the following example code:  

### Kotlin

```kotlin
val appCanUseCellular: Boolean =
        if (appRestrictions.containsKey("downloadOnCellular")) {
            appRestrictions.getBoolean("downloadOnCellular")
        } else {
            // cellularDefault is a boolean using the restriction's default value
            cellularDefault
        }

if (!appCanUseCellular) {
    // ...turn off app's cellular-download functionality
    // ...show appropriate notices to user
}
```

### Java

```java
boolean appCanUseCellular;

if (appRestrictions.containsKey("downloadOnCellular")) {
    appCanUseCellular = appRestrictions.getBoolean("downloadOnCellular");
} else {
    // cellularDefault is a boolean using the restriction's default value
    appCanUseCellular = cellularDefault;
}

if (!appCanUseCellular) {
    // ...turn off app's cellular-download functionality
    // ...show appropriate notices to user
}
```

To apply multiple[nested restrictions](https://developer.android.com/work/managed-configurations#nested-restrictions), read the[bundle_array](https://developer.android.com/reference/android/content/RestrictionEntry#TYPE_BUNDLE_ARRAY)restriction entry as a collection of[Parcelable](https://developer.android.com/reference/android/os/Parcelable)objects and cast as a[Bundle](https://developer.android.com/reference/android/os/Bundle). In this example, each VPN's configuration data is parsed and used to build a list of server connection choices:  

### Kotlin

```kotlin
// VpnConfig is a sample class used store config data, not defined
val vpnConfigs = mutableListOf<VpnConfig>()

val parcelables: Array<out Parcelable>? =
        appRestrictions.getParcelableArray("vpn_configuration_list")

if (parcelables?.isNotEmpty() == true) {
    // iterate parcelables and cast as bundle
    parcelables.map { it as Bundle }.forEach { vpnConfigBundle ->
        // parse bundle data and store in VpnConfig array
        vpnConfigs.add(VpnConfig()
                .setServer(vpnConfigBundle.getString("vpn_server"))
                .setUsername(vpnConfigBundle.getString("vpn_username"))
                .setPassword(vpnConfigBundle.getString("vpn_password")))
    }
}

if (vpnConfigs.isNotEmpty()) {
    // ...choose a VPN configuration or prompt user to select from list
}
```

### Java

```java
// VpnConfig is a sample class used store config data, not defined
List<VpnConfig> vpnConfigs = new ArrayList<>();

Parcelable[] parcelables =
    appRestrictions.getParcelableArray("vpn_configuration_list");

if (parcelables != null && parcelables.length > 0) {
    // iterate parcelables and cast as bundle
    for (int i = 0; i < parcelables.length; i++) {
        Bundle vpnConfigBundle = (Bundle) parcelables[i];
        // parse bundle data and store in VpnConfig array
        vpnConfigs.add(new VpnConfig()
            .setServer(vpnConfigBundle.getString("vpn_server"))
            .setUsername(vpnConfigBundle.getString("vpn_username"))
            .setPassword(vpnConfigBundle.getString("vpn_password")));
    }
}

if (!vpnConfigs.isEmpty()) {
    // ...choose a VPN configuration or prompt user to select from list
}
```

## Listen for managed configuration changes

Whenever an app's managed configurations are changed, the system fires the[ACTION_APPLICATION_RESTRICTIONS_CHANGED](https://developer.android.com/reference/android/content/Intent#ACTION_APPLICATION_RESTRICTIONS_CHANGED)intent. Your app has to listen for this intent so you can change the app's behavior when the configuration settings change.

**Note:** The[ACTION_APPLICATION_RESTRICTIONS_CHANGED](https://developer.android.com/reference/android/content/Intent#ACTION_APPLICATION_RESTRICTIONS_CHANGED)intent is sent only to listeners that are dynamically registered,*not*to listeners that are declared in the app manifest.

The following code shows how to dynamically register a broadcast receiver for this intent:  

### Kotlin

```kotlin
val restrictionsFilter = IntentFilter(Intent.ACTION_APPLICATION_RESTRICTIONS_CHANGED)

val restrictionsReceiver = object : BroadcastReceiver() {
    override fun onReceive(context: Context, intent: Intent) {

        // Get the current configuration bundle
        val appRestrictions = myRestrictionsMgr.applicationRestrictions

        // Check current configuration settings, change your app's UI and
        // functionality as necessary.
    }
}

registerReceiver(restrictionsReceiver, restrictionsFilter)
```

### Java

```java
IntentFilter restrictionsFilter =
    new IntentFilter(Intent.ACTION_APPLICATION_RESTRICTIONS_CHANGED);

BroadcastReceiver restrictionsReceiver = new BroadcastReceiver() {
  @Override public void onReceive(Context context, Intent intent) {

    // Get the current configuration bundle
    Bundle appRestrictions = myRestrictionsMgr.getApplicationRestrictions();

    // Check current configuration settings, change your app's UI and
    // functionality as necessary.
  }
};

registerReceiver(restrictionsReceiver, restrictionsFilter);
```

**Note:** Ordinarily, your app does not need to be notified about configuration changes when it is paused. Instead, you should unregister your broadcast receiver when the app is paused. When the app resumes, you first check for the current managed configurations (as discussed in[Check Managed Configurations](https://developer.android.com/work/managed-configurations#check-configuration)), then register your broadcast receiver to make sure you're notified about configuration changes that happen while the app is active.

## Send managed configuration feedback to EMMs

After applying managed configuration changes to your app, it's best practice to notify EMMs of the status of the change. Android supports a feature called*keyed app states*, which you can use to send feedback each time your app attempts to apply managed configuration changes. This feedback can act as confirmation that your app set managed configurations successfully or it can include an error message if your app failed to apply the specified changes.

EMM providers are capable of retrieving this feedback and displaying it in their consoles for IT admins to view. See[Send app feedback to EMMs](https://developer.android.com/work/app-feedback/overview)for more information on the topic, including a detailed guide on how to add feedback support to your app.

## Additional code samples

The[ManagedConfigurations](https://github.com/android/enterprise-samples/tree/main/ManagedConfigurations)sample further demonstrates the use of the APIs covered on this page.

## Allowlisting/blocklisting apps on the personal profile

Third-party app stores may express interest in using Managed Configurations to have a reliable way to apply an app blocklist or allowlist to both the personal profile and the[Private Space](https://source.android.com/docs/security/features/private-space)consumer feature, which is an additional personal space for users to keep their sensitive apps. If you develop an app store for enterprise usage and would like to use this feature, submit[this form](https://goo.gle/android-enterprise-response)to express interest and select*Interest in 3P app store allowlisting* as the*Reason for Response*in the form.