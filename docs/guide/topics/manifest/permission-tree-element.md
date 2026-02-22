---
title: https://developer.android.com/guide/topics/manifest/permission-tree-element
url: https://developer.android.com/guide/topics/manifest/permission-tree-element
source: md.txt
---

# &lt;permission-tree>

syntax:
:

    ```xml
    <permission-tree android:icon="drawable resource"
                     android:label="string resource"
                     android:name="string" />
    ```

contained in:
:   [<manifest>](https://developer.android.com/guide/topics/manifest/manifest-element)

description:
:   Declares the base name for a tree of permissions. The application takes ownership of all names within the tree. It can dynamically add new permissions to the tree by calling[PackageManager.addPermission()](https://developer.android.com/reference/android/content/pm/PackageManager#addPermission(android.content.pm.PermissionInfo)). Names within the tree are separated by periods ('`.`'). For example, if the base name is`com.example.project.taxes`, permissions like the following might be added:

    `com.example.project.taxes.CALCULATE`  
    `com.example.project.taxes.deductions.STORE_RECEIPTS`  
    `com.example.project.taxes.deductions.ACCESS_RECORDS`

    This element doesn't declare a permission itself, only a namespace in which permissions can be placed. For more information about declaring permissions, see the[<permission>](https://developer.android.com/guide/topics/manifest/permission-element)element.

attributes:
:

    `android:icon`
    :   An icon representing all the permissions in the tree. This attribute must be set as a reference to a drawable resource containing the image definition.

    `android:label`
    :   A user-readable name for the group. As a convenience, the label can be directly set as a raw string during development. However, when the application is ready to be published, set it as a reference to a string resource, so that it can be localized like other strings in the user interface.

    `android:name`
    :   The name at the base of the permission tree. It serves as a prefix to all permission names in the tree. Use Java-style scoping so that the name is unique. The name must have more than two period-separated segments in its path. For example,`com.example.base`is OK, but`com.example`isn't.

introduced in:
:   API level 1

see also:
:   [<permission>](https://developer.android.com/guide/topics/manifest/permission-element)  
    [<permission-group>](https://developer.android.com/guide/topics/manifest/permission-group-element)  
    [<uses-permission>](https://developer.android.com/guide/topics/manifest/uses-permission-element)