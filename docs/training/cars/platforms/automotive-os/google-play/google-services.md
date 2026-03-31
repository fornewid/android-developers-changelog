---
title: Google Play services for cars with Google built-in  |  Android for Cars  |  Android Developers
url: https://developer.android.com/training/cars/platforms/automotive-os/google-play/google-services
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android for Cars](https://developer.android.com/training/cars)

# Google Play services for cars with Google built-in Stay organized with collections Save and categorize content based on your preferences.



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
| --- | --- |
| [App set ID](/identity/app-set-id) | `com.google.android.gms.appset` |
| [Android Advertising ID (AAID)](https://developers.google.com/android/reference/com/google/android/gms/ads/identifier/AdvertisingIdClient) | `com.google.android.gms.ads.identifier` |
| [AppSearch](/develop/ui/views/search/appsearch) | `com.google.android.gms.appsearch` |
| Auth | `com.google.android.gms.auth`   `com.google.android.gms.auth.account` |
| Auth API | `com.google.android.gms.auth.api`   `com.google.android.gms.auth.api.credentials`   `com.google.android.gms.auth.api.signin` |
| [Cronet](/guide/topics/connectivity/cronet) | `com.google.android.gms.net` |
| [FIDO2](https://developers.google.com/identity/fido/android/native-apps) | `com.google.android.gms.fido` |
| [Firebase Authentication](https://firebase.google.com/docs/auth/) | `com.google.firebase.auth` |
| [Firebase Dynamic Links](https://firebase.google.com/docs/dynamic-links/) | `com.google.firebase.dynamiclinks` |
| [Google Analytics for Firebase](https://firebase.google.com/docs/analytics/android/start/) | `com.google.firebase.analytics`  `com.google.android.gms.measurement` |
| [Google Analytics Services](https://developers.google.com/analytics/) | `com.google.android.gms.analytics` |
| [Google Awareness](https://developers.google.com/awareness/) | `com.google.android.gms.awareness` |
| [Google Pay](https://developers.google.com/pay/) | `com.google.android.gms.wallet` |
| [Google Play Games Services (v2)](/games/pgs/overview) Note the following differences from mobile:   * Play Games profile creation isn't supported in cars. Users can   use their phone or the web to create a Play Games profile. * Play Games privacy settings can be viewed and edited on a user's   phone by scanning a QR Code and using a web browser for updates. * If a user isn't signed into a Google Account or doesn't have an   existing games profile, they aren't prompted to sign in to a   Google Account or create a game profile in the car. | `com.google.android.gms.games`   `com.google.android.gms.games.achievement`   `com.google.android.gms.games.event`   `com.google.android.gms.games.leaderboard`   `com.google.android.gms.games.snapshot`   `com.google.android.gms.games.stats` |
| Google Play services utilities | `com.google.android.gms.common` |
| [Google Tag Manager](https://developers.google.com/tag-manager/) | `com.google.android.gms.tagmanager` |
| [Location and Context](https://developers.google.com/location-context/) | `com.google.android.gms.location` |
| [Nearby](https://developers.google.com/nearby/) | `com.google.android.gms.nearby` |
| [Places](https://cloud.google.com/maps-platform/places/) | `com.google.android.gms.location.places` |
| [Play Integrity API](/google/play/integrity) | `com.google.android.play.core.integrity`   `com.google.android.play.core.integrity.model` |
| [SafetyNet](/training/safetynet)   *Deprecated: use Play Integrity API instead* | `com.google.android.gms.safetynet` |
| Stats | `com.google.android.gms.stats` |
| [Tasks](https://developers.google.com/android/guides/tasks) | `com.google.android.gms.tasks` |
| [Thread Network](https://developers.home.google.com/thread) | `com.google.android.gms.threadnetwork` |
| [Time](https://developers.google.com/location-context/time) | `com.google.android.gms.time`  `com.google.android.gms.time.trustedtime` |