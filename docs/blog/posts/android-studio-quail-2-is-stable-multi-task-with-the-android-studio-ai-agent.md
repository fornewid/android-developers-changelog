---
title: https://developer.android.com/blog/posts/android-studio-quail-2-is-stable-multi-task-with-the-android-studio-ai-agent
url: https://developer.android.com/blog/posts/android-studio-quail-2-is-stable-multi-task-with-the-android-studio-ai-agent
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news)

# Android Studio Quail 2 is Stable: Multi-task with the Android Studio AI agent

3-min read ![](https://developer.android.com/static/blog/assets/Quail_Blog_Strapi_46fcc9f1a1_ZzldHB.webp) 16 Jul 2026 [![View Amman Asfaw's profile](https://developer.android.com/static/blog/assets/unnamed_11_a00df7e0e8_ZARb6S.webp)](https://developer.android.com/blog/authors/amman-asfaw) [Amman Asfaw](https://developer.android.com/blog/authors/amman-asfaw) Product Manager, Android Studio Android Studio Quail 2 is now stable and ready for you to use in production, bringing a shift to your IDE with concurrent agentic workflows, natively integrated memory leak profiling, and context-aware crash remediation. Whether you are performing a sweeping architectural overhaul, tracing a memory leak, or resolving a critical production crash, Android Studio keeps you anchored in your workspace by reducing manual friction.

Here's a deep dive into what's new:

### **Multi-tasking with parallel chats**

In Android Studio Quail 2, we've been hard at work redesigning Agent Mode from the ground up. This new architecture provides better performance, offers more flexibility for decomposing complex tasks, and improves the suite of internal tools the agent uses to do its work.

In addition to these behind-the-scenes improvements, these changes also allow you to converse across multiple agent chats simultaneously. Waiting for the Android Studio agent to finish a task before you can ask another question or initiate a separate task in Agent Mode is a bottleneck of the past. You can multi-task seamlessly: kick off a UI refactor in one tab, fix a ProGuard rule in a second, and generate documentation in a third.

You can also change which models the agent uses from chat to chat based on the requests you have. Take a look at [Android Bench](http://d.android.com/bench) for an analysis of how LLMs perform Android development tasks.

- With parallel chats, **How to use:** Click the **"+"** icon to start a new parallel conversation, and use the **History** icon to navigate between active tasks. Alternatively, select File \> New \> New Agent Tab to open a conversation in a dedicated tab.
- **Note:** Worktree support is currently unavailable. Exercise caution when running concurrent chats that modify the same project files, which can potentially lead to editor conflicts.

[Video](https://www.youtube.com/watch?v=U6T67Lbar-w)

![image.png](https://developer.android.com/static/blog/assets/image_baf6beb0a8_Z1htvdX.webp) Use the History icon to navigate between active tasks.

### **Memory leak detection with LeakCanary**

Memory leaks in Android occur when your code holds onto an object's reference long after its life cycle has ended. This prevents the Garbage Collector from reclaiming that memory, eventually leading to sluggish performance or OutOfMemoryError.

Hunting down memory leaks can be a tedious, manual task. Starting with Android Studio Quail 2, the popular open-source leak detector [LeakCanary](https://square.github.io/leakcanary/) is natively integrated directly into the Profiler as a dedicated, first-class task.

This integration transforms your debugging performance by lifting and shifting the heap analysis off your resource-constrained testing phone, and onto your powerful development computer. By running the analysis on your computer, leak tracing is up to five times faster and jank-free, leaving your test app running smoothly on the device.

Once a leak is detected during a profiling session:

- The Profiler renders an interactive, color-coded leak trace, grouping occurrences and estimating lost memory.
- You can click **Go to declaration** on any leaking object in the trace to instantly jump to that exact line of code in your editor.
- You can click **Fix with Agent** to have the Gemini agent ingest the trace, explain the root cause of the retained reference, and write the exact code change (such as unbinding a listener or clearing a static reference) to plug the leak.

![LeakCanaryLg.png](https://developer.android.com/static/blog/assets/Leak_Canary_Lg_a2b012e26e_ZR335v.webp) Review memory leaks identified via LeakCanary through the Fix with Agent button.

### **App Quality Insights agent integration**

Tracking down the root cause of an app crash can require manually synthesizing stack traces, device data, and source code. However Android Studio's App Quality Insights (AQI) is now fully integrated with Agent Mode to do the heavy lifting for you.

When you click on a crash in the AQI panel, you immediately get a concise, high-level summary of the issue. If you need to dig deeper, simply click **See more**. This opens a dedicated chat where the agent uses your selected model and pulls in local source code and the full stack trace to deliver a comprehensive explanation of the failure.

With the new agent integration, you move directly from issue identification to resolution. By clicking **Fix with AI**, the agent will analyze the issue, propose a step-by-step fix plan, and---upon your approval---apply the necessary code changes directly to your project and verify the resulting fix

[Video](https://www.youtube.com/watch?v=JjgEePciHHg)

### **Quality \& stability improvements**

Beyond new features, we've continued our focus on quality by addressing numerous bugs and incorporating the latest stability and performance improvements from the IntelliJ platform, making this a significant enhancement for your daily development.

### **Get Started**

Ready to dive in and accelerate your development? [Download](https://developer.android.com/studio) Android Studio Quail 2 and start exploring these new features today! As always, your feedback is crucial to us. [Check known issues](https://developer.android.com/studio/known-issues), [report bugs](https://developer.android.com/studio/report-bugs), and be part of our vibrant community on [LinkedIn](https://www.linkedin.com/showcase/androiddev/posts/?feedView=all) [Medium](https://medium.com/androiddevelopers), [YouTube](https://www.youtube.com/c/AndroidDevelopers/videos), or [X](https://twitter.com/androidstudio).
- [#Gemini in Android Studio](https://developer.android.com/blog/topics/gemini-in-android-studio)
- [# Quail 2](https://developer.android.com/blog/topics/quail-2)
- [#Android Studio](https://developer.android.com/blog/topics/android-studio)
Written by:

-

  ## [Amman Asfaw](https://developer.android.com/blog/authors/amman-asfaw)

  ###### Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/amman-asfaw) ![View Amman Asfaw's profile](https://developer.android.com/static/blog/assets/unnamed_11_a00df7e0e8_ZARb6S.webp) ![View Amman Asfaw's profile](https://developer.android.com/static/blog/assets/unnamed_11_a00df7e0e8_ZARb6S.webp)
Continue reading
- [![View Matthew Warner's profile](https://developer.android.com/static/blog/assets/matthew_warner_67a99317e4_Z2c1VNu.webp)](https://developer.android.com/blog/authors/matthew-warner) 19 May 2026 19 May 2026 ![](https://developer.android.com/static/blog/assets/Google_For_Developers_Android_Combo_Strapi_2000x1000_5793c01e36_ZVoYvg.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android Studio I/O Edition: What's new in Android Developer tools](https://developer.android.com/blog/posts/android-studio-i-o-edition-what-s-new-in-android-developer-tools)

  [arrow_forward](https://developer.android.com/blog/posts/android-studio-i-o-edition-what-s-new-in-android-developer-tools) This year at Google I/O we are going beyond iterative changes, towards a fundamental shift in how apps are built. Our newest tools are built for the agentic era with features that boost productivity for you as an Android developer AND supercharge the AI agents you deploy in your codebase.
  [Matthew Warner](https://developer.android.com/blog/authors/matthew-warner) • 8 min read
  - [#Agent Skills](https://developer.android.com/blog/topics/agent-skills)
  - [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
  - [#Android](https://developer.android.com/blog/topics/android)
  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)
  - +2 ↩
- [![View Matthew Warner's profile](https://developer.android.com/static/blog/assets/matthew_warner_67a99317e4_Z2c1VNu.webp)](https://developer.android.com/blog/authors/matthew-warner) 02 Apr 2026 02 Apr 2026 ![](https://developer.android.com/static/blog/assets/android_studio_gemma4_73370772af_2lUopR.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android Studio supports Gemma 4: our most capable local model for agentic coding](https://developer.android.com/blog/posts/android-studio-supports-gemma-4-our-most-capable-local-model-for-agentic-coding)

  [arrow_forward](https://developer.android.com/blog/posts/android-studio-supports-gemma-4-our-most-capable-local-model-for-agentic-coding) Every developer's AI workflow and needs are unique, and it's important to be able to choose how AI helps your development. In January, we introduced the ability to choose any local or remote AI model to power AI functionality in Android Studio
  [Matthew Warner](https://developer.android.com/blog/authors/matthew-warner) • 2 min read
  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)
- [![View Matt Dyor's profile](https://developer.android.com/static/blog/assets/matt_dyor_b779fca40e_Z2hl456.webp)](https://developer.android.com/blog/authors/matt-dyor) 02 Apr 2026 02 Apr 2026 ![](https://developer.android.com/static/blog/assets/as_Panda3_385cde5eac_Z1E8IhJ.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Increase Guidance and Control over Agent Mode with Android Studio Panda 3](https://developer.android.com/blog/posts/increase-guidance-and-control-over-agent-mode-with-android-studio-panda-3)

  [arrow_forward](https://developer.android.com/blog/posts/increase-guidance-and-control-over-agent-mode-with-android-studio-panda-3) Android Studio Panda 3 is now stable and ready for you to use in production. This release gives you even more control and customization over your AI-powered workflows, making it easier than ever to build high-quality Android apps.
  [Matt Dyor](https://developer.android.com/blog/authors/matt-dyor) • 3 min read
  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)