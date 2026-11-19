---
title: https://developer.android.com/google/play/age-signals/v4/use-age-signals-api
url: https://developer.android.com/google/play/age-signals/v4/use-age-signals-api
source: md.txt
---

> [!CAUTION]
> **Caution:** You are viewing the documentation for Play Age Signals version 0.0.4. Although this version continues to return responses in Australia, Brazil, Canada, and US states like Alabama (starting January 2027), California (starting January 2027) and Texas, it is no longer receiving new updates. To view the active and supported version, refer to [Play Age Signals documentation](https://developer.android.com/google/play/age-signals/overview.md.txt).

By using the Play Age Signals API (beta), you agree to the [terms of service](https://developer.android.com/google/play/age-signals/v4/overview.md.txt#terms-service)
and you agree to comply with all [Google Play developer policies](https://play.google/developer-content-policy/).

To request a user's age range and sharing status, you call the Play Age Signals
API (beta) from your app at runtime. The default age ranges the API returns
are 0-12, 13-15, 16-17, and 18+, but you can receive [custom age ranges](https://developer.android.com/google/play/age-signals/v4/understand-age-signals-responses.md.txt#custom-age-ranges).

## Integrate Play Age Signals API into your app

The Play Age Signals API is supported on phones, foldables, and tablets running
Android 6.0 (API level 23) and higher. To integrate the Play Age Signals API
into your app, add the following dependency to your app's `build.gradle` file:

```java
implementation 'com.google.android.play:age-signals:0.0.4'
```