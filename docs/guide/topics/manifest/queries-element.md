---
title: https://developer.android.com/guide/topics/manifest/queries-element
url: https://developer.android.com/guide/topics/manifest/queries-element
source: md.txt
---

syntax:
:

    ```xml
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
:   [<manifest>](https://developer.android.com/guide/topics/manifest/manifest-element)

description:

:   Specifies the set of other apps that an app intends to interact with. These other apps are specified[by package name](https://developer.android.com/guide/topics/manifest/queries-element#package),[by intent signature](https://developer.android.com/guide/topics/manifest/queries-element#intent), or[by provider authority](https://developer.android.com/guide/topics/manifest/queries-element#provider), as described in the following sections on this page.

    **Note:** Some packages are[visible automatically](https://developer.android.com/training/package-visibility/automatic). Your app always sees these packages in its queries for other installed apps. To view other packages, declare your app's need for increased package visibility using the`<queries>`element.

    Learn more about how to use the`<queries>`element in[Package visibility filtering on Android](https://developer.android.com/training/package-visibility).

child elements:
:

    `<package>`

    :   Specifies a single app that your app intends to access. This other app might integrate with your app, or your app might use services that the other app provides.

        attributes:

        `android:name`
        :   **Required.**Specifies the package name of the other app.

    `<intent>`

    :   Specifies an[intent filter signature](https://developer.android.com/training/basics/intents/filters). Your app can discover other apps that have matching[`<intent-filter>`](https://developer.android.com/guide/topics/manifest/intent-filter-element)elements.

        **Note:** There are some restrictions on the options that you can include in this`<intent>`element, compared to a typical intent filter signature. Learn more about these restrictions in[Packages that match an intent filter signature](https://developer.android.com/training/package-visibility/declaring#intent-filter-signature).

    `<provider>`

    :   Specifies one or more[content provider authorities](https://developer.android.com/guide/topics/providers/content-provider-basics#ContentURIs). Your app can discover other apps whose content providers use the specified authorities.

        **Note:** There are some restrictions on the options that you can include in this`<provider>`element, compared to a typical[`<provider>`](https://developer.android.com/guide/topics/manifest/provider-element)manifest element. Usually, you only specify the`android:authorities`attribute.

introduced in:
:   API level 30

see also:
:   [Package visibility filtering on Android](https://developer.android.com/training/package-visibility)