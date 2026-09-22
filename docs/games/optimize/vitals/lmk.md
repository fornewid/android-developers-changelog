---
title: https://developer.android.com/games/optimize/vitals/lmk
url: https://developer.android.com/games/optimize/vitals/lmk
source: md.txt
---

The Android [low memory killer (LMK) daemon](https://source.android.com/docs/core/perf/lmkd)
monitors the memory state of a running Android system and reacts to high memory
pressure by terminating the least essential processes. Android vitals tracks and
reports user-perceived LMK terminations in Google Play Console to help you
identify memory pressure issues affecting your users.

> [!NOTE]
> **Note:** For information on how to diagnose and resolve this issue, see [Low memory killers](https://developer.android.com/topic/performance/issues/lmk).

## LMK metric on Android vitals

Android vitals can help you monitor and improve your app's LMK rate. Android
vitals measures only one LMK rate: **User-perceived LMK rate**.

The metric reflects the percentage of your daily active users who experienced
at least one user-perceived LMK. A user-perceived LMK is an LMK that is likely
to have been noticed by the user. For example, this includes LMKs that happen
while your app is displaying an activity or running as a foreground service.
These terminations result in an immediate, non-graceful process exit.
To the end user, it looks like the app crashed, often bypassing standard lifecycle
state-saving mechanisms and resulting in lost user progress.

Android Vitals focuses on these process terminations because they serve as a
high-fidelity proxy for memory mismanagement issues. An LMK rate above 1%
indicates a critical need for immediate action. However, a lower LMK rate
doesn't necessarily mean the app's memory usage is healthy. That lower rate
might mean that the LMK daemon is frequently killing processes while they are in
the background, which degrades "warm start" performance and multitasking
fluidity.

You can find the metric under the **Stability** section in Android vitals:
![](https://developer.android.com/static/google/play/vitals/images/lmk-in-vital.png) **Figure 1.** Access **User-perceived LMK rate** in Android vitals.

As with similar core vital metrics, such as ANRs and crashes, you can filter
the metrics, compare your metrics with your peers, or monitor the metric's change for a
long period of time (up to 3 years). Data is available for existing apps
starting from 28 Jan 2025.
![](https://developer.android.com/static/google/play/vitals/images/lmk-overview.png) **Figure 2.** Overview of LMK rate in Android Vitals.