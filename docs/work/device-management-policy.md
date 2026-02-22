---
title: https://developer.android.com/work/device-management-policy
url: https://developer.android.com/work/device-management-policy
source: md.txt
---

**Device admin deprecation** . Some admin policies have been marked as deprecated when invoked
by a device admin. To learn more and see the migration options, see
[Device admin deprecation](https://developers.google.com/android/work/device-admin-deprecation).

Since Android 2.2 (API level 8), the Android platform offers system-level device management
capabilities through the Device Administration APIs.

In this lesson, you will learn how to create a security-aware application that manages access to
its content by enforcing device management policies. Specifically, the application can be configured
such that it ensures a screen-lock password of sufficient strength is set up before displaying
restricted content to the user.

## Define and declare your policy

First, you need to define the kinds of policy to support at the functional level. Policies may
cover screen-lock password strength, expiration timeout, encryption, etc.

You must declare the selected policy set, which will be enforced by the application, in the
`res/xml/device_admin.xml` file. The Android manifest should also reference the
declared policy set.

Each declared policy corresponds to some number of related device policy methods in `https://developer.android.com/reference/android/app/admin/DevicePolicyManager` (defining minimum password length and minimum number of
uppercase characters are two examples). If an application attempts to invoke methods whose
corresponding policy is not declared in the XML, this will result in a `https://developer.android.com/reference/java/lang/SecurityException` at runtime. Other permissions,
such as `force-lock`, are available if the application intends to manage
other kinds of policy. As you'll see later, as part of the device administrator activation process,
the list of declared policies will be presented to the user on a system screen.

The following snippet declares the limit password policy in `res/xml/device_admin.xml`:

```xml
<device-admin xmlns:android="http://schemas.android.com/apk/res/android">
    <uses-policies>
        <limit-password />
    </uses-policies>
</device-admin>
```

Policy declaration XML referenced in Android manifest:

```xml
<receiver android:name=".Policy$PolicyAdmin"
    android:permission="android.permission.BIND_DEVICE_ADMIN">
    <meta-data android:name="android.app.device_admin"
        android:resource="@xml/device_admin" />
    <intent-filter>
        <action android:name="android.app.action.DEVICE_ADMIN_ENABLED" />
    </intent-filter>
</receiver>
```

## Create a device administration receiver

Create a Device Administration broadcast receiver, which gets notified of events related to the policies you've declared to support. An application can selectively override callback methods.

In the sample application, Device Admin, when the device administrator is deactivated by the
user, the configured policy is erased from the shared preference. You should consider implementing
business logic that is relevant to your use case. For example, the application might take some
actions to mitigate security risk by implementing some combination of deleting sensitive data on the
device, disabling remote synchronization, alerting an administrator, etc.

For the broadcast receiver to work, be sure to register it in the Android manifest as illustrated in the above snippet.

### Kotlin

```kotlin
class PolicyAdmin : DeviceAdminReceiver() {

    override fun onDisabled(context: Context, intent: Intent) {
        // Called when the app is about to be deactivated as a device administrator.
        // Deletes previously stored password policy.
        super.onDisabled(context, intent)
        context.getSharedPreferences(APP_PREF, Activity.MODE_PRIVATE).edit().apply {
            clear()
            apply()
        }
    }
}
```

### Java

```java
public static class PolicyAdmin extends DeviceAdminReceiver {

    @Override
    public void onDisabled(Context context, Intent intent) {
        // Called when the app is about to be deactivated as a device administrator.
        // Deletes previously stored password policy.
        super.onDisabled(context, intent);
        SharedPreferences prefs = context.getSharedPreferences(APP_PREF, Activity.MODE_PRIVATE);
        prefs.edit().clear().commit();
    }
}
```

## Activate the device administrator

Before enforcing any policies, the user needs to manually activate the application as a device
administrator. The snippet below illustrates how to trigger the settings activity in which the
user can activate your application. It is good practice to include the explanatory text to highlight
to users why the application is requesting to be a device administrator, by specifying the
`https://developer.android.com/reference/android/app/admin/DevicePolicyManager#EXTRA_ADD_EXPLANATION` extra in the intent.
![](https://developer.android.com/static/images/training/device-mgmt-activate-device-admin.png)

**Figure 1.** The user activation screen in which you can
provide a description of your device policies.

### Kotlin

```kotlin
if (!policy.isAdminActive()) {

    val activateDeviceAdminIntent = Intent(DevicePolicyManager.ACTION_ADD_DEVICE_ADMIN)

    activateDeviceAdminIntent.putExtra(
            DevicePolicyManager.EXTRA_DEVICE_ADMIN,
            policy.getPolicyAdmin()
    )

    // It is good practice to include the optional explanation text to
    // explain to user why the application is requesting to be a device
    // administrator. The system will display this message on the activation
    // screen.
    activateDeviceAdminIntent.putExtra(
            DevicePolicyManager.EXTRA_ADD_EXPLANATION,
            resources.getString(R.string.device_admin_activation_message)
    )

    startActivityForResult(activateDeviceAdminIntent, REQ_ACTIVATE_DEVICE_ADMIN)
}
```

### Java

```java
if (!policy.isAdminActive()) {

    Intent activateDeviceAdminIntent =
        new Intent(DevicePolicyManager.ACTION_ADD_DEVICE_ADMIN);

    activateDeviceAdminIntent.putExtra(
        DevicePolicyManager.EXTRA_DEVICE_ADMIN,
        policy.getPolicyAdmin());

    // It is good practice to include the optional explanation text to
    // explain to user why the application is requesting to be a device
    // administrator. The system will display this message on the activation
    // screen.
    activateDeviceAdminIntent.putExtra(
        DevicePolicyManager.EXTRA_ADD_EXPLANATION,
        getResources().getString(R.string.device_admin_activation_message));

    startActivityForResult(activateDeviceAdminIntent,
        REQ_ACTIVATE_DEVICE_ADMIN);
}
```

If the user chooses "Activate," the application becomes a device administrator and can begin
configuring and enforcing the policy.

The application also needs to be prepared to handle set back situations where the user abandons
the activation process by hitting the Cancel button, the Back key, or the Home key. Therefore,
`https://developer.android.com/reference/android/app/Activity#onResume()` in the Policy Set Up Activity needs to have logic
to reevaluate the condition and present the Device Administrator Activation option to the user if
needed.

## Implement the device policy controller

After the device administrator is activated successfully, the application then configures Device
Policy Manager with the requested policy. Keep in mind that new policies are being added to
Android with each release. It is appropriate to perform version checks in your application if using
new policies while supporting older versions of the platform. For example, the Password Minimum
Upper Case policy is only available with API level 11 (Honeycomb) and above. The following code
demonstrates how you can check the version at runtime.

### Kotlin

```kotlin
private lateinit var dpm: DevicePolicyManager
private lateinit var policyAdmin: ComponentName

dpm = context.getSystemService(Context.DEVICE_POLICY_SERVICE) as DevicePolicyManager
policyAdmin = ComponentName(context, PolicyAdmin::class.java)

dpm.apply {
    setPasswordQuality(policyAdmin, PASSWORD_QUALITY_VALUES[passwordQuality])
    setPasswordMinimumLength(policyAdmin, passwordLength)
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.HONEYCOMB) {
        setPasswordMinimumUpperCase(policyAdmin, passwordMinUpperCase)
    }
}
```

### Java

```java
DevicePolicyManager dpm = (DevicePolicyManager)
        context.getSystemService(Context.DEVICE_POLICY_SERVICE);
ComponentName policyAdmin = new ComponentName(context, PolicyAdmin.class);

dpm.setPasswordQuality(policyAdmin, PASSWORD_QUALITY_VALUES[passwordQuality]);
dpm.setPasswordMinimumLength(policyAdmin, passwordLength);
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.HONEYCOMB) {
    dpm.setPasswordMinimumUpperCase(policyAdmin, passwordMinUpperCase);
}
```

At this point, the application is able to enforce the policy. While the application has no access
to the actual screen-lock password used, through the Device Policy Manager API it can determine
whether the existing password satisfies the required policy. If it turns out that the existing
screen-lock password is not sufficient, the device administration API does not automatically take
corrective action. It is the application's responsibility to explicitly launch the system
password-change screen in the Settings app. For example:

### Kotlin

```kotlin
if (!dpm.isActivePasswordSufficient) {
    // Triggers password change screen in Settings.
    Intent(DevicePolicyManager.ACTION_SET_NEW_PASSWORD).also { intent ->
        startActivity(intent)
    }
}
```

### Java

```java
if (!dpm.isActivePasswordSufficient()) {
    ...
    // Triggers password change screen in Settings.
    Intent intent =
        new Intent(DevicePolicyManager.ACTION_SET_NEW_PASSWORD);
    startActivity(intent);
}
```

Normally, the user can select from one of the available lock mechanisms, such as None, Pattern,
PIN (numeric), or Password (alphanumeric). When a password policy is configured, those password
types that are weaker than those defined in the policy are disabled. For example, if the
"Numeric" password quality is configured, the user can select either PIN (numeric) or Password
(alphanumeric) password only.

Once the device is properly secured by setting up a proper screen-lock password, the application
allows access to the secured content.

### Kotlin

```kotlin
when {
    !dpm.isAdminActive(policyAdmin) -> {
        // Activates device administrator.
        ...
    }
    !dpm.isActivePasswordSufficient -> {
        // Launches password set-up screen in Settings.
        ...
    }
    else -> {
        // Grants access to secure content.
        ...
        startActivity(Intent(context, SecureActivity::class.java))
    }
}
```

### Java

```java
if (!dpm.isAdminActive(..)) {
    // Activates device administrator.
    ...
} else if (!dpm.isActivePasswordSufficient()) {
    // Launches password set-up screen in Settings.
    ...
} else {
    // Grants access to secure content.
    ...
    startActivity(new Intent(context, SecureActivity.class));
}
```