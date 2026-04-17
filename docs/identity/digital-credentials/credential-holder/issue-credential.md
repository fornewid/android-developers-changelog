---
title: Handle credential issuance with your holder app  |  Identity  |  Android Developers
url: https://developer.android.com/identity/digital-credentials/credential-holder/issue-credential
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [Security](https://developer.android.com/security)
* [Identity](https://developer.android.com/identity)
* [Guides](https://developer.android.com/identity/credential-manager)

# Handle credential issuance with your holder app Stay organized with collections Save and categorize content based on your preferences.





To receive and store credentials from issuers, your holder app needs to handle
issuance flows. In an issuance flow, the issuer website or app sends a
credential offer to the holder app detailing the information needed to provision
a credential. The holder app uses `RegistryManager` to register with Credential
Manager the credential types it intends to handle. This allows the app to be
displayed to and selected by the user during an issuance request to receive the
credential.

For more information about how credentials work with the Holder API, read the
[Holder API core concepts](/identity/digital-credentials/credential-holder/credential-holder#core-concepts).

### Android version compatibility

The Holder API is supported on Android 6 (API level 23) and higher.

## Implementation

To use the Credential Manager Holder API, add the following dependencies to your
app module's build script:

### Groovy

```
dependencies {
    // Use to implement credentials registrys

    implementation "androidx.credentials.registry:registry-digitalcredentials-mdoc:1.0.0-alpha04"
    implementation "androidx.credentials.registry:registry-digitalcredentials-openid:1.0.0-alpha04"
    implementation "androidx.credentials.registry:registry-digitalcredentials-sdjwtvc:1.0.0-alpha04"
    implementation "androidx.credentials.registry:registry-provider:1.0.0-alpha04"
    implementation "androidx.credentials.registry:registry-provider-play-services:1.0.0-alpha04"

}
```

### Kotlin

```
dependencies {
    // Use to implement credentials registrys

    implementation("androidx.credentials.registry:registry-digitalcredentials-mdoc:1.0.0-alpha04")
    implementation("androidx.credentials.registry:registry-digitalcredentials-openid:1.0.0-alpha04")
    implementation("androidx.credentials.registry:registry-digitalcredentials-sdjwtvc:1.0.0-alpha04")
    implementation("androidx.credentials.registry:registry-provider:1.0.0-alpha04")
    implementation("androidx.credentials.registry:registry-provider-play-services:1.0.0-alpha04")

}
```

### Create the RegistryManager

Create a `RegistryManager` instance and register a
`RegisterCreationOptionsRequest` request with it.

```
val registryManager = RegistryManager.create(context)

try {
    registryManager.registerCreationOptions(object :
        RegisterCreationOptionsRequest(
            creationOptions = buildIssuanceData(),
            matcher = loadIssuanceMatcher(),
            type = DigitalCredential.TYPE_DIGITAL_CREDENTIAL,
            id = "openid4vci",
        ) {}
    )
} catch (e: Exception) {
    Log.e(TAG, "Issuance registration failed.", e)
}
```

The matcher is a WebAssembly (Wasm) binary file that will receive the
`creationOptions` set during registration and the credential offer sent by the
issuer to determine the entries displayed on the Credential Manager UI. Refer to
the open source example [wallet app](https://github.com/digitalcredentialsdev/CMWallet/blob/71bf9086d196b05f4f85ff6badb975e5cbd7068d/app/src/main/java/com/credman/cmwallet/CmWalletApplication.kt#L97) for an example of a matcher.

### Handle an issuance request

Next, the wallet needs to handle when a credential creation option is selected
by the user. Define an activity that listens to the
`androidx.credentials.registry.provider.action.CREATE_CREDENTIAL` intent filter,
as demonstrated in the [sample wallet](https://github.com/digitalcredentialsdev/CMWallet/blob/9a0e1a713dc7559aaec6bf2c9583ab809b678cc9/app/src/main/AndroidManifest.xml#L36-L44).

The intent that launches the activity contains the creation request and calling
origin, which you can extract with the
`PendingIntentHandler.retrieveProviderCreateCredentialRequest` function. The API
returns a `ProviderCreateCredentialRequest` containing all information
associated with the creation request. There are two key components:

* The app that made the request. You can retrieve this with
  `getCallingAppInfo`.
* The request from the calling app. You can retrieve this with
  `getCallingRequest`, which returns a `CreateCredentialRequest`. If the request
  is for digital credentials, it is an instance of
  `CreateDigitalCredentialRequest`, which contains the issuance request JSON in
  the `requestJson` property. You can process that with the following sample code:

```
val pendingIntentRequest =
    PendingIntentHandler.retrieveProviderCreateCredentialRequest(intent)
val request = pendingIntentRequest!!.callingRequest
if (request is CreateDigitalCredentialRequest) {
    Log.i(TAG, "Got DC creation request: ${request.requestJson}")
    processCreationRequest(request.requestJson)
}
```

### Return the creation response

Once the wallet finishes the steps needed to save the credential, finish the
activity with the credential response:

```
val resultData = Intent()
PendingIntentHandler.setCreateCredentialResponse(
    resultData,
    CreateDigitalCredentialResponse(response.responseJson)
)
setResult(RESULT_OK, resultData)
finish()
```

If there is an exception, you can similarly send the credential exception:

```
val resultData = Intent()
PendingIntentHandler.setCreateCredentialException(
    resultData,
    CreateCredentialUnknownException() // Configure the proper exception
)
setResult(RESULT_OK, resultData)
finish()
```

To see a full example of returning the credential response in context, see the
[sample app](https://github.com/digitalcredentialsdev/CMWallet/blob/7f6fe62d208f2a88ea531925c22f9e4eccc403f6/app/src/main/java/com/credman/cmwallet/createcred/CreateCredentialActivity.kt#L212).