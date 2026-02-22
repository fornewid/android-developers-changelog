---
title: https://developer.android.com/develop/connectivity/5g/enhance-with-5g
url: https://developer.android.com/develop/connectivity/5g/enhance-with-5g
source: md.txt
---

# Enhance your apps with 5G

Sometimes changes to an Android app are little steps, and sometimes they require you to completely change the way you think. 5G is not a little step.

**Incremental experience**
:   An experience that's identical to the 4G experience but just happens to be naturally better because of the higher bandwidth and lower latency of 5G. Often just the Wi-Fi experience.

**Transformative experience**
:   An experience that's new and entirely dependent on the benefits of 5G (bandwidth and latency) and on being able to detect the unmetered nature of the connection.

5G is about more than just faster speeds and lower latency. It opens the door to new possibilities in your apps. This topic goes over some of the ways that you can transform your user experience.

To jump right into adding 5G capabilities to your apps, see[Add 5G capabilities to your app](https://developer.android.com/about/versions/11/features/5g).

To learn more about best practices for developing 5G-ready apps, see[Best Practices for 5G App Developers](https://www.gsma.com/get-involved/working-groups/gsma_resources/idg-15-v1-0-best-practices-for-5g-app-developers)from GSMA.

## Turn indoor use cases into outdoor use cases

Before 5G, video chat required users to confirm that everyone else was on Wi-Fi or was okay with paying for the data costs of an expensive and low-quality stream. With unmetered 5G, you can just video call people and expect your call to always be accepted, no matter where people are.

With 5G, your users can stop planning downloads ahead of a trip, instead downloading what they need, when they need it. You can encourage that mental shift by exposing a UI that encourages users to download entire albums or by showing playlists of every episode of a show.

5G also opens up opportunities to engage in real-time, multiplayer games when not tethered to Wi-Fi. No more requirement to ensure everyone has a strong connection to their home network; with 5G gaming anytime, anywhere is now possible. You could even consider adding capabilities that are normally reserved for gaming laptops or desktop computers, like in-game voice and video chat.

## Turn photo-centric UX into video-centric or AR-centric UX

Until 5G, most apps' visual experience was centered around photos or short video clips. With the addition of 5G capabilities, your app can shift the user experience to be more immersive by adding[augmented reality](https://developers.google.com/ar/develop/java/quickstart)capabilities to your app, such as when using maps to guide users.

You can use the additional bandwidth to make the user experience more appealing by replacing photos with videos. Consider providing video carousels with pre-fetched videos that always start instantly.

## Prefetch helpfully

With 3G and 4G, best practices limited you to relatively small amounts of buffering of content that the user is currently consuming. 5G removes that limitation, enabling you to use your understanding of the user journey to help them by prefetching whole chunks of content you know they're likely to want.

For example, instead of requiring your users to assemble their own collections (like playlists, albums, or sets) and explicitly download them, you can offer new primitives that let users specify the constraints (last 50 songs I've listened to, 10 most popular songs in this city, and so on) and then download them opportunistically.

## Turn niche use cases into mainstream use cases

Without 5G, few users streamed or consumed streams. With the introduction of 5G, this niche use case can become a mainstream use case. Android 11, specifically, adds support for low-latency video codecs. Apps can use the new APIs to[check](https://developer.android.com/reference/android/media/MediaCodecInfo.CodecCapabilities#isFeatureSupported(java.lang.String))and[configure](https://developer.android.com/reference/android/media/MediaCodec.html#PARAMETER_KEY_LOW_LATENCY)low-latency playback for a specific codec. This helps provide 5G devices with a compelling user experience.

To learn about offering your users a use-case-specific performance boost, see \[Use network slicing(/develop/connectivity/5g/use-network-slicing).

## Tell your users when they're on 5G

On Android 11 and higher, apps with[`android.Manifest.permission.READ_PHONE_STATE`](https://developer.android.com/reference/android/Manifest.permission#READ_PHONE_STATE)permission can request telephony display information updates through[`PhoneStateListener.onDisplayInfoChanged()`](https://developer.android.com/reference/android/telephony/PhoneStateListener#onDisplayInfoChanged(android.telephony.TelephonyDisplayInfo)). This includes radio access technology information for marketing and branding purposes.

Various 5G icon display solutions for different carriers are provided by this new API. The supported technologies include the following:

- LTE
- LTE with carrier aggregation (LTE+)
- Advanced pro LTE (5Ge)
- NR (5G)
- NR on millimeter-wave cellular bands (5G+ and 5G UW)