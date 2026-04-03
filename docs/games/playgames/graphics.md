---
title: https://developer.android.com/games/playgames/graphics
url: https://developer.android.com/games/playgames/graphics
source: md.txt
---

Google Play Games on PC requires that you update the graphics capabilities of
your game and add support for large screens. This topic describes those
requirements and related recommendations.

> [!NOTE]
> **Note:** For additional requirements, such as the other [PC compatibility requirements](https://developer.android.com/games/playgames/pc-compatibility), see the [get started](https://developer.android.com/games/playgames/start) guide.

Here's a summary of the requirements and recommendations on this page:

- [Prefer using Vulkan, up to version 1.1](https://developer.android.com/games/playgames/graphics#prefer-vulkan) (recommended)
- [When possible, use texture compression](https://developer.android.com/games/playgames/graphics#texture-compression) (recommended)
- [When possible, avoid textures that require transcoding](https://developer.android.com/games/playgames/graphics#transcoding-textures) (recommended)
- [Increase or remove frame rate limits](https://developer.android.com/games/playgames/graphics#increase-max-frame-rate) (recommended)
- [Use high resolution assets and textures](https://developer.android.com/games/playgames/graphics#high-resolution-assets) (required)
- [Adjust UI scaling](https://developer.android.com/games/playgames/graphics#ui-scaling) (required)
- [Support the required aspect ratios](https://developer.android.com/games/playgames/graphics#aspect-ratios) (required)
- [Make dynamic display updates](https://developer.android.com/games/playgames/graphics#dynamic-display) (required)

## Prefer Vulkan to OpenGL ES

We recommend using the Vulkan API on Google Play Games on PC for optimal
performance. We support Vulkan versions up to 1.1.

If using Vulkan 1.1 or below is not possible, then please use OpenGL ES. All
versions of OpenGL ES (namely, 3.2 and below) are supported.

## Texture compression

Since Google Play Games on PC passes through compressed textures whenever
possible, you should use `DXTC` or `BPTC` to take advantage of PC hardware.
Sometimes these textures still need to be decompressed if OpenGL features need
to be emulated for compatibility reasons, so you should always profile your
game.

### Avoid Texture Transcoding

Although Google Play Games on PC supports the mobile texture formats `ASTC`,
`ETC1`, and `ETC2`, the vast majority of desktop GPUs cannot natively sample
them, which requires runtime software transcoding to other texture formats.

Texture transcoding has a slight negative impact on performance and texture
memory usage, so it is better to use one of the desktop-friendly compressed
texture formats discussed [above](https://developer.android.com/games/playgames/graphics#texture-compression).

## Increase maximum frame rate limits

Some players will be able to run your game at a much higher frame rate on PCs
than on mobile devices. To give your players the best experience, we recommend
either ensuring the cap is at least 60 fps or removing your frame rate limits
altogether.

## Large screen optimization

The following large-screen optimizations are required by Google Play Games on PC:

### High resolution assets and textures

Google Play Games on PC supports resolutions up to 4k and you can expect a
performance level that matches a high-end Android-powered device released in the
last 12 months. Textures and assets designed for a smaller phone screen degrade
a player's perception of your game when viewed on a large 4k monitor on a PC.
When possible, ensure high resolution assets are available on first launch.

If you're using [Opaque Binary Blob OBB files](https://developer.android.com/studio/command-line/jobb) (also
known as APK expansion files) to deliver assets, additional high resolution
assets might cause the total size to exceed the OBB limit of 2 GB main plus 2GB
patch). In this case, consider using
[Play Asset Delivery](https://developer.android.com/guide/app-bundle/asset-delivery) to deliver your assets.

With Play Asset Delivery, you can automatically deliver the textures that match
a device's best supported texture compression format without increasing the game
size. You can also target devices based on their performance level, and
automatically deliver higher or lower resolution textures accordingly.

Play Asset Delivery is supported on
[Unity 5.6 and above](https://developer.android.com/guide/app-bundle/asset-delivery/build-unity) through the
Play Asset Delivery Unity plugin, and on
[Unreal Engine 4.25](https://docs.unrealengine.com/en-US/Platforms/Mobile/Android/Distribution/GooglePlayAssetDeliveryReference/index.html).
For other engines, we provide
[Java and Native SDKs](https://developer.android.com/guide/app-bundle/asset-delivery/build-native-java).

### UI scaling

On a larger screen, you may need to adjust your game's UI to ensure all elements
are appropriately sized. We recommend that HUDs take up no more than 20% of the
screen.

### Aspect ratios

Google Play Games on PC requires support for the 16:9 aspect ratio. For an
ideal player experience, games should also support 21:9, 16:10, and 3:2.

#### Portrait mode

Portrait mode games only need to support the 9:16 aspect ratio. Google Play Games on PC renders black bars in full screen mode if your game lacks
landscape support.

### Dynamic display

Google Play Games on PC never changes the logical resolution, display density,
nor aspect ratio of your game after it launches. Despite this, players can
toggle a game between fullscreen and windowed mode. When in windowed mode, the
player may also freely resize the window diagonally in a manner that maintains a
fixed aspect ratio. This means that your game doesn't have to handle resize
events to fit in with typical desktop windowing paradigms but it also means that
you can't rely on display density as an indicator of legibility of in-game
elements.

#### Choose a resolution

Google Play Games on PC provides your game with the aspect ratio that is the
closest match between a player's primary display and the advertised support in
your [app manifest](https://developer.android.com/guide/topics/manifest/manifest-intro). The default
resolution is chosen using internal heuristics to give the player the best
possible experience.

The player can override the default resolution for your game on their machine.
The aspect ratio calculation does not change, but the number of pixels you
render may be different between any two launches of your game. It's important to
be aware of this if you rely on reported resolution between launches of your
game, such as when determining which assets to cache and render. Google Play Games on PC Developer Emulator relaunches after a user changes the resolution so
you don't have to handle this change at runtime.

#### Best practices

To give your players the best experience, do the following:

- If your game plays best in portrait mode and players are likely to play it while multitasking, set [`android:screenOrientation="portrait"`](https://developer.android.com/guide/topics/manifest/activity-element#screen). This guarantees a portrait oriented window for your game.
- Specify supported min and max aspect ratios with `android:minAspectRatio` and `android:maxAspectRatio` to restrict your game to a range of verified aspect ratios. Thoroughly test your game within this range paying special attention to what happens with extremely wide, square, and tall aspect ratios.
- Although Google Play Games on PC reports DPI, this does not change while your game is active. Therefore it is impossible to figure out the physical size of an in-game element and it is best to place game elements based on ratios of the screen size rather than trying to [match a physically based size unit](https://developer.android.com/training/multiscreen/screendensities).
- Test the legibility of your game elements on a laptop screen and in windowed mode.
- Give players in-game control over the ui scale so they can size in-game elements or text to meet their personal preferences or environment needs. This helps avoid having players lower your game's resolution (and therefore visible quality) only to make text larger.

#### Testing dynamic display

The Google Play Games on PC Developer Emulator doesn't have extensive gui-based controls for
verifying every potential combination of resolution and aspect ratio. To
simulate running your game at a specific resolution, use the `wm size` command
in your [adb shell](https://developer.android.com/games/playgames/pg-emulator#adb-compatibility). For
example, to test a game at 4K use the following command:

    adb shell wm size 3840x2160

You can reset the display scale using the following command:

    adb shell wm size reset