---
title: https://developer.android.com/training/tv/tif
url: https://developer.android.com/training/tv/tif
source: md.txt
---

# Build TV input services

Watching live TV shows and other continuous, channel-based content is a big part of the TV experience. Users are accustomed to selecting and watching shows on TV by channel browsing. The TV Input Framework creates channels for publishing video or music content in the TV programming guide.

**Caution:** The TV Input Framework is meant to be used by OEMs to build channels for the Android system TV app. It is supported in Android 5.0 (API level 21) through Android 7.1 (API level 25) only. Third-party apps should build channels for their content using the Android TV home screen APIs. See[Recommend content on the home screen](https://developer.android.com/training/tv/discovery/recommendations)for details.

The TV Input Framework provides a unified method for the receiving and playback of live video content from hardware sources, such as HDMI ports and built-in-tuners, and software sources, such as video streamed over the internet.

The framework lets developers define live TV input sources by implementing a TV input service. This service publishes a list of channels and programs to the TV Provider. The live TV app on a TV device gets the list of available channels and programs from the TV Provider and displays them to a user.

When a user selects a specific channel, the live TV app creates a session for the associated TV input service through the TV Input Manager and tells the TV input service to tune to the requested channel and play the content to a display surface provided by the TV app.
![](https://developer.android.com/static/images/tv/tv-tif-overview.png)

**Figure 1.**Functional diagram of the TV Input Framework.

The TV Input Framework is designed to provide access to a wide variety of live TV input sources and bring them together in a single user interface where users can browse, view, and enjoy content. Building a TV input service for your content can help make it more accessible on TV devices.

For more details, check out the[TV Input Service](https://github.com/googlesamples/androidtv-sample-inputs)sample app.

## Topics

**[Develop a TV input service](https://developer.android.com/training/tv/tif/tvinput)**
:   Learn how to develop a TV input service that works with the system TV app.

**[Work with channel data](https://developer.android.com/training/tv/tif/channel)**
:   Learn how to describe channel and program data for the system.

**[Manage TV user interaction](https://developer.android.com/training/tv/tif/ui)**
:   Learn how to present overlays, manage content availability, and handle content selection.

**[Support time-shifting](https://developer.android.com/training/tv/tif/time-shifting)**
:   Learn how to support time-shifting in your TV input service.

**[Support content recording](https://developer.android.com/training/tv/tif/content-recording)**
:   Learn how to support content recording in your TV input service.