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

  [read_more
  View profile](https://developer.android.com/blog/authors/andrew-lewis) ![View Andrew Lewis's profile](https://developer.android.com/static/blog/assets/andrew_lewis_1f4294eade_ZLA0xp.webp) ![View Andrew Lewis's profile](https://developer.android.com/static/blog/assets/andrew_lewis_1f4294eade_ZLA0xp.webp)
Continue reading
- [![View Raghavendra Hareesh Pottamsetty's profile](https://developer.android.com/static/blog/assets/Raghavendra_Hareesh_Pottamsetty_72fdb063a0_1h0S85.webp)](https://developer.android.com/blog/authors/raghavendra-hareesh-pottamsetty) 26 Aug 2026 26 Aug 2026 ![](https://developer.android.com/static/blog/assets/Raising_the_bar_Google_Play_Strapi_2_a80695bf12_Z2jxf1k.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Elevating app quality: Reducing memory usage and improving device migration](https://developer.android.com/blog/posts/elevating-app-quality-reducing-memory-usage-and-improving-device-migration)

  [arrow_forward](https://developer.android.com/blog/posts/elevating-app-quality-reducing-memory-usage-and-improving-device-migration) Maintaining a healthy Android ecosystem is a shared commitment where every app and game has a role to play.
  [Raghavendra Hareesh Pottamsetty](https://developer.android.com/blog/authors/raghavendra-hareesh-pottamsetty) • 4 min read
- [![View Ron Aquino's profile](https://developer.android.com/static/blog/assets/unnamed_18_8bd07de9bd_9wUet.webp)](https://developer.android.com/blog/authors/ron-aquino) 25 Aug 2026 25 Aug 2026 ![](https://developer.android.com/static/blog/assets/Ensuring_a_safe_Gen_AI_ecosystem_on_Google_Play_Scrapi_a8fa6da415_ZsHups.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Ensuring Safety in the Generative AI Ecosystem: Protecting Users from Non-Consensual Intimate Content](https://developer.android.com/blog/posts/ensuring-safety-in-the-generative-ai-ecosystem-protecting-users-from-non-consensual-intimate-content)

  [arrow_forward](https://developer.android.com/blog/posts/ensuring-safety-in-the-generative-ai-ecosystem-protecting-users-from-non-consensual-intimate-content) At Google Play, user safety and developer success go hand in hand. We continue to see growth in apps with AI generated features, and indeed, adding generative AI into your apps is a great way to unlock incredible creative possibilities.
  [Ron Aquino](https://developer.android.com/blog/authors/ron-aquino) • 4 min read
- 3 Authors 24 Aug 2026 24 Aug 2026 ![](https://developer.android.com/static/blog/assets/Android_1_Strapi_6f49d09922_ZVXnJg.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [AAOS SDV - Secure by Design](https://developer.android.com/blog/posts/aaos-sdv-secure-by-design)

  [arrow_forward](https://developer.android.com/blog/posts/aaos-sdv-secure-by-design) At Google, we believe our products should be secure by design, which is why we built the Android Automotive Operating System for Software Defined Vehicle (AAOS SDV) on existing, market-proven platforms, leveraging virtualization technologies like Cuttlefish.
  [Markus Vill](https://developer.android.com/blog/authors/markus-vill), [Sean Keys](https://developer.android.com/blog/authors/sean-keys), [István Nádor](https://developer.android.com/blog/authors/istvan-nador) • 5 min read
  - [#Android Auto](https://developer.android.com/blog/topics/android-auto)
  - [#Security](https://developer.android.com/blog/topics/security)
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)