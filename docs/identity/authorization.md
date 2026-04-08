---
title: https://developer.android.com/identity/authorization
url: https://developer.android.com/identity/authorization
source: md.txt
---

Authentication establishes who someone is, and is commonly referred to as user
sign-up or sign-in. Authorization is the process of granting or rejecting access
to data or resources. For example, your app requests a user's consent to access
the user's Google Drive.

Authentication and authorization calls must be two separate and distinct flows
based on the needs of the app.

> [!NOTE]
> **Note:** [Authorization support for Google Identity Services APIs](https://developers.googleblog.com/2022/02/announcing-authorization-support-for.html) was announced in February 2022. Previously you could request [access to additional scopes](https://developers.google.com/identity/sign-in/android/additional-scopes) during authentication flow.

If your app has features that can make use of Google API data, but are not
required as part of your app's core features, design your app to be able to
gracefully handle cases when API data isn't accessible. For example, you might
hide a list of recently saved files when the user hasn't granted Drive access.

You should request access to scopes that you need to access Google APIs only
when the user performs an action that requires access to a particular API. For
example, you should request permission to access the user's Drive whenever the
user taps a **Save to Drive** button.

By separating authorization from authentication, you can avoid overwhelming new
users, or confusing users as to why they are being asked for certain
permissions.

For authentication, we recommend using the [Credential Manager API](https://developer.android.com/identity/sign-in/credential-manager-siwg). For
authorizing actions that need access to user data stored by Google, we recommend
using [AuthorizationClient](https://developers.google.com/android/reference/com/google/android/gms/auth/api/identity/AuthorizationClient).

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
   9. (Optional) [Verify ownership](https://developer.android.com/identity/authorization#verify-app-ownership) of your Android application.
4. In the [Clients page](https://console.developers.google.com/auth/clients), create a new "Web application" client ID if you haven't already. You can ignore the "Authorized JavaScript Origins" and "Authorized redirect URIs" fields for now. This client ID will be used to identify your backend server when it communicates with Google's authentication services.
   1. Go to the [Clients page](https://console.developers.google.com/auth/clients).
   2. Click **Create client**.
   3. Select the **Web application** type.

### Verify app ownership

You can verify ownership of your application to reduce the risk of app
impersonation.

> [!NOTE]
> **Note:** Android app ownership verification is only available for Google Play apps.

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

In your module's `build.gradle` file, declare dependencies using the latest
version of the Google Identity Services library.

    dependencies {
      // ... other dependencies

      implementation "com.google.android.gms:play-services-auth:21.5.1"
    }

## Request permissions required by user actions

Whenever a user performs an action that requires additional scope, call
`AuthorizationClient.authorize()`. For example, if a user performs an action
that requires access to their Drive app storage, do the following:

### Kotlin

    val requestedScopes: List<Scope> = listOf(DriveScopes.DRIVE_FILE)
    val authorizationRequest = AuthorizationRequest.builder()
        .setRequestedScopes(requestedScopes)
        .build()

    Identity.getAuthorizationClient(activity)
        .authorize(authorizationRequestBuilder.build())
        .addOnSuccessListener { authorizationResult ->
            if (authorizationResult.hasResolution()) {
                val pendingIntent = authorizationResult.pendingIntent
                // Access needs to be granted by the user
                startAuthorizationIntent.launch(IntentSenderRequest.Builder(pendingIntent!!.intentSender).build())
            } else {
                // Access was previously granted, continue with user action
                saveToDriveAppFolder(authorizationResult);
            }
        }
        .addOnFailureListener { e -> Log.e(TAG, "Failed to authorize", e) }

### Java

    List<Scopes> requestedScopes = Arrays.asList(DriveScopes.DRIVE_FILE);
    AuthorizationRequest authorizationRequest = AuthorizationRequest.builder()
        .setRequestedScopes(requestedScopes)
        .build();

    Identity.getAuthorizationClient(activity)
        .authorize(authorizationRequest)
        .addOnSuccessListener(authorizationResult -> {
            if (authorizationResult.hasResolution()) {
                // Access needs to be granted by the user
                startAuthorizationIntent.launch(
                    new IntentSenderRequest.Builder(
                        authorizationResult.getPendingIntent().getIntentSender()
                    ).build()
                );
            } else {
                // Access was previously granted, continue with user action
                saveToDriveAppFolder(authorizationResult);
            }
        })
        .addOnFailureListener(e -> Log.e(TAG, "Failed to authorize", e));

When defining `ActivityResultLauncher`, handle the response as shown in the
following snippet, where we assume it is done in a fragment. The code checks
that the required permissions were successfully granted and then carries out
the user action.

### Kotlin

    private lateinit var startAuthorizationIntent: ActivityResultLauncher<IntentSenderRequest>

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?,
    ): View? {
        // ...
        startAuthorizationIntent =
            registerForActivityResult(ActivityResultContracts.StartIntentSenderForResult()) { activityResult ->
                try {
                    // extract the result
                    val authorizationResult = Identity.getAuthorizationClient(requireContext())
                        .getAuthorizationResultFromIntent(activityResult.data)
                    // continue with user action
                    saveToDriveAppFolder(authorizationResult);
                } catch (e: ApiException) {
                    // log exception
                }
            }
    }

### Java

    private ActivityResultLauncher<IntentSenderRequest> startAuthorizationIntent;

    @Override
    public View onCreateView(
        @NonNull LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
    // ...
    startAuthorizationIntent =
        registerForActivityResult(
            new ActivityResultContracts.StartIntentSenderForResult(),
            activityResult -> {
                try {
                // extract the result
                AuthorizationResult authorizationResult =
                    Identity.getAuthorizationClient(requireActivity())
                        .getAuthorizationResultFromIntent(activityResult.getData());
                // continue with user action
                saveToDriveAppFolder(authorizationResult);
                } catch (ApiException e) {
                // log exception
                }
            });
    }

If you are accessing Google APIs on the server side, call the
[`getServerAuthCode()`](https://developers.google.com/android/reference/com/google/android/gms/auth/api/identity/AuthorizationResult#public-string-getserverauthcode) method from [`AuthorizationResult`](https://developers.google.com/android/reference/com/google/android/gms/auth/api/identity/AuthorizationResult) to get an
authorization code which you send to your backend to exchange for an access and
refresh token. To learn more, see
[Maintain ongoing access to the user's data](https://developer.android.com/identity/authorization#maintain-access).

## Revoke permissions to user data or resources

To revoke previously granted access, call
[`AuthorizationClient.revokeAccess()`](https://developers.google.com/android/reference/com/google/android/gms/auth/api/identity/AuthorizationClient#public-abstract-taskvoid-revokeaccess-revokeaccessrequest-request). For example, if the user is removing
their account from your app, and your app was previously granted access to
`DriveScopes.DRIVE_FILE`, use the following code to revoke the access:

### Kotlin

    val requestedScopes: MutableList<Scope> = mutableListOf(DriveScopes.DRIVE_FILE)
    RevokeAccessRequest revokeAccessRequest = RevokeAccessRequest.builder()
        .setAccount(account)
        .setScopes(requestedScopes)
        .build()

    Identity.getAuthorizationClient(activity)
        .revokeAccess(revokeAccessRequest)
        .addOnSuccessListener { Log.i(TAG, "Successfully revoked access") }
        .addOnFailureListener { e -> Log.e(TAG, "Failed to revoke access", e) }

### Java

    List<Scopes> requestedScopes = Arrays.asList(DriveScopes.DRIVE_FILE);
    RevokeAccessRequest revokeAccessRequest = RevokeAccessRequest.builder()
        .setAccount(account)
        .setScopes(requestedScopes)
        .build();

    Identity.getAuthorizationClient(activity)
        .revokeAccess(revokeAccessRequest)
        .addOnSuccessListener(unused -> Log.i(TAG, "Successfully revoked access"))
        .addOnFailureListener(e -> Log.e(TAG, "Failed to revoke access", e));

> [!IMPORTANT]
> **Important:** Calling `revokeAccess()` revokes all scopes previously granted to the user for your application, not just those specified in the request. It also clears any locally cached tokens for that user. To regain access, the user must go through the authorization flow again.

## Clear the token cache

OAuth access tokens are locally cached upon receipt from the server, speeding up
access and reducing network calls. These tokens are automatically deleted from
the cache when they expire, but they can also become invalid for other reasons.
If you receive an `IllegalStateException` when using a token, clear the local
cache to make sure that the next authorization request for an access token goes
to the OAuth server. The following snippet removes the `invalidAccessToken` from
the local cache:

### Kotlin

    Identity.getAuthorizationClient(activity)
        .clearToken(ClearTokenRequest.builder().setToken(invalidAccessToken).build())
        .addOnSuccessListener { Log.i(TAG, "Successfully removed the token from the cache") }
        .addOnFailureListener{ e -> Log.e(TAG, "Failed to clear token", e) }

### Java

    Identity.getAuthorizationClient(activity)
        .clearToken(ClearTokenRequest.builder().setToken(invalidAccessToken).build())
        .addOnSuccessListener(unused -> Log.i(TAG, "Successfully removed the token from the cache"))
        .addOnFailureListener(e -> Log.e(TAG, "Failed to clear the token cache", e));

## Get user information during authorization

The authorization response does not contain any information about the user
account that was used; the response only contains a token for the requested
scopes. For example, the response for obtaining an access token to access a
user's Google Drive does not reveal the identity of the account that was
selected by the user even though it can be used to access files on the
user's drive. To get information such as the user's name or email, you have the
following options:

- Sign in the user with their Google Account using the
  [Credential Manager APIs](https://developer.android.com/identity/sign-in/credential-manager) before asking for authorization. The
  authentication response from Credential Manager includes user information
  such as the email address and also sets the app's default account to the
  selected account; if required, you can track this account in your app. A
  subsequent authorization request uses the account as the default and skips
  the account selection step in the authorization flow. To use a different
  account for authorization, see
  [Authorization from a non-default account](https://developer.android.com/identity/authorization#auth-non-default).

- In your authorization request, in addition to the scopes that you want (for
  example, the `Drive scope`), ask for the `userinfo`, `profile`, and `openid`
  scopes. After an access token is returned, get the user info by making a
  `GET` HTTP request to the OAuth userinfo endpoint
  (https://www.googleapis.com/oauth2/v3/userinfo) using your preferred HTTP
  library and including the access token that you had received in the header,
  equivalent to the following `curl` command:

      curl -X GET \ "https://www.googleapis.com/oauth2/v1/userinfo?alt=json" \ -H "Authorization: Bearer $TOKEN"

  The response is the [`UserInfo`](https://cloud.google.com/identity-platform/docs/reference/rest/v1/UserInfo), limited to the scopes that were
  requested, formatted in JSON.

### Authorization from a non-default account

If you use Credential Manager to authenticate, and run
[`AuthorizationClient.authorize()`](https://developers.google.com/android/reference/com/google/android/gms/auth/api/identity/AuthorizationClient#public-abstract-taskauthorizationresult-authorize-authorizationrequest-request), your app's default account is set to
the one selected by your user. This means that any subsequent calls for
authorization use this default account. To force showing the account selector,
sign out the user from the app using the [`clearCredentialState()`](https://developer.android.com/reference/androidx/credentials/CredentialManager#clearCredentialState(androidx.credentials.ClearCredentialStateRequest)) API from
Credential Manager.

## Maintain ongoing access to the user's data

If you need to access user's data from your app, call
[`AuthorizationClient.authorize()`](https://developers.google.com/android/reference/com/google/android/gms/auth/api/identity/AuthorizationClient#public-abstract-taskauthorizationresult-authorize-authorizationrequest-request) once; in subsequent sessions, and as
long as the granted permissions are not removed by the user, call the same
method to obtain an access token to achieve your objectives, without any user
interaction. If, on the other hand, you need to access the user's data in an
offline mode, from your backend server, then you need to request a different
type of token called "refresh token".

Access tokens are intentionally designed to be short-lived and have a lifespan
of one hour. If an access token is intercepted or compromised, its limited
validity window minimizes potential misuse. After its expiration, the token
becomes invalid, and any attempts to use it will be rejected by the resource
server. Since access tokens are short-lived, servers use refresh tokens to
maintain continued access to a user's data. Refresh tokens are tokens with a
long lifespan that are used by a client to request a short-lived access token
from the authorization server, when the old access token is expired, without any
user interaction.

To obtain a refresh token, you would need to first obtain an auth code
(or authorization code) during the authorization step in your app by asking for
"offline access", and then exchange the auth code for a refresh token on your
server. It is critical to store long-lived refresh tokens securely on your
server because they can be repeatedly used to obtain new access tokens.
Therefore, it is strongly discouraged to store refresh tokens on the device due
to security concerns. Instead, they should be stored in the app's backend
servers where the exchange for an access token takes place.

After the auth code is sent to your app's backend server, you can exchange it
for a short-lived access token on the server and a long-lived refresh token by
following the steps in the [account authorization guide](https://developers.google.com/identity/protocols/oauth2/web-server#exchange-authorization-code). This exchange
should only happen in the backend of your app.

### Kotlin

    // Ask for offline access during the first authorization request
    val authorizationRequest = AuthorizationRequest.builder()
        .setRequestedScopes(requestedScopes)
        .requestOfflineAccess(serverClientId)
        .build()

    Identity.getAuthorizationClient(activity)
        .authorize(authorizationRequest)
        .addOnSuccessListener { authorizationResult ->
            startAuthorizationIntent.launch(IntentSenderRequest.Builder(
                pendingIntent!!.intentSender
            ).build())
        }
        .addOnFailureListener { e -> Log.e(TAG, "Failed to authorize", e) }

### Java

    // Ask for offline access during the first authorization request
    AuthorizationRequest authorizationRequest = AuthorizationRequest.builder()
        .setRequestedScopes(requestedScopes)
        .requestOfflineAccess(serverClientId)
        .build();

    Identity.getAuthorizationClient(getContext())
        .authorize(authorizationRequest)
        .addOnSuccessListener(authorizationResult -> {
            startAuthorizationIntent.launch(
                new IntentSenderRequest.Builder(
                    authorizationResult.getPendingIntent().getIntentSender()
                ).build()
            );
        })
        .addOnFailureListener(e -> Log.e(TAG, "Failed to authorize"));

The following snippet assumes that the authorization is started from a fragment.

### Kotlin

    private lateinit var startAuthorizationIntent: ActivityResultLauncher<IntentSenderRequest>

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?,
    ): View? {
        // ...
        startAuthorizationIntent =
            registerForActivityResult(ActivityResultContracts.StartIntentSenderForResult()) { activityResult ->
                try {
                    val authorizationResult = Identity.getAuthorizationClient(requireContext())
                        .getAuthorizationResultFromIntent(activityResult.data)
                    // short-lived access token
                    accessToken = authorizationResult.accessToken
                    // store the authorization code used for getting a refresh token safely to your app's backend server
                    val authCode: String = authorizationResult.serverAuthCode
                    storeAuthCodeSafely(authCode)
                } catch (e: ApiException) {
                    // log exception
                }
            }
    }

### Java

    private ActivityResultLauncher<IntentSenderRequest> startAuthorizationIntent;

    @Override
    public View onCreateView(
        @NonNull LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        // ...
        startAuthorizationIntent =
            registerForActivityResult(
                new ActivityResultContracts.StartIntentSenderForResult(),
                activityResult -> {
                    try {
                        AuthorizationResult authorizationResult =
                            Identity.getAuthorizationClient(requireActivity())
                                .getAuthorizationResultFromIntent(activityResult.getData());
                        // short-lived access token
                        accessToken = authorizationResult.getAccessToken();
                        // store the authorization code used for getting a refresh token safely to your app's backend server
                        String authCode = authorizationResult.getServerAuthCode()
                        storeAuthCodeSafely(authCode);
                    } catch (ApiException e) {
                        // log exception
                    }
                });
    }