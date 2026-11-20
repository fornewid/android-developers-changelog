---
title: https://developer.android.com/google/play/age-signals/test-age-signals-api
url: https://developer.android.com/google/play/age-signals/test-age-signals-api
source: md.txt
---

To verify your app's handling of various age signals and age sharing
status, use the [FakeAgeSignalsManager](https://developer.android.com/google/play/age-signals/reference/com/google/android/play/agesignals/testing/FakeAgeSignalsManager.md.txt) provided in the SDK testing artifact.
`FakeAgeSignalsManager` lets you simulate API responses for unit and integration
testing by replacing your production AgeSignalsManager instance.

To simulate different response types using the Play Age Signals API SDK
version 0.0.6, see the following examples:

## Example 1: Check applicable age features (mandatory sharing)

### Kotlin

```kotlin
val fakeFeaturesResult = ApplicableAgeFeaturesResult.builder()
    .setFeatures(setOf(ApplicableAgeFeature.MANDATORY_SHARING)) // or emptySet()
    .build()

val manager = FakeAgeSignalsManager()
manager.setNextApplicableAgeFeaturesResult(fakeFeaturesResult)
manager.getApplicableAgeFeatures(ApplicableAgeFeaturesRequest.builder().build())
    .addOnSuccessListener { /* handle success */ }
```

### Java

```java
ApplicableAgeFeaturesResult fakeFeaturesResult = ApplicableAgeFeaturesResult.builder()
    .setFeatures(Collections.singleton(ApplicableAgeFeature.MANDATORY_SHARING)) // or Collections.emptySet()
    .build();

FakeAgeSignalsManager manager = new FakeAgeSignalsManager();
manager.setNextApplicableAgeFeaturesResult(fakeFeaturesResult);
manager.getApplicableAgeFeatures(ApplicableAgeFeaturesRequest.builder().build())
    .addOnSuccessListener(/* handle success */);
```

## Example 2: Request access (user shared age)

### Kotlin

```kotlin
val fakeAccessResult = AgeSignalsAccessResult.builder()
    .setAgeSignalsStatus(AgeSignalsStatus.SHARED) // or NOT_SHARED
    .build()

val manager = FakeAgeSignalsManager()
manager.setNextAgeSignalsAccessResult(fakeAccessResult)
manager.requestAgeSignalsAccess(
    AgeSignalsAccessRequest.builder()
        .setActivity(fakeActivity)
        .build()
)
    .addOnSuccessListener { /* handle success */ }
```

### Java

```java
AgeSignalsAccessResult fakeAccessResult = AgeSignalsAccessResult.builder()
    .setAgeSignalsStatus(AgeSignalsStatus.SHARED) // or NOT_SHARED
    .build();

FakeAgeSignalsManager manager = new FakeAgeSignalsManager();
manager.setNextAgeSignalsAccessResult(fakeAccessResult);
manager.requestAgeSignalsAccess(
        AgeSignalsAccessRequest.builder()
            .setActivity(fakeActivity)
            .build())
    .addOnSuccessListener(/* handle success */);
```

## Example 3: Request access (user didn't share age)

### Kotlin

```kotlin
val fakeAccessResult = AgeSignalsAccessResult.builder()
    .setAgeSignalsStatus(AgeSignalsStatus.NOT_SHARED)
    .build()

val manager = FakeAgeSignalsManager()
manager.setNextAgeSignalsAccessResult(fakeAccessResult)
manager.requestAgeSignalsAccess(
    AgeSignalsAccessRequest.builder()
        .setActivity(fakeActivity)
        .build()
)
    .addOnSuccessListener { /* handle success */ }
```

### Java

```java
AgeSignalsAccessResult fakeAccessResult = AgeSignalsAccessResult.builder()
    .setAgeSignalsStatus(AgeSignalsStatus.NOT_SHARED)
    .build();

FakeAgeSignalsManager manager = new FakeAgeSignalsManager();
manager.setNextAgeSignalsAccessResult(fakeAccessResult);
manager.requestAgeSignalsAccess(
        AgeSignalsAccessRequest.builder()
            .setActivity(fakeActivity)
            .build())
    .addOnSuccessListener(/* handle success */);
```

## Example 4: Verified adult (18+ years)

### Kotlin

```kotlin
val fakeVerifiedUser = AgeSignalsResult.builder()
    .setAgeRangeSource(AgeRangeSource.TIER_D)
    .setAgeLower(18)
    .build()

val manager = FakeAgeSignalsManager()
manager.setNextAgeSignalsResult(fakeVerifiedUser)
manager.checkAgeSignals(AgeSignalsRequest.builder().build())
    .addOnSuccessListener { /* handle success */ }
```

### Java

```java
AgeSignalsResult fakeVerifiedUser = AgeSignalsResult.builder()
    .setAgeRangeSource(AgeRangeSource.TIER_D)
    .setAgeLower(18)
    .build();

FakeAgeSignalsManager manager = new FakeAgeSignalsManager();
manager.setNextAgeSignalsResult(fakeVerifiedUser);
manager.checkAgeSignals(AgeSignalsRequest.builder().build())
    .addOnSuccessListener(/* handle success */);
```

## Example 5: Supervised minor (13-15 years old)

### Kotlin

```kotlin
val fakeSupervisedUser = AgeSignalsResult.builder()
    .setAgeRangeSource(AgeRangeSource.TIER_B)
    .setAgeLower(13)
    .setAgeUpper(15)
    .setInstallId("fake_install_id_123")
    .build()

val manager = FakeAgeSignalsManager()
manager.setNextAgeSignalsResult(fakeSupervisedUser)
manager.checkAgeSignals(AgeSignalsRequest.builder().build())
    .addOnSuccessListener { /* handle success */ }
```

### Java

```java
AgeSignalsResult fakeSupervisedUser = AgeSignalsResult.builder()
    .setAgeRangeSource(AgeRangeSource.TIER_B)
    .setAgeLower(13)
    .setAgeUpper(15)
    .setInstallId("fake_install_id_123")
    .build();

FakeAgeSignalsManager manager = new FakeAgeSignalsManager();
manager.setNextAgeSignalsResult(fakeSupervisedUser);
manager.checkAgeSignals(AgeSignalsRequest.builder().build())
    .addOnSuccessListener(/* handle success */);
```

## Example 6: Supervised minor with pending significant change

### Kotlin

```kotlin
val fakePendingChangeUser = AgeSignalsResult.builder()
    .setAgeRangeSource(AgeRangeSource.TIER_B)
    .setAgeLower(13)
    .setAgeUpper(15)
    .setSignificantChangeStatus(SignificantChangeStatus.PENDING)
    .setInstallId("fake_install_id_123")
    .build()

val manager = FakeAgeSignalsManager()
manager.setNextAgeSignalsResult(fakePendingChangeUser)
manager.checkAgeSignals(AgeSignalsRequest.builder().build())
    .addOnSuccessListener { /* handle success */ }
```

### Java

```java
AgeSignalsResult fakePendingChangeUser = AgeSignalsResult.builder()
    .setAgeRangeSource(AgeRangeSource.TIER_B)
    .setAgeLower(13)
    .setAgeUpper(15)
    .setSignificantChangeStatus(SignificantChangeStatus.PENDING)
    .setInstallId("fake_install_id_123")
    .build();

FakeAgeSignalsManager manager = new FakeAgeSignalsManager();
manager.setNextAgeSignalsResult(fakePendingChangeUser);
manager.checkAgeSignals(AgeSignalsRequest.builder().build())
    .addOnSuccessListener(/* handle success */);
```

## Example 7: Supervised minor with approved significant change

### Kotlin

```kotlin
val fakeApprovedChangeUser = AgeSignalsResult.builder()
    .setAgeRangeSource(AgeRangeSource.TIER_B)
    .setAgeLower(13)
    .setAgeUpper(15)
    .setSignificantChangeStatus(SignificantChangeStatus.APPROVED)
    .setSignificantChangeApprovalDate(Date(1777939200000L)) // e.g., 2026-05-01
    .setInstallId("fake_install_id_123")
    .build()

val manager = FakeAgeSignalsManager()
manager.setNextAgeSignalsResult(fakeApprovedChangeUser)
manager.checkAgeSignals(AgeSignalsRequest.builder().build())
    .addOnSuccessListener { /* handle success */ }
```

### Java

```java
AgeSignalsResult fakeApprovedChangeUser = AgeSignalsResult.builder()
    .setAgeRangeSource(AgeRangeSource.TIER_B)
    .setAgeLower(13)
    .setAgeUpper(15)
    .setSignificantChangeStatus(SignificantChangeStatus.APPROVED)
    .setSignificantChangeApprovalDate(new Date(1777939200000L)) // e.g., 2026-05-01
    .setInstallId("fake_install_id_123")
    .build();

FakeAgeSignalsManager manager = new FakeAgeSignalsManager();
manager.setNextAgeSignalsResult(fakeApprovedChangeUser);
manager.checkAgeSignals(AgeSignalsRequest.builder().build())
    .addOnSuccessListener(/* handle success */);
```

## Example 8: Simulating API exceptions

### Kotlin

```kotlin
val manager = FakeAgeSignalsManager()
manager.setNextAgeSignalsException(AgeSignalsException(AgeSignalsErrorCode.NETWORK_ERROR))
manager.checkAgeSignals(AgeSignalsRequest.builder().build())
    .addOnFailureListener { /* handle error */ }
```

### Java

```java
FakeAgeSignalsManager manager = new FakeAgeSignalsManager();
manager.setNextAgeSignalsException(new AgeSignalsException(AgeSignalsErrorCode.NETWORK_ERROR));
manager.checkAgeSignals(AgeSignalsRequest.builder().build())
    .addOnFailureListener(/* handle error */);
```

## Testing with license testers

Ordinarily, the Play Age Signals API is blocked and returns an `APP_NOT_OWNED`
error for apps that aren't updated through Google Play. License testers can bypass
this check, meaning you can sideload apps to test your live Age Signals API
integration. This lets you use debug builds with debug signatures without
uploading the new version of your app. Note that the application's package
name must exactly match the app that is configured for Google Play, and the
active Google Account on the testing device must be registered as a license
tester for your Google Play Console account.