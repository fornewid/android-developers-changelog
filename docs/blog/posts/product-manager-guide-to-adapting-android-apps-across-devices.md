---
title: https://developer.android.com/blog/posts/product-manager-guide-to-adapting-android-apps-across-devices
url: https://developer.android.com/blog/posts/product-manager-guide-to-adapting-android-apps-across-devices
source: md.txt
---

#### [Product News](https://developer.android.com/blog/categories/product-news)

# A product manager's guide to adapting Android apps across devices

###### 6-min read

![](https://developer.android.com/static/blog/assets/across_Devices_1742e15ff4_ZE5L7I.webp) 10 Jun 2025 [![](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z15U8cx.webp)](https://developer.android.com/blog/authors/fahd-imtiaz) [##### Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz)

###### Senior Product Manager

*Today, Android is launching a few updates across the platform! This includes the start of Android 16's rollout, with details for both *[*developers*](https://android-developers.googleblog.com/2025/06/android-16-is-here.html)* and *[*users*](https://blog.google/products/android/android-16)*, a *[*Developer Preview for enhanced Android desktop experiences with connected displays*](https://android-developers.googleblog.com/2025/06/developer-preview-enhanced-android-desktop-experiences-connected-displays.html)*, and *[*updates for Android users across Google apps and more*](https://blog.google/products/android/new-android-features-june-2025/)*, plus the *[*June Pixel Drop*](https://blog.google/products/pixel/pixel-drop-june-2025/)*. We're also *[*recapping all the Google I/O updates for Android developers focused on building excellent, adaptive Android apps*](https://android-developers.googleblog.com/2025/06/top-3-updates-for-building-excellent-adaptive-apps-google-io-25.html)*.*

With new form factors emerging continually, the Android ecosystem is more dynamic than ever.

From phones and foldables to tablets, Chromebooks, TVs, cars, Wear and XR, Android users expect their apps to run seamlessly across an increasingly diverse range of form factors. Yet, many Android apps fall short of these expectations as they are built with UI constraints such as being locked to a single orientation or restricted in resizability.

With this in mind, [Android 16 introduced API changes](https://android-developers.googleblog.com/2025/01/orientation-and-resizability-changes-in-android-16.html) for apps targeting SDK level 36 to ignore orientation and resizability restrictions starting with large screen devices, shifting toward a unified model where adaptive apps are the norm. This is the moment to move ahead. Adaptive apps aren't just the future of Android, they're the expectation for your app to stand out across Android form factors.

## Why you should prioritize adaptive now

![500-plus-devices.png](https://developer.android.com/static/blog/assets/500_plus_devices_6428a9ddd7_Z2f6hLh.webp)

*Source: internal Google data*

Prioritizing optimizations to make your app *adaptive* isn't just about keeping up with [the orientation and resizability API changes in Android 16](https://android-developers.googleblog.com/2025/01/orientation-and-resizability-changes-in-android-16.html) for apps targeting SDK 36. Adaptive apps unlock tangible benefits across user experience, development efficiency, and market reach.

- **Mobile apps can now reach users on over 500 million active large screen devices:** Mobile apps run on foldables, tablets, Chromebooks, and even compatible cars, with minimal changes. Android 16 will introduce significant advancements in desktop windowing for a true desktop-like experience on large screens, including connected displays. And Android XR opens a new dimension, allowing your existing apps to be available in immersive environments. The user expectation is clear: a consistent, high-quality experience that intelligently adapts to any screen -- be it a foldable, a tablet with a keyboard, or a movable, resizable window on a Chromebook.
- **"The new baseline" with orientation and resizability API changes in Android 16:** We believe mobile apps are undergoing a shift to have UI adapt responsively to any screen size, just like websites. Android 16 will ignore app-defined restrictions like fixed orientation (portrait-only) and non-resizable windows, beginning with large screens (smallest width of the device is \>= 600dp) including tablets and inner displays on foldables. For most apps, it's key to helping them stretch to any screen size. In some cases if your app isn't adaptive, it could deliver a broken user experience on these screens. This moves adaptive design from a nice-to-have to a foundational requirement.

![goodbye.png](https://developer.android.com/static/blog/assets/goodbye_80078e92da_Z1xEPSX.webp)

- **Increase user reach and app discoverability in Play:** Adaptive apps are better positioned to be ranked higher in Play, and featured in editorial articles across form factors, reaching a wider audience across Play search and homepages. Additionally, Google Play Store surfaces ratings and reviews across all form factors. If your app is not optimized, a potential user's first impression might be tainted by a 1-star review complaining about a stretched UI on a device they don't even own yet. Users are also more likely to engage with apps that provide a great experience across their devices.
- **Increased engagement on large screens:** Users on large screen devices often have different interaction patterns. On large screens, users may engage for longer sessions, perform more complex tasks, and consume more content.

[**Concepts saw a 70% increase in user engagement**](https://www.youtube.com/watch?v=WSnfe3KiXbg) on large screens after optimizing.  
Usage for 6 major media streaming apps in the US was up to **3x more for tablet and phone users**, as compared to phone only users.

- **More accessible app experiences:** According to the World Bank, [15%](https://www.worldbank.org/en/news/immersive-story/2022/02/15/an-accessible-future-for-persons-with-disabilities-what-does-it-take#:~:text=10%20Commitments%0Aon%20Disability%2DInclusion) of the world's population has some type of disability. People with disabilities depend on apps and services that support accessibility to communicate, learn, and work. Matching the user's preferred orientation improves the accessibility of applications, helping to create an inclusive experience for all.

## Today, most apps are building for smartphones only

![android-16-form-factors_2.png](https://developer.android.com/static/blog/assets/android_16_form_factors_2_a6f81b479e_Z1eUyG0.webp)

*"...looking at the number of users, the ROI does not justify the investment".*

That's a frequent pushback from product managers and decision-makers, and if you're just looking at top-line analytics comparing the number of tablet sessions to smartphone sessions, it might seem like a closed case.

While top-line analytics might show lower session numbers on tablets compared to smartphones, concluding that large screens aren't worth the effort based solely on current volume can be a trap, causing you to miss out on valuable engagement and future opportunities.

Let's take a deeper look into why:

1. **The user experience 'chicken and egg' loop:** Is it possible that the low usage is a symptom rather than the root cause? Users are quick to abandon apps that feel clunky or broken. If your app on large screens is a stretched-out phone interface, the app likely provides a negative user experience. The lack of users might reflect the lack of a good experience, not always necessarily lack of potential users.

2. **Beyond user volume, look at user engagement:** Don't just count users, analyze their worth. Users interact with apps on large screens differently. The large screen often leads to longer sessions and more immersive experiences. As mentioned above, usage data shows that engagement time increases significantly for users who interact with apps on both their phone and tablet, as compared to phone only users.

3. **Market evolution:** The Android device ecosystem is continuing to evolve. With the rise of foldables, upcoming [connected displays support](https://android-developers.googleblog.com/2025/06/developer-preview-enhanced-android-desktop-experiences-connected-displays.html) in Android 16, and form factors like XR and Android Auto, adaptive design is now more critical than ever. Building for a specific screen size creates technical debt, and may slow your development velocity and compromise the product quality in the long run.

## Okay, I am convinced. Where do I start?

![three-step-workflow.png](https://developer.android.com/static/blog/assets/three_step_workflow_d6b69bf56a_Z20A1oX.webp)

For organizations ready to move forward, Android offers many resources and developer tools to optimize apps to be adaptive. See below for how to get started:

1. **Check how your app looks on large screens today:** Begin by looking at your app's current state on tablets, foldables (in different postures), Chromebooks, and environments like desktop windowing. Confirm if your app is available on these devices or if you are unintentionally leaving out these users by requiring [unnecessary features](https://android-developers.googleblog.com/2023/12/increase-your-apps-availability-across-device-types.html) within your app.
2. **Address common UI issues:** Assess what feels awkward in your app UI today. We have a lot of guidance available on how you can easily translate your mobile app to other screens.
   1. Check the [Large screens design gallery](https://developer.android.com/large-screens/gallery) for inspiration and understanding how your app UI can evolve across devices using proven solutions to common UI challenges.
   2. Start with quick wins. For example, prevent buttons from stretching to the full screen width, or switch to a vertical navigation bar on large screens to improve ergonomics.
   3. Identify patterns where [canonical layouts](https://developer.android.com/develop/ui/compose/layouts/adaptive/canonical-layouts) (e.g. list-detail) could solve any UI awkwardness you identified. Could a list-detail view improve your app's navigation? Would a supporting pane on the side make better use of the extra space than a bottom sheet?
3. **Optimize your app incrementally, screen by screen:** It may be helpful to prioritize how you approach optimization because not everything needs to be perfectly adaptive on day one. Incrementally improve your app based on what matters most -- it's not all or nothing.
   1. Start with the foundations. Check out the [large screen app quality guidelines](https://developer.android.com/docs/quality-guidelines/large-screen-app-quality) which tier and prioritize the fixes that are most critical to users. Remove orientation restrictions to support portrait and landscape, and ensure support for resizability (for when users are in split screen), and prevent major stretching of buttons, text fields, and images. These foundational fixes are critical, especially with API changes in Android 16 that will make these aspects even more important.
   2. Implement adaptive layout optimizations with a focus on core user journeys or screens first.
      1. Identify screens where optimizations (for example a [two-pane layout](https://m3.material.io/foundations/layout/canonical-layouts/list-detail)) offer the biggest UX win
      2. And then proceed to screens or parts of the app that are not as often used on large screens
   3. Support input methods beyond touch, including keyboard, mouse, trackpad, and stylus input. With new form factors and connected displays support, this sets users up to interact with your UI seamlessly.
   4. Add differentiating hero user experiences like support for tabletop mode or dual-screen mode on foldables. This can happen on a per-use-case basis - for example, tabletop mode is great for watching videos, and dual screen mode is great for video calls.

While there's an upfront investment in adopting adaptive principles (using tools like Jetpack Compose and window size classes), the long-term payoff may be significant. By designing and building features once, and letting them adapt across screen sizes, the benefits outweigh the cost of creating multiple bespoke layouts. Check out the adaptive apps [developer guidance](https://developer.android.com/adaptive-apps) for more.

## Unlock your app's potential with adaptive app design

The message for my fellow product managers, decision-makers, and businesses is clear: **adaptive design will up-level your app** for high-quality Android experiences in 2025 and beyond. An adaptive, responsive UI is the scalable way to support the many devices in Android without developing on a per-form factor basis. If you ignore the diverse device ecosystem of foldables, tablets, Chromebooks, and emerging form factors like XR and cars, your business is accepting hidden costs from negative user reviews, lower discovery in Play, increased technical debt, and missed opportunities for increased user engagement and user acquisition.

Maximize your apps' impact and unlock new user experiences. Learn more about [building adaptive apps](https://developer.android.com/adaptive-apps) today.

###### Written by:

-

  ## [Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz)

  ###### Senior Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/fahd-imtiaz) ![](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z15U8cx.webp) ![](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z15U8cx.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z15U8cx.webp)](https://developer.android.com/blog/authors/fahd-imtiaz) 19 Dec 2025 19 Dec 2025 ![](https://developer.android.com/static/blog/assets/Android_adaptives_festivity_01_blog_f70d48134f_Z2lMDgd.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Goodbye Mobile Only, Hello Adaptive: Three essential updates from 2025 for building adaptive apps](https://developer.android.com/blog/posts/goodbye-mobile-only-hello-adaptive)

  [arrow_forward](https://developer.android.com/blog/posts/goodbye-mobile-only-hello-adaptive) In 2025 the Android ecosystem has grown far beyond the phone. Today, developers have the opportunity to reach over 500 million active devices, including foldables, tablets, XR, Chromebooks, and compatible cars.

  ###### [Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz) •
  2 min read

  - [#Jetpack Navigation](https://developer.android.com/blog/topics/jetpack-navigation)
  - [#Adaptive apps](https://developer.android.com/blog/topics/adaptive-apps)
  - [#Compose](https://developer.android.com/blog/topics/compose)
  - [#Android 16](https://developer.android.com/blog/topics/android-16)
  - +2 ↩
- [![](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z15U8cx.webp)](https://developer.android.com/blog/authors/fahd-imtiaz)[![](https://developer.android.com/static/blog/assets/miguel_montemayor_552207c1c6_Z1tItyG.webp)](https://developer.android.com/blog/authors/miguel-montemayor) 03 Sep 2025 03 Sep 2025 ![](https://developer.android.com/static/blog/assets/yt_MBG_2_a56f169e60_ZSoFHF.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Unfold new possibilities with Compose Adaptive Layouts 1.2 beta](https://developer.android.com/blog/posts/unfold-new-possibilities-with-compose-adaptive-layouts)

  [arrow_forward](https://developer.android.com/blog/posts/unfold-new-possibilities-with-compose-adaptive-layouts) With new form factors like the Pixel 10 Pro Fold joining the Android ecosystem, adaptive app development is essential for creating high-quality user experiences across phones, tablets, and foldables.

  ###### [Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz), [Miguel Montemayor](https://developer.android.com/blog/authors/miguel-montemayor) •
  3 min read

- [![](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z15U8cx.webp)](https://developer.android.com/blog/authors/fahd-imtiaz) 20 May 2025 20 May 2025 ![](https://developer.android.com/static/blog/assets/yt_adaptive_b9097334d4_Z1poFG.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Google I/O 2025: Build adaptive Android apps that shine across form factors](https://developer.android.com/blog/posts/google-i-o-2025-build-adaptive-android-apps-that-shine-across-form-factors)

  [arrow_forward](https://developer.android.com/blog/posts/google-i-o-2025-build-adaptive-android-apps-that-shine-across-form-factors) At Google I/O this year, we are exploring how adaptive development isn't just a good idea, but essential to building apps that shine across the expanding Android device ecosystem.

  ###### [Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz) •
  5 min read

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)