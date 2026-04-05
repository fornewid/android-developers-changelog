---
title: https://developer.android.com/guide/topics/resources/drawable-resource
url: https://developer.android.com/guide/topics/resources/drawable-resource
source: md.txt
---

A drawable resource is a general concept for a graphic that can be drawn to the screen and that
you can retrieve with APIs such as [getDrawable(int)](https://developer.android.com/reference/android/content/res/Resources#getDrawable(int,%20android.content.res.Resources.Theme)) or apply
to another XML resource with attributes such as `android:drawable` and `android:icon`.
There are several types of drawables:

[Bitmap file](https://developer.android.com/guide/topics/resources/drawable-resource#Bitmap)

:   A bitmap graphic file (PNG, WEBP, JPG, or GIF).
    Creates a [BitmapDrawable](https://developer.android.com/reference/android/graphics/drawable/BitmapDrawable).

[Nine-patch file](https://developer.android.com/guide/topics/resources/drawable-resource#NinePatch)
:   A PNG file with stretchable regions to let images resize based on content (`.9.png`). Creates a [NinePatchDrawable](https://developer.android.com/reference/android/graphics/drawable/NinePatchDrawable).

[Layer list](https://developer.android.com/guide/topics/resources/drawable-resource#LayerList)
:   A drawable that manages an array of other drawables. These are drawn in array order, so the
    element with the largest index is drawn on top. Creates a [LayerDrawable](https://developer.android.com/reference/android/graphics/drawable/LayerDrawable).

[State list](https://developer.android.com/guide/topics/resources/drawable-resource#StateList)
:   An XML file that references different bitmap graphics
    for different states---for example, to use a different image when a button is tapped.
    Creates a [StateListDrawable](https://developer.android.com/reference/android/graphics/drawable/StateListDrawable).

[Level list](https://developer.android.com/guide/topics/resources/drawable-resource#LevelList)
:   An XML file that defines a drawable that manages a number of alternate drawables, each
    assigned a maximum numerical value. Creates a [LevelListDrawable](https://developer.android.com/reference/android/graphics/drawable/LevelListDrawable).

[Transition drawable](https://developer.android.com/guide/topics/resources/drawable-resource#Transition)
:   An XML file that defines a drawable that can cross-fade between two drawable resources.
    Creates a [TransitionDrawable](https://developer.android.com/reference/android/graphics/drawable/TransitionDrawable).

[Inset drawable](https://developer.android.com/guide/topics/resources/drawable-resource#Inset)
:   An XML file that defines a drawable that insets another drawable by a specified distance.
    This is useful when a view needs a background drawable that is smaller than the view's actual
    bounds.

[Clip drawable](https://developer.android.com/guide/topics/resources/drawable-resource#Clip)
:   An XML file that defines a drawable that clips another drawable based on this drawable's
    current level value. Creates a [ClipDrawable](https://developer.android.com/reference/android/graphics/drawable/ClipDrawable).

[Scale drawable](https://developer.android.com/guide/topics/resources/drawable-resource#Scale)
:   An XML file that defines a drawable that changes the size of another drawable based on its
    current level value. Creates a [ScaleDrawable](https://developer.android.com/reference/android/graphics/drawable/ScaleDrawable)

[Shape drawable](https://developer.android.com/guide/topics/resources/drawable-resource#Shape).
:   An XML file that defines a geometric shape, including colors and gradients.
    Creates a [GradientDrawable](https://developer.android.com/reference/android/graphics/drawable/GradientDrawable).

For information about how to
create an [AnimationDrawable](https://developer.android.com/reference/android/graphics/drawable/AnimationDrawable),
see the [Animation resources](https://developer.android.com/guide/topics/resources/animation-resource) document.

**Note:** A [color resource](https://developer.android.com/guide/topics/resources/more-resources#Color) can also be
used as a drawable in XML. For example, when creating a [state list
drawable](https://developer.android.com/guide/topics/resources/drawable-resource#StateList), you can reference a color resource for the `android:drawable` attribute (`android:drawable="@color/green"`).

## Bitmap

A bitmap image. Android supports bitmap files in the following formats:
PNG (preferred), WEBP (preferred, requires API level 17 or higher), JPG (acceptable), GIF (discouraged).

You can reference a bitmap file directly, using the filename as the resource ID, or create an
alias resource ID in XML.

**Note:** Bitmap files might be automatically optimized with lossless
image compression by the `aapt` tool during the build process. For
example, a true-color PNG that doesn't require more than 256 colors might be converted to an 8-bit
PNG with a color palette. This results in an image of equal quality that requires less
memory.  


So, be aware that the image binaries placed in this directory can change during the build. If
you plan to read an image as a bit stream to convert it to a bitmap, put your images in
the `res/raw/` folder instead, where they aren't optimized.

### Bitmap file

A bitmap file is a PNG, WEBP, JPG, or GIF file. Android creates a [Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable)
resource for any of these files when you save them in the `res/drawable/` directory.

file location:
:   `res/drawable/`*filename*`.png` (`.png`, `.webp`, `.jpg`, or `.gif`)  

    The filename is the resource ID

compiled resource datatype:
:   Resource pointer to a [BitmapDrawable](https://developer.android.com/reference/android/graphics/drawable/BitmapDrawable)

resource reference:
:
    In Java: `R.drawable.`*filename*  

    In XML: `@[`*package* `:]drawable/`*filename*

example:
:   With an image saved at `res/drawable/myimage.png`, this layout XML applies
    the image to a view:  

    ```xml
    <ImageView
        android:layout_height="wrap_content"
        android:layout_width="wrap_content"
        android:src="@drawable/myimage" />
    ```

    The following application code retrieves the image as a [Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable):

    ### Kotlin

        val drawable: Drawable? = ResourcesCompat.https://developer.android.com/reference/androidx/core/content/res/ResourcesCompat#getDrawable(android.content.res.Resources, int, android.content.res.Resources.Theme)(resources, R.drawable.myimage, null)

    ### Java

        Resources res = https://developer.android.com/reference/android/content/Context#getResources();
        Drawable drawable = ResourcesCompat.https://developer.android.com/reference/androidx/core/content/res/ResourcesCompat#getDrawable(android.content.res.Resources, int, android.content.res.Resources.Theme)(res, R.drawable.myimage, null);


see also:
:
    - [Drawables overview](https://developer.android.com/develop/ui/views/graphics/drawables)
    - [BitmapDrawable](https://developer.android.com/reference/android/graphics/drawable/BitmapDrawable)

### XML bitmap

An XML bitmap is a resource defined in XML that points to a bitmap file. The effect is an alias for a
raw bitmap file. The XML can specify additional properties for the bitmap, such as dithering and tiling.

**Note:** You can use a `<bitmap>` element as a child of
an `<item>` element. For
example, when creating a [state list](https://developer.android.com/guide/topics/resources/drawable-resource#StateList) or [layer list](https://developer.android.com/guide/topics/resources/drawable-resource#LayerList),
you can exclude the `android:drawable`
attribute from an `<item>` element and nest a `<bitmap>` inside it
that defines the drawable item.

file location:
:   `res/drawable/`*filename*`.xml`  

    The filename is the resource ID

compiled resource datatype:
:   Resource pointer to a [BitmapDrawable](https://developer.android.com/reference/android/graphics/drawable/BitmapDrawable)

resource reference:
:
    In Java: `R.drawable.`*filename*  

    In XML: `@[`*package* `:]drawable/`*filename*

syntax:
:

    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <bitmap
        xmlns:android="http://schemas.android.com/apk/res/android"
        android:src="@[package:]drawable/drawable_resource"
        android:antialias=["true" | "false"]
        android:dither=["true" | "false"]
        android:filter=["true" | "false"]
        android:gravity=["top" | "bottom" | "left" | "right" | "center_vertical" |
                          "fill_vertical" | "center_horizontal" | "fill_horizontal" |
                          "center" | "fill" | "clip_vertical" | "clip_horizontal"]
        android:mipMap=["true" | "false"]
        android:tileMode=["disabled" | "clamp" | "repeat" | "mirror"] />
    ```

elements:
:

    `<bitmap>`
    :   **Required.** Defines the bitmap source and its properties.

        Attributes:

        `xmlns:android`
        :   *String* . Defines the XML namespace, which must be
            `"http://schemas.android.com/apk/res/android"`. This is required only if the
            `<bitmap>` is the root element. It isn't needed when the
            `<bitmap>` is nested inside an `<item>`.

        `android:src`
        :   *Drawable resource* . **Required**. Reference to a drawable
            resource.

        `android:antialias`
        :   *Boolean*. Enables or disables antialiasing.

        `android:dither`
        :   *Boolean*. Enables or disables dithering of the bitmap if the bitmap doesn't
            have the same pixel configuration as the screen, such as an ARGB 8888 bitmap on an RGB 565
            screen.

        `android:filter`
        :   *Boolean*. Enables or disables bitmap filtering. Filtering is used when the
            bitmap is shrunk or stretched to smooth its appearance.

        `android:gravity`
        :   *Keyword* . Defines the gravity for the bitmap. The gravity indicates where to
            position the drawable in its container if the bitmap is smaller than the container.

            Must be one or more of the following constant values, separated by `|`:

            | Value | Description |
            |---|---|
            | `top` | Put the object at the top of its container, not changing its size. |
            | `bottom` | Put the object at the bottom of its container, not changing its size. |
            | `left` | Put the object at the left edge of its container, not changing its size. |
            | `right` | Put the object at the right edge of its container, not changing its size. |
            | `center_vertical` | Put the object in the vertical center of its container, not changing its size. |
            | `fill_vertical` | Grow the vertical size of the object if needed so it completely fills its container. |
            | `center_horizontal` | Place object in the horizontal center of its container, not changing its size. |
            | `fill_horizontal` | Grow the horizontal size of the object if needed so it completely fills its container. |
            | `center` | Put the object in the center of its container in both the vertical and horizontal axis, not changing its size. |
            | `fill` | Grow the horizontal and vertical size of the object if needed so it completely fills its container. This is the default. |
            | `clip_vertical` | Additional option that can be set to have the top and/or bottom edges of the child clipped to its container's bounds. The clip is based on the vertical gravity: a top gravity clips the bottom edge, a bottom gravity clips the top edge, and neither clips both edges. |
            | `clip_horizontal` | Additional option that can be set to have the left and/or right edges of the child clipped to its container's bounds. The clip is based on the horizontal gravity: a left gravity clips the right edge, a right gravity clips the left edge, and neither clips both edges. |


        `android:mipMap`
        :   *Boolean* . Enables or disables the mipmap hint. See [setHasMipMap()](https://developer.android.com/reference/android/graphics/Bitmap#setHasMipMap(boolean)) for more information.
            The default value is false.

        `android:tileMode`
        :   *Keyword* . Defines the tile mode. When the tile mode is enabled, the bitmap is
            repeated. Gravity is ignored when the tile mode is enabled.

            Must be one of the following constant values:

            | Value | Description |
            |---|---|
            | `disabled` | Don't tile the bitmap. This is the default value. |
            | `clamp` | Replicate the edge color if the shader draws outside its original bounds |
            | `repeat` | Repeat the shader's image horizontally and vertically. |
            | `mirror` | Repeat the shader's image horizontally and vertically, alternating mirror images so that adjacent images always seam. |


example:
:

    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <bitmap xmlns:android="http://schemas.android.com/apk/res/android"
        android:src="@drawable/icon"
        android:tileMode="repeat" />
    ```


see also:
:
    - [BitmapDrawable](https://developer.android.com/reference/android/graphics/drawable/BitmapDrawable)
    - [Create
      alias resources](https://developer.android.com/guide/topics/resources/providing-resources#AliasResources)

## Nine-patch

A [NinePatch](https://developer.android.com/reference/android/graphics/NinePatch) is a PNG image in which you can define stretchable regions
that Android scales when content within the view exceeds the normal image bounds. You
typically assign this type of image as the background of a view that has at least one dimension set
to `"wrap_content"`.

When the view grows to accommodate the content, the nine-patch image
is also scaled to match the size of the view. An example use of a nine-patch image is the
background used by Android's standard [Button](https://developer.android.com/reference/android/widget/Button) widget, which must stretch to
accommodate the text (or image) inside the button.

As with a normal [bitmap](https://developer.android.com/guide/topics/resources/drawable-resource#Bitmap), you can reference a nine-patch file directly
or from a resource defined by XML.

For a complete discussion about how to create a nine-patch file with stretchable regions,
see [Create resizable bitmaps (9-patch files)](https://developer.android.com/studio/write/draw9patch).

### Nine-patch file

file location:
:   `res/drawable/`*filename*`.9.png`  

    The filename is the resource ID

compiled resource datatype:
:   Resource pointer to a [NinePatchDrawable](https://developer.android.com/reference/android/graphics/drawable/NinePatchDrawable)

resource reference:
:
    In Java: `R.drawable.`*filename*  

    In XML: `@[`*package* `:]drawable/`*filename*

example:
:   With an image saved at `res/drawable/myninepatch.9.png`, this layout XML
    applies the nine-patch to a view:  

    ```xml
    <Button
        android:layout_height="wrap_content"
        android:layout_width="wrap_content"
        android:background="@drawable/myninepatch" />
    ```

see also:
:
    - [Create resizable bitmaps (9-patch files)](https://developer.android.com/studio/write/draw9patch)
    - [NinePatchDrawable](https://developer.android.com/reference/android/graphics/drawable/NinePatchDrawable)

### XML nine-patch

An XML nine-patch is a resource defined in XML that points to a nine-patch file. The XML can
specify dithering for the image.

file location:
:   `res/drawable/`*filename*`.xml`  

    The filename is the resource ID

compiled resource datatype:
:   Resource pointer to a [NinePatchDrawable](https://developer.android.com/reference/android/graphics/drawable/NinePatchDrawable)

resource reference:
:
    In Java: `R.drawable.`*filename*  

    In XML: `@[`*package* `:]drawable/`*filename*

syntax:
:

    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <nine-patch
        xmlns:android="http://schemas.android.com/apk/res/android"
        android:src="@[package:]drawable/drawable_resource"
        android:dither=["true" | "false"] />
    ```

elements:
:

    `<nine-patch>`
    :   **Required.** Defines the nine-patch source and its properties.

        Attributes:

        `xmlns:android`
        :   *String* . **Required.** Defines the XML namespace, which must be
            `"http://schemas.android.com/apk/res/android"`.

        `android:src`
        :   *Drawable resource* . **Required**. Reference to a nine-patch
            file.

        `android:dither`
        :   *Boolean*. Enables or disables dithering of the bitmap if the bitmap doesn't
            have the same pixel configuration as the screen, such as an ARGB 8888 bitmap on an RGB 565
            screen.


example:
:

    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <nine-patch xmlns:android="http://schemas.android.com/apk/res/android"
        android:src="@drawable/myninepatch"
        android:dither="false" />
    ```

## Layer list

A [LayerDrawable](https://developer.android.com/reference/android/graphics/drawable/LayerDrawable) is a drawable object
that manages an array of other drawables. Each drawable in the list is drawn in the order of the
list. The last drawable in the list is drawn on top.

Each drawable is represented by an `<item>` element inside a single `<layer-list>` element.

file location:
:   `res/drawable/`*filename*`.xml`  

    The filename is the resource ID

compiled resource datatype:
:   Resource pointer to a [LayerDrawable](https://developer.android.com/reference/android/graphics/drawable/LayerDrawable)

resource reference:
:
    In Java: `R.drawable.`*filename*  

    In XML: `@[`*package* `:]drawable/`*filename*

syntax:
:

    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <layer-list
        xmlns:android="http://schemas.android.com/apk/res/android" >
        <item
            android:drawable="@[package:]drawable/drawable_resource"
            android:id="@[+][package:]id/resource_name"
            android:top="dimension"
            android:right="dimension"
            android:bottom="dimension"
            android:left="dimension" />
    </layer-list>
    ```

elements:
:

    `<layer-list>`
    :   **Required.** This must be the root element. Contains one or more `<item>` elements.

        Attributes:

        `xmlns:android`
        :   *String* . **Required.** Defines the XML namespace, which must be
            `"http://schemas.android.com/apk/res/android"`.

    `<item>`
    :   Defines a drawable to place in the layer drawable, in a position defined by its attributes.
        Must be a child of a `<layer-list>` element. Accepts child `<bitmap>`
        elements.

        Attributes:

        `android:drawable`
        :   *Drawable resource* . **Required**. Reference to a drawable
            resource.

        `android:id`
        :   *Resource ID* . A unique resource ID for this drawable. To create a new resource
            ID for this item, use the form:
            `"@+id/`*name*`"`. The plus symbol indicates that this is created as a new
            ID. You can use this identifier to
            retrieve and modify the drawable with [View.findViewById()](https://developer.android.com/reference/android/view/View#findViewById(int)) or [Activity.findViewById()](https://developer.android.com/reference/android/app/Activity#findViewById(int)).

        `android:top`
        :   *Dimension* . The top offset, as a dimension value or [dimension resource](https://developer.android.com/guide/topics/resources/more-resources#Dimension).

        `android:right`
        :   *Dimension* . The right offset, as a dimension value or [dimension resource](https://developer.android.com/guide/topics/resources/more-resources#Dimension).

        `android:bottom`
        :   *Dimension* . The bottom offset, as a dimension value or [dimension resource](https://developer.android.com/guide/topics/resources/more-resources#Dimension).

        `android:left`
        :   *Dimension* . The left offset, as a dimension value or [dimension resource](https://developer.android.com/guide/topics/resources/more-resources#Dimension).

        All drawable items are scaled to fit the size of the containing view, by default. Thus,
        placing your images in a layer list at different positions might increase the size of the view, and
        some images scale as appropriate.

        To avoid
        scaling items in the list, use a `<bitmap>` element inside the `<item>` element to specify the drawable and define the gravity to something that doesn't
        scale, such as `"center"`. For example, the following `<item>` defines an item
        that scales to fit its container view:

        ```xml
        <item android:drawable="@drawable/image" />
        ```


        To avoid scaling, the following example uses a `<bitmap>` element with centered
        gravity:

        ```xml
        <item>
          <bitmap android:src="@drawable/image"
                  android:gravity="center" />
        </item>
        ```


example:
    : XML file saved at `res/drawable/layers.xml`:  

    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <layer-list xmlns:android="http://schemas.android.com/apk/res/android">
        <item>
          <bitmap android:src="@drawable/android_red"
            android:gravity="center" />
        </item>
        <item android:top="10dp" android:left="10dp">
          <bitmap android:src="@drawable/android_green"
            android:gravity="center" />
        </item>
        <item android:top="20dp" android:left="20dp">
          <bitmap android:src="@drawable/android_blue"
            android:gravity="center" />
        </item>
    </layer-list>
    ```

    This example uses a nested `<bitmap>` element to define the drawable
    resource for each item with a `"center"` gravity. This ensures that none of the images are scaled to
    fit the size of the container, due to resizing caused by the offset images.


    This layout XML applies the drawable to a view:

    ```xml
    <ImageView
        android:layout_height="wrap_content"
        android:layout_width="wrap_content"
        android:src="@drawable/layers" />
    ```


    The result is a stack of increasingly offset images:

    ![](https://developer.android.com/static/images/resources/layers.png)

see also:
:
    - [LayerDrawable](https://developer.android.com/reference/android/graphics/drawable/LayerDrawable)

## State list

A [StateListDrawable](https://developer.android.com/reference/android/graphics/drawable/StateListDrawable) is a drawable object defined in XML
that uses multiple images to represent the same graphic, depending on the state of
the object. For example, the state of a [Button](https://developer.android.com/reference/android/widget/Button) widget can be tapped, focused,
or neither; using a state list drawable, you can provide a different background image for each
state.

You describe the state list in an XML file. Each graphic is represented by an `<item>` element inside a single `<selector>` element. Each `<item>`
uses various attributes to describe the state in which it is used as the graphic for the
drawable.

During each state change, the state list is traversed top to bottom, and the first item that
matches the current state is used. The selection is *not* based on the "best
match," but rather the first item that meets the minimum criteria of the state.

file location:
:   `res/drawable/`*filename*`.xml`  

    The filename is the resource ID

compiled resource datatype:
:   Resource pointer to a [StateListDrawable](https://developer.android.com/reference/android/graphics/drawable/StateListDrawable)

resource reference:
:
    In Java: `R.drawable.`*filename*  

    In XML: `@[`*package* `:]drawable/`*filename*

syntax:
:

    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <selector xmlns:android="http://schemas.android.com/apk/res/android"
        android:constantSize=["true" | "false"]
        android:dither=["true" | "false"]
        android:variablePadding=["true" | "false"] >
        <item
            android:drawable="@[package:]drawable/drawable_resource"
            android:state_pressed=["true" | "false"]
            android:state_focused=["true" | "false"]
            android:state_hovered=["true" | "false"]
            android:state_selected=["true" | "false"]
            android:state_checkable=["true" | "false"]
            android:state_checked=["true" | "false"]
            android:state_enabled=["true" | "false"]
            android:state_activated=["true" | "false"]
            android:state_window_focused=["true" | "false"] />
    </selector>
    ```

elements:
:

    `<selector>`
    :   **Required.** This must be the root element. Contains one or more `<item>` elements.

        Attributes:

        `xmlns:android`
        :   *String* . **Required.** Defines the XML namespace, which must be
            `"http://schemas.android.com/apk/res/android"`.

        `android:constantSize`
        :   *Boolean*. True if the drawable's reported internal size remains constant as the state
            changes (the size is the maximum of all of the states); false if the size varies based on
            the current state. The default is false.

        `android:dither`
        :   *Boolean*. True to enable dithering of the bitmap if the bitmap doesn't have the same pixel
            configuration as the screen, such as an ARGB 8888 bitmap on an RGB 565 screen; false to
            disable dithering. The default is true.

        `android:variablePadding`
        :   *Boolean*. True if the drawable's padding changes based on the current
            state that is selected; false if the padding must stay the same, based on the maximum
            padding of all the states. Enabling this feature requires that you deal with
            performing layout when the state changes, which is often not supported. The default is false.

    `<item>`
    :   Defines a drawable to use during certain states, as described by its attributes. Must be a
        child of a `<selector>` element.

        Attributes:

        `android:drawable`
        :   *Drawable resource* . **Required**. Reference to a drawable resource.

        `android:state_pressed`
        :   *Boolean*. True if this item is used when the object is tapped, such as when a button
            is touched; false if this item is used in the default, non-tapped state.

        `android:state_focused`
        :   *Boolean*. True if this item is used when the object has input focus,
            such as when the user selects a text input; false if this item is used in the default,
            non-focused state.

        `android:state_hovered`
        :   *Boolean* . True if this item is used when the cursor hovers over the object;
            false if this item is used in the default, non-hovered state. Often, this
            drawable can be the same drawable used for the "focused" state.

            Introduced in API level 14.

        `android:state_selected`
        :   *Boolean* . True if this item is used when the object is the current
            user selection when navigating with a directional control, such as when navigating through a list
            with a D-pad; false if this item is used when the object isn't selected.

            The selected state is used when `android:state_focused` isn't sufficient,
            such as when the list view has focus and an item within it is selected with a D-pad.

        `android:state_checkable`
        :   *Boolean*. True if this item is used when the object is selectable; false if this
            item is used when the object isn't selectable. Only useful if the object can
            transition between a selectable and non-selectable widget.

        `android:state_checked`
        :   *Boolean*. True if this item is used when the object is selected; false if it
            is used when the object is un-selected.

        `android:state_enabled`
        :   *Boolean*. True if this item is used when the object is enabled,
            meaning capable of receiving touch or click events; false if it is used when the object is
            disabled.

        `android:state_activated`
        :   *Boolean* . True if this item is used when the object is activated as
            the persistent selection, such as to "highlight" the previously selected list item in a persistent
            navigation view; false if it is used when the object isn't activated.

            Introduced in API level 11.

        `android:state_window_focused`
        :   *Boolean*. True if this item is used when the application window has focus, meaning the
            application is in the foreground; false if this item is used when the application
            window doesn't have focus, for example, if the notification shade is pulled down or a dialog appears.

        **Note:** Android applies the first item in the state list that
        matches the current state of the object. So, if the first item in the list contains
        none of the preceding state attributes, then it is applied every time. This is why you want your
        default value to always be last, as demonstrated in the following example.


example:
    : XML file saved at `res/drawable/button.xml`:  

    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <selector xmlns:android="http://schemas.android.com/apk/res/android">
        <item android:state_pressed="true"
              android:drawable="@drawable/button_pressed" /> <!-- pressed -->
        <item android:state_focused="true"
              android:drawable="@drawable/button_focused" /> <!-- focused -->
        <item android:state_hovered="true"
              android:drawable="@drawable/button_focused" /> <!-- hovered -->
        <item android:drawable="@drawable/button_normal" /> <!-- default -->
    </selector>
    ```


    This layout XML applies the state list drawable to a button:

    ```xml
    <Button
        android:layout_height="wrap_content"
        android:layout_width="wrap_content"
        android:background="@drawable/button" />
    ```

see also:
:
    - [StateListDrawable](https://developer.android.com/reference/android/graphics/drawable/StateListDrawable)

## Level list

A drawable that manages a number of alternate drawables, each assigned a maximum numerical
value. Setting the level value of the drawable with [setLevel()](https://developer.android.com/reference/android/graphics/drawable/Drawable#setLevel(int)) loads the drawable resource in the
level list that has an `android:maxLevel` value greater than or equal to the value
passed to the method.

file location:
:   `res/drawable/`*filename*`.xml`  

    The filename is the resource ID

compiled resource datatype:
:   Resource pointer to a [LevelListDrawable](https://developer.android.com/reference/android/graphics/drawable/LevelListDrawable)

resource reference:
:
    In Java: `R.drawable.`*filename*  

    In XML: `@[`*package* `:]drawable/`*filename*

syntax:
:

    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <level-list
        xmlns:android="http://schemas.android.com/apk/res/android" >
        <item
            android:drawable="@drawable/drawable_resource"
            android:maxLevel="integer"
            android:minLevel="integer" />
    </level-list>
    ```

elements:
:

    `<level-list>`
    :   **Required.** This must be the root element. Contains one or more `<item>` elements.

        Attributes:

        `xmlns:android`
        :   *String* . **Required.** Defines the XML namespace, which must be
            `"http://schemas.android.com/apk/res/android"`.

    `<item>`

    :   Defines a drawable to use at a certain level. Attributes:

        `android:drawable`
        :   *Drawable resource* . **Required**. Reference to a drawable
            resource to be inset.

        `android:maxLevel`
        :   *Integer*. The maximum level permitted for this item.

        `android:minLevel`
        :   *Integer*. The minimum level permitted for this item.


example:
:

    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <level-list xmlns:android="http://schemas.android.com/apk/res/android" >
        <item
            android:drawable="@drawable/status_off"
            android:maxLevel="0" />
        <item
            android:drawable="@drawable/status_on"
            android:maxLevel="1" />
    </level-list>
    ```

    Once this is applied to a [View](https://developer.android.com/reference/android/view/View), the level can be changed with [setLevel()](https://developer.android.com/reference/android/graphics/drawable/Drawable#setLevel(int)) or [setImageLevel()](https://developer.android.com/reference/android/widget/ImageView#setImageLevel(int)).


see also:
:
    - [LevelListDrawable](https://developer.android.com/reference/android/graphics/drawable/LevelListDrawable)

## Transition drawable

A [TransitionDrawable](https://developer.android.com/reference/android/graphics/drawable/TransitionDrawable) is a drawable object
that can cross-fade between two other drawable resources.

Each drawable is represented by an `<item>` element inside a single `<transition>` element. No more than two items are supported. To transition forward, call
[startTransition()](https://developer.android.com/reference/android/graphics/drawable/TransitionDrawable#startTransition(int)). To
transition backward, call [reverseTransition()](https://developer.android.com/reference/android/graphics/drawable/TransitionDrawable#reverseTransition(int)).

file location:
:   `res/drawable/`*filename*`.xml`  

    The filename is the resource ID

compiled resource datatype:
:   Resource pointer to a [TransitionDrawable](https://developer.android.com/reference/android/graphics/drawable/TransitionDrawable)

resource reference:
:
    In Java: `R.drawable.`*filename*  

    In XML: `@[`*package* `:]drawable/`*filename*

syntax:
:

    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <transition
    xmlns:android="http://schemas.android.com/apk/res/android" >
        <item
            android:drawable="@[package:]drawable/drawable_resource"
            android:id="@[+][package:]id/resource_name"
            android:top="dimension"
            android:right="dimension"
            android:bottom="dimension"
            android:left="dimension" />
    </transition>
    ```

elements:
:

    `<transition>`
    :   **Required.** This must be the root element. Contains one or more `<item>` elements.

        Attributes:

        `xmlns:android`
        :   *String* . **Required.** Defines the XML namespace, which must be
            `"http://schemas.android.com/apk/res/android"`.

    `<item>`
    :   Defines a drawable to use as part of the drawable transition.
        Must be a child of a `<transition>` element. Accepts child `<bitmap>`
        elements.

        Attributes:

        `android:drawable`
        :   *Drawable resource* . **Required**. Reference to a drawable
            resource.

        `android:id`
        :   *Resource ID* . A unique resource ID for this drawable. To create a new resource
            ID for this item, use the form:
            `"@+id/`*name*`"`. The plus symbol indicates that this is created as a new
            ID. You can use this identifier to
            retrieve and modify the drawable with [View.findViewById()](https://developer.android.com/reference/android/view/View#findViewById(int)) or [Activity.findViewById()](https://developer.android.com/reference/android/app/Activity#findViewById(int)).

        `android:top`
        :   *Integer*. The top offset in pixels.

        `android:right`
        :   *Integer*. The right offset in pixels.

        `android:bottom`
        :   *Integer*. The bottom offset in pixels.

        `android:left`
        :   *Integer*. The left offset in pixels.


example:
    : XML file saved at `res/drawable/transition.xml`:  

    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <transition xmlns:android="http://schemas.android.com/apk/res/android">
        <item android:drawable="@drawable/on" />
        <item android:drawable="@drawable/off" />
    </transition>
    ```


    This layout XML applies the drawable to a view:

    ```xml
    <ImageButton
        android:id="@+id/button"
        android:layout_height="wrap_content"
        android:layout_width="wrap_content"
        android:src="@drawable/transition" />
    ```


    And the following code performs a 500 ms transition from the first item to the second:

    ### Kotlin

    ```kotlin
    val button: ImageButton = findViewById(R.id.button)
    val drawable: Drawable = button.drawable
    if (drawable is TransitionDrawable) {
        drawable.startTransition(500)
    }
    ```

    ### Java

    ```java
    ImageButton button = (ImageButton) findViewById(R.id.button);
    Drawable drawable = button.getDrawable();
    if (drawable instanceof TransitionDrawable) {
        ((TransitionDrawable) drawable).startTransition(500);
    }
    ```


see also:
:
    - [TransitionDrawable](https://developer.android.com/reference/android/graphics/drawable/TransitionDrawable)

## Inset drawable

A drawable defined in XML that insets another drawable by a specified distance. This is useful
when a view needs a background that is smaller than the view's actual bounds.

file location:
:   `res/drawable/`*filename*`.xml`  

    The filename is the resource ID

compiled resource datatype:
:   Resource pointer to a [InsetDrawable](https://developer.android.com/reference/android/graphics/drawable/InsetDrawable)

resource reference:
:
    In Java: `R.drawable.`*filename*  

    In XML: `@[`*package* `:]drawable/`*filename*

syntax:
:

    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <inset
        xmlns:android="http://schemas.android.com/apk/res/android"
        android:drawable="@drawable/drawable_resource"
        android:insetTop="dimension"
        android:insetRight="dimension"
        android:insetBottom="dimension"
        android:insetLeft="dimension" />
    ```

elements:
:

    `<inset>`
    :   **Required.** Defines the inset drawable. This must be the root element.

        Attributes:

        `xmlns:android`
        :   *String* . **Required.** Defines the XML namespace, which must be
            `"http://schemas.android.com/apk/res/android"`.

        `android:drawable`
        :   *Drawable resource* . **Required**. Reference to a drawable
            resource to be inset.

        `android:insetTop`
        :   *Dimension* . The top inset, as a dimension value or [dimension resource](https://developer.android.com/guide/topics/resources/more-resources#Dimension).

        `android:insetRight`
        :   *Dimension* . The right inset, as a dimension value or [dimension resource](https://developer.android.com/guide/topics/resources/more-resources#Dimension).

        `android:insetBottom`
        :   *Dimension* . The bottom inset, as a dimension value or [dimension resource](https://developer.android.com/guide/topics/resources/more-resources#Dimension).

        `android:insetLeft`
        :   *Dimension* . The left inset, as a dimension value or [dimension resource](https://developer.android.com/guide/topics/resources/more-resources#Dimension).


example:
:

    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <inset xmlns:android="http://schemas.android.com/apk/res/android"
        android:drawable="@drawable/background"
        android:insetTop="10dp"
        android:insetLeft="10dp" />
    ```

see also:
:
    - [InsetDrawable](https://developer.android.com/reference/android/graphics/drawable/InsetDrawable)

## Clip drawable

A drawable defined in XML that clips another drawable based on this drawable's current level. You
can control how much the child drawable gets clipped in width and height based on the level, as well
as a gravity to control where it is placed in its overall container. Most often used to implement
things like progress bars.

file location:
:   `res/drawable/`*filename*`.xml`  

    The filename is the resource ID

compiled resource datatype:
:   Resource pointer to a [ClipDrawable](https://developer.android.com/reference/android/graphics/drawable/ClipDrawable)

resource reference:
:
    In Java: `R.drawable.`*filename*  

    In XML: `@[`*package* `:]drawable/`*filename*

syntax:
:

    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <clip
        xmlns:android="http://schemas.android.com/apk/res/android"
        android:drawable="@drawable/drawable_resource"
        android:clipOrientation=["horizontal" | "vertical"]
        android:gravity=["top" | "bottom" | "left" | "right" | "center_vertical" |
                         "fill_vertical" | "center_horizontal" | "fill_horizontal" |
                         "center" | "fill" | "clip_vertical" | "clip_horizontal"] />
    ```

elements:
:

    `<clip>`
    :   **Required.** Defines the clip drawable. This must be the root element.

        Attributes:

        `xmlns:android`
        :   *String* . **Required.** Defines the XML namespace, which must be
            `"http://schemas.android.com/apk/res/android"`.

        `android:drawable`
        :   *Drawable resource* . **Required**. Reference to a drawable
            resource to be clipped.

        `android:clipOrientation`
        :   *Keyword* . The orientation for the clip.

            Must be one of the following constant values:

            | Value | Description |
            |---|---|
            | `horizontal` | Clip the drawable horizontally. |
            | `vertical` | Clip the drawable vertically. |


        `android:gravity`
        :   *Keyword* . Specifies where to clip within the drawable.

            Must be one or more of the following constant values, separated by `|`:

            | Value | Description |
            |---|---|
            | `top` | Put the object at the top of its container, not changing its size. When `clipOrientation` is `"vertical"`, clipping occurs at the bottom of the drawable. |
            | `bottom` | Put the object at the bottom of its container, not changing its size. When `clipOrientation` is `"vertical"`, clipping occurs at the top of the drawable. |
            | `left` | Put the object at the left edge of its container, not changing its size. This is the default. When `clipOrientation` is `"horizontal"`, clipping occurs at the right side of the drawable. |
            | `right` | Put the object at the right edge of its container, not changing its size. When `clipOrientation` is `"horizontal"`, clipping occurs at the left side of the drawable. |
            | `center_vertical` | Put the object in the vertical center of its container, not changing its size. Clipping behaves the same as when gravity is `"center"`. |
            | `fill_vertical` | Grow the vertical size of the object if needed so it completely fills its container. When `clipOrientation` is `"vertical"`, no clipping occurs because the drawable fills the vertical space (unless the drawable level is 0, in which case it's not visible). |
            | `center_horizontal` | Put the object in the horizontal center of its container, not changing its size. Clipping behaves the same as when gravity is `"center"`. |
            | `fill_horizontal` | Grow the horizontal size of the object if needed so it completely fills its container. When `clipOrientation` is `"horizontal"`, no clipping occurs because the drawable fills the horizontal space (unless the drawable level is 0, in which case it's not visible). |
            | `center` | Put the object in the center of its container in both the vertical and horizontal axis, not changing its size. When `clipOrientation` is `"horizontal"`, clipping occurs on the left and right. When `clipOrientation` is `"vertical"`, clipping occurs on the top and bottom. |
            | `fill` | Grow the horizontal and vertical size of the object if needed so it completely fills its container. No clipping occurs because the drawable fills the horizontal and vertical space (unless the drawable level is 0, in which case it's not visible). |
            | `clip_vertical` | Additional option that can be set to have the top and/or bottom edges of the child clipped to its container's bounds. The clip is based on the vertical gravity: a top gravity clips the bottom edge, a bottom gravity clips the top edge, and neither clips both edges. |
            | `clip_horizontal` | Additional option that can be set to have the left and/or right edges of the child clipped to its container's bounds. The clip is based on the horizontal gravity: a left gravity clips the right edge, a right gravity clips the left edge, and neither clips both edges. |


example:
    : XML file saved at `res/drawable/clip.xml`:  

    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <clip xmlns:android="http://schemas.android.com/apk/res/android"
        android:drawable="@drawable/android"
        android:clipOrientation="horizontal"
        android:gravity="left" />
    ```

    The following layout XML applies the clip drawable to a view:

    ```xml
    <ImageView
        android:id="@+id/image"
        android:src="@drawable/clip"
        android:layout_height="wrap_content"
        android:layout_width="wrap_content" />
    ```


    The following code gets the drawable and increases the amount of clipping to
    progressively reveal the image:

    ### Kotlin

    ```kotlin
    val imageview: ImageView = findViewById(R.id.image)
    val drawable: Drawable = imageview.background
    if (drawable is ClipDrawable) {
        drawable.level = drawable.level + 1000
    }
    ```

    ### Java

    ```java
    ImageView imageview = (ImageView) findViewById(R.id.image);
    Drawable drawable = imageview.getBackground();
    if (drawable instanceof ClipDrawable) {
        ((ClipDrawable)drawable).setLevel(drawable.getLevel() + 1000);
    }
    ```


    Increasing the level reduces the amount of clipping and slowly reveals the image. Here it is
    at a level of 7000:

    ![](https://developer.android.com/static/images/resources/clip.png)

    **Note:** The default level is 0, which is fully clipped so the image
    isn't visible. When the level is 10,000, the image isn't clipped and is completely visible.

see also:
:
    - [ClipDrawable](https://developer.android.com/reference/android/graphics/drawable/ClipDrawable)

## Scale drawable

A drawable defined in XML that changes the size of another drawable based on its current
level.

file location:
:   `res/drawable/`*filename*`.xml`  

    The filename is the resource ID

compiled resource datatype:
:   Resource pointer to a [ScaleDrawable](https://developer.android.com/reference/android/graphics/drawable/ScaleDrawable)

resource reference:
:
    In Java: `R.drawable.`*filename*  

    In XML: `@[`*package* `:]drawable/`*filename*

syntax:
:

    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <scale
        xmlns:android="http://schemas.android.com/apk/res/android"
        android:drawable="@drawable/drawable_resource"
        android:scaleGravity=["top" | "bottom" | "left" | "right" | "center_vertical" |
                              "fill_vertical" | "center_horizontal" | "fill_horizontal" |
                              "center" | "fill" | "clip_vertical" | "clip_horizontal"]
        android:scaleHeight="percentage"
        android:scaleWidth="percentage" />
    ```

elements:
:

    `<scale>`
    :   **Required.** Defines the scale drawable. This must be the root element.

        Attributes:

        `xmlns:android`
        :   *String* . **Required.** Defines the XML namespace, which must be
            `"http://schemas.android.com/apk/res/android"`.

        `android:drawable`
        :   *Drawable resource* . **Required**. Reference to a drawable
            resource.

        `android:scaleGravity`
        :   *Keyword* . Specifies the gravity position after scaling.

            Must be one or more of the following constant values, separated by `|`:

            | Value | Description |
            |---|---|
            | `top` | Put the object at the top of its container, not changing its size. |
            | `bottom` | Put the object at the bottom of its container, not changing its size. |
            | `left` | Put the object at the left edge of its container, not changing its size. This is the default. |
            | `right` | Put the object at the right edge of its container, not changing its size. |
            | `center_vertical` | Put the object in the vertical center of its container, not changing its size. |
            | `fill_vertical` | Grow the vertical size of the object if needed so it completely fills its container. |
            | `center_horizontal` | Put the object in the horizontal center of its container, not changing its size. |
            | `fill_horizontal` | Grow the horizontal size of the object if needed so it completely fills its container. |
            | `center` | Put the object in the center of its container in both the vertical and horizontal axis, not changing its size. |
            | `fill` | Grow the horizontal and vertical size of the object if needed so it completely fills its container. |
            | `clip_vertical` | Additional option that can be set to have the top and/or bottom edges of the child clipped to its container's bounds. The clip is based on the vertical gravity: a top gravity clips the bottom edge, a bottom gravity clips the top edge, and neither clips both edges. |
            | `clip_horizontal` | Additional option that can be set to have the left and/or right edges of the child clipped to its container's bounds. The clip is based on the horizontal gravity: a left gravity clips the right edge, a right gravity clips the left edge, and neither clips both edges. |

        `android:scaleHeight`
        :   *Percentage*. The scale height, expressed as a percentage of the drawable's
            bound. The value's format is XX%, such as 100% or 12.5%.

        `android:scaleWidth`
        :   *Percentage*. The scale width, expressed as a percentage of the drawable's
            bound. The value's format is XX%, such as 100% or 12.5%.


example:
:

    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <scale xmlns:android="http://schemas.android.com/apk/res/android"
        android:drawable="@drawable/logo"
        android:scaleGravity="center_vertical|center_horizontal"
        android:scaleHeight="80%"
        android:scaleWidth="80%" />
    ```

see also:
:
    - [ScaleDrawable](https://developer.android.com/reference/android/graphics/drawable/ScaleDrawable)

## Shape drawable

This is a generic shape defined in XML.

file location:
:   `res/drawable/`*filename*`.xml`  

    The filename is the resource ID

compiled resource datatype:
:   Resource pointer to a [GradientDrawable](https://developer.android.com/reference/android/graphics/drawable/GradientDrawable)

resource reference:
:
    In Java: `R.drawable.`*filename*  

    In XML: `@[`*package* `:]drawable/`*filename*

syntax:
:

    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <shape
        xmlns:android="http://schemas.android.com/apk/res/android"
        android:shape=["rectangle" | "oval" | "line" | "ring"] >
        <corners
            android:radius="integer"
            android:topLeftRadius="integer"
            android:topRightRadius="integer"
            android:bottomLeftRadius="integer"
            android:bottomRightRadius="integer" />
        <gradient
            android:angle="integer"
            android:centerX="float"
            android:centerY="float"
            android:centerColor="integer"
            android:endColor="color"
            android:gradientRadius="integer"
            android:startColor="color"
            android:type=["linear" | "radial" | "sweep"]
            android:useLevel=["true" | "false"] />
        <padding
            android:left="integer"
            android:top="integer"
            android:right="integer"
            android:bottom="integer" />
        <size
            android:width="integer"
            android:height="integer" />
        <solid
            android:color="color" />
        <stroke
            android:width="integer"
            android:color="color"
            android:dashWidth="integer"
            android:dashGap="integer" />
    </shape>
    ```

elements:
:

    `<shape>`
    :   **Required.** The shape drawable. This must be the root element.

        Attributes:

        `xmlns:android`
        :   *String* . **Required.** Defines the XML namespace, which must be
            `"http://schemas.android.com/apk/res/android"`.

        `android:shape`
        :   *Keyword* . Defines the type of shape. Valid values are:

            | Value | Description |
            |---|---|
            | `"rectangle"` | A rectangle that fills the containing view. This is the default shape. |
            | `"oval"` | An oval shape that fits the dimensions of the containing view. |
            | `"line"` | A horizontal line that spans the width of the containing view. This shape requires the `<stroke>` element to define the width of the line. |
            | `"ring"` | A ring shape. |


        The following attributes are used only when `android:shape="ring"`:

        `android:innerRadius`
        :   *Dimension* . The radius for the
            inner part of the ring (the hole in the middle), as a dimension value or [dimension resource](https://developer.android.com/guide/topics/resources/more-resources#Dimension).

        `android:innerRadiusRatio`
        :   *Float* . The radius for the inner
            part of the ring, expressed as a ratio of the ring's width. For instance, if `android:innerRadiusRatio="5"`, then the inner radius equals the ring's width divided by 5. This
            value is overridden by `android:innerRadius`. The default value is 9.

        `android:thickness`
        :   *Dimension* . The thickness of the
            ring, as a dimension value or [dimension resource](https://developer.android.com/guide/topics/resources/more-resources#Dimension).

        `android:thicknessRatio`
        :   *Float* . The thickness of the ring
            expressed as a ratio of the ring's width. For instance, if `android:thicknessRatio="2"`, then
            the thickness equals the ring's width divided by 2. This value is overridden by `android:innerRadius`. The default value is 3.

        `android:useLevel`
        :   *Boolean* . True if this is used as
            a [LevelListDrawable](https://developer.android.com/reference/android/graphics/drawable/LevelListDrawable). This normally is false,
            or else your shape might not appear.

    `<corners>`

    :   Creates rounded corners for the shape. Applies only when the shape is a rectangle. Attributes:

        `android:radius`
        :   *Dimension* . The radius for all corners, as a dimension value or [dimension resource](https://developer.android.com/guide/topics/resources/more-resources#Dimension). This is overridden for each
            corner by the following attributes.

        `android:topLeftRadius`
        :   *Dimension* . The radius for the top-left corner, as a dimension value or [dimension resource](https://developer.android.com/guide/topics/resources/more-resources#Dimension).

        `android:topRightRadius`
        :   *Dimension* . The radius for the top-right corner, as a dimension value or [dimension resource](https://developer.android.com/guide/topics/resources/more-resources#Dimension).

        `android:bottomLeftRadius`
        :   *Dimension* . The radius for the bottom-left corner, as a dimension value or [dimension resource](https://developer.android.com/guide/topics/resources/more-resources#Dimension).

        `android:bottomRightRadius`
        :   *Dimension* . The radius for the bottom-right corner, as a dimension value or [dimension resource](https://developer.android.com/guide/topics/resources/more-resources#Dimension).

        **Note:** Every corner must initially be provided a corner
        radius greater than 1, or else no corners are rounded. If you want specific corners
        to *not* be rounded, a workaround is to use `android:radius` to set a default corner
        radius greater than 1 and then override every corner with the values you really
        want, providing 0 ("0dp") where you don't want rounded corners.

    `<gradient>`

    :   Specifies a gradient color for the shape. Attributes:

        `android:angle`
        :   *Integer*. The angle for the gradient, in degrees. 0 is left to right, 90 is
            bottom to top. It must be a multiple of 45. The default is 0.

        `android:centerX`
        :   *Float*. The relative X-position for the center of the gradient (0 - 1.0).

        `android:centerY`
        :   *Float*. The relative Y-position for the center of the gradient (0 - 1.0).

        `android:centerColor`
        :   *Color* . Optional color that comes between the start and end colors, as a
            hexadecimal value or [color resource](https://developer.android.com/guide/topics/resources/more-resources#Color).

        `android:endColor`
        :   *Color* . The ending color, as a hexadecimal
            value or [color resource](https://developer.android.com/guide/topics/resources/more-resources#Color).

        `android:gradientRadius`
        :   *Float* . The radius for the gradient. Only applied when `android:type="radial"`.

        `android:startColor`
        :   *Color* . The starting color, as a hexadecimal
            value or [color resource](https://developer.android.com/guide/topics/resources/more-resources#Color).

        `android:type`
        :   *Keyword* . The type of gradient pattern to apply. Valid values are:

            | Value | Description |
            |---|---|
            | `"linear"` | A linear gradient. This is the default. |
            | `"radial"` | A radial gradient. The start color is the center color. |
            | `"sweep"` | A sweeping line gradient. |


        `android:useLevel`
        :   *Boolean* . True if this is used as a [LevelListDrawable](https://developer.android.com/reference/android/graphics/drawable/LevelListDrawable).

    `<padding>`

    :   Padding to apply to the containing view element. This pads the position of the view content, not the shape. Attributes:

        `android:left`
        :   *Dimension* . Left padding, as a dimension value or [dimension resource](https://developer.android.com/guide/topics/resources/more-resources#Dimension).

        `android:top`
        :   *Dimension* . Top padding, as a dimension value or [dimension resource](https://developer.android.com/guide/topics/resources/more-resources#Dimension).

        `android:right`
        :   *Dimension* . Right padding, as a dimension value or [dimension resource](https://developer.android.com/guide/topics/resources/more-resources#Dimension).

        `android:bottom`
        :   *Dimension* . Bottom padding, as a dimension value or [dimension resource](https://developer.android.com/guide/topics/resources/more-resources#Dimension).

    `<size>`

    :   The size of the shape. Attributes:

        `android:height`
        :   *Dimension* . The height of the shape, as a dimension value or [dimension resource](https://developer.android.com/guide/topics/resources/more-resources#Dimension).

        `android:width`
        :   *Dimension* . The width of the shape, as a dimension value or [dimension resource](https://developer.android.com/guide/topics/resources/more-resources#Dimension).

        **Note:** By default, the shape scales to the size of the container
        view proportionate to the dimensions defined here. When you use the shape in an [ImageView](https://developer.android.com/reference/android/widget/ImageView), you can restrict scaling by setting the [`android:scaleType`](https://developer.android.com/reference/android/widget/ImageView#attr_android:scaleType) to `"center"`.

    `<solid>`

    :   A solid color to fill the shape. Attributes:

        `android:color`
        :   *Color* . The color to apply to the shape, as a hexadecimal
            value or [color resource](https://developer.android.com/guide/topics/resources/more-resources#Color).

    `<stroke>`

    :   A stroke line for the shape. Attributes:

        `android:width`
        :   *Dimension* . The thickness of the line, as a dimension value or [dimension resource](https://developer.android.com/guide/topics/resources/more-resources#Dimension).

        `android:color`
        :   *Color* . The color of the line, as a
            hexadecimal value or [color resource](https://developer.android.com/guide/topics/resources/more-resources#Color).

        `android:dashGap`
        :   *Dimension* . The distance between line dashes, as a dimension value or [dimension resource](https://developer.android.com/guide/topics/resources/more-resources#Dimension). Only valid if `android:dashWidth` is set.

        `android:dashWidth`
        :   *Dimension* . The size of each dash line, as a dimension value or [dimension resource](https://developer.android.com/guide/topics/resources/more-resources#Dimension). Only valid if `android:dashGap` is set.

example:
    : XML file saved at `res/drawable/gradient_box.xml`:  

    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <shape xmlns:android="http://schemas.android.com/apk/res/android"
        android:shape="rectangle">
        <gradient
            android:startColor="#FFFF0000"
            android:endColor="#80FF00FF"
            android:angle="45"/>
        <padding android:left="7dp"
            android:top="7dp"
            android:right="7dp"
            android:bottom="7dp" />
        <corners android:radius="8dp" />
    </shape>
    ```


    This layout XML applies the shape drawable to a view:

    ```xml
    <TextView
        android:background="@drawable/gradient_box"
        android:layout_height="wrap_content"
        android:layout_width="wrap_content" />
    ```


    This application code gets the shape drawable and applies it to a view:

    ### Kotlin

        val shape: Drawable? = https://developer.android.com/reference/androidx/core/content/res/ResourcesCompat#getDrawable(android.content.res.Resources, int, android.content.res.Resources.Theme)(https://developer.android.com/reference/android/content/Context#getResources(), R.drawable.gradient_box, https://developer.android.com/reference/android/content/Context#getTheme())

        val tv: TextView = findViewById(R.id.textview)
        tv.background = shape

    ### Java

        Resources res = https://developer.android.com/reference/android/content/Context#getResources();
        Drawable shape = ResourcesCompat.https://developer.android.com/reference/androidx/core/content/res/ResourcesCompat#getDrawable(android.content.res.Resources, int, android.content.res.Resources.Theme)(res, R.drawable.gradient_box, https://developer.android.com/reference/android/content/Context#getTheme());

        TextView tv = (TextView)findViewById(R.id.textview);
        tv.setBackground(shape);


see also:
:
    - [ShapeDrawable](https://developer.android.com/reference/android/graphics/drawable/ShapeDrawable)