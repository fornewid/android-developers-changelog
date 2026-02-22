---
title: https://developer.android.com/identity/sign-in/single-tap-biometric
url: https://developer.android.com/identity/sign-in/single-tap-biometric
source: md.txt
---

On Android 15, Credential Manager supports a single tap flow for credential
creation and retrieval. In this flow, the information of the credential being
created, or being used, is displayed directly in the Biometric Prompt, along
with an entrypoint to more options. This simplified process creates a more
efficient and streamlined credential creation and retrieval process.

**Requirements:**

- Biometrics have been set up on the user's device and the user allows them for authentication into applications.
- For sign-in flows, this feature is enabled for single account scenarios only, even if there's multiple credentials (such as passkey and password) available for that account.

## Enable single tap on passkey creation flows

This method's creation steps match the [existing credential creation
process](https://developer.android.com/identity/sign-in/credential-provider#handle-passkey-creation). Within your `BeginCreatePublicKeyCredentialRequest`, use
`handleCreatePasskeyQuery()` to process the request if it is for a passkey.  

    is BeginCreatePublicKeyCredentialRequest -> {
        Log.i(TAG, "Request is passkey type")
        return handleCreatePasskeyQuery(request, passwordCount, passkeyCount)
    }

In your `handleCreatePasskeyQuery()`, include [`BiometricPromptData`](https://developer.android.com/reference/kotlin/androidx/credentials/provider/BiometricPromptData) with
the `CreateEntry` class:  

    val createEntry = CreateEntry(
        // Additional properties...
        biometricPromptData = BiometricPromptData(
            allowedAuthenticators = allowedAuthenticator
        ),
    )

Credential providers should explicitly set the `allowedAuthenticator` property
in the `BiometricPromptData` instance. If this property is not set, the value
defaults to `DEVICE_WEAK`. Set the optional `cryptoObject` property if needed
for your use case.
| **Note:** If the device is configured to use `DEVICE_CREDENTIALS` to require a PIN or passcode for authentication---regardless of whether biometrics are available or enabled---the standard credential manager flow will be used instead of the single-tap flow. This means the provider will always receive a `null` value for `biometricPromptResult` in these scenarios.

## Enable single tap on sign-in passkey flows

Similar to the passkey creation flow, this will follow the existing setup for
[handling user sign-in](https://developer.android.com/identity/sign-in/credential-provider#handle-user-sign-in). Under the `BeginGetPublicKeyCredentialOption`, use
`populatePasskeyData()` to gather the relevant information about the
authentication request:  

    is BeginGetPublicKeyCredentialOption -> {
        // ... other logic

        populatePasskeyData(
            origin,
            option,
            responseBuilder,
            autoSelectEnabled,
            allowedAuthenticator
        )

        // ... other logic as needed
    }

Similar to `CreateEntry`, a `BiometricPromptData` instance is set to the
`PublicKeyCredentialEntry` instance. If not explicitly set,
`allowedAuthenticator` defaults to `BIOMETRIC_WEAK`.  

    PublicKeyCredentialEntry(
        // other properties...

        biometricPromptData = BiometricPromptData(
            allowedAuthenticators = allowedAuthenticator
        )
    )

| **Note:** The user is presented with a biometric authentication option if their device supports it and they have granted permission for its use. The code is similar to the previous example, with the addition of a [`cryptoObject`](https://developer.android.com/reference/androidx/biometric/BiometricPrompt.CryptoObject).

## Handle credential entry selection

While handling the credential entry selection for [passkey creation](https://developer.android.com/identity/sign-in/credential-provider#handle-passkey-credential) or
[passkey selection during sign in](https://developer.android.com/identity/sign-in/credential-provider#passkeys-implement), call the `PendingIntentHandler's
retrieveProviderCreateCredentialRequest`, or
`retrieveProviderGetCredentialRequest`, as appropriate. These return objects
that contain the metadata needed for the provider. For example, when handling
passkey creation entry selection, update your code as shown:  

    val createRequest = PendingIntentHandler.retrieveProviderCreateCredentialRequest(intent)
    if (createRequest == null) {
        Log.i(TAG, "request is null")
        setUpFailureResponseAndFinish("Unable to extract request from intent")
        return
    }
    // Other logic...

    val biometricPromptResult = createRequest.biometricPromptResult

    // Add your logic based on what needs to be done
    // after getting biometrics

    if (createRequest.callingRequest is CreatePublicKeyCredentialRequest) {
        val publicKeyRequest: CreatePublicKeyCredentialRequest =
            createRequest.callingRequest as CreatePublicKeyCredentialRequest

        if (biometricPromptResult == null) {
            // Do your own authentication flow, if needed
        } else if (biometricPromptResult.isSuccessful) {
            createPasskey(
                publicKeyRequest.requestJson,
                createRequest.callingAppInfo,
                publicKeyRequest.clientDataHash,
                accountId
            )
        } else {
            val error = biometricPromptResult.authenticationError
            // Process the error
        }

        // Other logic...
    }

This example contains information about the biometric flow's success. It also
contains other information about the credential. If the flow fails, use the
error code under `biometricPromptResult.authenticationError` to make decisions.
The error codes returned as part of
`biometricPromptResult.authenticationError.errorCode` are the same error codes
defined in the androidx.biometric library, such as
[androidx.biometric.BiometricPrompt.NO_SPACE](https://developer.android.com/reference/androidx/biometric/BiometricPrompt#ERROR_NO_SPACE()),
[androidx.biometric.BiometricPrompt.UNABLE_TO_PROCESS](https://developer.android.com/identity/sign-in/androidx.biometric.BiometricPrompt.NO_SPACE),
[androidx.biometric.BiometricPrompt.ERROR_TIMEOUT](https://developer.android.com/reference/androidx/biometric/BiometricPrompt#ERROR_TIMEOUT()), and similar. The
`authenticationError` will also contain an error message associated with the
`errorCode` that can be displayed on a UI.

Similarly, extract metadata during the `retrieveProviderGetCredentialRequest`.
Check if your biometric flow is `null`. If yes, configure your own biometrics to
authenticate. This is similar to how the [get operation](https://developer.android.com/identity/sign-in/credential-provider#passkeys-implement) is instrumented:  

    val getRequest =
        PendingIntentHandler.retrieveProviderGetCredentialRequest(intent)

    if (getRequest == null) {
        Log.i(TAG, "request is null")
        setUpFailureResponseAndFinish("Unable to extract request from intent")
        return
    }

    // Other logic...

    val biometricPromptResult = getRequest.biometricPromptResult

    // Add your logic based on what needs to be done
    // after getting biometrics

    if (biometricPromptResult == null) {
        // Do your own authentication flow, if necessary
    } else if (biometricPromptResult.isSuccessful) {

        Log.i(TAG, "The response from the biometricPromptResult was ${biometricPromptResult.authenticationResult?.authenticationType}")

        validatePasskey(
            publicKeyRequest.requestJson,
            origin,
            packageName,
            uid,
            passkey.username,
            credId,
            privateKey
        )
    } else {
        val error = biometricPromptResult.authenticationError
        // Process the error
    }

    // Other logic...