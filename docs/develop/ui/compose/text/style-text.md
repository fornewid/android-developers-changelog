---
title: https://developer.android.com/develop/ui/compose/text/style-text
url: https://developer.android.com/develop/ui/compose/text/style-text
source: md.txt
---

The `Text` composable has multiple optional parameters to style its content.
Below, we've listed parameters that cover the most common use cases with text.
For all the parameters of `Text`, see the [Compose Text
source code](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:compose/material/material/src/commonMain/kotlin/androidx/compose/material/Text.kt;l=91).

Whenever you set one of these parameters, you're applying the style to the whole
text value. If you need to apply multiple styles within the same line or
paragraphs, see the section on [multiple inline
styles](https://developer.android.com/develop/ui/compose/text/style-text#multiple-styles).

## Common text stylings

The following sections describe common ways to style your text.

### Change text color


```kotlin
@Composable
fun BlueText() {
    Text("Hello World", color = Color.Blue)
}
```

<br />

![The words](https://developer.android.com/static/develop/ui/compose/images/text-blue.png)

### Change text size


```kotlin
@Composable
fun BigText() {
    Text("Hello World", fontSize = 30.sp)
}
```

<br />

![The words](https://developer.android.com/static/develop/ui/compose/images/text-big.png)

### Make text italic

Use the `fontStyle` parameter to italicize text (or set another
[`FontStyle`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/font/FontStyle)).


```kotlin
@Composable
fun ItalicText() {
    Text("Hello World", fontStyle = FontStyle.Italic)
}
```

<br />

![The words](https://developer.android.com/static/develop/ui/compose/images/text-italic.png)

### Make text bold

Use the `fontWeight` parameter to bold text (or set another [`FontWeight`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/font/FontWeight)).


```kotlin
@Composable
fun BoldText() {
    Text("Hello World", fontWeight = FontWeight.Bold)
}
```

<br />

![The words](https://developer.android.com/static/develop/ui/compose/images/text-bold.png)

### Add shadow

The `style` parameter lets you set an object of type [`TextStyle`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/TextStyle)
and configure multiple parameters, for example shadow.
[`Shadow`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/Shadow) receives a color
for the shadow, the offset, or where it is located in respect of the `Text` and
the blur radius which is how blurry it looks.


```kotlin
@Composable
fun TextShadow() {
    val offset = Offset(5.0f, 10.0f)
    Text(
        text = "Hello world!",
        style = TextStyle(
            fontSize = 24.sp,
            shadow = Shadow(
                color = Color.Blue, offset = offset, blurRadius = 3f
            )
        )
    )
}
```

<br />

![The words](https://developer.android.com/static/develop/ui/compose/images/text-shadow.png)

## Add multiple styles in text

To set different styles within the same [`Text`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#Text(androidx.compose.ui.text.AnnotatedString,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.font.FontStyle,androidx.compose.ui.text.font.FontWeight,androidx.compose.ui.text.font.FontFamily,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.style.TextDecoration,androidx.compose.ui.text.style.TextAlign,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.style.TextOverflow,kotlin.Boolean,kotlin.Int,kotlin.Int,kotlin.collections.Map,kotlin.Function1,androidx.compose.ui.text.TextStyle))
composable, use an [`AnnotatedString`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/AnnotatedString),
a string that can be annotated with styles of arbitrary annotations.

`AnnotatedString` is a data class containing:

- A `Text` value
- A `List` of `SpanStyleRange`, equivalent to inline styling with position range within the text value
- A `List` of `ParagraphStyleRange`, specifying text alignment, text direction, line height, and text indent styling

[`TextStyle`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/TextStyle) is for use
in the `Text` composable, whereas [`SpanStyle`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/SpanStyle)
and [`ParagraphStyle`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/ParagraphStyle)
is for use in `AnnotatedString`. For more information about multiple styles in
a paragraph, see [Add multiple styles in a paragraph](https://developer.android.com/develop/ui/compose/text/style-paragraph#multiple-paragraph-styles).

`AnnotatedString` has a [type-safe
builder](https://kotlinlang.org/docs/reference/type-safe-builders.html)
to make it easier to create: [`buildAnnotatedString`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/package-summary#buildAnnotatedString(kotlin.Function1)).


```kotlin
@Composable
fun MultipleStylesInText() {
    Text(
        buildAnnotatedString {
            withStyle(style = SpanStyle(color = Color.Blue)) {
                append("H")
            }
            append("ello ")

            withStyle(style = SpanStyle(fontWeight = FontWeight.Bold, color = Color.Red)) {
                append("W")
            }
            append("orld")
        }
    )
}
```

<br />

![The words](https://developer.android.com/static/develop/ui/compose/images/text-inline-styles.png)

### Display HTML with links in text

Use [`AnnotatedString.fromHtml()`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/AnnotatedString.Companion#(androidx.compose.ui.text.AnnotatedString.Companion).fromHtml(kotlin.String,androidx.compose.ui.text.TextLinkStyles,androidx.compose.ui.text.LinkInteractionListener)) to display HTML-formatted text with
clickable links in your Jetpack Compose application. This function converts a
string with HTML tags into an `AnnotatedString`, allowing for styling and link
handling.

#### Example: HTML with styled link

This snippet renders HTML-formatted text with a link, applying specific styling
to the link:


```kotlin
@Composable
fun AnnotatedHtmlStringWithLink(
    modifier: Modifier = Modifier,
    htmlText: String = """
       <h1>Jetpack Compose</h1>
       <p>
           Build <b>better apps</b> faster with <a href="https://www.android.com">Jetpack Compose</a>
       </p>
    """.trimIndent()
) {
    Text(
        AnnotatedString.fromHtml(
            htmlText,
            linkStyles = TextLinkStyles(
                style = SpanStyle(
                    textDecoration = TextDecoration.Underline,
                    fontStyle = FontStyle.Italic,
                    color = Color.Blue
                )
            )
        ),
        modifier
    )
}
```

<br />

##### Key points about the code

- `AnnotatedString.fromHtml()` converts the `htmlText` string into an
  [`AnnotatedString`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/AnnotatedString). The `linkStyles` parameter customizes link appearance.

- `TextLinkStyles` defines the style for links within the HTML. `SpanStyle` sets
  text decoration, font style, and color for the links.

- The [`Text`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#Text(androidx.compose.ui.text.AnnotatedString,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.font.FontStyle,androidx.compose.ui.text.font.FontWeight,androidx.compose.ui.text.font.FontFamily,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.style.TextDecoration,androidx.compose.ui.text.style.TextAlign,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.style.TextOverflow,kotlin.Boolean,kotlin.Int,kotlin.Int,kotlin.collections.Map,kotlin.Function1,androidx.compose.ui.text.TextStyle)) composable displays the resulting `AnnotatedString`.

##### Result

This snippet enables "Jetpack Compose" as a clickable link, styled with blue color,
underlined, and italicized:
![An H1 heading 'Jetpack Compose' followed by 'Build better apps with Jetpack
Compose', where Jetpack Compose is a clickable link styled with blue color,
underline, and italics.](https://developer.android.com/static/develop/ui/compose/images/text/AnnotatedHtmlStringWithLink.png) **Figure 2.** A heading and paragraph, where 'Jetpack Compose' in the paragraph is a clickable, styled link.

## Enable advanced styling with `Brush`

To enable more advanced text styling, you can use the [`Brush`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/Brush) API with
[`TextStyle`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/TextStyle) and [`SpanStyle`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/SpanStyle). In any place where you would typically
use `TextStyle` or `SpanStyle`, you can now also use `Brush`.

> [!CAUTION]
> **Caution:** The current usage of the Brush API in `TextStyle` is experimental. Experimental APIs can change in the future.

### Use a brush for text styling

Configure your text using a built-in brush within `TextStyle`. For example, you
can configure a [`linearGradient`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/Brush.Companion#linearGradient(kotlin.Array,androidx.compose.ui.geometry.Offset,androidx.compose.ui.geometry.Offset,androidx.compose.ui.graphics.TileMode)) brush to your text as follows:


```kotlin
val gradientColors = listOf(Cyan, LightBlue, Purple /*...*/)

Text(
    text = text,
    style = TextStyle(
        brush = Brush.linearGradient(
            colors = gradientColors
        )
    )
)
```

<br />

![Using Brush API’s `linearGradient` function with a defined list of colors.](https://developer.android.com/static/develop/ui/compose/images/text-designmain.png) **Figure 3.** Using Brush API's `linearGradient` function with a defined list of colors.

You are not limited to this particular color scheme or style of coloring. While
we have provided a simple example to highlight, use any of the built-in
[brushes](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/Brush) or even just a [`SolidColor`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/SolidColor) to enhance your text.

### Integrations

Since you can use `Brush` alongside both `TextStyle` and `SpanStyle`,
integration with [`TextField`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#TextField(androidx.compose.ui.text.input.TextFieldValue,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.Boolean,androidx.compose.ui.text.TextStyle,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Boolean,androidx.compose.ui.text.input.VisualTransformation,androidx.compose.foundation.text.KeyboardOptions,androidx.compose.foundation.text.KeyboardActions,kotlin.Boolean,kotlin.Int,kotlin.Int,androidx.compose.foundation.interaction.MutableInteractionSource,androidx.compose.ui.graphics.Shape,androidx.compose.material.TextFieldColors)) and [`buildAnnotatedString`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/package-summary#buildAnnotatedString(kotlin.Function1)) is seamless.

For more information about using the brush API within a `TextField`, see
[Style input with Brush API](https://developer.android.com/develop/ui/compose/text/user-input#style-input).

#### Additional styling using `SpanStyle`

##### Apply a brush to a span of text

If you only want to apply a brush to parts of your text, use
[`buildAnnotatedString`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/package-summary#buildAnnotatedString(kotlin.Function1)) and the [`SpanStyle`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/SpanStyle) API, along with your brush
and gradient of choice.


```kotlin
Text(
    text = buildAnnotatedString {
        append("Do not allow people to dim your shine\n")
        withStyle(
            SpanStyle(
                brush = Brush.linearGradient(
                    colors = rainbowColors
                )
            )
        ) {
            append("because they are blinded.")
        }
        append("\nTell them to put some sunglasses on.")
    }
)
```

<br />

![Using a default brush with linearGradient as a style for Text.](https://developer.android.com/static/develop/ui/compose/images/text-style.png) **Figure 4.** Using a default brush with `linearGradient` as a style for `Text`.

##### Opacity in a span of text

To adjust the opacity of a particular span of text, use [`SpanStyle`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/SpanStyle)'s
optional `alpha` parameter. Use the same brush for
both parts of a text, and change the alpha parameter in the corresponding span.
In the code sample, the first span of text displays at half opacity
(`alpha =.5f`) while the second displays at full opacity (`alpha = 1f`).


```kotlin
val brush = Brush.linearGradient(colors = rainbowColors)

buildAnnotatedString {
    withStyle(
        SpanStyle(
            brush = brush, alpha = .5f
        )
    ) {
        append("Text in ")
    }
    withStyle(
        SpanStyle(
            brush = brush, alpha = 1f
        )
    ) {
        append("Compose ❤️")
    }
}
```

<br />

![Using buildAnnotatedString and SpanStyle’s alpha parameter, along with linearGradient to add opacity to a span of text.](https://developer.android.com/static/develop/ui/compose/images/text-opacity.png) **Figure 5.** Using `buildAnnotatedString` and `SpanStyle`'s alpha parameter, along with `linearGradient` to add opacity to a span of text.

## Apply marquee effect to text

You can apply the [`basicMarquee`](https://developer.android.com/reference/kotlin/androidx/compose/ui/Modifier#(androidx.compose.ui.Modifier).basicMarquee(kotlin.Int,androidx.compose.foundation.MarqueeAnimationMode,kotlin.Int,kotlin.Int,androidx.compose.foundation.MarqueeSpacing,androidx.compose.ui.unit.Dp)) modifier to any composable to
produce an animated scrolling effect. The marquee effect occurs if the content
is too wide to fit in the available constraints. By default, `basicMarquee` has
certain configurations (such as velocity and initial delay) set, but you can
modify these parameters to customize the effect.

The following snippet implements a basic marquee effect on a `Text` composable:


```kotlin
@Composable
fun BasicMarqueeSample() {
    // Marquee only animates when the content doesn't fit in the max width.
    Column(Modifier.width(400.dp)) {
        Text(
            "Learn about why it's great to use Jetpack Compose",
            modifier = Modifier.basicMarquee(),
            fontSize = 50.sp
        )
    }
}
```

<br />

**Figure 6.** The `basicMarquee` modifier applied to text.

## Additional resources

- [Brushing Up on Compose Text Coloring](https://medium.com/androiddevelopers/brushing-up-on-compose-text-coloring-84d7d70dd8fa)
- [Animating brush Text coloring in Compose](https://medium.com/androiddevelopers/animating-brush-text-coloring-in-compose-%EF%B8%8F-26ae99d9b402)
- [Support multiple links in a single string of text](https://developer.android.com/develop/ui/compose/quick-guides/content/support-multiple-links)

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Style paragraph](https://developer.android.com/develop/ui/compose/text/style-paragraph)
- [Material Design 2 in Compose](https://developer.android.com/develop/ui/compose/designsystems/material)
- [Graphics Modifiers](https://developer.android.com/develop/ui/compose/graphics/draw/modifiers)