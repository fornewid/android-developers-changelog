---
title: https://developer.android.com/blog/posts/17-things-to-know-for-android-developers-at-google-i-o
url: https://developer.android.com/blog/posts/17-things-to-know-for-android-developers-at-google-i-o
source: md.txt
---

#### [Product News](https://developer.android.com/blog/categories/product-news)

# 17 Things to know for Android developers at Google I/O!

###### 8-min read

![](https://developer.android.com/static/blog/assets/Google_For_Developers_Android_Text_Strapi_2000x1000_2d4221d884_ZtW7eg.webp) 19 May 2026 [![](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_Z1Fsr5h.webp)](https://developer.android.com/blog/authors/matthew-mccullough) [##### Matthew McCullough](https://developer.android.com/blog/authors/matthew-mccullough)

###### Vice President, Product Management, Android Developer

Today at [Google I/O,](https://io.google/2026/) we announced the many ways we're powering agentic workflows to increase your productivity and ensure your apps shine across the expanding Android ecosystem. Here's a recap of 17 of our favorite announcements for Android developers; you can also [see what was announced last week](https://www.youtube.com/live/KvTRMSa1w4E?si=QBAxNvihPwJCJUuS) in [The Android Show: I/O Edition](https://developer.android.com/events/show). Stay tuned over the next two days as we dive into all of the topics in more detail!

## Build High Quality Android Apps Using Agents

#### 1: Android CLI: helping you build with any agent, LLM, and tool

[Android CLI is now stable](https://goo.gle/CLI_IO26). It offers programmatic tools that allow any AI agent, including Claude Code, Codex, or Antigravity, to perform core Android tasks much more easily and efficiently. With today's release, it also provides a bridge to tap directly into the "heavy-lifting" power of Android Studio to give you the production-ready polish needed for professional Android development. By leveraging the new android studio commands, developers can now grant their preferred agents the ability to perform semantic symbol resolution, analyze files for warnings, and even render Jetpack Compose previews. This release also enables official support for "Journeys" through new [Android skills](https://developer.android.com/tools/agents/android-skills), which enables agents to execute end-to-end UI tests under your direction. Watch the [developer keynote](https://www.youtube.com/watch?v=aqmpZocmR8o&list=PLOU2XLYxmsIKL_eEgkKJWDRhYUEvS9eYz&index=23), and tune into the [What's New in Android tools talk](https://io.google/2026/explore/pa-keynote-7) for more information.
![agy-android-cli.png](https://developer.android.com/static/blog/assets/agy_android_cli_8f92771623_ZGwXdW.webp) You can now easily install Android CLI for use with Google Antigravity 2.0

#### 2: Build production-ready apps with ease in Google AI Studio

Developers and creators can now [build native Android apps, starting with a prompt in Google AI Studio](http://android-developers.googleblog.com/2026/05/build-android-apps-google-ai-studio.html). The apps are built with development best practices like Jetpack Compose, Kotlin, and APIs that leverage our recommended developer patterns. Google AI Studio enables developers to prototype, iterate via an embedded emulator, and deploy to physical devices without heavy local installations. Developers are then able to take those apps and share them to Android devices, as well as share them with others for testing through Google Play Console's internal testing track. If a developer wants to prepare their app for a wider release, they're able to take it to Android Studio for advanced debugging, testing, and UI polish. Watch the [developer keynote](https://www.youtube.com/watch?v=aqmpZocmR8o&list=PLOU2XLYxmsIKL_eEgkKJWDRhYUEvS9eYz&index=23), and tune into the [What's New in Android tools talk](https://io.google/2026/explore/pa-keynote-7) for more information.
![image1-.gif](https://developer.android.com/static/blog/assets/image1_705721184b_1rdgJG.webp) Use the embedded Android Emulator to create Android apps in Google AI Studio

#### 3: Accelerating AI coding assistance with Android Bench

[Android Bench](http://d.android.com/bench) is our LLM leaderboard for Android development challenges. The goal is to accelerate model improvements, so you have more useful options for AI assistance. Many of you have been using open-weight models for AI assistance, so we're now adding commonly used ones, such as Gemma 4, to the leaderboard, so you can see how LLMs that offer offline access and additional flexibility for power-users measure up. We're continuously working on increasing the difficulty of challenges we're giving LLMs, to continue encouraging more useful improvements.

#### 4: Convert iOS apps to Android with the Migration Assistant in Android Studio

The Migration Assistant in Android Studio is designed to port apps from platforms like iOS, React Native, or web frameworks to native Android. By simply selecting an existing project, developers can have the agent intelligently map features, convert assets like storyboards and SVGs, and implement Android best practices using Jetpack Compose and our recommended Jetpack libraries. This will effectively transform what used to be weeks of manual porting into a streamlined agentic workflow that only takes hours. We shared a preview of this upcoming feature in the [developer keynote](https://www.youtube.com/watch?v=aqmpZocmR8o&list=PLOU2XLYxmsIKL_eEgkKJWDRhYUEvS9eYz&index=23).
![IO26_DEV_Android_MOD_v29_27hi.gif](https://developer.android.com/static/blog/assets/IO_26_DEV_Android_MOD_v29_27hi_c2728b60bd_1uJVdJ.webp) A sneak peek of the Migration Assistant converting an iOS app into a native Android app

## Building AI into your apps

#### 5: Building Intelligent Apps with generative AI

Generative AI enables you to create apps that are more intelligent, personalized, and agentic than ever before. This year, we introduced the latest advancements in on-device intelligence with a preview of Gemini Nano 4 for tasks like data extraction and summarization. We also expanded cloud capabilities via Firebase AI Logic, allowing developers to leverage Gemini models with robust grounding (including URL, Maps, and web search) to build smarter, more capable assistants. Furthermore, we unveiled our hybrid inference approach and the new Agent Development Kit (ADK) for Android, alongside communication protocols like AG-UI and A2UI that simplify the creation of autonomous, agentic experiences. To start integrating these powerful features, explore the [developer documentation](https://developer.android.com/ai), and watch the technical deep dive session where we showcase all these technologies.

#### 6: Experiment with AppFunctions today

AppFunctions is an [Android platform API](https://developer.android.com/reference/android/app/appfunctions/package-summary) with an accompanying [Jetpack library](https://developer.android.com/jetpack/androidx/releases/appfunctions) to simplify building Android MCP integrations. It empowers your apps to behave like on device MCP servers, contributing functions that act as tools for use by agents and assistants. AppFunctions integration with Gemini is currently in a private preview with trusted testers, and you can begin preparing your apps already. You can sign up for the [Early Access Program](http://goo.gle/eap-af) and start experimenting using the [API guidance](http://d.android.com/ai/appfunctions), [sample](http://github.com/android/app-functions), and [skill](https://github.com/android/skills/blob/main/device-ai/appfunctions/SKILL.md) today.

## The Future is Adaptive

#### 7: Android is now Compose First; Views are now in maintenance mode.

Compose is our standard for UI development, and we are moving to a Compose-first approach for all future guidance and libraries. Building on five years of evolution, the latest releases deliver a mature toolkit, from the highly customizable Styles API to refined shared element transitions and enhanced input support. These updates allow you to build beautiful, adaptive apps with less code and better performance. Learn more about what Compose-first means for Android Development in [our blog post](http://android-developers.googleblog.com/2026/05/android-ui-development-is-compose-first.html).
![image5.png](https://developer.android.com/static/blog/assets/image5_b94c904f85_1rJTxU.webp) Build Android UI with Compose

#### 8: Building seamless Android experiences across devices with Jetpack Compose

The Android ecosystem is now [adaptive by default](https://goo.gle/AdaptiveApps_IO26), moving fluidly across phones, foldables, tablets, cars, XR, and expanding usages with [Googlebook](https://developer.android.com/googlebook) and connected displays. With over 580 million large-screen devices, and users on multiple devices spending up to 14x more on apps, the investment in adaptive design presents a massive opportunity. [Jetpack Compose](https://developer.android.com/compose) is the definitive engine for this transition, offering core tools like our latest [Jetpack Navigation 3](http://goo.gle/nav3) release, new experimental [Grid](https://developer.android.com/develop/ui/compose/layouts/adaptive/grid) and [FlexBox](https://developer.android.com/develop/ui/compose/layouts/adaptive/flexbox) layouts, enhanced non-touch input support, and [CameraX](https://developer.android.com/media/camera/camerax) for correct camera previews across any window size. Furthermore, new [skills](https://developer.android.com/tools/agents/android-skills) in Android Studio make updating your existing app to adopt these adaptive patterns easier than ever.
![image6.png](https://developer.android.com/static/blog/assets/image6_3baa56f951_kg4rb.webp) Notability's Android debut sets a new standard for premium productivity apps. Built with Jetpack Compose, Navigation 3, and Kotlin Multiplatform, it delivers an intuitive, adaptive experience across devices.

#### 9: Create seamless experiences for Googlebook

Last week we announced [Googlebook](https://developer.android.com/googlebook), a high-performance laptop that provides a large-screen canvas for your existing apps. Building with adaptive principles today helps ensure your app will work on Googlebook. Get started by reviewing relevant [design guidance](https://developer.android.com/design/ui/desktop) and [developer guidelines](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/desktop) for desktop experiences. Try out the new Desktop Emulator available in the Android Studio Canary to test your apps for this form factor today.
![image3.png](https://developer.android.com/static/blog/assets/image3_5673f52dea_ZYwFy9.webp) New Desktop Android Emulator

#### 10: Unified widget development experience with Jetpack Glance

Android 17 marks a shift toward a single, Compose-based development model for all widgets. By unifying the experience across mobile, cars, and Wear OS through Jetpack Glance, you can soon scale UI components across the ecosystem with a familiar workflow.

The breakthrough this year is the integration of RemoteCompose. On mobile and cars, it powers high-fidelity animations, while on Wear OS, it allows Wear Widgets (formerly Tiles) to render complex UI logic natively on remote surfaces. This ensures peak performance on low-power hardware while allowing a cohesive user journey, like checking a flight status on your car dashboard and seeing gate change updates on your wrist.
![blog_widgets.gif](https://developer.android.com/static/blog/assets/blog_widgets_8af5abf0ee_Z2gr8sq.webp) Four widgets are shown cycling through in the Android Auto interface. A clock, a contact card, Google Home favorites and a photo.

#### 11: Expand your reach on the road with Android for Cars

To help you expand your reach when you build in-car experiences, we're making it easier to build once and deliver your apps to Android Auto and Android Automotive OS. With the latest releases of the Car App Library, you can build customized, distraction-optimized [templated media apps](https://developer.android.com/training/cars/apps/media) for both platforms. We're introducing new [components](https://developer.android.com/design/ui/cars/guides/components/overview) and template capabilities to give you increased flexibility and more options for laying out content. Parked experiences are expanding too, with immersive video playback coming to Android Auto for phones running Android 17. You can easily adapt your video apps for these parked experiences; [apply now to the early access program](https://docs.google.com/forms/d/e/1FAIpQLSf0z4Nfw8wrloVhlgHDpLgdkg4WXsFj9ni5c1pw0qTvJ3Q4fQ/viewform) to publish in these beta categories and learn more about the latest updates in our [blog](http://android-developers.googleblog.com/2026/05/android-for-cars-unifying-platforms-premium-experiences.html).

#### 12: Accelerate your development with Android XR Developer Preview 4

Inspired by the innovative experiences you've built for the platform, we're continuing to mature our tools with[Developer Preview 4 of the Android XR SDK](https://goo.gle/XRSDK_IO26). A key milestone in this journey is the transition of our core libraries, XR Runtime, Jetpack SceneCore, and ARCore for Jetpack XR, moving to Beta soon to provide a more stable and performant foundation. We are also accelerating hardware access through the [Android XR Developer Catalyst Program](https://goo.gle/Catalyst_IO26), where you can apply for XREAL's Project Aura, audio glasses, or display glasses developer kits. Watch The Latest in Android XR session or [read our blog](https://goo.gle/XRSDK_IO26) to see how these updates help you build experiences across the ecosystem.
![Aura Geospatial Tour Demo - Draft 01.gif](https://developer.android.com/static/blog/assets/Aura_Geospatial_Tour_Demo_Draft_01_c057b0afa3_Z198OHG.webp) Early preview of the Geospatial API in ARCore for Jetpack XR, enabling high-precision anchoring of digital content to real-world locations.

#### 13: Android is your new home for professional-grade media experiences

Android 17 streamlines the entire media lifecycle with a production-ready toolkit. High-fidelity capture is now simplified with the CameraXViewfinder Composable, which handles complex scaling and responsiveness on foldables and tablets. For post-production, the new Media3 AI Effects library provides a single interface for premium features like Magic Eraser and Studio Sound, automatically optimizing for the device's hardware.

The pipeline is completed by CodecDB, offering chipset-specific encoding recommendations to eliminate export noise, and a new Scrubbing Mode in ExoPlayer for ultra-smooth seeking. Whether you're compositing multi-asset edits with Media3 Transformer or using the streamlined CastPlayer API, these updates ensure a professional-grade experience with significantly less development overhead.
![supercharge.gif](https://developer.android.com/static/blog/assets/supercharge_334a70764d_8QuyM.webp) Low Light Boost and Magic Eraser in action

#### 14: Increase app discovery and engagement on Google TV

Pointer remotes, which enable motion-controlled input, will be a future way for users to interact with Google TV as it unlocks faster user navigation. App developers can start [declaring support for pointing input](https://developer.android.com/training/tv/get-started/hardware#no-touchscreen) to ensure their apps are discoverable on future TVs with pointer remotes. Additionally, the Engage SDK, formerly known as the Video Discovery API, optimizes Resumption, Entitlements, and Recommendations across all Google TV form factors to boost app discovery and engagement. It's a great time to start onboarding the Engage SDK now, since the legacy Watch Next API, which has been powering your continue watching 1.0 experience, will lose support in the 2nd half of 2027. Get all the details in our [blog](http://android-developers.googleblog.com/2026/05/increase-google-tv-app-discovery.html).

#### 15: Performance: the foundation of a great app experience

To help developers navigate memory limits in Android 17, we've launched a suite of optimization tools. The [R8 Configuration Analyzer](https://developer.android.com/r8-analyzer) identifies keep rules that are bloating your binary, while[ProfilingManager](https://developer.android.com/topic/performance/tracing/profiling-manager/how-to-capture) and the integrated LeakCanary in Android Studio streamline memory leak detection. Furthermore, the new [Android Performance Analyzer](https://developer.android.com/android-performance-analyzer) offers advanced AI integration for complex trace analysis and automated SQL query generation to pinpoint performance bottlenecks.

## And the Latest on Driving Business Growth

#### 16: What's new in Google Play

Today's [updates from Google Play](https://goo.gle/play-io26) help expand your reach and scale your business with less complexity. We're redefining Play Store discovery with an immersive, short-form video format called Play Shorts, while expanding your audience beyond the store with app discovery in the Gemini app on Android and web. Plus, we're introducing powerful new capabilities like agentic catalog management for seamless bulk price and SKU updates, and using Gemini models to enable Play Console to pre-populate store listings from imported documents---making global localization effortless.
![IO26_BlogInLine_App-discovery-in-Gemini_1920x1080_1605.gif](https://developer.android.com/static/blog/assets/IO_26_Blog_In_Line_App_discovery_in_Gemini_1920x1080_1605_7e47f7b67b_1UoFlo.webp) Gemini will provide users with app suggestions during a search

#### 17: And of course, Android 17

Android 17 includes new performance \& system architecture improvements (in addition to app memory limits) like a lock-free MessageQueue and a GC with more frequent, less intensive young-generation collections to ensure system-wide stability and smoother UIs. The new [contact picker](https://developer.android.com/about/versions/17/features/contact-picker) and [eyedropper API](https://developer.android.com/reference/android/content/Intent#ACTION_OPEN_EYE_DROPPER) help minimize the use of sensitive permissions and unnecessary access to user data.  

Review [the behavior changes](https://developer.android.com/about/versions/17/behavior-changes-all) to make sure your app is ready for Android 17, including [background audio hardening](https://developer.android.com/about/versions/17/behavior-changes-all#bg-audio) and [SMS OTP protection](https://developer.android.com/about/versions/17/behavior-changes-all#sms-otp-all-apps). Get ready to [target Android 17](https://developer.android.com/about/versions/17/behavior-changes-17) (API 37) with changes such as mandatory large-screen resizability, certificate transparency by default, and restricted local network access. You can start testing today by enrolling your device [in the Beta](https://android-developers.googleblog.com/2026/04/the-fourth-beta-of-android-17.html) or using the latest 17.0 emulator images.

Oh, and one more thing. The third beta of our Android 17 [quarterly platform release (QPR1) is here](https://developer.android.com/about/versions/17/qpr1/release-notes), and it contains a minor SDK release to support several features that just couldn't wait for QPR2.

## Check out all of the Android \& Play Content at Google I/O

This was just a preview of some of the updates for Android developers at Google I/O. Tune into [What's New in Android](https://io.google/2026/explore/pa-keynote-5) for the latest news and announcements and [follow Google I/O](https://io.google/2026/) for much more over the following week!
- [#Google I/O](https://developer.android.com/blog/topics/google-i-o)

###### Written by:

-

  ## [Matthew McCullough](https://developer.android.com/blog/authors/matthew-mccullough)

  ###### Vice President, Product Management, Android Developer

  [read_more
  View profile](https://developer.android.com/blog/authors/matthew-mccullough) ![](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_Z1Fsr5h.webp) ![](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_Z1Fsr5h.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/paul_feng_759ac95845_spvRU.webp)](https://developer.android.com/blog/authors/paul-feng) 19 May 2026 19 May 2026 ![](https://developer.android.com/static/blog/assets/IO_26_Blog_Strapi_Icons_2000x1000px_0a8b06b49b_Z1e2APA.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [I/O 2026: What's new in Google Play](https://developer.android.com/blog/posts/i-o-2026-what-s-new-in-google-play)

  [arrow_forward](https://developer.android.com/blog/posts/i-o-2026-what-s-new-in-google-play) At this year's Google I/O, we talked about our evolving business model that offers more choice and new ways for your apps and content to be discovered on and off the store. We also unveiled advanced tools and insights that will help scale your business with less complexity.

  ###### [Paul Feng](https://developer.android.com/blog/authors/paul-feng) •
  6 min read

  - [#Google Play](https://developer.android.com/blog/topics/google-play)
  - [#Play Console](https://developer.android.com/blog/topics/play-console)
  - [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
  - [#Android Developers](https://developer.android.com/blog/topics/android-developers)
  - +2 ↩
- [![](https://developer.android.com/static/blog/assets/Luke_Hopkins_9c1e15d778_Z2o9b3q.webp)](https://developer.android.com/blog/authors/luke-hopkins) 19 May 2026 19 May 2026 ![](https://developer.android.com/static/blog/assets/Google_For_Developers_Android_Combo3_Strapi_2000x1000_56726aebea_Z1kvKHr.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android XR Updates for Unity, Unreal, and Godot](https://developer.android.com/blog/posts/android-xr-updates-for-unity-unreal-and-godot)

  [arrow_forward](https://developer.android.com/blog/posts/android-xr-updates-for-unity-unreal-and-godot) We are excited to announce that official support for Unreal Engine and Godot has arrived for Android XR. We are also launching new tools designed to boost your productivity and enable new XR capabilities: the Android XR Engine Hub and the Android XR Interaction Framework.

  ###### [Luke Hopkins](https://developer.android.com/blog/authors/luke-hopkins) •
  4 min read

  - [#Android XR](https://developer.android.com/blog/topics/android-xr)
  - [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
- [![](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z15U8cx.webp)](https://developer.android.com/blog/authors/fahd-imtiaz) 19 May 2026 19 May 2026 ![](https://developer.android.com/static/blog/assets/Google_For_Developers_Combo_IO_Strapi_2000x1000_0370ff6d2c_ZQaFMJ.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Adaptive development for the expanding Android ecosystem](https://developer.android.com/blog/posts/adaptive-development-for-the-expanding-android-ecosystem)

  [arrow_forward](https://developer.android.com/blog/posts/adaptive-development-for-the-expanding-android-ecosystem) With the release of Android 17, we are transitioning into an adaptive first development standard. Your users no longer rely on a single form factor; they transition between phones, foldables, tablets, laptops, automotive displays, and immersive XR environments throughout their day.

  ###### [Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz) •
  4 min read

  - [#Adaptive development](https://developer.android.com/blog/topics/adaptive-development)
  - [#Adaptive apps](https://developer.android.com/blog/topics/adaptive-apps)
  - [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
  - +1 ↩

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)