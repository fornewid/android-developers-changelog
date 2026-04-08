---
title: https://developer.android.com/work/managed-profiles
url: https://developer.android.com/work/managed-profiles
source: md.txt
---

# Work profiles

The Android platform allows devices to have[work profiles](https://developer.android.com/about/versions/lollipop/android-5.0#Enterprise)(sometimes referred to as managed profiles). A work profile is controlled by an IT admin, and the functionality available to it is set separately from the functionality of the user's primary profile. This approach lets organizations control the environment where company-specific apps and data are running on a user's device, while still letting users use their personal apps and profiles.

This lesson shows you how to modify your application so it functions reliably on a device with a work profile. You don't need to do anything besides the ordinary app-development best practices. However, some of these best practices become especially important on devices with work profiles. This document highlights the issues you need to be aware of.

## Overview

Users often want to use their personal devices in an enterprise setting. This situation can present organizations with a dilemma. If the user can use their own device, the organization has to worry that confidential information (like employee emails and contacts) are on a device the organization does not control.

To address this situation, Android 5.0 (API level 21) allows organizations to set up*work profiles*. If a device has a work profile, the profile's settings are under the control of the IT admin. The IT admin can choose which apps are allowed for that profile, and can control just what device features are available to the profile.

If a device has a work profile, there are implications for apps running on the device, no matter which profile the app is running under:

- By default, most intents do not cross from one profile to the other. If an app running on profile fires an intent, there is no handler for the intent on that profile, and the intent is not allowed to cross to the other profile due to profile restrictions, the request fails and the app may shut down unexpectedly.
- The profile IT admin can limit which system apps are available on the work profile. This restriction can also result in there being no handler for some common intents on the work profile.
- Since the personal and work profiles have separate storage areas, a file URI that is valid on one profile is not valid on the other. Any intent fired on one profile might be handled on the other (depending on profile settings), so it is not safe to attach file URIs to intents.

## Prevent failed intents

On a device with a work profile, there are restrictions on whether intents can cross from one profile to another. In most cases, when an intent is fired off, it is handled on the same profile where it is fired. If there is no handler for the intent*on that profile*, the intent is not handled and the app that fired it may shut down unexpectedly---even if there's a handler for the intent on the other profile.

The profile admin can choose which intents are allowed to cross from one profile to another. Since the IT admin makes this decision, there's no way for you to know in advance*which*intents are allowed to cross this boundary. The IT admin sets this policy, and is free to change it at any time.

Before your app starts an activity, you should verify that there is a suitable resolution. You can verify that there is an acceptable resolution by calling[Intent.resolveActivity()](https://developer.android.com/reference/android/content/Intent#resolveActivity(android.content.pm.PackageManager)). If there is no way to resolve the intent, the method returns`null`. If the method returns non-null, there is at least one way to resolve the intent, and it is safe to fire off the intent. In this case, the intent could be resolvable either because there is a handler on the current profile, or because the intent is allowed to cross to a handler on the other profile. (For more information about resolving intents, see[Common Intents](https://developer.android.com/guide/components/intents-common).)

For example, if your app needs to set timers, it would need to check that there's a valid handler for the[ACTION_SET_TIMER](https://developer.android.com/reference/android/provider/AlarmClock#ACTION_SET_TIMER)intent. If the app cannot resolve the intent, it should take an appropriate action (such as showing an error message).  

### Kotlin

```kotlin
fun startTimer(message: String, seconds: Int) {

    // Build the "set timer" intent
    val timerIntent = Intent(AlarmClock.ACTION_SET_TIMER).apply {
        putExtra(AlarmClock.EXTRA_MESSAGE, message)
        putExtra(AlarmClock.EXTRA_LENGTH, seconds)
        putExtra(AlarmClock.EXTRA_SKIP_UI, true)
    }

    // Check if there's a handler for the intent
    if (timerIntent.resolveActivity(packageManager) == null) {

        // Can't resolve the intent! Fail this operation cleanly
        // (perhaps by showing an error message)

    } else {
        // Intent resolves, it's safe to fire it off
        startActivity(timerIntent)

    }
}
```

### Java

```java
public void startTimer(String message, int seconds) {

    // Build the "set timer" intent
    Intent timerIntent = new Intent(AlarmClock.ACTION_SET_TIMER)
            .putExtra(AlarmClock.EXTRA_MESSAGE, message)
            .putExtra(AlarmClock.EXTRA_LENGTH, seconds)
            .putExtra(AlarmClock.EXTRA_SKIP_UI, true);

    // Check if there's a handler for the intent
    if (timerIntent.resolveActivity(getPackageManager()) == null) {

        // Can't resolve the intent! Fail this operation cleanly
        // (perhaps by showing an error message)

    } else {
        // Intent resolves, it's safe to fire it off
        startActivity(timerIntent);

    }
}
```

## Share files across profiles

Sometimes an app needs to provide other apps with access to its own files. For example, an image gallery app might want to share its images with image editors. There are two ways you would ordinarily share a file: with a*file URI* or a*content URI*.

A file URI begins with the`file:`prefix, followed by the absolute path of the file on the device's storage. However, because the work profile and the personal profile use separate storage areas, a file URI that is valid on one profile is not valid on the other. This situation means that if you attach a file URI to an intent, and the intent is handled on the other profile, the handler is not able to access the file.

Instead, you should share files with*content URIs* . Content URIs identify the file in a more secure, shareable fashion. The content URI contains the file path, but also the authority that provides the file, and an ID number identifying the file. You can generate a content ID for any file by using a[FileProvider](https://developer.android.com/reference/androidx/core/content/FileProvider). You can then share that content ID with other apps (even on the other profile). The recipient can use the content ID to get access to the actual file.

For example, here's how you would get the content URI for a specific file URI:  

### Kotlin

```kotlin
// Open File object from its file URI
val fileToShare = File(fileUriToShare)

val contentUriToShare: Uri = FileProvider.getUriForFile(
        context,
        "com.example.myapp.fileprovider",
        fileToShare
)
```

### Java

```java
// Open File object from its file URI
File fileToShare = new File(fileUriToShare);

Uri contentUriToShare = FileProvider.getUriForFile(getContext(),
        "com.example.myapp.fileprovider", fileToShare);
```

When you call the[getUriForFile()](https://developer.android.com/reference/androidx/core/content/FileProvider#getUriForFile(android.content.Context, java.lang.String, java.io.File))method, you must include the file provider's authority (in this example,`"com.example.myapp.fileprovider"`), which is specified in the[`<provider>`](https://developer.android.com/guide/topics/manifest/provider-element)element of your app manifest. For more information about sharing files with content URIs, see[Sharing Files](https://developer.android.com/training/secure-file-sharing).

## Listen for notifications

An app typically provides a[NotificationListenerService](https://developer.android.com/reference/android/service/notification/NotificationListenerService)subclass to receive callbacks from the system about changes to notifications. Devices with work profiles might affect how`NotificationListenerService`works with your app.

### In a work profile

You can't use a`NotificationListenerService`from an app running in the work profile. When your app is running in a work profile, the system ignores your app's`NotificationListenerService`. However, apps running in the personal profile can listen for notifications.

### In a personal profile

When your app runs in the personal profile, you might not get notifications for apps running in the work profile. By default, all personal profile apps receive callbacks but an IT admin can allowlist one or more personal profile apps that they allow to listen for notification changes. The system then blocks non-allowlisted apps. In Android 8.0 (API level 26) or later, a device policy controller (DPC) that manages a work profile might block your app from listening to the work profile's notifications using the`DevicePolicyManager`method[setPermittedCrossProfileNotificationListeners()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setPermittedCrossProfileNotificationListeners(android.content.ComponentName, java.util.List<java.lang.String>)). Your app still receives callbacks about notifications posted in the personal profile.

## Test your App for Compatibility with Work Profiles

You should test your app in a work-profile environment to catch problems that would cause your app to fail on a device with work profiles. In particular, testing on a work-profile device is a good way to make sure that your app handles intents properly: not firing intents that can't be handled, not attaching URIs that don't work cross-profile, and so on.

We have provided a sample app,[TestDPC](https://github.com/googlesamples/android-testdpc#readme), which you can use to set up a work profile on an Android device that runs Android 5.0 (API level 21) and higher. This app offers you a simple way to test your app in a work-profile environment. You can also use this app to configure the work profile as follows:

- Specify which default apps are available on the managed profile
- Configure which intents are allowed to cross from one profile to the other

If you manually install an app over a USB cable to a device which has a work profile, the app is installed on both the personal and the work profile. Once you have installed the app, you can test the app under the following conditions:

- If an intent would ordinarily be handled by a default app (for example, the camera app), try disabling that default app on the work profile, and verify that the app handles this appropriately.
- If you fire an intent expecting it to be handled by some other app, try enabling and disabling that intent's permission to cross from one profile to another. Verify that the app behaves properly under both circumstances. If the intent is not allowed to cross between profiles, verify the app's behavior both when there is a suitable handler on the app's profile, and when there is not. For example, if your app fires a map-related intent, try each of the following scenarios:
  - The device allows map intents to cross from one profile to the other, and there is a suitable handler on the other profile (the profile the app is not running on)
  - The device does not allow map intents to cross between profiles, but there is a suitable handler on the app's profile
  - The device does not allow map intents to cross between profiles, and there is no suitable handler for map intents on the device's profile
- If you attach content to an intent, verify that the intent behaves properly both when it is handled on the app's profile, and when it crosses between profiles.

### Test on work profiles: tips and tricks

There are a few tricks that you may find helpful in testing on a work-profile device.

- As noted, when you side-load an app on a work-profile device, it is installed on both profiles. If you wish, you can delete the app from one profile and leave it on the other.
- Most of the activity manager commands available in the[Android Debug Bridge](https://developer.android.com/tools/help/adb)(adb) shell support the`--user`flag, which lets you specify which user to run as. By specifying a user, you can choose whether to run as the unmanaged primary user or work profile. For more information, see[ADB Shell Commands](https://developer.android.com/tools/help/shell#am).
- To find the active users on a device, use the adb package manager's`list users`command. The first number in the output string is the user ID, which you can use with the`--user`flag. For more information, see[ADB Shell Commands](https://developer.android.com/tools/help/shell#pm).

For example, to find the users on a device, you would run this command:  

```
$ adb shell pm list users
UserInfo{0:Drew:13} running
UserInfo{10:Work profile:30} running
```

In this case, the primary user("Drew") has the user ID 0, and the work profile has the user ID 10. To run an app in the work profile, you would use a command like this:  

```
$ adb shell am start --user 10 \
-n "com.example.myapp/com.example.myapp.testactivity" \
-a android.intent.action.MAIN -c android.intent.category.LAUNCHER
```