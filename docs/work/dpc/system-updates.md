---
title: https://developer.android.com/work/dpc/system-updates
url: https://developer.android.com/work/dpc/system-updates
source: md.txt
---

# Manage system updates

This developer's guide explains how your device policy controller (DPC) can manage Android system updates on behalf of the device user.

## Introduction

Android devices can receive and install over-the-air (OTA) updates to the system and application software. Android notifies the device user that a system update is available and the device user can install the update immediately or later.

Using your DPC, an IT admin can manage system updates for the device user. DPCs can own a fully managed device (called a device owner) or can own a work profile (called a profile owner). Table 1 shows how device owners can manage system updates, while profile owners can only report information about system updates.

**Table 1**: Tasks available to DPCs depend on the owner mode

|                                                                     Task                                                                      | Device owner | Profile owner |
|-----------------------------------------------------------------------------------------------------------------------------------------------|--------------|---------------|
| [Check for pending system updates](https://developer.android.com/work/dpc/system-updates#check-updates)                                       |              |               |
| [Receive callbacks when new system updates become available](https://developer.android.com/work/dpc/system-updates#callbacks)                 |              |               |
| [Set a local update policy to control when Android installs system updates](https://developer.android.com/work/dpc/system-updates#set-policy) |              |               |
| [Freeze the OS version over critical periods](https://developer.android.com/work/dpc/system-updates#freeze-periods)                           |              |               |

## Check for pending updates

A pending update is a system update for a device that hasn't yet been installed. Your DPC can help IT admins check which devices have pending system updates---and perhaps ask the device users to install critical updates promptly.

Device owners and profile owners running in Android 8.0 (API level 26) or higher can check if a device has a pending system update. Call[`DevicePolicyManager.getPendingSystemUpdate()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getPendingSystemUpdate(android.content.ComponentName))which returns`null`if the device is up to date. If a system update is pending, the method returns information about the update.

### Find out more about a pending update

After calling`getPendingSystemUpdate()`you can inspect the returned`SystemUpdateInfo`value to find out more about the pending update. The following example shows how you might find out when a pending update was first available to the device:  

### Kotlin

```kotlin
val firstAvailable =
        dpm.getPendingSystemUpdate(adminName)?.receivedTime
firstAvailable?.let {
    Log.i(TAG, "Update first available: ${Date(firstAvailable)}")
}
```

### Java

```java
SystemUpdateInfo updateInfo = dpm.getPendingSystemUpdate(adminName);
if (updateInfo != null) {
  Long firstAvailable = updateInfo.getReceivedTime();
  Log.i(TAG, "Update first available: " + new Date(firstAvailable));
}
```

## System callbacks

When an update becomes available, the Android system notifies device owners about the new update. In Android 8.0 or higher, the system notifies profile owners too.

In your`DeviceAdminReceiver`subclass, override the[`onSystemUpdatePending()`](https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver#onSystemUpdatePending(android.content.Context,%20android.content.Intent,%20long))callback. You don't need to register or advertise for your DPC to receive the callback. The system might call this method more than once for a single update so check the update's status before responding. Call`getPendingSystemUpdate()`to find out more about the system update in the callback. The following example shows how you can do this:  

### Kotlin

```kotlin
/**
 * Called when a new update is available.
 */
override fun onSystemUpdatePending(context: Context?, intent: Intent?,
                                   receivedTime: Long) {

    // System update information is supported in API level 26 or higher.
    if (Build.VERSION.SDK_INT < Build.VERSION_CODES.O) {
        return
    }

    val updateInfo = getManager(context)
            .getPendingSystemUpdate(getWho(context))
            ?: return
    if (updateInfo.securityPatchState ==
            SystemUpdateInfo.SECURITY_PATCH_STATE_TRUE) {
        // Perhaps install because this is a security patch.
        // ...
    }
}
```

### Java

```java
/**
 * Called when a new update is available.
 */
public void onSystemUpdatePending (Context context, Intent intent,
                                   long receivedTime) {

  // System update information is supported in API level 26 or higher.
  if (Build.VERSION.SDK_INT < Build.VERSION_CODES.O) {
    return;
  }
  SystemUpdateInfo updateInfo = getManager(context)
      .getPendingSystemUpdate(getWho(context));
  if (updateInfo == null) {
    return;
  }
  if (updateInfo.getSecurityPatchState() ==
      SystemUpdateInfo.SECURITY_PATCH_STATE_TRUE) {
    // Perhaps install because this is a security patch.
    // ...
  }
}
```

When a system has more than one DPC, for example work profiles on fully managed devices, the device owner and profile owner both receive the callback.

## Update policies

A device owner can control when updates are installed by setting a local system update policy for a device. The system update policy can be one of three types:

Automatic
:   Installs system updates as soon as they become available (without user interaction). Setting this policy type immediately installs any pending updates that might be postponed or waiting for a maintenance window.

Windowed
:   Installs system updates during a daily maintenance window (without user interaction). Set the start and end of the daily maintenance window, as minutes of the day, when creating a new windowed policy.

Postponed
:   Postpones the installation of system updates for 30 days. After the 30-day period has ended, the system prompts the device user to install the update.

### Postponement periods

The system limits each update to one 30-day postponement. The period begins when the system first postpones the update and setting new postponement policies won't extend the period.
| **Caution:** Postponing OTA updates can prevent devices from receiving critical updates. For this reason device manufacturers or carriers might choose to exempt important security updates from a postponement policy. Exempted updates notify the device user when they become available.

Besides postponement, Android might not be able to install an update for other reasons such as no connectivity, insufficient disk space, or low battery.

The system resets the 30-day postponement timer if a different update becomes available during the period---giving IT admins a chance to try the combined system updates. Once 30 days have passed without a new update, the system prompts the user to install all the pending updates. Later, when a new system update becomes available, the 30-day period begins again.

### How to set a policy

You can set update policies in Android 8.0 (API level 26) or higher. To specify when the device should install system updates, create an instance of[`SystemUpdatePolicy`](https://developer.android.com/reference/android/app/admin/SystemUpdatePolicy#example)using one of the three types outlined above. To set a policy, your device owner calls the`DevicePolicyManager`method[`setSystemUpdatePolicy()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setsystemupdatepolicy). The following code sample shows how you might do this. To see a windowed-policy example, look at the[`SystemUpdatePolicy`](https://developer.android.com/reference/android/app/admin/SystemUpdatePolicy#example)documentation.  

### Kotlin

```kotlin
// Create the system update policy to postpone installation for 30 days.
val policy = SystemUpdatePolicy.createPostponeInstallPolicy()

// Get a DevicePolicyManager instance to set the policy on the device.
val dpm = context.getSystemService(Context.DEVICE_POLICY_SERVICE)
        as DevicePolicyManager
val adminName = getComponentName(context)

// Set the policy.
dpm.setSystemUpdatePolicy(adminName, policy)
```

### Java

```java
// Create the system update policy to postpone installation for 30 days.
SystemUpdatePolicy policy = SystemUpdatePolicy.createPostponeInstallPolicy();

// Get a DevicePolicyManager instance to set the policy on the device.
DevicePolicyManager dpm = (DevicePolicyManager) context
    .getSystemService(Context.DEVICE_POLICY_SERVICE);
ComponentName adminName = getComponentName(context);

// Set the policy.
dpm.setSystemUpdatePolicy(adminName, policy);
```

Policy instances can't be changed once you create them. To change when a device installs updates, you can create and set a new policy. To remove a policy from a device, call`setSystemUpdatePolicy()`passing`null`as the`policy`argument. After your DPC removes a policy, the device user sees notifications for any available system updates.

Apps can call[`getSystemUpdatePolicy()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getsystemupdatepolicy)to get the current policy for the device. If this method returns`null`, this means a policy isn't currently set.

## Freeze periods

To freeze the OS version over critical periods, such as holidays or other busy times, device owners can suspend system updates for up to 90 days. When a device is within a freeze period it behaves as follows:

- The device does not receive any notifications about pending system updates.
- System updates to the OS are not installed.
- Device users cannot manually check for system updates in Settings.

The system enforces a mandatory 60-day buffer period following any defined freeze periods to prevent freezing the device indefinitely. Remember, freezing system updates can prevent devices from receiving critical updates.
**Figure 1.**Two freeze periods set for a device![Calendar showing two freeze periods in a year with 60-day buffers.](https://developer.android.com/static/images/work/dpc/freeze-periods.svg)

You set freeze periods on an update policy. You can't set freeze periods without setting a policy. When the device is outside any freeze periods you set, the normal policy behavior (automatic, windowed, or postponed) applies.

### How to set a freeze period

You can set freeze periods in Android 9 (API level 28) or higher. A device owner sets a freeze period on a system update policy before setting the policy for the device. The steps are:

1. Create a new (or get the current) system update policy.
2. Set the freeze periods on the policy by calling[`setFreezePeriods()`](https://developer.android.com/reference/android/app/admin/SystemUpdatePolicy#setfreezeperiods).
3. Set the policy and freeze periods for the device by calling[`setSystemUpdatePolicy()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setsystemupdatepolicy).

Because the freeze period repeats annually, the start and end dates of the period are represented by month and day values. The start day must begin at least 60 days after the end of any previous freeze period. The following example shows how you might set two freeze periods for an existing system update policy:  

### Kotlin

```kotlin
// Get the existing policy from the DevicePolicyController instance.
val policy = dpm.systemUpdatePolicy ?: return

try {
    // Set the two annual freeze periods on the policy for our retail
    // point-of-sale devices.
    val summerSale = FreezePeriod(
            MonthDay.of(6, 1),
            MonthDay.of(7, 31)) // Jun 1 - Jul 31 inclusive
    val winterSale = FreezePeriod(
            MonthDay.of(11, 20),
            MonthDay.of(1, 12)) // Nov 20 - Jan 12 inclusive
    policy.freezePeriods = Arrays.asList(summerSale, winterSale)

    // Set the policy again to activate the freeze periods.
    dpm.setSystemUpdatePolicy(adminName, policy)

} catch (e: SystemUpdatePolicy.ValidationFailedException) {
    // There must be previous periods recorded on the device because
    // summerSale and winterSale don't overlap and are separated by more
    // than 60 days. Report the overlap ...
}
```

### Java

```java
// Get the existing policy from the DevicePolicyController instance.
SystemUpdatePolicy policy = dpm.getSystemUpdatePolicy();

try {
  // Set the two annual freeze periods on the policy for our
  // retail point-of-sale devices.
  FreezePeriod summerSale = new FreezePeriod(
      MonthDay.of(6, 1),
      MonthDay.of(7, 31)); // Jun 1 - Jul 31 inclusive
  FreezePeriod winterSale = new FreezePeriod(
      MonthDay.of(11, 20),
      MonthDay.of(1, 12)); // Nov 20 - Jan 12 inclusive
  policy.setFreezePeriods(Arrays.asList(summerSale, winterSale));

  // Don't forget to set the policy again to activate the freeze periods.
  dpm.setSystemUpdatePolicy(adminName, policy);

} catch (SystemUpdatePolicy.ValidationFailedException e) {
  // There must be previous periods recorded on the device because summerSale
  // and winterSale don't overlap and are separated by more than 60 days.
  // Report the overlap ...
}
```

Both the start day and the end day are inclusive. If the start day is greater than the end day (such as`winterSale`in the previous example), the freeze period extends into the following year.

When setting freeze periods on a system update policy, Android tests for these requirements:

- No freeze period is longer than 90 days.
- The interval between freeze periods is at least 60 days.
- Freeze periods don't overlap.
- There are no duplicate freeze periods.

When setting the system update policy for a device, Android repeats these tests and includes any current or past freeze periods for the device.

Android throws a[`SystemUpdatePolicy.ValidationFailedException`](https://developer.android.com/reference/android/app/admin/SystemUpdatePolicy.ValidationFailedException)when any of these tests fails.

To get a list of freeze periods previously set on a system update policy object, all installed apps can call[`SystemUpdatePolicy.getFreezePeriods()`](https://developer.android.com/reference/android/app/admin/SystemUpdatePolicy#getFreezePeriods()). The following example calls this method to log a device's freeze periods:  

### Kotlin

```kotlin
// Log any freeze periods that might be set on a system update policy.
dpm.systemUpdatePolicy?.freezePeriods?.forEach {
    Log.i(TAG, "Freeze period: $it")
}
```

### Java

```java
// Log any freeze periods that might be set on a system update policy.
SystemUpdatePolicy currentPolicy = dpm.getSystemUpdatePolicy();
if (currentPolicy != null) { // A policy might not be set.
  for (FreezePeriod freezePeriod : currentPolicy.getFreezePeriods()) {
    Log.i(TAG, "Freeze period: " + freezePeriod.toString());
  }
}
```

### Leap years

Android uses the ISO 8601 calendar (also called the Gregorian calendar) to calculate freeze periods and it ignores leap years. This means that February 29th is not recognized as a valid date and is treated as if it were February 28th. Therefore February 29th isn't counted when computing the duration of a freeze period.

### Development and testing

While you're developing and testing your DPC's system update feature, you might need to create many freeze periods. Because Android checks for a 60-day interval between past freeze periods, you might not be able to set a new freeze period without first clearing the record of past periods. To clear the device's freeze period record, run the following command in the[Android Debug Bridge](https://developer.android.com/tools/help/adb)(adb) shell:  

    adb shell dpm clear-freeze-period-record

You can confirm that a device is in a freeze period by checking that the user interface for system updates is disabled.

## Google Play System updates (Mainline)

[Google Play System updates](https://source.android.com/docs/core/ota/modular-system)(also called Mainline updates) are automatically downloaded but require a device reboot to be installed. These updates won't trigger an automatic reboot and instead they are installed on the next user, admin, or policy initiated reboot. Reboots triggered by system update policy will install the associated Google/OEM system update and any previously downloaded Google Play System updates.

Google Play System updates can also be manually installed by navigating to**Settings \> About \> Android Version \> Google Play system update**.

### Roll back an update

In some cases, the[Google Play System Update Rollbacks (GPSUR) tool](https://flash.android.com/tools/google_play_system_update_rollbacks)can be used to recover device state due to a problematic Google Play System Update installation. This tool should be used by advanced users or when directed to do so by support staff as it may result in data loss. Here's how to use the GPSUR tool:

1. If you have[Android Debug Bridge (adb)](https://developer.android.com/studio/command-line/adb)running on your machine, stop the adb service before proceeding so that it doesn't interfere with the rollback process. To stop adb, run`adb kill-server`.
2. [Open the GPSUR tool](https://flash.android.com/tools/google_play_system_update_rollbacks).
3. Click**Allow ADB access**to allow the tool to communicate with your test device through adb.
4. Click**Add new device**.
5. Select your device from the list and click**Connect**. This list might not contain the full device name.
6. On your device's screen, select**Always allow from this computer** and click**OK**to accept the USB debugging connection.
7. Select the connected device in your browser.
8. The button text on the page should switch from*No Rollbacks Available* to*Rollback Recent Updates* if there are rollbacks available on your device. Click**Rollback Recent Updates**.
9. Read the warnings on the**Confirm Rollback** modal and click**Confirm**.
10. Wait for the rollback to complete. Once complete, a**Rollback Successful**modal will appear and the device will reboot. It is now safe to unplug your device.

## Additional resources

To learn more about system updates, read the Android Open Source Project's[OTA Updates](https://source.android.com/devices/tech/ota/)documentation.