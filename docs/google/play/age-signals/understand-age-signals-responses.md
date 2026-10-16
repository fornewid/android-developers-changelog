---
title: https://developer.android.com/google/play/age-signals/understand-age-signals-responses
url: https://developer.android.com/google/play/age-signals/understand-age-signals-responses
source: md.txt
---

> [!TIP]
> **Tip:** Use the [Play Integrity API](https://developer.android.com/google/play/integrity/overview) when calling the Play Age Signals API to verify that the call is coming from an untampered version of your app on a certified Android-powered device, protecting the response from potential spoofing or abuse.

This document explains the age signal responses returned by the Play Age Signals
API.

## (Optional) Receive custom age ranges

The default age ranges that the API returns are `0-12`, `13-15`,
`16-17`, and `18+`.

Alternatively, to customize the default age ranges according to your app's
minimum ages, you can provide these minimum ages for your app on the [Age
signals page](https://play.google.com/console/developers/app/age-signals)
in your Google Play Console.

1. Go to the [Age signals](https://play.google.com/console/developers/app/age-signals) page in your Play Console.
2. On the **Custom age ranges** tab, enter up to three minimum ages for your app. Minimum ages must be at least 2 years apart and can be changed once annually.
3. Click **Save**.

The age ranges returned will override the default API response. For example:

- If you set one minimum age (15) in the Google Play Console:
  - A 0 to 14 year old will return `ageLower = 0` and `ageUpper = 14`.
  - A 15+ year old will return `ageLower = 15`.
- If you set two minimum ages (13 and 17):
  - A 0 to 12 year old, will return `ageLower = 0` and `ageUpper = 12`.
  - A 13 to 16 year old will return `ageLower = 13` and `ageUpper = 16`.
  - A 17+ year old will return `ageLower = 17`.
- If you set three minimum ages (11, 13 and 15):
  - A 0 to 10 year old will return `ageLower = 0` and `ageUpper = 10`.
  - An 11 or 12 year old will return `ageLower = 11` and `ageUpper = 12`.
  - A 13 or 14 year old will return `ageLower = 13` and `ageUpper = 14`.
  - A 15+ year old will return `ageLower = 15`.

## Age signals response fields

The Play Age Signals API (beta) response includes the following fields and
values. You are responsible for providing age-appropriate experiences using
these signals.

| Response field | Type | Values | Description |
|---|---|---|---|
| ageRangeSource | Enum | - TIER_A - TIER_B - TIER_C - TIER_D - null | - **TIER_A**: User has self declared their age. - **TIER_B**: User's age is managed by a parent or a guardian. - **TIER_C**: User's age is assessed by using credit card, email address, selfie assessment, Government ID, or Tax ID. - **TIER_D**: User's age is checked by using a combination of Government ID and selfie assessment, or Digital ID. - **null** : Returned when **ageSignalsStatus** is **NOT_SHARED** or **VERIFICATION_REQUIRED**. |
| ageLower | Integer | - 0 to 18 - null | The inclusive lower bound of the user's age range. Combine it with **ageUpper** to determine the band. Returns **null** if **ageSignalsStatus** is **NOT_SHARED** or **VERIFICATION_REQUIRED**. |
| ageUpper | Integer | - 2 to 18 - null | The inclusive upper bound of the user's age range. Returns **null** for the highest band (for example, 18+) or if **ageSignalsStatus** is **NOT_SHARED** or **VERIFICATION_REQUIRED**. |
| significantChangeStatus | Enum | - APPROVED - PENDING - DECLINED - null | This only returns a non-null value in jurisdictions where significant changes are applicable. - **APPROVED**: The most recent significant change (and all prior changes) has been approved. - **PENDING**: Parent hasn't yet approved one or more pending significant changes. - **DECLINED**: Parents denied approval for one or more significant changes. - **null** : Returned for: - All unsupervised accounts - Supervised accounts that don't have any significant changes recorded yet. |
| significantChangeApprovalDate | Date | - DateStamp - null | The effective date of the most recently approved significant change. All changes with effective dates prior to this date are also approved. Returns **null** if no changes exist. Combine it with \`significantChangeStatus\` to get the approval status for this significant change |
| installId | String | - Alphanumeric - null | An ID assigned to supervised user installs by Google Play, used for the purposes of notifying you of revoked app approval. Review the documentation for [revoked app approvals](https://developer.android.com/google/play/age-signals/revoked-app-approval). |

## Example 1

For a user who verified their age by using Digital ID and shares
it with apps, you receive the following:

- `ageRangeSource` is `AgeRangeSource.TIER_D`.
- `ageLower` is a number (for example, 18).
- `ageUpper` is `null`.
- Other response fields are `null`.

## Example 2

For an adult user who declared their age (self-declared) and shares it
with apps, you receive the following:

- `ageRangeSource` is `AgeRangeSource.TIER_A`.
- `ageLower` is a number (for example, 18).
- `ageUpper` is `null`.
- Other response fields is `null`.

## Example 3

For a supervised minor user whose age is managed by a guardian who
has shared it with apps, you receive the following:

- `ageRangeSource` is `AgeRangeSource.TIER_B`.
- `ageLower` is a number (for example, 13).
- `ageUpper` is a number (for example, 15).
- Other response fields is `null`.

## Example 4

For a user who has not agreed (or whose parent has not agreed) to age sharing,
you receive the following:

- `ageRangeSource` is `null`.
- `ageLower` is `null`.
- `ageUpper` is `null`.
- Other response fields is `null`.

## Example 5

For an adult user with an assessed age verified by using age estimation methods
(such as selfie assessment, credit card, or Tax ID) who shares it with apps,
you receive the following:

- `ageRangeSource` is `AgeRangeSource.TIER_C`.
- `ageLower` is a number (for example, 18).
- `ageUpper` is `null`.
- Other response fields is `null`.

## Example 6

For a supervised minor user whose age is managed by a guardian, with an
approved significant change and active install tracking, you receive the
following:

- `ageRangeSource` is `AgeRangeSource.TIER_B`.
- `ageLower` is a number (for example, 13).
- `ageUpper` is a number (for example, 15).
- `significantChangeStatus` is `SignificantChangeStatus.APPROVED`.
- `significantChangeApprovalDate` is a Date (for example, "2026-01-15").
- `installId` is a string identifier (for example, "abc123xyz789").