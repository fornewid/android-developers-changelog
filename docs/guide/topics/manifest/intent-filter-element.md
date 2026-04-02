---
title: <intent-filter>  |  App architecture  |  Android Developers
url: https://developer.android.com/guide/topics/manifest/intent-filter-element
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [App architecture](https://developer.android.com/topic/architecture/intro)

# <intent-filter> Stay organized with collections Save and categorize content based on your preferences.




syntax:
:   ```
    <intent-filter android:icon="drawable resource"
                   android:label="string resource"
                   android:priority="integer" >
        ...
    </intent-filter>
    ```

contained in:
:   `<activity>`
      
    `<activity-alias>`
      
    `<service>`
      
    `<receiver>`
      
    `<provider>`

must contain:
:   `<action>`

can contain:
:   `<category>`
      
    `<data>`
      
    `<uri-relative-filter-group>`

description:
:   Specifies the types of intents that an activity, service, or broadcast
    receiver can respond to. An intent filter declares the capabilities of its
    parent component: what an activity or service can do and what types
    of broadcasts a receiver can handle.

    It opens the component to receiving
    intents of the advertised type while filtering out those that aren't
    meaningful for the component.
    Most of the contents of the filter are described by its subelements:

    * `<action>`,
    * `<category>`,
    * `<data>`, and
    * `<uri-relative-filter-group>`.

    For a more detailed discussion of filters, see
    [Intents
    and Intent Filters](/guide/components/intents-filters) and the
    [Intent filters](/guide/topics/manifest/manifest-intro#ifs)
    section in the app manifest overview.

attributes:
:   `android:icon`
    :   An icon that represents the parent activity, service, or broadcast
        receiver when that component is presented to the user as having the
        capability described by the filter.

        This attribute is set as a reference to a drawable resource
        containing the image definition. The default value is the icon set
        by the parent component's `icon` attribute. If the parent
        doesn't specify an icon, the default is the icon set by the
        `<application>` element.

        For more information about intent filter icons, see the
        [Icons and labels](/guide/topics/manifest/manifest-intro#iconlabel)
        section in the app manifest overview.

    `android:label`
    :   A user-readable label for the parent component. This label, rather than
        the one set by the parent component, is used when the component is presented
        to the user as having the capability described by the filter.

        The label is set as a reference to a string resource so that
        it can be localized like other strings in the user interface.
        However, as a convenience while you're developing the application,
        it can also be set as a raw string.

        The default value is the label set by the parent component. If the
        parent doesn't specify a label, the default is the label set by the
        `<application>` element's
         `label` attribute.

        For more information about intent filter labels, see the
        [Icons and labels](/guide/topics/manifest/manifest-intro#iconlabel)
        section in the app manifest overview.

    `android:priority`
    :   The priority given to the parent component with regard
        to handling intents of the type described by the filter. This attribute has
        meaning for both activities and broadcast receivers.

        * It provides information about how able an activity is to respond to
          an intent that matches the filter, relative to other activities that can
          also respond to the intent. When an intent can be handled by multiple
          activities with different priorities, Android considers only those with
          higher priority values as potential targets for the intent.
        * It controls the order in which broadcast receivers are executed to
          receive broadcast messages, with those having higher priority
          values being called before those having lower values. The order applies only
          to synchronous messages. It's ignored for asynchronous messages.

        Use this attribute only if you need to impose a specific order in
        which the broadcasts are received or want to force Android to prefer
        one activity over others.

        The value is an integer, such as `100`. Higher numbers have a
        higher priority. The default value is `0`.

        In certain circumstances the requested priority is ignored and the value
        is capped to `0`. This occurs when:

        * A non-privileged application requests any priority >0.
        * A privileged application requests a priority >0 for
          `ACTION_VIEW`,
          `ACTION_SEND`,
          `ACTION_SENDTO` or
          `ACTION_SEND_MULTIPLE`.

        For more information, see `setPriority()`.

    `android:order`
    :   The order in which the filter is processed when multiple filters match.

        `order` differs from `priority` in that `priority` applies
        across apps, while `order` disambiguates multiple matching filters in a single
        app.

        When multiple filters can match, use a directed intent instead.

        The value is an integer, such as `100`. Higher numbers are matched first.
        The default value is `0`.

        This attribute was introduced in API level 28.

    `android:autoVerify`
    :   Whether Android needs to verify that the Digital Asset Links JSON file from the specified
        host matches this application.

    For more information, see
    [Verify Android App Links](/training/app-links/verify-android-applinks).

    The default value is `false`.

    This attribute was introduced in API level 23.

introduced in:
:   API level 1

see also:
:   `<action>`
      
    `<category>`
      
    `<data>`
      
    `<uri-relative-filter-group>`