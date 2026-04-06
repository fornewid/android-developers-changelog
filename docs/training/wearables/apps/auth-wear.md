---
title: https://developer.android.com/training/wearables/apps/auth-wear
url: https://developer.android.com/training/wearables/apps/auth-wear
source: md.txt
---

Wear OS apps can run standalone, without a companion app. This means that
a Wear OS app needs to manage authentication on its own when accessing
data from the internet. But the watch's small screen size and reduced
input capabilities limit the authentication options that a Wear OS app can use.

This guide provides directions for the recommended authentication method for
Wear OS apps, Credential Manager.

To learn more about how to design a good sign-in experience, view the
[Sign-in UX guide](https://developer.android.com/design/ui/wear/guides/behaviors-and-patterns/sign-in).

## Preliminary considerations

Before beginning your implementation, consider the following points.

### Guest mode

Don't require authentication for all functionality. Instead, provide as many
features as possible to the user without requiring them to sign in.

Users might discover and install your Wear app without having used the mobile
app, so they might not have an account and might not know what features it
offers. Make sure the guest mode functionality accurately showcases your app's
features.

### Some devices might stay unlocked longer

On supported devices that run Wear OS 5 or higher, the system detects whether
the user is wearing the device on their wrist. If the user turns off wrist
detection and then takes the device off of their wrist, the system keeps the
device unlocked for a longer period of time than it would otherwise.

If your app requires a higher level of security---such as when displaying
potentially sensitive or private data---first check whether wrist detection is
enabled:


```kotlin
fun isWristDetectionAutoLockingEnabled(context: Context): Boolean {
    // Use the keyguard manager to check for the presence of a lock mechanism
    val keyguardManager = context.getSystemService<KeyguardManager>()
    val isSecured = keyguardManager?.isDeviceSecure == true

    // Use OEM-specific system settings to verify that on-body autolock is enabled.
    val isWristDetectionOn = android.provider.Settings.Global.getInt(
        context.contentResolver, PIXEL_WRIST_AUTOLOCK_SETTING_STATE,
        0
    ) == 1

    return isSecured && isWristDetectionOn
}
```

<br />

If the return value of this method is `false`, prompt the user to sign into an
account in your app before displaying user-specific content.

## Credential Manager

[Credential Manager](https://developer.android.com/reference/android/credentials/CredentialManager) is the recommended API for
authentication on Wear OS.
It provides a more secure environment for users to sign in to Wear OS
applications in a standalone setting, without needing a connected paired phone
and without needing to remember their password.

This document outlines the information developers need to implement a
Credential Manager
solution with the standard authentication mechanisms it hosts, which are:

- Passkeys
- Passwords
- Federated Identities (such as Sign in with Google)

This guide also provides directions for how to migrate the other acceptable Wear
OS authentication methods ([Data Layer Token Sharing](https://developer.android.com/training/wearables/apps/auth-wear#tokens) and
[OAuth](https://developer.android.com/training/wearables/apps/auth-wear#oath)) as backups for Credential Manager, and special directions for
handling the transition from the now-deprecated standalone Google Sign in Button
to the embedded Credential Manager version.

### Wear OS limitations and differences

Developers should be mindful of the following limitations and differences on
Wear OS:

- Credential Manager is available on Wear OS 3 and higher.
- Credentials cannot be created on Wear OS
- Neither "restore credentials" nor hybrid sign-in flows are supported.
- Only Credential Providers with Wear OS integrations can be reused from mobile.

### Passkeys on Wear OS

Developers are strongly encouraged to implement passkeys in their Wear OS
Credential Manager implementations.
Passkeys are the new industry standard for end-user authentication, and they
carry several significant [benefits](https://developer.android.com/design/ui/mobile/guides/patterns/passkeys) for users.

#### Passkeys are easier

- Users can select an account to sign in with. They don't need to type a username.
- Users can authenticate using device's screen lock.
- After a passkey is created and registered, the user can seamlessly switch to a new device and immediately use it without needing to re-enroll.

#### Passkeys are safer

- Developers only save a public key to the server instead of saving a password, meaning there's far less value for a bad actor to hack into servers, and far less cleanup to do in the event of a breach.
- Passkeys provide phishing-resistant protection. Passkeys work only on their registered websites and apps; a user cannot be tricked into authenticating on a deceptive site because the browser or OS handles verification.
- Passkeys reduce the need of sending SMS, making authentication more cost-effective.

### Implement passkeys

Includes setup and guidance for all implementation types.

#### Setup

1. Set the target API level to 35 in your application module's build.gradle
   file:

       android {
           defaultConfig {
               targetSdk(35)
           }
       }

2. Add the following lines to the build.gradle file for your app or module,
   using the latest stable version from the
   [`androidx.credentials` releases](https://developer.android.com/jetpack/androidx/releases/credentials)
   reference.

       androidx.credentials:credentials:1.5.0
       androidx.credentials:credentials-play-services-auth:1.5.0

### Built-in authentication methods

As Credential Manager is a unified API, the implementation steps for Wear OS
are the same as any other device type.

Use the [mobile directions](https://developer.android.com/identity/sign-in/credential-manager#configure)
to get started and to implement passkeys and passwords support.

The steps to
[add Sign in With Google support to Credential Manager](https://developer.android.com/identity/sign-in/credential-manager-siwg#trigger-siwg)
are geared toward mobile development, but the steps are the same on Wear OS.

Note that since credentials cannot be created on Wear OS, you don't need to
implement the credential creation methods mentioned in the mobile instructions.

### Backup authentication methods

There are two other acceptable authentication methods for Wear OS apps: OAuth
2.0 (either variant), and Mobile Auth Token Data Layer Sharing. While these
methods don't have integration points in the Credential Manager API, they can be
included in your UX flow of Credential Manager as fallbacks in case users
dismiss the Credential Manager screen.

To handle the user action of dismissing the Credential Manager screen, catch a
[`NoCredentialException`](https://developer.android.com/reference/androidx/credentials/exceptions/NoCredentialException) as part of your
[`GetCredential`](https://developer.android.com/reference/androidx/credentials/CredentialManager#getCredential(android.content.Context,androidx.credentials.GetCredentialRequest))
logic, and navigate to your own custom auth UI.


```kotlin
try {
    val getCredentialResponse: GetCredentialResponse =
        credentialManager.getCredential(activity, createGetCredentialRequest())
    return authenticate(getCredentialResponse.credential)
} catch (_: GetCredentialCancellationException) {
    navigateToSecondaryAuthentication()
}
```

<br />

Your custom auth UI can then provide any of the other acceptable authentication
methods that are described in the [sign-in UX guide](https://developer.android.com/design/ui/wear/guides/behaviors-and-patterns/sign-in).

#### Data layer token sharing

The phone companion app can securely transfer authentication data to the Wear OS
app
using the Wearable Data Layer API. Transfer credentials as messages or
as data items.

This type of authentication typically doesn't require any action from the user.
However, avoid performing authentication without informing the user that they
are being signed in. You can inform the user using a dismissible screen
that shows them their account is being transferred from mobile.
> **Important:**
> Your Wear OS app must offer at least one other authentication method, because
> this
> option works only on Android-paired watches when the corresponding mobile app is
> installed. Provide an alternate authentication method for users who don't have
> the corresponding mobile app or whose Wear OS device is paired with an iOS
> device.

Pass tokens using the data layer from the mobile app, as shown in the following
example:


```kotlin
val token = "..." // Auth token to transmit to the Wear OS device.
val putDataReq: PutDataRequest = PutDataMapRequest.create("/auth").run {
    dataMap.putString("token", token)
    asPutDataRequest()
}
val putDataTask: Task<DataItem> = Wearable.getDataClient(this).putDataItem(putDataReq)
```

<br />

Listen for data change events on the Wear OS app, as shown in the following
example:


```kotlin
class AuthDataListenerService : WearableListenerService() {
    override fun onDataChanged(dataEvents: DataEventBuffer) {
        dataEvents.forEach { event ->
            if (event.type == DataEvent.TYPE_CHANGED) {
                val dataItemPath = event.dataItem.uri.path ?: ""

                if (dataItemPath.startsWith("/auth")) {
                    val token = DataMapItem.fromDataItem(event.dataItem)
                        .dataMap
                        .getString("token")
                    // Display an interstitial screen to notify the user that they're being signed
                    // in. Then, store the token and use it in network requests.
                    handleSignInSequence(token)
                }
            }
        }
    }

    /** placeholder sign in handler. */
    fun handleSignInSequence(token: String?) {}
}
```

<br />

For more information on using the Wearable Data Layer, see
[Send and sync data on Wear OS](https://developer.android.com/training/wearables/data-layer).

#### Use OAuth 2.0

Wear OS supports two OAuth 2.0-based flows, which are described in the sections
that follow:

- Authorization Code Grant with Proof Key for Code Exchange (PKCE), as defined in [RFC 7636](https://datatracker.ietf.org/doc/html/rfc7636)
- Device Authorization Grant (DAG), as defined in [RFC 8628](https://datatracker.ietf.org/doc/html/rfc8628)

> [!NOTE]
> **Note:** To minimize the chance that your app shuts down when the Wear OS device goes into ambient mode, enable Always-on by implementing [`AmbientLifecycleObserver`](https://developer.android.com/reference/kotlin/androidx/wear/ambient/AmbientLifecycleObserver) for your app. For more information about best practices in ambient mode, see [Always-on apps and system ambient mode](https://developer.android.com/training/wearables/always-on).

##### Proof Key for Code Exchange (PKCE)

To effectively use PKCE, use [`RemoteAuthClient`](https://developer.android.com/reference/kotlin/androidx/wear/phone/interactions/authentication/RemoteAuthClient).
Then, to perform an auth request from your Wear OS app to an OAuth provider,
create an [`OAuthRequest`](https://developer.android.com/reference/kotlin/androidx/wear/phone/interactions/authentication/OAuthRequest) object. This object consists
of a URL to your OAuth endpoint for getting a token and a
[`CodeChallenge`](https://developer.android.com/reference/kotlin/androidx/wear/phone/interactions/authentication/CodeChallenge) object.

The following code shows an example of creating an auth request:


```kotlin
val oauthRequest = OAuthRequest.Builder(context)
    .setAuthProviderUrl(uri)
    .setCodeChallenge(codeChallenge)
    .setClientId(CLIENT_ID)
    .build()
```

<br />

After you build the auth request, send it to the companion app using the
[`sendAuthorizationRequest()`](https://developer.android.com/reference/kotlin/androidx/wear/phone/interactions/authentication/RemoteAuthClient#sendAuthorizationRequest(androidx.wear.phone.interactions.authentication.OAuthRequest,java.util.concurrent.Executor,androidx.wear.phone.interactions.authentication.RemoteAuthClient.Callback)) method:


```kotlin
RemoteAuthClient.create(context).sendAuthorizationRequest(
    request = oauthRequest,
    executor = { command -> command?.run() },
    clientCallback = object : RemoteAuthClient.Callback() {
        override fun onAuthorizationResponse(
            request: OAuthRequest,
            response: OAuthResponse
        ) {
            // Extract the token from the response, store it, and use it in requests.
            continuation.resume(parseCodeFromResponse(response))
        }
        override fun onAuthorizationError(request: OAuthRequest, errorCode: Int) {
            // Handle Errors
            continuation.resume(Result.failure(IOException("Authorization failed")))
        }
    }
)
```

<br />

This request triggers a call to the companion app, which then presents an
authorization UI in a web browser on the user's mobile phone. The OAuth 2.0
provider authenticates the user and obtains the user's consent for the requested
permissions. The response is sent to the automatically generated redirect URL.

After a successful or failed authorization, the OAuth 2.0 server redirects to
the URL specified in the request. If the user approves the access request, then
the response contains an authorization code. If the user doesn't approve the
request, the response contains an error message.

The response is in the form of a query string and looks like one of the
following examples:

      https://wear.googleapis.com/3p_auth/com.your.package.name?code=xyz
      https://wear.googleapis-cn.com/3p_auth/com.your.package.name?code=xyz

This loads a page that directs the user to the companion app. The companion app
verifies the response URL and relays the response to your Wear OS app.
using the `onAuthorizationResponse` API.

The watch app can then exchange the authorization code for an access token.

> [!NOTE]
> **Note:** Once the `OAuthRequest` is built, you can find your redirect URL by accessing [`redirectUrl`](https://developer.android.com/reference/kotlin/androidx/wear/phone/interactions/authentication/OAuthRequest#redirectUrl()).

##### Device Authorization Grant

When using Device Authorization Grant, the user opens the verification URI on
another device. Then the authorization server asks them to approve or deny the
request.

To make this process easier, use a
[`RemoteActivityHelper`](https://developer.android.com/reference/androidx/wear/remote/interactions/RemoteActivityHelper) to open a web page on
the user's paired mobile device, as shown in the following example:


```kotlin
// Request access from the authorization server and receive Device Authorization Response.
private fun verifyDeviceAuthGrant(verificationUri: String) {
    RemoteActivityHelper(context).startRemoteActivity(
        Intent(Intent.ACTION_VIEW).apply {
            addCategory(Intent.CATEGORY_BROWSABLE)
            data = Uri.parse(verificationUri)
        },
        null
    )
}
```

<br />

If you have an iOS app, use [universal links](https://developer.apple.com/ios/universal-links/) to intercept this
intent in your app instead of relying on the browser to authorize the token.