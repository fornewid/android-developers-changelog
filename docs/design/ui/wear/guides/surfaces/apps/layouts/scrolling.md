---
title: Scrolling app layouts  |  Wear  |  Android Developers
url: https://developer.android.com/design/ui/wear/guides/surfaces/apps/layouts/scrolling
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [UI Design](https://developer.android.com/design/ui)
* [Wear](https://developer.android.com/design/ui/wear)
* [Guides](https://developer.android.com/design/ui/wear/guides/get-started)

# Scrolling app layouts Stay organized with collections Save and categorize content based on your preferences.



For pages that contain more information that extends beyond the height of the
screen, or require longer and more immersive journeys, use a scroll view.

## Preset scrolling layout components

### Dialog with bottom button stack

![](/static/wear/images/design/app-layout-scrolling-battery-saver.png)

### Dialog with bottom button stack

![](/static/wear/images/design/app-layout-scrolling-incoming-call.png)

### Dialog with bottom double buttons

![](/static/wear/images/design/app-layout-scrolling-change-location.png)

## Custom scrolling layout examples

Scrolling app screens are not limited to the set components, but can combine
elements to create the layout you want. Be mindful of the length of a scrolling
screen, and the use of responsive (percentage) margins and padding, to verify
that components adapt to the available screen size.

### Additional content on larger screens

![](/static/wear/images/design/app-layout-scrolling-earthquake.png)

### Button list: Icon buttons with icon size 26dp

![](/static/wear/images/design/app-layout-scrolling-icon-buttons.png)

### Button list: App buttons with icon size 32dp

![](/static/wear/images/design/app-layout-scrolling-app-list.png)

### Button list: App buttons with icon size 36dp

![](/static/wear/images/design/app-layout-scrolling-contacts.png)

### Button list with toggle buttons

![](/static/wear/images/design/app-layout-scrolling-toggle-buttons.png)

### Mixed list with single-line elements

![](/static/wear/images/design/app-layout-scrolling-mixed-list.png)

### Mixed list with multi-line elements

![](/static/wear/images/design/app-layout-scrolling-settings.png)

### Card list with app cards

![](/static/wear/images/design/app-layout-scrolling-app-cards.png)

### Card list with title cards

![](/static/wear/images/design/app-layout-scrolling-title-cards.png)

### Card list with custom cards

![](/static/wear/images/design/app-layout-scrolling-custom-cards.png)

### Text list

![](/static/wear/images/design/app-layout-scrolling-text-list.png)

## Responsive and adaptive behavior

All components in the Compose library automatically adapt to the wider screen
size, and gain width and height. Scroll views that use responsive design
practices usually adapt to a range of screen sizes. However, in some special
cases, you can use a breakpoint to override dimensions and augment layouts which
expand functionality, improve glanceability, or make content fit better on
screen.

To verify that responsive parameters are properly defined, use the following
checklist:

* Apply the recommended top, bottom, and side margins.
* Define outer margins in percentage values to prevent clipping at the
  beginning and end of the scrollable container.
* Apply margins in fixed DP values between UI elements.
* Consider applying a breakpoint at 225dp to introduce additional content or
  make existing content more glanceable when on bigger screen sizes.

![](/static/wear/images/design/app-layout-scrolling-bottom-hero.png)