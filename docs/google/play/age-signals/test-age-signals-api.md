---
title: https://developer.android.com/google/play/age-signals/test-age-signals-api
url: https://developer.android.com/google/play/age-signals/test-age-signals-api
source: md.txt
---

To test your Play Age Signals API (beta) integration with your app, use the
[FakeAgeSignalsManager](https://developer.android.com/google/play/age-signals/reference/com/google/android/play/agesignals/testing/FakeAgeSignalsManager) implementation available in the age signals artifact.
The `FakeAgeSignalsManager` implementation lets you simulate the API's behavior.

The `FakeAgeSignalsManager` is intended solely for unit or integration tests to
confirm your app behavior. To test your integration, replace your
`AgeSignalsManager` instance with a `FakeAgeSignalsManager` instance.

The following example simulates the response for a verified adult:

### Kotlin

```kotlin
val fakeVerifiedUser =
    AgeSignalsResult.builder()
        .setUserStatus(AgeSignalsVerificationStatus.VERIFIED)
        .build()
val manager = FakeAgeSignalsManager()
manager.setNextAgeSignalsResult(fakeVerifiedUser)
manager.checkAgeSignals(AgeSignalsRequest.builder().build())
    .addOnSuccessListener { /* handle success case */ }
    .addOnFailureListener { /* handle failure case */ }
```

### Java

```java
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

```kotlin
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

```java
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

The following example simulates the response for a pending significant change
approval for a supervised user between 13 and 17 years old with no previous
significant change having been approved:

### Kotlin

```kotlin
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

```java
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

```kotlin
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

```java
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

```kotlin
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

```java
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

```kotlin
val fakeUnknownUser =
    AgeSignalsResult.builder().setUserStatus(AgeSignalsVerificationStatus.UNKNOWN).build()
val manager = FakeAgeSignalsManager()
manager.setNextAgeSignalsResult(fakeUnknownUser)
manager.checkAgeSignals(AgeSignalsRequest.builder().build())
    .addOnSuccessListener { /* handle success case */ }
    .addOnFailureListener { /* handle failure case */ }
```

### Java

```java
AgeSignalsResult fakeUnknownUser =
    AgeSignalsResult.builder().setUserStatus(AgeSignalsVerificationStatus.UNKNOWN).build();
FakeAgeSignalsManager manager = new FakeAgeSignalsManager();
manager.setNextAgeSignalsResult(fakeUnknownUser);
manager.checkAgeSignals(AgeSignalsRequest.builder().build())
    .addOnSuccessListener(/* handle success case */)
    .addOnFailureListener(/* handle failure case */);
```

The following example simulates the response with a network error code:

### Kotlin

```kotlin
val manager = FakeAgeSignalsManager()
manager.setNextAgeSignalsException(
  AgeSignalsException(AgeSignalsErrorCode.NETWORK_ERROR)
)
manager.checkAgeSignals(AgeSignalsRequest.builder().build())
    .addOnSuccessListener { /* handle success case */ }
    .addOnFailureListener { /* handle failure case */ }
```

### Java

```java
FakeAgeSignalsManager manager = new FakeAgeSignalsManager();
manager.setNextAgeSignalsException(
    new AgeSignalsException(AgeSignalsErrorCode.NETWORK_ERROR));
manager.checkAgeSignals(AgeSignalsRequest.builder().build())
    .addOnSuccessListener(/* handle success case */)
    .addOnFailureListener(/* handle failure case */);
```