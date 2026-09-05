---
title: https://developer.android.com/blog/posts/the-fourth-beta-of-android-17
url: https://developer.android.com/blog/posts/the-fourth-beta-of-android-17
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news)

# The Fourth Beta of Android 17

4 min read ![](https://developer.android.com/static/blog/assets/android17banner_359909419a_Z1HMAIH.webp) 16 Apr 2026 [![View Daniel Galpin's profile](https://developer.android.com/static/blog/assets/dgalpin_30033d2d42_Z1EXpfD.webp)](https://developer.android.com/blog/authors/daniel-galpin) [Daniel Galpin](https://developer.android.com/blog/authors/daniel-galpin) Developer Advocate Android 17 has reached beta 4, the last scheduled beta of this release cycle, a critical milestone for app compatibility and platform stability. Whether you're fine-tuning your app's user experience, ensuring smooth edge-to-edge rendering, or leveraging the newest APIs, Beta 4 provides the near-final environment you need to be testing with.

### **Get your apps, libraries, tools, and game engines ready!**

If you develop an Android SDK, library, tool, or game engine, it's critical to prepare any necessary updates now to prevent your downstream app and game developers from being blocked by compatibility issues and allow them to target the latest SDK features. Please let your downstream developers know if updates are needed to fully support Android 17.
![Android17_Timeline_01_V02.png](https://developer.android.com/static/blog/assets/Android_17_Timeline_01_V02_2_1_226309a3db_ZI4DHQ.webp)

Testing involves installing your production app or a test app making use of your library or engine using Google Play or other means onto a device or emulator running Android 17 Beta 4. Work through all your app's flows and look for functional or UI issues. Each release of Android contains platform changes that improve privacy, security, and overall user experience; review the app impacting behavior changes for apps [running on](https://developer.android.com/about/versions/17/behavior-changes-all) and [targeting](https://developer.android.com/about/versions/17/behavior-changes-17) Android 17 to focus your testing, including the following:

- **Resizability on large screens:** Once you target Android 17, you can no longer opt out of maintaining orientation, resizability and aspect ratio constraints [on large screens](https://developer.android.com/about/versions/17/changes/ff-restrictions-ignored).
- **Dynamic code loading:** If your app targets Android 17 or higher, the Safer Dynamic Code Loading (DCL) protection [introduced in Android 14](https://developer.android.com/about/versions/14/behavior-changes-14#safer-dynamic-code-loading) for DEX and JAR files now extends to native libraries. All native files loaded using System.load() must be marked as read-only. Otherwise, the system throws UnsatisfiedLinkError.
- **Enable CT by default:** [**Certificate transparency (CT)**](https://developer.android.com/privacy-and-security/security-config#CertificateTransparencySummary)**is enabled by default. (On Android 16, CT is available but apps had to** [**opt in**](https://developer.android.com/privacy-and-security/security-config#certificateTransparency)**.)**
- **Local network protections:** Apps targeting Android 17 or higher have [local network access blocked by default](https://developer.android.com/privacy-and-security/local-network-permission#android-17-enforcement). Switch to using privacy preserving pickers if possible, and use the new [ACCESS_LOCAL_NETWORK](https://developer.android.com/reference/kotlin/android/Manifest.permission#access_local_network) permission for broad, persistent access.
- **Background audio hardening:** Starting in Android 17, the audio framework enforces [restrictions on background audio interactions](https://developer.android.com/about/versions/17/changes/bg-audio) including audio playback, [audio focus](https://developer.android.com/media/optimize/audio-focus) requests, and [volume change](https://developer.android.com/reference/android/media/AudioManager#adjustStreamVolume(int,%20int,%20int)) APIs. Based on your feedback, we've made some changes since beta 2, including targetSDK gating while-in-use FGS enforcement and exempting alarm audio. Full details available in the [updated guidance](https://developer.android.com/about/versions/17/changes/bg-audio).

### **App memory limits**

Android is introducing app memory limits based on the device's total RAM to create a more stable and deterministic environment for your applications and Android users. In Android 17, limits are set conservatively to establish system baselines, targeting extreme memory leaks and other outliers before they trigger system-wide instability resulting in UI stuttering, higher battery drain, and apps being killed. While we anticipate minimal impact on the vast majority of app sessions, we recommend the [following memory best practices](https://developer.android.com/topic/performance/memory), including establishing a baseline for memory.

In the current implementation, [getDescription](https://developer.android.com/reference/android/app/ApplicationExitInfo#getDescription()) in [ApplicationExitInfo](https://developer.android.com/reference/kotlin/android/app/ApplicationExitInfo) will contain the string "MemoryLimiter" if your app was impacted. You can also use [trigger-based profiling](https://developer.android.com/topic/performance/tracing/profiling-manager/trigger-based-capture) with [TRIGGER_TYPE_ANOMALY](https://developer.android.com/reference/android/os/ProfilingTrigger#TRIGGER_TYPE_ANOMALY) to get heap dumps that are collected when the memory limit is hit.
![unnamed (2).png](https://developer.android.com/static/blog/assets/unnamed_2_681244c938_1S9WCW.webp) The LeakCanary task in the Android Studio Profiler

To help you find memory leaks, Android Studio Panda adds LeakCanary integration directly in the Android Studio Profiler as a dedicated task, contextualized within the IDE and fully integrated with your source code.

A lighter memory footprint translates directly to smoother performance, longer battery life, and a premium experience across all form factors. Let's build a faster, more reliable future for the Android ecosystem together!

**Profiling triggers for app anomalies**

Android introduces an on-device anomaly detection service that monitors for resource-intensive behaviors and potential compatibility regressions. Integrated with [ProfilingManager](https://developer.android.com/topic/performance/tracing/profiling-manager/overview), this service allows your app to receive profiling artifacts triggered by specific system-detected events.

Use the [TRIGGER_TYPE_ANOMALY](https://developer.android.com/reference/kotlin/android/os/ProfilingTrigger#trigger_type_anomaly) trigger to detect system performance issues such as excessive binder calls and excessive memory usage. When an app breaches OS-defined memory limits, the anomaly trigger allows developers to receive app-specific heap dumps to help identify and fix memory issues. Additionally, for excessive binder spam, the anomaly trigger provides a stack sampling profile on binder transactions.

This API callback occurs prior to any system imposed enforcements. For example, it can help developers collect debug data before the app is terminated by the system due exceeding memory limits. To understand how to use the trigger check out our documentation on [trigger based profiling](https://developer.android.com/topic/performance/tracing/profiling-manager/trigger-based-capture).

```java
    val profilingManager = applicationContext.getSystemService(ProfilingManager::class.java)
    val triggers = ArrayList<ProfilingTrigger>()  
    triggers.add(ProfilingTrigger.Builder(
                 ProfilingTrigger.TRIGGER_TYPE_ANOMALY))
    val mainExecutor: Executor = Executors.newSingleThreadExecutor()
    val resultCallback = Consumer<ProfilingResult> { profilingResult ->
        if (profilingResult.errorCode != ProfilingResult.ERROR_NONE) {
            // upload profile result to server for further analysis          
            setupProfileUploadWorker(profilingResult.resultFilePath)
        } 
    profilingManager.registerForAllProfilingResults(mainExecutor, resultCallback)
    profilingManager.addProfilingTriggers(triggers)
}
```

### **Post-Quantum Cryptography (PQC) in Android Keystore**

Android Keystore [added support](https://security.googleblog.com/2026/03/post-quantum-cryptography-in-android.html) for the [NIST-standardized](https://csrc.nist.gov/pubs/fips/204/final) ML-DSA (Module-Lattice-Based Digital Signature Algorithm). On supported devices, you can generate ML-DSA keys and use them to produce quantum-safe signatures, entirely in the device's secure hardware. Android Keystore exposes the ML-DSA-65 and ML-DSA-87 algorithm variants through the standard Java Cryptographic Architecture APIs: [KeyPairGenerator](https://developer.android.com/reference/java/security/KeyPairGenerator), [KeyFactory](https://developer.android.com/reference/java/security/KeyFactory), and [Signature](https://developer.android.com/reference/java/security/Signature). For further details, see our [developer documentation](https://developer.android.com/reference/android/security/keystore/KeyGenParameterSpec#example:-ml-dsa-key-pair-for-signing).

```java
KeyPairGenerator generator = KeyPairGenerator.getInstance(
        "ML-DSA-65", "AndroidKeyStore");
generator.initialize(
        new KeyGenParameterSpec.Builder(
                "my-key-alias",
                KeyProperties.PURPOSE_SIGN | KeyProperties.PURPOSE_VERIFY)
        .build());
KeyPair keyPair = generator.generateKeyPair();
```

### **Get started with Android 17**

You can [enroll any supported Pixel device](https://www.google.com/android/beta) to get this and future Android Beta updates over-the-air. If you don't have a Pixel device, you can [use the 64-bit system images with the Android Emulator](https://developer.android.com/about/versions/17/get#on_emulator) in Android Studio.

If you are currently in the Android Beta program, you will be offered an over-the-air update to Beta 4.

Continue to [report issues and submit feature requests](https://developer.android.com/about/versions/17/feedback) on the [feedback page](https://developer.android.com/about/versions/16/feedback). The earlier we get your feedback, the more we can include in our work on the final release.

For the best development experience with Android 17, we recommend that you use the latest preview of [Android Studio (Panda)](https://developer.android.com/studio/preview). Once you're set up, here are some of the things you should do:

- Compile against the new SDK, test in CI environments, and report any issues in our tracker on the [feedback page](https://developer.android.com/about/versions/17/feedback).
- Test your current app for compatibility, learn whether your app is affected by changes in Android 17, and install your app onto a device or emulator running Android 17 and extensively test it.

We'll update the [preview/beta system images](https://developer.android.com/about/versions/17/download) and SDK regularly throughout the Android 17 release cycle. Once you've installed a beta build, you'll automatically get future updates over-the-air for all later previews and Betas.

For complete information, visit the [Android 17 developer site](https://developer.android.com/about/versions/17).

### **Join the conversation**

Your feedback remains our most valuable asset. Whether you're an [early adopter on the Canary channel](https://www.reddit.com/r/android_canary/) or an [app developer testing on Beta 4](https://www.reddit.com/r/android_beta/), consider joining our communities and filing feedback. We're listening.
Written by:

-

  ## [Daniel Galpin](https://developer.android.com/blog/authors/daniel-galpin)

  ###### Developer Advocate

  [read_more
  View profile](https://developer.android.com/blog/authors/daniel-galpin) ![View Daniel Galpin's profile](https://developer.android.com/static/blog/assets/dgalpin_30033d2d42_Z1EXpfD.webp) ![View Daniel Galpin's profile](https://developer.android.com/static/blog/assets/dgalpin_30033d2d42_Z1EXpfD.webp)
Continue reading
- [![View Amman Asfaw's profile](https://developer.android.com/static/blog/assets/unnamed_11_a00df7e0e8_ZARb6S.webp)](https://developer.android.com/blog/authors/amman-asfaw) 01 Sep 2026 01 Sep 2026 ![](https://developer.android.com/static/blog/assets/Quail_Blog_Strapi_c8d4ba2105_Z2bRC9Y.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Leverage Android skills and Gemma 4 in Android Studio Quail 4](https://developer.android.com/blog/posts/leverage-android-skills-and-gemma-4-in-android-studio-quail-4)

  [arrow_forward](https://developer.android.com/blog/posts/leverage-android-skills-and-gemma-4-in-android-studio-quail-4) This is the final stable release for Android Studio Quail. The new features in Android Studio enable you to build premium apps with AI efficiently and effectively.
  [Amman Asfaw](https://developer.android.com/blog/authors/amman-asfaw) • 5 min read
  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)
  - [#Android Skills](https://developer.android.com/blog/topics/android-skills)
- [![View Raghavendra Hareesh Pottamsetty's profile](https://developer.android.com/static/blog/assets/Raghavendra_Hareesh_Pottamsetty_72fdb063a0_1h0S85.webp)](https://developer.android.com/blog/authors/raghavendra-hareesh-pottamsetty) 26 Aug 2026 26 Aug 2026 ![](https://developer.android.com/static/blog/assets/Raising_the_bar_Google_Play_Strapi_2_a80695bf12_Z2jxf1k.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Elevating app quality: Reducing memory usage and improving device migration](https://developer.android.com/blog/posts/elevating-app-quality-reducing-memory-usage-and-improving-device-migration)

  [arrow_forward](https://developer.android.com/blog/posts/elevating-app-quality-reducing-memory-usage-and-improving-device-migration) Maintaining a healthy Android ecosystem is a shared commitment where every app and game has a role to play.
  [Raghavendra Hareesh Pottamsetty](https://developer.android.com/blog/authors/raghavendra-hareesh-pottamsetty) • 4 min read
- [![View Ron Aquino's profile](https://developer.android.com/static/blog/assets/unnamed_18_8bd07de9bd_9wUet.webp)](https://developer.android.com/blog/authors/ron-aquino) 25 Aug 2026 25 Aug 2026 ![](https://developer.android.com/static/blog/assets/Ensuring_a_safe_Gen_AI_ecosystem_on_Google_Play_Scrapi_a8fa6da415_ZsHups.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Ensuring Safety in the Generative AI Ecosystem: Protecting Users from Non-Consensual Intimate Content](https://developer.android.com/blog/posts/ensuring-safety-in-the-generative-ai-ecosystem-protecting-users-from-non-consensual-intimate-content)

  [arrow_forward](https://developer.android.com/blog/posts/ensuring-safety-in-the-generative-ai-ecosystem-protecting-users-from-non-consensual-intimate-content) At Google Play, user safety and developer success go hand in hand. We continue to see growth in apps with AI generated features, and indeed, adding generative AI into your apps is a great way to unlock incredible creative possibilities.
  [Ron Aquino](https://developer.android.com/blog/authors/ron-aquino) • 4 min read
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)