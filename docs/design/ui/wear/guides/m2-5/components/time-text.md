---
title: https://developer.android.com/design/ui/wear/guides/m2-5/components/time-text
url: https://developer.android.com/design/ui/wear/guides/m2-5/components/time-text
source: md.txt
---

# Time text

[`TimeText`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material/package-summary#TimeText(androidx.compose.ui.Modifier,androidx.wear.compose.material.TimeSource,androidx.compose.ui.text.TextStyle,androidx.compose.foundation.layout.PaddingValues,kotlin.Function0,kotlin.Function1,kotlin.Function0,kotlin.Function1,kotlin.Function0,kotlin.Function1))is a layout that shows the current time at the top of the screen.

![](https://developer.android.com/static/wear/images/components/timetext-hero.png)  
![](https://developer.android.com/static/wear/images/components/timetext-default.png)  
**Time Text**

Use time text to display the time as well as an optional label on the top of the screen. When the device has a round screen time text is curved. When the device has a rectangular screen, time text is straight.

You can add an additional leading content label to the time text. When adding leading content, the full length of the arc should not be larger than a quarter of the watch face.

## Anatomy

![](https://developer.android.com/static/wear/images/components/timetext-anatomy.png)  
When creating`TimeText`with scrollable elements such as lists, design the`TimeText`to fade away when the element scrolls. Use[Modifier.scrollAway](https://developer.android.com/reference/kotlin/androidx/wear/compose/material/package-summary#(androidx.compose.ui.Modifier).scrollAway(androidx.compose.foundation.ScrollState,androidx.compose.ui.unit.Dp))to scroll`TimeText`vertically in and out of view, based on the scroll state.

**A. Leading content
B. Separator
C. Time**

## Usage

To show the estimated time of arrival in a maps app, use time text with leading content as shown in the following example.

![](https://developer.android.com/static/wear/images/components/timetext-usage.png)