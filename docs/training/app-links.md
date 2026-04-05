---
title: About deep links  |  App architecture  |  Android Developers
url: https://developer.android.com/training/app-links
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [App architecture](https://developer.android.com/topic/architecture/intro)

# About deep links Stay organized with collections Save and categorize content based on your preferences.




Android deep links let you bring users directly into your app content from links
they have tapped, such as from web browsing, search, notifications and more.

Android supports two general types of app linking to meet different needs:

* *Deep linking* is a standard Android platform capability that takes advantage
  of the intents system to route deep links to your app. Through intents, you
  can register to handle several types of deep links, from custom URIs to
  standard web schemes and domains. Deep links are powerful and useful for
  navigation, but they are subject to the system disambiguation dialog. Deep
  links are available on all Android versions.
* *Android App Links* is an enhanced deep linking capability that verifies deep
  links to your own website by establishing a trusted association between your
  app and your website. After they are verified, deep links to your website can
  immediately open corresponding content in your app, without requiring the user
  to select your app from a disambiguation dialog. App Links is supported on
  Android 6 and later, on devices that have Google services. For deep links to
  your website, App Links is a recommended approach.

## Android 15 update

With Android 15, App Links are even more powerful with the introduction of
Dynamic App Links. With the new dynamic capabilities, you can refine your app's
deep link behaviors on the fly, with fine-grained control over URL matching, and
without needing to release a new version of your app.

## In this guide

This guide explains how to create and test deep links, then covers how to
implement App Links to deliver the best user experience for deep links to your
website or domain.

You should already be familiar with the following guides:

* [Manifest file structure](/guide/topics/manifest/manifest-intro)
* [Intents and intent filters](/guide/components/intents-filters)