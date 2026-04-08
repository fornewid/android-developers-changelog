---
title: https://developer.android.com/design/ui/mobile/guides/layout-and-content/edge-to-edge
url: https://developer.android.com/design/ui/mobile/guides/layout-and-content/edge-to-edge
source: md.txt
---

![](https://developer.android.com/static/images/design/ui/mobile/e2e-hero.png)

An edge-to-edge app takes advantage of the entire screen by drawing UI under the
system bars.
![](https://developer.android.com/static/images/design/ui/mobile/e2e-app-contrast.gif) **Figure 1.** Left. An app that isn't edge-to-edge. Right. An app that is edge-to-edge.

## Takeaways

- Draw background and scrolling content underneath system bars for an edge-to-edge experience.
- Avoid adding tap gestures or drag targets under system insets; these conflict with edge-to-edge and gesture navigation.

![](https://developer.android.com/static/images/design/ui/mobile/e2e-gesture-insets.png) **Figure 2.** An app with gesture insets highlighted green.

### Draw your content behind the system bars

The edge-to-edge feature lets you draw the UI under the system bars for an
immersive experience.

An app can address overlaps in content by reacting to *insets* . Insets describe
how much the content of your app needs to be padded to avoid overlapping with
system bars or with physical device features such as [display cutouts](https://developer.android.com/develop/ui/views/layout/display-cutout). Read
about how to support edge-to-edge and handle insets in [Compose](https://developer.android.com/develop/ui/compose/layouts/insets) and
[Views](https://developer.android.com/develop/ui/views/layout/edge-to-edge).

Be aware of the following types of insets when designing edge-to-edge use cases:

- *System bar insets* apply to UI that is both tappable and shouldn't be visually obscured by the system bars.
- *System gesture insets* apply to gesture-navigational areas used by the OS that take priority over your app.
- *Display cutout insets* apply to device areas that extend into the display surface, such as the camera cutout.

### Status bar considerations

See the [Android System Bars](https://developer.android.com/design/ui/mobile/guides/foundations/system-bars) for fundamental system bar design guidance. The
following section discusses additional status bar considerations.

#### Scrolling content

Top app bars should collapse while scrolling. Learn how to [collapse](https://developer.android.com/develop/ui/compose/components/app-bars#scroll) the
Material 3 TopAppBar.  
![](https://developer.android.com/static/images/design/ui/mobile/e2e-collapse-bar.gif)  
check_circle

### Do

Collapse the top app bar to status bar height if the app bar is sticky.  
![](https://developer.android.com/static/images/design/ui/mobile/e2e-bg-color.gif)  
check_circle

### Do

Add a matching background color gradient if the top app bar is not sticky.

Status bars should be translucent when the UI scrolls underneath, so that the
status bar icons don't look cluttered. To accomplish this, first make a
scrollable UI edge-to-edge by implementing the steps in the [LazyColumn](https://developer.android.com/develop/ui/compose/layouts/insets#scaffold) or
[RecyclerView](https://developer.android.com/develop/ui/views/layout/recyclerview#enable-edge-to-edge-display) documentation. Then, ensure the system bar is translucent by
doing one of the following:

- Rely on the Material 3 TopAppBar automatic protection when [scrolling](https://developer.android.com/develop/ui/compose/components/app-bars#scroll), if applicable.
- Create a custom gradient composable or use [GradientProtection](https://developer.android.com/reference/androidx/core/view/insetscontrast/GradientProtection) for Views. For more information on doing this in compose, see [System bar protection](https://developer.android.com/develop/ui/compose/layouts/system-bars).

![](https://developer.android.com/static/images/design/ui/mobile/e2e-protection.png) **Figure 3.** An app with gesture insets highlighted green.

For adaptive layouts, ensure there are separate protections for panes with
different background colors.  
![](https://developer.android.com/static/images/design/ui/mobile/e2e-gradient-protection-dont.png)  
cancel

### Don´t

Have gradient protection that mismatches each pane's background  
![](https://developer.android.com/static/images/design/ui/mobile/e2e-gradient-protection-do.png)  
check_circle

### Do

Have gradient protection that matches each pane's background.

Likewise, navigation drawers should also have a separate protection from the
rest of the app.
![](https://developer.android.com/static/images/design/ui/mobile/e2e-translucent-status-bar.png) **Figure 4.** A translucent status bar for the navigation drawer. This image shows status bar protection for the navigation drawer but not the app.

Don't stack status bar protections, for example by using both the Material 3
TopAppBar built-in protection and a custom protection.

### Navigation bar considerations

See the [Android System Bars](https://developer.android.com/design/ui/mobile/guides/foundations/system-bars) for fundamental navigation bar design guidance.
The following section includes additional navigation bar considerations.

#### Scrolling content

Bottom app bars should collapse while scrolling.  
![](https://developer.android.com/static/images/design/ui/mobile/e2e-scrim-do.gif)  
check_circle

### Do

Add system bar scrim for three-button navigation when the bottom app bar animates away.  
![](https://developer.android.com/static/images/design/ui/mobile/e2e-transparent-do.gif)  
check_circle

### Do

Keep gesture navigation transparent and don't add an additional scrim.

### Display cutouts

Display cutouts can affect the appearance of your UI. Apps must handle display
cutout insets so that important parts of the UI don't draw underneath the
display cutout.  
![](https://developer.android.com/static/images/design/ui/mobile/e2e-inset-do.png)  
check_circle

### Do

Inset critical UI using display cutout insets.  
![](https://developer.android.com/static/images/design/ui/mobile/e2e-inset-dont.png)  
cancel

### Don´t

Place critical UI at the very edge of the screen.

However, solid app bar backgrounds should draw into the display cutout as shown
in the following image.
![](https://developer.android.com/static/images/design/ui/mobile/e2e-solid-bar.gif) **Figure 5.** Solid app bar backgrounds draw into the display cutout while important UI is inset.

Ensure horizontal carousels draw into the display cutout.
![](https://developer.android.com/static/images/design/ui/mobile/e2e-horizontal-display.png) **Figure 6.** An edge-to-edge horizontal display, where the carousel scrolls through the display cutout.

Read about how to support display cutouts in [Compose](https://developer.android.com/develop/ui/compose/system/cutouts) and [Views](https://developer.android.com/develop/ui/views/layout/display-cutout).

### Other guidance

In general, backgrounds and divider lines should also draw edge-to-edge while
content like text and buttons should be inset to avoid the system UI and
hardware elements.