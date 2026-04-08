---
title: Debugging recomposition in Compose  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/quick-guides/content/video/debugging-recomposition
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Quick Guides](https://developer.android.com/develop/ui/compose/quick-guides)

# Debugging recomposition in Compose Stay organized with collections Save and categorize content based on your preferences.



A look into debugging a performance issue in Jetsnack and how to fix it in
Compose. Learn why deferring state reads by using a lambda means composition can
be skipped.

## Key points

* The three phases of Compose are composition, layout, and draw.
* Compose can skip a phase if nothing has changed. Sometimes Compose will
  entirely skip composition to optimize performance.
* You can use a lambda modifier can skip composition.
* Skipping recomposition can help reduce jank during scrolling.
* The Layout Inspector in Android Studio is a good tool to help you debug
  recomposition issues.

## Resources

* [Blog post](https://goo.gle/3TRm8wv)
* [Jetsnack on GitHub](https://goo.gle/3D3NCJl)

## Collections that contain this guide

This guide is part of these curated Quick Guide collections that cover
broader Android development goals:

![](/static/images/quick-guides/collection-illustration.png)

![](/static/images/picto-icons/collection.svg)

### Compose basics

This series of videos introduces various Compose APIs,
quickly showing you what's available and how to use them.

[Quick guide collection](/develop/ui/compose/quick-guides/collections/compose-basics)

![](/static/images/picto-icons/help.svg)

## Have questions or feedback

Go to our frequently asked questions page and learn about quick guides or reach out and let us know your thoughts.

[Go to FAQ](/quick-guides/faq)
[Leave feedback](https://issuetracker.google.com/issues/new?component=1573691&template=1993320)