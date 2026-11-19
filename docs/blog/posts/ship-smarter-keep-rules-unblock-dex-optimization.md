---
title: https://developer.android.com/blog/posts/ship-smarter-keep-rules-unblock-dex-optimization
url: https://developer.android.com/blog/posts/ship-smarter-keep-rules-unblock-dex-optimization
source: md.txt
---

> Documentation index: https://developer.android.com/blog/llms.txt

[How-tos](https://developer.android.com/blog/categories/how-tos.md.txt)

# Ship smarter keep rules: How library providers can unblock app-level DEX code optimization

6 min read ![](https://developer.android.com/static/blog/assets/1109_ABL_160_Ship_smarter_keep_rules_How_library_providers_can_unblock_app_level_DEX_code_optimization_1_44aba4f3cd_1kr2I.webp) 17 Nov 2026 [![View Breana Tate's profile](https://developer.android.com/static/blog/assets/Breana_Tate_24c1d03bf2_1PpSPG.webp)](https://developer.android.com/blog/authors/breana-tate.md.txt) [Breana Tate](https://developer.android.com/blog/authors/breana-tate.md.txt) Developer Relations Engineer As Android app and library developers, we all strive for the same goal: **performant apps that provide a smooth user experience.** A major part of that involves [R8](https://developer.android.com/topic/performance/app-optimization/enable-app-optimization.md.txt), Android's app optimizer. R8 improves app performance by removing unused code, and optimizing and obfuscating the rest.

Google Play [recently announced](https://android-developers.googleblog.com/2026/08/app-quality-memory-optimization-secure-onboarding.html) new DEX code optimization thresholds for apps and games, which help improve startup times, reduce memory footprint, and align with Android's commitment to insulate the user experience from apps using excess memory. While these thresholds apply to apps and games, meeting them is a shared responsibility across the ecosystem---R8 can only optimize an app within the parameters it's given, which includes the keep rules bundled by the libraries the app depends on.

The [R8 Configuration Analyzer](https://developer.android.com/topic/performance/app-optimization/r8-configuration-analyzer.md.txt) is a great tool [for assessing app optimization](https://android-developers.googleblog.com/2026/08/tinder-app-cold-start-r8-configuration-analyzer.html), shrinking, and obfuscation percentages, which are at the core of Google Play's technical requirements. In addition to tracking these percentages, the R8 Configuration Analyzer also surfaces inefficient keep rules originating from not only *apps*, but also *consumer keep rules* bundled in libraries apps depend on.

This guide outlines how you can resolve some of the most common challenges library providers face, and ship [narrow, high-performance rules](https://developer.android.com/topic/performance/app-optimization/library-optimization.md.txt#requirements) to help your customers meet [Google Play technical requirements](https://support.google.com/googleplay/android-developer/answer/17492799#zippy=%2Cdex-code-optimization).

### **What are consumer keep rules?**

[Consumer keep rules](https://developer.android.com/topic/performance/app-optimization/library-optimization.md.txt#library-keep-rule-types) are instructions bundled within an Android or JAR library that tell R8 which parts of the library code may not be optimized during the app-level compilation process. Unlike standard keep rules written by the app or library used in their artifact minification, consumer keep rules are embedded inside libraries, and affect how the library is minified during whole-app optimization--ensuring that internal reflection targets, and native interfaces remain intact without the app developer needing to manually identify them.

**Intentional, narrowly scoped consumer keep rules** are a critical best practice that benefits both the library and the apps that consume it. Overly broad consumer keep rules preserve unused code and as a result, impact an app's optimization and performance. With [**DEX code optimization**](https://developer.android.com/events/dev-summit/talks/type-safe-keep-rules-and-dex-optimization.md.txt)**insights added to the Play Console**, the metrics app developers will see represent the combined impact of rules from both the app and its integrated libraries.

### **Balancing stability and performance**

Library providers are often well-intentioned in shipping broad consumer keep rules. No one wants their SDK to trigger a crash due to class removal during reflection.

However, package-wide or otherwise broad keep rules aren't recommended as a long term solution for crash prevention, as they severely limit R8's whole-program app optimization potential. Here are some recommended strategies to help you ship narrow, high-performance rules without sacrificing stability:

#### **1. Testing and rolling out narrow rules**

To help you release narrow rules with confidence, consider these best practices:

- Test in a sample app: The local testing guidance at [Test your optimization](https://developer.android.com/topic/performance/app-optimization/test-the-optimization.md.txt) applies for sample apps as well. After enabling R8, test critical user journeys to ensure functionality is working as expected.
- Run the [R8 Configuration Analyzer](https://developer.android.com/topic/performance/app-optimization/r8-configuration-analyzer.md.txt) on your sample app to see what app developers see when auditing their R8 configuration. It allows you to easily visualize the impacts of your keep rules on downstream apps.
- Use [the analyze command from Android CLI](https://developer.android.com/tools/agents/android-cli/commands/analyze.md.txt) to assess your AAR or JAR's optimization, including kept methods, classes, and fields. You can compare these numbers across releases to monitor for regressions.
- Monitor library version usage and crashes in the Google Play SDK Console.
- Reference the [Optimization for library authors](https://developer.android.com/topic/performance/app-optimization/library-optimization.md.txt) guidance, and the [R8 documentation](https://developer.android.com/topic/performance/app-optimization/enable-app-optimization.md.txt) for best practices.

#### **2. Preserving reflection and JNI targets without broad keep rules**

Shipping a library with broad or package-wide keep rules doesn't only impact your SDK, it also forces developers to accept code bloat that slows down app startup time and increases app download size, memory usage, and ANR rates. It's also possible that performance-minded apps will [write custom rules that replace the ones bundled with your library](https://developer.android.com/topic/performance/app-optimization/choose-libraries-wisely.md.txt#filter-rules), which also discourages these apps from adopting future library updates in order to reduce risk.

If your SDK targets [native code](https://developer.android.com/ndk), such as that in games or photo and video editors, provide rules for all classes that use [JNI](https://developer.android.com/topic/performance/app-optimization/keep-rule-examples.md.txt#java-native-interface-jni). Most games run on top of game engines such as [Unity](https://unity.com/) and [Unreal](https://www.unrealengine.com/), that compile the game down to native code. The game native code and your plugin communicates with the Android framework via JNI calls.

[Jetpack Keep annotations](https://developer.android.com/topic/performance/app-optimization/jetpack-keep-annotations.md.txt), now in alpha, can help reduce maintenance required by reflection, by letting you annotate reflection usage, which can then be used to generate keep rules at build time.

**Consider codegen over reflection**

To avoid crashes due to reflection, our biggest tip is to avoid reflection and use [codegen](https://developer.android.com/topic/performance/app-optimization/library-optimization.md.txt#requirements) where possible.

Runtime reflection hides code usage from R8 during compilation, which requires keep rules to avoid crashes. If you use codegen, code is optimized during the build process, enabling R8 to have the necessary visibility to safely optimize code with minimal keep rules. Common scenarios where codegen is a great choice include serialization and deserialization, and dependency injection ([Hilt](https://developer.android.com/training/dependency-injection/hilt-android.md.txt) is an example of a library that uses codegen).

However, codegen is not the right choice for every scenario. For patterns like optional dependencies, reflection is still necessary. We recommend pairing reflection with narrow keep rules that protect only required entry points, as described in the guidance on [Reflection to support optional dependencies](https://developer.android.com/topic/performance/app-optimization/keep-rule-examples.md.txt#reflection-to-support-optional-dependencies).

**Scope rules narrowly, even for pre-optimized library builds**

If it's not possible to avoid reflection, ensure your consumer [keep rules specify only what your library reflects on](https://developer.android.com/topic/performance/app-optimization/keep-rules-best-practices.md.txt). When your library accesses a class or method dynamically, you only need to specify the entry point, and R8 will take care of the rest. R8 uses the entry points to build a graph of referenced code and remove any unreferenced classes, methods, and fields.

This also applies if you have already optimized or obfuscated your library build, which is a great practice to ensure a performant and lightweight SDK. Because your rules apply during the app's compilation step, R8 can still further optimize your library based on the actual classes and methods that are used by the downstream app. The [Android CLI analyze command](https://developer.android.com/tools/agents/android-cli/commands/analyze.md.txt) proactively surfaces both used and unused package-wide keep rules that are contributing to blocked optimization.

**Scope keep rules narrowly for third-party dependencies**

This is a common pattern we've seen:

```
-keep public class com.google.android.gms.** { *; }
```

If an app integrating your SDK also uses another GMS library, and includes a keep rule to limit the amount of code kept, this broad rule supersedes it, contributing to unnecessary app bloat.

When invoking external libraries, you should design keep rules that strictly preserve only the specific elements your library accesses through reflection. Additionally, the reality is, many libraries (including GMS) already ship their own consumer keep rules--introducing a package-wide keep rule can also subsume carefully written, narrowly scoped consumer rules from the downstream library.

**Consider conditional keep rules for ad mediation adapters**

If your ad library is loaded using mediation adapters, narrow keep rules are still an option. In this scenario, we recommend using [conditional keep rules](https://developer.android.com/topic/performance/app-optimization/add-keep-rules.md.txt#conditional-keep-rules-reflection) to only preserve certain features or formats if the app includes the corresponding adapter. This ensures that R8 can still shrink features the app doesn't use. As another option, rather than writing complex rules by hand, you can also use the Jetpack Keep annotations to annotate your reflective calls directly in source code and automatically generate conditional consumer keep rules, including for optional add-on modules.

**Ship rules in consumer rules, not documentation**

By shipping consumer rules with your library, you ensure that apps with an R8-enabled build can use your library out of the box and unlock the maximum optimization.

Specifying rules in your documentation adds manual setup friction (especially since bundled consumer keep rules have been supported in AARs and JARs for years) and creates ongoing maintenance overhead. When you update your library (including refactoring, renaming classes, and changing how reflection is used) you must remember to update the documentation, and apps must remember to check for new rules. Over time, as apps upgrade through multiple versions of your library, they may accumulate legacy keep rules that are no longer needed, leading to unnecessary app bloat.

#### **3. Reading release stack traces**

You may have encountered an unreadable stack trace due to obfuscated code. To unblock critical analysis, it can be tempting to use `keepnames`, which [allows for shrinking](https://developer.android.com/topic/performance/app-optimization/add-keep-rules.md.txt#choose-keep), but prevents additional optimizations like renaming in the consuming app--the precise values you need when debugging a stack trace.

You don't need to prevent additional optimizations to get readable stack traces.

Firebase Crashlytics, Play Console, and Logcat in Android Studio deobfuscate stack traces for app developers. This means, if an app developer shares a stack trace with you, you do not need to prevent obfuscation to be able to read it.

If you upload your mapping file to the SDK Console, it will allow you to see deobfuscated stack traces in [SDK Console](https://support.google.com/googleplay/android-developer/answer/12244916).

### **Take the guesswork out of optimization**

Optimizing your library shouldn't feel like a game of trial and error.

By maintaining consumer keep rules, library providers can ensure that apps across the ecosystem are unblocked from optimization.

When libraries ship better rules, apps become smaller and faster. Start auditing your consumer keep rules today to help apps that depend on your library perform at their best.
- [#Adaptive \& Differentiated](https://developer.android.com/blog/topics/adaptive-and-differentiated.md.txt)
Written by:

-

  ## [Breana Tate](https://developer.android.com/blog/authors/breana-tate.md.txt)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/breana-tate) ![View Breana Tate's profile](https://developer.android.com/static/blog/assets/Breana_Tate_24c1d03bf2_1PpSPG.webp) ![View Breana Tate's profile](https://developer.android.com/static/blog/assets/Breana_Tate_24c1d03bf2_1PpSPG.webp)
Continue reading
- 3 Authors 19 Nov 2025 19 Nov 2025 ![](https://developer.android.com/static/blog/assets/performance_Week11_efe6dd10be_1ULXct.webp) [How-tos](https://developer.android.com/blog/categories/how-tos.md.txt)

  ## [Deeper Performance Considerations](https://developer.android.com/blog/posts/deeper-performance-considerations.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/deeper-performance-considerations.md.txt) We're covering Profile Guided Optimization, Jetpack Compose performance improvements and considerations on working behind the scenes.
  [Ben Weiss](https://developer.android.com/blog/authors/ben-weiss.md.txt), [Breana Tate](https://developer.android.com/blog/authors/breana-tate.md.txt), [Jossi Wolf](https://developer.android.com/blog/authors/jossi-wolf.md.txt) • 8 min read
- [![View Jolanda Verhoef's profile](https://developer.android.com/static/blog/assets/jolanda_b0e2beee3e_1gwMmp.webp)](https://developer.android.com/blog/authors/jolanda-verhoef.md.txt) 28 Sep 2026 28 Sep 2026 ![](https://developer.android.com/static/blog/assets/0817_Booking_assistant_agentic_cloud_Strapi_36710f6e0c_hrRjy.webp) [How-tos](https://developer.android.com/blog/categories/how-tos.md.txt)

  ## [Build intelligent Android apps: In-app agentic workflows](https://developer.android.com/blog/posts/build-intelligent-android-apps-in-app-agentic-workflows.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/build-intelligent-android-apps-in-app-agentic-workflows.md.txt) Welcome back to the blog post series "Build intelligent Android apps" where you take a basic Android app and transform it into a personalized, intelligent, and agentic experience. In our previous post you learned how to connect to the intelligence system using AppFunctions.
  [Jolanda Verhoef](https://developer.android.com/blog/authors/jolanda-verhoef.md.txt) • 9 min read
  - [#Intelligent Apps](https://developer.android.com/blog/topics/intelligent-apps.md.txt)
- [![View Toni Heidenreich's profile](https://developer.android.com/static/blog/assets/profile_picture_6cdbf09ec9_Z1i2yxW.webp)](https://developer.android.com/blog/authors/toni-heidenreich.md.txt) 11 Aug 2026 11 Aug 2026 ![](https://developer.android.com/static/blog/assets/AFD_ABL_101_Media3_1_11_is_out_Strapi_bebd1c9efc_Zpob7z.webp) [How-tos](https://developer.android.com/blog/categories/how-tos.md.txt)

  ## [Media3 1.11 - What's new?](https://developer.android.com/blog/posts/media3-1-11-whats-new.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/media3-1-11-whats-new.md.txt) Media3 1.11 is out. Powering the vast majority of top Android media apps, this release brings new features, bug fixes, and improvements across playback, editing, and UI components.
  [Toni Heidenreich](https://developer.android.com/blog/authors/toni-heidenreich.md.txt) • 3 min read
  - [#Media3](https://developer.android.com/blog/topics/media3.md.txt)
  - [#Jetpack](https://developer.android.com/blog/topics/jetpack.md.txt)
  - [#ExoPlayer](https://developer.android.com/blog/topics/exo-player.md.txt)
  - +1 ↩
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1zVtXW.webp)