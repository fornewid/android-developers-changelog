---
title: https://developer.android.com/agi/frame-trace-gui/commands-pane
url: https://developer.android.com/agi/frame-trace-gui/commands-pane
source: md.txt
---

The Commands pane displays the calls made by the application, grouped by frame and draw call or by user markers.
![Initial View of either an OpenGL or Vulkan trace](https://developer.android.com/static/images/agi/command-pane-images/command-pane-1.png) **Figure 1.**Initial View of either an OpenGL or Vulkan trace ![Viewing an OpenGL trace](https://developer.android.com/static/images/agi/command-pane-images/command-pane-2.png) **Figure 2.**Viewing an OpenGL trace ![Viewing a Vulkan trace](https://developer.android.com/static/images/agi/command-pane-images/command-pane-3.png) **Figure 3.**Viewing a Vulkan trace ![Viewing a Vulkan trace](https://developer.android.com/static/images/agi/command-pane-images/command-pane-4.png) **Figure 4.**Searching for a command in a Vulkan trace

## Operations

You can perform the following operations in this pane:

| Operation | Description |
|---|---|
| Show result | Click a command or group to update the other panes to reflect the state after the selected command or group. |
| Expand or collapse the command hierarchy | Click the gray triangle to the left of a grouping or double-click the grouping to expand or collapse it. |
| Search | Type a string in the search bar at the top of the pane, and then press **Return** (see the preceding image). To find the next occurrence, make sure the bar is selected and press **Return** again. Select the **Regex** box to use a regular expression search pattern. For example, `glClear.*` matches both commands `glClear()` and `glClearColor()`. You can also search for command parameter values such as buffer: `2`, which is used in `glBindBuffer().` |
| Edit | Right-click a command and select **Edit** . In the **Edit** dialog, change one or more values and click **OK**. Note: This is only valid for Vulkan commands, and not for OpenGL commands. |
| View state or memory information | Click a command argument that refers to a state parameter, such as a texture ID. The **State** pane displays additional information. Click a memory address or pointer to open the **Memory** pane. Note: This is only valid for Vulkan commands, and not for OpenGL commands. |
| Copy commands | Select items in the pane and press Control+C (or Command+C) to copy commands with their argument values. You can paste this information into a text file. |
| Magnify thumbnail | The thumbnail appears to the left of a call as shown in the following image. Hover the cursor over the thumbnail to enlarge it. |

![CAPTION](https://developer.android.com/static/images/agi/command-pane-images/command-pane-5.png)

## OpenGL ES command hierarchy

OpenGL ES commands are translated to Vulkan, and the Vulkan commands are
analyzed. As a result, OpenGL ES commands are shown with both OpenGL ES and
Vulkan commands shown in the expanded hierarchy. In the preceding example, you can
see multiple `glDrawElement` commands under the `RenderPass`. The second
`glDrawElements` command hierarchy was expanded, and shows **OpenGL ES Commands**
and **DrawIndexed**. You can expand both of these hierarchies to show the
related OpenGL ES commands, as well as the Vulkan commands that they were translated
into.

Because there isn't a one-to-one relationship between OpenGL ES and Vulkan,
there may be some differences. For example, a `glClear` command that occurs
before the first `glDraw*` command appears before a `RenderPass`. If you expand
the hierarchy of the `glClear`, there will be no Vulkan commands. That is because
the clear will be deferred and done as part of starting the Vulkan `RenderPass`.

## Debug markers

Depending on your app, the **Commands** pane can contain a very long list of
commands within one frame. For better navigation and readability, you can define
debug markers that group calls together under a heading in the tree. This could
include a grouping, for example, named "Setup" or "Render World."

If debug markers are enabled, click the **Commands** pane to reveal a
link to this information. OpenGL ES has the following APIs to group commands:

| EXTENSION / VERSION | PUSH | POP |
|---|---|---|
| [KHR_debug](https://www.khronos.org/registry/gles/extensions/KHR/KHR_debug.txt) | `glPushDebugGroupKHR()` | `glPopDebugGroupKHR()` |
| [EXT_debug_marker](https://www.khronos.org/registry/gles/extensions/EXT/EXT_debug_marker.txt) | `String` | `String` |
| [OpenGL ES 3.2](https://www.khronos.org/opengles/sdk/docs/man32/html/glPopDebugGroup.xhtml) | `String` | `String` |

Vulkan has the following APIs to group commands:

| EXTENSION / VERSION | PUSH | POP |
|---|---|---|
| [VK_EXT_debug_marker](https://github.com/KhronosGroup/Vulkan-Docs/blob/1.0/doc/specs/vulkan/chapters/VK_EXT_debug_marker.txt) | `glPushDebugGroupKHR()` | `glPopDebugGroupKHR()` |