---
title: https://developer.android.com/develop/ui/compose/adopt/for-large-teams
url: https://developer.android.com/develop/ui/compose/adopt/for-large-teams
source: md.txt
---

# Adopt Compose for teams

![](http://developer.android.com/static/images/spot-icons/jetpack-compose.svg)  

### Technical decision makers: Adopt Compose for your teams

Jetpack Compose is a declarative UI toolkit that accelerates Android app development, helps developers be more productive, eliminates common bugs, and enables intuitive app design.

Android is invested in the continued development of Jetpack Compose as many developers love it, including Googlers. Several Google teams are using Jetpack Compose, including the[Play Store](https://android-developers.googleblog.com/2022/03/play-time-with-jetpack-compose.html).

## How to get started

A best practice for tool adoption is to learn as a team, and to designate a champion to lead this learning effort. This person would act as a subject matter expert and would help build up the expertise of other team members. Other resources for getting started are listed below.  
Guide

### [Start with Kotlin](http://developer.android.com/kotlin/adopt-for-large-teams)

Compose makes heavy use of many of the great language benefits of Kotlin, and we suggest starting to migrate to Kotlin before jumping in with Compose.  
Guide

### [Migrate to a declarative approach](http://developer.android.com/develop/ui/compose/mental-model)

The industry has been shifting toward declarative UI frameworks, such as Jetpack Compose, which eliminate common bugs and simplify adding animations.Learning pathway

### [Start learning as a team](http://developer.android.com/courses/pathways/compose)

Start learning together using our in-depth course that covers intermediate and advanced topics, and encourage knowledge sharing along the learning journey.  
Guide

### [Design to high standards](https://developer.android.com/develop/ui/compose/designsystems/material3)

Compose components adhere to Material Design (or to your own custom design system), and Compose supports themes.

### Three approaches to integrating Compose

Compose is[fully interoperable](https://developer.android.com/develop/ui/compose/interop)with Android's view system so you don't have to completely rewrite your app to benefit from Compose. This allows you to take advantage of your existing resources, and gives you flexibility on how to add Compose into an existing app. There are three common approaches to consider:![](http://developer.android.com/static/develop/ui/compose/images/adopt-for-teams/new-features.png)  

### Write new features in Compose.

The most common approach is to start by writing new features in Compose. This approach has a lot of flexibility because you can use Compose for complete new screens, all the way down to an individual piece of UI such as a button. Twitter took this approach for their Communities feature.  
[See Twitter's Compose story](https://www.youtube.com/watch?v=7N9rKu7l_5U)![](http://developer.android.com/static/develop/ui/compose/images/adopt-for-teams/replace-simple-screens.png)  

### Replace simple screens.

Identifying a few of the more simple screens in your app as a starting point for migration is an easy way to start taking advantage of the benefits of Compose. This is an approach Monzo took when they were starting to dive into Compose.  
[See Monzo's Compose story](http://developer.android.com/stories/apps/monzo-compose)![](http://developer.android.com/static/develop/ui/compose/images/adopt-for-teams/redesign-ui.png)  

### Redesign your UI.

If you're already planning a major UI redesign for your app, it might make more sense to do the full UI update in Compose. Typically teams build out UI components in Compose and then create screens from those components. The Mercari team took this approach.  
[See Mercari's Compose story](http://developer.android.com/stories/apps/mercari)

## Focus on features

[![](http://developer.android.com/static/images/picto-icons/code.svg)](http://developer.android.com/develop/ui/compose/animation/introduction)  

### [Animate with a few lines of code](http://developer.android.com/develop/ui/compose/animation/introduction)

Compose supports linear and tweened animations, animations with custom keyframes, and even dynamic spring animations.  
[Discover Compose animations](http://developer.android.com/develop/ui/compose/animation/introduction)  
[![](http://developer.android.com/static/images/logos/android-studio.svg)](http://developer.android.com/develop/ui/compose/tooling#preview)  

### [Preview in Android Studio](http://developer.android.com/develop/ui/compose/tooling#preview)

With composables, you can set and review properties like size, locale, or light and dark mode as you work.  
[Learn about Preview](http://developer.android.com/develop/ui/compose/tooling#preview)  
[![](http://developer.android.com/static/images/picto-icons/phone.svg)](http://developer.android.com/develop/ui/compose/tooling#live-edit)  

### [See changes in real time](http://developer.android.com/develop/ui/compose/tooling#live-edit)

With Live Edit, you can see changes you make to a composable immediately on an emulator or device -- there's no need to rebuild your app.  
[Learn about Live Edit](http://developer.android.com/develop/ui/compose/tooling#live-edit)  
[![](http://developer.android.com/static/images/picto-icons/test-tube-2.svg)](http://developer.android.com/develop/ui/compose/testing)  

### [Test with semantics](http://developer.android.com/develop/ui/compose/testing)

Because Compose defines your UI with functions, you can test screens to buttons with the same APIs. Confidently significant updates to your app and test to confirm your features still work.  
[Test in Compose](http://developer.android.com/develop/ui/compose/testing)