---
title: https://developer.android.com/google/play/nested-targeting
url: https://developer.android.com/google/play/nested-targeting
source: md.txt
---

# Asset Targeting by Several Dimensions (Nested Targeting)

| **Warning:** Access to the information on this page is governed by a Google non-disclosure agreement.
| **Note:** This document assumes familiarity with targeting by a single dimension. You may want to read the documentation about[texture compression format targeting](https://developer.android.com/guide/playcore/asset-delivery/texture-compression),[country targeting](https://developer.android.com/google/play/asset-country-targeting)and[device tier targeting](https://developer.android.com/google/play/device-tier-targeting)first.

To target a folder in an asset pack or bundle module by several dimensions (texture compression format, device tier, country set), you can use nested targeting.

Nested targeting allows to define targeting criteria that combine up to 2 targeting dimensions.

## Format

To target a folder by multiple dimensions, specify the list of dimensions in a series of hashtag suffixes to the folder name.

For instance, to target an asset folder by texture compression format ASTC and device tier 2, the targeting would look like:  

    ...
    .../level1/src/main/assets/character-textures#tcf_astc#tier_2/
    ...

If you are using Gradle to build your app, targeting suffixes are stripped from the directory name in the final APKs or asset packs that are delivered to user devices.

If you are using bundletool directly, specify whether you want the suffix stripped for each of the dimensions individually in`BundleConfig.json`. With an example for device tier targeting:  

    {
      ...
      "optimizations": {
        "splitsConfig": {
          "splitDimension": [
          ...
          {
            "value": "DEVICE_TIER",
            "negate": false,
            "suffixStripping": {
              "enabled": true,
          }],
        }
      }
    }

Nested targeting is supported in bundletool 1.14.1 or higher, and Android Gradle Plugin 8.2.0-alpha01 or higher, which requires Gradle 8.1 or higher.

You can find more information on how to customize your configuration for individual dimensions in the documentation for each targeting dimension.

## Limitations

- You can use at most 2 nested dimensions. In other words, you cannot have a folder targeted by device tier, texture compression format and country set at the same time: you have to pick 2.

- You should specify the 2 nested dimensions at the same level of the folder path. For instance, the following folder targeting is forbidden, since #tcf_astc and #tier_2 appear in different path segments:

    .../level1/src/main/assets/character-textures#tcf_astc/level1#tier_2/

- Your nested dimensions must be the same across your whole bundle. For instance, you cannot have an asset pack where you nest device tiers and country set, and another asset pack where you nest country set and texture compression format.

- The values you use for the 2 dimensions need to be the same across the whole bundle and you must specify the complete combination of values. For instance, if you want to nest texture compression format and country set, and you have 4 TCFs (ASTC, ETC2, PVRTC, default fallback) and 3 country sets (latam, sea, default fallback), you must specify a folder for all 12 combinations:

    level1/textures#countries_latam#tcf_astc/...
    level1/textures#countries_latam#tcf_etc2/...
    level1/textures#countries_latam#tcf_pvrtc/...
    level1/textures#countries_latam/...
    level1/textures#countries_sea#tcf_astc/...
    level1/textures#countries_sea#tcf_etc2/...
    level1/textures#countries_sea#tcf_pvrtc/...
    level1/textures#countries_sea/...
    level1/textures#tcf_astc/...
    level1/textures#tcf_etc2/...
    level1/textures#tcf_pvrtc/...
    level1/textures/...

| **Note:** remember that`#tier_0`is the default fallback for device tier targeting. On the other hand, the fallback folder for texture compression format targeting and country set targeting is a folder without any targeting suffix, like in the example above.
| **Note:** this may result in duplication of assets in the bundle, but it doesn't cause duplication on user devices, since only one folder is served to each device.

- You are allowed to use both nested targeting and single-dimension targeting on distinct content folders in the same asset pack or bundle module. If you use a dimension both in single-dimension targeting and nested targeting, the set of values you use must be always the same ones. For instance, you cannot target by 4 tiers in single-dimension device tier targeting, and then use only 3 tiers when nested with country sets or TCFs.