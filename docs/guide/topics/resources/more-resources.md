---
title: https://developer.android.com/guide/topics/resources/more-resources
url: https://developer.android.com/guide/topics/resources/more-resources
source: md.txt
---

This page defines the following types of resources that you can externalize:

[Bool](https://developer.android.com/guide/topics/resources/more-resources#Bool)
:   XML resource that carries a boolean value.

[Color](https://developer.android.com/guide/topics/resources/more-resources#Color)
:   XML resource that carries a color value (a hexadecimal color).

[Dimension](https://developer.android.com/guide/topics/resources/more-resources#Dimension)
:   XML resource that carries a dimension value (with a unit of measure).

[ID](https://developer.android.com/guide/topics/resources/more-resources#Id)
:   XML resource that provides a unique identifier for application resources and components.

[Integer](https://developer.android.com/guide/topics/resources/more-resources#Integer)
:   XML resource that carries an integer value.

[Integer array](https://developer.android.com/guide/topics/resources/more-resources#IntegerArray)
:   XML resource that provides an array of integers.

[Typed array](https://developer.android.com/guide/topics/resources/more-resources#TypedArray)
:   XML resource that provides a[TypedArray](https://developer.android.com/reference/android/content/res/TypedArray)(which you can use for an array of drawables).

## Bool

A boolean value defined in XML.

**Note:** A bool is a simple resource that is referenced using the value provided in the`name`attribute, not the name of the XML file. As such, you can combine bool resources with other simple resources in one XML file, under one`<resources>`element.

file location:
:   `res/values/`*filename*`.xml`  
    The filename is arbitrary. The`<bool>`element's`name`is used as the resource ID.

resource reference:
:   In Java:`R.bool.`*bool_name*  
    In XML:`@[`*package* `:]bool/`*bool_name*

syntax:
:

    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <resources>
        <bool
            name="bool_name"
            >[true | false]</bool>
    </resources>
    ```

elements:
:

    `<resources>`
    :   **Required.** This is the root node.

        No attributes.

    `<bool>`
    :   A boolean value:`true`or`false`.

        Attributes:

        `name`
        :   *String*. A name for the bool value. This is used as the resource ID.

example:
:   XML file saved at`res/values-small/bools.xml`:  

    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <resources>
        <bool name="screen_small">true</bool>
        <bool name="adjust_view_bounds">true</bool>
    </resources>
    ```

    The following application code retrieves the boolean:  

    ### Kotlin

        val screenIsSmall: Boolean = https://developer.android.com/reference/android/content/Context#getResources().https://developer.android.com/reference/android/content/res/Resources#getBoolean(int)(R.bool.screen_small)

    ### Java

        Resources res = https://developer.android.com/reference/android/content/Context#getResources();
        boolean screenIsSmall = res.https://developer.android.com/reference/android/content/res/Resources#getBoolean(int)(R.bool.screen_small);

    The following layout XML uses the boolean for an attribute:  

    ```xml
    <ImageView
        android:layout_height="fill_parent"
        android:layout_width="fill_parent"
        android:src="@drawable/logo"
        android:adjustViewBounds="@bool/adjust_view_bounds" />
    ```

## Color

A color value defined in XML. The color is specified using an RGB value and alpha channel. You can use a color resource any place that accepts a hexadecimal color value. You can also use a color resource when a drawable resource is expected in XML, such as`android:drawable="@color/green"`.

The value always begins with a pound (#) character, which is followed by the Alpha-Red-Green-Blue information in one of the following formats:

- #*RGB*
- #*ARGB*
- #*RRGGBB*
- #*AARRGGBB*

**Note:** A color is a simple resource that is referenced using the value provided in the`name`attribute, not the name of the XML file. As such, you can combine color resources with other simple resources in one XML file, under one`<resources>`element.

file location:
:   `res/values/colors.xml`  
    The filename is arbitrary. The`<color>`element's`name`is used as the resource ID.

resource reference:
:   In Java:`R.color.`*color_name*  
    In XML:`@[`*package* `:]color/`*color_name*

syntax:
:

    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <resources>
        <color
            name="color_name"
            >hex_color</color>
    </resources>
    ```

elements:
:

    `<resources>`
    :   **Required.** This is the root node.

        No attributes.

    `<color>`

    :   A color expressed in hexadecimal.Attributes:

        `name`
        :   *String*. A name for the color. This is used as the resource ID.

example:
:   XML file saved at`res/values/colors.xml`:  

    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <resources>
       <color name="opaque_red">#f00</color>
       <color name="translucent_red">#80ff0000</color>
    </resources>
    ```

    The following application code retrieves the color resource:  

    ### Kotlin

        val color: Int = https://developer.android.com/reference/android/content/Context#getResources().https://developer.android.com/reference/android/content/res/Resources#getColor(int)(R.color.opaque_red)

    ### Java

        Resources res = https://developer.android.com/reference/android/content/Context#getResources();
        int color = res.https://developer.android.com/reference/android/content/res/Resources#getColor(int,%20android.content.res.Resources.Theme)(R.color.opaque_red);

    The following layout XML applies the color to an attribute:  

    ```xml
    <TextView
        android:layout_width="fill_parent"
        android:layout_height="wrap_content"
        android:textColor="@color/translucent_red"
        android:text="Hello"/>
    ```

## Dimension

A dimension value defined in XML. A dimension is specified with a number followed by a unit of measure, such as 10px, 2in, or 5sp. The following units of measure are supported by Android:

`dp`

:   Density-independent pixels: an abstract unit that is based on the physical density of the screen. These units are relative to a 160 dpi (dots per inch) screen, on which 1 dp is roughly equal to 1 px. When running on a higher density screen, the number of pixels used to draw 1 dp is scaled up by a factor appropriate for the screen's dpi.<br />

    Likewise, when on a lower-density screen, the number of pixels used for 1 dp is scaled down. The ratio of dps to pixels changes with the screen density, but not necessarily in direct proportion. Using dp units instead of px units is a solution to making the view dimensions in your layout resize properly for different screen densities. It provides consistency for the real-world sizes of your UI elements across different devices.

`sp`
:   Scale-independent Pixels - This is like the dp unit, but it is also scaled by the user's font size preference. It is recommend you use this unit when specifying font sizes, so they will be adjusted for both the screen density and the user's preference.

`pt`
:   Points: 1/72 of an inch based on the physical size of the screen, assuming a 72 dpi density screen.

`px`
:   Pixels: corresponds to actual pixels on the screen. We don't recommend using this unit, because the actual representation can vary across devices. Different devices can have a different number of pixels per inch and might have more or fewer total pixels available on the screen.

`mm`
:   Millimeters: based on the physical size of the screen.

`in`
:   Inches: based on the physical size of the screen.

**Note:** A dimension is a simple resource that is referenced using the value provided in the`name`attribute, not the name of the XML file. As such, you can combine dimension resources with other simple resources in one XML file, under one`<resources>`element.

file location:
:   `res/values/`*filename*`.xml`  
    The filename is arbitrary. The`<dimen>`element's`name`is used as the resource ID.

resource reference:
:   In Java:`R.dimen.`*dimension_name*  
    In XML:`@[`*package* `:]dimen/`*dimension_name*

syntax:
:

    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <resources>
        <dimen
            name="dimension_name"
            >dimension</dimen>
    </resources>
    ```

elements:
:

    `<resources>`
    :   **Required.** This is the root node.

        No attributes.

    `<dimen>`

    :   A dimension, represented by a float followed by a unit of measurement (dp, sp, pt, px, mm, in).Attributes:

        `name`
        :   *String*. A name for the dimension. This is used as the resource ID.

example:
:   XML file saved at`res/values/dimens.xml`:  

    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <resources>
        <dimen name="textview_height">25dp</dimen>
        <dimen name="textview_width">150dp</dimen>
        <dimen name="ball_radius">30dp</dimen>
        <dimen name="font_size">16sp</dimen>
    </resources>
    ```

    The following application code retrieves a dimension:  

    ### Kotlin

        val fontSize: Float = https://developer.android.com/reference/android/content/Context#getResources().https://developer.android.com/reference/android/content/res/Resources#getDimension(int)(R.dimen.font_size)

    ### Java

        Resources res = https://developer.android.com/reference/android/content/Context#getResources();
        float fontSize = res.https://developer.android.com/reference/android/content/res/Resources#getDimension(int)(R.dimen.font_size);

    The following layout XML applies dimensions to attributes:  

    ```xml
    <TextView
        android:layout_height="@dimen/textview_height"
        android:layout_width="@dimen/textview_width"
        android:textSize="@dimen/font_size"/>
    ```

## ID

A unique resource ID defined in XML. Using the name you provide in the`<item>`element, the Android developer tools create a unique integer in your project's`R.java`class, which you can use as an identifier for an application resources, such as a[View](https://developer.android.com/reference/android/view/View)in your UI layout, or a unique integer for use in your application code, such as an ID for a dialog or a result code.

**Note:** An ID is a simple resource that is referenced using the value provided in the`name`attribute, not the name of the XML file. As such, you can combine ID resources with other simple resources in one XML file, under one`<resources>`element. Also, an ID resource doesn't reference an actual resource item: it is a unique ID that you can attach to other resources or use as a unique integer in your application.

file location:
:   `res/values/`*filename.xml*  
    The filename is arbitrary.

resource reference:
:   In Java:`R.id.`*name*  
    In XML:`@[`*package* `:]id/`*name*

syntax:
:

    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <resources>
        <item
            type="id"
            name="id_name" />
    </resources>
    ```

elements:
:

    `<resources>`
    :   **Required.** This is the root node.

        No attributes.

    `<item>`

    :   Defines a unique ID. Takes no value, only attributes.Attributes:

        `type`
        :   Must be`"id"`.

        `name`
        :   *String*. A unique name for the ID.

example:

:   XML file saved at`res/values/ids.xml`:

    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <resources>
        <item type="id" name="button_ok" />
        <item type="id" name="dialog_exit" />
    </resources>
    ```

    The following layout snippet uses the`"button_ok"`ID for a`Button`widget:  

    ```xml
    <Button android:id="@id/button_ok"
        style="@style/button_style" />
    ```

    The`android:id`value here doesn't include the plus sign in the ID reference, because the ID already exists, as defined in the preceding`ids.xml`example. When you specify an ID to an XML resource using the plus sign, in the format`android:id="@+id/name"`, that means that the`"name"`ID doesn't yet exist, and it is created.

    As another example, the following code snippet uses the`"dialog_exit"`ID as a unique identifier for a dialog:  

    ### Kotlin

        https://developer.android.com/reference/android/app/Activity#showDialog(int)(R.id.dialog_exit)

    ### Java

        https://developer.android.com/reference/android/app/Activity#showDialog(int)(R.id.dialog_exit);

    In the same application, the`"dialog_exit"`ID is compared when creating a dialog:  

    ### Kotlin

        override fun https://developer.android.com/reference/android/app/Activity#onCreateDialog(int)(id: Int): Dialog? {
            return when(id) {
                R.id.dialog_exit -> {
                    ...
                }
                else -> {
                    null
                }
            }
        }

    ### Java

        protected Dialog https://developer.android.com/reference/android/app/Activity#onCreateDialog(int)(int id) {
            Dialog dialog;
            switch(id) {
            case R.id.dialog_exit:
                ...
                break;
            default:
                dialog = null;
            }
            return dialog;
        }

## Integer

An integer defined in XML.

**Note:** An integer is a simple resource that is referenced using the value provided in the`name`attribute, not the name of the XML file. As such, you can combine integer resources with other simple resources in one XML file, under one`<resources>`element.

file location:
:   `res/values/`*filename.xml*  
    The filename is arbitrary. The`<integer>`element's`name`is used as the resource ID.

resource reference:
:   In Java:`R.integer.`*integer_name*  
    In XML:`@[`*package* `:]integer/`*integer_name*

syntax:
:

    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <resources>
        <integer
            name="integer_name"
            >integer</integer>
    </resources>
    ```

elements:
:

    `<resources>`
    :   **Required.** This is the root node.

        No attributes.

    `<integer>`

    :   An integer.Attributes:

        `name`
        :   *String*. A name for the integer. This is used as the resource ID.

example:

:   XML file saved at`res/values/integers.xml`:

    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <resources>
        <integer name="max_speed">75</integer>
        <integer name="min_speed">5</integer>
    </resources>
    ```

    The following application code retrieves an integer:  

    ### Kotlin

        val maxSpeed: Int = https://developer.android.com/reference/android/content/Context#getResources().https://developer.android.com/reference/android/content/res/Resources#getInteger(int)(R.integer.max_speed)

    ### Java

        Resources res = https://developer.android.com/reference/android/content/Context#getResources();
        int maxSpeed = res.https://developer.android.com/reference/android/content/res/Resources#getInteger(int)(R.integer.max_speed);

## Integer array

An array of integers defined in XML.

**Note:** An integer array is a simple resource that is referenced using the value provided in the`name`attribute, not the name of the XML file. As such, you can combine integer array resources with other simple resources in one XML file, under one`<resources>`element.

file location:
:   `res/values/`*filename*`.xml`  
    The filename is arbitrary. The`<integer-array>`element's`name`is used as the resource ID.

compiled resource datatype:
:   Resource pointer to an array of integers.

resource reference:
:   In Java:`R.array.`*integer_array_name*  
    In XML:`@[`*package* `:]array/`*integer_array_name*

syntax:
:

    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <resources>
        <integer-array
            name="integer_array_name">
            <item
                >integer</item>
        </integer-array>
    </resources>
    ```

elements:
:

    `<resources>`
    :   **Required.** This is the root node.

        No attributes.

    `<integer-array>`
    :   Defines an array of integers. Contains one or more child`<item>`elements.

        Attributes:

        `android:name`
        :   *String*. A name for the array. This name is used as the resource ID to reference the array.

    `<item>`
    :   An integer. The value can be a reference to another integer resource. Must be a child of an`<integer-array>`element.

        No attributes.

example:
:   XML file saved at`res/values/integers.xml`:  

    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <resources>
        <integer-array name="bits">
            <item>4</item>
            <item>8</item>
            <item>16</item>
            <item>32</item>
        </integer-array>
    </resources>
    ```

    The following application code retrieves the integer array:  

    ### Kotlin

        val bits: IntArray = https://developer.android.com/reference/android/content/Context#getResources().https://developer.android.com/reference/android/content/res/Resources#getIntArray(int)(R.array.bits)

    ### Java

        Resources res = https://developer.android.com/reference/android/content/Context#getResources();
        int[] bits = res.https://developer.android.com/reference/android/content/res/Resources#getIntArray(int)(R.array.bits);

## Typed array

A[TypedArray](https://developer.android.com/reference/android/content/res/TypedArray)defined in XML. You can use this to create an array of other resources, such as drawables. The array isn't required to be homogeneous, so you can create an array of mixed resource types, but be aware of what and where the data types are in the array so that you can properly obtain each item with the`TypedArray`class's`get...()`methods.

**Note:** A typed array is a simple resource that is referenced using the value provided in the`name`attribute, not the name of the XML file. As such, you can combine typed array resources with other simple resources in one XML file, under one`<resources>`element.

file location:
:   `res/values/`*filename*`.xml`  
    The filename is arbitrary. The`<array>`element's`name`is used as the resource ID.

compiled resource datatype:
:   Resource pointer to a[TypedArray](https://developer.android.com/reference/android/content/res/TypedArray).

resource reference:
:   In Java:`R.array.`*array_name*  
    In XML:`@[`*package* `:]array/`*array_name*

syntax:
:

    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <resources>
        <array
            name="integer_array_name">
            <item>resource</item>
        </array>
    </resources>
    ```

elements:
:

    `<resources>`
    :   **Required.** This is the root node.

        No attributes.

    `<array>`
    :   Defines an array. Contains one or more child`<item>`elements.

        Attributes:

        `android:name`
        :   *String*. A name for the array. This name is used as the resource ID to reference the array.

    `<item>`
    :   A generic resource. The value can be a reference to a resource or a simple data type. Must be a child of an`<array>`element.

        No attributes.

example:
:   XML file saved at`res/values/arrays.xml`:  

    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <resources>
        <array name="icons">
            <item>@drawable/home</item>
            <item>@drawable/settings</item>
            <item>@drawable/logout</item>
        </array>
        <array name="colors">
            <item>#FFFF0000</item>
            <item>#FF00FF00</item>
            <item>#FF0000FF</item>
        </array>
    </resources>
    ```

    The following application code retrieves each array and then obtains the first entry in each array:  

    ### Kotlin

        val icons: TypedArray = https://developer.android.com/reference/android/content/Context#getResources().https://developer.android.com/reference/android/content/res/Resources#obtainTypedArray(int)(R.array.icons)
        val drawable: Drawable = icons.https://developer.android.com/reference/android/content/res/TypedArray#getDrawable(int)(0)

        val colors: TypedArray = https://developer.android.com/reference/android/content/Context#getResources().https://developer.android.com/reference/android/content/res/Resources#obtainTypedArray(int)(R.array.colors)
        val color: Int = colors.https://developer.android.com/reference/android/content/res/TypedArray#getColor(int, int)(0,0)

    ### Java

        Resources res = https://developer.android.com/reference/android/content/Context#getResources();
        TypedArray icons = res.https://developer.android.com/reference/android/content/res/Resources#obtainTypedArray(int)(R.array.icons);
        Drawable drawable = icons.https://developer.android.com/reference/android/content/res/TypedArray#getDrawable(int)(0);

        TypedArray colors = res.https://developer.android.com/reference/android/content/res/Resources#obtainTypedArray(int)(R.array.colors);
        int color = colors.https://developer.android.com/reference/android/content/res/TypedArray#getColor(int, int)(0,0);