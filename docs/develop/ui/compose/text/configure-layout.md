---
title: Configure text layout  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/text/configure-layout
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Configure text layout Stay organized with collections Save and categorize content based on your preferences.



This page describes how to configure your text layout with parameters like
`maxLines` and `overflow`.

## Limit visible lines

To limit the number of visible lines in a `Text` composable, set the `maxLines`
parameter:

```
@Composable
fun LongText() {
    Text("hello ".repeat(50), maxLines = 2)
}

TextSnippets.kt
```

![A long text passage truncated after two lines](/static/develop/ui/compose/images/text-maxlines.png)

## Indicate text overflow

When limiting a long text, you may want to indicate a [`TextOverflow`](/reference/kotlin/androidx/compose/ui/text/style/TextOverflow),
which is only shown if the displayed text is truncated. To do so, set the
`textOverflow` parameter:

```
@Composable
fun OverflowedText() {
    Text("Hello Compose ".repeat(50), maxLines = 2, overflow = TextOverflow.Ellipsis)
}

TextSnippets.kt
```

![A long passage of text truncated after three lines, with an ellipsis at the end](/static/develop/ui/compose/images/text-overflow.png)

## Recommended for you

* Note: link text is displayed when JavaScript is off
* [Graphics in Compose](/develop/ui/compose/graphics/draw/overview)
* [Style paragraph](/develop/ui/compose/text/style-paragraph)
* [Work with fonts](/develop/ui/compose/text/fonts)