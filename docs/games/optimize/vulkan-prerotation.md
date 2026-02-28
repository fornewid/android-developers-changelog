---
title: https://developer.android.com/games/optimize/vulkan-prerotation
url: https://developer.android.com/games/optimize/vulkan-prerotation
source: md.txt
---

This article describes how to efficiently handle device rotation
in your Vulkan application by implementing pre-rotation.

With [Vulkan](https://developer.android.com/ndk/guides/graphics), you can
specify much more information about rendering state than you can with OpenGL.
With Vulkan, you must explicitly implement things that are handled by the driver in
OpenGL, such as **device orientation** and its relationship to
**render surface orientation**. There are three ways that Android can
handle reconciling the render surface of the device with the device orientation:

1. The Android OS can use the device's Display Processing Unit (DPU), which can efficiently handle surface rotation in hardware. Available on supported devices only.
2. The Android OS can handle surface rotation by adding a compositor pass. This will have a performance cost depending on how the compositor has to deal with rotating the output image.
3. The application itself can handle the surface rotation by rendering a rotated image onto a render surface that matches the current orientation of the display.

## Which of these methods should you use?

Currently, there's no way for an application to know whether surface rotation
handled outside of the application will be free. Even if there is a DPU to take
care of this for you, there will still likely be a measurable performance penalty
to pay. If your application is CPU-bound, this becomes a power issue due to
the increased GPU usage by the Android Compositor, which is usually running at a
boosted frequency. If your application is GPU bound, then the Android Compositor
can also preempt your application's GPU work, causing additional performance
loss.

When running shipping titles on the Pixel 4XL, we have seen
that SurfaceFlinger (the higher-priority task that drives the Android
Compositor):

- Regularly preempts the application's work, causing 1-3ms
  hits to frametimes, and

- Puts increased pressure on the GPU's
  vertex/texture memory, because the Compositor has to read the entire
  framebuffer to do its composition work.

Handling orientation properly stops GPU preemption by SurfaceFlinger almost
entirely, while the GPU frequency drops 40% as the boosted frequency used by the
Android Compositor is no longer needed.

To ensure surface rotations are handled properly with as little overhead as
possible, as seen in the preceding case, you should implement method 3.
This is known as **pre-rotation** . This tells the Android OS that **your app**
handles the surface rotation. You can do so by passing surface transform flags
that specify the orientation during swapchain creation. This *stops* the
Android Compositor from doing the rotation *itself*.

Knowing how to set the surface transform flag is important for every Vulkan
application. Applications tend to either support multiple orientations
or support a single orientation where the render surface is in a different
orientation to what the device considers its identity orientation. For example,
a landscape-only application on a portrait-identity phone, or a portrait-only
application on a landscape-identity tablet.

## Modify AndroidManifest.xml

To handle device rotation in your app, begin by changing the application's
`AndroidManifest.xml` file to tell Android that your app will handle orientation
and screen size changes. This prevents Android from destroying and recreating
the Android [`Activity`](https://developer.android.com/reference/android/app/Activity) and calling the
[`onDestroy()`](https://developer.android.com/reference/android/app/Activity#onDestroy()) function on the
existing window surface when an orientation change occurs. This is done by
adding the `orientation` (to support API level \<13) and `screenSize` attributes
to the activity's
[`configChanges`](https://developer.android.com/guide/topics/manifest/activity-element#config) section:

    <activity android:name="android.app.NativeActivity"
              android:configChanges="orientation|screenSize">

If your application fixes its screen orientation using the [`screenOrientation`](https://developer.android.com/guide/topics/manifest/activity-element#screen)
attribute, you don't need to do this. Also, if your application uses a fixed
orientation then it will only need to set up the swapchain once on
application startup/resume.

> [!NOTE]
> **Note:** To learn more about configuration changes, how to restrict Activity recreation if needed, and how to react to those configuration changes from the View system and Jetpack Compose, check out the [Handle configuration changes](https://developer.android.com/guide/topics/resources/runtime-changes) page.

## Get the Identity Screen Resolution and Camera Parameters

Next, detect the device's screen resolution
associated with the `VK_SURFACE_TRANSFORM_IDENTITY_BIT_KHR` value. This
resolution is associated with the identity orientation of the device, and is
therefore the one that the swapchain will always need to be set to. The most
reliable way to get this is to make a call to
`vkGetPhysicalDeviceSurfaceCapabilitiesKHR()` at application startup, and
store the returned extent. Swap the width and height based on the
`currentTransform` that's also returned in order to ensure that you are storing
the identity screen resolution:

    VkSurfaceCapabilitiesKHR capabilities;
    vkGetPhysicalDeviceSurfaceCapabilitiesKHR(physDevice, surface, &capabilities);

    uint32_t width = capabilities.currentExtent.width;
    uint32_t height = capabilities.currentExtent.height;
    if (capabilities.currentTransform & VK_SURFACE_TRANSFORM_ROTATE_90_BIT_KHR ||
        capabilities.currentTransform & VK_SURFACE_TRANSFORM_ROTATE_270_BIT_KHR) {
      // Swap to get identity width and height
      capabilities.currentExtent.height = width;
      capabilities.currentExtent.width = height;
    }

    displaySizeIdentity = capabilities.currentExtent;

displaySizeIdentity is a `VkExtent2D` structure that we use to store said identity
resolution of the app's window surface in the display's natural orientation.

## Detect Device Orientation Changes (Android 10+)

The most reliable way to detect an orientation change in your application is
to verify whether the `vkQueuePresentKHR()` function returns
`VK_SUBOPTIMAL_KHR`. For example:

    auto res = vkQueuePresentKHR(queue_, &present_info);
    if (res == VK_SUBOPTIMAL_KHR){
      orientationChanged = true;
    }

**Note:** This solution only works on devices running
Android 10 and later. These versions of Android return
`VK_SUBOPTIMAL_KHR` from `vkQueuePresentKHR()`. We store the result of this
check in `orientationChanged`, a `boolean`that's accessible from the
applications' main rendering loop.

## Detect Device Orientation Changes (Pre-Android 10)

For devices running Android 10 or older, a different
implementation is needed, because `VK_SUBOPTIMAL_KHR` is not supported.

### Using Polling

On pre-Android 10 devices you can poll the current device transform every
`pollingInterval` frames, where `pollingInterval` is a granularity decided on
by the programmer. The way you do this is by calling
`vkGetPhysicalDeviceSurfaceCapabilitiesKHR()` and then comparing the returned
`currentTransform` field with that of the currently stored surface
transformation (in this code example stored in `pretransformFlag`).

    currFrameCount++;
    if (currFrameCount >= pollInterval){
      VkSurfaceCapabilitiesKHR capabilities;
      vkGetPhysicalDeviceSurfaceCapabilitiesKHR(physDevice, surface, &capabilities);

      if (pretransformFlag != capabilities.currentTransform) {
        window_resized = true;
      }
      currFrameCount = 0;
    }

On a Pixel 4 running Android 10, polling
`vkGetPhysicalDeviceSurfaceCapabilitiesKHR()` took between .120-.250ms and on a
Pixel 1XL running Android 8, polling took .110-.350ms.

### Using Callbacks

A second option for devices running below Android 10 is to register an
[`onNativeWindowResized()`](https://developer.android.com/ndk/reference/struct/a-native-activity-callbacks#struct_a_native_activity_callbacks_1a21b6cb2746c27f1874a3b6b5d6a1d6fb) callback to call a function that sets the
`orientationChanged` flag, signaling to the application an orientation change
has occurred:

    void android_main(struct android_app *app) {
      ...
      app->activity->callbacks->onNativeWindowResized = ResizeCallback;
    }

Where ResizeCallback is defined as:

    void ResizeCallback(ANativeActivity *activity, ANativeWindow *window){
      orientationChanged = true;
    }

The problem with this solution is that `onNativeWindowResized()` only gets
called for 90-degree orientation changes, such as going from landscape to portrait or
vice versa. Other orientation changes will not trigger the swapchain recreation.
For example, a change from landscape to reverse-landscape will
not trigger it, requiring the Android compositor to do the flip for your
application.

## Handling the Orientation Change

To handle the orientation change, call the orientation change routine at the
top of the main rendering loop when the `orientationChanged`
variable is set to true. For example:

    bool VulkanDrawFrame() {
     if (orientationChanged) {
       OnOrientationChange();
    }

You do all the work necessary to recreate the swapchain within
the `OnOrientationChange()` function. This means that you:

1. Destroy any existing instances of `Framebuffer` and `ImageView`,

2. Recreate the swapchain while destroying
   the old swapchain (which will be discussed next), and

3. Recreate the Framebuffers with the new swapchain's DisplayImages.
   **Note:** Attachment images (depth/stencil images, for example) usually don't
   need to be recreated as they
   are based on the identity resolution of the pre-rotated swapchain images.

    void OnOrientationChange() {
     vkDeviceWaitIdle(getDevice());

     for (int i = 0; i < getSwapchainLength(); ++i) {
       vkDestroyImageView(getDevice(), displayViews_[i], nullptr);
       vkDestroyFramebuffer(getDevice(), framebuffers_[i], nullptr);
     }

     createSwapChain(getSwapchain());
     createFrameBuffers(render_pass, depthBuffer.image_view);
     orientationChanged = false;
    }

And at the end of the function you reset the `orientationChanged` flag to false
to show that you have handled the orientation change.

### Swapchain Recreation

In the previous section we mention having to recreate the swapchain.
The first steps to doing so involves getting the new characteristics of the
rendering surface:

    void createSwapChain(VkSwapchainKHR oldSwapchain) {
       VkSurfaceCapabilitiesKHR capabilities;
       vkGetPhysicalDeviceSurfaceCapabilitiesKHR(physDevice, surface, &capabilities);
       pretransformFlag = capabilities.currentTransform;

With the `VkSurfaceCapabilities` struct populated with the new information, you
can now check to see whether an orientation change has occurred by checking the
`currentTransform` field. You'll store it for later in the `pretransformFlag`
field as you will be needing it for later when you make adjustments to the
MVP matrix.

To do so, specify the following attributes
in the `VkSwapchainCreateInfo` struct:

    VkSwapchainCreateInfoKHR swapchainCreateInfo{
      ...
      .sType = VK_STRUCTURE_TYPE_SWAPCHAIN_CREATE_INFO_KHR,
      .imageExtent = displaySizeIdentity,
      .preTransform = pretransformFlag,
      .oldSwapchain = oldSwapchain,
    };

    vkCreateSwapchainKHR(device_, &swapchainCreateInfo, nullptr, &swapchain_));

    if (oldSwapchain != VK_NULL_HANDLE) {
      vkDestroySwapchainKHR(device_, oldSwapchain, nullptr);
    }

The `imageExtent` field will be populated with the `displaySizeIdentity` extent that
you stored at application startup. The `preTransform` field will be populated
with the `pretransformFlag` variable (which is set to the currentTransform field
of the `surfaceCapabilities`). You also set the `oldSwapchain` field to the
swapchain that will be destroyed.

> [!NOTE]
> **Note:** It is **important** that the `surfaceCapabilities.currentTransform` field and the `swapchainCreateInfo.preTransform` field **match** because this lets Android know that we are handling the orientation change ourselves, thus avoiding the Android Compositor.

### MVP Matrix Adjustment

The last thing you must do is to apply the pre-transformation
by applying a rotation matrix to your MVP matrix. What this essentially does is
apply the rotation in clip space so that the resulting image is rotated to
the current device orientation. You can then simply pass this updated MVP matrix
into your vertex shader and use it as normal without the need to modify your
shaders.

    glm::mat4 pre_rotate_mat = glm::mat4(1.0f);
    glm::vec3 rotation_axis = glm::vec3(0.0f, 0.0f, 1.0f);

    if (pretransformFlag & VK_SURFACE_TRANSFORM_ROTATE_90_BIT_KHR) {
      pre_rotate_mat = glm::rotate(pre_rotate_mat, glm::radians(90.0f), rotation_axis);
    }

    else if (pretransformFlag & VK_SURFACE_TRANSFORM_ROTATE_270_BIT_KHR) {
      pre_rotate_mat = glm::rotate(pre_rotate_mat, glm::radians(270.0f), rotation_axis);
    }

    else if (pretransformFlag & VK_SURFACE_TRANSFORM_ROTATE_180_BIT_KHR) {
      pre_rotate_mat = glm::rotate(pre_rotate_mat, glm::radians(180.0f), rotation_axis);
    }

    MVP = pre_rotate_mat * MVP;

### Consideration - Non-Full Screen Viewport and Scissor

If your application is using a non-full screen viewport/scissor region, they
will need to be updated according to the orientation of the device. This
requires that you enable the dynamic Viewport and Scissor options during Vulkan's
pipeline creation:

    VkDynamicState dynamicStates[2] = {
      VK_DYNAMIC_STATE_VIEWPORT,
      VK_DYNAMIC_STATE_SCISSOR,
    };

    VkPipelineDynamicStateCreateInfo dynamicInfo = {
      .sType = VK_STRUCTURE_TYPE_PIPELINE_DYNAMIC_STATE_CREATE_INFO,
      .pNext = nullptr,
      .flags = 0,
      .dynamicStateCount = 2,
      .pDynamicStates = dynamicStates,
    };

    VkGraphicsPipelineCreateInfo pipelineCreateInfo = {
      .sType = VK_STRUCTURE_TYPE_GRAPHICS_PIPELINE_CREATE_INFO,
      ...
      .pDynamicState = &dynamicInfo,
      ...
    };

    VkCreateGraphicsPipelines(device, VK_NULL_HANDLE, 1, &pipelineCreateInfo, nullptr, &mPipeline);

The actual computation of the viewport extent during command buffer recording looks like this:

    int x = 0, y = 0, w = 500, h = 400;

    glm::vec4 viewportData;

    switch (device->GetPretransformFlag()) {
      case VK_SURFACE_TRANSFORM_ROTATE_90_BIT_KHR:
        viewportData = {bufferWidth - h - y, x, h, w};
        break;
      case VK_SURFACE_TRANSFORM_ROTATE_180_BIT_KHR:
        viewportData = {bufferWidth - w - x, bufferHeight - h - y, w, h};
        break;
      case VK_SURFACE_TRANSFORM_ROTATE_270_BIT_KHR:
        viewportData = {y, bufferHeight - w - x, h, w};
        break;
      default:
        viewportData = {x, y, w, h};
        break;
    }

    const VkViewport viewport = {
        .x = viewportData.x,
        .y = viewportData.y,
        .width = viewportData.z,
        .height = viewportData.w,
        .minDepth = 0.0F,
        .maxDepth = 1.0F,
    };

    vkCmdSetViewport(renderer->GetCurrentCommandBuffer(), 0, 1, &viewport);

The `x` and `y` variables define the coordinates of the top left corner of the
viewport, while `w` and `h` define the width and height of the viewport respectively.
The same computation can also be used to set the scissor test, and is included
here for completeness:

    int x = 0, y = 0, w = 500, h = 400;
    glm::vec4 scissorData;

    switch (device->GetPretransformFlag()) {
      case VK_SURFACE_TRANSFORM_ROTATE_90_BIT_KHR:
        scissorData = {bufferWidth - h - y, x, h, w};
        break;
      case VK_SURFACE_TRANSFORM_ROTATE_180_BIT_KHR:
        scissorData = {bufferWidth - w - x, bufferHeight - h - y, w, h};
        break;
      case VK_SURFACE_TRANSFORM_ROTATE_270_BIT_KHR:
        scissorData = {y, bufferHeight - w - x, h, w};
        break;
      default:
        scissorData = {x, y, w, h};
        break;
    }

    const VkRect2D scissor = {
        .offset =
            {
                .x = (int32_t)viewportData.x,
                .y = (int32_t)viewportData.y,
            },
        .extent =
            {
                .width = (uint32_t)viewportData.z,
                .height = (uint32_t)viewportData.w,
            },
    };

    vkCmdSetScissor(renderer->GetCurrentCommandBuffer(), 0, 1, &scissor);

### Consideration - Fragment Shader Derivatives

If your application is using derivative computations such as `dFdx` and `dFdy`,
additional transformations may be needed to account for the rotated coordinate
system as these computations are executed in pixel space. This requires the app
to pass some indication of the preTransform into the fragment shader (such as an
integer representing the current device orientation) and use that to map the
derivative computations properly:

- For a **90 degree** pre-rotated frame
  - **dFdx** must be mapped to **dFdy**
  - **dFdy** must be mapped to **-dFdx**
- For a **270 degree** pre-rotated frame
  - **dFdx** must be mapped to **-dFdy**
  - **dFdy** must be mapped to **dFdx**
- For a **180 degree** pre-rotated frame,
  - **dFdx** must be mapped to **-dFdx**
  - **dFdy** must be mapped to **-dFdy**

## Conclusion

In order for your application to get the most out of Vulkan on Android,
implementing pre-rotation is a must. The most important takeaways from this
article are:

- Ensure that during swapchain creation or recreation, the pretransform flag is set to match the flag returned by the Android operating system. This will avoid the compositor overhead.
- Keep the swapchain size fixed to the identity resolution of the app's window surface in the display's natural orientation.
- Rotate the MVP matrix in clip space to account for the devices orientation, because the swapchain resolution/extent no longer updates with the orientation of the display.
- Update viewport and scissor rectangles as needed by your application.

[**Sample App:** Minimal Android pre-rotation](https://github.com/google/vulkan-pre-rotation-demo)