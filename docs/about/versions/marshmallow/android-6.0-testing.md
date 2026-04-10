---
title: https://developer.android.com/about/versions/marshmallow/android-6.0-testing
url: https://developer.android.com/about/versions/marshmallow/android-6.0-testing
source: md.txt
---

Android 6.0 gives you an opportunity to ensure your apps work with the next
version of the platform. This release includes a number of APIs and behavior changes that can
impact your app, as described in the [API
Overview](https://developer.android.com/about/versions/marshmallow/android-6.0) and [Behavior Changes](https://developer.android.com/about/versions/marshmallow/android-6.0-changes). In testing
your app with this release, there are some specific system changes that you should focus on to
ensure that users have a good experience.


This guide describes the what and how to test Android 6.0 features with your app. You should
prioritize testing of these specific features, due to their high potential impact on your
app's behavior:

- [Permissions](https://developer.android.com/about/versions/marshmallow/android-6.0-testing#runtime-permissions)
- [Doze and App Standby](https://developer.android.com/about/versions/marshmallow/android-6.0-testing#doze-standby)
- [Auto Backup and Device Identifiers](https://developer.android.com/about/versions/marshmallow/android-6.0-testing#ids)

## Testing Permissions


The new [Permissions](https://developer.android.com/guide/topics/permissions/overview) model
changes the way that permissions are allocated to your app by the user. Instead of granting all
permissions during the install procedure, your app must ask the user for individual permissions
at runtime. For users this behavior provides more granular control over each app's activities, as
well as better context for understanding why the app is requesting a specific permission. Users
can grant or revoke the permissions granted to an app individually at any time. This feature of
the release is most likely to have an impact on your app's behavior and may prevent some of your
app features from working, or they may work in a degraded state.


This change affects all apps running on the new platform, even those not targeting the new
platform version. The platform provides a limited compatibility behavior for legacy apps, but you
should begin planning your app's migration to the new permissions model now, with a goal of
publishing an updated version of your app at the official platform launch.

### Test tips


Use the following test tips to help you plan and execute testing of your app with the new
permissions behavior.

- Identify your app's current permissions and the related code paths.
- Test user flows across permission-protected services and data.
- Test with various combinations of granted/revoked permission.
- Use the `adb` tool to manage permissions from the command line:
  - List permissions and status by group:

    ```text
    adb shell pm list permissions -d -g
    ```
  - Grant or revoke one or more permissions using the following syntax:  

    ```text
    adb shell pm [grant|revoke] <permission.name> ...
    ```
- Analyze your app for services that use permissions.

### Test strategy


The permissions change affects the structure and design of your app, as well as
the user experience and flows you provide to users. You should assess your app's current
permissions use and start planning for the new flows you want to offer. The official release of
the platform provides compatibility behavior, but you should plan on updating your app and not
rely on these behaviors.


Identify the permissions that your app actually needs and uses, and then find the various code
paths that use the permission-protected services. You can do this through a combination of
testing on the new platform and code analysis. In testing, you should focus on opting in to
runtime permissions by changing the app's `targetSdkVersion` to API level 23.


Test with various combinations of permissions revoked and added, to highlight the user flows that
depend on permissions. Where a dependency is not obvious or logical you should consider
refactoring or compartmentalizing that flow to eliminate the dependency or make it clear why the
permission is needed.


For more information on the behavior of runtime permissions, testing, and best practices, see
[Working with System Permissions](https://developer.android.com/training/permissions) developer.

## Testing Doze and App Standby


The power saving features of Doze and App Standby limit the amount of background processing that
your app can perform when a device is in an idle state or while your app is not in focus. The
restrictions the system may impose on apps include limited or no network access,
suspended background tasks, suspended Notifications, ignored wake requests, and alarms. To ensure
that your app behaves properly with these power saving optimizations, you should test your app by
simulating these low power states.

#### Testing your app with Doze

To test Doze with your app:

1. Configure a hardware device or virtual device with an Android 7.0 (API level 24) system image.
2. Connect the device to your development machine and install your app.
3. Run your app and leave it active.
4. Simulate the device going into Doze mode by running the following commands:

   ```bash
   $ adb shell dumpsys battery unplug
   $ adb shell dumpsys deviceidle step
   $ adb shell dumpsys deviceidle -h
   ```
5. Observe the behavior of your app when the device is re-activated. Make sure it recovers gracefully when the device exits Doze.

#### Testing apps with App Standby

To test the App Standby mode with your app:

1. Configure a hardware device or virtual device with an Android 7.0 (API level 24) system image.
2. Connect the device to your development machine and install your app.
3. Run your app and leave it active.
4. Simulate the app going into standby mode by running the following commands:

   ```bash
   $ adb shell am broadcast -a android.os.action.DISCHARGING
   $ adb shell am set-idle <packageName> true
   ```
5. Simulate waking your app using the following command:

   ```bash
   $ adb shell am set-idle <packageName> false
   ```
6. Observe the behavior of your app when it is woken. Make sure it recovers gracefully from standby mode. In particular, you should check if your app's Notifications and background jobs continue to function as expected.

## Auto Backup for Apps and Device-Specific Identifiers

If your app is persisting any device-specific identifiers, such as Google
Cloud Messaging registration ID, in internal storage,
make sure to follow best practices to exclude the storage
location from auto-backup, as described in [Back Up User
Data with Auto Backup](https://developer.android.com/guide/topics/data/autobackup).