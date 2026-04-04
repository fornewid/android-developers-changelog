---
title: Zillow builds clear new code with Android Architecture Components  |  Developer stories  |  Android Developers
url: https://developer.android.com/stories/apps/zillow
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Developer stories](https://developer.android.com/stories)

# Zillow builds clear new code with Android Architecture Components Stay organized with collections Save and categorize content based on your preferences.



![](/static/images/distribute/stories/zillow-logo.webp)

Zillow is a top online real estate marketplace that provides consumers with
the listings, data, and calculators they need to help them buy, rent, or sell
a home. The site also connects users with local agents, mortgage providers,
and home designers.

Launched in 2006 and headquartered in Seattle, Zillow maintains a database
of more than 110 million U.S. homes. They also operate a popular suite of
over two dozen mobile real estate apps. When they began a major overhaul of
their code in their Android mobile app in July 2017, Zillow wanted to simplify
their developers’ lives by making the code more readable and easier for
new team members to understand.

## What they did

Zillow revamped their code using
[Android Architecture Components](/topic/libraries/architecture).
"We were investigating different kinds of architecture," says Aayush Raj,
Zillow software engineer. "Architecture Components had the added advantage of
lifecycle awareness, which made code much easier to manage."

[ViewModel](/topic/libraries/architecture/viewmodel) allows data to
survive configuration changes (such as screen rotations), while
[LiveData](/topic/libraries/architecture/livedata) is an observable
data-holder class. Both were used by Zillow, and together, they provided a
powerful template for implementing Model-View-ViewModel (MVVM). "It helped make
our code more testable," Raj says. The
[Room](/topic/libraries/architecture/room) persistency library also
made it easy to build a local cache layer, so the app didn't have to pull data
from the network as often, "improving performance and the user experience."

## Results

Moving lots of code for data updates from activities to
[ViewModels](/topic/libraries/architecture/viewmodel) has
"definitely helped" make the whole code base more readable, Raj adds.
They haven't yet converted the whole app to
[ViewModel](/topic/libraries/architecture/viewmodel),
but components that are using
[ViewModel](/topic/libraries/architecture/viewmodel)
haven't had any lifecycle-related bugs. Communicating
data updates to activities and fragments also works very well.

"Developers are absolutely more productive using Android Architecture
Components," says Sumiran Pradhan, Zillow senior software development engineer.
Architecture Components gives them guidance when starting from scratch,
but is also useful in the existing code base. "Once new developers
understand where the logic lives in the
[ViewModel](/topic/libraries/architecture/viewmodel), they love it,"
Pradhan adds.

## Get started

Android Architecture Components is open to all developers as part of
[Android Jetpack](/jetpack). Get
started with [Android Architecture Components](/jetpack/arch).