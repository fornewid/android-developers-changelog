---
title: https://developer.android.com/guide/playcore/feature-delivery/on-demand
url: https://developer.android.com/guide/playcore/feature-delivery/on-demand
source: md.txt
---

Feature modules allow you to separate certain features and resources
from the base module of your app and include them in your app bundle. Through
Play Feature Delivery, users can, for example, later download and install those
components on demand after they've already installed the base APK of your app.

For example, consider a text messaging app that includes functionality for
capturing and sending picture messages, but only a small percentage of users
send picture messages. It may make sense to include picture messaging as a
downloadable feature module. That way, the initial app download is
smaller for all users and only those users who send picture messages need to
download that additional component.

Keep in mind, this type of modularization requires more effort and possibly
refactoring your app's existing code, so consider carefully which of your
app's features would benefit the most from being available to users on demand.
To better understand optimal use cases and guidelines for on demand features,
read [UX best practices for on demand delivery](https://developer.android.com/studio/projects/dynamic-delivery/ux-guidelines).

If you want to gradually modularize app features over time, without
enabling advanced delivery options, such as on demand deliver, instead
[configure install-time delivery](https://developer.android.com/studio/projects/dynamic-delivery/at-install-delivery).

This page helps you add a feature module to your app project and
configure it for on demand delivery. Before you begin, make sure you're
using [Android Studio 3.5](https://developer.android.com/studio) or higher and Android Gradle Plugin 3.5.0
or higher.

## Configure a new module for on demand delivery

The easiest way to create a new feature module is by using
[Android Studio 3.5](https://developer.android.com/studio) or higher.
Because feature modules have an
inherent dependency on the base app module, you can add them only to existing
app projects.

To add a feature module to your app project using Android Studio,
proceed as follows:

1. If you haven't already done so, open your app project in the IDE.
2. Select **File \> New \> New Module** from the menu bar.
3. In the **Create New Module** dialog, select **Dynamic Feature Module** and click **Next**.
4. In the **Configure your new module** section, complete the following:
   1. Select the **Base application module** for your app project from the dropdown menu.
   2. Specify a **Module name** . The IDE uses this name to identify the module as a Gradle subproject in your [Gradle settings file](https://developer.android.com/studio/build#settings-file). When you build your app bundle, Gradle uses the last element of the subproject name to inject the `<manifest split>` attribute in the [feature module's manifest](https://developer.android.com/guide/playcore/feature-delivery#feature-module-manifest).
   3. Specify the module's **package name**. By default, Android Studio suggests a package name that combines the root package name of the base module and the module name you specified in the previous step.
   4. Select the **Minimum API level** you want the module to support. This value should match that of the base module.
5. Click **Next**.
6. In the **Module Download Options** section, complete the following:

   1. Specify the **Module title** using up to 50 characters. The platform
      uses this title to identify the module to users when, for example,
      confirming whether the user wants to download the module. For this
      reason, your app's base module must include the module title as a
      [string resource](https://developer.android.com/guide/topics/resources/string-resource), which you
      can translate. When creating the module using Android Studio, the IDE
      adds the string resource to the base module for you and injects the
      following entry in the feature module's manifest:

          <dist:module
              ...
              dist:title="@string/feature_title">
          </dist:module>

      | **Note:** If you enable resource shrinking, such as for your release builds, the shrinker may remove the module title string resource if code in your base module does not reference it. To make sure the string resource remains in the build output, include the resource in a [custom resource keep file](https://developer.android.com/studio/build/shrink-code#keep-resources).
   2. In the dropdown menu under **Install-time inclusion** , select **Do not
      include module at install-time**. Android Studio injects the
      following in the module's manifest to reflect your choice:

          <dist:module ... >
            <dist:delivery>
                <dist:on-demand/>
            </dist:delivery>
          </dist:module>

   3. Check the box next to **Fusing** if you want this module to be available
      to devices running Android 4.4 (API level 20) and lower and included in
      multi-APKs. This means you can enable on demand behavior for this module
      and disable fusing to omit it from devices that don't support
      downloading and installing split APKs. Android Studio injects the
      following in the module's manifest to reflect your choice:

          <dist:module ...>
              <dist:fusing dist:include="true | false" />
          </dist:module>

7. Click **Finish**.

After Android Studio finishes creating your module, inspect its contents
yourself from the **Project** pane (select **View \> Tool Windows \> Project**
from the menu bar). The default code, resources, and organization should be
similar to those of the standard app module.

Next, you will need to implement the on demand install functionality using the Play Feature Delivery library.

## Include the Play Feature Delivery Library in your project

Before you can start, you need to first
[add the Play Feature Delivery Library](https://developer.android.com/guide/playcore#java-kotlin-feature-delivery) to your project.

## Request an on demand module

When your app needs to use a feature module, it can request one while
it's in the foreground through the
[`SplitInstallManager`](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager)
class. When making a
request, your app needs to specify the name of the module as defined by the
`split` element in the target module's manifest. When you
[create a feature module](https://developer.android.com/guide/app-bundle/play-feature-delivery)
using Android Studio, the build system uses the **Module name** you provide
to inject this property into the module's manifest at compile time.
For more information, read about the
[feature module manifests](https://developer.android.com/guide/playcore/feature-delivery#feature-module-manifest).

For example, consider an app that has an on demand module to capture and send
picture messages using the device's camera, and this on demand module
specifies `split="pictureMessages"` in its manifest. The
following sample uses `SplitInstallManager` to request the `pictureMessages`
module (along with an additional module for some promotional filters):  

### Kotlin

```kotlin
// Creates an instance of https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager.
val splitInstallManager = SplitInstallManagerFactory.create(context)

// Creates a request to install a module.
val request =
    SplitInstallRequest
        .newBuilder()
        // You can download multiple on demand modules per
        // request by invoking the following method for each
        // module you want to install.
        .addModule("pictureMessages")
        .addModule("promotionalFilters")
        .build()

splitInstallManager
    // Submits the request to install the module through the
    // asynchronous startInstall() task. Your app needs to be
    // in the foreground to submit the request.
    .startInstall(request)
    // You should also be able to gracefully handle
    // request state changes and errors. To learn more, go to
    // the section about how to https://developer.android.com/guide/playcore/feature-delivery/on-demand#monitor_requests.
    .addOnSuccessListener { sessionId -> ... }
    .addOnFailureListener { exception ->  ... }
```

### Java

```java
// Creates an instance of https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager.
SplitInstallManager splitInstallManager =
    SplitInstallManagerFactory.create(context);

// Creates a request to install a module.
SplitInstallRequest request =
    SplitInstallRequest
        .newBuilder()
        // You can download multiple on demand modules per
        // request by invoking the following method for each
        // module you want to install.
        .addModule("pictureMessages")
        .addModule("promotionalFilters")
        .build();

splitInstallManager
    // Submits the request to install the module through the
    // asynchronous startInstall() task. Your app needs to be
    // in the foreground to submit the request.
    .startInstall(request)
    // You should also be able to gracefully handle
    // request state changes and errors. To learn more, go to
    // the section about how to https://developer.android.com/guide/playcore/feature-delivery/on-demand#monitor_requests.
    .addOnSuccessListener(sessionId -> { ... })
    .addOnFailureListener(exception -> { ... });
```

When your app requests an on demand module, the Play Feature Delivery Library employs a
"fire-and-forget" strategy. That is, it sends the request to download the
module to the platform, but it does not monitor whether the installation
succeeded. To move the user journey forward after
installation or gracefully handle errors, make sure you [monitor the request
state](https://developer.android.com/guide/playcore/feature-delivery/on-demand#monitor_requests).


**Note:** It's okay to request a
feature module that's already installed on the device. The API
instantly considers the request as completed if it detects the module is already
installed. Additionally, after a module is installed, Google Play keeps it updated
automatically. That is, when you upload a new version of your app bundle, the platform
updates all installed APKs that belong to your app. For more information, read
[Manage app updates](https://developer.android.com/guide/app-bundle/configure-base#manage_app_updates).

To have access to the module's code and resources, your app needs to
[enable SplitCompat](https://developer.android.com/guide/playcore/feature-delivery/on-demand#access_downloaded_modules). Note that SplitCompat is not
required for Android Instant Apps.

### Defer installation of on demand modules

If you do not need your app to immediately download and install an on demand
module, you can defer installation for when the app is in the background. For
example, if you want to preload some promotional material for a later launch of
your app.

You can specify a module to be download later using the
[`deferredInstall()`](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager#deferredinstall)
method, as shown below. And, unlike
[`SplitInstallManager.startInstall()`](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager#startinstall),
your app does not need to be in the foreground to initiate a request for a
deferred installation.  

### Kotlin

```kotlin
// Requests an on demand module to be downloaded when the app enters
// the background. You can specify more than one module at a time.
splitInstallManager.deferredInstall(listOf("promotionalFilters"))
```

### Java

```java
// Requests an on demand module to be downloaded when the app enters
// the background. You can specify more than one module at a time.
splitInstallManager.deferredInstall(Arrays.asList("promotionalFilters"));
```

Requests for deferred installs are best-effort and you cannot track their
progress. So, before trying to access a module you have specified for deferred
installation, you should
[check that the module has been installed](https://developer.android.com/guide/playcore/feature-delivery/on-demand#manage_installed_modules). If you
need the module to be available immediately, instead use
`SplitInstallManager.startInstall()` to request it, as shown in the previous
section.

## Monitor the request state

To be able to update a progress bar, fire an intent after
installation, or gracefully handle a request error, you need to listen for
state updates from the asynchronous `SplitInstallManager.startInstall()` task.
Before you can start receiving updates for your install request, register a
listener and get the session ID for the request, as shown below.  

### Kotlin

```kotlin
// Initializes a variable to later track the session ID for a given request.
var mySessionId = 0

// Creates a listener for request status updates.
val listener = SplitInstallStateUpdatedListener { state ->
    if (state.sessionId() == mySessionId) {
      // Read the status of the request to https://developer.android.com/guide/playcore/feature-delivery/on-demand#handle_state_updates.
    }
}

// Registers the listener.
splitInstallManager.registerListener(listener)

...

splitInstallManager
    .startInstall(request)
    // When the platform accepts your request to download
    // an on demand module, it binds it to the following session ID.
    // You use this ID to track further status updates for the request.
    .addOnSuccessListener { sessionId -> mySessionId = sessionId }
    // You should also add the following listener to handle any errors
    // processing the request.
    .addOnFailureListener { exception ->
        // https://developer.android.com/guide/playcore/feature-delivery/on-demand#handle_request_errors.
    }

// When your app no longer requires further updates, unregister the listener.
splitInstallManager.unregisterListener(listener)
```

### Java

```java
// Initializes a variable to later track the session ID for a given request.
int mySessionId = 0;

// Creates a listener for request status updates.
SplitInstallStateUpdatedListener listener = state -> {
    if (state.sessionId() == mySessionId) {
      // Read the status of the request to https://developer.android.com/guide/playcore/feature-delivery/on-demand#handle_state_updates.
    }
};

// Registers the listener.
splitInstallManager.registerListener(listener);

...

splitInstallManager
    .startInstall(request)
    // When the platform accepts your request to download
    // an on demand module, it binds it to the following session ID.
    // You use this ID to track further status updates for the request.
    .addOnSuccessListener(sessionId -> { mySessionId = sessionId; })
    // You should also add the following listener to handle any errors
    // processing the request.
    .addOnFailureListener(exception -> {
        // https://developer.android.com/guide/playcore/feature-delivery/on-demand#handle_request_errors.
    });

// When your app no longer requires further updates, unregister the listener.
splitInstallManager.unregisterListener(listener);
```

### Handle request errors

Keep in mind that on demand installation of feature modules can sometime fail,
just like app installation doesn't always succeed. Failure to install can be due
to issues like low device storage, no network connectivity, or the user not being
signed in to the Google Play Store. For suggestions on how to handle these situations
gracefully from the user's perspective, check out our
[UX guidelines for on demand delivery](https://developer.android.com/guide/playcore/feature-delivery/ux-guidelines).

Code-wise, you should handle failures downloading or installing a module
using `addOnFailureListener()`, as shown below:  

### Kotlin

```kotlin
splitInstallManager
    .startInstall(request)
    .addOnFailureListener { exception ->
        when ((exception as SplitInstallException).errorCode) {
            SplitInstallErrorCode.NETWORK_ERROR -> {
                // Display a message that requests the user to establish a
                // network connection.
            }
            SplitInstallErrorCode.ACTIVE_SESSIONS_LIMIT_EXCEEDED -> checkForActiveDownloads()
            ...
        }
    }

fun checkForActiveDownloads() {
    splitInstallManager
        // Returns a SplitInstallSessionState object for each active session as a List.
        .sessionStates
        .addOnCompleteListener { task ->
            if (task.isSuccessful) {
                // Check for active sessions.
                for (state in task.result) {
                    if (state.status() == SplitInstallSessionStatus.DOWNLOADING) {
                        // https://developer.android.com/guide/playcore/feature-delivery/on-demand#cancel_request, or request a https://developer.android.com/guide/playcore/feature-delivery/on-demand#deferred_install.
                    }
                }
            }
        }
}
```

### Java

```java
splitInstallManager
    .startInstall(request)
    .addOnFailureListener(exception -> {
        switch (((SplitInstallException) exception).getErrorCode()) {
            case SplitInstallErrorCode.NETWORK_ERROR:
                // Display a message that requests the user to establish a
                // network connection.
                break;
            case SplitInstallErrorCode.ACTIVE_SESSIONS_LIMIT_EXCEEDED:
                checkForActiveDownloads();
            ...
    });

void checkForActiveDownloads() {
    splitInstallManager
        // Returns a SplitInstallSessionState object for each active session as a List.
        .getSessionStates()
        .addOnCompleteListener( task -> {
            if (task.isSuccessful()) {
                // Check for active sessions.
                for (SplitInstallSessionState state : task.getResult()) {
                    if (state.status() == SplitInstallSessionStatus.DOWNLOADING) {
                        // https://developer.android.com/guide/playcore/feature-delivery/on-demand#cancel_request, or request a https://developer.android.com/guide/playcore/feature-delivery/on-demand#deferred_install.
                    }
                }
            }
        });
}
```

The table below describes the error states your app may need to handle:

| Error code | Description | Suggested action |
|---|---|---|
| ACTIVE_SESSIONS_LIMIT_EXCEEDED | The request is rejected because there is at least one existing request that is currently downloading. | Check if there are any requests that are still downloading, as shown in the sample above. |
| MODULE_UNAVAILABLE | Google Play is unable to find the requested module based on the current installed version of the app, device, and user's Google Play account. | If the user does not have access to the module, notify them. |
| INVALID_REQUEST | Google Play received the request, but the request is not valid. | Verify that the information included in the request is complete and accurate. |
| SESSION_NOT_FOUND | A session for a given session ID was not found. | If you're trying to monitor the state of a request by its session ID, make sure that the session ID is correct. |
| API_NOT_AVAILABLE | The Play Feature Delivery Library is not supported on the current device. That is, the device is not able to download and install features on demand. | For devices running Android 4.4 (API level 20) or lower, you should include feature modules at install time using the `dist:fusing` manifest property. To learn more, read about the [feature module manifest](https://developer.android.com/guide/playcore/feature-delivery#feature-module-manifest). |
| NETWORK_ERROR | The request failed because of a network error. | Prompt the user to either establish a network connection or change to a different network. |
| ACCESS_DENIED | The app is unable to register the request because of insufficient permissions. | This typically occurs when the app is in the background. Attempt the request when the app returns to the foreground. |
| INCOMPATIBLE_WITH_EXISTING_SESSION | The request contains one or more modules that have already been requested but have not yet been installed. | Either create a new request that does not include modules that your app has already requested, or wait for all currently requested modules to finish installing before retrying the request. Keep in mind, requesting a module that has already been installed does not resolve in an error. |
| SERVICE_DIED | The service responsible for handling the request has died. | Retry the request. Your `SplitInstallStateUpdatedListener` receives a `SplitInstallSessionState` with this error code, status `FAILED` and session ID `-1`. |
| INSUFFICIENT_STORAGE | The device does not have enough free storage to install the feature module. | Notify the user that they do not have enough storage to install this feature. |
| SPLITCOMPAT_VERIFICATION_ERROR, SPLITCOMPAT_EMULATION_ERROR, SPLITCOMPAT_COPY_ERROR | SplitCompat could not load the feature module. | These errors should automatically resolve themselves after the next app restart. |
| PLAY_STORE_NOT_FOUND | The Play Store app is not installed on the device. | Let the user know that the Play Store app is required to download this feature. |
| APP_NOT_OWNED | The app has not been installed by Google Play and the feature cannot be downloaded. This error can only occur for deferred installs. | If you want the user to acquire the app on Google Play, use `startInstall()` which can obtain the necessary [user confirmation](https://developer.android.com/guide/playcore/feature-delivery/on-demand#obtain_confirmation). |
| INTERNAL_ERROR | An internal error occurred within the Play Store. | Retry the request. |

If a user requests downloading an on demand module and an error occurs,
consider displaying a dialog that provides two options for the user: **Try
again** (which attempts the request again) and **Cancel** (which abandons the
request). For additional support, you should also provide **Help** link that
directs users to the
[Google Play Help center](https://support.google.com/googleplay/answer/7513003).
| **Note:** When testing your app, if you see `onError(-2)`, it might be because you have not yet uploaded your app to Google Play. To test on demand functionality of your app, you must either [share your app with a URL](https://support.google.com/googleplay/android-developer/answer/9303479) or [set up an open, closed, or internal test](https://support.google.com/googleplay/android-developer/answer/3131213).

### Handle state updates

After you register a listener and record the session ID for your request,
use [`StateUpdatedListener.onStateUpdate()`](https://developer.android.com/reference/com/google/android/play/core/listener/StateUpdatedListener#onStateUpdate(StateT))
to handle state changes, as shown below.  

### Kotlin

```kotlin
override fun onStateUpdate(state : SplitInstallSessionState) {
    if (state.status() == SplitInstallSessionStatus.FAILED
        && state.errorCode() == SplitInstallErrorCode.SERVICE_DIED) {
       // Retry the request.
       return
    }
    if (state.sessionId() == mySessionId) {
        when (state.status()) {
            SplitInstallSessionStatus.DOWNLOADING -> {
              val totalBytes = state.totalBytesToDownload()
              val progress = state.bytesDownloaded()
              // Update progress bar.
            }
            SplitInstallSessionStatus.INSTALLED -> {

              // After a module is installed, you can start accessing its content or
              // https://developer.android.com/guide/components/intents-filters to start an activity in the installed module.
              // For other use cases, see https://developer.android.com/guide/playcore/feature-delivery/on-demand#access_installed_modules.

              // If the request is an on demand module for an Android Instant App
              // running on Android 8.0 (API level 26) or higher, you need to
              // https://developer.android.com/guide/playcore/feature-delivery/on-demand#aia_update_context using the SplitInstallHelper API.
            }
        }
    }
}
```

### Java

```java
@Override
public void onStateUpdate(SplitInstallSessionState state) {
    if (state.status() == SplitInstallSessionStatus.FAILED
        && state.errorCode() == SplitInstallErrorCode.SERVICE_DIES) {
       // Retry the request.
       return;
    }
    if (state.sessionId() == mySessionId) {
        switch (state.status()) {
            case SplitInstallSessionStatus.DOWNLOADING:
              int totalBytes = state.totalBytesToDownload();
              int progress = state.bytesDownloaded();
              // Update progress bar.
              break;

            case SplitInstallSessionStatus.INSTALLED:

              // After a module is installed, you can start accessing its content or
              // https://developer.android.com/guide/components/intents-filters to start an activity in the installed module.
              // For other use cases, see https://developer.android.com/guide/playcore/feature-delivery/on-demand#access_installed_modules.

              // If the request is an on demand module for an Android Instant App
              // running on Android 8.0 (API level 26) or higher, you need to
              // https://developer.android.com/guide/playcore/feature-delivery/on-demand#aia_update_context using the SplitInstallHelper API.
        }
    }
}
```

The possible states for your install request are described in the table below.

| Request state | Description | Suggested action |
|---|---|---|
| PENDING | The request has been accepted and the download should start soon. | Initialize UI components, such as a progress bar, to provide the user feedback on the download. |
| REQUIRES_USER_CONFIRMATION | The download requires user confirmation. Most commonly this status occurs if the app has not been installed through Google Play. | Prompt the user to confirm the feature download through Google Play. To learn more, go to the section about how to [obtain user confirmation](https://developer.android.com/guide/playcore/feature-delivery/on-demand#obtain_confirmation). |
| DOWNLOADING | Download is in progress. | If you provide a progress bar for the download, use the `SplitInstallSessionState.bytesDownloaded()` and `SplitInstallSessionState.totalBytesToDownload()` methods to update the UI (see the code sample above this table). |
| DOWNLOADED | The device has downloaded the module but installation has not yet begun. | Apps should [enable SplitCompat](https://developer.android.com/guide/playcore/feature-delivery/on-demand#access_downloaded_modules) to have access to downloaded modules and avoid seeing this state. This is required in order to access the feature module's code and resources. |
| INSTALLING | The device is currently installing the module. | Update the progress bar. This state is typically short. |
| INSTALLED | The module is installed on the device. | [Access code and resource in the module](https://developer.android.com/guide/playcore/feature-delivery/on-demand#access_installed_modules) to continue the user journey. If the module is for an Android Instant App running on Android 8.0 (API level 26) or higher, you need to use `splitInstallHelper` to [update app components with the new module](https://developer.android.com/guide/playcore/feature-delivery/on-demand#aia_update_context). |
| FAILED | The request failed before the module was installed on the device. | Prompt the user to either retry the request or cancel it. |
| CANCELING | The device is in the process of cancelling the request. | To learn more, go to the section about how to [cancel an install request](https://developer.android.com/guide/playcore/feature-delivery/on-demand#cancel_request). |
| CANCELED | The request has been cancelled. |   |

### Obtain user confirmation

In some cases, Google Play may require user confirmation before satisfying a
download request. For example, if your app has not been installed by Google
Play or if you are attempting a large download over mobile data. In such cases,
the status for the request reports `REQUIRES_USER_CONFIRMATION`, and your app
needs to obtain user confirmation before the device is able to download and
install the modules in the request. To obtain confirmation, your app should
prompt the user as follows:  

### Kotlin

```kotlin
override fun onSessionStateUpdate(state: SplitInstallSessionState) {
    if (state.status() == SplitInstallSessionStatus.REQUIRES_USER_CONFIRMATION) {
        // Displays a confirmation for the user to confirm the request.
        splitInstallManager.startConfirmationDialogForResult(
          state,
          // an activity result launcher registered via registerForActivityResult
          activityResultLauncher)
    }
    ...
 }
```

### Java

```java
@Override void onSessionStateUpdate(SplitInstallSessionState state) {
    if (state.status() == SplitInstallSessionStatus.REQUIRES_USER_CONFIRMATION) {
        // Displays a confirmation for the user to confirm the request.
        splitInstallManager.startConfirmationDialogForResult(
          state,
          // an activity result launcher registered via registerForActivityResult
          activityResultLauncher);
    }
    ...
 }
```

You can register an activity result launcher using the builtin
[`ActivityResultContracts.StartIntentSenderForResult`](https://developer.android.com/reference/androidx/activity/result/contract/ActivityResultContracts.StartIntentSenderForResult)
contract. See [Activity Result APIs](https://developer.android.com/training/basics/intents/result).

The status for the request is updated depending on the user response:

- If the user accepts the confirmation, the request status changes to `PENDING` and the download proceeds.
- If the user denies the confirmation, the request status changes to `CANCELED`.
- If the user does not make a selection before the dialog is destroyed, the request status remains as `REQUIRES_USER_CONFIRMATION`. Your app can prompt the user again to complete the request.

To receive a callback with the user's response, you can override the
ActivityResultCallback as shown below.  

### Kotlin

```kotlin
registerForActivityResult(StartIntentSenderForResult()) { result: ActivityResult -> {
        // Handle the user's decision. For example, if the user selects "Cancel",
        // you may want to disable certain functionality that depends on the module.
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
            // Handle the user's decision. For example, if the user selects "Cancel",
            // you may want to disable certain functionality that depends on the module.
        }
    });
```

### Cancel an install request

If your app needs to cancel a request before it is installed, it can invoke
the `cancelInstall()` method using the request's session ID, as shown below.  

### Kotlin

```kotlin
splitInstallManager
    // Cancels the request for the given session ID.
    .cancelInstall(mySessionId)
```

### Java

```java
splitInstallManager
    // Cancels the request for the given session ID.
    .cancelInstall(mySessionId);
```

## Access modules

To access code and resources from a downloaded module after it is downloaded,
your app needs to enable the
[SplitCompat Library](https://developer.android.com/reference/com/google/android/play/core/splitcompat/SplitCompat)
for both your app and each activity in the feature modules your app
downloads.

You should note, however, the platform experiences the following
restrictions to accessing contents of a module, for some time (days, in some
cases) after downloading the module:

- The platform can not apply any new manifest entries introduced by the module.
- The platform can not access the module's resources for system UI components, such as notifications. If you need to use such resources immediately, consider including those resource in the base module of your app.

### Enable SplitCompat

For your app to access code and resources from a downloaded module,
you need to enable SplitCompat using only one of the methods described in the
following sections.

After you enable SplitCompat for your app, you need to also [enable SplitCompat
for each activity](https://developer.android.com/guide/playcore/feature-delivery/on-demand#activity_splitcompat) in the feature modules you
want your app to have access to.

#### Declare SplitCompatApplication in the manifest

The simplest way to enable SplitCompat is to declare `SplitCompatApplication`
as the [`Application`](https://developer.android.com/reference/android/app/Application) subclass in
your app's manifest, as shown below:  

    <application
        ...
        android:name="com.google.android.play.core.splitcompat.SplitCompatApplication">
    </application>

After the app is installed on a device, you can access code and resources from
downloaded feature modules automatically.

#### Invoke SplitCompat at runtime

You can also enable SplitCompat in specific activities or services at runtime.
Enabling SplitCompat this way is required to launch activities included in
feature modules. To do this, override `attachBaseContext` as seen below.

If you have a custom [Application](https://developer.android.com/reference/android/app/Application) class,
have it instead extend
[`SplitCompatApplication`](https://developer.android.com/reference/com/google/android/play/core/splitcompat/SplitCompatApplication)
in order to enable SplitCompat for your app, as shown below:  

### Kotlin

```kotlin
class MyApplication : SplitCompatApplication() {
    ...
}
```

### Java

```java
public class MyApplication extends SplitCompatApplication {
    ...
}
```

`SplitCompatApplication` simply overrides `ContextWrapper.attachBaseContext()`
to include `SplitCompat.install(Context applicationContext)`. If you don't
want your `Application` class to
extend `SplitCompatApplication`, you can override the `attachBaseContext()`
method manually, as follows:  

### Kotlin

```kotlin
override fun attachBaseContext(base: Context) {
    super.attachBaseContext(base)
    // Emulates installation of future on demand modules using SplitCompat.
    SplitCompat.install(this)
}
```

### Java

```java
@Override
protected void attachBaseContext(Context base) {
    super.attachBaseContext(base);
    // Emulates installation of future on demand modules using SplitCompat.
    SplitCompat.install(this);
}
```

If your on demand module is compatible
with both instant apps and installed apps, you can invoke SplitCompat
conditionally, as follows:  

### Kotlin

```kotlin
override fun attachBaseContext(base: Context) {
    super.attachBaseContext(base)
    if (!InstantApps.isInstantApp(this)) {
        SplitCompat.install(this)
    }
}
```

### Java

```java
@Override
protected void attachBaseContext(Context base) {
    super.attachBaseContext(base);
    if (!InstantApps.isInstantApp(this)) {
        SplitCompat.install(this);
    }
}
```

### Enable SplitCompat for module activities

After you enable SplitCompat for your base app, you need to enable SplitCompat
for each activity that your app downloads in a feature module. To do so,
use the `SplitCompat.installActivity()` method, as follows:  

### Kotlin

```kotlin
override fun attachBaseContext(base: Context) {
    super.attachBaseContext(base)
    // Emulates installation of on demand modules using SplitCompat.
    SplitCompat.installActivity(this)
}
```

### Java

```java
@Override
protected void attachBaseContext(Context base) {
    super.attachBaseContext(base);
    // Emulates installation of on demand modules using SplitCompat.
    SplitCompat.installActivity(this);
}
```

## Access components defined in feature modules

### Start an activity defined in a feature module

You can launch activities defined in feature modules using
[`startActivity()`](https://developer.android.com/reference/android/app/Activity#startActivity(android.content.Intent))
after enabling SplitCompat.  

### Kotlin

```kotlin
startActivity(Intent()
  .setClassName("com.package", "com.package.module.MyActivity")
  .setFlags(...))
```

### Java

```java
startActivity(new Intent()
  .setClassName("com.package", "com.package.module.MyActivity")
  .setFlags(...));
```

The first parameter to `setClassName` is the package name of the app and the
second parameter is the full class name of the activity.

When you have an activity in a feature module you downloaded on-demand, you must
[enable SplitCompat in the activity](https://developer.android.com/guide/playcore/feature-delivery/on-demand#activity_splitcompat).

### Start a service defined in a feature module

You can launch services defined in feature modules using
[`startService()`](https://developer.android.com/reference/android/content/Context#startService(android.content.Intent))
after enabling SplitCompat.  

### Kotlin

```kotlin
startService(Intent()
  .setClassName("com.package", "com.package.module.MyService")
  .setFlags(...))
```

### Java

```java
startService(new Intent()
  .setClassName("com.package", "com.package.module.MyService")
  .setFlags(...));
```

### Export a component defined in a feature module

You should not include exported Android components inside optional modules.

The build system merges manifest entries for all modules into the base module;
if an optional module contained an exported component, it would be accessible
even before the module is installed and can cause a crash due to missing code
when invoked from another app.

This is not a problem for internal components; they are accessed only
by the app, so the app can
[check that the module is installed](https://developer.android.com/guide/playcore/feature-delivery/on-demand#manage_installed_modules) before accessing
the component.

If you need an exported component, and you want its content to be in an optional
module, consider implementing a proxy pattern.
You can do that by adding a proxy exported component in the base;
when accessed, the proxy component can check for the presence of the module that
contains the content. If the module is present, the proxy
component can start the internal component from the module via an `Intent`,
relaying the intent from the caller app. If the module is not present, the
component can download the module or return an appropriate error message to the
caller app.

## Access code and resources from installed modules

If you [enable SplitCompat](https://developer.android.com/guide/playcore/feature-delivery/on-demand#access_downloaded_modules) for your base
application context and the activities in your feature module, you can use the
code and resources from a feature module as if it were a part of the base APK,
once the optional module is installed.

### Access code from a different module

#### Access base code from a module

Code that is inside your base module can be used directly by other modules.
You don't need to do anything special; just import and use the classes you need.

#### Access module code from another module

An object or class inside a module cannot be statically accessed from another
module directly, but it can be accessed indirectly, using reflection.

You should be wary of how often this happens, due to the performance costs
of reflection. For complex use cases, use dependency injection frameworks like
[Dagger 2](https://dagger.dev/) to guarantee a single reflection call per
application lifetime.

To simplify the interactions with the object after instantiation, it is
recommended to define an interface in the base module and its implementation in
the feature module. For instance:  

### Kotlin

```kotlin
// In the base module
interface MyInterface {
  fun hello(): String
}

// In the feature module
object MyInterfaceImpl : MyInterface {
  override fun hello() = "Hello"
}

// In the base module, where we want to access the feature module code
val stringFromModule = (Class.forName("com.package.module.MyInterfaceImpl")
    .kotlin.objectInstance as MyInterface).hello();
```

### Java

```java
// In the base module
public interface MyInterface {
  String hello();
}

// In the feature module
public class MyInterfaceImpl implements MyInterface {
  @Override
  public String hello() {
    return "Hello";
  }
}

// In the base module, where we want to access the feature module code
String stringFromModule =
   ((MyInterface) Class.forName("com.package.module.MyInterfaceImpl").getConstructor().newInstance()).hello();
```

### Access resources and assets from a different module

Once a module is installed, you can access resources and assets within the
module in the standard way, with two caveats:

- If you are accessing a resource from a different module, the module will not have access to the resource identifier, though the resource can still be accessed by name. Note that the package to use to reference the resource is the package of the module where the resource is defined.
- If you want to access assets or resources that exist in a newly installed module from a different installed module of your app, you must do so [using the
  application context](https://developer.android.com/guide/topics/resources/providing-resources#Accessing). The context of the component that's trying to access the resources will not yet be updated. Alternatively, you can recreate that component (for instance calling [Activity.recreate()](https://developer.android.com/reference/android/app/Activity#recreate())) or [reinstall SplitCompat](https://developer.android.com/guide/playcore/feature-delivery/on-demand#activity_splitcompat) on it after the feature module installation.

### Load native code in an app using on-demand delivery

We recommend using [ReLinker](https://github.com/KeepSafe/ReLinker) to load all
your native libraries when using on-demand delivery of feature modules.
ReLinker fixes an issue in loading native libraries after the installation of a
feature module. You can learn more about ReLinker in the
[Android JNI Tips](https://developer.android.com/training/articles/perf-jni#native-libraries).

### Load native code from an optional module

Once a split is installed, we recommend loading its native code through
[ReLinker](https://github.com/KeepSafe/ReLinker).
For instant apps you should use [this special method](https://developer.android.com/guide/playcore/feature-delivery/on-demand#load_native_libs).

If you are using `System.loadLibrary()` to load your native code and your native
library has a dependency on another library in the module, you must manually
load that other library first.
If you are using ReLinker, the equivalent operation is
`Relinker.recursively().loadLibrary()`.

If you are using `dlopen()` in native code to load a library defined in an
optional module, it will not work with relative library paths.
The best solution is to retrieve the absolute path of the library from Java code
via `ClassLoader.findLibrary()` and then use it in your `dlopen()` call.
Do this before entering the native code or use a JNI call from your
native code into Java.

### Access installed Android Instant Apps

After an Android Instant App module reports as `INSTALLED`, you can access its
code and resources using a refreshed app
[Context](https://developer.android.com/reference/android/content/Context). A
context that your app creates *before* installing a module (for example, one
that's already stored in a variable) does not contain the content of the new
module. But a fresh context does---this can be obtained, for example, using
[`createPackageContext`](https://developer.android.com/reference/android/content/Context#createPackageContext(java.lang.String,%20int)).  

### Kotlin

```kotlin
// Generate a new context as soon as a request for a new module
// reports as INSTALLED.
override fun onStateUpdate(state: SplitInstallSessionState ) {
    if (state.sessionId() == mySessionId) {
        when (state.status()) {
            ...
            SplitInstallSessionStatus.INSTALLED -> {
                val newContext = context.createPackageContext(context.packageName, 0)
                // If you use https://developer.android.com/reference/android/content/res/AssetManager to access your app's raw asset files, you'll need
                // to generate a new AssetManager instance from the updated context.
                val am = newContext.assets
            }
        }
    }
}
```

### Java

```java
// Generate a new context as soon as a request for a new module
// reports as INSTALLED.
@Override
public void onStateUpdate(SplitInstallSessionState state) {
    if (state.sessionId() == mySessionId) {
        switch (state.status()) {
            ...
            case SplitInstallSessionStatus.INSTALLED:
                Context newContext = context.createPackageContext(context.getPackageName(), 0);
                // If you use https://developer.android.com/reference/android/content/res/AssetManager to access your app's raw asset files, you'll need
                // to generate a new AssetManager instance from the updated context.
                AssetManager am = newContext.getAssets();
        }
    }
}
```

#### Android Instant Apps on Android 8.0 and higher

When requesting an on demand module for an Android Instant App on Android 8.0
(API level 26) and higher, after an install request reports as `INSTALLED`, you
need to update the app with the context of the new module through a call to
[`SplitInstallHelper.updateAppInfo(Context context)`](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallHelper#updateAppInfo(android.content.Context)).
Otherwise, the app is not yet aware of the module's code
and resources. After updating the app's metadata, you should load the module's
contents during the next main thread event by invoking a new
[`Handler`](https://developer.android.com/reference/android/os/Handler), as shown below:  

### Kotlin

```kotlin
override fun onStateUpdate(state: SplitInstallSessionState ) {
    if (state.sessionId() == mySessionId) {
        when (state.status()) {
            ...
            SplitInstallSessionStatus.INSTALLED -> {
                // You need to perform the following only for Android Instant Apps
                // running on Android 8.0 (API level 26) and higher.
                if (BuildCompat.isAtLeastO()) {
                    // Updates the app's context with the code and resources of the
                    // installed module.
                    SplitInstallHelper.updateAppInfo(context)
                    Handler().post {
                        // Loads contents from the module using https://developer.android.com/reference/android/content/res/AssetManager
                        val am = context.assets
                        ...
                    }
                }
            }
        }
    }
}
```

### Java

```java
@Override
public void onStateUpdate(SplitInstallSessionState state) {
    if (state.sessionId() == mySessionId) {
        switch (state.status()) {
            ...
            case SplitInstallSessionStatus.INSTALLED:
            // You need to perform the following only for Android Instant Apps
            // running on Android 8.0 (API level 26) and higher.
            if (BuildCompat.isAtLeastO()) {
                // Updates the app's context with the code and resources of the
                // installed module.
                SplitInstallHelper.updateAppInfo(context);
                new Handler().post(new Runnable() {
                    @Override public void run() {
                        // Loads contents from the module using https://developer.android.com/reference/android/content/res/AssetManager
                        AssetManager am = context.getAssets();
                        ...
                    }
                });
            }
        }
    }
}
```

#### Load C/C++ libraries

If you want to load C/C++ libraries from a module that the device has already
downloaded in an Instant App, use
[`SplitInstallHelper.loadLibrary(Context context, String libName)`](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallHelper#loadLibrary(android.content.Context,%20java.lang.String)),
as shown below:  

### Kotlin

```kotlin
override fun onStateUpdate(state: SplitInstallSessionState) {
    if (state.sessionId() == mySessionId) {
        when (state.status()) {
            SplitInstallSessionStatus.INSTALLED -> {
                // Updates the app's context as soon as a module is installed.
                val newContext = context.createPackageContext(context.packageName, 0)
                // To load C/C++ libraries from an installed module, use the following API
                // instead of System.load().
                SplitInstallHelper.loadLibrary(newContext, "my-cpp-lib")
                ...
            }
        }
    }
}
```

### Java

```java
public void onStateUpdate(SplitInstallSessionState state) {
    if (state.sessionId() == mySessionId) {
        switch (state.status()) {
            case SplitInstallSessionStatus.INSTALLED:
                // Updates the app's context as soon as a module is installed.
                Context newContext = context.createPackageContext(context.getPackageName(), 0);
                // To load C/C++ libraries from an installed module, use the following API
                // instead of System.load().
                SplitInstallHelper.loadLibrary(newContext, "my-cpp-lib");
                ...
        }
    }
}
```

### Known limitations

- It isn't possible to use Android WebView in an activity that accesses resources or assets from an optional module. This is due to an incompatibility between WebView and SplitCompat on Android API level 28 and lower.
- You can't cache Android `ApplicationInfo` objects, their contents, or objects that contain them within your app. You should always fetch these objects as needed from an app context. Caching such objects could cause the app to crash when installing a feature module.

## Manage installed modules

To check which feature modules are currently installed on the device,
you can call
[`SplitInstallManager.getInstalledModules()`](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager#getInstalledModules()),
which returns a `Set<String>` of the names of the installed modules, as shown
below.
**Note:** If you're developing an Android Instant App, this section does not apply to you.  

### Kotlin

```kotlin
val installedModules: Set<String> = splitInstallManager.installedModules
```

### Java

```java
Set<String> installedModules = splitInstallManager.getInstalledModules();
```

### Uninstall modules

You can request the device to uninstall modules by invoking
[`SplitInstallManager.deferredUninstall(List<String> moduleNames)`](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager#deferreduninstall),
as shown below.  

### Kotlin

```kotlin
// Specifies two feature modules for deferred uninstall.
splitInstallManager.deferredUninstall(listOf("pictureMessages", "promotionalFilters"))
```

### Java

```java
// Specifies two feature modules for deferred uninstall.
splitInstallManager.deferredUninstall(Arrays.asList("pictureMessages", "promotionalFilters"));
```

Module uninstalls do not occur immediately. That is,
the device uninstalls them in the background as needed to save storage space.
You can confirm that the device has
deleted a module by invoking
[`SplitInstallManager.getInstalledModules()`](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager#getinstalledmodules)
and inspecting the result, as described in the previous section.

## Download additional language resources

With app bundles, devices download only the code and resources they
require to run your app. So, for language resources, a user's device downloads
only your app's language resources that match the one or more languages currently
selected in the device's settings.

If you want your app to have access to additional language resources---for
example, to implement an in-app language picker, you can use the Play Feature Delivery
Library to download them on demand. The process is similar to that of
downloading a feature module, as shown below.  

### Kotlin

```kotlin
// Captures the user's preferred language and persists it
// through the app's SharedPreferences.
sharedPrefs.edit().putString(LANGUAGE_SELECTION, "fr").apply()
...

// Creates a request to download and install additional language resources.
val request = SplitInstallRequest.newBuilder()
        // Uses the addLanguage() method to include French language resources in the request.
        // Note that country codes are ignored. That is, if your app
        // includes resources for "fr-FR" and "fr-CA", resources for both
        // country codes are downloaded when requesting resources for "fr".
        .addLanguage(Locale.forLanguageTag(sharedPrefs.getString(LANGUAGE_SELECTION)))
        .build()

// Submits the request to install the additional language resources.
splitInstallManager.startInstall(request)
```

### Java

```java
// Captures the user's preferred language and persists it
// through the app's SharedPreferences.
sharedPrefs.edit().putString(LANGUAGE_SELECTION, "fr").apply();
...

// Creates a request to download and install additional language resources.
SplitInstallRequest request =
    SplitInstallRequest.newBuilder()
        // Uses the addLanguage() method to include French language resources in the request.
        // Note that country codes are ignored. That is, if your app
        // includes resources for "fr-FR" and "fr-CA", resources for both
        // country codes are downloaded when requesting resources for "fr".
        .addLanguage(Locale.forLanguageTag(sharedPrefs.getString(LANGUAGE_SELECTION)))
        .build();

// Submits the request to install the additional language resources.
splitInstallManager.startInstall(request);
```

The request is handled as if it were a request for a feature module. That is,
you can [monitor the request state](https://developer.android.com/guide/playcore/feature-delivery/on-demand#monitor_requests) like you normally would.

If your app doesn't require the additional language resources immediately, you
can defer the installation for when the app is in the background, as shown
below.  

### Kotlin

```kotlin
splitInstallManager.deferredLanguageInstall(
    Locale.forLanguageTag(sharedPrefs.getString(LANGUAGE_SELECTION)))
```

### Java

```java
splitInstallManager.deferredLanguageInstall(
    Locale.forLanguageTag(sharedPrefs.getString(LANGUAGE_SELECTION)));
```

### Access downloaded language resources

To gain access to downloaded language resources, your app needs to run the
`SplitCompat.installActivity()` method within the `attachBaseContext()` method
of each activity that requires access to those resources, as shown below.  

### Kotlin

```kotlin
override fun attachBaseContext(base: Context) {
  super.attachBaseContext(base)
  SplitCompat.installActivity(this)
}
```

### Java

```java
@Override
protected void attachBaseContext(Context base) {
  super.attachBaseContext(base);
  SplitCompat.installActivity(this);
}
```

For each activity you want to use language resources your app has downloaded,
update the base context and set a new locale through its
[`Configuration`](https://developer.android.com/reference/android/content/res/Configuration):  

### Kotlin

```kotlin
override fun attachBaseContext(base: Context) {
  val configuration = Configuration()
  configuration.setLocale(Locale.forLanguageTag(sharedPrefs.getString(LANGUAGE_SELECTION)))
  val context = base.createConfigurationContext(configuration)
  super.attachBaseContext(context)
  SplitCompat.install(this)
}
```

### Java

```java
@Override
protected void attachBaseContext(Context base) {
  Configuration configuration = new Configuration();
  configuration.setLocale(Locale.forLanguageTag(sharedPrefs.getString(LANGUAGE_SELECTION)));
  Context context = base.createConfigurationContext(configuration);
  super.attachBaseContext(context);
  SplitCompat.install(this);
}
```

In order for these changes to take effect, you have to recreate your activity
after the new language is installed and ready to use. You can use the
`Activity#recreate()` method.  

### Kotlin

```kotlin
when (state.status()) {
  SplitInstallSessionStatus.INSTALLED -> {
      // Recreates the activity to load resources for the new language
      // preference.
      activity.recreate()
  }
  ...
}
```

### Java

```java
switch (state.status()) {
  case SplitInstallSessionStatus.INSTALLED:
      // Recreates the activity to load resources for the new language
      // preference.
      activity.recreate();
  ...
}
```

### Uninstall additional language resources

Similar to feature modules, you can uninstall additional resources at
any time. Before requesting an uninstall, you may want to first determine which
languages are currently installed, as follows.  

### Kotlin

```kotlin
val installedLanguages: Set<String> = splitInstallManager.installedLanguages
```

### Java

```java
Set<String> installedLanguages = splitInstallManager.getInstalledLanguages();
```

You can then decide which languages to uninstall using the
`deferredLanguageUninstall()` method, as shown below.  

### Kotlin

```kotlin
splitInstallManager.deferredLanguageUninstall(
    Locale.forLanguageTag(sharedPrefs.getString(LANGUAGE_SELECTION)))
```

### Java

```java
splitInstallManager.deferredLanguageUninstall(
    Locale.forLanguageTag(sharedPrefs.getString(LANGUAGE_SELECTION)));
```

## Locally test module installs

The Play Feature Delivery Library allows you to locally test your app's ability to do the
following, without connecting to the Play Store:

- Request and monitor module installs.
- Handle install errors.
- Use [`SplitCompat`](https://developer.android.com/reference/com/google/android/play/core/splitcompat/SplitCompat) to [access modules](https://developer.android.com/guide/playcore/dynamic-delivery#access_downloaded_modules).

This page describes how to deploy your app's split APKs to your test device so
that Play Feature Delivery automatically uses those APKs to simulate requesting, downloading,
and installing modules from the Play Store.

Although you don't need to make any changes to your app's logic, you need to
meet the following requirements:

- Download and install the [latest version of `bundletool`](https://github.com/google/bundletool/releases). You need `bundletool` to build a new set of installable APKs from your app's bundle.

| **Note:** Play Feature Delivery Library currently doesn't support module uninstalls or deferred installs. To test this functionality, consider using [internal app sharing](https://support.google.com/googleplay/android-developer/answer/9303479).

### Build a set of APKs

If you haven't already done so, build your app's split APKs, as follows:

1. Build an app bundle for your app using one of the following methods:
   - Use Android Studio and the Android plugin for Gradle to [build and sign
     an Android App Bundle](https://developer.android.com/studio/publish/app-signing#sign-apk).
   - [Build your app bundle from the command line](https://developer.android.com/studio/build/building-cmdline#build_bundle).
2. Use `bundletool` to [generate a set of
   APKs](https://developer.android.com/studio/command-line/bundletool#generate_apks) for all device
   configurations with the following command:

   ```
   bundletool build-apks --local-testing
     --bundle my_app.aab
     --output my_app.apks
   ```

The `--local-testing` flag includes meta-data in your APKs' manifests that
lets the Play Feature Delivery Library know to use the local split APKs to test
installing feature modules, without connecting to the Play Store.

### Deploy your app to the device

After you [build a set of APKs](https://developer.android.com/guide/playcore/feature-delivery/on-demand#build-apks) using the `--local-testing` flag,
use `bundletool` to install the base version of your app and transfer additional
APKs to your device's local storage. You can perform both actions with the
following command:  

```
bundletool install-apks --apks my_app.apks
```

Now, when you start your app and complete the user flow to download and install
a feature module, the Play Feature Delivery Library uses the APKs that `bundletool`
transferred to the device's local storage.

### Simulate a network error

To simulate module installs from the Play Store, the Play Feature Delivery Library uses an
alternative to the `SplitInstallManager`, called
[`FakeSplitInstallManager`](https://developer.android.com/reference/com/google/android/play/core/splitinstall/testing/FakeSplitInstallManager),
to request the module. When you use `bundletool` with the `--local-testing` flag
to [build a set of APKs](https://developer.android.com/guide/playcore/feature-delivery/on-demand#build-apks) and deploy them to your test device, it
includes metadata that instructs the Play Feature Delivery Library to automatically switch
your app's API calls to invoke `FakeSplitInstallManager`, instead of
`SplitInstallManager`.

`FakeSplitInstallManager` includes a boolean flag that you can enable to
simulate a network error the next time your app requests to install a module. To
access `FakeSplitInstallManager` in your tests, you can get an instance of it
using the
[`FakeSplitInstallManagerFactory`](https://developer.android.com/reference/com/google/android/play/core/splitinstall/testing/FakeSplitInstallManagerFactory),
as shown below:  

### Kotlin

```kotlin
// Creates an instance of FakeSplitInstallManager with the app's context.
val fakeSplitInstallManager = FakeSplitInstallManagerFactory.create(context)
// Tells Play Feature Delivery Library to force the next module request to
// result in a network error.
fakeSplitInstallManager.setShouldNetworkError(true)
```

### Java

```java
// Creates an instance of FakeSplitInstallManager with the app's context.
FakeSplitInstallManager fakeSplitInstallManager =
    FakeSplitInstallManagerFactory.create(context);
// Tells Play Feature Delivery Library to force the next module request to
// result in a network error.
fakeSplitInstallManager.setShouldNetworkError(true);
```