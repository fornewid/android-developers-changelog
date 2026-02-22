---
title: https://developer.android.com/guide/topics/manifest/attribution-element
url: https://developer.android.com/guide/topics/manifest/attribution-element
source: md.txt
---

# &lt;attribution>

syntax:
:

    ```xml
    <attribution android:tag="string"
                 android:label="string resource">
        ...
    </attribution>
    ```

contained in:
:   [<manifest>](https://developer.android.com/guide/topics/manifest/manifest-element)

description:
:   If you develop a multi-purpose app, you can apply this tag to each part
    of your app when you [audit its data access](https://developer.android.com/privacy-and-security/audit-data-access).
    This helps you trace data access back to logical parts of your code.

attributes:
:

    `android:tag`
    :   A literal string that serves as a label for a particular capability of your app.

    `android:label`
    :   A string resource that describes a particular capability of your app.

introduced in:
:   API level 31