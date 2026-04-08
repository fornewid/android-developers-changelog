---
title: https://developer.android.com/guide/topics/manifest/category-element
url: https://developer.android.com/guide/topics/manifest/category-element
source: md.txt
---

# &lt;category>

syntax:
:

    ```xml
    <category android:name="string" />
    ```

contained in:
:   [<intent-filter>](https://developer.android.com/guide/topics/manifest/intent-filter-element)

description:
:   Adds a category name to an intent filter. See
    [Intents and
    Intent Filters](https://developer.android.com/guide/components/intents-filters) for details on intent filters and the role of category
    specifications within a filter.

attributes:
:

    `android:name`
    :   The name of the category. Standard categories are defined in the
        [Intent](https://developer.android.com/reference/android/content/Intent) class as `CATEGORY_`*name*
        constants. The name assigned here is derived from those constants
        by prefixing `android.intent.category.` to the
        *name* that follows `CATEGORY_`. For example,
        the string value for `CATEGORY_LAUNCHER` is
        `android.intent.category.LAUNCHER`.

        **Note:** To receive implicit intents, you must include the
        [CATEGORY_DEFAULT](https://developer.android.com/reference/android/content/Intent#CATEGORY_DEFAULT) category in the intent filter. The methods
        [startActivity()](https://developer.android.com/reference/android/app/Activity#startActivity(android.content.Intent)) and
        [startActivityForResult()](https://developer.android.com/reference/android/app/Activity#startActivityForResult(android.content.Intent, int)) treat all intents
        as if they declared the [CATEGORY_DEFAULT](https://developer.android.com/reference/android/content/Intent#CATEGORY_DEFAULT) category.
        If you don't declare it in your intent filter, no implicit intents can resolve
        your activity.


        For custom categories, use the package name as a prefix so
        that they are unique.

introduced in:
:   API Level 1

see also:
:   [<action>](https://developer.android.com/guide/topics/manifest/action-element)

    [<data>](https://developer.android.com/guide/topics/manifest/data-element)