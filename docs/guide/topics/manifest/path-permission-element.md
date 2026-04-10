---
title: https://developer.android.com/guide/topics/manifest/path-permission-element
url: https://developer.android.com/guide/topics/manifest/path-permission-element
source: md.txt
---

# &lt;path-permission>

syntax:
:

    ```xml
    <path-permission android:path="string"
                     android:pathPrefix="string"
                     android:pathPattern="string"
                     android:permission="string"
                     android:readPermission="string"
                     android:writePermission="string" />
    ```

contained in:
:   [<provider>](https://developer.android.com/guide/topics/manifest/provider-element)

description:
:   Defines the path and required permissions for a specific subset of data within a content provider. This element can be specified multiple times to supply multiple paths.

attributes:
:

    `android:path`
    :   A complete URI path for a subset of content provider data. Permission can be granted only to the particular data identified by this path. When used to provide search suggestion content, it is appended with`/search_suggest_query`.

    `android:pathPrefix`
    :   The initial part of a URI path for a subset of content provider data. Permission can be granted to all data subsets with paths that share this initial part.

    `android:pathPattern`
    :   A complete URI path for a subset of content provider data, but one that can use the following wildcards:

        - An asterisk (`*`). This matches a sequence of zero to many occurrences of the immediately preceding character.
        - A period followed by an asterisk (`.*`). This matches any sequence of zero or more characters.

        Because the backslash (`\`) is used as an escape character when the string is read from XML, before it is parsed as a pattern, you need to double-escape. For example, a literal`*`is written as "`\\*`" and a literal`\`is written as "`\\\`". This is the same as what you write if constructing the string in the Java programming language.

        For more information about these types of patterns, see the descriptions of[`PATTERN_LITERAL`](https://developer.android.com/reference/android/os/PatternMatcher#PATTERN_LITERAL),[`PATTERN_PREFIX`](https://developer.android.com/reference/android/os/PatternMatcher#PATTERN_PREFIX), and[`PATTERN_SIMPLE_GLOB`](https://developer.android.com/reference/android/os/PatternMatcher#PATTERN_SIMPLE_GLOB)in the[`PatternMatcher`](https://developer.android.com/reference/android/os/PatternMatcher)class.

    `android:permission`
    :   The name of a permission that clients need in order to read or write the content provider's data. This attribute is a convenient way of setting a single permission for both reading and writing. However, the`readPermission`and`writePermission`attributes take precedence over this one.

    `android:readPermission`
    :   A permission that clients need in order to query the content provider.

    `android:writePermission`
    :   A permission that clients need in order to make changes to the data controlled by the content provider.

introduced in:
:   API level 4

see also:
:   [SearchManager](https://developer.android.com/reference/android/app/SearchManager)
:   [Manifest.permission](https://developer.android.com/reference/android/Manifest.permission)
:   [Security tips](https://developer.android.com/guide/topics/security/security)