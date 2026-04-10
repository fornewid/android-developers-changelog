---
title: https://developer.android.com/games/engines/godot/godot-formfactor
url: https://developer.android.com/games/engines/godot/godot-formfactor
source: md.txt
---

# Support multiple form factors and screen sizes

This topic describes how to support multiple form factors and screen sizes when using Godot for Android game development.

Android devices come in a variety of form factors and screen sizes. Common categories include:

- Mobile phones
- Tablets
- Televisions and television set-top boxes
- Laptops with Android Runtime for Chrome

This variety means your game will encounter a wide range of different screen resolutions. These screen resolutions often have different aspect ratios. For example:

- A phone in landscape orientation with a 19:9 aspect ratio (2280x1080)
- A different phone in landscape orientation with a 20:9 aspect ratio (3200x1400)
- A 1080p high definition television with a 16:9 aspect ratio (1920x1080)
- A tablet with a 4:3 aspect ratio (2048x1536)

The design of your game should take these differences into account to ensure correct presentation regardless of the screen resolution, aspect ratio of the device, and user input method.

## Display resolution

Godot defines screen resolution and size using pixels. We recommend that you set a standard base resolution for your Godot projects. Godot has settings for controlling behavior when display resolutions differ from the project's base resolution.

### Setting the base resolution

To set a base resolution for a project, with the project open in the Godot editor, perform the following steps:

1. Select**Project -\> Project Settings...**from the Godot menu bar.
2. In the**Project Settings** window, find the**Display** list in the**Category** tab, and then select the**Window**item.
3. Under the**Size** category, set the**Width** and**Height**fields to the desired base resolution as measured in pixels.

