---
title: https://developer.android.com/training/multiscreen/screendensities
url: https://developer.android.com/training/multiscreen/screendensities
source: md.txt
---

Android devices not only have [different screen sizes](https://developer.android.com/training/multiscreen/screensizes)---handsets, tablets, TVs,
etc.---but also have screens with different pixel sizes. One
device might have 160 pixels per inch, while another device fits 480
pixels in the same space. If you don't consider these variations in
pixel density, the system might scale
your images, resulting in blurry images, or the images might
appear at the wrong size.

This page shows you how you can design your app to support
different pixel densities by using resolution-independent units of measurements
and providing alternative bitmap resources for each pixel density.

Watch the following video for an overview of these techniques.  

For more information about designing icon assets, see the [Material Design icon guidelines](https://m3.material.io/styles/icons/designing-icons).

## Use density-independent pixels

Avoid using pixels to define distances or sizes. Defining dimensions with
pixels is a problem because different screens have different pixel densities,
so the same number of pixels corresponds to different physical sizes on
different devices.
![An image showing two example device displays with different densities](https://developer.android.com/static/images/screens_support/densities-phone_2x.png) **Figure 1**: Two screens of the same size can have a different number of pixels.

To preserve the visible size of your UI
on screens with different densities, design your UI using
*density-independent pixels* (dp) as your unit of measurement. One dp is a
virtual pixel unit that's roughly equal to one pixel on a medium-density screen
(160 dpi, or the "baseline" density). Android translates this value to the
appropriate number of real pixels for each other density.

Consider the two devices in figure 1. A view that is
100 pixels wide appears much larger on the device on the left. A view
defined to be 100 dp wide appears the same size on both screens.

When defining text sizes, you can instead use *scalable
pixels* (sp) as your units. The sp unit is
the same size as a dp, by default, but it resizes based on the user's preferred
text size. Never use sp for layout sizes.

For example, to specify spacing between two views, use dp:  

```xml
<Button android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:text="@string/clickme"
    android:layout_marginTop="20dp" />
```

When specifying text size, use sp:  

```xml
<TextView android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:textSize="20sp" />
```

### Convert dp units to pixel units

In some cases, you need to express dimensions in dp and then
convert them to pixels. The conversion of dp units to screen pixels
is as follows:

`px = dp * (dpi / 160)`

**Note:** Never hardcode this equation to calculate pixels. Instead, use
[TypedValue.applyDimension()](https://developer.android.com/reference/android/util/TypedValue#applyDimension(int,%20float,%20android.util.DisplayMetrics)),
which converts many types of dimensions (dp, sp, etc.) to pixels for you.

Imagine an app in which a scroll or fling gesture is recognized
after the user's finger has moved at least 16 pixels. On a baseline
screen, a user's finger must move `16 pixels
/ 160 dpi`, which equals 1/10 of an inch (or 2.5 mm), before
the gesture is recognized.

On a device
with a high-density display (240 dpi), the user's finger must move
`16 pixels / 240 dpi`, which
equals 1/15 of an inch (or 1.7 mm). The distance is much shorter, and
the app therefore appears more sensitive to the user.

To fix this issue, express the gesture threshold in code in dp and
then convert it to actual pixels. For example:  

### Kotlin

```kotlin
// The gesture threshold expressed in dp
private const val GESTURE_THRESHOLD_DP = 16.0f

private var gestureThreshold: Int = 0

// Convert the dps to pixels, based on density scale
gestureThreshold = TypedValue.applyDimension(
  COMPLEX_UNIT_DIP,
  GESTURE_THRESHOLD_DP + 0.5f,
  resources.displayMetrics).toInt()

// Use gestureThreshold as a distance in pixels...
```

### Java

```java
// The gesture threshold expressed in dp
private final float GESTURE_THRESHOLD_DP = 16.0f;

// Convert the dps to pixels, based on density scale
int gestureThreshold = (int) TypedValue.applyDimension(
  COMPLEX_UNIT_DIP,
  GESTURE_THRESHOLD_DP + 0.5f,
  getResources().getDisplayMetrics());

// Use gestureThreshold as a distance in pixels...
```


The [DisplayMetrics.density](https://developer.android.com/reference/android/util/DisplayMetrics#density) field
specifies the scale factor used to convert dp units to
pixels according to the current pixel density. On a medium-density screen,
`DisplayMetrics.density` equals
1.0, and on a high-density screen it equals 1.5. On an extra-high-density screen,
it equals 2.0, and on a low-density screen, it equals 0.75. This figure is
used by [TypedValue.applyDimension()](https://developer.android.com/reference/android/util/TypedValue#applyDimension(int,%20float,%20android.util.DisplayMetrics)) to
get the actual pixel count for the current screen.

### Use pre-scaled configuration values

You can use the [ViewConfiguration](https://developer.android.com/reference/android/view/ViewConfiguration) class to access common
distances, speeds, and times used by the Android system. For instance, the
distance in pixels used by the framework as the scroll threshold can be obtained
with [getScaledTouchSlop()](https://developer.android.com/reference/android/view/ViewConfiguration#getScaledTouchSlop()):  

### Kotlin

```kotlin
private val GESTURE_THRESHOLD_DP = ViewConfiguration.get(myContext).scaledTouchSlop
```

### Java

```java
private final int GESTURE_THRESHOLD_DP = ViewConfiguration.get(myContext).getScaledTouchSlop();
```

Methods in `ViewConfiguration` starting with the `getScaled` prefix
are guaranteed to return a value in pixels that display properly regardless of the current
pixel density.

## Prefer vector graphics

An alternative to creating multiple density-specific versions of an image is to
create just one vector graphic. Vector graphics create an image using XML to
define paths and colors, instead of using pixel bitmaps. As such, vector
graphics can scale to any size without scaling artifacts, though they're usually
best for illustrations such as icons, not photographs.

Vector graphics are often provided as SVG (Scalable Vector Graphics) files,
but Android doesn't support this format so you must convert SVG files to
Android's [vector
drawable](https://developer.android.com/guide/topics/graphics/vector-drawable-resources) format.

You can convert an SVG to a vector drawable using Android Studio's
[Vector Asset Studio](https://developer.android.com/studio/write/vector-asset-studio)
as follows:

1. In the **Project** window, right-click the **res** directory and select **New \> Vector Asset**.
2. Select **Local file (SVG, PSD)**.
3. Locate the file you want to import and make any adjustments.

   ![An image showing how to import SVGs in Android Studio](https://developer.android.com/static/images/screens_support/import-svg_2x.png) **Figure 2**: Importing an SVG with Android Studio.

   You might notice some errors in the **Asset Studio** window
   indicating that vector drawables don't support some properties of the file.
   This doesn't prevent you from importing the file; the unsupported properties
   are ignored.
4. Click **Next**.

5. On the next screen, confirm the [source set](https://developer.android.com/studio/build#sourcesets) where you want the file in your project
   and click **Finish**.

   Because one vector drawable can be used on all pixel densities, this file
   goes in your default drawables directory, as shown in the following
   hierarchy. You don't need to use density-specific directories.  

   ```
   res/
     drawable/
       ic_android_launcher.xml
   ```

For more information about creating vector graphics, read the [vector drawable](https://developer.android.com/guide/topics/graphics/vector-drawable-resources)
documentation.

## Provide alternative bitmaps

To provide good graphical quality on devices with different pixel densities,
provide multiple versions of each bitmap in your app---one for each
density bucket, at a corresponding resolution. Otherwise, Android must scale
your bitmap so it occupies the same visible space on each screen, resulting in
scaling artifacts such as blurring.
![An image showing relative sizes for bitmaps at different density sizes](https://developer.android.com/static/images/screens_support/devices-density_2x.png) **Figure 3**: Relative sizes for bitmaps in different density buckets.

There are several density buckets available for use in your apps. Table 1
describes the different configuration qualifiers available and what screen types
they apply to.

**Table 1.** Configuration qualifiers for different
pixel densities.

| Density qualifier | Description |
|---|---|
| `ldpi` | Resources for low-density (*ldpi*) screens (\~120 dpi). |
| `mdpi` | Resources for medium-density (*mdpi*) screens (\~160 dpi). This is the baseline density. |
| `hdpi` | Resources for high-density (*hdpi*) screens (\~240 dpi). |
| `xhdpi` | Resources for extra-high-density (*xhdpi*) screens (\~320 dpi). |
| `xxhdpi` | Resources for extra-extra-high-density (*xxhdpi*) screens (\~480 dpi). |
| `xxxhdpi` | Resources for extra-extra-extra-high-density (*xxxhdpi*) uses (\~640 dpi). |
| `nodpi` | Resources for all densities. These are density-independent resources. The system doesn't scale resources tagged with this qualifier, regardless of the current screen's density. |
| `tvdpi` | Resources for screens somewhere between mdpi and hdpi; approximately \~213 dpi. This isn't considered a "primary" density group. It is mostly intended for televisions, and most apps don't need it---providing mdpi and hdpi resources is sufficient for most apps, and the system scales them as appropriate. If you find it necessary to provide `tvdpi` resources, size them at a factor of 1.33 \* mdpi. For example, a 100x100 pixel image for mdpi screens is 133x133 pixels for tvdpi. |

To create alternative bitmap drawables for different densities, follow the
3:4:6:8:12:16 scaling ratio between the six primary densities. For example, if you have
a bitmap drawable that's 48x48 pixels for medium-density screens, the sizes are:

- 36x36 (0.75x) for low density (ldpi)
- 48x48 (1.0x baseline) for medium density (mdpi)
- 72x72 (1.5x) for high density (hdpi)
- 96x96 (2.0x) for extra-high density (xhdpi)
- 144x144 (3.0x) for extra-extra-high density (xxhdpi)
- 192x192 (4.0x) for extra-extra-extra-high density (xxxhdpi)

Place the generated image files in the appropriate subdirectory
under `res/`:  

```
res/
  drawable-xxxhdpi/
    awesome_image.png
  drawable-xxhdpi/
    awesome_image.png
  drawable-xhdpi/
    awesome_image.png
  drawable-hdpi/
    awesome_image.png
  drawable-mdpi/
    awesome_image.png
```

Then, any time you reference `@drawable/awesomeimage`,
the system selects the appropriate bitmap based on the screen's dpi. If you
don't provide a density-specific resource for that density, the system locates
the next-best match and scales it to fit the screen.

**Tip:** If you have drawable resources
that you don't want the system to scale, such as when you're performing
some adjustments to the image yourself at runtime, place them in a
directory with the `nodpi` configuration qualifier.
Resources with this qualifier are considered density-agnostic, and
the system doesn't scale them.

For more information about other configuration qualifiers and
how Android selects the appropriate resources for
the current screen configuration, see the [App resources overview](https://developer.android.com/guide/topics/resources/providing-resources).

### Put app icons in mipmap directories

As with other bitmap assets, you need to provide density-specific versions of
your app icon. However, some app launchers display your app icon as much as 25%
larger than what's called for by the device's density bucket.

For example, if a device's density bucket is xxhdpi and the largest app icon you
provide is in `drawable-xxhdpi`, the app launcher scales up this icon,
which makes it appear less crisp.

To avoid this, put all
your app icons in `mipmap` directories instead of `drawable` directories. Unlike
`drawable` directories, all `mipmap` directories are retained in the APK, even
if you build density-specific APKs. This lets launcher apps pick the best
resolution icon to display on the home screen.  

```
res/
  mipmap-xxxhdpi/
    launcher_icon.png
  mipmap-xxhdpi/
    launcher_icon.png
  mipmap-xhdpi/
    launcher_icon.png
  mipmap-hdpi/
    launcher_icon.png
  mipmap-mdpi/
    launcher_icon.png
```

In the previous example of an xxhdpi device, you can provide a
higher-density launcher icon in the `mipmap-xxxhdpi` directory.

For icon design guidelines, see the [System icons](https://material.io/design/iconography/system-icons.html).

For help building app icons, see [Create app icons with Image Asset Studio](https://developer.android.com/studio/write/image-asset-studio).

## Advice for uncommon density issues

This section describes how Android performs scaling for bitmaps
on different pixel densities and how you can further control how
bitmaps are drawn on different densities. Unless your app manipulates graphics
or you have encountered problems when running on different pixel densities, you
can ignore this section.

To better understand how you can support multiple densities when manipulating graphics at
runtime, you need to know how the system helps ensure the proper scale for bitmaps.
This is done in the following ways:

1. *Pre-scaling of resources, such as bitmap drawables*

   Based on the density of the current screen, the system uses any density-specific
   resources from your app. If resources are not available in
   the correct density, the system loads the default resources and scales them up or down as needed. The system assumes that default resources (those from a
   directory without configuration qualifiers) are designed for the baseline
   pixel density (mdpi) and resizes those bitmaps to the appropriate size for
   the current pixel density.

   If you request the dimensions of a pre-scaled resource, the system returns values
   representing the dimensions *after* scaling. For example, a bitmap designed at 50x50 pixels
   for an mdpi screen is scaled to 75x75 pixels on an hdpi screen (if there is no alternative resource
   for hdpi), and the system reports the size as such.

   There are some situations in which you might not want Android to pre-scale
   a resource. The easiest way to avoid pre-scaling is to put the resource in a resource directory
   with the `nodpi` configuration qualifier. For example:  

   ```
   res/drawable-nodpi/icon.png
   ```

   When the system uses the `icon.png` bitmap from this folder, it doesn't scale it
   based on the current device density.
2. *Auto-scaling of pixel dimensions and coordinates*


   You can disable pre-scaling dimensions and images by setting [`android:anyDensity`](https://developer.android.com/guide/topics/manifest/supports-screens-element#any)
   to `"false"` in the manifest or programmatically for a [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap) by setting [inScaled](https://developer.android.com/reference/android/graphics/BitmapFactory.Options#inScaled) to `"false"`. In
   this case, the system auto-scales any absolute pixel coordinates and pixel
   dimension values at draw time. It does this to ensure that pixel-defined
   screen elements are still displayed at approximately the same physical size
   that they can be displayed at the baseline pixel density (mdpi). The system handles
   this scaling transparently to the app and reports the scaled pixel
   dimensions to the app, rather than physical pixel dimensions.

   For instance, suppose a device has a WVGA high-density screen, which is 480x800 and about the
   same size as a traditional HVGA screen---but it's running an app that has disabled
   pre-scaling. In this case, the system "lies" to the app when it queries for screen
   dimensions and reports 320x533, the approximate mdpi translation for the pixel density.

   Then, when
   the app does drawing operations, such as invalidating a rectangle from (10,10) to (100,
   100), the system transforms the coordinates by scaling them the appropriate amount, and actually
   invalidates the region (15,15) to (150, 150). This discrepancy might cause unexpected behavior if
   your app directly manipulates the scaled bitmap, but this is considered a reasonable
   trade-off to ensure the best possible app performance. If you encounter this
   situation, read [Convert dp units to pixel
   units](https://developer.android.com/training/multiscreen/screendensities#dips-pels).

   Usually, *you don't disable pre-scaling*. The best way to support multiple
   screens is to follow the basic techniques described on this page.

If your app manipulates bitmaps or directly interacts with pixels on the screen
in some other way, you might need to take additional steps to support different
pixel densities. For example, if you respond to touch gestures by counting the
number of pixels that a finger crosses, you need to use the appropriate
density-independent pixel values, instead of actual pixels, but you can
[convert between dp and px values](https://developer.android.com/training/multiscreen/screendensities#dips-pels).

## Test on all pixel densities

Test your app on multiple devices with different pixel
densities so you can ensure your UI scales correctly. Testing on a physical
device when possible; use the [Android
Emulator](https://developer.android.com/studio/run/emulator) if you don't have access to physical
devices for all the different pixel densities.

If you want to test on physical devices but
don't want to buy the devices, you can use [Firebase Test Lab](https://firebase.google.com/docs/test-lab/) to
access devices in a Google data center.

<br />