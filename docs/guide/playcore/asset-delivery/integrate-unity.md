---
title: https://developer.android.com/guide/playcore/asset-delivery/integrate-unity
url: https://developer.android.com/guide/playcore/asset-delivery/integrate-unity
source: md.txt
---

# Integrate asset delivery (Unity)

When integrating asset delivery, Unity games can access asset packs using Addressables or AssetBundles. Addressables are the more recent and recommended asset delivery solution for games built with Unity 2019.4 or higher, while AssetBundles provide support of asset packs in Unity 2017.4 and 2018.4.

## Unity Addressables

Games built with Unity 2019.4 or higher should use[Addressables](https://unity.com/how-to/simplify-your-content-management-addressables#where-can-i-learn-more-about-addressables)for asset delivery on Android. Unity provides a Play Asset Delivery (PAD) API for handling Android asset packs using Addressables. For information about using Addressables, see the following:

- [Addressables for Android package](https://docs.unity3d.com/Packages/com.unity.addressables.android@1.0/manual/index.html)
- [PAD guide for Unity](https://docs.unity3d.com/Manual/play-asset-delivery.html)
- PAD API for Unity[reference documentation](https://docs.unity3d.com/ScriptReference/Android.AndroidAssetPacks.html)

## Use AssetBundle files

Games built with Unity 2017.4 and 2018.4 can use AssetBundle files for asset delivery on Android. Unity[AssetBundle](https://docs.unity3d.com/Manual/AssetBundlesIntro.html)files contain serialized assets that can be loaded by the Unity engine while the app is running. These files are platform-specific (for example, built for Android) and can be used in combination with asset packs. Most commonly, one AssetBundle file is packaged into a single asset pack, with the pack using the same name as the AssetBundle. If you want more flexibility in creating an asset pack, configure the asset pack[using the API](https://developer.android.com/guide/playcore/asset-delivery/integrate-unity#configure-asset-packs-api).

At runtime, use the[Play Asset Delivery for Unity](https://developer.android.com/reference/unity/class/Google/Play/AssetDelivery/PlayAssetDelivery)class to retrieve an AssetBundle packaged in an asset pack.

### Prerequisites

1. Set up your development environment:

### OpenUPM-CLI

If you have the[OpenUPM CLI](https://github.com/openupm/openupm-cli#installation)installed you can install the OpenUPM registry with the following command:  

    openupm add com.google.play.assetdelivery

### OpenUPM

1. Open the[package manager settings](https://docs.unity3d.com/Manual/class-PackageManager.html)by selecting the Unity menu option**Edit \> Project Settings \> Package Manager**.

2. Add OpenUPM as a scoped registry to the Package Manager window:

       Name: package.openupm.com
       URL: https://package.openupm.com
       Scopes: com.google.external-dependency-manager
         com.google.play.common
         com.google.play.core
         com.google.play.assetdelivery
         com.google.android.appbundle

3. Open the[package manager menu](https://docs.unity3d.com/Manual/upm-ui-install.html)by selecting the Unity menu option**Window \> Package Manager**.

4. Set the manager scope drop-down to select**My Registries**.

5. Select the**Google Play Integrity plugin for Unity** package from the package list and press**Install**.

### Import from GitHub

1. Download the latest[`.unitypackage`](https://github.com/google/play-asset-delivery-unity/releases/latest)release from GitHub.

2. Import the`.unitypackage`file by selecting the Unity menu option**Assets \> Import package \> Custom Package**and importing all items.

| **Note:** By downloading and using Google Play Unity Plugins, you agree to the[Play Core Software Development Kit Terms of Service](https://developer.android.com/guide/playcore#license).

1. [Create AssetBundles in Unity](https://docs.unity3d.com/Manual/AssetBundles-Workflow.html).

   | **Note:** You can use the[Unity AssetBundle Browser](https://docs.unity3d.com/Manual/AssetBundles-Browser.html)to create and manage AssetBundles in your Unity project.

### Configure AssetBundles using the UI

1. Configure each AssetBundle in an asset pack:

   1. Select**Google \> Android App Bundle \> Asset Delivery Settings**.
   2. To select folders that directly contain AssetBundle files, click**Add Folder**.

   ![](https://developer.android.com/static/images/app-bundle/unity-add-assetbundle-folder.png)
2. For each bundle, change the**Delivery Mode** to**Install Time** ,**Fast Follow** , or**On Demand**. Resolve any errors or dependencies and close the window.

   ![](https://developer.android.com/static/images/app-bundle/unity-asset-delivery-method-per-bundle.png)
3. Select**Google \> Build Android App Bundle**to build the app bundle.

4. (Optional) Configure your app bundle to support different[texture compression formats](https://developer.android.com/guide/playcore/asset-delivery/texture-compression).

### Configure asset packs using the API

You can configure asset delivery through editor scripts which can be run as part of an automated build system.

Use the[`AssetPackConfig`](https://developer.android.com/reference/unity/class/Google/Android/AppBundle/Editor/AssetPackConfig)class to define which assets to include in an Android App Bundle build, as well as the delivery mode of the assets. These asset packs do not need to contain an AssetBundle.  

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

You can also use the static[`BuildBundle`](https://developer.android.com/reference/unity/class/Google/Android/AppBundle/Editor/Bundletool#classGoogle_1_1Android_1_1AppBundle_1_1Editor_1_1Bundletool_1a419f1884fceff86fad1175c0546b85e8)method in the`Bundletool`class to generate an Android App Bundle with asset packs, given[BuildPlayerOptions](https://docs.unity3d.com/ScriptReference/BuildPlayerOptions.html)and[`AssetPackConfig`](https://developer.android.com/reference/unity/class/Google/Android/AppBundle/Editor/AssetPackConfig).

For a guided tutorial, see the[Using Play Asset Delivery in Unity games Codelab](https://codelabs.developers.google.com/codelabs/unity-gamepad).

### Integrate with Play Asset Delivery Unity API

The[Play Asset Delivery Unity API](https://developer.android.com/reference/unity/class/Google/Play/AssetDelivery/PlayAssetDelivery)provides the functionality for requesting asset packs, managing downloads, and accessing the assets. Make sure to[Add the Unity plugin](https://developer.android.com/guide/playcore#unity)into your project first.

The functions you use in the API depend on how you created the asset packs.

If you[created asset packs using the plugin UI](https://developer.android.com/guide/playcore/asset-delivery/integrate-unity#configure-assetbundles-ui), select**Plugin-configured asset packs**.

If you[created asset packs using the API (or plugin UI)](https://developer.android.com/guide/playcore/asset-delivery/integrate-unity#configure-asset-packs-api), select**API-configured asset packs**.  
Plugin-configured asset packsAPI-configured asset packs

You implement the API according to the delivery type of the asset pack you wish to access. These steps are shown in the following flowchart.

![Asset pack flow diagram for the plugin](https://developer.android.com/static/images/app-bundle/asset-pack-flow-unity-plugin.png)

**Figure 1.**Flow diagram for accessing asset packs

<br />

## Retrieve AssetBundles

Import the[Play Asset Delivery library](https://developer.android.com/reference/unity/class/Google/Play/AssetDelivery/PlayAssetDelivery)and call the[`RetrieveAssetBundleAsync()`](https://developer.android.com/reference/unity/class/Google/Play/AssetDelivery/PlayAssetDelivery#retrieveassetbundleasync)method to retrieve an AssetBundle.  

```c#
using Google.Play.AssetDelivery;

// Loads the AssetBundle from disk, downloading the asset pack containing it if necessary.
PlayAssetBundleRequest bundleRequest = PlayAssetDelivery.RetrieveAssetBundleAsync(asset-bundle-name);
```

## Install-time delivery

Asset packs configured as`install-time`are immediately available at app launch. You can use the following to load a scene from the AssetBundle:  

```c#
AssetBundle assetBundle = bundleRequest.AssetBundle;

// You may choose to load scenes from the AssetBundle. For example:
string[] scenePaths = assetBundle.GetAllScenePaths();
SceneManager.LoadScene(scenePaths[path-index]);
```

## Fast-follow and on-demand delivery

These sections apply to`fast-follow`and`on-demand`asset packs.

### Check status

Each asset pack is stored in a separate folder in the app's internal storage. Use the[`isDownloaded()`](https://developer.android.com/reference/unity/class/Google/Play/AssetDelivery/PlayAssetDelivery#isdownloaded)method to determine if an asset pack has already been downloaded.

### Monitor the download

Query the[`PlayAssetBundleRequest`](https://developer.android.com/reference/unity/class/Google/Play/AssetDelivery/PlayAssetBundleRequest)object to monitor the status of the request:  

```c#
// Download progress of request, between 0.0f and 1.0f. The value will always be
// 1.0 for assets delivered as install-time.
// NOTE: A value of 1.0 will only signify the download is complete. It will still need to be loaded.
float progress = bundleRequest.DownloadProgress;

// Returns true if:
//   * it had either completed the download, installing, and loading of the AssetBundle,
//   * OR if it has encountered an error.
bool done = bundleRequest.IsDone;

// Returns status of retrieval request.
AssetDeliveryStatus status = bundleRequest.Status;
switch(status) {
    case AssetDeliveryStatus.Pending:
        // Asset pack download is pending - N/A for install-time assets.
    case AssetDeliveryStatus.Retrieving:
        // Asset pack is being downloaded and transferred to app storage.
        // N/A for install-time assets.
    case AssetDeliveryStatus.Available:
        // Asset pack is downloaded on disk but NOT loaded into memory.
        // For PlayAssetPackRequest(), this indicates that the request is complete.
    case AssetDeliveryStatus.Loading:
        // Asset pack is being loaded.
    case AssetDeliveryStatus.Loaded:
        // Asset pack has finished loading, assets can now be loaded.
        // For PlayAssetBundleRequest(), this indicates that the request is complete.
    case AssetDeliveryStatus.Failed:
        // Asset pack retrieval has failed.
    case AssetDeliveryStatus.WaitingForWifi:
        // Asset pack retrieval paused until either the device connects via Wi-Fi,
        // or the user accepts the PlayAssetDelivery.ShowConfirmationDialog dialog.
    case AssetDeliveryStatus.RequiresUserConfirmation:
        // Asset pack retrieval paused until the user accepts the
        // PlayAssetDelivery.ShowConfirmationDialog dialog.
    default:
        break;
}
```

#### Large downloads

Asset packs larger than 200MB can download automatically, but only on Wi-Fi. If the user is not on Wi-Fi, the`PlayAssetBundleRequest`status is set to[`AssetDeliveryStatus.WaitingForWifi`](https://developer.android.com/reference/unity/namespace/Google/Play/AssetDelivery#assetdeliverystatus)and the download is paused. In this case, either wait until the device connects to Wi-Fi, resuming the download, or prompt the user for approval to download the pack over a cellular connection.

#### Required user confirmation

If a pack has the`AssetDeliveryStatus.RequiresUserConfirmation`status, the download won't proceed until the user accepts the dialog that is shown with`PlayAssetDelivery.ShowConfirmationDialog()`. This status can arise if the app is not recognized by Play. Note that calling`PlayAssetDelivery.ShowConfirmationDialog()`in this case causes the app to be updated. After the update, request the assets again.  

```c#
if(request.Status == AssetDeliveryStatus.RequiresUserConfirmation
   || request.Status == AssetDeliveryStatus.WaitingForWifi) {
    var userConfirmationOperation = PlayAssetDelivery.ShowConfirmationDialog();
    yield return userConfirmationOperation;

    switch(userConfirmationOperation.GetResult()) {
        case ConfirmationDialogResult.Unknown:
            // userConfirmationOperation finished with an error. Something went
            // wrong when displaying the prompt to the user, and they weren't
            // able to interact with the dialog.
        case ConfirmationDialogResult.Accepted:
            // User accepted the confirmation dialog--an update will start.
        case ConfirmationDialogResult.Declined:
            // User canceled or declined the dialog. It can be shown again.
        default:
            break;
    }
}
```

#### Cancel a request (on-demand only)

If you need to cancel the request before the AssetBundles are loaded into memory, call the[`AttemptCancel()`](https://developer.android.com/reference/unity/play/class/Google/Play/AssetDelivery/PlayAssetBundleRequest#classGoogle_1_1Play_1_1AssetDelivery_1_1PlayAssetBundleRequest_1a352bfe7cdff7d41c9039b1b54f1f61ad)method on the[`PlayAssetBundleRequest`](https://developer.android.com/reference/unity/class/Google/Play/AssetDelivery/PlayAssetBundleRequest)object:  

```c#
// Will only attempt if the status is Pending, Retrieving, or Available - otherwise
// it will be a no-op.
bundleRequest.AttemptCancel();

// Check to see if the request was successful by checking if the error code is Canceled.
if(bundleRequest.Error == AssetDeliveryErrorCode.Canceled) {
    // Request was successfully canceled.
}
```

### Request asset packs asynchronously

In most cases, you should use[Coroutines](https://docs.unity3d.com/Manual/Coroutines.html)to request asset packs asynchronously and monitor progress, as shown by the following:  

```c#
private IEnumerator LoadAssetBundleCoroutine(string assetBundleName) {

    PlayAssetBundleRequest bundleRequest =
        PlayAssetDelivery.RetrieveAssetBundleAsync(assetBundleName);

    while (!bundleRequest.IsDone) {
        if(bundleRequest.Status == AssetDeliveryStatus.WaitingForWifi) {
            var userConfirmationOperation = PlayAssetDelivery.ShowCellularDataConfirmation();

            // Wait for confirmation dialog action.
            yield return userConfirmationOperation;

            if((userConfirmationOperation.Error != AssetDeliveryErrorCode.NoError) ||
               (userConfirmationOperation.GetResult() != ConfirmationDialogResult.Accepted)) {
                // The user did not accept the confirmation. Handle as needed.
            }

            // Wait for Wi-Fi connection OR confirmation dialog acceptance before moving on.
            yield return new WaitUntil(() => bundleRequest.Status != AssetDeliveryStatus.WaitingForWifi);
        }

        // Use bundleRequest.DownloadProgress to track download progress.
        // Use bundleRequest.Status to track the status of request.

        yield return null;
    }

    if (bundleRequest.Error != AssetDeliveryErrorCode.NoError) {
        // There was an error retrieving the bundle. For error codes NetworkError
        // and InsufficientStorage, you may prompt the user to check their
        // connection settings or check their storage space, respectively, then
        // try again.
        yield return null;
    }

    // Request was successful. Retrieve AssetBundle from request.AssetBundle.
    AssetBundle assetBundle = bundleRequest.AssetBundle;
```

For more information on handling errors, see the list of[`AssetDeliveryErrorCodes`](https://developer.android.com/reference/unity/namespace/Google/Play/AssetDelivery#namespaceGoogle_1_1Play_1_1AssetDelivery_1a84566dc4da8247c6613f8bfb2d2c1736).

## Other Play Core API methods

The following are some additional API methods you may want to use in your app.

### Check download size

Check the size of an AssetBundle by making an asynchronous call to Google Play and setting a callback method for when the operation completes:  

```c#
public IEnumerator GetDownloadSize() {
   PlayAsyncOperation<long> getSizeOperation =
   PlayAssetDelivery.GetDownloadSize(assetPackName);

   yield return getSizeOperation;
   if(operation.Error != AssetDeliveryErrorCode.NoError) {
       // Error while retrieving download size.
    } else {
        // Download size is given in bytes.
        long downloadSize = operation.GetResult();
    }
}
```

### Remove AssetBundles

You can remove fast-follow and on-demand AssetBundles that are not currently loaded into memory. Make the following asynchronous call and set a callback method for when it completes:  

```c#
PlayAsyncOperation<string> removeOperation = PlayAssetDelivery.RemoveAssetPack(assetBundleName);

removeOperation.Completed += (operation) =>
            {
                if(operation.Error != AssetDeliveryErrorCode.NoError) {
                    // Error while attempting to remove AssetBundles.
                } else {
                    // Files were deleted OR files did not exist to begin with.
                }
            };
```

## Next steps

[Test asset delivery](https://developer.android.com/guide/playcore/asset-delivery/test)locally and from Google Play.