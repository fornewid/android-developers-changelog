---
title: https://developer.android.com/stories/instant-apps/vimeo
url: https://developer.android.com/stories/instant-apps/vimeo
source: md.txt
---

# Vimeo increases session duration by 130% with instant apps

![](https://developer.android.com/static/images/distribute/stories/vimeo-icon.png)

[Vimeo](https://play.google.com/store/apps/details?id=com.vimeo.android.videoapp&hl=en_GB)was founded by a group of filmmakers who wanted to share their creative work and personal moments from their lives. Today, Vimeo has over 240 million viewers worldwide, with nine million installs on Google Play, and a growing audience for its new Android TV application. With mobile driving over fifty percent of Vimeo's onsite visitors, the mobile video player experience is a critical piece of the Vimeo user journey.

Vimeo sees the highest engagement in their native installed app, so they wanted to implement Android Instant Apps to enable users to enter their immersive native app experience through a single tap.

## What did they do

Vimeo enabled instant app support by reducing their 15MB installed app down to a 4MB feature module. They identified most of the size savings by using the[APK analyzer](https://developer.android.com/studio/debug/apk-analyzer.html), removing unused libraries, and replacing their image caching library with a smaller library. They then shifted towards a dependency injection architecture for their core player, which had significant size savings.

Vimeo leveraged two other technologies to round out the experience -[Smart Lock](https://get.google.com/smartlock/)and[Branch.io](https://branch.io/). Smart Lock enabled automatic authentication of a user in the instant app, so users could leave comments on videos and save them to watch later. Branch.io was used to ensure that when a user in an instant app chose to install the native app, they were taken to the exact same video they were viewing within the instant app---bypassing things like onboarding and registration and making the experience truly seamless. To the user, it's like they never left.

Learn more about[how Vimeo developed their instant app](https://medium.com/vimeo-engineering-blog/vimeo-android-instant-apps-2f8b1e94760c)on their technical blog.

## Results

![](https://developer.android.com/static/images/distribute/stories/vimeo-stats.png)

Vimeo's instant app has the familiar look and feel of their fine-tuned Android experience. Since launching in May 2017, Vimeo has seen sessions more than double in length (+130% increase) and native app users increase 20%. Relative to their mobile website, Vimeo's instant app has a less aggressive strategy for calls to install, yet it has the same install rate (\~10%). This provides a smoother first-time user experience without sacrificing installs.

Jon Sheldrick, Vimeo's Director of Product Management, responsible for driving the instant apps implementation, is planning to expand Vimeo's instant app footprint:

*"The process of getting a user from mobile web into a native app for the first time is an antiquated experience that is ripe for disruption. Instant Apps is the first technology to address this issue head-on, and the results have been fantastic. We have seen a 20% month over month increase in total native app users. While this is just trading one form of traffic for another (mobile web vs. instant app), this is a trade we love to make, because native app users are far more likely to register and return to Vimeo.*

*Now that we've proven the concept with an instant app video player, we're interested in exploring other components of our native app that can be modularized. We're considering subscriber check-out flows, search, and authentication as additional features that can add to a constellation of instant experiences that eventually make the transition from web into a native experience completely seamless."*

## Get started

As of May 2017, Android Instant Apps is open to all developers.[Get started with instant apps](https://developer.android.com/topic/instant-apps).