![Godot width and height project settings](https://developer.android.com/static/images/games/engines/godot/Screens_BaseResolution.png)**Figure 1.** The**Width** and**Height** fields in**Project Settings**

When the Godot editor is set to 2D view, it will display a guide rectangle corresponding to the base resolution. The base resolution is used as the default dimensions for the project window when running a project or scene from the editor.
![The base resolution rectangle in the Godot editor 2D view](https://developer.android.com/static/images/games/engines/godot/Screens_2DGuide.png)**Figure 2.**The base resolution rectangle in the Godot editor 2D view with the base resolution set to 640x360 pixels

### Stretch settings

Two settings control how the base resolution is adjusted when it differs from the display resolution:**Stretch Mode** and**Stretch Aspect** . These settings are in the**Project Settings** window, under the**Display -\> Window**section.
![Godot stretch project settings](https://developer.android.com/static/images/games/engines/godot/Screens_Stretch.png)**Figure 3.** The**Stretch Mode** and**Stretch Aspect** fields in**Project Settings**

**Stretch Mode** has three settings:`disabled`,`2d`, and`viewport`. The next section includes visual examples of different**Stretch Aspect** and**Stretch Mode**settings. All examples use a project base resolution of 320x180 pixels.

The`disabled`setting doesn't resize or adjust the base resolution. The value of**Stretch Aspect** is always ignored if**Stretch Mode** is set to`disabled`.
![Stretch mode disabled with display resolution of 320x180](https://developer.android.com/static/images/games/engines/godot/Screens_disabled_320x180.png)**Figure 4. Stretch Mode** `disabled`with a display resolution of 320x180

If the display resolution is smaller than the base resolution, the bottom and/or right edges are cropped.
![Stretch mode disabled with display resolution of 256x128](https://developer.android.com/static/images/games/engines/godot/Screens_disabled_256x128.png)**Figure 5. Stretch Mode** `disabled`with a display resolution of 256x128

If the display resolution is larger than the base resolution, the extra region is left empty.
![Stretch mode disabled with display resolution of 512x256](https://developer.android.com/static/images/games/engines/godot/Screens_disabled_512x256.png)**Figure 6. Stretch Mode** `disabled`with a display resolution of 512x256

The`2d`setting scales the base resolution to the display resolution. For projects using 2D artwork, this results in scaling artifacts due to there no longer being a 1:1 pixel ratio between the base and display resolution. This setting may be appropriate for certain styles of high-resolution artwork in projects where pixel-perfect rendering is not required.

The**Stretch Aspect** setting specifies constraints applied to the scaling to maintain the aspect ratio of the base resolution. The**Stretch Aspect** setting options are described in the Aspect ratio section. Below are examples of the`2d`**Stretch Mode** setting using a**Stretch Aspect** of`ignore`, which scales to the display resolution with no constraints:
![Stretch mode 2d with display resolution of 256x128](https://developer.android.com/static/images/games/engines/godot/Screens_2d_256x128.png)**Figure 7. Stretch Mode** `2d`with a display resolution of 256x128![Stretch mode 2d with display resolution of 512x256](https://developer.android.com/static/images/games/engines/godot/Screens_2d_512x256.png)**Figure 8. Stretch Mode** `2d`with a display resolution of 512x256

The`viewport`setting sets the root scene's`Viewport`to the base resolution. The rendered output of the root`Viewport`is then scaled to the display resolution. Godot`Viewport`objects are used to create views into the screen, or create subviews inside another`Viewport`. Unlike the`2d`setting, the`viewport`setting does not apply filtering when scaling to the display resolution. The`viewport`setting also uses the value of**Stretch Aspect** to determine whether constraints are applied to the scaling to preserve the aspect ratio. The`viewport`setting is a better choice than the`2d`setting when pixel-perfect precision is required, since primary rendering still occurs at the base resolution. Below are examples of the`viewport`**Stretch Mode** setting using a**Stretch Aspect** of`ignore`:
![Stretch mode viewport with display resolution of 256x128](https://developer.android.com/static/images/games/engines/godot/Screens_viewport_256x128.png)**Figure 9. Stretch Mode** `viewport`with a display resolution of 256x128![Stretch mode viewport with display resolution of 512x256](https://developer.android.com/static/images/games/engines/godot/Screens_viewport_512x256.png)**Figure 10. Stretch Mode** `viewport`with a display resolution of 512x256

### Aspect ratio

**Stretch Aspect** has several options for aspect ratio scaling constraints. If**Stretch Aspect** is set to`ignore`, no constraints are applied. When**Stretch Aspect** is set to`keep`, the base resolution is scaled to the largest dimensions possible that fit in the display resolution while maintaining the original aspect ratio. Regions of the display that aren't covered by the scaled image are filled with black bars. Depending on the dominant dimension of the aspect ratio difference, the bars will either be horizontal bars known as letterboxes, or vertical bars known as pillarboxes.
![Stretch mode viewport, stretch aspect keep, with display resolution of 384x256](https://developer.android.com/static/images/games/engines/godot/Screens_viewport_letter_384x256.png)**Figure 11. Stretch Mode** `viewport`,**Stretch Aspect** `keep`, with a display resolution of 384x256![Stretch mode viewport, stretch aspect keep, with display resolution of 512x200](https://developer.android.com/static/images/games/engines/godot/Screens_viewport_pillar_512x200.png)**Figure 12. Stretch Mode** `viewport`,**Stretch Aspect** `keep`, with a display resolution of 512x200

**Stretch Aspect** includes two variants of the`keep`setting:`keep_width`and`keep_height`. When`keep_width`is set, pillarboxing is added if the display resolution has a wider aspect ratio than the base resolution. However, if the display resolution has a taller aspect ratio than the base resolution, the extra area is left empty. The empty region fills out the bottom of the screen.
![Stretch mode viewport, stretch aspect keep_width, with display resolution of 512x384](https://developer.android.com/static/images/games/engines/godot/Screens_viewport_keep_width_512x384.png)**Figure 13. Stretch Mode** `viewport`,**Stretch Aspect** `keep_width`, with a display resolution of 512x384

The`keep_height`setting functions in the horizontal direction instead of the vertical direction. The empty region fills out the right side of the screen.
![Stretch mode viewport, stretch aspect keep_height, with display resolution of 512x200](https://developer.android.com/static/images/games/engines/godot/Screens_viewport_keep_height_512x200.png)**Figure 14. Stretch Mode** `viewport`,**Stretch Aspect** `keep_height`, with a display resolution of 512x200

The final**Stretch Aspect** setting is`expand`. The`expand`setting maintains the base resolution aspect ratio, but leaves the excess region empty instead of letterboxing or pillarboxing.
![Stretch mode viewport, stretch aspect expand, with display resolution of 384x256](https://developer.android.com/static/images/games/engines/godot/Screens_expand_384x256.png)**Figure 15. Stretch Mode** `viewport`,**Stretch Aspect** `expand`, with a display resolution of 384x256![Stretch mode viewport, stretch aspect expand, with display resolution of 512x256](https://developer.android.com/static/images/games/engines/godot/Screens_expand_512x256.png)**Figure 16. Stretch Mode** `viewport`,**Stretch Aspect** `expand`, with a display resolution of 512x256

## Anchors

UI element positioning requires additional considerations when supporting multiple screen resolutions. For example, using absolute pixel coordinates to place a control in the upper-right corner results in inconsistent positioning on devices with different horizontal resolutions. Godot's UI system supports relative positioning with the`Anchor`and`Margin`properties. The`Anchor`properties of a UI element specify an anchor point on its parent control object or viewport. Values from the`Margin`properties are then used to offset the control relative to its anchor point.

An object must derive from the Godot`Control`object if it is to include the`Anchor`and`Margin`properties. Godot's standard UI elements all derive from`Control`. Property fields for`Anchor`and Margin appear in the**Inspector** tab when a`Control`derived object is selected in the Godot editor.
![A button control selected with anchor and margin properties visible in the inspector](https://developer.android.com/static/images/games/engines/godot/Screens_anchor.png)**Figure 17.** A`Button`control selected, with the**Anchor** and**Margin**properties visible in the inspector

Godot has a**Layout** tool that can quickly set`Anchor`,`Margin`, and`Size`properties to commonly used preset values. When a`Control`derived object is selected in the editor, the**Layout** drop-down menu is available in the toolbar above the scene view. The**Layout**tool presets include positioning and positioning combined with size. The positioning presets support use cases such as: centered, anchoring to top-right, anchoring to center-left. The positioning plus size presets include use cases such as, anchoring to the bottom while spanning the entire parent width.
![Godot editor layout drop-down menu](https://developer.android.com/static/images/games/engines/godot/Screens_layout_menu.png)**Figure 18.** Godot editor**Layout**drop-down menu

Anchors are suitable for common use cases such as heads-up displays, on screen prompts, or basic dialog boxes. The Godot[Container](https://docs.godotengine.org/en/stable/tutorials/gui/gui_containers.html)system is intended for more sophisticated UI layouts, such as when displaying windows or dialogs with large numbers of controls, or dynamically resizing content.

## Field of view

Godot has field of view settings that control the presentation of a 3D scene in different aspect ratios. Field of view adjustments are controlled with the`Keep
Aspect`property of a`Camera`object. The default value of`Keep Height`is intended for projects that run in a landscape orientation.`Keep Height`adjusts to a wider or narrower field of view when the aspect ratios of the base resolution and the display resolution differ. The`Keep Width`setting is a better choice for projects that run in portrait orientation.`Keep Width`adjusts to a taller or shorter field of view based on the difference in aspect ratio.

## Viewport control

`Viewport`objects provide fine-tuned control over aspect ratio and scaling. Projects can use Viewports to perform operations, such as:

- Rendering a scene at its base resolution aspect ratio with a resolution independent border.
- Rendering a 3D scene at a reduced resolution for increased performance and displaying it upscaled to the native resolution.
- Rendering left and right eye views of a scene for VR applications.
- Generating dynamic textures.

For samples that demonstrate how to use the Viewport object, see the[Godot Viewport](https://github.com/godotengine/godot-demo-projects/tree/master/viewport)samples.

## User input

Some game designs aren't compatible with every mode of input supported by Android. Games that support multi-touch gestures often have issues adding support for mouse and game controller input. Games designed around game controller input can struggle to implement effective touch controls. Godot supports all of these forms of input, but you should decide early in development which input methods you intend to use in your project and design accordingly.

For projects where touch and mouse input are interchangeable, Godot includes proxy options that generate emulated touch events from mouse events and vice versa. These options eliminate the need to write separate input handling code for mouse and touch events. The available options are:**Emulate Touch from Mouse** and**Emulate Mouse from Touch** . Both options are located in**Project Settings** under the**Input Devices -\> Pointing**section.
![Godot project settings for input devices](https://developer.android.com/static/images/games/engines/godot/Screens_input.png)**Figure 19.** The**Input Devices -\> Pointing** settings in the**Project Settings**

## Additional resources

- [Godot Documentation - Size and anchors](https://docs.godotengine.org/en/stable/tutorials/gui/size_and_anchors.html)
- [Godot Documentation - Viewports](https://docs.godotengine.org/en/stable/tutorials/viewports/viewports.html)
- [Godot FAQ - Multiple resolutions](https://docs.godotengine.org/en/stable/about/faq.html#how-should-assets-be-created-to-handle-multiple-resolutions-and-aspect-ratios)
- [Godot Sample - 3D viewport scaling](https://github.com/godotengine/godot-demo-projects/tree/master/viewport/3d_scaling)
- [Godot Tutorial - Containers](https://docs.godotengine.org/en/stable/tutorials/gui/gui_containers.html)
- [Godot Tutorial - Multiple resolutions](https://docs.godotengine.org/en/stable/tutorials/viewports/multiple_resolutions.html)