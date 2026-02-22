---
title: https://developer.android.com/ndk/guides/ndk-stack
url: https://developer.android.com/ndk/guides/ndk-stack
source: md.txt
---

# ndk-stack

The`ndk-stack`tool allows you to symbolize stack traces from[`adb logcat`](https://developer.android.com/tools/help/logcat)or a tombstone in`/data/tombstones/`. It replaces any address inside a shared library with the corresponding`<source-file>:<line-number>`from your source code, making debugging easier.

For example, it translates something like:  

```
I/DEBUG   (   31): *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** ***
I/DEBUG   (   31): Build fingerprint: 'generic/google_sdk/generic/:2.2/FRF91/43546:eng/test-keys'
I/DEBUG   (   31): pid: 351, tid: 351  >>> /data/local/ndk-tests/crasher <<<
I/DEBUG   (   31): signal 11 (SIGSEGV), fault addr 0d9f00d8
I/DEBUG   (   31):  r0 0000af88  r1 0000a008  r2 baadf00d  r3 0d9f00d8
I/DEBUG   (   31):  r4 00000004  r5 0000a008  r6 0000af88  r7 00013c44
I/DEBUG   (   31):  r8 00000000  r9 00000000  10 00000000  fp 00000000
I/DEBUG   (   31):  ip 0000959c  sp be956cc8  lr 00008403  pc 0000841e  cpsr 60000030
I/DEBUG   (   31):          #00  pc 0000841e  /data/local/ndk-tests/crasher
I/DEBUG   (   31):          #01  pc 000083fe  /data/local/ndk-tests/crasher
I/DEBUG   (   31):          #02  pc 000083f6  /data/local/ndk-tests/crasher
I/DEBUG   (   31):          #03  pc 000191ac  /system/lib/libc.so
I/DEBUG   (   31):          #04  pc 000083ea  /data/local/ndk-tests/crasher
I/DEBUG   (   31):          #05  pc 00008458  /data/local/ndk-tests/crasher
I/DEBUG   (   31):          #06  pc 0000d362  /system/lib/libc.so
I/DEBUG   (   31):
```

into the more readable:  

```
********** Crash dump: **********
Build fingerprint: 'generic/google_sdk/generic/:2.2/FRF91/43546:eng/test-keys'
pid: 351, tid: 351  >>> /data/local/ndk-tests/crasher <<<
signal 11 (SIGSEGV), fault addr 0d9f00d8
Stack frame #00  pc 0000841e  /data/local/ndk-tests/crasher : Routine zoo in /tmp/foo/crasher/jni/zoo.c:13
Stack frame #01  pc 000083fe  /data/local/ndk-tests/crasher : Routine bar in /tmp/foo/crasher/jni/bar.c:5
Stack frame #02  pc 000083f6  /data/local/ndk-tests/crasher : Routine my_comparison in /tmp/foo/crasher/jni/foo.c:9
Stack frame #03  pc 000191ac  /system/lib/libc.so
Stack frame #04  pc 000083ea  /data/local/ndk-tests/crasher : Routine foo in /tmp/foo/crasher/jni/foo.c:14
Stack frame #05  pc 00008458  /data/local/ndk-tests/crasher : Routine main in /tmp/foo/crasher/jni/main.c:19
Stack frame #06  pc 0000d362  /system/lib/libc.so
```

## Usage

To use`ndk-stack`, you first need a directory containing unstripped versions of your app's shared libraries. If you use`ndk-build`, these unstripped shared libraries are found in`$PROJECT_PATH/obj/local/<abi>`, where`<abi>`is your device's ABI.

For an Android Gradle Plugin (AGP) build, the unstripped libraries will be in`<project-path>/build/intermediates/cxx/<build-type>/<hash>/obj/<abi>`, where`<project-path>`is the directory of the AGP project that contains the module you're trying to symbolize (by default this is`app`),`<build-type>`is the name of the CMake or ndk-build build type (such as`RelWithDebInfo`,`Release`,`Debug`, etc.),`<hash>`is arbitrary, and`<abi>`is your device's ABI.

There are two ways to use the tool. You can feed the logcat text as direct input to the program. For example:  

```
adb logcat | $NDK/ndk-stack -sym $PROJECT_PATH/obj/local/armeabi-v7a
```

You can also use the`-dump`option to specify the logcat as an input file. For example:  

```
adb logcat > /tmp/foo.txt
$NDK/ndk-stack -sym $PROJECT_PATH/obj/local/armeabi-v7a -dump foo.txt
```

When it begins parsing the logcat output, the tool looks for an initial line of asterisks. For example:  

```
*** *** *** *** *** *** *** *** *** *** *** *** *** *** *** ***
```

**Note:** When copy/pasting traces, don't forget this line, or`ndk-stack`won't work correctly.

## More information

Google Play uses`ndk-stack`to symbolize stack traces for native apps in the Google Play Console. For information on how to enable this for your app in a production environment, see how to[include a native debug symbols file](https://developer.android.com/studio/build/shrink-code#strip-native-libraries)for your app in the Google Play Console.