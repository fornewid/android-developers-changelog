---
title: Go from prompt to working prototype with Android Studio Panda 2  |  Android Developers' Blog
url: https://developer.android.com/blog/posts/go-from-prompt-to-working-prototype-with-android-studio-panda-2
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Android Developers' Blog](https://developer.android.com/)
* [Blog](https://developer.android.com/blog)

Stay organized with collections

Save and categorize content based on your preferences.



#### [Product News](/blog/categories/product-news)

# Go from prompt to working prototype with Android Studio Panda 2

###### 3-min read

![](/static/blog/assets/as_Panda3_385cde5eac_Z1E8IhJ.webp)

03

Mar
2026

[![](/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)](/blog/authors/matt-dyor)

[##### Matt Dyor](/blog/authors/matt-dyor)

###### Senior Product Manager

Android Studio Panda 2 is now stable and ready for you to use in production. This release brings new agentic capabilities to Android Studio, enabling the agent to create an entire working application from scratch with the AI-powered New Project flow, and allowing the agent to automate the manual work of dependency updates.

Whether you're building your first prototype or maintaining a large, established codebase, these updates bring new efficiency to your workflow by enabling Gemini in Android Studio to help more than ever.

Here’s a deep dive into what’s new:

## **Create New Projects with AI**

Say goodbye to boilerplate starter templates that just get you to the start line. With the [AI-powered New Project flow](/studio/gemini/create-a-new-project-with-ai), you can now build a working app prototype with just a single prompt.

The agent reduces the time you spend setting up dependencies, writing boilerplate code, and creating basic navigation, allowing you to focus on the creative aspects of app development. The AI-powered New Project flow allows you to describe exactly what you want to build - you can even upload images for style inspiration. The agent then creates a detailed project plan for your review.

When you're ready, the agent turns your plan into a first draft of your app using Android best practices, including Kotlin, Compose, and the latest stable libraries. Under your direction, it creates an autonomous generation loop: it generates the necessary code, builds the project, analyzes any build errors, and attempts to self-correct the code, looping until your project builds successfully. It then deploys your app to an Android Emulator and walks through each screen, verifying that the implementation works correctly and is true to your original request. Whether you need a simple single-screen layout, a multi-page app with navigation, or even an application integrated with Gemini APIs, the AI-powered New Project flow can handle it.

### **Getting Started**

To use the agent to set up a project, do the following:

1. Start Android Studio.
2. Select **New Project** on the **Welcome to Android Studio** screen (or **File > New > New Project** from within a project)
3. Select **Create with AI**.
4. Type your prompt into the text entry field and click **Next**.  For best results we recommend using a paid [Gemini API key](/studio/gemini/add-api-key) or third-party [remote model](/studio/gemini/use-a-remote-model).

![img1-what_do_you_want_to_build.png](/static/blog/assets/img1_what_do_you_want_to_build_8b609005c6_Zxl3al.webp)

*Create a New Project with AI in Android Studio*

5. Name your app and click **Finish** to start the generation process.

6. Validate the finished app using the project plan and by running your app in the Android Emulator or on an Android device.

![newprojectFlow.png](/static/blog/assets/newproject_Flow_86d8c2c331_1KBPK0.webp)

*AI-powered New Project flow*

For more details on the New Project flow, check out the [official documentation](/studio/gemini/create-a-new-project-with-ai).

### **Share What You Build**

We want to hear from you and see the apps you’re able to build using the New Project flow. Share your apps with us by using #AndroidStudio in your social posts. We’ll be amplifying some of your submissions on our social channels.

### **Unlock more with your Gemini API key**

While the agent works out-of-the-box using Android Studio's default no-cost model, providing your own Google AI Studio API key unlocks the full potential of the assistant. By connecting a paid Gemini API key, you get access to the fastest and latest models from Google. It also allows the New Project flow to access Nano Banana, our best model for image generation, in order to ideate on UI design — allowing the agent to create richer, higher fidelity application designs.

In the AI-powered New Project flow, this increased capability means larger context windows for more tailored generation, as well as superior code quality. Furthermore, because the Agent uses Nano Banana behind the scenes for enhanced design generation, your prototype doesn't just work well—it features visually appealing, modern UI layouts and looks professional from the get go.

## Version Upgrade Assistant

Keeping your project dependencies up to date is time-consuming and often causes cascading build errors. You fix one issue by updating a dependency, only to introduce a new issue somewhere else.

The Version Upgrade Assistant in Android Studio just made that a problem of the past. You can now let AI do the heavy lifting of managing dependencies and boilerplate so you can focus on creating unique experiences for your users.

To use this feature, simply right-click in your version catalog, select **AI**, and then **Update Dependencies**.

![versions.png](/static/blog/assets/versions_823cdf76df_11AfrC.webp)

*Version Upgrade Assistant accessed from Version Catalog*

You can also access the Version Upgrade Assistant from the **Refactor** menu—just choose **Update all libraries with AI**.

![versions2.png](/static/blog/assets/versions2_12062592c2_1iGQXa.webp)

*Version Upgrade Assistant accessed from the Refactor menu*

The agent runs multiple automated rounds—attempting builds, reading error messages, and adjusting versions—until the build succeeds. Instead of manually fighting through dependency conflicts, you can let the agent handle the iterative process of finding a stable configuration for you. Read the [documentation](/studio/gemini/manage-dependencies) for more information on Version Upgrade Assistant.

### **Gemini 3.1 Pro is available in Android Studio**

We released Gemini 3.1 Pro preview, and it is even better than Gemini 3 Pro for reasoning and intelligence. You can access it in Android Studio by plugging in your Gemini API key. Put the new model to work on your toughest bugs, code completion, and UI logic. Let us know what you think of the new model.

![geminipro2.png](/static/blog/assets/geminipro2_f3626b4f5d_1PAzQy.webp)

*Gemini 3.1 Pro Now Available in Android Studio*

## **Get started**

Dive in and accelerate your development. [Download](/studio) Android Studio Panda 2 and start exploring these powerful new agentic features today.

As always, your feedback is crucial to us. [Check known issues](/studio/known-issues), [report bugs](/studio/report-bugs), and be part of our vibrant community on [LinkedIn](https://www.linkedin.com/showcase/androiddev/posts/?feedView=all), [Medium](https://medium.com/androiddevelopers), [YouTube](https://www.youtube.com/c/AndroidDevelopers/videos), or [X](https://twitter.com/androidstudio). Happy coding!

###### Written by:

* ## [Matt Dyor](/blog/authors/matt-dyor)

  ###### Senior Product Manager

  [read\_more
  View profile](/blog/authors/matt-dyor)

  ![](/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)

  ![](/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)

## Continue reading

* [![](/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)](/blog/authors/matt-dyor)

  02

  Apr
  2026

  02

  Apr
  2026

  ![](/static/blog/assets/as_Panda3_385cde5eac_Z1E8IhJ.webp)

  #### [Product News](/blog/categories/product-news)

  ## [Increase Guidance and Control over Agent Mode with Android Studio Panda 3](/blog/posts/increase-guidance-and-control-over-agent-mode-with-android-studio-panda-3)

  [arrow\_forward](/blog/posts/increase-guidance-and-control-over-agent-mode-with-android-studio-panda-3)

  Android Studio Panda 3 is now stable and ready for you to use in production. This release gives you even more control and customization over your AI-powered workflows, making it easier than ever to build high-quality Android apps.

  ###### [Matt Dyor](/blog/authors/matt-dyor) • 3 min read

  + [#Android Studio](/blog/topics/android-studio)
* [![](/static/blog/assets/matthew_warner_67a99317e4_Z2c1VNu.webp)](/blog/authors/matthew-warner)

  02

  Apr
  2026

  02

  Apr
  2026

  ![](/static/blog/assets/android_studio_gemma4_73370772af_2lUopR.webp)

  #### [Product News](/blog/categories/product-news)

  ## [Android Studio supports Gemma 4: our most capable local model for agentic coding](/blog/posts/android-studio-supports-gemma-4-our-most-capable-local-model-for-agentic-coding)

  [arrow\_forward](/blog/posts/android-studio-supports-gemma-4-our-most-capable-local-model-for-agentic-coding)

  Every developer's AI workflow and needs are unique, and it's important to be able to choose how AI helps your development. In January, we introduced the ability to choose any local or remote AI model to power AI functionality in Android Studio

  ###### [Matthew Warner](/blog/authors/matthew-warner) • 2 min read

  + [#Android Studio](/blog/topics/android-studio)
* [![](/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)](/blog/authors/caren-chang)[![](/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)](/blog/authors/david-chou)

  02

  Apr
  2026

  02

  Apr
  2026

  ![](/static/blog/assets/announcing_gemma4_aicore_ce479292b9_Z15e7FP.webp)

  #### [Product News](/blog/categories/product-news)

  ## [Announcing Gemma 4 in the AICore Developer Preview](/blog/posts/announcing-gemma-4-in-the-ai-core-developer-preview)

  [arrow\_forward](/blog/posts/announcing-gemma-4-in-the-ai-core-developer-preview)

  At Google, we’re committed to bringing the most capable AI models directly to the Android devices in your pocket. Today, we’re thrilled to announce the release of our latest state-of-the-art open model: Gemma 4.

  ###### [Caren Chang](/blog/authors/caren-chang), [David Chou](/blog/authors/david-chou) • 3 min read

# Stay in the loop

Get the latest Android development insights delivered to your inbox
weekly.

[mail
Subscribe](/subscribe)

![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)