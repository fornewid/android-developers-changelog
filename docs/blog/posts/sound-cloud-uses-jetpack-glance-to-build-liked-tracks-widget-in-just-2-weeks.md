---
title: https://developer.android.com/blog/posts/sound-cloud-uses-jetpack-glance-to-build-liked-tracks-widget-in-just-2-weeks
url: https://developer.android.com/blog/posts/sound-cloud-uses-jetpack-glance-to-build-liked-tracks-widget-in-just-2-weeks
source: md.txt
---

[Case Studies](https://developer.android.com/blog/categories/case-studies)

# SoundCloud uses Jetpack Glance to build Liked Tracks widget in just 2 weeks

3 min read ![](https://developer.android.com/static/blog/assets/soundcloud_Jet_Pack_8602d748f3_1zRpWT.webp) 04 Mar 2025 [![View Summers Pittman's profile](https://developer.android.com/static/blog/assets/Summers_Pittman_e1dd057c92_Z1pDsqU.webp)](https://developer.android.com/blog/authors/summers-pittman)[![View Tracy Agyemang's profile](https://developer.android.com/static/blog/assets/Tracy_Agyemang_Headshot_9a0c523435_1hBimO.webp)](https://developer.android.com/blog/authors/tracy-agyemang) [Summers Pittman](https://developer.android.com/blog/authors/summers-pittman) \& [Tracy Agyemang](https://developer.android.com/blog/authors/tracy-agyemang) To make it even easier for users to listen on Android, developers at [SoundCloud](https://soundcloud.com/) --- an artist-first music platform --- turned to [Jetpack Glance](https://developer.android.com/develop/ui/compose/glance) to create a Liked Tracks widget for their highly-rated app, which boasts 4.6 stars and over 100 million downloads. With a catalog of over 400 million tracks from more than 40 million creators, SoundCloud is dedicated to connecting artists and fans through music, and this latest update to its Android app offers listeners an even more convenient way to enjoy their favorite tracks. **Propelled by Glance, the team was able to complete the project in just two weeks, saving precious development time and boosting engagement.**

<br />

[Video](https://www.youtube.com/watch?v=JAafI2DuxKI)

<br />

## Maximize visibility with user-friendly touchpoints

By showcasing the artwork of their recently liked tracks, the new Liked Tracks widget allows users to to jump directly to a specific song or access their full track list right from their home screen. This keeps SoundCloud front and center for listeners, acting as a shortcut to their personal libraries and encouraging them to tune back in.

Liked Tracks isn't SoundCloud's first widget. Over a decade ago, SoundCloud developers used RemoteViews to create a Player widget that let users easily control playback and like tracks. After recently updating the Player widget based on design feedback, developers made sure to prioritize a personalized interface for Liked Tracks. The new widget features both light and dark modes, resizes freely to accommodate user preferences, and dynamically adapts its theme to complement the user's wallpaper. Backed by Glance, these design choices ensured the widget isn't just seamless to use but also serves as an appealing and tailored gateway into the SoundCloud app.
![souncloudJetPack2.png](https://developer.android.com/static/blog/assets/souncloud_Jet_Pack2_9e2d2f9827_1Gp5no.webp) SoundCloud's Liked Tracks widget in action.

## Accelerate development cycles with Glance

Glance also played a crucial role in streamlining the development of Liked Tracks. For developers already proficient in Compose, Glance's intuitive design felt familiar, minimizing the learning curve and accelerating the team's onboarding. The platform's collection of code samples provided a useful starting point, too, helping developers quickly grasp its capabilities and best practices. "Using sample app repositories is a great way to learn. I can check out an entire repository and inspect how the code operates," said Sigute Kateivaite, lead SoundCloud engineer on the Android team. "It sped up our widget development by a lot."
![SoundCloudJetPack3.png](https://developer.android.com/static/blog/assets/Sound_Cloud_Jet_Pack3_2faacf3a06_1oK7UO.webp)

The declarative nature of Glance's UI was especially beneficial to developers. Because they didn't have to use additional XML files when building, developers could create cleaner, more readable code with less boilerplate. Glance also allowed them to work with modules separately, meaning components could be written and integrated one at a time and reused for later iterations. By isolating components, developers could quickly test modules, identify and resolve issues, and build for different states without duplication, leading to more efficient workflows.

Glance's design also improved the overall code quality. The ability to make changes using Android Studio's support for Glance's real-time preview enabled developers to build components in isolation without needing to integrate the UI component into the widget or deploy the full widget on the phone. They could represent various states, view all relevant cases, and review changes to components without having to compile the full app. Put simply, Glance made developers more productive because it allowed them to iterate faster, refining the widget for a more polished final product.

## Elevate app widgets with the power of Glance

With effective new workflows and no major development issues, the SoundCloud team applauds Glance for streamlining a successful production. "With the new Liked Tracks widget, rollout has been really stable," Sigute said. "Development and the testing process went really smoothly." Early data also shows promising results --- active users now interact with the widget to access the app multiple times a day on average.
![SoundCloud4.png](https://developer.android.com/static/blog/assets/Sound_Cloud4_a50166d986_Z20fTnb.webp) 2X average daily active user interaction with widget feature.

Looking ahead, the SoundCloud team is eager to employ more of Glance to improve existing widgets, like adopting canonical layouts, and even develop new ones. While the current Liked Tracks widget focuses primarily on image display, the team is interested in including other types of content to further enrich user experience. Developers also hope to migrate the Player widget over to Glance to access the framework's robust theming options, simplify resizing processes, and address some long-standing bugs.

Beyond the Liked Tracks and Player features, the team is excited about the potential of using Glance to build a wider range of widgets. The modular, component-based architecture of the Liked Tracks widget, with reusable elements like UserAvatar and Logo, offers a solid foundation for future development, promising to simplify processes from the start.

## Get started building custom app widgets with Jetpack Glance

Rapidly develop and deploy widgets that keep your app visible and engaging with [Glance](https://developer.android.com/jetpack/androidx/releases/glance).

*** ** * ** ***

*This blog post is part of our series: **Spotlight Week on Widgets**, where we provide resources---blog posts, videos, sample code, and more---all designed to help you design and create widgets. You can *[*read more in the overview of Spotlight Week: Widgets*](https://android-developers.googleblog.com/2025/03/spotlight-week-widgets.html)*, which will be updated throughout the week.*
- [#Jetpack](https://developer.android.com/blog/topics/jetpack)
- [#Widgets](https://developer.android.com/blog/topics/widgets)
Written by:

-

  ## [Summers Pittman](https://developer.android.com/blog/authors/summers-pittman)

  ###### Technical Solutions Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/summers-pittman) ![View Summers Pittman's profile](https://developer.android.com/static/blog/assets/Summers_Pittman_e1dd057c92_Z1pDsqU.webp) ![View Summers Pittman's profile](https://developer.android.com/static/blog/assets/Summers_Pittman_e1dd057c92_Z1pDsqU.webp)
-

  ## [Tracy Agyemang](https://developer.android.com/blog/authors/tracy-agyemang)

  ###### Product Marketing Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/tracy-agyemang) ![View Tracy Agyemang's profile](https://developer.android.com/static/blog/assets/Tracy_Agyemang_Headshot_9a0c523435_1hBimO.webp) ![View Tracy Agyemang's profile](https://developer.android.com/static/blog/assets/Tracy_Agyemang_Headshot_9a0c523435_1hBimO.webp)
Continue reading
- [![View Thomas Ezan's profile](https://developer.android.com/static/blog/assets/thomas_ezan_d29c7508d0_l9O72.webp)](https://developer.android.com/blog/authors/thomas-ezan)[![View Tracy Agyemang's profile](https://developer.android.com/static/blog/assets/Tracy_Agyemang_Headshot_9a0c523435_1hBimO.webp)](https://developer.android.com/blog/authors/tracy-agyemang) 04 May 2026 04 May 2026 ![](https://developer.android.com/static/blog/assets/AANDDM_KARROT_Strapi_eed79b0e1b_cCxXk.webp) [Case Studies](https://developer.android.com/blog/categories/case-studies)

  ## [Gemini and Firebase AI Logic enabled Karrot to increase sales with a translation feature built in under 2 weeks](https://developer.android.com/blog/posts/gemini-and-firebase-ai-logic-enabled-karrot-to-increase-sales-with-a-translation-feature)

  [arrow_forward](https://developer.android.com/blog/posts/gemini-and-firebase-ai-logic-enabled-karrot-to-increase-sales-with-a-translation-feature) Karrot is a hyperlocal, community-driven peer-to-peer marketplace app that enables users to buy, sell, and trade items with other verified users. Since launching in South Korea in 2015, the platform has expanded into global markets, amassing over 43 million registered users.
  [Thomas Ezan](https://developer.android.com/blog/authors/thomas-ezan), [Tracy Agyemang](https://developer.android.com/blog/authors/tracy-agyemang) • 2 min read
  - [#Android](https://developer.android.com/blog/topics/android)
- [![View Ben Weiss's profile](https://developer.android.com/static/blog/assets/1_1_U4_K_Lr4r_A_Kx_Pq0_Crp_L3vr_Q_a4d1920594_2dcD9g.webp)](https://developer.android.com/blog/authors/ben-weiss)[![View Tracy Agyemang's profile](https://developer.android.com/static/blog/assets/Tracy_Agyemang_Headshot_9a0c523435_1hBimO.webp)](https://developer.android.com/blog/authors/tracy-agyemang) 30 Mar 2026 30 Mar 2026 ![](https://developer.android.com/static/blog/assets/monzo_boosts_performance_aff3a37917_6VY99.webp) [Case Studies](https://developer.android.com/blog/categories/case-studies)

  ## [Monzo boosts performance metrics by up to 35% with a simple R8 update](https://developer.android.com/blog/posts/monzo-boosts-performance-metrics-by-up-to-35-with-a-simple-r8-update)

  [arrow_forward](https://developer.android.com/blog/posts/monzo-boosts-performance-metrics-by-up-to-35-with-a-simple-r8-update) Monzo is a UK digital bank with 15 million customers and growing. As the app scaled, the engineering team identified app startup time as a critical area for improvement but worried it would require significant changes to their codebase.
  [Ben Weiss](https://developer.android.com/blog/authors/ben-weiss), [Tracy Agyemang](https://developer.android.com/blog/authors/tracy-agyemang) • 2 min read
- [![View Mayuri Khinvasara Khabya's profile](https://developer.android.com/static/blog/assets/Mayuri_Khinvasara_Khabya_92848b1e1b_1xSr0w.webp)](https://developer.android.com/blog/authors/mayuri-khabya)[![View Tracy Agyemang's profile](https://developer.android.com/static/blog/assets/Tracy_Agyemang_Headshot_9a0c523435_1hBimO.webp)](https://developer.android.com/blog/authors/tracy-agyemang) 05 Mar 2026 05 Mar 2026 ![](https://developer.android.com/static/blog/assets/meta_Header_2ac893569c_ZLkD4s.webp) [Case Studies](https://developer.android.com/blog/categories/case-studies)

  ## [Instagram and Facebook deliver instant playback and boost user engagement with Media3 PreloadManager](https://developer.android.com/blog/posts/instagram-and-facebook-deliver-instant-playback-and-boost-user-engagement-with-media3-preload-manager)

  [arrow_forward](https://developer.android.com/blog/posts/instagram-and-facebook-deliver-instant-playback-and-boost-user-engagement-with-media3-preload-manager) In the dynamic world of social media, user attention is won or lost quickly. Meta apps (Facebook and Instagram) are among the world's largest social platforms and serve billions of users globally.
  [Mayuri Khinvasara Khabya](https://developer.android.com/blog/authors/mayuri-khabya), [Tracy Agyemang](https://developer.android.com/blog/authors/tracy-agyemang) • 4 min read
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)