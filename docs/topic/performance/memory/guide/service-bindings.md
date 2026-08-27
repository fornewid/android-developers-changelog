---
title: https://developer.android.com/topic/performance/memory/guide/service-bindings
url: https://developer.android.com/topic/performance/memory/guide/service-bindings
source: md.txt
---

App processes on Android do not exist in isolation. Applications often rely on
services provided by other applications or the system itself. When one process
connects to another via a **Service Binding**, it creates a dependency that has
a profound impact on how the Android framework manages memory.

## Process states and OOM scores

The Android framework uses **Process States** to track the importance of each
running process. These states are then used by the `OomAdjuster` to assign an
**OOM Score Adjustment** (`oom_score_adj`) value, ranging from -1000 to 1000.

A lower `oom_score_adj` means the process is more important and less likely to
be killed by the Low Memory Killer (LMK).

### Common process states

The following table shows some of the most common process states and their
typical `oom_score_adj` values. For a complete and up-to-date list, refer to
`android.app.ActivityManager` and `com.android.server.am.psc.Constants` in the
Android source code.

| Process State (Abbr.) | Description | Typical `oom_score_adj` |
|---|---|---|
| **PER** (Persistent) | System processes that must always run (e.g., Telephony). | -800 |
| **TOP** | The process the user is currently interacting with. | 0 |
| **VIS** (Visible) | The process has a visible activity (e.g., behind a translucent dialog). | 100 |
| **PERC** (Perceptible) | Background process the user is aware of (e.g., music playback). | 200 |
| **FGS** | Process hosting a Foreground Service. | 0 to 200 (varies) |
| **BTOP** (Bound Top) | Process bound by a TOP application. | 100 |
| **BFGS** | Bound Foreground Service (typically system-bound). | 0 |
| **PREV** (Previous) | The last process the user was in before the current one. | 700 |
| **CACHED** | Background apps that can be killed safely. | 900 to 999 |

## The impact of service bindings

When a client process (e.g., an app in the `TOP` state) binds to a service in a
server process, the server process often **inherits** an elevated priority. This
ensures that the service remains available as long as the client needs it.

