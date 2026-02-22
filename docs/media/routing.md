---
title: https://developer.android.com/media/routing
url: https://developer.android.com/media/routing
source: md.txt
---

As users connect their televisions, home theater systems, and music players with wireless
technologies, they want to be able to play content from Android apps on these larger,
louder devices. Enabling this kind of playback can turn your one-device, one-user app
into a shared experience that delights and inspires multiple users.

<br />

The Android media router APIs are designed to enable media display and playback on
remote receiver devices using a common user interface. App developers that
implement a [MediaRouter](https://developer.android.com/reference/androidx/mediarouter/media/MediaRouter) interface can then connect to the
framework and play content to devices that participate in the media router framework. Media
playback device manufacturers can participate in the framework by publishing a [MediaRouteProvider](https://developer.android.com/reference/androidx/mediarouter/media/MediaRouteProvider) that allows other applications to connect to and
play media on the receiver devices. Figure 1 illustrates how an app connects to a receiver
device through the media router framework.

<br />

![](https://developer.android.com/static/images/mediarouter/media-route-provider-framework.png)


**Figure 1.** Overview of how media route provider classes provide communication
from a media app to a receiver device.

<br />


**Note:** If you want your app to support
[Google Cast](https://developers.google.com/cast/) devices,
you should use the [Cast SDK](https://developers.google.com/cast/docs/reference/)
and build your app as a Cast sender. Follow the directions in the
[Cast documentation](https://developers.google.com/cast/docs/android_sender_setup)
instead of using the MediaRouter framework directly.

## MediaRouter support library

The mediarouter APIs are defined in the
[AndroidX MediaRouter library](https://developer.android.com/guide/topics/media/mediarouter).
This library is compatible with devices running Android 2.3 (API level 9) and higher and ensures a consistent
experience across all of them.
For detailed information about the mediarouter APIs, see the [androidx.mediarouter.media](https://developer.android.com/reference/androidx/mediarouter/media/package-summary)
package in the API reference.

**[MediaRouter API](https://developer.android.com/guide/topics/media/mediarouter)**
:   A media app uses the `MediaRouter` API to discover available remote playback devices and to route audio and video to them.

**[MediaRouteProvider API](https://developer.android.com/guide/topics/media/mediarouteprovider)**
:   The `MediaRouteProvider` API defines the capabilities of a remote playback device and makes it visible to apps that use a `MediaRouter` to search for alternative media paths.

## The output switcher

![](https://developer.android.com/static/images/mediarouter/output-switcher.png)

Starting with Android 11, your app's routing
options also appear in the system media player. This helps to give the user a
seamless journey when moving between devices as they change their viewing and
listening contexts, such as watching video in the kitchen versus on a phone,
or listening to audio in the home or car.

Pressing the route selection button in a media notification brings up the
output switcher with these choices by default:

- The speaker on the current device
- All connected Bluetooth audio devices

Apps can also provide more options depending on their capabilities, such as Cast.

Apps can use the [`MediaRouter`](https://developer.android.com/reference/androidx/mediarouter/media/MediaRouter)
API to customize
the routing choices. You can exclude devices you don't support (like filtering
out audio-only Chromecast if you're watching a Netflix smart TV) or include
other special devices that your app recognizes.