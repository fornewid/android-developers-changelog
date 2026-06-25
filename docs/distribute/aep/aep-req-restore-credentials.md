---
title: https://developer.android.com/distribute/aep/aep-req-restore-credentials
url: https://developer.android.com/distribute/aep/aep-req-restore-credentials
source: md.txt
---

Implement the Restore Credentials API to provide an automatic sign in experience
for users during Android-to-Android transition or app restoration. This enables
apps to automatically re-establish a user's signed-in state on a new device,
eliminating the friction of manual credential entry and preventing app
abandonment during critical re-engagement moments, while also improving the
app's security posture.

## Required implementation

To qualify for AEP, your app must successfully integrate the Restore Credentials
API in its latest production version. For the avoidance of doubt, restore
credentials works with all accepted SSO providers from the [phishing resistant
authentication guideline](https://developer.android.com/distribute/aep/aep-req-phishing-resistant-auth#accepted-federated).

## Guideline applicability

This guideline applies to:

- Apps that want to qualify for AEP and require user sign-in for optional or mandatory functionalities.
- Phone, tablet, and foldable form factors.

## Exemptions

The following exemptions apply for this guideline:

- Apps without an account login functionality.
- Apps with high-security needs, short-lived sessions, or under regulatory compliance requirements, such as Banking, Fintech, Healthcare, and Government.
- Apps already using the Block Store API as of September 30, 2026 for the purpose of restoring sign in states are not required to migrate.

## Feature documentation and resources

The following resources provide implementation guidance and technical details on
the **Restore Credentials API**. These resources are for your reference only and
don't contain additional program requirements.

- [About Restore Credentials](https://developer.android.com/identity/sign-in/restore-credentials)
- [Overview of Block Store](https://developer.android.com/identity/block-store)