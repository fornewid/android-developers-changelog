---
title: https://developer.android.com/training/wide-color-gamut
url: https://developer.android.com/training/wide-color-gamut
source: md.txt
---

# Enhance graphics with wide color content

Android 8.0 (API level 26) introduced color management support for additional[color spaces](https://en.wikipedia.org/wiki/Color_space)besides standard RGB (sRGB) for rendering graphics on devices with compatible displays. With this support, your app can render bitmaps with embedded wide color profiles loaded from PNG, JPEG, and WebP files via Java or native code. Apps using OpenGL or Vulkan can directly output wide color gamut content (using[Display P3](https://en.wikipedia.org/wiki/DCI-P3)and[scRGB](https://en.wikipedia.org/wiki/ScRGB)). This capability is useful for creating apps that involve high fidelity color reproduction, such as image and video editing apps.  

## Understand the wide color gamut mode

Wide color profiles are[ICC profiles](https://en.wikipedia.org/wiki/ICC_profile), such as[Adobe RGB](https://en.wikipedia.org/wiki/Adobe_RGB_color_space),[Pro Photo RGB](https://en.wikipedia.org/wiki/ProPhoto_RGB_color_space), and[DCI-P3](https://en.wikipedia.org/wiki/DCI-P3), that are capable of representing a wider range of colors than sRGB. Screens supporting wide color profiles can display images with deeper primary colors (reds, greens, and blues) as well as richer secondary colors (such as magentas, cyans, and yellows).

On Android devices running Android 8.0 (API level 26) or higher that support it, your app can enable the*wide color gamut color mode* for an activity whereby the system recognizes and correctly process bitmap images with embedded wide color profiles. The[ColorSpace.Named](https://developer.android.com/reference/android/graphics/ColorSpace.Named)class enumerates a partial list of commonly used color spaces that Android supports.

**Note:**When wide color gamut mode is enabled, the activity's window uses more memory and GPU processing for screen composition. Before enabling wide color gamut mode, you should carefully consider if the activity truly benefits from it. For example, an activity that displays photos in fullscreen is a good candidate for wide color gamut mode, but an activity that shows small thumbnails is not.

## Enable wide color gamut mode

Use the[colorMode](https://developer.android.com/reference/android/R.attr#colorMode)attribute to request the activity to be displayed in wide color gamut mode on compatible devices. In wide color gamut mode, a window can render outside of the sRGB gamut to display more vibrant colors. If the device does not support wide color gamut rendering, this attribute has no effect. If your app needs to determine whether a given display is wide color gamut capable, call the[isWideColorGamut()](https://developer.android.com/reference/android/view/Display#isWideColorGamut())method. You app can also call[isScreenWideColorGamut()](https://developer.android.com/reference/android/content/res/Configuration#isScreenWideColorGamut()), which returns`true`only if the display is wide color gamut capable and the device supports wide color gamut color rendering.

A display might be wide color gamut capable but not color-managed, in which case, the system will not grant an app the wide color gamut mode. When a display is not color-managed ---as was the case for all versions of Android prior to 8.0---the system remaps the colors drawn by the app to the display's gamut.

To enable the wide color gamut in your activity, set the[colorMode](https://developer.android.com/reference/android/R.attr#colorMode)attribute to`wideColorGamut`in your`AndroidManifest.xml`file. You need to do this for each activity for which you want to enable wide color mode.  

```xml
android:colorMode="wideColorGamut"
```

You can also set the color mode programmatically in your activity by calling the[setColorMode(int)](https://developer.android.com/reference/android/view/Window#setColorMode(int))method and passing in[COLOR_MODE_WIDE_COLOR_GAMUT](https://developer.android.com/reference/android/content/pm/ActivityInfo#COLOR_MODE_WIDE_COLOR_GAMUT).

## Render wide color gamut content

![](https://developer.android.com/static/images/colorspace_display_p3.png)**Figure 1.**Display P3 (orange) vs. sRGB (white) color spaces

To render wide color gamut content, your app must load a wide color bitmap, that is a bitmap with a color profile containing a color space wider than sRGB. Common wide color profiles include Adobe RGB, DCI-P3 and Display P3.

Your app can query the color space of a bitmap, by calling[getColorSpace()](https://developer.android.com/reference/android/graphics/Bitmap#getColorSpace()). To determine if the system recognizes a specific color space to be wide gamut, you can call the[isWideGamut()](https://developer.android.com/reference/android/graphics/ColorSpace#isWideGamut())method.

The[Color](https://developer.android.com/reference/android/graphics/Color)class allows you to represent a color with four components packed into a 64-bit long value, instead of the most common representation that uses an integer value. Using long values, you can define colors with more precision than integer values. If you need to create or encode a color as a long value, use one of the`pack()`methods in the[Color](https://developer.android.com/reference/android/graphics/Color)class.

You can verify whether your app properly requested the wide color gamut mode, by checking that the[getColorMode()](https://developer.android.com/reference/android/view/Window#getColorMode())method returns[COLOR_MODE_WIDE_COLOR_GAMUT](https://developer.android.com/reference/android/content/pm/ActivityInfo#COLOR_MODE_WIDE_COLOR_GAMUT)(this method does not indicate, however, whether the wide color gamut mode was actually granted).

## Use wide color gamut support in native code

This section describes how to enable wide color gamut mode with the[OpenGL](https://developer.android.com/develop/ui/views/graphics/opengl/about-opengl)and[Vulkan](https://developer.android.com/ndk/guides/graphics)APIs if your app uses native code.

### OpenGL

In order to use wide color gamut mode in OpenGL, your app must include the EGL 1.4 library with one of the following extensions:

- [EGL_EXT_gl_colorspace_display_p3](https://www.khronos.org/registry/EGL/extensions/EXT/EGL_EXT_gl_colorspace_display_p3.txt)
- [EGL_EXT_gl_colorspace_scrgb](https://www.khronos.org/registry/EGL/extensions/EXT/EGL_EXT_gl_colorspace_scrgb.txt)
- [EGL_EXT_gl_colorspace_scrgb_linear](https://www.khronos.org/registry/EGL/extensions/EXT/EGL_EXT_gl_colorspace_scrgb_linear.txt)

To enable the feature, you must first create a GL context via[eglChooseConfig](https://www.khronos.org/registry/EGL/sdk/docs/man/html/eglChooseConfig.xhtml), with one of the three supported color buffer formats for wide color in the attributes. The color buffer format for wide color must be one of these sets of RGBA values:

- 8, 8, 8, 8
- 10, 10, 10, 2
- FP16, FP16, FP16, FP16

Then, request the P3 color space extension when creating your render targets, as shown in the following code snippet:  

```c++
std::vector<EGLint> attributes;
attributes.push_back(EGL_GL_COLORSPACE_KHR);
attributes.push_back(EGL_GL_COLORSPACE_DISPLAY_P3_EXT);
attributes.push_back(EGL_NONE);
engine->surface_ = eglCreateWindowSurface(
    engine->display_, config, engine->app->window, attributes.data());
```

### Vulkan

The Vulkan support for wide color gamut is provided through the[VK_EXT_swapchain_colorspace](https://www.khronos.org/registry/vulkan/specs/1.0-extensions/html/vkspec.html#VK_EXT_swapchain_colorspace)extension.

Before enabling wide color support in your Vulkan code, first check that the extension is supported via[vkEnumerateInstanceExtensionProperties](https://www.khronos.org/registry/vulkan/specs/1.0/man/html/VkExtensionProperties.html). If the extension is available, you must enable it during[vkCreateInstance](https://www.khronos.org/registry/vulkan/specs/1.0/man/html/vkCreateInstance.html)before creating any swapchain images that use the additional color spaces defined by the extension.

Before creating the swapchain, you need choose your desired color space, then loop through the available physical device surfaces and choose a valid color format for that color space.

On Android devices, Vulkan supports wide color gamut with the following color spaces and`VkSurfaceFormatKHR`color formats:

- **Vulkan wide color gamut color spaces** :
  - `VK_COLOR_SPACE_EXTENDED_SRGB_LINEAR_EXT`
  - `VK_COLOR_SPACE_DISPLAY_P3_NONLINEAR_EXT`
- **Vulkan color formats with wide color gamut support** :
  - `VK_FORMAT_R16G16B16A16_SFLOAT`
  - `VK_FORMAT_A2R10G10B10_UNORM_PACK32`
  - `VK_FORMAT_R8G8B8A8_UNORM`

The following code snippet shows how you can check that the device supports the Display P3 color space:  

```c++
uint32_t formatCount = 0;
vkGetPhysicalDeviceSurfaceFormatsKHR(
       vkPhysicalDev,
       vkSurface,
       &formatCount,
       nullptr);
VkSurfaceFormatKHR *formats = new VkSurfaceFormatKHR[formatCount];
vkGetPhysicalDeviceSurfaceFormatsKHR(
       vkPhysicalDev,
       vkSurface,
       &formatCount,
       formats);

uint32_t displayP3Index = formatCount;
for (uint32_t idx = 0; idx < formatCount; idx++) {
 if (formats[idx].format == requiredSwapChainFmt &&
     formats[idx].colorSpace==VK_COLOR_SPACE_DISPLAY_P3_NONLINEAR_EXT)
 {
   displayP3Index = idx;
   break;
 }
}
if (displayP3Index == formatCount) {
    // Display P3 is not supported on the platform
    // choose other format
}
```

The following code snippet shows how to request a Vulkan swapchain with`VK_COLOR_SPACE_DISPLAY_P3_NONLINEAR_EXT`:  

```c++
uint32_t queueFamily = 0;
VkSwapchainCreateInfoKHR swapchainCreate {
   .sType = VK_STRUCTURE_TYPE_SWAPCHAIN_CREATE_INFO_KHR,
   .pNext = nullptr,
   .surface = AndroidVkSurface_,
   .minImageCount = surfaceCapabilities.minImageCount,
   .imageFormat = requiredSwapChainFmt,
   .imageColorSpace = VK_COLOR_SPACE_DISPLAY_P3_NONLINEAR_EXT,
   .imageExtent = surfaceCapabilities.currentExtent,
   .imageUsage = VK_IMAGE_USAGE_COLOR_ATTACHMENT_BIT,
   .preTransform = VK_SURFACE_TRANSFORM_IDENTITY_BIT_KHR,
   .imageArrayLayers = 1,
   .imageSharingMode = VK_SHARING_MODE_EXCLUSIVE,
   .queueFamilyIndexCount = 1,
   .pQueueFamilyIndices = &queueFamily,
   .presentMode = VK_PRESENT_MODE_FIFO_KHR,
   .oldSwapchain = VK_NULL_HANDLE,
   .clipped = VK_FALSE,
};
VkRresult status = vkCreateSwapchainKHR(
                       vkDevice,
                       &swapchainCreate,
                       nullptr,
                       &vkSwapchain);
if (status != VK_SUCCESS) {
    // Display P3 is not supported
    return false;
}
```