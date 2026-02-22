---
title: https://developer.android.com/games/optimize/adpf
url: https://developer.android.com/games/optimize/adpf
source: md.txt
---

This guide describes how to use the Android Dynamic Performance Framework (ADPF) to optimize games based on the dynamic thermal and CPU management features on Android. The focus is on games, but you can also use the features for other performance-intensive apps.

ADPF is a set of APIs that allow games and performance-intensive apps to interact more directly with power and thermal systems of Android devices. With these APIs, you can monitor the dynamic behavior on Android systems and optimize game performance at a sustainable level that doesn't overheat devices.

Mobile SoCs and Android have more dynamic performance behaviors than desktops and consoles. These behaviors include thermal state management, varying CPU clocks, and varying CPU core types. This combined with the increasingly diverse core topology of SoCs creates challenges when trying to ensure that your game can take advantage of this behavior without negatively impacting device performance. ADPF provides some of this information in order to make performance more predictable.

Here are the main ADPF features:

- **Thermal API**: Monitor the thermal state of a device so that the application can proactively adjust workload before it becomes unsustainable.
- **Game Mode API \& Game State API**: Enable game play optimization by prioritizing performance or battery life characteristics, based on user's settings and game specific configurations.
- **Fixed Performance Mode**: Enable fixed-performance mode on a device during benchmarking to get measurements that aren't altered by dynamic CPU clocking.
- **Power Efficiency Mode** : Tells the session that the threads in Performance Hint Session can be safely scheduled to prefer power efficiency over performance. ([Available in Android 15](https://developer.android.com/reference/android/os/PerformanceHintManager.Session#setPreferPowerEfficiency(boolean)))