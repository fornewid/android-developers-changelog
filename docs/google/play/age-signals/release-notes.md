---
title: Play Age Signals release notes  |  Android Developers
url: https://developer.android.com/google/play/age-signals/release-notes
source: html-scrape
---

On March 17, 2026, the Play Age Signals API starts rolling out responses for users in Brazil in [preparation for requirements under Digital ECA](https://support.google.com/googleplay/android-developer/answer/6223646#digital_eca_requirements). Ongoing updates will be provided in advance of [age verification bills](http://support.google.com/googleplay/android-developer/answer/16569691) in US states, which are slated to go into effect in Utah and Louisiana in May and July 2026 respectively. API responses for users in Texas not live due to a Federal District Court preliminary injunction.

* [Android Developers](https://developer.android.com/)
* [Google Play](https://developer.android.com/distribute)
* [Play Age Signals](https://developer.android.com/google/play/age-signals)

# Play Age Signals release notes Stay organized with collections Save and categorize content based on your preferences.



This page explains what's in the recent updates to the [Maven repository](https://maven.google.com/web/index.html#com.google.android.play:age-signals) for
the [Play Age Signals Library](/google/play/age-signals/overview).

## 0.0.3 (February 2026)

* Add user status `DECLARED`.
* Add error code `SDK_VERSION_OUTDATED`.
* Fix unit test failures when calling the `AgeSignalsResult` builder.

## 0.0.2 (December 2025)

* This release makes sure empty values are returned as `null`.
* This release of the library will return real results when the API is
  enabled.

## 0.0.1 (December 2025)

* The first non-beta release of the library will return real results when the
  API is enabled.

## 0.0.1-beta02 (October 2025)

* Add `FakeAgeSignalsManager`, a fake implementation of the
  `AgeSignalsManager`.
* Replace `com.google.type.Date` by `java.util.Date`.
* This release won't return real results when the API is enabled.

## 0.0.1-beta01 (October 2025)

* Initial release.
* This release won't return real results when the API is enabled.

[Previous

arrow\_back

Test age signals](/google/play/age-signals/test-age-signals-api)