---
title: https://developer.android.com/guide/topics/resources/internationalization
url: https://developer.android.com/guide/topics/resources/internationalization
source: md.txt
---

Android leverages the
[ICU
library](http://site.icu-project.org/) and [CLDR project](http://cldr.unicode.org/) to provide Unicode and other internationalization
support. This page's discussion of Unicode and internationalization support is divided into two
sections: Android 6.0 (API level 23) and lower, and Android 7.0 (API level 24) and higher.

## Unicode and internationalization support through Android 6.0 (API level 23)


The Android platform uses ICU and CLDR to implement various
classes for handling both Latin and non-Latin orthographies, exposing classes
like [Locale](https://developer.android.com/reference/java/util/Locale), [Character](https://developer.android.com/reference/java/lang/Character), and many subclasses of
[java.text](https://developer.android.com/reference/java/text/package-summary). An app that requires internationalization functionalities beyond
the exposed classes, and targets versions of the platform through Android 6.0
(API level 23), must include the ICU library.

### Versioning


Successive releases of the Android platform correspond to newer versions of ICU
and the corresponding CLDR and Unicode versions. Table 1 shows this correspondence
through Android 6.0 (API level 23).

**Table 1.** ICU and CLDR versions used
through Android 6.0 (API level 23).

| Platform (API level) | ICU | CLDR | Unicode |
|---|---|---|---|
| Android 1.5--2.0 (API levels 3--7) | 3.8 | 1.5 | 5.0 |
| Android 2.2 (API level 8) | 4.2 | 1.7 | 5.1 |
| Android 2.3--3.0 (API levels 9--13) | 4.4 | 1.8 | 5.2 |
| Android 4.0 (API levels 14--15) | 4.6 | 1.9 | 6.0 |
| Android 4.1 (API levels 16--17) | 4.8 | 2.0 | 6.0 |
| Android 4.3 (API level 18) | 50 | 22.1 | 6.2 |
| Android 4.4 (API levels 19--20) | 51 | 23 | 6.2 |
| Android 5.0 (API levels 21--22) | 53 | 25 | 6.3 |
| Android 6.0 (API level 23) | 55.1 | 27.0.1 | 7.0 |


The Android framework provides more comprehensive support for Unicode and internationalization
for apps targeting Android 7.0 (API level 24) and higher. The next section of this page
provides details about that support.

## Unicode and internationalization support in Android 7.0 (API level 24) and higher


For Android 7.0 (API level 24) and higher, the Android platform
exposes a subset of the ICU4J APIs for app developers
to use under the `android.icu` package.
ICU4J is an open-source, widely used set of Java libraries providing Unicode
and internationalization support for software applications.

The ICU4J APIs use
localization data present on the device. As a result, you can reduce your app's
footprint by not compiling the ICU4J libraries into your app. Instead, you can
call out to them in the framework. If you do this, you might want to provide
[multiple versions
of your APK](https://developer.android.com/google/play/publishing/multiple-apks), so users running versions of Android lower than
Android 7.0 (API level 24)
can download a version of the app that contains the ICU4J libraries.


This section begins by providing some basic information on the minimum
Android API levels required to support these libraries. It then explains what
you need to know about the Android-specific implementation of ICU4J. Finally,
it tells you how to use the ICU4J APIs in the Android framework.

### ICU4J on Android


Android exposes a subset of the ICU4J APIs through the
`android.icu` package, rather than `com.ibm.icu`. Some
ICU4J APIs are not exposed by the Android framework,
for reasons such as the APIs being deprecated
or not declared stable. As the ICU team deprecates APIs in the future,
Android also marks them as deprecated but continues to include them.

Here are a few reminders:

- The ICU4J Android framework APIs don't include all the ICU4J APIs.
- The APIs in the Android framework don't replace Android's support for [localizing with
  resources](https://developer.android.com/guide/topics/resources/localization).
- In some cases, the Android framework supports more characters than the ICU libraries do. This is true, for example, of the [android.text](https://developer.android.com/reference/android/text/package-summary) class's support for emoji.

### Migrate to the android.icu package from com.ibm.icu


If you are already using the ICU4J APIs in your app, and the
`android.icu` APIs meet your requirements, then migrating to
the framework APIs requires you to change your Java imports
from `com.ibm.icu` to `android.icu`. You can then
remove your own copy of ICU4J files from the app.


**Note** : The ICU4J framework APIs use the `android.icu`
namespace instead of `com.ibm.icu`. This is to avoid namespace
conflicts in apps that contain their own `com.ibm.icu` libraries.

### Migrate to android.icu APIs from other Android SDK APIs


Some classes in the `java` and `android` packages have
equivalents to those found in ICU4J. However, ICU4J often provides broader
support for standards and languages.

Table 2 shows some examples of these equivalencies to get you started:

**Table 2.**Android
and Java ICU4J classes

| Class | Alternatives |
|---|---|
| `java.lang.Character` | `android.icu.lang.UCharacter` |
| `java.text.BreakIterator` | `android.icu.text.BreakIterator` |
| `java.text.DecimalFormat` | `android.icu.text.DecimalFormat` |
| `java.util.Calendar` | `android.icu.util.Calendar` |
| `android.text.BidiFormatter` | `android.icu.text.Bidi` |
| `android.text.format.DateFormat` | `android.icu.text.DateFormat` |
| `android.text.format.DateUtils` | `android.icu.text.DateFormat` `android.icu.text.RelativeDateTimeFormatter` |

### ICU4C on Android


Android exposes a subset of the ICU4C APIs through the `libicu.so` library,
rather than `libicuuc.so` or `libicui18n.so`. The APIs are available
starting with Android 12 (API level 31). The NDK headers are available starting with
the NDK release r22b.
No C++ API is exposed through the Android NDK. Some of the C APIs are not available.

### Versioning


Successive releases of the Android platform correspond to newer versions of ICU
and the corresponding CLDR and Unicode versions. Table 3 shows this correspondence
starting from Android 7.0 (API level 24). Use the
[`VersionInfo.ICU_VERSION`](https://developer.android.com/reference/android/icu/util/VersionInfo#ICU_VERSION) API (available since Android 7.0) to obtain the ICU
version information at runtime.

**Table 3.** ICU and CLDR versions used in Android versions
from Android 7.0 (API level 24) through Android 15 (API level 35).

| Platform (API level) | ICU | CLDR | Unicode |
|---|---|---|---|
| Android 7.0 - 7.1 (API levels 24 - 25) | 56 | 28 | 8.0 |
| Android 8.0 - 8.1 (API levels 26 - 27) | 58.2 | 30.0.3 | 9.0 |
| Android 9 (API level 28) | 60.2 | 32.0.1 | 10.0 |
| Android 10 (API level 29) | 63.2 | 34 | 11.0 |
| Android 11 (API level 30) | 66.1 | 36 | 13.0 |
| Android 12 (API level 31 - 32) | 68.2 | 38.1 | 13.0 |
| Android 13 (API level 33) | 70.1 | 40 | 14.0 |
| Android 14 (API level 34) | 72.1 | 42 | 15.0 |
| Android 15 (API level 35) | 75.1 | 45 | 15.1 |

### 24h/12h Time format setting

ICU on Android doesn't observe the user's 24h/12h time format setting, obtained from [`DateFormat.is24HourFormat()`](https://developer.android.com/reference/android/text/format/DateFormat#is24HourFormat(android.content.Context)). To observe this setting, either use [`DateFormat`](https://developer.android.com/reference/android/text/format/DateFormat) or [`DateUtils`](https://developer.android.com/reference/android/text/format/DateUtils) time formatting methods or use ICU time formatting patterns with appropriate hour pattern symbols ('h' for 12h, 'H' for 24h) for different `is24HourFormat()` return values. For example, this code generates a string with the current time that observes the user's 12h/24h setting:  

### Kotlin

```kotlin
val skeleton: String = if (DateFormat.is24HourFormat(context)) "Hm" else "hm"
val formattedTime: String = android.icu.text.DateFormat.getInstanceForSkeleton(
        skeleton,
        Locale.getDefault()).format(Date()
)
```

### Java

```java
String skeleton = DateFormat.is24HourFormat(context) ? "Hm" : "hm";
String formattedTime = android.icu.text.DateFormat.getInstanceForSkeleton(skeleton, Locale.getDefault()).format(new Date());
```

### Stability of Transliterator

Starting from Android 10 (API level 29), [`Transliterator`](https://developer.android.com/reference/android/icu/text/Transliterator) is provided to transliterate text from one format to another. The set of available transliteation IDs is unstable across Android releases and devices. Device manufacturers might add extra transliteration IDs. Developers must check the available IDs, obtained from [`Transliterator.getAvailableIDs()`](https://developer.android.com/reference/android/icu/text/Transliterator#getAvailableIDs()), before transliterating text.

## Licensing


ICU4J is released under the ICU license. For details, see the [ICU
user guide](http://userguide.icu-project.org/icufaq#TOC-How-is-the-ICU-licensed-).