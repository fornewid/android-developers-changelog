---
title: https://developer.android.com/about/versions/13/behavior-changes-all
url: https://developer.android.com/about/versions/13/behavior-changes-all
source: md.txt
---

The Android 13 platform includes behavior changes that may affect your app. The
following behavior changes apply to *all apps* when they run on Android 13,
regardless of `targetSdkVersion`. You should test your app and then modify it as
needed to support these properly, where applicable.

Make sure to also review the list of [behavior changes that only affect apps
targeting Android 13](https://developer.android.com/about/versions/13/behavior-changes-13).

## Performance and battery

### Task Manager

![At the bottom of the notification drawer is a button that indicates the
number of apps that are currently running in the background. When you press
this button, a dialog appears that lists the names of different apps. The
Stop button is to the right of each app](https://developer.android.com/static/images/guide/components/fgs-manager.svg) **Figure 1.** Workflow for Task Manager , which allows users to stop apps that have ongoing foreground services. This workflow appears only on devices that run Android 13 or higher.

Starting in Android 13 (API level 33), users can complete a workflow from the
notification drawer to stop apps that have ongoing foreground services, as shown
in figure 1. This affordance is known as the
*Task Manager* . Apps must be able to [handle this
user-initiated
stopping](https://developer.android.com/guide/components/foreground-services#handle-user-initiated-stop).

### Improve prefetch job handling using JobScheduler

JobScheduler provides a way for apps to mark specific jobs as "prefetch"
jobs (using [`JobInfo.Builder.setPrefetch()`](https://developer.android.com/reference/android/app/job/JobInfo.Builder#setPrefetch(boolean))), meaning that they should ideally run
close to, and before, the next app launch to improve user experience.
Historically, JobScheduler has only used the signal to let prefetch jobs
opportunistically use free or excess data.

In Android 13 (API level 33) and higher, the system tries to
determine the next time an app will be launched, and uses that estimation to run
prefetch jobs. Apps should try to use prefetch jobs for any work that they want
to be done prior to the next app launch.

### Battery Resource Utilization

Android 13 (API level 33) provides the following ways for the system to better
manage device battery life:

- Updated rules on when the system places your app in the ["restricted" App
  Standby Bucket](https://developer.android.com/topic/performance/appstandby#restricted-bucket).
- New limitations on the work that your app can do when the user places your app in the ["restricted" state](https://developer.android.com/topic/performance/background-optimization#bg-restrict) for background battery usage.

As you test your app with these changes, make sure to check the following
things:

- Test how your app responds when the system places it in the ["restricted" App
  Standby Bucket](https://developer.android.com/topic/performance/appstandby#restricted-bucket). Use the
  following Android Debug Bridge (ADB) command to assign your app to this bucket:

  ```
  adb shell am set-standby-bucket PACKAGE_NAME restricted
  ```
- Test how your app responds to the following restrictions that commonly apply
  to apps that are in a ["restricted" state](https://developer.android.com/topic/performance/background-optimization#bg-restrict)
  for background battery usage:

  - Can't launch foreground services
  - Existing foreground services are removed from the foreground
  - Alarms aren't triggered
  - Jobs aren't executed

  Use the following ADB command to place your app in this "restricted" state:

  ```
  adb shell cmd appops set PACKAGE_NAME RUN_ANY_IN_BACKGROUND ignore
  ```

### High Priority Firebase Cloud Message (FCM) Quotas

Android 13 (API level 33) updates [Firebase Cloud Messaging](https://firebase.google.com/docs/cloud-messaging) (FCM) quotas to improve the reliability of high priority FCM delivery for apps that show notifications in response to high priority FCMs. The following has changed in Android 13 (API level 33):

- [App Standby Buckets](https://developer.android.com/topic/performance/appstandby) no longer determine how many high priority FCMs an app can use.
- System now downgrades the high priority messages if it detects an app consistently sending high-priority messages that don't result in a notification.

As in previous versions of Android, high priority FCMs that go over the quota are downgraded to normal priority. When starting [Foreground Services](https://developer.android.com/guide/components/foreground-services) (FGS) in response to an FCM, we recommend checking the result of [`RemoteMessage.getPriority()`](https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage#getPriority()) and to confirm it is [`PRIORITY_HIGH`](https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage#PRIORITY_HIGH) and/or handling any potential [`ForegroundServiceStartNotAllowedException`](https://developer.android.com/reference/android/app/ForegroundServiceStartNotAllowedException) exceptions.

If your application doesn't always post notifications in response to High Priority FCMs, we recommend that you change the priority of these FCMs to **normal** so that the messages that result in a notification don't get downgraded.

## Privacy

### Runtime permission for notifications

Android 13 (API level 33) introduces a runtime
[notification permission](https://developer.android.com/guide/topics/ui/notifiers/notification-permission):
[`POST_NOTIFICATIONS`](https://developer.android.com/reference/android/Manifest.permission#POST_NOTIFICATIONS).
This change helps users focus on the notifications that are most important to
them.

> [!NOTE]
> **Note:** Notifications related to [media sessions](https://developer.android.com/guide/topics/media-apps/working-with-a-media-session) and apps that self-manage phone calls are exempt from this behavior change.

We highly recommend that you target Android 13 or higher as soon
as possible to gain the effects of the additional control and flexibility of
this feature.

Learn more about
[app permissions best practices](https://developer.android.com/training/permissions/usage-notes).

### Hide sensitive content from clipboard

If your app allows users to copy sensitive content, such as passwords or credit
card information, to the clipboard, you must add a flag to ClipData's
`ClipDescription` before calling `ClipboardManager#setPrimaryClip()`. Adding
this flag prevents sensitive content from appearing in the content preview.
![Copied text preview without flagging sensitive content](https://developer.android.com/static/images/about/versions/13/sensitive-content-before.png) Copied text preview without flagging sensitive content. ![Copied text preview flagging sensitive content.](https://developer.android.com/static/images/about/versions/13/sensitive-content-after.png) Copied text preview flagging sensitive content.

<br />

To flag sensitive content, add a boolean extra to the `ClipDescription`. All
apps should do this, regardless of the targeted API level.


    // When your app is compiled with the API level 33 SDK or higher
    clipData.apply {
        description.extras = PersistableBundle().apply {
            putBoolean(ClipDescription.EXTRA_IS_SENSITIVE, true)
        }
    }

    // If your app is compiled with a lower SDK
    clipData.apply {
        description.extras = PersistableBundle().apply {
            putBoolean("android.content.extra.IS_SENSITIVE", true)
        }
    }

To learn more about the new clipboard UI, visit the
[Copy and paste](https://developer.android.com/guide/topics/text/copy-paste#SensitiveContent) feature page.

## Security

### Migrate away from shared user ID

If your app uses the deprecated
[`android:sharedUserId`](https://developer.android.com/guide/topics/manifest/manifest-element#uid) attribute
and no longer depends on the attribute's functionality, you can set the
[`android:sharedUserMaxSdkVersion`](https://developer.android.com/guide/topics/manifest/manifest-element#uidmaxsdk)
attribute to `32`, as shown in the following code snippet:

```xml
<manifest ...>
    <!-- To maintain backward compatibility, continue to use
         "android:sharedUserId" if you already added it to your manifest. -->
    android:sharedUserId="SHARED_PACKAGE_NAME"
    android:sharedUserMaxSdkVersion="32"
    ...
</manifest>
```

This attribute tells the system that your app no longer relies on a shared
user ID. If your app declares `android:sharedUserMaxSdkVersion` and is newly
installed on devices running Android 13 or higher, your app
behaves as if you never defined `android:sharedUserId`. Updated apps still use
the existing shared user ID.

> [!CAUTION]
> **Caution:** If you already define the `android:sharedUserId` attribute in your manifest, don't remove it. Doing so causes app updates to fail.

Shared user IDs cause non-deterministic behavior within the package manager.
Your app should instead use proper communication mechanisms, such as services
and content providers, to facilitate interoperability between shared components.

## User experience

### Dismissible foreground service notifications

On devices that run Android 13 or higher, [users can dismiss
notifications associated with foreground
services](https://developer.android.com/guide/components/foreground-services#user-dismiss-notification) by
default.

## Core functionality

### Legacy copy of speech service implementation removed

Android 13 removes the `SpeechService` implementation---including
Voice IME, [`RecognitionService`](https://developer.android.com/reference/android/speech/RecognitionService)
and an [intent-based
API](https://developer.android.com/reference/android/speech/RecognizerIntent#ACTION_RECOGNIZE_SPEECH)---from
the Google app.

In Android 12, the following changes occurred:

- `SpeechService` functionalities were migrated to the [Speech Services by
  Google
  app](https://play.google.com/store/apps/details?id=com.google.android.tts), which became the default `SpeechService` provider.
- `RecognitionService` functionality was moved to the Android System Intelligence app to support on-device speech recognition.

To help maintain app compatibility on Android 12, the Google app
uses a trampoline to divert traffic to the Speech Services by Google app. In
Android 13, this trampoline is removed.

Apps should use the device's default provider for `SpeechService`, rather than
hard-coding a specific app.