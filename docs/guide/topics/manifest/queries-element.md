---
title: <queries>  |  App architecture  |  Android Developers
url: https://developer.android.com/guide/topics/manifest/queries-element
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [App architecture](https://developer.android.com/topic/architecture/intro)

# <queries> Stay organized with collections Save and categorize content based on your preferences.




syntax:
:   ```
    <queries>
        <package android:name="string" />
        <intent>
            ...
        </intent>
        <provider android:authorities="list" />
        ...
    </queries>
    ```

contained in:
:   `<manifest>`

description:
:   Specifies the set of other apps that an app
    intends to interact with. These other apps are specified
    [by package name](#package), [by intent
    signature](#intent), or [by provider authority](#provider), as described in
    the following sections on this page.

    **Note:** Some packages are
    [visible automatically](/training/package-visibility/automatic). Your
    app always sees these packages in its queries for other installed apps. To
    view other packages, declare your app's need for increased package visibility
    using the `<queries>` element.

    Learn more about how to use the `<queries>` element in
    [Package visibility filtering on Android](/training/package-visibility).

child elements:
:   `<package>`
    :   Specifies a single app that your app intends to access. This other
        app might integrate with your app, or your app might use services that the
        other app provides.

        attributes:

        `android:name`
        :   **Required.** Specifies the package name of the other app.

    `<intent>`
    :   Specifies an [intent filter
        signature](/training/basics/intents/filters). Your app can discover other apps that have matching
        [`<intent-filter>`](/guide/topics/manifest/intent-filter-element)
        elements.

        **Note:** There are some restrictions on the
        options that you can include in this `<intent>` element,
        compared to a typical intent filter signature. Learn more about these
        restrictions in [Packages
        that match an intent filter signature](/training/package-visibility/declaring#intent-filter-signature).

    `<provider>`
    :   Specifies one or more
        [content
        provider authorities](/guide/topics/providers/content-provider-basics#ContentURIs). Your app can discover other apps whose content
        providers use the specified authorities.

        **Note:** There are some restrictions on the
        options that you can include in this `<provider>` element,
        compared to a typical
        [`<provider>`](/guide/topics/manifest/provider-element)
        manifest element. Usually, you only specify the
        `android:authorities` attribute.

introduced in:
:   API level 30

see also:
:   [Package visibility filtering on Android](/training/package-visibility)