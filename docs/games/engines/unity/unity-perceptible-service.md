---
title: Run a perceptible service in a separate process with Unity  |  Android game development  |  Android Developers
url: https://developer.android.com/games/engines/unity/unity-perceptible-service
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Google Play](https://developer.android.com/distribute)
* [Games dev center](https://developer.android.com/games)
* [Guides](https://developer.android.com/games/guides)

Send feedback

# Run a perceptible service in a separate process with Unity Stay organized with collections Save and categorize content based on your preferences.





This guide covers the configuration and implementation needed to run an Android
perceptible service (Foreground Service, or FGS) in a private process from a
Unity application.

## 1. Configure perceptible-service support

This section explains how to set up the required permissions and declare the
service in your project's manifest.

### 1.1 Permissions and service declaration

The custom
[`Assets/Plugins/Android/AndroidManifest.xml`](https://docs.unity3d.com/6000.5/Documentation/Manual/android-modify-gradle-project-files-templates.html)
must declare the launcher Activity, perceptible-service permissions,
notification permission, network permission, and the service:

```
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
    <uses-permission android:name="android.permission.FOREGROUND_SERVICE" />
    <uses-permission android:name="android.permission.FOREGROUND_SERVICE_DATA_SYNC" />
    <uses-permission android:name="android.permission.POST_NOTIFICATIONS" />
    <uses-permission android:name="android.permission.INTERNET" />

    <application>
        <activity
            android:name="com.unity3d.player.UnityPlayerActivity"
            android:theme="@style/UnityThemeSelector"
            android:exported="true">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
            <meta-data android:name="unityplayer.UnityActivity" android:value="true" />
        </activity>

        <service
            android:name="com.sample.fgs.DownloadService"
            android:process=":downloader"
            android:exported="false"
            android:stopWithTask="false"
            android:foregroundServiceType="dataSync" />
    </application>
</manifest>
```

[`foregroundServiceType`](/develop/background-work/services/fgs/service-types)
must match the real work: `dataSync` for transfers, `mediaPlayback` for
playback, `location` for location tracking. It must agree with the
corresponding `FOREGROUND_SERVICE_<TYPE>` permission and the
`startForeground` call — all three must be consistent, or service startup
fails.

### 1.2 Add the service-process Java to the Unity project

The FGS service process runs Java. Package the service implementation Java
code into a jar and place it under
[Assets/Plugins/Android/](https://docs.unity3d.com/Manual/AndroidAARPlugins.html).
Unity automatically includes jars in that directory into Gradle's libs/
input and packages them into the APK; the service process loads these classes
at runtime.
For more information about how to implement the service in Java or Kotlin,
see [Java implementation](#java-implementation).

## 2. Configure a separate process

The process boundary is enabled by one manifest attribute:

```
android:process=":downloader"
```

The leading colon creates an application-private process named
`your.package.name:downloader`. It has a different PID from the main process
and can survive after the main process terminates.

### 2.1 The service process has no Unity

To avoid bringing Unity's `libunity.so`, the IL2CPP runtime, and similar into
the service process, service-side Java shouldn't use any Unity classes
(including `UnityPlayer.currentActivity`), and should depend only on Android
Context, Intent extras, and platform APIs. The Unity engine runtime is loaded
only through the main process's `UnityPlayerActivity`; the private
`:downloader` process doesn't load these libraries, so referencing Unity
classes doesn't work in the service process.

### 2.2 Process startup entry points

After the main process calls `startForegroundService`, the system forks the
`:downloader` service process:

* Instantiates `Application` and calls `Application.onCreate` — this
  runs in every process, so initialization needed by the service process
  must be done again here. For more information, see section 2.3.
* Creates `DownloadService` and calls `onCreate` — this is the
  service-process entry point.
* Calls back `onStartCommand` with the Intent constructed at startup. The
  service promotes itself to the foreground here and starts the worker.
  For more information, see section 3.1.

### 2.3 State exists once per process

Dex code is shared read-only, but runtime state isn't:

* `Application.attachBaseContext` and `Application.onCreate` run in every
  process that hosts application components.
* Static initializers and static fields exist independently in each process.
  Assigning a static field in the main process doesn't communicate with the
  service.
* Unity, C#, and Activities remain in the main process.

## 3. Java implementation

This section covers the Java side of the FGS module: 3.1 and 3.2 are
`DownloadService` in the service process; 3.3 is `FgsBridge` in the main
process (the entry point C# calls using JNI).

### 3.1 Promote to foreground first

```
public class DownloadService extends Service {
    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {
        try {
            startForegroundCompat();

            // Start the download thread; must come after promoting to foreground
            // ...
        } catch (Exception e) {
            Log.e(TAG, "onStartCommand() failed [errorType="
                    + e.getClass().getSimpleName() + "]: " + e.getMessage(), e);
            stopSelf();
        }

        return START_NOT_STICKY;
    }

    private void startForegroundCompat() {
        Notification notification = buildNotification(0L);
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
            startForeground(NOTIFICATION_ID, notification,
                    ServiceInfo.FOREGROUND_SERVICE_TYPE_DATA_SYNC);
        } else {
            startForeground(NOTIFICATION_ID, notification);
        }
    }

    ...
```

### 3.2 Add the notification

A perceptible service needs an ongoing notification on a notification channel
to report progress. The notification carries a Stop action that sends
`ACTION_STOP` to the service itself using `PendingIntent.getService` to stop it.

```
private Notification buildNotification(long progressBytes) {
    int progressMib = (int) (progressBytes / MIB);

    Intent launchIntent = getPackageManager().getLaunchIntentForPackage(getPackageName());
    PendingIntent contentIntent = launchIntent != null
            ? PendingIntent.getActivity(this, 0, launchIntent,
                    PendingIntent.FLAG_IMMUTABLE | PendingIntent.FLAG_UPDATE_CURRENT)
            : null;

    Intent stopIntent = new Intent(this, DownloadService.class)
            .setAction(ACTION_STOP);
    PendingIntent stopPendingIntent = PendingIntent.getService(this, 0,
            stopIntent, PendingIntent.FLAG_IMMUTABLE
            | PendingIntent.FLAG_UPDATE_CURRENT);

    Notification.Builder builder = new Notification.Builder(this,
            CHANNEL_ID)
            .setContentTitle("Download service")
            .setContentText("Downloaded " + progressMib + " MB / " + TOTAL_MIB + " MB")
            .setSmallIcon(android.R.drawable.stat_sys_download)
            .setProgress(TOTAL_MIB, progressMib, false)
            .setOngoing(true)
            .setOnlyAlertOnce(true)
            .addAction(new Notification.Action.Builder(null,
                    "Stop", stopPendingIntent).build());

    if (contentIntent != null) {
        builder.setContentIntent(contentIntent);
    }

    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.S) {
        builder.setForegroundServiceBehavior(
                Notification.FOREGROUND_SERVICE_IMMEDIATE);
    }
    return builder.build();
}
```

### 3.3 Java host entry point

`FgsBridge` is the Java entry point the main process uses to control the FGS
(it runs in the main process, not the service process). C# calls these static
methods using JNI to start and stop the service and handle notification
permission:

```
public class FgsBridge {
    // Start the :downloader perceptible service and begin downloading
    public static void startDownloadService(Context context) {
        try {
            context.startForegroundService(new Intent(context, DownloadService.class));
        } catch (Exception e) {
            Log.e(TAG, "startDownloadService() failed [errorType="
                    + e.getClass().getSimpleName() + "]: " + e.getMessage(), e);
        }
    }

    // Stop the service: sends a stop intent; the service removes its
    // notification before exiting
    public static void stopDownloadService(Context context) {
        try {
            context.startService(new Intent(context, DownloadService.class)
                    .setAction(ACTION_STOP));
        } catch (Exception e) {
            Log.e(TAG, "stopDownloadService() failed [errorType="
                    + e.getClass().getSimpleName() + "]: " + e.getMessage(), e);
        }
    }

    // Request notification permission (only needed on API 33+; if already
    // granted, no dialog is shown and it returns immediately)
    public static void requestNotificationPermission(Activity activity) {
        if (Build.VERSION.SDK_INT < 33) {
            return;
        }
        try {
            activity.requestPermissions(
                    new String[] { POST_NOTIFICATIONS }, NOTIFICATION_PERMISSION_REQUEST);
        } catch (Exception e) {
            Log.e(TAG, "requestNotificationPermission() failed [errorType="
                    + e.getClass().getSimpleName() + "]: " + e.getMessage(), e);
        }
    }
}
```

## 4. Start and control the FGS from Unity (C#)

`AndroidBridge` is the C# wrapper that calls `FgsBridge` using JNI. The three
method implementations:

```
public static void StartDownloadService()
{
#if UNITY_ANDROID && !UNITY_EDITOR
    CallStatic("startDownloadService");
#else
    Debug.Log("StartDownloadService() no-op outside Android");
#endif
}

public static void StopDownloadService()
{
#if UNITY_ANDROID && !UNITY_EDITOR
    CallStatic("stopDownloadService");
#else
    Debug.Log("StopDownloadService() no-op outside Android");
#endif
}

public static void RequestNotificationPermission()
{
#if UNITY_ANDROID && !UNITY_EDITOR
    CallStatic("requestNotificationPermission");
#else
    Debug.Log("RequestNotificationPermission() no-op outside Android");
#endif
}
```

`CallStatic` is an internal JNI helper that resolves the `FgsBridge` class and
calls the corresponding Java static method. `RequestNotificationPermission`
should be called at application startup so that the notification appears
immediately when the service process starts.






Send feedback