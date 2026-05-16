---
title: https://developer.android.com/blog/posts/the-fourth-beta-of-android-17
url: https://developer.android.com/blog/posts/the-fourth-beta-of-android-17
source: md.txt
---

#### [Product News](https://developer.android.com/blog/categories/product-news)

# The Fourth Beta of Android 17

###### 4-min read

![](https://developer.android.com/static/blog/assets/android17banner_359909419a_Z1HMAIH.webp) 16 Apr 2026 [![](https://developer.android.com/static/blog/assets/dgalpin_30033d2d42_Z1EXpfD.webp)](https://developer.android.com/blog/authors/daniel-galpin) [##### Daniel Galpin](https://developer.android.com/blog/authors/daniel-galpin)

###### Developer Advocate

Android 17 has reached beta 4, the last scheduled beta of this release cycle, a critical milestone for app compatibility and platform stability. Whether you're fine-tuning your app's user experience, ensuring smooth edge-to-edge rendering, or leveraging the newest APIs, Beta 4 provides the near-final environment you need to be testing with.

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

###### Written by:

-

  ## [Daniel Galpin](https://developer.android.com/blog/authors/daniel-galpin)

  ###### Developer Advocate

  [read_more
  View profile](https://developer.android.com/blog/authors/daniel-galpin) ![](https://developer.android.com/static/blog/assets/dgalpin_30033d2d42_Z1EXpfD.webp) ![](https://developer.android.com/static/blog/assets/dgalpin_30033d2d42_Z1EXpfD.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/Nataraj_K_work_profile_20e513e403_Z1TR4EY.webp)](https://developer.android.com/blog/authors/nataraj-k-r) 14 May 2026 14 May 2026 ![](https://developer.android.com/static/blog/assets/Bring_Native_Visibilityto_Your_Vo_IP_App_Experience_Strapi_4359a69748_Z2wOXhv.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Bring Native Visibility to Your VoIP App Experience with Telecom's Latest Alpha](https://developer.android.com/blog/posts/bring-native-visibility-to-your-vo-ip-app-experience-with-telecom-s-latest-alpha)

  [arrow_forward](https://developer.android.com/blog/posts/bring-native-visibility-to-your-vo-ip-app-experience-with-telecom-s-latest-alpha) Building on this foundation, Jetpack Telecom v1.1.0 brings native-level visibility and convenience to third-party VoIP apps.

  ###### [Nataraj K R](https://developer.android.com/blog/authors/nataraj-k-r) •
  2 min read

- [![](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_Z1Fsr5h.webp)](https://developer.android.com/blog/authors/matthew-mccullough) 12 May 2026 12 May 2026 ![](https://developer.android.com/static/blog/assets/Tas_Developers_cut_Strapi_3636223c9c_Z2pmmBN.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Building for the Intelligence System on Android](https://developer.android.com/blog/posts/building-for-the-intelligence-system-on-android)

  [arrow_forward](https://developer.android.com/blog/posts/building-for-the-intelligence-system-on-android) Announced today during The Android Show, Android is transitioning from an operating system to an intelligence system, creating more opportunities for engagement with your apps.

  ###### [Matthew McCullough](https://developer.android.com/blog/authors/matthew-mccullough) •
  4 min read

  - [#Android](https://developer.android.com/blog/topics/android)
- [![](https://developer.android.com/static/blog/assets/Vijaya_Kaza_38a0089092_1sYB49.webp)](https://developer.android.com/blog/authors/vijaya-kaza) 07 May 2026 07 May 2026 ![](https://developer.android.com/static/blog/assets/260429_A_look_ahead_to_2026_Banner_Strapi_2000_x_1000_px_b302a5104a_1L2cA4.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [A look ahead: Making it easier and faster to publish safer apps](https://developer.android.com/blog/posts/a-look-ahead-making-it-easier-and-faster-to-publish-safer-apps)

  [arrow_forward](https://developer.android.com/blog/posts/a-look-ahead-making-it-easier-and-faster-to-publish-safer-apps) The mobile ecosystem is always evolving, bringing both new opportunities and new threats. Through these changes, Android and Google Play remain committed to ensuring that billions of users can continue to enjoy their apps with confidence and developer innovation can thrive.

  ###### [Vijaya Kaza](https://developer.android.com/blog/authors/vijaya-kaza) •
  3 min read

  - [#Android](https://developer.android.com/blog/topics/android)

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)