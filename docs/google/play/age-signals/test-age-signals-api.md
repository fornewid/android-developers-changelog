---
title: Test your Play Age Signals API (beta) integration  |  Android Developers
url: https://developer.android.com/google/play/age-signals/test-age-signals-api
source: html-scrape
---

On March 17, 2026, the Play Age Signals API starts rolling out responses for users in Brazil in [preparation for requirements under Digital ECA](https://support.google.com/googleplay/android-developer/answer/6223646#digital_eca_requirements). Ongoing updates will be provided in advance of [age verification bills](http://support.google.com/googleplay/android-developer/answer/16569691) in US states, which are slated to go into effect in Utah and Louisiana in May and July 2026 respectively. API responses for users in Texas not live due to a Federal District Court preliminary injunction.

* [Android Developers](https://developer.android.com/)
* [Google Play](https://developer.android.com/distribute)
* [Play Age Signals](https://developer.android.com/google/play/age-signals)

# Test your Play Age Signals API (beta) integration Stay organized with collections Save and categorize content based on your preferences.



To test your Play Age Signals API (beta) integration with your app, use the
[FakeAgeSignalsManager](/google/play/age-signals/reference/com/google/android/play/agesignals/testing/FakeAgeSignalsManager) implementation available in the age signals artifact.
The `FakeAgeSignalsManager` implementation lets you simulate the API's behavior.

The `FakeAgeSignalsManager` is intended solely for unit or integration tests to
confirm your app behavior. To test your integration, replace your
`AgeSignalsManager` instance with a `FakeAgeSignalsManager` instance.

The following example simulates the response for a verified adult:

### Kotlin

```
val fakeVerifiedUser =
    AgeSignalsResult.builder()
        .setUserStatus(AgeSignalsVerificationStatus.VERIFIED)
        .setAgeLower(18)
        .build()
val manager = FakeAgeSignalsManager()
manager.setNextAgeSignalsResult(fakeVerifiedUser)
manager.checkAgeSignals(AgeSignalsRequest.builder().build())
    .addOnSuccessListener { /* handle success case */ }
    .addOnFailureListener { /* handle failure case */ }
```

### Java

```
AgeSignalsResult fakeVerifiedUser =
    AgeSignalsResult.builder()
        .setUserStatus(AgeSignalsVerificationStatus.VERIFIED)
        .build();
FakeAgeSignalsManager manager = new FakeAgeSignalsManager();
manager.setNextAgeSignalsResult(fakeVerifiedUser);
manager.checkAgeSignals(AgeSignalsRequest.builder().build())
    .addOnSuccessListener(/* handle success case */)
    .addOnFailureListener(/* handle failure case */);
```

The following example simulates the response for a supervised user between 13
and 17 years old:

### Kotlin

```
val fakeSupervisedUser =
    AgeSignalsResult.builder()
        .setUserStatus(AgeSignalsVerificationStatus.SUPERVISED)
        .setAgeLower(13)
        .setAgeUpper(17)
        .setInstallId("fake_install_id")
        .build()
val manager = FakeAgeSignalsManager()
manager.setNextAgeSignalsResult(fakeSupervisedUser)
manager.checkAgeSignals(AgeSignalsRequest.builder().build())
    .addOnSuccessListener { /* handle success case */ }
    .addOnFailureListener { /* handle failure case */ }
```

### Java

```
AgeSignalsResult fakeSupervisedUser =
    AgeSignalsResult.builder()
        .setUserStatus(AgeSignalsVerificationStatus.SUPERVISED)
        .setAgeLower(13)
        .setAgeUpper(17)
        .setInstallId("fake_install_id")
        .build();
FakeAgeSignalsManager manager = new FakeAgeSignalsManager();
manager.setNextAgeSignalsResult(fakeSupervisedUser);
manager.checkAgeSignals(AgeSignalsRequest.builder().build())
    .addOnSuccessListener(/* handle success case */)
    .addOnFailureListener(/* handle failure case */);
```

The following example simulates the response for a declared user with a custom
age range of 13 to 15:

### Kotlin

```
val fakeDeclaredUserWithCustomAgeRange =
    AgeSignalsResult.builder()
        .setUserStatus(AgeSignalsVerificationStatus.DECLARED)
        .setAgeLower(13)
        .setAgeUpper(15)
        .setInstallId("fake_install_id")
        .build()
val manager = FakeAgeSignalsManager()
manager.setNextAgeSignalsResult(fakeDeclaredUserWithCustomAgeRange)
manager.checkAgeSignals(AgeSignalsRequest.builder().build())
    .addOnSuccessListener { /* handle success case */ }
    .addOnFailureListener { /* handle failure case */ }
```

### Java

```
AgeSignalsResult fakeDeclaredUserWithCustomAgeRange =
    AgeSignalsResult.builder()
        .setUserStatus(AgeSignalsVerificationStatus.DECLARED)
        .setAgeLower(13)
        .setAgeUpper(15)
        .setInstallId("fake_install_id")
        .build();
FakeAgeSignalsManager manager = new FakeAgeSignalsManager();
manager.setNextAgeSignalsResult(fakeDeclaredUserWithCustomAgeRange);
manager
    .checkAgeSignals(AgeSignalsRequest.builder().build())
    .addOnSuccessListener(/* handle success case */)
    .addOnFailureListener(/* handle failure case */)
```

The following example simulates the response for a pending significant change
approval for a supervised user between 13 and 17 years old with no previous
significant change having been approved:

### Kotlin

```
val fakeSupervisedApprovalPendingUser =
    AgeSignalsResult.builder()
        .setUserStatus(AgeSignalsVerificationStatus.SUPERVISED_APPROVAL_PENDING)
        .setAgeLower(13)
        .setAgeUpper(17)
        .setInstallId("fake_install_id")
        .build()
val manager = FakeAgeSignalsManager()
manager.setNextAgeSignalsResult(fakeSupervisedApprovalPendingUser)
manager.checkAgeSignals(AgeSignalsRequest.builder().build())
    .addOnSuccessListener { /* handle success case */ }
    .addOnFailureListener { /* handle failure case */ }
```

### Java

```
AgeSignalsResult fakeSupervisedApprovalPendingUser =
    AgeSignalsResult.builder()
        .setUserStatus(AgeSignalsVerificationStatus.SUPERVISED_APPROVAL_PENDING)
        .setAgeLower(13)
        .setAgeUpper(17)
        .setInstallId("fake_install_id")
        .build();
FakeAgeSignalsManager manager = new FakeAgeSignalsManager();
manager.setNextAgeSignalsResult(fakeSupervisedApprovalPendingUser);
manager
    .checkAgeSignals(AgeSignalsRequest.builder().build())
    .addOnSuccessListener(/* handle success case */)
    .addOnFailureListener(/* handle failure case */)
```

The following example simulates the response for a pending significant change
approval for a supervised user between 13 and 17 years old with all significant
changes approved up to and including the significant change that was effective
from 2025-02-01:

### Kotlin

```
val fakeSupervisedApprovalPendingUser =
    AgeSignalsResult.builder()
        .setUserStatus(AgeSignalsVerificationStatus.SUPERVISED_APPROVAL_PENDING)
        .setAgeLower(13)
        .setAgeUpper(17)
        .setMostRecentApprovalDate(
          Date.from(LocalDate.of(2025, 2, 1).atStartOfDay(ZoneOffset.UTC).toInstant())
        )
        .setInstallId("fake_install_id")
        .build()
val manager = FakeAgeSignalsManager()
manager.setNextAgeSignalsResult(fakeSupervisedApprovalPendingUser)
manager.checkAgeSignals(AgeSignalsRequest.builder().build())
    .addOnSuccessListener { /* handle success case */ }
    .addOnFailureListener { /* handle failure case */ }
```

### Java

```
AgeSignalsResult fakeSupervisedApprovalPendingUser =
    AgeSignalsResult.builder()
        .setUserStatus(AgeSignalsVerificationStatus.SUPERVISED_APPROVAL_PENDING)
        .setAgeLower(13)
        .setAgeUpper(17)
        .setMostRecentApprovalDate(
          Date.from(LocalDate.of(2025, 2, 1).atStartOfDay(ZoneOffset.UTC).toInstant()))
        .setInstallId("fake_install_id")
        .build();
FakeAgeSignalsManager manager = new FakeAgeSignalsManager();
manager.setNextAgeSignalsResult(fakeSupervisedApprovalPendingUser);
manager.checkAgeSignals(AgeSignalsRequest.builder().build())
    .addOnSuccessListener(/* handle success case */)
    .addOnFailureListener(/* handle failure case */);
```

The following example simulates a significant change approval denied for a
supervised user between 13 and 17 years old with all significant changes
approved up to and including the significant change that was effective from
2025-02-01:

### Kotlin

```
val fakeSupervisedApprovalDeniedUser =
    AgeSignalsResult.builder()
        .setUserStatus(AgeSignalsVerificationStatus.SUPERVISED_APPROVAL_DENIED)
        .setAgeLower(13)
        .setAgeUpper(17)
        .setMostRecentApprovalDate(
          Date.from(LocalDate.of(2025, 2, 1).atStartOfDay(ZoneOffset.UTC).toInstant())
        )
        .setInstallId("fake_install_id")
        .build()
val manager = FakeAgeSignalsManager()
manager.setNextAgeSignalsResult(fakeSupervisedApprovalDeniedUser)
manager.checkAgeSignals(AgeSignalsRequest.builder().build())
    .addOnSuccessListener { /* handle success case */ }
    .addOnFailureListener { /* handle failure case */ }
```

### Java

```
AgeSignalsResult fakeSupervisedApprovalDeniedUser =
    AgeSignalsResult.builder()
        .setUserStatus(AgeSignalsVerificationStatus.SUPERVISED_APPROVAL_DENIED)
        .setAgeLower(13)
        .setAgeUpper(17)
        .setMostRecentApprovalDate(
          Date.from(LocalDate.of(2025, 2, 1).atStartOfDay(ZoneOffset.UTC).toInstant()))
        .setInstallId("fake_install_id")
        .build();
FakeAgeSignalsManager manager = new FakeAgeSignalsManager();
manager.setNextAgeSignalsResult(fakeSupervisedApprovalDeniedUser);
manager.checkAgeSignals(AgeSignalsRequest.builder().build())
    .addOnSuccessListener(/* handle success case */)
    .addOnFailureListener(/* handle failure case */);
```

The following example simulates the response for an unknown user status:

### Kotlin

```
val fakeUnknownUser =
    AgeSignalsResult.builder().setUserStatus(AgeSignalsVerificationStatus.UNKNOWN).build()
val manager = FakeAgeSignalsManager()
manager.setNextAgeSignalsResult(fakeUnknownUser)
manager.checkAgeSignals(AgeSignalsRequest.builder().build())
    .addOnSuccessListener { /* handle success case */ }
    .addOnFailureListener { /* handle failure case */ }
```

### Java

```
AgeSignalsResult fakeUnknownUser =
    AgeSignalsResult.builder().setUserStatus(AgeSignalsVerificationStatus.UNKNOWN).build();
FakeAgeSignalsManager manager = new FakeAgeSignalsManager();
manager.setNextAgeSignalsResult(fakeUnknownUser);
manager.checkAgeSignals(AgeSignalsRequest.builder().build())
    .addOnSuccessListener(/* handle success case */)
    .addOnFailureListener(/* handle failure case */);
```

The following example simulates the response for a `null` user status value:

### Kotlin

```
val fakeNullUserStatus =
    AgeSignalsResult.builder()
        .setUserStatus(null)
        .build()
val manager = FakeAgeSignalsManager()
manager.setNextAgeSignalsResult(fakeNullUserStatus)
manager.checkAgeSignals(AgeSignalsRequest.builder().build())
    .addOnSuccessListener { /* handle success case */ }
    .addOnFailureListener { /* handle failure case */ }
```

### Java

```
AgeSignalsResult fakeNullUserStatus =
    AgeSignalsResult.builder()
        .setUserStatus(null)
        .build();
FakeAgeSignalsManager manager = new FakeAgeSignalsManager();
manager.setNextAgeSignalsResult(fakeNullUserStatus);
manager
    .checkAgeSignals(AgeSignalsRequest.builder().build())
    .addOnSuccessListener(/* handle success case */)
    .addOnFailureListener(/* handle failure case */)
```

The following example simulates the response with a network error code:

### Kotlin

```
val manager = FakeAgeSignalsManager()
manager.setNextAgeSignalsException(
  AgeSignalsException(AgeSignalsErrorCode.NETWORK_ERROR)
)
manager.checkAgeSignals(AgeSignalsRequest.builder().build())
    .addOnSuccessListener { /* handle success case */ }
    .addOnFailureListener { /* handle failure case */ }
```

### Java

```
FakeAgeSignalsManager manager = new FakeAgeSignalsManager();
manager.setNextAgeSignalsException(
    new AgeSignalsException(AgeSignalsErrorCode.NETWORK_ERROR));
manager.checkAgeSignals(AgeSignalsRequest.builder().build())
    .addOnSuccessListener(/* handle success case */)
    .addOnFailureListener(/* handle failure case */);
```

[Previous

arrow\_back

Review revoked approvals](/google/play/age-signals/revoked-app-approval)

[Next

Release notes

arrow\_forward](/google/play/age-signals/release-notes)