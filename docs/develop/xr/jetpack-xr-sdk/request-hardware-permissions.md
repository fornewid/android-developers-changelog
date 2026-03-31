---
title: Request hardware permissions for AI glasses  |  Android XR for Jetpack XR SDK  |  Android Developers
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/request-hardware-permissions
source: html-scrape
---

The Android XR SDK has  [reached Developer Preview 3](https://android-developers.googleblog.com/2025/12/build-for-ai-glasses-with-android-xr.html), and we want your feedback! Try things out, and visit our [support page](/develop/xr/support) to reach out.

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android XR](https://developer.android.com/develop/xr)
* [Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk)
* [Guides](https://developer.android.com/develop/xr/get-started)

# Request hardware permissions for AI glasses Stay organized with collections Save and categorize content based on your preferences.



Applicable XR devices

This guidance helps you build experiences for these types of XR devices.

[Learn about XR device types →](/develop/xr/devices)

![](/static/images/develop/xr/ai-glasses-icon.svg)


AI Glasses

[Learn about XR device types →](/develop/xr/devices)

Just like on a phone, accessing sensitive hardware like the camera and
microphone on AI glasses requires explicit user consent. These are considered
**glasses-specific permissions**, and your app must request them at runtime,
even if it already has the corresponding permissions on the phone.

## Declare the permissions in your app's manifest

Before requesting permissions, you must [declare them in your app's manifest](/training/permissions/declaring)
file using the [`<uses-permission>`](/guide/topics/manifest/uses-permission-element) element. This declaration remains the
same whether the permission is for a phone or an AI-glasses-specific feature,
but you must still explicitly request it for glasses-specific hardware or
functionality.

```
<manifest ...>
    <!-- Only declare permissions that your app actually needs. In this example,
    we declare permissions for the camera. -->
    <uses-permission android:name="android.permission.CAMERA"/>
    <application ...>
        ...
    </application>
</manifest>
```

## Register the permissions launcher

To request permissions for AI glasses, first you use the
[`ActivityResultLauncher`](/reference/kotlin/androidx/activity/result/ActivityResultLauncher) with the
[`ProjectedPermissionsResultContract`](/reference/kotlin/androidx/xr/projected/permissions/ProjectedPermissionsResultContract#ProjectedPermissionsResultContract()) method to register the permissions
launcher.

```
// Register the permissions launcher using the ProjectedPermissionsResultContract.
private val requestPermissionLauncher: ActivityResultLauncher<List<ProjectedPermissionsRequestParams>> =
    registerForActivityResult(ProjectedPermissionsResultContract()) { results ->
        if (results[Manifest.permission.CAMERA] == true) {
            isPermissionDenied = false
            initializeGlassesFeatures()
        } else {
            // Handle permission denial.
            isPermissionDenied = true
        }
    }

GlassesMainActivity.kt
```

### Key points about the code

* The code creates an [`ActivityResultLauncher`](/reference/kotlin/androidx/activity/result/ActivityResultLauncher) using the
  [`ProjectedPermissionsResultContract`](/reference/kotlin/androidx/xr/projected/permissions/ProjectedPermissionsResultContract#ProjectedPermissionsResultContract()) method. The callback receives a
  map of permission names to their granted status.
* You need to specify which permissions your app requires, such as
  [`Manifest.permission.CAMERA`](/reference/kotlin/android/Manifest.permission#camera) or
  [`Manifest.permission.RECORD_AUDIO`](/reference/kotlin/android/Manifest.permission#record_audio).

## Create the request function

Next, you'll create a function that uses your app's permissions launcher to
request the permissions from the user at runtime.

```
private fun requestHardwarePermissions() {
    val params = ProjectedPermissionsRequestParams(
        permissions = listOf(Manifest.permission.CAMERA),
        rationale = "Camera access is required to overlay digital content on your physical environment."
    )
    requestPermissionLauncher.launch(listOf(params))
}

GlassesMainActivity.kt
```

### Key points about the code

* The `requestHardwarePermissions` function builds a
  [`ProjectedPermissionsRequestParams`](/reference/kotlin/androidx/xr/projected/permissions/ProjectedPermissionsRequestParams) object. This object bundles the
  list of permissions your app needs and the user-facing rationale. Make the
  rationale clear and concise to explain why your app needs these permissions.
* Calling `launch` on the launcher triggers the [permission request user
  flow](#permissions-user-flow).
* Your app should handle both granted and denied results gracefully in the
  launcher's callback.

## Create the permissions check function

Next, you'll create a function that can check whether the user has granted
permissions to your app.

```
private fun hasCameraPermission(): Boolean {
    return ContextCompat.checkSelfPermission(this, Manifest.permission.CAMERA) ==
            PackageManager.PERMISSION_GRANTED
}

GlassesMainActivity.kt
```

## Add the permission request logic

And lastly, create the logic that uses these functions to check for and request
the permissions at runtime.

```
if (hasCameraPermission()) {
    initializeGlassesFeatures()
} else {
    requestHardwarePermissions()
}

GlassesMainActivity.kt
```

### Key points about the code

* If the user has already granted your app the required permissions, the
  `initializeGlassesFeatures` function is called to initialize your app's
  experience. This function is defined as [part of your app's activity for AI
  glasses](/develop/xr/jetpack-xr-sdk/ai-glasses/first-activity#create-activity).

## Understand the permission request user flow

When you launch a permission request using the
[`ProjectedPermissionsResultContract`](/reference/kotlin/androidx/xr/projected/permissions/ProjectedPermissionsResultContract#ProjectedPermissionsResultContract()) method, the system initiates a
coordinated user flow across both the AI glasses and the phone.

**Important:**
You should call the `ProjectedPermissionsResultContract` method from an
[`Activity`](/reference/kotlin/android/app/Activity) displayed on AI glasses. Don't use the standard Android
permission APIs (such as [`requestPermissions`](/reference/kotlin/androidx/core/app/ActivityCompat#requestPermissions(android.app.Activity,%20java.lang.String%5B%5D,%20int)) with
[`ActivityResultLauncher<String>`](/reference/kotlin/androidx/activity/result/ActivityResultLauncher)) in code running on the glasses. Doing so
attempts to launch a non-interactable permission dialog on the glasses, breaking
the user flow.

If your app already has an `Activity` displayed on the phone, you should use
[`Activity#requestPermissions(permissions, requestCode, deviceId)`](/reference/kotlin/android/app/Activity#requestpermissions_1), where
the `deviceId` comes from calling the [`getDeviceId`](/reference/kotlin/android/content/Context#getdeviceid) method on the
[`Context`](/reference/kotlin/android/content/Context) returned by calling
[`ProjectedContext.createProjectedDeviceContext`](/reference/kotlin/androidx/xr/projected/ProjectedContext#createProjectedDeviceContext(android.content.Context)).

During the permissions user flow, here is what your app and the user can expect:

1. **On the AI glasses**: An activity appears on the **projected device
   (glasses)**, instructing the user to look at their phone to continue.

   **Preview:** Currently, the instructions and
   rationale provided by the system are not audible to the user. To provide an
   audible rationale to the user, we recommend using [Text to Speech
   (TTS)](/develop/xr/jetpack-xr-sdk/tts). For example:

   ```
   tts?.speak("Please review the permission request on your host device",
   TextToSpeech.QUEUE_ADD,
   null,
   "permission_request")
   ```
2. **On the phone**: Concurrently, an activity launches on the **host device
   (phone)**. This screen displays the rationale string you provided and gives
   the user the option to proceed or cancel.
3. **On the phone**: If the user accepts the rationale, a modified Android
   system permission dialog appears on the phone telling the user that they are
   granting the permission **for the AI glasses device** (not the phone), and
   the user can formally grant or deny the permission.
4. **Receiving the result**: After the user makes their final choice, the
   activities on both the phone and AI glasses are dismissed. Your
   [`ActivityResultLauncher`](/reference/kotlin/androidx/activity/result/ActivityResultLauncher) callback is then invoked with a map containing
   the granted status for each requested permission.

[Previous

arrow\_back

Overview](/develop/xr/jetpack-xr-sdk/access-hardware)

[Next

Use a projected context to access glasses hardware

arrow\_forward](/develop/xr/jetpack-xr-sdk/access-hardware-projected-context)