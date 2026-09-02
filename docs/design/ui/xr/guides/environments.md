---
title: https://developer.android.com/design/ui/xr/guides/environments
url: https://developer.android.com/design/ui/xr/guides/environments
source: md.txt
---

When a user launches your Android XR app in[Full Space](https://developer.android.com/design/ui/xr/guides/foundations#modes), you can present it in passthrough or override their environment with an immersive virtual space. Your app can trigger certain environments based on content or experiences. For example, an app could show a stormy environment when a thunderstorm is mentioned, or a history app could show a virtual Roman Colosseum when explaining gladiators.
| **Note:** While headsets offer completely immersive virtual spaces, wired XR glasses retain some visibility of the physical world through peripheral vision and display transparency.

Environments are a versatile way to customize your app and enhance immersion. In Full Space, you have full flexibility to create the experience you envision. Create unique visuals and audio to draw users in, while striving to make them feel comfortable and safe.
| **Preview:** For this developer preview release, spatial environments are only available in Full Space, and teleportation and interactivity aren't supported.
| **Note:** If a user enters Full Space and you haven't defined a spatial environment, your app inherits the system environment selected in Home Space.

## Elements of a spatial environment

Environments can incorporate depth, texture, and 3D geometry. When in Full Space, you can provide your own virtual environment in standard gITF format.[Learn how to add spatial environments](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-environments).

These optional components can help you build your scene. Choose one, or combine them all to create a complex visual experience.

<br />

![Surrounding 3D geometry](https://developer.android.com/static/images/design/ui/xr/guides/env-3d-geometry.jpg)  
**Surrounding 3D geometry**

You can create[immersive environments](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-environments#overview-spatial)by providing a`.gltf`or`.glb`file containing both the environment's geometry and a 360° image for the texture. You should also include an Image Based Lighting (IBL) file created from a high dynamic range[EXR image](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-environments#create-exr), which is necessary for realistic lighting and reflections on 3D objects.

<br />

<br />

![Additional 3D geometry](https://developer.android.com/static/images/design/ui/xr/guides/env-additional.jpeg)  
**Additional 3D geometry**

To enhance spatial awareness, strategically place supportive geometry near a user. Avoid placing objects above 0.9 meters within 1.5 meters of a user, as this can lead to depth conflicts with UI elements.

<br />

For surrounding or additional 3D geometry, Android XR supports either a`.gltf`or`.glb`file extension. You can create and export these file formats from third-party tools such as[Blender](https://www.blender.org/),[Maya](https://www.autodesk.com/products/maya),[Spline](https://spline.design/), among others.

## Create safe and comfortable experiences

Follow these guidelines to create a spatial environment that's safe and comfortable for users to explore.

- **Add clear visual cues** to let users quickly switch between Full Space and Home Space. For example, you can use[collapse content](https://fonts.google.com/icons?icon.query=collapse+content)and[expand content](https://fonts.google.com/icons?icon.query=expand+content)icons for buttons to trigger transitions.
- **Keep objects at least 1 meter away from the user to avoid collisions**. This gives the user enough room to move around while avoiding real-world physical objects.
- **You can create multiple environments**, and add a menu for users to switch between them.

## Optimize for performance

Some spatial environments demand high performance, and require optimization to maintain smooth frame rates, low latency, and avoid user discomfort.

Given the processing demands of stereoscopic rendering and real-time interactions, we recommend following efficient 3D model design and judicious use of textures and shaders. These guidelines can help you create XR experiences that are visually rich and perform well across a range of devices.

**Optimize files**

- Polycount will directly affect performance, try to optimize where possible.
- Employ efficient mesh structures and reduce unnecessary detail and overlapping geometry.
- Reduce draw calls by simplifying complex models and using texture atlases. Try combining multiple textures into a single file.
- Use efficient texture compression and reduce asset sizes to prevent GPU overload, and to optimize models and textures. Recommended asset sizes for optimal performance are approximately 80 MB for 3D wallpaper or glb, and 15 MB for audio files.
- Use[KTX2](https://github.khronos.org/KTX-Specification/ktxspec.v2.html)texture compression to optimize GPU performance.
- Bake lighting information into textures where possible.

## Consider a 360° UI safe zone

Stay in a safe tonal range with no spikes in brightness that could conflict with the UI or fatigue users.

![A spatial environment showing a safe tonal range.](https://developer.android.com/static/images/design/ui/xr/guides/env-safe-zone.jpg)

## Make it accessible

Ensure the UI is legible in all directions, especially in the middle horizontal band of a user's field of view. Avoid complexity or details that might distract.

![A person sitting in a chair in a spatial environment, with dashed lines outlining their field of view.](https://developer.android.com/static/images/design/ui/xr/guides/env-view.jpg)

## Design for comfort

If you are using mid-field large UI panels, consider the position of a user in relation to it. A user should be at least 5 feet above the surface that the screen floats above. This leaves enough distance for comfortable, centered viewing of a large virtual screen without having to look up.

![A person standing in a rocky spatial environment with a large UI panel in mid-field.](https://developer.android.com/static/images/design/ui/xr/guides/env-comfort.jpeg)