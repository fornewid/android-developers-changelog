---
title: https://developer.android.com/guide/topics/resources/string-resource
url: https://developer.android.com/guide/topics/resources/string-resource
source: md.txt
---

A string resource provides text strings for your application with optional text
styling and formatting. There are three types of resources that can provide
your application with strings:

[**String**](https://developer.android.com/guide/topics/resources/string-resource#String)
:   XML resource that provides a single string.

[**String Array**](https://developer.android.com/guide/topics/resources/string-resource#StringArray)
:   XML resource that provides an array of strings.

[**Quantity Strings (Plurals)**](https://developer.android.com/guide/topics/resources/string-resource#Plurals)
:   XML resource that carries different strings for pluralization.

All strings are capable of applying some styling markup and formatting
arguments. For information about styling and formatting strings, see the
section about [Formatting and Styling](https://developer.android.com/guide/topics/resources/string-resource#FormattingAndStyling).

## String

A single string that can be referenced from the application code (such as a
composable function) or from other resource files.

> [!NOTE]
> **Note:** A string is a simple resource that is referenced using the value provided in the `name` attribute (not the name of the XML file). So, you can combine string resources with other simple resources in the one XML file, under one `<resources>` element.

file location:
:   `res/values/filename.xml`  

    The filename is arbitrary. The `<string>` element's `name` is used as the
    resource ID.

compiled resource datatype:
:   Resource pointer to a `https://developer.android.com/reference/java/lang/String`.

resource reference:
:
    In Kotlin: `R.string.string_name`  

    In XML: `@string/string_name`

syntax:
:

    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <resources>
        <string
            name="string_name"
            >text_string</string>
    </resources>
    ```

elements:
:

    `<resources>`
    :   **Required.** This must be the root node.

        No attributes.

    `<string>`
    :   A string, which can include styling tags. Beware that you must escape apostrophes and
        quotation marks. For more information about how to properly style and format your strings see [Formatting and Styling](https://developer.android.com/guide/topics/resources/string-resource#FormattingAndStyling), below.

        attributes:

        `name`
        :   *String*. A name for the string. This name is used as the resource
            ID.


example:
:   XML file saved at `res/values/strings.xml`:

    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <resources>
        <string name="hello">Hello!</string>
    </resources>
    ```


    This application code retrieves a string from inside a composable with `https://developer.android.com/develop/ui/compose/resources#strings`:

    ```kotlin
    @Composable
    fun Greeting() {
        Text(text = stringResource(R.string.hello))
    }
    ```


    **Note:** To retrieve a string outside of a composable function, use `context.getString(R.string.hello)`.


    You can also reference string resources from other XML files, such as your `AndroidManifest.xml`:

    ```xml
    <activity
        android:name=".MainActivity"
        android:label="@string/hello" />
    ```


## String array

An array of strings that can be referenced from the application.

> [!NOTE]
> **Note:** A string array is a simple resource that is referenced using the value provided in the `name` attribute (not the name of the XML file). As such, you can combine string array resources with other simple resources in the one XML file, under one `<resources>` element.

file location:
:   `res/values/filename.xml`  

    The filename is arbitrary. The `<string-array>` element's `name` is used as the
    resource ID.

compiled resource datatype:
:   Resource pointer to an array of `https://developer.android.com/reference/java/lang/String`s.

resource reference:
:
    In Kotlin: `R.array.string_array_name`  

    In XML: `@[package:]array/string_array_name`

syntax:
:

    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <resources>
        <string-array
            name="string_array_name">
            <item
                >text_string</item>
        </string-array>
    </resources>
    ```

elements:
:

    `<resources>`
    :   **Required.** This must be the root node.

        No attributes.

    `<string-array>`
    :   Defines an array of strings. Contains one or more `<item>` elements.

        attributes:

        `name`
        :   *String*. A name for the array. This name is used as the resource
            ID to reference the array.

    `<item>`
    :   A string, which can include styling tags. The value can be a reference to another
        string resource. Must be a child of a `<string-array>` element. Beware that you
        must escape apostrophes and
        quotation marks. See [Formatting and Styling](https://developer.android.com/guide/topics/resources/string-resource#FormattingAndStyling), below, for
        information about how to properly style and format your strings.

        No attributes.


example:
:   XML file saved at `res/values/strings.xml`:

    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <resources>
        <string-array name="planets_array">
            <item>Mercury</item>
            <item>Venus</item>
            <item>Earth</item>
            <item>Mars</item>
        </string-array>
    </resources>
    ```


    This application code retrieves a string array from inside a composable with `stringArrayResource()`:


    ```kotlin
    @Composable
    fun PlanetList() {
        val planets: Array =
            stringArrayResource(R.array.planets_array)
        // Render the array, e.g. inside a LazyColumn.
    }
    ```


    **Note:** To retrieve a string array outside of a composable function, use `context.resources.getStringArray(R.array.planets_array)`.


## Quantity strings (plurals)

Different languages have different rules for grammatical agreement with
quantity. In English, for example, the quantity 1 is a special case. We write
"1 book", but for any other quantity we'd write "*n* books". This distinction
between singular and plural is very common, but other languages make finer
distinctions. The full set supported by Android is `zero`, `one`, `two`, `few`,
`many`, and `other`.

The rules for deciding which case to use for a given language and quantity can
be very complex, so Android provides you with methods such as
[`pluralStringResource()`](https://developer.android.com/develop/ui/compose/resources#string-plurals) to select the appropriate resource for you.

Although historically called "quantity strings" (and still called that in API),
quantity strings should *only* be used for plurals. It would be a mistake to
use quantity strings to implement something like Gmail's "Inbox" versus
"Inbox (12)" when there are unread messages, for example. It might seem
convenient to use quantity strings instead of an `if` statement, but it's
important to note that some languages (such as Chinese) don't make these
grammatical distinctions at all, so you'll always get the `other` string.

The selection of which string to use is made solely based on grammatical
*necessity* . In English, a string for `zero` is ignored even if the quantity is
0, because 0 isn't grammatically different from 2, or any other number except 1
("zero books", "one book", "two books", and so on). Conversely, in Korean
*only* the `other` string is ever used.

Don't be misled either by the fact that, say, `two` sounds like it could only
apply to the quantity 2: a language may require that 2, 12, 102 (and so on) are
all treated like one another but differently to other quantities. Rely on your
translator to know what distinctions their language actually insists upon.

If your message doesn't contain the quantity number, it is probably not a good
candidate for a plural. For example, in Lithuanian the singular form is used for
both 1 and 101, so "1 book" is translated as "1 knyga", and "101 books" is
translated as "101 knyga". Meanwhile "a book" is "knyga" and "many books" is
"daug knygų". If an English plural message contains "a book" (singular) and
"many books" (plural) without the actual number, it can be translated as
"knyga" (a book)/"daug knygų" (many books), but with Lithuanian rules, it will
show "knyga" (a single book), when the number happens to be 101.

It's often possible to avoid quantity strings by using quantity-neutral
formulations such as "Books: 1". This makes your life and your translators'
lives easier, if it's an acceptable style for your application.

On API 24+ you can use the much more powerful ICU [`MessageFormat`](https://developer.android.com/reference/kotlin/android/icu/text/MessageFormat)
class instead.

> [!NOTE]
> **Note:** A plurals collection is a simple resource that is referenced using the value provided in the `name` attribute (not the name of the XML file). As such you can combine plurals resources with other simple resources in the one XML file, under one `<resources>` element.

file location:
:   `res/values/filename.xml`  

    The filename is arbitrary. The `<plurals>` element's `name` is used as the
    resource ID.

resource reference:
:
    In Kotlin: `R.plurals.plural_name`

syntax:
:

    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <resources>
        <plurals
            name="plural_name">
            <item
                quantity=["zero" | "one" | "two" | "few" | "many" | "other"]
                >text_string</item>
        </plurals>
    </resources>
    ```

elements:
:

    `<resources>`
    :   **Required.** This must be the root node.

        No attributes.

    `<plurals>`
    :   A collection of strings, of which, one string is provided depending on the amount of
        something. Contains one or more `<item>` elements.

        attributes:

        `name`
        :   *String*. A name for the pair of strings. This name is used as the
            resource ID.

    `<item>`
    :   A plural or singular string. The value can be a reference to another
        string resource. Must be a child of a `<plurals>` element. Beware that you must
        escape apostrophes and quotation marks. See [Formatting and
        Styling](https://developer.android.com/guide/topics/resources/string-resource#FormattingAndStyling), below, for information about how to properly style and format your strings.

        attributes:

        `quantity`
        :   *Keyword* . A value indicating when this string should be used. Valid
            values, with non-exhaustive examples in parentheses:

            | Value | Description |
            |---|---|
            | `zero` | When the language requires special treatment of the number 0 (as in Arabic). |
            | `one` | When the language requires special treatment of numbers like one (as with the number 1 in English and most other languages; in Russian, any number ending in 1 but not ending in 11 is in this class). |
            | `two` | When the language requires special treatment of numbers like two (as with 2 in Welsh, or 102 in Slovenian). |
            | `few` | When the language requires special treatment of "small" numbers (as with 2, 3, and 4 in Czech; or numbers ending 2, 3, or 4 but not 12, 13, or 14 in Polish). |
            | `many` | When the language requires special treatment of "large" numbers (as with numbers ending 11-99 in Maltese). |
            | `other` | When the language does not require special treatment of the given quantity (as with all numbers in Chinese, or 42 in English). |


example:

:   XML file saved at `res/values/strings.xml`:

    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <resources>
        <plurals name="numberOfSongsAvailable">
            <!--
                 As a developer, you should always supply "one" and "other"
                 strings. Your translators will know which strings are actually
                 needed for their language. Always include %d in "one" because
                 translators will need to use %d for languages where "one"
                 doesn't mean 1 (as explained above).
              -->
            <item quantity="one">%d song found.</item>
            <item quantity="other">%d songs found.</item>
        </plurals>
    </resources>
    ```

    XML file saved at `res/values-pl/strings.xml`:

    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <resources>
        <plurals name="numberOfSongsAvailable">
            <item quantity="one">Znaleziono %d piosenkę.</item>
            <item quantity="few">Znaleziono %d piosenki.</item>
            <item quantity="other">Znaleziono %d piosenek.</item>
        </plurals>
    </resources>
    ```

    This application code retrieves a plural string from inside a composable with `https://developer.android.com/develop/ui/compose/resources#string-plurals`:

    ```kotlin
    @Composable
    fun SongCount(count: Int) {
        Text(
            text = pluralStringResource(
                R.plurals.numberOfSongsAvailable,
                count,
                count,
            )
        )
    }
    ```

    When using the `https://developer.android.com/develop/ui/compose/resources#string-plurals` function, you need to pass the `count` twice if your string includes
    [string formatting](https://developer.android.com/guide/topics/resources/string-resource#FormattingAndStyling) with a number. For example, for the string
    `%d songs found`, the first `count` parameter selects the appropriate plural string and
    the second `count` parameter is inserted into the `%d` placeholder. If your plural
    strings do not include string formatting, you don't need to pass the third parameter to `https://developer.android.com/develop/ui/compose/resources#string-plurals`.

    **Note:** To retrieve a plural string outside of a composable function, use `context.resources.getQuantityString(R.plurals.numberOfSongsAvailable, count, count)`.

## Format and style

Here are a few important things you should know about how to properly
format and style your string resources.

### Handle special characters

When a string contains characters that have special usage in XML, you must
escape the characters according to the standard XML/HTML escaping rules. If you
need to escape a character that has special meaning in Android you should use a
preceding backslash.

By default Android will collapse sequences of whitespace characters into a
single space. You can avoid this by enclosing the relevant part of your string
in double quotes. In this case all whitespace characters (including new lines)
will get preserved within the quoted region. Double quotes will allow you to
use regular single unescaped quotes as well.

| Character | Escaped form(s) |
|---|---|
| @ | `\@` |
| ? | `\?` |
| New line | `\n` |
| Tab | `\t` |
| U+XXXX Unicode character | `\uXXXX` |
| Single quote (`'`) | Any of the following: - `\'` - Enclose the entire string in double quotes (`"This'll work"`, for example) |
| Double quote (`"`) | `\"` Note that surrounding the string with single quotes does not work. |

Whitespace collapsing and Android escaping happen after your resource file
gets parsed as XML. This means that `<string> &#32; &#8200; &#8195;</string>`
(space, punctuation space, Unicode Em space) all collapse to a single space
(`" "`), because they are all Unicode spaces after the file is parsed as an XML.
To preserve those spaces as they are, you can either quote them
(`<string>" &#32; &#8200; &#8195;"</string>`)
or use Android escaping
(`<string> \u0032 \u8200 \u8195</string>`).

> [!NOTE]
> **Note:** From XML parser's perspective, there is no difference between `<string>"Test this"</string>` and `<string>&amp;quot;Test this&amp;quot;</string>` whatsoever. Both forms will not show any quotes but trigger Android whitespace-preserving quoting (that will have no practical effect in this case).

### Formatting strings

If you need to format your strings, then you can do so by putting your format
arguments in the string resource, as demonstrated by the following example
resource.

```xml
<string name="welcome_messages">Hello, %1$s! You have %2$d new messages.</string>
```

This application code formats the string from inside a composable by passing
arguments directly into `stringResource()`:

```kotlin
@Composable
fun WelcomeMessage(username: String, mailCount: Int) {
    Text(
        text = stringResource(
            R.string.welcome_messages,
            username,
            mailCount,
        )
    )
}
```

### Styling with HTML markup

You can add styling to your strings with HTML markup. For example:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string name="welcome">Welcome to <b>Android</b>!</string>
</resources>
```

The following HTML elements are supported:

- Bold: `<b>`
- Italic: `<i>`, `<cite>`, `<dfn>`, `<em>`
- 25% larger text: `<big>`
- 20% smaller text: `<small>`
- Setting font properties: `<font face="font_family" color="hex_color">`. Examples of possible font families include `monospace`, `serif`, and `sans_serif`.
- Setting a monospace font family: `<tt>`
- Strikethrough: `<s>`, `<strike>`, `<del>`
- Underline: `<u>`
- Superscript: `<sup>`
- Subscript: `<sub>`
- Bullet points: `<ul>`, `<li>`
- Line breaks: `<br>`
- Division: `<div>`
- CSS style: `<span style="color|background_color|text-decoration">`
- Paragraphs: `<p dir="rtl | ltr" style="...">`

In some cases, you may want to create a styled text resource that is also used
as a format string. Normally, this doesn't work because formatting methods,
such as `stringResource()`, strip all the style information from the string.
The work-around to this is to write the HTML tags with escaped entities, which
are then recovered with `AnnotatedString.fromHtml()`, after the formatting
takes place. For example:

1. Store your styled text resource as an HTML-escaped string:

   ```xml
   <resources>
     <string name="welcome_messages">Hello, %1$s! You have &lt;b>%2$d new messages&lt;/b>.</string>
   </resources>
   ```

   In this formatted string, a `<b>` element is added. Notice that the opening bracket is
   HTML-escaped, using the `&lt;` notation.
2. Then format the string as usual, but also call `AnnotatedString.fromHtml()` to convert the HTML text into a styled Compose string.

Because `fromHtml()` formats all HTML entities, be sure to escape any possible
HTML characters in the strings you use with the formatted text, using
`TextUtils.htmlEncode()`.

```kotlin
import android.text.TextUtils
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.text.AnnotatedString
import androidx.compose.ui.text.fromHtml

@Composable
fun WelcomeHtmlMessage(username: String, mailCount: Int) {
    // Escape the username in case it contains characters like "<" or "&"
    val escapedUsername = TextUtils.htmlEncode(username)

    val text = stringResource(
        R.string.welcome_messages,
        escapedUsername,
        mailCount,
    )

    Text(
        text = AnnotatedString.fromHtml(text)
    )
}
```

### Styling with AnnotatedString

An `AnnotatedString` is a Compose text object that you can style with
properties such as color and font weight. Build styled text programmatically
using `buildAnnotatedString` and `withStyle`.

This application code creates a single text element with mixed styles:

```kotlin
@Composable
fun StyledGreeting() {
    val styled = buildAnnotatedString {
        append("Welcome to ")
        withStyle(SpanStyle(fontWeight = FontWeight.Bold)) {
            append("Android")
        }
        append("!")
    }
    Text(text = styled)
}
```

To apply color, font size, and text decoration, use `SpanStyle`. To apply
paragraph-level styling (like alignment or line height), use `ParagraphStyle`:

```kotlin
@Composable
fun RichText() {
    val text = buildAnnotatedString {
        withStyle(ParagraphStyle(lineHeight = 24.sp, textAlign = TextAlign.Center)) {
            withStyle(SpanStyle(color = Color.Gray)) {
                append("Hello, ")
            }
            withStyle(
                SpanStyle(
                    fontWeight = FontWeight.Bold,
                    color = Color.Red,
                )
            ) {
                append("world")
            }
            append("!")
        }
    }
    Text(text = text)
}
```

> [!NOTE]
> **Note:** If you need to read complex `<annotation>` tags directly from an XML string resource, you must retrieve the string as a legacy `Spanned` object using `context.getText(R.string.your_string)` and convert the spans into an `AnnotatedString` manually.

Building the `AnnotatedString` directly is the recommended approach for
single-language apps or static text in Compose. However, for styled text that
requires localization, see the XML `<annotation>` approach detailed in the next
section.

### Styling translated strings with annotations

For strings that need custom styling *and* translation, define the
`<annotation>` tag in each locale's `strings.xml`. Translators preserve the
annotation regardless of where it lands in the sentence. Read the string with
`context.resources.getText()`, walk its `Annotation` spans, and convert the
result into an `AnnotatedString`:

```kotlin
@Composable
fun AnnotatedTitle() {
    val context = LocalContext.current
    val source = context.resources.getText(R.string.title) as SpannedString
    val text = buildAnnotatedString {
        append(source.toString())
        source.getSpans(0, source.length, Annotation::class.java)
            .forEach { annotation ->
                if (annotation.key == "font" &&
                    annotation.value == "title_emphasis") {
                    addStyle(
                        SpanStyle(
                            fontFamily = FontFamily(
                                Font(R.font.permanent_marker)
                            )
                        ),
                        source.getSpanStart(annotation),
                        source.getSpanEnd(annotation),
                    )
                }
            }
    }
    Text(text = text)
}
```

The `<annotation>` tag in your XML is unchanged. Only the retrieval code
differs. Translators still move the tag to wrap the correct word in each
language.

## Additional resources

For more information about string resources, see the following additional
resources:

### Documentation

- [Display text](https://developer.android.com/develop/ui/compose/text/display-text)
- [Style text](https://developer.android.com/develop/ui/compose/text/style-text)
- [Style paragraph](https://developer.android.com/develop/ui/compose/text/style-paragraph)
- [Resources in Compose](https://developer.android.com/develop/ui/compose/resources#strings)

### Views content

- [String resources (Views)](https://developer.android.com/topic/architecture/views/resources/string-resource-views)