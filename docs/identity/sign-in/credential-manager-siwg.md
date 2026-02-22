---
title: https://developer.android.com/identity/sign-in/credential-manager-siwg
url: https://developer.android.com/identity/sign-in/credential-manager-siwg
source: md.txt
---

[Sign in with Google](https://developers.google.com/identity/gsi/web/guides/overview) helps you quickly integrate user
authentication with your Android app. Users can use their Google Account to sign
in to your app, provide consent, and securely share their profile information
with your app. Android's Credential Manager Jetpack library makes this
integration smooth, offering a consistent experience across Android devices
using a single API.

This document guides you through implementing Sign in with Google in Android
apps, how you can set up the Sign in with Google button UI, and configuring
app-optimized one tap sign-up and sign-in experiences. For smooth device
migration, Sign in with Google supports auto sign-in, and its cross-platform
nature across Android, iOS, and web surfaces helps you provide sign-in access
for your app on any device. If you use Firebase Authentication for your
application, you can learn more about integrating Sign in with Google and
Credential Manager in their [Authenticate with Google on Android](https://firebase.google.com/docs/auth/android/google-signin) guide.
| **Note:** For **authorization** actions needed to access data stored in the Google Account such as Google Drive, use the [AuthorizationClient API](https://developer.android.com/training/sign-in/legacy-gsi-migration#authorization).

To set up Sign in with Google, follow these two main steps:

**Configure Sign in with Google as an option for Credential Manager's bottom
sheet UI** . This can be configured to automatically prompt the user to sign in.
If you have implemented either [passkeys or passwords](https://developer.android.com/training/sign-in/passkeys), you can request all
relevant credential types simultaneously, so that the user does not have to
remember the option they've used previously to sign in.
![Credential Manager bottom sheet](https://developer.android.com/static/training/sign-in/images/credman-bottomsheet-animated.gif) **Figure 1.** The Credential Manager bottomsheet credential selection UI

**Add the Sign in with Google button to your app's UI**. The Sign in with Google
button offers a streamlined way for users to use their existing Google Accounts
to sign up or sign in to Android apps. Users will click the Sign in with Google
button if they dismiss the bottom sheet UI, or if they explicitly want to use
their Google Account for sign up and sign in. For developers, this means easier
user onboarding and reduced friction during sign-up.
![Animation showing the Sign in with Google flow](https://developer.android.com/static/training/sign-in/images/add-siwg-animated-2.gif) **Figure 2.** The Credential Manager Sign in with Google button UI

This document explains how to integrate the Sign in with Google button and
bottom sheet dialog with the Credential Manager API using the [Google
ID](https://developers.google.com/identity/android-credential-manager/android/reference/client/identity_googleid/classes.html) helper library.

## Set up your Google Cloud Console project

1. Open your project in the [Cloud Console](https://console.developers.google.com/auth/overview), or create a project if you don't already have one.
2. On the [Branding page](https://console.developers.google.com/auth/branding), make sure all of the information is complete and accurate.
   1. Make sure your app has a correct App Name, App Logo, and App Homepage assigned. These values will be presented to users on the Sign in with Google consent screen on sign up and the [Third-party apps \& services
      screen](https://myaccount.google.com/connections).
   2. Make sure you have specified the URLs of your app's privacy policy and terms of service.
3. In the [Clients page](https://console.developers.google.com/auth/clients), create an Android client ID for your app if you don't already have one. You will need to specify your app's package name and SHA-1 signature.
   1. Go to the [Clients page](https://console.developers.google.com/auth/clients).
   2. Click **Create client**.
   3. Select the **Android** application type.
   4. Enter a name for the OAuth client. This name is displayed on your project's [Clients page](https://console.developers.google.com/auth/clients) to identify the client.
   5. Enter the package name of your Android app. This value is defined in the [`package` attribute of the `<manifest>` element](https://developer.android.com/guide/topics/manifest/manifest-element#package) in your `AndroidManifest.xml` file.
   6. Enter the SHA-1 signing certificate fingerprint of the app distribution.
   7. If your app uses [app signing by Google Play](https://support.google.com/googleplay/android-developer/answer/7384423), copy the SHA-1 fingerprint from the app signing page of the Play Console.
   8. If you manage your own keystore and signing keys, use the <kbd>keytool</kbd> utility included with Java to print certificate information in a human-readable format. Copy the `SHA-1` value in the `Certificate fingerprints` section of the <kbd>keytool</kbd> output. See [Authenticating Your Client](https://developers.google.com/android/guides/client-auth) in the Google APIs for Android documentation for more information.
   9. (Optional) [Verify ownership](https://developer.android.com/identity/sign-in/credential-manager-siwg#verify-app-ownership) of your Android application.
4. In the [Clients page](https://console.developers.google.com/auth/clients), create a new "Web application" client ID if you haven't already. You can ignore the "Authorized JavaScript Origins" and "Authorized redirect URIs" fields for now. This client ID will be used to identify your backend server when it communicates with Google's authentication services.
   1. Go to the [Clients page](https://console.developers.google.com/auth/clients).
   2. Click **Create client**.
   3. Select the **Web application** type.

### Verify app ownership

You can verify ownership of your application to reduce the risk of app
impersonation.
| **Note:** Android app ownership verification is only available for Google Play apps.

To complete the verification process, you can use your
Google Play Developer Account if you have one and your app is registered
on the [Google Play Console](https://play.google.com/console/). The
following requirements must be met for a successful verification:

- You must have a registered application in the Google Play Console with the same package name and SHA-1 signing certificate fingerprint as the Android OAuth client you are completing the verification for.
- You must have **Admin** permission for the app in the Google Play Console. [Learn more](https://support.google.com/googleplay/android-developer/answer/9844686) about access management in the Google Play Console.

In the **Verify App Ownership** section of the Android client, click the
**Verify Ownership** button to complete the verification process.

If the verification is successful, a notification will be displayed to confirm
the success of the verification process. Otherwise, an error prompt will be
shown.

To fix a failed verification, try the following:

- Make sure the app you are verifying is a registered app in the Google Play Console.
- Make sure you have **Admin** permission for the app in the Google Play Console.

## Declare dependencies

Add the following dependencies to your app module's build script- make sure to
replace `<latest version>` with the latest version of the [`googleid`](https://maven.google.com/web/index.html?q=com.google.android.libraries.identity.googleid)
library:  

### Kotlin

```kotlin
dependencies {
    implementation("androidx.credentials:credentials:1.6.0-rc01")
    implementation("androidx.credentials:credentials-play-services-auth:1.6.0-rc01")
    implementation("com.google.android.libraries.identity.googleid:googleid:<latest version>")
}
```

### Groovy

```groovy
dependencies {
    implementation "androidx.credentials:credentials:1.6.0-rc01"
    implementation "androidx.credentials:credentials-play-services-auth:1.6.0-rc01"
    implementation "com.google.android.libraries.identity.googleid:googleid:<latest version>"
}
```

## Instantiate a Google sign-in request

To begin your implementation, [instantiate a Google sign-in request](https://developer.android.com/training/sign-in/credential-manager#instantiate-sign-in-request). Use
[`GetGoogleIdOption`](https://developers.google.com/identity/android-credential-manager/android/reference/kotlin/com/google/android/libraries/identity/googleid/GetGoogleIdOption) to retrieve a user's Google ID Token.  

    val googleIdOption: GetGoogleIdOption = GetGoogleIdOption.Builder()
    .setFilterByAuthorizedAccounts(true)
    .setServerClientId(WEB_CLIENT_ID)
        .setAutoSelectEnabled(true)
        // nonce string to use when generating a Google ID token
        .setNonce(nonce)
    .build()

First, check if the user has any accounts that have previously been used to sign
in to your app by calling the API with the `setFilterByAuthorizedAccounts`
parameter set to `true`. Users can choose between available accounts to sign in.

If no authorized Google Accounts are available, the user should be prompted to
sign up with any of their available accounts. To do this, prompt the user by
calling the API again and setting `setFilterByAuthorizedAccounts` to `false`.
[Learn more about sign up](https://developer.android.com/identity/sign-in/credential-manager-siwg#enable-sign-up).

### Enable automatic sign-in for returning users (recommended)

Developers should enable automatic sign-in for users who register with their
single account. This provides a seamless experience across devices, especially
during device migration, where users can quickly regain access to their account
without re-entering credentials. For your users, this removes unnecessary
friction when they were already previously signed in.

To enable automatic sign-in, use `setAutoSelectEnabled(true)`. Automatic sign in
is only possible when the following criteria are met:

- There is a single credential matching the request, which can be a Google Account or a password, and this credential matches the default account on the Android-powered device.
- The user has not explicitly signed out.
- The user hasn't disabled automatic sign-in in their [Google Account
  settings](https://passwords.google.com/options).

    val googleIdOption: GetGoogleIdOption = GetGoogleIdOption.Builder()
        .setFilterByAuthorizedAccounts(true)
        .setServerClientId(WEB_CLIENT_ID)
    .setAutoSelectEnabled(true)
        // nonce string to use when generating a Google ID token
        .setNonce(nonce)
        .build()

Remember to correctly [handle sign-out](https://developer.android.com/identity/sign-in/credential-manager-siwg#handle-sign-out) when implementing automatic sign-in,
so that users can always choose the proper account after they explicitly sign
out of your app.

### Set a nonce to improve security

To improve sign-in security and avoid replay attacks, add
[`setNonce`](https://developers.google.com/identity/android-credential-manager/android/reference/com/google/android/libraries/identity/googleid/GetGoogleIdOption.Builder#setNonce(kotlin.String)) to include a nonce in each request. [Learn more
about generating a nonce](https://developer.android.com/google/play/integrity/classic#nonce).  

    val googleIdOption: GetGoogleIdOption = GetGoogleIdOption.Builder()
        .setFilterByAuthorizedAccounts(true)
        .setServerClientId(WEB_CLIENT_ID)
        .setAutoSelectEnabled(true)
        // nonce string to use when generating a Google ID token
    .setNonce(nonce)
        .build()

## Create the Sign in with Google flow

The steps to set up a Sign in with Google flow are as follows:

1. Instantiate a `GetCredentialRequest`, then add the previously created `googleIdOption` using [`addCredentialOption()`](https://developer.android.com/reference/android/credentials/GetCredentialRequest.Builder#addCredentialOption(android.credentials.CredentialOption)) to retrieve the credentials.
2. Pass this request to [`getCredential()`](https://developer.android.com/reference/kotlin/androidx/credentials/CredentialManager#getCredential(android.content.Context,androidx.credentials.GetCredentialRequest)) (Kotlin) or [`getCredentialAsync()`](https://developer.android.com/reference/kotlin/androidx/credentials/CredentialManager#getCredentialAsync(android.content.Context,androidx.credentials.GetCredentialRequest,android.os.CancellationSignal,java.util.concurrent.Executor,androidx.credentials.CredentialManagerCallback)) (Java) call to retrieve the user's available credentials.
3. Once the API is successful, extract the `CustomCredential` which holds the result for `GoogleIdTokenCredential` data.
4. The type for `CustomCredential` should be equal to the value of `GoogleIdTokenCredential.TYPE_GOOGLE_ID_TOKEN_CREDENTIAL`. Convert the object into a `GoogleIdTokenCredential` using the `GoogleIdTokenCredential.createFrom` method.
5. If the conversion succeeds, extract the `GoogleIdTokenCredential` ID,
   [validate](https://developers.google.com/identity/gsi/web/guides/verify-google-id-token) it, and authenticate the credential on your server.

6. If the conversion fails with a `GoogleIdTokenParsingException`, then you may
   need to update your [Sign in with Google library](https://developers.google.com/identity/android-credential-manager/releases) version.

7. Catch any unrecognized custom credential types.

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
            // Handle failure
        }
    }

    fun handleSignIn(result: GetCredentialResponse) {
        // Handle the successfully returned credential.
        val credential = result.credential
        val responseJson: String

        when (credential) {

            // Passkey credential
            is PublicKeyCredential -> {
                // Share responseJson such as a GetCredentialResponse to your server to validate and
                // authenticate
                responseJson = credential.authenticationResponseJson
            }

            // Password credential
            is PasswordCredential -> {
                // Send ID and password to your server to validate and authenticate.
                val username = credential.id
                val password = credential.password
            }

            // GoogleIdToken credential
            is CustomCredential -> {
                if (credential.type == GoogleIdTokenCredential.TYPE_GOOGLE_ID_TOKEN_CREDENTIAL) {
                    try {
                        // Use googleIdTokenCredential and extract the ID to validate and
                        // authenticate on your server.
                        val googleIdTokenCredential = GoogleIdTokenCredential
                            .createFrom(credential.data)
                        // You can use the members of googleIdTokenCredential directly for UX
                        // purposes, but don't use them to store or control access to user
                        // data. For that you first need to validate the token:
                        // pass googleIdTokenCredential.getIdToken() to the backend server.
                        // see [validation instructions](https://developers.google.com/identity/gsi/web/guides/verify-google-id-token)
                    } catch (e: GoogleIdTokenParsingException) {
                        Log.e(TAG, "Received an invalid google id token response", e)
                    }
                } else {
                    // Catch any unrecognized custom credential type here.
                    Log.e(TAG, "Unexpected type of credential")
                }
            }

            else -> {
                // Catch any unrecognized credential type here.
                Log.e(TAG, "Unexpected type of credential")
            }
        }
    }

## Trigger a Sign in with Google button flow

To trigger the Sign in with Google button flow, use
[`GetSignInWithGoogleOption`](https://developers.google.com/identity/android-credential-manager/android/reference/com/google/android/libraries/identity/googleid/GetSignInWithGoogleOption) instead of
[`GetGoogleIdOption`](https://developers.google.com/identity/android-credential-manager/android/reference/com/google/android/libraries/identity/googleid/GetGoogleIdOption):  

    val signInWithGoogleOption: GetSignInWithGoogleOption = GetSignInWithGoogleOption.Builder(
        serverClientId = WEB_CLIENT_ID
    ).setNonce(nonce)
        .build()

| **Note:** This `GetSignInWithGoogleOption` must be the only option in the `GetCredentialRequest`.

Handle the returned [`GoogleIdTokenCredential`](https://developers.google.com/identity/android-credential-manager/android/reference/com/google/android/libraries/identity/googleid/GoogleIdTokenCredential) as described in
the following code example.  

    fun handleSignInWithGoogleOption(result: GetCredentialResponse) {
        // Handle the successfully returned credential.
        val credential = result.credential

        when (credential) {
            is CustomCredential -> {
                if (credential.type == GoogleIdTokenCredential.TYPE_GOOGLE_ID_TOKEN_CREDENTIAL) {
                    try {
                        // Use googleIdTokenCredential and extract id to validate and
                        // authenticate on your server.
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

Once you instantiate the Google sign in request, launch the authentication flow
in a similar manner as mentioned in the [Sign in with Google](https://developer.android.com/training/sign-in/credential-manager#sign-in) section.

### Enable sign-up for new users (recommended)

Sign in with Google is the easiest way for users to create a new account with
your app or service in just a few taps.

If no saved credentials are found (no Google Accounts returned by
`getGoogleIdOption`), prompt your user to sign up. First, check if
`setFilterByAuthorizedAccounts(true)` to see if any previously used accounts
exist. If none are found, prompt the user to sign up with their Google Account
using `setFilterByAuthorizedAccounts(false)`

Example:  

    val googleIdOption: GetGoogleIdOption = GetGoogleIdOption.Builder()
        .setFilterByAuthorizedAccounts(false)
        .setServerClientId(WEB_CLIENT_ID)
        .build()

Once you instantiate the Google sign up request, launch the authentication flow.
If users don't want to use Sign in with Google for sign up, consider [optimizing
your app for autofill](https://developer.android.com/guide/topics/text/autofill-optimize). Once your user has created an account, consider
enrolling them in passkeys as a final step to account creation.

## Handle sign-out

When a user signs out of your app, call the API [`clearCredentialState()`](https://developer.android.com/reference/kotlin/androidx/credentials/CredentialManager#clearCredentialState(androidx.credentials.ClearCredentialStateRequest))
method to clear the current user credential state from all credential providers.
This will notify all credential providers that any stored credential session for
the given app should be cleared.

A credential provider may have stored an active credential session and use it to
limit sign-in options for future get-credential calls. For example, it may
prioritize the active credential over any other available credential. When your
user explicitly signs out of your app and in order to get the holistic sign-in
options the next time, you should call this API to let the provider clear any
stored credential session.