---
title: https://developer.android.com/guide/playcore/asset-delivery/integrate-java
url: https://developer.android.com/guide/playcore/asset-delivery/integrate-java
source: md.txt
---

Use the steps in this guide to access your app's asset packs from your Java
code.

## Build for Kotlin and Java

Use the following steps to build Play Asset Delivery into your project's Android
App Bundle. You don't need to use Android Studio to perform these steps.
| **Note:** For a guided tutorial, see the [Using Play Asset Delivery in native games Codelab](https://codelabs.developers.google.com/codelabs/native-gamepad).

1. Update the version of the Android Gradle plugin in your project's
   `build.gradle` file to `4.0.0` or later.

2. In the top-level directory of your project, create a directory for the asset
   pack. This directory name is used as the asset pack name. Asset pack names
   must start with a letter and can only contain letters, numbers, and
   underscores.

3. In the asset pack directory, create a `build.gradle` file and add the
   following code. Make sure to specify the name of the asset pack and only one
   delivery type:

   ### Groovy

   ```groovy
   // In the asset pack's build.gradle file:
   plugins {
     id 'com.android.asset-pack'
   }

   assetPack {
       packName = "<var translate="no">asset-pack-name</var>" // Directory name for the asset pack
       dynamicDelivery {
           deliveryType = "[ install-time | fast-follow | on-demand ]"
       }
   }
   ```

   ### Kotlin

   ```kotlin
   // In the asset pack's build.gradle.kts file:
   plugins {
     id("com.android.asset-pack")
   }

   assetPack {
     packName.set("<var translate="no">asset-pack-name</var>") // Directory name for the asset pack
     dynamicDelivery {
       deliveryType.set("[ install-time | fast-follow | on-demand ]")
     }
   }
   ```
4. In the project's app `build.gradle` file, add the name of every asset pack
   in your project as shown below:

   ### Groovy

   ```groovy
   // In the app build.gradle file:
   android {
       ...
       assetPacks = [":<var translate="no">asset-pack-name</var>", ":<var translate="no">asset-pack2-name</var>"]
   }
   ```

   ### Kotlin

   ```kotlin
   // In the app build.gradle.kts file:
   android {
       ...
       assetPacks += listOf(":<var translate="no">asset-pack-name</var>", ":<var translate="no">asset-pack2-name</var>")
   }
   ```
5. In the project's `settings.gradle` file, include all asset packs in your
   project as shown below:

   ### Groovy

   ```groovy
   // In the settings.gradle file:
   include ':app'
   include ':<var translate="no">asset-pack-name</var>'
   include ':<var translate="no">asset-pack2-name</var>'
   ```

   ### Kotlin

   ```kotlin
   // In the settings.gradle.kts file:
   include(":app")
   include(":<var translate="no">asset-pack-name</var>")
   include(":<var translate="no">asset-pack2-name</var>")
   ```
6. In the asset pack directory, create the following subdirectory:
   `src/main/assets`.

7. Place assets in the `src/main/assets` directory. You can create
   subdirectories in here as well. The directory structure for your app should
   now look like the following:

   - `build.gradle`
   - `settings.gradle`
   - `app/`
   - <var translate="no">asset-pack-name</var>`/build.gradle`
   - <var translate="no">asset-pack-name</var>`/src/main/assets/`<var translate="no">your-asset-directories</var>
8. [Build the Android App Bundle with Gradle](https://developer.android.com/studio/build/building-cmdline#build_bundle).
   In the generated app bundle, the root-level directory now includes the
   following:

   - <var translate="no">asset-pack-name</var>`/manifest/AndroidManifest.xml`: Configures the asset pack's identifier and delivery mode
   - <var translate="no">asset-pack-name</var>`/assets/`<var translate="no">your-asset-directories</var>: Directory that contains all assets delivered as part of the asset pack

   Gradle generates the manifest for each asset pack and outputs the `assets/`
   directory for you.
9. (Optional) Include the [Play Asset Delivery Library](https://developer.android.com/guide/playcore#java-kotlin-asset-delivery) if you plan to use fast-follow and on-demand delivery

   ### Groovy

   ```groovy
   implementation "com.google.android.play:asset-delivery:2.3.0"
   // For Kotlin use asset-delivery-ktx
   implementation "com.google.android.play:asset-delivery-ktx:2.3.0"
   ```

   ### Kotlin

   ```kotlin
   implementation("com.google.android.play:asset-delivery:2.3.0")
   // For Kotlin use core-ktx
   implementation("com.google.android.play:asset-delivery-ktx:2.3.0")
   ```

   <br />

10. (Optional) Configure your app bundle to support different [texture
    compression formats](https://developer.android.com/guide/playcore/asset-delivery/texture-compression).

| **Note:** You must run your app as an app bundle rather than as a standalone APK to access the bundled assets. Or, you can edit the default run/debug configuration to deliver the app as an APK rather than a bundle. See [Build and test your Android App Bundle](https://developer.android.com/guide/app-bundle/test#deploy-using-studio).

## Integrate with the Play Asset Delivery API

The [Play Asset Delivery Java API](https://developer.android.com/reference/com/google/android/play/core/assetpacks/package-summary)
provides the
[`AssetPackManager`](https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackManager)
class for requesting asset packs, managing downloads, and accessing the assets. Make sure to [Add the Play Asset Delivery Library](https://developer.android.com/guide/playcore#java-kotlin-asset-delivery) into your project first.

You implement this API according to the delivery type of the asset pack you wish
to access. These steps are shown in the following flowchart.
| **Note:** You use a different API to access `install-time` asset packs than `fast-follow` and `on-demand` asset packs.

![Asset pack flow diagram for the Java programming language](https://developer.android.com/static/images/app-bundle/asset-pack-flow-java.png)


**Figure 1.** Flow diagram for accessing asset packs

<br />

## Install-time delivery

Asset packs configured as `install-time` are immediately available at app
launch. Use the Java
[AssetManager API](https://developer.android.com/reference/android/content/res/AssetManager) to access assets
served in this mode:  

### Kotlin

```kotlin
import android.content.res.AssetManager
...
val context: Context = createPackageContext("<var translate="no">com.example.app</var>", 0)
val assetManager: AssetManager = context.assets
val stream: InputStream = assetManager.open("<var translate="no">asset-name</var>")
```

### Java

```java
import android.content.res.AssetManager;
...
Context context = createPackageContext("<var translate="no">com.example.app</var>", 0);
AssetManager assetManager = context.getAssets();
InputStream is = assetManager.open("<var translate="no">asset-name</var>");
```

## Fast-follow and on-demand delivery

The following sections show how to get information about asset packs before
downloading them, how to call the API to start the download, and then how to
access the downloaded packs. These sections apply to `fast-follow` and
`on-demand` asset packs.

### Check status

Each asset pack is stored in a separate folder in the app's internal storage.
Use the
[`getPackLocation()`](https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackManager#getpacklocation)
method to determine the root folder of an asset pack. This method returns the
following values:

| Return value | Status |
|---|---|
| A valid [`AssetPackLocation`](https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackLocation) object | Asset pack root folder is ready for immediate access at [`assetsPath()`](https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackLocation#assetspath) |
| `null` | Unknown asset pack or assets are not available |

| **Note:** Do not rely on cached asset pack locations between app launches. The app should always check for the existence of asset packs at every launch. Asset packs may become invalid due to app updates or if the user clears the app data.

### Get download information about asset packs

Apps are required to disclose the size of the download before fetching the asset
pack. Use the
[`requestPackStates()`](https://developer.android.com/reference/com/google/android/play/core/ktx/package-summary#requestpackstates)
or the [`getPackStates()`](https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackManager#getpackstates)
method to determine the size of the download and whether the pack is already
downloading.  

### Kotlin

```kotlin
suspend fun requestPackStates(packNames: List<String>): AssetPackStates
```

### Java

```java
Task<AssetPackStates> getPackStates(List<String> packNames)
```

`requestPackStates()` is a suspend function returning an
[`AssetPackStates`](https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackStates)
object while the `getPackStates()` is an asynchronous method that returns a `Task<AssetPackStates>`. The
[`packStates()`](https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackStates#packstates)
method of an `AssetPackStates` object returns a `Map<String,
AssetPackState>`. This map contains the state of each requested asset
pack, keyed by its name:  

### Kotlin

```kotlin
AssetPackStates#packStates(): Map<String, AssetPackState>
```

### Java

```java
Map<String, AssetPackState> AssetPackStates#packStates()
```

The final request is shown by the following:  

### Kotlin

```kotlin
const val assetPackName = "assetPackName"
coroutineScope.launch {
  try {
    val assetPackStates: AssetPackStates =
      manager.requestPackStates(listOf(assetPackName))
    val assetPackState: AssetPackState =
      assetPackStates.packStates()[assetPackName]
  } catch (e: RuntimeExecutionException) {
    Log.d("MainActivity", e.message)
  }
}
```

### Java

```java
final String assetPackName = "<var translate="no">myasset</var>";

assetPackManager
    .getPackStates(Collections.singletonList(assetPackName))
    .addOnCompleteListener(new OnCompleteListener<AssetPackStates>() {
        @Override
        public void onComplete(Task<AssetPackStates> task) {
            AssetPackStates assetPackStates;
            try {
                assetPackStates = task.getResult();
                AssetPackState assetPackState =
                    assetPackStates.packStates().get(assetPackName);
            } catch (RuntimeExecutionException e) {
                Log.d("MainActivity", e.getMessage());
                return;
            })
```

The following
[`AssetPackState`](https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackState)
methods provide the size of the asset pack, the downloaded amount so far (if
requested), and the amount already transferred to the app:

- [`totalBytesToDownload()`](https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackState#totalbytestodownload)
- [`bytesDownloaded()`](https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackState#bytesdownloaded)
- [`transferProgressPercentage()`](https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackState#transferprogresspercentage)

To get the status of an asset pack, use the
[`status()`](https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackState#status)
method, which returns the status as an integer that corresponds to a constant
field in the
[`AssetPackStatus`](https://developer.android.com/reference/com/google/android/play/core/assetpacks/model/AssetPackStatus)
class. An asset pack that's not installed yet has the status
`AssetPackStatus.NOT_INSTALLED`.

If a request fails, use the
[`errorCode()`](https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackState#errorcode)
method, whose return value corresponds to a constant field in the
[`AssetPackErrorCode`](https://developer.android.com/reference/com/google/android/play/core/assetpacks/model/AssetPackErrorCode)
class.

### Install

Use the [`requestFetch()`](https://developer.android.com/reference/com/google/android/play/core/ktx/package-summary#requestfetch) or
[`fetch()`](https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackManager#fetch)
method to download an asset pack for the first time or call for the update of an
asset pack to complete:  

### Kotlin

```kotlin
suspend fun AssetPackManager.requestFetch(packs: List<String>): AssetPackStates
```

### Java

```java
Task<AssetPackStates> fetch(List<String> packNames)
```

This method returns an
[`AssetPackStates`](https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackStates)
object containing a list of packs and their initial download states and sizes.
If an asset pack requested via `requestFetch()` or `fetch()` is already downloading, the download
status is returned and no additional download is started.
| **Note:** In most cases, you implement a `listener` to track the download and installation process as covered in the next section.

### Monitor download states

You should implement an
[`AssetPackStateUpdatedListener`](https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackStateUpdateListener)
to track the installation progress of asset
packs. The status updates are broken down per pack to support tracking the
status of individual asset packs. You can start using available asset packs
before all other downloads for your request have completed.  

### Kotlin

```kotlin
fun registerListener(listener: AssetPackStateUpdatedListener)
fun unregisterListener(listener: AssetPackStateUpdatedListener)
```

### Java

```java
void registerListener(AssetPackStateUpdatedListener listener)
void unregisterListener(AssetPackStateUpdatedListener listener)
```
| **Note:** The Play Store automatically triggers the download of any `fast-follow` packs after the user installs or updates the app. However, these packs may not be ready to use immediately. You must check the status of the `fast-follow` packs at every app launch. If the download is in progress, monitor it with a listener. If the download is cancelled or paused, you can resume it by using the `fetch()` method, as covered in the [Install](https://developer.android.com/guide/playcore/asset-delivery/integrate-java#install) section.

#### Large downloads

If the download is larger than 200 MB and the user is not on Wi-Fi, the download
does not start until the user explicitly gives their consent to proceed with the
download using a mobile data connection. Similarly, if the download is large and
the user loses Wi-Fi, the download is paused and explicit consent is required to
proceed using a mobile data connection. A paused pack has state
`WAITING_FOR_WIFI`. To trigger the UI flow to prompt the user for consent, use
the [`showConfirmationDialog()`](https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackManager#showConfirmationDialog(androidx.activity.result.ActivityResultLauncher%3Candroidx.activity.result.IntentSenderRequest%3E))
method.

Note that if the app does not call this method, the download is paused and will
resume automatically only when the user is back on a Wi-Fi connection.

#### Required user confirmation

If a pack has the `REQUIRES_USER_CONFIRMATION` status, the download won't
proceed until the user accepts the dialog that is shown with
[`showConfirmationDialog()`](https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackManager#showConfirmationDialog(androidx.activity.result.ActivityResultLauncher%3Candroidx.activity.result.IntentSenderRequest%3E)).
This status can occur when the app is not recognized by Play---for example, if
the app was side-loaded.
Note that calling
[`showConfirmationDialog()`](https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackManager#showConfirmationDialog(androidx.activity.result.ActivityResultLauncher%3Candroidx.activity.result.IntentSenderRequest%3E))
in this case will cause the app to be updated. After the update, you will need
to request the assets again.

The following is an example implementation of a listener:  

### Kotlin

```kotlin
private val activityResultLauncher = registerForActivityResult(
    ActivityResultContracts.StartIntentSenderForResult()
) { result ->
    if (result.resultCode == RESULT_OK) {
        Log.d(TAG, "Confirmation dialog has been accepted.")
    } else if (result.resultCode == RESULT_CANCELED) {
        Log.d(TAG, "Confirmation dialog has been denied by the user.")
    }
}

assetPackManager.registerListener { assetPackState ->
  when(assetPackState.status()) {
    AssetPackStatus.PENDING -> {
      Log.i(TAG, "Pending")
    }
    AssetPackStatus.DOWNLOADING -> {
      val downloaded = assetPackState.bytesDownloaded()
      val totalSize = assetPackState.totalBytesToDownload()
      val percent = 100.0 * downloaded / totalSize

      Log.i(TAG, "PercentDone=" + String.format("%.2f", percent))
    }
    AssetPackStatus.TRANSFERRING -> {
      // 100% downloaded and assets are being transferred.
      // Notify user to wait until transfer is complete.
    }
    AssetPackStatus.COMPLETED -> {
      // Asset pack is ready to use. Start the game.
    }
    AssetPackStatus.FAILED -> {
      // Request failed. Notify user.
      Log.e(TAG, assetPackState.errorCode())
    }
    AssetPackStatus.CANCELED -> {
      // Request canceled. Notify user.
    }
    AssetPackStatus.WAITING_FOR_WIFI,
    AssetPackStatus.REQUIRES_USER_CONFIRMATION -> {
      if (!confirmationDialogShown) {
        assetPackManager.showConfirmationDialog(activityResultLauncher);
        confirmationDialogShown = true
      }
    }
    AssetPackStatus.NOT_INSTALLED -> {
      // Asset pack is not downloaded yet.
    }
    AssetPackStatus.UNKNOWN -> {
      Log.wtf(TAG, "Asset pack status unknown")
    }
  }
}
```

### Java

```java
assetPackStateUpdateListener = new AssetPackStateUpdateListener() {
    private final ActivityResultLauncher<IntentSenderRequest> activityResultLauncher =
      registerForActivityResult(
          new ActivityResultContracts.StartIntentSenderForResult(),
          new ActivityResultCallback<ActivityResult>() {
            @Override
            public void onActivityResult(ActivityResult result) {
              if (result.getResultCode() == RESULT_OK) {
                Log.d(TAG, "Confirmation dialog has been accepted.");
              } else if (result.getResultCode() == RESULT_CANCELED) {
                Log.d(TAG, "Confirmation dialog has been denied by the user.");
              }
            }
          });

    @Override
    public void onStateUpdate(AssetPackState assetPackState) {
      switch (assetPackState.status()) {
        case AssetPackStatus.PENDING:
          Log.i(TAG, "Pending");
          break;

        case AssetPackStatus.DOWNLOADING:
          long downloaded = assetPackState.bytesDownloaded();
          long totalSize = assetPackState.totalBytesToDownload();
          double percent = 100.0 * downloaded / totalSize;

          Log.i(TAG, "PercentDone=" + String.format("%.2f", percent));
          break;

        case AssetPackStatus.TRANSFERRING:
          // 100% downloaded and assets are being transferred.
          // Notify user to wait until transfer is complete.
          break;

        case AssetPackStatus.COMPLETED:
          // Asset pack is ready to use. Start the game.
          break;

        case AssetPackStatus.FAILED:
          // Request failed. Notify user.
          Log.e(TAG, assetPackState.errorCode());
          break;

        case AssetPackStatus.CANCELED:
          // Request canceled. Notify user.
          break;

        case AssetPackStatus.WAITING_FOR_WIFI:
        case AssetPackStatus.REQUIRES_USER_CONFIRMATION:
          if (!confirmationDialogShown) {
            assetPackManager.showConfirmationDialog(activityResultLauncher);
            confirmationDialogShown = true;
          }
          break;

        case AssetPackStatus.NOT_INSTALLED:
          // Asset pack is not downloaded yet.
          break;
        case AssetPackStatus.UNKNOWN:
          Log.wtf(TAG, "Asset pack status unknown")
          break;
      }
    }
}
```

Alternatively, you can use the
[`getPackStates()`](https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackManager#getpackstates)
method to get the status of current downloads.
[`AssetPackStates`](https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackStates)
contains the download progress, download status, and any failure error codes.

### Access asset packs

You can access an asset pack using file system calls after the download request
reaches the
[`COMPLETED`](https://developer.android.com/reference/com/google/android/play/core/assetpacks/model/AssetPackStatus#completed)
state. Use the
[`getPackLocation()`](https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackManager#getpacklocation)
method to get the root folder of the asset pack.

Assets are stored in the `assets` directory within the asset pack root
directory. You can get the path to the `assets` directory by using the
convenience method
[`assetsPath()`](https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackLocation#assetspath).
Use the following method to get the path to a specific asset:  

### Kotlin

```kotlin
private fun getAbsoluteAssetPath(assetPack: String, relativeAssetPath: String): String? {
    val assetPackPath: AssetPackLocation =
      assetPackManager.getPackLocation(assetPack)
      // asset pack is not ready
      ?: return null

    val assetsFolderPath = assetPackPath.assetsPath()
    // equivalent to: FilenameUtils.concat(assetPackPath.path(), "assets")
    return FilenameUtils.concat(assetsFolderPath, relativeAssetPath)
}
```

### Java

```java
private String getAbsoluteAssetPath(String assetPack, String relativeAssetPath) {
    AssetPackLocation assetPackPath = assetPackManager.getPackLocation(assetPack);

    if (assetPackPath == null) {
        // asset pack is not ready
        return null;
    }

    String assetsFolderPath = assetPackPath.assetsPath();
    // equivalent to: FilenameUtils.concat(assetPackPath.path(), "assets");
    String assetPath = FilenameUtils.concat(assetsFolderPath, relativeAssetPath);
    return assetPath;
}
```

## Other Play Asset Delivery API methods

The following are some additional API methods you may want to use in your app.

### Cancel request

Use
[`cancel()`](https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackManager#cancel)
to cancel an active asset pack request. Note that this request is a best-effort
operation.

### Remove an asset pack

Use
[`requestRemovePack()`](https://developer.android.com/reference/com/google/android/play/core/ktx/package-summary#requestremovepack)
or
[`removePack()`](https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackManager#removepack)
to schedule the removal of an asset pack.

### Get locations of multiple asset packs

Use
[`getPackLocations()`](https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackManager#getpacklocations)
to query the status of multiple asset packs in bulk, which returns a map of
asset packs and their locations. The map returned by `getPackLocations()`
contains an entry for each pack that is currently downloaded and up-to-date.

## Next step

[Test Play Asset Delivery](https://developer.android.com/guide/playcore/asset-delivery/test) locally and from
Google Play.