---
title: https://developer.android.com/develop/ui/compose/text/display-text
url: https://developer.android.com/develop/ui/compose/text/display-text
source: md.txt
---

The most basic way to display text is to use the `Text` composable with a
`String` as an argument:


```kotlin
@Composable
fun SimpleText() {
    Text("Hello World")
}
```

<br />

![The words](https://developer.android.com/static/develop/ui/compose/images/text-plain.png)

## Display text from resource

We recommend you use [string resources](https://developer.android.com/develop/ui/compose/resources#strings)
instead of hardcoding `Text` values, as you can share the same strings with your
Android Views as well as preparing your app for internationalization:


```kotlin
@Composable
fun StringResourceText() {
    Text(stringResource(R.string.hello_world))
}
```

<br />

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Enable user interactions](https://developer.android.com/develop/ui/compose/text/user-interactions)
- [Thinking in Compose](https://developer.android.com/develop/ui/compose/mental-model)
- [Display emoji](https://developer.android.com/develop/ui/compose/text/emoji)