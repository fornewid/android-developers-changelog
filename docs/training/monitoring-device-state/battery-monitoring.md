---
title: https://developer.android.com/training/monitoring-device-state/battery-monitoring
url: https://developer.android.com/training/monitoring-device-state/battery-monitoring
source: md.txt
---

When you're altering the frequency of your background updates to reduce the effect of those
updates on battery life, checking the current battery level and charging state is a good place to
start.

The battery-life impact of performing application updates depends on the battery level and
charging state of the device. The impact of performing updates while the device is charging over AC
is negligible, so in most cases you can maximize your refresh rate whenever the device is connected
to a wall charger. Conversely, if the device is discharging, reducing your update rate helps
prolong the battery life.

Similarly, you can check the battery charge level, potentially reducing the frequency of---or
even stopping---your updates when the battery charge is nearly exhausted.

## Determine the current charging state

Start by determining the current charge status. The [BatteryManager](https://developer.android.com/reference/android/os/BatteryManager)
broadcasts all battery and charging details in a sticky [Intent](https://developer.android.com/reference/android/content/Intent) that includes
the charging status.

Because it's a sticky intent, you don't need to register a [BroadcastReceiver](https://developer.android.com/reference/android/content/BroadcastReceiver)---by simply calling `registerReceiver` passing in
`null` as the receiver as shown in the next snippet, the current battery status intent is
returned. You could pass in an actual [BroadcastReceiver](https://developer.android.com/reference/android/content/BroadcastReceiver) object here, but
we'll be handling updates in a later section so it's not necessary.  

### Kotlin

```kotlin
val batteryStatus: Intent? = IntentFilter(Intent.ACTION_BATTERY_CHANGED).let { ifilter ->
    context.registerReceiver(null, ifilter)
}
```

### Java

```java
IntentFilter ifilter = new IntentFilter(Intent.ACTION_BATTERY_CHANGED);
Intent batteryStatus = context.registerReceiver(null, ifilter);
```

You can extract both the current charging status and, if the device is being charged, whether
it's charging via USB or AC charger:


### Kotlin

```kotlin
val status: Int = batteryStatus?.getIntExtra(BatteryManager.EXTRA_STATUS, -1) ?: -1
val isCharging: Boolean = status == BatteryManager.BATTERY_STATUS_CHARGING
        || status == BatteryManager.BATTERY_STATUS_FULL

// How are we charging?
val chargePlug: Int = batteryStatus?.getIntExtra(BatteryManager.EXTRA_PLUGGED, -1) ?: -1
val usbCharge: Boolean = chargePlug == BatteryManager.BATTERY_PLUGGED_USB
val acCharge: Boolean = chargePlug == BatteryManager.BATTERY_PLUGGED_AC
```

### Java

```java
// Are we charging / charged?
int status = batteryStatus.getIntExtra(BatteryManager.EXTRA_STATUS, -1);
boolean isCharging = status == BatteryManager.BATTERY_STATUS_CHARGING ||
                     status == BatteryManager.BATTERY_STATUS_FULL;

// How are we charging?
int chargePlug = batteryStatus.getIntExtra(BatteryManager.EXTRA_PLUGGED, -1);
boolean usbCharge = chargePlug == BatteryManager.BATTERY_PLUGGED_USB;
boolean acCharge = chargePlug == BatteryManager.BATTERY_PLUGGED_AC;
```

Typically you should maximize the rate of your background updates in the case where the device is
connected to an AC charger, reduce the rate if the charge is over USB, and lower it
further if the battery is discharging.

## Monitor changes in charging state

The charging status can change as easily as a device can be plugged in, so it's important to
monitor the charging state for changes and alter your refresh rate accordingly.

The [BatteryManager](https://developer.android.com/reference/android/os/BatteryManager) broadcasts an action whenever the device is connected or
disconnected from power. It's important to receive these events even while your app isn't
running---particularly as these events should impact how often you start your app in order to
initiate a background update---so you should register a [BroadcastReceiver](https://developer.android.com/reference/android/content/BroadcastReceiver) in your manifest to listen for both events by defining the
[ACTION_POWER_CONNECTED](https://developer.android.com/reference/android/content/Intent#ACTION_POWER_CONNECTED) and [ACTION_POWER_DISCONNECTED](https://developer.android.com/reference/android/content/Intent#ACTION_POWER_DISCONNECTED) within an intent filter.  

```xml
<receiver android:name=".PowerConnectionReceiver">
  <intent-filter>
    <action android:name="android.intent.action.ACTION_POWER_CONNECTED"/>
    <action android:name="android.intent.action.ACTION_POWER_DISCONNECTED"/>
  </intent-filter>
</receiver>
```

## Determine the current battery level

In some cases it's also useful to determine the current battery level. You may choose to reduce
the rate of your background updates if the battery charge is below a certain level.

You can find the current battery charge by extracting the current battery level and scale from
the battery status intent as shown here:  

### Kotlin

```kotlin
val batteryPct: Float? = batteryStatus?.let { intent ->
    val level: Int = intent.getIntExtra(BatteryManager.EXTRA_LEVEL, -1)
    val scale: Int = intent.getIntExtra(BatteryManager.EXTRA_SCALE, -1)
    level * 100 / scale.toFloat()
}
```

### Java

```java
int level = batteryStatus.getIntExtra(BatteryManager.EXTRA_LEVEL, -1);
int scale = batteryStatus.getIntExtra(BatteryManager.EXTRA_SCALE, -1);

float batteryPct = level * 100 / (float)scale;
```

## React to significant changes in battery level

You can't easily continually monitor the battery state, but you don't need to.

Generally speaking, the impact of monitoring the battery level has a greater
impact on the battery than your app's normal behavior. For example, registering a
`BroadcastReceiver` in the manifest to cancel pending work when the battery is low will
mainly serve to drain the battery further (and is therefore
[impossible since
Android 8.0](https://developer.android.com/develop/background-work/background-tasks/broadcasts/broadcast-exceptions)). Instead, you can provide constraints on work that describe when it should be run,
allowing the system to make the decision without spending power starting your app.

It is generally good practice to not run your background updates when the battery is
critically low. It doesn't matter how fresh your data is if the phone turns itself off before you
can make use of it. To do this,
[use the WorkManager library](https://developer.android.com/develop/background-work/background-tasks/persistent/getting-started)
with a
[`BatteryNotLow` constraint](https://developer.android.com/develop/background-work/background-tasks/persistent/getting-started/define-work#work-constraints)
to specify that the work should not be run if the battery is low (in addition to any relevant
`NetworkType` constraints).

In many cases, the act of charging a device is coincident with putting it
into a dock. To learn more, see
[Determine and
monitor the docking state and type](https://developer.android.com/training/monitoring-device-state/docking-monitoring).