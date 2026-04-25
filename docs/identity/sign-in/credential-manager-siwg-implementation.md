---
title: https://developer.android.com/identity/sign-in/credential-manager-siwg-implementation
url: https://developer.android.com/identity/sign-in/credential-manager-siwg-implementation
source: md.txt
---

This guide describes how to implement Sign in with Google and covers the
following steps:

- Add dependencies to your app.
- Instantiate `CredentialManager`.
- Create the bottom sheet flow.
- Create the button flow.
- Handle the sign-in response.
- Handle errors.
- Handle sign-out.

## Add dependencies to your app

In your module's `build.gradle` file, declare dependencies using the latest
version of [Credential Manager, Play Services Auth](https://developer.android.com/jetpack/androidx/releases/credentials), and
[`googleid`](https://mvnrepository.com/artifact/com.google.android.libraries.identity.googleid/googleid):

### Kotlin

```kotlin
dependencies {
    implementation("androidx.credentials:credentials:1.7.0-alpha01")
    implementation("androidx.credentials:credentials-play-services-auth:1.7.0-alpha01")
    implementation("com.google.android.libraries.identity.googleid:googleid:<latest version>")
}
```

### Groovy

```groovy
dependencies {
    implementation "androidx.credentials:credentials:1.7.0-alpha01"
    implementation "androidx.credentials:credentials-play-services-auth:1.7.0-alpha01"
    implementation "com.google.android.libraries.identity.googleid:googleid:<latest version>"
}
```

## Instantiate Credential Manager

Use your app or activity context to create a `CredentialManager` object.

    // Use your app or activity context to instantiate a client instance of
    // CredentialManager.
    private val credentialManager = CredentialManager.create(context)

## Create the bottom sheet flow

The bottom sheet is Credential Manager's inbuilt UI. Using this UI creates a
consistent experience across all authentication methods, such as passwords,
passkeys, and Sign in with Google.

> [!NOTE]
> **Note:** For an ideal user experience with the bottom sheet, we recommend that you first enable Automatic Sign-in for authorized accounts. If no authorized accounts exist on the device, request all accounts on the device, including unauthorized accounts.

### Configure the sign-in request for previously authorized accounts

Attempt a Google sign-in request with [`GetGoogleIdOption`](https://developers.google.com/identity/android-credential-manager/android/reference/kotlin/com/google/android/libraries/identity/googleid/GetGoogleIdOption) to
retrieve the user's Google ID Token.

The following snippets check if the account is an authorized account.

> [!NOTE]
> **Note:** An authorized account is a user account that has consented to your app accessing specific information (such as email, name, or profile image). This authorization is universal; once granted on any platform, it applies to all devices associated with that account. This ensures a seamless, cross-device experience where the user is not prompted for the same permissions when they use the app on different devices.

    val googleIdOption: GetGoogleIdOption = GetGoogleIdOption.Builder()
        .setFilterByAuthorizedAccounts(true)
        .setServerClientId(WEB_CLIENT_ID)
        .setAutoSelectEnabled(true)
        .setNonce(generateSecureRandomNonce())
        .build()

The request `googleIdOption` object is configured as follows:

- **Filter previously authorized accounts:** To retrieve the authorized
  accounts that have previously been used to sign in to your app, set
  `setFilterByAuthorizedAccounts` to `true`.

  Note that the default value for `setFilterByAuthorizedAccounts` is `true`,
  implying that the default behavior for the bottom sheet UI is to display
  only previously authorized accounts.
- **Set the server client ID:** Set the `setServerClientId` parameter. The
  `webClientId` is the Web Client ID you set up for OAuth in your Google Cloud
  Project while completing the [prerequisites](https://developer.android.com/identity/sign-in/credential-manager-siwg#prerequisites).

- **Enable Automatic Sign-in (optional):** To enable [Automatic Sign-in](https://support.google.com/accounts/answer/12849458#zippy=%2Cautomatic-sign-in)
  for returning users, use `setAutoSelectEnabled(true)` and
  `setFilterByAuthorizedAccounts(true)`. For your app users, this removes
  unnecessary friction if they were already previously signed in.

  Automatic Sign-in is only possible when the following criteria are met:
  - There is only a single authorized account on the device and that authorized account was previously used to sign into the app on the device. Multiple authorized accounts on the device disable automatic sign-in.
  - The user has not explicitly signed out of the app during their previous session.
  - The user hasn't disabled Automatic Sign-in in their [Google Account
    settings](https://passwords.google.com/options).
- **Set a nonce (optional):** To enable enhanced security, set a nonce for
  server-side verification. To prevent replay attacks, you can include a nonce
  for server-side verification with `setNonce()`. Ensure that your server-side
  code validates that the request and response nonces are identical.

  To generate the nonce, use a function similar to the following function that
  generates a cryptographically strong random nonce of a specified length and
  encodes it using `Base64`:

    fun generateSecureRandomNonce(byteLength: Int = 32): String {
        val randomBytes = ByteArray(byteLength)
        SecureRandom().nextBytes(randomBytes)
        return Base64.encodeToString(randomBytes, Base64.NO_WRAP or Base64.URL_SAFE or Base64.NO_PADDING)
    }

### Request sign-in

Check if the user has an authorized account on the device by calling the
`getCredential` method:

    val request: GetCredentialRequest = GetCredentialRequest.Builder()
        .addCredentialOption(googleIdOption)
        .build()

    coroutineScope {
        try {
            val result = credentialManager.getCredential(
                request = request,
                context = activityContext,
            )
            handleSignIn(result)
        } catch (e: GetCredentialException) {
            // Handle failures
        }
    }

### Configure the sign-in request if no authorized accounts are available

If there are no authorized users for your app on the device, `CredentialManager`
returns a `NoCredentialException`. In this scenario, disable the authorized
accounts filter so that the user can use another account to sign up.

    val googleIdOption: GetGoogleIdOption = GetGoogleIdOption.Builder()
        .setFilterByAuthorizedAccounts(false)
        .setServerClientId(WEB_CLIENT_ID)
        .setNonce(generateSecureRandomNonce())
        .build()

Next, [request sign-in](https://developer.android.com/identity/sign-in/credential-manager-siwg-implementation#request-sign-in) similarly to how you did for authorized accounts.

## Create the button flow

Use a button if you want users to be able to Sign in with Google for the
following conditions:

- The user dismissed the Credential Manager bottom sheet UI.
- There are no Google Accounts on the device.
- The existing accounts on the device require reauthentication.

### Create the button UI

While this can be done with a Jetpack Compose button, you can use a preapproved
brand icon from the [Sign in with Google Branding Guidelines](https://developers.google.com/identity/branding-guidelines)
page.

### Create the sign-in flow

Create a Google sign-in request with
[`GetSignInWithGoogleOption`](https://developers.google.com/identity/android-credential-manager/android/reference/com/google/android/libraries/identity/googleid/GetSignInWithGoogleOption) to retrieve a Google ID Token.

    val signInWithGoogleOption: GetSignInWithGoogleOption = GetSignInWithGoogleOption.Builder(
        serverClientId = WEB_CLIENT_ID
    ).setNonce(generateSecureRandomNonce())
        .build()

Next, [request sign-in](https://developer.android.com/identity/sign-in/credential-manager-siwg-implementation#request-sign-in) similarly to how you did for the bottom sheet UI.

## Create the shared sign in function for the bottom sheet and button

To handle the sign-in, complete the following steps:

1. Use CredentialManager's [`getCredential()`](https://developer.android.com/reference/android/credentials/CredentialManager#getCredential(android.content.Context,%20android.credentials.GetCredentialRequest,%20android.os.CancellationSignal,%20java.util.concurrent.Executor,%20android.os.OutcomeReceiver%3Candroid.credentials.GetCredentialResponse,android.credentials.GetCredentialException%3E)) function. If the response is successful, extract the `CustomCredential`, which should be of type `GoogleIdTokenCredential.TYPE_GOOGLE_ID_TOKEN_CREDENTIAL`.
2. Convert the object into a [`GoogleIdTokenCredential`](https://developers.google.com/identity/android-credential-manager/android/reference/com/google/android/libraries/identity/googleid/GoogleIdTokenCredential) using
   the `GoogleIdTokenCredential.createFrom()` method.

   > [!NOTE]
   > **Note:** If the conversion fails with a `GoogleIdTokenParsingException`, then you might need to update your [Sign in with Google library](https://developers.google.com/identity/android-credential-manager/releases) version.

3. [Validate](https://developers.google.com/identity/gsi/web/guides/verify-google-id-token) the credential on your relying party server.

4. Make sure that you handle errors appropriately.

   > [!NOTE]
   > **Note:** Before trusting the ID token that you receive to sign the user into your app, you need to validate the authenticity of that token. To verify the token, send `googleIdTokenCredential.getIdToken()` to your server. For more information about server-side validation, see [Verify the Google ID token on
   > your server side](https://developers.google.com/identity/gsi/web/guides/verify-google-id-token).

    fun handleSign(result: GetCredentialResponse) {
        // Handle the successfully returned credential.
        val credential = result.credential

        when (credential) {
            is CustomCredential -> {
                if (credential.type == GoogleIdTokenCredential.TYPE_GOOGLE_ID_TOKEN_CREDENTIAL) {
                    try {
                        // Use googleIdTokenCredential and extract the ID for server-side validation.
                        val googleIdTokenCredential = GoogleIdTokenCredential
                            .createFrom(credential.data)
                    } catch (e: GoogleIdTokenParsingException) {
                        Log.e(TAG, "Received an invalid google id token response", e)
                    }
                } else {
                    // Catch any unrecognized credential type here.
                    Log.e(TAG, "Unexpected type of credential")
                }
            }

            else -> {
                // Catch any unrecognized credential type here.
                Log.e(TAG, "Unexpected type of credential")
            }
        }
    }

## Handle errors

Review the errors listed in [Troubleshooting](https://developer.android.com/identity/sign-in/credential-manager-troubleshooting-guide) to ensure your code handles
all the possible error scenarios.

## Handle sign-out

It is important to provide a mechanism for your users to sign out of your app.
For example, a user might have multiple Google Accounts on the device and decide
to sign in from a different account. You can provide this in your, for example,
settings page.

A credential provider might store an active credential session and use it to
limit sign-in options for future sign-in requests. For example, it can
prioritize the active credential over any other available credential.

When a user signs out of your app, call the API [`clearCredentialState()`](https://developer.android.com/reference/android/credentials/CredentialManager#clearCredentialState(android.credentials.ClearCredentialStateRequest,%20android.os.CancellationSignal,%20java.util.concurrent.Executor,%20android.os.OutcomeReceiver%3Cjava.lang.Void,android.credentials.ClearCredentialStateException%3E))
method to clear the current user credential state from all credential providers.
This will notify all credential providers that any stored credential session for
the given app should be cleared, providing users with full sign-in options the
next time.

> [!NOTE]
> **Note:** Signing out of your app doesn't clear the permissions that were previously granted to your app.