---
title: https://developer.android.com/develop/background-work/services/fgs/launch
url: https://developer.android.com/develop/background-work/services/fgs/launch
source: md.txt
---

There are two steps to launching a foreground service from your app. First, you
must start the service by calling
[`context.startForegroundService()`](https://developer.android.com/reference/android/content/Context#startForegroundService(android.content.Intent)). Then, have the
service call [`ServiceCompat.startForeground()`](https://developer.android.com/reference/androidx/core/app/ServiceCompat#startForeground(android.app.Service,int,android.app.Notification,int)) to promote
itself into a foreground service.

## Prerequisites

Depending on which API level your app targets, there are some restrictions on
when an app can launch a foreground service.

- Apps that target Android 12 (API level 31) or higher are not allowed to
  start a foreground service while the app is in the background, with a few
  specific exceptions. For more information, and information about the
  exceptions to this rule, see [Restrictions on starting a foreground service
  from the background](https://developer.android.com/develop/background-work/services/fgs/restrictions-bg-start).

- Apps that target Android 14 (API level 34) or higher must request the
  appropriate
  permissions for the foreground service type. When the app attempts to
  promote a service to the foreground, the system checks for the appropriate
  permissions and throws throws [`SecurityException`](https://developer.android.com/reference/java/lang/SecurityException) if
  the app is missing any. For example, if you try to launch a foreground
  service of type `location`, the system checks to make sure your app already
  has either the `ACCESS_COARSE_LOCATION` or `ACCESS_FINE_LOCATION`
  permission. The [foreground service type](https://developer.android.com/develop/background-work/services/fgs/service-types) documentation lists the
  required prerequisites for each foreground service type.

## Launch a service

In order to launch a foreground service, you must first launch it as an
ordinary (non-foreground) service:  

### Kotlin

```kotlin
val intent = Intent(...) // Build the intent for the service
context.startForegroundService(intent)
```

### Java

```java
Context context = getApplicationContext();
Intent intent = new Intent(...); // Build the intent for the service
context.startForegroundService(intent);
```

### Key points about the code

- The code snippet launches a service. However, the service is not yet running in the foreground. Inside the service itself, you need to call `ServiceCompat.startForeground()` to promote the service to a foreground service.

## Promote a service to the foreground

Once a service is running, you need to call
[`ServiceCompat.startForeground()`](https://developer.android.com/reference/androidx/core/app/ServiceCompat#startForeground(android.app.Service,int,android.app.Notification,int)) to request that the service
run in the foreground. Ordinarily you would call this method in the service's
[`onStartCommand()`](https://developer.android.com/reference/android/app/Service#onStartCommand(android.content.Intent,%20int,%20int)) method.

`ServiceCompat.startForeground()` takes the following parameters:

- The service.
- A positive integer that uniquely identifies the service's notification in the status bar.
- The [`Notification`](https://developer.android.com/reference/android/app/Notification) object itself.
- The [foreground service type or types](https://developer.android.com/develop/background-work/services/fgs/service-types) identifying the work done by the service

| **Note:** If you pass a foreground service type to `startForeground` that you did not declare in the manifest, the system throws `IllegalArgumentException`.

The foreground service types you pass to `startForeground()`
[types declared in the manifest](https://developer.android.com/develop/background-work/services/fgs/service-types#declare-fgs), depending on the specific
use case. Then, if you need to add more service types, you can call
`startForeground()` again.

For example, suppose a fitness app runs a running-tracker service that always
needs `location` information, but might or might not need to play media. You
would need to declare both `location` and `mediaPlayback` in the manifest. If a
user starts a run and just wants their location tracked, your app should call
`startForeground()` and pass just the `ACCESS_FINE_LOCATION` permission. Then,
if the user wants to start playing audio, call `startForeground()` again and
pass the bitwise combination of all the foreground service types (in this case,
`ACCESS_FINE_LOCATION|FOREGROUND_SERVICE_MEDIA_PLAYBACK`).
| **Note:** The status bar notification must use a priority of [`PRIORITY_LOW`](https://developer.android.com/reference/androidx/core/app/NotificationCompat#PRIORITY_LOW) or higher. If your app attempts to use a notification that has a lower priority than `PRIORITY_LOW`, the system adds a message to the notification drawer, alerting the user to the app's use of a foreground service.

The following example shows the code a camera service would use to promote
itself to a foreground service:  

### Kotlin

```kotlin
class MyCameraService: Service() {

  private fun startForeground() {
    // Before starting the service as foreground check that the app has the
    // appropriate runtime permissions. In this case, verify that the user has
    // granted the CAMERA permission.
    val cameraPermission =
            PermissionChecker.checkSelfPermission(this, Manifest.permission.CAMERA)
    if (cameraPermission != PermissionChecker.PERMISSION_GRANTED) {
        // Without camera permissions the service cannot run in the foreground
        // Consider informing user or updating your app UI if visible.
        stopSelf()
        return
    }

    try {
        val notification = NotificationCompat.Builder(this, "CHANNEL_ID")
            // Create the notification to display while the service is running
            .build()
        ServiceCompat.startForeground(
            /* service = */ this,
            /* id = */ 100, // Cannot be 0
            /* notification = */ notification,
            /* foregroundServiceType = */
            if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.R) {
                ServiceInfo.FOREGROUND_SERVICE_TYPE_CAMERA
            } else {
                0
            },
        )
    } catch (e: Exception) {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.S
                && e is ForegroundServiceStartNotAllowedException) {
            // App not in a valid state to start foreground service
            // (e.g. started from bg)
        }
        // ...
    }
  }
}
```

### Java

```java
public class MyCameraService extends Service {

    private void startForeground() {
        // Before starting the service as foreground check that the app has the
        // appropriate runtime permissions. In this case, verify that the user
        // has granted the CAMERA permission.
        int cameraPermission =
            ContextCompat.checkSelfPermission(this, Manifest.permission.CAMERA);
        if (cameraPermission == PackageManager.PERMISSION_DENIED) {
            // Without camera permissions the service cannot run in the
            // foreground. Consider informing user or updating your app UI if
            // visible.
            stopSelf();
            return;
        }

        try {
            Notification notification =
                new NotificationCompat.Builder(this, "CHANNEL_ID")
                    // Create the notification to display while the service
                    // is running
                    .build();
            int type = 0;
            if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.R) {
                type = ServiceInfo.FOREGROUND_SERVICE_TYPE_CAMERA;
            }
            ServiceCompat.startForeground(
                    /* service = */ this,
                    /* id = */ 100, // Cannot be 0
                    /* notification = */ notification,
                    /* foregroundServiceType = */ type
            );
        } catch (Exception e) {
            if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.S &&
                    e instanceof ForegroundServiceStartNotAllowedException
            ) {
                // App not in a valid state to start foreground service
                // (e.g started from bg)
            }
            // ...
        }
    }

    //...
}
```

### Key points about the code

- The app has already declared in the manifest that it needs the `CAMERA` permission. However, the app also has to check at runtime to make sure the user granted that permission. If the app does not actually have the correct permissions, it should let the user know about the problem.
- Different foreground service types were introduced with different versions of the Android platform. This code checks what version of Android it's running on and requests the appropriate permissions.
- The code checks for `ForegroundServiceStartNotAllowedException` in case it's trying to start a foreground service in a situation that's not allowed (for example, if it's trying to promote the service to the foreground [while
  the app is in the background](https://developer.android.com/develop/background-work/services/fgs/restrictions-bg-start)).