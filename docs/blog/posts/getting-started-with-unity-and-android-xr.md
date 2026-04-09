---
title: Getting started with Unity and Android XR  |  Android Developers' Blog
url: https://developer.android.com/blog/posts/getting-started-with-unity-and-android-xr
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Android Developers' Blog](https://developer.android.com/)
* [Blog](https://developer.android.com/blog)

Stay organized with collections

Save and categorize content based on your preferences.



#### [How-tos](/blog/categories/how-tos)

# Getting started with Unity and Android XR

###### 6-min read

![](/static/blog/assets/xr_Week3_984ec91c60_mkqpQ.webp)

23

Oct
2025

[![](/static/blog/assets/Luke_Hopkins_9c1e15d778_Z2o9b3q.webp)](/blog/authors/luke-hopkins)

[##### Luke Hopkins](/blog/authors/luke-hopkins)

###### Developer Relations Engineer, Android

[*Samsung Galaxy XR is here*](https://android-developers.googleblog.com/2025/10/giving-your-apps-new-home-on-samsung.html)*, powered by Android XR! This blog post is part of our* [*Android XR Spotlight Week*](https://android-developers.googleblog.com/2025/10/welcome-to-android-xr-spotlight-week.html)*, where we provide resources—blog posts, videos, sample code, and more—all designed to help you learn, build, and prepare your apps for Android XR.*

There’s never been a better time to get into XR development. Last December, we announced [Android XR](https://blog.google/products/android/android-xr/), Google's new Android platform built on open standards such as OpenXR and Vulkan, which makes XR development more accessible than it’s ever been.

And when combined with [Unity](https://unity.com/)’s existing XR tools, you get a powerful and mature development stack. This makes it possible to create and deploy XR apps that work across multiple devices.

![openxr_face_tracking2.webp](/static/blog/assets/openxr_face_tracking2_d1bed7ef87_2snsjU.webp)

No matter whether you’ve done XR development before or not, we want to help you get started.  
  
This blog will get you up and running with Android XR and Unity development. We’ll focus on the practical steps to configure your environment, understand the package ecosystem, and start building.  
  
By the end of this blog, you’ll have a good understanding of:

* The package ecosystem
* Essential setup steps
* Input methods
* Privacy and permissions
* Composition layers

## Unity for Android XR development

You might choose Unity for its cross-platform compatibility, allowing you to build once and deploy to Android XR and other XR devices.  
  
When using Unity, you benefit from its mature XR ecosystem and tooling. It already has established packages such as [XR Interaction Toolkit](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.0/manual/index.html), [OpenXR plugin](https://docs.unity3d.com/Packages/com.unity.xr.openxr@1.15/manual/index.html), [XR composition layers](https://docs.unity3d.com/Packages/com.unity.xr.compositionlayers@0.5/manual/usage-guide.html), [XR Hands](https://docs.unity3d.com/Packages/com.unity.xr.hands@1.7/manual/index.html), an extensive asset store full of XR-ready components and templates, and XR simulation and testing tools. And since Unity 6 was released last November, you’ll also benefit from its improved [Universal Render Pipeline (URP)](https://unity.com/features/srp/universal-render-pipeline) performance, better Vulkan graphics support, and enhanced build profiles.

Here are some sample projects to get an idea of what can be done:

* [Unity’s VR Project Template](https://docs.unity3d.com/Packages/com.unity.template.vr@9.2/manual/index.html)
* [VR Multiplayer Template](https://docs.unity3d.com/Packages/com.unity.template.vr-multiplayer@2.0/manual/index.html)
* [Android XR Samples for Unity](https://github.com/android/xr-unity-samples)

## Essential setup: your development foundation

### Unity 6 requirements and installation

You’ll need Unity 6 to create your app, as earlier versions don’t support Android XR. Install Unity Hub first, then Unity 6 with the Android Build Support module, following [these steps](/develop/xr/unity/setup).

![unity6.png](/static/blog/assets/unity6_a0ea079402_1UkljO.webp)

### Android XR build profiles: simplifying configuration

Unity build profiles are project assets that store your platform-specific settings and configurations. So instead of needing to manually set up 15-20 different settings across multiple menus, you can use a build profile to do this automatically.  
You can create your own build profiles, but for now we recommend using the dedicated Android XR build profile we created.

*You can select your build profile by selecting File > Build Profile from your Unity project. For full instructions, see the*[*Develop for Android XR*](https://docs.unity3d.com/6000.1/Documentation/Manual/xr-android-xr-develop.html) *workflow page.*

If you make any changes of your own, you can then create a new build profile to share with your team. This way you ensure consistent build experience across the board.

![buildprofiles.png](/static/blog/assets/buildprofiles_c607c069d3_kya9A.webp)

After these steps you can build and run your APK for Android XR devices.

### Graphics API: why Vulkan matters

Once you have your Unity project set up with an Android XR build profile, we first recommend making sure you have Vulkan set as your graphics API. Android XR is built as a Vulkan-first platform. In March 2025, Google announced that [Vulkan is now the official graphics API for Android](https://android-developers.googleblog.com/2025/03/building-excellent-games-with-better-graphics-and-performance.html). It’s a modern, low-level graphics API that helps developers maximize the performance of modern GPUs and unlocks advanced features like ray-tracing and multithreading for realistic and immersive gaming visuals.

These standards provide the best compatibility for your existing applications and ease the issues and costs of porting. And it makes it possible to enable advanced Android XR features such as [URP Application Space Warp](https://docs.unity3d.com/6000.3/Documentation/Manual/xr-graphics-spacewarp.html) and [foveated rendering](https://docs.unity3d.com/6000.2/Documentation/Manual/xr-foveated-rendering.html).

Unity 6 handles Vulkan automatically, so when you use the Android XR build profile, Unity will configure Vulkan as your graphics API. This ensures you get access to all the advanced Android XR features without any manual configuration.

*You can verify your graphics API settings by going to ‘Edit’ >’ Project Settings’ > ‘Player’ > ‘Android tab’ > ‘Other settings’ > ‘Graphics APIs’.*

![](/static/blog/assets/Z2bfYdm_274uYx.webp)
![appentrypoint.png](/static/blog/assets/appentrypoint_fb4df59e49_Z1aJDtB.webp)

### Understanding the package ecosystem

There are two different packages you can use for Android XR in Unity. One is by using the Android XR Extensions for Unity, and the other is using the Unity OpenXR: Android XR package.

***These may sound like the same thing, but bear with me***.

The [Unity OpenXR: Android XR](https://docs.unity3d.com/Packages/com.unity.xr.androidxr-openxr@1.0/manual/index.html) package is the official Unity package for Android XR support. It provides the majority of Android XR features, made available through OpenXR standards. It also enables [AR Foundation](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.2/manual/index.html) integration for mixed reality features. The primary benefit of using the Unity OpenXR: Android XR package is that it offers a unified API for supporting XR devices.

Whereas the [Android XR Extensions for Unity](https://github.com/android/android-xr-unity-package) is Google’s XR package, designed specifically for developing for Android XR devices. It supplements the Unity OpenXR package with additional features such as environment blend modes, scene meshing, image tracking, and body tracking. The tradeoff is that you can only develop for Android XR devices.

Which one you choose will depend on your specific needs, but we generally recommend going with the Unity OpenXR: Android XR, as it gives you far more flexibility for the devices your app will be compatible with, and then based on your application requirements you can then add Android XR Extensions for Unity.

### How to install packages

To add a new package, with your project open in Unity, select ‘Window’ > ‘Package Management’ > ‘Package Manager’.

From here you can install these packages from the ‘Unity Registry’ tab:

* ‘[Open XR: Android XR](https://docs.unity3d.com/Packages/com.unity.xr.androidxr-openxr@1.0/manual/index.html)’
* ‘[XR Interaction Toolkit](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.2/manual/index.html)’
* ‘[XR Hands](https://docs.unity3d.com/Packages/com.unity.xr.hands@1.6/manual/index.html)’

![packagemanager.png](/static/blog/assets/packagemanager_6e226e5295_OafUg.webp)

You can install the Android XR for unity package via Github by selecting the ➕ icon, selecting ‘Install package from git URL’, then entering ‘https://github.com/android/android-xr-unity-package.git’

![packagemanager2.png](/static/blog/assets/packagemanager2_a246c33bc1_ZUlTpI.webp)

## Required OpenXR features

Now you have the packages you need installed, let’s enable some core features in order to get our project working.

You can enable OpenXR setting for Android: *‘Edit’ -> ‘Project Settings’ -> ‘XR Plugin Management’ -> Click the Android and enable OpenXR*

![xrpluginmgmt.png](/static/blog/assets/xrpluginmgmt_eb1c0ead10_ZViJFq.webp)

Next we need to enable support for: ‘Android XR support’, we will cover other OpenXR features as we need them. For now we just need Android XR support to be enabled.

## Input

Android XR supports input for Hands, Voice, Eye tracking, Keyboard and Controllers. We recommend installing the [XR Interaction Toolkit](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.0/manual/index.html) and [XR Hands](https://docs.unity3d.com/Packages/com.unity.xr.hands@1.6/manual/index.html) as these contain the best prefabs for getting started. By using these prefabs, you’ll have everything you need to support Hands and Controllers in your app.

![xrinteractiontoolkit.png](/static/blog/assets/xrinteractiontoolkit_2a499ad14f_Zrb9Op.webp)

Once the XR Hands and XR Interactive toolkit are both installed, I recommend importing the Starter Assets and [Hands Interaction Demo](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@2.5/manual/samples-hands-interaction-demo.html). Then you need to enable the [Hand Interaction](https://docs.unity3d.com/Packages/com.unity.xr.openxr@1.8/manual/features/handinteractionprofile.html) and [Khronos Simple Controller](https://docs.unity3d.com/Packages/com.unity.xr.openxr@1.1/manual/features/khrsimplecontrollerprofile.html) profiles, and turn on the Hand Tracking Subsystem and Meta Hand Tracking Aim features.

You can edit these settings by going to *‘Edit’ > ‘Project Settings’ > XR Plug-in Management’ > ‘OpenXR’*

![profiles.png](/static/blog/assets/profiles_966997c02a_Z1DdhS7.webp)

We’d also recommend Unity’s prefab, [XR Origin](https://docs.unity3d.com/6000.2/Documentation/Manual/xr-origin.html), that represents the user's position and orientation in XR space. This contains the camera rig and tracking components needed to render your XR experience from the correct viewpoint.

The simplest way to add this prefab is to import it from the hands integration demo we imported earlier which can be found here *‘Hands Integration Toolkit’ > ’Hand Interaction’ > ’Prefabs’ > ’XR Origin’*

![prefabs.png](/static/blog/assets/prefabs_d7826eadd0_2hDE0k.webp)

I recommend using this Prefab over the ‘XR Origin’ option in your game objects as it uses the [XR Input Modality Manager](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@2.4/manual/xr-input-modality-manager.html) which automatically switches between users hands and controllers. This will give you the best success for switching between hands and controllers.

## Privacy and permissions: building user trust

Whatever you build, you’ll need to capture [runtime permissions](/guide/topics/permissions/overview) from the users. That’s because scene understanding, eye tracking, face tracking and hand tracking provide access to data that may be more sensitive to the user.

These capabilities provide deeper personal information than traditional desktop or mobile apps, so the runtime permissions ensure your users have full control over what data they choose to share. So, to keep with Android's security and privacy policies, Android XR has permissions for each of these features.  
  
For example, if you use the XR Hands package for custom hand gestures, you will need to request the [hand tracking permission](https://docs.unity3d.com/Packages/com.unity.xr.androidxr-openxr@0.4/manual/features/hand-tracking.html#permissions) (see below) as this package needs to track a lot of information about the user's hands. This includes things like tracking hand joint poses and angular and linear velocities;

**Note: For a full list of extensions that require permissions, check out information on the** [**XR developer website**](/develop/xr/get-started#understand-permissions)**.**

```
  const string k_Permission = "android.permission.HAND_TRACKING";

#if UNITY_ANDROID
void Start()
{
    if (!Permission.HasUserAuthorizedPermission(k_Permission))
    {
        var callbacks = new PermissionCallbacks();
        callbacks.PermissionDenied += OnPermissionDenied;
        callbacks.PermissionGranted += OnPermissionGranted;
        
        Permission.RequestUserPermission(k_Permission, callbacks);
    }
}

void OnPermissionDenied(string permission)
{
    // handle denied permission
}


void OnPermissionGranted(string permission)
{
    // handle granted permission
}

#endif // UNITY_ANDROID
```

### Enhancing visual quality with composition layers

A [Composition Layer](https://docs.unity3d.com/Packages/com.unity.xr.compositionlayers@0.6/manual/index.html) is the recommended way to render UI elements. They make it possible to display elements at a much higher quality compared to Unity’s standard rendering pipeline as everything is directly rendered to the platform's compositor.

For example, if you’re displaying text, the standard Unity rendering is more likely to have blurry text, soft edges, and visual artifacts. Whereas with composition layers, the text will be clearer, the outlines will be sharper, and the experience will be better overall.

As well as text, it also renders video, images, and UI elements at a much higher quality. It does this by utilising native support for the runtime’s compositor layers.

*To turn on Composition Layers, open Package Manager, select ‘Unity Register’, then install ‘XR Composition Layers’.*

## Build and Run

Now that you have your OpenXR packages installed and features enabled, a prefab setup for hand and head movement you can now build your scene and deploy directly to your headset for testing.

### What's next: expanding your skills

Now that you've got your Android XR development environment set up and understand the key concepts, here are the next steps to continue your XR development journey:

**Essential resources for continued learning:**

* [Android XR developer documentation](/develop/xr) - comprehensive guides for all Android XR features
* [Unity XR development manual](https://docs.unity3d.com/Manual/XR.html) - Unity's official XR development resources

**Sample projects to explore:**

* [Android XR Unity samples](https://github.com/android/xr-unity-samples) - Google's official sample projects showcasing different Android XR features
* [Unity XR Interaction Toolkit examples](https://github.com/Unity-Technologies/XR-Interaction-Toolkit-Examples) - comprehensive examples of XR interactions and gameplay mechanics
* [Unity VR Template](https://docs.unity3d.com/Packages/com.unity.template.vr@9.2/manual/index.html) - a complete starting point for VR projects
* [VR Multiplayer Template](https://docs.unity3d.com/Packages/com.unity.template.vr-multiplayer@2.0/manual/index.html) - explore social XR experiences

###### Written by:

* ## [Luke Hopkins](/blog/authors/luke-hopkins)

  ###### Developer Relations Engineer

  [read\_more
  View profile](/blog/authors/luke-hopkins)

  ![](/static/blog/assets/Luke_Hopkins_9c1e15d778_Z2o9b3q.webp)

  ![](/static/blog/assets/Luke_Hopkins_9c1e15d778_Z2o9b3q.webp)

## Continue reading

* [![](/static/blog/assets/Alice_Yuan_552a4dd4ee_ZlDEgJ.webp)](/blog/authors/alice-yuan)

  04

  Mar
  2026

  04

  Mar
  2026

  ![](/static/blog/assets/battery_Performance_08d6713f94_Z1IAO0P.webp)

  #### [How-tos](/blog/categories/how-tos)

  ## [Battery Technical Quality Enforcement is Here: How to Optimize Common Wake Lock Use Cases](/blog/posts/battery-technical-quality-enforcement-is-here-how-to-optimize-common-wake-lock-use-cases)

  [arrow\_forward](/blog/posts/battery-technical-quality-enforcement-is-here-how-to-optimize-common-wake-lock-use-cases)

  In recognition that excessive battery drain is top of mind for Android users, Google has been taking significant steps to help developers build more power-efficient apps.

  ###### [Alice Yuan](/blog/authors/alice-yuan) • 8 min read
* [![](/static/blog/assets/thomas_ezan_d29c7508d0_l9O72.webp)](/blog/authors/thomas-ezan)[![](/static/blog/assets/Ivy_Knight_3071ce592d_2j4ER1.webp)](/blog/authors/ivy-knight)

  02

  Dec
  2025

  02

  Dec
  2025

  ![](/static/blog/assets/sample_readme_bazel_9348d9f325_Z57CJe.webp)

  #### [How-tos](/blog/categories/how-tos)

  ## [Explore AI on Android with Our Sample Catalog App](/blog/posts/explore-ai-on-android-with-our-sample-catalog-app)

  [arrow\_forward](/blog/posts/explore-ai-on-android-with-our-sample-catalog-app)

  We wanted to provide you with examples of AI-enabled features using both on-device and Cloud models and inspire you to create delightful experiences for your users.

  ###### [Thomas Ezan](/blog/authors/thomas-ezan), [Ivy Knight](/blog/authors/ivy-knight) • 2 min read
* [![](/static/blog/assets/Alice_Yuan_552a4dd4ee_ZlDEgJ.webp)](/blog/authors/alice-yuan)

  20

  Nov
  2025

  20

  Nov
  2025

  ![](/static/blog/assets/performance_Week8_4d6efcacbe_ZI6a5e.webp)

  #### [How-tos](/blog/categories/how-tos)

  ## [Leveling Guide for your Performance Journey](/blog/posts/leveling-guide-for-your-performance-journey)

  [arrow\_forward](/blog/posts/leveling-guide-for-your-performance-journey)

  The performance leveling guide features 5 levels. We'll start with level 1, which introduces minimal adoption effort performance tooling, and we'll go up to level 5, ideal for apps that have the resourcing to maintain a bespoke performance framework.

  ###### [Alice Yuan](/blog/authors/alice-yuan) • 9 min read

# Stay in the loop

Get the latest Android development insights delivered to your inbox
weekly.

[mail
Subscribe](/subscribe)

![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)