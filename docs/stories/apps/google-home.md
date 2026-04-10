---
title: https://developer.android.com/stories/apps/google-home
url: https://developer.android.com/stories/apps/google-home
source: md.txt
---

# Google Home reduces #1 cause of crashes by 33%

![](https://developer.android.com/static/images/distribute/stories/google-home-icon.png)

The[Google Home app](https://play.google.com/store/apps/details?id=com.google.android.apps.chromecast.app&hl=en_US)helps set up, manage, and control your Google Home, Google Nest, and Chromecast devices---plus thousands of connected home products like lights, cameras, thermostats, and more.

The engineering team behind the Google Home app benefits from using Kotlin and Android Jetpack libraries to boost engineering productivity and developer happiness.

## What they did

The Google Home team decided to incorporate Kotlin into their codebase to make programming more productive and to enable the usage of modern language features like var/val, smart casts, coroutines, and more.**As of June 2020, about 30% of the codebase is written in Kotlin**, and Kotlin development is encouraged for all new features.

The team also adopted Jetpack libraries to improve developer velocity, decrease the need for boilerplate code maintenance, and reduce the necessary amount of code. Jetpack libraries also helped make their code more testable, since there are clearer functional boundaries and APIs.

## Results

*"Efficacy and writing less code that does more is the 'speed' increase you can achieve with Kotlin." - Jared Burrows, Software Engineer on Google Home*

Switching to Kotlin resulted in a reduction in the amount of required code, compared to the equivalent of existing Java code. One example is the use of data classes and the Parcelize plugin:**a class which was 126 hand-written lines in Java can now be represented in just 23 lines in Kotlin---an 80% reduction.**Additionally, equality and parcelizing methods can be automatically generated and kept up to date. Many nested loops and filtering checks were also simplified using the functional methods available in Kotlin.

Because Kotlin can make nullability a part of the language, tricky situations can be avoided, like when inconsistent usage of nullability annotations in Java might lead to a missed bug.**Since the team started migrating to developing new features with Kotlin, they saw a 33% decrease in NullPointerExceptions** . Since this is the[most common crash type on Google Play Console](https://developer.android.com/topic/performance/vitals/crash#prevent-crashes-null-pointer), reducing them led to a dramatically improved user experience.

With a large, mature app like Google Home---which has over a million lines of code---it's helpful to be able to gradually add Jetpack libraries. Incorporating them allowed the team to consolidate and replace custom tailored solutions, sometimes even with a single library. Since Jetpack libraries can help engineers follow best practices and be less verbose (for example, using[Room](https://developer.android.com/training/data-storage/room)or[ConstraintLayout](https://developer.android.com/training/constraint-layout)), readability was increased as well. The team considers many of the newer Jetpack libraries 'must-haves,' including[ViewModel](https://developer.android.com/topic/libraries/architecture/viewmodel)and[LiveData](https://developer.android.com/topic/libraries/architecture/livedata), both of which are used extensively in the Google Home codebase.

The Google Home app team found the Jetpack KTX integrations with Kotlin coroutines to be especially helpful. The team is now able to avoid tricky asynchronous programming bugs by associating coroutines with lifecycle-aware components like[ViewModel](https://developer.android.com/topic/libraries/architecture/viewmodel).

*Java is a registered trademark of Oracle and/or its affiliates.*

## Get Started

Learn more about[writing Android apps in Kotlin](https://developer.android.com/kotlin)and[using Android Jetpack libraries](https://developer.android.com/jetpack).