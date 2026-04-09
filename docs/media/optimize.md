---
title: Best practices for performance and reliability  |  Android media  |  Android Developers
url: https://developer.android.com/media/optimize
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Camera & media dev center](https://developer.android.com/media)
* [Guides](https://developer.android.com/media/guides)

# Best practices for performance and reliability Stay organized with collections Save and categorize content based on your preferences.




Media apps can demand a lot of resources including memory, CPU, network
connections and hardware codecs, many of which are in short supply.
In addition, apps have to reliably manage interacting with other apps, such as
controller apps sending playback command requests or media playback starting
elsewhere in the system. This section discusses best practices for making sure
that users can rely on your app to perform well and as expected.

* Use testing tools like the [Media Controller Test app](/media/optimize/mct) to
  validate your playback use-cases
* Use a device's [performance class](/topic/performance/performance-class)
  level to accurately gauge device capabilities
* Cooperate with other apps to [manage audio focus](/media/optimize/audio-focus)
* [Measure](/media/optimize/performance/measure) your app's performance and make
  decisions accordingly
* Maintain high quality when preparing to [share videos](/media/optimize/sharing)