---
title: https://developer.android.com/guide/playcore/asset-delivery/texture-compression
url: https://developer.android.com/guide/playcore/asset-delivery/texture-compression
source: md.txt
---

# Target texture compression formats in Android App Bundles

*Textures* are images that can be applied to the surface of a 3D model. Textures
are also used by 2D renderers to draw elements such as sprites or backgrounds.
This page describes popular texture compression formats used in games and how to
target them in Android App Bundles. Read
[About Android App Bundles](https://developer.android.com/guide/app-bundle) and
[Play Asset Delivery](https://developer.android.com/guide/playcore/asset-delivery) before starting this
guide.

## Background

GPUs typically support a set of texture compression formats. A
texture compression format (or TCF) is a file format that is optimized for GPUs.
The GPU loads and renders a texture quicker, and with less memory, than if it
were using an array of RGBA values in memory. This support is done at the
hardware level: the GPU manufacturer embeds components into the graphic cards
chip that read, decompress, and render the supported formats.

The following are common texture compression formats on modern mobile hardware:

- ASTC: Recent format designed to supersede prior formats. More flexible than previous formats due to support for various block sizes. Using this format is a good way to optimize the size of your game.
- ETC2: Supported by all devices that support OpenGL ES 3.0 and higher. This includes nearly all active Android mobile devices.

These formats are supported by the following approximate percentages of Android
devices:

| Texture compression format | Percentage of Google Play devices with support |
|----------------------------|------------------------------------------------|
| ASTC                       | \>80%                                          |
| ETC2                       | \>95%                                          |

Desktop computer GPUs running Google Play Games for PC also support this format:

- DDS or S3TC: Sometimes called BCn, DXTC or DXT*n*.

Older, no longer recommended texture compression formats include:

- ETC1: Supported on most devices. This format has no transparency support, but games can use a second texture file for the alpha component.
- PVRTC: Popular with iOS games, and also supported on some Android devices.

ETC1 support is only a requirement for games supporting very old legacy
devices or select Android TV devices which don't support OpenGL ES 3.0 and
higher.

### A default format

With so many available formats (with varying levels of device support), you
may not know which formats to use when building your game textures. As a
safeguard, the app bundle format lets you select a default texture compression
format for each asset pack. If a device does not support the other specified
formats, assets using this default format are installed.

Unless you are targeting very old device hardware, ETC2 is a good choice
for a default format. You should use the ETC2 formats that are guaranteed to be
[supported in OpenGL ES 3.0](https://en.wikipedia.org/wiki/Ericsson_Texture_Compression).
These formats are also available in the Vulkan graphics API.
| **Note:** Some game engines transcode the textures in memory if the format is not supported on the device. For example, consider a game bundled with ETC2 as the default format and no ETC1 support. Devices that support only ETC1 are still be able to run the game, but with slower loading times and performance. Refer to your game engine's documentation to verify if this transcoding is done and if it is acceptable for your use case. As an example, Unity decompresses the texture at runtime to a fallback format for older devices that don't support it. For more information, see the [Unity documentation](https://docs.unity3d.com/2020.2/Documentation/Manual/class-TextureImporterOverride.html#notes-on-android).

### Recommended formats

The ASTC format defines a variety of compression block sizes, which allow
you to selectively trade reduced image quality for greater compression.
Depending on the nature of the source art material, for a given texture you may
choose a smaller or larger block size to maintain acceptable visual quality.

If your game supports Google Play Games for PC and uses Vulkan, you
should include S3TC textures. The S3TC formats are supported by
all desktop GPUs.

## Build an app bundle

Google Play uses Android App Bundles to generate and serve optimized APKs for
each user's device configuration, so users download only the code and resources
they need to run your game. These optimized APKs include a single set of texture
assets, formatted with the optimal compression format for the device.

If your game is not in Unity, [use Gradle](https://developer.android.com/guide/playcore/asset-delivery/texture-compression#use-gradle) to build an app bundle.
Advanced users may want to [use `bundletool`](https://developer.android.com/guide/playcore/asset-delivery/texture-compression#use-bundletool).

If your game is in Unity, support for app bundles with Play Asset Delivery
is available in Unity 2021.3 and higher. For more information, see the
[Unity documentation](https://docs.unity3d.com/2022.3/Documentation/Manual/play-asset-delivery.html).
You can [use a Unity plugin](https://developer.android.com/guide/playcore/asset-delivery/texture-compression#unity-plugin) to build an app bundle with lower
versions of Unity.

### Use Gradle

1. Update the version of the Android Gradle plugin in your project's
   `build.gradle` file to 4.1 or higher (for example,
   `com.android.tools.build:gradle:4.1.0`).

2. Determine the set of device types that you want to target for your game and
   the texture compression formats they support (for more information on
   formats, see [Background](https://developer.android.com/guide/playcore/asset-delivery/texture-compression#background)).

3. Build versions of your assets for each texture compression format from the
   previous step. This could involve generating sprite sheets using software
   like
   [TexturePacker](https://www.codeandweb.com/texturepacker), or
   running a script that converts raw assets into those with a specific format
   (for example,
   [astc-encoder](https://github.com/ARM-software/astc-encoder)).

4. Create [asset packs](https://developer.android.com/guide/playcore/asset-delivery) (see
   [Build for C++ or Java](https://developer.android.com/guide/playcore/asset-delivery/integrate-java)),
   which contain your game assets and are used by Play Asset Delivery. For
   example, you can create one asset pack per level or asset packs for
   different parts of your game.

   | **Note:** You don't need to use Play Asset Delivery APIs inside your game if you select the `install-time` delivery type for your asset packs. These asset packs are installed at the same time as the main application APK.
5. Inside your asset packs, add directories for each texture compression format
   that you want to support. Add [supported suffixes](https://developer.android.com/guide/playcore/asset-delivery/texture-compression#supported-suffixes) to
   the texture directory names that correspond to the texture compression
   format used for the contained files.

   Create a directory with no suffix in its name (for example,
   `common/src/main/assets/textures/`). In this directory, place the default
   format of your texture assets. This default format should be supported by
   most devices (for example, ETC1 or ETC2). If a device does not support the
   other specified formats (for example, PVRTC and ASTC in the table below),
   the Google Play Store installs this directory instead.
   | **Note:** You decide what content goes into this directory. In most cases, the files in this directory should be the same as in the other directories, differing only by the texture format. However, some formats may require additional support files. For example, textures in the ETC1 format may have an extra file to support alpha channel. Verify how your game or game engine loads textures to determine the optimal file organization.

   |                                 Directory before                                  |                                                                               Directory after                                                                                |
   |-----------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
   | `common` **asset pack** : common/build.gradle common/src/main/assets/textures/... | `common` **asset pack** : common/build.gradle common/src/main/assets/textures/... common/src/main/assets/textures#tcf_astc/... common/src/main/assets/textures#tcf_pvrtc/... |
   | `level1` **asset pack** : level1/build.gradle level1/src/main/assets/textures/... | `level1` **asset pack** : level1/build.gradle level1/src/main/assets/textures/... level1/src/main/assets/textures#tcf_astc/... level1/src/main/assets/textures#tcf_pvrtc/... |
   | `level2` **asset pack** : level2/build.gradle level2/src/main/assets/textures/... | `level2` **asset pack** : level2/build.gradle level2/src/main/assets/textures/... level2/src/main/assets/textures#tcf_astc/... level2/src/main/assets/textures#tcf_pvrtc/... |

6. Update your app's `build.gradle` file to **enable the splitting of your
   asset packs per textures**.

   ```groovy
   // In the app build.gradle file:
   android {
       ...
       bundle {
           texture {
               enableSplit true
           }
       }
   }
   ```
7. In Android Studio, select **Build \> Generate Signed Bundle / APK** , or
   launch the
   [Gradle task from the command line](https://developer.android.com/studio/build/building-cmdline) to
   generate your bundle.

   | **Note:** When APKs (to be installed on a device) are generated from the app bundle, the suffixes (for example, `#tcf_xxx`) are removed from the directory names. Your game only has to read files from a well-known directory name (for example, `level1/assets/textures`). Some game engines can detect the format of a file, so your game can be indifferent about which format of game assets are installed.

### Use the Google Play Unity plugin

[Get the Unity plugin (or package) for Play Asset Delivery](https://developer.android.com/guide/playcore#unity)
to create an app bundle with texture-targeted asset packs.

#### Prepare the assets

To prepare your texture assets for building an app bundle, do the following:

1. Package your scene and assets into multiple Unity
   [AssetBundles](https://docs.unity3d.com/Manual/AssetBundlesIntro.html).

   | **Note:** While the AssetBundle Manager is deprecated for Unity versions 2018.2 and higher, AssetBundles are still supported.
2. Determine the set of device types that you want to target for your game and
   the texture compression formats they support (for more information on
   formats, see [Background](https://developer.android.com/guide/playcore/asset-delivery/texture-compression#background)).

3. Modify your game's build script to generate the AssetBundles multiple
   times, once for each texture format that you want to support. See the
   following example script:

       using Google.Android.AppBundle.Editor;
       using UnityEditor;

       public class MyBundleBuilder
       {
          [MenuItem("Assets/Build AssetBundles TCF variants")]
          public static void BuildAssetBundles()
          {
              // Describe the AssetBundles to be built:
              var assetBundlesToBuild = new []
              {
                  new AssetBundleBuild
                  {
                      assetBundleName = "level1-textures",
                      assetNames = new[] {"level1/character-textures", "level1/background-textures"}
                  },
                  new AssetBundleBuild
                  {
                      assetBundleName = "level2-textures",
                      assetNames = new[] {"level2/character-textures", "level2/background-textures"}
                  }
              };

              // Describe where to output the asset bundles and in which formats:
              var outputPath = "Assets/AssetBundles";
              var defaultTextureFormat = MobileTextureSubtarget.ETC2;
              var additionalTextureFormats = new[] { MobileTextureSubtarget.ASTC, MobileTextureSubtarget.PVRTC }
              var allowClearDirectory = true;

              // Generate asset bundles:
              AssetBundleBuilder.BuildAssetBundles(
                  outputPath,
                  assetBundlesToBuild,
                  BuildAssetBundleOptions.UncompressedAssetBundle,
                  defaultTextureFormat,
                  additionalTextureFormats,
                  allowClearDirectory);

              // While in this example we're using the UI to configure the
              // AssetBundles, you can use the value returned by BuildAssetBundles
              // to configure the asset packs, if you want to build the bundle
              // entirely using the scripting API.
          }
       }

4. Verify that each texture asset is output in a directory with the correct
   suffix in its name (for example, `#tcf_astc`).

   Verify that a directory with no suffix in its name is output (for example,
   `Assets/AssetBundles/`). This directory contains the default format of your
   texture assets. This default format should be supported by most devices (for
   example, ETC2). If a device does not support the other specified formats
   (for example, ASTC in the code from the previous step), then the Google Play
   Store installs this directory instead.  

       Assets/AssetBundles.meta
       Assets/AssetBundles/AssetBundles
       Assets/AssetBundles/AssetBundles.manifest
       Assets/AssetBundles/AssetBundles.manifest.meta
       Assets/AssetBundles/AssetBundles.meta
       Assets/AssetBundles/samplescene
       Assets/AssetBundles/samplescene.manifest
       Assets/AssetBundles/samplescene.manifest.meta
       Assets/AssetBundles/samplescene.meta
       Assets/AssetBundles/texturesbundle
       Assets/AssetBundles/texturesbundle.manifest
       Assets/AssetBundles/texturesbundle.manifest.meta
       Assets/AssetBundles/texturesbundle.meta
       Assets/AssetBundles#tcf_astc.meta
       Assets/AssetBundles#tcf_astc/AssetBundles
       Assets/AssetBundles#tcf_astc/AssetBundles.manifest
       Assets/AssetBundles#tcf_astc/AssetBundles.manifest.meta
       Assets/AssetBundles#tcf_astc/AssetBundles.meta
       Assets/AssetBundles#tcf_astc/samplescene
       Assets/AssetBundles#tcf_astc/samplescene.manifest
       Assets/AssetBundles#tcf_astc/samplescene.manifest.meta
       Assets/AssetBundles#tcf_astc/samplescene.meta
       Assets/AssetBundles#tcf_astc/texturesbundle
       Assets/AssetBundles#tcf_astc/texturesbundle.manifest
       Assets/AssetBundles#tcf_astc/texturesbundle.manifest.meta
       Assets/AssetBundles#tcf_astc/texturesbundle.meta

5. Select **Google \> Android \> Assets Delivery**.

6. Click **Add Folder** to add the folder containing your default asset
   bundles. These bundles are installed on devices that don't support the other
   formats you define.

   Make sure to set the **Delivery mode** for the AssetBundle.

   ![Unity AssetBundle Delivery default format](https://developer.android.com/static/images/app-bundle/unity-asset-bundle-config.svg)
7. Click **Add Folder** to add a folder containing AssetBundles built for
   another format (for example, ASTC). Repeat as needed.

   Make sure to set the **Delivery mode** for each AssetBundle.

   ![Unity AssetBundle Delivery ASTC format](https://developer.android.com/static/images/app-bundle/unity-asset-bundle-config-2.svg)

#### Build

Select **Google \> Build Android App Bundle** to launch the Unity build of your
game. It also packages the AssetBundles into multiple asset packs where each
AssetBundle name is converted to a single asset pack.

### (Advanced) Use bundletool

For more information on `bundletool`, see
[Build an app bundle using bundletool](https://developer.android.com/studio/build/building-cmdline#bundletool-build).

To create the app bundle, do the following:

1. Download [`bundletool`](https://github.com/google/bundletool/releases)
   from its GitHub repository.

2. Determine the set of device types that you want to target for your game and
   the texture compression formats they support (for more information on
   formats, see [Background](https://developer.android.com/guide/playcore/asset-delivery/texture-compression#background)).

3. Build versions of your assets for each texture compression format from the
   previous step. This could involve generating sprite sheets using software
   like
   [TexturePacker](https://www.codeandweb.com/texturepacker), or
   running a script that converts raw assets into those with a specific format
   (for example,
   [astc-encoder](https://github.com/ARM-software/astc-encoder)).

4. Create [asset packs](https://developer.android.com/guide/playcore/asset-delivery) (see
   [Build for C++ or Java](https://developer.android.com/guide/playcore/asset-delivery/integrate-java)),
   which contain your game assets and are used by Play Asset Delivery. For
   example, you can create one asset pack per level or asset packs for
   different parts of your game.

   | **Note:** You don't need to use Play Asset Delivery APIs inside your game if you select the `install-time` delivery type for your asset packs. These asset packs are installed at the same time as the main application APK.
5. In your different asset packs, add [supported suffixes](https://developer.android.com/guide/playcore/asset-delivery/texture-compression#supported-suffixes)
   to the texture directory names that correspond to the texture compression
   format used for the contained files.

   Create a directory with no suffix in its name (for example,
   `common/src/main/assets/textures/`). In this directory, place the default
   format of your texture assets. This default format should be supported by
   most devices (for example, ETC1 or ETC2). If a device does not support the
   other specified formats (for example, PVRTC and ASTC in the table below),
   the Google Play Store installs this directory instead.
   | **Note:** You decide what content goes into this directory. In most cases, the files in this directory should be the same as in the other directories, differing only by the texture format. However, some formats may require additional support files. For example, textures in the ETC1 format may have an extra file to support alpha channel. Verify how your game or game engine loads textures to determine the optimal file organization.

   |                                 Directory before                                  |                                                                               Directory after                                                                                |
   |-----------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
   | `common` **asset pack** : common/build.gradle common/src/main/assets/textures/... | `common` **asset pack** : common/build.gradle common/src/main/assets/textures/... common/src/main/assets/textures#tcf_astc/... common/src/main/assets/textures#tcf_pvrtc/... |
   | `level1` **asset pack** : level1/build.gradle level1/src/main/assets/textures/... | `level1` **asset pack** : level1/build.gradle level1/src/main/assets/textures/... level1/src/main/assets/textures#tcf_astc/... level1/src/main/assets/textures#tcf_pvrtc/... |
   | `level2` **asset pack** : level2/build.gradle level2/src/main/assets/textures/... | `level2` **asset pack** : level2/build.gradle level2/src/main/assets/textures/... level2/src/main/assets/textures#tcf_astc/... level2/src/main/assets/textures#tcf_pvrtc/... |

6. Add the TCF dimension to the
   [app bundle metadata file](https://developer.android.com/studio/build/building-cmdline#bundleconfig)
   (`BundleConfig.json`). Use `TEXTURE_COMPRESSION_FORMAT` for the `value`
   field:

   ```json
   {
     ...
     "optimizations": {
       "splitsConfig": {
         "splitDimension": [
         ...
         {
            "value": "TEXTURE_COMPRESSION_FORMAT",
            "negate": false,
            "suffixStripping": {
              "enabled": true,
              "defaultSuffix": ""
             }
         }],
       }
     }
   }
   ```

   Set `suffixStripping.enabled` to `true` to remove the suffix (for example,
   `#tcf_astc`) from the directory names when generating the asset packs. This
   enables your game to read files from a well-known directory name (such as
   `level1/assets/textures`). Some game engines can detect the format of a
   file, so your game can be indifferent about the format of texture assets that
   it was installed with.

   `suffixStripping.defaultSuffix` specifies the default directory suffix when
   `bundletool` generates a standalone APK for devices running Android 5.0 (API
   level 21) and lower. In the example table earlier, the default version of
   the texture assets is installed on these devices; this is the intended
   behavior in most cases.
7. Build the app bundle:

       bundletool build-bundle --config=<var translate="no">BUILD_CONFIG</var>.json \
         --modules=<var translate="no">level1</var>.zip,<var translate="no">level2</var>.zip,<var translate="no">common</var>.zip,<var translate="no">base</var>.zip --output=<var translate="no">MY_BUNDLE</var>.aab

## Verify the contents of the app bundle

If you haven't already,
[download `bundletool`](https://github.com/google/bundletool/releases)
from the GitHub repository.

Verify the contents of the output app bundle by building APKs from it and
inspecting them:  

    bundletool build-apks --output=<var translate="no">APKS</var>.apks --bundle=<var translate="no">MY_BUNDLE</var>.aab
    zipinfo <var translate="no">APKS</var>.apks

The output should be similar to the following:  

    toc.pb
    splits/base-master.apk
    splits/base-armeabi_v7a.apk
    splits/...
    asset-slices/level1-astc.apk
    asset-slices/level1-other_tcf.apk
    asset-slices/level1-pvrtc.apk

These names indicate that the TCF targeting is properly applied. If you extract
the contents of a level APK (for example, `asset-slices/level1-astc.apk`), you
can verify that *only one* directory named `textures` is present.

## Test the app bundle

Connect a device and install the applicable asset packs:  

    bundletool install-apks --apks=<var translate="no">APKS</var>.apks

This command installs only the asset packs that meet the device's specification.
These specifications include ABI, screen density, language, and the most
applicable texture compression format. This operation simulates what is done by
the Google Play Store for your published game.

To verify that the correct asset packs were installed, do any of the following:

- Use the `bundletool extract-apks` command to output the apks installed for
  your device into a directory and then inspect this directory.

  1. Extract the specification of your device:

         bundletool get-device-spec --output=<var translate="no">MY_DEVICE_SPEC</var>.json

  2. Run `bundletool extract-apks` with this device specification:

         bundletool extract-apks --apks=<var translate="no">APKS</var>.apks --device-spec=<var translate="no">MY_DEVICE_SPEC</var>.json \
             --output-dir out

  3. List the files in the `out` directory and verify that the proper asset packs
     are installed. Asset pack names are suffixed by the texture format name (for
     example, `level1-astc.apk`).

- Add log statements in your game that output the texture format when loading
  a texture.

- Generate a test set of textures (for example, replace a texture with a
  single bright color for a given format). Run the game and verify that it is
  present.

If your app contains `on-demand` or `fast-follow` asset packs, use the
[local testing solution for asset delivery](https://developer.android.com/guide/playcore/asset-delivery/test).

## Supported suffixes for texture directory names

Google Play understands the following suffixes used in texture directory names:

- `#tcf_astc` for Adaptive Scalable Texture Compression (ASTC)
- `#tcf_atc` for ATI texture compression (ATC)
- `#tcf_dxt1` for S3 DXT1 texture compression (DXT1)
- `#tcf_latc` for Luminance-Alpha texture compression (LATC)
- `#tcf_paletted` for generic paletted texture compression
- `#tcf_pvrtc` for PowerVR texture compression (PVRTC)
- `#tcf_etc1` for Ericsson texture compression (ETC1)
- `#tcf_etc2` for Ericsson texture compression 2 (ETC2)
- `#tcf_s3tc` for S3 texture compression (S3TC)
- `#tcf_3dc` for ATI 3Dc texture compression (3Dc)

## Google Play serving rules

Google Play inspects the OpenGL extension strings used by the device and the
OpenGL version supported by the device. Google Play uses this information to
determine the correct texture format to deliver to the device from the Android
App Bundle.

Google Play delivers the **first format**, in the order listed in the following
table, that is supported by the device.

If none of the texture formats in the App Bundle are supported by the device,
Google Play delivers the texture formats packaged in the **default format** .
(Unless you are targeting specific device hardware, ETC1 or ETC2 are good
choices for a default format.) For information on how to package assets in the
default format, see [Use bundletool](https://developer.android.com/guide/playcore/asset-delivery/texture-compression#use-bundletool) or
[Use the Google Play Unity plugin](https://developer.android.com/guide/playcore/asset-delivery/texture-compression#unity-plugin).

If assets have not been packaged in a default format, Google Play marks the app
as not available for the device. In this case, users cannot download the app.

| Format (designated in `tcf_xxxx`) |            Supported on devices with OpenGL extension string            |
|-----------------------------------|-------------------------------------------------------------------------|
| astc                              | `GL_KHR_texture_compression_astc_ldr`                                   |
| pvrtc                             | `GL_IMG_texture_compression_pvrtc`                                      |
| s3tc                              | `GL_EXT_texture_compression_s3tc`                                       |
| dxt1                              | `GL_EXT_texture_compression_dxt1`                                       |
| latc                              | `GL_EXT_texture_compression_latc`                                       |
| atc                               | `GL_AMD_compressed_ATC_texture`                                         |
| 3dc                               | `GL_AMD_compressed_3DC_texture`                                         |
| etc2                              | Not applicable. The device must support OpenGL ES version 3.0 or later. |
| etc1                              | `GL_OES_compressed_ETC1_RGB8_texture`                                   |
| paletted                          | `GL_OES_compressed_paletted_texture`                                    |