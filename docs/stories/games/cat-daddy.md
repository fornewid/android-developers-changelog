---
title: https://developer.android.com/stories/games/cat-daddy
url: https://developer.android.com/stories/games/cat-daddy
source: md.txt
---

# 2K delivers higher quality graphics with Play Asset Delivery

## Background

![NBA 2K Mobile, NBA SuperCard, WWE SuperCard](https://developer.android.com/static/images/cards/distribute/stories/cat-daddy-games-logo.png "NBA 2K Mobile, NBA SuperCard, WWE SuperCard")

Cat Daddy Games is a wholly-owned[2K](https://play.google.com/store/apps/dev?id=6681606924556273560)studio based in Kirkland, Washington. The teams behind the NBA 2K Mobile, NBA SuperCard, and WWE SuperCard series were looking for a solution to improve the overall quality of their games for users, specifically by serving higher quality assets on devices that support them.

They implemented Play Asset Delivery, which offered a simple and more flexible way to generate and serve optimized APKs for each user's device configuration, and used Texture Compression Format Targeting to deliver better art assets for specific devices and reduce asset downloads.

## What they did

To start, Cat Daddy switched over from using the APK Expansion File data delivery system to the new[Android App Bundle (AAB)](https://developer.android.com/guide/app-bundle)and[Play Asset Delivery (PAD)](https://developer.android.com/guide/playcore/asset-deliverysystem). The studio integrated PAD into its custom Gradle-based build system, and with minimal client side code changes, smoothly replaced their legacy download with a PAD Fast Follow download.

The deprecated APK Expansion File system was tied to the app's version number, which added extra complications while developing and testing. The new AAB system creates a version independent, self-contained bundle, which Cat Daddy easily tested using the Internal App Sharing portal. This does not require uploading the versioned OBB data or being concerned about the app version of local test builds.

One of Cat Daddy's favorite features in the PAD system is the ability to provide[Texture Compression Format specific data files](https://developer.android.com/guide/playcore/asset-delivery/texture-compression). This is implemented entirely on the Google Play side without requiring any client changes. Google detects the capabilities of the device and serves up the appropriate data. Cat Daddy only needed to add the additional data file to its build, and Google did the rest. These data formats do not count against any of the file size limitations.

Cat Daddy provided an additional set of data files for devices that support ASTC texture compression. Previously, the team had been using ASTC for high-quality artwork on all devices to maintain quality and compression, decompressing the texture on the CPU for devices that do not support ASTC. The studio used ETC1 for the GUI graphics.

## Results

By implementing PAD, Cat Daddy is able to have version-independent asset management. The studio's games have the entire build contained in a single bundle, rather than separating out the assets. This results in a much cleaner and more flexible build and test environment. By using Texture Compression Format specific data, they provide data packs that use ASTC format for all textures, including the GUI, which results in higher quality GUI graphics for those devices that support ASTC.

For the players of Cat Daddy's games, they maintained aggressive asset size minimization that resulted in download speed optimizations, providing a more seamless and smoother gameplay experience.

## Get started

Get started today by learning more about[Play Asset Delivery](https://developer.android.com/guide/app-bundle/asset-delivery)and[Texture Compression Format Targeting](https://developer.android.com/guide/playcore/asset-delivery/texture-compression).