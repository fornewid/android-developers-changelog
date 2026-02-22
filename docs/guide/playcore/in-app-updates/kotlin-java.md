---
title: https://developer.android.com/guide/playcore/in-app-updates/kotlin-java
url: https://developer.android.com/guide/playcore/in-app-updates/kotlin-java
source: md.txt
---

This guide describes how to support [in-app updates](https://developer.android.com/guide/playcore/in-app-updates) in your app using either
Kotlin or Java. There are separate guides for cases where your implementation
uses [native code (C/C++)](https://developer.android.com/guide/playcore/in-app-updates/native) and cases where your implementation uses
[Unity](https://developer.android.com/guide/playcore/in-app-updates/unity) or [Unreal Engine](https://developer.android.com/guide/playcore/in-app-updates/unreal-engine).

## Set up your development environment

The Play In-App Update Library is a part of the [Google Play Core libraries](https://developer.android.com/guide/playcore).
Include the following Gradle dependency to integrate the Play In-App Update
Library.  

### Groovy

```groovy
// In your app's build.gradle file:
...
dependencies {
    // This dependency is downloaded from the https://developer.android.com/studio/build/dependencies#google-maven.
    // So, make sure you also include that repository in your project's build.gradle file.
    implementation 'com.google.android.play:app-update:2.1.0'

    // For Kotlin users also add the Kotlin extensions library for Play In-App Update:
    implementation 'com.google.android.play:app-update-ktx:2.1.0'
    ...
}
```

### Kotlin

```kotlin
// In your app's build.gradle.kts file:
...
dependencies {
    // This dependency is downloaded from the https://developer.android.com/studio/build/dependencies#google-maven.
    // So, make sure you also include that repository in your project's build.gradle file.
    implementation("com.google.android.play:app-update:2.1.0")

    // For Kotlin users also import the Kotlin extensions library for Play In-App Update:
    implementation("com.google.android.play:app-update-ktx:2.1.0")
    ...
}
```

## Check for update availability

Before requesting an update, check if there is an update available for your app.
Use [`AppUpdateManager`](https://developer.android.com/reference/com/google/android/play/core/appupdate/AppUpdateManager) to check for an update:  

### Kotlin

```kotlin
val appUpdateManager = AppUpdateManagerFactory.create(context)

// Returns an intent object that you use to check for an update.
val appUpdateInfoTask = appUpdateManager.appUpdateInfo

// Checks that the platform will allow the specified type of update.
appUpdateInfoTask.addOnSuccessListener { appUpdateInfo ->
    if (appUpdateInfo.updateAvailability() == UpdateAvailability.UPDATE_AVAILABLE
        // This example applies an immediate update. To apply a flexible update
        // instead, pass in AppUpdateType.FLEXIBLE
        && appUpdateInfo.isUpdateTypeAllowed(AppUpdateType.IMMEDIATE)
    ) {
        // Request the update.
    }
}
```

### Java

```java
AppUpdateManager appUpdateManager = AppUpdateManagerFactory.create(context);

// Returns an intent object that you use to check for an update.
Task<AppUpdateInfo> appUpdateInfoTask = appUpdateManager.getAppUpdateInfo();

// Checks that the platform will allow the specified type of update.
appUpdateInfoTask.addOnSuccessListener(appUpdateInfo -> {
    if (appUpdateInfo.updateAvailability() == UpdateAvailability.UPDATE_AVAILABLE
          // This example applies an immediate update. To apply a flexible update
          // instead, pass in AppUpdateType.FLEXIBLE
          && appUpdateInfo.isUpdateTypeAllowed(AppUpdateType.IMMEDIATE)) {
              // Request the update.
    }
});
```

The returned [`AppUpdateInfo`](https://developer.android.com/reference/com/google/android/play/core/appupdate/AppUpdateInfo) instance contains the update availability
status. Depending on the status of the update, the instance also contains the
following:

- If an update is available and the update is allowed, the instance also contains an intent to start the update.
- If an in-app update is already in progress, the instance also reports the status of the in-progress update.

### Check update staleness

In addition to checking whether an update is available, you might also want to
check how much time has passed since the user was last notified of an update
through the Play Store. This can help you decide whether you should initiate a
flexible update or an immediate update. For example, you might wait a few days
before notifying the user with a flexible update, and a few days after that
before requiring an immediate update.

Use [`clientVersionStalenessDays()`](https://developer.android.com/reference/com/google/android/play/core/appupdate/AppUpdateInfo#clientVersionStalenessDays()) to check the number of days since the
update became available on the Play Store:  

### Kotlin

```kotlin
val appUpdateManager = AppUpdateManagerFactory.create(context)

// Returns an intent object that you use to check for an update.
val appUpdateInfoTask = appUpdateManager.appUpdateInfo

// Checks whether the platform allows the specified type of update,
// and current version staleness.
appUpdateInfoTask.addOnSuccessListener { appUpdateInfo ->
    if (appUpdateInfo.updateAvailability() == UpdateAvailability.UPDATE_AVAILABLE
          && (appUpdateInfo.clientVersionStalenessDays() ?: -1) >= DAYS_FOR_FLEXIBLE_UPDATE
          && appUpdateInfo.isUpdateTypeAllowed(AppUpdateType.FLEXIBLE)) {
              // Request the update.
    }
}
```

### Java

```java
AppUpdateManager appUpdateManager = AppUpdateManagerFactory.create(context);

// Returns an intent object that you use to check for an update.
Task<AppUpdateInfo> appUpdateInfoTask = appUpdateManager.getAppUpdateInfo();

// Checks whether the platform allows the specified type of update,
// and current version staleness.
appUpdateInfoTask.addOnSuccessListener(appUpdateInfo -> {
    if (appUpdateInfo.updateAvailability() == UpdateAvailability.UPDATE_AVAILABLE
          && appUpdateInfo.clientVersionStalenessDays() != null
          && appUpdateInfo.clientVersionStalenessDays() >= DAYS_FOR_FLEXIBLE_UPDATE
          && appUpdateInfo.isUpdateTypeAllowed(AppUpdateType.FLEXIBLE)) {
              // Request the update.
    }
});
```

### Check update priority

The Google Play Developer API lets you set the priority of each update. This
allows your app to decide how strongly to recommend an update to the user. For
example, consider the following strategy for setting update priority:

- Minor UI improvements: **Low-priority** update; request neither a flexible update nor an immediate update. Update only when the user isn't interacting with your app.
- Performance improvements: **Medium-priority** update; request a flexible update.
- Critical security update: **High-priority** update; request an immediate update.

To determine priority, Google Play uses an integer value between 0 and 5, with 0
being the default and 5 being the highest priority. To set the priority for an
update, use the `inAppUpdatePriority` field under `Edits.tracks.releases` in the
Google Play Developer API. All newly-added versions in the release are
considered to be the same priority as the release. Priority can only be set when
rolling out a new release and cannot be changed later.

Set the priority using the Google Play Developer API as described in the [Play
Developer API documentation](https://developers.google.com/android-publisher/tracks#apk_workflow_example). In-app update priority should be specified in
the [`Edit.tracks`](https://developers.google.com/android-publisher/api-ref/rest/v3/edits.tracks) resource passed in the [`Edit.tracks: update`](https://developers.google.com/android-publisher/api-ref/rest/v3/edits.tracks/update)
method. The following example demonstrates releasing an app with version code 88
and `inAppUpdatePriority` 5:  

```json
{
  "releases": [{
      "versionCodes": ["88"],
      "inAppUpdatePriority": 5,
      "status": "completed"
  }]
}
```

In your app's code, you can check the priority level for a given update using
[`updatePriority()`](https://developer.android.com/reference/com/google/android/play/core/appupdate/AppUpdateInfo#updatePriority()). The returned priority takes into account the
`inAppUpdatePriority` for all app version codes between the installed version
and latest available version, irrespective of the release track. For example,
consider the following scenario:

- You release version 1 to a production track with no priority.
- You release version 2 to an internal test track with priority 5.
- You release version 3 to a production track with no priority.

When production users update from version 1 to version 3, they will get priority
5, even though version 2 was published on a different track.  

### Kotlin

```kotlin
val appUpdateManager = AppUpdateManagerFactory.create(context)

// Returns an intent object that you use to check for an update.
val appUpdateInfoTask = appUpdateManager.appUpdateInfo

// Checks whether the platform allows the specified type of update,
// and checks the update priority.
appUpdateInfoTask.addOnSuccessListener { appUpdateInfo ->
    if (appUpdateInfo.updateAvailability() == UpdateAvailability.UPDATE_AVAILABLE
          && appUpdateInfo.updatePriority() >= 4 /* high priority */
          && appUpdateInfo.isUpdateTypeAllowed(AppUpdateType.IMMEDIATE)) {
              // Request an immediate update.
    }
}
```

### Java

```java
AppUpdateManager appUpdateManager = AppUpdateManagerFactory.create(context);

// Returns an intent object that you use to check for an update.
Task<AppUpdateInfo> appUpdateInfoTask = appUpdateManager.getAppUpdateInfo();

// Checks whether the platform allows the specified type of update,
// and checks the update priority.
appUpdateInfoTask.addOnSuccessListener(appUpdateInfo -> {
    if (appUpdateInfo.updateAvailability() == UpdateAvailability.UPDATE_AVAILABLE
          && appUpdateInfo.updatePriority() >= 4 /* high priority */
          && appUpdateInfo.isUpdateTypeAllowed(AppUpdateType.IMMEDIATE)) {
              // Request an immediate update.
    }
});
```

## Start an update

After you confirm that an update is available, you can request an update using
[`AppUpdateManager.startUpdateFlowForResult()`](https://developer.android.com/reference/com/google/android/play/core/appupdate/AppUpdateManager#startupdateflowforresult):  

### Kotlin

```kotlin
appUpdateManager.startUpdateFlowForResult(
    // Pass the intent that is returned by 'getAppUpdateInfo()'.
    appUpdateInfo,
    // an activity result launcher registered via registerForActivityResult
    activityResultLauncher,
    // Or pass 'AppUpdateType.FLEXIBLE' to newBuilder() for
    // flexible updates.
    AppUpdateOptions.newBuilder(AppUpdateType.IMMEDIATE).build())
```

### Java

```java
appUpdateManager.startUpdateFlowForResult(
    // Pass the intent that is returned by 'getAppUpdateInfo()'.
    appUpdateInfo,
    // an activity result launcher registered via registerForActivityResult
    activityResultLauncher,
    // Or pass 'AppUpdateType.FLEXIBLE' to newBuilder() for
    // flexible updates.
    AppUpdateOptions.newBuilder(AppUpdateType.IMMEDIATE).build());
```
| **Note:** Be mindful of how often you request updates to avoid annoying or tiring your users. You should only request in-app updates for changes that are important to the core functionality of your app.

Each `AppUpdateInfo` instance can be used to start an update only once. To retry
the update in case of failure, request a new `AppUpdateInfo` and check again
that the update is available and allowed.

You can register an activity result launcher using the built-in
[`ActivityResultContracts.StartIntentSenderForResult`](https://developer.android.com/reference/androidx/activity/result/contract/ActivityResultContracts.StartIntentSenderForResult) contract. Check the
section on [getting callback for update status](https://developer.android.com/guide/playcore/in-app-updates/kotlin-java#status-callback).

The next steps depend on whether you are requesting a [flexible update](https://developer.android.com/guide/playcore/in-app-updates/kotlin-java#flexible) or
an [immediate update](https://developer.android.com/guide/playcore/in-app-updates/kotlin-java#immediate).

### Configure an update with AppUpdateOptions

[`AppUpdateOptions`](https://developer.android.com/reference/com/google/android/play/core/appupdate/AppUpdateOptions) contains an `AllowAssetPackDeletion` field that defines
whether the update is allowed to clear [asset packs](https://developer.android.com/guide/app-bundle/asset-delivery) in case of limited
device storage. This field is set to `false` by default, but you can use the
[`setAllowAssetPackDeletion()`](https://developer.android.com/reference/com/google/android/play/core/appupdate/AppUpdateOptions.Builder#setallowassetpackdeletion) method to set it to `true` instead:  

### Kotlin

```kotlin
appUpdateManager.startUpdateFlowForResult(
    // Pass the intent that is returned by 'getAppUpdateInfo()'.
    appUpdateInfo,
    // an activity result launcher registered via registerForActivityResult
    activityResultLauncher,
    // Or pass 'AppUpdateType.FLEXIBLE' to newBuilder() for
    // flexible updates.
    AppUpdateOptions.newBuilder(AppUpdateType.IMMEDIATE)
        .setAllowAssetPackDeletion(true)
        .build())
```

### Java

```java
appUpdateManager.startUpdateFlowForResult(
    // Pass the intent that is returned by 'getAppUpdateInfo()'.
    appUpdateInfo,
    // an activity result launcher registered via registerForActivityResult
    activityResultLauncher,
    // Or pass 'AppUpdateType.FLEXIBLE' to newBuilder() for
    // flexible updates.
    AppUpdateOptions.newBuilder(AppUpdateType.IMMEDIATE)
        .setAllowAssetPackDeletion(true)
        .build());
```
| **Caution:** Use the `AllowAssetPackDeletion` API option with care to avoid accidentally deleting assets. Before setting this option to `true`, check whether the update is allowed with this option set to `false`.

### Get a callback for update status

After starting an update, registered activity result launcher callback gets the
confirmation dialog result:  

### Kotlin

```kotlin
registerForActivityResult(StartIntentSenderForResult()) { result: ActivityResult ->
    // handle callback
    if (result.resultCode != RESULT_OK) {
        log("Update flow failed! Result code: " + result.resultCode);
        // If the update is canceled or fails,
        // you can request to start the update again.
    }
}
```

### Java

```java
registerForActivityResult(
    new ActivityResultContracts.StartIntentSenderForResult(),
    new ActivityResultCallback<ActivityResult>() {
        @Override
        public void onActivityResult(ActivityResult result) {
            // handle callback
            if (result.getResultCode() != RESULT_OK) {
                log("Update flow failed! Result code: " + result.getResultCode());
                // If the update is canceled or fails,
                // you can request to start the update again.
            }
        }
    });
```

There are several values you might receive from the `onActivityResult()`
callback:

- [`RESULT_OK`](https://developer.android.com/reference/android/app/Activity#RESULT_OK): The user has accepted the update. For immediate updates, you might not receive this callback because the update should already be finished by the time control is given back to your app.
- [`RESULT_CANCELED`](https://developer.android.com/reference/android/app/Activity#RESULT_CANCELED): The user has denied or canceled the update.
- [`ActivityResult.RESULT_IN_APP_UPDATE_FAILED`](https://developer.android.com/reference/com/google/android/play/core/install/model/ActivityResult#RESULT_IN_APP_UPDATE_FAILED): Some other error prevented either the user from providing consent or the update from proceeding.

## Handle a flexible update

When you start a flexible update, a dialog first appears to the user to request
consent. If the user consents, then the download starts in the background, and
the user can continue to interact with your app. This section describes how to
monitor and complete a flexible in-app update.

### Monitor the flexible update state

After the download begins for a flexible update, your app needs to monitor the
update state to know when the update can be installed and to display the
progress in your app's UI.

You can monitor the state of an update in progress by registering a listener for
install status updates. You can also provide a progress bar in the app's UI to
inform users of the download's progress.  

### Kotlin

```kotlin
// Create a listener to track request state updates.
val listener = InstallStateUpdatedListener { state ->
    // (Optional) Provide a download progress bar.
    if (state.installStatus() == InstallStatus.DOWNLOADING) {
      val bytesDownloaded = state.bytesDownloaded()
      val totalBytesToDownload = state.totalBytesToDownload()
      // Show update progress bar.
    }
    // Log state or install the update.
}

// Before starting an update, register a listener for updates.
appUpdateManager.registerListener(listener)

// Start an update.

// When status updates are no longer needed, unregister the listener.
appUpdateManager.unregisterListener(listener)
```

### Java

```java
// Create a listener to track request state updates.
InstallStateUpdatedListener listener = state -> {
  // (Optional) Provide a download progress bar.
  if (state.installStatus() == InstallStatus.DOWNLOADING) {
      long bytesDownloaded = state.bytesDownloaded();
      long totalBytesToDownload = state.totalBytesToDownload();
      // Implement progress bar.
  }
  // Log state or install the update.
};

// Before starting an update, register a listener for updates.
appUpdateManager.registerListener(listener);

// Start an update.

// When status updates are no longer needed, unregister the listener.
appUpdateManager.unregisterListener(listener);
```

### Install a flexible update

When you detect the `InstallStatus.DOWNLOADED` state, you need to restart the
app to install the update.

Unlike with immediate updates, Google Play does not automatically trigger an app
restart for a flexible update. This is because during a flexible update, the
user has an expectation to continue interacting with the app until they decide
that they want to install the update.

It is recommended that you provide a notification (or some other UI indication)
to inform the user that the update is ready to install and request confirmation
before restarting the app.

The following example demonstrates implementing a [Material Design snackbar](https://material.io/design/components/snackbars.html)
that requests confirmation from the user to restart the app:  

### Kotlin

```kotlin
val listener = { state ->
    if (state.installStatus() == InstallStatus.DOWNLOADED) {
        // After the update is downloaded, show a notification
        // and request user confirmation to restart the app.
        popupSnackbarForCompleteUpdate()
    }
    ...
}

// Displays the snackbar notification and call to action.
fun popupSnackbarForCompleteUpdate() {
    Snackbar.make(
        findViewById(R.id.activity_main_layout),
        "An update has just been downloaded.",
        Snackbar.LENGTH_INDEFINITE
    ).apply {
        setAction("RESTART") { appUpdateManager.completeUpdate() }
        setActionTextColor(resources.getColor(R.color.snackbar_action_text_color))
        show()
    }
}
```

### Java

```java
InstallStateUpdatedListener listener = state -> {
    if (state.installStatus() == InstallStatus.DOWNLOADED) {
        // After the update is downloaded, show a notification
        // and request user confirmation to restart the app.
        popupSnackbarForCompleteUpdate();
    }
    ...
};

// Displays the snackbar notification and call to action.
private void popupSnackbarForCompleteUpdate() {
  Snackbar snackbar =
      Snackbar.make(
          findViewById(R.id.activity_main_layout),
          "An update has just been downloaded.",
          Snackbar.LENGTH_INDEFINITE);
  snackbar.setAction("RESTART", view -> appUpdateManager.completeUpdate());
  snackbar.setActionTextColor(
      getResources().getColor(R.color.snackbar_action_text_color));
  snackbar.show();
}
```

When you call [`appUpdateManager.completeUpdate()`](https://developer.android.com/reference/com/google/android/play/core/appupdate/AppUpdateManager#completeUpdate()) in the foreground, the
platform displays a full-screen UI that restarts the app in the background.
After the platform installs the update, your app restarts into its main
activity.

If you instead call `completeUpdate()` when your app is [in the background](https://developer.android.com/guide/background#definition),
the update is installed silently without obscuring the device UI.

Whenever the user brings your app to the foreground, check whether your app has
an update waiting to be installed. If your app has an update in the `DOWNLOADED`
state, prompt the user to install the update. Otherwise, the update data
continues to occupy the user's device storage.  

### Kotlin

```kotlin
// Checks that the update is not stalled during 'onResume()'.
// However, you should execute this check at all app entry points.
override fun onResume() {
    super.onResume()

    appUpdateManager
        .appUpdateInfo
        .addOnSuccessListener { appUpdateInfo ->
            ...
            // If the update is downloaded but not installed,
            // notify the user to complete the update.
            if (appUpdateInfo.installStatus() == InstallStatus.DOWNLOADED) {
                popupSnackbarForCompleteUpdate()
            }
        }
}
```

### Java

```java
// Checks that the update is not stalled during 'onResume()'.
// However, you should execute this check at all app entry points.
@Override
protected void onResume() {
  super.onResume();

  appUpdateManager
      .getAppUpdateInfo()
      .addOnSuccessListener(appUpdateInfo -> {
              ...
              // If the update is downloaded but not installed,
              // notify the user to complete the update.
              if (appUpdateInfo.installStatus() == InstallStatus.DOWNLOADED) {
                  popupSnackbarForCompleteUpdate();
              }
          });
}
```

## Handle an immediate update

When you start an immediate update and the user consents to begin the update,
Google Play displays the update progress on top of your app's UI throughout the
entire duration of the update. If the user closes or terminates your app during
the update, the update should continue to download and install in the background
without additional user confirmation.

However, when your app returns to the foreground, you should confirm that the
update is not stalled in the
[`UpdateAvailability.DEVELOPER_TRIGGERED_UPDATE_IN_PROGRESS`](https://developer.android.com/reference/com/google/android/play/core/install/model/UpdateAvailability#DEVELOPER_TRIGGERED_UPDATE_IN_PROGRESS) state. If the
update is stalled in this state, resume the update:  

### Kotlin

```kotlin
// Checks that the update is not stalled during 'onResume()'.
// However, you should execute this check at all entry points into the app.
override fun onResume() {
    super.onResume()

    appUpdateManager
        .appUpdateInfo
        .addOnSuccessListener { appUpdateInfo ->
            ...
            if (appUpdateInfo.updateAvailability()
                == UpdateAvailability.DEVELOPER_TRIGGERED_UPDATE_IN_PROGRESS
            ) {
                // If an in-app update is already running, resume the update.
                appUpdateManager.startUpdateFlowForResult(
                  appUpdateInfo,
                  activityResultLauncher,
                  AppUpdateOptions.newBuilder(AppUpdateType.IMMEDIATE).build())
            }
        }
}
```

### Java

```java
// Checks that the update is not stalled during 'onResume()'.
// However, you should execute this check at all entry points into the app.
@Override
protected void onResume() {
  super.onResume();

  appUpdateManager
      .getAppUpdateInfo()
      .addOnSuccessListener(
          appUpdateInfo -> {
            ...
            if (appUpdateInfo.updateAvailability()
                == UpdateAvailability.DEVELOPER_TRIGGERED_UPDATE_IN_PROGRESS) {
                // If an in-app update is already running, resume the update.
                appUpdateManager.startUpdateFlowForResult(
                  appUpdateInfo,
                  activityResultLauncher,
                  AppUpdateOptions.newBuilder(AppUpdateType.IMMEDIATE).build());
            }
          });
}
```

The update flow returns a result as described in the reference documentation for
[`startUpdateFlowForResult()`](https://developer.android.com/reference/com/google/android/play/core/appupdate/AppUpdateManager#startUpdateFlowForResult(com.google.android.play.core.appupdate.AppUpdateInfo,%20android.app.Activity,%20com.google.android.play.core.appupdate.AppUpdateOptions,%20int)). In particular, your app should be able to
handle cases where a user declines the update or cancels the download. When the
user performs either of these actions, the Google Play UI closes. Your app
should determine the best way to proceed.

If possible, let the user continue without the update and prompt them again
later. If your app can't function without the update, consider displaying an
informative message before restarting the update flow or prompting the user to
close the app. That way, the user understands that they can relaunch your app
when they're ready to install the required update.

## Next steps

[Test your app's in-app updates](https://developer.android.com/guide/playcore/in-app-updates/test) to verify that your integration is working
correctly.