---
title: https://developer.android.com/identity/credential-manager/signal-api-rp
url: https://developer.android.com/identity/credential-manager/signal-api-rp
source: md.txt
---

When a user creates a passkey, the [relying party server](https://developer.android.com/identity/credential-manager#authentication-terminology) saves certain
details, while the credential provider, such as Google Password Manager, saves
others. Specifically:

- The relying party server saves the public key credential.
- The credential provider saves the username, display name, private key, and other associated metadata. This metadata helps users identify and select the required passkey during sign-in.

Potential inconsistencies between the data saved on the relying party server and
the credential provider can lead to bad user experiences. Issues may arise in
the following scenarios:

- A credential is deleted on the relying party server but not on the credential provider, which results in the credential provider displaying the deleted credential to the user.
- A username or display name is updated on the relying party server but not on the credential provider, which results in the credential provider showing the outdated details.

Credential Manager's **Signal API** lets relying parties communicate with the
credential providers to delete credentials and to update user metadata, such as
the username and display name. There are three supported request types for
different scenarios:

- `SignalUnknownCredentialRequest`

  - Indicates that a specific credential is no longer valid and should be hidden from or removed from the credential provider.
- `SignalAllAcceptedCredentialIdsRequest`

  - Provides a list of accepted credential IDs to the credential provider.
- `SignalCurrentUserDetailsRequest`

  - Updates the user's metadata details.

## Version compatibility

The Signal API is available on devices that run Android 15 or higher, and is
available starting from version `1.6.0-beta03` of the [androidx.credentials](https://developer.android.com/jetpack/androidx/releases/credentials)
library.

## Implementation

To use the Signal API, follow these steps:

1. Add the Credential Manager dependency to your project.

   > [!NOTE]
   > **Note:** The Signal API is available starting with `credentials` 1.6.0-beta03, however when possible, use the [latest version](https://developer.android.com/jetpack/androidx/releases/credentials) of the library.


   ### Kotlin

   ```kotlin
   dependencies {
       implementation("androidx.credentials:credentials:1.6.0-rc02")
   }
   ```

   ### Groovy

   ```groovy
   dependencies {
       implementation "androidx.credentials:credentials:1.6.0-rc02"
   }
   ```

   <br />

2. Call the Signal API

   To send a signal request to the credential provider, use a supported signal
   request. Each of the signal request types requires a JSON request, as shown
   in the following examples:
   - **Unknown credential** (`SignalUnknownCredentialRequest`)

     Use [`SignalUnknownCredentialRequest`](https://developer.android.com/reference/androidx/credentials/SignalUnknownCredentialRequest) to signal that a credential is
     rejected and considered unknown. When the credential provider receives
     this signal, it hides or deletes the credential.

     **Usage**

     Use this signal when the relying party fails to verify a passkey
     assertion. This implies that the passkey is invalid and must be
     hidden from or removed by the credential provider.

     The required JSON parameters for this request are `rpId` and
     `credentialId`. For more information about the JSON structure, see
     [signalUnknownCredential options](https://w3c.github.io/webauthn/#dom-publickeycredential-signalunknowncredential).

         credentialManager.signalCredentialState(
             SignalUnknownCredentialRequest(
                 requestJson = JSONObject().apply {
                     put("rpId", rpId /* [String] RP ID of the relying party */)
                     put("credentialId", credentialId /* [String] Credential ID of the credential to be hidden or deleted */)
                 }.toString()
             )
         )

   - **All accepted credentials** (`SignalAllAcceptedCredentialIdsRequest`)

     Use `SignalAllAcceptedCredentialIdsRequest` to notify credential
     providers with the set of all accepted credentials. Once the signal is
     received by the credential provider, the credential provider hides or
     deletes any credentials that are not included in this list, or unhides
     any previously hidden credentials that are now included in the list.

     > [!NOTE]
     > **Note:** When a user is authenticated, prefer this signal over `SignalUnknownCredentialRequest`.

     **Usage**

     Use this signal when a passkey verification fails by the relying party.
     This failure means that the passkey is invalid and must be hidden from
     or removed by the credential provider. You can also use this signal
     whenever you need to broadcast the set of known credential IDs to
     credential providers.

     The required JSON parameters for this request are `rpId`, `userId`, and
     `allAcceptedCredentialIds`. For more information about the JSON
     structure, see [signalAllAcceptedCredential options](https://w3c.github.io/webauthn/#dom-publickeycredential-signalallacceptedcredentials).

         credentialManager.signalCredentialState(
             SignalAllAcceptedCredentialIdsRequest(
                 requestJson = JSONObject().apply {
                     put("rpId", rpId /* [String] RP ID of the relying party */)
                     put("userId", userId /* [String] User ID of the current user */)
                     put(
                         "allAcceptedCredentialIds",
                         JSONArray(credentialIdsList /* [List<String>] List of accepted Credential IDs */)
                     )
                 }.toString()
             )
         )

   - **Current user details** (`SignalCurrentUserDetailsRequest`)

     Use `SignalCurrentUserDetailsRequest` to notify credential providers
     that metadata, such as the username and display name for a given user,
     has been updated and should appear in the credential provider.

     **Usage**

     Use this signal when the user or the relying party updates passkey
     metadata associated with the user account.

     The required JSON parameters for this request are `rpId`, `userId`,
     `name`, and `displayName`. For more information about the JSON
     structure, see [signalCurrentUserDetails options](https://w3c.github.io/webauthn/#dom-publickeycredential-signalcurrentuserdetails).

         credentialManager.signalCredentialState(
             SignalCurrentUserDetailsRequest(
                 requestJson = JSONObject().apply {
                     put("rpId", rpId /* [String] RP ID of the relying party */)
                     put("userId", userId /* [String] User ID of the current user */)
                     put("name", name /* [String] New Name to be updated for the current user */)
                     put("displayName", displayName /* [String] New display name to be updated for the current user */)
                 }.toString()
             )
         )

   > [!NOTE]
   > **Note:** The Credential Manager Signal API supports background execution, though relying parties must limit call frequency to a maximum of 10 calls within any time window of 120 seconds to remain within established rate-limit thresholds. Excessive signaling may result in service throttling or request rejection.

## Test the implementation

To test your implementation of Signal API, complete the following steps:

1. Install the credential provider sample named [MyVault](https://github.com/android/identity-samples/tree/main/CredentialProvider/MyVault).

   > [!NOTE]
   > **Note:** The MyVault app is for testing purposes only.

2. Enable MyVault as a credential provider in **Settings** \> **Passwords,
   Passkeys \& Accounts** \> **Preferred Service**.

   ![The Preferred Service menu in Android settings, showing MyVault enabled as a credential provider.](https://developer.android.com/static/identity/credential-manager/images/signal-api-testing-step-2.svg)
3. Enable all notifications for MyVault in **Settings** \> **Apps** \>
   **MyVault** \> **Notifications**.

   ![The Notifications menu for the MyVault app, showing all notifications enabled.](https://developer.android.com/static/identity/credential-manager/images/signal-api-testing-step-3.svg)
4. Verify that **Pop on screen** is on for notifications in **Settings** \>
   **Apps** \> **MyVault** \> **Notifications** \> **Categories** \> **Signal API
   Notification Channel**.

   ![Signal API Notification Channel settings for MyVault, showing the 'Pop on screen' option enabled.](https://developer.android.com/static/identity/credential-manager/images/signal-api-testing-step-4.svg)
5. In your app, trigger the flows that send the signal requests to the
   credential provider. You should see notifications from MyVault on the screen.
   This verifies that the credential provider received the requests.