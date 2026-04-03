---
title: https://developer.android.com/design/ui/wear/guides/foundations/common-layouts/tiles
url: https://developer.android.com/design/ui/wear/guides/foundations/common-layouts/tiles
source: md.txt
---

# Common layouts for tiles

Tiles provide quick access to information and actions users need to get things done. With a swipe from the watch face, a user can see how they are progressing towards their fitness goals, check the weather, and more. Launch an app or get essential tasks done quickly from tiles.

![Three tiles, two of which show 1 row with 3 columns of main content and another that shows 2 rows with 3 columns of main content](https://developer.android.com/static/wear/images/design/common-layouts-tiles-hero.png)

## Build responsive and optimized designs

To help you adapt your design layouts to larger screen sizes, we have updated the behavior of our layouts and components to have built-in responsive behavior, including percentage-based margins and padding.

If you are using our ProtoLayout templates, you can inherit these updates automatically through the latest beta release of the[Wear ProtoLayout](https://developer.android.com/jetpack/androidx/releases/wear-protolayout)Jetpack library. Also, you only need to supply layouts where you have added additional content or components after a screen size breakpoint. For full guidance and recommendations on how to take advantage of a larger screen size, view our \[tiles guidance\]\[2\]. Tiles have a fixed screen height, so we've adjusted the padding to maximize the limited screen real estate without creating unwanted clipping.

## Check that components fill the available width

<br />

All components should be built responsively. By setting the height and width to "expand," they fill the available space. Include the necessary margins to prevent content from being clipped by the rounded screen.  
![](https://developer.android.com/static/wear/images/design/tiles-steps.png)![](https://developer.android.com/static/wear/images/design/tiles-moodboard.png)![](https://developer.android.com/static/wear/images/design/tiles-buddy-note.png)

<br />

## Build adaptive and differentiated designs

To make the most of the additional space on larger screen sizes, add a size breakpoint at 225dp. This breakpoint lets you reveal additional content, include more buttons or data, or change the layout to better suit the larger screen.

This requires a different design for each breakpoint. The larger screen design (225+ dp) could include the following additional elements:

### Show the previously hidden title slot

<br />

This is advised on layouts with two rows before the breakpoint, where the title slot needs to be removed in order to ensure the min tap target of 48dp.  
![](https://developer.android.com/static/wear/images/design/tiles-messages.png)![](https://developer.android.com/static/wear/images/design/tiles-contacts.png)

<br />

### Increase the size or change the state of the existing components

<br />

This could be done in order to show more detail or make the content more glanceable.
**Note:** Don't just scale up the design. Instead, use components that respond and adapt to the available width and height. You could also use a different or larger component style, or graphic content with additional details.  
![](https://developer.android.com/static/wear/images/design/tiles-buddy-note.png)![](https://developer.android.com/static/wear/images/design/tiles-fitness.png)

<br />

### Add component slots within the current layout

<br />

By adding components, the layout provides more options or additional details. Make sure the content remains glanceable, though.  
![](https://developer.android.com/static/wear/images/design/tiles-search.png)![](https://developer.android.com/static/wear/images/design/tiles-agenda.png)![](https://developer.android.com/static/wear/images/design/tiles-fitness-goals.png)

<br />

### Add more content at the bottom

<br />

In some cases, it makes more sense to add action buttons or content in the bottom section, rather than adding components within the main slot.  
![](https://developer.android.com/static/wear/images/design/tiles-notes.png)

<br />

**Caution:** A larger display size should*never*display less information than ones that are smaller than it. This is especially relevant for custom behaviors added in at the breakpoint.

A common example of this is when components or text sizes are increased past the breakpoint and end up showing less are the larger screens. Screens should*always*show more value with increasing size.

## Responsive and adaptive behavior

The responsive and adaptive behavior depends on the three slots (sections) of the layout.

### App icon and title slot

There is no behavior change on the app icon that the system provides. The title slot automatically adapts to the wider screen size, displaying additional characters. There are proportional (percentage) internal margins on the top section to avoid any clipping when the screen size increases.
| **Note:** The title slot is optional and should be hidden before the 225dp breakpoint when using a layout with two rows in the main content section. This lets the tap targets in the main content area remain large enough on the smallest screens.

![The title appears below the app icon](https://developer.android.com/static/wear/images/design/tiles-icon-title-slot.png)

### Main slot (components)

All components within the main slot should set their width and height to "expand" so that they automatically adapt to the wider screen size. There are proportional (percentage) internal margins on the main slot section---and each row within this slot in some instances---to avoid any clipping when the screen size increases. If you use a combination of corner radius and layout, your main slot might require larger margins.

![The main slot shows 2 rows of 3 icons each](https://developer.android.com/static/wear/images/design/tiles-main-slot.png)

### Bottom slot

There is no behavior change in the bottom button or text, but the width of the button and text boxes automatically adapt to the wider screen size, and gain characters. There are proportional (percentage) internal margins on the bottom slot to avoid any clipping when the screen size increases. When no bottom slot is present, a default margin is added automatically.
![Bottom button text is More](https://developer.android.com/static/wear/images/design/tiles-bottom-slot-button.png)Tiles that include a button in the bottom slot

<br />

![Bottom slot shows a fitness goal as text](https://developer.android.com/static/wear/images/design/tiles-bottom-slot-text.png)Tiles that include text in the bottom slot

<br />

![The main content extends to the bottom of the tile](https://developer.android.com/static/wear/images/design/tiles-no-bottom-slot.png)Tiles with no bottom slot

## Create differentiated experiences

One fully customizable layout, with 60 or more permutations built into it, allows for practically limitless customization. Tiles are built on a slot-based system, so you can replace a slot from the canonical layout with any content or component, and set the component to one of the many variants and color combinations. In this case, maintain responsive behavior and follow our design recommendations.

These customizations should be limited, and shouldn't deviate from the tile template. This is to maintain consistency when users scroll through the tiles carousel on their Wear OS devices.