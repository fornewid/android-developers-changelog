---
title: Issue digital credentials to wallets in an Android app  |  Android Developers
url: https://developer.android.com/agents/skills/identity/digital-credentials/credential-issuer/skill
source: html-scrape
---

# Issue digital credentials to wallets in an Android app Stay organized with collections Save and categorize content based on your preferences.





Build an Android credential issuer app that provisions digital credentials into
a user's holder wallet over OpenID4VCI (`openid4vci-v1`) using
`CreateDigitalCredentialRequest` and `credentialManager.createCredential()`,
alongside backend hardware-backed Android Keystore attestation
(`android_keystore_attestation`). When reviewing digital credential
architecture, client issuance flows, or Keystore attestation requirements,
consult [Digital credentials overview](/identity/digital-credentials), [Issue credentials](/identity/digital-credentials/credential-issuer/issue-credentials), and
[Hardware-backed attestation](/identity/digital-credentials/credential-issuer/keystore-attestation). When building a holder wallet app that
receives and stores issued credentials, suggest the `credential-holder` skill;
when requesting credentials as a verifier, suggest the `credential-verifier`
skill.

## Prerequisites and setup

* **Android version compatibility:** Supported with
  `androidx.credentials:credentials` `1.6.0` and higher
  (`minSdk` 23 or higher).
* **Build config permission:** Ask for user confirmation before modifying
  `settings.gradle.kts`, root `build.gradle.kts`, or
  `gradle/libs.versions.toml`, unless already requested by the user or running
  non-interactively.
* **Dependencies and package mapping:** Add the Credential Manager artifacts to
  the app module build script (`app/build.gradle.kts` or `app/build.gradle`;
  when checking full dependency declarations, consult [Issue credentials](/identity/digital-credentials/credential-issuer/issue-credentials)):

| Artifact | Key classes, constructor signatures, and package |
| --- | --- |
| `androidx.credentials:credentials:1.7.0-alpha03` (or `1.6.0`+) | `CredentialManager`, `CreateDigitalCredentialRequest(requestJson: String, origin: String?)`, `CreateDigitalCredentialResponse(responseJson: String)`, and `ExperimentalDigitalCredentialApi` in `androidx.credentials`; `CreateCredentialException`, `CreateCredentialCancellationException`, `CreateCredentialInterruptedException`, `CreateCredentialNoCreateOptionException`, `CreateCredentialUnsupportedException`, `CreateCredentialProviderConfigurationException`, `CreateCredentialCustomException`, and `CreateCredentialUnknownException` in `androidx.credentials.exceptions` |
| `androidx.credentials:credentials-play-services-auth:1.7.0-alpha03` (or `1.6.0`+) | Google Play services provider integration for Credential Manager |

### Expected inputs and file scope

* **Required inputs:** The `credential_issuer` URL,
  `credential_configuration_ids`, and grant type (`pre-authorized_code` with
  optional `tx_code` or `authorization_code` with `issuer_state`).
* **Files to modify:** `app/build.gradle.kts`, issuer client or repository
  classes, ViewModels, and UI screens (such as `MainActivity.kt`).

## Codebase exploration

Before modifying files, inspect the Android project:

1. **Validate baseline build and inspect configuration:** Run
   `./gradlew assembleDebug` to confirm the project compiles before making
   changes, and check `app/build.gradle.kts` and `gradle/libs.versions.toml`
   for `minSdk` and `androidx.credentials` dependencies.
2. **Locate target UI entry points:** Identify the `Activity` or Compose screen
   (such as `MainActivity.kt` or `TasksScreen.kt`) where credential issuance is
   triggered so `credentialManager.createCredential()` receives an `Activity`
   `Context`.

## Critical implementation mandates

Follow the step-by-step client implementation in [Issue credentials](/identity/digital-credentials/credential-issuer/issue-credentials) and
apply these non-obvious rules:

* **Opt in to experimental APIs:** Annotate classes or functions referencing
  `CreateDigitalCredentialRequest` or `CreateDigitalCredentialResponse` with
  `@OptIn(androidx.credentials.ExperimentalDigitalCredentialApi::class)`.
* **Enclose the OpenID4VCI request JSON in root `{ ... }` braces:** The example
  JSON snippet in [Issue credentials](/identity/digital-credentials/credential-issuer/issue-credentials) starts directly with `"requests":
  [...]` without outer braces. Always wrap the root payload in `{ "requests":
  [...] }` with `"protocol": "openid4vci-v1"` (not `"openid4vci1.0"`) and a
  `"data"` object specifying `"credential_issuer"`,
  `"credential_configuration_ids"` (a JSON array of one or more credential
  configuration IDs), and `"grants"` (such as
  `urn:ietf:params:oauth:grant-type:pre-authorized_code` or
  `authorization_code`).
