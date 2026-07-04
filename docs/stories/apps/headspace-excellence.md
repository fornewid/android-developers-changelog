---
title: https://developer.android.com/stories/apps/headspace-excellence
url: https://developer.android.com/stories/apps/headspace-excellence
source: md.txt
---

# Headspace&#39;s Android reboot increases monthly active users by 15%

Mindfulness doesn't happen in a vacuum --- it has a way of connecting to every other part of a person's life.[Headspace](https://play.google.com/store/apps/details?id=com.getsomeheadspace.android&gl=US), which created one of the world's first meditation apps and is now a leader in the mindfulness space, has been evolving recently with that holistic vision in mind. In 2019, they decided to expand their app beyond meditation and add new fitness and wellness features. Headspace realized that they would need a cross-functional team of engineers and designers to be able to deliver on the new product vision and create an[excellent app experience for users](https://android-developers.googleblog.com/2021/08/working-towards-android-app-excellence.html). An exciting new phase for the company: their design team started the process by creating prototypes for the new experience, with fresh new designs.

The only thing stopping Headspace from expanding their app and further broadening their user's horizons was their existing software architecture. It wasn't clearly structured enough to support all these new features. In fact, Headspace's development team projected that building on their current code would take longer than a complete rewrite. They decided to freeze development of their current Android app and dedicate themselves fulltime to a total overhaul.

## How they did it

Headspace's Android development team needed a convenient way to standardize how they built features. While immersing themselves in Google's literature on the latest, best practices for Android development and[app architecture](https://developer.android.com/jetpack/guide), they found their solution. Google recommended refactoring their app using[model-view-view-model](https://developer.android.com/jetpack/guide). MVVM is a widely supported software pattern that is progressively becoming industry standard because it allows developers to clearly separate areas of development, helping streamline an app's architecture. Choosing MVVM provided Headspace with a new set of standards and best practices that helped speed up development.

Another key resource from Google that the team drew on were the[Android Jetpack](https://developer.android.com/jetpack)libraries, including[Dagger](https://developer.android.com/training/dependency-injection/dagger-android)and[Hilt](https://developer.android.com/training/dependency-injection/hilt-android)for dependency injection. The new approach made boilerplate code smaller and more efficient, improving the team's productivity. They also took the opportunity to fully migrate their app to the Kotlin programming language. Using Kotlin, the team increased the test coverage in the app from approximately 15% to 80%. The increased test coverage resulted in faster deployments, higher quality code, and fewer crashes.

To make sure this improved user experience was reflected in their store listing reviews, Headspace implemented the[Google Play In-App Review API](https://developer.android.com/guide/playcore/in-app-review). This new API allowed them to encourage all users to share reviews of their Headspace experience from within the app. The implementation increased review scores, and, because store listing reviews are[tied to visibility on Google Play](https://developer.android.com/topic/performance/vitals), it also helped draw attention to the app's recent improvements. For a technical deep dive on Headspace's reboot, check out and share the[technical case study](https://android-developers.googleblog.com/2021/09/investing-in-app-excellence-headspaces.html)with your development team.

## Results

The team completed the rewrite in eight months, and they were able to deliver every feature from the design prototype. They met their initial goal of reaching new audiences in the fitness and wellness spaces, without compromising their reputation for quality. A new surge of reviews and subscriptions spoke to a better user experience and a happier user base.

Headspace's new focus on[Android App Excellence](https://developer.android.com/quality)yielded measurable improvements across all metrics.  
![](https://developer.android.com/static/images/distribute/stories/headspace-app-excellence.png)

The improvements to the quality of the app led to a 20% increase in paid subscriber parity between operating systems where their app is published, and the new approach to reviews drove an increase in their store listing reviews from 3.56 to 4.7 from Q2 to Q4 of 2020. Visibility from improved reviews combined with new features and an improved user experience lead to a 15% increase in monthly active users globally. Internally, the new architecture also allowed Headspace to create faster and more confident workflows for future development. Now, they spend a lot less time testing and fixing bugs, and more time implementing new features --- most recently, an improved retention flow, and optimizations to the upsell process. The rewrite also allowed better deep linking and marketing tool integration. This benefit gave Headspace's team the ability to gather better data from more users, respond directly to those who give feedback, and use this feedback to inform future development.

Headspace took the plunge and made a significant investment in Android App Excellence while opening up exciting new areas in fitness and wellness. With a strong new foundation for development and fresh feedback from their users, Headspace is well positioned to continue their mission: improve everyone's health and happiness.

## Get started

To discover how to rewrite your app to deliver a better user experience, see the[Headspace technical case study](https://android-developers.googleblog.com/2021/09/investing-in-app-excellence-headspaces.html). And, visit the[App Excellence landing page](https://developer.android.com/quality)to learn more about how consistent, intuitive app user experiences can grow your business.