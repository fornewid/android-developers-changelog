---
title: https://developer.android.com/guide/topics/manifest/layout-element
url: https://developer.android.com/guide/topics/manifest/layout-element
source: md.txt
---

# &lt;layout>

syntax:
:

    ```xml
    <layout android:defaultHeight="integer"
              android:defaultWidth="integer"
              android:gravity=["top" | "end" | ...]
              android:minHeight="integer"
              android:minWidth="integer" />
    ```

contained in:
:   [<activity>](https://developer.android.com/guide/topics/manifest/activity-element)

description:
:   Contains attributes that affect how an activity behaves in multi-window mode.

attributes:
:

    `android:defaultHeight`
    :   Default height of the activity when launched in free-form mode.

    `android:defaultWidth`
    :   Default width of the activity when launched in free-form mode.

    `android:gravity`
    :   Initial placement of the activity when launched in free-form mode. See[Gravity](https://developer.android.com/reference/android/view/Gravity)for suitable values.

    `android:minHeight`
    :   Minimum height for the activity in both split-screen and free-form modes. If the user moves the divider in split-screen mode to make an activity smaller than the specified minimum, the system crops the activity to the height the user requests.

    `android:minWidth`
    :   Minimum width for the activity in both split-screen and free-form modes. If the user moves the divider in split-screen mode to make an activity smaller than the specified minimum, the system crops the activity to the width the user requests.

    introduced in:
    :   API Level 24

    see also:
    :   [<activity>](https://developer.android.com/guide/topics/manifest/activity-element)