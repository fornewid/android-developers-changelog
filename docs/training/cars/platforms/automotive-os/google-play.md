---
title: https://developer.android.com/training/cars/platforms/automotive-os/google-play
url: https://developer.android.com/training/cars/platforms/automotive-os/google-play
source: md.txt
---

# Google Play on Android Automotive OS

Google Play is available on cars with[Google built-in](https://built-in.google/cars). This includes the Google Play Store, Google Play services, and more.

## Google Play services

The availability of[Google Play services](https://developers.google.com/android/guides/overview)in cars may be different than on other form factors. See[Google Play services for cars with Google built-in](https://developer.android.com/training/cars/platforms/automotive-os/google-services)for the list of supported services.

## Google Play Billing on Android Automotive OS

![Screenshot of the handoff screen shown to users when initiating an in-app purchase](https://developer.android.com/static/training/cars/images/play-billing.png)

[Google Play Billing](https://developer.android.com/google/play/billing)is supported on cars with Google built-in and uses the same integration as other form factors. Unlike other form factors, the purchase flow is not completed on device but is instead completed on another device, either through the Google Play app or website.

## Google Play Core libraries

The[Google Play Core libraries](https://developer.android.com/guide/playcore)allow your app to interact with the Play Store app.

The following libraries are supported by cars with Google built-in:

- [Play Asset Delivery](https://developer.android.com/guide/playcore/asset-delivery)
- [Play Feature Delivery](https://developer.android.com/guide/playcore/feature-delivery)

The following libraries are**not**supported by cars with Google built-in:

- [In-app reviews](https://developer.android.com/guide/playcore/in-app-review)
- [In-app updates](https://developer.android.com/guide/playcore/in-app-updates)

## Play Developer APIs

If you or a tool you use relies on the Play Developer Publishing API to upload and publish apps or to perform other publishing-related tasks, there are some differences to note for Android Automotive OS. See[Track name for form factors](https://developers.google.com/android-publisher/tracks#ff-track-name)for more details.

## Google Play Licensing

Cars with Google built-in support the[Google Play Licensing](https://developer.android.com/google/play/licensing)service, which can be used to obtain the licensing status for the current user, then allow or disallow further use as appropriate.