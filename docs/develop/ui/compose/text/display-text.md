---
title: Display text  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/text/display-text
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Display text Stay organized with collections Save and categorize content based on your preferences.



The most basic way to display text is to use the `Text` composable with a
`String` as an argument:

```
@Composable
fun SimpleText() {
    Text("Hello World")
}

TextSnippets.kt
```

![The words ](/static/develop/ui/compose/images/text-plain.png)

## Display text from resource

We recommend you use [string resources](/develop/ui/compose/resources#strings)
instead of hardcoding `Text` values, as you can share the same strings with your
Android Views as well as preparing your app for internationalization:

```
@Composable
fun StringResourceText() {
    Text(stringResource(R.string.hello_world))
}

TextSnippets.kt
```

## Recommended for you

* Note: link text is displayed when JavaScript is off
* [Enable user interactions](/develop/ui/compose/text/user-interactions)
* [Thinking in Compose](/develop/ui/compose/mental-model)
* [Display emoji](/develop/ui/compose/text/emoji)