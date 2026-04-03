---
title: Make Credential Manager calls on behalf of other parties for privileged apps  |  Identity  |  Android Developers
url: https://developer.android.com/identity/sign-in/privileged-apps
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [Security](https://developer.android.com/security)
* [Identity](https://developer.android.com/identity)
* [Guides](https://developer.android.com/identity/credential-manager)

# Make Credential Manager calls on behalf of other parties for privileged apps Stay organized with collections Save and categorize content based on your preferences.




Privileged apps such as web browsers can make a Credential Manager call on
behalf of other relying parties by setting the `origin` parameter in Credential
Manager's [`GetCredentialRequest()`](/reference/androidx/credentials/GetCredentialRequest#GetCredentialRequest(kotlin.collections.List,kotlin.String,kotlin.Boolean,android.content.ComponentName,kotlin.Boolean)) and
[`CreatePublicKeyCredentialRequest()`](/reference/androidx/credentials/CreatePublicKeyCredentialRequest#CreatePublicKeyCredentialRequest(kotlin.String,kotlin.ByteArray,kotlin.Boolean,kotlin.String,kotlin.Boolean)) methods.

The [`origin`](https://www.w3.org/TR/webauthn-2/#dom-collectedclientdata-origin) represents the application or website that a
request comes from, and is used by passkeys to protect against phishing attacks.
An app's servers are required to check the client data `origin` against an
allowlist of approved apps and websites. If the server receives a request from
an app or website from an unrecognized origin, the request should be rejected.
This document describes how to set the origin for such privileged calling apps,
and how to verify such apps are allowed to make calls on behalf of other
parties.

## Set the origin of the calling app

To get credentials on behalf of another relying party, the credential provider
that supplies the credentials must add your app to a list of privileged callers
that are allowed to get such access. Then, use [`setOrigin()`](/reference/android/credentials/GetCredentialRequest.Builder#setOrigin(java.lang.String)) on
[`createCredential()`](/reference/kotlin/androidx/credentials/CredentialManager#createCredential(android.content.Context,androidx.credentials.CreateCredentialRequest)) and [`getCredential()`](/reference/kotlin/androidx/credentials/CredentialManager#getCredential(android.content.Context,androidx.credentials.PrepareGetCredentialResponse.PendingGetCredentialHandle)) requests to set the
`origin` value.

**Note:** The `origin` parameter in the `createCredential()` and `getCredential()`
methods is only effective in API levels 34 (Android 14) and higher.

For privileged apps such as web browsers that need to handle third party
credentials, Google Password Manager requires approval to handle those
credentials. This ensures that only trusted apps are able to access and manage
user credentials for external services. To be approved for handling third party
credentials, [complete the request form](https://docs.google.com/forms/d/e/1FAIpQLScRuk9tTg0QPfSWl9SbpbIorX8xx2FCXlmoUYftCX2MxG4qyg/viewform) to open a ticket and
have your request reviewed.