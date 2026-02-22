---
title: https://developer.android.com/identity/digital-credentials
url: https://developer.android.com/identity/digital-credentials
source: md.txt
---

# Overview of digital credentials

Digital credentials are cryptographically verifiable documents that can be used to authenticate, authorize, or otherwise provide information about a user. These are typically things such as mobile driver's licenses, digital passports, boarding passes, etc. They reside in virtual containers called digital wallets, and are part of a W3C standard that specifies how to access and retrieve them. This standard is implemented for web use cases with the[W3C Credential Management API](https://www.w3.org/TR/credential-management-1/)and on Android, with Credential Manager's[DigitalCredential API](https://developer.android.com/reference/kotlin/androidx/credentials/DigitalCredential).

## Understand digital credentials

In the physical world, a person might keep their identity in their wallet, and present it to a requesting party when asked:
![Image showing the flow of a normal wallet interaction](https://developer.android.com/static/identity/digital-credentials/images/normal_wallet_flowchart.svg)**Figure 1.**The process of fulfilling a physical-world credential request. The requestor asks the user for a specific credential. Then, the user selects and retrieves it from their physical wallet. Finally, the user provides the credential to the requestor.

In this case, a user generally has a single wallet, and retrieves the requested credential(s) from the wallet to present to the requestor. Wallets are mostly interchangeable, and can generally store the same things.

Digital credentials have a few main differences:

1. Users are expected to have multiple wallets which can contain various different credentials. Wallets determine which credentials may be stored inside of them.
2. The requestor is now an application rather than a real person, and is referred to as a verifier.
3. The credential presentation happens in software, which means an API surface retrieves and presents the credentials - in Android, this is Credential Manager.

As such, Credential Manager takes on several roles that were formerly handled by the user:

1. On Android, Wallets must register their credentials metadata with Credential Manager to be listed in the Credential Manager UI.
2. Credential Manager matches credentials across wallets based on the request and presents a list for the user to select.
3. When the user selects a credential in the list, Credential Manager then invokes the wallet, which will handle the remainder of the transaction (showing UIs, etc.) and return the credential to the application.

This flow is shown here:
![Image showing the flow of a digital credential interaction](https://developer.android.com/static/identity/digital-credentials/images/digital_credentials_flowchart.svg)**Figure 2.**Interaction model for digital credential verification. Credential Manager uses pre-registered credentials metadata across user wallet(s) to match a verifier's request and prompts the user to select a credential. Credential Manager then directs the activity flow to the corresponding wallet which handles the remainder of the transaction and returns the credential to the verifier. Note: The verifier needs to handle and verify the credential response once it is returned.

### User experience

As shown in the Android flow, the user only needs to interact once with the Credential Manager UI to select the appropriate credential. Here is an example of how the selector looks:
![Image showing the digital credentials UI in Credential Manager](https://developer.android.com/static/identity/digital-credentials/images/digital_credentials_ui.png)**Figure 3.**The digital credentials UI.

### Standards

Digital credentials requests are created using the[OpenID4VP standard](https://openid.net/specs/openid-4-verifiable-presentations-1_0.html#name-introduction). You can see example requests at the[Digital Credentials Demo site](https://digital-credentials.dev/).

Digital credential responses are typically returned in a standardized credential format. These are maintained by different standards bodies, and include[W3C Verifiable Credentials](https://www.w3.org/TR/vc-data-model-2.0/),[sd-jwt](https://datatracker.ietf.org/doc/draft-ietf-oauth-selective-disclosure-jwt/), and[mdoc](https://www.iso.org/standard/69084.html).

Custom protocols are also feasible, though we recommend using one of the standard protocols in your application.

### Try it out

You can test out the digital credentials flow across platforms with an Android wallet and web-based verifier:

1. Install the[CMWallet public sample](https://github.com/digitalcredentialsdev/CMWallet)on your Android phone. You can do this by pulling from the repository and installing directly from Android Studio or navigating to<https://github.com/digitalcredentialsdev/CMWallet/actions>and selecting the latest build to access the latest`app-debug.apk`file.
2. Open the CMWallet to register the metadata with Credential Manager. Make sure Bluetooth is enabled to allow your devices to connect to each other.
3. Navigate to<https://digital-credentials.dev/>and select`Request Credentials (OpenID4VP)`.
4. Accept the warning prompts and scan the QR Code with your phone, then select "Use passkey" and tap through the confirmation to show the available credentials.
5. Select the credential from CMWallet to return to the browser. The browser should show the returned credential.

### See also

- To learn more about using Credential Manager to request digital credentials in your app, read the[Credential Manager - Verifier API](https://developer.android.com/identity/digital-credentials/credential-verifier)page.
- To learn more about building a digital wallet using Credential Manager, read the[Credential Manager - Holder API](https://developer.android.com/identity/digital-credentials/credential-holder)page.