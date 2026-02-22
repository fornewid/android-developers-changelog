---
title: https://developer.android.com/training/app-links/instant-app-links
url: https://developer.android.com/training/app-links/instant-app-links
source: md.txt
---

# Create App Links for Instant Apps

An Android Instant App is a small version of your app that runs without installation. Instead of installing an APK, users launch your app simply by clicking a URL. As such, all instant apps need to be accessible via a URL declared using Android App Links. This page explains how to use Android App Links for your[Android Instant Apps](https://developer.android.com/topic/instant-apps).
| **Note:** If you're not building an instant app, then you don't need to read this guide---you should instead create app links for your installable app by reading[Create Deep Links to App Content](https://developer.android.com/training/app-links/deep-linking).

## App links overview

First, here's a summary of what you should already understand about app links.

- When you create an intent filter for activities in your app that allow the user to jump straight to a specific screen in your app with a URL link, this is known as a "deep link." Other apps can declare a similar URL intent filter, though, so the system might ask the user which app to open. To create these deep links, read[Create Deep Links to App Content](https://developer.android.com/training/app-links/deep-linking).
- When you publish an`assetlinks.json`file on the website that corresponds to your app's HTTP deep links, you verify that your app is the true owner of those URLs. Thus, you've converted your deep links into Android App Links, which ensure that your app instantly opens when the user clicks such a URL. To create app links, read[Verify Android App Links](https://developer.android.com/training/app-links/verify-android-applinks).

So, Android App Links are simply HTTP deep links that your website is verified to own so that the user doesn't need to choose which app to open. For a more specific description, see[differences between deep links and app links](https://developer.android.com/training/app-links/verify-android-applinks#the-difference).

In both cases, however, the user must already have your app installed. If the user clicks one of your web site's links and they don't have your app installed (and no other app handles that URL intent), the URL is opened in a web browser. So, creating an Instant App solves this part---it allows users to open your app by simply clicking a URL, even if they don't have your app installed.

When end users perform a Google search for your app, Google Search displays a URL with the "Instant" badge.

## How app links for instant apps are different

If you've already followed the guides to[Create Deep Links to App Content](https://developer.android.com/training/app-links/deep-linking)and[Verify Android App Links](https://developer.android.com/training/app-links/verify-android-applinks), then you've already done most of the work necessary to make app links work with your instant app. There are just a couple extra rules when using app links for instant apps:

- All intent filters used as app links in your instant app must support both HTTP and HTTPS. For example:

      <intent-filter>
          <action android:name="android.intent.action.VIEW" />
          <category android:name="android.intent.category.DEFAULT" />
          <category android:name="android.intent.category.BROWSABLE" />
          <data android:scheme="http" android:host="www.example.com" />
          <data android:scheme="https" />
      </intent-filter>

  Notice that you don't need to include the`host`in the second`<data>`element because, within each`<intent-filter>`element, all combinations of each`<data>`attribute are considered valid (so this intent filter*does* resolve`https://www.example.com`).
- Only one instant app can be declared for each website domain. (This is unlike when creating app links for your installable app, which allows you to[associate a website with multiple apps](https://developer.android.com/training/app-links/verify-android-applinks#multiple-apps).)

## Other reminders when creating app links

- All HTTP URL intent filters in your instant app should be included in your installable app. This is important because once the user installs your full app, tapping a URL should always open the installed app, not the instant app.
- You must set`autoVerify="true"`in at least one intent filter in both the instant and the installable app. (See how to[enable automatic verification](https://developer.android.com/training/app-links/verify-android-applinks#config-verify).)
- You must publish one`assetlinks.json`for each domain (and subdomain supported by your app links, using the HTTPS protocol. (See how to[support app linking for multiple hosts](https://developer.android.com/training/app-links/verify-android-applinks#multi-host)).
- The`assetlinks.json`file must be valid JSON, be served without redirects, and be accessible to bots (your`robots.txt`must allow crawling`/.well-known/assetlinks.json`).
- Use of wildcards in your intent filter's host attribute is not recommended. (See how to[support app linking from multiple subdomains](https://developer.android.com/training/app-links/verify-android-applinks#multi-subdomain).)
- Custom host/scheme URLs should be declared with separate intent filters.
- Ensure that your app link URLs account for your top search results for your key terms.