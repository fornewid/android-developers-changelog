---
title: https://developer.android.com/design/ui/wear/guides/m2-5/components/buttons
url: https://developer.android.com/design/ui/wear/guides/m2-5/components/buttons
source: md.txt
---

# Buttons

![](https://developer.android.com/static/wear/images/buttons/button-hero.png)

Use a[Button](https://developer.android.com/reference/kotlin/androidx/wear/compose/material/package-summary#Button(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.wear.compose.material.ButtonColors,androidx.compose.foundation.interaction.MutableInteractionSource,androidx.compose.ui.graphics.Shape,androidx.wear.compose.material.ButtonBorder,kotlin.Function1))component for actions that are well understood by users and don't need a text label. Buttons are distinguished from chips by their circular shape.

## Anatomy

<br />

![Button anatomy diagram](https://developer.android.com/static/wear/images/buttons/button-anatomy.png)  
**A. Content**

Buttons have a single slot reserved for an icon or text. Choose an icon that is relevant to the action the button performs. You can use text with a maximum of three characters if an icon is unable to describe the relevant action. Consider the use of a Chip component if an icon cannot clearly describe the action

**B. Container**

Button containers are limited to a single solid color fill.

<br />

<br />

## Button types

<br />

![Toggle button examples](https://developer.android.com/static/wear/images/buttons/buttons-related-components-toggle-buttons.png)

**Toggle buttons**

[Toggle buttons](https://developer.android.com/reference/kotlin/androidx/wear/compose/material/package-summary#ToggleButton(kotlin.Boolean,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.wear.compose.material.ToggleButtonColors,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function1))enable users to toggle between two states.  
![Compact buttons example](https://developer.android.com/static/wear/images/buttons/buttons-related-components-compact-buttons.png)

**Compact buttons**

[Compact buttons](https://developer.android.com/reference/kotlin/androidx/wear/compose/material/package-summary#CompactButton(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.wear.compose.material.ButtonColors,androidx.compose.ui.unit.Dp,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function1))appear smaller but have a larger tappable area. The default tappable area is 48x48 dp.

<br />

## Hierarchy

<br />

![Button hierarchy diagram](https://developer.android.com/static/wear/images/buttons/buttons-hierarchy.png)  
Use different color fills to denote button hierarchy.

**High emphasis**

High emphasis buttons contain actions that are primary to the app. For high emphasis buttons use Primary or Secondary colors for the container and On Primary and On Secondary colors for the content. For more information see[Wear Material Theming](https://developer.android.com/training/wearables/design/theme).

**Medium emphasis**

Medium emphasis buttons are distinguished by a less contrasting color fill. They contain actions that are less important than the primary actions. Use the Surface color for the container and the On Surface color for the content.

Alternatively, use the custom[OutlinedButton](https://developer.android.com/reference/kotlin/androidx/wear/compose/material/package-summary#OutlinedButton(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.wear.compose.material.ButtonColors,androidx.compose.foundation.interaction.MutableInteractionSource,androidx.compose.ui.graphics.Shape,androidx.wear.compose.material.ButtonBorder,kotlin.Function1))component for a medium emphasis button. This has a transparent background, a primary variant colored stroke of 60% opacity, and primary colored content.
**Low emphasis (icon only)**

<br />

Low emphasis buttons are distinguished by having no fill. They are best suited for smaller areas on the watch face where a compact arrangement is needed. Use the On Surface colour for the content.

<br />

<br />

## Sizes

Use buttons of different sizes to emphasize or de-emphasize actions.

<br />

![Large button diagram](https://developer.android.com/static/wear/images/buttons/buttons-large.png)

**Large**

Icon (30 x 30 dp)  
Container (60 x 60 dp)  
![Default button diagram](https://developer.android.com/static/wear/images/buttons/buttons-default.png)

**Default**

Icon (26 x 26 dp)  
Container (52 x 52 dp)

<br />

<br />

![Small button diagram](https://developer.android.com/static/wear/images/buttons/buttons-related-sizes-small.png)

**Small**

Icon (24 x 24 dp)  
Container (48 x 48 dp)  
![Extra small button diagram](https://developer.android.com/static/wear/images/buttons/buttons-xsmall.png)

**Extra Small**

Icon (24 x 24 dp)  
Container (32 x 32 dp)

It's recommended to add additional padding around this button to create a tap target of at least 48 dp. This is our minimum tap target size for accessibility.

<br />

## Usage

Use standard buttons to enable the user to take a single action such as accepting or declining a call, or starting a timer.

![](https://developer.android.com/static/wear/images/buttons/buttons-usage-media-workout.png)

Use toggle buttons to allow the user to turn an option on or off, such as selecting and deselecting days of the week or pausing and restarting a timer.

![](https://developer.android.com/static/wear/images/buttons/buttons-usage-alarm-timer.png)

## Adaptive layouts

![](https://developer.android.com/static/wear/images/buttons/buttons-adaptive-layouts-buttons.png)

### **Responsive behavior**

<br />

![One button anatomy diagram](https://developer.android.com/static/wear/images/buttons/anatomy-large-screen-one-button.png)

**1 button**

The internal padding will remain the same, and the margins should be percentages in order to stop the buttons from stretching too far, and keeping a relative size.  
![Two buttons anatomy diagram](https://developer.android.com/static/wear/images/buttons/anatomy-large-screen-two-buttons.png)

**2 buttons**

When there are 2 buttons, percentage internal margins are added in order to stop the buttons from stretching too far, and keeping a relative size.

<br />

### **IMEs**

![](https://developer.android.com/static/wear/images/buttons/buttons-adaptive-layout-IME-buttons.png)

**1 or 2 Buttons**

IMEs with 2 or a single button lockup always stretch all the way to the side margins regardless of screen size.

![](https://developer.android.com/static/wear/images/buttons/Comparison-three-buttons.png)

**3 Buttons**

On screens smaller than 225 dp, the buttons remain circular and do not stretch. On larger screens, 225 dp or larger, the buttons stretch all the way to the side margins.