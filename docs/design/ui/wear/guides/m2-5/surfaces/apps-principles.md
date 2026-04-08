---
title: https://developer.android.com/design/ui/wear/guides/m2-5/surfaces/apps-principles
url: https://developer.android.com/design/ui/wear/guides/m2-5/surfaces/apps-principles
source: md.txt
---

# App design principles

An app is one of the primary surfaces on Wear OS. Apps are different from complications or tiles, which are glanceable representations of app content. Apps display more information and support richer interactivity. The user often enters an app from another surface, such as a notification, complication, Tile, or voice action.

## Principles

Keep the following principles in mind when designing apps:

- **Focused:**Focus on critical tasks to help people get things done within seconds.

- **Shallow and linear:**Avoid creating hierarchies deeper than two levels. Aim to display content and navigation inline when possible.

- **Scrolling:**Apps can scroll. This is a natural gesture for users to see more content on the watch.

## Guidelines

Follow these guidelines when designing apps.

### Optimize for vertical layouts

Simplify your app's design by using vertical layouts, which allow users to scroll in a single direction to move through content.  
![](https://developer.android.com/static/wear/images/surfaces/apps_4.png)  
check_circle

### Do

This app's goal is to take the user from point A to point B.  
![](https://developer.android.com/static/wear/images/surfaces/apps_5.png)  
cancel

### Don't

Don't use both vertical and horizontal scrolling, as this can make your app experience confusing. The exception is some specific use cases, including media playback, which can support both vertical and horizontal scrolling.

### Show the time

Users tend to spend more time in apps, so it's important to provide quick access to the time.  
![](https://developer.android.com/static/wear/images/surfaces/apps_6.png)  
check_circle

### Do

Display the time at the top of the app, as this provides a consistent place for the user to view the time.  
![](https://developer.android.com/static/wear/images/surfaces/apps_13.png)  
cancel

### Don't

Display the time in a dialog, confirmation screen, or picker, as users are likely to spend only a few seconds on those screens.

For more information about design and usage, see[Time text](https://developer.android.com/training/wearables/compose/time-text).

### Accessible inline entry points

Ensure all actions are displayed inline, using clear iconography and labels for accessibility. This includes entry points to settings and preferences.  
![](https://developer.android.com/static/wear/images/surfaces/apps_3.png)  
check_circle

### Do

Use both icons and labels when possible.  
![](https://developer.android.com/static/wear/images/surfaces/apps_14.png)  
cancel

### Don't

Rely solely on icons to prompt the user to take action.

### Elevate primary actions

Help users take action in your app by pulling primary actions to the top of the app. Elevate non-ambiguous primary actions to the top of the app.

![](https://developer.android.com/static/wear/images/surfaces/apps_1.png)

### Use labels to orient users

For longer apps, help orient the user with labels as they scroll through the content.  
![](https://developer.android.com/static/wear/images/surfaces/apps_10.png)  
check_circle

### Do

Use section breaks, labels, and other cues to organize content and help orient users as they scroll through longer views with mixed content.  
![](https://developer.android.com/static/wear/images/surfaces/apps_12.png)  
cancel

### Don't

Add a label for apps that contain a single content type.

### Show the scrollbar

Show the scrollbar if the entire view scrolls, as shown in the following image. For more information, see[Position indicator](https://developer.android.com/training/wearables/compose/position-indicators).

![](https://developer.android.com/wear/images/surfaces/apps_1.png%22)

## Content containers

See the following examples of content containers.

<br />

![Example of Button row layout](https://developer.android.com/static/wear/images/surfaces/apps_2.png)

**Figure 1.**Container of fixed height.  
![Example of Button column layout](https://developer.android.com/static/wear/images/surfaces/apps_11.png)

**Figure 2.**Container of variable height.

<br />

<br />

![Example of Button row layout](https://developer.android.com/static/wear/images/surfaces/apps_9.png)

**Figure 3.**Container of height and width greater than the viewport.  
![Example of Button column layout](https://developer.android.com/static/wear/images/surfaces/apps_8.png)

**Figure 4.**A paginated container.

<br />

<br />

![Example of Button row layout](https://developer.android.com/static/wear/images/surfaces/apps_7.png)

**Figure 5a.**Content pages that take the full dimension of the screen and are paginated vertically.  

<br />

| **Note:** Users find vertical layouts much easier to navigate than paginated UI's. Paginated UI's are best for situations when the user needs to navigate content using gross gestures, such as when working out or on the go. Because of this, they are generally used in workout and media app UIs.