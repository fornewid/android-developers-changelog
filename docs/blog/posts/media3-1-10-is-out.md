---
title: https://developer.android.com/blog/posts/media3-1-10-is-out
url: https://developer.android.com/blog/posts/media3-1-10-is-out
source: md.txt
---

> Documentation index: https://developer.android.com/blog/llms.txt

[Product News](https://developer.android.com/blog/categories/product-news.md.txt)

# Media3 1.10 is out

2 min read ![](https://developer.android.com/static/blog/assets/Androidmedia3_1_10_6c365d70f6_VsSP0.webp) 30 Mar 2026 [![View Andrew Lewis's profile](https://developer.android.com/static/blog/assets/andrew_lewis_1f4294eade_Z1SE2GD.webp)](https://developer.android.com/blog/authors/andrew-lewis.md.txt) [Andrew Lewis](https://developer.android.com/blog/authors/andrew-lewis.md.txt) Software Engineer Media3 1.10 includes new features, bug fixes and feature improvements, including Material3-based playback widgets, expanded format support in ExoPlayer and improved speed adjustment when exporting media with Transformer. Read on to find out more, and check out the [full release notes](https://github.com/androidx/media/releases/tag/1.10.0) for a comprehensive list of changes.

#### Playback UI and Compose

We are continuing to expand the media3-ui-compose-material3 module to help you build Compose UIs for playback.  

We've added a new [Player Composable](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/material3/package-summary.md.txt#Player(androidx.media3.common.Player,androidx.compose.ui.Modifier,kotlin.Int,androidx.compose.ui.layout.ContentScale,kotlin.Boolean,kotlin.Function0,kotlin.Boolean,kotlin.Function3,kotlin.Function3,kotlin.Function3)) that combines a ContentFrame with customizable playback controls, giving you an out-of-the-box player widget with a modern UI.

This release also adds a ProgressSlider Composable for displaying player progress and performing seeks using dragging and tapping gestures. For playback speed management, a new PlaybackSpeedControl is available in the base media3-ui-compose module, alongside a styled PlaybackSpeedToggleButton in the Material 3 module.

We'll continue working on new additions like track selection utils, subtitle support and more customization options in the upcoming Media3 releases. We're eager to hear your feedback so please share your thoughts on the project [issue tracker](https://github.com/androidx/media/issues).
![large_media31.102.jpeg](https://developer.android.com/static/blog/assets/large_media31_102_bc259f4117_1JaiNG.webp) Player Composable in the Media3 Compose demo app

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
Written by:

-

  ## [Andrew Lewis](https://developer.android.com/blog/authors/andrew-lewis.md.txt)

  ###### Software Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/andrew-lewis) ![View Andrew Lewis's profile](https://developer.android.com/static/blog/assets/andrew_lewis_1f4294eade_Z1SE2GD.webp) ![View Andrew Lewis's profile](https://developer.android.com/static/blog/assets/andrew_lewis_1f4294eade_Z1SE2GD.webp)
Continue reading
- [![View Aurash Mahbod's profile](https://developer.android.com/static/blog/assets/image3_98854eb3dd_Z2kItkm.webp)](https://developer.android.com/blog/authors/aurash-mahbod.md.txt) 18 Nov 2026 18 Nov 2026 ![](https://developer.android.com/static/blog/assets/ABL_162_2000x1000_1_ce7dba8d2a_72W03.webp) [Product News](https://developer.android.com/blog/categories/product-news.md.txt)

  ## [Elevating games: New large screens and foldables quality standards on Google Play](https://developer.android.com/blog/posts/elevating-game-quality-foldables-large-screens-google-play.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/elevating-game-quality-foldables-large-screens-google-play.md.txt) To give these experiences to players and ensure your games shine across every screen size, Google Play is introducing new large screen quality requirements for games
  [Aurash Mahbod](https://developer.android.com/blog/authors/aurash-mahbod.md.txt) • 4 min read
  - [#Google Play](https://developer.android.com/blog/topics/google-play.md.txt)
  - [#Android](https://developer.android.com/blog/topics/android.md.txt)
  - [#Adaptive Games](https://developer.android.com/blog/topics/adaptive-games.md.txt)
  - [#Foldables](https://developer.android.com/blog/topics/foldables.md.txt)
  - [#Large Screens](https://developer.android.com/blog/topics/large-screens.md.txt)
  - +3 ↩
- [![View Meghan Mehta's profile](https://developer.android.com/static/blog/assets/meghan_d663ed9c69_e0a5b5a564_Z2r6wan.webp)](https://developer.android.com/blog/authors/meghan-mehta.md.txt) 18 Nov 2026 18 Nov 2026 ![](https://developer.android.com/static/blog/assets/0420_Compose_1_11_Strapi_812f851abd_WuQ5h.webp) [Product News](https://developer.android.com/blog/categories/product-news.md.txt)

  ## [What's new in the Jetpack Compose November '26 release](https://developer.android.com/blog/posts/jetpack-compose-november-2026-release.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/jetpack-compose-november-2026-release.md.txt) The Jetpack Compose November '26 release is stable! This release brings version 1.13 across core Compose modules (see the full BOM mapping), introducing updates to text, graphics, layouts, performance, and more---along with a few important deprecations and behavior changes to be aware of.
  [Meghan Mehta](https://developer.android.com/blog/authors/meghan-mehta.md.txt) • 10 min read
  - [#Adaptive \& Differentiated](https://developer.android.com/blog/topics/adaptive-and-differentiated.md.txt)
- [![View Mekka Okereke's profile](https://developer.android.com/static/blog/assets/unnamed_32_974e21c6be_Z1qBCTw.webp)](https://developer.android.com/blog/authors/mekka-okereke.md.txt) 18 Nov 2026 18 Nov 2026 ![](https://developer.android.com/static/blog/assets/ABL_163_Elevating_Adaptive_App_Quality_Blue_30a2165ec7_Z1hsFPv.webp) [Product News](https://developer.android.com/blog/categories/product-news.md.txt)

  ## [Elevating apps: New adaptive quality standards on Google Play](https://developer.android.com/blog/posts/google-play-adaptive-quality-standards.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/google-play-adaptive-quality-standards.md.txt) To give users the premium experience they expect and ensure your apps shine across every screen size, Google Play is introducing new adaptive app quality requirements that go into effect April 2027.
  [Mekka Okereke](https://developer.android.com/blog/authors/mekka-okereke.md.txt) • 4 min read
  - [#Adaptive Games](https://developer.android.com/blog/topics/adaptive-games.md.txt)
  - [#Foldables](https://developer.android.com/blog/topics/foldables.md.txt)
  - [#Adaptive apps](https://developer.android.com/blog/topics/adaptive-apps.md.txt)
  - +1 ↩
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1zVtXW.webp)