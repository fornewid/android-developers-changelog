---
title: https://developer.android.com/develop/background-work/background-tasks/bg-work-restrictions
url: https://developer.android.com/develop/background-work/background-tasks/bg-work-restrictions
source: md.txt
---

# System restrictions on background tasks

Background processes can be memory- and battery-intensive. For example, an implicit broadcast may start many background processes that have registered to listen for it, even if those processes may not do much work. This can have a substantial impact on both device performance and user experience.

To avoid system restrictions, make sure you use the right API for your background task. The[Background tasks overview](https://developer.android.com/develop/background-work/background-tasks)documentation helps you choose the right API for your needs.

## User-initiated restrictions

If an app exhibits some of the bad behaviors described in[Android vitals](https://developer.android.com/topic/performance/vitals), the system prompts the user to restrict that app's access to system resources.

If the system notices that an app is consuming excessive resources, it notifies the user, and gives the user the option of restricting the app's actions. Behaviors that can trigger the notice include:

1. **Excessive wake locks**: 1 partial wake lock held for an hour when screen is off
2. **Excessive background services**: If app targets API levels lower than 26 and has excessive background services

The precise restrictions imposed are determined by the device manufacturer. For example, on AOSP builds, restricted apps cannot run jobs, trigger alarms, or use the network, except when the app is in the foreground.
| **Note:** To avoid these limitations and their associated warnings, you should use WorkManager to schedule your background tasks.

## Restrictions on receiving network activity broadcasts

Apps don't receive[`CONNECTIVITY_ACTION`](https://developer.android.com/reference/android/net/ConnectivityManager#CONNECTIVITY_ACTION)broadcasts if they register to receive them in their manifest, and processes that depend on this broadcast won't start. This could pose a problem for apps that want to listen for network changes or perform bulk network activities when the device connects to an unmetered network. Several solutions to get around this restriction already exist in the Android framework, but choosing the right one depends on what you want your app to accomplish.
| **Note:** A[`BroadcastReceiver`](https://developer.android.com/reference/android/content/BroadcastReceiver)registered with[`Context.registerReceiver`](https://developer.android.com/reference/android/content/Context#registerReceiver(android.content.BroadcastReceiver,%20android.content.IntentFilter))continues to receive these broadcasts while the app is running.

### Schedule work on unmetered connections

When building a`WorkRequest`, add a`NetworkType.UNMETERED``Constraint`.  

    fun scheduleWork(context: Context) {
        val workManager = WorkManager.getInstance(context)
        val workRequest = OneTimeWorkRequestBuilder<MyWorker>()
           .setConstraints(
               Constraints.Builder()
                   .setRequiredNetworkType(NetworkType.UNMETERED)
                   .build()
               )
           .build()

        workManager.enqueue(workRequest)
    }

When the conditions for your work are met, your app receives a callback to run the[`doWork()`](https://developer.android.com/reference/androidx/work/Worker#doWork())method in the specified`Worker`class.

### Monitor network connectivity while the app is running

Apps that are running can still listen for`CONNECTIVITY_CHANGE`with a registered[`BroadcastReceiver`](https://developer.android.com/reference/android/content/BroadcastReceiver). However, the[`ConnectivityManager`](https://developer.android.com/reference/android/net/ConnectivityManager)API provides a more robust method to request a callback only when specified network conditions are met.

[`NetworkRequest`](https://developer.android.com/reference/android/net/NetworkRequest)objects define the parameters of the network callback in terms of[`NetworkCapabilities`](https://developer.android.com/reference/android/net/NetworkCapabilities). You create[`NetworkRequest`](https://developer.android.com/reference/android/net/NetworkRequest)objects with the[`NetworkRequest.Builder`](https://developer.android.com/reference/android/net/NetworkRequest.Builder)class.[`registerNetworkCallback`](https://developer.android.com/reference/android/net/ConnectivityManager#registerNetworkCallback(android.net.NetworkRequest,%20android.net.ConnectivityManager.NetworkCallback))then passes the[`NetworkRequest`](https://developer.android.com/reference/android/net/NetworkRequest)object to the system. When the network conditions are met, the app receives a callback to execute the[`onAvailable()`](https://developer.android.com/reference/android/net/ConnectivityManager.NetworkCallback#onAvailable(android.net.Network))method defined in its[`ConnectivityManager.NetworkCallback`](https://developer.android.com/reference/android/net/ConnectivityManager.NetworkCallback)class.

The app continues to receive callbacks until either the app exits or it calls[unregisterNetworkCallback()](https://developer.android.com/reference/android/net/ConnectivityManager#unregisterNetworkCallback(android.app.PendingIntent)).

## Restrictions on receiving image and video broadcasts

Apps are not able to send or receive[ACTION_NEW_PICTURE](https://developer.android.com/reference/android/hardware/Camera#ACTION_NEW_PICTURE)or[ACTION_NEW_VIDEO](https://developer.android.com/reference/android/hardware/Camera#ACTION_NEW_VIDEO)broadcasts. This restriction helps alleviate the performance and user experience impacts when several apps must wake up in order to process a new image or video.

### Determine which content authorities triggered work

[`WorkerParameters`](https://developer.android.com/reference/androidx/work/WorkerParameters)allows your app to receive useful information about what content authorities and URIs triggered the work:

`List<Uri> getTriggeredContentUris()`

Returns a list of URIs that have triggered the work. This is empty if either no URIs have triggered the work (for example, the work was triggered due to a deadline or some other reason), or the number of changed URIs is greater than 50.

`List<String> getTriggeredContentAuthorities()`

Returns a string list of content authorities that have triggered the work. If the returned list is not empty, use`getTriggeredContentUris()`to retrieve the details of which URIs have changed.

The following sample code overrides the[`CoroutineWorker.doWork()`](https://developer.android.com/reference/kotlin/androidx/work/CoroutineWorker#CoroutineWorker(android.content.Context,androidx.work.WorkerParameters))method and records the content authorities and URIs that have triggered the job:  

    class MyWorker(
        appContext: Context,
        params: WorkerParameters
    ): CoroutineWorker(appContext, params)
        override suspend fun doWork(): Result {
            StringBuilder().apply {
                append("Media content has changed:\n")
                params.triggeredContentAuthorities
                    .takeIf { it.isNotEmpty() }
                    ?.let { authorities ->
                        append("Authorities: ${authorities.joinToString(", ")}\n")
                        append(params.triggeredContentUris.joinToString("\n"))
                    } ?: append("(No content)")
                Log.i(TAG, toString())
            }
            return Result.success()
        }
    }

## Test app under system restrictions

Optimizing your apps to run on low-memory devices, or in low-memory conditions, can improve performance and user experience. Removing dependencies on background services and manifest-registered implicit broadcast receivers can help your app run better on such devices. It is recommended that you optimize your app to run without the use of these background processes entirely.

Some additional[Android Debug Bridge (ADB)](https://developer.android.com/tools/help/adb)commands can help you test app behavior with those background processes disabled:

- To simulate conditions where implicit broadcasts and background services are unavailable, enter the following command:

  `$ adb shell cmd appops set <package_name> RUN_IN_BACKGROUND ignore`
- To re-enable implicit broadcasts and background services, enter the following command:

  `$ adb shell cmd appops set <package_name> RUN_IN_BACKGROUND allow`

## Further optimize your app

For other good ways to optimize your background tasks' behavior, see the[Optimize battery use for task scheduling APIs](https://developer.android.com/develop/background-work/background-tasks/optimize-battery)documentation.