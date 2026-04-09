---
title: Optimizing Performance for Android XR with Unity  |  Android Developers' Blog
url: https://developer.android.com/blog/posts/optimizing-performance-for-android-xr-with-unity
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Android Developers' Blog](https://developer.android.com/)
* [Blog](https://developer.android.com/blog)

Stay organized with collections

Save and categorize content based on your preferences.



#### [Product News](/blog/categories/product-news)

# Optimizing Performance for Android XR with Unity

###### 6-min read

![](/static/blog/assets/xr_Week5_985628de53_229QRh.webp)

23

Oct
2025

[![](/static/blog/assets/Luke_Hopkins_9c1e15d778_Z2o9b3q.webp)](/blog/authors/luke-hopkins)

[##### Luke Hopkins](/blog/authors/luke-hopkins)

###### Developer Relations Engineer, Android

[*Samsung Galaxy XR is here*](https://android-developers.googleblog.com/2025/10/giving-your-apps-new-home-on-samsung.html)*, powered by Android XR! This blog post is part of our*[*Android XR Spotlight Week*](https://android-developers.googleblog.com/2025/10/welcome-to-android-xr-spotlight-week.html)*, where we provide resources—blog posts, videos, sample code, and more—all designed to help you learn, build, and prepare your apps for Android XR.*

This week, [Samsung launched Galaxy XR](https://blog.google/products/android/samsung-galaxy-xr), built in collaboration with Google and Qualcomm. This is an exciting time for developers, and we wanted to help you get the best performance you can out of your XR app.

While poor performance in games and apps on non-XR devices can be frustrating for the user, in the world of XR performance isn’t just optional, it’s fundamental to the success of your app. If you miss your frame rate target in XR, it can cause far more serious problems like motion sickness.

In this guide, we'll walk you through the essential performance optimizations you need to understand for Android XR development. You'll learn which features deliver the biggest performance gains, when to use them, and how they work together to help you hit your frame rate targets.

Here’s what we’re aiming for:

* **Minimum:** 72fps (part of our play quality guidelines)
* **Optional:** 90fps with an 11ms budget per frame

For more information on why it's important to maintain such a high frame-rate check out our [performance guidelines](/develop/xr/unity/performance).

## XR-Specific Performance Features

We’re going to start by covering two XR-specific performance features: Foveated Rendering and Vulkan Subsampling.

### Foveated Rendering

Foveated rendering is an optimization that has two modes. The first is a **static mode** that renders the center of the screen at a higher resolution, and progressively lowers the resolution the further out you look.

The second is the **eye-tracking mode** that specifically renders the area where you're looking in full detail, while reducing the quality displayed in your peripherals. It essentially mimics how human vision works — where we only see fine detail in the specific area we’re focusing on.

Foveated rendering significantly cuts the GPU workload without sacrificing the perceived image quality for the user. The beauty of foveated rendering is that users won't notice the reduced quality in their peripheral vision, but your GPU will certainly notice the improved performance.

Imagine you're building a museum experience with intricate 3D artifacts. Without foveated rendering, you’d struggle to maintain 90fps trying to render everything in ‘field of view’. With foveated rendering, you can keep those high-poly details where the user’s looking, but the background environment renders at a lower quality. Your users won't notice the difference, but you'll have the headroom to add more detail to your scene.

### Vulkan Subsampling

Vulkan Subsampling is foveated rendering's best friend. While foveated rendering decides what to render at different quality levels, **Vulkan Subsampling handles how to efficiently render the different quality levels** using Fragment Density Maps.

When combined with foveated rendering, Vulkan Subsampling gives you an extra 0.5ms of performance. It also helps smooth out jagged edges in your peripheral vision, making the overall image look cleaner.

For example, in a flight simulator game where users focus on instruments and controls, combining foveated rendering with Vulkan Subsampling means the detailed controls render sharply, but the peripheral cockpit structure uses fewer resources. That extra 0.5ms doesn’t sound like much, but it's the difference between having room for an extra interactive element or dropping frames during intense moments.

## GPU Features for Complex Scenes

Besides Foveated Rendering and Vulkan Subsampling, there are some GPU features that reduce unnecessary strain through smart instancing and culling. These are particularly effective for complex scenes with repeated geometry or significant occlusion.

### GPU Resident Drawer

The [GPU Resident Drawer](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@17.0/manual/gpu-resident-drawer.html) automatically uses GPU instancing to reduce draw calls and free up CPU processing time. So, instead of the CPU telling the GPU about each object individually, the GPU batches similar objects together.

This feature is most effective for large scenes with repeated meshes, like trees in a forest, furniture in an office building, or props scattered throughout an environment.

Picture a forest scene with 200 trees using the same base mesh. Without the GPU Resident Drawer, you’ve got 200 draw calls eating up the GPU, therefore freeing up the CPU. When you enable this feature, the GPU will intelligently instance those trees, which should reduce it to just 5-10 draw calls. That's a massive GPU savings you can then invest in gameplay logic or physics calculations.

### GPU Occlusion Culling

[GPU Occlusion Culling](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@17.0/manual/gpu-culling.html) uses the *GPU* instead of the *CPU* to identify and skip rendering hidden objects. It automatically detects what's occluded (hidden) behind other objects, so you're not wasting your GPU on things the user can't see.

This feature is particularly powerful in interior spaces with multiple rooms, dense environments, or architectural scenes where walls, floors, and objects naturally block the view.

As an example, let’s say you're building a multi-room house experience. When the user is in the living room, why waste GPU cycles rendering the fully detailed kitchen that's completely hidden behind a wall? GPU Occlusion Culling automatically skips rendering those hidden objects, giving you more performance budget for what's actually visible.

## Monitoring Your Performance

It’s not enough to just use these features. You also need to measure your optimizations, so you can quantify their impact and verify your changes are actually working.

### Performance Metrics API

The [Performance Metrics API](https://docs.unity3d.com/Packages/com.unity.xr.androidxr-openxr@0.4/manual/features/performance-metrics.html) provides real-time monitoring of your apps memory usage, CPU performance, and GPU performance. It gives you comprehensive data from compositor and runtime layers, so you can see exactly what's happening in your application.

Establish a baseline before making your changes, apply an optimization, measure the impact, and iterate. This data-driven approach means you *know* you’re actually improving performance rather than guessing.

Before enabling foveated rendering, your GPU frame time might be 13ms, which is over your 11ms budget. Enable foveated rendering, measure again, and hopefully you see it drop to 9ms. That's 4ms of headroom you've gained to add more detail to your scene, improve visual quality elsewhere, or simply ensure smoother performance across a wider range of content.

Without these metrics, you're optimizing blind. The Performance Metrics API tells you the truth about what's actually helping your specific use case.

### Frame Debugger

The [Frame Debugger](https://docs.unity3d.com/6000.2/Documentation/Manual/FrameDebugger.html) is Unity's built-in tool for understanding exactly how your scene is being rendered, frame by frame. It shows you the sequence of draw calls and lets you step through them to verify your optimizations are working correctly.

Want to confirm the SRP Batcher is working? Look for 'RenderLoopNewBatcher' entries in the Frame Debugger. Checking if the GPU Resident Drawer is batching properly? Look for 'Hybrid Batch Group' entries. These visual confirmations help you understand whether your optimization settings are actually taking effect.

Step through the first 50 draw calls of your scene. If you see similar objects being drawn individually instead of batched, that's telling you that your instancing or batching isn't working correctly. The Frame Debugger makes these issues immediately visible so you can address them.

## Additional Optimizations

As well as the optimizations we’ve covered above, our full performance guide also covers a few other additional optimizations. Here’s a quick summary:

* **URP Settings:** Disable HDR and Post Processing for mobile XR. These features provide minimal visual impact compared to their performance cost on mobile hardware, so you'll get measurable performance gains with barely perceptible visual differences.
* **SRP Batcher:** Reduces CPU overhead for scenes with many materials using the same shader variant. By minimizing render-state changes between draw calls, you can significantly reduce CPU time spent on rendering.
* **Display Refresh Rate:** Dynamically adjust between 72fps and 90fps based on scene complexity. Lower the frame rate during complex sequences to maintain stability, then increase it during simpler moments for ultra-smooth interaction.
* **Depth/Opaque Textures:** Disable these unless specifically needed for shader effects. They cause unnecessary GPU copying operations that waste performance without providing benefit for most applications.
* **URP Render Scale:** This setting allows you to render at a reduced resolution for performance benefits or to upscale rendering for enhanced visual quality.

For step-by-step instructions on these and more optimizations, check our complete Unity Performance Guide for Android XR.

## Conclusion

The performance of your XR app isn't just a technical checkbox. It's the difference between a comfortable, engaging experience and one that makes users feel sick or uncomfortable. The optimizations we've covered are your toolkit for hitting those critical framerate targets on the newest XR devices.

Here's your roadmap:

1. Start with Foveated Rendering and Vulkan Subsampling. These XR-specific features deliver immediate and noticeable GPU savings.
2. Add GPU Resident Drawer and Occlusion Culling if you have complex scenes with repeated geometry or interior spaces.
3. Monitor everything with the Performance Metrics API to ensure your changes are actually helping
4. Explore additional URP optimizations for extra performance headroom

It’s vital to measure continuously and iterate. Not every optimization will benefit every project equally, so use the Performance Metrics API to get a clear idea of what actually helps your specific use case.

## What's next: expanding your skills

Ready to dive deeper? Check out these resources:

* **Unity Performance Guide for Android XR** - Complete step-by-step implementation instructions for all features covered [here](/develop/xr/unity/performance).
* **Getting Started with Unity and Android XR** - Set up your development environment and [start building](https://android.devsite.corp.google.com/develop/xr/unity).
* **Android XR Developer Documentation** - Comprehensive guides for all Android XR [features](https://android.devsite.corp.google.com/develop/xr/get-started)

###### Written by:

* ## [Luke Hopkins](/blog/authors/luke-hopkins)

  ###### Developer Relations Engineer

  [read\_more
  View profile](/blog/authors/luke-hopkins)

  ![](/static/blog/assets/Luke_Hopkins_9c1e15d778_Z2o9b3q.webp)

  ![](/static/blog/assets/Luke_Hopkins_9c1e15d778_Z2o9b3q.webp)

## Continue reading

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