---
title: https://developer.android.com/google/play/age-signals/release-notes
url: https://developer.android.com/google/play/age-signals/release-notes
source: md.txt
---

This page explains what's in the recent updates to the [Maven repository](https://maven.google.com/web/index.html#com.google.android.play:age-signals) for
the [Play Age Signals Library](https://developer.android.com/google/play/age-signals/overview).

## 0.0.3 (February 2026)

- Add user status `DECLARED`.
- Add error code `SDK_VERSION_OUTDATED`.
- Fix unit test failures when calling the `AgeSignalsResult` builder.

## 0.0.2 (December 2025)

- This release makes sure empty values are returned as `null`.
- This release of the library will return real results when the API is enabled.

## 0.0.1 (December 2025)

- The first non-beta release of the library will return real results when the API is enabled.

## 0.0.1-beta02 (October 2025)

- Add `FakeAgeSignalsManager`, a fake implementation of the `AgeSignalsManager`.
- Replace `com.google.type.Date` by `java.util.Date`.
- This release won't return real results when the API is enabled.

## 0.0.1-beta01 (October 2025)

- Initial release.
- This release won't return real results when the API is enabled.