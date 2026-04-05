---
title: https://developer.android.com/tools/logcat
url: https://developer.android.com/tools/logcat
source: md.txt
---

# Logcat command-line tool

Logcat is a command-line tool that dumps a log of system messages including
messages that you have written from your app with the
[Log](https://developer.android.com/reference/android/util/Log) class.

This page is about the command-line `logcat` tool, but you can also view log
messages from the **Logcat** window in Android Studio. For
information about viewing and filtering logs from Android Studio,
see [View and write logs with
Logcat](https://developer.android.com/studio/debug/am-logcat).

## Logging system overview


The Android logging system is a set of structured circular buffers maintained by the system
process `logd`. The set of available buffers is fixed and defined by the
system. The most relevant buffers are:

- `main`: Stores most application logs.
- `system`: Stores messages originating from the Android OS.
- `crash`: Stores crash logs. Each log entry has a priority, a tag that identifies the origin of the log, and the actual log message.

<br />


The primary C/C++ interface to the logging system is the shared library `liblog`
and its header `<android/log.h>`.
All language-specific logging facilities
(including [android.util.Log](https://developer.android.com/reference/android/util/Log))
eventually call the function
`__android_log_write`. By default, it calls the function
`__android_log_logd_logger`, which sends the log entry to `logd`
using a socket. Starting with API level 30, the logging function can be changed by calling
`__android_set_log_writer`. More information is available in the
[NDK documentation](https://developer.android.com/ndk/reference/group/logging).


Logs displayed by `adb logcat` undergo four levels of filtering:

Compile-time filtering
:   Depending on compilation settings, some logs may be completely
    removed from the binary. For example, ProGuard can be configured to remove calls to
    `Log.d` from Java code.

System property filtering
:   `liblog` queries a set of system properties to
    determine the minimum severity level to be sent to `logd`. If your logs have
    the tag `MyApp`, the following properties are checked and are expected to contain
    the first letter of the minimum severity (`V`, `D`, `I`,
    `W`, `E`, or `S` to disable all logs):

Application filtering
:   If none of the properties are set, `liblog` uses the minimum priority set by
    `__android_log_set_minimum_priority`. The default setting is
    `INFO`.

Display filtering
:   `adb logcat` supports additional filters that can reduce
    the amount of logs shown from `logd`. See the section about
    [filtering log output](https://developer.android.com/tools/logcat#filteringOutput) for more details.

## Command-line syntax


To run `logcat` through the `adb` shell, the general usage is:  

```
[adb] shell logcat [<option>] ... [<filter-spec>] ...
```

There is also a shorthand of `adb logcat`, but that just expands to
`adb shell logcat`.

### Options

`logcat` has a lot of options. What options are available will depend on the OS
version of the device you're using. To see help for `logcat` specific to the
device you're using, execute:  

```
    adb logcat --help
    
```

Note that because `logcat` is a tool for OS developers as well as app developers
(with app developers expected to use Android Studio instead) many of the options are only
usable as `root`.

## Filter log output

The tag of a log message is a short string that indicates the system component where the
message originates. For example, "View" for the view system.

The priority is one of the following character values, ordered from lowest to highest
priority:
-
  - `V`: Verbose (lowest priority)
  - `D`: Debug
  - `I`: Info
  - `W`: Warning
  - `E`: Error
  - `F`: Fatal
  - `S`: Silent (highest priority, where nothing is ever printed)
- To obtain a list of tags used in the system with priorities, run `logcat` and observe the first two columns of each message, given as `<priority>/<tag>`.
- The following is an example of brief `logcat` output obtained with the `logcat -v brief output` command. The output shows that the message relates to priority level "I" and tag "ActivityManager":  

```
I/ActivityManager(  585): Starting activity: Intent { action=android.intent.action...}
```
- To reduce the log output to a manageable level, restrict log output using *filter
  expressions*. Filter expressions let you indicate to the system the tag-priority combinations that you are interested in. The system suppresses other messages for the specified tags.
- A filter expression follows this format `tag:priority ...`, where `tag` indicates the tag of interest and `priority` indicates the minimum level of priority to report for that tag. Messages for that tag at or above the specified priority are written to the log. Supply any number of `tag:priority` specifications in a single filter expression. The series of specifications is whitespace-delimited.
- The following is an example of a filter expression that suppresses all log messages except those with the tag "ActivityManager" at priority "Info" or above and those with the tag "MyApp" with priority "Debug" or above:  

```
adb logcat ActivityManager:I MyApp:D *:S
```
- The final element in the preceding expression, `*:S`, sets the priority level for all tags to "silent", which ensures that only log messages with "ActivityManager" and "MyApp" are displayed. Using `*:S` ensures that log output is restricted to the filters that you have explicitly specified. `*:S` lets your filters serve as an allowlist for log output.
- **Note:** In some shells, the "`*`" character is reserved by the shell. If you are using such a shell, enclose the filter expression in quotes: `adb logcat
  "ActivityManager:I MyApp:D *:S"`
- The following filter expression displays all log messages with priority level "warning" and higher on all tags:  

```
adb logcat *:W
```
- If you're running `logcat` from your development computer instead of running it on a remote `adb` shell, you can also set a default filter expression by exporting a value for the environment variable `ANDROID_LOG_TAGS`:  

```
export ANDROID_LOG_TAGS="ActivityManager:I MyApp:D *:S"
```
- The `ANDROID_LOG_TAGS` filter is not exported to the emulator/device instance if you are running `logcat` from a remote shell or using `adb shell
  logcat`.

## Control log output format

- Log messages contain a number of metadata fields in addition to the tag and priority. You can modify the output format for messages so that they display a specific metadata field. To do so, use the `-v` option and specify one of the following supported output formats:
  - `brief`: Displays priority, tag, and PID of the process issuing the message.
  - `long`: Displays all metadata fields and separate messages with blank lines.
  - `process`: Displays PID only.
  - `raw`: Displays the raw log message with no other metadata fields.
  - `tag`: Displays the priority and tag only.
  - `thread:` A legacy format that shows priority, PID, and TID of the thread issuing the message.
  - `threadtime` (default): Displays the date, invocation time, priority, tag, PID, and TID of the thread issuing the message.
  - `time`: Displays the date, invocation time, priority, tag, and PID of the process issuing the message.
- When starting `logcat`, specify the output format you want by using the `-v` option:  

```
[adb] logcat [-v <format>]
```
- Here's an example that shows how to generate messages in `thread` output format:  

```
adb logcat -v thread
```
- You can only specify one output format with the `-v` option. However, you can specify as many modifiers as you need, provided they make sense. `logcat` ignores modifiers that don't make sense.

## Format modifiers

- Format modifiers change the `logcat` output. To specify a format modifier, use the `-v` option, as follows:  

```
adb logcat -b all -v color -d
```
- Every Android log message has a tag and a priority associated with it. You can combine any format modifier with any one of the following format options:
  - `brief`
  - `long`
  - `process`
  - `raw`
  - `tag`
  - `thread`
  - `threadtime`
  - `time`
- To format the following modifier details, enter `logcat -v --help` at the command line:
  - `color`: Shows each priority level with a different color.
  - `descriptive`: Shows log buffer event descriptions. This modifier affects event log buffer messages only and has no effect on the other non-binary buffers. The event descriptions come from the event-log-tags database.
  - `epoch`: Displays time in seconds starting from Jan 1, 1970.
  - `monotonic`: Displays time in CPU seconds starting from the last boot.
  - `printable`: Ensures that any binary logging content is escaped.
  - `uid`: If permitted by access controls, displays the UID or Android ID of the logged process.
  - `usec`: Displays the time, with precision in microseconds.
  - `UTC`: Displays the time as UTC.
  - `year`: Adds the year to the displayed time.
  - `zone`: Adds the local time zone to the displayed time.

## View alternative log buffers

- The Android logging system keeps multiple circular buffers for log messages, and not all of log messages are sent to the default circular buffer. To see additional log messages, run the `logcat` command with the `-b` option to request viewing of an alternate circular buffer. You can view any of these alternate buffers:
  - `radio`: Views the buffer that contains radio/telephony related messages.
  - `events`: Views the interpreted binary system event buffer messages.
  - `main`: Views the main log buffer (default), which doesn't contain system and crash log messages.
  - `system`: Views the system log buffer (default).
  - `crash`: Views the crash log buffer (default).
  - `all`: Views all buffers.
  - `default`: Reports `main`, `system`, and `crash` buffers.
- The usage of the `-b` option is:  

```
[adb] logcat [-b <buffer>]
```
- Here is an example of how to view a log buffer containing radio and telephony messages:  

```
adb logcat -b radio
```
- To specify multiple `-b` flags for all the buffers you want to print, enter the following:  

```
logcat -b main -b radio -b events
```
- Specify a single `-b` flag with a comma-separated list of buffers, for example:  

```
logcat -b main,radio,events
```

## Log from code

- The [Log](https://developer.android.com/reference/android/util/Log) class lets you create log entries in your code that display in the `logcat` tool. Common logging methods include:
  - [Log.v(String, String)](https://developer.android.com/reference/android/util/Log#v(java.lang.String, java.lang.String)) (verbose)
  - [Log.d(String, String)](https://developer.android.com/reference/android/util/Log#d(java.lang.String, java.lang.String)) (debug)
  - [Log.i(String, String)](https://developer.android.com/reference/android/util/Log#i(java.lang.String, java.lang.String)) (information)
  - [Log.w(String, String)](https://developer.android.com/reference/android/util/Log#w(java.lang.String, java.lang.String)) (warning)
  - [Log.e(String, String)](https://developer.android.com/reference/android/util/Log#e(java.lang.String, java.lang.String)) (error)
- For example, using the following call:  

### Kotlin

```kotlin
Log.i("MyActivity", "MyClass.getView() --- get item number $position")
```

### Java

```java
Log.i("MyActivity", "MyClass.getView() --- get item number " + position);
```
- `logcat` outputs something similar to the following:  

```
I/MyActivity( 1557): MyClass.getView() — get item number 1
```