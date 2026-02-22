---
title: https://developer.android.com/design/ui/xr/guides/get-started
url: https://developer.android.com/design/ui/xr/guides/get-started
source: md.txt
---

To unlock the full potential of Android XR immersive experiences, it helps to understand spatial computing, immersion, and how to blend digital content with a user's physical environment.

Great immersive XR design delivers a comfortable experience that's natural and intuitive. It draws users in and encourages them to explore all that your app has to offer. Android XR apps can help users throughout their day to:

- Focus on work, and be more productive and creative
- Watch videos, play games, listen to music, and browse photos
- Discover and learn
- Communicate and connect with family and friends
- Improve mental and physical health

## Considerations for a high-quality XR app

### Start from where you are

Android XR supports designing from where you are today. You can develop a new app or update an existing one with Android Jetpack XR, Unity, OpenXR, or WebXR.

<br />

**Build a new app or spatialize an Android app**   
You can build a new app from scratch, or adapt an Android large screen or mobile app for XR by adding spatial components.

Alas, your browser doesn't support HTML5 video. That's OK! You can still[download the video](https://developer.android.com/static/videos/design/ui/xr/xr-design-1-opt.mp4)and watch it with a video player.

An Android large screen app adapted for Android XR  
**Build a new app or port a Unity, OpenXR, or WebXR app**   
You can bring existing immersive experiences to a new audience, with minimal development lift.

Alas, your browser doesn't support HTML5 video. That's OK! You can still[download the video](https://developer.android.com/static/videos/design/ui/xr/onehandedcv1.mp4)and watch it with a video player.

Vacation Simulator, a Unity app ported to Android XR

<br />

**Follow established patterns** . You can use[Material Design guidelines](https://m3.material.io/)and[components](https://m3.material.io/components)to create a consistent experience across platforms. For Android apps, adopt established[UI patterns](https://developer.android.com/design/ui/large-screens). For[Unity](https://docs.unity3d.com/Manual/index.html),[OpenXR](https://registry.khronos.org/OpenXR/specs/1.0/styleguide.html), or[WebXR](https://immersiveweb.dev/)apps, apply platform-specific design guidelines to ensure a seamless user experience.

**Leverage users' knowledge**. Use common elements like buttons, menus, and text fields that users already know from other platforms. Design consistent interactions to help users navigate your app. Add visual cues to show how they might interact with objects.

## Make users feel comfortable and safe

Keep comfort in mind in every part of your design, with considerations for how people naturally move. Allow users to interact with your app in different body positions, using their hands, eyes, voice, physical keyboard, mouse, or controller.

**Design comfortable interactions**. Center interactable elements in a user's field of view to minimize head and eye strain. Keep content within clear boundaries to help users stay oriented and prevent sensory overload. Reserve large-scale head and body movements for interactions that genuinely enhance the experience.

**Accommodate seated, standing, and reclined experiences**. Position UI elements, controls, and interactive objects within the user's field of view. Enable custom height settings so users can personalize their experience.

**Prevent motion sickness during movement** . Use predictable[motion](https://developer.android.com/design/ui/xr/guides/motion)and stable frame rates to help users anticipate changes in the environment. Avoid unexpected movements such as abrupt accelerations, decelerations, or direction changes. It helps to keep some items stationary for a frame of reference.

**Allow users to choose between real and virtual worlds** . If your app supports full immersion to transport users to a virtual space, consider offering a[passthrough](https://developer.android.com/design/ui/xr/guides/foundations#give-users)option so users can see their physical space alongside your app when possible.
| **Note:** Full immersion behaves differently on XR glasses. Users retain visibility of their physical surroundings in their periphery and through the display's inherent transparency.

## Consider display technologies

Android XR immersive experiences run on a diverse range of hardware. While all devices support the core interaction models, the display technology fundamentally changes how digital content blends with the physical world.

Broadly, immersive devices fall into two categories:**XR headsets** , which use cameras to stream the outside world, and**wired XR glasses**, which use transparent lenses. Understanding these differences is critical for color selection, UI placement, and immersive design.

### XR headsets

XR headsets use high-resolution cameras to capture the physical world and stream it to displays inside the headset.

**Visuals**: Because the display is opaque, it can render "true black" and fully occlude the real world. This allows for complete virtual immersion (VR) where the physical environment is replaced entirely.
Alas, your browser doesn't support HTML5 video. That's OK! You can still[download the video](https://developer.android.com/static/images/design/ui/xr/xr-headsets.mp4)and watch it with a video player.

**Field of View**: Headsets typically offer a wide field of view (110°+), allowing for immersive, peripheral-filling interfaces.
Alas, your browser doesn't support HTML5 video. That's OK! You can still[download the video](https://developer.android.com/static/images/design/ui/xr/content-maps.mp4)and watch it with a video player.

**Inputs**: Primary inputs often include hand tracking, eye tracking, and dedicated 6DoF controllers.

### XR glasses (wired)

Wired XR glasses use additive light displays (such as waveguides) to project light onto semi-transparent lenses. Users view the physical world directly through the glass, with digital content overlaid on top.
Alas, your browser doesn't support HTML5 video. That's OK! You can still[download the video](https://developer.android.com/static/images/design/ui/xr/real-world-connection.mp4)and watch it with a video player.

**Additive color \& transparency**: In an additive display, pure black renders as transparent. Darker colors are rendered by emitting less light, which effectively reduces their opacity.
Alas, your browser doesn't support HTML5 video. That's OK! You can still[download the video](https://developer.android.com/static/images/design/ui/xr/additive-display.mp4)and watch it with a video player.

**Field of View**: The FOV is more focused, typically between 50° and 70°. While this still provides a wide-screen experience, it's narrower than a headset. UI scaling automatically adjusts content to keep it within this focused area.
Alas, your browser doesn't support HTML5 video. That's OK! You can still[download the video](https://developer.android.com/static/images/design/ui/xr/fov.mp4)and watch it with a video player.

**Dimming**: Many devices use electrochromatic dimming to darken the lenses globally, helping virtual content stand out against bright physical environments.
Alas, your browser doesn't support HTML5 video. That's OK! You can still[download the video](https://developer.android.com/static/images/design/ui/xr/adjustable-dimming.mp4)and watch it with a video player.

**Inputs**: Due to their form factor, glasses often rely on natural inputs (hands) and peripheral devices (such as phones, bluetooth keyboards/mice) rather than bulky dedicated controllers.

|         Feature         |                                 XR Headsets                                  |                                      XR Glasses (wired)                                      |
|-------------------------|------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| **Environment View**    | Digitized video feed (opaque display)                                        | Direct physical view (transparent lenses)                                                    |
| **Display type**        | MicroLED opaque displays, which can render full color ranges and pure blacks | Transparent additive optics, which can't render pure black and always have some transparency |
| **Immersion**           | Can completely block out the real world                                      | World is always visible; electrochromatic dimming can increase immersiveness                 |
| **Field of View (FOV)** | Wide (\~110°+)                                                               | Focused (\~50° - 70°)                                                                        |
| **UI Scaling**          | Standard scaling for immersive canvas                                        | Automatic scaling to fit content in narrower FOV                                             |
| **Mobility**            | Tethered or battery-constrained; designed for stationary or room-scale use   | High mobility; lightweight design for comfortable movement                                   |

## Explore experiences that feel special in XR

Android XR includes features to help you harness the infinite display and create engaging, immersive experiences.

**Interactive 3D models**. You may want to add interactive 3D objects that are realistic, stylized, or playful. Typically, 3D objects are rendered with depth and volume, can be viewed from all angles, and be moved with natural interactions using gestures.

**Fully-immersive virtual environments**. Save full immersion for experiences that significantly benefit from it. Choose a key moment to transport a user to a new reality, replacing their physical surroundings with a virtual space.

**Consider immersive blending** . In[passthrough](https://developer.android.com/design/ui/xr/guides/foundations#give-users)mode, you can blend virtual elements with a user's physical environment. Design virtual objects with natural lighting and occlusion to add a realistic feel.

**Spatial audio**. To add another layer of realism and immersion, position sounds accurately in an environment to create a believable soundscape that increases a user's spatial awareness.

## Make your app accessible

Android XR is designed to make it easy for all users to navigate, understand, and enjoy your app.  
Alas, your browser doesn't support HTML5 video. That's OK! You can still[download the video](https://developer.android.com/static/videos/design/ui/xr/xr-accessible-design.mp4)and watch it with a video player.

**System features** . Android XR includes mobile and large-screen accessibility features such as voice to text, live captions, color inversion and correction, magnification, and[dwell control](https://support.google.com/accessibility/android/answer/7071579). The platform is also adapted for[Google's TalkBack screen reader](https://developer.android.com/guide/topics/ui/accessibility/apps#describe-ui-element).

**Colors and lighting** . Provide sufficient[color contrast](https://m3.material.io/foundations/designing/color-contrast)to aid users with color vision differences. Keep contrast ratios for readability, especially if you use any transparent backgrounds. Use dimming to create contrast between your app and the user's surroundings. Avoid sudden shifts in brightness or color to prevent eye discomfort.

**Consider dynamic size and scale** . Larger UI and pointer[targets](https://developer.android.com/design/ui/xr/guides/visual-design#targets-android)make it easier for users to select and manipulate elements in space. If you are building an Android app, it will automatically scale when users move or resize it.

**Reduce cognitive load**. Present users with a limited number of choices at a time. Offer visual or audio feedback to confirm actions. Reveal advanced features gradually to avoid overwhelming users with excessive information.

**Design for both direct and distance interactions**, so users can comfortably interact with objects near and far. Users should be able to pick up a virtual tool, press a button, or resize a 3D object whether it's in arm's reach or further away.

[Learn about accessible multimodal inputs](https://developer.android.com/design/ui/xr/guides/foundations#design-multimodal).

*** ** * ** ***

OpenXR™ and the OpenXR logo are trademarks owned by The Khronos Group Inc. and are registered as a trademark in China, the European Union, Japan and the United Kingdom.