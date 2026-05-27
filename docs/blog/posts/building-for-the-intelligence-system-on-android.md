---
title: https://developer.android.com/blog/posts/building-for-the-intelligence-system-on-android
url: https://developer.android.com/blog/posts/building-for-the-intelligence-system-on-android
source: md.txt
---

#### [Product News](https://developer.android.com/blog/categories/product-news)

# Building for the Intelligence System on Android

###### 4-min read

![](https://developer.android.com/static/blog/assets/Tas_Developers_cut_Strapi_3636223c9c_Z2pmmBN.webp) 12 May 2026 [![](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_Z1Fsr5h.webp)](https://developer.android.com/blog/authors/matthew-mccullough) [##### Matthew McCullough](https://developer.android.com/blog/authors/matthew-mccullough)

###### Vice President, Product Management, Android Developer

Announced today during [The Android Show](https://developer.android.com/events/show), Android is transitioning from an operating system to an intelligence system, creating more opportunities for engagement with your apps. Through deep integration between hardware and software, Android devices will be able to handle the heavy lifting of anticipating user needs, so your app can focus on delivering that experience at the right moment. As part of this, we are [announcing](https://blog.google/products-and-platforms/platforms/android/gemini-intelligence) Gemini Intelligence, a suite of new features that bring the best of Gemini to our most advanced Android devices.
[Video](https://www.youtube.com/watch?v=KvTRMSa1w4E)

**Task Automation with Gemini**

With Gemini Intelligence, we're expanding Gemini's ability to [automate tasks](http://d.android.com/ai/computer-control) across selected apps on behalf of the user with built-in transparency and control. This creates another avenue for user engagement, driving high-intent traffic to your app without requiring code or major engineering work from you. By allowing Gemini to navigate complex, multi-step tasks, such as ordering a latte from a cafe or building a shopping cart from a grocery list in a notes app, Gemini handles the logistics for users, so you're free to focus on innovation and building great features.

We know there are times when people like to browse, and others when they want to quickly handle a task. Initially launched with selected food and ridesharing partners to build a grocery order or request a ride, this capability is expanding across more verticals and form factors, including foldables, watches, cars, and XR glasses.
![TAS-Gif (1).gif](https://developer.android.com/static/blog/assets/TAS_Gif_1_df328d11d1_2r1NcV.webp)

**Increase Engagement with AppFunctions**

For more control over how agents interact with your app, you can use Android [AppFunctions](https://developer.android.com/ai/appfunctions). This empowers you to provide specific tools, such as services, data, and actions directly to the OS and agents, paired with natural language descriptions. The system can then discover and execute these tools across form factors, enabling users to trigger your app's functionality through the intelligence system for richer and more customized experiences with task automation. We've started testing these early stage APIs in a private preview with apps like [KakaoTalk](https://play.google.com/store/search?q=kakaotalk) to enable users to "send messages" or "initiate voice calls" through this new framework. AppFunctions have already enabled local execution of 25 apps' use cases across device manufacturers. You can experiment with the API locally and already register your interest to join the AppFunctions [Early Access Program](http://goo.gle/eap-af) for full integration opportunities.

We're providing multiple integration paths to meet you wherever you are on this intelligence journey, whether it's with an effortless, "no-code change" app automation or using the AppFunctions API, to provide you with more control in an MCP-like fashion.

**Enhanced User Experience with Widgets**

We're elevating the user experience by expanding widget support to new form factors, starting with [cars](http://developer.android.com/design/ui/cars/guides/flows/widgets). This creates new opportunities for you to engage with users on 250M Android Auto compatible vehicles.

[Jetpack Glance](https://developer.android.com/develop/ui/compose/glance) makes it easy to build high-quality widgets, and it is now getting powerful new capabilities thanks to a new underlying framework called [RemoteCompose](https://developer.android.com/jetpack/androidx/releases/compose-remote).

- **New richer, premium interactions:**Built to be deeply adaptive and battery efficient, RemoteCompose allows Glance to deliver richer, more premium interactions. You can soon leverage new capabilities, including snapscroll, expressive buttons, and particle effects to create more engaging widgets.
- **Built-in Backward Compatibility:** These expressive RemoteCompose features are supported out-of-the-box on Android 16 and above. By using Jetpack Glance as your API, you maintain complete backward compatibility. Your widgets will automatically leverage these premium UI features on newer devices while gracefully degrading to support older OS versions.

Furthermore, RemoteCompose is the engine behind Create My Widget, a feature where users can ask Gemini to build fully adaptive custom widgets that can be resized and optimized seamlessly for the user's home screen or Wear OS watch.

**Building Adaptively Beyond the Phone**

From foldables, tablets, compatible cars, and XR headsets to the new [Googlebooks](http://developer.android.com/googlebook), the canvas for Android apps has expanded across screens and form factors. Here are some of the updates to help you build adaptively:
![morph-to-tablet.gif](https://developer.android.com/static/blog/assets/morph_to_tablet_6f8146a89f_QKlEe.webp)

- **Jetpack Navigation 3:** Our latest [Jetpack Navigation 3](https://developer.android.com/guide/navigation/navigation-3) offers deeper adaptive support adding Scene decorators to the Scene API. Scene decorators can be used to modify the scene calculated by your app's scene strategy. For example, they can be used to add common UI elements such as top app bars and navigation bars/rails that you'd like to add at the scene, rather than nav entry level. NavDisplay now includes built-in functionality that makes [nav entries shared elements](https://goo.gle/4c6GYCc) so now you can smoothly transition between scenes. Check out our [Nav3-recipes](https://www.linkedin.com/safety/go/?url=https://goo.gle/47Nremk&urlhash=UkxR&mt=uOHz8Ihh6kWHjeLkaF4T2l_hcsc2xyLREGGFpnlMl9imj-qfu9P1k6qWM0liAVmypDYOVs9Bb04x1g3qvtJPLm2w03hUoWtZhP8JaF7Or26Y2HJKdHHNnYrECQ&isSdui=true) for more.
- **Jetpack Compose:** Adopting Compose into your app remains the easiest way to start building adaptive UIs, and we want to ensure that you have the right level of architectural support. We are working on a new set of building blocks in Compose 1.11 for responsive layouts and customization with [Grid](https://developer.android.com/develop/ui/compose/layouts/adaptive/grid), [Flexbox](https://developer.android.com/develop/ui/compose/layouts/adaptive/flexbox), [MediaQuery](https://developer.android.com/develop/ui/compose/layouts/adaptive/mediaquery) and [Style](https://developer.android.com/develop/ui/compose/styles). We would love your [feedback](https://b.corp.google.com/issues/new?component=612128&pli=1&template=1253476) on them before removing the Experimental flag.
- **Design guidance:** Explore our updated [design gallery](https://developer.android.com/design/ui/gallery) to be inspired, our new [desktop design hub](https://developer.android.com/design/ui/desktop) or our [adaptive layout guidance](https://developer.android.com/design/ui/mobile/guides/layout-and-content/adapt-layout) to get started.

For device-differentiated experiences, take advantage of the latest updates to:

- **Car App Library:** We're streamlining development by expanding the [Car App Library](https://developer.android.com/jetpack/androidx/releases/car-app#version_18_2), which allows you to "build once" and deliver customized, distraction-optimized [media](https://developer.android.com/training/cars/apps/media) experiences to both Android Auto and Android Automotive OS. We're further enabling richer in-car engagement by expanding support for adaptive [video apps](https://developer.android.com/training/cars/parked/video), so that videos can played full screen when cars are parked.
- **Android XR SDK:** The [Android XR SDK](https://developer.android.com/develop/xr) allows you to build deeply differentiated, custom experiences for a growing spectrum of XR devices, including upcoming [wired XR glasses](https://developer.android.com/develop/xr/devices#xr-glasses) (like XREAL's Project Aura), while existing adaptive apps automatically surface in immersive environments without additional developmental effort. You can get ready for display glasses by using [Jetpack Compose Glimmer](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer) to build glanceable UIs tailored for display glasses, alongside [Jetpack Projected APIs](https://developer.android.com/develop/xr/jetpack-xr-sdk#jetpack-projected) to bridge app experiences from the phone to the user's field of view. The developer preview 4 of the Android XR SDK, coming next week, introduces new interactive components like Title Chips and Button Groups that optimize input for glasses touchpads. It streamlines your workflow with the new ProjectedTestRule API to automate testing environments.

**A New Age for Your Users on Android**

From the shift to an [intelligence system](https://developer.android.com/ai) to the expansion of new form factors like Googlebooks, Android is creating new ways for people to get more out of their device experiences with developers and app makers at the center of it.

Gemini Intelligence features will roll out in waves as they become ready, starting with the latest Samsung Galaxy and Google Pixel phones this summer. They will also become available across your Android devices including your watch, car, glasses and laptops later this year.

Stay tuned for even more news about app development in this new era [at Google I/O](http://io.google/) next week.
- [#Android](https://developer.android.com/blog/topics/android)

###### Written by:

-

  ## [Matthew McCullough](https://developer.android.com/blog/authors/matthew-mccullough)

  ###### Vice President, Product Management, Android Developer

  [read_more
  View profile](https://developer.android.com/blog/authors/matthew-mccullough) ![](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_Z1Fsr5h.webp) ![](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_Z1Fsr5h.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_Z1Fsr5h.webp)](https://developer.android.com/blog/authors/matthew-mccullough) 20 May 2025 20 May 2025 ![](https://developer.android.com/static/blog/assets/IO_25_Blog_Hero_Template_Art_Long_01_126026f6a9_Z2cQC8F.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Updates to the Android XR SDK: Introducing Developer Preview 2](https://developer.android.com/blog/posts/updates-to-the-android-xr-sdk-introducing-developer-preview-2)

  [arrow_forward](https://developer.android.com/blog/posts/updates-to-the-android-xr-sdk-introducing-developer-preview-2) Since launching the Android XR SDK Developer Preview alongside Samsung, Qualcomm, and Unity last year, we've been blown away by all of the excitement we've been hearing from the broader Android community.

  ###### [Matthew McCullough](https://developer.android.com/blog/authors/matthew-mccullough) •
  4 min read

  - [#Android](https://developer.android.com/blog/topics/android)
- [![](https://developer.android.com/static/blog/assets/Jingyu_Shi_ab6f01bd32_ZXPVGC.webp)](https://developer.android.com/blog/authors/jingyu-shi) 26 May 2026 26 May 2026 ![](https://developer.android.com/static/blog/assets/Blog_hero_Strapi_2x_0147a8b012_1yD2LQ.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Top AI on Android updates for building intelligent experiences from Google I/O '26](https://developer.android.com/blog/posts/top-ai-on-android-updates-for-building-intelligent-experiences-from-google-i-o-26)

  [arrow_forward](https://developer.android.com/blog/posts/top-ai-on-android-updates-for-building-intelligent-experiences-from-google-i-o-26) At Google I/O 2026, we introduced Android's shift from an operating system to an intelligence system. We also demonstrated how you can build intelligent experiences natively with the system and bring the power of Google's AI into your apps.

  ###### [Jingyu Shi](https://developer.android.com/blog/authors/jingyu-shi) •
  2 min read

  - [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
  - [#Android](https://developer.android.com/blog/topics/android)
  - [#AppFunctions](https://developer.android.com/blog/topics/app-functions)
  - [#On-device](https://developer.android.com/blog/topics/on-device)
  - +2 ↩
- [![](https://developer.android.com/static/blog/assets/matthew_warner_67a99317e4_Z2c1VNu.webp)](https://developer.android.com/blog/authors/matthew-warner) 19 May 2026 19 May 2026 ![](https://developer.android.com/static/blog/assets/Google_For_Developers_Android_Combo_Strapi_2000x1000_5793c01e36_ZVoYvg.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android Studio I/O Edition: What's new in Android Developer tools](https://developer.android.com/blog/posts/android-studio-i-o-edition-what-s-new-in-android-developer-tools)

  [arrow_forward](https://developer.android.com/blog/posts/android-studio-i-o-edition-what-s-new-in-android-developer-tools) This year at Google I/O we are going beyond iterative changes, towards a fundamental shift in how apps are built. Our newest tools are built for the agentic era with features that boost productivity for you as an Android developer AND supercharge the AI agents you deploy in your codebase.

  ###### [Matthew Warner](https://developer.android.com/blog/authors/matthew-warner) •
  8 min read

  - [#Agent Skills](https://developer.android.com/blog/topics/agent-skills)
  - [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
  - [#Android](https://developer.android.com/blog/topics/android)
  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)
  - +2 ↩

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)