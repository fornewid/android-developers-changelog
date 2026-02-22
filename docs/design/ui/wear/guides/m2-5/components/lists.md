---
title: https://developer.android.com/design/ui/wear/guides/m2-5/components/lists
url: https://developer.android.com/design/ui/wear/guides/m2-5/components/lists
source: md.txt
---

# Lists

![](https://developer.android.com/static/wear/images/lists/lists-hero.png)

Lists are continuous, vertical indexes of elements. Use[ScalingLazyColumn](https://developer.android.com/reference/kotlin/androidx/wear/compose/material/package-summary#ScalingLazyColumn(androidx.compose.ui.Modifier,androidx.wear.compose.material.ScalingLazyListState,androidx.compose.foundation.layout.PaddingValues,kotlin.Boolean,androidx.compose.foundation.layout.Arrangement.Vertical,androidx.compose.ui.Alignment.Horizontal,androidx.compose.foundation.gestures.FlingBehavior,kotlin.Boolean,androidx.wear.compose.material.ScalingParams,androidx.wear.compose.material.ScalingLazyListAnchorType,androidx.wear.compose.material.AutoCenteringParams,kotlin.Function1))to create lists on Wear OS.  
![](https://developer.android.com/static/wear/images/lists/lists-ScalingLazyColumn.png)  
`ScalingLazyColumn`is a customization of`LazyColumn`that's built specifically for Wear OS. Lists offer scaling and transparency, which allows content to shrink and fade at the top and bottom of the screen to help users see what to focus on. Lists are anchored on the center of the screen, which gives additional emphasis to the items in the middle of the list.  

Lists can contain items of fixed or variable height. List content should have margin enough to accommodate for circular screens.

<br />

<br />

## Padding

Standardized Paddings are used when creating a list depending on the element. If further vertical padding is needed for more complex lists, spacing is set in multiples of 4 dp for consistency.  
![](https://developer.android.com/static/wear/images/lists/lists-sections.png)  
**Between sections**

Padding between top, middle and bottom section should be set to 16 dp.

<br />

<br />

![](https://developer.android.com/static/wear/images/lists/lists-titles-content.png)  
**Between titles and content**

Padding between top, middle and bottom section should be set to 12 dp.

<br />

<br />

![](https://developer.android.com/static/wear/images/lists/lists-slots.png)  
**Between slots**

Padding between slots in the middle section should be set to 16 dp.

<br />

<br />

![](https://developer.android.com/static/wear/images/lists/lists-groups.png)  
**Between groups**

Padding between groups within a slot should be set to 8 dp.

<br />

<br />

![](https://developer.android.com/static/wear/images/lists/lists-elements.png)  
**Between elements**

Padding between elements within a group should be set to 4 dp.

<br />

<br />

## Snapping behavior

To give emphasis to a list item when scrolling, use snapping. Use snapping when items are tall but not taller than the screen.

Snapping behavior comes in two forms.`ItemCenter`uses the center of the item as a reference point.`ItemStart`uses the edge of the item as a reference point. Use the first to center one item on the screen, use the second to center two items on the screen. Set this behavior using the[anchorType](https://developer.android.com/reference/kotlin/androidx/wear/compose/material/ScalingLazyListAnchorType)parameter.

For further control over the snapping behavior in a list, set`flingBehavior`to`ScalingLazyColumnDefaults.snapFlingBehavior`and`rotaryScrollableBehavior`to`RotaryScrollableDefaults.snapBehavior`.

<br />

<br />

## Usage

See the following examples of how to use lists on watches.

![](https://developer.android.com/static/wear/images/lists/lists-usage.png)

## Adaptive layouts

The following images show several examples of adaptive layouts. For implementation guidance, visit the[develop for different screen sizes](https://developer.android.com/training/wearables/compose/screen-size)page.

![](https://developer.android.com/static/wear/images/lists/lists-adaptive-layouts-usage.png)  
![](https://developer.android.com/static/wear/images/lists/lists-anatomy-large-screens.png)  
**Responsive behavior**

Lists components stretch to fill the available width on larger displays.

<br />

<br />

### Top margins

Top margins vary depending on which elements are in the top section.

**List starts with Title**

![](https://developer.android.com/static/wear/images/lists/lists-chips-top-margins-title-adaptive-layouts.png)

**List starts with 1 or 2+ buttons**

![](https://developer.android.com/static/wear/images/lists/lists-chips-top-margins-buttons-adaptive-layouts.png)

**List starts with other elements**

![](https://developer.android.com/static/wear/images/lists/lists-chips-top-margins-other-adaptive-layouts.png)

![](https://developer.android.com/static/wear/images/lists/lists-chips-top-margins-other-2-adaptive-layouts.png)

![](https://developer.android.com/static/wear/images/lists/lists-chips-top-margins-other-2-adaptive-layout-layout.png)

### Bottom margins

Bottom margins vary depending on which elements are in the bottom section.

**List ends with buttons**

![](https://developer.android.com/static/wear/images/lists/lists-chips-bottom-margins-adaptive-layout-list-ends-with-buttons.png)

**List ends with other elements**

![](https://developer.android.com/static/wear/images/lists/lists-chips-bottom-adaptive-layouts-list-ends-with-other-elements.png)

![](https://developer.android.com/static/wear/images/lists/lists-chips-bottom-adaptive-layouts-list-ends-with-other-elements-2.png)

![](https://developer.android.com/static/wear/images/lists/lists-chips-bottom-adaptive-layouts-list-ends-with-other-elements-3.png)

### Side margins

Side margins uses a standard percentage of 5.2% across all list types to ensure scalability on larger displays.

![](https://developer.android.com/static/wear/images/lists/lists-side-margins-adpaptive-layouts-settings.png)

![](https://developer.android.com/static/wear/images/lists/lists-side-margins-adpaptive-layouts-cards.png)

![](https://developer.android.com/static/wear/images/lists/lists-side-margins-adpaptive-layouts-3.png)

### Internal margins

**Titles**

There's an added 7.3% internal margin to ensure titles don't clip.

![](https://developer.android.com/static/wear/images/lists/lists-internal-margins-adpaptive-layouts-titles.png)

**Bottom buttons**

Bottom buttons fill the available width past the 225 breakpoint. To keep visual hierarchy, there's an added internal padding of 14.56% on larger screens.

![](https://developer.android.com/static/wear/images/lists/lists-internal-margins-adaptive-layout-bottom-buttons.png)