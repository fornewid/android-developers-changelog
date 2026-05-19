---
title: https://developer.android.com/blog/posts/how-fot-mob-leveraged-cross-device-discovery-to-score-record-wear-os-adoption
url: https://developer.android.com/blog/posts/how-fot-mob-leveraged-cross-device-discovery-to-score-record-wear-os-adoption
source: md.txt
---

#### [Case Studies](https://developer.android.com/blog/categories/case-studies)

# How FotMob leveraged cross-device discovery to score record Wear OS adoption

###### 3-min read

![](https://developer.android.com/static/blog/assets/cross_device_discovery_to_score_record_Wear_OS_adoption_Strapi_2f9244f1db_Z23QTbE.webp) 15 May 2026 [![](https://developer.android.com/static/blog/assets/Garan_Jenkin_0529dbfef9_Z2crRat.webp)](https://developer.android.com/blog/authors/garan-jenkin) [##### Garan Jenkin](https://developer.android.com/blog/authors/garan-jenkin)

###### Developer Relations Engineer

FotMob recently experienced its largest single-day increase on Wear OS among its installed audience in 5 years, at 2-3x the daily average. The secret? A simple cross-device installation flow that helps users discover their Wear OS app directly from their phone.

[FotMob](https://www.fotmob.com/) is one of the world's most popular football (some call it soccer!) platforms, known for its [mobile app](https://play.google.com/store/apps/details?id=com.mobilefootie.wc2010) that provides real-time scores, statistical analysis, and news.
![fotmob-side-by-side.png](https://developer.android.com/static/blog/assets/fotmob_side_by_side_c1332b8f37_2bbOh.webp)

In addition to the mobile app, FotMob is available on Wear OS, allowing users to keep on top of the latest scores and results directly from their wrist.

*"Many FotMob users follow matches live, and that often happens when they're not actively using their phone,"* says Roy Solberg, Android Tech Lead at FotMob. *"Wear OS gives fans a quick way to glance at scores, match events, and updates directly from their wrist, so we saw it as a natural extension of the FotMob experience."*

By providing a smooth experience across different form factors, FotMob ensures that their users can continue to get the most from their platform, in the most convenient form. This includes ensuring that settings and preferences--such as favorite teams--are synced across devices.

### The Discovery Gap

Despite many FotMob users having a Wear OS device, FotMob realized that some users might not be aware of the Wear OS app. This led the team to consider technical options for how to educate users about and ultimately install the Wear OS app directly from within the core phone app.

Fortunately, the Wearable library on Android and Wear OS provides exactly the building blocks that FotMob needed to create an in-app experience that would allow their users to do just that.

### Detecting Eligible Wear OS Devices

Within the FotMob phone app, the team used the `NodeClient` to identify connected Wear OS devices - candidates for the Wear OS app:

```kotlin
val connectedNodes = nodeClient.connectedNodes.await()
```

Additionally, the team defined a capability within the Wear OS app, indicating that FotMob was installed on the device. This is defined as an XML resource in the Wear OS package, and then queried within the phone app:

```kotlin
val nodesWithApp = capabilityClient
    .getCapability(CAPABILITY_WEAR_APP, CapabilityClient.FILTER_REACHABLE)
    .await()
    .nodes
```

By looking for only nodes *without* the capability, the team ensured the FotMob phone app only lists Wear OS devices without the app.

### Initiating the install flow

The FotMob team designed an educational half-page prompt that quickly makes the user aware of the opportunity, allowing them either to kick off the install flow, or dismiss it. This featured a prominent screenshot of the Wear OS experience, allowing the user to immediately see how the app might look on their watch.
![fotmob_wear_wrist.png](https://developer.android.com/static/blog/assets/fotmob_wear_wrist_41bc498b9b_2qeAJb.webp)

To start the installation, the app uses the `RemoteActivityHelper` API, to launch the Play Store on the watch:

```kotlin
val remoteActivityHelper = RemoteActivityHelper(context)

remoteActivityHelper.startRemoteActivity(
    Intent(Intent.ACTION_VIEW)
        .setData("market://details?id=${context.packageName}".toUri())
        .addCategory(Intent.CATEGORY_BROWSABLE),
    nodeId
).await()
```

### Results

*"The Wearable APIs made the implementation straightforward,"* says Roy. *"Being able to detect connected devices and query capabilities meant we could quickly determine whether the watch app was already installed. From there it was mostly about designing a prompt that felt helpful to users rather than intrusive."*

The rollout of the cross-device installation feature saw the largest single-day increase in FotMob's installed audience on Wear OS in 5 years, 2-3x higher than the normal install rate. Within 48 hours of the rollout reaching 100%, the watch app gained over 1,500 new installs¹.

*"Within the first 10 days we saw a significant jump in new Wear OS installs,"* says Roy.* "The watch app has been around for years, but this confirmed that many users with compatible devices simply weren't aware it existed."*

### Evolving cross-device installs

In addition to the solution employed by FotMob, we've now launched a library to make it even easier to implement these cross-device installation journeys through the [In-App Install Prompts library](https://developer.android.com/guide/playcore/install-prompt).

The following is an example of adding an installation prompt at the appropriate point in your app:

```kotlin
val crossDevicePromptManager = CrossDevicePromptManagerFactory.create(activity)
val request = CrossDevicePromptInstallationRequest.create()

try {
    val info = crossDevicePromptManager.requestInstallationPromptFlow(request).await()
    crossDevicePromptManager.launchPromptFlow(activity, info).await()
} catch (e: CrossDevicePromptException) {
    Log.e(TAG, "Cross-device prompt failed with error: ${e.errorCode}", e)
}
```

### Next steps: Start building your own cross-device journey today

Dive into the [DataLayer sample](https://github.com/android/wear-os-samples/tree/main/DataLayer) to learn more about how to add cross-device functionality to your app, and explore the new [In-App Install Prompts library](https://developer.android.com/guide/playcore/install-prompt), providing you with options for how you help your users achieve cross-device installation.

*\[1\]. Install data from Play Developer Console*
- [#Wear OS](https://developer.android.com/blog/topics/wear-os)

###### Written by:

-

  ## [Garan Jenkin](https://developer.android.com/blog/authors/garan-jenkin)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/garan-jenkin) ![](https://developer.android.com/static/blog/assets/Garan_Jenkin_0529dbfef9_Z2crRat.webp) ![](https://developer.android.com/static/blog/assets/Garan_Jenkin_0529dbfef9_Z2crRat.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/Amrit_Sanjeev_5215e0d7cc_CrDLy.webp)](https://developer.android.com/blog/authors/amrit-sanjeev)[![](https://developer.android.com/static/blog/assets/ash_32bd9f9ed7_Zhh9o0.webp)](https://developer.android.com/blog/authors/ash-nohe) 08 May 2026 08 May 2026 ![](https://developer.android.com/static/blog/assets/AANDDM_Gratitude_2000x1000_7d5a00e6c2_Z2vwfIA.webp)

  #### [Case Studies](https://developer.android.com/blog/categories/case-studies)

  ## [Gratitude saw 25% higher retention for widget users](https://developer.android.com/blog/posts/gratitude-saw-25-higher-retention-for-widget-users)

  [arrow_forward](https://developer.android.com/blog/posts/gratitude-saw-25-higher-retention-for-widget-users) The mindfulness app Gratitude encourages consistency through micro daily journaling, affirmations, and vision boards. The app has over 6 million downloads, 150 thousand 5 star ratings, and 100 million journal entries logged.

  ###### [Amrit Sanjeev](https://developer.android.com/blog/authors/amrit-sanjeev), [Ash Nohe](https://developer.android.com/blog/authors/ash-nohe) •
  3 min read

- [![](https://developer.android.com/static/blog/assets/thomas_ezan_d29c7508d0_l9O72.webp)](https://developer.android.com/blog/authors/thomas-ezan)[![](https://developer.android.com/static/blog/assets/Tracy_Agyemang_Headshot_9a0c523435_1hBimO.webp)](https://developer.android.com/blog/authors/tracy-agyemang) 04 May 2026 04 May 2026 ![](https://developer.android.com/static/blog/assets/AANDDM_KARROT_Strapi_eed79b0e1b_cCxXk.webp)

  #### [Case Studies](https://developer.android.com/blog/categories/case-studies)

  ## [Gemini and Firebase AI Logic enabled Karrot to increase sales with a translation feature built in under 2 weeks](https://developer.android.com/blog/posts/gemini-and-firebase-ai-logic-enabled-karrot-to-increase-sales-with-a-translation-feature)

  [arrow_forward](https://developer.android.com/blog/posts/gemini-and-firebase-ai-logic-enabled-karrot-to-increase-sales-with-a-translation-feature) Karrot is a hyperlocal, community-driven peer-to-peer marketplace app that enables users to buy, sell, and trade items with other verified users. Since launching in South Korea in 2015, the platform has expanded into global markets, amassing over 43 million registered users.

  ###### [Thomas Ezan](https://developer.android.com/blog/authors/thomas-ezan), [Tracy Agyemang](https://developer.android.com/blog/authors/tracy-agyemang) •
  2 min read

  - [#Android](https://developer.android.com/blog/topics/android)
- [![](https://developer.android.com/static/blog/assets/1_1_U4_K_Lr4r_A_Kx_Pq0_Crp_L3vr_Q_a4d1920594_2dcD9g.webp)](https://developer.android.com/blog/authors/ben-weiss)[![](https://developer.android.com/static/blog/assets/Tracy_Agyemang_Headshot_9a0c523435_1hBimO.webp)](https://developer.android.com/blog/authors/tracy-agyemang) 30 Mar 2026 30 Mar 2026 ![](https://developer.android.com/static/blog/assets/monzo_boosts_performance_aff3a37917_6VY99.webp)

  #### [Case Studies](https://developer.android.com/blog/categories/case-studies)

  ## [Monzo boosts performance metrics by up to 35% with a simple R8 update](https://developer.android.com/blog/posts/monzo-boosts-performance-metrics-by-up-to-35-with-a-simple-r8-update)

  [arrow_forward](https://developer.android.com/blog/posts/monzo-boosts-performance-metrics-by-up-to-35-with-a-simple-r8-update) Monzo is a UK digital bank with 15 million customers and growing. As the app scaled, the engineering team identified app startup time as a critical area for improvement but worried it would require significant changes to their codebase.

  ###### [Ben Weiss](https://developer.android.com/blog/authors/ben-weiss), [Tracy Agyemang](https://developer.android.com/blog/authors/tracy-agyemang) •
  2 min read

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)