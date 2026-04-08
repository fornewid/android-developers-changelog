---
title: Enhance app experiences with perception using ARCore for Jetpack XR  |  Android XR for Jetpack XR SDK  |  Android Developers
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore
source: html-scrape
---

The Android XR SDK has  [reached Developer Preview 3](https://android-developers.googleblog.com/2025/12/build-for-ai-glasses-with-android-xr.html), and we want your feedback! Try things out, and visit our [support page](/develop/xr/support) to reach out.

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android XR](https://developer.android.com/develop/xr)
* [Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk)
* [Guides](https://developer.android.com/develop/xr/get-started)

# Enhance app experiences with perception using ARCore for Jetpack XR Stay organized with collections Save and categorize content based on your preferences.



Applicable XR devices

This guidance helps you build experiences for these types of XR devices.

[Learn about XR device types →](/develop/xr/devices)

![](/static/images/develop/xr/xr-headsets-icon.svg)


XR Headsets

![](/static/images/develop/xr/xr-glasses-icon.svg)


Wired XR Glasses

![](/static/images/develop/xr/ai-glasses-icon.svg)


AI Glasses

[Learn about XR device types →](/develop/xr/devices)

ARCore for Jetpack XR brings powerful perception capabilities for your app to
understand the real world through a variety of APIs. Some of these APIs help you
enhance immersive experiences for devices such as XR headsets and wired XR
glasses, some help you enhance augmented experiences for devices such as AI
glasses, and some help you enhance app experiences for all types of Android XR
devices.

For example, you can use ARCore for Jetpack XR to retrieve planar data, anchor
content to a fixed location in space, or use a geospatial pose to anchor content
to a real-world location.

## Add library dependencies

Before you begin using perception features in your XR app, [add the necessary
dependencies](/develop/xr/jetpack-xr-sdk/set-up-sdk#add-dependencies), depending on the type of app experiences you are enhancing
with AR.

## Access a session

Perception features in ARCore for Jetpack XR rely on a [`Session`](/reference/kotlin/androidx/xr/runtime/Session), which
uses the Jetpack XR Runtime.

How your app should access a session depends on the types of app experiences
that you're enhancing with perception features:

* If your app is enhancing immersive experiences with [spatial UI](/develop/xr/jetpack-xr-sdk/ui-compose) using
  Jetpack Compose for XR, [access a session from Jetpack Compose for XR](/develop/xr/jetpack-xr-sdk/add-session#localsession).
* For all other situations, you can access [access a session from Jetpack XR
  Runtime](#access-session-runtime), which is covered in the following section on this page.

### Access a session from Jetpack XR Runtime

To access a session from Jetpack XR Runtime, you'll create it:

To create a session, pass an activity to the [`create()`](/reference/kotlin/androidx/xr/runtime/Session#create(android.app.Activity,kotlin.coroutines.CoroutineContext))
method, as shown in the following example:

```
when (val result = Session.create(this)) {
    is SessionCreateSuccess -> {
        val xrSession = result.session
        // ...
    }
    else ->
        TODO(/* A different unhandled exception was thrown. */)
}

Session.kt
```

**Note:** You can only create a session on either an Android XR device, or on a
[supported ARCore device](https://developers.google.com/ar/devices).

When a session's activity is destroyed, all AR content associated with that
session is destroyed, and the session is no longer valid.

## Configure a session

Some features might be disabled by default and must be configured in order to
function. To configure a session, use [`configure()`](/reference/kotlin/androidx/xr/runtime/Session#configure(androidx.xr.runtime.Config)) and specify [the
configuration options](/reference/kotlin/androidx/xr/runtime/Config) that your [`Session`](/reference/kotlin/androidx/xr/runtime/Session) needs. For details about
the required configuration for different AR features, see the corresponding
pages for each AR feature.

## Next steps

After your app has a session, explore the ways you can use it to enhance app
experiences for different XR devices:

* [Detect planes using ARCore for Jetpack XR](/develop/xr/jetpack-xr-sdk/arcore/anchors)
* [Create anchors with ARCore for Jetpack XR](/develop/xr/jetpack-xr-sdk/arcore/planes)
* [Work with hands using ARCore for Jetpack XR](/develop/xr/jetpack-xr-sdk/arcore/hands)
* [Incorporate the head position in your app with ARCore for Jetpack XR](/develop/xr/jetpack-xr-sdk/arcore/head)
* [Incorporate face tracking in your app with ARCore for Jetpack XR](/develop/xr/jetpack-xr-sdk/arcore/face)
* [Retrieve depth information in your app with ARCore for Jetpack XR](/develop/xr/jetpack-xr-sdk/arcore/depth)
* [Track a device's pose using ARCore for Jetpack XR](/develop/xr/jetpack-xr-sdk/arcore/device-pose)
* [Work with geospatial poses using ARCore for Jetpack XR](/develop/xr/jetpack-xr-sdk/arcore/geospatial)