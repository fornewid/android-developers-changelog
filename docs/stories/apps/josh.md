---
title: https://developer.android.com/stories/apps/josh
url: https://developer.android.com/stories/apps/josh
source: md.txt
---

# Josh sees increased customer retention by improving app startup time by 30%

Josh is a made-in-India, short-video app launched in August 2020. It is also one of the fastest growing short-video apps in India with over 124 million MAUs and 60 million DAUs.

Optimizing Josh across a range of devices (high, mid, low end) and maintaining a standard experience across all of them is a tall order for any app developer, and the developers at Josh understood this from the very beginning. Improving Android Vitals was a major task in their sprints and importance was given to creating user delight by improving the app startup time and responsiveness.

App responsiveness and startup time were also important as video was the primary format users engaged with and consumed on the app. Any sputtering in the video stream or breaks in the different interactions could quickly result in the user losing interest and quitting the app.

By investing in app startup time performance, Josh improved app startup time by 30% for the average user and became 3x faster for \~10% users on older and low end devices.

### The Challenge

Josh app has witnessed a rapid pace of growth to over 100 million MAU in less than a year. Often in the race to push out product-led or event-led features, app optimization takes a back seat. App audits and structural feedback from Google helped them identify these issues early on and lay down a path to fix them.

### How They Did It

While monitoring Android vitals, an opportunity to improve app startup was identified. The team decided to prioritize improving the cold startup times, as this would automatically improve the warm and hot start times.

Using multiple custom traces, systrace, Android Studio Profiler and Perfetto, the team was able to do an extensive investigation and identify the bottlenecks. It was clear that the time taken by the Application class' onCreate and other synchronous methods could be optimized.

Here's what the team did specifically -

- Profiled every block of code that executes during App startup.
- Analyzed system traces using Android performance tools like Perfetto, Systrace, Dumpsys etc.
- Impact of 3rd party SDKs during app startup was investigated and autostart of some 3rd party SDKs was disabled.
- Eliminated legacy libraries
- Some modules were deferred and executed in the background
- Reduced the size of the drawables used on the splash screen on startup and optimized them for screen size

All the above were thoroughly validated by testing in isolation to confirm their positive impact on the app, emulating cold starts and integrating the new Jetpack[Macrobenchmark](https://developer.android.com/studio/profile/macrobenchmark-intro)library.

### Results

These changes didn't just lead to an immediate improvement across all the metrics, it also helped enhance overall user experience, along with invaluable learnings for the development team at Josh.

- Improving bounce rates and retention helped Josh**retain 1M+**users compared to the baseline. Focusing on these two metrics improved the overall engagement within the app as well.
- Play Store**ratings showed an upward positive trend**, post the launch of the app with startup improvements.
- App startup time improved by**30% for the average user and became 3x faster for \~10% users on older and low end devices**, thereby helping improve app responsiveness significantly for these users.

More importantly, this exercise in improving Android Vitals brought the whole team together, increasing the motivation of the team, especially the junior members. It cemented the importance of Vitals and even led to the team using some of the learnings in their other apps.
> *"When partners in an ecosystem come together, the ecosystem grows together. The power of data and analytics is unprecedented. As a creator-first, content-forward and consumer-focused platform, we have always focused on creating the ultimate user experience, which relies heavily on the app's stability. Josh witnessed immediate accelerated growth following its launch. Working closely with the Google Play team helped us identify and rectify challenges like app stability and optimization early on. Our efforts with Google have helped us drive improved stability and enhancements in user retention and engagement"*
>
> **-- Shailendra Sharma, SVP Product and Engineering, VerSe Innovation.**