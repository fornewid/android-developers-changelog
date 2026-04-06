---
title: Review revoked app approvals  |  Play Age Signals  |  Android Developers
url: https://developer.android.com/google/play/age-signals/revoked-app-approval
source: html-scrape
---

On March 17, 2026, the Play Age Signals API starts rolling out responses for users in Brazil in [preparation for requirements under Digital ECA](https://support.google.com/googleplay/android-developer/answer/6223646#digital_eca_requirements). Ongoing updates will be provided in advance of [age verification bills](http://support.google.com/googleplay/android-developer/answer/16569691) in US states, which are slated to go into effect in Utah and Louisiana in May and July 2026 respectively. API responses for users in Texas not live due to a Federal District Court preliminary injunction.

* [Android Developers](https://developer.android.com/)
* [Google Play](https://developer.android.com/distribute)
* [Play Age Signals](https://developer.android.com/google/play/age-signals)

# Review revoked app approvals Stay organized with collections Save and categorize content based on your preferences.



**Note:** Functionality for revoked app approvals is not yet live in Google Play
Console.

Parents can revoke app approval for supervised users on Android devices using
the [Google Family Link](https://families.google/familylink/) app. If app
approval is revoked for a supervised user, then that user will no longer be able
to use your app. Google Play will notify you about the revocation.

## Before revocation

Google Play will include an `installID` in the Play Age Signals API (beta)
response per user per device. You can store this `installID` on your app's
backend server in anticipation of being notified about revoked app approvals.

**Note:** The `installID` does not persist across device resets to protect user
privacy. The `installID` allows Google to notify you that approval was revoked
where providing this notice to you is required by law, and you are not
permitted to use it for other purposes.

## After revocation

Google Play provides details about revoked app approvals by listing the
`installID` for that user on the **Revoked app approvals** tab on the
[Age signals](https://play.google.com/console/developers/app/age-signals) page in the Google Play Console. Here, you can download a
CSV file with a list of the revoked app approvals. Revoked `installID`
values are listed for 90 days before being deleted.

## Repeat approvals and revocations

If a parent re-approves the same app for a user and the device has not been
reset, the same `installID` is returned in the Play Age Signals API response
for the re-approved app.

If the app approval is revoked again, the same `installID` appears
as a new entry in the table on the **Revoked app approvals** tab
on the [Age signals](https://play.google.com/console/developers/app/age-signals) page. That means a single `installID` can appear
multiple times in the revoked app approvals table, once for each revocation.

[Previous

arrow\_back

Notify significant changes](/google/play/age-signals/notify-significant-changes)

[Next

Test age signals

arrow\_forward](/google/play/age-signals/test-age-signals-api)