---
title: Limit loading in on-device Android containers  |  App architecture  |  Android Developers
url: https://developer.android.com/training/basics/intents/limit-play-loading
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [App architecture](https://developer.android.com/topic/architecture/intro)

# Limit loading in on-device Android containers Stay organized with collections Save and categorize content based on your preferences.




*On-device Android containers* are apps that simulate the Android OS on an
Android-powered device. This includes both apps that simulate the Android OS in
its entirety and apps that only simulate portions of the Android OS.

If you don't want on-device Android container apps to load in or proxy your Play
Store app, you can add a string to your app manifest that declares this
restriction.

Create a [property](/guide/topics/manifest/property-element) under the
[`<application>`](/guide/topics/manifest/application-element) in your Android
manifest with `android:name` set to `REQUIRE_SECURE_ENV` and `android:value` set
to 1:

```
<property android:name="REQUIRE_SECURE_ENV" android:value="1" />
```

For this use case, you can use the `REQUIRE_SECURE_ENV` property regardless of
the Android version that your app runs on.

On-device Android container apps are
[required](https://support.google.com/googleplay/android-developer/answer/9888379)
to respect this declaration.

For more information about on-device Android containers, see the [Help
Center](https://support.google.com/googleplay/android-developer/answer/13609005).

[Previous

arrow\_back

Allow other apps to start your activity](/training/basics/intents/filters)