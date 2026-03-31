---
title: Time text  |  Wear  |  Android Developers
url: https://developer.android.com/design/ui/wear/guides/m2-5/components/time-text
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [UI Design](https://developer.android.com/design/ui)
* [Wear](https://developer.android.com/design/ui/wear)
* [Guides](https://developer.android.com/design/ui/wear/guides/get-started)

# Time text Stay organized with collections Save and categorize content based on your preferences.



[`TimeText`](/reference/kotlin/androidx/wear/compose/material/TimeText.composable#TimeText(androidx.compose.ui.Modifier,androidx.wear.compose.material.TimeSource,androidx.compose.ui.text.TextStyle,androidx.compose.foundation.layout.PaddingValues,kotlin.Function0,kotlin.Function1,kotlin.Function0,kotlin.Function1,kotlin.Function0,kotlin.Function1))
is a layout that shows the current time at the top of the screen.

![](/static/wear/images/components/timetext-hero.png)

![](/static/wear/images/components/timetext-default.png)

**Time Text**

Use time text to display the time as well as an optional label on the top
of the screen. When the device has a round screen time text is curved.
When the device has a rectangular screen, time text is straight.

You can add an additional leading content label to the time text. When
adding leading content, the full length of the arc should not be larger
than a quarter of the watch face.

## Anatomy

![](/static/wear/images/components/timetext-anatomy.png)

When creating `TimeText` with scrollable elements such as
lists, design the `TimeText` to fade away when the element
scrolls. Use `Modifier.scrollAway` to scroll `TimeText` vertically in and out of view, based on the scroll state.

**A. Leading content  
B. Separator  
C. Time**

## Usage

To show the estimated time of arrival in a maps app, use time text with leading
content as shown in the following example.

![](/static/wear/images/components/timetext-usage.png)