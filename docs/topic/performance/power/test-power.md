---
title: Test power-related issues  |  App quality  |  Android Developers
url: https://developer.android.com/topic/performance/power/test-power
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [App quality](https://developer.android.com/quality)
* [Technical quality](https://developer.android.com/quality/technical)

# Test power-related issues Stay organized with collections Save and categorize content based on your preferences.



The power management features released in Android 9 (API level 28) affect all apps running on
this version, whether the apps target this version or not. It's important to make sure your app
behaves properly on these devices.

Test your app's main use cases under a variety of conditions to see how the power management
features interact with each other. You can use [Android
Debug Bridge (`adb`)](/studio/command-line/adb) commands to turn some of the features on and off.

### Android Debug Bridge (adb) commands

You can use `adb` shell commands to test several of the power management features.

For information about using `adb` to put your device in Doze, see
[Test with Doze
and App Standby](/training/monitoring-device-state/doze-standby#testing_doze_and_app_standby).

#### App Standby Buckets

You can use `adb` to manually assign your app to an App Standby Bucket. To change an
app's bucket, first simulate unplugging the device using the following command:

```
$ adb shell dumpsys battery unplug
```

Use the following command to assign your app to a standby bucket:

```
$ adb shell am set-standby-bucket packagename active|working_set|frequent|rare
```

You can also use the preceding command to set multiple packages at once:

```
$ adb shell am set-standby-bucket package1 bucket1 package2 bucket2...
```

To check what bucket an app is in, run the following:

```
$ adb shell am get-standby-bucket packagename
```

If you don't pass a packagename parameter, the command lists the buckets for all apps.
An app can also find out its bucket at runtime by calling the new method
[`UsageStatsManager.getAppStandbyBucket()`](/reference/android/app/usage/UsageStatsManager#getAppStandbyBucket()).

#### Background restrictions

To manually apply background restrictions, run the following command:

```
$ adb shell cmd appops set packagename RUN_ANY_IN_BACKGROUND ignore
```

To remove background restrictions, run the following command:

```
$ adb shell cmd appops set packagename RUN_ANY_IN_BACKGROUND allow
```

#### Battery saver

There are several commands to test how your app behaves in low-power conditions.

**Note:** You can also use the device **Settings > Battery saver** screen to put the
device in battery saver mode.

To simulate the device being unplugged, use the following command:

```
$ adb shell dumpsys battery unplug
```

To test how the device behaves under low power conditions, use the following command:

```
$ adb shell settings put global low_power 1
```

After you finish testing, you can undo your manual device settings with the following
command:

```
$ adb shell dumpsys battery reset
```