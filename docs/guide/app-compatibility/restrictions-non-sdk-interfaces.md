---
title: https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces
url: https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces
source: md.txt
---

Starting in Android 9 (API level 28), the platform restricts which non-SDK
interfaces your app can use. These restrictions apply whenever an app references
a non-SDK interface or attempts to obtain its handle using reflection or JNI.
These restrictions were put in place to help improve the user and developer
experience and reduce the risks of crashes for users and emergency rollouts for
developers. For more information about this decision, see [Improving Stability
by Reducing Usage of non-SDK Interfaces](https://android-developers.googleblog.com/2018/02/improving-stability-by-reducing-usage.html).

## Differentiate between SDK and non-SDK interfaces

Generally speaking, public SDK interfaces are those ones found documented in the
Android framework [Package Index](https://developer.android.com/reference/packages). Handling of non-SDK interfaces is an
implementation detail that the API abstracts away, so these interfaces are
subject to change without notice.

To avoid crashes and unexpected behavior, apps should only use the officially
documented parts of the classes in the SDK. This also means that you shouldn't
access methods or fields that are not listed in the SDK when you interact with a
class using mechanisms such as reflection.

### Non-SDK API lists

With each release of Android, additional non-SDK interfaces are restricted. We
know these restrictions can impact your release workflow, and we want to make
sure you have the tools to detect usage of non-SDK interfaces, an opportunity to
[give us feedback](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces#feature-request), and time to plan and adjust to the new policies.

To minimize the impact of non-SDK restrictions on your development workflow, the
non-SDK interfaces are divided into lists that define how tightly their use is
restricted, depending on which API level is being targeted. The following table
describes each of these lists:

| List | Code tags | Description |
|---|---|---|
| Blocklist | - `blocked` - Deprecated: `blacklist` | Non-SDK interfaces that you cannot use regardless of your app's [target API level](https://developer.android.com/distribute/best-practices/develop/target-sdk). If your app attempts to access one of these interfaces, the system [throws an error](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces#results-of-keeping-non-sdk). |
| Conditionally blocked | - `max-target-x` - Deprecated: `greylist-max-x` | Starting with Android 9 (API level 28), each API level has non-SDK interfaces that are restricted when an app targets that API level. These lists are labelled by the maximum API level (`max-target-x`) that an app can target before the app can no longer access the non-SDK interfaces in that list. For example, a non-SDK interface that was not blocked in Android Pie but is now blocked in Android 10 is part of the `max-target-p` (`greylist-max-p`) list, where "p" stands for Pie or Android 9 (API level 28). If your app attempts to access an interface that is restricted for your target API level, the system [behaves as if the API is part of the blocklist](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces#results-of-keeping-non-sdk). |
| Unsupported | - `unsupported` - Deprecated: `greylist` | Non-SDK interfaces that are unrestricted and your app can use. Note however, that these interfaces are **unsupported** and subject to change without notice. Expect these interfaces to be conditionally blocked in future Android versions in a `max-target-x` list. |
| SDK | - Both `public-api` and `sdk` - Deprecated: Both `public-api` and `whitelist` | Interfaces that can be freely used and are now supported as part of the officially documented Android framework [Package Index](https://developer.android.com/reference/packages). |
| Test APIs | - `test-api` | Interfaces that are used for internal system testing, such as APIs that facilitate testing through the Compatibility Test Suite (CTS). Test APIs are **not** part of the SDK. [Starting in Android 11 (API level 30)](https://developer.android.com/about/versions/11/non-sdk-11#test-api-restrictions), test APIs are included in the blocklist, so apps aren't allowed to use them regardless of their target API level. All test APIs are unsupported and subject to change without notice, regardless of the platform API level. |

While you can use some non-SDK interfaces (depending on your app's target API
level), using any non-SDK method or field always carries a high risk of breaking
your app. If your app relies on non-SDK interfaces, you should begin planning a
migration to SDK interfaces or other alternatives. If you cannot find an
alternative to using a non-SDK interface for a feature in your app, you should
[request a new public API](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces#feature-request).

### Determine which list an interface belongs to

The lists of non-SDK interfaces are built as part of the platform. See the
following sections for information about each Android release.

#### Android 16

For Android 16 (API level 36), you can download the following file that
describes all of the non-SDK interfaces and their corresponding lists:

File: [`hiddenapi-flags.csv`](https://dl.google.com/developers/android/baklava/non-sdk/hiddenapi-flags.csv)

SHA-256 checksum:
`9102af02fe6ab68b92464bdff5e5b09f3bd62c65d1130aaf85d3296f17d38074`

To learn more about the non-SDK API list changes in Android 16,
see [Updates to non-SDK interface restrictions in
Android 16](https://developer.android.com/about/versions/16/changes/non-sdk-16).

#### Android 15

For Android 15 (API level 35), you can download the following file that describes
all of the non-SDK interfaces and their corresponding lists:

File: [`hiddenapi-flags.csv`](https://dl.google.com/developers/android/vic/non-sdk/hiddenapi-flags.csv)

SHA-256 checksum:
`40134e205e58922a708c453726b279a296e6a1f34a988abd90cec0f3432ea5a9`

To learn more about the non-SDK API list changes in Android 15,
see [Updates to non-SDK interface restrictions in Android 15](https://developer.android.com/about/versions/15/changes/non-sdk-15).

#### Android 14

For Android 14 (API level 34), you can download the following file that describes
all of the non-SDK interfaces and their corresponding lists:

File: [`hiddenapi-flags.csv`](https://dl.google.com/developers/android/udc/non-sdk/hiddenapi-flags.csv)

SHA-256 checksum:
`7e00db074cbe51c51ff4b411f7b48e98692951395c5c17d069c822cc1d0eae0f`

To learn more about the non-SDK API list changes in Android 14,
see [Updates to non-SDK interface restrictions in Android 14](https://developer.android.com/about/versions/14/changes/non-sdk-14).

#### Android 13

For Android 13 (API level 33), you can download the following file that describes
all of the non-SDK interfaces and their corresponding lists:

File: [`hiddenapi-flags.csv`](https://dl.google.com/developers/android/tm/non-sdk/hiddenapi-flags.csv)

SHA-256 checksum:
`233a277aa8ac475b6df61bffd95665d86aac6eb2ad187b90bf42a98f5f2a11a3`

To learn more about the non-SDK API list changes in Android 13,
including suggested public API alternatives for APIs that are conditionally
blocked in Android 13, see [Updates to non-SDK interface
restrictions in Android 13](https://developer.android.com/about/versions/13/changes/non-sdk-13).

#### Android 12

For Android 12 (API level 31), you can download the following file that describes
all of the non-SDK interfaces and their corresponding lists:

File: [`hiddenapi-flags.csv`](https://dl.google.com/developers/android/sc/non-sdk/hiddenapi-flags.csv)

SHA-256 checksum:
`40674ff4291eb268f86561bf687e69dbd013df9ec9531a460404532a4ac9a761`

To learn more about the non-SDK API list changes in Android 12,
including suggested public API alternatives for APIs that are conditionally
blocked in Android 12, see [List changes for
Android 12](https://developer.android.com/about/versions/12/non-sdk-12#list-changes).

#### Android 11

For Android 11 (API level 30), you can download the following file that
describes all of the non-SDK interfaces and their corresponding lists:

File: [`hiddenapi-flags.csv`](https://dl.google.com/developers/android/rvc/non-sdk/hiddenapi-flags.csv)

SHA-256 checksum:
`a19d839f4f61dc9c94960ae977b2e0f3eb30f880ba1ffe5108e790010b477a56`

To learn more about the non-SDK API list changes in Android 11, including
suggested public API alternatives for APIs that are conditionally blocked in
Android 11, see [List changes for Android 11](https://developer.android.com/about/versions/11/non-sdk-11#r-list-changes).

#### Android 10

For Android 10 (API level 29), you can download the following file that
describes all of the non-SDK interfaces and their corresponding lists:

File: [`hiddenapi-flags.csv`](https://dl.google.com/developers/android/qt/non-sdk/hiddenapi-flags.csv)

SHA-256 checksum:
`f22a59c215e752777a114bd9b07b0b6b4aedfc8e49e6efca0f99681771c5bfeb`

To learn more about the non-SDK API list changes in Android 10, including
suggested public API alternatives for APIs that are conditionally blocked in
Android 10, see [List changes for Android 10](https://developer.android.com/about/versions/10/non-sdk-q#q-list-changes).

#### Android 9

For Android 9 (API level 28), the following text file contains the list of
non-SDK APIs that are not restricted (greylisted):
[`hiddenapi-light-greylist.txt`](https://android.googlesource.com/platform/frameworks/base/+/pie-release/config/hiddenapi-light-greylist.txt).

The blocklist (`blacklist`) and list of conditionally blocked APIs (darkgrey
list) are derived at build time.

#### Generate lists from AOSP

When working with AOSP, you can generate a `hiddenapi-flags.csv` file that
contains all of the non-SDK interfaces and their corresponding lists. To do so,
[download the AOSP source](https://source.android.com/setup/build/downloading) and then run the following command:  

```
m out/soong/hiddenapi/hiddenapi-flags.csv
```

You can then find the file in the following location:  

    out/soong/hiddenapi/hiddenapi-flags.csv

### Expected behavior when restricted non-SDK interfaces are accessed

The following table describes the behavior that you can expect if your app
attempts to access a non-SDK interface that is part of the blocklist.

| Means of access | Result |
|---|---|
| Dalvik instruction referencing a field | `NoSuchFieldError` thrown |
| Dalvik instruction referencing a method | `NoSuchMethodError` thrown |
| Reflection using `Class.getDeclaredField()` or `Class.getField()` | `NoSuchFieldException` thrown |
| Reflection using `Class.getDeclaredMethod()`, `Class.getMethod()` | `NoSuchMethodException` thrown |
| Reflection using `Class.getDeclaredFields()`, `Class.getFields()` | Non-SDK members not in results |
| Reflection using `Class.getDeclaredMethods()`, `Class.getMethods()` | Non-SDK members not in results |
| JNI using `env->GetFieldID()` | `NULL` returned, `NoSuchFieldError` thrown |
| JNI using `env->GetMethodID()` | `NULL` returned, `NoSuchMethodError` thrown |

## Test your app for non-SDK interfaces

There are several methods that you can use to test for non-SDK interfaces in
your app.

### Test using a debuggable app

You can test for non-SDK interfaces by building and running a
[debuggable app](https://developer.android.com/studio/debug#enable-debug) on a device or emulator running Android 9 (API level 28) or
higher. Make sure that the device or emulator that you are using matches the
[target API level](https://developer.android.com/distribute/best-practices/develop/target-sdk) of your app.

While running through tests on your app, the system prints a log message if your
app accesses certain non-SDK interfaces. You can inspect your app's log messages
to find the following details:

- The declaring class, name, and type (in the format that is used by the Android runtime).
- The means of access: either linking, using reflection, or using JNI.
- Which list the non-SDK interface belongs to.

You can use `adb logcat` to access these log messages, which appear under the
PID of the running app. For example, an entry in the log might read as follows:  

    Accessing hidden field Landroid/os/Message;->flags:I (light greylist, JNI)

### Test using the StrictMode API

You can also test for non-SDK interfaces by using the `StrictMode` API. Use the
[`detectNonSdkApiUsage`](https://developer.android.com/reference/android/os/StrictMode.VmPolicy.Builder#detectNonSdkApiUsage()) method to enable this. After enabling the
`StrictMode` API, you can receive a callback for each usage of a non-SDK
interface by using a [`penaltyListener`](https://developer.android.com/reference/android/os/StrictMode.VmPolicy.Builder#penaltyListener(java.util.concurrent.Executor,%20android.os.StrictMode.OnVmViolationListener)), where you can implement custom
handling. The `Violation` object provided in the callback derives from
`Throwable`, and the enclosed stack trace provides the context of the usage.

### Test using the Android Studio lint tool

Whenever you build your app in Android Studio, the [lint tool](https://developer.android.com/studio/write/lint) inspects your
code for potential issues. If your app uses non-SDK interfaces, you might see
build errors or warnings, depending on [which list](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces#list-names) those interfaces belong
to.

You can also [run the lint tool from the command line](https://developer.android.com/studio/write/lint#commandline) or [run inspections
manually](https://developer.android.com/studio/write/lint#manuallyRunInspections) on a specific project, folder, or file.

### Test using the Play Console

When you upload your app to a [testing track](https://support.google.com/googleplay/android-developer/answer/3131213) in the Play Console, your app
is automatically tested for potential issues and a pre-launch report is
generated. If your app uses non-SDK interfaces, an error or warning displays in
the pre-launch report, depending on [which list](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces#list-names) those interfaces belong to.

For more information, see the Android Compatibility section in [Use pre-launch
reports to identify issues](https://support.google.com/googleplay/android-developer/answer/7002270).

## Request a new public API

If you cannot find an alternative to using a non-SDK interface for a feature in
your app, you can request a new public API by [creating a feature request](https://issuetracker.google.com/issues/new?component=328403&template=1027267)
in our issue tracker.

When creating a feature request, provide the following information:

- Which unsupported API you are using, including the full descriptor seen in the `Accessing hidden ...` logcat message.
- Why you need to use these APIs, including details about the high-level feature that the API is necessary for, not just low level details.
- Why any related public SDK APIs are insufficient for your purposes.
- Any other alternatives you have tried and why these didn't work out.

When you provide these details in your feature request, you increase the
likelihood that a new public API will be granted.

## Other questions

This section includes some answers to other questions that developers have
frequently asked:

### General questions

#### How can Google be sure they can capture the needs of all apps through the issuetracker?

We created the initial lists for Android 9 (API level 28) through static
analysis of apps that was supplemented using the following methods:

- manual testing of top Play and non-Play apps
- internal reports
- automatic data collection from internal users
- developer preview reports
- additional static analysis that was designed to conservatively include more false positives

As we evaluate the lists for each new release, we take into account API usage as
well as developer feedback through the issue tracker.

#### How can I enable access to non-SDK interfaces?

You can enable access to non-SDK interfaces on development devices by using adb
commands to change the API enforcement policy. The commands that you use vary,
depending on the API level. These commands don't require a rooted device.

Android 10 (API level 29) or higher

:   To enable access, use the following adb

    command:  

    ```
    adb shell settings put global hidden_api_policy  1
    ```

    To reset the API enforcement policy to the default settings, use the
    following command:  

    ```
    adb shell settings delete global hidden_api_policy
    ```

Android 9 (API level 28)

:   To enable access, use the following adb commands:

        adb shell settings put global hidden_api_policy_pre_p_apps  1
        adb shell settings put global hidden_api_policy_p_apps 1

    To reset the API enforcement policy to the default settings, use the
    following commands:  

        adb shell settings delete global hidden_api_policy_pre_p_apps
        adb shell settings delete global hidden_api_policy_p_apps

You can set the integer in the API enforcement policy to one of the following
values:

- 0: Disable all detection of non-SDK interfaces. Using this setting disables all log messages for non-SDK interface usage and prevents you from testing your app [using the `StrictMode` API](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces#test-strictmode-api). This setting is not recommended.
- 1: Enable access to all non-SDK interfaces, but print log messages with warnings for any non-SDK interface usage. Using this setting also lets you test your app [using the `StrictMode` API](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces#test-strictmode-api).
- 2: Disallow usage of non-SDK interfaces that belong to the blocklist or are conditionally blocked for your [target API level](https://developer.android.com/distribute/best-practices/develop/target-sdk).

### Questions about non-SDK interface lists

#### Where can I find the non-SDK API lists in the system image?

They are encoded in the field and method access flag bits in platform dex files.
There is no separate file in the system image that contains these lists.

#### Are the non-SDK API lists the same on different OEM devices with the same Android versions?

OEMs can add their own interfaces to the blocklist (blacklist), but they cannot
remove interfaces from the AOSP non-SDK API lists. The CDD prevents such changes
and CTS tests ensure that the Android Runtime is enforcing the list.

### Questions about the compatibility of related apps

#### Is there any restriction on non-NDK interfaces in native code?

The Android SDK includes Java interfaces. The platform started restricting
access to non-NDK interfaces for native C/C++ code in Android 7 (API level 26).
For more information, see [Improving Stability with Private C/C++ Symbol
Restrictions in Android N](https://android-developers.googleblog.com/2016/06/improving-stability-with-private-cc.html).

#### Is there any plan to restrict dex2oat or DEX file manipulation?

We don't have active plans to restrict access to the dex2oat binary, but we
don't intend for the DEX file format to be stable or a public interface beyond
the portions that are publicly specified in the [Dalvik Executable format](https://source.android.com/devices/tech/dalvik/dex-format).
We reserve the right to modify or eliminate dex2oat and the unspecified portions
of the DEX format at any time. Also note that derived files produced by dex2oat
such as ODEX (also known as OAT), VDEX, and CDEX are all unspecified formats.

#### What if a crucial third-party SDK (for example, an obfuscator) cannot avoid using non-SDK interfaces, but does commit to maintain compatibility with future Android versions? Can Android waive its compatibility requirements in this case?

We don't have plans to waive compatibility requirements on a per-SDK basis. If
an SDK developer can only maintain compatibility by depending on interfaces in
the unsupported (formerly grey) lists, they should begin planning a migration to
SDK interfaces or other alternatives, and [request a new public API](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces#feature-request) whenever
they cannot find an alternative to using a non-SDK interface.

#### Do non-SDK interface restrictions apply to all apps including system and first-party apps, not just third-party apps?

Yes, however, we exempt apps signed with the platform key and some system image
apps. Note that these exemptions only apply to apps that are part of the system
image (or updated system image apps). The list is intended only for apps that
build against the private platform APIs, rather than the SDK APIs (where
`LOCAL_PRIVATE_PLATFORM_APIS := true`).