---
title: https://developer.android.com/studio/write/create-app-icons
url: https://developer.android.com/studio/write/create-app-icons
source: md.txt
---

Icons help your users identify your app and actions within it. You can access the suite of
Material icons and add them to your app directly with Compose. To create custom icons or icons for
your app with Views, Android Studio offers Image Asset Studio.

## Add icons within your app with Compose

With Compose, you can import the
[Compose Material library](https://developer.android.com/jetpack/androidx/releases/compose-material) or
[Compose Material 3 library](https://developer.android.com/jetpack/androidx/releases/compose-material3) to access
any Material icons. Then use the `Icon` composable to add icons to your app. The
Material icons are most useful for action bar icons, tab icons, or notification icons. For more
information, see
[Material icons](https://developer.android.com/jetpack/compose/graphics/images/material).

If you need to create custom icons, for example your app launcher icon, use
[Image Asset Studio](https://developer.android.com/studio/write/create-app-icons#about). For launcher icons, the `AndroidManifest.xml`
file must reference the `mipmap/` location. Image Asset Studio adds this code
automatically. The following manifest file code references the
`ic_launcher` icon in the `mipmap/` directory:  

```xml
  <application android:name="ApplicationTitle"
            android:label="@string/app_label"
            android:icon="@mipmap/ic_launcher" >
  
```

## About Image Asset Studio

Android Studio includes a tool called Image Asset Studio that helps you generate your own app
icons from
[material icons](https://design.google.com/icons/),
custom images, and text strings. It generates a set of icons at the appropriate resolution
for each [pixel
density](https://developer.android.com/training/multiscreen/screendensities) that your app supports.
Image Asset Studio places the newly generated icons in density-specific folders under the
`res/` directory in your project. At runtime, Android uses the appropriate
resource based on the screen density of the device your app is running on.

Image Asset Studio helps you generate the following icon types:

- Launcher icons
- Action bar and tab icons
- Notification icons

The following sections describe the icon types that you can create and the image and text inputs
that you can use.

### Adaptive and legacy launcher icons

A launcher icon is a graphic that represents your app to users. It can:

- Appear in the list of apps installed on a device and on the Home screen.
- Represent shortcuts into your app (for example, a contact shortcut icon that opens detail information for a contact).
- Be used by launcher apps.
- Help users find your app on Google Play.

Adaptive launcher icons can display as a variety of shapes across different device models and are
available in Android 8.0 (API level 26) and higher. Android Studio 3.0 introduces support for
creating adaptive icons using Image Asset Studio. Image Asset Studio generates previews of an
adaptive icon in circle, squircle, rounded square, and square shapes, as well as a full bleed
preview of the icon. Image Asset Studio also generates legacy, round, and Google Play Store
previews of the icon. A legacy launcher icon is a graphic that represents your app on a device's
home screen and in the launcher window. Legacy launcher icons are intended for use on devices
running Android 7.1 (API level 25) or lower, which don't support adaptive icons, and don't display
as varying shapes across device models.

Image Asset Studio places the icons in the proper locations in the
`res/mipmap-`<var translate="no">density</var>`/` directories. It also creates a 512 x 512 pixel image
that's appropriate for the Google Play store.

We recommend that you use the material design style for launcher icons,
even if you support older Android versions.

See [Adaptive Launcher Icons](https://developer.android.com/guide/practices/ui_guidelines/icon_design_adaptive) and
[Product Icons - Material Design](https://material.io/design/iconography/product-icons.html) for more information.

### Action bar and tab icons

Action bar icons are graphical elements placed in the action bar and that represent individual
action items. See [Adding and Handling Actions](https://developer.android.com/training/appbar/actions),
[App Bar - Material Design](https://material.google.com/layout/structure.html#structure-app-bar), and
[Action Bar Design](https://developer.android.com/design/patterns/actionbar)
for more information.

Tab icons are graphical elements used to represent individual tabs in a
multi-tab interface. Each tab icon has two states: unselected and selected.
See [Creating Swipe Views with Tabs](https://developer.android.com/training/implementing-navigation/lateral) and
[Tabs - Material Design](https://material.google.com/components/tabs.html)
for more information.

Image Asset Studio places the icons in the proper locations in the
`res/drawable-`<var translate="no">density</var>`/`
directories.

We recommend that you use the material design style for action bar
and tab icons, even if you support older Android versions. Use `appcompat` and other
[support libraries](https://developer.android.com/topic/libraries/support-library)
to deliver your material design UI to older platform versions.

As an alternative to Image Asset Studio, you can use
[Vector Asset Studio](https://developer.android.com/studio/write/vector-asset-studio) to create action bar and
tab icons. Vector drawables are appropriate for simple icons and can reduce the size of your
app.

### Notification icons

A notification is a message that you can display to the user outside of the normal UI of your
app. Image Asset Studio places notifications icons in the proper locations in the
`res/drawable-`<var translate="no">density</var>`/` directories:

- Icons for Android 2.2 (API level 8) and lower are placed in `res/drawable-`<var translate="no">density</var>`/` directories.
- Icons for Android 2.3 to 2.3.7 (API level 9 to 10) are placed in `res/drawable-`<var translate="no">density</var>`-v9/` directories.
- Icons for Android 3 (API level 11) and higher are placed in `res/drawable-`<var translate="no">density</var>`-v11/` directories.

If your app supports Android 2.3 to 2.3.7 (API level 9 to 10), Image Asset Studio generates a
gray version of your icon. Later Android versions use the white icon that Image Asset Studio
generates.

See [Notifications](https://developer.android.com/guide/topics/ui/notifiers/notifications);
[Notifications Material Design](https://material.io/design/platform-guidance/android-notifications);
[Notifications, Android 5.0 Changes](https://developer.android.com/about/versions/lollipop#Notifications);
[Notifications, Android 4.4 and Lower](https://developer.android.com/design/patterns/notifications_k); and
[Status Bar Icons, Android 3.0 and Lower](https://developer.android.com/guide/practices/ui_guidelines/icon_design_status_bar)
for more information.

### Clip art

Image Asset Studio makes it easy for you to import Google material icons in VectorDrawable and
PNG formats: simply select an icon from a dialog. For more information, see
[Material Icons](https://fonts.google.com/icons).

### Images

You can import your own images and adjust them for the icon type. Image Asset Studio supports
the following file types: PNG (preferred), JPG (acceptable), and GIF (discouraged).

### Text strings

Image Asset Studio lets you type a text string in a variety of fonts, and places it on an icon.
It converts the text-based icon into PNG files for different densities. You can use the fonts that
are installed on your computer.

## Run Image Asset Studio

To start Image Asset Studio, follow these steps:

1. In the **Project** window, select the [Android view](https://developer.android.com/studio/projects#ProjectFiles).
2. Right-click the **res** folder and select **New** \> **Image Asset** .

   ![The adaptive and legacy icon wizard in Image Asset Studio.](https://developer.android.com/static/studio/images/write/new-image-asset-studio.png)
3. Continue by following the steps to:
   - Create [adaptive and legacy launcher icons](https://developer.android.com/studio/write/create-app-icons#create-adaptive).
   - Create an [action bar or tab icon](https://developer.android.com/studio/write/create-app-icons#create-actionbartab).
   - Create a [notification icon](https://developer.android.com/studio/write/create-app-icons#create-notification).

## Create adaptive and legacy launcher icons

After you [open Image Asset Studio](https://developer.android.com/studio/write/create-app-icons#access), you can add adaptive and legacy icons by
following these steps:

1. In the **Icon Type** field, select **Launcher Icons (Adaptive and
   Legacy)**.
2. In the **Foreground Layer** tab, select an **Asset Type** , and then specify the asset in the field underneath:
   - Select **Image** to specify the path for an image file.
   - Select **Clip Art** to specify an image from the [material design icon set](https://design.google.com/icons).
   - Select **Text** to specify a text string and select a font.
3. In the **Background Layer** tab, select an **Asset Type**, and then specify the asset in the field underneath. You can either select a color or specify an image to use as the background layer.
4. In the **Monochrome Layer** tab, select an **Asset Type** (**Image** , **Clip Art** , or **Text**), or let Android Studio default to reusing the same asset as the foreground layer.
5. In the **Options** tab, review the default settings and confirm you want to generate legacy, round, and Google Play Store icons.
6. Optionally change the name and display settings for each of the **Foreground Layer** and **Background Layer** tabs:
   - **Name** - If you don't want to use the default name, type a new name. If that resource name already exists in the project, as indicated by an error at the bottom of the wizard, it's overwritten. The name can contain lowercase characters, underscores, and digits only.
   - **Trim** - To adjust the margin between the icon graphic and border in the source asset, select **Yes** . This operation removes transparent space, while preserving the aspect ratio. To leave the source asset unchanged, select **No**.
   - **Color** - To change the color for a **Clip Art** or **Text** icon, click the field. In the **Select Color** dialog, specify a color and then click **Choose**. The new value appears in the field.
   - **Resize** - Use the slider to specify a scaling factor in percent to resize an **Image** , **Clip Art** , or **Text** icon. This control is disabled for the background layer when you specify a **Color** asset type.
7. Click **Next**.
8. Optionally, change the resource directory: Select the resource source set where you want to add the image asset: **src/main/res** , **src/debug/res** , **src/release/res** , or a custom source set. The main source set applies to all build variants, including debug and release. The debug and release source sets override the main source set and apply to one version of a build. The debug source set is for debugging only. To define a new source set, select **File** \> **Project Structure** \> **app** \> **Build Types** . For example, you can define a beta source set and create a version of an icon that includes the text "BETA" in the bottom right corner. For more information, see [Configure
   Build Variants](https://developer.android.com/studio/build/build-variants#workBuildVariants).
9. Click **Finish** . Image Asset Studio adds the images to the **mipmap** folders for the different densities.

### Preview themed app icons

Android Studio lets you preview
your [themed app icon](https://developer.android.com/about/versions/13/features#themed-app-icons)
and test how it adapts to the coloring of the user's wallpaper. To preview your themed app
icon, open the `launcher.xml` file that defines your icon and then use the
**System UI Mode** selector on the toolbar to switch wallpapers and see how the icon reacts.

To learn more about how to create themed app icons, see
[Adaptive icons](https://developer.android.com/develop/ui/views/launch/icon_design_adaptive).
![](https://developer.android.com/static/studio/images/system-ui-mode-selector.png) **System UI Mode** selector.   
![](https://developer.android.com/static/studio/images/preview-themed-app-icons.gif) Preview themed app icons across different wallpapers.

## Create an action bar or tab icon

After you [open Image Asset Studio](https://developer.android.com/studio/write/create-app-icons#access), you can add an action bar or tab icon
by following these steps:

1. In the **Icon Type** field, select **Action Bar and Tab Icons**.
2. Select an **Asset Type**, and then specify the asset in the field underneath:
   - In the **Clip Art** field, click the button.
   - In the **Select Icon** dialog, select a [material icon](https://design.google.com/icons) and then click **OK**.
   - In the **Path** field, specify the path and file name of the image. Click **...** to use a dialog.
   - In the **Text** field, type a text string and select a font.
3. The icon appears in the **Source Asset** area on the right side, and in the preview area at the bottom of the wizard.
4. Optionally change the name and display options:
   - **Name** - If you don't want to use the default name, type a new name. If that resource name already exists in the project, as indicated by an error at the bottom of the wizard, it's overwritten. The name can contain lowercase characters, underscores, and digits only.
   - **Trim** - To adjust the margin between the icon graphic and border in the source asset, select **Yes** . This operation removes transparent space, while preserving the aspect ratio. To leave the source asset unchanged, select **No**.
   - **Padding** - If you want to adjust the source asset padding on all four sides, move the slider. Select a value between -10% and 50%. If you also select **Trim**, the trimming happens first.
   - **Theme** - Select **[HOLO_LIGHT](https://developer.android.com/guide/topics/ui/themes#SelectATheme)** or **HOLO_DARK** . Or, to specify a color in the **Select Color** dialog, select **CUSTOM** and then click the **Custom color** field.

   Image Asset Studio creates the icon within a transparent square so there's some padding
   on the edges. The padding provides adequate space for the standard drop-shadow icon effect.
5. Click **Next**.
6. Optionally change the resource directory:
   - **Res Directory** - Select the resource source set where you want to add the image asset: **src/main/res** , **src/debug/res** , **src/release/res** , or a user-defined source set. The main source set applies to all build variants, including debug and release. The debug and release source sets override the main source set and apply to one version of a build. The debug source set is for debugging only. To define a new source set, select **File** \> **Project Structure** \> **app** \> **Build Types** . For example, you could define a beta source set and create a version of an icon that includes the text "BETA" in the bottom right corner. For more information, see [Configure Build Variants](https://developer.android.com/studio/build/build-variants#workBuildVariants).
7. The **Output Directories** area displays the images and the folders where they will appear in [Project Files view](https://developer.android.com/studio/projects#ProjectFiles) of the **Project** window.
8. Click **Finish**.
9. Image Asset Studio adds the images in the **drawable** folders for the different densities.

## Create a notification icon

After you [open Image Asset Studio](https://developer.android.com/studio/write/create-app-icons#access), you can add a notification icon
by following these steps:

1. In the **Icon Type** field, select **Notification Icons**.
2. Select an **Asset Type**, and then specify the asset in the field underneath:
   - In the **Clip Art** field, click the button.
   - In the **Select Icon** dialog, select a [material icon](https://design.google.com/icons) and then click **OK**.
   - In the **Path** field, specify the path and file name of the image. Click **...** to use a dialog.
   - In the **Text** field, type a text string and select a font.
3. The icon appears in the **Source Asset** area on the right side, and in the preview area at the bottom of the wizard.
4. Optionally change the name and display options:
   - **Name** - If you don't want to use the default name, type a new name. If that resource name already exists in the project, as indicated by an error at the bottom of the wizard, it's overwritten. The name can contain lowercase characters, underscores, and digits only.
   - **Trim** - To adjust the margin between the icon graphic and border in the source asset, select **Yes** . This operation removes transparent space, while preserving the aspect ratio. To leave the source asset unchanged, select **No**.
   - **Padding** - If you want to adjust the source asset padding on all four sides, move the slider. Select a value between -10% and 50%. If you also select **Trim**, the trimming happens first.

   Image Asset Studio creates the icon within a transparent square so there's some padding
   on the edges. The padding provides adequate space for the standard drop-shadow icon effect.
5. Click **Next**.
6. Optionally change the resource directory:
   - **Res Directory** - Select the resource source set where you want to add the image asset: **src/main/res** , **src/debug/res** , **src/release/res** , or a user-defined source set. The main source set applies to all build variants, including debug and release. The debug and release source sets override the main source set and apply to one version of a build. The debug source set is for debugging only. To define a new source set, select **File** \> **Project Structure** \> **app** \> **Build Types** . For example, you could define a beta source set and create a version of an icon that includes the text "BETA" in the bottom right corner. For more information, see [Configure Build Variants](https://developer.android.com/studio/build/build-variants#workBuildVariants).
7. The **Output Directories** area displays the images and the folders where they will appear in [Project Files view](https://developer.android.com/studio/projects#ProjectFiles) of the **Project** window.
8. Click **Finish**.
9. Image Asset Studio adds the images in the **drawable** folders for the different densities and versions.

## Refer to an image resource in code with Views

| **Note:** For information about referring to launcher icons in your code, see the [Compose launcher icon guidance](https://developer.android.com/studio/write/create-app-icons#material-icons-compose), which applies to Views too.

You can normally refer to an image resource in a generic way in your code, and when
your app runs, the corresponding image displays automatically depending on the
device:

- In most cases, you can refer to image resources as `@drawable` in XML code or [Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable) in Java code.
- For example, the following layout XML code displays the drawable in an [ImageView](https://developer.android.com/reference/android/widget/ImageView):  

```xml
<ImageView
    android:layout_height="wrap_content"
    android:layout_width="wrap_content"
    android:src="@drawable/myimage" />
```
- The following Java code retrieves the image as a [Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable):  

### Kotlin

```kotlin
val drawable = resources.getDrawable(R.drawable.myimage, theme)
```

### Java

```java
Resources res = getResources();
Drawable drawable = res.getDrawable(R.drawable.myimage, getTheme());
```
- The [getResources()](https://developer.android.com/reference/android/content/Context#getResources()) method resides in the [Context](https://developer.android.com/reference/android/content/Context) class, which applies to UI objects, such as activities, fragments, layouts, views, and so on.
- If your app uses the Support Library, you can refer to an image resource in XML code with an `app:srcCompat` statement. For example:  

```xml
<ImageView
    android:layout_height="wrap_content"
    android:layout_width="wrap_content"
    app:srcCompat="@drawable/myimage" />
```

You can access image resources from the main thread only.

After you have an image resource in the `res/` directory of your project, you can
reference it from your Java code or your XML layout using its resource ID.
The following Java code sets an
[ImageView](https://developer.android.com/reference/android/widget/ImageView) to use
the `drawable/myimage.png` resource:  

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

See
[Accessing Resources](https://developer.android.com/guide/topics/resources/accessing-resources#ResourcesFromCode) for more information.

## Delete an icon from a project

To remove an icon from a project:

1. In the **Project** window, select the [Android view](https://developer.android.com/studio/projects#ProjectFiles).
2. Expand the **res/mipmap** folder for a launcher icon, or the **res/drawable** folder for other types of icons.
3. Locate a subfolder that has the name of the icon you want to delete.
4. This folder contains the icon in different densities.
5. Select the folder and press the **Delete** key.
6. Alternatively, select **Edit** \> **Delete** . Or right-click the file and select **Delete**.
7. The **Safe Delete** dialog appears.
8. Optionally select options to find where the icon is used in the project, and click **OK**.
9. Android Studio deletes the files from the project and the drive. However, if you chose to search for places in the project where the files are used and some usages are found, you can view them and decide whether to delete them. You must delete or replace these references to be able to successfully compile your project.
10. Select **Build** \> **Clean Project**.
11. Android Studio removes any generated image files corresponding to the deleted image resource. It removes them from the project and the drive.
12. If needed, correct any remaining errors due to portions of the code that reference the resource.
13. Android Studio highlights these errors in your code. When you've removed all references from your code, you can successfully build your project again.