---
title: Beyond the smartphone: How JioHotstar optimized its UX for foldables and tablets  |  Android Developers' Blog
url: https://developer.android.com/blog/posts/beyond-the-smartphone-how-jio-hotstar-optimized-its-ux-for-foldables-and-tablets
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Android Developers' Blog](https://developer.android.com/)
* [Blog](https://developer.android.com/blog)

Stay organized with collections

Save and categorize content based on your preferences.



#### [Case Studies](/blog/categories/case-studies)

# Beyond the smartphone: How JioHotstar optimized its UX for foldables and tablets

###### 3-min read

![](/static/blog/assets/beyond_Smartphone_e17b5979d9_ZBzwz8.webp)

26

Jan
2026

[![](/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)](/blog/authors/prateek-batra)

[##### Prateek Batra](/blog/authors/prateek-batra)

###### Developer Relations Engineer, Android Adaptive Apps

### **Beyond Phones: How JioHotstar Built an Adaptive UX**

[JioHotstar](https://play.google.com/store/apps/details?id=in.startv.hotstar) is a leading streaming platform in India, serving a user base exceeding 400 million. With a vast content library encompassing over 330,000 hours of video on demand (VOD) and real-time delivery of major sporting events, the platform operates at a massive scale.

To help ensure a premium experience for its vast audience, JioHotstar elevated the viewing experience by optimizing their app for foldables and tablets. They accomplished this by following Google’s adaptive app guidance and utilizing resources like  [samples](/design/ui/large-screens/samples), [codelabs](https://github.com/android/large-screen-codelabs), [cookbooks](/guide/topics/large-screens/large-screen-cookbook), and [documentation](/guide/topics/large-screens) to help create a consistently seamless and engaging experience across all display sizes.

### **JioHotstar's large screen challenge**

JioHotstar offered an excellent user experience on standard phones and the team wanted to take advantage of new form factors. To start, the team evaluated their app against the [large screen app quality guidelines](/docs/quality-guidelines/large-screen-app-quality) to understand the optimizations required to extend their user experience to foldables and tablets. To achieve [Tier 1](/docs/quality-guidelines/large-screen-app-quality#tier_1_best_large_screen_differentiated) large screen app status, the team implemented two strategic updates to adapt the app across various form factors and differentiate on foldables. By addressing the unique challenges posed by foldable and tablet devices, JioHotstar aims to deliver a high-quality and immersive experience across all display sizes and aspect ratios.

### **What they needed to do**

JioHotstar’s user interface, designed primarily for standard phone displays, encountered challenges in adapting hero image aspect ratios, menus, and show screens to the diverse screen sizes and resolutions of other form factors. This often led to image cropping, letterboxing, low resolution, and unutilized space, particularly in landscape mode. To help fully leverage the capabilities of tablets and foldables and deliver an optimized user experience across these device types, JioHotstar focused on refining the UI to ensure optimal layout flexibility, image rendering, and navigation across a wider range of devices.

### **What they did**

For a better viewing experience on large screens, JioHotstar took the initiative to enhance its app by incorporating [WindowSizeClass](/develop/ui/compose/layouts/adaptive/use-window-size-classes) and creating optimized layouts for compact, medium and extended widths. This allowed the app to adapt its user interface to various screen dimensions and aspect ratios, ensuring a consistent and visually appealing UI across different devices.

JioHotstar followed this pattern using Material 3 Adaptive library to know how much space the app has available. First invoking the [currentWindowAdaptiveInfo()](/reference/kotlin/androidx/compose/material3/adaptive/package-summary#currentWindowAdaptiveInfo(kotlin.Boolean)) function, then using new layouts accordingly for the three window size classes:

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

The breakpoints are in order, from the biggest to the smallest, as internally the API checks for with a greater or equal then, so any width that is at least greater or equal then `EXPANDED` will always be greater than `MEDIUM`.

JioHotstar is able to provide the premium experience unique to foldable devices: [Tabletop Mode](/develop/ui/compose/layouts/adaptive/foldables/make-your-app-fold-aware#tabletop_posture). This feature conveniently relocates the video player to the top half of the screen and the video controls to the bottom half when a foldable device is partially folded for a handsfree experience.

[](/static/blog/assets/videos/Hotstar_Fixed_size_v3_opt_9d3f7d9f17/Hotstar_Fixed_size_v3_opt_9d3f7d9f17.mp4)

To accomplish this, also using the Material 3 Adaptive library, the same [currentWindowAdaptiveInfo()](/reference/kotlin/androidx/compose/material3/adaptive/Posture#isTabletop()) can be used to query for the tabletop mode. Once the device is held in tabletop mode, a change of layout to match the top and bottom half of the posture can be done with a column to place the player in the top half and the controllers in the bottom half:

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

JioHotstar is now meeting the [Large Screen app quality guidelines](/docs/quality-guidelines/large-screen-app-quality) for Tier 1. The team leveraged [adaptive app](/adaptive-apps) guidance, utilizing [samples](/design/ui/large-screens/samples), [codelabs](https://github.com/android/large-screen-codelabs), [cookbooks](/guide/topics/large-screens/large-screen-cookbook), and [documentation](/guide/topics/large-screens) to incorporate these recommendations.

To further improve the user experience, JioHotstar increased touch target sizes, to the recommended 48dp, on video discovery pages, ensuring accessibility across large screen devices. Their video details page is now adaptive, adjusting to screen sizes and orientations. They moved beyond simple image scaling, instead leveraging window size classes to detect window size and density in real time and load the most appropriate hero image for each form factor, helping to enhance visual fidelity. Navigation was also improved, with layouts adapting to suit different screen sizes.

Now users can view their favorite content from JioHotstar on large screens devices with an improved and highly optimized viewing experience.

*"Achieving Tier 1 large screen app status with Google is a milestone that reflects the strength of our shared vision. At JioHotstar, we have always believed that optimizing for large screen devices goes beyond adaptability, it’s about elevating the viewing experience for audiences who are rapidly embracing foldables, tablets, and connected TVs.*

*Leveraging Google's Jetpack libraries and guides allowed us to combine our insights on content consumption with their expertise in platform innovation. This collaboration allowed both teams to push boundaries, address gaps, and co-create a seamless, immersive experience across every screen size.*

*Together, we’re proud to bring this enhanced experience to millions of users and to set new benchmarks in how India and the world experience streaming."*  
*-* Sonu Sanjeev, Senior Software Development Engineer

###### Written by:

* ## [Prateek Batra](/blog/authors/prateek-batra)

  ###### Developer Relations Engineer

  [read\_more
  View profile](/blog/authors/prateek-batra)

  ![](/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)

  ![](/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)

## Continue reading

* [![](/static/blog/assets/1_1_U4_K_Lr4r_A_Kx_Pq0_Crp_L3vr_Q_a4d1920594_2dcD9g.webp)](/blog/authors/ben-weiss)

  30

  Mar
  2026

  30

  Mar
  2026

  ![](/static/blog/assets/monzo_boosts_performance_aff3a37917_6VY99.webp)

  #### [Case Studies](/blog/categories/case-studies)

  ## [Monzo boosts performance metrics by up to 35% with a simple R8 update](/blog/posts/monzo-boosts-performance-metrics-by-up-to-35-with-a-simple-r8-update)

  [arrow\_forward](/blog/posts/monzo-boosts-performance-metrics-by-up-to-35-with-a-simple-r8-update)

  Monzo is a UK digital bank with 15 million customers and growing. As the app scaled, the engineering team identified app startup time as a critical area for improvement but worried it would require significant changes to their codebase.

  ###### [Ben Weiss](/blog/authors/ben-weiss) • 2 min read
* [![](/static/blog/assets/Ben_Trengrove_b9e17c8c2e_2uVqlp.webp)](/blog/authors/ben-trengrove)[![](/static/blog/assets/Ajesh_R_Pai_fc75c62777_Z1G5g2B.webp)](/blog/authors/ajesh-pai)

  13

  Mar
  2026

  13

  Mar
  2026

  ![](/static/blog/assets/tiktok_Case_Study_ae91bba156_1Bjq08.webp)

  #### [Case Studies](/blog/categories/case-studies)

  ## [TikTok reduces code size by 58% and improves app performance for new features with Jetpack Compose](/blog/posts/tiktok-reduces-code-size-and-improves-app-performance-for-new-features-with-jetpack-compose)

  [arrow\_forward](/blog/posts/tiktok-reduces-code-size-and-improves-app-performance-for-new-features-with-jetpack-compose)

  TikTok is a global short-video platform known for its massive user base and innovative features.

  ###### [Ben Trengrove](/blog/authors/ben-trengrove), [Ajesh Pai](/blog/authors/ajesh-pai) • 2 min read
* [![](/static/blog/assets/Mayuri_Khinvasara_Khabya_92848b1e1b_1xSr0w.webp)](/blog/authors/mayuri-khabya)

  05

  Mar
  2026

  05

  Mar
  2026

  ![](/static/blog/assets/meta_Header_2ac893569c_ZLkD4s.webp)

  #### [Case Studies](/blog/categories/case-studies)

  ## [Instagram and Facebook deliver instant playback and boost user engagement with Media3 PreloadManager](/blog/posts/instagram-and-facebook-deliver-instant-playback-and-boost-user-engagement-with-media3-preload-manager)

  [arrow\_forward](/blog/posts/instagram-and-facebook-deliver-instant-playback-and-boost-user-engagement-with-media3-preload-manager)

  In the dynamic world of social media, user attention is won or lost quickly. Meta apps (Facebook and Instagram) are among the world's largest social platforms and serve billions of users globally.

  ###### [Mayuri Khinvasara Khabya](/blog/authors/mayuri-khabya) • 4 min read

# Stay in the loop

Get the latest Android development insights delivered to your inbox
weekly.

[mail
Subscribe](/subscribe)

![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)