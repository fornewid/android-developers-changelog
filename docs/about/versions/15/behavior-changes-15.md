---
title: https://developer.android.com/about/versions/15/behavior-changes-15
url: https://developer.android.com/about/versions/15/behavior-changes-15
source: md.txt
---

Like previous releases, Android 15 includes behavior changes that might affect
your app. The following behavior changes apply exclusively to apps that are
targeting Android 15 or higher. If your app is targeting Android 15 or higher,
you should modify your app to support these behaviors properly, where
applicable.

Be sure to also review the list of [behavior changes that affect all apps
running on Android 15](https://developer.android.com/about/versions/15/behavior-changes-all) regardless of your app's [`targetSdkVersion`](https://developer.android.com/guide/topics/manifest/uses-sdk-element#target).

## Core functionality

Android 15 modifies or expands various core capabilities of the Android system.

### Changes to foreground services

We are making the following changes to foreground services with Android 15.

- [Data sync foreground service timeout behavior](https://developer.android.com/about/versions/15/behavior-changes-15#datasync-timeout)
- [New media processing foreground service type](https://developer.android.com/about/versions/15/behavior-changes-15#mediaprocessing-fgs-type)
- [Restrictions on `BOOT_COMPLETED` broadcast receivers launching foreground services](https://developer.android.com/about/versions/15/behavior-changes-15#fgs-boot-completed)
- [Restrictions on starting foreground services while an app holds the `SYSTEM_ALERT_WINDOW` permission](https://developer.android.com/about/versions/15/behavior-changes-15#fgs-sysalert)

#### Data sync foreground service timeout behavior

Android 15 introduces a new timeout behavior to `dataSync` for apps targeting
Android 15 (API level 35) or higher. This behavior also applies to the new
[`mediaProcessing` foreground service type](https://developer.android.com/about/versions/15/changes/foreground-service-types#media-processing).

The system permits an app's `dataSync` services to run for a total of 6 hours
in a 24-hour period, after which the system calls the running service's
[`Service.onTimeout(int, int)`](https://developer.android.com/reference/android/app/Service#onTimeout(int,%20int)) method (introduced in Android
15). At this time, the service has a few seconds to call
[`Service.stopSelf()`](https://developer.android.com/reference/android/app/Service#stopSelf()). When `Service.onTimeout()` is called, the
service is no longer considered a foreground service. If the service does not
call `Service.stopSelf()`, the system throws an internal exception. The
exception is logged in [Logcat](https://developer.android.com/tools/logcat) with the following message:

    Fatal Exception: android.app.RemoteServiceException: "A foreground service of
    type dataSync did not stop within its timeout: [component name]"

> [!NOTE]
> **Note:** The 6-hour time limit is shared by all of an app's `dataSync` foreground services. For example, if an app runs a `dataSync` service for four hours, then starts a different `dataSync` service, that second service will only be allowed to run for two hours. However, if the user brings the app to the foreground, the timer resets and the app has 6 hours available.

To avoid problems with this behavior change, you can do one or more of the
following:

1. Have your service implement the new `Service.onTimeout(int, int)` method. When your app receives the callback, make sure to call `stopSelf()` within a few seconds. (If you don't stop the app right away, the system generates a failure.)
2. Make sure your app's `dataSync` services don't run for more than a total of 6 hours in any 24-hour period (unless the user interacts with the app, resetting the timer).
3. Only start `dataSync` foreground services as a result of direct user interaction; since your app is in the foreground when the service starts, your service has the full six hours after the app goes to the background.
4. Instead of using a `dataSync` foreground service, use an [alternative API](https://developer.android.com/develop/background-work/background-tasks/data-transfer-options).

If your app's `dataSync` foreground services have run for 6 hours in the last
24, you cannot start another `dataSync` foreground service *unless* the user
has brought your app to the foreground (which resets the timer). If you try to
start another `dataSync` foreground service, the system throws
[`ForegroundServiceStartNotAllowedException`](https://developer.android.com/reference/android/app/ForegroundServiceStartNotAllowedException)
with an error message like "Time limit already exhausted for foreground service
type dataSync".

##### Testing

To test your app's behavior, you can enable data sync timeouts even if your app
is not targeting Android 15 (as long as the app is running on an Android 15
device). To enable timeouts, run the following [`adb`](https://developer.android.com/tools/adb) command:

    adb shell am compat enable FGS_INTRODUCE_TIME_LIMITS your-package-name

You can also adjust the timeout period, to make it easier to test how your
app behaves when the limit is reached. To set a new timeout period, run the
following `adb` command:

    adb shell device_config put activity_manager data_sync_fgs_timeout_duration duration-in-milliseconds

#### New media processing foreground service type

Android 15 introduces a new foreground service type, `mediaProcessing`. This
service type is appropriate for operations like transcoding media files. For
example, a media app might download an audio file and need to convert it to a
different format before playing it. You can use a `mediaProcessing` foreground
service to make sure the conversion continues even while the app is in the
background.

The system permits an app's `mediaProcessing` services to run for a total of 6
hours in a 24-hour period, after which the system calls the running service's
[`Service.onTimeout(int, int)`](https://developer.android.com/reference/android/app/Service#onTimeout(int,%20int)) method (introduced in Android
15). At this time, the service has a few seconds to call
[`Service.stopSelf()`](https://developer.android.com/reference/android/app/Service#stopSelf()). If the service does not
call `Service.stopSelf()`, the system throws an internal exception. The
exception is logged in [Logcat](https://developer.android.com/tools/logcat) with the following message:

    Fatal Exception: android.app.RemoteServiceException: "A foreground service of
    type mediaProcessing did not stop within its timeout: [component name]"

> [!NOTE]
> **Note:** The 6-hour time limit is shared by all of an app's `mediaProcessing` foreground services. For example, if an app runs a `mediaProcessing` service for four hours, then starts a different `mediaProcessing` service, that second service will only be allowed to run for two hours. However, if the user brings the app to the foreground, the timer resets and the app has 6 hours available.

To avoid having the exception, you can do one of the following:

1. Have your service implement the new `Service.onTimeout(int, int)` method. When your app receives the callback, make sure to call `stopSelf()` within a few seconds. (If you don't stop the app right away, the system generates a failure.)
2. Make sure your app's `mediaProcessing` services don't run for more than a total of 6 hours in any 24-hour period (unless the user interacts with the app, resetting the timer).
3. Only start `mediaProcessing` foreground services as a result of direct user interaction; since your app is in the foreground when the service starts, your service has the full six hours after the app goes to the background.
4. Instead of using a `mediaProcessing` foreground service, use an [alternative
   API](https://developer.android.com/develop/background-work/services/foreground-services#purpose-built-apis), like WorkManager.

If your app's `mediaProcessing` foreground services have run for 6 hours in the
last 24, you cannot start another `mediaProcessing` foreground service *unless*
the user has brought your app to the foreground (which resets the timer). If you
try to start another `mediaProcessing` foreground service, the system throws
[`ForegroundServiceStartNotAllowedException`](https://developer.android.com/reference/android/app/ForegroundServiceStartNotAllowedException)
with an error message like "Time limit already exhausted for foreground service
type mediaProcessing".

For more information about the `mediaProcessing` service type, see [Changes to
foreground service types for Android 15: Media processing](https://developer.android.com/about/versions/15/changes/foreground-service-types#media-processing).

##### Testing

To test your app's behavior, you can enable media processing timeouts even if
your app is not targeting Android 15 (as long as the app is running on an
Android 15 device). To enable timeouts, run the following [`adb`](https://developer.android.com/tools/adb) command:

    adb shell am compat enable FGS_INTRODUCE_TIME_LIMITS your-package-name

You can also adjust the timeout period, to make it easier to test how your
app behaves when the limit is reached. To set a new timeout period, run the
following `adb` command:

    adb shell device_config put activity_manager media_processing_fgs_timeout_duration duration-in-milliseconds

#### Restrictions on `BOOT_COMPLETED` broadcast receivers launching foreground services

There are new restrictions on `BOOT_COMPLETED` broadcast receivers launching
foreground services. `BOOT_COMPLETED` receivers are *not* allowed to launch the
following types of foreground services:

- [`dataSync`](https://developer.android.com/develop/background-work/services/fg-service-types#data-sync)
- [`camera`](https://developer.android.com/develop/background-work/services/fg-service-types#camera)
- [`mediaPlayback`](https://developer.android.com/develop/background-work/services/fg-service-types#media)
- [`phoneCall`](https://developer.android.com/develop/background-work/services/fg-service-types#phone-call)
- [`mediaProjection`](https://developer.android.com/develop/background-work/services/fg-service-types#media-projection)
- [`microphone`](https://developer.android.com/develop/background-work/services/fg-service-types#microphone) (this restriction has been in place for `microphone` since Android 14)

If a `BOOT_COMPLETED` receiver tries to launch any of those types of foreground
services, the system throws [`ForegroundServiceStartNotAllowedException`](https://developer.android.com/reference/android/app/ForegroundServiceStartNotAllowedException).

##### Testing

To test your app's behavior, you can enable these new restrictions even if your
app is not targeting Android 15 (as long as the app is running on an Android 15
device). Run the following [`adb`](https://developer.android.com/tools/adb) command:

    adb shell am compat enable FGS_BOOT_COMPLETED_RESTRICTIONS your-package-name

To send a `BOOT_COMPLETED` broadcast without restarting the device,
run the following [`adb`](https://developer.android.com/tools/adb) command:

    adb shell am broadcast -a android.intent.action.BOOT_COMPLETED your-package-name

#### Restrictions on starting foreground services while an app holds the `SYSTEM_ALERT_WINDOW` permission

Previously, if an app held the `SYSTEM_ALERT_WINDOW` permission, it could launch
a foreground service even if the app was currently in the background (as
discussed in [exemptions from background start restrictions](https://developer.android.com/develop/background-work/services/fgs/restrictions-bg-start#background-start-restriction-exemptions))).

If an app targets Android 15, this exemption is now narrower. The app now needs
to have the `SYSTEM_ALERT_WINDOW` permission and *also* have a visible overlay
window. That is, the app needs to first launch a
[`TYPE_APPLICATION_OVERLAY`](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#TYPE_APPLICATION_OVERLAY) window *and* the window
needs to be visible before you start a foreground service.

If your app attempts to start a foreground service from the background without
meeting these new requirements (and it does not have some other exemption), the
system throws [`ForegroundServiceStartNotAllowedException`](https://developer.android.com/reference/android/app/ForegroundServiceStartNotAllowedException).

If your app declares the [`SYSTEM_ALERT_WINDOW`](https://developer.android.com/reference/android/Manifest.permission#SYSTEM_ALERT_WINDOW) permission
and launches foreground services from the background, it may be affected by this
change. If your app gets a `ForegroundServiceStartNotAllowedException`, check
your app's order of operations and make sure your app already has an active
overlay window before it attempts to start a foreground service from the
background. You can check if your overlay window is currently visible
by calling [`View.getWindowVisibility()`](https://developer.android.com/reference/android/view/View#getWindowVisibility()), or you
can override [`View.onWindowVisibilityChanged()`](https://developer.android.com/reference/android/view/View#onWindowVisibilityChanged(int))
to get notified whenever the visibility changes.

##### Testing

To test your app's behavior, you can enable these new restrictions even if your
app is not targeting Android 15 (as long as the app is running on an Android 15
device). To enable these new restrictions on starting foreground services
from the background, run the following [`adb`](https://developer.android.com/tools/adb) command:

    adb shell am compat enable FGS_SAW_RESTRICTIONS your-package-name

### Changes to when apps can modify the global state of Do Not Disturb mode

Apps that target Android 15 (API level 35) and higher can no longer change the
global state or policy of Do Not Disturb (DND) on a device (either by modifying
user settings, or turning off DND mode). Instead, apps must contribute an
[`AutomaticZenRule`](https://developer.android.com/reference/android/app/AutomaticZenRule), which the system combines into a global policy with the
existing most-restrictive-policy-wins scheme. Calls to existing APIs that
previously affected global state ([`setInterruptionFilter`](https://developer.android.com/reference/android/app/NotificationManager#setInterruptionFilter(int)),
[`setNotificationPolicy`](https://developer.android.com/reference/android/app/NotificationManager#setNotificationPolicy(android.app.NotificationManager.Policy))) result in the creation or update of an implicit
`AutomaticZenRule`, which is toggled on and off depending on the call-cycle of
those API calls.

Note that this change only affects observable behavior if the app is calling
`setInterruptionFilter(INTERRUPTION_FILTER_ALL)` and expects that call to
deactivate an `AutomaticZenRule` that was previously activated by their owners.

### OpenJDK API changes

Android 15 continues the work of refreshing Android's core libraries to align
with the features in the latest OpenJDK LTS releases.

Some of these changes can affect app compatibility for apps targeting
Android 15 (API level 35):

- **Changes to string formatting APIs** : Validation of argument index, flags,
  width, and precision are now more strict when using the following
  `String.format()` and `Formatter.format()` APIs:

  - [`String.format(String, Object[])`](https://developer.android.com/reference/java/lang/String#format(java.lang.String,%20java.lang.Object%5B%5D))
  - [`String.format(Locale, String, Object[])`](https://developer.android.com/reference/java/lang/String#format(java.util.Locale,%20java.lang.String,%20java.lang.Object%5B%5D))
  - [`Formatter.format(String, Object[])`](https://developer.android.com/reference/java/util/Formatter#format(java.lang.String,%20java.lang.Object%5B%5D))
  - [`Formatter.format(Locale, String, Object[])`](https://developer.android.com/reference/java/util/Formatter#format(java.util.Locale,%20java.lang.String,%20java.lang.Object%5B%5D))

  For example, the following exception is thrown when an argument index of 0
  is used (`%0` in the format string):

      IllegalFormatArgumentIndexException: Illegal format argument index = 0

  In this case, the issue can be fixed by using an argument index of 1 (`%1`
  in the format string).
- **Changes to component type of `Arrays.asList(...).toArray()`** : When using
  `Arrays.asList(...).toArray()`, the component type of the resulting array is
  now an [`Object`](https://developer.android.com/reference/java/lang/Object)---not the type of the underlying array's elements. So the
  following code throws a [`ClassCastException`](https://developer.android.com/reference/java/lang/ClassCastException):

      String[] elements = (String[]) Arrays.asList("one", "two").toArray();

  For this case, to preserve `String` as the component type in the resulting
  array, you could use [`Collection.toArray(Object[])`](https://developer.android.com/reference/java/util/Collection#toArray(T%5B%5D)) instead:

      String[] elements = Arrays.asList("two", "one").toArray(new String[0]);

- **Changes to language code handling** : When using the [`Locale`](https://developer.android.com/reference/java/util/Locale) API,
  language codes for Hebrew, Yiddish, and Indonesian are no longer converted
  to their obsolete forms (Hebrew: `iw`, Yiddish: `ji`, and Indonesian: `in`).
  When specifying the language code for one of these locales, use the codes
  from ISO 639-1 instead (Hebrew: `he`, Yiddish: `yi`, and Indonesian: `id`).

- **Changes to random int sequences** : Following the changes made in
  <https://bugs.openjdk.org/browse/JDK-8301574>, the following
  `Random.ints()` methods now return a different sequence of numbers than
  the `Random.nextInt()` methods do:

  - [`Random.ints(long)`](https://developer.android.com/reference/java/util/Random#ints(long))
  - [`Random.ints(long, int, int)`](https://developer.android.com/reference/java/util/Random#ints(long,%20int,%20int))
  - [`Random.ints(int, int)`](https://developer.android.com/reference/java/util/Random#ints(int,%20int))
  - [`Random.ints()`](https://developer.android.com/reference/java/util/Random#ints())

  Generally, this change shouldn't result in app-breaking behavior, but your
  code shouldn't expect the sequence generated from `Random.ints()` methods to
  match `Random.nextInt()`.

The new [`SequencedCollection`](https://developer.android.com/reference/java/util/SequencedCollection) API can affect your app's compatibility
after you [update `compileSdk` in your app's build configuration to use
Android 15 (API level 35)](https://developer.android.com/about/versions/15/setup-sdk#config):

- **Collision with [`MutableList.removeFirst()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/remove-first.html) and
  [`MutableList.removeLast()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/remove-last.html) extension functions in `kotlin-stdlib`**

  The [`List`](https://developer.android.com/reference/java/util/List) type in Java is mapped to the `MutableList` type in Kotlin.
  Because the [`List.removeFirst()`](https://developer.android.com/reference/java/util/List#removeFirst()) and [`List.removeLast()`](https://developer.android.com/reference/java/util/List#removeLast()) APIs
  have been introduced in Android 15 (API level 35), the Kotlin compiler
  resolves function calls, for example `list.removeFirst()`, statically to the
  new [`List`](https://developer.android.com/reference/java/util/List) APIs instead of to the extension functions in
  `kotlin-stdlib`.

  If an app is re-compiled with `compileSdk` set to `35` and `minSdk` set to
  `34` or lower, and then the app is run on Android 14 and lower, a runtime
  error is thrown:

      java.lang.NoSuchMethodError: No virtual method
      removeFirst()Ljava/lang/Object; in class Ljava/util/ArrayList;

  The existing `NewApi` lint option in Android Gradle Plugin can catch these
  new API usages.

      ./gradlew lint

      MainActivity.kt:41: Error: Call requires API level 35 (current min is 34): java.util.List#removeFirst [NewApi]
            list.removeFirst()

  To fix the runtime exception and lint errors, the `removeFirst()` and
  `removeLast()` function calls can be replaced with `removeAt(0)` and
  `removeAt(list.lastIndex)` respectively in Kotlin. If you're using
  Android Studio Ladybug \| 2024.1.3 or higher, it also provides a quick fix
  option for these errors.

  Consider removing `@SuppressLint("NewApi")` and `lintOptions { disable
  'NewApi' }` if the lint option has been disabled.
- **Collision with other methods in Java**

  New methods have been added into the existing types, for example,
  [`List`](https://developer.android.com/reference/java/util/List) and [`Deque`](https://developer.android.com/reference/java/util/Deque). These new methods might not be compatible
  with the methods with the same name and argument types in other interfaces
  and classes. In the case of a method signature collision with
  incompatibility, the `javac` compiler outputs a build-time error. For
  example:

  Example error 1:

      javac MyList.java

      MyList.java:135: error: removeLast() in MyList cannot implement removeLast() in List
        public void removeLast() {
                    ^
        return type void is not compatible with Object
        where E is a type-variable:
          E extends Object declared in interface List

  Example error 2:

      javac MyList.java

      MyList.java:7: error: types Deque<Object> and List<Object> are incompatible;
      public class MyList implements  List<Object>, Deque<Object> {
        both define reversed(), but with unrelated return types
      1 error

  Example error 3:

      javac MyList.java

      MyList.java:43: error: types List<E#1> and MyInterface<E#2> are incompatible;
      public static class MyList implements List<Object>, MyInterface<Object> {
        class MyList inherits unrelated defaults for getFirst() from types List and MyInterface
        where E#1,E#2 are type-variables:
          E#1 extends Object declared in interface List
          E#2 extends Object declared in interface MyInterface
      1 error

  To fix these build errors, the class implementing these interfaces should
  override the method with a compatible return type. For example:

      @Override
      public Object getFirst() {
          return List.super.getFirst();
      }

## Security

Android 15 includes changes that promote system security to help protect apps
and users from malicious apps.

### Restricted TLS versions

Android 15 restricts the usage of TLS versions 1.0 and 1.1. These versions had
previously been deprecated in Android, but are now disallowed for apps targeting
Android 15.

### Secured background activity launches

Android 15 protects users from malicious apps and gives them more control over
their devices by adding changes that prevent malicious background apps from
bringing other apps to the foreground, elevating their privileges, and abusing
user interaction. Background activity launches have been restricted since
Android 10 (API level 29).

#### Other changes

- **Change `PendingIntent` creators to [block background activity launches](https://developer.android.com/guide/components/activities/background-starts) by
  default** . This helps prevent apps from accidentally creating a `PendingIntent` that could be abused by malicious actors.
- **Don't bring an app to the foreground unless the `PendingIntent` sender
  allows it**. This change aims to prevent malicious apps from abusing the ability to start activities in the background. By default, apps are not allowed to bring the task stack to the foreground unless the creator allows background activity launch privileges or the sender has background activity launch privileges.
- **Control how the top activity of a task stack can finish its task**. If the top activity finishes a task, Android will go back to whichever task was last active. Moreover, if a non-top activity finishes its task, Android will go back to the home screen; it won't block the finish of this non-top activity.
- **Prevent launching arbitrary activities from other apps into your own
  task**. This change prevents malicious apps from phishing users by creating activities that appear to be from other apps.
- **Block non-visible windows from being considered for background activity
  launches**. This helps prevent malicious apps from abusing background activity launches to display unwanted or malicious content to users.

### Safer intents

Android 15 introduces [`StrictMode`](https://developer.android.com/reference/android/os/StrictMode) for
intents.

In order to see detailed logs about `Intent` usage violations, use following
method:

### Kotlin

```kotlin
fun onCreate() {
    StrictMode.setVmPolicy(VmPolicy.Builder()
        .detectUnsafeIntentLaunch()
        .build()
    )
}
```

### Java

```java
public void onCreate() {
    StrictMode.setVmPolicy(new VmPolicy.Builder()
            .detectUnsafeIntentLaunch()
            .build());
}
```

## User experience and system UI

Android 15 includes some changes that are intended to create a more consistent,
intuitive user experience.

### Window inset changes

There are two changes related to window insets in Android 15: edge-to-edge is
enforced by default, and there are also configuration changes, such as the
default configuration of system bars.

#### Edge-to-edge enforcement

Apps are edge-to-edge by default on devices running Android 15 if the app is
targeting Android 15 (API level 35).

> [!IMPORTANT]
> **Important:** If your app is not already edge-to-edge, portions of your app may be obscured and you must handle insets. Depending on the app, this work may or may not be significant. The Material 3 [`Scaffold`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#Scaffold(androidx.compose.foundation.layout.WindowInsets,androidx.compose.ui.Modifier,androidx.compose.material.ScaffoldState,kotlin.Function0,kotlin.Function0,kotlin.Function1,kotlin.Function0,androidx.compose.material.FabPosition,kotlin.Boolean,kotlin.Function1,kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.compose.ui.unit.Dp,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,kotlin.Function1)) component can reduce the work required to be compatible with the Android 15 edge-to-edge enforcement.

![](https://developer.android.com/static/about/versions/15/images/edge-to-edge-1.png) An app that targets Android 14 and is not edge-to-edge on an Android 15 device.

<br />

An app that targets Android 15 (API level 35) and is edge-to-edge on an Android 15 device. This app mostly uses Material 3 Compose Components that automatically apply insets. This screen is not negatively impacted by the Android 15 edge-to-edge enforcement.

This is a breaking change that might negatively impact your app's UI. The
changes affect the following UI areas:

- **Gesture handle navigation bar**
  - Transparent by default.
  - Bottom offset is disabled so content draws behind the system navigation bar unless insets are applied.
  - [`setNavigationBarColor`](https://developer.android.com/reference/android/view/Window#setNavigationBarColor(int)) and `R.attr#navigationBarColor` are deprecated and don't affect gesture navigation.
  - [`setNavigationBarContrastEnforced`](https://developer.android.com/reference/android/view/Window#setNavigationBarContrastEnforced(boolean)) and `R.attr#navigationBarContrastEnforced` continue to have no effect on gesture navigation.
- **3-button navigation**
  - Opacity set to 80% by default, with color possibly matching the window background.
  - Bottom offset disabled so content draws behind the system navigation bar unless insets are applied.
  - [`setNavigationBarColor`](https://developer.android.com/reference/android/view/Window#setNavigationBarColor(int)) and `R.attr#navigationBarColor` are set to match the window background by default. The window background must be a color drawable for this default to apply. This API is deprecated but continues to affect 3-button navigation.
  - [`setNavigationBarContrastEnforced`](https://developer.android.com/reference/android/view/Window#setNavigationBarContrastEnforced(boolean)) and `R.attr#navigationBarContrastEnforced` is true by default, which adds an 80% opaque background across 3-button navigation.
- **Status bar**
  - Transparent by default.
  - The top offset is disabled so content draws behind the status bar unless insets are applied.
  - [`setStatusBarColor`](https://developer.android.com/reference/android/view/Window#setStatusBarColor(int)) and `R.attr#statusBarColor` are deprecated and have no effect on Android 15.
  - [`setStatusBarContrastEnforced`](https://developer.android.com/reference/android/view/Window#setStatusBarContrastEnforced(boolean)) and `R.attr#statusBarContrastEnforced` are deprecated but still have an effect on Android 15.
- **Display cutout**
  - `layoutInDisplayCutoutMode` of non-floating windows must be `LAYOUT_IN_DISPLAY_CUTOUT_MODE_ALWAYS`. `SHORT_EDGES`, `NEVER`, and `DEFAULT` are interpreted as `ALWAYS` so that users don't see a black bar caused by the display cutout and appear edge-to-edge.

The following example shows an app before and after targeting
Android 15 (API level 35), and before and after applying insets. This example is
not comprehensive, this might appear differently on Android Auto.
![](https://developer.android.com/static/about/versions/15/images/edge-to-edge-4.png) An app that targets Android 14 and is not edge-to-edge on an Android 15 device. ![](https://developer.android.com/static/about/versions/15/images/edge-to-edge-6.png) An app that targets Android 15 (API level 35) and is edge-to-edge on an Android 15 device. However, many elements are now hidden by the status bar, 3-button navigation bar, or display cutout due to the Android 15 edge-to-edge enforcements. Hidden UI includes the Material 2 top app bar, floating action buttons, and list items. ![](https://developer.android.com/static/about/versions/15/images/edge-to-edge-2.png) An app that targets Android 15 (API level 35), is edge to edge on an Android 15 device and applies insets so that UI is not hidden.

##### What to check if your app is already edge-to-edge

If your app is already [edge-to-edge](https://developer.android.com/develop/ui/compose/layouts/insets) and applies insets, you are
mostly unimpacted, except in the following scenarios. However, even if you think
you aren't impacted, we recommend you test your app.

- You have a non-floating window, such as an `Activity` that uses `SHORT_EDGES`, `NEVER` or `DEFAULT` instead of `LAYOUT_IN_DISPLAY_CUTOUT_MODE_ALWAYS`. If your app crashes on launch, this might be due to your splashscreen. You can either upgrade the [core
  splashscreen](https://developer.android.com/jetpack/androidx/releases/core#core_splashscreen_version_12_2) dependency to 1.2.0-alpha01 or later or set `window.attributes.layoutInDisplayCutoutMode =
  WindowManager.LayoutInDisplayCutoutMode.always`.
- There might be lower-traffic screens with occluded UI. Verify these less-visited screens don't have occluded UI. Lower-traffic screens include:
  - Onboarding or sign-in screens
  - Settings pages

##### What to check if your app is not already edge-to-edge

If your app is not already edge-to-edge, you are most likely impacted. In
addition to the scenarios for apps that are already edge-to-edge, you should
consider the following:

- If your app uses Material 3 Components ( [`androidx.compose.material3`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary)) in compose, such as `TopAppBar`, `BottomAppBar`, and `NavigationBar`, these components are likely *not* impacted because they automatically handle insets.
- If your app is using Material 2 Components ( [`androidx.compose.material`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary)) in Compose, these components don't automatically handle insets. However, you can get access to the insets and apply them manually. In [androidx.compose.material 1.6.0](https://developer.android.com/jetpack/androidx/releases/compose-material#1.6.0-alpha03) and later, use the `windowInsets` parameter to apply the insets manually for [`BottomAppBar`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#BottomAppBar(androidx.compose.foundation.layout.WindowInsets,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Shape,androidx.compose.ui.unit.Dp,androidx.compose.foundation.layout.PaddingValues,kotlin.Function1)), [`TopAppBar`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#TopAppBar(androidx.compose.foundation.layout.WindowInsets,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.Dp,androidx.compose.foundation.layout.PaddingValues,kotlin.Function1)), [`BottomNavigation`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#BottomNavigation(androidx.compose.foundation.layout.WindowInsets,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.Dp,kotlin.Function1)), and [`NavigationRail`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#NavigationRail(androidx.compose.foundation.layout.WindowInsets,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.Dp,kotlin.Function1,kotlin.Function1)). Likewise, use the `contentWindowInsets` parameter for [`Scaffold`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#Scaffold(androidx.compose.foundation.layout.WindowInsets,androidx.compose.ui.Modifier,androidx.compose.material.ScaffoldState,kotlin.Function0,kotlin.Function0,kotlin.Function1,kotlin.Function0,androidx.compose.material.FabPosition,kotlin.Boolean,kotlin.Function1,kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.compose.ui.unit.Dp,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,kotlin.Function1)).
- If your app uses views and Material Components ([`com.google.android.material`](https://developer.android.com/reference/com/google/android/material/classes)), most views-based Material Components such as `BottomNavigationView`, `BottomAppBar`, `NavigationRailView`, or `NavigationView`, handle insets and require no additional work. However, you need to add `android:fitsSystemWindows="true"` if using `AppBarLayout`.
- For custom composables, apply the insets manually as padding. If your content is within a `Scaffold`, you can consume insets using the [`Scaffold`
  padding values](https://developer.android.com/develop/ui/compose/layouts/insets#scaffold). Otherwise, apply padding using one of the [`WindowInsets`](https://developer.android.com/develop/ui/compose/layouts/insets#inset-fundamentals).
- If your app is using views and `BottomSheet`, `SideSheet` or custom containers, apply padding using [`ViewCompat.setOnApplyWindowInsetsListener`](https://developer.android.com/develop/ui/views/layout/edge-to-edge#handle-overlaps). For `RecyclerView`, apply padding using this listener and also add `clipToPadding="false"`.

##### What to check if your app must offer custom background protection

If your app must offer custom background protection to 3-button navigation or
the status bar, your app should place a composable or view behind the system bar
using [`WindowInsets.Type#tappableElement()`](https://developer.android.com/reference/android/view/WindowInsets.Type#tappableElement()) to get the 3-button
navigation bar height or [`WindowInsets.Type#statusBars`](https://developer.android.com/reference/android/view/WindowInsets.Type#statusBars()).

##### Additional edge-to-edge resources

See the [Edge to Edge Views](https://developer.android.com/develop/ui/views/layout/edge-to-edge) and [Edge to Edge Compose](https://developer.android.com/develop/ui/compose/layouts/insets)
guides for additional considerations on applying insets.

##### Deprecated APIs

The following APIs are deprecated but not disabled:

- [`R.attr#enforceStatusBarContrast`](https://developer.android.com/reference/android/R.attr#enforceStatusBarContrast)
- [`R.attr#navigationBarColor`](https://developer.android.com/reference/android/R.attr#navigationBarColor) (for 3 button navigation, with 80% alpha)
- [`Window#isStatusBarContrastEnforced`](https://developer.android.com/reference/android/view/Window#isStatusBarContrastEnforced())
- [`Window#setNavigationBarColor`](https://developer.android.com/reference/android/view/Window#setNavigationBarColor(int)) (for 3 button navigation, with 80% alpha)
- [`Window#setStatusBarContrastEnforced`](https://developer.android.com/reference/android/view/Window#setStatusBarContrastEnforced(boolean))

The following APIs are deprecated and disabled:

- [`R.attr#navigationBarColor`](https://developer.android.com/reference/android/R.attr#navigationBarColor) (for gesture navigation)
- [`R.attr#navigationBarDividerColor`](https://developer.android.com/reference/android/R.attr#navigationBarDividerColor)
- [`R.attr#statusBarColor`](https://developer.android.com/reference/android/R.attr#statusBarColor)
- [`Window#setDecorFitsSystemWindows`](https://developer.android.com/reference/android/view/Window#setDecorFitsSystemWindows(boolean))
- [`Window#getNavigationBarColor`](https://developer.android.com/reference/android/view/Window#getNavigationBarColor())
- [`Window#getNavigationBarDividerColor`](https://developer.android.com/reference/android/view/Window#getNavigationBarDividerColor())
- [`Window#getStatusBarColor`](https://developer.android.com/reference/android/view/Window#getStatusBarColor())
- [`Window#setNavigationBarColor`](https://developer.android.com/reference/android/view/Window#setNavigationBarColor(int)) (for gesture navigation)
- [`Window#setNavigationBarDividerColor`](https://developer.android.com/reference/android/view/Window#setNavigationBarDividerColor(int))
- [`Window#setStatusBarColor`](https://developer.android.com/reference/android/view/Window#setStatusBarColor(int))

#### Stable configuration

If your app targets Android 15 (API level 35) or higher, `Configuration` no
longer excludes the system bars. If you use the screen size in the
`Configuration` class for layout calculation, you should replace it with better
alternatives like an appropriate `ViewGroup`, `WindowInsets`, or
`WindowMetricsCalculator` depending on your need.

`Configuration` has been available since API 1. It is typically obtained from
`Activity.onConfigurationChanged`. It provides information like window density,
orientation, and sizes. One important characteristic about the window sizes
returned from `Configuration` is that it previously excluded the system bars.

The configuration size is typically used for resource selection, such as
`/res/layout-h500dp`, and this is still a valid use case. However, using it for
layout calculation has always been discouraged. If you do so, you should move
away from it now. You should replace the use of `Configuration` with something
more suitable depending on your use case.

If you use it to calculate the layout, use an appropriate `ViewGroup`, such as
`CoordinatorLayout` or `ConstraintLayout`. If you use it to determine the height
of the system navbar, use `WindowInsets`. If you want to know the current size
of your app window, use `computeCurrentWindowMetrics`.

The following list describes the fields affected by this change:

- [`Configuration.screenWidthDp`](https://developer.android.com/reference/android/content/res/Configuration#screenWidthDp) and [`screenHeightDp`](https://developer.android.com/reference/android/content/res/Configuration#screenHeightDp) sizes no longer exclude the system bars.
- [`Configuration.smallestScreenWidthDp`](https://developer.android.com/reference/android/content/res/Configuration#smallestScreenWidthDp) is indirectly affected by changes to `screenWidthDp` and `screenHeightDp`.
- [`Configuration.orientation`](https://developer.android.com/reference/android/content/res/Configuration#orientation) is indirectly affected by changes to `screenWidthDp` and `screenHeightDp` on close-to-square devices.
- [`Display.getSize(Point)`](https://developer.android.com/reference/android/view/Display#getSize(android.graphics.Point)) is indirectly affected by the changes in `Configuration`. This was deprecated beginning in API level 30.
- `Display.getMetrics()` has already worked like this since API level 33.

### elegantTextHeight attribute defaults to true

For apps targeting Android 15 (API level 35), the
[`elegantTextHeight`](https://developer.android.com/reference/android/R.attr#elegantTextHeight) [`TextView`](https://developer.android.com/reference/android/widget/TextView) attribute
becomes `true` by default, replacing the compact font used by default with some
scripts that have large vertical metrics with one that is much more readable.
The compact font was introduced to prevent breaking layouts; Android 13 (API
level 33) prevents many of these breakages by allowing the text layout to
stretch the vertical height utilizing the [`fallbackLineSpacing`](https://developer.android.com/reference/android/widget/TextView#attr_android:fallbackLineSpacing)
attribute.

In Android 15, the compact font still remains in the system, so your app can set
`elegantTextHeight` to `false` to get the same behavior as before, but it is
unlikely to be supported in upcoming releases. So, if your app supports the
following scripts: Arabic, Lao, Myanmar, Tamil, Gujarati, Kannada, Malayalam,
Odia, Telugu or Thai, test your app by setting `elegantTextHeight` to `true`.
![](https://developer.android.com/static/about/versions/15/images/elegant-text-height-before.png) `elegantTextHeight` behavior for apps targeting Android 14 (API level 34) and lower. ![](https://developer.android.com/static/about/versions/15/images/elegant-text-height-after.png) `elegantTextHeight` behavior for apps targeting Android 15.

### TextView width changes for complex letter shapes

In previous versions of Android, some cursive fonts or languages that have
complex shaping might draw the letters in the previous or next character's area.
In some cases, such letters were clipped at the beginning or ending position.
Starting in Android 15, a `TextView` allocates width for drawing enough space
for such letters and allows apps to request extra paddings to the left to
prevent clipping.

Because this change affects how a `TextView` decides the width, `TextView`
allocates more width by default if the app targets Android 15 (API level 35) or
higher. You can enable or disable this behavior by calling the
`setUseBoundsForWidth` API on `TextView`.

Because adding left padding might cause a misalignment for existing layouts, the
padding is not added by default even for apps that target Android 15 or higher.
However, you can add extra padding to preventing clipping by calling
`setShiftDrawingOffsetForStartOverhang`.

The following examples show how these changes can improve text layout for some
fonts and languages.
![](https://developer.android.com/static/about/versions/15/images/cursive-clipped.png) Standard layout for English text in a cursive font. Some of the letters are clipped. Here is the corresponding XML:  

```xml
<TextView
    android:fontFamily="cursive"
    android:text="java" />
```
![](https://developer.android.com/static/about/versions/15/images/cursive-noclipping.png) Layout for the same English text with additional width and padding. Here is the corresponding XML:  

```xml
<TextView
    android:fontFamily="cursive"
    android:text="java"
    android:useBoundsForWidth="true"
    android:shiftDrawingOffsetForStartOverhang="true" />
```
![](https://developer.android.com/static/about/versions/15/images/thai-clipped.png) Standard layout for Thai text. Some of the letters are clipped. Here is the corresponding XML:  

```xml
<TextView
    android:text="คอมพิวเตอร์" />
```
![](https://developer.android.com/static/about/versions/15/images/thai-noclipping.png) Layout for the same Thai text with additional width and padding. Here is the corresponding XML:  

```xml
<TextView
    android:text="คอมพิวเตอร์"
    android:useBoundsForWidth="true"
    android:shiftDrawingOffsetForStartOverhang="true" />
```

### Locale-aware default line height for EditText

In previous versions of Android, the text layout stretched the height of the
text to meet the line height of the font that matched the current locale. For
example, if the content was in Japanese, because the line height of the Japanese
font is slightly larger than the one of a Latin font, the height of the text
became slightly larger. However, despite these differences in line heights, the
[`EditText`](https://developer.android.com/reference/android/widget/EditText) element was sized uniformly, regardless
of the locale being used, as illustrated in the following image:
![](https://developer.android.com/static/about/versions/15/images/locale-aware-line-height-before.png) Three boxes representing `EditText` elements that can contain text from English (en), Japanese (ja), and Burmese (my). The height of the `EditText` is the same, even though these languages have different line heights from each other.

For apps targeting Android 15 (API level 35), a minimum line height is now
reserved for `EditText` to match the reference font for the specified Locale, as
shown in the following image:
![](https://developer.android.com/static/about/versions/15/images/locale-aware-line-height-after.png) Three boxes representing `EditText` elements that can contain text from English (en), Japanese (ja), and Burmese (my). The height of the `EditText` now includes space to accommodate the default line height for these languages' fonts.

If needed, your app can restore the previous behavior by specifying the
[`useLocalePreferredLineHeightForMinimum`](https://developer.android.com/reference/android/R.attr#useLocalePreferredLineHeightForMinimum) attribute
to `false`, and your app can set custom minimum vertical metrics using the
[`setMinimumFontMetrics`](https://developer.android.com/reference/android/text/DynamicLayout.Builder#setMinimumFontMetrics(android.graphics.Paint.FontMetrics)) API in Kotlin and Java.

## Camera and media

Android 15 makes the following changes to camera and media behavior for apps
that target Android 15 or higher.

### Restrictions on requesting audio focus

Apps that target Android 15 (API level 35) must be the top app or running a
foreground service in order to [request audio focus](https://developer.android.com/reference/android/media/AudioManager#requestAudioFocus(android.media.AudioFocusRequest)). If an app
attempts to request focus when it does not meet one of these requirements, the
call returns [`AUDIOFOCUS_REQUEST_FAILED`](https://developer.android.com/reference/android/media/AudioManager#AUDIOFOCUS_REQUEST_FAILED).

You can learn more about audio focus at [Manage audio focus](https://developer.android.com/media/optimize/audio-focus).

## Updated non-SDK restrictions

Android 15 includes updated lists of restricted non-SDK
interfaces based on collaboration with Android developers and the latest
internal testing. Whenever possible, we make sure that public alternatives are
available before we restrict non-SDK interfaces.

If your app does not target Android 15, some of these changes
might not immediately affect you. However, while it's possible for your app to
access some non-SDK interfaces
[depending on your app's target API level](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces#list-names)), using any non-SDK
method or field always carries a high risk of breaking your app.

If you are unsure if your app uses non-SDK interfaces, you can
[test your app](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces#test-for-non-sdk) to find out. If your app relies on non-SDK
interfaces, you should begin planning a migration to SDK alternatives.
Nevertheless, we understand that some apps have valid use cases for using
non-SDK interfaces. If you can't find an alternative to using a non-SDK
interface for a feature in your app, you should
[request a new public API](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces#feature-request).

To learn more about the changes in this release of Android, see [Updates to
non-SDK interface restrictions in Android 15](https://developer.android.com/about/versions/15/changes/non-sdk-15). To learn more
about non-SDK interfaces generally, see
[Restrictions on non-SDK interfaces](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces).