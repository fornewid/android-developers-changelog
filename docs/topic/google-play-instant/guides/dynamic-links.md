---
title: https://developer.android.com/topic/google-play-instant/guides/dynamic-links
url: https://developer.android.com/topic/google-play-instant/guides/dynamic-links
source: md.txt
---

**Warning:** Google Play Instant will no longer be available. Starting December 2025, Instant Apps cannot be published through Google Play, and all[Google Play services Instant APIs](https://developers.google.com/android/reference/com/google/android/gms/instantapps/package-summary)will no longer work. Users will no longer be served Instant Apps by Play using any mechanism.

We're making this change based on developer feedback and our continuous investments to improve the ecosystem since the introduction of Google Play Instant.

To continue optimizing for user growth, we encourage developers to refer users to their regular app or game, using[deeplinks](https://support.google.com/googleplay/android-developer/answer/12463044)to redirect them to specific journeys or features when relevant.

Several deep linking libraries are compatible with Google Play Instant such as[Branch](https://branch.io).

If your current deep linking solution isn't listed or if you find that it doesn't work with Google Play Instant, consider using Firebase Dynamic Links. This page describes how to set up Firebase Dynamic Links in an instant app project.

### Key benefits

- **Wrapping your links with Firebase Dynamic Links guarantees that clicks on links always take users to your instant app.**Otherwise, apps can force links to be opened inside an in-app browser instead of an instant app. Firebase Dynamic Links allows you to control the behavior of clicks on links.
- **Firebase Dynamic Links allows you to track analytics on events like clicks, first-opens, re-opens, and installs.**Dynamic Links events also are recorded in Google Analytics for Firebase.

### Integrating Firebase Dynamic Links with an instant app project

You can integrate Firebase Dynamic Links with your instant app project the same way you would[integrate a standard Android app](https://firebase.google.com/docs/dynamic-links/android/receive).

After you integrate with Firebase Dynamic Links, you just have to set the[androidFallbackLink parameter](https://firebase.google.com/docs/reference/dynamic-links/link-shortener)to your Instant Apps link.