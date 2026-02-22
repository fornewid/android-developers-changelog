---
title: https://developer.android.com/topic/performance/tracing/on-device
url: https://developer.android.com/topic/performance/tracing/on-device
source: md.txt
---

Devices running Android 9 (API level 28) or higher include a system-level app
called System Tracing. This app is similar to the
[`systrace`](https://developer.android.com/topic/performance/tracing/command-line) command-line utility, but
the app lets you record traces directly from a test device itself, without
needing to plug in the device and connect to it over `adb`. You can then use the
app to share results from these traces with your development team.

Devices running Android 10 and higher record traces in Perfetto format, whereas
earlier devices record them in Systrace format. We recommend using the [Perfetto
trace viewer](https://ui.perfetto.dev/) to open both formats and
then analyze traces.

It helps to record traces when addressing performance-related bugs in your app,
such as slow startup, slow transitions, or UI jank.

## Record a system trace

The System Tracing app lets you record a system trace using **Quick Settings
tile** or a menu within the app itself. The following sections describe how to
complete the recording process using these interfaces.
| **Note:** As part of your development workflow, you might submit an on-device bug report. It's important to file this type of bug report after you finish recording a system trace. That way, the bug report process itself isn't included in the recorded trace.

### Record using Quick Settings tile

**Quick Settings tile** is usually the more convenient way to complete the
on-device system tracing process.

#### Set up tile

If you're using System Tracing for the first time on your test device, or if you
don't see the **System Tracing** tile in your device's **Quick Settings** panel,
as shown in figure 2, complete the following setup steps:

1. [Enable developer options](https://developer.android.com/studio/debug/dev-options#enable).
2. Open the **Developer Options** settings screen.
3. In the **Debugging** section, select **System Tracing**. The System Tracing app opens, showing the app menu.
4. From the app menu, enable **Show Quick Settings tile** , as shown in figure 1.
   The system adds the **System Tracing** tile to the **Quick Settings** panel,
   as shown in figure 2:

   ![](https://developer.android.com/static/topic/performance/images/tracing/system-trace-menu-show-quick-settings-tile.png) **Figure 1.** The **Show Quick Settings tile** switch in the System Tracing app. ![](https://developer.android.com/static/topic/performance/images/tracing/quick-settings-systrace-icon.webp) **Figure 2.** The **System Tracing** tile within the **Quick Settings** panel.

   **Note:** By default, the system
   adds the **System Tracing** tile as the first tile in the **Quick
   Settings** panel. If you want the tile to appear in a different position,
   use the panel's edit mode to move the tile.

#### Complete a system trace recording

To record a system trace using the **Quick Settings** panel, complete the
following steps:

1. Tap the **System Tracing** tile, which has the label **Record trace**. The
   tile becomes enabled, and a persistent notification appears to notify you
   that the system is recording a trace, as shown in figure 3:

   ![Notification with the message 'Trace is being recorded. Tap to stop
   tracing.'](https://developer.android.com/static/topic/performance/images/tracing/on-device-systrace-start.webp) **Figure 3.** Persistent notification that appears after starting an on-device system trace.
2. Perform the actions in your app that you want the system to inspect.

   | **Note:** You can record bugs that are difficult to reproduce by leaving System Tracing running in the background and then stopping System Tracing soon after the bug occurs. System Tracing saves a device's activity to a rolling buffer, which holds 10-30 seconds of events.
3. Stop tracing by tapping either the **System Tracing** tile in the **Quick
   Settings** panel or on the System Tracing notification.

   The system displays a new notification that contains the message "Saving
   trace". When saving is complete, the system dismisses the notification and
   displays a third notification, confirming that your trace is saved and that
   you're ready to [share the system trace](https://developer.android.com/topic/performance/tracing/on-device#share-trace), as shown in figure
   4:
   ![Notification with the message 'Trace saved. Tap to share your
   trace.'](https://developer.android.com/static/topic/performance/images/tracing/on-device-systrace-saved.webp) **Figure 4.** Persistent notification that appears after the system finishes saving a recorded trace.

### Record using app menu

The app menu lets you configure several advanced settings related to system
tracing and provides a switch for starting and stopping a system trace.

To record a system trace using the System Tracing app menu, complete the
following steps:

1. [Enable developer options](https://developer.android.com/studio/debug/dev-options#enable).
2. Open the **Developer Options** settings screen. In the **Debugging** section,
   select **System Tracing**. The System Tracing app opens.

   Alternatively, if you [set up the **System Tracing** tile](https://developer.android.com/topic/performance/tracing/on-device#set-up-tile),
   you can tap and hold the tile to enter the System Tracing app.
3. Make sure **Trace debuggable applications** is selected to include apps that
   have debugging enabled in the system trace.

4. Optionally, choose the **Categories** of system and sensor calls to trace,
   and choose a **Per-CPU buffer size** in KB. Choose categories that correspond
   to the use case that you're testing, such as the **Audio** category for
   testing Bluetooth operations or the **Memory** category for heap allocations.

   | **Note:** These categories serve as app-level settings, so the system uses these categories when [using the **Quick Settings** tile](https://developer.android.com/topic/performance/tracing/on-device#quick-settings), too. In addition, these settings persist across device reboots.
5. Optionally, select **Long traces** to enable traces that are saved
   continuously to device storage. For this option, set limits for the **Maximum
   long trace size** and **Maximum long trace duration**.

6. Enable the **Record trace** switch, highlighted in figure 5. The tile becomes
   enabled, and a persistent notification appears to notify you that the system
   is recording a trace, as shown in [figure 3](https://developer.android.com/topic/performance/tracing/on-device#systrace-start).

   ![](https://developer.android.com/static/topic/performance/images/tracing/system-trace-menu-record-trace.png) **Figure 5.** The **Record trace** switch in the System Tracing settings.
7. Perform the actions in your app that you want the system to inspect.

   | **Note:** You can record bugs that are difficult to reproduce by leaving System Tracing running in the background, then stopping System Tracing soon after the bug occurs. By default, System Tracing saves a device's activity to a rolling buffer, which holds 10-30 seconds of events. If **Long traces** is enabled, the device's activity is saved continuously to device storage up to the limits you set.
8. Stop tracing by disabling the **Record trace** switch.

   The system displays a new notification that contains the message "Saving
   trace". When saving is complete, the system dismisses the notification and
   displays a third notification, confirming that your trace is saved and that
   you're ready to [share the system trace](https://developer.android.com/topic/performance/tracing/on-device#share-trace), as shown in
   [figure 4](https://developer.android.com/topic/performance/tracing/on-device#systrace-saved).

## Share a system trace

The System Tracing app helps you share system trace results as part of several
different workflows. On a device running Android 10 (API level 29) or higher, trace
files are saved with the `.perfetto-trace` filename extension and can be opened
in the [Perfetto UI](https://ui.perfetto.dev/#!/). On a device
running an earlier version of Android, trace files are saved with the `.ctrace`
filename extension, which denotes the Systrace format.

### Share as a message

System Tracing lets you share your collected trace with other apps on your
device. You can send the trace to your development team through an email or a
bug-tracking app without needing to connect a device to your development
machine.

After you record a system trace, tap on the notification that appears on
the device, like the one shown in [figure 4](https://developer.android.com/topic/performance/tracing/on-device#systrace-saved). The platform's
intent picker appears, letting you share your trace using the messaging app of
your choice.

### Share from the Files app

On devices running Android 10 (API level 29) or higher, traces are shown in the
Files app. You can share a trace from this app.

### Download report using ADB

You can also extract a system trace from a device using `adb`. Connect the
device used to record the trace to your development machine, then run the
following commands in a terminal window:  

```
cd /path-to-traces-on-my-dev-machine && \
  adb pull /data/local/traces/ .
```

## Convert between trace formats

You can convert Perfetto trace files to the Systrace format. See [Converting
between trace formats](https://docs.perfetto.dev/#/traceconv.md)
for more information.

## Create an HTML report

When sharing your trace, the report itself is in a `.perfetto-trace` file on
devices running Android 10
or higher, or a `.ctrace` file for all other versions.

Create an HTML report from the trace file using a [web-based UI](https://developer.android.com/topic/performance/tracing/on-device#web-ui) or
from the [command line](https://developer.android.com/topic/performance/tracing/on-device#command-line).

### Web-based UI

Use the [Perfetto UI](https://perfetto.dev/#/running.md) to open
the trace file and generate the report.

For a Perfetto file, click **Open trace file** . For a Systrace file, click
**Open with legacy UI** . The legacy UI has the same look and feel as the
[**Systrace report**](https://developer.android.com/topic/performance/tracing/navigate-report).

### Command line

Run the following commands in a terminal window to generate an HTML report
from the trace file:  

```
cd /path-to-traces-on-my-dev-machine && \
  systrace --from-file trace-file-name{.ctrace | .perfetto-trace}
```

If you don't already have the `systrace` command-line program, you can download
it from the
[Catapult](https://github.com/catapult-project/catapult/tree/main/systrace)
project on GitHub, or directly from the [Android Open Source
Project](https://android.googlesource.com/platform/external/chromium-trace/+/main/catapult/systrace/systrace/).

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Benchmark in Continuous Integration](https://developer.android.com/topic/performance/benchmarking/benchmarking-in-ci)
- [Capture a system trace on the command line](https://developer.android.com/topic/performance/tracing/command-line)