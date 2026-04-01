---
title: <meta-data>  |  App architecture  |  Android Developers
url: https://developer.android.com/guide/topics/manifest/meta-data-element
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [App architecture](https://developer.android.com/topic/architecture/intro)

# <meta-data> Stay organized with collections Save and categorize content based on your preferences.




syntax:
:   ```
    <meta-data android:name="string"
               android:resource="resource specification"
               android:value="string" />
    ```

contained in:
:   `<activity>`
      
    `<activity-alias>`
      
    `<application>`
      
    `<provider>`
      
    `<receiver>`
      
    `<service>`

description:
:   A name-value pair for an item of additional, arbitrary data that can be
    supplied to the parent component. A component element can contain any
    number of `<meta-data>` subelements. The values from all of
    them are collected in a single `Bundle` object and made
    available to the component as the
    `PackageItemInfo.metaData` field.

    Specify ordinary values through the `value`
    attribute. To assign a resource ID as the value, use the
    `resource` attribute instead. For example,
    the following code assigns whatever value is stored in the `@string/kangaroo`
    resource to the `zoo` name:

    ```
    <meta-data android:name="zoo" android:value="@string/kangaroo" />
    ```

    On the other hand, using the `resource` attribute assigns `zoo`
    the numeric ID of the resource, not the value stored in the resource:

    ```
    <meta-data android:name="zoo" android:resource="@string/kangaroo" />
    ```

    We highly recommend that you avoid supplying related data as
    multiple separate `<meta-data>` entries. Instead, if you
    have complex data to associate with a component, store it as a resource and
    use the `resource` attribute to inform the component of its ID.

attributes:
:   `android:name`
    :   A unique name for the item. To keep the name unique, use a
        Java-style naming convention, such as
        "`com.example.project.activity.fred`".

    `android:resource`
    :   A reference to a resource. The ID of the resource is the value assigned
        to the item. The ID is retrieved from the meta-data `Bundle` using the
        `Bundle.getInt()` method.

    `android:value`
    :   The value assigned to the item. The data types that can be assigned as values and the
        `Bundle` methods that components use to retrieve those values are listed in the following table:
          

        | Type | Bundle method |
        | --- | --- |
        | String: use double backslashes (`\\`) to escape characters, such as `\\n` for a new line and `\\uxxxxx` for a Unicode character | `getString()` |
        | Integer: for example, `100` | `getInt()` |
        | Boolean: either `true` or `false` | `getBoolean()` |
        | Color: in the form `#rgb`, `#argb`, `#rrggbb`, or `#aarrggbb` | `getInt()` |
        | Float: for example, `1.23` | `getFloat()` |

introduced in:
:   API level 1