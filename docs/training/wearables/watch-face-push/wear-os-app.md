---
title: https://developer.android.com/training/wearables/watch-face-push/wear-os-app
url: https://developer.android.com/training/wearables/watch-face-push/wear-os-app
source: md.txt
---

> [!NOTE]
> **Note:** The Watch Face Push library is meant for watch face developers who prefer to publish to their own marketplace stores.  
>
> If you publish your watch faces to Google Play, use a tool that supports a less complex publishing process, such as [Watch Face Designer](https://developer.android.com/training/wearables/watch-face-designer/publish) or [Watch Face Studio](https://developer.samsung.com/watch-face-studio/user-guide/build.html).

Watch Face Push lets your app manage watch faces on a Wear OS device.
This includes adding, updating, and removing watch faces, as well as setting
the active watch face. Configure your Wear OS app to
use the Watch Face Push API.

## Setup

Include the [`androidx.wear.watchfacepush:watchfacepush`](https://developer.android.com/jetpack/androidx/releases/wear-watchfacepush#declaring_dependencies) dependency in your
`build.gradle.kts` file.

Add the following to your `AndroidManifest.xml`:

<br />

```xml
<!-- Required to use the Watch Face Push API.  -->
<uses-permission android:name="com.google.wear.permission.PUSH_WATCH_FACES" />
```

<br />

## Get a reference to the manager instance

Obtain an instance of `WatchFacePushManager`:

<br />

```kotlin
val watchFacePushManager = WatchFacePushManagerFactory.createWatchFacePushManager(context)
```

<br />

`WatchFacePushManager` provides access to all the methods for interacting with
Watch Face Push.

## Work with slots

A key concept when working with Watch Face Push is *slots*. Slots are a way of
addressing installed watch faces that belong to your application. The system
sets a maximum number of slots that a marketplace can have; with Wear OS 6,
the limit is 1.

When updating or removing a watch face, `slotId` is used to identify the
watch face to perform the operation on.

### List watch faces

To list the set of installed watch faces, use `listWatchFaces()`:

<br />

```kotlin
val response = watchFacePushManager.listWatchFaces()
val installedList = response.installedWatchFaceDetails
installedList.forEach {
    Log.i(TAG, "Installed watchface: ${it.packageName}")
}

val remainingSlots = response.remainingSlotCount
Log.i(TAG, "Remaining slots: $remainingSlots")
```

<br />

This lets you determine whether the slot is available, or whether
adding another watch face requires replacing the existing one. The list also
gives you details about the installed watch face.
For example, to check whether a given watch face package is installed:

<br />

```kotlin
suspend fun isInstalled(packageName: String) = watchFacePushManager.listWatchFaces()
    .installedWatchFaceDetails.any { it.packageName == packageName }
```

<br />

### Add a watch face

If there are slots available, as determined by the `listWatchFaces`
response, then the `addWatchFace()` method should be used:

<br />

```kotlin
try {
    // Supply the validation token along with the watch face package data itself.
    val slot = watchFacePushManager.addWatchFace(parcelFileDescriptor, token)
    Log.i(TAG, "${slot.packageName} (${slot.versionCode}) added in slot ${slot.slotId}")
} catch (e: WatchFacePushManager.AddWatchFaceException) {
    Log.e(TAG, "Something went wrong installing the watch face", e)
}
```

<br />

> [!NOTE]
> **Note:** Don't store `slotId` values or treat them as persistent. The state could change outside of your application; for example, a user might uninstall your watch face through the system UI. Always obtain the current state immediately before any slot-based operation.

## Update a watch face

Updating a watch face lets you replace the contents of a given slot with a
new package. This could either be upgrading the same watch face to a newer
version or replacing the watch face entirely with another.

<br />

```kotlin
// Replacing the com.example.watchfacepush.green watch face with
// com.example.watchfacepush.red
val slotId =
    watchFacePushManager.listWatchFaces().installedWatchFaceDetails
        .firstOrNull { it.packageName == "com.example.watchfacepush.green" }?.slotId
        ?: throw IllegalArgumentException("No green watch face found")
try {
    watchFacePushManager.updateWatchFace(slotId, redParcelFileDesc, redValidationToken)
} catch (e: WatchFacePushManager.UpdateWatchFaceException) {
    Log.e(TAG, "Something went wrong updating the watch face", e)
}
```

<br />

## Remove a watch face

To remove a watch face:

<br />

```kotlin
// Remove the com.example.watchfacepush.green watch face.
val slotId =
    watchFacePushManager.listWatchFaces().installedWatchFaceDetails
        .firstOrNull { it.packageName == "com.example.watchfacepush.green" }?.slotId
        ?: throw IllegalArgumentException("No green watch face found")

try {
    watchFacePushManager.removeWatchFace(slotId)
} catch (e: WatchFacePushManager.RemoveWatchFaceException) {
    Log.e(TAG, "Something went wrong removing the watch face", e)
}
```

<br />

> [!NOTE]
> **Note:** Consider whether your app should call `removeWatchFace` at all. Instead, when the user taps to uninstall a watch face through your marketplace app, you may want to replace it with a default watch face.

This approach means your watch face can always be found in the system watch
face picker. You can feature your logo prominently, and can even feature a
button to launch your Marketplace app on the phone.

## Check if your watch face is active

Determining whether your marketplace has the active watch face set is important
in helping the user have a smooth experience: If the marketplace already has the
active watch face set, then if the user wishes to choose another watch face,
they only need to replace the current one through the marketplace app for this
to take effect. However, if the marketplace does not have the active watch face
set, the phone app must offer the user more guidance. See the section on the
phone app for more details on how to handle this user experience.

To determine whether the marketplace has the active watch face set, use the
following logic:

<br />

```kotlin
suspend fun hasActiveWatchFace() = watchFacePushManager.listWatchFaces()
    .installedWatchFaceDetails
    .any {
        watchFacePushManager.isWatchFaceActive(it.packageName)
    }
```

<br />

> [!WARNING]
> **Warning:** When calling `updateWatchFace()`, don't call `isWatchFaceActive()` immediately afterward because this can lead to unexpected results. It can take a little time for the watch face swap to finish.  
>
> Instead, first determine whether the calling app has a reference to the active watch face as, shown in the previous snippet, and *then* call `updateWatchFace()`. If `updateWatchFace()` completes successfully, you can assume that your app still has control of the active watch face.

## Supply a default watch face

Watch Face Push offers the ability to install a default watch face when your
marketplace app is installed. This doesn't, by itself, set that default watch
face as active (see setting the active watch face), but makes your watch face
available in the system watch face picker.

To use this feature:

1. In your Wear OS app build, include the default watch face in the path: `assets/default_watchface.apk`
2. Add the following entry to your `AndroidManifest.xml`

   <br />

   ```xml
   <meta-data
       android:name="com.google.android.wearable.marketplace.DEFAULT_WATCHFACE_VALIDATION_TOKEN"
       android:value="@string/default_wf_token" />
   ```

   <br />

> [!NOTE]
> **Note:** A typical build pattern includes building your `default_watchface.apk` as part of your overall app build as a pre-build step. You can use this to populate the validation token manifest value by having the default watch face build process output an additional Android resources XML file and include that resources path as an additional resources path within your main app. This approach is simpler than trying to manipulate the manifest file itself during the build process.

## Set the active watch face

The Watch Face Push provides the means for the marketplace app to set the active
watch face.

This means specifically that the app can set the active watch face to one
belonging to the marketplace in the case where the current active watch face
does not belong to the marketplace. Note that in the case where the marketplace
already has the active watch face, changing this to another watch face is done
through a call to `updateWatchFace` to replace the contents of the watch face
slot with another watch face.

Setting the active watch face is a two-stage process:

1. Acquire the Android Permission required for setting the active watch face.
2. Call the `setWatchFaceAsActive` method.

### Acquire permissions to set the active watch face

The required permission is `SET_PUSHED_WATCH_FACE_AS_ACTIVE`, which must be
added to your manifest:

<br />

```xml
<!-- Required to be able to call the setWatchFaceAsActive() method. -->
<uses-permission android:name="com.google.wear.permission.SET_PUSHED_WATCH_FACE_AS_ACTIVE" />
```

<br />

As this is a runtime permission, your app must request this permission from the
user when the app runs (consider the [Accompanist library](https://google.github.io/accompanist/permissions/) to
help with this).

> [!NOTE]
> **Note:** This permission has a maximum rejection count of 1: If the user denies the request, then the request cannot be made again. In that case, the app should direct the user to the settings in order to manually adjust the permission.

### Set the watch face as active

Once the permission has been granted, call `setWatchFaceAsActive` on the slot ID
of the watch face that should be active.

> [!NOTE]
> **Note:** The active watch face can be set by this means *only once*. Should the user move to a watch face from another developer, calling this API to set the active watch face back to your watch face throws an exception.

Once this means has been used, your [phone app](https://developer.android.com/training/wearables/watch-face-push/phone-app) should instead offer
guidance on how to manually set the active watch face.

## Read additional metadata from your watch face APK

The `WatchFaceSlot` object also provides the means to obtain additional
information you can declare on your watch face.

This can be useful particularly in scenarios where you have minor variants of
the same watch face. For example, you could have a watch face defined:

- Package name: `com.myapp.watchfacepush.mywatchface`
- Package version: `1.0.0`

But this watch face might come as four different APKs, where all are almost
exactly the same, but with different default colors: *red, yellow, green* and
*blue* , set in a `ColorConfiguration` in the Watch Face Format XML.

This slight variation is then reflected in each of four APKs:

<br />

```xml
<!-- For watch face com.myapp.watchfacepush.mywatchface -->
<property
    android:name="default_color"
    android:value="red" />
```

<br />

Using a custom property allows your app to determine which of these variants is
installed:

<br />

```kotlin
val color = watchFaceDetails
    .getMetaData("com.myapp.watchfacepush.mywatchface.default_color")
    .invoke()
Log.i(TAG, "Default color: $color")
```

<br />

> [!NOTE]
> **Note:** In the preceding example, the namespace needed to be given for the property because `none` was declared on the property. If the property includes a dot (`.`), this is not necessary, so a property named `abc.def` can be retrieved using `getMetaDataValues("abc.def")`.

## Considerations

Important considerations when implementing Watch Face Push
in your app include focusing on power consumption, caching, updating bundled
watch faces, and providing a representative default watch face.

### Power

A key consideration for any app that runs on Wear OS is power consumption. For
the Wear OS component of your marketplace app:

1. **Your app should run as little and infrequently as possible** (unless being directly interacted with by the user). This includes:
   - Minimizing waking the app up from the phone app
   - Minimizing the running of WorkManager jobs
2. **Schedule any analytics reporting for when the watch is charging** :
   1. If you want to report usage statistics from the Wear OS app or any other metrics, use WorkManager with the `requiresCharging` constraint.
3. **Schedule updates for when the watch is charging and utilize WiFi** :
   1. You may want to check the versions of the installed watch faces and automatically update them. Again, use the `requiresCharging` constraint and the `UNMETERED` network type for `requiresNetworkType`.
   2. When on-charge, the device is likely to have access to Wi-Fi. [Request
      Wi-Fi to quickly download](https://developer.android.com/training/wearables/data/network-communication#high-bandwidth-network-access) the updated APKs, and release the network when done.
   3. This same guidance applies for where the marketplace may offer a *watch
      face of the day*; pre-download this while the watch is charging.
4. **Do not schedule jobs to check the active watch face** :
   1. Periodically checking whether your marketplace still has the active watch face and which watch face it is places a drain on the battery. Avoid this approach.
5. **Do not use notifications on the watch** :
   1. If your app uses notifications, focus these on the phone, where the user action opens the phone app to continue the journey. Configure notifications not to bridge across to the watch app using [`setLocalOnly`](https://developer.android.com/reference/android/app/Notification.Builder#setLocalOnly(boolean))().

### Caching

In the canonical marketplace example, watch faces are transferred from the phone
to the watch. This connection is typically a Bluetooth connection, which can be
quite slow.

To both provide a better user experience, and conserve retransmission power,
consider implementing a [small cache](https://developer.android.com/training/data-storage/app-specific#internal-create-cache) in the Wear OS device to store a
handful of APKs.

In the case where the user tries another watch face but then decides to revert
to their previously chosen watch face, this action is then nearly
instantaneous.

Similarly, this can be used for precaching for *watch face of the day* or
similar schemes where watch faces are downloaded while the Wear OS device is
charging.

### Update bundled watch faces

Your app may include a default watch face asset as described previously. It is
important to recognize that, while this watch face is installed to the system
when your marketplace app is installed, the watch face isn't updated should a
newer version be bundled with any update to your marketplace app.

To handle this situation, your marketplace app should listen for the
[`MY_PACKAGE_REPLACED`](https://developer.android.com/reference/android/content/Intent#ACTION_MY_PACKAGE_REPLACED) broadcast action and check for the need
to update any bundled watch face from package assets.

### Representative default watch face

A default watch face is a great way to help your users discover and use your
marketplace: The watch face is installed when your marketplace is, so users can
find it in the watch face gallery.

Some considerations when working with default watch faces:

- Don't use `removeWatchFace` if the user chooses to uninstall a watch face from your marketplace app. Instead, in this case, revert the watch face back to the default watch face using `updateWatchFace`. This helps users locate your watch face and set it from the gallery.
- Make the default watch face simple and instantly recognizable through your logo and theming. This helps users find it in the watch face gallery.
- Add a button to the default watch face to open the phone app. This can
  be achieved in two stages:

  1. Add a `Launch` element to the watch face to launch an intent using
     the Wear OS app, for example:

     `<Launch target="com.myapp/com.myapp.LaunchOnPhoneActivity" />`
  2. In `LaunchOnPhoneActivity`, launch the phone app using
     [`RemoteActivityHelper`](https://developer.android.com/reference/androidx/wear/remote/interactions/RemoteActivityHelper).