---
title: <grant-uri-permission>  |  App architecture  |  Android Developers
url: https://developer.android.com/guide/topics/manifest/grant-uri-permission-element
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [App architecture](https://developer.android.com/topic/architecture/intro)

# <grant-uri-permission> Stay organized with collections Save and categorize content based on your preferences.




syntax:
:   ```
    <grant-uri-permission android:path="string"
                          android:pathPattern="string"
                          android:pathPrefix="string" />
    ```

contained in:
:   `<provider>`

description:
:   Specifies the subsets of app data that the parent content provider
    has permission to access. Data subsets are indicated by the path part of a
    `content:` URI. The authority part of the URI identifies the
    content provider.
    Granting permission is a way of enabling clients of the provider that don't
    normally have permission to access its data to overcome that restriction on
    a one-time basis.

    If a content provider's `grantUriPermissions`
    attribute is `true`, permission can be granted for any of the data under
    the provider's purview. However, if that attribute is `false`, permission
    is granted only to data subsets that are specified by this element.
    A provider can contain any number of `<grant-uri-permission>` elements.
    Each one can specify only one path, using one of the three possible attributes.

    For information about how permission is granted, see the
    `<intent-filter>` element's
    `grantUriPermissions` attribute.

attributes:
:   `android:path` `android:pathPrefix` `android:pathPattern`
    :   A path identifying the data subset or subsets that permission can be
        granted for. The `path` attribute specifies a complete path.
        Permission can granted only to the particular data subset identified
        by that path.

        The `pathPrefix` attribute specifies the initial part of a path.
        Permission can be granted to all data subsets with paths that share that
        initial part.
        The `pathPattern` attribute specifies a complete path, but one
        that can contain the following wildcards:

        * An asterisk (`*`) matches a sequence of zero to many occurrences of
          the immediately preceding character.
        * A period followed by an asterisk (`.*`) matches any sequence of
          zero to many characters.

        Because `\` is used as an escape character when the string is read
        from XML, before it is parsed as a pattern, you need to double-escape.
        For example, a literal `*` is written as `\\*` and a
        literal `\` is written as `\\\`.

        For more information about these types of patterns, see the descriptions of
        `PATTERN_LITERAL`,
        `PATTERN_PREFIX`, and
        `PATTERN_SIMPLE_GLOB` in the
        `PatternMatcher` class.

introduced in:
:   API level 1

see also:
:   `grantUriPermissions`
    attribute of the
    `<provider>`
    element