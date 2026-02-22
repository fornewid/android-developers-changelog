---
title: https://developer.android.com/design/ui/wear/guides/m2-5/foundations/adaptive-layouts
url: https://developer.android.com/design/ui/wear/guides/m2-5/foundations/adaptive-layouts
source: md.txt
---

# Get started with adaptive layouts

![](https://developer.android.com/static/wear/images/design/getting-started-adaptive-header.png)

The Wear OS ecosystem is made up of devices that have a wide variety of screen sizes. Utilizing adaptive UI principles is critical to delivering the highest quality experience for all users.

## What is adaptive UI?

Adaptive UIs stretch and change to make the best possible use of all available screen space, no matter what size screen they're rendered on.

Adaptive UIs change responsively, using components and methods built directly into the layout logic. These layouts also utilize screen size breakpoints---applying a different design on different screen sizes---to create an even richer experience for users.

## Key screen sizes

<br />

Learn about key reference sizes to keep in mind as you design new experiences

[Screen sizes](https://developer.android.com/design/ui/wear/guides/foundations/screen-sizes)  
![Key screen sizes](https://developer.android.com/static/wear/images/design/key-screen-sizes.png)

<br />

<br />

## Types of layouts

When designing for adaptive layouts on the round screen, scrolling and non-scrolling views each have unique requirements for scaling UI elements and maintaining a balanced layout and composition.

<br />

![Example of scrolling view](https://developer.android.com/static/wear/images/design/scrolling-view.gif)

**Scrolling views**

All top, bottom, and side margins should be defined in percentages to avoid clipping and provide proportional scaling of elements.  
![Example of non-scrolling view](https://developer.android.com/static/wear/images/design/non-scrolling-view.gif)

**Non-scrolling views**

All margins should be defined in percentages and vertical constraints should be defined such that the main content in the middle can stretch to fill the available area.

<br />

## Add value through adaptive layouts and design practices

When designing for adaptive layouts on the round screen, scrolling and non-scrolling views each have unique requirements for scaling UI elements and maintaining a balanced layout and composition.

The following images are broad suggestions; examples are for illustrative purposes only. View each component or surface page for detailed, contextual, responsive guidance.

<br />

![Example of responsive layouts](https://developer.android.com/static/wear/images/design/content-at-a-glance.png)

**More content at a glance**

Responsive layouts allow for more chips, more cards, more lines of text, and more buttons to fit on a single screen  
![Example of alternate layouts at different breakpoints](https://developer.android.com/static/wear/images/design/content-elements-visible.png)

**More content elements visible**

Utilize new layouts, applied at defined screen size breakpoints, to allow for the introduction of new content when possible, giving the user additional value on devices with larger screen sizes.

<br />

<br />

![Example of using screen space to improve glanceability](https://developer.android.com/static/wear/images/design/glanceability.png)

**Improved glanceability**

Use extra screen space to provide larger containers, larger text, thicker rings, and more granular data visualization to provide better glanceability for users.  
![Example of larger tap targets](https://developer.android.com/static/wear/images/design/usability.png)

**Improved usability**

Use extra screen space to provide bigger tap targets, greater visual hierarchy, and additional space between content items to make interfaces easier and more comfortable to interact with.

<br />

<br />

![Example of updated components](https://developer.android.com/static/wear/images/design/optimized-compositions.png)

**Optimized compositions**

Utilize our updated components and templates to offer a better look and feel for our UIs across all screen sizes.  

<br />

## App quality

<br />

Our quality guidelines are organized into three levels. Enable the best possible experience for your users by meeting guidelines in all three tiers.

[Quality guidelines](https://developer.android.com/docs/quality-guidelines/wear-app-quality)  
![Quality guidelines](https://developer.android.com/static/wear/images/design/quality-guidelines.png)

<br />

<br />

*** ** * ** ***

<br />

**Ready for all screen sizes**

Make sure your app is delivering a quality experience across all screen sizes. Create layouts that fully use the available app space.

[Get started](https://developer.android.com/design/ui/wear/guides/foundations/larger-screens-ready)  
**Responsive and optimized**

Deliver more content to users on devices which allow for it, and utilize responsive layouts that automatically adapt to different screen sizes.

[Get started](https://developer.android.com/design/ui/wear/guides/foundations/larger-screens-optimized)  
**Adaptive and differentiated**

Make the most of additional real estate by utilizing breakpoints to offer powerful new experiences on larger screens which are not possible on devices with smaller screens.

[Get started](https://developer.android.com/design/ui/wear/guides/foundations/larger-screens-differentiated)

<br />

*** ** * ** ***

## Utilize established canonical layouts

<br />

Use established canonical layouts to help your UIs adapt smoothly across a range of device sizes.

Our canonical layouts have been developed thoughtfully to offer a high quality experience across all screen sizes.

[Canonical layouts](https://developer.android.com/design/ui/wear/guides/foundations/canonical-adaptive-layouts)  
![Canonical layouts](https://developer.android.com/static/wear/images/design/canonical-layouts.png)

<br />