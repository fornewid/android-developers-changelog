---
title: Best practices for designing apps  |  Wear  |  Android Developers
url: https://developer.android.com/design/ui/wear/guides/surfaces/apps/best-practices
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [UI Design](https://developer.android.com/design/ui)
* [Wear](https://developer.android.com/design/ui/wear)
* [Guides](https://developer.android.com/design/ui/wear/guides/get-started)

# Best practices for designing apps Stay organized with collections Save and categorize content based on your preferences.



## Optimize for vertical layouts

Simplify your app’s design by using vertical layouts, which allow users to scroll in a single direction to traverse content.

![](/static/wear/images/design/apps-bestpractices-DOvertical.png)

check\_circle

### Do this

This app’s goal is to take the user from point A to B.

![](/static/wear/images/design/apps-bestpractices-DONTmixhorzvert.png)

cancel

### Don't do this

Use both vertical and horizontal scrolling, as this can make your app experience confusing.

## Show the time

Display the time (overlay) at the top, as this provides a consistent place for the user to view the time.

![](/static/wear/images/design/apps-bestpractices-DOshowtime.png)

check\_circle

### Do this

Display the time at the top of the overlay, as this provides a consistent place for the user to view the time.

![](/static/wear/images/design/apps-bestpractices-DONTshowtime.png)

cancel

### Don't do this

Display the time on a temporary dialog, confirmation overlay or a picker, for example, a user is only likely to see a confirmation screen very briefly.

## Accessible inline entry points

Ensure all actions are displayed inline, using clear iconography and labels for accessibility. This includes entry points to settings and preferences.

![](/static/wear/images/design/apps-bestpractices-DOiconslabels.png)

check\_circle

### Do this

Use both icons and labels when possible.

![](/static/wear/images/design/apps-bestpractices-DONTiconsonly.png)

cancel

### Don't do this

Rely solely on icons to prompt the user to take action.

## Use labels to orient users

For longer dialogs, help orient the user with labels as they scroll through the content.

![](/static/wear/images/design/apps-bestpractices-DOcueorient.png)

check\_circle

### Do this

Use section breaks, labels, and other cues to organize content and help orient users as they scroll through longer views with mixed content.

![](/static/wear/images/design/apps-bestpractices-DONTlabeldialogs.png)

cancel

### Don't do this

Add a label for dialogs that contain a single content type.

## Elevate primary actions

Make it easy for users to take action in your app by pulling primary actions to the top of the overlay.

![](/static/wear/images/design/apps-bestpractices-elevateprimaryactions.png)

check\_circle

### Do this

Elevate non-ambiguous primary actions to the top.

![](/static/wear/images/design/apps-bestpractices-DONTprimarybelowfold.png)

cancel

### Don't do this

Put the primary action on a very long page at the bottom.

## Show the scrollbar on scrolling screens

Only use the scroll-indicator on scrolling screens to avoid the wrong interaction expectation. Similarly, remember to add the scroll-indicator on scrolling screens to indicate at what point of the screen you're viewing.

![](/static/wear/images/design/apps-bestpractices-DOshowscrollbar.png)

check\_circle

### Do this

Show the scroll-indicator if the entire view scrolls.

![](/static/wear/images/design/apps-bestpractices-DONTshowscrollbar.png)

cancel

### Don't do this

Show the scroll-indicator on non-scrolling views, or not show the scrollbar on scrolling views.

## Design responsively for larger screen sizes

Ensure the components you use fill the available width and consider the height on non-scrolling layouts.

All Compose components are build responsively, but any customization to elevate your design and add additional value on larger displays is encouraged.

![](/static/wear/images/design/apps-bestpractices-DOfillscreen-updated.png)

check\_circle

### Do this

Ensure content fills the available width and height and full screen elements (ProgressIndicators, TimeText, etc.) responsively adapt on non-scrolling layouts.

![](/static/wear/images/design/apps-bestpractices-DONTfixedwidth-updated.png)

cancel

### Don't do this

Use components with a fixed width that don’t fill the screen responsively or not adjust the behavior of content to fill the available space.

## Use responsive (percentage) margins

We recommend using percentage margins so the size of the margins adapts to the growing curve of the display.

![](/static/wear/images/design/apps-bestpractices-DOpercentmargins.png)

check\_circle

### Do this

Use additional percentage margins to ensure content doesn’t get clipped at the top and bottom.

![](/static/wear/images/design/apps-bestpractices-DONTfixedcomponents.png)

cancel

### Don't do this

Components shouldn’t just scale to fill the available space without additional margins.