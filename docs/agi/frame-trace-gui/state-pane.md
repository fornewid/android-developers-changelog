---
title: https://developer.android.com/agi/frame-trace-gui/state-pane
url: https://developer.android.com/agi/frame-trace-gui/state-pane
source: md.txt
---

To check the render state after a specific submitted command, click the command
in the [**Commands** pane](https://developer.android.com/agi/refdocs/commands-pane). The **State** pane lets
you examine the render state using the following items.

![alt text](https://gapid.dev/images/state-pane/vulkan.png "Vulkan State")

## Last bound queue (currently bound queue)

The **LastBoundQueue** node contains the information of the queue used for the
`vkQueueSubmit`, which submits the command in question. The `VulkanHandle` will
be used to find the drawing information of the current render state in
`LastDrawInfos`.

![alt text](https://gapid.dev/images/state-pane-vulkan-last-bound-queue.png "Vulkan Last Bound Queue")

1. The `VulkanHandle` shows the value of the last used `VkQueue`, which is
   actually the currently bound queue for the submitted command in question.

2. The information of the current render state is stored in `LastDrawInfos`,
   and indexed by the `VkQueue` value.

## Last draw infos (current render state info)

The **LastDrawInfos** node contains the information of the last drawing for each
`VkQueue`, and includes the following information:

- Framebuffer information
- Render pass information
- Bound descriptor sets
- Bound vertex and index buffers
- Graphics pipeline
- Drawing parameters

**Bound Framebuffer**

![alt text](https://gapid.dev/images/state-pane-vulkan-draw-info-framebuffer.png "Vulkan Last Draw Info Framebuffer")

- **Framebuffer** node: shows the info of the currently bound framebuffer.
  This node gets updated after each `vkCmdBeginRenderPass` executes on the
  same queue.

- **Renderpass** node: shows the info of the render pass used to create the
  framebuffer. Note that this is not the render pass currently bound for
  drawing.

- **ImageAttachments** node: lists all the image attachments (`VkImageViews`)
  bound to the framebuffer. Each item of the list shows the info of the image
  view.

- **Image** node shows the info of the image bound to the image view.

**Bound renderpass**

![alt text](https://gapid.dev/images/state-pane-vulkan-draw-info-renderpass.png "Vulkan Last Draw Info Renderpass")

- **Renderpass** node: shows the info of the renderpass currently used for rendering. It gets updated after each `VkCmdBeginRenderPass` executes on the same queue.

- **AttachmentDescriptions** node: lists all the `VkAttachmentDescription` of the current renderpass in use.

- **SubpassDescriptions** node: lists the `VkSubpassDescription` for each subpass.

- **SubpassDependencies** node: lists the `VkSubpassDependency` for each subpass.

**Bound descriptor sets**

![alt text](https://gapid.dev/images/state-pane-vulkan-draw-info-descriptorsets.png "Vulkan Last Draw Info Descriptor Sets")

- **DescriptorSets** node: lists all the currently bound descriptor sets. The list of bounded descriptor sets reflect the state after the last `vkCmdBindDescriptorSets` being rolled out on the same queue, and the original descriptor set info will be overwritten or new info will be added according to the parameters of the last executed `vkCmdBindDescriptorSets`.

- **Bindings**: node lists all the currently bound descriptor bindings in the
  descriptor set.

  Each descriptor binding also lists its bound descriptors.
- **Layout** node: shows the info of the `VkDescriptorSetLayout` used to allocate the descriptor set.

**Bound graphics pipeline**

![alt text](https://gapid.dev/images/state-pane-vulkan-draw-info-gfx-pipeline.png "Vulkan Last Draw Info Graphics Pipeline")

`GraphicsPipeline` node: contains the info about the last bound graphics pipeline. This node gets updated after each `VkCmdBindPipeline` executes on the current queue.

**Bound Buffers**

![alt text](https://gapid.dev/images/state-pane-vulkan-draw-info-bound-buffers.png "Vulkan Last Draw Info Buffers")

- **BoundVertexBuffers** node lists all the bound vertex buffers. For each bound vertex buffer, it shows the info of the backing buffer. The list gets updated accordingly after each `vkCmdBindVertexBuffers` executes on the same queue.

- `BoundIndexBuffer` node shows the last bound index buffer, including the index type and the info of the backing buffer.

**Draw Command Parameters**

![alt text](https://gapid.dev/images/state-pane-vulkan-draw-info-draw-params.png "Vulkan Last Draw Info Draw Command Parameters")

**CommandParameters** node: contains the parameters to `vkCmdDraw`, `vkCmdDrawIndexed`, `vkCmdDrawIndirect` and `vkCmdDrawIndirectIndexed`. For each type of drawing command, there is a corresponding sub-node to contains the parameter values. As these four types of drawining commands cannot be used at the same time, only one of the four sub-nodes can be populated at a time. The content of **CommandParameters** gets updated after any one of the four drawining commands being executed on the same queue.