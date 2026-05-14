---
title: https://developer.android.com/blog/posts/how-calm-reimagined-mindfulness-for-android-xr
url: https://developer.android.com/blog/posts/how-calm-reimagined-mindfulness-for-android-xr
source: md.txt
---

#### [Case Studies](https://developer.android.com/blog/categories/case-studies)

# How Calm Reimagined Mindfulness for Android XR

###### 4-min read

![](https://developer.android.com/static/blog/assets/how_Calm_edf30223a8_kG1yA.webp) 30 Oct 2025 [![](https://developer.android.com/static/blog/assets/Stevan_Silva_7661118077_V4WGm.webp)](https://developer.android.com/blog/authors/stevan-silva) [##### Stevan Silva](https://developer.android.com/blog/authors/stevan-silva)

###### Group Product Manager

[Calm](https://play.google.com/store/apps/details?id=com.calm.android) is a leading mental health and wellness company with over 180 million downloads. When they started their development for[Android XR,](https://developer.android.com/xr) their core engineering team was able to build their first functional XR orbiter menus on Day 1 and a core experience in just two weeks. This demonstrates that building for XR can be an [extension of existing Android development work,](https://developer.android.com/adaptive-apps) not something that has to be started from scratch. As a company dedicated to helping users sleep better, stress less, and live more mindfully, their extensive library has made Calm a trusted source for well-being content on Android.
[Video](https://www.youtube.com/watch?v=yUx8T06arKQ)

With the introduction of the [Android XR platform](https://android-developers.googleblog.com/2024/12/introducing-android-xr-sdk-developer-preview.html), the Calm team saw an opportunity to not just optimize their existing Android app, but to truly create the next generation of immersive experiences.

We sat down with Kristen Coke, Lead Product Manager, and Jamie Martini, Sr. Manager of Engineering at Calm, to dive into their journey building for Android XR and learn how other developers can follow their lead.
![calm.png](https://developer.android.com/static/blog/assets/calm_fe96e2fdff_263o2O.webp)

***Q: What was the vision for the Calm experience on Android XR, and how does it advance your mission?***

**A (Kristen Coke, Lead Product Manager):**Our mission is to support everyone on every step of their mental health journey. XR allows us to expand how people engage with our mindfulness content, creating an experience that wasn't just transportive but transformative.

If I had to describe it in one sentence, Calm on Android XR reimagines mindfulness for the world around you, turning any room into a fully immersive, multi-sensory meditation experience.

We wanted to create a version of Calm that couldn't exist anywhere else, a serene and emotionally intelligent sanctuary that users don't just want to visit, but will return to again and again.
![calm2.gif](https://developer.android.com/static/blog/assets/calm2_9a4a2fdb19_Div3v.webp)

***Q: For developers who might think building for XR is a massive undertaking, what was your initial approach to bringing your existing Android app over?***

**A (Jamie Martini, Sr. Manager of Engineering):** Our main goal was to [adapt our Android app](https://developer.android.com/develop/ui/compose/build-adaptive-apps) for XR and honestly, the process felt easy and seamless.

We already use [Jetpack Compose](https://developer.android.com/develop/ui/compose/documentation) extensively for our mobile app, so expanding that expertise into XR was the natural choice. It felt like extending our Android development, not starting from scratch. We were able to reuse a lot of our existing codebase, including our backend, media playback, and other core components, which dramatically cut down on the initial work.

The [Android XR design guides](https://developer.android.com/design/ui/xr/guides) provided valuable context throughout the process, helping both our design and development teams shape Calm's mobile-first UX into something natural and intuitive for a spatial experience.

***Q: You noted the process felt seamless. How quickly was your team able to start building and iterating on the core XR experience?***

**A (Jamie Martini, Sr. Manager of Engineering):**We were productive right away, building our first orbiter menus on day one and a core XR Calm experience in about two weeks. The ability to apply our existing Android and Jetpack experience directly to a spatial environment gave us a massive head start, making the time-to-first-feature incredibly fast.

***Q: Could you tell us about what you built to translate the Calm experience into this new spatial environment?***

**A (Jamie Martini, Sr. Manager of Engineering):**We wanted to take full advantage of the immersive canvas to rethink how users engage with our content.

Two of the key features we evolved were the Immersive Breathe Bubble and the Immersive Scene Experiences.

The Breathe Bubble is our beloved breathwork experience, but brought into 3D. It's a softly pulsing orb that anchors users to their breath with full environmental immersion.
![breathe_bubble.webp](https://developer.android.com/static/blog/assets/breathe_bubble_e363524e14_Z1affoD.webp)

And with our Immersive Scene Experiences, users can choose from a curated selection of ambient environments designed to gently wrap around them and fade into their physical environment. This was a fantastic way to take a proven 2D concept (the mobile app's customizable background scenes) and transform it for the spatial environment.

We didn't build new experiences from scratch; we simply evolved core, proven features to take advantage of the immersive canvas.

***Q: What were the keys to building a visually compelling experience that feels native to the Android XR platform?***

**A (Kristen Coke, Lead Product Manager):**Building for a human-scale, spatial environment required us to update our creative workflow.

We started with concept art to establish our direction, which we then translated into 3D models using a human-scale reference to ensure natural proportions and comfort for the user.

Then, we consistently tested the assets directly in a headset to fine-tune scale, lighting, and atmosphere. For developers who may not have a physical device, the [Android XR emulator](https://developer.android.com/develop/xr/jetpack-xr-sdk/studio-tools) is a helpful alternative for testing and debugging.

We quickly realized that in a multisensory environment, restraint was incredibly powerful. We let the existing content (the narration, the audio) amplify the environment, rather than letting the novelty of the 3D space distract from the mindfulness core.

***Q: How would you describe the learning curve for other developers interested in building for XR? Do you have any advice?***

**A (Jamie Martini, Sr. Manager of Engineering)**: This project was the first step into immersive platforms for our Android engineering team, and we were pleasantly surprised. The APIs were very easy to learn and use and felt consistent with other Jetpack libraries.

My advice to other developers? Begin by integrating the[Jetpack XR APIs](https://developer.android.com/develop/xr/jetpack-xr-sdk) into your existing Android app and reusing as much of your existing code as possible. That is the quickest way to get a functional prototype.

**A (Kristen Coke, Lead Product Manager)**: Think as big as possible. Android XR gave us a whole new world to build our app within. Teams should ask themselves: What is the biggest, boldest version of your experience that you could possibly build? This is your opportunity to finally put into action what you've always wanted to do, because now, you have the platform that can make it real.
![calm4.png](https://developer.android.com/static/blog/assets/calm4_7e5a953563_Z1CipDV.webp)

**Building the next generation of spatial experiences**

The work the Calm team has done showcases how building on the [Android XR platform](https://developer.android.com/xr) can be a natural extension of your existing Android expertise. By leveraging the [Jetpack XR SDKs](https://developer.android.com/develop/xr/jetpack-xr-sdk), Calm quickly evolved their core mobile features into a stunning spatial experience.

If you're ready to get started, you can find all the resources you need at[developer.android.com/xr](https://developer.android.com/xr). Head over there to download the latest SDK, explore our documentation, and start building today.

###### Written by:

-

  ## [Stevan Silva](https://developer.android.com/blog/authors/stevan-silva)

  ###### Group Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/stevan-silva) ![](https://developer.android.com/static/blog/assets/Stevan_Silva_7661118077_V4WGm.webp) ![](https://developer.android.com/static/blog/assets/Stevan_Silva_7661118077_V4WGm.webp)

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