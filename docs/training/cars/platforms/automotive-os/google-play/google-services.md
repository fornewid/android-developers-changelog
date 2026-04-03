---
title: https://developer.android.com/training/cars/platforms/automotive-os/google-play/google-services
url: https://developer.android.com/training/cars/platforms/automotive-os/google-play/google-services
source: md.txt
---

When you are developing apps for Android Automotive OS cars with
[Google built-in](https://built-in.google/cars/), some Google Play services may
not be available or may be restricted to provide a safe and consistent
experience for drivers.

Android Automotive OS uses the same [client libraries](https://maven.google.com/web/index.html#com.google.android.gms) for Google Play
services as mobile apps, so you can implement functionality for your automotive
app using the same libraries that you use for mobile apps.

The following table shows which [Google APIs for Android](https://developers.google.com/android/) are available on
Android Automotive OS cars with Google built-in:

| API | Available packages |
|---|---|
| [App set ID](https://developer.android.com/identity/app-set-id) | `https://developers.google.com/android/reference/com/google/android/gms/appset/package-summary` |
| [Android Advertising ID (AAID)](https://developers.google.com/android/reference/com/google/android/gms/ads/identifier/AdvertisingIdClient) | `https://developers.google.com/android/reference/com/google/android/gms/ads/identifier/package-summary` |
| [AppSearch](https://developer.android.com/develop/ui/views/search/appsearch) | `https://developers.google.com/android/reference/com/google/android/gms/appsearch/package-summary` |
| Auth | `https://developers.google.com/android/reference/com/google/android/gms/auth/package-summary` `https://developers.google.com/android/reference/com/google/android/gms/auth/account/package-summary` |
| Auth API | `https://developers.google.com/android/reference/com/google/android/gms/auth/api/package-summary` `https://developers.google.com/android/reference/com/google/android/gms/auth/api/credentials/package-summary` `https://developers.google.com/android/reference/com/google/android/gms/auth/api/signin/package-summary` |
| [Cronet](https://developer.android.com/guide/topics/connectivity/cronet) | `https://developers.google.com/android/reference/com/google/android/gms/net/package-summary` |
| [FIDO2](https://developers.google.com/identity/fido/android/native-apps) | `https://developers.google.com/android/reference/com/google/android/gms/fido/package-summary` |
| [Firebase Authentication](https://firebase.google.com/docs/auth/) | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/package-summary` |
| [Firebase Dynamic Links](https://firebase.google.com/docs/dynamic-links/) | `https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/package-summary` |
| [Google Analytics for Firebase](https://firebase.google.com/docs/analytics/android/start/) | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/package-summary.html` `https://firebase.google.com/docs/reference/android/com/google/android/gms/measurement/package-summary` |
| [Google Analytics Services](https://developers.google.com/analytics/) | `https://developers.google.com/android/reference/com/google/android/gms/analytics/package-summary` |
| [Google Awareness](https://developers.google.com/awareness/) | `https://developers.google.com/android/reference/com/google/android/gms/awareness/package-summary` |
| [Google Pay](https://developers.google.com/pay/) | `https://developers.google.com/android/reference/com/google/android/gms/wallet/package-summary` |
| [Google Play Games Services (v2)](https://developer.android.com/games/pgs/overview) Note the following differences from mobile: - Play Games profile creation isn't supported in cars. Users can use their phone or the web to create a Play Games profile. - Play Games privacy settings can be viewed and edited on a user's phone by scanning a QR Code and using a web browser for updates. - If a user isn't signed into a Google Account or doesn't have an existing games profile, they aren't prompted to sign in to a Google Account or create a game profile in the car. | `https://developers.google.com/android/reference/com/google/android/gms/games/package-summary` `https://developers.google.com/android/reference/com/google/android/gms/games/achievement/package-summary` `https://developers.google.com/android/reference/com/google/android/gms/games/event/package-summary` `https://developers.google.com/android/reference/com/google/android/gms/games/leaderboard/package-summary` `https://developers.google.com/android/reference/com/google/android/gms/games/snapshot/package-summary` `https://developers.google.com/android/reference/com/google/android/gms/games/stats/package-summary` |
| Google Play services utilities | `https://developers.google.com/android/reference/com/google/android/gms/common/package-summary` |
| [Google Tag Manager](https://developers.google.com/tag-manager/) | `https://developers.google.com/android/reference/com/google/android/gms/tagmanager/package-summary` |
| [Location and Context](https://developers.google.com/location-context/) | `https://developers.google.com/android/reference/com/google/android/gms/location/package-summary` |
| [Nearby](https://developers.google.com/nearby/) | `https://developers.google.com/android/reference/com/google/android/gms/nearby/package-summary` |
| [Places](https://cloud.google.com/maps-platform/places/) | `https://developers.google.com/android/reference/com/google/android/gms/location/places/package-summary` |
| [Play Integrity API](https://developer.android.com/google/play/integrity) | `https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/package-summary` `https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/package-summary` |
| [SafetyNet](https://developer.android.com/training/safetynet) *Deprecated: use Play Integrity API instead* | `https://developers.google.com/android/reference/com/google/android/gms/safetynet/package-summary` |
| Stats | `https://developers.google.com/android/reference/com/google/android/gms/stats/package-summary` |
| [Tasks](https://developers.google.com/android/guides/tasks) | `https://developers.google.com/android/reference/com/google/android/gms/tasks/package-summary` |
| [Thread Network](https://developers.home.google.com/thread) | `https://developers.home.google.com/reference/com/google/android/gms/threadnetwork/package-summary` |
| [Time](https://developers.google.com/location-context/time) | `https://developers.google.com/android/reference/com/google/android/gms/time/package-summary` `https://developers.google.com/android/reference/com/google/android/gms/time/trustedtime/package-summary` |