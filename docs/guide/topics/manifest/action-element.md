---
title: https://developer.android.com/guide/topics/manifest/action-element
url: https://developer.android.com/guide/topics/manifest/action-element
source: md.txt
---

# &lt;action>

syntax:
:

    ```xml
    <action android:name="string" />
    ```

contained in:
:   [<intent-filter>](https://developer.android.com/guide/topics/manifest/intent-filter-element)

description:
:   Adds an action to an intent filter. An[<intent-filter>](https://developer.android.com/guide/topics/manifest/intent-filter-element)element must contain one or more`<action>`elements. If there are no`<action>`elements in an intent filter, the filter doesn't accept any[Intent](https://developer.android.com/reference/android/content/Intent)objects. For details about intent filters and the role of action specifications within a filter, see[Intents and Intent Filters](https://developer.android.com/guide/components/intents-filters).

attributes:
:

    `android:name`
    :   The name of the action. Some standard actions are defined in the[Intent](https://developer.android.com/reference/android/content/Intent#ACTION_CHOOSER)class as`ACTION_`*string*constants. To assign one of these actions to this attribute, prepend`android.intent.action.`to the*string*that follows`ACTION_`. For example, for`ACTION_MAIN`, use`android.intent.action.MAIN`, and for`ACTION_WEB_SEARCH`, use`android.intent.action.WEB_SEARCH`.

        For actions you define, it's best to use your app's package name as a prefix to help ensure uniqueness. For example, a`TRANSMOGRIFY`action might be specified as follows:  

        ```xml
        <action android:name="com.example.project.TRANSMOGRIFY" />
        ```

introduced in:
:   API Level 1

see also:
:   [<intent-filter>](https://developer.android.com/guide/topics/manifest/intent-filter-element)