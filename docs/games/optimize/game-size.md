---
title: https://developer.android.com/games/optimize/game-size
url: https://developer.android.com/games/optimize/game-size
source: md.txt
---

This guide describes how to reduce the size of a game. Upon installation, a
smaller game requires less time to download and less data. Both of these lead to
higher install conversions.
[Google research](https://medium.com/googleplaydev/shrinking-apks-growing-installs-5d3fcba23ce2)
shows that a 6 MB increase in served APK size results in a 1% decrease in
install rate. Many developers move assets out from the APK to a content delivery
network (CDN), but then incur costs both in hosting the CDN and in developing
and maintaining the asset management system.

To reduce the size of a game, perform the following steps:

1. [Use optimized delivery methods such as App Bundles and Play Asset Delivery](https://developer.android.com/games/optimize/game-size#bundles-and-pad).
2. [Determine the baseline size of the game and understand its structure](https://developer.android.com/games/optimize/game-size#determine-baseline).
3. [Search for assets and other files that can be reduced in size](https://developer.android.com/games/optimize/game-size#inspect-assets).
4. [Inspect the graphics textures and identify opportunities for optimization](https://developer.android.com/games/optimize/game-size#inspect-graphics-textures).
5. Follow the [general recommendations for assets](https://developer.android.com/games/optimize/game-size#general-recommendations).

## Use optimized delivery methods such as Android App Bundles and Play Asset Delivery

Consider the following delivery methods:

- While legacy projects typically output an APK for publishing, games
  publishing on Google Play should use an
  [Android App Bundle](https://developer.android.com/guide/app-bundle). App bundles deliver optimized APKs
  tailored to each user's device configuration. On average, app bundles reduce
  app size by 20%.

- To serve game assets via Google Play and exceed the 200MB download size
  limit for app bundles up to multiple GBs, use
  [Play Asset Delivery (PAD)](https://developer.android.com/guide/app-bundle/asset-delivery). No external
  CDN is required. PAD supports three distinct delivery methods, each of which
  can be used in a single game:

  - **Install-time:** Download assets upon installation. Assets are packaged in asset packs, which are a replacement for Opaque Binary Blob (OBB) files.
  - **Fast-follow:** Download assets after installation.
  - **On-demand:** The game initiates asset download as needed.

  PAD requires that games are packaged using the App Bundle format. PAD can
  also reduce the amount of data used by a developer's CDN (if one is still
  needed).
- Google Play uses Android App Bundles to generate and serve optimized APKs for
  each user's device configuration. These optimized APKs include a single set
  of texture assets, formatted with the optimal compression format for the
  device. Configure your app bundle to support different
  [texture compression formats](https://developer.android.com/guide/app-bundle/asset-delivery/texture-compression)
  to support the widest array of devices.

## Determine the baseline size of the game and understand its structure

To familiarize yourself with the game, determine the amount of work required for
any given optimization, and determine whether the game downloads additional
assets, perform the following steps:

1. Use a production (non-debug) build from the developer or the published APK.
2. Record the size of the binary file either as delivered by the developer or, if the game has been published, on the game's Play Store page. For APK size, the most important factor is the amount of data a user must download to run the actual game.
3. Install the game on a device and run it to the initial game menu. At this point, check the install size of the game as reported by Android (under **Settings \> Storage**). Some games have a small initial install size, as this is the key number to optimize, but download additional data after install. Some games download multiple gigabytes of data after install.
4. Some games download data only after you start playing them. You should play the game for a bit to determine how much additional data the game downloads for a typical user playing the game for the first time.

## Search for assets and other files that can be reduced in size

This section describes how to reduce the size of files in an APK. You can use
the
[App Bundle Explorer](https://play.google.com/console/about/app-bundle-explorer/)
to download device-specific APKs.

> [!NOTE]
> **Note:** For games built in Unity, disregard this section. Unity packages the game in the engine and most of the game's assets are put into a single binary file located at `assets/bin/Data/data.unity3d`.

To reduce the size of files packaged directly into the APK, perform the
following steps:

1. Use the Android Studio [APK Analyzer](https://developer.android.com/studio/debug/apk-analyzer). In Android Studio, select **File \> Profile or debug APK** and select your APK.
2. Select the **Assets** folder. For each file, the raw file size and the percentage of the total download size are listed.
3. Review the **Assets** folder and determine where the bulk of the game's data
   is located. Determine whether there are any assets that take up an excessive
   amount of space (that is, greater than 1% of the total). In particular, look
   for the following:

   - Large image and video files (for example, PNG, JPEG, and mp4 files): These files are typically used in splash screens, backgrounds, and logos. These files are rarely used in most games and can be compressed further without affecting the user experience. Lossless PNG files are particularly large and are excellent candidates for compression.
   - Large font files (for example, TTF files): If you add emoji support, it can significantly increase the font file's size. If a font file is larger than a few hundred kilobytes, consider ways to reduce its size.
   - Duplicate audio file formats or versions that you can combine.
4. If multiple [Application Binary Interfaces](https://developer.android.com/ndk/guides/abis) (ABIs) are
   included in the APK, move to [App Bundles](https://developer.android.com/guide/app-bundle) or build
   multiple APKs.

5. Determine the size of the binary shared object (.so) files. To inspect
   binary files to see whether there are things that might not need to be
   included, such as log files, you can use the
   [Bloaty McBloatface tool](https://github.com/google/bloaty).
   For more information about how to optimize the binary files, refer to
   [compile flags and options](https://developer.android.com/studio/build/shrink-code#optimization).

6. Review the Android manifest file for supported graphics formats. Determine
   whether there are multiple `<supports-gl-texture>` tags in the APK. If the
   game supports formats for multiple GPUs in one APK, then consider using
   [Binomial's Basis Universal](https://github.com/BinomialLLC/basis_universal).
   This GPU texture compression system creates texture files in an intermediate
   format that can be quickly transcoded to the GPU.

## Inspect the graphics textures and identify opportunities for optimization

This section describes the tools and methods required to determine whether the
graphics textures used in the game can be optimized.

To inspect the textures in the game, use [Android GPU
Inspector](https://developer.android.com/agi) (AGI),
[RenderDoc](https://renderdoc.org/), or, for Qualcomm Snapdragon
GPUs only, [Snapdragon
Profiler](https://developer.qualcomm.com/software/snapdragon-profiler).

Look for the following:

- Textures that can be resized to a smaller resolution, such as a large texture for something that is only rendered at a small size in the game. Downsampling textures is computationally expensive.
- Use of multiple small textures that can be combined into a single texture map.
- Textures that can use fewer bits in the color channels. Good candidates are textures with a few, solid textures. Gradients and shades of color require more bits of resolution, and therefore aren't good candidates.
- Explore better texture compression algorithms, from ETC1 to ETC2 and ASTC.
- Discard the top mipmap level when loading the textures on lower end devices
  to save memory. Unity's
  [Texture Streaming system](https://docs.unity3d.com/Manual/TextureStreaming.html)
  can do this.

- If you haven't already done so, review the Android manifest file for
  supported graphics formats. Determine whether there are multiple
  `<supports-gl-texture>` tags in the APK. If the game supports formats for
  multiple GPUs in one APK, then consider using
  [Binomial's Basis Universal](https://github.com/BinomialLLC/basis_universal).
  This GPU texture compression system creates texture files in an intermediate
  format that can be quickly transcoded to the GPU.

## General recommendations for assets

Follow these recommendations for an APK's assets:

- Image, audio, and video assets (not GPU textures): Determine whether the assets can be resized or compressed even further. Higher compression ratios are usually acceptable for games. Lossless PNG files are particularly large and are therefore excellent candidates for compression.
- Image assets (not GPU textures): Consider using [WEBP](https://developers.google.com/speed/webp), an image compression format for both lossy and lossless compression. Lossy WEBP compresses images 25% to 34% more than JPG.
- Reduce texture resolution: A texture much larger than the number of pixels that ultimately render on the screen is an inefficient use of space and GPU resources. To change a texture and see what it looks like in a frame without the need to rebuild the game, use [AGI](https://developer.android.com/agi).
- Change graphics' texture formats: Use texture formats that use fewer bits per channel. For example, use a 16-bit texture format such as RGB565 instead of a 32-bit texture format such as ARGB. For more information, refer to the following:
  - [Unity documentation for setting texture formats](https://docs.unity3d.com/ScriptReference/TextureFormat.html)
  - [Unity documentation for platform-specific texture compression formats](https://docs.unity3d.com/Manual/class-TextureImporterOverride.html)
  - [Binomial's Basis Universal texture format](https://github.com/BinomialLLC/basis_universal) for in-game model textures

## Additional resources

- [Recent Android App Bundle improvements and timeline for new apps on Google
  Play](https://android-developers.googleblog.com/2020/08/recent-android-app-bundle-improvements.html)
- [Reduce APK size in Android instant games](https://developer.android.com/topic/google-play-instant/getting-started/game-instant-app#apk-size-reduction)
- [GPU-decodable Supercompressed Textures (research paper)](http://gamma.cs.unc.edu/GST/gst.pdf)