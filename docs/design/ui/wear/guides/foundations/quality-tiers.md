---
title: https://developer.android.com/design/ui/wear/guides/foundations/quality-tiers
url: https://developer.android.com/design/ui/wear/guides/foundations/quality-tiers
source: md.txt
---

# Design quality tiers

Material 3 Expressive leans into shape language in a much more expansive and meaningful way by utilizing flexible container shapes to apply rounding and sharpening of corner radii to support shape morphing lists and button states. The design system also introduces edge-hugging buttons as an ownable and iconic design pattern for round devices on Wear OS.

![](https://developer.android.com/static/wear/images/design/quality-tiers-hero.png)

## Maintain UI element scaling

When designing layouts on a round screen, scrolling and non-scrolling views each have unique requirements to maintain UI element scaling and preserve a balanced layout and composition.

<br />

**Scrolling views**

For scrolling views, use percentages to define all top, bottom, and side margins to avoid clipping and provide proportional scaling of elements.

All top, bottom, and side margins should be defined in percentages to avoid clipping and provide proportional scaling of elements.  
**Non-scrolling views**

For non-scrolling views, use percentages and vertical constraints for all margins. That way, the main content in the middle can stretch to fill the available area.

All margins should be defined in percentages and vertical constraints should be defined such that the main content in the middle can stretch to fill the available area.

<br />

## Tiers of quality guidelines

Our quality guidelines are organized into three tiers. Enable the best possible experience for your users by meeting guidelines in all three tiers.

<br />

![](https://developer.android.com/static/wear/images/design/quality-tier-1-hero.png)

**Ready for all screen sizes**

Ensure your app is delivering a quality experience across all screen sizes. Create layouts that fully use the available app space.  
![](https://developer.android.com/static/wear/images/design/quality-tier-2-hero.png)

**Responsive and optimized**

Deliver more content to users on devices which allow for it, and utilize responsive layouts that automatically adapt to different screen sizes.  
![](https://developer.android.com/static/wear/images/design/quality-tier-3-hero.png)

**Adaptive and differentiated**

Make the most of additional real estate by utilizing breakpoints to offer powerful new experiences on larger screens which are not possible on devices with smaller screens.

<br />

| **Caution:** A larger display size should*never*display less information than ones that are smaller than it, this is especially relevant for custom behaviors added in at the breakpoint. A common example of this is when components or text sizes are increased past the breakpoint and end up showing less are the larger screens. Screens should always show "more value" and never "less value" with increasing size.