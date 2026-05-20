---
title: https://developer.android.com/blog/posts/media3-1-10-is-out
url: https://developer.android.com/blog/posts/media3-1-10-is-out
source: md.txt
---

#### [Product News](https://developer.android.com/blog/categories/product-news)

# Media3 1.10 is out

###### 2-min read

![](https://developer.android.com/static/blog/assets/Androidmedia3_1_10_6c365d70f6_Oaj9H.webp) 30 Mar 2026 [![](https://developer.android.com/static/blog/assets/andrew_lewis_1f4294eade_ZLA0xp.webp)](https://developer.android.com/blog/authors/andrew-lewis) [##### Andrew Lewis](https://developer.android.com/blog/authors/andrew-lewis)

###### Software Engineer

Media3 1.10 includes new features, bug fixes and feature improvements, including Material3-based playback widgets, expanded format support in ExoPlayer and improved speed adjustment when exporting media with Transformer. Read on to find out more, and check out the [full release notes](https://github.com/androidx/media/releases/tag/1.10.0) for a comprehensive list of changes.

#### Playback UI and Compose

We are continuing to expand the media3-ui-compose-material3 module to help you build Compose UIs for playback.  

We've added a new [Player Composable](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/material3/package-summary#Player(androidx.media3.common.Player,androidx.compose.ui.Modifier,kotlin.Int,androidx.compose.ui.layout.ContentScale,kotlin.Boolean,kotlin.Function0,kotlin.Boolean,kotlin.Function3,kotlin.Function3,kotlin.Function3)) that combines a ContentFrame with customizable playback controls, giving you an out-of-the-box player widget with a modern UI.

This release also adds a ProgressSlider Composable for displaying player progress and performing seeks using dragging and tapping gestures. For playback speed management, a new PlaybackSpeedControl is available in the base media3-ui-compose module, alongside a styled PlaybackSpeedToggleButton in the Material 3 module.

We'll continue working on new additions like track selection utils, subtitle support and more customization options in the upcoming Media3 releases. We're eager to hear your feedback so please share your thoughts on the project [issue tracker](https://github.com/androidx/media/issues).
![large_media31.102.jpeg](https://developer.android.com/static/blog/assets/large_media31_102_bc259f4117_Z1jVA9.webp) Player Composable in the Media3 Compose demo app

#### Playback feature enhancements

Media3 1.10 includes a variety of additions and improvements across the playback modules:

- Format support: ExoPlayer now supports extracting Dolby Vision Profile 10 and Versatile Video Coding (VVC) tracks in MP4 containers, and we've introduced MPEG-H UI manager support in the decoder_mpeghextension. The IAMF extension now seamlessly supports binaural output, either through the decoder viaiamf_tools or through the Android OS Spatializer, with new logic to match the output layout of the speakers.
- Ad playback: Improvements to reliability, improved HLS interstitial support forX-PLAYOUT-LIMIT and X-SNAP, and with the latest IMA SDK dependency you can control whether ad click-through URLs open in custom tabs with setEnableCustomTabs.

HLS: ExoPlayer now allows location fallback upon encountering load errors if redundant streams from different locations are available.

- Session: MediaSessionService now extends LifecycleService, allowing apps to access the lifecycle scoping of the service.

One of our key focus areas this year is on playback efficiency and performance. Media3 1.10 includes experimental support for scheduling the core playback loop in a more efficient way. You can try this out by enabling experimentalSetDynamicSchedulingEnabled() via the ExoPlayer.Builder. We plan to make further improvements in future releases so stay tuned!

#### Media editing and Transformer

For developers building media editing experiences, we've made speed adjustments more robust. EditedMediaItem.Builder.setFrameRate()can now set a maximum output frame rate for video. This is particularly helpful for controlling output size and maintaining performance when increasing media speed with setSpeed().

#### New modules for frame extraction and applying Lottie effects

In this release we've split some functionality into new modules to reduce the scope of some dependencies:

- FrameExtractor has been removed from the main media3-inspector module, so please migrate your code to use the new media3-inspector-framemodule and update your imports toandroidx.media3.inspector.frame.FrameExtractor.
- We have also moved theLottieOverlayeffect to a separate media3-effect-lottie module. As a reminder, this gives you a straightforward way to apply vector-based Lottie animations directly to video frames.

Please get in touch via the [issue tracker](https://github.com/androidx/media/issues) if you run into any bugs, or if you have questions or feature requests. We look forward to hearing from you!

###### Written by:

-

  ## [Andrew Lewis](https://developer.android.com/blog/authors/andrew-lewis)

  ###### Software Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/andrew-lewis) ![](https://developer.android.com/static/blog/assets/andrew_lewis_1f4294eade_ZLA0xp.webp) ![](https://developer.android.com/static/blog/assets/andrew_lewis_1f4294eade_ZLA0xp.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/paul_feng_759ac95845_spvRU.webp)](https://developer.android.com/blog/authors/paul-feng) 19 May 2026 19 May 2026 ![](https://developer.android.com/static/blog/assets/IO_26_Blog_Strapi_Icons_2000x1000px_0a8b06b49b_Z1e2APA.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [I/O 2026: What's new in Google Play](https://developer.android.com/blog/posts/i-o-2026-what-s-new-in-google-play)

  [arrow_forward](https://developer.android.com/blog/posts/i-o-2026-what-s-new-in-google-play) At this year's Google I/O, we talked about our evolving business model that offers more choice and new ways for your apps and content to be discovered on and off the store. We also unveiled advanced tools and insights that will help scale your business with less complexity.

  ###### [Paul Feng](https://developer.android.com/blog/authors/paul-feng) •
  6 min read

  - [#Google Play](https://developer.android.com/blog/topics/google-play)
  - [#Play Console](https://developer.android.com/blog/topics/play-console)
  - [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
  - [#Android Developers](https://developer.android.com/blog/topics/android-developers)
  - +2 ↩
- [![](https://developer.android.com/static/blog/assets/Luke_Hopkins_9c1e15d778_Z2o9b3q.webp)](https://developer.android.com/blog/authors/luke-hopkins) 19 May 2026 19 May 2026 ![](https://developer.android.com/static/blog/assets/Google_For_Developers_Android_Combo3_Strapi_2000x1000_56726aebea_Z1kvKHr.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android XR Updates for Unity, Unreal, and Godot](https://developer.android.com/blog/posts/android-xr-updates-for-unity-unreal-and-godot)

  [arrow_forward](https://developer.android.com/blog/posts/android-xr-updates-for-unity-unreal-and-godot) We are excited to announce that official support for Unreal Engine and Godot has arrived for Android XR. We are also launching new tools designed to boost your productivity and enable new XR capabilities: the Android XR Engine Hub and the Android XR Interaction Framework.

  ###### [Luke Hopkins](https://developer.android.com/blog/authors/luke-hopkins) •
  4 min read

  - [#Android XR](https://developer.android.com/blog/topics/android-xr)
  - [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
- [![](https://developer.android.com/static/blog/assets/Paul_Lammertsma_2f7e1baf32_Z28iSTy.webp)](https://developer.android.com/blog/authors/paul-lammertsma) 19 May 2026 19 May 2026 ![](https://developer.android.com/static/blog/assets/Google_For_Developers_Android_Text_Strapi_2000x1000_2d4221d884_ZtW7eg.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Increasing app discovery and engagement on Google TV](https://developer.android.com/blog/posts/increasing-app-discovery-and-engagement-on-google-tv)

  [arrow_forward](https://developer.android.com/blog/posts/increasing-app-discovery-and-engagement-on-google-tv) We're excited to share Google TV features and developer tools designed to increase the discoverability of your content and prepare your app for future TV experiences.

  ###### [Paul Lammertsma](https://developer.android.com/blog/authors/paul-lammertsma) •
  4 min read

  - [#Gemini features](https://developer.android.com/blog/topics/gemini-features)
  - [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
  - [#Engage SDK](https://developer.android.com/blog/topics/engage-sdk)
  - +1 ↩

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)