* **Pass `origin = null` in standard Android issuer apps:** When instantiating
  `CreateDigitalCredentialRequest(requestJson = issuanceRequestJson, origin =
  null)`, always pass `origin = null` for standard Android issuer apps. Only
  privileged browsers holding `android.permission.CREDENTIAL_MANAGER_SET_ORIGIN`
  pass a non-null `origin`; passing a non-null `origin` from a standard app
  throws a `SecurityException`.
* **Handle asynchronous issuance completion and exceptions:** Cast the returned
  `CreateCredentialResponse` from `credentialManager.createCredential()` to
  `CreateDigitalCredentialResponse` and inspect `response.responseJson` (noting
  that actual credential provisioning can complete asynchronously after the
  holder accepts the offer), and catch all `CreateCredentialException` subtypes
  shown in [Issue credentials](/identity/digital-credentials/credential-issuer/issue-credentials).

## Troubleshooting

| Symptom | Cause | Fix |
| --- | --- | --- |
| Experimental API compilation error | `CreateDigitalCredentialRequest` and `CreateDigitalCredentialResponse` require opt-in | Add `@OptIn(androidx.credentials.ExperimentalDigitalCredentialApi::class)` to the calling class or function. |
| `SecurityException` on `createCredential` | Non-null `origin` passed by a non-privileged Android app | Pass `origin = null` to `CreateDigitalCredentialRequest`. |
| `CreateCredentialNoCreateOptionException` thrown | No installed wallet app has registered matching `openid4vci-v1` creation options | Verify the JSON is wrapped in `{ "requests": [...] }` with `"protocol": "openid4vci-v1"` and prompt the user to install or set up a compatible digital wallet app. |
| Keystore attestation generation fails on holder device | `c_nonce` exceeds 128 UTF-8 bytes | Restrict `c_nonce` generation on the issuer's nonce endpoint to at most 128 UTF-8 bytes. |

## Verification and reporting guidelines

* [ ] Run `./gradlew assembleDebug` to verify the Android project compiles
  without errors.
* [ ] Verify `app/build.gradle.kts` includes `androidx.credentials:credentials`
  and `androidx.credentials:credentials-play-services-auth`.
* [ ] Verify `CreateDigitalCredentialRequest` passes `origin = null` and uses a
  valid `{ "requests": [...] }` JSON object with `"protocol": "openid4vci-v1"`.
* [ ] Verify `credentialManager.createCredential()` is called with an `Activity`
  `Context` and catches `CreateCredentialException` subtypes.

### Post-implementation warnings for the human developer

Present these backend reminders from [Hardware-backed attestation](/identity/digital-credentials/credential-issuer/keystore-attestation) after
completing client-side issuer code changes:

1. **Issuer `.well-known` attestation metadata:** In the issuer backend's
   `credential_configurations_supported` metadata, declare
   `proof_types_supported.android_keystore_attestation` with
   `proof_signing_alg_values_supported` (such as `["ES256"]`) and
   `key_attestations_required` (`key_mint_security_level` in `["Software",
   "TrustedEnvironment", "StrongBox"]` and `user_auth_types` in `["LSKF",
   "BIOMETRIC"]`).
2. **Nonce size limit (128 bytes max):** Verify `c_nonce` values generated by
   the issuer's nonce endpoint are at most 128 UTF-8 bytes so they fit in the
   Android Keystore `attestationChallenge` `OCTET_STRING`.
3. **Backend X.509 attestation chain validation:** Validate each Base64-encoded
   X.509 certificate chain in `proofs.android_keystore_attestation` on the
   issuer's backend server (for example, using the server-side Android Key
   Attestation library): verify the chain back to the Google hardware Root of
   Trust, check the certificate revocation status list, verify the
   `attestationChallenge` in the leaf certificate matches `c_nonce`, and check
   `keyMintSecurityLevel` and `userAuthType` against the issuer's metadata
   requirements before signing credentials.

## Antipatterns

* **NEVER** implement digital credential issuance using only generic Android
  share intents (`Intent.ACTION_SEND`) or local storage without integrating
  `CredentialManager` and `CreateDigitalCredentialRequest`.
* **NEVER** pass a non-null `origin` to `CreateDigitalCredentialRequest` from a
  standard Android issuer app; always pass `origin = null`.
* **NEVER** generate a `c_nonce` longer than 128 UTF-8 bytes for Android
  Keystore attestation.

## Best practices

* **MUST** annotate classes or functions using `CreateDigitalCredentialRequest`
  and `CreateDigitalCredentialResponse` with
  `@OptIn(androidx.credentials.ExperimentalDigitalCredentialApi::class)`.
* **MUST** handle `CreateCredentialException` subtypes (including
  `CreateCredentialCancellationException`,
  `CreateCredentialNoCreateOptionException`, and
  `CreateCredentialUnsupportedException`) when calling
  `credentialManager.createCredential()`.
* **MUST** verify the `attestationChallenge` in the leaf certificate extension
  matches `c_nonce` and check Android Keystore certificate revocation during
  backend key attestation validation.