---
title: Button  |  Cars  |  Android Developers
url: https://developer.android.com/design/ui/cars/guides/components/button
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [UI Design](https://developer.android.com/design/ui)
* [Cars](https://developer.android.com/design/ui/cars)
* [Guides](https://developer.android.com/design/ui/cars/guides/foundations/design-principles)

# Button Stay organized with collections Save and categorize content based on your preferences.




Buttons give users access to actions they may need to take in the car to provide
access to actions that drivers may need to take — for example, confirming a
choice or returning to the previous template.

Buttons can include the following:

* Icon only
* Label only
* Icon + label

![Examples](/static/images/design/ui/cars/components/button-1.png)


Examples of action buttons

### Template support

You can use buttons in the following places:

* [Pane template](/design/ui/cars/guides/templates/pane-template)
* [Message template](/design/ui/cars/guides/templates/message-template)
* [Long message template](/design/ui/cars/guides/templates/long-message-template)
* [Sign-in templates](/design/ui/cars/guides/templates/sign-in-template)
* In the [action strip](/design/ui/cars/guides/components/action-strip) on any template

### Guidance

Consider the following advice as you design buttons for your app.

* You can supply foreground and background colors to replace default colors.
  However, vehicle OEMs can choose whether or not to use the colors you supply
  in AAOS versions of your app.
* You can specify which button is the [primary button](/design/ui/cars/guides/components/button#primary).
* Keep labels short to avoid truncation – especially on the
  [Navigation template](/design/ui/cars/guides/templates/navigation-template), where space is limited.

![Examples](/static/images/design/ui/cars/components/button-3.png)


Example of a button design

### Primary buttons

In the [Message](/design/ui/cars/guides/templates/message-template), [Long Message](/design/ui/cars/guides/templates/long-message-template), and
[Pane](/design/ui/cars/guides/templates/pane-template) templates, which feature
up to 2 buttons, you can optionally tag one button as primary to represent the
primary action.

The primary button will be highlighted with the app accent color for visibility
and ease-of-use.

**Note:** On AAOS, vehicle OEMs can apply their own color to the primary button and
determine its horizontal order for the other button.

### Timed buttons

You can create buttons associated with default actions that are taken
automatically if the user doesn't act within a specified amount of time
(customizable by the app). For a sample flow using this strategy, see
[Respond to a timed alert](/design/ui/cars/guides/app-types/timed-alert).

To convey the countdown to the user, the button becomes a timer with a built-in
progress indicator. The timer countdown is indicated by shading that moves
horizontally across the button.

The Car App Library determines the timer color based on the button's background
color, adjusting it as needed to ensure sufficient contrast.

To create a timed button, assign a [default flag](/reference/androidx/car/app/model/Action#FLAG_DEFAULT()) to it.

![Examples](/static/images/design/ui/cars/components/button-2.png)

In these examples, the **Navigate** or **Accept** action will automatically be
taken if the user doesn't choose the other action before the shaded progress
indicator moves all the way across the button.