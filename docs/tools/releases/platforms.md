---
title: https://developer.android.com/tools/releases/platforms
url: https://developer.android.com/tools/releases/platforms
source: md.txt
---

This page provides release information about the SDK packages available for
download from the [SDK Manager](https://developer.android.com/studio/intro/update#sdk-manager), in the **SDK Platforms** tab.

![](https://developer.android.com/static/studio/images/intro/sdk-manager-platforms_2x.png)

Each SDK Platform version includes the following packages:

- The **Android SDK Platform** package. This is required to compile your app for that version.
- Several **System Image** packages. At least one of these is required to run
  that version on the [Android Emulator](https://developer.android.com/studio/run/emulator).

  Each platform version includes a system image for each supported form factor
  (handsets, Android TV, and Android Wear). Each form factor might offer
  variations to match your computer's processor architecture (such as x86_64
  and ARM 64 v8a). System images labeled **Google APIs** include access to
  [Google Play services](https://developers.google.com/android/guides/overview) and those labeled **Google Play** also include the
  Google Play Store.
- The **Sources for Android** package. This includes the source files for the
  platform. Android Studio may show lines of code from these files while you
  debug your app.

The revision numbers listed in the following sections are for the **Android SDK
Platform** package only. The system images may receive separate updates, usually
to resolve bugs with the emulator. There are no release notes for the system
images, but you should always keep them up to date.
| **Important:** To see the most recent Android system components in the Android SDK Manager, you must first install the most recent [Android SDK Command-Line
| tools](https://developer.android.com/studio#command-line-tools-only) package.

## Android 16 (API level 36)

For details about the platform changes, see the [Android 16 documentation](https://developer.android.com/about/versions/16).

#### Revision 1 (March 2025)

Released to the stable channel (no longer in preview) when
[Android 16 reached the Platform Stability milestone](https://android-developers.googleblog.com/2025/03/the-third-beta-of-android-16.html).

## Android 15 (API level 35)

For details about the platform changes, see the [Android 15 documentation](https://developer.android.com/about/versions/15).

#### Revision 1 (June 2024)

Released to the stable channel (no longer in preview) when
[Android 15 reached the Platform Stability milestone](https://android-developers.googleblog.com/2024/06/the-third-beta-of-android-15.html).

## Android 14 (API level 34)

For details about the platform changes, see the [Android 14 documentation](https://developer.android.com/about/versions/14).

#### Revision 1 (June 2023)

Released to the stable channel (no longer in preview) when
[Android 14 reached the Platform Stability milestone](https://android-developers.googleblog.com/2023/06/android-14-beta-3-and-platform-stability.html).

## Android 13 (API level 33)

For details about the platform changes, see the [Android 13 documentation](https://developer.android.com/about/versions/13).

#### Revision 1 (June 2022)

Released to the stable channel (no longer in preview) when
[Android 13 reached the Platform Stability milestone](https://android-developers.googleblog.com/2022/06/android-13-beta-3-platform-stability.html).

## Android 12 (API levels 31, 32)

12L feature drop (API level 32)
:   For details about the platform changes, see
    the [12L documentation](https://developer.android.com/about/versions/12/12L).

    #### Revision 1 (March 2022)

    [Released to the stable channel](https://blog.google/products/android/12l-larger-screens/) (no longer in preview).

Android 12 (API level 31)
:   For details about the platform changes, see the
    [Android 12 documentation](https://developer.android.com/about/versions/12).

    #### Revision 1 (August 2021)

    Released to the stable channel (no longer in preview) when
    [Android 12 reached the Platform Stability milestone](https://android-developers.googleblog.com/2021/08/android-12-beta-4-and-platform-stability.html).

Android 12 ATD system images

:   This Automated Test Device (ATD) image is an
    Android system image that is optimized for headless automated tests. Early
    data indicates that tests that use this image should experience reduction in
    emulator process CPU and memory usage, and reduction in test wall time.

    It achieves these performance gains through:

    - Removing most user-facing applications (for example Dialer, Settings, and SystemUI).
    - Disabling hardware renderer drawing.

    The image comes with two versions: Google APIs ATD which provides Google
    APIs, and AOSP ATD which provides pure AOSP experience.

    To learn more about running tests using ATDs, see [Run tests using Automated
    Test Devices](https://developer.android.com/studio/test/gradle-managed-devices#gmd-atd).

## Android 11 (API level 30)

For details about the platform changes, see the [Android 11 documentation](https://developer.android.com/about/versions/11).

#### Revision 1 (July 2020)

Released to the stable channel (no longer in preview) when
[Android 11 reached the Platform Stability milestone](https://android-developers.googleblog.com/2020/07/android-11-beta-2-and-platform-stability.html).

## Android 10 (API level 29)

For details about the platform changes, see [Android 10 for Developers](https://developer.android.com/about/versions/10/highlights).

#### Revision 5 (July 2020)

This revision adds Android Automotive OS stubs.

## Android 9 (API level 28)

For details about the platform changes, see [Android 9 for developers](https://developer.android.com/about/versions/pie/android-9.0).

#### Revision 1 (August 2018)

Released to the stable channel (no longer in preview).

## Android 8.1 (API level 27)

For details about the platform changes, see [Android 8.1 for developers](https://developer.android.com/about/versions/oreo/android-8.1).

#### Revision 1 (December 2017)

Released to the stable channel (no longer in preview).

## Android 8.0 (API level 26)

For details about the platform changes, see [Android 8.0 for developers](https://developer.android.com/about/versions/oreo/android-8.0).

#### Revision 2 (August 2017)

Released to the stable channel (no longer in preview).

## Android 7.1 (API level 25)

For details about the platform changes, see [Android 7.1 for developers](https://developer.android.com/about/versions/nougat/android-7.1).

#### Revision 3 (December 2016)

Incremental update. Released as the final Android 7.1.1 (no longer in
preview).

Dependencies:

- Android SDK Platform-Tools 25.0.1 or higher is required.
- Android SDK Build-Tools 25.0.1 or higher is required.

#### Revision 2 (November 2016)

Incremental update. Released as Android 7.1.1 Developer Preview 2.
For more information, see the
[Android 7.1 API Overview](https://developer.android.com/about/versions/nougat/android-7.1).

Dependencies:

- Android SDK Platform-Tools 25.0.1 or higher is required.
- Android SDK Build-Tools 25.0.1 or higher is required.

#### Revision 1 (October 2016)

Initial release for Android 7.1 (API level 25).
Released as Android 7.1 Developer Preview 1.
For more information, see the
[Android 7.1 API Overview](https://developer.android.com/about/versions/nougat/android-7.1).

Dependencies:

- Android SDK Platform-Tools 25.0.0 or higher is required.
- Android SDK Build-Tools 25.0.0 or higher is required.

## Android 7.0 (API level 24)

For details about the platform changes, see [Android 7.0 for developers](https://developer.android.com/about/versions/nougat/android-7.0).

#### Revision 1 (August 2016)

Initial release for Android 7.0 (API level 24). For more information, see
the [Android 7.0 API Overview](https://developer.android.com/about/versions/nougat/android-7.0).

Dependencies:

- Android SDK Platform-tools r24 or higher is required.
- Android SDK Tools 24.0.0 or higher is required.

## Android 6.0 (API level 23)

For details about the platform changes, see the [Android 6.0 changes](https://developer.android.com/about/versions/marshmallow/android-6.0-changes) and
[Android 6.0 APIs](https://developer.android.com/about/versions/marshmallow/android-6.0).

#### Revision 2 (November 2015)

Fixed bugs in the layout rendering library used by Android Studio.

Dependencies:

- Android SDK Platform-tools r23 or higher is required.
- Android SDK Tools 24.3.4 or higher is required.

#### Revision 1 (August 2015)

Initial release for Android 6.0 (API level 23). For more information, see
the [Android 6.0 API Overview](https://developer.android.com/about/versions/marshmallow/android-6.0).

Dependencies:

- Android SDK Platform-tools r23 or higher is required.
- Android SDK Tools 24.3.4 or higher is required.

## Android 5.1 (API level 22)

For details about the platform changes, see the [Lollipop overview](https://developer.android.com/about/versions/lollipop) and
[Android 5.1 API changes](https://developer.android.com/about/versions/lollipop/android-5.1).

#### Revision 1 (March 2015)

Initial release for Android 5.1 (API level 22). For more information, see
the [Android 5.1 API Overview](https://developer.android.com/about/versions/lollipop/android-5.1).

Dependencies:

- Android SDK Platform-tools r22 or higher is required.
- Android SDK Tools 23.0.5 or higher is required.

## Android 5.0 (API level 21)

For details about the platform changes, see the [Lollipop overview](https://developer.android.com/about/versions/lollipop) and
[Android 5.0 API changes](https://developer.android.com/about/versions/lollipop/android-5.0).

#### Revision 2 (December 2014)

Updated layouts in the Support Library and fixed various issues.

Dependencies:

- Android SDK Platform-tools r21 or higher is required.
- Android SDK Tools 23.0.5 or higher is required.

#### Revision 1 (October 2014)

Initial release for Android 5.0 (API level 21). For more information, see
the [Android 5.0 API Overview](https://developer.android.com/about/versions/lollipop/android-5.0).

Dependencies:

- Android SDK Platform-tools r21 or higher is required.
- Android SDK Tools 23.0.5 or higher is required.

## Android 4.4W (API level 20)

This version makes KitKat available for Android Wear.

#### Revision 2 (October 2014)

Updated the rendering library.

Dependencies:

- Android SDK Platform-tools r20 or higher is required.
- Android SDK Tools 23.0 or higher is required.

#### Revision 1 (June 2014)

Initial release for Android Wear.

Dependencies:

- Android SDK Platform-tools r20 or higher is required.
- Android SDK Tools 23.0 or higher is required.

## Android 4.4 (API level 19)

For details about the platform changes, see the [KitKat overview](https://developer.android.com/about/versions/kitkat) and
[Android 4.4 API changes](https://developer.android.com/about/versions/kitkat/android-4.4).

#### Revision 2 (December 2013)

Maintenance release. The system version is 4.4.2. For more information,
see the [Android 4.4 API Overview](https://developer.android.com/about/versions/kitkat/android-4.4).

Dependencies:
:   Android SDK Platform-tools r19 or higher is required.
:   Android SDK Tools 22.3 or higher is recommended.

#### Revision 1 (October 2013)

Initial release. The system version is 4.4. For more information, see the
[Android 4.4 API Overview](https://developer.android.com/about/versions/kitkat/android-4.4).

Dependencies:
:   Android SDK Platform-tools r19 or higher is required.
:   Android SDK Tools 22.3 or higher is recommended.

## Android 4.3 (API level 18)

For details about the platform changes, see the [Jelly Bean overview](https://developer.android.com/about/versions/jelly-bean) and
[Android 4.3 API changes](https://developer.android.com/about/versions/android-4.3).

#### Revision 2 (August 2013)

Maintenance update. The system version is 4.3.

Dependencies:
:   Android SDK Platform-tools r18 or higher is required.
:   Android SDK Tools 22.0.4 or higher is recommended.

#### Revision 1 (July 2013)

Initial release. The system version is 4.3.

Dependencies:
:   Android SDK Platform-tools r18 or higher is required.
:   Android SDK Tools 22.0.4 or higher is recommended.

## Android 4.2 (API level 17)

For details about the platform changes, see the [Jelly Bean overview](https://developer.android.com/about/versions/jelly-bean) and
[Android 4.2 API changes](https://developer.android.com/about/versions/android-4.2).

#### Revision 2 (February 2013)

Maintenance update. The system version is 4.2.2.

Dependencies:
:   SDK Tools r21 or higher is required.

#### Revision 1 (November 2012)

Initial release. The system version is 4.2.

Dependencies:
:   SDK Tools r20 or higher is required.

## Android 4.1 (API level 16)

For details about the platform changes, see the [Jelly Bean overview](https://developer.android.com/about/versions/jelly-bean) and
[Android 4.1 API changes](https://developer.android.com/about/versions/android-4.1).

#### Revision 3 (October 2012)

Maintenance update. The system version is 4.1.2.

Dependencies:
:   SDK Tools r20 or higher is required.

#### Revision 2 (July 2012)

Maintenance update. The system version is 4.1.1.

Dependencies:
:   SDK Tools r20 or higher is required.

#### Revision 1 (June 2012)

Initial release. The system version is 4.1.0.

Dependencies:
:   SDK Tools r20 or higher is required.

## Android 4.0.3 (API level 15)

#### Revision 3 (March 2012)

Maintenance update. The system version is 4.0.4.

**Note:** This system image includes support
for emulator hardware graphics acceleration when used with SDK Tools r17 or
higher.
([more info](https://developer.android.com/tools/devices/emulator#accel-graphics))

Dependencies:
:   SDK Tools r17 or higher is required.

#### Revision 2 (January 2012)

Maintenance update. The system version is 4.0.3.

Dependencies:
:   SDK Tools r14 or higher is required.

#### Revision 1 (December 2011)

Initial release. The system version is 4.0.3.

Dependencies:
:   SDK Tools r14 or higher is required.

## Android 4.0 (API level 14)

#### Android 4.0, Revision 2 (December 2011)

Maintenance update. The system version is 4.0.2.

Dependencies:
:   SDK Tools r14 or higher is required.

#### Android 4.0, Revision 1 (October 2011)

Initial release. The system version is 4.0.1.

Dependencies:
:   SDK Tools r14 or higher is required.

## Android 3.2 (API level 13)

#### Android 3.2, Revision 1 (July 2011)

Initial release. SDK Tools r12 or higher is recommended.

## Android 3.1 (API level 12)

#### Android 3.1, Revision 3 (July 2011)

Dependencies:

:   Requires [SDK Tools r12](https://developer.android.com/studio/releases/sdk-tools) or
    higher.

Notes:

:   Improvements to the platform's rendering library to support the
    visual layout editor in the ADT Eclipse plugin. This revision allows for
    more drawing features in ADT and fixes several bugs in the previous
    rendering library. It also unlocks several editor features that were
    added in ADT 12.

#### Android 3.1, Revision 2 (May 2011)

Dependencies:

:   Requires [SDK Tools r11](https://developer.android.com/studio/releases/sdk-tools) or
    higher.

Notes:

:   Fixes an issue with the visual layout editor rendering library that
    prevented Android 3.1 from running in ADT.

#### Android 3.1, Revision 1 (May 2011)

Dependencies:

:   Requires [SDK Tools r11](https://developer.android.com/studio/releases/sdk-tools) or
    higher.

## Android 3.0 (API level 11)

#### Android 3.0, Revision 2 (July 2011)

Dependencies:

:   Requires [SDK Tools r12](https://developer.android.com/studio/releases/sdk-tools) or
    higher.

Notes:

:   Improvements to the platform's rendering library to support the
    visual layout editor in the ADT Eclipse plugin. This revision allows for
    more drawing features in ADT and fixes several bugs in the previous
    rendering library. It also unlocks several editor features that were
    added in ADT 12.

#### Android 3.0, Revision 1 (February 2011)

Dependencies:

:   Requires [SDK Tools r10](https://developer.android.com/studio/releases/sdk-tools) or
    higher.

## Android 2.3.3 (API level 10)

#### Android 2.3.3, Revision 2 (July 2011)

Dependencies:

:   Requires [SDK Tools r12](https://developer.android.com/studio/releases/sdk-tools) or
    higher.

Notes:

:   Improvements to the platform's rendering library to support the
    visual layout editor in the ADT Eclipse plugin. This revision allows for
    more drawing features in ADT and fixes several bugs in the previous
    rendering library. It also unlocks several editor features that were
    added in ADT 12.

#### Android 2.3.3, Revision 1 (February 2011)

Dependencies:

:   Requires SDK Tools r9 or higher.

## Android 2.3 (API level 9)

#### Android 2.3, Revision 1 (December 2010)

Dependencies:

:   Requires SDK Tools r8 or higher.