---
title: https://developer.android.com/google/play/age-signals/release-notes
url: https://developer.android.com/google/play/age-signals/release-notes
source: md.txt
---

This page explains what's in the recent updates to the [Maven repository](https://maven.google.com/web/index.html#com.google.android.play:age-signals) for
the [Play Age Signals Library](https://developer.android.com/google/play/age-signals/overview.md.txt).

## 0.0.5 (November 2026)

- **New method for applicable age features** : Introduced
  `getApplicableAgeFeatures()` to check which age-related features (such as
  `ApplicableAgeFeature.MANDATORY_SHARING`) apply to the current user before
  calling `requestAgeSignalsAccess()`.

- **New error code** : Added `DEVICE_NOT_SUPPORTED` (`-11`) for unsupported
  device types.

- **Testing updates** : Added the following methods to `FakeAgeSignalsManager`
  so that you can test how your app handles `getApplicableAgeFeatures()`
  responses without connecting to the Play Store:

  - `setNextApplicableAgeFeaturesResult()`: Sets the
    `ApplicableAgeFeaturesResult` that the next `getApplicableAgeFeatures()`
    call returns. Use this method to simulate users in regions where
    mandatory age sharing applies (`ApplicableAgeFeature.MANDATORY_SHARING`)
    or doesn't apply (an empty set).

  - `setNextApplicableAgeFeaturesException()`: Makes the next
    `getApplicableAgeFeatures()` call fail with the `AgeSignalsException`
    that you specify. Use this method to test your app's error handling,
    such as retry logic for a `NETWORK_ERROR`.

## 0.0.4 (July 2026)

- **Two-function architecture:** Starting with this release, you must use the following methods to receive age signals:
  - `requestAgeSignalsAccess()` (new method): Explicitly triggers the Play in-app prompt for age range sharing request.
  - `checkAgeSignals()` (existing method): Receive age signals.
- **Deprecate userStatus:** `userStatus` is deprecated and no longer supported in version 0.0.4 or higher. `userStatus` is now replaced by `ageRangeSource` and `significantChangeStatus`.
- **New field for significant changes:** Introduced the `significantChangeStatus` enum field to track pending, approved, or declined status for significant changes, and renamed `mostRecentApprovalDate` to `significantChangeApprovalDate` for clarity.

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