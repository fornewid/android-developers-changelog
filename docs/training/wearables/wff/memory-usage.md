---
title: https://developer.android.com/training/wearables/wff/memory-usage
url: https://developer.android.com/training/wearables/wff/memory-usage
source: md.txt
---

Wear OS improves battery life by tracking memory use. Watch faces using the
Watch Face Format have memory limits, as per the [Wear OS app quality
guidelines](https://developer.android.com/docs/quality-guidelines/wear-app-quality#memory-usage):

- Ambient mode: 10 MB maximum memory use.
- Interactive mode: 100 MB maximum memory use.

> [!NOTE]
> **Note:** Memory calculations only include bitmaps, fonts, and XML-derived layers.

## Memory usage calculation

To compute memory usage for an image or bitmap font in a watch face using the
Watch Face Format, the system does the following:

1. Decompress the image or font.
2. Check if the following optimizations apply:
   - Resizing to better fit the screen
   - Cropping transparent pixels
   - Downsampling to [RGB565](https://en.wikipedia.org/wiki/List_of_monochrome_and_RGB_color_formats#16-bit_RGB_(also_known_as_RGB565)), without loss of fidelity

Based on the resulting bounding box, the size is computed as follows:

- For images and fonts using [RGBA8888](https://en.wikipedia.org/wiki/RGBA_color_model#RGBA8888): 4 x width x height
- For images and fonts using RGB565: 2 x width x height
- For images and fonts using the ALPHA_8 bitmap configuration: width x height

> [!NOTE]
> **Note:** If an image has multiple frames (like an animated GIF), the system decompresses each frame. The union of bounding boxes across all frames is the animation's bounding box.

### Interactive mode

To compute memory usage for interactive mode, the system sums the following
values:

1. The unprocessed size of any [vector fonts](https://developer.android.com/guide/topics/resources/font-resource)
2. The estimated usage of the system's default font
3. The total size of the images and bitmap fonts after cropping, resizing, and reformatting is applied

### Configurations

For watch faces with [configurations](https://developer.android.com/training/wearables/wff/user-configuration/user-configurations), the system attempts to calculate the
total size of the watch face resources across different configurations. If the
number of combinations is very large, the system may overestimate how many
resources are used simultaneously.

### Ambient mode and layers

The system assumes ambient mode uses up to three full-screen layers, two of
which are static. The layers include:

1. The watch face background. The system treats this as one image, regardless of how many images the background comprises.
2. Moving parts like hands, digital displays, or dynamic elements.
3. Remaining elements from the source XML file.

Large bitmap fonts often use the most memory in ambient mode.

## Methods of reducing memory usage

Use the following optimizations to reduce memory usage.

> [!TIP]
> **Tip:** Use the [Watch Face Format Optimizer](https://github.com/google/watchface/tree/main/tools/wff-optimizer) to automatically apply some optimizations.

### Crop and resize bitmap fonts

Crop your images and [`BitmapFont`](https://developer.android.com/training/wearables/wff/group/part/text/bitmap-font) objects to match the display size.

Wear OS draws watch faces with all images decompressed. A mostly blank
full-screen image might consume 3 KB on disk, but 750 KB or more on a
450-pixel x 450-pixel screen.

### Use consistent bitmap font heights

When using a `BitmapFont`, ensure all images for a character have the same
height. Likewise, ensure all images for words have the same height.

### Use consistent frame sizes in animations

Instead of moving an image across a watch face, update the elements in the image
and keep the bounding box position fixed. For example, to animate a circle on
your watch face, change its color instead of rolling it.

This technique shrinks the size of the animation's calculated bounding box.

### Deduplicate images

To display an image multiple times, include only one image resource and
reference it multiple times.

### Show progress using arcs

To simulate a progress bar finishing after 1 minute or 1 hour, don't use 60
images. Use an [`Arc`](https://developer.android.com/training/wearables/wff/group/part/draw/shape/arc) object with an expression controlling its length, as
shown here:

<br />

```xml
<PartDraw angle="0" width="400" height="400" name="ProgressBar"
    pivotX="0.5" pivotY="0.5" x="25" y="25">
    <Arc centerX="200" centerY="200" width="400" height="400"
        startAngle="0" endAngle="360">
        <!-- Completes a "progress loop" every minute. -->
        <Transform target="endAngle"
            value="0 + (clamp([SECOND], 0, 60) - 0) * 6" />
        <Stroke cap="ROUND" color="#654456" thickness="10" />
    </Arc>
</PartDraw>
```

<br />

To display a noncontinuous line, for example to achieve a retro digital watch
style look, use a dash property for a [`Stroke`](https://developer.android.com/training/wearables/wff/group/part/draw/style/stroke) object or a semitransparent
mask image overlay.

### Place watch hands and complications at the end of the source file

XML nodes are drawn in the order listed in the source XML. By putting watch
hands and complications at the end, you enable the system to eliminate an entire
layer from the ambient mode memory calculation.

## Evaluate the memory usage of your watch face

To measure the memory usage of your watch face, use the memory footprint
evaluator tool, available in the [`watchface`](https://github.com/google/watchface) repository on GitHub.

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Arc](https://developer.android.com/training/wearables/wff/group/part/draw/shape/arc)
- [Line](https://developer.android.com/training/wearables/wff/group/part/draw/shape/line)
- [Rectangle](https://developer.android.com/training/wearables/wff/group/part/draw/shape/rectangle)