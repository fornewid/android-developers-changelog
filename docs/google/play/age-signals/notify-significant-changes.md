---
title: https://developer.android.com/google/play/age-signals/notify-significant-changes
url: https://developer.android.com/google/play/age-signals/notify-significant-changes
source: md.txt
---

Regulations in some jurisdictions and regions may require you to notify Google Play when you make certain types of changes, sometimes referred to as*significant changes*. You are responsible for determining when you are required to notify Google Play of such a change.

There are important points to understand about how significant changes work on Google Play:

- **Google Play handles significant changes independently of app releases.**When you notify Google Play about a significant change, Play will raise an approval request to the parents of supervised users in the applicable jurisdictions and regions. You can use the Play Age Signals API to track the most recently approved significant change and the approval status of any pending significant changes. You are responsible for restricting access to any content or functionality in your app relating to significant changes based on the approval status you receive from the Play Age Signals API. Only supervised users, and not verified users, have a significant change approval status in the API response.

- **Significant changes are cumulative.**Notifying Play about a new significant change will include any pending and denied significant changes in a new parent approval request. When a parent grants approval, they approve, in a single action, all pending significant changes that have not yet been approved since the last approval.

## Example significant change workflow

This is an example of a significant change workflow:

1. You can notify Google Play of an upcoming significant change with an effective from date of YYYY-MM-DD on the[Age signals](https://play.google.com/console/developers/app/age-signals)page in your Play Console.
2. You can cancel significant changes up to 48 hours before the effective date.
3. **Before** YYYY-MM-DD, your app can receive age signals from the Play Age Signals API, including the existing`mostRecentApprovalDate`of the significant change that was approved before YYYY-MM-DD.
4. **From** YYYY-MM-DD, your app can receive age signals relating to the new significant change:
   1. **userStatus** is**SUPERVISED** and**mostRecentApprovalDate** is YYYY-MM-DD: The parent has approved the significant change(s) up to and including the significant change with the*effective from*date YYYY-MM-DD.
   2. **userStatus** is**SUPERVISED_APPROVAL_PENDING** : The parent has not yet approved the significant change(s) after the`mostRecentApprovalDate`.
   3. **userStatus** is**SUPERVISED_APPROVAL_DENIED** : The parent has denied approval for the significant change(s) after the`mostRecentApprovalDate`.

The following steps explain in detail how to notify Play about significant changes.

## Step 1: Notify Play about an upcoming significant change

You can submit a significant change on the[Age signals](https://play.google.com/console/developers/app/age-signals)page in your Google Play Console. To submit a significant change, you will need to provide:

- **Effective from date (required):**A future date when the change takes effect. Changes are effective from 00:00 UTC.
- **Description (optional):**A short description of the update (up to 500 characters). The description you provide will be shown verbatim to parents. You can provide the description in all languages that your app supports.

You can submit up to 3 significant changes up to 90 days in advance. You can view and cancel upcoming significant changes on the Age signals page in your Play Console up to 48 hours before the significant change's effective from date. You can view significant changes that you previously submitted in the Play Console activity log.
| **Tip:** Bookmark the[Age signals](https://play.google.com/console/developers/app/age-signals)page in your Google Play Console to return to it at any time.

## Step 2: Use the Play Age Signals API to monitor significant change approval statuses

Google Play will only provide notification of significant changes to users based in jurisdictions where such notification is required by law. From the effective date, Google Play will start triggering a request for parents to approve the significant change for supervised users in applicable regions and change the supervised user's approval status in the Play Age Signals API to pending approval until the parent either approves or denies the request. If a description was provided, parents will see it in the approval request. If multiple significant changes are pending approval, parents will see at most the 10 most recent descriptions.
| **Important:** Significant changes are cumulative. When a parent grants approval, they approve all pending significant changes that have not yet been approved since the last approval in a single action and the most recent ApprovalDate is updated to the*effective from*date of the most recent significant change.

You can use the user status and the most recent approval date to grant access only to age-appropriate app experiences associated with significant changes that have been approved.