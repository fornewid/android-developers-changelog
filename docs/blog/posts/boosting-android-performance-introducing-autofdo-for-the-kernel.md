---
title: https://developer.android.com/blog/posts/boosting-android-performance-introducing-autofdo-for-the-kernel
url: https://developer.android.com/blog/posts/boosting-android-performance-introducing-autofdo-for-the-kernel
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news)

# Boosting Android Performance: Introducing AutoFDO for the Kernel

4 min read ![](https://developer.android.com/static/blog/assets/P_Mguide_a86dec5079_cjxF5.webp) 10 Mar 2026 [![View Charles Munger's profile](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_Z1SMg9h.svg)](https://developer.android.com/blog/authors/yabin-cui) [Yabin Cui](https://developer.android.com/blog/authors/yabin-cui) Software Engineer We are the Android LLVM toolchain team. One of our top priorities is to improve Android performance through optimization techniques in the LLVM ecosystem. We are constantly searching for ways to make Android faster, smoother, and more efficient. While much of our optimization work happens in userspace, the kernel remains the heart of the system. Today, we're excited to share how we are bringing [Automatic Feedback-Directed Optimization (AutoFDO)](https://research.google/pubs/autofdo-automatic-feedback-directed-optimization-for-warehouse-scale-applications/) to the Android kernel to deliver significant performance wins for users.

## What is AutoFDO?

During a standard software build, the compiler makes thousands of small decisions, such as whether to inline a function and which branch of a conditional is likely to be taken, based on static code hints.While these heuristics are useful, they don't always accurately predict code execution during real-world phone usage.  

AutoFDO changes this by using real-world execution patterns to guide the compiler. These patterns represent the most common instruction execution paths the code takes during actual use, captured by recording the CPU's branching history. While this data can be collected from fleet devices, for the kernel we synthesize it in a lab environment using representative workloads, such as running the top 100 most popular apps. We use a sampling profiler to capture this data, identifying which parts of the code are 'hot' (frequently used) and which are 'cold'. When we rebuild the kernel with these profiles, the compiler can make much smarter optimization decisions tailored to actual Android workloads.  

To understand the impact of this optimization, consider these key facts:

- On Android, the kernel accounts for about 40% of CPU time.
- We are already using AutoFDO to optimize native executables and libraries in the userspace, achieving about 4% cold app launch improvement and a 1% boot time reduction.

### Real-World Performance Wins

We have seen impressive improvements across key Android metrics by leveraging profiles from controlled lab environments. These profiles were collected using app crawling and launching, and measured on Pixel devices across the 6.1, 6.6, and 6.12 kernels.  

The most noticeable improvements are listed below. Details on the AutoFDO profiles for these kernel versions can be found in the respective Android kernel repositories for [android16-6.12](https://android.googlesource.com/kernel/common/+/refs/heads/android16-6.12/gki/aarch64/afdo/) and [android15-6.6](https://android.googlesource.com/kernel/common/+/refs/heads/android15-6.6/android/gki/aarch64/afdo/) kernels.
![boosting_2.png](https://developer.android.com/static/blog/assets/boosting_2_9a4c45f66e_Z1XF848.webp)

These aren't just theoretical numbers. They translate to a snappier interface, faster app switching, extended battery life, and an overall more responsive device for the end user.

## How It Works: The Pipeline

Our deployment strategy involves a sophisticated pipeline to ensure profiles stay relevant and performance remains stable.
![boosting_3.png](https://developer.android.com/static/blog/assets/boosting_3_46277fc83c_Z1FMME1.webp)

#### **Step 1: Profile Collection**

While we rely on our internal test fleet to profile userspace binaries, we shifted to a controlled lab environment for the [Generic Kernel Image (GKI)](https://source.android.com/docs/core/architecture/kernel/generic-kernel-image). Decoupling profiling from the device release cycle allows for flexible, immediate updates independent of deployed kernel versions. Crucially, tests confirm that this lab-based data delivers performance gains comparable to those from real-world fleets.

- **Tools \& Environment:** We flash test devices with the latest kernel image and use [**simpleperf**](https://android.googlesource.com/platform/system/extras/+/refs/heads/android16-qpr2-release/simpleperf/doc/) to capture instruction execution streams. This process relies on hardware capabilities to [record branching history](https://android.googlesource.com/platform/prebuilts/simpleperf/+/refs/heads/mirror-goog-main-prebuilts/doc/collect_etm_data_for_autofdo.md), specifically utilizing [**ARM Embedded Trace Extension (ETE)**](https://developer.arm.com/documentation/102856/0100/Embedded-Trace-Extension?lang=en) and [**ARM Trace Buffer Extension (TRBE)**](https://developer.arm.com/documentation/102856/0100/Trace-Buffer-Extension) on Pixel devices.
- **Workloads:** We construct a representative workload using the top 100 most popular apps from the [**Android App Compatibility Test Suite (C-Suite)**](https://android.googlesource.com/platform/test/app_compat/csuite/). To capture the most accurate data, we focus on:
  - [**App Launching**](https://developer.android.com/topic/performance/vitals/launch-time)**:** Optimizing for the most visible user delays
  - [**AI-Driven App Crawling**](https://developer.android.com/studio/test/other-testing-tools/app-crawler)**:** Simulating contiguous, evolving user interactions
  - **System-Wide Monitoring:** Capturing not only foreground app activities, but also critical background workloads and inter-process communications
- **Validation:** This synthesized workload shows an **85% similarity** to execution patterns collected from our internal fleet.
- **Targeted Data:** By repeating these tests sufficiently, we capture high-fidelity execution patterns that accurately represent real-world user interaction with the most popular applications. Furthermore, this extensible framework allows us to seamlessly integrate additional workloads and benchmarks to broaden our coverage.

#### **Step 2: Profile Processing**

We post-process the raw trace data to ensure it is clean, effective, and ready for the compiler.

- **Aggregation:** We consolidate data from multiple test runs and devices into a single system view.
- **Conversion:** We [convert](https://android.googlesource.com/platform/prebuilts/simpleperf/+/refs/heads/mirror-goog-main-prebuilts/doc/collect_etm_data_for_autofdo.md#a-complete-example_kernel) raw traces into the AutoFDO profile format, filtering out unwanted symbols as needed.
- **Profile Trimming:** We trim profiles to remove data for "cold" functions, allowing them to use standard optimization. This prevents regressions in rarely used code and avoids unnecessary increases in binary size.

#### **Step 3: Profile Testing**

Before deployment, profiles undergo rigorous verification to ensure they deliver consistent performance wins without stability risks.

- **Profile \& Binary Analysis:** We strictly compare the new profile's content (including hot functions, sample counts, and profile size) against previous versions. We also use the profile to build a new kernel image, analyzing binaries to ensure that changes to the text section are consistent with expectations.
- **Performance Verification:** We run targeted benchmarks on the new kernel image. This confirms that it maintains the performance improvements established by previous baselines.

#### **Continuous Updates**

Code naturally "drifts" over time, so a static profile would eventually lose its effectiveness. To maintain peak performance, we run the pipeline continuously to drive regular updates:

- **Regular Refresh:** We refresh profiles in [Android kernel LTS branches](https://source.android.com/docs/core/architecture/kernel/android-common) ahead of each GKI release, ensuring every build includes the latest profile data.
- **Future Expansion:** We are currently delivering these updates to the `android16-6.12` and `android15-6.6` branches and will expand support to newer GKI versions, such as the upcoming `android17-6.18`.

## **Ensuring Stability**

A common question with profile-guided optimization is whether it introduces stability risks. Because AutoFDO primarily influences compiler heuristics, such as function inlining and code layout, rather than altering the source code's logic, it preserves the functional integrity of the kernel. This technology has already been proven at scale, serving as a standard optimization for Android platform libraries, ChromeOS, and Google's own server infrastructure for years.

To further guarantee consistent behavior, we apply a "conservative by default" strategy. Functions not captured in our high-fidelity profiles are optimized using standard compiler methods. This ensures that the "cold" or rarely executed parts of the kernel behave exactly as they would in a standard build, preventing performance regressions or unexpected behaviors in corner cases.

## **Looking Ahead**

We are currently deploying AutoFDO across the `android16-6.12` and `android15-6.6` branches. Beyond this initial rollout, we see several promising avenues to further enhance the technology:

- **Expanded Reach:** We look forward to deploying AutoFDO profiles to newer GKI kernel versions and additional build targets beyond the current `aarch64` support.
- **GKI Module Optimization:** Currently, our optimization is focused on the main kernel binary (`vmlinux`). Expanding AutoFDO to GKI modules could bring performance benefits to a larger portion of the kernel subsystem.
- **Vendor Module Support:** We are also interested in supporting AutoFDO for vendor modules built using the [Driver Development Kit (DDK)](https://android.googlesource.com/kernel/build/+/refs/heads/main/kleaf/docs/ddk/main.md). With support already available in our build system ([Kleaf](https://android.googlesource.com/kernel/build/+/refs/heads/main/kleaf/docs/kleaf.md)) and profiling tools ([simpleperf](https://android.googlesource.com/platform/prebuilts/simpleperf/+/refs/heads/mirror-goog-main-prebuilts/doc/collect_etm_data_for_autofdo.md#A-complete-example_kernel-module-using-DDK)), this allows vendors to apply these same optimization techniques to their specific hardware drivers.
- **Broader Profile Coverage:** There is potential to collect profiles from a wider range of Critical User Journeys (CUJs) to optimize them.

By bringing AutoFDO to the Android kernel, we're ensuring that the very foundation of the OS is optimized for the way you use your device every day.
Written by:

-

  ## [Yabin Cui](https://developer.android.com/blog/authors/yabin-cui)

  ###### Software Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/yabin-cui) ![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_Z1SMg9h.svg) ![View Charles Munger's profile](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_Z1SMg9h.svg)
Continue reading
- [![View Roxanna Aliabadi Walker's profile](https://developer.android.com/static/blog/assets/roxana_02dc1d3afc_1Q1ceg.webp)](https://developer.android.com/blog/authors/roxanna-walker) 21 Oct 2026 21 Oct 2026 ![](https://developer.android.com/static/blog/assets/1009_ABL_142_A_more_reliable_way_to_add_and_edit_contacts_on_Android_Strapi_b510ec4fc0_ZXfljU.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [A more reliable way to add and edit contacts on Android](https://developer.android.com/blog/posts/reliable-way-to-add-and-edit-contacts-android)

  [arrow_forward](https://developer.android.com/blog/posts/reliable-way-to-add-and-edit-contacts-android) Apps that target the upcoming Android release will no longer be able to directly write to contacts with the WRITE_CONTACTS permission.
  [Roxanna Aliabadi Walker](https://developer.android.com/blog/authors/roxanna-walker) • 6 min read
  - [#Android](https://developer.android.com/blog/topics/android)
- [![View Jason Buchel's profile](https://developer.android.com/static/blog/assets/unnamed_25_28af9250eb_I4mHO.webp)](https://developer.android.com/blog/authors/jason-buchel) 13 Oct 2026 13 Oct 2026 ![](https://developer.android.com/static/blog/assets/Blog_0140_strapi_8d85f71a6e_ZvGJv2.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Bringing our latest frontier model to Android Developers](https://developer.android.com/blog/posts/bringing-gemini-4-argon-to-android-agentic-engineering-antigravity-cli)

  [arrow_forward](https://developer.android.com/blog/posts/bringing-gemini-4-argon-to-android-agentic-engineering-antigravity-cli) As agentic development accelerates, Android engineering is reaching an exciting new frontier: moving from assistive code completion to agents executing end-to-end under your direction. You have total choice and flexibility in the models and agents you use.
  [Jason Buchel](https://developer.android.com/blog/authors/jason-buchel) • 3 min read
  - [#Agentic Android development](https://developer.android.com/blog/topics/agentic-android-development)
- [![View Paul Feng's profile](https://developer.android.com/static/blog/assets/paul_feng_759ac95845_ZnD5Di.webp)](https://developer.android.com/blog/authors/paul-feng) 13 Oct 2026 13 Oct 2026 ![](https://developer.android.com/static/blog/assets/Developer_Strapi_Banner_2000x1000_c21932c96a_1wEPmN.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [New ways to drive smarter discovery, deeper engagement, and business growth on Google Play](https://developer.android.com/blog/posts/google-play-discovery-engagement-growth)

  [arrow_forward](https://developer.android.com/blog/posts/google-play-discovery-engagement-growth) Today, we shared how we're taking our "more than a store" vision into its next chapter. From You tab, now the personal home base for over 250M monthly active users, to our unified gaming platform connecting over 700M gamer profiles, Google Play is meeting users wherever they are.
  [Paul Feng](https://developer.android.com/blog/authors/paul-feng) • 3 min read
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1zVtXW.webp)