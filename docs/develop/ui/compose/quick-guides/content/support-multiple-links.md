---
title: Support multiple links in a single string of text  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/quick-guides/content/support-multiple-links
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Quick Guides](https://developer.android.com/develop/ui/compose/quick-guides)

# Support multiple links in a single string of text Stay organized with collections Save and categorize content based on your preferences.




You can support multiple links in a single string of text to perform different
actions when clicking a subsection of text.

## Results

![One text string containing two different links](/static/develop/ui/compose/quick-guides/content/multiple-links.png)


**Figure 1.** A screenshot of one text string containing two different links.

## Version compatibility

This implementation requires that your project minSDK be set to API level 21 or
higher.

### Dependencies

## Display multiple links in a single string

This snippet embeds multiple clickable links into a single string of text:

```
@Composable
fun AnnotatedStringWithLinkSample() {
    // Display multiple links in the text
    Text(
        buildAnnotatedString {
            append("Go to the ")
            withLink(
                LinkAnnotation.Url(
                    "https://developer.android.com/",
                    TextLinkStyles(style = SpanStyle(color = Color.Blue))
                )
            ) {
                append("Android Developers ")
            }
            append("website, and check out the")
            withLink(
                LinkAnnotation.Url(
                    "https://developer.android.com/jetpack/compose",
                    TextLinkStyles(style = SpanStyle(color = Color.Green))
                )
            ) {
                append("Compose guidance")
            }
            append(".")
        }
    )
}

TextSnippets.kt
```

### Key points about the code

* Uses the [`buildAnnotatedString`](/reference/kotlin/androidx/compose/ui/text/package-summary#buildAnnotatedString(kotlin.Function1)) function to create an annotated string
  of text.
* Specifies the the link and text styling by passing them as arguments of the
  [`LinkAnnotation.Url()`](/reference/kotlin/androidx/compose/ui/text/LinkAnnotation.Url) function (itself passed as an argument of the
  [`withLink()`](/reference/kotlin/androidx/compose/ui/text/AnnotatedString.Builder#(androidx.compose.ui.text.AnnotatedString.Builder).withLink(androidx.compose.ui.text.LinkAnnotation,kotlin.Function1)) function). A click listener is built into
  `LinkAnnotation.Url()`.
* Adds text using [`append()`](/reference/kotlin/androidx/compose/ui/text/AnnotatedString.Builder#append(kotlin.CharSequence,kotlin.Int,kotlin.Int)) in the body of the `withLink` function.
* Repeats this process to add another linked text segment.

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