---
title: https://developer.android.com/identity/autofill/credential-manager-autofill
url: https://developer.android.com/identity/autofill/credential-manager-autofill
source: md.txt
---

Starting with Android 15 Beta 2, paired with
[androidx.credentials:1.5.0-alpha01](https://developer.android.com/jetpack/androidx/releases/credentials#version_15_2), developers can link specific views like
username or password fields with Credential Manager requests. When the user
focuses on one of these views, the corresponding request is sent to Credential
Manager. The resulting credentials are aggregated across providers and displayed
in autofill UIs, such as keyboard inline suggestions, or drop-down suggestions.
This feature can be used as a fallback when users accidentally dismiss the
Credential Manager account selector and then tap on the relevant fields.

The ***Jetpack androidx.credentials*** library is the preferred endpoint for
developers to use for this feature.

![Illustration showing credentials in autofill results](https://developer.android.com/static/identity/sign-in/images/credman-autofill.svg)  

**Figure 1:** Autofill results with credentials using password, passkey, and
Sign in with Google.
| **Note:** This feature is only available for `View` objects at this time.

## Implementation

To use Credential Manager to show credentials in autofill results, use the
[standard implementation](https://developer.android.com/identity/sign-in/credential-manager) to build a `GetCredentialRequest` and then set it
to the relevant views. The response handling is the same, whether the response
comes from the `getCredential` API call or the `PendingGetCredentialRequest`, as
shown in the following example.

First, construct a `GetCredentialRequest`:  

    // Retrieves the user's saved password for your app.
    val getPasswordOption = GetPasswordOption()

    // Get a passkey from the user's public key credential provider.
    val getPublicKeyCredentialOption = GetPublicKeyCredentialOption(
        requestJson = requestJson
    )

    val getCredRequest = GetCredentialRequest(
        listOf(getPasswordOption, getPublicKeyCredentialOption)
    )

Next, call the `getCredential` API. This displays the Credential Manager
selector.  

    coroutineScope {
        try {
            val result = credentialManager.getCredential(
                context = activityContext, // Use an activity-based context.
                request = getCredRequest
            )
            handleSignIn(result)
        } catch (e: GetCredentialException) {
            handleFailure(e)
        }
    }

Finally, enable the autofill experience. Set the `getCredRequest` to relevant
views (such as `username, password`) to enable credential results in autofill
when the user interacts with these views.
**Note:** The `setPendingGetCredentialRequest` is an *extension API* in the androidx.credentials library, and is called differently between Kotlin and Java.  

    usernameEditText.pendingGetCredentialRequest = PendingGetCredentialRequest(
        getCredRequest
    ) { response ->
        handleSignIn(response)
    }

    passwordEditText.pendingGetCredentialRequest = PendingGetCredentialRequest(
        getCredRequest
    ) { response ->
        handleSignIn(response)
    }