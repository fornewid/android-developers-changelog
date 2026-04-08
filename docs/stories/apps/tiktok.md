---
title: https://developer.android.com/stories/apps/tiktok
url: https://developer.android.com/stories/apps/tiktok
source: md.txt
---

# TikTok Optimizes User Experience with Android Tools

[TikTok](https://play.google.com/store/apps/details?id=com.zhiliaoapp.musically), the world's community-driven entertainment destination, brings over 1 billion people together from around the world to discover, create and share content they love.

A diverse user base requires various network conditions and device specifications, and all users want a seamless, responsive app experience regardless of which device they use.

If TikTok is slow to load, or playbacks get stuck, users will get frustrated and abandon the app altogether. To avoid this, TikTok relies on data monitoring, peer app comparison and user surveys to track the overall app performance. The team also adopted profiling tools like[Systrace](https://developer.android.com/topic/performance/tracing)and[Simpleperf](https://developer.android.com/ndk/guides/simpleperf), to reduce UI jank, playback lags and network issues. While this has been working well, the engineering team was looking to take it one step further and uncover the underlying factors affecting the performance and develop an optimization plan with quantifiable performance indicators.

## How they did it

TikTok's goal was to achieve a faster startup speed and ensure a more seamless playback and user experience. To meet these goals, the team used Android development tools to find areas of improvement and refine them.

To reduce TikTok's startup time, the team refactored the startup framework based on Android[Jetpack's App Startup library](https://developer.android.com/topic/libraries/app-startup).

To ensure a smoother user interface, the team used the[Layout Inspector](https://developer.android.com/studio/debug/layout-inspector)in[Andriod Studio](https://developer.android.com/studio)to simplify their View hierarchy and remove excessive content. TikTok developed a strategy to spread complex tasks across different frames to ensure consistent frame rates while the app is running.

Video playback is at the core of TikTok's app experience. The team reused player instances and utilized preloading/pre-rendering to create quick and seamless transitions from watching one video then switching to another.

## Results

The TikTok team has been using[Android performance tools](https://developer.android.com/topic/performance)for over a year to track, quantify, and optimize all of their performance factors. Many of the app's performance indicators have seen significant improvement, including:

- The app startup time was reduced by 45%
- A 49% decrease in jank, dropped or frozen frames in user experience - the first frame when playing a video now appears 41% faster and video lag has been reduced by 27%

With an improved user experience, more people are now using TikTok. Session duration has gone up and users are more likely to stay active in the app with the active days per user in 30 days increasing by 1%. User surveys and app ratings have also pointed to a significant increase in overall user satisfaction.

By shifting their focus on achieving[Android App Excellence](https://developer.android.com/quality)and targeting the latest platform release, Android 13, the team continuously improves the user experience, leading more people to share and consume content.

With more than 250 million large screen Android devices currently in use globally, the team is also focusing on growing their large-screen device adoption to bring a more immersive TikTok experience for users in the near future.

## Get Started

To learn more about how the TikTok team optimized their app based on performance data and improved the overall app experience using Android tools, please read our[technical case study](https://android-developers.googleblog.com/2022/08/precise-improvements-how-tiktok-enhanced-its-social-experience-on-android.html)for developers.