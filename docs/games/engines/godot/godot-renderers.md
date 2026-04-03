---
title: https://developer.android.com/games/engines/godot/godot-renderers
url: https://developer.android.com/games/engines/godot/godot-renderers
source: md.txt
---

# Godot renderer options

Godot supports two rendering engines: GLES2 and GLES3. You should choose between GLES2 or GLES3 when you start your project, and avoid switching if possible. Projects can switch back and forth between these two rendering engines, but switching requires additional migration work.

On Android, these renderers use the OpenGL ES 2.0 and OpenGL ES 3.0 APIs respectively. The GLES3 renderer has more sophisticated capabilities and features, while the GLES2 renderer is compatible with more Android devices. The renderers also produce slightly different visual output for identical input scene data. This disparity is caused by the GLES2 renderer using a sRGB color space while the GLES3 renderer uses a linear color space.

## Choosing a renderer

### GLES2

The GLES2 renderer is most appropriate for 2D or 3D projects with modest graphic requirements, and is compatible with virtually all active Android devices. If your project is designed to run well on older devices, and you intend to support them, GLES2 may be the best choice.

An important limitation of the GLES2 renderer on Android is that only one compressed texture format is supported: ETC1. ETC1 doesn't support an alpha channel. Other engines may use dual ETC1 textures as a workaround, with one texture containing color data and a second texture containing the alpha channel data. Godot doesn't do this. Projects using the GLES2 renderer on Android must use uncompressed textures when including an alpha channel. Uncompressed textures use significantly more memory and don't perform as well as compressed textures. Older devices with limited resources in particular may have issues when using large uncompressed textures, including running into memory limits.

Advanced rendering features might not be available to the GLES2 renderer. Limitations of the GLES2 renderer include but are not limited to:

- Poor performance scaling per active real-time light.
- Lack of support for rendering features such as high-definition range, refraction properties, screen space reflections, or screen space ambient occlusion.
- Restrictions on shader complexity.
- Lack of real-time global illumination support.
- Lack of GPU acceleration support for particles.

### GLES3

The GLES3 renderer is compatible with the approximately 90% of active Android devices that have OpenGL ES 3.0 support. Only the oldest of active Android devices lack OpenGL ES 3.0 support.

While the GLES3 renderer is compatible with any OpenGL ES 3.0 device, be aware that older devices are less likely to run at acceptable frame rates. Some older devices also contain graphic driver bugs in their OpenGL ES 3.0 implementations. The GLES3 renderer on Android has limited mitigations for driver bugs. These issues are less of a concern on newer devices.

The GLES3 renderer supports the ETC2 texture compression format on Android. Unlike ETC1, ETC2 includes support for an alpha channel.

For more information, see the[Godot Documentation - Differences between GLES2 and GLES3](https://docs.godotengine.org/en/stable/tutorials/misc/gles2_gles3_differences.html)