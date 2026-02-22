---
title: https://developer.android.com/agi/sys-trace/system-profiler-gui
url: https://developer.android.com/agi/sys-trace/system-profiler-gui
source: md.txt
---

# View a system profile

In Android GPU Inspector (AGI), you can view and analyze a[system profile](https://developer.android.com/agi/sys-trace/system-profiler)in the System Profiler UI. After you profile a system and[open the trace file](https://developer.android.com/agi/start#system-profile)in AGI, System Profiler displays the[profiling data](https://developer.android.com/agi/sys-trace/system-profiler-gui#profiling_data)in a timeline with expandable items that display additional details.
| **Note:** For information about performing frame profiling, see the[Frame profiling](https://developer.android.com/agi/frame-trace/frame-profiler)overview.

The main elements of the System Profiler UI includes the following:

- Toolbar

  - [Navigation mode buttons](https://developer.android.com/agi/sys-trace/system-profiler-gui#navigation_mode)

  - Track filter textbox: filters the tracks that are displayed in the[track](https://developer.android.com/agi/sys-trace/system-profiler-gui#profiling_data)pane.

  - Info button (**i**): displays trace and device metadata.

  - Help button (**?** ): displays[keyboard and mouse shortcuts](https://developer.android.com/agi/sys-trace/system-profiler-gui#navigation_shortcuts).

- [Timeline](https://developer.android.com/agi/sys-trace/system-profiler-gui#select_a_time_range): indicates the timespan of trace events.

- [Track](https://developer.android.com/agi/sys-trace/system-profiler-gui#profiling_data)pane: displays profiling data in relation to the timeline.

- [Details](https://developer.android.com/agi/sys-trace/system-profiler-gui#view_details)pane: an expandable pane that displays details about a selected item.

## Profiling data

In a trace file, the profiling data is stored in timestamped events called trace events. Trace events consist of various types of slices and counters. For example, CPU trace events include scheduling slices, while GPU trace events include GPU performance counters and thread slices.

In the System Profiler UI, the track pane contains trace events that are displayed in rows called tracks, which are based on the timeline. Tracks of the same type are displayed in track groups.

### GPU tracks

The GPU tracks display GPU profiling information. These are the main GPU track types:

1. **GPU Queue Tracks**: GPU activity of the application.

2. **GPU Counter Tracks**: GPU's hardware counters sampled at periodic intervals.

3. **Vulkan Events Track**: Vulkan API related events.

4. **SurfaceFlinger Tracks**: SurfaceFlinger events, which indicate how graphics buffers move through the system.

#### GPU queue tracks

A GPU can have one or more**GPU Queue** tracks based on the number of hardware queues that ran during the trace.**GPU Queue**tracks contain activity slices that represent the period and type of GPU work that was used by your app.

An activity slice contains metadata that you can view, such as the Vulkan command buffer, render pass, and frame buffer that initiated the work. The Vulkan handles to these objects are displayed in the[details](https://developer.android.com/agi/sys-trace/system-profiler-gui#view_details)pane as follows:

- `VkCommandBuffer`
- `VkRenderPass`
- `VkFrameBuffer`

You can give user-friendly names to these objects, so you can easily identify them in a trace alongside their handles, by using the[`vkSetDebugUtilsObjectNameEXT`](https://www.khronos.org/registry/vulkan/specs/1.2-extensions/man/html/vkSetDebugUtilsObjectNameEXT.html)function from the`VK_EXT_debug_utils`extension, or the[`vkDebugMarkerSetObjectNameEXT`](https://www.khronos.org/registry/vulkan/specs/1.2-extensions/man/html/vkDebugMarkerSetObjectNameEXT.html)function from the`VK_EXT_debug_marker`extension. Both extensions are implemented by AGI and available to your application while tracing.

#### GPU counter tracks

GPU counter tracks graph the value of GPU performance counters sampled at a periodic interval. The graphs display variations in the performance of your GPUs underlying hardware components between samples. You can use this info to identify bottlenecks in your GPU usage.

The available counters are hardware specific. You can view brief descriptions of each counter by hovering over the track name. For details, see[GPU performance counters](https://developer.android.com/agi/sys-trace/counters-arm).

#### Vulkan event track

The Vulkan event track shows Vulkan API events recorded during the trace. The track event types are mainly queue submit events (`vkQueueSubmit`calls). If you click a queue submit event, AGI highlights the GPU activity slices that are associated with the call. You can use this data to inspect the asynchronous work queued by Vulkan API calls and the latency between the CPU and GPU.

#### SurfaceFlinger tracks

[SurfaceFlinger](https://source.android.com/devices/graphics/surfaceflinger-windowmanager)tracks display the lifecycle of graphics buffers (an app's swapchain render targets) as they pogress through the system until they are displayed. The events are aggregated by buffer to make it easier to track the overhead and latency needed for acquiring and posting buffers.

## Interact with profiling data

This section describes how to interact with[profiling data](https://developer.android.com/agi/sys-trace/system-profiler-gui#profiling_data)in the System Profiler UI.

### Pin

You can pin tracks and track groups by using their pin button.

### Collapse and expand

Some tracks and all track groups are are collapsable. Some track groups display a summary when collapsed. For example, when collapsed, the CPU track group shows the overall CPU usage in a graph.

### Zoom

AGI aggregates profiling data based on zoom level. When you first[open a trace file](https://developer.android.com/agi/start#system-profile), the System Profiler UI displays the entire profile at the maximum zoomed-out level. You can inspect the profile by finding areas of interest and then viewing the details.

As you zoom in and out on different track types, they display different types of profiling data. For example, CPU tracks initially display time slices of each thread, and then eventually switch to displaying CPU core utilization data when zooming in.

### View details

You can display detailed metadata in the details pane by selecting items in the track pane. If an item is selectable, hovering over it will change the cursor to a pointer and then you can choose the item.

### Select a time range

You can select a time range, which allows you to compare trace events from different tracks. To do so, enable**Timing**mode and then drag to select a range. Everything outside of the is dimmed and duration of the range is displayed.

You can also select the time range of a selected slice by pressing`M`. You can then scroll through additional tracks to identify events from the same time period.

### Navigation shortcuts

You can navigate items in the track pane with the`WASD`keys or by scrolling and panning. System Profiler uses the same keyboard and mouse shortcuts as[Systrace](https://source.android.com/devices/tech/debug/systrace). The available shortcuts include the following:

- `W`and`S`, or`Ctrl++`and`Ctrl+-`to zoom.
- `A`and`D`, or`left`and`right`arrows pan the view left and right.
- `Q`and`E`, or`up`and`down`arrows scroll the tracks.
- Hold`shift`increases the movement speed of navigation.
- `Ctrl`+scroll zooms on the selected item.
- `F`zooms on a selected item.
- `Z`+`0`resets and completely zooms out.
- `V`toggles highlighting VSync if it is available in the trace.
- `M`marks the current selection by selecting its time range.
- `H`or`?`shows the keyboard and mouse shortcut cheatsheet.

#### Navigation mode

The toolbar contains buttons that switch between navigation modes, which select the action that is performed when you drag items in the track pane. You can also select the following navigation modes by pressing the`1`,`2`,`3`, and`4`keys:

1. **Selection**: Drag to box-select items.
2. **Pan**: Drag to pan and scroll the tracks. This is the default mode.
3. **Zoom**: Drag vertically to zoom on items.
4. **Timing**: Drag to select a time range.

You can also use navigation modes with these modifier keys:

- `Shift+`drag to box select items.
- `Space+`drag to pan and scroll.
- `Ctrl+`scroll to zoom.
- `Ctrl+`drag to select a time range.