---
title: https://developer.android.com/blog/posts/android-studio-narwhal-4-feature-drop-watch-face-support-and-improved-stability
url: https://developer.android.com/blog/posts/android-studio-narwhal-4-feature-drop-watch-face-support-and-improved-stability
source: md.txt
---

#### [Product News](https://developer.android.com/blog/categories/product-news)

# Android Studio Narwhal 4 Feature Drop: watch face support and improved stability

###### 5-min read

![](https://developer.android.com/static/blog/assets/as_Narwhal_7bf25b6657_Zl5Grc.webp) 09 Oct 2025 [![](https://developer.android.com/static/blog/assets/2_o2_H5_V1lr_Zrcfhto_Au9_B2_Q_fd3ec10461_acae303cd5_Z2izffS.webp)](https://developer.android.com/blog/authors/paris-hsu) [##### Paris Hsu](https://developer.android.com/blog/authors/paris-hsu)

###### Product Manager, Android Studio

[Android Studio Narwhal 4 Feature Drop](https://developer.android.com/studio) is now stable and ready for you to use! This release brings targeted support for declarative Wear OS watch faces, a new customization option for your Project view, and continues our focus on quality by fixing 550+ numbers of bugs to improve stability and performance. You told us Agent Mode has been really helpful for your productivity, and we've now graduated it from being in preview to being stable.

This is also the final feature drop for the Android Studio Narwhal releases. With the [new monthly release cadence](https://android-developers.googleblog.com/2025/08/accelerating-development-with-monthly-releases-android-studio-2x-more-than-before.html), we've been delivering new features and bug fixes every month. The last three Narwhal releases have been packed with features, including the launch of Agent Mode and Compose previews. We'd like to not only share what's new in this release, but also recap some key features from the Narwhal releases.

## What's New in Android Studio Narwhal 4 Feature Drop

Here are the new features shipping with this release:

### Declarative Wear OS watch faces support in Android Studio ⌚

Android Studio Narwhal 4 Feature Drop improves the workflow for creating Wear OS [watch faces](https://developer.android.com/training/wearables/watch-faces) by introducing editor support for the [Watch Face XML Format](https://developer.android.com/training/wearables/wff) to write, debug, and fine-tune your watch face designs directly within the IDE. This helps you work faster by bringing the Android development process into the IDE instead of having to change context and work with multiple programs when developing watch faces.
![Declarative-watchfaces.gif](https://developer.android.com/static/blog/assets/Declarative_watchfaces_4fa8d2cf1c_Z41FCK.webp)

Android Studio lets you directly edit the XML files used in the Watch Face Format. It now provides code completion for tags and attributes based on the official Watch Face Format schemas and live error validation that helps identify issues like missing required attributes. Android Studio also includes resource linking to quickly navigate to drawable resources and other referenced XML elements along with advanced syntax support for handling arithmetic expressions and data source references embedded in the XML. Finally, you can deploy watch faces directly to a Wear OS emulator or physical device from Android Studio.

### Option to make Project view your default 📂

Tired of always having to switch to the Project view every time you open a new project? There is a new setting to have new projects open in Project view by default. To enable the setting go to **File** (**Android Studio** on macOS) **\> Settings \> Advanced Settings \> Project View** and select **Set Project view as the default**.
![large_Project_view_default_8f84ca0259.png](https://developer.android.com/static/blog/assets/large_Project_view_default_8f84ca0259_6a23e31a8f_1NTvk1.webp)

## A look back: key features from the Android Studio Narwhal releases

The Android Studio Narwhal releases have been packed with features, especially with our move to monthly releases. Between powerful AI integrations and new testing tools, it can be easy to miss an update. Below, we highlight a few key features, but for a complete look at everything we shipped, we highly recommend reading the full posts for [Narwhal Feature Drop](https://android-developers.googleblog.com/2025/07/android-studio-narwhal-feature-drop-stable-agent-mode.html) and [Narwhal 3 Feature Drop](https://android-developers.googleblog.com/2025/09/android-studio-narwhal-3-smarter-ai-backup-restore-compose-preview.html).

Here's a quick summary of some of the top features you should be trying out:

### Agent Mode (now stable!)

Have Google Gemini help with your tasks by using [Agent Mode](https://developer.android.com/studio/gemini/agent-mode). The AI agent can understand your project, break down complex tasks into smaller steps, make edits on your behalf, and help you with multi-step operations --- like adding new features, refactoring code, or debugging complex issues right inside your IDE. [Developers such as Entri used Agent Mode](https://youtu.be/zpAy91KUkfg?si=AM2U73VviAheBXxu&t=146) to generate Jetpack Compose layouts from UI mockups, and found that Gemini in Android Studio reduced their overall UI development time by 40%.
![large_agent_mode_bc15d51e81.png](https://developer.android.com/static/blog/assets/large_agent_mode_bc15d51e81_398cb81353_1uY2CM.webp)

### Android partner device labs (using Android Device Streaming)

We expanded Android Device Streaming by adding [Android Partner Device Labs](https://developer.android.com/studio/run/android-device-streaming#2P). This gives you secure access to a wide range of remote, physical devices from partners like Samsung, enabling you to test your app's compatibility and performance on some of the most popular devices in the market, directly from Android Studio.
![large_Partner_device_labs_9f591f44d0.png](https://developer.android.com/static/blog/assets/large_Partner_device_labs_9f591f44d0_a8477e5007_rQ32e.webp)

### Test app backup and restore

We added tools to test your app's data backup and restoration flow. This is critical for ensuring a smooth user experience when switching to a new device. You can generate a backup of your app's data, restore it to another device, and even attach backups to your run configurations to test this flow easily.
![large_Backup_restore_50901ad504.png](https://developer.android.com/static/blog/assets/large_Backup_restore_50901ad504_4255c19f0b_1HOTJb.webp)

### Resizable Compose Preview

Building responsive UIs became much easier in Android Studio Narwhal. [Compose Preview](https://developer.android.com/develop/ui/compose/tooling/previews) now supports dynamic resizing, giving you instant visual feedback on how your UI adapts to different screen sizes. You can simply enter Focus mode in the Compose Preview and drag the edges to see your layout change in real time.
![resizable_preview_87e89db34a.gif](https://developer.android.com/static/blog/assets/resizable_preview_87e89db34a_dfee635ba1_9JDEi.webp)

### Google Play policy insights

Get early warnings about potential Google Play policy violations to help you build more compliant apps with Play Policy Insights, now in Android Studio. The IDE now shows lint warnings directly in your code when it relates to a Google Play policy requirement. You can also integrate these lint checks into your CI/CD pipelines. These insights provide an overview of the policy, dos and don'ts, and links more resources, helping you address potential issues early in your development cycle.
![small_unnamed_488ff3b00e.png](https://developer.android.com/static/blog/assets/small_unnamed_488ff3b00e_0c9103612e_Z21HyvP.webp)

*** ** * ** ***

### Summary

To recap, the entire Android Studio Narwhal release series, including this Narwhal 4 Feature Drop, has delivered a wide array of powerful features. Here is a comprehensive summary of the major additions:

**Develop with AI (Gemini)**

- **Agent Mode:** An semi-autonomous AI assistant that helps with complex, multi-step operations like refactoring, adding features, and debugging.
- **AGENTS.md support:** Provide project-specific context, instructions, and style guides to Gemini.
- **Rules in Prompt Library:** Customize Gemini's output to match your team's coding standards.
- **Image \& @File attachment:** Attach screenshots and project files for more context-aware responses.
- **Transform UI (Studio Labs):** Use natural language to iterate on Compose UI directly in the preview window.

**Faster UI iteration and development**

- **Declarative Wear OS watch faces support (New in Narwhal 4 ✨):** Write, debug, and deploy watch faces with code completion, error validation, and direct deployment.
- **Resizable Compose Preview:** Dynamically resize previews in Focus mode to instantly test responsive UIs.
- **Compose preview improvements:** Better code navigation and a new picker for managing previews.

**Optimize, refine and test**

- **Test App Backup and Restore:** Easily test your app's data backup and restoration flow for new device transfers.
- **Android Partner Device Labs:** Access a wide range of remote, physical partner devices from Samsung and more for testing.
- **Google Play policy insights:** Get early warnings about potential Play Policy violations directly in the IDE.
- **Proguard inspections:** Identify and fix overly broad keep rules for better code optimization.
- **K2 mode by default:** Faster performance with the next-generation Kotlin compiler.
- **16 KB page size support:** Lint warnings and an emulator to prepare for new devices.

**Immersive development (XR)**

- **Embedded Android XR emulator:** Run the XR emulator directly inside the IDE.
- **Embedded Layout Inspector for Android XR:** Inspect and optimize UI layouts within the XR environment.
- **Android XR project template:** A new template to quickly start XR projects.

**IDE workflow and quality improvements**

- **Project view default (New in Narwhal 4 ✨):** A new advanced setting to always open new projects in the Project view.
- **Display build files under module:** Improve project navigation in the Android view.
- **Manual project sync:** Gain more control over when Gradle syncs occur in large projects.
- **Quality improvements:** Fixed xx numbers of bugs in this release for better stability and performance.

*** ** * ** ***

## Get started

Ready to accelerate your development? [**Download**](https://developer.android.com/studio)**Android Studio Narwhal 4 Feature Drop from the stable channel today!**

Your feedback is essential. Please continue to share your thoughts by [reporting bugs](https://developer.android.com/studio/report-bugs) or [suggesting features](https://developer.android.com/studio/report-bugs). For early access to the latest features, download Android Studio from the [Canary channel](https://developer.android.com/studio/preview).

Join our vibrant Android developer community on[LinkedIn](https://www.google.com/search?q=https://www.linkedin.com/company/android-developers/),[Medium](https://android-developers.googleblog.com/),[YouTube](https://www.youtube.com/user/androiddevelopers), or[X](https://x.com/AndroidDev). We can't wait to see what you build!
- [#Android Studio](https://developer.android.com/blog/topics/android-studio)

###### Written by:

-

  ## [Paris Hsu](https://developer.android.com/blog/authors/paris-hsu)

  ###### Product Manager, Android Studio

  [read_more
  View profile](https://developer.android.com/blog/authors/paris-hsu) ![](https://developer.android.com/static/blog/assets/2_o2_H5_V1lr_Zrcfhto_Au9_B2_Q_fd3ec10461_acae303cd5_Z2izffS.webp) ![](https://developer.android.com/static/blog/assets/2_o2_H5_V1lr_Zrcfhto_Au9_B2_Q_fd3ec10461_acae303cd5_Z2izffS.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/matthew_warner_67a99317e4_Z2c1VNu.webp)](https://developer.android.com/blog/authors/matthew-warner) 02 Apr 2026 02 Apr 2026 ![](https://developer.android.com/static/blog/assets/android_studio_gemma4_73370772af_2lUopR.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android Studio supports Gemma 4: our most capable local model for agentic coding](https://developer.android.com/blog/posts/android-studio-supports-gemma-4-our-most-capable-local-model-for-agentic-coding)

  [arrow_forward](https://developer.android.com/blog/posts/android-studio-supports-gemma-4-our-most-capable-local-model-for-agentic-coding) Every developer's AI workflow and needs are unique, and it's important to be able to choose how AI helps your development. In January, we introduced the ability to choose any local or remote AI model to power AI functionality in Android Studio

  ###### [Matthew Warner](https://developer.android.com/blog/authors/matthew-warner) •
  2 min read

  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)
- [![](https://developer.android.com/static/blog/assets/matt_dyor_b779fca40e_Z2hl456.webp)](https://developer.android.com/blog/authors/matt-dyor) 02 Apr 2026 02 Apr 2026 ![](https://developer.android.com/static/blog/assets/as_Panda3_385cde5eac_Z1E8IhJ.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Increase Guidance and Control over Agent Mode with Android Studio Panda 3](https://developer.android.com/blog/posts/increase-guidance-and-control-over-agent-mode-with-android-studio-panda-3)

  [arrow_forward](https://developer.android.com/blog/posts/increase-guidance-and-control-over-agent-mode-with-android-studio-panda-3) Android Studio Panda 3 is now stable and ready for you to use in production. This release gives you even more control and customization over your AI-powered workflows, making it easier than ever to build high-quality Android apps.

  ###### [Matt Dyor](https://developer.android.com/blog/authors/matt-dyor) •
  3 min read

  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)
- [![](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_Z1Fsr5h.webp)](https://developer.android.com/blog/authors/matthew-mccullough) 02 Apr 2026 02 Apr 2026 ![](https://developer.android.com/static/blog/assets/Gemma_Android_2x1_2x_a6d27254c4_Z10SxJJ.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Gemma 4: The new standard for local agentic intelligence on Android](https://developer.android.com/blog/posts/gemma-4-the-new-standard-for-local-agentic-intelligence-on-android)

  [arrow_forward](https://developer.android.com/blog/posts/gemma-4-the-new-standard-for-local-agentic-intelligence-on-android) Today, we are enhancing Android development with Gemma 4, our latest state-of-the-art open model designed with complex reasoning and autonomous tool-calling capabilities.

  ###### [Matthew McCullough](https://developer.android.com/blog/authors/matthew-mccullough) •
  2 min read

  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)