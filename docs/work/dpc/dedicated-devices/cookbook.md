---
title: https://developer.android.com/work/dpc/dedicated-devices/cookbook
url: https://developer.android.com/work/dpc/dedicated-devices/cookbook
source: md.txt
---

# Dedicated devices cookbook

This cookbook helps developers and system integrators enhance their dedicated device solution. Follow our how-to recipes to find solutions for dedicated-device behaviors. This cookbook works best for developers that already have a dedicated device app---if you're just getting started, read[Dedicated devices overview](https://developer.android.com/work/dpc/dedicated-devices).

## Custom Home apps

These recipes are useful if you're developing an app to replace the Android Home screen and Launcher.

### Be the home app

You can set your app as the device's home app so that it's launched automatically when the device starts up. You can also[enable the Home button](https://developer.android.com/work/dpc/dedicated-devices/lock-task-mode#customize-ui)that brings your allowlisted app to the foreground in lock task mode.

All home apps handle the[`CATEGORY_HOME`](https://developer.android.com/reference/android/content/Intent#CATEGORY_HOME)intent category---this is how the system recognizes a home app. To become the default home app, set one of your app's activities as the preferred Home intent handler, by calling[`DevicePolicyManager.addPersistentPreferredActivity()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#addPersistentPreferredActivity(android.content.ComponentName,%20android.content.IntentFilter,%20android.content.ComponentName))as shown in the following example:  

### Kotlin

```kotlin
// Create an intent filter to specify the Home category.
val filter = IntentFilter(Intent.ACTION_MAIN)
filter.addCategory(Intent.CATEGORY_HOME)
filter.addCategory(Intent.CATEGORY_DEFAULT)

// Set the activity as the preferred option for the device.
val activity = ComponentName(context, KioskModeActivity::class.java)
val dpm = context.getSystemService(Context.DEVICE_POLICY_SERVICE)
        as DevicePolicyManager
dpm.addPersistentPreferredActivity(adminName, filter, activity)
```

### Java

```java
// Create an intent filter to specify the Home category.
IntentFilter filter = new IntentFilter(Intent.ACTION_MAIN);
filter.addCategory(Intent.CATEGORY_HOME);
filter.addCategory(Intent.CATEGORY_DEFAULT);

// Set the activity as the preferred option for the device.
ComponentName activity = new ComponentName(context, KioskModeActivity.class);
DevicePolicyManager dpm =
    (DevicePolicyManager) context.getSystemService(Context.DEVICE_POLICY_SERVICE);
dpm.addPersistentPreferredActivity(adminName, filter, activity);
```

You still need to declare the[intent filter](https://developer.android.com/guide/components/intents-filters)in your app manifest file as shown in the following XML snippet:  

    <activity
            android:name=".KioskModeActivity"
            android:label="@string/kiosk_mode"
            android:launchMode="singleInstance"
            android:excludeFromRecents="true">
        <intent-filter>
            <action android:name="android.intent.action.MAIN"/>
            <category android:name="android.intent.category.HOME"/>
            <category android:name="android.intent.category.DEFAULT"/>
        </intent-filter>
    </activity>

Typically you don't want your launcher app to appear in the Overview screen. However, you don't need to add[`excludeFromRecents`](https://developer.android.com/guide/topics/manifest/activity-element#exclude)to the activity declaration because Android's Launcher hides the initially launched activity when the system is running in lock task mode.

### Show separate tasks

[`FLAG_ACTIVITY_NEW_TASK`](https://developer.android.com/reference/android/content/Intent#FLAG_ACTIVITY_NEW_TASK)can be a useful flag for launcher-type apps because each new task appears as a separate item in the Overview screen. To learn more about tasks in the Overview screen, read[Recents Screen](https://developer.android.com/guide/components/activities/recents).

## Public kiosks

These recipes are great for unattended devices in public spaces but can also help many dedicated device users focus on their tasks.

### Lock down the device

To help make sure that devices are used for their intended purpose, you can add the user restrictions listed in table 1.

|                                                        User restriction                                                         |                                                                                                                                                 Description                                                                                                                                                 |
|---------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`DISALLOW_FACTORY_RESET`](https://developer.android.com/reference/android/os/UserManager#DISALLOW_FACTORY_RESET)               | Prevents a device user resetting the device to its factory defaults. Admins of fully managed devices and the primary user can set this restriction.                                                                                                                                                         |
| [`DISALLOW_SAFE_BOOT`](https://developer.android.com/reference/android/os/UserManager#DISALLOW_SAFE_BOOT)                       | Prevents a device user starting the device in[safe mode](https://source.android.com/security/overview/kernel-security#system-partition-and-safe-mode)where the system won't automatically launch your app. Admins of fully managed devices and the primary user can set this restriction.                   |
| [`DISALLOW_MOUNT_PHYSICAL_MEDIA`](https://developer.android.com/reference/android/os/UserManager#DISALLOW_MOUNT_PHYSICAL_MEDIA) | Prevents the device user from mounting any storage volumes they might attach to the device. Admins of fully managed devices and the primary user can set this restriction.                                                                                                                                  |
| [`DISALLOW_ADJUST_VOLUME`](https://developer.android.com/reference/android/os/UserManager#DISALLOW_ADJUST_VOLUME)               | Mutes the device and prevents the device user from changing the sound volume and vibration settings. Check that your kiosk doesn't need audio for media playback or accessibility features. Admins of fully managed devices, the primary user, secondary users, and work profiles can set this restriction. |
| [`DISALLOW_ADD_USER`](https://developer.android.com/reference/android/os/UserManager#DISALLOW_ADD_USER)                         | Prevents the device user adding new users, such as secondary users or restricted users. The system automatically adds this user restriction to fully managed devices but it might have been cleared. Admins of fully managed devices and the primary user can set this restriction.                         |
[**Table 1**. User restrictions for kiosk devices]

The following snippet shows how you can set the restrictions:  

### Kotlin

```kotlin
// If the system is running in lock task mode, set the user restrictions
// for a kiosk after launching the activity.
arrayOf(
        UserManager.DISALLOW_FACTORY_RESET,
        UserManager.DISALLOW_SAFE_BOOT,
        UserManager.DISALLOW_MOUNT_PHYSICAL_MEDIA,
        UserManager.DISALLOW_ADJUST_VOLUME,
        UserManager.DISALLOW_ADD_USER).forEach { dpm.addUserRestriction(adminName, it) }
```

### Java

```java
// If the system is running in lock task mode, set the user restrictions
// for a kiosk after launching the activity.
String[] restrictions = {
    UserManager.DISALLOW_FACTORY_RESET,
    UserManager.DISALLOW_SAFE_BOOT,
    UserManager.DISALLOW_MOUNT_PHYSICAL_MEDIA,
    UserManager.DISALLOW_ADJUST_VOLUME,
    UserManager.DISALLOW_ADD_USER};

for (String restriction: restrictions) dpm.addUserRestriction(adminName, restriction);
```

You might want to remove these restrictions when your app is in an admin mode so that an IT admin could still use these features for device maintenance. To clear the restriction, call[`DevicePolicyManager.clearUserRestriction()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#clearUserRestriction(android.content.ComponentName,%20java.lang.String)).

### Suppress error dialogs

In some environments, such as retail demonstrations or public information displays, you might not want to show error dialogs to users. In Android 9.0 (API level 28) or higher, you can suppress system error dialogs for crashed or unresponsive apps by adding the[`DISALLOW_SYSTEM_ERROR_DIALOGS`](https://developer.android.com/reference/android/os/UserManager#DISALLOW_SYSTEM_ERROR_DIALOGS)user restriction. The system restarts unresponsive apps as if the device user closed the app from the dialog. The following example shows how you can do this:  

### Kotlin

```kotlin
override fun onEnabled(context: Context, intent: Intent) {
    val dpm = getManager(context)
    val adminName = getWho(context)

    dpm.addUserRestriction(adminName, UserManager.DISALLOW_SYSTEM_ERROR_DIALOGS)
}
```

### Java

```java
public void onEnabled(Context context, Intent intent) {
  DevicePolicyManager dpm = getManager(context);
  ComponentName adminName = getWho(context);

  dpm.addUserRestriction(adminName, UserManager.DISALLOW_SYSTEM_ERROR_DIALOGS);
}
```

If an admin of the primary or a secondary user sets this restriction, the system suppresses error dialogs for just that user. If an admin of a fully managed device sets this restriction, the system suppresses dialogs for all users.

### Keep the screen on

If you're building a kiosk, you can[stop a device going to sleep](https://developer.android.com/training/scheduling/wakelock)when it's running your app's activity. Add the[`FLAG_KEEP_SCREEN_ON`](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#FLAG_KEEP_SCREEN_ON)layout flag to your app's window as shown in the following example:  

### Kotlin

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    setContentView(R.layout.activity_main)

    // Keep the screen on and bright while this kiosk activity is running.
    window.addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON)
}
```

### Java

```java
@Override
protected void onCreate(Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);
  setContentView(R.layout.activity_main);

  // Keep the screen on and bright while this kiosk activity is running.
  getWindow().addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON);
}
```

You might want to check that the device is plugged in to an AC, USB, or wireless charger. Register for battery-change broadcasts and use[`BatteryManager`](https://developer.android.com/reference/android/os/BatteryManager)values to discover the charging state. You can even send remote alerts to an IT admin if the device becomes unplugged. For step-by-step instructions, read[Monitor the Battery Level and Charging State](https://developer.android.com/training/monitoring-device-state/battery-monitoring).

You can also set the[`STAY_ON_WHILE_PLUGGED_IN`](https://developer.android.com/reference/android/provider/Settings.Global#STAY_ON_WHILE_PLUGGED_IN)global setting to keep the device awake while connected to a power source. Admins of fully managed devices, in Android 6.0 (API level 23) or higher, can call[`DevicePolicyManager.setGlobalSetting()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setGlobalSetting(android.content.ComponentName,%20java.lang.String,%20java.lang.String))as shown in the following example:  

### Kotlin

```kotlin
val pluggedInto = BatteryManager.BATTERY_PLUGGED_AC or
        BatteryManager.BATTERY_PLUGGED_USB or
        BatteryManager.BATTERY_PLUGGED_WIRELESS
dpm.setGlobalSetting(adminName,
        Settings.Global.STAY_ON_WHILE_PLUGGED_IN, pluggedInto.toString())
```

### Java

```java
int pluggedInto = BatteryManager.BATTERY_PLUGGED_AC |
    BatteryManager.BATTERY_PLUGGED_USB |
    BatteryManager.BATTERY_PLUGGED_WIRELESS;
dpm.setGlobalSetting( adminName,
    Settings.Global.STAY_ON_WHILE_PLUGGED_IN, String.valueOf(pluggedInto));
```

## App packages

This section contains recipes to efficiently install apps onto dedicated devices.

### Cache app packages

If the users of a shared device all share a common set of apps, it makes sense to avoid downloading apps whenever possible. To streamline user provisioning on shared devices with a fixed set of users, such as devices for shift workers, in Android 9.0 (API level 28) or later, you can cache app packages (APKs) that are needed for multi-user sessions.

Installing a cached APK (that's already installed on the device) happens in two stages:

1. The admin component of a fully managed device (or a delegate---[see following](https://developer.android.com/work/dpc/dedicated-devices/cookbook#delegates)) sets the list of APKs to keep on the device.
2. Admin components of affiliated secondary users (or their delegates) can install the cached APK on behalf of the user. Admins of the fully managed device, the primary user, or an affiliated work profile (or their delegates) can also install the cached app if needed.

To set the list of APKs to keep on the device, the admin calls[`DevicePolicyManager.setKeepUninstalledPackages()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setKeepUninstalledPackages(android.content.ComponentName,%20java.util.List%3Cjava.lang.String%3E)). This method doesn't check that the APK is installed on the device---useful if you want to install an app just before you need it for a user. To get a list of previously-set packages, you can call[`DevicePolicyManager.getKeepUninstalledPackages()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getKeepUninstalledPackages(android.content.ComponentName)). After you call`setKeepUninstalledPackages()`with changes, or when a secondary user is deleted, the system deletes any cached APKs that are no longer needed.

To install a cached APK, call[`DevicePolicyManager.installExistingPackage()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#installExistingPackage(android.content.ComponentName,%20java.lang.String)). This method can only install an app that the system has already cached---your dedicated device solution (or the user of a device) must first install the app on the device before you can call this method.

The following sample shows how you could use these API calls in the admin of a fully managed device and secondary user:  

### Kotlin

```kotlin
// Set the package to keep. This method assumes that the package is already
// installed on the device by managed Google Play.
val cachedAppPackageName = "com.example.android.myapp"
dpm.setKeepUninstalledPackages(adminName, listOf(cachedAppPackageName))

// ...

// The admin of a secondary user installs the app.
val success = dpm.installExistingPackage(adminName, cachedAppPackageName)
```

### Java

```java
// Set the package to keep. This method assumes that the package is already
// installed on the device by managed Google Play.
String cachedAppPackageName = "com.example.android.myapp";
List<String> packages = new ArrayList<String>();
packages.add(cachedAppPackageName);
dpm.setKeepUninstalledPackages(adminName, packages);

// ...

// The admin of a secondary user installs the app.
boolean success = dpm.installExistingPackage(adminName, cachedAppPackageName);
```

#### Delegate apps

You can delegate another app to manage app caching. You might do this to separate the features of your solution or offer the ability for IT admins to use their own apps. The delegate app gets the same permissions as the admin component. For example, an app delegate of a secondary user's admin can call`installExistingPackage()`but can't call`setKeepUninstalledPackages()`.

To make a delegate call[`DevicePolicyManager.setDelegatedScopes()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setDelegatedScopes(android.content.ComponentName,%20java.lang.String,%20java.util.List%3Cjava.lang.String%3E))and include[`DELEGATION_KEEP_UNINSTALLED_PACKAGES`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#DELEGATION_KEEP_UNINSTALLED_PACKAGES)in the scopes argument. The following example shows how you can make another app the delegate:  

### Kotlin

```kotlin
var delegatePackageName = "com.example.tools.kept_app_assist"

// Check that the package is installed before delegating.
try {
    context.packageManager.getPackageInfo(delegatePackageName, 0)
    dpm.setDelegatedScopes(
            adminName,
            delegatePackageName,
            listOf(DevicePolicyManager.DELEGATION_KEEP_UNINSTALLED_PACKAGES))
} catch (e: PackageManager.NameNotFoundException) {
    // The delegate app isn't installed. Send a report to the IT admin ...
}
```

### Java

```java
String delegatePackageName = "com.example.tools.kept_app_assist";

// Check that the package is installed before delegating.
try {
  context.getPackageManager().getPackageInfo(delegatePackageName, 0);
  dpm.setDelegatedScopes(
      adminName,
      delegatePackageName,
      Arrays.asList(DevicePolicyManager.DELEGATION_KEEP_UNINSTALLED_PACKAGES));
} catch (PackageManager.NameNotFoundException e) {
  // The delegate app isn't installed. Send a report to the IT admin ...
}
```

If everything goes well, the delegate app receives the[`ACTION_APPLICATION_DELEGATION_SCOPES_CHANGED`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#ACTION_APPLICATION_DELEGATION_SCOPES_CHANGED)broadcast and becomes the delegate. The app can call the methods in this guide as if it were the device owner or profile owner. When calling`DevicePolicyManager`methods, the delegate passes`null`for the admin component argument.

### Install app packages

Sometimes it's useful to install a locally-cached custom app onto a dedicated device. For example, dedicated devices are frequently deployed to bandwidth-limited environments or areas without any internet connectivity. Your dedicated device solution should be mindful of your customers' bandwidth. Your app can start the installation of another app package (APK) using the[`PackageInstaller`](https://developer.android.com/reference/android/content/pm/PackageInstaller)classes.
| **Caution:** Use the PackageInstaller APIs to install custom or private apps. Always get the permission of the app developer before installing their app. The[Google Play Terms of Service](https://play.google.com/about/play-terms.html)doesn't allow you to download and install apps from Google Play using these APIs.

While any app can install APKs,[admins](https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver)on fully managed devices can install (or uninstall) packages without user interaction. The admin might manage the device, an affiliated secondary user, or an affiliated work profile. After finishing the installation, the system posts a notification that all device users see. The notification informs device users that the app was installed (or updated) by their admin.

|           Android version            |                  Admin component for install and uninstall                   |
|--------------------------------------|------------------------------------------------------------------------------|
| Android 9.0 (API level 28) or higher | Affiliated secondary users and work profiles---both on fully managed devices |
| Android 6.0 (API level 23) or higher | Fully managed devices                                                        |
[**Table 2**. Android versions supporting package installation without user interaction]

How you distribute one or more copies of the APK to dedicated devices will depend on how remote the devices are and possibly by how far apart the devices are from one another. Your solution needs to follow security best practices before installing APKs onto dedicated devices.

You can use[`PackageInstaller.Session`](https://developer.android.com/reference/android/content/pm/PackageInstaller)to create a session that queues one or more APKs for installation. In the following example we receive status feedback in our activity ([singleTop](https://developer.android.com/guide/topics/manifest/activity-element#lmode)mode) but you could use a service or broadcast receiver:  

### Kotlin

```kotlin
// First, create a package installer session.
val packageInstaller = context.packageManager.packageInstaller
val params = PackageInstaller.SessionParams(
        PackageInstaller.SessionParams.MODE_FULL_INSTALL)
val sessionId = packageInstaller.createSession(params)
val session = packageInstaller.openSession(sessionId)

// Add the APK binary to the session. The APK is included in our app binary
// and is read from res/raw but file storage is a more typical location.
// The I/O streams can't be open when installation begins.
session.openWrite("apk", 0, -1).use { output ->
    getContext().resources.openRawResource(R.raw.app).use { input ->
        input.copyTo(output, 2048)
    }
}

// Create a status receiver to report progress of the installation.
// We'll use the current activity.
// Here we're requesting status feedback to our Activity but this can be a
// service or broadcast receiver.
val intent = Intent(context, activity.javaClass)
intent.action = "com.android.example.APK_INSTALLATION_ACTION"
val pendingIntent = PendingIntent.getActivity(context, 0, intent, 0)
val statusReceiver = pendingIntent.intentSender

// Start the installation. Because we're an admin of a fully managed device,
// there isn't any user interaction.
session.commit(statusReceiver)
```

### Java

```java
// First, create a package installer session.
PackageInstaller packageInstaller = context.getPackageManager().getPackageInstaller();
PackageInstaller.SessionParams params = new PackageInstaller.SessionParams(
    PackageInstaller.SessionParams.MODE_FULL_INSTALL);
int sessionId = packageInstaller.createSession(params);
PackageInstaller.Session session = packageInstaller.openSession(sessionId);

// Add the APK binary to the session. The APK is included in our app binary
// and is read from res/raw but file storage is a more typical location.
try (
    // These I/O streams can't be open when installation begins.
    OutputStream output = session.openWrite("apk", 0, -1);
    InputStream input = getContext().getResources().openRawResource(R.raw.app);
) {
  byte[] buffer = new byte[2048];
  int n;
  while ((n = input.read(buffer)) >= 0) {
    output.write(buffer, 0, n);
  }
}

// Create a status receiver to report progress of the installation.
// We'll use the current activity.
// Here we're requesting status feedback to our Activity but this can be a
// service or broadcast receiver.
Intent intent = new Intent(context, getActivity().getClass());
intent.setAction("com.android.example.APK_INSTALLATION_ACTION");
PendingIntent pendingIntent = PendingIntent.getActivity(context, 0, intent, 0);
IntentSender statusReceiver = pendingIntent.getIntentSender();

// Start the installation. Because we're an admin of a fully managed device,
// there isn't any user interaction.
session.commit(statusReceiver);
```

The session sends status feedback about the installation using intents. Check each intent's[`EXTRA_STATUS`](https://developer.android.com/reference/android/content/pm/PackageInstaller#EXTRA_STATUS)field to get the[status](https://developer.android.com/reference/android/content/pm/PackageInstaller#STATUS_SUCCESS). Remember, admins don't receive the[`STATUS_PENDING_USER_ACTION`](https://developer.android.com/reference/android/content/pm/PackageInstaller#STATUS_PENDING_USER_ACTION)status update because the device user doesn't need to approve the installation.

To uninstall apps, you can call[`PackageInstaller.uninstall`](https://developer.android.com/reference/android/content/pm/PackageInstaller#uninstall(java.lang.String,%20android.content.IntentSender)). Admins of fully managed devices, users, and work profiles can uninstall packages without user interaction running supported Android versions (see[table 2](https://developer.android.com/work/dpc/dedicated-devices/cookbook#t-2)).

## Freeze system updates

Android devices receive over-the-air (OTA) updates to the system and application software. To freeze the OS version over critical periods, such as holidays or other busy times, dedicated devices can suspend OTA system updates for up to 90 days. To learn more, read[Manage system updates](https://developer.android.com/work/dpc/system-updates).

## Remote config

Android's[managed configurations](https://developer.android.com/work/managed-configurations)allow IT admins to remotely configure your app. You might want to expose settings such as allowlists, network hosts, or content URLs to make your app more useful to IT admins.

If your app exposes its config, remember to include the settings in your documentation. To learn more about exposing your app's config and reacting to changes in settings, read[Set up managed configurations](https://developer.android.com/work/managed-configurations).

## Development setup

While you're developing your solution for dedicated devices, it's sometimes useful to set your app as the admin of a fully managed device without a factory reset. To set the admin of a fully managed device, follow these steps:

1. Build and install your device policy controller (DPC) app on the device.
2. Check that there are no accounts on the device.
3. Run the following command in the[Android Debug Bridge](https://developer.android.com/studio/command-line/adb)(adb) shell. You need to replace`com.example.dpc/.MyDeviceAdminReceiver`in the example with your app's admin component name:

   ```
   adb shell dpm set-device-owner com.example.dpc/.MyDeviceAdminReceiver
   ```

To help customers deploy your solution, you'll need to look at[other enrollment methods](https://developers.google.com/android/work/play/emm-api/prov-devices). We recommend[QR-code enrollment](https://developers.google.com/android/work/play/emm-api/prov-devices#qr_code_method)for dedicated devices.

## Additional resources

To learn more about dedicated devices, read the following documents:

- [Manage dedicated devices](https://developer.android.com/work/dpc/dedicated-devices)
- [Lock task mode](https://developer.android.com/work/dpc/dedicated-devices/lock-task-mode)
- [Manage multiple users](https://developer.android.com/work/dpc/dedicated-devices/multiple-users)