---
title: https://developer.android.com/blog/posts/the-intelligent-os-making-ai-agents-more-helpful-for-android-apps
url: https://developer.android.com/blog/posts/the-intelligent-os-making-ai-agents-more-helpful-for-android-apps
source: md.txt
---

#### [Product News](https://developer.android.com/blog/categories/product-news)

# The Intelligent OS: Making AI agents more helpful for Android apps

###### 3-min read

![](https://developer.android.com/static/blog/assets/intelligent_OS_215691a288_G81Rr.webp) 25 Feb 2026 [![](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_Z1Fsr5h.webp)](https://developer.android.com/blog/authors/matthew-mccullough) [##### Matthew McCullough](https://developer.android.com/blog/authors/matthew-mccullough)

###### Vice President, Product Management, Android Developer

User expectations for AI on their devices are fundamentally shifting how they interact with their apps. Instead of opening apps to do tasks step-by-step, they're asking AI to do the heavy lifting for them. In this new interaction model, success is shifting from getting users to open your app, to successfully fulfilling their tasks and helping them get more done faster.

To help you evolve your apps for this agentic future, we're introducing early stage developer capabilities that bridge the gap between your apps and agentic apps and personalized assistants, such as Google Gemini. While we are in the early, beta stages of this journey, we're designing these features with privacy and security at their core as our first step in exploring this paradigm shift as an app ecosystem.

### **Empowering apps with AppFunctions**

Android [AppFunctions](https://developer.android.com/ai/appfunctions) allows apps to expose data and functionality directly to AI agents and assistants. With the[](https://developer.android.com/jetpack/androidx/releases/appfunctions)AppFunctions [Jetpack library](https://developer.android.com/jetpack/androidx/releases/appfunctions) and [platform APIs](https://developer.android.com/reference/android/app/appfunctions/package-summary), developers can create self-describing functions that agentic apps can discover and execute via natural language. Mirroring how backend capabilities are declared via MCP cloud servers, AppFunctions provides an on-device solution for Android apps. Much like [WebMCP](https://developer.chrome.com/blog/webmcp-epp), it executes these functions locally on the device rather than on a server.

The **Samsung Gallery integration with Gemini on the Galaxy S26 series** showcases AppFunctions in action. Instead of manually scrolling through photo albums, you can now simply ask Gemini to "Show me pictures of my cat from Samsung Gallery." Gemini takes the user query, intelligently identifies and triggers the right function, and presents the returned photos from Samsung Gallery directly in the Gemini app, so users never need to leave. This experience is multimodal and can be done via voice or text. Users can even use the returned photos in follow-up conversations, like sending them to friends in a text message.
![photos.gif](https://developer.android.com/static/blog/assets/photos_fea372e64a_Z1CIdkc.webp)

This integration is currently available on the Galaxy S26 series and will soon expand to Samsung devices running OneUI 8.5 and higher. Through AppFunctions, Gemini can already automate tasks across app categories like [Calendar](https://support.google.com/gemini/answer/15305236?ref_topic=16695931&sjid=2355454043249888712-NC&co=GENIE.Platform%3DAndroid&oco=1), [Notes](https://support.google.com/gemini/answer/15230597?ref_topic=16695931&sjid=2355454043249888712-NC&co=GENIE.Platform%3DAndroid&oco=1), and [Tasks](https://support.google.com/gemini/answer/15230285?ref_topic=16695931&sjid=2355454043249888712-NC&co=GENIE.Platform%3DAndroid&oco=1), on devices from multiple manufacturers. Whether it's coordinating calendar events, organizing notes, or setting to-do reminders, users can streamline daily activities in one place.

### **Enabling agentic apps with intelligent UI automation**

While AppFunctions provides a structured framework and more control for apps to communicate with AI agents and assistants, we know that not every interaction has a dedicated integration yet. We're also developing a UI automation framework for AI agents and assistants to intelligently execute generic tasks on users' installed apps, with user transparency and control built in. This is the platform doing the heavy lifting, so developers can get agentic reach with zero code. It's a low-effort way to extend their reach without a major engineering lift right now.   

To get feedback as we refine this framework, we're starting with an early preview on the Galaxy S26 series and select Pixel 10 devices, where users will be able to delegate multi-step tasks to Gemini with just a long press of the power button. Launching as a beta feature in the Gemini app, this will support a curated selection of apps in the food delivery, grocery, and rideshare categories in the US and Korea to start. Whether users need to place a complex pizza order for their family members with particular tastes, coordinate a multi-stop rideshare with co-workers, or reorder their last grocery purchase, Gemini can help complete tasks using the context already available from your apps, without any developer work needed.
![photos2.gif](https://developer.android.com/static/blog/assets/photos2_835c905721_Z1Q9cOu.webp)

Users are in control while a task is being actioned in the background through UI automation. For any automation action, users have the option to monitor a task's progress via notifications or "live view" and can switch to manual control at any point to take over the experience. Gemini is also designed to alert users before completing sensitive tasks, such as making a purchase.

### **Looking ahead**

In Android 17, we're looking to broaden these capabilities to reach even more users, developers, and device manufacturers.

We are currently building experiences with a small set of app developers, focusing on high-quality user experiences as the ecosystem evolves. We plan to share more details later this year on how you can use AppFunctions and UI automation to enable agentic integrations for your app. Stay tuned for updates.

###### Written by:

-

  ## [Matthew McCullough](https://developer.android.com/blog/authors/matthew-mccullough)

  ###### Vice President, Product Management, Android Developer

  [read_more
  View profile](https://developer.android.com/blog/authors/matthew-mccullough) ![](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_Z1Fsr5h.webp) ![](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_Z1Fsr5h.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_Z1Fsr5h.webp)](https://developer.android.com/blog/authors/matthew-mccullough) 02 Apr 2026 02 Apr 2026 ![](https://developer.android.com/static/blog/assets/Gemma_Android_2x1_2x_a6d27254c4_Z10SxJJ.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Gemma 4: The new standard for local agentic intelligence on Android](https://developer.android.com/blog/posts/gemma-4-the-new-standard-for-local-agentic-intelligence-on-android)

  [arrow_forward](https://developer.android.com/blog/posts/gemma-4-the-new-standard-for-local-agentic-intelligence-on-android) Today, we are enhancing Android development with Gemma 4, our latest state-of-the-art open model designed with complex reasoning and autonomous tool-calling capabilities.

  ###### [Matthew McCullough](https://developer.android.com/blog/authors/matthew-mccullough) •
  2 min read

  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)
- [![](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_Z1Fsr5h.webp)](https://developer.android.com/blog/authors/matthew-mccullough) 26 Mar 2026 26 Mar 2026 ![](https://developer.android.com/static/blog/assets/android17banner_359909419a_Z1HMAIH.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [The Third Beta of Android 17](https://developer.android.com/blog/posts/the-third-beta-of-android-17)

  [arrow_forward](https://developer.android.com/blog/posts/the-third-beta-of-android-17) Android 17 has officially reached platform stability today with Beta 3. That means that the API surface is locked; you can perform final compatibility testing and push your Android 17-targeted apps to the Play Store.

  ###### [Matthew McCullough](https://developer.android.com/blog/authors/matthew-mccullough) •
  5 min read

  - [#Android 17](https://developer.android.com/blog/topics/android-17)
  - [#beta](https://developer.android.com/blog/topics/beta)
- [![](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_Z1Fsr5h.webp)](https://developer.android.com/blog/authors/matthew-mccullough) 05 Mar 2026 05 Mar 2026 ![](https://developer.android.com/static/blog/assets/android_Bench_f2e4dd4fda_2816Hg.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Elevating AI-assisted Android development and improving LLMs with Android Bench](https://developer.android.com/blog/posts/elevating-ai-assisted-android-development-and-improving-ll-ms-with-android-bench)

  [arrow_forward](https://developer.android.com/blog/posts/elevating-ai-assisted-android-development-and-improving-ll-ms-with-android-bench) We want to make it faster and easier for you to build high-quality Android apps, and one way we're helping you be more productive is by putting AI at your fingertips.

  ###### [Matthew McCullough](https://developer.android.com/blog/authors/matthew-mccullough) •
  2 min read

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)