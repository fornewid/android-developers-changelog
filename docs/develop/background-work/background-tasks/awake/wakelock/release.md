---
title: https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/release
url: https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/release
source: md.txt
---

This page describes how to release a wake lock held by your app.
It's important to release a wake lock as soon as your app is
finished using it to avoid draining the battery.

## Release an active wake lock

To release an active wake lock, call its [`release()`](https://developer.android.com/reference/android/os/PowerManager.WakeLock#release()) method. Doing so
releases your claim to the CPU.

For example, the following code [acquires a wake lock](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/set),
does some work, then releases the wake lock:


### Kotlin

```kotlin
@Throws(MyException::class)
fun doSomethingAndRelease() {
    wakeLock.apply {
        try {
            acquire(WAKELOCK_TIMEOUT)
            doTheWork()
        } finally {
            release()
        }
    }
}
```

### Java

```java
void doSomethingAndRelease() throws MyException {
    try {
        wakeLock.acquire(WAKELOCK_TIMEOUT);
        doTheWork();
    } finally {
        wakeLock.release();
    }
}
```

<br />

Make sure to release wake locks as soon as they are no longer needed. For
example, if you use a wake lock to allow a background task to finish, make sure
to release the lock as soon as the task finishes.

### Key points about this code

- In this example, the method `doTheWork()` might throw an exception. For this
  reason, the code releases the wake lock in the `finally` block, to make sure
  the wake lock is released whether or not an exception is thrown. It's very
  important to make sure every wake lock you set is released, so you need to
  check every possible code path to make sure the wake lock isn't left active
  on any of them.

- It's best to acquire the wake lock with
  [`WakeLock.acquire(long timeout)`](https://developer.android.com/reference/android/os/PowerManager.WakeLock#acquire(long)), which
  automatically releases the wake lock after the specified timeout period.
  However, you should still release the wake lock explicitly when you no
  longer need it, so you don't hold the wake lock for longer than necessary.

## See also

- [Set a wake lock](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/set)