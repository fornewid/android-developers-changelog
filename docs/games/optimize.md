---
title: https://developer.android.com/games/optimize
url: https://developer.android.com/games/optimize
source: md.txt
---

# Configure system tracing

You can configure[system tracing](https://developer.android.com/topic/performance/tracing)to capture a CPU and thread profile of your app over a short period of time. Then you can use the output report from a system trace to improve your game's performance.

## Set up a game-based system trace

The Systrace tool is available in two ways:

- [A command-line program](https://developer.android.com/topic/performance/tracing/command-line)
- [An on-device service](https://developer.android.com/topic/performance/tracing/on-device)

Systrace is a low-level tool that:

- **Provides ground truth**. Systrace captures output directly from the kernel, so the metrics that it captures are nearly identical to those that a series of system calls would report.
- **Consumes few resources**. Systrace introduces very low overhead on the device, usually less than 1%, because it streams data into an in-memory buffer.

### Optimal settings

It's important to give the tool a reasonable set of arguments:

- **Categories:** The best set of categories to enable for a game-based system trace are: {`sched`,`freq`,`idle`,`am`,`wm`,`gfx`,`view`,`sync`,`binder_driver`,`hal`,`dalvik`}.
- **Buffer size:** A general rule is that a buffer size of 10 MB per CPU core allows for a trace that's about 20 seconds long. For example, if a device has a two quad-core CPUs (8 cores total), an appropriate value to pass into the`systrace`program is 80,000 KB (80 MB).

  If your game performs a great deal of context-switching, increase the buffer to 15 MB per CPU core.
  | **Note:** In order to request a large buffer size, the device must have enough memory available for all cores, and each piece of memory per core must be contiguous. For example, if you attempt to capture a system trace on an 8-core device with a buffer size of 80 MB, the device must have 640 MB available, and each 80-MB piece of memory must be available as a contiguous chunk.
- **Custom events:** If you[define custom events](https://developer.android.com/topic/performance/tracing/custom-events)to capture in your game, enable the`-a`flag, which allows Systrace to include these custom events in the output report.

If you're using the`systrace`command-line program, use the following command to capture a system trace that applies best practices for category set, buffer size, and custom events:  

```
python systrace.py -a com.example.myapp -b 80000 -o my_systrace_report.html \
  sched freq idle am wm gfx view sync binder_driver hal dalvik
```

If you're using the Systrace system app on a device, complete the following steps to capture a system trace that applies best practices for category set, buffer size, and custom events:

1. Enable the**Trace debuggable applications**option.

   To use this setting, the device must have 256 MB or 512 MB available (depending on whether the CPU has 4 or 8 cores), and each 64-MB piece of memory must be available as a contiguous chunk.
2. Choose**Categories**, then enable the categories in the following list:

   - `am`: Activity Manager
   - `binder_driver`: Binder Kernel driver
   - `dalvik`: Dalvik VM
   - `freq`: CPU Frequency
   - `gfx`: Graphics
   - `hal`: Hardware Modules
   - `idle`: CPU Idle
   - `sched`: CPU Scheduling
   - `sync`: Synchronization
   - `view`: View System
   - `wm`: Window Manager
3. Enable**Record tracing**.

4. Load your game.

5. Perform the interactions in your game corresponding to the gameplay whose device performance you want to measure.

6. Shortly after you encounter undesirable behavior in your game, turn system tracing off.

You've captured the performance statistics needed to further analyze the issue.

To save disk space, on-device system traces save files in a compressed trace format (`*.ctrace`). To uncompress this file when generating a report, use the command-line program and include the`--from-file`option:  

```
python systrace.py --from-file=/data/local/traces/my_game_trace.ctrace \
  -o my_systrace_report.html
```

## Improve specific performance areas

This section highlights several common performance concerns in mobile games and describes how to identify and improve these aspects of your game.

### Load speed

Players want to get into your game's action as quickly as possible, so it's important to improve your game's load times as much as possible. The following measures usually help load times:

- **Perform*lazy loading*.**If you use the same assets across consecutive scenes or levels in your game, load these assets only once.
- **Reduce the size of your assets.**That way, you can bundle uncompressed versions of these assets with your game's APK.
- **Use a disk-efficient compression method.** An example of such a method is[zlib](https://www.zlib.net/).
- **Use[IL2CPP](https://docs.unity3d.com/Manual/IL2CPP.html)instead of mono**. (Applies only if you're using Unity.) IL2CPP provides better execution performance for your C# scripts.
- **Make your game multithreaded.** For more details, see the[framerate consistency](https://developer.android.com/games/optimize#framerate-consistency)section.

### Framerate consistency

One of the most important elements of gameplay experience is achieving a consistent framerate. To make this goal easier to achieve, follow the optimization techniques discussed in this section.

#### Multithreading

When developing for multiple platforms, it's natural to place all activity within your game in a single thread. Although this method of execution is simple to implement in many game engines, it's far from optimal when running on Android devices. As a result, single-threaded games often load slowly and lack a consistent framerate.

The Systrace shown in Figure 1 displays behavior that's typical of a game running on only one CPU at a time:

![Diagram of threads within a system trace](https://developer.android.com/static/images/games/systrace-single-threaded.svg)
**Figure 1.**Systrace report for a single-threaded game

<br />

To improve your game's performance,**make your game multithreaded**. Typically, the best model is to have 2 threads:

- A*game thread*, which contains your game's main modules and sends render commands.
- A*render thread*, which receives render commands and translates them into graphics commands that a device's GPU can use to display a scene.

The Vulkan API expands upon this model, given its capability to push 2 common buffers in parallel. Using this feature, you can distribute multiple render threads across multiple CPUs, further improving a scene's rendering time.

You can also make some engine-specific changes to enhance your game's multithreading performance:

- If you're developing your game using the Unity game engine, enable the**Multithreaded Rendering** and**GPU Skinning**options.
- If you're using a custom rendering engine, make sure that the render command pipeline and graphics command pipeline are aligned correctly; otherwise, you could introduce delays in displaying your game's scenes.

After applying these changes, you should see your game occupying at least 2 CPUs simultaneously, as shown in Figure 2:

![Diagram of threads within a system trace](https://developer.android.com/static/images/games/systrace-multi-threaded.svg)
**Figure 2.**Systrace report for a multi-threaded game

<br />

#### UI element loading

![Diagram of a frame stack within a system trace](https://developer.android.com/static/images/games/systrace-frame-stack.svg)**Figure 3.**Systrace report for a game that's rendering dozens of UI elements at the same time

When creating a feature-rich game, it's tempting to show many different options and actions to the player at the same time. To maintain a consistent framerate, however, it's important to consider the relatively small size of mobile displays and keep your UI as simple as possible.

The Systrace report shown in Figure 3 is an example of a UI frame that's attempting to render too many elements relative to a mobile device's capabilities.

A good goal is to**reduce the UI update time to 2-3 milliseconds**. You can achieve such quick updates by performing optimizations similar to the following:

- Update only the elements on screen that have moved.
- Limit the number of UI textures and layers. Consider combining graphics calls, such as shaders and textures, that use the same material.
- Defer element animation operations to the GPU.
- Perform more aggressive frustum and occlusion culling.
- If possible, perform draw operations using the Vulkan API. The draw call overhead is lower on Vulkan.

### Power consumption

Even after making the optimizations discussed in the previous section, you might find that your game's framerate deteriorates within the first 45-50 minutes of gameplay. Furthermore, the device might begin to heat up and consume more battery over time.

In many cases, this undesirable set of thermals and power consumption is related to how your game's workload is distributed across a device's CPUs. To increase your game's power consumption efficiency, apply the best practices shown in the following sections.

#### Keep memory-heavy threads on one CPU

On many mobile devices, the L1 caches reside on specific CPUs, and L2 caches reside on the set of CPUs that share a clock. To maximize L1 cache hits, it's generally best to keep your game's main thread, along with any other memory-heavy threads, running on a single CPU.

#### Defer short-duration work to lower-powered CPUs

Most game engines, including Unity, know to defer worker thread operations onto a different CPU relative to your game's main thread. However, the engine isn't aware of a device's specific architecture and cannot anticipate your game's workload as well as you can.

Most system-on-a-chip devices have at least 2 shared clocks, one for the device's*fast CPUs* and one for the device's*slow CPUs*. A consequence of this architecture is that, if one fast CPU needs to operate at maximum speed, all the other fast CPUs also operate at maximum speed.

The example report shown in Figure 4 shows a game that takes advantage of fast CPUs. However, this high activity level generates a great deal of power and heat quickly.

![Diagram of threads within a system trace](https://developer.android.com/static/images/games/systrace-cpu-assignment.svg)
**Figure 4.**Systrace report showing a suboptimal assignment of threads to the device's CPUs

<br />

| **Note:** Within a Systrace report, if you select a thread in one of the CPU rows, Systrace shows the CPU state that occurred while the thread was executing. A state of`"3"`represents maximum CPU speed.

To reduce overall power usage, it's best to suggest to the scheduler that shorter-duration work---such as loading audio, running worker threads, and executing the choreographer---be deferred to the set of slow CPUs on a device. Transfer as much of this work onto the slow CPUs as you can while maintaining a desired framerate.

Most devices list the slow CPUs before the fast CPUs, but you cannot assume that your device's SOC uses this order. To check, run commands similar to the ones shown in this[CPU topology discovery code](https://github.com/fcarucci/peuck/blob/master/src/Peuck.cpp)on GitHub.

After you know which CPUs are the slow CPUs on your device, you can declare affinities for your short-duration threads, which the device's scheduler follows. To do so, add the following code within each thread:  

```c++
#include <sched.h>
#include <sys/types.h>
#include <unistd.h>

pid_t my_pid; // PID of the process containing your thread.

// Assumes that cpu0, cpu1, cpu2, and cpu3 are the "slow CPUs".
cpu_set_t my_cpu_set;
CPU_ZERO(&my_cpu_set);
CPU_SET(0, &my_cpu_set);
CPU_SET(1, &my_cpu_set);
CPU_SET(2, &my_cpu_set);
CPU_SET(3, &my_cpu_set);
sched_setaffinity(my_pid, sizeof(cpu_set_t), &my_cpu_set);
```
| **Note:** In advanced cases where you have a highly-parallelized workload, you might want to manage these threads in such a way so that the slow CPUs stay active as frequently as possible. This high level of granularity for CPU scheduling further helps maintain your game's framerate.

### Thermal stress

When devices get too warm, they may throttle the CPU and/or GPU, and this can affect games in unexpected ways. Games that incorporate complex graphics, heavy computation, or sustained network activity are more likely to encounter issues.

Use the thermal API to monitor temperature changes on the device and take action to maintain lower power usage and cooler device temperature. When the device reports thermal stress, back off ongoing activities to reduce power usage. For example, reduce the frame rate or polygon tessellation.

First, declare the[`PowerManager`](https://developer.android.com/reference/android/os/PowerManager)object and initialize it in the`onCreate()`method. Add a thermal status listener to the object.  

### Kotlin

```kotlin
class MainActivity : AppCompatActivity() {
    lateinit var powerManager: PowerManager

    override fun onCreate(savedInstanceState: Bundle?) {
        powerManager = getSystemService(Context.POWER_SERVICE) as PowerManager
        powerManager.addThermalStatusListener(thermalListener)
    }
}
```

### Java

```java
public class MainActivity extends AppCompatActivity {
    PowerManager powerManager;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        ...
        powerManager = (PowerManager) getSystemService(Context.POWER_SERVICE);
        powerManager.addThermalStatusListener(thermalListener);
    }
}
```

Define the actions to take when the listener detects a status change. If your game uses C/C++, add code to the thermal status levels in`onThermalStatusChanged()`to[call into your native game code using JNI](https://developer.android.com/ndk/guides/concepts)or use the native[Thermal API](https://developer.android.com/ndk/reference/group/thermal).  

### Kotlin

```kotlin
val thermalListener = object : PowerManager.OnThermalStatusChangedListener() {
    override fun onThermalStatusChanged(status: Int) {
        when (status) {
            PowerManager.THERMAL_STATUS_NONE -> {
                // No thermal status, so no action necessary
            }

            PowerManager.THERMAL_STATUS_LIGHT -> {
                // Add code to handle light thermal increase
            }

            PowerManager.THERMAL_STATUS_MODERATE -> {
                // Add code to handle moderate thermal increase
            }

            PowerManager.THERMAL_STATUS_SEVERE -> {
                // Add code to handle severe thermal increase
            }

            PowerManager.THERMAL_STATUS_CRITICAL -> {
                // Add code to handle critical thermal increase
            }

            PowerManager.THERMAL_STATUS_EMERGENCY -> {
                // Add code to handle emergency thermal increase
            }

            PowerManager.THERMAL_STATUS_SHUTDOWN -> {
                // Add code to handle immediate shutdown
            }
        }
    }
}
```

### Java

```java
PowerManager.OnThermalStatusChangedListener thermalListener =
    new PowerManager.OnThermalStatusChangedListener () {

    @Override
    public void onThermalStatusChanged(int status) {

        switch (status)
        {
            case PowerManager.THERMAL_STATUS_NONE:
                // No thermal status, so no action necessary
                break;

            case PowerManager.THERMAL_STATUS_LIGHT:
                // Add code to handle light thermal increase
                break;

            case PowerManager.THERMAL_STATUS_MODERATE:
                // Add code to handle moderate thermal increase
                break;

            case PowerManager.THERMAL_STATUS_SEVERE:
                // Add code to handle severe thermal increase
                break;

            case PowerManager.THERMAL_STATUS_CRITICAL:
                // Add code to handle critical thermal increase
                break;

            case PowerManager.THERMAL_STATUS_EMERGENCY:
                // Add code to handle emergency thermal increase
                break;

            case PowerManager.THERMAL_STATUS_SHUTDOWN:
                // Add code to handle immediate shutdown
                break;
        }
    }
};
```

### Touch-to-display latency

Games that render frames as quickly as possible create a GPU-bound scenario, where the frame buffer becomes overstuffed. The CPU needs to wait for the GPU, which causes a noticeable delay between a player's input and the input taking effect on screen.

To determine whether you could improve your game's frame pacing, complete the following steps:

1. Generate a Systrace report that includes the`gfx`and`input`categories. These categories comprise particularly useful measurements for determining touch-to-display latency.
2. Check the`SurfaceView`section of a Systrace report. An overstuffed buffer causes the number of pending buffer draws to oscillate between 1 and 2, as shown in Figure 5:

   ![Diagram of buffer queue within a system trace](https://developer.android.com/static/images/games/systrace-overstuffed-buffer.svg)
   **Figure 5.**Systrace report showing an overstuffed buffer that is periodically too full to accept drawing commands

   <br />

To mitigate this inconsistency in frame pacing, complete the actions described in the following sections:

#### Integrate the Android Frame Pacing API into your game

The[Android Frame Pacing API](https://developer.android.com/topic/performance/frame-pacing)helps you perform frame swaps and define a swap interval such that your game maintains a more consistent framerate.

#### Reduce the resolution of your game's non-UI assets

The displays on modern mobile devices contain many more pixels than a player can process, so it's OK to downsample such that a run of 5 or even 10 pixels all contains one color. Given the structure of most display caches, it's best to**reduce the resolution along one dimension only**.

However, don't reduce the resolution of your game's UI elements. It's important to preserve the line thickness on these elements to maintain a[large enough touch target size](https://developer.android.com/guide/topics/ui/accessibility/apps#touch-targets)for all of your players.
| **Note:** Because the GPU requires some time to resize your assets, it's best to perform any resolution-reduction operations in your game's post-processing step, if you have one.

### Rendering smoothness

When SurfaceFlinger latches onto a display buffer to show a scene in your game, the CPU activity momentarily increases. If these spikes in CPU activity occur unevenly, it's possible to see stuttering in your game. The diagram in Figure 6 depicts the reason why this occurs:

![Diagram of frames missing a Vsync window because they started drawing too late](https://developer.android.com/static/images/games/systrace-missed-vsync.svg)
**Figure 6.**Systrace report showing how a frame can miss a Vsync

<br />

If a frame starts drawing too late, even by a few milliseconds, it might miss the next display window. The frame must then wait until the next Vsync to be displayed (33 milliseconds when running a game at 30 FPS), which causes a noticeable delay from the player's perspective.

To address this situation, use the[Android Frame Pacing API](https://developer.android.com/topic/performance/frame-pacing), which always presents a new frame on a VSync wavefront.

### Memory state

When running your game for an extended period of time, it's possible for the device to experience out-of-memory errors.

In this situation, check the CPU activity in a Systrace report and see how often the system is making calls to the`kswapd`daemon. If there are many calls during your game's execution, it's best to take a closer look at how your game is managing and cleaning up memory.

For more information, see[Manage memory effectively in games](https://developer.android.com/games/optimize/memory-allocation).

### Thread state

When navigating through the typical elements of a Systrace report, you can view the amount of time that a given thread spent in[each possible thread state](https://developer.android.com/topic/performance/tracing/navigate-report#display-frames)by selecting the thread within the report, as shown in Figure 7:

![Diagram of a Systrace report](https://developer.android.com/static/images/games/systrace-thread-state.svg)
**Figure 7.**Systrace report showing how selecting a thread causes the report to display a state summary for that thread

<br />

As Figure 7 shows, you might find that your game's threads aren't in the "running" or "runnable" state as often as they should be. The following list shows several common reasons why a given thread might be periodically transitioning to an unusual state:

- If a thread is sleeping for an extended period of time, it might be suffering from either lock contention or waiting for GPU activity.
- If a thread is constantly blocked on I/O, you're either reading too much data from disk at a time, or your game is thrashing.

| **Note:** Higher-end devices tend to be CPU-bound much more often than I/O-bound, but if your game runs on an entry-level device, it might be worth making several minor optimizations to I/O throughput.

## Additional resources

To learn more about improving your game's performance, see the following additional resources:

### Videos

- [Systrace for Games](https://www.youtube.com/watch?v=4oAlB-3tkqc)presentation from Android Game Developer Summit 2018