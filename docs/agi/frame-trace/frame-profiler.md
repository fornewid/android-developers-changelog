---
title: https://developer.android.com/agi/frame-trace/frame-profiler
url: https://developer.android.com/agi/frame-trace/frame-profiler
source: md.txt
---

With Android GPU Inspector (AGI), you can profile a specific frame of your Android app
and use it to perform an in-depth analysis of the app's GPU usage. This
profiling data can give you a deeper understand of your app's GPU usage than
with [system profiling](https://developer.android.com/agi/sys-trace/system-profiler) alone.

Frame profiling with AGI starts by collecting traces and other performance data
and then measuring and displaying it for analysis.

The available frame profiling data includes the following:

- Vulkan API calls

- Framebuffer content

- Rendered mesh draw calls

- RAM and GPU memory values for commands

- GPU performance data for rendering events

- Pipeline data

- Render state data

- Texture and shader resources

## Get started

The AGI [quickstart](https://developer.android.com/agi/start) describes how to set up AGI, capture frame
profile data, and then open the resulting trace file. The next section describes
the configuration options in more detail.

## Profiling options

This sections describes the main options that are available when you
capture a frame profile.

### Graphics API options

The Graphics API options indicate the graphics API used by your app. The options
are available in the **Type** list of the **Capture System Profile** dialog.
These are the available options:

- **Vulkan**: for apps that use the Vulkan API directly.
- **OpenGL on ANGLE**: for apps that use OpenGL ES.

AGI traces Vulkan commands directly. However, if your app uses OpenGL ES, AGI
uses a custom [ANGLE](https://github.com/google/angle) build to
translate the commands into Vulkan commands before tracing the app.

### Additional arguments

The **Additional Arguments** field is for passing additional flags to the
adb `am start-activity` command, which is sent to your device to start your app
during profiling. For more information, see
[adb commands](https://developer.android.com/studio/command-line/adb).

### Start and duration options

In the **Start and Duration** section, you can specify how AGI captures the
frame to profile. The following options are available:

- **Beginning**: AGI captures all commands from application startup to the end
  of the first rendered frame.

- **Manual**: Press a button in the tracing dialog to manually capture the
  frame.

- **Time**: AGI automatically captures a frame after the given number of seconds
  elapse.

- **Frame**: AGI automatically captures the specified frame.

### Trace options

The **Trace Options** section contains settings that configure tracing flags.
These are the available settings:

- **Disable Buffering**: Disable memory buffering on the device when capturing
  data. This option is useful for debugging an app crash because it ensures
  that all tracing data is serialized up to the crash. However, it slightly
  increases the overhead of AGI during profiling.

- **Include Unsupported Extensions** : Include extensions that are not supported
  by AGI on the device. If your app uses an extension that isn't supported by
  AGI, you might encounter undesirable behavior, including subtle errors or
  crashes, when replaying the trace. Browse
  [a list of supported extensions](https://developer.android.com/agi/vulkan-extensions).

- **Clear Package Data** : Use the `pm clear`
  [adb command](https://developer.android.com/studio/command-line/adb) to request that the device clear your
  app's user data before launching.

### Output settings

The **Output** section contains settings for trace file storage, such as:

- Specify the directory to store the trace file.

- Modify the automatically generated file name for the trace file.

## View the results

When you open a trace file that contains frame profiling data, AGI displays the
data in the Frame Profiler UI for analysis.

Frame Profiler is the AGI component that manages the UI and
instrumentation for profiling an individual frame.
Frame Profiler displays data in the following UI
elements:

- [**Commands** pane](https://developer.android.com/agi/frame-trace-gui/commands-pane):
  Vulkan API calls.

- [**Framebuffer** pane](https://developer.android.com/agi/frame-trace-gui/framebuffer-pane):
  Framebuffer content.

- [**Geometry** pane](https://developer.android.com/agi/frame-trace-gui/geometry-pane):
  Rendering of mesh draw calls.

- [**Memory** pane](https://developer.android.com/agi/frame-trace-gui/memory-pane):
  RAM and GPU memory values for commands.

- [**Performance** pane](https://developer.android.com/agi/frame-trace-gui/perftab-pane):
  GPU performance data for rendering events.

- [**Pipeline** pane](https://developer.android.com/agi/frame-trace-gui/pipeline-pane):
  Pipeline content.

- [**Shader** pane](https://developer.android.com/agi/frame-trace-gui/shader-pane):
  Shader content.

- [**State** pane](https://developer.android.com/agi/frame-trace-gui/state-pane):
  The render state for submitted commands.

- [**Textures** pane](https://developer.android.com/agi/frame-trace-gui/textures-pane):
  A list of texture resources that are associated with a command.

- [**Texture** pane](https://developer.android.com/agi/frame-trace-gui/texture-pane):
  The content of a selected texture resource.

- [**Report** pane](https://developer.android.com/agi/frame-trace-gui/report-pane):
  A list of profiling errors.

## Analyze the results

These topics describe how to analyze frame profiling data with AGI:

- [Analyze render passes](https://developer.android.com/agi/frame-trace/renderpasses)
- [Analyze shader performance](https://developer.android.com/agi/frame-trace/shader-performance)
- [Analyze vertex formats](https://developer.android.com/agi/frame-trace/vertex-formats)