---
title: Style parts of text  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/quick-guides/content/style-parts-text
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Quick Guides](https://developer.android.com/develop/ui/compose/quick-guides)

# Style parts of text Stay organized with collections Save and categorize content based on your preferences.



You can style parts of text to improve readability, increase positive user
experience, and encourage greater creativity through use of colors and fonts.

## Results

![ Hello World text with multiple styles](/static/develop/ui/compose/quick-guides/content/style parts of a text display.png)


**Figure 1.** A line of text with multiple styles.

## Version compatibility

This implementation requires that your project minSDK be set to API level 21 or
higher.

### Dependencies

## Style parts of text

The following code displays the string "Hello World" using blue for the "H", red
for the "W", and black for the rest of the text. To set different styles within
a single [`Text`](/reference/kotlin/androidx/compose/material/Text.composable#Text(androidx.compose.ui.text.AnnotatedString,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.font.FontStyle,androidx.compose.ui.text.font.FontWeight,androidx.compose.ui.text.font.FontFamily,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.style.TextDecoration,androidx.compose.ui.text.style.TextAlign,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.style.TextOverflow,kotlin.Boolean,kotlin.Int,kotlin.Int,kotlin.collections.Map,kotlin.Function1,androidx.compose.ui.text.TextStyle)) composable, use the following code:

```
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

TextSnippets.kt
```

### Key points about the code

* Uses [`buildAnnotatedString`](/reference/kotlin/androidx/compose/ui/text/package-summary#buildAnnotatedString(kotlin.Function1)) that returns an [`AnnotatedString`](/reference/kotlin/androidx/compose/ui/text/AnnotatedString)
  string to set different styles within text.
* Styles part of text with [`SpanStyle`](/reference/kotlin/androidx/compose/ui/text/SpanStyle), a configuration that allows
  character-level styling.

## Collections that contain this guide

This guide is part of these curated Quick Guide collections that cover
broader Android development goals:

![](/static/images/quick-guides/collection-illustration.png)

![](/static/images/picto-icons/collection.svg)

### Display text

Text is a central piece of any UI. Find out different ways
you can present text in your app to provide a delightful user experience.

[Quick guide collection](/develop/ui/compose/quick-guides/collections/display-text)

![](/static/images/picto-icons/help.svg)

## Have questions or feedback

Go to our frequently asked questions page and learn about quick guides or reach out and let us know your thoughts.

[Go to FAQ](/quick-guides/faq)
[Leave feedback](https://issuetracker.google.com/issues/new?component=1573691&template=1993320)