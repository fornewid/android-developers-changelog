---
title: Layout resource  |  App architecture  |  Android Developers
url: https://developer.android.com/guide/topics/resources/layout-resource
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [App architecture](https://developer.android.com/topic/architecture/intro)

# Layout resource Stay organized with collections Save and categorize content based on your preferences.




A layout resource defines the architecture for the UI in an `Activity` or a
component of a UI.

file location:
:   `res/layout/filename.xml`  
    The filename is used as the resource ID.

compiled resource datatype:
:   Resource pointer to a `View` (or subclass) resource

resource reference:
:   In Java: `R.layout.filename`  
    In XML: `@[package:]layout/filename`

syntax:
:   ```
    <?xml version="1.0" encoding="utf-8"?>
    <ViewGroup
        xmlns:android="http://schemas.android.com/apk/res/android"
        android:id="@[+][package:]id/resource_name"
        android:layout_height=["dimension" | "match_parent" | "wrap_content"]
        android:layout_width=["dimension" | "match_parent" | "wrap_content"]
        [ViewGroup-specific attributes] >
        <View
            android:id="@[+][package:]id/resource_name"
            android:layout_height=["dimension" | "match_parent" | "wrap_content"]
            android:layout_width=["dimension" | "match_parent" | "wrap_content"]
            [View-specific attributes] >
            <requestFocus/>
        </View>
        <ViewGroup >
            <View />
        </ViewGroup>
        <include layout="@layout/layout_resource"/>
    </ViewGroup>
    ```

    **Note:** The root element can be a
    `ViewGroup`, a `View`, or a [`<merge>`](#merge-element) element, but there can be only
    one root element and it must contain the `xmlns:android` attribute with the `android`
    namespace as shown in the preceding syntax example.

elements:
:   `<ViewGroup>`
    :   A container for other `View` elements. There are many
        different kinds of `ViewGroup` objects, and each one lets you
        specify the layout of the child elements in different ways. Different kinds of
        `ViewGroup` objects include `LinearLayout`,
        `RelativeLayout`, and `FrameLayout`.

        Don't assume that any derivation of `ViewGroup`
        accepts nested views. Some view groups
        are implementations of the `AdapterView` class, which determines
        its children only from an `Adapter`.

        Attributes:

        `android:id`
        :   *Resource ID*. A unique resource name for the element, which you can
            use to obtain a reference to the `ViewGroup` from your application. For more
            information, see the [Value for android:id](#idvalue) section.

        `android:layout_height`
        :   *Dimension or keyword*. **Required**. The height for the group, as a
            dimension value (or
            [dimension resource](/guide/topics/resources/more-resources#Dimension)) or a keyword
            (`"match_parent"` or `"wrap_content"`). For more information,
            see the [Values for android:layout\_height and
            android:layout\_width](#layoutvalues) section.

        `android:layout_width`
        :   *Dimension or keyword*. **Required**. The width for the group, as a
            dimension value (or
            [dimension resource](/guide/topics/resources/more-resources#Dimension)) or a keyword
            (`"match_parent"` or `"wrap_content"`). For more information,
            see the [Values for android:layout\_height and
            android:layout\_width](#layoutvalues) section.

        The `ViewGroup`
        base class supports more attributes, and many more are supported by each implementation of
        `ViewGroup`. For a reference of all available attributes,
        see the corresponding reference documentation for the `ViewGroup` class,
        for example, the [`LinearLayout` XML
        attributes](/reference/android/widget/LinearLayout#lattrs).

    `<View>`
    :   An individual UI component, generally referred to as a *widget*. Different
        kinds of `View` objects include `TextView`,
        `Button`, and `CheckBox`.

        Attributes:

        `android:id`
        :   *Resource ID*. A unique resource name for the element, which you can use to
            obtain a reference to the `View` from your application. For more
            information, see the [Value for android:id](#idvalue) section.

        `android:layout_height`
        :   *Dimension or keyword*. **Required**. The height for the element, as
            a dimension value (or
            [dimension resource](/guide/topics/resources/more-resources#Dimension)) or a keyword
            (`"match_parent"` or `"wrap_content"`). For more information,
            see the [Values for android:layout\_height and
            android:layout\_width](#layoutvalues) section.

        `android:layout_width`
        :   *Dimension or keyword*. **Required**. The width for the element, as
            a dimension value (or
            [dimension resource](/guide/topics/resources/more-resources#Dimension)) or a keyword
            (`"match_parent"` or `"wrap_content"`). For more information,
            see the [Values for android:layout\_height and
            android:layout\_width](#layoutvalues) section.

        The `View`
        base class supports more attributes, and many more are supported by each implementation of
        `View`. For more information, read [Layouts](/guide/topics/ui/declaring-layout). For
        a reference of all available attributes,
        see the corresponding reference documentation, for example, the [`TextView` XML attributes](/reference/android/widget/TextView#lattrs).

    `<requestFocus>`
    :   Any element representing a `View` object can include this empty element,
        which gives its parent initial focus on the screen. You can have only one of these
        elements per file.

    `<include>`
    :   Includes a layout file into this layout.

        Attributes:

        `layout`
        :   *Layout resource*. **Required**. Reference to a layout
            resource.

        `android:id`
        :   *Resource ID*. Overrides the ID given to the root view in the included layout.

        `android:layout_height`
        :   *Dimension or keyword*. Overrides the height given to the root view in the
            included layout. Only effective if `android:layout_width` is also declared.

        `android:layout_width`
        :   *Dimension or keyword*. Overrides the width given to the root view in the
            included layout. Only effective if `android:layout_height` is also declared.

        You can include any other layout attributes in the `<include>` that are
        supported by the root element in the included layout and they override those defined in the
        root element.

        **Caution:** If you want to override layout attributes using
        the `<include>` tag, you must override both
        `android:layout_height` and `android:layout_width` in order for
        other layout attributes to take effect.

        Another way to include a layout is to use `ViewStub`: a lightweight
        view that consumes no layout space until you explicitly inflate it. When you do, it includes a
        layout file defined by its `android:layout` attribute. For more information about using `ViewStub`, read [Load
        views on demand](/develop/ui/views/layout/improving-layouts/loading-ondemand).

    `<merge>`
    :   An alternative root element that isn't drawn in the layout hierarchy. Using this as the
        root element is useful when you know that this layout is placed into a layout
        that already contains the appropriate parent `View` to contain the children of the
        `<merge>` element.

        This is particularly useful when you plan to include this layout
        in another layout file using [`<include>`](#include-element) and
        this layout doesn't require a different `ViewGroup` container. For more
        information about merging layouts, read [Reuse layouts with <include>](/develop/ui/views/layout/improving-layouts/reusing-layouts).

    #### Value for android:id

    For the ID value, you typically use this syntax form: `"@+id/name"`, as shown in the following example. The
    plus symbol, `+`, indicates that this is a new resource ID, and the `aapt` tool creates
    a new resource integer in the `R.java` class, if it doesn't already exist.

    ```
    <TextView android:id="@+id/nameTextbox"/>
    ```

    The `nameTextbox` name is now a resource ID attached to this element. You can then
    refer to the `TextView` to which the ID is associated in Java:

    ### Kotlin

    ```
    val textView: TextView? = findViewById(R.id.nameTextbox)
    ```

    ### Java

    ```
    TextView textView = findViewById(R.id.nameTextbox);
    ```

    This code returns the `TextView` object.

    However, if you have already defined an [ID resource](/guide/topics/resources/drawable-resource#Id), and it isn't
    already used, then you can apply that ID to a `View` element by excluding the
    plus symbol in the `android:id` value.

    #### Values for android:layout\_height and android:layout\_width

    The height and width values are expressed using any of the
    [dimension
    units](/guide/topics/resources/more-resources#Dimension) supported by Android (px, dp, sp, pt, in, mm) or with the following keywords:

    | Value | Description |
    | --- | --- |
    | `match_parent` | Sets the dimension to match that of the parent element. Added in API level 8 to deprecate `fill_parent`. |
    | `wrap_content` | Sets the dimension only to the size required to fit the content of this element. |

    #### Custom view elements

    You can create custom `View` and `ViewGroup`
    elements and apply them to your layout the same as a standard layout
    element. You can also specify the attributes supported in the XML element. For more information,
    see [Create custom view components](/guide/topics/ui/custom-components).

example:
:   XML file saved at `res/layout/main_activity.xml`:

    ```
    <?xml version="1.0" encoding="utf-8"?>
    <LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
                  android:layout_width="match_parent"
                  android:layout_height="match_parent"
                  android:orientation="vertical" >
        <TextView android:id="@+id/text"
                  android:layout_width="wrap_content"
                  android:layout_height="wrap_content"
                  android:text="Hello, I am a TextView" />
        <Button android:id="@+id/button"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="Hello, I am a Button" />
    </LinearLayout>
    ```

    This application code loads the layout for an `Activity` in the
    `onCreate()` method::   ### Kotlin

        ```
        public override fun onCreate(savedInstanceState: Bundle?) {
            super.onCreate(savedInstanceState)
            setContentView(R.layout.main_activity)
        }
        ```

        ### Java

        ```
        public void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            setContentView(R.layout.main_activity);
        }
        ```

    see also:
    :   * [Layouts](/guide/topics/ui/declaring-layout)
        * `View`
        * `ViewGroup`

[Previous

arrow\_back

Drawable](/guide/topics/resources/drawable-resource)

[Next

Menu

arrow\_forward](/guide/topics/resources/menu-resource)