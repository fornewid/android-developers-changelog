---
title: https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/best-practices
url: https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/best-practices
source: md.txt
---

Using a wake lock can impair device performance. If you need to use a wake
lock, it's important to do it properly. This document covers some best practices
that can help you avoid common wake lock pitfalls.

> [!NOTE]
> **Note:** Creating and holding wake locks can have a dramatic impact on the device's battery life. You shouldn't use wake locks if there are any suitable alternatives. For other options, see the [Keep the device awake](https://developer.android.com/develop/background-work/background-tasks/awake) documentation. If you do need to use a wake lock, make sure to hold it for as short a time as possible.

## Name the wake lock properly

We recommend including your package, class, or method name in the wakelock
tag. That way, if an error occurs, it's easier to find the location in your
source code where the wake lock was created. Here are some additional tips:

- Leave out any personally identifying information (PII) in the name, such as an email address. If the device detects PII in the wake lock tag, it logs `_UNKNOWN` instead of the tag you specified.
- Don't get the class or method name programmatically, for example by calling `getName()`. If you try to get the name programmatically, it might get obfuscated by tools like Proguard. Instead use a hard-coded string.
- Don't add a counter or unique identifiers to wake lock tags. The code that creates a wake lock should use the same tag every time it runs. This practice enables the system to aggregate each method's wake lock usage.

## Make sure your app is visible in the foreground

While a wake lock is active, the device is using power. The device's user
should be aware that this is going on. For this reason, if you're using a
wake lock, you should display some notification to the user.
In practice, this means you should get and hold the wakelock in a
[foreground service](https://developer.android.com/develop/background-work/services/fgs). Foreground services are required to display
a notification.

If a foreground service isn't the right choice for your app,
you probably shouldn't be using a wake lock, either. See the
[Choose the right API to keep the device awake](https://developer.android.com/develop/background-work/background-tasks/awake)
documentation for other ways to do work while your app isn't in the foreground.

## Keep the logic simple

Make sure the logic for acquiring and releasing wake locks is as simple as
possible. When your wake lock logic is tied to complex state machines, timeouts,
executor pools, or callback events, any subtle bug in that logic can cause the
wake lock to be held longer than expected. These bugs are difficult to diagnose
and debug.

## Check that the wake lock is always released

If you use a wake lock, you must make sure that every wake lock you acquire
is properly released. This isn't always as easy as it sounds. For example,
the following code has a problem:

### Kotlin

    @Throws(MyException::class)
    fun doSomethingAndRelease() {
        wakeLock.apply {
            acquire()
            doTheWork() // can potentially throw MyException
            release()   // does not run if an exception is thrown
        }
    }

### Java

    void doSomethingAndRelease() throws MyException {
        wakeLock.acquire();
        doTheWork();         // can potentially throw MyException
        wakeLock.release();  // does not run if an exception is thrown
    }

The problem here is that the method `doTheWork()` can throw the exception
`MyException`. If it does, the `doSomethingAndRelease()` method propagates
the exception outward, and it never reaches the `release()` call. The result
is that the wake lock is acquired but not released, which is very bad.

In the corrected code, `doSomethingAndRelease()` makes sure to release the
wake lock even if an exception is thrown:

### Kotlin

    @Throws(MyException::class)
    fun doSomethingAndRelease() {
        wakeLock.apply {
            try {
                acquire()
                doTheWork()
            } finally {
                release()
            }
        }
    }

### Java

    void doSomethingAndRelease() throws MyException {
        try {
            wakeLock.acquire();
            doTheWork();
        } finally {
            wakeLock.release();
        }
    }