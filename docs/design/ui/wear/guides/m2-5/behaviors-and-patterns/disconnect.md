---
title: Disconnection indicators  |  Wear  |  Android Developers
url: https://developer.android.com/design/ui/wear/guides/m2-5/behaviors-and-patterns/disconnect
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [UI Design](https://developer.android.com/design/ui)
* [Wear](https://developer.android.com/design/ui/wear)
* [Guides](https://developer.android.com/design/ui/wear/guides/get-started)

# Disconnection indicators Stay organized with collections Save and categorize content based on your preferences.




Disconnection indicators let users know when a Wear OS device is disconnected
from its companion phone or the internet.

## Usage

When Wear OS device are disconnected, your app can lose some functionality.
To indicate this, use an offline indicator.

![](/static/wear/images/design/disconnection_1.png)

An offline indicator at the top of a view helps users identify that some
functionality in the app may be not be available. Your app can gray out or hide
the functions that are not available when disconnected.

![](/static/wear/images/design/disconnection_2.png)

An offline indicator at the bottom of a list or a scroll view lets users know
that no more content can be loaded while the app is disconnected.