---
title: https://developer.android.com/about/versions/14/changes/fgs-types-required
url: https://developer.android.com/about/versions/14/changes/fgs-types-required
source: md.txt
---

# Foreground service types are required

To help developers be more intentional with defining user-facing[foreground services](https://developer.android.com/guide/components/foreground-services), Android 10 introduced the`android:foregroundServiceType`attribute within the[`<service>`](https://developer.android.com/guide/topics/manifest/service-element)element.

If your app targets Android 14, it must specify appropriate foreground service types. As in previous versions of Android, multiple types can be combined. This list shows the foreground service types to choose from:

- [`camera`](https://developer.android.com/about/versions/14/changes/fgs-types-required#camera)
- [`connectedDevice`](https://developer.android.com/about/versions/14/changes/fgs-types-required#connected-device)
- [`dataSync`](https://developer.android.com/about/versions/14/changes/fgs-types-required#data-sync)
- [`health`](https://developer.android.com/about/versions/14/changes/fgs-types-required#health)
- [`location`](https://developer.android.com/about/versions/14/changes/fgs-types-required#location)
- [`mediaPlayback`](https://developer.android.com/about/versions/14/changes/fgs-types-required#media)
- [`mediaProjection`](https://developer.android.com/about/versions/14/changes/fgs-types-required#media-projection)
- [`microphone`](https://developer.android.com/about/versions/14/changes/fgs-types-required#microphone)
- [`phoneCall`](https://developer.android.com/about/versions/14/changes/fgs-types-required#phone-call)
- [`remoteMessaging`](https://developer.android.com/about/versions/14/changes/fgs-types-required#remote-messaging)
- [`shortService`](https://developer.android.com/about/versions/14/changes/fgs-types-required#short-service)
- [`specialUse`](https://developer.android.com/about/versions/14/changes/fgs-types-required#special-use)
- [`systemExempted`](https://developer.android.com/about/versions/14/changes/fgs-types-required#system-exempted)

If a use case in your app isn't associated with any of these types, we strongly recommend that you migrate your logic to use[WorkManager](https://developer.android.com/topic/libraries/architecture/workmanager)or[user-initiated data transfer jobs](https://developer.android.com/develop/background-work/background-tasks/uidt).

The`health, remoteMessaging, shortService, specialUse`, and`systemExempted`types are new in Android 14.

The following code snippet provides an example of a foreground service type declaration in the manifest:  

    <manifest ...>
      <uses-permission android:name="android.permission.FOREGROUND_SERVICE" />
      <uses-permission android:name="android.permission.FOREGROUND_SERVICE_MEDIA_PLAYBACK" />
        <application ...>
          <service
              android:name=".MyMediaPlaybackService"
              android:foregroundServiceType="mediaPlayback"
              android:exported="false">
          </service>
        </application>
    </manifest>

If an app that targets Android 14 doesn't define types for a given service in the manifest, then the system will raise`MissingForegroundServiceTypeException`upon calling[`startForeground()`](https://developer.android.com/reference/android/app/Service#startForeground(int,%20android.app.Notification))for that service.

## Declare new permission to use foreground service types

If apps that target Android 14 use a foreground service, they must declare a specific permission, based on the foreground service type, that Android 14 introduces. These permissions appear in the sections labeled "permission that you must declare in your manifest file" in the[intended use cases and enforcement for each foreground service type](https://developer.android.com/about/versions/14/changes/fgs-types-required#use-cases)section on this page.

All of the permissions are defined as[normal permissions](https://developer.android.com/guide/topics/permissions/overview#install-time)and are granted by default. Users cannot revoke these permissions.
| **Caution:** If you call[`startForeground()`](https://developer.android.com/reference/android/app/Service#startForeground(int,%20android.app.Notification))without declaring the appropriate foreground service type permission, the system throws a[`SecurityException`](https://developer.android.com/reference/java/lang/SecurityException).

### Include foreground service type at runtime

The best practice for applications starting foreground services is to use the`ServiceCompat`version of[`startForeground()`](https://developer.android.com/reference/androidx/core/app/ServiceCompat#startForeground(android.app.Service,int,android.app.Notification,int))(available in androidx-core 1.12 and higher) where you pass in a bitwise integer of foreground service types. You can choose to pass one or more type values.

Usually, you should declare only the types required for a particular use case. This makes it easier to meet the[system's expectations for each foreground service type](https://developer.android.com/guide/components/foreground-services#fgs-prerequisites). In cases where a foreground service is started with multiple types, then the foreground service must adhere to the[platform enforcement requirements](https://developer.android.com/guide/components/foreground-services#runtime-permissions)of**all**types.  

    ServiceCompat.startForeground(0, notification, FOREGROUND_SERVICE_TYPE_LOCATION)

If the foreground service type is not specified in the call, the type defaults to the values defined in the manifest. If you didn't specify the service type in the manifest, the system throws[`MissingForegroundServiceTypeException`](https://developer.android.com/reference/android/app/MissingForegroundServiceTypeException).

If the foreground service needs new permissions after you launch it, you should call`startForeground()`again and add the new service types. For example, suppose a fitness app runs a running-tracker service that always needs`location`information, but might or might not need`media`permissions. You would need to declare both`location`and`mediaPlayback`in the manifest. If a user starts a run and just wants their location tracked, your app should call`startForeground()`and pass just the`location`service type. Then, if the user wants to start playing audio, call`startForeground()`again and pass`location|mediaPlayback`.

## System runtime checks

The system checks for proper use of foreground service types and confirms that the app has requested the proper runtime permissions or uses the required APIs. For instance, the system expects apps that use the foreground service type[`FOREGROUND_SERVICE_TYPE_LOCATION`](https://developer.android.com/reference/android/content/pm/ServiceInfo#FOREGROUND_SERVICE_TYPE_LOCATION)type to request either`ACCESS_COARSE_LOCATION`or`ACCESS_FINE_LOCATION`.

This implies that apps must follow a very specific order of operations when requesting permissions from the user and starting foreground services. Permissions must be requested and granted*before* the app attempts to call`startForeground()`. Apps that request the appropriate permissions after the foreground service has been started must change this order of operations and request the permission before starting the foreground service.
| **Caution:** If your app doesn't fulfill all of the runtime requirements for starting a foreground service, the system throws a[`SecurityException`](https://developer.android.com/reference/java/lang/SecurityException)after you call`startForeground()`for that service. This prevents the foreground service from starting, might cause a running foreground service to be removed from the foreground process state, and might cause your app to crash.

The specifics of platform enforcement appear in the sections labeled "runtime requirements" in the[intended use cases and enforcement for each foreground service type](https://developer.android.com/about/versions/14/changes/fgs-types-required#use-cases)section on this page.

## Intended use cases and enforcement for each foreground service type

In order to use a given foreground service type, you must declare a particular permission in your manifest file, you must fulfill specific runtime requirements, and your app must fulfill one of the intended sets of use cases for that type. The following sections explain the permission that you must declare, the runtime prerequisites, and the intended use cases for each type.

### Camera

Foreground service type to declare in manifest under`android:foregroundServiceType`
:   `camera`

Permission to declare in your manifest
:   [`FOREGROUND_SERVICE_CAMERA`](https://developer.android.com/reference/android/Manifest.permission#FOREGROUND_SERVICE_CAMERA)

Constant to pass to`startForeground()`
:   [`FOREGROUND_SERVICE_TYPE_CAMERA`](https://developer.android.com/reference/android/content/pm/ServiceInfo#FOREGROUND_SERVICE_TYPE_CAMERA)

Runtime prerequisites

:   Request and be granted the[`CAMERA`](https://developer.android.com/reference/android/Manifest.permission#CAMERA)runtime permission

    **Note:** The`CAMERA`runtime permission is subject to while-in-use restrictions. For this reason, you cannot create a`camera`foreground service while your app is in the background,[with a few exceptions](https://developer.android.com/develop/background-work/services/fgs/restrictions-bg-start#wiu-restrictions-exemptions). For more information, see[Restrictions on starting foreground services that need while-in-use permissions](https://developer.android.com/develop/background-work/services/fgs/restrictions-bg-start#wiu-restrictions).

Description

:   Continue to access the camera from the background, such as video chat apps that allow for multitasking.

### Connected device

Foreground service type to declare in manifest under
`android:foregroundServiceType`
:   `connectedDevice`

Permission to declare in your manifest
:   [`FOREGROUND_SERVICE_CONNECTED_DEVICE`](https://developer.android.com/reference/android/Manifest.permission#FOREGROUND_SERVICE_CONNECTED_DEVICE)

Constant to pass to`startForeground()`
:   [`FOREGROUND_SERVICE_TYPE_CONNECTED_DEVICE`](https://developer.android.com/reference/android/content/pm/ServiceInfo#FOREGROUND_SERVICE_TYPE_CONNECTED_DEVICE)

Runtime prerequisites

:   At least one of the following conditions must be true:

    - Declare at least one of the following permissions in your manifest:

      - [`CHANGE_NETWORK_STATE`](https://developer.android.com/reference/android/Manifest.permission#CHANGE_NETWORK_STATE)
      - [`CHANGE_WIFI_STATE`](https://developer.android.com/reference/android/Manifest.permission#CHANGE_WIFI_STATE)
      - [`CHANGE_WIFI_MULTICAST_STATE`](https://developer.android.com/reference/android/Manifest.permission#CHANGE_WIFI_MULTICAST_STATE)
      - [`NFC`](https://developer.android.com/reference/android/Manifest.permission#NFC)
      - [`TRANSMIT_IR`](https://developer.android.com/reference/android/Manifest.permission#TRANSMIT_IR)
    - Request and be granted at least one of the following runtime permissions:

      - [`BLUETOOTH_CONNECT`](https://developer.android.com/reference/android/Manifest.permission#BLUETOOTH_CONNECT)
      - [`BLUETOOTH_ADVERTISE`](https://developer.android.com/reference/android/Manifest.permission#BLUETOOTH_ADVERTISE)
      - [`BLUETOOTH_SCAN`](https://developer.android.com/reference/android/Manifest.permission#BLUETOOTH_SCAN)
      - [`UWB_RANGING`](https://developer.android.com/reference/android/Manifest.permission#UWB_RANGING)
    - Call[`UsbManager.requestPermission()`](https://developer.android.com/reference/android/hardware/usb/UsbManager#requestPermission(android.hardware.usb.UsbDevice,%20android.app.PendingIntent))

Description

:   Interactions with external devices that require a Bluetooth, NFC, IR, USB, or network connection.

    | **Note:** If your app performs a projection or remote messaging operation, use the corresponding[media projection](https://developer.android.com/about/versions/14/changes/fgs-types-required#media-projection)or[remote messaging](https://developer.android.com/about/versions/14/changes/fgs-types-required#remote-messaging)type instead.

Alternatives

:   If your app needs to do continuous data transfer to an external device, consider using the[companion device manager](https://developer.android.com/guide/topics/connectivity/companion-device-pairing)instead. Use the[companion device presence API](https://developer.android.com/guide/topics/connectivity/companion-device-pairing#keep-awake)to help your app stay running while the companion device is in range.

:   If your app needs to scan for bluetooth devices, consider using the[Bluetooth scan API](https://developer.android.com/guide/topics/connectivity/bluetooth/find-ble-devices)instead.

### Data sync

Foreground service type to declare in manifest under
`android:foregroundServiceType`
:   `dataSync`

Permission to declare in your manifest
:   [`FOREGROUND_SERVICE_DATA_SYNC`](https://developer.android.com/reference/android/Manifest.permission#FOREGROUND_SERVICE_DATA_SYNC)

Constant to pass to`startForeground()`
:   [`FOREGROUND_SERVICE_TYPE_DATA_SYNC`](https://developer.android.com/reference/android/content/pm/ServiceInfo#FOREGROUND_SERVICE_TYPE_DATA_SYNC)

Runtime prerequisites
:   None

Description

:   Data transfer operations, such as the following:

    - Data upload or download
    - Backup-and-restore operations
    - Import or export operations
    - Fetch data
    - Local file processing
    - Transfer data between a device and the cloud over a network

Alternatives

:   See[Alternatives to data sync foreground services](https://developer.android.com/about/versions/15/changes/datasync-migration)for detailed information.

### Health

Foreground service type to declare in manifest under
`android:foregroundServiceType`
:   `health`

Permission to declare in your manifest
:   [`FOREGROUND_SERVICE_HEALTH`](https://developer.android.com/reference/android/Manifest.permission#FOREGROUND_SERVICE_HEALTH)

Constant to pass to`startForeground()`
:   [`FOREGROUND_SERVICE_TYPE_HEALTH`](https://developer.android.com/reference/android/content/pm/ServiceInfo#FOREGROUND_SERVICE_TYPE_HEALTH)

Runtime prerequisites

:   At least one of the following conditions must be true:

    - Declare the[`HIGH_SAMPLING_RATE_SENSORS`](https://developer.android.com/reference/android/Manifest.permission#HIGH_SAMPLING_RATE_SENSORS)permission in your manifest.

    - Request and be granted at least one of the following runtime permissions:

      - [`BODY_SENSORS`](https://developer.android.com/reference/android/Manifest.permission#BODY_SENSORS)on API level 35 and lower
      - [`READ_HEART_RATE`](https://developer.android.com/reference/android/health/connect/HealthPermissions#READ_HEART_RATE)
      - [`READ_SKIN_TEMPERATURE`](https://developer.android.com/reference/android/health/connect/HealthPermissions#READ_SKIN_TEMPERATURE)
      - [`READ_OXYGEN_SATURATION`](https://developer.android.com/reference/android/health/connect/HealthPermissions#READ_OXYGEN_SATURATION)
      - [`ACTIVITY_RECOGNITION`](https://developer.android.com/reference/android/Manifest.permission#ACTIVITY_RECOGNITION)

    **Note:** The`BODY_SENSORS`and sensor-based READ runtime permissions are subject to while-in-use restrictions. For this reason, you cannot create a`health`foreground service that uses body sensors while your app is in the background unless you've been granted the[`BODY_SENSORS_BACKGROUND`](https://developer.android.com/reference/android/Manifest.permission#BODY_SENSORS_BACKGROUND)(API level 33 to 35) or[`READ_HEALTH_DATA_IN_BACKGROUND`](https://developer.android.com/reference/android/health/connect/HealthPermissions#READ_HEALTH_DATA_IN_BACKGROUND)(API level 36 and higher) permissions. For more information, see[Restrictions on starting foreground services that need while-in-use permissions](https://developer.android.com/develop/background-work/services/fgs/restrictions-bg-start#wiu-restrictions).

Description

:   Any long-running use cases to support apps in the fitness category such as exercise trackers.

### Location

Foreground service type to declare in manifest under
`android:foregroundServiceType`
:   `location`

Permission to declare in your manifest
:   [`FOREGROUND_SERVICE_LOCATION`](https://developer.android.com/reference/android/Manifest.permission#FOREGROUND_SERVICE_LOCATION)

Constant to pass to`startForeground()`
:   [`FOREGROUND_SERVICE_TYPE_LOCATION`](https://developer.android.com/reference/android/content/pm/ServiceInfo#FOREGROUND_SERVICE_TYPE_LOCATION)

Runtime prerequisites

:   The user must have enabled location services and the app must be granted at least one of the following runtime permissions:

    - [`ACCESS_COARSE_LOCATION`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_COARSE_LOCATION)
    - [`ACCESS_FINE_LOCATION`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_FINE_LOCATION)

    **Note:** In order to check that the user has enabled location services as well as granted access to the runtime permissions, use[`PermissionChecker#checkSelfPermission()`](https://developer.android.com/reference/androidx/core/content/PermissionChecker#checkSelfPermission(android.content.Context,java.lang.String))

    **Note:** The location runtime permissions are subject to while-in-use restrictions. For this reason, you cannot create a`location`foreground service while your app is in the background, unless you've been granted the[`ACCESS_BACKGROUND_LOCATION`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_BACKGROUND_LOCATION)runtime permission. For more information, see[Restrictions on starting foreground services that need while-in-use permissions](https://developer.android.com/guide/components/foreground-services#wiu-restrictions).

Description

:   Long-running use cases that require location access, such as navigation and location sharing.

Alternatives

:   If your app needs to be triggered when the user reaches specific locations, consider using the[geofence API](https://developer.android.com/training/location/geofencing)instead.

### Media

Foreground service type to declare in manifest under
`android:foregroundServiceType`
:   `mediaPlayback`

Permission to declare in your manifest
:   [`FOREGROUND_SERVICE_MEDIA_PLAYBACK`](https://developer.android.com/reference/android/Manifest.permission#FOREGROUND_SERVICE_MEDIA_PLAYBACK)

Constant to pass to`startForeground()`
:   [`FOREGROUND_SERVICE_TYPE_MEDIA_PLAYBACK`](https://developer.android.com/reference/android/content/pm/ServiceInfo#FOREGROUND_SERVICE_TYPE_MEDIA_PLAYBACK)

Runtime prerequisites
:   None

Description
:   Continue audio or video playback from the background. Support Digital Video Recording (DVR) functionality on[Android TV](https://developer.android.com/training/tv/tif/content-recording).

Alternatives
:   If you're showing picture-in-picture video, use[Picture-in-Picture mode](https://developer.android.com/develop/ui/views/picture-in-picture).

### Media projection

Foreground service type to declare in manifest under
`android:foregroundServiceType`
:   `mediaProjection`

Permission to declare in your manifest
:   [`FOREGROUND_SERVICE_MEDIA_PROJECTION`](https://developer.android.com/reference/android/Manifest.permission#FOREGROUND_SERVICE_MEDIA_PROJECTION)

Constant to pass to`startForeground()`
:   [`FOREGROUND_SERVICE_TYPE_MEDIA_PROJECTION`](https://developer.android.com/reference/android/content/pm/ServiceInfo#FOREGROUND_SERVICE_TYPE_MEDIA_PROJECTION)

Runtime prerequisites

:   Call the[`createScreenCaptureIntent()`](https://developer.android.com/reference/android/media/projection/MediaProjectionManager#createScreenCaptureIntent(android.media.projection.MediaProjectionConfig))method before starting the foreground service. Doing so shows a permission notification to the user; the user must grant the permission before you can create the service.

:   After you have created the foreground service, you can call[`MediaProjectionManager.getMediaProjection()`](https://developer.android.com/reference/android/media/projection/MediaProjectionManager#getMediaProjection(int,%20android.content.Intent)).

Description

:   Project content to non-primary display or external device using the[`MediaProjection`](https://developer.android.com/reference/android/media/projection/MediaProjection)APIs. This content doesn't have to be exclusively media content.

Alternatives

:   To stream media to another device, use the[Google Cast SDK](https://developers.google.com/cast/docs/android_sender).

### Microphone

Foreground service type to declare in manifest under
`android:foregroundServiceType`
:   `microphone`

Permission to declare in your manifest
:   [`FOREGROUND_SERVICE_MICROPHONE`](https://developer.android.com/reference/android/Manifest.permission#FOREGROUND_SERVICE_MICROPHONE)

Constant to pass to`startForeground()`
:   [`FOREGROUND_SERVICE_TYPE_MICROPHONE`](https://developer.android.com/reference/android/content/pm/ServiceInfo#FOREGROUND_SERVICE_TYPE_MICROPHONE)

Runtime prerequisites

:   Request and be granted the[`RECORD_AUDIO`](https://developer.android.com/reference/android/Manifest.permission#RECORD_AUDIO)runtime permission.

    **Note:** The`RECORD_AUDIO`runtime permission is subject to while-in-use restrictions. For this reason, you cannot create a`microphone`foreground service while your app is in the background,[with a few exceptions](https://developer.android.com/develop/background-work/services/fgs/restrictions-bg-start#wiu-restrictions-exemptions). For more information, see[Restrictions on starting foreground services that need while-in-use permissions](https://developer.android.com/develop/background-work/services/fgs/restrictions-bg-start#wiu-restrictions).

Description

:   Continue microphone capture from the background, such as voice recorders or communication apps.

### Phone call

Foreground service type to declare in manifest under
`android:foregroundServiceType`
:   `phoneCall`

Permission to declare in your manifest
:   [`FOREGROUND_SERVICE_PHONE_CALL`](https://developer.android.com/reference/android/Manifest.permission#FOREGROUND_SERVICE_PHONE_CALL)

Constant to pass to`startForeground()`
:   [`FOREGROUND_SERVICE_TYPE_PHONE_CALL`](https://developer.android.com/reference/android/content/pm/ServiceInfo#FOREGROUND_SERVICE_TYPE_PHONE_CALL)

Runtime prerequisites

:   At least one of these conditions must be true:

:
    - App has declared the[`MANAGE_OWN_CALLS`](https://developer.android.com/reference/android/Manifest.permission#MANAGE_OWN_CALLS)permission in its manifest file.
:
    - App is the default dialer app through the[`ROLE_DIALER`](https://developer.android.com/reference/android/app/role/RoleManager#ROLE_DIALER)role.

Description

:   Continue an ongoing call using the[`ConnectionService`](https://developer.android.com/reference/android/telecom/ConnectionService)APIs.

Alternatives

:   If you need to make phone, video, or VoIP calls, consider using the[`android.telecom`](https://developer.android.com/reference/android/telecom/package-summary)library.

:   Consider using[`CallScreeningService`](https://developer.android.com/reference/android/telecom/CallScreeningService)to screen calls.

### Remote messaging

Foreground service type to declare in manifest under
`android:foregroundServiceType`
:   `remoteMessaging`

Permission to declare in your manifest
:   [`FOREGROUND_SERVICE_REMOTE_MESSAGING`](https://developer.android.com/reference/android/Manifest.permission#FOREGROUND_SERVICE_REMOTE_MESSAGING)

Constant to pass to`startForeground()`
:   [`FOREGROUND_SERVICE_TYPE_REMOTE_MESSAGING`](https://developer.android.com/reference/android/content/pm/ServiceInfo#FOREGROUND_SERVICE_TYPE_REMOTE_MESSAGING)

Runtime prerequisites
:   None

Description
:   Transfer text messages from one device to another. Assists with continuity of a user's messaging tasks when they switch devices.

### Short service

Foreground service type to declare in manifest under
`android:foregroundServiceType`
:   `shortService`

Permission to declare in your manifest
:   None

Constant to pass to`startForeground()`
:   [`FOREGROUND_SERVICE_TYPE_SHORT_SERVICE`](https://developer.android.com/reference/android/content/pm/ServiceInfo#FOREGROUND_SERVICE_TYPE_SHORT_SERVICE)

Runtime prerequisites
:   None

Description

:   Quickly finish critical work that cannot be interrupted or postponed.

    This type has some unique characteristics:

    - Can only run for a short period of time (about 3 minutes).
    - No support for[sticky](https://developer.android.com/reference/android/app/Service#START_STICKY)foreground services.
    - Cannot start other foreground services.
    - Doesn't require a[type-specific permission](https://developer.android.com/about/versions/14/changes/fgs-types-required#permission-for-fgs-type), though it still requires the[`FOREGROUND_SERVICE`](https://developer.android.com/reference/android/Manifest.permission#FOREGROUND_SERVICE)permission.
    - A`shortService`can only change to another service type if the app is currently eligible to start a new foreground service.
    - A foreground service can change its type to`shortService`at any time, at which point the timeout period begins.

    The timeout for shortService begins from the moment that[`Service.startForeground()`](https://developer.android.com/reference/android/app/Service#startForeground(int,%20android.app.Notification,%20int))is called. The app is expected to call[`Service.stopSelf()`](https://developer.android.com/reference/android/app/Service#stopSelf())or[`Service.stopForeground()`](https://developer.android.com/reference/android/app/Service#stopForeground(int))before the timeout occurs. Otherwise, the new`Service.onTimeout()`is called, giving apps a brief opportunity to call`stopSelf()`or`stopForeground()`to stop their service.

    A short time after`Service.onTimeout()`is called, the app enters a[cached state](https://developer.android.com/guide/components/activities/process-lifecycle)and is no longer considered to be in the foreground, unless the user is actively interacting with the app. A short time after the app is cached and the service has not stopped, the app receives an[ANR](https://developer.android.com/topic/performance/vitals/anr). The ANR message mentions`FOREGROUND_SERVICE_TYPE_SHORT_SERVICE`. For these reasons, it's considered best practice to implement the`Service.onTimeout()`callback.

    The`Service.onTimeout()`callback doesn't exist on Android 13 and lower. If the same service runs on such devices, it doesn't receive a timeout, nor does it ANR. Make sure that your service stops as soon as it finishes the processing task, even if it hasn't received the`Service.onTimeout()`callback yet.

    It's important to note that if the timeout of the`shortService`is not respected, the app will ANR even if it has other valid foreground services or other app lifecycle processes running.

    If an app is visible to the user or satisfies one of the[exemptions](https://developer.android.com/guide/components/foreground-services#background-start-restriction-exemptions)that allow foreground services to be started from the background, calling`Service.StartForeground()`again with the`FOREGROUND_SERVICE_TYPE_SHORT_SERVICE`parameter extends the timeout by another 3 minutes. If the app isn't visible to the user and doesn't satisfy one of the[exemptions](https://developer.android.com/guide/components/foreground-services#background-start-restriction-exemptions), any attempt to start another foreground service, regardless of type, causes a[`ForegroundServiceStartNotAllowedException`](https://developer.android.com/reference/android/app/ForegroundServiceStartNotAllowedException).

    If a user disables[battery optimization](https://support.google.com/pixelphone/answer/7015477)for your app, it's still affected by the timeout of shortService FGS.

    If you start a foreground service that includes the`shortService`type and another foreground service type, the system ignores the`shortService`type declaration. However, the service must still adhere to the prerequisites of the other declared types. For more information, see the[Foreground services documentation](https://developer.android.com/guide/components/foreground-services).

### Special use

Foreground service type to declare in manifest under
`android:foregroundServiceType`
:   `specialUse`

Permission to declare in your manifest
:   [`FOREGROUND_SERVICE_SPECIAL_USE`](https://developer.android.com/reference/android/Manifest.permission#FOREGROUND_SERVICE_SPECIAL_USE)

Constant to pass to`startForeground()`
:   [`FOREGROUND_SERVICE_TYPE_SPECIAL_USE`](https://developer.android.com/reference/android/content/pm/ServiceInfo#FOREGROUND_SERVICE_TYPE_SPECIAL_USE)

Runtime prerequisites
:   None

Description

:   Covers any valid foreground service use cases that aren't covered by the other foreground service types.

    In addition to declaring the`FOREGROUND_SERVICE_TYPE_SPECIAL_USE`foreground service type, developers should declare use cases in the manifest. To do so, they specify the`<property>`element within the[`<service>`](https://developer.android.com/guide/topics/manifest/service-element)element. These values and corresponding use cases are reviewed when you submit your app in the Google Play Console. The use cases you provide are free-form, and you should make sure to provide enough information to let the reviewer see why you need to use the`specialUse`type.  

        <service android:name="fooService" android:foregroundServiceType="specialUse">
          <property android:name="android.app.PROPERTY_SPECIAL_USE_FGS_SUBTYPE"
              android:value="explanation_for_special_use"/>
        </service>

### System exempted

Foreground service type to declare in manifest under
`android:foregroundServiceType`
:   `systemExempted`

Permission to declare in your manifest
:   [`FOREGROUND_SERVICE_SYSTEM_EXEMPTED`](https://developer.android.com/reference/android/Manifest.permission#FOREGROUND_SERVICE_SYSTEM_EXEMPTED)

Constant to pass to`startForeground()`
:   [`FOREGROUND_SERVICE_TYPE_SYSTEM_EXEMPTED`](https://developer.android.com/reference/android/content/pm/ServiceInfo#FOREGROUND_SERVICE_TYPE_SYSTEM_EXEMPTED)

Runtime prerequisites
:   None

Description

:   Reserved for system applications and specific system integrations, to continue to use foreground services.

    To use this type, an app must meet at least one of the following criteria:

- Device is in demo mode state
- App is a[Device Owner](https://source.android.com/devices/tech/admin/provision)
- App is a[Profiler Owner](https://source.android.com/devices/tech/admin/managed-profiles)
- Safety Apps that have the[`ROLE_EMERGENCY`](https://developer.android.com/reference/android/app/role/RoleManager#ROLE_EMERGENCY)role
- [Device Admin](https://developer.android.com/work/device-admin)apps
- Apps holding[`SCHEDULE_EXACT_ALARM`](https://developer.android.com/reference/android/Manifest.permission#SCHEDULE_EXACT_ALARM)or[`USE_EXACT_ALARM`](https://developer.android.com/reference/android/Manifest.permission#USE_EXACT_ALARM)permission and are using Foreground Service to continue alarms in the background, including haptics-only alarms.
- VPN apps (configured using**Settings \> Network \& Internet \> VPN**)

  Otherwise, declaring this type causes the system to throw a`ForegroundServiceTypeNotAllowedException`.

## Google Play policy enforcement for using foreground service types

If your app targets Android 14 or higher, you'll need to declare your app's foreground service types in the Play Console's app content page (**Policy \> App content** ). For more information on how to declare your foreground service types in Play Console, see[Understanding foreground service and full-screen intent requirements](https://support.google.com/googleplay/android-developer/answer/13392821).