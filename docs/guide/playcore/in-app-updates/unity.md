---
title: https://developer.android.com/guide/playcore/in-app-updates/unity
url: https://developer.android.com/guide/playcore/in-app-updates/unity
source: md.txt
---

# Support in-app updates (Unity)

This guide describes how to support[in-app updates](https://developer.android.com/guide/playcore/in-app-updates)in your app using Unity. There are separate guides for cases where your implementation uses[the Kotlin programming language or the Java programming language](https://developer.android.com/guide/playcore/in-app-updates/kotlin-java), and cases where your implementation uses[native code (C/C++)](https://developer.android.com/guide/playcore/in-app-updates/native).

## Unity SDK overview

The Play in-app update API is part of the[Play Core SDK](https://developer.android.com/reference/com/google/android/play/core/release-notes)family. The Unity Plugin offers an[`AppUpdateManager`](https://developer.android.com/reference/unity/class/Google/Play/AppUpdate/AppUpdateManager)class to handle communication between your app and the Google Play API. You must instantiate this class before you can use it to manage in-app updates:  

    AppUpdateManager appUpdateManager = new AppUpdateManager();

## Set up your development environment

### OpenUPM-CLI

If you have the[OpenUPM CLI](https://github.com/openupm/openupm-cli#installation)installed you can install the OpenUPM registry with the following command:  

    openupm add com.google.play.appupdate

### OpenUPM

1. Open the[package manager settings](https://docs.unity3d.com/Manual/class-PackageManager.html)by selecting the Unity menu option**Edit \> Project Settings \> Package Manager**.

2. Add OpenUPM as a scoped registry to the Package Manager window:

       Name: package.openupm.com
       URL: https://package.openupm.com
       Scopes: com.google.external-dependency-manager
         com.google.play.common
         com.google.play.core
         com.google.play.appupdate

3. Open the[package manager menu](https://docs.unity3d.com/Manual/upm-ui-install.html)by selecting the Unity menu option**Window \> Package Manager**.

4. Set the manager scope drop-down to select**My Registries**.

5. Select the**Google Play Integrity plugin for Unity** package from the package list and press**Install**.

### Import from GitHub

1. Download the latest[`.unitypackage`](https://github.com/google/play-in-app-updates-unity/releases/latest)release from GitHub.

2. Import the`.unitypackage`file by selecting the Unity menu option**Assets \> Import package \> Custom Package**and importing all items.

| **Note:** By downloading and using Google Play Unity Plugins, you agree to the[Play Core Software Development Kit Terms of Service](https://developer.android.com/guide/playcore#license).

## Check for update availability

Before you request an update, check if there is an update available for your app. Use`AppUpdateManager`to check for an update in a[coroutine](https://docs.unity3d.com/Manual/Coroutines):  

    IEnumerator CheckForUpdate()
    {
      PlayAsyncOperation<AppUpdateInfo, AppUpdateErrorCode> appUpdateInfoOperation =
        appUpdateManager.GetAppUpdateInfo();

      // Wait until the asynchronous operation completes.
      yield return appUpdateInfoOperation;

      if (appUpdateInfoOperation.IsSuccessful)
      {
        var appUpdateInfoResult = appUpdateInfoOperation.GetResult();
        // Check AppUpdateInfo's UpdateAvailability, UpdatePriority,
        // IsUpdateTypeAllowed(), ... and decide whether to ask the user
        // to start an in-app update.
      }
      else
      {
        // Log appUpdateInfoOperation.Error.
      }
    }

The returned[`AppUpdateInfo`](https://developer.android.com/reference/unity/class/Google/Play/AppUpdate/AppUpdateInfo)instance contains the update availability status. If an in-app update is already in progress, the instance also reports the status of the in-progress update.

### Check update staleness

In addition to checking whether an update is available, you might also want to check how much time has passed since the user was last notified of an update through the Play Store. This can help you decide whether you should initiate a flexible update or an immediate update. For example, you might wait a few days before notifying the user with a flexible update, and a few days after that before requiring an immediate update.

Use[`ClientVersionStalenessDays`](https://developer.android.com/reference/unity/class/Google/Play/AppUpdate/AppUpdateInfo#clientversionstalenessdays)to check the number of days since the update became available through the Play Store:  

    var stalenessDays = appUpdateInfoOperation.ClientVersionStalenessDays;

### Check update priority

The Google Play Developer API lets you set the priority of each update. This allows your app to decide how strongly to recommend an update to the user. For example, consider the following strategy for setting update priority:

- Minor UI improvements:**Low-priority**update; request neither a flexible update nor an immediate update.
- Performance improvements:**Medium-priority**update; request a flexible update.
- Critical security update:**High-priority**update; request an immediate update.

To determine priority, Google Play uses an integer value between 0 and 5, with 0 being the default and 5 being the highest priority. To set the priority for an update, use the`inAppUpdatePriority`field under`Edits.tracks.releases`in the Google Play Developer API. All newly-added versions in the release are considered to be the same priority as the release. Priority can only be set when rolling out a new release and cannot be changed later.

Set the priority using the Google Play Developer API as described in the[Play Developer API documentation](https://developers.google.com/android-publisher/tracks#apk_workflow_example). In-app update priority should be specified in the[`Edit.tracks`](https://developers.google.com/android-publisher/api-ref/rest/v3/edits.tracks)resource passed in the[`Edit.tracks: update`](https://developers.google.com/android-publisher/api-ref/rest/v3/edits.tracks/update)method. The following example demonstrates releasing an app with version code 88 and`inAppUpdatePriority`5:  

```json
{
  "releases": [{
      "versionCodes": ["88"],
      "inAppUpdatePriority": 5,
      "status": "completed"
  }]
}
```

In your app's code, you can check the priority level for a given update using[`UpdatePriority`](https://developer.android.com/reference/unity/class/Google/Play/AppUpdate/AppUpdateInfo#updatepriority):  

    var priority = appUpdateInfoOperation.UpdatePriority;

## Start an update

After ensuring that an update is available, you can request an update using[`AppUpdateManager.StartUpdate()`](https://developer.android.com/reference/unity/class/Google/Play/AppUpdate/AppUpdateManager#startupdate). Before you request an update, make sure that you have an up-to-date`AppUpdateInfo`object. You must also create an[`AppUpdateOptions`](https://developer.android.com/reference/unity/class/Google/Play/AppUpdate/AppUpdateOptions)object to configure the update flow.

The following example creates an`AppUpdateOptions`object for an immediate update flow:  

    // Creates an AppUpdateOptions defining an immediate in-app
    // update flow and its parameters.
    var appUpdateOptions = AppUpdateOptions.ImmediateAppUpdateOptions();

The following example creates an`AppUpdateOptions`object for a flexible update flow:  

    // Creates an AppUpdateOptions defining a flexible in-app
    // update flow and its parameters.
    var appUpdateOptions = AppUpdateOptions.FlexibleAppUpdateOptions();

The`AppUpdateOptions`object also contains an`AllowAssetPackDeletion`field that defines whether the update is allowed to clear[asset packs](https://developer.android.com/guide/app-bundle/asset-delivery)in case of limited device storage. This field is set to`false`by default, but you can pass the`allowAssetPackDeletion`optional argument to`ImmediateAppUpdateOptions()`or`FlexibleAppUpdateOptions()`to set it to`true`instead:  

    // Creates an AppUpdateOptions for an immediate flow that allows
    // asset pack deletion.
    var appUpdateOptions =
      AppUpdateOptions.ImmediateAppUpdateOptions(allowAssetPackDeletion: true);

    // Creates an AppUpdateOptions for a flexible flow that allows asset
    // pack deletion.
    var appUpdateOptions =
      AppUpdateOptions.FlexibleAppUpdateOptions(allowAssetPackDeletion: true);

| **Note:** Use the`AllowAssetPackDeletion`API option with care to avoid accidentally deleting assets. Before setting this option to`true`, you should check`AppUpdateManager.IsUpdateTypeAllowed()`with the`AllowAssetPackDeletion`option set to`false`.

The next steps depend on whether you are requesting a[flexible update](https://developer.android.com/guide/playcore/in-app-updates/unity#flexible)or an[immediate update](https://developer.android.com/guide/playcore/in-app-updates/unity#immediate).

## Handle a flexible update

After you have an up-to-date`AppUpdateInfo`object and a properly-configured`AppUpdateOptions`object, you can call`AppUpdateManager.StartUpdate()`to asynchronously request an update flow.  

    IEnumerator StartFlexibleUpdate()
    {
      // Creates an AppUpdateRequest that can be used to monitor the
      // requested in-app update flow.
      var startUpdateRequest = appUpdateManager.StartUpdate(
        // The result returned by PlayAsyncOperation.GetResult().
        appUpdateInfoResult,
        // The AppUpdateOptions created defining the requested in-app update
        // and its parameters.
        appUpdateOptions);

      while (!startUpdateRequest.IsDone)
      {
      // For flexible flow,the user can continue to use the app while
      // the update downloads in the background. You can implement a
      // progress bar showing the download status during this time.
      yield return null;
      }

    }

For a flexible update flow, you must trigger the installation of the app update after the download finishes successfully. To do this, call[`AppUpdateManager.CompleteUpdate()`](https://developer.android.com/reference/unity/class/Google/Play/AppUpdate/AppUpdateManager#completeupdate), as shown in the following example:  

    IEnumerator CompleteFlexibleUpdate()
    {
      var result = appUpdateManager.CompleteUpdate();
      yield return result;

      // If the update completes successfully, then the app restarts and this line
      // is never reached. If this line is reached, then handle the failure (e.g. by
      // logging result.Error or by displaying a message to the user).
    }

## Handle an immediate update

After you have an up-to-date`AppUpdateInfo`object and a properly-configured`AppUpdateOptions`object, you can call`AppUpdateManager.StartUpdate()`to asynchronously request an update flow.  

    IEnumerator StartImmediateUpdate()
    {
      // Creates an AppUpdateRequest that can be used to monitor the
      // requested in-app update flow.
      var startUpdateRequest = appUpdateManager.StartUpdate(
        // The result returned by PlayAsyncOperation.GetResult().
        appUpdateInfoResult,
        // The AppUpdateOptions created defining the requested in-app update
        // and its parameters.
        appUpdateOptions);
      yield return startUpdateRequest;

      // If the update completes successfully, then the app restarts and this line
      // is never reached. If this line is reached, then handle the failure (for
      // example, by logging result.Error or by displaying a message to the user).
    }

For an immediate update flow, Google Play displays a user confirmation dialog. When the user accepts the request, Google Play automatically downloads and installs the update, then restarts the app to the updated version if installation is successful.

## Error handling

This section describes solutions for common errors.

- If`StartUpdate()`throws an`ArgumentNullException`, it means that`AppUpdateInfo`is null. Make sure the`AppUpdateInfo`object returned from`GetAppUpdateInfo()`is not null before starting the update flow.
- If`PlayAsyncOperation`returns the`ErrorUpdateUnavailable`error code, make sure there is an updated app version available that has the same application ID and signing key.
- If`PlayAsyncOperation`returns the`ErrorUpdateNotAllowed`error code, it means that the`AppUpdateOptions`object indicates an update type that is not allowed for the available update. Check whether the`AppUpdateInfo`object indicates that the selected update type is allowed before starting the update flow.

## Next steps

[Test your app's in-app updates](https://developer.android.com/guide/playcore/in-app-updates/test)to verify that your integration is working correctly.