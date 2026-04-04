---
title: Generate Trace Logs by Instrumenting Your App  |  Android Studio  |  Android Developers
url: https://developer.android.com/studio/profile/generate-trace-logs
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Android Studio](https://developer.android.com/studio)
* [IDE guides](https://developer.android.com/studio/intro)

# Generate Trace Logs by Instrumenting Your App Stay organized with collections Save and categorize content based on your preferences.




To generate a method trace of your app's execution, you can instrument your app
using the `Debug`
class. Instrumenting your app this way gives you more control over exactly when
the device starts and stops recording tracing information. The device also saves
your trace logs using the names you specify, so you can easily identify each log
later. You can then view each trace log using the Android Studio
[CPU Profiler](/studio/profile/cpu-profiler).

You can also
[start and stop tracing in the CPU Profiler](/studio/profile/cpu-profiler#method_traces)
without instrumenting your app's code.

Before you start generating trace logs, make sure your app has added logic to
save trace logs to its [app-specific
directory](/training/data-storage/app-specific).

## Instrument your app

To create trace logs, call `startMethodTracing()`
where you want the system to start logging tracing data.

In the call, you can specify the name for the
`.trace` file, and the system saves it to a package-specific
directory that's intended for persistent app data on the target device—this is
the same directory that is returned by
`getExternalFilesDir()`
and is located in the `~/sdcard/` directory on most devices.
This file contains the binary method trace data and a mapping table with thread
and method names. To stop tracing, call
`stopMethodTracing()`.

The following sample starts and stops recording a trace log with the name
`sample.trace`:

### Kotlin

```
// Starts recording a trace log with the name you provide. For example, the
// following code tells the system to start recording a .trace file to the
// device with the name "sample.trace".
Debug.startMethodTracing("sample")

// The system begins buffering the generated trace data, until your
// application calls <code><a href="/reference/android/os/Debug.html#stopMethodTracing()">stopMethodTracing()</a></code>, at which time it writes
// the buffered data to the output file.
Debug.stopMethodTracing()
```

### Java

```
// Starts recording a trace log with the name you provide. For example, the
// following code tells the system to start recording a .trace file to the
// device with the name "sample.trace".
Debug.startMethodTracing("sample");
...
// The system begins buffering the generated trace data, until your
// application calls <code><a href="/reference/android/os/Debug.html#stopMethodTracing()">stopMethodTracing()</a></code>, at which time it writes
// the buffered data to the output file.
Debug.stopMethodTracing();
```

Note that if your app calls the
`startMethodTracing()`
again without changing the name of the trace log, it overwrites the existing log
saved to the device. To learn how to dynamically change the name of each trace
log, go to the section about [saving multiple logs](#save_multiple_logs).

If the system reaches the maximum buffer size before you call
`stopMethodTracing()`,
the system stops tracing and sends a notification to the console.
The methods that start and stop traces work across your entire app process. That
is, you could call
`startMethodTracing()`
in your activity's
`onCreate(Bundle)`
method, and call `stopMethodTracing()`
in that activity's `onDestroy()`
method.

Note that your app runs more slowly when profiling is enabled. That is, you
shouldn't use the profiling data to determine absolute timings (such as, "method
`foo()` takes 2.5 seconds to run"). The timing information in the trace logs are
useful only when comparing it to previous trace logs, so you can see if recent
changes make your app faster or slower.

When deploying to devices running Android 5.0 (API level 21) and higher, you can
use sample-based profiling to profile with less runtime performance impact. To
enable sample profiling, call
`startMethodTracingSampling()`
(instead of calling `startMethodTracing()`) with a specified sampling
interval. The system gathers samples periodically until your app calls
`stopMethodTracing()`.

### Save multiple logs

If your app starts and stops a method trace multiple times without specifying a
new name for the trace log, the device overwrites the older trace log with the
new one—that is, it only keeps the most recent trace log. To save multiple
trace logs to your device, dynamically rename the trace log each time your app
calls `startMethodTracing()`.
The sample below uses the `SimpleDateFormat`
class to include the current date and time when naming each trace log:

### Kotlin

```
// Uses the <code><a href="/reference/java/text/SimpleDateFormat.html">SimpleDateFormat</a></code> class to create a String with
// the current date and time.
val dateFormat: DateFormat = SimpleDateFormat("dd_MM_yyyy_hh_mm_ss", Locale.getDefault())
val logDate: String = dateFormat.format(Date())
// Applies the date and time to the name of the trace log.
Debug.startMethodTracing("sample-$logDate")
```

### Java

```
// Uses the <code><a href="/reference/java/text/SimpleDateFormat.html">SimpleDateFormat</a></code> class to create a String with
// the current date and time.
SimpleDateFormat dateFormat =
        new SimpleDateFormat("dd_MM_yyyy_hh_mm_ss", Locale.getDefault());
String logDate = dateFormat.format(new Date());
// Applies the date and time to the name of the trace log.
Debug.startMethodTracing(
        "sample-" + logDate);
```

## Access trace logs on the device

After the system creates the trace log on your device, you can access the file
in one of the following ways:

* [Use the Device Explorer](/studio/debug/device-file-explorer).
  To open the Device Explorer, click
  **View > Tool Windows > Device Explorer** (or click the
  **Device Explorer**
  ![](/static/studio/images/buttons/device-explorer-icon.png) button in the tool window bar). As shown in figure 1
  you can locate the `.trace` files by navigating to your app's
  package-specific directory.

  ![](/static/studio/images/profile/locating_log_with_device_explorer-2X.png)

  **Figure 1.** Locating the trace logs using the Device Explorer.
* Copy the file to your local machine using the `adb pull` command.
  The command below copies a trace log named `sample.trace` from the device to
  the `~/Documents/trace-logs/` directory of your local machine.

  ```
  adb pull path-on-device/sample.trace ~/Documents/trace-logs/
  ```

You can then
[import the trace file](/studio/profile/import-traces) with the CPU Profiler.