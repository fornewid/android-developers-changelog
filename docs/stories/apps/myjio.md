---
title: https://developer.android.com/stories/apps/myjio
url: https://developer.android.com/stories/apps/myjio
source: md.txt
---

# MyJio reduces customer complaints by lowering ANRs by 40%

MyJio is the gateway to the world of Jio products and services. It is the-one-stop destination for recharges, managing accounts \& Jio devices, UPI \& payments, entertainment services with movies, music, news, games, quizzes \& a lot more. With over 500Mn installs and 150Mn MAUs, MyJio is one of the largest apps in India.

Moreover, with the introduction of the JioPhone NEXT (Jio's low-cost 4G smartphone), a new user segment, recently migrated from feature phones, came into the pie.

Catering to such a huge user base, a performance issue affecting even 1% of users translates into 5 million users. The magnitude, thus, invited a dedicated effort in enhancing the app performance and user experience.

## The Challenge

MyJio's ANR and crash metrics were taking a hit due to the app being present in a large number of mid and low-end devices spread across Android versions. It was a challenge to provide a seamless customer experience while continuing to support a variety of devices, some of which were running on older and deprecated Android versions. It was also a priority for the team to ensure the app runs smoothly on the lowest end Android Go device.

Debugging took considerable time as the logs were limited in number and it was very difficult to reproduce the scenarios.

These challenges directly impacted MyJio's monetization strategy as well. An important area of focus was to make the journeys inside the app seamless and have lesser ANRs. This way users could recharge, generate leads, transact via UPI and various other activities without any hassle of the app not responding.

## How They Did It

To analyze the bottlenecks created by ANRs and crashes across various device hardware configurations, the MyJio team relied on Play Console, Android Studio (for development and debugging), Firebase Crashlytics, and more.

The team took a targeted approach to address the following issues -

- Identified Broadcast ANRs, Recompose ANRs, and ANRs due to rendering thread block on devices (particularly low memory devices).
- Observed Compose related ANRs which were hampering the rendering of Dashboard as per the stack trace.
- After observing ANRs on Play Console, they checked MyJio app on strict mode in Android Studio and proceeded to fix the issues one by one which were blocking on the main thread.
- Enabled velocity alerts error reporting on Firebase Crashlytics so that any anomalies get highlighted immediately.
- Integration of third party SDKs was watched closely so that they do not occupy the main thread for more than 300ms.

## Results

The MyJio team had to be mindful of the various device configurations while implementing these changes. They also had to take into account the influx of new users, upgrading from feature phones to the JioPhone NEXT 4G smartphone.  
![](https://developer.android.com/static/images/distribute/stories/MyJio.png)

The team achieved the following results -

- 20% reduction in user feedback with respect to app slowness, crashes and ANRs. This directly translated into improved session time of users by 15%
- Improvement in ANR rate by 40%
- Hot startup time improved by 70%
- Play Store ratings improved by 18%
- Improvement in session time by 15%

Team velocity and productivity are always on the rise, and seeing these improvements come to fruition boosted the team's morale even more.
> "The obsession to provide best-in-class services to users is a vision that is shared between Jio and Google. This partnership has helped us take the customer-centricity further with JioPhone Next; allowing a new digital revolution for an untapped set of users. With more \& more users being onboarded acrross demographics, devices and android versions, it becomes imperative that experience and optimisations be made for all users, especially the new entrants in the digital world."
>
> **-- Mohsin Abbas, VP - Head of Products \& Engineering for Customer \& Partner Channels, MyJio**