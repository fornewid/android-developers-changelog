---
title: https://developer.android.com/guide/topics/manifest/intent-filter-element
url: https://developer.android.com/guide/topics/manifest/intent-filter-element
source: md.txt
---

# &lt;intent-filter>

syntax:
:

    ```xml
    <intent-filter android:icon="drawable resource"
                   android:label="string resource"
                   android:priority="integer" >
        ...
    </intent-filter>
    ```

contained in:
:   [<activity>](https://developer.android.com/guide/topics/manifest/activity-element)  
    [<activity-alias>](https://developer.android.com/guide/topics/manifest/activity-alias-element)  
    [<service>](https://developer.android.com/guide/topics/manifest/service-element)  
    [<receiver>](https://developer.android.com/guide/topics/manifest/receiver-element)  
    [<provider>](https://developer.android.com/guide/topics/manifest/provider-element)

must contain:
:   [<action>](https://developer.android.com/guide/topics/manifest/action-element)

can contain:
:   [<category>](https://developer.android.com/guide/topics/manifest/category-element)  
    [<data>](https://developer.android.com/guide/topics/manifest/data-element)  
    [<uri-relative-filter-group>](https://developer.android.com/guide/topics/manifest/uri-relative-filter-group-element)

description:

:   Specifies the types of intents that an activity, service, or broadcast receiver can respond to. An intent filter declares the capabilities of its parent component: what an activity or service can do and what types of broadcasts a receiver can handle.<br />

    It opens the component to receiving intents of the advertised type while filtering out those that aren't meaningful for the component. Most of the contents of the filter are described by its subelements:

    - [<action>](https://developer.android.com/guide/topics/manifest/action-element),
    - [<category>](https://developer.android.com/guide/topics/manifest/category-element),
    - [<data>](https://developer.android.com/guide/topics/manifest/data-element), and
    - [<uri-relative-filter-group>](https://developer.android.com/guide/topics/manifest/uri-relative-filter-group-element).

    <br />

    For a more detailed discussion of filters, see[Intents and Intent Filters](https://developer.android.com/guide/components/intents-filters)and the[Intent filters](https://developer.android.com/guide/topics/manifest/manifest-intro#ifs)section in the app manifest overview.

attributes:
:

    `android:icon`

    :   An icon that represents the parent activity, service, or broadcast receiver when that component is presented to the user as having the capability described by the filter.<br />

        This attribute is set as a reference to a drawable resource containing the image definition. The default value is the icon set by the parent component's`icon`attribute. If the parent doesn't specify an icon, the default is the icon set by the[<application>](https://developer.android.com/guide/topics/manifest/application-element)element.

        For more information about intent filter icons, see the[Icons and labels](https://developer.android.com/guide/topics/manifest/manifest-intro#iconlabel)section in the app manifest overview.

    `android:label`

    :   A user-readable label for the parent component. This label, rather than the one set by the parent component, is used when the component is presented to the user as having the capability described by the filter.<br />

        The label is set as a reference to a string resource so that it can be localized like other strings in the user interface. However, as a convenience while you're developing the application, it can also be set as a raw string.

        The default value is the label set by the parent component. If the parent doesn't specify a label, the default is the label set by the[<application>](https://developer.android.com/guide/topics/manifest/application-element)element's[label](https://developer.android.com/guide/topics/manifest/application-element#label)attribute.

        For more information about intent filter labels, see the[Icons and labels](https://developer.android.com/guide/topics/manifest/manifest-intro#iconlabel)section in the app manifest overview.

    `android:priority`
    :   The priority given to the parent component with regard to handling intents of the type described by the filter. This attribute has meaning for both activities and broadcast receivers.

        - It provides information about how able an activity is to respond to an intent that matches the filter, relative to other activities that can also respond to the intent. When an intent can be handled by multiple activities with different priorities, Android considers only those with higher priority values as potential targets for the intent.
        - It controls the order in which broadcast receivers are executed to receive broadcast messages, with those having higher priority values being called before those having lower values. The order applies only to synchronous messages. It's ignored for asynchronous messages.

        Use this attribute only if you need to impose a specific order in which the broadcasts are received or want to force Android to prefer one activity over others.

        The value is an integer, such as`100`. Higher numbers have a higher priority. The default value is`0`.

        In certain circumstances the requested priority is ignored and the value is capped to`0`. This occurs when:

        - A non-privileged application requests any priority \>0.
        - A privileged application requests a priority \>0 for[ACTION_VIEW](https://developer.android.com/reference/android/content/Intent#ACTION_VIEW),[ACTION_SEND](https://developer.android.com/reference/android/content/Intent#ACTION_SEND),[ACTION_SENDTO](https://developer.android.com/reference/android/content/Intent#ACTION_SENDTO)or[ACTION_SEND_MULTIPLE](https://developer.android.com/reference/android/content/Intent#ACTION_SEND_MULTIPLE).

        For more information, see[setPriority()](https://developer.android.com/reference/android/content/IntentFilter#setPriority(int)).

    `android:order`

    :   The order in which the filter is processed when multiple filters match.

        `order`differs from`priority`in that`priority`applies across apps, while`order`disambiguates multiple matching filters in a single app.

        When multiple filters can match, use a directed intent instead.

        The value is an integer, such as`100`. Higher numbers are matched first. The default value is`0`.

        This attribute was introduced in API level 28.

    `android:autoVerify`
    :   Whether Android needs to verify that the Digital Asset Links JSON file from the specified host matches this application.

introduced in:
:   API level 1

see also:
:   [<action>](https://developer.android.com/guide/topics/manifest/action-element)  
    [<category>](https://developer.android.com/guide/topics/manifest/category-element)  
    [<data>](https://developer.android.com/guide/topics/manifest/data-element)  
    [<uri-relative-filter-group>](https://developer.android.com/guide/topics/manifest/uri-relative-filter-group-element)