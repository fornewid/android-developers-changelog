---
title: https://developer.android.com/blog/posts/datadog-delivers-millions-of-in-depth-performance-insights-with-profiling-manager
url: https://developer.android.com/blog/posts/datadog-delivers-millions-of-in-depth-performance-insights-with-profiling-manager
source: md.txt
---

#### [Case Studies](https://developer.android.com/blog/categories/case-studies)

# Datadog delivers millions of in-depth performance insights with ProfilingManager

###### 4-min read

![](https://developer.android.com/static/blog/assets/ANDDM_TITLE_Strapi_b83ae0beee_i9nEs.webp) 08 Jun 2026 3 Authors

##### [Alice Yuan,](https://developer.android.com/blog/authors/alice-yuan)
[Arti Arutiunov,](https://developer.android.com/blog/authors/arti-arutiunov)
[Nikita Ogorodnikov](https://developer.android.com/blog/authors/nikita-ogorodnikov)

Performance regressions are notoriously hard to reproduce, making regressions a massive bottleneck for mobile developers. Although signals like ANR rates indicate *what* issues occur in production, pinpointing the specific line of code that resulted in the performance issue has historically necessitated exhaustive manual reproduction or speculative trial-and-error experimentation.

Datadog collaborated with Google to mitigate this frustration by integrating the ProfilingManager API (available on Android 15+ devices) into its Real User Monitoring (RUM) and Continuous Profiling platforms. This integration transforms the debugging workflow, allowing developers to move beyond surface-level symptoms to being able to detect the *why* behind a performance bottleneck.

By leveraging this system-level API, Datadog now processes millions of production profiles weekly across the globe according to Datadog internal data of June 2026. It provides engineering teams with a new level of visibility into real-world performance, all while maintaining a low runtime overhead for production-scale performance monitoring.

## The impact of ProfilingManager

ProfilingManager is a system service introduced in Android 15 that enables apps to programmatically collect performance data such as call stack samples, field traces and memory heap dumps directly from production environments. This capability shifts the engineering paradigm from reactive manual reproduction to proactive field analysis.
![AANDDM_DataDog_Quote_01.png](https://developer.android.com/static/blog/assets/AANDDM_Data_Dog_Quote_01_06bf636466_Z25J28N.webp)

For example, a Google communications app used field traces to investigate why its cold start times were slower on newer, more powerful hardware. By diving into the field-collected traces and comparing traces across different device types, the engineer discovered a hidden scheduling issue: a background text-to-speech service was unnecessarily being prewarmed during app startup. The traces revealed that this background process was monopolizing the device's highest-performing big CPU core, forcing the app's main thread to sleep while the prewarm occurred.

## Solving the Android code-level visibility challenge

Prior to the implementation of ProfilingManager, Datadog's Real User Monitoring (RUM) focused on high-level application health and session-level telemetry to assess the user journey. Engineering teams could monitor Android performance signals like time to initial display, ANR rates, CPU load, and frozen frames. These insights extended to granular interactions, such as network latency, touch events, and main thread hangs. However, while this data effectively highlighted which performance bottlenecks were surfacing in the field, it provided no clear path to identifying the root cause of these failures.
![AANDDM_DataDog_Quote_02.png](https://developer.android.com/static/blog/assets/AANDDM_Data_Dog_Quote_02_769d993429_O8qPO.webp)

To address this, Datadog needed a profiling engine capable of capturing Android traces directly from devices in production with minimal performance impact. After evaluating alternative approaches, such as writing their own trace processor using Android Debug APIs, the team selected ProfilingManager because it is the most performant solution of the profiling options they evaluated and offloads the sampling decisions overhead to the OS.

ProfilingManager supports a wide range of collection methods, including CPU traces, call stack sampling, memory analysis through Java heap dumps and native heap profiles. It enables developers to profile production builds, upload trace files to external storage, and review them in the Perfetto trace analyzer UI. As a SaaS provider, Datadog uploads, visualizes, and analyzes these profiles collected via its SDK, providing a unified view of application health.

By centralizing high-fidelity telemetry within a unified observability API, ProfilingManager empowers Datadog and its clients to proactively monitor, investigate, and remediate complex Android performance regressions through key technical advantages:

- **Granular session diagnostics:** ProfilingManager enhances debuggability by delivering direct OS-level trace data, overcoming the visibility and alignment challenges typical of custom logging with system services. To dive deeper, developers can download these traces from Datadog to investigate further in visualization tools like the [Perfetto UI](https://ui.perfetto.dev/).
- **Automated telemetry triggers:** By leveraging native system events to initiate trace recordings at key optimization points, Datadog reduces the need to build custom collection logic. While the initial rollout focuses on the [APP_FULLY_DRAWN](https://developer.android.com/reference/android/os/ProfilingTrigger?_gl=1*xix6h8*_up*MQ..*_ga*MTc4ODI2NDgwMy4xNzc5MzE2ODcw*_ga_6HH9YJMN9M*czE3NzkzMTY4NzAkbzEkZzAkdDE3NzkzMTY4NzAkajYwJGwwJGgyMTE1NzIyNjk1#TRIGGER_TYPE_APP_FULLY_DRAWN) signal, there are already plans to expand this observability to include [ANR](https://developer.android.com/reference/android/os/ProfilingTrigger?_gl=1*1hl4p7n*_up*MQ..*_ga*MTc4ODI2NDgwMy4xNzc5MzE2ODcw*_ga_6HH9YJMN9M*czE3NzkzMTY4NzAkbzEkZzAkdDE3NzkzMTY4NzAkajYwJGwwJGgyMTE1NzIyNjk1#TRIGGER_TYPE_ANR), [OOM](https://developer.android.com/reference/android/os/ProfilingTrigger?_gl=1*8x3pd*_up*MQ..*_ga*MTc4ODI2NDgwMy4xNzc5MzE2ODcw*_ga_6HH9YJMN9M*czE3NzkzMTY4NzAkbzEkZzAkdDE3NzkzMTY4NzAkajYwJGwwJGgyMTE1NzIyNjk1#TRIGGER_TYPE_OOM), and [COLD_START](https://developer.android.com/reference/android/os/ProfilingTrigger?_gl=1*1ezx2ma*_up*MQ..*_ga*MTc4ODI2NDgwMy4xNzc5MzE2ODcw*_ga_6HH9YJMN9M*czE3NzkzMTY4NzAkbzEkZzAkdDE3NzkzMTY4NzAkajYwJGwwJGgyMTE1NzIyNjk1#TRIGGER_TYPE_COLD_START) triggers.
- **Proactive trace snapshots:**By interfacing directly with the system-level Perfetto service (traced), ProfilingManager utilizes a proactive background recording model designed to capture unpredictable issues. This ensures that developers receive a precise visualization of the events leading up to a performance anomaly, offering a level of insight that exceeds what is possible through manual instrumentation.
- **Bottleneck detection at scale:**Datadog is able to synthesize telemetry from across Datadog's global customer base to uncover regressions that only emerge under unique hardware configurations and variable network environments.
- **System-enforced resource stability:**The API leverages sampling trace collection to ensure performance and user experience impacts remain unnoticeable.
- **On-device data controls:**ProfilingManager filters out irrelevant information from other processes on-device before the profile is delivered to the app. This minimizes file sizes and ensures that only data relevant to the app's processes is provided.

## Processing millions of weekly profiles to optimize real-world apps

![datadog-profiling-blogpost-final.png](https://developer.android.com/static/blog/assets/datadog_profiling_blogpost_final_971624974a_jE6t9.webp) An example of Datadog's time to initial display measurement with stack sampling powered by ProfilingManager

Integrating a system-level profiling API into a global monitoring SDK required solving infrastructure challenges. Because ProfilingManager generates highly detailed performance traces, the Datadog engineering team had to build a pipeline capable of parsing and analyzing these profiles on the server side at scale. Beyond profile collection, Datadog also emphasizes the importance of balancing sampling frequency with collecting enough data to generate meaningful insights about your application. Datadog relies on ProfilingManager's built-in rate limiting as a critical stability safeguard, preventing excessive telemetry requests from overburdening user devices.

The team has been profiling Datadog's own native Android application and a number of early adopters' applications for months, gathering millions of profiles to ensure a fast, error-free launch experience and to refine their performance-detection algorithms. Today, the production integration seamlessly scales across a variety of Android devices.

## Conclusion

By integrating Android's ProfilingManager API, Datadog successfully closed the visibility gap between backend systems and mobile client applications for their customers. By processing millions of profiles weekly with negligible device overhead, Datadog equips Android developers with the code-level insights necessary to diagnose complex performance bugs instantly, helping developers build smoother applications and improve their app's performance signals in the Play Store. To adopt the ProfilingManager API directly into your performance observability framework, check out our [documentation](https://developer.android.com/topic/performance/tracing/profiling-manager/overview).

In the future, Datadog aims to make Android profiling data a first-class input for coding agents to autonomously resolve performance bottlenecks, closing the feedback loop between detection and remediation. Datadog is working toward making Android profiling broadly accessible to developers.

To get started using the Datadog real user monitoring feature powered by ProfilingManager, visit[Datadog Mobile Real User Monitoring](https://www.datadoghq.com/dg/real-user-monitoring/android-profiling/?utm_source=inbound&utm_medium=corpsite-display&utm_campaign=int-rum-ww-blog-announcement-announcement-androidprofilerblog2026).
- [#Profiling Manager](https://developer.android.com/blog/topics/profiling-manager)
- [#Android](https://developer.android.com/blog/topics/android)
- [#Performance](https://developer.android.com/blog/topics/performance)

###### Written by:

-

  ## [Alice Yuan](https://developer.android.com/blog/authors/alice-yuan)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/alice-yuan) ![](https://developer.android.com/static/blog/assets/Alice_Yuan_552a4dd4ee_ZlDEgJ.webp) ![](https://developer.android.com/static/blog/assets/Alice_Yuan_552a4dd4ee_ZlDEgJ.webp)
-

  ## [Arti Arutiunov](https://developer.android.com/blog/authors/arti-arutiunov)

  ###### Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/arti-arutiunov) ![](https://developer.android.com/static/blog/assets/arti_a_profile_blog_bbf00f0087_1Nh5K.webp) ![](https://developer.android.com/static/blog/assets/arti_a_profile_blog_bbf00f0087_1Nh5K.webp)
-

  ## [Nikita Ogorodnikov](https://developer.android.com/blog/authors/nikita-ogorodnikov)

  ###### Staff Software Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/nikita-ogorodnikov) ![](https://developer.android.com/static/blog/assets/nickolay_profile_blog_4e456d6b31_Z1NuT0q.webp) ![](https://developer.android.com/static/blog/assets/nickolay_profile_blog_4e456d6b31_Z1NuT0q.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/thomas_ezan_d29c7508d0_l9O72.webp)](https://developer.android.com/blog/authors/thomas-ezan)[![](https://developer.android.com/static/blog/assets/Tracy_Agyemang_Headshot_9a0c523435_1hBimO.webp)](https://developer.android.com/blog/authors/tracy-agyemang) 04 May 2026 04 May 2026 ![](https://developer.android.com/static/blog/assets/AANDDM_KARROT_Strapi_eed79b0e1b_cCxXk.webp)

  #### [Case Studies](https://developer.android.com/blog/categories/case-studies)

  ## [Gemini and Firebase AI Logic enabled Karrot to increase sales with a translation feature built in under 2 weeks](https://developer.android.com/blog/posts/gemini-and-firebase-ai-logic-enabled-karrot-to-increase-sales-with-a-translation-feature)

  [arrow_forward](https://developer.android.com/blog/posts/gemini-and-firebase-ai-logic-enabled-karrot-to-increase-sales-with-a-translation-feature) Karrot is a hyperlocal, community-driven peer-to-peer marketplace app that enables users to buy, sell, and trade items with other verified users. Since launching in South Korea in 2015, the platform has expanded into global markets, amassing over 43 million registered users.

  ###### [Thomas Ezan](https://developer.android.com/blog/authors/thomas-ezan), [Tracy Agyemang](https://developer.android.com/blog/authors/tracy-agyemang) •
  2 min read

  - [#Android](https://developer.android.com/blog/topics/android)
- 3 Authors 02 Jun 2026 02 Jun 2026 ![](https://developer.android.com/static/blog/assets/Engineering_Memory_Blog_Strapi_3_bfd74f43e5_Z2i8kF7.webp)

  #### [How-tos](https://developer.android.com/blog/categories/how-tos)

  ## [Prioritizing Memory Efficiency: Essential Steps for Android 17](https://developer.android.com/blog/posts/prioritizing-memory-efficiency-essential-steps-for-android-17)

  [arrow_forward](https://developer.android.com/blog/posts/prioritizing-memory-efficiency-essential-steps-for-android-17) While app performance is often equated with a smooth UI and fast start times, memory serves as the silent foundation upon which these visible metrics are built. It's no secret that we're seeing a shift where device memory is more important than ever.

  ###### [Alice Yuan](https://developer.android.com/blog/authors/alice-yuan), [Ajesh Pai](https://developer.android.com/blog/authors/ajesh-pai), [Fung Lam](https://developer.android.com/blog/authors/fung-lam) •
  10 min read

  - [#Memory](https://developer.android.com/blog/topics/memory)
  - [#Android](https://developer.android.com/blog/topics/android)
  - [#Performance](https://developer.android.com/blog/topics/performance)
  - +1 ↩
- [![](https://developer.android.com/static/blog/assets/Garan_Jenkin_0529dbfef9_Z2crRat.webp)](https://developer.android.com/blog/authors/garan-jenkin) 15 May 2026 15 May 2026 ![](https://developer.android.com/static/blog/assets/cross_device_discovery_to_score_record_Wear_OS_adoption_Strapi_2f9244f1db_Z23QTbE.webp)

  #### [Case Studies](https://developer.android.com/blog/categories/case-studies)

  ## [How FotMob leveraged cross-device discovery to score record Wear OS adoption](https://developer.android.com/blog/posts/how-fot-mob-leveraged-cross-device-discovery-to-score-record-wear-os-adoption)

  [arrow_forward](https://developer.android.com/blog/posts/how-fot-mob-leveraged-cross-device-discovery-to-score-record-wear-os-adoption) FotMob recently experienced its largest single-day increase on Wear OS among its installed audience in 5 years, at 2-3x the daily average. The secret? A simple cross-device installation flow that helps users discover their Wear OS app directly from their phone.

  ###### [Garan Jenkin](https://developer.android.com/blog/authors/garan-jenkin) •
  3 min read

  - [#Wear OS](https://developer.android.com/blog/topics/wear-os)

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)