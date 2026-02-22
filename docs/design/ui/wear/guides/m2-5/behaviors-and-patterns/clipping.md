---
title: https://developer.android.com/design/ui/wear/guides/m2-5/behaviors-and-patterns/clipping
url: https://developer.android.com/design/ui/wear/guides/m2-5/behaviors-and-patterns/clipping
source: md.txt
---

# Prevent text truncation and content clipping

Smartwatches have smaller screen sizes than handheld devices, so it's critical to arrange and display elements in a manner that users can access and that efficiently uses the available screen space. To help your items fit the screen, use the correct amount of padding and margins as specified by the[Material guidelines](https://m3.material.io/foundations/layout/understanding-layout/spacing).

Even when your design fits the screen, elements of your interface may be truncated or clipped when the user does one of the following:

- Changes the display language.
- Changes the text size.
- Enables the**Bold text**system setting.

It's crucial to test your designs with these considerations in mind to ensure they adapt seamlessly to different user environments.

## Keep interactive elements fully visible

If your interface includes interactive elements, check that users can scroll these elements fully into view, especially if these elements are placed at the edges of a page. If your app uses the[Horologist](https://github.com/google/horologist)library, use the[`responsive()`layout factory](https://github.com/google/horologist/blob/main/docs/compose-layout.md). Otherwise, use spacers and add margins to the top and bottom of a[`ScalingLazyColumn`](https://developer.android.com/reference/kotlin/androidx/wear/compose/foundation/lazy/package-summary#ScalingLazyColumn%28androidx.compose.ui.Modifier,androidx.wear.compose.foundation.lazy.ScalingLazyListState,androidx.compose.foundation.layout.PaddingValues,kotlin.Boolean,androidx.compose.foundation.layout.Arrangement.Vertical,androidx.compose.ui.Alignment.Horizontal,androidx.compose.foundation.gestures.FlingBehavior,kotlin.Boolean,androidx.wear.compose.foundation.lazy.ScalingParams,androidx.wear.compose.foundation.lazy.ScalingLazyListAnchorType,androidx.wear.compose.foundation.lazy.AutoCenteringParams,kotlin.Function1%29)object to prevent the first and last list items from always being clipped.

## Use chips instead of cards for dense layouts

If you need a denser layout, use[`CompactChip`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material/package-summary#CompactChip(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Function1,kotlin.Function1,androidx.wear.compose.material.ChipColors,kotlin.Boolean,androidx.compose.foundation.interaction.MutableInteractionSource,androidx.compose.foundation.layout.PaddingValues,androidx.compose.ui.graphics.Shape,androidx.wear.compose.material.ChipBorder))instead of cards. The larger surface area of cards makes it much more difficult to prevent text truncation and content clipping.

## Consider screen size effects on truncation and clipping

Depending on the Wear OS device's screen size, you have a smaller or larger space for additional text and buttons to be visible:

### Design for percentage margins, not fixed margins

To create content that adapts responsively to the Wear OS device's screen size, apply percentage margins, where the size of each margin is relative to the screen size. In cases where items sit on the top or bottom of the screen, apply additional inner padding to minimize content clipping from the screen's curved edge. In contrast, the space at the top and bottom increases when a group of content is small enough to fit on one screen.

![](https://developer.android.com/static/wear/images/design/percentage-margins-do.png)  
check_circle

### Do

Components must adhere to the percentage margins so that their size scales with the screen's size. This way, the content of your screen always fills the space available and isn't cropped by the screen's edges.

![](https://developer.android.com/static/wear/images/design/percentage-margins-dont.png)  
cancel

### Don't

Don't use the maximum space available for text without considering how it may truncate on smaller screens and affect the functionality of your design.

### Use the character limits required by smaller screens

In most cases, larger screens can show more text and content before truncation. Even though more horizontal space might be available, however, always design for the smallest screen size to create a consistent experience across devices.

For example, a button may have space for more characters on a larger screen before truncation, but if it's an important call to action that is vital to the user experience, then use text that's short enough to appear entirely, without truncating, on a small device's screen.

Alternatively, if the tile shows variable content, such as text fetched from a server, plan for the possibility that this text is truncated on smaller screens.

![](https://developer.android.com/static/wear/images/design/character-limits-do.png)  
check_circle

### Do

Text which affects the functionality of your design, like call-to-action buttons, is designed with the smallest screen in mind. The additional space on larger screens can show additional lines of text after the breakpoint. The number of lines of text depends on the component and context.

![](https://developer.android.com/static/wear/images/design/character-limits-dont.png)  
cancel

### Don't

Don't write text that consumes the maximum space available on a larger screen without considering how it may appear truncated on smaller screens and affect the functionality of your design.