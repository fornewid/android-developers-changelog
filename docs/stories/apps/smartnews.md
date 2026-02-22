---
title: https://developer.android.com/stories/apps/smartnews
url: https://developer.android.com/stories/apps/smartnews
source: md.txt
---

# SmartNews reduces lines of code by 20% and improves team morale with Kotlin

![](https://developer.android.com/static/images/distribute/stories/smartnews-logo.png)

[SmartNews](https://play.google.com/store/apps/details?id=jp.gocro.smartnews.android)helps millions of people discover their world everyday by sharing timely news from a diverse set of news sources. The company was founded in 2012 in Japan, and it now has over 50 million downloads globally.

In June 2019, the team saw Android development moving towards Kotlin first and decided to start testing Kotlin themselves. They wanted to take advantage of Kotlin-first Jetpack libraries, reduce the amount of code they had to maintain, and benefit from Kotlin's expressive and easy-to-understand syntax.

## What they did

The team at SmartNews is well versed in Java, so it was fairly easy for them to start writing in Kotlin. As Kotlin is 100% interoperable with Java, they could easily start writing new features such as[Weather Radar and News From All Sides](https://about.smartnews.com/en/2020/09/17/20200917/)in Kotlin, while working in their existing codebase. They used coroutines to manage image downloading and caching within the patented Weather Radar feature. Coroutine dispatchers provide a useful abstraction for managing tasks, and this helped the SmartNews engineers avoid the pitfalls that come from managing raw threads.

The team also refactored some of their Java code, and was impressed with Kotlin's null safety features. Kotlin's syntax for identifying mutability, nullability, and initialization helped the team catch errors early on, and**reduced the amount of time to review code changes by 10%**. Using Kotlin's succinct and efficient syntax, they were also able to increase the readability of their codebase, which has made their code easier to maintain as the company continues to grow.

## Results

Writing in Kotlin has**improved their overall productivity from implementation to launch** . The biggest improvement they saw was that writing in Kotlin**reduced their converted lines of code by 20%**. Approximately half of the SmartNews app is currently in Kotlin, and the development team plans on writing all new features in Kotlin as well as refactoring some of their existing code in order to continue increasing their code maintainability.

As the development team was implementing Kotlin and reducing boilerplate code, they noticed an**increase in team morale** . The team was excited to be able to express their ideas in a more efficient way, and have their code be more readable for the future. Hideo Ohashi, the Engineering Manager for SmartNews noticed**Kotlin has helped their engineering recruiting efforts** .*"The most frequent questions from candidates are 'are you using Kotlin? How often do you use it?' It seems now that many engineers are interested in migrating to Kotlin and want to support it."*While these improvements in team morale and recruitment were not the main reasons the team adopted Kotlin, these positive changes will help the company as it continues to grow in this competitive industry.

## Get started

Learn more about[developing an Android app with Kotlin](https://developer.android.com/kotlin).