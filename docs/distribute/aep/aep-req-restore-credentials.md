---
title: https://developer.android.com/distribute/aep/aep-req-restore-credentials
url: https://developer.android.com/distribute/aep/aep-req-restore-credentials
source: md.txt
---

> Documentation index: https://developer.android.com/distribute/aep/llms.txt

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

| ID | Guideline |
|---|---|
| AEP-RC-GAA | To qualify for AEP, your app must successfully integrate the Restore Credentials API in its latest production version. For the avoidance of doubt, restore credentials works with all accepted SSO providers from the [phishing resistant authentication guideline](https://developer.android.com/distribute/aep/aep-req-phishing-resistant-auth.md.txt#accepted-federated). |

> [!NOTE]
> **Note:** Restore Credentials works alongside passwords, passkeys, and accepted federated SSO providers without requiring user-facing passkeys. Your app can verify `RestoreCredential` assertions on a WebAuthn relying party server (recommended) or, for token-based backends without WebAuthn endpoints, use the WebAuthn `largeBlob` extension on Google Play services `26.43` and higher to store and restore login session tokens directly. For architectural trade-offs and implementation steps, see [Implement Restore Credentials](https://developer.android.com/identity/sign-in/restore-credentials-implementation.md.txt).

## Guideline applicability

This guideline applies to:

- Apps that want to qualify for AEP and require user sign-in for optional or mandatory functionalities.
- Phone, tablet, and foldable form factors.

## Exemptions

The following exemptions apply for this guideline:

| ID | Exemption |
|---|---|
| AEP-RC-EAA | Apps without an account login functionality. |
| AEP-RC-EAB | Apps with high-security needs, short-lived sessions, or under regulatory compliance requirements, such as Banking, Fintech, Healthcare, and Government. |
| AEP-RC-EAC | Apps already using the Block Store API as of September 30, 2026 for the purpose of restoring sign in states are not required to migrate. |

## Feature documentation and resources

The following resources provide implementation guidance and technical details on
the **Restore Credentials API**. These resources are for your reference only and
don't contain additional program requirements.

- [About Restore Credentials](https://developer.android.com/identity/sign-in/restore-credentials.md.txt)
- [Implement Restore Credentials](https://developer.android.com/identity/sign-in/restore-credentials-implementation.md.txt)
- [Test Restore Credentials](https://developer.android.com/identity/sign-in/test-restore-credentials.md.txt)
- [Automated backup and restore testing](https://developer.android.com/studio/preview/backup-restore-testing.md.txt)
- [Restore Credentials Android skill](https://developer.android.com/agents/skills/identity/restore-credentials/skill.md.txt)
- [Overview of Block Store](https://developer.android.com/identity/block-store.md.txt)
- [Play Console Technical Quality Requirements](https://support.google.com/googleplay/android-developer/answer/17492799)