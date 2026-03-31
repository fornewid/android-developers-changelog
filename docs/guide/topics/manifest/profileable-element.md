---
title: <profileable>  |  App architecture  |  Android Developers
url: https://developer.android.com/guide/topics/manifest/profileable-element
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [App architecture](https://developer.android.com/topic/architecture/intro)

# <profileable> Stay organized with collections Save and categorize content based on your preferences.



syntax:
:   ```
    <profileable android:shell=["true" | "false"] android:enabled=["true" | "false"] />
    ```

contained in:
:   `<application>`

description:
:   Specifies how profilers can access this application.

attributes:
:   `android:shell`
    :   Specifies whether the user of the device can profile this application through local debugging
        tools such as the following:

        * `android.os.Trace` tracing APIs (Android 11 and lower)
        * `simpleperf`
        * `am profile` commands
        * [`perfetto` profilers](/studio/command-line/perfetto) (native memory, Java memory, CPU)

        If this isn't set, or is set to `false`, these tools and APIs work only when an app is
        `debuggable`.
        Debuggable apps incur significant and varied performance degradation and aren't useful for
        measuring timing accurately. This element is strongly recommended for local performance
        measurements, to capture accurate results.

        This element is designed to be usable in release, or production, builds to enable local profiling.
        It incurs minimal risk of data exposure: no memory data is readable by the host profiling tools
        and the shell process. Only stack traces are readable, which are typically obfuscated or lacking symbols
        in release builds.
:   `android:enabled`
    :   Specifies whether the application can be profiled by system services or shell tools.
        For the latter, you also set [`android:shell`](#shell).
        If false, the application can't be profiled at all. The default is true.
        This attribute was added in API level 30.

introduced in:
:   API Level 29