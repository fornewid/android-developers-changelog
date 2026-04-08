---
title: https://developer.android.com/about/versions/oreo/android-8.0-samples
url: https://developer.android.com/about/versions/oreo/android-8.0-samples
source: md.txt
---

# Code Samples

Use the code samples below to learn about Android 8.0 (API level 26) capabilities and APIs. To download the samples in Android Studio, select the**File \> New \> Import Samples**menu option.

**Note:**These downloadable projects are designed for use with Gradle and Android Studio.

## Autofill Framework

**AutofillFramework Sample**- This sample demonstrates the use of the Autofill Framework introduced in Android 8.0 (API level 26). It includes implementations of client Activities that want to be autofilled, and a Service that can provide autofill data to those Activities.

Get it on GitHub:[Java](https://github.com/android/input-samples/tree/main/AutofillFramework)\|[Kotlin](https://github.com/android/input-samples/tree/main/AutofillFrameworkKotlin)

## Picture-in-Picture Mode

**PictureInPicture Sample**- This sample demonstrates basic usage of Picture-in-Picture mode for handheld devices. The sample plays a video. The video keeps on playing when the app is turned into Picture-in-Picture mode. On Picture-in-Picture screen, the app shows an action item to pause or resume the video.

Get it on GitHub:[Java](https://github.com/android/media-samples/tree/main/PictureInPicture/)\|[Kotlin](https://github.com/android/media-samples/tree/main/PictureInPictureKotlin)

## Downloadable Fonts

**DownloadableFonts**- This sample demonstrates how to use the Downloadable Fonts feature introduced in Android 8.0 (API level 26). Downloadable Fonts allows apps to request a certain font from a provider, instead of bundling it or downloading it themselves. This means there is no need to independently bundle the font as an asset.

Get it on GitHub:[Java](https://github.com/android/user-interface-samples/tree/main/DownloadableFonts/)\|[Kotlin](https://github.com/android/user-interface-samples/tree/main/DownloadableFontsKotlin)

**EmojiCompat**- This sample demonstrates usage of the Emoji Compatibility Support Library. You can use this library to prevent your app from showing missing emoji characters in the form of tofu (□). You can use either bundled or downloadable emoji fonts. This sample shows both usages.

Get it on GitHub:[Java](https://github.com/android/user-interface-samples/tree/main/EmojiCompat)\|[Kotlin](https://github.com/android/user-interface-samples/tree/main/EmojiCompatKotlin)

## Background Execution Limits

**Bluetooth Advertisements Sample**- The Bluetooth Advertisements sample was updated to comply with Android 8.0 (API level 26)'s background execution limits. The sample previously created a background service which was used to broadcast Bluetooth LE Advertisements; this process is now started as a foreground service to ensure execution.

Get it on GitHub:[Java](https://github.com/android/connectivity-samples/tree/main/BluetoothAdvertisements)

## Background Location Restrictions

**LocationUpdatesPendingIntent Sample** - Shows how to request location updates using a`PendingIntent`. For apps targeting Android 7.x (API levels 24-25) but running on Android 8.0 (API level 26), developers can use either`PendingIntent.getService()`or`PendingIntent.getBroadcast()`. For apps targeting Android 8.0,`PendingIntent.getService()`does not work due to the limits placed on services started in the background. When targeting Android 8.0, developers should use`PendingIntent.getBroadcast()`.

Get it on GitHub:[Java](https://github.com/android/location-samples/tree/432d3b72b8c058f220416958b444274ddd186abd/LocationUpdatesPendingIntent)

**LocationUpdatesForegroundService Sample**- Shows how to use a foreground service to get location updates when the app activities are not visible. For apps running on Android 8.0 (API level 26), background updates are limited to only a few times per hour. Using a foreground service is a way to receive more frequent updates.

Get it on GitHub:[Java](https://github.com/android/location-samples/blob/432d3b72b8c058f220416958b444274ddd186abd/LocationUpdatesForegroundService)