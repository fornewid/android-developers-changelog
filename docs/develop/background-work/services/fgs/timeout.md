---
title: https://developer.android.com/develop/background-work/services/fgs/timeout
url: https://developer.android.com/develop/background-work/services/fgs/timeout
source: md.txt
---

If an app targets Android 15 or higher, the system places
restrictions on how long certain foreground services are allowed to run while
your app is in the background. Currently, this restriction only applies to
[`dataSync`](https://developer.android.com/develop/background-work/services/fgs/service-types#data-sync) and
[`mediaProcessing` foreground service type](https://developer.android.com/develop/background-work/services/fgs/service-types#media-processing) foreground
services. There are more restrictive limits on the [`shortService` foreground
service type](https://developer.android.com/develop/background-work/services/fgs/service-types#short-service) which are discussed in that service type's
documentation.

## Timeout behavior

The system permits `dataSync` and `mediaProcessing` foreground services to run
for a total of 6 hours in a 24-hour period, after which the system calls the
running service's [`Service.onTimeout(int, int)`](https://developer.android.com/reference/android/app/Service#onTimeout(int,%20int)) method
(introduced in Android 15). (The `mediaProcessing` foreground
service type was added in Android 15.) The six-hour time limit is
tracked separately for `dataSync` and for `mediaProcessing` services. For
example, if a `dataSync` service just ran for one hour, the app would only have
five hours available for `dataSync` foreground services, but it would
have a full six hours available for `mediaProcessing` services.

> [!NOTE]
> **Note:** `shortService` foreground services have a more restrictive time limit. For more information, see the [short service documentation](https://developer.android.com/develop/background-work/services/fgs/service-types#short-service).

When a foreground service reaches the six-hour limit, the service has a few
seconds to call [`Service.stopSelf()`](https://developer.android.com/reference/android/app/Service#stopSelf()). When the system calls
`Service.onTimeout()`, the service is no longer considered a foreground service.
If the service does not call `Service.stopSelf()`, the system throws an internal
exception. The exception is logged in [Logcat](https://developer.android.com/tools/logcat) with the following
message:

    Fatal Exception: android.app.RemoteServiceException: "A foreground service of
    type [service type] did not stop within its timeout: [component name]"

> [!NOTE]
> **Note:** The 6-hour time limit is shared by all of an app's foreground services of the specified type. For example, if an app runs a `dataSync` service for four hours, then starts a different `dataSync` service, that second service will only be allowed to run for two hours. However, if the user brings the app to the foreground, the timer resets and the app has 6 hours available.

To avoid problems with this behavior change, you can do one or more of the
following:

1. Have your service implement the new `Service.onTimeout(int, int)` method. When your app receives the callback, make sure to call `stopSelf()` within a few seconds. (If you don't stop the app right away, the system generates a failure.)
2. Make sure your app's `dataSync` and `mediaProcessing` services don't run for more than a total of 6 hours in any 24-hour period (unless the user interacts with the app, resetting the timer).
3. Only start `dataSync` or `mediaProcessing` foreground services as a result of direct user interaction; since your app is in the foreground when the service starts, your service has the full six hours after the app goes to the background.
4. Instead of using these foreground services, use an use an [alternative
   API](https://developer.android.com/develop/background-work/background-tasks#alternative-apis), like WorkManager. In particular, instead of using a `dataSync` foreground service, consider using an [alternative API](https://developer.android.com/develop/background-work/background-tasks/data-transfer-options).

If your app's `dataSync` foreground services have run for 6 hours in the last
24, you cannot start another `dataSync` foreground service *unless* the user
has brought your app to the foreground (which resets the timer). If you try to
start another `dataSync` foreground service, the system throws
[`ForegroundServiceStartNotAllowedException`](https://developer.android.com/reference/android/app/ForegroundServiceStartNotAllowedException)
with an error message like "Time limit already exhausted for foreground service
type dataSync".

## Testing

To test your app's behavior, you can enable data sync timeouts even if your app
is not targeting Android 15 (as long as the app is running on an Android 15
device). To enable timeouts, run the following [`adb`](https://developer.android.com/tools/adb) command:

    adb shell am compat enable FGS_INTRODUCE_TIME_LIMITS your-package-name

You can also adjust the timeout period, to make it easier to test how your
app behaves when the limit is reached. To set a new timeout period for
`dataSync` foreground services, run the following `adb` command:

    adb shell device_config put activity_manager data_sync_fgs_timeout_duration duration-in-milliseconds

To set a new timeout period for `mediaProcessing` foreground services, run this
command:

    adb shell device_config put activity_manager media_processing_fgs_timeout_duration duration-in-milliseconds