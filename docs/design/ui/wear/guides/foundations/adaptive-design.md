---
title: https://developer.android.com/design/ui/wear/guides/foundations/adaptive-design
url: https://developer.android.com/design/ui/wear/guides/foundations/adaptive-design
source: md.txt
---

# Overview

The Wear OS ecosystem consists of devices with a wide variety of screen sizes. Using adaptive UI principles is critical to delivering the highest quality experience for everyone. Adaptive UIs stretch and change to make the best possible use of all available screen space, no matter what size screen they're rendered on. Adaptive UIs change responsively, using components and methods built directly into the layout logic. These layouts also utilize screen size breakpoints - applying a different design on different screen sizes - to create an even richer experience for everyone.

## Essential terms

**Responsive design:**A design approach in which layouts dynamically format and position elements such as buttons, text fields, and dialogs for an optimal user experience. Automatically offer users additional value on larger screens by utilizing responsive design practices. Whether it's more text visible at a glance, more actions on screen, or larger, more accessible tap targets, responsive practices provide an enhanced experience for users of large screens.

**Adaptive design:**A design approach in which the interface changes based on known user, device, or environmental conditions. Adaptive design in Material includes layout and component adaptations.

## Types of layouts

When designing for adaptive layouts on the round screen, scrolling and non-scrolling views each have unique requirements for scaling UI elements and maintaining a balanced layout and composition.

<br />

![alt text](https://developer.android.com/static/wear/images/design/adaptivedesign-scrollinglayout.png)

**Adaptive scrolling layouts**

All top, bottom, and side margins should be defined in percentages to avoid clipping and provide proportional scaling of elements.  
![alt text](https://developer.android.com/static/wear/images/design/adaptivedesign-nonscrollinglayout.png)

**Adaptive non-scrolling layouts**

All margins should be defined in percentages, and vertical constraints should be defined such that the main content in the middle can stretch to fill the available area.

<br />

## Key screen sizes

Many of the watches within the Wear OS ecosystem have different screen sizes. When designing for Wear OS, keep in mind that your app surfaces are displayed on these different screen sizes. Keep the following principles in mind when designing for different devices.

<br />

![alt text](https://developer.android.com/static/wear/images/design/adaptivedesign-smallfirst.png)

**Small first**

Always design for small supported round-screen emulator first: 204dp - 216dp. If the layout is dense render it at 192dp to ensure nothing breaks - be sure to also test it as 192dp with larger font sizes. Then, optimize for larger devices.  
![alt text](https://developer.android.com/static/wear/images/design/adaptivedesign-designforscale.png)

**Design for scale**

Define outer margins as percentages rather than absolute values, so that margins can scale proportionally on round screens and avoid clipping any UI elements.  
![alt text](https://developer.android.com/static/wear/images/design/adaptivedesign-fontsizes.png)

**Font sizes**

The height of a UI element might change in a non-linear way, depending on font scaling and accessibility settings such as bold text.

<br />

The following screen sizes are particularly common choices for Wear OS devices. It's beneficial to use 225dp as a breakpoint between smaller screens and larger screens.

<br />

![alt text](https://developer.android.com/static/wear/images/design/adaptivedesign-192to224dp.png)

192dp to 224dp  
![alt text](https://developer.android.com/static/wear/images/design/adaptivedesign-225to240dp.png)

225dp to 240+dp

<br />

## Design quality tiers

We are also leaning into shape language in a much more expansive and meaningful way by utilizing flexible container shapes to apply rounding/sharpening of corner radius to support shape morphing lists and button states. We are also introducing edge-hugging buttons as a new component and iconic design pattern for round devices on Wear OS. Our quality guidelines are organized into three tiers. Enable the best possible experience for your users by meeting guidelines in all three tiers.

<br />

![alt text](https://developer.android.com/static/wear/images/design/adaptivedesign-allsizesready.png)

**Ready for all screen sizes**

Ensure your app is delivering a quality experience across all screen sizes. Create layouts that fully utilize the available app space.  
![alt text](https://developer.android.com/static/wear/images/design/adaptivedesign-responsive-optimized.png)

**Responsive and optimized**

Deliver more content to users on devices which allow for it, and utilize responsive layouts that automatically adapt to different screen sizes.  
![alt text](https://developer.android.com/static/wear/images/design/adaptivedesign-adaptivedifferentiated.png)

**Adaptive and differentiated**

Make the most of additional real estate by utilizing breakpoints to offer powerful new experiences on larger screens which are not possible on devices with smaller screens.

<br />

| **Caution:** A display size should*never*display less information than ones that are smaller than it, this is especially relevant for custom behaviors added in at the breakpoint. A common example of this is when components or text sizes are increased past the breakpoint and end up showing less are the larger screens. Screens should always show more value and never less value with increasing size.