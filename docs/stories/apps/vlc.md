---
title: https://developer.android.com/stories/apps/vlc
url: https://developer.android.com/stories/apps/vlc
source: md.txt
---

# VLC optimizes its Android app for immersive video experiences on larger screens

![](https://developer.android.com/static/images/distribute/stories/vlc-icon.svg)

[VLC](https://www.videolan.org/vlc/index.html)is a free, open source cross-platform multimedia player developed by the[VideoLAN project.](https://www.videolan.org/)Seamless compatibility with all files and screens is at the core of VLC's design. VLC is able to play most local video and audio files as well as various streaming protocols, and a large number of third-party apps use the VLC engine to handle video playback. Ultimately, VideoLAN's developers want users to be able to play everything, everywhere --- no matter what device or screen size they prefer.

The team originally designed the[VLC app](https://play.google.com/store/apps/details?id=org.videolan.vlc)for Android, and it wasn't long before users started requesting the same experience on Chromebooks. That's when VideoLAN saw an opportunity to offer users a desktop-style experience by bringing VLC to ChromeOS.

By optimizing the Android app for ChromeOS and larger screens --- as well as supporting x86 and 64-bit ARM from the start --- VideoLAN ensured VLC users could enjoy the same immersive experience across a range of different devices and form factors.

## What they did

The team started by noting which features VLC users preferred on desktop, such as mouse input, right-click menus, and making sure external storage (i.e., hard drives and USB thumb drives) worked just right. From there, they started adjusting the app's layout and functionality to ensure users could enjoy those same features in a desktop-like environment.

### Keyboard and mouse support

One of the team's most important optimizations was to support keyboard and mouse input. Supporting keyboards allowed people to use shortcuts and direction buttons to easily navigate the app, while mouse input enabled right-click commands and file drag-and-drop to and from the VLC player.

### Dynamic resizing

VideoLAN designed multiple versions of the layout to allow users to easily scale and resize the app. Because the team had already designed VLC's layout for tablets, accommodating larger, wider layouts was a fairly simple process. They also tweaked the player's audio settings to take advantage of the extra real estate available on larger screens.

Previously, the team needed to use individual emulators or separate devices to test each layout. But, with Android support for ChromeOS, the team was able to test UI layout for desktop, tablet, and mobile all at once, on the same device, and without having to use an emulator. This substantially sped up the design and test times.

And now with[Linux (Beta) on ChromeOS](https://cros.page.link/linux-dev), developers can use Android Studio to build and test Android apps natively, making Chromebooks development-ready devices.  
![Image showing multiple versions of layout, examples of dynamic resizing across Mobile, Tablet and Laptop devices](https://developer.android.com/static/images/distribute/stories/vlc-1.png)

### Writing code in Kotlin

Best of all, the team did all the work in[Kotlin](https://developer.android.com/kotlin), a powerful programming language that helped them improve productivity by writing in safer and more concise code. By reducing the app's codebase, they were able to spend less time troubleshooting issues and more time optimizing the app's layout and functionality.

"We're usually reluctant to majorly restructure or rewrite our code because we risk losing functionality," said Geoffrey Métais, VideoLAN's lead Android developer. "We were pleased to find the transition from Java to Kotlin was really smooth, thanks to Android Studio's built-in migration tool, and Kotlin's[couroutines framework](https://developer.android.com/kotlin/coroutines)helped us improve performance."

## Results

VideoLAN used the same APK for mobile, ChromeOS, and Android TV, so it only took the lead developer two months to optimize the app for each platform. Users had been asking for VLC support on ChromeOS for months, especially for DVD playback, and the team has received overwhelmingly positive feedback so far. Plus, the latest version of ChromeOS fully supports external storage, so every Android user now enjoys the same benefit.

"Our team is always on the lookout for new opportunities to drive the biggest impact for our users," said VideoLAN President Jean-Baptiste Kempf. "Optimizing for Chromebooks has helped us extend our app across a huge number of devices and form factors, and it's clear we hit the mark based on feedback from users around the world."

## Get Started

Check out some best practices to[optimize your apps for ChromeOS](https://developer.android.com/topic/arc/optimizing).