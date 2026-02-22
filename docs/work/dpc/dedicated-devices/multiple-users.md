---
title: https://developer.android.com/work/dpc/dedicated-devices/multiple-users
url: https://developer.android.com/work/dpc/dedicated-devices/multiple-users
source: md.txt
---

This developer's guide explains how your device policy controller (DPC) can
manage multiple Android users on [dedicated devices](https://developer.android.com/work/dpc/dedicated-devices).

## Overview

Your DPC can help multiple people share a single dedicated device. Your DPC
running on a fully managed device can create and manage two types of users:

- **Secondary users** are Android users with separate apps and data saved between sessions. You manage the user with an admin component. These users are useful for cases where a device is picked up at the start of a shift, such as delivery drivers or security workers.
- **Ephemeral users** are secondary users that the system deletes when the user stops, switches away, or the device reboots. These users are useful for cases where data can be deleted after the session finishes, such as public-access internet kiosks.

> [!NOTE]
> **Note:** Because secondary users and ephemeral users are almost identical, for the rest of this guide we'll just refer to secondary users when talking about both.

You use your existing DPC to manage the dedicated device and the secondary
users. An admin component in your DPC sets itself as the admin for new secondary
users when you create them.
![Primary user and two secondary users.](https://developer.android.com/static/images/work/dpc/dedicated-devices/secondary-users.svg) **Figure 1.** Primary and secondary users managed by admins from the same DPC

Admins of a secondary user must belong to the same package as the admin of the
fully managed device. To simplify development, we recommend sharing an admin
between the device and secondary users.

Managing multiple users on dedicated devices typically requires Android 9.0,
however some of the methods used in this developer's guide are available in
earlier versions of Android.

> [!NOTE]
> **Note:** [Multi-user](https://source.android.com/compatibility/12/android-12-cdd#95_multi-user_support) is an optional feature and may not be supported on all Android devices. Even when supported, manufacturers may limit the maximum number of users allowed on a device. Exceeding the user limits may result in [`USER_OPERATION_ERROR_MAX_USERS`](https://developer.android.com/reference/android/os/UserManager#USER_OPERATION_ERROR_MAX_USERS) or [`USER_OPERATION_ERROR_MAX_RUNNING_USERS`](https://developer.android.com/reference/android/os/UserManager#USER_OPERATION_ERROR_MAX_RUNNING_USERS) errors when attempting to create new users.

### Secondary users

Secondary users can connect to Wifi and can configure new networks. However, they
can't edit or delete networks, not even the networks they created.

## Create users

Your DPC can create additional users in the background and then can switch them
to the foreground. The process is almost the same for both secondary and
ephemeral users. Implement the following steps in the admins of the fully
managed device and secondary user:

1. Call [`DevicePolicyManager.createAndManageUser()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#createAndManageUser(android.content.ComponentName,%20java.lang.String,%20android.content.ComponentName,%20android.os.PersistableBundle,%20int)). To create an ephemeral user, include [`MAKE_USER_EPHEMERAL`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#MAKE_USER_EPHEMERAL) in the flags argument.
2. Call [`DevicePolicyManager.startUserInBackground()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#startUserInBackground(android.content.ComponentName,%20android.os.UserHandle)) to start the user in the background. The user starts running but you will want to finish setup before bringing the user to the foreground and showing it to the person using the device.
3. In the admin of the secondary user, call [`DevicePolicyManager.setAffiliationIds()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setAffiliationIds(android.content.ComponentName,%20java.util.Set%3Cjava.lang.String%3E)) to affiliate the new user with the primary user. See [DPC coordination](https://developer.android.com/work/dpc/dedicated-devices/multiple-users#dpc-coord) below.
4. Back in the admin of the fully managed device, call [`DevicePolicyManager.switchUser()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#switchUser(android.content.ComponentName,%20android.os.UserHandle)) to switch the user to the foreground.

The following sample shows how you can add step 1 to your DPC:

### Kotlin

```kotlin
val dpm = getContext().getSystemService(Context.DEVICE_POLICY_SERVICE)
        as DevicePolicyManager

// If possible, reuse an existing affiliation ID across the
// primary user and (later) the ephemeral user.
val identifiers = dpm.getAffiliationIds(adminName)
if (identifiers.isEmpty()) {
    identifiers.add(UUID.randomUUID().toString())
    dpm.setAffiliationIds(adminName, identifiers)
}

// Pass an affiliation ID to the ephemeral user in the admin extras.
val adminExtras = PersistableBundle()
adminExtras.putString(AFFILIATION_ID_KEY, identifiers.first())
// Include any other config for the new user here ...

// Create the ephemeral user, using this component as the admin.
try {
    val ephemeralUser = dpm.createAndManageUser(
            adminName,
            "tmp_user",
            adminName,
            adminExtras,
            DevicePolicyManager.MAKE_USER_EPHEMERAL or
                    DevicePolicyManager.SKIP_SETUP_WIZARD)

} catch (e: UserManager.UserOperationException) {
    if (e.userOperationResult ==
            UserManager.USER_OPERATION_ERROR_MAX_USERS) {
        // Find a way to free up users...
    }
}
```

### Java

```java
DevicePolicyManager dpm = (DevicePolicyManager)
    getContext().getSystemService(Context.DEVICE_POLICY_SERVICE);

// If possible, reuse an existing affiliation ID across the
// primary user and (later) the ephemeral user.
Set<String> identifiers = dpm.getAffiliationIds(adminName);
if (identifiers.isEmpty()) {
  identifiers.add(UUID.randomUUID().toString());
  dpm.setAffiliationIds(adminName, identifiers);
}

// Pass an affiliation ID to the ephemeral user in the admin extras.
PersistableBundle adminExtras = new PersistableBundle();
adminExtras.putString(AFFILIATION_ID_KEY, identifiers.iterator().next());
// Include any other config for the new user here ...

// Create the ephemeral user, using this component as the admin.
try {
  UserHandle ephemeralUser = dpm.createAndManageUser(
      adminName,
      "tmp_user",
      adminName,
      adminExtras,
      DevicePolicyManager.MAKE_USER_EPHEMERAL |
          DevicePolicyManager.SKIP_SETUP_WIZARD);

} catch (UserManager.UserOperationException e) {
  if (e.getUserOperationResult() ==
      UserManager.USER_OPERATION_ERROR_MAX_USERS) {
    // Find a way to free up users...
  }
}
```

When you create or start a new user, you can check the reason for any failures
by catching the [`UserOperationException`](https://developer.android.com/reference/android/os/UserManager.UserOperationException) exception and calling
[`getUserOperationResult()`](https://developer.android.com/reference/android/os/UserManager.UserOperationException#getUserOperationResult()). Exceeding the user
limits are common failure reasons:

- [`USER_OPERATION_ERROR_MAX_USERS`](https://developer.android.com/reference/android/os/UserManager#USER_OPERATION_ERROR_MAX_USERS)
- [`USER_OPERATION_ERROR_MAX_RUNNING_USERS`](https://developer.android.com/reference/android/os/UserManager#USER_OPERATION_ERROR_MAX_RUNNING_USERS)

> [!NOTE]
> **Note:** Because each user consumes a device's resources, manufacturers limit the number of users you can add and run on a device. You can't check the maximum users allowed on a device, but you can catch the exceptions after you try to create or start a new user.

Creating a user can take some time. If you're frequently creating users, you can
improve the user experience by preparing a ready-to-go user in the background.
You might need to balance the advantages of a ready-to-go user with the maximum
number of users allowed on a device.

### Identification

After creating a new user, you should refer to the user with a persistent serial
number. Don't persist the `UserHandle` because the system recycles these as you
create and delete users. Get the serial number by calling
[`UserManager.getSerialNumberForUser()`](https://developer.android.com/reference/android/os/UserManager#getSerialNumberForUser(android.os.UserHandle)):

### Kotlin

```kotlin
// After calling createAndManageUser() use a device-unique serial number
// (that isn't recycled) to identify the new user.
secondaryUser?.let {
    val userManager = getContext().getSystemService(UserManager::class.java)
    val ephemeralUserId = userManager!!.getSerialNumberForUser(it)
    // Save the serial number to storage  ...
}
```

### Java

```java
// After calling createAndManageUser() use a device-unique serial number
// (that isn't recycled) to identify the new user.
if (secondaryUser != null) {
  UserManager userManager = getContext().getSystemService(UserManager.class);
  long ephemeralUserId = userManager.getSerialNumberForUser(secondaryUser);
  // Save the serial number to storage  ...
}
```

### User config

Depending on the needs of your users, you can customize the setup of secondary
users. You can include the following flags when calling `createAndManageUser()`:

[`SKIP_SETUP_WIZARD`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#SKIP_SETUP_WIZARD)
:   Skips running the new-user setup wizard that checks for and installs updates,
    prompts the user to add a Google Account along with Google services, and sets
    a screen lock. This can take some time and might not be applicable for all
    users---public internet kiosks, for example.

[`LEAVE_ALL_SYSTEM_APPS_ENABLED`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#SKIP_SETUP_WIZARD)
:   Leaves all the system apps enabled in the new user. If you don't set this flag,
    the new user contains just the minimal set of apps that the phone needs to
    operate---typically a file browser, telephone dialer, contacts, and SMS messages.

## Follow the user lifecycle

Your DPC (if it's an admin of the fully managed device) might find it useful to
know when secondary users change. To run follow-on tasks after changes, override
these callback methods in your DPC's [`DeviceAdminReceiver`](https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver) subclass:

[`onUserStarted()`](https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver#onUserStarted(android.content.Context,%20android.content.Intent,%20android.os.UserHandle))
:   Called after the system starts a user. This user might still be setting up or
    be running in the background. You can get the user from the `startedUser`
    argument.

[`onUserSwitched()`](https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver#onUserSwitched(android.content.Context,%20android.content.Intent,%20android.os.UserHandle))
:   Called after the system switches to a different user. You can get the new user
    that's now running in the foreground from the `switchedUser` argument.

[`onUserStopped()`](https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver#onUserStopped(android.content.Context,%20android.content.Intent,%20android.os.UserHandle))
:   Called after the system stops a user because they logged out, switched to a
    new user (if the user is ephemeral), or your DPC stopped the user. You can get
    the user from the `stoppedUser` argument.

[`onUserAdded()`](https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver#onUserAdded(android.content.Context,%20android.content.Intent,%20android.os.UserHandle))
:   Called when the system adds a new user. Typically, secondary users aren't
    fully set up when your DPC gets the callback. You can get the user from the
    `newUser` argument.

[`onUserRemoved()`](https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver#onUserRemoved(android.content.Context,%20android.content.Intent,%20android.os.UserHandle))
:   Called after the system deletes a user. Because the user is already deleted,
    you can't access the user represented by the `removedUser` argument.

To know when the system brings a user to the foreground or sends a user to the
background, apps can register a receiver for the
[`ACTION_USER_FOREGROUND`](https://developer.android.com/reference/android/content/Intent#ACTION_USER_FOREGROUND) and
[`ACTION_USER_BACKGROUND`](https://developer.android.com/reference/android/content/Intent#ACTION_USER_BACKGROUND) broadcasts.

## Discover users

To get all the secondary users, an admin of a fully managed device can call
[`DevicePolicyManager.getSecondaryUsers()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getSecondaryUsers(android.content.ComponentName)). The results
include any secondary or ephemeral users the admin created. The results also
include any secondary users (or a guest user) a person using the device might
have created. The results don't include work profiles because they aren't
secondary users. The following sample shows how you can use this method:

### Kotlin

```kotlin
// The device is stored for the night. Stop all running secondary users.
dpm.getSecondaryUsers(adminName).forEach {
    dpm.stopUser(adminName, it)
}
```

### Java

```java
// The device is stored for the night. Stop all running secondary users.
for (UserHandle user : dpm.getSecondaryUsers(adminName)) {
  dpm.stopUser(adminName, user);
}
```

Here are other methods you can call to find out the status of secondary users:

[`DevicePolicyManager.isEphemeralUser()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#isEphemeralUser(android.content.ComponentName))
:   Call this method from the admin of a secondary user to find out if this is an
    ephemeral user.

[`DevicePolicyManager.isAffiliatedUser()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#isAffiliatedUser())
:   Call this method from the admin of a secondary user to find out if this user is
    affiliated with the primary user. To learn more about affiliation, see [DPC
    coordination](https://developer.android.com/work/dpc/dedicated-devices/multiple-users#dpc-coord) below.

## User management

If you want to completely manage the user lifecycle, you can call APIs for
fine-grained control of when and how the device changes users. For example, you
can delete a user when a device hasn't been used for a period of time or you can
send any unsent orders to a server before a person's shift finishes.

### Logout

Android 9.0 added a log-out button to the lock screen so that a person using the
device can end their session. After tapping the button, the system stops the
secondary user, deletes the user if it's ephemeral, and the primary user returns
to the foreground. Android hides the button when the primary user is in the
foreground because the primary user can't log out.

Android doesn't show the end-session button by default but your admin (of a
fully managed device) can enable it by calling
[`DevicePolicyManager.setLogoutEnabled()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setLogoutEnabled(android.content.ComponentName,%20boolean)). If you need to
confirm the current state of the button, call
[`DevicePolicyManager.isLogoutEnabled()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#isLogoutEnabled()).

The admin of a secondary user can programmatically log out the user and return
to the primary user. First, confirm the secondary and the primary users are
affiliated, then call [`DevicePolicyManager.logoutUser()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#logoutUser(android.content.ComponentName)). If
the logged-out user is an ephemeral user, the system stops and then deletes the
user.

### Switch users

To switch to a different secondary user, the admin of a fully managed device can
call [`DevicePolicyManager.switchUser()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#switchUser(android.content.ComponentName,%20android.os.UserHandle)). As a convenience, you
can pass `null` to switch to the primary user.

### Stop a user

To stop a secondary user, a DPC that owns a fully managed device can call
[`DevicePolicyManager.stopUser()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#stopUser(android.content.ComponentName,%20android.os.UserHandle)). If the stopped user is an
ephemeral user, the user is stopped and then deleted.

We recommend stopping users whenever possible to help stay below the device's
maximum number of running users.

### Delete a user

To permanently delete a secondary user a DPC can call one of the following
`DevicePolicyManager` methods:

- An admin of a fully managed device can call [`removeUser()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#removeUser(android.content.ComponentName,%20android.os.UserHandle)).
- An admin of the secondary user can call [`wipeData()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#wipeData(int,%20java.lang.CharSequence)).

The system deletes ephemeral users when they're logged out, stopped, or switched
away from.

### Disable the default UI

If your DPC provides a UI to manage users, you can disable Android's built-in
multi-user interface. You can do this by calling
[`DevicePolicyManager.setLogoutEnabled()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setLogoutEnabled(android.content.ComponentName,%20boolean)) and adding the
[`DISALLOW_USER_SWITCH`](https://developer.android.com/reference/android/os/UserManager#DISALLOW_USER_SWITCH) restriction as shown in the
following example:

### Kotlin

```kotlin
// Explicitly disallow logging out using Android UI (disabled by default).
dpm.setLogoutEnabled(adminName, false)

// Disallow switching users in Android's UI. This DPC can still
// call switchUser() to manage users.
dpm.addUserRestriction(adminName, UserManager.DISALLOW_USER_SWITCH)
```

### Java

```java
// Explicitly disallow logging out using Android UI (disabled by default).
dpm.setLogoutEnabled(adminName, false);

// Disallow switching users in Android's UI. This DPC can still
// call switchUser() to manage users.
dpm.addUserRestriction(adminName, UserManager.DISALLOW_USER_SWITCH);
```

The person using the device can't add secondary users with Android's built-in UI
because admins of fully managed devices automatically add the
[`DISALLOW_ADD_USER`](https://developer.android.com/reference/android/os/UserManager#DISALLOW_ADD_USER) user restriction.

## Session messages

When the person using a device switches to a new user, Android shows a panel to
highlight the switch. Android shows the following messages:

- *Start-user-session message* shown when the device switches to a secondary user from the primary user.
- *End-user-session message* shown when the device returns to the primary user from a secondary user.

The system doesn't show the messages when switching between two secondary users.

Because the messages might not be suitable for all situations, you can change
the text of these messages. For example, if your solution uses ephemeral user
sessions, you can reflect this in the messages such as: *Stopping browser
session \& deleting personal data...*

The system shows the message for just a couple of seconds, so each message
should be a short, clear phrase. To customize the messages, your admin can call
the `DevicePolicyManager` methods
[`setStartUserSessionMessage()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setStartUserSessionMessage(android.content.ComponentName,%20java.lang.CharSequence)) and
[`setEndUserSessionMessage()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setEndUserSessionMessage(android.content.ComponentName,%20java.lang.CharSequence)) as shown in the
following example:

### Kotlin

```kotlin
// Short, easy-to-read messages shown at the start and end of a session.
// In your app, store these strings in a localizable resource.
internal val START_USER_SESSION_MESSAGE = "Starting guest session..."
internal val END_USER_SESSION_MESSAGE = "Stopping & clearing data..."

// ...
dpm.setStartUserSessionMessage(adminName, START_USER_SESSION_MESSAGE)
dpm.setEndUserSessionMessage(adminName, END_USER_SESSION_MESSAGE)
```

### Java

```java
// Short, easy-to-read messages shown at the start and end of a session.
// In your app, store these strings in a localizable resource.
private static final String START_USER_SESSION_MESSAGE = "Starting guest session...";
private static final String END_USER_SESSION_MESSAGE = "Stopping & clearing data...";

// ...
dpm.setStartUserSessionMessage(adminName, START_USER_SESSION_MESSAGE);
dpm.setEndUserSessionMessage(adminName, END_USER_SESSION_MESSAGE);
```

Pass `null` to delete your custom messages and return to Android's default
messages. If you need to check the current message text, call
[`getStartUserSessionMessage()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getStartUserSessionMessage(android.content.ComponentName)) or
[`getEndUserSessionMessage()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getEndUserSessionMessage(android.content.ComponentName)).

Your DPC should set [localized messages](https://developer.android.com/guide/topics/resources/localization)
for the user's current locale. You also need to update the messages when the
user's locale changes:

### Kotlin

```kotlin
override fun onReceive(context: Context?, intent: Intent?) {
    // Added the <action android:name="android.intent.action.LOCALE_CHANGED" />
    // intent filter for our DeviceAdminReceiver subclass in the app manifest file.
    if (intent?.action === ACTION_LOCALE_CHANGED) {

        // Android's resources return a string suitable for the new locale.
        getManager(context).setStartUserSessionMessage(
                getWho(context),
                context?.getString(R.string.start_user_session_message))

        getManager(context).setEndUserSessionMessage(
                getWho(context),
                context?.getString(R.string.end_user_session_message))
    }
    super.onReceive(context, intent)
}
```

### Java

```java
public void onReceive(Context context, Intent intent) {
  // Added the <action android:name="android.intent.action.LOCALE_CHANGED" />
  // intent filter for our DeviceAdminReceiver subclass in the app manifest file.
  if (intent.getAction().equals(ACTION_LOCALE_CHANGED)) {

    // Android's resources return a string suitable for the new locale.
    getManager(context).setStartUserSessionMessage(
        getWho(context),
        context.getString(R.string.start_user_session_message));

    getManager(context).setEndUserSessionMessage(
        getWho(context),
        context.getString(R.string.end_user_session_message));
  }
  super.onReceive(context, intent);
}
```

## DPC coordination

Managing secondary users typically needs two instances of your DPC---one that owns
the fully managed device while the other owns the secondary user. When creating
a new user, the admin of the fully managed device sets another instance of
itself as the admin of the new user.

### Affiliated users

Some of the APIs in this developer's guide only work when the secondary users
are [affiliated](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#isAffiliatedUser()). Because Android disables some features
(network logging for example) when you add new unaffiliated secondary users to
the device, you should affiliate users as soon as possible. See the example in
[Setup](https://developer.android.com/work/dpc/dedicated-devices/multiple-users#dpc-coord-setup) below.

### Setup

Set up new secondary users (from the DPC that owns the secondary user) before
letting people use them. You can do this setup from the
[`DeviceAdminReceiver.onEnabled()`](https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver#onEnabled(android.content.Context,%20android.content.Intent)) callback. If you previously
set any admin extras in the call to `createAndManageUser()`, you can get the
values from the `intent` argument. The following example shows a DPC affiliating
a new secondary user in the callback:

### Kotlin

```kotlin
override fun onEnabled(context: Context?, intent: Intent?) {
    super.onEnabled(context, intent)

    // Get the affiliation ID (our DPC previously put in the extras) and
    // set the ID for this new secondary user.
    intent?.getStringExtra(AFFILIATION_ID_KEY)?.let {
        val dpm = getManager(context)
        dpm.setAffiliationIds(getWho(context), setOf(it))
    }
    // Continue setup of the new secondary user ...
}
```

### Java

```java
public void onEnabled(Context context, Intent intent) {
  // Get the affiliation ID (our DPC previously put in the extras) and
  // set the ID for this new secondary user.
  String affiliationId = intent.getStringExtra(AFFILIATION_ID_KEY);
  if (affiliationId != null) {
    DevicePolicyManager dpm = getManager(context);
    dpm.setAffiliationIds(getWho(context),
        new HashSet<String>(Arrays.asList(affiliationId)));
  }
  // Continue setup of the new secondary user ...
}
```

### RPCs between DPCs

Even though the two DPC instances are running under separate users, the DPCs
that own the device and the secondary users can communicate with each other.
Because calling another DPC's service crosses user boundaries, your DPC can't
call `bindService()` as you [normally would in
Android](https://developer.android.com/guide/components/bound-services). To bind to a service running in
another user, call
[`DevicePolicyManager.bindDeviceAdminServiceAsUser()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#bindDeviceAdminServiceAsUser(android.content.ComponentName,%20android.content.Intent,%20android.content.ServiceConnection,%20int,%20android.os.UserHandle)).
![Primary user and two affiliated secondary users calling RPCs.](https://developer.android.com/static/images/work/dpc/dedicated-devices/secondary-users-rpcs.svg) **Figure 2.** Admins of affiliated primary and secondary users calling service methods

Your DPC can only bind to services running in the users returned by
[`DevicePolicyManager.getBindDeviceAdminTargetUsers()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getBindDeviceAdminTargetUsers(android.content.ComponentName)).
The following example shows the admin of a secondary user binding to the admin
of the fully managed device:

### Kotlin

```kotlin
// From a secondary user, the list contains just the primary user.
dpm.getBindDeviceAdminTargetUsers(adminName).forEach {

    // Set up the callbacks for the service connection.
    val intent = Intent(mContext, FullyManagedDeviceService::class.java)
    val serviceconnection = object : ServiceConnection {
        override fun onServiceConnected(componentName: ComponentName,
                                        iBinder: IBinder) {
            // Call methods on service ...
        }
        override fun onServiceDisconnected(componentName: ComponentName) {
            // Clean up or reconnect if needed ...
        }
    }

    // Bind to the service as the primary user [it].
    val bindSuccessful = dpm.bindDeviceAdminServiceAsUser(adminName,
            intent,
            serviceconnection,
            Context.BIND_AUTO_CREATE,
            it)
}
```

### Java

```java
// From a secondary user, the list contains just the primary user.
List<UserHandle> targetUsers = dpm.getBindDeviceAdminTargetUsers(adminName);
if (targetUsers.isEmpty()) {
  // If the users aren't affiliated, the list doesn't contain any users.
  return;
}

// Set up the callbacks for the service connection.
Intent intent = new Intent(mContext, FullyManagedDeviceService.class);
ServiceConnection serviceconnection = new ServiceConnection() {
  @Override
  public void onServiceConnected(
      ComponentName componentName, IBinder iBinder) {
    // Call methods on service ...
  }

  @Override
  public void onServiceDisconnected(ComponentName componentName) {
    // Clean up or reconnect if needed ...
  }
};

// Bind to the service as the primary user.
UserHandle primaryUser = targetUsers.get(0);
boolean bindSuccessful = dpm.bindDeviceAdminServiceAsUser(
    adminName,
    intent,
    serviceconnection,
    Context.BIND_AUTO_CREATE,
    primaryUser);
```

## Additional resources

To learn more about dedicated devices, read the following documents:

- [Dedicated devices overview](https://developer.android.com/work/dpc/dedicated-devices) is an overview of dedicated devices.
- [Lock task mode](https://developer.android.com/work/dpc/dedicated-devices/lock-task-mode) explains how to lock a dedicated device to a single app or set of apps.
- [Dedicated devices cookbook](https://developer.android.com/work/dpc/dedicated-devices/cookbook) with further examples to restrict the dedicated devices and enhance the user experience.