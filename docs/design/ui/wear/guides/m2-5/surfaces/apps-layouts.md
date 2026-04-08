---
title: https://developer.android.com/design/ui/wear/guides/m2-5/surfaces/apps-layouts
url: https://developer.android.com/design/ui/wear/guides/m2-5/surfaces/apps-layouts
source: md.txt
---

# App layouts

![](https://developer.android.com/static/wear/images/surfaces/app-layouts-hero.png)

When designing apps for Wear OS, be intentional about the layouts you choose for each experience. Because Wear OS runs on circular displays and clipping is more common than on handheld devices, there are two categories of canonical layouts that you should consider when designing your app.

## Non-scrolling app layouts

Non-scrolling layouts focus on glanceable information and offer users value with little or no interaction. Because of that, it can be challenging to build responsive behavior into these layouts:

![Examples include dialogs, confirmation overlays, pickers, steppers, and combinations](https://developer.android.com/static/wear/images/surfaces/app-layouts-non-scrolling.png)

### Build for responsive non-scrolling views

- Test on a combination of languages, font scaling, devices, and variable content.
- Use non-scrollable layouts only when the content is known or controlled ahead of time, or if you must use a specific design.
- Apply the[recommended top, bottom, and side margins](https://developer.android.com/design/ui/wear/guides/components/dialogs#adaptive-layouts)to the layout.
- Define margins in percentage values in places where content might otherwise be clipped.
- Arrange elements to make the best possible use of the space within the screen and maintain balance across different device sizes.

## Scrolling app layouts

For pages that contain more information than can fit on a single screen, or which are required to support longer and more immersive journeys, use a scroll view.

![Examples include chip lists, mixed lists, card lists, button lists, and dialogs with bottom chips and bottom buttons](https://developer.android.com/static/wear/images/surfaces/app-layouts-scrolling.png)

### Build for responsive scroll views

- Apply the[recommended top, bottom, and side margins](https://developer.android.com/design/ui/wear/guides/components/dialogs#adaptive-layouts).
- Define outer margins in percentage values to prevent clipping at the beginning and end of the scrollable container.
- Apply margins in fixed DP values between UI elements.

### How to build for adaptive scroll views using a screen size breakpoint

Scroll views that use responsive design practices usually adapt to a range of screen sizes. However, in some special cases, you can use a breakpoint to override dimensions and augment layouts which show additional options, improve glanceability, or make content fit better on screen. The following example shows how, on larger screens, the bottom two buttons are widened:

![Buttons are wider, and more text fits on list items, in the layout for larger screen sizes](https://developer.android.com/static/wear/images/surfaces/app-layouts-scrolling-breakpoint.png)

## Figma design kits

[Visit the design kit downloads page](https://developer.android.com/design/ui/wear/guides/foundations/download)to explore design layouts with built-in components, options, and recommendations to create different app and tile designs that follow best practices.