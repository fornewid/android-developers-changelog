---
title: https://developer.android.com/identity/legacy/one-tap/linked-account-signin-client
url: https://developer.android.com/identity/legacy/one-tap/linked-account-signin-client
source: md.txt
---

| **Caution:** One Tap for Android is deprecated. To ensure the continued security and usability of your app, [migrate to
| Credential Manager](https://developer.android.com/identity/sign-in/credential-manager). Credential Manager supports passkey, password, and federated identity authentication (such as Sign-in with Google), stronger security, and a more consistent user experience.

Linked Account Sign-In enables [One Tap Sign In With Google](https://developer.android.com/identity/legacy/one-tap/overview) for users
that already have their Google Account linked to your service. This improves the
experience for users as they can sign in with one click, without re-entering
their username and password. It also reduces the chances of users creating
duplicate accounts on your service.

Linked Account Sign-In is available as part of the One Tap Sign-In flow for
Android. This means you don't need to import a separate library if your app
already has the One Tap feature enabled.

In this document, you will learn how to modify your Android app to support
Linked Account Sign-In.

## How it works

1. You opt in to show linked accounts during the One Tap Sign-In flow.
2. If the user is signed in on Google and has linked their Google Account with their account on your service, an ID token will be returned for the linked account.
3. The user is shown a One Tap sign-in prompt with an option to sign in to your service with their linked account.
4. If the user chooses to continue with the linked account, the user's ID token is returned to your app. You match this against the token that was sent to your server in step 2 to identify the logged in user.

## Setup

### Set up your development environment

Get the latest Google Play services on your development host:

1. Open the [Android SDK Manager](https://developer.android.com/studio/intro/update#sdk-manager).

| **Note:** If this is your first time setting up your Android Development environment, you should review and install the [Android SDK recommended packages](https://developer.android.com/studio/intro/update#recommended).

1. Under **SDK Tools** , find **Google Play services**.

2. If the status for these packages is not Installed, select them both and click
   **Install Packages**.

### Configure your app

1. In your project-level `build.gradle` file, include Google's Maven repository
   in both your `buildscript` and `allprojects` sections.

       buildscript {
           repositories {
               google()
           }
       }

       allprojects {
           repositories {
               google()
           }
       }

2. Add the dependencies for the "Link with Google" API to your module's
   app-level gradle file, which is usually `app/build.gradle`:

       dependencies {
         implementation 'com.google.android.gms:play-services-auth:21.3.0'
       }

## Modify your Android app to support Linked Account Sign-In

At the end of the Linked Account Sign-In flow, an ID token is returned to your
app. The ID token's integrity should be verified before signing the user in.

The following code sample details the steps to retrieve,
[verify the ID token](https://developer.android.com/identity/legacy/one-tap/linked-account-signin-client#verify_the_integrity_of_the_id_token), and subsequently
sign the user in.

1. Create an activity to receive the result of the Sign-In intent

   ### Kotlin

         private val activityResultLauncher = registerForActivityResult(
           ActivityResultContracts.StartIntentSenderForResult()) { result ->
           if (result.resultCode == RESULT_OK) {
             try {
               val signInCredentials = Identity.signInClient(this)
                                       .signInCredentialFromIntent(result.data)
               // Review the Verify the integrity of the ID token section for
               // details on how to verify the ID token
               verifyIdToken(signInCredential.googleIdToken)
             } catch (e: ApiException) {
               Log.e(TAG, "Sign-in failed with error code:", e)
             }
           } else {
             Log.e(TAG, "Sign-in failed")
           }
         }

   ### Java

         private final ActivityResultLauncher<IntentSenderResult>
           activityResultLauncher = registerForActivityResult(
           new ActivityResultContracts.StartIntentSenderForResult(),
           result -> {
           If (result.getResultCode() == RESULT_OK) {
               try {
                 SignInCredential signInCredential = Identity.getSignInClient(this)
                                .getSignInCredentialFromIntent(result.getData());
                 verifyIdToken(signInCredential.getGoogleIdToken());
               } catch (e: ApiException ) {
                 Log.e(TAG, "Sign-in failed with error:", e)
               }
           } else {
               Log.e(TAG, "Sign-in failed")
           }
       });

2. Build the sign in request

   ### Kotlin

       private val tokenRequestOptions =
       GoogleIdTokenRequestOptions.Builder()
         .supported(true)
         // Your server's client ID, not your Android client ID.
         .serverClientId(getString("your-server-client-id")
         .filterByAuthorizedAccounts(true)
         .associateLinkedAccounts("service-id-of-and-defined-by-developer",
       scopes)
         .build()

   ### Java

        private final GoogleIdTokenRequestOptions tokenRequestOptions =
            GoogleIdTokenRequestOptions.Builder()
         .setSupported(true)
         .setServerClientId("your-service-client-id")
         .setFilterByAuthorizedAccounts(true)
         .associateLinkedAccounts("service-id-of-and-defined-by-developer",
       scopes)
         .build()

3. Launch the Sign-In Pending intent

   ### Kotlin

        Identity.signInClient(this)
           .beginSignIn(
         BeginSignInRequest.Builder()
           .googleIdTokenRequestOptions(tokenRequestOptions)
         .build())
           .addOnSuccessListener{result ->
             activityResultLauncher.launch(result.pendingIntent.intentSender)
         }
         .addOnFailureListener {e ->
           Log.e(TAG, "Sign-in failed because:", e)
         }

   ### Java

        Identity.getSignInClient(this)
         .beginSignIn(
           BeginSignInRequest.Builder()
             .setGoogleIdTokenRequestOptions(tokenRequestOptions)
             .build())
         .addOnSuccessListener(result -> {
           activityResultLauncher.launch(
               result.getPendingIntent().getIntentSender());
       })
       .addOnFailureListener(e -> {
         Log.e(TAG, "Sign-in failed because:", e);
       });

## Verify the integrity of the ID token

### Use a Google API Client Library

Using the
[Java Google API Client Library](https://developers.google.com/api-client-library/java/google-api-java-client/setup)
is the recommended way to validate Google ID tokens in a production environment.

### Java

      import com.google.api.client.googleapis.auth.oauth2.GoogleIdToken;
      import com.google.api.client.googleapis.auth.oauth2.GoogleIdToken.Payload;
      import com.google.api.client.googleapis.auth.oauth2.GoogleIdTokenVerifier;

      ...

      GoogleIdTokenVerifier verifier = new GoogleIdTokenVerifier.Builder(transport, jsonFactory)
          // Specify the CLIENT_ID of the app that accesses the backend:
          .setAudience(Collections.singletonList(CLIENT_ID))
          // Or, if multiple clients access the backend:
          //.setAudience(Arrays.asList(CLIENT_ID_1, CLIENT_ID_2, CLIENT_ID_3))
          .build();

      // (Receive idTokenString by HTTPS POST)

      GoogleIdToken idToken = verifier.verify(idTokenString);
      if (idToken != null) {
        Payload payload = idToken.getPayload();

        // Print user identifier
        String userId = payload.getSubject();
        System.out.println("User ID: " + userId);

        // Get profile information from payload
        String email = payload.getEmail();
        boolean emailVerified = Boolean.valueOf(payload.getEmailVerified());
        String name = (String) payload.get("name");
        String pictureUrl = (String) payload.get("picture");
        String locale = (String) payload.get("locale");
        String familyName = (String) payload.get("family_name");
        String givenName = (String) payload.get("given_name");

        // Use or store profile information
        // ...

      } else {
        System.out.println("Invalid ID token.");
      }

The `GoogleIdTokenVerifier.verify()` method verifies the JWT signature, the
`aud` claim, the `iss` claim, and them`exp` claim.

If you need to validate that the ID token represents a Google Workspace or Cloud
organization account, you can verify the `hd` claim by checking the domain name
returned by the `Payload.getHostedDomain()` method.