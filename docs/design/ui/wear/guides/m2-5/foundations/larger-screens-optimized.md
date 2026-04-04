---
title: Responsive and optimized  |  Wear  |  Android Developers
url: https://developer.android.com/design/ui/wear/guides/m2-5/foundations/larger-screens-optimized
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [UI Design](https://developer.android.com/design/ui)
* [Wear](https://developer.android.com/design/ui/wear)
* [Guides](https://developer.android.com/design/ui/wear/guides/get-started)

# Responsive and optimized Stay organized with collections Save and categorize content based on your preferences.




![](/static/wear/images/design/larger-screens-optimized-heading.png)

Apps that are **responsive and optimized** utilize responsive layouts that
automatically adapt to different screen sizes, offering some additional value to
users and providing a productive, engaging user experience.

## Add value through responsive design

Responsive layouts dynamically format and position elements such as buttons,
text fields, and dialogs for an optimal user experience. Automatically offer
users of your app additional value on larger screens by utilizing responsive
design practices. Whether it's more text visible at a glance, more actions on
screen, or larger, more accessible tap targets, responsive practices provide an
enhanced experience for users of larger screens.

![](/static/wear/images/design/larger-screens-optimized-sizes-1.png)
![](/static/wear/images/design/larger-screens-optimized-sizes-2.png)

## Build responsive apps and tiles for Wear OS

Responsive UIs stretch and change to make the best possible use of all available
screen space, no matter what size screen they're rendered on. When designing
responsive layouts on a round screen, scrolling and non-scrolling views each
have unique requirements to maintain UI element scaling, as well as preserve a
balanced layout and composition. For [scrolling views](/design/ui/wear/guides/foundations/canonical-adaptive-layouts#scrolling), use percentages to
define all top, bottom, and side margins to avoid clipping and provide
proportional scaling of elements. For [non-scrolling views](/design/ui/wear/guides/foundations/canonical-adaptive-layouts#non-scrolling), use percentages
and vertical constraints for all margins. That way, the main content in the
middle can stretch to fill the available area.

See the [Compose](/training/wearables/compose/screen-size#responsive-layouts) and [Tiles](/training/wearables/tiles/screen-size#responsive-layouts) implementation guidance for responsive
layouts.

![](/static/wear/images/design/larger-screens-optimized-do.png)

check\_circle

### Do

* Use standard components which are designed for
  adaptation.
* Utilize adaptive layouts which adapt smoothly across
  screen sizes.

![](/static/wear/images/design/larger-screens-optimized-dont.png)

cancel

### Don't

* Stretch UI elements (text fields, buttons, dialogs)
  to fill extra space.
* Increase the sizes of fonts (unless they're
  serving a primarily graphic purpose).

## Next step: adaptive and differentiated

![](/static/wear/images/design/larger-screens-differentiated-header.png)

Apps that are **adaptive and differentiated** create a user experience that
isn't possible on devices with smaller screens.

[Get started](/design/ui/wear/guides/foundations/larger-screens-differentiated)