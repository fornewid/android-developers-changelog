---
title: Run a perceptible service in a separate process with Unreal  |  Android game development  |  Android Developers
url: https://developer.android.com/games/engines/unreal/unreal-perceptible-service
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Google Play](https://developer.android.com/distribute)
* [Games dev center](https://developer.android.com/games)
* [Guides](https://developer.android.com/games/guides)

Send feedback

# Run a perceptible service in a separate process with Unreal Stay organized with collections Save and categorize content based on your preferences.





This guide covers the configuration and implementation needed to run an Android
perceptible service (FGS) in a private process from an Unreal application.

## 1. Configure perceptible-service support

This section explains how to set up the required permissions and declare the
service in your project's manifest.

### 1.1 Permissions and service declaration (UPL additions)

Unreal doesn't replace the engine manifest—UnrealBuildTool generate
AndroidManifest.xml already declared GameActivity, so the UPL only needs to
**add** permissions and the service; the launcher Activity doesn't have to be
restated. Add the following under <androidManifestUpdates> in
Source/PSUnreal/PSUnreal\_UPL.xml:

```
<androidManifestUpdates>
    <addPermission android:name="android.permission.FOREGROUND_SERVICE" />
    <addPermission android:name="android.permission.FOREGROUND_SERVICE_DATA_SYNC" />
    <addPermission android:name="android.permission.POST_NOTIFICATIONS" />

    <addElements tag="application">
        <service
            android:name="com.sample.fgs.DownloadService"
            android:process=":downloader"
            android:exported="false"
            android:foregroundServiceType="dataSync"
            android:stopWithTask="false" />
    </addElements>
</androidManifestUpdates>
```

`foregroundServiceType` must match the real work: `dataSync` for transfers,
`mediaPlayback` for playback, `location` for location tracking. It must agree
with the corresponding `FOREGROUND_SERVICE_<TYPE>` permission and the
`startForeground` call — all three must be consistent, or service startup
fails.

The service uses the fully qualified name `com.sample.fgs.DownloadService`—a
leading dot would resolve relative to the application ID `com.sample.psunreal`,
but the Java module lives in the `com.sample.fgs` package, so it wouldn't be
found.

### 1.2 Add the service-process Java to the Unreal project

Compile the service implementation Java code into a jar and copy it into the
staging libs directory using UPL's <prebuildCopies>. UEDeployAndroid copies
the staging libs/ into the Gradle project's app/libs/, and Gradle
automatically includes every jar there, packaging them into the APK; the
service process loads these classes at runtime:

```
<prebuildCopies>
    <copyFile src="$S(PluginDir)/fgs-android.jar"
              dst="$S(BuildDir)/libs/fgs-android.jar" />
</prebuildCopies>
```

`$S(PluginDir)` is the directory the UPL file sits in—place the compiled jar
there; `$S(BuildDir)` is the staging directory.

These classes are reached only through JNI and the manifest, with no Java
call sites, so they must also be kept in <proguardAdditions>, or the
shrinker will consider them unused and strip them:

```
<proguardAdditions>
    <insert>
        -keep class com.sample.fgs.FgsBridge { public *; }
        -keep class com.sample.fgs.DownloadService { public *; }
        -keep class com.sample.fgs.ProgressFile { public *; }
        -keep class com.sample.fgs.FgsLogger { public *; }
    </insert>
</proguardAdditions>
```

## 2. Configure a separate process

The process boundary is enabled by one manifest attribute:

```
android:process=":downloader"
```

The leading colon creates an application-private process named
`com.sample.psunreal:downloader`. It has a different PID from the main
process and can survive after the main process terminates.

### 2.1 The service process has no Unreal

To avoid bringing Unreal's native libraries, such as `libUE4.so` or
`libUE5.so`, into the service process, service-side Java shouldn't use any
Unreal classes, and should depend only on Android `Context`, `Intent` extras,
and platform APIs. The Unreal engine runtime is loaded only through the main
process's `GameActivity`; the private `:downloader` process doesn't load
these libraries, so referencing Unreal classes doesn't work in the service
process.

### 2.2 Process startup entry points

After the main process calls `startForegroundService`, the system forks
the `:downloader` service process:

* Instantiates `Application` and calls `Application.onCreate`—this runs
  in every process, so initialization needed by the service process must
  be done again here (see 2.3).
* Creates `DownloadService` and calls `onCreate`—this is the
  service-process entry point.
* Calls back `onStartCommand` with the `Intent` constructed at startup. The
  service promotes itself to the foreground here and starts the worker (see
  3.1).

### 2.3 State exists once per process

Dex code is shared read-only, but runtime state isn't:

* `Application.attachBaseContext` and `Application.onCreate` run in every
  process that hosts application components.
* Static initializers and static fields exist independently in each process.
  Assigning a static field in the main process doesn't communicate with the
  service.
* Unreal, C++, and Activities remain in the main process.

## 3. Java implementation

This section covers the Java side of the FGS module: 3.1 and 3.2 are
`DownloadService` in the service process; 3.3 is `FgsBridge` in the main process
(the entry point C++ calls using JNI).

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
`ACTION_STOP` to the service itself using `PendingIntent.getService` to
stop it.

```
private Notification buildNotification(long progressBytes) {
    int progressMib = (int) (progressBytes / MIB);

    Intent launchIntent =
            getPackageManager().getLaunchIntentForPackage(getPackageName());
    PendingIntent contentIntent = launchIntent != null
            ? PendingIntent.getActivity(this, 0, launchIntent,
                    PendingIntent.FLAG_IMMUTABLE
                            | PendingIntent.FLAG_UPDATE_CURRENT)
            : null;

    Intent stopIntent =
            new Intent(this, DownloadService.class).setAction(ACTION_STOP);
    PendingIntent stopPendingIntent = PendingIntent.getService(this, 0,
            stopIntent,
            PendingIntent.FLAG_IMMUTABLE
                    | PendingIntent.FLAG_UPDATE_CURRENT);

    Notification.Builder builder =
            new Notification.Builder(this, CHANNEL_ID)
            .setContentTitle("Download service")
            .setContentText("Downloaded " + progressMib + " MB / " + TOTAL_MIB + " MB")
            .setSmallIcon(android.R.drawable.stat_sys_download)
            .setProgress(TOTAL_MIB, progressMib, false)
            .setOngoing(true)
            .setOnlyAlertOnce(true)
            .addAction(
                    new Notification.Action.Builder(null, "Stop", stopPendingIntent).build());

    if (contentIntent != null) {
        builder.setContentIntent(contentIntent);
    }

    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.S) {
        builder.setForegroundServiceBehavior(Notification.FOREGROUND_SERVICE_IMMEDIATE);
    }
    return builder.build();
}
```

### 3.3 Java host entry point

FgsBridge is the Java entry point the main process uses to control the FGS
(it runs in the main process, not the service process). C++ calls these
static methods using JNI to start and stop the service and handle
notification permission:

```
public class FgsBridge {
    // Start the :downloader perceptible service and begin downloading
    public static void startDownloadService(Context context) {
        try {
            context.startForegroundService(
                    new Intent(context, DownloadService.class));
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

## 4. Start and control the FGS from Unreal (C++)

`PSUnrealAndroidBridge` is the C++ wrapper that calls `FgsBridge` using JNI.
Here are the three method implementations:

```
void FPSUnrealAndroidBridge::StartDownloadService()
{
    CallActivityVoid(
            GBridgeInfo.StartDownloadService, TEXT("StartDownloadService"));
}

void FPSUnrealAndroidBridge::StopDownloadService()
{
    CallActivityVoid(
            GBridgeInfo.StopDownloadService, TEXT("StopDownloadService"));
}

void FPSUnrealAndroidBridge::RequestNotificationPermission()
{
    CallActivityVoid(
            GBridgeInfo.RequestNotificationPermission, TEXT("RequestNotificationPermission"));
}
```

`CallActivityVoid` is an internal JNI helper that calls the corresponding
Java static method, using `FJavaWrapper::GameActivityThis` as the Context.
To ensure the notification appears immediately when the service process
starts, call `RequestNotificationPermission` in `BeginPlay`.






Send feedback