![Diagram showing process A (TOP) calling bindService() via system_server,
elevating process B to BTOP](https://developer.android.com/static/topic/performance/memory/guide/images/service-bindings/binding-inheritance.png)

### Controlling inheritance with BIND flags

Inheritance is the default behavior when using `Context.BIND_AUTO_CREATE`.
However, developers can control how the binding affects the target process's
importance using various flags in `bindService()`.

#### Key BIND flags for OOM score

The following flags are most relevant when managing system-wide memory pressure:

- **`BIND_AUTO_CREATE`**: The most common flag. It ensures the service process is started and kept alive as long as the binding exists. By default, it also elevates the server process priority to match the client.
- **`BIND_NOT_FOREGROUND`** : Prevents the target service's process from being raised to the foreground **scheduling** priority (CPU priority). However, it **still allows** the memory priority (`oom_score_adj`) to be elevated. This is useful for background work that shouldn't compete with the UI for CPU cycles but should still be protected from being killed.
- **`BIND_WAIVE_PRIORITY`** : A very strong flag that instructs the system **not** to impact the scheduling or memory management priority of the target process. The service process will be managed as if it were a regular background process on the LRU list, making it eligible for OOM killing even while bound.
- **`BIND_ABOVE_CLIENT`** : Indicates the service is more important than the client app itself. When the system needs to reclaim memory, it will prefer killing the client app before killing the bound service. This is "stronger" than `BIND_AUTO_CREATE` as it provides an extra layer of protection for the service at the expense of the client.
- **`BIND_NOT_PERCEPTIBLE`** : Lowers the target service's importance to below `PERCEPTIBLE` level, allowing the system to reclaim its memory to make room for more critical user-perceptible processes.

## Hands-on: observing binding effects

We will use the **MemoryLab** application to demonstrate how a binding from a
`TOP` app affects the state of a separate process.

### 1. Launch MemoryLab

The following command launches the app. After it opens, **ensure the app stays
in the foreground** (do not press Home or switch apps yet).

    adb shell am start -n com.android.memorylab/.MainActivity

### 2. Identify processes

Check the process states before binding. `MemoryLab` runs its main UI in one
process and has a `RemoteService` that runs in a `:remote` process.

    adb shell dumpsys activity processes com.android.memorylab

Sample output snippet:

      Process OOM control (154 total, non-act at 7, non-svc at 7):
        Proc #0: fg       T/A/TOP  LCMNFUATI  t: 0 13470:com.android.memorylab/u0a417 (top-activity)
            oom: max=1001 curRaw=0 setRaw=0 cur=0 set=0
            state: cur=TOP  set=TOP   lastRss=0.00 lastCachedRss=0.00

You will see the main process `com.android.memorylab` in the `TOP` state. The
`:remote` process is not yet started.

### 3. Trigger binding

Send a broadcast to the app to trigger the service binding:

    adb shell am broadcast -a com.android.memorylab.LEAK_BINDER

### 4. Observe elevated state

Check the process states again:

    adb shell dumpsys activity processes | grep -A 10 "com.android.memorylab"

Sample output snippet:

      Proc #  1: vis      F/ /BTOP ---NFUATI  t: 0 13560:com.android.memorylab:remote/u0a417 (service)
        com.android.memorylab/.RemoteService<=Proc{13470:com.android.memorylab/u0a417}
        oom: max=1001 curRaw=100 setRaw=100 cur=100 set=100
        state: cur=BTOP set=BTOP  lastRss=0.00 lastCachedRss=0.00

The `:remote` process is now running and in the **BTOP** (Bound TOP) state with
an **`oom_score_adj`** of **100** . This is significantly more protected than a
typical background service (which would be at `500` or higher). The notation
`<=Proc{...}` shows which process is responsible for this priority elevation.

### 5. Send to background

Press the **HOME** button on the device. Check the states again:

    adb shell dumpsys activity processes | grep -A 10 "com.android.memorylab"

Sample output snippet:

        Proc #  2: prev     b/ /LAST ---I  t: 0 13560:com.android.memorylab:remote/u0a417 (service)
            com.android.memorylab/.RemoteService<=Proc{13470:com.android.memorylab/u0a417}
            oom: max=1001 curRaw=700 setRaw=700 cur=700 set=700
            state: cur=LAST set=LAST  lastRss=0.00 lastCachedRss=0.00
        Proc #  1: prev     b/ /LAST ---I  t: 0 13470:com.android.memorylab/u0a417 (previous)
            oom: max=1001 curRaw=700 setRaw=700 cur=700 set=700
            state: cur=LAST set=LAST  lastRss=209MB lastCachedRss=0.00

Now both processes have shifted to a lower priority state (**PREV** /
`oom_score_adj` **700** ), because the client process is no longer `TOP`. (Note:
`LAST` in the state dump refers to the `LAST_ACTIVITY` internal state, which
maps to `PREV` in high-level summaries).

## Analyzing with procstats

The `procstats` tool provides a historical view of these states.

    # View stats for MemoryLab over the last hour
    adb shell dumpsys procstats --hours 1 com.android.memorylab

Sample output snippet:

      *   com.android.memorylab / u0a417 / v37:
          *   Prc com.android.memorylab / u0a417 / v37:
                 TOTAL: 0.89% (0.00-0.00-0.00/0.00-0.00-0.00/210MB-210MB-210MB over 1)
                   Top: 0.89% (0.00-0.00-0.00/0.00-0.00-0.00/210MB-210MB-210MB over 1)
          *   Prc com.android.memorylab:remote / u0a417 / v37:
                 TOTAL: 0.19%
               Bnd Top: 0.19%

Here, **`Bnd Top`** indicates the percentage of time the remote process spent
being bound by an application in the `TOP` state.

## Capturing and analyzing bindings with Perfetto

While `dumpsys` gives you a snapshot, Perfetto allows you to see the exact
moment a binding occurs and how the OOM score changes in real-time.

### 1. Record a trace

Use a configuration that includes `linux.process_stats` and the `am` atrace category:

    adb shell perfetto -c - --txt -o /data/misc/perfetto-traces/service_bindings.perfetto-trace <<EOF
    buffers: { size_kb: 65536 }
    data_sources: {
        config {
            name: "linux.process_stats"
            process_stats_config { proc_stats_poll_ms: 100 }
        }
    }
    data_sources: {
        config {
            name: "linux.ftrace"
            ftrace_config { ftrace_events: "am/am_proc_bound" }
        }
    }
    duration_ms: 15000
    EOF

### 2. Query OOM score transitions

Using PerfettoSQL, you can see how the OOM score of the remote process changed
relative to the UI process:

    SELECT ts, p.name, value AS oom_score_adj
    FROM counter c
    JOIN process_counter_track t ON c.track_id = t.id
    JOIN process p USING (upid)
    WHERE p.name LIKE 'com.android.memorylab%'
      AND t.name = 'oom_score_adj'
    ORDER BY ts;

### 3. Identify binding events

To see exactly when a binding dependency was established and which process
initiated it, use this query:

    SELECT
        s.ts,
        p.name AS process_name,
        t.name AS thread_name,
        s.name AS slice_name
    FROM slice s
    JOIN thread_track tt ON s.track_id = tt.id
    JOIN thread t USING (utid)
    JOIN process p USING (upid)
    WHERE s.name LIKE 'bindService:{com.android.memorylab%';

## System-to-app bindings

The Android system itself often binds to services in third-party apps to provide
core functionality. Often the goal of these bindings is **latency reduction**.
By keeping a process alive and in memory, the system avoids the costly overhead
of a "cold start" (loading the APK, initializing the runtime, and creating the
Application object) when a critical user interaction occurs. Other bindings
exist to prevent frequent cold starts for apps that need to handle streams of
background events.

Here are some real-world examples you can observe on a typical device:

### `VoiceInteractor`

Users expect a digital assistant to be embedded in their phone OS, to be able to
summon it instantaneously with a spoken hotword or a quick input gesture, and
for the interaction to be smooth and seamless.

When an assistant trigger occurs (such as the "OK Google" hotword on Google
Pixel phones), the digital assistant needs to respond instantly. To ensure this,
`system_server` maintains a permanent binding to the [voice interaction
service](https://developer.android.com/reference/android/app/VoiceInteractor) that's selected by the user.

![Diagram showing system_server binding to the Google App's interactor process](https://developer.android.com/static/topic/performance/memory/guide/images/service-bindings/voice-interaction.png)

If you check the process states (e.g., using `dumpsys activity processes`), you
might see a process like `com.google.android.googlequicksearchbox:interactor` in
the `BFGS` (Bound Foreground Service) state, kept alive by a binding from
`system_server` (UID 1000).

### `NotificationListenerService`

For some system-to-app bindings, the goal is not latency, but rather preventing
frequent cold starts.
[`NotificationListenerService`](https://developer.android.com/reference/android/service/notification/NotificationListenerService),
a service that receives calls from the system when new notifications are posted
or removed, is a prime example. A typical smartphone user may receive hundreds
of notifications throughout the day. If the system unbound from a notification
listener, that app's process would likely drop into the cached state and may be
killed by the LMK.

When the next notification arrives - potentially seconds later - the system
would be forced to cold start the app's process all over again just to deliver
the event. This constant cycle of killing and cold starting would consume far
more CPU and battery than simply keeping the process bound and alive in the
background.

### The launcher's "-1 screen" (news feed)

Modern Launcher apps typically combine the core navigational functionality (home
icons and widgets) with a news feed that's available on one of the launcher
screens and is seamlessly integrated with the Launcher UX. The news feed may be
provided by another app. For instance, on Google Pixel the Launcher integrates
with a feed that's provided by the Google app.

When you swipe left on your home screen to view the news feed, the transition
must be smooth. The launcher achieves this by binding to a service interface in
the app that provides the news feed, and maintaining that binding alive for as
long as the launcher is alive. This keeps the feed content rendered and ready in
memory even when you aren't looking at it.

### Other common examples

- **The Launcher (HOME_APP_ADJ)** : The launcher app (Home) has its own special slot in the priority list. While not always bound by a service, it is assigned the `HOME_APP_ADJ` (typically **600** ). The system prefers to keep the launcher alive, because the user returns to it frequently. In fact, the system would prefer to kill the previously used app (`PREV_APP_ADJ = 700`) than to kill the launcher, because killing the launcher would result in a sluggish user experience when exiting any app as the user will need to wait for the launcher to be cold started.
- **Input Method Editor (IME)**: When you are typing, the system binds to your chosen keyboard app (e.g., Gboard). This keeps the keyboard process in an elevated state even if the keyboard is temporarily hidden. This ensures the keyboard can reappear instantly when you tap another text field.
- **NFC Payments**: When you tap your phone to pay, the system binds to the NFC payment service (e.g., Google Wallet). These transactions often have strict real-time requirements from the merchant terminal. If the payment app had to cold start, the transaction could time out and fail.

## Tradeoffs and the performance cliff

While bindings are necessary for performance and correctness, they come at a
cost to the system's memory health.

- **Reduced Flexibility** : Every bound process is a process the LMK **cannot** easily kill. This reduces the "cushion" of cached processes that the system can use to free up memory under pressure.
- **Aggravating the Performance Cliff**: If too many processes are bound, the system may find itself with almost no killable background processes. When memory pressure increases, the system will "fall off the performance cliff" much faster, as it is forced to kill more important processes or thrash the page cache.

*** ** * ** ***

**[← Locality](https://developer.android.com/topic/performance/memory/guide/locality) \| [↑ Up](https://developer.android.com/topic/performance/memory/guide) \| [System-wide
→](https://developer.android.com/topic/performance/memory/guide/system-wide-memory)**