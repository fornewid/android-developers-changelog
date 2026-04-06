---
title: https://developer.android.com/design/ui/mobile/guides/layout-and-content/images-graphics
url: https://developer.android.com/design/ui/mobile/guides/layout-and-content/images-graphics
source: md.txt
---

![](https://developer.android.com/static/images/design/ui/mobile/graphics_11.png)

While your app could contain only text and color, you might want to add more
visual elements, such as a logo or illustration. Android has particular best
practices for adding graphics to your app along with various libraries to create
graphic effects or add motion.

An Android asset is referred to as a [drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable), a type of resource that is
drawn on the screen. This includes, but is not limited to, bitmaps, shapes, and
vectors.

When creating images and graphics keep the following in mind:

- Avoid including immutable text in assets.
- Use vector formats first whenever possible.
- Provide assets for resolution buckets.
- Provide sufficient scrim between background images and text.
- Although Android is able to achieve different image effects like gradients, colorization, and blurs, some are more performance costly.
- Animated Vector Drawables provide a scalable format for small UI animations.

## How to export assets for Android

- Format asset names in lowercase.
- Set simplistic assets to export as SVG.
- Set complex images, like photos, to export as WebP, PNG, JPG.
- Set correct resolution scaling as shown in the following table.

| Screen size | Scale |
|---|---|
| mdpi | x1 |
| hdpi | x1.5 |
| xhdpi | x2 |
| xxhdpi | x3 |
| xxxhdpi | x4 |

Optionally you can convert SVGs to Vector Drawables (VD) using Android Studio.
Organize assets into directories corresponding to resolution for handoff as
shown in the following image. For example, include screen size in folder names.
![organized res directory](https://developer.android.com/static/images/design/ui/mobile/graphics_6.png) **Figure 2.** Organized res directory.

## Asset types

Android supports the following asset types.

### Vector

A vector graphic is a lossless format, which means that it does not lose visual
information when scaled. Vectors are composed of mathematical points that are
filled to create an image.
![](https://developer.android.com/static/images/design/ui/mobile/graphics_7.png) **Figure 3.** The left image shows an image composed of vector graphic bezier points in contrast with a zoomed in raster image on the right.

#### Vector formats

Android supports the following vector image formats: SVGs and Vector Drawables.

Vector Drawables look similar to SVGs but are XML-based. They also support
various attributes, like gradients. For more information on what is supported,
see [`VectorDrawable`](https://developer.android.com/reference/android/graphics/drawable/VectorDrawable). You can convert SVGs to Vector Drawables through
[Vector Asset Studio](https://developer.android.com/studio/write/vector-asset-studio#running).

#### Use cases

Because of their small size, it's best to create icons using a vector format. An
[Animated Vector Drawable](https://developer.android.com/reference/android/graphics/drawable/AnimatedVectorDrawable) can be used to add motion to an icon.

- Illustrations are graphics that help direct users, explain concepts, or express ideas. They typically express the brand style.
- Hero illustrations are high-emphasis amongst the rest of the content, used to set overall look and feel and explain primary information.
- Spot illustrations are smaller, typically inline, and support the surrounding content.

![](https://developer.android.com/static/images/design/ui/mobile/graphics_4.png) **Figure 4.** A hero illustration and an inline spot illustration.

### Raster

A lossy graphic, or a graphic that loses detail when manipulated through
compression or scaling, is composed of pixels to make up the image. Raster
graphics are commonly used for detailed images such as photos or complex
gradients. Since they lose detail when scaled, export multiple resolutions of
these images.

#### Raster formats

Android supports the following raster image formats: PNG, GIF, JPG, WebP.

#### Use cases

Use cases include images that have a range of textures resulting in a wide color
palette and gradation, or images that would have an overly complex set of bezier
points. Use cases could also include highly detailed photo assets such as
product photos, location details and more.

## Sizing

When creating assets keep the following considerations in mind.

### Resolution buckets

Your app should provide bitmap graphics based on screen density ranges or
buckets. The operating system automatically displays the correct graphic to
the device in question using these buckets. Ensure high-fidelity graphics are
shown on every device by providing assets for each bucket.
![Example of image resolution sizes and bucket labels.](https://developer.android.com/static/images/design/ui/mobile/graphics_5.png) **Figure 5.** Party cantaloupe in their respective densities and scale to export. **Note:** You don't need to provide vector drawables for all densities, since vectors automatically scale across densities.

### Padding

Icons and similar small assets should include intrinsic (built-in) padding to
give the asset enough touch target space and ensure consistent sizing.
![](https://developer.android.com/static/images/design/ui/mobile/graphics_8.png) **Figure 6.** 24 dp icons with padding built into assets.

## File names

Android assets are lowercase and don't include a resolution suffix.

Keep a consistent naming convention and structure to keep your files and
projects organized. For example, naming icons with the prefix "ic_..." can help
organize all icons in your project, and help quickly identify icons during
development.

## Other app assets

![](https://developer.android.com/static/images/design/ui/mobile/graphics_3.png) **Figure 7.** Monochrome launcher icons and splash screens.

### App icons

Launcher icons are found on the homescreen. Find monochrome icons in the System
UI, including monochrome notifications, status bar, and widgets.

Format [app icons](https://developer.android.com/develop/ui/views/launch/icon_design_adaptive) as vector drawables for adaptive icons and PNG for legacy
icons. To learn more about creating and previewing your app icon, check out
[Design and Preview your App Icons](https://codelabs.developers.google.com/design-android-launcher).

### Splash screens

Starting with Android 12, your app can display an animated [splash screen](https://developer.android.com/develop/ui/views/launch/splash-screen)
that features the app icon while your app opens.

## Placement

Note how images should [scale](https://developer.android.com/design/ui/mobile/guides/layout-and-content/layout-basics) and position on the screen. **Fit, Crop,
FillHeight, FillWidth, FillBounds, Inside** , and **None** are available to [set
the scaling](https://developer.android.com/develop/ui/compose/graphics/images/customize#content-scale) on an image.
![](https://developer.android.com/static/images/design/ui/mobile/graphics_1.png) **Figure 8.** Cropping examples.

You can also clip images to a shape to create additional effects.

### Responsive cropping

To display images responsively, define how an image will be cropped at different
breakpoint ranges. At different breakpoint ranges cropping can:

- Maintain one fixed ratio.
- Adapt to different ratios.
- Maintain fixed image heights.

#### Maintain one ratio

Image sizing can hold one fixed ratio across breakpoint ranges.
![](https://developer.android.com/static/images/design/ui/mobile/graphics_2.png) **Figure 9.** An image shown in different aspect ratios.

#### Adapt to different ratios

Image ratios can change by adapting to different breakpoint ranges. For example,
in figure 9 the image ratio changes from 1:1 to 16:9 between breakpoints.

#### Fixed image heights

Image sizing can maintain a fixed height and fluid width across and within
breakpoint ranges. The image maintains a fixed height while the width between
breakpoints is fluid.

## Effects

Android includes various built-in image effects. Here are some common effects:

### Gradients

In Compose, use a [Brush](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/Brush) to draw something on the screen. Different brushes
can be used to draw shapes of different colors or gradients. Use the built-in
[gradient brushes](https://developer.android.com/develop/ui/compose/graphics/draw/brush#gradient-brushes) to achieve different gradient effects. These brushes
allow you to specify the list of colors that you would like to create a gradient
from.

Gradient brushes are capable of more advanced gradients by adding color stops
and tiling, as long as you provide the list of colors and percentages where the
stop occurs. Use containers or shapes to crop gradients, solid color fills, or
images.
![](https://developer.android.com/static/images/design/ui/mobile/graphics_9.png) **Figure 10.** Translate a gradient from Figma using compose modifiers.

### Blur

Apply blurring effects to images by using the `Modifier.blur()` method and
providing the blur ratios. Use blurs with caution because they can affect
performance and are only available on devices running Android 12 and higher. For
more information, see [Blur an image composable](https://developer.android.com/develop/ui/compose/graphics/images/customize#blur_an_image_composable).

### Blend modes

Android is capable of modifying images through similar boolean operations and
blend modes you might find in design software, like union or multiply. For more
information, see [BlendMode](https://developer.android.com/reference/android/graphics/BlendMode).

### Tint

Use blend modes and fills to tint assets. This lets you have a single asset
and apply different colors to it, which can reduce the amount of produced
assets.
![](https://developer.android.com/static/images/design/ui/mobile/graphics_10.png) **Figure 11.** Assets with different tints used to complement the content colors or to indicate different states.

### Motion

Graphics can be animated programmatically to create motion graphics instead of
uploading motion files. This can allow for greater flexibility and smaller asset
resources.

Animated Vector Drawables lets you create small UI animations. Otherwise, learn
more about animating with keyframes in [Compose](https://developer.android.com/develop/ui/compose/graphics). For more on image effects
read [Customize an image](https://developer.android.com/develop/ui/compose/graphics/images/customize#border-image).