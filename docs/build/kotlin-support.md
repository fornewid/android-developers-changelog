---
title: AGP, D8, and R8 versions required for Kotlin versions  |  Android Studio  |  Android Developers
url: https://developer.android.com/build/kotlin-support
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Android Studio](https://developer.android.com/studio)
* [Gradle build guides](https://developer.android.com/build/gradle-build-overview)

# AGP, D8, and R8 versions required for Kotlin versions Stay organized with collections Save and categorize content based on your preferences.



The Android Gradle plugin (AGP) and the D8 and R8 compilers are compatible with
class files from Kotlin version 1.3 and higher.

The D8 and R8 compilers support class files from Kotlin version 1.3 starting
from version 2.1.86 (included in AGP 4.1).
For class files from Kotlin version 1.4 and higher there is a minimum required
AGP, D8, and R8 version for each Kotlin version.

The following table shows the minimum required versions of AGP, D8 and R8 for
each Kotlin version. Note that AGP comes bundled with D8 and R8, so the
required D8 and R8 version is only relevant when using D8 and R8 outside of AGP
or if overriding the bundled version.

| Kotlin version | Required AGP version | Required R8 version |
| --- | --- | --- |
| 1.3 | 4.1 | 2.1.86 |
| 1.4 | 7.0 | 3.0.76 |
| 1.5 | 7.0 | 3.0.77 |
| 1.6 | 7.1 | 3.1.51 |
| 1.7 | 7.2 | 3.2.47 |
| 1.8 | 7.4 | 4.0.48 |
| 1.9 | 8.0 | 8.0.27 |
| 2.0 | 8.5 | 8.5.10 |
| 2.1 | 8.6 | 8.6.17 |
| 2.2 | 8.10 | 8.10.21 |
| 2.3 | 8.13.2 | 8.13.19[1](#fn1) |
| 2.4 | 9.1.0 | 9.1.29 |

The AGP versions listed in the table automatically use the
specified D8 and R8 compiler versions.

When using [Java 8+ API desugaring](/studio/build/library-desugaring)
AGP version 7.0 (and D8 and R8 version 3.0.76) is required.
R8 can only emit Kotlin metadata of version 1.4 and newer. When using R8 to
shrink a Kotlin library with metadata from Kotlin version 1.3 the metadata
is converted to the Kotlin 1.4 format. For Kotlin version 1.4 and newer R8
preserves the version.

---

1. 9.x versions before 9.0.28 don't support Kotlin 2.3. [↩](#fnref1)