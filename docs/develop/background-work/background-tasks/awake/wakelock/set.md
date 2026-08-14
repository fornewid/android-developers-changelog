---
title: https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/set
url: https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/set
source: md.txt
---

You can set a *wake lock* to temporarily keep the device awake.

> [!NOTE]
> **Note:** Creating and holding wake locks can have a dramatic impact on the device's battery life. You shouldn't use wake locks if there are any suitable alternatives. For other options, see the [Choose the right API to keep the device awake](https://developer.android.com/develop/background-work/background-tasks/awake) documentation. If you do need to use a wake lock, make sure to hold it for as short a time as possible.

## Dependencies

Your app must have the [`WAKE_LOCK`](https://developer.android.com/reference/android/Manifest.permission#WAKE_LOCK) permission to set a wake lock.
Add the permission to your app's manifest:

    <uses-permission android:name="android.permission.WAKE_LOCK" />

## Create and acquire a wake lock

To acquire a wake lock, do the following:

1. Call [`PowerManager.newWakeLock()`](https://developer.android.com/reference/android/os/PowerManager#newWakeLock(int,%20java.lang.String)) to create a wake lock.
   This creates and configures a `PowerManager.WakeLock` object but does not
   actually keep the device awake.

2. When you want to keep the device awake, call the wake lock object's
   [`acquire()`](https://developer.android.com/reference/android/os/PowerManager.WakeLock#acquire(long)) method.

For example, if your app includes a broadcast receiver that uses a service to do
some work, you can use this code to set and acquire a wake lock:


### Kotlin

```kotlin
val wakeLock: PowerManager.WakeLock =
    (getSystemService(POWER_SERVICE) as PowerManager).run {
        newWakeLock(PowerManager.PARTIAL_WAKE_LOCK, "MyClassName::MyWakelockTag").apply {
            acquire(WAKELOCK_TIMEOUT)
        }
    }
```

### Java

```java
PowerManager powerManager = (PowerManager) getSystemService(POWER_SERVICE);
PowerManager.WakeLock wakeLock =
        powerManager.newWakeLock(PowerManager.PARTIAL_WAKE_LOCK, "MyClassName::MyWakelockTag");
wakeLock.acquire(WAKELOCK_TIMEOUT);
```

<br />

### Key points about this code

- When the code creates the wake lock object, it uses the class's name as part
  of the wake lock tag. We recommend including your package, class, or method
  name as part of the wake lock tag. That way, if an error occurs, it's easier
  to locate the wake lock in your source code. For more information, see [Name
  the wake lock properly](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/best-practices#name).

- `WakeLock.acquire(long)` is passed a timeout value in milliseconds. The
  system releases the wake lock after this much time passes, if you have not
  [already released it](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/release).

## See also

- [Release a wake lock](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/release)
- [Follow wake lock best practices](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/best-practices)