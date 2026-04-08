---
title: App rendering differences on Chromebooks  |  ChromeOS  |  Android Developers
url: https://developer.android.com/develop/devices/chromeos/learn/differences
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [ChromeOS](https://developer.android.com/chrome-os/intro)

# App rendering differences on Chromebooks Stay organized with collections Save and categorize content based on your preferences.



Because Android apps run in a window under ChromeOS, there are small
differences in how apps are rendered on Chromebooks. These differences are
outlined in the following paragraphs.

## Tasks, windows, and transparency

A [task](/guide/components/tasks-and-back-stack)
consists of a stack of activities that the user interacts with when running an
app. Tasks are presented on ChromeOS as a window with a title bar, with the
apps layered on top of each other. Each activity can then be
partially translucent, letting the lower layers show through.

In a conventional Android app, the previous task or the desktop shows through beneath the task.
In this way, there is always something visible beneath a translucent task.

This does not work in a window environment, for the following reasons:

* The visible content below a window cannot be controlled, and could therefore
  be anything.
* Fully transparent pixels could "magically" swallow touch or mouse
  events.
* Window elements might visually be disconnected from the caption, confusing
  the user with possibly unconnected visual elements.

To mitigate this problem, Play for ChromeOS draws a semitransparent rectangle behind
each window. For this reason, apps can never be 100 percent transparent
when running under ChromeOS, even when using the `Theme.Translucent.NoTitleBar`
theme.