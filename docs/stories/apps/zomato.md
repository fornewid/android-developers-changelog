---
title: https://developer.android.com/stories/apps/zomato
url: https://developer.android.com/stories/apps/zomato
source: md.txt
---

# Increasing app speed by 30%: a key ingredient in Zomato’s growth recipe

Zomato is an Indian multinational restaurant aggregator and food delivery company serving customers across 500 cities in India alone. With over 43M+ active customers and 1.5M+ average orders a day, it's one of the most popular food ordering and delivery services in the country. This also means customers use a varied range of devices and have differing network availability. Besides speedy deliveries, this also makes having a smooth and seamless experience on the app imperative.

Users expect fast[app open times and responsiveness](https://developer.android.com/topic/performance/vitals/launch-time). Improving this metric not only directly impacts the App Vitals, but ensures more order completions and supports Zomato's strategy - expanding to new markets and enabling a better experience on low to mid-range devices.This ultimately helps them capture their next billion users. App open times also act as a predictor for an increased funnel size as their users travel further down the sales funnel.

And Zomato got some impressive gains from focusing on App Vitals. For e.g., speeding up the app loading time by 30% led to an improvement in Day 1 customer retention by about 90% !

## The challenge

Zomato's rapid pace of development and focus on feature additions, albeit great for customers, resulted in a need to optimize their codebase and UX. While in pursuit of adding new features, Zomato wanted to keep their performance up to par as well. With multiple SDKs consuming resources that weren't always required, there was a need to streamline and rationalize the codebase.

All this was underpinned by Zomato's expansion into Tier 2 and Tier 3 cities in India, where people largely use low to mid tier devices with relatively limited processing capacity. With the inclusion of these devices the team had to ensure the same world class user experience as was in higher tier devices.

## What did they do?

Zomato used a simple rubric to analyze their overheads - which solution can give the best return on investment vs the effort by the development team. Using this rubric, the team started with a 4-month long optimization and improvement journey.

The first step was to look into the system traces to find issues, time-based analysis and prioritise accordingly.[Perfetto](https://perfetto.dev/)is the perfect tool to analyse, profile and trace Android processes. Zomato utilised the tool to trace all the SDKs being initialized during app startup and point out those that can be removed or loaded lazily.

Removing the legacy SDKs and unused 3P libraries was the top priority as it was a low-effort, high-gain task. This approach helped Zomato in saving precious 20% in the app startup time.

Many third-party libraries use content providers to initialise on the app start, which affects the app startup time. Zomato uses Facebook SDK for login, but the user also has other login options, so initialising the SDK at the startup is inefficient. With the introduction of the[App Startup library](https://developer.android.com/topic/libraries/app-startup), Zomato only loads the SDK if the user is going for the Facebook login option. This helped them in reducing startup time by \~6%!

The next step was improving the inflation time of the views as the rendering and inflation of the view itself can take a significant time in a complex UI structure like Zomato's.[Viewstub](https://developer.android.com/reference/android/view/ViewStub)helps in increasing the efficiency as it allows views to be created but not added to the view hierarchy unless required. Viewstubs are more efficient than using View. GONE as even if the view is in GONE state, it will be getting inflated and will eat up memory and CPU usage. Zomato flattened their view hierarchy and merged layouts along with viewstubs in their login activity. These changes significantly improved the inflation time by 7%.

Android profiler helped in optimising memory usage, as it allows tracking CPU activity, memory and network in real-time. The profiler enabled them to identify the root issue for the locking situations and memory overheads and fix it accordingly. Zomato also worked on their caching mechanism to achieve a massive drop of 60% in out of memory issues.

|                  Action                  | Before (sec) | After (sec) | Improvement |
|------------------------------------------|--------------|-------------|-------------|
| Removed legacy SDKs, unused 3P libraries | 4.873        | 3.813       | 21.74%      |
| Lazy loading libraries                   | 3.814        | 3.577       | 6.2%        |
| Layout improvements, viewstubs           | 2.529        | 2.348       | 7.15%       |

*App startup time = App initialization + Libraries load time + View inflation time*

## Results

Zomato's performance gains helped them create a much smoother experience. Further UI improvements and caching, reduced the janking too.  
![](https://developer.android.com/static/images/distribute/stories/zomato.png)

App to homepage (clicking on the app icon to a fully loaded and usable homepage) is a key business metric that Zomato tracked internally. After the improvements were implemented, they saw a meaningful uptick in this metric. Customers that landed on a fully loaded page increased by about 20% during this period.

**This led to an improvement in Day 1 customer retention by about 90%!**These improvements had a trickle down effect on their forward funnels as well - the overall order through rate (home -\> menu -\> cart -\> order) improved by \~1.5 percentage points i.e around 600K orders MoM.

According to Firebase performance's cold startup metric, there was an improvement of 25% on average, and for low/mid end devices, the cold app startup time improvement reached up to 30%.

App startup time performance is an important metric affecting user perception and investing efforts to optimize performance can lead to a significant impact on the business as well.
> "At Zomato, providing and building towards an amazing customer experience has always been at the center of our ideology. We believe performance is one of the key levers and hence our team strived towards engineering excellence to improve app load times using Google's developer tools and saw substantial results in real time. With this, we hope to provide a blazing fast app for India's online ordering needs and set a benchmark for our future development."
>
> **--- Sajal Gupta, Engineering Manager, Zomato**