---
title: https://developer.android.com/google/play/age-signals/request-age-signals
url: https://developer.android.com/google/play/age-signals/request-age-signals
source: md.txt
---

This document describes how to request age signals by using the Play Age Signals
API.

The Play Age Signals 0.0.4 SDK introduces a two-function architecture
designed to simplify age signal requests and support our user choice based
model. To request age signals, use this high-level workflow:

Call the `requestAgeSignalsAccess(Activity)` method, which returns
`ageSignalsStatus`. The value of `ageSignalsStatus` can be `SHARED`,
`NOT_SHARED`, or `VERIFICATION_REQUIRED`.

- If `ageSignalsStatus == NOT_SHARED`: Your app won't get age signals in the API response.
- If `ageSignalsStatus == SHARED`: Call the `checkAgeSignals()` method. If the user or parent has decided to share the age signals, you receive age signals as part of the API response, and you can decide how to handle the response.
- If `ageSignalsStatus == VERIFICATION_REQUIRED`: The user's age is unknown and the user is in an applicable jurisdiction or region where age verification and age signals sharing is mandatory. To obtain an age signal from Google Play in these regions, ask the user to visit the Play Store to resolve their status.

The `requestAgeSignalsAccess(Activity)` method returns different values
depending on whether mandatory age sharing is applicable in a region:

