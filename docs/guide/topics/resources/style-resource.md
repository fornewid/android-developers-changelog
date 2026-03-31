---
title: Style resource  |  App architecture  |  Android Developers
url: https://developer.android.com/guide/topics/resources/style-resource
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [App architecture](https://developer.android.com/topic/architecture/intro)

# Style resource Stay organized with collections Save and categorize content based on your preferences.




A style resource defines the format and look for a UI.
A style can be applied to an individual `View` (from within a layout file) or to
an entire `Activity` or application (from within the manifest file).

For more information about creating and applying styles, please read
[Styles and Themes](/guide/topics/ui/themes).

**Note:** A style is a simple resource that is referenced
using the value provided in the `name` attribute (not the name of the XML file). As
such, you can combine style resources with other simple resources in the one XML file,
under one `<resources>` element.

file location:
:   `res/values/filename.xml`  
    The filename is arbitrary. The element's `name` will be used as the resource ID.

resource reference:
:   In XML: `@[package:]style/style_name`

syntax:
:   ```
    <?xml version="1.0" encoding="utf-8"?>
    <resources>
        <style
            name="style_name"
            parent="@[package:]style/style_to_inherit">
            <item
                name="[package:]style_property_name"
                >style_value</item>
        </style>
    </resources>
    ```

elements:
:   `<resources>`
    :   **Required.** This must be the root node.

        No attributes.

    `<style>`
    :   Defines a single style. Contains `<item>` elements.

        attributes:

        `name`
        :   *String*. **Required**. A name for the style, which is used as the
            resource ID to apply the style to a View, Activity, or application.

        `parent`
        :   *Style resource*. Reference to a style from which this
            style should inherit style properties.

    `<item>`
    :   Defines a single property for the style. Must be a child of a
        `<style>` element.

        attributes:

        `name`
        :   *Attribute resource*. **Required**. The name of the style property
            to be defined, with a package prefix if necessary (for example `android:textColor`).

example:
:   XML file for the style (saved in `res/values/`):
    :   ```
        <?xml version="1.0" encoding="utf-8"?>
        <resources>
            <style name="CustomText" parent="@style/Text">
                <item name="android:textSize">20sp</item>
                <item name="android:textColor">#008</item>
            </style>
        </resources>
        ```

    XML file that applies the style to a `TextView` (saved in `res/layout/`):
    :   ```
        <?xml version="1.0" encoding="utf-8"?>
        <EditText
            style="@style/CustomText"
            android:layout_width="fill_parent"
            android:layout_height="wrap_content"
            android:text="Hello, World!" />
        ```

[Previous

arrow\_back

String](/guide/topics/resources/string-resource)

[Next

Font

arrow\_forward](/guide/topics/resources/font-resource)