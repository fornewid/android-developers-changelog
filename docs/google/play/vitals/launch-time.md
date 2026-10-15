---
title: App startup time  |  Android vitals  |  Android Developers
url: https://developer.android.com/google/play/vitals/launch-time
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Google Play](https://developer.android.com/distribute)
* [Android vitals](https://developer.android.com/google/play/vitals)

# App startup time Stay organized with collections Save and categorize content based on your preferences.





Users expect apps to load fast and be responsive. An app with a slow start time
doesn't meet this expectation and can disappoint users. This sort of poor
experience can cause a user to rate your app poorly on the Play store or even
abandon your app altogether.

**Note:** For information on how to diagnose and resolve this issue, see [App startup time](/topic/performance/issues/launch-time).

## Android vitals

Android vitals can help improve your app's performance by alerting you on the
[Play Console](https://play.google.com/console/) when your app's startup times are excessive.

Android vitals considers the following startup times for your app excessive:

* [Cold](/topic/performance/issues/launch-time#cold) startup takes 5 seconds or longer.
* [Warm](/topic/performance/issues/launch-time#warm) startup takes 2 seconds or longer.
* [Hot](/topic/performance/issues/launch-time#hot) startup takes 1.5 seconds or longer.

Android vitals uses the [time to initial display (TTID)](/topic/performance/issues/launch-time#time-initial) metric. TTID is the
time it takes to display the first frame of the app's UI, including process
initialization during a cold start, activity creation during a cold or warm
start, and displaying the first frame.

For information about how Google Play collects Android vitals data, see the
[Play Console documentation](https://support.google.com/googleplay/android-developer/answer/7385505).

[Previous

arrow\_back

Permission Denials](/google/play/vitals/permissions)