---
title: https://developer.android.com/about/versions/17/changes/messagequeue
url: https://developer.android.com/about/versions/17/changes/messagequeue
source: md.txt
---

Beginning with Android 17, apps targeting Android 17
or higher receive a new lock-free implementation of
[`android.os.MessageQueue`](https://developer.android.com/reference/android/os/MessageQueue). The new implementation improves performance and
reduces missed frames, but may break clients that reflect on `MessageQueue`
private fields and methods.

Android 17 introduces a significant overhaul to how [`Looper`](https://developer.android.com/reference/android/os/Looper) and
[`Handler`](https://developer.android.com/reference/android/os/Handler) work, by rewriting the underlying [`MessageQueue`](https://developer.android.com/reference/android/os/MessageQueue) class.
Since the first release of the Android operating system, `MessageQueue` relied
on a single lock to manage the main thread's task queue. This design often
caused lock contention; the main thread could be blocked by a background thread,
leading to dropped frames and UI jank.

## Mitigate impact

Your app may be impacted by this change if it or its dependencies rely on
[runtime reflection](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces) to peek inside `MessageQueue`. Avoid using runtime
reflection to inspect `MessageQueue`.

With the legacy implementation, developers sometimes accessed private fields
like `MessageQueue.mMessages` to inspect pending messages. With the new
lock-free implementation, the internal data structures have changed completely.
To maintain binary compatibility, Android 17 keeps the `mMessages` field, but in
the new implementation this field is **always null**, regardless of whether
there are messages in the queue.

In addition, if you use some popular testing libraries, you'll need to update
your libraries to be compatible with the new `MessageQueue` implementation.

### Espresso

Espresso is commonly used for UI testing. The Espresso library needs to know
when the main thread is idle to correctly assert on UI state. Earlier versions
of Espresso relied on reflection techniques that are no longer compatible with
the lock-free MessageQueue.

#### Action

Update to **Espresso 3.7.0** or newer. This version uses the
[`TestLooperManager`](https://developer.android.com/reference/android/os/TestLooperManager) API, particularly new APIs that Android 16 introduced,
to safely interact with the `Looper` without relying on internal implementation
details.

### Robolectric

Similarly, if you run unit tests using Robolectric, you may encounter issues if
your tests rely on the legacy Looper mode.

#### Action

Update to **Robolectric 4.17** or newer. If you are using `@LooperMode(LEGACY)`,
you will need to migrate your tests to the new `@LooperMode(PAUSED)`. Refer to
[Robolectric's migration guide](https://robolectric.org/blog/2019/06/04/paused-looper/) for more information.

## Test the behavior

You can test your app with the behavior change on Android 17 without updating
`targetSDK` by executing the following command:

    adb am compat enable USE_NEW_MESSAGEQUEUE <your-package-name>

This command enables the lock-free `MessageQueue` in your app, if it's a
debuggable build.

If your app targets Android 17, the new behavior is enabled
by default. If you notice unexpected behavior or crashes after targeting this
API level, you can temporarily disable the new implementation to verify if
`MessageQueue` is the cause.

You can toggle the change using either of two options:

1. The [**App Compatibility Changes** menu in **Developer Options**](https://developer.android.com/guide/app-compatibility/test-debug#toggle-dev-options).

2. By running the following ADB command:

       adb am compat disable USE_NEW_MESSAGEQUEUE <your-package-name>

This reverts your app to the legacy, lock-based implementation, allowing you to
identify if the issue was a result of message queue behavior change.