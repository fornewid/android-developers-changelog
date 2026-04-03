---
title: https://developer.android.com/develop/ui/compose/text/configure-layout
url: https://developer.android.com/develop/ui/compose/text/configure-layout
source: md.txt
---

This page describes how to configure your text layout with parameters like
`maxLines` and `overflow`.

## Limit visible lines

To limit the number of visible lines in a `Text` composable, set the `maxLines`
parameter:


```kotlin
@Composable
fun LongText() {
    Text("hello ".repeat(50), maxLines = 2)
}
```

<br />

![A long text passage truncated after two lines](https://developer.android.com/static/develop/ui/compose/images/text-maxlines.png)

## Indicate text overflow

When limiting a long text, you may want to indicate a [`TextOverflow`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/style/TextOverflow),
which is only shown if the displayed text is truncated. To do so, set the
`textOverflow` parameter:


```kotlin
@Composable
fun OverflowedText() {
    Text("Hello Compose ".repeat(50), maxLines = 2, overflow = TextOverflow.Ellipsis)
}
```

<br />

![A long passage of text truncated after three lines, with an ellipsis at the end](https://developer.android.com/static/develop/ui/compose/images/text-overflow.png)

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Graphics in Compose](https://developer.android.com/develop/ui/compose/graphics/draw/overview)
- [Style paragraph](https://developer.android.com/develop/ui/compose/text/style-paragraph)
- [Work with fonts](https://developer.android.com/develop/ui/compose/text/fonts)