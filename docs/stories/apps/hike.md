---
title: Hike Messenger gains speed and simplicity with Android Architecture Components  |  Developer stories  |  Android Developers
url: https://developer.android.com/stories/apps/hike
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Developer stories](https://developer.android.com/stories)

# Hike Messenger gains speed and simplicity with Android Architecture Components Stay organized with collections Save and categorize content based on your preferences.



![](/static/images/distribute/stories/hike-logo.webp)

Launched in 2012, Hike is building products with the aim of simplifying the
internet to bring India online. Hike combines chat, messaging, feeds,
and integrations with third-party transportation and payment apps.
It developed these features very rapidly and at different points in
time, resulting in what the company called "significant technical and
architectural debt." Because this debt was becoming a bottleneck to
stability, maintainability and performance, the company wanted to simplify
its code quickly.

## What they did

Hike turned to [Android Architecture Components](/jetpack/arch), which
became "our Swiss army knife to tackle all of these challenges" says
CTO Vishwanath Ramarao. It began using
[ViewModel](/topic/libraries/architecture/viewmodel), which allows data to
survive configuration changes (such as screen rotations);
[LiveData](/topic/libraries/architecture/livedata), an
observable data-holder class; and the
[Room](/topic/libraries/architecture/room) persistence library.
"We're a modern, reactive app, and Room and LiveData fit really
well with our forward-design principles" Ramarao adds.

Hike is also evaluating the [Paging Library](/topic/libraries/paging),
which makes it easier for an app gradually to load information as needed from a
data source, without overloading the device or waiting too long for a big
database query.

> "We were aware of Architecture Components in general and wanted to learn more"
> Ramarao says. "But what started as an exploration of the Android-ecosystem
> best practices became an important tool to tackle our technical and
> architectural debt. It ultimately became a way of modernizing our
> architecture and development practice".

## Results

Thanks to Architecture Components, Hike significantly reduced the total
lines of code in their app, while also making that code more readable
and maintainable. Android Architecture Components also helped them to
raise their crash-free user ratings to well beyond 99 percent,
something they’d struggled to accomplish in the past.

## Get started

Android Architecture Components is open to all developers as part of
[Android Jetpack](/jetpack). [Get
started with Android Architecture Components](/jetpack/arch).