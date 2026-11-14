---
title: https://developer.android.com/guide/playcore/asset-delivery/integrate-unity
url: https://developer.android.com/guide/playcore/asset-delivery/integrate-unity
source: md.txt
---

> Documentation index: https://developer.android.com/guide/playcore/asset-delivery/llms.txt

When integrating asset delivery, Unity games
can access asset packs using Addressables or AssetBundles. Addressables are the
more recent and recommended asset delivery solution for games built with Unity
2019.4 or higher, while AssetBundles provide support of asset packs in Unity
2017.4 and 2018.4.

## Unity Addressables

Games built with Unity 2019.4 or higher should use
[Addressables](https://unity.com/how-to/simplify-your-content-management-addressables#where-can-i-learn-more-about-addressables)
for asset delivery on Android. Unity provides a Play Asset Delivery (PAD) API
for handling Android asset packs using Addressables. For information about using
Addressables, see the following:

- [Addressables for Android package](https://docs.unity3d.com/Packages/com.unity.addressables.android@1.0/manual/index.html)
- [PAD guide for Unity](https://docs.unity3d.com/Manual/play-asset-delivery.html)
- PAD API for Unity [reference documentation](https://docs.unity3d.com/ScriptReference/Android.AndroidAssetPacks.html)

## Use AssetBundle files

Games built with Unity 2017.4 and 2018.4 can use AssetBundle files for asset
delivery on Android. Unity
[AssetBundle](https://docs.unity3d.com/Manual/AssetBundlesIntro.html)
files contain serialized assets that can be loaded by the Unity engine while the
app is running. These files are platform-specific (for example, built for
Android) and can be used in combination with asset packs. Most commonly,
one AssetBundle file is packaged into a single asset pack, with the pack
using the same name as the AssetBundle. If you want more flexibility in
creating an asset pack, configure the asset pack [using the API](https://developer.android.com/guide/playcore/asset-delivery/integrate-unity.md.txt#configure-asset-packs-api).

At runtime, use the [Play Asset Delivery for Unity](https://developer.android.com/reference/unity/class/Google/Play/AssetDelivery/PlayAssetDelivery.md.txt)
class to retrieve an AssetBundle packaged in an asset pack.

### Prerequisites

1. Set up your development environment:

### OpenUPM-CLI

If you have the [OpenUPM CLI](https://github.com/openupm/openupm-cli#installation)
installed you can install the OpenUPM registry with the following command:

```bash
openupm add com.google.play.assetdelivery
```

### OpenUPM

1. Open the [package manager settings](https://docs.unity3d.com/Manual/class-PackageManager.html)
   by selecting the Unity menu option
   **Edit \> Project Settings \> Package Manager**.

2. Add OpenUPM as a scoped registry to the Package Manager window:

       Name: package.openupm.com
       URL: https://package.openupm.com
       Scopes: com.google.external-dependency-manager
         com.google.play.common
         com.google.play.core
         com.google.play.assetdelivery
         com.google.android.appbundle

3. Open the [package manager menu](https://docs.unity3d.com/Manual/upm-ui-install.html) by selecting the Unity
   menu option **Window \> Package Manager**.

4. Set the manager scope drop-down to select **My Registries**.

5. Select the **Google Play Integrity plugin for Unity** package from the
   package list and press **Install**.

### Import from GitHub

1. Download the latest [`.unitypackage`](https://github.com/google/play-asset-delivery-unity/releases/latest)
   release from GitHub.

2. Import the `.unitypackage` file by selecting the Unity menu option
   **Assets \> Import package \> Custom Package** and importing all items.

> [!NOTE]
> **Note:** By downloading and using Google Play Unity Plugins, you agree to the [Play Core Software Development Kit Terms of Service](https://developer.android.com/guide/playcore.md.txt#license).

1. [Create AssetBundles in Unity](https://docs.unity3d.com/Manual/AssetBundles-Workflow.html).

   > [!NOTE]
   > **Note:** You can use the [Unity AssetBundle Browser](https://docs.unity3d.com/Packages/com.unity.assetbundlebrowser@1.7/manual/index.html) to create and manage AssetBundles in your Unity project.

### Configure AssetBundles using the UI

1. Configure each AssetBundle in an asset pack:

   1. Select **Google \> Android App Bundle \> Asset Delivery Settings**.
   2. To select folders that directly contain AssetBundle files, click **Add
      Folder**.

   ![Asset Delivery Settings Add Folder button in Unity](https://developer.android.com/static/images/app-bundle/unity-add-assetbundle-folder.png)
2. For each bundle, change the **Delivery Mode** to **Install Time** , **Fast
   Follow** , or **On Demand**. Resolve any errors or dependencies and close the
   window.

   ![Asset Delivery delivery mode selector per bundle in Unity](https://developer.android.com/static/images/app-bundle/unity-asset-delivery-method-per-bundle.png)
3. Select **Google \> Build Android App Bundle** to build the app bundle.

4. (Optional) Configure your app bundle to support different [texture
   compression formats](https://developer.android.com/guide/playcore/asset-delivery/texture-compression).

### Configure asset packs using the API

You can configure asset delivery through editor scripts which can be run as part
of an automated build system.

Use the
[`AssetPackConfig`](https://developer.android.com/reference/unity/class/Google/Android/AppBundle/Editor/AssetPackConfig.md.txt)
class to define which assets to include in an Android App Bundle build, as well
as the delivery mode of the assets. These asset packs don't need to contain
an AssetBundle.

```c#
public void ConfigureAssetPacks {
   // Creates an AssetPackConfig with a single asset pack, named
   // examplePackName, containing all the files in path/to/exampleFolder.
   var assetPackConfig = new AssetPackConfig();
   assetPackConfig.AddAssetsFolder("examplePackName",
                                   "path/to/exampleFolder",
                                   AssetPackDeliveryMode.OnDemand);

   // Configures the build system to use the newly created assetPackConfig when
   // calling Google > Build and Run or Google > Build Android App Bundle.
   AssetPackConfigSerializer.SaveConfig(assetPackConfig);

   // Alternatively, use BundleTool.BuildBundle to build an App Bundle from script.
   BuildBundle(new buildPlayerOptions(), assetPackConfig);
}
```

You can also use the static
[`BuildBundle`](https://developer.android.com/reference/unity/class/Google/Android/AppBundle/Editor/Bundletool.md.txt#classGoogle_1_1Android_1_1AppBundle_1_1Editor_1_1Bundletool_1a419f1884fceff86fad1175c0546b85e8)
method in the `Bundletool` class to generate an Android App Bundle with asset
packs, given
[BuildPlayerOptions](https://docs.unity3d.com/ScriptReference/BuildPlayerOptions.html)
and
[`AssetPackConfig`](https://developer.android.com/reference/unity/class/Google/Android/AppBundle/Editor/AssetPackConfig.md.txt).

For a guided tutorial, see the
[Using Play Asset Delivery in Unity games Codelab](https://codelabs.developers.google.com/codelabs/unity-gamepad).

### Integrate with Play Asset Delivery Unity API

The
[Play Asset Delivery Unity API](https://developer.android.com/reference/unity/class/Google/Play/AssetDelivery/PlayAssetDelivery.md.txt)
provides the functionality for requesting asset packs, managing downloads, and
accessing the assets. Make sure to [Add the Unity plugin](https://developer.android.com/guide/playcore/asset-delivery/integrate-unity.md.txt#prerequisites) into your project
first.

The functions you use in the API depend on how you created
the asset packs.

If you
[created asset packs using the plugin UI](https://developer.android.com/guide/playcore/asset-delivery/integrate-unity.md.txt#configure-assetbundles-ui),
select **Plugin-configured asset packs**.

If you
[created asset packs using the API (or plugin UI)](https://developer.android.com/guide/playcore/asset-delivery/integrate-unity.md.txt#configure-asset-packs-api),
select **API-configured asset packs**.
<button value="plugin" default="">Plugin-configured asset packs</button> <button value="api">API-configured asset packs</button>

## Next steps

[Test asset delivery](https://developer.android.com/guide/playcore/asset-delivery/test.md.txt) locally and from
Google Play.