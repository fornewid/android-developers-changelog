---
title: https://developer.android.com/training/tv/get-started/google-tv
url: https://developer.android.com/training/tv/get-started/google-tv
source: md.txt
---

# Best practices to drive engagement on Google TV

Android TV OS powers millions of TVs, streaming devices, and PayTV set-top boxes. Google TV is a brand-new experience available first on the Chromecast with Google TV and to more devices over time.

All apps built for Android TV work on devices running Google TV. To provide the best user experience on Google TV, we recommend that you apply the best practices in this guide.
| **Note:** To ensure a great user experience, all TV apps must meet specific requirements for usability before they are available for TVs on Google Play. For more information, see[TV app quality](https://developer.android.com/docs/quality-guidelines/tv-app-quality).

## Baseline requirements

- **Support Google Cast:** Google Cast lets you extend your Android, iOS, and Chrome apps to enable audio and video streaming to Android TVs as well as Chromecast devices and Assistant devices. For more information, see the[Google Cast documentation](https://developers.google.com/cast/docs/developers).
- **Use media sessions:** media sessions provide a universal way of interacting with an audio or video player. When an app informs Android that it is playing media, playback controls can be delegated to the app. Integrating with the media session lets an app advertise media playback externally and receive playback commands from external sources. These sources can be physical buttons, such as the play button on a headset or TV remote control, or indirect commands, such as instructing "pause" to Google Assistant. The media session then delegates these commands to the app, which applies them to the media player where the commands originated. See[Using a media session](https://developer.android.com/guide/topics/media-apps/working-with-a-media-session)for more details.

## Content discovery across surfaces

- **Offer a media actions feed:**when you provide a JSON media actions feed to Google, your content can be discovered through Google TV recommendations and other Google surfaces, such as Google Search. The deep links you provide let users jump directly into playback of your content to increase engagement. The feed also enables on-device search and the ability to play media using Google Assistant voice commands.

  Google is working with a limited number of providers at a time to integrate them into this feature. For more details, see the[Media Actions documentation](https://developers.google.com/actions/media).
- **Integrate Watch Next:** Watch Next lets users re-engage with the content in your app. When users leave your app partway through a movie or with a TV series in progress, you can surface that content directly on the Google TV home screen using Watch Next. The user can select a tile to deep link directly into playback within your app. Note that a Watch Next integration must be certified for quality to show on Google TV devices. See the[Watch Next documentation](https://developer.android.com/training/tv/discovery/watch-next-add-programs)for more details.

## Voice and engagement

- **Support account linking:** account linking provides seamless linking between a user's Google Account and your app's account to facilitate a streamlined user experience for your app's existing and new users.[Account linking](https://developers.google.com/identity/account-linking)is a prerequisite for other capabilities such as frictionless subscriptions, entitlement sync, and voice casting.
- **Support entitlement sync:** if your media actions feed includes media with entitlement requirements---for example, a user needs to have a particular subscription to access content---you can support entitlement sync to declare which subscriptions a linked account has. See the[entitlements endpoint documentation](https://developers.google.com/actions/media/concepts/access-requirements#entitlements-endpoint)for more details.
- **Offer voice casting:** voice casting lets your users initiate media playback on supported Cast devices through Google Assistant. You can enable this functionality by providing a[media actions](https://developers.google.com/actions/media)feed, supporting[account linking](https://developers.google.com/identity/account-linking/oauth-with-sign-in-linking?oauth=implicit), and creating a[Cast receiver](https://developers.google.com/cast/docs/developers).
- **Enable Cast Connect:** with Cast Connect, your Android TV app can act as a Cast receiver. This lets you provide a richer experience and support interaction with the remote control. See the[Android TV Receiver Overview](https://developers.google.com/cast/docs/android_tv_receiver)for more details.

## User acquisition

- **Integrate Google Play Billing:** use the Play Billing library to support in-app purchases and manage subscriptions across both mobile and TV. See the[billing documentation](https://developer.android.com/google/play/billing)for more details.
- **Provide frictionless subscriptions:** by combining[streamlined account linking](https://developers.google.com/identity/account-linking/oauth-with-sign-in-linking?oauth=implicit),[Play Billing](https://developer.android.com/google/play/billing)with[real time developer notifications](https://developer.android.com/google/play/billing/getting-ready#configure-rtdn), and[silent sign-in](https://developers.google.com/android/reference/com/google/android/gms/auth/api/signin/GoogleSignInClient.html#silentSignIn%28%29), you can provide a seamless purchase experience for your users. Watch the[Frictionless Subscriptions video](https://www.youtube.com/watch?v=ARuf97ncE4w&list=PLWz5rJ2EKKc-Z8NeBXJkf1bzUVhx3fvh4&index=4)for more details.

## Google TV feature evaluation

An app built for Android TV OS works for all the devices in the TV ecosystem, including new Google TV branded devices. To know whether a device offers the Google TV experience, for instance for analytics, you can[evaluate or filter](https://developer.android.com/guide/topics/manifest/uses-feature-element#market-feature-filtering)on the system feature`com.google.android.feature.AMATI_EXPERIENCE`.