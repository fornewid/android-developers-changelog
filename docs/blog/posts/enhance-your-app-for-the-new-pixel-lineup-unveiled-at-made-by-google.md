---
title: https://developer.android.com/blog/posts/enhance-your-app-for-the-new-pixel-lineup-unveiled-at-made-by-google
url: https://developer.android.com/blog/posts/enhance-your-app-for-the-new-pixel-lineup-unveiled-at-made-by-google
source: md.txt
---

> Documentation index: https://developer.android.com/blog/llms.txt

[Product News](https://developer.android.com/blog/categories/product-news.md.txt)

# Enhance your app for the new Pixel lineup: Unveiled at Made by Google

4 min read ![](https://developer.android.com/static/blog/assets/Strapi_2ca09e764b_1JLHid.webp) 11 Aug 2026 3 Authors [Fahd Imtiaz,](https://developer.android.com/blog/authors/fahd-imtiaz.md.txt) [Loryn Hairston,](https://developer.android.com/blog/authors/loryn-hairston.md.txt) [Tracy Agyemang](https://developer.android.com/blog/authors/tracy-agyemang.md.txt) [Made by Google](https://www.youtube.com/live/c84y9gAY90c?si=4T2AofHVbkWGbig1) expands what's possible across the Android ecosystem. With the introduction of the [Pixel 11 Pro Fold](https://blog.google/products-and-platforms/devices/pixel/google-pixel-11-pro-fold/), [Pixel Watch 5](https://blog.google/products-and-platforms/devices/pixel/pixel-watch-5/), and the entire Pixel family, users are moving seamlessly across diverse screen sizes, unique postures, and intelligent experiences. For you, the developer, this represents a massive opportunity: foldable users spend about 14x more than standard phone users. To help you elevate your existing experience without starting from scratch, we're sharing our latest platform guidance alongside real-world examples from developers already putting these features into production.

## **Deliver adaptive experiences across foldables and expanded displays**

![crop pixelfold.jpg](https://developer.android.com/static/blog/assets/crop_pixelfold_8cad10315a_1l8PsC.webp)

The Pixel 11 Pro Fold gives your app a chance to flex its capabilities with an expanded inner display and a standard size outer screen. Building for the foldable form factor requires dropping hardcoded layout rules and designing around available window space. Leveraging Jetpack Compose APIs like [Navigation 3](https://developer.android.com/guide/navigation/navigation-3.md.txt) with [Scene](https://developer.android.com/guide/navigation/navigation-3/scenes.md.txt) strategies or our newest layout APIs like [Grid](https://developer.android.com/develop/ui/compose/layouts/adaptive/grid.md.txt) and [FlexBox](https://developer.android.com/develop/ui/compose/layouts/adaptive/flexbox.md.txt) allows your layout containers to automatically wrap, span, and reflow. You can also use the experimental [MediaQuery](https://developer.android.com/develop/ui/compose/layouts/adaptive/mediaquery.md.txt) API to dynamically adapt your UI to environmental signals like foldable posture, and keyboard states.

Building adaptively requires tracking actual app dimensions rather than physical device size, especially during split-screen and multitasking flows. Using [Window Size Classes](https://developer.android.com/develop/adaptive-apps/guides/use-window-size-classes.md.txt) from the [WindowManager library](https://developer.android.com/blog/posts/jetpack-window-manager-1-5-is-stable.md.txt) allows your layout to respect folds and hinges as natural content separators.
![image.png](https://developer.android.com/static/blog/assets/image_accb606a2f_LUmqW.webp)

For instance, Notability leveraged Material 3 Window Size Classes to create a responsive two-pane layout that transitions smoothly between folded and expanded screens. As Ryan Shea, Android Engineering Manager at Notability, shared, tracking the window itself allows their layout and canvas zoom to ensure notes stay fit to the page through every fold, rotation, or split-screen resize, noting that they wanted the app "to feel native at every size, not just stretched to fit."
![image.png](https://developer.android.com/static/blog/assets/image_c4e847ad69_4x2Aj.webp) Notability's quiz UI adapted for expanded screens

Ensuring these transitions feel seamless also requires state preservation across configuration changes. Using [ViewModel](https://developer.android.com/topic/libraries/architecture/viewmodel.md.txt) retains UI state so interactions like scroll position, form inputs, and open dialogs remain uninterrupted when transitioning between inner and outer screens.

Taking this approach, Flo Health used Jetpack Compose state primitives, ViewModel, and Window Size Classes to make their highest-traffic user journeys resilient to rotation, fold/unfold and resizing transitions. As Aleksandr Kolodiazhnyi, Senior Android Engineer at Flo Health, shared, "Android's adaptive guidance turned what looked like a major refactor into a templated rollout," allowing them to adopt Compose primitives without a rewrite, "cutting \[their\] state-preservation code by roughly 30% while fixing lifecycle and analytics correctness issues that improved the app on every form factor."
![image.png](https://developer.android.com/static/blog/assets/image_528ab870cc_Z2fmUe5.webp)

To take full advantage of the foldable form factor, leverage [FoldingFeature updates](https://developer.android.com/develop/adaptive-apps/guides/foldables/make-your-app-fold-aware.md.txt) to trigger posture-specific layouts. When a user partially folds their device into tabletop posture, you can split your UI automatically by placing primary controls on the lower display and main content or viewfinders on the upper display.

Handling camera previews across foldable state changes, requires managing orientation shifts carefully. Migrating to the[CameraX library](https://developer.android.com/training/camerax) ensures automatic handling of sensor rotation and display scaling across screens, while existing [Camera2](https://developer.android.com/media/camera/camera2.md.txt) codebases can also achieve stability using the [CameraViewfinder](https://developer.android.com/media/camera/camera2/camera-preview.md.txt#cameraviewfinder) library. These [camera and display capabilities](https://developer.android.com/develop/adaptive-apps/guides/foldables/support-foldable-display-modes.md.txt) allow you to power dual-screen previewing and high-resolution rear camera selfies with minimal custom logic.

Prepare your app for these form factors today by exploring our complete adaptive development guidance at [Build adaptive apps](http://developer.android.com/adaptive-apps).

## **Bring delightful, gesture-driven experiences to the wrist**

![croppixelwatch.jpg](https://developer.android.com/static/blog/assets/croppixelwatch_f7f078730b_2qDNVg.webp)

The new Pixel Watch 5 is here, and we've optimized it to take advantage of the intelligent, power-efficient, touch-free convenience of [Wear OS 7.](https://developer.android.com/blog/posts/what-s-new-in-wear-os-7.md.txt) Thanks to system-wide performance optimizations and a collection of new features built to help users complete tasks efficiently, you can provide rich experiences that require only a single user action to complete.

The [one-handed gestures framework](http://android-developers.googleblog.com/2026/08/one-handed-gestures-wear-os.html) provides a convenient way for users to interact with their watches without needing to touch the screen with their opposite hand. Starting with the [1.7 beta release of Compose for Wear OS 7](https://developer.android.com/jetpack/androidx/releases/wear-compose.md.txt), you can seamlessly integrate one-handed gesture control into your Wear Compose apps with simple physical inputs on the watch-wearing arm, like a double-pinch or wrist turn.

Spotify is [adopting this framework](https://developer.android.com/design/ui/wear/guides/patterns/gestures.md.txt)to make controlling media more effortless. By mapping Wear OS gesture events directly to the media player state, users will be able to pause or resume playback using a simple double-pinch, keeping music controls accessible even when their hands are full.
![image6.gif](https://developer.android.com/static/blog/assets/image6_b680226851_Z10kyW3.webp) Pause Spotify media with a pinch gesture

Wear OS 7 also brings [Live Updates](https://developer.android.com/develop/ui/views/notifications/live-update.md.txt) directly to the wrist to surface real-time information like live sports scores, workout progress, and delivery status, which can also appear in the At-a-Glance surface on Pixel Watch 5. For example, Just Eat uses Live Updates to keep users informed on order arrival times at a glance. You can publish updates locally from your watch app or leverage phone notification bridging on supported devices to deliver real-time tracking across screens.
![image.png](https://developer.android.com/static/blog/assets/image_1bf8c92528_Z14SwTq.webp) Live Updates from Just Eat delivering real-time status and delivery ETAs at a glance

You can also extend glanceable interactions across watch surfaces on Wear OS 7 by using Wear Widgets, powered by [Jetpack Glance](https://developer.android.com/jetpack/androidx/releases/glance-wear.md.txt) and [RemoteCompose](https://developer.android.com/jetpack/androidx/releases/compose-remote.md.txt). Wear Widgets with Compose offer greater expressiveness and consistency than the old Tiles framework, and the two available widget layouts---small and large-- align perfectly with the 2x1 and 2x2 formats on mobile, ensuring your designs feel cohesive across devices.

On top of all these great new features, Wear OS 7 delivers up to a 10 percent improvement in battery life over Wear OS 6, making the Pixel Watch 5 a truly indispensable all-day companion for your users.

To get started developing for Wear OS 7, use the new [emulator](https://developer.android.com/training/wearables/versions/7/setup.md.txt), and check out all of our Wear OS resources and guidance at [Build apps for the wrist with Wear OS](https://developer.android.com/wear).

## **Unlock on-device intelligence with Gemini Nano 4**

![crop pixel11.jpg](https://developer.android.com/static/blog/assets/crop_pixel11_1a96b9a783_1zympo.webp)

Pixel 11 devices are built to run Gemini Nano 4, bringing fast, responsive, on-device intelligence to the hardware. By running AI workflows directly on device, you can offer low-latency, real-time interactions that feel instant and integrated without needing round trips to the cloud.

Through the[ML Kit GenAI Prompt API](https://developers.google.com/ml-kit/genai), you can send natural language requests directly to Gemini Nano on device. The model supports over 140 languages, better multimodal understanding, and [much more](https://developers.google.com/ml-kit/release-notes#july_14_2026). Build intelligent on-device features using advanced capabilities like [structured output](https://developers.google.com/ml-kit/genai/prompt/android/structured-output) and [thinking mode](https://developers.google.com/ml-kit/genai/prompt/android/thinking-mode).

Build smart capabilities into your app using our self-service tools and [Gemini models.](https://developer.android.com/ai/overview.md.txt)

## **Shape the next generation of experiences for the Pixel ecosystem today**

Made by Google showcases what's possible when hardware and software evolve together, and you are at the center of that innovation. You can begin optimizing your apps today by exploring our updated[adaptive guidance](https://developer.android.com/develop/adaptive-apps), creating [glanceable experiences](https://developer.android.com/wear) for Wear OS 7, and integrating on-device AI with[ML Kit](https://developers.google.com/ml-kit).

To help you implement these updates even faster, you can now leverage [Android skills](https://developer.android.com/tools/agents/android-skills.md.txt), which provide AI-optimized instructions for agents and tools. Whether you are using Gemini in Android Studio or running the [Android CLI](https://developer.android.com/tools/agents/android-cli.md.txt)through other agents, Android skills give your AI tools the context needed to execute complex workflows automatically. For instance, you can prompt your agent with the [CameraX skill](https://github.com/android/skills/tree/main/camera/camerax) to handle camera display scaling across foldables, or use the [Adaptive skill](https://github.com/android/skills/tree/main/jetpack-compose/adaptive) to set up dynamic Compose layouts without additional manual work.

Take advantage of these new surfaces, accelerate your workflow with agentic tools, and share your latest builds with the Android community! Head over to[developer.android.com](https://developer.android.com/) to access full documentation, explore the[Android skills GitHub repository](https://goo.gle/android-skills), and start building today.
- [#Wear OS 7](https://developer.android.com/blog/topics/wear-os-7.md.txt)
- [#made by google](https://developer.android.com/blog/topics/made-by-google.md.txt)
- [#Adaptive development](https://developer.android.com/blog/topics/adaptive-development.md.txt)
- [#Gemini Nano 4](https://developer.android.com/blog/topics/gemini-nano-4.md.txt)
- [#ML Kit Prompt API](https://developer.android.com/blog/topics/ml-kit-prompt-api.md.txt)
- [#Foldables](https://developer.android.com/blog/topics/foldables.md.txt)
- [#Jetpack Compose](https://developer.android.com/blog/topics/jetpack-compose.md.txt)
Written by:

-

  ## [Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz.md.txt)

  ###### Senior Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/fahd-imtiaz) ![View Fahd Imtiaz's profile](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z2vO4ST.webp) ![View Fahd Imtiaz's profile](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z2vO4ST.webp)
-

  ## [Loryn Hairston](https://developer.android.com/blog/authors/loryn-hairston.md.txt)

  ###### Product Marketing Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/loryn-hairston) ![View Loryn Hairston's profile](https://developer.android.com/static/blog/assets/unnamed_13_777347786d_24gdiI.webp) ![View Loryn Hairston's profile](https://developer.android.com/static/blog/assets/unnamed_13_777347786d_24gdiI.webp)
-

  ## [Tracy Agyemang](https://developer.android.com/blog/authors/tracy-agyemang.md.txt)

  ###### Product Marketing Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/tracy-agyemang) ![View Tracy Agyemang's profile](https://developer.android.com/static/blog/assets/Tracy_Agyemang_Headshot_9a0c523435_Z2epjbl.webp) ![View Tracy Agyemang's profile](https://developer.android.com/static/blog/assets/Tracy_Agyemang_Headshot_9a0c523435_Z2epjbl.webp)
Continue reading
- [![View Fahd Imtiaz's profile](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z2vO4ST.webp)](https://developer.android.com/blog/authors/fahd-imtiaz.md.txt)[![View Loryn Hairston's profile](https://developer.android.com/static/blog/assets/unnamed_13_777347786d_24gdiI.webp)](https://developer.android.com/blog/authors/loryn-hairston.md.txt) 22 Sep 2026 22 Sep 2026 ![](https://developer.android.com/static/blog/assets/Googlebook_Blog_Strapi_4a4a7d3291_Z1ReCnu.webp) [Product News](https://developer.android.com/blog/categories/product-news.md.txt)

  ## [Land your apps on Googlebook with adaptive development](https://developer.android.com/blog/posts/land-your-apps-on-googlebook-with-adaptive-development.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/land-your-apps-on-googlebook-with-adaptive-development.md.txt) Googlebook introduces a new category of laptops built on a shared Android foundation. High-performance hardware from partners such as HP, Dell, Lenovo, Acer, and Asus, combines mobile convenience with desktop power.
  [Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz.md.txt), [Loryn Hairston](https://developer.android.com/blog/authors/loryn-hairston.md.txt) • 4 min read
  - [#Googlebook](https://developer.android.com/blog/topics/googlebook.md.txt)
  - [#Adaptive development](https://developer.android.com/blog/topics/adaptive-development.md.txt)
  - [#Jetpack Compose](https://developer.android.com/blog/topics/jetpack-compose.md.txt)
  - +1 ↩
- [![View Fahd Imtiaz's profile](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z2vO4ST.webp)](https://developer.android.com/blog/authors/fahd-imtiaz.md.txt) 19 May 2026 19 May 2026 ![](https://developer.android.com/static/blog/assets/Google_For_Developers_Combo_IO_Strapi_2000x1000_0370ff6d2c_Z14DWX.webp) [Product News](https://developer.android.com/blog/categories/product-news.md.txt)

  ## [Adaptive development for the expanding Android ecosystem](https://developer.android.com/blog/posts/adaptive-development-for-the-expanding-android-ecosystem.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/adaptive-development-for-the-expanding-android-ecosystem.md.txt) With the release of Android 17, we are transitioning into an adaptive first development standard. Your users no longer rely on a single form factor; they transition between phones, foldables, tablets, laptops, automotive displays, and immersive XR environments throughout their day.
  [Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz.md.txt) • 3 min read
  - [#Adaptive development](https://developer.android.com/blog/topics/adaptive-development.md.txt)
  - [#Adaptive apps](https://developer.android.com/blog/topics/adaptive-apps.md.txt)
  - [#Google I/O](https://developer.android.com/blog/topics/google-i-o.md.txt)
  - +1 ↩
- [![View Aurash Mahbod's profile](https://developer.android.com/static/blog/assets/image3_98854eb3dd_Z2kItkm.webp)](https://developer.android.com/blog/authors/aurash-mahbod.md.txt) 18 Nov 2026 18 Nov 2026 ![](https://developer.android.com/static/blog/assets/ABL_162_2000x1000_1_ce7dba8d2a_72W03.webp) [Product News](https://developer.android.com/blog/categories/product-news.md.txt)

  ## [Elevating games: New large screens and foldables quality standards on Google Play](https://developer.android.com/blog/posts/elevating-game-quality-foldables-large-screens-google-play.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/elevating-game-quality-foldables-large-screens-google-play.md.txt) To give these experiences to players and ensure your games shine across every screen size, Google Play is introducing new large screen quality requirements for games
  [Aurash Mahbod](https://developer.android.com/blog/authors/aurash-mahbod.md.txt) • 4 min read
  - [#Google Play](https://developer.android.com/blog/topics/google-play.md.txt)
  - [#Android](https://developer.android.com/blog/topics/android.md.txt)
  - [#Adaptive Games](https://developer.android.com/blog/topics/adaptive-games.md.txt)
  - [#Foldables](https://developer.android.com/blog/topics/foldables.md.txt)
  - [#Large Screens](https://developer.android.com/blog/topics/large-screens.md.txt)
  - +3 ↩
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1zVtXW.webp)