---
title: https://developer.android.com/blog/posts/tinder-cuts-app-cold-starts-by-47-with-new-r8-configuration-analyzer
url: https://developer.android.com/blog/posts/tinder-cuts-app-cold-starts-by-47-with-new-r8-configuration-analyzer
source: md.txt
---

[Case Studies](https://developer.android.com/blog/categories/case-studies)

# Tinder cuts app cold starts by 47% with new R8 Configuration Analyzer

4 min read ![](https://developer.android.com/static/blog/assets/Copy_of_ANDDM_TINDER_Strapi_d8536aec8a_j79Hm.webp) 18 Aug 2026 3 Authors [Ajesh Pai,](https://developer.android.com/blog/authors/ajesh-pai) [Ulises Uriel Verduzco Díaz ,](https://developer.android.com/blog/authors/ulises-uriel-verduzco-diaz) [Tracy Agyemang](https://developer.android.com/blog/authors/tracy-agyemang) Tinder is on a mission to power and inspire real connections by making meeting easy and fun for every new generation of singles. However, as their Android application codebase grew in size, so did its complexity. Prior to their latest optimization efforts, approximately 70% of the application was not optimized, carrying 17 dex files,including three dedicated just to startup. Although they had enabled R8, much of its optimization potential was blocked due to keep rules, and the team was unable to identify which specific rules were preventing optimization. To reduce startup time and decrease user-perceived Application Not Responding (ANR) errors, Tinder turned to the new R8 Configuration Analyzer to tackle these challenges.

By utilizing the [R8 Configuration Analyzer](https://developer.android.com/topic/performance/app-optimization/r8-configuration-analyzer), Tinder successfully identified and removed unintentional optimization blockers. The results were immediate and impactful: Tinder achieved a 47% reduction in app cold starts, shrank their app download size by 28.98% (down to 61.5 MB), and reduced user-perceived ANRs by 28%.

## **Configuration analyzer**

The [R8 Configuration Analyzer](https://developer.android.com/topic/performance/app-optimization/r8-configuration-analyzer) shows R8 optimization by tracking shrinking, optimization, and obfuscation scores to show available refinement areas. It shows the broad, redundant, or obsolete keep rules, including those from external libraries so that you can analyse the keep rule impact and refine the keep rules.

Key metrics shown in Configuration Analyzer include:

- **Shrinking Score:** Code percentage available for R8 shrinking.
- **Optimization Score:** Code percentage open to optimization (for example, method inlining, horizontal class merging).
- **Obfuscation Score:** Percentage of classes, methods and fields that can be renamed by R8 to decrease size.

Use the analyzer to audit keep rules and their impacts:

- **Find broad rules:** Narrow the scope of package-wide rules that restrict R8 optimization, and identify the specific classes, methods, and fields excluded from shrinking, optimization, and obfuscation.
- **Refine rules:** Target only specific classes/methods requiring reflection to unlock optimization
- **Remove redundant rules**: Remove rules that match zero classes, methods, or fields in your current build.
- **Identical rules**: Identical keep rules means rules that target the same classes, fields, and methods or duplicate declarations of keep rule in same or across keep rule files.
- **Find subsumed rules:** Clean up specific rules already covered by broader configurations.
- **Identify problematic libraries:** Check the combined optimization impact of merged consumer keep rules from all libraries.

![R8-Configuration-Analyzer-Screenshot.png](https://developer.android.com/static/blog/assets/R8_Configuration_Analyzer_Screenshot_f39649ce62_1brnaH.webp) R8 Configuration Analyzer report of a sample application

To assist you in using the R8 Configuration Analyzer with agentic tools, we have published an [R8 Analyzer skill](https://github.com/android/skills/blob/main/performance/r8-analyzer/SKILL.md). This skill optimizes automated development workflows by summarizing the R8 Configuration Analyzer report to display key metrics: optimization, obfuscation, and shrinking scores. It also highlights the five most impactful keep rules, giving you clear insight into what blocks code optimization.

## **Pinpointing hidden optimization blockers**

![image.png](https://developer.android.com/static/blog/assets/image_5ab49108cf_nz4Ei.webp)

Prior to integrating the R8 Configuration Analyzer, Tinder's Android app suffered from significant technical debt due to a heavily unoptimized codebase. This lack of optimization directly degraded the user experience, leading to users experiencing slow cold starts

To resolve these issues, the Tinder team utilized the R8 Configuration Analyzer to comprehensively audit their R8 configuration. The analyzer showed the R8 optimization of the codebase was around 28% even with R8 full mode. With R8 Configuration Analyzer, Tinder identified that an in-house library was introducing a broad, unscoped keep rule.

```kotlin
# Prevents optimization in all public classes along with all of their public and protected members

-keep public class * {
    public protected *;
}
```

This "wide" rule unintentionally covered various dependencies across the entire app, preventing optimization in a large number of classes. Because the over-inclusive rule prevented runtime crashes, developers frequently missed adding new rules for new features that used reflection, allowing hidden issues to compound over time.

By leveraging the insights provided by the R8 Configuration Analyzer, the team successfully traced and analyzed the specific classes affected by the broad keep rule from the library. The team immediately discovered that optimization was being blocked in larger, non-dynamically invoked classes where R8 could do optimization. Refining this specific keep rule allowed Tinder to unlock substantial optimization capabilities, untangle their legacy configurations, and drastically improve their overall optimization numbers, with R8 scores increasing from 28% to 50%, driving immediate performance gains across the application, and the Tinder team is actively working to further improve this figure.

- **Faster Loading:** The team achieved a 47% reduction on users experiencing slow cold starts of the app.
- **Smaller Footprint:** The App download size went from 86.6MB down to 61.5 MB (28.98% decrease).
- **Improved Stability:** User-perceived Application Not Responding (ANR) errors decreased from 0.35% to 0.28%, bringing them significantly closer to the peer median numbers
- **Reduced Complexity:** The total number of DEX files was cut down from 17 to 11, including just two startup files.

Beyond these technical performance enhancements, the increased application optimization directly translated into tangible business growth and higher user engagement, particularly in resource-constrained markets.

- **Regional Engagement:** Countries where Low RAM devices take a huge portion of the market, presented the largest increase in engagement, and decreasing the ANR rates was key to improving engagement in this vast market.
- **Engagement Growth:** Engagement has increased 3% since the increase in app optimization.

![image.png](https://developer.android.com/static/blog/assets/image_cae300b10c_ZK9gQO.webp)

## **Safeguarding future performance with continuous integration**

Addressing code minification isn't just a one-time fix; it requires continuous vigilance. Inspired by the massive gains achieved through the R8 Configuration Analyzer, Tinder's Android team proactively integrated optimization monitoring into their daily workflow to prevent regressions.

Tinder's team added a new job in their CI/CD pipeline to report changes in the optimization stats so everyone can see how their contribution is affecting optimization. When advising other developers considering R8 configuration integration, the team emphasizes the importance of auditing internal dependencies. While most popular third-party libraries come with well-defined rules, internal company projects that are considered "stable" might actually be introducing wide rules that negatively impact overall optimization.

## **Key Takeaways**

Faced with a heavily unoptimized codebase and a high volume of DEX files, Tinder needed a way to cleanly audit their app's minification rules. The R8 Configuration Analyzer provided the ideal tooling necessary to identify overly broad internal library rules, , the classes affected by the keep rule, allowing the team to confidently optimize their codebase. As a result, Tinder successfully cut cold starts by nearly half, shrank their APK size by over 28%, and established a healthier, more performant foundation for their users, with the team actively working to further improve these numbers.

## **How to Use R8 Configuration Analyzer**

The R8 Configuration Analyzer and its standalone features can be utilized based on your current Android Gradle Plugin (AGP) version:

**1. AGP 9.3 Release:** The R8 Configuration Analyzer is fully integrated and released with AGP 9.3. When running an R8 release build, the report will be generated in the **\`build/outputs/mapping/release/configanalyzer.html\`** folder.

**2. Standalone Gradle Task:** AGP 9.3 introduces a standalone Gradle task that allows you to generate the analyzer report without running a full release build, providing a much faster feedback loop when refining keep rules locally:

```
./gradlew :app:analyzeReleaseR8Config
```

The report is generated at `build/reports/r8/r8-config-analyzer-release.html.`

**3. Usage on Older AGP Versions:** If you are using a version below AGP 9.3, you do not need to migrate your entire AGP version to analyze your configuration. You can update the R8 version independently to 9.3.7-dev or higher by following the [Replacing R8 in AGP instructions](https://r8.googlesource.com/r8/+/refs/heads/main/README.md#replacing-r8-in-agp). To generate the report locally, run your build with the property specified:

```
./gradlew assembleRelease  -Dcom.android.tools.r8.dumpkeepradiushtmltodirectory=<output_directory>
```

To learn more, see the [R8 Configuration Analyzer](https://developer.android.com/topic/performance/app-optimization/r8-configuration-analyzer) documentation.
- [#Adaptive \& Differentiated](https://developer.android.com/blog/topics/adaptive-and-differentiated)
Written by:

-

  ## [Ajesh Pai](https://developer.android.com/blog/authors/ajesh-pai)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/ajesh-pai) ![View Ajesh Pai's profile](https://developer.android.com/static/blog/assets/Ajesh_R_Pai_fc75c62777_Z1G5g2B.webp) ![View Ajesh Pai's profile](https://developer.android.com/static/blog/assets/Ajesh_R_Pai_fc75c62777_Z1G5g2B.webp)
-

  ## [Ulises Uriel Verduzco Díaz](https://developer.android.com/blog/authors/ulises-uriel-verduzco-diaz)

  ###### Software Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/ulises-uriel-verduzco-diaz) ![View Ulises Uriel Verduzco Díaz 's profile](https://developer.android.com/static/blog/assets/IMG_20260209_160438_447c913f52_1MR7JL.webp) ![View Ulises Uriel Verduzco Díaz 's profile](https://developer.android.com/static/blog/assets/IMG_20260209_160438_447c913f52_1MR7JL.webp)
-

  ## [Tracy Agyemang](https://developer.android.com/blog/authors/tracy-agyemang)

  ###### Product Marketing Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/tracy-agyemang) ![View Tracy Agyemang's profile](https://developer.android.com/static/blog/assets/Tracy_Agyemang_Headshot_9a0c523435_1hBimO.webp) ![View Tracy Agyemang's profile](https://developer.android.com/static/blog/assets/Tracy_Agyemang_Headshot_9a0c523435_1hBimO.webp)
Continue reading
- 3 Authors 27 Aug 2026 27 Aug 2026 ![](https://developer.android.com/static/blog/assets/ANDDM_Passkeys_Strapi_2fc9df18a8_Z1oNucg.webp) [Case Studies](https://developer.android.com/blog/categories/case-studies)

  ## [How WhatsApp Upgraded to Secure, Seamless Sign-In for 1 Billion Users with Passkeys](https://developer.android.com/blog/posts/how-whats-app-upgraded-to-secure-seamless-sign-in-for-1-billion-users-with-passkeys)

  [arrow_forward](https://developer.android.com/blog/posts/how-whats-app-upgraded-to-secure-seamless-sign-in-for-1-billion-users-with-passkeys) WhatsApp is the world's largest messaging platform, serving billions of users globally. It is the default communication tool for people across diverse regions, connecting users through private, reliable, and secure messaging.
  [Niharika Arora](https://developer.android.com/blog/authors/niharika-arora), [Tracy Agyemang](https://developer.android.com/blog/authors/tracy-agyemang), [Mayank Jain](https://developer.android.com/blog/authors/blog-author) • 8 min read
  - [#Passkeys](https://developer.android.com/blog/topics/passkeys)
- [![View Thomas Ezan's profile](https://developer.android.com/static/blog/assets/thomas_ezan_d29c7508d0_l9O72.webp)](https://developer.android.com/blog/authors/thomas-ezan)[![View Tracy Agyemang's profile](https://developer.android.com/static/blog/assets/Tracy_Agyemang_Headshot_9a0c523435_1hBimO.webp)](https://developer.android.com/blog/authors/tracy-agyemang) 04 May 2026 04 May 2026 ![](https://developer.android.com/static/blog/assets/AANDDM_KARROT_Strapi_eed79b0e1b_cCxXk.webp) [Case Studies](https://developer.android.com/blog/categories/case-studies)

  ## [Gemini and Firebase AI Logic enabled Karrot to increase sales with a translation feature built in under 2 weeks](https://developer.android.com/blog/posts/gemini-and-firebase-ai-logic-enabled-karrot-to-increase-sales-with-a-translation-feature)

  [arrow_forward](https://developer.android.com/blog/posts/gemini-and-firebase-ai-logic-enabled-karrot-to-increase-sales-with-a-translation-feature) Karrot is a hyperlocal, community-driven peer-to-peer marketplace app that enables users to buy, sell, and trade items with other verified users. Since launching in South Korea in 2015, the platform has expanded into global markets, amassing over 43 million registered users.
  [Thomas Ezan](https://developer.android.com/blog/authors/thomas-ezan), [Tracy Agyemang](https://developer.android.com/blog/authors/tracy-agyemang) • 2 min read
  - [#Android](https://developer.android.com/blog/topics/android)
- [![View Ben Weiss's profile](https://developer.android.com/static/blog/assets/1_1_U4_K_Lr4r_A_Kx_Pq0_Crp_L3vr_Q_a4d1920594_2dcD9g.webp)](https://developer.android.com/blog/authors/ben-weiss)[![View Tracy Agyemang's profile](https://developer.android.com/static/blog/assets/Tracy_Agyemang_Headshot_9a0c523435_1hBimO.webp)](https://developer.android.com/blog/authors/tracy-agyemang) 30 Mar 2026 30 Mar 2026 ![](https://developer.android.com/static/blog/assets/monzo_boosts_performance_aff3a37917_6VY99.webp) [Case Studies](https://developer.android.com/blog/categories/case-studies)

  ## [Monzo boosts performance metrics by up to 35% with a simple R8 update](https://developer.android.com/blog/posts/monzo-boosts-performance-metrics-by-up-to-35-with-a-simple-r8-update)

  [arrow_forward](https://developer.android.com/blog/posts/monzo-boosts-performance-metrics-by-up-to-35-with-a-simple-r8-update) Monzo is a UK digital bank with 15 million customers and growing. As the app scaled, the engineering team identified app startup time as a critical area for improvement but worried it would require significant changes to their codebase.
  [Ben Weiss](https://developer.android.com/blog/authors/ben-weiss), [Tracy Agyemang](https://developer.android.com/blog/authors/tracy-agyemang) • 2 min read
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)