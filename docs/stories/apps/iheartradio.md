---
title: iHeartRadio creates a cleaner, leaner code base with Android Architecture Components  |  Developer stories  |  Android Developers
url: https://developer.android.com/stories/apps/iheartradio
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Developer stories](https://developer.android.com/stories)

# iHeartRadio creates a cleaner, leaner code base with Android Architecture Components Stay organized with collections Save and categorize content based on your preferences.



![](/static/images/distribute/stories/iheartradio-logo.webp)

New York City-based [iHeartRadio](https://www.iheart.com/) provides
unlimited music and thousands of radio stations, all in one app. The company's
operations include radio broadcasting, online, mobile, digital and social media,
live concerts and events, syndication, music-research services, and
independent media representation.

Listeners around the world have downloaded the app over a billion times
since it launched in 2008. By late 2017, however, the codebase was aging,
and managing the code and integrating new features proved to be difficult.

## What they did

iHeartRadio chose
[Android Architecture Components](/topic/libraries/architecture) as they
began upgrading their code. The straightforward, easy-to-implement
[Room](/topic/libraries/architecture/room) persistency library was
attractive to their engineers for its
capabilities for handling such things as asynchronous queries and support for
RxJava, which iHeartRadio uses extensively in their code.

They also adopted
[lifecycle-aware components](/topic/libraries/architecture/lifecycle),
which perform actions in response to a change in the
lifecycle status of another component. The iHeartRadio
engineers found these components very useful for shrinking dependencies
injected into activities and fragments. In addition, the company created
prototypes using [ViewModel](/topic/libraries/architecture/viewmodel),
which allows data to survive configuration changes, such as screen rotations.

## Results

iHeartRadio found it easy to migrate over to
[Architecture Components](/jetpack/arch)
and to use the libraries to test how well integration was working.
[Room](/topic/libraries/architecture/room) and other components require
the use of very little boilerplate code, meaning that the app's code is
now significantly shorter. [Architecture Components](/jetpack/arch)
also resulted in fewer memory leaks. An additional benefit was that new
developers joining the team could quickly get ramped up and start coding.

Overall, adopting [Architecture Components](/jetpack/arch) has helped
iHeartRadio to create a cleaner, leaner code base that helps them to prevent errors.
That's good news for any app, especially for one offering
all-in-one digital audio to a worldwide audience.

## Get started

Android Architecture Components is open to all developers as part of
[Android Jetpack](/jetpack). [Get
started with Android Architecture Components](/jetpack/arch).