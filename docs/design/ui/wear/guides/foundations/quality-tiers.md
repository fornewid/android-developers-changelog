---
title: Design quality tiers  |  Wear  |  Android Developers
url: https://developer.android.com/design/ui/wear/guides/foundations/quality-tiers
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [UI Design](https://developer.android.com/design/ui)
* [Wear](https://developer.android.com/design/ui/wear)
* [Guides](https://developer.android.com/design/ui/wear/guides/get-started)

# Design quality tiers Stay organized with collections Save and categorize content based on your preferences.



Material 3 Expressive leans into shape language in a much more expansive and
meaningful way by utilizing flexible container shapes to apply rounding and
sharpening of corner radii to support shape morphing lists and button states.
The design system also introduces edge-hugging buttons as an ownable and iconic
design pattern for round devices on Wear OS.

![](/static/wear/images/design/quality-tiers-hero.png)

## Maintain UI element scaling

When designing layouts on a round screen, scrolling and non-scrolling
views each have unique requirements to maintain UI element scaling and preserve
a balanced layout and composition.

**Scrolling views**

For scrolling views, use percentages to define all top, bottom, and side
margins to avoid clipping and provide proportional scaling of elements.

All top, bottom, and side margins should be defined in percentages to avoid
clipping and provide proportional scaling of elements.

[
](/static/wear/images/design/quality-scrolling.mp4)

**Non-scrolling views**

For non-scrolling views, use percentages and vertical constraints for all
margins. That way, the main content in the middle can stretch to fill the
available area.

All margins should be defined in percentages and vertical constraints should be
defined such that the main content in the middle can stretch to fill the
available area.

[
](/static/wear/images/design/quality-non-scrolling.mp4)

## Tiers of quality guidelines

Our quality guidelines are organized into three tiers. Enable the best possible
experience for your users by meeting guidelines in all three tiers.

![](/static/wear/images/design/quality-tier-1-hero.png)

**Ready for all screen sizes**

Ensure your app is delivering a quality experience across all screen sizes.
Create layouts that fully use the available app space.

![](/static/wear/images/design/quality-tier-2-hero.png)

**Responsive and optimized**

Deliver more content to users on devices which allow for it, and utilize
responsive layouts that automatically adapt to different screen sizes.

![](/static/wear/images/design/quality-tier-3-hero.png)

**Adaptive and differentiated**

Make the most of additional real estate by utilizing breakpoints to offer
powerful new experiences on larger screens which are not possible on devices
with smaller screens.

**Caution:** A larger display size should *never* display less information than ones
that are smaller than it, this is especially relevant for custom behaviors added
in at the breakpoint. A common example of this is when components or text sizes
are increased past the breakpoint and end up showing less are the larger
screens. Screens should always show "more value" and never "less value" with
increasing size.