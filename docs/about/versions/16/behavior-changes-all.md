---
title: https://developer.android.com/about/versions/16/behavior-changes-all
url: https://developer.android.com/about/versions/16/behavior-changes-all
source: md.txt
---

<br />

The Android 16 platform includes behavior changes that might affect your app.
The following behavior changes apply to *all apps* when they run on Android 16,
regardless of [`targetSdkVersion`](https://developer.android.com/guide/topics/manifest/uses-sdk-element#target). You should test your app and then modify
it as needed to support these changes, where applicable.

Make sure to also review the list of [behavior changes that only affect apps
targeting Android 16](https://developer.android.com/about/versions/16/behavior-changes-16).

## Core functionality

Android 16 (API level 36) includes the following changes that modify or
expand various core capabilities of the Android system.

### JobScheduler quota optimizations

Starting in Android 16, we're adjusting regular and expedited job execution
runtime quota based on the following factors:

- **Which [app standby bucket](https://developer.android.com/topic/performance/appstandby) the application is in**: in Android 16, active standby buckets will start being enforced by a generous runtime quota.
- **If the job starts execution while the app is in a top state**: in Android 16, Jobs started while the app is visible to the user and continues after the app becomes invisible, will adhere to the job runtime quota.
- **If the job is executing while running a Foreground Service** : in Android 16, jobs that are executing concurrently with a foreground service will adhere to the job runtime quota. If you're leveraging jobs for user initiated data transfer, consider using [user initiated data transfer
  jobs](https://developer.android.com/develop/background-work/background-tasks/uidt) instead.

This change impacts tasks scheduled using WorkManager, JobScheduler, and
DownloadManager. To debug why a job was stopped, we recommend logging why your
job was stopped by calling [`WorkInfo.getStopReason()`](https://developer.android.com/reference/androidx/work/WorkInfo#getStopReason()) (for
JobScheduler jobs, call [`JobParameters.getStopReason()`](https://developer.android.com/reference/android/app/job/JobParameters#getStopReason())).

For information about how your app's state affects the resources it can use,
see [Power management resource limits](https://developer.android.com/topic/performance/power/power-details).
For more information on battery-optimal best practices, refer to guidance on
[optimize battery use for task scheduling APIs](https://developer.android.com/develop/background-work/background-tasks/optimize-battery).

We also recommend leveraging the new
[`JobScheduler#getPendingJobReasonsHistory`](https://developer.android.com/about/versions/16/features#feature-pending-job-reason-history) API introduced in
Android 16 to understand why a job has not executed.

##### Testing

To test your app's behavior, you can enable override of certain job quota
optimizations as long as the app is running on an Android 16 device.

To disable enforcement of "top state will adhere to job runtime quota", run the
following [`adb`](https://developer.android.com/tools/adb) command:  

    adb shell am compat enable OVERRIDE_QUOTA_ENFORCEMENT_TO_TOP_STARTED_JOBS <var label="package-name" translate="no">APP_PACKAGE_NAME</var>

To disable enforcement of "jobs that are executing while concurrently with a
foreground service will adhere to the job runtime quota", run the following
`adb` command:  

    adb shell am compat enable OVERRIDE_QUOTA_ENFORCEMENT_TO_FGS_JOBS <var label="package-name" translate="no">APP_PACKAGE_NAME</var>

To test certain app standby bucket behavior, you can set the app standby bucket
of your app using the following `adb` command:  

    adb shell am set-standby-bucket <var label="package-name" translate="no">APP_PACKAGE_NAME</var> active|working_set|frequent|rare|restricted

To understand the app standby bucket your app is in, you can get the app standby
bucket of your app using the following `adb` command:  

    adb shell am get-standby-bucket <var label="package-name" translate="no">APP_PACKAGE_NAME</var>

### Abandoned empty jobs stop reason

An abandoned job occurs when the `JobParameters` object associated with the job
has been garbage collected, but [`JobService#jobFinished(JobParameters,
boolean)`](https://developer.android.com/reference/android/app/job/JobService#jobFinished(android.app.job.JobParameters,%20boolean)) has not been called to signal job completion. This indicates that
the job may be running and being rescheduled without the app's awareness.

Apps that rely on JobScheduler, don't maintain a strong reference to the
`JobParameters` object, and timeout will now be granted the new job stop reason
`STOP_REASON_TIMEOUT_ABANDONED`, instead of `STOP_REASON_TIMEOUT`.

If there are frequent occurrences of the new abandoned stop reason, the system
will take mitigation steps to reduce job frequency.

Apps should use the new stop reason to detect and reduce abandoned jobs.

If you're using WorkManager, AsyncTask, or DownloadManager, you aren't impacted
because these APIs manage the job lifecycle on your app's behalf.

#### Fully deprecating JobInfo#setImportantWhileForeground

The [`JobInfo.Builder#setImportantWhileForeground(boolean)`](https://developer.android.com/reference/android/app/job/JobInfo.Builder#setImportantWhileForeground(boolean))
method indicates the importance of a job while the scheduling app is in the
foreground or when temporarily exempted from background restrictions.

This method has been deprecated since Android 12 (API level 31). Starting in
Android 16, it no longer functions effectively and calling this method will be
ignored.

This removal of functionality also applies to
[`JobInfo#isImportantWhileForeground()`](https://developer.android.com/reference/android/app/job/JobInfo#isImportantWhileForeground()). Starting in Android
16, if the method is called, the method returns `false`.

### Ordered broadcast priority scope no longer global

Android apps are allowed to define priorities on broadcast receivers to control
the order in which the receivers receive and process the broadcast. For
manifest-declared receivers, apps can use the
[`android:priority`](https://developer.android.com/guide/topics/manifest/intent-filter-element#priority) attribute to define the priority and for
context-registered receivers, apps can use the
[`IntentFilter#setPriority()`](https://developer.android.com/reference/android/content/IntentFilter#setPriority(int)) API to define the priority. When
a broadcast is sent, the system delivers it to receivers in order of their
priority, from highest to lowest.

In Android 16, broadcast delivery order using the `android:priority` attribute
or `IntentFilter#setPriority()` across different processes will not be
guaranteed. Broadcast priorities will only be respected within the same
application process rather than across all processes.

Also, broadcast priorities will be automatically confined to the range
([`SYSTEM_LOW_PRIORITY`](https://developer.android.com/reference/android/content/IntentFilter#SYSTEM_LOW_PRIORITY) + 1,
[`SYSTEM_HIGH_PRIORITY`](https://developer.android.com/reference/android/content/IntentFilter#SYSTEM_HIGH_PRIORITY) - 1). Only system components will be
allowed to set `SYSTEM_LOW_PRIORITY`, `SYSTEM_HIGH_PRIORITY` as broadcast
priority.

Your app might be impacted if it does either of the following:

1. Your application has declared multiple processes with the same broadcast intent, and has expectations around receiving those intents in a certain order based on the priority.
2. Your application process interacts with other processes and has expectations around receiving a broadcast intent in a certain order.

If the processes need to coordinate with each other, they should communicate
using other coordination channels.

### ART internal changes

Android 16 includes the latest updates to the Android Runtime (ART) that improve
the Android Runtime's (ART's) performance and provide support for additional
Java features. Through Google Play System updates, these improvements are also
available to [over a billion devices running Android 12 (API level 31) and
higher](https://android-developers.googleblog.com/2023/11/the-secret-to-androids-improved-memory-latest-android-runtime-update.html).

As these changes are released, libraries and app code that rely on internal
structures of ART might not work correctly on devices running Android 16, along
with earlier Android versions that update the ART module through Google Play
system updates.

Relying on internal structures (such as [non-SDK interfaces](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces)) can
always lead to compatibility problems, but it's particularly important to avoid
relying on code (or libraries containing code) that leverages internal ART
structures, since ART changes aren't tied to the platform version the device is
running on and they go out to over a billion devices through Google Play system
updates.

All developers should check whether their app is impacted by testing their apps
thoroughly on Android 16. In addition, check the [known issues](https://developer.android.com/about/versions/16/release-notes#art-impacted-libraries) to
see if your app depends on any libraries that we've identified that rely on
internal ART structures. If you do have app code or library dependencies that
are affected, seek public API alternatives whenever possible and request public
APIs for new use cases by [creating a feature request](https://issuetracker.google.com/issues/new?component=328403&template=1027267) in our issue
tracker.

### 16 KB page size compatibility mode

Android 15 introduced support for 16 KB memory pages to [optimize
performance](https://developer.android.com/guide/practices/page-sizes) of the platform. Android 16 adds a [compatibility
mode](https://source.android.com/docs/core/architecture/16kb-page-size/16kb-backcompat-option), allowing some apps built for 4 KB memory
pages to run on a device configured for 16 KB memory pages.

When your app is running on a device with Android 16 or higher, if Android
detects that your app has 4 KB aligned memory pages, it automatically uses
compatibility mode and display a notification dialog to the user. Setting the
`android:pageSizeCompat` property in the `AndroidManifest.xml` to enable the
backwards compatibility mode will prevent the display of the dialog when your
app launches. To use the `android:pageSizeCompat` property, compile your app
using the [Android 16 SDK](https://developer.android.com/about/versions/16/setup-sdk).

For best performance, reliability, and stability,
your app should still be 16 KB aligned. Check out
[our recent blog post](https://android-developers.googleblog.com/2024/12/get-your-apps-ready-for-16-kb-page-size-devices.html)
on updating your apps to support 16 KB memory pages for more details.
![](https://developer.android.com/static/about/versions/16/images/16-kb-compat-mode-dialog.png) The compatibility mode dialog that displays when the system detects that a 4 KB-aligned app could run more optimally if 16 KB aligned.

## User experience and system UI

Android 16 (API level 36) includes the following changes that are intended
to create a more consistent, intuitive user experience.

### Deprecating disruptive accessibility announcements

Android 16 deprecates accessibility announcements, characterized by the use of
[`announceForAccessibility`](https://developer.android.com/reference/android/view/View#announceForAccessibility(java.lang.CharSequence)) or the dispatch of
[`TYPE_ANNOUNCEMENT`](https://developer.android.com/reference/android/view/accessibility/AccessibilityEvent#TYPE_ANNOUNCEMENT) accessibility events. These can create
inconsistent user experiences for users of TalkBack and Android's screen reader,
and alternatives better serve a broader range of user needs across a variety of
Android's assistive technologies.

Examples of alternatives:

- For significant UI changes like window changes, use [`Activity.setTitle(CharSequence)`](https://developer.android.com/reference/android/app/Activity#setTitle(java.lang.CharSequence)) and [`setAccessibilityPaneTitle(java.lang.CharSequence)`](https://developer.android.com/reference/android/view/View#setAccessibilityPaneTitle(java.lang.CharSequence)). In Compose, use [`Modifier.semantics { paneTitle = "paneTitle" }`](https://developer.android.com/reference/kotlin/androidx/compose/ui/semantics/package-summary#(androidx.compose.ui.semantics.SemanticsPropertyReceiver).liveRegion())
- To inform the user of changes to critical UI, use [`setAccessibilityLiveRegion(int)`](https://developer.android.com/reference/android/view/View#setAccessibilityLiveRegion(int)). In Compose, use [`Modifier.semantics { liveRegion =
  LiveRegionMode.[Polite|Assertive]}`](https://developer.android.com/reference/kotlin/androidx/compose/ui/semantics/package-summary#(androidx.compose.ui.semantics.SemanticsPropertyReceiver).liveRegion()) . These should be used sparingly as they may generate announcements every time a View is updated.
- To notify users about errors, send an `AccessibilityEvent` of type [`AccessibilityEvent#CONTENT_CHANGE_TYPE_ERROR`](https://developer.android.com/reference/android/view/accessibility/AccessibilityEvent#CONTENT_CHANGE_TYPE_ERROR) and set [`AccessibilityNodeInfo#setError(CharSequence)`](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo#setError(java.lang.CharSequence)), or use [`TextView#setError(CharSequence)`](https://developer.android.com/reference/android/widget/TextView#setError(java.lang.CharSequence)).

The reference documentation for the deprecated
[`announceForAccessibility`](https://developer.android.com/reference/android/view/View#announceForAccessibility(java.lang.CharSequence)) API includes more details about
suggested alternatives.

### Support for 3-button navigation

Android 16 brings predictive back support to the 3-button navigation for apps
that have [properly migrated to predictive
back](https://developer.android.com/guide/navigation/custom-back/predictive-back-gesture). Long-pressing the
back button initiates a predictive back animation, giving you a preview of where
the back swipe takes you.

This behavior applies across all areas of the system that support predictive
back animations, including the system animations (back-to-home, cross-task, and
cross-activity).
The predictive back animations in 3-button navigation mode.

### Automatic themed app icons

Beginning with Android 16 QPR 2, Android automatically applies themes to app
icons to create a cohesive home screen experience. This occurs if an app does
not provide its own themed app icon. Apps can control the design of their
themed app icon by including a monochrome layer within their adaptive icon
and previewing what their app icon will look like in [Android Studio](https://developer.android.com/studio/releases/past-releases/as-meerkat-feature-drop-release-notes#themed-icon-support).

## Device form factors

Android 16 (API level 36) includes the following changes for apps when
projected onto displays by virtual device owners.

### Virtual device owner overrides

A virtual device owner is a trusted or privileged app that creates and manages
a virtual device. Virtual device owners run apps on a virtual device and then
project the apps to the display of a remote device, such as a personal
computer, virtual reality device, or car infotainment system. The virtual
device owner is on a local device, such as a mobile phone.
![](https://developer.android.com/static/about/versions/16/images/16-virtual-device-owner-projection.png) Virtual device owner on phone creates virtual device that projects app to remote display.

#### Per-app overrides

On devices running Android 16 (API level 36), virtual device owners can
override app settings on select virtual devices that the virtual device owners
manage. For example, to improve app layout, a virtual device owner can
ignore orientation, aspect ratio, and resizability restrictions when projecting
apps onto an external display.

#### Common breaking changes

The Android 16 behavior might impact your app's UI on large screen form
factors such as car displays or Chromebooks, especially layouts that were
designed for small displays in portrait orientation. To learn how to make your
app adaptive for all device form factors, see [About adaptive
layouts](https://developer.android.com/develop/ui/compose/layouts/adaptive).

#### References

[Companion app streaming](https://source.android.com/docs/core/permissions/app-streaming)

## Security

Android 16 (API level 36) includes changes that promote system security to
help protect apps and users from malicious apps.

### Improved security against Intent redirection attacks

Android 16 provides default security against general `Intent` redirection
attacks, with minimum compatibility and developer changes required.

We are introducing by-default security hardening solutions to `Intent`
redirection exploits. In most cases, apps that use intents normally won't
experience any compatibility issues; we've gathered metrics throughout our
development process to monitor which apps might experience breakages.

[*Intent redirection*](https://developer.android.com/privacy-and-security/risks/intent-redirection) in Android occurs when an attacker can partly or fully
control the contents of an intent used to launch a new component in the context
of a vulnerable app, while the victim app launches an untrusted sub-level intent
in an extras field of an ("top-level") Intent. This can lead to the attacker app
launching private components in the context of the victim app,
triggering privileged actions, or gaining URI access to sensitive data,
potentially leading to data theft and arbitrary code execution.

#### Opt out of Intent redirection handling

Android 16 introduces a new API that allows apps to opt out of launch
security protections. This might be necessary in specific cases where the default
security behavior interferes with legitimate app use cases.
| **Important:** Opting out of security protections should be done with caution and only when absolutely necessary, as it can increase the risk of security vulnerabilities. Carefully assess the potential impact on your app's security before using this API.

##### For applications compiling against Android 16 (API level 36) SDK or higher

You can directly use the `removeLaunchSecurityProtection()` method on the Intent
object.  

    val i = intent
    val iSublevel: Intent? = i.getParcelableExtra("sub_intent")
    iSublevel?.removeLaunchSecurityProtection() // Opt out from hardening
    iSublevel?.let { startActivity(it) }

##### For applications compiling against Android 15 (API level 35) or lower

While not recommended, you can use reflection to access the
`removeLaunchSecurityProtection()` method.
**Caution:** Using reflection can make your code more fragile and prone to errors, especially if the underlying API changes in future Android versions. Whenever possible, update your compile SDK to target Android 16 (API level 36) or higher to use the API directly.  

    val i = intent
    val iSublevel: Intent? = i.getParcelableExtra("sub_intent", Intent::class.java)
    try {
        val removeLaunchSecurityProtection = Intent::class.java.getDeclaredMethod("removeLaunchSecurityProtection")
        removeLaunchSecurityProtection.invoke(iSublevel)
    } catch (e: Exception) {
        // Handle the exception, e.g., log it
    } // Opt-out from the security hardening using reflection
    iSublevel?.let { startActivity(it) }

### Companion apps no longer notified of discovery timeouts

Android 16 introduces a new behavior during
[companion device pairing flow](https://developer.android.com/develop/connectivity/bluetooth/companion-device-pairing) to protect the user's location
privacy from malicious apps. All companion apps running on Android 16 are no
longer directly notified of discovery timeout using
[`RESULT_DISCOVERY_TIMEOUT`](https://developer.android.com/reference/android/companion/CompanionDeviceManager#RESULT_DISCOVERY_TIMEOUT). Instead, the user is
notified of timeout events with a visual dialog. When the user dismisses
the dialog, the app is alerted of the association failure with
[`RESULT_USER_REJECTED`](https://developer.android.com/reference/android/companion/CompanionDeviceManager#RESULT_USER_REJECTED).

The search duration has also been extended from the original 20 seconds,
and the device discovery can be stopped by the user at any point during the
search. If at least one device was discovered within the first 20 seconds of
starting the search, the CDM stops searching for additional devices.

## Connectivity

Android 16 (API level 36) includes the following changes in Bluetooth stack
to improve connectivity with peripheral devices.

### Improved bond loss handling

Starting in Android 16, the Bluetooth stack has been updated to improve security
and user experience when a remote bond loss is detected. Previously, the system
would automatically remove the bond and initiate a new pairing process, which
could lead to unintentional re-pairing. We have seen in many instances apps not
taking care of the bond loss event in a consistent way.

To unify the experience, Android 16 improved the bond loss handling to the
system. If a previously bonded Bluetooth device could not be authenticated upon
reconnection, the system will disconnect the link, retain local bond
information, and display a system dialog informing users of the bond loss and
directing them to re-pair.