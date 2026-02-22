---
title: https://developer.android.com/identity/digital-credentials/credential-holder
url: https://developer.android.com/identity/digital-credentials/credential-holder
source: md.txt
---

# Credential Manager - Holder API

The Credential Manager - Holder API enables Android apps to manage and present digital credentials to verifiers.

## Get started

To use the Credential Manager - Holder API, add the following dependencies to your app module's build script:  

    // In your app module's build.gradle:
    dependencies {
        implementation(libs.androidx.registry.provider)
        implementation(libs.androidx.registry.provider.play.services)
    }

    // In libs.versions.toml:
    registryDigitalCredentials = "1.0.0-alpha02"

    androidx-registry-provider = { module = "androidx.credentials.registry:registry-provider", version.ref = "registryDigitalCredentials" }
    androidx-registry-provider-play-services = { module = "androidx.credentials.registry:registry-provider-play-services", version.ref = "registryDigitalCredentials" }

## Register credentials with Credential Manager

A wallet needs to register credential metadata so Credential Manager can filter and display them in the credential selector when a request comes in.
![Image showing the digital credentials UI in Credential Manager](https://developer.android.com/static/identity/digital-credentials/images/digital_credentials_ui.png)**Figure 1.**The digital credentials UI.

## The Credential Manager Selector UI

The format for this metadata is passed into a`RegisterCredentialsRequest`. Create a`[RegistryManager][1]`and register the credentials:

In this example, the metadata is compiled from a database of credentials entries. You can find a[reference in our sample wallet](https://github.com/digitalcredentialsdev/CMWallet/blob/main/app/src/main/java/com/credman/cmwallet/CmWalletApplication.kt#L74-L91)which registers the metadata on app load. In the future, credential database composition will be supported by the Jetpack API. At that point, you can register the credential metadata as well-defined data structures.

The registry persists across device reboots. Re-registering the same registry of the same ID + type overwrites the previous registry record. Therefore, re-register only when your credential data has changed.

### Optional: Create a matcher

Credential Manager is protocol-agnostic; it treats the metadata registry as an opaque blob and doesn't verify or check its contents. Therefore, the wallet has to provide a matcher, a runnable binary that can process the wallet's own data and generate the display metadata based on an incoming request. Credential Manager runs the matcher in a sandbox environment without network or disk access so that nothing leaks to a wallet before the UI is rendered to the user.

The Credential Manager API will provide matchers for popular protocols, today OpenID4VP. It is not officially released yet, so for now use our[sample matcher](https://github.com/digitalcredentialsdev/CMWallet/blob/main/app/src/main/assets/openid4vp1_0.wasm)for the[OpenID4VP protocol](https://openid.net/specs/openid-4-verifiable-presentations-1_0.html#name-format-identifier).

## Handle a selected credential

Next, the wallet needs to handle when a credential is selected by the user. You can define an Activity that listens to the`androidx.credentials.registry.provider.action.GET_CREDENTIAL`intent filter. Our sample wallet[demonstrates this procedure](https://github.com/digitalcredentialsdev/CMWallet/blob/9a0e1a713dc7559aaec6bf2c9583ab809b678cc9/app/src/main/AndroidManifest.xml#L26-L35).

The intent that launches the activity contains the Verifier request and calling origin, which you can[extract with the`PendingIntentHandler.retrieveProviderGetCredentialRequest`function](https://github.com/digitalcredentialsdev/CMWallet/blob/9a0e1a713dc7559aaec6bf2c9583ab809b678cc9/app/src/main/java/com/credman/cmwallet/getcred/GetCredentialActivity.kt#L153). The API returns a[`ProviderGetCredentialRequest`](https://developer.android.com/reference/androidx/credentials/provider/ProviderGetCredentialRequest)containing all the information associated with the verifier request. There are three key components:

- The app which made the request. You can retrieve this with[`getCallingAppInfo`](https://developer.android.com/reference/androidx/credentials/provider/ProviderGetCredentialRequest#getCallingAppInfo()).
- The selected credential. You can get information about which candidate the user has chosen through[the`selectedEntryId`extension method](https://developer.android.com/reference/androidx/credentials/registry/provider/ProviderGetCredentialRequest#(androidx.credentials.provider.ProviderGetCredentialRequest).getSelectedEntryId()); this will match the credential ID that you registered.
- Any specific requests that the verifier has made. You can get this from the[`getCredentialOptions`](https://developer.android.com/reference/androidx/credentials/provider/ProviderGetCredentialRequest#getCredentialOptions())method. In this case, you can expect to find a[`GetDigitalCredentialOption`](https://developer.android.com/reference/kotlin/androidx/credentials/GetDigitalCredentialOption)in this list, containing the Digital Credentials request.

Most commonly, the verifier makes a digital credential**presentation**request so you can process it with the following sample code:  

    request.credentialOptions.forEach { option ->
        if (option is GetDigitalCredentialOption) {
            Log.i(TAG, "Got DC request: ${option.requestJson}")
            processRequest(option.requestJson)
        }
    }

You can see an example of this in our[sample wallet](https://github.com/digitalcredentialsdev/CMWallet/blob/9a0e1a713dc7559aaec6bf2c9583ab809b678cc9/app/src/main/java/com/credman/cmwallet/getcred/GetCredentialActivity.kt#L172).

### Render the wallet UI

Once the credential is selected, the wallet is invoked and the user is taken through its UI. In the sample, this is a[biometric prompt](https://github.com/digitalcredentialsdev/CMWallet/blob/9a0e1a713dc7559aaec6bf2c9583ab809b678cc9/app/src/main/java/com/credman/cmwallet/getcred/GetCredentialActivity.kt#L299).

## Return the credential response

Once the wallet is ready to send back the result, you can do so by finishing the activity with the credential response:  

    PendingIntentHandler.setGetCredentialResponse(
        resultData,
        GetCredentialResponse(DigitalCredential(response.responseJson))
    )
    setResult(RESULT_OK, resultData)
    finish()

If there's an exception, you can similarly send the credential exception:  

    PendingIntentHandler.setGetCredentialException(
        resultData,
        GetCredentialUnknownException() // Configure the proper exception
    )
    setResult(RESULT_OK, resultData)
    finish()

Refer to the[sample app](https://github.com/digitalcredentialsdev/CMWallet/blob/9a0e1a713dc7559aaec6bf2c9583ab809b678cc9/app/src/main/java/com/credman/cmwallet/getcred/GetCredentialActivity.kt#L276-L282)for an example of how to return the credential response in context.