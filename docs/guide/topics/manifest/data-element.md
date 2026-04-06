---
title: <data>  |  App architecture  |  Android Developers
url: https://developer.android.com/guide/topics/manifest/data-element
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [App architecture](https://developer.android.com/topic/architecture/intro)

# <data> Stay organized with collections Save and categorize content based on your preferences.



syntax:
:   If the data tag is the immediate child of an
    `<intent-filter>`:
      

    ```
    <data android:scheme="string"
          android:host="string"
          android:port="string"
          android:path="string"
          android:pathPattern="string"
          android:pathPrefix="string"
          android:pathSuffix="string"
          android:pathAdvancedPattern="string"
          android:mimeType="string" />
    ```

      
    If the data tag is the immediate child of a
    `<uri-relative-filter-group>`:
      

    ```
    <data
          android:path="string"
          android:pathPattern="string"
          android:pathPrefix="string"
          android:pathSuffix="string"
          android:pathAdvancedPattern="string"
          android:fragment="string"
          android:fragmentPattern="string"
          android:fragmentPrefix="string"
          android:fragmentSuffix="string"
          android:fragmentAdvancedPattern="string"
          android:query="string"
          android:queryPattern="string"
          android:queryPrefix="string"
          android:querySuffix="string"
          android:queryAdvancedPattern="string" />
    ```

contained in:
:   `<intent-filter>`
      
    `<uri-relative-filter-group>`

description:
:   Adds a data specification to an intent filter. The specification is
    a data type, using the `mimeType`
    attribute, a URI, or both a data type and a URI. A URI is specified by separate
    attributes for each of its parts:

    `<scheme>://<host>:<port>[<path>|<pathPrefix>|<pathPattern>|<pathAdvancedPattern>|<pathSuffix>]`

    These attributes that specify the URI format are optional, but also mutually dependent:

    * If a `scheme`
      isn't specified for the intent filter, all the other URI attributes are ignored.
    * If a `host`
      isn't specified for the filter, the `port` attribute and all the path attributes are ignored.

    All the `<data>` elements contained within the same
    `<intent-filter>` element contribute to
    the same filter. So, for example, the following filter specification:

    ```
    <intent-filter . . . >
        <data android:scheme="something" android:host="project1.example.com" />
        <data android:scheme="something-else" android:host="project2.example.com" android:path="/page1" />
        ...
    </intent-filter>
    ```

    is equivalent to this one:

    ```
    <intent-filter . . . >
        <data android:scheme="something" />
        <data android:scheme="something-else" />
        <data android:host="project1.example.com" />
        <data android:host="project2.example.com" />
        <data android:path="/page1" />
        ...
    </intent-filter>
    ```

    You can place any number of `<data>` elements inside an
    `<intent-filter>` to give it multiple data
    options. None of its attributes have default values.

    For information on how intent filters work, including the rules for how intent objects
    are matched against filters, see
    [Intents and
    Intent Filters](/guide/components/intents-filters) and the
    [Intent filters](/guide/topics/manifest/manifest-intro#ifs)
    section in the manifest file overview.

attributes:
:   `android:scheme`
    :   The scheme part of a URI. This is the minimal essential attribute for
        specifying a URI. At least one `scheme` attribute must be set
        for the filter, or none of the other URI attributes are meaningful.

        A scheme is specified without the trailing colon, such as
        `http` rather than `http:`.

        If the filter has a data type set (using the `mimeType`
        attribute) but no scheme, the `content:` and `file:` schemes are
        assumed.

        **Note**: Scheme matching in the Android framework is
        case-sensitive, unlike the RFC. As a result, always specify schemes
        using lowercase letters.

    `android:host`
    :   The host part of a URI authority. This attribute is meaningless
        unless a `scheme` attribute
        is also specified for the filter. To match multiple subdomains, use an asterisk (`*`) to
        match zero or more characters in the host. For example, the host `*.google.com` matches
        `www.google.com`, `.google.com`, and `developer.google.com`.

        The asterisk must be the first character of the host attribute. For example, the host
        `google.co.*` is invalid, because the asterisk wildcard isn't the first character.

        **Note**: Host name matching in the Android framework is
        case-sensitive, unlike the formal RFC. As a result, always specify
        host names using lowercase letters.

    `android:port`
    :   The port part of a URI authority. This attribute is meaningful only
        if the `scheme` and
        `host` attributes are also specified for
        the filter.

    `android:path` `android:pathPrefix` `android:pathSuffix` `android:pathPattern` `android:pathAdvancedPattern`
    :   The path part of a URI, which must begin with a `/`.
        The `path` attribute specifies a complete
        path that is matched against the complete path in an `Intent` object. The
        `pathPrefix` attribute specifies a partial path that is matched against
        only the initial part of the path in the `Intent` object.

        The
        `pathSuffix` attribute is matched exactly against the ending part of the path in the
        `Intent` object, and this attribute doesn't have to begin with the `/` character.

        The `pathPattern` attribute specifies a complete path that is matched against the
        complete path in the `Intent` object, but it can contain the following wildcards:

        * A period (`.`) matches any character.
        * An asterisk (`*`) matches a sequence of zero to many occurrences of
          the immediately preceding character.
        * A period followed by an asterisk (`.*`) matches any sequence of
          zero to many characters.

        The `pathAdvancedPattern` attribute specifies a complete path, which is matched against the
        complete path of the `Intent` object and supports the following regex-like patterns:

        * A period (`.`) matches any character.
        * A set (`[...]`) matches ranges of characters. For example , `[0-5]`
          matches a single digit from 0 through 5 but not 6 through 9. `[a-zA-Z]`
          matches any letter, regardless of case. Sets also support the "not" `^` modifier.
        * The asterisk (`*`) modifier matches the preceding pattern zero or more times.
        * The plus (`+`) modifier matches the preceding pattern one or more times.
        * The range (`{...}`) modifier specifies the number of times a pattern
          can match.

        The `pathAdvancedPattern` matcher is an evaluation implementation in which matching
        is done against the pattern in real time with no backtracking support.

        Because `\` is used as an escape character when the string is read
        from XML, before it is parsed as a pattern, you need to double-escape.
        For example, a literal `*` is written as `\\*`, and a
        literal `\` is written as `\\\\`. This is like what you write when
        constructing the string in Java code.

        For more information about these five types of patterns, see the descriptions of
        `PATTERN_LITERAL`,
        `PATTERN_PREFIX`,
        `PATTERN_SIMPLE_GLOB`,
        `PATTERN_SUFFIX`, and
        `PATTERN_ADVANCED_GLOB` in the
        `PatternMatcher` class.

        These attributes are meaningful only if the
        `scheme` and `host`
        attributes are also specified for the filter.

        `pathSuffix` and `pathAdvancedPattern` were introduced in API level 31.

    `android:fragment` `android:fragmentPrefix` `android:fragmentSuffix` `android:fragmentPattern` `android:fragmentAdvancedPattern`
    :   A matcher for a URI fragment. Do not include the `#` prefix. See above for the
        meaning of and patterns permitted in each attribute.

        To match characters that are usually URI encoded, include the raw
        (nonencoded) form in the attribute value. For example,
        `<data android:fragment="test!" />` matches `#test!` and
        `#test%21`.

        Introduced in API level 35.

    `android:query` `android:queryPrefix` `android:querySuffix` `android:queryPattern` `android:queryAdvancedPattern`
    :   A matcher for a URI query parameter (and, optionally, a value). For example, you can match URIs
        ending in `?param=value` with `<data android:query="param=value" />`.
        Do not include the `?` prefix. See above for the meaning of and patterns permitted in
        each attribute.

        To match characters that are usually URI-encoded, include the raw
        (nonencoded) form in the attribute value. For example,
        `<data android:query="test!" />` matches `?test!` and
        `?test%21`.

        Introduced in API level 35.

    `android:mimeType`
    :   A MIME media type, such as `image/jpeg` or `audio/mpeg4-generic`.
        The subtype can be the asterisk wildcard (`*`) to indicate that any
        subtype matches.

        It's common for an intent filter to declare a `<data>` element that includes
        only the `android:mimeType` attribute.

        **Note**: MIME type matching in the Android framework is
        case-sensitive, unlike formal RFC MIME types. As a result, always
        specify MIME types using lowercase letters.

introduced in:
:   API level 1

see also:
:   `<action>`
      
    `<category>`