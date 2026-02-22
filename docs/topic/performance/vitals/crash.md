---
title: https://developer.android.com/topic/performance/vitals/crash
url: https://developer.android.com/topic/performance/vitals/crash
source: md.txt
---

# Crashes

An Android app crashes whenever there's an unexpected exit caused by an
unhandled exception or signal. An app that is written using Java or Kotlin
crashes if it throws an unhandled exception, represented by the
[`Throwable`](https://developer.android.com/reference/java/lang/Throwable) class. An
app that is written using machine code or C++ crashes if there's an unhandled
signal, such as `SIGSEGV`, during its execution.

When an app crashes, Android terminates the app's process and displays a dialog
to let the user know that the app has stopped, as shown in figure 1.

![An app crash on an Android device](https://developer.android.com/static/topic/performance/images/crash-example-framed.png)

**Figure 1.** An app crash on an Android device

An app doesn't need to be running in the foreground for it to crash. Any app
component, even components like broadcast receivers or content providers that
are running in the background, can cause an app to crash. These crashes are
often confusing for users because they were not actively engaging with your app.

If your app is experiencing crashes, you can use the guidance in this page to
diagnose and fix the problem.

## Detect the problem

You may not always know that your users are experiencing crashes when
they use your app. If you have already published your app, you can use
Android vitals to see crash rates for your app.

### Android vitals

Android vitals can help you monitor and improve your app's crash rate.
Android vitals measures several crash rates:

- **Crash rate:** The percentage of your daily active users who experienced any type of crash.
- **User-perceived crash rate:** The percentage of your daily active users
  who experienced at least one crash while they were actively using your app
  (a user-perceived crash). An app is considered to be in active use
  if it is displaying any activity or executing any
  [foreground service](https://developer.android.com/develop/background-work/services/fgs).

  | **Note:** For Wear OS apps, user-perceived crash rates include both foreground and background crashes. Wear OS devices always have watch faces running in the background, and users frequently move Wear OS apps to the background, even during active usage, because of the small screen size.
- **Multiple crash rate:** The percentage of your daily active users who
  experienced at least two crashes.

A *daily active user* is a unique user who uses your app
on a single day on a single device, potentially over multiple sessions.
If a user uses your app on more than one device in a single day,
each device will contribute to the number of active users for that day.
If multiple users use the same device in a single day,
this is counted as one active user.

User-perceived crash rate is a *core vital* meaning that it affects the
discoverability of your app on Google Play. It is important because the crashes it
counts always occur when the user is engaged with the app, causing the most
disruption.

Play has defined two **bad behavior thresholds** on this metric:

- **Overall bad behavior threshold:** At least 1.09% of daily active users experience a user-perceived crash, across all device models.
- **Per-device bad behavior threshold:** At least 8% of daily active users experience a user-perceived crash, **for a single device model**.

If your app exceeds the overall bad behavior threshold, it is likely to be
less discoverable on all devices. If your app exceeds the per-device bad behavior
threshold on some devices, it is likely to be less discoverable on those devices,
and a warning may be shown on your store listing.

Android vitals can alert you via the
[Play Console](https://play.google.com/console/)
when your app is exhibiting excessive crashes.

For information on how Google Play collects Android vitals data, see the
[Play Console](https://support.google.com/googleplay/android-developer/answer/7385505)
documentation.

## Diagnose the crashes

Once you have identified that your app is reporting crashes, the
next step is to diagnose them. Solving crashes can be difficult.
However, if you can identify the root cause of
the crash, most likely you can find a solution to it.

There are many situations that can cause a crash in your app. Some reasons are
obvious, like checking for a null value or empty string, but others are more
subtle, like passing invalid arguments to an API or even complex multithreaded
interactions.

Crashes on Android produce a stack trace, which is a snapshot of the sequence of
nested functions called in your program up to the moment it crashed. You can
view crash stack traces in
[Android vitals](https://support.google.com/googleplay/android-developer/answer/9859174).

### How to read a stack trace

The first step to fix a crash is to identify the place where it happens. You can
use the stack trace available in the report details if you are using Play
Console or the output of the [logcat](https://developer.android.com/studio/command-line/logcat) tool. If you
don't have a stack trace available, you should locally reproduce the crash,
either by manually testing the app or by reaching out to affected users, and
reproduce it while using logcat.

The following trace shows an example of a crash on an app written using the Java
programming language:  

    --------- beginning of crash
    AndroidRuntime: FATAL EXCEPTION: main
    Process: com.android.developer.crashsample, PID: 3686
    java.lang.NullPointerException: crash sample
    at com.android.developer.crashsample.MainActivity$1.onClick(MainActivity.java:27)
    at android.view.View.performClick(View.java:6134)
    at android.view.View$PerformClick.run(View.java:23965)
    at android.os.Handler.handleCallback(Handler.java:751)
    at android.os.Handler.dispatchMessage(Handler.java:95)
    at android.os.Looper.loop(Looper.java:156)
    at android.app.ActivityThread.main(ActivityThread.java:6440)
    at java.lang.reflect.Method.invoke(Native Method)
    at com.android.internal.os.Zygote$MethodAndArgsCaller.run(Zygote.java:240)
    at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:746)
    --------- beginning of system

A stack trace shows two pieces of information that are critical to debugging a
crash:

- The type of exception thrown.
- The section of code where the exception is thrown.

The type of exception thrown is usually a very strong hint as to what went
wrong. Look at whether it is an
[`IOException`](https://developer.android.com/reference/java/io/IOException), an
[`OutOfMemoryError`](https://developer.android.com/reference/java/lang/OutOfMemoryError),
or something else, and find the documentation about the exception class.

The class, method, file, and line number of the source file where the exception
is thrown is shown on the second line of a stack trace. For each function that
was called, another line shows the preceding call site (called a stack frame).
By walking up the stack and examining the code, you may find a place that is
passing an incorrect value. If your code doesn't appear in the stack trace, it
is likely that somewhere, you passed an invalid parameter into an asynchronous
operation. You can often figure out what happened by examining each line of the
stack trace, finding any API classes that you used, and confirming that the
parameters you passed were correct, and that you called it from a place that is
allowed.

Stack traces for apps with C and C++ code work much the same way.  

    *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** ***
    Build fingerprint: 'google/foo/bar:10/123.456/78910:user/release-keys'
    ABI: 'arm64'
    Timestamp: 2020-02-16 11:16:31+0100
    pid: 8288, tid: 8288, name: com.example.testapp  >>> com.example.testapp <<<
    uid: 1010332
    signal 11 (SIGSEGV), code 1 (SEGV_MAPERR), fault addr 0x0
    Cause: null pointer dereference
        x0  0000007da81396c0  x1  0000007fc91522d4  x2  0000000000000001  x3  000000000000206e
        x4  0000007da8087000  x5  0000007fc9152310  x6  0000007d209c6c68  x7  0000007da8087000
        x8  0000000000000000  x9  0000007cba01b660  x10 0000000000430000  x11 0000007d80000000
        x12 0000000000000060  x13 0000000023fafc10  x14 0000000000000006  x15 ffffffffffffffff
        x16 0000007cba01b618  x17 0000007da44c88c0  x18 0000007da943c000  x19 0000007da8087000
        x20 0000000000000000  x21 0000007da8087000  x22 0000007fc9152540  x23 0000007d17982d6b
        x24 0000000000000004  x25 0000007da823c020  x26 0000007da80870b0  x27 0000000000000001
        x28 0000007fc91522d0  x29 0000007fc91522a0
        sp  0000007fc9152290  lr  0000007d22d4e354  pc  0000007cba01b640

    backtrace:
      #00  pc 0000000000042f89  /data/app/com.example.testapp/lib/arm64/libexample.so (com::example::Crasher::crash() const)
      #01  pc 0000000000000640  /data/app/com.example.testapp/lib/arm64/libexample.so (com::example::runCrashThread())
      #02  pc 0000000000065a3b  /system/lib/libc.so (__pthread_start(void*))
      #03  pc 000000000001e4fd  /system/lib/libc.so (__start_thread)

If you don't see class and function-level information in native stack traces,
you may need to
[generate a native debug symbols file](https://developer.android.com/studio/build/shrink-code#strip-native-libraries)
and upload it to the Google Play Console. For more information, see
[Deobfuscate crash stack traces](https://support.google.com/googleplay/android-developer/answer/9848633#generate_file).
For general information on native crashes, see
[Diagnosing native crashes](https://source.android.com/devices/tech/debug/native-crash).

### Tips for reproducing a crash

It's possible that you can't quite reproduce the problem just by starting an
emulator or connecting your device to your computer. Development environments
tend to have more resources, such as bandwidth, memory, and storage. Use the
type of exception to determine what could be the resource that is scarce, or
find a correlation between the version of Android, device type or your app's
version.

#### Memory errors

If you have an
[`OutOfMemoryError`](https://developer.android.com/reference/java/lang/OutOfMemoryError),
then you could create an emulator with low memory capacity to test with. Figure
2 shows the AVD manager settings where you can control the amount of memory on
the device.

![Memory setting on AVD manager](https://developer.android.com/static/topic/performance/images/crash-emulator-memory.png)

**Figure 2.** Memory setting on AVD manager

#### Networking exceptions

Since users frequently move in and out of mobile or WiFi network coverage, in an
application network exceptions usually shouldn't be treated as *errors*, but
rather as normal operating conditions that happen unexpectedly.

If you need to reproduce a network exception, such as an
[`UnknownHostException`](https://developer.android.com/reference/java/net/UnknownHostException),
then try turning on airplane mode while your application attempts to use the
network.

Another option is to reduce the quality of the network in the emulator by
choosing a network speed emulation and/or a network delay. You can use the
**Speed** and **Latency** settings on AVD manager, or you can start the emulator
with the `-netdelay` and `-netspeed` flags, as shown in the following
command-line example:  

    emulator -avd [your-avd-image] -netdelay 20000 -netspeed gsm

This example sets a delay of 20 seconds on all network requests and an upload
and download speed of 14.4 Kbps. For more information on command-line options
for the emulator, see
[Start the emulator from the command line](https://developer.android.com/studio/run/emulator-commandline).

### Reading with logcat

Once you are able have the steps to reproduce the crash, you can use a tool like
[`logcat`](https://developer.android.com/studio/command-line/logcat) to get more information.

The logcat output will show you what other log messages you have printed, along
with others from the system. Don't forget to turn off any extra
[`Log`](https://developer.android.com/reference/android/util/Log) statements that you
have added because printing them wastes CPU and battery while your app is
running.

## Prevent crashes caused by null pointer exceptions

Null pointer exceptions (identified by the runtime error type
`NullPointerException`) occur when you're trying to access an object that is
null, typically by invoking its methods or accessing its members. **Null pointer
exceptions are the largest cause of app crashes on Google Play.** The purpose of
null is to signify that the object is missing - for example, it hasn't been
created or assigned yet. To avoid null pointer exceptions, you need to make sure
that the object references you're working with are non-null before calling
methods on them or trying to access their members. If the object reference is
null, handle this case well (for example, exit from a method before performing
any operations on the object reference and write information to a debug log).

Because you don't want to have null checks for every parameter of every method
called, you can rely on the IDE or on the type of the object to signify
nullability.

### Java programming language

The following sections apply to the Java programming language.

#### Compile time warnings

Annotate your methods' parameters and return values with
[`@Nullable`](https://developer.android.com/reference/androidx/annotation/Nullable) and
[`@NonNull`](https://developer.android.com/reference/androidx/annotation/NonNull) to receive compile time
warnings from the IDE. These warnings prompt you to expect a nullable object:

![Null pointer exception warning](https://developer.android.com/static/topic/images/reliability/null-pointer-exception-warning.png)

These null checks are for objects that you know could be null. An exception on a
`@NonNull` object is an indication of an error in your code that needs to be
addressed.

#### Compile time errors

Because nullability should be meaningful, you can embed it in the types you use
so that there is a compile time check for null. If you know an object can be
null and that nullability should be handled, you could wrap it in an object like
[`Optional`](https://docs.oracle.com/javase/8/docs/api/java/util/Optional.html).
You should always prefer types that convey nullability.

### Kotlin

In Kotlin,
[nullability](https://kotlinlang.org/docs/reference/null-safety.html)
is part of the type system. For example, a variable needs to be declared from
the beginning as nullable or non-nullable. Nullable types are marked with a `?`:  

    // non-null
    var s: String = "Hello"

    // null
    var s: String? = "Hello"

Non-nullable variables cannot be assigned a null value and nullable variables
need to be checked for nullability before being used as non-null.

If you don't want to check for null explicitly, you can use the `?.` safe call
operator:  

    val length: Int? = string?.length  // length is a nullable int
                                       // if string is null, then length is null

As a best practice, make sure you address the null case for a nullable object,
or your app could get into unexpected states. If your application won't crash
anymore with `NullPointerException`, you won't know that these errors exist.

The following are some ways to check for null:

- `if` checks

      val length = if(string != null) string.length else 0

  Due to smart-cast and the null check, the Kotlin compiler knows that the
  string value is non-null so it allows you to use the reference directly,
  without the need for the safe call operator.
- `?:` [Elvis operator](https://kotlinlang.org/docs/reference/null-safety.html#elvis-operator)

  This operator allows you to state "if the object is non-null, return the
  object; otherwise, return something else".  

      val length = string?.length ?: 0

You can still get a `NullPointerException` in Kotlin. The following are the most
common situations:

- When you're explicitly throwing a `NullPointerException`.
- When you're using the [null assertion `!!` operator](https://kotlinlang.org/docs/reference/null-safety.html#the--operator). This operator converts any value to a non-null type, throwing `NullPointerException` if the value is null.
- When accessing a null reference of a platform type.

### Platform types

Platform types are object declarations coming from Java.
[These types are specially-treated](https://kotlinlang.org/docs/reference/java-interop.html#null-safety-and-platform-types);
null checks are not as enforced, so the non-null guarantee is the same as in
Java. When you access a platform type reference, Kotlin does not create compile
time errors but these references can lead to runtime errors. See the following
example from the Kotlin documentation:  

    val list = ArrayList<String>() // non-null (constructor result) list.add("Item")
    val size = list.size // non-null (primitive int) val item = list[0] // platform
    type inferred (ordinary Java object) item.substring(1) // allowed, may throw an
                                                           // exception if item == null

Kotlin relies on type inference when a platform value is assigned to a Kotlin
variable, or you can define what type to expect. The best way to ensure the
correct nullability state of a reference coming from Java is to use nullability
annotations (for example, `@Nullable`) in your Java code. The Kotlin compiler
will represent these references as actual nullable or non-nullable types, not as
platform types.

Java Jetpack APIs have been annotated with `@Nullable` or `@NonNull` as needed,
and a similar approach has been taken in the
[Android 11 SDK](https://android-developers.googleblog.com/2020/03/handling-nullability-in-android-11-and.html).
Types coming from this SDK, that are used in Kotlin, will be represented as
correct nullable or non-nullable types.

Because of Kotlin's type system, we've seen apps have a major reduction in
`NullPointerException` crashes. For example, the Google Home app saw a 30%
reduction in crashes caused by null pointer exceptions during the year that it
migrated new feature development to Kotlin.