---
title: https://developer.android.com/stories/apps/duolingo-excellence
url: https://developer.android.com/stories/apps/duolingo-excellence
source: md.txt
---

# Duolingo refactors on Android with MVVM and Jetpack libraries

Duolingo is the world's most popular language learning app because it's managed to make something people have found daunting in the past feel easy and fun. This breezy language experience requires a constant stream of new features and experiments --- and a smooth-running app that can deliver all of them. To Duolingo, an unresponsive app on a device anywhere in the world could mean a potentially discouraged learner. This commits them to app excellence, particularly on the Android devices used by sixty percent of their learners, including their CEO, who keeps track of the app from an entry-level phone. And so, when Duolingo's Android development team noticed an increase in "App not Responding" errors, dropped frames --- and even received hand-written complaints --- they took action immediately.

They soon uncovered the source of the app's performance issues: the existing software architecture wasn't scaling well with the growth of their team. Necessary updates were causing painful performance regressions on the app. Their developers were devoting more time to fixing bugs, and less to shipping new revenue-generating features. Their outdated software architecture was starting to become an unacceptable drag --- on them, their team velocity, and, above all, on their users' experience. They needed to rebuild their codebase from the ground up.

## How they did it

At the beginning, the team was torn. Should this be their sole priority now? One group felt that it was more important to continue shipping new features and driving revenue, while the other believed that focusing all their attention on an Android reboot was the way forward. Eventually, they reached the consensus that the increasing effort of fighting regressions risked derailing their road map entirely. They had to go all-in.

The team settled on an increasingly popular solution. They decided to rewrite their app using[Model-View-ViewModel](https://developer.android.com/jetpack/guide?gclid=Cj0KCQjw6s2IBhCnARIsAP8RfAj6I4mhRRdSqjYfPlvGET9S6mmRGJrc8Inkc-cCe1IVdTDEvlE3hFEaApHkEALw_wcB&gclsrc=aw.ds), a software pattern supported by Google that allows developers to streamline an app's architecture by creating clear separation of concerns. With MVVM, they could separate the development of the graphical user interface (the view) from the development of the business logic (the model). They could establish clear and agreed upon patterns, making it easier to both align their approach to new features and onboard incoming developers.

Breaking each feature into its own modular piece allowed the team to quickly regain productivity, as they could assign small groups to work on each feature in parallel, increasing velocity while reducing errors.

They implemented this new architecture with libraries from Android's[Jetpack](https://developer.android.com/jetpack), including[Dagger](https://developer.android.com/training/dependency-injection/dagger-basics)and[Hilt](https://developer.android.com/training/dependency-injection/hilt-android), to help them write code that works consistently across Android versions and devices. These two additions enabled them to create better encapsulated features and[utilize Android's built-in modules more efficiently](https://developer.android.com/training/dependency-injection).

## Results

These performance gains significantly improved learners' experience on Android and in particular on entry-level devices. They also led to a more responsive app with smoother animations on flagship devices. The daily "App Not Responding" or ANR rate dropped 41%. The percentage of time that the app fell below its target frame rate decreased by 28%. Most importantly, their users experienced a 40% increase in speed when scrolling through key screens.

![](https://developer.android.com/static/images/distribute/stories/duolingo-supporting-chart.jpg)  
*Hands holding notes reading 41% less ANRs, 28% improved frame rate and 40% faster experience.*

<br />

The whole reboot took eight weeks and made the app considerably more engaging and delightful for all Duolingo learners. In the six months since, the team has recorded no significant new performance regressions, allowing them to focus again on shipping revenue-generating features. The decision to focus the team's efforts on quality had paid off.

Duolingo's dedication to their mission made them the world's top app in the language learning space. Their commitment to app excellence --- creating cutting edge educational experiences without compromising accessibility --- is what kept them there.

## Get started

If you feel like diving into the nitty-gritty of how Duolingo integrated Jetpack's libraries, and how Model-View-ViewModel improved their app, read our[technical case study](https://android-developers.googleblog.com/2021/08/android-app-excellence-duolingo.html)for developers.