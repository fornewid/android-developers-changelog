---
title: <permission-group>  |  App architecture  |  Android Developers
url: https://developer.android.com/guide/topics/manifest/permission-group-element
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [App architecture](https://developer.android.com/topic/architecture/intro)

# <permission-group> Stay organized with collections Save and categorize content based on your preferences.




syntax:
:   ```
    <permission-group android:description="string resource"
                      android:icon="drawable resource"
                      android:label="string resource"
                      android:name="string" />
    ```

contained in:
:   `<manifest>`

description:
:   Declares a name for a logical grouping of related permissions. Individual
    permissions join the group through the `permissionGroup` attribute of the
    `<permission>` element. Members of a group are
    presented together in the user interface.

    This element doesn't declare a permission itself, only a category in which permissions can be placed.
    For information about declaring permissions and assigning them to groups, see the
    `<permission>` element.

attributes:
:   `android:description`
    :   User-readable text that describes the group. The text is
        longer and more explanatory than the label. This attribute must be
        set as a reference to a string resource. Unlike the `label`
        attribute, it can't be a raw string.

    `android:icon`
    :   An icon representing the permission. This attribute must be set
        as a reference to a drawable resource containing the image definition.

    `android:label`
    :   A user-readable name for the group. As a convenience, the label
        can be directly set as a raw string while you're developing the application.
        However, when the application is ready to be published, set it
        as a reference to a string resource, so that it can be localized like other
        strings in the user interface.

    `android:name`
    :   The name of the group. This is the name that can be assigned to a
        `<permission>`
        element's
        `android:permissionGroup`
        attribute.

introduced in:
:   API level 1

see also:
:   `<permission>`
      
    `<permission-tree>`
      
    `<uses-permission>`