---
title: https://developer.android.com/stories/apps/vlc-android-tv
url: https://developer.android.com/stories/apps/vlc-android-tv
source: md.txt
---

# VLC adapts for Android TV to bring users’ personal videos to the big screen

![](https://developer.android.com/static/images/distribute/stories/vlc-icon.svg)

[VLC](https://www.videolan.org/vlc/index.html)---a free, open source cross-platform multimedia player developed by the[VideoLAN project](https://www.videolan.org/)---is rooted in giving users the power to play any type of video file anywhere, no matter their device or screen size. To deliver an optimal viewing experience to as many users as possible, the VideoLAN team has worked hard to adapt the VLC app for a variety of platforms, including Android TV and large-screen devices like[tablets and Chromebooks](https://developer.android.com/stories/apps/vlc).

## What they did

Apps on Android TV devices offer a unique viewing experience compared with apps on mobile devices. TV viewers sit farther from the screen, and they also typically expect to see their entire content library in a single view---like a traditional TV guide---while mobile users expect to see only the one video they chose to watch. Plus, users navigate apps on Android TV via remote control while the mobile apps are purely touchscreen.

While VideoLAN decided to retain most of VLC's mobile UI in the latest version of the app ([3.2](https://geoffreymetais.github.io/features/vlc-32/#)), the team needed to go a few steps further to ensure an optimal experience on both mobile and Android TV.

### Optimizing for TV remote controls

VideoLAN's first step was to ensure the app's video player UI would be easily navigable using remote controls from Android TV devices, which only has a directional pad and a few buttons. For instance, the team moved the video player options to a side panel so the full list would be easy to click on a smartphone or tablet and easy to browse with a remote.  
![VLC optimizes for large-screen, leanback viewing experiences on Android TV](https://developer.android.com/static/images/distribute/stories/vlc-atv-1.png)

### Tweaking the layout for Leanback Library

On Android TV devices, VLC users can see all their video categories at once, rather than aggregating categories as on mobile. To optimize for this browsing feature, the[Leanback Library](https://codelabs.developers.google.com/codelabs/androidtv-adding-leanback/index.html#0)uses extendable fragments to allow developers to easily create rich, animated experiences for each piece of content.

VideoLAN created a custom browsing UI to enable sorting and scrolling with a[Floating Action Button](https://material.io/components/buttons-floating-action-button/)and added animations for each scrolling option. The team also created a quick scroll feature similar to their Android Auto app that allows users to quickly browse their video content using first-letter searches, rather than needing to scroll the entire list.

Implementing an entirely new UI for Android TV led to a decent amount of code refactorization---that's where the Model-View-ViewModel (MVVM) architecture proposed by[Android's architecture components](https://developer.android.com/topic/libraries/architecture)came in handy. By following these[architectural guidelines](https://developer.android.com/jetpack/docs/guide), the team was able to create a clear separation between UI code and app logic, which simplified the sharing of the app logic code once the new UI was written. Now, the same code powers VLC's mobile and TV UI.

The team also worked with[Livedata transformations](https://developer.android.com/topic/libraries/architecture/livedata#transform_livedata)to create a map with elements grouped by video information (such as title, date added or video length) starting from the unique list they used on mobile. Because Android TV displays videos in landscape mode, the team split the content into several rows rather than featuring them in a vertical, scrollable list.

### Integrating voice controls and "play next" feature

Finally, VideoLAN implemented a[MediaSession](https://developer.android.com/guide/topics/media-apps/working-with-a-media-session)to enable voice command playback control via the Google Assistant. The team also added a "play next" feature to the TV app's code, which allows users to resume playback of a previously started video directly from the Android TV home screen.

## Results

As a free and easy-to-navigate media player, VLC is at its best on bigger screens. The VideoLAN team continues to receive positive feedback from users around the world, and internet service providers in France and Switzerland have even requested to add VLC as a default app on their set-top boxes.

"TVs are a natural home for a media player like VLC, so we knew there was a large community of people waiting to use the app on Android TV," said Jean-Baptiste Kempf, VideoLAN's President. "It was actually the simplest platform to optimize for as we were able to reuse 95% of the code from Android, and we've been thrilled with the results."

With an app designed for devices from small-screen smartphones to big-screen TVs, VideoLAN is primed to reach more mobile users wherever they prefer to watch their favorite videos.

## Getting started

Check out some best practices to[optimize your apps for Android TV](https://developer.android.com/training/tv/start).