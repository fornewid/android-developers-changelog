---
title: https://developer.android.com/guide/playcore/in-app-updates/unreal-engine
url: https://developer.android.com/guide/playcore/in-app-updates/unreal-engine
source: md.txt
---

# Support in-app updates (Unreal Engine)

This guide describes how to support[in-app updates](https://developer.android.com/guide/playcore/in-app-updates)in your app using Unreal Engine. There are separate guides for cases where your implementation uses[the Kotlin programming language or the Java programming language](https://developer.android.com/guide/playcore/in-app-updates/kotlin-java), and cases where your implementation uses[native code (C/C++)](https://developer.android.com/guide/playcore/in-app-updates/native)or[Unity](https://developer.android.com/guide/playcore/in-app-updates/unity).

## Unreal Engine SDK overview

The Play In-App Updates API is part of Play Core SDK family. The API for Unreal Engine offers a`UInAppUpdatesManager`class to handle communication between your app and the Play API. After a request is made, your app can check the status of the request using`EAppUpdateErrorCode`.

## Supported Unreal Engine versions

The plugin supports**Unreal Engine 5.0**and all subsequent versions.

## Set up your development environment

| **Note:** If you have already used the In-app Reviews or In-app Updates plugins in Unreal Engine, you can skip to the final step.

1. Download the[Play Unreal Engine Plugin](https://github.com/google/play-unreal-engine-plugin)from the GitHub repository.

2. Copy the`GooglePlay`folder inside your`Plugins`folder in your Unreal Engine project.

3. Open your Unreal Engine project and click**Edit → Plugins**.

4. Search for**Google Play** and check the**Enabled**checkbox.

5. Restart the game project and trigger a build.

6. Open your project's`Build.cs`file and add the`PlayInAppUpdates`module to`PublicDependencyModuleNames`:

       using UnrealBuildTool;

       public class MyGame : ModuleRules
       {
         public MyGame(ReadOnlyTargetRules Target) : base(Target)
         {
           // ...

           PublicDependencyModuleNames.Add("PlayInAppUpdates");

           // ...
         }
       }

## Check for update availability

Before you request an update, check if there is an update available for your app. Use`UInAppUpdatesManager::RequestInfo`to check for an update:

MyClass.h  

    void MyClass::OnRequestInfoOperationCompleted(
      EAppUpdateErrorCode ErrorCode,
      UAppUpdateInfo* UpdateInfo)
    {
      // Check the resulting error code.
      if (ErrorCode == EAppUpdateErrorCode::AppUpdate_NO_ERROR)
      {
        // Check AppUpdateInfo's UpdateAvailability, UpdatePriority,
        // IsUpdateTypeAllowed(), ... and decide whether to ask the user
        // to start an in-app update.
      }
    }

MyClass.cpp  

    void MyClass::CheckForUpdateAvailability()
    {
      // Create a delegate to bind the callback function.
      FRequestInfoOperationCompletedDelegate Delegate;

      // Bind the completion handler (OnRequestInfoOperationCompleted) to the delegate.
      Delegate.BindDynamic(this, &MyClass::OnRequestInfoOperationCompleted);

      // Initiate the request info operation, passing the delegate to handle the result.
      GetGameInstance()
        ->GetSubsystem<UInAppUpdatesManager>()
        ->RequestInfo(Delegate);
    }

The returned`UAppUpdateInfo`instance contains the update availability status. If an in-app update is already in progress, the instance also reports the status of the in-progress update.

### Check update staleness

In addition to checking whether an update is available, you might also want to check how much time has passed since the user was last notified of an update through the Play Store. This can help you decide whether you should initiate a flexible update or an immediate update. For example, you might wait a few days before notifying the user with a flexible update, and a few days after that before requiring an immediate update.

Use`UAppUpdateInfo:GetClientVersionStalenessDays`to check the number of days since the update became available through the Play Store:  

    int32 ClientVersionStalenessDays = UpdateInfo->GetClientVersionStalenessDays();

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

In your app's code, you can check the priority level for a given update using`UAppUpdateInfo::UpdatePriority`:  

    int32 Priority = UpdateInfo->GetPriority();

## Start an update

After you confirm that an update is available, you can request an update using`UInAppUpdatesManager::StartUpdate`. Before you request an update, make sure that you have an up-to-date`UAppUpdateInfo`object. You must also create an`UAppUpdateOptions`object to configure the update flow.

The following example creates an`UAppUpdateOptions`object for an immediate update flow:  

    // Creates an UAppUpdateOptions defining an immediate in-app
    // update flow and its parameters.
    UAppUpdateOptions* Options = NewObject<UAppUpdateOptions>();
    Options->CreateOptions(EAppUpdateType::AppUpdate_TYPE_IMMEDIATE);

The following example creates an`UAppUpdateOptions`object for a flexible update flow:  

    // Creates an UAppUpdateOptions defining a flexible in-app
    // update flow and its parameters.
    UAppUpdateOptions* Options = NewObject<UAppUpdateOptions>();
    Options->CreateOptions(EAppUpdateType::AppUpdate_TYPE_FLEXIBLE);

The`UAppUpdateOptions`object also contains an`IsAssetPackDeletionAllowed`function that returns whether the update is allowed to clear[asset packs](https://developer.android.com/guide/app-bundle/asset-delivery)in case of limited device storage. This field is set to`false`by default, but you can set the field using`UAppUpdateOptions::SetAssetPackDeletionAllowed`to set it to`true`instead:  

    // Sets the AssetPackDeletionAllowed field to true.
    Options->SetAssetPackDeletionAllowed(true);

| **Note:** Use the`AllowAssetPackDeletion`API option with care to avoid accidentally deleting assets. Before setting this option to`true`, you should check`UAppUpdateInfo::IsUpdateTypeAllowed`with the`AllowAssetPackDeletion`option set to`false`.

The next steps depend on whether you are requesting a[flexible update](https://developer.android.com/guide/playcore/in-app-updates/unreal-engine#flexible)or an[immediate update](https://developer.android.com/guide/playcore/in-app-updates/unreal-engine#immediate).

## Handle a flexible update

After you have an up-to-date`UAppUpdateInfo`object and a properly-configured`UAppUpdateOptions`object, you can call`UInAppUpdatesManager::StartUpdate`to request an update flow.

MyClass.h  

    void MyClass::OnStartUpdateOperationCompleted(EAppUpdateErrorCode ErrorCode)
    {
      // ...
    }

MyClass.cpp  

    // .cpp
    void MyClass::StartUpdate()
    {
      // Create a delegate to bind the callback function.
      FUpdateOperationCompletedDelegate Delegate;

      // Bind the completion handler (OnStartUpdateOperationCompleted) to the delegate.
      Delegate.BindDynamic(this, &MyClass::OnStartUpdateOperationCompleted);

      // Initiate the start update operation, passing the delegate to handle the result.
      GetGameInstance()
        ->GetSubsystem<UInAppUpdatesManager>()
        ->StartUpdate(UpdateInfo, UpdateOptions, Delegate);
    }

For a flexible update flow, you must trigger the installation of the app update after the download finishes successfully. To do this, call`InAppUpdatesManager::CompleteUpdate`, as shown in the following example:

MyClass.h  

    void MyClass::OnCompleteUpdateOperationCompleted(EAppUpdateErrorCode ErrorCode)
    {
      // ...
    }

MyClass.cpp  

    void MyClass::CompleteFlexibleUpdate()
    {
      // Create a delegate to bind the callback function.
      FUpdateOperationCompletedDelegate Delegate;

      // Bind the completion handler (OnCompleteUpdateOperationCompleted) to the delegate.
      Delegate.BindDynamic(this, &MyClass::OnCompleteUpdateOperationCompleted);

      // Initiate the complete update operation, passing the delegate to handle the result.
      GetGameInstance()
        ->GetSubsystem<UInAppUpdatesManager>()
        ->CompleteUpdate(UpdateInfo, UpdateOptions, Delegate);
    }

## Handle an immediate update

After you have an up-to-date`UAppUpdateInfo`object and a properly-configured`UAppUpdateOptions`object, you can call`InAppUpdatesManager::StartUpdate`to request an update flow.

MyClass.h  

    void MyClass::OnStartUpdateOperationCompleted(EAppUpdateErrorCode ErrorCode)
    {
      // ...
    }

MyClass.cpp  

    void MyClass::StartUpdate()
    {
      // Create a delegate to bind the callback function.
      FUpdateOperationCompletedDelegate Delegate;

      // Bind the completion handler (OnStartUpdateOperationCompleted) to the delegate.
      Delegate.BindDynamic(this, &MyClass::OnStartUpdateOperationCompleted);

      // Initiate the start update operation, passing the delegate to handle the result.
      GetGameInstance()
        ->GetSubsystem<UInAppUpdatesManager>()
        ->StartUpdate(UpdateInfo, UpdateOptions, Delegate);
    }

For an immediate update flow, Google Play displays a user confirmation dialog. When the user accepts the request, Google Play automatically downloads and installs the update, then restarts the app to the updated version if installation is successful.

## Error handling

This section describes solutions for common errors.

- If`UInAppUpdatesManager::StartUpdate`returns an`AppUpdate_INVALID_REQUEST`error, it means that`UAppUpdateInfo`is invalid. Make sure the`UAppUpdateInfo`object returned from`UInAppUpdatesManager::RequestInfo`is not null before starting the update flow.
- If`UInAppUpdatesManager::StartUpdate`returns the`AppUpdate_NOT_ALLOWED`error, it means that the`UAppUpdateOptions`object indicates an update type that is not allowed for the available update. Check whether the`UAppUpdateInfo`object indicates that the selected update type is allowed before starting the update flow.

## Next steps

[Test your app's in-app updates](https://developer.android.com/guide/playcore/in-app-updates/test)to verify that your integration is working correctly.