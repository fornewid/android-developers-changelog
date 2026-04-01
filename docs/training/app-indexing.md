---
title: Making Your App Content Searchable by Google  |  Android Developers
url: https://developer.android.com/training/app-indexing
source: html-scrape
---

* [Android Developers](https://developer.android.com/)

# Making Your App Content Searchable by Google Stay organized with collections Save and categorize content based on your preferences.



Google can crawl through your app content and present your Android app as a destination to users
through Google Search results, when that content corresponds to a web page that you own.

Make it possible for users to open specific content in your app from Google Search results by
setting up Android App Links: adding links to your content and associating your app with your
website. Once you add Android App Links to your app, Google can crawl your app content through your
website association and direct users on mobile devices to your app from their search results,
allowing them to directly view your app's content instead of a web page.

To set up your Android app for indexing by Google, use the
[Android App Links Assistant](/tools/help/app-link-indexing) in Android Studio
or follow these steps:

1. [Create deep links to specific content](/training/app-links/deep-linking)
   in your app by adding intent filters in your app manifest.
2. [Verify ownership of your app content](/training/app-links/verify-android-applinks) through a website association. Use Digital Asset Links or
   Google Search Console.