---
title: https://developer.android.com/google/play/age-signals/use-age-signals-api
url: https://developer.android.com/google/play/age-signals/use-age-signals-api
source: md.txt
---

By using the Play Age Signals API (beta), you agree to the [terms of service](https://developer.android.com/google/play/age-signals/overview#terms-service)
and you agree to comply with all [Google Play developer policies](https://play.google/developer-content-policy/). To request
the user's status and age range, you call the API from your app at runtime. The
Play Age Signals API only returns data for users based in regions where Play is
required by law to provide age category data.

Play returns an age range based on the age bands defined by the applicable
jurisdiction and regions. The default ages the API returns in applicable
jurisdictions and regions are 0-12, 13-15, 16-17, and 18+ but
[custom age ranges](https://developer.android.com/google/play/age-signals/use-age-signals-api#custom-age-ranges) may be received. Google Play automatically updates
cached age signals for a user within 2 to 8 weeks following the user's
birthday.

## Integrate Play Age Signals API into your app

The Play Age Signals API is supported on phones, foldables, and tablets running
Android 6.0 (API level 23) and higher. To integrate the Play Age Signals API
into your app, add the following dependency to your app's `build.gradle` file:

`implementation 'com.google.android.play:age-signals:0.0.3'`

## Request age signals

Here's an example of making an age signals request:

### Kotlin

```kotlin
// Create an instance of a manager
val ageSignalsManager =
    AgeSignalsManagerFactory.create(ApplicationProvider.getApplicationContext())

// Request an age signals check
ageSignalsManager
    .checkAgeSignals(AgeSignalsRequest.builder().build())
    .addOnSuccessListener { ageSignalsResult ->
        // Store the install ID for later...
        val installId = ageSignalsResult.installId()

        if (ageSignalsResult.userStatus() == AgeSignalsVerificationStatus.SUPERVISED_APPROVAL_DENIED) {
          // Disallow access...
        } else {
           // Do something else if the user is VERIFIED, DECLARED, SUPERVISED, etc.
        }
    }
```

### Java

```java
// Create an instance of a manager
AgeSignalsManager ageSignalsManager =
    AgeSignalsManagerFactory.create(ApplicationProvider.getApplicationContext());

// Request an age signals check
ageSignalsManager
    .checkAgeSignals(AgeSignalsRequest.builder().build())
    .addOnSuccessListener(
        ageSignalsResult -> {
          // Store the install ID for later...
          String installId = ageSignalsResult.installId();

          if (ageSignalsResult
              .userStatus()
              .equals(AgeSignalsVerificationStatus.SUPERVISED_APPROVAL_DENIED)) {
            // Disallow access ...
          } else {
            // Do something else if the user is SUPERVISED, VERIFIED, etc.
          }
        });
```

> [!TIP]
> **Tip:** Use the [Play Integrity API](https://developer.android.com/google/play/integrity/overview) when calling the Play Age Signals API to verify that the call is coming from an untampered version of your app on a certified Android-powered device, protecting the response from potential spoofing or abuse.

### (Optional) Receive custom age ranges

The default age ranges that the API returns in applicable jurisdictions and
regions are 0-12, 13-15, 16-17, and 18+.

Alternatively, to customize the default age ranges according to your app's
minimum ages, you can provide these minimum ages for your app on the
[Age signals](https://play.google.com/console/developers/app/age-signals) page in your Google Play Console. The age ranges returned will
override the default API response. For example, if you provide minimum ages of
9, 15, and 17, a 14-year-old user would fall within the 10-15 age range.

To customize the default age ranges returned by the Age Signals API, you can
provide minimum ages for your app:

1. Go to the [Age signals](https://play.google.com/console/developers/app/age-signals) page in your Play Console.
2. On the **Custom age ranges** tab, enter up to three minimum ages for your app. Minimum ages must be at least 2 years apart and can be changed once annually.
3. Click **Save**.

## Age signals responses

The Play Age Signals API (beta) response includes the following fields and
values. The values are subject to change. If you want the most recent values,
request an API response when your app opens. You are responsible for providing
age-appropriate experiences using these signals.

| Response field | Values | Description |
| `userStatus` | VERIFIED | Google verified the user's age using a commercially reasonable method such as a government-issued ID, credit card, or facial age estimation. If `userStatus` is `VERIFIED`, you can ignore the other fields. <br /> Use `ageLower` and `ageUpper` to determine the user's age range. |
| `userStatus` | DECLARED | The user's age was declared by the user, their parent or legal guardian. <br /> Use `ageLower` and `ageUpper` to determine the user's age range. |
| `userStatus` | SUPERVISED | The user has a supervised Google Account managed by a parent who sets their age. <br /> Use `ageLower` and `ageUpper` to determine the user's age range. <br /> Use `mostRecentApprovalDate` to determine the last significant change that was approved. |
| `userStatus` | SUPERVISED_APPROVAL_PENDING | The user has a supervised Google Account, and their supervising parent has not yet approved one or more pending significant changes. <br /> Use `ageLower` and `ageUpper` to determine the user's age range. <br /> Use `mostRecentApprovalDate` to determine the last significant change that was approved. |
| `userStatus` | SUPERVISED_APPROVAL_DENIED | The user has a supervised Google Account, and their supervising parent denied approval for one or more significant changes. <br /> Use `ageLower` and `ageUpper` to determine the user's age range. <br /> Use `mostRecentApprovalDate` to determine the last significant change that was approved. |
| `userStatus` | UNKNOWN | The user's age is unknown and the user is in an applicable jurisdiction or region. <br /> **Applicable only to US states:** To obtain an age signal from Google Play, ask the user to visit the Play Store to resolve their status. |
| `userStatus` | `null` | All other users return this value. If `userStatus` is `null`, you can ignore the other fields. |
| `ageLower` | 0 to 18 | The (inclusive) lower bound of a supervised user's age range. <br /> Use the `ageLower` and `ageUpper` to determine the user's age range. |
| `ageLower` | `null` | `userStatus` is unknown or `null`. |
| `ageUpper` | 2 to 18 | The (inclusive) upper bound of a supervised user's age range. <br /> Use the `ageLower` and `ageUpper` to determine the user's age range. |
| `ageUpper` | `null` | **Either** the `userStatus` is supervised and the user's parent attested age is over 18. <br /> **Or** the `userStatus` is unknown or `null`. |
| `mostRecentApprovalDate` | Datestamp | The `effective from` date of the most recent significant change that was approved. When an app is installed, the date of the most recent significant change prior to install is used. |
| `mostRecentApprovalDate` | `null` | **Either** the `userStatus` is supervised and no significant change has been submitted. <br /> **Or** `userStatus` is verified, unknown, or `null`. |
| `installID` | Play-generated alphanumeric ID. | An ID assigned to supervised user installs by Google Play, used for the purposes of notifying you of revoked app approval. Review the documentation for [revoked app approvals](https://developer.android.com/google/play/age-signals/revoked-app-approval). |
| `installID` | `null` | `userStatus` is verified, unknown, or `null`. |
|---|---|---|

## Example responses for users in Brazil

In Brazil, `userStatus` can only be `DECLARED` and
`UNKNOWN`.

> [!NOTE]
> **Note:** Use library version 0.0.3 or higher to receive `DECLARED` as a user status. Earlier library versions will return `null` instead of `DECLARED`.

For a user who declared their age, you would receive the following:

- `userStatus` would be `AgeSignalsVerificationStatus.DECLARED`.
- `ageLower` would be a number (for example, 13).
- `ageUpper` would be a number or `null` (for example, 15).
- Other response fields would be `null`.

For a user whose age is unknown, you would receive the following:

- `userStatus` would be `AgeSignalsVerificationStatus.UNKNOWN`.
- Other response fields would be `null`.

The user status may change from `UNKNOWN` to `DECLARED`
once the user's age is available to share.

## Example responses for users in US states

In applicable US states, `userStatus` can be `VERIFIED`,
`SUPERVISED`, `SUPERVISED_APPROVAL_PENDING`,
`SUPERVISED_APPROVAL_DENIED`, `UNKNOWN`, or
`null`.

For a verified user, you would receive the following:

- `userStatus` would be `AgeSignalsVerificationStatus.VERIFIED`.
- `ageLower` would be a number (for example, 18).
- `ageUpper` would be a number or `null` (for example, `null`).
- Other response fields would be `null`.

For a supervised user, you would receive the following:

- `userStatus` would be `AgeSignalsVerificationStatus.SUPERVISED`.
- `ageLower` would be a number (for example, 13).
- `ageUpper` would be a number or `null` (for example, 15).
- `mostRecentApprovalDate` would be a Java date object (for example, `2026-01-01`) or `null` (if no [significant change](https://developer.android.com/google/play/age-signals/notify-significant-changes) has been approved).
- `installID` would be a Play-generated alphanumeric ID (for example, `550e8400-e29b-41d4-a716-446655441111`).

For a supervised user with a significant change approval pending, you would
receive the following:

- `userStatus` would be `AgeSignalsVerificationStatus.SUPERVISED_APPROVAL_PENDING`.
- `ageLower` would be a number (for example, 13).
- `ageUpper` would be a number or `null` (for example, 15).
- `mostRecentApprovalDate` would be a Java date object (for example, `2026-01-01`) or `null` (if no [significant change](https://developer.android.com/google/play/age-signals/notify-significant-changes) has been approved).
- `installID` would be a Play-generated alphanumeric ID (for example, `550e8400-e29b-41d4-a716-446655441111`).

## Handle API error codes

If your app makes a Play Age Signals API request and the call fails, your
app receives an error code. These errors can happen for various reasons, such as
the Play Store app being out of date.

### Retry strategy

In situations where the user is in session, we recommend implementing a retry
strategy with a maximum number of attempts as an exit condition so that the
error disrupts the user experience as little as possible.

| Numerical value of error code | Error Code | Description | Retryable |
| -1 | API_NOT_AVAILABLE | The Play Age Signals API is not available. The Play Store app version installed on the device might be old. Possible resolution - Ask the user to update the Play Store. | Yes |
| -2 | PLAY_STORE_NOT_FOUND | No Play Store app is found on the device. Ask the user to install or enable the Play Store. | Yes |
| -3 | NETWORK_ERROR | No available network is found. Ask the user to check for a connection. | Yes |
| -4 | PLAY_SERVICES_NOT_FOUND | Play Services is not available or its version is too old. Ask the user to install, update, or enable Play Services. | Yes |
| -5 | CANNOT_BIND_TO_SERVICE | Binding to the service in the Play Store has failed. This can be due to having an old Play Store version installed on the device or device memory is overloaded. Ask the user to update the Play Store app. Retry with an exponential backoff. | Yes |
| -6 | PLAY_STORE_VERSION_OUTDATED | The Play Store app needs to be updated. Ask the user to update the Play Store app. | Yes |
| -7 | PLAY_SERVICES_VERSION_OUTDATED | Play Services needs to be updated. Ask the user to update Play Services. | Yes |
| -8 | CLIENT_TRANSIENT_ERROR | There was a transient error in the client device. Implement a retry strategy with a maximum number of attempts as an exit condition. If the issue still doesn't resolve, ask the user to try again later. | Yes |
| -9 | APP_NOT_OWNED | The app was not installed by Google Play. Ask the user to get your app from Google Play. | No |
| -10 | SDK_VERSION_OUTDATED | The Play Age Signals SDK version is no longer supported. Ask the user to update your app to a later version that uses a recent version of the Play Age Signals SDK. | No |
| -100 | INTERNAL_ERROR | Unknown internal error. Implement a retry strategy with a maximum number of attempts as an exit condition. If the issue still doesn't resolve, ask the user to try again later. If it fails consistently, [contact Google Play Developer support](https://support.google.com/googleplay/android-developer/gethelp), include Play Age Signals API in the subject, and include as much technical detail as possible (such as a bug report). | No |
|---|---|---|---|