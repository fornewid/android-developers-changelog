---
title: https://developer.android.com/work/dpc/build-dpc
url: https://developer.android.com/work/dpc/build-dpc
source: md.txt
---

# Build a device policy controller

| **Caution:** Android Enterprise is no longer accepting new registrations for custom device policy controllers (DPCs) to the Google Play EMM API. To get your DPC approved by Android Enterprise for device management, visit[the DPC approval support page](https://support.google.com/work/android/answer/16694822).[Learn more](https://developers.google.com/android/work/play/emm-api/register).

This guide describes how to develop a*device policy controller* (DPC) for devices in an Android enterprise deployment. A DPC app, previously known as a*work policy controller*, controls local device policies and system applications on devices.
| **Note:** This guide does not cover the situation where the work profile, under the enterprise's control, is the only profile on the device. See[Deployment scenarios](https://developers.google.com/android/work/overview#deployment_scenarios)for more information.

## About DPCs

In an Android enterprise deployment, an enterprise maintains control over various aspects of user devices, such as isolating work-related information from users' personal data, pre-configuring approved apps for the environment, or disabling device capabilities (for example, the camera).

As an EMM, you develop a DPC app that can be used by your customers in conjunction with your[EMM console](https://developers.google.com/android/work/overview#emm_console)and server. Your customer deploys the DPC to the user devices that they manage. The DPC acts as the bridge between your EMM console (and server) and the device. An admin uses the EMM console to perform a range of tasks, including configuring device settings and apps.

The DPC creates and manages the*work profile*on the device on which it is installed. The work profile encrypts work-related information and keeps it separate from users' personal apps and data. Before creating the work profile, the DPC can also provision a managed Google Play Account for use on the device.

This guide shows you how to develop a DPC that can create and manage work profiles.

## DPC Support Library for EMMs

The DPC Support Library for EMMs comprises utility and helper classes that facilitate provisioning and management of Android devices in an enterprise environment. The library lets you take advantage of important features in your DPC apps:

- **Managed Google Play Accounts provisioning support** : Provisioning[managed Google Play Accounts](https://developers.google.com/android/work/overview#managed_google_play_accounts)from the DPC app requires that Google Play and Google Play services apps meet minimum version requirements. However, updating these apps can be complex. The DPC support library takes care of updating these apps, and also ensures compatibility with future updates to the managed Google Play Accounts provisioning process. See[managed Google Play Accounts provisioning support](https://developer.android.com/work/dpc/build-dpc#managed_google_play_account_support)for details.
- **Managed Configurations support** : Using Play EMM API to handle managed configurations for approved apps is the easiest way to implement managed configurations on your DPC. The DPC Support Library lets you delegate to Google Play the task of applying managed configurations (formerly, app restrictions) as set by the admin using your EMM console. Using the Play EMM API to handle managed configurations allows the app configuration to be applied atomically during the installation. See[Apply managed configurations to work apps](https://developer.android.com/work/dpc/build-dpc#apply_managed_configurations_to_work_apps)for more information about how to enable this capability in your DPC.

Follow the steps below to download the library. The tasks detailed in this guide assume the use of the DPC Support Library.

### Download the DPC Support Library

To use the DPC Support Library, download the library from the[Android Enterprise EMM Provider community](https://emm.androidenterprise.dev/s/). You must add the library to your build.gradle file and take care of other dependencies when you build your DPC app. For example, the library requires 11.4.0[Google Play Services auth client library](https://developers.google.com/android/guides/setup#add_google_play_services_to_your_project).

1. Add the library to the`build.gradle`file:  

   ### Groovy

   ```groovy
   implementation(name:'dpcsupport-yyyymmdd', ext:'aar')
   ```

   ### Kotlin

   ```kotlin
   implementation(name = "dpcsupport-yyyymmdd", ext = "aar")
   ```
2. Add 11.4.0[Google Play Services auth client library](https://developers.google.com/android/guides/setup#add_google_play_services_to_your_project)to the build.gradle file:  

   ### Groovy

   ```groovy
   implementation 'com.google.android.gms:play-services-auth:11.4.0'
   ```

   ### Kotlin

   ```kotlin
   implementation("com.google.android.gms:play-services-auth:11.4.0")
   ```

| **Note:**Updating Google Play and Google Play services might require downloading 60 MB or more of data. Because the download uses the data connection that's available, you should advise your customers that updating Google Play and Google Play services could be time-consuming.

The library requires certain permissions to run, so you must add these to your DPC app's manifest when you upload to Google Play:  

```xml
  <uses-permission android:name=
      "android.permission.DOWNLOAD_WITHOUT_NOTIFICATION"/>
  <uses-permission android:name=
      "android.permission.GET_ACCOUNTS"/>
  <uses-permission android:name=
      "android.permission.MANAGE_ACCOUNTS"/>
  <uses-permission android:name=
      "android.permission.WRITE_SYNC_SETTINGS"/>
  <uses-permission android:name=
      "com.google.android.providers.gsf.permission.READ_GSERVICES"/>
```

<br />

In addition to these preliminary setup and deployment steps, you must also initialize the specific library functionality in your DPC code, depending on the capability you want to implement. The details are included in the relevant sections below.

## Create a DPC

Build your DPC on the existing model used for device administration applications. Specifically, your app must subclass`
`[DeviceAdminReceiver](https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver)(a class from the`android.app.admin`package) as described in[Device Administration](https://developer.android.com/work/device-admin).

### Create a work profile

For a sample that demonstrates how to create a basic work profile, see[BasicManagedProfile](https://github.com/googlearchive/android-BasicManagedProfile)on GitHub.

To create a work profile on a device that already has a personal profile, first find out if the device can support a work profile, by checking for the existence of the[`FEATURE_MANAGED_USERS`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_MANAGED_USERS)system feature:  

### Kotlin

```kotlin
if (!packageManager.hasSystemFeature(PackageManager.FEATURE_MANAGED_USERS)) {
    // This device does not support work profiles!
}
```

### Java

```java
PackageManager pm = getPackageManager();
if (!pm.hasSystemFeature(PackageManager.FEATURE_MANAGED_USERS)) {
    // This device does not support work profiles!
}
```

If the device supports work profiles, create a work profile by sending an intent with an[ACTION_PROVISION_MANAGED_PROFILE](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#ACTION_PROVISION_MANAGED_PROFILE)action. (In some documentation,*managed profile* is a general term that means the same thing as*work profile*in the context of Android in the enterprise.) Include the device admin package name as an extra:  

### Kotlin

```kotlin
val provisioningActivity = getActivity()

// You'll need the package name for the DPC app.
val myDPCPackageName = "com.example.myDPCApp"

// Set up the provisioning intent
val adminComponent = ComponentName(provisioningActivity.applicationContext, MyAdminReceiver::class.java)
provisioningIntent.putExtra(EXTRA_PROVISIONING_DEVICE_ADMIN_COMPONENT_NAME, adminComponent.flattenToString())
if (provisioningIntent.resolveActivity(provisioningActivity.packageManager) == null) {
    // No handler for intent! Can't provision this device.
    // Show an error message and cancel.
} else {
    // REQUEST_PROVISION_MANAGED_PROFILE is defined
    // to be a suitable request code
    startActivityForResult(provisioningIntent,
            REQUEST_PROVISION_MANAGED_PROFILE)
    provisioningActivity.finish()
}
```

### Java

```java
Activity provisioningActivity = getActivity();
// You'll need the package name for the DPC app.
String myDPCPackageName = "com.example.myDPCApp";
// Set up the provisioning intent
Intent provisioningIntent =
        new Intent("android.app.action.PROVISION_MANAGED_PROFILE");
ComponentName adminComponent = new ComponentName(provisioningActivity.getApplicationContext(), MyAdminReceiver.class);
provisioningIntent.putExtra(EXTRA_PROVISIONING_DEVICE_ADMIN_COMPONENT_NAME, adminComponent.flattenToString());
if (provisioningIntent.resolveActivity(provisioningActivity.getPackageManager())
         == null) {
    // No handler for intent! Can't provision this device.
    // Show an error message and cancel.
} else {
    // REQUEST_PROVISION_MANAGED_PROFILE is defined
    // to be a suitable request code
    startActivityForResult(provisioningIntent,
            REQUEST_PROVISION_MANAGED_PROFILE);
    provisioningActivity.finish();
}
```

The system responds to this intent by doing the following:

- Verifies that the device is encrypted. If it isn't, the system prompts the user to encrypt the device before proceeding.
- Creates a work profile.
- Removes non-required applications from the work profile.
- Copies the DPC app into the work profile and sets the DPC itself as the profile owner.

Override[onActivityResult()](https://developer.android.com/reference/android/app/Activity#onActivityResult(int, int, android.content.Intent))to see if provisioning was successful:  

### Kotlin

```kotlin
override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent) {
    // Check if this is the result of the provisioning activity
    if (requestCode == REQUEST_PROVISION_MANAGED_PROFILE) {
        // If provisioning was successful, the result code is
        // Activity.RESULT_OK
        if (resultCode == Activity.RESULT_OK) {
            // Work profile created and provisioned.
        } else {
            // Provisioning failed.
        }
        return
    } else {
        // This is the result of some other activity. Call the superclass.
        super.onActivityResult(requestCode, resultCode, data)
    }
}
```

### Java

```java
@Override
public void onActivityResult(int requestCode, int resultCode, Intent data) {
    // Check if this is the result of the provisioning activity
    if (requestCode == REQUEST_PROVISION_MANAGED_PROFILE) {
        // If provisioning was successful, the result code is
        // Activity.RESULT_OK
        if (resultCode == Activity.RESULT_OK) {
            // Work profile created and provisioned.
        } else {
            // Provisioning failed.
        }
        return;
    } else {
        // This is the result of some other activity. Call the superclass.
        super.onActivityResult(requestCode, resultCode, data);
    }
}
```

#### Finish enabling the work profile

When the profile has been provisioned, the system calls the DPC app's[DeviceAdminReceiver.onProfileProvisioningComplete()](https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver#onProfileProvisioningComplete(android.content.Context, android.content.Intent))method. Override this callback method to finish enabling the work profile.

A typical`DeviceAdminReceiver.onProfileProvisioningComplete()`callback implementation does the following:

- Verifies that the device is complying with the EMM's device policies, as described in[Set up device policies](https://developer.android.com/work/dpc/build-dpc#set_up_policies).
- Enables the system applications that the admin has made available within the work profile using[DevicePolicyManager.enableSystemApp()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#enableSystemApp(android.content.ComponentName, android.content.Intent)).
- If the device uses managed Google Play, adds the appropriate account to the work profile so that approved apps can be installed on the device.  
  - **Managed Google Play Accounts** : See[Ensure the working environment for managed Google Play Accounts](https://developer.android.com/work/dpc/build-dpc#ensure_the_working_environment)and[Add a managed Google Play Account](https://developer.android.com/work/dpc/build-dpc#add_a_managed_google_play_account)for details.
  - **Google Accounts** : Use[AccountManager.addAccount()](https://developer.android.com/reference/android/accounts/AccountManager#addAccount(java.lang.String, java.lang.String, java.lang.String[], android.os.Bundle, android.app.Activity, android.accounts.AccountManagerCallback<android.os.Bundle>, android.os.Handler)).

### Activate the work profile

Once you have completed these tasks, call the device policy manager's[setProfileEnabled()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setProfileEnabled(android.content.ComponentName))method to activate the work profile:  

### Kotlin

```kotlin
// Get the device policy manager
val myDevicePolicyMgr = getSystemService(Context.DEVICE_POLICY_SERVICE) as DevicePolicyManager
val componentName = myDeviceAdminReceiver.getComponentName(this)
// Set the name for the newly created work profile.
myDevicePolicyMgr.setProfileName(componentName, "My New Work Profile")
// ...and enable the profile
myDevicePolicyMgr.setProfileEnabled(componentName)
```

### Java

```java
// Get the device policy manager
DevicePolicyManager myDevicePolicyMgr =
        (DevicePolicyManager) getSystemService(Context.DEVICE_POLICY_SERVICE);
ComponentName componentName = myDeviceAdminReceiver.getComponentName(this);
// Set the name for the newly created work profile.
myDevicePolicyMgr.setProfileName(componentName, "My New Work Profile");
// ...and enable the profile
myDevicePolicyMgr.setProfileEnabled(componentName);
```

### Set up device policies

The DPC app applies the device policies as set by an admin to meet an organization's requirements and constraints. For example, security policy might require that devices lock after a certain number of failed password attempts. The DPC queries the EMM console for current policies then applies the policies using the[Device Administration](https://developer.android.com/work/device-admin)API.

For information on how to apply device policies, see[Policies](https://developer.android.com/work/device-admin#policies).

### Apply managed configurations to work apps

Managed configurations let you provide your customers with the ability to pre-configure the apps that they've approved for deployment, and update those apps easily when the configuration needs to change. Configuring an app prior to deployment ensures that the organization's security and other policies are met upon installation of the app on the target device.

The app capabilities are defined by the app developer in an XML schema (the managed configurations schema) that accompanies the app upon upload to Google Play (app developers, see[Set Up Managed Configurations](https://developer.android.com/work/managed-configurations)for details).

You retrieve this schema from the app to display for your customer admins in your EMM console, provide a UI in which the various options defined in the schema display, and enable admins to pre-configure the app's settings. The resulting managed configuration set by the admin is typically stored on the EMM server which then uses the Play EMM API to set[Managedconfigurationsfordevice](https://developers.google.com/android/work/play/emm-api/v1/managedconfigurationsfordevice)or[Managedconfigurationsforuser](https://developers.google.com/android/work/play/emm-api/v1/managedconfigurationsforuser). See[Managed Configurations through Play](https://developers.google.com/android/work/play/emm-api/managed-configurations)for details.

Managed configurations can be applied to the app by using the Play EMM API (recommended approach) or directly from the DPC (described in[Apply managed configurations directly from the DPC](https://developer.android.com/work/dpc/build-dpc#apply_managed_configurations_from_dpc)). Using the Play EMM API has several advantages, including easy implementation because you can use the[DPC Support Library](https://developer.android.com/work/dpc/build-dpc#dpc_support_library)to simplify DPC tasks. In addition, the Play EMM API:

- Sets the configuration atomically when a new app is installed, thus ensuring the app is ready the first time the user launches the app.
- Lets you manage configurations on a per-user basis, so you can avoid monitoring provisioning on a per-device basis.

#### Apply managed configurations using the Play EMM API

To use the Play EMM API for managed configurations, the DPC must allow the Google Play to set configurations. The DPC Support Library takes care of this task for you by proxying the configuration sent by Google Play.

To use the Play EMM API, download the[DPC Support Library](https://developer.android.com/work/dpc/build-dpc#dpc_support_library)and then enable managed configurations support in your DPC.

##### Enable Managed Configurations support in your DPC

Import this class in your DPC:  

```
com.google.android.apps.work.dpcsupport.ManagedConfigurationsSupport
```

Initialize the managed configurations library. In this example, "admin" is the ComponentName of the[DeviceAdminReceiver](https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver).  

### Kotlin

```kotlin
var managedConfigurationsSupport = ManagedConfigurationsSupport(context, admin)
```

### Java

```java
ManagedConfigurationsSupport managedConfigurationsSupport =
    new ManagedConfigurationsSupport(context, admin);
```

Enable managed configurations:  

### Kotlin

```kotlin
managedConfigurationsSupport.enableManagedConfigurations()
```

### Java

```java
managedConfigurationsSupport.enableManagedConfigurations();
```

With this library initialized in your DPC, you can use the[Google Play EMM API](https://developers.google.com/android/work/play/emm-api/v1)in your EMM console and server to apply managed configurations to approved apps, instead of coding these tasks directly in the DPC. See[Managed Configurations through Play](https://developers.google.com/android/work/play/emm-api/managed-configurations)for details.

#### Apply managed configurations directly from the DPC

To change an app's configuration settings directly from the DPC, call the[DevicePolicyManager.setApplicationRestrictions()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setApplicationRestrictions(android.content.ComponentName, java.lang.String, android.os.Bundle))method and pass parameters for the DPC app's[DeviceAdminReceiver](https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver), the package name of the target app, and the[Bundle](https://developer.android.com/reference/android/os/Bundle)comprising the app's managed configuration as set by the admin. See[How your DPC and EMM console interact](https://developers.google.com/android/work/overview#how_your_dpc_and_emm_console_interact)and[Set up Managed Configurations](https://developer.android.com/work/managed-configurations)for details. However, note that this alternative approach to applying managed configurations is not recommended in managed Google Play Accounts deployments.

### Managed Google Play Account provisioning support

The[DPC Support Library](https://developer.android.com/work/dpc/build-dpc#dpc_support_library)includes support for provisioning managed Google Play Accounts. To use this support, you must first initialize the library, and then you can[Ensure the working environment](https://developer.android.com/work/dpc/build-dpc#ensure_the_working_environment)and[Add a managed Google Play Account](https://developer.android.com/work/dpc/build-dpc#add_a_managed_google_play_account).

#### Initialize managed Google Play Accounts support in your DPC

Import this class in your DPC:  

```
com.google.android.apps.work.dpcsupport.AndroidForWorkAccountSupport
```

Initialize the provisioning compatibility library. In this example, "admin" is the`ComponentName`of the`
`[DeviceAdminReceiver](https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver).  

### Kotlin

```kotlin
var androidForWorkAccountSupport = AndroidForWorkAccountSupport(context, admin)
```

### Java

```java
AndroidForWorkAccountSupport androidForWorkAccountSupport =
    new AndroidForWorkAccountSupport(context, admin);
```

#### Ensure the working environment for managed Google Play Accounts

After the DPC provisions a device in profile owner mode ([ACTION_PROVISION_MANAGED_PROFILE](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#ACTION_PROVISION_MANAGED_PROFILE)) or device owner mode ([ACTION_PROVISION_MANAGED_DEVICE](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#ACTION_PROVISION_MANAGED_DEVICE)), make sure that the device can support managed Google Play Accounts by calling:  

### Kotlin

```kotlin
androidForWorkAccountSupport.ensureWorkingEnvironment(callback)
```

### Java

```java
androidForWorkAccountSupport.ensureWorkingEnvironment(callback);
```
| **Important:** The DPC should call`ensureWorkingEnvironment`as early as possible during provisioning and before the user has set a passcode.

The callback reports the success or failure of this process. When the callback returns successfully, a managed Google Play Account can be added. If the callback reports an error, prompt the user to make sure the device has a network connection (for example, if the download fails). In other cases, report the failure to Google.  

### Kotlin

```kotlin
object : WorkingEnvironmentCallback() {
    override fun onSuccess() {
        // Can now provision the managed Google Play Account
    }
    override fun onFailure(error: Error) {
        // Notify user, handle error (check network connection)
    }
}
```

### Java

```java
new WorkingEnvironmentCallback() {
    @Override
    public void onSuccess() {
        // Can now provision the managed Google Play Account
    }

    @Override
    public void onFailure(Error error) {
        // Notify user, handle error (check network connection)
    }
}
```

#### Add a managed Google Play Account

The Android framework's[AccountManager](https://developer.android.com/reference/android/accounts/AccountManager)can add a managed Google Play Account to a device. To simplify interaction with`AccountManager`, use the helper function (shown in the example below) from the[DPC Support Library](https://developer.android.com/work/dpc/build-dpc#dpc_support_library). The function handles the token returned by Google Play server and facilitates provisioning the managed Google Play Account. The function returns when the managed Google Play Account is in a valid state:  

### Kotlin

```kotlin
androidForWorkAccountSupport.addAndroidForWorkAccount(token, accountAddedCallback)
```

### Java

```java
androidForWorkAccountSupport.addAndroidForWorkAccount(token, accountAddedCallback);
```

- `token`---The user authentication token generated by the Google Play EMM API`
  `[Users.generateAuthenticationToken()](https://developers.google.com/android/work/play/emm-api/v1/users/generateAuthenticationToken)call.
- `accountAddedCallback`---Returns the managed Google Play Account that was successfully added to the device. This callback should include`onAccountReady()`and`onFailure()`methods.

### Kotlin

```kotlin
val workAccountAddedCallback = object : WorkAccountAddedCallback() {
    override fun onAccountReady(account: Account, deviceHint: String) {
        // Device account was successfully added to the device
        // and is ready to be used.
    }

    override fun onFailure(error: Error) {
        // The account was not successfully added. Check that the token
        // provided was valid (it expires after a certain period of time).
    }
}
```

### Java

```java
WorkAccountAddedCallback workAccountAddedCallback =
    new WorkAccountAddedCallback() {
        @Override
        public void onAccountReady(Account account, String deviceHint) {
            // Device account was successfully added to the device
            // and is ready to be used.
        }

        @Override
        public void onFailure(Error error) {
            // The account was not successfully added. Check that the token
            // provided was valid (it expires after a certain period of time).
        }
};
```

## Related documentation

- To learn more about the Device Administration API, see[Device Administration](https://developer.android.com/work/device-admin).
- To learn about Android Enterprise provisioning methods, see[Provision devices](https://developers.google.com/android/work/play/emm-api/prov-devices)in the Android Enterprise developer's guide.
- For a GitHub sample that demonstrates how to create a basic work profile, see[BasicManagedProfile](https://github.com/googlearchive/android-BasicManagedProfile).
- For a GitHub sample that demonstrates how to set configurations on other apps as a profile owner, see[AppRestrictionEnforcer](https://github.com/googlearchive/android-AppRestrictionEnforcer).