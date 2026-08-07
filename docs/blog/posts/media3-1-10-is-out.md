---
title: https://developer.android.com/blog/posts/media3-1-10-is-out
url: https://developer.android.com/blog/posts/media3-1-10-is-out
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news)

# Media3 1.10 is out

2 min read ![](https://developer.android.com/static/blog/assets/Androidmedia3_1_10_6c365d70f6_Oaj9H.webp) 30 Mar 2026 [![View Andrew Lewis's profile](https://developer.android.com/static/blog/assets/andrew_lewis_1f4294eade_ZLA0xp.webp)](https://developer.android.com/blog/authors/andrew-lewis) [Andrew Lewis](https://developer.android.com/blog/authors/andrew-lewis) Software Engineer Media3 1.10 includes new features, bug fixes and feature improvements, including Material3-based playback widgets, expanded format support in ExoPlayer and improved speed adjustment when exporting media with Transformer. Read on to find out more, and check out the [full release notes](https://github.com/androidx/media/releases/tag/1.10.0) for a comprehensive list of changes.

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
Written by:

-

  ## [Andrew Lewis](https://developer.android.com/blog/authors/andrew-lewis)

  ###### Software Engineer

  [read_more View profile](https://developer.android.com/blog/authors/andrew-lewis) ![View Andrew Lewis's profile](https://developer.android.com/static/blog/assets/andrew_lewis_1f4294eade_ZLA0xp.webp) ![View Andrew Lewis's profile](https://developer.android.com/static/blog/assets/andrew_lewis_1f4294eade_ZLA0xp.webp)
Continue reading
- [![View Paul Feng's profile](https://developer.android.com/static/blog/assets/paul_feng_759ac95845_spvRU.webp)](https://developer.android.com/blog/authors/paul-feng) 29 Jul 2026 29 Jul 2026 ![](https://developer.android.com/static/blog/assets/Google_Play_Age_Signals_API_Blog_Strapi_d532f6c0b8_Z298Ads.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Delivering safer, age-appropriate experiences on Google Play](https://developer.android.com/blog/posts/delivering-safer-age-appropriate-experiences-on-google-play)

  [arrow_forward](https://developer.android.com/blog/posts/delivering-safer-age-appropriate-experiences-on-google-play) Providing a safe online experience and protecting users from harm is a top priority at Google Play.
  [Paul Feng](https://developer.android.com/blog/authors/paul-feng) • 2 min read
- 3 Authors 28 Jul 2026 28 Jul 2026 ![](https://developer.android.com/static/blog/assets/Jetpack_compose_Strapi_123481f79e_Z1F9b9M.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Celebrating 5 years of Jetpack Compose](https://developer.android.com/blog/posts/celebrating-5-years-of-jetpack-compose)

  [arrow_forward](https://developer.android.com/blog/posts/celebrating-5-years-of-jetpack-compose) Today, we officially celebrate five years since the release of Jetpack Compose 1.0. From version 1.0, announced on July 28th, 2021, to our latest 1.11 release, we've seen the APIs evolve significantly over the years, and we're taking a moment to celebrate.
  [Rebecca Franks](https://developer.android.com/blog/authors/rebecca-franks), [Nick Butcher](https://developer.android.com/blog/authors/nick-butcher), [Loryn Hairston](https://developer.android.com/blog/authors/loryn-hairston) • 4 min read
- [![View Fahd Imtiaz's profile](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z15U8cx.webp)](https://developer.android.com/blog/authors/fahd-imtiaz)[![View Miguel Montemayor's profile](https://developer.android.com/static/blog/assets/miguel_montemayor_552207c1c6_Z1tItyG.webp)](https://developer.android.com/blog/authors/miguel-montemayor) 22 Jul 2026 22 Jul 2026 ![](https://developer.android.com/static/blog/assets/MM_Adaptive_and_device_Meta_18e67bafd8_Z1BKgnT.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Optimize your apps for the next generation of Samsung Galaxy devices](https://developer.android.com/blog/posts/optimize-your-apps-for-the-next-generation-of-samsung-galaxy-devices)

  [arrow_forward](https://developer.android.com/blog/posts/optimize-your-apps-for-the-next-generation-of-samsung-galaxy-devices) Today at Galaxy Unpacked, Samsung unveiled its latest lineup of foldable and wearable devices. For developers, this means that the variety of form factors, screen sizes, and device postures your app needs to support is expanding once again.
  [Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz), [Miguel Montemayor](https://developer.android.com/blog/authors/miguel-montemayor) • 3 min read
Stay in the loop

Get the latest Android development insights delivered to your inbox weekly.
[mail Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)