---
title: https://developer.android.com/distribute/aep/aep-req-phishing-resistant-auth
url: https://developer.android.com/distribute/aep/aep-req-phishing-resistant-auth
source: md.txt
---

In addition to any existing sign-in methods, implement a phishing-resistant
authentication method, specifically FIDO or WebAuthn-based passkey, or Single
Sign-On from an accepted federated identity provider such as Sign in with
Google.

This guideline secures your app and simplifies user sign-in by mitigating
vulnerabilities like password fatigue, credential stuffing, and phishing.

## Required implementation

To qualify for AEP, your app must successfully offer at least one approved
phishing-resistant authentication method (Passkeys or an approved Single Sign-On
provider) at sign-in in a similar prominent way.

- For Passkeys, this is verified by creating and retrieving Passkeys through the Credential Manager API.
- Apps using Sign-in with Google must be integrated through the Credential [Manager API](https://developer.android.com/identity/sign-in/legacy-gsi-migration). While other approved SSO providers are accepted, Sign-in with Google is recommended because it offers a modern authentication flow that protects users from phishing while providing a consistent, cross-platform experience.

## Guideline applicability

This guideline applies to:

- Apps that want to qualify for AEP and require user sign-in.
- Phone, tablet, foldable, XR, Wear, and Auto form factors.

## Exemptions

This guideline does not apply to apps that don't support user authentication or
a signed-in state.

Additionally, you can submit alternative federated identity providers for
evaluation here if you believe they should be considered alongside the [accepted
providers](https://developer.android.com/distribute/aep/aep-req-phishing-resistant-auth#accepted-federated).

## Accepted Federated Identity Providers for SSO

The following Consumer Federated Identity Providers are accepted for the Single
Sign-On requirement:

- Sign in with Google
- Sign in with Apple
- Microsoft Account (Consumer)
- Shop.app
- Amazon Login
- GitHub Login
- Discord Sign-In
- Line or Kakao Login
- WeChat Login
- Facebook Login

This list is reviewed periodically as the federated identity ecosystem evolves.
Evaluation criteria include:

- User safety and privacy controls
- Developer and integration experience (in alignment with native Android Credential Manager API, open-standards compliance)
- Active consumer footprint

## Feature documentation and resources

The following resources provide implementation guidance and technical details on
**Phishing Resistant Authentication**. These resources are for your reference
only and don't contain additional program requirements.

- [Credential Manager Guide](https://developer.android.com/identity/sign-in/credential-manager)
- [Sign in with Google Integration](https://developer.android.com/identity/sign-in/credential-manager-siwg)