---
title: https://developer.android.com/training/system-ui
url: https://developer.android.com/training/system-ui
source: md.txt
---

# Control the system UI visibility

![system bars](https://developer.android.com/static/images/training/system-ui.png)

**Figure 1.**System bars, including the \[1\] status bar, and \[2\] navigation bar.

The[system bars](https://material.io/design/platform-guidance/android-bars.html)are screen areas dedicated to the display of notifications, communication of device status, and device navigation. Typically the system bars (which consist of the status and navigation bars, as shown in figure 1) are displayed concurrently with your app. Apps that display immersive content, such as movies or images, can temporarily dim the system bar icons for a less distracting experience, or temporarily hide the bars for a fully immersive experience.

If you're familiar with the[Android Design Guide](https://developer.android.com/design), you know the importance of designing your apps to conform to standard Android UI guidelines and usage patterns. You should carefully consider your users' needs and expectations before modifying the system bars, since they give users a standard way of navigating a device and viewing its status.  

This class describes how to dim or hide system bars across different versions of Android to create an immersive user experience, while still preserving easy access to the system bars.

## Lessons

**[Dimming the System Bars](https://developer.android.com/training/system-ui/dim)**
:   Learn how to dim the status and navigation bars. (Deprecated)

**[Hiding the Status Bar](https://developer.android.com/training/system-ui/status)**
:   Learn how to hide the status bar on different versions of Android.

**[Hiding the Navigation Bar](https://developer.android.com/training/system-ui/navigation)**
:   Learn how to hide the navigation bar, in addition to the status bar.

**[Using Immersive Full-Screen Mode](https://developer.android.com/training/system-ui/immersive)**
:   Learn how to create a fully immersive experience in your app.

**[Responding to UI Visibility Changes](https://developer.android.com/training/system-ui/visibility)**
:   Learn how to register a listener to get notified of system UI visibility changes so that you can adjust your app's UI accordingly.