- For eligible users in US states with laws requiring app stores to provide verified age information to developers, the in-app prompt is not triggered. Instead, users will be asked to verify or set up supervision when they visit the Play Store app. Use the value of `ageSignalsStatus` to determine the verification status:
  - If the user has completed age verification or parental supervision is active, the value of `ageSignalsStatus` is `SHARED`.
  - If the user has not yet verified their age or set up supervision, the value of `ageSignalsStatus` is `VERIFICATION_REQUIRED`. For more information, see [Changes to Google Play for upcoming app store bills
    for users in applicable US states](https://support.google.com/googleplay/android-developer/answer/16569691).
- For users in other regions where age sharing is based on the user's or parent's choice:
  - If the user's setting is **Ask before sharing** , the in-app prompt is shown. If the user agrees to share their age, the value of `ageSignalsStatus` is `SHARED`; otherwise, `NOT_SHARED`.
  - If the user's setting is **Always Share** , the in-app prompt is not shown, and the value of `ageSignalsStatus` is `SHARED`.
  - If the user's setting is **Never Share** , the in-app prompt is not shown, and the value of `ageSignalsStatus` is `NOT_SHARED`.
  - For supervised users, parents can choose to share the age for their child in Family Link app settings. If the parents choose to share the age the value of `ageSignalsStatus` will be `SHARED` otherwise it will be `NOT_SHARED`.

To understand how age sharing works on Google Play, including the in-app prompt
and age range sharing settings, see [Age range sharing on Google Play](https://support.google.com/googleplay/answer/17232873).

The following example shows how to request for age signals:

### Kotlin

    // 1. Initialize the AgeSignalsManager (usually in onCreate or class initialization)
    val ageSignalsManager = AgeSignalsManagerFactory.create(applicationContext)

    // 2. Request or check for age signals access.
    // Passing the current Activity allows the Play Store to render the age sharing prompt UI if required.
    val accessRequest = AgeSignalsAccessRequest.builder()
        .setActivity(this)
        .build()

    ageSignalsManager.requestAgeSignalsAccess(accessRequest)
        .addOnSuccessListener { accessResult ->
            if (accessResult.ageSignalsStatus() == AgeSignalsStatus.SHARED) {
                // The user (or parent) has agreed to share age range, or is in an eligible auto-share region.
                // Retrieve the actual age signals.
                retrieveAgeSignals(ageSignalsManager)
            } else {
                // Age signals are not shared (user didn't share age range, parent rejected the request, or not eligible).
            }
        }
        .addOnFailureListener { exception ->
            // Handle API/Play Store connection and system errors
            handleAgeSignalsError(exception)
        }

    private fun retrieveAgeSignals(manager: AgeSignalsManager) {
        // 3. Perform the actual age signals query once sharing is active.
        manager.checkAgeSignals(AgeSignalsRequest.builder().build())
            .addOnSuccessListener { ageSignalsResult ->
                val installId = ageSignalsResult.installId()
                val ageLower = ageSignalsResult.ageLower()
                val ageUpper = ageSignalsResult.ageUpper()
                val significantChangeDate = ageSignalsResult.significantChangeApprovalDate()
                val ageRangeSource = ageSignalsResult.ageRangeSource()

                if (ageLower != null) {
                    if (ageUpper != null) {
                        // The user is in a specific closed age range [ageLower, ageUpper] (e.g. [13, 15])
                    } else {
                        // The user is in the highest open-ended age band [ageLower, null] (e.g. [18, null])
                    }
                } else {
                    // Both bounds are null: The user is not sharing their age (e.g. they are a verified adult)
                }
            }
            .addOnFailureListener { exception ->
                handleAgeSignalsError(exception)
            }
    }

### Java

    // 1. Initialize the AgeSignalsManager (usually in onCreate or class initialization)
    AgeSignalsManager ageSignalsManager = AgeSignalsManagerFactory.create(getApplicationContext());

    // 2. Request or check for age signals access.
    // Passing the current Activity allows the Play Store to render the age sharing prompt UI if required.
    AgeSignalsAccessRequest accessRequest = AgeSignalsAccessRequest.builder()
        .setActivity(this)
        .build();

    ageSignalsManager.requestAgeSignalsAccess(accessRequest)
        .addOnSuccessListener(accessResult -> {
            Integer status = accessResult.ageSignalsStatus();
            if (status == AgeSignalsStatus.SHARED) {
                // The user (or parent) has agreed to share age range, or is in an eligible auto-share region.
                // Retrieve the actual age signals.
                retrieveAgeSignals(ageSignalsManager);
            } else {
                // Age signals are not shared (user didn't share age range, parent rejected the request, or not eligible).
            }
        })
        .addOnFailureListener(exception -> {
            // Handle API/Play Store connection and system errors
        });

    private void retrieveAgeSignals(AgeSignalsManager manager) {
        // 3. Perform the actual age signals query once sharing is active.
        manager.checkAgeSignals(AgeSignalsRequest.builder().build())
            .addOnSuccessListener(ageSignalsResult -> {
                String installId = ageSignalsResult.installId();
                Integer ageLower = ageSignalsResult.ageLower();
                Integer ageUpper = ageSignalsResult.ageUpper();
                Date significantChangeDate = ageSignalsResult.significantChangeApprovalDate();
                @AgeRangeSource Integer ageRangeSource = ageSignalsResult.ageRangeSource();

                if (ageLower != null) {
                    if (ageUpper != null) {
                        // The user is in a specific closed age range [ageLower, ageUpper] (e.g. [13, 15])
                    } else {
                        // The user is in the highest open-ended age band [ageLower, null] (e.g. [18, null])
                    }
                } else {
                    // Both bounds are null: The user is not sharing their age (e.g. they are a verified adult)
                }
            })
            .addOnFailureListener(exception -> {
                handleAgeSignalsError(exception);
            });
    }

## Key points about the code

- The `requestAgeSignalsAccess(Activity)` method performs a blocking check of the user's current age signals and age signals sharing status.
- After you call `requestAgeSignalsAccess(Activity)`, Play displays a built-in in-app prompt only for unsupervised users. Parents of supervised users can choose to share their child's age by managing the age sharing settings in the Family Link app.
- If the user dismisses or declines age sharing, the in-app prompt will be shown a few times before the prompt is suppressed.
- The `checkAgeSignals()` method gets the age signals value in the API response. This method returns `ageRangeSource`, `ageUpper`, `ageLower`, and other significant change values.