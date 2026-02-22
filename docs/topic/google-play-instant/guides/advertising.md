---
title: https://developer.android.com/topic/google-play-instant/guides/advertising
url: https://developer.android.com/topic/google-play-instant/guides/advertising
source: md.txt
---

**Warning:** Google Play Instant will no longer be available. Starting December 2025, Instant Apps cannot be published through Google Play, and all[Google Play services Instant APIs](https://developers.google.com/android/reference/com/google/android/gms/instantapps/package-summary)will no longer work. Users will no longer be served Instant Apps by Play using any mechanism.

We're making this change based on developer feedback and our continuous investments to improve the ecosystem since the introduction of Google Play Instant.

To continue optimizing for user growth, we encourage developers to refer users to their regular app or game, using[deeplinks](https://support.google.com/googleplay/android-developer/answer/12463044)to redirect them to specific journeys or features when relevant.

Now that you've written your app, one way you can monetize it is by enabling it to carry advertising.

## Confirm that your ad network's SDK is compatible with Google Play Instant

For an app to be able to carry ads from your ad network, your ad network's SDK must be compatible with Google Play Instant. To confirm compatibility, follow these steps:

1. Download the sample instant app from the[Google Play Instant samples](https://github.com/android/app-bundle/tree/main/InstantApps)page.

2. Integrate your SDK with the sample.

3. Validate each type of ad you serve, such as banner ads or interstitial ads.

4. Ensure that your ad network's SDK doesn't serve HTTP ads. Doing so breaks the instant-app experience, because Google Play Instant doesn't allow HTTP traffic.

5. After you confirm compatibility, contact aia-compatibility@google.com to have your app added to the network. If there are issues with integration, reach out to aia-compatibility@google.com.

## Configure your app for ads

To configure your app to carry ads, you must integrate an Google Play Instant-compatible ad-network SDK into your app. The Google Mobile Ads Lite SDK is one such SDK. For more information about integrating an ad-network SDK, see the guides related to[Google Mobile Ads Lite SDK](https://developers.google.com/admob/android/lite-sdk)and[Google AdMob](https://developers.google.com/admob/android/instant-apps).

If you plan to integrate a different ad network's SDK into your app, consider reaching out to your relevant ad network to have them integrate with Google Play Instant.