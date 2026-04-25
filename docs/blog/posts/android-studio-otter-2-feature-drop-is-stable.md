---
title: https://developer.android.com/blog/posts/android-studio-otter-2-feature-drop-is-stable
url: https://developer.android.com/blog/posts/android-studio-otter-2-feature-drop-is-stable
source: md.txt
---

#### [Product News](https://developer.android.com/blog/categories/product-news)

# Android Studio Otter 2 Feature Drop is stable!

###### 3-min read

![](https://developer.android.com/static/blog/assets/as_Otter2_96831eedef_Z19EUHu.webp) 04 Dec 2025 [![](https://developer.android.com/static/blog/assets/Sandhya_Mohan_30435468a9_1b689e.webp)](https://developer.android.com/blog/authors/sandhya-mohan)[![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)](https://developer.android.com/blog/authors/trevor-johns)

##### [Sandhya Mohan](https://developer.android.com/blog/authors/sandhya-mohan)
\&
[Trevor Johns](https://developer.android.com/blog/authors/trevor-johns)

The [**Android Studio Otter 2 Feature Drop**](http://d.android.com/studio) is here to supercharge your productivity.

This final stable release for '25 powers up Agent Mode, equipping it with the new Android Knowledge Base for improved accuracy, and giving you the option to try out the new Gemini 3 model. You'll also be able to take advantage of new settings such as the ability to keep your personalized IDE environment consistent across all of your machines. We've also incorporated all of the latest stability and performance improvements from the IntelliJ IDEA 2025.2 platform, including Kotlin compiler and terminal improvements, making this a significant enhancement for your development workflow.

#### **Updates to Agent Mode**

**Access to Gemini 3**

We recently introduced the ability to use our latest model, Gemini 3 Pro Preview, within Android Studio. This is our best model for coding and agentic capabilities. It'll give you superior performance in Agent Mode and advanced problem-solving capabilities so you can focus on what you do best: creating high quality apps for your users.

We are beginning to roll out limited Gemini 3 access (with a 1 million token size window) to developers who are using the no-cost default model. For higher usage rate limits and longer sessions with Agent Mode, you can add a paid Gemini API Key or use a Gemini Code Assist Enterprise plan. Learn more about how to [get started with Gemini 3](https://android-developers.googleblog.com/2025/11/gemini-3-is-now-available-for-ai.html).

**Enhance Agent Mode with Android knowledge**

While the training of large language models provides deep knowledge that is excellent for common tasks---like creating Compose UIs---training concludes on a fixed date, resulting in gaps for new libraries and updated best practices. They are also less effective with niche APIs because the necessary training data is scarce. To fix this, Android Studio's Agent Mode is now equipped with the [Android Knowledge Base](https://developer.android.com/r/studio-ui/gemini/android-knowledge-base), a new feature designed to significantly improve accuracy and reduce hallucinations by grounding responses with authoritative documentation. This means that instead of just relying on its training data, the agent can actively consult fresh documentation from official sources like the Android developer docs, Firebase, Google Developers, and Kotlin docs before it answers you.

The information in the Android Knowledge Base is stored in Android Studio and its content is automatically updated in the background on a periodic basis, so this feature is available regardless of which LLM you're using for AI assistance.
![agent.png](https://developer.android.com/static/blog/assets/agent_9f9eebd143_Z2rsL5X.webp)

*Gemini searching documentation before it answers you*

This feature will be invoked automatically when Agent Mode detects a need for additional context, and you'll see additional explanatory text. However, if you'd like Agent Mode to reference documentation more frequently, you can include a line such as "Refer to Android documentation for guidance" in your [Rules configuration](https://developer.android.com/studio/gemini/rules).

**Requested settings updates**

**Backup and Sync**

[Backup and Sync](https://developer.android.com/studio/intro/studio-config#ExportImportSettings) is a new way to keep your personalized Android Studio environment consistent across all your installations. You can now back up your settings---including your preferred keymaps, Code Editor settings, system settings, and more---to cloud storage using your Google Account, giving you a seamless experience wherever you code. We also support Backup and Sync using JetBrains accounts for developers using both IntelliJ and Android Studio installs simultaneously.
![settings.png](https://developer.android.com/static/blog/assets/settings_d1b7687b5e_ZL9B4g.webp)

*Backup and Sync*

Getting started is simple. Just sign into your Google Account by clicking the avatar in the top-right corner of the IDE, or navigate to **Settings \> Backup and Sync**. Once you authorize Android Studio to access your account's storage, you have full control over which categories of app data you want to sync. If you're syncing for the first time on a new machine, Android Studio will give you the option to either download your existing remote settings or upload your current local settings to the cloud. Of course, if you change your mind, you can easily disable Backup and Sync at any time from the settings menu. This feature has been available since the first Android Studio Otter release.

**Communications from Android Studio**

You can now opt in to receive communications directly from the Android Studio team. This enables you to get emails and notifications about important product updates, new features, and new libraries as soon as they're available.

You'll see this option when you sign in, and you can change your preference at any time by going to **Settings \> Tools \> Google Accounts \> Communications**.
![astudio.png](https://developer.android.com/static/blog/assets/astudio_2cdbfad21c_Z8k1OB.webp)

*Your option to receive emails and notifications*

**IntelliJ Merge Updates**

This release incorporates all stability and quality improvements from the [IntelliJ IDEA 2025.2 platform](https://www.jetbrains.com/idea/whatsnew/2025-2/). Notable highlights include:

- **Kotlin K2 Mode:** Following its rapid adoption after being enabled by default, the K2 Kotlin mode is now more stable and performant. This version improves Kotlin code analysis stability, adds new inspections, and enhances the reliability of Kotlin script execution.
- **Terminal Performance:** The integrated terminal is significantly faster, with major improvements in rendering. For Bash and Zsh, this update also introduces minor visual refinements without compromising or altering core shell behavior.

**Get started**

Ready to dive in and accelerate your development? [Download](https://developer.android.com/studio) Android Studio Otter 2 Feature Drop and start exploring these powerful new features today! As always, your feedback is crucial to us. [Check known issues](https://developer.android.com/studio/known-issues), [report bugs](https://developer.android.com/studio/report-bugs), and be part of our vibrant community on [LinkedIn](https://www.linkedin.com/showcase/androiddev/posts/?feedView=all) [Medium](https://medium.com/androiddevelopers), [YouTube](https://www.youtube.com/c/AndroidDevelopers/videos), or [X](https://twitter.com/androidstudio). Let's build the future of Android apps together!

###### Written by:

-

  ## [Sandhya Mohan](https://developer.android.com/blog/authors/sandhya-mohan)

  ###### Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/sandhya-mohan) ![](https://developer.android.com/static/blog/assets/Sandhya_Mohan_30435468a9_1b689e.webp) ![](https://developer.android.com/static/blog/assets/Sandhya_Mohan_30435468a9_1b689e.webp)
-

  ## [Trevor Johns](https://developer.android.com/blog/authors/trevor-johns)

  ###### Staff Developer Programs Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/trevor-johns) ![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg) ![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/Sandhya_Mohan_30435468a9_1b689e.webp)](https://developer.android.com/blog/authors/sandhya-mohan)[![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)](https://developer.android.com/blog/authors/trevor-johns) 15 Jan 2026 15 Jan 2026 ![](https://developer.android.com/static/blog/assets/as_Otter3feb_2dc12a1b18_Z1VaHAk.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [LLM flexibility, Agent Mode improvements, and new agentic experiences in Android Studio Otter 3 Feature Drop](https://developer.android.com/blog/posts/llm-flexibility-agent-mode-improvements-and-new-agentic-experiences-in-android-studio-otter-3-feature-drop)

  [arrow_forward](https://developer.android.com/blog/posts/llm-flexibility-agent-mode-improvements-and-new-agentic-experiences-in-android-studio-otter-3-feature-drop) We are excited to announce that Android Studio Otter 3 Feature Drop is now stable! This feature-packed release brings a huge update to your agentic workflows in Android Studio, and offers you more flexibility and control for how you use AI to help you build Android apps.

  ###### [Sandhya Mohan](https://developer.android.com/blog/authors/sandhya-mohan), [Trevor Johns](https://developer.android.com/blog/authors/trevor-johns) •
  9 min read

- [![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)](https://developer.android.com/blog/authors/trevor-johns) 02 Mar 2026 02 Mar 2026 ![](https://developer.android.com/static/blog/assets/supercharge_99f4219536_Z2aoaib.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Supercharge your Android development with 6 expert tips for Gemini in Android Studio](https://developer.android.com/blog/posts/supercharge-your-android-development-with-6-expert-tips-for-gemini-in-android-studio)

  [arrow_forward](https://developer.android.com/blog/posts/supercharge-your-android-development-with-6-expert-tips-for-gemini-in-android-studio) In January we announced Android Studio Otter 3 Feature Drop in stable, including Agent Mode enhancements and many other updates to provide more control and flexibility over using AI to help you build high quality Android apps.

  ###### [Trevor Johns](https://developer.android.com/blog/authors/trevor-johns) •
  4 min read

- [![](https://developer.android.com/static/blog/assets/meghan_d663ed9c69_e0a5b5a564_Z21FLk.webp)](https://developer.android.com/blog/authors/meghan-mehta) 22 Apr 2026 22 Apr 2026 ![](https://developer.android.com/static/blog/assets/0420_Compose_1_11_Strapi_9c17b19a5e_1zjMqo.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [What's new in the Jetpack Compose April '26 release](https://developer.android.com/blog/posts/whats-new-in-the-jetpack-compose-april-26-release)

  [arrow_forward](https://developer.android.com/blog/posts/whats-new-in-the-jetpack-compose-april-26-release) The Jetpack Compose April '26 release is stable. This release contains version 1.11 of core Compose modules (see the full BOM mapping), shared element debug tools, trackpad events, and more.

  ###### [Meghan Mehta](https://developer.android.com/blog/authors/meghan-mehta) •
  5 min read

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)