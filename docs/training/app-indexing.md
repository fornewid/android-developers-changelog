---
title: https://developer.android.com/training/app-indexing
url: https://developer.android.com/training/app-indexing
source: md.txt
---

# Making Your App Content Searchable by Google

Google can crawl through your app content and present your Android app as a destination to users
through Google Search results, when that content corresponds to a web page that you own.

Make it possible for users to open specific content in your app from Google Search results by
setting up Android App Links: adding links to your content and associating your app with your
website. Once you add Android App Links to your app, Google can crawl your app content through your
website association and direct users on mobile devices to your app from their search results,
allowing them to directly view your app's content instead of a web page.

To set up your Android app for indexing by Google, use the
[Android App Links Assistant](https://developer.android.com/tools/help/app-link-indexing) in Android Studio
or follow these steps:

1. [Create deep links to specific content](https://developer.android.com/training/app-links/deep-linking) in your app by adding intent filters in your app manifest.
2. [Verify ownership of your app content](https://developer.android.com/training/app-links/verify-android-applinks) through a website association. Use Digital Asset Links or Google Search Console.