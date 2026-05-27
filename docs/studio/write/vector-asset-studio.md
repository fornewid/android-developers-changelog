---
title: https://developer.android.com/studio/write/vector-asset-studio
url: https://developer.android.com/studio/write/vector-asset-studio
source: md.txt
---

Android Studio includes a tool called Vector Asset Studio that helps you add
Material icons and import Scalable Vector Graphic (SVG) and Adobe Photoshop
Document (PSD) files into your project as vector drawable resources. Using
vector drawables instead of bitmaps reduces the size of your APK because the
same file can be resized for different screen densities without loss of image
quality. For earlier versions of Android that don't support vector drawables,
Vector Asset Studio can, at build time, turn your vector drawables into
different bitmap sizes for each screen density.
[Video](https://www.youtube.com/watch?v=8e3I-PYJNHg)

## About Vector Asset Studio

Vector Asset Studio adds a vector graphic to the project as an XML file that
describes the image. Maintaining one XML file can be easier than updating
multiple raster graphics at various resolutions.

To use vector drawables with Jetpack Compose, you must set the minimum API level
to Android 5.0 (API level 21) and higher.

Android 4.4 (API level 20) and lower doesn't support vector drawables. If your
minimum API level is set at one of these API levels, you have two options when
using Vector Asset Studio: generate Portable Network Graphic (PNG) files (the
default) or use the backward compatibility technique in AndroidX.

For backward compatibility, Vector Asset Studio generates raster images of the
vector drawable. The vector and raster drawables are packaged together in the
APK. You can refer to vector drawables as [`Drawable`](https://developer.android.com/reference/kotlin/android/graphics/drawable/Drawable) in Kotlin code or
`@drawable` in XML code; when your app runs, the corresponding vector
or raster image displays automatically depending on the API level.

If you want to use vector drawables only, you can use AndroidX 1.0.0 or
higher. This technique requires a change to your `build.gradle` file
before you run Vector Asset Studio, as described in [AndroidX](https://developer.android.com/studio/write/vector-asset-studio#androidx-backward-compatibility). The
[`VectorDrawableCompat`](https://developer.android.com/reference/kotlin/androidx/vectordrawable/graphics/drawable/VectorDrawableCompat) class in AndroidX lets you support
`VectorDrawable` in Android 2.1 (API level 7) and higher.

### Supported vector graphic types

The Google Material Design specification provides
[Material icons](https://m3.material.io/styles/icons/overview) that you can
use in your Android apps. Vector Asset Studio helps you choose, import, and
size Material icons, as well as define opacity and the Right-to-Left (RTL)
mirroring setting.

Vector Asset Studio also lets you import your own SVG and PSD files. SVG is an
XML-based open standard of the World Wide Web Consortium (W3C). The PSD file
format supports Adobe Photoshop features. Vector Asset Studio supports the
essential standards, but not all SVG and PSD features. When you specify an SVG
or PSD file, Vector Asset Studio gives immediate feedback about whether the
graphics code is supported or not. It converts the file into an XML file
containing [`VectorDrawable`](https://developer.android.com/reference/kotlin/android/graphics/drawable/VectorDrawable) code. If you receive errors, you should
verify that your vector drawable appears as intended. For more information
about allowed PSD features, see [Support and restrictions for PSD files](https://developer.android.com/studio/write/vector-asset-studio#PSD).

For Android 5.0 (API level 21) and higher, you can use the
[`AnimatedVectorDrawable`](https://developer.android.com/reference/kotlin/android/graphics/drawable/AnimatedVectorDrawable) class to animate the properties of the
[`VectorDrawable`](https://developer.android.com/reference/kotlin/android/graphics/drawable/VectorDrawable) class. With AndroidX, you can use the
[`AnimatedVectorDrawableCompat`](https://developer.android.com/reference/kotlin/androidx/vectordrawable/graphics/drawable/AnimatedVectorDrawableCompat) class to animate the `VectorDrawable` class
for Android 3.0 (API level 11) and higher. For more information, see
[Animated vector images in Compose](https://developer.android.com/develop/ui/compose/animation/vectors).

### Considerations for SVG and PSD files

A vector drawable is appropriate for simple icons. The
[Material icons](https://m3.material.io/styles/icons/overview) provide good examples of the types
of images that work well as vector drawables in an app. In contrast, many app
launch icons do have many details, so they work better as raster images.

The initial loading of a vector drawable can cost more CPU cycles than the
corresponding raster image. Afterward, memory use and performance are similar
between the two. We recommend that you limit a vector image to a maximum of
200 x 200 dp; otherwise, it can take too long to draw.

Although vector drawables do support one or more colors, in many cases it makes
sense to color icons black (`android:fillColor="#FF000000"`). Using this
approach, you can add a [tint](https://developer.android.com/develop/ui/compose/graphics/images/customize#tint-image) to the vector drawable that you placed in
a layout, and the icon color changes to the tint color. If the icon color
isn't black, the icon color might instead blend with the tint color.

### Vector drawable backward-compatibility solutions

The following table summarizes the two techniques that you can use for
backward compatibility:

| Technique | Drawables in APK | VectorDrawable XML elements | Version | Build flags | App code |
|---|---|---|---|---|---|
| **PNG generation** | Vector and raster | [Subset supported](https://developer.android.com/studio/write/vector-asset-studio#apilevel) | SVG: [Android plugin for Gradle](https://developer.android.com/studio/releases/gradle-plugin) 1.5.0 or higher PSD: Android Studio 2.2 or higher | Default | Variety of coding techniques supported |
| **AndroidX 1.0 or higher** | Vector | Full support | Android plugin for Gradle 3.2 or higher | Support Library statements required | [Subset of coding techniques supported](https://android-developers.blogspot.com/2016/02/android-support-library-232.html) |

Using vector drawables can produce a smaller APK, but the initial loading of
vector drawables can take longer.

#### PNG generation

Android 5.0 (API level 21) and higher provides vector drawable support. If your
app has a minimum API level that's lower, Vector Asset Studio adds the vector
drawable file to your project; also, at build time, Gradle creates PNG raster
images at various resolutions. Gradle generates the PNG densities specified by
the Domain Specific Language (DSL) [generatedDensities](https://google.github.io/android-gradle-dsl/3.4/com.android.build.gradle.internal.dsl.VectorDrawablesOptions.html#com.android.build.gradle.internal.dsl.VectorDrawablesOptions:generatedDensities) property
in a `build.gradle` file.

For Android 5.0 (API level 21) and higher, Vector Asset Studio supports all of
the [`VectorDrawable`](https://developer.android.com/reference/kotlin/android/graphics/drawable/VectorDrawable) elements. For backward compatibility with Android
4.4 (API level 20) and lower, Vector Asset Studio supports the following
XML elements:
`<vector>`

- `android:width`
- `android:height`
- `android:viewportWidth`
- `android:viewportHeight`
- `android:alpha`
`<group>`

- `android:rotation`
- `android:pivotX`
- `android:pivotY`
- `android:scaleX`
- `android:scaleY`
- `android:translateX`
- `android:translateY`
`<path>`

- `android:pathData`
- `android:fillColor`
- `android:strokeColor`
- `android:strokeWidth`
- `android:strokeAlpha`
- `android:fillAlpha`
- `android:strokeLineCap`
- `android:strokeLineJoin`
- `android:strokeMiterLimit`

<br />

<br />

You can change the XML code that Vector Asset Studio generates, although it's
not a best practice. Changing the values in the code shouldn't cause any
issues, as long as they're valid and static. If you want to add XML elements,
you need to make sure that they're supported based on your minimum API level.

#### AndroidX

This technique requires AndroidX 1.0 or higher and Android Plugin for Gradle
3.2 or higher, and uses vector drawables only. The [`VectorDrawableCompat`](https://developer.android.com/reference/kotlin/androidx/vectordrawable/graphics/drawable/VectorDrawableCompat)
class in AndroidX lets you support `VectorDrawable` in
Android 2.1 (API level 7) and higher.

Before using Vector Asset Studio, you must add a statement to your
`build.gradle` file:

### Kotlin

```kotlin
android {
    defaultConfig {
        vectorDrawables.useSupportLibrary = true
    }
}

dependencies {
    implementation("androidx.appcompat:appcompat:1.7.1")
}
```

### Groovy

```groovy
android {
    defaultConfig {
        vectorDrawables.useSupportLibrary = true
    }
}

dependencies {
    implementation 'androidx.appcompat:appcompat:1.7.1'
}
```

## Running Vector Asset Studio

To start Vector Asset Studio:

1. In Android Studio, open an Android app project.

2. In the *Project* window, select the [Android view](https://developer.android.com/studio/projects#ProjectFiles).

3. Right-click the **res** folder and select **New** \> **Vector Asset**.

   Some other project views and folders have this menu item as well.

   Vector Asset Studio appears.

   ![](https://developer.android.com/static/studio/images/write/vector-asset-studio-material-icon.png)

   **Figure 1**. Vector Asset Studio.

   <br />

4. If a *Need Newer Android Plugin for Gradle* dialog appears instead, correct
   your Gradle version as follows:

   1. Select **File** \> **Project Structure**.

   2. In the *Project Structure* dialog, select **Project**.

   3. In the **Android Plugin Version** field, change the Android Plugin for
      Gradle version to **1.5.0** or higher, and click **OK**.

      Gradle syncs the project.
   4. In the [Android view](https://developer.android.com/studio/projects#ProjectFiles)
      of the *Project* window, right-click the **res** folder and select
      **New** \> **Vector Asset**.

      Vector Asset Studio appears.
5. Continue with [Importing a Vector Graphic](https://developer.android.com/studio/write/vector-asset-studio#importing).

## Importing a vector graphic

Vector Asset Studio helps you to import a vector graphics file into your app
project. Follow one of the following procedures:

- [Adding a Material icon](https://developer.android.com/studio/write/vector-asset-studio#materialicon)
- [Importing an SVG or PSD file](https://developer.android.com/studio/write/vector-asset-studio#svg)

### Adding a Material icon

After you [open Vector Asset Studio](https://developer.android.com/studio/write/vector-asset-studio#running), you can add a Material icon as
follows:

1. In Vector Asset Studio, select **Clip art**.

2. In the Clip art field, click the button.

3. The **Select Icon** dialog appears. You can filter which icons are visible
   by selecting an icon category from the menu or typing in the
   search field as shown in figure 2.

   ![](https://developer.android.com/static/studio/images/write/vector-asset-studio-filtering.png)

   **Figure 2**. Filtering Material icons in the Vector Asset Studio.

   <br />

   Select a Material icon and click **OK** . The icon appears in the
   **Vector Drawable Preview**.
4. Optionally change the resource name, size, opacity, and Right-To-Left (RTL)
   mirroring setting:

   - **Name** - Type a new name if you don't want to use the default name.
     Vector Asset Studio automatically creates a unique name (adds a number
     to the end of the name) if that resource name already exists in the
     project. The name can contain lowercase characters, underscores, and
     digits only.

   - **Override** - Select this option if you
     want to adjust the size of the image. When you type a new size, the
     change appears in the preview area.

     The default is 24 x 24 dp, which is defined in the
     [Material design](https://m3.material.io/styles/icons/designing-icons#d2a5feec-5c85-4d22-906e-4ba139802be1) specification. Deselect the checkbox
     to return to the default.
   - **Opacity** - Use the slider to adjust the opacity of the image. The
     change appears in the preview area.

   - **Enable auto mirroring for RTL layout** - Select this option if you
     want a mirror image to display when the layout is right to left,
     instead of left to right. For example, some languages are read right
     to left; if you have an arrow icon, you might want to display a mirror
     image of it in this case. Note that if you're working with an older
     project, you might also need to add `android:supportsRtl="true"` to
     your app manifest. Auto-mirroring is supported on Android 5.0
     (API level 21) and higher, and with AndroidX.

5. Click **Next**.

6. Optionally change the module and resource directory:

   - **Res Directory** - Select the resource source set where you want to add the vector drawable: `src/main/res`, `src/debug/res`, `src/release/res`, or a user-defined source set. The main source set applies to all build variants, including debug and release. The debug and release source sets override the main source set and apply to one version of a build. The debug source set is for debugging only. To define a new source set, select **File** \> **Project Structure** \> **app** \> **Build Types** . For example, you could define a beta source set and create a version of an icon that includes the text "BETA" in the bottom right corner. For more information, see [Configure Build Variants](https://developer.android.com/studio/build/build-variants#workBuildVariants).

   The **Output Directories** area displays the vector drawable and the
   directory where it will appear.
7. Click **Finish**.

   Vector Asset Studio adds an XML file defining the vector drawable to the
   project in the `app/src/main/res/drawable/` folder. From the
   [Android view](https://developer.android.com/studio/projects#ProjectFiles) of the *Project* window, you can view the generated
   vector XML file in the **drawable** folder.
8. Build the project.

   If the minimum API level is Android 4.4 (API level 20) and lower, and you
   haven't enabled the AndroidX technique, Vector Asset Studio generates
   PNG files. From the [Project Files view](https://developer.android.com/studio/projects#ProjectFiles)
   of the *Project* window, you can view the generated PNG and XML files in the
   `app/build/generated/res/pngs/debug/` folder.

   You shouldn't edit these generated raster files, but instead work with the
   vector XML file. The build system regenerates the raster files automatically
   when needed so you don't need to maintain them.

### Importing an SVG or PSD file

After you [open Vector Asset Studio](https://developer.android.com/studio/write/vector-asset-studio#running), you can import an SVG or PSD file as
follows:

1. In Vector Asset Studio, select **Local file**.

   The file must be on a local drive. If it's located on the network, for
   example, you need to download it to a local drive first.
2. Specify an **Image file** by clicking **...** .

   The image appears in the **Vector Drawable Preview**.

   If the SVG or PSD file contains unsupported features, an error appears at
   the bottom of Vector Asset Studio, as shown in figure 3.

   ![](https://developer.android.com/static/studio/images/write/vector-asset-studio-error.png)

   **Figure 3**. Vector Asset Studio displaying some errors.

   <br />

   If you see errors, you need to make sure that the imported vector drawable
   renders properly. Scroll through the list to view the errors.

   For a list of supported elements, see
   [Vector Drawable Backward-Compatibility Solutions](https://developer.android.com/studio/write/vector-asset-studio#apilevel). For more information
   about allowed PSD files, see [Support and Restrictions for PSD Files](https://developer.android.com/studio/write/vector-asset-studio#PSD).
3. Optionally change the resource name, size, opacity, and Right-To-Left (RTL)
   mirroring setting:

   - **Name** - Type a new name if you don't want to use the default name.
     Vector Asset Studio automatically creates a unique name (adds a number
     to the end of the name) if that resource name already exists in the
     project. The name can contain lowercase characters, underscores, and
     digits only.

   - **Override** - Select this option if you want to adjust the size of the
     image. After you select it, the size changes to the size of the image
     itself. Whenever you change the size, the change appears in the preview
     area. The default is 24 x 24 dp, which is defined in the
     [Material design](https://m3.material.io/styles/icons/designing-icons#d2a5feec-5c85-4d22-906e-4ba139802be1) specification.

   - **Opacity** - Use the slider to adjust the opacity of the image. The
     change appears in the preview area.

   - **Enable auto mirroring for RTL layout** - Select this option if you
     want a mirror image to display when the layout is right to left,
     instead of left to right. For example, some languages are read right to
     left; if you have an arrow icon, you might want to display a mirror
     image of it in this case. Note that if you're working with an older
     project, you might need to add `android:supportsRtl="true"` to your app
     manifest. Auto-mirroring is supported by Android 5.0 (API level 21)
     and higher, and AndroidX.

4. Click **Next**.

5. Optionally change the resource directory:

   - **Res Directory** - Select the resource source set where you want to add the vector drawable: `src/main/res`, `src/debug/res`, `src/release/res`, or a user-defined source set. The main source set applies to all build variants, including debug and release. The debug and release source sets override the main source set and apply to one version of a build. The debug source set is for debugging only. To define a new source set, select **File** \> **Project Structure** \> **app** \> **Build Types** . For example, you could define a beta source set and create a version of an icon that includes the text "BETA" in the bottom right corner. For more information, see [Configure Build Variants](https://developer.android.com/studio/build/build-variants#workBuildVariants).

   The **Output Directories** area displays the vector drawable and the
   directory where it will appear.
6. Click **Finish**.

   Vector Asset Studio adds an XML file defining the vector drawable to the
   project in the `app/src/main/res/drawable/` folder. From the
   [Android view](https://developer.android.com/studio/projects#ProjectFiles) of the *Project* window, you can view the generated
   vector XML file in the **drawable** folder.
7. Build the project.

   If the minimum API level is Android 4.4 (API level 20) and lower, and you
   haven't enabled the AndroidX technique, Vector Asset Studio generates
   PNG files. From the [Project Files view](https://developer.android.com/studio/projects#ProjectFiles)
   of the *Project* window, you can view the generated PNG and XML files in the
   `app/build/generated/res/pngs/debug/` folder.

   You shouldn't edit these generated raster files, but instead work with the
   vector XML file. The build system regenerates the raster files automatically
   when needed so you don't need to maintain them.

## Referencing a vector asset in Jetpack Compose

After you have used Vector Asset Studio to add an asset to your `res/drawable`
folder, you can reference it in your code.

In Jetpack Compose, the most common way to display your vector is using the
`Icon` or `Image` composable.

The `Icon` composable is the standard way to display small, monochromatic
assets. It provides built-in support for Material Design principles, such as
applying dynamic tinting based on Material 3 themes and automatic accessibility
through content descriptions.

Use the `painterResource` API to provide XML vector assets to the composable:

```kotlin
Icon(
    painter = painterResource(id = R.drawable.ic_speedometer),
    tint = MaterialTheme.colorScheme.primary, // Applies dynamic theme color
    contentDescription = "Current Speed", // Essential for accessibility
)
```

For complex and multicolor vectors, use the `Image` composable:

```kotlin
Image(
     painter = painterResource(id = R.drawable.ic_complex_vector),
     contentDescription = null // Decorative element
)
```

For other complex scenarios, such as customizing an image or optimizing
performance, see [Working with images](https://developer.android.com/develop/ui/compose/graphics/images).
For animating vectors, see [Animated vector images in Compose](https://developer.android.com/develop/ui/compose/animation/vectors).

## Modifying XML code generated by Vector Asset Studio

You can modify the vector drawable XML code, but not the PNGs and corresponding
XML code generated at build time. However, we don't recommend it.

When using the PNG generation technique, Vector Asset Studio makes sure that
the vector drawable and the PNGs match, and that the manifest contains the
proper code. If you add code that's [not supported](https://developer.android.com/studio/write/vector-asset-studio#apilevel) on Android 4.4
(API level 20) and lower, your vector and PNG images might differ. You also
need to make sure that the manifest contains the code to support your changes.

To modify the vector XML file when you're not using the AndroidX
technique:

1. In the *Project* window, double-click the generated vector XML file in the
   **drawable** folder.

   The XML file appears in the editor and *Preview* windows.

   ![](https://developer.android.com/static/studio/images/write/vector-asset-studio-drawable-preview.png)

   **Figure 4**. A vector XML file displayed in the Code Editor and the Preview window.

   <br />

2. Edit the XML code based on what's supported by the minimum API level:

   - Android 5.0 (API level 21) and higher - Vector Asset Studio supports all
     of the [`Drawable`](https://developer.android.com/reference/kotlin/android/graphics/drawable/Drawable) and [`VectorDrawable`](https://developer.android.com/reference/kotlin/android/graphics/drawable/VectorDrawable) elements. You can add XML
     elements and change values. For Jetpack Compose, you can load the vector
     drawable into [`ImageVector`](https://developer.android.com/develop/ui/compose/graphics/images/compare#image-vector) for further customization.

   - Android 4.4 (API level 20) and lower - Vector Asset Studio supports all of
     the [`Drawable`](https://developer.android.com/reference/kotlin/android/graphics/drawable/Drawable) elements and a subset of the [`VectorDrawable`](https://developer.android.com/reference/kotlin/android/graphics/drawable/VectorDrawable)
     elements. See [Vector Drawable Backward-Compatibility Solutions](https://developer.android.com/studio/write/vector-asset-studio#apilevel) for
     a list. You can change values in the generated code and add XML elements
     that are supported.

3. Build the project and check that the vector drawable and corresponding
   raster images look the same.

   Remember that the generated PNGs could display differently in the *Preview*
   window than in the app due to different rendering engines and any changes
   made to the vector drawable before a build. If you add code to the vector
   XML file created by Vector Asset Studio, any features unsupported in Android
   4.4 (API level 20) and lower don't appear in the generated PNG files. As a
   result, when you add code, you should always check that the generated PNGs
   match the vector drawable. To do so, you could double-click the PNG in the
   [Project Files view](https://developer.android.com/studio/projects#ProjectFiles) of the *Project*
   window; the left margin of the Code Editor also displays the PNG image when
   your code refers to the drawable, as shown in figure 5.

   ![](https://developer.android.com/static/studio/images/write/vector-asset-studio-code-editor-drawable-preview.png)

   **Figure 5**. A PNG image displayed in the left margin of the Code Editor.

   <br />

## Deleting a vector drawable from a project

To remove a vector drawable from a project:

1. In the *Project* window, delete the generated vector XML file by selecting
   the file and pressing the **Delete** key (or select **Edit** \> **Delete**).

   The *Safe Delete* dialog appears.
2. Optionally select options to find where the file is used in the project, and
   click **OK**.

   Android Studio deletes the file from the project and the drive. However, if
   you chose to search for places in the project where the file is used and
   some usages are found, you can view them and decide whether to delete
   the file.
3. Select **Build** \> **Clean Project**.

   Any auto-generated PNG and XML files corresponding to the deleted vector
   drawable are removed from the project and the drive.

## Delivering an app containing vector drawables

If you used the AndroidX technique or your minimum API level is
Android 5.0 (API level 21) or higher, your APK will contain the vector drawables
that you added with Vector Asset Studio.
These APKs will be smaller than if the vector images were converted to PNGs.

When your minimum API level includes Android 4.4 (API level 20) or lower,
and you have corresponding vector drawables and raster images in your project,
you have two options for delivering your APK files:

- Create one APK that includes both the vector drawables and the corresponding raster representations. This solution is the simplest to implement.
- Create separate APKs for different API levels. When you don't include the corresponding raster images in the APK for Android 5.0 (API level 21) and higher, the APK can be much smaller in size. For more information, see [Multiple APK Support](https://developer.android.com/google/play/publishing/multiple-apks).

## Support and restrictions for PSD files

Vector Asset Studio doesn't support all PSD file features. The following list
summarizes supported and unsupported PSD characteristics, as well as some
conversion details.

#### Document

Supported:

- A PSD color mode of bitmap, grayscale, indexed, RGB, Lab, or CMYK.
- A color depth of 8, 16, or 32 bits.

Conversion details:

- PSD document dimensions become the vector drawable and viewport dimensions.

Not supported:

- A PSD color mode of duotone or multichannel.

#### Shapes

Supported:

- Clipping masks, if the clipping base is another shape.
- Shape operations, including merge/add, intersect, subtract, and exclude.

Not supported:

- Even-odd fill rule used by Photoshop shapes. In Android 6.0 (API level 23)
  and lower, vector drawables support the nonzero fill rule only. In
  self-intersecting shapes, this limitation can lead to rendering differences
  between the PSD and the resulting vector drawable. To fix this issue, add
  `android:fillType="evenOdd"` on the shape in the vector drawable. For
  example:

  ```xml
  <vector xmlns:android="https://schemas.android.com/apk/res/android"
    android:viewportHeight="168"
    android:height="24dp"
    android:viewportWidth="209"
    android:width="24dp">

    <path
        android:fillAlpha="1.0"
        android:fillColor="#000000"
        android:fillType="evenOdd"
        android:pathData="M24,58 L24,167 L114,167 L114,66 M64,1 L64,96 L208,96 L208,8 M1,97 L146,139 L172,47"/>
  </vector>
  ```

#### Strokes and fills

Supported:

- Strokes, including color, opacity, width, join, cap, dashes, and alignment.
- Solid color fills and strokes.
- Stroke and fill colors specified as RGB, Lab, or CMYK.

Conversion details:

- If a stroke is dashed, clipped using a clipping base, or uses an alignment different from center, Vector Asset Studio converts it into a fill shape in the vector drawable.

Not supported:

- Color fills and strokes other than solid, such as gradients.

#### Opacity

Supported:

- Shape layers with an opacity of 0.

Conversion details:

- Vector Asset Studio multiplies the fill opacity with the layer opacity to compute the fill alpha.
- The tool multiplies the opacity of the clipping base (if there is a clipping base) with the fill alpha to compute the final fill alpha.
- The tool multiplies the stroke opacity with the layer opacity to compute the stroke alpha.
- The tool multiplies the opacity of the clipping base (if there is a clipping base) with the stroke alpha to compute the final stroke alpha.

#### Layers

Supported:

- Any *visible* shape layer.

Conversion details:

- Vector Asset Studio preserves the names of the layers in the vector drawable file.

Not supported:

- Layer effects.
- Adjustment and text layers.
- Blending modes (ignored).

## Support and restrictions for SVG files

Vector Asset Studio doesn't support all SVG file features. The following section
summarizes supported and unsupported features when the tool converts an SVG file
to a [`VectorDrawable`](https://developer.android.com/reference/kotlin/android/graphics/drawable/VectorDrawable),
along with additional conversion details.

### Supported features

`VectorDrawable` supports all features from [Tiny SVG 1.2](https://www.w3.org/TR/SVGTiny12/)
except for [text](https://www.w3.org/TR/SVGTiny12/text.html).

#### Shapes

`VectorDrawable` supports [SVG paths](https://www.w3.org/TR/SVG/paths.html#DAttribute).

The tool converts primitive [shapes](https://www.w3.org/TR/SVG/shapes.html) such
as circles, squares, and polygons to paths.

#### Transformations

The tool supports transformation matrices and applies them directly to child
paths.

#### Groups

The tool supports group elements for translation, scaling, and rotation. Groups
don't support an opacity property.

The tool also applies any group styling or opacity to child paths.

#### Fills and strokes

Paths can be filled and stroked using solid colors or gradients (linear, radial,
or angular). Only centered strokes are supported. Blend modes are not supported.
Dashed paths are not supported.

#### Masks

The tool supports one clipping mask per group.

### Features not supported by the SVG importer

Any feature not listed in the earlier [Supported features](https://developer.android.com/studio/write/vector-asset-studio#svg-supported) section is
unsupported. Notable unsupported features include the following:

- Filter effects: effects such as drop shadows, blurs, and color matrix are not supported.
- Text: conversion of text to shapes using other tools is recommended.
- Pattern fills

## Additional resources

For more information about vector graphics, see the following additional
resources:

### Documentation

- [Animated vector images in Compose](https://developer.android.com/develop/ui/compose/animation/vectors)
- [Working with images](https://developer.android.com/develop/ui/compose/graphics/images)

### Views content

- [Add multi-density vector graphics (Views)](https://developer.android.com/studio/views/vector-asset-studio-views)