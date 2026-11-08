---
title: https://developer.android.com/identity/sign-in/restore-credentials-implementation-common
url: https://developer.android.com/identity/sign-in/restore-credentials-implementation-common
source: md.txt
---

## Version compatibility

Credential Manager's Restore Credentials works on devices running Android 9 (API
level 28) and higher, Google Play services (GMS) core version `242200000`
(v24.22) or higher, and version `1.5.0` or higher of the `androidx.credentials`
library. On devices without Google Play services or with an older GMS version,
catch `CreateCredentialProviderConfigurationException` and
`GetCredentialProviderConfigurationException` so your app falls back gracefully
to standard sign-in.

## Prerequisites

Configure a WebAuthn [relying party server](https://developer.android.com/identity/credential-manager#authentication-terminology) similar to the server for
[passkeys](https://developer.android.com/identity/passkeys). If you already have a [server](https://developers.google.com/identity/passkeys/developer-guides/server-introduction) set up to handle authentication
with passkeys, you can reuse the same WebAuthn registration and assertion
endpoints for restore keys.

> [!NOTE]
> **Note:** While the server-side cryptographic validation is the same for passkeys and restore keys, your client-side app can support restore keys without supporting user-facing passkeys. Store restore keys with a distinct credential flag in your backend database so they don't appear in user-facing passkey management screens.

## Dependencies

Add the following dependencies to your app module's `build.gradle` file:

### Kotlin

```kotlin
dependencies {
    implementation("androidx.credentials:credentials:1.7.0-alpha03")
    implementation("androidx.credentials:credentials-play-services-auth:1.7.0-alpha03")
}
```

### Groovy

```groovy
dependencies {
    implementation "androidx.credentials:credentials:1.7.0-alpha03"
    implementation "androidx.credentials:credentials-play-services-auth:1.7.0-alpha03"
}
```

Restore Credentials is available from version `1.5.0` and higher of the
`androidx.credentials` library. However, it's recommended to use the latest
stable versions of the dependencies where possible.

### How `android:allowBackup` affects Restore Credentials

The [`android:allowBackup`](https://developer.android.com/guide/topics/manifest/application-element#allowbackup) manifest attribute controls app data backup,
which interacts with Restore Credentials in three distinct ways:

- **Restore key transfer (`allowBackup` independent)** : Google Play services transfers the `RestoreCredential` key pair using end-to-end encrypted cloud backup or local device-to-device (D2D) transfer regardless of whether `android:allowBackup` is `true` or `false`. For D2D transfers, the restore key always transfers; the only condition under which it isn't transferred is during a cloud backup when the user has opted out of cloud backup in Android Settings.
- **Background restoration in `BackupAgent` (requires
  `android:allowBackup="true"`)** : Silent background sign-in before the user opens the app on the new device (`BackupAgent.onRestoreFinished()`) only runs when `android:allowBackup="true"` and `android:backupAgent` are configured in your manifest. If `android:allowBackup="false"`, restore the session when the user first launches your main `Activity`. You can also implement both approaches to make restoration more robust.
- **Android Studio Cloud Backup testing (requires
  `android:allowBackup="true"`)** : Testing the **Cloud** backup type in Android Studio's Backup and Restore tool requires `android:allowBackup="true"`, whereas **Device to Device** testing works regardless of `allowBackup`.

## Overview

Restore Credentials follows a three-stage lifecycle across the user's previous
and new devices:

1. [**Create a restore key on the previous device**](https://developer.android.com/identity/sign-in/restore-credentials-implementation-common#create-restore-key): After the user signs in (or on app startup if the user is already signed in and no restore key is recorded in local storage), fetch creation options from your relying party server and call `credentialManager.createCredential()`.
2. [**Sign in with the restore key on the new device**](https://developer.android.com/identity/sign-in/restore-credentials-implementation-common#sign-restore): Retrieve the transferred `RestoreCredential` using a two-tier strategy: first silently in `BackupAgent.onRestoreFinished()` (when `android:allowBackup="true"`) so background sync and push notifications resume immediately, and second as a fallback in your launcher `Activity.onCreate()` on first app launch.
3. [**Delete the restore key on sign-out**](https://developer.android.com/identity/sign-in/restore-credentials-implementation-common#delete-restore): When the user signs out or their session is invalidated by the server, call `credentialManager.clearCredentialState()` with `ClearCredentialStateRequest(ClearCredentialStateRequest.TYPE_CLEAR_RESTORE_CREDENTIAL)` and clear your local sync flag.

## Create a restore key

Your app should cover all cases of a user signing in to ensure active users have
a restore key created. Create the restore key in the following scenarios:

- If the user is signed in and a restore key isn't already created (such as in the `onCreate()` method for the main `Activity`).
- When the user is signing in or completing a new account registration flow.

To avoid calling `createCredential()` on every app launch, store a local sync
flag such as `has_synced_restore_credential` inside local storage. Don't store
this flag in default backed-up `SharedPreferences` or `DataStore` unless that
file is excluded in `data_extraction_rules.xml`; otherwise, Auto Backup copies
`has_synced_restore_credential = true` onto the new device and prevents the new
device from generating or rotating its own restore key.

> [!NOTE]
> **Note:** A restore key is tied to an application's unique package name. If your organization's main app and sub-apps have different package names, create a separate restore key for each app.

### Instantiate Credential Manager

Use your app's activity context to instantiate a `CredentialManager` object.

    // Use your app or activity context to instantiate a client instance of
    // CredentialManager.
    private val credentialManager = CredentialManager.create(context)

### Get credential creation options from your app server

Use a FIDO-compliant library in your app server to send your client app the
`PublicKeyCredentialCreationOptions` JSON required to create the restore
credential. For more information about the server-side implementation, see
[Server-side guidance](https://developers.google.com/identity/passkeys/developer-guides/server-registration).

The creation options JSON follows the same structure as passkey registration:

    {
      "challenge": "<base64url-encoded challenge>",
      "rp": {
        "name": "<relying party name>",
        "id": "<relying party host name>"
      },
      "user": {
        "id": "<base64url-encoded user ID>",
        "name": "<user name>",
        "displayName": "<user display name>"
      },
      "pubKeyCredParams": [
        {
          "type": "public-key",
          "alg": -7
        }
      ],
      "attestation": "none",
      "excludeCredentials": [
        {
            "id": "<base64url-encoded credential ID to exclude>", 
            "type": "public-key"
        }
      ],
      "authenticatorSelection": {
        "requireResidentKey": true,
        "residentKey": "required",
        "userVerification": "required"
      }
    }

Ensure that your creation options JSON meets these requirements:

- `challenge` and `user.id`: Encode both values as unpadded Base64URL strings (replacing `+` with `-`, `/` with `_`, and stripping trailing `=`). Standard Base64 characters or raw integer IDs cause `CreateRestoreCredentialDomException` or `IllegalArgumentException`.
- `rp.id`: Set to your relying party's domain (for example, `example.com`).
- `pubKeyCredParams`: Include `{"type": "public-key", "alg": -7}` (ES256) and `{"type": "public-key", "alg": -257}` (RS256).

### Create the restore key

After receiving the public key creation options JSON from your server, wrap the
JSON in a [`CreateRestoreCredentialRequest`](https://developer.android.com/reference/androidx/credentials/CreateRestoreCredentialRequest) object and call
[`createCredential()`](https://developer.android.com/reference/androidx/credentials/CredentialManager#createCredential(android.content.Context,androidx.credentials.CreateCredentialRequest)) on the `CredentialManager` object.

    // requestJson contains the credential creation options sent by the server
    val createRestoreRequest = CreateRestoreCredentialRequest(requestJson)
    val response = try {
        credentialManager.createCredential(context, createRestoreRequest)
    } catch (e: E2eeUnavailableException) {
        // Fall back to local device-to-device (D2D) restore if cloud E2EE is unavailable
        credentialManager.createCredential(
            context,
            CreateRestoreCredentialRequest(requestJson, isCloudBackupEnabled = false),
        )
    }

#### Key points about the code

- The `CreateRestoreCredentialRequest` object contains the following fields:

  - `requestJson`: The credential creation options sent by the app server in the [Web Authentication API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Authentication_API) format for [`PublicKeyCredentialCreationOptionsJSON`](https://w3c.github.io/webauthn/#dictdef-publickeycredentialcreationoptionsjson).
  - `isCloudBackupEnabled`: `Boolean` field to determine if the restore key
    should be backed up to the cloud. By default, this flag is `true`. This
    field has these values:

    - `true`: (**Recommended**) This value enables the backup of restore keys to the cloud if the user has Google Backup and end-to-end encryption, such as a screen lock, enabled.
    - `false`: This value saves the key locally and not in the cloud. The key is not available on the new device if the user chooses to restore from the cloud, but it still transfers during a local cable or Wi-Fi device-to-device (D2D) setup.

  > [!CAUTION]
  > **Caution:** Set `isCloudBackupEnabled` to `true` on your initial call, and fall back to `isCloudBackupEnabled = false` only if `E2eeUnavailableException` is thrown. If the user disabled cloud backup (or `isCloudBackupEnabled` is `false`) and later restores from a cloud backup, the call to retrieve the restore key fails. Users who restore your app with a cloud backup don't receive the restore key and aren't automatically signed in.

### Handle the credential creation response

The Credential Manager API returns a response of type
[`CreateRestoreCredentialResponse`](https://developer.android.com/reference/androidx/credentials/CreateRestoreCredentialResponse). This response holds the public key
credential registration response in [JSON format](https://w3c.github.io/webauthn/#authenticatorattestationresponse).

Send `response.registrationResponseJson` from your app to your relying party
server to verify and store the public key alongside the user's account, and then
record your local sync marker in local storage. For more information about
server-side verification, see [the guidance for passkeys](https://developer.android.com/identity/passkeys/create-passkeys).

During the restore key creation process, handle these exceptions:

- [`CreateRestoreCredentialDomException`](https://developer.android.com/reference/androidx/credentials/exceptions/restorecredential/CreateRestoreCredentialDomException): This exception occurs if `requestJson` is invalid and doesn't follow the WebAuthn format for [`PublicKeyCredentialCreationOptionsJSON`](https://w3c.github.io/webauthn/#dictdef-publickeycredentialcreationoptionsjson).
- [`E2eeUnavailableException`](https://developer.android.com/reference/androidx/credentials/exceptions/restorecredential/E2eeUnavailableException): This exception occurs if `isCloudBackupEnabled` is `true`, but the user's device doesn't have data backup or end-to-end encryption, such as a screen lock.  
  To ensure that Restore Credentials are created for local device-to-device (D2D) transfers even when cloud E2EE is unavailable, catch `E2eeUnavailableException` and immediately retry `createCredential()` with `CreateRestoreCredentialRequest(requestJson, isCloudBackupEnabled = false)`.
- `IllegalArgumentException`: This exception occurs if `requestJson` is empty, isn't valid JSON, or doesn't have a valid Base64URL-encoded `user.id` that conforms to the WebAuthn [specifications](https://w3c.github.io/webauthn/#dictdef-publickeycredentialcreationoptionsjson).

## Sign in with a restore key

Use Restore Credentials to silently sign in the user during the device setup
process.

### Get credential retrieval options from the app server

Before calling `getCredential()` on the new device, request a WebAuthn
`PublicKeyCredentialRequestOptions` JSON challenge from your app server. Because
the app on the new device doesn't yet know which user is signing in, this
endpoint must be **unauthenticated** (userless discovery). For related server
guidance, see [Sign in with a passkey](https://developer.android.com/identity/passkeys/sign-in-with-passkeys#get-options) and the [server-side authentication
guide](https://developers.google.com/identity/passkeys/developer-guides/server-authentication#create_credential_request_options).

The retrieval options JSON has the following structure:

    {
      "challenge": "<your app challenge>",
      "allowCredentials": [],
      "rpId": "<your app server domain>"
    }

Configure the retrieval options JSON on your server as follows:

- `allowCredentials`: Omit this field or pass an empty array (`[]`) because the user's account isn't known before restoration. After `getCredential()` returns, your server identifies the user from the `response.userHandle` field (which matches the `user.id` registered during creation) and looks up the public key by `id` (`credentialId`).
- `userVerification`: Set to `"discouraged"` (or `"preferred"`). Because Restore Credentials runs silently without biometric or screen-lock UI, Android overrides `"required"` to `"discouraged"`, and the authenticator data returned to your server has the User Verified (`uv`) flag set to `false`. Configure your WebAuthn server verifier to accept `uv = false` for restore key assertions.

### Get the restore key

To get the restore key on the new device, wrap the server's `requestJson` in a
`GetRestoreCredentialOption` inside a `GetCredentialRequest` and call
`getCredential()` on the `CredentialManager` object.

> [!CAUTION]
> **Caution:** Don't combine `GetRestoreCredentialOption` with any other `CredentialOption` (such as `GetPublicKeyCredentialOption` or `GetPasswordOption`) in the same `GetCredentialRequest`. Passing multiple options with `GetRestoreCredentialOption` throws an `IllegalArgumentException`.

Implement a **two-tier restoration strategy** so users are signed in whether or
not background app data restore runs:

- **Tier 1 (Background restore in `BackupAgent.onRestoreFinished()`)** : If app data backup is enabled (`android:allowBackup="true"`), subclass [`BackupAgent`](https://developer.android.com/reference/android/app/backup/BackupAgent) and override [`onRestoreFinished()`](https://developer.android.com/reference/android/app/backup/BackupAgent#onRestoreFinished()) (don't use `onRestore()`, which is only called for legacy key-value backups). Because `onRestoreFinished()` is synchronous and `getCredential()` is a Kotlin `suspend` function, bridge the call using `runBlocking(Dispatchers.IO)`. Catch `NoCredentialException` quietly when no restore key is present.
- **Tier 2 (Foreground fallback in launcher `Activity.onCreate()`)** : On the first app launch when no local session exists, call `getCredential()` from `lifecycleScope` before showing your login screen. This handles apps with `android:allowBackup="false"` and recovers if the device was offline when `onRestoreFinished()` ran.

If you add a new `BackupAgent` to an app that already uses Auto Backup with
`android:allowBackup="true"`, also set `android:fullBackupOnly="true"` on the
`<application>` element in `AndroidManifest.xml` so Android continues using
Auto Backup instead of switching to legacy key-value backup.

> [!IMPORTANT]
> **Important:** Push notifications aren't automatically restored when credentials are retrieved. Inside `BackupAgent.onRestoreFinished()` (or immediately after Tier-2 sign-in), fetch a fresh Firebase Cloud Messaging (FCM) registration token using `FirebaseMessaging.getInstance().token.await()` and register it with your backend so background notifications resume before the user opens the app.

        suspend fun getRestoreKey(
            fetchAuthenticationJson: () -> String,
        ) {
            // Fetch the options required to get the restore key
            val authenticationJson = fetchAuthenticationJson()

            // Create the GetRestoreCredentialOption object
            val options = GetRestoreCredentialOption(authenticationJson)
            val getRequest = GetCredentialRequest(listOf(options))

            try {
                val response = credentialManager.getCredential(context, getRequest)

                // Type-check and extract the restore credential
                val credential = response.credential
                if (credential is RestoreCredential) {
                    val responseJson = credential.authenticationResponseJson
                }
            } catch (e: NoCredentialException) {
                // No restore key is present on this device
            }
        }

    class MyBackupAgent : BackupAgent() {

        override fun onRestoreFinished() {
            super.onRestoreFinished()
            val credentialManager = CredentialManager.create(this)
            val restoreFunctions = RestoreCredentialsFunctions(this, credentialManager)

            runBlocking(Dispatchers.IO) {
                restoreFunctions.getRestoreKey(
                    fetchAuthenticationJson = {
                        /* Fetch challenge JSON from server */ ""
                    }
                )
            }
        }
    }

The Credential Manager API returns a [`GetCredentialResponse`](https://developer.android.com/reference/androidx/credentials/GetCredentialResponse) whose
`credential` property is a [`RestoreCredential`](https://developer.android.com/reference/androidx/credentials/RestoreCredential) (not a
`PublicKeyCredential`) containing `authenticationResponseJson`.

### Handle the sign-in response

Send `restoreCredential.authenticationResponseJson` from the app to your relying
party server to verify the cryptographic assertion and issue a new session token
for the user. For server-side verification details, see [Sign in with a
passkey](https://developer.android.com/identity/passkeys/sign-in-with-passkeys).

When designing your backend storage and lifecycle policies for restore keys,
follow these guidelines:

- **Differentiate restore keys from user passkeys** : Tag restore keys in your database so they are hidden from user-facing passkey management screens and exempt from user verification (`uv = true`) checks.
- **Support multiple active devices per user**: A user can have multiple devices (such as a phone and a tablet). Allow multiple active restore keys per user account (for example, keyed by device or installation ID) rather than overwriting a single row.
- **Set an appropriate TTL and clean up orphaned keys**: Uninstalling an app or clearing app data deletes the local restore key without notifying your server. Retain restore keys long enough to survive device upgrade windows (even if the user signs out on the old device after transferring), and prune stale keys based on inactivity TTL or per-user key limits.

## Delete the restore key

Credential Manager is stateless and unaware of user activity, so it doesn't
automatically delete restore keys after use. To delete a restore key, call the
[`clearCredentialState()`](https://developer.android.com/reference/androidx/credentials/CredentialManager#clearCredentialState(androidx.credentials.ClearCredentialStateRequest)) method. For security, delete the key whenever a
user signs out so they aren't silently signed back in on the next app launch.

> [!NOTE]
> **Note:** A user sign-out can also happen remotely, for example when a user changes their password on the web or when they're signed out remotely by the server (such as when your server returns an HTTP `401 Unauthorized` error). If your app detects a **server-side session invalidation**, delete the restore key on the device as well.

Restore keys are removed only in the following situations:

- **System-level actions**: Users uninstall the app or clear its data.
- **App-level calls** : Programmatically delete the key by calling [`clearCredentialState()`](https://developer.android.com/reference/androidx/credentials/CredentialManager#clearCredentialState(androidx.credentials.ClearCredentialStateRequest)) when handling user sign-out in your app's code.

Because a default `ClearCredentialStateRequest()` only clears standard session
state and leaves the restore key intact, perform a **dual clear** on sign-out:

1. Call `credentialManager.clearCredentialState(ClearCredentialStateRequest())` to clear active credential provider session state.
2. Call `credentialManager.clearCredentialState()` with `ClearCredentialStateRequest(ClearCredentialStateRequest.TYPE_CLEAR_RESTORE_CREDENTIAL)` to delete the stored `RestoreCredential`.
3. Delete your local `has_synced_restore_credential` marker from local storage.

    // Clear active credential provider session state
    credentialManager.clearCredentialState(ClearCredentialStateRequest())

    // When the user logs out, delete the restore key
    val clearRequest = ClearCredentialStateRequest(TYPE_CLEAR_RESTORE_CREDENTIAL)
    val response = credentialManager.clearCredentialState(clearRequest)

## Next steps

- [**Test Restore Credentials**](https://developer.android.com/identity/sign-in/test-restore-credentials): Test cloud and device-to-device (D2D) restore flows using Android Studio or `adb shell bmgr`.
- [**Automated backup and restore testing**](https://developer.android.com/studio/preview/backup-restore-testing): Write JUnit 5 host tests with `BackupRestoreController` to verify `CLOUD_ENCRYPTED` and `DEVICE_TO_DEVICE` restores in CI.