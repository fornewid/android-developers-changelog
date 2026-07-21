---
title: https://developer.android.com/google/play/age-signals/use-age-signals-api
url: https://developer.android.com/google/play/age-signals/use-age-signals-api
source: md.txt
---

By using the Play Age Signals API (beta), you agree to the [terms of service](https://developer.android.com/google/play/age-signals/overview#terms-service)
and you agree to comply with all [Google Play developer policies](https://play.google/developer-content-policy/).

To request a user's age range and sharing status, you call the Play Age Signals
API (beta) from your app at runtime. The default age ranges the API returns
are 0-12, 13-15, 16-17, and 18+, but you can receive [custom age ranges](https://developer.android.com/google/play/age-signals/understand-age-signals-responses#custom-age-ranges).

## Integrate Play Age Signals API into your app

The Play Age Signals API is supported on phones, foldables, and tablets running
Android 6.0 (API level 23) and higher. To integrate the Play Age Signals API
into your app, add the following dependency to your app's `build.gradle` file:

    implementation 'com.google.android.play:age-signals:0.0.4'