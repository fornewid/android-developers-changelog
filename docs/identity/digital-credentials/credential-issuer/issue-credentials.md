---
title: https://developer.android.com/identity/digital-credentials/credential-issuer/issue-credentials
url: https://developer.android.com/identity/digital-credentials/credential-issuer/issue-credentials
source: md.txt
---

The Credential Manager API lets you issue credentials to Android holder (also
called "wallet") apps. This guide explains how to save credentials to a user's
preferred holder.

## Implementation

This section details the steps required to issue digital credentials.

### Add dependencies

Add the following dependencies to your gradle build script:

### Kotlin

```kotlin
dependencies {
    implementation("androidx.credentials:credentials:1.7.0-alpha02")
    implementation("androidx.credentials:credentials-play-services-auth:1.7.0-alpha02")
}
```

### Groovy

```groovy
dependencies {
    implementation "androidx.credentials:credentials:1.7.0-alpha02"
    implementation "androidx.credentials:credentials-play-services-auth:1.7.0-alpha02"
}
```

> [!NOTE]
> **Note:** You must add the `@ExperimentalDigitalCredentialApi` annotation to your classes or methods.

### Initialize Credential Manager

Initialize an instance of the `CredentialManager` class.

    val credentialManager = CredentialManager.create(context)

### Create an issuance request

The digital credential creation request should contain a JSON string that
follows the [OpenID4VCI](https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html) standard protocol. Here is an example of how an
OpenID4VCI request looks:

    "requests": [
      {
        "protocol": "openid4vci-v1",
        "data": {
          "credential_issuer": "https://digital-credentials.dev",
          "credential_configuration_ids": [
            "com.emvco.payment_card"
          ],
          "grants": {
            "urn:ietf:params:oauth:grant-type:pre-authorized_code": {
              "pre-authorized_code": "..."
            }
          }
        }
      }
    ]

Create a `CreateDigitalCredentialRequest` that contains the issuance request.

    val issuanceRequestJson = "{ ... }" // Your issuance JSON
    val createRequest = CreateDigitalCredentialRequest(
        requestJson = issuanceRequestJson,
        origin = null
    )

### Make the issuance request

Issue the credential to the user's holder using the `createCredential`
function. This function launches the Credential Manager bottom sheet selector
that lets the user to select the holder app they'd like the credential to be
stored in.

    try {
        val response = credentialManager.createCredential(
            context = context,
            request = createRequest
        )
        handleSuccess(response as CreateDigitalCredentialResponse)
    } catch (e: CreateCredentialException) {
        handleCreateException(e)
    }

### Handle the response

After you make the issuance request, a `CreateDigitalCredentialResponse` will be
returned. This response contains a `responseJson` string, which describes the
result of the issuance.

> [!NOTE]
> **Note:** Because some issuances involve asynchronous operations, the actual issuance of the credential may happen at a later time. A successful result only means that the holder has successfully received the request and indicated that your issuer app can continue with next steps.

    fun handleSuccess(response: CreateDigitalCredentialResponse) {
        val responseJson = response.responseJson
        // Parse responseJson according to your protocol (e.g. OpenID4VCI)
    }

### Handle exceptions

If the issuance flow fails, `createCredential` throws a
`CreateCredentialException`, which your app should handle:

    fun handleCreateException(e: CreateCredentialException) {
        when (e) {
            is CreateCredentialCancellationException -> {
                // The user canceled the flow
            }
            is CreateCredentialInterruptedException -> {
                // The flow was interrupted (e.g. by another UI element)
            }
            is CreateCredentialNoCreateOptionException -> {
                // No wallet application is available to handle the request
            }
            is CreateCredentialUnsupportedException -> {
                // The device or the system doesn't support this request
            }
            is CreateCredentialProviderConfigurationException -> {
                // There is a configuration issue with the wallet provider
            }
            is CreateCredentialCustomException -> {
                // A protocol-specific error occurred
                val errorType = e.type
                val errorMessage = e.message
            }
            is CreateCredentialUnknownException -> {
                // An unknown error occurred
            }
            else -> {
                // Generic error handling
            }
        }
    }