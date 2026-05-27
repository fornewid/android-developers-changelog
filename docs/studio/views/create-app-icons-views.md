---
title: https://developer.android.com/studio/views/create-app-icons-views
url: https://developer.android.com/studio/views/create-app-icons-views
source: md.txt
---

[Jetpack Compose implementation](https://developer.android.com/studio/write/create-app-icons)

This page includes information about creating and using app icons that is
unique to View-based layouts. For more comprehensive information about creating
app icons, see [Create app icons](https://developer.android.com/studio/write/create-app-icons), which covers our
recommended UI framework.

## Create an action bar or tab icon

Use [Image Asset Studio](https://developer.android.com/studio/write/create-app-icons#about) to create action bar and tab
icons for View-based layouts.

Action bar icons are graphical elements placed in the action bar and that
represent individual action items. See [Adding and Handling
Actions](https://developer.android.com/training/appbar/actions), [App Bar - Material Design](https://material.google.com/layout/structure.html#structure-app-bar)
{:.external}, and [Action Bar Design](https://developer.android.com/design/patterns/actionbar) for more information.

Tab icons are graphical elements used to represent individual tabs in a
multi-tab interface. Each tab icon has two states: unselected and selected. See
[Creating Swipe Views with Tabs](https://developer.android.com/training/implementing-navigation/lateral) and [Tabs - Material
Design](https://material.google.com/components/tabs.html) for more information.

Image Asset Studio places the icons in the proper locations in the
`res/drawable-<density>/` directories.

We recommend that you use the material design style for action bar and tab
icons, even if you support older Android versions. Use `appcompat` and other
[support libraries](https://developer.android.com/topic/libraries/support-library) to deliver your material design UI to
older platform versions.

As an alternative to Image Asset Studio, you can use [Vector Asset
Studio](https://developer.android.com/studio/write/vector-asset-studio) to create action bar and tab icons. Vector
drawables are appropriate for simple icons and can reduce the size of your app.

After you [open Image Asset Studio](https://developer.android.com/studio/write/create-app-icons#access), you can add an
action bar or tab icon by following these steps:

1. In the **Icon Type** field, select **Action Bar and Tab Icons**.
2. Select an **Asset Type**, and then specify the asset in the field
   underneath:

   - In the **Clip Art** field, click the button.

     In the **Select Icon** dialog, select a [material
     icon](https://design.google.com/icons) and then click **OK**.
   - In the **Path** field, specify the path and file name of the image.
     Click **...** to use a dialog.

   - In the **Text** field, type a text string and select a font.

   The icon appears in the **Source Asset** area on the right side, and in the
   preview area at the bottom of the wizard.
3. Optionally change the name and display options:

   - **Name** - If you don't want to use the default name, type a new name.
     If that resource name already exists in the project, as indicated by an
     error at the bottom of the wizard, it's overwritten. The name can
     contain lowercase characters, underscores, and digits only.

   - **Trim** - To adjust the margin between the icon graphic and border in
     the source asset, select **Yes** . This operation removes transparent
     space, while preserving the aspect ratio. To leave the source asset
     unchanged, select **No**.

   - **Padding** - If you want to adjust the source asset padding on all
     four sides, move the slider. Select a value between -10% and 50%. If
     you also select **Trim**, the trimming happens first.

   - **Theme** - Select **[HOLO_LIGHT](https://developer.android.com/guide/topics/ui/themes#SelectATheme)** or **HOLO_DARK** . Or, to
     specify a color in the **Select Color** dialog, select **CUSTOM** and
     then click the **Custom color** field.

   Image Asset Studio creates the icon within a transparent square so there's
   some padding on the edges. The padding provides adequate space for the
   standard drop-shadow icon effect.
4. Click **Next**.

5. Optionally change the resource directory:

   - **Res Directory** - Select the resource source set where you want to add the image asset: **src/main/res** , **src/debug/res** , **src/release/res** , or a user-defined source set. The main source set applies to all build variants, including debug and release. The debug and release source sets override the main source set and apply to one version of a build. The debug source set is for debugging only. To define a new source set, select **File** \> **Project Structure** \> **app** \> **Build Types** . For example, you could define a beta source set and create a version of an icon that includes the text "BETA" in the bottom right corner. For more information, see [Configure Build
     Variants](https://developer.android.com/studio/build/build-variants#workBuildVariants).

   The **Output Directories** area displays the images and the folders where
   they will appear in [Project Files view](https://developer.android.com/studio/projects#ProjectFiles) of the
   **Project** window.
6. Click **Finish**.

   Image Asset Studio adds the images in the **drawable** folders for the
   different densities.

## Refer to an image resource in code

> [!NOTE]
> **Note:** For information about referring to launcher icons in your code, see the [Compose launcher icon guidance](https://developer.android.com/studio/write/create-app-icons#material-icons-compose), which applies to Views too.

You can normally refer to an image resource in a generic way in your code, and
when your app runs, the corresponding image displays automatically depending on
the device:

- In most cases, you can refer to image resources as `@drawable` in XML code
  or [`Drawable`](https://developer.android.com/reference/android/graphics/drawable/Drawable) in Java code.

  For example, the following layout XML code displays the drawable in an
  [`ImageView`](https://developer.android.com/reference/android/widget/ImageView):

      <ImageView
          android:layout_height="wrap_content"
          android:layout_width="wrap_content"
          android:src="@drawable/myimage" />

  The following Java code retrieves the image as a
  [`Drawable`](https://developer.android.com/reference/android/graphics/drawable/Drawable):

  ### Kotlin

  ```kotlin
  val drawable = resources.getDrawable(R.drawable.myimage, theme)
  ```

  ### Java

  ```java
  Resources res = getResources();
  Drawable drawable = res.getDrawable(R.drawable.myimage, getTheme());
  ```

  The [`getResources()`](https://developer.android.com/reference/android/content/Context#getResources()) method resides in the
  [`Context`](https://developer.android.com/reference/android/content/Context) class, which applies to UI objects, such as
  activities, fragments, layouts, views, and so on.
- If your app uses the Support Library, you can refer to an image resource in
  XML code with an `app:srcCompat` statement. For example:

      <ImageView
          android:layout_height="wrap_content"
          android:layout_width="wrap_content"
          app:srcCompat="@drawable/myimage" />

You can access image resources from the main thread only.

After you have an image resource in the `res/` directory of your project, you
can reference it from your Java code or your XML layout using its resource ID.
The following Java code sets an [`ImageView`](https://developer.android.com/reference/android/widget/ImageView) to use the
`drawable/myimage.png` resource:

### Kotlin

```kotlin
findViewById<ImageView>(R.id.myimageview).apply {
    setImageResource(R.drawable.myimage)
}
```

### Java

```java
ImageView imageView = (ImageView) findViewById(R.id.myimageview);
imageView.setImageResource(R.drawable.myimage);
```

See [Access your app resources](https://developer.android.com/guide/topics/resources/accessing-resources#ResourcesFromCode) for more information.