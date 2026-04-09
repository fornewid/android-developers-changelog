---
title: https://developer.android.com/stories/apps/tinder
url: https://developer.android.com/stories/apps/tinder
source: md.txt
---

# Tinder solves dating-app pain points with Android Architecture Components

![](https://developer.android.com/static/images/distribute/stories/tinder-logo.png)

[Tinder](https://tinder.com)is the world's most popular app for meeting new people. Known for changing how people meet and date, it empowers users to swipe right to connect and chat with others. Tinder sparks over 26 million matches a day, with more than 20 billion matches made since their launch in 2012.

The company needed to scale up the[app](https://play.google.com/store/apps/details?id=com.tinder)quickly, based on user demand, but their database implementation was left over from their early days, making it increasingly more complicated to expand upon. They also had a view-heavy architecture to reduce lifecycle complexities, but needed to know which lifecycle events were specific to an activity. They lacked a consistent framework for handling tasks such as marshalling[`Cursor`](https://developer.android.com/reference/android/database/Cursor)objects into domain objects, making database migrations, or consistently performing queries.

## What they did

![Image of a profile](https://developer.android.com/static/images/distribute/stories/tinder-screenshot.svg)**Figure 1:**A photo of a photographer on Tinder

Tinder turned to[Android Architecture Components](https://developer.android.com/topic/libraries/architecture)for solutions for upgrading their code. They used[`Lifecycle`](https://developer.android.com/reference/androidx/lifecycle/Lifecycle)to let a[`View`](https://developer.android.com/reference/android/view/View)observe its host activity's lifecycle, and they used[`LifecycleObserver`](https://developer.android.com/reference/androidx/lifecycle/LifecycleObserver)to facilitate a decentralized plugin architecture and to prevent bloat in[`Presenter`](https://developer.android.com/reference/androidx/leanback/widget/Presenter),[`Activity`](https://developer.android.com/reference/android/app/Activity), and[`View`](https://developer.android.com/reference/android/view/View)objects. The[Room persistence library](https://developer.android.com/topic/libraries/architecture/room)provided a turnkey method for defining, managing, and querying their local database.

The Tinder development team was able to implement the[`LifecycleObserver`](https://developer.android.com/reference/androidx/lifecycle/LifecycleObserver)and plugin architecture in only two weeks, while seamlessly implementing Room for their internal Ads SDK took just two days.
> "We no longer had to invest significant time managing the Activity Lifecycle inside of plugins or views," says Andy Lawton, Head of Android at Tinder. "Room's design is well- thought-out and makes our persistence layer easy to implement. Using Room for the internal Ads SDK probably saved a week of time in upfront development."

## Results

Tinder was so pleased with their results with their Ads SDK that they're migrating their entire database layer to Room. Testing was easy, and Room's protection against forgetting to unregister something reduced memory leaks. Android Architecture Components is also helping to produce smaller memory footprints.
> "Android Architecture Components has provided a prescription for solving many of the pain points that developers face at all different scales," Lawton says. "Through the use of lifecycle-aware components, Tinder has managed to improve developer productivity, testability, and modularity, while being conducive to a view-first architecture. Room eliminates the need for other solutions for managing SQLite, and turns database management and querying into an exercise in configuration."

## Metric

**500+** lines of code removed from`MainActivity`via[`LifecycleObserver`](https://developer.android.com/reference/androidx/lifecycle/LifecycleObserver)/ plugin architecture

## Get started

Android Architecture Components is open to all developers as part of Android Jetpack.[Get started with Android Architecture Components](https://developer.android.com/topic/libraries/architecture).