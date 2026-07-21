---
title: https://developer.android.com/google/play/age-signals/test-age-signals-api
url: https://developer.android.com/google/play/age-signals/test-age-signals-api
source: md.txt
---

To verify your app's handling of various age signals and age sharing
status, use the [FakeAgeSignalsManager](https://developer.android.com/google/play/age-signals/reference/com/google/android/play/agesignals/testing/FakeAgeSignalsManager) provided in the SDK testing artifact.
`FakeAgeSignalsManager` lets you simulate API responses for unit and integration
testing by replacing your production AgeSignalsManager instance.

To simulate different response types using the Play Age Signals API SDK
version 0.0.4, see the following examples:

## Example 1: Request access (user shared age)

### Kotlin

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

### Java

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

## Example 2: Request access (user didn't share age)

### Kotlin

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

### Java

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

## Example 3: Verified adult (18+ years)

### Kotlin

    val fakeVerifiedUser = AgeSignalsResult.builder()
        .setAgeRangeSource(AgeRangeSource.TIER_D)
        .setAgeLower(18)
        .build()

    val manager = FakeAgeSignalsManager()
    manager.setNextAgeSignalsResult(fakeVerifiedUser)
    manager.checkAgeSignals(AgeSignalsRequest.builder().build())
        .addOnSuccessListener { /* handle success */ }

### Java

    AgeSignalsResult fakeVerifiedUser = AgeSignalsResult.builder()
        .setAgeRangeSource(AgeRangeSource.TIER_D)
        .setAgeLower(18)
        .build();

    FakeAgeSignalsManager manager = new FakeAgeSignalsManager();
    manager.setNextAgeSignalsResult(fakeVerifiedUser);
    manager.checkAgeSignals(AgeSignalsRequest.builder().build())
        .addOnSuccessListener(/* handle success */);

## Example 4: Supervised minor (13-15 years old)

### Kotlin

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

### Java

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

## Example 5: Supervised minor with pending significant change

### Kotlin

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

### Java

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

## Example 6: Supervised minor with approved significant change

### Kotlin

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

### Java

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

## Example 7: Simulating API exceptions

### Kotlin

    val manager = FakeAgeSignalsManager()
    manager.setNextAgeSignalsException(AgeSignalsException(AgeSignalsErrorCode.NETWORK_ERROR))
    manager.checkAgeSignals(AgeSignalsRequest.builder().build())
        .addOnFailureListener { /* handle error */ }

### Java

    FakeAgeSignalsManager manager = new FakeAgeSignalsManager();
    manager.setNextAgeSignalsException(new AgeSignalsException(AgeSignalsErrorCode.NETWORK_ERROR));
    manager.checkAgeSignals(AgeSignalsRequest.builder().build())
        .addOnFailureListener(/* handle error */);