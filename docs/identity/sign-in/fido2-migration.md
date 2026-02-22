---
title: https://developer.android.com/identity/sign-in/fido2-migration
url: https://developer.android.com/identity/sign-in/fido2-migration
source: md.txt
---

With support for [passkeys](https://developer.android.com/training/sign-in/passkeys), federated sign-in, and third-party
authentication providers, Credential Manager is the recommended API for
authentication on Android that provides a secure and convenient environment that
allows users to sync and manage their credentials. For developers that use local
[FIDO2](https://developers.google.com/identity/fido/android/native-apps) credentials, you should update your app to support passkey
authentication by integrating with the Credential Manager API. This document
describes how to migrate your project from FIDO2 to Credential Manager.

## Reasons to migrate from FIDO2 to Credential Manager

In most cases, you should migrate your Android app's authentication provider to
Credential Manager. The reasons to migrate to Credential Manager include:

- **Passkey support:** Credential Manager supports [passkeys](https://developer.android.com/training/sign-in/passkeys), a new, passwordless authentication mechanism that is more secure and easier to use than passwords.
- **Multiple sign-in methods:** Credential Manager supports multiple sign-in methods, including passwords, passkeys, and federated sign-in methods. This makes it easier for users to authenticate to your app, regardless of their preferred authentication method.
- **Third party credential provider support:** On Android 14 and higher, Credential Manager supports multiple third party credential providers. This means your users can use their existing credentials from other providers to sign in to your app.
- **Consistent user experience:** Credential Manager provides a more consistent user experience for authentication across apps and sign-in mechanisms. This makes it easier for users to understand and use your app's authentication flow.

| **Note:** If your app requires non-discoverable [FIDO credentials](https://developers.google.com/identity/fido/android/native-apps) or uses physical security keys, you should continue to use FIDO at this time.

To begin migration from FIDO2 to Credential Manager, follow the steps below.

## Update dependencies

1. Update the Kotlin plugin in your project's build.gradle to version 1.8.10 or
   higher.

         plugins {
           //...
             id 'org.jetbrains.kotlin.android' version '1.8.10' apply false
           //...
         }

2. In your project's `build.gradle`, update your dependencies to use the
   [latest versions](https://developer.android.com/jetpack/androidx/releases/credentials) of the Credential Manager and Play Services
   Authentication libraries.

         dependencies {
           // ...
           // Credential Manager:
           implementation 'androidx.credentials:credentials:<latest-version>'

           // Play Services Authentication:
           // Optional - needed for credentials support from play services, for devices running
           // Android 13 and below:
           implementation 'androidx.credentials:credentials-play-services-auth:<latest-version>'
           // ...
         }

3. Replace FIDO initialization with Credential Manager initialization. Add this
   declaration in the class you use for passkey creation and sign in methods:

       val credMan = CredentialManager.create(context)

| **Tip:** View models shouldn't handle activity or context. Keep server calls with your business logic.

## Create passkeys

You'll need to create a new passkey, associate it with a user's account, and
store the passkey's public key on your server before the user can sign in with
it. Set up your app with this ability by updating the register function calls.
![](https://developer.android.com/static/training/sign-in/images/fido-fig1a.svg) **Figure 1.** This figure shows how data is exchanged between app and server when a passkey is created using Credential Manager.

1. To obtain the necessary parameters that are sent to the `createCredential()`
   method during passkey creation, add `name("residentKey").value("required")`
   as described in the [WebAuthn](https://www.w3.org/TR/webauthn-2/#enum-residentKeyRequirement) specification) to your
   `registerRequest()` server call.

       suspend fun registerRequest() {
           // ...
           val call = client.newCall(
               Builder()
                   .method(
                       "POST",
                       jsonRequestBody {
                           name("attestation").value("none")
                           name("authenticatorSelection").objectValue {
                               name("residentKey").value("required")
                           }
                       }
                   ).build()
           )
           // ...
       }

2. Set the `return` type for `registerRequest()` and all child functions to
   `JSONObject`.

       suspend fun registerRequest(sessionId: String): ApiResult<JSONObject> {
           val call = client.newCall(
               Builder()
                   .url("$BASE_URL/<your api url>")
                   .addHeader("Cookie", formatCookie(sessionId))
                   .method(
                       "POST",
                       jsonRequestBody {
                           name("attestation").value("none")
                           name("authenticatorSelection").objectValue {
                               name("authenticatorAttachment").value("platform")
                               name("userVerification").value("required")
                               name("residentKey").value("required")
                           }
                       }
                   ).build()
           )
           val response = call.await()
           return response.result("Error calling the api") {
               parsePublicKeyCredentialCreationOptions(
                   body ?: throw ApiException("Empty response from the api call")
               )
           }
       }

   | **Note:** Refer to the list of allowed [enums](https://www.w3.org/TR/webauthn-2/#enum-attachment) as indicated in the specification.
3. Safely remove any methods that handle intent launcher and activity result
   calls from your view.

4. Since `registerRequest()` now returns a `JSONObject`, you don't need to
   create a `PendingIntent`. Replace the returned intent with a `JSONObject`.
   Update your intent launcher calls to call `createCredential()` from the
   Credential Manager API. Call `createCredential()` API method.

       suspend fun createPasskey(
           activity: Activity,
           requestResult: JSONObject
       ): CreatePublicKeyCredentialResponse? {
           val request = CreatePublicKeyCredentialRequest(requestResult.toString())
           var response: CreatePublicKeyCredentialResponse? = null
           try {
               response = credMan.createCredential(
                   request = request as CreateCredentialRequest,
                   context = activity
               ) as CreatePublicKeyCredentialResponse
           } catch (e: CreateCredentialException) {

               showErrorAlert(activity, e)

               return null
           }
           return response
       }

5. Once the call is successful, send the response back to the server. The
   request and response for this call are similar to the FIDO2 implementation,
   so no changes are required.

## Authenticate with passkeys

After you set up passkey creation, you can set up your app to allow users to
sign in and authenticate using their passkeys. To do this, you'll update your
authentication code to handle Credential Manager results, and implement a
function to authenticate through passkeys.
![](https://developer.android.com/static/training/sign-in/images/fido-fig2a.svg) **Figure 2.** Credential Manager's passkey authentication flow.

1. Your sign in request call to the server to get necessary information to be sent to `getCredential()` request is the same as the FIDO2 implementation. No changes are required.
2. Similar to the register request call, the returned response is in JSONObject
   format.

       /**
        * @param sessionId The session ID to be used for the sign-in.
        * @param credentialId The credential ID of this device.
        * @return a JSON object.
        */
       suspend fun signinRequest(): ApiResult<JSONObject> {
           val call = client.newCall(
               Builder().url(
                   buildString {
                       append("$BASE_URL/signinRequest")
                   }
               ).method("POST", jsonRequestBody {})
                   .build()
           )
           val response = call.await()
           return response.result("Error calling /signinRequest") {
               parsePublicKeyCredentialRequestOptions(
                   body ?: throw ApiException("Empty response from /signinRequest")
               )
           }
       }

       /**
        * @param sessionId The session ID to be used for the sign-in.
        * @param response The JSONObject for signInResponse.
        * @param credentialId id/rawId.
        * @return A list of all the credentials registered on the server,
        * including the newly-registered one.
        */
       suspend fun signinResponse(
           sessionId: String,
           response: JSONObject,
           credentialId: String
       ): ApiResult<Unit> {

           val call = client.newCall(
               Builder().url("$BASE_URL/signinResponse")
                   .addHeader("Cookie", formatCookie(sessionId))
                   .method(
                       "POST",
                       jsonRequestBody {
                           name("id").value(credentialId)
                           name("type").value(PUBLIC_KEY.toString())
                           name("rawId").value(credentialId)
                           name("response").objectValue {
                               name("clientDataJSON").value(
                                   response.getString("clientDataJSON")
                               )
                               name("authenticatorData").value(
                                   response.getString("authenticatorData")
                               )
                               name("signature").value(
                                   response.getString("signature")
                               )
                               name("userHandle").value(
                                   response.getString("userHandle")
                               )
                           }
                       }
                   ).build()
           )
           val apiResponse = call.await()
           return apiResponse.result("Error calling /signingResponse") {
           }
       }

3. Safely remove any methods that handle the intent launcher and activity
   result calls from your view.

4. Since `signInRequest()` now returns a `JSONObject`, you don't need to create
   a `PendingIntent`. Replace the returned intent with a `JSONObject`, and call
   `getCredential()` from your API methods.

       suspend fun getPasskey(
           activity: Activity,
           creationResult: JSONObject
       ): GetCredentialResponse? {
           Toast.makeText(
               activity,
               "Fetching previously stored credentials",
               Toast.LENGTH_SHORT
           )
               .show()
           var result: GetCredentialResponse? = null
           try {
               val request = GetCredentialRequest(
                   listOf(
                       GetPublicKeyCredentialOption(
                           creationResult.toString(),
                           null
                       ),
                       GetPasswordOption()
                   )
               )
               result = credMan.getCredential(activity, request)
               if (result.credential is PublicKeyCredential) {
                   val publicKeycredential = result.credential as PublicKeyCredential
                   Log.i("TAG", "Passkey ${publicKeycredential.authenticationResponseJson}")
                   return result
               }
           } catch (e: Exception) {
               showErrorAlert(activity, e)
           }
           return result
       }

5. Once the call is successful, send the response back to the server to
   validate and authenticate the user. The request and response parameters for
   this API call are similar to the FIDO2 implementation, so no changes are
   required.

## Additional resources

- [Credential Manager Sample reference](https://github.com/android/identity-samples/tree/glitch_me_version/CredentialManager)
- [Credential Manager Codelab](https://codelabs.developers.google.com/credential-manager-api-for-android#0)
- [Bringing seamless authentication to your apps with passkeys using
  Credential Manager API](https://medium.com/androiddevelopers/bringing-seamless-authentication-to-your-apps-using-credential-manager-api-b3f0d09e0093)
- [FIDO2 codelab](https://codelabs.developers.google.com/codelabs/fido2-for-android#0)