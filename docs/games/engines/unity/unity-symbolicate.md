---
title: https://developer.android.com/games/engines/unity/unity-symbolicate
url: https://developer.android.com/games/engines/unity/unity-symbolicate
source: md.txt
---

# Symbolicate Android crashes and ANR for Unity games

Crashes and ANRs on Android produce a stack trace, which is a snapshot of the sequence of nested functions called in your game up to the moment it crashed. These snapshots can help you identify and fix any problems in the source.

However, when you build your game with Unity in release mode, the symbols are not packed with the APK. If your game crashes or has ANRs, the call stack only shows the memory address.

For example:
>
>     05-26 18:06:51.311: A/libc(26986): Fatal signal 11 (SIGSEGV) at 0x000004e4 (code=1), thread 27024 (Worker Thread)
>     05-26 18:06:51.411: I/DEBUG(242): *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** ***
>     05-26 18:06:51.411: I/DEBUG(242): Build fingerprint: 'Xiaomi/cancro_wc_lte/cancro:4.4.4/KTU84P/V6.7.1.0.KXDCNCH:user/release-keys'
>     05-26 18:06:51.411: I/DEBUG(242): Revision: '0'
>     05-26 18:06:51.411: I/DEBUG(242): pid: 26986, tid: 27024, name: Worker Thread  >>> com.u.demo <<<
>     05-26 18:06:51.411: I/DEBUG(242): signal 11 (SIGSEGV), code 1 (SEGV_MAPERR), fault addr 000004e4
>      I/DEBUG(242): backtrace:
>      I/DEBUG(242):     #00  pc 006d4960  /data/app-lib/com.u.demo-1/libunity.so
>      I/DEBUG(242):     #01  pc 006d4c0c  /data/app-lib/com.u.demo-1/libunity.so
>      I/DEBUG(242):     #02  pc 006d4c0c  /data/app-lib/com.u.demo-1/libunity.so
>      I/DEBUG(242):     #03  pc 006d4c0c  /data/app-lib/com.u.demo-1/libunity.so
>      I/DEBUG(242):     #04  pc 006d4c0c  /data/app-lib/com.u.demo-1/libunity.so
>      I/DEBUG(242):     #05  pc 001c5510  /data/app-lib/com.u.demo-1/libunity.so
>      I/DEBUG(242):     #06  pc 001c595c  /data/app-lib/com.u.demo-1/libunity.so
>      I/DEBUG(242):     #07  pc 001c4ec0  /data/app-lib/com.u.demo-1/libunity.so
>      I/DEBUG(242):     #08  pc 0043a05c  /data/app-lib/com.u.demo-1/libunity.so
>      I/DEBUG(242):     #09  pc 0000d248  /system/lib/libc.so (__thread_entry+72)
>      I/DEBUG(242):     #10  pc 0000d3e0  /system/lib/libc.so (pthread_create+240)

Google Play supports uploading a debug symbols file for each version of your app in Play Console. This makes it easier to analyze and fix your crashes and ANRs.

From Unity 2020.3 and higher, you can follow Unity's guidance to generate[Android symbols](https://docs.unity3d.com/2020.3/Documentation/Manual/android-symbols.html)and then[upload the symbolication file](https://support.google.com/googleplay/android-developer/answer/9848633#zippy=%2Cupload-files-using-play-console)to Google Play Console to see a human-readable stack trace on the Android Vitals dashboard.

Otherwise, you can follow the[Symbolicate Android crash](https://support.unity.com/hc/en-us/articles/115000292166-Symbolicate-Android-crash)article from Unity to manually resolve the stack trace or generate symbol files for lower versions of Unity.