---
title: https://developer.android.com/develop/ui/compose/quick-guides/content/support-multiple-links
url: https://developer.android.com/develop/ui/compose/quick-guides/content/support-multiple-links
source: md.txt
---

<br />

You can support multiple links in a single string of text to perform different
actions when clicking a subsection of text.

## Results

![One text string containing two different links](https://developer.android.com/static/develop/ui/compose/quick-guides/content/multiple-links.png) **Figure 1.** A screenshot of one text string containing two different links.

## Version compatibility

This implementation requires that your project minSDK be set to API level 21 or
higher.

### Dependencies

<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/support-multiple-links_4f7e31a439c9cc9f72d357797fb8d5ca9a12ef24f6f470510958c451c1f45542.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

## Display multiple links in a single string

This snippet embeds multiple clickable links into a single string of text:


```kotlin
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
```

<br />

### Key points about the code

- Uses the [`buildAnnotatedString`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/package-summary#buildAnnotatedString(kotlin.Function1)) function to create an annotated string of text.
- Specifies the the link and text styling by passing them as arguments of the [`LinkAnnotation.Url()`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/LinkAnnotation.Url) function (itself passed as an argument of the [`withLink()`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/AnnotatedString.Builder#(androidx.compose.ui.text.AnnotatedString.Builder).withLink(androidx.compose.ui.text.LinkAnnotation,kotlin.Function1)) function). A click listener is built into `LinkAnnotation.Url()`.
- Adds text using [`append()`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/AnnotatedString.Builder#append(kotlin.CharSequence,kotlin.Int,kotlin.Int)) in the body of the `withLink` function.
- Repeats this process to add another linked text segment.

## Collections that contain this guide

This guide is part of these curated Quick Guide collections that cover
broader Android development goals:
![](https://developer.android.com/static/images/quick-guides/collection-illustration.png) ![](https://developer.android.com/static/images/picto-icons/collection.svg)

### Display text

Text is a central piece of any UI. Find out different ways you can present text in your app to provide a delightful user experience. [Quick guide collection](https://developer.android.com/develop/ui/compose/quick-guides/collections/display-text) ![](https://developer.android.com/static/images/picto-icons/help.svg)

## Have questions or feedback

Go to our frequently asked questions page and learn about quick guides or reach out and let us know your thoughts. [Go to FAQ](https://developer.android.com/quick-guides/faq) [Leave feedback](https://issuetracker.google.com/issues/new?component=1573691&template=1993320)