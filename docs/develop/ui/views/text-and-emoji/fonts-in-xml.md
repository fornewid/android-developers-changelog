---
title: https://developer.android.com/develop/ui/views/text-and-emoji/fonts-in-xml
url: https://developer.android.com/develop/ui/views/text-and-emoji/fonts-in-xml
source: md.txt
---

Try the Compose way Jetpack Compose is the recommended UI toolkit for Android. Learn how to use text in Compose. [Set font →](https://developer.android.com/develop/ui/compose/text/fonts#set-font) ![](https://developer.android.com/static/images/android-compose-ui-logo.png)


Android 8.0 (API level 26) introduces fonts in XML, a feature that
lets you use fonts as resources. You can add the `font` file in
the `res/font/` folder to bundle fonts as resources. These fonts
are compiled in your `R` file and are automatically available in
Android Studio. You can access the font resources using the `font` resource type. For
example, to access a font resource,
use `@font/myfont`, or `R.font.myfont`.


To use the fonts in XML feature on devices running Android 4.1
(API level 16) and higher, use Support Library 26.0. For more information
on using the Support Library, refer to the
[Use the Support Library](https://developer.android.com/develop/ui/views/text-and-emoji/fonts-in-xml#using-support-lib) section.


To add fonts as resources, perform the following steps in Android
Studio:


1. Right-click the **res** folder and go to **New \> Android resource directory** . The **New Resource Directory** window appears.
2. In the **Resource type** list, select **font** , then click **OK** .

   **Note** : The name of the resource directory must be
   **font**.
   ![Adding the font resource directory](https://developer.android.com/static/guide/topics/ui/images/look-and-feel/fonts-in-xml/resource-directory-font.png)


   **Figure 1.** Adding the font resource directory.
3. Add your font files in the `font` folder.

   The folder structure below generates
   `R.font.dancing_script`, `R.font.lobster`, and
   `R.font.typo_graphica`.
   ![Adding the font files in the resource directory](https://developer.android.com/static/guide/topics/ui/images/look-and-feel/fonts-in-xml/font-files-structure.png)


   **Figure 2.** Adding the font files in the `res/font` directory.
4. Double-click a font file to preview the file's fonts in the editor. ![Previewing the font file](https://developer.android.com/static/guide/topics/ui/images/look-and-feel/fonts-in-xml/preview-font.png)

   **Figure 3.**
   Previewing the font file.

### Create a font family


A font family is a set of font files along with style and weight details.
In Android, you can create a new font family as an XML resource and access
it as a single unit, instead of referencing each style and weight as
separate resources. By doing this, you let the system select the correct font
based on the text style you are using.

To create a font family, perform the following steps in Android Studio:

1. Right-click the `font` folder and select **New \> Font resource file** . The **New Resource File** window appears.
2. Enter the filename, then click **OK**. The new font resource XML opens in the editor.
3. Enclose each font file, style, and weight attribute in the `<font>` element. The following XML illustrates adding font-related attributes in the font resource XML:

   ```xml
   <?xml version="1.0" encoding="utf-8"?>
   <font-family xmlns:android="http://schemas.android.com/apk/res/android">
       <font
           android:fontStyle="normal"
           android:fontWeight="400"
           android:font="@font/lobster_regular" />
       <font
           android:fontStyle="italic"
           android:fontWeight="400"
           android:font="@font/lobster_italic" />
   </font-family>
   ```

### Use fonts in XML layouts


Use your fonts, either a single font file or a font from a
font family, in `https://developer.android.com/reference/android/widget/TextView`
objects or in styles by using the
`fontFamily` attribute.

**Note:** When you use a font family, the
`TextView` switches on its own, as needed, to use the
font files from that family.

#### Add fonts to a TextView


To set a font for a `TextView`, do one of the
following:

- In the layout XML file, set the `fontFamily` attribute to the font file you want to access.

  ```xml
  <TextView
          android:layout_width="wrap_content"
          android:layout_height="wrap_content"
          android:fontFamily="@font/lobster"/>
  ```
- Open the **Properties** window to set the font for the `TextView`.
  1. Select a view to open the **Properties** window.

     **Note:** The **Properties** window is available
     only when the design editor is open. Select the **Design** tab at
     the bottom of the window.
  2. Expand the **textAppearance** property, and then select the font from the *fontFamily* list.
  3. ![Selecting the font from Properties](https://developer.android.com/static/guide/topics/ui/images/look-and-feel/fonts-in-xml/property-window.png)

     **Figure 4.**
     Selecting the font from the **Properties** window.


The Android Studio layout preview, shown in the rightmost pane in Figure 5,
lets you preview the font set in the `TextView`.
![Previewing fonts in layout preview](https://developer.android.com/static/guide/topics/ui/images/look-and-feel/fonts-in-xml/xml-font-preview.png)

**Figure 5.**
Previewing fonts in layout preview.

#### Add fonts to a style

Open the `styles.xml` file and set the `fontFamily`
attribute to the font file you want to access.
-

  ```xml
  <style name="customfontstyle" parent="@android:style/TextAppearance.Small">
      <item name="android:fontFamily">@font/lobster</item>
  </style>
  ```

### Use fonts programmatically

- To retrieve fonts programmatically, call the `https://developer.android.com/reference/android/content/res/Resources#getFont(int)` method and provide the resource identifier of the font you want to retrieve. This method returns a `https://developer.android.com/reference/android/graphics/Typeface` object. Although the system picks the best style for you from the fonts' information, you can use the `https://developer.android.com/reference/android/widget/TextView#setTypeface(android.graphics.Typeface, int)` method to set the typeface with specific styles.
- **Note:** The `TextView` does this for you.

### Kotlin

```kotlin
val typeface = resources.getFont(R.font.myfont)
textView.typeface = typeface
```

### Java

```java
Typeface typeface = getResources().getFont(R.font.myfont);
textView.setTypeface(typeface);
```

### Use the Support Library

- The Support Library 26.0 supports fonts in XML on devices running Android 4.1 (API level 16) and higher.
- **Note** : When you declare font families in XML layout through the Support Library, use the **app** namespace to ensure that your fonts load.

```xml
<?xml version="1.0" encoding="utf-8"?>
<font-family xmlns:app="http://schemas.android.com/apk/res-auto">
    <font app:fontStyle="normal" app:fontWeight="400" app:font="@font/myfont-Regular"/>
    <font app:fontStyle="italic" app:fontWeight="400" app:font="@font/myfont-Italic" />
</font-family>
```
- To retrieve fonts programmatically, call the `ResourceCompat.getFont(Context, int)` method and provide an instance of `Context` and the resource identifier.

### Kotlin

```kotlin
val typeface = ResourcesCompat.getFont(context, R.font.myfont)
```

### Java

```java
Typeface typeface = ResourcesCompat.getFont(context, R.font.myfont);
```