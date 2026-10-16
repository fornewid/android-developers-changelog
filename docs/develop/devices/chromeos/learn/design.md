---
title: https://developer.android.com/develop/devices/chromeos/learn/design
url: https://developer.android.com/develop/devices/chromeos/learn/design
source: md.txt
---

Android helps you develop an app that runs well on a wide range of device screen sizes and form factors. This broad compatibility helps you design a single app that you can distribute widely to all of your targeted devices.


However, to give your users the best possible experience on each screen configuration, you need to optimize your layouts and other UI components for different sizes. On ChromeOS, optimizing your UI lets you take full advantage of the additional screen space to offer new features, present new content, or enhance the experience to deepen user engagement.

## Layouts for larger screens


If you developed your app for handsets and want to improve your design on ChromeOS and other large-screen form factors, start by making minor adjustments to your layouts, fonts, and spacing. For 7-inch tablets or a game with a large canvas, these adjustments may be all you need.


For larger displays, you can redesign parts of your UI to replace a "stretched-out" UI with an efficient multi-pane UI, simpler navigation, and additional content. The Material Design team's [Material Studies](https://material.io/design/material-studies/) provide examples of what this can look like. For instance, see how [Reply](https://material.io/design/material-studies/reply.html) adapts to different screen sizes.


![Reply app on different screen sizes](https://developer.android.com/images/develop/chromeos/design-1.avif)


Here are some suggestions:

- Provide custom layouts for these larger screens. You can do this by using the screen's [shortest dimension](https://developer.android.com/guide/practices/screens_support#sizes) or the minimum available width and height.
- Imagine how your UX and layouts work in a landscape-first environment such as ChromeOS. Adapt your layouts to look and perform well in these orientations based on window size, or provide specific landscape layouts by using the land resource qualifier. You can learn more about dynamic window resizing and other considerations for large screens on [the Window management page](https://developer.android.com/develop/devices/chromeos/learn/window-management).
- Bottom navigation bars don't scale well when your app is stretched to be wide. Consider moving your navigation to a left-side menu where it's more accessible and can show more options. The Reply example illustrates this well.
- At a minimum, customize dimensions such as font sizes, margins, and spacing for larger screens to improve the use of space and content legibility. Consider how things may look when users are a bit further from the device, such as a ChromeOS device or other desktop environments.
- Adjust the positioning of UI controls so that they are accessible to users when using a mouse or holding a tablet, such as toward the sides and away from the center.
- Padding of UI elements should normally be larger on ChromeOS and other large-screen devices than on handsets. [Your margins and gutters](https://material.io/design/layout/responsive-layout-grid.html#columns-gutters-margins) should all adapt as you get to different screen sizes.
- Adequately pad text content so that it's not aligned directly along screen edges. Use a minimum 16dp padding around content near screen edges.


In particular, make sure that your layouts don't appear "stretched" across the screen:

- Lines of text shouldn't be excessively long---optimize for a maximum of 100 characters per line, with best results between 50 and 75.
- Lists and menus shouldn't use the full screen width.
- Use padding to manage the widths of onscreen elements or switch to a multi-pane UI for larger screen devices (see next section).

## Take advantage of extra screen area


ChromeOS devices provide significantly more screen real estate to your app. When designing your app's UI for larger screens, take full advantage of the extra area.


In the [Reply](https://material.io/design/material-studies/reply.html) and [Rally](https://material.io/design/material-studies/rally.html) examples, the apps take different approaches to using the increased screen size. Reply adds space for a cleaner look, while Rally displays more data to reduce scrolling and taps.


![Rally app on different screen sizes](https://developer.android.com/images/develop/chromeos/design-2.avif)


A good place to start is by looking at things that may be hidden from the user and how you can make them visible. This could be showing more information about an item, making menus visible that may be hidden behind a right-click or long-press, or showing different or deeper navigation options now that you have a larger left-side navigation area. These are big usability wins that can improve your UX and give a more desktop-like feel to your app, without a complete re-design of the current experience.


Here are some recommendations for your app:

- Your brand dictates the direction you should go when thinking about these different screen sizes. Deciding what to prioritize and show the user depends on the type of user journeys that exist and the most commonly used features. For inspiration, check out the [Material Studies](https://material.io/design/material-studies) and look at how each product responds differently to a larger screen.
- Think about how your app's design should behave using a [responsive grid system](https://material.io/design/layout/responsive-layout-grid.html#), and how content, navigation, and options should move as you get larger screen real-estate.
- Decide on which screen sizes you'll use a different layout, then provide the different layouts in the appropriate window size buckets (such as large/xlarge) or minimum window widths (such as sw600dp/sw720). Remember that as you get to these layouts, the overall context that the user was in shouldn't change, and you should try and retain all user state while transitioning between layouts (scroll position, text being written, etc.)

## Use assets designed for higher density \& larger screens


To make your app look its best, provide icons and other bitmap assets for each density in the range commonly supported by ChromeOS. Specifically, you should design your icons for the app bar, notifications, and launcher according to the [iconography guidelines](https://material.io/design/iconography/#design-principles) and provide them in vector formats so that they can scale gracefully with the different screens you will find your app on.


For more information on VectorDrawables and vector assets on Android, check out this [blog post](https://medium.com/androiddevelopers/understanding-androids-vector-image-format-vectordrawable-ab09e41d5c68) by [Nick Butcher](https://twitter.com/crafty).

## Adjust font sizes and touch targets


To make your app usable on ChromeOS and higher density screens, adjust the font sizes and touch targets in your UI for all of the screen configurations you're targeting. You can adjust font sizes through [styleable attributes](https://developer.android.com/guide/topics/ui/themes) or [dimension resources](https://developer.android.com/guide/topics/resources/more-resources#Dimension), and you can adjust touch targets through layouts and bitmap drawables, as previously discussed.


Here are some considerations:

- Text shouldn't be excessively large or small on larger screen sizes and densities. Make sure that labels are sized appropriately for the UI elements they correspond to and ensure that there are no improper line breaks in labels, titles, and other elements.
- The recommended touch-target size for onscreen elements is 48dp---some adjustments may be needed in your larger screen UI. Read more about [Spacing Methods](https://material.io/design/layout/spacing-methods.html#) to learn about touch targets and spacing between items as screen sizes change. These recommendations also meet minimum [accessibility guidelines](https://developer.android.com/guide/topics/ui/accessibility/apps).
- When possible, for smaller icons, expand the touchable area to more than 48dp using [`TouchDelegate`](https://developer.android.com/reference/android/view/TouchDelegate) or just centering the icon within the transparent button.