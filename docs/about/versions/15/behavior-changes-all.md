---
title: https://developer.android.com/about/versions/15/behavior-changes-all
url: https://developer.android.com/about/versions/15/behavior-changes-all
source: md.txt
---

The Android 15 platform includes behavior changes that might affect your app.
The following behavior changes apply to *all apps* when they run on Android 15,
regardless of [`targetSdkVersion`](https://developer.android.com/guide/topics/manifest/uses-sdk-element#target). You should test your app and then modify
it as needed to support these properly, where applicable.

Make sure to also review the list of [behavior changes that only affect apps
targeting Android 15](https://developer.android.com/about/versions/15/behavior-changes-15).

## Core functionality

Android 15 modifies or expands various core capabilities of the Android system.

### Changes to package stopped state

The intention of the package [`FLAG_STOPPED`](https://developer.android.com/reference/android/content/pm/ApplicationInfo#FLAG_STOPPED) state (which users
can engage in AOSP builds by long-pressing an app icon and selecting "Force
Stop") has always been to keep apps in this state until the user explicitly
removes the app from this state by directly launching the app or indirectly
interacting with the app (through the sharesheet or a widget, selecting the app
as live wallpaper, etc.). In Android 15, we've updated the behavior of the
system to be aligned with this intended behavior. Apps should only be removed
from the stopped state through direct or indirect user action.

To support the intended behavior, in addition to the existing restrictions, the
system also cancels all [pending intents](https://developer.android.com/reference/android/app/PendingIntent) when the app enters the
stopped state on a device running Android 15. When the user's actions remove the
app from the stopped state, the [`ACTION_BOOT_COMPLETED`](https://developer.android.com/reference/android/content/Intent#ACTION_BOOT_COMPLETED)
broadcast is delivered to the app providing an opportunity to re-register any
pending intents.
| **Note:** Apps use pending intents to update [app widgets](https://developer.android.com/develop/ui/views/appwidgets/overview). If an app enters the stopped state, all these pending intents are canceled, and the system disables the app's widgets. (The widgets are grayed out, and the device user cannot interact with them.) The system re-enables the widgets the next time the user launches the app.

You can call the new
[`ApplicationStartInfo.wasForceStopped()`](https://developer.android.com/reference/android/app/ApplicationStartInfo#wasForceStopped())
method to confirm whether the app was put into the stopped state.

### Support for 16 KB page sizes

Historically, Android has only supported 4 KB memory page sizes, which has
optimized system memory performance for the average amount of total memory that
Android devices have typically had. Beginning with Android 15, AOSP supports
devices that are configured to use a page size of 16 KB (16 KB
devices). If your app uses any [NDK](https://developer.android.com/ndk) libraries, either directly
or indirectly through an SDK, then you will need to rebuild your app for it to
work on these 16 KB devices.

As device manufacturers continue to build devices with larger amounts of
physical memory (RAM), many of these devices will adopt 16 KB (and
eventually greater) page sizes to optimize the device's performance. Adding
support for 16 KB page size devices enables your app to run on these
devices and helps your app benefit from the associated performance
improvements. Without recompiling, apps won't work on 16 KB devices in
future Android releases.

To help you add support for your app, we've provided guidance on how to [check
if your app is impacted](https://developer.android.com/guide/practices/page-sizes#16-kb-impact), how to
[rebuild your app](https://developer.android.com/guide/practices/page-sizes#build) (if applicable), and how to [test your app in
a 16 KB environment](https://developer.android.com/guide/practices/page-sizes#test) using emulators (including Android 15
system images for the Android Emulator).

#### Benefits and performance gains

Devices configured with 16 KB page sizes use slightly more memory on
average, but also gain various performance improvements for both the system and
apps:

- Lower app launch times while the system is under memory pressure: 3.16% lower on average, with more significant improvements (up to 30%) for some apps that we tested
- Reduced power draw during app launch: 4.56% reduction on average
- Faster camera launch: 4.48% faster hot starts on average, and 6.60% faster cold starts on average
- Improved system boot time: improved by 8% (approximately 950 milliseconds) on average

These improvements are based on our initial testing, and results on actual
devices will likely differ. We'll provide additional analysis of potential gains
for apps as we continue our testing.

#### Check if your app is impacted

If your app [uses any native code](https://developer.android.com/guide/practices/page-sizes#native-code), then you should [rebuild
your app with support for 16 KB devices](https://developer.android.com/guide/practices/page-sizes#build). If you are unsure
if your app uses native code, you can [use the APK Analyzer to identify whether
any native code is present](https://developer.android.com/guide/practices/page-sizes#identify-native-code) and then [check the alignment of ELF
segments for any shared libraries](https://developer.android.com/guide/practices/page-sizes#elf-alignment) that you find. Android Studio
also provides features that help you to [automatically detect alignment
issues](https://developer.android.com/guide/practices/page-sizes#auto-checks).

If your app only uses code written in the Java programming language or in
Kotlin, including all libraries or SDKs, then your app already supports
16 KB devices. Nevertheless, we recommend that you [test your app in a
16 KB environment](https://developer.android.com/guide/practices/page-sizes#test) to verify that there are no unexpected
regressions in app behavior.

### Required changes for some apps to support private space

[Private space](https://developer.android.com/about/versions/15/features#private-space) is a new feature in Android 15 that lets users
create a separate space on their device where they can keep sensitive apps away
from prying eyes, under an additional layer of authentication. Because apps in
the private space have restricted visibility, some types of apps need to take
additional steps to be able to see and interact with apps in a user's private
space.

#### All apps

Because apps in the private space are kept in a separate user profile, similar
to [work profiles](https://developer.android.com/work/managed-profiles), apps shouldn't assume that any installed
copies of their app that aren't in the main profile are in the work profile. If
your app has logic related to work profile apps that make this assumption,
you'll need to adjust this logic.

#### Medical apps

When a user locks the private space, all apps in the private space are stopped,
and those apps can't perform foreground or background activities, including
showing notifications. This behavior might critically impact the use and
function of medical apps installed in the private space.

The private space setup experience warns users that the private space is not
suitable for apps that need to perform critical foreground or background
activities, such as showing notifications from medical apps. However,
apps can't determine whether or not they're being used in the private space,
so they can't show a warning to the user for this case.

For these reasons, if you develop a medical app, review how this feature might
impact your app and take appropriate actions---such as informing your users not to
install your app in the private space---to avoid disrupting critical app
capabilities.

#### Launcher apps

If you develop a launcher app, you must do the following before apps in the
private space will be visible:

1. Your app must be assigned as the default launcher app for the device---that is, possessing the [`ROLE_HOME`](https://developer.android.com/reference/android/app/role/RoleManager#ROLE_HOME) role.
2. Your app must declare the [`ACCESS_HIDDEN_PROFILES`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_HIDDEN_PROFILES) normal permission [in your app's manifest file](https://developer.android.com/training/permissions/declaring).

Launcher apps that declare the `ACCESS_HIDDEN_PROFILES` permission must handle
the following private space use cases:

1. Your app must have a separate launcher container for apps installed in the private space. Use the [`getLauncherUserInfo()`](https://developer.android.com/reference/android/content/pm/LauncherApps#getLauncherUserInfo(android.os.UserHandle)) method to determine which type of user profile is being handled.
2. The user must be able to hide and show the private space container.
3. The user must be able to lock and unlock the private space container. Use the [`requestQuietModeEnabled()`](https://developer.android.com/reference/android/os/UserManager#requestQuietModeEnabled(boolean,%20android.os.UserHandle)) method to lock (by passing `true`) or unlock (by passing `false`) the private space.
4. While locked, no apps in the private space container should be visible or
   discoverable through mechanisms such as search. Your app should [register a
   receiver](https://developer.android.com/develop/background-work/background-tasks/broadcasts#context-registered-receivers) for the
   [`ACTION_PROFILE_AVAILABLE`](https://developer.android.com/reference/android/content/Intent#ACTION_PROFILE_AVAILABLE) and
   [`ACTION_PROFILE_UNAVAILABLE`](https://developer.android.com/reference/android/content/Intent#ACTION_PROFILE_UNAVAILABLE) broadcasts and update the
   UI in your app when the locked or unlocked state of the private space
   container changes. Both of these broadcasts include
   [`EXTRA_USER`](https://developer.android.com/reference/android/content/Intent#EXTRA_USER), which your app can use to refer to the
   private profile user.

   You can also use the [`isQuietModeEnabled()`](https://developer.android.com/reference/android/os/UserManager#isQuietModeEnabled(android.os.UserHandle)) method to
   check whether the private space profile is locked or not.

#### App store apps

The private space includes an "Install Apps" button that launches an implicit
intent to install apps into the user's private space. In order for your app to
receive this implicit intent, declare an [`<intent-filter>`](https://developer.android.com/guide/topics/manifest/intent-filter-element)
in your app's manifest file with a [`<category>`](https://developer.android.com/guide/topics/manifest/category-element) of
[`CATEGORY_APP_MARKET`](https://developer.android.com/reference/android/content/Intent#CATEGORY_APP_MARKET).

### PNG-based emoji font removed

The legacy, PNG-based emoji font file (`NotoColorEmojiLegacy.ttf`) has been
removed, leaving just the vector-based file. Beginning with Android 13 (API
level 33), the emoji font file used by the system emoji renderer [changed from a
PNG-based file to a vector based file](https://developer.android.com/about/versions/13/features#color-vector-fonts). The system retained
the legacy font file in Android 13 and 14 for compatibility reasons, so that
apps with their own font renderers could continue to use the legacy font file
until they were able to upgrade.

To check if your app is affected, search your app's code for references to the
`NotoColorEmojiLegacy.ttf` file.

You can choose to adapt your app in a number of ways:

- Use platform APIs for text rendering. You can render text to a bitmap-backed `Canvas` and use that to get a raw image if necessary.
- Add COLRv1 font support to your app. The FreeType open source library supports COLRv1 in [version 2.13.0](https://sourceforge.net/projects/freetype/files/freetype2/2.13.0/) and higher.
- As a last resort, you can bundle the legacy emoji font file ([`NotoColorEmoji.ttf`](https://github.com/googlefonts/noto-emoji/blob/main/fonts/NotoColorEmoji.ttf)) into your APK, although in that case your app will be missing the latest emoji updates. For more information, see the [Noto Emoji GitHub project
  page](https://github.com/googlefonts/noto-emoji).

### Increased minimum target SDK version from 23 to 24

Android 15 builds on the
[the changes that were made in Android 14](https://developer.android.com/about/versions/14/behavior-changes-all#minimum-target-api-level) and extends this
security further. In Android 15, apps with a
[`targetSdkVersion`](https://developer.android.com/guide/topics/manifest/uses-sdk-element) lower than 24 can't be installed.
Requiring apps to meet modern API levels helps to ensure better security and
privacy.

Malware often targets lower API levels in order to bypass security and privacy
protections that have been introduced in higher Android versions. For example,
some malware apps use a `targetSdkVersion` of 22 to avoid being subjected to the
runtime permission model introduced in 2015 by Android 6.0 Marshmallow (API
level 23). This Android 15 change makes it harder for malware to avoid security
and privacy improvements. Attempting to install an app targeting a lower API
level results in an installation failure, with a message like the following one
appearing in Logcat:  

    INSTALL_FAILED_DEPRECATED_SDK_VERSION: App package must target at least SDK version 24, but found 7

On devices upgrading to Android 15, any apps with a `targetSdkVersion` lower
than 24 remain installed.

If you need to test an app targeting an older API level, use the following ADB
command:  

```
adb install --bypass-low-target-sdk-block FILENAME.apk
```

## Security and privacy

Android 15 introduces robust measures to combat one-time passcode (OTP) fraud
and to protect the user's sensitive content, focusing on hardening the
Notification Listener Service and screenshare protections. Key enhancements
include redacting OTPs from notifications accessible to untrusted apps, hiding
notifications during screenshare, and securing app activities when OTPs are
posted. These changes aim to keep the user's sensitive content safe from
unauthorized actors.

Developers need to be aware of the following to ensure their apps are compatible
with the changes in Android 15:

### OTP Redaction

Android will stop untrusted apps that implement a
[`NotificationListenerService`](https://developer.android.com/reference/android/service/notification/NotificationListenerService) from reading unredacted content
from notifications where an OTP has been detected. Trusted apps such as
companion device manager associations are exempt from these restrictions.

### Screenshare Protection

- Notification content is hidden during screen sharing sessions to preserve the user's privacy. If the app implements [`setPublicVersion()`](https://developer.android.com/reference/android/app/Notification.Builder#setPublicVersion(android.app.Notification)), Android shows the public version of the notification which serves as a replacement notification in insecure contexts. Otherwise, the notification content is redacted without any further context.
- Sensitive content like password input is hidden from remote viewers to prevent revealing the user's sensitive information.
- Activities from apps that post notifications during screenshare where an OTP has been detected will be hidden. App content is hidden from the remote viewer when launched.
- Beyond Android's automatic identification of sensitive fields, developers can manually mark parts of their app as sensitive using [`setContentSensitivity`](https://developer.android.com/reference/android/view/View#setContentSensitivity(int)), which is hidden from remote viewers during screenshare.
- Developers can choose to toggle the **Disable screen share protections** option under **Developer Options** to be exempted from the screenshare protections for demo or testing purposes. The default system screen recorder is exempted from these changes, since the recordings remain on-device.

## Camera and media

Android 15 makes the following changes to camera and media behavior for all
apps.

### Direct and offload audio playback invalidates previously open direct or offload audio tracks when resource limits are reached

Before Android 15, if an app requested direct or offload audio playback while
another app was playing audio and the resource limits were reached, the app
would fail to open a new [`AudioTrack`](https://developer.android.com/reference/android/media/AudioTrack).

Beginning with Android 15, when an app requests direct or offload
playback and the resource
limits are reached, the system invalidates any currently open
`AudioTrack` objects which prevent fulfilling the new track request.

(Direct and offload audio tracks are typically opened for playback of compressed
audio formats. Common use-cases for playing direct audio include streaming
encoded audio over HDMI to a TV. Offload tracks are typically used to play
compressed audio on a mobile device with hardware DSP acceleration.)

## User experience and system UI

Android 15 includes some changes that are intended to create a more consistent,
intuitive user experience.

### Predictive back animations enabled for apps that opted in

Beginning in Android 15, the developer option for
[predictive back animations](https://developer.android.com/guide/navigation/custom-back/predictive-back-gesture) has been removed. System
animations such as back-to-home, cross-task, and cross-activity now appear for
apps that have [opted in to the predictive back gesture](https://developer.android.com/guide/navigation/custom-back/predictive-back-gesture#opt-predictive)
either entirely or at an activity level. If your app is affected, take the
following actions:

- Ensure that your app has been properly migrated to use the predictive back gesture.
- Ensure that your fragment transitions work with predictive back navigation.
- Migrate away from animation and framework transitions and use animator and androidx transitions instead.
- Migrate away from back stacks that `FragmentManager` doesn't know about. Use back stacks managed by `FragmentManager` or by the Navigation component instead.

### Widgets disabled when user force-stops an app

If a user force-stops an app on a device running Android 15, the system
temporarily disables all the app's widgets. The widgets are grayed out, and the
user cannot interact with them. This is because beginning with Android 15, the
system cancels all an app's pending intents when the app is force-stopped.

The system re-enables those widgets the next time the user launches the app.

For more information, see
[Changes to package stopped state](https://developer.android.com/about/versions/15/behavior-changes-all#enhanced-stop-states).

### Media projection status bar chip alerts users to screen sharing, casting, and recording

| **Note:** This change is included on devices running [Android 15
| QPR1](https://developer.android.com/about/versions/15/release-notes) or higher.

Screen projection exploits expose private user data such as financial
information because users don't realize their device screen is being shared.

For apps running on devices with Android 15 QPR1 or higher, a status bar chip
that is large and prominent alerts users to any in‑progress screen
projection. Users can tap the chip to stop their screen from being shared, cast,
or recorded. Also, screen projection automatically stops when the device screen
is locked.
![](https://developer.android.com/static/media/images/grow/media_projection_status_bar_chip.png) Status bar chip for screen sharing, casting, and recording.

#### Check if your app is impacted

By default, your app includes the status bar chip and automatically suspends
screen projection when the lock screen activates.

To learn more about how to test your app for these use cases, see [Status bar
chip and auto stop](https://developer.android.com/media/grow/media-projection#status_bar_chip_auto_stop).

### Background network access restrictions

In Android 15, apps that start a network request outside of a valid [process
lifecycle](https://developer.android.com/guide/components/activities/process-lifecycle) receive an exception. Typically, an
[`UnknownHostException`](https://developer.android.com/reference/java/net/UnknownHostException) or other socket-related
`IOException`. Network requests that happen outside of a valid lifecycle are
usually due to apps unknowingly continuing a network request even after the app
is no longer active.

To mitigate this exception, ensure your network requests are lifecycle aware
and cancelled upon leaving a valid process lifecycle by using
[lifecycle aware components](https://developer.android.com/topic/libraries/architecture/lifecycle).
If it is important that the network request should happen even when the user
leaves the application, consider scheduling the network request using
[WorkManager](https://developer.android.com/topic/libraries/architecture/workmanager) or continue a user visible task using
[Foreground Service](https://developer.android.com/develop/background-work/services/fgs).

## Deprecations

With each release, specific Android APIs might become obsolete or need to be
refactored to provide a better developer experience or support new platform
capabilities. In these cases, we officially deprecate the obsolete APIs and
direct developers to alternative APIs to use instead.

Deprecation means that we've ended official support for the APIs, but they will
continue to remain available to developers. To learn more about notable
deprecations in this release of Android, see the [deprecations page](https://developer.android.com/about/versions/15/deprecations).