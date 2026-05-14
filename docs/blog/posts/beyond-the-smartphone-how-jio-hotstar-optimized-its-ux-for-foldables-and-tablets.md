---
title: https://developer.android.com/blog/posts/beyond-the-smartphone-how-jio-hotstar-optimized-its-ux-for-foldables-and-tablets
url: https://developer.android.com/blog/posts/beyond-the-smartphone-how-jio-hotstar-optimized-its-ux-for-foldables-and-tablets
source: md.txt
---

#### [Case Studies](https://developer.android.com/blog/categories/case-studies)

# Beyond the smartphone: How JioHotstar optimized its UX for foldables and tablets

###### 3-min read

![](https://developer.android.com/static/blog/assets/beyond_Smartphone_e17b5979d9_ZBzwz8.webp) 26 Jan 2026 [![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)](https://developer.android.com/blog/authors/prateek-batra) [##### Prateek Batra](https://developer.android.com/blog/authors/prateek-batra)

###### Developer Relations Engineer, Android Adaptive Apps

### **Beyond Phones: How JioHotstar Built an Adaptive UX**

[JioHotstar](https://play.google.com/store/apps/details?id=in.startv.hotstar) is a leading streaming platform in India, serving a user base exceeding 400 million. With a vast content library encompassing over 330,000 hours of video on demand (VOD) and real-time delivery of major sporting events, the platform operates at a massive scale.

To help ensure a premium experience for its vast audience, JioHotstar elevated the viewing experience by optimizing their app for foldables and tablets. They accomplished this by following Google's adaptive app guidance and utilizing resources like [samples](https://developer.android.com/design/ui/large-screens/samples), [codelabs](https://github.com/android/large-screen-codelabs), [cookbooks](https://developer.android.com/guide/topics/large-screens/large-screen-cookbook), and [documentation](https://developer.android.com/guide/topics/large-screens) to help create a consistently seamless and engaging experience across all display sizes.

### **JioHotstar's large screen challenge**

JioHotstar offered an excellent user experience on standard phones and the team wanted to take advantage of new form factors. To start, the team evaluated their app against the [large screen app quality guidelines](https://developer.android.com/docs/quality-guidelines/large-screen-app-quality) to understand the optimizations required to extend their user experience to foldables and tablets. To achieve [Tier 1](https://developer.android.com/docs/quality-guidelines/large-screen-app-quality#tier_1_best_large_screen_differentiated) large screen app status, the team implemented two strategic updates to adapt the app across various form factors and differentiate on foldables. By addressing the unique challenges posed by foldable and tablet devices, JioHotstar aims to deliver a high-quality and immersive experience across all display sizes and aspect ratios.

### **What they needed to do**

JioHotstar's user interface, designed primarily for standard phone displays, encountered challenges in adapting hero image aspect ratios, menus, and show screens to the diverse screen sizes and resolutions of other form factors. This often led to image cropping, letterboxing, low resolution, and unutilized space, particularly in landscape mode. To help fully leverage the capabilities of tablets and foldables and deliver an optimized user experience across these device types, JioHotstar focused on refining the UI to ensure optimal layout flexibility, image rendering, and navigation across a wider range of devices.

### **What they did**

For a better viewing experience on large screens, JioHotstar took the initiative to enhance its app by incorporating [WindowSizeClass](https://developer.android.com/develop/ui/compose/layouts/adaptive/use-window-size-classes) and creating optimized layouts for compact, medium and extended widths. This allowed the app to adapt its user interface to various screen dimensions and aspect ratios, ensuring a consistent and visually appealing UI across different devices.

JioHotstar followed this pattern using Material 3 Adaptive library to know how much space the app has available. First invoking the [currentWindowAdaptiveInfo()](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/package-summary#currentWindowAdaptiveInfo(kotlin.Boolean)) function, then using new layouts accordingly for the three window size classes:

```
val sizeClass = currentWindowAdaptiveInfo().windowSizeClass

if(sizeClass.isWidthAtLeastBreakpoint(WIDTH_DP_EXPANDED_LOWER_BOUND)) {
    showExpandedLayout()
} else if(sizeClass.isHeightAtLeastBreakpoint(WIDTH_DP_MEDIUM_LOWER_BOUND)) {
    showMediumLayout()
} else {
    showCompactLayout()
}
```

The breakpoints are in order, from the biggest to the smallest, as internally the API checks for with a greater or equal then, so any width that is at least greater or equal then `EXPANDED` will always be greater than `MEDIUM`.

<br />

JioHotstar is able to provide the premium experience unique to foldable devices: [Tabletop Mode](https://developer.android.com/develop/ui/compose/layouts/adaptive/foldables/make-your-app-fold-aware#tabletop_posture). This feature conveniently relocates the video player to the top half of the screen and the video controls to the bottom half when a foldable device is partially folded for a handsfree experience.

To accomplish this, also using the Material 3 Adaptive library, the same [currentWindowAdaptiveInfo()](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/Posture#isTabletop()) can be used to query for the tabletop mode. Once the device is held in tabletop mode, a change of layout to match the top and bottom half of the posture can be done with a column to place the player in the top half and the controllers in the bottom half:

```
val isTabletTop = currentWindowAdaptiveInfo().windowPosture.isTabletop
if(isTabletopMode) {
   Column {
       Player(Modifier.weight(1f))
       Controls(Modifier.weight(1f))
   }
} else {
   usualPlayerLayout()
}
```

JioHotstar is now meeting the [Large Screen app quality guidelines](https://developer.android.com/docs/quality-guidelines/large-screen-app-quality) for Tier 1. The team leveraged [adaptive app](https://developer.android.com/adaptive-apps) guidance, utilizing [samples](https://developer.android.com/design/ui/large-screens/samples), [codelabs](https://github.com/android/large-screen-codelabs), [cookbooks](https://developer.android.com/guide/topics/large-screens/large-screen-cookbook), and [documentation](https://developer.android.com/guide/topics/large-screens) to incorporate these recommendations.

To further improve the user experience, JioHotstar increased touch target sizes, to the recommended 48dp, on video discovery pages, ensuring accessibility across large screen devices. Their video details page is now adaptive, adjusting to screen sizes and orientations. They moved beyond simple image scaling, instead leveraging window size classes to detect window size and density in real time and load the most appropriate hero image for each form factor, helping to enhance visual fidelity. Navigation was also improved, with layouts adapting to suit different screen sizes.

Now users can view their favorite content from JioHotstar on large screens devices with an improved and highly optimized viewing experience.

*"Achieving Tier 1 large screen app status with Google is a milestone that reflects the strength of our shared vision. At JioHotstar, we have always believed that optimizing for large screen devices goes beyond adaptability, it's about elevating the viewing experience for audiences who are rapidly embracing foldables, tablets, and connected TVs.*

*Leveraging Google's Jetpack libraries and guides allowed us to combine our insights on content consumption with their expertise in platform innovation. This collaboration allowed both teams to push boundaries, address gaps, and co-create a seamless, immersive experience across every screen size.*

*Together, we're proud to bring this enhanced experience to millions of users and to set new benchmarks in how India and the world experience streaming."*  
*- *Sonu Sanjeev, Senior Software Development Engineer

###### Written by:

-

  ## [Prateek Batra](https://developer.android.com/blog/authors/prateek-batra)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/prateek-batra) ![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg) ![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)

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