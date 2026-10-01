---
title: https://developer.android.com/blog/posts/land-your-apps-on-googlebook-with-adaptive-development
url: https://developer.android.com/blog/posts/land-your-apps-on-googlebook-with-adaptive-development
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news)

# Land your apps on Googlebook with adaptive development

4 min read ![](https://developer.android.com/static/blog/assets/Googlebook_Blog_Strapi_4a4a7d3291_Z1ReCnu.webp) 22 Sep 2026 [![View Fahd Imtiaz's profile](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z2vO4ST.webp)](https://developer.android.com/blog/authors/fahd-imtiaz)[![View Loryn Hairston's profile](https://developer.android.com/static/blog/assets/unnamed_13_777347786d_24gdiI.webp)](https://developer.android.com/blog/authors/loryn-hairston) [Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz) \& [Loryn Hairston](https://developer.android.com/blog/authors/loryn-hairston) [Googlebook](https://blog.google/products-and-platforms/devices/googlebook/pre-order-googlebook/) introduces a new category of laptops built on a shared Android foundation. High-performance hardware from partners such as HP, Dell, Lenovo, Acer, and Asus, combines mobile convenience with desktop power. Googlebook offers high-resolution OLED touchscreens, dedicated keyboards, and precision trackpads with all-day battery life and OS-level Gemini Intelligence. With Googlebook, users can transition fluidly from quick interactions on their phones to rich, immersive sessions on their laptop.

Bringing your app to Googlebook opens up valuable opportunities for you across the Android ecosystem. Google Play highlights optimized titles with dedicated badging, enhanced search, and featured spots across curated store homepages. Delivering this level of quality also prepares your app for the [Apps Experience Program](https://developer.android.com/distribute/aep), where you can enroll to unlock a new program rate card designed to drive business growth. Even better, when users set up their new Googlebook using their Android phone, optimized apps are prominently highlighted for easy transfer, giving your app day-one presence on their new device.
![desktop optimized.png](https://developer.android.com/static/blog/assets/desktop_optimized_1b523627bf_3aG7R.webp) Optimized for desktop badging and dedicated collections on Google Play.

The best part? You don't need to build a separate app from the ground up to take advantage of this reach. Adaptive development is how modern Android apps naturally scale across large displays, new device postures, and emerging form factors. If your app already embraces adaptive layouts, it is primed for Googlebooks. By building on your existing foundation of adaptive UI, window size classes, and multi-input support, you can deliver an optimized experience.
![image5.png](https://developer.android.com/static/blog/assets/image5_ef6c1516ee_1Ke9rn.webp) Adaptive layouts reorganizing mobile views into a multi-pane experience.

## Anchor your app in desktop fundamentals

On a laptop, your app operates within a desktop environment where user expectations shift toward higher information density, precision input, and active multitasking. Following desktop development and design guidance provides the principles needed to make the most of this experience. Instead of simply stretching mobile interfaces across a wide screen, an adaptive layout reorganizes content into functional groupings.

Adopt a multi-pane architecture to allow your UI to expand, reflow, or reveal richer detail as window boundaries change. With [Navigation 3](https://developer.android.com/guide/navigation/navigation-3), you can implement adaptive scene strategies to coordinate multi-pane layouts directly from your back stack. Use [ListDetailSceneStrategy](https://developer.android.com/guide/navigation/navigation-3/recipes/scenes-listdetail) and [SupportingPaneSceneStrategy](https://developer.android.com/guide/navigation/navigation-3/recipes/material-supportingpane) to enable side-by-side layouts when expanded window space is available. [Scene decorators](https://developer.android.com/guide/navigation/navigation-3/scenes/scene-decorators) let you wrap screens with persistent desktop navigation rails. Pair these patterns with layout primitives like [Grid](https://developer.android.com/develop/ui/compose/layouts/adaptive/grid) and [FlexBox](https://developer.android.com/develop/ui/compose/layouts/adaptive/flexbox), and soon alongside experimental [MediaQuery](https://developer.android.com/reference/kotlin/androidx/compose/ui/mediaQuery.composable) and [Styles APIs](https://developer.android.com/develop/ui/compose/styles), to organize complex content and adjust visual styles dynamically for desktop displays.
![image2.png](https://developer.android.com/static/blog/assets/image2_f4d96b41d6_Z2jqR5B.webp) Representations of width-based window size classes.

In free-form desktop windowing, app windows can be resized dynamically at any time. Your layout decisions should respond directly to the available window space using [window size classes](https://developer.android.com/develop/adaptive-apps/guides/get-started-with-adaptive-apps) rather than the physical display dimensions.

Desktop design also accounts for ergonomic viewing distances and precise pointer targets. Adjust your type scale for comfortable viewing across larger displays, set layout max widths to keep line lengths readable, and define explicit click targets to prevent misclicks. Explore complete design patterns in our [design principles guide](https://developer.android.com/design/ui/desktop/guides/foundations/design-principles) and discover real world inspiration in the [desktop design gallery](https://developer.android.com/design/ui/gallery?keywords=form_desktop).

## Deliver differentiated experiences for Googlebooks

Once your core layout is adaptive, you can enrich your app with differentiated features that take full advantage of a desktop environment. Everyday productivity in these setups relies on versatile input methods. Jetpack Compose natively supports physical keyboard navigation and pointer selection. Elevate your app's usability by integrating [contextual cursors](https://developer.android.com/guide/topics/large-screens/cursors) that provide visual feedback for text entry, pane resizing, and tool selection. Implement right click context menus and hover states; make your shortcuts discoverable through the [Keyboard Shortcuts Helper](https://developer.android.com/develop/ui/compose/touch-input/keyboard-input/keyboard-shortcuts-helper).
![image4.png](https://developer.android.com/static/blog/assets/image4_0077b8b280_Z1B6oan.webp) Task switcher displaying multiple open windows and app instances.

<br />

On Googlebook, apps run in free-form windows where users can tackle multiple tasks simultaneously. Unlock side-by-side workflows by enabling [multi-instance support](https://developer.android.com/develop/adaptive-apps/guides/support-multi-window-mode#multi-instance), giving users the ability to launch independent windows for comparing content or managing multiple documents. Pair this with [drag and drop](https://developer.android.com/develop/ui/compose/touch-input/user-interactions/drag-and-drop) to let users move text, images, and files fluidly between windows or even drop items onto an empty workspace to spin up a new task.
![image3.png](https://developer.android.com/static/blog/assets/image3_f7bffce877_ZsYLlU.webp) Multi-window multitasking with cross-window drag and drop.

Go all in and customize your window frame. In desktop windowing, apps include a caption [header bar that you can style](https://developer.android.com/develop/ui/compose/components/app-bars) with custom backgrounds, search bars, or tabs while respecting system window controls.

Beyond individual app windows, [Continue On](https://developer.android.com/develop/better-together/continue-on) keeps experiences connected across phones, tablets, and Googlebooks with bidirectional handoff that lets users start a task on one screen and pick up seamlessly on another. Passing state through [HandoffActivityData](https://developer.android.com/develop/better-together/continue-on/enable-support) preserves context such as document position or active tabs, with optional web fallbacks to ensure smooth transitions.

Complement this by surfacing actionable information at a glance with customizable [widgets](https://developer.android.com/design/ui/widget). And, as you refine your app experience, benchmark against our comprehensive [desktop app quality guidelines](https://developer.android.com/develop/adaptive-apps/quality-guidelines/adaptive-app-quality/experiences/desktop).

Developers are already bringing these patterns to life across the ecosystem. When bringing Notability to Googlebook, prior investments in tablets and foldables gave the team an immediate head start. Because their layout already relied on window size classes and adaptive scene strategies, their canvas and toolbars reflowed naturally during window resizing, while existing keyboard and trackpad support carried straight over.  

"We had already been targeting first-class experiences for tablets and foldables," explains Ryan Shea, Android Engineering Manager at Notability. "So by the time Googlebook came along, scaling Notability up to a laptop-class experience was mostly turning a dial we had already built. That left us free to spend our time on the things that only make sense on a bigger screen or with the newer APIs, like Continue On, which hands a note off from your phone to the laptop, and optimizing the side-by-side app experience for studying."

## Accelerate your workflow with dedicated tooling

Testing and optimizing your app for Googlebook fits naturally into your existing development workflow.

With the desktop emulator in Android Studio, you can run a virtual desktop environment directly on your workstation to test free-form window resizing, verify multi-instance interactions, and debug mouse, trackpad, and keyboard interactions. Download [Android Studio Canary](https://developer.android.com/studio/preview) to set up your virtual device today.

Help speed up your layout modernization with AI-assisted development. The [adaptive skill](https://github.com/android/skills/tree/main/jetpack-compose/adaptive) gives your AI agents the necessary context to help refactor mobile layouts into responsive Compose containers automatically. Install the skill directly through the [Android CLI](https://developer.android.com/tools/agents/android-cli) to streamline your implementation.

## Realize new possibilities on Googlebook

![Untitled design (2).png](https://developer.android.com/static/blog/assets/Untitled_design_2_6db2a68557_Z1dE2EO.webp) The Googlebook family of laptops from ecosystem partners.

The Googlebook lineup marks an exciting new chapter for the Android ecosystem, giving your apps a premium platform to deliver richer, more capable experiences. By building adaptively, a single codebase ensures your app looks and performs optimally across phones, foldables, tablets, and Googlebooks while unlocking elevated visibility and badging across Google Play. Explore documentation at our [Googlebook developer hub](https://developer.android.com/adaptive-apps), review the [desktop design guide](https://developer.android.com/design/ui/desktop), and start building for Googlebook today!
- [#Googlebook](https://developer.android.com/blog/topics/googlebook)
- [#Adaptive development](https://developer.android.com/blog/topics/adaptive-development)
- [#Jetpack Compose](https://developer.android.com/blog/topics/jetpack-compose)
Written by:

-

  ## [Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz)

  ###### Senior Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/fahd-imtiaz) ![View Fahd Imtiaz's profile](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z2vO4ST.webp) ![View Fahd Imtiaz's profile](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z2vO4ST.webp)
-

  ## [Loryn Hairston](https://developer.android.com/blog/authors/loryn-hairston)

  ###### Product Marketing Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/loryn-hairston) ![View Loryn Hairston's profile](https://developer.android.com/static/blog/assets/unnamed_13_777347786d_24gdiI.webp) ![View Loryn Hairston's profile](https://developer.android.com/static/blog/assets/unnamed_13_777347786d_24gdiI.webp)
Continue reading
- 3 Authors 11 Aug 2026 11 Aug 2026 ![](https://developer.android.com/static/blog/assets/Strapi_2ca09e764b_1JLHid.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Enhance your app for the new Pixel lineup: Unveiled at Made by Google](https://developer.android.com/blog/posts/enhance-your-app-for-the-new-pixel-lineup-unveiled-at-made-by-google)

  [arrow_forward](https://developer.android.com/blog/posts/enhance-your-app-for-the-new-pixel-lineup-unveiled-at-made-by-google) With the introduction of the Pixel 11 Pro Fold, Pixel Watch 5, and the entire Pixel family, users are moving seamlessly across diverse screen sizes, unique postures, and intelligent experiences.
  [Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz), [Loryn Hairston](https://developer.android.com/blog/authors/loryn-hairston), [Tracy Agyemang](https://developer.android.com/blog/authors/tracy-agyemang) • 4 min read
  - [#Wear OS 7](https://developer.android.com/blog/topics/wear-os-7)
  - [#made by google](https://developer.android.com/blog/topics/made-by-google)
  - [#Adaptive development](https://developer.android.com/blog/topics/adaptive-development)
  - [#Gemini Nano 4](https://developer.android.com/blog/topics/gemini-nano-4)
  - [#ML Kit Prompt API](https://developer.android.com/blog/topics/ml-kit-prompt-api)
  - [#Foldables](https://developer.android.com/blog/topics/foldables)
  - [#Jetpack Compose](https://developer.android.com/blog/topics/jetpack-compose)
  - +5 ↩
- [![View Fahd Imtiaz's profile](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z2vO4ST.webp)](https://developer.android.com/blog/authors/fahd-imtiaz) 19 May 2026 19 May 2026 ![](https://developer.android.com/static/blog/assets/Google_For_Developers_Combo_IO_Strapi_2000x1000_0370ff6d2c_Z14DWX.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Adaptive development for the expanding Android ecosystem](https://developer.android.com/blog/posts/adaptive-development-for-the-expanding-android-ecosystem)

  [arrow_forward](https://developer.android.com/blog/posts/adaptive-development-for-the-expanding-android-ecosystem) With the release of Android 17, we are transitioning into an adaptive first development standard. Your users no longer rely on a single form factor; they transition between phones, foldables, tablets, laptops, automotive displays, and immersive XR environments throughout their day.
  [Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz) • 3 min read
  - [#Adaptive development](https://developer.android.com/blog/topics/adaptive-development)
  - [#Adaptive apps](https://developer.android.com/blog/topics/adaptive-apps)
  - [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
  - +1 ↩
- [![View Nick Butcher's profile](https://developer.android.com/static/blog/assets/Nick_Butcher_5393f4552a_2d47S.webp)](https://developer.android.com/blog/authors/nick-butcher) 11 Aug 2026 11 Aug 2026 ![](https://developer.android.com/static/blog/assets/Social_Android_Jetpack_Compose_January_24_ba31d9063b_ZrjgNw.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [What's new in the Jetpack Compose August '26 release](https://developer.android.com/blog/posts/what-s-new-in-the-jetpack-compose-august-26-release)

  [arrow_forward](https://developer.android.com/blog/posts/what-s-new-in-the-jetpack-compose-august-26-release) Today, the Jetpack Compose August '26 release is stable!
  [Nick Butcher](https://developer.android.com/blog/authors/nick-butcher) • 5 min read
  - [#Jetpack Compose](https://developer.android.com/blog/topics/jetpack-compose)
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1zVtXW.webp)