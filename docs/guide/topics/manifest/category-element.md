---
title: <category>  |  App architecture  |  Android Developers
url: https://developer.android.com/guide/topics/manifest/category-element
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [App architecture](https://developer.android.com/topic/architecture/intro)

# <category> Stay organized with collections Save and categorize content based on your preferences.




syntax:
:   ```
    <category android:name="string" />
    ```

contained in:
:   `<intent-filter>`

description:
:   Adds a category name to an intent filter. See
    [Intents and
    Intent Filters](/guide/components/intents-filters) for details on intent filters and the role of category
    specifications within a filter.

attributes:
:   `android:name`
    :   The name of the category. Standard categories are defined in the
        `Intent` class as `CATEGORY_name`
        constants. The name assigned here is derived from those constants
        by prefixing `android.intent.category.` to the
        `name` that follows `CATEGORY_`. For example,
        the string value for `CATEGORY_LAUNCHER` is
        `android.intent.category.LAUNCHER`.

        **Note:** To receive implicit intents, you must include the
        `CATEGORY_DEFAULT` category in the intent filter. The methods
        `startActivity()` and
        `startActivityForResult()` treat all intents
        as if they declared the `CATEGORY_DEFAULT` category.
        If you don't declare it in your intent filter, no implicit intents can resolve
        your activity.

        For custom categories, use the package name as a prefix so
        that they are unique.

introduced in:
:   API Level 1

see also:
:   `<action>`
      
    `<data>`