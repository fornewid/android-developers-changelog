---
title: https://developer.android.com/tools/perfetto
url: https://developer.android.com/tools/perfetto
source: md.txt
---

# perfetto

`perfetto`is a tool that lets you collect performance information from Android devices via the[Android Debug Bridge (ADB)](https://developer.android.com/studio/command-line/adb). Invoke the`perfetto`tool using the`adb shell perfetto ...`command.`perfetto`uses various sources to collect performance traces from your device, such as:

- `ftrace`for information from the kernel
- `atrace`for user-space annotation in services and apps
- `heapprofd`for native memory usage information of services and apps

This page describes how to call`perfetto`and configure it to generate the desired output. For further information, refer to the[`perfetto`documentation](https://perfetto.dev/docs).

## Syntax

This section describes how to use ADB to call`perfetto`for different modes and generate a trace.

### Data source selection

`perfetto`includes the following two modes that determine the data sources it uses to record your trace:

- **light mode** : can select only a subset of data sources, specifically`atrace`and`ftrace`. However, this mode offers an interface similar to[`systrace`](https://developer.android.com/topic/performance/tracing/command-line).
- **normal mode** : gets its configuration in a protocol buffer and lets you leverage more of`perfetto`'s functionality by using data sources different from`atrace`and`ftrace`.

### General options

The following table lists the available options when using`perfetto`in either mode:

**Table 1.**List of available general perfetto tool options.

|                                         Option                                          |                                                                                                                                                                                                                                              Description                                                                                                                                                                                                                                               |
|-----------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `--background |` ` -d`                                                                  | `perfetto`immediately exits the command-line interface and continues recording your trace in background.                                                                                                                                                                                                                                                                                                                                                                                               |
| `--background-wait | -D`                                                                | Like`--background`, but waits (up to 30s) for all data sources to start before exiting. Exit code is zero if a successful acknowledgement is received and non-zero otherwise (error or timeout).                                                                                                                                                                                                                                                                                                       |
| `--alert-id`                                                                            | ID of the alert that triggered this trace.                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `--config-id`                                                                           | ID of the triggering config.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `--config-uid`                                                                          | UID of the app that registered the config.                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `--subscription-id`                                                                     | ID of the subscription that triggered this trace.                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `--out `<var translate="no">OUT_FILE</var>` |` ` -o `<var translate="no">OUT_FILE</var> | Specifies the desired path to the output trace file or`-`for`stdout`.`perfetto`writes the output to the file described in the preceding flags. The output format compiles with the format defined in[AOSP`trace.proto`](https://android.googlesource.com/platform/external/perfetto/+/refs/tags/android-q-preview-5/protos/perfetto/trace/trace.proto). *Note:* You must specify the full pathname of the output file. Typically the files should be written to the`/data/misc/perfetto-traces`folder. |
| `--upload`                                                                              | On completion, passes the trace to the package specified by the`IncidentReportConfig`message in the proto trace config.                                                                                                                                                                                                                                                                                                                                                                                |
| `--no-guardrails`                                                                       | Disables protections against excessive resource usage when enabling the`--upload`flag during testing.                                                                                                                                                                                                                                                                                                                                                                                                  |
| `--reset-guardrails`                                                                    | Resets the persistent state of the guardrails and exits for testing.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `--rsave-for-bugreport`                                                                 | If a trace with`bugreport_score`\> 0 is running, saves the trace into a file. Outputs the path when done.                                                                                                                                                                                                                                                                                                                                                                                              |
| `--query`                                                                               | Queries the service state and prints it as human-readable text.                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `--query-raw`                                                                           | Similar to`--query`, but prints raw proto-encoded bytes of`tracing_service_state.proto.`                                                                                                                                                                                                                                                                                                                                                                                                               |
| `--help | -h `                                                                          | Prints out help text for the`perfetto`tool.                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

### Light mode

The general syntax for using`perfetto`in light mode is as follows:  

```
 adb shell perfetto [ --time TIMESPEC ] [ --buffer SIZE ] [ --size SIZE ]
             [ ATRACE_CAT | FTRACE_GROUP/FTRACE_NAME | FTRACE_GROUP/* ]...
             --out FILE
```

The following table lists the available options when using`perfetto`in light mode:

**Table 2.** List of available`perfetto`tool options when using light mode.

|                                               Option                                               |                                                                          Description                                                                           |
|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `--time `<var translate="no">TIME</var>`[s|m|h] |` ` -t `<var translate="no">TIME</var>`[s|m|h]`   | Specifies the trace duration in seconds, minutes, or hours. For example,`--time 1m`specifies a trace duration of 1 minute. The default duration is 10 seconds. |
| `--buffer `<var translate="no">SIZE</var>`[mb|gb] |` ` -b `<var translate="no">SIZE</var>`[mb|gb]` | Specifies the ring buffer size in megabytes (mb) or gigabytes (gb). The default parameter is`--buffer 32mb`.                                                   |
| `--size `<var translate="no">SIZE</var>`[mb|gb] |` ` -s `<var translate="no">SIZE</var>`[mb|gb]`   | Specifies the max file size in megabytes (mb) or gigabytes (gb). By default,`perfetto`uses only in-memory ring-buffer.                                         |
| `--app | -a`                                                                                       | Android (atrace) app name                                                                                                                                      |

These options are followed by a list of event specifiers:

**Table 3.**List of event specifiers for light mode.

|                       Event                        |                                                                                                                                                                                Description                                                                                                                                                                                |
|----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <var translate="no">ATRACE_CAT</var>               | Specifies the`atrace`categories you want to record a trace for. For example, the following command traces Window Manager using`atrace`: ``` adb shell perfetto --out FILE wm ``` To record other categories, see this[list of`atrace`categories](https://android.googlesource.com/platform/frameworks/native/+/refs/tags/android-q-preview-5/cmds/atrace/atrace.cpp#100). |
| <var translate="no">FTRACE_GROUP/FTRACE_NAME</var> | Specifies the`ftrace`events you want to record a trace for. For example, the following command traces`sched/sched_switch`events: ``` adb shell perfetto --out FILE sched/sched_switch ```                                                                                                                                                                                 |

### Normal mode

The general syntax for using`perfetto`in normal mode is as follows:  

```
 adb shell perfetto [ --txt ] --config CONFIG_FILE --out FILE
```

The following table lists the available options when using`perfetto`in normal mode:

**Table 4.** List of available`perfetto`tool options when using normal mode.

|                                            Option                                             |                                                                                                                                                                                                                                                                                                                          Description                                                                                                                                                                                                                                                                                                                           |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `--config `<var translate="no">CONFIG_FILE</var>` | -c `<var translate="no">CONFIG_FILE</var> | Specifies the path to a configuration file. In normal mode, some configurations may be encoded in a configuration protocol buffer. This file must comply with the protocol buffer schema defined in[AOSP`trace_config.proto`](https://android.googlesource.com/platform/external/perfetto/+/refs/tags/android-q-preview-5/protos/perfetto/config/trace_config.proto). Select and configure the data sources using the`DataSourceConfig`member of the`TraceConfig`, as defined in[AOSP`data_source_config.proto`](https://android.googlesource.com/platform/external/perfetto/+/refs/tags/android-q-preview-5/protos/perfetto/config/data_source_config.proto). |
| `--txt`                                                                                       | Instructs`perfetto`to parse the config file as`pbtxt`. This flag is intended for local testing only, and it's not recommended that you enable it for production.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

## Supported data sources

This section describes the different sources that`perfetto`uses to generate your trace.

### ftrace

The`ftrace`data source allows`perfetto`to get events from the kernel.

Enable this source by setting[`ftrace_config`](https://android.googlesource.com/platform/external/perfetto/+/refs/tags/android-q-preview-5/protos/perfetto/config/ftrace/ftrace_config.proto)in the DataSourceConfig.

The events that can be enabled include:

- [Scheduling activity](https://android.googlesource.com/platform/external/perfetto/+/refs/tags/android-q-preview-5/protos/perfetto/trace/ftrace/sched.proto):

  - `sched/sched_switch`
  - `sched/sched_wakeup`
  - `sched/sched_wakeup_new`
  - `sched/sched_process_exec`
  - `sched/sched_process_exit`
  - `sched/sched_process_fork`
  - `sched/sched_process_free`
  - `sched/sched_process_hang`
  - `sched/sched_process_wait`
- Filesystem events:

  - [`ext4`](https://android.googlesource.com/platform/external/perfetto/+/refs/tags/android-q-preview-5/protos/perfetto/trace/ftrace/ext4.proto)
  - [`f2fs`](https://android.googlesource.com/platform/external/perfetto/+/refs/tags/android-q-preview-5/protos/perfetto/trace/ftrace/f2fs.proto)
  - [`block`](https://android.googlesource.com/platform/external/perfetto/+/refs/tags/android-q-preview-5/protos/perfetto/trace/ftrace/block.proto)
- [`atrace`events](https://android.googlesource.com/platform/external/perfetto/+/refs/tags/android-q-preview-5/protos/perfetto/trace/ftrace/print.proto)

Depending on your device, OS version, or kernel, more events might be available. For more information, refer to the[config protos](https://android.googlesource.com/platform/external/perfetto/+/refs/tags/android-q-preview-5/protos/perfetto/trace/ftrace/).

### Process Stats

The process stats data source allows you to get polled counters about the system and individual processes.

Enable this source by setting[`process_stats_config`](https://android.googlesource.com/platform/external/perfetto/+/refs/tags/android-q-preview-5/protos/perfetto/config/process_stats/process_stats_config.proto)and[`sys_stats_config`](https://android.googlesource.com/platform/external/perfetto/+/refs/tags/android-q-preview-5/protos/perfetto/config/sys_stats/sys_stats_config.proto)in the DataSourceConfig.

The data that`perfetto`generates includes:

- [System-wide](https://android.googlesource.com/platform/external/perfetto/+/refs/tags/android-q-preview-5/protos/perfetto/trace/sys_stats/sys_stats.proto)

  - `/proc/meminfo`
  - `/proc/vmstat`
  - `/proc/stat`
- [Per process](https://android.googlesource.com/platform/external/perfetto/+/refs/tags/android-q-preview-5/protos/perfetto/trace/ps/process_stats.proto)

  - `/proc/\<pid\>/status`
  - `/proc/\<pid\>/oom_score_adj`

Depending on your device, OS version, and kernel, more events might be available. To learn more, refer to the config protos for[`sys_stats`](https://android.googlesource.com/platform/external/perfetto/+/refs/tags/android-q-preview-5/protos/perfetto/config/sys_stats/sys_stats_config.proto)and[`process_stats`](https://android.googlesource.com/platform/external/perfetto/+/refs/tags/android-q-preview-5/protos/perfetto/config/process_stats/process_stats_config.proto).

### `heapprofd`

`heapprofd`lets you sample the causes of native memory use.

Enable this source by setting[`heapprofd_config`](https://android.googlesource.com/platform/external/perfetto/+/refs/tags/android-q-preview-5/protos/perfetto/config/profiling/heapprofd_config.proto)in the DataSourceConfig. This setting produces[`ProfilePackets`](https://android.googlesource.com/platform/external/perfetto/+/refs/tags/android-q-preview-5/protos/perfetto/trace/profiling/profile_packet.proto), including the Java frames of the callstack.

Additional information on how to use`heapprofd`can be found at[`perfetto.dev`](https://docs.perfetto.dev/#heapprofd).

### Other sources

Depending on your device, OS version, and kernel, more data sources might be available. To learn more, refer to the[data source config protos](https://android.googlesource.com/platform/external/perfetto/+/refs/tags/android-q-preview-5/protos/perfetto/config/data_source_config.proto).

Additional information about`perfetto`can be found at[perfetto.dev](https://perfetto.dev).