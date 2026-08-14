---
title: https://developer.android.com/blog/posts/enhance-your-app-for-the-new-pixel-lineup-unveiled-at-made-by-google
url: https://developer.android.com/blog/posts/enhance-your-app-for-the-new-pixel-lineup-unveiled-at-made-by-google
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news)

# Enhance your app for the new Pixel lineup: Unveiled at Made by Google

4 min read ![](https://developer.android.com/static/blog/assets/Strapi_2ca09e764b_Z1hF7qE.webp) 11 Aug 2026 3 Authors [Fahd Imtiaz,](https://developer.android.com/blog/authors/fahd-imtiaz) [Loryn Hairston,](https://developer.android.com/blog/authors/loryn-hairston) [Tracy Agyemang](https://developer.android.com/blog/authors/tracy-agyemang) [Made by Google](https://www.youtube.com/live/c84y9gAY90c?si=4T2AofHVbkWGbig1) expands what's possible across the Android ecosystem. With the introduction of the [Pixel 11 Pro Fold](https://blog.google/products-and-platforms/devices/pixel/google-pixel-11-pro-fold/), [Pixel Watch 5](https://blog.google/products-and-platforms/devices/pixel/pixel-watch-5/), and the entire Pixel family, users are moving seamlessly across diverse screen sizes, unique postures, and intelligent experiences. For you, the developer, this represents a massive opportunity: foldable users spend about 14x more than standard phone users. To help you elevate your existing experience without starting from scratch, we're sharing our latest platform guidance alongside real-world examples from developers already putting these features into production.

## **Deliver adaptive experiences across foldables and expanded displays**

![crop pixelfold.jpg](https://developer.android.com/static/blog/assets/crop_pixelfold_8cad10315a_ZPnIiW.webp)

The Pixel 11 Pro Fold gives your app a chance to flex its capabilities with an expanded inner display and a standard size outer screen. Building for the foldable form factor requires dropping hardcoded layout rules and designing around available window space. Leveraging Jetpack Compose APIs like [Navigation 3](https://developer.android.com/guide/navigation/navigation-3) with [Scene](https://developer.android.com/guide/navigation/navigation-3/scenes) strategies or our newest layout APIs like [Grid](https://developer.android.com/develop/ui/compose/layouts/adaptive/grid) and [FlexBox](https://developer.android.com/develop/ui/compose/layouts/adaptive/flexbox) allows your layout containers to automatically wrap, span, and reflow. You can also use the experimental [MediaQuery](https://developer.android.com/develop/ui/compose/layouts/adaptive/mediaquery) API to dynamically adapt your UI to environmental signals like foldable posture, and keyboard states.

Building adaptively requires tracking actual app dimensions rather than physical device size, especially during split-screen and multitasking flows. Using [Window Size Classes](https://developer.android.com/develop/adaptive-apps/guides/use-window-size-classes) from the [WindowManager library](https://developer.android.com/blog/posts/jetpack-window-manager-1-5-is-stable) allows your layout to respect folds and hinges as natural content separators.
![image.png](https://developer.android.com/static/blog/assets/image_accb606a2f_Z1JKChD.webp)

For instance, Notability leveraged Material 3 Window Size Classes to create a responsive two-pane layout that transitions smoothly between folded and expanded screens. As Ryan Shea, Android Engineering Manager at Notability, shared, tracking the window itself allows their layout and canvas zoom to ensure notes stay fit to the page through every fold, rotation, or split-screen resize, noting that they wanted the app "to feel native at every size, not just stretched to fit."
![image.png](https://developer.android.com/static/blog/assets/image_c4e847ad69_Z2s8W8h.webp) Notability's quiz UI adapted for expanded screens

Ensuring these transitions feel seamless also requires state preservation across configuration changes. Using [ViewModel](https://developer.android.com/topic/libraries/architecture/viewmodel) retains UI state so interactions like scroll position, form inputs, and open dialogs remain uninterrupted when transitioning between inner and outer screens.

Taking this approach, Flo Health used Jetpack Compose state primitives, ViewModel, and Window Size Classes to make their highest-traffic user journeys resilient to rotation, fold/unfold and resizing transitions. As Aleksandr Kolodiazhnyi, Senior Android Engineer at Flo Health, shared, "Android's adaptive guidance turned what looked like a major refactor into a templated rollout," allowing them to adopt Compose primitives without a rewrite, "cutting \[their\] state-preservation code by roughly 30% while fixing lifecycle and analytics correctness issues that improved the app on every form factor."
![image.png](https://developer.android.com/static/blog/assets/image_528ab870cc_i8dQg.webp)

To take full advantage of the foldable form factor, leverage [FoldingFeature updates](https://developer.android.com/develop/adaptive-apps/guides/foldables/make-your-app-fold-aware) to trigger posture-specific layouts. When a user partially folds their device into tabletop posture, you can split your UI automatically by placing primary controls on the lower display and main content or viewfinders on the upper display.

Handling camera previews across foldable state changes, requires managing orientation shifts carefully. Migrating to the[CameraX library](https://developer.android.com/training/camerax) ensures automatic handling of sensor rotation and display scaling across screens, while existing [Camera2](https://developer.android.com/media/camera/camera2) codebases can also achieve stability using the [CameraViewfinder](https://developer.android.com/media/camera/camera2/camera-preview#cameraviewfinder) library. These [camera and display capabilities](https://developer.android.com/develop/adaptive-apps/guides/foldables/support-foldable-display-modes) allow you to power dual-screen previewing and high-resolution rear camera selfies with minimal custom logic.

Prepare your app for these form factors today by exploring our complete adaptive development guidance at [Build adaptive apps](http://developer.android.com/adaptive-apps).

## **Bring delightful, gesture-driven experiences to the wrist**

![croppixelwatch.jpg](https://developer.android.com/static/blog/assets/croppixelwatch_f7f078730b_f7f9G.webp)

The new Pixel Watch 5 is here, and we've optimized it to take advantage of the intelligent, power-efficient, touch-free convenience of [Wear OS 7.](https://developer.android.com/blog/posts/what-s-new-in-wear-os-7) Thanks to system-wide performance optimizations and a collection of new features built to help users complete tasks efficiently, you can provide rich experiences that require only a single user action to complete.

The [one-handed gestures framework](http://android-developers.googleblog.com/2026/08/one-handed-gestures-wear-os.html) provides a convenient way for users to interact with their watches without needing to touch the screen with their opposite hand. Starting with the [1.7 beta release of Compose for Wear OS 7](https://developer.android.com/jetpack/androidx/releases/wear-compose), you can seamlessly integrate one-handed gesture control into your Wear Compose apps with simple physical inputs on the watch-wearing arm, like a double-pinch or wrist turn.

Spotify is [adopting this framework](https://developer.android.com/design/ui/wear/guides/patterns/gestures)to make controlling media more effortless. By mapping Wear OS gesture events directly to the media player state, users will be able to pause or resume playback using a simple double-pinch, keeping music controls accessible even when their hands are full.
![image6.gif](https://developer.android.com/static/blog/assets/image6_b680226851_Z29z5jB.webp) Pause Spotify media with a pinch gesture

Wear OS 7 also brings [Live Updates](https://developer.android.com/develop/ui/views/notifications/live-update) directly to the wrist to surface real-time information like live sports scores, workout progress, and delivery status, which can also appear in the At-a-Glance surface on Pixel Watch 5. For example, Just Eat uses Live Updates to keep users informed on order arrival times at a glance. You can publish updates locally from your watch app or leverage phone notification bridging on supported devices to deliver real-time tracking across screens.
![image.png](https://developer.android.com/static/blog/assets/image_1bf8c92528_1sBBaU.webp) Live Updates from Just Eat delivering real-time status and delivery ETAs at a glance

You can also extend glanceable interactions across watch surfaces on Wear OS 7 by using Wear Widgets, powered by [Jetpack Glance](https://developer.android.com/jetpack/androidx/releases/glance-wear) and [RemoteCompose](https://developer.android.com/jetpack/androidx/releases/compose-remote). Wear Widgets with Compose offer greater expressiveness and consistency than the old Tiles framework, and the two available widget layouts---small and large-- align perfectly with the 2x1 and 2x2 formats on mobile, ensuring your designs feel cohesive across devices.

On top of all these great new features, Wear OS 7 delivers up to a 10 percent improvement in battery life over Wear OS 6, making the Pixel Watch 5 a truly indispensable all-day companion for your users.

To get started developing for Wear OS 7, use the new [emulator](https://developer.android.com/training/wearables/versions/7/setup), and check out all of our Wear OS resources and guidance at [Build apps for the wrist with Wear OS](https://developer.android.com/wear).

## **Unlock on-device intelligence with Gemini Nano 4**

![crop pixel11.jpg](https://developer.android.com/static/blog/assets/crop_pixel11_1a96b9a783_zdrmX.webp)

Pixel 11 devices are built to run Gemini Nano 4, bringing fast, responsive, on-device intelligence to the hardware. By running AI workflows directly on device, you can offer low-latency, real-time interactions that feel instant and integrated without needing round trips to the cloud.

Through the[ML Kit GenAI Prompt API](https://developers.google.com/ml-kit/genai), you can send natural language requests directly to Gemini Nano on device. The model supports over 140 languages, better multimodal understanding, and [much more](https://developers.google.com/ml-kit/release-notes#july_14_2026). Build intelligent on-device features using advanced capabilities like [structured output](https://developers.google.com/ml-kit/genai/prompt/android/structured-output) and [thinking mode](https://developers.google.com/ml-kit/genai/prompt/android/thinking-mode).

Build smart capabilities into your app using our self-service tools and [Gemini models.](https://developer.android.com/ai/overview)

## **Shape the next generation of experiences for the Pixel ecosystem today**

Made by Google showcases what's possible when hardware and software evolve together, and you are at the center of that innovation. You can begin optimizing your apps today by exploring our updated[adaptive guidance](https://developer.android.com/develop/adaptive-apps), creating [glanceable experiences](https://developer.android.com/wear) for Wear OS 7, and integrating on-device AI with[ML Kit](https://developers.google.com/ml-kit).

To help you implement these updates even faster, you can now leverage [Android skills](https://developer.android.com/tools/agents/android-skills), which provide AI-optimized instructions for agents and tools. Whether you are using Gemini in Android Studio or running the [Android CLI](https://developer.android.com/tools/agents/android-cli)through other agents, Android skills give your AI tools the context needed to execute complex workflows automatically. For instance, you can prompt your agent with the [CameraX skill](https://github.com/android/skills/tree/main/camera/camerax) to handle camera display scaling across foldables, or use the [Adaptive skill](https://github.com/android/skills/tree/main/jetpack-compose/adaptive) to set up dynamic Compose layouts without additional manual work.

Take advantage of these new surfaces, accelerate your workflow with agentic tools, and share your latest builds with the Android community! Head over to[developer.android.com](https://developer.android.com/) to access full documentation, explore the[Android skills GitHub repository](https://goo.gle/android-skills), and start building today.
- [#Wear OS 7](https://developer.android.com/blog/topics/wear-os-7)
- [#made by google](https://developer.android.com/blog/topics/made-by-google)
- [#Adaptive development](https://developer.android.com/blog/topics/adaptive-development)
- [#Gemini Nano 4](https://developer.android.com/blog/topics/gemini-nano-4)
- [#ML Kit Prompt API](https://developer.android.com/blog/topics/ml-kit-prompt-api)
- [#Foldables](https://developer.android.com/blog/topics/foldables)
- [#Jetpack Compose](https://developer.android.com/blog/topics/jetpack-compose)
Written by:

-

  ## [Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz)

  ###### Senior Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/fahd-imtiaz) ![View Fahd Imtiaz's profile](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z15U8cx.webp) ![View Fahd Imtiaz's profile](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z15U8cx.webp)
-

  ## [Loryn Hairston](https://developer.android.com/blog/authors/loryn-hairston)

  ###### Product Marketing Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/loryn-hairston) ![View Loryn Hairston's profile](https://developer.android.com/static/blog/assets/unnamed_13_777347786d_Z1Y5zeh.webp) ![View Loryn Hairston's profile](https://developer.android.com/static/blog/assets/unnamed_13_777347786d_Z1Y5zeh.webp)
-

  ## [Tracy Agyemang](https://developer.android.com/blog/authors/tracy-agyemang)

  ###### Product Marketing Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/tracy-agyemang) ![View Tracy Agyemang's profile](https://developer.android.com/static/blog/assets/Tracy_Agyemang_Headshot_9a0c523435_1hBimO.webp) ![View Tracy Agyemang's profile](https://developer.android.com/static/blog/assets/Tracy_Agyemang_Headshot_9a0c523435_1hBimO.webp)
Continue reading
- [![View Fahd Imtiaz's profile](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z15U8cx.webp)](https://developer.android.com/blog/authors/fahd-imtiaz) 19 May 2026 19 May 2026 ![](https://developer.android.com/static/blog/assets/Google_For_Developers_Combo_IO_Strapi_2000x1000_0370ff6d2c_ZQaFMJ.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Adaptive development for the expanding Android ecosystem](https://developer.android.com/blog/posts/adaptive-development-for-the-expanding-android-ecosystem)

  [arrow_forward](https://developer.android.com/blog/posts/adaptive-development-for-the-expanding-android-ecosystem) With the release of Android 17, we are transitioning into an adaptive first development standard. Your users no longer rely on a single form factor; they transition between phones, foldables, tablets, laptops, automotive displays, and immersive XR environments throughout their day.
  [Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz) • 3 min read
  - [#Adaptive development](https://developer.android.com/blog/topics/adaptive-development)
  - [#Adaptive apps](https://developer.android.com/blog/topics/adaptive-apps)
  - [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
  - +1 ↩
- [![View Nick Butcher's profile](https://developer.android.com/static/blog/assets/Nick_Butcher_5393f4552a_19h6h7.webp)](https://developer.android.com/blog/authors/nick-butcher) 11 Aug 2026 11 Aug 2026 ![](https://developer.android.com/static/blog/assets/Social_Android_Jetpack_Compose_January_24_ba31d9063b_1w4qDC.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [What's new in the Jetpack Compose August '26 release](https://developer.android.com/blog/posts/what-s-new-in-the-jetpack-compose-august-26-release)

  [arrow_forward](https://developer.android.com/blog/posts/what-s-new-in-the-jetpack-compose-august-26-release) Today, the Jetpack Compose August '26 release is stable!
  [Nick Butcher](https://developer.android.com/blog/authors/nick-butcher) • 5 min read
  - [#Jetpack Compose](https://developer.android.com/blog/topics/jetpack-compose)
- [![View Chiara Chiappini's profile](https://developer.android.com/static/blog/assets/unnamed_14_383c39c2c2_Derb5.webp)](https://developer.android.com/blog/authors/chiara-chiappini) 11 Aug 2026 11 Aug 2026 ![](https://developer.android.com/static/blog/assets/Bring_one_handed_gestures_Strapi_defff06599_Z1FDx9g.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Bring one-handed gestures to your Wear OS app](https://developer.android.com/blog/posts/bring-one-handed-gestures-to-your-wear-os-app)

  [arrow_forward](https://developer.android.com/blog/posts/bring-one-handed-gestures-to-your-wear-os-app) First introduced on Pixel Watch with Wear OS 6.1, one-handed gestures made quick interactions effortless, such as starting and stopping a timer, accepting calls, and controlling media.
  [Chiara Chiappini](https://developer.android.com/blog/authors/chiara-chiappini) • 3 min read
  - [#Wear OS](https://developer.android.com/blog/topics/wear-os)
  - [#made by google](https://developer.android.com/blog/topics/made-by-google)
  - [#pixel watch](https://developer.android.com/blog/topics/pixel-watch)
  - +1 ↩
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)