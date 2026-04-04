---
title: https://developer.android.com/games/optimize/adpf/fixed-performance-mode
url: https://developer.android.com/games/optimize/adpf/fixed-performance-mode
source: md.txt
---

**Released**: Android 11 (API level 30)

Android devices can change clocking dynamically based on the system load. This
behavior is good for power savings during use, but can make it difficult to get
reliable performance data. If you are trying to determine how fast a code
fragment can run for regression prevention, or if an optimization is repeatable,
your results won't be reliable if they aren't tested at fixed clock speeds. With
fixed clocks, you can do accurate A/B testing of performance without changes in
the CPU frequency being a factor.

Fixed-performance mode sets CPU and GPU clocks with an upper and lower bound.
This mode does not disable other dynamic performance behaviors, such as core
selection.

You can enable fixed-performance mode with the following adb command:

    adb shell cmd power set-fixed-performance-mode-enabled [true|false]

A device that is running in fixed-performance mode can still overheat because
the mode doesn't put the device into a thermally-sustainable state. Because of
this, we recommend the following for benchmark runs:

- Wait for the device to return to a thermally-sustainable state before starting the run.
- Monitor the thermal state of the device during testing to differentiate the impact between the benchmark code and thermal events.