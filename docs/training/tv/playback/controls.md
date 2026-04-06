---
title: Playback controls on TV  |  Android TV  |  Android Developers
url: https://developer.android.com/training/tv/playback/controls
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android TV](https://developer.android.com/training/tv)

# Playback controls on TV Stay organized with collections Save and categorize content based on your preferences.



Video playback is one of the most important features on TV. It's important
that video players in apps across Android TV behave the same. Here are the
recommendations on how video player controls should work on Android TV.

## Summary

| Button | Action |
| --- | --- |
| Center | Play or pause |
| Right single press | Forward +N seconds |
| Left single press | Rewind -N seconds |
| Press and hold right | Scrubbing forward |
| Press and hold left | Scrubbing rewind |
| Up or down | Peek information—progress, name, etc. |

**Important:** Refer to the
[TV App quality requiments](/docs/quality-guidelines/tv-app-quality)
for Media Playback before publishing.

## Play or pause

While a video or audio is playing, pressing the center D-pad button
pauses the media that is playing and, if applicable, shows
media playback controls like the progress bar and play button.

![Illustration of play/pause button](/static/training/tv/images/tv-playback-center.gif)


**Figure 1.** When media is playing, pressing the center D-pad button
pauses playback. Pressing the button again resumes playback.

## Rewind and fast-forward

Rewind and fast-forward are controlled by pressing the left or right D-pad
button when a video or audio is playing or paused. The playing or paused state
is maintained when rewinding or fast-forwarding.

![Illustration of forward/rewind button](/static/training/tv/images/tv-playback-right.gif)


**Figure 2.** When the left or right D-pad button is pressed once, playback
rewinds or fast-forwards by a set number of seconds.

## Peek information

Pressing the up or down D-pad button peeks up controls but does not pause the
video.

![Illustration of peeking information](/static/training/tv/images/tv-playback-bottom.gif)


**Figure 3.** Users can press the up or down D-pad button to show information about the
media without pausing playback.


Elephants dream © 2006, Blender Foundation/Netherlands Media Art
Institute/www.elephantsdream.org

[Previous

arrow\_back

Ambient mode](/training/tv/playback/ambient-mode)

[Next

Implement a media session

arrow\_forward](/training/tv/playback/media-session)