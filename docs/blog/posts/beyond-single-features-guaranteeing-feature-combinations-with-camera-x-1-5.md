---
title: https://developer.android.com/blog/posts/beyond-single-features-guaranteeing-feature-combinations-with-camera-x-1-5
url: https://developer.android.com/blog/posts/beyond-single-features-guaranteeing-feature-combinations-with-camera-x-1-5
source: md.txt
---

#### [Product News](https://developer.android.com/blog/categories/product-news)

# Beyond Single Features: Guaranteeing Feature Combinations With CameraX 1.5

###### 6-min read

![](https://developer.android.com/static/blog/assets/25_Android_Camera_X_Feature_blog_1_856fb165e3_Z3rLg4.webp) 15 Oct 2025 [![](https://developer.android.com/static/blog/assets/Tahsin_a6df1d8c3c_1WrW45.webp)](https://developer.android.com/blog/authors/tahsin-masrur) [##### Tahsin Masrur](https://developer.android.com/blog/authors/tahsin-masrur)

###### Software Engineer

Modern camera apps are defined by powerful, overlapping features. Users expect to record video with stunning HDR, capture fluid motion at 60 FPS, and get buttery-smooth footage with Preview Stabilization---often all at the same time.

As developers, we know the reality is more complicated. How can you guarantee that a specific device actually supports a given combination? Until now, enabling multiple features was often a gamble. You could check for individual feature support, but combining them could lead to undefined behavior or, worse, a failed camera session. This uncertainty forces developers to be conservative, which prevents users on capable devices from accessing the best possible experience.

For instance, very few premium devices reliably support HDR and 60 FPS video simultaneously. Consequently, most apps avoid enabling both at once to prevent a poor user experience on the majority of phones.

To address this, we're introducing **Feature Group in CameraX** - a new API designed to eliminate this guesswork. You can now query whether a specific combination of features is supported *before* configuring the camera, or simply tell CameraX your priorities and let it enable the best-supported combination for you.

## For Those New to CameraX

Before we dive into the new Feature Group API, let's quickly recap what CameraX is. CameraX is a Jetpack support library, built to help you make camera app development easier. It provides a consistent and easy-to-use API surface that works across most Android devices, with backward-compatibility to Android 6.0 (API level 23). If you are new to CameraX, we recommend checking out the [official documentation](https://developer.android.com/media/camera/camerax) and trying the [codelab](https://developer.android.com/codelabs/camerax-getting-started#0) to get started.

## What You Can Build with the Feature Group API

You no longer need to gamble on feature combinations and can confidently deliver the best possible camera experiences -- like simultaneous HDR and 60 FPS video on capable hardware (e.g. a Pixel 10 Pro) -- while gracefully avoiding errors on devices that can't support the combination.
![unnamed.png](https://developer.android.com/static/blog/assets/unnamed_36b4e63acd_Z15qxE2.webp)

*Pixel 10 Pro enabling both HDR and 60 FPS simultaneously*
![unnamed (1).png](https://developer.android.com/static/blog/assets/unnamed_1_f0d1910035_ZaydsF.webp)

*On an older device where HDR and 60 FPS can't run simultaneously, only HDR is enabled while the 60 FPS option is disabled.*

With the Feature Group API, you can:

- **Build smarter, dynamic UIs:** Intelligently enable or disable settings in your UI based on real-time hardware support. For example, if a user enables HDR, you can instantly gray out and disable the 60 FPS option if the combination isn't supported on that device.

![unsupported-features-disabled.gif](https://developer.android.com/static/blog/assets/unsupported_features_disabled_f52700ed3a_lIAlh.webp)

- **Deliver a reliable "High-Quality" mode:**Configure the camera with a prioritized list of desired features. CameraX automatically finds and enables the best-supported combination for any given device, ensuring a great result without complex, device-specific logic.
- **Prevent camera session failures:** By verifying support beforehand, you prevent the camera from attempting to configure an unsupported combination, eliminating a common source of crashes and offering a smooth user experience.

## How It Works: The Core Components

The new API is centered around key additions to [SessionConfig](https://developer.android.com/reference/androidx/camera/core/SessionConfig) and [CameraInfo](https://developer.android.com/reference/androidx/camera/core/CameraInfo).

1. [**GroupableFeature**](https://developer.android.com/reference/androidx/camera/core/featuregroup/GroupableFeature): This API introduces a set of predefined groupable features, such as [HDR_HLG10](https://developer.android.com/reference/androidx/camera/core/featuregroup/GroupableFeature#HDR_HLG10()), [FPS_60](https://developer.android.com/reference/androidx/camera/core/featuregroup/GroupableFeature#FPS_60()), [PREVIEW_STABILIZATION](https://developer.android.com/reference/androidx/camera/core/featuregroup/GroupableFeature#PREVIEW_STABILIZATION()), and [IMAGE_ULTRA_HDR](https://developer.android.com/reference/androidx/camera/core/featuregroup/GroupableFeature#IMAGE_ULTRA_HDR()). Due to computational limitations, only a specific set of features can be grouped with the high degree of reliability this API provides. We are actively working to expand this list and will introduce support for more features in future releases.  
2. **New** [**SessionConfig**](https://developer.android.com/reference/androidx/camera/core/SessionConfig)**Parameters:** This class, used for starting a camera session, now accepts two new parameters:
   - `requiredFeatureGroup`: Use this for features that **must** be supported for the configuration to succeed - ideal for features that a user explicitly enables, such as toggling an 'HDR' switch. To ensure a deterministic and consistent experience, the `bindToLifecycle` call will throw an `IllegalArgumentException` if the requested combination is not supported, rather than silently ignoring a feature request. The `CameraInfo#isFeatureGroupSupported` API (details below) should be used to query this result beforehand.
   - `preferredFeatureGroup`: Use this for features that are desirable but optional, for example when you want to implement a default "High-Quality" mode. You provide a list of your desired features **ordered according to your priorities**, and CameraX automatically enables the highest-priority combination that the device supports.
3. [**CameraInfo#isFeatureGroupSupported()**](https://developer.android.com/reference/androidx/camera/core/CameraInfo#isFeatureGroupSupported(androidx.camera.core.SessionConfig)): This is the core query method for explicitly checking if a feature group is supported, well-suited for providing only supported feature options to users in your app UI. You pass it a `SessionConfig`, and it returns a boolean indicating whether the combination is supported. If you intend to bind a `SessionConfig` with required features, you should use this API first to ensure it is supported.

## Implementation in Practice

Let's look at how to use these components to build a better camera experience.

### Scenario 1: "Best Effort" High-Quality Mode

If you want to enable the best possible features by default, you can provide a prioritized list to `preferredFeatureGroup`. In this example, we tell CameraX to prioritize HDR, then 60 FPS, and finally Preview Stabilization. CameraX handles the complexity of checking all possible combinations and choosing the best one that the device supports.

For instance, if a device can handle HDR and 60 FPS together but not with Preview Stabilization, CameraX will enable the first two and discard the third. This way, you get the best possible experience without writing complex, device-specific checks.

```
  cameraProvider.bindToLifecycle(

    lifecycleOwner,

    cameraSelector,

    SessionConfig(

        useCases = listOf(preview, videoCapture),

        // The order of features in this list determines their priority. 

        // CameraX will enable the best-supported combination based on these

        // priorities: HDR_HLG10 > FPS_60 > Preview Stabilization.  

        preferredFeatureGroup =

           listOf(HDR_HLG10, FPS_60, PREVIEW_STABILIZATION),

    ).apply {

        // (Optional) Get a callback with the enabled features

        // to update your UI. 

        setFeatureSelectionListener { selectedFeatures ->

            updateUiIndicators(selectedFeatures)

        }

    }

)
```

For this code snippet, CameraX will attempt to enable feature combinations in the following priority order, selecting the first one the device fully supports:

1. HDR + 60 FPS + Preview Stabilization
2. HDR + 60 FPS
3. HDR + Preview Stabilization
4. HDR
5. 60 FPS + Preview Stabilization
6. 60 FPS
7. Preview Stabilization
8. None of the above features

### Scenario 2: Building a Reactive UI

To create a UI that responds to user selections and prevents users from selecting an unsupported feature combination, you can query for support directly. The function below checks which features are incompatible with the user's *current* selections, allowing you to disable the corresponding UI elements.

```
  /**

 * Returns a list of features that are NOT supported in combination

 * with the currently selected features.

 */

fun getUnsupportedFeatures(

    currentFeatures: Set<GroupableFeature>

): Set<GroupableFeature> {

    val unsupportedFeatures = mutableSetOf<GroupableFeature>()

    val appFeatureOptions = setOf(HDR_HLG10, FPS_60, PREVIEW_STABILIZATION)


    // Iterate over every available feature option in your app. 

    appFeatureOptions.forEach { featureOption ->

        // Skip features the user has already selected. 

        if (currentFeatures.contains(featureOption)) return@forEach


        // Check if adding this new feature is supported. 

        val isSupported = cameraInfo.isFeatureGroupSupported(

            SessionConfig(

                useCases = useCases,

                // Check the new feature on top of existing ones.

                requiredFeatureGroup = currentFeatures + featureOption

            )

        )


        if (!isSupported) {

            unsupportedFeatures.add(featureOption)

        }

    }


    return unsupportedFeatures

}
```

You can then wire this logic into your ViewModel or UI controller to react to user input and re-bind the camera with a guaranteed-to-work configuration.

```
  // Invoked when user turns some feature on/off.

fun onFeatureChange(currentFeatures: Set<GroupableFeature>) {

    // Identify features that are unsupported with the current selection.

    val unsupportedFeatures = getUnsupportedFeatures(currentFeatures)



    // Update app UI so that users can't enable them.

    updateDisabledFeatures(unsupportedFeatures)



    // Since the UI now only allows selecting supported feature combinations, 

    // `currentFeatures` is always valid. This allows setting

    // `requiredFeatureGroup` directly, without needing to re-check for

    // support or set a feature selection listener.  

    cameraProvider.bindToLifecycle(

        lifecycleOwner,

        cameraSelector,

        SessionConfig(

            useCases = listOf(preview, videoCapture),

            requiredFeatureGroup = currentFeatures,

        )

    )

}
```

To see these concepts in a working application, you can explore [our internal test app](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:camera/integration-tests/featurecombotestapp/src/main/java/androidx/camera/integration/featurecombo/;drc=16d6cbf8fb302abd57e45ce528ff0ae4903e6dcb). It provides a complete implementation of both the "best effort" and "reactive UI" scenarios discussed above.

Please note: This is a test application and not an officially supported sample. While it's a great reference for the Feature Group API, it has not been polished for production use.

## Get Started Today

The Feature Group API removes the ambiguity of working with advanced camera capabilities. By providing a deterministic way to query for feature support, you can build more powerful and reliable camera apps with confidence.

The API is available as experimental in CameraX 1.5 and is scheduled to become fully stable in the 1.6 release, with more support and improvements on the way.

To learn more, check out the official documentation. We can't wait to see what you create, and we look forward to your feedback. Please share your thoughts and report any issues through the following channels:

- [CameraX developers discussion group](https://groups.google.com/a/android.com/g/camerax-developers)
- [File a bug here](https://issuetracker.google.com/issues/new?component=618491)

###### Written by:

-

  ## [Tahsin Masrur](https://developer.android.com/blog/authors/tahsin-masrur)

  ###### Software Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/tahsin-masrur) ![](https://developer.android.com/static/blog/assets/Tahsin_a6df1d8c3c_1WrW45.webp) ![](https://developer.android.com/static/blog/assets/Tahsin_a6df1d8c3c_1WrW45.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/matthew_warner_67a99317e4_Z2c1VNu.webp)](https://developer.android.com/blog/authors/matthew-warner) 02 Apr 2026 02 Apr 2026 ![](https://developer.android.com/static/blog/assets/android_studio_gemma4_73370772af_2lUopR.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android Studio supports Gemma 4: our most capable local model for agentic coding](https://developer.android.com/blog/posts/android-studio-supports-gemma-4-our-most-capable-local-model-for-agentic-coding)

  [arrow_forward](https://developer.android.com/blog/posts/android-studio-supports-gemma-4-our-most-capable-local-model-for-agentic-coding) Every developer's AI workflow and needs are unique, and it's important to be able to choose how AI helps your development. In January, we introduced the ability to choose any local or remote AI model to power AI functionality in Android Studio

  ###### [Matthew Warner](https://developer.android.com/blog/authors/matthew-warner) •
  2 min read

  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)
- [![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)](https://developer.android.com/blog/authors/matt-dyor) 02 Apr 2026 02 Apr 2026 ![](https://developer.android.com/static/blog/assets/as_Panda3_385cde5eac_Z1E8IhJ.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Increase Guidance and Control over Agent Mode with Android Studio Panda 3](https://developer.android.com/blog/posts/increase-guidance-and-control-over-agent-mode-with-android-studio-panda-3)

  [arrow_forward](https://developer.android.com/blog/posts/increase-guidance-and-control-over-agent-mode-with-android-studio-panda-3) Android Studio Panda 3 is now stable and ready for you to use in production. This release gives you even more control and customization over your AI-powered workflows, making it easier than ever to build high-quality Android apps.

  ###### [Matt Dyor](https://developer.android.com/blog/authors/matt-dyor) •
  3 min read

  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)
- [![](https://developer.android.com/static/blog/assets/Caren_Chang_e58d793559_1i40VV.webp)](https://developer.android.com/blog/authors/caren-chang)[![](https://developer.android.com/static/blog/assets/David_Chou_226df78370_tqGIk.webp)](https://developer.android.com/blog/authors/david-chou) 02 Apr 2026 02 Apr 2026 ![](https://developer.android.com/static/blog/assets/announcing_gemma4_aicore_ce479292b9_Z15e7FP.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Announcing Gemma 4 in the AICore Developer Preview](https://developer.android.com/blog/posts/announcing-gemma-4-in-the-ai-core-developer-preview)

  [arrow_forward](https://developer.android.com/blog/posts/announcing-gemma-4-in-the-ai-core-developer-preview) At Google, we're committed to bringing the most capable AI models directly to the Android devices in your pocket. Today, we're thrilled to announce the release of our latest state-of-the-art open model: Gemma 4.

  ###### [Caren Chang](https://developer.android.com/blog/authors/caren-chang), [David Chou](https://developer.android.com/blog/authors/david-chou) •
  3 min read

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)