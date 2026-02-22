---
title: https://developer.android.com/training/wearables/watch-face-designer/basics
url: https://developer.android.com/training/wearables/watch-face-designer/basics
source: md.txt
---

This guide explains how to create a watch face, add time-based elements, and
include support for user-selected photos, including a multi-photo gallery. For
additional features, see the [advanced](https://developer.android.com/training/wearables/watch-face-designer/advanced) guide.

## Create a watch face

To create a watch face, [draw a frame in Figma](https://help.figma.com/hc/articles/360041539473-Frames-in-Figma-Design), then configure
it as follows:

1. Set its size to 450 units wide by 450 units tall:

   ![The width and height options appear in text boxes labeled W and
   H, respectively](https://developer.android.com/static/wear/images/design/watch-face-designer/wf-layout.png) **Figure 1**: Figma's frame layout panel, showing a 450x450 watch face

   Other sizes work too, but 450x450 is recommended for Wear OS watch faces and
   is required for export to Watch Face Studio.
2. For a battery efficient watch face, set the frame's fill color to black:

   ![Fill color uses six alphanumeric digits representing a hex
   color](https://developer.android.com/static/wear/images/design/watch-face-designer/black-fill-color.png) **Figure 2**: Frame fill panel showing a black fill color
3. Set the frame's name to what you'd like your watch face to be called. This
   appears on your users' watches.

After creating and configuring the frame, open the Watch Face Designer
[plugin](https://help.figma.com/hc/articles/360042532714-Use-plugins-in-files), and select the frame you just created. A live preview
of it appears in the Watch Face Designer window.

## Add elements to a watch face

Add some elements to the watch face so users can tell the time.

### Analog time

[Draw a rectangle](https://help.figma.com/hc/articles/360040450133-Shape-tools), which acts as the second hand on your watch.

Verify that, when showing the beginning of a new minute, the rectangle is
horizontally centered and that its bottom edge sits on the center of the watch
face, just as a real clock hand would be. By default, Figma enables
**Snap to Geometry**, which shows red guidelines to help you with this rectangle
alignment:
![](https://developer.android.com/static/wear/images/design/watch-face-designer/alignment.png) **Figure 3**: Positioning a frame using Figma's Snap to Geometry feature

Next, inform Watch Face Designer that this layer isn't just for decoration.
Select the rectangle that you drew in the previous step, then navigate to the
**Watch Face Designer** window and change **Behavior** from "Static" to "Second
hand."
![The 'Second hand' option is near the middle of the list](https://developer.android.com/static/wear/images/design/watch-face-designer/assignment.png) **Figure 4**: Assign a layer to the "second hand" function

Notice how the hand begins to move once each second, simulating a clock tick.
You can adjust how it rotates if you want, and you can create a minute hand and
hour hand similarly to how you made this one.

For advice on subdials, see the [advanced usage](https://developer.android.com/training/wearables/watch-face-designer/advanced) guide.

### Digital time

We can also display the time using a digital format. To do so, [create a text
layer in Figma](https://help.figma.com/hc/articles/360039956434-Guide-to-text-in-Figma-Design). For now, enter `Hh:Mm:Ss` as the text content
of the layer.

In the **Watch Face Designer** window, change the text's **Behavior** from
"Static" to "Digital time." The preview shows how this would look on a real
device:
![](https://developer.android.com/static/wear/images/design/watch-face-designer/digital-preview.png) **Figure 5**: Digital time preview in Watch Face Designer

To learn about the set of available characters you can use, follow the template
guide displayed in the sidebar of the **Watch Face Designer** window. For
example, `a` represents whether the current time is "AM" or "PM," which you can
use with the "hour format" to display 12-hour time.

You can select any font in Figma, including ones that aren't available in
Wear OS, and it's automatically exported and bundled into your watch face. Keep
in mind that each font has its own licensing terms for redistribution.

## Preview different times

To see your watch face at different times of day, you can adjust what time the
preview is showing by dragging the slider at the bottom of the
**Watch Face Designer** window:
![](https://developer.android.com/static/wear/images/design/watch-face-designer/time-scrubber.png) **Figure 6** : The time scrubbing bar at the bottom of the **Watch Face Designer** window. The bottom-left element shows the current time being previewed using a 24-hour hour/minute/second format.

When you're finished previewing different times, you can reset the time to the
current time by selecting the **Reset** button in the bottom-left corner:
![](https://developer.android.com/static/wear/images/design/watch-face-designer/reset-time.png) **Figure 7** : Reset to the current time using the bottom-left corner of the **Watch Face Designer** window.

## Include user-provided photos

Your watch face can include a slot for a custom photo. This lets users add a
photo that's personal to them as a backdrop, while still showing the time and
any other elements you've included in your design.
| **Note:** If your watch face uses this element, it becomes available only on watches that run Wear OS 6 or higher, as this was the version that added support for user-provided photos.

To support custom photos, add a layer to your watch face, and set its
**Behavior** to "User-provided photo." For this example, we're [using a sample
photograph of a flower for this layer as the default image](https://www.figma.com/best-practices/working-with-images-in-figma/).
This image is used as a fallback before the user has assigned their own photo,
or when the user chooses not to use one of their photos.
![](https://developer.android.com/static/wear/images/design/watch-face-designer/user-photo.png) **Figure 8**: Add support for user-provided photos

### Support multiple selection of photos

Your watch face can support multi-selection of photos. Watch Face Designer calls
this a *gallery*:
![](https://developer.android.com/static/wear/images/design/watch-face-designer/gallery.png) **Figure 9**: Gallery options for user-provided photos

When **Photo selection** is set to "Gallery," the user can select multiple
photos for this slot, and the [watch cycles through them at different
points](https://developer.android.com/training/wearables/wff/images), depending on what you select under "Change photo:"

- When "On tap" is selected, the photo changes when the user taps on your layer.
- When "On wrist raise" is selected, the changes every third time the user raises their wrist. At the moment, this cannot be adjusted using Watch Face Designer. Learn more about how Watch Face Format provides more advanced support using the [`changeAfterEvery`](https://developer.android.com/reference/wear-os/wff/group/part/image/photos) attribute.

## Learn more

To preview your watch face on a physical device, see the [exports](https://developer.android.com/training/wearables/watch-face-designer/export) guide.

For more options and features, see the [advanced usage](https://developer.android.com/training/wearables/watch-face-designer/advanced) guide.