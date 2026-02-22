---
title: https://developer.android.com/design/ui/tv/guides/components/buttons
url: https://developer.android.com/design/ui/tv/guides/components/buttons
source: md.txt
---

# Buttons help users initiate actions or flow. Choose from different types of buttons to inform emphasis.

![Cover Buttons](https://developer.android.com/static/design/ui/tv/guides/components/images/covers/cover-buttons.webp)

## Resources

|      Type      |                                                                                                                                                                                                                                                                  Link                                                                                                                                                                                                                                                                   |  Status   |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| Design         | [Design source (Figma)](https://goo.gle/tv-desing-kit)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Available |
| Implementation | [Jetpack Compose](https://developer.android.com/reference/kotlin/androidx/tv/material3/package-summary#Button(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Boolean,androidx.tv.material3.ButtonScale,androidx.tv.material3.ButtonGlow,androidx.tv.material3.ButtonShape,androidx.tv.material3.ButtonColors,androidx.compose.ui.unit.Dp,androidx.tv.material3.ButtonBorder,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function1)) | Available |

## Highlights

- Choose the type of button based on the importance of the action. The more important the action is, the more emphasis on the button.
- Buttons should have clear labels to indicate the action they perform.
- Place buttons logically on the screen---where users likely expect to find them.
- Don't overuse buttons. Too many buttons on a screen disrupt the visual hierarchy.

## Variants

There are six types of buttons:

1. Filled button
2. Outline button
3. Icon button
4. Outline icon button
5. Long button
6. Image button

![Filled button](https://developer.android.com/static/design/ui/tv/guides/components/images/buttons/button-1.webp)![Outline button](https://developer.android.com/static/design/ui/tv/guides/components/images/buttons/button-2.webp)![Icon button](https://developer.android.com/static/design/ui/tv/guides/components/images/buttons/button-3.webp)![Outline icon button](https://developer.android.com/static/design/ui/tv/guides/components/images/buttons/button-4.webp)  
![Long button](https://developer.android.com/static/design/ui/tv/guides/components/images/buttons/button-5.webp)![Image button](https://developer.android.com/static/design/ui/tv/guides/components/images/buttons/button-6.webp)

Choose the type of button based on the importance of the action. The more important the action is, the more emphasis its button should have.

![Button Emphasis](https://developer.android.com/static/design/ui/tv/guides/components/images/buttons/button-emphasis.webp)

## Filled and outline button

Filled buttons have the most visual impact and should be used for important, final actions that complete a flow, like Save, Join now, Confirm, or Download.

Outlined buttons are medium emphasis buttons. They contain actions that are important, but aren't the primary action in an app. Outlined buttons pair well with filled buttons to indicate an alternative, secondary action.

### Anatomy

![Filled and outline button anatomy](https://developer.android.com/static/design/ui/tv/guides/components/images/buttons/button-anatomy.webp)

1. Container
2. Label text
3. Icon (optional)

### States

Visual representation of a component's status.

![Filled and outline button states](https://developer.android.com/static/design/ui/tv/guides/components/images/buttons/button-states.webp)

1. Default
2. Focused
3. Pressed

### Specification

![Filled and outline button specifications](https://developer.android.com/static/design/ui/tv/guides/components/images/buttons/button-specs.webp)

## Icon and outline icon button

Use icon buttons to display actions in a compact layout. Icon buttons can represent opening actions such as opening an overflow menu or search, or represent binary actions that can be toggled on and off, such as favorite or bookmark. They are also used to play or pause media.

Icon buttons can be defined in three sizes: small, medium and large.

### Anatomy

![Icon & outline icon button Anatomy](https://developer.android.com/static/design/ui/tv/guides/components/images/buttons/icon-button-anatomy.webp)

1. Container
2. Icon

### States

![Icon & outline icon button States](https://developer.android.com/static/design/ui/tv/guides/components/images/buttons/icon-button-states.webp)

1. Default
2. Focused
3. Pressed

States are visual representations used to communicate the status of a component or interactive element.

### Spec

![Icon & outline icon button Specs](https://developer.android.com/static/design/ui/tv/guides/components/images/buttons/icon-button-specs.webp)

## Wide button

Wide buttons are used for higher-emphasis than usual buttons. They contain actions that are important. Buttons that represent related options are grouped together. The group should share a common surface.

### Anatomy

![Wide button Anatomy](https://developer.android.com/static/design/ui/tv/guides/components/images/buttons/wide-button-anatomy.webp)

1. Container
2. Leading icon
3. Title
4. Subtitle

### States

![Wide button States](https://developer.android.com/static/design/ui/tv/guides/components/images/buttons/wide-button-states.webp)

1. Default
2. Focused
3. Pressed

States are visual representations used to communicate the status of a component or interactive element.

### Specifications

![Wide button Spec](https://developer.android.com/static/design/ui/tv/guides/components/images/buttons/wide-button-specs.webp)

## Image button

Image buttons are typically used to display thumbnails of the content that is available in the next level of navigation. They are usually grouped together with related actions, and the group should share a common surface.

### Anatomy

![Image button Spec](https://developer.android.com/static/design/ui/tv/guides/components/images/buttons/image-button-anatomy.webp)

1. Container
2. Leading icon
3. Title
4. Subtitle
5. Image layer, which consists of:
   1. Scrim (state overlay)
   2. Gradient (based on surface color)
   3. Image

### States

![Image button States](https://developer.android.com/static/design/ui/tv/guides/components/images/buttons/image-button-states.webp)

1. Default
2. Focused
3. Pressed

States are visual representations used to communicate the status of a component or interactive element.

### Spec

![Image button Specs](https://developer.android.com/static/design/ui/tv/guides/components/images/buttons/image-button-specs.webp)

## Usage

Buttons are generally used to communicate actions that a user can take. They are frequently found in UI elements such as dialogs, modal windows, forms, cards, and toolbars.

Buttons are just one option for representing actions in your UI. Don't overuse them. Too many buttons on a screen disrupts the visual hierarchy.

![Button Anatomy](https://developer.android.com/static/design/ui/tv/guides/components/images/buttons/buttons-anatomy.webp)

1. Container
2. Icon
3. Label text
4. Title
5. Subtitle
6. Image

### Container

Buttons display a container around content. The container scales by 1.1x on focus, maintaining the internal padding. Here are some considerations for container:

- Set container width based on content with consistent padding.
- Set the container's relative position to the responsive layout grid.
- Use solid color containers for filled buttons.
- Use stroke and fill color on focus for outlined buttons. On focus, the container gets a fill color along with outline.
- For wide and image buttons, container width is set according to the layout grid.
- Container size, position, and alignment can change as its parent container scales.

![Button container](https://developer.android.com/static/design/ui/tv/guides/components/images/buttons/container.webp)

Text and icon button containers have fully rounded corners. Wide and image button containers have rounded containers of 12dp.  
![](https://developer.android.com/static/design/ui/tv/guides/components/images/buttons/container-do.webp)  
check_circle

### Do

Filled button width can be responsive to the layout grid. Icons and label text remain centered when button width increases.  
![](https://developer.android.com/static/design/ui/tv/guides/components/images/buttons/container-caution.webp)  
warning

### Caution

For wide and image buttons, container width is defined by the parent container. Content anchors to the left.

### Icon

Icons visually communicate the button's action and help draw attention. They should be placed on the leading side of the button. Icons are always vertically centered within the container.  
![](https://developer.android.com/static/design/ui/tv/guides/components/images/buttons/icons-do.webp)  
check_circle

### Do

Icon buttons with different sizes can be grouped together.  
![](https://developer.android.com/static/design/ui/tv/guides/components/images/buttons/icons-dont-1.webp)  
cancel

### Don't

Don't vertically align an icon and text in the center of a button  
![](https://developer.android.com/static/design/ui/tv/guides/components/images/buttons/icons-dont-2.webp)  
warning

### Caution

Don't use two icons in the same button

### Label text

Label text is the most important element of a button. It describes the action that occurs if a user taps a button.

Use sentence case for button label text, capitalizing the first word and proper nouns. Avoid wrapping text. For maximum legibility, label text should remain on a single line.  
![](https://developer.android.com/static/design/ui/tv/guides/components/images/buttons/label-do.webp)  
check_circle

### Do

Use sentence case for button label text, capitalizing the first word and proper nouns.  
![](https://developer.android.com/static/design/ui/tv/guides/components/images/buttons/label-caution.webp)  
warning

### Caution

Ensure legibility for label text when placing outlined buttons on top of images; use scrims to maintain contrast.

### Image

Image buttons always have a gradient overlay and scrim on top of the image in the background. The gradient overlay is set according to container color. The scrim changes according to state.

## Button groups

Buttons appear together in a row or column to maintain consistent navigation between actions. The following sections describe considerations.

### Inform hierarchy

Each screen should have one primary action that is represented by a prominent, typically wide, button. The button should be easier to see and understand. Other buttons should be less prominent and shouldn't distract users from the primary action.

The first button in the group acts as the primary action since focus lands on it first.

### Maintain linear layout

<br />

![Example of Button row layout](https://developer.android.com/static/design/ui/tv/guides/components/images/buttons/button-row.webp)  
![Example of Button column layout](https://developer.android.com/static/design/ui/tv/guides/components/images/buttons/button-column.webp)

<br />

1. Row layout
2. Column layout

### Use variants logically

In column layout, single button variants should be maintained. In row layout, different variants can be clustered together in a button group but the logic should be clear. Filled and outline buttons can be used in the same group, but ensure clear hierarchy for actions.  
![](https://developer.android.com/static/design/ui/tv/guides/components/images/buttons/button-group-1.webp)  
check_circle

### Do

Use the same button variants in a button group.  
![](https://developer.android.com/static/design/ui/tv/guides/components/images/buttons/button-group-2.webp)  
cancel

### Don't

Mix long buttons and image buttons in a button group.  
![](https://developer.android.com/static/design/ui/tv/guides/components/images/buttons/button-group-3.webp)  
warning

### Caution

In row layout, text and icon buttons can be placed together. Ensure that the primary button has higher emphasis.  
![](https://developer.android.com/static/design/ui/tv/guides/components/images/buttons/button-group-4.webp)  
check_circle

### Do

In column layout, use only one button variant.