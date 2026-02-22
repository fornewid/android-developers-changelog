---
title: https://developer.android.com/topic/performance/baselineprofiles/case-study-android-calendar
url: https://developer.android.com/topic/performance/baselineprofiles/case-study-android-calendar
source: md.txt
---

# How the Android Calendar team improved app startup and jank with Baseline Profiles

Baseline Profiles improve code execution speed by up to 30% by avoiding interpreter and just-in-time (JIT)[compilation steps](https://source.android.com/docs/core/runtime/jit-compiler#architectural-overview)for common user journeys. Baseline Profiles let you choose the user journeys you want to optimize and can help improve app startup, reduce jank, and more---which in turn result in improved business metrics, such as user retention and ratings.[Learn more about Baseline Profiles](https://developer.android.com/topic/performance/baselineprofiles/overview).

The Android Calendar team implemented Baseline Profiles and observed \~20% app startup time improvement and \~50% reduction in slow or frozen frames. Here's what they did end-to-end to achieve these performance wins, from why they decided to use Baseline Profiles to how they measured impact.

## Cloud Profiles v. Baseline Profiles

The Android Calendar team had already been using[Cloud Profiles](https://developer.android.com/topic/performance/baselineprofiles/overview#cloud-profiles), which are another Profile Guided Optimization (PGO) method based on real-world user interactions with the app. Here's how Cloud Profiles and Baseline Profiles compare:

|   Profile type    |       Set up       |               User journeys included               | Works best when user base is |   Impact realized    |     Supported Android versions      |
|-------------------|--------------------|----------------------------------------------------|------------------------------|----------------------|-------------------------------------|
| Cloud Profiles    | Enabled by default | Chosen automatically based on real-world user data | Large                        | Within a couple days | Android 9 (API level 28) and higher |
| Baseline Profiles | Configured by you  | Chosen by you                                      | All sizes                    | Immediate            | Android 7 (API level 24) and higher |

One key reason the Android Calendar team decided to add Baseline Profiles to their codebase was because they were moving to a faster, weekly release cycle. While Cloud Profiles provide significant performance gains, it takes 1-2 days after app launch for them to reach their peak impact because they rely on aggregating real-world user data. Supplementing Cloud Profiles with Baseline Profiles gives users more time to experience peak performance improvements before the next app version rolls out.

Additionally, it was important for the Android Calendar team to be able to choose which critical user journeys (CUJs) specifically are included in the profile, which you can do using Baseline Profiles.

Generally, we recommend using Baseline Profiles in addition to Cloud Profiles, enabled by default, for the best performance outcomes.

## User journeys included

The Android Calendar team chose to include two CUJs in their Baseline Profiles:

- Opening the app in schedule view: initially the default view, so important to optimize for users using the app for the first time or who don't change the default settings.
- Opening the app in month view: the chosen view for many users, based on user data. To track how users are using your app, you can use tools such as[Firebase](https://firebase.google.com/docs/analytics).

Generally, you should add the CUJs that are profitable for the business (if applicable) and CUJs that are most common. To learn more about how to choose CUJs to optimize, see[What to include](https://developer.android.com/topic/performance/baselineprofiles/overview#what-to-include).

## Implementation

The Android Calendar team uses an internal wrapper for the[Jetpack Macrobenchmark library](https://developer.android.com/topic/performance/baselineprofiles/measure-baselineprofile)to generate Baseline Profiles for ease of integration with internal tools and general scalability.

Here's the Macrobenchmark test configuration for opening the app in schedule view:  

    @Test
    fun generateProfile() =
        baselineProfileRule.collect(PACKAGE_NAME, includeInStartupProfile = true) {
            startActivityAndWait()
            // Verify pre-existing recurring events and tasks are shown.
            device.waitAndFindObject(By.text("Recurring event"), 20_000)
            device.waitAndFindObject(By.text("Recurring task"), 20_000)

            // Open drawer and verify selected view.
            device.findObject(By.desc("Show Calendar List and Settings drawer")).click()
            device.waitAndFindObject(By.desc("Schedule view, Selected"), 1_000)
        }

## Measure impact using controlled releases

Since Baseline Profiles are tightly coupled with the APK they're shipped with and incorporated before your app runs, it's not possible to run a standard A/B experiment to understand their impact. However, the Android Calendar team was able to get an accurate measure of impact using*controlled releases*, where you essentially release the new app version to only a subset of users and compare them to users who are on a version similar to the previous release.

With Baseline Profiles, they saw the following immediate, significant improvements in multiple areas. These stats are aggregated across a wide range of devices and across all users---those who start in schedule and month view likely gain the biggest benefits, but other users also benefit due to the optimization of shared processes such as loading calendar data from the database.

- Median interactive app startup (most common scenario) latency decreased from 775ms to 644ms (17%)
- Median cold start latency decreased from 1,058ms to 901ms (15%)
- Median warm start latency decreased from 453ms to 378ms (17%)
- Median janky frame rate decreased by 42-60% in schedule and month views

Keep in mind that if you use Cloud Profiles in conjunction with Baseline Profiles you'll likely see the improvements decrease slightly over the course of the first week, as Cloud Profiles are generated. However, you should still observe significant performance gains with Baseline Profiles on top of other optimizations you have in place.

To learn more about the tools and features, see the following resources:

- [About Baseline Profiles](https://developer.android.com/topic/performance/baselineprofiles/overview)
- [Benchmark Baseline Profiles with Macrobenchmark library](https://developer.android.com/topic/performance/baselineprofiles/measure-baselineprofile)