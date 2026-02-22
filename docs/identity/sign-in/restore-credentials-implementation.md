---
title: https://developer.android.com/identity/sign-in/restore-credentials-implementation
url: https://developer.android.com/identity/sign-in/restore-credentials-implementation
source: md.txt
---

This page describes how to create, sign in with, and delete a restore key.

## Version compatibility

Credential Manager's Restore Credentials works on devices running Android 9 and
higher, Google Play services (GMS) core version 24220000 or higher, and version
1.5.0 or higher of the `androidx.credentials` library.

## Prerequisites

Set up a [relying party server](https://developer.android.com/identity/credential-manager#authentication-terminology) similar to the server for [passkeys](https://developer.android.com/identity/passkeys).
If you already have a [server](https://developers.google.com/identity/passkeys/developer-guides/server-introduction) set up to handle authentication with passkeys,
use the same server-side implementation for restore keys.
| **Note:** While the server-side implementation is the same for passkeys and restore keys, your client-side app can support restore keys without supporting passkeys. Because restore keys work independently of the authentication method in your app (for example, passwords or Sign in with Google), you don't need to make any additional changes to the existing authentication methods in your app's code.

## Dependencies

Add the following dependencies to your app module's `build.gradle` file:

### Kotlin

```kotlin
dependencies {
    implementation("androidx.credentials:credentials:1.6.0-rc01")
    implementation("androidx.credentials:credentials-play-services-auth:1.6.0-rc01")
}
```

### Groovy

```groovy
dependencies {
    implementation "androidx.credentials:credentials:1.6.0-rc01"
    implementation "androidx.credentials:credentials-play-services-auth:1.6.0-rc01"
}
```

Restore Credentials is available from version 1.5.0 and higher of the
androidx.credentials library. However, it's recommended to use the latest stable
versions of the dependencies where possible.
| **Note:** The Restore Credentials feature works regardless of whether [`allowBackup`](https://developer.android.com/guide/topics/manifest/application-element#allowbackup) is set in the `manifest`.

## Overview

1. [**Create a restore key**](https://developer.android.com/identity/sign-in/restore-credentials-implementation#create-restore-key): To create a restore key, complete the following steps:
   1. [**Instantiate Credential Manager**](https://developer.android.com/identity/sign-in/restore-credentials-implementation#instantiate-credential): Create a `CredentialManager` object.
   2. [**Get credential creation options from the app server**](https://developer.android.com/identity/sign-in/restore-credentials-implementation#get-credential): Send the client app the details required to create the restore key from your app server.
   3. [**Create the restore key**](https://developer.android.com/identity/sign-in/restore-credentials-implementation#create-restore): Create a restore key for the user's account if the user is signed in to your app.
   4. [**Handle the credential creation response**](https://developer.android.com/identity/sign-in/restore-credentials-implementation#handle-credential): Send the credentials from your client app to your app server for processing, and handle any exceptions.
2. [**Sign in with a restore key**](https://developer.android.com/identity/sign-in/restore-credentials-implementation#sign-restore): To sign in with a restore key, complete the following steps:
   1. [**Get credential retrieval options from the app server**](https://developer.android.com/identity/sign-in/restore-credentials-implementation#get-credential-retrieval): Send the client app the details required to retrieve the restore key from your app server.
   2. [**Get the restore key**](https://developer.android.com/identity/sign-in/restore-credentials-implementation#get-restore): Request the restore key from Credential Manager when the user sets up a new device. This lets the user sign in without additional input.
   3. [**Handle the credential retrieval response**](https://developer.android.com/identity/sign-in/restore-credentials-implementation#handle-sign-in): Send the restore key from the client app to the app server to sign in the user.
3. [**Delete a restore key**](https://developer.android.com/identity/sign-in/restore-credentials-implementation#delete-restore).

## Create a restore key

Create the restore key after the user authenticates to your app---immediately
after sign-in, or during a subsequent app launch if they are already signed in.
| **Note:** A restore key is tied to an application's unique package name. If your organization's main app and sub-apps have different package names, create a separate restore key for each app.

### Instantiate Credential Manager

Use your app's activity context to instantiate a `CredentialManager` object.

    // Use your app or activity context to instantiate a client instance of
    // CredentialManager.
    private val credentialManager = CredentialManager.create(context)

### Get credential creation options from your app server

Use a FIDO-compliant library in your app server to send your client app the
information required to create the restore credential, such as information about
the user, the app, and additional configuration properties. For more information
about the server-side implementation, see [Server-side
guidance](https://developers.google.com/identity/passkeys/developer-guides/server-registration).

### Create the restore key

After parsing the public key creation options sent by the server, create a
restore key by wrapping these options in a
[`CreateRestoreCredentialRequest`](https://developer.android.com/reference/androidx/credentials/CreateRestoreCredentialRequest) object and calling the
[`createCredential()`](https://developer.android.com/reference/androidx/credentials/CredentialManager#createCredential(android.content.Context,androidx.credentials.CreateCredentialRequest)) method with the `CredentialManager` object.

    // createRestoreRequest contains the details sent by the server 
    val response = credentialManager.createCredential(context, createRestoreRequest)

#### Key points about the code

- The `CreateRestoreCredentialRequest` object contains the following fields:

  - `requestJson`: The credential creation options sent by the app server in the [Web Authentication API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Authentication_API) format for [`PublicKeyCredentialCreationOptionsJSON`](https://w3c.github.io/webauthn/#dictdef-publickeycredentialcreationoptionsjson).
  - `isCloudBackupEnabled`: `Boolean` field to determine if the restore key
    should be backed up to the cloud. By default, this flag is `true`. This
    field has these values:

    - `true`: (**Recommended**) This value enables the backup of restore keys to the cloud if the user has Google Backup and end-to-end encryption, such as a screen lock, enabled.
    - `false`: This value saves the key locally and not in the cloud. The key is not available on the new device if the user chooses to restore from the cloud.

  | **Caution:** It is recommended to set `isCloudBackupEnabled` to `true`. If cloud backup is disabled and the user restores from a cloud backup, the call to retrieve the restore key fails. Users who restore your app with a cloud backup don't receive the restore key and are not automatically signed in.

### Handle the credential creation response

The Credential Manager API returns a response of type
[`CreateRestoreCredentialResponse`](https://developer.android.com/reference/androidx/credentials/CreateRestoreCredentialResponse). This response holds the public key
credential registration response in [JSON format](https://w3c.github.io/webauthn/#authenticatorattestationresponse).

Send the public key from your app to the relying party server. This public key
is similar to the public key generated when you create a passkey. The same code
that handles passkey creation on the server can also handle restore key
creation. For more information about the server-side implementation, see [the
guidance for passkeys](https://developer.android.com/identity/passkeys/create-passkeys).

During the restore key creation process, handle these exceptions:

- [`CreateRestoreCredentialDomException`](https://developer.android.com/reference/androidx/credentials/exceptions/restorecredential/CreateRestoreCredentialDomException): This exception occurs if `requestJson` is invalid and does not follow the WebAuthn format for [`PublicKeyCredentialCreationOptionsJSON`](https://w3c.github.io/webauthn/#dictdef-publickeycredentialcreationoptionsjson).
- [`E2eeUnavailableException`](https://developer.android.com/reference/androidx/credentials/exceptions/restorecredential/E2eeUnavailableException): This exception occurs if `isCloudBackupEnabled` is `true`, but the user's device does not have data backup or end-to-end encryption, such as a screen lock.
- `IllegalArgumentException`: This exception occurs if `createRestoreRequest` is empty or not valid JSON, or if it does not have a valid `user.id` that conforms to the WebAuthn [specifications](https://w3c.github.io/webauthn/#dictdef-publickeycredentialcreationoptionsjson).

## Sign in with a restore key

Use Restore Credentials to silently sign in the user during the device setup
process.

### Get credential retrieval options from the app server

Send the client app the options required to get the restore key from the server.
For similar passkey guidance for this step, see [Sign in with a passkey](https://developer.android.com/identity/passkeys/sign-in-with-passkeys#get-options).
For more information about the server-side implementation, see the [server-side
authentication guide](https://developers.google.com/identity/passkeys/developer-guides/server-authentication#create_credential_request_options).

### Get the restore key

To get the restore key on the new device, call the `getCredential()` method on
the `CredentialManager` object.

You can fetch the restore key in the following scenarios:

- (**Recommended** ) Immediately after the app data is restored. Use [`BackupAgent`](https://developer.android.com/reference/android/app/backup/BackupAgent) to configure your app's backup and complete the `getCredential` functionality within the [`onRestore`](https://developer.android.com/reference/android/app/backup/BackupAgent#onRestore(android.app.backup.BackupDataInput,%20int,%20android.os.ParcelFileDescriptor)) callback to ensure the app's credentials are restored immediately after the app data is restored. This avoids potential delays when users open their new device for the first time and lets users interact without waiting for them to open your app.
- On the first launch of the app on the device.

To send a user notifications before they open the app for the first time on a
new device, fetch the restore key within `BackupAgent`'s `onRestore` callback.
This is particularly relevant for messaging or communications apps.

    // Fetch the options required to get the restore key
    val authenticationJson = fetchAuthenticationJson()

    // Create the GetRestoreCredentialRequest object
    val options = GetRestoreCredentialOption(authenticationJson)
    val getRequest = GetCredentialRequest(listOf(options))

    val response = credentialManager.getCredential(context, getRequest)

The credential manager APIs return a response of type
[`GetCredentialResponse`](https://developer.android.com/reference/android/credentials/GetCredentialResponse). This response holds the public key.

### Handle the sign-in response

Send the public key from the app to the relying party server, which can then be
used to sign in the user. On the server side, this action is similar to signing
in using a passkey. The same code that handles sign-in with passkeys on the
server can also handle sign-ins with restore keys. For more information about
the server-side implementation for passkeys, see [Sign in with a passkey](https://developer.android.com/identity/passkeys/sign-in-with-passkeys).
| **Note:** Even though restore keys and passkeys use the same underlying server implementation, differentiate between them when saving them in your app server's database. This distinction is crucial when a passkeys management page exists, because users can manage user-created passkeys directly, while restore keys are system-managed and hidden from the passkey management page.

## Delete the restore key

Credential Manager is stateless and unaware of user activity, so it does not
automatically delete restore keys after use. To delete a restore key, call the
`clearCredentialState()` method. For security, delete the key whenever a user
signs out. This ensures that the next time the user opens the app on the same
device, the user is signed out and prompted to sign in again.

Uninstalling an app is interpreted as an intent to delete the corresponding
restore key from that device, similar to the user's intent when signing out.

Restore keys are removed only in the following situations:

- **System-level actions**: Users uninstall the app or clear its data.
- **App-level calls** : Programmatically delete the key by calling [`clearCredentialState()`](https://developer.android.com/reference/androidx/credentials/CredentialManager#clearCredentialState(androidx.credentials.ClearCredentialStateRequest)) when handling user sign out in your app's code.

When the user signs out of your app, call the `clearCredentialState()` method on
the `CredentialManager` object.

    // Create a ClearCredentialStateRequest object
    val clearRequest = ClearCredentialStateRequest(TYPE_CLEAR_RESTORE_CREDENTIAL)

    // When the user logs out, delete the restore key
    val response = credentialManager.clearCredentialState(clearRequest)