---
title: https://developer.android.com/blog/posts/level-up-your-development-with-planning-mode-and-next-edit-prediction-in-android-studio-panda-4
url: https://developer.android.com/blog/posts/level-up-your-development-with-planning-mode-and-next-edit-prediction-in-android-studio-panda-4
source: md.txt
---

#### [Product News](https://developer.android.com/blog/categories/product-news)

# Level up your development with Planning Mode and Next Edit Prediction in Android Studio Panda 4

###### 5-min read

![](https://developer.android.com/static/blog/assets/as_Panda3_385cde5eac_Z1E8IhJ.webp) 21 Apr 2026 [![](https://developer.android.com/static/blog/assets/matt_dyor_b779fca40e_Z2hl456.webp)](https://developer.android.com/blog/authors/matt-dyor) [##### Matt Dyor](https://developer.android.com/blog/authors/matt-dyor)

###### Senior Product Manager

Android Studio Panda 4 is now stable and ready for you to use in production. This release brings Planning Mode, Next Edit Prediction, and more, making it easier than ever to build high-quality Android apps.
[Video](https://www.youtube.com/watch?v=ThfXy_Cx4gg)

Here's a deep dive into what's new:

## **Planning Mode**

Before the agent starts working on complex tasks for you, it would be helpful if it could come up with a detailed plan. Jumping straight into a large coding project without a design often leads to technical debt or logic errors; the same is true for AI. That's why we're adding Planning Mode.

In this mode, the agent comes up with a detailed project plan before executing tasks. Instead of a single pass where the model directly predicts the next token of code, Planning Mode facilitates a multi-stage reasoning process---giving the agent additional space to evaluate its own proposed logic for potential issues before presenting it to you. This is especially useful for complex and long-running tasks which demand a high degree of architectural precision.

To use Planning Mode, switch your conversation mode to "Planning" in the agent input box and enter your prompt.
![2-5-walkthrough-artifact.png](https://developer.android.com/static/blog/assets/2_5_walkthrough_artifact_e8031644b5_1AfWMi.webp) Switch to Planning Mode

In Planning Mode, the agent examines your request and may generate an implementation plan for large or complex tasks. You have the opportunity to fix mistakes or clarify which approaches to use---all before the agent has spent any time or tokens heading in the wrong direction.
![2-2-open-implementation-plan.png](https://developer.android.com/static/blog/assets/2_2_open_implementation_plan_b21e774e25_Z1DRbbr.webp) Open Implementation Plan ![2-3-add-comments-to-implementation.png](https://developer.android.com/static/blog/assets/2_3_add_comments_to_implementation_ed1fe9893c_uKc7D.webp) Add Comments to Implementation Plan

After adding comments, click "Submit Comments" and the agent will use your feedback to revise the implementation plan. To stay on track during execution---which is particularly important with larger changes---the agent organizes its work and generates a "Task List" artifact. You can sit back and watch as the agent methodically completes all of the tasks.
![2-4=task-list-artifact.png](https://developer.android.com/static/blog/assets/2_4_task_list_artifact_61fd3b0665_V3WrM.webp) Task List Artifact

After the work is done, the agent produces a "Walkthrough" artifact, giving you a clear summary of exactly what has been changed and making it easy to review the agent's changes. Build with more confidence and control using Planning Mode in the latest release of Android Studio.
![2-1-switch-to-planning-mode.png](https://developer.android.com/static/blog/assets/2_1_switch_to_planning_mode_9ae893cfbf_Z2qD2nL.webp) Add Comments to Implementation Plan

## **Next Edit Prediction**

Classic autocomplete is great for finishing your sentences, but coding is rarely a linear path. Often, a change in one place requires a secondary change elsewhere---like adding a new parameter to a function and then needing to update its invocations, or a UI preview update when a Composable is changed. Traditionally, this meant breaking your focus to hunt down the related lines of code that need attention.

Next Edit Prediction (NEP) evolves code completion by anticipating your next move, even when it's not at your current cursor position. By analyzing your recent edits, Android Studio recognizes the logical pattern of your workflow. If you modify a data class or update a constructor, NEP can suggest the next relevant edit---perhaps in a distant function---allowing you to jump straight to the fix.

Instead of manually navigating back and forth, you can accept these multi-location suggestions with a single keystroke. This keeps you deep in the "flow state," reducing the cognitive load of routine updates and letting you focus on the complex logic that truly matters to your application. Experience a more intuitive, non-linear way to code in the latest version of Android Studio.
![3-1-nep-update.png](https://developer.android.com/static/blog/assets/3_1_nep_update_5519a97e2d_15b2Em.webp) NEP Updating Function Name ![3-2-nep-addition.png](https://developer.android.com/static/blog/assets/3_2_nep_addition_061cf6e8d9_Zc5y4S.webp) NEP Adding New Line

## **Gemini API Starter Template**

Adding powerful AI features to your app just got easier, introducing the Gemini API Starter template for Android Studio!   

Integrating generative AI into your Android application used to mean managing complex backend plumbing and worrying about API key security. With the new Gemini API Starter template in Android Studio, developers can now jump straight into building features rather than spending time configuring infrastructure.

**Key benefits include:**

- **Zero API key management:**Stop worrying about provisioning or rotating keys. By leveraging Firebase AI Logic, the template eliminates the need to embed sensitive credentials in your client-side code.
- **Automated Firebase integration:**The backend plumbing is handled for you. The template automatically connects your project to Firebase services, ensuring a secure bridge between your app and Google's Gemini models.
- **Built to scale:**This isn't just for prototypes. The production-ready architecture allows you to scale from a local test to a global user base without redesigning your foundation.
- **Multimodal processing:** Supports text, image, video, and audio inputs. You can build features like real-time image analysis, video summarization, and audio transcription.

### **Get started**

1. Open Android Studio.
2. Navigate to **File \> New \> New Project**.
3. Select the Gemini API Starter template from the gallery.

![4-1-gemini-api-template.png](https://developer.android.com/static/blog/assets/4_1_gemini_api_template_9114ef3aa8_2dmc6r.webp) Gemini API Starter new project template

## **Agent Web Search**

When you're deep in development, the right answer is often just a search away---but leaving your IDE to find it can snap you out of your flow. Whether you need the exact version number for a dependency or the latest API changes for a third-party library, the agent web search tool is here to help without you ever having to leave Android Studio.

While Android Studio's agent already leverages the [Android Knowledge Base](https://developer.android.com/studio/gemini/knowledge-base) for official documentation, modern Android development relies on a vast ecosystem of external libraries. Agent web search expands Gemini's reach, allowing it to query Google directly to fetch current reference material from across the web. From checking the latest setup guides for Coil to finding advanced configuration tips for Koin or Moshi, the agent can now pull in the most up-to-date information in real time.

The agent web search tool is designed to be helpful but unobtrusive; it will automatically trigger a web search when it identifies a gap in its local knowledge. You can also take the wheel by asking it to find something specific---simply include "**search the web for...**" in your prompt. By integrating live web results directly into your workspace, agent web search ensures you're always building with the most current data available, speeding up your workflow and keeping your project on the cutting edge.
![trash-5-1-aws-invocation.png](https://developer.android.com/static/blog/assets/trash_5_1_aws_invocation_7c63aee270_1soPNV.webp) Agent Web Search Tool Invocation

### **Android Studio Panda releases**

Panda 4 continues Android Studio's focus on accelerating developer productivity with AI. Check out [Go from prompt to working prototype with Android Studio Panda 2](https://android-developers.googleblog.com/2026/05/go-from-prompt-to-working-prototype.html) and [Increase Guidance and Control over Agent Mode with Android Studio Panda 3](https://android-developers.googleblog.com/2026/04/Increase-Guidance-and-Control-over-Agent-Mode-with-Android-Studio-Panda-3.html).

#### [**Android Studio Panda 2**](https://android-developers.googleblog.com/2026/05/go-from-prompt-to-working-prototype.html)

- **AI-powered New Project flow**: Allows you to build a working app prototype with a single prompt. The agent manages initial setup, navigation configuration, and proper dependencies, and features an autonomous generation loop to handle build errors and deploy to an emulator.
- **Version Upgrade Assistant**: Automates dependency management and updates, iteratively attempting builds and resolving conflicts until a stable configuration is found.

#### [**Android Studio Panda 3**](https://android-developers.googleblog.com/2026/04/Increase-Guidance-and-Control-over-Agent-Mode-with-Android-Studio-Panda-3.html)

- **Agent skills**: Specialized, user-defined instructions (stored in a .skills directory) that teach the AI agent project-specific capabilities, coding standards, or library usage.
- **Agent permissions**: Provides fine-grained control over what agents can do, with features like "Always Allow" rules for trusted operations. For even more security, you can also use an optional sandbox to enforce strict, isolated control over the agent.
- **Empty Car App Library App template**: Simplifies building driving-optimized apps for Android Auto and Android Automotive OS by handling required boilerplate code.

### **Get started**

Dive in and accelerate your development. [Download](https://developer.android.com/studio) Android Studio Panda 4 and start exploring these powerful new agentic features today.

As always, your feedback is crucial to us. [Check known issues](https://developer.android.com/studio/known-issues), [report bugs](https://developer.android.com/studio/report-bugs), and be part of our vibrant community on [LinkedIn](https://www.linkedin.com/showcase/androiddev/posts/?feedView=all), [Medium](https://medium.com/androiddevelopers), [YouTube](https://www.youtube.com/c/AndroidDevelopers/videos), or [X](https://twitter.com/androidstudio). Happy coding

###### Written by:

-

  ## [Matt Dyor](https://developer.android.com/blog/authors/matt-dyor)

  ###### Senior Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/matt-dyor) ![](https://developer.android.com/static/blog/assets/matt_dyor_b779fca40e_Z2hl456.webp) ![](https://developer.android.com/static/blog/assets/matt_dyor_b779fca40e_Z2hl456.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/matt_dyor_b779fca40e_Z2hl456.webp)](https://developer.android.com/blog/authors/matt-dyor) 02 Apr 2026 02 Apr 2026 ![](https://developer.android.com/static/blog/assets/as_Panda3_385cde5eac_Z1E8IhJ.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Increase Guidance and Control over Agent Mode with Android Studio Panda 3](https://developer.android.com/blog/posts/increase-guidance-and-control-over-agent-mode-with-android-studio-panda-3)

  [arrow_forward](https://developer.android.com/blog/posts/increase-guidance-and-control-over-agent-mode-with-android-studio-panda-3) Android Studio Panda 3 is now stable and ready for you to use in production. This release gives you even more control and customization over your AI-powered workflows, making it easier than ever to build high-quality Android apps.

  ###### [Matt Dyor](https://developer.android.com/blog/authors/matt-dyor) •
  3 min read

  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)
- [![](https://developer.android.com/static/blog/assets/matt_dyor_b779fca40e_Z2hl456.webp)](https://developer.android.com/blog/authors/matt-dyor) 03 Mar 2026 03 Mar 2026 ![](https://developer.android.com/static/blog/assets/as_Panda3_385cde5eac_Z1E8IhJ.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Go from prompt to working prototype with Android Studio Panda 2](https://developer.android.com/blog/posts/go-from-prompt-to-working-prototype-with-android-studio-panda-2)

  [arrow_forward](https://developer.android.com/blog/posts/go-from-prompt-to-working-prototype-with-android-studio-panda-2) Android Studio Panda 2 is now stable and ready for you to use in production.

  ###### [Matt Dyor](https://developer.android.com/blog/authors/matt-dyor) •
  3 min read

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