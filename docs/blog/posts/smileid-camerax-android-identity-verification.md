---
title: https://developer.android.com/blog/posts/smileid-camerax-android-identity-verification
url: https://developer.android.com/blog/posts/smileid-camerax-android-identity-verification
source: md.txt
---

[Case Studies](https://developer.android.com/blog/categories/case-studies.md.txt)

# How SmileID Scaled Identity Verification to 18,000+ Android Device Types with CameraX

4 min read ![](https://developer.android.com/static/blog/assets/1007_ABL_134_How_Smile_ID_Scaled_Identity_Verification_with_Camera_X_Strapi_788bf73f23_1N5Hb5.webp) 11 Nov 2026 [![View Donovan McMurray's profile](https://developer.android.com/static/blog/assets/Donovan_Mc_Murray_9413499dd8_1V0INl.webp)](https://developer.android.com/blog/authors/donovan-mcmurray.md.txt) [Donovan McMurray](https://developer.android.com/blog/authors/donovan-mcmurray.md.txt) Developer Relations Engineer Identity verification apps for banking and SIM registration require clear, high-resolution face captures to detect spoofing and deepfakes. Capturing frames sharp enough for liveness and anti-spoofing checks, without crashing low-memory devices, is a common challenge for Android camera developers.

For [SmileID](https://usesmileid.com/), a leading identity verification SDK in Africa, this challenge is doubled by a diverse hardware ecosystem. Android represents **85% of SmileID's target devices market share**, including entry-level smartphones with highly constrained processors, obscure regional models, and ruggedized custom Point of Sale (POS) terminals.
![harun_quote_card_green.png](https://developer.android.com/static/blog/assets/harun_quote_card_green_57e4940f8b_1aEyED.webp)

Before adopting [CameraX](https://developer.android.com/training/camerax), SmileID faced standard but daunting camera engineering hurdles:**stretched preview feeds,** **rotated sensor orientations** , **out-of-memory (OOM) crashes** , and **custom original equipment manufacturer (OEM) bugs**. By migrating their core Android SDKs to CameraX, SmileID transformed these challenges into a major business advantage.

According to SmileID, migrating their Android SDKs to CameraX delivered the following results:

| Metric | Impact of CameraX Migration |
|---|---|
| SDK Adoption Growth | 20x by year 2 (up from 2-3x before CameraX) |
| Verification Pass Rates | 20% increase for apps using SmileID's SDKs |
| Capture Resolution | 4x increase in selfie/liveness pixels with zero network overhead |
| Device Model Compatibility | 18,000+ Android device types supported |
| Total Verifications Scaled | 160 million+ identity verifications processed |

## **The Challenge: Fragmented Hardware \& Legacy API Pain**

To confirm that a user is who they claim to be, SmileID's SDK must capture high-resolution selfie frames for on-device liveness checks and cloud-based deepfake detection.

Under [legacy Camera1](https://developer.android.com/media/camera/camerax/camera1-to-camerax.md.txt) and low-level Camera2 API implementations, achieving this consistently was difficult for several reasons:

- **OEM Customizations \& Quirks** : Devices from different manufacturers reported physical [camera sensor orientations](https://developer.android.com/media/camera/camerax/orientation-rotation.md.txt) differently, resulting in rotated previews or incorrectly oriented face captures.
- **Aspect Ratio Distortions**: Requesting a specific frame size on budget devices often caused the camera preview to stretch vertically or horizontally, distorting the user's face and rendering biometric verification useless.
- **Out-of-Memory (OOM) Crashes**: Processing raw high-resolution images on devices with low RAM (often 1 GB or less) frequently led to fatal memory allocation crashes.

Because of these friction points, SmileID's year-over-year SDK adoption growth was limited to 2-3x, and many verifications had to fall back to uploading static photos over a high-latency REST API instead of running real-time on-device liveness checks.

## **The Solution: Consistent Pipelines with CameraX**

SmileID re-engineered their Mobile SDKs from the ground up using CameraX, which is built specifically to abstract away the complexity of the underlying device ecosystem and provide a consistent, [natively lifecycle-aware](https://developer.android.com/media/camera/camerax/architecture.md.txt#lifecycles) developer interface.

Using CameraX's core use cases (specifically `Preview` and `ImageAnalysis`) SmileID built a robust, dual-purpose camera pipeline:

- [Preview](https://developer.android.com/media/camera/camerax/preview.md.txt): Renders a perfectly proportioned, real-time preview of the camera feed to guide the user.
- [ImageAnalysis](https://developer.android.com/media/camera/camerax/analyze.md.txt): Continuously processes frames locally in real-time to execute automated liveness and face-in-frame detection and extract the verified selfie frame.

To capture ultra-sharp details for deepfake detection without causing OOM crashes, SmileID added CameraX's modern [ResolutionSelector](https://developer.android.com/reference/androidx/camera/core/resolutionselector/ResolutionSelector.md.txt) API directly to their `ImageAnalysis` configuration. It lets developers request a target resolution and choose a fallback rule when a device does not support that exact size. For example, the following diagram and sample configuration illustrate how ResolutionSelector evaluates candidate sizes around a 1200x900 target:
![resolution_selector_diagram_vertical.png](https://developer.android.com/static/blog/assets/resolution_selector_diagram_vertical_374522856f_Z2n3DVI.webp)

Here is the corresponding sample code showing how you can pair ResolutionSelector with `STRATEGY_KEEP_ONLY_LATEST` in your own app (use `FALLBACK_RULE_CLOSEST_HIGHER_THEN_LOWER` to prioritize sharpness, or `FALLBACK_RULE_CLOSEST_LOWER_THEN_HIGHER` to cap memory usage):

```kotlin
import android.util.Size
import androidx.camera.core.CameraSelector
import androidx.camera.core.ImageAnalysis
import androidx.camera.core.Preview
import androidx.camera.core.resolutionselector.AspectRatioStrategy
import androidx.camera.core.resolutionselector.ResolutionSelector
import androidx.camera.core.resolutionselector.ResolutionStrategy
import androidx.camera.lifecycle.ProcessCameraProvider
import androidx.lifecycle.LifecycleOwner

fun configureCameraX(cameraProvider: ProcessCameraProvider, lifecycleOwner: LifecycleOwner, 
                     surfaceProvider: Preview.SurfaceProvider, 
                     executor: java.util.concurrent.Executor, analyzer: ImageAnalysis.Analyzer) {
    // 1. Define a resolution strategy requesting high quality (for example, 1200x900px) 
    // and selecting the closest higher (or, if unavailable, lower) resolution.
    val resolutionSelector = ResolutionSelector.Builder()
        .setResolutionStrategy(
            ResolutionStrategy(
                Size(1200, 900),
                ResolutionStrategy.FALLBACK_RULE_CLOSEST_HIGHER_THEN_LOWER
            )
        )
        .setAspectRatioStrategy(AspectRatioStrategy.RATIO_4_3_FALLBACK_AUTO_STRATEGY)
        .build()

    // 2. Configure the ImageAnalysis use case with the resolution selector
    // and a backpressure strategy that keeps the UI responsive on slow processors.
    val imageAnalysis = ImageAnalysis.Builder()
        .setResolutionSelector(resolutionSelector)        
        // Drops older frames if the device's CPU is still busy analyzing the previous one
        .setBackpressureStrategy(ImageAnalysis.STRATEGY_KEEP_ONLY_LATEST)
        .build()

    // 3. Set up the preview stream and attach the Analyzer and SurfaceProvider
    imageAnalysis.setAnalyzer(executor, analyzer)
    val preview = Preview.Builder().build().also { it.surfaceProvider = surfaceProvider }

    // 4. Bind both use cases concurrently to the lifecycle provider
    try {
        cameraProvider.unbindAll()
        cameraProvider.bindToLifecycle(
            lifecycleOwner,
            CameraSelector.DEFAULT_FRONT_CAMERA,
            preview,
            imageAnalysis
        )
    } catch (exc: Exception) {
        // Handle binding failure safely
    }
}
```

By requesting high-density pixel frames and processing them locally, SmileID achieved a **4x increase in captured selfie resolution**. SmileID also compressed the cropped face region on the device so the network upload size stayed identical to their previous system. This architecture guaranteed sharper data for their machine learning models without increasing cellular data costs for their users.

## **How CameraX Solves Hardware Differences**

Standardizing on CameraX meant SmileID could rely on two layers of compatibility engineering to keep their SDK stable across devices:

### **1. Google's Camera and Media Test Lab**

CameraX's compatibility is backed by continuous, physical hardware verification. In Google's dedicated **Camera and Media Test Lab** , an automated test suite runs daily across a massive, rotating matrix of over **190 physical Android device models**. This includes devices representing different chipsets, OS versions, and hardware capabilities.

To move toward more consistent behavior across popular devices, Google's Camera and Media Test Lab automatically catches library regressions before they can affect your production code.

### **2. Automatic Workarounds for Device Quirks**

Different Android devices have different physical limitations. Some might fail to set custom exposure settings, while others might report inverted image data when using certain aspect ratios. To prevent developers from polluting their codebases with complex conditional blocks based on device manufacturer and model, CameraX maintains internal device quirk classes such as DeviceQuirks and CameraQuirks in camera-camera2 ([DeviceQuirksLoader.kt](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:camera/camera-camera2/src/main/java/androidx/camera/camera2/compat/quirk/DeviceQuirksLoader.kt)). When CameraX detects a device with a known issue, it automatically injects a tailored workaround. For SmileID, this meant their SDK could work reliably across 18,000+ Android device types without needing device-specific patches in their codebase.

## **Scaling up to 160 million+ Verifications**

By migrating to CameraX, SmileID simplified SDK integration for external app developers.

Eliminating aspect ratio distortions, laggy previews, and sudden OOM crashes drove a **20% increase in verification pass rates** for services using their SDKs. For financial institutions and mobile money apps across Africa, a 20% increase in pass rates means hundreds of thousands of legitimate users successfully onboarding instead of churning.
![juma_quote_card_blue.png](https://developer.android.com/static/blog/assets/juma_quote_card_blue_2f96951498_1vt0dY.webp)

Developers took notice. The ease of integrating the CameraX-based SDK triggered a **15x adoption surge in the first year** , climbing to **20x adoption by the second year** . To date, SmileID has successfully processed over **160 million identity verifications** using CameraX.

## **Build Your Compatibility Story with the CameraX Skill**

Developing for cameras doesn't have to be hard. To help your team adopt the same CameraX patterns SmileID used, Android has launched the [CameraX Skill](https://github.com/android/skills/tree/main/camera/camerax) for AI coding agents.

When you use the CameraX Skill in your development environment, AI coding agents such as Gemini apply current CameraX patterns for [migration](https://developer.android.com/media/camera/camerax/camera1-to-camerax.md.txt), lifecycle binding, [ConcurrentCamera](https://developer.android.com/reference/androidx/camera/core/ConcurrentCamera.md.txt), and [MlKitAnalyzer](https://developer.android.com/media/camera/camerax/mlkitanalyzer.md.txt). Whether you are setting up dual-camera feeds, configuring a preview with [PreviewView](https://developer.android.com/reference/androidx/camera/view/PreviewView.md.txt) or [CameraXViewfinder](https://developer.android.com/reference/kotlin/androidx/camera/compose/CameraXViewfinder.composable.md.txt), or managing real-time machine learning (ML) analysis, the CameraX Skill guides your agent to generate precise, production-ready code.

- **Explore the CameraX Skill** : Visit the [Android Developer Skills Directory](https://developer.android.com/tools/agents/android-skills/browse.md.txt) or run `android skills add camerax` with the Android CLI to add the skill to your AI coding tool.
- **Get Started with CameraX** : Jump into the [Official CameraX Documentation](https://developer.android.com/training/camerax) and make your camera experience run anywhere.
- [#Camera X](https://developer.android.com/blog/topics/camera-x.md.txt)
Written by:

-

  ## [Donovan McMurray](https://developer.android.com/blog/authors/donovan-mcmurray.md.txt)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/donovan-mcmurray) ![View Donovan McMurray's profile](https://developer.android.com/static/blog/assets/Donovan_Mc_Murray_9413499dd8_1V0INl.webp) ![View Donovan McMurray's profile](https://developer.android.com/static/blog/assets/Donovan_Mc_Murray_9413499dd8_1V0INl.webp)
Continue reading
- 3 Authors 19 Oct 2026 19 Oct 2026 ![](https://developer.android.com/static/blog/assets/ANDDM_Grab_Strapi_2000x1000_STATIC_1_dbb884ce74_22df0m.webp) [Case Studies](https://developer.android.com/blog/categories/case-studies.md.txt)

  ## [Grab Reduces ANRs by 32% and improves startup time by 35% with R8 and Profile guided optimization](https://developer.android.com/blog/posts/grab-r8-profile-guided-optimization-anr-startup-time.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/grab-r8-profile-guided-optimization-anr-startup-time.md.txt) Grab is Southeast Asia's leading superapp, offering deliveries, mobility, and financial services to millions of users across eight countries through a single app.
  [Ajesh Pai](https://developer.android.com/blog/authors/ajesh-pai.md.txt), [Nguyen Van Minh](https://developer.android.com/blog/authors/nguyen-van-minh.md.txt), [Tracy Agyemang](https://developer.android.com/blog/authors/tracy-agyemang.md.txt) • 5 min read
  - [#Adaptive \& Differentiated](https://developer.android.com/blog/topics/adaptive-and-differentiated.md.txt)
- [![View Pavlo Stavytskyi's profile](https://developer.android.com/static/blog/assets/pavlo_a4e2ec12e9_v4xs2.webp)](https://developer.android.com/blog/authors/pavlo-stavytskyi.md.txt)[![View Rebecca Franks's profile](https://developer.android.com/static/blog/assets/unnamed_12_b05cc1bf55_Z1XnKqa.webp)](https://developer.android.com/blog/authors/rebecca-franks.md.txt) 30 Sep 2026 30 Sep 2026 ![](https://developer.android.com/static/blog/assets/Compose_Carousel_Strapi_3_ca1ff69fce_Z1u412n.webp) [Case Studies](https://developer.android.com/blog/categories/case-studies.md.txt)

  ## [How Instagram Direct engineers built AI-native UI architecture with Jetpack Compose and reduced token cost per agent session by 33%](https://developer.android.com/blog/posts/jetpack-compose-ai-native-ui-instagram-direct.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/jetpack-compose-ai-native-ui-instagram-direct.md.txt) The team built an AI-native UI codebase that is 50% smaller than the original implementation, while achieving a 35% reduction in AI agent execution time, 32% fewer engineer-agent exchanges, and a 33% reduction in token cost.
  [Pavlo Stavytskyi](https://developer.android.com/blog/authors/pavlo-stavytskyi.md.txt), [Rebecca Franks](https://developer.android.com/blog/authors/rebecca-franks.md.txt) • 11 min read
  - [#Compose-first](https://developer.android.com/blog/topics/compose-first.md.txt)
  - [#Jetpack Compose](https://developer.android.com/blog/topics/jetpack-compose.md.txt)
- 3 Authors 27 Aug 2026 27 Aug 2026 ![](https://developer.android.com/static/blog/assets/ANDDM_Passkeys_Strapi_2fc9df18a8_Z28fFzY.webp) [Case Studies](https://developer.android.com/blog/categories/case-studies.md.txt)

  ## [How WhatsApp Upgraded to Secure, Seamless Sign-In for 1 Billion Users with Passkeys](https://developer.android.com/blog/posts/how-whats-app-upgraded-to-secure-seamless-sign-in-for-1-billion-users-with-passkeys.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/how-whats-app-upgraded-to-secure-seamless-sign-in-for-1-billion-users-with-passkeys.md.txt) WhatsApp is the world's largest messaging platform, serving billions of users globally. It is the default communication tool for people across diverse regions, connecting users through private, reliable, and secure messaging.
  [Niharika Arora](https://developer.android.com/blog/authors/niharika-arora.md.txt), [Tracy Agyemang](https://developer.android.com/blog/authors/tracy-agyemang.md.txt), [Mayank Jain](https://developer.android.com/blog/authors/blog-author.md.txt) • 8 min read
  - [#Passkeys](https://developer.android.com/blog/topics/passkeys.md.txt)
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1zVtXW.webp)