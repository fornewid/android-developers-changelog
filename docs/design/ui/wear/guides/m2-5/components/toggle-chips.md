---
title: Toggle chips  |  Wear  |  Android Developers
url: https://developer.android.com/design/ui/wear/guides/m2-5/components/toggle-chips
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [UI Design](https://developer.android.com/design/ui)
* [Wear](https://developer.android.com/design/ui/wear)
* [Guides](https://developer.android.com/design/ui/wear/guides/get-started)

# Toggle chips Stay organized with collections Save and categorize content based on your preferences.



![](/static/wear/images/toggle-chips/toggle-chips-hero.png)

A [ToggleChip](/reference/kotlin/androidx/wear/compose/material/package-summary#ToggleChip(kotlin.Boolean,kotlin.Function1,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Function1,kotlin.Function1,androidx.wear.compose.material.ToggleChipColors,kotlin.Boolean,androidx.compose.foundation.interaction.MutableInteractionSource,androidx.compose.foundation.layout.PaddingValues,androidx.compose.ui.graphics.Shape,kotlin.Function0)) is a specialized chip that allows users to select various options.

![](/static/wear/images/toggle-chips/toggle-chip.png)

Toggle chips include a bi-state toggle control. Some examples of a bi-state toggle control include a switch, radio button, or checkbox. Use toggle chips for situations in which many options may need to be quickly and easily set, such as in Settings.

## Anatomy

![](/static/wear/images/toggle-chips/slider-toggle-chip-anatomy.png)
![](/static/wear/images/toggle-chips/slider-toggle-chip-redlines.png)

Toggle chips have four slots that accommodate two text labels, one selection control and one application icon. The icon and secondary label are optional.

**A. Label  
B. Secondary label   
C. Icon   
D. Selection control  
E. Container**

## Toggle Chips Gradient

![](/static/wear/images/toggle-chips/Colour_Gradient.png)

Top/Left = 0% Surface   
Bottom/Right = 50% Primary   
(Gradient overlays on a background of Surface color)

## Selection control

![](/static/wear/images/toggle-chips/slider-switch.png)

**Switch**

Use a switch to turn a selection on or off.

![](/static/wear/images/toggle-chips/slider-radio-button.png)

**Radio button**

Use radio buttons in lists where the user can select only one option.

![](/static/wear/images/toggle-chips/slider-checkbox.png)

**Checkbox**

Use checkboxes in lists where the user can select multiple options.

![](/static/wear/images/toggle-chips/slider-split-toggle-chips.png)

**Split toggle chips**

Use split toggle chips when you want two tappable areas.

## Related components

![](/static/wear/images/toggle-chips/sliders-split-toggle-chips.png)

**Split ToggleChips**

The SplitToggleChip differs from the ToggleChip by having two tappable areas, one clickable and one with the toggle.  
  
On split toggle chips, differentiate between the tappable background area and the toggle control by making each section a different color.

## Usage

Use ToggleChips as shown in the following examples.

![](/static/wear/images/toggle-chips/sliders-usage.png)

## Adaptive layouts

![](/static/wear/images/toggle-chips/toggle-chips-adaptive-layouts-usage.png)

![](/static/wear/images/toggle-chips/sliders-anatomy-large-screens.png)

**Responsive behavior**

ToggleChips stretch to fill the available width on larger displays.   
  
Icon (24 x 24 dp)  
Container (52 x XX dp)