---
title: https://developer.android.com/guide/topics/manifest/property-element
url: https://developer.android.com/guide/topics/manifest/property-element
source: md.txt
---

# &lt;property>

syntax:
:

    ```xml
    <property android:name="string"
               android:resource="resource specification"
               android:value="string" />
    ```

contained in:
:   [<activity>](https://developer.android.com/guide/topics/manifest/activity-element)  
    [<activity-alias>](https://developer.android.com/guide/topics/manifest/activity-alias-element)  
    [<application>](https://developer.android.com/guide/topics/manifest/application-element)  
    [<provider>](https://developer.android.com/guide/topics/manifest/provider-element)  
    [<receiver>](https://developer.android.com/guide/topics/manifest/receiver-element)  
    [<service>](https://developer.android.com/guide/topics/manifest/service-element)

description:
:   A name-value pair for an item of additional, arbitrary data that can be supplied to the parent component. A component element can contain any number of`<property>`subelements. Valid names include any of the[property constants](https://developer.android.com/reference/android/content/pm/PackageManager#constants_1)defined in the[PackageManager](https://developer.android.com/reference/android/content/pm/PackageManager)class,[PackageManager.Property](https://developer.android.com/reference/android/content/pm/PackageManager.Property)tags defined in classes such as[WindowProperties](https://developer.android.com/reference/kotlin/androidx/window/WindowProperties), and arbitrary constants defined ad hoc. Obtain values individually using the[PackageManager.getProperty()](https://developer.android.com/reference/android/content/pm/PackageManager#getProperty(java.lang.String,%20java.lang.String))method.

    Specify ordinary values with the[android:value](https://developer.android.com/guide/topics/manifest/property-element#val)`
    `attribute. Specify resource IDs with the[android:resource](https://developer.android.com/guide/topics/manifest/property-element#rsrc)attribute. Specifying both`android:value`and`android:resource`is invalid.

    For example, the following code assigns whatever value is stored in the`@string/kangaroo`resource to the`zoo`name:  

    ```xml
    <property android:name="zoo" android:value=”@string/kangaroo” />
    ```

    The code here, however, assigns the numeric ID of the resource, not the value stored in the resource, to`zoo`:  

    ```xml
    <property android:name="zoo" android:resource=”@string/kangaroo” />
    ```

attributes:
:

    `android:name`
    :   The name of the property. A parsing error results if multiple, sibling`<property>`tags have the same name.

    `android:resource`
    :   A reference to a resource. The ID of the resource is the value assigned to the property. The ID can be retrieved from the property by[PackageManager.Property.getResourceId()](https://developer.android.com/reference/android/content/pm/PackageManager.Property#getResourceId()).

    `android:value`
    :   A value assigned to the property. The following table lists valid data types and accessor methods for the value attribute:  

        |                                                       Type                                                        |                                        PackageManager.Property accessor                                         |
        |-------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
        | String: Use double backslashes (\\\\) to escape characters; for example,`\\n`and`\\uxxxxx`for a Unicode character | [getString()](https://developer.android.com/reference/android/content/pm/PackageManager.Property#getString())   |
        | Integer: For example,`100`                                                                                        | [getInteger()](https://developer.android.com/reference/android/content/pm/PackageManager.Property#getInteger()) |
        | Boolean: Either`true`or`false`                                                                                    | [getBoolean()](https://developer.android.com/reference/android/content/pm/PackageManager.Property#getBoolean()) |
        | Color: In the form`#rgb`,`#argb`,`#rrggbb`, or`#aarrggbb`                                                         | [getInteger()](https://developer.android.com/reference/android/content/pm/PackageManager.Property#getInteger()) |
        | Float: For example,`1.23`                                                                                         | [getFloat()](https://developer.android.com/reference/android/content/pm/PackageManager.Property#getFloat())     |

introduced in:
:   API Level 31