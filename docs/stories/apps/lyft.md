---
title: https://developer.android.com/stories/apps/lyft
url: https://developer.android.com/stories/apps/lyft
source: md.txt
---

# Lyft improves Android app startup time for drivers by 21%

![](https://developer.android.com/static/images/cards/distribute/stories/AppExcellenceLyftBusinessCaseStudy_V2_Header_4209x1253.png)

[Lyft](https://www.lyft.com/)is committed to app excellence. They have to be. For a rideshare app --- providing a vital, time-sensitive service to millions of drivers and riders every day --- a slow or unresponsive app adds unacceptable friction. To keep things running smoothly, Lyft's development team keeps a close eye on app performance. That's how they noticed that their Android driver app had a slow startup time.

In an organization with so many time-sensitive priorities, every project has to be weighed out carefully. The development team knew that slow start-up time was affecting their customers' experience, but, if they wanted to do something about it, they first needed to demonstrate the extent of the problem to senior leadership. This required making a clear business case.

## What They Did

Using[Android vitals](https://play.google.com/console/about/vitals/), Lyft's development team discovered that Lyft Driver's startup time was 15--20% slower than comparable applications in the ridesharing space. This is what they needed to make a case to their leadership.

Having tabulated the extent of the problem, they estimated that one single developer working for one month could make significant improvements to the app's startup time --- a worthwhile investment that their leadership couldn't refuse.

With support from leadership, they now needed to locate the impasse itself. They reviewed the app's startup process and broke it down into phases.  
![](https://developer.android.com/static/images/cards/distribute/stories/AppExcellenceLyftBusinessCaseStudy_V2_InlineGraphic_02.png)

The app started smoothly; UI rendering proceeded as expected; but then, in the third phase --- the bootstrapping phase, where the app connects to the network and requests data to render the home screen --- they found the bottleneck.

The team moved quickly to resolve it, removing unnecessary network calls, moving some to execute asynchronously, and caching data between sessions.

## Results and Learnings

These relatively simple improvements led to a dramatic 21% average reduction in app startup time and a 5% increase in driver sessions. The initial experiment proved that a modest investment in app excellence could yield valuable results. Seeing this, Lyft leadership has expanded the initiative and have commited to address other challenges including app stability.  
![](https://developer.android.com/static/images/cards/distribute/stories/AppExcellenceLyftBusinessCaseStudy_V2_InlineGraphic_01.png)

To read more technical details about how Lyft improved the Lyft Driver Android app, read our technical case study.

## About Android Vitals and App Discoverability in Google Play

- Google Play considers app startup time a key determinant of app quality.
- Android vitals allows product owners to understand and track historical performance of key metrics for their apps on real devices.
- In the Google Play Console, product owners can ensure their app is best in class by comparing aggregated performance data against other apps in their category.
- Android vitals allows you to compare metrics including: app-not-responding (ANR) rates, crash rates, rendering performance, and app startup time, among others.
- App startup time is an important metric of user experience. An app which is slow or unresponsive during startup may frustrate users or lose their attention altogether.