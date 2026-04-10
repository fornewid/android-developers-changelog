---
title: https://developer.android.com/guide/topics/manifest/profileable-element
url: https://developer.android.com/guide/topics/manifest/profileable-element
source: md.txt
---

# &lt;profileable>

syntax:
:

    ```xml
    <profileable android:shell=["true" | "false"] android:enabled=["true" | "false"] />
    ```

contained in:
:   [<application>](https://developer.android.com/guide/topics/manifest/application-element)

description:
:   Specifies how profilers can access this application.

attributes:
:

    `android:shell`
    :   Specifies whether the user of the device can profile this application through local debugging tools such as the following:

        - [android.os.Trace](https://developer.android.com/reference/kotlin/android/os/Trace)tracing APIs (Android 11 and lower)
        - [simpleperf](https://developer.android.com/ndk/guides/simpleperf)
        - [am profile](https://developer.android.com/studio/command-line/adb#am)commands
        - [`perfetto`profilers](https://developer.android.com/studio/command-line/perfetto)(native memory, Java memory, CPU)

        If this isn't set, or is set to`false`, these tools and APIs work only when an app is[debuggable](https://developer.android.com/guide/topics/manifest/application-element#debug). Debuggable apps incur significant and varied performance degradation and aren't useful for measuring timing accurately. This element is strongly recommended for local performance measurements, to capture accurate results.

        This element is designed to be usable in release, or production, builds to enable local profiling. It incurs minimal risk of data exposure: no memory data is readable by the host profiling tools and the shell process. Only stack traces are readable, which are typically obfuscated or lacking symbols in release builds.
:

    `android:enabled`
    :   Specifies whether the application can be profiled by system services or shell tools. For the latter, you also set[`android:shell`](https://developer.android.com/guide/topics/manifest/profileable-element#shell). If false, the application can't be profiled at all. The default is true. This attribute was added in API level 30.

introduced in:
:   API Level 29