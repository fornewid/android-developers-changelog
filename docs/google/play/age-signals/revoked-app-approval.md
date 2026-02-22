---
title: https://developer.android.com/google/play/age-signals/revoked-app-approval
url: https://developer.android.com/google/play/age-signals/revoked-app-approval
source: md.txt
---

Parents can revoke app approval for supervised users on Android devices using the[Google Family Link](https://families.google/familylink/)app. If app approval is revoked for a supervised user, then that user will no longer be able to use your app. Google Play will notify you about the revocation.

## Before revocation

Google Play will include an`installID`in the Play Age Signals API (beta) response per user per device. You can store this`installID`on your app's backend server in anticipation of being notified about revoked app approvals.
| **Note:** The`installID`does not persist across device resets to protect user privacy. The`installID`allows Google to notify you that approval was revoked where providing this notice to you is required by law, and you are not permitted to use it for other purposes.

## After revocation

Google Play provides details about revoked app approvals by listing the`installID`for that user on the**Revoked app approvals** tab on the[Age signals](https://play.google.com/console/developers/app/age-signals)page in the Google Play Console. Here, you can download a CSV file with a list of the revoked app approvals. Revoked`installID`values are listed for 90 days before being deleted.

## Repeat approvals and revocations

If a parent re-approves the same app for a user and the device has not been reset, the same`installID`is returned in the Play Age Signals API response for the re-approved app.

If the app approval is revoked again, the same`installID`appears as a new entry in the table on the**Revoked app approvals** tab on the[Age signals](https://play.google.com/console/developers/app/age-signals)page. That means a single`installID`can appear multiple times in the revoked app approvals table, once for each revocation.