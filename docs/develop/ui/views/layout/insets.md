---
title: https://developer.android.com/develop/ui/views/layout/insets
url: https://developer.android.com/develop/ui/views/layout/insets
source: md.txt
---

Try the Compose way Jetpack Compose is the recommended UI toolkit for Android. Learn how to work with WindowInsets in Compose. [WindowInsets in Compose →](https://developer.android.com/develop/ui/compose/system/insets) ![](https://developer.android.com/static/images/android-compose-ui-logo.png)

<br />

![](https://developer.android.com/static/develop/ui/compose/images/layouts/insets/e2e-intro.gif) **Figure 1.** The status bar and navigation bar, collectively called the *system bars*.

Layout all apps so that your content stretches from the top edge to the bottom
edge of the screen. This is the default behavior beginning in Android 15
(API level 35). This means that the top and bottom areas of your app are laid
out behind the status bar and the navigation bar. Together, the status bar and
the navigation bar are called the *system bars*. The system bars are areas that
are generally dedicated to the display of notifications, communication of device
status, and device navigation.

The overlaps between your app and the areas where the system UI is displayed is
one example of *window insets*, which represent the parts of your screen where
your app can intersect with the system UI. Intersecting with these parts of the
UI can mean displaying above the content, but it can also inform your app about
system gestures.

The following types of window insets are available.

- By default, opt-in to expand your app window to extend across the entire
  screen and draw app content [edge-to-edge](https://developer.android.com/training/gestures/edge-to-edge)
  behind the system bars. Use offsets to avoid displaying important content
  and touch targets behind system bars.

- Apps that display content such as movies or images can temporarily [hide the
  system bars](https://developer.android.com/training/system-ui/immersive) for a more immersive experience.
  Carefully consider your users' needs and expectations before modifying the
  system bars, since they give users a standard way of navigating a device and
  viewing its status.

- A *display cutout* is an area on some devices that extends into the display
  surface to provide space for sensors on the front of the device. Apps can
  support [display cutouts](https://developer.android.com/guide/topics/display-cutout) by querying their
  positions so that no important content overlaps the cutout area.

- A keyboard transition is a common example where window insets are
  dynamically updated. Apps can observe the current keyboard state,
  programmatically toggle the states, support animations for window insets,
  and make app content animate seamlessly between keyboard transitions.