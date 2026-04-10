---
title: https://developer.android.com/stories/apps/google-duo
url: https://developer.android.com/stories/apps/google-duo
source: md.txt
---

# Google Duo sees increased engagement and improved ratings by optimizing for larger screens

[Google Duo](https://play.google.com/store/apps/details?id=com.google.android.apps.tachyon)is a simple, high quality video calling app for everyone. With the increase of people being at home during the Covid-19 pandemic, the Duo team saw a significant increase in people using the app to stay connected with friends \& family, school and work. The team strives to build great experiences across all platforms and surfaces, and saw an opportunity to improve the experience for tablets and foldable devices given the huge growth of these devices in the market, and the prevalence of them amongst Duo users.  
*Google Duo on the Samsung Galaxy Z Fold2*

## What they did

The team started by thinking about the unique experience they can provide users with foldables. They wanted to design for each[posture](https://developer.android.com/guide/topics/ui/foldables#postures)to make sure the app experience is optimal across them.*"All of our support is within the same application, we configure for different devices based on different widths and heights." - Oren Freiberg, Software Engineer*

As one of the first optimizations, they removed all small buttons from the middle of the screen to avoid users having to press buttons within the crease, using the[WindowManager](https://developer.android.com/reference/androidx/window/WindowManager)and[FoldingFeature](https://developer.android.com/reference/androidx/window/FoldingFeature)Jetpack libraries to redesign the UI and create a tabletop experience for calls. This enabled callers to be shown on the top screen of the foldable, while the bottom screen displayed all of the controls and menu items, which is a**huge improvement for the user experience.**  
![](https://developer.android.com/static/images/distribute/stories/duo-before-after-tabletop.png)

After this, the team thought about user interactions with Duo across all screen sizes. While swiping to answer a call works really well on a phone, the development team learned through testing that this didn't work as well on a tablet or foldable. Some Duo users were unintentionally answering phone calls and having to hang up quickly. The team optimized the larger screen experience by implementing buttons on tablets, and dual sliding pucks on foldables.The team was closely monitoring behavior changes as part of this UI improvement, and saw a**decrease in unintentional brief calls on these devices, as well as an increase in call time**on these devices. This UI tweak enabled Duo's users to have a more seamless calling experience.  
![](https://developer.android.com/static/images/distribute/stories/duo-before-after-tablet.png)

## Results

The investment in optimizing for tablets and foldables led to a better experience for users on larger screens, which led to an**improvement in the average app ratings for optimized tablets by half a point.**App engagement improved as well as call time on tablets and foldables increased after these changes. Upgrading the experience and look \& feel was critical to the business as communication apps are taking off on larger screens, and it's important to optimize these experiences to stay competitive. The Duo team plans on continuing to optimize the experience across all form factors.

## Get Started

Learn more about how you can get started with[optimizing your app for larger screens](https://developer.android.com/guide/topics/ui/nff-overview).