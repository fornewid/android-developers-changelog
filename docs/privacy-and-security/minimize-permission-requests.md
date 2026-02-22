---
title: https://developer.android.com/privacy-and-security/minimize-permission-requests
url: https://developer.android.com/privacy-and-security/minimize-permission-requests
source: md.txt
---

# Minimize your permission requests

As part of[improving app quality](https://android-developers.googleblog.com/2022/10/raising-bar-on-technical-quality-on-google-play.html)and protecting user privacy, we recommend you minimize the permissions usage in your apps. This helps users discover and use high-quality apps that provide a safe and secure user environment.

Requesting permissions from users interrupts the user flow, and users can deny your request. In addition, each time you declare a new permission, you must[review how your app requests and shares user data](https://developer.android.com/guide/topics/data/collect-share). Some[particularly sensitive permissions and APIs](https://support.google.com/googleplay/android-developer/answer/9888170)require you to provide in-app disclosure of your data access, collection, use, and sharing.

There are multiple alternative ways to minimize permission usage:

- Declare permissions which provide coarse location information, rather than precise location information, if your app just needs approximate location.
- Call APIs which allow your app to perform the desired functionality without declaring permissions.
- Invoke specific intents or event handlers to perform functionality, instead of declaring permissions.
- The system provides[built-in contracts](https://developer.android.com/reference/androidx/activity/result/contract/ActivityResultContracts)for different file operations and also supports[custom contracts](https://developer.android.com/training/basics/intents/result#custom).

If you must declare a permission, always[respect the user's decision](https://developer.android.com/training/permissions/requesting#handle-denial)and provide a way to gracefully degrade your app's experience.

This page describes several use cases that your app can fulfill without declaring the need for any permissions.

## Show nearby places

Your app might need to know the user's approximate location. This is useful for showing location-aware information, such as nearby restaurants.

Some use cases only require a rough estimate of a device's location. In these situations, do one of the following, depending on how often your app needs location-aware information:

- If your app frequently needs location, declare the[`ACCESS_COARSE_LOCATION`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_COARSE_LOCATION)permission. The permission provides a device location estimate from location services, as described in the documentation about[approximate location accuracy](https://developer.android.com/training/location/permissions#accuracy).
- If your app needs location less often, or only once, consider asking the user to enter an address or a postal code instead.

Other use cases require a more precise estimate of a device's location. Those situations are the only times when it's OK to declare the[`ACCESS_FINE_LOCATION`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_FINE_LOCATION)permission.

## Create and access files

Android lets you create and access files without needing to declare any permissions related to storage or sensors.

### Open media files

Your app might allow users to choose from their photos and videos, such as for message attachments or profile pictures.

To support this functionality, use the[photo picker](https://developer.android.com/training/data-storage/shared/photopicker). The photo picker doesn't require any runtime permissions to use. When a user interacts with the photo picker to select photos or videos to share with your app, the system grants temporary read access to the URI associated with the selected media files.

If your app needs to access media files without using the photo picker, you don't need to declare any storage permissions:

- If you access media files that your app created, your app already has access to these files in the[media store](https://developer.android.com/training/data-storage/shared/media#media_store).
- If you access media files that other apps created,[use the Storage Access Framework](https://developer.android.com/training/data-storage/shared/documents-files).

### Open documents

Your app might show documents that the user created, either in your app or in another app. A common example is a text file.

In this situation, declare the[`READ_EXTERNAL_STORAGE`](https://developer.android.com/reference/android/Manifest.permission#READ_EXTERNAL_STORAGE)only for compatibility with older devices. Set the`android:maxSdkVersion`to`28`.

Depending on which app created the document, do one of the following:

- If the user created the document in your app,[access it directly](https://developer.android.com/training/data-storage/app-specific#external-access-files).
- If the user created the document in another app, use the[Storage Access Framework](https://developer.android.com/training/data-storage/shared/documents-files).

### Take a photo

Users might take pictures in your app, using the pre-installed system camera app.

In this situation, don't declare the`CAMERA`permission. Instead, invoke the[`ACTION_IMAGE_CAPTURE`](https://developer.android.com/reference/android/provider/MediaStore#ACTION_IMAGE_CAPTURE)intent action.
| **Note:** If your app declares Manifest.permission.CAMERA permission and is not granted, then the action results in a`SecurityException`.

### Record a video

Users might record videos in your app, using the pre-installed system camera app.

In this situation, don't declare the`CAMERA`permission. Instead, invoke the[`ACTION_VIDEO_CAPTURE`](https://developer.android.com/reference/android/provider/MediaStore#ACTION_VIDEO_CAPTURE)intent action.
| **Note:** If your app declares Manifest.permission.CAMERA permission and is not granted, then the action results in a`SecurityException`.

## Identify the device that's running an instance of your app

A particular instance of your app might need to know which device it's running on. This is useful for apps that have device-specific preferences or messaging, such as different playlists for TV devices and wearable devices.

In this situation, don't access the device's IMEI directly. In fact, as of Android 10, you can't do so. Instead, do one of the following:

- Get a unique device identifier for your app's instance using the[Instance ID](https://developers.google.com/instance-id/guides/android-implementation)library.
- Create your own identifier that's scoped to your app's storage. Use basic system functions, such as[`randomUUID()`](https://developer.android.com/reference/java/util/UUID#randomUUID()).

## Pair with a device over Bluetooth

Your app might offer an enhanced experience by transferring data to another device over Bluetooth.

To support this functionality, don't declare the`ACCESS_FINE_LOCATION`,`ACCESS_COARSE_LOCATIION`, or`BLUETOOTH_ADMIN`permissions. Instead, use[companion device pairing](https://developer.android.com/guide/topics/connectivity/companion-device-pairing).

## Automatically enter a payment card number

Google Play services offers a library that lets you automatically enter a payment card number. Instead of declaring the`CAMERA`permission, you can use the[debit and credit card recognition](https://developers.google.com/pay/payment-card-recognition/debit-credit-card-recognition)library.

## Manage phone calls and text messages

Android and Google Play services offer libraries that let you manage phone calls and text messages without needing to declare any permissions related to phone calls or SMS messages.

### Enter a one-time passcode automatically

To streamline a two-factor authentication workflow, your app might automatically enter the one-time passcode that is sent to a user's device to verify their identity.

To support this functionality on devices powered by Google Play services, don't declare the`READ_SMS`permission. Instead, use the[SMS Retriever API](https://developers.google.com/identity/sms-retriever/overview).

On other devices, if your app targets Android 8.0 (API level 26) or higher, generate an app-specific token using[`createAppSpecificSmsToken()`](https://developer.android.com/reference/android/telephony/SmsManager#createAppSpecificSmsToken(android.app.PendingIntent)). Pass this token to another app or service that can send a verification SMS message.

### Enter the user's phone number automatically

To provide more efficient sales or support, your app might allow the user to enter their device's phone number automatically.

To support this functionality on devices powered by Google Play services, don't declare the`READ_PHONE_STATE`permission. Instead, use the[Phone Number Hint](https://developers.google.com/identity/phone-number-hint/android)library.

### Filter phone calls

To minimize unnecessary interruptions for the user, your app might filter phone calls for spam.

To support this functionality, don't declare the`READ_PHONE_STATE`permission. Instead, use the[`CallScreeningService`](https://developer.android.com/reference/android/telecom/CallScreeningService)API.

### Place phone calls

Your app might offer the ability to place a phone call by tapping a contact's information.

To support this functionality, use the[`ACTION_DIAL`](https://developer.android.com/reference/android/content/Intent#ACTION_DIAL)intent action rather than the`ACTION_CALL`action.`ACTION_CALL`requires the install-time permission`CALL_PHONE`, which prevents devices that can't place calls, such as some tablets, from installing your application.

## Pause media when your app is interrupted

If the user receives a phone call, or if a user-configured alarm occurs, your app should pause any media playback until your app regains audio focus.

To support this functionality, don't declare the`READ_PHONE_STATE`permission. Instead, implement the[`onAudioFocusChange()`](https://developer.android.com/reference/android/media/AudioManager.OnAudioFocusChangeListener#onAudioFocusChange(int))event handler, which runs automatically when the system shifts its audio focus. Learn more about how to[implement audio focus](https://developer.android.com/guide/topics/media-apps/audio-focus).

## Scan barcodes

Android includes support for the[Google Code Scanner API](https://developers.google.com/ml-kit/vision/barcode-scanning/code-scanner), powered by Google Play services, which allows you to decode barcodes without declaring any camera permissions. This API helps preserve user privacy and makes it less likely that you need to create a custom UI for your barcode-scanning use case.

The API scans the barcode and only returns the scan results to your app. Images are processed on-device, and Google doesn't store any data or scan results.

If your app needs to support complex use cases or barcode formats, or if it requires a custom UI, use the[ML Kit barcode scanning API](https://developers.google.com/ml-kit/vision/barcode-scanning/android)instead.

## Reset unused permissions

Android provides multiple ways to reset unused runtime permissions to their default, denied state.

Read[design guidance](https://developer.android.com/training/permissions/requesting#reset-unused-permissions).

## Request runtime permissions

Once you've evaluated that your app needs to declare and request runtime permissions, follow a specific workflow to do so.

Read[design guidance](https://developer.android.com/training/permissions/requesting#workflow_for_requesting_permissions).

## Explain why your app needs permissions

Using`requestPermissions()`displays a dialog indicating which permissions your app wants to use but doesn't explain why, which might be puzzling to the user.

For more details and recommendations on how and when to show this dialog, read[design guidance](https://developer.android.com/training/permissions/requesting#explain).

## Handle permission denials

Your app should help users understand the implications of denying a permission before and after they choose to do so.

Read[design guidance](https://developer.android.com/training/permissions/requesting#handle-denial).