---
title: https://developer.android.com/stories/apps/reflectly
url: https://developer.android.com/stories/apps/reflectly
source: md.txt
---

# Reflectly quickly spins up a beautiful mobile experience on Android and iOS with Flutter

![](https://developer.android.com/static/images/cards/distribute/stories/Header-Flutter-Reflectly-min.png)

Reflectly uses artificial intelligence to help users structure and reflect on their daily thoughts and problems. Rather than a one-size-fits-all approach to journaling, Reflectly offers a personalized journal experience for each user, encouraging them to come back often and make mental health a part of their daily routine.

When Reflectly first launched on iOS, there was a significant interest in an Android version of the app. The small team faced many challenges supporting two platforms and providing a fast, consistent and beautiful experience to their growing user base. Given that Reflectly prides itself on its beautiful design and user experience, it was clear that the team needed to find a new solution.

## What They Did

Despite substantial issues, the Reflectly iOS app was quickly building a user base. Reflectly spent six months trying to fix their existing implementation before deciding to abandon the whole codebase and start from scratch.

Initially, the safest solution seemed to be to build two new native apps, but with only two engineers that approach just wouldn't work. "We could not afford to build a separate Android app, so we seriously considered shutting it down or abandoning it to focus on the iOS app," explained co-founder and CTO Daniel Vestergaard.

That's when the team discovered Flutter. "After experimenting with Flutter for a little while, the team fell in love with the cross-platform consistency, near-instant stateful hot reloading, great tooling and high performance of the platform," said CTO and co-founder Daniel Vestergaard. The team also appreciated Flutter's "easy, readable, and well-documented code," he added.

At that point, they decided to dive right in. Just 2.5 months after Reflectly's two engineers wrote their first line of Flutter code, Reflectly 2.0 began rolling out for both Android and iOS simultaneously. In that amount of time, they were not only able to completely rewrite the app, but they were also able to develop several large new features, such as their entire premium subscription implementation and a custom state management solution.  
![](https://developer.android.com/static/images/cards/distribute/stories/reflectlyscreennew.png)

## Results and Learnings

Reflectly 2.0 received a lot of positive feedback from users across a multitude of different Android and iOS devices, many of whom appreciated the app's new sleek look and design. After re-releasing the app with Flutter, the Android Reflectly app jumped from an**average 3.2-star rating on the Play Store to an average of 4.3**. It was also featured in Apple's list of "New Apps We Love." The team believes the original low rating was largely due to crashes, jank, and aesthetic inconsistencies, which they were able to solve with Flutter. "In summary, we largely attribute the improved average rating and hundreds of thousands --- possibly millions --- of Android downloads after \[the Flutter release\] to Flutter because it allowed us to retain the app, stabilize it, and have feature parity with iOS," says Vestergaard.

Because Flutter paints every pixel directly, the team didn't have to worry about rendering differences between platforms. They can now maintain a common codebase but still write iOS and Android-specific UI where appropriate. And now that they're able to dedicate their entire development team to a single, high-quality experience, Reflectly has seen a**50% decrease in development time**, allowing them to move from biweekly releases to weekly releases and launch new features on both platforms simultaneously.

## About Flutter

Anyone can build, test, and deploy beautiful apps for any screen from a single codebase with Flutter.[Get started today](https://flutter.dev/).